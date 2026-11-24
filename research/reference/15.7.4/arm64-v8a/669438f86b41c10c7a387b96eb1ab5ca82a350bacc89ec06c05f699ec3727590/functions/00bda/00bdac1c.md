# 00bdac1c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdabdc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdabdc.md) · 移動量 `+0x40`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-8f3ec2a6deacec6eb30d56ce07a970bc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5766c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c57/00c5766c.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0079.md#compare-7e4fa1f75c379843bb34893611bc8578)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdac1c",
  "name": "FUN_00bdac1c",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07e5efe3dd140e677898eb6008e03fa309d36baf715d7ef38206032e01432596",
  "source_text_sha256": "07e5efe3dd140e677898eb6008e03fa309d36baf715d7ef38206032e01432596",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdac1c",
        "00bdad17"
      ]
    ],
    "bytes_sha256": "658522320678155fdffb0e2d118132d05e24808003646acdc692a15e1e3fb8c3",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdaab4](../00bda/00bdaab4.md)

## 呼び出し先

- [00bdd360](../00bdd/00bdd360.md)
- [00bde2c0](../00bde/00bde2c0.md)
- [00be1f80](../00be1/00be1f80.md)

## 関連文字列（未確認候補）

~~~text
"Can't binary search on variable length encoded data."
"Unknown DWARF encoding for search table."
"getTableEntrySize"
"libunwind: %s - %s\n"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1989 bytes

~~~c

undefined8 FUN_00bdac1c(uint param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR___sF_00c1bd48;
  param_1 = param_1 & 0xf;
                    /* try { // try from 00bdac38 to 00cdac87 has its CatchHandler @ 00bdac38
                       catch() { ... } // from try @ 00bdac38 with catch @ 00bdac38
                       catch() { ... } // from try @ 00bdacdc with catch @ 00bdac38 */
  if (param_1 < 9) {
    if (param_1 < 3) {
      if (param_1 == 2) {
        return 4;
      }
      if (param_1 == 1) {
LAB_00bdace4:
        fprintf((FILE *)(PTR___sF_00c1bd48 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
                "Can\'t binary search on variable length encoded data.");
                    /* try { // try from 00bdad0c to 00cdad33 has its CatchHandler @ 00bdad0c
                       catch() { ... } // from try @ 00bdad0c with catch @ 00bdad0c
                       catch() { ... } // from try @ 00bdad6c with catch @ 00bdad0c */
        fflush((FILE *)(puVar1 + 0x130));
                    /* WARNING: Subroutine does not return */
        abort();
      }
    }
    else {
      if (param_1 == 3) {
        return 8;
      }
      if (param_1 == 4) {
        return 0x10;
      }
    }
  }
  else if (param_1 < 0xb) {
    if (param_1 == 10) {
      return 4;
    }
                    /* catch() { ... } // from try @ 00bdac88 with catch @ 00bdacdc
                       try { // try from 00bdacdc to 00cdad0b has its CatchHandler @ 00bdac38 */
    if (param_1 == 9) goto LAB_00bdace4;
  }
  else {
    if (param_1 == 0xc) {
                    /* try { // try from 00bdac88 to 00cdacdb has its CatchHandler @ 00bdacdc */
      return 0x10;
    }
    if (param_1 == 0xb) {
      return 8;
    }
  }
  fprintf((FILE *)(PTR___sF_00c1bd48 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
          "Unknown DWARF encoding for search table.");
  fflush((FILE *)(puVar1 + 0x130));
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdac1c"></a> `00bdac1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bdac20"></a> `00bdac20` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdac24"></a> `00bdac24` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdac28"></a> `00bdac28` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bdac2c"></a> `00bdac2c` | `08 0c 00 12` | and w8,w0,#0xf | `FALL_THROUGH`
<a id="insn-00bdac30"></a> `00bdac30` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00bdac34"></a> `00bdac34` | `1f 21 00 71` | cmp w8,#0x8 | `FALL_THROUGH`
<a id="insn-00bdac38"></a> `00bdac38` | `0c 01 00 54` | b.gt 0x00bdac58 | `CONDITIONAL_JUMP`
<a id="insn-00bdac3c"></a> `00bdac3c` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bdac40"></a> `00bdac40` | `cd 02 00 54` | b.le 0x00bdac98 | `CONDITIONAL_JUMP`
<a id="insn-00bdac44"></a> `00bdac44` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bdac48"></a> `00bdac48` | `40 01 00 54` | b.eq 0x00bdac70 | `CONDITIONAL_JUMP`
<a id="insn-00bdac4c"></a> `00bdac4c` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bdac50"></a> `00bdac50` | `a0 01 00 54` | b.eq 0x00bdac84 | `CONDITIONAL_JUMP`
<a id="insn-00bdac54"></a> `00bdac54` | `14 00 00 14` | b 0x00bdaca4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdac58"></a> `00bdac58` | `1f 29 00 71` | cmp w8,#0xa | `FALL_THROUGH`
<a id="insn-00bdac5c"></a> `00bdac5c` | `ed 03 00 54` | b.le 0x00bdacd8 | `CONDITIONAL_JUMP`
<a id="insn-00bdac60"></a> `00bdac60` | `1f 31 00 71` | cmp w8,#0xc | `FALL_THROUGH`
<a id="insn-00bdac64"></a> `00bdac64` | `00 01 00 54` | b.eq 0x00bdac84 | `CONDITIONAL_JUMP`
<a id="insn-00bdac68"></a> `00bdac68` | `1f 2d 00 71` | cmp w8,#0xb | `FALL_THROUGH`
<a id="insn-00bdac6c"></a> `00bdac6c` | `c1 01 00 54` | b.ne 0x00bdaca4 | `CONDITIONAL_JUMP`
<a id="insn-00bdac70"></a> `00bdac70` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00bdac74"></a> `00bdac74` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdac78"></a> `00bdac78` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdac7c"></a> `00bdac7c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdac80"></a> `00bdac80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdac84"></a> `00bdac84` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00bdac88"></a> `00bdac88` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdac8c"></a> `00bdac8c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdac90"></a> `00bdac90` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdac94"></a> `00bdac94` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdac98"></a> `00bdac98` | `e0 fe ff 54` | b.eq 0x00bdac74 | `CONDITIONAL_JUMP`
<a id="insn-00bdac9c"></a> `00bdac9c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bdaca0"></a> `00bdaca0` | `20 02 00 54` | b.eq 0x00bdace4 | `CONDITIONAL_JUMP`
<a id="insn-00bdaca4"></a> `00bdaca4` | `13 02 00 b0` | adrp x19,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bdaca8"></a> `00bdaca8` | `a1 b5 ff f0` | adrp x1,0x291000 | `FALL_THROUGH`
<a id="insn-00bdacac"></a> `00bdacac` | `21 ac 20 91` | add x1,x1,#0x82b | `FALL_THROUGH`
<a id="insn-00bdacb0"></a> `00bdacb0` | `73 a6 46 f9` | ldr x19,[x19, #0xd48] | `FALL_THROUGH`
<a id="insn-00bdacb4"></a> `00bdacb4` | `e2 b5 ff f0` | adrp x2,0x299000 | `FALL_THROUGH`
<a id="insn-00bdacb8"></a> `00bdacb8` | `42 3c 2a 91` | add x2,x2,#0xa8f | `FALL_THROUGH`
<a id="insn-00bdacbc"></a> `00bdacbc` | `63 b6 ff f0` | adrp x3,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdacc0"></a> `00bdacc0` | `63 7c 08 91` | add x3,x3,#0x21f | `FALL_THROUGH`
<a id="insn-00bdacc4"></a> `00bdacc4` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdacc8"></a> `00bdacc8` | `ae 1c 00 94` | bl 0x00be1f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaccc"></a> `00bdaccc` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdacd0"></a> `00bdacd0` | `a4 09 00 94` | bl 0x00bdd360 | `UNCONDITIONAL_CALL`
<a id="insn-00bdacd4"></a> `00bdacd4` | `7b 0d 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bdacd8"></a> `00bdacd8` | `e0 fc ff 54` | b.eq 0x00bdac74 | `CONDITIONAL_JUMP`
<a id="insn-00bdacdc"></a> `00bdacdc` | `1f 25 00 71` | cmp w8,#0x9 | `FALL_THROUGH`
<a id="insn-00bdace0"></a> `00bdace0` | `21 fe ff 54` | b.ne 0x00bdaca4 | `CONDITIONAL_JUMP`
<a id="insn-00bdace4"></a> `00bdace4` | `13 02 00 b0` | adrp x19,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bdace8"></a> `00bdace8` | `a1 b5 ff f0` | adrp x1,0x291000 | `FALL_THROUGH`
<a id="insn-00bdacec"></a> `00bdacec` | `21 ac 20 91` | add x1,x1,#0x82b | `FALL_THROUGH`
<a id="insn-00bdacf0"></a> `00bdacf0` | `73 a6 46 f9` | ldr x19,[x19, #0xd48] | `FALL_THROUGH`
<a id="insn-00bdacf4"></a> `00bdacf4` | `e2 b5 ff f0` | adrp x2,0x299000 | `FALL_THROUGH`
<a id="insn-00bdacf8"></a> `00bdacf8` | `42 3c 2a 91` | add x2,x2,#0xa8f | `FALL_THROUGH`
<a id="insn-00bdacfc"></a> `00bdacfc` | `c3 b5 ff f0` | adrp x3,0x295000 | `FALL_THROUGH`
<a id="insn-00bdad00"></a> `00bdad00` | `63 00 20 91` | add x3,x3,#0x800 | `FALL_THROUGH`
<a id="insn-00bdad04"></a> `00bdad04` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdad08"></a> `00bdad08` | `9e 1c 00 94` | bl 0x00be1f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdad0c"></a> `00bdad0c` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdad10"></a> `00bdad10` | `94 09 00 94` | bl 0x00bdd360 | `UNCONDITIONAL_CALL`
<a id="insn-00bdad14"></a> `00bdad14` | `6b 0d 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdac1c`](#insn-00bdac1c) 範囲 `[['00bdac1c', '00bdac37']]`
  - `FALL_THROUGH` [`00bdac34`](#insn-00bdac34) → [`00bdac38`](#insn-00bdac38)
- ブロック [`00bdac38`](#insn-00bdac38) 範囲 `[['00bdac38', '00bdac3b']]`
  - `CONDITIONAL_JUMP` [`00bdac38`](#insn-00bdac38) → [`00bdac58`](#insn-00bdac58)
  - `FALL_THROUGH` [`00bdac38`](#insn-00bdac38) → [`00bdac3c`](#insn-00bdac3c)
- ブロック [`00bdac3c`](#insn-00bdac3c) 範囲 `[['00bdac3c', '00bdac43']]`
  - `CONDITIONAL_JUMP` [`00bdac40`](#insn-00bdac40) → [`00bdac98`](#insn-00bdac98)
  - `FALL_THROUGH` [`00bdac40`](#insn-00bdac40) → [`00bdac44`](#insn-00bdac44)
- ブロック [`00bdac44`](#insn-00bdac44) 範囲 `[['00bdac44', '00bdac4b']]`
  - `CONDITIONAL_JUMP` [`00bdac48`](#insn-00bdac48) → [`00bdac70`](#insn-00bdac70)
  - `FALL_THROUGH` [`00bdac48`](#insn-00bdac48) → [`00bdac4c`](#insn-00bdac4c)
- ブロック [`00bdac4c`](#insn-00bdac4c) 範囲 `[['00bdac4c', '00bdac53']]`
  - `CONDITIONAL_JUMP` [`00bdac50`](#insn-00bdac50) → [`00bdac84`](#insn-00bdac84)
  - `FALL_THROUGH` [`00bdac50`](#insn-00bdac50) → [`00bdac54`](#insn-00bdac54)
- ブロック [`00bdac54`](#insn-00bdac54) 範囲 `[['00bdac54', '00bdac57']]`
  - `UNCONDITIONAL_JUMP` [`00bdac54`](#insn-00bdac54) → [`00bdaca4`](#insn-00bdaca4)
- ブロック [`00bdac58`](#insn-00bdac58) 範囲 `[['00bdac58', '00bdac5f']]`
  - `CONDITIONAL_JUMP` [`00bdac5c`](#insn-00bdac5c) → [`00bdacd8`](#insn-00bdacd8)
  - `FALL_THROUGH` [`00bdac5c`](#insn-00bdac5c) → [`00bdac60`](#insn-00bdac60)
- ブロック [`00bdac60`](#insn-00bdac60) 範囲 `[['00bdac60', '00bdac67']]`
  - `CONDITIONAL_JUMP` [`00bdac64`](#insn-00bdac64) → [`00bdac84`](#insn-00bdac84)
  - `FALL_THROUGH` [`00bdac64`](#insn-00bdac64) → [`00bdac68`](#insn-00bdac68)
- ブロック [`00bdac68`](#insn-00bdac68) 範囲 `[['00bdac68', '00bdac6f']]`
  - `CONDITIONAL_JUMP` [`00bdac6c`](#insn-00bdac6c) → [`00bdaca4`](#insn-00bdaca4)
  - `FALL_THROUGH` [`00bdac6c`](#insn-00bdac6c) → [`00bdac70`](#insn-00bdac70)
- ブロック [`00bdac70`](#insn-00bdac70) 範囲 `[['00bdac70', '00bdac73']]`
  - `FALL_THROUGH` [`00bdac70`](#insn-00bdac70) → [`00bdac74`](#insn-00bdac74)
- ブロック [`00bdac74`](#insn-00bdac74) 範囲 `[['00bdac74', '00bdac83']]`
- ブロック [`00bdac84`](#insn-00bdac84) 範囲 `[['00bdac84', '00bdac87']]`
  - `FALL_THROUGH` [`00bdac84`](#insn-00bdac84) → [`00bdac88`](#insn-00bdac88)
- ブロック [`00bdac88`](#insn-00bdac88) 範囲 `[['00bdac88', '00bdac97']]`
- ブロック [`00bdac98`](#insn-00bdac98) 範囲 `[['00bdac98', '00bdac9b']]`
  - `CONDITIONAL_JUMP` [`00bdac98`](#insn-00bdac98) → [`00bdac74`](#insn-00bdac74)
  - `FALL_THROUGH` [`00bdac98`](#insn-00bdac98) → [`00bdac9c`](#insn-00bdac9c)
- ブロック [`00bdac9c`](#insn-00bdac9c) 範囲 `[['00bdac9c', '00bdaca3']]`
  - `CONDITIONAL_JUMP` [`00bdaca0`](#insn-00bdaca0) → [`00bdace4`](#insn-00bdace4)
  - `FALL_THROUGH` [`00bdaca0`](#insn-00bdaca0) → [`00bdaca4`](#insn-00bdaca4)
- ブロック [`00bdaca4`](#insn-00bdaca4) 範囲 `[['00bdaca4', '00bdacd7']]`
- ブロック [`00bdacd8`](#insn-00bdacd8) 範囲 `[['00bdacd8', '00bdacdb']]`
  - `CONDITIONAL_JUMP` [`00bdacd8`](#insn-00bdacd8) → [`00bdac74`](#insn-00bdac74)
  - `FALL_THROUGH` [`00bdacd8`](#insn-00bdacd8) → [`00bdacdc`](#insn-00bdacdc)
- ブロック [`00bdacdc`](#insn-00bdacdc) 範囲 `[['00bdacdc', '00bdace3']]`
  - `CONDITIONAL_JUMP` [`00bdace0`](#insn-00bdace0) → [`00bdaca4`](#insn-00bdaca4)
  - `FALL_THROUGH` [`00bdace0`](#insn-00bdace0) → [`00bdace4`](#insn-00bdace4)
- ブロック [`00bdace4`](#insn-00bdace4) 範囲 `[['00bdace4', '00bdad0b']]`
  - `FALL_THROUGH` [`00bdad08`](#insn-00bdad08) → [`00bdad0c`](#insn-00bdad0c)
- ブロック [`00bdad0c`](#insn-00bdad0c) 範囲 `[['00bdad0c', '00bdad17']]`

## 命令位置別の参照

- [`00bdac20`](#insn-00bdac20) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac24`](#insn-00bdac24) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac38`](#insn-00bdac38) → [`00bdac58`](#insn-00bdac58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac40`](#insn-00bdac40) → [`00bdac98`](#insn-00bdac98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac48`](#insn-00bdac48) → [`00bdac70`](#insn-00bdac70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac50`](#insn-00bdac50) → [`00bdac84`](#insn-00bdac84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac54`](#insn-00bdac54) → [`00bdaca4`](#insn-00bdaca4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac5c`](#insn-00bdac5c) → [`00bdacd8`](#insn-00bdacd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac64`](#insn-00bdac64) → [`00bdac84`](#insn-00bdac84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac6c`](#insn-00bdac6c) → [`00bdaca4`](#insn-00bdaca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac74`](#insn-00bdac74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac78`](#insn-00bdac78) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac88`](#insn-00bdac88) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac8c`](#insn-00bdac8c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac98`](#insn-00bdac98) → [`00bdac74`](#insn-00bdac74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaca0`](#insn-00bdaca0) → [`00bdace4`](#insn-00bdace4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdacac`](#insn-00bdacac) → `0029182b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdacb0`](#insn-00bdacb0) → `00c1bd48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdacb8`](#insn-00bdacb8) → `00299a8f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdacc0`](#insn-00bdacc0) → `002a921f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdacc4`](#insn-00bdacc4) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdacc8`](#insn-00bdacc8) → [`00be1f80`](../00be1/00be1f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1f80` · 推定シンボル `None` · 推定型 `None`
- [`00bdaccc`](#insn-00bdaccc) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdacd0`](#insn-00bdacd0) → [`00bdd360`](../00bdd/00bdd360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd360` · 推定シンボル `None` · 推定型 `None`
- [`00bdacd4`](#insn-00bdacd4) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bdacd8`](#insn-00bdacd8) → [`00bdac74`](#insn-00bdac74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdace0`](#insn-00bdace0) → [`00bdaca4`](#insn-00bdaca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdacec`](#insn-00bdacec) → `0029182b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdacf0`](#insn-00bdacf0) → `00c1bd48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdacf8`](#insn-00bdacf8) → `00299a8f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdad00`](#insn-00bdad00) → `00295800`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdad04`](#insn-00bdad04) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdad08`](#insn-00bdad08) → [`00be1f80`](../00be1/00be1f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1f80` · 推定シンボル `None` · 推定型 `None`
- [`00bdad0c`](#insn-00bdad0c) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdad10`](#insn-00bdad10) → [`00bdd360`](../00bdd/00bdd360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd360` · 推定シンボル `None` · 推定型 `None`
- [`00bdad14`](#insn-00bdad14) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdac20`](#insn-00bdac20)

~~~json
{
  "source": "00bdac20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac24`](#insn-00bdac24)

~~~json
{
  "source": "00bdac24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac38`](#insn-00bdac38)

~~~json
{
  "source": "00bdac38",
  "target": "00bdac58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac40`](#insn-00bdac40)

~~~json
{
  "source": "00bdac40",
  "target": "00bdac98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac48`](#insn-00bdac48)

~~~json
{
  "source": "00bdac48",
  "target": "00bdac70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac50`](#insn-00bdac50)

~~~json
{
  "source": "00bdac50",
  "target": "00bdac84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac54`](#insn-00bdac54)

~~~json
{
  "source": "00bdac54",
  "target": "00bdaca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac5c`](#insn-00bdac5c)

~~~json
{
  "source": "00bdac5c",
  "target": "00bdacd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac64`](#insn-00bdac64)

~~~json
{
  "source": "00bdac64",
  "target": "00bdac84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac6c`](#insn-00bdac6c)

~~~json
{
  "source": "00bdac6c",
  "target": "00bdaca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac74`](#insn-00bdac74)

~~~json
{
  "source": "00bdac74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac78`](#insn-00bdac78)

~~~json
{
  "source": "00bdac78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac88`](#insn-00bdac88)

~~~json
{
  "source": "00bdac88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac8c`](#insn-00bdac8c)

~~~json
{
  "source": "00bdac8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac98`](#insn-00bdac98)

~~~json
{
  "source": "00bdac98",
  "target": "00bdac74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaca0`](#insn-00bdaca0)

~~~json
{
  "source": "00bdaca0",
  "target": "00bdace4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdacac`](#insn-00bdacac)

~~~json
{
  "source": "00bdacac",
  "target": "0029182b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029182b",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6c6962756e77696e643a202573202d2025730a00",
  "capture_start": "0029182b",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdacb0`](#insn-00bdacb0)

~~~json
{
  "source": "00bdacb0",
  "target": "00c1bd48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bd48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdacb8`](#insn-00bdacb8)

~~~json
{
  "source": "00bdacb8",
  "target": "00299a8f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00299a8f",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6765745461626c65456e74727953697a6500",
  "capture_start": "00299a8f",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdacc0`](#insn-00bdacc0)

~~~json
{
  "source": "00bdacc0",
  "target": "002a921f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a921f",
  "offset": 0,
  "size": 41,
  "datatype": "string",
  "bytes": "556e6b6e6f776e20445741524620656e636f64696e6720666f72207365617263",
  "capture_start": "002a921f",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdacc4`](#insn-00bdacc4)

~~~json
{
  "source": "00bdacc4",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdacc8`](#insn-00bdacc8)

~~~json
{
  "source": "00bdacc8",
  "target": "00be1f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaccc`](#insn-00bdaccc)

~~~json
{
  "source": "00bdaccc",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdacd0`](#insn-00bdacd0)

~~~json
{
  "source": "00bdacd0",
  "target": "00bdd360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdacd4`](#insn-00bdacd4)

~~~json
{
  "source": "00bdacd4",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdacd8`](#insn-00bdacd8)

~~~json
{
  "source": "00bdacd8",
  "target": "00bdac74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdace0`](#insn-00bdace0)

~~~json
{
  "source": "00bdace0",
  "target": "00bdaca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdacec`](#insn-00bdacec)

~~~json
{
  "source": "00bdacec",
  "target": "0029182b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029182b",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6c6962756e77696e643a202573202d2025730a00",
  "capture_start": "0029182b",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdacf0`](#insn-00bdacf0)

~~~json
{
  "source": "00bdacf0",
  "target": "00c1bd48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bd48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdacf8`](#insn-00bdacf8)

~~~json
{
  "source": "00bdacf8",
  "target": "00299a8f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00299a8f",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6765745461626c65456e74727953697a6500",
  "capture_start": "00299a8f",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdad00`](#insn-00bdad00)

~~~json
{
  "source": "00bdad00",
  "target": "00295800",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00295800",
  "offset": 0,
  "size": 53,
  "datatype": "string",
  "bytes": "43616e27742062696e61727920736561726368206f6e207661726961626c6520",
  "capture_start": "00295800",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdad04`](#insn-00bdad04)

~~~json
{
  "source": "00bdad04",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdad08`](#insn-00bdad08)

~~~json
{
  "source": "00bdad08",
  "target": "00be1f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdad0c`](#insn-00bdad0c)

~~~json
{
  "source": "00bdad0c",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdad10`](#insn-00bdad10)

~~~json
{
  "source": "00bdad10",
  "target": "00bdd360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdad14`](#insn-00bdad14)

~~~json
{
  "source": "00bdad14",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
