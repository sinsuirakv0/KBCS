# 006acaac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00686764`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00686/00686764.md) · 移動量 `+0x26348`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0029.md#compare-509160cc66480d2d9103d8dfe1588c41)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `006acaec`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/006ac/006acaec.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0031.md#compare-abb839cb61b4f6646263482b8fd1e65b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006acaac",
  "name": "FUN_006acaac",
  "size": 1136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "35cfd09fdffe131baaa881c3199bc1a7cde624f1fdfe13ecc81ff8f27fb7d64a",
  "source_text_sha256": "35cfd09fdffe131baaa881c3199bc1a7cde624f1fdfe13ecc81ff8f27fb7d64a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006acaac",
        "006acf1b"
      ]
    ],
    "bytes_sha256": "ea13409b6e4ddcb88c3376516e8ea1e6db6812d9e1d177b234f5ca8cd9fcbd40",
    "instruction_count": 284,
    "instruction_bytes": 1136,
    "body_bytes": 1136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00996ea0](../00996/00996ea0.md)

## 呼び出し先

- [00467820](../00467/00467820.md)
- [00467ab0](../00467/00467ab0.md)
- [00467aec](../00467/00467aec.md)
- [00467f14](../00467/00467f14.md)
- [00468878](../00468/00468878.md)
- [00469bc4](../00469/00469bc4.md)
- [0046bd14](../0046b/0046bd14.md)
- [0046c984](../0046c/0046c984.md)
- [0046ca44](../0046c/0046ca44.md)
- [0046e6ec](../0046e/0046e6ec.md)
- [0046e76c](../0046e/0046e76c.md)
- [0046e774](../0046e/0046e774.md)
- [0046e77c](../0046e/0046e77c.md)
- [00470074](../00470/00470074.md)
- [004700ec](../00470/004700ec.md)
- [006acf1c](../006ac/006acf1c.md)
- [006ad3d4](../006ad/006ad3d4.md)
- [006c115c](../006c1/006c115c.md)
- [008514b8](../00851/008514b8.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c58210](../00c58/00c58210.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6866 bytes

~~~c

void FUN_006acaac(char *param_1)

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
  if (DAT_00ca4578 == 0) {
    lVar8 = 0;
  }
  else {
    lVar8 = __dynamic_cast(DAT_00ca4578,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65a58,
                           &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c70dc0,0);
  }
  uVar9 = FUN_00467820();
  if (*param_1 == '\0') goto LAB_006acee8;
  if ((param_1[0x4e0] & 1U) == 0) {
    uVar12 = *(undefined8 *)(param_1 + 0x208);
                    /* try { // try from 006acb2c to 007acb33 has its CatchHandler @ 006acda8 */
    FUN_008514b8();
    uVar3 = FUN_0046c984();
    FUN_008514b8();
    uVar4 = FUN_0046ca44();
                    /* try { // try from 006acb54 to 007acb7f has its CatchHandler @ 006acdb0 */
    uVar5 = 0x62;
    if (*(int *)(param_1 + 0x4e8) != 3) {
      uVar5 = 2;
    }
    FUN_00469bc4(uVar9,uVar12,0,0,uVar3,uVar4,uVar5);
    iVar6 = *(int *)(param_1 + 0x4ec);
    if (iVar6 == 1) {
                    /* try { // try from 006acb80 to 007acbf7 has its CatchHandler @ 006aca04 */
      FUN_00467ab0(uVar9,1);
      FUN_00467aec(uVar9,0xab,0x2c,0,0x40);
      lVar10 = FUN_008514b8();
      iVar6 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar10);
      FUN_008514b8();
      uVar5 = FUN_0046c984();
      FUN_008514b8();
      uVar3 = FUN_0046ca44();
      FUN_00467f14(uVar9,0,-iVar6,uVar5,uVar3);
      FUN_00467aec(uVar9,0xff,0xff,0xff,0xff);
                    /* try { // try from 006acbf8 to 007acbff has its CatchHandler @ 006acd38 */
      FUN_00467ab0(uVar9,0);
                    /* try { // try from 006acc04 to 007acc0b has its CatchHandler @ 006acd88 */
      iVar6 = *(int *)(param_1 + 0x4ec);
    }
    FUN_00470074(param_1 + (long)iVar6 * 0xa8 + 0x38,param_1 + (long)iVar6 * 0x38 + 0x188,
                 *(undefined4 *)(param_1 + 0x4f4),0);
    FUN_004700ec(param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,0);
    uVar12 = FUN_0046e76c();
    iVar6 = *(int *)(param_1 + 0x4ec);
                    /* try { // try from 006acc48 to 007acc4f has its CatchHandler @ 006acd18 */
    FUN_004700ec(param_1 + (long)iVar6 * 0xa8 + 0x38,1);
    uVar5 = FUN_0046e774();
                    /* try { // try from 006acc5c to 007acc6b has its CatchHandler @ 006acd50 */
                    /* try { // try from 006acc6c to 007acdef has its CatchHandler @ 006aca04 */
    FUN_004700ec(param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,1);
    uVar3 = FUN_0046e77c();
    FUN_0046e6ec(uVar12,param_1 + (long)iVar6 * 0xa8 + 0x38,uVar5,uVar3,&local_70);
    FUN_008514b8();
    iVar6 = FUN_0046c984();
    if (iVar6 < 0) {
      iVar6 = iVar6 + 1;
    }
    lVar10 = FUN_008514b8();
    lVar10 = lVar10 + (long)*(int *)(param_1 + 0x4e4) * 0x100;
    pbVar1 = (byte *)(lVar10 + 0x4b278 +
                     (long)(*(int *)(param_1 + 0x4e8) + *(int *)(param_1 + 0x4ec) + 0x33) * 4);
                    /* catch() { ... } // from try @ 006acc48 with catch @ 006acd18 */
    FUN_0046bd14(uVar9,param_1 + (long)*(int *)(param_1 + 0x4ec) * 0xa8 + 0x38,
                 (iVar6 >> 1) - local_70,
                 ((uint)CONCAT12(*(byte *)(lVar10 + 0x4b376) ^ pbVar1[2],
                                 CONCAT11(*(byte *)(lVar10 + 0x4b375) ^ pbVar1[1],
                                          *(byte *)(lVar10 + 0x4b374) ^ *pbVar1)) - iStack_6c) +
                 (uint)(*(byte *)(lVar10 + 0x4b377) ^ pbVar1[3]) * 0x1000000 + 0x1d4);
    iVar6 = *(int *)(param_1 + 0x4f0);
    if (iVar6 < 3) {
      if (iVar6 == 1) {
                    /* try { // try from 006ace80 to 007acf53 has its CatchHandler @ 006ace80
                       catch() { ... } // from try @ 006ace80 with catch @ 006ace80
                       catch() { ... } // from try @ 006acf80 with catch @ 006ace80
                       catch() { ... } // from try @ 006ad0a8 with catch @ 006ace80 */
        FUN_00470074(param_1 + 0x268,param_1 + 0x310,*(undefined4 *)(param_1 + 0x4f8),0);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_008514b8();
        iVar7 = FUN_0046ca44();
        pcVar11 = param_1 + 0x268;
      }
      else {
                    /* catch() { ... } // from try @ 006acbf8 with catch @ 006acd38 */
        if (iVar6 != 2) goto LAB_006acecc;
                    /* catch() { ... } // from try @ 006acc5c with catch @ 006acd50 */
        FUN_00470074(param_1 + 0x380,param_1 + 0x428,*(undefined4 *)(param_1 + 0x4fc),0);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_008514b8();
        iVar7 = FUN_0046ca44();
        pcVar11 = param_1 + 0x380;
      }
      if (iVar7 < 0) {
        iVar7 = iVar7 + 1;
      }
      FUN_0046bd14(uVar9,pcVar11,iVar6 >> 1,iVar7 >> 1);
    }
    else {
                    /* catch() { ... } // from try @ 006acc04 with catch @ 006acd88 */
      if ((iVar6 == 3) || (iVar6 == 4)) {
        FUN_00470074(param_1 + 0x380,param_1 + 0x428,*(undefined4 *)(param_1 + 0x4fc),0);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
                    /* catch() { ... } // from try @ 006acb2c with catch @ 006acda8 */
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
                    /* catch() { ... } // from try @ 006acb54 with catch @ 006acdb0 */
        FUN_008514b8();
        iVar7 = FUN_0046ca44();
        if (iVar7 < 0) {
          iVar7 = iVar7 + 1;
        }
        FUN_0046bd14(uVar9,param_1 + 0x380,iVar6 >> 1,iVar7 >> 1);
        FUN_006c115c(param_1 + 0x460);
        uVar12 = *(undefined8 *)(lVar8 + 8);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_00469bc4(uVar9,uVar12,(iVar6 >> 1) + -0xd7,0x1f8,0xdc,0x3e,1);
        uVar12 = *(undefined8 *)(lVar8 + 8);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_00469bc4(uVar9,uVar12,iVar6 >> 1,0x1f8,0xdc,0x3e,2);
        uVar12 = *(undefined8 *)(param_1 + 0x1f8);
        FUN_008514b8();
        iVar6 = FUN_0046c984();
        if (iVar6 < 0) {
          iVar6 = iVar6 + 1;
        }
        FUN_00468878(uVar9,uVar12,iVar6 >> 1,0x217,0x1a4,5);
      }
    }
LAB_006acecc:
    FUN_006acf1c();
  }
  if ((*(uint *)(param_1 + 0x4f0) | 4) == 4) {
    FUN_006ad3d4(param_1);
  }
LAB_006acee8:
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
<a id="insn-006acaac"></a> `006acaac` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-006acab0"></a> `006acab0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006acab4"></a> `006acab4` | `fb 13 00 f9` | str x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006acab8"></a> `006acab8` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006acabc"></a> `006acabc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006acac0"></a> `006acac0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006acac4"></a> `006acac4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006acac8"></a> `006acac8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-006acacc"></a> `006acacc` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-006acad0"></a> `006acad0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006acad4"></a> `006acad4` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-006acad8"></a> `006acad8` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006acadc"></a> `006acadc` | `c8 2f 00 90` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-006acae0"></a> `006acae0` | `08 bd 42 f9` | ldr x8,[x8, #0x578] | `FALL_THROUGH`
<a id="insn-006acae4"></a> `006acae4` | `48 01 00 b4` | cbz x8,0x006acb0c | `CONDITIONAL_JUMP`
<a id="insn-006acae8"></a> `006acae8` | `c1 2d 00 b0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-006acaec"></a> `006acaec` | `21 60 29 91` | add x1,x1,#0xa58 | `FALL_THROUGH`
<a id="insn-006acaf0"></a> `006acaf0` | `22 2e 00 90` | adrp x2,0xc70000 | `FALL_THROUGH`
<a id="insn-006acaf4"></a> `006acaf4` | `42 00 37 91` | add x2,x2,#0xdc0 | `FALL_THROUGH`
<a id="insn-006acaf8"></a> `006acaf8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-006acafc"></a> `006acafc` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-006acb00"></a> `006acb00` | `c4 ad 16 94` | bl 0x00c58210 | `UNCONDITIONAL_CALL`
<a id="insn-006acb04"></a> `006acb04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-006acb08"></a> `006acb08` | `02 00 00 14` | b 0x006acb10 | `UNCONDITIONAL_JUMP`
<a id="insn-006acb0c"></a> `006acb0c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-006acb10"></a> `006acb10` | `44 eb f6 97` | bl 0x00467820 | `UNCONDITIONAL_CALL`
<a id="insn-006acb14"></a> `006acb14` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-006acb18"></a> `006acb18` | `88 1e 00 34` | cbz w8,0x006acee8 | `CONDITIONAL_JUMP`
<a id="insn-006acb1c"></a> `006acb1c` | `68 82 53 39` | ldrb w8,[x19, #0x4e0] | `FALL_THROUGH`
<a id="insn-006acb20"></a> `006acb20` | `88 1d 00 37` | tbnz w8,#0x0,0x006aced0 | `CONDITIONAL_JUMP`
<a id="insn-006acb24"></a> `006acb24` | `76 06 41 f9` | ldr x22,[x19, #0x208] | `FALL_THROUGH`
<a id="insn-006acb28"></a> `006acb28` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-006acb2c"></a> `006acb2c` | `63 92 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acb30"></a> `006acb30` | `95 ff f6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-006acb34"></a> `006acb34` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-006acb38"></a> `006acb38` | `60 92 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acb3c"></a> `006acb3c` | `c2 ff f6 97` | bl 0x0046ca44 | `UNCONDITIONAL_CALL`
<a id="insn-006acb40"></a> `006acb40` | `68 ea 44 b9` | ldr w8,[x19, #0x4e8] | `FALL_THROUGH`
<a id="insn-006acb44"></a> `006acb44` | `49 0c 80 52` | mov w9,#0x62 | `FALL_THROUGH`
<a id="insn-006acb48"></a> `006acb48` | `e5 03 00 2a` | mov w5,w0 | `FALL_THROUGH`
<a id="insn-006acb4c"></a> `006acb4c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acb50"></a> `006acb50` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-006acb54"></a> `006acb54` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-006acb58"></a> `006acb58` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-006acb5c"></a> `006acb5c` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-006acb60"></a> `006acb60` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006acb64"></a> `006acb64` | `26 01 88 1a` | csel w6,w9,w8,eq | `FALL_THROUGH`
<a id="insn-006acb68"></a> `006acb68` | `e4 03 17 2a` | mov w4,w23 | `FALL_THROUGH`
<a id="insn-006acb6c"></a> `006acb6c` | `16 f4 f6 97` | bl 0x00469bc4 | `UNCONDITIONAL_CALL`
<a id="insn-006acb70"></a> `006acb70` | `68 ee 44 b9` | ldr w8,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006acb74"></a> `006acb74` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acb78"></a> `006acb78` | `81 04 00 54` | b.ne 0x006acc08 | `CONDITIONAL_JUMP`
<a id="insn-006acb7c"></a> `006acb7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acb80"></a> `006acb80` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-006acb84"></a> `006acb84` | `cb eb f6 97` | bl 0x00467ab0 | `UNCONDITIONAL_CALL`
<a id="insn-006acb88"></a> `006acb88` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acb8c"></a> `006acb8c` | `61 15 80 52` | mov w1,#0xab | `FALL_THROUGH`
<a id="insn-006acb90"></a> `006acb90` | `82 05 80 52` | mov w2,#0x2c | `FALL_THROUGH`
<a id="insn-006acb94"></a> `006acb94` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006acb98"></a> `006acb98` | `04 08 80 52` | mov w4,#0x40 | `FALL_THROUGH`
<a id="insn-006acb9c"></a> `006acb9c` | `d4 eb f6 97` | bl 0x00467aec | `UNCONDITIONAL_CALL`
<a id="insn-006acba0"></a> `006acba0` | `46 92 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acba4"></a> `006acba4` | `08 3d 87 52` | mov w8,#0x39e8 | `FALL_THROUGH`
<a id="insn-006acba8"></a> `006acba8` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-006acbac"></a> `006acbac` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006acbb0"></a> `006acbb0` | `f6 03 08 4b` | neg w22,w8 | `FALL_THROUGH`
<a id="insn-006acbb4"></a> `006acbb4` | `41 92 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acbb8"></a> `006acbb8` | `73 ff f6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-006acbbc"></a> `006acbbc` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-006acbc0"></a> `006acbc0` | `3e 92 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acbc4"></a> `006acbc4` | `a0 ff f6 97` | bl 0x0046ca44 | `UNCONDITIONAL_CALL`
<a id="insn-006acbc8"></a> `006acbc8` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-006acbcc"></a> `006acbcc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acbd0"></a> `006acbd0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006acbd4"></a> `006acbd4` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-006acbd8"></a> `006acbd8` | `e3 03 17 2a` | mov w3,w23 | `FALL_THROUGH`
<a id="insn-006acbdc"></a> `006acbdc` | `ce ec f6 97` | bl 0x00467f14 | `UNCONDITIONAL_CALL`
<a id="insn-006acbe0"></a> `006acbe0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acbe4"></a> `006acbe4` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-006acbe8"></a> `006acbe8` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-006acbec"></a> `006acbec` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-006acbf0"></a> `006acbf0` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-006acbf4"></a> `006acbf4` | `be eb f6 97` | bl 0x00467aec | `UNCONDITIONAL_CALL`
<a id="insn-006acbf8"></a> `006acbf8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acbfc"></a> `006acbfc` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006acc00"></a> `006acc00` | `ac eb f6 97` | bl 0x00467ab0 | `UNCONDITIONAL_CALL`
<a id="insn-006acc04"></a> `006acc04` | `68 ee 44 b9` | ldr w8,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006acc08"></a> `006acc08` | `1a 15 80 52` | mov w26,#0xa8 | `FALL_THROUGH`
<a id="insn-006acc0c"></a> `006acc0c` | `09 07 80 52` | mov w9,#0x38 | `FALL_THROUGH`
<a id="insn-006acc10"></a> `006acc10` | `7b e2 00 91` | add x27,x19,#0x38 | `FALL_THROUGH`
<a id="insn-006acc14"></a> `006acc14` | `00 6d 3a 9b` | smaddl x0,w8,w26,x27 | `FALL_THROUGH`
<a id="insn-006acc18"></a> `006acc18` | `62 f6 44 b9` | ldr w2,[x19, #0x4f4] | `FALL_THROUGH`
<a id="insn-006acc1c"></a> `006acc1c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006acc20"></a> `006acc20` | `08 4d 29 9b` | smaddl x8,w8,w9,x19 | `FALL_THROUGH`
<a id="insn-006acc24"></a> `006acc24` | `01 21 06 91` | add x1,x8,#0x188 | `FALL_THROUGH`
<a id="insn-006acc28"></a> `006acc28` | `13 0d f7 97` | bl 0x00470074 | `UNCONDITIONAL_CALL`
<a id="insn-006acc2c"></a> `006acc2c` | `68 ee 84 b9` | ldrsw x8,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006acc30"></a> `006acc30` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006acc34"></a> `006acc34` | `00 6d 3a 9b` | smaddl x0,w8,w26,x27 | `FALL_THROUGH`
<a id="insn-006acc38"></a> `006acc38` | `2d 0d f7 97` | bl 0x004700ec | `UNCONDITIONAL_CALL`
<a id="insn-006acc3c"></a> `006acc3c` | `cc 06 f7 97` | bl 0x0046e76c | `UNCONDITIONAL_CALL`
<a id="insn-006acc40"></a> `006acc40` | `68 ee 84 b9` | ldrsw x8,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006acc44"></a> `006acc44` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-006acc48"></a> `006acc48` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-006acc4c"></a> `006acc4c` | `16 6d 3a 9b` | smaddl x22,w8,w26,x27 | `FALL_THROUGH`
<a id="insn-006acc50"></a> `006acc50` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-006acc54"></a> `006acc54` | `26 0d f7 97` | bl 0x004700ec | `UNCONDITIONAL_CALL`
<a id="insn-006acc58"></a> `006acc58` | `c7 06 f7 97` | bl 0x0046e774 | `UNCONDITIONAL_CALL`
<a id="insn-006acc5c"></a> `006acc5c` | `68 ee 84 b9` | ldrsw x8,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006acc60"></a> `006acc60` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-006acc64"></a> `006acc64` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-006acc68"></a> `006acc68` | `08 6d 3a 9b` | smaddl x8,w8,w26,x27 | `FALL_THROUGH`
<a id="insn-006acc6c"></a> `006acc6c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-006acc70"></a> `006acc70` | `1f 0d f7 97` | bl 0x004700ec | `UNCONDITIONAL_CALL`
<a id="insn-006acc74"></a> `006acc74` | `c2 06 f7 97` | bl 0x0046e77c | `UNCONDITIONAL_CALL`
<a id="insn-006acc78"></a> `006acc78` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-006acc7c"></a> `006acc7c` | `e4 03 00 91` | mov x4,sp | `FALL_THROUGH`
<a id="insn-006acc80"></a> `006acc80` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-006acc84"></a> `006acc84` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-006acc88"></a> `006acc88` | `e2 03 18 2a` | mov w2,w24 | `FALL_THROUGH`
<a id="insn-006acc8c"></a> `006acc8c` | `98 06 f7 97` | bl 0x0046e6ec | `UNCONDITIONAL_CALL`
<a id="insn-006acc90"></a> `006acc90` | `0a 92 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acc94"></a> `006acc94` | `3c ff f6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-006acc98"></a> `006acc98` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acc9c"></a> `006acc9c` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acca0"></a> `006acca0` | `16 7d 01 13` | asr w22,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acca4"></a> `006acca4` | `05 92 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acca8"></a> `006acca8` | `68 e6 84 b9` | ldrsw x8,[x19, #0x4e4] | `FALL_THROUGH`
<a id="insn-006accac"></a> `006accac` | `69 ea 44 b9` | ldr w9,[x19, #0x4e8] | `FALL_THROUGH`
<a id="insn-006accb0"></a> `006accb0` | `6a ee 84 b9` | ldrsw x10,[x19, #0x4ec] | `FALL_THROUGH`
<a id="insn-006accb4"></a> `006accb4` | `08 20 08 8b` | add x8,x0,x8, LSL #0x8 | `FALL_THROUGH`
<a id="insn-006accb8"></a> `006accb8` | `29 01 0a 0b` | add w9,w9,w10 | `FALL_THROUGH`
<a id="insn-006accbc"></a> `006accbc` | `41 6d 3a 9b` | smaddl x1,w10,w26,x27 | `FALL_THROUGH`
<a id="insn-006accc0"></a> `006accc0` | `29 cd 00 11` | add w9,w9,#0x33 | `FALL_THROUGH`
<a id="insn-006accc4"></a> `006accc4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006accc8"></a> `006accc8` | `08 2d 41 91` | add x8,x8,#0x4b, LSL #12 | `FALL_THROUGH`
<a id="insn-006acccc"></a> `006acccc` | `08 e1 09 91` | add x8,x8,#0x278 | `FALL_THROUGH`
<a id="insn-006accd0"></a> `006accd0` | `09 c9 29 8b` | add x9,x8,w9, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-006accd4"></a> `006accd4` | `0b f1 43 39` | ldrb w11,[x8, #0xfc] | `FALL_THROUGH`
<a id="insn-006accd8"></a> `006accd8` | `0d f5 43 39` | ldrb w13,[x8, #0xfd] | `FALL_THROUGH`
<a id="insn-006accdc"></a> `006accdc` | `2c 01 40 39` | ldrb w12,[x9] | `FALL_THROUGH`
<a id="insn-006acce0"></a> `006acce0` | `2e 05 40 39` | ldrb w14,[x9, #0x1] | `FALL_THROUGH`
<a id="insn-006acce4"></a> `006acce4` | `6b 01 0c 4a` | eor w11,w11,w12 | `FALL_THROUGH`
<a id="insn-006acce8"></a> `006acce8` | `ac 01 0e 4a` | eor w12,w13,w14 | `FALL_THROUGH`
<a id="insn-006accec"></a> `006accec` | `2d 09 40 39` | ldrb w13,[x9, #0x2] | `FALL_THROUGH`
<a id="insn-006accf0"></a> `006accf0` | `0e f9 43 39` | ldrb w14,[x8, #0xfe] | `FALL_THROUGH`
<a id="insn-006accf4"></a> `006accf4` | `6b 21 0c 2a` | orr w11,w11,w12, LSL #0x8 | `FALL_THROUGH`
<a id="insn-006accf8"></a> `006accf8` | `29 0d 40 39` | ldrb w9,[x9, #0x3] | `FALL_THROUGH`
<a id="insn-006accfc"></a> `006accfc` | `08 fd 43 39` | ldrb w8,[x8, #0xff] | `FALL_THROUGH`
<a id="insn-006acd00"></a> `006acd00` | `cc 01 0d 4a` | eor w12,w14,w13 | `FALL_THROUGH`
<a id="insn-006acd04"></a> `006acd04` | `6b 41 0c 2a` | orr w11,w11,w12, LSL #0x10 | `FALL_THROUGH`
<a id="insn-006acd08"></a> `006acd08` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-006acd0c"></a> `006acd0c` | `ec 37 40 29` | ldp w12,w13,[sp] | `FALL_THROUGH`
<a id="insn-006acd10"></a> `006acd10` | `69 01 0d 4b` | sub w9,w11,w13 | `FALL_THROUGH`
<a id="insn-006acd14"></a> `006acd14` | `c2 02 0c 4b` | sub w2,w22,w12 | `FALL_THROUGH`
<a id="insn-006acd18"></a> `006acd18` | `28 61 08 0b` | add w8,w9,w8, LSL #0x18 | `FALL_THROUGH`
<a id="insn-006acd1c"></a> `006acd1c` | `03 51 07 11` | add w3,w8,#0x1d4 | `FALL_THROUGH`
<a id="insn-006acd20"></a> `006acd20` | `fd fb f6 97` | bl 0x0046bd14 | `UNCONDITIONAL_CALL`
<a id="insn-006acd24"></a> `006acd24` | `68 f2 44 b9` | ldr w8,[x19, #0x4f0] | `FALL_THROUGH`
<a id="insn-006acd28"></a> `006acd28` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-006acd2c"></a> `006acd2c` | `8c 02 00 54` | b.gt 0x006acd7c | `CONDITIONAL_JUMP`
<a id="insn-006acd30"></a> `006acd30` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acd34"></a> `006acd34` | `60 0a 00 54` | b.eq 0x006ace80 | `CONDITIONAL_JUMP`
<a id="insn-006acd38"></a> `006acd38` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-006acd3c"></a> `006acd3c` | `81 0c 00 54` | b.ne 0x006acecc | `CONDITIONAL_JUMP`
<a id="insn-006acd40"></a> `006acd40` | `62 fe 44 b9` | ldr w2,[x19, #0x4fc] | `FALL_THROUGH`
<a id="insn-006acd44"></a> `006acd44` | `60 02 0e 91` | add x0,x19,#0x380 | `FALL_THROUGH`
<a id="insn-006acd48"></a> `006acd48` | `61 a2 10 91` | add x1,x19,#0x428 | `FALL_THROUGH`
<a id="insn-006acd4c"></a> `006acd4c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006acd50"></a> `006acd50` | `c9 0c f7 97` | bl 0x00470074 | `UNCONDITIONAL_CALL`
<a id="insn-006acd54"></a> `006acd54` | `d9 91 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acd58"></a> `006acd58` | `0b ff f6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-006acd5c"></a> `006acd5c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acd60"></a> `006acd60` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acd64"></a> `006acd64` | `15 7d 01 13` | asr w21,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acd68"></a> `006acd68` | `d4 91 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acd6c"></a> `006acd6c` | `36 ff f6 97` | bl 0x0046ca44 | `UNCONDITIONAL_CALL`
<a id="insn-006acd70"></a> `006acd70` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acd74"></a> `006acd74` | `61 02 0e 91` | add x1,x19,#0x380 | `FALL_THROUGH`
<a id="insn-006acd78"></a> `006acd78` | `50 00 00 14` | b 0x006aceb8 | `UNCONDITIONAL_JUMP`
<a id="insn-006acd7c"></a> `006acd7c` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-006acd80"></a> `006acd80` | `60 00 00 54` | b.eq 0x006acd8c | `CONDITIONAL_JUMP`
<a id="insn-006acd84"></a> `006acd84` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-006acd88"></a> `006acd88` | `21 0a 00 54` | b.ne 0x006acecc | `CONDITIONAL_JUMP`
<a id="insn-006acd8c"></a> `006acd8c` | `62 fe 44 b9` | ldr w2,[x19, #0x4fc] | `FALL_THROUGH`
<a id="insn-006acd90"></a> `006acd90` | `60 02 0e 91` | add x0,x19,#0x380 | `FALL_THROUGH`
<a id="insn-006acd94"></a> `006acd94` | `61 a2 10 91` | add x1,x19,#0x428 | `FALL_THROUGH`
<a id="insn-006acd98"></a> `006acd98` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006acd9c"></a> `006acd9c` | `b6 0c f7 97` | bl 0x00470074 | `UNCONDITIONAL_CALL`
<a id="insn-006acda0"></a> `006acda0` | `c6 91 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acda4"></a> `006acda4` | `f8 fe f6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-006acda8"></a> `006acda8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acdac"></a> `006acdac` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acdb0"></a> `006acdb0` | `16 7d 01 13` | asr w22,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acdb4"></a> `006acdb4` | `c1 91 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acdb8"></a> `006acdb8` | `23 ff f6 97` | bl 0x0046ca44 | `UNCONDITIONAL_CALL`
<a id="insn-006acdbc"></a> `006acdbc` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acdc0"></a> `006acdc0` | `61 02 0e 91` | add x1,x19,#0x380 | `FALL_THROUGH`
<a id="insn-006acdc4"></a> `006acdc4` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-006acdc8"></a> `006acdc8` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acdcc"></a> `006acdcc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acdd0"></a> `006acdd0` | `03 7d 01 13` | asr w3,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acdd4"></a> `006acdd4` | `d0 fb f6 97` | bl 0x0046bd14 | `UNCONDITIONAL_CALL`
<a id="insn-006acdd8"></a> `006acdd8` | `60 82 11 91` | add x0,x19,#0x460 | `FALL_THROUGH`
<a id="insn-006acddc"></a> `006acddc` | `e0 50 00 94` | bl 0x006c115c | `UNCONDITIONAL_CALL`
<a id="insn-006acde0"></a> `006acde0` | `b6 06 40 f9` | ldr x22,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-006acde4"></a> `006acde4` | `b5 91 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006acde8"></a> `006acde8` | `e7 fe f6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-006acdec"></a> `006acdec` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acdf0"></a> `006acdf0` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-006acdf4"></a> `006acdf4` | `03 3f 80 52` | mov w3,#0x1f8 | `FALL_THROUGH`
<a id="insn-006acdf8"></a> `006acdf8` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acdfc"></a> `006acdfc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006ace00"></a> `006ace00` | `84 1b 80 52` | mov w4,#0xdc | `FALL_THROUGH`
<a id="insn-006ace04"></a> `006ace04` | `08 7d 01 13` | asr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006ace08"></a> `006ace08` | `c5 07 80 52` | mov w5,#0x3e | `FALL_THROUGH`
<a id="insn-006ace0c"></a> `006ace0c` | `26 00 80 52` | mov w6,#0x1 | `FALL_THROUGH`
<a id="insn-006ace10"></a> `006ace10` | `02 5d 03 51` | sub w2,w8,#0xd7 | `FALL_THROUGH`
<a id="insn-006ace14"></a> `006ace14` | `6c f3 f6 97` | bl 0x00469bc4 | `UNCONDITIONAL_CALL`
<a id="insn-006ace18"></a> `006ace18` | `b5 06 40 f9` | ldr x21,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-006ace1c"></a> `006ace1c` | `a7 91 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006ace20"></a> `006ace20` | `d9 fe f6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-006ace24"></a> `006ace24` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006ace28"></a> `006ace28` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-006ace2c"></a> `006ace2c` | `03 3f 80 52` | mov w3,#0x1f8 | `FALL_THROUGH`
<a id="insn-006ace30"></a> `006ace30` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006ace34"></a> `006ace34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006ace38"></a> `006ace38` | `84 1b 80 52` | mov w4,#0xdc | `FALL_THROUGH`
<a id="insn-006ace3c"></a> `006ace3c` | `02 7d 01 13` | asr w2,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006ace40"></a> `006ace40` | `c5 07 80 52` | mov w5,#0x3e | `FALL_THROUGH`
<a id="insn-006ace44"></a> `006ace44` | `46 00 80 52` | mov w6,#0x2 | `FALL_THROUGH`
<a id="insn-006ace48"></a> `006ace48` | `5f f3 f6 97` | bl 0x00469bc4 | `UNCONDITIONAL_CALL`
<a id="insn-006ace4c"></a> `006ace4c` | `75 fe 40 f9` | ldr x21,[x19, #0x1f8] | `FALL_THROUGH`
<a id="insn-006ace50"></a> `006ace50` | `9a 91 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006ace54"></a> `006ace54` | `cc fe f6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-006ace58"></a> `006ace58` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006ace5c"></a> `006ace5c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-006ace60"></a> `006ace60` | `e3 42 80 52` | mov w3,#0x217 | `FALL_THROUGH`
<a id="insn-006ace64"></a> `006ace64` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006ace68"></a> `006ace68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006ace6c"></a> `006ace6c` | `84 34 80 52` | mov w4,#0x1a4 | `FALL_THROUGH`
<a id="insn-006ace70"></a> `006ace70` | `02 7d 01 13` | asr w2,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006ace74"></a> `006ace74` | `a5 00 80 52` | mov w5,#0x5 | `FALL_THROUGH`
<a id="insn-006ace78"></a> `006ace78` | `80 ee f6 97` | bl 0x00468878 | `UNCONDITIONAL_CALL`
<a id="insn-006ace7c"></a> `006ace7c` | `14 00 00 14` | b 0x006acecc | `UNCONDITIONAL_JUMP`
<a id="insn-006ace80"></a> `006ace80` | `62 fa 44 b9` | ldr w2,[x19, #0x4f8] | `FALL_THROUGH`
<a id="insn-006ace84"></a> `006ace84` | `60 a2 09 91` | add x0,x19,#0x268 | `FALL_THROUGH`
<a id="insn-006ace88"></a> `006ace88` | `61 42 0c 91` | add x1,x19,#0x310 | `FALL_THROUGH`
<a id="insn-006ace8c"></a> `006ace8c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-006ace90"></a> `006ace90` | `79 0c f7 97` | bl 0x00470074 | `UNCONDITIONAL_CALL`
<a id="insn-006ace94"></a> `006ace94` | `89 91 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006ace98"></a> `006ace98` | `bb fe f6 97` | bl 0x0046c984 | `UNCONDITIONAL_CALL`
<a id="insn-006ace9c"></a> `006ace9c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006acea0"></a> `006acea0` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acea4"></a> `006acea4` | `15 7d 01 13` | asr w21,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acea8"></a> `006acea8` | `84 91 06 94` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-006aceac"></a> `006aceac` | `e6 fe f6 97` | bl 0x0046ca44 | `UNCONDITIONAL_CALL`
<a id="insn-006aceb0"></a> `006aceb0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-006aceb4"></a> `006aceb4` | `61 a2 09 91` | add x1,x19,#0x268 | `FALL_THROUGH`
<a id="insn-006aceb8"></a> `006aceb8` | `08 a4 80 1a` | cinc w8,w0,lt | `FALL_THROUGH`
<a id="insn-006acebc"></a> `006acebc` | `03 7d 01 13` | asr w3,w8,#0x1 | `FALL_THROUGH`
<a id="insn-006acec0"></a> `006acec0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-006acec4"></a> `006acec4` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-006acec8"></a> `006acec8` | `93 fb f6 97` | bl 0x0046bd14 | `UNCONDITIONAL_CALL`
<a id="insn-006acecc"></a> `006acecc` | `14 00 00 94` | bl 0x006acf1c | `UNCONDITIONAL_CALL`
<a id="insn-006aced0"></a> `006aced0` | `68 f2 44 b9` | ldr w8,[x19, #0x4f0] | `FALL_THROUGH`
<a id="insn-006aced4"></a> `006aced4` | `08 01 1e 32` | orr w8,w8,#0x4 | `FALL_THROUGH`
<a id="insn-006aced8"></a> `006aced8` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-006acedc"></a> `006acedc` | `61 00 00 54` | b.ne 0x006acee8 | `CONDITIONAL_JUMP`
<a id="insn-006acee0"></a> `006acee0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-006acee4"></a> `006acee4` | `3c 01 00 94` | bl 0x006ad3d4 | `UNCONDITIONAL_CALL`
<a id="insn-006acee8"></a> `006acee8` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-006aceec"></a> `006aceec` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-006acef0"></a> `006acef0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-006acef4"></a> `006acef4` | `21 01 00 54` | b.ne 0x006acf18 | `CONDITIONAL_JUMP`
<a id="insn-006acef8"></a> `006acef8` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-006acefc"></a> `006acefc` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006acf00"></a> `006acf00` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-006acf04"></a> `006acf04` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006acf08"></a> `006acf08` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006acf0c"></a> `006acf0c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006acf10"></a> `006acf10` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-006acf14"></a> `006acf14` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006acf18"></a> `006acf18` | `f2 aa 16 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006acaac`](#insn-006acaac) 範囲 `[['006acaac', '006acae7']]`
  - `CONDITIONAL_JUMP` [`006acae4`](#insn-006acae4) → [`006acb0c`](#insn-006acb0c)
  - `FALL_THROUGH` [`006acae4`](#insn-006acae4) → [`006acae8`](#insn-006acae8)
- ブロック [`006acae8`](#insn-006acae8) 範囲 `[['006acae8', '006acb0b']]`
  - `UNCONDITIONAL_JUMP` [`006acb08`](#insn-006acb08) → [`006acb10`](#insn-006acb10)
- ブロック [`006acb0c`](#insn-006acb0c) 範囲 `[['006acb0c', '006acb0f']]`
  - `FALL_THROUGH` [`006acb0c`](#insn-006acb0c) → [`006acb10`](#insn-006acb10)
- ブロック [`006acb10`](#insn-006acb10) 範囲 `[['006acb10', '006acb1b']]`
  - `CONDITIONAL_JUMP` [`006acb18`](#insn-006acb18) → [`006acee8`](#insn-006acee8)
  - `FALL_THROUGH` [`006acb18`](#insn-006acb18) → [`006acb1c`](#insn-006acb1c)
- ブロック [`006acb1c`](#insn-006acb1c) 範囲 `[['006acb1c', '006acb23']]`
  - `CONDITIONAL_JUMP` [`006acb20`](#insn-006acb20) → [`006aced0`](#insn-006aced0)
  - `FALL_THROUGH` [`006acb20`](#insn-006acb20) → [`006acb24`](#insn-006acb24)
- ブロック [`006acb24`](#insn-006acb24) 範囲 `[['006acb24', '006acb2b']]`
  - `FALL_THROUGH` [`006acb28`](#insn-006acb28) → [`006acb2c`](#insn-006acb2c)
- ブロック [`006acb2c`](#insn-006acb2c) 範囲 `[['006acb2c', '006acb53']]`
  - `FALL_THROUGH` [`006acb50`](#insn-006acb50) → [`006acb54`](#insn-006acb54)
- ブロック [`006acb54`](#insn-006acb54) 範囲 `[['006acb54', '006acb7b']]`
  - `CONDITIONAL_JUMP` [`006acb78`](#insn-006acb78) → [`006acc08`](#insn-006acc08)
  - `FALL_THROUGH` [`006acb78`](#insn-006acb78) → [`006acb7c`](#insn-006acb7c)
- ブロック [`006acb7c`](#insn-006acb7c) 範囲 `[['006acb7c', '006acb7f']]`
  - `FALL_THROUGH` [`006acb7c`](#insn-006acb7c) → [`006acb80`](#insn-006acb80)
- ブロック [`006acb80`](#insn-006acb80) 範囲 `[['006acb80', '006acbf7']]`
  - `FALL_THROUGH` [`006acbf4`](#insn-006acbf4) → [`006acbf8`](#insn-006acbf8)
- ブロック [`006acbf8`](#insn-006acbf8) 範囲 `[['006acbf8', '006acc03']]`
  - `FALL_THROUGH` [`006acc00`](#insn-006acc00) → [`006acc04`](#insn-006acc04)
- ブロック [`006acc04`](#insn-006acc04) 範囲 `[['006acc04', '006acc07']]`
  - `FALL_THROUGH` [`006acc04`](#insn-006acc04) → [`006acc08`](#insn-006acc08)
- ブロック [`006acc08`](#insn-006acc08) 範囲 `[['006acc08', '006acc47']]`
  - `FALL_THROUGH` [`006acc44`](#insn-006acc44) → [`006acc48`](#insn-006acc48)
- ブロック [`006acc48`](#insn-006acc48) 範囲 `[['006acc48', '006acc5b']]`
  - `FALL_THROUGH` [`006acc58`](#insn-006acc58) → [`006acc5c`](#insn-006acc5c)
- ブロック [`006acc5c`](#insn-006acc5c) 範囲 `[['006acc5c', '006acc6b']]`
  - `FALL_THROUGH` [`006acc68`](#insn-006acc68) → [`006acc6c`](#insn-006acc6c)
- ブロック [`006acc6c`](#insn-006acc6c) 範囲 `[['006acc6c', '006acd17']]`
  - `FALL_THROUGH` [`006acd14`](#insn-006acd14) → [`006acd18`](#insn-006acd18)
- ブロック [`006acd18`](#insn-006acd18) 範囲 `[['006acd18', '006acd2f']]`
  - `CONDITIONAL_JUMP` [`006acd2c`](#insn-006acd2c) → [`006acd7c`](#insn-006acd7c)
  - `FALL_THROUGH` [`006acd2c`](#insn-006acd2c) → [`006acd30`](#insn-006acd30)
- ブロック [`006acd30`](#insn-006acd30) 範囲 `[['006acd30', '006acd37']]`
  - `CONDITIONAL_JUMP` [`006acd34`](#insn-006acd34) → [`006ace80`](#insn-006ace80)
  - `FALL_THROUGH` [`006acd34`](#insn-006acd34) → [`006acd38`](#insn-006acd38)
- ブロック [`006acd38`](#insn-006acd38) 範囲 `[['006acd38', '006acd3f']]`
  - `CONDITIONAL_JUMP` [`006acd3c`](#insn-006acd3c) → [`006acecc`](#insn-006acecc)
  - `FALL_THROUGH` [`006acd3c`](#insn-006acd3c) → [`006acd40`](#insn-006acd40)
- ブロック [`006acd40`](#insn-006acd40) 範囲 `[['006acd40', '006acd4f']]`
  - `FALL_THROUGH` [`006acd4c`](#insn-006acd4c) → [`006acd50`](#insn-006acd50)
- ブロック [`006acd50`](#insn-006acd50) 範囲 `[['006acd50', '006acd7b']]`
  - `UNCONDITIONAL_JUMP` [`006acd78`](#insn-006acd78) → [`006aceb8`](#insn-006aceb8)
- ブロック [`006acd7c`](#insn-006acd7c) 範囲 `[['006acd7c', '006acd83']]`
  - `CONDITIONAL_JUMP` [`006acd80`](#insn-006acd80) → [`006acd8c`](#insn-006acd8c)
  - `FALL_THROUGH` [`006acd80`](#insn-006acd80) → [`006acd84`](#insn-006acd84)
- ブロック [`006acd84`](#insn-006acd84) 範囲 `[['006acd84', '006acd87']]`
  - `FALL_THROUGH` [`006acd84`](#insn-006acd84) → [`006acd88`](#insn-006acd88)
- ブロック [`006acd88`](#insn-006acd88) 範囲 `[['006acd88', '006acd8b']]`
  - `CONDITIONAL_JUMP` [`006acd88`](#insn-006acd88) → [`006acecc`](#insn-006acecc)
  - `FALL_THROUGH` [`006acd88`](#insn-006acd88) → [`006acd8c`](#insn-006acd8c)
- ブロック [`006acd8c`](#insn-006acd8c) 範囲 `[['006acd8c', '006acda7']]`
  - `FALL_THROUGH` [`006acda4`](#insn-006acda4) → [`006acda8`](#insn-006acda8)
- ブロック [`006acda8`](#insn-006acda8) 範囲 `[['006acda8', '006acdaf']]`
  - `FALL_THROUGH` [`006acdac`](#insn-006acdac) → [`006acdb0`](#insn-006acdb0)
- ブロック [`006acdb0`](#insn-006acdb0) 範囲 `[['006acdb0', '006ace7f']]`
  - `UNCONDITIONAL_JUMP` [`006ace7c`](#insn-006ace7c) → [`006acecc`](#insn-006acecc)
- ブロック [`006ace80`](#insn-006ace80) 範囲 `[['006ace80', '006aceb7']]`
  - `FALL_THROUGH` [`006aceb4`](#insn-006aceb4) → [`006aceb8`](#insn-006aceb8)
- ブロック [`006aceb8`](#insn-006aceb8) 範囲 `[['006aceb8', '006acecb']]`
  - `FALL_THROUGH` [`006acec8`](#insn-006acec8) → [`006acecc`](#insn-006acecc)
- ブロック [`006acecc`](#insn-006acecc) 範囲 `[['006acecc', '006acecf']]`
  - `FALL_THROUGH` [`006acecc`](#insn-006acecc) → [`006aced0`](#insn-006aced0)
- ブロック [`006aced0`](#insn-006aced0) 範囲 `[['006aced0', '006acedf']]`
  - `CONDITIONAL_JUMP` [`006acedc`](#insn-006acedc) → [`006acee8`](#insn-006acee8)
  - `FALL_THROUGH` [`006acedc`](#insn-006acedc) → [`006acee0`](#insn-006acee0)
- ブロック [`006acee0`](#insn-006acee0) 範囲 `[['006acee0', '006acee7']]`
  - `FALL_THROUGH` [`006acee4`](#insn-006acee4) → [`006acee8`](#insn-006acee8)
- ブロック [`006acee8`](#insn-006acee8) 範囲 `[['006acee8', '006acef7']]`
  - `CONDITIONAL_JUMP` [`006acef4`](#insn-006acef4) → [`006acf18`](#insn-006acf18)
  - `FALL_THROUGH` [`006acef4`](#insn-006acef4) → [`006acef8`](#insn-006acef8)
- ブロック [`006acef8`](#insn-006acef8) 範囲 `[['006acef8', '006acf17']]`
- ブロック [`006acf18`](#insn-006acf18) 範囲 `[['006acf18', '006acf1b']]`

## 命令位置別の参照

- [`006acab0`](#insn-006acab0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acab4`](#insn-006acab4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acab8`](#insn-006acab8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acabc`](#insn-006acabc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acac0`](#insn-006acac0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acac4`](#insn-006acac4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acad8`](#insn-006acad8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acae0`](#insn-006acae0) → `00ca4578`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`006acae4`](#insn-006acae4) → [`006acb0c`](#insn-006acb0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acaec`](#insn-006acaec) → `00c65a58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`006acaf4`](#insn-006acaf4) → `00c70dc0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`006acb00`](#insn-006acb00) → [`00c58210`](../00c58/00c58210.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58210` · 推定シンボル `None` · 推定型 `None`
- [`006acb08`](#insn-006acb08) → [`006acb10`](#insn-006acb10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb10`](#insn-006acb10) → [`00467820`](../00467/00467820.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467820` · 推定シンボル `None` · 推定型 `None`
- [`006acb18`](#insn-006acb18) → [`006acee8`](#insn-006acee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb20`](#insn-006acb20) → [`006aced0`](#insn-006aced0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb2c`](#insn-006acb2c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acb30`](#insn-006acb30) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`006acb38`](#insn-006acb38) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acb3c`](#insn-006acb3c) → [`0046ca44`](../0046c/0046ca44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca44` · 推定シンボル `None` · 推定型 `None`
- [`006acb6c`](#insn-006acb6c) → [`00469bc4`](../00469/00469bc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469bc4` · 推定シンボル `None` · 推定型 `None`
- [`006acb78`](#insn-006acb78) → [`006acc08`](#insn-006acc08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acb84`](#insn-006acb84) → [`00467ab0`](../00467/00467ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ab0` · 推定シンボル `None` · 推定型 `None`
- [`006acb9c`](#insn-006acb9c) → [`00467aec`](../00467/00467aec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467aec` · 推定シンボル `None` · 推定型 `None`
- [`006acba0`](#insn-006acba0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acbac`](#insn-006acbac) → `003339e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`006acbb4`](#insn-006acbb4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acbb8`](#insn-006acbb8) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`006acbc0`](#insn-006acbc0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acbc4`](#insn-006acbc4) → [`0046ca44`](../0046c/0046ca44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca44` · 推定シンボル `None` · 推定型 `None`
- [`006acbdc`](#insn-006acbdc) → [`00467f14`](../00467/00467f14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467f14` · 推定シンボル `None` · 推定型 `None`
- [`006acbf4`](#insn-006acbf4) → [`00467aec`](../00467/00467aec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467aec` · 推定シンボル `None` · 推定型 `None`
- [`006acc00`](#insn-006acc00) → [`00467ab0`](../00467/00467ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467ab0` · 推定シンボル `None` · 推定型 `None`
- [`006acc28`](#insn-006acc28) → [`00470074`](../00470/00470074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470074` · 推定シンボル `None` · 推定型 `None`
- [`006acc38`](#insn-006acc38) → [`004700ec`](../00470/004700ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004700ec` · 推定シンボル `None` · 推定型 `None`
- [`006acc3c`](#insn-006acc3c) → [`0046e76c`](../0046e/0046e76c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e76c` · 推定シンボル `None` · 推定型 `None`
- [`006acc54`](#insn-006acc54) → [`004700ec`](../00470/004700ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004700ec` · 推定シンボル `None` · 推定型 `None`
- [`006acc58`](#insn-006acc58) → [`0046e774`](../0046e/0046e774.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e774` · 推定シンボル `None` · 推定型 `None`
- [`006acc70`](#insn-006acc70) → [`004700ec`](../00470/004700ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004700ec` · 推定シンボル `None` · 推定型 `None`
- [`006acc74`](#insn-006acc74) → [`0046e77c`](../0046e/0046e77c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e77c` · 推定シンボル `None` · 推定型 `None`
- [`006acc8c`](#insn-006acc8c) → [`0046e6ec`](../0046e/0046e6ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e6ec` · 推定シンボル `None` · 推定型 `None`
- [`006acc90`](#insn-006acc90) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acc94`](#insn-006acc94) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`006acca4`](#insn-006acca4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acd0c`](#insn-006acd0c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd20`](#insn-006acd20) → [`0046bd14`](../0046b/0046bd14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046bd14` · 推定シンボル `None` · 推定型 `None`
- [`006acd2c`](#insn-006acd2c) → [`006acd7c`](#insn-006acd7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd34`](#insn-006acd34) → [`006ace80`](#insn-006ace80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd3c`](#insn-006acd3c) → [`006acecc`](#insn-006acecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd50`](#insn-006acd50) → [`00470074`](../00470/00470074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470074` · 推定シンボル `None` · 推定型 `None`
- [`006acd54`](#insn-006acd54) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acd58`](#insn-006acd58) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`006acd68`](#insn-006acd68) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acd6c`](#insn-006acd6c) → [`0046ca44`](../0046c/0046ca44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca44` · 推定シンボル `None` · 推定型 `None`
- [`006acd78`](#insn-006acd78) → [`006aceb8`](#insn-006aceb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd80`](#insn-006acd80) → [`006acd8c`](#insn-006acd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd88`](#insn-006acd88) → [`006acecc`](#insn-006acecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acd9c`](#insn-006acd9c) → [`00470074`](../00470/00470074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470074` · 推定シンボル `None` · 推定型 `None`
- [`006acda0`](#insn-006acda0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acda4`](#insn-006acda4) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`006acdb4`](#insn-006acdb4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acdb8`](#insn-006acdb8) → [`0046ca44`](../0046c/0046ca44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca44` · 推定シンボル `None` · 推定型 `None`
- [`006acdd4`](#insn-006acdd4) → [`0046bd14`](../0046b/0046bd14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046bd14` · 推定シンボル `None` · 推定型 `None`
- [`006acddc`](#insn-006acddc) → [`006c115c`](../006c1/006c115c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006c115c` · 推定シンボル `None` · 推定型 `None`
- [`006acde4`](#insn-006acde4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006acde8`](#insn-006acde8) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`006ace14`](#insn-006ace14) → [`00469bc4`](../00469/00469bc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469bc4` · 推定シンボル `None` · 推定型 `None`
- [`006ace1c`](#insn-006ace1c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006ace20`](#insn-006ace20) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`006ace48`](#insn-006ace48) → [`00469bc4`](../00469/00469bc4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469bc4` · 推定シンボル `None` · 推定型 `None`
- [`006ace50`](#insn-006ace50) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006ace54`](#insn-006ace54) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`006ace78`](#insn-006ace78) → [`00468878`](../00468/00468878.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468878` · 推定シンボル `None` · 推定型 `None`
- [`006ace7c`](#insn-006ace7c) → [`006acecc`](#insn-006acecc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006ace90`](#insn-006ace90) → [`00470074`](../00470/00470074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470074` · 推定シンボル `None` · 推定型 `None`
- [`006ace94`](#insn-006ace94) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006ace98`](#insn-006ace98) → [`0046c984`](../0046c/0046c984.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c984` · 推定シンボル `None` · 推定型 `None`
- [`006acea8`](#insn-006acea8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`006aceac`](#insn-006aceac) → [`0046ca44`](../0046c/0046ca44.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca44` · 推定シンボル `None` · 推定型 `None`
- [`006acec8`](#insn-006acec8) → [`0046bd14`](../0046b/0046bd14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046bd14` · 推定シンボル `None` · 推定型 `None`
- [`006acecc`](#insn-006acecc) → [`006acf1c`](006acf1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006acf1c` · 推定シンボル `None` · 推定型 `None`
- [`006acedc`](#insn-006acedc) → [`006acee8`](#insn-006acee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acee4`](#insn-006acee4) → [`006ad3d4`](../006ad/006ad3d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `006ad3d4` · 推定シンボル `None` · 推定型 `None`
- [`006aceec`](#insn-006aceec) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acef4`](#insn-006acef4) → [`006acf18`](#insn-006acf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acef8`](#insn-006acef8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acefc`](#insn-006acefc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf00`](#insn-006acf00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf04`](#insn-006acf04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf08`](#insn-006acf08) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf0c`](#insn-006acf0c) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006acf18`](#insn-006acf18) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006acab0`](#insn-006acab0)

~~~json
{
  "source": "006acab0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acab4`](#insn-006acab4)

~~~json
{
  "source": "006acab4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acab8`](#insn-006acab8)

~~~json
{
  "source": "006acab8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acabc`](#insn-006acabc)

~~~json
{
  "source": "006acabc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acac0`](#insn-006acac0)

~~~json
{
  "source": "006acac0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acac4`](#insn-006acac4)

~~~json
{
  "source": "006acac4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acad8`](#insn-006acad8)

~~~json
{
  "source": "006acad8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acae0`](#insn-006acae0)

~~~json
{
  "source": "006acae0",
  "target": "00ca4578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`006acae4`](#insn-006acae4)

~~~json
{
  "source": "006acae4",
  "target": "006acb0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acaec`](#insn-006acaec)

~~~json
{
  "source": "006acaec",
  "target": "00c65a58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65a58",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006acaf4`](#insn-006acaf4)

~~~json
{
  "source": "006acaf4",
  "target": "00c70dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c70dc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`006acb00`](#insn-006acb00)

~~~json
{
  "source": "006acb00",
  "target": "00c58210",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb08`](#insn-006acb08)

~~~json
{
  "source": "006acb08",
  "target": "006acb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb10`](#insn-006acb10)

~~~json
{
  "source": "006acb10",
  "target": "00467820",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb18`](#insn-006acb18)

~~~json
{
  "source": "006acb18",
  "target": "006acee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb20`](#insn-006acb20)

~~~json
{
  "source": "006acb20",
  "target": "006aced0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb2c`](#insn-006acb2c)

~~~json
{
  "source": "006acb2c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb30`](#insn-006acb30)

~~~json
{
  "source": "006acb30",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb38`](#insn-006acb38)

~~~json
{
  "source": "006acb38",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb3c`](#insn-006acb3c)

~~~json
{
  "source": "006acb3c",
  "target": "0046ca44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb6c`](#insn-006acb6c)

~~~json
{
  "source": "006acb6c",
  "target": "00469bc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb78`](#insn-006acb78)

~~~json
{
  "source": "006acb78",
  "target": "006acc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acb84`](#insn-006acb84)

~~~json
{
  "source": "006acb84",
  "target": "00467ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acb9c`](#insn-006acb9c)

~~~json
{
  "source": "006acb9c",
  "target": "00467aec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acba0`](#insn-006acba0)

~~~json
{
  "source": "006acba0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbac`](#insn-006acbac)

~~~json
{
  "source": "006acbac",
  "target": "003339e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003339e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "44c26a00bc790900",
  "capture_start": "003339e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`006acbb4`](#insn-006acbb4)

~~~json
{
  "source": "006acbb4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbb8`](#insn-006acbb8)

~~~json
{
  "source": "006acbb8",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbc0`](#insn-006acbc0)

~~~json
{
  "source": "006acbc0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbc4`](#insn-006acbc4)

~~~json
{
  "source": "006acbc4",
  "target": "0046ca44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbdc`](#insn-006acbdc)

~~~json
{
  "source": "006acbdc",
  "target": "00467f14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acbf4`](#insn-006acbf4)

~~~json
{
  "source": "006acbf4",
  "target": "00467aec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc00`](#insn-006acc00)

~~~json
{
  "source": "006acc00",
  "target": "00467ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc28`](#insn-006acc28)

~~~json
{
  "source": "006acc28",
  "target": "00470074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc38`](#insn-006acc38)

~~~json
{
  "source": "006acc38",
  "target": "004700ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc3c`](#insn-006acc3c)

~~~json
{
  "source": "006acc3c",
  "target": "0046e76c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc54`](#insn-006acc54)

~~~json
{
  "source": "006acc54",
  "target": "004700ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc58`](#insn-006acc58)

~~~json
{
  "source": "006acc58",
  "target": "0046e774",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc70`](#insn-006acc70)

~~~json
{
  "source": "006acc70",
  "target": "004700ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc74`](#insn-006acc74)

~~~json
{
  "source": "006acc74",
  "target": "0046e77c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc8c`](#insn-006acc8c)

~~~json
{
  "source": "006acc8c",
  "target": "0046e6ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc90`](#insn-006acc90)

~~~json
{
  "source": "006acc90",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acc94`](#insn-006acc94)

~~~json
{
  "source": "006acc94",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acca4`](#insn-006acca4)

~~~json
{
  "source": "006acca4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acd0c`](#insn-006acd0c)

~~~json
{
  "source": "006acd0c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd20`](#insn-006acd20)

~~~json
{
  "source": "006acd20",
  "target": "0046bd14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acd2c`](#insn-006acd2c)

~~~json
{
  "source": "006acd2c",
  "target": "006acd7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd34`](#insn-006acd34)

~~~json
{
  "source": "006acd34",
  "target": "006ace80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd3c`](#insn-006acd3c)

~~~json
{
  "source": "006acd3c",
  "target": "006acecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd50`](#insn-006acd50)

~~~json
{
  "source": "006acd50",
  "target": "00470074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acd54`](#insn-006acd54)

~~~json
{
  "source": "006acd54",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acd58`](#insn-006acd58)

~~~json
{
  "source": "006acd58",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acd68`](#insn-006acd68)

~~~json
{
  "source": "006acd68",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acd6c`](#insn-006acd6c)

~~~json
{
  "source": "006acd6c",
  "target": "0046ca44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acd78`](#insn-006acd78)

~~~json
{
  "source": "006acd78",
  "target": "006aceb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd80`](#insn-006acd80)

~~~json
{
  "source": "006acd80",
  "target": "006acd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd88`](#insn-006acd88)

~~~json
{
  "source": "006acd88",
  "target": "006acecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acd9c`](#insn-006acd9c)

~~~json
{
  "source": "006acd9c",
  "target": "00470074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acda0`](#insn-006acda0)

~~~json
{
  "source": "006acda0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acda4`](#insn-006acda4)

~~~json
{
  "source": "006acda4",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acdb4`](#insn-006acdb4)

~~~json
{
  "source": "006acdb4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acdb8`](#insn-006acdb8)

~~~json
{
  "source": "006acdb8",
  "target": "0046ca44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acdd4`](#insn-006acdd4)

~~~json
{
  "source": "006acdd4",
  "target": "0046bd14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acddc`](#insn-006acddc)

~~~json
{
  "source": "006acddc",
  "target": "006c115c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acde4`](#insn-006acde4)

~~~json
{
  "source": "006acde4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acde8`](#insn-006acde8)

~~~json
{
  "source": "006acde8",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace14`](#insn-006ace14)

~~~json
{
  "source": "006ace14",
  "target": "00469bc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace1c`](#insn-006ace1c)

~~~json
{
  "source": "006ace1c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace20`](#insn-006ace20)

~~~json
{
  "source": "006ace20",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace48`](#insn-006ace48)

~~~json
{
  "source": "006ace48",
  "target": "00469bc4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace50`](#insn-006ace50)

~~~json
{
  "source": "006ace50",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace54`](#insn-006ace54)

~~~json
{
  "source": "006ace54",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace78`](#insn-006ace78)

~~~json
{
  "source": "006ace78",
  "target": "00468878",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace7c`](#insn-006ace7c)

~~~json
{
  "source": "006ace7c",
  "target": "006acecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006ace90`](#insn-006ace90)

~~~json
{
  "source": "006ace90",
  "target": "00470074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace94`](#insn-006ace94)

~~~json
{
  "source": "006ace94",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006ace98`](#insn-006ace98)

~~~json
{
  "source": "006ace98",
  "target": "0046c984",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acea8`](#insn-006acea8)

~~~json
{
  "source": "006acea8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aceac`](#insn-006aceac)

~~~json
{
  "source": "006aceac",
  "target": "0046ca44",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acec8`](#insn-006acec8)

~~~json
{
  "source": "006acec8",
  "target": "0046bd14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acecc`](#insn-006acecc)

~~~json
{
  "source": "006acecc",
  "target": "006acf1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006acedc`](#insn-006acedc)

~~~json
{
  "source": "006acedc",
  "target": "006acee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acee4`](#insn-006acee4)

~~~json
{
  "source": "006acee4",
  "target": "006ad3d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006aceec`](#insn-006aceec)

~~~json
{
  "source": "006aceec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acef4`](#insn-006acef4)

~~~json
{
  "source": "006acef4",
  "target": "006acf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acef8`](#insn-006acef8)

~~~json
{
  "source": "006acef8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acefc`](#insn-006acefc)

~~~json
{
  "source": "006acefc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf00`](#insn-006acf00)

~~~json
{
  "source": "006acf00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf04`](#insn-006acf04)

~~~json
{
  "source": "006acf04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf08`](#insn-006acf08)

~~~json
{
  "source": "006acf08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf0c`](#insn-006acf0c)

~~~json
{
  "source": "006acf0c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006acf18`](#insn-006acf18)

~~~json
{
  "source": "006acf18",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
