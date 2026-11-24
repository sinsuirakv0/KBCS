# 006acaec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `006acaac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ac/006acaac.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0031.md#compare-abb839cb61b4f6646263482b8fd1e65b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `006acb44`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006ac/006acb44.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0031.md#compare-cea5d637a7fb9e767709deee1857f768)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006acaec",
  "name": "FUN_006acaec",
  "size": 1136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45473c2ae722ab12b886d48f69e9d870b234626afd31970cceb3348fbed31ec9",
  "source_text_sha256": "45473c2ae722ab12b886d48f69e9d870b234626afd31970cceb3348fbed31ec9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006acaec",
        "006acf5b"
      ]
    ],
    "bytes_sha256": "cdc7c798b3726ad1f2fdbf5a4dcd61647ed8a4971c987c73a55518a3c28c7d4d",
    "instruction_count": 284,
    "instruction_bytes": 1136,
    "body_bytes": 1136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0099703c](../00997/0099703c.md)

## 呼び出し先

- [00467860](../00467/00467860.md)
- [00467af0](../00467/00467af0.md)
- [00467b2c](../00467/00467b2c.md)
- [00467f54](../00467/00467f54.md)
- [004688b8](../00468/004688b8.md)
- [00469c04](../00469/00469c04.md)
- [0046bd54](../0046b/0046bd54.md)
- [0046c9c4](../0046c/0046c9c4.md)
- [0046ca84](../0046c/0046ca84.md)
- [0046e72c](../0046e/0046e72c.md)
- [0046e7ac](../0046e/0046e7ac.md)
- [0046e7b4](../0046e/0046e7b4.md)
- [0046e7bc](../0046e/0046e7bc.md)
- [004700b4](../00470/004700b4.md)
- [0047012c](../00470/0047012c.md)
- [006acf5c](../006ac/006acf5c.md)
- [006ad414](../006ad/006ad414.md)
- [006c119c](../006c1/006c119c.md)
- [008514f8](../00851/008514f8.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58610](../00c58/00c58610.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6866 bytes

~~~c

void FUN_006acaec(char *param_1)

{
  byte *pbVar1;
  long lVar2;
  undefined4 uVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  int iVar6;
  int iVar7;
  long lVar8;
  undefined8 uVar9;
  long lVar10;
  char *pcVar11;
  undefined8 uVar12;
  int local_70;
  int iStack_6c;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  if (DAT_00ca4978 == 0) {
    lVar8 = 0;
  }
  else {
    lVar8 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c711c0,0);
  }
  uVar9 = FUN_00467860();
  if (*param_1 == '\0') goto LAB_006acf28;
  if ((param_1[0x4e0] & 1U) == 0) {
    uVar12 = *(undefined8 *)(param_1 + 0x208);
                    /* try { // try from 006acb6c to 007acb73 has its CatchHandler @ 006acde8 */
    FUN_008514f8();
    uVar3 = FUN_0046c9c4();
    FUN_008514f8();
    uVar4 = FUN_0046ca84();
                    /* try { // try from 006acb94 to 007acbbf has its CatchHandler @ 006acdf0 */
    uVar5 = 0x62;
    if (*(int *)(param_1 + 0x4e8) != 3) {
      uVar5 = 2;
    }
    FUN_00469c04(uVar9,uVar12,0,0,uVar3,uVar4,uVar5);
    iVar6 = *(int *)(param_1 + 0x4ec);
    if (iVar6 == 1) {
                    /* try { // try from 006acbc0 to 007acc37 has its CatchHandler @ 006aca44 */
      FUN_00467af0(uVar9,1);
      FUN_00467b2c(uVar9,0xab,0x2c,0,0x40);
      lVar10 = FUN_008514f8();
      iVar6 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar10);
      FUN_008514f8();
      uVar5 = FUN_0046c9c4();
      FUN_008514f8();
      uVar3 = FUN_0046ca84();
      FUN_00467f54(uVar9,0,-iVar6,uVar5,uVar3);
      FUN_00467b2c(uVar9,0xff,0xff,0xff,0xff);
                    /* try { // try from 006acc38 to 007acc3f has its CatchHandler @ 006acd78 */
      FUN_00467af0(uVar9,0);
                    /* try { // try from 006acc44 to 007acc4b has its CatchHandler @ 006acdc8 */
      iVar6 = *(int *)(param_1 + 0x4ec);
    }
    FUN_004700b4(param_1 + (long)iVar6 * 0xa8 + 0x38,param_1 + (long)iVar6 * 0x38 + 0x188,
                 *(undefined4 *)(param_1 + 0x4f4),0);
    FUN_0047012c(param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,0);
    uVar12 = FUN_0046e7ac();
    iVar6 = *(int *)(param_1 + 0x4ec);
                    /* try { // try from 006acc88 to 007acc8f has its CatchHandler @ 006acd58 */
    FUN_0047012c(param_1 + (long)iVar6 * 0xa8 + 0x38,1);
    uVar5 = FUN_0046e7b4();
                    /* try { // try from 006acc9c to 007accab has its CatchHandler @ 006acd90 */
                    /* try { // try from 006accac to 007ace2f has its CatchHandler @ 006aca44 */
    FUN_0047012c(param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,1);
    uVar3 = FUN_0046e7bc();
    FUN_0046e72c(uVar12,param_1 + (long)iVar6 * 0xa8 + 0x38,uVar5,uVar3,&local_70);
    FUN_008514f8();
    iVar6 = FUN_0046c9c4();
    if (iVar6 < 0) {
      iVar6 = iVar6 + 1;
    }
    lVar10 = FUN_008514f8();
    lVar10 = lVar10 + (long)*(int *)(param_1 + 0x4e4) * 0x100;
    pbVar1 = (byte *)(lVar10 + 0x4b278 +
                     (long)(*(int *)(param_1 + 0x4e8) + *(int *)(param_1 + 0x4ec) + 0x33) * 4);
                    /* catch() { ... } // from try @ 006acc88 with catch @ 006acd58 */
    FUN_0046bd54(uVar9,param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,
                 (iVar6 >> 1) - local_70,
                 ((uint)CONCAT12(*(byte *)(lVar10 + 0x4b376) ^ pbVar1[2],
                                 CONCAT11(*(byte *)(lVar10 + 0x4b375) ^ pbVar1[1],
                                          *(byte *)(lVar10 + 0x4b374) ^ *pbVar1)) - iStack_6c) +
                 (uint)(*(byte *)(lVar10 + 0x4b377) ^ pbVar1[3]) * 0x1000000 + 0x1d4);
    iVar6 = *(int *)(param_1 + 0x4f0);
    if (iVar6 < 3) {
      if (iVar6 == 1) {
                    /* try { // try from 006acec0 to 007acf93 has its CatchHandler @ 006acec0
                       catch() { ... } // from try @ 006acec0 with catch @ 006acec0
                       catch() { ... } // from try @ 006acfc0 with catch @ 006acec0
                       catch() { ... } // from try @ 006ad0e8 with catch @ 006acec0 */
        FUN_004700b4(param_1 + 0x268,param_1 + 0x310,*(undefined4 *)(param_1 + 0x4f8),0);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_008514f8();
        iVar7 = FUN_0046ca84();
        pcVar11 = param_1 + 0x268;
      }
      else {
                    /* catch() { ... } // from try @ 006acc38 with catch @ 006acd78 */
        if (iVar6 != 2) goto LAB_006acf0c;
                    /* catch() { ... } // from try @ 006acc9c with catch @ 006acd90 */
        FUN_004700b4(param_1 + 0x380,param_1 + 0x428,*(undefined4 *)(param_1 + 0x4fc),0);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_008514f8();
        iVar7 = FUN_0046ca84();
        pcVar11 = param_1 + 0x380;
      }
      if (iVar7 < 0) {
        iVar7 = iVar7 + 1;
      }
      FUN_0046bd54(uVar9,pcVar11,iVar6 >> 1,iVar7 >> 1);
    }
    else {
                    /* catch() { ... } // from try @ 006acc44 with catch @ 006acdc8 */
      if ((iVar6 == 3) || (iVar6 == 4)) {
        FUN_004700b4(param_1 + 0x380,param_1 + 0x428,*(undefined4 *)(param_1 + 0x4fc),0);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
                    /* catch() { ... } // from try @ 006acb6c with catch @ 006acde8 */
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
                    /* catch() { ... } // from try @ 006acb94 with catch @ 006acdf0 */
        FUN_008514f8();
        iVar7 = FUN_0046ca84();
        if (iVar7 < 0) {
          iVar7 = iVar7 + 1;
        }
        FUN_0046bd54(uVar9,param_1 + 0x380,iVar6 >> 1,iVar7 >> 1);
        FUN_006c119c(param_1 + 0x460);
        uVar12 = *(undefined8 *)(lVar8 + 8);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_00469c04(uVar9,uVar12,(iVar6 >> 1) + -0xd7,0x1f8,0xdc,0x3e,1);
        uVar12 = *(undefined8 *)(lVar8 + 8);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_00469c04(uVar9,uVar12,iVar6 >> 1,0x1f8,0xdc,0x3e,2);
        uVar12 = *(undefined8 *)(param_1 + 0x1f8);
        FUN_008514f8();
        iVar6 = FUN_0046c9c4();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_004688b8(uVar9,uVar12,iVar6 >> 1,0x217,0x1a4,5);
      }
    }
LAB_006acf0c:
    FUN_006acf5c();
  }
  if ((*(uint *)(param_1 + 0x4f0) | 4) == 4) {
    FUN_006ad414(param_1);
  }
LAB_006acf28:
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006acaec"></a> `006acaec` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-006acaf0"></a> `006acaf0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006acaf4"></a> `006acaf4` | `fb 13 00 f9` | str x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006acaf8"></a> `006acaf8` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006acafc"></a> `006acafc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006acb00"></a> `006acb00` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006acb04"></a> `006acb04` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006acb08"></a> `006acb08` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-006acb0c"></a> `006acb0c` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-006acb10"></a> `006acb10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006acb14"></a> `006acb14` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-006acb18"></a> `006acb18` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006acb1c"></a> `006acb1c` | `c8 2f 00 90` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-006acb20"></a> `006acb20` | `08 bd 44 f9` | ldr x8,[x8, #0x978] | `FALL_THROUGH`
<a id="insn-006acb24"></a> `006acb24` | `48 01 00 b4` | cbz x8,0x006acb4c | `CONDITIONAL_JUMP`
<a id="insn-006acb28"></a> `006acb28` | `c1 2d 00 b0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-006acb2c"></a> `006acb2c` | `21 60 39 91` | add x1,x1,#0xe58 | `FALL_THROUGH`
<a id="insn-006acb30"></a> `006acb30` | `22 2e 00 b0` | adrp x2,0xc71000 | `FALL_THROUGH`
<a id="insn-006acb34"></a> `006acb34` | `42 00 07 91` | add x2,x2,#0x1c0 | `FALL_THROUGH`
<a id="insn-006acb38"></a> `006acb38` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-006acb3c"></a> `006acb3c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-006acb40"></a> `006acb40` | `b4 ae 16 94` | bl 0x00c58610 | `UNCONDITIONAL_CALL`
<a id="insn-006acb44"></a> `006acb44` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-006acb48"></a> `006acb48` | `02 00 00 14` | b 0x006acb50 | `UNCONDITIONAL_JUMP`
<a id="insn-006acb4c"></a> `006acb4c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-006acb50"></a> `006acb50` | `44 eb f6 97` | bl 0x00467860 | `UNCONDITIONAL_CALL`
<a id="insn-006acb54"></a> `006acb54` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-006acb58"></a> `006acb58` | `88 1e 00 34` | cbz w8,0x006acf28 | `CONDITIONAL_JUMP`
<a id="insn-006acb5c"></a> `006acb5c` | `68 82 53 39` | ldrb w8,[x19, #0x4e0] | `FALL_THROUGH`
<a id="insn-006acb60"></a> `006acb60` | `88 1d 00 37` | tbnz w8,#0x0,0x006acf10 | `CONDITIONAL_JUMP`
<a id="insn-006acb64"></a> `006acb64` | `76 06 41 f9` | ldr x22,[x19, #0x208] | `FALL_THROUGH`
<a id="insn-006acb68"></a> `006acb68` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-006acb6c"></a> `006acb6c` | `63 92 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006acb70"></a> `006acb70` | `95 ff f6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-006acb74"></a> `006acb74` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-006acb78"></a> `006acb78` | `60 92 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006acb7c"></a> `006acb7c` | `c2 ff f6 97` | bl 0x0046ca84 | `UNCONDITIONAL_CALL`
<a id="insn-006acb80"></a> `006acb80` | `68 ea 44 b9` | ldr w8,[x19, #0x4e8] | `FALL_THROUGH`
<a id="insn-006acb84"></a> `006acb84` | `49 0c 80 52` | mov w9,#0x62 | `FALL_THROUGH`
<a id="insn-006acb88"></a> `006acb88` | `e5 03 00 2a` | mov w5,w0 | `FALL_THROUGH`
<a id="insn-006acb8c"></a> `006acb8c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acb90"></a> `006acb90` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-006acb94"></a> `006acb94` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-006acb98"></a> `006acb98` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-006acb9c"></a> `006acb9c` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-006acba0"></a> `006acba0` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006acba4"></a> `006acba4` | `26 01 88 1a` | csel w6,w9,w8,eq | `FALL_THROUGH`
<a id="insn-006acba8"></a> `006acba8` | `e4 03 17 2a` | mov w4,w23 | `FALL_THROUGH`
<a id="insn-006acbac"></a> `006acbac` | `16 f4 f6 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-006acbb0"></a> `006acbb0` | `68 ee 44 b9` | ldr w8,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006acbb4"></a> `006acbb4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acbb8"></a> `006acbb8` | `81 04 00 54` | b.ne 0x006acc48 | `CONDITIONAL_JUMP`
<a id="insn-006acbbc"></a> `006acbbc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acbc0"></a> `006acbc0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-006acbc4"></a> `006acbc4` | `cb eb f6 97` | bl 0x00467af0 | `UNCONDITIONAL_CALL`
<a id="insn-006acbc8"></a> `006acbc8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acbcc"></a> `006acbcc` | `61 15 80 52` | mov w1,#0xab | `FALL_THROUGH`
<a id="insn-006acbd0"></a> `006acbd0` | `82 05 80 52` | mov w2,#0x2c | `FALL_THROUGH`
<a id="insn-006acbd4"></a> `006acbd4` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006acbd8"></a> `006acbd8` | `04 08 80 52` | mov w4,#0x40 | `FALL_THROUGH`
<a id="insn-006acbdc"></a> `006acbdc` | `d4 eb f6 97` | bl 0x00467b2c | `UNCONDITIONAL_CALL`
<a id="insn-006acbe0"></a> `006acbe0` | `46 92 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006acbe4"></a> `006acbe4` | `08 3d 87 52` | mov w8,#0x39e8 | `FALL_THROUGH`
<a id="insn-006acbe8"></a> `006acbe8` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-006acbec"></a> `006acbec` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006acbf0"></a> `006acbf0` | `f6 03 08 4b` | neg w22,w8 | `FALL_THROUGH`
<a id="insn-006acbf4"></a> `006acbf4` | `41 92 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006acbf8"></a> `006acbf8` | `73 ff f6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-006acbfc"></a> `006acbfc` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-006acc00"></a> `006acc00` | `3e 92 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006acc04"></a> `006acc04` | `a0 ff f6 97` | bl 0x0046ca84 | `UNCONDITIONAL_CALL`
<a id="insn-006acc08"></a> `006acc08` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-006acc0c"></a> `006acc0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acc10"></a> `006acc10` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006acc14"></a> `006acc14` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-006acc18"></a> `006acc18` | `e3 03 17 2a` | mov w3,w23 | `FALL_THROUGH`
<a id="insn-006acc1c"></a> `006acc1c` | `ce ec f6 97` | bl 0x00467f54 | `UNCONDITIONAL_CALL`
<a id="insn-006acc20"></a> `006acc20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acc24"></a> `006acc24` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-006acc28"></a> `006acc28` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-006acc2c"></a> `006acc2c` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-006acc30"></a> `006acc30` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-006acc34"></a> `006acc34` | `be eb f6 97` | bl 0x00467b2c | `UNCONDITIONAL_CALL`
<a id="insn-006acc38"></a> `006acc38` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acc3c"></a> `006acc3c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006acc40"></a> `006acc40` | `ac eb f6 97` | bl 0x00467af0 | `UNCONDITIONAL_CALL`
<a id="insn-006acc44"></a> `006acc44` | `68 ee 44 b9` | ldr w8,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006acc48"></a> `006acc48` | `1a 15 80 52` | mov w26,#0xa8 | `FALL_THROUGH`
<a id="insn-006acc4c"></a> `006acc4c` | `09 07 80 52` | mov w9,#0x38 | `FALL_THROUGH`
<a id="insn-006acc50"></a> `006acc50` | `7b e2 00 91` | add x27,x19,#0x38 | `FALL_THROUGH`
<a id="insn-006acc54"></a> `006acc54` | `00 6d 3a 9b` | smaddl x0,w8,w26,x27 | `FALL_THROUGH`
<a id="insn-006acc58"></a> `006acc58` | `62 f6 44 b9` | ldr w2,[x19, #0x4f4] | `FALL_THROUGH`
<a id="insn-006acc5c"></a> `006acc5c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006acc60"></a> `006acc60` | `08 4d 29 9b` | smaddl x8,w8,w9,x19 | `FALL_THROUGH`
<a id="insn-006acc64"></a> `006acc64` | `01 21 06 91` | add x1,x8,#0x188 | `FALL_THROUGH`
<a id="insn-006acc68"></a> `006acc68` | `13 0d f7 97` | bl 0x004700b4 | `UNCONDITIONAL_CALL`
<a id="insn-006acc6c"></a> `006acc6c` | `68 ee 84 b9` | ldrsw x8,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006acc70"></a> `006acc70` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006acc74"></a> `006acc74` | `00 6d 3a 9b` | smaddl x0,w8,w26,x27 | `FALL_THROUGH`
<a id="insn-006acc78"></a> `006acc78` | `2d 0d f7 97` | bl 0x0047012c | `UNCONDITIONAL_CALL`
<a id="insn-006acc7c"></a> `006acc7c` | `cc 06 f7 97` | bl 0x0046e7ac | `UNCONDITIONAL_CALL`
<a id="insn-006acc80"></a> `006acc80` | `68 ee 84 b9` | ldrsw x8,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006acc84"></a> `006acc84` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-006acc88"></a> `006acc88` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-006acc8c"></a> `006acc8c` | `16 6d 3a 9b` | smaddl x22,w8,w26,x27 | `FALL_THROUGH`
<a id="insn-006acc90"></a> `006acc90` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-006acc94"></a> `006acc94` | `26 0d f7 97` | bl 0x0047012c | `UNCONDITIONAL_CALL`
<a id="insn-006acc98"></a> `006acc98` | `c7 06 f7 97` | bl 0x0046e7b4 | `UNCONDITIONAL_CALL`
<a id="insn-006acc9c"></a> `006acc9c` | `68 ee 84 b9` | ldrsw x8,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006acca0"></a> `006acca0` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-006acca4"></a> `006acca4` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-006acca8"></a> `006acca8` | `08 6d 3a 9b` | smaddl x8,w8,w26,x27 | `FALL_THROUGH`
<a id="insn-006accac"></a> `006accac` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-006accb0"></a> `006accb0` | `1f 0d f7 97` | bl 0x0047012c | `UNCONDITIONAL_CALL`
<a id="insn-006accb4"></a> `006accb4` | `c2 06 f7 97` | bl 0x0046e7bc | `UNCONDITIONAL_CALL`
<a id="insn-006accb8"></a> `006accb8` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-006accbc"></a> `006accbc` | `e4 03 00 91` | mov x4,sp | `FALL_THROUGH`
<a id="insn-006accc0"></a> `006accc0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-006accc4"></a> `006accc4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-006accc8"></a> `006accc8` | `e2 03 18 2a` | mov w2,w24 | `FALL_THROUGH`
<a id="insn-006acccc"></a> `006acccc` | `98 06 f7 97` | bl 0x0046e72c | `UNCONDITIONAL_CALL`
<a id="insn-006accd0"></a> `006accd0` | `0a 92 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006accd4"></a> `006accd4` | `3c ff f6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-006accd8"></a> `006accd8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006accdc"></a> `006accdc` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acce0"></a> `006acce0` | `16 7d 01 13` | asr w22,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acce4"></a> `006acce4` | `05 92 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006acce8"></a> `006acce8` | `68 e6 84 b9` | ldrsw x8,[x19, #0x4e4] | `FALL_THROUGH`
<a id="insn-006accec"></a> `006accec` | `69 ea 44 b9` | ldr w9,[x19, #0x4e8] | `FALL_THROUGH`
<a id="insn-006accf0"></a> `006accf0` | `6a ee 84 b9` | ldrsw x10,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006accf4"></a> `006accf4` | `08 20 08 8b` | add x8,x0,x8, LSL #0x8 | `FALL_THROUGH`
<a id="insn-006accf8"></a> `006accf8` | `29 01 0a 0b` | add w9,w9,w10 | `FALL_THROUGH`
<a id="insn-006accfc"></a> `006accfc` | `41 6d 3a 9b` | smaddl x1,w10,w26,x27 | `FALL_THROUGH`
<a id="insn-006acd00"></a> `006acd00` | `29 cd 00 11` | add w9,w9,#0x33 | `FALL_THROUGH`
<a id="insn-006acd04"></a> `006acd04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acd08"></a> `006acd08` | `08 2d 41 91` | add x8,x8,#0x4b, LSL #12 | `FALL_THROUGH`
<a id="insn-006acd0c"></a> `006acd0c` | `08 e1 09 91` | add x8,x8,#0x278 | `FALL_THROUGH`
<a id="insn-006acd10"></a> `006acd10` | `09 c9 29 8b` | add x9,x8,w9, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-006acd14"></a> `006acd14` | `0b f1 43 39` | ldrb w11,[x8, #0xfc] | `FALL_THROUGH`
<a id="insn-006acd18"></a> `006acd18` | `0d f5 43 39` | ldrb w13,[x8, #0xfd] | `FALL_THROUGH`
<a id="insn-006acd1c"></a> `006acd1c` | `2c 01 40 39` | ldrb w12,[x9] | `FALL_THROUGH`
<a id="insn-006acd20"></a> `006acd20` | `2e 05 40 39` | ldrb w14,[x9, #0x1] | `FALL_THROUGH`
<a id="insn-006acd24"></a> `006acd24` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-006acd28"></a> `006acd28` | `ac 01 0e 4a` | eor w12,w13,w14 | `FALL_THROUGH`
<a id="insn-006acd2c"></a> `006acd2c` | `2d 09 40 39` | ldrb w13,[x9, #0x2] | `FALL_THROUGH`
<a id="insn-006acd30"></a> `006acd30` | `0e f9 43 39` | ldrb w14,[x8, #0xfe] | `FALL_THROUGH`
<a id="insn-006acd34"></a> `006acd34` | `6b 21 0c 2a` | orr w11,w11,w12, LSL #0x8 | `FALL_THROUGH`
<a id="insn-006acd38"></a> `006acd38` | `29 0d 40 39` | ldrb w9,[x9, #0x3] | `FALL_THROUGH`
<a id="insn-006acd3c"></a> `006acd3c` | `08 fd 43 39` | ldrb w8,[x8, #0xff] | `FALL_THROUGH`
<a id="insn-006acd40"></a> `006acd40` | `cc 01 0d 4a` | eor w12,w14,w13 | `FALL_THROUGH`
<a id="insn-006acd44"></a> `006acd44` | `6b 41 0c 2a` | orr w11,w11,w12, LSL #0x10 | `FALL_THROUGH`
<a id="insn-006acd48"></a> `006acd48` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-006acd4c"></a> `006acd4c` | `ec 37 40 29` | ldp w12,w13,[sp] | `FALL_THROUGH`
<a id="insn-006acd50"></a> `006acd50` | `69 01 0d 4b` | sub w9,w11,w13 | `FALL_THROUGH`
<a id="insn-006acd54"></a> `006acd54` | `c2 02 0c 4b` | sub w2,w22,w12 | `FALL_THROUGH`
<a id="insn-006acd58"></a> `006acd58` | `28 61 08 0b` | add w8,w9,w8, LSL #0x18 | `FALL_THROUGH`
<a id="insn-006acd5c"></a> `006acd5c` | `03 51 07 11` | add w3,w8,#0x1d4 | `FALL_THROUGH`
<a id="insn-006acd60"></a> `006acd60` | `fd fb f6 97` | bl 0x0046bd54 | `UNCONDITIONAL_CALL`
<a id="insn-006acd64"></a> `006acd64` | `68 f2 44 b9` | ldr w8,[x19, #0x4f0] | `FALL_THROUGH`
<a id="insn-006acd68"></a> `006acd68` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-006acd6c"></a> `006acd6c` | `8c 02 00 54` | b.gt 0x006acdbc | `CONDITIONAL_JUMP`
<a id="insn-006acd70"></a> `006acd70` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acd74"></a> `006acd74` | `60 0a 00 54` | b.eq 0x006acec0 | `CONDITIONAL_JUMP`
<a id="insn-006acd78"></a> `006acd78` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-006acd7c"></a> `006acd7c` | `81 0c 00 54` | b.ne 0x006acf0c | `CONDITIONAL_JUMP`
<a id="insn-006acd80"></a> `006acd80` | `62 fe 44 b9` | ldr w2,[x19, #0x4fc] | `FALL_THROUGH`
<a id="insn-006acd84"></a> `006acd84` | `60 02 0e 91` | add x0,x19,#0x380 | `FALL_THROUGH`
<a id="insn-006acd88"></a> `006acd88` | `61 a2 10 91` | add x1,x19,#0x428 | `FALL_THROUGH`
<a id="insn-006acd8c"></a> `006acd8c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006acd90"></a> `006acd90` | `c9 0c f7 97` | bl 0x004700b4 | `UNCONDITIONAL_CALL`
<a id="insn-006acd94"></a> `006acd94` | `d9 91 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006acd98"></a> `006acd98` | `0b ff f6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-006acd9c"></a> `006acd9c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acda0"></a> `006acda0` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acda4"></a> `006acda4` | `15 7d 01 13` | asr w21,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acda8"></a> `006acda8` | `d4 91 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006acdac"></a> `006acdac` | `36 ff f6 97` | bl 0x0046ca84 | `UNCONDITIONAL_CALL`
<a id="insn-006acdb0"></a> `006acdb0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acdb4"></a> `006acdb4` | `61 02 0e 91` | add x1,x19,#0x380 | `FALL_THROUGH`
<a id="insn-006acdb8"></a> `006acdb8` | `50 00 00 14` | b 0x006acef8 | `UNCONDITIONAL_JUMP`
<a id="insn-006acdbc"></a> `006acdbc` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-006acdc0"></a> `006acdc0` | `60 00 00 54` | b.eq 0x006acdcc | `CONDITIONAL_JUMP`
<a id="insn-006acdc4"></a> `006acdc4` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-006acdc8"></a> `006acdc8` | `21 0a 00 54` | b.ne 0x006acf0c | `CONDITIONAL_JUMP`
<a id="insn-006acdcc"></a> `006acdcc` | `62 fe 44 b9` | ldr w2,[x19, #0x4fc] | `FALL_THROUGH`
<a id="insn-006acdd0"></a> `006acdd0` | `60 02 0e 91` | add x0,x19,#0x380 | `FALL_THROUGH`
<a id="insn-006acdd4"></a> `006acdd4` | `61 a2 10 91` | add x1,x19,#0x428 | `FALL_THROUGH`
<a id="insn-006acdd8"></a> `006acdd8` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006acddc"></a> `006acddc` | `b6 0c f7 97` | bl 0x004700b4 | `UNCONDITIONAL_CALL`
<a id="insn-006acde0"></a> `006acde0` | `c6 91 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006acde4"></a> `006acde4` | `f8 fe f6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-006acde8"></a> `006acde8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acdec"></a> `006acdec` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acdf0"></a> `006acdf0` | `16 7d 01 13` | asr w22,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acdf4"></a> `006acdf4` | `c1 91 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006acdf8"></a> `006acdf8` | `23 ff f6 97` | bl 0x0046ca84 | `UNCONDITIONAL_CALL`
<a id="insn-006acdfc"></a> `006acdfc` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006ace00"></a> `006ace00` | `61 02 0e 91` | add x1,x19,#0x380 | `FALL_THROUGH`
<a id="insn-006ace04"></a> `006ace04` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-006ace08"></a> `006ace08` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006ace0c"></a> `006ace0c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006ace10"></a> `006ace10` | `03 7d 01 13` | asr w3,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006ace14"></a> `006ace14` | `d0 fb f6 97` | bl 0x0046bd54 | `UNCONDITIONAL_CALL`
<a id="insn-006ace18"></a> `006ace18` | `60 82 11 91` | add x0,x19,#0x460 | `FALL_THROUGH`
<a id="insn-006ace1c"></a> `006ace1c` | `e0 50 00 94` | bl 0x006c119c | `UNCONDITIONAL_CALL`
<a id="insn-006ace20"></a> `006ace20` | `b6 06 40 f9` | ldr x22,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-006ace24"></a> `006ace24` | `b5 91 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006ace28"></a> `006ace28` | `e7 fe f6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-006ace2c"></a> `006ace2c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006ace30"></a> `006ace30` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-006ace34"></a> `006ace34` | `03 3f 80 52` | mov w3,#0x1f8 | `FALL_THROUGH`
<a id="insn-006ace38"></a> `006ace38` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006ace3c"></a> `006ace3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006ace40"></a> `006ace40` | `84 1b 80 52` | mov w4,#0xdc | `FALL_THROUGH`
<a id="insn-006ace44"></a> `006ace44` | `08 7d 01 13` | asr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006ace48"></a> `006ace48` | `c5 07 80 52` | mov w5,#0x3e | `FALL_THROUGH`
<a id="insn-006ace4c"></a> `006ace4c` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-006ace50"></a> `006ace50` | `02 5d 03 51` | sub w2,w8,#0xd7 | `FALL_THROUGH`
<a id="insn-006ace54"></a> `006ace54` | `6c f3 f6 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-006ace58"></a> `006ace58` | `b5 06 40 f9` | ldr x21,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-006ace5c"></a> `006ace5c` | `a7 91 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006ace60"></a> `006ace60` | `d9 fe f6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-006ace64"></a> `006ace64` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006ace68"></a> `006ace68` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-006ace6c"></a> `006ace6c` | `03 3f 80 52` | mov w3,#0x1f8 | `FALL_THROUGH`
<a id="insn-006ace70"></a> `006ace70` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006ace74"></a> `006ace74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006ace78"></a> `006ace78` | `84 1b 80 52` | mov w4,#0xdc | `FALL_THROUGH`
<a id="insn-006ace7c"></a> `006ace7c` | `02 7d 01 13` | asr w2,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006ace80"></a> `006ace80` | `c5 07 80 52` | mov w5,#0x3e | `FALL_THROUGH`
<a id="insn-006ace84"></a> `006ace84` | `46 00 80 52` | mov w6,#0x2 | `FALL_THROUGH`
<a id="insn-006ace88"></a> `006ace88` | `5f f3 f6 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-006ace8c"></a> `006ace8c` | `75 fe 40 f9` | ldr x21,[x19, #0x1f8] | `FALL_THROUGH`
<a id="insn-006ace90"></a> `006ace90` | `9a 91 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006ace94"></a> `006ace94` | `cc fe f6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-006ace98"></a> `006ace98` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006ace9c"></a> `006ace9c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-006acea0"></a> `006acea0` | `e3 42 80 52` | mov w3,#0x217 | `FALL_THROUGH`
<a id="insn-006acea4"></a> `006acea4` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acea8"></a> `006acea8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006aceac"></a> `006aceac` | `84 34 80 52` | mov w4,#0x1a4 | `FALL_THROUGH`
<a id="insn-006aceb0"></a> `006aceb0` | `02 7d 01 13` | asr w2,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006aceb4"></a> `006aceb4` | `a5 00 80 52` | mov w5,#0x5 | `FALL_THROUGH`
<a id="insn-006aceb8"></a> `006aceb8` | `80 ee f6 97` | bl 0x004688b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acebc"></a> `006acebc` | `14 00 00 14` | b 0x006acf0c | `UNCONDITIONAL_JUMP`
<a id="insn-006acec0"></a> `006acec0` | `62 fa 44 b9` | ldr w2,[x19, #0x4f8] | `FALL_THROUGH`
<a id="insn-006acec4"></a> `006acec4` | `60 a2 09 91` | add x0,x19,#0x268 | `FALL_THROUGH`
<a id="insn-006acec8"></a> `006acec8` | `61 42 0c 91` | add x1,x19,#0x310 | `FALL_THROUGH`
<a id="insn-006acecc"></a> `006acecc` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006aced0"></a> `006aced0` | `79 0c f7 97` | bl 0x004700b4 | `UNCONDITIONAL_CALL`
<a id="insn-006aced4"></a> `006aced4` | `89 91 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006aced8"></a> `006aced8` | `bb fe f6 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-006acedc"></a> `006acedc` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acee0"></a> `006acee0` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acee4"></a> `006acee4` | `15 7d 01 13` | asr w21,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acee8"></a> `006acee8` | `84 91 06 94` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-006aceec"></a> `006aceec` | `e6 fe f6 97` | bl 0x0046ca84 | `UNCONDITIONAL_CALL`
<a id="insn-006acef0"></a> `006acef0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acef4"></a> `006acef4` | `61 a2 09 91` | add x1,x19,#0x268 | `FALL_THROUGH`
<a id="insn-006acef8"></a> `006acef8` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acefc"></a> `006acefc` | `03 7d 01 13` | asr w3,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acf00"></a> `006acf00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acf04"></a> `006acf04` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-006acf08"></a> `006acf08` | `93 fb f6 97` | bl 0x0046bd54 | `UNCONDITIONAL_CALL`
<a id="insn-006acf0c"></a> `006acf0c` | `14 00 00 94` | bl 0x006acf5c | `UNCONDITIONAL_CALL`
<a id="insn-006acf10"></a> `006acf10` | `68 f2 44 b9` | ldr w8,[x19, #0x4f0] | `FALL_THROUGH`
<a id="insn-006acf14"></a> `006acf14` | `08 01 1e 32` | orr w8,w8,#0x4 | `FALL_THROUGH`
<a id="insn-006acf18"></a> `006acf18` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-006acf1c"></a> `006acf1c` | `61 00 00 54` | b.ne 0x006acf28 | `CONDITIONAL_JUMP`
<a id="insn-006acf20"></a> `006acf20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006acf24"></a> `006acf24` | `3c 01 00 94` | bl 0x006ad414 | `UNCONDITIONAL_CALL`
<a id="insn-006acf28"></a> `006acf28` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-006acf2c"></a> `006acf2c` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006acf30"></a> `006acf30` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006acf34"></a> `006acf34` | `21 01 00 54` | b.ne 0x006acf58 | `CONDITIONAL_JUMP`
<a id="insn-006acf38"></a> `006acf38` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006acf3c"></a> `006acf3c` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006acf40"></a> `006acf40` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006acf44"></a> `006acf44` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006acf48"></a> `006acf48` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006acf4c"></a> `006acf4c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006acf50"></a> `006acf50` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-006acf54"></a> `006acf54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006acf58"></a> `006acf58` | `e2 ab 16 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006acaec`](#insn-006acaec) 範囲 `[['006acaec', '006acb27']]`
  - `CONDITIONAL_JUMP` [`006acb24`](#insn-006acb24) → [`006acb4c`](#insn-006acb4c)
  - `FALL_THROUGH` [`006acb24`](#insn-006acb24) → [`006acb28`](#insn-006acb28)
- ブロック [`006acb28`](#insn-006acb28) 範囲 `[['006acb28', '006acb4b']]`
  - `UNCONDITIONAL_JUMP` [`006acb48`](#insn-006acb48) → [`006acb50`](#insn-006acb50)
- ブロック [`006acb4c`](#insn-006acb4c) 範囲 `[['006acb4c', '006acb4f']]`
  - `FALL_THROUGH` [`006acb4c`](#insn-006acb4c) → [`006acb50`](#insn-006acb50)
- ブロック [`006acb50`](#insn-006acb50) 範囲 `[['006acb50', '006acb5b']]`
  - `CONDITIONAL_JUMP` [`006acb58`](#insn-006acb58) → [`006acf28`](#insn-006acf28)
  - `FALL_THROUGH` [`006acb58`](#insn-006acb58) → [`006acb5c`](#insn-006acb5c)
- ブロック [`006acb5c`](#insn-006acb5c) 範囲 `[['006acb5c', '006acb63']]`
  - `CONDITIONAL_JUMP` [`006acb60`](#insn-006acb60) → [`006acf10`](#insn-006acf10)
  - `FALL_THROUGH` [`006acb60`](#insn-006acb60) → [`006acb64`](#insn-006acb64)
- ブロック [`006acb64`](#insn-006acb64) 範囲 `[['006acb64', '006acb6b']]`
  - `FALL_THROUGH` [`006acb68`](#insn-006acb68) → [`006acb6c`](#insn-006acb6c)
- ブロック [`006acb6c`](#insn-006acb6c) 範囲 `[['006acb6c', '006acb93']]`
  - `FALL_THROUGH` [`006acb90`](#insn-006acb90) → [`006acb94`](#insn-006acb94)
- ブロック [`006acb94`](#insn-006acb94) 範囲 `[['006acb94', '006acbbb']]`
  - `CONDITIONAL_JUMP` [`006acbb8`](#insn-006acbb8) → [`006acc48`](#insn-006acc48)
  - `FALL_THROUGH` [`006acbb8`](#insn-006acbb8) → [`006acbbc`](#insn-006acbbc)
- ブロック [`006acbbc`](#insn-006acbbc) 範囲 `[['006acbbc', '006acbbf']]`
  - `FALL_THROUGH` [`006acbbc`](#insn-006acbbc) → [`006acbc0`](#insn-006acbc0)
- ブロック [`006acbc0`](#insn-006acbc0) 範囲 `[['006acbc0', '006acc37']]`
  - `FALL_THROUGH` [`006acc34`](#insn-006acc34) → [`006acc38`](#insn-006acc38)
- ブロック [`006acc38`](#insn-006acc38) 範囲 `[['006acc38', '006acc43']]`
  - `FALL_THROUGH` [`006acc40`](#insn-006acc40) → [`006acc44`](#insn-006acc44)
- ブロック [`006acc44`](#insn-006acc44) 範囲 `[['006acc44', '006acc47']]`
  - `FALL_THROUGH` [`006acc44`](#insn-006acc44) → [`006acc48`](#insn-006acc48)
- ブロック [`006acc48`](#insn-006acc48) 範囲 `[['006acc48', '006acc87']]`
  - `FALL_THROUGH` [`006acc84`](#insn-006acc84) → [`006acc88`](#insn-006acc88)
- ブロック [`006acc88`](#insn-006acc88) 範囲 `[['006acc88', '006acc9b']]`
  - `FALL_THROUGH` [`006acc98`](#insn-006acc98) → [`006acc9c`](#insn-006acc9c)
- ブロック [`006acc9c`](#insn-006acc9c) 範囲 `[['006acc9c', '006accab']]`
  - `FALL_THROUGH` [`006acca8`](#insn-006acca8) → [`006accac`](#insn-006accac)
- ブロック [`006accac`](#insn-006accac) 範囲 `[['006accac', '006acd57']]`
  - `FALL_THROUGH` [`006acd54`](#insn-006acd54) → [`006acd58`](#insn-006acd58)
- ブロック [`006acd58`](#insn-006acd58) 範囲 `[['006acd58', '006acd6f']]`
  - `CONDITIONAL_JUMP` [`006acd6c`](#insn-006acd6c) → [`006acdbc`](#insn-006acdbc)
  - `FALL_THROUGH` [`006acd6c`](#insn-006acd6c) → [`006acd70`](#insn-006acd70)
- ブロック [`006acd70`](#insn-006acd70) 範囲 `[['006acd70', '006acd77']]`
  - `CONDITIONAL_JUMP` [`006acd74`](#insn-006acd74) → [`006acec0`](#insn-006acec0)
  - `FALL_THROUGH` [`006acd74`](#insn-006acd74) → [`006acd78`](#insn-006acd78)
- ブロック [`006acd78`](#insn-006acd78) 範囲 `[['006acd78', '006acd7f']]`
  - `CONDITIONAL_JUMP` [`006acd7c`](#insn-006acd7c) → [`006acf0c`](#insn-006acf0c)
  - `FALL_THROUGH` [`006acd7c`](#insn-006acd7c) → [`006acd80`](#insn-006acd80)
- ブロック [`006acd80`](#insn-006acd80) 範囲 `[['006acd80', '006acd8f']]`
  - `FALL_THROUGH` [`006acd8c`](#insn-006acd8c) → [`006acd90`](#insn-006acd90)
- ブロック [`006acd90`](#insn-006acd90) 範囲 `[['006acd90', '006acdbb']]`
  - `UNCONDITIONAL_JUMP` [`006acdb8`](#insn-006acdb8) → [`006acef8`](#insn-006acef8)
- ブロック [`006acdbc`](#insn-006acdbc) 範囲 `[['006acdbc', '006acdc3']]`
  - `CONDITIONAL_JUMP` [`006acdc0`](#insn-006acdc0) → [`006acdcc`](#insn-006acdcc)
  - `FALL_THROUGH` [`006acdc0`](#insn-006acdc0) → [`006acdc4`](#insn-006acdc4)
- ブロック [`006acdc4`](#insn-006acdc4) 範囲 `[['006acdc4', '006acdc7']]`
  - `FALL_THROUGH` [`006acdc4`](#insn-006acdc4) → [`006acdc8`](#insn-006acdc8)
- ブロック [`006acdc8`](#insn-006acdc8) 範囲 `[['006acdc8', '006acdcb']]`
  - `CONDITIONAL_JUMP` [`006acdc8`](#insn-006acdc8) → [`006acf0c`](#insn-006acf0c)
  - `FALL_THROUGH` [`006acdc8`](#insn-006acdc8) → [`006acdcc`](#insn-006acdcc)
- ブロック [`006acdcc`](#insn-006acdcc) 範囲 `[['006acdcc', '006acde7']]`
  - `FALL_THROUGH` [`006acde4`](#insn-006acde4) → [`006acde8`](#insn-006acde8)
- ブロック [`006acde8`](#insn-006acde8) 範囲 `[['006acde8', '006acdef']]`
  - `FALL_THROUGH` [`006acdec`](#insn-006acdec) → [`006acdf0`](#insn-006acdf0)
- ブロック [`006acdf0`](#insn-006acdf0) 範囲 `[['006acdf0', '006acebf']]`
  - `UNCONDITIONAL_JUMP` [`006acebc`](#insn-006acebc) → [`006acf0c`](#insn-006acf0c)
- ブロック [`006acec0`](#insn-006acec0) 範囲 `[['006acec0', '006acef7']]`
  - `FALL_THROUGH` [`006acef4`](#insn-006acef4) → [`006acef8`](#insn-006acef8)
- ブロック [`006acef8`](#insn-006acef8) 範囲 `[['006acef8', '006acf0b']]`
  - `FALL_THROUGH` [`006acf08`](#insn-006acf08) → [`006acf0c`](#insn-006acf0c)
- ブロック [`006acf0c`](#insn-006acf0c) 範囲 `[['006acf0c', '006acf0f']]`
  - `FALL_THROUGH` [`006acf0c`](#insn-006acf0c) → [`006acf10`](#insn-006acf10)
- ブロック [`006acf10`](#insn-006acf10) 範囲 `[['006acf10', '006acf1f']]`
  - `CONDITIONAL_JUMP` [`006acf1c`](#insn-006acf1c) → [`006acf28`](#insn-006acf28)
  - `FALL_THROUGH` [`006acf1c`](#insn-006acf1c) → [`006acf20`](#insn-006acf20)
- ブロック [`006acf20`](#insn-006acf20) 範囲 `[['006acf20', '006acf27']]`
  - `FALL_THROUGH` [`006acf24`](#insn-006acf24) → [`006acf28`](#insn-006acf28)
- ブロック [`006acf28`](#insn-006acf28) 範囲 `[['006acf28', '006acf37']]`
  - `CONDITIONAL_JUMP` [`006acf34`](#insn-006acf34) → [`006acf58`](#insn-006acf58)
  - `FALL_THROUGH` [`006acf34`](#insn-006acf34) → [`006acf38`](#insn-006acf38)
- ブロック [`006acf38`](#insn-006acf38) 範囲 `[['006acf38', '006acf57']]`
- ブロック [`006acf58`](#insn-006acf58) 範囲 `[['006acf58', '006acf5b']]`

## 命令位置別の参照

- [`006acaf0`](#insn-006acaf0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acaf4`](#insn-006acaf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acaf8`](#insn-006acaf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acafc`](#insn-006acafc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb00`](#insn-006acb00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb04`](#insn-006acb04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb18`](#insn-006acb18) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb20`](#insn-006acb20) → `00ca4978`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006acb24`](#insn-006acb24) → [`006acb4c`](#insn-006acb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb2c`](#insn-006acb2c) → `00c65e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`006acb34`](#insn-006acb34) → `00c711c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`006acb40`](#insn-006acb40) → [`00c58610`](../00c58/00c58610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58610` · 推定シンボル `None` · 推定型 `None`
- [`006acb48`](#insn-006acb48) → [`006acb50`](#insn-006acb50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb50`](#insn-006acb50) → [`00467860`](../00467/00467860.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467860` · 推定シンボル `None` · 推定型 `None`
- [`006acb58`](#insn-006acb58) → [`006acf28`](#insn-006acf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb60`](#insn-006acb60) → [`006acf10`](#insn-006acf10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb6c`](#insn-006acb6c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006acb70`](#insn-006acb70) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`006acb78`](#insn-006acb78) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006acb7c`](#insn-006acb7c) → [`0046ca84`](../0046c/0046ca84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca84` · 推定シンボル `None` · 推定型 `None`
- [`006acbac`](#insn-006acbac) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`006acbb8`](#insn-006acbb8) → [`006acc48`](#insn-006acc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acbc4`](#insn-006acbc4) → [`00467af0`](../00467/00467af0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467af0` · 推定シンボル `None` · 推定型 `None`
- [`006acbdc`](#insn-006acbdc) → [`00467b2c`](../00467/00467b2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b2c` · 推定シンボル `None` · 推定型 `None`
- [`006acbe0`](#insn-006acbe0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006acbec`](#insn-006acbec) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`006acbf4`](#insn-006acbf4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006acbf8`](#insn-006acbf8) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`006acc00`](#insn-006acc00) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006acc04`](#insn-006acc04) → [`0046ca84`](../0046c/0046ca84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca84` · 推定シンボル `None` · 推定型 `None`
- [`006acc1c`](#insn-006acc1c) → [`00467f54`](../00467/00467f54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467f54` · 推定シンボル `None` · 推定型 `None`
- [`006acc34`](#insn-006acc34) → [`00467b2c`](../00467/00467b2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b2c` · 推定シンボル `None` · 推定型 `None`
- [`006acc40`](#insn-006acc40) → [`00467af0`](../00467/00467af0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467af0` · 推定シンボル `None` · 推定型 `None`
- [`006acc68`](#insn-006acc68) → [`004700b4`](../00470/004700b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004700b4` · 推定シンボル `None` · 推定型 `None`
- [`006acc78`](#insn-006acc78) → [`0047012c`](../00470/0047012c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047012c` · 推定シンボル `None` · 推定型 `None`
- [`006acc7c`](#insn-006acc7c) → [`0046e7ac`](../0046e/0046e7ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e7ac` · 推定シンボル `None` · 推定型 `None`
- [`006acc94`](#insn-006acc94) → [`0047012c`](../00470/0047012c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047012c` · 推定シンボル `None` · 推定型 `None`
- [`006acc98`](#insn-006acc98) → [`0046e7b4`](../0046e/0046e7b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e7b4` · 推定シンボル `None` · 推定型 `None`
- [`006accb0`](#insn-006accb0) → [`0047012c`](../00470/0047012c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047012c` · 推定シンボル `None` · 推定型 `None`
- [`006accb4`](#insn-006accb4) → [`0046e7bc`](../0046e/0046e7bc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e7bc` · 推定シンボル `None` · 推定型 `None`
- [`006acccc`](#insn-006acccc) → [`0046e72c`](../0046e/0046e72c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e72c` · 推定シンボル `None` · 推定型 `None`
- [`006accd0`](#insn-006accd0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006accd4`](#insn-006accd4) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`006acce4`](#insn-006acce4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006acd4c`](#insn-006acd4c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd60`](#insn-006acd60) → [`0046bd54`](../0046b/0046bd54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046bd54` · 推定シンボル `None` · 推定型 `None`
- [`006acd6c`](#insn-006acd6c) → [`006acdbc`](#insn-006acdbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd74`](#insn-006acd74) → [`006acec0`](#insn-006acec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd7c`](#insn-006acd7c) → [`006acf0c`](#insn-006acf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd90`](#insn-006acd90) → [`004700b4`](../00470/004700b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004700b4` · 推定シンボル `None` · 推定型 `None`
- [`006acd94`](#insn-006acd94) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006acd98`](#insn-006acd98) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`006acda8`](#insn-006acda8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006acdac`](#insn-006acdac) → [`0046ca84`](../0046c/0046ca84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca84` · 推定シンボル `None` · 推定型 `None`
- [`006acdb8`](#insn-006acdb8) → [`006acef8`](#insn-006acef8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acdc0`](#insn-006acdc0) → [`006acdcc`](#insn-006acdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acdc8`](#insn-006acdc8) → [`006acf0c`](#insn-006acf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acddc`](#insn-006acddc) → [`004700b4`](../00470/004700b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004700b4` · 推定シンボル `None` · 推定型 `None`
- [`006acde0`](#insn-006acde0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006acde4`](#insn-006acde4) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`006acdf4`](#insn-006acdf4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006acdf8`](#insn-006acdf8) → [`0046ca84`](../0046c/0046ca84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca84` · 推定シンボル `None` · 推定型 `None`
- [`006ace14`](#insn-006ace14) → [`0046bd54`](../0046b/0046bd54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046bd54` · 推定シンボル `None` · 推定型 `None`
- [`006ace1c`](#insn-006ace1c) → [`006c119c`](../006c1/006c119c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006c119c` · 推定シンボル `None` · 推定型 `None`
- [`006ace24`](#insn-006ace24) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006ace28`](#insn-006ace28) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`006ace54`](#insn-006ace54) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`006ace5c`](#insn-006ace5c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006ace60`](#insn-006ace60) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`006ace88`](#insn-006ace88) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`006ace90`](#insn-006ace90) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006ace94`](#insn-006ace94) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`006aceb8`](#insn-006aceb8) → [`004688b8`](../00468/004688b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004688b8` · 推定シンボル `None` · 推定型 `None`
- [`006acebc`](#insn-006acebc) → [`006acf0c`](#insn-006acf0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006aced0`](#insn-006aced0) → [`004700b4`](../00470/004700b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004700b4` · 推定シンボル `None` · 推定型 `None`
- [`006aced4`](#insn-006aced4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006aced8`](#insn-006aced8) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`006acee8`](#insn-006acee8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`006aceec`](#insn-006aceec) → [`0046ca84`](../0046c/0046ca84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca84` · 推定シンボル `None` · 推定型 `None`
- [`006acf08`](#insn-006acf08) → [`0046bd54`](../0046b/0046bd54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046bd54` · 推定シンボル `None` · 推定型 `None`
- [`006acf0c`](#insn-006acf0c) → [`006acf5c`](006acf5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006acf5c` · 推定シンボル `None` · 推定型 `None`
- [`006acf1c`](#insn-006acf1c) → [`006acf28`](#insn-006acf28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf24`](#insn-006acf24) → [`006ad414`](../006ad/006ad414.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006ad414` · 推定シンボル `None` · 推定型 `None`
- [`006acf2c`](#insn-006acf2c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf34`](#insn-006acf34) → [`006acf58`](#insn-006acf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf38`](#insn-006acf38) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf3c`](#insn-006acf3c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf40`](#insn-006acf40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf44`](#insn-006acf44) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf48`](#insn-006acf48) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf4c`](#insn-006acf4c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf58`](#insn-006acf58) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006acaf0`](#insn-006acaf0)

~~~json
{
  "source": "006acaf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acaf4`](#insn-006acaf4)

~~~json
{
  "source": "006acaf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acaf8`](#insn-006acaf8)

~~~json
{
  "source": "006acaf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acafc`](#insn-006acafc)

~~~json
{
  "source": "006acafc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb00`](#insn-006acb00)

~~~json
{
  "source": "006acb00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb04`](#insn-006acb04)

~~~json
{
  "source": "006acb04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb18`](#insn-006acb18)

~~~json
{
  "source": "006acb18",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb20`](#insn-006acb20)

~~~json
{
  "source": "006acb20",
  "target": "00ca4978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4978",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006acb24`](#insn-006acb24)

~~~json
{
  "source": "006acb24",
  "target": "006acb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb2c`](#insn-006acb2c)

~~~json
{
  "source": "006acb2c",
  "target": "00c65e58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65e58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006acb34`](#insn-006acb34)

~~~json
{
  "source": "006acb34",
  "target": "00c711c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c711c0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006acb40`](#insn-006acb40)

~~~json
{
  "source": "006acb40",
  "target": "00c58610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb48`](#insn-006acb48)

~~~json
{
  "source": "006acb48",
  "target": "006acb50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb50`](#insn-006acb50)

~~~json
{
  "source": "006acb50",
  "target": "00467860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb58`](#insn-006acb58)

~~~json
{
  "source": "006acb58",
  "target": "006acf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb60`](#insn-006acb60)

~~~json
{
  "source": "006acb60",
  "target": "006acf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb6c`](#insn-006acb6c)

~~~json
{
  "source": "006acb6c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb70`](#insn-006acb70)

~~~json
{
  "source": "006acb70",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb78`](#insn-006acb78)

~~~json
{
  "source": "006acb78",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb7c`](#insn-006acb7c)

~~~json
{
  "source": "006acb7c",
  "target": "0046ca84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbac`](#insn-006acbac)

~~~json
{
  "source": "006acbac",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbb8`](#insn-006acbb8)

~~~json
{
  "source": "006acbb8",
  "target": "006acc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acbc4`](#insn-006acbc4)

~~~json
{
  "source": "006acbc4",
  "target": "00467af0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbdc`](#insn-006acbdc)

~~~json
{
  "source": "006acbdc",
  "target": "00467b2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbe0`](#insn-006acbe0)

~~~json
{
  "source": "006acbe0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbec`](#insn-006acbec)

~~~json
{
  "source": "006acbec",
  "target": "003339e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4c26a00f4780900",
  "capture_start": "003339e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006acbf4`](#insn-006acbf4)

~~~json
{
  "source": "006acbf4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbf8`](#insn-006acbf8)

~~~json
{
  "source": "006acbf8",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc00`](#insn-006acc00)

~~~json
{
  "source": "006acc00",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc04`](#insn-006acc04)

~~~json
{
  "source": "006acc04",
  "target": "0046ca84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc1c`](#insn-006acc1c)

~~~json
{
  "source": "006acc1c",
  "target": "00467f54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc34`](#insn-006acc34)

~~~json
{
  "source": "006acc34",
  "target": "00467b2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc40`](#insn-006acc40)

~~~json
{
  "source": "006acc40",
  "target": "00467af0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc68`](#insn-006acc68)

~~~json
{
  "source": "006acc68",
  "target": "004700b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc78`](#insn-006acc78)

~~~json
{
  "source": "006acc78",
  "target": "0047012c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc7c`](#insn-006acc7c)

~~~json
{
  "source": "006acc7c",
  "target": "0046e7ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc94`](#insn-006acc94)

~~~json
{
  "source": "006acc94",
  "target": "0047012c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc98`](#insn-006acc98)

~~~json
{
  "source": "006acc98",
  "target": "0046e7b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006accb0`](#insn-006accb0)

~~~json
{
  "source": "006accb0",
  "target": "0047012c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006accb4`](#insn-006accb4)

~~~json
{
  "source": "006accb4",
  "target": "0046e7bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acccc`](#insn-006acccc)

~~~json
{
  "source": "006acccc",
  "target": "0046e72c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006accd0`](#insn-006accd0)

~~~json
{
  "source": "006accd0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006accd4`](#insn-006accd4)

~~~json
{
  "source": "006accd4",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acce4`](#insn-006acce4)

~~~json
{
  "source": "006acce4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acd4c`](#insn-006acd4c)

~~~json
{
  "source": "006acd4c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd60`](#insn-006acd60)

~~~json
{
  "source": "006acd60",
  "target": "0046bd54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acd6c`](#insn-006acd6c)

~~~json
{
  "source": "006acd6c",
  "target": "006acdbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd74`](#insn-006acd74)

~~~json
{
  "source": "006acd74",
  "target": "006acec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd7c`](#insn-006acd7c)

~~~json
{
  "source": "006acd7c",
  "target": "006acf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd90`](#insn-006acd90)

~~~json
{
  "source": "006acd90",
  "target": "004700b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acd94`](#insn-006acd94)

~~~json
{
  "source": "006acd94",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acd98`](#insn-006acd98)

~~~json
{
  "source": "006acd98",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acda8`](#insn-006acda8)

~~~json
{
  "source": "006acda8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acdac`](#insn-006acdac)

~~~json
{
  "source": "006acdac",
  "target": "0046ca84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acdb8`](#insn-006acdb8)

~~~json
{
  "source": "006acdb8",
  "target": "006acef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acdc0`](#insn-006acdc0)

~~~json
{
  "source": "006acdc0",
  "target": "006acdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acdc8`](#insn-006acdc8)

~~~json
{
  "source": "006acdc8",
  "target": "006acf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acddc`](#insn-006acddc)

~~~json
{
  "source": "006acddc",
  "target": "004700b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acde0`](#insn-006acde0)

~~~json
{
  "source": "006acde0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acde4`](#insn-006acde4)

~~~json
{
  "source": "006acde4",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acdf4`](#insn-006acdf4)

~~~json
{
  "source": "006acdf4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acdf8`](#insn-006acdf8)

~~~json
{
  "source": "006acdf8",
  "target": "0046ca84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace14`](#insn-006ace14)

~~~json
{
  "source": "006ace14",
  "target": "0046bd54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace1c`](#insn-006ace1c)

~~~json
{
  "source": "006ace1c",
  "target": "006c119c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace24`](#insn-006ace24)

~~~json
{
  "source": "006ace24",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace28`](#insn-006ace28)

~~~json
{
  "source": "006ace28",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace54`](#insn-006ace54)

~~~json
{
  "source": "006ace54",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace5c`](#insn-006ace5c)

~~~json
{
  "source": "006ace5c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace60`](#insn-006ace60)

~~~json
{
  "source": "006ace60",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace88`](#insn-006ace88)

~~~json
{
  "source": "006ace88",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace90`](#insn-006ace90)

~~~json
{
  "source": "006ace90",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace94`](#insn-006ace94)

~~~json
{
  "source": "006ace94",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aceb8`](#insn-006aceb8)

~~~json
{
  "source": "006aceb8",
  "target": "004688b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acebc`](#insn-006acebc)

~~~json
{
  "source": "006acebc",
  "target": "006acf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006aced0`](#insn-006aced0)

~~~json
{
  "source": "006aced0",
  "target": "004700b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aced4`](#insn-006aced4)

~~~json
{
  "source": "006aced4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aced8`](#insn-006aced8)

~~~json
{
  "source": "006aced8",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acee8`](#insn-006acee8)

~~~json
{
  "source": "006acee8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aceec`](#insn-006aceec)

~~~json
{
  "source": "006aceec",
  "target": "0046ca84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acf08`](#insn-006acf08)

~~~json
{
  "source": "006acf08",
  "target": "0046bd54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acf0c`](#insn-006acf0c)

~~~json
{
  "source": "006acf0c",
  "target": "006acf5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acf1c`](#insn-006acf1c)

~~~json
{
  "source": "006acf1c",
  "target": "006acf28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf24`](#insn-006acf24)

~~~json
{
  "source": "006acf24",
  "target": "006ad414",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acf2c`](#insn-006acf2c)

~~~json
{
  "source": "006acf2c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf34`](#insn-006acf34)

~~~json
{
  "source": "006acf34",
  "target": "006acf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf38`](#insn-006acf38)

~~~json
{
  "source": "006acf38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf3c`](#insn-006acf3c)

~~~json
{
  "source": "006acf3c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf40`](#insn-006acf40)

~~~json
{
  "source": "006acf40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf44`](#insn-006acf44)

~~~json
{
  "source": "006acf44",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf48`](#insn-006acf48)

~~~json
{
  "source": "006acf48",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf4c`](#insn-006acf4c)

~~~json
{
  "source": "006acf4c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf58`](#insn-006acf58)

~~~json
{
  "source": "006acf58",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
