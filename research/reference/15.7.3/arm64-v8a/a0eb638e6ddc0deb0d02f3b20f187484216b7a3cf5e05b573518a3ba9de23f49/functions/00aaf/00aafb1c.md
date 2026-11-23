# 00aafb1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aafa54`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaf/00aafa54.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-cd7a301aeb9c2d666e214dcc2ec6429e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aafb60`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaf/00aafb60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-a34a1694c2bf3dab8bc31b7ea43e0fd5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aafb1c",
  "name": "FUN_00aafb1c",
  "size": 4748,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb8fd3ba11d02203c10bb01d75667c5ad35c9bc73ff8cccdb3333d010001a1d5",
  "source_text_sha256": "eb8fd3ba11d02203c10bb01d75667c5ad35c9bc73ff8cccdb3333d010001a1d5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aafb1c",
        "00ab0da3"
      ],
      [
        "00ab0e34",
        "00ab0e37"
      ]
    ],
    "bytes_sha256": "10422ee5047b8c98045cf31017512e5fd67eefb59e6e84eef377d286cdf8b56d",
    "instruction_count": 1187,
    "instruction_bytes": 4748,
    "body_bytes": 4748,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0082ea34](../0082e/0082ea34.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0041e380](../0041e/0041e380.md)
- [0044a8d8](../0044a/0044a8d8.md)
- [0044d968](../0044d/0044d968.md)
- [007ac4fc](../007ac/007ac4fc.md)
- [007ac574](../007ac/007ac574.md)
- [0081f580](../0081f/0081f580.md)
- [00aaf9b8](../00aaf/00aaf9b8.md)
- [00ab0e4c](../00ab0/00ab0e4c.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb160](../00bdb/00bdb160.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 41541 bytes

~~~c

void FUN_00aafb1c(void)

{
  byte *pbVar1;
  byte bVar2;
  char cVar3;
  long lVar4;
  bool bVar5;
  int iVar6;
  int iVar7;
  int iVar8;
  int iVar9;
  long lVar10;
  long lVar11;
  undefined8 *puVar12;
  int *piVar13;
  undefined8 uVar14;
  ulong uVar15;
  undefined8 *puVar16;
  undefined8 *puVar17;
  undefined8 *puVar18;
  long *plVar19;
  undefined8 *puVar20;
  ulong uVar21;
  int *piVar22;
  undefined4 uVar23;
  ulong uVar24;
  size_t sVar25;
  int iVar26;
  int iVar27;
  int iVar28;
  int *piVar29;
  int *local_a0;
  int *local_98;
  int *local_90;
  undefined1 auStack_88 [8];
  int *local_80;
  int *local_78;
  long local_68;
  
  lVar4 = tpidr_el0;
  local_68 = *(long *)(lVar4 + 0x28);
  FUN_00aaf9b8(auStack_88);
  uVar24 = 0;
  do {
    if (uVar24 != 3) {
      lVar10 = FUN_0081f580();
      pbVar1 = (byte *)(lVar10 + 0xca3c + uVar24 * 4);
      if (0x2f < (int)((uint)(*(byte *)(lVar10 + 0xca66) ^ pbVar1[2]) << 0x10 |
                       (uint)(*(byte *)(lVar10 + 0xca67) ^ pbVar1[3]) << 0x18 |
                       (uint)(*(byte *)(lVar10 + 0xca65) ^ pbVar1[1]) << 8 |
                      (uint)(*(byte *)(lVar10 + 0xca64) ^ *pbVar1))) {
        lVar11 = FUN_0081f580();
        lVar10 = lVar11 + uVar24 * 4;
        if (((*(char *)(lVar11 + 0xca66) != *(char *)(lVar10 + 0xca3e) ||
             *(char *)(lVar11 + 0xca67) != *(char *)(lVar10 + 0xca3f)) ||
            *(char *)(lVar11 + 0xca65) != *(char *)(lVar10 + 0xca3d)) ||
            *(char *)(lVar11 + 0xca64) != *(char *)(lVar10 + 0xca3c)) {
          lVar10 = FUN_0081f580();
          uVar23 = (undefined4)uVar24;
          puVar18 = *(undefined8 **)((long)&DWORD_00334038 + lVar10);
          puVar17 = (undefined8 *)((long)&DWORD_00334038 + lVar10);
          while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
            while (puVar12 = puVar18, puVar17 = puVar12, (long)*(int *)(puVar12 + 4) <= (long)uVar24
                  ) {
              if ((long)uVar24 <= (long)*(int *)(puVar12 + 4)) goto LAB_00aafccc;
              puVar18 = (undefined8 *)puVar12[1];
              if ((undefined8 *)puVar12[1] == (undefined8 *)0x0) {
                puVar20 = puVar12 + 1;
                goto LAB_00aafc6c;
              }
            }
            puVar18 = (undefined8 *)*puVar12;
          }
LAB_00aafc6c:
          puVar12 = (undefined8 *)_Znwm(0x40);
          puVar12[7] = 0;
          puVar12[6] = 0;
          puVar12[5] = puVar12 + 6;
          *puVar12 = 0;
          puVar12[1] = 0;
          puVar12[2] = puVar17;
          *puVar20 = puVar12;
          plVar19 = *(long **)((long)&QWORD_0033402c + lVar10 + 4);
          *(undefined4 *)(puVar12 + 4) = uVar23;
          lVar11 = *plVar19;
          puVar17 = puVar12;
          if (lVar11 != 0) {
            *(long *)((long)&QWORD_0033402c + lVar10 + 4) = lVar11;
            puVar17 = (undefined8 *)*puVar20;
          }
          FUN_00419064(*(undefined8 *)((long)&DWORD_00334038 + lVar10),puVar17);
          *(long *)((long)&DWORD_00334040 + lVar10) = *(long *)((long)&DWORD_00334040 + lVar10) + 1;
LAB_00aafccc:
          if ((undefined8 *)puVar12[5] == puVar12 + 6) {
            iVar28 = 0;
            local_a0 = (int *)0x0;
            local_98 = (int *)0x0;
            local_90 = (int *)0x0;
LAB_00aafdf0:
            iVar26 = 0;
            do {
              lVar10 = FUN_0081f580();
              puVar18 = *(undefined8 **)((long)&DWORD_00334038 + lVar10);
              puVar17 = (undefined8 *)((long)&DWORD_00334038 + lVar10);
              while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                while (puVar12 = puVar18, puVar17 = puVar12,
                      (long)*(int *)(puVar12 + 4) <= (long)uVar24) {
                  if ((long)uVar24 <= (long)*(int *)(puVar12 + 4)) goto LAB_00aafeb4;
                  puVar18 = (undefined8 *)puVar12[1];
                  if ((undefined8 *)puVar12[1] == (undefined8 *)0x0) {
                    puVar20 = puVar12 + 1;
                    goto LAB_00aafe54;
                  }
                }
                puVar18 = (undefined8 *)*puVar12;
              }
LAB_00aafe54:
              puVar12 = (undefined8 *)_Znwm(0x40);
              puVar12[7] = 0;
              puVar12[6] = 0;
              puVar12[5] = puVar12 + 6;
              *puVar12 = 0;
              puVar12[1] = 0;
              puVar12[2] = puVar17;
              *puVar20 = puVar12;
              plVar19 = *(long **)((long)&QWORD_0033402c + lVar10 + 4);
              *(undefined4 *)(puVar12 + 4) = uVar23;
              lVar11 = *plVar19;
              puVar17 = puVar12;
              if (lVar11 != 0) {
                *(long *)((long)&QWORD_0033402c + lVar10 + 4) = lVar11;
                puVar17 = (undefined8 *)*puVar20;
              }
              FUN_00419064(*(undefined8 *)((long)&DWORD_00334038 + lVar10),puVar17);
              *(long *)((long)&DWORD_00334040 + lVar10) =
                   *(long *)((long)&DWORD_00334040 + lVar10) + 1;
LAB_00aafeb4:
              puVar17 = puVar12 + 6;
              puVar18 = (undefined8 *)*puVar17;
              while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                while (puVar17 = puVar18, *(int *)((long)puVar17 + 0x1c) <= iVar26) {
                  if (iVar26 <= *(int *)((long)puVar17 + 0x1c)) {
                    bVar2 = *(byte *)(puVar17 + 4);
                    piVar22 = local_a0;
                    goto joined_r0x00aaff58;
                  }
                  puVar18 = (undefined8 *)puVar17[1];
                  if ((undefined8 *)puVar17[1] == (undefined8 *)0x0) {
                    puVar20 = puVar17 + 1;
                    goto LAB_00aafef8;
                  }
                }
                puVar18 = (undefined8 *)*puVar17;
              }
LAB_00aafef8:
              puVar18 = (undefined8 *)_Znwm(0x28);
              *puVar18 = 0;
              puVar18[1] = 0;
              puVar18[2] = puVar17;
              *puVar20 = puVar18;
              plVar19 = (long *)puVar12[5];
              *(int *)((long)puVar18 + 0x1c) = iVar26;
              *(undefined1 *)(puVar18 + 4) = 0;
              puVar17 = puVar18;
              if (*plVar19 != 0) {
                puVar12[5] = *plVar19;
                puVar17 = (undefined8 *)*puVar20;
              }
              FUN_00419064(puVar12[6],puVar17);
              puVar12[7] = puVar12[7] + 1;
              bVar2 = *(byte *)(puVar18 + 4);
              piVar22 = local_a0;
joined_r0x00aaff58:
              local_a0 = piVar22;
              if ((bVar2 & 1) == 0) {
                if (local_98 < local_90) {
                  *local_98 = iVar26;
                  local_98 = local_98 + 1;
                }
                else {
                  sVar25 = (long)local_98 - (long)piVar22;
                  lVar10 = (long)sVar25 >> 2;
                  uVar15 = lVar10 + 1;
                  if (uVar15 >> 0x3e != 0) {
                    if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
                      FUN_0044d968(&local_a0);
                    }
                    goto LAB_00ab0e34;
                  }
                  uVar21 = (long)local_90 - (long)piVar22 >> 1;
                  if (uVar21 <= uVar15) {
                    uVar21 = uVar15;
                  }
                  if (0x7ffffffffffffffb < (ulong)((long)local_90 - (long)piVar22)) {
                    uVar21 = 0x3fffffffffffffff;
                  }
                  if (uVar21 == 0) {
                    piVar13 = (int *)0x0;
                  }
                  else {
                    if (uVar21 >> 0x3e != 0) {
                      if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
                        FUN_0041e380();
                      }
                      goto LAB_00ab0e34;
                    }
                    piVar13 = (int *)_Znwm(uVar21 << 2);
                  }
                  piVar29 = piVar13 + lVar10 + 1;
                  piVar13[lVar10] = iVar26;
                  memcpy(piVar13,piVar22,sVar25);
                  local_a0 = piVar13;
                  local_98 = piVar29;
                  local_90 = piVar13 + uVar21;
                  if (piVar22 != (int *)0x0) {
                    _ZdlPv(piVar22);
                    local_98 = piVar29;
                  }
                }
              }
              iVar26 = iVar26 + 1;
            } while (iVar26 != 0x2f);
          }
          else {
            iVar28 = 0;
            puVar17 = (undefined8 *)puVar12[5];
            do {
              puVar18 = (undefined8 *)puVar17[1];
              puVar20 = puVar17;
              if ((undefined8 *)puVar17[1] == (undefined8 *)0x0) {
                do {
                  puVar16 = (undefined8 *)puVar20[2];
                  bVar5 = (undefined8 *)*puVar16 != puVar20;
                  puVar20 = puVar16;
                } while (bVar5);
              }
              else {
                do {
                  puVar16 = puVar18;
                  puVar18 = (undefined8 *)*puVar16;
                } while ((undefined8 *)*puVar16 != (undefined8 *)0x0);
              }
              iVar28 = iVar28 + (*(byte *)(puVar17 + 4) & 1);
              puVar17 = puVar16;
            } while (puVar16 != puVar12 + 6);
            local_a0 = (int *)0x0;
            local_98 = (int *)0x0;
            local_90 = (int *)0x0;
            if (iVar28 != 0x2f) goto LAB_00aafdf0;
            lVar10 = FUN_0081f580();
            puVar18 = *(undefined8 **)((long)&DWORD_00334038 + lVar10);
            puVar17 = (undefined8 *)((long)&DWORD_00334038 + lVar10);
            while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
              while (puVar12 = puVar18, puVar17 = puVar12,
                    (long)*(int *)(puVar12 + 4) <= (long)uVar24) {
                if ((long)uVar24 <= (long)*(int *)(puVar12 + 4)) goto LAB_00aafff8;
                puVar18 = (undefined8 *)puVar12[1];
                if ((undefined8 *)puVar12[1] == (undefined8 *)0x0) {
                  puVar20 = puVar12 + 1;
                  goto LAB_00aafd88;
                }
              }
              puVar18 = (undefined8 *)*puVar12;
            }
LAB_00aafd88:
            puVar12 = (undefined8 *)_Znwm(0x40);
            puVar12[7] = 0;
            puVar12[6] = 0;
            puVar12[5] = puVar12 + 6;
            *puVar12 = 0;
            puVar12[1] = 0;
            puVar12[2] = puVar17;
            *puVar20 = puVar12;
            plVar19 = *(long **)((long)&QWORD_0033402c + lVar10 + 4);
            *(undefined4 *)(puVar12 + 4) = uVar23;
            lVar11 = *plVar19;
            puVar17 = puVar12;
            if (lVar11 != 0) {
              *(long *)((long)&QWORD_0033402c + lVar10 + 4) = lVar11;
              puVar17 = (undefined8 *)*puVar20;
            }
            FUN_00419064(*(undefined8 *)((long)&DWORD_00334038 + lVar10),puVar17);
            *(long *)((long)&DWORD_00334040 + lVar10) =
                 *(long *)((long)&DWORD_00334040 + lVar10) + 1;
LAB_00aafff8:
            puVar17 = puVar12 + 6;
            puVar18 = (undefined8 *)*puVar17;
            while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
              while (puVar17 = puVar18, *(int *)((long)puVar17 + 0x1c) < 0x30) {
                if (*(int *)((long)puVar17 + 0x1c) == 0x2f) {
                  cVar3 = *(char *)(puVar17 + 4);
                  goto joined_r0x00ab00a0;
                }
                puVar18 = (undefined8 *)puVar17[1];
                if ((undefined8 *)puVar17[1] == (undefined8 *)0x0) {
                  puVar20 = puVar17 + 1;
                  goto LAB_00ab003c;
                }
              }
              puVar18 = (undefined8 *)*puVar17;
            }
LAB_00ab003c:
            puVar18 = (undefined8 *)_Znwm(0x28);
            *puVar18 = 0;
            puVar18[1] = 0;
            puVar18[2] = puVar17;
            *puVar20 = puVar18;
            plVar19 = (long *)puVar12[5];
            *(undefined4 *)((long)puVar18 + 0x1c) = 0x2f;
            *(undefined1 *)(puVar18 + 4) = 0;
            puVar17 = puVar18;
            if (*plVar19 != 0) {
              puVar12[5] = *plVar19;
              puVar17 = (undefined8 *)*puVar20;
            }
            FUN_00419064(puVar12[6],puVar17);
            puVar12[7] = puVar12[7] + 1;
            cVar3 = *(char *)(puVar18 + 4);
joined_r0x00ab00a0:
            if (cVar3 == '\0') goto LAB_00aafdf0;
            iVar26 = 0;
            do {
              lVar10 = FUN_0081f580();
              puVar18 = *(undefined8 **)((long)&DWORD_00334038 + lVar10);
              puVar17 = (undefined8 *)((long)&DWORD_00334038 + lVar10);
              while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                while (puVar12 = puVar18, puVar17 = puVar12,
                      (long)*(int *)(puVar12 + 4) <= (long)uVar24) {
                  if ((long)uVar24 <= (long)*(int *)(puVar12 + 4)) goto LAB_00ab017c;
                  puVar18 = (undefined8 *)puVar12[1];
                  if ((undefined8 *)puVar12[1] == (undefined8 *)0x0) {
                    puVar20 = puVar12 + 1;
                    goto LAB_00ab011c;
                  }
                }
                puVar18 = (undefined8 *)*puVar12;
              }
LAB_00ab011c:
              puVar12 = (undefined8 *)_Znwm(0x40);
              puVar12[7] = 0;
              puVar12[6] = 0;
              puVar12[5] = puVar12 + 6;
              *puVar12 = 0;
              puVar12[1] = 0;
              puVar12[2] = puVar17;
              *puVar20 = puVar12;
              plVar19 = *(long **)((long)&QWORD_0033402c + lVar10 + 4);
              *(undefined4 *)(puVar12 + 4) = uVar23;
              lVar11 = *plVar19;
              puVar17 = puVar12;
              if (lVar11 != 0) {
                *(long *)((long)&QWORD_0033402c + lVar10 + 4) = lVar11;
                puVar17 = (undefined8 *)*puVar20;
              }
              FUN_00419064(*(undefined8 *)((long)&DWORD_00334038 + lVar10),puVar17);
              *(long *)((long)&DWORD_00334040 + lVar10) =
                   *(long *)((long)&DWORD_00334040 + lVar10) + 1;
LAB_00ab017c:
              puVar17 = puVar12 + 6;
              puVar18 = (undefined8 *)*puVar17;
              while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                while (puVar17 = puVar18, *(int *)((long)puVar17 + 0x1c) <= iVar26) {
                  if (iVar26 <= *(int *)((long)puVar17 + 0x1c)) {
                    bVar2 = *(byte *)(puVar17 + 4);
                    piVar22 = local_a0;
                    goto joined_r0x00ab0204;
                  }
                  puVar18 = (undefined8 *)puVar17[1];
                  if ((undefined8 *)puVar17[1] == (undefined8 *)0x0) {
                    puVar20 = puVar17 + 1;
                    goto LAB_00ab01c0;
                  }
                }
                puVar18 = (undefined8 *)*puVar17;
              }
LAB_00ab01c0:
              puVar18 = (undefined8 *)_Znwm(0x28);
              *puVar18 = 0;
              puVar18[1] = 0;
              puVar18[2] = puVar17;
              *puVar20 = puVar18;
              plVar19 = (long *)puVar12[5];
              *(int *)((long)puVar18 + 0x1c) = iVar26;
              *(undefined1 *)(puVar18 + 4) = 0;
              puVar17 = puVar18;
              if (*plVar19 != 0) {
                puVar12[5] = *plVar19;
                puVar17 = (undefined8 *)*puVar20;
              }
              FUN_00419064(puVar12[6],puVar17);
              puVar12[7] = puVar12[7] + 1;
              bVar2 = *(byte *)(puVar18 + 4);
              piVar22 = local_a0;
joined_r0x00ab0204:
              local_a0 = piVar22;
              if ((bVar2 & 1) == 0) {
                if (local_98 < local_90) {
                  *local_98 = iVar26;
                  local_98 = local_98 + 1;
                }
                else {
                  sVar25 = (long)local_98 - (long)piVar22;
                  lVar10 = (long)sVar25 >> 2;
                  uVar15 = lVar10 + 1;
                  if (uVar15 >> 0x3e != 0) goto LAB_00ab0d70;
                  uVar21 = (long)local_90 - (long)piVar22 >> 1;
                  if (uVar21 <= uVar15) {
                    uVar21 = uVar15;
                  }
                  if (0x7ffffffffffffffb < (ulong)((long)local_90 - (long)piVar22)) {
                    uVar21 = 0x3fffffffffffffff;
                  }
                  if (uVar21 == 0) {
                    piVar13 = (int *)0x0;
                  }
                  else {
                    if (uVar21 >> 0x3e != 0) {
                      if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
                        FUN_0041e380();
                      }
                      goto LAB_00ab0e34;
                    }
                    piVar13 = (int *)_Znwm(uVar21 << 2);
                  }
                  piVar29 = piVar13 + lVar10 + 1;
                  piVar13[lVar10] = iVar26;
                  memcpy(piVar13,piVar22,sVar25);
                  local_a0 = piVar13;
                  local_98 = piVar29;
                  local_90 = piVar13 + uVar21;
                  if (piVar22 != (int *)0x0) {
                    _ZdlPv(piVar22);
                    local_98 = piVar29;
                  }
                }
                break;
              }
              iVar26 = iVar26 + 1;
            } while (iVar26 != 0x2f);
          }
          if (local_78 == local_80) {
            if (*(long *)(lVar4 + 0x28) == local_68) {
              FUN_00ab0e4c(&local_80);
LAB_00ab0d70:
              if (*(long *)(lVar4 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
                FUN_0044d968(&local_a0);
              }
            }
            goto LAB_00ab0e34;
          }
          piVar22 = local_80;
          if (iVar28 < *local_80) {
            iVar28 = local_80[1];
            piVar13 = local_80;
          }
          else {
            do {
              piVar13 = piVar22;
              piVar22 = piVar13 + 4;
              if (piVar22 == local_78) break;
            } while (*piVar22 <= iVar28);
            iVar28 = piVar13[1];
          }
          iVar26 = (int)((ulong)*(undefined8 *)(piVar13 + 2) >> 0x20);
          if (local_98 == local_a0) {
            lVar10 = FUN_0081f580();
            puVar18 = *(undefined8 **)((long)&DWORD_00334038 + lVar10);
            puVar17 = (undefined8 *)((long)&DWORD_00334038 + lVar10);
            while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
              while (puVar12 = puVar18, puVar17 = puVar12,
                    (long)*(int *)(puVar12 + 4) <= (long)uVar24) {
                if ((long)uVar24 <= (long)*(int *)(puVar12 + 4)) goto LAB_00ab0a70;
                puVar18 = (undefined8 *)puVar12[1];
                if ((undefined8 *)puVar12[1] == (undefined8 *)0x0) {
                  puVar20 = puVar12 + 1;
                  goto LAB_00ab06ac;
                }
              }
              puVar18 = (undefined8 *)*puVar12;
            }
LAB_00ab06ac:
            puVar12 = (undefined8 *)_Znwm(0x40);
            puVar12[7] = 0;
            puVar12[6] = 0;
            puVar12[5] = puVar12 + 6;
            *puVar12 = 0;
            puVar12[1] = 0;
            puVar12[2] = puVar17;
            *puVar20 = puVar12;
            plVar19 = *(long **)((long)&QWORD_0033402c + lVar10 + 4);
            *(undefined4 *)(puVar12 + 4) = uVar23;
            lVar11 = *plVar19;
            puVar17 = puVar12;
            if (lVar11 != 0) {
              *(long *)((long)&QWORD_0033402c + lVar10 + 4) = lVar11;
              puVar17 = (undefined8 *)*puVar20;
            }
            FUN_00419064(*(undefined8 *)((long)&DWORD_00334038 + lVar10),puVar17);
            *(long *)((long)&DWORD_00334040 + lVar10) =
                 *(long *)((long)&DWORD_00334040 + lVar10) + 1;
LAB_00ab0a70:
            puVar17 = puVar12 + 6;
            puVar18 = (undefined8 *)*puVar17;
            while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
              while (puVar17 = puVar18, *(int *)((long)puVar17 + 0x1c) < 0x30) {
                if (*(int *)((long)puVar17 + 0x1c) == 0x2f) {
                  bVar2 = *(byte *)(puVar17 + 4);
                  goto joined_r0x00ab0b18;
                }
                puVar18 = (undefined8 *)puVar17[1];
                if ((undefined8 *)puVar17[1] == (undefined8 *)0x0) {
                  puVar20 = puVar17 + 1;
                  goto LAB_00ab0ab4;
                }
              }
              puVar18 = (undefined8 *)*puVar17;
            }
LAB_00ab0ab4:
            puVar18 = (undefined8 *)_Znwm(0x28);
            *puVar18 = 0;
            puVar18[1] = 0;
            puVar18[2] = puVar17;
            *puVar20 = puVar18;
            plVar19 = (long *)puVar12[5];
            *(undefined4 *)((long)puVar18 + 0x1c) = 0x2f;
            *(undefined1 *)(puVar18 + 4) = 0;
            puVar17 = puVar18;
            if (*plVar19 != 0) {
              puVar12[5] = *plVar19;
              puVar17 = (undefined8 *)*puVar20;
            }
            FUN_00419064(puVar12[6],puVar17);
            puVar12[7] = puVar12[7] + 1;
            bVar2 = *(byte *)(puVar18 + 4);
joined_r0x00ab0b18:
            if ((bVar2 & 1) == 0) {
              iVar9 = FUN_0044a8d8(100);
              iVar27 = 100;
              if (iVar26 < 1) {
                iVar27 = iVar28;
              }
              if (iVar9 < iVar27) {
                uVar14 = FUN_0081f580();
                uVar15 = FUN_007ac4fc(uVar14,uVar24 & 0xffffffff);
                if ((uVar15 & 1) != 0) {
                  uVar14 = FUN_0081f580();
                  uVar15 = FUN_007ac574(uVar14,uVar24 & 0xffffffff);
                  if (((uVar15 & 1) != 0) &&
                     (lVar10 = FUN_0081f580(), BYTE_ARRAY_00334045[lVar10 + 0x13] == 0x2f))
                  goto LAB_00ab0cc8;
                }
                lVar10 = FUN_0081f580();
                puVar18 = *(undefined8 **)((long)&fde_00334020 + lVar10);
                puVar17 = (undefined8 *)((long)&fde_00334020 + lVar10);
                while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                  while (puVar12 = puVar18, puVar17 = puVar12,
                        (long)*(int *)(puVar12 + 4) <= (long)uVar24) {
                    if ((long)uVar24 <= (long)*(int *)(puVar12 + 4)) goto LAB_00ab0c20;
                    puVar18 = (undefined8 *)puVar12[1];
                    if ((undefined8 *)puVar12[1] == (undefined8 *)0x0) {
                      puVar20 = puVar12 + 1;
                      goto LAB_00ab0bc0;
                    }
                  }
                  puVar18 = (undefined8 *)*puVar12;
                }
LAB_00ab0bc0:
                puVar12 = (undefined8 *)_Znwm(0x40);
                puVar12[7] = 0;
                puVar12[6] = 0;
                puVar12[5] = puVar12 + 6;
                *puVar12 = 0;
                puVar12[1] = 0;
                puVar12[2] = puVar17;
                *puVar20 = puVar12;
                plVar19 = *(long **)(BYTE_ARRAY_00333ff9 + lVar10 + 0x1f);
                *(undefined4 *)(puVar12 + 4) = uVar23;
                puVar17 = puVar12;
                if (*plVar19 != 0) {
                  *(long *)(BYTE_ARRAY_00333ff9 + lVar10 + 0x1f) = *plVar19;
                  puVar17 = (undefined8 *)*puVar20;
                }
                FUN_00419064(*(undefined8 *)((long)&fde_00334020 + lVar10),puVar17);
                *(long *)((long)&DWORD_00334028 + lVar10) =
                     *(long *)((long)&DWORD_00334028 + lVar10) + 1;
LAB_00ab0c20:
                puVar18 = (undefined8 *)puVar12[6];
                puVar17 = puVar12 + 6;
                while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                  while (puVar16 = puVar18, puVar17 = puVar16, *(int *)((long)puVar16 + 0x1c) < 0x30
                        ) {
                    if (*(int *)((long)puVar16 + 0x1c) == 0x2f) goto LAB_00ab0cbc;
                    puVar18 = (undefined8 *)puVar16[1];
                    if ((undefined8 *)puVar16[1] == (undefined8 *)0x0) {
                      puVar20 = puVar16 + 1;
                      goto LAB_00ab0c64;
                    }
                  }
                  puVar18 = (undefined8 *)*puVar16;
                }
LAB_00ab0c64:
                puVar16 = (undefined8 *)_Znwm(0x28);
                *puVar16 = 0;
                puVar16[1] = 0;
                puVar16[2] = puVar17;
                *puVar20 = puVar16;
                plVar19 = (long *)puVar12[5];
                *(undefined4 *)((long)puVar16 + 0x1c) = 0x2f;
                *(undefined1 *)(puVar16 + 4) = 0;
                puVar17 = puVar16;
                if (*plVar19 != 0) {
                  puVar12[5] = *plVar19;
                  puVar17 = (undefined8 *)*puVar20;
                }
                FUN_00419064(puVar12[6],puVar17);
                puVar12[7] = puVar12[7] + 1;
LAB_00ab0cbc:
                *(undefined1 *)(puVar16 + 4) = 1;
              }
            }
          }
          else {
            iVar27 = (int)*(undefined8 *)(piVar13 + 2);
            if (iVar27 < 1) {
              iVar9 = 0;
            }
            else {
              iVar9 = 0;
              iVar8 = 0;
              do {
                iVar6 = FUN_0044a8d8(100);
                if (iVar6 < iVar28) {
                  iVar7 = FUN_0044a8d8((ulong)((long)local_98 - (long)local_a0) >> 2);
                  iVar6 = local_a0[iVar7];
                  lVar10 = FUN_0081f580();
                  puVar17 = (undefined8 *)((long)&DWORD_00334038 + lVar10);
                  puVar18 = (undefined8 *)*puVar17;
                  while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                    while (puVar17 = puVar18, (long)*(int *)(puVar17 + 4) <= (long)uVar24) {
                      if ((long)uVar24 <= (long)*(int *)(puVar17 + 4)) goto LAB_00ab0410;
                      puVar18 = (undefined8 *)puVar17[1];
                      if ((undefined8 *)puVar17[1] == (undefined8 *)0x0) {
                        puVar20 = puVar17 + 1;
                        goto LAB_00ab03b0;
                      }
                    }
                    puVar18 = (undefined8 *)*puVar17;
                  }
LAB_00ab03b0:
                  puVar18 = (undefined8 *)_Znwm(0x40);
                  puVar18[7] = 0;
                  puVar18[6] = 0;
                  puVar18[5] = puVar18 + 6;
                  *puVar18 = 0;
                  puVar18[1] = 0;
                  puVar18[2] = puVar17;
                  *puVar20 = puVar18;
                  plVar19 = *(long **)((long)&QWORD_0033402c + lVar10 + 4);
                  *(undefined4 *)(puVar18 + 4) = uVar23;
                  lVar11 = *plVar19;
                  puVar17 = puVar18;
                  if (lVar11 != 0) {
                    *(long *)((long)&QWORD_0033402c + lVar10 + 4) = lVar11;
                    puVar17 = (undefined8 *)*puVar20;
                  }
                  FUN_00419064(*(undefined8 *)((long)&DWORD_00334038 + lVar10),puVar17);
                  *(long *)((long)&DWORD_00334040 + lVar10) =
                       *(long *)((long)&DWORD_00334040 + lVar10) + 1;
                  puVar17 = puVar18;
LAB_00ab0410:
                  puVar18 = puVar17 + 6;
                  puVar20 = (undefined8 *)*puVar18;
                  while (puVar12 = puVar18, puVar20 != (undefined8 *)0x0) {
                    while (puVar18 = puVar20, *(int *)((long)puVar18 + 0x1c) <= iVar6) {
                      if (iVar6 <= *(int *)((long)puVar18 + 0x1c)) {
                        bVar2 = *(byte *)(puVar18 + 4);
                        goto joined_r0x00ab04b4;
                      }
                      puVar20 = (undefined8 *)puVar18[1];
                      if ((undefined8 *)puVar18[1] == (undefined8 *)0x0) {
                        puVar12 = puVar18 + 1;
                        goto LAB_00ab0454;
                      }
                    }
                    puVar20 = (undefined8 *)*puVar18;
                  }
LAB_00ab0454:
                  puVar20 = (undefined8 *)_Znwm(0x28);
                  *puVar20 = 0;
                  puVar20[1] = 0;
                  puVar20[2] = puVar18;
                  *puVar12 = puVar20;
                  plVar19 = (long *)puVar17[5];
                  *(int *)((long)puVar20 + 0x1c) = iVar6;
                  *(undefined1 *)(puVar20 + 4) = 0;
                  puVar18 = puVar20;
                  if (*plVar19 != 0) {
                    puVar17[5] = *plVar19;
                    puVar18 = (undefined8 *)*puVar12;
                  }
                  FUN_00419064(puVar17[6],puVar18);
                  puVar17[7] = puVar17[7] + 1;
                  bVar2 = *(byte *)(puVar20 + 4);
joined_r0x00ab04b4:
                  if ((bVar2 & 1) == 0) {
                    uVar14 = FUN_0081f580();
                    uVar15 = FUN_007ac4fc(uVar14,uVar24 & 0xffffffff);
                    if ((uVar15 & 1) != 0) {
                      uVar14 = FUN_0081f580();
                      uVar15 = FUN_007ac574(uVar14,uVar24 & 0xffffffff);
                      if (((uVar15 & 1) != 0) &&
                         (lVar10 = FUN_0081f580(), iVar6 == (char)BYTE_ARRAY_00334045[lVar10 + 0x13]
                         )) goto LAB_00ab032c;
                    }
                    lVar10 = FUN_0081f580();
                    puVar18 = *(undefined8 **)((long)&fde_00334020 + lVar10);
                    puVar17 = (undefined8 *)((long)&fde_00334020 + lVar10);
                    while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                      while (puVar12 = puVar18, (long)*(int *)(puVar12 + 4) <= (long)uVar24) {
                        if ((long)uVar24 <= (long)*(int *)(puVar12 + 4)) goto LAB_00ab0598;
                        puVar18 = (undefined8 *)puVar12[1];
                        if ((undefined8 *)puVar12[1] == (undefined8 *)0x0) {
                          puVar17 = puVar12 + 1;
                          puVar20 = puVar12;
                          goto LAB_00ab0538;
                        }
                      }
                      puVar17 = puVar12;
                      puVar18 = (undefined8 *)*puVar12;
                    }
LAB_00ab0538:
                    puVar12 = (undefined8 *)_Znwm(0x40);
                    puVar12[7] = 0;
                    puVar12[6] = 0;
                    puVar12[5] = puVar12 + 6;
                    *puVar12 = 0;
                    puVar12[1] = 0;
                    puVar12[2] = puVar20;
                    *puVar17 = puVar12;
                    plVar19 = *(long **)(BYTE_ARRAY_00333ff9 + lVar10 + 0x1f);
                    *(undefined4 *)(puVar12 + 4) = uVar23;
                    puVar18 = puVar12;
                    if (*plVar19 != 0) {
                      *(long *)(BYTE_ARRAY_00333ff9 + lVar10 + 0x1f) = *plVar19;
                      puVar18 = (undefined8 *)*puVar17;
                    }
                    FUN_00419064(*(undefined8 *)((long)&fde_00334020 + lVar10),puVar18);
                    *(long *)((long)&DWORD_00334028 + lVar10) =
                         *(long *)((long)&DWORD_00334028 + lVar10) + 1;
LAB_00ab0598:
                    puVar18 = (undefined8 *)puVar12[6];
                    puVar17 = puVar12 + 6;
                    while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                      while (puVar16 = puVar18, *(int *)((long)puVar16 + 0x1c) <= iVar6) {
                        if (iVar6 <= *(int *)((long)puVar16 + 0x1c)) goto LAB_00ab0630;
                        puVar18 = (undefined8 *)puVar16[1];
                        if ((undefined8 *)puVar16[1] == (undefined8 *)0x0) {
                          puVar17 = puVar16 + 1;
                          puVar20 = puVar16;
                          goto LAB_00ab05dc;
                        }
                      }
                      puVar17 = puVar16;
                      puVar18 = (undefined8 *)*puVar16;
                    }
LAB_00ab05dc:
                    puVar16 = (undefined8 *)_Znwm(0x28);
                    *puVar16 = 0;
                    puVar16[1] = 0;
                    puVar16[2] = puVar20;
                    *puVar17 = puVar16;
                    plVar19 = (long *)puVar12[5];
                    *(int *)((long)puVar16 + 0x1c) = iVar6;
                    *(undefined1 *)(puVar16 + 4) = 0;
                    puVar18 = puVar16;
                    if (*plVar19 != 0) {
                      puVar12[5] = *plVar19;
                      puVar18 = (undefined8 *)*puVar17;
                    }
                    FUN_00419064(puVar12[6],puVar18);
                    puVar12[7] = puVar12[7] + 1;
LAB_00ab0630:
                    piVar22 = local_a0 + iVar7;
                    *(undefined1 *)(puVar16 + 4) = 1;
                    sVar25 = (long)local_98 - (long)(piVar22 + 1);
                    if (sVar25 != 0) {
                      memmove(piVar22,piVar22 + 1,sVar25);
                    }
                    local_98 = (int *)((long)piVar22 + sVar25);
                    iVar9 = iVar9 + 1;
                    if (local_a0 == local_98) break;
                  }
                }
LAB_00ab032c:
                iVar8 = iVar8 + 1;
              } while (iVar8 != iVar27);
            }
            if (((iVar9 < iVar26) && (local_a0 != local_98)) && (0 < iVar26 - iVar9)) {
              iVar28 = 0;
              do {
                iVar8 = FUN_0044a8d8((ulong)((long)local_98 - (long)local_a0) >> 2);
                iVar27 = local_a0[iVar8];
                lVar10 = FUN_0081f580();
                puVar18 = *(undefined8 **)((long)&DWORD_00334038 + lVar10);
                puVar17 = (undefined8 *)((long)&DWORD_00334038 + lVar10);
                while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                  while (puVar12 = puVar18, puVar17 = puVar12,
                        (long)*(int *)(puVar12 + 4) <= (long)uVar24) {
                    if ((long)uVar24 <= (long)*(int *)(puVar12 + 4)) goto LAB_00ab0818;
                    puVar18 = (undefined8 *)puVar12[1];
                    if ((undefined8 *)puVar12[1] == (undefined8 *)0x0) {
                      puVar20 = puVar12 + 1;
                      goto LAB_00ab07b8;
                    }
                  }
                  puVar18 = (undefined8 *)*puVar12;
                }
LAB_00ab07b8:
                puVar12 = (undefined8 *)_Znwm(0x40);
                puVar12[7] = 0;
                puVar12[6] = 0;
                puVar12[5] = puVar12 + 6;
                *puVar12 = 0;
                puVar12[1] = 0;
                puVar12[2] = puVar17;
                *puVar20 = puVar12;
                plVar19 = *(long **)((long)&QWORD_0033402c + lVar10 + 4);
                *(undefined4 *)(puVar12 + 4) = uVar23;
                lVar11 = *plVar19;
                puVar17 = puVar12;
                if (lVar11 != 0) {
                  *(long *)((long)&QWORD_0033402c + lVar10 + 4) = lVar11;
                  puVar17 = (undefined8 *)*puVar20;
                }
                FUN_00419064(*(undefined8 *)((long)&DWORD_00334038 + lVar10),puVar17);
                *(long *)((long)&DWORD_00334040 + lVar10) =
                     *(long *)((long)&DWORD_00334040 + lVar10) + 1;
LAB_00ab0818:
                puVar17 = puVar12 + 6;
                puVar18 = (undefined8 *)*puVar17;
                while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                  while (puVar17 = puVar18, *(int *)((long)puVar17 + 0x1c) <= iVar27) {
                    if (iVar27 <= *(int *)((long)puVar17 + 0x1c)) {
                      bVar2 = *(byte *)(puVar17 + 4);
                      goto joined_r0x00ab08bc;
                    }
                    puVar18 = (undefined8 *)puVar17[1];
                    if ((undefined8 *)puVar17[1] == (undefined8 *)0x0) {
                      puVar20 = puVar17 + 1;
                      goto LAB_00ab085c;
                    }
                  }
                  puVar18 = (undefined8 *)*puVar17;
                }
LAB_00ab085c:
                puVar18 = (undefined8 *)_Znwm(0x28);
                *puVar18 = 0;
                puVar18[1] = 0;
                puVar18[2] = puVar17;
                *puVar20 = puVar18;
                plVar19 = (long *)puVar12[5];
                *(int *)((long)puVar18 + 0x1c) = iVar27;
                *(undefined1 *)(puVar18 + 4) = 0;
                puVar17 = puVar18;
                if (*plVar19 != 0) {
                  puVar12[5] = *plVar19;
                  puVar17 = (undefined8 *)*puVar20;
                }
                FUN_00419064(puVar12[6],puVar17);
                puVar12[7] = puVar12[7] + 1;
                bVar2 = *(byte *)(puVar18 + 4);
joined_r0x00ab08bc:
                if ((bVar2 & 1) == 0) {
                  uVar14 = FUN_0081f580();
                  uVar15 = FUN_007ac4fc(uVar14,uVar24 & 0xffffffff);
                  if ((uVar15 & 1) != 0) {
                    uVar14 = FUN_0081f580();
                    uVar15 = FUN_007ac574(uVar14,uVar24 & 0xffffffff);
                    if (((uVar15 & 1) != 0) &&
                       (lVar10 = FUN_0081f580(), iVar27 == (char)BYTE_ARRAY_00334045[lVar10 + 0x13])
                       ) goto LAB_00ab0748;
                  }
                  lVar10 = FUN_0081f580();
                  puVar18 = *(undefined8 **)((long)&fde_00334020 + lVar10);
                  puVar17 = (undefined8 *)((long)&fde_00334020 + lVar10);
                  while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                    while (puVar12 = puVar18, puVar17 = puVar12,
                          (long)*(int *)(puVar12 + 4) <= (long)uVar24) {
                      if ((long)uVar24 <= (long)*(int *)(puVar12 + 4)) goto LAB_00ab09a0;
                      puVar18 = (undefined8 *)puVar12[1];
                      if ((undefined8 *)puVar12[1] == (undefined8 *)0x0) {
                        puVar20 = puVar12 + 1;
                        goto LAB_00ab0940;
                      }
                    }
                    puVar18 = (undefined8 *)*puVar12;
                  }
LAB_00ab0940:
                  puVar12 = (undefined8 *)_Znwm(0x40);
                  puVar12[7] = 0;
                  puVar12[6] = 0;
                  puVar12[5] = puVar12 + 6;
                  *puVar12 = 0;
                  puVar12[1] = 0;
                  puVar12[2] = puVar17;
                  *puVar20 = puVar12;
                  plVar19 = *(long **)(BYTE_ARRAY_00333ff9 + lVar10 + 0x1f);
                  *(undefined4 *)(puVar12 + 4) = uVar23;
                  puVar17 = puVar12;
                  if (*plVar19 != 0) {
                    *(long *)(BYTE_ARRAY_00333ff9 + lVar10 + 0x1f) = *plVar19;
                    puVar17 = (undefined8 *)*puVar20;
                  }
                  FUN_00419064(*(undefined8 *)((long)&fde_00334020 + lVar10),puVar17);
                  *(long *)((long)&DWORD_00334028 + lVar10) =
                       *(long *)((long)&DWORD_00334028 + lVar10) + 1;
LAB_00ab09a0:
                  puVar18 = (undefined8 *)puVar12[6];
                  puVar17 = puVar12 + 6;
                  while (puVar20 = puVar17, puVar18 != (undefined8 *)0x0) {
                    while (puVar16 = puVar18, puVar17 = puVar16,
                          *(int *)((long)puVar16 + 0x1c) <= iVar27) {
                      if (iVar27 <= *(int *)((long)puVar16 + 0x1c)) goto LAB_00ab0a38;
                      puVar18 = (undefined8 *)puVar16[1];
                      if ((undefined8 *)puVar16[1] == (undefined8 *)0x0) {
                        puVar20 = puVar16 + 1;
                        goto LAB_00ab09e4;
                      }
                    }
                    puVar18 = (undefined8 *)*puVar16;
                  }
LAB_00ab09e4:
                  puVar16 = (undefined8 *)_Znwm(0x28);
                  *puVar16 = 0;
                  puVar16[1] = 0;
                  puVar16[2] = puVar17;
                  *puVar20 = puVar16;
                  plVar19 = (long *)puVar12[5];
                  *(int *)((long)puVar16 + 0x1c) = iVar27;
                  *(undefined1 *)(puVar16 + 4) = 0;
                  puVar17 = puVar16;
                  if (*plVar19 != 0) {
                    puVar12[5] = *plVar19;
                    puVar17 = (undefined8 *)*puVar20;
                  }
                  FUN_00419064(puVar12[6],puVar17);
                  puVar12[7] = puVar12[7] + 1;
LAB_00ab0a38:
                  piVar22 = local_a0 + iVar8;
                  *(undefined1 *)(puVar16 + 4) = 1;
                  sVar25 = (long)local_98 - (long)(piVar22 + 1);
                  if (sVar25 != 0) {
                    memmove(piVar22,piVar22 + 1,sVar25);
                  }
                  local_98 = (int *)((long)piVar22 + sVar25);
                  if (local_a0 == local_98) break;
                }
LAB_00ab0748:
                iVar28 = iVar28 + 1;
              } while (iVar28 != iVar26 - iVar9);
            }
          }
LAB_00ab0cc8:
          if (local_a0 != (int *)0x0) {
            local_98 = local_a0;
            _ZdlPv(local_a0);
          }
        }
      }
    }
    uVar24 = uVar24 + 1;
    if (uVar24 == 10) {
      if (local_80 != (int *)0x0) {
        local_78 = local_80;
        _ZdlPv(local_80);
      }
      if (*(long *)(lVar4 + 0x28) == local_68) {
        return;
      }
LAB_00ab0e34:
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aafb1c"></a> `00aafb1c` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00aafb20"></a> `00aafb20` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aafb24"></a> `00aafb24` | `fc 6f 06 a9` | stp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aafb28"></a> `00aafb28` | `fa 67 07 a9` | stp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aafb2c"></a> `00aafb2c` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aafb30"></a> `00aafb30` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aafb34"></a> `00aafb34` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aafb38"></a> `00aafb38` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aafb3c"></a> `00aafb3c` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aafb40"></a> `00aafb40` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00aafb44"></a> `00aafb44` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aafb48"></a> `00aafb48` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aafb4c"></a> `00aafb4c` | `e8 a3 00 91` | add x8,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00aafb50"></a> `00aafb50` | `9a ff ff 97` | bl 0x00aaf9b8 | `UNCONDITIONAL_CALL`
<a id="insn-00aafb54"></a> `00aafb54` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00aafb58"></a> `00aafb58` | `9c 47 99 52` | mov w28,#0xca3c | `FALL_THROUGH`
<a id="insn-00aafb5c"></a> `00aafb5c` | `04 00 00 14` | b 0x00aafb6c | `UNCONDITIONAL_JUMP`
<a id="insn-00aafb60"></a> `00aafb60` | `73 06 00 91` | add x19,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00aafb64"></a> `00aafb64` | `7f 2a 00 f1` | cmp x19,#0xa | `FALL_THROUGH`
<a id="insn-00aafb68"></a> `00aafb68` | `80 8b 00 54` | b.eq 0x00ab0cd8 | `CONDITIONAL_JUMP`
<a id="insn-00aafb6c"></a> `00aafb6c` | `7f 0e 00 f1` | cmp x19,#0x3 | `FALL_THROUGH`
<a id="insn-00aafb70"></a> `00aafb70` | `80 ff ff 54` | b.eq 0x00aafb60 | `CONDITIONAL_JUMP`
<a id="insn-00aafb74"></a> `00aafb74` | `83 be f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aafb78"></a> `00aafb78` | `74 f6 7e d3` | lsl x20,x19,#0x2 | `FALL_THROUGH`
<a id="insn-00aafb7c"></a> `00aafb7c` | `08 00 1c 8b` | add x8,x0,x28 | `FALL_THROUGH`
<a id="insn-00aafb80"></a> `00aafb80` | `09 30 40 91` | add x9,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aafb84"></a> `00aafb84` | `2b 99 69 39` | ldrb w11,[x9, #0xa66] | `FALL_THROUGH`
<a id="insn-00aafb88"></a> `00aafb88` | `2c 9d 69 39` | ldrb w12,[x9, #0xa67] | `FALL_THROUGH`
<a id="insn-00aafb8c"></a> `00aafb8c` | `08 01 14 8b` | add x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00aafb90"></a> `00aafb90` | `0a 09 40 39` | ldrb w10,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aafb94"></a> `00aafb94` | `0d 05 40 39` | ldrb w13,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aafb98"></a> `00aafb98` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aafb9c"></a> `00aafb9c` | `0b 0d 40 39` | ldrb w11,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00aafba0"></a> `00aafba0` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00aafba4"></a> `00aafba4` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00aafba8"></a> `00aafba8` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00aafbac"></a> `00aafbac` | `2c 95 69 39` | ldrb w12,[x9, #0xa65] | `FALL_THROUGH`
<a id="insn-00aafbb0"></a> `00aafbb0` | `29 91 69 39` | ldrb w9,[x9, #0xa64] | `FALL_THROUGH`
<a id="insn-00aafbb4"></a> `00aafbb4` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aafbb8"></a> `00aafbb8` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aafbbc"></a> `00aafbbc` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aafbc0"></a> `00aafbc0` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aafbc4"></a> `00aafbc4` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00aafbc8"></a> `00aafbc8` | `1f c1 00 71` | cmp w8,#0x30 | `FALL_THROUGH`
<a id="insn-00aafbcc"></a> `00aafbcc` | `ab fc ff 54` | b.lt 0x00aafb60 | `CONDITIONAL_JUMP`
<a id="insn-00aafbd0"></a> `00aafbd0` | `6c be f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aafbd4"></a> `00aafbd4` | `08 00 14 8b` | add x8,x0,x20 | `FALL_THROUGH`
<a id="insn-00aafbd8"></a> `00aafbd8` | `09 30 40 91` | add x9,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aafbdc"></a> `00aafbdc` | `08 01 1c 8b` | add x8,x8,x28 | `FALL_THROUGH`
<a id="insn-00aafbe0"></a> `00aafbe0` | `2b 99 69 39` | ldrb w11,[x9, #0xa66] | `FALL_THROUGH`
<a id="insn-00aafbe4"></a> `00aafbe4` | `2c 9d 69 39` | ldrb w12,[x9, #0xa67] | `FALL_THROUGH`
<a id="insn-00aafbe8"></a> `00aafbe8` | `0a 09 40 39` | ldrb w10,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aafbec"></a> `00aafbec` | `0d 05 40 39` | ldrb w13,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aafbf0"></a> `00aafbf0` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aafbf4"></a> `00aafbf4` | `0b 0d 40 39` | ldrb w11,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00aafbf8"></a> `00aafbf8` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00aafbfc"></a> `00aafbfc` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00aafc00"></a> `00aafc00` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00aafc04"></a> `00aafc04` | `2c 95 69 39` | ldrb w12,[x9, #0xa65] | `FALL_THROUGH`
<a id="insn-00aafc08"></a> `00aafc08` | `29 91 69 39` | ldrb w9,[x9, #0xa64] | `FALL_THROUGH`
<a id="insn-00aafc0c"></a> `00aafc0c` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aafc10"></a> `00aafc10` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aafc14"></a> `00aafc14` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aafc18"></a> `00aafc18` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aafc1c"></a> `00aafc1c` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00aafc20"></a> `00aafc20` | `08 fa ff 34` | cbz w8,0x00aafb60 | `CONDITIONAL_JUMP`
<a id="insn-00aafc24"></a> `00aafc24` | `57 be f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aafc28"></a> `00aafc28` | `15 d0 4c 91` | add x21,x0,#0x334, LSL #12 | `FALL_THROUGH`
<a id="insn-00aafc2c"></a> `00aafc2c` | `f7 03 15 aa` | mov x23,x21 | `FALL_THROUGH`
<a id="insn-00aafc30"></a> `00aafc30` | `e8 8e 43 f8` | ldr x8,[x23, #0x38]! | `FALL_THROUGH`
<a id="insn-00aafc34"></a> `00aafc34` | `c8 00 00 b5` | cbnz x8,0x00aafc4c | `CONDITIONAL_JUMP`
<a id="insn-00aafc38"></a> `00aafc38` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00aafc3c"></a> `00aafc3c` | `0c 00 00 14` | b 0x00aafc6c | `UNCONDITIONAL_JUMP`
<a id="insn-00aafc40"></a> `00aafc40` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00aafc44"></a> `00aafc44` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00aafc48"></a> `00aafc48` | `28 01 00 b4` | cbz x8,0x00aafc6c | `CONDITIONAL_JUMP`
<a id="insn-00aafc4c"></a> `00aafc4c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00aafc50"></a> `00aafc50` | `08 21 80 b9` | ldrsw x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aafc54"></a> `00aafc54` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00aafc58"></a> `00aafc58` | `4b ff ff 54` | b.lt 0x00aafc40 | `CONDITIONAL_JUMP`
<a id="insn-00aafc5c"></a> `00aafc5c` | `6d 03 00 54` | b.le 0x00aafcc8 | `CONDITIONAL_JUMP`
<a id="insn-00aafc60"></a> `00aafc60` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00aafc64"></a> `00aafc64` | `48 ff ff b5` | cbnz x8,0x00aafc4c | `CONDITIONAL_JUMP`
<a id="insn-00aafc68"></a> `00aafc68` | `d7 22 00 91` | add x23,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aafc6c"></a> `00aafc6c` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aafc70"></a> `00aafc70` | `e0 ac 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aafc74"></a> `00aafc74` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aafc78"></a> `00aafc78` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00aafc7c"></a> `00aafc7c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aafc80"></a> `00aafc80` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00aafc84"></a> `00aafc84` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aafc88"></a> `00aafc88` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aafc8c"></a> `00aafc8c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aafc90"></a> `00aafc90` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aafc94"></a> `00aafc94` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-00aafc98"></a> `00aafc98` | `a8 1a 40 f9` | ldr x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00aafc9c"></a> `00aafc9c` | `13 20 00 b9` | str w19,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aafca0"></a> `00aafca0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aafca4"></a> `00aafca4` | `68 00 00 b4` | cbz x8,0x00aafcb0 | `CONDITIONAL_JUMP`
<a id="insn-00aafca8"></a> `00aafca8` | `a8 1a 00 f9` | str x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00aafcac"></a> `00aafcac` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00aafcb0"></a> `00aafcb0` | `a0 1e 40 f9` | ldr x0,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00aafcb4"></a> `00aafcb4` | `ec a4 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aafcb8"></a> `00aafcb8` | `a8 22 40 f9` | ldr x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00aafcbc"></a> `00aafcbc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aafcc0"></a> `00aafcc0` | `a8 22 00 f9` | str x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00aafcc4"></a> `00aafcc4` | `02 00 00 14` | b 0x00aafccc | `UNCONDITIONAL_JUMP`
<a id="insn-00aafcc8"></a> `00aafcc8` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00aafccc"></a> `00aafccc` | `89 16 40 f9` | ldr x9,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aafcd0"></a> `00aafcd0` | `88 c2 00 91` | add x8,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00aafcd4"></a> `00aafcd4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00aafcd8"></a> `00aafcd8` | `60 08 00 54` | b.eq 0x00aafde4 | `CONDITIONAL_JUMP`
<a id="insn-00aafcdc"></a> `00aafcdc` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-00aafce0"></a> `00aafce0` | `07 00 00 14` | b 0x00aafcfc | `UNCONDITIONAL_JUMP`
<a id="insn-00aafce4"></a> `00aafce4` | `29 81 40 39` | ldrb w9,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00aafce8"></a> `00aafce8` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00aafcec"></a> `00aafcec` | `29 01 00 12` | and w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aafcf0"></a> `00aafcf0` | `18 03 09 0b` | add w24,w24,w9 | `FALL_THROUGH`
<a id="insn-00aafcf4"></a> `00aafcf4` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-00aafcf8"></a> `00aafcf8` | `c0 01 00 54` | b.eq 0x00aafd30 | `CONDITIONAL_JUMP`
<a id="insn-00aafcfc"></a> `00aafcfc` | `2b 05 40 f9` | ldr x11,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00aafd00"></a> `00aafd00` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00aafd04"></a> `00aafd04` | `ab 00 00 b4` | cbz x11,0x00aafd18 | `CONDITIONAL_JUMP`
<a id="insn-00aafd08"></a> `00aafd08` | `ea 03 0b aa` | mov x10,x11 | `FALL_THROUGH`
<a id="insn-00aafd0c"></a> `00aafd0c` | `6b 01 40 f9` | ldr x11,[x11] | `FALL_THROUGH`
<a id="insn-00aafd10"></a> `00aafd10` | `cb ff ff b5` | cbnz x11,0x00aafd08 | `CONDITIONAL_JUMP`
<a id="insn-00aafd14"></a> `00aafd14` | `f4 ff ff 17` | b 0x00aafce4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafd18"></a> `00aafd18` | `8a 09 40 f9` | ldr x10,[x12, #0x10] | `FALL_THROUGH`
<a id="insn-00aafd1c"></a> `00aafd1c` | `4b 01 40 f9` | ldr x11,[x10] | `FALL_THROUGH`
<a id="insn-00aafd20"></a> `00aafd20` | `7f 01 0c eb` | cmp x11,x12 | `FALL_THROUGH`
<a id="insn-00aafd24"></a> `00aafd24` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00aafd28"></a> `00aafd28` | `81 ff ff 54` | b.ne 0x00aafd18 | `CONDITIONAL_JUMP`
<a id="insn-00aafd2c"></a> `00aafd2c` | `ee ff ff 17` | b 0x00aafce4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafd30"></a> `00aafd30` | `1f bf 00 71` | cmp w24,#0x2f | `FALL_THROUGH`
<a id="insn-00aafd34"></a> `00aafd34` | `ff 7f 01 a9` | stp xzr,xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aafd38"></a> `00aafd38` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aafd3c"></a> `00aafd3c` | `a1 05 00 54` | b.ne 0x00aafdf0 | `CONDITIONAL_JUMP`
<a id="insn-00aafd40"></a> `00aafd40` | `10 be f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aafd44"></a> `00aafd44` | `15 d0 4c 91` | add x21,x0,#0x334, LSL #12 | `FALL_THROUGH`
<a id="insn-00aafd48"></a> `00aafd48` | `f7 03 15 aa` | mov x23,x21 | `FALL_THROUGH`
<a id="insn-00aafd4c"></a> `00aafd4c` | `e8 8e 43 f8` | ldr x8,[x23, #0x38]! | `FALL_THROUGH`
<a id="insn-00aafd50"></a> `00aafd50` | `c8 00 00 b5` | cbnz x8,0x00aafd68 | `CONDITIONAL_JUMP`
<a id="insn-00aafd54"></a> `00aafd54` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00aafd58"></a> `00aafd58` | `0c 00 00 14` | b 0x00aafd88 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafd5c"></a> `00aafd5c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00aafd60"></a> `00aafd60` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00aafd64"></a> `00aafd64` | `28 01 00 b4` | cbz x8,0x00aafd88 | `CONDITIONAL_JUMP`
<a id="insn-00aafd68"></a> `00aafd68` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00aafd6c"></a> `00aafd6c` | `08 21 80 b9` | ldrsw x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aafd70"></a> `00aafd70` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00aafd74"></a> `00aafd74` | `4b ff ff 54` | b.lt 0x00aafd5c | `CONDITIONAL_JUMP`
<a id="insn-00aafd78"></a> `00aafd78` | `ed 13 00 54` | b.le 0x00aafff4 | `CONDITIONAL_JUMP`
<a id="insn-00aafd7c"></a> `00aafd7c` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00aafd80"></a> `00aafd80` | `48 ff ff b5` | cbnz x8,0x00aafd68 | `CONDITIONAL_JUMP`
<a id="insn-00aafd84"></a> `00aafd84` | `d7 22 00 91` | add x23,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aafd88"></a> `00aafd88` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aafd8c"></a> `00aafd8c` | `99 ac 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aafd90"></a> `00aafd90` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aafd94"></a> `00aafd94` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00aafd98"></a> `00aafd98` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aafd9c"></a> `00aafd9c` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00aafda0"></a> `00aafda0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aafda4"></a> `00aafda4` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aafda8"></a> `00aafda8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aafdac"></a> `00aafdac` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aafdb0"></a> `00aafdb0` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-00aafdb4"></a> `00aafdb4` | `a8 1a 40 f9` | ldr x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00aafdb8"></a> `00aafdb8` | `13 20 00 b9` | str w19,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aafdbc"></a> `00aafdbc` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aafdc0"></a> `00aafdc0` | `68 00 00 b4` | cbz x8,0x00aafdcc | `CONDITIONAL_JUMP`
<a id="insn-00aafdc4"></a> `00aafdc4` | `a8 1a 00 f9` | str x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00aafdc8"></a> `00aafdc8` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00aafdcc"></a> `00aafdcc` | `a0 1e 40 f9` | ldr x0,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00aafdd0"></a> `00aafdd0` | `a5 a4 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aafdd4"></a> `00aafdd4` | `a8 22 40 f9` | ldr x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00aafdd8"></a> `00aafdd8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aafddc"></a> `00aafddc` | `a8 22 00 f9` | str x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00aafde0"></a> `00aafde0` | `86 00 00 14` | b 0x00aafff8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafde4"></a> `00aafde4` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-00aafde8"></a> `00aafde8` | `ff 7f 01 a9` | stp xzr,xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aafdec"></a> `00aafdec` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aafdf0"></a> `00aafdf0` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00aafdf4"></a> `00aafdf4` | `06 00 00 14` | b 0x00aafe0c | `UNCONDITIONAL_JUMP`
<a id="insn-00aafdf8"></a> `00aafdf8` | `37 47 00 b8` | str w23,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-00aafdfc"></a> `00aafdfc` | `f9 0f 00 f9` | str x25,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aafe00"></a> `00aafe00` | `f7 06 00 11` | add w23,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00aafe04"></a> `00aafe04` | `ff be 00 71` | cmp w23,#0x2f | `FALL_THROUGH`
<a id="insn-00aafe08"></a> `00aafe08` | `00 25 00 54` | b.eq 0x00ab02a8 | `CONDITIONAL_JUMP`
<a id="insn-00aafe0c"></a> `00aafe0c` | `dd bd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aafe10"></a> `00aafe10` | `15 d0 4c 91` | add x21,x0,#0x334, LSL #12 | `FALL_THROUGH`
<a id="insn-00aafe14"></a> `00aafe14` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00aafe18"></a> `00aafe18` | `28 8f 43 f8` | ldr x8,[x25, #0x38]! | `FALL_THROUGH`
<a id="insn-00aafe1c"></a> `00aafe1c` | `c8 00 00 b5` | cbnz x8,0x00aafe34 | `CONDITIONAL_JUMP`
<a id="insn-00aafe20"></a> `00aafe20` | `f6 03 19 aa` | mov x22,x25 | `FALL_THROUGH`
<a id="insn-00aafe24"></a> `00aafe24` | `0c 00 00 14` | b 0x00aafe54 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafe28"></a> `00aafe28` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00aafe2c"></a> `00aafe2c` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00aafe30"></a> `00aafe30` | `28 01 00 b4` | cbz x8,0x00aafe54 | `CONDITIONAL_JUMP`
<a id="insn-00aafe34"></a> `00aafe34` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00aafe38"></a> `00aafe38` | `08 21 80 b9` | ldrsw x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aafe3c"></a> `00aafe3c` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00aafe40"></a> `00aafe40` | `4b ff ff 54` | b.lt 0x00aafe28 | `CONDITIONAL_JUMP`
<a id="insn-00aafe44"></a> `00aafe44` | `6d 03 00 54` | b.le 0x00aafeb0 | `CONDITIONAL_JUMP`
<a id="insn-00aafe48"></a> `00aafe48` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00aafe4c"></a> `00aafe4c` | `48 ff ff b5` | cbnz x8,0x00aafe34 | `CONDITIONAL_JUMP`
<a id="insn-00aafe50"></a> `00aafe50` | `d9 22 00 91` | add x25,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aafe54"></a> `00aafe54` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aafe58"></a> `00aafe58` | `66 ac 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aafe5c"></a> `00aafe5c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aafe60"></a> `00aafe60` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00aafe64"></a> `00aafe64` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aafe68"></a> `00aafe68` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00aafe6c"></a> `00aafe6c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aafe70"></a> `00aafe70` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aafe74"></a> `00aafe74` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aafe78"></a> `00aafe78` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aafe7c"></a> `00aafe7c` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00aafe80"></a> `00aafe80` | `a8 1a 40 f9` | ldr x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00aafe84"></a> `00aafe84` | `13 20 00 b9` | str w19,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aafe88"></a> `00aafe88` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aafe8c"></a> `00aafe8c` | `68 00 00 b4` | cbz x8,0x00aafe98 | `CONDITIONAL_JUMP`
<a id="insn-00aafe90"></a> `00aafe90` | `a8 1a 00 f9` | str x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00aafe94"></a> `00aafe94` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00aafe98"></a> `00aafe98` | `a0 1e 40 f9` | ldr x0,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00aafe9c"></a> `00aafe9c` | `72 a4 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aafea0"></a> `00aafea0` | `a8 22 40 f9` | ldr x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00aafea4"></a> `00aafea4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aafea8"></a> `00aafea8` | `a8 22 00 f9` | str x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00aafeac"></a> `00aafeac` | `02 00 00 14` | b 0x00aafeb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafeb0"></a> `00aafeb0` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00aafeb4"></a> `00aafeb4` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00aafeb8"></a> `00aafeb8` | `28 0f 43 f8` | ldr x8,[x25, #0x30]! | `FALL_THROUGH`
<a id="insn-00aafebc"></a> `00aafebc` | `c8 00 00 b5` | cbnz x8,0x00aafed4 | `CONDITIONAL_JUMP`
<a id="insn-00aafec0"></a> `00aafec0` | `f6 03 19 aa` | mov x22,x25 | `FALL_THROUGH`
<a id="insn-00aafec4"></a> `00aafec4` | `0d 00 00 14` | b 0x00aafef8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aafec8"></a> `00aafec8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00aafecc"></a> `00aafecc` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00aafed0"></a> `00aafed0` | `48 01 00 b4` | cbz x8,0x00aafef8 | `CONDITIONAL_JUMP`
<a id="insn-00aafed4"></a> `00aafed4` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00aafed8"></a> `00aafed8` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aafedc"></a> `00aafedc` | `ff 02 08 6b` | cmp w23,w8 | `FALL_THROUGH`
<a id="insn-00aafee0"></a> `00aafee0` | `4b ff ff 54` | b.lt 0x00aafec8 | `CONDITIONAL_JUMP`
<a id="insn-00aafee4"></a> `00aafee4` | `1f 01 17 6b` | cmp w8,w23 | `FALL_THROUGH`
<a id="insn-00aafee8"></a> `00aafee8` | `4a 03 00 54` | b.ge 0x00aaff50 | `CONDITIONAL_JUMP`
<a id="insn-00aafeec"></a> `00aafeec` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00aafef0"></a> `00aafef0` | `28 ff ff b5` | cbnz x8,0x00aafed4 | `CONDITIONAL_JUMP`
<a id="insn-00aafef4"></a> `00aafef4` | `d9 22 00 91` | add x25,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aafef8"></a> `00aafef8` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00aafefc"></a> `00aafefc` | `3d ac 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaff00"></a> `00aaff00` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aaff04"></a> `00aaff04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aaff08"></a> `00aaff08` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aaff0c"></a> `00aaff0c` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aaff10"></a> `00aaff10` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00aaff14"></a> `00aaff14` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aaff18"></a> `00aaff18` | `17 1c 00 b9` | str w23,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00aaff1c"></a> `00aaff1c` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aaff20"></a> `00aaff20` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aaff24"></a> `00aaff24` | `68 00 00 b4` | cbz x8,0x00aaff30 | `CONDITIONAL_JUMP`
<a id="insn-00aaff28"></a> `00aaff28` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aaff2c"></a> `00aaff2c` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00aaff30"></a> `00aaff30` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aaff34"></a> `00aaff34` | `4c a4 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aaff38"></a> `00aaff38` | `88 1e 40 f9` | ldr x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00aaff3c"></a> `00aaff3c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aaff40"></a> `00aaff40` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00aaff44"></a> `00aaff44` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00aaff48"></a> `00aaff48` | `c8 f5 07 37` | tbnz w8,#0x0,0x00aafe00 | `CONDITIONAL_JUMP`
<a id="insn-00aaff4c"></a> `00aaff4c` | `04 00 00 14` | b 0x00aaff5c | `UNCONDITIONAL_JUMP`
<a id="insn-00aaff50"></a> `00aaff50` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00aaff54"></a> `00aaff54` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00aaff58"></a> `00aaff58` | `48 f5 07 37` | tbnz w8,#0x0,0x00aafe00 | `CONDITIONAL_JUMP`
<a id="insn-00aaff5c"></a> `00aaff5c` | `f9 a3 41 a9` | ldp x25,x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aaff60"></a> `00aaff60` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-00aaff64"></a> `00aaff64` | `a3 f4 ff 54` | b.cc 0x00aafdf8 | `CONDITIONAL_JUMP`
<a id="insn-00aaff68"></a> `00aaff68` | `f4 0b 40 f9` | ldr x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaff6c"></a> `00aaff6c` | `35 03 14 cb` | sub x21,x25,x20 | `FALL_THROUGH`
<a id="insn-00aaff70"></a> `00aaff70` | `b9 fe 42 93` | asr x25,x21,#0x2 | `FALL_THROUGH`
<a id="insn-00aaff74"></a> `00aaff74` | `29 07 00 91` | add x9,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00aaff78"></a> `00aaff78` | `2a fd 7e d3` | lsr x10,x9,#0x3e | `FALL_THROUGH`
<a id="insn-00aaff7c"></a> `00aaff7c` | `0a 6d 00 b5` | cbnz x10,0x00ab0d1c | `CONDITIONAL_JUMP`
<a id="insn-00aaff80"></a> `00aaff80` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00aaff84"></a> `00aaff84` | `0a fd 41 93` | asr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aaff88"></a> `00aaff88` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00aaff8c"></a> `00aaff8c` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00aaff90"></a> `00aaff90` | `ea f3 7e b2` | orr x10,xzr,#0x7ffffffffffffffc | `FALL_THROUGH`
<a id="insn-00aaff94"></a> `00aaff94` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00aaff98"></a> `00aaff98` | `08 00 f8 92` | mov x8,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-00aaff9c"></a> `00aaff9c` | `3a 31 88 9a` | csel x26,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00aaffa0"></a> `00aaffa0` | `fa 00 00 b4` | cbz x26,0x00aaffbc | `CONDITIONAL_JUMP`
<a id="insn-00aaffa4"></a> `00aaffa4` | `48 ff 7e d3` | lsr x8,x26,#0x3e | `FALL_THROUGH`
<a id="insn-00aaffa8"></a> `00aaffa8` | `88 6c 00 b5` | cbnz x8,0x00ab0d38 | `CONDITIONAL_JUMP`
<a id="insn-00aaffac"></a> `00aaffac` | `40 f7 7e d3` | lsl x0,x26,#0x2 | `FALL_THROUGH`
<a id="insn-00aaffb0"></a> `00aaffb0` | `10 ac 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaffb4"></a> `00aaffb4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aaffb8"></a> `00aaffb8` | `02 00 00 14` | b 0x00aaffc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaffbc"></a> `00aaffbc` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00aaffc0"></a> `00aaffc0` | `d9 0a 19 8b` | add x25,x22,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00aaffc4"></a> `00aaffc4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aaffc8"></a> `00aaffc8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00aaffcc"></a> `00aaffcc` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00aaffd0"></a> `00aaffd0` | `da 0a 1a 8b` | add x26,x22,x26, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00aaffd4"></a> `00aaffd4` | `37 47 00 b8` | str w23,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-00aaffd8"></a> `00aaffd8` | `62 ac 04 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00aaffdc"></a> `00aaffdc` | `f6 67 01 a9` | stp x22,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaffe0"></a> `00aaffe0` | `fa 13 00 f9` | str x26,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaffe4"></a> `00aaffe4` | `d4 f0 ff b4` | cbz x20,0x00aafdfc | `CONDITIONAL_JUMP`
<a id="insn-00aaffe8"></a> `00aaffe8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaffec"></a> `00aaffec` | `09 ac 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00aafff0"></a> `00aafff0` | `83 ff ff 17` | b 0x00aafdfc | `UNCONDITIONAL_JUMP`
<a id="insn-00aafff4"></a> `00aafff4` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00aafff8"></a> `00aafff8` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-00aafffc"></a> `00aafffc` | `e8 0e 43 f8` | ldr x8,[x23, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab0000"></a> `00ab0000` | `c8 00 00 b5` | cbnz x8,0x00ab0018 | `CONDITIONAL_JUMP`
<a id="insn-00ab0004"></a> `00ab0004` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00ab0008"></a> `00ab0008` | `0d 00 00 14` | b 0x00ab003c | `UNCONDITIONAL_JUMP`
<a id="insn-00ab000c"></a> `00ab000c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00ab0010"></a> `00ab0010` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00ab0014"></a> `00ab0014` | `48 01 00 b4` | cbz x8,0x00ab003c | `CONDITIONAL_JUMP`
<a id="insn-00ab0018"></a> `00ab0018` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00ab001c"></a> `00ab001c` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0020"></a> `00ab0020` | `1f c1 00 71` | cmp w8,#0x30 | `FALL_THROUGH`
<a id="insn-00ab0024"></a> `00ab0024` | `4a ff ff 54` | b.ge 0x00ab000c | `CONDITIONAL_JUMP`
<a id="insn-00ab0028"></a> `00ab0028` | `1f bd 00 71` | cmp w8,#0x2f | `FALL_THROUGH`
<a id="insn-00ab002c"></a> `00ab002c` | `60 03 00 54` | b.eq 0x00ab0098 | `CONDITIONAL_JUMP`
<a id="insn-00ab0030"></a> `00ab0030` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00ab0034"></a> `00ab0034` | `28 ff ff b5` | cbnz x8,0x00ab0018 | `CONDITIONAL_JUMP`
<a id="insn-00ab0038"></a> `00ab0038` | `d7 22 00 91` | add x23,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00ab003c"></a> `00ab003c` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00ab0040"></a> `00ab0040` | `ec ab 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0044"></a> `00ab0044` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab0048"></a> `00ab0048` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ab004c"></a> `00ab004c` | `e9 05 80 52` | mov w9,#0x2f | `FALL_THROUGH`
<a id="insn-00ab0050"></a> `00ab0050` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0054"></a> `00ab0054` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab0058"></a> `00ab0058` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-00ab005c"></a> `00ab005c` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0060"></a> `00ab0060` | `09 1c 00 b9` | str w9,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0064"></a> `00ab0064` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0068"></a> `00ab0068` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab006c"></a> `00ab006c` | `68 00 00 b4` | cbz x8,0x00ab0078 | `CONDITIONAL_JUMP`
<a id="insn-00ab0070"></a> `00ab0070` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0074"></a> `00ab0074` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00ab0078"></a> `00ab0078` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00ab007c"></a> `00ab007c` | `fa a3 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0080"></a> `00ab0080` | `88 1e 40 f9` | ldr x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0084"></a> `00ab0084` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0088"></a> `00ab0088` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00ab008c"></a> `00ab008c` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0090"></a> `00ab0090` | `a8 00 00 35` | cbnz w8,0x00ab00a4 | `CONDITIONAL_JUMP`
<a id="insn-00ab0094"></a> `00ab0094` | `57 ff ff 17` | b 0x00aafdf0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0098"></a> `00ab0098` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00ab009c"></a> `00ab009c` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ab00a0"></a> `00ab00a0` | `88 ea ff 34` | cbz w8,0x00aafdf0 | `CONDITIONAL_JUMP`
<a id="insn-00ab00a4"></a> `00ab00a4` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00ab00a8"></a> `00ab00a8` | `0b 00 00 14` | b 0x00ab00d4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab00ac"></a> `00ab00ac` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00ab00b0"></a> `00ab00b0` | `ed a3 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab00b4"></a> `00ab00b4` | `88 1e 40 f9` | ldr x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00ab00b8"></a> `00ab00b8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab00bc"></a> `00ab00bc` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00ab00c0"></a> `00ab00c0` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ab00c4"></a> `00ab00c4` | `28 0a 00 36` | tbz w8,#0x0,0x00ab0208 | `CONDITIONAL_JUMP`
<a id="insn-00ab00c8"></a> `00ab00c8` | `f7 06 00 11` | add w23,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00ab00cc"></a> `00ab00cc` | `ff be 00 71` | cmp w23,#0x2f | `FALL_THROUGH`
<a id="insn-00ab00d0"></a> `00ab00d0` | `c0 0e 00 54` | b.eq 0x00ab02a8 | `CONDITIONAL_JUMP`
<a id="insn-00ab00d4"></a> `00ab00d4` | `2b bd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab00d8"></a> `00ab00d8` | `15 d0 4c 91` | add x21,x0,#0x334, LSL #12 | `FALL_THROUGH`
<a id="insn-00ab00dc"></a> `00ab00dc` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00ab00e0"></a> `00ab00e0` | `28 8f 43 f8` | ldr x8,[x25, #0x38]! | `FALL_THROUGH`
<a id="insn-00ab00e4"></a> `00ab00e4` | `c8 00 00 b5` | cbnz x8,0x00ab00fc | `CONDITIONAL_JUMP`
<a id="insn-00ab00e8"></a> `00ab00e8` | `f6 03 19 aa` | mov x22,x25 | `FALL_THROUGH`
<a id="insn-00ab00ec"></a> `00ab00ec` | `0c 00 00 14` | b 0x00ab011c | `UNCONDITIONAL_JUMP`
<a id="insn-00ab00f0"></a> `00ab00f0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00ab00f4"></a> `00ab00f4` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00ab00f8"></a> `00ab00f8` | `28 01 00 b4` | cbz x8,0x00ab011c | `CONDITIONAL_JUMP`
<a id="insn-00ab00fc"></a> `00ab00fc` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00ab0100"></a> `00ab0100` | `08 21 80 b9` | ldrsw x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0104"></a> `00ab0104` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00ab0108"></a> `00ab0108` | `4b ff ff 54` | b.lt 0x00ab00f0 | `CONDITIONAL_JUMP`
<a id="insn-00ab010c"></a> `00ab010c` | `6d 03 00 54` | b.le 0x00ab0178 | `CONDITIONAL_JUMP`
<a id="insn-00ab0110"></a> `00ab0110` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00ab0114"></a> `00ab0114` | `48 ff ff b5` | cbnz x8,0x00ab00fc | `CONDITIONAL_JUMP`
<a id="insn-00ab0118"></a> `00ab0118` | `d9 22 00 91` | add x25,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00ab011c"></a> `00ab011c` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00ab0120"></a> `00ab0120` | `b4 ab 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0124"></a> `00ab0124` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ab0128"></a> `00ab0128` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00ab012c"></a> `00ab012c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ab0130"></a> `00ab0130` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab0134"></a> `00ab0134` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab0138"></a> `00ab0138` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00ab013c"></a> `00ab013c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab0140"></a> `00ab0140` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0144"></a> `00ab0144` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00ab0148"></a> `00ab0148` | `a8 1a 40 f9` | ldr x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00ab014c"></a> `00ab014c` | `13 20 00 b9` | str w19,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0150"></a> `00ab0150` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab0154"></a> `00ab0154` | `68 00 00 b4` | cbz x8,0x00ab0160 | `CONDITIONAL_JUMP`
<a id="insn-00ab0158"></a> `00ab0158` | `a8 1a 00 f9` | str x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00ab015c"></a> `00ab015c` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00ab0160"></a> `00ab0160` | `a0 1e 40 f9` | ldr x0,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0164"></a> `00ab0164` | `c0 a3 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0168"></a> `00ab0168` | `a8 22 40 f9` | ldr x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00ab016c"></a> `00ab016c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0170"></a> `00ab0170` | `a8 22 00 f9` | str x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00ab0174"></a> `00ab0174` | `02 00 00 14` | b 0x00ab017c | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0178"></a> `00ab0178` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00ab017c"></a> `00ab017c` | `f9 03 14 aa` | mov x25,x20 | `FALL_THROUGH`
<a id="insn-00ab0180"></a> `00ab0180` | `28 0f 43 f8` | ldr x8,[x25, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab0184"></a> `00ab0184` | `c8 00 00 b5` | cbnz x8,0x00ab019c | `CONDITIONAL_JUMP`
<a id="insn-00ab0188"></a> `00ab0188` | `f6 03 19 aa` | mov x22,x25 | `FALL_THROUGH`
<a id="insn-00ab018c"></a> `00ab018c` | `0d 00 00 14` | b 0x00ab01c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0190"></a> `00ab0190` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00ab0194"></a> `00ab0194` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00ab0198"></a> `00ab0198` | `48 01 00 b4` | cbz x8,0x00ab01c0 | `CONDITIONAL_JUMP`
<a id="insn-00ab019c"></a> `00ab019c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00ab01a0"></a> `00ab01a0` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab01a4"></a> `00ab01a4` | `ff 02 08 6b` | cmp w23,w8 | `FALL_THROUGH`
<a id="insn-00ab01a8"></a> `00ab01a8` | `4b ff ff 54` | b.lt 0x00ab0190 | `CONDITIONAL_JUMP`
<a id="insn-00ab01ac"></a> `00ab01ac` | `1f 01 17 6b` | cmp w8,w23 | `FALL_THROUGH`
<a id="insn-00ab01b0"></a> `00ab01b0` | `6a 02 00 54` | b.ge 0x00ab01fc | `CONDITIONAL_JUMP`
<a id="insn-00ab01b4"></a> `00ab01b4` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00ab01b8"></a> `00ab01b8` | `28 ff ff b5` | cbnz x8,0x00ab019c | `CONDITIONAL_JUMP`
<a id="insn-00ab01bc"></a> `00ab01bc` | `d9 22 00 91` | add x25,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00ab01c0"></a> `00ab01c0` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00ab01c4"></a> `00ab01c4` | `8b ab 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab01c8"></a> `00ab01c8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab01cc"></a> `00ab01cc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ab01d0"></a> `00ab01d0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab01d4"></a> `00ab01d4` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab01d8"></a> `00ab01d8` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00ab01dc"></a> `00ab01dc` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ab01e0"></a> `00ab01e0` | `17 1c 00 b9` | str w23,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab01e4"></a> `00ab01e4` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab01e8"></a> `00ab01e8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab01ec"></a> `00ab01ec` | `08 f6 ff b4` | cbz x8,0x00ab00ac | `CONDITIONAL_JUMP`
<a id="insn-00ab01f0"></a> `00ab01f0` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ab01f4"></a> `00ab01f4` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00ab01f8"></a> `00ab01f8` | `ad ff ff 17` | b 0x00ab00ac | `UNCONDITIONAL_JUMP`
<a id="insn-00ab01fc"></a> `00ab01fc` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00ab0200"></a> `00ab0200` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0204"></a> `00ab0204` | `28 f6 07 37` | tbnz w8,#0x0,0x00ab00c8 | `CONDITIONAL_JUMP`
<a id="insn-00ab0208"></a> `00ab0208` | `f9 a3 41 a9` | ldp x25,x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ab020c"></a> `00ab020c` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-00ab0210"></a> `00ab0210` | `62 00 00 54` | b.cs 0x00ab021c | `CONDITIONAL_JUMP`
<a id="insn-00ab0214"></a> `00ab0214` | `37 47 00 b8` | str w23,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-00ab0218"></a> `00ab0218` | `23 00 00 14` | b 0x00ab02a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab021c"></a> `00ab021c` | `f4 0b 40 f9` | ldr x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0220"></a> `00ab0220` | `35 03 14 cb` | sub x21,x25,x20 | `FALL_THROUGH`
<a id="insn-00ab0224"></a> `00ab0224` | `b9 fe 42 93` | asr x25,x21,#0x2 | `FALL_THROUGH`
<a id="insn-00ab0228"></a> `00ab0228` | `29 07 00 91` | add x9,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00ab022c"></a> `00ab022c` | `2a fd 7e d3` | lsr x10,x9,#0x3e | `FALL_THROUGH`
<a id="insn-00ab0230"></a> `00ab0230` | `0a 5a 00 b5` | cbnz x10,0x00ab0d70 | `CONDITIONAL_JUMP`
<a id="insn-00ab0234"></a> `00ab0234` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00ab0238"></a> `00ab0238` | `0a fd 41 93` | asr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab023c"></a> `00ab023c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00ab0240"></a> `00ab0240` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00ab0244"></a> `00ab0244` | `ea f3 7e b2` | orr x10,xzr,#0x7ffffffffffffffc | `FALL_THROUGH`
<a id="insn-00ab0248"></a> `00ab0248` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00ab024c"></a> `00ab024c` | `08 00 f8 92` | mov x8,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-00ab0250"></a> `00ab0250` | `3a 31 88 9a` | csel x26,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00ab0254"></a> `00ab0254` | `fa 00 00 b4` | cbz x26,0x00ab0270 | `CONDITIONAL_JUMP`
<a id="insn-00ab0258"></a> `00ab0258` | `48 ff 7e d3` | lsr x8,x26,#0x3e | `FALL_THROUGH`
<a id="insn-00ab025c"></a> `00ab025c` | `88 59 00 b5` | cbnz x8,0x00ab0d8c | `CONDITIONAL_JUMP`
<a id="insn-00ab0260"></a> `00ab0260` | `40 f7 7e d3` | lsl x0,x26,#0x2 | `FALL_THROUGH`
<a id="insn-00ab0264"></a> `00ab0264` | `63 ab 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0268"></a> `00ab0268` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ab026c"></a> `00ab026c` | `02 00 00 14` | b 0x00ab0274 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0270"></a> `00ab0270` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00ab0274"></a> `00ab0274` | `d9 0a 19 8b` | add x25,x22,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ab0278"></a> `00ab0278` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ab027c"></a> `00ab027c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ab0280"></a> `00ab0280` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00ab0284"></a> `00ab0284` | `da 0a 1a 8b` | add x26,x22,x26, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ab0288"></a> `00ab0288` | `37 47 00 b8` | str w23,[x25], #0x4 | `FALL_THROUGH`
<a id="insn-00ab028c"></a> `00ab028c` | `b5 ab 04 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0290"></a> `00ab0290` | `f6 67 01 a9` | stp x22,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0294"></a> `00ab0294` | `fa 13 00 f9` | str x26,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0298"></a> `00ab0298` | `74 00 00 b4` | cbz x20,0x00ab02a4 | `CONDITIONAL_JUMP`
<a id="insn-00ab029c"></a> `00ab029c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ab02a0"></a> `00ab02a0` | `5c ab 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00ab02a4"></a> `00ab02a4` | `f9 0f 00 f9` | str x25,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ab02a8"></a> `00ab02a8` | `e9 23 43 a9` | ldp x9,x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ab02ac"></a> `00ab02ac` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab02b0"></a> `00ab02b0` | `00 55 00 54` | b.eq 0x00ab0d50 | `CONDITIONAL_JUMP`
<a id="insn-00ab02b4"></a> `00ab02b4` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00ab02b8"></a> `00ab02b8` | `1f 03 0a 6b` | cmp w24,w10 | `FALL_THROUGH`
<a id="insn-00ab02bc"></a> `00ab02bc` | `6a 00 00 54` | b.ge 0x00ab02c8 | `CONDITIONAL_JUMP`
<a id="insn-00ab02c0"></a> `00ab02c0` | `28 05 40 b9` | ldr w8,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00ab02c4"></a> `00ab02c4` | `0b 00 00 14` | b 0x00ab02f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab02c8"></a> `00ab02c8` | `2a 41 00 91` | add x10,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00ab02cc"></a> `00ab02cc` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-00ab02d0"></a> `00ab02d0` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00ab02d4"></a> `00ab02d4` | `a0 00 00 54` | b.eq 0x00ab02e8 | `CONDITIONAL_JUMP`
<a id="insn-00ab02d8"></a> `00ab02d8` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-00ab02dc"></a> `00ab02dc` | `4b 05 41 b8` | ldr w11,[x10], #0x10 | `FALL_THROUGH`
<a id="insn-00ab02e0"></a> `00ab02e0` | `7f 01 18 6b` | cmp w11,w24 | `FALL_THROUGH`
<a id="insn-00ab02e4"></a> `00ab02e4` | `4d ff ff 54` | b.le 0x00ab02cc | `CONDITIONAL_JUMP`
<a id="insn-00ab02e8"></a> `00ab02e8` | `28 41 5f b8` | ldur w8,[x9, #-0xc] | `FALL_THROUGH`
<a id="insn-00ab02ec"></a> `00ab02ec` | `29 41 00 d1` | sub x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-00ab02f0"></a> `00ab02f0` | `e8 0f 00 b9` | str w8,[sp, #0xc] | `FALL_THROUGH`
<a id="insn-00ab02f4"></a> `00ab02f4` | `ea 23 41 a9` | ldp x10,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab02f8"></a> `00ab02f8` | `37 05 40 f9` | ldr x23,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00ab02fc"></a> `00ab02fc` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00ab0300"></a> `00ab0300` | `20 1b 00 54` | b.eq 0x00ab0664 | `CONDITIONAL_JUMP`
<a id="insn-00ab0304"></a> `00ab0304` | `ff 06 00 71` | cmp w23,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0308"></a> `00ab0308` | `0b 20 00 54` | b.lt 0x00ab0708 | `CONDITIONAL_JUMP`
<a id="insn-00ab030c"></a> `00ab030c` | `fc 03 1f 2a` | mov w28,wzr | `FALL_THROUGH`
<a id="insn-00ab0310"></a> `00ab0310` | `f9 03 1f 2a` | mov w25,wzr | `FALL_THROUGH`
<a id="insn-00ab0314"></a> `00ab0314` | `09 00 00 14` | b 0x00ab0338 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0318"></a> `00ab0318` | `89 02 15 8b` | add x9,x20,x21 | `FALL_THROUGH`
<a id="insn-00ab031c"></a> `00ab031c` | `9c 07 00 11` | add w28,w28,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0320"></a> `00ab0320` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab0324"></a> `00ab0324` | `e9 0f 00 f9` | str x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ab0328"></a> `00ab0328` | `20 1f 00 54` | b.eq 0x00ab070c | `CONDITIONAL_JUMP`
<a id="insn-00ab032c"></a> `00ab032c` | `39 07 00 11` | add w25,w25,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0330"></a> `00ab0330` | `3f 03 17 6b` | cmp w25,w23 | `FALL_THROUGH`
<a id="insn-00ab0334"></a> `00ab0334` | `c0 1e 00 54` | b.eq 0x00ab070c | `CONDITIONAL_JUMP`
<a id="insn-00ab0338"></a> `00ab0338` | `80 0c 80 52` | mov w0,#0x64 | `FALL_THROUGH`
<a id="insn-00ab033c"></a> `00ab033c` | `67 69 e6 97` | bl 0x0044a8d8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0340"></a> `00ab0340` | `e8 0f 40 b9` | ldr w8,[sp, #0xc] | `FALL_THROUGH`
<a id="insn-00ab0344"></a> `00ab0344` | `1f 00 08 6b` | cmp w0,w8 | `FALL_THROUGH`
<a id="insn-00ab0348"></a> `00ab0348` | `2a ff ff 54` | b.ge 0x00ab032c | `CONDITIONAL_JUMP`
<a id="insn-00ab034c"></a> `00ab034c` | `e9 23 41 a9` | ldp x9,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0350"></a> `00ab0350` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00ab0354"></a> `00ab0354` | `00 fd 42 d3` | lsr x0,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ab0358"></a> `00ab0358` | `60 69 e6 97` | bl 0x0044a8d8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab035c"></a> `00ab035c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0360"></a> `00ab0360` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00ab0364"></a> `00ab0364` | `1a d9 60 b8` | ldr w26,[x8, w0, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00ab0368"></a> `00ab0368` | `86 bc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab036c"></a> `00ab036c` | `18 d0 4c 91` | add x24,x0,#0x334, LSL #12 | `FALL_THROUGH`
<a id="insn-00ab0370"></a> `00ab0370` | `f6 03 18 aa` | mov x22,x24 | `FALL_THROUGH`
<a id="insn-00ab0374"></a> `00ab0374` | `c8 8e 43 f8` | ldr x8,[x22, #0x38]! | `FALL_THROUGH`
<a id="insn-00ab0378"></a> `00ab0378` | `c8 00 00 b5` | cbnz x8,0x00ab0390 | `CONDITIONAL_JUMP`
<a id="insn-00ab037c"></a> `00ab037c` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00ab0380"></a> `00ab0380` | `0c 00 00 14` | b 0x00ab03b0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0384"></a> `00ab0384` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00ab0388"></a> `00ab0388` | `f6 03 15 aa` | mov x22,x21 | `FALL_THROUGH`
<a id="insn-00ab038c"></a> `00ab038c` | `28 01 00 b4` | cbz x8,0x00ab03b0 | `CONDITIONAL_JUMP`
<a id="insn-00ab0390"></a> `00ab0390` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00ab0394"></a> `00ab0394` | `08 21 80 b9` | ldrsw x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0398"></a> `00ab0398` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00ab039c"></a> `00ab039c` | `4b ff ff 54` | b.lt 0x00ab0384 | `CONDITIONAL_JUMP`
<a id="insn-00ab03a0"></a> `00ab03a0` | `6d 03 00 54` | b.le 0x00ab040c | `CONDITIONAL_JUMP`
<a id="insn-00ab03a4"></a> `00ab03a4` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00ab03a8"></a> `00ab03a8` | `48 ff ff b5` | cbnz x8,0x00ab0390 | `CONDITIONAL_JUMP`
<a id="insn-00ab03ac"></a> `00ab03ac` | `b6 22 00 91` | add x22,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00ab03b0"></a> `00ab03b0` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00ab03b4"></a> `00ab03b4` | `0f ab 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab03b8"></a> `00ab03b8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ab03bc"></a> `00ab03bc` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00ab03c0"></a> `00ab03c0` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00ab03c4"></a> `00ab03c4` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab03c8"></a> `00ab03c8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab03cc"></a> `00ab03cc` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00ab03d0"></a> `00ab03d0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab03d4"></a> `00ab03d4` | `15 08 00 f9` | str x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab03d8"></a> `00ab03d8` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00ab03dc"></a> `00ab03dc` | `08 1b 40 f9` | ldr x8,[x24, #0x30] | `FALL_THROUGH`
<a id="insn-00ab03e0"></a> `00ab03e0` | `13 20 00 b9` | str w19,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab03e4"></a> `00ab03e4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab03e8"></a> `00ab03e8` | `68 00 00 b4` | cbz x8,0x00ab03f4 | `CONDITIONAL_JUMP`
<a id="insn-00ab03ec"></a> `00ab03ec` | `08 1b 00 f9` | str x8,[x24, #0x30] | `FALL_THROUGH`
<a id="insn-00ab03f0"></a> `00ab03f0` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00ab03f4"></a> `00ab03f4` | `00 1f 40 f9` | ldr x0,[x24, #0x38] | `FALL_THROUGH`
<a id="insn-00ab03f8"></a> `00ab03f8` | `1b a3 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab03fc"></a> `00ab03fc` | `08 23 40 f9` | ldr x8,[x24, #0x40] | `FALL_THROUGH`
<a id="insn-00ab0400"></a> `00ab0400` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0404"></a> `00ab0404` | `08 23 00 f9` | str x8,[x24, #0x40] | `FALL_THROUGH`
<a id="insn-00ab0408"></a> `00ab0408` | `02 00 00 14` | b 0x00ab0410 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab040c"></a> `00ab040c` | `fb 03 15 aa` | mov x27,x21 | `FALL_THROUGH`
<a id="insn-00ab0410"></a> `00ab0410` | `f8 03 1b aa` | mov x24,x27 | `FALL_THROUGH`
<a id="insn-00ab0414"></a> `00ab0414` | `08 0f 43 f8` | ldr x8,[x24, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab0418"></a> `00ab0418` | `c8 00 00 b5` | cbnz x8,0x00ab0430 | `CONDITIONAL_JUMP`
<a id="insn-00ab041c"></a> `00ab041c` | `f5 03 18 aa` | mov x21,x24 | `FALL_THROUGH`
<a id="insn-00ab0420"></a> `00ab0420` | `0d 00 00 14` | b 0x00ab0454 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0424"></a> `00ab0424` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00ab0428"></a> `00ab0428` | `f8 03 15 aa` | mov x24,x21 | `FALL_THROUGH`
<a id="insn-00ab042c"></a> `00ab042c` | `48 01 00 b4` | cbz x8,0x00ab0454 | `CONDITIONAL_JUMP`
<a id="insn-00ab0430"></a> `00ab0430` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00ab0434"></a> `00ab0434` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0438"></a> `00ab0438` | `5f 03 08 6b` | cmp w26,w8 | `FALL_THROUGH`
<a id="insn-00ab043c"></a> `00ab043c` | `4b ff ff 54` | b.lt 0x00ab0424 | `CONDITIONAL_JUMP`
<a id="insn-00ab0440"></a> `00ab0440` | `1f 01 1a 6b` | cmp w8,w26 | `FALL_THROUGH`
<a id="insn-00ab0444"></a> `00ab0444` | `4a 03 00 54` | b.ge 0x00ab04ac | `CONDITIONAL_JUMP`
<a id="insn-00ab0448"></a> `00ab0448` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00ab044c"></a> `00ab044c` | `28 ff ff b5` | cbnz x8,0x00ab0430 | `CONDITIONAL_JUMP`
<a id="insn-00ab0450"></a> `00ab0450` | `b8 22 00 91` | add x24,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00ab0454"></a> `00ab0454` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00ab0458"></a> `00ab0458` | `e6 aa 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab045c"></a> `00ab045c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab0460"></a> `00ab0460` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ab0464"></a> `00ab0464` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab0468"></a> `00ab0468` | `15 08 00 f9` | str x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab046c"></a> `00ab046c` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00ab0470"></a> `00ab0470` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0474"></a> `00ab0474` | `1a 1c 00 b9` | str w26,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0478"></a> `00ab0478` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab047c"></a> `00ab047c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab0480"></a> `00ab0480` | `68 00 00 b4` | cbz x8,0x00ab048c | `CONDITIONAL_JUMP`
<a id="insn-00ab0484"></a> `00ab0484` | `68 17 00 f9` | str x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0488"></a> `00ab0488` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00ab048c"></a> `00ab048c` | `60 1b 40 f9` | ldr x0,[x27, #0x30] | `FALL_THROUGH`
<a id="insn-00ab0490"></a> `00ab0490` | `f5 a2 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0494"></a> `00ab0494` | `68 1f 40 f9` | ldr x8,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0498"></a> `00ab0498` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab049c"></a> `00ab049c` | `68 1f 00 f9` | str x8,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-00ab04a0"></a> `00ab04a0` | `c8 82 40 39` | ldrb w8,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00ab04a4"></a> `00ab04a4` | `48 f4 07 37` | tbnz w8,#0x0,0x00ab032c | `CONDITIONAL_JUMP`
<a id="insn-00ab04a8"></a> `00ab04a8` | `04 00 00 14` | b 0x00ab04b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab04ac"></a> `00ab04ac` | `f6 03 15 aa` | mov x22,x21 | `FALL_THROUGH`
<a id="insn-00ab04b0"></a> `00ab04b0` | `c8 82 40 39` | ldrb w8,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00ab04b4"></a> `00ab04b4` | `c8 f3 07 37` | tbnz w8,#0x0,0x00ab032c | `CONDITIONAL_JUMP`
<a id="insn-00ab04b8"></a> `00ab04b8` | `32 bc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab04bc"></a> `00ab04bc` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00ab04c0"></a> `00ab04c0` | `0f f0 f3 97` | bl 0x007ac4fc | `UNCONDITIONAL_CALL`
<a id="insn-00ab04c4"></a> `00ab04c4` | `60 01 00 36` | tbz w0,#0x0,0x00ab04f0 | `CONDITIONAL_JUMP`
<a id="insn-00ab04c8"></a> `00ab04c8` | `2e bc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab04cc"></a> `00ab04cc` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00ab04d0"></a> `00ab04d0` | `29 f0 f3 97` | bl 0x007ac574 | `UNCONDITIONAL_CALL`
<a id="insn-00ab04d4"></a> `00ab04d4` | `e0 00 00 36` | tbz w0,#0x0,0x00ab04f0 | `CONDITIONAL_JUMP`
<a id="insn-00ab04d8"></a> `00ab04d8` | `2a bc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab04dc"></a> `00ab04dc` | `08 0b 88 52` | mov w8,#0x4058 | `FALL_THROUGH`
<a id="insn-00ab04e0"></a> `00ab04e0` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab04e4"></a> `00ab04e4` | `08 68 e8 38` | ldrsb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ab04e8"></a> `00ab04e8` | `5f 03 08 6b` | cmp w26,w8 | `FALL_THROUGH`
<a id="insn-00ab04ec"></a> `00ab04ec` | `00 f2 ff 54` | b.eq 0x00ab032c | `CONDITIONAL_JUMP`
<a id="insn-00ab04f0"></a> `00ab04f0` | `24 bc f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab04f4"></a> `00ab04f4` | `16 d0 4c 91` | add x22,x0,#0x334, LSL #12 | `FALL_THROUGH`
<a id="insn-00ab04f8"></a> `00ab04f8` | `f8 03 16 aa` | mov x24,x22 | `FALL_THROUGH`
<a id="insn-00ab04fc"></a> `00ab04fc` | `08 0f 42 f8` | ldr x8,[x24, #0x20]! | `FALL_THROUGH`
<a id="insn-00ab0500"></a> `00ab0500` | `c8 00 00 b5` | cbnz x8,0x00ab0518 | `CONDITIONAL_JUMP`
<a id="insn-00ab0504"></a> `00ab0504` | `fb 03 18 aa` | mov x27,x24 | `FALL_THROUGH`
<a id="insn-00ab0508"></a> `00ab0508` | `0c 00 00 14` | b 0x00ab0538 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab050c"></a> `00ab050c` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00ab0510"></a> `00ab0510` | `f8 03 1b aa` | mov x24,x27 | `FALL_THROUGH`
<a id="insn-00ab0514"></a> `00ab0514` | `28 01 00 b4` | cbz x8,0x00ab0538 | `CONDITIONAL_JUMP`
<a id="insn-00ab0518"></a> `00ab0518` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00ab051c"></a> `00ab051c` | `08 21 80 b9` | ldrsw x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0520"></a> `00ab0520` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00ab0524"></a> `00ab0524` | `4b ff ff 54` | b.lt 0x00ab050c | `CONDITIONAL_JUMP`
<a id="insn-00ab0528"></a> `00ab0528` | `6d 03 00 54` | b.le 0x00ab0594 | `CONDITIONAL_JUMP`
<a id="insn-00ab052c"></a> `00ab052c` | `68 07 40 f9` | ldr x8,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00ab0530"></a> `00ab0530` | `48 ff ff b5` | cbnz x8,0x00ab0518 | `CONDITIONAL_JUMP`
<a id="insn-00ab0534"></a> `00ab0534` | `78 23 00 91` | add x24,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00ab0538"></a> `00ab0538` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00ab053c"></a> `00ab053c` | `ad aa 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0540"></a> `00ab0540` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ab0544"></a> `00ab0544` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0548"></a> `00ab0548` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ab054c"></a> `00ab054c` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab0550"></a> `00ab0550` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab0554"></a> `00ab0554` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0558"></a> `00ab0558` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab055c"></a> `00ab055c` | `1b 08 00 f9` | str x27,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0560"></a> `00ab0560` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00ab0564"></a> `00ab0564` | `c8 0e 40 f9` | ldr x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00ab0568"></a> `00ab0568` | `13 20 00 b9` | str w19,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab056c"></a> `00ab056c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab0570"></a> `00ab0570` | `68 00 00 b4` | cbz x8,0x00ab057c | `CONDITIONAL_JUMP`
<a id="insn-00ab0574"></a> `00ab0574` | `c8 0e 00 f9` | str x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00ab0578"></a> `00ab0578` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00ab057c"></a> `00ab057c` | `c0 12 40 f9` | ldr x0,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0580"></a> `00ab0580` | `b9 a2 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0584"></a> `00ab0584` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0588"></a> `00ab0588` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab058c"></a> `00ab058c` | `c8 16 00 f9` | str x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0590"></a> `00ab0590` | `02 00 00 14` | b 0x00ab0598 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0594"></a> `00ab0594` | `f5 03 1b aa` | mov x21,x27 | `FALL_THROUGH`
<a id="insn-00ab0598"></a> `00ab0598` | `f8 03 15 aa` | mov x24,x21 | `FALL_THROUGH`
<a id="insn-00ab059c"></a> `00ab059c` | `08 0f 43 f8` | ldr x8,[x24, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab05a0"></a> `00ab05a0` | `c8 00 00 b5` | cbnz x8,0x00ab05b8 | `CONDITIONAL_JUMP`
<a id="insn-00ab05a4"></a> `00ab05a4` | `fb 03 18 aa` | mov x27,x24 | `FALL_THROUGH`
<a id="insn-00ab05a8"></a> `00ab05a8` | `0d 00 00 14` | b 0x00ab05dc | `UNCONDITIONAL_JUMP`
<a id="insn-00ab05ac"></a> `00ab05ac` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00ab05b0"></a> `00ab05b0` | `f8 03 1b aa` | mov x24,x27 | `FALL_THROUGH`
<a id="insn-00ab05b4"></a> `00ab05b4` | `48 01 00 b4` | cbz x8,0x00ab05dc | `CONDITIONAL_JUMP`
<a id="insn-00ab05b8"></a> `00ab05b8` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00ab05bc"></a> `00ab05bc` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab05c0"></a> `00ab05c0` | `5f 03 08 6b` | cmp w26,w8 | `FALL_THROUGH`
<a id="insn-00ab05c4"></a> `00ab05c4` | `4b ff ff 54` | b.lt 0x00ab05ac | `CONDITIONAL_JUMP`
<a id="insn-00ab05c8"></a> `00ab05c8` | `1f 01 1a 6b` | cmp w8,w26 | `FALL_THROUGH`
<a id="insn-00ab05cc"></a> `00ab05cc` | `0a 03 00 54` | b.ge 0x00ab062c | `CONDITIONAL_JUMP`
<a id="insn-00ab05d0"></a> `00ab05d0` | `68 07 40 f9` | ldr x8,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00ab05d4"></a> `00ab05d4` | `28 ff ff b5` | cbnz x8,0x00ab05b8 | `CONDITIONAL_JUMP`
<a id="insn-00ab05d8"></a> `00ab05d8` | `78 23 00 91` | add x24,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00ab05dc"></a> `00ab05dc` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00ab05e0"></a> `00ab05e0` | `84 aa 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab05e4"></a> `00ab05e4` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab05e8"></a> `00ab05e8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ab05ec"></a> `00ab05ec` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab05f0"></a> `00ab05f0` | `1b 08 00 f9` | str x27,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab05f4"></a> `00ab05f4` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00ab05f8"></a> `00ab05f8` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00ab05fc"></a> `00ab05fc` | `1a 1c 00 b9` | str w26,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0600"></a> `00ab0600` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0604"></a> `00ab0604` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab0608"></a> `00ab0608` | `68 00 00 b4` | cbz x8,0x00ab0614 | `CONDITIONAL_JUMP`
<a id="insn-00ab060c"></a> `00ab060c` | `a8 16 00 f9` | str x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0610"></a> `00ab0610` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00ab0614"></a> `00ab0614` | `a0 1a 40 f9` | ldr x0,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00ab0618"></a> `00ab0618` | `93 a2 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab061c"></a> `00ab061c` | `a8 1e 40 f9` | ldr x8,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0620"></a> `00ab0620` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0624"></a> `00ab0624` | `a8 1e 00 f9` | str x8,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0628"></a> `00ab0628` | `02 00 00 14` | b 0x00ab0630 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab062c"></a> `00ab062c` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00ab0630"></a> `00ab0630` | `e8 2b 41 a9` | ldp x8,x10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0634"></a> `00ab0634` | `89 7e 40 93` | sxtw x9,w20 | `FALL_THROUGH`
<a id="insn-00ab0638"></a> `00ab0638` | `14 09 09 8b` | add x20,x8,x9, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ab063c"></a> `00ab063c` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0640"></a> `00ab0640` | `c9 82 00 39` | strb w9,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0644"></a> `00ab0644` | `81 12 00 91` | add x1,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00ab0648"></a> `00ab0648` | `55 01 01 eb` | subs x21,x10,x1 | `FALL_THROUGH`
<a id="insn-00ab064c"></a> `00ab064c` | `60 e6 ff 54` | b.eq 0x00ab0318 | `CONDITIONAL_JUMP`
<a id="insn-00ab0650"></a> `00ab0650` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ab0654"></a> `00ab0654` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00ab0658"></a> `00ab0658` | `92 aa 04 94` | bl 0x00bdb0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab065c"></a> `00ab065c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0660"></a> `00ab0660` | `2e ff ff 17` | b 0x00ab0318 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0664"></a> `00ab0664` | `c7 bb f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0668"></a> `00ab0668` | `15 d0 4c 91` | add x21,x0,#0x334, LSL #12 | `FALL_THROUGH`
<a id="insn-00ab066c"></a> `00ab066c` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00ab0670"></a> `00ab0670` | `28 8f 43 f8` | ldr x8,[x25, #0x38]! | `FALL_THROUGH`
<a id="insn-00ab0674"></a> `00ab0674` | `c8 00 00 b5` | cbnz x8,0x00ab068c | `CONDITIONAL_JUMP`
<a id="insn-00ab0678"></a> `00ab0678` | `f6 03 19 aa` | mov x22,x25 | `FALL_THROUGH`
<a id="insn-00ab067c"></a> `00ab067c` | `0c 00 00 14` | b 0x00ab06ac | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0680"></a> `00ab0680` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00ab0684"></a> `00ab0684` | `f9 03 16 aa` | mov x25,x22 | `FALL_THROUGH`
<a id="insn-00ab0688"></a> `00ab0688` | `28 01 00 b4` | cbz x8,0x00ab06ac | `CONDITIONAL_JUMP`
<a id="insn-00ab068c"></a> `00ab068c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00ab0690"></a> `00ab0690` | `08 21 80 b9` | ldrsw x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0694"></a> `00ab0694` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00ab0698"></a> `00ab0698` | `4b ff ff 54` | b.lt 0x00ab0680 | `CONDITIONAL_JUMP`
<a id="insn-00ab069c"></a> `00ab069c` | `8d 1e 00 54` | b.le 0x00ab0a6c | `CONDITIONAL_JUMP`
<a id="insn-00ab06a0"></a> `00ab06a0` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00ab06a4"></a> `00ab06a4` | `48 ff ff b5` | cbnz x8,0x00ab068c | `CONDITIONAL_JUMP`
<a id="insn-00ab06a8"></a> `00ab06a8` | `d9 22 00 91` | add x25,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00ab06ac"></a> `00ab06ac` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00ab06b0"></a> `00ab06b0` | `50 aa 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab06b4"></a> `00ab06b4` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ab06b8"></a> `00ab06b8` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00ab06bc"></a> `00ab06bc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ab06c0"></a> `00ab06c0` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab06c4"></a> `00ab06c4` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab06c8"></a> `00ab06c8` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00ab06cc"></a> `00ab06cc` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab06d0"></a> `00ab06d0` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab06d4"></a> `00ab06d4` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00ab06d8"></a> `00ab06d8` | `a8 1a 40 f9` | ldr x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00ab06dc"></a> `00ab06dc` | `13 20 00 b9` | str w19,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab06e0"></a> `00ab06e0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab06e4"></a> `00ab06e4` | `68 00 00 b4` | cbz x8,0x00ab06f0 | `CONDITIONAL_JUMP`
<a id="insn-00ab06e8"></a> `00ab06e8` | `a8 1a 00 f9` | str x8,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00ab06ec"></a> `00ab06ec` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00ab06f0"></a> `00ab06f0` | `a0 1e 40 f9` | ldr x0,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00ab06f4"></a> `00ab06f4` | `5c a2 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab06f8"></a> `00ab06f8` | `a8 22 40 f9` | ldr x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00ab06fc"></a> `00ab06fc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0700"></a> `00ab0700` | `a8 22 00 f9` | str x8,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00ab0704"></a> `00ab0704` | `db 00 00 14` | b 0x00ab0a70 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0708"></a> `00ab0708` | `fc 03 1f 2a` | mov w28,wzr | `FALL_THROUGH`
<a id="insn-00ab070c"></a> `00ab070c` | `e8 fe 60 d3` | lsr x8,x23,#0x20 | `FALL_THROUGH`
<a id="insn-00ab0710"></a> `00ab0710` | `17 01 1c 6b` | subs w23,w8,w28 | `FALL_THROUGH`
<a id="insn-00ab0714"></a> `00ab0714` | `9c 47 99 52` | mov w28,#0xca3c | `FALL_THROUGH`
<a id="insn-00ab0718"></a> `00ab0718` | `6d 2d 00 54` | b.le 0x00ab0cc4 | `CONDITIONAL_JUMP`
<a id="insn-00ab071c"></a> `00ab071c` | `e0 23 41 a9` | ldp x0,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0720"></a> `00ab0720` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00ab0724"></a> `00ab0724` | `20 2d 00 54` | b.eq 0x00ab0cc8 | `CONDITIONAL_JUMP`
<a id="insn-00ab0728"></a> `00ab0728` | `ff 06 00 71` | cmp w23,#0x1 | `FALL_THROUGH`
<a id="insn-00ab072c"></a> `00ab072c` | `cb 2c 00 54` | b.lt 0x00ab0cc4 | `CONDITIONAL_JUMP`
<a id="insn-00ab0730"></a> `00ab0730` | `f8 03 1f 2a` | mov w24,wzr | `FALL_THROUGH`
<a id="insn-00ab0734"></a> `00ab0734` | `08 00 00 14` | b 0x00ab0754 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0738"></a> `00ab0738` | `88 02 15 8b` | add x8,x20,x21 | `FALL_THROUGH`
<a id="insn-00ab073c"></a> `00ab073c` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00ab0740"></a> `00ab0740` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ab0744"></a> `00ab0744` | `20 2c 00 54` | b.eq 0x00ab0cc8 | `CONDITIONAL_JUMP`
<a id="insn-00ab0748"></a> `00ab0748` | `18 07 00 11` | add w24,w24,#0x1 | `FALL_THROUGH`
<a id="insn-00ab074c"></a> `00ab074c` | `1f 03 17 6b` | cmp w24,w23 | `FALL_THROUGH`
<a id="insn-00ab0750"></a> `00ab0750` | `a0 2b 00 54` | b.eq 0x00ab0cc4 | `CONDITIONAL_JUMP`
<a id="insn-00ab0754"></a> `00ab0754` | `e9 23 41 a9` | ldp x9,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0758"></a> `00ab0758` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00ab075c"></a> `00ab075c` | `00 fd 42 d3` | lsr x0,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00ab0760"></a> `00ab0760` | `5e 68 e6 97` | bl 0x0044a8d8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0764"></a> `00ab0764` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0768"></a> `00ab0768` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00ab076c"></a> `00ab076c` | `19 d9 60 b8` | ldr w25,[x8, w0, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00ab0770"></a> `00ab0770` | `84 bb f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0774"></a> `00ab0774` | `16 d0 4c 91` | add x22,x0,#0x334, LSL #12 | `FALL_THROUGH`
<a id="insn-00ab0778"></a> `00ab0778` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00ab077c"></a> `00ab077c` | `68 8f 43 f8` | ldr x8,[x27, #0x38]! | `FALL_THROUGH`
<a id="insn-00ab0780"></a> `00ab0780` | `c8 00 00 b5` | cbnz x8,0x00ab0798 | `CONDITIONAL_JUMP`
<a id="insn-00ab0784"></a> `00ab0784` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00ab0788"></a> `00ab0788` | `0c 00 00 14` | b 0x00ab07b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab078c"></a> `00ab078c` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00ab0790"></a> `00ab0790` | `fb 03 1a aa` | mov x27,x26 | `FALL_THROUGH`
<a id="insn-00ab0794"></a> `00ab0794` | `28 01 00 b4` | cbz x8,0x00ab07b8 | `CONDITIONAL_JUMP`
<a id="insn-00ab0798"></a> `00ab0798` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00ab079c"></a> `00ab079c` | `08 21 80 b9` | ldrsw x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ab07a0"></a> `00ab07a0` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00ab07a4"></a> `00ab07a4` | `4b ff ff 54` | b.lt 0x00ab078c | `CONDITIONAL_JUMP`
<a id="insn-00ab07a8"></a> `00ab07a8` | `6d 03 00 54` | b.le 0x00ab0814 | `CONDITIONAL_JUMP`
<a id="insn-00ab07ac"></a> `00ab07ac` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00ab07b0"></a> `00ab07b0` | `48 ff ff b5` | cbnz x8,0x00ab0798 | `CONDITIONAL_JUMP`
<a id="insn-00ab07b4"></a> `00ab07b4` | `5b 23 00 91` | add x27,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00ab07b8"></a> `00ab07b8` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00ab07bc"></a> `00ab07bc` | `0d aa 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab07c0"></a> `00ab07c0` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ab07c4"></a> `00ab07c4` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00ab07c8"></a> `00ab07c8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ab07cc"></a> `00ab07cc` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab07d0"></a> `00ab07d0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab07d4"></a> `00ab07d4` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00ab07d8"></a> `00ab07d8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab07dc"></a> `00ab07dc` | `1a 08 00 f9` | str x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab07e0"></a> `00ab07e0` | `60 03 00 f9` | str x0,[x27] | `FALL_THROUGH`
<a id="insn-00ab07e4"></a> `00ab07e4` | `c8 1a 40 f9` | ldr x8,[x22, #0x30] | `FALL_THROUGH`
<a id="insn-00ab07e8"></a> `00ab07e8` | `13 20 00 b9` | str w19,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab07ec"></a> `00ab07ec` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab07f0"></a> `00ab07f0` | `68 00 00 b4` | cbz x8,0x00ab07fc | `CONDITIONAL_JUMP`
<a id="insn-00ab07f4"></a> `00ab07f4` | `c8 1a 00 f9` | str x8,[x22, #0x30] | `FALL_THROUGH`
<a id="insn-00ab07f8"></a> `00ab07f8` | `61 03 40 f9` | ldr x1,[x27] | `FALL_THROUGH`
<a id="insn-00ab07fc"></a> `00ab07fc` | `c0 1e 40 f9` | ldr x0,[x22, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0800"></a> `00ab0800` | `19 a2 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0804"></a> `00ab0804` | `c8 22 40 f9` | ldr x8,[x22, #0x40] | `FALL_THROUGH`
<a id="insn-00ab0808"></a> `00ab0808` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab080c"></a> `00ab080c` | `c8 22 00 f9` | str x8,[x22, #0x40] | `FALL_THROUGH`
<a id="insn-00ab0810"></a> `00ab0810` | `02 00 00 14` | b 0x00ab0818 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0814"></a> `00ab0814` | `f5 03 1a aa` | mov x21,x26 | `FALL_THROUGH`
<a id="insn-00ab0818"></a> `00ab0818` | `fb 03 15 aa` | mov x27,x21 | `FALL_THROUGH`
<a id="insn-00ab081c"></a> `00ab081c` | `68 0f 43 f8` | ldr x8,[x27, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab0820"></a> `00ab0820` | `c8 00 00 b5` | cbnz x8,0x00ab0838 | `CONDITIONAL_JUMP`
<a id="insn-00ab0824"></a> `00ab0824` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00ab0828"></a> `00ab0828` | `0d 00 00 14` | b 0x00ab085c | `UNCONDITIONAL_JUMP`
<a id="insn-00ab082c"></a> `00ab082c` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00ab0830"></a> `00ab0830` | `fb 03 1a aa` | mov x27,x26 | `FALL_THROUGH`
<a id="insn-00ab0834"></a> `00ab0834` | `48 01 00 b4` | cbz x8,0x00ab085c | `CONDITIONAL_JUMP`
<a id="insn-00ab0838"></a> `00ab0838` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00ab083c"></a> `00ab083c` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0840"></a> `00ab0840` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00ab0844"></a> `00ab0844` | `4b ff ff 54` | b.lt 0x00ab082c | `CONDITIONAL_JUMP`
<a id="insn-00ab0848"></a> `00ab0848` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00ab084c"></a> `00ab084c` | `4a 03 00 54` | b.ge 0x00ab08b4 | `CONDITIONAL_JUMP`
<a id="insn-00ab0850"></a> `00ab0850` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00ab0854"></a> `00ab0854` | `28 ff ff b5` | cbnz x8,0x00ab0838 | `CONDITIONAL_JUMP`
<a id="insn-00ab0858"></a> `00ab0858` | `5b 23 00 91` | add x27,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00ab085c"></a> `00ab085c` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00ab0860"></a> `00ab0860` | `e4 a9 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0864"></a> `00ab0864` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab0868"></a> `00ab0868` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ab086c"></a> `00ab086c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab0870"></a> `00ab0870` | `1a 08 00 f9` | str x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0874"></a> `00ab0874` | `60 03 00 f9` | str x0,[x27] | `FALL_THROUGH`
<a id="insn-00ab0878"></a> `00ab0878` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00ab087c"></a> `00ab087c` | `19 1c 00 b9` | str w25,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0880"></a> `00ab0880` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0884"></a> `00ab0884` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab0888"></a> `00ab0888` | `68 00 00 b4` | cbz x8,0x00ab0894 | `CONDITIONAL_JUMP`
<a id="insn-00ab088c"></a> `00ab088c` | `a8 16 00 f9` | str x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0890"></a> `00ab0890` | `61 03 40 f9` | ldr x1,[x27] | `FALL_THROUGH`
<a id="insn-00ab0894"></a> `00ab0894` | `a0 1a 40 f9` | ldr x0,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00ab0898"></a> `00ab0898` | `f3 a1 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab089c"></a> `00ab089c` | `a8 1e 40 f9` | ldr x8,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00ab08a0"></a> `00ab08a0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab08a4"></a> `00ab08a4` | `a8 1e 00 f9` | str x8,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00ab08a8"></a> `00ab08a8` | `c8 82 40 39` | ldrb w8,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00ab08ac"></a> `00ab08ac` | `e8 f4 07 37` | tbnz w8,#0x0,0x00ab0748 | `CONDITIONAL_JUMP`
<a id="insn-00ab08b0"></a> `00ab08b0` | `04 00 00 14` | b 0x00ab08c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab08b4"></a> `00ab08b4` | `f6 03 1a aa` | mov x22,x26 | `FALL_THROUGH`
<a id="insn-00ab08b8"></a> `00ab08b8` | `c8 82 40 39` | ldrb w8,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00ab08bc"></a> `00ab08bc` | `68 f4 07 37` | tbnz w8,#0x0,0x00ab0748 | `CONDITIONAL_JUMP`
<a id="insn-00ab08c0"></a> `00ab08c0` | `30 bb f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab08c4"></a> `00ab08c4` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00ab08c8"></a> `00ab08c8` | `0d ef f3 97` | bl 0x007ac4fc | `UNCONDITIONAL_CALL`
<a id="insn-00ab08cc"></a> `00ab08cc` | `60 01 00 36` | tbz w0,#0x0,0x00ab08f8 | `CONDITIONAL_JUMP`
<a id="insn-00ab08d0"></a> `00ab08d0` | `2c bb f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab08d4"></a> `00ab08d4` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00ab08d8"></a> `00ab08d8` | `27 ef f3 97` | bl 0x007ac574 | `UNCONDITIONAL_CALL`
<a id="insn-00ab08dc"></a> `00ab08dc` | `e0 00 00 36` | tbz w0,#0x0,0x00ab08f8 | `CONDITIONAL_JUMP`
<a id="insn-00ab08e0"></a> `00ab08e0` | `28 bb f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab08e4"></a> `00ab08e4` | `08 0b 88 52` | mov w8,#0x4058 | `FALL_THROUGH`
<a id="insn-00ab08e8"></a> `00ab08e8` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab08ec"></a> `00ab08ec` | `08 68 e8 38` | ldrsb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ab08f0"></a> `00ab08f0` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00ab08f4"></a> `00ab08f4` | `a0 f2 ff 54` | b.eq 0x00ab0748 | `CONDITIONAL_JUMP`
<a id="insn-00ab08f8"></a> `00ab08f8` | `22 bb f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab08fc"></a> `00ab08fc` | `16 d0 4c 91` | add x22,x0,#0x334, LSL #12 | `FALL_THROUGH`
<a id="insn-00ab0900"></a> `00ab0900` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00ab0904"></a> `00ab0904` | `68 0f 42 f8` | ldr x8,[x27, #0x20]! | `FALL_THROUGH`
<a id="insn-00ab0908"></a> `00ab0908` | `c8 00 00 b5` | cbnz x8,0x00ab0920 | `CONDITIONAL_JUMP`
<a id="insn-00ab090c"></a> `00ab090c` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00ab0910"></a> `00ab0910` | `0c 00 00 14` | b 0x00ab0940 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0914"></a> `00ab0914` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00ab0918"></a> `00ab0918` | `fb 03 1a aa` | mov x27,x26 | `FALL_THROUGH`
<a id="insn-00ab091c"></a> `00ab091c` | `28 01 00 b4` | cbz x8,0x00ab0940 | `CONDITIONAL_JUMP`
<a id="insn-00ab0920"></a> `00ab0920` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00ab0924"></a> `00ab0924` | `08 21 80 b9` | ldrsw x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0928"></a> `00ab0928` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00ab092c"></a> `00ab092c` | `4b ff ff 54` | b.lt 0x00ab0914 | `CONDITIONAL_JUMP`
<a id="insn-00ab0930"></a> `00ab0930` | `6d 03 00 54` | b.le 0x00ab099c | `CONDITIONAL_JUMP`
<a id="insn-00ab0934"></a> `00ab0934` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00ab0938"></a> `00ab0938` | `48 ff ff b5` | cbnz x8,0x00ab0920 | `CONDITIONAL_JUMP`
<a id="insn-00ab093c"></a> `00ab093c` | `5b 23 00 91` | add x27,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00ab0940"></a> `00ab0940` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00ab0944"></a> `00ab0944` | `ab a9 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0948"></a> `00ab0948` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ab094c"></a> `00ab094c` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0950"></a> `00ab0950` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ab0954"></a> `00ab0954` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab0958"></a> `00ab0958` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab095c"></a> `00ab095c` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0960"></a> `00ab0960` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab0964"></a> `00ab0964` | `1a 08 00 f9` | str x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0968"></a> `00ab0968` | `60 03 00 f9` | str x0,[x27] | `FALL_THROUGH`
<a id="insn-00ab096c"></a> `00ab096c` | `c8 0e 40 f9` | ldr x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00ab0970"></a> `00ab0970` | `13 20 00 b9` | str w19,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0974"></a> `00ab0974` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab0978"></a> `00ab0978` | `68 00 00 b4` | cbz x8,0x00ab0984 | `CONDITIONAL_JUMP`
<a id="insn-00ab097c"></a> `00ab097c` | `c8 0e 00 f9` | str x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00ab0980"></a> `00ab0980` | `61 03 40 f9` | ldr x1,[x27] | `FALL_THROUGH`
<a id="insn-00ab0984"></a> `00ab0984` | `c0 12 40 f9` | ldr x0,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0988"></a> `00ab0988` | `b7 a1 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab098c"></a> `00ab098c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0990"></a> `00ab0990` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0994"></a> `00ab0994` | `c8 16 00 f9` | str x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0998"></a> `00ab0998` | `02 00 00 14` | b 0x00ab09a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab099c"></a> `00ab099c` | `f5 03 1a aa` | mov x21,x26 | `FALL_THROUGH`
<a id="insn-00ab09a0"></a> `00ab09a0` | `fb 03 15 aa` | mov x27,x21 | `FALL_THROUGH`
<a id="insn-00ab09a4"></a> `00ab09a4` | `68 0f 43 f8` | ldr x8,[x27, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab09a8"></a> `00ab09a8` | `c8 00 00 b5` | cbnz x8,0x00ab09c0 | `CONDITIONAL_JUMP`
<a id="insn-00ab09ac"></a> `00ab09ac` | `fa 03 1b aa` | mov x26,x27 | `FALL_THROUGH`
<a id="insn-00ab09b0"></a> `00ab09b0` | `0d 00 00 14` | b 0x00ab09e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab09b4"></a> `00ab09b4` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-00ab09b8"></a> `00ab09b8` | `fb 03 1a aa` | mov x27,x26 | `FALL_THROUGH`
<a id="insn-00ab09bc"></a> `00ab09bc` | `48 01 00 b4` | cbz x8,0x00ab09e4 | `CONDITIONAL_JUMP`
<a id="insn-00ab09c0"></a> `00ab09c0` | `fa 03 08 aa` | mov x26,x8 | `FALL_THROUGH`
<a id="insn-00ab09c4"></a> `00ab09c4` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab09c8"></a> `00ab09c8` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00ab09cc"></a> `00ab09cc` | `4b ff ff 54` | b.lt 0x00ab09b4 | `CONDITIONAL_JUMP`
<a id="insn-00ab09d0"></a> `00ab09d0` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00ab09d4"></a> `00ab09d4` | `0a 03 00 54` | b.ge 0x00ab0a34 | `CONDITIONAL_JUMP`
<a id="insn-00ab09d8"></a> `00ab09d8` | `48 07 40 f9` | ldr x8,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00ab09dc"></a> `00ab09dc` | `28 ff ff b5` | cbnz x8,0x00ab09c0 | `CONDITIONAL_JUMP`
<a id="insn-00ab09e0"></a> `00ab09e0` | `5b 23 00 91` | add x27,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00ab09e4"></a> `00ab09e4` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00ab09e8"></a> `00ab09e8` | `82 a9 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab09ec"></a> `00ab09ec` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab09f0"></a> `00ab09f0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ab09f4"></a> `00ab09f4` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab09f8"></a> `00ab09f8` | `1a 08 00 f9` | str x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab09fc"></a> `00ab09fc` | `60 03 00 f9` | str x0,[x27] | `FALL_THROUGH`
<a id="insn-00ab0a00"></a> `00ab0a00` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0a04"></a> `00ab0a04` | `19 1c 00 b9` | str w25,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0a08"></a> `00ab0a08` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0a0c"></a> `00ab0a0c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab0a10"></a> `00ab0a10` | `68 00 00 b4` | cbz x8,0x00ab0a1c | `CONDITIONAL_JUMP`
<a id="insn-00ab0a14"></a> `00ab0a14` | `a8 16 00 f9` | str x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0a18"></a> `00ab0a18` | `61 03 40 f9` | ldr x1,[x27] | `FALL_THROUGH`
<a id="insn-00ab0a1c"></a> `00ab0a1c` | `a0 1a 40 f9` | ldr x0,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00ab0a20"></a> `00ab0a20` | `91 a1 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0a24"></a> `00ab0a24` | `a8 1e 40 f9` | ldr x8,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0a28"></a> `00ab0a28` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0a2c"></a> `00ab0a2c` | `a8 1e 00 f9` | str x8,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0a30"></a> `00ab0a30` | `02 00 00 14` | b 0x00ab0a38 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0a34"></a> `00ab0a34` | `f6 03 1a aa` | mov x22,x26 | `FALL_THROUGH`
<a id="insn-00ab0a38"></a> `00ab0a38` | `e0 27 41 a9` | ldp x0,x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0a3c"></a> `00ab0a3c` | `88 7e 40 93` | sxtw x8,w20 | `FALL_THROUGH`
<a id="insn-00ab0a40"></a> `00ab0a40` | `14 08 08 8b` | add x20,x0,x8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00ab0a44"></a> `00ab0a44` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0a48"></a> `00ab0a48` | `c8 82 00 39` | strb w8,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0a4c"></a> `00ab0a4c` | `81 12 00 91` | add x1,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00ab0a50"></a> `00ab0a50` | `35 01 01 eb` | subs x21,x9,x1 | `FALL_THROUGH`
<a id="insn-00ab0a54"></a> `00ab0a54` | `20 e7 ff 54` | b.eq 0x00ab0738 | `CONDITIONAL_JUMP`
<a id="insn-00ab0a58"></a> `00ab0a58` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ab0a5c"></a> `00ab0a5c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00ab0a60"></a> `00ab0a60` | `90 a9 04 94` | bl 0x00bdb0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0a64"></a> `00ab0a64` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0a68"></a> `00ab0a68` | `34 ff ff 17` | b 0x00ab0738 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0a6c"></a> `00ab0a6c` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00ab0a70"></a> `00ab0a70` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00ab0a74"></a> `00ab0a74` | `08 0f 43 f8` | ldr x8,[x24, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab0a78"></a> `00ab0a78` | `c8 00 00 b5` | cbnz x8,0x00ab0a90 | `CONDITIONAL_JUMP`
<a id="insn-00ab0a7c"></a> `00ab0a7c` | `f6 03 18 aa` | mov x22,x24 | `FALL_THROUGH`
<a id="insn-00ab0a80"></a> `00ab0a80` | `0d 00 00 14` | b 0x00ab0ab4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0a84"></a> `00ab0a84` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00ab0a88"></a> `00ab0a88` | `f8 03 16 aa` | mov x24,x22 | `FALL_THROUGH`
<a id="insn-00ab0a8c"></a> `00ab0a8c` | `48 01 00 b4` | cbz x8,0x00ab0ab4 | `CONDITIONAL_JUMP`
<a id="insn-00ab0a90"></a> `00ab0a90` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00ab0a94"></a> `00ab0a94` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0a98"></a> `00ab0a98` | `1f c1 00 71` | cmp w8,#0x30 | `FALL_THROUGH`
<a id="insn-00ab0a9c"></a> `00ab0a9c` | `4a ff ff 54` | b.ge 0x00ab0a84 | `CONDITIONAL_JUMP`
<a id="insn-00ab0aa0"></a> `00ab0aa0` | `1f bd 00 71` | cmp w8,#0x2f | `FALL_THROUGH`
<a id="insn-00ab0aa4"></a> `00ab0aa4` | `60 03 00 54` | b.eq 0x00ab0b10 | `CONDITIONAL_JUMP`
<a id="insn-00ab0aa8"></a> `00ab0aa8` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00ab0aac"></a> `00ab0aac` | `28 ff ff b5` | cbnz x8,0x00ab0a90 | `CONDITIONAL_JUMP`
<a id="insn-00ab0ab0"></a> `00ab0ab0` | `d8 22 00 91` | add x24,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00ab0ab4"></a> `00ab0ab4` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00ab0ab8"></a> `00ab0ab8` | `4e a9 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0abc"></a> `00ab0abc` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab0ac0"></a> `00ab0ac0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ab0ac4"></a> `00ab0ac4` | `e9 05 80 52` | mov w9,#0x2f | `FALL_THROUGH`
<a id="insn-00ab0ac8"></a> `00ab0ac8` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0acc"></a> `00ab0acc` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab0ad0"></a> `00ab0ad0` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00ab0ad4"></a> `00ab0ad4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0ad8"></a> `00ab0ad8` | `09 1c 00 b9` | str w9,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0adc"></a> `00ab0adc` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0ae0"></a> `00ab0ae0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab0ae4"></a> `00ab0ae4` | `68 00 00 b4` | cbz x8,0x00ab0af0 | `CONDITIONAL_JUMP`
<a id="insn-00ab0ae8"></a> `00ab0ae8` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0aec"></a> `00ab0aec` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00ab0af0"></a> `00ab0af0` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00ab0af4"></a> `00ab0af4` | `5c a1 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0af8"></a> `00ab0af8` | `88 1e 40 f9` | ldr x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0afc"></a> `00ab0afc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0b00"></a> `00ab0b00` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0b04"></a> `00ab0b04` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0b08"></a> `00ab0b08` | `e8 0d 00 37` | tbnz w8,#0x0,0x00ab0cc4 | `CONDITIONAL_JUMP`
<a id="insn-00ab0b0c"></a> `00ab0b0c` | `04 00 00 14` | b 0x00ab0b1c | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0b10"></a> `00ab0b10` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00ab0b14"></a> `00ab0b14` | `a8 82 40 39` | ldrb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0b18"></a> `00ab0b18` | `68 0d 00 37` | tbnz w8,#0x0,0x00ab0cc4 | `CONDITIONAL_JUMP`
<a id="insn-00ab0b1c"></a> `00ab0b1c` | `80 0c 80 52` | mov w0,#0x64 | `FALL_THROUGH`
<a id="insn-00ab0b20"></a> `00ab0b20` | `6e 67 e6 97` | bl 0x0044a8d8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0b24"></a> `00ab0b24` | `e8 fe 60 d3` | lsr x8,x23,#0x20 | `FALL_THROUGH`
<a id="insn-00ab0b28"></a> `00ab0b28` | `e9 0f 40 b9` | ldr w9,[sp, #0xc] | `FALL_THROUGH`
<a id="insn-00ab0b2c"></a> `00ab0b2c` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00ab0b30"></a> `00ab0b30` | `88 0c 80 52` | mov w8,#0x64 | `FALL_THROUGH`
<a id="insn-00ab0b34"></a> `00ab0b34` | `08 c1 89 1a` | csel w8,w8,w9,gt | `FALL_THROUGH`
<a id="insn-00ab0b38"></a> `00ab0b38` | `1f 01 00 6b` | cmp w8,w0 | `FALL_THROUGH`
<a id="insn-00ab0b3c"></a> `00ab0b3c` | `4d 0c 00 54` | b.le 0x00ab0cc4 | `CONDITIONAL_JUMP`
<a id="insn-00ab0b40"></a> `00ab0b40` | `90 ba f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0b44"></a> `00ab0b44` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00ab0b48"></a> `00ab0b48` | `6d ee f3 97` | bl 0x007ac4fc | `UNCONDITIONAL_CALL`
<a id="insn-00ab0b4c"></a> `00ab0b4c` | `60 01 00 36` | tbz w0,#0x0,0x00ab0b78 | `CONDITIONAL_JUMP`
<a id="insn-00ab0b50"></a> `00ab0b50` | `8c ba f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0b54"></a> `00ab0b54` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00ab0b58"></a> `00ab0b58` | `87 ee f3 97` | bl 0x007ac574 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0b5c"></a> `00ab0b5c` | `e0 00 00 36` | tbz w0,#0x0,0x00ab0b78 | `CONDITIONAL_JUMP`
<a id="insn-00ab0b60"></a> `00ab0b60` | `88 ba f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0b64"></a> `00ab0b64` | `08 0b 88 52` | mov w8,#0x4058 | `FALL_THROUGH`
<a id="insn-00ab0b68"></a> `00ab0b68` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0b6c"></a> `00ab0b6c` | `08 68 68 38` | ldrb w8,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ab0b70"></a> `00ab0b70` | `1f bd 00 71` | cmp w8,#0x2f | `FALL_THROUGH`
<a id="insn-00ab0b74"></a> `00ab0b74` | `80 0a 00 54` | b.eq 0x00ab0cc4 | `CONDITIONAL_JUMP`
<a id="insn-00ab0b78"></a> `00ab0b78` | `82 ba f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0b7c"></a> `00ab0b7c` | `15 d0 4c 91` | add x21,x0,#0x334, LSL #12 | `FALL_THROUGH`
<a id="insn-00ab0b80"></a> `00ab0b80` | `f7 03 15 aa` | mov x23,x21 | `FALL_THROUGH`
<a id="insn-00ab0b84"></a> `00ab0b84` | `e8 0e 42 f8` | ldr x8,[x23, #0x20]! | `FALL_THROUGH`
<a id="insn-00ab0b88"></a> `00ab0b88` | `c8 00 00 b5` | cbnz x8,0x00ab0ba0 | `CONDITIONAL_JUMP`
<a id="insn-00ab0b8c"></a> `00ab0b8c` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00ab0b90"></a> `00ab0b90` | `0c 00 00 14` | b 0x00ab0bc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0b94"></a> `00ab0b94` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00ab0b98"></a> `00ab0b98` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00ab0b9c"></a> `00ab0b9c` | `28 01 00 b4` | cbz x8,0x00ab0bc0 | `CONDITIONAL_JUMP`
<a id="insn-00ab0ba0"></a> `00ab0ba0` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00ab0ba4"></a> `00ab0ba4` | `08 21 80 b9` | ldrsw x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0ba8"></a> `00ab0ba8` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00ab0bac"></a> `00ab0bac` | `4b ff ff 54` | b.lt 0x00ab0b94 | `CONDITIONAL_JUMP`
<a id="insn-00ab0bb0"></a> `00ab0bb0` | `6d 03 00 54` | b.le 0x00ab0c1c | `CONDITIONAL_JUMP`
<a id="insn-00ab0bb4"></a> `00ab0bb4` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00ab0bb8"></a> `00ab0bb8` | `48 ff ff b5` | cbnz x8,0x00ab0ba0 | `CONDITIONAL_JUMP`
<a id="insn-00ab0bbc"></a> `00ab0bbc` | `d7 22 00 91` | add x23,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00ab0bc0"></a> `00ab0bc0` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00ab0bc4"></a> `00ab0bc4` | `0b a9 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0bc8"></a> `00ab0bc8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ab0bcc"></a> `00ab0bcc` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0bd0"></a> `00ab0bd0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ab0bd4"></a> `00ab0bd4` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab0bd8"></a> `00ab0bd8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab0bdc"></a> `00ab0bdc` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0be0"></a> `00ab0be0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab0be4"></a> `00ab0be4` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0be8"></a> `00ab0be8` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-00ab0bec"></a> `00ab0bec` | `a8 0e 40 f9` | ldr x8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00ab0bf0"></a> `00ab0bf0` | `13 20 00 b9` | str w19,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0bf4"></a> `00ab0bf4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab0bf8"></a> `00ab0bf8` | `68 00 00 b4` | cbz x8,0x00ab0c04 | `CONDITIONAL_JUMP`
<a id="insn-00ab0bfc"></a> `00ab0bfc` | `a8 0e 00 f9` | str x8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00ab0c00"></a> `00ab0c00` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00ab0c04"></a> `00ab0c04` | `a0 12 40 f9` | ldr x0,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0c08"></a> `00ab0c08` | `17 a1 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0c0c"></a> `00ab0c0c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0c10"></a> `00ab0c10` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0c14"></a> `00ab0c14` | `a8 16 00 f9` | str x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0c18"></a> `00ab0c18` | `02 00 00 14` | b 0x00ab0c20 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0c1c"></a> `00ab0c1c` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00ab0c20"></a> `00ab0c20` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-00ab0c24"></a> `00ab0c24` | `e8 0e 43 f8` | ldr x8,[x23, #0x30]! | `FALL_THROUGH`
<a id="insn-00ab0c28"></a> `00ab0c28` | `c8 00 00 b5` | cbnz x8,0x00ab0c40 | `CONDITIONAL_JUMP`
<a id="insn-00ab0c2c"></a> `00ab0c2c` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00ab0c30"></a> `00ab0c30` | `0d 00 00 14` | b 0x00ab0c64 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0c34"></a> `00ab0c34` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00ab0c38"></a> `00ab0c38` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00ab0c3c"></a> `00ab0c3c` | `48 01 00 b4` | cbz x8,0x00ab0c64 | `CONDITIONAL_JUMP`
<a id="insn-00ab0c40"></a> `00ab0c40` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00ab0c44"></a> `00ab0c44` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0c48"></a> `00ab0c48` | `1f c1 00 71` | cmp w8,#0x30 | `FALL_THROUGH`
<a id="insn-00ab0c4c"></a> `00ab0c4c` | `4a ff ff 54` | b.ge 0x00ab0c34 | `CONDITIONAL_JUMP`
<a id="insn-00ab0c50"></a> `00ab0c50` | `1f bd 00 71` | cmp w8,#0x2f | `FALL_THROUGH`
<a id="insn-00ab0c54"></a> `00ab0c54` | `20 03 00 54` | b.eq 0x00ab0cb8 | `CONDITIONAL_JUMP`
<a id="insn-00ab0c58"></a> `00ab0c58` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00ab0c5c"></a> `00ab0c5c` | `28 ff ff b5` | cbnz x8,0x00ab0c40 | `CONDITIONAL_JUMP`
<a id="insn-00ab0c60"></a> `00ab0c60` | `d7 22 00 91` | add x23,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00ab0c64"></a> `00ab0c64` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00ab0c68"></a> `00ab0c68` | `e2 a8 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0c6c"></a> `00ab0c6c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00ab0c70"></a> `00ab0c70` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ab0c74"></a> `00ab0c74` | `e9 05 80 52` | mov w9,#0x2f | `FALL_THROUGH`
<a id="insn-00ab0c78"></a> `00ab0c78` | `16 08 00 f9` | str x22,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0c7c"></a> `00ab0c7c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00ab0c80"></a> `00ab0c80` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-00ab0c84"></a> `00ab0c84` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0c88"></a> `00ab0c88` | `09 1c 00 b9` | str w9,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00ab0c8c"></a> `00ab0c8c` | `1f 80 00 39` | strb wzr,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0c90"></a> `00ab0c90` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00ab0c94"></a> `00ab0c94` | `68 00 00 b4` | cbz x8,0x00ab0ca0 | `CONDITIONAL_JUMP`
<a id="insn-00ab0c98"></a> `00ab0c98` | `88 16 00 f9` | str x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0c9c"></a> `00ab0c9c` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00ab0ca0"></a> `00ab0ca0` | `80 1a 40 f9` | ldr x0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00ab0ca4"></a> `00ab0ca4` | `f0 a0 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0ca8"></a> `00ab0ca8` | `88 1e 40 f9` | ldr x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0cac"></a> `00ab0cac` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0cb0"></a> `00ab0cb0` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0cb4"></a> `00ab0cb4` | `02 00 00 14` | b 0x00ab0cbc | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0cb8"></a> `00ab0cb8` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00ab0cbc"></a> `00ab0cbc` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0cc0"></a> `00ab0cc0` | `a8 82 00 39` | strb w8,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0cc4"></a> `00ab0cc4` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0cc8"></a> `00ab0cc8` | `c0 74 ff b4` | cbz x0,0x00aafb60 | `CONDITIONAL_JUMP`
<a id="insn-00ab0ccc"></a> `00ab0ccc` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ab0cd0"></a> `00ab0cd0` | `d0 a8 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0cd4"></a> `00ab0cd4` | `a3 fb ff 17` | b 0x00aafb60 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0cd8"></a> `00ab0cd8` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ab0cdc"></a> `00ab0cdc` | `60 00 00 b4` | cbz x0,0x00ab0ce8 | `CONDITIONAL_JUMP`
<a id="insn-00ab0ce0"></a> `00ab0ce0` | `e0 1f 00 f9` | str x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ab0ce4"></a> `00ab0ce4` | `cb a8 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0ce8"></a> `00ab0ce8` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00ab0cec"></a> `00ab0cec` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0cf0"></a> `00ab0cf0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ab0cf4"></a> `00ab0cf4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab0cf8"></a> `00ab0cf8` | `e1 09 00 54` | b.ne 0x00ab0e34 | `CONDITIONAL_JUMP`
<a id="insn-00ab0cfc"></a> `00ab0cfc` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ab0d00"></a> `00ab0d00` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00ab0d04"></a> `00ab0d04` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ab0d08"></a> `00ab0d08` | `fa 67 47 a9` | ldp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ab0d0c"></a> `00ab0d0c` | `fc 6f 46 a9` | ldp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ab0d10"></a> `00ab0d10` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ab0d14"></a> `00ab0d14` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00ab0d18"></a> `00ab0d18` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ab0d1c"></a> `00ab0d1c` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00ab0d20"></a> `00ab0d20` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0d24"></a> `00ab0d24` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ab0d28"></a> `00ab0d28` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab0d2c"></a> `00ab0d2c` | `41 08 00 54` | b.ne 0x00ab0e34 | `CONDITIONAL_JUMP`
<a id="insn-00ab0d30"></a> `00ab0d30` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ab0d34"></a> `00ab0d34` | `0d 73 e6 97` | bl 0x0044d968 | `CALL_TERMINATOR`
<a id="insn-00ab0d38"></a> `00ab0d38` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00ab0d3c"></a> `00ab0d3c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0d40"></a> `00ab0d40` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ab0d44"></a> `00ab0d44` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab0d48"></a> `00ab0d48` | `61 07 00 54` | b.ne 0x00ab0e34 | `CONDITIONAL_JUMP`
<a id="insn-00ab0d4c"></a> `00ab0d4c` | `8d b5 e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-00ab0d50"></a> `00ab0d50` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00ab0d54"></a> `00ab0d54` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0d58"></a> `00ab0d58` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ab0d5c"></a> `00ab0d5c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab0d60"></a> `00ab0d60` | `a1 06 00 54` | b.ne 0x00ab0e34 | `CONDITIONAL_JUMP`
<a id="insn-00ab0d64"></a> `00ab0d64` | `e8 a3 00 91` | add x8,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00ab0d68"></a> `00ab0d68` | `00 21 00 91` | add x0,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00ab0d6c"></a> `00ab0d6c` | `38 00 00 94` | bl 0x00ab0e4c | `UNCONDITIONAL_CALL`
<a id="insn-00ab0d70"></a> `00ab0d70` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00ab0d74"></a> `00ab0d74` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0d78"></a> `00ab0d78` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ab0d7c"></a> `00ab0d7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab0d80"></a> `00ab0d80` | `a1 05 00 54` | b.ne 0x00ab0e34 | `CONDITIONAL_JUMP`
<a id="insn-00ab0d84"></a> `00ab0d84` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ab0d88"></a> `00ab0d88` | `f8 72 e6 97` | bl 0x0044d968 | `CALL_TERMINATOR`
<a id="insn-00ab0d8c"></a> `00ab0d8c` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00ab0d90"></a> `00ab0d90` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ab0d94"></a> `00ab0d94` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ab0d98"></a> `00ab0d98` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ab0d9c"></a> `00ab0d9c` | `c1 04 00 54` | b.ne 0x00ab0e34 | `CONDITIONAL_JUMP`
<a id="insn-00ab0da0"></a> `00ab0da0` | `78 b5 e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-00ab0e34"></a> `00ab0e34` | `83 a8 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aafb1c`](#insn-00aafb1c) 範囲 `[['00aafb1c', '00aafb5f']]`
  - `UNCONDITIONAL_JUMP` [`00aafb5c`](#insn-00aafb5c) → [`00aafb6c`](#insn-00aafb6c)
- ブロック [`00aafb60`](#insn-00aafb60) 範囲 `[['00aafb60', '00aafb6b']]`
  - `CONDITIONAL_JUMP` [`00aafb68`](#insn-00aafb68) → [`00ab0cd8`](#insn-00ab0cd8)
  - `FALL_THROUGH` [`00aafb68`](#insn-00aafb68) → [`00aafb6c`](#insn-00aafb6c)
- ブロック [`00aafb6c`](#insn-00aafb6c) 範囲 `[['00aafb6c', '00aafb73']]`
  - `CONDITIONAL_JUMP` [`00aafb70`](#insn-00aafb70) → [`00aafb60`](#insn-00aafb60)
  - `FALL_THROUGH` [`00aafb70`](#insn-00aafb70) → [`00aafb74`](#insn-00aafb74)
- ブロック [`00aafb74`](#insn-00aafb74) 範囲 `[['00aafb74', '00aafbcf']]`
  - `CONDITIONAL_JUMP` [`00aafbcc`](#insn-00aafbcc) → [`00aafb60`](#insn-00aafb60)
  - `FALL_THROUGH` [`00aafbcc`](#insn-00aafbcc) → [`00aafbd0`](#insn-00aafbd0)
- ブロック [`00aafbd0`](#insn-00aafbd0) 範囲 `[['00aafbd0', '00aafc23']]`
  - `CONDITIONAL_JUMP` [`00aafc20`](#insn-00aafc20) → [`00aafb60`](#insn-00aafb60)
  - `FALL_THROUGH` [`00aafc20`](#insn-00aafc20) → [`00aafc24`](#insn-00aafc24)
- ブロック [`00aafc24`](#insn-00aafc24) 範囲 `[['00aafc24', '00aafc37']]`
  - `CONDITIONAL_JUMP` [`00aafc34`](#insn-00aafc34) → [`00aafc4c`](#insn-00aafc4c)
  - `FALL_THROUGH` [`00aafc34`](#insn-00aafc34) → [`00aafc38`](#insn-00aafc38)
- ブロック [`00aafc38`](#insn-00aafc38) 範囲 `[['00aafc38', '00aafc3f']]`
  - `UNCONDITIONAL_JUMP` [`00aafc3c`](#insn-00aafc3c) → [`00aafc6c`](#insn-00aafc6c)
- ブロック [`00aafc40`](#insn-00aafc40) 範囲 `[['00aafc40', '00aafc4b']]`
  - `CONDITIONAL_JUMP` [`00aafc48`](#insn-00aafc48) → [`00aafc6c`](#insn-00aafc6c)
  - `FALL_THROUGH` [`00aafc48`](#insn-00aafc48) → [`00aafc4c`](#insn-00aafc4c)
- ブロック [`00aafc4c`](#insn-00aafc4c) 範囲 `[['00aafc4c', '00aafc5b']]`
  - `CONDITIONAL_JUMP` [`00aafc58`](#insn-00aafc58) → [`00aafc40`](#insn-00aafc40)
  - `FALL_THROUGH` [`00aafc58`](#insn-00aafc58) → [`00aafc5c`](#insn-00aafc5c)
- ブロック [`00aafc5c`](#insn-00aafc5c) 範囲 `[['00aafc5c', '00aafc5f']]`
  - `CONDITIONAL_JUMP` [`00aafc5c`](#insn-00aafc5c) → [`00aafcc8`](#insn-00aafcc8)
  - `FALL_THROUGH` [`00aafc5c`](#insn-00aafc5c) → [`00aafc60`](#insn-00aafc60)
- ブロック [`00aafc60`](#insn-00aafc60) 範囲 `[['00aafc60', '00aafc67']]`
  - `CONDITIONAL_JUMP` [`00aafc64`](#insn-00aafc64) → [`00aafc4c`](#insn-00aafc4c)
  - `FALL_THROUGH` [`00aafc64`](#insn-00aafc64) → [`00aafc68`](#insn-00aafc68)
- ブロック [`00aafc68`](#insn-00aafc68) 範囲 `[['00aafc68', '00aafc6b']]`
  - `FALL_THROUGH` [`00aafc68`](#insn-00aafc68) → [`00aafc6c`](#insn-00aafc6c)
- ブロック [`00aafc6c`](#insn-00aafc6c) 範囲 `[['00aafc6c', '00aafca7']]`
  - `CONDITIONAL_JUMP` [`00aafca4`](#insn-00aafca4) → [`00aafcb0`](#insn-00aafcb0)
  - `FALL_THROUGH` [`00aafca4`](#insn-00aafca4) → [`00aafca8`](#insn-00aafca8)
- ブロック [`00aafca8`](#insn-00aafca8) 範囲 `[['00aafca8', '00aafcaf']]`
  - `FALL_THROUGH` [`00aafcac`](#insn-00aafcac) → [`00aafcb0`](#insn-00aafcb0)
- ブロック [`00aafcb0`](#insn-00aafcb0) 範囲 `[['00aafcb0', '00aafcc7']]`
  - `UNCONDITIONAL_JUMP` [`00aafcc4`](#insn-00aafcc4) → [`00aafccc`](#insn-00aafccc)
- ブロック [`00aafcc8`](#insn-00aafcc8) 範囲 `[['00aafcc8', '00aafccb']]`
  - `FALL_THROUGH` [`00aafcc8`](#insn-00aafcc8) → [`00aafccc`](#insn-00aafccc)
- ブロック [`00aafccc`](#insn-00aafccc) 範囲 `[['00aafccc', '00aafcdb']]`
  - `CONDITIONAL_JUMP` [`00aafcd8`](#insn-00aafcd8) → [`00aafde4`](#insn-00aafde4)
  - `FALL_THROUGH` [`00aafcd8`](#insn-00aafcd8) → [`00aafcdc`](#insn-00aafcdc)
- ブロック [`00aafcdc`](#insn-00aafcdc) 範囲 `[['00aafcdc', '00aafce3']]`
  - `UNCONDITIONAL_JUMP` [`00aafce0`](#insn-00aafce0) → [`00aafcfc`](#insn-00aafcfc)
- ブロック [`00aafce4`](#insn-00aafce4) 範囲 `[['00aafce4', '00aafcfb']]`
  - `CONDITIONAL_JUMP` [`00aafcf8`](#insn-00aafcf8) → [`00aafd30`](#insn-00aafd30)
  - `FALL_THROUGH` [`00aafcf8`](#insn-00aafcf8) → [`00aafcfc`](#insn-00aafcfc)
- ブロック [`00aafcfc`](#insn-00aafcfc) 範囲 `[['00aafcfc', '00aafd07']]`
  - `CONDITIONAL_JUMP` [`00aafd04`](#insn-00aafd04) → [`00aafd18`](#insn-00aafd18)
  - `FALL_THROUGH` [`00aafd04`](#insn-00aafd04) → [`00aafd08`](#insn-00aafd08)
- ブロック [`00aafd08`](#insn-00aafd08) 範囲 `[['00aafd08', '00aafd13']]`
  - `CONDITIONAL_JUMP` [`00aafd10`](#insn-00aafd10) → [`00aafd08`](#insn-00aafd08)
  - `FALL_THROUGH` [`00aafd10`](#insn-00aafd10) → [`00aafd14`](#insn-00aafd14)
- ブロック [`00aafd14`](#insn-00aafd14) 範囲 `[['00aafd14', '00aafd17']]`
  - `UNCONDITIONAL_JUMP` [`00aafd14`](#insn-00aafd14) → [`00aafce4`](#insn-00aafce4)
- ブロック [`00aafd18`](#insn-00aafd18) 範囲 `[['00aafd18', '00aafd2b']]`
  - `CONDITIONAL_JUMP` [`00aafd28`](#insn-00aafd28) → [`00aafd18`](#insn-00aafd18)
  - `FALL_THROUGH` [`00aafd28`](#insn-00aafd28) → [`00aafd2c`](#insn-00aafd2c)
- ブロック [`00aafd2c`](#insn-00aafd2c) 範囲 `[['00aafd2c', '00aafd2f']]`
  - `UNCONDITIONAL_JUMP` [`00aafd2c`](#insn-00aafd2c) → [`00aafce4`](#insn-00aafce4)
- ブロック [`00aafd30`](#insn-00aafd30) 範囲 `[['00aafd30', '00aafd3f']]`
  - `CONDITIONAL_JUMP` [`00aafd3c`](#insn-00aafd3c) → [`00aafdf0`](#insn-00aafdf0)
  - `FALL_THROUGH` [`00aafd3c`](#insn-00aafd3c) → [`00aafd40`](#insn-00aafd40)
- ブロック [`00aafd40`](#insn-00aafd40) 範囲 `[['00aafd40', '00aafd53']]`
  - `CONDITIONAL_JUMP` [`00aafd50`](#insn-00aafd50) → [`00aafd68`](#insn-00aafd68)
  - `FALL_THROUGH` [`00aafd50`](#insn-00aafd50) → [`00aafd54`](#insn-00aafd54)
- ブロック [`00aafd54`](#insn-00aafd54) 範囲 `[['00aafd54', '00aafd5b']]`
  - `UNCONDITIONAL_JUMP` [`00aafd58`](#insn-00aafd58) → [`00aafd88`](#insn-00aafd88)
- ブロック [`00aafd5c`](#insn-00aafd5c) 範囲 `[['00aafd5c', '00aafd67']]`
  - `CONDITIONAL_JUMP` [`00aafd64`](#insn-00aafd64) → [`00aafd88`](#insn-00aafd88)
  - `FALL_THROUGH` [`00aafd64`](#insn-00aafd64) → [`00aafd68`](#insn-00aafd68)
- ブロック [`00aafd68`](#insn-00aafd68) 範囲 `[['00aafd68', '00aafd77']]`
  - `CONDITIONAL_JUMP` [`00aafd74`](#insn-00aafd74) → [`00aafd5c`](#insn-00aafd5c)
  - `FALL_THROUGH` [`00aafd74`](#insn-00aafd74) → [`00aafd78`](#insn-00aafd78)
- ブロック [`00aafd78`](#insn-00aafd78) 範囲 `[['00aafd78', '00aafd7b']]`
  - `CONDITIONAL_JUMP` [`00aafd78`](#insn-00aafd78) → [`00aafff4`](#insn-00aafff4)
  - `FALL_THROUGH` [`00aafd78`](#insn-00aafd78) → [`00aafd7c`](#insn-00aafd7c)
- ブロック [`00aafd7c`](#insn-00aafd7c) 範囲 `[['00aafd7c', '00aafd83']]`
  - `CONDITIONAL_JUMP` [`00aafd80`](#insn-00aafd80) → [`00aafd68`](#insn-00aafd68)
  - `FALL_THROUGH` [`00aafd80`](#insn-00aafd80) → [`00aafd84`](#insn-00aafd84)
- ブロック [`00aafd84`](#insn-00aafd84) 範囲 `[['00aafd84', '00aafd87']]`
  - `FALL_THROUGH` [`00aafd84`](#insn-00aafd84) → [`00aafd88`](#insn-00aafd88)
- ブロック [`00aafd88`](#insn-00aafd88) 範囲 `[['00aafd88', '00aafdc3']]`
  - `CONDITIONAL_JUMP` [`00aafdc0`](#insn-00aafdc0) → [`00aafdcc`](#insn-00aafdcc)
  - `FALL_THROUGH` [`00aafdc0`](#insn-00aafdc0) → [`00aafdc4`](#insn-00aafdc4)
- ブロック [`00aafdc4`](#insn-00aafdc4) 範囲 `[['00aafdc4', '00aafdcb']]`
  - `FALL_THROUGH` [`00aafdc8`](#insn-00aafdc8) → [`00aafdcc`](#insn-00aafdcc)
- ブロック [`00aafdcc`](#insn-00aafdcc) 範囲 `[['00aafdcc', '00aafde3']]`
  - `UNCONDITIONAL_JUMP` [`00aafde0`](#insn-00aafde0) → [`00aafff8`](#insn-00aafff8)
- ブロック [`00aafde4`](#insn-00aafde4) 範囲 `[['00aafde4', '00aafdef']]`
  - `FALL_THROUGH` [`00aafdec`](#insn-00aafdec) → [`00aafdf0`](#insn-00aafdf0)
- ブロック [`00aafdf0`](#insn-00aafdf0) 範囲 `[['00aafdf0', '00aafdf7']]`
  - `UNCONDITIONAL_JUMP` [`00aafdf4`](#insn-00aafdf4) → [`00aafe0c`](#insn-00aafe0c)
- ブロック [`00aafdf8`](#insn-00aafdf8) 範囲 `[['00aafdf8', '00aafdfb']]`
  - `FALL_THROUGH` [`00aafdf8`](#insn-00aafdf8) → [`00aafdfc`](#insn-00aafdfc)
- ブロック [`00aafdfc`](#insn-00aafdfc) 範囲 `[['00aafdfc', '00aafdff']]`
  - `FALL_THROUGH` [`00aafdfc`](#insn-00aafdfc) → [`00aafe00`](#insn-00aafe00)
- ブロック [`00aafe00`](#insn-00aafe00) 範囲 `[['00aafe00', '00aafe0b']]`
  - `CONDITIONAL_JUMP` [`00aafe08`](#insn-00aafe08) → [`00ab02a8`](#insn-00ab02a8)
  - `FALL_THROUGH` [`00aafe08`](#insn-00aafe08) → [`00aafe0c`](#insn-00aafe0c)
- ブロック [`00aafe0c`](#insn-00aafe0c) 範囲 `[['00aafe0c', '00aafe1f']]`
  - `CONDITIONAL_JUMP` [`00aafe1c`](#insn-00aafe1c) → [`00aafe34`](#insn-00aafe34)
  - `FALL_THROUGH` [`00aafe1c`](#insn-00aafe1c) → [`00aafe20`](#insn-00aafe20)
- ブロック [`00aafe20`](#insn-00aafe20) 範囲 `[['00aafe20', '00aafe27']]`
  - `UNCONDITIONAL_JUMP` [`00aafe24`](#insn-00aafe24) → [`00aafe54`](#insn-00aafe54)
- ブロック [`00aafe28`](#insn-00aafe28) 範囲 `[['00aafe28', '00aafe33']]`
  - `CONDITIONAL_JUMP` [`00aafe30`](#insn-00aafe30) → [`00aafe54`](#insn-00aafe54)
  - `FALL_THROUGH` [`00aafe30`](#insn-00aafe30) → [`00aafe34`](#insn-00aafe34)
- ブロック [`00aafe34`](#insn-00aafe34) 範囲 `[['00aafe34', '00aafe43']]`
  - `CONDITIONAL_JUMP` [`00aafe40`](#insn-00aafe40) → [`00aafe28`](#insn-00aafe28)
  - `FALL_THROUGH` [`00aafe40`](#insn-00aafe40) → [`00aafe44`](#insn-00aafe44)
- ブロック [`00aafe44`](#insn-00aafe44) 範囲 `[['00aafe44', '00aafe47']]`
  - `CONDITIONAL_JUMP` [`00aafe44`](#insn-00aafe44) → [`00aafeb0`](#insn-00aafeb0)
  - `FALL_THROUGH` [`00aafe44`](#insn-00aafe44) → [`00aafe48`](#insn-00aafe48)
- ブロック [`00aafe48`](#insn-00aafe48) 範囲 `[['00aafe48', '00aafe4f']]`
  - `CONDITIONAL_JUMP` [`00aafe4c`](#insn-00aafe4c) → [`00aafe34`](#insn-00aafe34)
  - `FALL_THROUGH` [`00aafe4c`](#insn-00aafe4c) → [`00aafe50`](#insn-00aafe50)
- ブロック [`00aafe50`](#insn-00aafe50) 範囲 `[['00aafe50', '00aafe53']]`
  - `FALL_THROUGH` [`00aafe50`](#insn-00aafe50) → [`00aafe54`](#insn-00aafe54)
- ブロック [`00aafe54`](#insn-00aafe54) 範囲 `[['00aafe54', '00aafe8f']]`
  - `CONDITIONAL_JUMP` [`00aafe8c`](#insn-00aafe8c) → [`00aafe98`](#insn-00aafe98)
  - `FALL_THROUGH` [`00aafe8c`](#insn-00aafe8c) → [`00aafe90`](#insn-00aafe90)
- ブロック [`00aafe90`](#insn-00aafe90) 範囲 `[['00aafe90', '00aafe97']]`
  - `FALL_THROUGH` [`00aafe94`](#insn-00aafe94) → [`00aafe98`](#insn-00aafe98)
- ブロック [`00aafe98`](#insn-00aafe98) 範囲 `[['00aafe98', '00aafeaf']]`
  - `UNCONDITIONAL_JUMP` [`00aafeac`](#insn-00aafeac) → [`00aafeb4`](#insn-00aafeb4)
- ブロック [`00aafeb0`](#insn-00aafeb0) 範囲 `[['00aafeb0', '00aafeb3']]`
  - `FALL_THROUGH` [`00aafeb0`](#insn-00aafeb0) → [`00aafeb4`](#insn-00aafeb4)
- ブロック [`00aafeb4`](#insn-00aafeb4) 範囲 `[['00aafeb4', '00aafebf']]`
  - `CONDITIONAL_JUMP` [`00aafebc`](#insn-00aafebc) → [`00aafed4`](#insn-00aafed4)
  - `FALL_THROUGH` [`00aafebc`](#insn-00aafebc) → [`00aafec0`](#insn-00aafec0)
- ブロック [`00aafec0`](#insn-00aafec0) 範囲 `[['00aafec0', '00aafec7']]`
  - `UNCONDITIONAL_JUMP` [`00aafec4`](#insn-00aafec4) → [`00aafef8`](#insn-00aafef8)
- ブロック [`00aafec8`](#insn-00aafec8) 範囲 `[['00aafec8', '00aafed3']]`
  - `CONDITIONAL_JUMP` [`00aafed0`](#insn-00aafed0) → [`00aafef8`](#insn-00aafef8)
  - `FALL_THROUGH` [`00aafed0`](#insn-00aafed0) → [`00aafed4`](#insn-00aafed4)
- ブロック [`00aafed4`](#insn-00aafed4) 範囲 `[['00aafed4', '00aafee3']]`
  - `CONDITIONAL_JUMP` [`00aafee0`](#insn-00aafee0) → [`00aafec8`](#insn-00aafec8)
  - `FALL_THROUGH` [`00aafee0`](#insn-00aafee0) → [`00aafee4`](#insn-00aafee4)
- ブロック [`00aafee4`](#insn-00aafee4) 範囲 `[['00aafee4', '00aafeeb']]`
  - `CONDITIONAL_JUMP` [`00aafee8`](#insn-00aafee8) → [`00aaff50`](#insn-00aaff50)
  - `FALL_THROUGH` [`00aafee8`](#insn-00aafee8) → [`00aafeec`](#insn-00aafeec)
- ブロック [`00aafeec`](#insn-00aafeec) 範囲 `[['00aafeec', '00aafef3']]`
  - `CONDITIONAL_JUMP` [`00aafef0`](#insn-00aafef0) → [`00aafed4`](#insn-00aafed4)
  - `FALL_THROUGH` [`00aafef0`](#insn-00aafef0) → [`00aafef4`](#insn-00aafef4)
- ブロック [`00aafef4`](#insn-00aafef4) 範囲 `[['00aafef4', '00aafef7']]`
  - `FALL_THROUGH` [`00aafef4`](#insn-00aafef4) → [`00aafef8`](#insn-00aafef8)
- ブロック [`00aafef8`](#insn-00aafef8) 範囲 `[['00aafef8', '00aaff27']]`
  - `CONDITIONAL_JUMP` [`00aaff24`](#insn-00aaff24) → [`00aaff30`](#insn-00aaff30)
  - `FALL_THROUGH` [`00aaff24`](#insn-00aaff24) → [`00aaff28`](#insn-00aaff28)
- ブロック [`00aaff28`](#insn-00aaff28) 範囲 `[['00aaff28', '00aaff2f']]`
  - `FALL_THROUGH` [`00aaff2c`](#insn-00aaff2c) → [`00aaff30`](#insn-00aaff30)
- ブロック [`00aaff30`](#insn-00aaff30) 範囲 `[['00aaff30', '00aaff4b']]`
  - `CONDITIONAL_JUMP` [`00aaff48`](#insn-00aaff48) → [`00aafe00`](#insn-00aafe00)
  - `FALL_THROUGH` [`00aaff48`](#insn-00aaff48) → [`00aaff4c`](#insn-00aaff4c)
- ブロック [`00aaff4c`](#insn-00aaff4c) 範囲 `[['00aaff4c', '00aaff4f']]`
  - `UNCONDITIONAL_JUMP` [`00aaff4c`](#insn-00aaff4c) → [`00aaff5c`](#insn-00aaff5c)
- ブロック [`00aaff50`](#insn-00aaff50) 範囲 `[['00aaff50', '00aaff5b']]`
  - `CONDITIONAL_JUMP` [`00aaff58`](#insn-00aaff58) → [`00aafe00`](#insn-00aafe00)
  - `FALL_THROUGH` [`00aaff58`](#insn-00aaff58) → [`00aaff5c`](#insn-00aaff5c)
- ブロック [`00aaff5c`](#insn-00aaff5c) 範囲 `[['00aaff5c', '00aaff67']]`
  - `CONDITIONAL_JUMP` [`00aaff64`](#insn-00aaff64) → [`00aafdf8`](#insn-00aafdf8)
  - `FALL_THROUGH` [`00aaff64`](#insn-00aaff64) → [`00aaff68`](#insn-00aaff68)
- ブロック [`00aaff68`](#insn-00aaff68) 範囲 `[['00aaff68', '00aaff7f']]`
  - `CONDITIONAL_JUMP` [`00aaff7c`](#insn-00aaff7c) → [`00ab0d1c`](#insn-00ab0d1c)
  - `FALL_THROUGH` [`00aaff7c`](#insn-00aaff7c) → [`00aaff80`](#insn-00aaff80)
- ブロック [`00aaff80`](#insn-00aaff80) 範囲 `[['00aaff80', '00aaffa3']]`
  - `CONDITIONAL_JUMP` [`00aaffa0`](#insn-00aaffa0) → [`00aaffbc`](#insn-00aaffbc)
  - `FALL_THROUGH` [`00aaffa0`](#insn-00aaffa0) → [`00aaffa4`](#insn-00aaffa4)
- ブロック [`00aaffa4`](#insn-00aaffa4) 範囲 `[['00aaffa4', '00aaffab']]`
  - `CONDITIONAL_JUMP` [`00aaffa8`](#insn-00aaffa8) → [`00ab0d38`](#insn-00ab0d38)
  - `FALL_THROUGH` [`00aaffa8`](#insn-00aaffa8) → [`00aaffac`](#insn-00aaffac)
- ブロック [`00aaffac`](#insn-00aaffac) 範囲 `[['00aaffac', '00aaffbb']]`
  - `UNCONDITIONAL_JUMP` [`00aaffb8`](#insn-00aaffb8) → [`00aaffc0`](#insn-00aaffc0)
- ブロック [`00aaffbc`](#insn-00aaffbc) 範囲 `[['00aaffbc', '00aaffbf']]`
  - `FALL_THROUGH` [`00aaffbc`](#insn-00aaffbc) → [`00aaffc0`](#insn-00aaffc0)
- ブロック [`00aaffc0`](#insn-00aaffc0) 範囲 `[['00aaffc0', '00aaffe7']]`
  - `CONDITIONAL_JUMP` [`00aaffe4`](#insn-00aaffe4) → [`00aafdfc`](#insn-00aafdfc)
  - `FALL_THROUGH` [`00aaffe4`](#insn-00aaffe4) → [`00aaffe8`](#insn-00aaffe8)
- ブロック [`00aaffe8`](#insn-00aaffe8) 範囲 `[['00aaffe8', '00aafff3']]`
  - `UNCONDITIONAL_JUMP` [`00aafff0`](#insn-00aafff0) → [`00aafdfc`](#insn-00aafdfc)
- ブロック [`00aafff4`](#insn-00aafff4) 範囲 `[['00aafff4', '00aafff7']]`
  - `FALL_THROUGH` [`00aafff4`](#insn-00aafff4) → [`00aafff8`](#insn-00aafff8)
- ブロック [`00aafff8`](#insn-00aafff8) 範囲 `[['00aafff8', '00ab0003']]`
  - `CONDITIONAL_JUMP` [`00ab0000`](#insn-00ab0000) → [`00ab0018`](#insn-00ab0018)
  - `FALL_THROUGH` [`00ab0000`](#insn-00ab0000) → [`00ab0004`](#insn-00ab0004)
- ブロック [`00ab0004`](#insn-00ab0004) 範囲 `[['00ab0004', '00ab000b']]`
  - `UNCONDITIONAL_JUMP` [`00ab0008`](#insn-00ab0008) → [`00ab003c`](#insn-00ab003c)
- ブロック [`00ab000c`](#insn-00ab000c) 範囲 `[['00ab000c', '00ab0017']]`
  - `CONDITIONAL_JUMP` [`00ab0014`](#insn-00ab0014) → [`00ab003c`](#insn-00ab003c)
  - `FALL_THROUGH` [`00ab0014`](#insn-00ab0014) → [`00ab0018`](#insn-00ab0018)
- ブロック [`00ab0018`](#insn-00ab0018) 範囲 `[['00ab0018', '00ab0027']]`
  - `CONDITIONAL_JUMP` [`00ab0024`](#insn-00ab0024) → [`00ab000c`](#insn-00ab000c)
  - `FALL_THROUGH` [`00ab0024`](#insn-00ab0024) → [`00ab0028`](#insn-00ab0028)
- ブロック [`00ab0028`](#insn-00ab0028) 範囲 `[['00ab0028', '00ab002f']]`
  - `CONDITIONAL_JUMP` [`00ab002c`](#insn-00ab002c) → [`00ab0098`](#insn-00ab0098)
  - `FALL_THROUGH` [`00ab002c`](#insn-00ab002c) → [`00ab0030`](#insn-00ab0030)
- ブロック [`00ab0030`](#insn-00ab0030) 範囲 `[['00ab0030', '00ab0037']]`
  - `CONDITIONAL_JUMP` [`00ab0034`](#insn-00ab0034) → [`00ab0018`](#insn-00ab0018)
  - `FALL_THROUGH` [`00ab0034`](#insn-00ab0034) → [`00ab0038`](#insn-00ab0038)
- ブロック [`00ab0038`](#insn-00ab0038) 範囲 `[['00ab0038', '00ab003b']]`
  - `FALL_THROUGH` [`00ab0038`](#insn-00ab0038) → [`00ab003c`](#insn-00ab003c)
- ブロック [`00ab003c`](#insn-00ab003c) 範囲 `[['00ab003c', '00ab006f']]`
  - `CONDITIONAL_JUMP` [`00ab006c`](#insn-00ab006c) → [`00ab0078`](#insn-00ab0078)
  - `FALL_THROUGH` [`00ab006c`](#insn-00ab006c) → [`00ab0070`](#insn-00ab0070)
- ブロック [`00ab0070`](#insn-00ab0070) 範囲 `[['00ab0070', '00ab0077']]`
  - `FALL_THROUGH` [`00ab0074`](#insn-00ab0074) → [`00ab0078`](#insn-00ab0078)
- ブロック [`00ab0078`](#insn-00ab0078) 範囲 `[['00ab0078', '00ab0093']]`
  - `CONDITIONAL_JUMP` [`00ab0090`](#insn-00ab0090) → [`00ab00a4`](#insn-00ab00a4)
  - `FALL_THROUGH` [`00ab0090`](#insn-00ab0090) → [`00ab0094`](#insn-00ab0094)
- ブロック [`00ab0094`](#insn-00ab0094) 範囲 `[['00ab0094', '00ab0097']]`
  - `UNCONDITIONAL_JUMP` [`00ab0094`](#insn-00ab0094) → [`00aafdf0`](#insn-00aafdf0)
- ブロック [`00ab0098`](#insn-00ab0098) 範囲 `[['00ab0098', '00ab00a3']]`
  - `CONDITIONAL_JUMP` [`00ab00a0`](#insn-00ab00a0) → [`00aafdf0`](#insn-00aafdf0)
  - `FALL_THROUGH` [`00ab00a0`](#insn-00ab00a0) → [`00ab00a4`](#insn-00ab00a4)
- ブロック [`00ab00a4`](#insn-00ab00a4) 範囲 `[['00ab00a4', '00ab00ab']]`
  - `UNCONDITIONAL_JUMP` [`00ab00a8`](#insn-00ab00a8) → [`00ab00d4`](#insn-00ab00d4)
- ブロック [`00ab00ac`](#insn-00ab00ac) 範囲 `[['00ab00ac', '00ab00c7']]`
  - `CONDITIONAL_JUMP` [`00ab00c4`](#insn-00ab00c4) → [`00ab0208`](#insn-00ab0208)
  - `FALL_THROUGH` [`00ab00c4`](#insn-00ab00c4) → [`00ab00c8`](#insn-00ab00c8)
- ブロック [`00ab00c8`](#insn-00ab00c8) 範囲 `[['00ab00c8', '00ab00d3']]`
  - `CONDITIONAL_JUMP` [`00ab00d0`](#insn-00ab00d0) → [`00ab02a8`](#insn-00ab02a8)
  - `FALL_THROUGH` [`00ab00d0`](#insn-00ab00d0) → [`00ab00d4`](#insn-00ab00d4)
- ブロック [`00ab00d4`](#insn-00ab00d4) 範囲 `[['00ab00d4', '00ab00e7']]`
  - `CONDITIONAL_JUMP` [`00ab00e4`](#insn-00ab00e4) → [`00ab00fc`](#insn-00ab00fc)
  - `FALL_THROUGH` [`00ab00e4`](#insn-00ab00e4) → [`00ab00e8`](#insn-00ab00e8)
- ブロック [`00ab00e8`](#insn-00ab00e8) 範囲 `[['00ab00e8', '00ab00ef']]`
  - `UNCONDITIONAL_JUMP` [`00ab00ec`](#insn-00ab00ec) → [`00ab011c`](#insn-00ab011c)
- ブロック [`00ab00f0`](#insn-00ab00f0) 範囲 `[['00ab00f0', '00ab00fb']]`
  - `CONDITIONAL_JUMP` [`00ab00f8`](#insn-00ab00f8) → [`00ab011c`](#insn-00ab011c)
  - `FALL_THROUGH` [`00ab00f8`](#insn-00ab00f8) → [`00ab00fc`](#insn-00ab00fc)
- ブロック [`00ab00fc`](#insn-00ab00fc) 範囲 `[['00ab00fc', '00ab010b']]`
  - `CONDITIONAL_JUMP` [`00ab0108`](#insn-00ab0108) → [`00ab00f0`](#insn-00ab00f0)
  - `FALL_THROUGH` [`00ab0108`](#insn-00ab0108) → [`00ab010c`](#insn-00ab010c)
- ブロック [`00ab010c`](#insn-00ab010c) 範囲 `[['00ab010c', '00ab010f']]`
  - `CONDITIONAL_JUMP` [`00ab010c`](#insn-00ab010c) → [`00ab0178`](#insn-00ab0178)
  - `FALL_THROUGH` [`00ab010c`](#insn-00ab010c) → [`00ab0110`](#insn-00ab0110)
- ブロック [`00ab0110`](#insn-00ab0110) 範囲 `[['00ab0110', '00ab0117']]`
  - `CONDITIONAL_JUMP` [`00ab0114`](#insn-00ab0114) → [`00ab00fc`](#insn-00ab00fc)
  - `FALL_THROUGH` [`00ab0114`](#insn-00ab0114) → [`00ab0118`](#insn-00ab0118)
- ブロック [`00ab0118`](#insn-00ab0118) 範囲 `[['00ab0118', '00ab011b']]`
  - `FALL_THROUGH` [`00ab0118`](#insn-00ab0118) → [`00ab011c`](#insn-00ab011c)
- ブロック [`00ab011c`](#insn-00ab011c) 範囲 `[['00ab011c', '00ab0157']]`
  - `CONDITIONAL_JUMP` [`00ab0154`](#insn-00ab0154) → [`00ab0160`](#insn-00ab0160)
  - `FALL_THROUGH` [`00ab0154`](#insn-00ab0154) → [`00ab0158`](#insn-00ab0158)
- ブロック [`00ab0158`](#insn-00ab0158) 範囲 `[['00ab0158', '00ab015f']]`
  - `FALL_THROUGH` [`00ab015c`](#insn-00ab015c) → [`00ab0160`](#insn-00ab0160)
- ブロック [`00ab0160`](#insn-00ab0160) 範囲 `[['00ab0160', '00ab0177']]`
  - `UNCONDITIONAL_JUMP` [`00ab0174`](#insn-00ab0174) → [`00ab017c`](#insn-00ab017c)
- ブロック [`00ab0178`](#insn-00ab0178) 範囲 `[['00ab0178', '00ab017b']]`
  - `FALL_THROUGH` [`00ab0178`](#insn-00ab0178) → [`00ab017c`](#insn-00ab017c)
- ブロック [`00ab017c`](#insn-00ab017c) 範囲 `[['00ab017c', '00ab0187']]`
  - `CONDITIONAL_JUMP` [`00ab0184`](#insn-00ab0184) → [`00ab019c`](#insn-00ab019c)
  - `FALL_THROUGH` [`00ab0184`](#insn-00ab0184) → [`00ab0188`](#insn-00ab0188)
- ブロック [`00ab0188`](#insn-00ab0188) 範囲 `[['00ab0188', '00ab018f']]`
  - `UNCONDITIONAL_JUMP` [`00ab018c`](#insn-00ab018c) → [`00ab01c0`](#insn-00ab01c0)
- ブロック [`00ab0190`](#insn-00ab0190) 範囲 `[['00ab0190', '00ab019b']]`
  - `CONDITIONAL_JUMP` [`00ab0198`](#insn-00ab0198) → [`00ab01c0`](#insn-00ab01c0)
  - `FALL_THROUGH` [`00ab0198`](#insn-00ab0198) → [`00ab019c`](#insn-00ab019c)
- ブロック [`00ab019c`](#insn-00ab019c) 範囲 `[['00ab019c', '00ab01ab']]`
  - `CONDITIONAL_JUMP` [`00ab01a8`](#insn-00ab01a8) → [`00ab0190`](#insn-00ab0190)
  - `FALL_THROUGH` [`00ab01a8`](#insn-00ab01a8) → [`00ab01ac`](#insn-00ab01ac)
- ブロック [`00ab01ac`](#insn-00ab01ac) 範囲 `[['00ab01ac', '00ab01b3']]`
  - `CONDITIONAL_JUMP` [`00ab01b0`](#insn-00ab01b0) → [`00ab01fc`](#insn-00ab01fc)
  - `FALL_THROUGH` [`00ab01b0`](#insn-00ab01b0) → [`00ab01b4`](#insn-00ab01b4)
- ブロック [`00ab01b4`](#insn-00ab01b4) 範囲 `[['00ab01b4', '00ab01bb']]`
  - `CONDITIONAL_JUMP` [`00ab01b8`](#insn-00ab01b8) → [`00ab019c`](#insn-00ab019c)
  - `FALL_THROUGH` [`00ab01b8`](#insn-00ab01b8) → [`00ab01bc`](#insn-00ab01bc)
- ブロック [`00ab01bc`](#insn-00ab01bc) 範囲 `[['00ab01bc', '00ab01bf']]`
  - `FALL_THROUGH` [`00ab01bc`](#insn-00ab01bc) → [`00ab01c0`](#insn-00ab01c0)
- ブロック [`00ab01c0`](#insn-00ab01c0) 範囲 `[['00ab01c0', '00ab01ef']]`
  - `CONDITIONAL_JUMP` [`00ab01ec`](#insn-00ab01ec) → [`00ab00ac`](#insn-00ab00ac)
  - `FALL_THROUGH` [`00ab01ec`](#insn-00ab01ec) → [`00ab01f0`](#insn-00ab01f0)
- ブロック [`00ab01f0`](#insn-00ab01f0) 範囲 `[['00ab01f0', '00ab01fb']]`
  - `UNCONDITIONAL_JUMP` [`00ab01f8`](#insn-00ab01f8) → [`00ab00ac`](#insn-00ab00ac)
- ブロック [`00ab01fc`](#insn-00ab01fc) 範囲 `[['00ab01fc', '00ab0207']]`
  - `CONDITIONAL_JUMP` [`00ab0204`](#insn-00ab0204) → [`00ab00c8`](#insn-00ab00c8)
  - `FALL_THROUGH` [`00ab0204`](#insn-00ab0204) → [`00ab0208`](#insn-00ab0208)
- ブロック [`00ab0208`](#insn-00ab0208) 範囲 `[['00ab0208', '00ab0213']]`
  - `CONDITIONAL_JUMP` [`00ab0210`](#insn-00ab0210) → [`00ab021c`](#insn-00ab021c)
  - `FALL_THROUGH` [`00ab0210`](#insn-00ab0210) → [`00ab0214`](#insn-00ab0214)
- ブロック [`00ab0214`](#insn-00ab0214) 範囲 `[['00ab0214', '00ab021b']]`
  - `UNCONDITIONAL_JUMP` [`00ab0218`](#insn-00ab0218) → [`00ab02a4`](#insn-00ab02a4)
- ブロック [`00ab021c`](#insn-00ab021c) 範囲 `[['00ab021c', '00ab0233']]`
  - `CONDITIONAL_JUMP` [`00ab0230`](#insn-00ab0230) → [`00ab0d70`](#insn-00ab0d70)
  - `FALL_THROUGH` [`00ab0230`](#insn-00ab0230) → [`00ab0234`](#insn-00ab0234)
- ブロック [`00ab0234`](#insn-00ab0234) 範囲 `[['00ab0234', '00ab0257']]`
  - `CONDITIONAL_JUMP` [`00ab0254`](#insn-00ab0254) → [`00ab0270`](#insn-00ab0270)
  - `FALL_THROUGH` [`00ab0254`](#insn-00ab0254) → [`00ab0258`](#insn-00ab0258)
- ブロック [`00ab0258`](#insn-00ab0258) 範囲 `[['00ab0258', '00ab025f']]`
  - `CONDITIONAL_JUMP` [`00ab025c`](#insn-00ab025c) → [`00ab0d8c`](#insn-00ab0d8c)
  - `FALL_THROUGH` [`00ab025c`](#insn-00ab025c) → [`00ab0260`](#insn-00ab0260)
- ブロック [`00ab0260`](#insn-00ab0260) 範囲 `[['00ab0260', '00ab026f']]`
  - `UNCONDITIONAL_JUMP` [`00ab026c`](#insn-00ab026c) → [`00ab0274`](#insn-00ab0274)
- ブロック [`00ab0270`](#insn-00ab0270) 範囲 `[['00ab0270', '00ab0273']]`
  - `FALL_THROUGH` [`00ab0270`](#insn-00ab0270) → [`00ab0274`](#insn-00ab0274)
- ブロック [`00ab0274`](#insn-00ab0274) 範囲 `[['00ab0274', '00ab029b']]`
  - `CONDITIONAL_JUMP` [`00ab0298`](#insn-00ab0298) → [`00ab02a4`](#insn-00ab02a4)
  - `FALL_THROUGH` [`00ab0298`](#insn-00ab0298) → [`00ab029c`](#insn-00ab029c)
- ブロック [`00ab029c`](#insn-00ab029c) 範囲 `[['00ab029c', '00ab02a3']]`
  - `FALL_THROUGH` [`00ab02a0`](#insn-00ab02a0) → [`00ab02a4`](#insn-00ab02a4)
- ブロック [`00ab02a4`](#insn-00ab02a4) 範囲 `[['00ab02a4', '00ab02a7']]`
  - `FALL_THROUGH` [`00ab02a4`](#insn-00ab02a4) → [`00ab02a8`](#insn-00ab02a8)
- ブロック [`00ab02a8`](#insn-00ab02a8) 範囲 `[['00ab02a8', '00ab02b3']]`
  - `CONDITIONAL_JUMP` [`00ab02b0`](#insn-00ab02b0) → [`00ab0d50`](#insn-00ab0d50)
  - `FALL_THROUGH` [`00ab02b0`](#insn-00ab02b0) → [`00ab02b4`](#insn-00ab02b4)
- ブロック [`00ab02b4`](#insn-00ab02b4) 範囲 `[['00ab02b4', '00ab02bf']]`
  - `CONDITIONAL_JUMP` [`00ab02bc`](#insn-00ab02bc) → [`00ab02c8`](#insn-00ab02c8)
  - `FALL_THROUGH` [`00ab02bc`](#insn-00ab02bc) → [`00ab02c0`](#insn-00ab02c0)
- ブロック [`00ab02c0`](#insn-00ab02c0) 範囲 `[['00ab02c0', '00ab02c7']]`
  - `UNCONDITIONAL_JUMP` [`00ab02c4`](#insn-00ab02c4) → [`00ab02f0`](#insn-00ab02f0)
- ブロック [`00ab02c8`](#insn-00ab02c8) 範囲 `[['00ab02c8', '00ab02cb']]`
  - `FALL_THROUGH` [`00ab02c8`](#insn-00ab02c8) → [`00ab02cc`](#insn-00ab02cc)
- ブロック [`00ab02cc`](#insn-00ab02cc) 範囲 `[['00ab02cc', '00ab02d7']]`
  - `CONDITIONAL_JUMP` [`00ab02d4`](#insn-00ab02d4) → [`00ab02e8`](#insn-00ab02e8)
  - `FALL_THROUGH` [`00ab02d4`](#insn-00ab02d4) → [`00ab02d8`](#insn-00ab02d8)
- ブロック [`00ab02d8`](#insn-00ab02d8) 範囲 `[['00ab02d8', '00ab02e7']]`
  - `CONDITIONAL_JUMP` [`00ab02e4`](#insn-00ab02e4) → [`00ab02cc`](#insn-00ab02cc)
  - `FALL_THROUGH` [`00ab02e4`](#insn-00ab02e4) → [`00ab02e8`](#insn-00ab02e8)
- ブロック [`00ab02e8`](#insn-00ab02e8) 範囲 `[['00ab02e8', '00ab02ef']]`
  - `FALL_THROUGH` [`00ab02ec`](#insn-00ab02ec) → [`00ab02f0`](#insn-00ab02f0)
- ブロック [`00ab02f0`](#insn-00ab02f0) 範囲 `[['00ab02f0', '00ab0303']]`
  - `CONDITIONAL_JUMP` [`00ab0300`](#insn-00ab0300) → [`00ab0664`](#insn-00ab0664)
  - `FALL_THROUGH` [`00ab0300`](#insn-00ab0300) → [`00ab0304`](#insn-00ab0304)
- ブロック [`00ab0304`](#insn-00ab0304) 範囲 `[['00ab0304', '00ab030b']]`
  - `CONDITIONAL_JUMP` [`00ab0308`](#insn-00ab0308) → [`00ab0708`](#insn-00ab0708)
  - `FALL_THROUGH` [`00ab0308`](#insn-00ab0308) → [`00ab030c`](#insn-00ab030c)
- ブロック [`00ab030c`](#insn-00ab030c) 範囲 `[['00ab030c', '00ab0317']]`
  - `UNCONDITIONAL_JUMP` [`00ab0314`](#insn-00ab0314) → [`00ab0338`](#insn-00ab0338)
- ブロック [`00ab0318`](#insn-00ab0318) 範囲 `[['00ab0318', '00ab032b']]`
  - `CONDITIONAL_JUMP` [`00ab0328`](#insn-00ab0328) → [`00ab070c`](#insn-00ab070c)
  - `FALL_THROUGH` [`00ab0328`](#insn-00ab0328) → [`00ab032c`](#insn-00ab032c)
- ブロック [`00ab032c`](#insn-00ab032c) 範囲 `[['00ab032c', '00ab0337']]`
  - `CONDITIONAL_JUMP` [`00ab0334`](#insn-00ab0334) → [`00ab070c`](#insn-00ab070c)
  - `FALL_THROUGH` [`00ab0334`](#insn-00ab0334) → [`00ab0338`](#insn-00ab0338)
- ブロック [`00ab0338`](#insn-00ab0338) 範囲 `[['00ab0338', '00ab034b']]`
  - `CONDITIONAL_JUMP` [`00ab0348`](#insn-00ab0348) → [`00ab032c`](#insn-00ab032c)
  - `FALL_THROUGH` [`00ab0348`](#insn-00ab0348) → [`00ab034c`](#insn-00ab034c)
- ブロック [`00ab034c`](#insn-00ab034c) 範囲 `[['00ab034c', '00ab037b']]`
  - `CONDITIONAL_JUMP` [`00ab0378`](#insn-00ab0378) → [`00ab0390`](#insn-00ab0390)
  - `FALL_THROUGH` [`00ab0378`](#insn-00ab0378) → [`00ab037c`](#insn-00ab037c)
- ブロック [`00ab037c`](#insn-00ab037c) 範囲 `[['00ab037c', '00ab0383']]`
  - `UNCONDITIONAL_JUMP` [`00ab0380`](#insn-00ab0380) → [`00ab03b0`](#insn-00ab03b0)
- ブロック [`00ab0384`](#insn-00ab0384) 範囲 `[['00ab0384', '00ab038f']]`
  - `CONDITIONAL_JUMP` [`00ab038c`](#insn-00ab038c) → [`00ab03b0`](#insn-00ab03b0)
  - `FALL_THROUGH` [`00ab038c`](#insn-00ab038c) → [`00ab0390`](#insn-00ab0390)
- ブロック [`00ab0390`](#insn-00ab0390) 範囲 `[['00ab0390', '00ab039f']]`
  - `CONDITIONAL_JUMP` [`00ab039c`](#insn-00ab039c) → [`00ab0384`](#insn-00ab0384)
  - `FALL_THROUGH` [`00ab039c`](#insn-00ab039c) → [`00ab03a0`](#insn-00ab03a0)
- ブロック [`00ab03a0`](#insn-00ab03a0) 範囲 `[['00ab03a0', '00ab03a3']]`
  - `CONDITIONAL_JUMP` [`00ab03a0`](#insn-00ab03a0) → [`00ab040c`](#insn-00ab040c)
  - `FALL_THROUGH` [`00ab03a0`](#insn-00ab03a0) → [`00ab03a4`](#insn-00ab03a4)
- ブロック [`00ab03a4`](#insn-00ab03a4) 範囲 `[['00ab03a4', '00ab03ab']]`
  - `CONDITIONAL_JUMP` [`00ab03a8`](#insn-00ab03a8) → [`00ab0390`](#insn-00ab0390)
  - `FALL_THROUGH` [`00ab03a8`](#insn-00ab03a8) → [`00ab03ac`](#insn-00ab03ac)
- ブロック [`00ab03ac`](#insn-00ab03ac) 範囲 `[['00ab03ac', '00ab03af']]`
  - `FALL_THROUGH` [`00ab03ac`](#insn-00ab03ac) → [`00ab03b0`](#insn-00ab03b0)
- ブロック [`00ab03b0`](#insn-00ab03b0) 範囲 `[['00ab03b0', '00ab03eb']]`
  - `CONDITIONAL_JUMP` [`00ab03e8`](#insn-00ab03e8) → [`00ab03f4`](#insn-00ab03f4)
  - `FALL_THROUGH` [`00ab03e8`](#insn-00ab03e8) → [`00ab03ec`](#insn-00ab03ec)
- ブロック [`00ab03ec`](#insn-00ab03ec) 範囲 `[['00ab03ec', '00ab03f3']]`
  - `FALL_THROUGH` [`00ab03f0`](#insn-00ab03f0) → [`00ab03f4`](#insn-00ab03f4)
- ブロック [`00ab03f4`](#insn-00ab03f4) 範囲 `[['00ab03f4', '00ab040b']]`
  - `UNCONDITIONAL_JUMP` [`00ab0408`](#insn-00ab0408) → [`00ab0410`](#insn-00ab0410)
- ブロック [`00ab040c`](#insn-00ab040c) 範囲 `[['00ab040c', '00ab040f']]`
  - `FALL_THROUGH` [`00ab040c`](#insn-00ab040c) → [`00ab0410`](#insn-00ab0410)
- ブロック [`00ab0410`](#insn-00ab0410) 範囲 `[['00ab0410', '00ab041b']]`
  - `CONDITIONAL_JUMP` [`00ab0418`](#insn-00ab0418) → [`00ab0430`](#insn-00ab0430)
  - `FALL_THROUGH` [`00ab0418`](#insn-00ab0418) → [`00ab041c`](#insn-00ab041c)
- ブロック [`00ab041c`](#insn-00ab041c) 範囲 `[['00ab041c', '00ab0423']]`
  - `UNCONDITIONAL_JUMP` [`00ab0420`](#insn-00ab0420) → [`00ab0454`](#insn-00ab0454)
- ブロック [`00ab0424`](#insn-00ab0424) 範囲 `[['00ab0424', '00ab042f']]`
  - `CONDITIONAL_JUMP` [`00ab042c`](#insn-00ab042c) → [`00ab0454`](#insn-00ab0454)
  - `FALL_THROUGH` [`00ab042c`](#insn-00ab042c) → [`00ab0430`](#insn-00ab0430)
- ブロック [`00ab0430`](#insn-00ab0430) 範囲 `[['00ab0430', '00ab043f']]`
  - `CONDITIONAL_JUMP` [`00ab043c`](#insn-00ab043c) → [`00ab0424`](#insn-00ab0424)
  - `FALL_THROUGH` [`00ab043c`](#insn-00ab043c) → [`00ab0440`](#insn-00ab0440)
- ブロック [`00ab0440`](#insn-00ab0440) 範囲 `[['00ab0440', '00ab0447']]`
  - `CONDITIONAL_JUMP` [`00ab0444`](#insn-00ab0444) → [`00ab04ac`](#insn-00ab04ac)
  - `FALL_THROUGH` [`00ab0444`](#insn-00ab0444) → [`00ab0448`](#insn-00ab0448)
- ブロック [`00ab0448`](#insn-00ab0448) 範囲 `[['00ab0448', '00ab044f']]`
  - `CONDITIONAL_JUMP` [`00ab044c`](#insn-00ab044c) → [`00ab0430`](#insn-00ab0430)
  - `FALL_THROUGH` [`00ab044c`](#insn-00ab044c) → [`00ab0450`](#insn-00ab0450)
- ブロック [`00ab0450`](#insn-00ab0450) 範囲 `[['00ab0450', '00ab0453']]`
  - `FALL_THROUGH` [`00ab0450`](#insn-00ab0450) → [`00ab0454`](#insn-00ab0454)
- ブロック [`00ab0454`](#insn-00ab0454) 範囲 `[['00ab0454', '00ab0483']]`
  - `CONDITIONAL_JUMP` [`00ab0480`](#insn-00ab0480) → [`00ab048c`](#insn-00ab048c)
  - `FALL_THROUGH` [`00ab0480`](#insn-00ab0480) → [`00ab0484`](#insn-00ab0484)
- ブロック [`00ab0484`](#insn-00ab0484) 範囲 `[['00ab0484', '00ab048b']]`
  - `FALL_THROUGH` [`00ab0488`](#insn-00ab0488) → [`00ab048c`](#insn-00ab048c)
- ブロック [`00ab048c`](#insn-00ab048c) 範囲 `[['00ab048c', '00ab04a7']]`
  - `CONDITIONAL_JUMP` [`00ab04a4`](#insn-00ab04a4) → [`00ab032c`](#insn-00ab032c)
  - `FALL_THROUGH` [`00ab04a4`](#insn-00ab04a4) → [`00ab04a8`](#insn-00ab04a8)
- ブロック [`00ab04a8`](#insn-00ab04a8) 範囲 `[['00ab04a8', '00ab04ab']]`
  - `UNCONDITIONAL_JUMP` [`00ab04a8`](#insn-00ab04a8) → [`00ab04b8`](#insn-00ab04b8)
- ブロック [`00ab04ac`](#insn-00ab04ac) 範囲 `[['00ab04ac', '00ab04b7']]`
  - `CONDITIONAL_JUMP` [`00ab04b4`](#insn-00ab04b4) → [`00ab032c`](#insn-00ab032c)
  - `FALL_THROUGH` [`00ab04b4`](#insn-00ab04b4) → [`00ab04b8`](#insn-00ab04b8)
- ブロック [`00ab04b8`](#insn-00ab04b8) 範囲 `[['00ab04b8', '00ab04c7']]`
  - `CONDITIONAL_JUMP` [`00ab04c4`](#insn-00ab04c4) → [`00ab04f0`](#insn-00ab04f0)
  - `FALL_THROUGH` [`00ab04c4`](#insn-00ab04c4) → [`00ab04c8`](#insn-00ab04c8)
- ブロック [`00ab04c8`](#insn-00ab04c8) 範囲 `[['00ab04c8', '00ab04d7']]`
  - `CONDITIONAL_JUMP` [`00ab04d4`](#insn-00ab04d4) → [`00ab04f0`](#insn-00ab04f0)
  - `FALL_THROUGH` [`00ab04d4`](#insn-00ab04d4) → [`00ab04d8`](#insn-00ab04d8)
- ブロック [`00ab04d8`](#insn-00ab04d8) 範囲 `[['00ab04d8', '00ab04ef']]`
  - `CONDITIONAL_JUMP` [`00ab04ec`](#insn-00ab04ec) → [`00ab032c`](#insn-00ab032c)
  - `FALL_THROUGH` [`00ab04ec`](#insn-00ab04ec) → [`00ab04f0`](#insn-00ab04f0)
- ブロック [`00ab04f0`](#insn-00ab04f0) 範囲 `[['00ab04f0', '00ab0503']]`
  - `CONDITIONAL_JUMP` [`00ab0500`](#insn-00ab0500) → [`00ab0518`](#insn-00ab0518)
  - `FALL_THROUGH` [`00ab0500`](#insn-00ab0500) → [`00ab0504`](#insn-00ab0504)
- ブロック [`00ab0504`](#insn-00ab0504) 範囲 `[['00ab0504', '00ab050b']]`
  - `UNCONDITIONAL_JUMP` [`00ab0508`](#insn-00ab0508) → [`00ab0538`](#insn-00ab0538)
- ブロック [`00ab050c`](#insn-00ab050c) 範囲 `[['00ab050c', '00ab0517']]`
  - `CONDITIONAL_JUMP` [`00ab0514`](#insn-00ab0514) → [`00ab0538`](#insn-00ab0538)
  - `FALL_THROUGH` [`00ab0514`](#insn-00ab0514) → [`00ab0518`](#insn-00ab0518)
- ブロック [`00ab0518`](#insn-00ab0518) 範囲 `[['00ab0518', '00ab0527']]`
  - `CONDITIONAL_JUMP` [`00ab0524`](#insn-00ab0524) → [`00ab050c`](#insn-00ab050c)
  - `FALL_THROUGH` [`00ab0524`](#insn-00ab0524) → [`00ab0528`](#insn-00ab0528)
- ブロック [`00ab0528`](#insn-00ab0528) 範囲 `[['00ab0528', '00ab052b']]`
  - `CONDITIONAL_JUMP` [`00ab0528`](#insn-00ab0528) → [`00ab0594`](#insn-00ab0594)
  - `FALL_THROUGH` [`00ab0528`](#insn-00ab0528) → [`00ab052c`](#insn-00ab052c)
- ブロック [`00ab052c`](#insn-00ab052c) 範囲 `[['00ab052c', '00ab0533']]`
  - `CONDITIONAL_JUMP` [`00ab0530`](#insn-00ab0530) → [`00ab0518`](#insn-00ab0518)
  - `FALL_THROUGH` [`00ab0530`](#insn-00ab0530) → [`00ab0534`](#insn-00ab0534)
- ブロック [`00ab0534`](#insn-00ab0534) 範囲 `[['00ab0534', '00ab0537']]`
  - `FALL_THROUGH` [`00ab0534`](#insn-00ab0534) → [`00ab0538`](#insn-00ab0538)
- ブロック [`00ab0538`](#insn-00ab0538) 範囲 `[['00ab0538', '00ab0573']]`
  - `CONDITIONAL_JUMP` [`00ab0570`](#insn-00ab0570) → [`00ab057c`](#insn-00ab057c)
  - `FALL_THROUGH` [`00ab0570`](#insn-00ab0570) → [`00ab0574`](#insn-00ab0574)
- ブロック [`00ab0574`](#insn-00ab0574) 範囲 `[['00ab0574', '00ab057b']]`
  - `FALL_THROUGH` [`00ab0578`](#insn-00ab0578) → [`00ab057c`](#insn-00ab057c)
- ブロック [`00ab057c`](#insn-00ab057c) 範囲 `[['00ab057c', '00ab0593']]`
  - `UNCONDITIONAL_JUMP` [`00ab0590`](#insn-00ab0590) → [`00ab0598`](#insn-00ab0598)
- ブロック [`00ab0594`](#insn-00ab0594) 範囲 `[['00ab0594', '00ab0597']]`
  - `FALL_THROUGH` [`00ab0594`](#insn-00ab0594) → [`00ab0598`](#insn-00ab0598)
- ブロック [`00ab0598`](#insn-00ab0598) 範囲 `[['00ab0598', '00ab05a3']]`
  - `CONDITIONAL_JUMP` [`00ab05a0`](#insn-00ab05a0) → [`00ab05b8`](#insn-00ab05b8)
  - `FALL_THROUGH` [`00ab05a0`](#insn-00ab05a0) → [`00ab05a4`](#insn-00ab05a4)
- ブロック [`00ab05a4`](#insn-00ab05a4) 範囲 `[['00ab05a4', '00ab05ab']]`
  - `UNCONDITIONAL_JUMP` [`00ab05a8`](#insn-00ab05a8) → [`00ab05dc`](#insn-00ab05dc)
- ブロック [`00ab05ac`](#insn-00ab05ac) 範囲 `[['00ab05ac', '00ab05b7']]`
  - `CONDITIONAL_JUMP` [`00ab05b4`](#insn-00ab05b4) → [`00ab05dc`](#insn-00ab05dc)
  - `FALL_THROUGH` [`00ab05b4`](#insn-00ab05b4) → [`00ab05b8`](#insn-00ab05b8)
- ブロック [`00ab05b8`](#insn-00ab05b8) 範囲 `[['00ab05b8', '00ab05c7']]`
  - `CONDITIONAL_JUMP` [`00ab05c4`](#insn-00ab05c4) → [`00ab05ac`](#insn-00ab05ac)
  - `FALL_THROUGH` [`00ab05c4`](#insn-00ab05c4) → [`00ab05c8`](#insn-00ab05c8)
- ブロック [`00ab05c8`](#insn-00ab05c8) 範囲 `[['00ab05c8', '00ab05cf']]`
  - `CONDITIONAL_JUMP` [`00ab05cc`](#insn-00ab05cc) → [`00ab062c`](#insn-00ab062c)
  - `FALL_THROUGH` [`00ab05cc`](#insn-00ab05cc) → [`00ab05d0`](#insn-00ab05d0)
- ブロック [`00ab05d0`](#insn-00ab05d0) 範囲 `[['00ab05d0', '00ab05d7']]`
  - `CONDITIONAL_JUMP` [`00ab05d4`](#insn-00ab05d4) → [`00ab05b8`](#insn-00ab05b8)
  - `FALL_THROUGH` [`00ab05d4`](#insn-00ab05d4) → [`00ab05d8`](#insn-00ab05d8)
- ブロック [`00ab05d8`](#insn-00ab05d8) 範囲 `[['00ab05d8', '00ab05db']]`
  - `FALL_THROUGH` [`00ab05d8`](#insn-00ab05d8) → [`00ab05dc`](#insn-00ab05dc)
- ブロック [`00ab05dc`](#insn-00ab05dc) 範囲 `[['00ab05dc', '00ab060b']]`
  - `CONDITIONAL_JUMP` [`00ab0608`](#insn-00ab0608) → [`00ab0614`](#insn-00ab0614)
  - `FALL_THROUGH` [`00ab0608`](#insn-00ab0608) → [`00ab060c`](#insn-00ab060c)
- ブロック [`00ab060c`](#insn-00ab060c) 範囲 `[['00ab060c', '00ab0613']]`
  - `FALL_THROUGH` [`00ab0610`](#insn-00ab0610) → [`00ab0614`](#insn-00ab0614)
- ブロック [`00ab0614`](#insn-00ab0614) 範囲 `[['00ab0614', '00ab062b']]`
  - `UNCONDITIONAL_JUMP` [`00ab0628`](#insn-00ab0628) → [`00ab0630`](#insn-00ab0630)
- ブロック [`00ab062c`](#insn-00ab062c) 範囲 `[['00ab062c', '00ab062f']]`
  - `FALL_THROUGH` [`00ab062c`](#insn-00ab062c) → [`00ab0630`](#insn-00ab0630)
- ブロック [`00ab0630`](#insn-00ab0630) 範囲 `[['00ab0630', '00ab064f']]`
  - `CONDITIONAL_JUMP` [`00ab064c`](#insn-00ab064c) → [`00ab0318`](#insn-00ab0318)
  - `FALL_THROUGH` [`00ab064c`](#insn-00ab064c) → [`00ab0650`](#insn-00ab0650)
- ブロック [`00ab0650`](#insn-00ab0650) 範囲 `[['00ab0650', '00ab0663']]`
  - `UNCONDITIONAL_JUMP` [`00ab0660`](#insn-00ab0660) → [`00ab0318`](#insn-00ab0318)
- ブロック [`00ab0664`](#insn-00ab0664) 範囲 `[['00ab0664', '00ab0677']]`
  - `CONDITIONAL_JUMP` [`00ab0674`](#insn-00ab0674) → [`00ab068c`](#insn-00ab068c)
  - `FALL_THROUGH` [`00ab0674`](#insn-00ab0674) → [`00ab0678`](#insn-00ab0678)
- ブロック [`00ab0678`](#insn-00ab0678) 範囲 `[['00ab0678', '00ab067f']]`
  - `UNCONDITIONAL_JUMP` [`00ab067c`](#insn-00ab067c) → [`00ab06ac`](#insn-00ab06ac)
- ブロック [`00ab0680`](#insn-00ab0680) 範囲 `[['00ab0680', '00ab068b']]`
  - `CONDITIONAL_JUMP` [`00ab0688`](#insn-00ab0688) → [`00ab06ac`](#insn-00ab06ac)
  - `FALL_THROUGH` [`00ab0688`](#insn-00ab0688) → [`00ab068c`](#insn-00ab068c)
- ブロック [`00ab068c`](#insn-00ab068c) 範囲 `[['00ab068c', '00ab069b']]`
  - `CONDITIONAL_JUMP` [`00ab0698`](#insn-00ab0698) → [`00ab0680`](#insn-00ab0680)
  - `FALL_THROUGH` [`00ab0698`](#insn-00ab0698) → [`00ab069c`](#insn-00ab069c)
- ブロック [`00ab069c`](#insn-00ab069c) 範囲 `[['00ab069c', '00ab069f']]`
  - `CONDITIONAL_JUMP` [`00ab069c`](#insn-00ab069c) → [`00ab0a6c`](#insn-00ab0a6c)
  - `FALL_THROUGH` [`00ab069c`](#insn-00ab069c) → [`00ab06a0`](#insn-00ab06a0)
- ブロック [`00ab06a0`](#insn-00ab06a0) 範囲 `[['00ab06a0', '00ab06a7']]`
  - `CONDITIONAL_JUMP` [`00ab06a4`](#insn-00ab06a4) → [`00ab068c`](#insn-00ab068c)
  - `FALL_THROUGH` [`00ab06a4`](#insn-00ab06a4) → [`00ab06a8`](#insn-00ab06a8)
- ブロック [`00ab06a8`](#insn-00ab06a8) 範囲 `[['00ab06a8', '00ab06ab']]`
  - `FALL_THROUGH` [`00ab06a8`](#insn-00ab06a8) → [`00ab06ac`](#insn-00ab06ac)
- ブロック [`00ab06ac`](#insn-00ab06ac) 範囲 `[['00ab06ac', '00ab06e7']]`
  - `CONDITIONAL_JUMP` [`00ab06e4`](#insn-00ab06e4) → [`00ab06f0`](#insn-00ab06f0)
  - `FALL_THROUGH` [`00ab06e4`](#insn-00ab06e4) → [`00ab06e8`](#insn-00ab06e8)
- ブロック [`00ab06e8`](#insn-00ab06e8) 範囲 `[['00ab06e8', '00ab06ef']]`
  - `FALL_THROUGH` [`00ab06ec`](#insn-00ab06ec) → [`00ab06f0`](#insn-00ab06f0)
- ブロック [`00ab06f0`](#insn-00ab06f0) 範囲 `[['00ab06f0', '00ab0707']]`
  - `UNCONDITIONAL_JUMP` [`00ab0704`](#insn-00ab0704) → [`00ab0a70`](#insn-00ab0a70)
- ブロック [`00ab0708`](#insn-00ab0708) 範囲 `[['00ab0708', '00ab070b']]`
  - `FALL_THROUGH` [`00ab0708`](#insn-00ab0708) → [`00ab070c`](#insn-00ab070c)
- ブロック [`00ab070c`](#insn-00ab070c) 範囲 `[['00ab070c', '00ab071b']]`
  - `CONDITIONAL_JUMP` [`00ab0718`](#insn-00ab0718) → [`00ab0cc4`](#insn-00ab0cc4)
  - `FALL_THROUGH` [`00ab0718`](#insn-00ab0718) → [`00ab071c`](#insn-00ab071c)
- ブロック [`00ab071c`](#insn-00ab071c) 範囲 `[['00ab071c', '00ab0727']]`
  - `CONDITIONAL_JUMP` [`00ab0724`](#insn-00ab0724) → [`00ab0cc8`](#insn-00ab0cc8)
  - `FALL_THROUGH` [`00ab0724`](#insn-00ab0724) → [`00ab0728`](#insn-00ab0728)
- ブロック [`00ab0728`](#insn-00ab0728) 範囲 `[['00ab0728', '00ab072f']]`
  - `CONDITIONAL_JUMP` [`00ab072c`](#insn-00ab072c) → [`00ab0cc4`](#insn-00ab0cc4)
  - `FALL_THROUGH` [`00ab072c`](#insn-00ab072c) → [`00ab0730`](#insn-00ab0730)
- ブロック [`00ab0730`](#insn-00ab0730) 範囲 `[['00ab0730', '00ab0737']]`
  - `UNCONDITIONAL_JUMP` [`00ab0734`](#insn-00ab0734) → [`00ab0754`](#insn-00ab0754)
- ブロック [`00ab0738`](#insn-00ab0738) 範囲 `[['00ab0738', '00ab0747']]`
  - `CONDITIONAL_JUMP` [`00ab0744`](#insn-00ab0744) → [`00ab0cc8`](#insn-00ab0cc8)
  - `FALL_THROUGH` [`00ab0744`](#insn-00ab0744) → [`00ab0748`](#insn-00ab0748)
- ブロック [`00ab0748`](#insn-00ab0748) 範囲 `[['00ab0748', '00ab0753']]`
  - `CONDITIONAL_JUMP` [`00ab0750`](#insn-00ab0750) → [`00ab0cc4`](#insn-00ab0cc4)
  - `FALL_THROUGH` [`00ab0750`](#insn-00ab0750) → [`00ab0754`](#insn-00ab0754)
- ブロック [`00ab0754`](#insn-00ab0754) 範囲 `[['00ab0754', '00ab0783']]`
  - `CONDITIONAL_JUMP` [`00ab0780`](#insn-00ab0780) → [`00ab0798`](#insn-00ab0798)
  - `FALL_THROUGH` [`00ab0780`](#insn-00ab0780) → [`00ab0784`](#insn-00ab0784)
- ブロック [`00ab0784`](#insn-00ab0784) 範囲 `[['00ab0784', '00ab078b']]`
  - `UNCONDITIONAL_JUMP` [`00ab0788`](#insn-00ab0788) → [`00ab07b8`](#insn-00ab07b8)
- ブロック [`00ab078c`](#insn-00ab078c) 範囲 `[['00ab078c', '00ab0797']]`
  - `CONDITIONAL_JUMP` [`00ab0794`](#insn-00ab0794) → [`00ab07b8`](#insn-00ab07b8)
  - `FALL_THROUGH` [`00ab0794`](#insn-00ab0794) → [`00ab0798`](#insn-00ab0798)
- ブロック [`00ab0798`](#insn-00ab0798) 範囲 `[['00ab0798', '00ab07a7']]`
  - `CONDITIONAL_JUMP` [`00ab07a4`](#insn-00ab07a4) → [`00ab078c`](#insn-00ab078c)
  - `FALL_THROUGH` [`00ab07a4`](#insn-00ab07a4) → [`00ab07a8`](#insn-00ab07a8)
- ブロック [`00ab07a8`](#insn-00ab07a8) 範囲 `[['00ab07a8', '00ab07ab']]`
  - `CONDITIONAL_JUMP` [`00ab07a8`](#insn-00ab07a8) → [`00ab0814`](#insn-00ab0814)
  - `FALL_THROUGH` [`00ab07a8`](#insn-00ab07a8) → [`00ab07ac`](#insn-00ab07ac)
- ブロック [`00ab07ac`](#insn-00ab07ac) 範囲 `[['00ab07ac', '00ab07b3']]`
  - `CONDITIONAL_JUMP` [`00ab07b0`](#insn-00ab07b0) → [`00ab0798`](#insn-00ab0798)
  - `FALL_THROUGH` [`00ab07b0`](#insn-00ab07b0) → [`00ab07b4`](#insn-00ab07b4)
- ブロック [`00ab07b4`](#insn-00ab07b4) 範囲 `[['00ab07b4', '00ab07b7']]`
  - `FALL_THROUGH` [`00ab07b4`](#insn-00ab07b4) → [`00ab07b8`](#insn-00ab07b8)
- ブロック [`00ab07b8`](#insn-00ab07b8) 範囲 `[['00ab07b8', '00ab07f3']]`
  - `CONDITIONAL_JUMP` [`00ab07f0`](#insn-00ab07f0) → [`00ab07fc`](#insn-00ab07fc)
  - `FALL_THROUGH` [`00ab07f0`](#insn-00ab07f0) → [`00ab07f4`](#insn-00ab07f4)
- ブロック [`00ab07f4`](#insn-00ab07f4) 範囲 `[['00ab07f4', '00ab07fb']]`
  - `FALL_THROUGH` [`00ab07f8`](#insn-00ab07f8) → [`00ab07fc`](#insn-00ab07fc)
- ブロック [`00ab07fc`](#insn-00ab07fc) 範囲 `[['00ab07fc', '00ab0813']]`
  - `UNCONDITIONAL_JUMP` [`00ab0810`](#insn-00ab0810) → [`00ab0818`](#insn-00ab0818)
- ブロック [`00ab0814`](#insn-00ab0814) 範囲 `[['00ab0814', '00ab0817']]`
  - `FALL_THROUGH` [`00ab0814`](#insn-00ab0814) → [`00ab0818`](#insn-00ab0818)
- ブロック [`00ab0818`](#insn-00ab0818) 範囲 `[['00ab0818', '00ab0823']]`
  - `CONDITIONAL_JUMP` [`00ab0820`](#insn-00ab0820) → [`00ab0838`](#insn-00ab0838)
  - `FALL_THROUGH` [`00ab0820`](#insn-00ab0820) → [`00ab0824`](#insn-00ab0824)
- ブロック [`00ab0824`](#insn-00ab0824) 範囲 `[['00ab0824', '00ab082b']]`
  - `UNCONDITIONAL_JUMP` [`00ab0828`](#insn-00ab0828) → [`00ab085c`](#insn-00ab085c)
- ブロック [`00ab082c`](#insn-00ab082c) 範囲 `[['00ab082c', '00ab0837']]`
  - `CONDITIONAL_JUMP` [`00ab0834`](#insn-00ab0834) → [`00ab085c`](#insn-00ab085c)
  - `FALL_THROUGH` [`00ab0834`](#insn-00ab0834) → [`00ab0838`](#insn-00ab0838)
- ブロック [`00ab0838`](#insn-00ab0838) 範囲 `[['00ab0838', '00ab0847']]`
  - `CONDITIONAL_JUMP` [`00ab0844`](#insn-00ab0844) → [`00ab082c`](#insn-00ab082c)
  - `FALL_THROUGH` [`00ab0844`](#insn-00ab0844) → [`00ab0848`](#insn-00ab0848)
- ブロック [`00ab0848`](#insn-00ab0848) 範囲 `[['00ab0848', '00ab084f']]`
  - `CONDITIONAL_JUMP` [`00ab084c`](#insn-00ab084c) → [`00ab08b4`](#insn-00ab08b4)
  - `FALL_THROUGH` [`00ab084c`](#insn-00ab084c) → [`00ab0850`](#insn-00ab0850)
- ブロック [`00ab0850`](#insn-00ab0850) 範囲 `[['00ab0850', '00ab0857']]`
  - `CONDITIONAL_JUMP` [`00ab0854`](#insn-00ab0854) → [`00ab0838`](#insn-00ab0838)
  - `FALL_THROUGH` [`00ab0854`](#insn-00ab0854) → [`00ab0858`](#insn-00ab0858)
- ブロック [`00ab0858`](#insn-00ab0858) 範囲 `[['00ab0858', '00ab085b']]`
  - `FALL_THROUGH` [`00ab0858`](#insn-00ab0858) → [`00ab085c`](#insn-00ab085c)
- ブロック [`00ab085c`](#insn-00ab085c) 範囲 `[['00ab085c', '00ab088b']]`
  - `CONDITIONAL_JUMP` [`00ab0888`](#insn-00ab0888) → [`00ab0894`](#insn-00ab0894)
  - `FALL_THROUGH` [`00ab0888`](#insn-00ab0888) → [`00ab088c`](#insn-00ab088c)
- ブロック [`00ab088c`](#insn-00ab088c) 範囲 `[['00ab088c', '00ab0893']]`
  - `FALL_THROUGH` [`00ab0890`](#insn-00ab0890) → [`00ab0894`](#insn-00ab0894)
- ブロック [`00ab0894`](#insn-00ab0894) 範囲 `[['00ab0894', '00ab08af']]`
  - `CONDITIONAL_JUMP` [`00ab08ac`](#insn-00ab08ac) → [`00ab0748`](#insn-00ab0748)
  - `FALL_THROUGH` [`00ab08ac`](#insn-00ab08ac) → [`00ab08b0`](#insn-00ab08b0)
- ブロック [`00ab08b0`](#insn-00ab08b0) 範囲 `[['00ab08b0', '00ab08b3']]`
  - `UNCONDITIONAL_JUMP` [`00ab08b0`](#insn-00ab08b0) → [`00ab08c0`](#insn-00ab08c0)
- ブロック [`00ab08b4`](#insn-00ab08b4) 範囲 `[['00ab08b4', '00ab08bf']]`
  - `CONDITIONAL_JUMP` [`00ab08bc`](#insn-00ab08bc) → [`00ab0748`](#insn-00ab0748)
  - `FALL_THROUGH` [`00ab08bc`](#insn-00ab08bc) → [`00ab08c0`](#insn-00ab08c0)
- ブロック [`00ab08c0`](#insn-00ab08c0) 範囲 `[['00ab08c0', '00ab08cf']]`
  - `CONDITIONAL_JUMP` [`00ab08cc`](#insn-00ab08cc) → [`00ab08f8`](#insn-00ab08f8)
  - `FALL_THROUGH` [`00ab08cc`](#insn-00ab08cc) → [`00ab08d0`](#insn-00ab08d0)
- ブロック [`00ab08d0`](#insn-00ab08d0) 範囲 `[['00ab08d0', '00ab08df']]`
  - `CONDITIONAL_JUMP` [`00ab08dc`](#insn-00ab08dc) → [`00ab08f8`](#insn-00ab08f8)
  - `FALL_THROUGH` [`00ab08dc`](#insn-00ab08dc) → [`00ab08e0`](#insn-00ab08e0)
- ブロック [`00ab08e0`](#insn-00ab08e0) 範囲 `[['00ab08e0', '00ab08f7']]`
  - `CONDITIONAL_JUMP` [`00ab08f4`](#insn-00ab08f4) → [`00ab0748`](#insn-00ab0748)
  - `FALL_THROUGH` [`00ab08f4`](#insn-00ab08f4) → [`00ab08f8`](#insn-00ab08f8)
- ブロック [`00ab08f8`](#insn-00ab08f8) 範囲 `[['00ab08f8', '00ab090b']]`
  - `CONDITIONAL_JUMP` [`00ab0908`](#insn-00ab0908) → [`00ab0920`](#insn-00ab0920)
  - `FALL_THROUGH` [`00ab0908`](#insn-00ab0908) → [`00ab090c`](#insn-00ab090c)
- ブロック [`00ab090c`](#insn-00ab090c) 範囲 `[['00ab090c', '00ab0913']]`
  - `UNCONDITIONAL_JUMP` [`00ab0910`](#insn-00ab0910) → [`00ab0940`](#insn-00ab0940)
- ブロック [`00ab0914`](#insn-00ab0914) 範囲 `[['00ab0914', '00ab091f']]`
  - `CONDITIONAL_JUMP` [`00ab091c`](#insn-00ab091c) → [`00ab0940`](#insn-00ab0940)
  - `FALL_THROUGH` [`00ab091c`](#insn-00ab091c) → [`00ab0920`](#insn-00ab0920)
- ブロック [`00ab0920`](#insn-00ab0920) 範囲 `[['00ab0920', '00ab092f']]`
  - `CONDITIONAL_JUMP` [`00ab092c`](#insn-00ab092c) → [`00ab0914`](#insn-00ab0914)
  - `FALL_THROUGH` [`00ab092c`](#insn-00ab092c) → [`00ab0930`](#insn-00ab0930)
- ブロック [`00ab0930`](#insn-00ab0930) 範囲 `[['00ab0930', '00ab0933']]`
  - `CONDITIONAL_JUMP` [`00ab0930`](#insn-00ab0930) → [`00ab099c`](#insn-00ab099c)
  - `FALL_THROUGH` [`00ab0930`](#insn-00ab0930) → [`00ab0934`](#insn-00ab0934)
- ブロック [`00ab0934`](#insn-00ab0934) 範囲 `[['00ab0934', '00ab093b']]`
  - `CONDITIONAL_JUMP` [`00ab0938`](#insn-00ab0938) → [`00ab0920`](#insn-00ab0920)
  - `FALL_THROUGH` [`00ab0938`](#insn-00ab0938) → [`00ab093c`](#insn-00ab093c)
- ブロック [`00ab093c`](#insn-00ab093c) 範囲 `[['00ab093c', '00ab093f']]`
  - `FALL_THROUGH` [`00ab093c`](#insn-00ab093c) → [`00ab0940`](#insn-00ab0940)
- ブロック [`00ab0940`](#insn-00ab0940) 範囲 `[['00ab0940', '00ab097b']]`
  - `CONDITIONAL_JUMP` [`00ab0978`](#insn-00ab0978) → [`00ab0984`](#insn-00ab0984)
  - `FALL_THROUGH` [`00ab0978`](#insn-00ab0978) → [`00ab097c`](#insn-00ab097c)
- ブロック [`00ab097c`](#insn-00ab097c) 範囲 `[['00ab097c', '00ab0983']]`
  - `FALL_THROUGH` [`00ab0980`](#insn-00ab0980) → [`00ab0984`](#insn-00ab0984)
- ブロック [`00ab0984`](#insn-00ab0984) 範囲 `[['00ab0984', '00ab099b']]`
  - `UNCONDITIONAL_JUMP` [`00ab0998`](#insn-00ab0998) → [`00ab09a0`](#insn-00ab09a0)
- ブロック [`00ab099c`](#insn-00ab099c) 範囲 `[['00ab099c', '00ab099f']]`
  - `FALL_THROUGH` [`00ab099c`](#insn-00ab099c) → [`00ab09a0`](#insn-00ab09a0)
- ブロック [`00ab09a0`](#insn-00ab09a0) 範囲 `[['00ab09a0', '00ab09ab']]`
  - `CONDITIONAL_JUMP` [`00ab09a8`](#insn-00ab09a8) → [`00ab09c0`](#insn-00ab09c0)
  - `FALL_THROUGH` [`00ab09a8`](#insn-00ab09a8) → [`00ab09ac`](#insn-00ab09ac)
- ブロック [`00ab09ac`](#insn-00ab09ac) 範囲 `[['00ab09ac', '00ab09b3']]`
  - `UNCONDITIONAL_JUMP` [`00ab09b0`](#insn-00ab09b0) → [`00ab09e4`](#insn-00ab09e4)
- ブロック [`00ab09b4`](#insn-00ab09b4) 範囲 `[['00ab09b4', '00ab09bf']]`
  - `CONDITIONAL_JUMP` [`00ab09bc`](#insn-00ab09bc) → [`00ab09e4`](#insn-00ab09e4)
  - `FALL_THROUGH` [`00ab09bc`](#insn-00ab09bc) → [`00ab09c0`](#insn-00ab09c0)
- ブロック [`00ab09c0`](#insn-00ab09c0) 範囲 `[['00ab09c0', '00ab09cf']]`
  - `CONDITIONAL_JUMP` [`00ab09cc`](#insn-00ab09cc) → [`00ab09b4`](#insn-00ab09b4)
  - `FALL_THROUGH` [`00ab09cc`](#insn-00ab09cc) → [`00ab09d0`](#insn-00ab09d0)
- ブロック [`00ab09d0`](#insn-00ab09d0) 範囲 `[['00ab09d0', '00ab09d7']]`
  - `CONDITIONAL_JUMP` [`00ab09d4`](#insn-00ab09d4) → [`00ab0a34`](#insn-00ab0a34)
  - `FALL_THROUGH` [`00ab09d4`](#insn-00ab09d4) → [`00ab09d8`](#insn-00ab09d8)
- ブロック [`00ab09d8`](#insn-00ab09d8) 範囲 `[['00ab09d8', '00ab09df']]`
  - `CONDITIONAL_JUMP` [`00ab09dc`](#insn-00ab09dc) → [`00ab09c0`](#insn-00ab09c0)
  - `FALL_THROUGH` [`00ab09dc`](#insn-00ab09dc) → [`00ab09e0`](#insn-00ab09e0)
- ブロック [`00ab09e0`](#insn-00ab09e0) 範囲 `[['00ab09e0', '00ab09e3']]`
  - `FALL_THROUGH` [`00ab09e0`](#insn-00ab09e0) → [`00ab09e4`](#insn-00ab09e4)
- ブロック [`00ab09e4`](#insn-00ab09e4) 範囲 `[['00ab09e4', '00ab0a13']]`
  - `CONDITIONAL_JUMP` [`00ab0a10`](#insn-00ab0a10) → [`00ab0a1c`](#insn-00ab0a1c)
  - `FALL_THROUGH` [`00ab0a10`](#insn-00ab0a10) → [`00ab0a14`](#insn-00ab0a14)
- ブロック [`00ab0a14`](#insn-00ab0a14) 範囲 `[['00ab0a14', '00ab0a1b']]`
  - `FALL_THROUGH` [`00ab0a18`](#insn-00ab0a18) → [`00ab0a1c`](#insn-00ab0a1c)
- ブロック [`00ab0a1c`](#insn-00ab0a1c) 範囲 `[['00ab0a1c', '00ab0a33']]`
  - `UNCONDITIONAL_JUMP` [`00ab0a30`](#insn-00ab0a30) → [`00ab0a38`](#insn-00ab0a38)
- ブロック [`00ab0a34`](#insn-00ab0a34) 範囲 `[['00ab0a34', '00ab0a37']]`
  - `FALL_THROUGH` [`00ab0a34`](#insn-00ab0a34) → [`00ab0a38`](#insn-00ab0a38)
- ブロック [`00ab0a38`](#insn-00ab0a38) 範囲 `[['00ab0a38', '00ab0a57']]`
  - `CONDITIONAL_JUMP` [`00ab0a54`](#insn-00ab0a54) → [`00ab0738`](#insn-00ab0738)
  - `FALL_THROUGH` [`00ab0a54`](#insn-00ab0a54) → [`00ab0a58`](#insn-00ab0a58)
- ブロック [`00ab0a58`](#insn-00ab0a58) 範囲 `[['00ab0a58', '00ab0a6b']]`
  - `UNCONDITIONAL_JUMP` [`00ab0a68`](#insn-00ab0a68) → [`00ab0738`](#insn-00ab0738)
- ブロック [`00ab0a6c`](#insn-00ab0a6c) 範囲 `[['00ab0a6c', '00ab0a6f']]`
  - `FALL_THROUGH` [`00ab0a6c`](#insn-00ab0a6c) → [`00ab0a70`](#insn-00ab0a70)
- ブロック [`00ab0a70`](#insn-00ab0a70) 範囲 `[['00ab0a70', '00ab0a7b']]`
  - `CONDITIONAL_JUMP` [`00ab0a78`](#insn-00ab0a78) → [`00ab0a90`](#insn-00ab0a90)
  - `FALL_THROUGH` [`00ab0a78`](#insn-00ab0a78) → [`00ab0a7c`](#insn-00ab0a7c)
- ブロック [`00ab0a7c`](#insn-00ab0a7c) 範囲 `[['00ab0a7c', '00ab0a83']]`
  - `UNCONDITIONAL_JUMP` [`00ab0a80`](#insn-00ab0a80) → [`00ab0ab4`](#insn-00ab0ab4)
- ブロック [`00ab0a84`](#insn-00ab0a84) 範囲 `[['00ab0a84', '00ab0a8f']]`
  - `CONDITIONAL_JUMP` [`00ab0a8c`](#insn-00ab0a8c) → [`00ab0ab4`](#insn-00ab0ab4)
  - `FALL_THROUGH` [`00ab0a8c`](#insn-00ab0a8c) → [`00ab0a90`](#insn-00ab0a90)
- ブロック [`00ab0a90`](#insn-00ab0a90) 範囲 `[['00ab0a90', '00ab0a9f']]`
  - `CONDITIONAL_JUMP` [`00ab0a9c`](#insn-00ab0a9c) → [`00ab0a84`](#insn-00ab0a84)
  - `FALL_THROUGH` [`00ab0a9c`](#insn-00ab0a9c) → [`00ab0aa0`](#insn-00ab0aa0)
- ブロック [`00ab0aa0`](#insn-00ab0aa0) 範囲 `[['00ab0aa0', '00ab0aa7']]`
  - `CONDITIONAL_JUMP` [`00ab0aa4`](#insn-00ab0aa4) → [`00ab0b10`](#insn-00ab0b10)
  - `FALL_THROUGH` [`00ab0aa4`](#insn-00ab0aa4) → [`00ab0aa8`](#insn-00ab0aa8)
- ブロック [`00ab0aa8`](#insn-00ab0aa8) 範囲 `[['00ab0aa8', '00ab0aaf']]`
  - `CONDITIONAL_JUMP` [`00ab0aac`](#insn-00ab0aac) → [`00ab0a90`](#insn-00ab0a90)
  - `FALL_THROUGH` [`00ab0aac`](#insn-00ab0aac) → [`00ab0ab0`](#insn-00ab0ab0)
- ブロック [`00ab0ab0`](#insn-00ab0ab0) 範囲 `[['00ab0ab0', '00ab0ab3']]`
  - `FALL_THROUGH` [`00ab0ab0`](#insn-00ab0ab0) → [`00ab0ab4`](#insn-00ab0ab4)
- ブロック [`00ab0ab4`](#insn-00ab0ab4) 範囲 `[['00ab0ab4', '00ab0ae7']]`
  - `CONDITIONAL_JUMP` [`00ab0ae4`](#insn-00ab0ae4) → [`00ab0af0`](#insn-00ab0af0)
  - `FALL_THROUGH` [`00ab0ae4`](#insn-00ab0ae4) → [`00ab0ae8`](#insn-00ab0ae8)
- ブロック [`00ab0ae8`](#insn-00ab0ae8) 範囲 `[['00ab0ae8', '00ab0aef']]`
  - `FALL_THROUGH` [`00ab0aec`](#insn-00ab0aec) → [`00ab0af0`](#insn-00ab0af0)
- ブロック [`00ab0af0`](#insn-00ab0af0) 範囲 `[['00ab0af0', '00ab0b0b']]`
  - `CONDITIONAL_JUMP` [`00ab0b08`](#insn-00ab0b08) → [`00ab0cc4`](#insn-00ab0cc4)
  - `FALL_THROUGH` [`00ab0b08`](#insn-00ab0b08) → [`00ab0b0c`](#insn-00ab0b0c)
- ブロック [`00ab0b0c`](#insn-00ab0b0c) 範囲 `[['00ab0b0c', '00ab0b0f']]`
  - `UNCONDITIONAL_JUMP` [`00ab0b0c`](#insn-00ab0b0c) → [`00ab0b1c`](#insn-00ab0b1c)
- ブロック [`00ab0b10`](#insn-00ab0b10) 範囲 `[['00ab0b10', '00ab0b1b']]`
  - `CONDITIONAL_JUMP` [`00ab0b18`](#insn-00ab0b18) → [`00ab0cc4`](#insn-00ab0cc4)
  - `FALL_THROUGH` [`00ab0b18`](#insn-00ab0b18) → [`00ab0b1c`](#insn-00ab0b1c)
- ブロック [`00ab0b1c`](#insn-00ab0b1c) 範囲 `[['00ab0b1c', '00ab0b3f']]`
  - `CONDITIONAL_JUMP` [`00ab0b3c`](#insn-00ab0b3c) → [`00ab0cc4`](#insn-00ab0cc4)
  - `FALL_THROUGH` [`00ab0b3c`](#insn-00ab0b3c) → [`00ab0b40`](#insn-00ab0b40)
- ブロック [`00ab0b40`](#insn-00ab0b40) 範囲 `[['00ab0b40', '00ab0b4f']]`
  - `CONDITIONAL_JUMP` [`00ab0b4c`](#insn-00ab0b4c) → [`00ab0b78`](#insn-00ab0b78)
  - `FALL_THROUGH` [`00ab0b4c`](#insn-00ab0b4c) → [`00ab0b50`](#insn-00ab0b50)
- ブロック [`00ab0b50`](#insn-00ab0b50) 範囲 `[['00ab0b50', '00ab0b5f']]`
  - `CONDITIONAL_JUMP` [`00ab0b5c`](#insn-00ab0b5c) → [`00ab0b78`](#insn-00ab0b78)
  - `FALL_THROUGH` [`00ab0b5c`](#insn-00ab0b5c) → [`00ab0b60`](#insn-00ab0b60)
- ブロック [`00ab0b60`](#insn-00ab0b60) 範囲 `[['00ab0b60', '00ab0b77']]`
  - `CONDITIONAL_JUMP` [`00ab0b74`](#insn-00ab0b74) → [`00ab0cc4`](#insn-00ab0cc4)
  - `FALL_THROUGH` [`00ab0b74`](#insn-00ab0b74) → [`00ab0b78`](#insn-00ab0b78)
- ブロック [`00ab0b78`](#insn-00ab0b78) 範囲 `[['00ab0b78', '00ab0b8b']]`
  - `CONDITIONAL_JUMP` [`00ab0b88`](#insn-00ab0b88) → [`00ab0ba0`](#insn-00ab0ba0)
  - `FALL_THROUGH` [`00ab0b88`](#insn-00ab0b88) → [`00ab0b8c`](#insn-00ab0b8c)
- ブロック [`00ab0b8c`](#insn-00ab0b8c) 範囲 `[['00ab0b8c', '00ab0b93']]`
  - `UNCONDITIONAL_JUMP` [`00ab0b90`](#insn-00ab0b90) → [`00ab0bc0`](#insn-00ab0bc0)
- ブロック [`00ab0b94`](#insn-00ab0b94) 範囲 `[['00ab0b94', '00ab0b9f']]`
  - `CONDITIONAL_JUMP` [`00ab0b9c`](#insn-00ab0b9c) → [`00ab0bc0`](#insn-00ab0bc0)
  - `FALL_THROUGH` [`00ab0b9c`](#insn-00ab0b9c) → [`00ab0ba0`](#insn-00ab0ba0)
- ブロック [`00ab0ba0`](#insn-00ab0ba0) 範囲 `[['00ab0ba0', '00ab0baf']]`
  - `CONDITIONAL_JUMP` [`00ab0bac`](#insn-00ab0bac) → [`00ab0b94`](#insn-00ab0b94)
  - `FALL_THROUGH` [`00ab0bac`](#insn-00ab0bac) → [`00ab0bb0`](#insn-00ab0bb0)
- ブロック [`00ab0bb0`](#insn-00ab0bb0) 範囲 `[['00ab0bb0', '00ab0bb3']]`
  - `CONDITIONAL_JUMP` [`00ab0bb0`](#insn-00ab0bb0) → [`00ab0c1c`](#insn-00ab0c1c)
  - `FALL_THROUGH` [`00ab0bb0`](#insn-00ab0bb0) → [`00ab0bb4`](#insn-00ab0bb4)
- ブロック [`00ab0bb4`](#insn-00ab0bb4) 範囲 `[['00ab0bb4', '00ab0bbb']]`
  - `CONDITIONAL_JUMP` [`00ab0bb8`](#insn-00ab0bb8) → [`00ab0ba0`](#insn-00ab0ba0)
  - `FALL_THROUGH` [`00ab0bb8`](#insn-00ab0bb8) → [`00ab0bbc`](#insn-00ab0bbc)
- ブロック [`00ab0bbc`](#insn-00ab0bbc) 範囲 `[['00ab0bbc', '00ab0bbf']]`
  - `FALL_THROUGH` [`00ab0bbc`](#insn-00ab0bbc) → [`00ab0bc0`](#insn-00ab0bc0)
- ブロック [`00ab0bc0`](#insn-00ab0bc0) 範囲 `[['00ab0bc0', '00ab0bfb']]`
  - `CONDITIONAL_JUMP` [`00ab0bf8`](#insn-00ab0bf8) → [`00ab0c04`](#insn-00ab0c04)
  - `FALL_THROUGH` [`00ab0bf8`](#insn-00ab0bf8) → [`00ab0bfc`](#insn-00ab0bfc)
- ブロック [`00ab0bfc`](#insn-00ab0bfc) 範囲 `[['00ab0bfc', '00ab0c03']]`
  - `FALL_THROUGH` [`00ab0c00`](#insn-00ab0c00) → [`00ab0c04`](#insn-00ab0c04)
- ブロック [`00ab0c04`](#insn-00ab0c04) 範囲 `[['00ab0c04', '00ab0c1b']]`
  - `UNCONDITIONAL_JUMP` [`00ab0c18`](#insn-00ab0c18) → [`00ab0c20`](#insn-00ab0c20)
- ブロック [`00ab0c1c`](#insn-00ab0c1c) 範囲 `[['00ab0c1c', '00ab0c1f']]`
  - `FALL_THROUGH` [`00ab0c1c`](#insn-00ab0c1c) → [`00ab0c20`](#insn-00ab0c20)
- ブロック [`00ab0c20`](#insn-00ab0c20) 範囲 `[['00ab0c20', '00ab0c2b']]`
  - `CONDITIONAL_JUMP` [`00ab0c28`](#insn-00ab0c28) → [`00ab0c40`](#insn-00ab0c40)
  - `FALL_THROUGH` [`00ab0c28`](#insn-00ab0c28) → [`00ab0c2c`](#insn-00ab0c2c)
- ブロック [`00ab0c2c`](#insn-00ab0c2c) 範囲 `[['00ab0c2c', '00ab0c33']]`
  - `UNCONDITIONAL_JUMP` [`00ab0c30`](#insn-00ab0c30) → [`00ab0c64`](#insn-00ab0c64)
- ブロック [`00ab0c34`](#insn-00ab0c34) 範囲 `[['00ab0c34', '00ab0c3f']]`
  - `CONDITIONAL_JUMP` [`00ab0c3c`](#insn-00ab0c3c) → [`00ab0c64`](#insn-00ab0c64)
  - `FALL_THROUGH` [`00ab0c3c`](#insn-00ab0c3c) → [`00ab0c40`](#insn-00ab0c40)
- ブロック [`00ab0c40`](#insn-00ab0c40) 範囲 `[['00ab0c40', '00ab0c4f']]`
  - `CONDITIONAL_JUMP` [`00ab0c4c`](#insn-00ab0c4c) → [`00ab0c34`](#insn-00ab0c34)
  - `FALL_THROUGH` [`00ab0c4c`](#insn-00ab0c4c) → [`00ab0c50`](#insn-00ab0c50)
- ブロック [`00ab0c50`](#insn-00ab0c50) 範囲 `[['00ab0c50', '00ab0c57']]`
  - `CONDITIONAL_JUMP` [`00ab0c54`](#insn-00ab0c54) → [`00ab0cb8`](#insn-00ab0cb8)
  - `FALL_THROUGH` [`00ab0c54`](#insn-00ab0c54) → [`00ab0c58`](#insn-00ab0c58)
- ブロック [`00ab0c58`](#insn-00ab0c58) 範囲 `[['00ab0c58', '00ab0c5f']]`
  - `CONDITIONAL_JUMP` [`00ab0c5c`](#insn-00ab0c5c) → [`00ab0c40`](#insn-00ab0c40)
  - `FALL_THROUGH` [`00ab0c5c`](#insn-00ab0c5c) → [`00ab0c60`](#insn-00ab0c60)
- ブロック [`00ab0c60`](#insn-00ab0c60) 範囲 `[['00ab0c60', '00ab0c63']]`
  - `FALL_THROUGH` [`00ab0c60`](#insn-00ab0c60) → [`00ab0c64`](#insn-00ab0c64)
- ブロック [`00ab0c64`](#insn-00ab0c64) 範囲 `[['00ab0c64', '00ab0c97']]`
  - `CONDITIONAL_JUMP` [`00ab0c94`](#insn-00ab0c94) → [`00ab0ca0`](#insn-00ab0ca0)
  - `FALL_THROUGH` [`00ab0c94`](#insn-00ab0c94) → [`00ab0c98`](#insn-00ab0c98)
- ブロック [`00ab0c98`](#insn-00ab0c98) 範囲 `[['00ab0c98', '00ab0c9f']]`
  - `FALL_THROUGH` [`00ab0c9c`](#insn-00ab0c9c) → [`00ab0ca0`](#insn-00ab0ca0)
- ブロック [`00ab0ca0`](#insn-00ab0ca0) 範囲 `[['00ab0ca0', '00ab0cb7']]`
  - `UNCONDITIONAL_JUMP` [`00ab0cb4`](#insn-00ab0cb4) → [`00ab0cbc`](#insn-00ab0cbc)
- ブロック [`00ab0cb8`](#insn-00ab0cb8) 範囲 `[['00ab0cb8', '00ab0cbb']]`
  - `FALL_THROUGH` [`00ab0cb8`](#insn-00ab0cb8) → [`00ab0cbc`](#insn-00ab0cbc)
- ブロック [`00ab0cbc`](#insn-00ab0cbc) 範囲 `[['00ab0cbc', '00ab0cc3']]`
  - `FALL_THROUGH` [`00ab0cc0`](#insn-00ab0cc0) → [`00ab0cc4`](#insn-00ab0cc4)
- ブロック [`00ab0cc4`](#insn-00ab0cc4) 範囲 `[['00ab0cc4', '00ab0cc7']]`
  - `FALL_THROUGH` [`00ab0cc4`](#insn-00ab0cc4) → [`00ab0cc8`](#insn-00ab0cc8)
- ブロック [`00ab0cc8`](#insn-00ab0cc8) 範囲 `[['00ab0cc8', '00ab0ccb']]`
  - `CONDITIONAL_JUMP` [`00ab0cc8`](#insn-00ab0cc8) → [`00aafb60`](#insn-00aafb60)
  - `FALL_THROUGH` [`00ab0cc8`](#insn-00ab0cc8) → [`00ab0ccc`](#insn-00ab0ccc)
- ブロック [`00ab0ccc`](#insn-00ab0ccc) 範囲 `[['00ab0ccc', '00ab0cd7']]`
  - `UNCONDITIONAL_JUMP` [`00ab0cd4`](#insn-00ab0cd4) → [`00aafb60`](#insn-00aafb60)
- ブロック [`00ab0cd8`](#insn-00ab0cd8) 範囲 `[['00ab0cd8', '00ab0cdf']]`
  - `CONDITIONAL_JUMP` [`00ab0cdc`](#insn-00ab0cdc) → [`00ab0ce8`](#insn-00ab0ce8)
  - `FALL_THROUGH` [`00ab0cdc`](#insn-00ab0cdc) → [`00ab0ce0`](#insn-00ab0ce0)
- ブロック [`00ab0ce0`](#insn-00ab0ce0) 範囲 `[['00ab0ce0', '00ab0ce7']]`
  - `FALL_THROUGH` [`00ab0ce4`](#insn-00ab0ce4) → [`00ab0ce8`](#insn-00ab0ce8)
- ブロック [`00ab0ce8`](#insn-00ab0ce8) 範囲 `[['00ab0ce8', '00ab0cfb']]`
  - `CONDITIONAL_JUMP` [`00ab0cf8`](#insn-00ab0cf8) → [`00ab0e34`](#insn-00ab0e34)
  - `FALL_THROUGH` [`00ab0cf8`](#insn-00ab0cf8) → [`00ab0cfc`](#insn-00ab0cfc)
- ブロック [`00ab0cfc`](#insn-00ab0cfc) 範囲 `[['00ab0cfc', '00ab0d1b']]`
- ブロック [`00ab0d1c`](#insn-00ab0d1c) 範囲 `[['00ab0d1c', '00ab0d2f']]`
  - `CONDITIONAL_JUMP` [`00ab0d2c`](#insn-00ab0d2c) → [`00ab0e34`](#insn-00ab0e34)
  - `FALL_THROUGH` [`00ab0d2c`](#insn-00ab0d2c) → [`00ab0d30`](#insn-00ab0d30)
- ブロック [`00ab0d30`](#insn-00ab0d30) 範囲 `[['00ab0d30', '00ab0d37']]`
- ブロック [`00ab0d38`](#insn-00ab0d38) 範囲 `[['00ab0d38', '00ab0d4b']]`
  - `CONDITIONAL_JUMP` [`00ab0d48`](#insn-00ab0d48) → [`00ab0e34`](#insn-00ab0e34)
  - `FALL_THROUGH` [`00ab0d48`](#insn-00ab0d48) → [`00ab0d4c`](#insn-00ab0d4c)
- ブロック [`00ab0d4c`](#insn-00ab0d4c) 範囲 `[['00ab0d4c', '00ab0d4f']]`
- ブロック [`00ab0d50`](#insn-00ab0d50) 範囲 `[['00ab0d50', '00ab0d63']]`
  - `CONDITIONAL_JUMP` [`00ab0d60`](#insn-00ab0d60) → [`00ab0e34`](#insn-00ab0e34)
  - `FALL_THROUGH` [`00ab0d60`](#insn-00ab0d60) → [`00ab0d64`](#insn-00ab0d64)
- ブロック [`00ab0d64`](#insn-00ab0d64) 範囲 `[['00ab0d64', '00ab0d6f']]`
  - `FALL_THROUGH` [`00ab0d6c`](#insn-00ab0d6c) → [`00ab0d70`](#insn-00ab0d70)
- ブロック [`00ab0d70`](#insn-00ab0d70) 範囲 `[['00ab0d70', '00ab0d83']]`
  - `CONDITIONAL_JUMP` [`00ab0d80`](#insn-00ab0d80) → [`00ab0e34`](#insn-00ab0e34)
  - `FALL_THROUGH` [`00ab0d80`](#insn-00ab0d80) → [`00ab0d84`](#insn-00ab0d84)
- ブロック [`00ab0d84`](#insn-00ab0d84) 範囲 `[['00ab0d84', '00ab0d8b']]`
- ブロック [`00ab0d8c`](#insn-00ab0d8c) 範囲 `[['00ab0d8c', '00ab0d9f']]`
  - `CONDITIONAL_JUMP` [`00ab0d9c`](#insn-00ab0d9c) → [`00ab0e34`](#insn-00ab0e34)
  - `FALL_THROUGH` [`00ab0d9c`](#insn-00ab0d9c) → [`00ab0da0`](#insn-00ab0da0)
- ブロック [`00ab0da0`](#insn-00ab0da0) 範囲 `[['00ab0da0', '00ab0da3']]`
- ブロック [`00ab0e34`](#insn-00ab0e34) 範囲 `[['00ab0e34', '00ab0e37']]`

## 命令位置別の参照

- [`00aafb20`](#insn-00aafb20) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb24`](#insn-00aafb24) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb28`](#insn-00aafb28) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb2c`](#insn-00aafb2c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb30`](#insn-00aafb30) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb34`](#insn-00aafb34) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb40`](#insn-00aafb40) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb48`](#insn-00aafb48) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb50`](#insn-00aafb50) → [`00aaf9b8`](00aaf9b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aaf9b8` · 推定シンボル `None` · 推定型 `None`
- [`00aafb5c`](#insn-00aafb5c) → [`00aafb6c`](#insn-00aafb6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb68`](#insn-00aafb68) → [`00ab0cd8`](#insn-00ab0cd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb70`](#insn-00aafb70) → [`00aafb60`](#insn-00aafb60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafb74`](#insn-00aafb74) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aafbcc`](#insn-00aafbcc) → [`00aafb60`](#insn-00aafb60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafbd0`](#insn-00aafbd0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aafc20`](#insn-00aafc20) → [`00aafb60`](#insn-00aafb60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc24`](#insn-00aafc24) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aafc30`](#insn-00aafc30) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafc34`](#insn-00aafc34) → [`00aafc4c`](#insn-00aafc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc3c`](#insn-00aafc3c) → [`00aafc6c`](#insn-00aafc6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc48`](#insn-00aafc48) → [`00aafc6c`](#insn-00aafc6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc58`](#insn-00aafc58) → [`00aafc40`](#insn-00aafc40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc5c`](#insn-00aafc5c) → [`00aafcc8`](#insn-00aafcc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc64`](#insn-00aafc64) → [`00aafc4c`](#insn-00aafc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafc70`](#insn-00aafc70) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aafc94`](#insn-00aafc94) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafc98`](#insn-00aafc98) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00aafca4`](#insn-00aafca4) → [`00aafcb0`](#insn-00aafcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafca8`](#insn-00aafca8) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00aafcac`](#insn-00aafcac) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafcb0`](#insn-00aafcb0) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafcb4`](#insn-00aafcb4) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aafcb8`](#insn-00aafcb8) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafcc0`](#insn-00aafcc0) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafcc4`](#insn-00aafcc4) → [`00aafccc`](#insn-00aafccc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafcd8`](#insn-00aafcd8) → [`00aafde4`](#insn-00aafde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafce0`](#insn-00aafce0) → [`00aafcfc`](#insn-00aafcfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafcf8`](#insn-00aafcf8) → [`00aafd30`](#insn-00aafd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd04`](#insn-00aafd04) → [`00aafd18`](#insn-00aafd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd10`](#insn-00aafd10) → [`00aafd08`](#insn-00aafd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd14`](#insn-00aafd14) → [`00aafce4`](#insn-00aafce4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd28`](#insn-00aafd28) → [`00aafd18`](#insn-00aafd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd2c`](#insn-00aafd2c) → [`00aafce4`](#insn-00aafce4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd34`](#insn-00aafd34) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd38`](#insn-00aafd38) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd3c`](#insn-00aafd3c) → [`00aafdf0`](#insn-00aafdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd40`](#insn-00aafd40) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aafd4c`](#insn-00aafd4c) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafd50`](#insn-00aafd50) → [`00aafd68`](#insn-00aafd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd58`](#insn-00aafd58) → [`00aafd88`](#insn-00aafd88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd64`](#insn-00aafd64) → [`00aafd88`](#insn-00aafd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd74`](#insn-00aafd74) → [`00aafd5c`](#insn-00aafd5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd78`](#insn-00aafd78) → [`00aafff4`](#insn-00aafff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd80`](#insn-00aafd80) → [`00aafd68`](#insn-00aafd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafd8c`](#insn-00aafd8c) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aafdb0`](#insn-00aafdb0) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafdb4`](#insn-00aafdb4) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00aafdc0`](#insn-00aafdc0) → [`00aafdcc`](#insn-00aafdcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafdc4`](#insn-00aafdc4) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00aafdc8`](#insn-00aafdc8) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafdcc`](#insn-00aafdcc) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafdd0`](#insn-00aafdd0) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aafdd4`](#insn-00aafdd4) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafddc`](#insn-00aafddc) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafde0`](#insn-00aafde0) → [`00aafff8`](#insn-00aafff8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafde8`](#insn-00aafde8) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafdec`](#insn-00aafdec) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafdf4`](#insn-00aafdf4) → [`00aafe0c`](#insn-00aafe0c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafdfc`](#insn-00aafdfc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe08`](#insn-00aafe08) → [`00ab02a8`](#insn-00ab02a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe0c`](#insn-00aafe0c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aafe18`](#insn-00aafe18) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafe1c`](#insn-00aafe1c) → [`00aafe34`](#insn-00aafe34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe24`](#insn-00aafe24) → [`00aafe54`](#insn-00aafe54) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe30`](#insn-00aafe30) → [`00aafe54`](#insn-00aafe54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe40`](#insn-00aafe40) → [`00aafe28`](#insn-00aafe28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe44`](#insn-00aafe44) → [`00aafeb0`](#insn-00aafeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe4c`](#insn-00aafe4c) → [`00aafe34`](#insn-00aafe34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe58`](#insn-00aafe58) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aafe7c`](#insn-00aafe7c) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafe80`](#insn-00aafe80) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00aafe8c`](#insn-00aafe8c) → [`00aafe98`](#insn-00aafe98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafe90`](#insn-00aafe90) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00aafe94`](#insn-00aafe94) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafe98`](#insn-00aafe98) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafe9c`](#insn-00aafe9c) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aafea0`](#insn-00aafea0) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafea8`](#insn-00aafea8) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00aafeac`](#insn-00aafeac) → [`00aafeb4`](#insn-00aafeb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafebc`](#insn-00aafebc) → [`00aafed4`](#insn-00aafed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafec4`](#insn-00aafec4) → [`00aafef8`](#insn-00aafef8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafed0`](#insn-00aafed0) → [`00aafef8`](#insn-00aafef8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafee0`](#insn-00aafee0) → [`00aafec8`](#insn-00aafec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafee8`](#insn-00aafee8) → [`00aaff50`](#insn-00aaff50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafef0`](#insn-00aafef0) → [`00aafed4`](#insn-00aafed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aafefc`](#insn-00aafefc) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aaff24`](#insn-00aaff24) → [`00aaff30`](#insn-00aaff30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff34`](#insn-00aaff34) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aaff48`](#insn-00aaff48) → [`00aafe00`](#insn-00aafe00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff4c`](#insn-00aaff4c) → [`00aaff5c`](#insn-00aaff5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff58`](#insn-00aaff58) → [`00aafe00`](#insn-00aafe00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff5c`](#insn-00aaff5c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff64`](#insn-00aaff64) → [`00aafdf8`](#insn-00aafdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff68`](#insn-00aaff68) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaff7c`](#insn-00aaff7c) → [`00ab0d1c`](#insn-00ab0d1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffa0`](#insn-00aaffa0) → [`00aaffbc`](#insn-00aaffbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffa8`](#insn-00aaffa8) → [`00ab0d38`](#insn-00ab0d38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffb0`](#insn-00aaffb0) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aaffb8`](#insn-00aaffb8) → [`00aaffc0`](#insn-00aaffc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffd8`](#insn-00aaffd8) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00aaffdc`](#insn-00aaffdc) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffe0`](#insn-00aaffe0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffe4`](#insn-00aaffe4) → [`00aafdfc`](#insn-00aafdfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaffec`](#insn-00aaffec) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00aafff0`](#insn-00aafff0) → [`00aafdfc`](#insn-00aafdfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0000`](#insn-00ab0000) → [`00ab0018`](#insn-00ab0018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0008`](#insn-00ab0008) → [`00ab003c`](#insn-00ab003c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0014`](#insn-00ab0014) → [`00ab003c`](#insn-00ab003c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0024`](#insn-00ab0024) → [`00ab000c`](#insn-00ab000c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab002c`](#insn-00ab002c) → [`00ab0098`](#insn-00ab0098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0034`](#insn-00ab0034) → [`00ab0018`](#insn-00ab0018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0040`](#insn-00ab0040) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab006c`](#insn-00ab006c) → [`00ab0078`](#insn-00ab0078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab007c`](#insn-00ab007c) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab0090`](#insn-00ab0090) → [`00ab00a4`](#insn-00ab00a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0094`](#insn-00ab0094) → [`00aafdf0`](#insn-00aafdf0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab00a0`](#insn-00ab00a0) → [`00aafdf0`](#insn-00aafdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab00a8`](#insn-00ab00a8) → [`00ab00d4`](#insn-00ab00d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab00b0`](#insn-00ab00b0) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab00c4`](#insn-00ab00c4) → [`00ab0208`](#insn-00ab0208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab00d0`](#insn-00ab00d0) → [`00ab02a8`](#insn-00ab02a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab00d4`](#insn-00ab00d4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab00e0`](#insn-00ab00e0) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab00e4`](#insn-00ab00e4) → [`00ab00fc`](#insn-00ab00fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab00ec`](#insn-00ab00ec) → [`00ab011c`](#insn-00ab011c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab00f8`](#insn-00ab00f8) → [`00ab011c`](#insn-00ab011c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0108`](#insn-00ab0108) → [`00ab00f0`](#insn-00ab00f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab010c`](#insn-00ab010c) → [`00ab0178`](#insn-00ab0178) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0114`](#insn-00ab0114) → [`00ab00fc`](#insn-00ab00fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0120`](#insn-00ab0120) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab0144`](#insn-00ab0144) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0148`](#insn-00ab0148) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab0154`](#insn-00ab0154) → [`00ab0160`](#insn-00ab0160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0158`](#insn-00ab0158) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab015c`](#insn-00ab015c) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0160`](#insn-00ab0160) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0164`](#insn-00ab0164) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab0168`](#insn-00ab0168) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0170`](#insn-00ab0170) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0174`](#insn-00ab0174) → [`00ab017c`](#insn-00ab017c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0184`](#insn-00ab0184) → [`00ab019c`](#insn-00ab019c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab018c`](#insn-00ab018c) → [`00ab01c0`](#insn-00ab01c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0198`](#insn-00ab0198) → [`00ab01c0`](#insn-00ab01c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab01a8`](#insn-00ab01a8) → [`00ab0190`](#insn-00ab0190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab01b0`](#insn-00ab01b0) → [`00ab01fc`](#insn-00ab01fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab01b8`](#insn-00ab01b8) → [`00ab019c`](#insn-00ab019c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab01c4`](#insn-00ab01c4) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab01ec`](#insn-00ab01ec) → [`00ab00ac`](#insn-00ab00ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab01f8`](#insn-00ab01f8) → [`00ab00ac`](#insn-00ab00ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0204`](#insn-00ab0204) → [`00ab00c8`](#insn-00ab00c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0208`](#insn-00ab0208) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0210`](#insn-00ab0210) → [`00ab021c`](#insn-00ab021c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0218`](#insn-00ab0218) → [`00ab02a4`](#insn-00ab02a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab021c`](#insn-00ab021c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0230`](#insn-00ab0230) → [`00ab0d70`](#insn-00ab0d70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0254`](#insn-00ab0254) → [`00ab0270`](#insn-00ab0270) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab025c`](#insn-00ab025c) → [`00ab0d8c`](#insn-00ab0d8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0264`](#insn-00ab0264) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab026c`](#insn-00ab026c) → [`00ab0274`](#insn-00ab0274) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab028c`](#insn-00ab028c) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00ab0290`](#insn-00ab0290) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0294`](#insn-00ab0294) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0298`](#insn-00ab0298) → [`00ab02a4`](#insn-00ab02a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab02a0`](#insn-00ab02a0) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00ab02a4`](#insn-00ab02a4) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab02a8`](#insn-00ab02a8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab02b0`](#insn-00ab02b0) → [`00ab0d50`](#insn-00ab0d50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab02bc`](#insn-00ab02bc) → [`00ab02c8`](#insn-00ab02c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab02c4`](#insn-00ab02c4) → [`00ab02f0`](#insn-00ab02f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab02d4`](#insn-00ab02d4) → [`00ab02e8`](#insn-00ab02e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab02e4`](#insn-00ab02e4) → [`00ab02cc`](#insn-00ab02cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab02f0`](#insn-00ab02f0) → `Stack[-0xa4]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab02f4`](#insn-00ab02f4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0300`](#insn-00ab0300) → [`00ab0664`](#insn-00ab0664) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0308`](#insn-00ab0308) → [`00ab0708`](#insn-00ab0708) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0314`](#insn-00ab0314) → [`00ab0338`](#insn-00ab0338) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0324`](#insn-00ab0324) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0328`](#insn-00ab0328) → [`00ab070c`](#insn-00ab070c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0334`](#insn-00ab0334) → [`00ab070c`](#insn-00ab070c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab033c`](#insn-00ab033c) → [`0044a8d8`](../0044a/0044a8d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044a8d8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0340`](#insn-00ab0340) → `Stack[-0xa4]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0348`](#insn-00ab0348) → [`00ab032c`](#insn-00ab032c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab034c`](#insn-00ab034c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0358`](#insn-00ab0358) → [`0044a8d8`](../0044a/0044a8d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044a8d8` · 推定シンボル `None` · 推定型 `None`
- [`00ab035c`](#insn-00ab035c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0368`](#insn-00ab0368) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab0374`](#insn-00ab0374) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0378`](#insn-00ab0378) → [`00ab0390`](#insn-00ab0390) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0380`](#insn-00ab0380) → [`00ab03b0`](#insn-00ab03b0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab038c`](#insn-00ab038c) → [`00ab03b0`](#insn-00ab03b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab039c`](#insn-00ab039c) → [`00ab0384`](#insn-00ab0384) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab03a0`](#insn-00ab03a0) → [`00ab040c`](#insn-00ab040c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab03a8`](#insn-00ab03a8) → [`00ab0390`](#insn-00ab0390) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab03b4`](#insn-00ab03b4) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab03d8`](#insn-00ab03d8) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab03dc`](#insn-00ab03dc) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab03e8`](#insn-00ab03e8) → [`00ab03f4`](#insn-00ab03f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab03ec`](#insn-00ab03ec) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab03f0`](#insn-00ab03f0) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab03f4`](#insn-00ab03f4) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab03f8`](#insn-00ab03f8) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab03fc`](#insn-00ab03fc) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0404`](#insn-00ab0404) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0408`](#insn-00ab0408) → [`00ab0410`](#insn-00ab0410) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0418`](#insn-00ab0418) → [`00ab0430`](#insn-00ab0430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0420`](#insn-00ab0420) → [`00ab0454`](#insn-00ab0454) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab042c`](#insn-00ab042c) → [`00ab0454`](#insn-00ab0454) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab043c`](#insn-00ab043c) → [`00ab0424`](#insn-00ab0424) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0444`](#insn-00ab0444) → [`00ab04ac`](#insn-00ab04ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab044c`](#insn-00ab044c) → [`00ab0430`](#insn-00ab0430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0458`](#insn-00ab0458) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab0480`](#insn-00ab0480) → [`00ab048c`](#insn-00ab048c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0490`](#insn-00ab0490) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab04a4`](#insn-00ab04a4) → [`00ab032c`](#insn-00ab032c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab04a8`](#insn-00ab04a8) → [`00ab04b8`](#insn-00ab04b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab04b4`](#insn-00ab04b4) → [`00ab032c`](#insn-00ab032c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab04b8`](#insn-00ab04b8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab04c0`](#insn-00ab04c0) → [`007ac4fc`](../007ac/007ac4fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007ac4fc` · 推定シンボル `None` · 推定型 `None`
- [`00ab04c4`](#insn-00ab04c4) → [`00ab04f0`](#insn-00ab04f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab04c8`](#insn-00ab04c8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab04d0`](#insn-00ab04d0) → [`007ac574`](../007ac/007ac574.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007ac574` · 推定シンボル `None` · 推定型 `None`
- [`00ab04d4`](#insn-00ab04d4) → [`00ab04f0`](#insn-00ab04f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab04d8`](#insn-00ab04d8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab04e4`](#insn-00ab04e4) → `00334058`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00ab04ec`](#insn-00ab04ec) → [`00ab032c`](#insn-00ab032c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab04f0`](#insn-00ab04f0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab04fc`](#insn-00ab04fc) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab0500`](#insn-00ab0500) → [`00ab0518`](#insn-00ab0518) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0508`](#insn-00ab0508) → [`00ab0538`](#insn-00ab0538) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0514`](#insn-00ab0514) → [`00ab0538`](#insn-00ab0538) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0524`](#insn-00ab0524) → [`00ab050c`](#insn-00ab050c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0528`](#insn-00ab0528) → [`00ab0594`](#insn-00ab0594) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0530`](#insn-00ab0530) → [`00ab0518`](#insn-00ab0518) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab053c`](#insn-00ab053c) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab0560`](#insn-00ab0560) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab0564`](#insn-00ab0564) → `00334018`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ab0570`](#insn-00ab0570) → [`00ab057c`](#insn-00ab057c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0574`](#insn-00ab0574) → `00334018`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ab0578`](#insn-00ab0578) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab057c`](#insn-00ab057c) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab0580`](#insn-00ab0580) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab0584`](#insn-00ab0584) → `00334028`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab058c`](#insn-00ab058c) → `00334028`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0590`](#insn-00ab0590) → [`00ab0598`](#insn-00ab0598) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab05a0`](#insn-00ab05a0) → [`00ab05b8`](#insn-00ab05b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab05a8`](#insn-00ab05a8) → [`00ab05dc`](#insn-00ab05dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab05b4`](#insn-00ab05b4) → [`00ab05dc`](#insn-00ab05dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab05c4`](#insn-00ab05c4) → [`00ab05ac`](#insn-00ab05ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab05cc`](#insn-00ab05cc) → [`00ab062c`](#insn-00ab062c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab05d4`](#insn-00ab05d4) → [`00ab05b8`](#insn-00ab05b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab05e0`](#insn-00ab05e0) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab0608`](#insn-00ab0608) → [`00ab0614`](#insn-00ab0614) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0618`](#insn-00ab0618) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab0628`](#insn-00ab0628) → [`00ab0630`](#insn-00ab0630) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0630`](#insn-00ab0630) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab064c`](#insn-00ab064c) → [`00ab0318`](#insn-00ab0318) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0658`](#insn-00ab0658) → [`00bdb0a0`](../00bdb/00bdb0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0a0` · 推定シンボル `None` · 推定型 `None`
- [`00ab065c`](#insn-00ab065c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0660`](#insn-00ab0660) → [`00ab0318`](#insn-00ab0318) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0664`](#insn-00ab0664) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab0670`](#insn-00ab0670) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0674`](#insn-00ab0674) → [`00ab068c`](#insn-00ab068c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab067c`](#insn-00ab067c) → [`00ab06ac`](#insn-00ab06ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0688`](#insn-00ab0688) → [`00ab06ac`](#insn-00ab06ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0698`](#insn-00ab0698) → [`00ab0680`](#insn-00ab0680) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab069c`](#insn-00ab069c) → [`00ab0a6c`](#insn-00ab0a6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab06a4`](#insn-00ab06a4) → [`00ab068c`](#insn-00ab068c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab06b0`](#insn-00ab06b0) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab06d4`](#insn-00ab06d4) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab06d8`](#insn-00ab06d8) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab06e4`](#insn-00ab06e4) → [`00ab06f0`](#insn-00ab06f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab06e8`](#insn-00ab06e8) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab06ec`](#insn-00ab06ec) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab06f0`](#insn-00ab06f0) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab06f4`](#insn-00ab06f4) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab06f8`](#insn-00ab06f8) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0700`](#insn-00ab0700) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0704`](#insn-00ab0704) → [`00ab0a70`](#insn-00ab0a70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0718`](#insn-00ab0718) → [`00ab0cc4`](#insn-00ab0cc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab071c`](#insn-00ab071c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0724`](#insn-00ab0724) → [`00ab0cc8`](#insn-00ab0cc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab072c`](#insn-00ab072c) → [`00ab0cc4`](#insn-00ab0cc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0734`](#insn-00ab0734) → [`00ab0754`](#insn-00ab0754) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0740`](#insn-00ab0740) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0744`](#insn-00ab0744) → [`00ab0cc8`](#insn-00ab0cc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0750`](#insn-00ab0750) → [`00ab0cc4`](#insn-00ab0cc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0754`](#insn-00ab0754) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0760`](#insn-00ab0760) → [`0044a8d8`](../0044a/0044a8d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044a8d8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0764`](#insn-00ab0764) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0770`](#insn-00ab0770) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab077c`](#insn-00ab077c) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0780`](#insn-00ab0780) → [`00ab0798`](#insn-00ab0798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0788`](#insn-00ab0788) → [`00ab07b8`](#insn-00ab07b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0794`](#insn-00ab0794) → [`00ab07b8`](#insn-00ab07b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab07a4`](#insn-00ab07a4) → [`00ab078c`](#insn-00ab078c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab07a8`](#insn-00ab07a8) → [`00ab0814`](#insn-00ab0814) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab07b0`](#insn-00ab07b0) → [`00ab0798`](#insn-00ab0798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab07bc`](#insn-00ab07bc) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab07e0`](#insn-00ab07e0) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab07e4`](#insn-00ab07e4) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab07f0`](#insn-00ab07f0) → [`00ab07fc`](#insn-00ab07fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab07f4`](#insn-00ab07f4) → `00334030`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab07f8`](#insn-00ab07f8) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab07fc`](#insn-00ab07fc) → `00334038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0800`](#insn-00ab0800) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab0804`](#insn-00ab0804) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab080c`](#insn-00ab080c) → `00334040`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0810`](#insn-00ab0810) → [`00ab0818`](#insn-00ab0818) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0820`](#insn-00ab0820) → [`00ab0838`](#insn-00ab0838) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0828`](#insn-00ab0828) → [`00ab085c`](#insn-00ab085c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0834`](#insn-00ab0834) → [`00ab085c`](#insn-00ab085c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0844`](#insn-00ab0844) → [`00ab082c`](#insn-00ab082c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab084c`](#insn-00ab084c) → [`00ab08b4`](#insn-00ab08b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0854`](#insn-00ab0854) → [`00ab0838`](#insn-00ab0838) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0860`](#insn-00ab0860) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab0888`](#insn-00ab0888) → [`00ab0894`](#insn-00ab0894) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0898`](#insn-00ab0898) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab08ac`](#insn-00ab08ac) → [`00ab0748`](#insn-00ab0748) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab08b0`](#insn-00ab08b0) → [`00ab08c0`](#insn-00ab08c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab08bc`](#insn-00ab08bc) → [`00ab0748`](#insn-00ab0748) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab08c0`](#insn-00ab08c0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab08c8`](#insn-00ab08c8) → [`007ac4fc`](../007ac/007ac4fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007ac4fc` · 推定シンボル `None` · 推定型 `None`
- [`00ab08cc`](#insn-00ab08cc) → [`00ab08f8`](#insn-00ab08f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab08d0`](#insn-00ab08d0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab08d8`](#insn-00ab08d8) → [`007ac574`](../007ac/007ac574.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007ac574` · 推定シンボル `None` · 推定型 `None`
- [`00ab08dc`](#insn-00ab08dc) → [`00ab08f8`](#insn-00ab08f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab08e0`](#insn-00ab08e0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab08ec`](#insn-00ab08ec) → `00334058`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00ab08f4`](#insn-00ab08f4) → [`00ab0748`](#insn-00ab0748) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab08f8`](#insn-00ab08f8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab0904`](#insn-00ab0904) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab0908`](#insn-00ab0908) → [`00ab0920`](#insn-00ab0920) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0910`](#insn-00ab0910) → [`00ab0940`](#insn-00ab0940) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab091c`](#insn-00ab091c) → [`00ab0940`](#insn-00ab0940) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab092c`](#insn-00ab092c) → [`00ab0914`](#insn-00ab0914) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0930`](#insn-00ab0930) → [`00ab099c`](#insn-00ab099c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0938`](#insn-00ab0938) → [`00ab0920`](#insn-00ab0920) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0944`](#insn-00ab0944) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab0968`](#insn-00ab0968) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab096c`](#insn-00ab096c) → `00334018`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ab0978`](#insn-00ab0978) → [`00ab0984`](#insn-00ab0984) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab097c`](#insn-00ab097c) → `00334018`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ab0980`](#insn-00ab0980) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab0984`](#insn-00ab0984) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab0988`](#insn-00ab0988) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab098c`](#insn-00ab098c) → `00334028`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0994`](#insn-00ab0994) → `00334028`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0998`](#insn-00ab0998) → [`00ab09a0`](#insn-00ab09a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab09a8`](#insn-00ab09a8) → [`00ab09c0`](#insn-00ab09c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab09b0`](#insn-00ab09b0) → [`00ab09e4`](#insn-00ab09e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab09bc`](#insn-00ab09bc) → [`00ab09e4`](#insn-00ab09e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab09cc`](#insn-00ab09cc) → [`00ab09b4`](#insn-00ab09b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab09d4`](#insn-00ab09d4) → [`00ab0a34`](#insn-00ab0a34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab09dc`](#insn-00ab09dc) → [`00ab09c0`](#insn-00ab09c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab09e8`](#insn-00ab09e8) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a10`](#insn-00ab0a10) → [`00ab0a1c`](#insn-00ab0a1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a20`](#insn-00ab0a20) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a30`](#insn-00ab0a30) → [`00ab0a38`](#insn-00ab0a38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a38`](#insn-00ab0a38) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a54`](#insn-00ab0a54) → [`00ab0738`](#insn-00ab0738) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a60`](#insn-00ab0a60) → [`00bdb0a0`](../00bdb/00bdb0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0a0` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a64`](#insn-00ab0a64) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a68`](#insn-00ab0a68) → [`00ab0738`](#insn-00ab0738) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a78`](#insn-00ab0a78) → [`00ab0a90`](#insn-00ab0a90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a80`](#insn-00ab0a80) → [`00ab0ab4`](#insn-00ab0ab4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a8c`](#insn-00ab0a8c) → [`00ab0ab4`](#insn-00ab0ab4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0a9c`](#insn-00ab0a9c) → [`00ab0a84`](#insn-00ab0a84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0aa4`](#insn-00ab0aa4) → [`00ab0b10`](#insn-00ab0b10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0aac`](#insn-00ab0aac) → [`00ab0a90`](#insn-00ab0a90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ab8`](#insn-00ab0ab8) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ae4`](#insn-00ab0ae4) → [`00ab0af0`](#insn-00ab0af0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0af4`](#insn-00ab0af4) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b08`](#insn-00ab0b08) → [`00ab0cc4`](#insn-00ab0cc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b0c`](#insn-00ab0b0c) → [`00ab0b1c`](#insn-00ab0b1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b18`](#insn-00ab0b18) → [`00ab0cc4`](#insn-00ab0cc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b20`](#insn-00ab0b20) → [`0044a8d8`](../0044a/0044a8d8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044a8d8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b28`](#insn-00ab0b28) → `Stack[-0xa4]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b3c`](#insn-00ab0b3c) → [`00ab0cc4`](#insn-00ab0cc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b40`](#insn-00ab0b40) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b48`](#insn-00ab0b48) → [`007ac4fc`](../007ac/007ac4fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007ac4fc` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b4c`](#insn-00ab0b4c) → [`00ab0b78`](#insn-00ab0b78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b50`](#insn-00ab0b50) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b58`](#insn-00ab0b58) → [`007ac574`](../007ac/007ac574.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007ac574` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b5c`](#insn-00ab0b5c) → [`00ab0b78`](#insn-00ab0b78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b60`](#insn-00ab0b60) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b6c`](#insn-00ab0b6c) → `00334058`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00ab0b74`](#insn-00ab0b74) → [`00ab0cc4`](#insn-00ab0cc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b78`](#insn-00ab0b78) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b84`](#insn-00ab0b84) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab0b88`](#insn-00ab0b88) → [`00ab0ba0`](#insn-00ab0ba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b90`](#insn-00ab0b90) → [`00ab0bc0`](#insn-00ab0bc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0b9c`](#insn-00ab0b9c) → [`00ab0bc0`](#insn-00ab0bc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0bac`](#insn-00ab0bac) → [`00ab0b94`](#insn-00ab0b94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0bb0`](#insn-00ab0bb0) → [`00ab0c1c`](#insn-00ab0c1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0bb8`](#insn-00ab0bb8) → [`00ab0ba0`](#insn-00ab0ba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0bc4`](#insn-00ab0bc4) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab0be8`](#insn-00ab0be8) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab0bec`](#insn-00ab0bec) → `00334018`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ab0bf8`](#insn-00ab0bf8) → [`00ab0c04`](#insn-00ab0c04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0bfc`](#insn-00ab0bfc) → `00334018`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[39]`
- [`00ab0c00`](#insn-00ab0c00) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab0c04`](#insn-00ab0c04) → `00334020`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_00334020` · 推定型 `dword`
- [`00ab0c08`](#insn-00ab0c08) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab0c0c`](#insn-00ab0c0c) → `00334028`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0c14`](#insn-00ab0c14) → `00334028`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0c18`](#insn-00ab0c18) → [`00ab0c20`](#insn-00ab0c20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0c28`](#insn-00ab0c28) → [`00ab0c40`](#insn-00ab0c40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0c30`](#insn-00ab0c30) → [`00ab0c64`](#insn-00ab0c64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0c3c`](#insn-00ab0c3c) → [`00ab0c64`](#insn-00ab0c64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0c4c`](#insn-00ab0c4c) → [`00ab0c34`](#insn-00ab0c34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0c54`](#insn-00ab0c54) → [`00ab0cb8`](#insn-00ab0cb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0c5c`](#insn-00ab0c5c) → [`00ab0c40`](#insn-00ab0c40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0c68`](#insn-00ab0c68) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00ab0c94`](#insn-00ab0c94) → [`00ab0ca0`](#insn-00ab0ca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ca4`](#insn-00ab0ca4) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00ab0cb4`](#insn-00ab0cb4) → [`00ab0cbc`](#insn-00ab0cbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0cc4`](#insn-00ab0cc4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0cc8`](#insn-00ab0cc8) → [`00aafb60`](#insn-00aafb60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ccc`](#insn-00ab0ccc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0cd0`](#insn-00ab0cd0) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00ab0cd4`](#insn-00ab0cd4) → [`00aafb60`](#insn-00aafb60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0cd8`](#insn-00ab0cd8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0cdc`](#insn-00ab0cdc) → [`00ab0ce8`](#insn-00ab0ce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ce0`](#insn-00ab0ce0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ce4`](#insn-00ab0ce4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ce8`](#insn-00ab0ce8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0cf0`](#insn-00ab0cf0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0cf8`](#insn-00ab0cf8) → [`00ab0e34`](#insn-00ab0e34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0cfc`](#insn-00ab0cfc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d00`](#insn-00ab0d00) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d04`](#insn-00ab0d04) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d08`](#insn-00ab0d08) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d0c`](#insn-00ab0d0c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d10`](#insn-00ab0d10) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d1c`](#insn-00ab0d1c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d24`](#insn-00ab0d24) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d2c`](#insn-00ab0d2c) → [`00ab0e34`](#insn-00ab0e34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d34`](#insn-00ab0d34) → [`0044d968`](../0044d/0044d968.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044d968` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d38`](#insn-00ab0d38) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d40`](#insn-00ab0d40) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d48`](#insn-00ab0d48) → [`00ab0e34`](#insn-00ab0e34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d4c`](#insn-00ab0d4c) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d50`](#insn-00ab0d50) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d58`](#insn-00ab0d58) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d60`](#insn-00ab0d60) → [`00ab0e34`](#insn-00ab0e34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d6c`](#insn-00ab0d6c) → [`00ab0e4c`](../00ab0/00ab0e4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ab0e4c` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d70`](#insn-00ab0d70) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d78`](#insn-00ab0d78) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d80`](#insn-00ab0d80) → [`00ab0e34`](#insn-00ab0e34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d88`](#insn-00ab0d88) → [`0044d968`](../0044d/0044d968.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044d968` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d8c`](#insn-00ab0d8c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d94`](#insn-00ab0d94) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0d9c`](#insn-00ab0d9c) → [`00ab0e34`](#insn-00ab0e34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0da0`](#insn-00ab0da0) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e34`](#insn-00ab0e34) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aafb20`](#insn-00aafb20)

~~~json
{
  "source": "00aafb20",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb24`](#insn-00aafb24)

~~~json
{
  "source": "00aafb24",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb28`](#insn-00aafb28)

~~~json
{
  "source": "00aafb28",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb2c`](#insn-00aafb2c)

~~~json
{
  "source": "00aafb2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb30`](#insn-00aafb30)

~~~json
{
  "source": "00aafb30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb34`](#insn-00aafb34)

~~~json
{
  "source": "00aafb34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb40`](#insn-00aafb40)

~~~json
{
  "source": "00aafb40",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb48`](#insn-00aafb48)

~~~json
{
  "source": "00aafb48",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb50`](#insn-00aafb50)

~~~json
{
  "source": "00aafb50",
  "target": "00aaf9b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafb5c`](#insn-00aafb5c)

~~~json
{
  "source": "00aafb5c",
  "target": "00aafb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb68`](#insn-00aafb68)

~~~json
{
  "source": "00aafb68",
  "target": "00ab0cd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb70`](#insn-00aafb70)

~~~json
{
  "source": "00aafb70",
  "target": "00aafb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafb74`](#insn-00aafb74)

~~~json
{
  "source": "00aafb74",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafbcc`](#insn-00aafbcc)

~~~json
{
  "source": "00aafbcc",
  "target": "00aafb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafbd0`](#insn-00aafbd0)

~~~json
{
  "source": "00aafbd0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc20`](#insn-00aafc20)

~~~json
{
  "source": "00aafc20",
  "target": "00aafb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc24`](#insn-00aafc24)

~~~json
{
  "source": "00aafc24",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc30`](#insn-00aafc30)

~~~json
{
  "source": "00aafc30",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafc34`](#insn-00aafc34)

~~~json
{
  "source": "00aafc34",
  "target": "00aafc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc3c`](#insn-00aafc3c)

~~~json
{
  "source": "00aafc3c",
  "target": "00aafc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc48`](#insn-00aafc48)

~~~json
{
  "source": "00aafc48",
  "target": "00aafc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc58`](#insn-00aafc58)

~~~json
{
  "source": "00aafc58",
  "target": "00aafc40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc5c`](#insn-00aafc5c)

~~~json
{
  "source": "00aafc5c",
  "target": "00aafcc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc64`](#insn-00aafc64)

~~~json
{
  "source": "00aafc64",
  "target": "00aafc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafc70`](#insn-00aafc70)

~~~json
{
  "source": "00aafc70",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafc94`](#insn-00aafc94)

~~~json
{
  "source": "00aafc94",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafc98`](#insn-00aafc98)

~~~json
{
  "source": "00aafc98",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafca4`](#insn-00aafca4)

~~~json
{
  "source": "00aafca4",
  "target": "00aafcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafca8`](#insn-00aafca8)

~~~json
{
  "source": "00aafca8",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafcac`](#insn-00aafcac)

~~~json
{
  "source": "00aafcac",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafcb0`](#insn-00aafcb0)

~~~json
{
  "source": "00aafcb0",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafcb4`](#insn-00aafcb4)

~~~json
{
  "source": "00aafcb4",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafcb8`](#insn-00aafcb8)

~~~json
{
  "source": "00aafcb8",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafcc0`](#insn-00aafcc0)

~~~json
{
  "source": "00aafcc0",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafcc4`](#insn-00aafcc4)

~~~json
{
  "source": "00aafcc4",
  "target": "00aafccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafcd8`](#insn-00aafcd8)

~~~json
{
  "source": "00aafcd8",
  "target": "00aafde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafce0`](#insn-00aafce0)

~~~json
{
  "source": "00aafce0",
  "target": "00aafcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafcf8`](#insn-00aafcf8)

~~~json
{
  "source": "00aafcf8",
  "target": "00aafd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd04`](#insn-00aafd04)

~~~json
{
  "source": "00aafd04",
  "target": "00aafd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd10`](#insn-00aafd10)

~~~json
{
  "source": "00aafd10",
  "target": "00aafd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd14`](#insn-00aafd14)

~~~json
{
  "source": "00aafd14",
  "target": "00aafce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd28`](#insn-00aafd28)

~~~json
{
  "source": "00aafd28",
  "target": "00aafd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd2c`](#insn-00aafd2c)

~~~json
{
  "source": "00aafd2c",
  "target": "00aafce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd34`](#insn-00aafd34)

~~~json
{
  "source": "00aafd34",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd38`](#insn-00aafd38)

~~~json
{
  "source": "00aafd38",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd3c`](#insn-00aafd3c)

~~~json
{
  "source": "00aafd3c",
  "target": "00aafdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd40`](#insn-00aafd40)

~~~json
{
  "source": "00aafd40",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafd4c`](#insn-00aafd4c)

~~~json
{
  "source": "00aafd4c",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafd50`](#insn-00aafd50)

~~~json
{
  "source": "00aafd50",
  "target": "00aafd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd58`](#insn-00aafd58)

~~~json
{
  "source": "00aafd58",
  "target": "00aafd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd64`](#insn-00aafd64)

~~~json
{
  "source": "00aafd64",
  "target": "00aafd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd74`](#insn-00aafd74)

~~~json
{
  "source": "00aafd74",
  "target": "00aafd5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd78`](#insn-00aafd78)

~~~json
{
  "source": "00aafd78",
  "target": "00aafff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd80`](#insn-00aafd80)

~~~json
{
  "source": "00aafd80",
  "target": "00aafd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafd8c`](#insn-00aafd8c)

~~~json
{
  "source": "00aafd8c",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafdb0`](#insn-00aafdb0)

~~~json
{
  "source": "00aafdb0",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafdb4`](#insn-00aafdb4)

~~~json
{
  "source": "00aafdb4",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafdc0`](#insn-00aafdc0)

~~~json
{
  "source": "00aafdc0",
  "target": "00aafdcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafdc4`](#insn-00aafdc4)

~~~json
{
  "source": "00aafdc4",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafdc8`](#insn-00aafdc8)

~~~json
{
  "source": "00aafdc8",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafdcc`](#insn-00aafdcc)

~~~json
{
  "source": "00aafdcc",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafdd0`](#insn-00aafdd0)

~~~json
{
  "source": "00aafdd0",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafdd4`](#insn-00aafdd4)

~~~json
{
  "source": "00aafdd4",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafddc`](#insn-00aafddc)

~~~json
{
  "source": "00aafddc",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafde0`](#insn-00aafde0)

~~~json
{
  "source": "00aafde0",
  "target": "00aafff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafde8`](#insn-00aafde8)

~~~json
{
  "source": "00aafde8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafdec`](#insn-00aafdec)

~~~json
{
  "source": "00aafdec",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafdf4`](#insn-00aafdf4)

~~~json
{
  "source": "00aafdf4",
  "target": "00aafe0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafdfc`](#insn-00aafdfc)

~~~json
{
  "source": "00aafdfc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe08`](#insn-00aafe08)

~~~json
{
  "source": "00aafe08",
  "target": "00ab02a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe0c`](#insn-00aafe0c)

~~~json
{
  "source": "00aafe0c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafe18`](#insn-00aafe18)

~~~json
{
  "source": "00aafe18",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafe1c`](#insn-00aafe1c)

~~~json
{
  "source": "00aafe1c",
  "target": "00aafe34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe24`](#insn-00aafe24)

~~~json
{
  "source": "00aafe24",
  "target": "00aafe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe30`](#insn-00aafe30)

~~~json
{
  "source": "00aafe30",
  "target": "00aafe54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe40`](#insn-00aafe40)

~~~json
{
  "source": "00aafe40",
  "target": "00aafe28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe44`](#insn-00aafe44)

~~~json
{
  "source": "00aafe44",
  "target": "00aafeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe4c`](#insn-00aafe4c)

~~~json
{
  "source": "00aafe4c",
  "target": "00aafe34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe58`](#insn-00aafe58)

~~~json
{
  "source": "00aafe58",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafe7c`](#insn-00aafe7c)

~~~json
{
  "source": "00aafe7c",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafe80`](#insn-00aafe80)

~~~json
{
  "source": "00aafe80",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafe8c`](#insn-00aafe8c)

~~~json
{
  "source": "00aafe8c",
  "target": "00aafe98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafe90`](#insn-00aafe90)

~~~json
{
  "source": "00aafe90",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafe94`](#insn-00aafe94)

~~~json
{
  "source": "00aafe94",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafe98`](#insn-00aafe98)

~~~json
{
  "source": "00aafe98",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafe9c`](#insn-00aafe9c)

~~~json
{
  "source": "00aafe9c",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafea0`](#insn-00aafea0)

~~~json
{
  "source": "00aafea0",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafea8`](#insn-00aafea8)

~~~json
{
  "source": "00aafea8",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aafeac`](#insn-00aafeac)

~~~json
{
  "source": "00aafeac",
  "target": "00aafeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafebc`](#insn-00aafebc)

~~~json
{
  "source": "00aafebc",
  "target": "00aafed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafec4`](#insn-00aafec4)

~~~json
{
  "source": "00aafec4",
  "target": "00aafef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafed0`](#insn-00aafed0)

~~~json
{
  "source": "00aafed0",
  "target": "00aafef8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafee0`](#insn-00aafee0)

~~~json
{
  "source": "00aafee0",
  "target": "00aafec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafee8`](#insn-00aafee8)

~~~json
{
  "source": "00aafee8",
  "target": "00aaff50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafef0`](#insn-00aafef0)

~~~json
{
  "source": "00aafef0",
  "target": "00aafed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aafefc`](#insn-00aafefc)

~~~json
{
  "source": "00aafefc",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaff24`](#insn-00aaff24)

~~~json
{
  "source": "00aaff24",
  "target": "00aaff30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff34`](#insn-00aaff34)

~~~json
{
  "source": "00aaff34",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaff48`](#insn-00aaff48)

~~~json
{
  "source": "00aaff48",
  "target": "00aafe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff4c`](#insn-00aaff4c)

~~~json
{
  "source": "00aaff4c",
  "target": "00aaff5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff58`](#insn-00aaff58)

~~~json
{
  "source": "00aaff58",
  "target": "00aafe00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff5c`](#insn-00aaff5c)

~~~json
{
  "source": "00aaff5c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff64`](#insn-00aaff64)

~~~json
{
  "source": "00aaff64",
  "target": "00aafdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff68`](#insn-00aaff68)

~~~json
{
  "source": "00aaff68",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaff7c`](#insn-00aaff7c)

~~~json
{
  "source": "00aaff7c",
  "target": "00ab0d1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffa0`](#insn-00aaffa0)

~~~json
{
  "source": "00aaffa0",
  "target": "00aaffbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffa8`](#insn-00aaffa8)

~~~json
{
  "source": "00aaffa8",
  "target": "00ab0d38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffb0`](#insn-00aaffb0)

~~~json
{
  "source": "00aaffb0",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaffb8`](#insn-00aaffb8)

~~~json
{
  "source": "00aaffb8",
  "target": "00aaffc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffd8`](#insn-00aaffd8)

~~~json
{
  "source": "00aaffd8",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaffdc`](#insn-00aaffdc)

~~~json
{
  "source": "00aaffdc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffe0`](#insn-00aaffe0)

~~~json
{
  "source": "00aaffe0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffe4`](#insn-00aaffe4)

~~~json
{
  "source": "00aaffe4",
  "target": "00aafdfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaffec`](#insn-00aaffec)

~~~json
{
  "source": "00aaffec",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aafff0`](#insn-00aafff0)

~~~json
{
  "source": "00aafff0",
  "target": "00aafdfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0000`](#insn-00ab0000)

~~~json
{
  "source": "00ab0000",
  "target": "00ab0018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0008`](#insn-00ab0008)

~~~json
{
  "source": "00ab0008",
  "target": "00ab003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0014`](#insn-00ab0014)

~~~json
{
  "source": "00ab0014",
  "target": "00ab003c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0024`](#insn-00ab0024)

~~~json
{
  "source": "00ab0024",
  "target": "00ab000c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab002c`](#insn-00ab002c)

~~~json
{
  "source": "00ab002c",
  "target": "00ab0098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0034`](#insn-00ab0034)

~~~json
{
  "source": "00ab0034",
  "target": "00ab0018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0040`](#insn-00ab0040)

~~~json
{
  "source": "00ab0040",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab006c`](#insn-00ab006c)

~~~json
{
  "source": "00ab006c",
  "target": "00ab0078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab007c`](#insn-00ab007c)

~~~json
{
  "source": "00ab007c",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0090`](#insn-00ab0090)

~~~json
{
  "source": "00ab0090",
  "target": "00ab00a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0094`](#insn-00ab0094)

~~~json
{
  "source": "00ab0094",
  "target": "00aafdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab00a0`](#insn-00ab00a0)

~~~json
{
  "source": "00ab00a0",
  "target": "00aafdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab00a8`](#insn-00ab00a8)

~~~json
{
  "source": "00ab00a8",
  "target": "00ab00d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab00b0`](#insn-00ab00b0)

~~~json
{
  "source": "00ab00b0",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab00c4`](#insn-00ab00c4)

~~~json
{
  "source": "00ab00c4",
  "target": "00ab0208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab00d0`](#insn-00ab00d0)

~~~json
{
  "source": "00ab00d0",
  "target": "00ab02a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab00d4`](#insn-00ab00d4)

~~~json
{
  "source": "00ab00d4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab00e0`](#insn-00ab00e0)

~~~json
{
  "source": "00ab00e0",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab00e4`](#insn-00ab00e4)

~~~json
{
  "source": "00ab00e4",
  "target": "00ab00fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab00ec`](#insn-00ab00ec)

~~~json
{
  "source": "00ab00ec",
  "target": "00ab011c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab00f8`](#insn-00ab00f8)

~~~json
{
  "source": "00ab00f8",
  "target": "00ab011c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0108`](#insn-00ab0108)

~~~json
{
  "source": "00ab0108",
  "target": "00ab00f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab010c`](#insn-00ab010c)

~~~json
{
  "source": "00ab010c",
  "target": "00ab0178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0114`](#insn-00ab0114)

~~~json
{
  "source": "00ab0114",
  "target": "00ab00fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0120`](#insn-00ab0120)

~~~json
{
  "source": "00ab0120",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0144`](#insn-00ab0144)

~~~json
{
  "source": "00ab0144",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0148`](#insn-00ab0148)

~~~json
{
  "source": "00ab0148",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0154`](#insn-00ab0154)

~~~json
{
  "source": "00ab0154",
  "target": "00ab0160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0158`](#insn-00ab0158)

~~~json
{
  "source": "00ab0158",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab015c`](#insn-00ab015c)

~~~json
{
  "source": "00ab015c",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0160`](#insn-00ab0160)

~~~json
{
  "source": "00ab0160",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0164`](#insn-00ab0164)

~~~json
{
  "source": "00ab0164",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0168`](#insn-00ab0168)

~~~json
{
  "source": "00ab0168",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0170`](#insn-00ab0170)

~~~json
{
  "source": "00ab0170",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0174`](#insn-00ab0174)

~~~json
{
  "source": "00ab0174",
  "target": "00ab017c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0184`](#insn-00ab0184)

~~~json
{
  "source": "00ab0184",
  "target": "00ab019c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab018c`](#insn-00ab018c)

~~~json
{
  "source": "00ab018c",
  "target": "00ab01c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0198`](#insn-00ab0198)

~~~json
{
  "source": "00ab0198",
  "target": "00ab01c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab01a8`](#insn-00ab01a8)

~~~json
{
  "source": "00ab01a8",
  "target": "00ab0190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab01b0`](#insn-00ab01b0)

~~~json
{
  "source": "00ab01b0",
  "target": "00ab01fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab01b8`](#insn-00ab01b8)

~~~json
{
  "source": "00ab01b8",
  "target": "00ab019c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab01c4`](#insn-00ab01c4)

~~~json
{
  "source": "00ab01c4",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab01ec`](#insn-00ab01ec)

~~~json
{
  "source": "00ab01ec",
  "target": "00ab00ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab01f8`](#insn-00ab01f8)

~~~json
{
  "source": "00ab01f8",
  "target": "00ab00ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0204`](#insn-00ab0204)

~~~json
{
  "source": "00ab0204",
  "target": "00ab00c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0208`](#insn-00ab0208)

~~~json
{
  "source": "00ab0208",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0210`](#insn-00ab0210)

~~~json
{
  "source": "00ab0210",
  "target": "00ab021c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0218`](#insn-00ab0218)

~~~json
{
  "source": "00ab0218",
  "target": "00ab02a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab021c`](#insn-00ab021c)

~~~json
{
  "source": "00ab021c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0230`](#insn-00ab0230)

~~~json
{
  "source": "00ab0230",
  "target": "00ab0d70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0254`](#insn-00ab0254)

~~~json
{
  "source": "00ab0254",
  "target": "00ab0270",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab025c`](#insn-00ab025c)

~~~json
{
  "source": "00ab025c",
  "target": "00ab0d8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0264`](#insn-00ab0264)

~~~json
{
  "source": "00ab0264",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab026c`](#insn-00ab026c)

~~~json
{
  "source": "00ab026c",
  "target": "00ab0274",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab028c`](#insn-00ab028c)

~~~json
{
  "source": "00ab028c",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0290`](#insn-00ab0290)

~~~json
{
  "source": "00ab0290",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0294`](#insn-00ab0294)

~~~json
{
  "source": "00ab0294",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0298`](#insn-00ab0298)

~~~json
{
  "source": "00ab0298",
  "target": "00ab02a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab02a0`](#insn-00ab02a0)

~~~json
{
  "source": "00ab02a0",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab02a4`](#insn-00ab02a4)

~~~json
{
  "source": "00ab02a4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab02a8`](#insn-00ab02a8)

~~~json
{
  "source": "00ab02a8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab02b0`](#insn-00ab02b0)

~~~json
{
  "source": "00ab02b0",
  "target": "00ab0d50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab02bc`](#insn-00ab02bc)

~~~json
{
  "source": "00ab02bc",
  "target": "00ab02c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab02c4`](#insn-00ab02c4)

~~~json
{
  "source": "00ab02c4",
  "target": "00ab02f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab02d4`](#insn-00ab02d4)

~~~json
{
  "source": "00ab02d4",
  "target": "00ab02e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab02e4`](#insn-00ab02e4)

~~~json
{
  "source": "00ab02e4",
  "target": "00ab02cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab02f0`](#insn-00ab02f0)

~~~json
{
  "source": "00ab02f0",
  "target": "Stack[-0xa4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab02f4`](#insn-00ab02f4)

~~~json
{
  "source": "00ab02f4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0300`](#insn-00ab0300)

~~~json
{
  "source": "00ab0300",
  "target": "00ab0664",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0308`](#insn-00ab0308)

~~~json
{
  "source": "00ab0308",
  "target": "00ab0708",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0314`](#insn-00ab0314)

~~~json
{
  "source": "00ab0314",
  "target": "00ab0338",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0324`](#insn-00ab0324)

~~~json
{
  "source": "00ab0324",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0328`](#insn-00ab0328)

~~~json
{
  "source": "00ab0328",
  "target": "00ab070c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0334`](#insn-00ab0334)

~~~json
{
  "source": "00ab0334",
  "target": "00ab070c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab033c`](#insn-00ab033c)

~~~json
{
  "source": "00ab033c",
  "target": "0044a8d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0340`](#insn-00ab0340)

~~~json
{
  "source": "00ab0340",
  "target": "Stack[-0xa4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0348`](#insn-00ab0348)

~~~json
{
  "source": "00ab0348",
  "target": "00ab032c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab034c`](#insn-00ab034c)

~~~json
{
  "source": "00ab034c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0358`](#insn-00ab0358)

~~~json
{
  "source": "00ab0358",
  "target": "0044a8d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab035c`](#insn-00ab035c)

~~~json
{
  "source": "00ab035c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0368`](#insn-00ab0368)

~~~json
{
  "source": "00ab0368",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0374`](#insn-00ab0374)

~~~json
{
  "source": "00ab0374",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0378`](#insn-00ab0378)

~~~json
{
  "source": "00ab0378",
  "target": "00ab0390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0380`](#insn-00ab0380)

~~~json
{
  "source": "00ab0380",
  "target": "00ab03b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab038c`](#insn-00ab038c)

~~~json
{
  "source": "00ab038c",
  "target": "00ab03b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab039c`](#insn-00ab039c)

~~~json
{
  "source": "00ab039c",
  "target": "00ab0384",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab03a0`](#insn-00ab03a0)

~~~json
{
  "source": "00ab03a0",
  "target": "00ab040c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab03a8`](#insn-00ab03a8)

~~~json
{
  "source": "00ab03a8",
  "target": "00ab0390",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab03b4`](#insn-00ab03b4)

~~~json
{
  "source": "00ab03b4",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab03d8`](#insn-00ab03d8)

~~~json
{
  "source": "00ab03d8",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab03dc`](#insn-00ab03dc)

~~~json
{
  "source": "00ab03dc",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab03e8`](#insn-00ab03e8)

~~~json
{
  "source": "00ab03e8",
  "target": "00ab03f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab03ec`](#insn-00ab03ec)

~~~json
{
  "source": "00ab03ec",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab03f0`](#insn-00ab03f0)

~~~json
{
  "source": "00ab03f0",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab03f4`](#insn-00ab03f4)

~~~json
{
  "source": "00ab03f4",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab03f8`](#insn-00ab03f8)

~~~json
{
  "source": "00ab03f8",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab03fc`](#insn-00ab03fc)

~~~json
{
  "source": "00ab03fc",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0404`](#insn-00ab0404)

~~~json
{
  "source": "00ab0404",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0408`](#insn-00ab0408)

~~~json
{
  "source": "00ab0408",
  "target": "00ab0410",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0418`](#insn-00ab0418)

~~~json
{
  "source": "00ab0418",
  "target": "00ab0430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0420`](#insn-00ab0420)

~~~json
{
  "source": "00ab0420",
  "target": "00ab0454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab042c`](#insn-00ab042c)

~~~json
{
  "source": "00ab042c",
  "target": "00ab0454",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab043c`](#insn-00ab043c)

~~~json
{
  "source": "00ab043c",
  "target": "00ab0424",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0444`](#insn-00ab0444)

~~~json
{
  "source": "00ab0444",
  "target": "00ab04ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab044c`](#insn-00ab044c)

~~~json
{
  "source": "00ab044c",
  "target": "00ab0430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0458`](#insn-00ab0458)

~~~json
{
  "source": "00ab0458",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0480`](#insn-00ab0480)

~~~json
{
  "source": "00ab0480",
  "target": "00ab048c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0490`](#insn-00ab0490)

~~~json
{
  "source": "00ab0490",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab04a4`](#insn-00ab04a4)

~~~json
{
  "source": "00ab04a4",
  "target": "00ab032c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab04a8`](#insn-00ab04a8)

~~~json
{
  "source": "00ab04a8",
  "target": "00ab04b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab04b4`](#insn-00ab04b4)

~~~json
{
  "source": "00ab04b4",
  "target": "00ab032c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab04b8`](#insn-00ab04b8)

~~~json
{
  "source": "00ab04b8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab04c0`](#insn-00ab04c0)

~~~json
{
  "source": "00ab04c0",
  "target": "007ac4fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab04c4`](#insn-00ab04c4)

~~~json
{
  "source": "00ab04c4",
  "target": "00ab04f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab04c8`](#insn-00ab04c8)

~~~json
{
  "source": "00ab04c8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab04d0`](#insn-00ab04d0)

~~~json
{
  "source": "00ab04d0",
  "target": "007ac574",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab04d4`](#insn-00ab04d4)

~~~json
{
  "source": "00ab04d4",
  "target": "00ab04f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab04d8`](#insn-00ab04d8)

~~~json
{
  "source": "00ab04d8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab04e4`](#insn-00ab04e4)

~~~json
{
  "source": "00ab04e4",
  "target": "00334058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334045",
  "offset": 19,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e20480c1d2093049e069d08580c1f20480e00d3dedd",
  "capture_start": "00334045",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab04ec`](#insn-00ab04ec)

~~~json
{
  "source": "00ab04ec",
  "target": "00ab032c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab04f0`](#insn-00ab04f0)

~~~json
{
  "source": "00ab04f0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab04fc`](#insn-00ab04fc)

~~~json
{
  "source": "00ab04fc",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0500`](#insn-00ab0500)

~~~json
{
  "source": "00ab0500",
  "target": "00ab0518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0508`](#insn-00ab0508)

~~~json
{
  "source": "00ab0508",
  "target": "00ab0538",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0514`](#insn-00ab0514)

~~~json
{
  "source": "00ab0514",
  "target": "00ab0538",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0524`](#insn-00ab0524)

~~~json
{
  "source": "00ab0524",
  "target": "00ab050c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0528`](#insn-00ab0528)

~~~json
{
  "source": "00ab0528",
  "target": "00ab0594",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0530`](#insn-00ab0530)

~~~json
{
  "source": "00ab0530",
  "target": "00ab0518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab053c`](#insn-00ab053c)

~~~json
{
  "source": "00ab053c",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0560`](#insn-00ab0560)

~~~json
{
  "source": "00ab0560",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0564`](#insn-00ab0564)

~~~json
{
  "source": "00ab0564",
  "target": "00334018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333ff9",
  "offset": 31,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "00333ff9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab0570`](#insn-00ab0570)

~~~json
{
  "source": "00ab0570",
  "target": "00ab057c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0574`](#insn-00ab0574)

~~~json
{
  "source": "00ab0574",
  "target": "00334018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333ff9",
  "offset": 31,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "00333ff9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab0578`](#insn-00ab0578)

~~~json
{
  "source": "00ab0578",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab057c`](#insn-00ab057c)

~~~json
{
  "source": "00ab057c",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0580`](#insn-00ab0580)

~~~json
{
  "source": "00ab0580",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0584`](#insn-00ab0584)

~~~json
{
  "source": "00ab0584",
  "target": "00334028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334028",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "64031300",
  "capture_start": "00334028",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab058c`](#insn-00ab058c)

~~~json
{
  "source": "00ab058c",
  "target": "00334028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334028",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "64031300",
  "capture_start": "00334028",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0590`](#insn-00ab0590)

~~~json
{
  "source": "00ab0590",
  "target": "00ab0598",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab05a0`](#insn-00ab05a0)

~~~json
{
  "source": "00ab05a0",
  "target": "00ab05b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab05a8`](#insn-00ab05a8)

~~~json
{
  "source": "00ab05a8",
  "target": "00ab05dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab05b4`](#insn-00ab05b4)

~~~json
{
  "source": "00ab05b4",
  "target": "00ab05dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab05c4`](#insn-00ab05c4)

~~~json
{
  "source": "00ab05c4",
  "target": "00ab05ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab05cc`](#insn-00ab05cc)

~~~json
{
  "source": "00ab05cc",
  "target": "00ab062c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab05d4`](#insn-00ab05d4)

~~~json
{
  "source": "00ab05d4",
  "target": "00ab05b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab05e0`](#insn-00ab05e0)

~~~json
{
  "source": "00ab05e0",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0608`](#insn-00ab0608)

~~~json
{
  "source": "00ab0608",
  "target": "00ab0614",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0618`](#insn-00ab0618)

~~~json
{
  "source": "00ab0618",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0628`](#insn-00ab0628)

~~~json
{
  "source": "00ab0628",
  "target": "00ab0630",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0630`](#insn-00ab0630)

~~~json
{
  "source": "00ab0630",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab064c`](#insn-00ab064c)

~~~json
{
  "source": "00ab064c",
  "target": "00ab0318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0658`](#insn-00ab0658)

~~~json
{
  "source": "00ab0658",
  "target": "00bdb0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab065c`](#insn-00ab065c)

~~~json
{
  "source": "00ab065c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0660`](#insn-00ab0660)

~~~json
{
  "source": "00ab0660",
  "target": "00ab0318",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0664`](#insn-00ab0664)

~~~json
{
  "source": "00ab0664",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0670`](#insn-00ab0670)

~~~json
{
  "source": "00ab0670",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0674`](#insn-00ab0674)

~~~json
{
  "source": "00ab0674",
  "target": "00ab068c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab067c`](#insn-00ab067c)

~~~json
{
  "source": "00ab067c",
  "target": "00ab06ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0688`](#insn-00ab0688)

~~~json
{
  "source": "00ab0688",
  "target": "00ab06ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0698`](#insn-00ab0698)

~~~json
{
  "source": "00ab0698",
  "target": "00ab0680",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab069c`](#insn-00ab069c)

~~~json
{
  "source": "00ab069c",
  "target": "00ab0a6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab06a4`](#insn-00ab06a4)

~~~json
{
  "source": "00ab06a4",
  "target": "00ab068c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab06b0`](#insn-00ab06b0)

~~~json
{
  "source": "00ab06b0",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab06d4`](#insn-00ab06d4)

~~~json
{
  "source": "00ab06d4",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab06d8`](#insn-00ab06d8)

~~~json
{
  "source": "00ab06d8",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab06e4`](#insn-00ab06e4)

~~~json
{
  "source": "00ab06e4",
  "target": "00ab06f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab06e8`](#insn-00ab06e8)

~~~json
{
  "source": "00ab06e8",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab06ec`](#insn-00ab06ec)

~~~json
{
  "source": "00ab06ec",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab06f0`](#insn-00ab06f0)

~~~json
{
  "source": "00ab06f0",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab06f4`](#insn-00ab06f4)

~~~json
{
  "source": "00ab06f4",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab06f8`](#insn-00ab06f8)

~~~json
{
  "source": "00ab06f8",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0700`](#insn-00ab0700)

~~~json
{
  "source": "00ab0700",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0704`](#insn-00ab0704)

~~~json
{
  "source": "00ab0704",
  "target": "00ab0a70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0718`](#insn-00ab0718)

~~~json
{
  "source": "00ab0718",
  "target": "00ab0cc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab071c`](#insn-00ab071c)

~~~json
{
  "source": "00ab071c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0724`](#insn-00ab0724)

~~~json
{
  "source": "00ab0724",
  "target": "00ab0cc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab072c`](#insn-00ab072c)

~~~json
{
  "source": "00ab072c",
  "target": "00ab0cc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0734`](#insn-00ab0734)

~~~json
{
  "source": "00ab0734",
  "target": "00ab0754",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0740`](#insn-00ab0740)

~~~json
{
  "source": "00ab0740",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0744`](#insn-00ab0744)

~~~json
{
  "source": "00ab0744",
  "target": "00ab0cc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0750`](#insn-00ab0750)

~~~json
{
  "source": "00ab0750",
  "target": "00ab0cc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0754`](#insn-00ab0754)

~~~json
{
  "source": "00ab0754",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0760`](#insn-00ab0760)

~~~json
{
  "source": "00ab0760",
  "target": "0044a8d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0764`](#insn-00ab0764)

~~~json
{
  "source": "00ab0764",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0770`](#insn-00ab0770)

~~~json
{
  "source": "00ab0770",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab077c`](#insn-00ab077c)

~~~json
{
  "source": "00ab077c",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0780`](#insn-00ab0780)

~~~json
{
  "source": "00ab0780",
  "target": "00ab0798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0788`](#insn-00ab0788)

~~~json
{
  "source": "00ab0788",
  "target": "00ab07b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0794`](#insn-00ab0794)

~~~json
{
  "source": "00ab0794",
  "target": "00ab07b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab07a4`](#insn-00ab07a4)

~~~json
{
  "source": "00ab07a4",
  "target": "00ab078c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab07a8`](#insn-00ab07a8)

~~~json
{
  "source": "00ab07a8",
  "target": "00ab0814",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab07b0`](#insn-00ab07b0)

~~~json
{
  "source": "00ab07b0",
  "target": "00ab0798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab07bc`](#insn-00ab07bc)

~~~json
{
  "source": "00ab07bc",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab07e0`](#insn-00ab07e0)

~~~json
{
  "source": "00ab07e0",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab07e4`](#insn-00ab07e4)

~~~json
{
  "source": "00ab07e4",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab07f0`](#insn-00ab07f0)

~~~json
{
  "source": "00ab07f0",
  "target": "00ab07fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab07f4`](#insn-00ab07f4)

~~~json
{
  "source": "00ab07f4",
  "target": "00334030",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033402c",
  "offset": 4,
  "size": 8,
  "datatype": "qword",
  "bytes": "1000000000000000",
  "capture_start": "0033402c",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab07f8`](#insn-00ab07f8)

~~~json
{
  "source": "00ab07f8",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab07fc`](#insn-00ab07fc)

~~~json
{
  "source": "00ab07fc",
  "target": "00334038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334038",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "408b0000",
  "capture_start": "00334038",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0800`](#insn-00ab0800)

~~~json
{
  "source": "00ab0800",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0804`](#insn-00ab0804)

~~~json
{
  "source": "00ab0804",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab080c`](#insn-00ab080c)

~~~json
{
  "source": "00ab080c",
  "target": "00334040",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334040",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "30000000",
  "capture_start": "00334040",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0810`](#insn-00ab0810)

~~~json
{
  "source": "00ab0810",
  "target": "00ab0818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0820`](#insn-00ab0820)

~~~json
{
  "source": "00ab0820",
  "target": "00ab0838",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0828`](#insn-00ab0828)

~~~json
{
  "source": "00ab0828",
  "target": "00ab085c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0834`](#insn-00ab0834)

~~~json
{
  "source": "00ab0834",
  "target": "00ab085c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0844`](#insn-00ab0844)

~~~json
{
  "source": "00ab0844",
  "target": "00ab082c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab084c`](#insn-00ab084c)

~~~json
{
  "source": "00ab084c",
  "target": "00ab08b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0854`](#insn-00ab0854)

~~~json
{
  "source": "00ab0854",
  "target": "00ab0838",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0860`](#insn-00ab0860)

~~~json
{
  "source": "00ab0860",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0888`](#insn-00ab0888)

~~~json
{
  "source": "00ab0888",
  "target": "00ab0894",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0898`](#insn-00ab0898)

~~~json
{
  "source": "00ab0898",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab08ac`](#insn-00ab08ac)

~~~json
{
  "source": "00ab08ac",
  "target": "00ab0748",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab08b0`](#insn-00ab08b0)

~~~json
{
  "source": "00ab08b0",
  "target": "00ab08c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab08bc`](#insn-00ab08bc)

~~~json
{
  "source": "00ab08bc",
  "target": "00ab0748",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab08c0`](#insn-00ab08c0)

~~~json
{
  "source": "00ab08c0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab08c8`](#insn-00ab08c8)

~~~json
{
  "source": "00ab08c8",
  "target": "007ac4fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab08cc`](#insn-00ab08cc)

~~~json
{
  "source": "00ab08cc",
  "target": "00ab08f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab08d0`](#insn-00ab08d0)

~~~json
{
  "source": "00ab08d0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab08d8`](#insn-00ab08d8)

~~~json
{
  "source": "00ab08d8",
  "target": "007ac574",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab08dc`](#insn-00ab08dc)

~~~json
{
  "source": "00ab08dc",
  "target": "00ab08f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab08e0`](#insn-00ab08e0)

~~~json
{
  "source": "00ab08e0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab08ec`](#insn-00ab08ec)

~~~json
{
  "source": "00ab08ec",
  "target": "00334058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334045",
  "offset": 19,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e20480c1d2093049e069d08580c1f20480e00d3dedd",
  "capture_start": "00334045",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab08f4`](#insn-00ab08f4)

~~~json
{
  "source": "00ab08f4",
  "target": "00ab0748",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab08f8`](#insn-00ab08f8)

~~~json
{
  "source": "00ab08f8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0904`](#insn-00ab0904)

~~~json
{
  "source": "00ab0904",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0908`](#insn-00ab0908)

~~~json
{
  "source": "00ab0908",
  "target": "00ab0920",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0910`](#insn-00ab0910)

~~~json
{
  "source": "00ab0910",
  "target": "00ab0940",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab091c`](#insn-00ab091c)

~~~json
{
  "source": "00ab091c",
  "target": "00ab0940",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab092c`](#insn-00ab092c)

~~~json
{
  "source": "00ab092c",
  "target": "00ab0914",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0930`](#insn-00ab0930)

~~~json
{
  "source": "00ab0930",
  "target": "00ab099c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0938`](#insn-00ab0938)

~~~json
{
  "source": "00ab0938",
  "target": "00ab0920",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0944`](#insn-00ab0944)

~~~json
{
  "source": "00ab0944",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0968`](#insn-00ab0968)

~~~json
{
  "source": "00ab0968",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab096c`](#insn-00ab096c)

~~~json
{
  "source": "00ab096c",
  "target": "00334018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333ff9",
  "offset": 31,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "00333ff9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab0978`](#insn-00ab0978)

~~~json
{
  "source": "00ab0978",
  "target": "00ab0984",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab097c`](#insn-00ab097c)

~~~json
{
  "source": "00ab097c",
  "target": "00334018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333ff9",
  "offset": 31,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "00333ff9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab0980`](#insn-00ab0980)

~~~json
{
  "source": "00ab0980",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0984`](#insn-00ab0984)

~~~json
{
  "source": "00ab0984",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0988`](#insn-00ab0988)

~~~json
{
  "source": "00ab0988",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab098c`](#insn-00ab098c)

~~~json
{
  "source": "00ab098c",
  "target": "00334028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334028",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "64031300",
  "capture_start": "00334028",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0994`](#insn-00ab0994)

~~~json
{
  "source": "00ab0994",
  "target": "00334028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334028",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "64031300",
  "capture_start": "00334028",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0998`](#insn-00ab0998)

~~~json
{
  "source": "00ab0998",
  "target": "00ab09a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab09a8`](#insn-00ab09a8)

~~~json
{
  "source": "00ab09a8",
  "target": "00ab09c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab09b0`](#insn-00ab09b0)

~~~json
{
  "source": "00ab09b0",
  "target": "00ab09e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab09bc`](#insn-00ab09bc)

~~~json
{
  "source": "00ab09bc",
  "target": "00ab09e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab09cc`](#insn-00ab09cc)

~~~json
{
  "source": "00ab09cc",
  "target": "00ab09b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab09d4`](#insn-00ab09d4)

~~~json
{
  "source": "00ab09d4",
  "target": "00ab0a34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab09dc`](#insn-00ab09dc)

~~~json
{
  "source": "00ab09dc",
  "target": "00ab09c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab09e8`](#insn-00ab09e8)

~~~json
{
  "source": "00ab09e8",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0a10`](#insn-00ab0a10)

~~~json
{
  "source": "00ab0a10",
  "target": "00ab0a1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0a20`](#insn-00ab0a20)

~~~json
{
  "source": "00ab0a20",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0a30`](#insn-00ab0a30)

~~~json
{
  "source": "00ab0a30",
  "target": "00ab0a38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0a38`](#insn-00ab0a38)

~~~json
{
  "source": "00ab0a38",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0a54`](#insn-00ab0a54)

~~~json
{
  "source": "00ab0a54",
  "target": "00ab0738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0a60`](#insn-00ab0a60)

~~~json
{
  "source": "00ab0a60",
  "target": "00bdb0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0a64`](#insn-00ab0a64)

~~~json
{
  "source": "00ab0a64",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0a68`](#insn-00ab0a68)

~~~json
{
  "source": "00ab0a68",
  "target": "00ab0738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0a78`](#insn-00ab0a78)

~~~json
{
  "source": "00ab0a78",
  "target": "00ab0a90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0a80`](#insn-00ab0a80)

~~~json
{
  "source": "00ab0a80",
  "target": "00ab0ab4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0a8c`](#insn-00ab0a8c)

~~~json
{
  "source": "00ab0a8c",
  "target": "00ab0ab4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0a9c`](#insn-00ab0a9c)

~~~json
{
  "source": "00ab0a9c",
  "target": "00ab0a84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0aa4`](#insn-00ab0aa4)

~~~json
{
  "source": "00ab0aa4",
  "target": "00ab0b10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0aac`](#insn-00ab0aac)

~~~json
{
  "source": "00ab0aac",
  "target": "00ab0a90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0ab8`](#insn-00ab0ab8)

~~~json
{
  "source": "00ab0ab8",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0ae4`](#insn-00ab0ae4)

~~~json
{
  "source": "00ab0ae4",
  "target": "00ab0af0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0af4`](#insn-00ab0af4)

~~~json
{
  "source": "00ab0af4",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0b08`](#insn-00ab0b08)

~~~json
{
  "source": "00ab0b08",
  "target": "00ab0cc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0b0c`](#insn-00ab0b0c)

~~~json
{
  "source": "00ab0b0c",
  "target": "00ab0b1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0b18`](#insn-00ab0b18)

~~~json
{
  "source": "00ab0b18",
  "target": "00ab0cc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0b20`](#insn-00ab0b20)

~~~json
{
  "source": "00ab0b20",
  "target": "0044a8d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0b28`](#insn-00ab0b28)

~~~json
{
  "source": "00ab0b28",
  "target": "Stack[-0xa4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0b3c`](#insn-00ab0b3c)

~~~json
{
  "source": "00ab0b3c",
  "target": "00ab0cc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0b40`](#insn-00ab0b40)

~~~json
{
  "source": "00ab0b40",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0b48`](#insn-00ab0b48)

~~~json
{
  "source": "00ab0b48",
  "target": "007ac4fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0b4c`](#insn-00ab0b4c)

~~~json
{
  "source": "00ab0b4c",
  "target": "00ab0b78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0b50`](#insn-00ab0b50)

~~~json
{
  "source": "00ab0b50",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0b58`](#insn-00ab0b58)

~~~json
{
  "source": "00ab0b58",
  "target": "007ac574",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0b5c`](#insn-00ab0b5c)

~~~json
{
  "source": "00ab0b5c",
  "target": "00ab0b78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0b60`](#insn-00ab0b60)

~~~json
{
  "source": "00ab0b60",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0b6c`](#insn-00ab0b6c)

~~~json
{
  "source": "00ab0b6c",
  "target": "00334058",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334045",
  "offset": 19,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "440e20480c1d2093049e069d08580c1f20480e00d3dedd",
  "capture_start": "00334045",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0b74`](#insn-00ab0b74)

~~~json
{
  "source": "00ab0b74",
  "target": "00ab0cc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0b78`](#insn-00ab0b78)

~~~json
{
  "source": "00ab0b78",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0b84`](#insn-00ab0b84)

~~~json
{
  "source": "00ab0b84",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0b88`](#insn-00ab0b88)

~~~json
{
  "source": "00ab0b88",
  "target": "00ab0ba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0b90`](#insn-00ab0b90)

~~~json
{
  "source": "00ab0b90",
  "target": "00ab0bc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0b9c`](#insn-00ab0b9c)

~~~json
{
  "source": "00ab0b9c",
  "target": "00ab0bc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0bac`](#insn-00ab0bac)

~~~json
{
  "source": "00ab0bac",
  "target": "00ab0b94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0bb0`](#insn-00ab0bb0)

~~~json
{
  "source": "00ab0bb0",
  "target": "00ab0c1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0bb8`](#insn-00ab0bb8)

~~~json
{
  "source": "00ab0bb8",
  "target": "00ab0ba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0bc4`](#insn-00ab0bc4)

~~~json
{
  "source": "00ab0bc4",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0be8`](#insn-00ab0be8)

~~~json
{
  "source": "00ab0be8",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0bec`](#insn-00ab0bec)

~~~json
{
  "source": "00ab0bec",
  "target": "00334018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333ff9",
  "offset": 31,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "00333ff9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab0bf8`](#insn-00ab0bf8)

~~~json
{
  "source": "00ab0bf8",
  "target": "00ab0c04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0bfc`](#insn-00ab0bfc)

~~~json
{
  "source": "00ab0bfc",
  "target": "00334018",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333ff9",
  "offset": 31,
  "size": 39,
  "datatype": "byte[39]",
  "bytes": "440e20480c1d2093049e069d080a580c1f20480e00d3dedd440b540c1f20480e",
  "capture_start": "00333ff9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab0c00`](#insn-00ab0c00)

~~~json
{
  "source": "00ab0c00",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0c04`](#insn-00ab0c04)

~~~json
{
  "source": "00ab0c04",
  "target": "00334020",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334020",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "00334020",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0c08`](#insn-00ab0c08)

~~~json
{
  "source": "00ab0c08",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0c0c`](#insn-00ab0c0c)

~~~json
{
  "source": "00ab0c0c",
  "target": "00334028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334028",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "64031300",
  "capture_start": "00334028",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0c14`](#insn-00ab0c14)

~~~json
{
  "source": "00ab0c14",
  "target": "00334028",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00334028",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "64031300",
  "capture_start": "00334028",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0c18`](#insn-00ab0c18)

~~~json
{
  "source": "00ab0c18",
  "target": "00ab0c20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0c28`](#insn-00ab0c28)

~~~json
{
  "source": "00ab0c28",
  "target": "00ab0c40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0c30`](#insn-00ab0c30)

~~~json
{
  "source": "00ab0c30",
  "target": "00ab0c64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0c3c`](#insn-00ab0c3c)

~~~json
{
  "source": "00ab0c3c",
  "target": "00ab0c64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0c4c`](#insn-00ab0c4c)

~~~json
{
  "source": "00ab0c4c",
  "target": "00ab0c34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0c54`](#insn-00ab0c54)

~~~json
{
  "source": "00ab0c54",
  "target": "00ab0cb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0c5c`](#insn-00ab0c5c)

~~~json
{
  "source": "00ab0c5c",
  "target": "00ab0c40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0c68`](#insn-00ab0c68)

~~~json
{
  "source": "00ab0c68",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0c94`](#insn-00ab0c94)

~~~json
{
  "source": "00ab0c94",
  "target": "00ab0ca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0ca4`](#insn-00ab0ca4)

~~~json
{
  "source": "00ab0ca4",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0cb4`](#insn-00ab0cb4)

~~~json
{
  "source": "00ab0cb4",
  "target": "00ab0cbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0cc4`](#insn-00ab0cc4)

~~~json
{
  "source": "00ab0cc4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0cc8`](#insn-00ab0cc8)

~~~json
{
  "source": "00ab0cc8",
  "target": "00aafb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0ccc`](#insn-00ab0ccc)

~~~json
{
  "source": "00ab0ccc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0cd0`](#insn-00ab0cd0)

~~~json
{
  "source": "00ab0cd0",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0cd4`](#insn-00ab0cd4)

~~~json
{
  "source": "00ab0cd4",
  "target": "00aafb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0cd8`](#insn-00ab0cd8)

~~~json
{
  "source": "00ab0cd8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0cdc`](#insn-00ab0cdc)

~~~json
{
  "source": "00ab0cdc",
  "target": "00ab0ce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0ce0`](#insn-00ab0ce0)

~~~json
{
  "source": "00ab0ce0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0ce4`](#insn-00ab0ce4)

~~~json
{
  "source": "00ab0ce4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0ce8`](#insn-00ab0ce8)

~~~json
{
  "source": "00ab0ce8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0cf0`](#insn-00ab0cf0)

~~~json
{
  "source": "00ab0cf0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0cf8`](#insn-00ab0cf8)

~~~json
{
  "source": "00ab0cf8",
  "target": "00ab0e34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0cfc`](#insn-00ab0cfc)

~~~json
{
  "source": "00ab0cfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d00`](#insn-00ab0d00)

~~~json
{
  "source": "00ab0d00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d04`](#insn-00ab0d04)

~~~json
{
  "source": "00ab0d04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d08`](#insn-00ab0d08)

~~~json
{
  "source": "00ab0d08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d0c`](#insn-00ab0d0c)

~~~json
{
  "source": "00ab0d0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d10`](#insn-00ab0d10)

~~~json
{
  "source": "00ab0d10",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d1c`](#insn-00ab0d1c)

~~~json
{
  "source": "00ab0d1c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d24`](#insn-00ab0d24)

~~~json
{
  "source": "00ab0d24",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d2c`](#insn-00ab0d2c)

~~~json
{
  "source": "00ab0d2c",
  "target": "00ab0e34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d34`](#insn-00ab0d34)

~~~json
{
  "source": "00ab0d34",
  "target": "0044d968",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0d38`](#insn-00ab0d38)

~~~json
{
  "source": "00ab0d38",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d40`](#insn-00ab0d40)

~~~json
{
  "source": "00ab0d40",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d48`](#insn-00ab0d48)

~~~json
{
  "source": "00ab0d48",
  "target": "00ab0e34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d4c`](#insn-00ab0d4c)

~~~json
{
  "source": "00ab0d4c",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0d50`](#insn-00ab0d50)

~~~json
{
  "source": "00ab0d50",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d58`](#insn-00ab0d58)

~~~json
{
  "source": "00ab0d58",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d60`](#insn-00ab0d60)

~~~json
{
  "source": "00ab0d60",
  "target": "00ab0e34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d6c`](#insn-00ab0d6c)

~~~json
{
  "source": "00ab0d6c",
  "target": "00ab0e4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0d70`](#insn-00ab0d70)

~~~json
{
  "source": "00ab0d70",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d78`](#insn-00ab0d78)

~~~json
{
  "source": "00ab0d78",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d80`](#insn-00ab0d80)

~~~json
{
  "source": "00ab0d80",
  "target": "00ab0e34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d88`](#insn-00ab0d88)

~~~json
{
  "source": "00ab0d88",
  "target": "0044d968",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0d8c`](#insn-00ab0d8c)

~~~json
{
  "source": "00ab0d8c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d94`](#insn-00ab0d94)

~~~json
{
  "source": "00ab0d94",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0d9c`](#insn-00ab0d9c)

~~~json
{
  "source": "00ab0d9c",
  "target": "00ab0e34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0da0`](#insn-00ab0da0)

~~~json
{
  "source": "00ab0da0",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0e34`](#insn-00ab0e34)

~~~json
{
  "source": "00ab0e34",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
