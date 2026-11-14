# 00ad7aec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00ad7aec",
  "name": "FUN_00ad7aec",
  "size": 1220,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "082e43f754b2f05681b462dc4418a371c11e2b0ae4e6e89a43fd4e15428b950e",
  "source_text_sha256": "082e43f754b2f05681b462dc4418a371c11e2b0ae4e6e89a43fd4e15428b950e"
}
~~~

## 呼び出し元

- [00ad19bc](../00ad1/00ad19bc.md)
- [00ad7fb0](../00ad7/00ad7fb0.md)
- [00ae1ccc](../00ae1/00ae1ccc.md)
- [00aed9f0](../00aed/00aed9f0.md)
- [00af1198](../00af1/00af1198.md)
- [00b0d2e4](../00b0d/00b0d2e4.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [005c08e0](../005c0/005c08e0.md)
- [00615d00](../00615/00615d00.md)
- [00676b3c](../00676/00676b3c.md)
- [00744198](../00744/00744198.md)
- [00744334](../00744/00744334.md)
- [00744610](../00744/00744610.md)
- [007bcd04](../007bc/007bcd04.md)
- [007df5b8](../007df/007df5b8.md)
- [007df630](../007df/007df630.md)
- [008011a8](../00801/008011a8.md)
- [00803674](../00803/00803674.md)
- [00803b14](../00803/00803b14.md)
- [00803c64](../00803/00803c64.md)
- [008621ec](../00862/008621ec.md)
- [00a33a4c](../00a33/00a33a4c.md)
- [00a33ee0](../00a33/00a33ee0.md)
- [00a43078](../00a43/00a43078.md)
- [00a43104](../00a43/00a43104.md)
- [00a43aec](../00a43/00a43aec.md)
- [00b0a6ec](../00b0a/00b0a6ec.md)
- [00b0bda4](../00b0b/00b0bda4.md)
- [00c58f30](../00c58/00c58f30.md)

## 疑似コード / UTF-8 12177 bytes

~~~c

undefined8 FUN_00ad7aec(long param_1)

{
  char cVar1;
  uint uVar2;
  int iVar3;
  undefined4 uVar4;
  undefined4 uVar5;
  undefined4 uVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  ulong uVar9;
  ulong uVar10;
  undefined8 *puVar11;
  undefined8 uVar12;
  undefined8 *puVar13;
  long *plVar14;
  long lVar15;
  long *plVar16;
  byte *pbVar17;
  long lVar18;
  ulong uVar19;
  undefined8 *puVar20;
  long lVar21;
  char *pcVar22;
  
                    /* try { // try from 00ad7af4 to 00bd7b03 has its CatchHandler @ 00ad8904 */
                    /* try { // try from 00ad7b08 to 00bd7b1b has its CatchHandler @ 00ad8900 */
  plVar16 = (long *)((long)&fde_table_entry_003380b8.initial_loc + param_1);
  cVar1 = *(char *)((long)&fde_table_entry_003380e8.initial_loc + param_1 + 1);
                    /* try { // try from 00ad7b1c to 00bd7b2f has its CatchHandler @ 00ad88fc */
  *(undefined1 *)((long)&fde_table_entry_003380e8.initial_loc + param_1) = 0;
  if (cVar1 != '\0') {
    iVar3 = *(int *)((long)&fde_table_entry_00333970.data_loc + param_1);
    puVar11 = (undefined8 *)((long)&fde_table_entry_003380c0.initial_loc + param_1);
    puVar13 = (undefined8 *)*puVar11;
    while (puVar20 = puVar11, puVar13 != (undefined8 *)0x0) {
      while (puVar7 = puVar13, puVar11 = puVar7, *(int *)(puVar7 + 4) <= iVar3) {
                    /* try { // try from 00ad7b5c to 00bd7b6f has its CatchHandler @ 00ad88b8 */
        if (iVar3 <= *(int *)(puVar7 + 4)) goto LAB_00ad7bc8;
        puVar13 = (undefined8 *)puVar7[1];
        if ((undefined8 *)puVar7[1] == (undefined8 *)0x0) {
          puVar20 = puVar7 + 1;
          goto LAB_00ad7b6c;
        }
      }
      puVar13 = (undefined8 *)*puVar7;
                    /* try { // try from 00ad7b44 to 00bd7b53 has its CatchHandler @ 00ad88bc */
    }
LAB_00ad7b6c:
                    /* try { // try from 00ad7b70 to 00bd7b83 has its CatchHandler @ 00ad88b4 */
    puVar7 = (undefined8 *)_Znwm(0x40);
    puVar7[7] = 0;
    puVar7[6] = 0;
                    /* try { // try from 00ad7b8c to 00bd7b93 has its CatchHandler @ 00ad89f0 */
    puVar7[5] = puVar7 + 6;
    *puVar7 = 0;
    puVar7[1] = 0;
    puVar7[2] = puVar11;
    *puVar20 = puVar7;
                    /* try { // try from 00ad7b9c to 00bd7bab has its CatchHandler @ 00ad88b0 */
    plVar14 = (long *)*plVar16;
    *(int *)(puVar7 + 4) = iVar3;
    lVar15 = *plVar14;
    puVar11 = puVar7;
    if (lVar15 != 0) {
      *plVar16 = lVar15;
                    /* try { // try from 00ad7bb0 to 00bd7bc3 has its CatchHandler @ 00ad88ac */
      puVar11 = (undefined8 *)*puVar20;
    }
    FUN_0043bf04(*(undefined8 *)((long)&fde_table_entry_003380c0.initial_loc + param_1),puVar11);
                    /* try { // try from 00ad7bc4 to 00bd7bd7 has its CatchHandler @ 00ad88a8 */
    *(long *)((long)&fde_table_entry_003380c8.initial_loc + param_1) =
         *(long *)((long)&fde_table_entry_003380c8.initial_loc + param_1) + 1;
LAB_00ad7bc8:
    iVar3 = FUN_00803c64();
    puVar13 = (undefined8 *)puVar7[6];
    puVar11 = puVar7 + 6;
    while (puVar20 = puVar11, puVar13 != (undefined8 *)0x0) {
                    /* try { // try from 00ad7bf4 to 00bd7c07 has its CatchHandler @ 00ad88dc */
      while (puVar8 = puVar13, puVar11 = puVar8, *(int *)((long)puVar8 + 0x1c) <= iVar3) {
        if (iVar3 <= *(int *)((long)puVar8 + 0x1c)) goto LAB_00ad7c64;
                    /* try { // try from 00ad7c08 to 00bd7c1b has its CatchHandler @ 00ad88c8 */
        puVar13 = (undefined8 *)puVar8[1];
        if ((undefined8 *)puVar8[1] == (undefined8 *)0x0) {
          puVar20 = puVar8 + 1;
          goto LAB_00ad7c14;
        }
      }
      puVar13 = (undefined8 *)*puVar8;
    }
LAB_00ad7c14:
    puVar8 = (undefined8 *)_Znwm(0x28);
                    /* try { // try from 00ad7c20 to 00bd7c2f has its CatchHandler @ 00ad88ec */
    *puVar8 = 0;
    puVar8[1] = 0;
    puVar8[2] = puVar11;
    *puVar20 = puVar8;
    plVar16 = (long *)puVar7[5];
                    /* try { // try from 00ad7c38 to 00bd7c4b has its CatchHandler @ 00ad88d8 */
    *(int *)((long)puVar8 + 0x1c) = iVar3;
    *(undefined1 *)(puVar8 + 4) = 0;
    puVar11 = puVar8;
    if (*plVar16 != 0) {
      puVar7[5] = *plVar16;
                    /* try { // try from 00ad7c4c to 00bd7c5f has its CatchHandler @ 00ad88c4 */
      puVar11 = (undefined8 *)*puVar20;
    }
    FUN_0043bf04(puVar7[6],puVar11);
    puVar7[7] = puVar7[7] + 1;
LAB_00ad7c64:
                    /* try { // try from 00ad7c64 to 00bd7c73 has its CatchHandler @ 00ad88e8 */
    if (*(char *)(puVar8 + 4) != '\0') {
      *(undefined1 *)((long)&fde_table_entry_003380e8.initial_loc + param_1) = 1;
    }
  }
  uVar5 = *(undefined4 *)((long)&fde_table_entry_00333970.data_loc + param_1);
                    /* try { // try from 00ad7c7c to 00bd7c8f has its CatchHandler @ 00ad88d4 */
  *(undefined1 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 2) = 0;
  uVar9 = FUN_007df5b8(param_1,uVar5);
                    /* try { // try from 00ad7c90 to 00bd7ca3 has its CatchHandler @ 00ad88c0 */
  if (((uVar9 & 1) != 0) &&
     (cVar1 = *(char *)((long)&fde_table_entry_003380f8.initial_loc + param_1),
     iVar3 = FUN_00803c64(), iVar3 == cVar1)) {
    *(undefined1 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 2) = 1;
  }
  uVar5 = *(undefined4 *)((long)&fde_table_entry_00333970.data_loc + param_1);
                    /* try { // try from 00ad7ca8 to 00bd7caf has its CatchHandler @ 00ad89f0 */
  *(undefined1 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 3) = 0;
  uVar9 = FUN_007df630(param_1,uVar5);
                    /* try { // try from 00ad7cb8 to 00bd7cc7 has its CatchHandler @ 00ad88a4 */
  if (((uVar9 & 1) != 0) &&
     (cVar1 = *(char *)((long)&fde_table_entry_003380f8.initial_loc + param_1),
     iVar3 = FUN_00803c64(), iVar3 == cVar1)) {
    *(undefined1 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 3) = 1;
  }
                    /* try { // try from 00ad7cd0 to 00bd7ce3 has its CatchHandler @ 00ad88a0 */
  uVar4 = FUN_00803b14(0);
  uVar5 = FUN_00803c64();
                    /* try { // try from 00ad7ce4 to 00bd7cf7 has its CatchHandler @ 00ad889c */
  uVar9 = FUN_00676b3c(param_1 + 0x13d8,1);
  if ((uVar9 & 1) == 0) {
    uVar9 = FUN_007bcd04(param_1,1);
                    /* try { // try from 00ad7d0c to 00bd7d1b has its CatchHandler @ 00ad8898 */
    if ((uVar9 & 1) == 0) {
                    /* try { // try from 00ad7f6c to 00bd7f7b has its CatchHandler @ 00ad8868 */
      uVar9 = FUN_00a33a4c(param_1 + 0x530,0xffffffff,0xffffffff);
      if ((uVar9 & 1) != 0) {
        uVar4 = FUN_00a33ee0(param_1 + 0x530,uVar4);
                    /* try { // try from 00ad7f84 to 00bd7f97 has its CatchHandler @ 00ad8864 */
      }
      goto LAB_00ad7d24;
    }
    uVar12 = 0x44;
  }
  else {
    uVar12 = 0x2a;
                    /* try { // try from 00ad7cfc to 00bd7d03 has its CatchHandler @ 00ad89f0 */
  }
  uVar4 = FUN_008011a8(0xfffffff8,uVar12);
  uVar5 = 0;
LAB_00ad7d24:
                    /* try { // try from 00ad7d24 to 00bd7d37 has its CatchHandler @ 00ad8894 */
  uVar6 = FUN_008621ec(param_1);
                    /* try { // try from 00ad7d38 to 00bd7d4b has its CatchHandler @ 00ad8890 */
  uVar9 = FUN_00615d00(param_1,uVar4,uVar5,uVar6);
  if ((((uVar9 & 1) == 0) && (uVar9 = FUN_00744610(param_1 + 0xbe0), (uVar9 & 1) == 0)) &&
     (iVar3 = FUN_00803674(0), iVar3 != -0x18)) {
    uVar12 = 0;
    *(undefined2 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 2) = 0;
    *(undefined1 *)((long)&fde_table_entry_003380e8.initial_loc + param_1) = 0;
  }
  else {
    *(undefined2 *)((long)&fde_table_entry_003380f0.data_loc + param_1 + 2) = 0;
                    /* try { // try from 00ad7d6c to 00bd7d73 has its CatchHandler @ 00ad89f0 */
    *(undefined1 *)((long)&fde_table_entry_003380e8.initial_loc + param_1) = 0;
                    /* try { // try from 00ad7d74 to 00bd7dff has its CatchHandler @ 00ad8970 */
    pcVar22 = (char *)(param_1 + 0x46f91);
    lVar15 = param_1 + 0xc5bb;
    lVar21 = 10;
    do {
      iVar3 = *(int *)((long)&QWORD_0039b978 + param_1 + 4);
      lVar18 = param_1 + 0xc5b8 + (long)iVar3 * 0x2c;
      pbVar17 = (byte *)(lVar15 + (long)iVar3 * 0x2c);
      uVar2 = (uint)(*(byte *)(lVar18 + 0x2a) ^ pbVar17[-1]) << 0x10 |
              (uint)(*(byte *)(lVar18 + 0x2b) ^ *pbVar17) << 0x18 |
              (uint)(*(byte *)(lVar18 + 0x29) ^ pbVar17[-2]) << 8 |
              (uint)(*(byte *)(lVar18 + 0x28) ^ pbVar17[-3]);
      iVar3 = uVar2 - 2;
                    /* try { // try from 00ad7e10 to 00bd7e17 has its CatchHandler @ 00ad8974 */
                    /* try { // try from 00ad7e1c to 00bd7e3f has its CatchHandler @ 00ad89b0 */
      if (((int)uVar2 < 2) ||
         (((uVar9 = FUN_00744610(param_1 + 0xbe0), (uVar9 & 1) == 0 ||
           ((uVar9 = FUN_00744198(param_1 + 0xbe0,iVar3), (uVar9 & 1) != 0 &&
            (uVar9 = FUN_00744334(param_1 + 0xbe0,iVar3), (uVar9 & 1) == 0)))) &&
          (uVar9 = FUN_005c08e0(param_1 + 0x4a0,*(undefined4 *)((long)&QWORD_0039b978 + param_1 + 4)
                                ,iVar3), (uVar9 & 1) == 0)))) {
                    /* try { // try from 00ad7e44 to 00bd7e5b has its CatchHandler @ 00ad89f0 */
        if ((*(uint *)(param_1 + 0x3398) & 0xfffffffe) == 2) {
          uVar5 = FUN_00a43078(param_1 + 0x347348);
                    /* try { // try from 00ad7e64 to 00bd7e73 has its CatchHandler @ 00ad888c */
          uVar9 = FUN_00a43104(param_1 + 0x347348,uVar5);
          uVar9 = uVar9 & 0xffffffff;
        }
        else {
                    /* try { // try from 00ad7e78 to 00bd7e8b has its CatchHandler @ 00ad8888 */
          uVar9 = 0;
        }
        uVar19 = 0;
                    /* try { // try from 00ad7e8c to 00bd7e9f has its CatchHandler @ 00ad8884 */
                    /* try { // try from 00ad7eac to 00bd7eb3 has its CatchHandler @ 00ad89f0 */
                    /* try { // try from 00ad7ebc to 00bd7ecb has its CatchHandler @ 00ad8880 */
                    /* try { // try from 00ad7ed4 to 00bd7ee7 has its CatchHandler @ 00ad887c */
                    /* try { // try from 00ad7ee8 to 00bd7efb has its CatchHandler @ 00ad8878 */
                    /* try { // try from 00ad7f04 to 00bd7f0b has its CatchHandler @ 00ad89f0 */
                    /* try { // try from 00ad7f14 to 00bd7f23 has its CatchHandler @ 00ad8874 */
                    /* try { // try from 00ad7f28 to 00bd7f3b has its CatchHandler @ 00ad8870 */
                    /* try { // try from 00ad7f3c to 00bd7f4f has its CatchHandler @ 00ad886c */
        while ((((((*(char *)(param_1 + 0x47d72) == pcVar22[1] &&
                   *(char *)(param_1 + 0x47d73) == pcVar22[2]) &&
                  *(char *)(param_1 + 0x47d71) == *pcVar22) &&
                  *(char *)(param_1 + 0x47d70) == pcVar22[-1] ||
                 ((uVar10 = FUN_00744610(param_1 + 0xbe0), (uVar10 & 1) != 0 &&
                  ((uVar10 = FUN_00744198(param_1 + 0xbe0,uVar19 & 0xffffffff), (uVar10 & 1) == 0 ||
                   (uVar10 = FUN_00744334(param_1 + 0xbe0,uVar19 & 0xffffffff), (uVar10 & 1) != 0)))
                  ))) || ((uVar10 = FUN_00b0a6ec(param_1 + 0x3d8), (uVar10 & 1) != 0 &&
                          (uVar10 = FUN_00b0bda4(param_1 + 0x3d8,uVar19 & 0xffffffff),
                          (uVar10 & 1) == 0)))) ||
               ((uVar10 = FUN_005c08e0(param_1 + 0x4a0,
                                       *(undefined4 *)((long)&QWORD_0039b978 + param_1 + 4),
                                       uVar19 & 0xffffffff), (uVar10 & 1) != 0 ||
                (((uVar9 & 1) != 0 &&
                 (uVar10 = FUN_00a43aec(param_1 + 0x347348,uVar19 & 0xffffffff), (uVar10 & 1) == 0))
                ))))) {
          uVar19 = uVar19 + 1;
          pcVar22 = pcVar22 + 4;
          if (uVar19 == 0x378) {
            return 2;
          }
        }
        return 3;
      }
      lVar21 = lVar21 + -1;
      lVar15 = lVar15 + 4;
    } while (lVar21 != 0);
    uVar12 = 1;
  }
                    /* try { // try from 00ad7f98 to 00bd7fab has its CatchHandler @ 00ad8860 */
  return uVar12;
}

~~~
