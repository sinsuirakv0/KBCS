# 00abbd3c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00abad48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aba/00abad48.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0066.md#compare-80611defa0dae9931d6d828d786aa91e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abbd3c",
  "name": "FUN_00abbd3c",
  "size": 676,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2bba40da582e96b93d1e1d5aaf37d25c82ffca55887efd6fab44c2f1d45b30d7",
  "source_text_sha256": "2bba40da582e96b93d1e1d5aaf37d25c82ffca55887efd6fab44c2f1d45b30d7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abbd3c",
        "00abbfdf"
      ]
    ],
    "bytes_sha256": "51cef13d5ce806675d8ce82508efaec48797ae37681df1847600737652dbdf7e",
    "instruction_count": 169,
    "instruction_bytes": 676,
    "body_bytes": 676,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005fea5c](../005fe/005fea5c.md)
- [00ab4208](../00ab4/00ab4208.md)
- [00ab77a4](../00ab7/00ab77a4.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [008524fc](../00852/008524fc.md)
- [00aba21c](../00aba/00aba21c.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5054 bytes

~~~c

bool FUN_00abbd3c(int param_1,undefined4 param_2)

{
  long lVar1;
  long lVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long lVar6;
  bool bVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  long lVar10;
  int iVar11;
  int local_98 [2];
  void *local_90;
  void *local_88;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  if (param_1 == 3) {
    bVar7 = false;
  }
  else {
    lVar10 = 0;
    do {
      lVar2 = FUN_008524fc();
                    /* try { // try from 00abbdc0 to 00bbbdcb has its CatchHandler @ 00abdcd8 */
      FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
                    /* try { // try from 00abbdcc to 00bbbddf has its CatchHandler @ 00abdcb4 */
      lVar2 = (long)local_98[0];
      bVar7 = lVar2 <= lVar10;
      if (local_90 != (void *)0x0) {
        local_88 = local_90;
        _ZdlPv(local_90);
      }
      if (lVar2 <= lVar10) {
        bVar7 = true;
        break;
      }
      lVar2 = FUN_008524fc();
      FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
      iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      local_88 = local_90;
      _ZdlPv(local_90);
                    /* try { // try from 00abbe18 to 00bbbe23 has its CatchHandler @ 00abdc40 */
      if (iVar11 < 0x2e) {
        lVar2 = FUN_008524fc();
                    /* try { // try from 00abbe24 to 00bbbe33 has its CatchHandler @ 00abdb94 */
                    /* try { // try from 00abbe34 to 00bbbe4f has its CatchHandler @ 00abdafc */
        FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = 0x2d - *(int *)((long)local_90 + lVar10 * 4);
      }
      else {
                    /* try { // try from 00abbe50 to 00bbbfb3 has its CatchHandler @ 00abbd00 */
        lVar2 = FUN_008524fc();
        FUN_00aba21c(local_98,(long)&uleb128_0029a6e0 + lVar2,param_1,param_2);
        iVar11 = *(int *)((long)local_90 + lVar10 * 4);
      }
      local_88 = local_90;
      _ZdlPv(local_90);
      lVar2 = FUN_008524fc();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2);
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar5, puVar9 = puVar3, param_1 < *(int *)(puVar3 + 4)) {
            puVar5 = (undefined8 *)*puVar3;
            puVar8 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abbec0;
          }
          if (param_1 <= *(int *)(puVar3 + 4)) goto LAB_00abbf1c;
          puVar5 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar8 = puVar3 + 1;
      }
LAB_00abbec0:
      puVar3 = (undefined8 *)_Znwm(0x40);
      *(int *)(puVar3 + 4) = param_1;
      puVar3[7] = 0;
      puVar3[6] = 0;
      puVar3[5] = puVar3 + 6;
      *puVar3 = 0;
      puVar3[1] = 0;
      puVar3[2] = puVar9;
      *puVar8 = puVar3;
      lVar6 = **(long **)((long)&fde_table_entry_003380d0.initial_loc + lVar2);
      puVar5 = puVar3;
      if (lVar6 != 0) {
        *(long *)((long)&fde_table_entry_003380d0.initial_loc + lVar2) = lVar6;
        puVar5 = (undefined8 *)*puVar8;
      }
      FUN_0043bf04(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar2),puVar5);
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar2) + 1;
LAB_00abbf1c:
      puVar8 = puVar3 + 6;
      puVar5 = (undefined8 *)*puVar8;
      puVar9 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar4 = puVar5, puVar9 = puVar4, iVar11 < *(int *)((long)puVar4 + 0x1c)) {
            puVar5 = (undefined8 *)*puVar4;
            puVar8 = puVar4;
            if ((undefined8 *)*puVar4 == (undefined8 *)0x0) goto LAB_00abbf60;
          }
          if (iVar11 <= *(int *)((long)puVar4 + 0x1c)) goto LAB_00abbda8;
          puVar5 = (undefined8 *)puVar4[1];
        } while ((undefined8 *)puVar4[1] != (undefined8 *)0x0);
        puVar8 = puVar4 + 1;
      }
LAB_00abbf60:
      puVar4 = (undefined8 *)_Znwm(0x28);
      *(int *)((long)puVar4 + 0x1c) = iVar11;
      *(undefined1 *)(puVar4 + 4) = 0;
      *puVar4 = 0;
      puVar4[1] = 0;
      puVar4[2] = puVar9;
      *puVar8 = puVar4;
      puVar5 = puVar4;
      if (*(long *)puVar3[5] != 0) {
        puVar3[5] = *(long *)puVar3[5];
        puVar5 = (undefined8 *)*puVar8;
      }
      FUN_0043bf04(puVar3[6],puVar5);
                    /* try { // try from 00abbd9c to 00bbbda3 has its CatchHandler @ 00abdcf4 */
      puVar3[7] = puVar3[7] + 1;
LAB_00abbda8:
      lVar10 = lVar10 + 1;
    } while ((*(byte *)(puVar4 + 4) & 1) != 0);
  }
                    /* try { // try from 00abbfb4 to 00bbbfc3 has its CatchHandler @ 00abda58 */
  if (*(long *)(lVar1 + 0x28) != local_68) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return bVar7;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abbd3c"></a> `00abbd3c` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00abbd40"></a> `00abbd40` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abbd44"></a> `00abbd44` | `fc 6f 05 a9` | stp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abbd48"></a> `00abbd48` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abbd4c"></a> `00abbd4c` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abbd50"></a> `00abbd50` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abbd54"></a> `00abbd54` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abbd58"></a> `00abbd58` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00abbd5c"></a> `00abbd5c` | `49 d0 3b d5` | mrs x9,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00abbd60"></a> `00abbd60` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00abbd64"></a> `00abbd64` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00abbd68"></a> `00abbd68` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abbd6c"></a> `00abbd6c` | `61 00 00 54` | b.ne 0x00abbd78 | `CONDITIONAL_JUMP`
<a id="insn-00abbd70"></a> `00abbd70` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00abbd74"></a> `00abbd74` | `8d 00 00 14` | b 0x00abbfa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abbd78"></a> `00abbd78` | `1a dc 94 52` | mov w26,#0xa6e0 | `FALL_THROUGH`
<a id="insn-00abbd7c"></a> `00abbd7c` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00abbd80"></a> `00abbd80` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abbd84"></a> `00abbd84` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00abbd88"></a> `00abbd88` | `3a 05 a0 72` | movk w26,#0x29, LSL #16 | `FALL_THROUGH`
<a id="insn-00abbd8c"></a> `00abbd8c` | `e9 03 00 f9` | str x9,[sp] | `FALL_THROUGH`
<a id="insn-00abbd90"></a> `00abbd90` | `09 00 00 14` | b 0x00abbdb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abbd94"></a> `00abbd94` | `60 1b 40 f9` | ldr x0,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00abbd98"></a> `00abbd98` | `5b 00 e6 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-00abbd9c"></a> `00abbd9c` | `68 1f 40 f9` | ldr x8,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00abbda0"></a> `00abbda0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abbda4"></a> `00abbda4` | `68 1f 00 f9` | str x8,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00abbda8"></a> `00abbda8` | `e8 82 40 39` | ldrb w8,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00abbdac"></a> `00abbdac` | `39 07 00 91` | add x25,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00abbdb0"></a> `00abbdb0` | `a8 0f 00 36` | tbz w8,#0x0,0x00abbfa4 | `CONDITIONAL_JUMP`
<a id="insn-00abbdb4"></a> `00abbdb4` | `d2 59 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00abbdb8"></a> `00abbdb8` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abbdbc"></a> `00abbdbc` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abbdc0"></a> `00abbdc0` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abbdc4"></a> `00abbdc4` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00abbdc8"></a> `00abbdc8` | `15 f9 ff 97` | bl 0x00aba21c | `UNCONDITIONAL_CALL`
<a id="insn-00abbdcc"></a> `00abbdcc` | `f6 0b 80 b9` | ldrsw x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00abbdd0"></a> `00abbdd0` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abbdd4"></a> `00abbdd4` | `3f 03 16 eb` | cmp x25,x22 | `FALL_THROUGH`
<a id="insn-00abbdd8"></a> `00abbdd8` | `f5 b7 9f 1a` | cset w21,ge | `FALL_THROUGH`
<a id="insn-00abbddc"></a> `00abbddc` | `60 00 00 b4` | cbz x0,0x00abbde8 | `CONDITIONAL_JUMP`
<a id="insn-00abbde0"></a> `00abbde0` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abbde4"></a> `00abbde4` | `5b 74 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abbde8"></a> `00abbde8` | `3f 03 16 eb` | cmp x25,x22 | `FALL_THROUGH`
<a id="insn-00abbdec"></a> `00abbdec` | `aa 0d 00 54` | b.ge 0x00abbfa0 | `CONDITIONAL_JUMP`
<a id="insn-00abbdf0"></a> `00abbdf0` | `c3 59 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00abbdf4"></a> `00abbdf4` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abbdf8"></a> `00abbdf8` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abbdfc"></a> `00abbdfc` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abbe00"></a> `00abbe00` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00abbe04"></a> `00abbe04` | `06 f9 ff 97` | bl 0x00aba21c | `UNCONDITIONAL_CALL`
<a id="insn-00abbe08"></a> `00abbe08` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abbe0c"></a> `00abbe0c` | `16 78 79 b8` | ldr w22,[x0, x25, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abbe10"></a> `00abbe10` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abbe14"></a> `00abbe14` | `4f 74 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abbe18"></a> `00abbe18` | `df b6 00 71` | cmp w22,#0x2d | `FALL_THROUGH`
<a id="insn-00abbe1c"></a> `00abbe1c` | `ac 01 00 54` | b.gt 0x00abbe50 | `CONDITIONAL_JUMP`
<a id="insn-00abbe20"></a> `00abbe20` | `b7 59 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00abbe24"></a> `00abbe24` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abbe28"></a> `00abbe28` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abbe2c"></a> `00abbe2c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abbe30"></a> `00abbe30` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00abbe34"></a> `00abbe34` | `fa f8 ff 97` | bl 0x00aba21c | `UNCONDITIONAL_CALL`
<a id="insn-00abbe38"></a> `00abbe38` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abbe3c"></a> `00abbe3c` | `a9 05 80 52` | mov w9,#0x2d | `FALL_THROUGH`
<a id="insn-00abbe40"></a> `00abbe40` | `08 78 79 b8` | ldr w8,[x0, x25, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abbe44"></a> `00abbe44` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abbe48"></a> `00abbe48` | `3c 01 08 4b` | sub w28,w9,w8 | `FALL_THROUGH`
<a id="insn-00abbe4c"></a> `00abbe4c` | `0a 00 00 14` | b 0x00abbe74 | `UNCONDITIONAL_JUMP`
<a id="insn-00abbe50"></a> `00abbe50` | `ab 59 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00abbe54"></a> `00abbe54` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00abbe58"></a> `00abbe58` | `00 00 1a 8b` | add x0,x0,x26 | `FALL_THROUGH`
<a id="insn-00abbe5c"></a> `00abbe5c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abbe60"></a> `00abbe60` | `e2 03 13 2a` | mov w2,w19 | `FALL_THROUGH`
<a id="insn-00abbe64"></a> `00abbe64` | `ee f8 ff 97` | bl 0x00aba21c | `UNCONDITIONAL_CALL`
<a id="insn-00abbe68"></a> `00abbe68` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abbe6c"></a> `00abbe6c` | `1c 78 79 b8` | ldr w28,[x0, x25, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00abbe70"></a> `00abbe70` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00abbe74"></a> `00abbe74` | `37 74 06 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00abbe78"></a> `00abbe78` | `a1 59 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00abbe7c"></a> `00abbe7c` | `17 e0 4c 91` | add x23,x0,#0x338, LSL #12 | `FALL_THROUGH`
<a id="insn-00abbe80"></a> `00abbe80` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00abbe84"></a> `00abbe84` | `c8 8e 4d f8` | ldr x8,[x22, #0xd8]! | `FALL_THROUGH`
<a id="insn-00abbe88"></a> `00abbe88` | `c8 00 00 b5` | cbnz x8,0x00abbea0 | `CONDITIONAL_JUMP`
<a id="insn-00abbe8c"></a> `00abbe8c` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00abbe90"></a> `00abbe90` | `0c 00 00 14` | b 0x00abbec0 | `UNCONDITIONAL_JUMP`
<a id="insn-00abbe94"></a> `00abbe94` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00abbe98"></a> `00abbe98` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00abbe9c"></a> `00abbe9c` | `28 01 00 b4` | cbz x8,0x00abbec0 | `CONDITIONAL_JUMP`
<a id="insn-00abbea0"></a> `00abbea0` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00abbea4"></a> `00abbea4` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00abbea8"></a> `00abbea8` | `1f 01 14 6b` | cmp w8,w20 | `FALL_THROUGH`
<a id="insn-00abbeac"></a> `00abbeac` | `4c ff ff 54` | b.gt 0x00abbe94 | `CONDITIONAL_JUMP`
<a id="insn-00abbeb0"></a> `00abbeb0` | `6a 03 00 54` | b.ge 0x00abbf1c | `CONDITIONAL_JUMP`
<a id="insn-00abbeb4"></a> `00abbeb4` | `68 07 40 f9` | ldr x8,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00abbeb8"></a> `00abbeb8` | `48 ff ff b5` | cbnz x8,0x00abbea0 | `CONDITIONAL_JUMP`
<a id="insn-00abbebc"></a> `00abbebc` | `76 23 00 91` | add x22,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00abbec0"></a> `00abbec0` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00abbec4"></a> `00abbec4` | `f8 03 1b aa` | mov x24,x27 | `FALL_THROUGH`
<a id="insn-00abbec8"></a> `00abbec8` | `1a 74 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00abbecc"></a> `00abbecc` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abbed0"></a> `00abbed0` | `14 20 00 b9` | str w20,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abbed4"></a> `00abbed4` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00abbed8"></a> `00abbed8` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00abbedc"></a> `00abbedc` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abbee0"></a> `00abbee0` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00abbee4"></a> `00abbee4` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00abbee8"></a> `00abbee8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abbeec"></a> `00abbeec` | `18 08 00 f9` | str x24,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abbef0"></a> `00abbef0` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00abbef4"></a> `00abbef4` | `e8 6a 40 f9` | ldr x8,[x23, #0xd0] | `FALL_THROUGH`
<a id="insn-00abbef8"></a> `00abbef8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abbefc"></a> `00abbefc` | `68 00 00 b4` | cbz x8,0x00abbf08 | `CONDITIONAL_JUMP`
<a id="insn-00abbf00"></a> `00abbf00` | `e8 6a 00 f9` | str x8,[x23, #0xd0] | `FALL_THROUGH`
<a id="insn-00abbf04"></a> `00abbf04` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00abbf08"></a> `00abbf08` | `e0 6e 40 f9` | ldr x0,[x23, #0xd8] | `FALL_THROUGH`
<a id="insn-00abbf0c"></a> `00abbf0c` | `fe ff e5 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-00abbf10"></a> `00abbf10` | `e8 72 40 f9` | ldr x8,[x23, #0xe0] | `FALL_THROUGH`
<a id="insn-00abbf14"></a> `00abbf14` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00abbf18"></a> `00abbf18` | `e8 72 00 f9` | str x8,[x23, #0xe0] | `FALL_THROUGH`
<a id="insn-00abbf1c"></a> `00abbf1c` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00abbf20"></a> `00abbf20` | `c8 0e 43 f8` | ldr x8,[x22, #0x30]! | `FALL_THROUGH`
<a id="insn-00abbf24"></a> `00abbf24` | `c8 00 00 b5` | cbnz x8,0x00abbf3c | `CONDITIONAL_JUMP`
<a id="insn-00abbf28"></a> `00abbf28` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00abbf2c"></a> `00abbf2c` | `0d 00 00 14` | b 0x00abbf60 | `UNCONDITIONAL_JUMP`
<a id="insn-00abbf30"></a> `00abbf30` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00abbf34"></a> `00abbf34` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00abbf38"></a> `00abbf38` | `48 01 00 b4` | cbz x8,0x00abbf60 | `CONDITIONAL_JUMP`
<a id="insn-00abbf3c"></a> `00abbf3c` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00abbf40"></a> `00abbf40` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00abbf44"></a> `00abbf44` | `9f 03 08 6b` | cmp w28,w8 | `FALL_THROUGH`
<a id="insn-00abbf48"></a> `00abbf48` | `4b ff ff 54` | b.lt 0x00abbf30 | `CONDITIONAL_JUMP`
<a id="insn-00abbf4c"></a> `00abbf4c` | `1f 01 1c 6b` | cmp w8,w28 | `FALL_THROUGH`
<a id="insn-00abbf50"></a> `00abbf50` | `ca f2 ff 54` | b.ge 0x00abbda8 | `CONDITIONAL_JUMP`
<a id="insn-00abbf54"></a> `00abbf54` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00abbf58"></a> `00abbf58` | `28 ff ff b5` | cbnz x8,0x00abbf3c | `CONDITIONAL_JUMP`
<a id="insn-00abbf5c"></a> `00abbf5c` | `f6 22 00 91` | add x22,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00abbf60"></a> `00abbf60` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00abbf64"></a> `00abbf64` | `f8 03 17 aa` | mov x24,x23 | `FALL_THROUGH`
<a id="insn-00abbf68"></a> `00abbf68` | `f2 73 06 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00abbf6c"></a> `00abbf6c` | `1c 1c 00 b9` | str w28,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00abbf70"></a> `00abbf70` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00abbf74"></a> `00abbf74` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00abbf78"></a> `00abbf78` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00abbf7c"></a> `00abbf7c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00abbf80"></a> `00abbf80` | `18 08 00 f9` | str x24,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00abbf84"></a> `00abbf84` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00abbf88"></a> `00abbf88` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00abbf8c"></a> `00abbf8c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00abbf90"></a> `00abbf90` | `28 f0 ff b4` | cbz x8,0x00abbd94 | `CONDITIONAL_JUMP`
<a id="insn-00abbf94"></a> `00abbf94` | `68 17 00 f9` | str x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00abbf98"></a> `00abbf98` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00abbf9c"></a> `00abbf9c` | `7e ff ff 17` | b 0x00abbd94 | `UNCONDITIONAL_JUMP`
<a id="insn-00abbfa0"></a> `00abbfa0` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-00abbfa4"></a> `00abbfa4` | `e9 03 40 f9` | ldr x9,[sp] | `FALL_THROUGH`
<a id="insn-00abbfa8"></a> `00abbfa8` | `28 15 40 f9` | ldr x8,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00abbfac"></a> `00abbfac` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00abbfb0"></a> `00abbfb0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abbfb4"></a> `00abbfb4` | `41 01 00 54` | b.ne 0x00abbfdc | `CONDITIONAL_JUMP`
<a id="insn-00abbfb8"></a> `00abbfb8` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00abbfbc"></a> `00abbfbc` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00abbfc0"></a> `00abbfc0` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00abbfc4"></a> `00abbfc4` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00abbfc8"></a> `00abbfc8` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00abbfcc"></a> `00abbfcc` | `fc 6f 45 a9` | ldp x28,x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00abbfd0"></a> `00abbfd0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abbfd4"></a> `00abbfd4` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00abbfd8"></a> `00abbfd8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00abbfdc"></a> `00abbfdc` | `e9 73 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abbd3c`](#insn-00abbd3c) 範囲 `[['00abbd3c', '00abbd6f']]`
  - `CONDITIONAL_JUMP` [`00abbd6c`](#insn-00abbd6c) → [`00abbd78`](#insn-00abbd78)
  - `FALL_THROUGH` [`00abbd6c`](#insn-00abbd6c) → [`00abbd70`](#insn-00abbd70)
- ブロック [`00abbd70`](#insn-00abbd70) 範囲 `[['00abbd70', '00abbd77']]`
  - `UNCONDITIONAL_JUMP` [`00abbd74`](#insn-00abbd74) → [`00abbfa8`](#insn-00abbfa8)
- ブロック [`00abbd78`](#insn-00abbd78) 範囲 `[['00abbd78', '00abbd93']]`
  - `UNCONDITIONAL_JUMP` [`00abbd90`](#insn-00abbd90) → [`00abbdb4`](#insn-00abbdb4)
- ブロック [`00abbd94`](#insn-00abbd94) 範囲 `[['00abbd94', '00abbd9b']]`
  - `FALL_THROUGH` [`00abbd98`](#insn-00abbd98) → [`00abbd9c`](#insn-00abbd9c)
- ブロック [`00abbd9c`](#insn-00abbd9c) 範囲 `[['00abbd9c', '00abbda7']]`
  - `FALL_THROUGH` [`00abbda4`](#insn-00abbda4) → [`00abbda8`](#insn-00abbda8)
- ブロック [`00abbda8`](#insn-00abbda8) 範囲 `[['00abbda8', '00abbdb3']]`
  - `CONDITIONAL_JUMP` [`00abbdb0`](#insn-00abbdb0) → [`00abbfa4`](#insn-00abbfa4)
  - `FALL_THROUGH` [`00abbdb0`](#insn-00abbdb0) → [`00abbdb4`](#insn-00abbdb4)
- ブロック [`00abbdb4`](#insn-00abbdb4) 範囲 `[['00abbdb4', '00abbdbf']]`
  - `FALL_THROUGH` [`00abbdbc`](#insn-00abbdbc) → [`00abbdc0`](#insn-00abbdc0)
- ブロック [`00abbdc0`](#insn-00abbdc0) 範囲 `[['00abbdc0', '00abbdcb']]`
  - `FALL_THROUGH` [`00abbdc8`](#insn-00abbdc8) → [`00abbdcc`](#insn-00abbdcc)
- ブロック [`00abbdcc`](#insn-00abbdcc) 範囲 `[['00abbdcc', '00abbddf']]`
  - `CONDITIONAL_JUMP` [`00abbddc`](#insn-00abbddc) → [`00abbde8`](#insn-00abbde8)
  - `FALL_THROUGH` [`00abbddc`](#insn-00abbddc) → [`00abbde0`](#insn-00abbde0)
- ブロック [`00abbde0`](#insn-00abbde0) 範囲 `[['00abbde0', '00abbde7']]`
  - `FALL_THROUGH` [`00abbde4`](#insn-00abbde4) → [`00abbde8`](#insn-00abbde8)
- ブロック [`00abbde8`](#insn-00abbde8) 範囲 `[['00abbde8', '00abbdef']]`
  - `CONDITIONAL_JUMP` [`00abbdec`](#insn-00abbdec) → [`00abbfa0`](#insn-00abbfa0)
  - `FALL_THROUGH` [`00abbdec`](#insn-00abbdec) → [`00abbdf0`](#insn-00abbdf0)
- ブロック [`00abbdf0`](#insn-00abbdf0) 範囲 `[['00abbdf0', '00abbe17']]`
  - `FALL_THROUGH` [`00abbe14`](#insn-00abbe14) → [`00abbe18`](#insn-00abbe18)
- ブロック [`00abbe18`](#insn-00abbe18) 範囲 `[['00abbe18', '00abbe1f']]`
  - `CONDITIONAL_JUMP` [`00abbe1c`](#insn-00abbe1c) → [`00abbe50`](#insn-00abbe50)
  - `FALL_THROUGH` [`00abbe1c`](#insn-00abbe1c) → [`00abbe20`](#insn-00abbe20)
- ブロック [`00abbe20`](#insn-00abbe20) 範囲 `[['00abbe20', '00abbe23']]`
  - `FALL_THROUGH` [`00abbe20`](#insn-00abbe20) → [`00abbe24`](#insn-00abbe24)
- ブロック [`00abbe24`](#insn-00abbe24) 範囲 `[['00abbe24', '00abbe33']]`
  - `FALL_THROUGH` [`00abbe30`](#insn-00abbe30) → [`00abbe34`](#insn-00abbe34)
- ブロック [`00abbe34`](#insn-00abbe34) 範囲 `[['00abbe34', '00abbe4f']]`
  - `UNCONDITIONAL_JUMP` [`00abbe4c`](#insn-00abbe4c) → [`00abbe74`](#insn-00abbe74)
- ブロック [`00abbe50`](#insn-00abbe50) 範囲 `[['00abbe50', '00abbe73']]`
  - `FALL_THROUGH` [`00abbe70`](#insn-00abbe70) → [`00abbe74`](#insn-00abbe74)
- ブロック [`00abbe74`](#insn-00abbe74) 範囲 `[['00abbe74', '00abbe8b']]`
  - `CONDITIONAL_JUMP` [`00abbe88`](#insn-00abbe88) → [`00abbea0`](#insn-00abbea0)
  - `FALL_THROUGH` [`00abbe88`](#insn-00abbe88) → [`00abbe8c`](#insn-00abbe8c)
- ブロック [`00abbe8c`](#insn-00abbe8c) 範囲 `[['00abbe8c', '00abbe93']]`
  - `UNCONDITIONAL_JUMP` [`00abbe90`](#insn-00abbe90) → [`00abbec0`](#insn-00abbec0)
- ブロック [`00abbe94`](#insn-00abbe94) 範囲 `[['00abbe94', '00abbe9f']]`
  - `CONDITIONAL_JUMP` [`00abbe9c`](#insn-00abbe9c) → [`00abbec0`](#insn-00abbec0)
  - `FALL_THROUGH` [`00abbe9c`](#insn-00abbe9c) → [`00abbea0`](#insn-00abbea0)
- ブロック [`00abbea0`](#insn-00abbea0) 範囲 `[['00abbea0', '00abbeaf']]`
  - `CONDITIONAL_JUMP` [`00abbeac`](#insn-00abbeac) → [`00abbe94`](#insn-00abbe94)
  - `FALL_THROUGH` [`00abbeac`](#insn-00abbeac) → [`00abbeb0`](#insn-00abbeb0)
- ブロック [`00abbeb0`](#insn-00abbeb0) 範囲 `[['00abbeb0', '00abbeb3']]`
  - `CONDITIONAL_JUMP` [`00abbeb0`](#insn-00abbeb0) → [`00abbf1c`](#insn-00abbf1c)
  - `FALL_THROUGH` [`00abbeb0`](#insn-00abbeb0) → [`00abbeb4`](#insn-00abbeb4)
- ブロック [`00abbeb4`](#insn-00abbeb4) 範囲 `[['00abbeb4', '00abbebb']]`
  - `CONDITIONAL_JUMP` [`00abbeb8`](#insn-00abbeb8) → [`00abbea0`](#insn-00abbea0)
  - `FALL_THROUGH` [`00abbeb8`](#insn-00abbeb8) → [`00abbebc`](#insn-00abbebc)
- ブロック [`00abbebc`](#insn-00abbebc) 範囲 `[['00abbebc', '00abbebf']]`
  - `FALL_THROUGH` [`00abbebc`](#insn-00abbebc) → [`00abbec0`](#insn-00abbec0)
- ブロック [`00abbec0`](#insn-00abbec0) 範囲 `[['00abbec0', '00abbeff']]`
  - `CONDITIONAL_JUMP` [`00abbefc`](#insn-00abbefc) → [`00abbf08`](#insn-00abbf08)
  - `FALL_THROUGH` [`00abbefc`](#insn-00abbefc) → [`00abbf00`](#insn-00abbf00)
- ブロック [`00abbf00`](#insn-00abbf00) 範囲 `[['00abbf00', '00abbf07']]`
  - `FALL_THROUGH` [`00abbf04`](#insn-00abbf04) → [`00abbf08`](#insn-00abbf08)
- ブロック [`00abbf08`](#insn-00abbf08) 範囲 `[['00abbf08', '00abbf1b']]`
  - `FALL_THROUGH` [`00abbf18`](#insn-00abbf18) → [`00abbf1c`](#insn-00abbf1c)
- ブロック [`00abbf1c`](#insn-00abbf1c) 範囲 `[['00abbf1c', '00abbf27']]`
  - `CONDITIONAL_JUMP` [`00abbf24`](#insn-00abbf24) → [`00abbf3c`](#insn-00abbf3c)
  - `FALL_THROUGH` [`00abbf24`](#insn-00abbf24) → [`00abbf28`](#insn-00abbf28)
- ブロック [`00abbf28`](#insn-00abbf28) 範囲 `[['00abbf28', '00abbf2f']]`
  - `UNCONDITIONAL_JUMP` [`00abbf2c`](#insn-00abbf2c) → [`00abbf60`](#insn-00abbf60)
- ブロック [`00abbf30`](#insn-00abbf30) 範囲 `[['00abbf30', '00abbf3b']]`
  - `CONDITIONAL_JUMP` [`00abbf38`](#insn-00abbf38) → [`00abbf60`](#insn-00abbf60)
  - `FALL_THROUGH` [`00abbf38`](#insn-00abbf38) → [`00abbf3c`](#insn-00abbf3c)
- ブロック [`00abbf3c`](#insn-00abbf3c) 範囲 `[['00abbf3c', '00abbf4b']]`
  - `CONDITIONAL_JUMP` [`00abbf48`](#insn-00abbf48) → [`00abbf30`](#insn-00abbf30)
  - `FALL_THROUGH` [`00abbf48`](#insn-00abbf48) → [`00abbf4c`](#insn-00abbf4c)
- ブロック [`00abbf4c`](#insn-00abbf4c) 範囲 `[['00abbf4c', '00abbf53']]`
  - `CONDITIONAL_JUMP` [`00abbf50`](#insn-00abbf50) → [`00abbda8`](#insn-00abbda8)
  - `FALL_THROUGH` [`00abbf50`](#insn-00abbf50) → [`00abbf54`](#insn-00abbf54)
- ブロック [`00abbf54`](#insn-00abbf54) 範囲 `[['00abbf54', '00abbf5b']]`
  - `CONDITIONAL_JUMP` [`00abbf58`](#insn-00abbf58) → [`00abbf3c`](#insn-00abbf3c)
  - `FALL_THROUGH` [`00abbf58`](#insn-00abbf58) → [`00abbf5c`](#insn-00abbf5c)
- ブロック [`00abbf5c`](#insn-00abbf5c) 範囲 `[['00abbf5c', '00abbf5f']]`
  - `FALL_THROUGH` [`00abbf5c`](#insn-00abbf5c) → [`00abbf60`](#insn-00abbf60)
- ブロック [`00abbf60`](#insn-00abbf60) 範囲 `[['00abbf60', '00abbf93']]`
  - `CONDITIONAL_JUMP` [`00abbf90`](#insn-00abbf90) → [`00abbd94`](#insn-00abbd94)
  - `FALL_THROUGH` [`00abbf90`](#insn-00abbf90) → [`00abbf94`](#insn-00abbf94)
- ブロック [`00abbf94`](#insn-00abbf94) 範囲 `[['00abbf94', '00abbf9f']]`
  - `UNCONDITIONAL_JUMP` [`00abbf9c`](#insn-00abbf9c) → [`00abbd94`](#insn-00abbd94)
- ブロック [`00abbfa0`](#insn-00abbfa0) 範囲 `[['00abbfa0', '00abbfa3']]`
  - `FALL_THROUGH` [`00abbfa0`](#insn-00abbfa0) → [`00abbfa4`](#insn-00abbfa4)
- ブロック [`00abbfa4`](#insn-00abbfa4) 範囲 `[['00abbfa4', '00abbfa7']]`
  - `FALL_THROUGH` [`00abbfa4`](#insn-00abbfa4) → [`00abbfa8`](#insn-00abbfa8)
- ブロック [`00abbfa8`](#insn-00abbfa8) 範囲 `[['00abbfa8', '00abbfb3']]`
  - `FALL_THROUGH` [`00abbfb0`](#insn-00abbfb0) → [`00abbfb4`](#insn-00abbfb4)
- ブロック [`00abbfb4`](#insn-00abbfb4) 範囲 `[['00abbfb4', '00abbfb7']]`
  - `CONDITIONAL_JUMP` [`00abbfb4`](#insn-00abbfb4) → [`00abbfdc`](#insn-00abbfdc)
  - `FALL_THROUGH` [`00abbfb4`](#insn-00abbfb4) → [`00abbfb8`](#insn-00abbfb8)
- ブロック [`00abbfb8`](#insn-00abbfb8) 範囲 `[['00abbfb8', '00abbfdb']]`
- ブロック [`00abbfdc`](#insn-00abbfdc) 範囲 `[['00abbfdc', '00abbfdf']]`

## 命令位置別の参照

- [`00abbd40`](#insn-00abbd40) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd44`](#insn-00abbd44) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd48`](#insn-00abbd48) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd4c`](#insn-00abbd4c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd50`](#insn-00abbd50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd54`](#insn-00abbd54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd68`](#insn-00abbd68) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd6c`](#insn-00abbd6c) → [`00abbd78`](#insn-00abbd78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd74`](#insn-00abbd74) → [`00abbfa8`](#insn-00abbfa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd8c`](#insn-00abbd8c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd90`](#insn-00abbd90) → [`00abbdb4`](#insn-00abbdb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbd98`](#insn-00abbd98) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`00abbdb0`](#insn-00abbdb0) → [`00abbfa4`](#insn-00abbfa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbdb4`](#insn-00abbdb4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00abbdc8`](#insn-00abbdc8) → [`00aba21c`](../00aba/00aba21c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aba21c` · 推定シンボル `None` · 推定型 `None`
- [`00abbdcc`](#insn-00abbdcc) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbdd0`](#insn-00abbdd0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbddc`](#insn-00abbddc) → [`00abbde8`](#insn-00abbde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbde0`](#insn-00abbde0) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbde4`](#insn-00abbde4) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abbdec`](#insn-00abbdec) → [`00abbfa0`](#insn-00abbfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbdf0`](#insn-00abbdf0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00abbe04`](#insn-00abbe04) → [`00aba21c`](../00aba/00aba21c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aba21c` · 推定シンボル `None` · 推定型 `None`
- [`00abbe08`](#insn-00abbe08) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbe10`](#insn-00abbe10) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbe14`](#insn-00abbe14) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abbe1c`](#insn-00abbe1c) → [`00abbe50`](#insn-00abbe50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbe20`](#insn-00abbe20) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00abbe34`](#insn-00abbe34) → [`00aba21c`](../00aba/00aba21c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aba21c` · 推定シンボル `None` · 推定型 `None`
- [`00abbe38`](#insn-00abbe38) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbe44`](#insn-00abbe44) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbe4c`](#insn-00abbe4c) → [`00abbe74`](#insn-00abbe74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbe50`](#insn-00abbe50) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00abbe64`](#insn-00abbe64) → [`00aba21c`](../00aba/00aba21c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aba21c` · 推定シンボル `None` · 推定型 `None`
- [`00abbe68`](#insn-00abbe68) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbe70`](#insn-00abbe70) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbe74`](#insn-00abbe74) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00abbe78`](#insn-00abbe78) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00abbe84`](#insn-00abbe84) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abbe88`](#insn-00abbe88) → [`00abbea0`](#insn-00abbea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbe90`](#insn-00abbe90) → [`00abbec0`](#insn-00abbec0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbe9c`](#insn-00abbe9c) → [`00abbec0`](#insn-00abbec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbeac`](#insn-00abbeac) → [`00abbe94`](#insn-00abbe94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbeb0`](#insn-00abbeb0) → [`00abbf1c`](#insn-00abbf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbeb8`](#insn-00abbeb8) → [`00abbea0`](#insn-00abbea0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbec8`](#insn-00abbec8) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00abbef0`](#insn-00abbef0) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abbef4`](#insn-00abbef4) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abbefc`](#insn-00abbefc) → [`00abbf08`](#insn-00abbf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbf00`](#insn-00abbf00) → `003380d0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abbf04`](#insn-00abbf04) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abbf08`](#insn-00abbf08) → `003380d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abbf0c`](#insn-00abbf0c) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`00abbf10`](#insn-00abbf10) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abbf18`](#insn-00abbf18) → `003380e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00abbf24`](#insn-00abbf24) → [`00abbf3c`](#insn-00abbf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbf2c`](#insn-00abbf2c) → [`00abbf60`](#insn-00abbf60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbf38`](#insn-00abbf38) → [`00abbf60`](#insn-00abbf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbf48`](#insn-00abbf48) → [`00abbf30`](#insn-00abbf30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbf50`](#insn-00abbf50) → [`00abbda8`](#insn-00abbda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbf58`](#insn-00abbf58) → [`00abbf3c`](#insn-00abbf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbf68`](#insn-00abbf68) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00abbf90`](#insn-00abbf90) → [`00abbd94`](#insn-00abbd94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbf9c`](#insn-00abbf9c) → [`00abbd94`](#insn-00abbd94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfa4`](#insn-00abbfa4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfac`](#insn-00abbfac) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfb4`](#insn-00abbfb4) → [`00abbfdc`](#insn-00abbfdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfbc`](#insn-00abbfbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfc0`](#insn-00abbfc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfc4`](#insn-00abbfc4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfc8`](#insn-00abbfc8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfcc`](#insn-00abbfcc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfd0`](#insn-00abbfd0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abbfdc`](#insn-00abbfdc) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abbd40`](#insn-00abbd40)

~~~json
{
  "source": "00abbd40",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd44`](#insn-00abbd44)

~~~json
{
  "source": "00abbd44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd48`](#insn-00abbd48)

~~~json
{
  "source": "00abbd48",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd4c`](#insn-00abbd4c)

~~~json
{
  "source": "00abbd4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd50`](#insn-00abbd50)

~~~json
{
  "source": "00abbd50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd54`](#insn-00abbd54)

~~~json
{
  "source": "00abbd54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd68`](#insn-00abbd68)

~~~json
{
  "source": "00abbd68",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd6c`](#insn-00abbd6c)

~~~json
{
  "source": "00abbd6c",
  "target": "00abbd78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd74`](#insn-00abbd74)

~~~json
{
  "source": "00abbd74",
  "target": "00abbfa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd8c`](#insn-00abbd8c)

~~~json
{
  "source": "00abbd8c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd90`](#insn-00abbd90)

~~~json
{
  "source": "00abbd90",
  "target": "00abbdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbd98`](#insn-00abbd98)

~~~json
{
  "source": "00abbd98",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbdb0`](#insn-00abbdb0)

~~~json
{
  "source": "00abbdb0",
  "target": "00abbfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbdb4`](#insn-00abbdb4)

~~~json
{
  "source": "00abbdb4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbdc8`](#insn-00abbdc8)

~~~json
{
  "source": "00abbdc8",
  "target": "00aba21c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbdcc`](#insn-00abbdcc)

~~~json
{
  "source": "00abbdcc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbdd0`](#insn-00abbdd0)

~~~json
{
  "source": "00abbdd0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbddc`](#insn-00abbddc)

~~~json
{
  "source": "00abbddc",
  "target": "00abbde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbde0`](#insn-00abbde0)

~~~json
{
  "source": "00abbde0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbde4`](#insn-00abbde4)

~~~json
{
  "source": "00abbde4",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbdec`](#insn-00abbdec)

~~~json
{
  "source": "00abbdec",
  "target": "00abbfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbdf0`](#insn-00abbdf0)

~~~json
{
  "source": "00abbdf0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbe04`](#insn-00abbe04)

~~~json
{
  "source": "00abbe04",
  "target": "00aba21c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbe08`](#insn-00abbe08)

~~~json
{
  "source": "00abbe08",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbe10`](#insn-00abbe10)

~~~json
{
  "source": "00abbe10",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbe14`](#insn-00abbe14)

~~~json
{
  "source": "00abbe14",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbe1c`](#insn-00abbe1c)

~~~json
{
  "source": "00abbe1c",
  "target": "00abbe50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbe20`](#insn-00abbe20)

~~~json
{
  "source": "00abbe20",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbe34`](#insn-00abbe34)

~~~json
{
  "source": "00abbe34",
  "target": "00aba21c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbe38`](#insn-00abbe38)

~~~json
{
  "source": "00abbe38",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbe44`](#insn-00abbe44)

~~~json
{
  "source": "00abbe44",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbe4c`](#insn-00abbe4c)

~~~json
{
  "source": "00abbe4c",
  "target": "00abbe74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbe50`](#insn-00abbe50)

~~~json
{
  "source": "00abbe50",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbe64`](#insn-00abbe64)

~~~json
{
  "source": "00abbe64",
  "target": "00aba21c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbe68`](#insn-00abbe68)

~~~json
{
  "source": "00abbe68",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbe70`](#insn-00abbe70)

~~~json
{
  "source": "00abbe70",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbe74`](#insn-00abbe74)

~~~json
{
  "source": "00abbe74",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbe78`](#insn-00abbe78)

~~~json
{
  "source": "00abbe78",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbe84`](#insn-00abbe84)

~~~json
{
  "source": "00abbe84",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78c97d00606f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbe88`](#insn-00abbe88)

~~~json
{
  "source": "00abbe88",
  "target": "00abbea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbe90`](#insn-00abbe90)

~~~json
{
  "source": "00abbe90",
  "target": "00abbec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbe9c`](#insn-00abbe9c)

~~~json
{
  "source": "00abbe9c",
  "target": "00abbec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbeac`](#insn-00abbeac)

~~~json
{
  "source": "00abbeac",
  "target": "00abbe94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbeb0`](#insn-00abbeb0)

~~~json
{
  "source": "00abbeb0",
  "target": "00abbf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbeb8`](#insn-00abbeb8)

~~~json
{
  "source": "00abbeb8",
  "target": "00abbea0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbec8`](#insn-00abbec8)

~~~json
{
  "source": "00abbec8",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbef0`](#insn-00abbef0)

~~~json
{
  "source": "00abbef0",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78c97d00606f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbef4`](#insn-00abbef4)

~~~json
{
  "source": "00abbef4",
  "target": "003380d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6cc97d004c6f0a00",
  "capture_start": "003380d0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbefc`](#insn-00abbefc)

~~~json
{
  "source": "00abbefc",
  "target": "00abbf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbf00`](#insn-00abbf00)

~~~json
{
  "source": "00abbf00",
  "target": "003380d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "6cc97d004c6f0a00",
  "capture_start": "003380d0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbf04`](#insn-00abbf04)

~~~json
{
  "source": "00abbf04",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78c97d00606f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbf08`](#insn-00abbf08)

~~~json
{
  "source": "00abbf08",
  "target": "003380d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380d8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "78c97d00606f0a00",
  "capture_start": "003380d8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbf0c`](#insn-00abbf0c)

~~~json
{
  "source": "00abbf0c",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbf10`](#insn-00abbf10)

~~~json
{
  "source": "00abbf10",
  "target": "003380e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cc97d00746f0a00",
  "capture_start": "003380e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbf18`](#insn-00abbf18)

~~~json
{
  "source": "00abbf18",
  "target": "003380e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003380e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "7cc97d00746f0a00",
  "capture_start": "003380e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00abbf24`](#insn-00abbf24)

~~~json
{
  "source": "00abbf24",
  "target": "00abbf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbf2c`](#insn-00abbf2c)

~~~json
{
  "source": "00abbf2c",
  "target": "00abbf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbf38`](#insn-00abbf38)

~~~json
{
  "source": "00abbf38",
  "target": "00abbf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbf48`](#insn-00abbf48)

~~~json
{
  "source": "00abbf48",
  "target": "00abbf30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbf50`](#insn-00abbf50)

~~~json
{
  "source": "00abbf50",
  "target": "00abbda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbf58`](#insn-00abbf58)

~~~json
{
  "source": "00abbf58",
  "target": "00abbf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbf68`](#insn-00abbf68)

~~~json
{
  "source": "00abbf68",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abbf90`](#insn-00abbf90)

~~~json
{
  "source": "00abbf90",
  "target": "00abbd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbf9c`](#insn-00abbf9c)

~~~json
{
  "source": "00abbf9c",
  "target": "00abbd94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfa4`](#insn-00abbfa4)

~~~json
{
  "source": "00abbfa4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfac`](#insn-00abbfac)

~~~json
{
  "source": "00abbfac",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfb4`](#insn-00abbfb4)

~~~json
{
  "source": "00abbfb4",
  "target": "00abbfdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfbc`](#insn-00abbfbc)

~~~json
{
  "source": "00abbfbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfc0`](#insn-00abbfc0)

~~~json
{
  "source": "00abbfc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfc4`](#insn-00abbfc4)

~~~json
{
  "source": "00abbfc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfc8`](#insn-00abbfc8)

~~~json
{
  "source": "00abbfc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfcc`](#insn-00abbfcc)

~~~json
{
  "source": "00abbfcc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfd0`](#insn-00abbfd0)

~~~json
{
  "source": "00abbfd0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abbfdc`](#insn-00abbfdc)

~~~json
{
  "source": "00abbfdc",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
