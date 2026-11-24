# 00acddbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acdd78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acd/00acdd78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-d97ac59336ad01cf6c8b1e4a2bdb0a0c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2d874`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2d/00b2d874.md) · 移動量 `+0x5fab8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0054.md#compare-64bba3b8fea5c754bdc68b1600052d19)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acddbc",
  "name": "FUN_00acddbc",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "140bcdbb7aa2293e32c2413214e4851318ac3d5917545375975af957326ff683",
  "source_text_sha256": "140bcdbb7aa2293e32c2413214e4851318ac3d5917545375975af957326ff683",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acddbc",
        "00acddff"
      ]
    ],
    "bytes_sha256": "8fd9d5885de3b227e19bf7b8fe801053209db680cf0fc1b06dce7a7dc73e2a48",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00657e7c](../00657/00657e7c.md)

## 呼び出し先

- [00adccd8](../00adc/00adccd8.md)
- [00bdb240](../00bdb/00bdb240.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 188 bytes

~~~c

void FUN_00acddbc(undefined8 *param_1)

{
  FUN_00adccd8();
  *param_1 = &PTR_FUN_00bf7308;
  memset(param_1 + 0x15,0,0x220);
  *(undefined4 *)(param_1 + 0x59) = 0x3f800000;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acddbc"></a> `00acddbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acddc0"></a> `00acddc0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acddc4"></a> `00acddc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acddc8"></a> `00acddc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acddcc"></a> `00acddcc` | `c3 3b 00 94` | bl 0x00adccd8 | `UNCONDITIONAL_CALL`
<a id="insn-00acddd0"></a> `00acddd0` | `48 09 00 d0` | adrp x8,0xbf7000 | `FALL_THROUGH`
<a id="insn-00acddd4"></a> `00acddd4` | `08 21 0c 91` | add x8,x8,#0x308 | `FALL_THROUGH`
<a id="insn-00acddd8"></a> `00acddd8` | `60 a2 02 91` | add x0,x19,#0xa8 | `FALL_THROUGH`
<a id="insn-00acdddc"></a> `00acdddc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acdde0"></a> `00acdde0` | `02 44 80 52` | mov w2,#0x220 | `FALL_THROUGH`
<a id="insn-00acdde4"></a> `00acdde4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00acdde8"></a> `00acdde8` | `16 35 04 94` | bl 0x00bdb240 | `UNCONDITIONAL_CALL`
<a id="insn-00acddec"></a> `00acddec` | `08 f0 a7 52` | mov w8,#0x3f800000 | `FALL_THROUGH`
<a id="insn-00acddf0"></a> `00acddf0` | `68 ca 02 b9` | str w8,[x19, #0x2c8] | `FALL_THROUGH`
<a id="insn-00acddf4"></a> `00acddf4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acddf8"></a> `00acddf8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acddfc"></a> `00acddfc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acddbc`](#insn-00acddbc) 範囲 `[['00acddbc', '00acddff']]`

## 命令位置別の参照

- [`00acddbc`](#insn-00acddbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acddc0`](#insn-00acddc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acddcc`](#insn-00acddcc) → [`00adccd8`](../00adc/00adccd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adccd8` · 推定シンボル `None` · 推定型 `None`
- [`00acdde4`](#insn-00acdde4) → `00bf7308`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acdde8`](#insn-00acdde8) → [`00bdb240`](../00bdb/00bdb240.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb240` · 推定シンボル `None` · 推定型 `None`
- [`00acddf4`](#insn-00acddf4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acddf8`](#insn-00acddf8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acddbc`](#insn-00acddbc)

~~~json
{
  "source": "00acddbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acddc0`](#insn-00acddc0)

~~~json
{
  "source": "00acddc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acddcc`](#insn-00acddcc)

~~~json
{
  "source": "00acddcc",
  "target": "00adccd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acdde4`](#insn-00acdde4)

~~~json
{
  "source": "00acdde4",
  "target": "00bf7308",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00bf7308",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acdde8`](#insn-00acdde8)

~~~json
{
  "source": "00acdde8",
  "target": "00bdb240",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acddf4`](#insn-00acddf4)

~~~json
{
  "source": "00acddf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acddf8`](#insn-00acddf8)

~~~json
{
  "source": "00acddf8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
