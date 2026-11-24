# 00aebab4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aeba70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aeba70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-1dc02455b01c58dc61c13b794109c685)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b4b838`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b4b/00b4b838.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0058.md#compare-35b33258954371f18a23b9621052eac0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebab4",
  "name": "_ZN8firebase4util8iterable13CacheFieldIdsEP7_JNIEnvP8_jobject",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d1e554776c6e055da9f9b08954a9224050d401fe4fb3a07c4deed4820c93d60e",
  "source_text_sha256": "d1e554776c6e055da9f9b08954a9224050d401fe4fb3a07c4deed4820c93d60e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebab4",
        "00aebb23"
      ]
    ],
    "bytes_sha256": "a50cc59c84f4a10e11d52e9b92919aedcd48d7a7242b5819c2b1f4b07fb25fe1",
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

- [00bde070](../00bde/00bde070.md)
- [00bde090](../00bde/00bde090.md)

## 関連文字列（未確認候補）

~~~text
"java/lang/Iterable"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 788 bytes

~~~c

void _ZN8firebase4util8iterable13CacheFieldIdsEP7_JNIEnvP8_jobject
               (undefined8 param_1,undefined8 param_2)

{
                    /* try { // try from 00aebabc to 00bebac7 has its CatchHandler @ 00af1940 */
                    /* try { // try from 00aebac8 to 00bebb97 has its CatchHandler @ 00aeae0c */
  if (DAT_010a08d8 == 0) {
    DAT_010a08d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"java/lang/Iterable",0);
  }
  _ZN8firebase4util14LookupFieldIdsEP7_JNIEnvP7_jclassPKNS0_15FieldDescriptorEmPP9_jfieldIDPKc
            (param_1,DAT_010a08d8,&DAT_002f5d10,1,&DAT_010a08f0,"java/lang/Iterable");
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebab4"></a> `00aebab4` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebab8"></a> `00aebab8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebabc"></a> `00aebabc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebac0"></a> `00aebac0` | `b4 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebac4"></a> `00aebac4` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aebac8"></a> `00aebac8` | `81 6e 44 f9` | ldr x1,[x20, #0x8d8] | `FALL_THROUGH`
<a id="insn-00aebacc"></a> `00aebacc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aebad0"></a> `00aebad0` | `41 01 00 b5` | cbnz x1,0x00aebaf8 | `CONDITIONAL_JUMP`
<a id="insn-00aebad4"></a> `00aebad4` | `23 bd ff b0` | adrp x3,0x290000 | `FALL_THROUGH`
<a id="insn-00aebad8"></a> `00aebad8` | `63 c8 0d 91` | add x3,x3,#0x372 | `FALL_THROUGH`
<a id="insn-00aebadc"></a> `00aebadc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebae0"></a> `00aebae0` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00aebae4"></a> `00aebae4` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aebae8"></a> `00aebae8` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aebaec"></a> `00aebaec` | `69 c9 03 94` | bl 0x00bde090 | `UNCONDITIONAL_CALL`
<a id="insn-00aebaf0"></a> `00aebaf0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aebaf4"></a> `00aebaf4` | `80 6e 04 f9` | str x0,[x20, #0x8d8] | `FALL_THROUGH`
<a id="insn-00aebaf8"></a> `00aebaf8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebafc"></a> `00aebafc` | `42 c0 ff d0` | adrp x2,0x2f5000 | `FALL_THROUGH`
<a id="insn-00aebb00"></a> `00aebb00` | `a4 2d 00 b0` | adrp x4,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebb04"></a> `00aebb04` | `25 bd ff b0` | adrp x5,0x290000 | `FALL_THROUGH`
<a id="insn-00aebb08"></a> `00aebb08` | `42 40 34 91` | add x2,x2,#0xd10 | `FALL_THROUGH`
<a id="insn-00aebb0c"></a> `00aebb0c` | `84 c0 23 91` | add x4,x4,#0x8f0 | `FALL_THROUGH`
<a id="insn-00aebb10"></a> `00aebb10` | `a5 c8 0d 91` | add x5,x5,#0x372 | `FALL_THROUGH`
<a id="insn-00aebb14"></a> `00aebb14` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00aebb18"></a> `00aebb18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aebb1c"></a> `00aebb1c` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebb20"></a> `00aebb20` | `54 c9 03 14` | b 0x00bde070 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebab4`](#insn-00aebab4) 範囲 `[['00aebab4', '00aebabb']]`
  - `FALL_THROUGH` [`00aebab8`](#insn-00aebab8) → [`00aebabc`](#insn-00aebabc)
- ブロック [`00aebabc`](#insn-00aebabc) 範囲 `[['00aebabc', '00aebac7']]`
  - `FALL_THROUGH` [`00aebac4`](#insn-00aebac4) → [`00aebac8`](#insn-00aebac8)
- ブロック [`00aebac8`](#insn-00aebac8) 範囲 `[['00aebac8', '00aebad3']]`
  - `CONDITIONAL_JUMP` [`00aebad0`](#insn-00aebad0) → [`00aebaf8`](#insn-00aebaf8)
  - `FALL_THROUGH` [`00aebad0`](#insn-00aebad0) → [`00aebad4`](#insn-00aebad4)
- ブロック [`00aebad4`](#insn-00aebad4) 範囲 `[['00aebad4', '00aebaf7']]`
  - `FALL_THROUGH` [`00aebaf4`](#insn-00aebaf4) → [`00aebaf8`](#insn-00aebaf8)
- ブロック [`00aebaf8`](#insn-00aebaf8) 範囲 `[['00aebaf8', '00aebb23']]`

## 命令位置別の参照

- [`00aebab4`](#insn-00aebab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebab8`](#insn-00aebab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebac8`](#insn-00aebac8) → `010a08d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebad0`](#insn-00aebad0) → [`00aebaf8`](#insn-00aebaf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebad8`](#insn-00aebad8) → `00290372`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebaec`](#insn-00aebaec) → [`00bde090`](../00bde/00bde090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde090` · 推定シンボル `None` · 推定型 `None`
- [`00aebaf4`](#insn-00aebaf4) → `010a08d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aebaf8`](#insn-00aebaf8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb08`](#insn-00aebb08) → `002f5d10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb0c`](#insn-00aebb0c) → `010a08f0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebb10`](#insn-00aebb10) → `00290372`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebb20`](#insn-00aebb20) → [`00bde070`](../00bde/00bde070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde070` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebab4`](#insn-00aebab4)

~~~json
{
  "source": "00aebab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebab8`](#insn-00aebab8)

~~~json
{
  "source": "00aebab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebac8`](#insn-00aebac8)

~~~json
{
  "source": "00aebac8",
  "target": "010a08d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebad0`](#insn-00aebad0)

~~~json
{
  "source": "00aebad0",
  "target": "00aebaf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebad8`](#insn-00aebad8)

~~~json
{
  "source": "00aebad8",
  "target": "00290372",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290372",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4974657261626c6500",
  "capture_start": "00290372",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebaec`](#insn-00aebaec)

~~~json
{
  "source": "00aebaec",
  "target": "00bde090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebaf4`](#insn-00aebaf4)

~~~json
{
  "source": "00aebaf4",
  "target": "010a08d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aebaf8`](#insn-00aebaf8)

~~~json
{
  "source": "00aebaf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb08`](#insn-00aebb08)

~~~json
{
  "source": "00aebb08",
  "target": "002f5d10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb0c`](#insn-00aebb0c)

~~~json
{
  "source": "00aebb0c",
  "target": "010a08f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebb10`](#insn-00aebb10)

~~~json
{
  "source": "00aebb10",
  "target": "00290372",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00290372",
  "offset": 0,
  "size": 19,
  "datatype": "string",
  "bytes": "6a6176612f6c616e672f4974657261626c6500",
  "capture_start": "00290372",
  "capture_bytes": 19,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebb20`](#insn-00aebb20)

~~~json
{
  "source": "00aebb20",
  "target": "00bde070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
