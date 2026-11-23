# 00aeaeb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeaf78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aea/00aeaf78.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-d4c418725822443b4f237697d8f9ec75)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeaeb0",
  "name": "_ZN8firebase4util8hash_map13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8b9b8f1caa2109d509b8eca92a674a9d1680675e2c94ed89f205ca3904e40a70",
  "source_text_sha256": "8b9b8f1caa2109d509b8eca92a674a9d1680675e2c94ed89f205ca3904e40a70",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeaeb0",
        "00aeaf1f"
      ]
    ],
    "bytes_sha256": "4940b59119ec9b96212ef7ab48a14640a2691d2c3bfc68498838a120e2edd2c1",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bddf70](../00bdd/00bddf70.md)
- [00bddf90](../00bdd/00bddf90.md)

## 関連文字列（未確認候補）

~~~text
"java/util/HashMap"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 592 bytes

~~~c

void _ZN8firebase4util8hash_map13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0750 == 0) {
    DAT_010a0750 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/HashMap",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a0750,&DAT_002f5cc8,1,&DAT_010a0768,"java/util/HashMap");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeaeb0"></a> `00aeaeb0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeaeb4"></a> `00aeaeb4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaeb8"></a> `00aeaeb8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeaebc"></a> `00aeaebc` | `b4 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaec0"></a> `00aeaec0` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aeaec4"></a> `00aeaec4` | `81 aa 43 f9` | ldr x1,[x20, #0x750] | `FALL_THROUGH`
<a id="insn-00aeaec8"></a> `00aeaec8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeaecc"></a> `00aeaecc` | `41 01 00 b5` | cbnz x1,0x00aeaef4 | `CONDITIONAL_JUMP`
<a id="insn-00aeaed0"></a> `00aeaed0` | `63 bd ff 90` | adrp x3,0x296000 | `FALL_THROUGH`
<a id="insn-00aeaed4"></a> `00aeaed4` | `63 54 2f 91` | add x3,x3,#0xbd5 | `FALL_THROUGH`
<a id="insn-00aeaed8"></a> `00aeaed8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaedc"></a> `00aeaedc` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aeaee0"></a> `00aeaee0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeaee4"></a> `00aeaee4` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeaee8"></a> `00aeaee8` | `2a cc 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaeec"></a> `00aeaeec` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aeaef0"></a> `00aeaef0` | `80 aa 03 f9` | str x0,[x20, #0x750] | `FALL_THROUGH`
<a id="insn-00aeaef4"></a> `00aeaef4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaef8"></a> `00aeaef8` | `42 c0 ff f0` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00aeaefc"></a> `00aeaefc` | `a4 2d 00 d0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaf00"></a> `00aeaf00` | `65 bd ff 90` | adrp x5,0x296000 | `FALL_THROUGH`
<a id="insn-00aeaf04"></a> `00aeaf04` | `42 20 33 91` | add x2,x2,#0xcc8 | `FALL_THROUGH`
<a id="insn-00aeaf08"></a> `00aeaf08` | `84 a0 1d 91` | add x4,x4,#0x768 | `FALL_THROUGH`
<a id="insn-00aeaf0c"></a> `00aeaf0c` | `a5 54 2f 91` | add x5,x5,#0xbd5 | `FALL_THROUGH`
<a id="insn-00aeaf10"></a> `00aeaf10` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aeaf14"></a> `00aeaf14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaf18"></a> `00aeaf18` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeaf1c"></a> `00aeaf1c` | `15 cc 03 14` | b 0x00bddf70 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeaeb0`](#insn-00aeaeb0) 範囲 `[['00aeaeb0', '00aeaecf']]`
  - `CONDITIONAL_JUMP` [`00aeaecc`](#insn-00aeaecc) → [`00aeaef4`](#insn-00aeaef4)
  - `FALL_THROUGH` [`00aeaecc`](#insn-00aeaecc) → [`00aeaed0`](#insn-00aeaed0)
- ブロック [`00aeaed0`](#insn-00aeaed0) 範囲 `[['00aeaed0', '00aeaef3']]`
  - `FALL_THROUGH` [`00aeaef0`](#insn-00aeaef0) → [`00aeaef4`](#insn-00aeaef4)
- ブロック [`00aeaef4`](#insn-00aeaef4) 範囲 `[['00aeaef4', '00aeaf1f']]`

## 命令位置別の参照

- [`00aeaeb0`](#insn-00aeaeb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaeb4`](#insn-00aeaeb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaec4`](#insn-00aeaec4) → `010a0750`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaecc`](#insn-00aeaecc) → [`00aeaef4`](#insn-00aeaef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaed4`](#insn-00aeaed4) → `00296bd5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeaee8`](#insn-00aeaee8) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00aeaef0`](#insn-00aeaef0) → `010a0750`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaef4`](#insn-00aeaef4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf04`](#insn-00aeaf04) → `002f5cc8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf08`](#insn-00aeaf08) → `010a0768`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf0c`](#insn-00aeaf0c) → `00296bd5`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeaf1c`](#insn-00aeaf1c) → [`00bddf70`](../00bdd/00bddf70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf70` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeaeb0`](#insn-00aeaeb0)

~~~json
{
  "source": "00aeaeb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaeb4`](#insn-00aeaeb4)

~~~json
{
  "source": "00aeaeb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaec4`](#insn-00aeaec4)

~~~json
{
  "source": "00aeaec4",
  "target": "010a0750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0750",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaecc`](#insn-00aeaecc)

~~~json
{
  "source": "00aeaecc",
  "target": "00aeaef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaed4`](#insn-00aeaed4)

~~~json
{
  "source": "00aeaed4",
  "target": "00296bd5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296bd5",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f486173684d617000",
  "capture_start": "00296bd5",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeaee8`](#insn-00aeaee8)

~~~json
{
  "source": "00aeaee8",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaef0`](#insn-00aeaef0)

~~~json
{
  "source": "00aeaef0",
  "target": "010a0750",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0750",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaef4`](#insn-00aeaef4)

~~~json
{
  "source": "00aeaef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf04`](#insn-00aeaf04)

~~~json
{
  "source": "00aeaf04",
  "target": "002f5cc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf08`](#insn-00aeaf08)

~~~json
{
  "source": "00aeaf08",
  "target": "010a0768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf0c`](#insn-00aeaf0c)

~~~json
{
  "source": "00aeaf0c",
  "target": "00296bd5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296bd5",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f486173684d617000",
  "capture_start": "00296bd5",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeaf1c`](#insn-00aeaf1c)

~~~json
{
  "source": "00aeaf1c",
  "target": "00bddf70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
