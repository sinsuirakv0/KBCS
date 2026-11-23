# 00aedaac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aed9e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aed/00aed9e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0061.md#compare-5d46a797210b2b2ffdaa927a8c36406b)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aedaf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aed/00aedaf0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-52061bc9526a74e20225d69405663b5a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aedaac",
  "name": "_ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9dc6dba353c9f347ac5eb28ad9dbb14c76acf2241b8a658251c7799d756b1738",
  "source_text_sha256": "9dc6dba353c9f347ac5eb28ad9dbb14c76acf2241b8a658251c7799d756b1738",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aedaac",
        "00aedb1b"
      ]
    ],
    "bytes_sha256": "19bf8d10a407582d44379ba3ee11bc23ea270ddd650045db7759a8e196f2f7d7",
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
"java/lang/Throwable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 835 bytes

~~~c

void _ZN8firebase4util9throwable14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aedab4 to 00bedaef has its CatchHandler @ 00af1ad8 */
  if (DAT_010a09f0 == 0) {
    DAT_010a09f0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Throwable",0);
  }
                    /* try { // try from 00aedaf0 to 00beed27 has its CatchHandler @ 00aeadc8 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a09f0,&PTR_s_getLocalizedMessage_00c105a8,3,&DAT_010a0a00,
             "java/lang/Throwable");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aedaac"></a> `00aedaac` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aedab0"></a> `00aedab0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedab4"></a> `00aedab4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aedab8"></a> `00aedab8` | `94 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedabc"></a> `00aedabc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aedac0"></a> `00aedac0` | `81 fa 44 f9` | ldr x1,[x20, #0x9f0] | `FALL_THROUGH`
<a id="insn-00aedac4"></a> `00aedac4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aedac8"></a> `00aedac8` | `41 01 00 b5` | cbnz x1,0x00aedaf0 | `CONDITIONAL_JUMP`
<a id="insn-00aedacc"></a> `00aedacc` | `c3 bd ff f0` | adrp x3,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aedad0"></a> `00aedad0` | `63 28 30 91` | add x3,x3,#0xc0a | `FALL_THROUGH`
<a id="insn-00aedad4"></a> `00aedad4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedad8"></a> `00aedad8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aedadc"></a> `00aedadc` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aedae0"></a> `00aedae0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aedae4"></a> `00aedae4` | `57 c1 03 94` | bl 0x00bde040 | `UNCONDITIONAL_CALL`
<a id="insn-00aedae8"></a> `00aedae8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aedaec"></a> `00aedaec` | `80 fa 04 f9` | str x0,[x20, #0x9f0] | `FALL_THROUGH`
<a id="insn-00aedaf0"></a> `00aedaf0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aedaf4"></a> `00aedaf4` | `02 09 00 f0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aedaf8"></a> `00aedaf8` | `84 2d 00 f0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aedafc"></a> `00aedafc` | `c5 bd ff f0` | adrp x5,0x2a8000 | `FALL_THROUGH`
<a id="insn-00aedb00"></a> `00aedb00` | `42 a0 16 91` | add x2,x2,#0x5a8 | `FALL_THROUGH`
<a id="insn-00aedb04"></a> `00aedb04` | `84 00 28 91` | add x4,x4,#0xa00 | `FALL_THROUGH`
<a id="insn-00aedb08"></a> `00aedb08` | `a5 28 30 91` | add x5,x5,#0xc0a | `FALL_THROUGH`
<a id="insn-00aedb0c"></a> `00aedb0c` | `63 00 80 52` | mov w3,#0x3 | `FALL_THROUGH`
<a id="insn-00aedb10"></a> `00aedb10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aedb14"></a> `00aedb14` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aedb18"></a> `00aedb18` | `52 c1 03 14` | b 0x00bde060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aedaac`](#insn-00aedaac) 範囲 `[['00aedaac', '00aedab3']]`
  - `FALL_THROUGH` [`00aedab0`](#insn-00aedab0) → [`00aedab4`](#insn-00aedab4)
- ブロック [`00aedab4`](#insn-00aedab4) 範囲 `[['00aedab4', '00aedacb']]`
  - `CONDITIONAL_JUMP` [`00aedac8`](#insn-00aedac8) → [`00aedaf0`](#insn-00aedaf0)
  - `FALL_THROUGH` [`00aedac8`](#insn-00aedac8) → [`00aedacc`](#insn-00aedacc)
- ブロック [`00aedacc`](#insn-00aedacc) 範囲 `[['00aedacc', '00aedaef']]`
  - `FALL_THROUGH` [`00aedaec`](#insn-00aedaec) → [`00aedaf0`](#insn-00aedaf0)
- ブロック [`00aedaf0`](#insn-00aedaf0) 範囲 `[['00aedaf0', '00aedb1b']]`

## 命令位置別の参照

- [`00aedaac`](#insn-00aedaac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedab0`](#insn-00aedab0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedac0`](#insn-00aedac0) → `010a09f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedac8`](#insn-00aedac8) → [`00aedaf0`](#insn-00aedaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedad0`](#insn-00aedad0) → `002a8c0a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedae4`](#insn-00aedae4) → [`00bde040`](../00bde/00bde040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde040` · 推定シンボル `None` · 推定型 `None`
- [`00aedaec`](#insn-00aedaec) → `010a09f0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedaf0`](#insn-00aedaf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aedb00`](#insn-00aedb00) → `00c105a8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aedb04`](#insn-00aedb04) → `010a0a00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aedb08`](#insn-00aedb08) → `002a8c0a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aedb18`](#insn-00aedb18) → [`00bde060`](../00bde/00bde060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aedaac`](#insn-00aedaac)

~~~json
{
  "source": "00aedaac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedab0`](#insn-00aedab0)

~~~json
{
  "source": "00aedab0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedac0`](#insn-00aedac0)

~~~json
{
  "source": "00aedac0",
  "target": "010a09f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedac8`](#insn-00aedac8)

~~~json
{
  "source": "00aedac8",
  "target": "00aedaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedad0`](#insn-00aedad0)

~~~json
{
  "source": "00aedad0",
  "target": "002a8c0a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8c0a",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f5468726f7761626c6500",
  "capture_start": "002a8c0a",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedae4`](#insn-00aedae4)

~~~json
{
  "source": "00aedae4",
  "target": "00bde040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aedaec`](#insn-00aedaec)

~~~json
{
  "source": "00aedaec",
  "target": "010a09f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedaf0`](#insn-00aedaf0)

~~~json
{
  "source": "00aedaf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aedb00`](#insn-00aedb00)

~~~json
{
  "source": "00aedb00",
  "target": "00c105a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c105a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aedb04`](#insn-00aedb04)

~~~json
{
  "source": "00aedb04",
  "target": "010a0a00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0a00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aedb08`](#insn-00aedb08)

~~~json
{
  "source": "00aedb08",
  "target": "002a8c0a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8c0a",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f5468726f7761626c6500",
  "capture_start": "002a8c0a",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aedb18`](#insn-00aedb18)

~~~json
{
  "source": "00aedb18",
  "target": "00bde060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
