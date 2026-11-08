import com.google.gson.Gson;
import com.google.gson.stream.JsonWriter;
import ghidra.app.util.headless.HeadlessScript;
import ghidra.program.model.address.*;
import ghidra.program.model.block.*;
import ghidra.program.model.listing.*;
import ghidra.program.model.pcode.*;
import ghidra.program.model.symbol.*;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.security.MessageDigest;
import java.util.*;
import java.util.zip.GZIPOutputStream;

public class ExportStructure extends HeadlessScript {
    private final Gson gson = new Gson();

    private void row(JsonWriter out, Writer stream, Map<String, ?> data) throws IOException {
        gson.toJson(data, Map.class, out);
        stream.write('\n');
    }

    private String storage(Varnode node) {
        if (node == null) return null;
        return node.getAddress().getAddressSpace().getName() + ":" +
            Long.toUnsignedString(node.getOffset(), 16) + ":" + node.getSize();
    }

    private void rangeList(JsonWriter out, AddressSetView body) throws IOException {
        out.beginArray();
        for (AddressRange range : body.getAddressRanges()) {
            out.beginArray().value(range.getMinAddress().toString())
                .value(range.getMaxAddress().toString()).endArray();
        }
        out.endArray();
    }

    private void blocks(JsonWriter out, BasicBlockModel model, AddressSetView body) throws Exception {
        out.beginArray();
        CodeBlockIterator blocks = model.getCodeBlocksContaining(body, monitor);
        while (blocks.hasNext()) {
            monitor.checkCancelled();
            CodeBlock block = blocks.next();
            out.beginArray().value(block.getFirstStartAddress().toString());
            rangeList(out, block.intersect(body));
            out.beginArray();
            CodeBlockReferenceIterator edges = block.getDestinations(monitor);
            while (edges.hasNext()) {
                CodeBlockReference edge = edges.next();
                if (edge.getFlowType().isCall()) continue;
                out.beginArray().value(edge.getFlowType().toString()).value(edge.getReferent().toString())
                    .value(edge.getReference().toString()).endArray();
            }
            out.endArray().endArray();
        }
        out.endArray();
    }

    private void references(JsonWriter out, AddressSetView body) throws Exception {
        out.beginArray();
        ReferenceManager refs = currentProgram.getReferenceManager();
        FunctionManager functions = currentProgram.getFunctionManager();
        AddressIterator locations = refs.getReferenceSourceIterator(body, true);
        while (locations.hasNext()) {
            monitor.checkCancelled();
            for (Reference ref : refs.getReferencesFrom(locations.next())) {
                RefType type = ref.getReferenceType();
                Address target = ref.getToAddress();
                Function callee = functions.getFunctionAt(target);
                Symbol symbol = currentProgram.getSymbolTable().getPrimarySymbol(target);
                String name = symbol == null || symbol.getSource() == SourceType.DEFAULT ? null : symbol.getName(true);
                Data data = target.isMemoryAddress() ? currentProgram.getListing().getDefinedDataContaining(target) : null;
                out.beginArray().value(ref.getFromAddress().toString()).value(target.toString())
                    .value(type.toString()).value(ref.getSource().toString())
                    .value(callee == null ? null : callee.getEntryPoint().toString())
                    .value(name).value(data == null ? null : data.getDataType().getDisplayName()).endArray();
            }
        }
        out.endArray();
    }

    private void function(JsonWriter out, Writer stream, BasicBlockModel model, Function function) throws Exception {
        AddressSetView body = function.getBody();
        out.beginObject().name("type").value("function").name("address").value(function.getEntryPoint().toString())
            .name("source").value(function.getSymbol().getSource().toString()).name("thunk").value(function.isThunk())
            .name("ranges");
        rangeList(out, body);
        out.name("blocks");
        blocks(out, model, body);
        out.name("refs");
        references(out, body);
        out.name("instructions").beginArray();
        MessageDigest bytes = MessageDigest.getInstance("SHA-256");
        InstructionIterator instructions = currentProgram.getListing().getInstructions(body, true);
        int count = 0, indirect = 0, unresolved = 0;
        long length = 0;
        while (instructions.hasNext()) {
            monitor.checkCancelled();
            Instruction instruction = instructions.next();
            bytes.update(instruction.getBytes());
            length += instruction.getLength();
            FlowType flow = instruction.getFlowType();
            if (flow.isComputed() && (flow.isCall() || flow.isJump())) {
                indirect++;
                if (instruction.getFlows().length == 0) unresolved++;
            }
            out.beginArray().value(instruction.getAddress().toString()).value(instruction.getMnemonicString())
                .value(flow.toString()).beginArray();
            for (PcodeOp operation : instruction.getPcode()) {
                out.beginArray().value(operation.getMnemonic()).value(storage(operation.getOutput())).beginArray();
                for (Varnode input : operation.getInputs()) out.value(storage(input));
                out.endArray().endArray();
            }
            out.endArray().endArray();
            count++;
        }
        out.endArray().name("bytes_sha256").value(HexFormat.of().formatHex(bytes.digest()))
            .name("instruction_count").value(count).name("instruction_bytes").value(length)
            .name("body_bytes").value(body.getNumAddresses()).name("indirect").value(indirect)
            .name("unresolved").value(unresolved).endObject();
        stream.write('\n');
    }

    @Override
    public void run() throws Exception {
        Path root = Path.of(getScriptArgs()[0]);
        String sha = currentProgram.getExecutableSHA256().toLowerCase(Locale.ROOT);
        if (!sha.equals(getScriptArgs()[2]) || analysisTimeoutOccurred() ||
                !currentProgram.getOptions(Program.PROGRAM_INFO).getBoolean(Program.ANALYZED_OPTION_NAME, false)) {
            throw new IOException("Structure export requires the verified, fully analyzed program");
        }
        Path partial = root.resolve("structure.jsonl.gz.partial");
        long start = System.nanoTime();
        int count = 0;
        BasicBlockModel model = new BasicBlockModel(currentProgram);
        try (Writer stream = new BufferedWriter(new OutputStreamWriter(
                new GZIPOutputStream(Files.newOutputStream(partial), 65536), StandardCharsets.UTF_8), 65536)) {
            JsonWriter out = new JsonWriter(stream);
            out.setStrictness(com.google.gson.Strictness.LENIENT);
            row(out, stream, Map.of("type", "program", "schema", 1, "sha256", sha,
                "language", currentProgram.getLanguageID().toString(), "image_base", currentProgram.getImageBase().toString(),
                "ghidra", ghidra.framework.Application.getApplicationVersion()));
            FunctionIterator functions = currentProgram.getFunctionManager().getFunctions(true);
            while (functions.hasNext()) {
                function(out, stream, model, functions.next());
                count++;
            }
            row(out, stream, Map.of("type", "complete", "functions", count, "seconds", (System.nanoTime()-start)/1e9));
            out.flush();
        }
        Files.move(partial, root.resolve("structure.jsonl.gz"), StandardCopyOption.REPLACE_EXISTING);
        println("Structure export complete: " + count);
    }
}
