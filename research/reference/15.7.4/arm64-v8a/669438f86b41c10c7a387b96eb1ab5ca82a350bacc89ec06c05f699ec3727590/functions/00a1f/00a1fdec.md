# 00a1fdec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a1fda8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a1f/00a1fda8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0001.md#compare-9c21350ae15f5eef8987a012fd0f813f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a7dc7c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a7d/00a7dc7c.md) · 移動量 `+0x5de90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0013.md#compare-d816bfd6455b92b54f26dc83fc851e52)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a1fdec",
  "name": "FUN_00a1fdec",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8060844e4292cb0105d28455cc2b5d22b7d7418fc3f6ae5217e4f36042264052",
  "source_text_sha256": "8060844e4292cb0105d28455cc2b5d22b7d7418fc3f6ae5217e4f36042264052",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a1fdec",
        "00a1fe1f"
      ]
    ],
    "bytes_sha256": "fcceeaca9852e50fbfb674616855d59ba9038318203ac81c30c00ce7085d90d0",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 515 bytes

~~~c

void FUN_00a1fdec(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
                    /* try { // try from 00a1fdf0 to 00b1fdfb has its CatchHandler @ 00a2a8c8 */
                    /* try { // try from 00a1fdfc to 00b1fe0f has its CatchHandler @ 00a2a8a4 */
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00a1fe10 to 00b1fe37 has its CatchHandler @ 00a2a878 */
  *puVar1 = &PTR_FUN_00c0c400;
  puVar1[1] = uVar2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a1fdec"></a> `00a1fdec` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a1fdf0"></a> `00a1fdf0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a1fdf4"></a> `00a1fdf4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a1fdf8"></a> `00a1fdf8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a1fdfc"></a> `00a1fdfc` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00a1fe00"></a> `00a1fe00` | `90 ec 06 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00a1fe04"></a> `00a1fe04` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a1fe08"></a> `00a1fe08` | `68 0f 00 b0` | adrp x8,0xc0c000 | `FALL_THROUGH`
<a id="insn-00a1fe0c"></a> `00a1fe0c` | `08 01 10 91` | add x8,x8,#0x400 | `FALL_THROUGH`
<a id="insn-00a1fe10"></a> `00a1fe10` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00a1fe14"></a> `00a1fe14` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a1fe18"></a> `00a1fe18` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a1fe1c"></a> `00a1fe1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a1fdec`](#insn-00a1fdec) 範囲 `[['00a1fdec', '00a1fdef']]`
  - `FALL_THROUGH` [`00a1fdec`](#insn-00a1fdec) → [`00a1fdf0`](#insn-00a1fdf0)
- ブロック [`00a1fdf0`](#insn-00a1fdf0) 範囲 `[['00a1fdf0', '00a1fdfb']]`
  - `FALL_THROUGH` [`00a1fdf8`](#insn-00a1fdf8) → [`00a1fdfc`](#insn-00a1fdfc)
- ブロック [`00a1fdfc`](#insn-00a1fdfc) 範囲 `[['00a1fdfc', '00a1fe0f']]`
  - `FALL_THROUGH` [`00a1fe0c`](#insn-00a1fe0c) → [`00a1fe10`](#insn-00a1fe10)
- ブロック [`00a1fe10`](#insn-00a1fe10) 範囲 `[['00a1fe10', '00a1fe1f']]`

## 命令位置別の参照

- [`00a1fdec`](#insn-00a1fdec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1fdf0`](#insn-00a1fdf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1fe00`](#insn-00a1fe00) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00a1fe10`](#insn-00a1fe10) → `00c0c400`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a1fe14`](#insn-00a1fe14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a1fe18`](#insn-00a1fe18) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a1fdec`](#insn-00a1fdec)

~~~json
{
  "source": "00a1fdec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1fdf0`](#insn-00a1fdf0)

~~~json
{
  "source": "00a1fdf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1fe00`](#insn-00a1fe00)

~~~json
{
  "source": "00a1fe00",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a1fe10`](#insn-00a1fe10)

~~~json
{
  "source": "00a1fe10",
  "target": "00c0c400",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0c400",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a1fe14`](#insn-00a1fe14)

~~~json
{
  "source": "00a1fe14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a1fe18`](#insn-00a1fe18)

~~~json
{
  "source": "00a1fe18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
