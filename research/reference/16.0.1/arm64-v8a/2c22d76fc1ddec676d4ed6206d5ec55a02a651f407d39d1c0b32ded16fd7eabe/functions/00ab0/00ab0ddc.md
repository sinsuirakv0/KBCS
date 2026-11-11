# 00ab0ddc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00ab0ddc",
  "name": "FUN_00ab0ddc",
  "size": 2396,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c027dfca3c5f61c66e71f58b8a528a262fee9c618ffc6189b8a36de4abe23411",
  "source_text_sha256": "c027dfca3c5f61c66e71f58b8a528a262fee9c618ffc6189b8a36de4abe23411"
}
~~~

## 呼び出し元

- [006af588](../006af/006af588.md)
- [00830b30](../00830/00830b30.md)

## 呼び出し先

- [0046ca84](../0046c/0046ca84.md)
- [0047acf4](../0047a/0047acf4.md)
- [0047ca8c](../0047c/0047ca8c.md)
- [00728d08](../00728/00728d08.md)
- [00728e48](../00728/00728e48.md)
- [0072bf4c](../0072b/0072bf4c.md)
- [00744208](../00744/00744208.md)
- [0074423c](../00744/0074423c.md)
- [008001cc](../00800/008001cc.md)
- [008001dc](../00800/008001dc.md)
- [008001ec](../00800/008001ec.md)
- [00806af4](../00806/00806af4.md)
- [008514f8](../00851/008514f8.md)
- [0085bb70](../0085b/0085bb70.md)
- [0085ccf0](../0085c/0085ccf0.md)
- [0085cefc](../0085c/0085cefc.md)
- [0085d4f4](../0085d/0085d4f4.md)
- [009d8834](../009d8/009d8834.md)

## 疑似コード / UTF-8 12749 bytes

~~~c

void FUN_00ab0ddc(undefined8 param_1,int param_2,int param_3,undefined4 param_4,undefined4 param_5,
                 byte param_6)

{
  byte *pbVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  int iVar4;
  int iVar5;
  int iVar6;
  int iVar7;
  long lVar8;
  undefined8 uVar9;
  long lVar10;
  ulong uVar11;
  undefined8 uVar12;
  long lVar13;
  int iVar14;
  
  lVar8 = FUN_008514f8();
  *(undefined1 *)(lVar8 + 0x339c) = 1;
  uVar9 = FUN_008514f8();
  FUN_0085bb70(uVar9,9);
  lVar8 = FUN_008514f8();
  *(undefined4 *)((long)&fde_table_entry_00333f50.data_loc + lVar8) = 0xffffffff;
  lVar8 = FUN_008514f8();
  *(undefined1 *)((long)&fde_table_entry_00332a20.data_loc + lVar8 + 1) = 0;
  lVar8 = FUN_008514f8();
  BYTE_ARRAY_0039badd[lVar8 + 3] = param_6;
  uVar2 = FUN_008001dc(param_2);
  lVar8 = FUN_008514f8();
  *(undefined4 *)((long)&fde_0038f284 + lVar8) = uVar2;
  if (param_2 < -3) {
    if (param_2 == -0x13) {
      lVar8 = FUN_008514f8();
      *(undefined4 *)((long)&fde_table_entry_00333970.data_loc + lVar8) = 3;
      lVar8 = FUN_008514f8();
      FUN_0074423c(lVar8 + 0xbe0,0);
      lVar8 = FUN_008514f8();
      *(undefined4 *)(lVar8 + 0xc5a8) = 0;
      lVar8 = FUN_008514f8();
      *(undefined4 *)((long)&DWORD_00344440 + lVar8) = 0;
      lVar8 = FUN_008514f8();
      *(undefined4 *)(&uleb128_0039badc + lVar8) = 0;
      lVar8 = FUN_008514f8();
      uVar3 = FUN_008001cc(*(undefined4 *)((long)&fde_0038f284 + lVar8));
      lVar8 = FUN_008514f8();
      uVar2 = *(undefined4 *)((long)&DWORD_00344440 + lVar8);
      lVar8 = FUN_008514f8();
      uVar2 = FUN_00806af4(uVar3,uVar2,*(undefined4 *)(&uleb128_0039badc + lVar8),0);
      lVar8 = FUN_008514f8();
      *(undefined4 *)((long)&fde_table_entry_00331680.initial_loc + lVar8) = uVar2;
      lVar8 = FUN_008514f8();
      *(undefined4 *)(lVar8 + 0x13d0) = 0xffffffff;
      uVar9 = FUN_008514f8();
      FUN_009d8834(uVar9,param_3,0,0,0);
      lVar8 = FUN_008514f8();
      *(undefined4 *)((long)&fde_table_entry_00333f60.data_loc + lVar8) = 0;
      goto LAB_00ab1078;
    }
    if (param_2 == -7) {
      lVar8 = FUN_008514f8();
      *(int *)(lVar8 + 0xc5a8) = param_3 + 7;
      lVar8 = FUN_008514f8();
      *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8) = param_3 + 7;
      uVar9 = FUN_008514f8();
      uVar12 = 2;
      goto LAB_00ab1068;
    }
LAB_00ab0ef4:
    lVar8 = FUN_008514f8();
    *(undefined4 *)(lVar8 + 0xc5a8) = 3;
    lVar8 = FUN_008514f8();
    *(undefined4 *)((long)&fde_table_entry_00333970.data_loc + lVar8) = 3;
    lVar8 = FUN_008514f8();
    *(int *)((long)&DWORD_00344440 + lVar8) = param_3;
    lVar8 = FUN_008514f8();
    *(undefined4 *)(&uleb128_0039badc + lVar8) = param_5;
    uVar9 = FUN_008514f8();
    FUN_009d8834(uVar9,param_3,0,1,0);
    if (param_2 != -0x15) goto LAB_00ab1078;
    lVar8 = FUN_008514f8();
    FUN_0074423c(lVar8 + 0xbe0,1);
    uVar2 = 0x61;
LAB_00ab10b4:
    lVar8 = FUN_008514f8();
    *(undefined4 *)(lVar8 + 0xc5a8) = uVar2;
  }
  else {
    if (param_2 == -3) {
      lVar8 = FUN_008514f8();
      *(int *)(lVar8 + 0xc5a8) = param_3 + 4;
      lVar8 = FUN_008514f8();
      *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8) = param_3 + 4;
      uVar9 = FUN_008514f8();
      uVar12 = 1;
    }
    else {
      if (param_2 != -2) goto LAB_00ab0ef4;
      lVar8 = FUN_008514f8();
      *(int *)(lVar8 + 0xc5a8) = param_3;
      lVar8 = FUN_008514f8();
      *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8) = param_3;
      uVar9 = FUN_008514f8();
      uVar12 = 0;
    }
LAB_00ab1068:
    FUN_009d8834(uVar9,uVar12,param_3,1,1);
LAB_00ab1078:
    lVar8 = FUN_008514f8();
    FUN_0074423c(lVar8 + 0xbe0,0);
    lVar8 = FUN_008514f8();
    *(bool *)(lVar8 + 0x33d9) = param_2 == -0x18 || param_2 - 3U < 2;
    lVar8 = FUN_008514f8();
    if (*(char *)(lVar8 + 0x33d9) != '\0') {
      uVar2 = 0x62;
      goto LAB_00ab10b4;
    }
  }
  lVar8 = FUN_008514f8();
  if ((*(int *)(lVar8 + 0xc5a8) == 3) || (lVar8 = FUN_008514f8(), *(int *)(lVar8 + 0xc5a8) == 0x62))
  {
    lVar8 = FUN_008514f8();
    *(undefined4 *)(&uleb128_00344448 + lVar8) = 1;
  }
  lVar8 = FUN_008514f8();
  *(undefined4 *)((long)&fde_table_entry_00331690.initial_loc + lVar8) = param_4;
  lVar8 = FUN_008514f8();
  *(undefined4 *)((long)&fde_table_entry_00331680.initial_loc + lVar8) = param_4;
  lVar8 = FUN_008514f8();
  *(undefined4 *)(&uleb128_00393ca8 + lVar8) = 0;
  lVar8 = FUN_008514f8();
  uVar2 = 0;
  iVar7 = *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8);
  lVar8 = FUN_008514f8();
  if (iVar7 == 3) {
LAB_00ab11a8:
    *(undefined4 *)((long)&QWORD_003c7c70 + lVar8) = uVar2;
  }
  else {
    iVar7 = *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8);
    lVar8 = FUN_008514f8();
    if (iVar7 < 3) {
      uVar2 = 1;
      goto LAB_00ab11a8;
    }
    iVar7 = *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8);
    lVar8 = FUN_008514f8();
    if (iVar7 < 7) {
      uVar2 = 2;
      goto LAB_00ab11a8;
    }
    if (*(int *)((long)&fde_table_entry_00333970.data_loc + lVar8) < 10) {
      uVar2 = 3;
      lVar8 = FUN_008514f8();
      goto LAB_00ab11a8;
    }
  }
  lVar8 = FUN_008514f8();
  if ((*(int *)((long)&QWORD_003c7c70 + lVar8) == 0) ||
     (lVar8 = FUN_008514f8(), *(int *)((long)&QWORD_003c7c70 + lVar8) == 1)) {
    uVar2 = 0;
LAB_00ab11e4:
    lVar8 = FUN_008514f8();
LAB_00ab11e8:
    *(undefined4 *)((long)&DWORD_003c7c6c + lVar8) = uVar2;
  }
  else {
    lVar8 = FUN_008514f8();
    iVar7 = *(int *)((long)&QWORD_003c7c70 + lVar8);
    lVar8 = FUN_008514f8();
    if (iVar7 == 2) {
      uVar2 = 1;
      goto LAB_00ab11e8;
    }
    if (*(int *)((long)&QWORD_003c7c70 + lVar8) == 3) {
      uVar2 = 2;
      goto LAB_00ab11e4;
    }
  }
  lVar8 = FUN_008514f8();
  *(undefined4 *)(lVar8 + 0x4796bc) = 0xffffffff;
  lVar8 = FUN_008514f8();
  *(undefined4 *)(&uleb128_00344448 + lVar8) = 0;
  FUN_008514f8();
  FUN_0085cefc();
  lVar8 = FUN_008514f8();
  if ((param_2 != -0x13) && (*(int *)((long)&fde_table_entry_00333970.data_loc + lVar8) == 3)) {
    if (param_2 == -10) {
      lVar8 = FUN_008514f8();
      *(undefined1 *)(lVar8 + 0x21e4) = 1;
    }
    FUN_008514f8();
    uVar2 = FUN_0085d4f4();
    lVar8 = FUN_008514f8();
    lVar13 = 500;
    *(undefined4 *)(BYTE_ARRAY_00347329 + lVar8 + 0x13) = uVar2;
    lVar8 = 0x38e8c0;
    do {
      lVar10 = FUN_008514f8();
      iVar7 = *(int *)(lVar10 + lVar8);
      lVar10 = FUN_008514f8();
      if (iVar7 != *(int *)(lVar10 + lVar8 + -2000)) {
        lVar10 = FUN_008514f8();
        uVar2 = *(undefined4 *)(lVar10 + lVar8 + -2000);
        lVar10 = FUN_008514f8();
        *(undefined4 *)(lVar10 + lVar8) = uVar2;
      }
      lVar13 = lVar13 + -1;
      lVar8 = lVar8 + 4;
    } while (lVar13 != 0);
    lVar8 = FUN_008514f8();
    *(undefined4 *)(lVar8 + 0x1610) = 0xffffffff;
    lVar8 = FUN_008514f8();
    *(undefined4 *)(&uleb128_00344448 + lVar8) = 1;
    lVar8 = FUN_008514f8();
    if (0 < *(int *)(BYTE_ARRAY_00347329 + lVar8 + 0x13)) {
      iVar7 = 0;
      iVar6 = -1;
      iVar14 = -0x75;
      do {
        lVar8 = FUN_008514f8();
        lVar13 = FUN_008514f8();
        iVar5 = *(int *)(BYTE_ARRAY_0038e0ed +
                        lVar8 + (long)(iVar6 + *(int *)(BYTE_ARRAY_00347329 + lVar13 + 0x13)) * 4 +
                        3);
        iVar4 = FUN_008001ec(param_2,param_3);
        if (iVar4 == iVar5) {
          iVar4 = FUN_00728e48(iVar7);
          FUN_008514f8();
          iVar5 = FUN_0046ca84();
          if (iVar5 < 0) {
            iVar5 = iVar5 + 1;
          }
          lVar8 = FUN_008514f8();
          *(int *)(BYTE_ARRAY_00344449 + lVar8 + 3) = (iVar14 - iVar4) + (iVar5 >> 1);
        }
        iVar7 = iVar7 + 1;
        lVar8 = FUN_008514f8();
        iVar6 = iVar6 + -1;
        iVar14 = iVar14 + -0x5c;
      } while (iVar7 < *(int *)(BYTE_ARRAY_00347329 + lVar8 + 0x13));
    }
    lVar8 = FUN_008514f8();
    iVar7 = *(int *)(BYTE_ARRAY_00344449 + lVar8 + 3);
    iVar6 = FUN_00728d08();
    if (iVar7 <= iVar6 * -0x5c + 0x228) {
      iVar7 = FUN_00728d08();
      lVar8 = FUN_008514f8();
      *(int *)(BYTE_ARRAY_00344449 + lVar8 + 3) = iVar7 * -0x5c + 0x228;
    }
    lVar8 = FUN_008514f8();
    if (0x5b < *(int *)(BYTE_ARRAY_00344449 + lVar8 + 3)) {
      lVar8 = FUN_008514f8();
      pbVar1 = BYTE_ARRAY_00344449 + lVar8 + 3;
      pbVar1[0] = 0x5c;
      pbVar1[1] = 0;
      pbVar1[2] = 0;
      pbVar1[3] = 0;
    }
  }
  if (param_2 == -0x13) goto LAB_00ab16fc;
  FUN_008514f8();
  lVar8 = FUN_008514f8();
  iVar7 = *(int *)((long)&fde_table_entry_0033f8e0.initial_loc + lVar8);
  lVar8 = FUN_008514f8();
  if (*(int *)(lVar8 + 0xc5a8) == 0x62) {
    if (iVar7 != -1) goto LAB_00ab14d0;
LAB_00ab1450:
    uVar2 = 0;
  }
  else {
    lVar8 = FUN_008514f8();
    uVar11 = FUN_00744208(lVar8 + 0xbe0);
    if ((uVar11 & 1) == 0) {
      lVar8 = FUN_008514f8();
      if (iVar7 != *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8)) goto LAB_00ab14d0;
      goto LAB_00ab1450;
    }
    if (iVar7 == 0x3e6) goto LAB_00ab1450;
LAB_00ab14d0:
    FUN_008514f8();
    lVar8 = FUN_008514f8();
    iVar7 = *(int *)((long)&fde_table_entry_0033f8e0.data_loc + lVar8);
    lVar8 = FUN_008514f8();
    if (*(int *)(lVar8 + 0xc5a8) == 0x62) {
      if (iVar7 != -1) goto LAB_00ab1544;
LAB_00ab1504:
      uVar2 = 1;
    }
    else {
      lVar8 = FUN_008514f8();
      uVar11 = FUN_00744208(lVar8 + 0xbe0);
      if ((uVar11 & 1) == 0) {
        lVar8 = FUN_008514f8();
        if (iVar7 != *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8)) goto LAB_00ab1544;
        goto LAB_00ab1504;
      }
      if (iVar7 == 0x3e6) goto LAB_00ab1504;
LAB_00ab1544:
      FUN_008514f8();
      lVar8 = FUN_008514f8();
      iVar7 = *(int *)((long)&fde_table_entry_0033f8e8.initial_loc + lVar8);
      lVar8 = FUN_008514f8();
      if (*(int *)(lVar8 + 0xc5a8) == 0x62) {
        if (iVar7 != -1) goto LAB_00ab15b8;
LAB_00ab1578:
        uVar2 = 2;
      }
      else {
        lVar8 = FUN_008514f8();
        uVar11 = FUN_00744208(lVar8 + 0xbe0);
        if ((uVar11 & 1) == 0) {
          lVar8 = FUN_008514f8();
          if (iVar7 != *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8))
          goto LAB_00ab15b8;
          goto LAB_00ab1578;
        }
        if (iVar7 == 0x3e6) goto LAB_00ab1578;
LAB_00ab15b8:
        FUN_008514f8();
        lVar8 = FUN_008514f8();
        iVar7 = *(int *)((long)&fde_table_entry_0033f8e8.data_loc + lVar8);
        lVar8 = FUN_008514f8();
        if (*(int *)(lVar8 + 0xc5a8) == 0x62) {
          iVar6 = -1;
        }
        else {
          lVar8 = FUN_008514f8();
          uVar11 = FUN_00744208(lVar8 + 0xbe0);
          if ((uVar11 & 1) == 0) {
            lVar8 = FUN_008514f8();
            iVar6 = *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8);
          }
          else {
            iVar6 = 0x3e6;
          }
        }
        if (iVar7 == iVar6) {
          uVar2 = 3;
        }
        else {
          FUN_008514f8();
          lVar8 = FUN_008514f8();
          iVar7 = *(int *)((long)&fde_table_entry_0033f8f0.initial_loc + lVar8);
          lVar8 = FUN_008514f8();
          if (*(int *)(lVar8 + 0xc5a8) == 0x62) {
            iVar6 = -1;
          }
          else {
            lVar8 = FUN_008514f8();
            uVar11 = FUN_00744208(lVar8 + 0xbe0);
            if ((uVar11 & 1) == 0) {
              lVar8 = FUN_008514f8();
              iVar6 = *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8);
            }
            else {
              iVar6 = 0x3e6;
            }
          }
          if (iVar7 == iVar6) {
            uVar2 = 4;
          }
          else {
            FUN_008514f8();
            lVar8 = FUN_008514f8();
            iVar7 = *(int *)((long)&fde_table_entry_0033f8f0.data_loc + lVar8);
            lVar8 = FUN_008514f8();
            if (*(int *)(lVar8 + 0xc5a8) == 0x62) {
              iVar6 = -1;
            }
            else {
              lVar8 = FUN_008514f8();
              uVar11 = FUN_00744208(lVar8 + 0xbe0);
              if ((uVar11 & 1) == 0) {
                lVar8 = FUN_008514f8();
                iVar6 = *(int *)((long)&fde_table_entry_00333970.data_loc + lVar8);
              }
              else {
                iVar6 = 0x3e6;
              }
            }
            if (iVar7 != iVar6) {
              FUN_008514f8();
              goto LAB_00ab16fc;
            }
            uVar2 = 5;
          }
        }
      }
    }
  }
  lVar8 = FUN_008514f8();
  *(undefined4 *)((long)&fde_table_entry_00333f60.data_loc + lVar8) = uVar2;
LAB_00ab16fc:
  FUN_008514f8();
  FUN_0085ccf0();
  uVar9 = FUN_0047acf4();
  FUN_0047ca8c(uVar9,0xffffffff);
  FUN_0072bf4c(0);
  return;
}

~~~
