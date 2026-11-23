# 00bdabdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdab1c`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bda/00bdab1c.md) · 移動量 `+0xc0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0080.md#compare-6ad743562ae5ed670db46bfd55bb578f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdac1c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bda/00bdac1c.md) · 移動量 `+0x40`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-8f3ec2a6deacec6eb30d56ce07a970bc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdabdc",
  "name": "FUN_00bdabdc",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a25dac38b0b5bb107537cc0760f2f897fa833d9b7a36a8d62788d032f95494e2",
  "source_text_sha256": "a25dac38b0b5bb107537cc0760f2f897fa833d9b7a36a8d62788d032f95494e2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdabdc",
        "00bdacd7"
      ]
    ],
    "bytes_sha256": "7aa51e4c3813c44038c43e06746a918c3fbe39da2f1ca73cdd38eab45ab7f759",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdaa74](../00bda/00bdaa74.md)

## 呼び出し先

- [00bdd310](../00bdd/00bdd310.md)
- [00bde270](../00bde/00bde270.md)
- [00be1f30](../00be1/00be1f30.md)

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

undefined8 FUN_00bdabdc(uint param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR___sF_00c1bcf8;
  param_1 = param_1 & 0xf;
                    /* try { // try from 00bdabf4 to 00cdac43 has its CatchHandler @ 00bdabf4
                       catch() { ... } // from try @ 00bdabf4 with catch @ 00bdabf4
                       catch() { ... } // from try @ 00bdac98 with catch @ 00bdabf4 */
  if (param_1 < 9) {
    if (param_1 < 3) {
      if (param_1 == 2) {
        return 4;
      }
      if (param_1 == 1) {
LAB_00bdaca4:
                    /* try { // try from 00bdacc8 to 00cdacef has its CatchHandler @ 00bdacc8
                       catch() { ... } // from try @ 00bdacc8 with catch @ 00bdacc8
                       catch() { ... } // from try @ 00bdad28 with catch @ 00bdacc8 */
        fprintf((FILE *)(PTR___sF_00c1bcf8 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
                "Can\'t binary search on variable length encoded data.");
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
                    /* catch() { ... } // from try @ 00bdac44 with catch @ 00bdac98
                       try { // try from 00bdac98 to 00cdacc7 has its CatchHandler @ 00bdabf4 */
    if (param_1 == 10) {
      return 4;
    }
    if (param_1 == 9) goto LAB_00bdaca4;
  }
  else {
    if (param_1 == 0xc) {
                    /* try { // try from 00bdac44 to 00cdac97 has its CatchHandler @ 00bdac98 */
      return 0x10;
    }
    if (param_1 == 0xb) {
      return 8;
    }
  }
  fprintf((FILE *)(PTR___sF_00c1bcf8 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
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
<a id="insn-00bdabdc"></a> `00bdabdc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bdabe0"></a> `00bdabe0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdabe4"></a> `00bdabe4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdabe8"></a> `00bdabe8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bdabec"></a> `00bdabec` | `08 0c 00 12` | and w8,w0,#0xf | `FALL_THROUGH`
<a id="insn-00bdabf0"></a> `00bdabf0` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00bdabf4"></a> `00bdabf4` | `1f 21 00 71` | cmp w8,#0x8 | `FALL_THROUGH`
<a id="insn-00bdabf8"></a> `00bdabf8` | `0c 01 00 54` | b.gt 0x00bdac18 | `CONDITIONAL_JUMP`
<a id="insn-00bdabfc"></a> `00bdabfc` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bdac00"></a> `00bdac00` | `cd 02 00 54` | b.le 0x00bdac58 | `CONDITIONAL_JUMP`
<a id="insn-00bdac04"></a> `00bdac04` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bdac08"></a> `00bdac08` | `40 01 00 54` | b.eq 0x00bdac30 | `CONDITIONAL_JUMP`
<a id="insn-00bdac0c"></a> `00bdac0c` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bdac10"></a> `00bdac10` | `a0 01 00 54` | b.eq 0x00bdac44 | `CONDITIONAL_JUMP`
<a id="insn-00bdac14"></a> `00bdac14` | `14 00 00 14` | b 0x00bdac64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdac18"></a> `00bdac18` | `1f 29 00 71` | cmp w8,#0xa | `FALL_THROUGH`
<a id="insn-00bdac1c"></a> `00bdac1c` | `ed 03 00 54` | b.le 0x00bdac98 | `CONDITIONAL_JUMP`
<a id="insn-00bdac20"></a> `00bdac20` | `1f 31 00 71` | cmp w8,#0xc | `FALL_THROUGH`
<a id="insn-00bdac24"></a> `00bdac24` | `00 01 00 54` | b.eq 0x00bdac44 | `CONDITIONAL_JUMP`
<a id="insn-00bdac28"></a> `00bdac28` | `1f 2d 00 71` | cmp w8,#0xb | `FALL_THROUGH`
<a id="insn-00bdac2c"></a> `00bdac2c` | `c1 01 00 54` | b.ne 0x00bdac64 | `CONDITIONAL_JUMP`
<a id="insn-00bdac30"></a> `00bdac30` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00bdac34"></a> `00bdac34` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdac38"></a> `00bdac38` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdac3c"></a> `00bdac3c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdac40"></a> `00bdac40` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdac44"></a> `00bdac44` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00bdac48"></a> `00bdac48` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdac4c"></a> `00bdac4c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdac50"></a> `00bdac50` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdac54"></a> `00bdac54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdac58"></a> `00bdac58` | `e0 fe ff 54` | b.eq 0x00bdac34 | `CONDITIONAL_JUMP`
<a id="insn-00bdac5c"></a> `00bdac5c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bdac60"></a> `00bdac60` | `20 02 00 54` | b.eq 0x00bdaca4 | `CONDITIONAL_JUMP`
<a id="insn-00bdac64"></a> `00bdac64` | `13 02 00 b0` | adrp x19,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bdac68"></a> `00bdac68` | `a1 b5 ff f0` | adrp x1,0x291000 | `FALL_THROUGH`
<a id="insn-00bdac6c"></a> `00bdac6c` | `21 ac 20 91` | add x1,x1,#0x82b | `FALL_THROUGH`
<a id="insn-00bdac70"></a> `00bdac70` | `73 7e 46 f9` | ldr x19,[x19, #0xcf8] | `FALL_THROUGH`
<a id="insn-00bdac74"></a> `00bdac74` | `e2 b5 ff f0` | adrp x2,0x299000 | `FALL_THROUGH`
<a id="insn-00bdac78"></a> `00bdac78` | `42 70 2c 91` | add x2,x2,#0xb1c | `FALL_THROUGH`
<a id="insn-00bdac7c"></a> `00bdac7c` | `63 b6 ff f0` | adrp x3,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdac80"></a> `00bdac80` | `63 14 06 91` | add x3,x3,#0x185 | `FALL_THROUGH`
<a id="insn-00bdac84"></a> `00bdac84` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdac88"></a> `00bdac88` | `aa 1c 00 94` | bl 0x00be1f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bdac8c"></a> `00bdac8c` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdac90"></a> `00bdac90` | `a0 09 00 94` | bl 0x00bdd310 | `UNCONDITIONAL_CALL`
<a id="insn-00bdac94"></a> `00bdac94` | `77 0d 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bdac98"></a> `00bdac98` | `e0 fc ff 54` | b.eq 0x00bdac34 | `CONDITIONAL_JUMP`
<a id="insn-00bdac9c"></a> `00bdac9c` | `1f 25 00 71` | cmp w8,#0x9 | `FALL_THROUGH`
<a id="insn-00bdaca0"></a> `00bdaca0` | `21 fe ff 54` | b.ne 0x00bdac64 | `CONDITIONAL_JUMP`
<a id="insn-00bdaca4"></a> `00bdaca4` | `13 02 00 b0` | adrp x19,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bdaca8"></a> `00bdaca8` | `a1 b5 ff f0` | adrp x1,0x291000 | `FALL_THROUGH`
<a id="insn-00bdacac"></a> `00bdacac` | `21 ac 20 91` | add x1,x1,#0x82b | `FALL_THROUGH`
<a id="insn-00bdacb0"></a> `00bdacb0` | `73 7e 46 f9` | ldr x19,[x19, #0xcf8] | `FALL_THROUGH`
<a id="insn-00bdacb4"></a> `00bdacb4` | `e2 b5 ff f0` | adrp x2,0x299000 | `FALL_THROUGH`
<a id="insn-00bdacb8"></a> `00bdacb8` | `42 70 2c 91` | add x2,x2,#0xb1c | `FALL_THROUGH`
<a id="insn-00bdacbc"></a> `00bdacbc` | `c3 b5 ff f0` | adrp x3,0x295000 | `FALL_THROUGH`
<a id="insn-00bdacc0"></a> `00bdacc0` | `63 34 22 91` | add x3,x3,#0x88d | `FALL_THROUGH`
<a id="insn-00bdacc4"></a> `00bdacc4` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdacc8"></a> `00bdacc8` | `9a 1c 00 94` | bl 0x00be1f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bdaccc"></a> `00bdaccc` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdacd0"></a> `00bdacd0` | `90 09 00 94` | bl 0x00bdd310 | `UNCONDITIONAL_CALL`
<a id="insn-00bdacd4"></a> `00bdacd4` | `67 0d 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdabdc`](#insn-00bdabdc) 範囲 `[['00bdabdc', '00bdabf3']]`
  - `FALL_THROUGH` [`00bdabf0`](#insn-00bdabf0) → [`00bdabf4`](#insn-00bdabf4)
- ブロック [`00bdabf4`](#insn-00bdabf4) 範囲 `[['00bdabf4', '00bdabfb']]`
  - `CONDITIONAL_JUMP` [`00bdabf8`](#insn-00bdabf8) → [`00bdac18`](#insn-00bdac18)
  - `FALL_THROUGH` [`00bdabf8`](#insn-00bdabf8) → [`00bdabfc`](#insn-00bdabfc)
- ブロック [`00bdabfc`](#insn-00bdabfc) 範囲 `[['00bdabfc', '00bdac03']]`
  - `CONDITIONAL_JUMP` [`00bdac00`](#insn-00bdac00) → [`00bdac58`](#insn-00bdac58)
  - `FALL_THROUGH` [`00bdac00`](#insn-00bdac00) → [`00bdac04`](#insn-00bdac04)
- ブロック [`00bdac04`](#insn-00bdac04) 範囲 `[['00bdac04', '00bdac0b']]`
  - `CONDITIONAL_JUMP` [`00bdac08`](#insn-00bdac08) → [`00bdac30`](#insn-00bdac30)
  - `FALL_THROUGH` [`00bdac08`](#insn-00bdac08) → [`00bdac0c`](#insn-00bdac0c)
- ブロック [`00bdac0c`](#insn-00bdac0c) 範囲 `[['00bdac0c', '00bdac13']]`
  - `CONDITIONAL_JUMP` [`00bdac10`](#insn-00bdac10) → [`00bdac44`](#insn-00bdac44)
  - `FALL_THROUGH` [`00bdac10`](#insn-00bdac10) → [`00bdac14`](#insn-00bdac14)
- ブロック [`00bdac14`](#insn-00bdac14) 範囲 `[['00bdac14', '00bdac17']]`
  - `UNCONDITIONAL_JUMP` [`00bdac14`](#insn-00bdac14) → [`00bdac64`](#insn-00bdac64)
- ブロック [`00bdac18`](#insn-00bdac18) 範囲 `[['00bdac18', '00bdac1f']]`
  - `CONDITIONAL_JUMP` [`00bdac1c`](#insn-00bdac1c) → [`00bdac98`](#insn-00bdac98)
  - `FALL_THROUGH` [`00bdac1c`](#insn-00bdac1c) → [`00bdac20`](#insn-00bdac20)
- ブロック [`00bdac20`](#insn-00bdac20) 範囲 `[['00bdac20', '00bdac27']]`
  - `CONDITIONAL_JUMP` [`00bdac24`](#insn-00bdac24) → [`00bdac44`](#insn-00bdac44)
  - `FALL_THROUGH` [`00bdac24`](#insn-00bdac24) → [`00bdac28`](#insn-00bdac28)
- ブロック [`00bdac28`](#insn-00bdac28) 範囲 `[['00bdac28', '00bdac2f']]`
  - `CONDITIONAL_JUMP` [`00bdac2c`](#insn-00bdac2c) → [`00bdac64`](#insn-00bdac64)
  - `FALL_THROUGH` [`00bdac2c`](#insn-00bdac2c) → [`00bdac30`](#insn-00bdac30)
- ブロック [`00bdac30`](#insn-00bdac30) 範囲 `[['00bdac30', '00bdac33']]`
  - `FALL_THROUGH` [`00bdac30`](#insn-00bdac30) → [`00bdac34`](#insn-00bdac34)
- ブロック [`00bdac34`](#insn-00bdac34) 範囲 `[['00bdac34', '00bdac43']]`
- ブロック [`00bdac44`](#insn-00bdac44) 範囲 `[['00bdac44', '00bdac57']]`
- ブロック [`00bdac58`](#insn-00bdac58) 範囲 `[['00bdac58', '00bdac5b']]`
  - `CONDITIONAL_JUMP` [`00bdac58`](#insn-00bdac58) → [`00bdac34`](#insn-00bdac34)
  - `FALL_THROUGH` [`00bdac58`](#insn-00bdac58) → [`00bdac5c`](#insn-00bdac5c)
- ブロック [`00bdac5c`](#insn-00bdac5c) 範囲 `[['00bdac5c', '00bdac63']]`
  - `CONDITIONAL_JUMP` [`00bdac60`](#insn-00bdac60) → [`00bdaca4`](#insn-00bdaca4)
  - `FALL_THROUGH` [`00bdac60`](#insn-00bdac60) → [`00bdac64`](#insn-00bdac64)
- ブロック [`00bdac64`](#insn-00bdac64) 範囲 `[['00bdac64', '00bdac97']]`
- ブロック [`00bdac98`](#insn-00bdac98) 範囲 `[['00bdac98', '00bdac9b']]`
  - `CONDITIONAL_JUMP` [`00bdac98`](#insn-00bdac98) → [`00bdac34`](#insn-00bdac34)
  - `FALL_THROUGH` [`00bdac98`](#insn-00bdac98) → [`00bdac9c`](#insn-00bdac9c)
- ブロック [`00bdac9c`](#insn-00bdac9c) 範囲 `[['00bdac9c', '00bdaca3']]`
  - `CONDITIONAL_JUMP` [`00bdaca0`](#insn-00bdaca0) → [`00bdac64`](#insn-00bdac64)
  - `FALL_THROUGH` [`00bdaca0`](#insn-00bdaca0) → [`00bdaca4`](#insn-00bdaca4)
- ブロック [`00bdaca4`](#insn-00bdaca4) 範囲 `[['00bdaca4', '00bdacc7']]`
  - `FALL_THROUGH` [`00bdacc4`](#insn-00bdacc4) → [`00bdacc8`](#insn-00bdacc8)
- ブロック [`00bdacc8`](#insn-00bdacc8) 範囲 `[['00bdacc8', '00bdacd7']]`

## 命令位置別の参照

- [`00bdabe0`](#insn-00bdabe0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabe4`](#insn-00bdabe4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabf8`](#insn-00bdabf8) → [`00bdac18`](#insn-00bdac18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac00`](#insn-00bdac00) → [`00bdac58`](#insn-00bdac58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac08`](#insn-00bdac08) → [`00bdac30`](#insn-00bdac30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac10`](#insn-00bdac10) → [`00bdac44`](#insn-00bdac44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac14`](#insn-00bdac14) → [`00bdac64`](#insn-00bdac64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac1c`](#insn-00bdac1c) → [`00bdac98`](#insn-00bdac98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac24`](#insn-00bdac24) → [`00bdac44`](#insn-00bdac44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac2c`](#insn-00bdac2c) → [`00bdac64`](#insn-00bdac64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac34`](#insn-00bdac34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac38`](#insn-00bdac38) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac48`](#insn-00bdac48) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac4c`](#insn-00bdac4c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac58`](#insn-00bdac58) → [`00bdac34`](#insn-00bdac34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac60`](#insn-00bdac60) → [`00bdaca4`](#insn-00bdaca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac6c`](#insn-00bdac6c) → `0029182b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdac70`](#insn-00bdac70) → `00c1bcf8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdac78`](#insn-00bdac78) → `00299b1c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdac80`](#insn-00bdac80) → `002a9185`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdac84`](#insn-00bdac84) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdac88`](#insn-00bdac88) → [`00be1f30`](../00be1/00be1f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1f30` · 推定シンボル `None` · 推定型 `None`
- [`00bdac8c`](#insn-00bdac8c) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdac90`](#insn-00bdac90) → [`00bdd310`](../00bdd/00bdd310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd310` · 推定シンボル `None` · 推定型 `None`
- [`00bdac94`](#insn-00bdac94) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bdac98`](#insn-00bdac98) → [`00bdac34`](#insn-00bdac34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaca0`](#insn-00bdaca0) → [`00bdac64`](#insn-00bdac64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdacac`](#insn-00bdacac) → `0029182b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdacb0`](#insn-00bdacb0) → `00c1bcf8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdacb8`](#insn-00bdacb8) → `00299b1c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdacc0`](#insn-00bdacc0) → `0029588d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdacc4`](#insn-00bdacc4) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdacc8`](#insn-00bdacc8) → [`00be1f30`](../00be1/00be1f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1f30` · 推定シンボル `None` · 推定型 `None`
- [`00bdaccc`](#insn-00bdaccc) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdacd0`](#insn-00bdacd0) → [`00bdd310`](../00bdd/00bdd310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd310` · 推定シンボル `None` · 推定型 `None`
- [`00bdacd4`](#insn-00bdacd4) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdabe0`](#insn-00bdabe0)

~~~json
{
  "source": "00bdabe0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabe4`](#insn-00bdabe4)

~~~json
{
  "source": "00bdabe4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabf8`](#insn-00bdabf8)

~~~json
{
  "source": "00bdabf8",
  "target": "00bdac18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac00`](#insn-00bdac00)

~~~json
{
  "source": "00bdac00",
  "target": "00bdac58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac08`](#insn-00bdac08)

~~~json
{
  "source": "00bdac08",
  "target": "00bdac30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac10`](#insn-00bdac10)

~~~json
{
  "source": "00bdac10",
  "target": "00bdac44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac14`](#insn-00bdac14)

~~~json
{
  "source": "00bdac14",
  "target": "00bdac64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac1c`](#insn-00bdac1c)

~~~json
{
  "source": "00bdac1c",
  "target": "00bdac98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac24`](#insn-00bdac24)

~~~json
{
  "source": "00bdac24",
  "target": "00bdac44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac2c`](#insn-00bdac2c)

~~~json
{
  "source": "00bdac2c",
  "target": "00bdac64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac34`](#insn-00bdac34)

~~~json
{
  "source": "00bdac34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac38`](#insn-00bdac38)

~~~json
{
  "source": "00bdac38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac48`](#insn-00bdac48)

~~~json
{
  "source": "00bdac48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac4c`](#insn-00bdac4c)

~~~json
{
  "source": "00bdac4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac58`](#insn-00bdac58)

~~~json
{
  "source": "00bdac58",
  "target": "00bdac34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac60`](#insn-00bdac60)

~~~json
{
  "source": "00bdac60",
  "target": "00bdaca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac6c`](#insn-00bdac6c)

~~~json
{
  "source": "00bdac6c",
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
- 参照命令 [`00bdac70`](#insn-00bdac70)

~~~json
{
  "source": "00bdac70",
  "target": "00c1bcf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bcf8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdac78`](#insn-00bdac78)

~~~json
{
  "source": "00bdac78",
  "target": "00299b1c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00299b1c",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6765745461626c65456e74727953697a6500",
  "capture_start": "00299b1c",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdac80`](#insn-00bdac80)

~~~json
{
  "source": "00bdac80",
  "target": "002a9185",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9185",
  "offset": 0,
  "size": 41,
  "datatype": "string",
  "bytes": "556e6b6e6f776e20445741524620656e636f64696e6720666f72207365617263",
  "capture_start": "002a9185",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdac84`](#insn-00bdac84)

~~~json
{
  "source": "00bdac84",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac88`](#insn-00bdac88)

~~~json
{
  "source": "00bdac88",
  "target": "00be1f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac8c`](#insn-00bdac8c)

~~~json
{
  "source": "00bdac8c",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac90`](#insn-00bdac90)

~~~json
{
  "source": "00bdac90",
  "target": "00bdd310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac94`](#insn-00bdac94)

~~~json
{
  "source": "00bdac94",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac98`](#insn-00bdac98)

~~~json
{
  "source": "00bdac98",
  "target": "00bdac34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaca0`](#insn-00bdaca0)

~~~json
{
  "source": "00bdaca0",
  "target": "00bdac64",
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
  "target": "00c1bcf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bcf8",
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
  "target": "00299b1c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00299b1c",
  "offset": 0,
  "size": 18,
  "datatype": "string",
  "bytes": "6765745461626c65456e74727953697a6500",
  "capture_start": "00299b1c",
  "capture_bytes": 18,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdacc0`](#insn-00bdacc0)

~~~json
{
  "source": "00bdacc0",
  "target": "0029588d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029588d",
  "offset": 0,
  "size": 53,
  "datatype": "string",
  "bytes": "43616e27742062696e61727920736561726368206f6e207661726961626c6520",
  "capture_start": "0029588d",
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
  "target": "00be1f30",
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
  "target": "00bdd310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdacd4`](#insn-00bdacd4)

~~~json
{
  "source": "00bdacd4",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
