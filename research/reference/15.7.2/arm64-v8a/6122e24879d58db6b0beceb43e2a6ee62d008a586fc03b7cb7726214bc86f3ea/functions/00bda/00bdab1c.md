# 00bdab1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdabdc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdabdc.md) · 移動量 `+0xc0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0080.md#compare-6ad743562ae5ed670db46bfd55bb578f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdab1c",
  "name": "FUN_00bdab1c",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ca19d7b6d13f571d098d5b637efe7f07a2b28d4d30c859fa5047397ab99afe31",
  "source_text_sha256": "ca19d7b6d13f571d098d5b637efe7f07a2b28d4d30c859fa5047397ab99afe31",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdab1c",
        "00bdac17"
      ]
    ],
    "bytes_sha256": "7b107efa90fbf8f3c5ecce92669f882fb0179095b028309a3ca39b6369f23e68",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bda9b4](../00bda/00bda9b4.md)

## 呼び出し先

- [00bdd260](../00bdd/00bdd260.md)
- [00bde1c0](../00bde/00bde1c0.md)
- [00be1e80](../00be1/00be1e80.md)

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

undefined8 FUN_00bdab1c(uint param_1)

{
  undefined *puVar1;
  
  puVar1 = PTR___sF_00c1bc48;
                    /* try { // try from 00bdab2c to 00cdab7b has its CatchHandler @ 00bdab2c
                       catch() { ... } // from try @ 00bdab2c with catch @ 00bdab2c
                       catch() { ... } // from try @ 00bdabd0 with catch @ 00bdab2c */
  param_1 = param_1 & 0xf;
  if (param_1 < 9) {
    if (param_1 < 3) {
      if (param_1 == 2) {
        return 4;
      }
      if (param_1 == 1) {
LAB_00bdabe4:
                    /* try { // try from 00bdac00 to 00cdac27 has its CatchHandler @ 00bdac00
                       catch() { ... } // from try @ 00bdac00 with catch @ 00bdac00
                       catch() { ... } // from try @ 00bdac60 with catch @ 00bdac00 */
        fprintf((FILE *)(PTR___sF_00c1bc48 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
                "Can\'t binary search on variable length encoded data.");
        fflush((FILE *)(puVar1 + 0x130));
                    /* WARNING: Subroutine does not return */
        abort();
      }
    }
    else {
      if (param_1 == 3) {
                    /* try { // try from 00bdab7c to 00cdabcf has its CatchHandler @ 00bdabd0 */
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
    if (param_1 == 9) goto LAB_00bdabe4;
  }
  else {
    if (param_1 == 0xc) {
      return 0x10;
    }
    if (param_1 == 0xb) {
      return 8;
    }
  }
  fprintf((FILE *)(PTR___sF_00c1bc48 + 0x130),"libunwind: %s - %s\n","getTableEntrySize",
          "Unknown DWARF encoding for search table.");
                    /* catch() { ... } // from try @ 00bdab7c with catch @ 00bdabd0
                       try { // try from 00bdabd0 to 00cdabff has its CatchHandler @ 00bdab2c */
  fflush((FILE *)(puVar1 + 0x130));
                    /* WARNING: Subroutine does not return */
  abort();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdab1c"></a> `00bdab1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bdab20"></a> `00bdab20` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdab24"></a> `00bdab24` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdab28"></a> `00bdab28` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bdab2c"></a> `00bdab2c` | `08 0c 00 12` | and w8,w0,#0xf | `FALL_THROUGH`
<a id="insn-00bdab30"></a> `00bdab30` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00bdab34"></a> `00bdab34` | `1f 21 00 71` | cmp w8,#0x8 | `FALL_THROUGH`
<a id="insn-00bdab38"></a> `00bdab38` | `0c 01 00 54` | b.gt 0x00bdab58 | `CONDITIONAL_JUMP`
<a id="insn-00bdab3c"></a> `00bdab3c` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bdab40"></a> `00bdab40` | `cd 02 00 54` | b.le 0x00bdab98 | `CONDITIONAL_JUMP`
<a id="insn-00bdab44"></a> `00bdab44` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bdab48"></a> `00bdab48` | `40 01 00 54` | b.eq 0x00bdab70 | `CONDITIONAL_JUMP`
<a id="insn-00bdab4c"></a> `00bdab4c` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bdab50"></a> `00bdab50` | `a0 01 00 54` | b.eq 0x00bdab84 | `CONDITIONAL_JUMP`
<a id="insn-00bdab54"></a> `00bdab54` | `14 00 00 14` | b 0x00bdaba4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdab58"></a> `00bdab58` | `1f 29 00 71` | cmp w8,#0xa | `FALL_THROUGH`
<a id="insn-00bdab5c"></a> `00bdab5c` | `ed 03 00 54` | b.le 0x00bdabd8 | `CONDITIONAL_JUMP`
<a id="insn-00bdab60"></a> `00bdab60` | `1f 31 00 71` | cmp w8,#0xc | `FALL_THROUGH`
<a id="insn-00bdab64"></a> `00bdab64` | `00 01 00 54` | b.eq 0x00bdab84 | `CONDITIONAL_JUMP`
<a id="insn-00bdab68"></a> `00bdab68` | `1f 2d 00 71` | cmp w8,#0xb | `FALL_THROUGH`
<a id="insn-00bdab6c"></a> `00bdab6c` | `c1 01 00 54` | b.ne 0x00bdaba4 | `CONDITIONAL_JUMP`
<a id="insn-00bdab70"></a> `00bdab70` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00bdab74"></a> `00bdab74` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdab78"></a> `00bdab78` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdab7c"></a> `00bdab7c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdab80"></a> `00bdab80` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdab84"></a> `00bdab84` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00bdab88"></a> `00bdab88` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdab8c"></a> `00bdab8c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdab90"></a> `00bdab90` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bdab94"></a> `00bdab94` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdab98"></a> `00bdab98` | `e0 fe ff 54` | b.eq 0x00bdab74 | `CONDITIONAL_JUMP`
<a id="insn-00bdab9c"></a> `00bdab9c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bdaba0"></a> `00bdaba0` | `20 02 00 54` | b.eq 0x00bdabe4 | `CONDITIONAL_JUMP`
<a id="insn-00bdaba4"></a> `00bdaba4` | `13 02 00 b0` | adrp x19,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bdaba8"></a> `00bdaba8` | `a1 b5 ff f0` | adrp x1,0x291000 | `FALL_THROUGH`
<a id="insn-00bdabac"></a> `00bdabac` | `21 ac 20 91` | add x1,x1,#0x82b | `FALL_THROUGH`
<a id="insn-00bdabb0"></a> `00bdabb0` | `73 26 46 f9` | ldr x19,[x19, #0xc48] | `FALL_THROUGH`
<a id="insn-00bdabb4"></a> `00bdabb4` | `e2 b5 ff f0` | adrp x2,0x299000 | `FALL_THROUGH`
<a id="insn-00bdabb8"></a> `00bdabb8` | `42 3c 2a 91` | add x2,x2,#0xa8f | `FALL_THROUGH`
<a id="insn-00bdabbc"></a> `00bdabbc` | `63 b6 ff f0` | adrp x3,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bdabc0"></a> `00bdabc0` | `63 64 08 91` | add x3,x3,#0x219 | `FALL_THROUGH`
<a id="insn-00bdabc4"></a> `00bdabc4` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdabc8"></a> `00bdabc8` | `ae 1c 00 94` | bl 0x00be1e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdabcc"></a> `00bdabcc` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdabd0"></a> `00bdabd0` | `a4 09 00 94` | bl 0x00bdd260 | `UNCONDITIONAL_CALL`
<a id="insn-00bdabd4"></a> `00bdabd4` | `7b 0d 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bdabd8"></a> `00bdabd8` | `e0 fc ff 54` | b.eq 0x00bdab74 | `CONDITIONAL_JUMP`
<a id="insn-00bdabdc"></a> `00bdabdc` | `1f 25 00 71` | cmp w8,#0x9 | `FALL_THROUGH`
<a id="insn-00bdabe0"></a> `00bdabe0` | `21 fe ff 54` | b.ne 0x00bdaba4 | `CONDITIONAL_JUMP`
<a id="insn-00bdabe4"></a> `00bdabe4` | `13 02 00 b0` | adrp x19,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bdabe8"></a> `00bdabe8` | `a1 b5 ff f0` | adrp x1,0x291000 | `FALL_THROUGH`
<a id="insn-00bdabec"></a> `00bdabec` | `21 ac 20 91` | add x1,x1,#0x82b | `FALL_THROUGH`
<a id="insn-00bdabf0"></a> `00bdabf0` | `73 26 46 f9` | ldr x19,[x19, #0xc48] | `FALL_THROUGH`
<a id="insn-00bdabf4"></a> `00bdabf4` | `e2 b5 ff f0` | adrp x2,0x299000 | `FALL_THROUGH`
<a id="insn-00bdabf8"></a> `00bdabf8` | `42 3c 2a 91` | add x2,x2,#0xa8f | `FALL_THROUGH`
<a id="insn-00bdabfc"></a> `00bdabfc` | `c3 b5 ff f0` | adrp x3,0x295000 | `FALL_THROUGH`
<a id="insn-00bdac00"></a> `00bdac00` | `63 00 20 91` | add x3,x3,#0x800 | `FALL_THROUGH`
<a id="insn-00bdac04"></a> `00bdac04` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdac08"></a> `00bdac08` | `9e 1c 00 94` | bl 0x00be1e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bdac0c"></a> `00bdac0c` | `60 c2 04 91` | add x0,x19,#0x130 | `FALL_THROUGH`
<a id="insn-00bdac10"></a> `00bdac10` | `94 09 00 94` | bl 0x00bdd260 | `UNCONDITIONAL_CALL`
<a id="insn-00bdac14"></a> `00bdac14` | `6b 0d 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdab1c`](#insn-00bdab1c) 範囲 `[['00bdab1c', '00bdab2b']]`
  - `FALL_THROUGH` [`00bdab28`](#insn-00bdab28) → [`00bdab2c`](#insn-00bdab2c)
- ブロック [`00bdab2c`](#insn-00bdab2c) 範囲 `[['00bdab2c', '00bdab3b']]`
  - `CONDITIONAL_JUMP` [`00bdab38`](#insn-00bdab38) → [`00bdab58`](#insn-00bdab58)
  - `FALL_THROUGH` [`00bdab38`](#insn-00bdab38) → [`00bdab3c`](#insn-00bdab3c)
- ブロック [`00bdab3c`](#insn-00bdab3c) 範囲 `[['00bdab3c', '00bdab43']]`
  - `CONDITIONAL_JUMP` [`00bdab40`](#insn-00bdab40) → [`00bdab98`](#insn-00bdab98)
  - `FALL_THROUGH` [`00bdab40`](#insn-00bdab40) → [`00bdab44`](#insn-00bdab44)
- ブロック [`00bdab44`](#insn-00bdab44) 範囲 `[['00bdab44', '00bdab4b']]`
  - `CONDITIONAL_JUMP` [`00bdab48`](#insn-00bdab48) → [`00bdab70`](#insn-00bdab70)
  - `FALL_THROUGH` [`00bdab48`](#insn-00bdab48) → [`00bdab4c`](#insn-00bdab4c)
- ブロック [`00bdab4c`](#insn-00bdab4c) 範囲 `[['00bdab4c', '00bdab53']]`
  - `CONDITIONAL_JUMP` [`00bdab50`](#insn-00bdab50) → [`00bdab84`](#insn-00bdab84)
  - `FALL_THROUGH` [`00bdab50`](#insn-00bdab50) → [`00bdab54`](#insn-00bdab54)
- ブロック [`00bdab54`](#insn-00bdab54) 範囲 `[['00bdab54', '00bdab57']]`
  - `UNCONDITIONAL_JUMP` [`00bdab54`](#insn-00bdab54) → [`00bdaba4`](#insn-00bdaba4)
- ブロック [`00bdab58`](#insn-00bdab58) 範囲 `[['00bdab58', '00bdab5f']]`
  - `CONDITIONAL_JUMP` [`00bdab5c`](#insn-00bdab5c) → [`00bdabd8`](#insn-00bdabd8)
  - `FALL_THROUGH` [`00bdab5c`](#insn-00bdab5c) → [`00bdab60`](#insn-00bdab60)
- ブロック [`00bdab60`](#insn-00bdab60) 範囲 `[['00bdab60', '00bdab67']]`
  - `CONDITIONAL_JUMP` [`00bdab64`](#insn-00bdab64) → [`00bdab84`](#insn-00bdab84)
  - `FALL_THROUGH` [`00bdab64`](#insn-00bdab64) → [`00bdab68`](#insn-00bdab68)
- ブロック [`00bdab68`](#insn-00bdab68) 範囲 `[['00bdab68', '00bdab6f']]`
  - `CONDITIONAL_JUMP` [`00bdab6c`](#insn-00bdab6c) → [`00bdaba4`](#insn-00bdaba4)
  - `FALL_THROUGH` [`00bdab6c`](#insn-00bdab6c) → [`00bdab70`](#insn-00bdab70)
- ブロック [`00bdab70`](#insn-00bdab70) 範囲 `[['00bdab70', '00bdab73']]`
  - `FALL_THROUGH` [`00bdab70`](#insn-00bdab70) → [`00bdab74`](#insn-00bdab74)
- ブロック [`00bdab74`](#insn-00bdab74) 範囲 `[['00bdab74', '00bdab7b']]`
  - `FALL_THROUGH` [`00bdab78`](#insn-00bdab78) → [`00bdab7c`](#insn-00bdab7c)
- ブロック [`00bdab7c`](#insn-00bdab7c) 範囲 `[['00bdab7c', '00bdab83']]`
- ブロック [`00bdab84`](#insn-00bdab84) 範囲 `[['00bdab84', '00bdab97']]`
- ブロック [`00bdab98`](#insn-00bdab98) 範囲 `[['00bdab98', '00bdab9b']]`
  - `CONDITIONAL_JUMP` [`00bdab98`](#insn-00bdab98) → [`00bdab74`](#insn-00bdab74)
  - `FALL_THROUGH` [`00bdab98`](#insn-00bdab98) → [`00bdab9c`](#insn-00bdab9c)
- ブロック [`00bdab9c`](#insn-00bdab9c) 範囲 `[['00bdab9c', '00bdaba3']]`
  - `CONDITIONAL_JUMP` [`00bdaba0`](#insn-00bdaba0) → [`00bdabe4`](#insn-00bdabe4)
  - `FALL_THROUGH` [`00bdaba0`](#insn-00bdaba0) → [`00bdaba4`](#insn-00bdaba4)
- ブロック [`00bdaba4`](#insn-00bdaba4) 範囲 `[['00bdaba4', '00bdabcf']]`
  - `FALL_THROUGH` [`00bdabcc`](#insn-00bdabcc) → [`00bdabd0`](#insn-00bdabd0)
- ブロック [`00bdabd0`](#insn-00bdabd0) 範囲 `[['00bdabd0', '00bdabd7']]`
- ブロック [`00bdabd8`](#insn-00bdabd8) 範囲 `[['00bdabd8', '00bdabdb']]`
  - `CONDITIONAL_JUMP` [`00bdabd8`](#insn-00bdabd8) → [`00bdab74`](#insn-00bdab74)
  - `FALL_THROUGH` [`00bdabd8`](#insn-00bdabd8) → [`00bdabdc`](#insn-00bdabdc)
- ブロック [`00bdabdc`](#insn-00bdabdc) 範囲 `[['00bdabdc', '00bdabe3']]`
  - `CONDITIONAL_JUMP` [`00bdabe0`](#insn-00bdabe0) → [`00bdaba4`](#insn-00bdaba4)
  - `FALL_THROUGH` [`00bdabe0`](#insn-00bdabe0) → [`00bdabe4`](#insn-00bdabe4)
- ブロック [`00bdabe4`](#insn-00bdabe4) 範囲 `[['00bdabe4', '00bdabff']]`
  - `FALL_THROUGH` [`00bdabfc`](#insn-00bdabfc) → [`00bdac00`](#insn-00bdac00)
- ブロック [`00bdac00`](#insn-00bdac00) 範囲 `[['00bdac00', '00bdac17']]`

## 命令位置別の参照

- [`00bdab20`](#insn-00bdab20) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab24`](#insn-00bdab24) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab38`](#insn-00bdab38) → [`00bdab58`](#insn-00bdab58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab40`](#insn-00bdab40) → [`00bdab98`](#insn-00bdab98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab48`](#insn-00bdab48) → [`00bdab70`](#insn-00bdab70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab50`](#insn-00bdab50) → [`00bdab84`](#insn-00bdab84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab54`](#insn-00bdab54) → [`00bdaba4`](#insn-00bdaba4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab5c`](#insn-00bdab5c) → [`00bdabd8`](#insn-00bdabd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab64`](#insn-00bdab64) → [`00bdab84`](#insn-00bdab84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab6c`](#insn-00bdab6c) → [`00bdaba4`](#insn-00bdaba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab74`](#insn-00bdab74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab78`](#insn-00bdab78) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab88`](#insn-00bdab88) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab8c`](#insn-00bdab8c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdab98`](#insn-00bdab98) → [`00bdab74`](#insn-00bdab74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdaba0`](#insn-00bdaba0) → [`00bdabe4`](#insn-00bdabe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabac`](#insn-00bdabac) → `0029182b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdabb0`](#insn-00bdabb0) → `00c1bc48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdabb8`](#insn-00bdabb8) → `00299a8f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdabc0`](#insn-00bdabc0) → `002a9219`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdabc4`](#insn-00bdabc4) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdabc8`](#insn-00bdabc8) → [`00be1e80`](../00be1/00be1e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1e80` · 推定シンボル `None` · 推定型 `None`
- [`00bdabcc`](#insn-00bdabcc) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdabd0`](#insn-00bdabd0) → [`00bdd260`](../00bdd/00bdd260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd260` · 推定シンボル `None` · 推定型 `None`
- [`00bdabd4`](#insn-00bdabd4) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bdabd8`](#insn-00bdabd8) → [`00bdab74`](#insn-00bdab74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabe0`](#insn-00bdabe0) → [`00bdaba4`](#insn-00bdaba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabec`](#insn-00bdabec) → `0029182b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdabf0`](#insn-00bdabf0) → `00c1bc48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdabf8`](#insn-00bdabf8) → `00299a8f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdac00`](#insn-00bdac00) → `00295800`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdac04`](#insn-00bdac04) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdac08`](#insn-00bdac08) → [`00be1e80`](../00be1/00be1e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1e80` · 推定シンボル `None` · 推定型 `None`
- [`00bdac0c`](#insn-00bdac0c) → [`010a58b8`](../010a5/010a58b8.md) · `PARAM` · `ANALYSIS` · 関数 `010a58b8` · 推定シンボル `None` · 推定型 `None`
- [`00bdac10`](#insn-00bdac10) → [`00bdd260`](../00bdd/00bdd260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd260` · 推定シンボル `None` · 推定型 `None`
- [`00bdac14`](#insn-00bdac14) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdab20`](#insn-00bdab20)

~~~json
{
  "source": "00bdab20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab24`](#insn-00bdab24)

~~~json
{
  "source": "00bdab24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab38`](#insn-00bdab38)

~~~json
{
  "source": "00bdab38",
  "target": "00bdab58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab40`](#insn-00bdab40)

~~~json
{
  "source": "00bdab40",
  "target": "00bdab98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab48`](#insn-00bdab48)

~~~json
{
  "source": "00bdab48",
  "target": "00bdab70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab50`](#insn-00bdab50)

~~~json
{
  "source": "00bdab50",
  "target": "00bdab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab54`](#insn-00bdab54)

~~~json
{
  "source": "00bdab54",
  "target": "00bdaba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab5c`](#insn-00bdab5c)

~~~json
{
  "source": "00bdab5c",
  "target": "00bdabd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab64`](#insn-00bdab64)

~~~json
{
  "source": "00bdab64",
  "target": "00bdab84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab6c`](#insn-00bdab6c)

~~~json
{
  "source": "00bdab6c",
  "target": "00bdaba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab74`](#insn-00bdab74)

~~~json
{
  "source": "00bdab74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab78`](#insn-00bdab78)

~~~json
{
  "source": "00bdab78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab88`](#insn-00bdab88)

~~~json
{
  "source": "00bdab88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab8c`](#insn-00bdab8c)

~~~json
{
  "source": "00bdab8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdab98`](#insn-00bdab98)

~~~json
{
  "source": "00bdab98",
  "target": "00bdab74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdaba0`](#insn-00bdaba0)

~~~json
{
  "source": "00bdaba0",
  "target": "00bdabe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabac`](#insn-00bdabac)

~~~json
{
  "source": "00bdabac",
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
- 参照命令 [`00bdabb0`](#insn-00bdabb0)

~~~json
{
  "source": "00bdabb0",
  "target": "00c1bc48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bc48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdabb8`](#insn-00bdabb8)

~~~json
{
  "source": "00bdabb8",
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
- 参照命令 [`00bdabc0`](#insn-00bdabc0)

~~~json
{
  "source": "00bdabc0",
  "target": "002a9219",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9219",
  "offset": 0,
  "size": 41,
  "datatype": "string",
  "bytes": "556e6b6e6f776e20445741524620656e636f64696e6720666f72207365617263",
  "capture_start": "002a9219",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdabc4`](#insn-00bdabc4)

~~~json
{
  "source": "00bdabc4",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdabc8`](#insn-00bdabc8)

~~~json
{
  "source": "00bdabc8",
  "target": "00be1e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdabcc`](#insn-00bdabcc)

~~~json
{
  "source": "00bdabcc",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdabd0`](#insn-00bdabd0)

~~~json
{
  "source": "00bdabd0",
  "target": "00bdd260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdabd4`](#insn-00bdabd4)

~~~json
{
  "source": "00bdabd4",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdabd8`](#insn-00bdabd8)

~~~json
{
  "source": "00bdabd8",
  "target": "00bdab74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabe0`](#insn-00bdabe0)

~~~json
{
  "source": "00bdabe0",
  "target": "00bdaba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabec`](#insn-00bdabec)

~~~json
{
  "source": "00bdabec",
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
- 参照命令 [`00bdabf0`](#insn-00bdabf0)

~~~json
{
  "source": "00bdabf0",
  "target": "00c1bc48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bc48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdabf8`](#insn-00bdabf8)

~~~json
{
  "source": "00bdabf8",
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
- 参照命令 [`00bdac00`](#insn-00bdac00)

~~~json
{
  "source": "00bdac00",
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
- 参照命令 [`00bdac04`](#insn-00bdac04)

~~~json
{
  "source": "00bdac04",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac08`](#insn-00bdac08)

~~~json
{
  "source": "00bdac08",
  "target": "00be1e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac0c`](#insn-00bdac0c)

~~~json
{
  "source": "00bdac0c",
  "target": "010a58b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac10`](#insn-00bdac10)

~~~json
{
  "source": "00bdac10",
  "target": "00bdd260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac14`](#insn-00bdac14)

~~~json
{
  "source": "00bdac14",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
