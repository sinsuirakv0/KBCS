# 00bbbfa0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbbf5c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbbf5c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-91c8a77b823f33b29b3df49f95249431)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c389e8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c38/00c389e8.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-d66f6137d5b3f1fec982eef529f564be)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbfa0",
  "name": "FUN_00bbbfa0",
  "size": 364,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bd9a0a1165ef10735d581cb3ed1cecff9bb2889c2e4600235bbf92f4ebb07887",
  "source_text_sha256": "bd9a0a1165ef10735d581cb3ed1cecff9bb2889c2e4600235bbf92f4ebb07887",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbfa0",
        "00bbc10b"
      ]
    ],
    "bytes_sha256": "3fda645181f2a12e87299e6ac124b066dd8a8b5989b0cae31959fbdb5226d1f3",
    "instruction_count": 91,
    "instruction_bytes": 364,
    "body_bytes": 364,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb7c0](../00bdb/00bdb7c0.md)
- [00bde9d0](../00bde/00bde9d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2451 bytes

~~~c

bool FUN_00bbbfa0(long param_1,long param_2,undefined8 *param_3)

{
  uint uVar1;
  int iVar2;
  long lVar3;
  undefined *puVar4;
  char *__s2;
  
                    /* try { // try from 00bbbfa8 to 00cbbfb3 has its CatchHandler @ 00bbd1e8 */
                    /* try { // try from 00bbbfb4 to 00cbbfc3 has its CatchHandler @ 00bbd1d4 */
  __s2 = *(char **)(param_2 + 8);
                    /* try { // try from 00bbbfc4 to 00cbbfd7 has its CatchHandler @ 00bbd1bc */
  if (__s2 == PTR__ZTSDn_00c1c060) {
    if ((*(long *)(param_1 + 0x18) == 0) ||
       (lVar3 = __dynamic_cast(*(long *)(param_1 + 0x18),
                               PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048,
                               PTR__ZTIN10__cxxabiv120__function_type_infoE_00c1c078,0), lVar3 == 0)
       ) {
                    /* try { // try from 00bbc0d0 to 00cbc0df has its CatchHandler @ 00bbd42c */
      puVar4 = &DAT_002fc9b8;
    }
    else {
      puVar4 = &DAT_002fc9a8;
    }
    *param_3 = puVar4;
    return true;
  }
  uVar1 = *(uint *)(param_1 + 0x10);
  if ((uVar1 & 0x18) == 0) {
    lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048,
                           PTR__ZTIN10__cxxabiv117__pbase_type_infoE_00c1c058,0);
    if (lVar3 == 0) goto LAB_00bbc070;
    if ((*(byte *)(lVar3 + 0x10) & 0x18) == 0) {
      if (*(char **)(param_1 + 8) == __s2) {
        return true;
      }
      goto LAB_00bbc070;
    }
  }
  if ((param_1 == param_2) || (iVar2 = strcmp(*(char **)(param_1 + 8),__s2), iVar2 == 0)) {
    return true;
  }
LAB_00bbc070:
  lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1c048,
                         PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c080,0);
  if (lVar3 == 0) {
    return false;
  }
                    /* try { // try from 00bbc094 to 00cbc09f has its CatchHandler @ 00bbd3b8 */
  if ((((*(uint *)(lVar3 + 0x10) & (uVar1 ^ 0xffffffff) & 7) == 0) &&
      ((uVar1 & (*(uint *)(lVar3 + 0x10) ^ 0xffffffff) & 0x60) == 0)) &&
     (*(long *)(*(long *)(param_1 + 0x18) + 8) == *(long *)(*(long *)(lVar3 + 0x18) + 8))) {
                    /* try { // try from 00bbc0f4 to 00cbc0fb has its CatchHandler @ 00bbd32c */
                    /* try { // try from 00bbc0fc to 00cbc103 has its CatchHandler @ 00bbd1b8 */
    return *(long *)(*(long *)(param_1 + 0x20) + 8) == *(long *)(*(long *)(lVar3 + 0x20) + 8);
  }
  return false;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbfa0"></a> `00bbbfa0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbbfa4"></a> `00bbbfa4` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbbfa8"></a> `00bbbfa8` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbfac"></a> `00bbbfac` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbfb0"></a> `00bbbfb0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbbfb4"></a> `00bbbfb4` | `08 03 00 b0` | adrp x8,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbfb8"></a> `00bbbfb8` | `35 04 40 f9` | ldr x21,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbfbc"></a> `00bbbfbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbbfc0"></a> `00bbbfc0` | `08 31 40 f9` | ldr x8,[x8, #0x60] | `FALL_THROUGH`
<a id="insn-00bbbfc4"></a> `00bbbfc4` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bbbfc8"></a> `00bbbfc8` | `a0 01 00 54` | b.eq 0x00bbbffc | `CONDITIONAL_JUMP`
<a id="insn-00bbbfcc"></a> `00bbbfcc` | `76 12 40 b9` | ldr w22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbfd0"></a> `00bbbfd0` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbbfd4"></a> `00bbbfd4` | `df 06 1d 72` | tst w22,#0x18 | `FALL_THROUGH`
<a id="insn-00bbbfd8"></a> `00bbbfd8` | `00 03 00 54` | b.eq 0x00bbc038 | `CONDITIONAL_JUMP`
<a id="insn-00bbbfdc"></a> `00bbbfdc` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bbbfe0"></a> `00bbbfe0` | `a0 00 00 54` | b.eq 0x00bbbff4 | `CONDITIONAL_JUMP`
<a id="insn-00bbbfe4"></a> `00bbbfe4` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbfe8"></a> `00bbbfe8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbbfec"></a> `00bbbfec` | `79 8a 00 94` | bl 0x00bde9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbff0"></a> `00bbbff0` | `00 04 00 35` | cbnz w0,0x00bbc070 | `CONDITIONAL_JUMP`
<a id="insn-00bbbff4"></a> `00bbbff4` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbff8"></a> `00bbbff8` | `39 00 00 14` | b 0x00bbc0dc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbffc"></a> `00bbbffc` | `60 0e 40 f9` | ldr x0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbc000"></a> `00bbc000` | `60 06 00 b4` | cbz x0,0x00bbc0cc | `CONDITIONAL_JUMP`
<a id="insn-00bbc004"></a> `00bbc004` | `01 03 00 90` | adrp x1,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbc008"></a> `00bbc008` | `08 03 00 90` | adrp x8,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbc00c"></a> `00bbc00c` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bbc010"></a> `00bbc010` | `21 24 40 f9` | ldr x1,[x1, #0x48] | `FALL_THROUGH`
<a id="insn-00bbc014"></a> `00bbc014` | `08 3d 40 f9` | ldr x8,[x8, #0x78] | `FALL_THROUGH`
<a id="insn-00bbc018"></a> `00bbc018` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbc01c"></a> `00bbc01c` | `e2 03 08 aa` | mov x2,x8 | `FALL_THROUGH`
<a id="insn-00bbc020"></a> `00bbc020` | `e8 7d 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc024"></a> `00bbc024` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bbc028"></a> `00bbc028` | `20 05 00 b4` | cbz x0,0x00bbc0cc | `CONDITIONAL_JUMP`
<a id="insn-00bbc02c"></a> `00bbc02c` | `08 ba ff 90` | adrp x8,0x2fc000 | `FALL_THROUGH`
<a id="insn-00bbc030"></a> `00bbc030` | `08 a1 26 91` | add x8,x8,#0x9a8 | `FALL_THROUGH`
<a id="insn-00bbc034"></a> `00bbc034` | `28 00 00 14` | b 0x00bbc0d4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbc038"></a> `00bbc038` | `01 03 00 90` | adrp x1,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbc03c"></a> `00bbc03c` | `02 03 00 90` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbc040"></a> `00bbc040` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbc044"></a> `00bbc044` | `21 24 40 f9` | ldr x1,[x1, #0x48] | `FALL_THROUGH`
<a id="insn-00bbc048"></a> `00bbc048` | `42 2c 40 f9` | ldr x2,[x2, #0x58] | `FALL_THROUGH`
<a id="insn-00bbc04c"></a> `00bbc04c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbc050"></a> `00bbc050` | `dc 7d 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc054"></a> `00bbc054` | `e0 00 00 b4` | cbz x0,0x00bbc070 | `CONDITIONAL_JUMP`
<a id="insn-00bbc058"></a> `00bbc058` | `08 40 40 39` | ldrb w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc05c"></a> `00bbc05c` | `1f 05 1d 72` | tst w8,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc060"></a> `00bbc060` | `e1 fb ff 54` | b.ne 0x00bbbfdc | `CONDITIONAL_JUMP`
<a id="insn-00bbc064"></a> `00bbc064` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc068"></a> `00bbc068` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bbc06c"></a> `00bbc06c` | `40 fc ff 54` | b.eq 0x00bbbff4 | `CONDITIONAL_JUMP`
<a id="insn-00bbc070"></a> `00bbc070` | `01 03 00 90` | adrp x1,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbc074"></a> `00bbc074` | `02 03 00 90` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbc078"></a> `00bbc078` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbc07c"></a> `00bbc07c` | `21 24 40 f9` | ldr x1,[x1, #0x48] | `FALL_THROUGH`
<a id="insn-00bbc080"></a> `00bbc080` | `42 40 40 f9` | ldr x2,[x2, #0x80] | `FALL_THROUGH`
<a id="insn-00bbc084"></a> `00bbc084` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbc088"></a> `00bbc088` | `ce 7d 00 94` | bl 0x00bdb7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc08c"></a> `00bbc08c` | `80 02 00 b4` | cbz x0,0x00bbc0dc | `CONDITIONAL_JUMP`
<a id="insn-00bbc090"></a> `00bbc090` | `08 10 40 b9` | ldr w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc094"></a> `00bbc094` | `09 01 36 0a` | bic w9,w8,w22 | `FALL_THROUGH`
<a id="insn-00bbc098"></a> `00bbc098` | `3f 09 00 72` | tst w9,#0x7 | `FALL_THROUGH`
<a id="insn-00bbc09c"></a> `00bbc09c` | `41 01 00 54` | b.ne 0x00bbc0c4 | `CONDITIONAL_JUMP`
<a id="insn-00bbc0a0"></a> `00bbc0a0` | `c8 02 28 0a` | bic w8,w22,w8 | `FALL_THROUGH`
<a id="insn-00bbc0a4"></a> `00bbc0a4` | `1f 05 1b 72` | tst w8,#0x60 | `FALL_THROUGH`
<a id="insn-00bbc0a8"></a> `00bbc0a8` | `e1 00 00 54` | b.ne 0x00bbc0c4 | `CONDITIONAL_JUMP`
<a id="insn-00bbc0ac"></a> `00bbc0ac` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbc0b0"></a> `00bbc0b0` | `09 0c 40 f9` | ldr x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bbc0b4"></a> `00bbc0b4` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc0b8"></a> `00bbc0b8` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc0bc"></a> `00bbc0bc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbc0c0"></a> `00bbc0c0` | `80 01 00 54` | b.eq 0x00bbc0f0 | `CONDITIONAL_JUMP`
<a id="insn-00bbc0c4"></a> `00bbc0c4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbc0c8"></a> `00bbc0c8` | `05 00 00 14` | b 0x00bbc0dc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbc0cc"></a> `00bbc0cc` | `08 ba ff 90` | adrp x8,0x2fc000 | `FALL_THROUGH`
<a id="insn-00bbc0d0"></a> `00bbc0d0` | `08 e1 26 91` | add x8,x8,#0x9b8 | `FALL_THROUGH`
<a id="insn-00bbc0d4"></a> `00bbc0d4` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00bbc0d8"></a> `00bbc0d8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc0dc"></a> `00bbc0dc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc0e0"></a> `00bbc0e0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc0e4"></a> `00bbc0e4` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbc0e8"></a> `00bbc0e8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbc0ec"></a> `00bbc0ec` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbc0f0"></a> `00bbc0f0` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc0f4"></a> `00bbc0f4` | `09 10 40 f9` | ldr x9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc0f8"></a> `00bbc0f8` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc0fc"></a> `00bbc0fc` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc100"></a> `00bbc100` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbc104"></a> `00bbc104` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bbc108"></a> `00bbc108` | `f5 ff ff 17` | b 0x00bbc0dc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbbfa0`](#insn-00bbbfa0) 範囲 `[['00bbbfa0', '00bbbfa7']]`
  - `FALL_THROUGH` [`00bbbfa4`](#insn-00bbbfa4) → [`00bbbfa8`](#insn-00bbbfa8)
- ブロック [`00bbbfa8`](#insn-00bbbfa8) 範囲 `[['00bbbfa8', '00bbbfb3']]`
  - `FALL_THROUGH` [`00bbbfb0`](#insn-00bbbfb0) → [`00bbbfb4`](#insn-00bbbfb4)
- ブロック [`00bbbfb4`](#insn-00bbbfb4) 範囲 `[['00bbbfb4', '00bbbfc3']]`
  - `FALL_THROUGH` [`00bbbfc0`](#insn-00bbbfc0) → [`00bbbfc4`](#insn-00bbbfc4)
- ブロック [`00bbbfc4`](#insn-00bbbfc4) 範囲 `[['00bbbfc4', '00bbbfcb']]`
  - `CONDITIONAL_JUMP` [`00bbbfc8`](#insn-00bbbfc8) → [`00bbbffc`](#insn-00bbbffc)
  - `FALL_THROUGH` [`00bbbfc8`](#insn-00bbbfc8) → [`00bbbfcc`](#insn-00bbbfcc)
- ブロック [`00bbbfcc`](#insn-00bbbfcc) 範囲 `[['00bbbfcc', '00bbbfdb']]`
  - `CONDITIONAL_JUMP` [`00bbbfd8`](#insn-00bbbfd8) → [`00bbc038`](#insn-00bbc038)
  - `FALL_THROUGH` [`00bbbfd8`](#insn-00bbbfd8) → [`00bbbfdc`](#insn-00bbbfdc)
- ブロック [`00bbbfdc`](#insn-00bbbfdc) 範囲 `[['00bbbfdc', '00bbbfe3']]`
  - `CONDITIONAL_JUMP` [`00bbbfe0`](#insn-00bbbfe0) → [`00bbbff4`](#insn-00bbbff4)
  - `FALL_THROUGH` [`00bbbfe0`](#insn-00bbbfe0) → [`00bbbfe4`](#insn-00bbbfe4)
- ブロック [`00bbbfe4`](#insn-00bbbfe4) 範囲 `[['00bbbfe4', '00bbbff3']]`
  - `CONDITIONAL_JUMP` [`00bbbff0`](#insn-00bbbff0) → [`00bbc070`](#insn-00bbc070)
  - `FALL_THROUGH` [`00bbbff0`](#insn-00bbbff0) → [`00bbbff4`](#insn-00bbbff4)
- ブロック [`00bbbff4`](#insn-00bbbff4) 範囲 `[['00bbbff4', '00bbbffb']]`
  - `UNCONDITIONAL_JUMP` [`00bbbff8`](#insn-00bbbff8) → [`00bbc0dc`](#insn-00bbc0dc)
- ブロック [`00bbbffc`](#insn-00bbbffc) 範囲 `[['00bbbffc', '00bbc003']]`
  - `CONDITIONAL_JUMP` [`00bbc000`](#insn-00bbc000) → [`00bbc0cc`](#insn-00bbc0cc)
  - `FALL_THROUGH` [`00bbc000`](#insn-00bbc000) → [`00bbc004`](#insn-00bbc004)
- ブロック [`00bbc004`](#insn-00bbc004) 範囲 `[['00bbc004', '00bbc02b']]`
  - `CONDITIONAL_JUMP` [`00bbc028`](#insn-00bbc028) → [`00bbc0cc`](#insn-00bbc0cc)
  - `FALL_THROUGH` [`00bbc028`](#insn-00bbc028) → [`00bbc02c`](#insn-00bbc02c)
- ブロック [`00bbc02c`](#insn-00bbc02c) 範囲 `[['00bbc02c', '00bbc037']]`
  - `UNCONDITIONAL_JUMP` [`00bbc034`](#insn-00bbc034) → [`00bbc0d4`](#insn-00bbc0d4)
- ブロック [`00bbc038`](#insn-00bbc038) 範囲 `[['00bbc038', '00bbc057']]`
  - `CONDITIONAL_JUMP` [`00bbc054`](#insn-00bbc054) → [`00bbc070`](#insn-00bbc070)
  - `FALL_THROUGH` [`00bbc054`](#insn-00bbc054) → [`00bbc058`](#insn-00bbc058)
- ブロック [`00bbc058`](#insn-00bbc058) 範囲 `[['00bbc058', '00bbc063']]`
  - `CONDITIONAL_JUMP` [`00bbc060`](#insn-00bbc060) → [`00bbbfdc`](#insn-00bbbfdc)
  - `FALL_THROUGH` [`00bbc060`](#insn-00bbc060) → [`00bbc064`](#insn-00bbc064)
- ブロック [`00bbc064`](#insn-00bbc064) 範囲 `[['00bbc064', '00bbc06f']]`
  - `CONDITIONAL_JUMP` [`00bbc06c`](#insn-00bbc06c) → [`00bbbff4`](#insn-00bbbff4)
  - `FALL_THROUGH` [`00bbc06c`](#insn-00bbc06c) → [`00bbc070`](#insn-00bbc070)
- ブロック [`00bbc070`](#insn-00bbc070) 範囲 `[['00bbc070', '00bbc08f']]`
  - `CONDITIONAL_JUMP` [`00bbc08c`](#insn-00bbc08c) → [`00bbc0dc`](#insn-00bbc0dc)
  - `FALL_THROUGH` [`00bbc08c`](#insn-00bbc08c) → [`00bbc090`](#insn-00bbc090)
- ブロック [`00bbc090`](#insn-00bbc090) 範囲 `[['00bbc090', '00bbc093']]`
  - `FALL_THROUGH` [`00bbc090`](#insn-00bbc090) → [`00bbc094`](#insn-00bbc094)
- ブロック [`00bbc094`](#insn-00bbc094) 範囲 `[['00bbc094', '00bbc09f']]`
  - `CONDITIONAL_JUMP` [`00bbc09c`](#insn-00bbc09c) → [`00bbc0c4`](#insn-00bbc0c4)
  - `FALL_THROUGH` [`00bbc09c`](#insn-00bbc09c) → [`00bbc0a0`](#insn-00bbc0a0)
- ブロック [`00bbc0a0`](#insn-00bbc0a0) 範囲 `[['00bbc0a0', '00bbc0ab']]`
  - `CONDITIONAL_JUMP` [`00bbc0a8`](#insn-00bbc0a8) → [`00bbc0c4`](#insn-00bbc0c4)
  - `FALL_THROUGH` [`00bbc0a8`](#insn-00bbc0a8) → [`00bbc0ac`](#insn-00bbc0ac)
- ブロック [`00bbc0ac`](#insn-00bbc0ac) 範囲 `[['00bbc0ac', '00bbc0c3']]`
  - `CONDITIONAL_JUMP` [`00bbc0c0`](#insn-00bbc0c0) → [`00bbc0f0`](#insn-00bbc0f0)
  - `FALL_THROUGH` [`00bbc0c0`](#insn-00bbc0c0) → [`00bbc0c4`](#insn-00bbc0c4)
- ブロック [`00bbc0c4`](#insn-00bbc0c4) 範囲 `[['00bbc0c4', '00bbc0cb']]`
  - `UNCONDITIONAL_JUMP` [`00bbc0c8`](#insn-00bbc0c8) → [`00bbc0dc`](#insn-00bbc0dc)
- ブロック [`00bbc0cc`](#insn-00bbc0cc) 範囲 `[['00bbc0cc', '00bbc0cf']]`
  - `FALL_THROUGH` [`00bbc0cc`](#insn-00bbc0cc) → [`00bbc0d0`](#insn-00bbc0d0)
- ブロック [`00bbc0d0`](#insn-00bbc0d0) 範囲 `[['00bbc0d0', '00bbc0d3']]`
  - `FALL_THROUGH` [`00bbc0d0`](#insn-00bbc0d0) → [`00bbc0d4`](#insn-00bbc0d4)
- ブロック [`00bbc0d4`](#insn-00bbc0d4) 範囲 `[['00bbc0d4', '00bbc0db']]`
  - `FALL_THROUGH` [`00bbc0d8`](#insn-00bbc0d8) → [`00bbc0dc`](#insn-00bbc0dc)
- ブロック [`00bbc0dc`](#insn-00bbc0dc) 範囲 `[['00bbc0dc', '00bbc0ef']]`
- ブロック [`00bbc0f0`](#insn-00bbc0f0) 範囲 `[['00bbc0f0', '00bbc0f3']]`
  - `FALL_THROUGH` [`00bbc0f0`](#insn-00bbc0f0) → [`00bbc0f4`](#insn-00bbc0f4)
- ブロック [`00bbc0f4`](#insn-00bbc0f4) 範囲 `[['00bbc0f4', '00bbc0fb']]`
  - `FALL_THROUGH` [`00bbc0f8`](#insn-00bbc0f8) → [`00bbc0fc`](#insn-00bbc0fc)
- ブロック [`00bbc0fc`](#insn-00bbc0fc) 範囲 `[['00bbc0fc', '00bbc10b']]`
  - `UNCONDITIONAL_JUMP` [`00bbc108`](#insn-00bbc108) → [`00bbc0dc`](#insn-00bbc0dc)

## 命令位置別の参照

- [`00bbbfa4`](#insn-00bbbfa4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfa8`](#insn-00bbbfa8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfac`](#insn-00bbbfac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfc0`](#insn-00bbbfc0) → `00c1c060`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbfc8`](#insn-00bbbfc8) → [`00bbbffc`](#insn-00bbbffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfd8`](#insn-00bbbfd8) → [`00bbc038`](#insn-00bbc038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfe0`](#insn-00bbbfe0) → [`00bbbff4`](#insn-00bbbff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfec`](#insn-00bbbfec) → [`00bde9d0`](../00bde/00bde9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde9d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbbff0`](#insn-00bbbff0) → [`00bbc070`](#insn-00bbc070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbff8`](#insn-00bbbff8) → [`00bbc0dc`](#insn-00bbc0dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc000`](#insn-00bbc000) → [`00bbc0cc`](#insn-00bbc0cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc010`](#insn-00bbc010) → `00c1c048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc010`](#insn-00bbc010) → `00c16c10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbc014`](#insn-00bbc014) → `00c1c078`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc01c`](#insn-00bbc01c) → `00c16c70`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv120__function_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbc020`](#insn-00bbc020) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc028`](#insn-00bbc028) → [`00bbc0cc`](#insn-00bbc0cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc034`](#insn-00bbc034) → [`00bbc0d4`](#insn-00bbc0d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc044`](#insn-00bbc044) → `00c1c048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc044`](#insn-00bbc044) → `00c16c10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbc048`](#insn-00bbc048) → `00c1c058`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc048`](#insn-00bbc048) → `00c16c40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv117__pbase_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbc050`](#insn-00bbc050) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc054`](#insn-00bbc054) → [`00bbc070`](#insn-00bbc070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc060`](#insn-00bbc060) → [`00bbbfdc`](#insn-00bbbfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc06c`](#insn-00bbc06c) → [`00bbbff4`](#insn-00bbbff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc07c`](#insn-00bbc07c) → `00c1c048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc07c`](#insn-00bbc07c) → `00c16c10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbc080`](#insn-00bbc080) → `00c1c080`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc080`](#insn-00bbc080) → `00c16c88`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv129__pointer_to_member_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbc088`](#insn-00bbc088) → [`00bdb7c0`](../00bdb/00bdb7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbc08c`](#insn-00bbc08c) → [`00bbc0dc`](#insn-00bbc0dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc09c`](#insn-00bbc09c) → [`00bbc0c4`](#insn-00bbc0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0a8`](#insn-00bbc0a8) → [`00bbc0c4`](#insn-00bbc0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0c0`](#insn-00bbc0c0) → [`00bbc0f0`](#insn-00bbc0f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0c8`](#insn-00bbc0c8) → [`00bbc0dc`](#insn-00bbc0dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0d4`](#insn-00bbc0d4) → `002fc9a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0d4`](#insn-00bbc0d4) → `002fc9b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0dc`](#insn-00bbc0dc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0e0`](#insn-00bbc0e0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0e4`](#insn-00bbc0e4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc108`](#insn-00bbc108) → [`00bbc0dc`](#insn-00bbc0dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbfa4`](#insn-00bbbfa4)

~~~json
{
  "source": "00bbbfa4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfa8`](#insn-00bbbfa8)

~~~json
{
  "source": "00bbbfa8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfac`](#insn-00bbbfac)

~~~json
{
  "source": "00bbbfac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfc0`](#insn-00bbbfc0)

~~~json
{
  "source": "00bbbfc0",
  "target": "00c1c060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbfc8`](#insn-00bbbfc8)

~~~json
{
  "source": "00bbbfc8",
  "target": "00bbbffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfd8`](#insn-00bbbfd8)

~~~json
{
  "source": "00bbbfd8",
  "target": "00bbc038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfe0`](#insn-00bbbfe0)

~~~json
{
  "source": "00bbbfe0",
  "target": "00bbbff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfec`](#insn-00bbbfec)

~~~json
{
  "source": "00bbbfec",
  "target": "00bde9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbff0`](#insn-00bbbff0)

~~~json
{
  "source": "00bbbff0",
  "target": "00bbc070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbff8`](#insn-00bbbff8)

~~~json
{
  "source": "00bbbff8",
  "target": "00bbc0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc000`](#insn-00bbc000)

~~~json
{
  "source": "00bbc000",
  "target": "00bbc0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc010`](#insn-00bbc010)

~~~json
{
  "source": "00bbc010",
  "target": "00c1c048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c048",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc010`](#insn-00bbc010)

~~~json
{
  "source": "00bbc010",
  "target": "00c16c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc014`](#insn-00bbc014)

~~~json
{
  "source": "00bbc014",
  "target": "00c1c078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c078",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc01c`](#insn-00bbc01c)

~~~json
{
  "source": "00bbc01c",
  "target": "00c16c70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc020`](#insn-00bbc020)

~~~json
{
  "source": "00bbc020",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc028`](#insn-00bbc028)

~~~json
{
  "source": "00bbc028",
  "target": "00bbc0cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc034`](#insn-00bbc034)

~~~json
{
  "source": "00bbc034",
  "target": "00bbc0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc044`](#insn-00bbc044)

~~~json
{
  "source": "00bbc044",
  "target": "00c1c048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c048",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc044`](#insn-00bbc044)

~~~json
{
  "source": "00bbc044",
  "target": "00c16c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc048`](#insn-00bbc048)

~~~json
{
  "source": "00bbc048",
  "target": "00c1c058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c058",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc048`](#insn-00bbc048)

~~~json
{
  "source": "00bbc048",
  "target": "00c16c40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c40",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc050`](#insn-00bbc050)

~~~json
{
  "source": "00bbc050",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc054`](#insn-00bbc054)

~~~json
{
  "source": "00bbc054",
  "target": "00bbc070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc060`](#insn-00bbc060)

~~~json
{
  "source": "00bbc060",
  "target": "00bbbfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc06c`](#insn-00bbc06c)

~~~json
{
  "source": "00bbc06c",
  "target": "00bbbff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc07c`](#insn-00bbc07c)

~~~json
{
  "source": "00bbc07c",
  "target": "00c1c048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c048",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc07c`](#insn-00bbc07c)

~~~json
{
  "source": "00bbc07c",
  "target": "00c16c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc080`](#insn-00bbc080)

~~~json
{
  "source": "00bbc080",
  "target": "00c1c080",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c080",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc080`](#insn-00bbc080)

~~~json
{
  "source": "00bbc080",
  "target": "00c16c88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc088`](#insn-00bbc088)

~~~json
{
  "source": "00bbc088",
  "target": "00bdb7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc08c`](#insn-00bbc08c)

~~~json
{
  "source": "00bbc08c",
  "target": "00bbc0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc09c`](#insn-00bbc09c)

~~~json
{
  "source": "00bbc09c",
  "target": "00bbc0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0a8`](#insn-00bbc0a8)

~~~json
{
  "source": "00bbc0a8",
  "target": "00bbc0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0c0`](#insn-00bbc0c0)

~~~json
{
  "source": "00bbc0c0",
  "target": "00bbc0f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0c8`](#insn-00bbc0c8)

~~~json
{
  "source": "00bbc0c8",
  "target": "00bbc0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0d4`](#insn-00bbc0d4)

~~~json
{
  "source": "00bbc0d4",
  "target": "002fc9a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0d4`](#insn-00bbc0d4)

~~~json
{
  "source": "00bbc0d4",
  "target": "002fc9b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0dc`](#insn-00bbc0dc)

~~~json
{
  "source": "00bbc0dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0e0`](#insn-00bbc0e0)

~~~json
{
  "source": "00bbc0e0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0e4`](#insn-00bbc0e4)

~~~json
{
  "source": "00bbc0e4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc108`](#insn-00bbc108)

~~~json
{
  "source": "00bbc108",
  "target": "00bbc0dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
