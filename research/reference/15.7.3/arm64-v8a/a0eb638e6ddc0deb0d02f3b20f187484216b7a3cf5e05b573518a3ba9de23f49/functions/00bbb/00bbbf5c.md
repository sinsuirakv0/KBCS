# 00bbbf5c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbbe94`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbbe94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-8340ce8479ec6e2134df1e28dd611903)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbbfa0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbfa0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-91c8a77b823f33b29b3df49f95249431)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbf5c",
  "name": "FUN_00bbbf5c",
  "size": 364,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a2e0bbe7055dfcf1067c2df772e817161422077e9ac045c428b5aacce6d9d0b",
  "source_text_sha256": "7a2e0bbe7055dfcf1067c2df772e817161422077e9ac045c428b5aacce6d9d0b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbf5c",
        "00bbc0c7"
      ]
    ],
    "bytes_sha256": "eeaaade4ef91bd923b4a0f804d13fc1e5cf650fb8a91baa34274351885dfbf77",
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

- [00bdb770](../00bdb/00bdb770.md)
- [00bde980](../00bde/00bde980.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2451 bytes

~~~c

bool FUN_00bbbf5c(long param_1,long param_2,undefined8 *param_3)

{
  uint uVar1;
  int iVar2;
  long lVar3;
  undefined *puVar4;
  char *__s2;
  
                    /* try { // try from 00bbbf64 to 00cbbf6f has its CatchHandler @ 00bbd1a4 */
                    /* try { // try from 00bbbf70 to 00cbbf7f has its CatchHandler @ 00bbd190 */
  __s2 = *(char **)(param_2 + 8);
                    /* try { // try from 00bbbf80 to 00cbbf93 has its CatchHandler @ 00bbd178 */
  if (__s2 == PTR__ZTSDn_00c1c010) {
    if ((*(long *)(param_1 + 0x18) == 0) ||
       (lVar3 = __dynamic_cast(*(long *)(param_1 + 0x18),
                               PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                               PTR__ZTIN10__cxxabiv120__function_type_infoE_00c1c028,0), lVar3 == 0)
       ) {
                    /* try { // try from 00bbc08c to 00cbc09b has its CatchHandler @ 00bbd3e8 */
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
    lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                           PTR__ZTIN10__cxxabiv117__pbase_type_infoE_00c1c008,0);
    if (lVar3 == 0) goto LAB_00bbc02c;
    if ((*(byte *)(lVar3 + 0x10) & 0x18) == 0) {
      if (*(char **)(param_1 + 8) == __s2) {
        return true;
      }
      goto LAB_00bbc02c;
    }
  }
  if ((param_1 == param_2) || (iVar2 = strcmp(*(char **)(param_1 + 8),__s2), iVar2 == 0)) {
    return true;
  }
LAB_00bbc02c:
  lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                         PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c030,0);
  if (lVar3 == 0) {
    return false;
  }
                    /* try { // try from 00bbc050 to 00cbc05b has its CatchHandler @ 00bbd374 */
  if ((((*(uint *)(lVar3 + 0x10) & (uVar1 ^ 0xffffffff) & 7) == 0) &&
      ((uVar1 & (*(uint *)(lVar3 + 0x10) ^ 0xffffffff) & 0x60) == 0)) &&
     (*(long *)(*(long *)(param_1 + 0x18) + 8) == *(long *)(*(long *)(lVar3 + 0x18) + 8))) {
                    /* try { // try from 00bbc0b0 to 00cbc0b7 has its CatchHandler @ 00bbd2e8 */
                    /* try { // try from 00bbc0b8 to 00cbc0bf has its CatchHandler @ 00bbd174 */
    return *(long *)(*(long *)(param_1 + 0x20) + 8) == *(long *)(*(long *)(lVar3 + 0x20) + 8);
  }
  return false;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbf5c"></a> `00bbbf5c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbbf60"></a> `00bbbf60` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bbbf64"></a> `00bbbf64` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbf68"></a> `00bbbf68` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbf6c"></a> `00bbbf6c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbbf70"></a> `00bbbf70` | `08 03 00 b0` | adrp x8,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbf74"></a> `00bbbf74` | `35 04 40 f9` | ldr x21,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbf78"></a> `00bbbf78` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbbf7c"></a> `00bbbf7c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbf80"></a> `00bbbf80` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bbbf84"></a> `00bbbf84` | `a0 01 00 54` | b.eq 0x00bbbfb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbbf88"></a> `00bbbf88` | `76 12 40 b9` | ldr w22,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbf8c"></a> `00bbbf8c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbbf90"></a> `00bbbf90` | `df 06 1d 72` | tst w22,#0x18 | `FALL_THROUGH`
<a id="insn-00bbbf94"></a> `00bbbf94` | `00 03 00 54` | b.eq 0x00bbbff4 | `CONDITIONAL_JUMP`
<a id="insn-00bbbf98"></a> `00bbbf98` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bbbf9c"></a> `00bbbf9c` | `a0 00 00 54` | b.eq 0x00bbbfb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbbfa0"></a> `00bbbfa0` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbfa4"></a> `00bbbfa4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbbfa8"></a> `00bbbfa8` | `76 8a 00 94` | bl 0x00bde980 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbfac"></a> `00bbbfac` | `00 04 00 35` | cbnz w0,0x00bbc02c | `CONDITIONAL_JUMP`
<a id="insn-00bbbfb0"></a> `00bbbfb0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbfb4"></a> `00bbbfb4` | `39 00 00 14` | b 0x00bbc098 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbfb8"></a> `00bbbfb8` | `60 0e 40 f9` | ldr x0,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbfbc"></a> `00bbbfbc` | `60 06 00 b4` | cbz x0,0x00bbc088 | `CONDITIONAL_JUMP`
<a id="insn-00bbbfc0"></a> `00bbbfc0` | `01 03 00 90` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbfc4"></a> `00bbbfc4` | `08 03 00 b0` | adrp x8,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbfc8"></a> `00bbbfc8` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bbbfcc"></a> `00bbbfcc` | `21 fc 47 f9` | ldr x1,[x1, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbbfd0"></a> `00bbbfd0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbfd4"></a> `00bbbfd4` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbfd8"></a> `00bbbfd8` | `e2 03 08 aa` | mov x2,x8 | `FALL_THROUGH`
<a id="insn-00bbbfdc"></a> `00bbbfdc` | `e5 7d 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbfe0"></a> `00bbbfe0` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bbbfe4"></a> `00bbbfe4` | `20 05 00 b4` | cbz x0,0x00bbc088 | `CONDITIONAL_JUMP`
<a id="insn-00bbbfe8"></a> `00bbbfe8` | `08 ba ff b0` | adrp x8,0x2fc000 | `FALL_THROUGH`
<a id="insn-00bbbfec"></a> `00bbbfec` | `08 a1 26 91` | add x8,x8,#0x9a8 | `FALL_THROUGH`
<a id="insn-00bbbff0"></a> `00bbbff0` | `28 00 00 14` | b 0x00bbc090 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbff4"></a> `00bbbff4` | `01 03 00 90` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbff8"></a> `00bbbff8` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbffc"></a> `00bbbffc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbc000"></a> `00bbc000` | `21 fc 47 f9` | ldr x1,[x1, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbc004"></a> `00bbc004` | `42 04 40 f9` | ldr x2,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc008"></a> `00bbc008` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbc00c"></a> `00bbc00c` | `d9 7d 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc010"></a> `00bbc010` | `e0 00 00 b4` | cbz x0,0x00bbc02c | `CONDITIONAL_JUMP`
<a id="insn-00bbc014"></a> `00bbc014` | `08 40 40 39` | ldrb w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc018"></a> `00bbc018` | `1f 05 1d 72` | tst w8,#0x18 | `FALL_THROUGH`
<a id="insn-00bbc01c"></a> `00bbc01c` | `e1 fb ff 54` | b.ne 0x00bbbf98 | `CONDITIONAL_JUMP`
<a id="insn-00bbc020"></a> `00bbc020` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc024"></a> `00bbc024` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bbc028"></a> `00bbc028` | `40 fc ff 54` | b.eq 0x00bbbfb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbc02c"></a> `00bbc02c` | `e1 02 00 f0` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbc030"></a> `00bbc030` | `02 03 00 90` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbc034"></a> `00bbc034` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbc038"></a> `00bbc038` | `21 fc 47 f9` | ldr x1,[x1, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbc03c"></a> `00bbc03c` | `42 18 40 f9` | ldr x2,[x2, #0x30] | `FALL_THROUGH`
<a id="insn-00bbc040"></a> `00bbc040` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbc044"></a> `00bbc044` | `cb 7d 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbc048"></a> `00bbc048` | `80 02 00 b4` | cbz x0,0x00bbc098 | `CONDITIONAL_JUMP`
<a id="insn-00bbc04c"></a> `00bbc04c` | `08 10 40 b9` | ldr w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc050"></a> `00bbc050` | `09 01 36 0a` | bic w9,w8,w22 | `FALL_THROUGH`
<a id="insn-00bbc054"></a> `00bbc054` | `3f 09 00 72` | tst w9,#0x7 | `FALL_THROUGH`
<a id="insn-00bbc058"></a> `00bbc058` | `41 01 00 54` | b.ne 0x00bbc080 | `CONDITIONAL_JUMP`
<a id="insn-00bbc05c"></a> `00bbc05c` | `c8 02 28 0a` | bic w8,w22,w8 | `FALL_THROUGH`
<a id="insn-00bbc060"></a> `00bbc060` | `1f 05 1b 72` | tst w8,#0x60 | `FALL_THROUGH`
<a id="insn-00bbc064"></a> `00bbc064` | `e1 00 00 54` | b.ne 0x00bbc080 | `CONDITIONAL_JUMP`
<a id="insn-00bbc068"></a> `00bbc068` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbc06c"></a> `00bbc06c` | `09 0c 40 f9` | ldr x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bbc070"></a> `00bbc070` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc074"></a> `00bbc074` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc078"></a> `00bbc078` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbc07c"></a> `00bbc07c` | `80 01 00 54` | b.eq 0x00bbc0ac | `CONDITIONAL_JUMP`
<a id="insn-00bbc080"></a> `00bbc080` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbc084"></a> `00bbc084` | `05 00 00 14` | b 0x00bbc098 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbc088"></a> `00bbc088` | `08 ba ff 90` | adrp x8,0x2fc000 | `FALL_THROUGH`
<a id="insn-00bbc08c"></a> `00bbc08c` | `08 e1 26 91` | add x8,x8,#0x9b8 | `FALL_THROUGH`
<a id="insn-00bbc090"></a> `00bbc090` | `48 00 00 f9` | str x8,[x2] | `FALL_THROUGH`
<a id="insn-00bbc094"></a> `00bbc094` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbc098"></a> `00bbc098` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc09c"></a> `00bbc09c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbc0a0"></a> `00bbc0a0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bbc0a4"></a> `00bbc0a4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbc0a8"></a> `00bbc0a8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbc0ac"></a> `00bbc0ac` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc0b0"></a> `00bbc0b0` | `09 10 40 f9` | ldr x9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bbc0b4"></a> `00bbc0b4` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc0b8"></a> `00bbc0b8` | `29 05 40 f9` | ldr x9,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bbc0bc"></a> `00bbc0bc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbc0c0"></a> `00bbc0c0` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bbc0c4"></a> `00bbc0c4` | `f5 ff ff 17` | b 0x00bbc098 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbbf5c`](#insn-00bbbf5c) 範囲 `[['00bbbf5c', '00bbbf63']]`
  - `FALL_THROUGH` [`00bbbf60`](#insn-00bbbf60) → [`00bbbf64`](#insn-00bbbf64)
- ブロック [`00bbbf64`](#insn-00bbbf64) 範囲 `[['00bbbf64', '00bbbf6f']]`
  - `FALL_THROUGH` [`00bbbf6c`](#insn-00bbbf6c) → [`00bbbf70`](#insn-00bbbf70)
- ブロック [`00bbbf70`](#insn-00bbbf70) 範囲 `[['00bbbf70', '00bbbf7f']]`
  - `FALL_THROUGH` [`00bbbf7c`](#insn-00bbbf7c) → [`00bbbf80`](#insn-00bbbf80)
- ブロック [`00bbbf80`](#insn-00bbbf80) 範囲 `[['00bbbf80', '00bbbf87']]`
  - `CONDITIONAL_JUMP` [`00bbbf84`](#insn-00bbbf84) → [`00bbbfb8`](#insn-00bbbfb8)
  - `FALL_THROUGH` [`00bbbf84`](#insn-00bbbf84) → [`00bbbf88`](#insn-00bbbf88)
- ブロック [`00bbbf88`](#insn-00bbbf88) 範囲 `[['00bbbf88', '00bbbf97']]`
  - `CONDITIONAL_JUMP` [`00bbbf94`](#insn-00bbbf94) → [`00bbbff4`](#insn-00bbbff4)
  - `FALL_THROUGH` [`00bbbf94`](#insn-00bbbf94) → [`00bbbf98`](#insn-00bbbf98)
- ブロック [`00bbbf98`](#insn-00bbbf98) 範囲 `[['00bbbf98', '00bbbf9f']]`
  - `CONDITIONAL_JUMP` [`00bbbf9c`](#insn-00bbbf9c) → [`00bbbfb0`](#insn-00bbbfb0)
  - `FALL_THROUGH` [`00bbbf9c`](#insn-00bbbf9c) → [`00bbbfa0`](#insn-00bbbfa0)
- ブロック [`00bbbfa0`](#insn-00bbbfa0) 範囲 `[['00bbbfa0', '00bbbfaf']]`
  - `CONDITIONAL_JUMP` [`00bbbfac`](#insn-00bbbfac) → [`00bbc02c`](#insn-00bbc02c)
  - `FALL_THROUGH` [`00bbbfac`](#insn-00bbbfac) → [`00bbbfb0`](#insn-00bbbfb0)
- ブロック [`00bbbfb0`](#insn-00bbbfb0) 範囲 `[['00bbbfb0', '00bbbfb7']]`
  - `UNCONDITIONAL_JUMP` [`00bbbfb4`](#insn-00bbbfb4) → [`00bbc098`](#insn-00bbc098)
- ブロック [`00bbbfb8`](#insn-00bbbfb8) 範囲 `[['00bbbfb8', '00bbbfbf']]`
  - `CONDITIONAL_JUMP` [`00bbbfbc`](#insn-00bbbfbc) → [`00bbc088`](#insn-00bbc088)
  - `FALL_THROUGH` [`00bbbfbc`](#insn-00bbbfbc) → [`00bbbfc0`](#insn-00bbbfc0)
- ブロック [`00bbbfc0`](#insn-00bbbfc0) 範囲 `[['00bbbfc0', '00bbbfe7']]`
  - `CONDITIONAL_JUMP` [`00bbbfe4`](#insn-00bbbfe4) → [`00bbc088`](#insn-00bbc088)
  - `FALL_THROUGH` [`00bbbfe4`](#insn-00bbbfe4) → [`00bbbfe8`](#insn-00bbbfe8)
- ブロック [`00bbbfe8`](#insn-00bbbfe8) 範囲 `[['00bbbfe8', '00bbbff3']]`
  - `UNCONDITIONAL_JUMP` [`00bbbff0`](#insn-00bbbff0) → [`00bbc090`](#insn-00bbc090)
- ブロック [`00bbbff4`](#insn-00bbbff4) 範囲 `[['00bbbff4', '00bbc013']]`
  - `CONDITIONAL_JUMP` [`00bbc010`](#insn-00bbc010) → [`00bbc02c`](#insn-00bbc02c)
  - `FALL_THROUGH` [`00bbc010`](#insn-00bbc010) → [`00bbc014`](#insn-00bbc014)
- ブロック [`00bbc014`](#insn-00bbc014) 範囲 `[['00bbc014', '00bbc01f']]`
  - `CONDITIONAL_JUMP` [`00bbc01c`](#insn-00bbc01c) → [`00bbbf98`](#insn-00bbbf98)
  - `FALL_THROUGH` [`00bbc01c`](#insn-00bbc01c) → [`00bbc020`](#insn-00bbc020)
- ブロック [`00bbc020`](#insn-00bbc020) 範囲 `[['00bbc020', '00bbc02b']]`
  - `CONDITIONAL_JUMP` [`00bbc028`](#insn-00bbc028) → [`00bbbfb0`](#insn-00bbbfb0)
  - `FALL_THROUGH` [`00bbc028`](#insn-00bbc028) → [`00bbc02c`](#insn-00bbc02c)
- ブロック [`00bbc02c`](#insn-00bbc02c) 範囲 `[['00bbc02c', '00bbc04b']]`
  - `CONDITIONAL_JUMP` [`00bbc048`](#insn-00bbc048) → [`00bbc098`](#insn-00bbc098)
  - `FALL_THROUGH` [`00bbc048`](#insn-00bbc048) → [`00bbc04c`](#insn-00bbc04c)
- ブロック [`00bbc04c`](#insn-00bbc04c) 範囲 `[['00bbc04c', '00bbc04f']]`
  - `FALL_THROUGH` [`00bbc04c`](#insn-00bbc04c) → [`00bbc050`](#insn-00bbc050)
- ブロック [`00bbc050`](#insn-00bbc050) 範囲 `[['00bbc050', '00bbc05b']]`
  - `CONDITIONAL_JUMP` [`00bbc058`](#insn-00bbc058) → [`00bbc080`](#insn-00bbc080)
  - `FALL_THROUGH` [`00bbc058`](#insn-00bbc058) → [`00bbc05c`](#insn-00bbc05c)
- ブロック [`00bbc05c`](#insn-00bbc05c) 範囲 `[['00bbc05c', '00bbc067']]`
  - `CONDITIONAL_JUMP` [`00bbc064`](#insn-00bbc064) → [`00bbc080`](#insn-00bbc080)
  - `FALL_THROUGH` [`00bbc064`](#insn-00bbc064) → [`00bbc068`](#insn-00bbc068)
- ブロック [`00bbc068`](#insn-00bbc068) 範囲 `[['00bbc068', '00bbc07f']]`
  - `CONDITIONAL_JUMP` [`00bbc07c`](#insn-00bbc07c) → [`00bbc0ac`](#insn-00bbc0ac)
  - `FALL_THROUGH` [`00bbc07c`](#insn-00bbc07c) → [`00bbc080`](#insn-00bbc080)
- ブロック [`00bbc080`](#insn-00bbc080) 範囲 `[['00bbc080', '00bbc087']]`
  - `UNCONDITIONAL_JUMP` [`00bbc084`](#insn-00bbc084) → [`00bbc098`](#insn-00bbc098)
- ブロック [`00bbc088`](#insn-00bbc088) 範囲 `[['00bbc088', '00bbc08b']]`
  - `FALL_THROUGH` [`00bbc088`](#insn-00bbc088) → [`00bbc08c`](#insn-00bbc08c)
- ブロック [`00bbc08c`](#insn-00bbc08c) 範囲 `[['00bbc08c', '00bbc08f']]`
  - `FALL_THROUGH` [`00bbc08c`](#insn-00bbc08c) → [`00bbc090`](#insn-00bbc090)
- ブロック [`00bbc090`](#insn-00bbc090) 範囲 `[['00bbc090', '00bbc097']]`
  - `FALL_THROUGH` [`00bbc094`](#insn-00bbc094) → [`00bbc098`](#insn-00bbc098)
- ブロック [`00bbc098`](#insn-00bbc098) 範囲 `[['00bbc098', '00bbc0ab']]`
- ブロック [`00bbc0ac`](#insn-00bbc0ac) 範囲 `[['00bbc0ac', '00bbc0af']]`
  - `FALL_THROUGH` [`00bbc0ac`](#insn-00bbc0ac) → [`00bbc0b0`](#insn-00bbc0b0)
- ブロック [`00bbc0b0`](#insn-00bbc0b0) 範囲 `[['00bbc0b0', '00bbc0b7']]`
  - `FALL_THROUGH` [`00bbc0b4`](#insn-00bbc0b4) → [`00bbc0b8`](#insn-00bbc0b8)
- ブロック [`00bbc0b8`](#insn-00bbc0b8) 範囲 `[['00bbc0b8', '00bbc0c7']]`
  - `UNCONDITIONAL_JUMP` [`00bbc0c4`](#insn-00bbc0c4) → [`00bbc098`](#insn-00bbc098)

## 命令位置別の参照

- [`00bbbf60`](#insn-00bbbf60) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf64`](#insn-00bbbf64) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf68`](#insn-00bbbf68) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf7c`](#insn-00bbbf7c) → `00c1c010`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbf84`](#insn-00bbbf84) → [`00bbbfb8`](#insn-00bbbfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf94`](#insn-00bbbf94) → [`00bbbff4`](#insn-00bbbff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbf9c`](#insn-00bbbf9c) → [`00bbbfb0`](#insn-00bbbfb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfa8`](#insn-00bbbfa8) → [`00bde980`](../00bde/00bde980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde980` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfac`](#insn-00bbbfac) → [`00bbc02c`](#insn-00bbc02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfb4`](#insn-00bbbfb4) → [`00bbc098`](#insn-00bbc098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfbc`](#insn-00bbbfbc) → [`00bbc088`](#insn-00bbc088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfcc`](#insn-00bbbfcc) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbfcc`](#insn-00bbbfcc) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbfd0`](#insn-00bbbfd0) → `00c1c028`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbfd8`](#insn-00bbbfd8) → `00c16c20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv120__function_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbfdc`](#insn-00bbbfdc) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbfe4`](#insn-00bbbfe4) → [`00bbc088`](#insn-00bbc088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbff0`](#insn-00bbbff0) → [`00bbc090`](#insn-00bbc090) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc000`](#insn-00bbc000) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc000`](#insn-00bbc000) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbc004`](#insn-00bbc004) → `00c1c008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc004`](#insn-00bbc004) → `00c16bf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv117__pbase_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbc00c`](#insn-00bbc00c) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbc010`](#insn-00bbc010) → [`00bbc02c`](#insn-00bbc02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc01c`](#insn-00bbc01c) → [`00bbbf98`](#insn-00bbbf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc028`](#insn-00bbc028) → [`00bbbfb0`](#insn-00bbbfb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc038`](#insn-00bbc038) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc038`](#insn-00bbc038) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbc03c`](#insn-00bbc03c) → `00c1c030`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbc03c`](#insn-00bbc03c) → `00c16c38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv129__pointer_to_member_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbc044`](#insn-00bbc044) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbc048`](#insn-00bbc048) → [`00bbc098`](#insn-00bbc098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc058`](#insn-00bbc058) → [`00bbc080`](#insn-00bbc080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc064`](#insn-00bbc064) → [`00bbc080`](#insn-00bbc080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc07c`](#insn-00bbc07c) → [`00bbc0ac`](#insn-00bbc0ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc084`](#insn-00bbc084) → [`00bbc098`](#insn-00bbc098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc090`](#insn-00bbc090) → `002fc9a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc090`](#insn-00bbc090) → `002fc9b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc098`](#insn-00bbc098) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc09c`](#insn-00bbc09c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0a0`](#insn-00bbc0a0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbc0c4`](#insn-00bbc0c4) → [`00bbc098`](#insn-00bbc098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbf60`](#insn-00bbbf60)

~~~json
{
  "source": "00bbbf60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf64`](#insn-00bbbf64)

~~~json
{
  "source": "00bbbf64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf68`](#insn-00bbbf68)

~~~json
{
  "source": "00bbbf68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf7c`](#insn-00bbbf7c)

~~~json
{
  "source": "00bbbf7c",
  "target": "00c1c010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c010",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbf84`](#insn-00bbbf84)

~~~json
{
  "source": "00bbbf84",
  "target": "00bbbfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf94`](#insn-00bbbf94)

~~~json
{
  "source": "00bbbf94",
  "target": "00bbbff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbf9c`](#insn-00bbbf9c)

~~~json
{
  "source": "00bbbf9c",
  "target": "00bbbfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfa8`](#insn-00bbbfa8)

~~~json
{
  "source": "00bbbfa8",
  "target": "00bde980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbfac`](#insn-00bbbfac)

~~~json
{
  "source": "00bbbfac",
  "target": "00bbc02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfb4`](#insn-00bbbfb4)

~~~json
{
  "source": "00bbbfb4",
  "target": "00bbc098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfbc`](#insn-00bbbfbc)

~~~json
{
  "source": "00bbbfbc",
  "target": "00bbc088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbfcc`](#insn-00bbbfcc)

~~~json
{
  "source": "00bbbfcc",
  "target": "00c1bff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bff8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbfcc`](#insn-00bbbfcc)

~~~json
{
  "source": "00bbbfcc",
  "target": "00c16bc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16bc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbfd0`](#insn-00bbbfd0)

~~~json
{
  "source": "00bbbfd0",
  "target": "00c1c028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c028",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbfd8`](#insn-00bbbfd8)

~~~json
{
  "source": "00bbbfd8",
  "target": "00c16c20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c20",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbfdc`](#insn-00bbbfdc)

~~~json
{
  "source": "00bbbfdc",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbfe4`](#insn-00bbbfe4)

~~~json
{
  "source": "00bbbfe4",
  "target": "00bbc088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbff0`](#insn-00bbbff0)

~~~json
{
  "source": "00bbbff0",
  "target": "00bbc090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc000`](#insn-00bbc000)

~~~json
{
  "source": "00bbc000",
  "target": "00c1bff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bff8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc000`](#insn-00bbc000)

~~~json
{
  "source": "00bbc000",
  "target": "00c16bc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16bc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc004`](#insn-00bbc004)

~~~json
{
  "source": "00bbc004",
  "target": "00c1c008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c008",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc004`](#insn-00bbc004)

~~~json
{
  "source": "00bbc004",
  "target": "00c16bf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16bf0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc00c`](#insn-00bbc00c)

~~~json
{
  "source": "00bbc00c",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc010`](#insn-00bbc010)

~~~json
{
  "source": "00bbc010",
  "target": "00bbc02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc01c`](#insn-00bbc01c)

~~~json
{
  "source": "00bbc01c",
  "target": "00bbbf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc028`](#insn-00bbc028)

~~~json
{
  "source": "00bbc028",
  "target": "00bbbfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc038`](#insn-00bbc038)

~~~json
{
  "source": "00bbc038",
  "target": "00c1bff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bff8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc038`](#insn-00bbc038)

~~~json
{
  "source": "00bbc038",
  "target": "00c16bc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16bc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc03c`](#insn-00bbc03c)

~~~json
{
  "source": "00bbc03c",
  "target": "00c1c030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c030",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc03c`](#insn-00bbc03c)

~~~json
{
  "source": "00bbc03c",
  "target": "00c16c38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c38",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbc044`](#insn-00bbc044)

~~~json
{
  "source": "00bbc044",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbc048`](#insn-00bbc048)

~~~json
{
  "source": "00bbc048",
  "target": "00bbc098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc058`](#insn-00bbc058)

~~~json
{
  "source": "00bbc058",
  "target": "00bbc080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc064`](#insn-00bbc064)

~~~json
{
  "source": "00bbc064",
  "target": "00bbc080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc07c`](#insn-00bbc07c)

~~~json
{
  "source": "00bbc07c",
  "target": "00bbc0ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc084`](#insn-00bbc084)

~~~json
{
  "source": "00bbc084",
  "target": "00bbc098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc090`](#insn-00bbc090)

~~~json
{
  "source": "00bbc090",
  "target": "002fc9a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc090`](#insn-00bbc090)

~~~json
{
  "source": "00bbc090",
  "target": "002fc9b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc098`](#insn-00bbc098)

~~~json
{
  "source": "00bbc098",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc09c`](#insn-00bbc09c)

~~~json
{
  "source": "00bbc09c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0a0`](#insn-00bbc0a0)

~~~json
{
  "source": "00bbc0a0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbc0c4`](#insn-00bbc0c4)

~~~json
{
  "source": "00bbc0c4",
  "target": "00bbc098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
