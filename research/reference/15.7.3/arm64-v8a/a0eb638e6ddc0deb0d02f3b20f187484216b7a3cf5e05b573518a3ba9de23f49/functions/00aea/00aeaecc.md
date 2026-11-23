# 00aeaecc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeae04`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeae04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-6e133340510cf0872c358fee0b9d73d1)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeaf10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aea/00aeaf10.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-0d7a26a71f0d0f57f55856597b5a6e2e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeaecc",
  "name": "_ZN8firebase4util8hash_map14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95dd82a3f3a8b0f7ad653c1aa61ceda2e1f4bfbffa756626afc4ebfc3cdb7f41",
  "source_text_sha256": "95dd82a3f3a8b0f7ad653c1aa61ceda2e1f4bfbffa756626afc4ebfc3cdb7f41",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeaecc",
        "00aeaf3b"
      ]
    ],
    "bytes_sha256": "adf290fc68ad3d0f3d76b308b70cf4946e388a0873d3d4edd39b77bcf92547b5",
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

- [00bde040](../00bde/00bde040.md)
- [00bde060](../00bde/00bde060.md)

## 関連文字列（未確認候補）

~~~text
"java/util/HashMap"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 609 bytes

~~~c

void _ZN8firebase4util8hash_map14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0810 == 0) {
    DAT_010a0810 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/HashMap",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0810,&PTR_s_<init>_00c10368,1,&DAT_010a0820,"java/util/HashMap");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeaecc"></a> `00aeaecc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeaed0"></a> `00aeaed0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaed4"></a> `00aeaed4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeaed8"></a> `00aeaed8` | `b4 2d 00 d0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaedc"></a> `00aeaedc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aeaee0"></a> `00aeaee0` | `81 0a 44 f9` | ldr x1,[x20, #0x810] | `FALL_THROUGH`
<a id="insn-00aeaee4"></a> `00aeaee4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aeaee8"></a> `00aeaee8` | `41 01 00 b5` | cbnz x1,0x00aeaf10 | `CONDITIONAL_JUMP`
<a id="insn-00aeaeec"></a> `00aeaeec` | `63 bd ff 90` | adrp x3,0x296000 | `FALL_THROUGH`
<a id="insn-00aeaef0"></a> `00aeaef0` | `63 88 31 91` | add x3,x3,#0xc62 | `FALL_THROUGH`
<a id="insn-00aeaef4"></a> `00aeaef4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaef8"></a> `00aeaef8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aeaefc"></a> `00aeaefc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aeaf00"></a> `00aeaf00` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aeaf04"></a> `00aeaf04` | `4f cc 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aeaf08"></a> `00aeaf08` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aeaf0c"></a> `00aeaf0c` | `80 0a 04 f9` | str x0,[x20, #0x810] | `FALL_THROUGH`
<a id="insn-00aeaf10"></a> `00aeaf10` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaf14"></a> `00aeaf14` | `22 09 00 d0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aeaf18"></a> `00aeaf18` | `a4 2d 00 d0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeaf1c"></a> `00aeaf1c` | `65 bd ff 90` | adrp x5,0x296000 | `FALL_THROUGH`
<a id="insn-00aeaf20"></a> `00aeaf20` | `42 a0 0d 91` | add x2,x2,#0x368 | `FALL_THROUGH`
<a id="insn-00aeaf24"></a> `00aeaf24` | `84 80 20 91` | add x4,x4,#0x820 | `FALL_THROUGH`
<a id="insn-00aeaf28"></a> `00aeaf28` | `a5 88 31 91` | add x5,x5,#0xc62 | `FALL_THROUGH`
<a id="insn-00aeaf2c"></a> `00aeaf2c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aeaf30"></a> `00aeaf30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aeaf34"></a> `00aeaf34` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeaf38"></a> `00aeaf38` | `4a cc 03 14` | b 0x00bde060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeaecc`](#insn-00aeaecc) 範囲 `[['00aeaecc', '00aeaeeb']]`
  - `CONDITIONAL_JUMP` [`00aeaee8`](#insn-00aeaee8) → [`00aeaf10`](#insn-00aeaf10)
  - `FALL_THROUGH` [`00aeaee8`](#insn-00aeaee8) → [`00aeaeec`](#insn-00aeaeec)
- ブロック [`00aeaeec`](#insn-00aeaeec) 範囲 `[['00aeaeec', '00aeaf0f']]`
  - `FALL_THROUGH` [`00aeaf0c`](#insn-00aeaf0c) → [`00aeaf10`](#insn-00aeaf10)
- ブロック [`00aeaf10`](#insn-00aeaf10) 範囲 `[['00aeaf10', '00aeaf3b']]`

## 命令位置別の参照

- [`00aeaecc`](#insn-00aeaecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaed0`](#insn-00aeaed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaee0`](#insn-00aeaee0) → `010a0810`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaee8`](#insn-00aeaee8) → [`00aeaf10`](#insn-00aeaf10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaef0`](#insn-00aeaef0) → `00296c62`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeaf04`](#insn-00aeaf04) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf0c`](#insn-00aeaf0c) → `010a0810`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaf10`](#insn-00aeaf10) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaf20`](#insn-00aeaf20) → `00c10368`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aeaf24`](#insn-00aeaf24) → `010a0820`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aeaf28`](#insn-00aeaf28) → `00296c62`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeaf38`](#insn-00aeaf38) → [`00bde060`](../00bde/00bde060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeaecc`](#insn-00aeaecc)

~~~json
{
  "source": "00aeaecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaed0`](#insn-00aeaed0)

~~~json
{
  "source": "00aeaed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaee0`](#insn-00aeaee0)

~~~json
{
  "source": "00aeaee0",
  "target": "010a0810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0810",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaee8`](#insn-00aeaee8)

~~~json
{
  "source": "00aeaee8",
  "target": "00aeaf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaef0`](#insn-00aeaef0)

~~~json
{
  "source": "00aeaef0",
  "target": "00296c62",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296c62",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f486173684d617000",
  "capture_start": "00296c62",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeaf04`](#insn-00aeaf04)

~~~json
{
  "source": "00aeaf04",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeaf0c`](#insn-00aeaf0c)

~~~json
{
  "source": "00aeaf0c",
  "target": "010a0810",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0810",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaf10`](#insn-00aeaf10)

~~~json
{
  "source": "00aeaf10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaf20`](#insn-00aeaf20)

~~~json
{
  "source": "00aeaf20",
  "target": "00c10368",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10368",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aeaf24`](#insn-00aeaf24)

~~~json
{
  "source": "00aeaf24",
  "target": "010a0820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0820",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aeaf28`](#insn-00aeaf28)

~~~json
{
  "source": "00aeaf28",
  "target": "00296c62",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00296c62",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f486173684d617000",
  "capture_start": "00296c62",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeaf38`](#insn-00aeaf38)

~~~json
{
  "source": "00aeaf38",
  "target": "00bde060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
