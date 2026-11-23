# 00ae9bbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae9c84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae9/00ae9c84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-e050f11e57ecde5325a2b082dfff89a6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae9bbc",
  "name": "_ZN8firebase4util4date14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea541ba29adefea8596a83311ad2c8d4c836e2d488cc5afd7920bc53d7719f41",
  "source_text_sha256": "ea541ba29adefea8596a83311ad2c8d4c836e2d488cc5afd7920bc53d7719f41",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae9bbc",
        "00ae9c2b"
      ]
    ],
    "bytes_sha256": "14bf37ae55591218e33406184b336afb154566c1707ec385ec429826a8e88558",
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

- [00bddf90](../00bdd/00bddf90.md)
- [00bddfb0](../00bdd/00bddfb0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Date"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 696 bytes

~~~c

void _ZN8firebase4util4date14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a0650 == 0) {
    DAT_010a0650 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Date",0);
  }
                    /* try { // try from 00ae9c20 to 00be9c5f has its CatchHandler @ 00ae9c98 */
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a0650,&PTR_s_<init>_00c10120,3,&DAT_010a0660,"java/util/Date");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae9bbc"></a> `00ae9bbc` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae9bc0"></a> `00ae9bc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae9bc4"></a> `00ae9bc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae9bc8"></a> `00ae9bc8` | `b4 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae9bcc"></a> `00ae9bcc` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00ae9bd0"></a> `00ae9bd0` | `81 2a 43 f9` | ldr x1,[x20, #0x650] | `FALL_THROUGH`
<a id="insn-00ae9bd4"></a> `00ae9bd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ae9bd8"></a> `00ae9bd8` | `41 01 00 b5` | cbnz x1,0x00ae9c00 | `CONDITIONAL_JUMP`
<a id="insn-00ae9bdc"></a> `00ae9bdc` | `63 bd ff f0` | adrp x3,0x298000 | `FALL_THROUGH`
<a id="insn-00ae9be0"></a> `00ae9be0` | `63 f8 17 91` | add x3,x3,#0x5fe | `FALL_THROUGH`
<a id="insn-00ae9be4"></a> `00ae9be4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae9be8"></a> `00ae9be8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00ae9bec"></a> `00ae9bec` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00ae9bf0"></a> `00ae9bf0` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00ae9bf4"></a> `00ae9bf4` | `e7 d0 03 94` | bl 0x00bddf90 | `UNCONDITIONAL_CALL`
<a id="insn-00ae9bf8"></a> `00ae9bf8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ae9bfc"></a> `00ae9bfc` | `80 2a 03 f9` | str x0,[x20, #0x650] | `FALL_THROUGH`
<a id="insn-00ae9c00"></a> `00ae9c00` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae9c04"></a> `00ae9c04` | `22 09 00 f0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00ae9c08"></a> `00ae9c08` | `a4 2d 00 f0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae9c0c"></a> `00ae9c0c` | `65 bd ff f0` | adrp x5,0x298000 | `FALL_THROUGH`
<a id="insn-00ae9c10"></a> `00ae9c10` | `42 80 04 91` | add x2,x2,#0x120 | `FALL_THROUGH`
<a id="insn-00ae9c14"></a> `00ae9c14` | `84 80 19 91` | add x4,x4,#0x660 | `FALL_THROUGH`
<a id="insn-00ae9c18"></a> `00ae9c18` | `a5 f8 17 91` | add x5,x5,#0x5fe | `FALL_THROUGH`
<a id="insn-00ae9c1c"></a> `00ae9c1c` | `63 00 80 52` | mov w3,#0x3 | `FALL_THROUGH`
<a id="insn-00ae9c20"></a> `00ae9c20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ae9c24"></a> `00ae9c24` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae9c28"></a> `00ae9c28` | `e2 d0 03 14` | b 0x00bddfb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae9bbc`](#insn-00ae9bbc) 範囲 `[['00ae9bbc', '00ae9bdb']]`
  - `CONDITIONAL_JUMP` [`00ae9bd8`](#insn-00ae9bd8) → [`00ae9c00`](#insn-00ae9c00)
  - `FALL_THROUGH` [`00ae9bd8`](#insn-00ae9bd8) → [`00ae9bdc`](#insn-00ae9bdc)
- ブロック [`00ae9bdc`](#insn-00ae9bdc) 範囲 `[['00ae9bdc', '00ae9bff']]`
  - `FALL_THROUGH` [`00ae9bfc`](#insn-00ae9bfc) → [`00ae9c00`](#insn-00ae9c00)
- ブロック [`00ae9c00`](#insn-00ae9c00) 範囲 `[['00ae9c00', '00ae9c1f']]`
  - `FALL_THROUGH` [`00ae9c1c`](#insn-00ae9c1c) → [`00ae9c20`](#insn-00ae9c20)
- ブロック [`00ae9c20`](#insn-00ae9c20) 範囲 `[['00ae9c20', '00ae9c2b']]`

## 命令位置別の参照

- [`00ae9bbc`](#insn-00ae9bbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae9bc0`](#insn-00ae9bc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae9bd0`](#insn-00ae9bd0) → `010a0650`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae9bd8`](#insn-00ae9bd8) → [`00ae9c00`](#insn-00ae9c00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae9be0`](#insn-00ae9be0) → `002985fe`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae9bf4`](#insn-00ae9bf4) → [`00bddf90`](../00bdd/00bddf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddf90` · 推定シンボル `None` · 推定型 `None`
- [`00ae9bfc`](#insn-00ae9bfc) → `010a0650`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ae9c00`](#insn-00ae9c00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae9c10`](#insn-00ae9c10) → `00c10120`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ae9c14`](#insn-00ae9c14) → `010a0660`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae9c18`](#insn-00ae9c18) → `002985fe`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae9c28`](#insn-00ae9c28) → [`00bddfb0`](../00bdd/00bddfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae9bbc`](#insn-00ae9bbc)

~~~json
{
  "source": "00ae9bbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae9bc0`](#insn-00ae9bc0)

~~~json
{
  "source": "00ae9bc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae9bd0`](#insn-00ae9bd0)

~~~json
{
  "source": "00ae9bd0",
  "target": "010a0650",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0650",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae9bd8`](#insn-00ae9bd8)

~~~json
{
  "source": "00ae9bd8",
  "target": "00ae9c00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae9be0`](#insn-00ae9be0)

~~~json
{
  "source": "00ae9be0",
  "target": "002985fe",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002985fe",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4461746500",
  "capture_start": "002985fe",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae9bf4`](#insn-00ae9bf4)

~~~json
{
  "source": "00ae9bf4",
  "target": "00bddf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae9bfc`](#insn-00ae9bfc)

~~~json
{
  "source": "00ae9bfc",
  "target": "010a0650",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0650",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ae9c00`](#insn-00ae9c00)

~~~json
{
  "source": "00ae9c00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae9c10`](#insn-00ae9c10)

~~~json
{
  "source": "00ae9c10",
  "target": "00c10120",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10120",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ae9c14`](#insn-00ae9c14)

~~~json
{
  "source": "00ae9c14",
  "target": "010a0660",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae9c18`](#insn-00ae9c18)

~~~json
{
  "source": "00ae9c18",
  "target": "002985fe",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002985fe",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f4461746500",
  "capture_start": "002985fe",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae9c28`](#insn-00ae9c28)

~~~json
{
  "source": "00ae9c28",
  "target": "00bddfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
