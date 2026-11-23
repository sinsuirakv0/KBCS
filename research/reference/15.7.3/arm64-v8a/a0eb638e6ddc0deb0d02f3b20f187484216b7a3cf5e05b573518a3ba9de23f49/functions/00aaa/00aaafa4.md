# 00aaafa4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aaaedc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaaedc.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-5f71ef8828c78c35851f11bd38981c2e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aaafe8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaafe8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-fb9a421efdf5205024bc3fd4c377f8a7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaafa4",
  "name": "FUN_00aaafa4",
  "size": 1200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b3d69471e6244fada01c7ef5280e83d6da118fd51d7c10ff6a4b593c04ab45b",
  "source_text_sha256": "7b3d69471e6244fada01c7ef5280e83d6da118fd51d7c10ff6a4b593c04ab45b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaafa4",
        "00aab44f"
      ],
      [
        "00aab484",
        "00aab487"
      ]
    ],
    "bytes_sha256": "52738fe758d414747eb2c83643996aee167b89864e0a0b0b40ea023c9f139d3c",
    "instruction_count": 300,
    "instruction_bytes": 1200,
    "body_bytes": 1200,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005d996c](../005d9/005d996c.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0041e380](../0041e/0041e380.md)
- [007cf950](../007cf/007cf950.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [0081f580](../0081f/0081f580.md)
- [00aacb40](../00aac/00aacb40.md)
- [00aacb54](../00aac/00aacb54.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb160](../00bdb/00bdb160.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7699 bytes

~~~c

void FUN_00aaafa4(long param_1,int param_2,int param_3,int param_4)

{
  ulong uVar1;
  byte *pbVar2;
  undefined4 uVar3;
  byte bVar4;
  byte bVar5;
  byte bVar6;
  byte bVar7;
  byte bVar8;
  byte bVar9;
  byte bVar10;
  byte bVar11;
  int iVar12;
  int iVar13;
  long lVar14;
  undefined8 *puVar15;
  undefined8 uVar16;
  long lVar17;
  undefined8 *puVar18;
  void *__dest;
  undefined8 *puVar19;
  long *plVar20;
  ulong uVar21;
  undefined8 *puVar22;
  ulong uVar23;
  undefined8 *puVar24;
  void *__src;
  long lVar25;
  long lVar26;
  void *local_80;
  void *local_78;
  undefined8 local_70;
  long local_68;
  
  lVar14 = tpidr_el0;
  local_68 = *(long *)(lVar14 + 0x28);
  if (param_2 == -1) {
    param_2 = FUN_007cf950(0);
    param_3 = FUN_007cfaa0();
    param_4 = FUN_007cfcd8();
  }
  iVar12 = param_4 + param_3 * 10 + param_2 * 1000;
  puVar22 = (undefined8 *)(param_1 + 0x20);
  puVar19 = (undefined8 *)*puVar22;
  puVar18 = puVar22;
  puVar24 = puVar22;
  if ((undefined8 *)*puVar22 != (undefined8 *)0x0) {
    do {
      while (puVar15 = puVar19, puVar24 = puVar15, iVar12 < *(int *)(puVar15 + 4)) {
        puVar19 = (undefined8 *)*puVar15;
        puVar18 = puVar15;
        if ((undefined8 *)*puVar15 == (undefined8 *)0x0) goto LAB_00aab060;
      }
      if (iVar12 <= *(int *)(puVar15 + 4)) goto LAB_00aab0b4;
      puVar19 = (undefined8 *)puVar15[1];
    } while ((undefined8 *)puVar15[1] != (undefined8 *)0x0);
    puVar18 = puVar15 + 1;
  }
LAB_00aab060:
  puVar15 = (undefined8 *)_Znwm(0x40);
  puVar15[6] = 0;
  puVar15[7] = 0;
  puVar15[5] = 0;
  *puVar15 = 0;
  puVar15[1] = 0;
  puVar15[2] = puVar24;
  *puVar18 = puVar15;
  plVar20 = *(long **)(param_1 + 0x18);
  *(int *)(puVar15 + 4) = iVar12;
  puVar19 = puVar15;
  if (*plVar20 != 0) {
    *(long *)(param_1 + 0x18) = *plVar20;
    puVar19 = (undefined8 *)*puVar18;
  }
  FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar19);
  *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aab0b4:
  if ((ulong)(((long)(puVar15[6] - puVar15[5]) >> 3) * -0x5555555555555555) < 10) {
    puVar19 = (undefined8 *)*puVar22;
    puVar18 = puVar22;
    puVar24 = puVar22;
    if ((undefined8 *)*puVar22 != (undefined8 *)0x0) {
      do {
        while (puVar15 = puVar19, puVar24 = puVar15, iVar12 < *(int *)(puVar15 + 4)) {
          puVar19 = (undefined8 *)*puVar15;
          puVar18 = puVar15;
          if ((undefined8 *)*puVar15 == (undefined8 *)0x0) goto LAB_00aab14c;
        }
        if (iVar12 <= *(int *)(puVar15 + 4)) goto LAB_00aab1a0;
        puVar19 = (undefined8 *)puVar15[1];
      } while ((undefined8 *)puVar15[1] != (undefined8 *)0x0);
      puVar18 = puVar15 + 1;
    }
LAB_00aab14c:
    puVar15 = (undefined8 *)_Znwm(0x40);
    puVar15[6] = 0;
    puVar15[7] = 0;
    puVar15[5] = 0;
    *puVar15 = 0;
    puVar15[1] = 0;
    puVar15[2] = puVar24;
    *puVar18 = puVar15;
    plVar20 = *(long **)(param_1 + 0x18);
    *(int *)(puVar15 + 4) = iVar12;
    puVar19 = puVar15;
    if (*plVar20 != 0) {
      *(long *)(param_1 + 0x18) = *plVar20;
      puVar19 = (undefined8 *)*puVar18;
    }
    FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar19);
    *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aab1a0:
    puVar19 = (undefined8 *)puVar15[6];
    local_80 = (void *)0x0;
    local_78 = (void *)0x0;
    local_70 = 0;
    if (puVar19 < (undefined8 *)puVar15[7]) {
      *puVar19 = 0;
      puVar19[1] = 0;
      puVar19[2] = 0;
      puVar15[6] = puVar19 + 3;
    }
    else {
      uVar16 = FUN_00aacb54(puVar15 + 5,&local_80);
      puVar15[6] = uVar16;
      if (local_80 != (void *)0x0) {
        local_78 = local_80;
        _ZdlPv(local_80);
      }
    }
    lVar26 = 0;
    while( true ) {
      lVar17 = FUN_0081f580();
      pbVar2 = (byte *)(lVar17 + 0xc744 + lVar26 * 4);
      if (((uint)(*(byte *)(lVar17 + 0xc76e) ^ pbVar2[2]) << 0x10 |
           (uint)(*(byte *)(lVar17 + 0xc76f) ^ pbVar2[3]) << 0x18 |
           (uint)(*(byte *)(lVar17 + 0xc76d) ^ pbVar2[1]) << 8 |
          (uint)(*(byte *)(lVar17 + 0xc76c) ^ *pbVar2)) == 0xffffffff) break;
      lVar17 = FUN_0081f580();
      pbVar2 = (byte *)(lVar17 + 0xc744 + lVar26 * 4);
      bVar4 = *(byte *)(lVar17 + 0xc76c);
      bVar5 = *(byte *)(lVar17 + 0xc76d);
      bVar6 = *pbVar2;
      bVar7 = pbVar2[1];
      bVar8 = pbVar2[2];
      bVar9 = *(byte *)(lVar17 + 0xc76e);
      bVar10 = pbVar2[3];
      bVar11 = *(byte *)(lVar17 + 0xc76f);
      puVar19 = (undefined8 *)*puVar22;
      puVar18 = puVar22;
      while (puVar15 = puVar18, puVar24 = puVar18, puVar19 != (undefined8 *)0x0) {
        while (puVar18 = puVar19, *(int *)(puVar18 + 4) <= iVar12) {
          if (iVar12 <= *(int *)(puVar18 + 4)) goto LAB_00aab348;
          puVar19 = (undefined8 *)puVar18[1];
          if ((undefined8 *)puVar18[1] == (undefined8 *)0x0) {
            puVar24 = puVar18 + 1;
            puVar15 = puVar18;
            goto LAB_00aab2e0;
          }
        }
        puVar19 = (undefined8 *)*puVar18;
      }
LAB_00aab2e0:
      puVar18 = (undefined8 *)_Znwm(0x40);
      puVar18[2] = puVar15;
      puVar18[6] = 0;
      puVar18[7] = 0;
      puVar18[5] = 0;
      *puVar18 = 0;
      puVar18[1] = 0;
      *puVar24 = puVar18;
      plVar20 = *(long **)(param_1 + 0x18);
      *(int *)(puVar18 + 4) = iVar12;
      puVar19 = puVar18;
      if (*plVar20 != 0) {
        *(long *)(param_1 + 0x18) = *plVar20;
        puVar19 = (undefined8 *)*puVar24;
      }
      FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar19);
      *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aab348:
      lVar25 = puVar18[6];
      iVar13 = CONCAT13(bVar11 ^ bVar10,
                        CONCAT12(bVar9 ^ bVar8,CONCAT11(bVar5 ^ bVar7,bVar4 ^ bVar6))) + -2;
      lVar17 = FUN_0081f580();
      puVar19 = *(undefined8 **)(lVar25 + -0x10);
      uVar3 = *(undefined4 *)(lVar17 + (long)iVar13 * 4 + 0x49734);
      if (puVar19 < *(undefined8 **)(lVar25 + -8)) {
        puVar18 = puVar19 + 1;
        *puVar19 = CONCAT44(uVar3,iVar13);
      }
      else {
        __src = *(void **)(lVar25 + -0x18);
        lVar17 = (long)puVar19 - (long)__src >> 3;
        uVar1 = lVar17 + 1;
        if (uVar1 >> 0x3d != 0) {
          if (*(long *)(lVar14 + 0x28) == local_68) {
            FUN_00aacb40();
LAB_00aab438:
            if (*(long *)(lVar14 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_0041e380();
            }
          }
          goto LAB_00aab484;
        }
        uVar21 = (long)*(undefined8 **)(lVar25 + -8) - (long)__src;
        uVar23 = (long)uVar21 >> 2;
        if (uVar23 <= uVar1) {
          uVar23 = uVar1;
        }
        if (0x7ffffffffffffff7 < uVar21) {
          uVar23 = 0x1fffffffffffffff;
        }
        if (uVar23 == 0) {
          __dest = (void *)0x0;
        }
        else {
          if (uVar23 >> 0x3d != 0) goto LAB_00aab438;
          __dest = (void *)_Znwm(uVar23 << 3);
        }
        puVar24 = (undefined8 *)((long)__dest + lVar17 * 8);
        puVar18 = puVar24 + 1;
        *puVar24 = CONCAT44(uVar3,iVar13);
        memcpy(__dest,__src,(long)puVar19 - (long)__src);
        *(void **)(lVar25 + -0x18) = __dest;
        *(undefined8 **)(lVar25 + -0x10) = puVar18;
        *(void **)(lVar25 + -8) = (void *)((long)__dest + uVar23 * 8);
        if (__src != (void *)0x0) {
          _ZdlPv(__src);
        }
      }
      lVar26 = lVar26 + 1;
      *(undefined8 **)(lVar25 + -0x10) = puVar18;
      if (lVar26 == 10) break;
    }
  }
  if (*(long *)(lVar14 + 0x28) == local_68) {
    return;
  }
LAB_00aab484:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaafa4"></a> `00aaafa4` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00aaafa8"></a> `00aaafa8` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aaafac"></a> `00aaafac` | `fc 6f 06 a9` | stp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aaafb0"></a> `00aaafb0` | `fa 67 07 a9` | stp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aaafb4"></a> `00aaafb4` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aaafb8"></a> `00aaafb8` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aaafbc"></a> `00aaafbc` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aaafc0"></a> `00aaafc0` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aaafc4"></a> `00aaafc4` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aaafc8"></a> `00aaafc8` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00aaafcc"></a> `00aaafcc` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aaafd0"></a> `00aaafd0` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aaafd4"></a> `00aaafd4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aaafd8"></a> `00aaafd8` | `3f 04 00 31` | cmn w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aaafdc"></a> `00aaafdc` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aaafe0"></a> `00aaafe0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaafe4"></a> `00aaafe4` | `01 01 00 54` | b.ne 0x00aab004 | `CONDITIONAL_JUMP`
<a id="insn-00aaafe8"></a> `00aaafe8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aaafec"></a> `00aaafec` | `59 92 f4 97` | bl 0x007cf950 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaff0"></a> `00aaaff0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aaaff4"></a> `00aaaff4` | `ab 92 f4 97` | bl 0x007cfaa0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaff8"></a> `00aaaff8` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aaaffc"></a> `00aaaffc` | `37 93 f4 97` | bl 0x007cfcd8 | `UNCONDITIONAL_CALL`
<a id="insn-00aab000"></a> `00aab000` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-00aab004"></a> `00aab004` | `48 01 80 52` | mov w8,#0xa | `FALL_THROUGH`
<a id="insn-00aab008"></a> `00aab008` | `09 7d 80 52` | mov w9,#0x3e8 | `FALL_THROUGH`
<a id="insn-00aab00c"></a> `00aab00c` | `ea 03 16 aa` | mov x10,x22 | `FALL_THROUGH`
<a id="insn-00aab010"></a> `00aab010` | `a8 0e 08 1b` | madd w8,w21,w8,w3 | `FALL_THROUGH`
<a id="insn-00aab014"></a> `00aab014` | `99 22 09 1b` | madd w25,w20,w9,w8 | `FALL_THROUGH`
<a id="insn-00aab018"></a> `00aab018` | `48 0d 42 f8` | ldr x8,[x10, #0x20]! | `FALL_THROUGH`
<a id="insn-00aab01c"></a> `00aab01c` | `f3 03 0a aa` | mov x19,x10 | `FALL_THROUGH`
<a id="insn-00aab020"></a> `00aab020` | `f4 03 0a aa` | mov x20,x10 | `FALL_THROUGH`
<a id="insn-00aab024"></a> `00aab024` | `f6 2b 01 a9` | stp x22,x10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aab028"></a> `00aab028` | `a8 00 00 b5` | cbnz x8,0x00aab03c | `CONDITIONAL_JUMP`
<a id="insn-00aab02c"></a> `00aab02c` | `0d 00 00 14` | b 0x00aab060 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab030"></a> `00aab030` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab034"></a> `00aab034` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00aab038"></a> `00aab038` | `48 01 00 b4` | cbz x8,0x00aab060 | `CONDITIONAL_JUMP`
<a id="insn-00aab03c"></a> `00aab03c` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aab040"></a> `00aab040` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aab044"></a> `00aab044` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00aab048"></a> `00aab048` | `4b ff ff 54` | b.lt 0x00aab030 | `CONDITIONAL_JUMP`
<a id="insn-00aab04c"></a> `00aab04c` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00aab050"></a> `00aab050` | `2a 03 00 54` | b.ge 0x00aab0b4 | `CONDITIONAL_JUMP`
<a id="insn-00aab054"></a> `00aab054` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aab058"></a> `00aab058` | `28 ff ff b5` | cbnz x8,0x00aab03c | `CONDITIONAL_JUMP`
<a id="insn-00aab05c"></a> `00aab05c` | `93 22 00 91` | add x19,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aab060"></a> `00aab060` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aab064"></a> `00aab064` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-00aab068"></a> `00aab068` | `e2 bf 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aab06c"></a> `00aab06c` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aab070"></a> `00aab070` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aab074"></a> `00aab074` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aab078"></a> `00aab078` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aab07c"></a> `00aab07c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aab080"></a> `00aab080` | `15 08 00 f9` | str x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aab084"></a> `00aab084` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00aab088"></a> `00aab088` | `c8 0e 40 f9` | ldr x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aab08c"></a> `00aab08c` | `19 20 00 b9` | str w25,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aab090"></a> `00aab090` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aab094"></a> `00aab094` | `68 00 00 b4` | cbz x8,0x00aab0a0 | `CONDITIONAL_JUMP`
<a id="insn-00aab098"></a> `00aab098` | `c8 0e 00 f9` | str x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aab09c"></a> `00aab09c` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00aab0a0"></a> `00aab0a0` | `c0 12 40 f9` | ldr x0,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00aab0a4"></a> `00aab0a4` | `f0 b7 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aab0a8"></a> `00aab0a8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aab0ac"></a> `00aab0ac` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab0b0"></a> `00aab0b0` | `c8 16 00 f9` | str x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aab0b4"></a> `00aab0b4` | `89 a2 42 a9` | ldp x9,x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aab0b8"></a> `00aab0b8` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aab0bc"></a> `00aab0bc` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00aab0c0"></a> `00aab0c0` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00aab0c4"></a> `00aab0c4` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00aab0c8"></a> `00aab0c8` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aab0cc"></a> `00aab0cc` | `1f 25 00 f1` | cmp x8,#0x9 | `FALL_THROUGH`
<a id="insn-00aab0d0"></a> `00aab0d0` | `c9 01 00 54` | b.ls 0x00aab108 | `CONDITIONAL_JUMP`
<a id="insn-00aab0d4"></a> `00aab0d4` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aab0d8"></a> `00aab0d8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aab0dc"></a> `00aab0dc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab0e0"></a> `00aab0e0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab0e4"></a> `00aab0e4` | `01 1d 00 54` | b.ne 0x00aab484 | `CONDITIONAL_JUMP`
<a id="insn-00aab0e8"></a> `00aab0e8` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aab0ec"></a> `00aab0ec` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aab0f0"></a> `00aab0f0` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aab0f4"></a> `00aab0f4` | `fa 67 47 a9` | ldp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aab0f8"></a> `00aab0f8` | `fc 6f 46 a9` | ldp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aab0fc"></a> `00aab0fc` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aab100"></a> `00aab100` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00aab104"></a> `00aab104` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aab108"></a> `00aab108` | `f6 53 41 a9` | ldp x22,x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aab10c"></a> `00aab10c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab110"></a> `00aab110` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00aab114"></a> `00aab114` | `a8 00 00 b5` | cbnz x8,0x00aab128 | `CONDITIONAL_JUMP`
<a id="insn-00aab118"></a> `00aab118` | `0d 00 00 14` | b 0x00aab14c | `UNCONDITIONAL_JUMP`
<a id="insn-00aab11c"></a> `00aab11c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab120"></a> `00aab120` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00aab124"></a> `00aab124` | `48 01 00 b4` | cbz x8,0x00aab14c | `CONDITIONAL_JUMP`
<a id="insn-00aab128"></a> `00aab128` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aab12c"></a> `00aab12c` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aab130"></a> `00aab130` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00aab134"></a> `00aab134` | `4b ff ff 54` | b.lt 0x00aab11c | `CONDITIONAL_JUMP`
<a id="insn-00aab138"></a> `00aab138` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00aab13c"></a> `00aab13c` | `2a 03 00 54` | b.ge 0x00aab1a0 | `CONDITIONAL_JUMP`
<a id="insn-00aab140"></a> `00aab140` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aab144"></a> `00aab144` | `28 ff ff b5` | cbnz x8,0x00aab128 | `CONDITIONAL_JUMP`
<a id="insn-00aab148"></a> `00aab148` | `93 22 00 91` | add x19,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aab14c"></a> `00aab14c` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aab150"></a> `00aab150` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-00aab154"></a> `00aab154` | `a7 bf 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aab158"></a> `00aab158` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aab15c"></a> `00aab15c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aab160"></a> `00aab160` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aab164"></a> `00aab164` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aab168"></a> `00aab168` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aab16c"></a> `00aab16c` | `15 08 00 f9` | str x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aab170"></a> `00aab170` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00aab174"></a> `00aab174` | `c8 0e 40 f9` | ldr x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aab178"></a> `00aab178` | `19 20 00 b9` | str w25,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aab17c"></a> `00aab17c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aab180"></a> `00aab180` | `68 00 00 b4` | cbz x8,0x00aab18c | `CONDITIONAL_JUMP`
<a id="insn-00aab184"></a> `00aab184` | `c8 0e 00 f9` | str x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aab188"></a> `00aab188` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00aab18c"></a> `00aab18c` | `c0 12 40 f9` | ldr x0,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00aab190"></a> `00aab190` | `b5 b7 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aab194"></a> `00aab194` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aab198"></a> `00aab198` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab19c"></a> `00aab19c` | `c8 16 00 f9` | str x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aab1a0"></a> `00aab1a0` | `88 26 43 a9` | ldp x8,x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab1a4"></a> `00aab1a4` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aab1a8"></a> `00aab1a8` | `bf 03 1f f8` | stur xzr,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab1ac"></a> `00aab1ac` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab1b0"></a> `00aab1b0` | `e2 00 00 54` | b.cs 0x00aab1cc | `CONDITIONAL_JUMP`
<a id="insn-00aab1b4"></a> `00aab1b4` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00aab1b8"></a> `00aab1b8` | `0a 61 00 91` | add x10,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00aab1bc"></a> `00aab1bc` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab1c0"></a> `00aab1c0` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aab1c4"></a> `00aab1c4` | `8a 1a 00 f9` | str x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab1c8"></a> `00aab1c8` | `0a 00 00 14` | b 0x00aab1f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab1cc"></a> `00aab1cc` | `80 a2 00 91` | add x0,x20,#0x28 | `FALL_THROUGH`
<a id="insn-00aab1d0"></a> `00aab1d0` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00aab1d4"></a> `00aab1d4` | `60 06 00 94` | bl 0x00aacb54 | `UNCONDITIONAL_CALL`
<a id="insn-00aab1d8"></a> `00aab1d8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aab1dc"></a> `00aab1dc` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aab1e0"></a> `00aab1e0` | `88 1a 00 f9` | str x8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab1e4"></a> `00aab1e4` | `60 00 00 b4` | cbz x0,0x00aab1f0 | `CONDITIONAL_JUMP`
<a id="insn-00aab1e8"></a> `00aab1e8` | `a0 83 1e f8` | stur x0,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aab1ec"></a> `00aab1ec` | `89 bf 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00aab1f0"></a> `00aab1f0` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00aab1f4"></a> `00aab1f4` | `95 e8 98 52` | mov w21,#0xc744 | `FALL_THROUGH`
<a id="insn-00aab1f8"></a> `00aab1f8` | `08 00 00 14` | b 0x00aab218 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab1fc"></a> `00aab1fc` | `68 82 1b aa` | orr x8,x19,x27, LSL #0x20 | `FALL_THROUGH`
<a id="insn-00aab200"></a> `00aab200` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00aab204"></a> `00aab204` | `5a 07 00 91` | add x26,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00aab208"></a> `00aab208` | `95 e8 98 52` | mov w21,#0xc744 | `FALL_THROUGH`
<a id="insn-00aab20c"></a> `00aab20c` | `f8 02 1f f8` | stur x24,[x23, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab210"></a> `00aab210` | `5f 2b 00 f1` | cmp x26,#0xa | `FALL_THROUGH`
<a id="insn-00aab214"></a> `00aab214` | `00 f6 ff 54` | b.eq 0x00aab0d4 | `CONDITIONAL_JUMP`
<a id="insn-00aab218"></a> `00aab218` | `da d0 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aab21c"></a> `00aab21c` | `53 f7 7e d3` | lsl x19,x26,#0x2 | `FALL_THROUGH`
<a id="insn-00aab220"></a> `00aab220` | `08 00 15 8b` | add x8,x0,x21 | `FALL_THROUGH`
<a id="insn-00aab224"></a> `00aab224` | `09 30 40 91` | add x9,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aab228"></a> `00aab228` | `2b b9 5d 39` | ldrb w11,[x9, #0x76e] | `FALL_THROUGH`
<a id="insn-00aab22c"></a> `00aab22c` | `2c bd 5d 39` | ldrb w12,[x9, #0x76f] | `FALL_THROUGH`
<a id="insn-00aab230"></a> `00aab230` | `08 01 13 8b` | add x8,x8,x19 | `FALL_THROUGH`
<a id="insn-00aab234"></a> `00aab234` | `0a 09 40 39` | ldrb w10,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aab238"></a> `00aab238` | `0d 05 40 39` | ldrb w13,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aab23c"></a> `00aab23c` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aab240"></a> `00aab240` | `0b 0d 40 39` | ldrb w11,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00aab244"></a> `00aab244` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00aab248"></a> `00aab248` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00aab24c"></a> `00aab24c` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00aab250"></a> `00aab250` | `2c b5 5d 39` | ldrb w12,[x9, #0x76d] | `FALL_THROUGH`
<a id="insn-00aab254"></a> `00aab254` | `29 b1 5d 39` | ldrb w9,[x9, #0x76c] | `FALL_THROUGH`
<a id="insn-00aab258"></a> `00aab258` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aab25c"></a> `00aab25c` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aab260"></a> `00aab260` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aab264"></a> `00aab264` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aab268"></a> `00aab268` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00aab26c"></a> `00aab26c` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab270"></a> `00aab270` | `20 f3 ff 54` | b.eq 0x00aab0d4 | `CONDITIONAL_JUMP`
<a id="insn-00aab274"></a> `00aab274` | `c3 d0 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aab278"></a> `00aab278` | `f4 0f 40 f9` | ldr x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aab27c"></a> `00aab27c` | `0a 00 15 8b` | add x10,x0,x21 | `FALL_THROUGH`
<a id="insn-00aab280"></a> `00aab280` | `09 30 40 91` | add x9,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aab284"></a> `00aab284` | `4a 01 13 8b` | add x10,x10,x19 | `FALL_THROUGH`
<a id="insn-00aab288"></a> `00aab288` | `38 b1 5d 39` | ldrb w24,[x9, #0x76c] | `FALL_THROUGH`
<a id="insn-00aab28c"></a> `00aab28c` | `33 b5 5d 39` | ldrb w19,[x9, #0x76d] | `FALL_THROUGH`
<a id="insn-00aab290"></a> `00aab290` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab294"></a> `00aab294` | `50 01 40 39` | ldrb w16,[x10] | `FALL_THROUGH`
<a id="insn-00aab298"></a> `00aab298` | `51 05 40 39` | ldrb w17,[x10, #0x1] | `FALL_THROUGH`
<a id="insn-00aab29c"></a> `00aab29c` | `5b 09 40 39` | ldrb w27,[x10, #0x2] | `FALL_THROUGH`
<a id="insn-00aab2a0"></a> `00aab2a0` | `35 b9 5d 39` | ldrb w21,[x9, #0x76e] | `FALL_THROUGH`
<a id="insn-00aab2a4"></a> `00aab2a4` | `5c 0d 40 39` | ldrb w28,[x10, #0x3] | `FALL_THROUGH`
<a id="insn-00aab2a8"></a> `00aab2a8` | `2f bd 5d 39` | ldrb w15,[x9, #0x76f] | `FALL_THROUGH`
<a id="insn-00aab2ac"></a> `00aab2ac` | `02 00 00 14` | b 0x00aab2b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab2b0"></a> `00aab2b0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab2b4"></a> `00aab2b4` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00aab2b8"></a> `00aab2b8` | `48 01 00 b4` | cbz x8,0x00aab2e0 | `CONDITIONAL_JUMP`
<a id="insn-00aab2bc"></a> `00aab2bc` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aab2c0"></a> `00aab2c0` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aab2c4"></a> `00aab2c4` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00aab2c8"></a> `00aab2c8` | `4b ff ff 54` | b.lt 0x00aab2b0 | `CONDITIONAL_JUMP`
<a id="insn-00aab2cc"></a> `00aab2cc` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00aab2d0"></a> `00aab2d0` | `ca 03 00 54` | b.ge 0x00aab348 | `CONDITIONAL_JUMP`
<a id="insn-00aab2d4"></a> `00aab2d4` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aab2d8"></a> `00aab2d8` | `28 ff ff b5` | cbnz x8,0x00aab2bc | `CONDITIONAL_JUMP`
<a id="insn-00aab2dc"></a> `00aab2dc` | `96 22 00 91` | add x22,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aab2e0"></a> `00aab2e0` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aab2e4"></a> `00aab2e4` | `f1 c3 04 29` | stp w17,w16,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aab2e8"></a> `00aab2e8` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-00aab2ec"></a> `00aab2ec` | `af c3 1d b8` | stur w15,[x29, #-0x24] | `FALL_THROUGH`
<a id="insn-00aab2f0"></a> `00aab2f0` | `40 bf 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aab2f4"></a> `00aab2f4` | `17 08 00 f9` | str x23,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aab2f8"></a> `00aab2f8` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aab2fc"></a> `00aab2fc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aab300"></a> `00aab300` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aab304"></a> `00aab304` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aab308"></a> `00aab308` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aab30c"></a> `00aab30c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aab310"></a> `00aab310` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00aab314"></a> `00aab314` | `e8 0e 40 f9` | ldr x8,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00aab318"></a> `00aab318` | `19 20 00 b9` | str w25,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aab31c"></a> `00aab31c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aab320"></a> `00aab320` | `68 00 00 b4` | cbz x8,0x00aab32c | `CONDITIONAL_JUMP`
<a id="insn-00aab324"></a> `00aab324` | `e8 0e 00 f9` | str x8,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00aab328"></a> `00aab328` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00aab32c"></a> `00aab32c` | `e0 12 40 f9` | ldr x0,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00aab330"></a> `00aab330` | `4d b7 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aab334"></a> `00aab334` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aab338"></a> `00aab338` | `af c3 5d b8` | ldur w15,[x29, #-0x24] | `FALL_THROUGH`
<a id="insn-00aab33c"></a> `00aab33c` | `f1 c3 44 29` | ldp w17,w16,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aab340"></a> `00aab340` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab344"></a> `00aab344` | `e8 16 00 f9` | str x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aab348"></a> `00aab348` | `08 03 10 4a` | eor w8,w24,w16 | `FALL_THROUGH`
<a id="insn-00aab34c"></a> `00aab34c` | `69 02 11 4a` | eor w9,w19,w17 | `FALL_THROUGH`
<a id="insn-00aab350"></a> `00aab350` | `97 1a 40 f9` | ldr x23,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab354"></a> `00aab354` | `08 21 09 2a` | orr w8,w8,w9, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aab358"></a> `00aab358` | `a9 02 1b 4a` | eor w9,w21,w27 | `FALL_THROUGH`
<a id="insn-00aab35c"></a> `00aab35c` | `08 41 09 2a` | orr w8,w8,w9, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00aab360"></a> `00aab360` | `e9 01 1c 4a` | eor w9,w15,w28 | `FALL_THROUGH`
<a id="insn-00aab364"></a> `00aab364` | `08 61 09 2a` | orr w8,w8,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aab368"></a> `00aab368` | `13 09 00 51` | sub w19,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aab36c"></a> `00aab36c` | `85 d0 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aab370"></a> `00aab370` | `f8 22 7f a9` | ldp x24,x8,[x23, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab374"></a> `00aab374` | `09 c8 33 8b` | add x9,x0,w19, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00aab378"></a> `00aab378` | `8a e6 92 52` | mov w10,#0x9734 | `FALL_THROUGH`
<a id="insn-00aab37c"></a> `00aab37c` | `8a 00 a0 72` | movk w10,#0x4, LSL #16 | `FALL_THROUGH`
<a id="insn-00aab380"></a> `00aab380` | `3b 69 6a b8` | ldr w27,[x9, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aab384"></a> `00aab384` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00aab388"></a> `00aab388` | `a3 f3 ff 54` | b.cc 0x00aab1fc | `CONDITIONAL_JUMP`
<a id="insn-00aab38c"></a> `00aab38c` | `e0 62 00 d1` | sub x0,x23,#0x18 | `FALL_THROUGH`
<a id="insn-00aab390"></a> `00aab390` | `14 00 40 f9` | ldr x20,[x0] | `FALL_THROUGH`
<a id="insn-00aab394"></a> `00aab394` | `15 03 14 cb` | sub x21,x24,x20 | `FALL_THROUGH`
<a id="insn-00aab398"></a> `00aab398` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00aab39c"></a> `00aab39c` | `09 07 00 91` | add x9,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00aab3a0"></a> `00aab3a0` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-00aab3a4"></a> `00aab3a4` | `ea 03 00 b5` | cbnz x10,0x00aab420 | `CONDITIONAL_JUMP`
<a id="insn-00aab3a8"></a> `00aab3a8` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00aab3ac"></a> `00aab3ac` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aab3b0"></a> `00aab3b0` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00aab3b4"></a> `00aab3b4` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00aab3b8"></a> `00aab3b8` | `ea ef 7d b2` | orr x10,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00aab3bc"></a> `00aab3bc` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00aab3c0"></a> `00aab3c0` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00aab3c4"></a> `00aab3c4` | `3c 31 88 9a` | csel x28,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00aab3c8"></a> `00aab3c8` | `fc 00 00 b4` | cbz x28,0x00aab3e4 | `CONDITIONAL_JUMP`
<a id="insn-00aab3cc"></a> `00aab3cc` | `88 ff 7d d3` | lsr x8,x28,#0x3d | `FALL_THROUGH`
<a id="insn-00aab3d0"></a> `00aab3d0` | `48 03 00 b5` | cbnz x8,0x00aab438 | `CONDITIONAL_JUMP`
<a id="insn-00aab3d4"></a> `00aab3d4` | `80 f3 7d d3` | lsl x0,x28,#0x3 | `FALL_THROUGH`
<a id="insn-00aab3d8"></a> `00aab3d8` | `06 bf 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aab3dc"></a> `00aab3dc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aab3e0"></a> `00aab3e0` | `02 00 00 14` | b 0x00aab3e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab3e4"></a> `00aab3e4` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00aab3e8"></a> `00aab3e8` | `d8 0e 18 8b` | add x24,x22,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aab3ec"></a> `00aab3ec` | `68 82 1b aa` | orr x8,x19,x27, LSL #0x20 | `FALL_THROUGH`
<a id="insn-00aab3f0"></a> `00aab3f0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aab3f4"></a> `00aab3f4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00aab3f8"></a> `00aab3f8` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00aab3fc"></a> `00aab3fc` | `d3 0e 1c 8b` | add x19,x22,x28, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aab400"></a> `00aab400` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00aab404"></a> `00aab404` | `57 bf 04 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00aab408"></a> `00aab408` | `f6 e2 3e a9` | stp x22,x24,[x23, #-0x18] | `FALL_THROUGH`
<a id="insn-00aab40c"></a> `00aab40c` | `f3 82 1f f8` | stur x19,[x23, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab410"></a> `00aab410` | `b4 ef ff b4` | cbz x20,0x00aab204 | `CONDITIONAL_JUMP`
<a id="insn-00aab414"></a> `00aab414` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aab418"></a> `00aab418` | `fe be 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00aab41c"></a> `00aab41c` | `7a ff ff 17` | b 0x00aab204 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab420"></a> `00aab420` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aab424"></a> `00aab424` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aab428"></a> `00aab428` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab42c"></a> `00aab42c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab430"></a> `00aab430` | `a1 02 00 54` | b.ne 0x00aab484 | `CONDITIONAL_JUMP`
<a id="insn-00aab434"></a> `00aab434` | `c3 05 00 94` | bl 0x00aacb40 | `UNCONDITIONAL_CALL`
<a id="insn-00aab438"></a> `00aab438` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aab43c"></a> `00aab43c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aab440"></a> `00aab440` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab444"></a> `00aab444` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab448"></a> `00aab448` | `e1 01 00 54` | b.ne 0x00aab484 | `CONDITIONAL_JUMP`
<a id="insn-00aab44c"></a> `00aab44c` | `cd cb e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-00aab484"></a> `00aab484` | `ef be 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaafa4`](#insn-00aaafa4) 範囲 `[['00aaafa4', '00aaafe7']]`
  - `CONDITIONAL_JUMP` [`00aaafe4`](#insn-00aaafe4) → [`00aab004`](#insn-00aab004)
  - `FALL_THROUGH` [`00aaafe4`](#insn-00aaafe4) → [`00aaafe8`](#insn-00aaafe8)
- ブロック [`00aaafe8`](#insn-00aaafe8) 範囲 `[['00aaafe8', '00aab003']]`
  - `FALL_THROUGH` [`00aab000`](#insn-00aab000) → [`00aab004`](#insn-00aab004)
- ブロック [`00aab004`](#insn-00aab004) 範囲 `[['00aab004', '00aab02b']]`
  - `CONDITIONAL_JUMP` [`00aab028`](#insn-00aab028) → [`00aab03c`](#insn-00aab03c)
  - `FALL_THROUGH` [`00aab028`](#insn-00aab028) → [`00aab02c`](#insn-00aab02c)
- ブロック [`00aab02c`](#insn-00aab02c) 範囲 `[['00aab02c', '00aab02f']]`
  - `UNCONDITIONAL_JUMP` [`00aab02c`](#insn-00aab02c) → [`00aab060`](#insn-00aab060)
- ブロック [`00aab030`](#insn-00aab030) 範囲 `[['00aab030', '00aab03b']]`
  - `CONDITIONAL_JUMP` [`00aab038`](#insn-00aab038) → [`00aab060`](#insn-00aab060)
  - `FALL_THROUGH` [`00aab038`](#insn-00aab038) → [`00aab03c`](#insn-00aab03c)
- ブロック [`00aab03c`](#insn-00aab03c) 範囲 `[['00aab03c', '00aab04b']]`
  - `CONDITIONAL_JUMP` [`00aab048`](#insn-00aab048) → [`00aab030`](#insn-00aab030)
  - `FALL_THROUGH` [`00aab048`](#insn-00aab048) → [`00aab04c`](#insn-00aab04c)
- ブロック [`00aab04c`](#insn-00aab04c) 範囲 `[['00aab04c', '00aab053']]`
  - `CONDITIONAL_JUMP` [`00aab050`](#insn-00aab050) → [`00aab0b4`](#insn-00aab0b4)
  - `FALL_THROUGH` [`00aab050`](#insn-00aab050) → [`00aab054`](#insn-00aab054)
- ブロック [`00aab054`](#insn-00aab054) 範囲 `[['00aab054', '00aab05b']]`
  - `CONDITIONAL_JUMP` [`00aab058`](#insn-00aab058) → [`00aab03c`](#insn-00aab03c)
  - `FALL_THROUGH` [`00aab058`](#insn-00aab058) → [`00aab05c`](#insn-00aab05c)
- ブロック [`00aab05c`](#insn-00aab05c) 範囲 `[['00aab05c', '00aab05f']]`
  - `FALL_THROUGH` [`00aab05c`](#insn-00aab05c) → [`00aab060`](#insn-00aab060)
- ブロック [`00aab060`](#insn-00aab060) 範囲 `[['00aab060', '00aab097']]`
  - `CONDITIONAL_JUMP` [`00aab094`](#insn-00aab094) → [`00aab0a0`](#insn-00aab0a0)
  - `FALL_THROUGH` [`00aab094`](#insn-00aab094) → [`00aab098`](#insn-00aab098)
- ブロック [`00aab098`](#insn-00aab098) 範囲 `[['00aab098', '00aab09f']]`
  - `FALL_THROUGH` [`00aab09c`](#insn-00aab09c) → [`00aab0a0`](#insn-00aab0a0)
- ブロック [`00aab0a0`](#insn-00aab0a0) 範囲 `[['00aab0a0', '00aab0b3']]`
  - `FALL_THROUGH` [`00aab0b0`](#insn-00aab0b0) → [`00aab0b4`](#insn-00aab0b4)
- ブロック [`00aab0b4`](#insn-00aab0b4) 範囲 `[['00aab0b4', '00aab0d3']]`
  - `CONDITIONAL_JUMP` [`00aab0d0`](#insn-00aab0d0) → [`00aab108`](#insn-00aab108)
  - `FALL_THROUGH` [`00aab0d0`](#insn-00aab0d0) → [`00aab0d4`](#insn-00aab0d4)
- ブロック [`00aab0d4`](#insn-00aab0d4) 範囲 `[['00aab0d4', '00aab0e7']]`
  - `CONDITIONAL_JUMP` [`00aab0e4`](#insn-00aab0e4) → [`00aab484`](#insn-00aab484)
  - `FALL_THROUGH` [`00aab0e4`](#insn-00aab0e4) → [`00aab0e8`](#insn-00aab0e8)
- ブロック [`00aab0e8`](#insn-00aab0e8) 範囲 `[['00aab0e8', '00aab107']]`
- ブロック [`00aab108`](#insn-00aab108) 範囲 `[['00aab108', '00aab117']]`
  - `CONDITIONAL_JUMP` [`00aab114`](#insn-00aab114) → [`00aab128`](#insn-00aab128)
  - `FALL_THROUGH` [`00aab114`](#insn-00aab114) → [`00aab118`](#insn-00aab118)
- ブロック [`00aab118`](#insn-00aab118) 範囲 `[['00aab118', '00aab11b']]`
  - `UNCONDITIONAL_JUMP` [`00aab118`](#insn-00aab118) → [`00aab14c`](#insn-00aab14c)
- ブロック [`00aab11c`](#insn-00aab11c) 範囲 `[['00aab11c', '00aab127']]`
  - `CONDITIONAL_JUMP` [`00aab124`](#insn-00aab124) → [`00aab14c`](#insn-00aab14c)
  - `FALL_THROUGH` [`00aab124`](#insn-00aab124) → [`00aab128`](#insn-00aab128)
- ブロック [`00aab128`](#insn-00aab128) 範囲 `[['00aab128', '00aab137']]`
  - `CONDITIONAL_JUMP` [`00aab134`](#insn-00aab134) → [`00aab11c`](#insn-00aab11c)
  - `FALL_THROUGH` [`00aab134`](#insn-00aab134) → [`00aab138`](#insn-00aab138)
- ブロック [`00aab138`](#insn-00aab138) 範囲 `[['00aab138', '00aab13f']]`
  - `CONDITIONAL_JUMP` [`00aab13c`](#insn-00aab13c) → [`00aab1a0`](#insn-00aab1a0)
  - `FALL_THROUGH` [`00aab13c`](#insn-00aab13c) → [`00aab140`](#insn-00aab140)
- ブロック [`00aab140`](#insn-00aab140) 範囲 `[['00aab140', '00aab147']]`
  - `CONDITIONAL_JUMP` [`00aab144`](#insn-00aab144) → [`00aab128`](#insn-00aab128)
  - `FALL_THROUGH` [`00aab144`](#insn-00aab144) → [`00aab148`](#insn-00aab148)
- ブロック [`00aab148`](#insn-00aab148) 範囲 `[['00aab148', '00aab14b']]`
  - `FALL_THROUGH` [`00aab148`](#insn-00aab148) → [`00aab14c`](#insn-00aab14c)
- ブロック [`00aab14c`](#insn-00aab14c) 範囲 `[['00aab14c', '00aab183']]`
  - `CONDITIONAL_JUMP` [`00aab180`](#insn-00aab180) → [`00aab18c`](#insn-00aab18c)
  - `FALL_THROUGH` [`00aab180`](#insn-00aab180) → [`00aab184`](#insn-00aab184)
- ブロック [`00aab184`](#insn-00aab184) 範囲 `[['00aab184', '00aab18b']]`
  - `FALL_THROUGH` [`00aab188`](#insn-00aab188) → [`00aab18c`](#insn-00aab18c)
- ブロック [`00aab18c`](#insn-00aab18c) 範囲 `[['00aab18c', '00aab19f']]`
  - `FALL_THROUGH` [`00aab19c`](#insn-00aab19c) → [`00aab1a0`](#insn-00aab1a0)
- ブロック [`00aab1a0`](#insn-00aab1a0) 範囲 `[['00aab1a0', '00aab1b3']]`
  - `CONDITIONAL_JUMP` [`00aab1b0`](#insn-00aab1b0) → [`00aab1cc`](#insn-00aab1cc)
  - `FALL_THROUGH` [`00aab1b0`](#insn-00aab1b0) → [`00aab1b4`](#insn-00aab1b4)
- ブロック [`00aab1b4`](#insn-00aab1b4) 範囲 `[['00aab1b4', '00aab1cb']]`
  - `UNCONDITIONAL_JUMP` [`00aab1c8`](#insn-00aab1c8) → [`00aab1f0`](#insn-00aab1f0)
- ブロック [`00aab1cc`](#insn-00aab1cc) 範囲 `[['00aab1cc', '00aab1e7']]`
  - `CONDITIONAL_JUMP` [`00aab1e4`](#insn-00aab1e4) → [`00aab1f0`](#insn-00aab1f0)
  - `FALL_THROUGH` [`00aab1e4`](#insn-00aab1e4) → [`00aab1e8`](#insn-00aab1e8)
- ブロック [`00aab1e8`](#insn-00aab1e8) 範囲 `[['00aab1e8', '00aab1ef']]`
  - `FALL_THROUGH` [`00aab1ec`](#insn-00aab1ec) → [`00aab1f0`](#insn-00aab1f0)
- ブロック [`00aab1f0`](#insn-00aab1f0) 範囲 `[['00aab1f0', '00aab1fb']]`
  - `UNCONDITIONAL_JUMP` [`00aab1f8`](#insn-00aab1f8) → [`00aab218`](#insn-00aab218)
- ブロック [`00aab1fc`](#insn-00aab1fc) 範囲 `[['00aab1fc', '00aab203']]`
  - `FALL_THROUGH` [`00aab200`](#insn-00aab200) → [`00aab204`](#insn-00aab204)
- ブロック [`00aab204`](#insn-00aab204) 範囲 `[['00aab204', '00aab217']]`
  - `CONDITIONAL_JUMP` [`00aab214`](#insn-00aab214) → [`00aab0d4`](#insn-00aab0d4)
  - `FALL_THROUGH` [`00aab214`](#insn-00aab214) → [`00aab218`](#insn-00aab218)
- ブロック [`00aab218`](#insn-00aab218) 範囲 `[['00aab218', '00aab273']]`
  - `CONDITIONAL_JUMP` [`00aab270`](#insn-00aab270) → [`00aab0d4`](#insn-00aab0d4)
  - `FALL_THROUGH` [`00aab270`](#insn-00aab270) → [`00aab274`](#insn-00aab274)
- ブロック [`00aab274`](#insn-00aab274) 範囲 `[['00aab274', '00aab2af']]`
  - `UNCONDITIONAL_JUMP` [`00aab2ac`](#insn-00aab2ac) → [`00aab2b4`](#insn-00aab2b4)
- ブロック [`00aab2b0`](#insn-00aab2b0) 範囲 `[['00aab2b0', '00aab2b3']]`
  - `FALL_THROUGH` [`00aab2b0`](#insn-00aab2b0) → [`00aab2b4`](#insn-00aab2b4)
- ブロック [`00aab2b4`](#insn-00aab2b4) 範囲 `[['00aab2b4', '00aab2bb']]`
  - `CONDITIONAL_JUMP` [`00aab2b8`](#insn-00aab2b8) → [`00aab2e0`](#insn-00aab2e0)
  - `FALL_THROUGH` [`00aab2b8`](#insn-00aab2b8) → [`00aab2bc`](#insn-00aab2bc)
- ブロック [`00aab2bc`](#insn-00aab2bc) 範囲 `[['00aab2bc', '00aab2cb']]`
  - `CONDITIONAL_JUMP` [`00aab2c8`](#insn-00aab2c8) → [`00aab2b0`](#insn-00aab2b0)
  - `FALL_THROUGH` [`00aab2c8`](#insn-00aab2c8) → [`00aab2cc`](#insn-00aab2cc)
- ブロック [`00aab2cc`](#insn-00aab2cc) 範囲 `[['00aab2cc', '00aab2d3']]`
  - `CONDITIONAL_JUMP` [`00aab2d0`](#insn-00aab2d0) → [`00aab348`](#insn-00aab348)
  - `FALL_THROUGH` [`00aab2d0`](#insn-00aab2d0) → [`00aab2d4`](#insn-00aab2d4)
- ブロック [`00aab2d4`](#insn-00aab2d4) 範囲 `[['00aab2d4', '00aab2db']]`
  - `CONDITIONAL_JUMP` [`00aab2d8`](#insn-00aab2d8) → [`00aab2bc`](#insn-00aab2bc)
  - `FALL_THROUGH` [`00aab2d8`](#insn-00aab2d8) → [`00aab2dc`](#insn-00aab2dc)
- ブロック [`00aab2dc`](#insn-00aab2dc) 範囲 `[['00aab2dc', '00aab2df']]`
  - `FALL_THROUGH` [`00aab2dc`](#insn-00aab2dc) → [`00aab2e0`](#insn-00aab2e0)
- ブロック [`00aab2e0`](#insn-00aab2e0) 範囲 `[['00aab2e0', '00aab323']]`
  - `CONDITIONAL_JUMP` [`00aab320`](#insn-00aab320) → [`00aab32c`](#insn-00aab32c)
  - `FALL_THROUGH` [`00aab320`](#insn-00aab320) → [`00aab324`](#insn-00aab324)
- ブロック [`00aab324`](#insn-00aab324) 範囲 `[['00aab324', '00aab32b']]`
  - `FALL_THROUGH` [`00aab328`](#insn-00aab328) → [`00aab32c`](#insn-00aab32c)
- ブロック [`00aab32c`](#insn-00aab32c) 範囲 `[['00aab32c', '00aab347']]`
  - `FALL_THROUGH` [`00aab344`](#insn-00aab344) → [`00aab348`](#insn-00aab348)
- ブロック [`00aab348`](#insn-00aab348) 範囲 `[['00aab348', '00aab38b']]`
  - `CONDITIONAL_JUMP` [`00aab388`](#insn-00aab388) → [`00aab1fc`](#insn-00aab1fc)
  - `FALL_THROUGH` [`00aab388`](#insn-00aab388) → [`00aab38c`](#insn-00aab38c)
- ブロック [`00aab38c`](#insn-00aab38c) 範囲 `[['00aab38c', '00aab3a7']]`
  - `CONDITIONAL_JUMP` [`00aab3a4`](#insn-00aab3a4) → [`00aab420`](#insn-00aab420)
  - `FALL_THROUGH` [`00aab3a4`](#insn-00aab3a4) → [`00aab3a8`](#insn-00aab3a8)
- ブロック [`00aab3a8`](#insn-00aab3a8) 範囲 `[['00aab3a8', '00aab3cb']]`
  - `CONDITIONAL_JUMP` [`00aab3c8`](#insn-00aab3c8) → [`00aab3e4`](#insn-00aab3e4)
  - `FALL_THROUGH` [`00aab3c8`](#insn-00aab3c8) → [`00aab3cc`](#insn-00aab3cc)
- ブロック [`00aab3cc`](#insn-00aab3cc) 範囲 `[['00aab3cc', '00aab3d3']]`
  - `CONDITIONAL_JUMP` [`00aab3d0`](#insn-00aab3d0) → [`00aab438`](#insn-00aab438)
  - `FALL_THROUGH` [`00aab3d0`](#insn-00aab3d0) → [`00aab3d4`](#insn-00aab3d4)
- ブロック [`00aab3d4`](#insn-00aab3d4) 範囲 `[['00aab3d4', '00aab3e3']]`
  - `UNCONDITIONAL_JUMP` [`00aab3e0`](#insn-00aab3e0) → [`00aab3e8`](#insn-00aab3e8)
- ブロック [`00aab3e4`](#insn-00aab3e4) 範囲 `[['00aab3e4', '00aab3e7']]`
  - `FALL_THROUGH` [`00aab3e4`](#insn-00aab3e4) → [`00aab3e8`](#insn-00aab3e8)
- ブロック [`00aab3e8`](#insn-00aab3e8) 範囲 `[['00aab3e8', '00aab413']]`
  - `CONDITIONAL_JUMP` [`00aab410`](#insn-00aab410) → [`00aab204`](#insn-00aab204)
  - `FALL_THROUGH` [`00aab410`](#insn-00aab410) → [`00aab414`](#insn-00aab414)
- ブロック [`00aab414`](#insn-00aab414) 範囲 `[['00aab414', '00aab41f']]`
  - `UNCONDITIONAL_JUMP` [`00aab41c`](#insn-00aab41c) → [`00aab204`](#insn-00aab204)
- ブロック [`00aab420`](#insn-00aab420) 範囲 `[['00aab420', '00aab433']]`
  - `CONDITIONAL_JUMP` [`00aab430`](#insn-00aab430) → [`00aab484`](#insn-00aab484)
  - `FALL_THROUGH` [`00aab430`](#insn-00aab430) → [`00aab434`](#insn-00aab434)
- ブロック [`00aab434`](#insn-00aab434) 範囲 `[['00aab434', '00aab437']]`
  - `FALL_THROUGH` [`00aab434`](#insn-00aab434) → [`00aab438`](#insn-00aab438)
- ブロック [`00aab438`](#insn-00aab438) 範囲 `[['00aab438', '00aab44b']]`
  - `CONDITIONAL_JUMP` [`00aab448`](#insn-00aab448) → [`00aab484`](#insn-00aab484)
  - `FALL_THROUGH` [`00aab448`](#insn-00aab448) → [`00aab44c`](#insn-00aab44c)
- ブロック [`00aab44c`](#insn-00aab44c) 範囲 `[['00aab44c', '00aab44f']]`
- ブロック [`00aab484`](#insn-00aab484) 範囲 `[['00aab484', '00aab487']]`

## 命令位置別の参照

- [`00aaafa8`](#insn-00aaafa8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafac`](#insn-00aaafac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafb0`](#insn-00aaafb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafb4`](#insn-00aaafb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafb8`](#insn-00aaafb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafbc`](#insn-00aaafbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafd0`](#insn-00aaafd0) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafe0`](#insn-00aaafe0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafe4`](#insn-00aaafe4) → [`00aab004`](#insn-00aab004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafec`](#insn-00aaafec) → [`007cf950`](../007cf/007cf950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf950` · 推定シンボル `None` · 推定型 `None`
- [`00aaaff4`](#insn-00aaaff4) → [`007cfaa0`](../007cf/007cfaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfaa0` · 推定シンボル `None` · 推定型 `None`
- [`00aaaffc`](#insn-00aaaffc) → [`007cfcd8`](../007cf/007cfcd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfcd8` · 推定シンボル `None` · 推定型 `None`
- [`00aab024`](#insn-00aab024) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab028`](#insn-00aab028) → [`00aab03c`](#insn-00aab03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab02c`](#insn-00aab02c) → [`00aab060`](#insn-00aab060) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab038`](#insn-00aab038) → [`00aab060`](#insn-00aab060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab048`](#insn-00aab048) → [`00aab030`](#insn-00aab030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab050`](#insn-00aab050) → [`00aab0b4`](#insn-00aab0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab058`](#insn-00aab058) → [`00aab03c`](#insn-00aab03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab068`](#insn-00aab068) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aab094`](#insn-00aab094) → [`00aab0a0`](#insn-00aab0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0a4`](#insn-00aab0a4) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aab0d0`](#insn-00aab0d0) → [`00aab108`](#insn-00aab108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0d4`](#insn-00aab0d4) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0dc`](#insn-00aab0dc) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0e4`](#insn-00aab0e4) → [`00aab484`](#insn-00aab484) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0e8`](#insn-00aab0e8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0ec`](#insn-00aab0ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0f0`](#insn-00aab0f0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0f4`](#insn-00aab0f4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0f8`](#insn-00aab0f8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0fc`](#insn-00aab0fc) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab108`](#insn-00aab108) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab114`](#insn-00aab114) → [`00aab128`](#insn-00aab128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab118`](#insn-00aab118) → [`00aab14c`](#insn-00aab14c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab124`](#insn-00aab124) → [`00aab14c`](#insn-00aab14c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab134`](#insn-00aab134) → [`00aab11c`](#insn-00aab11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab13c`](#insn-00aab13c) → [`00aab1a0`](#insn-00aab1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab144`](#insn-00aab144) → [`00aab128`](#insn-00aab128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab154`](#insn-00aab154) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aab180`](#insn-00aab180) → [`00aab18c`](#insn-00aab18c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab190`](#insn-00aab190) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aab1a4`](#insn-00aab1a4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1a8`](#insn-00aab1a8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1b0`](#insn-00aab1b0) → [`00aab1cc`](#insn-00aab1cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1bc`](#insn-00aab1bc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1c8`](#insn-00aab1c8) → [`00aab1f0`](#insn-00aab1f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1d4`](#insn-00aab1d4) → [`00aacb54`](../00aac/00aacb54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aacb54` · 推定シンボル `None` · 推定型 `None`
- [`00aab1dc`](#insn-00aab1dc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1e4`](#insn-00aab1e4) → [`00aab1f0`](#insn-00aab1f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1e8`](#insn-00aab1e8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1ec`](#insn-00aab1ec) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00aab1f8`](#insn-00aab1f8) → [`00aab218`](#insn-00aab218) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab214`](#insn-00aab214) → [`00aab0d4`](#insn-00aab0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab218`](#insn-00aab218) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aab270`](#insn-00aab270) → [`00aab0d4`](#insn-00aab0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab274`](#insn-00aab274) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aab278`](#insn-00aab278) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2ac`](#insn-00aab2ac) → [`00aab2b4`](#insn-00aab2b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2b8`](#insn-00aab2b8) → [`00aab2e0`](#insn-00aab2e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2c8`](#insn-00aab2c8) → [`00aab2b0`](#insn-00aab2b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2d0`](#insn-00aab2d0) → [`00aab348`](#insn-00aab348) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2d8`](#insn-00aab2d8) → [`00aab2bc`](#insn-00aab2bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2e4`](#insn-00aab2e4) → `Stack[-0x8c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2ec`](#insn-00aab2ec) → `Stack[-0x84]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2f0`](#insn-00aab2f0) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aab2f8`](#insn-00aab2f8) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab320`](#insn-00aab320) → [`00aab32c`](#insn-00aab32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab330`](#insn-00aab330) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aab338`](#insn-00aab338) → `Stack[-0x84]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab33c`](#insn-00aab33c) → `Stack[-0x8c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab36c`](#insn-00aab36c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aab388`](#insn-00aab388) → [`00aab1fc`](#insn-00aab1fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab3a4`](#insn-00aab3a4) → [`00aab420`](#insn-00aab420) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab3c8`](#insn-00aab3c8) → [`00aab3e4`](#insn-00aab3e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab3d0`](#insn-00aab3d0) → [`00aab438`](#insn-00aab438) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab3d8`](#insn-00aab3d8) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aab3e0`](#insn-00aab3e0) → [`00aab3e8`](#insn-00aab3e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab404`](#insn-00aab404) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00aab410`](#insn-00aab410) → [`00aab204`](#insn-00aab204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab418`](#insn-00aab418) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00aab41c`](#insn-00aab41c) → [`00aab204`](#insn-00aab204) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab420`](#insn-00aab420) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab428`](#insn-00aab428) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab430`](#insn-00aab430) → [`00aab484`](#insn-00aab484) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab434`](#insn-00aab434) → [`00aacb40`](../00aac/00aacb40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aacb40` · 推定シンボル `None` · 推定型 `None`
- [`00aab438`](#insn-00aab438) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab440`](#insn-00aab440) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab448`](#insn-00aab448) → [`00aab484`](#insn-00aab484) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab44c`](#insn-00aab44c) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`00aab484`](#insn-00aab484) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaafa8`](#insn-00aaafa8)

~~~json
{
  "source": "00aaafa8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafac`](#insn-00aaafac)

~~~json
{
  "source": "00aaafac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafb0`](#insn-00aaafb0)

~~~json
{
  "source": "00aaafb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafb4`](#insn-00aaafb4)

~~~json
{
  "source": "00aaafb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafb8`](#insn-00aaafb8)

~~~json
{
  "source": "00aaafb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafbc`](#insn-00aaafbc)

~~~json
{
  "source": "00aaafbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafd0`](#insn-00aaafd0)

~~~json
{
  "source": "00aaafd0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafe0`](#insn-00aaafe0)

~~~json
{
  "source": "00aaafe0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafe4`](#insn-00aaafe4)

~~~json
{
  "source": "00aaafe4",
  "target": "00aab004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafec`](#insn-00aaafec)

~~~json
{
  "source": "00aaafec",
  "target": "007cf950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaff4`](#insn-00aaaff4)

~~~json
{
  "source": "00aaaff4",
  "target": "007cfaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaffc`](#insn-00aaaffc)

~~~json
{
  "source": "00aaaffc",
  "target": "007cfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab024`](#insn-00aab024)

~~~json
{
  "source": "00aab024",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab028`](#insn-00aab028)

~~~json
{
  "source": "00aab028",
  "target": "00aab03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab02c`](#insn-00aab02c)

~~~json
{
  "source": "00aab02c",
  "target": "00aab060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab038`](#insn-00aab038)

~~~json
{
  "source": "00aab038",
  "target": "00aab060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab048`](#insn-00aab048)

~~~json
{
  "source": "00aab048",
  "target": "00aab030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab050`](#insn-00aab050)

~~~json
{
  "source": "00aab050",
  "target": "00aab0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab058`](#insn-00aab058)

~~~json
{
  "source": "00aab058",
  "target": "00aab03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab068`](#insn-00aab068)

~~~json
{
  "source": "00aab068",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab094`](#insn-00aab094)

~~~json
{
  "source": "00aab094",
  "target": "00aab0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0a4`](#insn-00aab0a4)

~~~json
{
  "source": "00aab0a4",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab0d0`](#insn-00aab0d0)

~~~json
{
  "source": "00aab0d0",
  "target": "00aab108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0d4`](#insn-00aab0d4)

~~~json
{
  "source": "00aab0d4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0dc`](#insn-00aab0dc)

~~~json
{
  "source": "00aab0dc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0e4`](#insn-00aab0e4)

~~~json
{
  "source": "00aab0e4",
  "target": "00aab484",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0e8`](#insn-00aab0e8)

~~~json
{
  "source": "00aab0e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0ec`](#insn-00aab0ec)

~~~json
{
  "source": "00aab0ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0f0`](#insn-00aab0f0)

~~~json
{
  "source": "00aab0f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0f4`](#insn-00aab0f4)

~~~json
{
  "source": "00aab0f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0f8`](#insn-00aab0f8)

~~~json
{
  "source": "00aab0f8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0fc`](#insn-00aab0fc)

~~~json
{
  "source": "00aab0fc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab108`](#insn-00aab108)

~~~json
{
  "source": "00aab108",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab114`](#insn-00aab114)

~~~json
{
  "source": "00aab114",
  "target": "00aab128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab118`](#insn-00aab118)

~~~json
{
  "source": "00aab118",
  "target": "00aab14c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab124`](#insn-00aab124)

~~~json
{
  "source": "00aab124",
  "target": "00aab14c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab134`](#insn-00aab134)

~~~json
{
  "source": "00aab134",
  "target": "00aab11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab13c`](#insn-00aab13c)

~~~json
{
  "source": "00aab13c",
  "target": "00aab1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab144`](#insn-00aab144)

~~~json
{
  "source": "00aab144",
  "target": "00aab128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab154`](#insn-00aab154)

~~~json
{
  "source": "00aab154",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab180`](#insn-00aab180)

~~~json
{
  "source": "00aab180",
  "target": "00aab18c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab190`](#insn-00aab190)

~~~json
{
  "source": "00aab190",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab1a4`](#insn-00aab1a4)

~~~json
{
  "source": "00aab1a4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1a8`](#insn-00aab1a8)

~~~json
{
  "source": "00aab1a8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1b0`](#insn-00aab1b0)

~~~json
{
  "source": "00aab1b0",
  "target": "00aab1cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1bc`](#insn-00aab1bc)

~~~json
{
  "source": "00aab1bc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1c8`](#insn-00aab1c8)

~~~json
{
  "source": "00aab1c8",
  "target": "00aab1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1d4`](#insn-00aab1d4)

~~~json
{
  "source": "00aab1d4",
  "target": "00aacb54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab1dc`](#insn-00aab1dc)

~~~json
{
  "source": "00aab1dc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1e4`](#insn-00aab1e4)

~~~json
{
  "source": "00aab1e4",
  "target": "00aab1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1e8`](#insn-00aab1e8)

~~~json
{
  "source": "00aab1e8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1ec`](#insn-00aab1ec)

~~~json
{
  "source": "00aab1ec",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab1f8`](#insn-00aab1f8)

~~~json
{
  "source": "00aab1f8",
  "target": "00aab218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab214`](#insn-00aab214)

~~~json
{
  "source": "00aab214",
  "target": "00aab0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab218`](#insn-00aab218)

~~~json
{
  "source": "00aab218",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab270`](#insn-00aab270)

~~~json
{
  "source": "00aab270",
  "target": "00aab0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab274`](#insn-00aab274)

~~~json
{
  "source": "00aab274",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab278`](#insn-00aab278)

~~~json
{
  "source": "00aab278",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2ac`](#insn-00aab2ac)

~~~json
{
  "source": "00aab2ac",
  "target": "00aab2b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2b8`](#insn-00aab2b8)

~~~json
{
  "source": "00aab2b8",
  "target": "00aab2e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2c8`](#insn-00aab2c8)

~~~json
{
  "source": "00aab2c8",
  "target": "00aab2b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2d0`](#insn-00aab2d0)

~~~json
{
  "source": "00aab2d0",
  "target": "00aab348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2d8`](#insn-00aab2d8)

~~~json
{
  "source": "00aab2d8",
  "target": "00aab2bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2e4`](#insn-00aab2e4)

~~~json
{
  "source": "00aab2e4",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2ec`](#insn-00aab2ec)

~~~json
{
  "source": "00aab2ec",
  "target": "Stack[-0x84]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2f0`](#insn-00aab2f0)

~~~json
{
  "source": "00aab2f0",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab2f8`](#insn-00aab2f8)

~~~json
{
  "source": "00aab2f8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab320`](#insn-00aab320)

~~~json
{
  "source": "00aab320",
  "target": "00aab32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab330`](#insn-00aab330)

~~~json
{
  "source": "00aab330",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab338`](#insn-00aab338)

~~~json
{
  "source": "00aab338",
  "target": "Stack[-0x84]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab33c`](#insn-00aab33c)

~~~json
{
  "source": "00aab33c",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab36c`](#insn-00aab36c)

~~~json
{
  "source": "00aab36c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab388`](#insn-00aab388)

~~~json
{
  "source": "00aab388",
  "target": "00aab1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab3a4`](#insn-00aab3a4)

~~~json
{
  "source": "00aab3a4",
  "target": "00aab420",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab3c8`](#insn-00aab3c8)

~~~json
{
  "source": "00aab3c8",
  "target": "00aab3e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab3d0`](#insn-00aab3d0)

~~~json
{
  "source": "00aab3d0",
  "target": "00aab438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab3d8`](#insn-00aab3d8)

~~~json
{
  "source": "00aab3d8",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab3e0`](#insn-00aab3e0)

~~~json
{
  "source": "00aab3e0",
  "target": "00aab3e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab404`](#insn-00aab404)

~~~json
{
  "source": "00aab404",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab410`](#insn-00aab410)

~~~json
{
  "source": "00aab410",
  "target": "00aab204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab418`](#insn-00aab418)

~~~json
{
  "source": "00aab418",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab41c`](#insn-00aab41c)

~~~json
{
  "source": "00aab41c",
  "target": "00aab204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab420`](#insn-00aab420)

~~~json
{
  "source": "00aab420",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab428`](#insn-00aab428)

~~~json
{
  "source": "00aab428",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab430`](#insn-00aab430)

~~~json
{
  "source": "00aab430",
  "target": "00aab484",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab434`](#insn-00aab434)

~~~json
{
  "source": "00aab434",
  "target": "00aacb40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab438`](#insn-00aab438)

~~~json
{
  "source": "00aab438",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab440`](#insn-00aab440)

~~~json
{
  "source": "00aab440",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab448`](#insn-00aab448)

~~~json
{
  "source": "00aab448",
  "target": "00aab484",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab44c`](#insn-00aab44c)

~~~json
{
  "source": "00aab44c",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab484`](#insn-00aab484)

~~~json
{
  "source": "00aab484",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
