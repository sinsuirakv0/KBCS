# 00aecff8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aecfb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aec/00aecfb4.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-e1cf4a8fa4ed193e87dba13e7e0c8b3a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4cd7c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4c/00b4cd7c.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0059.md#compare-dbbe481379aa6644a6cba0d56b17df87)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aecff8",
  "name": "_ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6cecee126d1016edd404fb1665f1cb8bda03b79b660691f266e5b88333b53229",
  "source_text_sha256": "6cecee126d1016edd404fb1665f1cb8bda03b79b660691f266e5b88333b53229",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aecff8",
        "00aed067"
      ]
    ],
    "bytes_sha256": "fcd35388dda43cb18c53930c161f91bd02d98988ebe91b47fbf32295ee57df58",
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

- [00bde090](../00bde/00bde090.md)
- [00bde0b0](../00bde/00bde0b0.md)

## 関連文字列（未確認候補）

~~~text
"java/util/Set"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 598 bytes

~~~c

void _ZN8firebase4util3set14CacheMethodIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
  if (DAT_010a09c8 == 0) {
    DAT_010a09c8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/util/Set",0);
  }
  _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
            (param_1,DAT_010a09c8,&PTR_s_iterator_00c10598,1,&DAT_010a09d8,"java/util/Set");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aecff8"></a> `00aecff8` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aecffc"></a> `00aecffc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed000"></a> `00aed000` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aed004"></a> `00aed004` | `94 2d 00 f0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aed008"></a> `00aed008` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aed00c"></a> `00aed00c` | `81 e6 44 f9` | ldr x1,[x20, #0x9c8] | `FALL_THROUGH`
<a id="insn-00aed010"></a> `00aed010` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aed014"></a> `00aed014` | `41 01 00 b5` | cbnz x1,0x00aed03c | `CONDITIONAL_JUMP`
<a id="insn-00aed018"></a> `00aed018` | `83 bd ff f0` | adrp x3,0x2a0000 | `FALL_THROUGH`
<a id="insn-00aed01c"></a> `00aed01c` | `63 28 01 91` | add x3,x3,#0x4a | `FALL_THROUGH`
<a id="insn-00aed020"></a> `00aed020` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed024"></a> `00aed024` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aed028"></a> `00aed028` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aed02c"></a> `00aed02c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aed030"></a> `00aed030` | `18 c4 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aed034"></a> `00aed034` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aed038"></a> `00aed038` | `80 e6 04 f9` | str x0,[x20, #0x9c8] | `FALL_THROUGH`
<a id="insn-00aed03c"></a> `00aed03c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aed040"></a> `00aed040` | `02 09 00 f0` | adrp x2,0xc10000 | `FALL_THROUGH`
<a id="insn-00aed044"></a> `00aed044` | `84 2d 00 f0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aed048"></a> `00aed048` | `85 bd ff f0` | adrp x5,0x2a0000 | `FALL_THROUGH`
<a id="insn-00aed04c"></a> `00aed04c` | `42 60 16 91` | add x2,x2,#0x598 | `FALL_THROUGH`
<a id="insn-00aed050"></a> `00aed050` | `84 60 27 91` | add x4,x4,#0x9d8 | `FALL_THROUGH`
<a id="insn-00aed054"></a> `00aed054` | `a5 28 01 91` | add x5,x5,#0x4a | `FALL_THROUGH`
<a id="insn-00aed058"></a> `00aed058` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aed05c"></a> `00aed05c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aed060"></a> `00aed060` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aed064"></a> `00aed064` | `13 c4 03 14` | b 0x00bde0b0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aecff8`](#insn-00aecff8) 範囲 `[['00aecff8', '00aed017']]`
  - `CONDITIONAL_JUMP` [`00aed014`](#insn-00aed014) → [`00aed03c`](#insn-00aed03c)
  - `FALL_THROUGH` [`00aed014`](#insn-00aed014) → [`00aed018`](#insn-00aed018)
- ブロック [`00aed018`](#insn-00aed018) 範囲 `[['00aed018', '00aed03b']]`
  - `FALL_THROUGH` [`00aed038`](#insn-00aed038) → [`00aed03c`](#insn-00aed03c)
- ブロック [`00aed03c`](#insn-00aed03c) 範囲 `[['00aed03c', '00aed067']]`

## 命令位置別の参照

- [`00aecff8`](#insn-00aecff8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aecffc`](#insn-00aecffc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed00c`](#insn-00aed00c) → `010a09c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed014`](#insn-00aed014) → [`00aed03c`](#insn-00aed03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed01c`](#insn-00aed01c) → `002a004a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aed030`](#insn-00aed030) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aed038`](#insn-00aed038) → `010a09c8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed03c`](#insn-00aed03c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aed04c`](#insn-00aed04c) → `00c10598`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aed050`](#insn-00aed050) → `010a09d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aed054`](#insn-00aed054) → `002a004a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aed064`](#insn-00aed064) → [`00bde0b0`](../00bde/00bde0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde0b0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aecff8`](#insn-00aecff8)

~~~json
{
  "source": "00aecff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aecffc`](#insn-00aecffc)

~~~json
{
  "source": "00aecffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed00c`](#insn-00aed00c)

~~~json
{
  "source": "00aed00c",
  "target": "010a09c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed014`](#insn-00aed014)

~~~json
{
  "source": "00aed014",
  "target": "00aed03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed01c`](#insn-00aed01c)

~~~json
{
  "source": "00aed01c",
  "target": "002a004a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a004a",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "002a004a",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aed030`](#insn-00aed030)

~~~json
{
  "source": "00aed030",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aed038`](#insn-00aed038)

~~~json
{
  "source": "00aed038",
  "target": "010a09c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed03c`](#insn-00aed03c)

~~~json
{
  "source": "00aed03c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aed04c`](#insn-00aed04c)

~~~json
{
  "source": "00aed04c",
  "target": "00c10598",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10598",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aed050`](#insn-00aed050)

~~~json
{
  "source": "00aed050",
  "target": "010a09d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a09d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aed054`](#insn-00aed054)

~~~json
{
  "source": "00aed054",
  "target": "002a004a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a004a",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "6a6176612f7574696c2f53657400",
  "capture_start": "002a004a",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aed064`](#insn-00aed064)

~~~json
{
  "source": "00aed064",
  "target": "00bde0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
