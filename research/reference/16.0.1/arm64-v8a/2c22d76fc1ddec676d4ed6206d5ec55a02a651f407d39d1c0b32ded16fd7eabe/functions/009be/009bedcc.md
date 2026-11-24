# 009bedcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009bec30`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009be/009bec30.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0056.md#compare-8098e592b4b93cf973faed117fe68ec7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `009bee20`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009be/009bee20.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0058.md#compare-19b8f21ff2894558bdca6413f13aa968)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009bedcc",
  "name": "FUN_009bedcc",
  "size": 1096,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "814fbf19c8aeb9efdd1413349e5033bed418b882b1e61bf8263c64dba58f8e87",
  "source_text_sha256": "814fbf19c8aeb9efdd1413349e5033bed418b882b1e61bf8263c64dba58f8e87",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009bedcc",
        "009bf213"
      ]
    ],
    "bytes_sha256": "f8bca90d6cd33706c37f43380f48721b23e3a08a3095367e634ff1dd6093c25c",
    "instruction_count": 274,
    "instruction_bytes": 1096,
    "body_bytes": 1096,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00859b58](../00859/00859b58.md)

## 呼び出し先

- [00467b60](../00467/00467b60.md)
- [00468bdc](../00468/00468bdc.md)
- [00468c60](../00468/00468c60.md)
- [00468f88](../00468/00468f88.md)
- [00469c04](../00469/00469c04.md)
- [0046c9c4](../0046c/0046c9c4.md)
- [0046ca84](../0046c/0046ca84.md)
- [0046d974](../0046d/0046d974.md)
- [0046d9ac](../0046d/0046d9ac.md)
- [008514f8](../00851/008514f8.md)
- [008614b0](../00861/008614b0.md)
- [009be2e0](../009be/009be2e0.md)
- [00ac977c](../00ac9/00ac977c.md)
- [00c58610](../00c58/00c58610.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6207 bytes

~~~c

void FUN_009bedcc(long param_1,undefined8 param_2)

{
  int *piVar1;
  uint uVar2;
  int iVar3;
  int iVar4;
  uint uVar5;
  undefined *puVar6;
  int iVar7;
  undefined4 uVar8;
  long lVar9;
  undefined8 uVar10;
  float fVar11;
  
                    /* try { // try from 009bede0 to 00abee6f has its CatchHandler @ 009bdb00 */
  if ((DAT_00ca4978 != 0) &&
     (lVar9 = __dynamic_cast(DAT_00ca4978,&PTR__ZTVN10__cxxabiv117__class_type_infoE_16__00c65e58,
                             &PTR__ZTVN10__cxxabiv120__si_class_type_infoE_16__00c89680,0),
     lVar9 != 0)) {
    piVar1 = (int *)((long)&fde_table_entry_00333cc8.data_loc + param_1);
    FUN_00467b60(param_2,0x5c,0x9a,0x4a,0xff);
    uVar10 = *(undefined8 *)(lVar9 + 0x108);
    iVar7 = FUN_0046c9c4(param_1);
    FUN_008514f8();
                    /* try { // try from 009bee70 to 00abee73 has its CatchHandler @ 009bf354 */
    uVar8 = FUN_0046ca84();
    FUN_00469c04(param_2,uVar10,0xffffffd8,0,iVar7 + 0x50,uVar8,0);
                    /* try { // try from 009bee98 to 00abeecb has its CatchHandler @ 009bf334 */
    FUN_00467b60(param_2,0x6e,0xa6,0x59,0xff);
    fVar11 = (float)FUN_0046d9ac((float)*(int *)((long)&fde_table_entry_00333f98.data_loc + param_1)
                                );
                    /* try { // try from 009beecc to 00abefd7 has its CatchHandler @ 009bdb00 */
    FUN_00468bdc(param_2,(int)(fVar11 * 115.0) + 0x8c);
    uVar10 = *(undefined8 *)(lVar9 + 0x118);
    uVar8 = FUN_0046c9c4(param_1);
    FUN_00469c04(param_2,uVar10,0,0,uVar8,0x330,0);
    FUN_00467b60(param_2,0xff,0xff,0xff,0xff);
    FUN_00468c60(param_2,0);
    FUN_008614b0(param_1,*(undefined8 *)(lVar9 + 200),0,0);
    uVar10 = *(undefined8 *)(lVar9 + 200);
    uVar8 = FUN_0046c9c4(param_1);
    FUN_00469c04(param_2,uVar10,0,0,uVar8,0x37,0);
    FUN_00468c60(param_2,2);
    uVar10 = *(undefined8 *)(lVar9 + 200);
    uVar8 = FUN_0046c9c4(param_1);
    FUN_00469c04(param_2,uVar10,0,0x249,uVar8,0x37,0);
    FUN_00468c60(param_2,0);
    FUN_00468f88(param_2,*(undefined8 *)(lVar9 + 0x108),
                 8 - *(int *)((long)&fde_table_entry_00334170.initial_loc + param_1),3,6);
                    /* try { // try from 009befd8 to 00abefef has its CatchHandler @ 009bf32c */
    if (((((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1) & 1) == 0) &&
         ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 1) & 1) == 0)) &&
        ((*(byte *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 1) & 1) == 0)) &&
       ((((*(byte *)((long)&fde_table_entry_00332a30.initial_loc + param_1 + 1) & 1) == 0 &&
         ((*(byte *)((long)&fde_table_entry_00332a20.data_loc + param_1 + 2) & 1) == 0)) &&
        (((*(byte *)((long)&fde_table_entry_00332060.initial_loc + param_1) & 1) == 0 &&
         (*(char *)((long)&fde_table_entry_00332a28.data_loc + param_1 + 2) != '\0')))))) {
      uVar2 = *(uint *)((long)&fde_table_entry_00333f98.initial_loc + param_1);
      uVar5 = -uVar2;
                    /* try { // try from 009bf014 to 00abf04f has its CatchHandler @ 009bf398 */
      uVar2 = uVar2 & 3;
      if (-1 < (int)uVar5) {
        uVar2 = -(uVar5 & 3);
      }
      FUN_00469c04(param_2,*(undefined8 *)(lVar9 + 0xa8),3,0x21c,0x60,0x60,
                   ((uint)(int)(char)((char)uVar2 + (char)((uVar2 & 0x80) >> 7)) >> 1) + 0xc & 0xff)
      ;
    }
    puVar6 = PTR_DAT_00c9b4a8;
                    /* try { // try from 009bf050 to 00abf19b has its CatchHandler @ 009bdb00 */
    iVar3 = *(int *)(PTR_DAT_00c9b4a8 +
                    (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1) * 4);
    iVar7 = iVar3;
    if (iVar3 < 0) {
      iVar7 = iVar3 + 1;
    }
    FUN_00469c04(param_2,*(undefined8 *)(lVar9 + 0xa8),*piVar1 - (iVar7 >> 1),
                 *(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar7 >> 1),
                 *(int *)((long)&fde_table_entry_00333cd0.data_loc + param_1) + iVar3,
                 *(int *)((long)&fde_table_entry_00333cd8.initial_loc + param_1) + iVar3,9);
    iVar4 = *(int *)(puVar6 + (long)*(int *)((long)&fde_table_entry_00333dc0.initial_loc + param_1)
                              * 4);
    iVar7 = iVar4 + 0x54;
    iVar3 = iVar4 + 0x3c;
    if (iVar4 < 0) {
      iVar4 = iVar4 + 1;
    }
    FUN_00469c04(param_2,*(undefined8 *)(lVar9 + 0xa8),(*piVar1 - (iVar4 >> 1)) + 4,
                 (*(int *)((long)&fde_table_entry_00333cd0.initial_loc + param_1) - (iVar4 >> 1)) +
                 0x11,iVar7,iVar3,3);
    FUN_00ac977c((long)&fde_table_entry_00337d90.initial_loc + param_1,
                 *(undefined8 *)(lVar9 + 0x138),*(undefined8 *)(lVar9 + 0x178));
    FUN_00467b60(param_2,0xff,0xff,0xff,0xff);
    FUN_00468bdc(param_2,0x72);
    if (0 < *(int *)((long)&fde_table_entry_00337670.initial_loc + param_1)) {
      uVar10 = *(undefined8 *)(lVar9 + 0xa8);
      fVar11 = (float)FUN_0046d974((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   param_1) * 0x1e));
      FUN_00468f88(param_2,uVar10,(int)(fVar11 * 10.0 + 24.0),0x11a,8);
    }
    FUN_00468c60(param_2,1);
    if (*(int *)((long)&fde_table_entry_00337670.initial_loc + param_1) <
        *(int *)((long)&fde_table_entry_00335f78.initial_loc + param_1) + -1) {
      uVar10 = *(undefined8 *)(lVar9 + 0xa8);
      iVar7 = FUN_0046c9c4(param_1);
      fVar11 = (float)FUN_0046d974((float)(*(int *)((long)&fde_table_entry_00333f98.initial_loc +
                                                   param_1) * 0x1e));
                    /* try { // try from 009bf19c to 00abf1a7 has its CatchHandler @ 009bf520 */
      FUN_00468f88(param_2,uVar10,(int)((float)(iVar7 + -0x56) + fVar11 * -10.0),0x11a,8);
    }
                    /* try { // try from 009bf1bc to 00abf1db has its CatchHandler @ 009bf414 */
    FUN_00468c60(param_2,0);
    FUN_00468bdc(param_2,0xff);
                    /* try { // try from 009bf1f0 to 00abf1f7 has its CatchHandler @ 009bf3f0 */
    FUN_009be2e0((long)&fde_table_entry_00337630.initial_loc + param_1);
    return;
  }
                    /* try { // try from 009bf20c to 00abf213 has its CatchHandler @ 009bf3ec */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009bedcc"></a> `009bedcc` | `e8 0f 1a fc` | str d8,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-009bedd0"></a> `009bedd0` | `fd fb 00 a9` | stp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009bedd4"></a> `009bedd4` | `fb 0f 00 f9` | str x27,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009bedd8"></a> `009bedd8` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009beddc"></a> `009beddc` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009bede0"></a> `009bede0` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009bede4"></a> `009bede4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009bede8"></a> `009bede8` | `fd 23 00 91` | add x29,sp,#0x8 | `FALL_THROUGH`
<a id="insn-009bedec"></a> `009bedec` | `28 17 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-009bedf0"></a> `009bedf0` | `08 bd 44 f9` | ldr x8,[x8, #0x978] | `FALL_THROUGH`
<a id="insn-009bedf4"></a> `009bedf4` | `08 20 00 b4` | cbz x8,0x009bf1f4 | `CONDITIONAL_JUMP`
<a id="insn-009bedf8"></a> `009bedf8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-009bedfc"></a> `009bedfc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-009bee00"></a> `009bee00` | `21 15 00 f0` | adrp x1,0xc65000 | `FALL_THROUGH`
<a id="insn-009bee04"></a> `009bee04` | `21 60 39 91` | add x1,x1,#0xe58 | `FALL_THROUGH`
<a id="insn-009bee08"></a> `009bee08` | `42 16 00 f0` | adrp x2,0xc89000 | `FALL_THROUGH`
<a id="insn-009bee0c"></a> `009bee0c` | `42 00 1a 91` | add x2,x2,#0x680 | `FALL_THROUGH`
<a id="insn-009bee10"></a> `009bee10` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-009bee14"></a> `009bee14` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-009bee18"></a> `009bee18` | `fe 65 0a 94` | bl 0x00c58610 | `UNCONDITIONAL_CALL`
<a id="insn-009bee1c"></a> `009bee1c` | `c0 1e 00 b4` | cbz x0,0x009bf1f4 | `CONDITIONAL_JUMP`
<a id="insn-009bee20"></a> `009bee20` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-009bee24"></a> `009bee24` | `19 ce 8e 52` | mov w25,#0x7670 | `FALL_THROUGH`
<a id="insn-009bee28"></a> `009bee28` | `68 ce 4c 91` | add x8,x19,#0x333, LSL #12 | `FALL_THROUGH`
<a id="insn-009bee2c"></a> `009bee2c` | `69 ca 4c 91` | add x9,x19,#0x332, LSL #12 | `FALL_THROUGH`
<a id="insn-009bee30"></a> `009bee30` | `1a ef 8b 52` | mov w26,#0x5f78 | `FALL_THROUGH`
<a id="insn-009bee34"></a> `009bee34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bee38"></a> `009bee38` | `81 0b 80 52` | mov w1,#0x5c | `FALL_THROUGH`
<a id="insn-009bee3c"></a> `009bee3c` | `42 13 80 52` | mov w2,#0x9a | `FALL_THROUGH`
<a id="insn-009bee40"></a> `009bee40` | `43 09 80 52` | mov w3,#0x4a | `FALL_THROUGH`
<a id="insn-009bee44"></a> `009bee44` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-009bee48"></a> `009bee48` | `79 06 a0 72` | movk w25,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-009bee4c"></a> `009bee4c` | `7a 06 a0 72` | movk w26,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-009bee50"></a> `009bee50` | `18 31 33 91` | add x24,x8,#0xccc | `FALL_THROUGH`
<a id="insn-009bee54"></a> `009bee54` | `3b 81 01 91` | add x27,x9,#0x60 | `FALL_THROUGH`
<a id="insn-009bee58"></a> `009bee58` | `42 a3 ea 97` | bl 0x00467b60 | `UNCONDITIONAL_CALL`
<a id="insn-009bee5c"></a> `009bee5c` | `b6 86 40 f9` | ldr x22,[x21, #0x108] | `FALL_THROUGH`
<a id="insn-009bee60"></a> `009bee60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009bee64"></a> `009bee64` | `d8 b6 ea 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-009bee68"></a> `009bee68` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-009bee6c"></a> `009bee6c` | `a3 49 fa 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-009bee70"></a> `009bee70` | `05 b7 ea 97` | bl 0x0046ca84 | `UNCONDITIONAL_CALL`
<a id="insn-009bee74"></a> `009bee74` | `e5 03 00 2a` | mov w5,w0 | `FALL_THROUGH`
<a id="insn-009bee78"></a> `009bee78` | `e4 42 01 11` | add w4,w23,#0x50 | `FALL_THROUGH`
<a id="insn-009bee7c"></a> `009bee7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bee80"></a> `009bee80` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-009bee84"></a> `009bee84` | `e2 04 80 12` | mov w2,#0xffffffd8 | `FALL_THROUGH`
<a id="insn-009bee88"></a> `009bee88` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009bee8c"></a> `009bee8c` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-009bee90"></a> `009bee90` | `5d ab ea 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-009bee94"></a> `009bee94` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bee98"></a> `009bee98` | `c1 0d 80 52` | mov w1,#0x6e | `FALL_THROUGH`
<a id="insn-009bee9c"></a> `009bee9c` | `c2 14 80 52` | mov w2,#0xa6 | `FALL_THROUGH`
<a id="insn-009beea0"></a> `009beea0` | `23 0b 80 52` | mov w3,#0x59 | `FALL_THROUGH`
<a id="insn-009beea4"></a> `009beea4` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-009beea8"></a> `009beea8` | `2e a3 ea 97` | bl 0x00467b60 | `UNCONDITIONAL_CALL`
<a id="insn-009beeac"></a> `009beeac` | `00 d3 42 bd` | ldr s0,[x24, #0x2d0] | `FALL_THROUGH`
<a id="insn-009beeb0"></a> `009beeb0` | `00 d8 21 5e` | scvtf s0,s0 | `FALL_THROUGH`
<a id="insn-009beeb4"></a> `009beeb4` | `be ba ea 97` | bl 0x0046d9ac | `UNCONDITIONAL_CALL`
<a id="insn-009beeb8"></a> `009beeb8` | `c8 5c a8 52` | mov w8,#0x42e60000 | `FALL_THROUGH`
<a id="insn-009beebc"></a> `009beebc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009beec0"></a> `009beec0` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-009beec4"></a> `009beec4` | `00 08 21 1e` | fmul s0,s0,s1 | `FALL_THROUGH`
<a id="insn-009beec8"></a> `009beec8` | `08 00 38 1e` | fcvtzs w8,s0 | `FALL_THROUGH`
<a id="insn-009beecc"></a> `009beecc` | `01 31 02 11` | add w1,w8,#0x8c | `FALL_THROUGH`
<a id="insn-009beed0"></a> `009beed0` | `43 a7 ea 97` | bl 0x00468bdc | `UNCONDITIONAL_CALL`
<a id="insn-009beed4"></a> `009beed4` | `b6 8e 40 f9` | ldr x22,[x21, #0x118] | `FALL_THROUGH`
<a id="insn-009beed8"></a> `009beed8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009beedc"></a> `009beedc` | `ba b6 ea 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-009beee0"></a> `009beee0` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-009beee4"></a> `009beee4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009beee8"></a> `009beee8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-009beeec"></a> `009beeec` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009beef0"></a> `009beef0` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009beef4"></a> `009beef4` | `05 66 80 52` | mov w5,#0x330 | `FALL_THROUGH`
<a id="insn-009beef8"></a> `009beef8` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-009beefc"></a> `009beefc` | `42 ab ea 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-009bef00"></a> `009bef00` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bef04"></a> `009bef04` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-009bef08"></a> `009bef08` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-009bef0c"></a> `009bef0c` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-009bef10"></a> `009bef10` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-009bef14"></a> `009bef14` | `13 a3 ea 97` | bl 0x00467b60 | `UNCONDITIONAL_CALL`
<a id="insn-009bef18"></a> `009bef18` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bef1c"></a> `009bef1c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009bef20"></a> `009bef20` | `50 a7 ea 97` | bl 0x00468c60 | `UNCONDITIONAL_CALL`
<a id="insn-009bef24"></a> `009bef24` | `a1 66 40 f9` | ldr x1,[x21, #0xc8] | `FALL_THROUGH`
<a id="insn-009bef28"></a> `009bef28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009bef2c"></a> `009bef2c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009bef30"></a> `009bef30` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009bef34"></a> `009bef34` | `5f 89 fa 97` | bl 0x008614b0 | `UNCONDITIONAL_CALL`
<a id="insn-009bef38"></a> `009bef38` | `b6 66 40 f9` | ldr x22,[x21, #0xc8] | `FALL_THROUGH`
<a id="insn-009bef3c"></a> `009bef3c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009bef40"></a> `009bef40` | `a1 b6 ea 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-009bef44"></a> `009bef44` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-009bef48"></a> `009bef48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bef4c"></a> `009bef4c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-009bef50"></a> `009bef50` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009bef54"></a> `009bef54` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-009bef58"></a> `009bef58` | `e5 06 80 52` | mov w5,#0x37 | `FALL_THROUGH`
<a id="insn-009bef5c"></a> `009bef5c` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-009bef60"></a> `009bef60` | `29 ab ea 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-009bef64"></a> `009bef64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bef68"></a> `009bef68` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-009bef6c"></a> `009bef6c` | `3d a7 ea 97` | bl 0x00468c60 | `UNCONDITIONAL_CALL`
<a id="insn-009bef70"></a> `009bef70` | `b6 66 40 f9` | ldr x22,[x21, #0xc8] | `FALL_THROUGH`
<a id="insn-009bef74"></a> `009bef74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009bef78"></a> `009bef78` | `93 b6 ea 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-009bef7c"></a> `009bef7c` | `e4 03 00 2a` | mov w4,w0 | `FALL_THROUGH`
<a id="insn-009bef80"></a> `009bef80` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bef84"></a> `009bef84` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-009bef88"></a> `009bef88` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-009bef8c"></a> `009bef8c` | `23 49 80 52` | mov w3,#0x249 | `FALL_THROUGH`
<a id="insn-009bef90"></a> `009bef90` | `e5 06 80 52` | mov w5,#0x37 | `FALL_THROUGH`
<a id="insn-009bef94"></a> `009bef94` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-009bef98"></a> `009bef98` | `1b ab ea 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-009bef9c"></a> `009bef9c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009befa0"></a> `009befa0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009befa4"></a> `009befa4` | `2f a7 ea 97` | bl 0x00468c60 | `UNCONDITIONAL_CALL`
<a id="insn-009befa8"></a> `009befa8` | `08 a7 44 b9` | ldr w8,[x24, #0x4a4] | `FALL_THROUGH`
<a id="insn-009befac"></a> `009befac` | `a1 86 40 f9` | ldr x1,[x21, #0x108] | `FALL_THROUGH`
<a id="insn-009befb0"></a> `009befb0` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-009befb4"></a> `009befb4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009befb8"></a> `009befb8` | `63 00 80 52` | mov w3,#0x3 | `FALL_THROUGH`
<a id="insn-009befbc"></a> `009befbc` | `c4 00 80 52` | mov w4,#0x6 | `FALL_THROUGH`
<a id="insn-009befc0"></a> `009befc0` | `22 01 08 4b` | sub w2,w9,w8 | `FALL_THROUGH`
<a id="insn-009befc4"></a> `009befc4` | `f1 a7 ea 97` | bl 0x00468f88 | `UNCONDITIONAL_CALL`
<a id="insn-009befc8"></a> `009befc8` | `68 13 67 39` | ldrb w8,[x27, #0x9c4] | `FALL_THROUGH`
<a id="insn-009befcc"></a> `009befcc` | `e8 03 00 37` | tbnz w8,#0x0,0x009bf048 | `CONDITIONAL_JUMP`
<a id="insn-009befd0"></a> `009befd0` | `68 17 67 39` | ldrb w8,[x27, #0x9c5] | `FALL_THROUGH`
<a id="insn-009befd4"></a> `009befd4` | `a8 03 00 37` | tbnz w8,#0x0,0x009bf048 | `CONDITIONAL_JUMP`
<a id="insn-009befd8"></a> `009befd8` | `68 37 67 39` | ldrb w8,[x27, #0x9cd] | `FALL_THROUGH`
<a id="insn-009befdc"></a> `009befdc` | `68 03 00 37` | tbnz w8,#0x0,0x009bf048 | `CONDITIONAL_JUMP`
<a id="insn-009befe0"></a> `009befe0` | `68 47 67 39` | ldrb w8,[x27, #0x9d1] | `FALL_THROUGH`
<a id="insn-009befe4"></a> `009befe4` | `28 03 00 37` | tbnz w8,#0x0,0x009bf048 | `CONDITIONAL_JUMP`
<a id="insn-009befe8"></a> `009befe8` | `68 1b 67 39` | ldrb w8,[x27, #0x9c6] | `FALL_THROUGH`
<a id="insn-009befec"></a> `009befec` | `e8 02 00 37` | tbnz w8,#0x0,0x009bf048 | `CONDITIONAL_JUMP`
<a id="insn-009beff0"></a> `009beff0` | `68 03 40 39` | ldrb w8,[x27] | `FALL_THROUGH`
<a id="insn-009beff4"></a> `009beff4` | `a8 02 00 37` | tbnz w8,#0x0,0x009bf048 | `CONDITIONAL_JUMP`
<a id="insn-009beff8"></a> `009beff8` | `68 3b 67 39` | ldrb w8,[x27, #0x9ce] | `FALL_THROUGH`
<a id="insn-009beffc"></a> `009beffc` | `68 02 00 34` | cbz w8,0x009bf048 | `CONDITIONAL_JUMP`
<a id="insn-009bf000"></a> `009bf000` | `08 cf 42 b9` | ldr w8,[x24, #0x2cc] | `FALL_THROUGH`
<a id="insn-009bf004"></a> `009bf004` | `a1 56 40 f9` | ldr x1,[x21, #0xa8] | `FALL_THROUGH`
<a id="insn-009bf008"></a> `009bf008` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bf00c"></a> `009bf00c` | `62 00 80 52` | mov w2,#0x3 | `FALL_THROUGH`
<a id="insn-009bf010"></a> `009bf010` | `83 43 80 52` | mov w3,#0x21c | `FALL_THROUGH`
<a id="insn-009bf014"></a> `009bf014` | `04 0c 80 52` | mov w4,#0x60 | `FALL_THROUGH`
<a id="insn-009bf018"></a> `009bf018` | `e9 03 08 6b` | negs w9,w8 | `FALL_THROUGH`
<a id="insn-009bf01c"></a> `009bf01c` | `08 05 00 12` | and w8,w8,#0x3 | `FALL_THROUGH`
<a id="insn-009bf020"></a> `009bf020` | `05 0c 80 52` | mov w5,#0x60 | `FALL_THROUGH`
<a id="insn-009bf024"></a> `009bf024` | `29 05 00 12` | and w9,w9,#0x3 | `FALL_THROUGH`
<a id="insn-009bf028"></a> `009bf028` | `08 45 89 5a` | csneg w8,w8,w9,mi | `FALL_THROUGH`
<a id="insn-009bf02c"></a> `009bf02c` | `09 01 19 12` | and w9,w8,#0x80 | `FALL_THROUGH`
<a id="insn-009bf030"></a> `009bf030` | `08 1d 49 0b` | add w8,w8,w9, LSR #0x7 | `FALL_THROUGH`
<a id="insn-009bf034"></a> `009bf034` | `08 1d 00 13` | sxtb w8,w8 | `FALL_THROUGH`
<a id="insn-009bf038"></a> `009bf038` | `08 7d 01 53` | lsr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-009bf03c"></a> `009bf03c` | `08 31 00 11` | add w8,w8,#0xc | `FALL_THROUGH`
<a id="insn-009bf040"></a> `009bf040` | `06 1d 00 12` | and w6,w8,#0xff | `FALL_THROUGH`
<a id="insn-009bf044"></a> `009bf044` | `f0 aa ea 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-009bf048"></a> `009bf048` | `f6 16 00 90` | adrp x22,0xc9b000 | `FALL_THROUGH`
<a id="insn-009bf04c"></a> `009bf04c` | `08 f7 80 b9` | ldrsw x8,[x24, #0xf4] | `FALL_THROUGH`
<a id="insn-009bf050"></a> `009bf050` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bf054"></a> `009bf054` | `d6 56 42 f9` | ldr x22,[x22, #0x4a8] | `FALL_THROUGH`
<a id="insn-009bf058"></a> `009bf058` | `a1 56 40 f9` | ldr x1,[x21, #0xa8] | `FALL_THROUGH`
<a id="insn-009bf05c"></a> `009bf05c` | `26 01 80 52` | mov w6,#0x9 | `FALL_THROUGH`
<a id="insn-009bf060"></a> `009bf060` | `0a 2f 40 29` | ldp w10,w11,[x24] | `FALL_THROUGH`
<a id="insn-009bf064"></a> `009bf064` | `c8 7a 68 b8` | ldr w8,[x22, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-009bf068"></a> `009bf068` | `0c 37 41 29` | ldp w12,w13,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-009bf06c"></a> `009bf06c` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-009bf070"></a> `009bf070` | `09 a5 88 1a` | cinc w9,w8,lt | `FALL_THROUGH`
<a id="insn-009bf074"></a> `009bf074` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-009bf078"></a> `009bf078` | `84 01 08 0b` | add w4,w12,w8 | `FALL_THROUGH`
<a id="insn-009bf07c"></a> `009bf07c` | `a5 01 08 0b` | add w5,w13,w8 | `FALL_THROUGH`
<a id="insn-009bf080"></a> `009bf080` | `42 01 09 4b` | sub w2,w10,w9 | `FALL_THROUGH`
<a id="insn-009bf084"></a> `009bf084` | `63 01 09 4b` | sub w3,w11,w9 | `FALL_THROUGH`
<a id="insn-009bf088"></a> `009bf088` | `df aa ea 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-009bf08c"></a> `009bf08c` | `08 f7 80 b9` | ldrsw x8,[x24, #0xf4] | `FALL_THROUGH`
<a id="insn-009bf090"></a> `009bf090` | `a1 56 40 f9` | ldr x1,[x21, #0xa8] | `FALL_THROUGH`
<a id="insn-009bf094"></a> `009bf094` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bf098"></a> `009bf098` | `0a 2f 40 29` | ldp w10,w11,[x24] | `FALL_THROUGH`
<a id="insn-009bf09c"></a> `009bf09c` | `c8 7a 68 b8` | ldr w8,[x22, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-009bf0a0"></a> `009bf0a0` | `66 00 80 52` | mov w6,#0x3 | `FALL_THROUGH`
<a id="insn-009bf0a4"></a> `009bf0a4` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-009bf0a8"></a> `009bf0a8` | `04 51 01 11` | add w4,w8,#0x54 | `FALL_THROUGH`
<a id="insn-009bf0ac"></a> `009bf0ac` | `05 f1 00 11` | add w5,w8,#0x3c | `FALL_THROUGH`
<a id="insn-009bf0b0"></a> `009bf0b0` | `09 a5 88 1a` | cinc w9,w8,lt | `FALL_THROUGH`
<a id="insn-009bf0b4"></a> `009bf0b4` | `29 7d 01 13` | asr w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-009bf0b8"></a> `009bf0b8` | `4a 01 09 4b` | sub w10,w10,w9 | `FALL_THROUGH`
<a id="insn-009bf0bc"></a> `009bf0bc` | `69 01 09 4b` | sub w9,w11,w9 | `FALL_THROUGH`
<a id="insn-009bf0c0"></a> `009bf0c0` | `42 11 00 11` | add w2,w10,#0x4 | `FALL_THROUGH`
<a id="insn-009bf0c4"></a> `009bf0c4` | `23 45 00 11` | add w3,w9,#0x11 | `FALL_THROUGH`
<a id="insn-009bf0c8"></a> `009bf0c8` | `cf aa ea 97` | bl 0x00469c04 | `UNCONDITIONAL_CALL`
<a id="insn-009bf0cc"></a> `009bf0cc` | `a1 9e 40 f9` | ldr x1,[x21, #0x138] | `FALL_THROUGH`
<a id="insn-009bf0d0"></a> `009bf0d0` | `a2 be 40 f9` | ldr x2,[x21, #0x178] | `FALL_THROUGH`
<a id="insn-009bf0d4"></a> `009bf0d4` | `68 de 4c 91` | add x8,x19,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-009bf0d8"></a> `009bf0d8` | `00 41 36 91` | add x0,x8,#0xd90 | `FALL_THROUGH`
<a id="insn-009bf0dc"></a> `009bf0dc` | `a8 29 04 94` | bl 0x00ac977c | `UNCONDITIONAL_CALL`
<a id="insn-009bf0e0"></a> `009bf0e0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bf0e4"></a> `009bf0e4` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-009bf0e8"></a> `009bf0e8` | `e2 1f 80 52` | mov w2,#0xff | `FALL_THROUGH`
<a id="insn-009bf0ec"></a> `009bf0ec` | `e3 1f 80 52` | mov w3,#0xff | `FALL_THROUGH`
<a id="insn-009bf0f0"></a> `009bf0f0` | `e4 1f 80 52` | mov w4,#0xff | `FALL_THROUGH`
<a id="insn-009bf0f4"></a> `009bf0f4` | `9b a2 ea 97` | bl 0x00467b60 | `UNCONDITIONAL_CALL`
<a id="insn-009bf0f8"></a> `009bf0f8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bf0fc"></a> `009bf0fc` | `41 0e 80 52` | mov w1,#0x72 | `FALL_THROUGH`
<a id="insn-009bf100"></a> `009bf100` | `b7 a6 ea 97` | bl 0x00468bdc | `UNCONDITIONAL_CALL`
<a id="insn-009bf104"></a> `009bf104` | `68 6a 79 b8` | ldr w8,[x19, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009bf108"></a> `009bf108` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-009bf10c"></a> `009bf10c` | `0b 02 00 54` | b.lt 0x009bf14c | `CONDITIONAL_JUMP`
<a id="insn-009bf110"></a> `009bf110` | `08 cf 42 b9` | ldr w8,[x24, #0x2cc] | `FALL_THROUGH`
<a id="insn-009bf114"></a> `009bf114` | `b6 56 40 f9` | ldr x22,[x21, #0xa8] | `FALL_THROUGH`
<a id="insn-009bf118"></a> `009bf118` | `09 69 1b 53` | lsl w9,w8,#0x5 | `FALL_THROUGH`
<a id="insn-009bf11c"></a> `009bf11c` | `28 05 08 4b` | sub w8,w9,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-009bf120"></a> `009bf120` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-009bf124"></a> `009bf124` | `14 ba ea 97` | bl 0x0046d974 | `UNCONDITIONAL_CALL`
<a id="insn-009bf128"></a> `009bf128` | `01 10 27 1e` | fmov s1,0x41c00000 | `FALL_THROUGH`
<a id="insn-009bf12c"></a> `009bf12c` | `02 90 24 1e` | fmov s2,0x41200000 | `FALL_THROUGH`
<a id="insn-009bf130"></a> `009bf130` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bf134"></a> `009bf134` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-009bf138"></a> `009bf138` | `43 23 80 52` | mov w3,#0x11a | `FALL_THROUGH`
<a id="insn-009bf13c"></a> `009bf13c` | `04 01 80 52` | mov w4,#0x8 | `FALL_THROUGH`
<a id="insn-009bf140"></a> `009bf140` | `00 04 02 1f` | fmadd s0,s0,s2,s1 | `FALL_THROUGH`
<a id="insn-009bf144"></a> `009bf144` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-009bf148"></a> `009bf148` | `90 a7 ea 97` | bl 0x00468f88 | `UNCONDITIONAL_CALL`
<a id="insn-009bf14c"></a> `009bf14c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bf150"></a> `009bf150` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-009bf154"></a> `009bf154` | `c3 a6 ea 97` | bl 0x00468c60 | `UNCONDITIONAL_CALL`
<a id="insn-009bf158"></a> `009bf158` | `68 6a 7a b8` | ldr w8,[x19, x26, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009bf15c"></a> `009bf15c` | `69 6a 79 b8` | ldr w9,[x19, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-009bf160"></a> `009bf160` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-009bf164"></a> `009bf164` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-009bf168"></a> `009bf168` | `6a 02 00 54` | b.ge 0x009bf1b4 | `CONDITIONAL_JUMP`
<a id="insn-009bf16c"></a> `009bf16c` | `b5 56 40 f9` | ldr x21,[x21, #0xa8] | `FALL_THROUGH`
<a id="insn-009bf170"></a> `009bf170` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009bf174"></a> `009bf174` | `14 b6 ea 97` | bl 0x0046c9c4 | `UNCONDITIONAL_CALL`
<a id="insn-009bf178"></a> `009bf178` | `08 cf 42 b9` | ldr w8,[x24, #0x2cc] | `FALL_THROUGH`
<a id="insn-009bf17c"></a> `009bf17c` | `09 58 01 51` | sub w9,w0,#0x56 | `FALL_THROUGH`
<a id="insn-009bf180"></a> `009bf180` | `28 01 22 1e` | scvtf s8,w9 | `FALL_THROUGH`
<a id="insn-009bf184"></a> `009bf184` | `0a 69 1b 53` | lsl w10,w8,#0x5 | `FALL_THROUGH`
<a id="insn-009bf188"></a> `009bf188` | `48 05 08 4b` | sub w8,w10,w8, LSL #0x1 | `FALL_THROUGH`
<a id="insn-009bf18c"></a> `009bf18c` | `00 01 22 1e` | scvtf s0,w8 | `FALL_THROUGH`
<a id="insn-009bf190"></a> `009bf190` | `f9 b9 ea 97` | bl 0x0046d974 | `UNCONDITIONAL_CALL`
<a id="insn-009bf194"></a> `009bf194` | `01 90 34 1e` | fmov s1,0xc1200000 | `FALL_THROUGH`
<a id="insn-009bf198"></a> `009bf198` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bf19c"></a> `009bf19c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-009bf1a0"></a> `009bf1a0` | `43 23 80 52` | mov w3,#0x11a | `FALL_THROUGH`
<a id="insn-009bf1a4"></a> `009bf1a4` | `04 01 80 52` | mov w4,#0x8 | `FALL_THROUGH`
<a id="insn-009bf1a8"></a> `009bf1a8` | `00 20 01 1f` | fmadd s0,s0,s1,s8 | `FALL_THROUGH`
<a id="insn-009bf1ac"></a> `009bf1ac` | `02 00 38 1e` | fcvtzs w2,s0 | `FALL_THROUGH`
<a id="insn-009bf1b0"></a> `009bf1b0` | `76 a7 ea 97` | bl 0x00468f88 | `UNCONDITIONAL_CALL`
<a id="insn-009bf1b4"></a> `009bf1b4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bf1b8"></a> `009bf1b8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-009bf1bc"></a> `009bf1bc` | `a9 a6 ea 97` | bl 0x00468c60 | `UNCONDITIONAL_CALL`
<a id="insn-009bf1c0"></a> `009bf1c0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-009bf1c4"></a> `009bf1c4` | `e1 1f 80 52` | mov w1,#0xff | `FALL_THROUGH`
<a id="insn-009bf1c8"></a> `009bf1c8` | `85 a6 ea 97` | bl 0x00468bdc | `UNCONDITIONAL_CALL`
<a id="insn-009bf1cc"></a> `009bf1cc` | `68 de 4c 91` | add x8,x19,#0x337, LSL #12 | `FALL_THROUGH`
<a id="insn-009bf1d0"></a> `009bf1d0` | `00 c1 18 91` | add x0,x8,#0x630 | `FALL_THROUGH`
<a id="insn-009bf1d4"></a> `009bf1d4` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009bf1d8"></a> `009bf1d8` | `fb 0f 40 f9` | ldr x27,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009bf1dc"></a> `009bf1dc` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009bf1e0"></a> `009bf1e0` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009bf1e4"></a> `009bf1e4` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009bf1e8"></a> `009bf1e8` | `fd fb 40 a9` | ldp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009bf1ec"></a> `009bf1ec` | `e8 07 46 fc` | ldr d8,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-009bf1f0"></a> `009bf1f0` | `3c fc ff 17` | b 0x009be2e0 | `CALL_TERMINATOR`
<a id="insn-009bf1f4"></a> `009bf1f4` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009bf1f8"></a> `009bf1f8` | `fb 0f 40 f9` | ldr x27,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-009bf1fc"></a> `009bf1fc` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009bf200"></a> `009bf200` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009bf204"></a> `009bf204` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009bf208"></a> `009bf208` | `fd fb 40 a9` | ldp x29,x30,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009bf20c"></a> `009bf20c` | `e8 07 46 fc` | ldr d8,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-009bf210"></a> `009bf210` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009bedcc`](#insn-009bedcc) 範囲 `[['009bedcc', '009beddf']]`
  - `FALL_THROUGH` [`009beddc`](#insn-009beddc) → [`009bede0`](#insn-009bede0)
- ブロック [`009bede0`](#insn-009bede0) 範囲 `[['009bede0', '009bedf7']]`
  - `CONDITIONAL_JUMP` [`009bedf4`](#insn-009bedf4) → [`009bf1f4`](#insn-009bf1f4)
  - `FALL_THROUGH` [`009bedf4`](#insn-009bedf4) → [`009bedf8`](#insn-009bedf8)
- ブロック [`009bedf8`](#insn-009bedf8) 範囲 `[['009bedf8', '009bee1f']]`
  - `CONDITIONAL_JUMP` [`009bee1c`](#insn-009bee1c) → [`009bf1f4`](#insn-009bf1f4)
  - `FALL_THROUGH` [`009bee1c`](#insn-009bee1c) → [`009bee20`](#insn-009bee20)
- ブロック [`009bee20`](#insn-009bee20) 範囲 `[['009bee20', '009bee6f']]`
  - `FALL_THROUGH` [`009bee6c`](#insn-009bee6c) → [`009bee70`](#insn-009bee70)
- ブロック [`009bee70`](#insn-009bee70) 範囲 `[['009bee70', '009bee97']]`
  - `FALL_THROUGH` [`009bee94`](#insn-009bee94) → [`009bee98`](#insn-009bee98)
- ブロック [`009bee98`](#insn-009bee98) 範囲 `[['009bee98', '009beecb']]`
  - `FALL_THROUGH` [`009beec8`](#insn-009beec8) → [`009beecc`](#insn-009beecc)
- ブロック [`009beecc`](#insn-009beecc) 範囲 `[['009beecc', '009befcf']]`
  - `CONDITIONAL_JUMP` [`009befcc`](#insn-009befcc) → [`009bf048`](#insn-009bf048)
  - `FALL_THROUGH` [`009befcc`](#insn-009befcc) → [`009befd0`](#insn-009befd0)
- ブロック [`009befd0`](#insn-009befd0) 範囲 `[['009befd0', '009befd7']]`
  - `CONDITIONAL_JUMP` [`009befd4`](#insn-009befd4) → [`009bf048`](#insn-009bf048)
  - `FALL_THROUGH` [`009befd4`](#insn-009befd4) → [`009befd8`](#insn-009befd8)
- ブロック [`009befd8`](#insn-009befd8) 範囲 `[['009befd8', '009befdf']]`
  - `CONDITIONAL_JUMP` [`009befdc`](#insn-009befdc) → [`009bf048`](#insn-009bf048)
  - `FALL_THROUGH` [`009befdc`](#insn-009befdc) → [`009befe0`](#insn-009befe0)
- ブロック [`009befe0`](#insn-009befe0) 範囲 `[['009befe0', '009befe7']]`
  - `CONDITIONAL_JUMP` [`009befe4`](#insn-009befe4) → [`009bf048`](#insn-009bf048)
  - `FALL_THROUGH` [`009befe4`](#insn-009befe4) → [`009befe8`](#insn-009befe8)
- ブロック [`009befe8`](#insn-009befe8) 範囲 `[['009befe8', '009befef']]`
  - `CONDITIONAL_JUMP` [`009befec`](#insn-009befec) → [`009bf048`](#insn-009bf048)
  - `FALL_THROUGH` [`009befec`](#insn-009befec) → [`009beff0`](#insn-009beff0)
- ブロック [`009beff0`](#insn-009beff0) 範囲 `[['009beff0', '009beff7']]`
  - `CONDITIONAL_JUMP` [`009beff4`](#insn-009beff4) → [`009bf048`](#insn-009bf048)
  - `FALL_THROUGH` [`009beff4`](#insn-009beff4) → [`009beff8`](#insn-009beff8)
- ブロック [`009beff8`](#insn-009beff8) 範囲 `[['009beff8', '009befff']]`
  - `CONDITIONAL_JUMP` [`009beffc`](#insn-009beffc) → [`009bf048`](#insn-009bf048)
  - `FALL_THROUGH` [`009beffc`](#insn-009beffc) → [`009bf000`](#insn-009bf000)
- ブロック [`009bf000`](#insn-009bf000) 範囲 `[['009bf000', '009bf013']]`
  - `FALL_THROUGH` [`009bf010`](#insn-009bf010) → [`009bf014`](#insn-009bf014)
- ブロック [`009bf014`](#insn-009bf014) 範囲 `[['009bf014', '009bf047']]`
  - `FALL_THROUGH` [`009bf044`](#insn-009bf044) → [`009bf048`](#insn-009bf048)
- ブロック [`009bf048`](#insn-009bf048) 範囲 `[['009bf048', '009bf04f']]`
  - `FALL_THROUGH` [`009bf04c`](#insn-009bf04c) → [`009bf050`](#insn-009bf050)
- ブロック [`009bf050`](#insn-009bf050) 範囲 `[['009bf050', '009bf10f']]`
  - `CONDITIONAL_JUMP` [`009bf10c`](#insn-009bf10c) → [`009bf14c`](#insn-009bf14c)
  - `FALL_THROUGH` [`009bf10c`](#insn-009bf10c) → [`009bf110`](#insn-009bf110)
- ブロック [`009bf110`](#insn-009bf110) 範囲 `[['009bf110', '009bf14b']]`
  - `FALL_THROUGH` [`009bf148`](#insn-009bf148) → [`009bf14c`](#insn-009bf14c)
- ブロック [`009bf14c`](#insn-009bf14c) 範囲 `[['009bf14c', '009bf16b']]`
  - `CONDITIONAL_JUMP` [`009bf168`](#insn-009bf168) → [`009bf1b4`](#insn-009bf1b4)
  - `FALL_THROUGH` [`009bf168`](#insn-009bf168) → [`009bf16c`](#insn-009bf16c)
- ブロック [`009bf16c`](#insn-009bf16c) 範囲 `[['009bf16c', '009bf19b']]`
  - `FALL_THROUGH` [`009bf198`](#insn-009bf198) → [`009bf19c`](#insn-009bf19c)
- ブロック [`009bf19c`](#insn-009bf19c) 範囲 `[['009bf19c', '009bf1b3']]`
  - `FALL_THROUGH` [`009bf1b0`](#insn-009bf1b0) → [`009bf1b4`](#insn-009bf1b4)
- ブロック [`009bf1b4`](#insn-009bf1b4) 範囲 `[['009bf1b4', '009bf1bb']]`
  - `FALL_THROUGH` [`009bf1b8`](#insn-009bf1b8) → [`009bf1bc`](#insn-009bf1bc)
- ブロック [`009bf1bc`](#insn-009bf1bc) 範囲 `[['009bf1bc', '009bf1ef']]`
  - `FALL_THROUGH` [`009bf1ec`](#insn-009bf1ec) → [`009bf1f0`](#insn-009bf1f0)
- ブロック [`009bf1f0`](#insn-009bf1f0) 範囲 `[['009bf1f0', '009bf1f3']]`
- ブロック [`009bf1f4`](#insn-009bf1f4) 範囲 `[['009bf1f4', '009bf20b']]`
  - `FALL_THROUGH` [`009bf208`](#insn-009bf208) → [`009bf20c`](#insn-009bf20c)
- ブロック [`009bf20c`](#insn-009bf20c) 範囲 `[['009bf20c', '009bf213']]`

## 命令位置別の参照

- [`009bedcc`](#insn-009bedcc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bedd0`](#insn-009bedd0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bedd4`](#insn-009bedd4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bedd8`](#insn-009bedd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009beddc`](#insn-009beddc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bede0`](#insn-009bede0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bede4`](#insn-009bede4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bedf0`](#insn-009bedf0) → `00ca4978`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`009bedf4`](#insn-009bedf4) → [`009bf1f4`](#insn-009bf1f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bee04`](#insn-009bee04) → `00c65e58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`009bee0c`](#insn-009bee0c) → `00c89680`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x10)))`
- [`009bee18`](#insn-009bee18) → [`00c58610`](../00c58/00c58610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58610` · 推定シンボル `None` · 推定型 `None`
- [`009bee1c`](#insn-009bee1c) → [`009bf1f4`](#insn-009bf1f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bee58`](#insn-009bee58) → [`00467b60`](../00467/00467b60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b60` · 推定シンボル `None` · 推定型 `None`
- [`009bee64`](#insn-009bee64) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`009bee6c`](#insn-009bee6c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`009bee70`](#insn-009bee70) → [`0046ca84`](../0046c/0046ca84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca84` · 推定シンボル `None` · 推定型 `None`
- [`009bee90`](#insn-009bee90) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`009beea8`](#insn-009beea8) → [`00467b60`](../00467/00467b60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b60` · 推定シンボル `None` · 推定型 `None`
- [`009beeac`](#insn-009beeac) → `00333f9c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009beeb4`](#insn-009beeb4) → [`0046d9ac`](../0046d/0046d9ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d9ac` · 推定シンボル `None` · 推定型 `None`
- [`009beed0`](#insn-009beed0) → [`00468bdc`](../00468/00468bdc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468bdc` · 推定シンボル `None` · 推定型 `None`
- [`009beedc`](#insn-009beedc) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`009beefc`](#insn-009beefc) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`009bef14`](#insn-009bef14) → [`00467b60`](../00467/00467b60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b60` · 推定シンボル `None` · 推定型 `None`
- [`009bef20`](#insn-009bef20) → [`00468c60`](../00468/00468c60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468c60` · 推定シンボル `None` · 推定型 `None`
- [`009bef34`](#insn-009bef34) → [`008614b0`](../00861/008614b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008614b0` · 推定シンボル `None` · 推定型 `None`
- [`009bef40`](#insn-009bef40) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`009bef60`](#insn-009bef60) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`009bef6c`](#insn-009bef6c) → [`00468c60`](../00468/00468c60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468c60` · 推定シンボル `None` · 推定型 `None`
- [`009bef78`](#insn-009bef78) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`009bef98`](#insn-009bef98) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`009befa4`](#insn-009befa4) → [`00468c60`](../00468/00468c60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468c60` · 推定シンボル `None` · 推定型 `None`
- [`009befa8`](#insn-009befa8) → `00334170`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009befc4`](#insn-009befc4) → [`00468f88`](../00468/00468f88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468f88` · 推定シンボル `None` · 推定型 `None`
- [`009befc8`](#insn-009befc8) → `00332a24`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009befcc`](#insn-009befcc) → [`009bf048`](#insn-009bf048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009befd0`](#insn-009befd0) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009befd4`](#insn-009befd4) → [`009bf048`](#insn-009bf048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009befd8`](#insn-009befd8) → `00332a2d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009befdc`](#insn-009befdc) → [`009bf048`](#insn-009bf048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009befe0`](#insn-009befe0) → `00332a31`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009befe4`](#insn-009befe4) → [`009bf048`](#insn-009bf048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009befe8`](#insn-009befe8) → `00332a26`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009befec`](#insn-009befec) → [`009bf048`](#insn-009bf048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009beff0`](#insn-009beff0) → `00332060`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009beff4`](#insn-009beff4) → [`009bf048`](#insn-009bf048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009beff8`](#insn-009beff8) → `00332a2e`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009beffc`](#insn-009beffc) → [`009bf048`](#insn-009bf048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf000`](#insn-009bf000) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf044`](#insn-009bf044) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`009bf04c`](#insn-009bf04c) → `00333dc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf054`](#insn-009bf054) → `00c9b4a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`009bf060`](#insn-009bf060) → `00333ccc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf060`](#insn-009bf060) → `00333cd0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf064`](#insn-009bf064) → `00ca4484`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf068`](#insn-009bf068) → `00333cd4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf068`](#insn-009bf068) → `00333cd8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf088`](#insn-009bf088) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`009bf08c`](#insn-009bf08c) → `00333dc0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf098`](#insn-009bf098) → `00333ccc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf098`](#insn-009bf098) → `00333cd0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf09c`](#insn-009bf09c) → `00ca4484`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf0c8`](#insn-009bf0c8) → [`00469c04`](../00469/00469c04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469c04` · 推定シンボル `None` · 推定型 `None`
- [`009bf0dc`](#insn-009bf0dc) → [`00ac977c`](../00ac9/00ac977c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ac977c` · 推定シンボル `None` · 推定型 `None`
- [`009bf0f4`](#insn-009bf0f4) → [`00467b60`](../00467/00467b60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00467b60` · 推定シンボル `None` · 推定型 `None`
- [`009bf100`](#insn-009bf100) → [`00468bdc`](../00468/00468bdc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468bdc` · 推定シンボル `None` · 推定型 `None`
- [`009bf104`](#insn-009bf104) → `00337670`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf10c`](#insn-009bf10c) → [`009bf14c`](#insn-009bf14c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf110`](#insn-009bf110) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf124`](#insn-009bf124) → [`0046d974`](../0046d/0046d974.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d974` · 推定シンボル `None` · 推定型 `None`
- [`009bf148`](#insn-009bf148) → [`00468f88`](../00468/00468f88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468f88` · 推定シンボル `None` · 推定型 `None`
- [`009bf154`](#insn-009bf154) → [`00468c60`](../00468/00468c60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468c60` · 推定シンボル `None` · 推定型 `None`
- [`009bf158`](#insn-009bf158) → `00335f78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf15c`](#insn-009bf15c) → `00337670`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf168`](#insn-009bf168) → [`009bf1b4`](#insn-009bf1b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf174`](#insn-009bf174) → [`0046c9c4`](../0046c/0046c9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046c9c4` · 推定シンボル `None` · 推定型 `None`
- [`009bf178`](#insn-009bf178) → `00333f98`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`009bf190`](#insn-009bf190) → [`0046d974`](../0046d/0046d974.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046d974` · 推定シンボル `None` · 推定型 `None`
- [`009bf1b0`](#insn-009bf1b0) → [`00468f88`](../00468/00468f88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468f88` · 推定シンボル `None` · 推定型 `None`
- [`009bf1bc`](#insn-009bf1bc) → [`00468c60`](../00468/00468c60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468c60` · 推定シンボル `None` · 推定型 `None`
- [`009bf1c8`](#insn-009bf1c8) → [`00468bdc`](../00468/00468bdc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00468bdc` · 推定シンボル `None` · 推定型 `None`
- [`009bf1d4`](#insn-009bf1d4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf1d8`](#insn-009bf1d8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf1dc`](#insn-009bf1dc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf1e0`](#insn-009bf1e0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf1e4`](#insn-009bf1e4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf1e8`](#insn-009bf1e8) → `Stack[-0x58]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf1f0`](#insn-009bf1f0) → [`009be2e0`](009be2e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009be2e0` · 推定シンボル `None` · 推定型 `None`
- [`009bf1f4`](#insn-009bf1f4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf1f8`](#insn-009bf1f8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf1fc`](#insn-009bf1fc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf200`](#insn-009bf200) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf204`](#insn-009bf204) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009bf208`](#insn-009bf208) → `Stack[-0x58]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009bedcc`](#insn-009bedcc)

~~~json
{
  "source": "009bedcc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bedd0`](#insn-009bedd0)

~~~json
{
  "source": "009bedd0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bedd4`](#insn-009bedd4)

~~~json
{
  "source": "009bedd4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bedd8`](#insn-009bedd8)

~~~json
{
  "source": "009bedd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009beddc`](#insn-009beddc)

~~~json
{
  "source": "009beddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bede0`](#insn-009bede0)

~~~json
{
  "source": "009bede0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bede4`](#insn-009bede4)

~~~json
{
  "source": "009bede4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bedf0`](#insn-009bedf0)

~~~json
{
  "source": "009bedf0",
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
- 参照命令 [`009bedf4`](#insn-009bedf4)

~~~json
{
  "source": "009bedf4",
  "target": "009bf1f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bee04`](#insn-009bee04)

~~~json
{
  "source": "009bee04",
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
- 参照命令 [`009bee0c`](#insn-009bee0c)

~~~json
{
  "source": "009bee0c",
  "target": "00c89680",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c89680",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009bee18`](#insn-009bee18)

~~~json
{
  "source": "009bee18",
  "target": "00c58610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bee1c`](#insn-009bee1c)

~~~json
{
  "source": "009bee1c",
  "target": "009bf1f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bee58`](#insn-009bee58)

~~~json
{
  "source": "009bee58",
  "target": "00467b60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bee64`](#insn-009bee64)

~~~json
{
  "source": "009bee64",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bee6c`](#insn-009bee6c)

~~~json
{
  "source": "009bee6c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bee70`](#insn-009bee70)

~~~json
{
  "source": "009bee70",
  "target": "0046ca84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bee90`](#insn-009bee90)

~~~json
{
  "source": "009bee90",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009beea8`](#insn-009beea8)

~~~json
{
  "source": "009beea8",
  "target": "00467b60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009beeac`](#insn-009beeac)

~~~json
{
  "source": "009beeac",
  "target": "00333f9c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "80b96c00048e0900",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009beeb4`](#insn-009beeb4)

~~~json
{
  "source": "009beeb4",
  "target": "0046d9ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009beed0`](#insn-009beed0)

~~~json
{
  "source": "009beed0",
  "target": "00468bdc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009beedc`](#insn-009beedc)

~~~json
{
  "source": "009beedc",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009beefc`](#insn-009beefc)

~~~json
{
  "source": "009beefc",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bef14`](#insn-009bef14)

~~~json
{
  "source": "009bef14",
  "target": "00467b60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bef20`](#insn-009bef20)

~~~json
{
  "source": "009bef20",
  "target": "00468c60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bef34`](#insn-009bef34)

~~~json
{
  "source": "009bef34",
  "target": "008614b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bef40`](#insn-009bef40)

~~~json
{
  "source": "009bef40",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bef60`](#insn-009bef60)

~~~json
{
  "source": "009bef60",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bef6c`](#insn-009bef6c)

~~~json
{
  "source": "009bef6c",
  "target": "00468c60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bef78`](#insn-009bef78)

~~~json
{
  "source": "009bef78",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bef98`](#insn-009bef98)

~~~json
{
  "source": "009bef98",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009befa4`](#insn-009befa4)

~~~json
{
  "source": "009befa4",
  "target": "00468c60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009befa8`](#insn-009befa8)

~~~json
{
  "source": "009befa8",
  "target": "00334170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334170",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6c266d00bc950900",
  "capture_start": "00334170",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009befc4`](#insn-009befc4)

~~~json
{
  "source": "009befc4",
  "target": "00468f88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009befc8`](#insn-009befc8)

~~~json
{
  "source": "009befc8",
  "target": "00332a24",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4f96800bc470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009befcc`](#insn-009befcc)

~~~json
{
  "source": "009befcc",
  "target": "009bf048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009befd0`](#insn-009befd0)

~~~json
{
  "source": "009befd0",
  "target": "00332a25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4f96800bc470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009befd4`](#insn-009befd4)

~~~json
{
  "source": "009befd4",
  "target": "009bf048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009befd8`](#insn-009befd8)

~~~json
{
  "source": "009befd8",
  "target": "00332a2d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 5,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e8f96800d0470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009befdc`](#insn-009befdc)

~~~json
{
  "source": "009befdc",
  "target": "009bf048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009befe0`](#insn-009befe0)

~~~json
{
  "source": "009befe0",
  "target": "00332a31",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a30",
  "offset": 1,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "30fa6800f8470900",
  "capture_start": "00332a30",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009befe4`](#insn-009befe4)

~~~json
{
  "source": "009befe4",
  "target": "009bf048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009befe8`](#insn-009befe8)

~~~json
{
  "source": "009befe8",
  "target": "00332a26",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a20",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e4f96800bc470900",
  "capture_start": "00332a20",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009befec`](#insn-009befec)

~~~json
{
  "source": "009befec",
  "target": "009bf048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009beff0`](#insn-009beff0)

~~~json
{
  "source": "009beff0",
  "target": "00332060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332060",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "cc04620064240900",
  "capture_start": "00332060",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009beff4`](#insn-009beff4)

~~~json
{
  "source": "009beff4",
  "target": "009bf048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009beff8`](#insn-009beff8)

~~~json
{
  "source": "009beff8",
  "target": "00332a2e",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00332a28",
  "offset": 6,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "e8f96800d0470900",
  "capture_start": "00332a28",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009beffc`](#insn-009beffc)

~~~json
{
  "source": "009beffc",
  "target": "009bf048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf000`](#insn-009bf000)

~~~json
{
  "source": "009bf000",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "80b96c00048e0900",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf044`](#insn-009bf044)

~~~json
{
  "source": "009bf044",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf04c`](#insn-009bf04c)

~~~json
{
  "source": "009bf04c",
  "target": "00333dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333dc0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d8f96b0044211100",
  "capture_start": "00333dc0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf054`](#insn-009bf054)

~~~json
{
  "source": "009bf054",
  "target": "00c9b4a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b4a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`009bf060`](#insn-009bf060)

~~~json
{
  "source": "009bf060",
  "target": "00333ccc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cc8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "44476b0018820900",
  "capture_start": "00333cc8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf060`](#insn-009bf060)

~~~json
{
  "source": "009bf060",
  "target": "00333cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "ac496b0050820900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf064`](#insn-009bf064)

~~~json
{
  "source": "009bf064",
  "target": "00ca4484",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf068`](#insn-009bf068)

~~~json
{
  "source": "009bf068",
  "target": "00333cd4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "ac496b0050820900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf068`](#insn-009bf068)

~~~json
{
  "source": "009bf068",
  "target": "00333cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "c0496b006c820900",
  "capture_start": "00333cd8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf088`](#insn-009bf088)

~~~json
{
  "source": "009bf088",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf08c`](#insn-009bf08c)

~~~json
{
  "source": "009bf08c",
  "target": "00333dc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333dc0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "d8f96b0044211100",
  "capture_start": "00333dc0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf098`](#insn-009bf098)

~~~json
{
  "source": "009bf098",
  "target": "00333ccc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cc8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "44476b0018820900",
  "capture_start": "00333cc8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf098`](#insn-009bf098)

~~~json
{
  "source": "009bf098",
  "target": "00333cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333cd0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "ac496b0050820900",
  "capture_start": "00333cd0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf09c`](#insn-009bf09c)

~~~json
{
  "source": "009bf09c",
  "target": "00ca4484",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf0c8`](#insn-009bf0c8)

~~~json
{
  "source": "009bf0c8",
  "target": "00469c04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf0dc`](#insn-009bf0dc)

~~~json
{
  "source": "009bf0dc",
  "target": "00ac977c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf0f4`](#insn-009bf0f4)

~~~json
{
  "source": "009bf0f4",
  "target": "00467b60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf100`](#insn-009bf100)

~~~json
{
  "source": "009bf100",
  "target": "00468bdc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf104`](#insn-009bf104)

~~~json
{
  "source": "009bf104",
  "target": "00337670",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00337670",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "34f27a00b48f1100",
  "capture_start": "00337670",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf10c`](#insn-009bf10c)

~~~json
{
  "source": "009bf10c",
  "target": "009bf14c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf110`](#insn-009bf110)

~~~json
{
  "source": "009bf110",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "80b96c00048e0900",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf124`](#insn-009bf124)

~~~json
{
  "source": "009bf124",
  "target": "0046d974",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf148`](#insn-009bf148)

~~~json
{
  "source": "009bf148",
  "target": "00468f88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf154`](#insn-009bf154)

~~~json
{
  "source": "009bf154",
  "target": "00468c60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf158`](#insn-009bf158)

~~~json
{
  "source": "009bf158",
  "target": "00335f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00335f78",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "747f750068ff0900",
  "capture_start": "00335f78",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf15c`](#insn-009bf15c)

~~~json
{
  "source": "009bf15c",
  "target": "00337670",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00337670",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "34f27a00b48f1100",
  "capture_start": "00337670",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf168`](#insn-009bf168)

~~~json
{
  "source": "009bf168",
  "target": "009bf1b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf174`](#insn-009bf174)

~~~json
{
  "source": "009bf174",
  "target": "0046c9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf178`](#insn-009bf178)

~~~json
{
  "source": "009bf178",
  "target": "00333f98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f98",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "80b96c00048e0900",
  "capture_start": "00333f98",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`009bf190`](#insn-009bf190)

~~~json
{
  "source": "009bf190",
  "target": "0046d974",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf1b0`](#insn-009bf1b0)

~~~json
{
  "source": "009bf1b0",
  "target": "00468f88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf1bc`](#insn-009bf1bc)

~~~json
{
  "source": "009bf1bc",
  "target": "00468c60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf1c8`](#insn-009bf1c8)

~~~json
{
  "source": "009bf1c8",
  "target": "00468bdc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf1d4`](#insn-009bf1d4)

~~~json
{
  "source": "009bf1d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf1d8`](#insn-009bf1d8)

~~~json
{
  "source": "009bf1d8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf1dc`](#insn-009bf1dc)

~~~json
{
  "source": "009bf1dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf1e0`](#insn-009bf1e0)

~~~json
{
  "source": "009bf1e0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf1e4`](#insn-009bf1e4)

~~~json
{
  "source": "009bf1e4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf1e8`](#insn-009bf1e8)

~~~json
{
  "source": "009bf1e8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf1f0`](#insn-009bf1f0)

~~~json
{
  "source": "009bf1f0",
  "target": "009be2e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009bf1f4`](#insn-009bf1f4)

~~~json
{
  "source": "009bf1f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf1f8`](#insn-009bf1f8)

~~~json
{
  "source": "009bf1f8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf1fc`](#insn-009bf1fc)

~~~json
{
  "source": "009bf1fc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf200`](#insn-009bf200)

~~~json
{
  "source": "009bf200",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf204`](#insn-009bf204)

~~~json
{
  "source": "009bf204",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009bf208`](#insn-009bf208)

~~~json
{
  "source": "009bf208",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
