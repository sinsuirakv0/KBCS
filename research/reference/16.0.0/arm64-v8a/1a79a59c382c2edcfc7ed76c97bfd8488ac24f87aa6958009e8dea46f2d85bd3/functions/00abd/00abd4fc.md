# 00abd4fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a5f544`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5f/00a5f544.md) · 移動量 `+0x5dfb8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-a5534df28c64d78ba3efeb30e33d9faf)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abd6f8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abd/00abd6f8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-1f3a3b288042c9f0b18e3c65e054b581)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abd4fc",
  "name": "FUN_00abd4fc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b36ccadad6d773697ceeae7865419329ef493c7b26d99c553b3273f43b53d115",
  "source_text_sha256": "b36ccadad6d773697ceeae7865419329ef493c7b26d99c553b3273f43b53d115",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abd4fc",
        "00abd5a3"
      ]
    ],
    "bytes_sha256": "d57f0c67e826a638236b0d4116d1ae2981e65940341fe93e8801a39ebe0737c8",
    "instruction_count": 42,
    "instruction_bytes": 168,
    "body_bytes": 168,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0083f844](../0083f/0083f844.md)

## 呼び出し先

- [0046e784](../0046e/0046e784.md)
- [0046eeb8](../0046e/0046eeb8.md)
- [005c175c](../005c1/005c175c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 955 bytes

~~~c

void FUN_00abd4fc(undefined8 *param_1)

{
  undefined8 *puVar1;
  
  param_1[0xb] = 0;
  puVar1 = param_1 + 10;
  *puVar1 = 0;
  param_1[9] = puVar1;
  param_1[1] = 0;
  *param_1 = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[8] = 0;
  param_1[0x10] = 0;
  param_1[0xf] = 0;
  param_1[0x12] = 0;
  param_1[0x11] = 0;
  param_1[0x14] = 0;
  param_1[0x13] = 0;
  FUN_0046eeb8(param_1 + 0x15);
  FUN_0046e784(param_1 + 0x2a);
                    /* try { // try from 00abd55c to 00bbd64f has its CatchHandler @ 00abd2c0 */
  *(undefined4 *)(param_1 + 0xd) = 0;
  param_1[0xc] = 0;
  param_1[7] = param_1[6];
  FUN_005c175c(param_1 + 9,param_1[10]);
  param_1[10] = 0;
  param_1[0xb] = 0;
  *(undefined4 *)(param_1 + 0xe) = 0xffffffff;
  param_1[9] = puVar1;
  *(undefined1 *)((long)param_1 + 0x6c) = 0;
  param_1[0x10] = param_1[0xf];
  param_1[0x13] = param_1[0x12];
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abd4fc"></a> `00abd4fc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00abd500"></a> `00abd500` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abd504"></a> `00abd504` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abd508"></a> `00abd508` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abd50c"></a> `00abd50c` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00abd510"></a> `00abd510` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abd514"></a> `00abd514` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00abd518"></a> `00abd518` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00abd51c"></a> `00abd51c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00abd520"></a> `00abd520` | `1f 2c 00 f9` | str xzr,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00abd524"></a> `00abd524` | `bf 0e 05 f8` | str xzr,[x21, #0x50]! | `FALL_THROUGH`
<a id="insn-00abd528"></a> `00abd528` | `95 8e 04 f8` | str x21,[x20, #0x48]! | `FALL_THROUGH`
<a id="insn-00abd52c"></a> `00abd52c` | `00 00 00 ad` | stp q0,q0,[x0] | `FALL_THROUGH`
<a id="insn-00abd530"></a> `00abd530` | `00 00 01 ad` | stp q0,q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abd534"></a> `00abd534` | `1f 20 00 f9` | str xzr,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00abd538"></a> `00abd538` | `c0 8e 87 3c` | str q0,[x22, #0x78]! | `FALL_THROUGH`
<a id="insn-00abd53c"></a> `00abd53c` | `00 80 88 3c` | stur q0,[x0, #0x88] | `FALL_THROUGH`
<a id="insn-00abd540"></a> `00abd540` | `00 80 89 3c` | stur q0,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00abd544"></a> `00abd544` | `00 a0 02 91` | add x0,x0,#0xa8 | `FALL_THROUGH`
<a id="insn-00abd548"></a> `00abd548` | `5c c6 e6 97` | bl 0x0046eeb8 | `UNCONDITIONAL_CALL`
<a id="insn-00abd54c"></a> `00abd54c` | `60 42 05 91` | add x0,x19,#0x150 | `FALL_THROUGH`
<a id="insn-00abd550"></a> `00abd550` | `8d c4 e6 97` | bl 0x0046e784 | `UNCONDITIONAL_CALL`
<a id="insn-00abd554"></a> `00abd554` | `68 1a 40 f9` | ldr x8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00abd558"></a> `00abd558` | `61 2a 40 f9` | ldr x1,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00abd55c"></a> `00abd55c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00abd560"></a> `00abd560` | `7f 6a 00 b9` | str wzr,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00abd564"></a> `00abd564` | `7f 32 00 f9` | str xzr,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00abd568"></a> `00abd568` | `68 1e 00 f9` | str x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00abd56c"></a> `00abd56c` | `7c 10 ec 97` | bl 0x005c175c | `UNCONDITIONAL_CALL`
<a id="insn-00abd570"></a> `00abd570` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00abd574"></a> `00abd574` | `69 3e 40 f9` | ldr x9,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00abd578"></a> `00abd578` | `7f 7e 05 a9` | stp xzr,xzr,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00abd57c"></a> `00abd57c` | `68 72 00 b9` | str w8,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00abd580"></a> `00abd580` | `68 4a 40 f9` | ldr x8,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00abd584"></a> `00abd584` | `75 26 00 f9` | str x21,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00abd588"></a> `00abd588` | `7f b2 01 39` | strb wzr,[x19, #0x6c] | `FALL_THROUGH`
<a id="insn-00abd58c"></a> `00abd58c` | `69 42 00 f9` | str x9,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00abd590"></a> `00abd590` | `68 4e 00 f9` | str x8,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00abd594"></a> `00abd594` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abd598"></a> `00abd598` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abd59c"></a> `00abd59c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00abd5a0"></a> `00abd5a0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abd4fc`](#insn-00abd4fc) 範囲 `[['00abd4fc', '00abd55b']]`
  - `FALL_THROUGH` [`00abd558`](#insn-00abd558) → [`00abd55c`](#insn-00abd55c)
- ブロック [`00abd55c`](#insn-00abd55c) 範囲 `[['00abd55c', '00abd5a3']]`

## 命令位置別の参照

- [`00abd4fc`](#insn-00abd4fc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd500`](#insn-00abd500) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd504`](#insn-00abd504) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd548`](#insn-00abd548) → [`0046eeb8`](../0046e/0046eeb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046eeb8` · 推定シンボル `None` · 推定型 `None`
- [`00abd550`](#insn-00abd550) → [`0046e784`](../0046e/0046e784.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e784` · 推定シンボル `None` · 推定型 `None`
- [`00abd56c`](#insn-00abd56c) → [`005c175c`](../005c1/005c175c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c175c` · 推定シンボル `None` · 推定型 `None`
- [`00abd594`](#insn-00abd594) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd598`](#insn-00abd598) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd59c`](#insn-00abd59c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abd4fc`](#insn-00abd4fc)

~~~json
{
  "source": "00abd4fc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd500`](#insn-00abd500)

~~~json
{
  "source": "00abd500",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd504`](#insn-00abd504)

~~~json
{
  "source": "00abd504",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd548`](#insn-00abd548)

~~~json
{
  "source": "00abd548",
  "target": "0046eeb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd550`](#insn-00abd550)

~~~json
{
  "source": "00abd550",
  "target": "0046e784",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd56c`](#insn-00abd56c)

~~~json
{
  "source": "00abd56c",
  "target": "005c175c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abd594`](#insn-00abd594)

~~~json
{
  "source": "00abd594",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd598`](#insn-00abd598)

~~~json
{
  "source": "00abd598",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd59c`](#insn-00abd59c)

~~~json
{
  "source": "00abd59c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
