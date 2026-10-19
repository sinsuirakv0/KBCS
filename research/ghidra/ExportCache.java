import ghidra.app.util.headless.HeadlessScript;
import ghidra.app.decompiler.*;
import ghidra.program.model.listing.*;
import ghidra.program.model.symbol.*;
import ghidra.program.model.address.*;
import com.google.gson.Gson;
import java.nio.file.*;
import java.nio.charset.StandardCharsets;
import java.nio.ByteBuffer;
import java.nio.charset.CodingErrorAction;
import java.io.*;
import java.util.*;

public class ExportCache extends HeadlessScript {
    private final Gson gson = new Gson();
    private Map<String,Object> row(Object... pairs) {
        Map<String,Object> result = new LinkedHashMap<>();
        for (int i=0; i<pairs.length; i+=2) result.put((String)pairs[i], pairs[i+1]);
        return result;
    }
    private void emit(BufferedWriter writer, Object value) throws IOException {
        writer.write(gson.toJson(value)); writer.newLine();
    }
    private String key(Address address) { return address.toString(); }
    private String relatedString(Address address) {
        try {
            Data data=currentProgram.getListing().getDefinedDataContaining(address);
            if(data!=null && data.hasStringValue()) return String.valueOf(data.getValue());
            ghidra.program.model.mem.MemoryBlock block=currentProgram.getMemory().getBlock(address);
            if(block==null || block.isExecute() || !block.isInitialized()) return null;
            int size=(int)Math.min(256,block.getEnd().subtract(address)+1);
            if(size<5) return null;
            byte[] bytes=new byte[size];
            currentProgram.getMemory().getBytes(address,bytes);
            boolean wide=bytes[1]==0;
            int step=wide ? 2 : 1, length=0;
            while(length+step<=size && !(bytes[length]==0 && (!wide || bytes[length+1]==0))) length+=step;
            if(length<4 || length+step>size) return null;
            String value=(wide ? StandardCharsets.UTF_16LE : StandardCharsets.UTF_8).newDecoder()
                .onMalformedInput(CodingErrorAction.REPORT).onUnmappableCharacter(CodingErrorAction.REPORT)
                .decode(ByteBuffer.wrap(bytes,0,length)).toString();
            if(value.trim().length()<2) return null;
            for(int i=0;i<value.length();i++) {
                char ch=value.charAt(i);
                if(Character.isISOControl(ch) && ch!='\n' && ch!='\r' && ch!='\t') return null;
            }
            return value;
        } catch(Exception exception) { return null; }
    }
    public void run() throws Exception {
        String[] args = getScriptArgs();
        Path root = Paths.get(args[0]);
        String mode = args[1];
        Files.createDirectories(root);
        Path identityFile=root.resolve("identity.json");
        if(Files.exists(identityFile)) {
            try(Reader reader=Files.newBufferedReader(identityFile,StandardCharsets.UTF_8)) {
                Map<?,?> identity=gson.fromJson(reader,Map.class);
                if(!currentProgram.getExecutableSHA256().equalsIgnoreCase((String)identity.get("sha256")))
                    throw new IOException("Program SHA-256 mismatch");
            }
        }
        long started = System.nanoTime();
        FunctionManager manager = currentProgram.getFunctionManager();
        if (mode.equals("index")) {
            started=System.nanoTime();
            Path partial = root.resolve("index.jsonl.partial");
            int count=0;
            try (BufferedWriter writer=Files.newBufferedWriter(partial, StandardCharsets.UTF_8)) {
                writer.write('\ufeff');
                emit(writer, row("type","program","sha256",currentProgram.getExecutableSHA256(),
                    "library",currentProgram.getName(),"language",currentProgram.getLanguageID().toString(),
                    "image_base",key(currentProgram.getImageBase()),"ghidra",ghidra.framework.Application.getApplicationVersion(),
                    "function_count",manager.getFunctionCount(),"executable",currentProgram.getExecutablePath(),
                    "analysis_timed_out",analysisTimeoutOccurred(),
                    "analysis_marked_complete",currentProgram.getOptions(Program.PROGRAM_INFO).getBoolean(Program.ANALYZED_OPTION_NAME,false),
                    "string_extraction","defined-data-or-bounded-readonly-utf8-utf16le"));
                for(FunctionIterator functions : new FunctionIterator[]{manager.getFunctions(true),manager.getExternalFunctions()}) {
                  while(functions.hasNext()) {
                    monitor.checkCancelled();
                    Function function=functions.next();
                    String entry=key(function.getEntryPoint());
                    emit(writer,row("type","function","address",entry,"name",function.getName(true),
                        "size",function.getBody().getNumAddresses(),"external",function.isExternal(),
                        "thunk",function.isThunk(),"name_source",function.getSymbol().getSource().toString(),
                        "confidence","unreviewed"));
                    AddressIterator sources=currentProgram.getReferenceManager().getReferenceSourceIterator(function.getBody(),true);
                    while(sources.hasNext()) {
                        Address source=sources.next();
                        for(Reference reference:currentProgram.getReferenceManager().getReferencesFrom(source)) {
                            Address target=reference.getToAddress();
                            Function callee=manager.getFunctionAt(target);
                            String value=relatedString(target);
                            emit(writer,row("type","reference","function",entry,"source",key(source),
                                "target",key(target),"kind",reference.getReferenceType().toString(),
                                "call",reference.getReferenceType().isCall(),
                                "callee",callee==null ? null : key(callee.getEntryPoint()),"string",value));
                        }
                    }
                    count++;
                  }
                }
                if(count!=manager.getFunctionCount()) throw new IOException("Function count mismatch: "+count);
                emit(writer,row("type","complete","functions",count,"seconds",(System.nanoTime()-started)/1e9));
            }
            Files.move(partial,root.resolve("index.jsonl"),StandardCopyOption.REPLACE_EXISTING);
            println("Cache index: "+count+" functions");
        } else if(mode.equals("decompile")) {
            int timeout=Integer.parseInt(args[2]);
            String style=args.length>3 ? args[3] : "decompile";
            if(!Set.of("decompile","conservative","minimal").contains(style)) throw new IOException("Invalid decompiler style");
            DecompInterface decompiler=new DecompInterface();
            decompiler.setSimplificationStyle("decompile");
            if(!style.equals("decompile")) {
                DecompileOptions options=new DecompileOptions();
                options.setEliminateUnreachable(style.equals("minimal"));
                if(style.equals("minimal")) options.setRespectReadOnly(false);
                options.setSimplifyDoublePrecision(false);
                options.setPredicate(false);
                options.setInferConstantPointers(false);
                options.setSplitStructures(false);
                options.setSplitArrays(false);
                options.setSplitPointers(false);
                decompiler.setOptions(options);
            }
            decompiler.toggleSyntaxTree(false);
            try {
                if(!decompiler.openProgram(currentProgram)) throw new IOException(decompiler.getLastMessage());
                Path codeRoot=root.resolve("code"); Files.createDirectories(codeRoot);
                Path fallbackRoot=root.resolve("assembly"); Files.createDirectories(fallbackRoot);
                Path journal=root.resolve("results.jsonl");
                if(Files.exists(journal) && Files.size(journal)>0) {
                    try(RandomAccessFile tail=new RandomAccessFile(journal.toFile(),"rw")) {
                        tail.seek(tail.length()-1);
                        if(tail.read()!=10) { tail.seek(tail.length()); tail.write(10); }
                    }
                }
                try(BufferedWriter writer=Files.newBufferedWriter(root.resolve("results.jsonl"),StandardCharsets.UTF_8,StandardOpenOption.CREATE,StandardOpenOption.APPEND)) {
                    int processed=0;
                    for(String address:Files.readAllLines(root.resolve("requests.txt"),StandardCharsets.UTF_8)) {
                        monitor.checkCancelled();
                        Function function=manager.getFunctionAt(toAddr(address));
                        long tick=System.nanoTime();
                        String status="failed", error="function not found", filename="";
                        String cachedFile="code/"+address.replaceAll("[^a-zA-Z0-9_-]","_")+".c";
                        if(Files.isRegularFile(root.resolve(cachedFile))) {
                            emit(writer,row("address",address,"status","cached","error","recovered file",
                                "file",cachedFile,"seconds",0));
                            writer.flush();
                            continue;
                        }
                        if(function!=null) {
                            try {
                                if(function.getBody().getNumAddresses()>16384)
                                    println("Cache large function: "+address+" bytes="+function.getBody().getNumAddresses());
                                DecompileResults result=decompiler.decompileFunction(function,timeout,monitor);
                                error=result.getErrorMessage();
                                DecompiledFunction output=result.getDecompiledFunction();
                                if(output!=null && !result.failedToStart() && !result.isTimedOut() && !result.isCancelled()) {
                                    filename="code/"+address.replaceAll("[^a-zA-Z0-9_-]","_")+".c";
                                    Path target=root.resolve(filename), temp=root.resolve(filename+".partial");
                                    String code=output.getC();
                                    if(code.isBlank()) throw new IOException("Empty decompiled output");
                                    if(code.chars().anyMatch(ch->ch>127)) code="\ufeff"+code;
                                    Files.writeString(temp,code,StandardCharsets.UTF_8);
                                    Files.move(temp,target,StandardCopyOption.REPLACE_EXISTING);
                                    status="cached";
                                    if(!style.equals("decompile")) error="Recovered with "+style+"; "+(error==null ? "" : error);
                                }
                            } catch(Exception exception) { error=exception.toString(); }
                            if(status.equals("failed")) {
                                if(error==null || error.isBlank()) error="No C output returned";
                                filename="assembly/"+address.replaceAll("[^a-zA-Z0-9_-]","_")+".asm";
                                Path target=root.resolve(filename), temp=root.resolve(filename+".partial");
                                try(BufferedWriter assembly=Files.newBufferedWriter(temp,StandardCharsets.UTF_8)) {
                                    InstructionIterator instructions=currentProgram.getListing().getInstructions(function.getBody(),true);
                                    while(instructions.hasNext()) {
                                        monitor.checkCancelled();
                                        Instruction instruction=instructions.next();
                                        assembly.write(key(instruction.getAddress())+"  "+instruction.toString());
                                        assembly.newLine();
                                    }
                                }
                                Files.move(temp,target,StandardCopyOption.REPLACE_EXISTING);
                            }
                        }
                        emit(writer,row("address",address,"status",status,"error",error,"file",filename,
                            "seconds",(System.nanoTime()-tick)/1e9,"style",style,"syntax_tree",false));
                        writer.flush();
                        if(++processed%250==0) {
                            decompiler.flushCache();
                            println("Cache processed: "+processed);
                        }
                    }
                }
            } finally { decompiler.dispose(); }
            println("Cache decompilation complete");
        } else throw new IllegalArgumentException("Unknown mode: "+mode);
    }
}
