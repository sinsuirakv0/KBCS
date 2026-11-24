# 00ab0ddc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0082.md#review-317740b94b8bf21025d94018a278c82a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0041.md#review-317740b94b8bf21025d94018a278c82a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_text_sha256": "c027dfca3c5f61c66e71f58b8a528a262fee9c618ffc6189b8a36de4abe23411",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ab0ddc",
        "00ab1737"
      ]
    ],
    "bytes_sha256": "f8d07583ffbe7eeb136dfda639f63acbd18154acb7e4cb3687592a15e8ca2453",
    "instruction_count": 599,
    "instruction_bytes": 2396,
    "body_bytes": 2396,
    "indirect": 0,
    "unresolved": 0
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ab0ddc"></a> `00ab0ddc` | `fd 7b ba a9` | stp x29,x30,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00ab0de0"></a> `00ab0de0` | `fb 0b 00 f9` | str x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab0de4"></a> `00ab0de4` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ab0de8"></a> `00ab0de8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ab0dec"></a> `00ab0dec` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ab0df0"></a> `00ab0df0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ab0df4"></a> `00ab0df4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ab0df8"></a> `00ab0df8` | `f7 03 05 2a` | mov w23,w5 | `FALL_THROUGH`
<a id="insn-00ab0dfc"></a> `00ab0dfc` | `f6 03 04 2a` | mov w22,w4 | `FALL_THROUGH`
<a id="insn-00ab0e00"></a> `00ab0e00` | `f5 03 03 2a` | mov w21,w3 | `FALL_THROUGH`
<a id="insn-00ab0e04"></a> `00ab0e04` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00ab0e08"></a> `00ab0e08` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00ab0e0c"></a> `00ab0e0c` | `bb 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0e10"></a> `00ab0e10` | `88 73 86 52` | mov w8,#0x339c | `FALL_THROUGH`
<a id="insn-00ab0e14"></a> `00ab0e14` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0e18"></a> `00ab0e18` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ab0e1c"></a> `00ab0e1c` | `b7 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0e20"></a> `00ab0e20` | `21 01 80 52` | mov w1,#0x9 | `FALL_THROUGH`
<a id="insn-00ab0e24"></a> `00ab0e24` | `53 ab f6 97` | bl 0x0085bb70 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0e28"></a> `00ab0e28` | `b4 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0e2c"></a> `00ab0e2c` | `88 ea 87 52` | mov w8,#0x3f54 | `FALL_THROUGH`
<a id="insn-00ab0e30"></a> `00ab0e30` | `09 00 80 12` | mov w9,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab0e34"></a> `00ab0e34` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0e38"></a> `00ab0e38` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0e3c"></a> `00ab0e3c` | `af 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0e40"></a> `00ab0e40` | `a8 44 85 52` | mov w8,#0x2a25 | `FALL_THROUGH`
<a id="insn-00ab0e44"></a> `00ab0e44` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0e48"></a> `00ab0e48` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ab0e4c"></a> `00ab0e4c` | `ab 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0e50"></a> `00ab0e50` | `08 5c 97 52` | mov w8,#0xbae0 | `FALL_THROUGH`
<a id="insn-00ab0e54"></a> `00ab0e54` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0e58"></a> `00ab0e58` | `17 68 28 38` | strb w23,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ab0e5c"></a> `00ab0e5c` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00ab0e60"></a> `00ab0e60` | `df 3c f5 97` | bl 0x008001dc | `UNCONDITIONAL_CALL`
<a id="insn-00ab0e64"></a> `00ab0e64` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00ab0e68"></a> `00ab0e68` | `a4 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0e6c"></a> `00ab0e6c` | `88 50 9e 52` | mov w8,#0xf284 | `FALL_THROUGH`
<a id="insn-00ab0e70"></a> `00ab0e70` | `7f 12 00 31` | cmn w19,#0x4 | `FALL_THROUGH`
<a id="insn-00ab0e74"></a> `00ab0e74` | `08 07 a0 72` | movk w8,#0x38, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0e78"></a> `00ab0e78` | `17 68 28 b8` | str w23,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0e7c"></a> `00ab0e7c` | `0c 02 00 54` | b.gt 0x00ab0ebc | `CONDITIONAL_JUMP`
<a id="insn-00ab0e80"></a> `00ab0e80` | `7f 4e 00 31` | cmn w19,#0x13 | `FALL_THROUGH`
<a id="insn-00ab0e84"></a> `00ab0e84` | `40 07 00 54` | b.eq 0x00ab0f6c | `CONDITIONAL_JUMP`
<a id="insn-00ab0e88"></a> `00ab0e88` | `7f 1e 00 31` | cmn w19,#0x7 | `FALL_THROUGH`
<a id="insn-00ab0e8c"></a> `00ab0e8c` | `41 03 00 54` | b.ne 0x00ab0ef4 | `CONDITIONAL_JUMP`
<a id="insn-00ab0e90"></a> `00ab0e90` | `96 1e 00 11` | add w22,w20,#0x7 | `FALL_THROUGH`
<a id="insn-00ab0e94"></a> `00ab0e94` | `99 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0e98"></a> `00ab0e98` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab0e9c"></a> `00ab0e9c` | `16 68 28 b8` | str w22,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0ea0"></a> `00ab0ea0` | `96 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0ea4"></a> `00ab0ea4` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab0ea8"></a> `00ab0ea8` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0eac"></a> `00ab0eac` | `16 68 28 b8` | str w22,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0eb0"></a> `00ab0eb0` | `92 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0eb4"></a> `00ab0eb4` | `41 00 80 52` | mov w1,#0x2 | `FALL_THROUGH`
<a id="insn-00ab0eb8"></a> `00ab0eb8` | `6c 00 00 14` | b 0x00ab1068 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0ebc"></a> `00ab0ebc` | `7f 0e 00 31` | cmn w19,#0x3 | `FALL_THROUGH`
<a id="insn-00ab0ec0"></a> `00ab0ec0` | `00 0c 00 54` | b.eq 0x00ab1040 | `CONDITIONAL_JUMP`
<a id="insn-00ab0ec4"></a> `00ab0ec4` | `7f 0a 00 31` | cmn w19,#0x2 | `FALL_THROUGH`
<a id="insn-00ab0ec8"></a> `00ab0ec8` | `61 01 00 54` | b.ne 0x00ab0ef4 | `CONDITIONAL_JUMP`
<a id="insn-00ab0ecc"></a> `00ab0ecc` | `8b 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0ed0"></a> `00ab0ed0` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab0ed4"></a> `00ab0ed4` | `14 68 28 b8` | str w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0ed8"></a> `00ab0ed8` | `88 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0edc"></a> `00ab0edc` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab0ee0"></a> `00ab0ee0` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0ee4"></a> `00ab0ee4` | `14 68 28 b8` | str w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0ee8"></a> `00ab0ee8` | `84 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0eec"></a> `00ab0eec` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ab0ef0"></a> `00ab0ef0` | `5e 00 00 14` | b 0x00ab1068 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0ef4"></a> `00ab0ef4` | `81 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0ef8"></a> `00ab0ef8` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab0efc"></a> `00ab0efc` | `77 00 80 52` | mov w23,#0x3 | `FALL_THROUGH`
<a id="insn-00ab0f00"></a> `00ab0f00` | `17 68 28 b8` | str w23,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0f04"></a> `00ab0f04` | `7d 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0f08"></a> `00ab0f08` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab0f0c"></a> `00ab0f0c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0f10"></a> `00ab0f10` | `17 68 28 b8` | str w23,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0f14"></a> `00ab0f14` | `79 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0f18"></a> `00ab0f18` | `08 88 88 52` | mov w8,#0x4440 | `FALL_THROUGH`
<a id="insn-00ab0f1c"></a> `00ab0f1c` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0f20"></a> `00ab0f20` | `14 68 28 b8` | str w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0f24"></a> `00ab0f24` | `75 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0f28"></a> `00ab0f28` | `88 5b 97 52` | mov w8,#0xbadc | `FALL_THROUGH`
<a id="insn-00ab0f2c"></a> `00ab0f2c` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0f30"></a> `00ab0f30` | `16 68 28 b8` | str w22,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0f34"></a> `00ab0f34` | `71 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0f38"></a> `00ab0f38` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00ab0f3c"></a> `00ab0f3c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00ab0f40"></a> `00ab0f40` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0f44"></a> `00ab0f44` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00ab0f48"></a> `00ab0f48` | `3b 9e fc 97` | bl 0x009d8834 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0f4c"></a> `00ab0f4c` | `7f 56 00 31` | cmn w19,#0x15 | `FALL_THROUGH`
<a id="insn-00ab0f50"></a> `00ab0f50` | `41 09 00 54` | b.ne 0x00ab1078 | `CONDITIONAL_JUMP`
<a id="insn-00ab0f54"></a> `00ab0f54` | `69 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0f58"></a> `00ab0f58` | `00 80 2f 91` | add x0,x0,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ab0f5c"></a> `00ab0f5c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00ab0f60"></a> `00ab0f60` | `b7 4c f2 97` | bl 0x0074423c | `UNCONDITIONAL_CALL`
<a id="insn-00ab0f64"></a> `00ab0f64` | `36 0c 80 52` | mov w22,#0x61 | `FALL_THROUGH`
<a id="insn-00ab0f68"></a> `00ab0f68` | `53 00 00 14` | b 0x00ab10b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab0f6c"></a> `00ab0f6c` | `63 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0f70"></a> `00ab0f70` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab0f74"></a> `00ab0f74` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00ab0f78"></a> `00ab0f78` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0f7c"></a> `00ab0f7c` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0f80"></a> `00ab0f80` | `5e 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0f84"></a> `00ab0f84` | `00 80 2f 91` | add x0,x0,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ab0f88"></a> `00ab0f88` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ab0f8c"></a> `00ab0f8c` | `ac 4c f2 97` | bl 0x0074423c | `UNCONDITIONAL_CALL`
<a id="insn-00ab0f90"></a> `00ab0f90` | `5a 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0f94"></a> `00ab0f94` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab0f98"></a> `00ab0f98` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0f9c"></a> `00ab0f9c` | `57 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0fa0"></a> `00ab0fa0` | `17 88 88 52` | mov w23,#0x4440 | `FALL_THROUGH`
<a id="insn-00ab0fa4"></a> `00ab0fa4` | `97 06 a0 72` | movk w23,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0fa8"></a> `00ab0fa8` | `1f 68 37 b8` | str wzr,[x0, x23, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0fac"></a> `00ab0fac` | `53 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0fb0"></a> `00ab0fb0` | `98 5b 97 52` | mov w24,#0xbadc | `FALL_THROUGH`
<a id="insn-00ab0fb4"></a> `00ab0fb4` | `38 07 a0 72` | movk w24,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0fb8"></a> `00ab0fb8` | `1f 68 38 b8` | str wzr,[x0, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0fbc"></a> `00ab0fbc` | `4f 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0fc0"></a> `00ab0fc0` | `88 50 9e 52` | mov w8,#0xf284 | `FALL_THROUGH`
<a id="insn-00ab0fc4"></a> `00ab0fc4` | `08 07 a0 72` | movk w8,#0x38, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab0fc8"></a> `00ab0fc8` | `00 68 68 b8` | ldr w0,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0fcc"></a> `00ab0fcc` | `80 3c f5 97` | bl 0x008001cc | `UNCONDITIONAL_CALL`
<a id="insn-00ab0fd0"></a> `00ab0fd0` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00ab0fd4"></a> `00ab0fd4` | `49 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0fd8"></a> `00ab0fd8` | `17 68 77 b8` | ldr w23,[x0, x23, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0fdc"></a> `00ab0fdc` | `47 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0fe0"></a> `00ab0fe0` | `02 68 78 b8` | ldr w2,[x0, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab0fe4"></a> `00ab0fe4` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00ab0fe8"></a> `00ab0fe8` | `e1 03 17 2a` | mov w1,w23 | `FALL_THROUGH`
<a id="insn-00ab0fec"></a> `00ab0fec` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00ab0ff0"></a> `00ab0ff0` | `c1 56 f5 97` | bl 0x00806af4 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0ff4"></a> `00ab0ff4` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00ab0ff8"></a> `00ab0ff8` | `40 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab0ffc"></a> `00ab0ffc` | `08 d0 82 52` | mov w8,#0x1680 | `FALL_THROUGH`
<a id="insn-00ab1000"></a> `00ab1000` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1004"></a> `00ab1004` | `16 68 28 b8` | str w22,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1008"></a> `00ab1008` | `3c 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab100c"></a> `00ab100c` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab1010"></a> `00ab1010` | `08 d0 13 b9` | str w8,[x0, #0x13d0] | `FALL_THROUGH`
<a id="insn-00ab1014"></a> `00ab1014` | `39 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1018"></a> `00ab1018` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00ab101c"></a> `00ab101c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00ab1020"></a> `00ab1020` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00ab1024"></a> `00ab1024` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00ab1028"></a> `00ab1028` | `03 9e fc 97` | bl 0x009d8834 | `UNCONDITIONAL_CALL`
<a id="insn-00ab102c"></a> `00ab102c` | `33 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1030"></a> `00ab1030` | `88 ec 87 52` | mov w8,#0x3f64 | `FALL_THROUGH`
<a id="insn-00ab1034"></a> `00ab1034` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1038"></a> `00ab1038` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab103c"></a> `00ab103c` | `0f 00 00 14` | b 0x00ab1078 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab1040"></a> `00ab1040` | `96 12 00 11` | add w22,w20,#0x4 | `FALL_THROUGH`
<a id="insn-00ab1044"></a> `00ab1044` | `2d 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1048"></a> `00ab1048` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab104c"></a> `00ab104c` | `16 68 28 b8` | str w22,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1050"></a> `00ab1050` | `2a 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1054"></a> `00ab1054` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab1058"></a> `00ab1058` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab105c"></a> `00ab105c` | `16 68 28 b8` | str w22,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1060"></a> `00ab1060` | `26 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1064"></a> `00ab1064` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1068"></a> `00ab1068` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00ab106c"></a> `00ab106c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1070"></a> `00ab1070` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1074"></a> `00ab1074` | `f0 9d fc 97` | bl 0x009d8834 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1078"></a> `00ab1078` | `20 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab107c"></a> `00ab107c` | `00 80 2f 91` | add x0,x0,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ab1080"></a> `00ab1080` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00ab1084"></a> `00ab1084` | `6e 4c f2 97` | bl 0x0074423c | `UNCONDITIONAL_CALL`
<a id="insn-00ab1088"></a> `00ab1088` | `68 0e 00 51` | sub w8,w19,#0x3 | `FALL_THROUGH`
<a id="insn-00ab108c"></a> `00ab108c` | `7f 62 00 31` | cmn w19,#0x18 | `FALL_THROUGH`
<a id="insn-00ab1090"></a> `00ab1090` | `00 19 42 7a` | ccmp w8,#0x2,#0x0,ne | `FALL_THROUGH`
<a id="insn-00ab1094"></a> `00ab1094` | `f6 27 9f 1a` | cset w22,cc | `FALL_THROUGH`
<a id="insn-00ab1098"></a> `00ab1098` | `18 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab109c"></a> `00ab109c` | `37 7b 86 52` | mov w23,#0x33d9 | `FALL_THROUGH`
<a id="insn-00ab10a0"></a> `00ab10a0` | `16 68 37 38` | strb w22,[x0, x23, LSL ] | `FALL_THROUGH`
<a id="insn-00ab10a4"></a> `00ab10a4` | `15 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab10a8"></a> `00ab10a8` | `08 68 77 38` | ldrb w8,[x0, x23, LSL ] | `FALL_THROUGH`
<a id="insn-00ab10ac"></a> `00ab10ac` | `a8 00 00 34` | cbz w8,0x00ab10c0 | `CONDITIONAL_JUMP`
<a id="insn-00ab10b0"></a> `00ab10b0` | `56 0c 80 52` | mov w22,#0x62 | `FALL_THROUGH`
<a id="insn-00ab10b4"></a> `00ab10b4` | `11 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab10b8"></a> `00ab10b8` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab10bc"></a> `00ab10bc` | `16 68 28 b8` | str w22,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab10c0"></a> `00ab10c0` | `0e 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab10c4"></a> `00ab10c4` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab10c8"></a> `00ab10c8` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab10cc"></a> `00ab10cc` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00ab10d0"></a> `00ab10d0` | `c0 00 00 54` | b.eq 0x00ab10e8 | `CONDITIONAL_JUMP`
<a id="insn-00ab10d4"></a> `00ab10d4` | `09 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab10d8"></a> `00ab10d8` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab10dc"></a> `00ab10dc` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab10e0"></a> `00ab10e0` | `1f 89 01 71` | cmp w8,#0x62 | `FALL_THROUGH`
<a id="insn-00ab10e4"></a> `00ab10e4` | `c1 00 00 54` | b.ne 0x00ab10fc | `CONDITIONAL_JUMP`
<a id="insn-00ab10e8"></a> `00ab10e8` | `04 81 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab10ec"></a> `00ab10ec` | `08 89 88 52` | mov w8,#0x4448 | `FALL_THROUGH`
<a id="insn-00ab10f0"></a> `00ab10f0` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00ab10f4"></a> `00ab10f4` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab10f8"></a> `00ab10f8` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab10fc"></a> `00ab10fc` | `ff 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1100"></a> `00ab1100` | `08 d2 82 52` | mov w8,#0x1690 | `FALL_THROUGH`
<a id="insn-00ab1104"></a> `00ab1104` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1108"></a> `00ab1108` | `15 68 28 b8` | str w21,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab110c"></a> `00ab110c` | `fb 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1110"></a> `00ab1110` | `08 d0 82 52` | mov w8,#0x1680 | `FALL_THROUGH`
<a id="insn-00ab1114"></a> `00ab1114` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1118"></a> `00ab1118` | `15 68 28 b8` | str w21,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab111c"></a> `00ab111c` | `f7 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1120"></a> `00ab1120` | `08 95 87 52` | mov w8,#0x3ca8 | `FALL_THROUGH`
<a id="insn-00ab1124"></a> `00ab1124` | `28 07 a0 72` | movk w8,#0x39, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1128"></a> `00ab1128` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab112c"></a> `00ab112c` | `f3 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1130"></a> `00ab1130` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab1134"></a> `00ab1134` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00ab1138"></a> `00ab1138` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab113c"></a> `00ab113c` | `16 68 68 b8` | ldr w22,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1140"></a> `00ab1140` | `ee 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1144"></a> `00ab1144` | `df 0e 00 71` | cmp w22,#0x3 | `FALL_THROUGH`
<a id="insn-00ab1148"></a> `00ab1148` | `00 03 00 54` | b.eq 0x00ab11a8 | `CONDITIONAL_JUMP`
<a id="insn-00ab114c"></a> `00ab114c` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab1150"></a> `00ab1150` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1154"></a> `00ab1154` | `15 68 68 b8` | ldr w21,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1158"></a> `00ab1158` | `e8 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab115c"></a> `00ab115c` | `bf 0e 00 71` | cmp w21,#0x3 | `FALL_THROUGH`
<a id="insn-00ab1160"></a> `00ab1160` | `6a 00 00 54` | b.ge 0x00ab116c | `CONDITIONAL_JUMP`
<a id="insn-00ab1164"></a> `00ab1164` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1168"></a> `00ab1168` | `10 00 00 14` | b 0x00ab11a8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab116c"></a> `00ab116c` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab1170"></a> `00ab1170` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1174"></a> `00ab1174` | `15 68 68 b8` | ldr w21,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1178"></a> `00ab1178` | `e0 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab117c"></a> `00ab117c` | `bf 1e 00 71` | cmp w21,#0x7 | `FALL_THROUGH`
<a id="insn-00ab1180"></a> `00ab1180` | `6a 00 00 54` | b.ge 0x00ab118c | `CONDITIONAL_JUMP`
<a id="insn-00ab1184"></a> `00ab1184` | `55 00 80 52` | mov w21,#0x2 | `FALL_THROUGH`
<a id="insn-00ab1188"></a> `00ab1188` | `08 00 00 14` | b 0x00ab11a8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab118c"></a> `00ab118c` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab1190"></a> `00ab1190` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1194"></a> `00ab1194` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1198"></a> `00ab1198` | `1f 25 00 71` | cmp w8,#0x9 | `FALL_THROUGH`
<a id="insn-00ab119c"></a> `00ab119c` | `cc 00 00 54` | b.gt 0x00ab11b4 | `CONDITIONAL_JUMP`
<a id="insn-00ab11a0"></a> `00ab11a0` | `75 00 80 52` | mov w21,#0x3 | `FALL_THROUGH`
<a id="insn-00ab11a4"></a> `00ab11a4` | `d5 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab11a8"></a> `00ab11a8` | `08 8e 8f 52` | mov w8,#0x7c70 | `FALL_THROUGH`
<a id="insn-00ab11ac"></a> `00ab11ac` | `88 07 a0 72` | movk w8,#0x3c, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab11b0"></a> `00ab11b0` | `15 68 28 b8` | str w21,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab11b4"></a> `00ab11b4` | `d1 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab11b8"></a> `00ab11b8` | `08 8e 8f 52` | mov w8,#0x7c70 | `FALL_THROUGH`
<a id="insn-00ab11bc"></a> `00ab11bc` | `88 07 a0 72` | movk w8,#0x3c, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab11c0"></a> `00ab11c0` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab11c4"></a> `00ab11c4` | `e8 00 00 34` | cbz w8,0x00ab11e0 | `CONDITIONAL_JUMP`
<a id="insn-00ab11c8"></a> `00ab11c8` | `cc 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab11cc"></a> `00ab11cc` | `08 8e 8f 52` | mov w8,#0x7c70 | `FALL_THROUGH`
<a id="insn-00ab11d0"></a> `00ab11d0` | `88 07 a0 72` | movk w8,#0x3c, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab11d4"></a> `00ab11d4` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab11d8"></a> `00ab11d8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab11dc"></a> `00ab11dc` | `e1 13 00 54` | b.ne 0x00ab1458 | `CONDITIONAL_JUMP`
<a id="insn-00ab11e0"></a> `00ab11e0` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00ab11e4"></a> `00ab11e4` | `c5 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab11e8"></a> `00ab11e8` | `88 8d 8f 52` | mov w8,#0x7c6c | `FALL_THROUGH`
<a id="insn-00ab11ec"></a> `00ab11ec` | `88 07 a0 72` | movk w8,#0x3c, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab11f0"></a> `00ab11f0` | `15 68 28 b8` | str w21,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab11f4"></a> `00ab11f4` | `c1 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab11f8"></a> `00ab11f8` | `88 d7 92 52` | mov w8,#0x96bc | `FALL_THROUGH`
<a id="insn-00ab11fc"></a> `00ab11fc` | `09 00 80 12` | mov w9,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab1200"></a> `00ab1200` | `e8 08 a0 72` | movk w8,#0x47, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1204"></a> `00ab1204` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1208"></a> `00ab1208` | `bc 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab120c"></a> `00ab120c` | `08 89 88 52` | mov w8,#0x4448 | `FALL_THROUGH`
<a id="insn-00ab1210"></a> `00ab1210` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1214"></a> `00ab1214` | `1f 68 28 b8` | str wzr,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1218"></a> `00ab1218` | `b8 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab121c"></a> `00ab121c` | `38 af f6 97` | bl 0x0085cefc | `UNCONDITIONAL_CALL`
<a id="insn-00ab1220"></a> `00ab1220` | `b6 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1224"></a> `00ab1224` | `7f 4e 00 31` | cmn w19,#0x13 | `FALL_THROUGH`
<a id="insn-00ab1228"></a> `00ab1228` | `60 0f 00 54` | b.eq 0x00ab1414 | `CONDITIONAL_JUMP`
<a id="insn-00ab122c"></a> `00ab122c` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab1230"></a> `00ab1230` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1234"></a> `00ab1234` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1238"></a> `00ab1238` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00ab123c"></a> `00ab123c` | `c1 0e 00 54` | b.ne 0x00ab1414 | `CONDITIONAL_JUMP`
<a id="insn-00ab1240"></a> `00ab1240` | `7f 2a 00 31` | cmn w19,#0xa | `FALL_THROUGH`
<a id="insn-00ab1244"></a> `00ab1244` | `a1 00 00 54` | b.ne 0x00ab1258 | `CONDITIONAL_JUMP`
<a id="insn-00ab1248"></a> `00ab1248` | `ac 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab124c"></a> `00ab124c` | `88 3c 84 52` | mov w8,#0x21e4 | `FALL_THROUGH`
<a id="insn-00ab1250"></a> `00ab1250` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1254"></a> `00ab1254` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ab1258"></a> `00ab1258` | `a8 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab125c"></a> `00ab125c` | `a6 b0 f6 97` | bl 0x0085d4f4 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1260"></a> `00ab1260` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00ab1264"></a> `00ab1264` | `a5 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1268"></a> `00ab1268` | `88 67 8e 52` | mov w8,#0x733c | `FALL_THROUGH`
<a id="insn-00ab126c"></a> `00ab126c` | `96 3e 80 52` | mov w22,#0x1f4 | `FALL_THROUGH`
<a id="insn-00ab1270"></a> `00ab1270` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1274"></a> `00ab1274` | `15 68 28 b8` | str w21,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1278"></a> `00ab1278` | `15 18 9d 52` | mov w21,#0xe8c0 | `FALL_THROUGH`
<a id="insn-00ab127c"></a> `00ab127c` | `15 07 a0 72` | movk w21,#0x38, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1280"></a> `00ab1280` | `04 00 00 14` | b 0x00ab1290 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab1284"></a> `00ab1284` | `d6 06 00 f1` | subs x22,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1288"></a> `00ab1288` | `b5 12 00 91` | add x21,x21,#0x4 | `FALL_THROUGH`
<a id="insn-00ab128c"></a> `00ab128c` | `00 02 00 54` | b.eq 0x00ab12cc | `CONDITIONAL_JUMP`
<a id="insn-00ab1290"></a> `00ab1290` | `9a 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1294"></a> `00ab1294` | `17 68 75 b8` | ldr w23,[x0, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1298"></a> `00ab1298` | `98 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab129c"></a> `00ab129c` | `08 00 15 8b` | add x8,x0,x21 | `FALL_THROUGH`
<a id="insn-00ab12a0"></a> `00ab12a0` | `08 41 1f d1` | sub x8,x8,#0x7d0 | `FALL_THROUGH`
<a id="insn-00ab12a4"></a> `00ab12a4` | `08 01 40 b9` | ldr w8,[x8] | `FALL_THROUGH`
<a id="insn-00ab12a8"></a> `00ab12a8` | `ff 02 08 6b` | cmp w23,w8 | `FALL_THROUGH`
<a id="insn-00ab12ac"></a> `00ab12ac` | `c0 fe ff 54` | b.eq 0x00ab1284 | `CONDITIONAL_JUMP`
<a id="insn-00ab12b0"></a> `00ab12b0` | `92 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab12b4"></a> `00ab12b4` | `08 00 15 8b` | add x8,x0,x21 | `FALL_THROUGH`
<a id="insn-00ab12b8"></a> `00ab12b8` | `08 41 1f d1` | sub x8,x8,#0x7d0 | `FALL_THROUGH`
<a id="insn-00ab12bc"></a> `00ab12bc` | `17 01 40 b9` | ldr w23,[x8] | `FALL_THROUGH`
<a id="insn-00ab12c0"></a> `00ab12c0` | `8e 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab12c4"></a> `00ab12c4` | `17 68 35 b8` | str w23,[x0, x21, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab12c8"></a> `00ab12c8` | `ef ff ff 17` | b 0x00ab1284 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab12cc"></a> `00ab12cc` | `8b 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab12d0"></a> `00ab12d0` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab12d4"></a> `00ab12d4` | `08 10 16 b9` | str w8,[x0, #0x1610] | `FALL_THROUGH`
<a id="insn-00ab12d8"></a> `00ab12d8` | `88 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab12dc"></a> `00ab12dc` | `08 89 88 52` | mov w8,#0x4448 | `FALL_THROUGH`
<a id="insn-00ab12e0"></a> `00ab12e0` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00ab12e4"></a> `00ab12e4` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab12e8"></a> `00ab12e8` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab12ec"></a> `00ab12ec` | `83 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab12f0"></a> `00ab12f0` | `88 67 8e 52` | mov w8,#0x733c | `FALL_THROUGH`
<a id="insn-00ab12f4"></a> `00ab12f4` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab12f8"></a> `00ab12f8` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab12fc"></a> `00ab12fc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1300"></a> `00ab1300` | `4b 05 00 54` | b.lt 0x00ab13a8 | `CONDITIONAL_JUMP`
<a id="insn-00ab1304"></a> `00ab1304` | `99 67 8e 52` | mov w25,#0x733c | `FALL_THROUGH`
<a id="insn-00ab1308"></a> `00ab1308` | `1a 1e 9c 52` | mov w26,#0xe0f0 | `FALL_THROUGH`
<a id="insn-00ab130c"></a> `00ab130c` | `9b 89 88 52` | mov w27,#0x444c | `FALL_THROUGH`
<a id="insn-00ab1310"></a> `00ab1310` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00ab1314"></a> `00ab1314` | `17 00 80 12` | mov w23,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab1318"></a> `00ab1318` | `98 0e 80 12` | mov w24,#0xffffff8b | `FALL_THROUGH`
<a id="insn-00ab131c"></a> `00ab131c` | `99 06 a0 72` | movk w25,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1320"></a> `00ab1320` | `1a 07 a0 72` | movk w26,#0x38, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1324"></a> `00ab1324` | `9b 06 a0 72` | movk w27,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1328"></a> `00ab1328` | `08 00 00 14` | b 0x00ab1348 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab132c"></a> `00ab132c` | `b5 06 00 11` | add w21,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1330"></a> `00ab1330` | `72 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1334"></a> `00ab1334` | `08 68 79 b8` | ldr w8,[x0, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1338"></a> `00ab1338` | `f7 06 00 51` | sub w23,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00ab133c"></a> `00ab133c` | `18 73 01 51` | sub w24,w24,#0x5c | `FALL_THROUGH`
<a id="insn-00ab1340"></a> `00ab1340` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00ab1344"></a> `00ab1344` | `2a 03 00 54` | b.ge 0x00ab13a8 | `CONDITIONAL_JUMP`
<a id="insn-00ab1348"></a> `00ab1348` | `6c 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab134c"></a> `00ab134c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ab1350"></a> `00ab1350` | `6a 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1354"></a> `00ab1354` | `08 68 79 b8` | ldr w8,[x0, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1358"></a> `00ab1358` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00ab135c"></a> `00ab135c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00ab1360"></a> `00ab1360` | `e8 02 08 0b` | add w8,w23,w8 | `FALL_THROUGH`
<a id="insn-00ab1364"></a> `00ab1364` | `c8 ca 28 8b` | add x8,x22,w8, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00ab1368"></a> `00ab1368` | `16 69 7a b8` | ldr w22,[x8, x26, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab136c"></a> `00ab136c` | `a0 3b f5 97` | bl 0x008001ec | `UNCONDITIONAL_CALL`
<a id="insn-00ab1370"></a> `00ab1370` | `1f 00 16 6b` | cmp w0,w22 | `FALL_THROUGH`
<a id="insn-00ab1374"></a> `00ab1374` | `c1 fd ff 54` | b.ne 0x00ab132c | `CONDITIONAL_JUMP`
<a id="insn-00ab1378"></a> `00ab1378` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00ab137c"></a> `00ab137c` | `b3 de f1 97` | bl 0x00728e48 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1380"></a> `00ab1380` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00ab1384"></a> `00ab1384` | `5d 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1388"></a> `00ab1388` | `bf ed e6 97` | bl 0x0046ca84 | `UNCONDITIONAL_CALL`
<a id="insn-00ab138c"></a> `00ab138c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00ab1390"></a> `00ab1390` | `08 03 16 4b` | sub w8,w24,w22 | `FALL_THROUGH`
<a id="insn-00ab1394"></a> `00ab1394` | `09 a4 80 1a` | cinc w9,w0,lt | `FALL_THROUGH`
<a id="insn-00ab1398"></a> `00ab1398` | `16 05 89 0b` | add w22,w8,w9, ASR #0x1 | `FALL_THROUGH`
<a id="insn-00ab139c"></a> `00ab139c` | `57 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab13a0"></a> `00ab13a0` | `16 68 3b b8` | str w22,[x0, x27, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab13a4"></a> `00ab13a4` | `e2 ff ff 17` | b 0x00ab132c | `UNCONDITIONAL_JUMP`
<a id="insn-00ab13a8"></a> `00ab13a8` | `54 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab13ac"></a> `00ab13ac` | `88 89 88 52` | mov w8,#0x444c | `FALL_THROUGH`
<a id="insn-00ab13b0"></a> `00ab13b0` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab13b4"></a> `00ab13b4` | `16 68 68 b8` | ldr w22,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab13b8"></a> `00ab13b8` | `54 de f1 97` | bl 0x00728d08 | `UNCONDITIONAL_CALL`
<a id="insn-00ab13bc"></a> `00ab13bc` | `74 0b 80 12` | mov w20,#0xffffffa4 | `FALL_THROUGH`
<a id="insn-00ab13c0"></a> `00ab13c0` | `15 45 80 52` | mov w21,#0x228 | `FALL_THROUGH`
<a id="insn-00ab13c4"></a> `00ab13c4` | `08 54 14 1b` | madd w8,w0,w20,w21 | `FALL_THROUGH`
<a id="insn-00ab13c8"></a> `00ab13c8` | `df 02 08 6b` | cmp w22,w8 | `FALL_THROUGH`
<a id="insn-00ab13cc"></a> `00ab13cc` | `ec 00 00 54` | b.gt 0x00ab13e8 | `CONDITIONAL_JUMP`
<a id="insn-00ab13d0"></a> `00ab13d0` | `4e de f1 97` | bl 0x00728d08 | `UNCONDITIONAL_CALL`
<a id="insn-00ab13d4"></a> `00ab13d4` | `14 54 14 1b` | madd w20,w0,w20,w21 | `FALL_THROUGH`
<a id="insn-00ab13d8"></a> `00ab13d8` | `48 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab13dc"></a> `00ab13dc` | `88 89 88 52` | mov w8,#0x444c | `FALL_THROUGH`
<a id="insn-00ab13e0"></a> `00ab13e0` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab13e4"></a> `00ab13e4` | `14 68 28 b8` | str w20,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab13e8"></a> `00ab13e8` | `44 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab13ec"></a> `00ab13ec` | `88 89 88 52` | mov w8,#0x444c | `FALL_THROUGH`
<a id="insn-00ab13f0"></a> `00ab13f0` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab13f4"></a> `00ab13f4` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab13f8"></a> `00ab13f8` | `1f 71 01 71` | cmp w8,#0x5c | `FALL_THROUGH`
<a id="insn-00ab13fc"></a> `00ab13fc` | `cb 00 00 54` | b.lt 0x00ab1414 | `CONDITIONAL_JUMP`
<a id="insn-00ab1400"></a> `00ab1400` | `3e 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1404"></a> `00ab1404` | `88 89 88 52` | mov w8,#0x444c | `FALL_THROUGH`
<a id="insn-00ab1408"></a> `00ab1408` | `89 0b 80 52` | mov w9,#0x5c | `FALL_THROUGH`
<a id="insn-00ab140c"></a> `00ab140c` | `88 06 a0 72` | movk w8,#0x34, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1410"></a> `00ab1410` | `09 68 28 b8` | str w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1414"></a> `00ab1414` | `7f 4e 00 31` | cmn w19,#0x13 | `FALL_THROUGH`
<a id="insn-00ab1418"></a> `00ab1418` | `20 17 00 54` | b.eq 0x00ab16fc | `CONDITIONAL_JUMP`
<a id="insn-00ab141c"></a> `00ab141c` | `37 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1420"></a> `00ab1420` | `36 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1424"></a> `00ab1424` | `08 1c 9f 52` | mov w8,#0xf8e0 | `FALL_THROUGH`
<a id="insn-00ab1428"></a> `00ab1428` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab142c"></a> `00ab142c` | `13 68 68 b8` | ldr w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1430"></a> `00ab1430` | `32 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1434"></a> `00ab1434` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab1438"></a> `00ab1438` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab143c"></a> `00ab143c` | `1f 89 01 71` | cmp w8,#0x62 | `FALL_THROUGH`
<a id="insn-00ab1440"></a> `00ab1440` | `e1 01 00 54` | b.ne 0x00ab147c | `CONDITIONAL_JUMP`
<a id="insn-00ab1444"></a> `00ab1444` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab1448"></a> `00ab1448` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab144c"></a> `00ab144c` | `21 04 00 54` | b.ne 0x00ab14d0 | `CONDITIONAL_JUMP`
<a id="insn-00ab1450"></a> `00ab1450` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00ab1454"></a> `00ab1454` | `a6 00 00 14` | b 0x00ab16ec | `UNCONDITIONAL_JUMP`
<a id="insn-00ab1458"></a> `00ab1458` | `28 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab145c"></a> `00ab145c` | `08 8e 8f 52` | mov w8,#0x7c70 | `FALL_THROUGH`
<a id="insn-00ab1460"></a> `00ab1460` | `88 07 a0 72` | movk w8,#0x3c, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1464"></a> `00ab1464` | `15 68 68 b8` | ldr w21,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1468"></a> `00ab1468` | `24 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab146c"></a> `00ab146c` | `bf 0a 00 71` | cmp w21,#0x2 | `FALL_THROUGH`
<a id="insn-00ab1470"></a> `00ab1470` | `61 01 00 54` | b.ne 0x00ab149c | `CONDITIONAL_JUMP`
<a id="insn-00ab1474"></a> `00ab1474` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1478"></a> `00ab1478` | `5c ff ff 17` | b 0x00ab11e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab147c"></a> `00ab147c` | `1f 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1480"></a> `00ab1480` | `00 80 2f 91` | add x0,x0,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ab1484"></a> `00ab1484` | `61 4b f2 97` | bl 0x00744208 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1488"></a> `00ab1488` | `80 01 00 36` | tbz w0,#0x0,0x00ab14b8 | `CONDITIONAL_JUMP`
<a id="insn-00ab148c"></a> `00ab148c` | `c8 7c 80 52` | mov w8,#0x3e6 | `FALL_THROUGH`
<a id="insn-00ab1490"></a> `00ab1490` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab1494"></a> `00ab1494` | `e0 fd ff 54` | b.eq 0x00ab1450 | `CONDITIONAL_JUMP`
<a id="insn-00ab1498"></a> `00ab1498` | `0e 00 00 14` | b 0x00ab14d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab149c"></a> `00ab149c` | `08 8e 8f 52` | mov w8,#0x7c70 | `FALL_THROUGH`
<a id="insn-00ab14a0"></a> `00ab14a0` | `88 07 a0 72` | movk w8,#0x3c, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab14a4"></a> `00ab14a4` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab14a8"></a> `00ab14a8` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00ab14ac"></a> `00ab14ac` | `41 ea ff 54` | b.ne 0x00ab11f4 | `CONDITIONAL_JUMP`
<a id="insn-00ab14b0"></a> `00ab14b0` | `55 00 80 52` | mov w21,#0x2 | `FALL_THROUGH`
<a id="insn-00ab14b4"></a> `00ab14b4` | `4c ff ff 17` | b 0x00ab11e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab14b8"></a> `00ab14b8` | `10 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab14bc"></a> `00ab14bc` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab14c0"></a> `00ab14c0` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab14c4"></a> `00ab14c4` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab14c8"></a> `00ab14c8` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab14cc"></a> `00ab14cc` | `20 fc ff 54` | b.eq 0x00ab1450 | `CONDITIONAL_JUMP`
<a id="insn-00ab14d0"></a> `00ab14d0` | `0a 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab14d4"></a> `00ab14d4` | `09 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab14d8"></a> `00ab14d8` | `88 1c 9f 52` | mov w8,#0xf8e4 | `FALL_THROUGH`
<a id="insn-00ab14dc"></a> `00ab14dc` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab14e0"></a> `00ab14e0` | `13 68 68 b8` | ldr w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab14e4"></a> `00ab14e4` | `05 80 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab14e8"></a> `00ab14e8` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab14ec"></a> `00ab14ec` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab14f0"></a> `00ab14f0` | `1f 89 01 71` | cmp w8,#0x62 | `FALL_THROUGH`
<a id="insn-00ab14f4"></a> `00ab14f4` | `c1 00 00 54` | b.ne 0x00ab150c | `CONDITIONAL_JUMP`
<a id="insn-00ab14f8"></a> `00ab14f8` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab14fc"></a> `00ab14fc` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab1500"></a> `00ab1500` | `21 02 00 54` | b.ne 0x00ab1544 | `CONDITIONAL_JUMP`
<a id="insn-00ab1504"></a> `00ab1504` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00ab1508"></a> `00ab1508` | `79 00 00 14` | b 0x00ab16ec | `UNCONDITIONAL_JUMP`
<a id="insn-00ab150c"></a> `00ab150c` | `fb 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1510"></a> `00ab1510` | `00 80 2f 91` | add x0,x0,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ab1514"></a> `00ab1514` | `3d 4b f2 97` | bl 0x00744208 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1518"></a> `00ab1518` | `a0 00 00 36` | tbz w0,#0x0,0x00ab152c | `CONDITIONAL_JUMP`
<a id="insn-00ab151c"></a> `00ab151c` | `c8 7c 80 52` | mov w8,#0x3e6 | `FALL_THROUGH`
<a id="insn-00ab1520"></a> `00ab1520` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab1524"></a> `00ab1524` | `00 ff ff 54` | b.eq 0x00ab1504 | `CONDITIONAL_JUMP`
<a id="insn-00ab1528"></a> `00ab1528` | `07 00 00 14` | b 0x00ab1544 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab152c"></a> `00ab152c` | `f3 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1530"></a> `00ab1530` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab1534"></a> `00ab1534` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1538"></a> `00ab1538` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab153c"></a> `00ab153c` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab1540"></a> `00ab1540` | `20 fe ff 54` | b.eq 0x00ab1504 | `CONDITIONAL_JUMP`
<a id="insn-00ab1544"></a> `00ab1544` | `ed 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1548"></a> `00ab1548` | `ec 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab154c"></a> `00ab154c` | `08 1d 9f 52` | mov w8,#0xf8e8 | `FALL_THROUGH`
<a id="insn-00ab1550"></a> `00ab1550` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1554"></a> `00ab1554` | `13 68 68 b8` | ldr w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1558"></a> `00ab1558` | `e8 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab155c"></a> `00ab155c` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab1560"></a> `00ab1560` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1564"></a> `00ab1564` | `1f 89 01 71` | cmp w8,#0x62 | `FALL_THROUGH`
<a id="insn-00ab1568"></a> `00ab1568` | `c1 00 00 54` | b.ne 0x00ab1580 | `CONDITIONAL_JUMP`
<a id="insn-00ab156c"></a> `00ab156c` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab1570"></a> `00ab1570` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab1574"></a> `00ab1574` | `21 02 00 54` | b.ne 0x00ab15b8 | `CONDITIONAL_JUMP`
<a id="insn-00ab1578"></a> `00ab1578` | `53 00 80 52` | mov w19,#0x2 | `FALL_THROUGH`
<a id="insn-00ab157c"></a> `00ab157c` | `5c 00 00 14` | b 0x00ab16ec | `UNCONDITIONAL_JUMP`
<a id="insn-00ab1580"></a> `00ab1580` | `de 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1584"></a> `00ab1584` | `00 80 2f 91` | add x0,x0,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ab1588"></a> `00ab1588` | `20 4b f2 97` | bl 0x00744208 | `UNCONDITIONAL_CALL`
<a id="insn-00ab158c"></a> `00ab158c` | `a0 00 00 36` | tbz w0,#0x0,0x00ab15a0 | `CONDITIONAL_JUMP`
<a id="insn-00ab1590"></a> `00ab1590` | `c8 7c 80 52` | mov w8,#0x3e6 | `FALL_THROUGH`
<a id="insn-00ab1594"></a> `00ab1594` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab1598"></a> `00ab1598` | `00 ff ff 54` | b.eq 0x00ab1578 | `CONDITIONAL_JUMP`
<a id="insn-00ab159c"></a> `00ab159c` | `07 00 00 14` | b 0x00ab15b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab15a0"></a> `00ab15a0` | `d6 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab15a4"></a> `00ab15a4` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab15a8"></a> `00ab15a8` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab15ac"></a> `00ab15ac` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab15b0"></a> `00ab15b0` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab15b4"></a> `00ab15b4` | `20 fe ff 54` | b.eq 0x00ab1578 | `CONDITIONAL_JUMP`
<a id="insn-00ab15b8"></a> `00ab15b8` | `d0 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab15bc"></a> `00ab15bc` | `cf 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab15c0"></a> `00ab15c0` | `88 1d 9f 52` | mov w8,#0xf8ec | `FALL_THROUGH`
<a id="insn-00ab15c4"></a> `00ab15c4` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab15c8"></a> `00ab15c8` | `13 68 68 b8` | ldr w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab15cc"></a> `00ab15cc` | `cb 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab15d0"></a> `00ab15d0` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab15d4"></a> `00ab15d4` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab15d8"></a> `00ab15d8` | `1f 89 01 71` | cmp w8,#0x62 | `FALL_THROUGH`
<a id="insn-00ab15dc"></a> `00ab15dc` | `61 00 00 54` | b.ne 0x00ab15e8 | `CONDITIONAL_JUMP`
<a id="insn-00ab15e0"></a> `00ab15e0` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab15e4"></a> `00ab15e4` | `0b 00 00 14` | b 0x00ab1610 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab15e8"></a> `00ab15e8` | `c4 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab15ec"></a> `00ab15ec` | `00 80 2f 91` | add x0,x0,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ab15f0"></a> `00ab15f0` | `06 4b f2 97` | bl 0x00744208 | `UNCONDITIONAL_CALL`
<a id="insn-00ab15f4"></a> `00ab15f4` | `60 00 00 36` | tbz w0,#0x0,0x00ab1600 | `CONDITIONAL_JUMP`
<a id="insn-00ab15f8"></a> `00ab15f8` | `c8 7c 80 52` | mov w8,#0x3e6 | `FALL_THROUGH`
<a id="insn-00ab15fc"></a> `00ab15fc` | `05 00 00 14` | b 0x00ab1610 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab1600"></a> `00ab1600` | `be 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1604"></a> `00ab1604` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab1608"></a> `00ab1608` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab160c"></a> `00ab160c` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1610"></a> `00ab1610` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab1614"></a> `00ab1614` | `61 00 00 54` | b.ne 0x00ab1620 | `CONDITIONAL_JUMP`
<a id="insn-00ab1618"></a> `00ab1618` | `73 00 80 52` | mov w19,#0x3 | `FALL_THROUGH`
<a id="insn-00ab161c"></a> `00ab161c` | `34 00 00 14` | b 0x00ab16ec | `UNCONDITIONAL_JUMP`
<a id="insn-00ab1620"></a> `00ab1620` | `b6 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1624"></a> `00ab1624` | `b5 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1628"></a> `00ab1628` | `08 1e 9f 52` | mov w8,#0xf8f0 | `FALL_THROUGH`
<a id="insn-00ab162c"></a> `00ab162c` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1630"></a> `00ab1630` | `13 68 68 b8` | ldr w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1634"></a> `00ab1634` | `b1 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1638"></a> `00ab1638` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab163c"></a> `00ab163c` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1640"></a> `00ab1640` | `1f 89 01 71` | cmp w8,#0x62 | `FALL_THROUGH`
<a id="insn-00ab1644"></a> `00ab1644` | `61 00 00 54` | b.ne 0x00ab1650 | `CONDITIONAL_JUMP`
<a id="insn-00ab1648"></a> `00ab1648` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab164c"></a> `00ab164c` | `0b 00 00 14` | b 0x00ab1678 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab1650"></a> `00ab1650` | `aa 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1654"></a> `00ab1654` | `00 80 2f 91` | add x0,x0,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ab1658"></a> `00ab1658` | `ec 4a f2 97` | bl 0x00744208 | `UNCONDITIONAL_CALL`
<a id="insn-00ab165c"></a> `00ab165c` | `60 00 00 36` | tbz w0,#0x0,0x00ab1668 | `CONDITIONAL_JUMP`
<a id="insn-00ab1660"></a> `00ab1660` | `c8 7c 80 52` | mov w8,#0x3e6 | `FALL_THROUGH`
<a id="insn-00ab1664"></a> `00ab1664` | `05 00 00 14` | b 0x00ab1678 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab1668"></a> `00ab1668` | `a4 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab166c"></a> `00ab166c` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab1670"></a> `00ab1670` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1674"></a> `00ab1674` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab1678"></a> `00ab1678` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab167c"></a> `00ab167c` | `61 00 00 54` | b.ne 0x00ab1688 | `CONDITIONAL_JUMP`
<a id="insn-00ab1680"></a> `00ab1680` | `93 00 80 52` | mov w19,#0x4 | `FALL_THROUGH`
<a id="insn-00ab1684"></a> `00ab1684` | `1a 00 00 14` | b 0x00ab16ec | `UNCONDITIONAL_JUMP`
<a id="insn-00ab1688"></a> `00ab1688` | `9c 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab168c"></a> `00ab168c` | `9b 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1690"></a> `00ab1690` | `88 1e 9f 52` | mov w8,#0xf8f4 | `FALL_THROUGH`
<a id="insn-00ab1694"></a> `00ab1694` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab1698"></a> `00ab1698` | `13 68 68 b8` | ldr w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab169c"></a> `00ab169c` | `97 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab16a0"></a> `00ab16a0` | `08 b5 98 52` | mov w8,#0xc5a8 | `FALL_THROUGH`
<a id="insn-00ab16a4"></a> `00ab16a4` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab16a8"></a> `00ab16a8` | `1f 89 01 71` | cmp w8,#0x62 | `FALL_THROUGH`
<a id="insn-00ab16ac"></a> `00ab16ac` | `61 00 00 54` | b.ne 0x00ab16b8 | `CONDITIONAL_JUMP`
<a id="insn-00ab16b0"></a> `00ab16b0` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab16b4"></a> `00ab16b4` | `0b 00 00 14` | b 0x00ab16e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab16b8"></a> `00ab16b8` | `90 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab16bc"></a> `00ab16bc` | `00 80 2f 91` | add x0,x0,#0xbe0 | `FALL_THROUGH`
<a id="insn-00ab16c0"></a> `00ab16c0` | `d2 4a f2 97` | bl 0x00744208 | `UNCONDITIONAL_CALL`
<a id="insn-00ab16c4"></a> `00ab16c4` | `60 00 00 36` | tbz w0,#0x0,0x00ab16d0 | `CONDITIONAL_JUMP`
<a id="insn-00ab16c8"></a> `00ab16c8` | `c8 7c 80 52` | mov w8,#0x3e6 | `FALL_THROUGH`
<a id="insn-00ab16cc"></a> `00ab16cc` | `05 00 00 14` | b 0x00ab16e0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ab16d0"></a> `00ab16d0` | `8a 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab16d4"></a> `00ab16d4` | `88 2e 87 52` | mov w8,#0x3974 | `FALL_THROUGH`
<a id="insn-00ab16d8"></a> `00ab16d8` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab16dc"></a> `00ab16dc` | `08 68 68 b8` | ldr w8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab16e0"></a> `00ab16e0` | `7f 02 08 6b` | cmp w19,w8 | `FALL_THROUGH`
<a id="insn-00ab16e4"></a> `00ab16e4` | `61 02 00 54` | b.ne 0x00ab1730 | `CONDITIONAL_JUMP`
<a id="insn-00ab16e8"></a> `00ab16e8` | `b3 00 80 52` | mov w19,#0x5 | `FALL_THROUGH`
<a id="insn-00ab16ec"></a> `00ab16ec` | `83 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab16f0"></a> `00ab16f0` | `88 ec 87 52` | mov w8,#0x3f64 | `FALL_THROUGH`
<a id="insn-00ab16f4"></a> `00ab16f4` | `68 06 a0 72` | movk w8,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00ab16f8"></a> `00ab16f8` | `13 68 28 b8` | str w19,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ab16fc"></a> `00ab16fc` | `7f 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1700"></a> `00ab1700` | `7c ad f6 97` | bl 0x0085ccf0 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1704"></a> `00ab1704` | `7c 25 e7 97` | bl 0x0047acf4 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1708"></a> `00ab1708` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00ab170c"></a> `00ab170c` | `e0 2c e7 97` | bl 0x0047ca8c | `UNCONDITIONAL_CALL`
<a id="insn-00ab1710"></a> `00ab1710` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ab1714"></a> `00ab1714` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ab1718"></a> `00ab1718` | `fb 0b 40 f9` | ldr x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ab171c"></a> `00ab171c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ab1720"></a> `00ab1720` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ab1724"></a> `00ab1724` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ab1728"></a> `00ab1728` | `fd 7b c6 a8` | ldp x29,x30,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00ab172c"></a> `00ab172c` | `08 ea f1 17` | b 0x0072bf4c | `CALL_TERMINATOR`
<a id="insn-00ab1730"></a> `00ab1730` | `72 7f f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ab1734"></a> `00ab1734` | `f2 ff ff 17` | b 0x00ab16fc | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00ab0ddc`](#insn-00ab0ddc) 範囲 `[['00ab0ddc', '00ab0e7f']]`
  - `CONDITIONAL_JUMP` [`00ab0e7c`](#insn-00ab0e7c) → [`00ab0ebc`](#insn-00ab0ebc)
  - `FALL_THROUGH` [`00ab0e7c`](#insn-00ab0e7c) → [`00ab0e80`](#insn-00ab0e80)
- ブロック [`00ab0e80`](#insn-00ab0e80) 範囲 `[['00ab0e80', '00ab0e87']]`
  - `CONDITIONAL_JUMP` [`00ab0e84`](#insn-00ab0e84) → [`00ab0f6c`](#insn-00ab0f6c)
  - `FALL_THROUGH` [`00ab0e84`](#insn-00ab0e84) → [`00ab0e88`](#insn-00ab0e88)
- ブロック [`00ab0e88`](#insn-00ab0e88) 範囲 `[['00ab0e88', '00ab0e8f']]`
  - `CONDITIONAL_JUMP` [`00ab0e8c`](#insn-00ab0e8c) → [`00ab0ef4`](#insn-00ab0ef4)
  - `FALL_THROUGH` [`00ab0e8c`](#insn-00ab0e8c) → [`00ab0e90`](#insn-00ab0e90)
- ブロック [`00ab0e90`](#insn-00ab0e90) 範囲 `[['00ab0e90', '00ab0ebb']]`
  - `UNCONDITIONAL_JUMP` [`00ab0eb8`](#insn-00ab0eb8) → [`00ab1068`](#insn-00ab1068)
- ブロック [`00ab0ebc`](#insn-00ab0ebc) 範囲 `[['00ab0ebc', '00ab0ec3']]`
  - `CONDITIONAL_JUMP` [`00ab0ec0`](#insn-00ab0ec0) → [`00ab1040`](#insn-00ab1040)
  - `FALL_THROUGH` [`00ab0ec0`](#insn-00ab0ec0) → [`00ab0ec4`](#insn-00ab0ec4)
- ブロック [`00ab0ec4`](#insn-00ab0ec4) 範囲 `[['00ab0ec4', '00ab0ecb']]`
  - `CONDITIONAL_JUMP` [`00ab0ec8`](#insn-00ab0ec8) → [`00ab0ef4`](#insn-00ab0ef4)
  - `FALL_THROUGH` [`00ab0ec8`](#insn-00ab0ec8) → [`00ab0ecc`](#insn-00ab0ecc)
- ブロック [`00ab0ecc`](#insn-00ab0ecc) 範囲 `[['00ab0ecc', '00ab0ef3']]`
  - `UNCONDITIONAL_JUMP` [`00ab0ef0`](#insn-00ab0ef0) → [`00ab1068`](#insn-00ab1068)
- ブロック [`00ab0ef4`](#insn-00ab0ef4) 範囲 `[['00ab0ef4', '00ab0f53']]`
  - `CONDITIONAL_JUMP` [`00ab0f50`](#insn-00ab0f50) → [`00ab1078`](#insn-00ab1078)
  - `FALL_THROUGH` [`00ab0f50`](#insn-00ab0f50) → [`00ab0f54`](#insn-00ab0f54)
- ブロック [`00ab0f54`](#insn-00ab0f54) 範囲 `[['00ab0f54', '00ab0f6b']]`
  - `UNCONDITIONAL_JUMP` [`00ab0f68`](#insn-00ab0f68) → [`00ab10b4`](#insn-00ab10b4)
- ブロック [`00ab0f6c`](#insn-00ab0f6c) 範囲 `[['00ab0f6c', '00ab103f']]`
  - `UNCONDITIONAL_JUMP` [`00ab103c`](#insn-00ab103c) → [`00ab1078`](#insn-00ab1078)
- ブロック [`00ab1040`](#insn-00ab1040) 範囲 `[['00ab1040', '00ab1067']]`
  - `FALL_THROUGH` [`00ab1064`](#insn-00ab1064) → [`00ab1068`](#insn-00ab1068)
- ブロック [`00ab1068`](#insn-00ab1068) 範囲 `[['00ab1068', '00ab1077']]`
  - `FALL_THROUGH` [`00ab1074`](#insn-00ab1074) → [`00ab1078`](#insn-00ab1078)
- ブロック [`00ab1078`](#insn-00ab1078) 範囲 `[['00ab1078', '00ab10af']]`
  - `CONDITIONAL_JUMP` [`00ab10ac`](#insn-00ab10ac) → [`00ab10c0`](#insn-00ab10c0)
  - `FALL_THROUGH` [`00ab10ac`](#insn-00ab10ac) → [`00ab10b0`](#insn-00ab10b0)
- ブロック [`00ab10b0`](#insn-00ab10b0) 範囲 `[['00ab10b0', '00ab10b3']]`
  - `FALL_THROUGH` [`00ab10b0`](#insn-00ab10b0) → [`00ab10b4`](#insn-00ab10b4)
- ブロック [`00ab10b4`](#insn-00ab10b4) 範囲 `[['00ab10b4', '00ab10bf']]`
  - `FALL_THROUGH` [`00ab10bc`](#insn-00ab10bc) → [`00ab10c0`](#insn-00ab10c0)
- ブロック [`00ab10c0`](#insn-00ab10c0) 範囲 `[['00ab10c0', '00ab10d3']]`
  - `CONDITIONAL_JUMP` [`00ab10d0`](#insn-00ab10d0) → [`00ab10e8`](#insn-00ab10e8)
  - `FALL_THROUGH` [`00ab10d0`](#insn-00ab10d0) → [`00ab10d4`](#insn-00ab10d4)
- ブロック [`00ab10d4`](#insn-00ab10d4) 範囲 `[['00ab10d4', '00ab10e7']]`
  - `CONDITIONAL_JUMP` [`00ab10e4`](#insn-00ab10e4) → [`00ab10fc`](#insn-00ab10fc)
  - `FALL_THROUGH` [`00ab10e4`](#insn-00ab10e4) → [`00ab10e8`](#insn-00ab10e8)
- ブロック [`00ab10e8`](#insn-00ab10e8) 範囲 `[['00ab10e8', '00ab10fb']]`
  - `FALL_THROUGH` [`00ab10f8`](#insn-00ab10f8) → [`00ab10fc`](#insn-00ab10fc)
- ブロック [`00ab10fc`](#insn-00ab10fc) 範囲 `[['00ab10fc', '00ab114b']]`
  - `CONDITIONAL_JUMP` [`00ab1148`](#insn-00ab1148) → [`00ab11a8`](#insn-00ab11a8)
  - `FALL_THROUGH` [`00ab1148`](#insn-00ab1148) → [`00ab114c`](#insn-00ab114c)
- ブロック [`00ab114c`](#insn-00ab114c) 範囲 `[['00ab114c', '00ab1163']]`
  - `CONDITIONAL_JUMP` [`00ab1160`](#insn-00ab1160) → [`00ab116c`](#insn-00ab116c)
  - `FALL_THROUGH` [`00ab1160`](#insn-00ab1160) → [`00ab1164`](#insn-00ab1164)
- ブロック [`00ab1164`](#insn-00ab1164) 範囲 `[['00ab1164', '00ab116b']]`
  - `UNCONDITIONAL_JUMP` [`00ab1168`](#insn-00ab1168) → [`00ab11a8`](#insn-00ab11a8)
- ブロック [`00ab116c`](#insn-00ab116c) 範囲 `[['00ab116c', '00ab1183']]`
  - `CONDITIONAL_JUMP` [`00ab1180`](#insn-00ab1180) → [`00ab118c`](#insn-00ab118c)
  - `FALL_THROUGH` [`00ab1180`](#insn-00ab1180) → [`00ab1184`](#insn-00ab1184)
- ブロック [`00ab1184`](#insn-00ab1184) 範囲 `[['00ab1184', '00ab118b']]`
  - `UNCONDITIONAL_JUMP` [`00ab1188`](#insn-00ab1188) → [`00ab11a8`](#insn-00ab11a8)
- ブロック [`00ab118c`](#insn-00ab118c) 範囲 `[['00ab118c', '00ab119f']]`
  - `CONDITIONAL_JUMP` [`00ab119c`](#insn-00ab119c) → [`00ab11b4`](#insn-00ab11b4)
  - `FALL_THROUGH` [`00ab119c`](#insn-00ab119c) → [`00ab11a0`](#insn-00ab11a0)
- ブロック [`00ab11a0`](#insn-00ab11a0) 範囲 `[['00ab11a0', '00ab11a7']]`
  - `FALL_THROUGH` [`00ab11a4`](#insn-00ab11a4) → [`00ab11a8`](#insn-00ab11a8)
- ブロック [`00ab11a8`](#insn-00ab11a8) 範囲 `[['00ab11a8', '00ab11b3']]`
  - `FALL_THROUGH` [`00ab11b0`](#insn-00ab11b0) → [`00ab11b4`](#insn-00ab11b4)
- ブロック [`00ab11b4`](#insn-00ab11b4) 範囲 `[['00ab11b4', '00ab11c7']]`
  - `CONDITIONAL_JUMP` [`00ab11c4`](#insn-00ab11c4) → [`00ab11e0`](#insn-00ab11e0)
  - `FALL_THROUGH` [`00ab11c4`](#insn-00ab11c4) → [`00ab11c8`](#insn-00ab11c8)
- ブロック [`00ab11c8`](#insn-00ab11c8) 範囲 `[['00ab11c8', '00ab11df']]`
  - `CONDITIONAL_JUMP` [`00ab11dc`](#insn-00ab11dc) → [`00ab1458`](#insn-00ab1458)
  - `FALL_THROUGH` [`00ab11dc`](#insn-00ab11dc) → [`00ab11e0`](#insn-00ab11e0)
- ブロック [`00ab11e0`](#insn-00ab11e0) 範囲 `[['00ab11e0', '00ab11e3']]`
  - `FALL_THROUGH` [`00ab11e0`](#insn-00ab11e0) → [`00ab11e4`](#insn-00ab11e4)
- ブロック [`00ab11e4`](#insn-00ab11e4) 範囲 `[['00ab11e4', '00ab11e7']]`
  - `FALL_THROUGH` [`00ab11e4`](#insn-00ab11e4) → [`00ab11e8`](#insn-00ab11e8)
- ブロック [`00ab11e8`](#insn-00ab11e8) 範囲 `[['00ab11e8', '00ab11f3']]`
  - `FALL_THROUGH` [`00ab11f0`](#insn-00ab11f0) → [`00ab11f4`](#insn-00ab11f4)
- ブロック [`00ab11f4`](#insn-00ab11f4) 範囲 `[['00ab11f4', '00ab122b']]`
  - `CONDITIONAL_JUMP` [`00ab1228`](#insn-00ab1228) → [`00ab1414`](#insn-00ab1414)
  - `FALL_THROUGH` [`00ab1228`](#insn-00ab1228) → [`00ab122c`](#insn-00ab122c)
- ブロック [`00ab122c`](#insn-00ab122c) 範囲 `[['00ab122c', '00ab123f']]`
  - `CONDITIONAL_JUMP` [`00ab123c`](#insn-00ab123c) → [`00ab1414`](#insn-00ab1414)
  - `FALL_THROUGH` [`00ab123c`](#insn-00ab123c) → [`00ab1240`](#insn-00ab1240)
- ブロック [`00ab1240`](#insn-00ab1240) 範囲 `[['00ab1240', '00ab1247']]`
  - `CONDITIONAL_JUMP` [`00ab1244`](#insn-00ab1244) → [`00ab1258`](#insn-00ab1258)
  - `FALL_THROUGH` [`00ab1244`](#insn-00ab1244) → [`00ab1248`](#insn-00ab1248)
- ブロック [`00ab1248`](#insn-00ab1248) 範囲 `[['00ab1248', '00ab1257']]`
  - `FALL_THROUGH` [`00ab1254`](#insn-00ab1254) → [`00ab1258`](#insn-00ab1258)
- ブロック [`00ab1258`](#insn-00ab1258) 範囲 `[['00ab1258', '00ab1283']]`
  - `UNCONDITIONAL_JUMP` [`00ab1280`](#insn-00ab1280) → [`00ab1290`](#insn-00ab1290)
- ブロック [`00ab1284`](#insn-00ab1284) 範囲 `[['00ab1284', '00ab128f']]`
  - `CONDITIONAL_JUMP` [`00ab128c`](#insn-00ab128c) → [`00ab12cc`](#insn-00ab12cc)
  - `FALL_THROUGH` [`00ab128c`](#insn-00ab128c) → [`00ab1290`](#insn-00ab1290)
- ブロック [`00ab1290`](#insn-00ab1290) 範囲 `[['00ab1290', '00ab12af']]`
  - `CONDITIONAL_JUMP` [`00ab12ac`](#insn-00ab12ac) → [`00ab1284`](#insn-00ab1284)
  - `FALL_THROUGH` [`00ab12ac`](#insn-00ab12ac) → [`00ab12b0`](#insn-00ab12b0)
- ブロック [`00ab12b0`](#insn-00ab12b0) 範囲 `[['00ab12b0', '00ab12cb']]`
  - `UNCONDITIONAL_JUMP` [`00ab12c8`](#insn-00ab12c8) → [`00ab1284`](#insn-00ab1284)
- ブロック [`00ab12cc`](#insn-00ab12cc) 範囲 `[['00ab12cc', '00ab1303']]`
  - `CONDITIONAL_JUMP` [`00ab1300`](#insn-00ab1300) → [`00ab13a8`](#insn-00ab13a8)
  - `FALL_THROUGH` [`00ab1300`](#insn-00ab1300) → [`00ab1304`](#insn-00ab1304)
- ブロック [`00ab1304`](#insn-00ab1304) 範囲 `[['00ab1304', '00ab132b']]`
  - `UNCONDITIONAL_JUMP` [`00ab1328`](#insn-00ab1328) → [`00ab1348`](#insn-00ab1348)
- ブロック [`00ab132c`](#insn-00ab132c) 範囲 `[['00ab132c', '00ab1347']]`
  - `CONDITIONAL_JUMP` [`00ab1344`](#insn-00ab1344) → [`00ab13a8`](#insn-00ab13a8)
  - `FALL_THROUGH` [`00ab1344`](#insn-00ab1344) → [`00ab1348`](#insn-00ab1348)
- ブロック [`00ab1348`](#insn-00ab1348) 範囲 `[['00ab1348', '00ab1377']]`
  - `CONDITIONAL_JUMP` [`00ab1374`](#insn-00ab1374) → [`00ab132c`](#insn-00ab132c)
  - `FALL_THROUGH` [`00ab1374`](#insn-00ab1374) → [`00ab1378`](#insn-00ab1378)
- ブロック [`00ab1378`](#insn-00ab1378) 範囲 `[['00ab1378', '00ab13a7']]`
  - `UNCONDITIONAL_JUMP` [`00ab13a4`](#insn-00ab13a4) → [`00ab132c`](#insn-00ab132c)
- ブロック [`00ab13a8`](#insn-00ab13a8) 範囲 `[['00ab13a8', '00ab13cf']]`
  - `CONDITIONAL_JUMP` [`00ab13cc`](#insn-00ab13cc) → [`00ab13e8`](#insn-00ab13e8)
  - `FALL_THROUGH` [`00ab13cc`](#insn-00ab13cc) → [`00ab13d0`](#insn-00ab13d0)
- ブロック [`00ab13d0`](#insn-00ab13d0) 範囲 `[['00ab13d0', '00ab13e7']]`
  - `FALL_THROUGH` [`00ab13e4`](#insn-00ab13e4) → [`00ab13e8`](#insn-00ab13e8)
- ブロック [`00ab13e8`](#insn-00ab13e8) 範囲 `[['00ab13e8', '00ab13ff']]`
  - `CONDITIONAL_JUMP` [`00ab13fc`](#insn-00ab13fc) → [`00ab1414`](#insn-00ab1414)
  - `FALL_THROUGH` [`00ab13fc`](#insn-00ab13fc) → [`00ab1400`](#insn-00ab1400)
- ブロック [`00ab1400`](#insn-00ab1400) 範囲 `[['00ab1400', '00ab1413']]`
  - `FALL_THROUGH` [`00ab1410`](#insn-00ab1410) → [`00ab1414`](#insn-00ab1414)
- ブロック [`00ab1414`](#insn-00ab1414) 範囲 `[['00ab1414', '00ab141b']]`
  - `CONDITIONAL_JUMP` [`00ab1418`](#insn-00ab1418) → [`00ab16fc`](#insn-00ab16fc)
  - `FALL_THROUGH` [`00ab1418`](#insn-00ab1418) → [`00ab141c`](#insn-00ab141c)
- ブロック [`00ab141c`](#insn-00ab141c) 範囲 `[['00ab141c', '00ab1443']]`
  - `CONDITIONAL_JUMP` [`00ab1440`](#insn-00ab1440) → [`00ab147c`](#insn-00ab147c)
  - `FALL_THROUGH` [`00ab1440`](#insn-00ab1440) → [`00ab1444`](#insn-00ab1444)
- ブロック [`00ab1444`](#insn-00ab1444) 範囲 `[['00ab1444', '00ab144f']]`
  - `CONDITIONAL_JUMP` [`00ab144c`](#insn-00ab144c) → [`00ab14d0`](#insn-00ab14d0)
  - `FALL_THROUGH` [`00ab144c`](#insn-00ab144c) → [`00ab1450`](#insn-00ab1450)
- ブロック [`00ab1450`](#insn-00ab1450) 範囲 `[['00ab1450', '00ab1457']]`
  - `UNCONDITIONAL_JUMP` [`00ab1454`](#insn-00ab1454) → [`00ab16ec`](#insn-00ab16ec)
- ブロック [`00ab1458`](#insn-00ab1458) 範囲 `[['00ab1458', '00ab1473']]`
  - `CONDITIONAL_JUMP` [`00ab1470`](#insn-00ab1470) → [`00ab149c`](#insn-00ab149c)
  - `FALL_THROUGH` [`00ab1470`](#insn-00ab1470) → [`00ab1474`](#insn-00ab1474)
- ブロック [`00ab1474`](#insn-00ab1474) 範囲 `[['00ab1474', '00ab147b']]`
  - `UNCONDITIONAL_JUMP` [`00ab1478`](#insn-00ab1478) → [`00ab11e8`](#insn-00ab11e8)
- ブロック [`00ab147c`](#insn-00ab147c) 範囲 `[['00ab147c', '00ab148b']]`
  - `CONDITIONAL_JUMP` [`00ab1488`](#insn-00ab1488) → [`00ab14b8`](#insn-00ab14b8)
  - `FALL_THROUGH` [`00ab1488`](#insn-00ab1488) → [`00ab148c`](#insn-00ab148c)
- ブロック [`00ab148c`](#insn-00ab148c) 範囲 `[['00ab148c', '00ab1497']]`
  - `CONDITIONAL_JUMP` [`00ab1494`](#insn-00ab1494) → [`00ab1450`](#insn-00ab1450)
  - `FALL_THROUGH` [`00ab1494`](#insn-00ab1494) → [`00ab1498`](#insn-00ab1498)
- ブロック [`00ab1498`](#insn-00ab1498) 範囲 `[['00ab1498', '00ab149b']]`
  - `UNCONDITIONAL_JUMP` [`00ab1498`](#insn-00ab1498) → [`00ab14d0`](#insn-00ab14d0)
- ブロック [`00ab149c`](#insn-00ab149c) 範囲 `[['00ab149c', '00ab14af']]`
  - `CONDITIONAL_JUMP` [`00ab14ac`](#insn-00ab14ac) → [`00ab11f4`](#insn-00ab11f4)
  - `FALL_THROUGH` [`00ab14ac`](#insn-00ab14ac) → [`00ab14b0`](#insn-00ab14b0)
- ブロック [`00ab14b0`](#insn-00ab14b0) 範囲 `[['00ab14b0', '00ab14b7']]`
  - `UNCONDITIONAL_JUMP` [`00ab14b4`](#insn-00ab14b4) → [`00ab11e4`](#insn-00ab11e4)
- ブロック [`00ab14b8`](#insn-00ab14b8) 範囲 `[['00ab14b8', '00ab14cf']]`
  - `CONDITIONAL_JUMP` [`00ab14cc`](#insn-00ab14cc) → [`00ab1450`](#insn-00ab1450)
  - `FALL_THROUGH` [`00ab14cc`](#insn-00ab14cc) → [`00ab14d0`](#insn-00ab14d0)
- ブロック [`00ab14d0`](#insn-00ab14d0) 範囲 `[['00ab14d0', '00ab14f7']]`
  - `CONDITIONAL_JUMP` [`00ab14f4`](#insn-00ab14f4) → [`00ab150c`](#insn-00ab150c)
  - `FALL_THROUGH` [`00ab14f4`](#insn-00ab14f4) → [`00ab14f8`](#insn-00ab14f8)
- ブロック [`00ab14f8`](#insn-00ab14f8) 範囲 `[['00ab14f8', '00ab1503']]`
  - `CONDITIONAL_JUMP` [`00ab1500`](#insn-00ab1500) → [`00ab1544`](#insn-00ab1544)
  - `FALL_THROUGH` [`00ab1500`](#insn-00ab1500) → [`00ab1504`](#insn-00ab1504)
- ブロック [`00ab1504`](#insn-00ab1504) 範囲 `[['00ab1504', '00ab150b']]`
  - `UNCONDITIONAL_JUMP` [`00ab1508`](#insn-00ab1508) → [`00ab16ec`](#insn-00ab16ec)
- ブロック [`00ab150c`](#insn-00ab150c) 範囲 `[['00ab150c', '00ab151b']]`
  - `CONDITIONAL_JUMP` [`00ab1518`](#insn-00ab1518) → [`00ab152c`](#insn-00ab152c)
  - `FALL_THROUGH` [`00ab1518`](#insn-00ab1518) → [`00ab151c`](#insn-00ab151c)
- ブロック [`00ab151c`](#insn-00ab151c) 範囲 `[['00ab151c', '00ab1527']]`
  - `CONDITIONAL_JUMP` [`00ab1524`](#insn-00ab1524) → [`00ab1504`](#insn-00ab1504)
  - `FALL_THROUGH` [`00ab1524`](#insn-00ab1524) → [`00ab1528`](#insn-00ab1528)
- ブロック [`00ab1528`](#insn-00ab1528) 範囲 `[['00ab1528', '00ab152b']]`
  - `UNCONDITIONAL_JUMP` [`00ab1528`](#insn-00ab1528) → [`00ab1544`](#insn-00ab1544)
- ブロック [`00ab152c`](#insn-00ab152c) 範囲 `[['00ab152c', '00ab1543']]`
  - `CONDITIONAL_JUMP` [`00ab1540`](#insn-00ab1540) → [`00ab1504`](#insn-00ab1504)
  - `FALL_THROUGH` [`00ab1540`](#insn-00ab1540) → [`00ab1544`](#insn-00ab1544)
- ブロック [`00ab1544`](#insn-00ab1544) 範囲 `[['00ab1544', '00ab156b']]`
  - `CONDITIONAL_JUMP` [`00ab1568`](#insn-00ab1568) → [`00ab1580`](#insn-00ab1580)
  - `FALL_THROUGH` [`00ab1568`](#insn-00ab1568) → [`00ab156c`](#insn-00ab156c)
- ブロック [`00ab156c`](#insn-00ab156c) 範囲 `[['00ab156c', '00ab1577']]`
  - `CONDITIONAL_JUMP` [`00ab1574`](#insn-00ab1574) → [`00ab15b8`](#insn-00ab15b8)
  - `FALL_THROUGH` [`00ab1574`](#insn-00ab1574) → [`00ab1578`](#insn-00ab1578)
- ブロック [`00ab1578`](#insn-00ab1578) 範囲 `[['00ab1578', '00ab157f']]`
  - `UNCONDITIONAL_JUMP` [`00ab157c`](#insn-00ab157c) → [`00ab16ec`](#insn-00ab16ec)
- ブロック [`00ab1580`](#insn-00ab1580) 範囲 `[['00ab1580', '00ab158f']]`
  - `CONDITIONAL_JUMP` [`00ab158c`](#insn-00ab158c) → [`00ab15a0`](#insn-00ab15a0)
  - `FALL_THROUGH` [`00ab158c`](#insn-00ab158c) → [`00ab1590`](#insn-00ab1590)
- ブロック [`00ab1590`](#insn-00ab1590) 範囲 `[['00ab1590', '00ab159b']]`
  - `CONDITIONAL_JUMP` [`00ab1598`](#insn-00ab1598) → [`00ab1578`](#insn-00ab1578)
  - `FALL_THROUGH` [`00ab1598`](#insn-00ab1598) → [`00ab159c`](#insn-00ab159c)
- ブロック [`00ab159c`](#insn-00ab159c) 範囲 `[['00ab159c', '00ab159f']]`
  - `UNCONDITIONAL_JUMP` [`00ab159c`](#insn-00ab159c) → [`00ab15b8`](#insn-00ab15b8)
- ブロック [`00ab15a0`](#insn-00ab15a0) 範囲 `[['00ab15a0', '00ab15b7']]`
  - `CONDITIONAL_JUMP` [`00ab15b4`](#insn-00ab15b4) → [`00ab1578`](#insn-00ab1578)
  - `FALL_THROUGH` [`00ab15b4`](#insn-00ab15b4) → [`00ab15b8`](#insn-00ab15b8)
- ブロック [`00ab15b8`](#insn-00ab15b8) 範囲 `[['00ab15b8', '00ab15df']]`
  - `CONDITIONAL_JUMP` [`00ab15dc`](#insn-00ab15dc) → [`00ab15e8`](#insn-00ab15e8)
  - `FALL_THROUGH` [`00ab15dc`](#insn-00ab15dc) → [`00ab15e0`](#insn-00ab15e0)
- ブロック [`00ab15e0`](#insn-00ab15e0) 範囲 `[['00ab15e0', '00ab15e7']]`
  - `UNCONDITIONAL_JUMP` [`00ab15e4`](#insn-00ab15e4) → [`00ab1610`](#insn-00ab1610)
- ブロック [`00ab15e8`](#insn-00ab15e8) 範囲 `[['00ab15e8', '00ab15f7']]`
  - `CONDITIONAL_JUMP` [`00ab15f4`](#insn-00ab15f4) → [`00ab1600`](#insn-00ab1600)
  - `FALL_THROUGH` [`00ab15f4`](#insn-00ab15f4) → [`00ab15f8`](#insn-00ab15f8)
- ブロック [`00ab15f8`](#insn-00ab15f8) 範囲 `[['00ab15f8', '00ab15ff']]`
  - `UNCONDITIONAL_JUMP` [`00ab15fc`](#insn-00ab15fc) → [`00ab1610`](#insn-00ab1610)
- ブロック [`00ab1600`](#insn-00ab1600) 範囲 `[['00ab1600', '00ab160f']]`
  - `FALL_THROUGH` [`00ab160c`](#insn-00ab160c) → [`00ab1610`](#insn-00ab1610)
- ブロック [`00ab1610`](#insn-00ab1610) 範囲 `[['00ab1610', '00ab1617']]`
  - `CONDITIONAL_JUMP` [`00ab1614`](#insn-00ab1614) → [`00ab1620`](#insn-00ab1620)
  - `FALL_THROUGH` [`00ab1614`](#insn-00ab1614) → [`00ab1618`](#insn-00ab1618)
- ブロック [`00ab1618`](#insn-00ab1618) 範囲 `[['00ab1618', '00ab161f']]`
  - `UNCONDITIONAL_JUMP` [`00ab161c`](#insn-00ab161c) → [`00ab16ec`](#insn-00ab16ec)
- ブロック [`00ab1620`](#insn-00ab1620) 範囲 `[['00ab1620', '00ab1647']]`
  - `CONDITIONAL_JUMP` [`00ab1644`](#insn-00ab1644) → [`00ab1650`](#insn-00ab1650)
  - `FALL_THROUGH` [`00ab1644`](#insn-00ab1644) → [`00ab1648`](#insn-00ab1648)
- ブロック [`00ab1648`](#insn-00ab1648) 範囲 `[['00ab1648', '00ab164f']]`
  - `UNCONDITIONAL_JUMP` [`00ab164c`](#insn-00ab164c) → [`00ab1678`](#insn-00ab1678)
- ブロック [`00ab1650`](#insn-00ab1650) 範囲 `[['00ab1650', '00ab165f']]`
  - `CONDITIONAL_JUMP` [`00ab165c`](#insn-00ab165c) → [`00ab1668`](#insn-00ab1668)
  - `FALL_THROUGH` [`00ab165c`](#insn-00ab165c) → [`00ab1660`](#insn-00ab1660)
- ブロック [`00ab1660`](#insn-00ab1660) 範囲 `[['00ab1660', '00ab1667']]`
  - `UNCONDITIONAL_JUMP` [`00ab1664`](#insn-00ab1664) → [`00ab1678`](#insn-00ab1678)
- ブロック [`00ab1668`](#insn-00ab1668) 範囲 `[['00ab1668', '00ab1677']]`
  - `FALL_THROUGH` [`00ab1674`](#insn-00ab1674) → [`00ab1678`](#insn-00ab1678)
- ブロック [`00ab1678`](#insn-00ab1678) 範囲 `[['00ab1678', '00ab167f']]`
  - `CONDITIONAL_JUMP` [`00ab167c`](#insn-00ab167c) → [`00ab1688`](#insn-00ab1688)
  - `FALL_THROUGH` [`00ab167c`](#insn-00ab167c) → [`00ab1680`](#insn-00ab1680)
- ブロック [`00ab1680`](#insn-00ab1680) 範囲 `[['00ab1680', '00ab1687']]`
  - `UNCONDITIONAL_JUMP` [`00ab1684`](#insn-00ab1684) → [`00ab16ec`](#insn-00ab16ec)
- ブロック [`00ab1688`](#insn-00ab1688) 範囲 `[['00ab1688', '00ab16af']]`
  - `CONDITIONAL_JUMP` [`00ab16ac`](#insn-00ab16ac) → [`00ab16b8`](#insn-00ab16b8)
  - `FALL_THROUGH` [`00ab16ac`](#insn-00ab16ac) → [`00ab16b0`](#insn-00ab16b0)
- ブロック [`00ab16b0`](#insn-00ab16b0) 範囲 `[['00ab16b0', '00ab16b7']]`
  - `UNCONDITIONAL_JUMP` [`00ab16b4`](#insn-00ab16b4) → [`00ab16e0`](#insn-00ab16e0)
- ブロック [`00ab16b8`](#insn-00ab16b8) 範囲 `[['00ab16b8', '00ab16c7']]`
  - `CONDITIONAL_JUMP` [`00ab16c4`](#insn-00ab16c4) → [`00ab16d0`](#insn-00ab16d0)
  - `FALL_THROUGH` [`00ab16c4`](#insn-00ab16c4) → [`00ab16c8`](#insn-00ab16c8)
- ブロック [`00ab16c8`](#insn-00ab16c8) 範囲 `[['00ab16c8', '00ab16cf']]`
  - `UNCONDITIONAL_JUMP` [`00ab16cc`](#insn-00ab16cc) → [`00ab16e0`](#insn-00ab16e0)
- ブロック [`00ab16d0`](#insn-00ab16d0) 範囲 `[['00ab16d0', '00ab16df']]`
  - `FALL_THROUGH` [`00ab16dc`](#insn-00ab16dc) → [`00ab16e0`](#insn-00ab16e0)
- ブロック [`00ab16e0`](#insn-00ab16e0) 範囲 `[['00ab16e0', '00ab16e7']]`
  - `CONDITIONAL_JUMP` [`00ab16e4`](#insn-00ab16e4) → [`00ab1730`](#insn-00ab1730)
  - `FALL_THROUGH` [`00ab16e4`](#insn-00ab16e4) → [`00ab16e8`](#insn-00ab16e8)
- ブロック [`00ab16e8`](#insn-00ab16e8) 範囲 `[['00ab16e8', '00ab16eb']]`
  - `FALL_THROUGH` [`00ab16e8`](#insn-00ab16e8) → [`00ab16ec`](#insn-00ab16ec)
- ブロック [`00ab16ec`](#insn-00ab16ec) 範囲 `[['00ab16ec', '00ab16fb']]`
  - `FALL_THROUGH` [`00ab16f8`](#insn-00ab16f8) → [`00ab16fc`](#insn-00ab16fc)
- ブロック [`00ab16fc`](#insn-00ab16fc) 範囲 `[['00ab16fc', '00ab172f']]`
- ブロック [`00ab1730`](#insn-00ab1730) 範囲 `[['00ab1730', '00ab1737']]`
  - `UNCONDITIONAL_JUMP` [`00ab1734`](#insn-00ab1734) → [`00ab16fc`](#insn-00ab16fc)

## 命令位置別の参照

- [`00ab0ddc`](#insn-00ab0ddc) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0de0`](#insn-00ab0de0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0de4`](#insn-00ab0de4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0de8`](#insn-00ab0de8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0dec`](#insn-00ab0dec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0df0`](#insn-00ab0df0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e0c`](#insn-00ab0e0c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e1c`](#insn-00ab0e1c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e24`](#insn-00ab0e24) → [`0085bb70`](../0085b/0085bb70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085bb70` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e28`](#insn-00ab0e28) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e38`](#insn-00ab0e38) → `00333f54`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab0e3c`](#insn-00ab0e3c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e48`](#insn-00ab0e48) → `00332a25`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab0e4c`](#insn-00ab0e4c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e58`](#insn-00ab0e58) → `0039bae0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[23]`
- [`00ab0e60`](#insn-00ab0e60) → [`008001dc`](../00800/008001dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008001dc` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e68`](#insn-00ab0e68) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e78`](#insn-00ab0e78) → `0038f284`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0038f284` · 推定型 `dword`
- [`00ab0e7c`](#insn-00ab0e7c) → [`00ab0ebc`](#insn-00ab0ebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e84`](#insn-00ab0e84) → [`00ab0f6c`](#insn-00ab0f6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e8c`](#insn-00ab0e8c) → [`00ab0ef4`](#insn-00ab0ef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0e94`](#insn-00ab0e94) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ea0`](#insn-00ab0ea0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0eac`](#insn-00ab0eac) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab0eb0`](#insn-00ab0eb0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0eb8`](#insn-00ab0eb8) → [`00ab1068`](#insn-00ab1068) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ec0`](#insn-00ab0ec0) → [`00ab1040`](#insn-00ab1040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ec8`](#insn-00ab0ec8) → [`00ab0ef4`](#insn-00ab0ef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ecc`](#insn-00ab0ecc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ed8`](#insn-00ab0ed8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ee4`](#insn-00ab0ee4) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab0ee8`](#insn-00ab0ee8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ef0`](#insn-00ab0ef0) → [`00ab1068`](#insn-00ab1068) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ef4`](#insn-00ab0ef4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f04`](#insn-00ab0f04) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f10`](#insn-00ab0f10) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab0f14`](#insn-00ab0f14) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f20`](#insn-00ab0f20) → `00344440`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0f24`](#insn-00ab0f24) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f30`](#insn-00ab0f30) → `0039badc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00ab0f34`](#insn-00ab0f34) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f48`](#insn-00ab0f48) → [`009d8834`](../009d8/009d8834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009d8834` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f50`](#insn-00ab0f50) → [`00ab1078`](#insn-00ab1078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f54`](#insn-00ab0f54) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f60`](#insn-00ab0f60) → [`0074423c`](../00744/0074423c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0074423c` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f68`](#insn-00ab0f68) → [`00ab10b4`](#insn-00ab10b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f6c`](#insn-00ab0f6c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f7c`](#insn-00ab0f7c) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab0f80`](#insn-00ab0f80) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f8c`](#insn-00ab0f8c) → [`0074423c`](../00744/0074423c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0074423c` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f90`](#insn-00ab0f90) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0f9c`](#insn-00ab0f9c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0fa8`](#insn-00ab0fa8) → `00344440`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0fac`](#insn-00ab0fac) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0fb8`](#insn-00ab0fb8) → `0039badc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00ab0fbc`](#insn-00ab0fbc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0fc8`](#insn-00ab0fc8) → `0038f284`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `fde_0038f284` · 推定型 `dword`
- [`00ab0fcc`](#insn-00ab0fcc) → [`008001cc`](../00800/008001cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008001cc` · 推定シンボル `None` · 推定型 `None`
- [`00ab0fd4`](#insn-00ab0fd4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0fd8`](#insn-00ab0fd8) → `00344440`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab0fdc`](#insn-00ab0fdc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab0fe0`](#insn-00ab0fe0) → `0039badc`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00ab0ff0`](#insn-00ab0ff0) → [`00806af4`](../00806/00806af4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00806af4` · 推定シンボル `None` · 推定型 `None`
- [`00ab0ff8`](#insn-00ab0ff8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1004`](#insn-00ab1004) → `00331680`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab1008`](#insn-00ab1008) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1014`](#insn-00ab1014) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1028`](#insn-00ab1028) → [`009d8834`](../009d8/009d8834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009d8834` · 推定シンボル `None` · 推定型 `None`
- [`00ab102c`](#insn-00ab102c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1038`](#insn-00ab1038) → `00333f64`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab103c`](#insn-00ab103c) → [`00ab1078`](#insn-00ab1078) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1044`](#insn-00ab1044) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1050`](#insn-00ab1050) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab105c`](#insn-00ab105c) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab1060`](#insn-00ab1060) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1074`](#insn-00ab1074) → [`009d8834`](../009d8/009d8834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009d8834` · 推定シンボル `None` · 推定型 `None`
- [`00ab1078`](#insn-00ab1078) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1084`](#insn-00ab1084) → [`0074423c`](../00744/0074423c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0074423c` · 推定シンボル `None` · 推定型 `None`
- [`00ab1098`](#insn-00ab1098) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab10a4`](#insn-00ab10a4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab10ac`](#insn-00ab10ac) → [`00ab10c0`](#insn-00ab10c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab10b4`](#insn-00ab10b4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab10c0`](#insn-00ab10c0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab10d0`](#insn-00ab10d0) → [`00ab10e8`](#insn-00ab10e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab10d4`](#insn-00ab10d4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab10e4`](#insn-00ab10e4) → [`00ab10fc`](#insn-00ab10fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab10e8`](#insn-00ab10e8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab10f8`](#insn-00ab10f8) → `00344448`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00ab10fc`](#insn-00ab10fc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1108`](#insn-00ab1108) → `00331690`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab110c`](#insn-00ab110c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1118`](#insn-00ab1118) → `00331680`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab111c`](#insn-00ab111c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1128`](#insn-00ab1128) → `00393ca8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00ab112c`](#insn-00ab112c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab113c`](#insn-00ab113c) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab1140`](#insn-00ab1140) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1148`](#insn-00ab1148) → [`00ab11a8`](#insn-00ab11a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1154`](#insn-00ab1154) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab1158`](#insn-00ab1158) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1160`](#insn-00ab1160) → [`00ab116c`](#insn-00ab116c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1168`](#insn-00ab1168) → [`00ab11a8`](#insn-00ab11a8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1174`](#insn-00ab1174) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab1178`](#insn-00ab1178) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1180`](#insn-00ab1180) → [`00ab118c`](#insn-00ab118c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1188`](#insn-00ab1188) → [`00ab11a8`](#insn-00ab11a8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1194`](#insn-00ab1194) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab119c`](#insn-00ab119c) → [`00ab11b4`](#insn-00ab11b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab11a4`](#insn-00ab11a4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab11b0`](#insn-00ab11b0) → `003c7c70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab11b4`](#insn-00ab11b4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab11c0`](#insn-00ab11c0) → `003c7c70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab11c4`](#insn-00ab11c4) → [`00ab11e0`](#insn-00ab11e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab11c8`](#insn-00ab11c8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab11d4`](#insn-00ab11d4) → `003c7c70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab11dc`](#insn-00ab11dc) → [`00ab1458`](#insn-00ab1458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab11e4`](#insn-00ab11e4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab11f0`](#insn-00ab11f0) → `003c7c6c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `dword`
- [`00ab11f4`](#insn-00ab11f4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1208`](#insn-00ab1208) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1214`](#insn-00ab1214) → `00344448`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00ab1218`](#insn-00ab1218) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab121c`](#insn-00ab121c) → [`0085cefc`](../0085c/0085cefc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085cefc` · 推定シンボル `None` · 推定型 `None`
- [`00ab1220`](#insn-00ab1220) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1228`](#insn-00ab1228) → [`00ab1414`](#insn-00ab1414) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1234`](#insn-00ab1234) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab123c`](#insn-00ab123c) → [`00ab1414`](#insn-00ab1414) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1244`](#insn-00ab1244) → [`00ab1258`](#insn-00ab1258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1248`](#insn-00ab1248) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1258`](#insn-00ab1258) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab125c`](#insn-00ab125c) → [`0085d4f4`](../0085d/0085d4f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085d4f4` · 推定シンボル `None` · 推定型 `None`
- [`00ab1264`](#insn-00ab1264) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1274`](#insn-00ab1274) → `0034733c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[27]`
- [`00ab1280`](#insn-00ab1280) → [`00ab1290`](#insn-00ab1290) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab128c`](#insn-00ab128c) → [`00ab12cc`](#insn-00ab12cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1290`](#insn-00ab1290) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1294`](#insn-00ab1294) → `0038e8c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[99]`
- [`00ab1298`](#insn-00ab1298) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab12a4`](#insn-00ab12a4) → `0038e0f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[31]`
- [`00ab12ac`](#insn-00ab12ac) → [`00ab1284`](#insn-00ab1284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab12b0`](#insn-00ab12b0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab12bc`](#insn-00ab12bc) → `0038e0f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[31]`
- [`00ab12c0`](#insn-00ab12c0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab12c4`](#insn-00ab12c4) → `0038e8c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[99]`
- [`00ab12c8`](#insn-00ab12c8) → [`00ab1284`](#insn-00ab1284) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab12cc`](#insn-00ab12cc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab12d8`](#insn-00ab12d8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab12e8`](#insn-00ab12e8) → `00344448`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `uleb128`
- [`00ab12ec`](#insn-00ab12ec) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab12f8`](#insn-00ab12f8) → `0034733c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[27]`
- [`00ab1300`](#insn-00ab1300) → [`00ab13a8`](#insn-00ab13a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1328`](#insn-00ab1328) → [`00ab1348`](#insn-00ab1348) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1330`](#insn-00ab1330) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1334`](#insn-00ab1334) → `0034733c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[27]`
- [`00ab1344`](#insn-00ab1344) → [`00ab13a8`](#insn-00ab13a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1348`](#insn-00ab1348) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1350`](#insn-00ab1350) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1354`](#insn-00ab1354) → `0034733c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[27]`
- [`00ab1368`](#insn-00ab1368) → `0038e0f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[31]`
- [`00ab136c`](#insn-00ab136c) → [`008001ec`](../00800/008001ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008001ec` · 推定シンボル `None` · 推定型 `None`
- [`00ab1374`](#insn-00ab1374) → [`00ab132c`](#insn-00ab132c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab137c`](#insn-00ab137c) → [`00728e48`](../00728/00728e48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00728e48` · 推定シンボル `None` · 推定型 `None`
- [`00ab1384`](#insn-00ab1384) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1388`](#insn-00ab1388) → [`0046ca84`](../0046c/0046ca84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046ca84` · 推定シンボル `None` · 推定型 `None`
- [`00ab139c`](#insn-00ab139c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab13a0`](#insn-00ab13a0) → `0034444c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[43]`
- [`00ab13a4`](#insn-00ab13a4) → [`00ab132c`](#insn-00ab132c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab13a8`](#insn-00ab13a8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab13b4`](#insn-00ab13b4) → `0034444c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[43]`
- [`00ab13b8`](#insn-00ab13b8) → [`00728d08`](../00728/00728d08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00728d08` · 推定シンボル `None` · 推定型 `None`
- [`00ab13cc`](#insn-00ab13cc) → [`00ab13e8`](#insn-00ab13e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab13d0`](#insn-00ab13d0) → [`00728d08`](../00728/00728d08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00728d08` · 推定シンボル `None` · 推定型 `None`
- [`00ab13d8`](#insn-00ab13d8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab13e4`](#insn-00ab13e4) → `0034444c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[43]`
- [`00ab13e8`](#insn-00ab13e8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab13f4`](#insn-00ab13f4) → `0034444c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[43]`
- [`00ab13fc`](#insn-00ab13fc) → [`00ab1414`](#insn-00ab1414) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1400`](#insn-00ab1400) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1410`](#insn-00ab1410) → `0034444c`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `byte[43]`
- [`00ab1418`](#insn-00ab1418) → [`00ab16fc`](#insn-00ab16fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab141c`](#insn-00ab141c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1420`](#insn-00ab1420) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab142c`](#insn-00ab142c) → `0033f8e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab1430`](#insn-00ab1430) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1440`](#insn-00ab1440) → [`00ab147c`](#insn-00ab147c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab144c`](#insn-00ab144c) → [`00ab14d0`](#insn-00ab14d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1454`](#insn-00ab1454) → [`00ab16ec`](#insn-00ab16ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1458`](#insn-00ab1458) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1464`](#insn-00ab1464) → `003c7c70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab1468`](#insn-00ab1468) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1470`](#insn-00ab1470) → [`00ab149c`](#insn-00ab149c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1478`](#insn-00ab1478) → [`00ab11e8`](#insn-00ab11e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab147c`](#insn-00ab147c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1484`](#insn-00ab1484) → [`00744208`](../00744/00744208.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744208` · 推定シンボル `None` · 推定型 `None`
- [`00ab1488`](#insn-00ab1488) → [`00ab14b8`](#insn-00ab14b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1494`](#insn-00ab1494) → [`00ab1450`](#insn-00ab1450) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1498`](#insn-00ab1498) → [`00ab14d0`](#insn-00ab14d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab14a4`](#insn-00ab14a4) → `003c7c70`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `qword`
- [`00ab14ac`](#insn-00ab14ac) → [`00ab11f4`](#insn-00ab11f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab14b4`](#insn-00ab14b4) → [`00ab11e4`](#insn-00ab11e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab14b8`](#insn-00ab14b8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab14c4`](#insn-00ab14c4) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab14cc`](#insn-00ab14cc) → [`00ab1450`](#insn-00ab1450) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab14d0`](#insn-00ab14d0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab14d4`](#insn-00ab14d4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab14e0`](#insn-00ab14e0) → `0033f8e4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab14e4`](#insn-00ab14e4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab14f4`](#insn-00ab14f4) → [`00ab150c`](#insn-00ab150c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1500`](#insn-00ab1500) → [`00ab1544`](#insn-00ab1544) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1508`](#insn-00ab1508) → [`00ab16ec`](#insn-00ab16ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab150c`](#insn-00ab150c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1514`](#insn-00ab1514) → [`00744208`](../00744/00744208.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744208` · 推定シンボル `None` · 推定型 `None`
- [`00ab1518`](#insn-00ab1518) → [`00ab152c`](#insn-00ab152c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1524`](#insn-00ab1524) → [`00ab1504`](#insn-00ab1504) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1528`](#insn-00ab1528) → [`00ab1544`](#insn-00ab1544) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab152c`](#insn-00ab152c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1538`](#insn-00ab1538) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab1540`](#insn-00ab1540) → [`00ab1504`](#insn-00ab1504) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1544`](#insn-00ab1544) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1548`](#insn-00ab1548) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1554`](#insn-00ab1554) → `0033f8e8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab1558`](#insn-00ab1558) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1568`](#insn-00ab1568) → [`00ab1580`](#insn-00ab1580) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1574`](#insn-00ab1574) → [`00ab15b8`](#insn-00ab15b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab157c`](#insn-00ab157c) → [`00ab16ec`](#insn-00ab16ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1580`](#insn-00ab1580) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1588`](#insn-00ab1588) → [`00744208`](../00744/00744208.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744208` · 推定シンボル `None` · 推定型 `None`
- [`00ab158c`](#insn-00ab158c) → [`00ab15a0`](#insn-00ab15a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1598`](#insn-00ab1598) → [`00ab1578`](#insn-00ab1578) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab159c`](#insn-00ab159c) → [`00ab15b8`](#insn-00ab15b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab15a0`](#insn-00ab15a0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab15ac`](#insn-00ab15ac) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab15b4`](#insn-00ab15b4) → [`00ab1578`](#insn-00ab1578) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab15b8`](#insn-00ab15b8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab15bc`](#insn-00ab15bc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab15c8`](#insn-00ab15c8) → `0033f8ec`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab15cc`](#insn-00ab15cc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab15dc`](#insn-00ab15dc) → [`00ab15e8`](#insn-00ab15e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab15e4`](#insn-00ab15e4) → [`00ab1610`](#insn-00ab1610) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab15e8`](#insn-00ab15e8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab15f0`](#insn-00ab15f0) → [`00744208`](../00744/00744208.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744208` · 推定シンボル `None` · 推定型 `None`
- [`00ab15f4`](#insn-00ab15f4) → [`00ab1600`](#insn-00ab1600) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab15fc`](#insn-00ab15fc) → [`00ab1610`](#insn-00ab1610) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1600`](#insn-00ab1600) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab160c`](#insn-00ab160c) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab1614`](#insn-00ab1614) → [`00ab1620`](#insn-00ab1620) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab161c`](#insn-00ab161c) → [`00ab16ec`](#insn-00ab16ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1620`](#insn-00ab1620) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1624`](#insn-00ab1624) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1630`](#insn-00ab1630) → `0033f8f0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab1634`](#insn-00ab1634) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1644`](#insn-00ab1644) → [`00ab1650`](#insn-00ab1650) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab164c`](#insn-00ab164c) → [`00ab1678`](#insn-00ab1678) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1650`](#insn-00ab1650) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1658`](#insn-00ab1658) → [`00744208`](../00744/00744208.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744208` · 推定シンボル `None` · 推定型 `None`
- [`00ab165c`](#insn-00ab165c) → [`00ab1668`](#insn-00ab1668) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1664`](#insn-00ab1664) → [`00ab1678`](#insn-00ab1678) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1668`](#insn-00ab1668) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1674`](#insn-00ab1674) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab167c`](#insn-00ab167c) → [`00ab1688`](#insn-00ab1688) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1684`](#insn-00ab1684) → [`00ab16ec`](#insn-00ab16ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1688`](#insn-00ab1688) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab168c`](#insn-00ab168c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1698`](#insn-00ab1698) → `0033f8f4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab169c`](#insn-00ab169c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab16ac`](#insn-00ab16ac) → [`00ab16b8`](#insn-00ab16b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab16b4`](#insn-00ab16b4) → [`00ab16e0`](#insn-00ab16e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab16b8`](#insn-00ab16b8) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab16c0`](#insn-00ab16c0) → [`00744208`](../00744/00744208.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744208` · 推定シンボル `None` · 推定型 `None`
- [`00ab16c4`](#insn-00ab16c4) → [`00ab16d0`](#insn-00ab16d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab16cc`](#insn-00ab16cc) → [`00ab16e0`](#insn-00ab16e0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab16d0`](#insn-00ab16d0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab16dc`](#insn-00ab16dc) → `00333974`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab16e4`](#insn-00ab16e4) → [`00ab1730`](#insn-00ab1730) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab16ec`](#insn-00ab16ec) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab16f8`](#insn-00ab16f8) → `00333f64`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `fde_table_entry`
- [`00ab16fc`](#insn-00ab16fc) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1700`](#insn-00ab1700) → [`0085ccf0`](../0085c/0085ccf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0085ccf0` · 推定シンボル `None` · 推定型 `None`
- [`00ab1704`](#insn-00ab1704) → [`0047acf4`](../0047a/0047acf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047acf4` · 推定シンボル `None` · 推定型 `None`
- [`00ab170c`](#insn-00ab170c) → [`0047ca8c`](../0047c/0047ca8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047ca8c` · 推定シンボル `None` · 推定型 `None`
- [`00ab1714`](#insn-00ab1714) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1718`](#insn-00ab1718) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab171c`](#insn-00ab171c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1720`](#insn-00ab1720) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1724`](#insn-00ab1724) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab1728`](#insn-00ab1728) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ab172c`](#insn-00ab172c) → [`0072bf4c`](../0072b/0072bf4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0072bf4c` · 推定シンボル `None` · 推定型 `None`
- [`00ab1730`](#insn-00ab1730) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00ab1734`](#insn-00ab1734) → [`00ab16fc`](#insn-00ab16fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ab0ddc`](#insn-00ab0ddc)

~~~json
{
  "source": "00ab0ddc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0de0`](#insn-00ab0de0)

~~~json
{
  "source": "00ab0de0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0de4`](#insn-00ab0de4)

~~~json
{
  "source": "00ab0de4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0de8`](#insn-00ab0de8)

~~~json
{
  "source": "00ab0de8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0dec`](#insn-00ab0dec)

~~~json
{
  "source": "00ab0dec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0df0`](#insn-00ab0df0)

~~~json
{
  "source": "00ab0df0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0e0c`](#insn-00ab0e0c)

~~~json
{
  "source": "00ab0e0c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0e1c`](#insn-00ab0e1c)

~~~json
{
  "source": "00ab0e1c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0e24`](#insn-00ab0e24)

~~~json
{
  "source": "00ab0e24",
  "target": "0085bb70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0e28`](#insn-00ab0e28)

~~~json
{
  "source": "00ab0e28",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0e38`](#insn-00ab0e38)

~~~json
{
  "source": "00ab0e38",
  "target": "00333f54",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f50",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "30a76c00008d0900",
  "capture_start": "00333f50",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0e3c`](#insn-00ab0e3c)

~~~json
{
  "source": "00ab0e3c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0e48`](#insn-00ab0e48)

~~~json
{
  "source": "00ab0e48",
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
- 参照命令 [`00ab0e4c`](#insn-00ab0e4c)

~~~json
{
  "source": "00ab0e4c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0e58`](#insn-00ab0e58)

~~~json
{
  "source": "00ab0e58",
  "target": "0039bae0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039badd",
  "offset": 3,
  "size": 23,
  "datatype": "byte[23]",
  "bytes": "580e20480c1d2093049e069d08580c1f20480e00d3dedd",
  "capture_start": "0039badd",
  "capture_bytes": 23,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0e60`](#insn-00ab0e60)

~~~json
{
  "source": "00ab0e60",
  "target": "008001dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0e68`](#insn-00ab0e68)

~~~json
{
  "source": "00ab0e68",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0e78`](#insn-00ab0e78)

~~~json
{
  "source": "00ab0e78",
  "target": "0038f284",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038f284",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0038f284",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0e7c`](#insn-00ab0e7c)

~~~json
{
  "source": "00ab0e7c",
  "target": "00ab0ebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0e84`](#insn-00ab0e84)

~~~json
{
  "source": "00ab0e84",
  "target": "00ab0f6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0e8c`](#insn-00ab0e8c)

~~~json
{
  "source": "00ab0e8c",
  "target": "00ab0ef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0e94`](#insn-00ab0e94)

~~~json
{
  "source": "00ab0e94",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0ea0`](#insn-00ab0ea0)

~~~json
{
  "source": "00ab0ea0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0eac`](#insn-00ab0eac)

~~~json
{
  "source": "00ab0eac",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0eb0`](#insn-00ab0eb0)

~~~json
{
  "source": "00ab0eb0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0eb8`](#insn-00ab0eb8)

~~~json
{
  "source": "00ab0eb8",
  "target": "00ab1068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0ec0`](#insn-00ab0ec0)

~~~json
{
  "source": "00ab0ec0",
  "target": "00ab1040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0ec8`](#insn-00ab0ec8)

~~~json
{
  "source": "00ab0ec8",
  "target": "00ab0ef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0ecc`](#insn-00ab0ecc)

~~~json
{
  "source": "00ab0ecc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0ed8`](#insn-00ab0ed8)

~~~json
{
  "source": "00ab0ed8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0ee4`](#insn-00ab0ee4)

~~~json
{
  "source": "00ab0ee4",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0ee8`](#insn-00ab0ee8)

~~~json
{
  "source": "00ab0ee8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0ef0`](#insn-00ab0ef0)

~~~json
{
  "source": "00ab0ef0",
  "target": "00ab1068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0ef4`](#insn-00ab0ef4)

~~~json
{
  "source": "00ab0ef4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f04`](#insn-00ab0f04)

~~~json
{
  "source": "00ab0f04",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f10`](#insn-00ab0f10)

~~~json
{
  "source": "00ab0f10",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0f14`](#insn-00ab0f14)

~~~json
{
  "source": "00ab0f14",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f20`](#insn-00ab0f20)

~~~json
{
  "source": "00ab0f20",
  "target": "00344440",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344440",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "80ec0f00",
  "capture_start": "00344440",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0f24`](#insn-00ab0f24)

~~~json
{
  "source": "00ab0f24",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f30`](#insn-00ab0f30)

~~~json
{
  "source": "00ab0f30",
  "target": "0039badc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039badc",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0039badc",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0f34`](#insn-00ab0f34)

~~~json
{
  "source": "00ab0f34",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f48`](#insn-00ab0f48)

~~~json
{
  "source": "00ab0f48",
  "target": "009d8834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f50`](#insn-00ab0f50)

~~~json
{
  "source": "00ab0f50",
  "target": "00ab1078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0f54`](#insn-00ab0f54)

~~~json
{
  "source": "00ab0f54",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f60`](#insn-00ab0f60)

~~~json
{
  "source": "00ab0f60",
  "target": "0074423c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f68`](#insn-00ab0f68)

~~~json
{
  "source": "00ab0f68",
  "target": "00ab10b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab0f6c`](#insn-00ab0f6c)

~~~json
{
  "source": "00ab0f6c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f7c`](#insn-00ab0f7c)

~~~json
{
  "source": "00ab0f7c",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0f80`](#insn-00ab0f80)

~~~json
{
  "source": "00ab0f80",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f8c`](#insn-00ab0f8c)

~~~json
{
  "source": "00ab0f8c",
  "target": "0074423c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f90`](#insn-00ab0f90)

~~~json
{
  "source": "00ab0f90",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0f9c`](#insn-00ab0f9c)

~~~json
{
  "source": "00ab0f9c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0fa8`](#insn-00ab0fa8)

~~~json
{
  "source": "00ab0fa8",
  "target": "00344440",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344440",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "80ec0f00",
  "capture_start": "00344440",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0fac`](#insn-00ab0fac)

~~~json
{
  "source": "00ab0fac",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0fb8`](#insn-00ab0fb8)

~~~json
{
  "source": "00ab0fb8",
  "target": "0039badc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039badc",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0039badc",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0fbc`](#insn-00ab0fbc)

~~~json
{
  "source": "00ab0fbc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0fc8`](#insn-00ab0fc8)

~~~json
{
  "source": "00ab0fc8",
  "target": "0038f284",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038f284",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "10000000",
  "capture_start": "0038f284",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0fcc`](#insn-00ab0fcc)

~~~json
{
  "source": "00ab0fcc",
  "target": "008001cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0fd4`](#insn-00ab0fd4)

~~~json
{
  "source": "00ab0fd4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0fd8`](#insn-00ab0fd8)

~~~json
{
  "source": "00ab0fd8",
  "target": "00344440",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344440",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "80ec0f00",
  "capture_start": "00344440",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0fdc`](#insn-00ab0fdc)

~~~json
{
  "source": "00ab0fdc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0fe0`](#insn-00ab0fe0)

~~~json
{
  "source": "00ab0fe0",
  "target": "0039badc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0039badc",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "0039badc",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab0ff0`](#insn-00ab0ff0)

~~~json
{
  "source": "00ab0ff0",
  "target": "00806af4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab0ff8`](#insn-00ab0ff8)

~~~json
{
  "source": "00ab0ff8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1004`](#insn-00ab1004)

~~~json
{
  "source": "00ab1004",
  "target": "00331680",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00331680",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "685c6100b0040900",
  "capture_start": "00331680",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1008`](#insn-00ab1008)

~~~json
{
  "source": "00ab1008",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1014`](#insn-00ab1014)

~~~json
{
  "source": "00ab1014",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1028`](#insn-00ab1028)

~~~json
{
  "source": "00ab1028",
  "target": "009d8834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab102c`](#insn-00ab102c)

~~~json
{
  "source": "00ab102c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1038`](#insn-00ab1038)

~~~json
{
  "source": "00ab1038",
  "target": "00333f64",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f60",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "04ab6c002c8d0900",
  "capture_start": "00333f60",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab103c`](#insn-00ab103c)

~~~json
{
  "source": "00ab103c",
  "target": "00ab1078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1044`](#insn-00ab1044)

~~~json
{
  "source": "00ab1044",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1050`](#insn-00ab1050)

~~~json
{
  "source": "00ab1050",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab105c`](#insn-00ab105c)

~~~json
{
  "source": "00ab105c",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1060`](#insn-00ab1060)

~~~json
{
  "source": "00ab1060",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1074`](#insn-00ab1074)

~~~json
{
  "source": "00ab1074",
  "target": "009d8834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1078`](#insn-00ab1078)

~~~json
{
  "source": "00ab1078",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1084`](#insn-00ab1084)

~~~json
{
  "source": "00ab1084",
  "target": "0074423c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1098`](#insn-00ab1098)

~~~json
{
  "source": "00ab1098",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab10a4`](#insn-00ab10a4)

~~~json
{
  "source": "00ab10a4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab10ac`](#insn-00ab10ac)

~~~json
{
  "source": "00ab10ac",
  "target": "00ab10c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab10b4`](#insn-00ab10b4)

~~~json
{
  "source": "00ab10b4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab10c0`](#insn-00ab10c0)

~~~json
{
  "source": "00ab10c0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab10d0`](#insn-00ab10d0)

~~~json
{
  "source": "00ab10d0",
  "target": "00ab10e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab10d4`](#insn-00ab10d4)

~~~json
{
  "source": "00ab10d4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab10e4`](#insn-00ab10e4)

~~~json
{
  "source": "00ab10e4",
  "target": "00ab10fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab10e8`](#insn-00ab10e8)

~~~json
{
  "source": "00ab10e8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab10f8`](#insn-00ab10f8)

~~~json
{
  "source": "00ab10f8",
  "target": "00344448",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344448",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "00344448",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab10fc`](#insn-00ab10fc)

~~~json
{
  "source": "00ab10fc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1108`](#insn-00ab1108)

~~~json
{
  "source": "00ab1108",
  "target": "00331690",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00331690",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "dc5c610000050900",
  "capture_start": "00331690",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab110c`](#insn-00ab110c)

~~~json
{
  "source": "00ab110c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1118`](#insn-00ab1118)

~~~json
{
  "source": "00ab1118",
  "target": "00331680",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00331680",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "685c6100b0040900",
  "capture_start": "00331680",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab111c`](#insn-00ab111c)

~~~json
{
  "source": "00ab111c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1128`](#insn-00ab1128)

~~~json
{
  "source": "00ab1128",
  "target": "00393ca8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00393ca8",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "00393ca8",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab112c`](#insn-00ab112c)

~~~json
{
  "source": "00ab112c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab113c`](#insn-00ab113c)

~~~json
{
  "source": "00ab113c",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1140`](#insn-00ab1140)

~~~json
{
  "source": "00ab1140",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1148`](#insn-00ab1148)

~~~json
{
  "source": "00ab1148",
  "target": "00ab11a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1154`](#insn-00ab1154)

~~~json
{
  "source": "00ab1154",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1158`](#insn-00ab1158)

~~~json
{
  "source": "00ab1158",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1160`](#insn-00ab1160)

~~~json
{
  "source": "00ab1160",
  "target": "00ab116c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1168`](#insn-00ab1168)

~~~json
{
  "source": "00ab1168",
  "target": "00ab11a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1174`](#insn-00ab1174)

~~~json
{
  "source": "00ab1174",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1178`](#insn-00ab1178)

~~~json
{
  "source": "00ab1178",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1180`](#insn-00ab1180)

~~~json
{
  "source": "00ab1180",
  "target": "00ab118c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1188`](#insn-00ab1188)

~~~json
{
  "source": "00ab1188",
  "target": "00ab11a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1194`](#insn-00ab1194)

~~~json
{
  "source": "00ab1194",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab119c`](#insn-00ab119c)

~~~json
{
  "source": "00ab119c",
  "target": "00ab11b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab11a4`](#insn-00ab11a4)

~~~json
{
  "source": "00ab11a4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab11b0`](#insn-00ab11b0)

~~~json
{
  "source": "00ab11b0",
  "target": "003c7c70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003c7c70",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0c00000000000000",
  "capture_start": "003c7c70",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab11b4`](#insn-00ab11b4)

~~~json
{
  "source": "00ab11b4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab11c0`](#insn-00ab11c0)

~~~json
{
  "source": "00ab11c0",
  "target": "003c7c70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003c7c70",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0c00000000000000",
  "capture_start": "003c7c70",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab11c4`](#insn-00ab11c4)

~~~json
{
  "source": "00ab11c4",
  "target": "00ab11e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab11c8`](#insn-00ab11c8)

~~~json
{
  "source": "00ab11c8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab11d4`](#insn-00ab11d4)

~~~json
{
  "source": "00ab11d4",
  "target": "003c7c70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003c7c70",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0c00000000000000",
  "capture_start": "003c7c70",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab11dc`](#insn-00ab11dc)

~~~json
{
  "source": "00ab11dc",
  "target": "00ab1458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab11e4`](#insn-00ab11e4)

~~~json
{
  "source": "00ab11e4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab11f0`](#insn-00ab11f0)

~~~json
{
  "source": "00ab11f0",
  "target": "003c7c6c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003c7c6c",
  "offset": 0,
  "size": 4,
  "datatype": "dword",
  "bytes": "e8e97700",
  "capture_start": "003c7c6c",
  "capture_bytes": 4,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab11f4`](#insn-00ab11f4)

~~~json
{
  "source": "00ab11f4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1208`](#insn-00ab1208)

~~~json
{
  "source": "00ab1208",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1214`](#insn-00ab1214)

~~~json
{
  "source": "00ab1214",
  "target": "00344448",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344448",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "00344448",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1218`](#insn-00ab1218)

~~~json
{
  "source": "00ab1218",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab121c`](#insn-00ab121c)

~~~json
{
  "source": "00ab121c",
  "target": "0085cefc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1220`](#insn-00ab1220)

~~~json
{
  "source": "00ab1220",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1228`](#insn-00ab1228)

~~~json
{
  "source": "00ab1228",
  "target": "00ab1414",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1234`](#insn-00ab1234)

~~~json
{
  "source": "00ab1234",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab123c`](#insn-00ab123c)

~~~json
{
  "source": "00ab123c",
  "target": "00ab1414",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1244`](#insn-00ab1244)

~~~json
{
  "source": "00ab1244",
  "target": "00ab1258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1248`](#insn-00ab1248)

~~~json
{
  "source": "00ab1248",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1258`](#insn-00ab1258)

~~~json
{
  "source": "00ab1258",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab125c`](#insn-00ab125c)

~~~json
{
  "source": "00ab125c",
  "target": "0085d4f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1264`](#insn-00ab1264)

~~~json
{
  "source": "00ab1264",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1274`](#insn-00ab1274)

~~~json
{
  "source": "00ab1274",
  "target": "0034733c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00347329",
  "offset": 19,
  "size": 27,
  "datatype": "byte[27]",
  "bytes": "440e304c0c1d2093049e069d080a7c0c1f304c0e00d3dedd440b00",
  "capture_start": "00347329",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1280`](#insn-00ab1280)

~~~json
{
  "source": "00ab1280",
  "target": "00ab1290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab128c`](#insn-00ab128c)

~~~json
{
  "source": "00ab128c",
  "target": "00ab12cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1290`](#insn-00ab1290)

~~~json
{
  "source": "00ab1290",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1294`](#insn-00ab1294)

~~~json
{
  "source": "00ab1294",
  "target": "0038e8c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038e879",
  "offset": 71,
  "size": 99,
  "datatype": "byte[99]",
  "bytes": "440e40500c1d409302940495069608970a980c9e0e9d100a02ac0c1f40500e00",
  "capture_start": "0038e879",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab1298`](#insn-00ab1298)

~~~json
{
  "source": "00ab1298",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab12a4`](#insn-00ab12a4)

~~~json
{
  "source": "00ab12a4",
  "target": "0038e0f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038e0ed",
  "offset": 3,
  "size": 31,
  "datatype": "byte[31]",
  "bytes": "440e20480c1d20930294049e069d080390020c1f20480e00d3d4dedd000000",
  "capture_start": "0038e0ed",
  "capture_bytes": 31,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab12ac`](#insn-00ab12ac)

~~~json
{
  "source": "00ab12ac",
  "target": "00ab1284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab12b0`](#insn-00ab12b0)

~~~json
{
  "source": "00ab12b0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab12bc`](#insn-00ab12bc)

~~~json
{
  "source": "00ab12bc",
  "target": "0038e0f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038e0ed",
  "offset": 3,
  "size": 31,
  "datatype": "byte[31]",
  "bytes": "440e20480c1d20930294049e069d080390020c1f20480e00d3d4dedd000000",
  "capture_start": "0038e0ed",
  "capture_bytes": 31,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab12c0`](#insn-00ab12c0)

~~~json
{
  "source": "00ab12c0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab12c4`](#insn-00ab12c4)

~~~json
{
  "source": "00ab12c4",
  "target": "0038e8c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038e879",
  "offset": 71,
  "size": 99,
  "datatype": "byte[99]",
  "bytes": "440e40500c1d409302940495069608970a980c9e0e9d100a02ac0c1f40500e00",
  "capture_start": "0038e879",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab12c8`](#insn-00ab12c8)

~~~json
{
  "source": "00ab12c8",
  "target": "00ab1284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab12cc`](#insn-00ab12cc)

~~~json
{
  "source": "00ab12cc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab12d8`](#insn-00ab12d8)

~~~json
{
  "source": "00ab12d8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab12e8`](#insn-00ab12e8)

~~~json
{
  "source": "00ab12e8",
  "target": "00344448",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344448",
  "offset": 0,
  "size": 1,
  "datatype": "uleb128",
  "bytes": "00",
  "capture_start": "00344448",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab12ec`](#insn-00ab12ec)

~~~json
{
  "source": "00ab12ec",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab12f8`](#insn-00ab12f8)

~~~json
{
  "source": "00ab12f8",
  "target": "0034733c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00347329",
  "offset": 19,
  "size": 27,
  "datatype": "byte[27]",
  "bytes": "440e304c0c1d2093049e069d080a7c0c1f304c0e00d3dedd440b00",
  "capture_start": "00347329",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1300`](#insn-00ab1300)

~~~json
{
  "source": "00ab1300",
  "target": "00ab13a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1328`](#insn-00ab1328)

~~~json
{
  "source": "00ab1328",
  "target": "00ab1348",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1330`](#insn-00ab1330)

~~~json
{
  "source": "00ab1330",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1334`](#insn-00ab1334)

~~~json
{
  "source": "00ab1334",
  "target": "0034733c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00347329",
  "offset": 19,
  "size": 27,
  "datatype": "byte[27]",
  "bytes": "440e304c0c1d2093049e069d080a7c0c1f304c0e00d3dedd440b00",
  "capture_start": "00347329",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1344`](#insn-00ab1344)

~~~json
{
  "source": "00ab1344",
  "target": "00ab13a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1348`](#insn-00ab1348)

~~~json
{
  "source": "00ab1348",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1350`](#insn-00ab1350)

~~~json
{
  "source": "00ab1350",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1354`](#insn-00ab1354)

~~~json
{
  "source": "00ab1354",
  "target": "0034733c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00347329",
  "offset": 19,
  "size": 27,
  "datatype": "byte[27]",
  "bytes": "440e304c0c1d2093049e069d080a7c0c1f304c0e00d3dedd440b00",
  "capture_start": "00347329",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1368`](#insn-00ab1368)

~~~json
{
  "source": "00ab1368",
  "target": "0038e0f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0038e0ed",
  "offset": 3,
  "size": 31,
  "datatype": "byte[31]",
  "bytes": "440e20480c1d20930294049e069d080390020c1f20480e00d3d4dedd000000",
  "capture_start": "0038e0ed",
  "capture_bytes": 31,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab136c`](#insn-00ab136c)

~~~json
{
  "source": "00ab136c",
  "target": "008001ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1374`](#insn-00ab1374)

~~~json
{
  "source": "00ab1374",
  "target": "00ab132c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab137c`](#insn-00ab137c)

~~~json
{
  "source": "00ab137c",
  "target": "00728e48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1384`](#insn-00ab1384)

~~~json
{
  "source": "00ab1384",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1388`](#insn-00ab1388)

~~~json
{
  "source": "00ab1388",
  "target": "0046ca84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab139c`](#insn-00ab139c)

~~~json
{
  "source": "00ab139c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab13a0`](#insn-00ab13a0)

~~~json
{
  "source": "00ab13a0",
  "target": "0034444c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344449",
  "offset": 3,
  "size": 43,
  "datatype": "byte[43]",
  "bytes": "440e20480c1d20930294049e069d080a02540c1f20480e00d3d4dedd440b440c",
  "capture_start": "00344449",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab13a4`](#insn-00ab13a4)

~~~json
{
  "source": "00ab13a4",
  "target": "00ab132c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab13a8`](#insn-00ab13a8)

~~~json
{
  "source": "00ab13a8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab13b4`](#insn-00ab13b4)

~~~json
{
  "source": "00ab13b4",
  "target": "0034444c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344449",
  "offset": 3,
  "size": 43,
  "datatype": "byte[43]",
  "bytes": "440e20480c1d20930294049e069d080a02540c1f20480e00d3d4dedd440b440c",
  "capture_start": "00344449",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab13b8`](#insn-00ab13b8)

~~~json
{
  "source": "00ab13b8",
  "target": "00728d08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab13cc`](#insn-00ab13cc)

~~~json
{
  "source": "00ab13cc",
  "target": "00ab13e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab13d0`](#insn-00ab13d0)

~~~json
{
  "source": "00ab13d0",
  "target": "00728d08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab13d8`](#insn-00ab13d8)

~~~json
{
  "source": "00ab13d8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab13e4`](#insn-00ab13e4)

~~~json
{
  "source": "00ab13e4",
  "target": "0034444c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344449",
  "offset": 3,
  "size": 43,
  "datatype": "byte[43]",
  "bytes": "440e20480c1d20930294049e069d080a02540c1f20480e00d3d4dedd440b440c",
  "capture_start": "00344449",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab13e8`](#insn-00ab13e8)

~~~json
{
  "source": "00ab13e8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab13f4`](#insn-00ab13f4)

~~~json
{
  "source": "00ab13f4",
  "target": "0034444c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344449",
  "offset": 3,
  "size": 43,
  "datatype": "byte[43]",
  "bytes": "440e20480c1d20930294049e069d080a02540c1f20480e00d3d4dedd440b440c",
  "capture_start": "00344449",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab13fc`](#insn-00ab13fc)

~~~json
{
  "source": "00ab13fc",
  "target": "00ab1414",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1400`](#insn-00ab1400)

~~~json
{
  "source": "00ab1400",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1410`](#insn-00ab1410)

~~~json
{
  "source": "00ab1410",
  "target": "0034444c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00344449",
  "offset": 3,
  "size": 43,
  "datatype": "byte[43]",
  "bytes": "440e20480c1d20930294049e069d080a02540c1f20480e00d3d4dedd440b440c",
  "capture_start": "00344449",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00ab1418`](#insn-00ab1418)

~~~json
{
  "source": "00ab1418",
  "target": "00ab16fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab141c`](#insn-00ab141c)

~~~json
{
  "source": "00ab141c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1420`](#insn-00ab1420)

~~~json
{
  "source": "00ab1420",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab142c`](#insn-00ab142c)

~~~json
{
  "source": "00ab142c",
  "target": "0033f8e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033f8e0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "24e18c009c470c00",
  "capture_start": "0033f8e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1430`](#insn-00ab1430)

~~~json
{
  "source": "00ab1430",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1440`](#insn-00ab1440)

~~~json
{
  "source": "00ab1440",
  "target": "00ab147c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab144c`](#insn-00ab144c)

~~~json
{
  "source": "00ab144c",
  "target": "00ab14d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1454`](#insn-00ab1454)

~~~json
{
  "source": "00ab1454",
  "target": "00ab16ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1458`](#insn-00ab1458)

~~~json
{
  "source": "00ab1458",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1464`](#insn-00ab1464)

~~~json
{
  "source": "00ab1464",
  "target": "003c7c70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003c7c70",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0c00000000000000",
  "capture_start": "003c7c70",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1468`](#insn-00ab1468)

~~~json
{
  "source": "00ab1468",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1470`](#insn-00ab1470)

~~~json
{
  "source": "00ab1470",
  "target": "00ab149c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1478`](#insn-00ab1478)

~~~json
{
  "source": "00ab1478",
  "target": "00ab11e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab147c`](#insn-00ab147c)

~~~json
{
  "source": "00ab147c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1484`](#insn-00ab1484)

~~~json
{
  "source": "00ab1484",
  "target": "00744208",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1488`](#insn-00ab1488)

~~~json
{
  "source": "00ab1488",
  "target": "00ab14b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1494`](#insn-00ab1494)

~~~json
{
  "source": "00ab1494",
  "target": "00ab1450",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1498`](#insn-00ab1498)

~~~json
{
  "source": "00ab1498",
  "target": "00ab14d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab14a4`](#insn-00ab14a4)

~~~json
{
  "source": "00ab14a4",
  "target": "003c7c70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "003c7c70",
  "offset": 0,
  "size": 8,
  "datatype": "qword",
  "bytes": "0c00000000000000",
  "capture_start": "003c7c70",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab14ac`](#insn-00ab14ac)

~~~json
{
  "source": "00ab14ac",
  "target": "00ab11f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab14b4`](#insn-00ab14b4)

~~~json
{
  "source": "00ab14b4",
  "target": "00ab11e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab14b8`](#insn-00ab14b8)

~~~json
{
  "source": "00ab14b8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab14c4`](#insn-00ab14c4)

~~~json
{
  "source": "00ab14c4",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab14cc`](#insn-00ab14cc)

~~~json
{
  "source": "00ab14cc",
  "target": "00ab1450",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab14d0`](#insn-00ab14d0)

~~~json
{
  "source": "00ab14d0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab14d4`](#insn-00ab14d4)

~~~json
{
  "source": "00ab14d4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab14e0`](#insn-00ab14e0)

~~~json
{
  "source": "00ab14e0",
  "target": "0033f8e4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033f8e0",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "24e18c009c470c00",
  "capture_start": "0033f8e0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab14e4`](#insn-00ab14e4)

~~~json
{
  "source": "00ab14e4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab14f4`](#insn-00ab14f4)

~~~json
{
  "source": "00ab14f4",
  "target": "00ab150c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1500`](#insn-00ab1500)

~~~json
{
  "source": "00ab1500",
  "target": "00ab1544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1508`](#insn-00ab1508)

~~~json
{
  "source": "00ab1508",
  "target": "00ab16ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab150c`](#insn-00ab150c)

~~~json
{
  "source": "00ab150c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1514`](#insn-00ab1514)

~~~json
{
  "source": "00ab1514",
  "target": "00744208",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1518`](#insn-00ab1518)

~~~json
{
  "source": "00ab1518",
  "target": "00ab152c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1524`](#insn-00ab1524)

~~~json
{
  "source": "00ab1524",
  "target": "00ab1504",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1528`](#insn-00ab1528)

~~~json
{
  "source": "00ab1528",
  "target": "00ab1544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab152c`](#insn-00ab152c)

~~~json
{
  "source": "00ab152c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1538`](#insn-00ab1538)

~~~json
{
  "source": "00ab1538",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1540`](#insn-00ab1540)

~~~json
{
  "source": "00ab1540",
  "target": "00ab1504",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1544`](#insn-00ab1544)

~~~json
{
  "source": "00ab1544",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1548`](#insn-00ab1548)

~~~json
{
  "source": "00ab1548",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1554`](#insn-00ab1554)

~~~json
{
  "source": "00ab1554",
  "target": "0033f8e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033f8e8",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "30e18c00b0470c00",
  "capture_start": "0033f8e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1558`](#insn-00ab1558)

~~~json
{
  "source": "00ab1558",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1568`](#insn-00ab1568)

~~~json
{
  "source": "00ab1568",
  "target": "00ab1580",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1574`](#insn-00ab1574)

~~~json
{
  "source": "00ab1574",
  "target": "00ab15b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab157c`](#insn-00ab157c)

~~~json
{
  "source": "00ab157c",
  "target": "00ab16ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1580`](#insn-00ab1580)

~~~json
{
  "source": "00ab1580",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1588`](#insn-00ab1588)

~~~json
{
  "source": "00ab1588",
  "target": "00744208",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab158c`](#insn-00ab158c)

~~~json
{
  "source": "00ab158c",
  "target": "00ab15a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1598`](#insn-00ab1598)

~~~json
{
  "source": "00ab1598",
  "target": "00ab1578",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab159c`](#insn-00ab159c)

~~~json
{
  "source": "00ab159c",
  "target": "00ab15b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab15a0`](#insn-00ab15a0)

~~~json
{
  "source": "00ab15a0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab15ac`](#insn-00ab15ac)

~~~json
{
  "source": "00ab15ac",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab15b4`](#insn-00ab15b4)

~~~json
{
  "source": "00ab15b4",
  "target": "00ab1578",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab15b8`](#insn-00ab15b8)

~~~json
{
  "source": "00ab15b8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab15bc`](#insn-00ab15bc)

~~~json
{
  "source": "00ab15bc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab15c8`](#insn-00ab15c8)

~~~json
{
  "source": "00ab15c8",
  "target": "0033f8ec",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033f8e8",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "30e18c00b0470c00",
  "capture_start": "0033f8e8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab15cc`](#insn-00ab15cc)

~~~json
{
  "source": "00ab15cc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab15dc`](#insn-00ab15dc)

~~~json
{
  "source": "00ab15dc",
  "target": "00ab15e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab15e4`](#insn-00ab15e4)

~~~json
{
  "source": "00ab15e4",
  "target": "00ab1610",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab15e8`](#insn-00ab15e8)

~~~json
{
  "source": "00ab15e8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab15f0`](#insn-00ab15f0)

~~~json
{
  "source": "00ab15f0",
  "target": "00744208",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab15f4`](#insn-00ab15f4)

~~~json
{
  "source": "00ab15f4",
  "target": "00ab1600",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab15fc`](#insn-00ab15fc)

~~~json
{
  "source": "00ab15fc",
  "target": "00ab1610",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1600`](#insn-00ab1600)

~~~json
{
  "source": "00ab1600",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab160c`](#insn-00ab160c)

~~~json
{
  "source": "00ab160c",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1614`](#insn-00ab1614)

~~~json
{
  "source": "00ab1614",
  "target": "00ab1620",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab161c`](#insn-00ab161c)

~~~json
{
  "source": "00ab161c",
  "target": "00ab16ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1620`](#insn-00ab1620)

~~~json
{
  "source": "00ab1620",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1624`](#insn-00ab1624)

~~~json
{
  "source": "00ab1624",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1630`](#insn-00ab1630)

~~~json
{
  "source": "00ab1630",
  "target": "0033f8f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033f8f0",
  "offset": 0,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "4ce18c00c4470c00",
  "capture_start": "0033f8f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab1634`](#insn-00ab1634)

~~~json
{
  "source": "00ab1634",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1644`](#insn-00ab1644)

~~~json
{
  "source": "00ab1644",
  "target": "00ab1650",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab164c`](#insn-00ab164c)

~~~json
{
  "source": "00ab164c",
  "target": "00ab1678",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1650`](#insn-00ab1650)

~~~json
{
  "source": "00ab1650",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1658`](#insn-00ab1658)

~~~json
{
  "source": "00ab1658",
  "target": "00744208",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab165c`](#insn-00ab165c)

~~~json
{
  "source": "00ab165c",
  "target": "00ab1668",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1664`](#insn-00ab1664)

~~~json
{
  "source": "00ab1664",
  "target": "00ab1678",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1668`](#insn-00ab1668)

~~~json
{
  "source": "00ab1668",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1674`](#insn-00ab1674)

~~~json
{
  "source": "00ab1674",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab167c`](#insn-00ab167c)

~~~json
{
  "source": "00ab167c",
  "target": "00ab1688",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1684`](#insn-00ab1684)

~~~json
{
  "source": "00ab1684",
  "target": "00ab16ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1688`](#insn-00ab1688)

~~~json
{
  "source": "00ab1688",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab168c`](#insn-00ab168c)

~~~json
{
  "source": "00ab168c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1698`](#insn-00ab1698)

~~~json
{
  "source": "00ab1698",
  "target": "0033f8f4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0033f8f0",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "4ce18c00c4470c00",
  "capture_start": "0033f8f0",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab169c`](#insn-00ab169c)

~~~json
{
  "source": "00ab169c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab16ac`](#insn-00ab16ac)

~~~json
{
  "source": "00ab16ac",
  "target": "00ab16b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab16b4`](#insn-00ab16b4)

~~~json
{
  "source": "00ab16b4",
  "target": "00ab16e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab16b8`](#insn-00ab16b8)

~~~json
{
  "source": "00ab16b8",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab16c0`](#insn-00ab16c0)

~~~json
{
  "source": "00ab16c0",
  "target": "00744208",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab16c4`](#insn-00ab16c4)

~~~json
{
  "source": "00ab16c4",
  "target": "00ab16d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab16cc`](#insn-00ab16cc)

~~~json
{
  "source": "00ab16cc",
  "target": "00ab16e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab16d0`](#insn-00ab16d0)

~~~json
{
  "source": "00ab16d0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab16dc`](#insn-00ab16dc)

~~~json
{
  "source": "00ab16dc",
  "target": "00333974",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333970",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "68b56a00a0770900",
  "capture_start": "00333970",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab16e4`](#insn-00ab16e4)

~~~json
{
  "source": "00ab16e4",
  "target": "00ab1730",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab16ec`](#insn-00ab16ec)

~~~json
{
  "source": "00ab16ec",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab16f8`](#insn-00ab16f8)

~~~json
{
  "source": "00ab16f8",
  "target": "00333f64",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00333f60",
  "offset": 4,
  "size": 8,
  "datatype": "fde_table_entry",
  "bytes": "04ab6c002c8d0900",
  "capture_start": "00333f60",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ab16fc`](#insn-00ab16fc)

~~~json
{
  "source": "00ab16fc",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1700`](#insn-00ab1700)

~~~json
{
  "source": "00ab1700",
  "target": "0085ccf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1704`](#insn-00ab1704)

~~~json
{
  "source": "00ab1704",
  "target": "0047acf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab170c`](#insn-00ab170c)

~~~json
{
  "source": "00ab170c",
  "target": "0047ca8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1714`](#insn-00ab1714)

~~~json
{
  "source": "00ab1714",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1718`](#insn-00ab1718)

~~~json
{
  "source": "00ab1718",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab171c`](#insn-00ab171c)

~~~json
{
  "source": "00ab171c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1720`](#insn-00ab1720)

~~~json
{
  "source": "00ab1720",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1724`](#insn-00ab1724)

~~~json
{
  "source": "00ab1724",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab1728`](#insn-00ab1728)

~~~json
{
  "source": "00ab1728",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ab172c`](#insn-00ab172c)

~~~json
{
  "source": "00ab172c",
  "target": "0072bf4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1730`](#insn-00ab1730)

~~~json
{
  "source": "00ab1730",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ab1734`](#insn-00ab1734)

~~~json
{
  "source": "00ab1734",
  "target": "00ab16fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
