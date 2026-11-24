# 00a8dcfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a8db04`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8d/00a8db04.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0062.md#compare-5d3920838802e21d982ea20b936868ad)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a8dd6c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a8d/00a8dd6c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0063.md#compare-3857806d850c411eca34349379916af6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a8dcfc",
  "name": "FUN_00a8dcfc",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4ea9204233f5bd8f1ee5d25803793bdafb647bdb03c885f85ed56c11ce30e602",
  "source_text_sha256": "4ea9204233f5bd8f1ee5d25803793bdafb647bdb03c885f85ed56c11ce30e602",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a8dcfc",
        "00a8ddb7"
      ]
    ],
    "bytes_sha256": "72555bad310a161367017f22f96b1eee9e4739329e2f2993bcfc887bc336f554",
    "instruction_count": 47,
    "instruction_bytes": 188,
    "body_bytes": 188,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00851a0c](../00851/00851a0c.md)
- [00a8a418](../00a8a/00a8a418.md)

## 呼び出し先

- [007683d8](../00768/007683d8.md)
- [00a91af8](../00a91/00a91af8.md)
- [00a91e10](../00a91/00a91e10.md)
- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 677 bytes

~~~c

void FUN_00a8dcfc(long param_1)

{
  int iVar1;
  ulong uVar2;
  
  uVar2 = FUN_007683d8();
  if ((uVar2 & 1) != 0) {
    *(undefined1 *)(param_1 + 0x2030) = 0;
    if (((DAT_00ca4f38 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_00ca4f38), iVar1 != 0)) {
      DAT_00ca4f08 = 0;
      DAT_00ca4f00 = &DAT_00ca4f08;
      DAT_00ca4f28 = 0;
      DAT_00ca4f30 = 0;
      DAT_00ca4f20 = 0;
      DAT_00ca4f10 = 0;
      DAT_00ca4f18 = &DAT_00ca4f20;
      __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
      __cxa_guard_release(&DAT_00ca4f38);
    }
    FUN_00a91af8(param_1,&DAT_00ca4f00);
    FUN_00a91e10(param_1,&DAT_00ca4f00);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a8dcfc"></a> `00a8dcfc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a8dd00"></a> `00a8dd00` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a8dd04"></a> `00a8dd04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a8dd08"></a> `00a8dd08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a8dd0c"></a> `00a8dd0c` | `b3 69 f3 97` | bl 0x007683d8 | `UNCONDITIONAL_CALL`
<a id="insn-00a8dd10"></a> `00a8dd10` | `20 02 00 36` | tbz w0,#0x0,0x00a8dd54 | `CONDITIONAL_JUMP`
<a id="insn-00a8dd14"></a> `00a8dd14` | `08 06 84 52` | mov w8,#0x2030 | `FALL_THROUGH`
<a id="insn-00a8dd18"></a> `00a8dd18` | `7f 6a 28 38` | strb wzr,[x19, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00a8dd1c"></a> `00a8dd1c` | `a8 10 00 f0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-00a8dd20"></a> `00a8dd20` | `08 e1 3c 91` | add x8,x8,#0xf38 | `FALL_THROUGH`
<a id="insn-00a8dd24"></a> `00a8dd24` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00a8dd28"></a> `00a8dd28` | `c8 01 00 36` | tbz w8,#0x0,0x00a8dd60 | `CONDITIONAL_JUMP`
<a id="insn-00a8dd2c"></a> `00a8dd2c` | `b4 10 00 f0` | adrp x20,0xca4000 | `FALL_THROUGH`
<a id="insn-00a8dd30"></a> `00a8dd30` | `94 02 3c 91` | add x20,x20,#0xf00 | `FALL_THROUGH`
<a id="insn-00a8dd34"></a> `00a8dd34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a8dd38"></a> `00a8dd38` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00a8dd3c"></a> `00a8dd3c` | `6f 0f 00 94` | bl 0x00a91af8 | `UNCONDITIONAL_CALL`
<a id="insn-00a8dd40"></a> `00a8dd40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a8dd44"></a> `00a8dd44` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00a8dd48"></a> `00a8dd48` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a8dd4c"></a> `00a8dd4c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a8dd50"></a> `00a8dd50` | `30 10 00 14` | b 0x00a91e10 | `CALL_TERMINATOR`
<a id="insn-00a8dd54"></a> `00a8dd54` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a8dd58"></a> `00a8dd58` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a8dd5c"></a> `00a8dd5c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a8dd60"></a> `00a8dd60` | `a0 10 00 f0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00a8dd64"></a> `00a8dd64` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00a8dd68"></a> `00a8dd68` | `3a 28 07 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00a8dd6c"></a> `00a8dd6c` | `00 fe ff 34` | cbz w0,0x00a8dd2c | `CONDITIONAL_JUMP`
<a id="insn-00a8dd70"></a> `00a8dd70` | `a1 10 00 f0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-00a8dd74"></a> `00a8dd74` | `21 00 3c 91` | add x1,x1,#0xf00 | `FALL_THROUGH`
<a id="insn-00a8dd78"></a> `00a8dd78` | `80 cf ff b0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-00a8dd7c"></a> `00a8dd7c` | `00 d0 36 91` | add x0,x0,#0xdb4 | `FALL_THROUGH`
<a id="insn-00a8dd80"></a> `00a8dd80` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00a8dd84"></a> `00a8dd84` | `a2 0e 00 b0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-00a8dd88"></a> `00a8dd88` | `42 40 3e 91` | add x2,x2,#0xf90 | `FALL_THROUGH`
<a id="insn-00a8dd8c"></a> `00a8dd8c` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00a8dd90"></a> `00a8dd90` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00a8dd94"></a> `00a8dd94` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00a8dd98"></a> `00a8dd98` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00a8dd9c"></a> `00a8dd9c` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00a8dda0"></a> `00a8dda0` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00a8dda4"></a> `00a8dda4` | `23 28 07 94` | bl 0x00c57e30 | `UNCONDITIONAL_CALL`
<a id="insn-00a8dda8"></a> `00a8dda8` | `a0 10 00 f0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-00a8ddac"></a> `00a8ddac` | `00 e0 3c 91` | add x0,x0,#0xf38 | `FALL_THROUGH`
<a id="insn-00a8ddb0"></a> `00a8ddb0` | `30 28 07 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00a8ddb4"></a> `00a8ddb4` | `de ff ff 17` | b 0x00a8dd2c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00a8dcfc`](#insn-00a8dcfc) 範囲 `[['00a8dcfc', '00a8dd13']]`
  - `CONDITIONAL_JUMP` [`00a8dd10`](#insn-00a8dd10) → [`00a8dd54`](#insn-00a8dd54)
  - `FALL_THROUGH` [`00a8dd10`](#insn-00a8dd10) → [`00a8dd14`](#insn-00a8dd14)
- ブロック [`00a8dd14`](#insn-00a8dd14) 範囲 `[['00a8dd14', '00a8dd2b']]`
  - `CONDITIONAL_JUMP` [`00a8dd28`](#insn-00a8dd28) → [`00a8dd60`](#insn-00a8dd60)
  - `FALL_THROUGH` [`00a8dd28`](#insn-00a8dd28) → [`00a8dd2c`](#insn-00a8dd2c)
- ブロック [`00a8dd2c`](#insn-00a8dd2c) 範囲 `[['00a8dd2c', '00a8dd53']]`
- ブロック [`00a8dd54`](#insn-00a8dd54) 範囲 `[['00a8dd54', '00a8dd5f']]`
- ブロック [`00a8dd60`](#insn-00a8dd60) 範囲 `[['00a8dd60', '00a8dd6f']]`
  - `CONDITIONAL_JUMP` [`00a8dd6c`](#insn-00a8dd6c) → [`00a8dd2c`](#insn-00a8dd2c)
  - `FALL_THROUGH` [`00a8dd6c`](#insn-00a8dd6c) → [`00a8dd70`](#insn-00a8dd70)
- ブロック [`00a8dd70`](#insn-00a8dd70) 範囲 `[['00a8dd70', '00a8ddb7']]`
  - `UNCONDITIONAL_JUMP` [`00a8ddb4`](#insn-00a8ddb4) → [`00a8dd2c`](#insn-00a8dd2c)

## 命令位置別の参照

- [`00a8dcfc`](#insn-00a8dcfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd00`](#insn-00a8dd00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd0c`](#insn-00a8dd0c) → [`007683d8`](../00768/007683d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007683d8` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd10`](#insn-00a8dd10) → [`00a8dd54`](#insn-00a8dd54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd24`](#insn-00a8dd24) → `00ca4f38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a8dd28`](#insn-00a8dd28) → [`00a8dd60`](#insn-00a8dd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd38`](#insn-00a8dd38) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dd3c`](#insn-00a8dd3c) → [`00a91af8`](../00a91/00a91af8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a91af8` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd44`](#insn-00a8dd44) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dd48`](#insn-00a8dd48) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd4c`](#insn-00a8dd4c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd50`](#insn-00a8dd50) → [`00a91e10`](../00a91/00a91e10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a91e10` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd54`](#insn-00a8dd54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd58`](#insn-00a8dd58) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd64`](#insn-00a8dd64) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a8dd68`](#insn-00a8dd68) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd6c`](#insn-00a8dd6c) → [`00a8dd2c`](#insn-00a8dd2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd74`](#insn-00a8dd74) → `00ca4f00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dd7c`](#insn-00a8dd7c) → [`0047edb4`](../0047e/0047edb4.md) · `PARAM` · `ANALYSIS` · 関数 `0047edb4` · 推定シンボル `None` · 推定型 `None`
- [`00a8dd88`](#insn-00a8dd88) → `00c62f90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00a8dd8c`](#insn-00a8dd8c) → `00ca4f08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dd90`](#insn-00a8dd90) → `00ca4f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dd90`](#insn-00a8dd90) → `00ca4f08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dd98`](#insn-00a8dd98) → `00ca4f28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dd98`](#insn-00a8dd98) → `00ca4f30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dd9c`](#insn-00a8dd9c) → `00ca4f20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dda0`](#insn-00a8dda0) → `00ca4f10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dda0`](#insn-00a8dda0) → `00ca4f18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dda0`](#insn-00a8dda0) → `00ca4f20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00a8dda4`](#insn-00a8dda4) → [`00c57e30`](../00c57/00c57e30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e30` · 推定シンボル `None` · 推定型 `None`
- [`00a8ddac`](#insn-00a8ddac) → `00ca4f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00a8ddb0`](#insn-00a8ddb0) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00a8ddb4`](#insn-00a8ddb4) → [`00a8dd2c`](#insn-00a8dd2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a8dcfc`](#insn-00a8dcfc)

~~~json
{
  "source": "00a8dcfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8dd00`](#insn-00a8dd00)

~~~json
{
  "source": "00a8dd00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8dd0c`](#insn-00a8dd0c)

~~~json
{
  "source": "00a8dd0c",
  "target": "007683d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8dd10`](#insn-00a8dd10)

~~~json
{
  "source": "00a8dd10",
  "target": "00a8dd54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8dd24`](#insn-00a8dd24)

~~~json
{
  "source": "00a8dd24",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dd28`](#insn-00a8dd28)

~~~json
{
  "source": "00a8dd28",
  "target": "00a8dd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8dd38`](#insn-00a8dd38)

~~~json
{
  "source": "00a8dd38",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dd3c`](#insn-00a8dd3c)

~~~json
{
  "source": "00a8dd3c",
  "target": "00a91af8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8dd44`](#insn-00a8dd44)

~~~json
{
  "source": "00a8dd44",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dd48`](#insn-00a8dd48)

~~~json
{
  "source": "00a8dd48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8dd4c`](#insn-00a8dd4c)

~~~json
{
  "source": "00a8dd4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8dd50`](#insn-00a8dd50)

~~~json
{
  "source": "00a8dd50",
  "target": "00a91e10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8dd54`](#insn-00a8dd54)

~~~json
{
  "source": "00a8dd54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8dd58`](#insn-00a8dd58)

~~~json
{
  "source": "00a8dd58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8dd64`](#insn-00a8dd64)

~~~json
{
  "source": "00a8dd64",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dd68`](#insn-00a8dd68)

~~~json
{
  "source": "00a8dd68",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8dd6c`](#insn-00a8dd6c)

~~~json
{
  "source": "00a8dd6c",
  "target": "00a8dd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a8dd74`](#insn-00a8dd74)

~~~json
{
  "source": "00a8dd74",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dd7c`](#insn-00a8dd7c)

~~~json
{
  "source": "00a8dd7c",
  "target": "0047edb4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8dd88`](#insn-00a8dd88)

~~~json
{
  "source": "00a8dd88",
  "target": "00c62f90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62f90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a8dd8c`](#insn-00a8dd8c)

~~~json
{
  "source": "00a8dd8c",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dd90`](#insn-00a8dd90)

~~~json
{
  "source": "00a8dd90",
  "target": "00ca4f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dd90`](#insn-00a8dd90)

~~~json
{
  "source": "00a8dd90",
  "target": "00ca4f08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dd98`](#insn-00a8dd98)

~~~json
{
  "source": "00a8dd98",
  "target": "00ca4f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dd98`](#insn-00a8dd98)

~~~json
{
  "source": "00a8dd98",
  "target": "00ca4f30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dd9c`](#insn-00a8dd9c)

~~~json
{
  "source": "00a8dd9c",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dda0`](#insn-00a8dda0)

~~~json
{
  "source": "00a8dda0",
  "target": "00ca4f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dda0`](#insn-00a8dda0)

~~~json
{
  "source": "00a8dda0",
  "target": "00ca4f18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dda0`](#insn-00a8dda0)

~~~json
{
  "source": "00a8dda0",
  "target": "00ca4f20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8dda4`](#insn-00a8dda4)

~~~json
{
  "source": "00a8dda4",
  "target": "00c57e30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8ddac`](#insn-00a8ddac)

~~~json
{
  "source": "00a8ddac",
  "target": "00ca4f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4f38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00a8ddb0`](#insn-00a8ddb0)

~~~json
{
  "source": "00a8ddb0",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a8ddb4`](#insn-00a8ddb4)

~~~json
{
  "source": "00a8ddb4",
  "target": "00a8dd2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
