# 00bbbb0c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bbba44`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbb/00bbba44.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0078.md#compare-b4b13ef3ad9be33b818a26b28480e86a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bbbb50`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bbb/00bbbb50.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-6d380dba5f2f6f8b34a63efad70b2c83)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbbb0c",
  "name": "FUN_00bbbb0c",
  "size": 700,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "285d19dabedd3e61683e0f0dba2e7a2cb2e5dcacb240e2b33eb5cda88e22b1fb",
  "source_text_sha256": "285d19dabedd3e61683e0f0dba2e7a2cb2e5dcacb240e2b33eb5cda88e22b1fb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbbb0c",
        "00bbbdc7"
      ]
    ],
    "bytes_sha256": "b5ad94e8713cfa2726b804789d4389733d1267288e97cb60712c2a7ee0a5693d",
    "instruction_count": 175,
    "instruction_bytes": 700,
    "body_bytes": 700,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbbdc8](../00bbb/00bbbdc8.md)
- [00bbbebc](../00bbb/00bbbebc.md)
- [00bdb770](../00bdb/00bdb770.md)
- [00bde980](../00bde/00bde980.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5197 bytes

~~~c

ulong FUN_00bbbb0c(long param_1,long param_2,long *param_3)

{
  uint uVar1;
  int iVar2;
  long lVar3;
  long lVar4;
  ulong uVar5;
  long lVar6;
  char *__s2;
  long lVar7;
  long *local_98;
  undefined8 uStack_90;
  long local_88;
  undefined8 uStack_80;
  long local_78;
  undefined8 uStack_70;
  undefined8 local_68;
  undefined7 uStack_60;
  undefined1 local_59;
  undefined7 uStack_58;
  undefined8 uStack_51;
  undefined1 local_49;
  undefined8 local_48;
  
  __s2 = *(char **)(param_2 + 8);
  if (__s2 == PTR__ZTSDn_00c1c010) {
    *param_3 = 0;
    return 1;
  }
  uVar1 = *(uint *)(param_1 + 0x10);
  if ((uVar1 & 0x18) == 0) {
                    /* try { // try from 00bbbba4 to 00cbbbaf has its CatchHandler @ 00bbd21c */
    lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                           PTR__ZTIN10__cxxabiv117__pbase_type_infoE_00c1c008,0);
    if (lVar3 == 0) goto LAB_00bbbbc8;
                    /* try { // try from 00bbbbb0 to 00cbbbbf has its CatchHandler @ 00bbd208 */
    if ((*(byte *)(lVar3 + 0x10) & 0x18) == 0) {
                    /* try { // try from 00bbbbc0 to 00cbbbd3 has its CatchHandler @ 00bbd1f0 */
      if (*(char **)(param_1 + 8) != __s2) goto LAB_00bbbbc8;
      goto LAB_00bbbb6c;
    }
  }
                    /* try { // try from 00bbbb54 to 00cbbb5b has its CatchHandler @ 00bbd2e8 */
                    /* try { // try from 00bbbb5c to 00cbbb63 has its CatchHandler @ 00bbd220 */
  if ((param_1 == param_2) || (iVar2 = strcmp(*(char **)(param_1 + 8),__s2), iVar2 == 0)) {
LAB_00bbbb6c:
    if ((long *)*param_3 == (long *)0x0) {
      return 1;
    }
    *param_3 = *(long *)*param_3;
    return 1;
  }
LAB_00bbbbc8:
  lVar3 = __dynamic_cast(param_2,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                         PTR__ZTIN10__cxxabiv119__pointer_type_infoE_00c1c018,0);
  if (lVar3 == 0) {
    return 0;
  }
  if ((long *)*param_3 == (long *)0x0) {
    lVar6 = 0;
  }
  else {
    lVar6 = *(long *)*param_3;
    *param_3 = lVar6;
  }
  if (((*(uint *)(lVar3 + 0x10) & (uVar1 ^ 0xffffffff) & 7) == 0) &&
     ((uVar1 & (*(uint *)(lVar3 + 0x10) ^ 0xffffffff) & 0x60) == 0)) {
    lVar7 = *(long *)(param_1 + 0x18);
    lVar3 = *(long *)(lVar3 + 0x18);
    if (*(undefined **)(lVar7 + 8) == *(undefined **)(lVar3 + 8)) {
                    /* try { // try from 00bbbc94 to 00cbbca3 has its CatchHandler @ 00bbd3ec */
      return 1;
    }
    if (*(undefined **)(lVar7 + 8) == PTR__ZTSv_00c1c020) {
                    /* try { // try from 00bbbcb8 to 00cbbcbf has its CatchHandler @ 00bbd2e8 */
                    /* try { // try from 00bbbcc0 to 00cbbcc7 has its CatchHandler @ 00bbd1ec */
      lVar3 = __dynamic_cast(lVar3,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                             PTR__ZTIN10__cxxabiv120__function_type_infoE_00c1c028,0);
      return (ulong)(lVar3 == 0);
    }
                    /* try { // try from 00bbbc5c to 00cbbc67 has its CatchHandler @ 00bbd388 */
    lVar4 = __dynamic_cast(lVar7,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                           PTR__ZTIN10__cxxabiv119__pointer_type_infoE_00c1c018,0);
    if (lVar4 == 0) {
      lVar4 = __dynamic_cast(lVar7,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                             PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c030,0);
      if (lVar4 == 0) {
                    /* try { // try from 00bbbd20 to 00cbbd33 has its CatchHandler @ 00bbd1bc */
        local_88 = __dynamic_cast(lVar7,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                                  PTR__ZTIN10__cxxabiv117__class_type_infoE_00c1c000,0);
        if (local_88 == 0) {
          return 0;
        }
        local_98 = (long *)__dynamic_cast(lVar3,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                                          PTR__ZTIN10__cxxabiv117__class_type_infoE_00c1c000,0);
        if (local_98 != (long *)0x0) {
          local_49 = lVar6 != 0;
          local_48 = 0;
                    /* try { // try from 00bbbd6c to 00cbbd77 has its CatchHandler @ 00bbd2e8 */
                    /* try { // try from 00bbbd78 to 00cbbe53 has its CatchHandler @ 00bbd29c */
          uStack_90 = 0;
          uStack_58 = 0;
          uStack_70 = 0;
          local_78 = 0;
          uStack_60 = 0;
          local_59 = 0;
          local_68 = 0;
          uStack_51 = 0x100;
          uStack_80 = 0xffffffffffffffff;
          (**(code **)(*local_98 + 0x38))(local_98,&local_98,lVar6,1);
          if ((int)local_68 == 1) {
            if (lVar6 == 0) {
              local_78 = 0;
            }
            *param_3 = local_78;
            return 1;
          }
          return 0;
        }
        return 0;
      }
      if ((uVar1 & 1) != 0) {
                    /* try { // try from 00bbbd04 to 00cbbd0f has its CatchHandler @ 00bbd1e8 */
                    /* try { // try from 00bbbd10 to 00cbbd1f has its CatchHandler @ 00bbd1d4 */
        uVar5 = FUN_00bbbebc(lVar4,lVar3);
        return uVar5;
      }
    }
    else if ((uVar1 & 1) != 0) {
      uVar5 = FUN_00bbbdc8(lVar4,lVar3);
      return uVar5;
    }
  }
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbbb0c"></a> `00bbbb0c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbbb10"></a> `00bbbb10` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbbb14"></a> `00bbbb14` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbbb18"></a> `00bbbb18` | `f7 3b 00 f9` | str x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbbb1c"></a> `00bbbb1c` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbbb20"></a> `00bbbb20` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbbb24"></a> `00bbbb24` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bbbb28"></a> `00bbbb28` | `08 03 00 b0` | adrp x8,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbb2c"></a> `00bbbb2c` | `36 04 40 f9` | ldr x22,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbb30"></a> `00bbbb30` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bbbb34"></a> `00bbbb34` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbb38"></a> `00bbbb38` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bbbb3c"></a> `00bbbb3c` | `40 02 00 54` | b.eq 0x00bbbb84 | `CONDITIONAL_JUMP`
<a id="insn-00bbbb40"></a> `00bbbb40` | `17 10 40 b9` | ldr w23,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbb44"></a> `00bbbb44` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bbbb48"></a> `00bbbb48` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbbb4c"></a> `00bbbb4c` | `ff 06 1d 72` | tst w23,#0x18 | `FALL_THROUGH`
<a id="insn-00bbbb50"></a> `00bbbb50` | `00 02 00 54` | b.eq 0x00bbbb90 | `CONDITIONAL_JUMP`
<a id="insn-00bbbb54"></a> `00bbbb54` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00bbbb58"></a> `00bbbb58` | `a0 00 00 54` | b.eq 0x00bbbb6c | `CONDITIONAL_JUMP`
<a id="insn-00bbbb5c"></a> `00bbbb5c` | `a0 06 40 f9` | ldr x0,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbb60"></a> `00bbbb60` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbbb64"></a> `00bbbb64` | `87 8b 00 94` | bl 0x00bde980 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbb68"></a> `00bbbb68` | `00 03 00 35` | cbnz w0,0x00bbbbc8 | `CONDITIONAL_JUMP`
<a id="insn-00bbbb6c"></a> `00bbbb6c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbb70"></a> `00bbbb70` | `08 09 00 b4` | cbz x8,0x00bbbc90 | `CONDITIONAL_JUMP`
<a id="insn-00bbbb74"></a> `00bbbb74` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bbbb78"></a> `00bbbb78` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbb7c"></a> `00bbbb7c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbb80"></a> `00bbbb80` | `45 00 00 14` | b 0x00bbbc94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbb84"></a> `00bbbb84` | `7f 02 00 f9` | str xzr,[x19] | `FALL_THROUGH`
<a id="insn-00bbbb88"></a> `00bbbb88` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbb8c"></a> `00bbbb8c` | `42 00 00 14` | b 0x00bbbc94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbb90"></a> `00bbbb90` | `01 03 00 90` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbb94"></a> `00bbbb94` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbb98"></a> `00bbbb98` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbbb9c"></a> `00bbbb9c` | `21 fc 47 f9` | ldr x1,[x1, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbbba0"></a> `00bbbba0` | `42 04 40 f9` | ldr x2,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbba4"></a> `00bbbba4` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbba8"></a> `00bbbba8` | `f2 7e 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbbac"></a> `00bbbbac` | `e0 00 00 b4` | cbz x0,0x00bbbbc8 | `CONDITIONAL_JUMP`
<a id="insn-00bbbbb0"></a> `00bbbbb0` | `08 40 40 39` | ldrb w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbbb4"></a> `00bbbbb4` | `1f 05 1d 72` | tst w8,#0x18 | `FALL_THROUGH`
<a id="insn-00bbbbb8"></a> `00bbbbb8` | `e1 fc ff 54` | b.ne 0x00bbbb54 | `CONDITIONAL_JUMP`
<a id="insn-00bbbbbc"></a> `00bbbbbc` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbbc0"></a> `00bbbbc0` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bbbbc4"></a> `00bbbbc4` | `40 fd ff 54` | b.eq 0x00bbbb6c | `CONDITIONAL_JUMP`
<a id="insn-00bbbbc8"></a> `00bbbbc8` | `01 03 00 90` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbbcc"></a> `00bbbbcc` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbbd0"></a> `00bbbbd0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbbbd4"></a> `00bbbbd4` | `21 fc 47 f9` | ldr x1,[x1, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbbbd8"></a> `00bbbbd8` | `42 0c 40 f9` | ldr x2,[x2, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbbdc"></a> `00bbbbdc` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbbe0"></a> `00bbbbe0` | `e4 7e 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbbe4"></a> `00bbbbe4` | `80 05 00 b4` | cbz x0,0x00bbbc94 | `CONDITIONAL_JUMP`
<a id="insn-00bbbbe8"></a> `00bbbbe8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbbec"></a> `00bbbbec` | `88 00 00 b4` | cbz x8,0x00bbbbfc | `CONDITIONAL_JUMP`
<a id="insn-00bbbbf0"></a> `00bbbbf0` | `14 01 40 f9` | ldr x20,[x8] | `FALL_THROUGH`
<a id="insn-00bbbbf4"></a> `00bbbbf4` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bbbbf8"></a> `00bbbbf8` | `02 00 00 14` | b 0x00bbbc00 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbbfc"></a> `00bbbbfc` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00bbbc00"></a> `00bbbc00` | `08 10 40 b9` | ldr w8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbbc04"></a> `00bbbc04` | `09 01 37 0a` | bic w9,w8,w23 | `FALL_THROUGH`
<a id="insn-00bbbc08"></a> `00bbbc08` | `3f 09 00 72` | tst w9,#0x7 | `FALL_THROUGH`
<a id="insn-00bbbc0c"></a> `00bbbc0c` | `81 00 00 54` | b.ne 0x00bbbc1c | `CONDITIONAL_JUMP`
<a id="insn-00bbbc10"></a> `00bbbc10` | `e8 02 28 0a` | bic w8,w23,w8 | `FALL_THROUGH`
<a id="insn-00bbbc14"></a> `00bbbc14` | `1f 05 1b 72` | tst w8,#0x60 | `FALL_THROUGH`
<a id="insn-00bbbc18"></a> `00bbbc18` | `60 00 00 54` | b.eq 0x00bbbc24 | `CONDITIONAL_JUMP`
<a id="insn-00bbbc1c"></a> `00bbbc1c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bbbc20"></a> `00bbbc20` | `1d 00 00 14` | b 0x00bbbc94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbc24"></a> `00bbbc24` | `b6 0e 40 f9` | ldr x22,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbc28"></a> `00bbbc28` | `15 0c 40 f9` | ldr x21,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbc2c"></a> `00bbbc2c` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbc30"></a> `00bbbc30` | `a9 06 40 f9` | ldr x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbc34"></a> `00bbbc34` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbbc38"></a> `00bbbc38` | `c0 02 00 54` | b.eq 0x00bbbc90 | `CONDITIONAL_JUMP`
<a id="insn-00bbbc3c"></a> `00bbbc3c` | `09 03 00 b0` | adrp x9,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbc40"></a> `00bbbc40` | `01 03 00 90` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbc44"></a> `00bbbc44` | `29 11 40 f9` | ldr x9,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bbbc48"></a> `00bbbc48` | `21 fc 47 f9` | ldr x1,[x1, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbbc4c"></a> `00bbbc4c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbbc50"></a> `00bbbc50` | `00 03 00 54` | b.eq 0x00bbbcb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbbc54"></a> `00bbbc54` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbc58"></a> `00bbbc58` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbbc5c"></a> `00bbbc5c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbc60"></a> `00bbbc60` | `42 0c 40 f9` | ldr x2,[x2, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbc64"></a> `00bbbc64` | `c3 7e 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbc68"></a> `00bbbc68` | `40 03 00 b4` | cbz x0,0x00bbbcd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbbc6c"></a> `00bbbc6c` | `97 fd 07 36` | tbz w23,#0x0,0x00bbbc1c | `CONDITIONAL_JUMP`
<a id="insn-00bbbc70"></a> `00bbbc70` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbbc74"></a> `00bbbc74` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbbc78"></a> `00bbbc78` | `f7 3b 40 f9` | ldr x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbbc7c"></a> `00bbbc7c` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbbc80"></a> `00bbbc80` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbbc84"></a> `00bbbc84` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbbc88"></a> `00bbbc88` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbbc8c"></a> `00bbbc8c` | `4f 00 00 14` | b 0x00bbbdc8 | `CALL_TERMINATOR`
<a id="insn-00bbbc90"></a> `00bbbc90` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbc94"></a> `00bbbc94` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbbc98"></a> `00bbbc98` | `f7 3b 40 f9` | ldr x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbbc9c"></a> `00bbbc9c` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbbca0"></a> `00bbbca0` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbbca4"></a> `00bbbca4` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbbca8"></a> `00bbbca8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbbcac"></a> `00bbbcac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbbcb0"></a> `00bbbcb0` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbcb4"></a> `00bbbcb4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbbcb8"></a> `00bbbcb8` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbcbc"></a> `00bbbcbc` | `42 14 40 f9` | ldr x2,[x2, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbcc0"></a> `00bbbcc0` | `ac 7e 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbcc4"></a> `00bbbcc4` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00bbbcc8"></a> `00bbbcc8` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bbbccc"></a> `00bbbccc` | `f2 ff ff 17` | b 0x00bbbc94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbbcd0"></a> `00bbbcd0` | `01 03 00 90` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbcd4"></a> `00bbbcd4` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbcd8"></a> `00bbbcd8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbbcdc"></a> `00bbbcdc` | `21 fc 47 f9` | ldr x1,[x1, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbbce0"></a> `00bbbce0` | `42 18 40 f9` | ldr x2,[x2, #0x30] | `FALL_THROUGH`
<a id="insn-00bbbce4"></a> `00bbbce4` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbce8"></a> `00bbbce8` | `a2 7e 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbcec"></a> `00bbbcec` | `40 01 00 b4` | cbz x0,0x00bbbd14 | `CONDITIONAL_JUMP`
<a id="insn-00bbbcf0"></a> `00bbbcf0` | `77 f9 07 36` | tbz w23,#0x0,0x00bbbc1c | `CONDITIONAL_JUMP`
<a id="insn-00bbbcf4"></a> `00bbbcf4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbbcf8"></a> `00bbbcf8` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbbcfc"></a> `00bbbcfc` | `f7 3b 40 f9` | ldr x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbbd00"></a> `00bbbd00` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbbd04"></a> `00bbbd04` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbbd08"></a> `00bbbd08` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbbd0c"></a> `00bbbd0c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbbd10"></a> `00bbbd10` | `6b 00 00 14` | b 0x00bbbebc | `CALL_TERMINATOR`
<a id="insn-00bbbd14"></a> `00bbbd14` | `01 03 00 90` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbd18"></a> `00bbbd18` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbd1c"></a> `00bbbd1c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbbd20"></a> `00bbbd20` | `21 fc 47 f9` | ldr x1,[x1, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbbd24"></a> `00bbbd24` | `42 00 40 f9` | ldr x2,[x2] | `FALL_THROUGH`
<a id="insn-00bbbd28"></a> `00bbbd28` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbd2c"></a> `00bbbd2c` | `91 7e 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd30"></a> `00bbbd30` | `20 fb ff b4` | cbz x0,0x00bbbc94 | `CONDITIONAL_JUMP`
<a id="insn-00bbbd34"></a> `00bbbd34` | `01 03 00 90` | adrp x1,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbbd38"></a> `00bbbd38` | `02 03 00 b0` | adrp x2,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bbbd3c"></a> `00bbbd3c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbbd40"></a> `00bbbd40` | `21 fc 47 f9` | ldr x1,[x1, #0xff8] | `FALL_THROUGH`
<a id="insn-00bbbd44"></a> `00bbbd44` | `42 00 40 f9` | ldr x2,[x2] | `FALL_THROUGH`
<a id="insn-00bbbd48"></a> `00bbbd48` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbbd4c"></a> `00bbbd4c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbbd50"></a> `00bbbd50` | `88 7e 00 94` | bl 0x00bdb770 | `UNCONDITIONAL_CALL`
<a id="insn-00bbbd54"></a> `00bbbd54` | `00 fa ff b4` | cbz x0,0x00bbbc94 | `CONDITIONAL_JUMP`
<a id="insn-00bbbd58"></a> `00bbbd58` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bbbd5c"></a> `00bbbd5c` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00bbbd60"></a> `00bbbd60` | `ff 2f 00 f9` | str xzr,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bbbd64"></a> `00bbbd64` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00bbbd68"></a> `00bbbd68` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbbd6c"></a> `00bbbd6c` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bbbd70"></a> `00bbbd70` | `e8 5f 01 39` | strb w8,[sp, #0x57] | `FALL_THROUGH`
<a id="insn-00bbbd74"></a> `00bbbd74` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbd78"></a> `00bbbd78` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbd7c"></a> `00bbbd7c` | `e0 ff 00 a9` | stp x0,xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbbd80"></a> `00bbbd80` | `e0 73 84 3c` | stur q0,[sp, #0x47] | `FALL_THROUGH`
<a id="insn-00bbbd84"></a> `00bbbd84` | `e0 83 82 3c` | stur q0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbd88"></a> `00bbbd88` | `e0 83 83 3c` | stur q0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbbd8c"></a> `00bbbd8c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bbbd90"></a> `00bbbd90` | `e8 53 00 b9` | str w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbbd94"></a> `00bbbd94` | `08 00 80 92` | mov x8,#-0x1 | `FALL_THROUGH`
<a id="insn-00bbbd98"></a> `00bbbd98` | `f6 a3 01 a9` | stp x22,x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbbd9c"></a> `00bbbd9c` | `29 1d 40 f9` | ldr x9,[x9, #0x38] | `FALL_THROUGH`
<a id="insn-00bbbda0"></a> `00bbbda0` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bbbda4"></a> `00bbbda4` | `e8 3b 40 b9` | ldr w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbbda8"></a> `00bbbda8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbbdac"></a> `00bbbdac` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bbbdb0"></a> `00bbbdb0` | `21 f7 ff 54` | b.ne 0x00bbbc94 | `CONDITIONAL_JUMP`
<a id="insn-00bbbdb4"></a> `00bbbdb4` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbbdb8"></a> `00bbbdb8` | `9f 02 00 f1` | cmp x20,#0x0 | `FALL_THROUGH`
<a id="insn-00bbbdbc"></a> `00bbbdbc` | `08 11 9f 9a` | csel x8,x8,xzr,ne | `FALL_THROUGH`
<a id="insn-00bbbdc0"></a> `00bbbdc0` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbbdc4"></a> `00bbbdc4` | `b4 ff ff 17` | b 0x00bbbc94 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bbbb0c`](#insn-00bbbb0c) 範囲 `[['00bbbb0c', '00bbbb3f']]`
  - `CONDITIONAL_JUMP` [`00bbbb3c`](#insn-00bbbb3c) → [`00bbbb84`](#insn-00bbbb84)
  - `FALL_THROUGH` [`00bbbb3c`](#insn-00bbbb3c) → [`00bbbb40`](#insn-00bbbb40)
- ブロック [`00bbbb40`](#insn-00bbbb40) 範囲 `[['00bbbb40', '00bbbb53']]`
  - `CONDITIONAL_JUMP` [`00bbbb50`](#insn-00bbbb50) → [`00bbbb90`](#insn-00bbbb90)
  - `FALL_THROUGH` [`00bbbb50`](#insn-00bbbb50) → [`00bbbb54`](#insn-00bbbb54)
- ブロック [`00bbbb54`](#insn-00bbbb54) 範囲 `[['00bbbb54', '00bbbb5b']]`
  - `CONDITIONAL_JUMP` [`00bbbb58`](#insn-00bbbb58) → [`00bbbb6c`](#insn-00bbbb6c)
  - `FALL_THROUGH` [`00bbbb58`](#insn-00bbbb58) → [`00bbbb5c`](#insn-00bbbb5c)
- ブロック [`00bbbb5c`](#insn-00bbbb5c) 範囲 `[['00bbbb5c', '00bbbb6b']]`
  - `CONDITIONAL_JUMP` [`00bbbb68`](#insn-00bbbb68) → [`00bbbbc8`](#insn-00bbbbc8)
  - `FALL_THROUGH` [`00bbbb68`](#insn-00bbbb68) → [`00bbbb6c`](#insn-00bbbb6c)
- ブロック [`00bbbb6c`](#insn-00bbbb6c) 範囲 `[['00bbbb6c', '00bbbb73']]`
  - `CONDITIONAL_JUMP` [`00bbbb70`](#insn-00bbbb70) → [`00bbbc90`](#insn-00bbbc90)
  - `FALL_THROUGH` [`00bbbb70`](#insn-00bbbb70) → [`00bbbb74`](#insn-00bbbb74)
- ブロック [`00bbbb74`](#insn-00bbbb74) 範囲 `[['00bbbb74', '00bbbb83']]`
  - `UNCONDITIONAL_JUMP` [`00bbbb80`](#insn-00bbbb80) → [`00bbbc94`](#insn-00bbbc94)
- ブロック [`00bbbb84`](#insn-00bbbb84) 範囲 `[['00bbbb84', '00bbbb8f']]`
  - `UNCONDITIONAL_JUMP` [`00bbbb8c`](#insn-00bbbb8c) → [`00bbbc94`](#insn-00bbbc94)
- ブロック [`00bbbb90`](#insn-00bbbb90) 範囲 `[['00bbbb90', '00bbbba3']]`
  - `FALL_THROUGH` [`00bbbba0`](#insn-00bbbba0) → [`00bbbba4`](#insn-00bbbba4)
- ブロック [`00bbbba4`](#insn-00bbbba4) 範囲 `[['00bbbba4', '00bbbbaf']]`
  - `CONDITIONAL_JUMP` [`00bbbbac`](#insn-00bbbbac) → [`00bbbbc8`](#insn-00bbbbc8)
  - `FALL_THROUGH` [`00bbbbac`](#insn-00bbbbac) → [`00bbbbb0`](#insn-00bbbbb0)
- ブロック [`00bbbbb0`](#insn-00bbbbb0) 範囲 `[['00bbbbb0', '00bbbbbb']]`
  - `CONDITIONAL_JUMP` [`00bbbbb8`](#insn-00bbbbb8) → [`00bbbb54`](#insn-00bbbb54)
  - `FALL_THROUGH` [`00bbbbb8`](#insn-00bbbbb8) → [`00bbbbbc`](#insn-00bbbbbc)
- ブロック [`00bbbbbc`](#insn-00bbbbbc) 範囲 `[['00bbbbbc', '00bbbbbf']]`
  - `FALL_THROUGH` [`00bbbbbc`](#insn-00bbbbbc) → [`00bbbbc0`](#insn-00bbbbc0)
- ブロック [`00bbbbc0`](#insn-00bbbbc0) 範囲 `[['00bbbbc0', '00bbbbc7']]`
  - `CONDITIONAL_JUMP` [`00bbbbc4`](#insn-00bbbbc4) → [`00bbbb6c`](#insn-00bbbb6c)
  - `FALL_THROUGH` [`00bbbbc4`](#insn-00bbbbc4) → [`00bbbbc8`](#insn-00bbbbc8)
- ブロック [`00bbbbc8`](#insn-00bbbbc8) 範囲 `[['00bbbbc8', '00bbbbe7']]`
  - `CONDITIONAL_JUMP` [`00bbbbe4`](#insn-00bbbbe4) → [`00bbbc94`](#insn-00bbbc94)
  - `FALL_THROUGH` [`00bbbbe4`](#insn-00bbbbe4) → [`00bbbbe8`](#insn-00bbbbe8)
- ブロック [`00bbbbe8`](#insn-00bbbbe8) 範囲 `[['00bbbbe8', '00bbbbef']]`
  - `CONDITIONAL_JUMP` [`00bbbbec`](#insn-00bbbbec) → [`00bbbbfc`](#insn-00bbbbfc)
  - `FALL_THROUGH` [`00bbbbec`](#insn-00bbbbec) → [`00bbbbf0`](#insn-00bbbbf0)
- ブロック [`00bbbbf0`](#insn-00bbbbf0) 範囲 `[['00bbbbf0', '00bbbbfb']]`
  - `UNCONDITIONAL_JUMP` [`00bbbbf8`](#insn-00bbbbf8) → [`00bbbc00`](#insn-00bbbc00)
- ブロック [`00bbbbfc`](#insn-00bbbbfc) 範囲 `[['00bbbbfc', '00bbbbff']]`
  - `FALL_THROUGH` [`00bbbbfc`](#insn-00bbbbfc) → [`00bbbc00`](#insn-00bbbc00)
- ブロック [`00bbbc00`](#insn-00bbbc00) 範囲 `[['00bbbc00', '00bbbc0f']]`
  - `CONDITIONAL_JUMP` [`00bbbc0c`](#insn-00bbbc0c) → [`00bbbc1c`](#insn-00bbbc1c)
  - `FALL_THROUGH` [`00bbbc0c`](#insn-00bbbc0c) → [`00bbbc10`](#insn-00bbbc10)
- ブロック [`00bbbc10`](#insn-00bbbc10) 範囲 `[['00bbbc10', '00bbbc1b']]`
  - `CONDITIONAL_JUMP` [`00bbbc18`](#insn-00bbbc18) → [`00bbbc24`](#insn-00bbbc24)
  - `FALL_THROUGH` [`00bbbc18`](#insn-00bbbc18) → [`00bbbc1c`](#insn-00bbbc1c)
- ブロック [`00bbbc1c`](#insn-00bbbc1c) 範囲 `[['00bbbc1c', '00bbbc23']]`
  - `UNCONDITIONAL_JUMP` [`00bbbc20`](#insn-00bbbc20) → [`00bbbc94`](#insn-00bbbc94)
- ブロック [`00bbbc24`](#insn-00bbbc24) 範囲 `[['00bbbc24', '00bbbc3b']]`
  - `CONDITIONAL_JUMP` [`00bbbc38`](#insn-00bbbc38) → [`00bbbc90`](#insn-00bbbc90)
  - `FALL_THROUGH` [`00bbbc38`](#insn-00bbbc38) → [`00bbbc3c`](#insn-00bbbc3c)
- ブロック [`00bbbc3c`](#insn-00bbbc3c) 範囲 `[['00bbbc3c', '00bbbc53']]`
  - `CONDITIONAL_JUMP` [`00bbbc50`](#insn-00bbbc50) → [`00bbbcb0`](#insn-00bbbcb0)
  - `FALL_THROUGH` [`00bbbc50`](#insn-00bbbc50) → [`00bbbc54`](#insn-00bbbc54)
- ブロック [`00bbbc54`](#insn-00bbbc54) 範囲 `[['00bbbc54', '00bbbc5b']]`
  - `FALL_THROUGH` [`00bbbc58`](#insn-00bbbc58) → [`00bbbc5c`](#insn-00bbbc5c)
- ブロック [`00bbbc5c`](#insn-00bbbc5c) 範囲 `[['00bbbc5c', '00bbbc6b']]`
  - `CONDITIONAL_JUMP` [`00bbbc68`](#insn-00bbbc68) → [`00bbbcd0`](#insn-00bbbcd0)
  - `FALL_THROUGH` [`00bbbc68`](#insn-00bbbc68) → [`00bbbc6c`](#insn-00bbbc6c)
- ブロック [`00bbbc6c`](#insn-00bbbc6c) 範囲 `[['00bbbc6c', '00bbbc6f']]`
  - `CONDITIONAL_JUMP` [`00bbbc6c`](#insn-00bbbc6c) → [`00bbbc1c`](#insn-00bbbc1c)
  - `FALL_THROUGH` [`00bbbc6c`](#insn-00bbbc6c) → [`00bbbc70`](#insn-00bbbc70)
- ブロック [`00bbbc70`](#insn-00bbbc70) 範囲 `[['00bbbc70', '00bbbc8f']]`
- ブロック [`00bbbc90`](#insn-00bbbc90) 範囲 `[['00bbbc90', '00bbbc93']]`
  - `FALL_THROUGH` [`00bbbc90`](#insn-00bbbc90) → [`00bbbc94`](#insn-00bbbc94)
- ブロック [`00bbbc94`](#insn-00bbbc94) 範囲 `[['00bbbc94', '00bbbcaf']]`
- ブロック [`00bbbcb0`](#insn-00bbbcb0) 範囲 `[['00bbbcb0', '00bbbcb7']]`
  - `FALL_THROUGH` [`00bbbcb4`](#insn-00bbbcb4) → [`00bbbcb8`](#insn-00bbbcb8)
- ブロック [`00bbbcb8`](#insn-00bbbcb8) 範囲 `[['00bbbcb8', '00bbbcbf']]`
  - `FALL_THROUGH` [`00bbbcbc`](#insn-00bbbcbc) → [`00bbbcc0`](#insn-00bbbcc0)
- ブロック [`00bbbcc0`](#insn-00bbbcc0) 範囲 `[['00bbbcc0', '00bbbccf']]`
  - `UNCONDITIONAL_JUMP` [`00bbbccc`](#insn-00bbbccc) → [`00bbbc94`](#insn-00bbbc94)
- ブロック [`00bbbcd0`](#insn-00bbbcd0) 範囲 `[['00bbbcd0', '00bbbcef']]`
  - `CONDITIONAL_JUMP` [`00bbbcec`](#insn-00bbbcec) → [`00bbbd14`](#insn-00bbbd14)
  - `FALL_THROUGH` [`00bbbcec`](#insn-00bbbcec) → [`00bbbcf0`](#insn-00bbbcf0)
- ブロック [`00bbbcf0`](#insn-00bbbcf0) 範囲 `[['00bbbcf0', '00bbbcf3']]`
  - `CONDITIONAL_JUMP` [`00bbbcf0`](#insn-00bbbcf0) → [`00bbbc1c`](#insn-00bbbc1c)
  - `FALL_THROUGH` [`00bbbcf0`](#insn-00bbbcf0) → [`00bbbcf4`](#insn-00bbbcf4)
- ブロック [`00bbbcf4`](#insn-00bbbcf4) 範囲 `[['00bbbcf4', '00bbbd03']]`
  - `FALL_THROUGH` [`00bbbd00`](#insn-00bbbd00) → [`00bbbd04`](#insn-00bbbd04)
- ブロック [`00bbbd04`](#insn-00bbbd04) 範囲 `[['00bbbd04', '00bbbd0f']]`
  - `FALL_THROUGH` [`00bbbd0c`](#insn-00bbbd0c) → [`00bbbd10`](#insn-00bbbd10)
- ブロック [`00bbbd10`](#insn-00bbbd10) 範囲 `[['00bbbd10', '00bbbd13']]`
- ブロック [`00bbbd14`](#insn-00bbbd14) 範囲 `[['00bbbd14', '00bbbd1f']]`
  - `FALL_THROUGH` [`00bbbd1c`](#insn-00bbbd1c) → [`00bbbd20`](#insn-00bbbd20)
- ブロック [`00bbbd20`](#insn-00bbbd20) 範囲 `[['00bbbd20', '00bbbd33']]`
  - `CONDITIONAL_JUMP` [`00bbbd30`](#insn-00bbbd30) → [`00bbbc94`](#insn-00bbbc94)
  - `FALL_THROUGH` [`00bbbd30`](#insn-00bbbd30) → [`00bbbd34`](#insn-00bbbd34)
- ブロック [`00bbbd34`](#insn-00bbbd34) 範囲 `[['00bbbd34', '00bbbd57']]`
  - `CONDITIONAL_JUMP` [`00bbbd54`](#insn-00bbbd54) → [`00bbbc94`](#insn-00bbbc94)
  - `FALL_THROUGH` [`00bbbd54`](#insn-00bbbd54) → [`00bbbd58`](#insn-00bbbd58)
- ブロック [`00bbbd58`](#insn-00bbbd58) 範囲 `[['00bbbd58', '00bbbd6b']]`
  - `FALL_THROUGH` [`00bbbd68`](#insn-00bbbd68) → [`00bbbd6c`](#insn-00bbbd6c)
- ブロック [`00bbbd6c`](#insn-00bbbd6c) 範囲 `[['00bbbd6c', '00bbbd77']]`
  - `FALL_THROUGH` [`00bbbd74`](#insn-00bbbd74) → [`00bbbd78`](#insn-00bbbd78)
- ブロック [`00bbbd78`](#insn-00bbbd78) 範囲 `[['00bbbd78', '00bbbdb3']]`
  - `CONDITIONAL_JUMP` [`00bbbdb0`](#insn-00bbbdb0) → [`00bbbc94`](#insn-00bbbc94)
  - `FALL_THROUGH` [`00bbbdb0`](#insn-00bbbdb0) → [`00bbbdb4`](#insn-00bbbdb4)
- ブロック [`00bbbdb4`](#insn-00bbbdb4) 範囲 `[['00bbbdb4', '00bbbdc7']]`
  - `UNCONDITIONAL_JUMP` [`00bbbdc4`](#insn-00bbbdc4) → [`00bbbc94`](#insn-00bbbc94)

## 命令位置別の参照

- [`00bbbb14`](#insn-00bbbb14) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb18`](#insn-00bbbb18) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb1c`](#insn-00bbbb1c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb20`](#insn-00bbbb20) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb34`](#insn-00bbbb34) → `00c1c010`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbb3c`](#insn-00bbbb3c) → [`00bbbb84`](#insn-00bbbb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb50`](#insn-00bbbb50) → [`00bbbb90`](#insn-00bbbb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb58`](#insn-00bbbb58) → [`00bbbb6c`](#insn-00bbbb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb64`](#insn-00bbbb64) → [`00bde980`](../00bde/00bde980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde980` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb68`](#insn-00bbbb68) → [`00bbbbc8`](#insn-00bbbbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb70`](#insn-00bbbb70) → [`00bbbc90`](#insn-00bbbc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb80`](#insn-00bbbb80) → [`00bbbc94`](#insn-00bbbc94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb8c`](#insn-00bbbb8c) → [`00bbbc94`](#insn-00bbbc94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbb9c`](#insn-00bbbb9c) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbb9c`](#insn-00bbbb9c) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbba0`](#insn-00bbbba0) → `00c1c008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbba0`](#insn-00bbbba0) → `00c16bf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv117__pbase_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbba8`](#insn-00bbbba8) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbac`](#insn-00bbbbac) → [`00bbbbc8`](#insn-00bbbbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbb8`](#insn-00bbbbb8) → [`00bbbb54`](#insn-00bbbb54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbc4`](#insn-00bbbbc4) → [`00bbbb6c`](#insn-00bbbb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbd4`](#insn-00bbbbd4) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbbd4`](#insn-00bbbbd4) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbbd8`](#insn-00bbbbd8) → `00c1c018`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbbd8`](#insn-00bbbbd8) → `00c16c08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv119__pointer_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbbe0`](#insn-00bbbbe0) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbe4`](#insn-00bbbbe4) → [`00bbbc94`](#insn-00bbbc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbec`](#insn-00bbbbec) → [`00bbbbfc`](#insn-00bbbbfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbbf8`](#insn-00bbbbf8) → [`00bbbc00`](#insn-00bbbc00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc0c`](#insn-00bbbc0c) → [`00bbbc1c`](#insn-00bbbc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc18`](#insn-00bbbc18) → [`00bbbc24`](#insn-00bbbc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc20`](#insn-00bbbc20) → [`00bbbc94`](#insn-00bbbc94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc38`](#insn-00bbbc38) → [`00bbbc90`](#insn-00bbbc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc44`](#insn-00bbbc44) → `00c1c020`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbc48`](#insn-00bbbc48) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbc48`](#insn-00bbbc48) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbc50`](#insn-00bbbc50) → [`00bbbcb0`](#insn-00bbbcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc60`](#insn-00bbbc60) → `00c1c018`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbc60`](#insn-00bbbc60) → `00c16c08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv119__pointer_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbc64`](#insn-00bbbc64) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc68`](#insn-00bbbc68) → [`00bbbcd0`](#insn-00bbbcd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc6c`](#insn-00bbbc6c) → [`00bbbc1c`](#insn-00bbbc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc74`](#insn-00bbbc74) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc78`](#insn-00bbbc78) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc7c`](#insn-00bbbc7c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc80`](#insn-00bbbc80) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc8c`](#insn-00bbbc8c) → [`00bbbdc8`](00bbbdc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbbdc8` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc94`](#insn-00bbbc94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc98`](#insn-00bbbc98) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbc9c`](#insn-00bbbc9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbca0`](#insn-00bbbca0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcbc`](#insn-00bbbcbc) → `00c1c028`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbcbc`](#insn-00bbbcbc) → `00c16c20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv120__function_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbcc0`](#insn-00bbbcc0) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbccc`](#insn-00bbbccc) → [`00bbbc94`](#insn-00bbbc94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcdc`](#insn-00bbbcdc) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbcdc`](#insn-00bbbcdc) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbce0`](#insn-00bbbce0) → `00c1c030`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbce0`](#insn-00bbbce0) → `00c16c38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv129__pointer_to_member_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbce8`](#insn-00bbbce8) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcec`](#insn-00bbbcec) → [`00bbbd14`](#insn-00bbbd14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcf0`](#insn-00bbbcf0) → [`00bbbc1c`](#insn-00bbbc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcf8`](#insn-00bbbcf8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbcfc`](#insn-00bbbcfc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd00`](#insn-00bbbd00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd04`](#insn-00bbbd04) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd10`](#insn-00bbbd10) → [`00bbbebc`](00bbbebc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbbebc` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd20`](#insn-00bbbd20) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbd20`](#insn-00bbbd20) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbd24`](#insn-00bbbd24) → `00c1c000`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbd24`](#insn-00bbbd24) → `00c16bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv117__class_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbd2c`](#insn-00bbbd2c) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd30`](#insn-00bbbd30) → [`00bbbc94`](#insn-00bbbc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd40`](#insn-00bbbd40) → `00c1bff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbd40`](#insn-00bbbd40) → `00c16bc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv116__shim_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbd44`](#insn-00bbbd44) → `00c1c000`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbbd44`](#insn-00bbbd44) → `00c16bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN10__cxxabiv117__class_type_infoE` · 推定型 `pointer __((offset(0x10)))`
- [`00bbbd50`](#insn-00bbbd50) → [`00bdb770`](../00bdb/00bdb770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb770` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd54`](#insn-00bbbd54) → [`00bbbc94`](#insn-00bbbc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd60`](#insn-00bbbd60) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd70`](#insn-00bbbd70) → `Stack[-0x49]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd7c`](#insn-00bbbd7c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd80`](#insn-00bbbd80) → `Stack[-0x59]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd84`](#insn-00bbbd84) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd88`](#insn-00bbbd88) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd90`](#insn-00bbbd90) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbd98`](#insn-00bbbd98) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbda4`](#insn-00bbbda4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdb0`](#insn-00bbbdb0) → [`00bbbc94`](#insn-00bbbc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdb4`](#insn-00bbbdb4) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbbdc4`](#insn-00bbbdc4) → [`00bbbc94`](#insn-00bbbc94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbbb14`](#insn-00bbbb14)

~~~json
{
  "source": "00bbbb14",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb18`](#insn-00bbbb18)

~~~json
{
  "source": "00bbbb18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb1c`](#insn-00bbbb1c)

~~~json
{
  "source": "00bbbb1c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb20`](#insn-00bbbb20)

~~~json
{
  "source": "00bbbb20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb34`](#insn-00bbbb34)

~~~json
{
  "source": "00bbbb34",
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
- 参照命令 [`00bbbb3c`](#insn-00bbbb3c)

~~~json
{
  "source": "00bbbb3c",
  "target": "00bbbb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb50`](#insn-00bbbb50)

~~~json
{
  "source": "00bbbb50",
  "target": "00bbbb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb58`](#insn-00bbbb58)

~~~json
{
  "source": "00bbbb58",
  "target": "00bbbb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb64`](#insn-00bbbb64)

~~~json
{
  "source": "00bbbb64",
  "target": "00bde980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbb68`](#insn-00bbbb68)

~~~json
{
  "source": "00bbbb68",
  "target": "00bbbbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb70`](#insn-00bbbb70)

~~~json
{
  "source": "00bbbb70",
  "target": "00bbbc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb80`](#insn-00bbbb80)

~~~json
{
  "source": "00bbbb80",
  "target": "00bbbc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb8c`](#insn-00bbbb8c)

~~~json
{
  "source": "00bbbb8c",
  "target": "00bbbc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbb9c`](#insn-00bbbb9c)

~~~json
{
  "source": "00bbbb9c",
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
- 参照命令 [`00bbbb9c`](#insn-00bbbb9c)

~~~json
{
  "source": "00bbbb9c",
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
- 参照命令 [`00bbbba0`](#insn-00bbbba0)

~~~json
{
  "source": "00bbbba0",
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
- 参照命令 [`00bbbba0`](#insn-00bbbba0)

~~~json
{
  "source": "00bbbba0",
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
- 参照命令 [`00bbbba8`](#insn-00bbbba8)

~~~json
{
  "source": "00bbbba8",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbbac`](#insn-00bbbbac)

~~~json
{
  "source": "00bbbbac",
  "target": "00bbbbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbb8`](#insn-00bbbbb8)

~~~json
{
  "source": "00bbbbb8",
  "target": "00bbbb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbc4`](#insn-00bbbbc4)

~~~json
{
  "source": "00bbbbc4",
  "target": "00bbbb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbd4`](#insn-00bbbbd4)

~~~json
{
  "source": "00bbbbd4",
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
- 参照命令 [`00bbbbd4`](#insn-00bbbbd4)

~~~json
{
  "source": "00bbbbd4",
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
- 参照命令 [`00bbbbd8`](#insn-00bbbbd8)

~~~json
{
  "source": "00bbbbd8",
  "target": "00c1c018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c018",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbbd8`](#insn-00bbbbd8)

~~~json
{
  "source": "00bbbbd8",
  "target": "00c16c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbbe0`](#insn-00bbbbe0)

~~~json
{
  "source": "00bbbbe0",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbbe4`](#insn-00bbbbe4)

~~~json
{
  "source": "00bbbbe4",
  "target": "00bbbc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbec`](#insn-00bbbbec)

~~~json
{
  "source": "00bbbbec",
  "target": "00bbbbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbbf8`](#insn-00bbbbf8)

~~~json
{
  "source": "00bbbbf8",
  "target": "00bbbc00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc0c`](#insn-00bbbc0c)

~~~json
{
  "source": "00bbbc0c",
  "target": "00bbbc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc18`](#insn-00bbbc18)

~~~json
{
  "source": "00bbbc18",
  "target": "00bbbc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc20`](#insn-00bbbc20)

~~~json
{
  "source": "00bbbc20",
  "target": "00bbbc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc38`](#insn-00bbbc38)

~~~json
{
  "source": "00bbbc38",
  "target": "00bbbc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc44`](#insn-00bbbc44)

~~~json
{
  "source": "00bbbc44",
  "target": "00c1c020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c020",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbc48`](#insn-00bbbc48)

~~~json
{
  "source": "00bbbc48",
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
- 参照命令 [`00bbbc48`](#insn-00bbbc48)

~~~json
{
  "source": "00bbbc48",
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
- 参照命令 [`00bbbc50`](#insn-00bbbc50)

~~~json
{
  "source": "00bbbc50",
  "target": "00bbbcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc60`](#insn-00bbbc60)

~~~json
{
  "source": "00bbbc60",
  "target": "00c1c018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c018",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbc60`](#insn-00bbbc60)

~~~json
{
  "source": "00bbbc60",
  "target": "00c16c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16c08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbc64`](#insn-00bbbc64)

~~~json
{
  "source": "00bbbc64",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbc68`](#insn-00bbbc68)

~~~json
{
  "source": "00bbbc68",
  "target": "00bbbcd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc6c`](#insn-00bbbc6c)

~~~json
{
  "source": "00bbbc6c",
  "target": "00bbbc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc74`](#insn-00bbbc74)

~~~json
{
  "source": "00bbbc74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc78`](#insn-00bbbc78)

~~~json
{
  "source": "00bbbc78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc7c`](#insn-00bbbc7c)

~~~json
{
  "source": "00bbbc7c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc80`](#insn-00bbbc80)

~~~json
{
  "source": "00bbbc80",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc8c`](#insn-00bbbc8c)

~~~json
{
  "source": "00bbbc8c",
  "target": "00bbbdc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbc94`](#insn-00bbbc94)

~~~json
{
  "source": "00bbbc94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc98`](#insn-00bbbc98)

~~~json
{
  "source": "00bbbc98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbc9c`](#insn-00bbbc9c)

~~~json
{
  "source": "00bbbc9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbca0`](#insn-00bbbca0)

~~~json
{
  "source": "00bbbca0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcbc`](#insn-00bbbcbc)

~~~json
{
  "source": "00bbbcbc",
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
- 参照命令 [`00bbbcbc`](#insn-00bbbcbc)

~~~json
{
  "source": "00bbbcbc",
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
- 参照命令 [`00bbbcc0`](#insn-00bbbcc0)

~~~json
{
  "source": "00bbbcc0",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbccc`](#insn-00bbbccc)

~~~json
{
  "source": "00bbbccc",
  "target": "00bbbc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcdc`](#insn-00bbbcdc)

~~~json
{
  "source": "00bbbcdc",
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
- 参照命令 [`00bbbcdc`](#insn-00bbbcdc)

~~~json
{
  "source": "00bbbcdc",
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
- 参照命令 [`00bbbce0`](#insn-00bbbce0)

~~~json
{
  "source": "00bbbce0",
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
- 参照命令 [`00bbbce0`](#insn-00bbbce0)

~~~json
{
  "source": "00bbbce0",
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
- 参照命令 [`00bbbce8`](#insn-00bbbce8)

~~~json
{
  "source": "00bbbce8",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbcec`](#insn-00bbbcec)

~~~json
{
  "source": "00bbbcec",
  "target": "00bbbd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcf0`](#insn-00bbbcf0)

~~~json
{
  "source": "00bbbcf0",
  "target": "00bbbc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcf8`](#insn-00bbbcf8)

~~~json
{
  "source": "00bbbcf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbcfc`](#insn-00bbbcfc)

~~~json
{
  "source": "00bbbcfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd00`](#insn-00bbbd00)

~~~json
{
  "source": "00bbbd00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd04`](#insn-00bbbd04)

~~~json
{
  "source": "00bbbd04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd10`](#insn-00bbbd10)

~~~json
{
  "source": "00bbbd10",
  "target": "00bbbebc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd20`](#insn-00bbbd20)

~~~json
{
  "source": "00bbbd20",
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
- 参照命令 [`00bbbd20`](#insn-00bbbd20)

~~~json
{
  "source": "00bbbd20",
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
- 参照命令 [`00bbbd24`](#insn-00bbbd24)

~~~json
{
  "source": "00bbbd24",
  "target": "00c1c000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c000",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbd24`](#insn-00bbbd24)

~~~json
{
  "source": "00bbbd24",
  "target": "00c16bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16bd8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbd2c`](#insn-00bbbd2c)

~~~json
{
  "source": "00bbbd2c",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd30`](#insn-00bbbd30)

~~~json
{
  "source": "00bbbd30",
  "target": "00bbbc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd40`](#insn-00bbbd40)

~~~json
{
  "source": "00bbbd40",
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
- 参照命令 [`00bbbd40`](#insn-00bbbd40)

~~~json
{
  "source": "00bbbd40",
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
- 参照命令 [`00bbbd44`](#insn-00bbbd44)

~~~json
{
  "source": "00bbbd44",
  "target": "00c1c000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c000",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbd44`](#insn-00bbbd44)

~~~json
{
  "source": "00bbbd44",
  "target": "00c16bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16bd8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbbd50`](#insn-00bbbd50)

~~~json
{
  "source": "00bbbd50",
  "target": "00bdb770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbbd54`](#insn-00bbbd54)

~~~json
{
  "source": "00bbbd54",
  "target": "00bbbc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd60`](#insn-00bbbd60)

~~~json
{
  "source": "00bbbd60",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd70`](#insn-00bbbd70)

~~~json
{
  "source": "00bbbd70",
  "target": "Stack[-0x49]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd7c`](#insn-00bbbd7c)

~~~json
{
  "source": "00bbbd7c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd80`](#insn-00bbbd80)

~~~json
{
  "source": "00bbbd80",
  "target": "Stack[-0x59]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd84`](#insn-00bbbd84)

~~~json
{
  "source": "00bbbd84",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd88`](#insn-00bbbd88)

~~~json
{
  "source": "00bbbd88",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd90`](#insn-00bbbd90)

~~~json
{
  "source": "00bbbd90",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbd98`](#insn-00bbbd98)

~~~json
{
  "source": "00bbbd98",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbda4`](#insn-00bbbda4)

~~~json
{
  "source": "00bbbda4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdb0`](#insn-00bbbdb0)

~~~json
{
  "source": "00bbbdb0",
  "target": "00bbbc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdb4`](#insn-00bbbdb4)

~~~json
{
  "source": "00bbbdb4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbbdc4`](#insn-00bbbdc4)

~~~json
{
  "source": "00bbbdc4",
  "target": "00bbbc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
