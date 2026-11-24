# 00afeae8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afe6c0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afe/00afe6c0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-92223e184fe625bb2cdb839f544bba2d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afeb84`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afe/00afeb84.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0067.md#compare-668c8ad174cbf2166ff2db158f5d4b16)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afeae8",
  "name": "FUN_00afeae8",
  "size": 2020,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef39ebe1212841dd57aaafaa6b1750c180b7d3490bd596278490752324bdeb56",
  "source_text_sha256": "ef39ebe1212841dd57aaafaa6b1750c180b7d3490bd596278490752324bdeb56",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afeae8",
        "00aff2cb"
      ]
    ],
    "bytes_sha256": "e555c3bb769d948200cdf7a4eda75c4842c3f34b27574889048eab90f97df69b",
    "instruction_count": 505,
    "instruction_bytes": 2020,
    "body_bytes": 2020,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0070ea5c](../0070e/0070ea5c.md)
- [007102d8](../00710/007102d8.md)
- [007119f0](../00711/007119f0.md)
- [00716d90](../00716/00716d90.md)
- [00a4f3b4](../00a4f/00a4f3b4.md)
- [00a51fc4](../00a51/00a51fc4.md)
- [00afe40c](../00afe/00afe40c.md)
- [00aff3f8](../00aff/00aff3f8.md)
- [00aff4a0](../00aff/00aff4a0.md)
- [00aff62c](../00aff/00aff62c.md)
- [00affe14](../00aff/00affe14.md)
- [00afff64](../00aff/00afff64.md)
- [00b00054](../00b00/00b00054.md)
- [00b0037c](../00b00/00b0037c.md)
- [00b00f38](../00b00/00b00f38.md)
- [00b00fe0](../00b00/00b00fe0.md)
- [00b01110](../00b01/00b01110.md)
- [00b011b8](../00b01/00b011b8.md)
- [00b01260](../00b01/00b01260.md)
- [00b013c4](../00b01/00b013c4.md)
- [00b01794](../00b01/00b01794.md)
- [00b0183c](../00b01/00b0183c.md)
- [00b019b4](../00b01/00b019b4.md)
- [00b02408](../00b02/00b02408.md)
- [00b02684](../00b02/00b02684.md)
- [00b032f4](../00b03/00b032f4.md)
- [00b0339c](../00b03/00b0339c.md)
- [00b03444](../00b03/00b03444.md)
- [00b03514](../00b03/00b03514.md)
- [00b03650](../00b03/00b03650.md)
- [00b037b4](../00b03/00b037b4.md)
- [00b03ef4](../00b03/00b03ef4.md)
- [00b052d4](../00b05/00b052d4.md)
- [00b055c4](../00b05/00b055c4.md)
- [00b0566c](../00b05/00b0566c.md)
- [00b05714](../00b05/00b05714.md)
- [00b05818](../00b05/00b05818.md)
- [00b058e8](../00b05/00b058e8.md)
- [00b059b8](../00b05/00b059b8.md)
- [00b05b9c](../00b05/00b05b9c.md)
- [00b05c44](../00b05/00b05c44.md)
- [00b05cec](../00b05/00b05cec.md)
- [00b05d78](../00b05/00b05d78.md)
- [00b05e34](../00b05/00b05e34.md)
- [00b05edc](../00b05/00b05edc.md)
- [00b05f84](../00b05/00b05f84.md)
- [00b0602c](../00b06/00b0602c.md)
- [00b0613c](../00b06/00b0613c.md)
- [00b061e4](../00b06/00b061e4.md)
- [00b0628c](../00b06/00b0628c.md)
- [00b06334](../00b06/00b06334.md)
- [00b063c0](../00b06/00b063c0.md)
- [00b067e0](../00b06/00b067e0.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [008514f8](../00851/008514f8.md)
- [009e0fc0](../009e0/009e0fc0.md)
- [009e3ea8](../009e3/009e3ea8.md)
- [00b0272c](../00b02/00b0272c.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58090](../00c58/00c58090.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 16604 bytes

~~~c

void FUN_00afeae8(undefined8 param_1,int param_2,undefined8 param_3,int param_4,int param_5)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  long lVar5;
  int iVar6;
  ulong uVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined8 *puVar11;
  undefined8 *puVar12;
  undefined8 *puVar13;
  long lVar14;
  long *plVar15;
  undefined8 *puVar16;
  void *local_88;
  void *local_80;
  char local_70;
  long local_68;
  
  lVar5 = tpidr_el0;
  local_68 = *(long *)(lVar5 + 0x28);
  uVar7 = FUN_00b0272c();
  if ((uVar7 & 1) != 0) {
    lVar8 = FUN_008514f8();
    uVar7 = FUN_009e0fc0(lVar8 + 0x50,0xffffffff,0xffffffff);
    if ((uVar7 & 1) == 0) {
      lVar8 = 0;
      do {
        lVar9 = FUN_008514f8();
        puVar13 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
        if (puVar13 == (undefined8 *)0x0) {
          puVar16 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
          puVar11 = puVar16;
        }
        else {
          do {
            while (puVar10 = puVar13, puVar16 = puVar10, *(int *)((long)puVar10 + 0x1c) <= param_2)
            {
              if (param_2 <= *(int *)((long)puVar10 + 0x1c)) goto code_r0x00afec30;
              puVar13 = (undefined8 *)puVar10[1];
              if ((undefined8 *)puVar10[1] == (undefined8 *)0x0) {
                puVar11 = puVar10 + 1;
                goto LAB_00afebd0;
              }
            }
            puVar13 = (undefined8 *)*puVar10;
            puVar11 = puVar10;
          } while ((undefined8 *)*puVar10 != (undefined8 *)0x0);
        }
LAB_00afebd0:
        puVar10 = (undefined8 *)_Znwm(0x290);
        *(int *)((long)puVar10 + 0x1c) = param_2;
        memset(puVar10 + 4,0,0x26c);
        *puVar10 = 0;
        puVar10[1] = 0;
        puVar10[2] = puVar16;
        *puVar11 = puVar10;
        lVar14 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar9);
        puVar13 = puVar10;
        if (lVar14 != 0) {
          *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar9) = lVar14;
          puVar13 = (undefined8 *)*puVar11;
        }
        FUN_0043bba4(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9),puVar13);
        *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) =
             *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) + 1;
code_r0x00afec30:
        if (*(int *)((long)puVar10 + lVar8 * 0x38 + 0x24) == param_4) {
          lVar9 = FUN_008514f8();
          puVar13 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
          if (puVar13 != (undefined8 *)0x0) goto LAB_00afeca8;
          puVar16 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
          puVar11 = puVar16;
          goto LAB_00afecc8;
        }
        lVar8 = lVar8 + 1;
      } while (lVar8 != 0xb);
    }
    else {
      lVar8 = FUN_008514f8();
      FUN_009e3ea8(&local_88,lVar8 + 0x50,param_2,param_4,0xffffffff,0xffffffff);
      if (local_70 != '\0') {
        iVar6 = *(int *)((long)local_88 + (long)param_5 * 4);
        local_80 = local_88;
        _ZdlPv(local_88);
        goto LAB_00afec50;
      }
    }
  }
  iVar6 = 0;
  goto LAB_00afec50;
  while (puVar13 = (undefined8 *)*puVar10, puVar11 = puVar10,
        (undefined8 *)*puVar10 != (undefined8 *)0x0) {
LAB_00afeca8:
    puVar10 = puVar13;
    puVar16 = puVar10;
    if (*(int *)((long)puVar10 + 0x1c) <= param_2) {
      if (param_2 <= *(int *)((long)puVar10 + 0x1c)) goto LAB_00afed24;
      puVar13 = (undefined8 *)puVar10[1];
      if ((undefined8 *)puVar10[1] == (undefined8 *)0x0) {
        puVar11 = puVar10 + 1;
        break;
      }
      goto LAB_00afeca8;
    }
  }
LAB_00afecc8:
  puVar10 = (undefined8 *)_Znwm(0x290);
  *(int *)((long)puVar10 + 0x1c) = param_2;
  memset(puVar10 + 4,0,0x26c);
  *puVar10 = 0;
  puVar10[1] = 0;
  puVar10[2] = puVar16;
  *puVar11 = puVar10;
  lVar14 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar9);
  puVar13 = puVar10;
  if (lVar14 != 0) {
    *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar9) = lVar14;
    puVar13 = (undefined8 *)*puVar11;
  }
  FUN_0043bba4(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9),puVar13);
  *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) =
       *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) + 1;
LAB_00afed24:
  iVar1 = *(int *)(puVar10 + lVar8 * 7 + 5);
  lVar9 = FUN_008514f8();
  if (iVar1 < 2) {
    puVar13 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
    if (puVar13 == (undefined8 *)0x0) {
      puVar16 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
      puVar11 = puVar16;
    }
    else {
      do {
        while (puVar10 = puVar13, puVar16 = puVar10, *(int *)((long)puVar10 + 0x1c) <= param_2) {
          if (param_2 <= *(int *)((long)puVar10 + 0x1c)) goto LAB_00afeddc;
          puVar13 = (undefined8 *)puVar10[1];
          if ((undefined8 *)puVar10[1] == (undefined8 *)0x0) {
            puVar11 = puVar10 + 1;
            goto LAB_00afed80;
          }
        }
        puVar13 = (undefined8 *)*puVar10;
        puVar11 = puVar10;
      } while ((undefined8 *)*puVar10 != (undefined8 *)0x0);
    }
LAB_00afed80:
    puVar10 = (undefined8 *)_Znwm(0x290);
    *(int *)((long)puVar10 + 0x1c) = param_2;
    memset(puVar10 + 4,0,0x26c);
    *puVar10 = 0;
    puVar10[1] = 0;
    puVar10[2] = puVar16;
    *puVar11 = puVar10;
    lVar14 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar9);
    puVar13 = puVar10;
    if (lVar14 != 0) {
      *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar9) = lVar14;
      puVar13 = (undefined8 *)*puVar11;
    }
    FUN_0043bba4(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9),puVar13);
    *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) =
         *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) + 1;
LAB_00afeddc:
    iVar6 = *(int *)((long)puVar10 + (long)param_5 * 4 + lVar8 * 0x38 + 0x2c);
  }
  else {
    puVar13 = *(undefined8 **)((long)&__DT_JMPREL[0xfd].r_offset + lVar9);
    if (puVar13 == (undefined8 *)0x0) {
      puVar16 = (undefined8 *)((long)&__DT_JMPREL[0xfd].r_offset + lVar9);
      puVar11 = puVar16;
    }
    else {
      do {
        while (puVar10 = puVar13, puVar16 = puVar10, param_2 < *(int *)(puVar10 + 4)) {
          puVar13 = (undefined8 *)*puVar10;
          puVar11 = puVar10;
          if ((undefined8 *)*puVar10 == (undefined8 *)0x0) goto LAB_00afee30;
        }
        if (param_2 <= *(int *)(puVar10 + 4)) goto LAB_00afee8c;
        puVar13 = (undefined8 *)puVar10[1];
      } while ((undefined8 *)puVar10[1] != (undefined8 *)0x0);
      puVar11 = puVar10 + 1;
    }
LAB_00afee30:
    puVar10 = (undefined8 *)_Znwm(0x40);
    puVar10[7] = 0;
    puVar10[6] = 0;
    puVar10[5] = puVar10 + 6;
    *puVar10 = 0;
    puVar10[1] = 0;
    puVar10[2] = puVar16;
    *puVar11 = puVar10;
    plVar15 = *(long **)((long)&__DT_JMPREL[0xfc].r_addend + lVar9);
    *(int *)(puVar10 + 4) = param_2;
    lVar14 = *plVar15;
    puVar13 = puVar10;
    if (lVar14 != 0) {
      *(long *)((long)&__DT_JMPREL[0xfc].r_addend + lVar9) = lVar14;
      puVar13 = (undefined8 *)*puVar11;
    }
    FUN_0043bba4(*(undefined8 *)((long)&__DT_JMPREL[0xfd].r_offset + lVar9),puVar13);
    *(long *)((long)&__DT_JMPREL[0xfd].r_info + lVar9) =
         *(long *)((long)&__DT_JMPREL[0xfd].r_info + lVar9) + 1;
LAB_00afee8c:
    lVar9 = FUN_008514f8();
    puVar13 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
    if (puVar13 == (undefined8 *)0x0) {
      puVar16 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
      puVar12 = puVar16;
    }
    else {
      do {
        while (puVar11 = puVar13, puVar16 = puVar11, *(int *)((long)puVar11 + 0x1c) <= param_2) {
          if (param_2 <= *(int *)((long)puVar11 + 0x1c)) goto LAB_00afef30;
          puVar13 = (undefined8 *)puVar11[1];
          if ((undefined8 *)puVar11[1] == (undefined8 *)0x0) {
            puVar12 = puVar11 + 1;
            goto LAB_00afeed4;
          }
        }
        puVar13 = (undefined8 *)*puVar11;
        puVar12 = puVar11;
      } while ((undefined8 *)*puVar11 != (undefined8 *)0x0);
    }
LAB_00afeed4:
    puVar11 = (undefined8 *)_Znwm(0x290);
    *(int *)((long)puVar11 + 0x1c) = param_2;
    memset(puVar11 + 4,0,0x26c);
    *puVar11 = 0;
    puVar11[1] = 0;
    puVar11[2] = puVar16;
    *puVar12 = puVar11;
    lVar14 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar9);
    puVar13 = puVar11;
    if (lVar14 != 0) {
      *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar9) = lVar14;
      puVar13 = (undefined8 *)*puVar12;
    }
    FUN_0043bba4(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9),puVar13);
    *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) =
         *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) + 1;
LAB_00afef30:
    iVar1 = *(int *)((long)puVar11 + lVar8 * 0x38 + 0x24);
    puVar16 = (undefined8 *)puVar10[6];
    puVar13 = puVar10 + 6;
    while (puVar11 = puVar13, puVar16 != (undefined8 *)0x0) {
      while (puVar12 = puVar16, puVar13 = puVar12, *(int *)((long)puVar12 + 0x1c) <= iVar1) {
        if (iVar1 <= *(int *)((long)puVar12 + 0x1c)) goto LAB_00afefcc;
        puVar16 = (undefined8 *)puVar12[1];
        if ((undefined8 *)puVar12[1] == (undefined8 *)0x0) {
          puVar11 = puVar12 + 1;
          goto LAB_00afef80;
        }
      }
      puVar16 = (undefined8 *)*puVar12;
    }
LAB_00afef80:
    puVar12 = (undefined8 *)_Znwm(0x28);
    *puVar12 = 0;
    puVar12[1] = 0;
    puVar12[2] = puVar13;
    *puVar11 = puVar12;
    plVar15 = (long *)puVar10[5];
    *(int *)((long)puVar12 + 0x1c) = iVar1;
    *(undefined4 *)(puVar12 + 4) = 0;
    puVar13 = puVar12;
    if (*plVar15 != 0) {
      puVar10[5] = *plVar15;
      puVar13 = (undefined8 *)*puVar11;
    }
    FUN_0043bba4(puVar10[6],puVar13);
    puVar10[7] = puVar10[7] + 1;
LAB_00afefcc:
    iVar1 = *(int *)(puVar12 + 4);
    lVar9 = FUN_008514f8();
    puVar13 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
    if (puVar13 == (undefined8 *)0x0) {
      puVar16 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
      puVar11 = puVar16;
    }
    else {
      do {
        while (puVar10 = puVar13, puVar16 = puVar10, *(int *)((long)puVar10 + 0x1c) <= param_2) {
          if (param_2 <= *(int *)((long)puVar10 + 0x1c)) goto LAB_00aff074;
          puVar13 = (undefined8 *)puVar10[1];
          if ((undefined8 *)puVar10[1] == (undefined8 *)0x0) {
            puVar11 = puVar10 + 1;
            goto LAB_00aff018;
          }
        }
        puVar13 = (undefined8 *)*puVar10;
        puVar11 = puVar10;
      } while ((undefined8 *)*puVar10 != (undefined8 *)0x0);
    }
LAB_00aff018:
    puVar10 = (undefined8 *)_Znwm(0x290);
    *(int *)((long)puVar10 + 0x1c) = param_2;
    memset(puVar10 + 4,0,0x26c);
    *puVar10 = 0;
    puVar10[1] = 0;
    puVar10[2] = puVar16;
    *puVar11 = puVar10;
    lVar14 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar9);
    puVar13 = puVar10;
    if (lVar14 != 0) {
      *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar9) = lVar14;
      puVar13 = (undefined8 *)*puVar11;
    }
    FUN_0043bba4(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9),puVar13);
    *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) =
         *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) + 1;
LAB_00aff074:
    iVar2 = *(int *)((long)puVar10 + (long)param_5 * 4 + lVar8 * 0x38 + 0x2c);
    lVar9 = FUN_008514f8();
    puVar13 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
    if (puVar13 == (undefined8 *)0x0) {
      puVar16 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
      puVar11 = puVar16;
    }
    else {
      do {
        while (puVar10 = puVar13, puVar16 = puVar10, *(int *)((long)puVar10 + 0x1c) <= param_2) {
          if (param_2 <= *(int *)((long)puVar10 + 0x1c)) goto LAB_00aff130;
          puVar13 = (undefined8 *)puVar10[1];
          if ((undefined8 *)puVar10[1] == (undefined8 *)0x0) {
            puVar11 = puVar10 + 1;
            goto LAB_00aff0d4;
          }
        }
        puVar13 = (undefined8 *)*puVar10;
        puVar11 = puVar10;
      } while ((undefined8 *)*puVar10 != (undefined8 *)0x0);
    }
LAB_00aff0d4:
    puVar10 = (undefined8 *)_Znwm(0x290);
    *(int *)((long)puVar10 + 0x1c) = param_2;
    memset(puVar10 + 4,0,0x26c);
    *puVar10 = 0;
    puVar10[1] = 0;
    puVar10[2] = puVar16;
    *puVar11 = puVar10;
    lVar14 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar9);
    puVar13 = puVar10;
    if (lVar14 != 0) {
      *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar9) = lVar14;
      puVar13 = (undefined8 *)*puVar11;
    }
    FUN_0043bba4(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9),puVar13);
    *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) =
         *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) + 1;
LAB_00aff130:
    iVar3 = *(int *)((long)puVar10 + (long)param_5 * 4 + lVar8 * 0x38 + 0x3c);
    lVar9 = FUN_008514f8();
    puVar13 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
    if (puVar13 == (undefined8 *)0x0) {
      puVar16 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
      puVar11 = puVar16;
    }
    else {
      do {
        while (puVar10 = puVar13, puVar16 = puVar10, *(int *)((long)puVar10 + 0x1c) <= param_2) {
          if (param_2 <= *(int *)((long)puVar10 + 0x1c)) goto LAB_00aff1e4;
          puVar13 = (undefined8 *)puVar10[1];
          if ((undefined8 *)puVar10[1] == (undefined8 *)0x0) {
            puVar11 = puVar10 + 1;
            goto LAB_00aff188;
          }
        }
        puVar13 = (undefined8 *)*puVar10;
        puVar11 = puVar10;
      } while ((undefined8 *)*puVar10 != (undefined8 *)0x0);
    }
LAB_00aff188:
    puVar10 = (undefined8 *)_Znwm(0x290);
    *(int *)((long)puVar10 + 0x1c) = param_2;
    memset(puVar10 + 4,0,0x26c);
    *puVar10 = 0;
    puVar10[1] = 0;
    puVar10[2] = puVar16;
    *puVar11 = puVar10;
    lVar14 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar9);
    puVar13 = puVar10;
    if (lVar14 != 0) {
      *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar9) = lVar14;
      puVar13 = (undefined8 *)*puVar11;
    }
    FUN_0043bba4(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9),puVar13);
    *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) =
         *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) + 1;
LAB_00aff1e4:
    iVar4 = *(int *)((long)puVar10 + (long)param_5 * 4 + lVar8 * 0x38 + 0x2c);
    lVar9 = FUN_008514f8();
    puVar13 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
    if (puVar13 == (undefined8 *)0x0) {
      puVar16 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9);
      puVar11 = puVar16;
    }
    else {
      do {
        while (puVar10 = puVar13, puVar16 = puVar10, *(int *)((long)puVar10 + 0x1c) <= param_2) {
          if (param_2 <= *(int *)((long)puVar10 + 0x1c)) goto LAB_00aff2a4;
          puVar13 = (undefined8 *)puVar10[1];
          if ((undefined8 *)puVar10[1] == (undefined8 *)0x0) {
            puVar11 = puVar10 + 1;
            goto LAB_00aff248;
          }
        }
        puVar13 = (undefined8 *)*puVar10;
        puVar11 = puVar10;
      } while ((undefined8 *)*puVar10 != (undefined8 *)0x0);
    }
LAB_00aff248:
    puVar10 = (undefined8 *)_Znwm(0x290);
                    /* try { // try from 00aff258 to 00bff2ab has its CatchHandler @ 00aff258
                       catch() { ... } // from try @ 00aff258 with catch @ 00aff258
                       catch() { ... } // from try @ 00aff2cc with catch @ 00aff258 */
    *(int *)((long)puVar10 + 0x1c) = param_2;
    memset(puVar10 + 4,0,0x26c);
    *puVar10 = 0;
    puVar10[1] = 0;
    puVar10[2] = puVar16;
    *puVar11 = puVar10;
    lVar14 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar9);
    puVar13 = puVar10;
    if (lVar14 != 0) {
      *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar9) = lVar14;
      puVar13 = (undefined8 *)*puVar11;
    }
    FUN_0043bba4(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar9),puVar13);
    *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) =
         *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar9) + 1;
LAB_00aff2a4:
                    /* try { // try from 00aff2ac to 00bff2cb has its CatchHandler @ 00aff2e4 */
    iVar6 = 0;
    if (*(int *)(puVar10 + lVar8 * 7 + 5) + -1 != 0) {
      iVar6 = ((iVar3 - iVar4) * (iVar1 + -1)) / (*(int *)(puVar10 + lVar8 * 7 + 5) + -1);
    }
    iVar6 = iVar6 + iVar2;
  }
LAB_00afec50:
  if (*(long *)(lVar5 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(iVar6);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afeae8"></a> `00afeae8` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00afeaec"></a> `00afeaec` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afeaf0"></a> `00afeaf0` | `fc 6f 04 a9` | stp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afeaf4"></a> `00afeaf4` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afeaf8"></a> `00afeaf8` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afeafc"></a> `00afeafc` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afeb00"></a> `00afeb00` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00afeb04"></a> `00afeb04` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00afeb08"></a> `00afeb08` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afeb0c"></a> `00afeb0c` | `f4 03 04 2a` | mov w20,w4 | `FALL_THROUGH`
<a id="insn-00afeb10"></a> `00afeb10` | `f5 03 03 2a` | mov w21,w3 | `FALL_THROUGH`
<a id="insn-00afeb14"></a> `00afeb14` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00afeb18"></a> `00afeb18` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afeb1c"></a> `00afeb1c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00afeb20"></a> `00afeb20` | `03 0f 00 94` | bl 0x00b0272c | `UNCONDITIONAL_CALL`
<a id="insn-00afeb24"></a> `00afeb24` | `40 09 00 36` | tbz w0,#0x0,0x00afec4c | `CONDITIONAL_JUMP`
<a id="insn-00afeb28"></a> `00afeb28` | `74 4a f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afeb2c"></a> `00afeb2c` | `00 40 01 91` | add x0,x0,#0x50 | `FALL_THROUGH`
<a id="insn-00afeb30"></a> `00afeb30` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00afeb34"></a> `00afeb34` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00afeb38"></a> `00afeb38` | `22 89 fb 97` | bl 0x009e0fc0 | `UNCONDITIONAL_CALL`
<a id="insn-00afeb3c"></a> `00afeb3c` | `20 02 00 36` | tbz w0,#0x0,0x00afeb80 | `CONDITIONAL_JUMP`
<a id="insn-00afeb40"></a> `00afeb40` | `6e 4a f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afeb44"></a> `00afeb44` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00afeb48"></a> `00afeb48` | `00 40 01 91` | add x0,x0,#0x50 | `FALL_THROUGH`
<a id="insn-00afeb4c"></a> `00afeb4c` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00afeb50"></a> `00afeb50` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00afeb54"></a> `00afeb54` | `03 00 80 12` | mov w3,#0xffffffff | `FALL_THROUGH`
<a id="insn-00afeb58"></a> `00afeb58` | `04 00 80 12` | mov w4,#0xffffffff | `FALL_THROUGH`
<a id="insn-00afeb5c"></a> `00afeb5c` | `d3 94 fb 97` | bl 0x009e3ea8 | `UNCONDITIONAL_CALL`
<a id="insn-00afeb60"></a> `00afeb60` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afeb64"></a> `00afeb64` | `48 07 00 34` | cbz w8,0x00afec4c | `CONDITIONAL_JUMP`
<a id="insn-00afeb68"></a> `00afeb68` | `e0 07 40 f9` | ldr x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00afeb6c"></a> `00afeb6c` | `13 d8 74 b8` | ldr w19,[x0, w20, SXTW #0x2] | `FALL_THROUGH`
<a id="insn-00afeb70"></a> `00afeb70` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afeb74"></a> `00afeb74` | `cf 64 05 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00afeb78"></a> `00afeb78` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00afeb7c"></a> `00afeb7c` | `35 00 00 14` | b 0x00afec50 | `UNCONDITIONAL_JUMP`
<a id="insn-00afeb80"></a> `00afeb80` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00afeb84"></a> `00afeb84` | `19 07 80 52` | mov w25,#0x38 | `FALL_THROUGH`
<a id="insn-00afeb88"></a> `00afeb88` | `5c 4a f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afeb8c"></a> `00afeb8c` | `1a f4 48 91` | add x26,x0,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-00afeb90"></a> `00afeb90` | `48 1f 41 f9` | ldr x8,[x26, #0x238] | `FALL_THROUGH`
<a id="insn-00afeb94"></a> `00afeb94` | `e8 00 00 b5` | cbnz x8,0x00afebb0 | `CONDITIONAL_JUMP`
<a id="insn-00afeb98"></a> `00afeb98` | `5b e3 08 91` | add x27,x26,#0x238 | `FALL_THROUGH`
<a id="insn-00afeb9c"></a> `00afeb9c` | `f6 03 1b aa` | mov x22,x27 | `FALL_THROUGH`
<a id="insn-00afeba0"></a> `00afeba0` | `0c 00 00 14` | b 0x00afebd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00afeba4"></a> `00afeba4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00afeba8"></a> `00afeba8` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00afebac"></a> `00afebac` | `28 01 00 b4` | cbz x8,0x00afebd0 | `CONDITIONAL_JUMP`
<a id="insn-00afebb0"></a> `00afebb0` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00afebb4"></a> `00afebb4` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00afebb8"></a> `00afebb8` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00afebbc"></a> `00afebbc` | `4c ff ff 54` | b.gt 0x00afeba4 | `CONDITIONAL_JUMP`
<a id="insn-00afebc0"></a> `00afebc0` | `6a 03 00 54` | b.ge 0x00afec2c | `CONDITIONAL_JUMP`
<a id="insn-00afebc4"></a> `00afebc4` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00afebc8"></a> `00afebc8` | `48 ff ff b5` | cbnz x8,0x00afebb0 | `CONDITIONAL_JUMP`
<a id="insn-00afebcc"></a> `00afebcc` | `db 22 00 91` | add x27,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00afebd0"></a> `00afebd0` | `00 52 80 52` | mov w0,#0x290 | `FALL_THROUGH`
<a id="insn-00afebd4"></a> `00afebd4` | `fc 03 16 aa` | mov x28,x22 | `FALL_THROUGH`
<a id="insn-00afebd8"></a> `00afebd8` | `ae 64 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00afebdc"></a> `00afebdc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00afebe0"></a> `00afebe0` | `13 1c 00 b9` | str w19,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00afebe4"></a> `00afebe4` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00afebe8"></a> `00afebe8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00afebec"></a> `00afebec` | `82 4d 80 52` | mov w2,#0x26c | `FALL_THROUGH`
<a id="insn-00afebf0"></a> `00afebf0` | `28 65 05 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-00afebf4"></a> `00afebf4` | `df 7e 00 a9` | stp xzr,xzr,[x22] | `FALL_THROUGH`
<a id="insn-00afebf8"></a> `00afebf8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afebfc"></a> `00afebfc` | `dc 0a 00 f9` | str x28,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00afec00"></a> `00afec00` | `76 03 00 f9` | str x22,[x27] | `FALL_THROUGH`
<a id="insn-00afec04"></a> `00afec04` | `48 1b 41 f9` | ldr x8,[x26, #0x230] | `FALL_THROUGH`
<a id="insn-00afec08"></a> `00afec08` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afec0c"></a> `00afec0c` | `68 00 00 b4` | cbz x8,0x00afec18 | `CONDITIONAL_JUMP`
<a id="insn-00afec10"></a> `00afec10` | `48 1b 01 f9` | str x8,[x26, #0x230] | `FALL_THROUGH`
<a id="insn-00afec14"></a> `00afec14` | `61 03 40 f9` | ldr x1,[x27] | `FALL_THROUGH`
<a id="insn-00afec18"></a> `00afec18` | `40 1f 41 f9` | ldr x0,[x26, #0x238] | `FALL_THROUGH`
<a id="insn-00afec1c"></a> `00afec1c` | `e2 f3 e4 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00afec20"></a> `00afec20` | `48 23 41 f9` | ldr x8,[x26, #0x240] | `FALL_THROUGH`
<a id="insn-00afec24"></a> `00afec24` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afec28"></a> `00afec28` | `48 23 01 f9` | str x8,[x26, #0x240] | `FALL_THROUGH`
<a id="insn-00afec2c"></a> `00afec2c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00afec30"></a> `00afec30` | `08 5b 19 9b` | madd x8,x24,x25,x22 | `FALL_THROUGH`
<a id="insn-00afec34"></a> `00afec34` | `08 25 40 b9` | ldr w8,[x8, #0x24] | `FALL_THROUGH`
<a id="insn-00afec38"></a> `00afec38` | `1f 01 15 6b` | cmp w8,w21 | `FALL_THROUGH`
<a id="insn-00afec3c"></a> `00afec3c` | `20 02 00 54` | b.eq 0x00afec80 | `CONDITIONAL_JUMP`
<a id="insn-00afec40"></a> `00afec40` | `18 07 00 91` | add x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00afec44"></a> `00afec44` | `1f 2f 00 f1` | cmp x24,#0xb | `FALL_THROUGH`
<a id="insn-00afec48"></a> `00afec48` | `01 fa ff 54` | b.ne 0x00afeb88 | `CONDITIONAL_JUMP`
<a id="insn-00afec4c"></a> `00afec4c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00afec50"></a> `00afec50` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00afec54"></a> `00afec54` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00afec58"></a> `00afec58` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afec5c"></a> `00afec5c` | `61 33 00 54` | b.ne 0x00aff2c8 | `CONDITIONAL_JUMP`
<a id="insn-00afec60"></a> `00afec60` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00afec64"></a> `00afec64` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00afec68"></a> `00afec68` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afec6c"></a> `00afec6c` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00afec70"></a> `00afec70` | `fc 6f 44 a9` | ldp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afec74"></a> `00afec74` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afec78"></a> `00afec78` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00afec7c"></a> `00afec7c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afec80"></a> `00afec80` | `1e 4a f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afec84"></a> `00afec84` | `16 f4 48 91` | add x22,x0,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-00afec88"></a> `00afec88` | `c8 1e 41 f9` | ldr x8,[x22, #0x238] | `FALL_THROUGH`
<a id="insn-00afec8c"></a> `00afec8c` | `e8 00 00 b5` | cbnz x8,0x00afeca8 | `CONDITIONAL_JUMP`
<a id="insn-00afec90"></a> `00afec90` | `d9 e2 08 91` | add x25,x22,#0x238 | `FALL_THROUGH`
<a id="insn-00afec94"></a> `00afec94` | `f5 03 19 aa` | mov x21,x25 | `FALL_THROUGH`
<a id="insn-00afec98"></a> `00afec98` | `0c 00 00 14` | b 0x00afecc8 | `UNCONDITIONAL_JUMP`
<a id="insn-00afec9c"></a> `00afec9c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00afeca0"></a> `00afeca0` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00afeca4"></a> `00afeca4` | `28 01 00 b4` | cbz x8,0x00afecc8 | `CONDITIONAL_JUMP`
<a id="insn-00afeca8"></a> `00afeca8` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00afecac"></a> `00afecac` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00afecb0"></a> `00afecb0` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00afecb4"></a> `00afecb4` | `4c ff ff 54` | b.gt 0x00afec9c | `CONDITIONAL_JUMP`
<a id="insn-00afecb8"></a> `00afecb8` | `6a 03 00 54` | b.ge 0x00afed24 | `CONDITIONAL_JUMP`
<a id="insn-00afecbc"></a> `00afecbc` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00afecc0"></a> `00afecc0` | `48 ff ff b5` | cbnz x8,0x00afeca8 | `CONDITIONAL_JUMP`
<a id="insn-00afecc4"></a> `00afecc4` | `b9 22 00 91` | add x25,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00afecc8"></a> `00afecc8` | `00 52 80 52` | mov w0,#0x290 | `FALL_THROUGH`
<a id="insn-00afeccc"></a> `00afeccc` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-00afecd0"></a> `00afecd0` | `70 64 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00afecd4"></a> `00afecd4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00afecd8"></a> `00afecd8` | `13 1c 00 b9` | str w19,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00afecdc"></a> `00afecdc` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00afece0"></a> `00afece0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00afece4"></a> `00afece4` | `82 4d 80 52` | mov w2,#0x26c | `FALL_THROUGH`
<a id="insn-00afece8"></a> `00afece8` | `ea 64 05 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-00afecec"></a> `00afecec` | `bf 7e 00 a9` | stp xzr,xzr,[x21] | `FALL_THROUGH`
<a id="insn-00afecf0"></a> `00afecf0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afecf4"></a> `00afecf4` | `ba 0a 00 f9` | str x26,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00afecf8"></a> `00afecf8` | `35 03 00 f9` | str x21,[x25] | `FALL_THROUGH`
<a id="insn-00afecfc"></a> `00afecfc` | `c8 1a 41 f9` | ldr x8,[x22, #0x230] | `FALL_THROUGH`
<a id="insn-00afed00"></a> `00afed00` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afed04"></a> `00afed04` | `68 00 00 b4` | cbz x8,0x00afed10 | `CONDITIONAL_JUMP`
<a id="insn-00afed08"></a> `00afed08` | `c8 1a 01 f9` | str x8,[x22, #0x230] | `FALL_THROUGH`
<a id="insn-00afed0c"></a> `00afed0c` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00afed10"></a> `00afed10` | `c0 1e 41 f9` | ldr x0,[x22, #0x238] | `FALL_THROUGH`
<a id="insn-00afed14"></a> `00afed14` | `a4 f3 e4 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00afed18"></a> `00afed18` | `c8 22 41 f9` | ldr x8,[x22, #0x240] | `FALL_THROUGH`
<a id="insn-00afed1c"></a> `00afed1c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afed20"></a> `00afed20` | `c8 22 01 f9` | str x8,[x22, #0x240] | `FALL_THROUGH`
<a id="insn-00afed24"></a> `00afed24` | `08 07 80 52` | mov w8,#0x38 | `FALL_THROUGH`
<a id="insn-00afed28"></a> `00afed28` | `08 57 08 9b` | madd x8,x24,x8,x21 | `FALL_THROUGH`
<a id="insn-00afed2c"></a> `00afed2c` | `15 29 40 b9` | ldr w21,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00afed30"></a> `00afed30` | `f2 49 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afed34"></a> `00afed34` | `bf 06 00 71` | cmp w21,#0x1 | `FALL_THROUGH`
<a id="insn-00afed38"></a> `00afed38` | `16 f4 48 91` | add x22,x0,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-00afed3c"></a> `00afed3c` | `ac 05 00 54` | b.gt 0x00afedf0 | `CONDITIONAL_JUMP`
<a id="insn-00afed40"></a> `00afed40` | `c8 1e 41 f9` | ldr x8,[x22, #0x238] | `FALL_THROUGH`
<a id="insn-00afed44"></a> `00afed44` | `e8 00 00 b5` | cbnz x8,0x00afed60 | `CONDITIONAL_JUMP`
<a id="insn-00afed48"></a> `00afed48` | `d9 e2 08 91` | add x25,x22,#0x238 | `FALL_THROUGH`
<a id="insn-00afed4c"></a> `00afed4c` | `f5 03 19 aa` | mov x21,x25 | `FALL_THROUGH`
<a id="insn-00afed50"></a> `00afed50` | `0c 00 00 14` | b 0x00afed80 | `UNCONDITIONAL_JUMP`
<a id="insn-00afed54"></a> `00afed54` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00afed58"></a> `00afed58` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00afed5c"></a> `00afed5c` | `28 01 00 b4` | cbz x8,0x00afed80 | `CONDITIONAL_JUMP`
<a id="insn-00afed60"></a> `00afed60` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00afed64"></a> `00afed64` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00afed68"></a> `00afed68` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00afed6c"></a> `00afed6c` | `4c ff ff 54` | b.gt 0x00afed54 | `CONDITIONAL_JUMP`
<a id="insn-00afed70"></a> `00afed70` | `6a 03 00 54` | b.ge 0x00afeddc | `CONDITIONAL_JUMP`
<a id="insn-00afed74"></a> `00afed74` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00afed78"></a> `00afed78` | `48 ff ff b5` | cbnz x8,0x00afed60 | `CONDITIONAL_JUMP`
<a id="insn-00afed7c"></a> `00afed7c` | `b9 22 00 91` | add x25,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00afed80"></a> `00afed80` | `00 52 80 52` | mov w0,#0x290 | `FALL_THROUGH`
<a id="insn-00afed84"></a> `00afed84` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-00afed88"></a> `00afed88` | `42 64 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00afed8c"></a> `00afed8c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00afed90"></a> `00afed90` | `13 1c 00 b9` | str w19,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00afed94"></a> `00afed94` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00afed98"></a> `00afed98` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00afed9c"></a> `00afed9c` | `82 4d 80 52` | mov w2,#0x26c | `FALL_THROUGH`
<a id="insn-00afeda0"></a> `00afeda0` | `bc 64 05 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-00afeda4"></a> `00afeda4` | `bf 7e 00 a9` | stp xzr,xzr,[x21] | `FALL_THROUGH`
<a id="insn-00afeda8"></a> `00afeda8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00afedac"></a> `00afedac` | `ba 0a 00 f9` | str x26,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00afedb0"></a> `00afedb0` | `35 03 00 f9` | str x21,[x25] | `FALL_THROUGH`
<a id="insn-00afedb4"></a> `00afedb4` | `c8 1a 41 f9` | ldr x8,[x22, #0x230] | `FALL_THROUGH`
<a id="insn-00afedb8"></a> `00afedb8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afedbc"></a> `00afedbc` | `68 00 00 b4` | cbz x8,0x00afedc8 | `CONDITIONAL_JUMP`
<a id="insn-00afedc0"></a> `00afedc0` | `c8 1a 01 f9` | str x8,[x22, #0x230] | `FALL_THROUGH`
<a id="insn-00afedc4"></a> `00afedc4` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00afedc8"></a> `00afedc8` | `c0 1e 41 f9` | ldr x0,[x22, #0x238] | `FALL_THROUGH`
<a id="insn-00afedcc"></a> `00afedcc` | `76 f3 e4 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00afedd0"></a> `00afedd0` | `c8 22 41 f9` | ldr x8,[x22, #0x240] | `FALL_THROUGH`
<a id="insn-00afedd4"></a> `00afedd4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afedd8"></a> `00afedd8` | `c8 22 01 f9` | str x8,[x22, #0x240] | `FALL_THROUGH`
<a id="insn-00afeddc"></a> `00afeddc` | `08 07 80 52` | mov w8,#0x38 | `FALL_THROUGH`
<a id="insn-00afede0"></a> `00afede0` | `08 57 08 9b` | madd x8,x24,x8,x21 | `FALL_THROUGH`
<a id="insn-00afede4"></a> `00afede4` | `08 c9 34 8b` | add x8,x8,w20, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00afede8"></a> `00afede8` | `00 2d 40 b9` | ldr w0,[x8, #0x2c] | `FALL_THROUGH`
<a id="insn-00afedec"></a> `00afedec` | `99 ff ff 17` | b 0x00afec50 | `UNCONDITIONAL_JUMP`
<a id="insn-00afedf0"></a> `00afedf0` | `c8 2a 41 f9` | ldr x8,[x22, #0x250] | `FALL_THROUGH`
<a id="insn-00afedf4"></a> `00afedf4` | `e8 00 00 b5` | cbnz x8,0x00afee10 | `CONDITIONAL_JUMP`
<a id="insn-00afedf8"></a> `00afedf8` | `d9 42 09 91` | add x25,x22,#0x250 | `FALL_THROUGH`
<a id="insn-00afedfc"></a> `00afedfc` | `f5 03 19 aa` | mov x21,x25 | `FALL_THROUGH`
<a id="insn-00afee00"></a> `00afee00` | `0c 00 00 14` | b 0x00afee30 | `UNCONDITIONAL_JUMP`
<a id="insn-00afee04"></a> `00afee04` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00afee08"></a> `00afee08` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00afee0c"></a> `00afee0c` | `28 01 00 b4` | cbz x8,0x00afee30 | `CONDITIONAL_JUMP`
<a id="insn-00afee10"></a> `00afee10` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00afee14"></a> `00afee14` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00afee18"></a> `00afee18` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00afee1c"></a> `00afee1c` | `4c ff ff 54` | b.gt 0x00afee04 | `CONDITIONAL_JUMP`
<a id="insn-00afee20"></a> `00afee20` | `6a 03 00 54` | b.ge 0x00afee8c | `CONDITIONAL_JUMP`
<a id="insn-00afee24"></a> `00afee24` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00afee28"></a> `00afee28` | `48 ff ff b5` | cbnz x8,0x00afee10 | `CONDITIONAL_JUMP`
<a id="insn-00afee2c"></a> `00afee2c` | `b9 22 00 91` | add x25,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00afee30"></a> `00afee30` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00afee34"></a> `00afee34` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-00afee38"></a> `00afee38` | `16 64 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00afee3c"></a> `00afee3c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00afee40"></a> `00afee40` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00afee44"></a> `00afee44` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00afee48"></a> `00afee48` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00afee4c"></a> `00afee4c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00afee50"></a> `00afee50` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00afee54"></a> `00afee54` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00afee58"></a> `00afee58` | `1a 08 00 f9` | str x26,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afee5c"></a> `00afee5c` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00afee60"></a> `00afee60` | `c8 26 41 f9` | ldr x8,[x22, #0x248] | `FALL_THROUGH`
<a id="insn-00afee64"></a> `00afee64` | `13 20 00 b9` | str w19,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00afee68"></a> `00afee68` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afee6c"></a> `00afee6c` | `68 00 00 b4` | cbz x8,0x00afee78 | `CONDITIONAL_JUMP`
<a id="insn-00afee70"></a> `00afee70` | `c8 26 01 f9` | str x8,[x22, #0x248] | `FALL_THROUGH`
<a id="insn-00afee74"></a> `00afee74` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00afee78"></a> `00afee78` | `c0 2a 41 f9` | ldr x0,[x22, #0x250] | `FALL_THROUGH`
<a id="insn-00afee7c"></a> `00afee7c` | `4a f3 e4 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00afee80"></a> `00afee80` | `c8 2e 41 f9` | ldr x8,[x22, #0x258] | `FALL_THROUGH`
<a id="insn-00afee84"></a> `00afee84` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afee88"></a> `00afee88` | `c8 2e 01 f9` | str x8,[x22, #0x258] | `FALL_THROUGH`
<a id="insn-00afee8c"></a> `00afee8c` | `9b 49 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afee90"></a> `00afee90` | `19 f4 48 91` | add x25,x0,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-00afee94"></a> `00afee94` | `28 1f 41 f9` | ldr x8,[x25, #0x238] | `FALL_THROUGH`
<a id="insn-00afee98"></a> `00afee98` | `e8 00 00 b5` | cbnz x8,0x00afeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00afee9c"></a> `00afee9c` | `3a e3 08 91` | add x26,x25,#0x238 | `FALL_THROUGH`
<a id="insn-00afeea0"></a> `00afeea0` | `f6 03 1a aa` | mov x22,x26 | `FALL_THROUGH`
<a id="insn-00afeea4"></a> `00afeea4` | `0c 00 00 14` | b 0x00afeed4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afeea8"></a> `00afeea8` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00afeeac"></a> `00afeeac` | `fa 03 16 aa` | mov x26,x22 | `FALL_THROUGH`
<a id="insn-00afeeb0"></a> `00afeeb0` | `28 01 00 b4` | cbz x8,0x00afeed4 | `CONDITIONAL_JUMP`
<a id="insn-00afeeb4"></a> `00afeeb4` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00afeeb8"></a> `00afeeb8` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00afeebc"></a> `00afeebc` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00afeec0"></a> `00afeec0` | `4c ff ff 54` | b.gt 0x00afeea8 | `CONDITIONAL_JUMP`
<a id="insn-00afeec4"></a> `00afeec4` | `6a 03 00 54` | b.ge 0x00afef30 | `CONDITIONAL_JUMP`
<a id="insn-00afeec8"></a> `00afeec8` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00afeecc"></a> `00afeecc` | `48 ff ff b5` | cbnz x8,0x00afeeb4 | `CONDITIONAL_JUMP`
<a id="insn-00afeed0"></a> `00afeed0` | `da 22 00 91` | add x26,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00afeed4"></a> `00afeed4` | `00 52 80 52` | mov w0,#0x290 | `FALL_THROUGH`
<a id="insn-00afeed8"></a> `00afeed8` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00afeedc"></a> `00afeedc` | `ed 63 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00afeee0"></a> `00afeee0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00afeee4"></a> `00afeee4` | `13 1c 00 b9` | str w19,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00afeee8"></a> `00afeee8` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00afeeec"></a> `00afeeec` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00afeef0"></a> `00afeef0` | `82 4d 80 52` | mov w2,#0x26c | `FALL_THROUGH`
<a id="insn-00afeef4"></a> `00afeef4` | `67 64 05 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-00afeef8"></a> `00afeef8` | `df 7e 00 a9` | stp xzr,xzr,[x22] | `FALL_THROUGH`
<a id="insn-00afeefc"></a> `00afeefc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00afef00"></a> `00afef00` | `db 0a 00 f9` | str x27,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00afef04"></a> `00afef04` | `56 03 00 f9` | str x22,[x26] | `FALL_THROUGH`
<a id="insn-00afef08"></a> `00afef08` | `28 1b 41 f9` | ldr x8,[x25, #0x230] | `FALL_THROUGH`
<a id="insn-00afef0c"></a> `00afef0c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afef10"></a> `00afef10` | `68 00 00 b4` | cbz x8,0x00afef1c | `CONDITIONAL_JUMP`
<a id="insn-00afef14"></a> `00afef14` | `28 1b 01 f9` | str x8,[x25, #0x230] | `FALL_THROUGH`
<a id="insn-00afef18"></a> `00afef18` | `41 03 40 f9` | ldr x1,[x26] | `FALL_THROUGH`
<a id="insn-00afef1c"></a> `00afef1c` | `20 1f 41 f9` | ldr x0,[x25, #0x238] | `FALL_THROUGH`
<a id="insn-00afef20"></a> `00afef20` | `21 f3 e4 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00afef24"></a> `00afef24` | `28 23 41 f9` | ldr x8,[x25, #0x240] | `FALL_THROUGH`
<a id="insn-00afef28"></a> `00afef28` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afef2c"></a> `00afef2c` | `28 23 01 f9` | str x8,[x25, #0x240] | `FALL_THROUGH`
<a id="insn-00afef30"></a> `00afef30` | `08 07 80 52` | mov w8,#0x38 | `FALL_THROUGH`
<a id="insn-00afef34"></a> `00afef34` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-00afef38"></a> `00afef38` | `09 5b 08 9b` | madd x9,x24,x8,x22 | `FALL_THROUGH`
<a id="insn-00afef3c"></a> `00afef3c` | `48 0f 43 f8` | ldr x8,[x26, #0x30]! | `FALL_THROUGH`
<a id="insn-00afef40"></a> `00afef40` | `39 25 40 b9` | ldr w25,[x9, #0x24] | `FALL_THROUGH`
<a id="insn-00afef44"></a> `00afef44` | `c8 00 00 b5` | cbnz x8,0x00afef5c | `CONDITIONAL_JUMP`
<a id="insn-00afef48"></a> `00afef48` | `f6 03 1a aa` | mov x22,x26 | `FALL_THROUGH`
<a id="insn-00afef4c"></a> `00afef4c` | `0d 00 00 14` | b 0x00afef80 | `UNCONDITIONAL_JUMP`
<a id="insn-00afef50"></a> `00afef50` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00afef54"></a> `00afef54` | `fa 03 16 aa` | mov x26,x22 | `FALL_THROUGH`
<a id="insn-00afef58"></a> `00afef58` | `48 01 00 b4` | cbz x8,0x00afef80 | `CONDITIONAL_JUMP`
<a id="insn-00afef5c"></a> `00afef5c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00afef60"></a> `00afef60` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00afef64"></a> `00afef64` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00afef68"></a> `00afef68` | `4b ff ff 54` | b.lt 0x00afef50 | `CONDITIONAL_JUMP`
<a id="insn-00afef6c"></a> `00afef6c` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00afef70"></a> `00afef70` | `ea 02 00 54` | b.ge 0x00afefcc | `CONDITIONAL_JUMP`
<a id="insn-00afef74"></a> `00afef74` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00afef78"></a> `00afef78` | `28 ff ff b5` | cbnz x8,0x00afef5c | `CONDITIONAL_JUMP`
<a id="insn-00afef7c"></a> `00afef7c` | `da 22 00 91` | add x26,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00afef80"></a> `00afef80` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00afef84"></a> `00afef84` | `fb 03 16 aa` | mov x27,x22 | `FALL_THROUGH`
<a id="insn-00afef88"></a> `00afef88` | `c2 63 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00afef8c"></a> `00afef8c` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00afef90"></a> `00afef90` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00afef94"></a> `00afef94` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00afef98"></a> `00afef98` | `1b 08 00 f9` | str x27,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afef9c"></a> `00afef9c` | `40 03 00 f9` | str x0,[x26] | `FALL_THROUGH`
<a id="insn-00afefa0"></a> `00afefa0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00afefa4"></a> `00afefa4` | `19 fc 03 29` | stp w25,wzr,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00afefa8"></a> `00afefa8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00afefac"></a> `00afefac` | `68 00 00 b4` | cbz x8,0x00afefb8 | `CONDITIONAL_JUMP`
<a id="insn-00afefb0"></a> `00afefb0` | `a8 16 00 f9` | str x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00afefb4"></a> `00afefb4` | `41 03 40 f9` | ldr x1,[x26] | `FALL_THROUGH`
<a id="insn-00afefb8"></a> `00afefb8` | `a0 1a 40 f9` | ldr x0,[x21, #0x30] | `FALL_THROUGH`
<a id="insn-00afefbc"></a> `00afefbc` | `fa f2 e4 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00afefc0"></a> `00afefc0` | `a8 1e 40 f9` | ldr x8,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00afefc4"></a> `00afefc4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afefc8"></a> `00afefc8` | `a8 1e 00 f9` | str x8,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00afefcc"></a> `00afefcc` | `d6 22 40 b9` | ldr w22,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00afefd0"></a> `00afefd0` | `4a 49 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afefd4"></a> `00afefd4` | `19 f4 48 91` | add x25,x0,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-00afefd8"></a> `00afefd8` | `28 1f 41 f9` | ldr x8,[x25, #0x238] | `FALL_THROUGH`
<a id="insn-00afefdc"></a> `00afefdc` | `e8 00 00 b5` | cbnz x8,0x00afeff8 | `CONDITIONAL_JUMP`
<a id="insn-00afefe0"></a> `00afefe0` | `3a e3 08 91` | add x26,x25,#0x238 | `FALL_THROUGH`
<a id="insn-00afefe4"></a> `00afefe4` | `f5 03 1a aa` | mov x21,x26 | `FALL_THROUGH`
<a id="insn-00afefe8"></a> `00afefe8` | `0c 00 00 14` | b 0x00aff018 | `UNCONDITIONAL_JUMP`
<a id="insn-00afefec"></a> `00afefec` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00afeff0"></a> `00afeff0` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-00afeff4"></a> `00afeff4` | `28 01 00 b4` | cbz x8,0x00aff018 | `CONDITIONAL_JUMP`
<a id="insn-00afeff8"></a> `00afeff8` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00afeffc"></a> `00afeffc` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aff000"></a> `00aff000` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00aff004"></a> `00aff004` | `4c ff ff 54` | b.gt 0x00afefec | `CONDITIONAL_JUMP`
<a id="insn-00aff008"></a> `00aff008` | `6a 03 00 54` | b.ge 0x00aff074 | `CONDITIONAL_JUMP`
<a id="insn-00aff00c"></a> `00aff00c` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00aff010"></a> `00aff010` | `48 ff ff b5` | cbnz x8,0x00afeff8 | `CONDITIONAL_JUMP`
<a id="insn-00aff014"></a> `00aff014` | `ba 22 00 91` | add x26,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00aff018"></a> `00aff018` | `00 52 80 52` | mov w0,#0x290 | `FALL_THROUGH`
<a id="insn-00aff01c"></a> `00aff01c` | `fb 03 15 aa` | mov x27,x21 | `FALL_THROUGH`
<a id="insn-00aff020"></a> `00aff020` | `9c 63 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00aff024"></a> `00aff024` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aff028"></a> `00aff028` | `13 1c 00 b9` | str w19,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00aff02c"></a> `00aff02c` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00aff030"></a> `00aff030` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aff034"></a> `00aff034` | `82 4d 80 52` | mov w2,#0x26c | `FALL_THROUGH`
<a id="insn-00aff038"></a> `00aff038` | `16 64 05 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-00aff03c"></a> `00aff03c` | `bf 7e 00 a9` | stp xzr,xzr,[x21] | `FALL_THROUGH`
<a id="insn-00aff040"></a> `00aff040` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00aff044"></a> `00aff044` | `bb 0a 00 f9` | str x27,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00aff048"></a> `00aff048` | `55 03 00 f9` | str x21,[x26] | `FALL_THROUGH`
<a id="insn-00aff04c"></a> `00aff04c` | `28 1b 41 f9` | ldr x8,[x25, #0x230] | `FALL_THROUGH`
<a id="insn-00aff050"></a> `00aff050` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aff054"></a> `00aff054` | `68 00 00 b4` | cbz x8,0x00aff060 | `CONDITIONAL_JUMP`
<a id="insn-00aff058"></a> `00aff058` | `28 1b 01 f9` | str x8,[x25, #0x230] | `FALL_THROUGH`
<a id="insn-00aff05c"></a> `00aff05c` | `41 03 40 f9` | ldr x1,[x26] | `FALL_THROUGH`
<a id="insn-00aff060"></a> `00aff060` | `20 1f 41 f9` | ldr x0,[x25, #0x238] | `FALL_THROUGH`
<a id="insn-00aff064"></a> `00aff064` | `d0 f2 e4 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00aff068"></a> `00aff068` | `28 23 41 f9` | ldr x8,[x25, #0x240] | `FALL_THROUGH`
<a id="insn-00aff06c"></a> `00aff06c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aff070"></a> `00aff070` | `28 23 01 f9` | str x8,[x25, #0x240] | `FALL_THROUGH`
<a id="insn-00aff074"></a> `00aff074` | `08 07 80 52` | mov w8,#0x38 | `FALL_THROUGH`
<a id="insn-00aff078"></a> `00aff078` | `99 7e 40 93` | sxtw x25,w20 | `FALL_THROUGH`
<a id="insn-00aff07c"></a> `00aff07c` | `08 57 08 9b` | madd x8,x24,x8,x21 | `FALL_THROUGH`
<a id="insn-00aff080"></a> `00aff080` | `08 c9 34 8b` | add x8,x8,w20, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00aff084"></a> `00aff084` | `08 2d 40 b9` | ldr w8,[x8, #0x2c] | `FALL_THROUGH`
<a id="insn-00aff088"></a> `00aff088` | `e8 07 00 b9` | str w8,[sp, #0x4] | `FALL_THROUGH`
<a id="insn-00aff08c"></a> `00aff08c` | `1b 49 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aff090"></a> `00aff090` | `1a f4 48 91` | add x26,x0,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-00aff094"></a> `00aff094` | `48 1f 41 f9` | ldr x8,[x26, #0x238] | `FALL_THROUGH`
<a id="insn-00aff098"></a> `00aff098` | `e8 00 00 b5` | cbnz x8,0x00aff0b4 | `CONDITIONAL_JUMP`
<a id="insn-00aff09c"></a> `00aff09c` | `5b e3 08 91` | add x27,x26,#0x238 | `FALL_THROUGH`
<a id="insn-00aff0a0"></a> `00aff0a0` | `f4 03 1b aa` | mov x20,x27 | `FALL_THROUGH`
<a id="insn-00aff0a4"></a> `00aff0a4` | `0c 00 00 14` | b 0x00aff0d4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aff0a8"></a> `00aff0a8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aff0ac"></a> `00aff0ac` | `fb 03 14 aa` | mov x27,x20 | `FALL_THROUGH`
<a id="insn-00aff0b0"></a> `00aff0b0` | `28 01 00 b4` | cbz x8,0x00aff0d4 | `CONDITIONAL_JUMP`
<a id="insn-00aff0b4"></a> `00aff0b4` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aff0b8"></a> `00aff0b8` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aff0bc"></a> `00aff0bc` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00aff0c0"></a> `00aff0c0` | `4c ff ff 54` | b.gt 0x00aff0a8 | `CONDITIONAL_JUMP`
<a id="insn-00aff0c4"></a> `00aff0c4` | `6a 03 00 54` | b.ge 0x00aff130 | `CONDITIONAL_JUMP`
<a id="insn-00aff0c8"></a> `00aff0c8` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aff0cc"></a> `00aff0cc` | `48 ff ff b5` | cbnz x8,0x00aff0b4 | `CONDITIONAL_JUMP`
<a id="insn-00aff0d0"></a> `00aff0d0` | `9b 22 00 91` | add x27,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aff0d4"></a> `00aff0d4` | `00 52 80 52` | mov w0,#0x290 | `FALL_THROUGH`
<a id="insn-00aff0d8"></a> `00aff0d8` | `fc 03 14 aa` | mov x28,x20 | `FALL_THROUGH`
<a id="insn-00aff0dc"></a> `00aff0dc` | `6d 63 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00aff0e0"></a> `00aff0e0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aff0e4"></a> `00aff0e4` | `13 1c 00 b9` | str w19,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00aff0e8"></a> `00aff0e8` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00aff0ec"></a> `00aff0ec` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aff0f0"></a> `00aff0f0` | `82 4d 80 52` | mov w2,#0x26c | `FALL_THROUGH`
<a id="insn-00aff0f4"></a> `00aff0f4` | `e7 63 05 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-00aff0f8"></a> `00aff0f8` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00aff0fc"></a> `00aff0fc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00aff100"></a> `00aff100` | `9c 0a 00 f9` | str x28,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aff104"></a> `00aff104` | `74 03 00 f9` | str x20,[x27] | `FALL_THROUGH`
<a id="insn-00aff108"></a> `00aff108` | `48 1b 41 f9` | ldr x8,[x26, #0x230] | `FALL_THROUGH`
<a id="insn-00aff10c"></a> `00aff10c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aff110"></a> `00aff110` | `68 00 00 b4` | cbz x8,0x00aff11c | `CONDITIONAL_JUMP`
<a id="insn-00aff114"></a> `00aff114` | `48 1b 01 f9` | str x8,[x26, #0x230] | `FALL_THROUGH`
<a id="insn-00aff118"></a> `00aff118` | `61 03 40 f9` | ldr x1,[x27] | `FALL_THROUGH`
<a id="insn-00aff11c"></a> `00aff11c` | `40 1f 41 f9` | ldr x0,[x26, #0x238] | `FALL_THROUGH`
<a id="insn-00aff120"></a> `00aff120` | `a1 f2 e4 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00aff124"></a> `00aff124` | `48 23 41 f9` | ldr x8,[x26, #0x240] | `FALL_THROUGH`
<a id="insn-00aff128"></a> `00aff128` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aff12c"></a> `00aff12c` | `48 23 01 f9` | str x8,[x26, #0x240] | `FALL_THROUGH`
<a id="insn-00aff130"></a> `00aff130` | `08 07 80 52` | mov w8,#0x38 | `FALL_THROUGH`
<a id="insn-00aff134"></a> `00aff134` | `08 53 08 9b` | madd x8,x24,x8,x20 | `FALL_THROUGH`
<a id="insn-00aff138"></a> `00aff138` | `08 09 19 8b` | add x8,x8,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00aff13c"></a> `00aff13c` | `1a 3d 40 b9` | ldr w26,[x8, #0x3c] | `FALL_THROUGH`
<a id="insn-00aff140"></a> `00aff140` | `ee 48 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aff144"></a> `00aff144` | `1b f4 48 91` | add x27,x0,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-00aff148"></a> `00aff148` | `68 1f 41 f9` | ldr x8,[x27, #0x238] | `FALL_THROUGH`
<a id="insn-00aff14c"></a> `00aff14c` | `e8 00 00 b5` | cbnz x8,0x00aff168 | `CONDITIONAL_JUMP`
<a id="insn-00aff150"></a> `00aff150` | `7c e3 08 91` | add x28,x27,#0x238 | `FALL_THROUGH`
<a id="insn-00aff154"></a> `00aff154` | `f4 03 1c aa` | mov x20,x28 | `FALL_THROUGH`
<a id="insn-00aff158"></a> `00aff158` | `0c 00 00 14` | b 0x00aff188 | `UNCONDITIONAL_JUMP`
<a id="insn-00aff15c"></a> `00aff15c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aff160"></a> `00aff160` | `fc 03 14 aa` | mov x28,x20 | `FALL_THROUGH`
<a id="insn-00aff164"></a> `00aff164` | `28 01 00 b4` | cbz x8,0x00aff188 | `CONDITIONAL_JUMP`
<a id="insn-00aff168"></a> `00aff168` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aff16c"></a> `00aff16c` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aff170"></a> `00aff170` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00aff174"></a> `00aff174` | `4c ff ff 54` | b.gt 0x00aff15c | `CONDITIONAL_JUMP`
<a id="insn-00aff178"></a> `00aff178` | `6a 03 00 54` | b.ge 0x00aff1e4 | `CONDITIONAL_JUMP`
<a id="insn-00aff17c"></a> `00aff17c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aff180"></a> `00aff180` | `48 ff ff b5` | cbnz x8,0x00aff168 | `CONDITIONAL_JUMP`
<a id="insn-00aff184"></a> `00aff184` | `9c 22 00 91` | add x28,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aff188"></a> `00aff188` | `00 52 80 52` | mov w0,#0x290 | `FALL_THROUGH`
<a id="insn-00aff18c"></a> `00aff18c` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-00aff190"></a> `00aff190` | `40 63 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00aff194"></a> `00aff194` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aff198"></a> `00aff198` | `13 1c 00 b9` | str w19,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00aff19c"></a> `00aff19c` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00aff1a0"></a> `00aff1a0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aff1a4"></a> `00aff1a4` | `82 4d 80 52` | mov w2,#0x26c | `FALL_THROUGH`
<a id="insn-00aff1a8"></a> `00aff1a8` | `ba 63 05 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-00aff1ac"></a> `00aff1ac` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00aff1b0"></a> `00aff1b0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00aff1b4"></a> `00aff1b4` | `95 0a 00 f9` | str x21,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aff1b8"></a> `00aff1b8` | `94 03 00 f9` | str x20,[x28] | `FALL_THROUGH`
<a id="insn-00aff1bc"></a> `00aff1bc` | `68 1b 41 f9` | ldr x8,[x27, #0x230] | `FALL_THROUGH`
<a id="insn-00aff1c0"></a> `00aff1c0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aff1c4"></a> `00aff1c4` | `68 00 00 b4` | cbz x8,0x00aff1d0 | `CONDITIONAL_JUMP`
<a id="insn-00aff1c8"></a> `00aff1c8` | `68 1b 01 f9` | str x8,[x27, #0x230] | `FALL_THROUGH`
<a id="insn-00aff1cc"></a> `00aff1cc` | `81 03 40 f9` | ldr x1,[x28] | `FALL_THROUGH`
<a id="insn-00aff1d0"></a> `00aff1d0` | `60 1f 41 f9` | ldr x0,[x27, #0x238] | `FALL_THROUGH`
<a id="insn-00aff1d4"></a> `00aff1d4` | `74 f2 e4 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00aff1d8"></a> `00aff1d8` | `68 23 41 f9` | ldr x8,[x27, #0x240] | `FALL_THROUGH`
<a id="insn-00aff1dc"></a> `00aff1dc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aff1e0"></a> `00aff1e0` | `68 23 01 f9` | str x8,[x27, #0x240] | `FALL_THROUGH`
<a id="insn-00aff1e4"></a> `00aff1e4` | `08 07 80 52` | mov w8,#0x38 | `FALL_THROUGH`
<a id="insn-00aff1e8"></a> `00aff1e8` | `c9 06 00 51` | sub w9,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00aff1ec"></a> `00aff1ec` | `08 53 08 9b` | madd x8,x24,x8,x20 | `FALL_THROUGH`
<a id="insn-00aff1f0"></a> `00aff1f0` | `08 09 19 8b` | add x8,x8,x25, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00aff1f4"></a> `00aff1f4` | `08 2d 40 b9` | ldr w8,[x8, #0x2c] | `FALL_THROUGH`
<a id="insn-00aff1f8"></a> `00aff1f8` | `48 03 08 4b` | sub w8,w26,w8 | `FALL_THROUGH`
<a id="insn-00aff1fc"></a> `00aff1fc` | `16 7d 09 1b` | mul w22,w8,w9 | `FALL_THROUGH`
<a id="insn-00aff200"></a> `00aff200` | `be 48 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aff204"></a> `00aff204` | `19 f4 48 91` | add x25,x0,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-00aff208"></a> `00aff208` | `28 1f 41 f9` | ldr x8,[x25, #0x238] | `FALL_THROUGH`
<a id="insn-00aff20c"></a> `00aff20c` | `e8 00 00 b5` | cbnz x8,0x00aff228 | `CONDITIONAL_JUMP`
<a id="insn-00aff210"></a> `00aff210` | `3a e3 08 91` | add x26,x25,#0x238 | `FALL_THROUGH`
<a id="insn-00aff214"></a> `00aff214` | `f4 03 1a aa` | mov x20,x26 | `FALL_THROUGH`
<a id="insn-00aff218"></a> `00aff218` | `0c 00 00 14` | b 0x00aff248 | `UNCONDITIONAL_JUMP`
<a id="insn-00aff21c"></a> `00aff21c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aff220"></a> `00aff220` | `fa 03 14 aa` | mov x26,x20 | `FALL_THROUGH`
<a id="insn-00aff224"></a> `00aff224` | `28 01 00 b4` | cbz x8,0x00aff248 | `CONDITIONAL_JUMP`
<a id="insn-00aff228"></a> `00aff228` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aff22c"></a> `00aff22c` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00aff230"></a> `00aff230` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00aff234"></a> `00aff234` | `4c ff ff 54` | b.gt 0x00aff21c | `CONDITIONAL_JUMP`
<a id="insn-00aff238"></a> `00aff238` | `6a 03 00 54` | b.ge 0x00aff2a4 | `CONDITIONAL_JUMP`
<a id="insn-00aff23c"></a> `00aff23c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aff240"></a> `00aff240` | `48 ff ff b5` | cbnz x8,0x00aff228 | `CONDITIONAL_JUMP`
<a id="insn-00aff244"></a> `00aff244` | `9a 22 00 91` | add x26,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aff248"></a> `00aff248` | `00 52 80 52` | mov w0,#0x290 | `FALL_THROUGH`
<a id="insn-00aff24c"></a> `00aff24c` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-00aff250"></a> `00aff250` | `10 63 05 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00aff254"></a> `00aff254` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aff258"></a> `00aff258` | `13 1c 00 b9` | str w19,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00aff25c"></a> `00aff25c` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00aff260"></a> `00aff260` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aff264"></a> `00aff264` | `82 4d 80 52` | mov w2,#0x26c | `FALL_THROUGH`
<a id="insn-00aff268"></a> `00aff268` | `8a 63 05 94` | bl 0x00c58090 | `UNCONDITIONAL_CALL`
<a id="insn-00aff26c"></a> `00aff26c` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00aff270"></a> `00aff270` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00aff274"></a> `00aff274` | `95 0a 00 f9` | str x21,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00aff278"></a> `00aff278` | `54 03 00 f9` | str x20,[x26] | `FALL_THROUGH`
<a id="insn-00aff27c"></a> `00aff27c` | `28 1b 41 f9` | ldr x8,[x25, #0x230] | `FALL_THROUGH`
<a id="insn-00aff280"></a> `00aff280` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aff284"></a> `00aff284` | `68 00 00 b4` | cbz x8,0x00aff290 | `CONDITIONAL_JUMP`
<a id="insn-00aff288"></a> `00aff288` | `28 1b 01 f9` | str x8,[x25, #0x230] | `FALL_THROUGH`
<a id="insn-00aff28c"></a> `00aff28c` | `41 03 40 f9` | ldr x1,[x26] | `FALL_THROUGH`
<a id="insn-00aff290"></a> `00aff290` | `20 1f 41 f9` | ldr x0,[x25, #0x238] | `FALL_THROUGH`
<a id="insn-00aff294"></a> `00aff294` | `44 f2 e4 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-00aff298"></a> `00aff298` | `28 23 41 f9` | ldr x8,[x25, #0x240] | `FALL_THROUGH`
<a id="insn-00aff29c"></a> `00aff29c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aff2a0"></a> `00aff2a0` | `28 23 01 f9` | str x8,[x25, #0x240] | `FALL_THROUGH`
<a id="insn-00aff2a4"></a> `00aff2a4` | `08 07 80 52` | mov w8,#0x38 | `FALL_THROUGH`
<a id="insn-00aff2a8"></a> `00aff2a8` | `e9 07 40 b9` | ldr w9,[sp, #0x4] | `FALL_THROUGH`
<a id="insn-00aff2ac"></a> `00aff2ac` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00aff2b0"></a> `00aff2b0` | `08 53 08 9b` | madd x8,x24,x8,x20 | `FALL_THROUGH`
<a id="insn-00aff2b4"></a> `00aff2b4` | `08 29 40 b9` | ldr w8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aff2b8"></a> `00aff2b8` | `08 05 00 51` | sub w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aff2bc"></a> `00aff2bc` | `c8 0e c8 1a` | sdiv w8,w22,w8 | `FALL_THROUGH`
<a id="insn-00aff2c0"></a> `00aff2c0` | `00 01 09 0b` | add w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00aff2c4"></a> `00aff2c4` | `63 fe ff 17` | b 0x00afec50 | `UNCONDITIONAL_JUMP`
<a id="insn-00aff2c8"></a> `00aff2c8` | `06 63 05 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afeae8`](#insn-00afeae8) 範囲 `[['00afeae8', '00afeb27']]`
  - `CONDITIONAL_JUMP` [`00afeb24`](#insn-00afeb24) → [`00afec4c`](#insn-00afec4c)
  - `FALL_THROUGH` [`00afeb24`](#insn-00afeb24) → [`00afeb28`](#insn-00afeb28)
- ブロック [`00afeb28`](#insn-00afeb28) 範囲 `[['00afeb28', '00afeb3f']]`
  - `CONDITIONAL_JUMP` [`00afeb3c`](#insn-00afeb3c) → [`00afeb80`](#insn-00afeb80)
  - `FALL_THROUGH` [`00afeb3c`](#insn-00afeb3c) → [`00afeb40`](#insn-00afeb40)
- ブロック [`00afeb40`](#insn-00afeb40) 範囲 `[['00afeb40', '00afeb67']]`
  - `CONDITIONAL_JUMP` [`00afeb64`](#insn-00afeb64) → [`00afec4c`](#insn-00afec4c)
  - `FALL_THROUGH` [`00afeb64`](#insn-00afeb64) → [`00afeb68`](#insn-00afeb68)
- ブロック [`00afeb68`](#insn-00afeb68) 範囲 `[['00afeb68', '00afeb7f']]`
  - `UNCONDITIONAL_JUMP` [`00afeb7c`](#insn-00afeb7c) → [`00afec50`](#insn-00afec50)
- ブロック [`00afeb80`](#insn-00afeb80) 範囲 `[['00afeb80', '00afeb87']]`
  - `FALL_THROUGH` [`00afeb84`](#insn-00afeb84) → [`00afeb88`](#insn-00afeb88)
- ブロック [`00afeb88`](#insn-00afeb88) 範囲 `[['00afeb88', '00afeb97']]`
  - `CONDITIONAL_JUMP` [`00afeb94`](#insn-00afeb94) → [`00afebb0`](#insn-00afebb0)
  - `FALL_THROUGH` [`00afeb94`](#insn-00afeb94) → [`00afeb98`](#insn-00afeb98)
- ブロック [`00afeb98`](#insn-00afeb98) 範囲 `[['00afeb98', '00afeba3']]`
  - `UNCONDITIONAL_JUMP` [`00afeba0`](#insn-00afeba0) → [`00afebd0`](#insn-00afebd0)
- ブロック [`00afeba4`](#insn-00afeba4) 範囲 `[['00afeba4', '00afebaf']]`
  - `CONDITIONAL_JUMP` [`00afebac`](#insn-00afebac) → [`00afebd0`](#insn-00afebd0)
  - `FALL_THROUGH` [`00afebac`](#insn-00afebac) → [`00afebb0`](#insn-00afebb0)
- ブロック [`00afebb0`](#insn-00afebb0) 範囲 `[['00afebb0', '00afebbf']]`
  - `CONDITIONAL_JUMP` [`00afebbc`](#insn-00afebbc) → [`00afeba4`](#insn-00afeba4)
  - `FALL_THROUGH` [`00afebbc`](#insn-00afebbc) → [`00afebc0`](#insn-00afebc0)
- ブロック [`00afebc0`](#insn-00afebc0) 範囲 `[['00afebc0', '00afebc3']]`
  - `CONDITIONAL_JUMP` [`00afebc0`](#insn-00afebc0) → [`00afec2c`](#insn-00afec2c)
  - `FALL_THROUGH` [`00afebc0`](#insn-00afebc0) → [`00afebc4`](#insn-00afebc4)
- ブロック [`00afebc4`](#insn-00afebc4) 範囲 `[['00afebc4', '00afebcb']]`
  - `CONDITIONAL_JUMP` [`00afebc8`](#insn-00afebc8) → [`00afebb0`](#insn-00afebb0)
  - `FALL_THROUGH` [`00afebc8`](#insn-00afebc8) → [`00afebcc`](#insn-00afebcc)
- ブロック [`00afebcc`](#insn-00afebcc) 範囲 `[['00afebcc', '00afebcf']]`
  - `FALL_THROUGH` [`00afebcc`](#insn-00afebcc) → [`00afebd0`](#insn-00afebd0)
- ブロック [`00afebd0`](#insn-00afebd0) 範囲 `[['00afebd0', '00afec0f']]`
  - `CONDITIONAL_JUMP` [`00afec0c`](#insn-00afec0c) → [`00afec18`](#insn-00afec18)
  - `FALL_THROUGH` [`00afec0c`](#insn-00afec0c) → [`00afec10`](#insn-00afec10)
- ブロック [`00afec10`](#insn-00afec10) 範囲 `[['00afec10', '00afec17']]`
  - `FALL_THROUGH` [`00afec14`](#insn-00afec14) → [`00afec18`](#insn-00afec18)
- ブロック [`00afec18`](#insn-00afec18) 範囲 `[['00afec18', '00afec2b']]`
  - `FALL_THROUGH` [`00afec28`](#insn-00afec28) → [`00afec2c`](#insn-00afec2c)
- ブロック [`00afec2c`](#insn-00afec2c) 範囲 `[['00afec2c', '00afec3f']]`
  - `CONDITIONAL_JUMP` [`00afec3c`](#insn-00afec3c) → [`00afec80`](#insn-00afec80)
  - `FALL_THROUGH` [`00afec3c`](#insn-00afec3c) → [`00afec40`](#insn-00afec40)
- ブロック [`00afec40`](#insn-00afec40) 範囲 `[['00afec40', '00afec4b']]`
  - `CONDITIONAL_JUMP` [`00afec48`](#insn-00afec48) → [`00afeb88`](#insn-00afeb88)
  - `FALL_THROUGH` [`00afec48`](#insn-00afec48) → [`00afec4c`](#insn-00afec4c)
- ブロック [`00afec4c`](#insn-00afec4c) 範囲 `[['00afec4c', '00afec4f']]`
  - `FALL_THROUGH` [`00afec4c`](#insn-00afec4c) → [`00afec50`](#insn-00afec50)
- ブロック [`00afec50`](#insn-00afec50) 範囲 `[['00afec50', '00afec5f']]`
  - `CONDITIONAL_JUMP` [`00afec5c`](#insn-00afec5c) → [`00aff2c8`](#insn-00aff2c8)
  - `FALL_THROUGH` [`00afec5c`](#insn-00afec5c) → [`00afec60`](#insn-00afec60)
- ブロック [`00afec60`](#insn-00afec60) 範囲 `[['00afec60', '00afec7f']]`
- ブロック [`00afec80`](#insn-00afec80) 範囲 `[['00afec80', '00afec8f']]`
  - `CONDITIONAL_JUMP` [`00afec8c`](#insn-00afec8c) → [`00afeca8`](#insn-00afeca8)
  - `FALL_THROUGH` [`00afec8c`](#insn-00afec8c) → [`00afec90`](#insn-00afec90)
- ブロック [`00afec90`](#insn-00afec90) 範囲 `[['00afec90', '00afec9b']]`
  - `UNCONDITIONAL_JUMP` [`00afec98`](#insn-00afec98) → [`00afecc8`](#insn-00afecc8)
- ブロック [`00afec9c`](#insn-00afec9c) 範囲 `[['00afec9c', '00afeca7']]`
  - `CONDITIONAL_JUMP` [`00afeca4`](#insn-00afeca4) → [`00afecc8`](#insn-00afecc8)
  - `FALL_THROUGH` [`00afeca4`](#insn-00afeca4) → [`00afeca8`](#insn-00afeca8)
- ブロック [`00afeca8`](#insn-00afeca8) 範囲 `[['00afeca8', '00afecb7']]`
  - `CONDITIONAL_JUMP` [`00afecb4`](#insn-00afecb4) → [`00afec9c`](#insn-00afec9c)
  - `FALL_THROUGH` [`00afecb4`](#insn-00afecb4) → [`00afecb8`](#insn-00afecb8)
- ブロック [`00afecb8`](#insn-00afecb8) 範囲 `[['00afecb8', '00afecbb']]`
  - `CONDITIONAL_JUMP` [`00afecb8`](#insn-00afecb8) → [`00afed24`](#insn-00afed24)
  - `FALL_THROUGH` [`00afecb8`](#insn-00afecb8) → [`00afecbc`](#insn-00afecbc)
- ブロック [`00afecbc`](#insn-00afecbc) 範囲 `[['00afecbc', '00afecc3']]`
  - `CONDITIONAL_JUMP` [`00afecc0`](#insn-00afecc0) → [`00afeca8`](#insn-00afeca8)
  - `FALL_THROUGH` [`00afecc0`](#insn-00afecc0) → [`00afecc4`](#insn-00afecc4)
- ブロック [`00afecc4`](#insn-00afecc4) 範囲 `[['00afecc4', '00afecc7']]`
  - `FALL_THROUGH` [`00afecc4`](#insn-00afecc4) → [`00afecc8`](#insn-00afecc8)
- ブロック [`00afecc8`](#insn-00afecc8) 範囲 `[['00afecc8', '00afed07']]`
  - `CONDITIONAL_JUMP` [`00afed04`](#insn-00afed04) → [`00afed10`](#insn-00afed10)
  - `FALL_THROUGH` [`00afed04`](#insn-00afed04) → [`00afed08`](#insn-00afed08)
- ブロック [`00afed08`](#insn-00afed08) 範囲 `[['00afed08', '00afed0f']]`
  - `FALL_THROUGH` [`00afed0c`](#insn-00afed0c) → [`00afed10`](#insn-00afed10)
- ブロック [`00afed10`](#insn-00afed10) 範囲 `[['00afed10', '00afed23']]`
  - `FALL_THROUGH` [`00afed20`](#insn-00afed20) → [`00afed24`](#insn-00afed24)
- ブロック [`00afed24`](#insn-00afed24) 範囲 `[['00afed24', '00afed3f']]`
  - `CONDITIONAL_JUMP` [`00afed3c`](#insn-00afed3c) → [`00afedf0`](#insn-00afedf0)
  - `FALL_THROUGH` [`00afed3c`](#insn-00afed3c) → [`00afed40`](#insn-00afed40)
- ブロック [`00afed40`](#insn-00afed40) 範囲 `[['00afed40', '00afed47']]`
  - `CONDITIONAL_JUMP` [`00afed44`](#insn-00afed44) → [`00afed60`](#insn-00afed60)
  - `FALL_THROUGH` [`00afed44`](#insn-00afed44) → [`00afed48`](#insn-00afed48)
- ブロック [`00afed48`](#insn-00afed48) 範囲 `[['00afed48', '00afed53']]`
  - `UNCONDITIONAL_JUMP` [`00afed50`](#insn-00afed50) → [`00afed80`](#insn-00afed80)
- ブロック [`00afed54`](#insn-00afed54) 範囲 `[['00afed54', '00afed5f']]`
  - `CONDITIONAL_JUMP` [`00afed5c`](#insn-00afed5c) → [`00afed80`](#insn-00afed80)
  - `FALL_THROUGH` [`00afed5c`](#insn-00afed5c) → [`00afed60`](#insn-00afed60)
- ブロック [`00afed60`](#insn-00afed60) 範囲 `[['00afed60', '00afed6f']]`
  - `CONDITIONAL_JUMP` [`00afed6c`](#insn-00afed6c) → [`00afed54`](#insn-00afed54)
  - `FALL_THROUGH` [`00afed6c`](#insn-00afed6c) → [`00afed70`](#insn-00afed70)
- ブロック [`00afed70`](#insn-00afed70) 範囲 `[['00afed70', '00afed73']]`
  - `CONDITIONAL_JUMP` [`00afed70`](#insn-00afed70) → [`00afeddc`](#insn-00afeddc)
  - `FALL_THROUGH` [`00afed70`](#insn-00afed70) → [`00afed74`](#insn-00afed74)
- ブロック [`00afed74`](#insn-00afed74) 範囲 `[['00afed74', '00afed7b']]`
  - `CONDITIONAL_JUMP` [`00afed78`](#insn-00afed78) → [`00afed60`](#insn-00afed60)
  - `FALL_THROUGH` [`00afed78`](#insn-00afed78) → [`00afed7c`](#insn-00afed7c)
- ブロック [`00afed7c`](#insn-00afed7c) 範囲 `[['00afed7c', '00afed7f']]`
  - `FALL_THROUGH` [`00afed7c`](#insn-00afed7c) → [`00afed80`](#insn-00afed80)
- ブロック [`00afed80`](#insn-00afed80) 範囲 `[['00afed80', '00afedbf']]`
  - `CONDITIONAL_JUMP` [`00afedbc`](#insn-00afedbc) → [`00afedc8`](#insn-00afedc8)
  - `FALL_THROUGH` [`00afedbc`](#insn-00afedbc) → [`00afedc0`](#insn-00afedc0)
- ブロック [`00afedc0`](#insn-00afedc0) 範囲 `[['00afedc0', '00afedc7']]`
  - `FALL_THROUGH` [`00afedc4`](#insn-00afedc4) → [`00afedc8`](#insn-00afedc8)
- ブロック [`00afedc8`](#insn-00afedc8) 範囲 `[['00afedc8', '00afeddb']]`
  - `FALL_THROUGH` [`00afedd8`](#insn-00afedd8) → [`00afeddc`](#insn-00afeddc)
- ブロック [`00afeddc`](#insn-00afeddc) 範囲 `[['00afeddc', '00afedef']]`
  - `UNCONDITIONAL_JUMP` [`00afedec`](#insn-00afedec) → [`00afec50`](#insn-00afec50)
- ブロック [`00afedf0`](#insn-00afedf0) 範囲 `[['00afedf0', '00afedf7']]`
  - `CONDITIONAL_JUMP` [`00afedf4`](#insn-00afedf4) → [`00afee10`](#insn-00afee10)
  - `FALL_THROUGH` [`00afedf4`](#insn-00afedf4) → [`00afedf8`](#insn-00afedf8)
- ブロック [`00afedf8`](#insn-00afedf8) 範囲 `[['00afedf8', '00afee03']]`
  - `UNCONDITIONAL_JUMP` [`00afee00`](#insn-00afee00) → [`00afee30`](#insn-00afee30)
- ブロック [`00afee04`](#insn-00afee04) 範囲 `[['00afee04', '00afee0f']]`
  - `CONDITIONAL_JUMP` [`00afee0c`](#insn-00afee0c) → [`00afee30`](#insn-00afee30)
  - `FALL_THROUGH` [`00afee0c`](#insn-00afee0c) → [`00afee10`](#insn-00afee10)
- ブロック [`00afee10`](#insn-00afee10) 範囲 `[['00afee10', '00afee1f']]`
  - `CONDITIONAL_JUMP` [`00afee1c`](#insn-00afee1c) → [`00afee04`](#insn-00afee04)
  - `FALL_THROUGH` [`00afee1c`](#insn-00afee1c) → [`00afee20`](#insn-00afee20)
- ブロック [`00afee20`](#insn-00afee20) 範囲 `[['00afee20', '00afee23']]`
  - `CONDITIONAL_JUMP` [`00afee20`](#insn-00afee20) → [`00afee8c`](#insn-00afee8c)
  - `FALL_THROUGH` [`00afee20`](#insn-00afee20) → [`00afee24`](#insn-00afee24)
- ブロック [`00afee24`](#insn-00afee24) 範囲 `[['00afee24', '00afee2b']]`
  - `CONDITIONAL_JUMP` [`00afee28`](#insn-00afee28) → [`00afee10`](#insn-00afee10)
  - `FALL_THROUGH` [`00afee28`](#insn-00afee28) → [`00afee2c`](#insn-00afee2c)
- ブロック [`00afee2c`](#insn-00afee2c) 範囲 `[['00afee2c', '00afee2f']]`
  - `FALL_THROUGH` [`00afee2c`](#insn-00afee2c) → [`00afee30`](#insn-00afee30)
- ブロック [`00afee30`](#insn-00afee30) 範囲 `[['00afee30', '00afee6f']]`
  - `CONDITIONAL_JUMP` [`00afee6c`](#insn-00afee6c) → [`00afee78`](#insn-00afee78)
  - `FALL_THROUGH` [`00afee6c`](#insn-00afee6c) → [`00afee70`](#insn-00afee70)
- ブロック [`00afee70`](#insn-00afee70) 範囲 `[['00afee70', '00afee77']]`
  - `FALL_THROUGH` [`00afee74`](#insn-00afee74) → [`00afee78`](#insn-00afee78)
- ブロック [`00afee78`](#insn-00afee78) 範囲 `[['00afee78', '00afee8b']]`
  - `FALL_THROUGH` [`00afee88`](#insn-00afee88) → [`00afee8c`](#insn-00afee8c)
- ブロック [`00afee8c`](#insn-00afee8c) 範囲 `[['00afee8c', '00afee9b']]`
  - `CONDITIONAL_JUMP` [`00afee98`](#insn-00afee98) → [`00afeeb4`](#insn-00afeeb4)
  - `FALL_THROUGH` [`00afee98`](#insn-00afee98) → [`00afee9c`](#insn-00afee9c)
- ブロック [`00afee9c`](#insn-00afee9c) 範囲 `[['00afee9c', '00afeea7']]`
  - `UNCONDITIONAL_JUMP` [`00afeea4`](#insn-00afeea4) → [`00afeed4`](#insn-00afeed4)
- ブロック [`00afeea8`](#insn-00afeea8) 範囲 `[['00afeea8', '00afeeb3']]`
  - `CONDITIONAL_JUMP` [`00afeeb0`](#insn-00afeeb0) → [`00afeed4`](#insn-00afeed4)
  - `FALL_THROUGH` [`00afeeb0`](#insn-00afeeb0) → [`00afeeb4`](#insn-00afeeb4)
- ブロック [`00afeeb4`](#insn-00afeeb4) 範囲 `[['00afeeb4', '00afeec3']]`
  - `CONDITIONAL_JUMP` [`00afeec0`](#insn-00afeec0) → [`00afeea8`](#insn-00afeea8)
  - `FALL_THROUGH` [`00afeec0`](#insn-00afeec0) → [`00afeec4`](#insn-00afeec4)
- ブロック [`00afeec4`](#insn-00afeec4) 範囲 `[['00afeec4', '00afeec7']]`
  - `CONDITIONAL_JUMP` [`00afeec4`](#insn-00afeec4) → [`00afef30`](#insn-00afef30)
  - `FALL_THROUGH` [`00afeec4`](#insn-00afeec4) → [`00afeec8`](#insn-00afeec8)
- ブロック [`00afeec8`](#insn-00afeec8) 範囲 `[['00afeec8', '00afeecf']]`
  - `CONDITIONAL_JUMP` [`00afeecc`](#insn-00afeecc) → [`00afeeb4`](#insn-00afeeb4)
  - `FALL_THROUGH` [`00afeecc`](#insn-00afeecc) → [`00afeed0`](#insn-00afeed0)
- ブロック [`00afeed0`](#insn-00afeed0) 範囲 `[['00afeed0', '00afeed3']]`
  - `FALL_THROUGH` [`00afeed0`](#insn-00afeed0) → [`00afeed4`](#insn-00afeed4)
- ブロック [`00afeed4`](#insn-00afeed4) 範囲 `[['00afeed4', '00afef13']]`
  - `CONDITIONAL_JUMP` [`00afef10`](#insn-00afef10) → [`00afef1c`](#insn-00afef1c)
  - `FALL_THROUGH` [`00afef10`](#insn-00afef10) → [`00afef14`](#insn-00afef14)
- ブロック [`00afef14`](#insn-00afef14) 範囲 `[['00afef14', '00afef1b']]`
  - `FALL_THROUGH` [`00afef18`](#insn-00afef18) → [`00afef1c`](#insn-00afef1c)
- ブロック [`00afef1c`](#insn-00afef1c) 範囲 `[['00afef1c', '00afef2f']]`
  - `FALL_THROUGH` [`00afef2c`](#insn-00afef2c) → [`00afef30`](#insn-00afef30)
- ブロック [`00afef30`](#insn-00afef30) 範囲 `[['00afef30', '00afef47']]`
  - `CONDITIONAL_JUMP` [`00afef44`](#insn-00afef44) → [`00afef5c`](#insn-00afef5c)
  - `FALL_THROUGH` [`00afef44`](#insn-00afef44) → [`00afef48`](#insn-00afef48)
- ブロック [`00afef48`](#insn-00afef48) 範囲 `[['00afef48', '00afef4f']]`
  - `UNCONDITIONAL_JUMP` [`00afef4c`](#insn-00afef4c) → [`00afef80`](#insn-00afef80)
- ブロック [`00afef50`](#insn-00afef50) 範囲 `[['00afef50', '00afef5b']]`
  - `CONDITIONAL_JUMP` [`00afef58`](#insn-00afef58) → [`00afef80`](#insn-00afef80)
  - `FALL_THROUGH` [`00afef58`](#insn-00afef58) → [`00afef5c`](#insn-00afef5c)
- ブロック [`00afef5c`](#insn-00afef5c) 範囲 `[['00afef5c', '00afef6b']]`
  - `CONDITIONAL_JUMP` [`00afef68`](#insn-00afef68) → [`00afef50`](#insn-00afef50)
  - `FALL_THROUGH` [`00afef68`](#insn-00afef68) → [`00afef6c`](#insn-00afef6c)
- ブロック [`00afef6c`](#insn-00afef6c) 範囲 `[['00afef6c', '00afef73']]`
  - `CONDITIONAL_JUMP` [`00afef70`](#insn-00afef70) → [`00afefcc`](#insn-00afefcc)
  - `FALL_THROUGH` [`00afef70`](#insn-00afef70) → [`00afef74`](#insn-00afef74)
- ブロック [`00afef74`](#insn-00afef74) 範囲 `[['00afef74', '00afef7b']]`
  - `CONDITIONAL_JUMP` [`00afef78`](#insn-00afef78) → [`00afef5c`](#insn-00afef5c)
  - `FALL_THROUGH` [`00afef78`](#insn-00afef78) → [`00afef7c`](#insn-00afef7c)
- ブロック [`00afef7c`](#insn-00afef7c) 範囲 `[['00afef7c', '00afef7f']]`
  - `FALL_THROUGH` [`00afef7c`](#insn-00afef7c) → [`00afef80`](#insn-00afef80)
- ブロック [`00afef80`](#insn-00afef80) 範囲 `[['00afef80', '00afefaf']]`
  - `CONDITIONAL_JUMP` [`00afefac`](#insn-00afefac) → [`00afefb8`](#insn-00afefb8)
  - `FALL_THROUGH` [`00afefac`](#insn-00afefac) → [`00afefb0`](#insn-00afefb0)
- ブロック [`00afefb0`](#insn-00afefb0) 範囲 `[['00afefb0', '00afefb7']]`
  - `FALL_THROUGH` [`00afefb4`](#insn-00afefb4) → [`00afefb8`](#insn-00afefb8)
- ブロック [`00afefb8`](#insn-00afefb8) 範囲 `[['00afefb8', '00afefcb']]`
  - `FALL_THROUGH` [`00afefc8`](#insn-00afefc8) → [`00afefcc`](#insn-00afefcc)
- ブロック [`00afefcc`](#insn-00afefcc) 範囲 `[['00afefcc', '00afefdf']]`
  - `CONDITIONAL_JUMP` [`00afefdc`](#insn-00afefdc) → [`00afeff8`](#insn-00afeff8)
  - `FALL_THROUGH` [`00afefdc`](#insn-00afefdc) → [`00afefe0`](#insn-00afefe0)
- ブロック [`00afefe0`](#insn-00afefe0) 範囲 `[['00afefe0', '00afefeb']]`
  - `UNCONDITIONAL_JUMP` [`00afefe8`](#insn-00afefe8) → [`00aff018`](#insn-00aff018)
- ブロック [`00afefec`](#insn-00afefec) 範囲 `[['00afefec', '00afeff7']]`
  - `CONDITIONAL_JUMP` [`00afeff4`](#insn-00afeff4) → [`00aff018`](#insn-00aff018)
  - `FALL_THROUGH` [`00afeff4`](#insn-00afeff4) → [`00afeff8`](#insn-00afeff8)
- ブロック [`00afeff8`](#insn-00afeff8) 範囲 `[['00afeff8', '00aff007']]`
  - `CONDITIONAL_JUMP` [`00aff004`](#insn-00aff004) → [`00afefec`](#insn-00afefec)
  - `FALL_THROUGH` [`00aff004`](#insn-00aff004) → [`00aff008`](#insn-00aff008)
- ブロック [`00aff008`](#insn-00aff008) 範囲 `[['00aff008', '00aff00b']]`
  - `CONDITIONAL_JUMP` [`00aff008`](#insn-00aff008) → [`00aff074`](#insn-00aff074)
  - `FALL_THROUGH` [`00aff008`](#insn-00aff008) → [`00aff00c`](#insn-00aff00c)
- ブロック [`00aff00c`](#insn-00aff00c) 範囲 `[['00aff00c', '00aff013']]`
  - `CONDITIONAL_JUMP` [`00aff010`](#insn-00aff010) → [`00afeff8`](#insn-00afeff8)
  - `FALL_THROUGH` [`00aff010`](#insn-00aff010) → [`00aff014`](#insn-00aff014)
- ブロック [`00aff014`](#insn-00aff014) 範囲 `[['00aff014', '00aff017']]`
  - `FALL_THROUGH` [`00aff014`](#insn-00aff014) → [`00aff018`](#insn-00aff018)
- ブロック [`00aff018`](#insn-00aff018) 範囲 `[['00aff018', '00aff057']]`
  - `CONDITIONAL_JUMP` [`00aff054`](#insn-00aff054) → [`00aff060`](#insn-00aff060)
  - `FALL_THROUGH` [`00aff054`](#insn-00aff054) → [`00aff058`](#insn-00aff058)
- ブロック [`00aff058`](#insn-00aff058) 範囲 `[['00aff058', '00aff05f']]`
  - `FALL_THROUGH` [`00aff05c`](#insn-00aff05c) → [`00aff060`](#insn-00aff060)
- ブロック [`00aff060`](#insn-00aff060) 範囲 `[['00aff060', '00aff073']]`
  - `FALL_THROUGH` [`00aff070`](#insn-00aff070) → [`00aff074`](#insn-00aff074)
- ブロック [`00aff074`](#insn-00aff074) 範囲 `[['00aff074', '00aff09b']]`
  - `CONDITIONAL_JUMP` [`00aff098`](#insn-00aff098) → [`00aff0b4`](#insn-00aff0b4)
  - `FALL_THROUGH` [`00aff098`](#insn-00aff098) → [`00aff09c`](#insn-00aff09c)
- ブロック [`00aff09c`](#insn-00aff09c) 範囲 `[['00aff09c', '00aff0a7']]`
  - `UNCONDITIONAL_JUMP` [`00aff0a4`](#insn-00aff0a4) → [`00aff0d4`](#insn-00aff0d4)
- ブロック [`00aff0a8`](#insn-00aff0a8) 範囲 `[['00aff0a8', '00aff0b3']]`
  - `CONDITIONAL_JUMP` [`00aff0b0`](#insn-00aff0b0) → [`00aff0d4`](#insn-00aff0d4)
  - `FALL_THROUGH` [`00aff0b0`](#insn-00aff0b0) → [`00aff0b4`](#insn-00aff0b4)
- ブロック [`00aff0b4`](#insn-00aff0b4) 範囲 `[['00aff0b4', '00aff0c3']]`
  - `CONDITIONAL_JUMP` [`00aff0c0`](#insn-00aff0c0) → [`00aff0a8`](#insn-00aff0a8)
  - `FALL_THROUGH` [`00aff0c0`](#insn-00aff0c0) → [`00aff0c4`](#insn-00aff0c4)
- ブロック [`00aff0c4`](#insn-00aff0c4) 範囲 `[['00aff0c4', '00aff0c7']]`
  - `CONDITIONAL_JUMP` [`00aff0c4`](#insn-00aff0c4) → [`00aff130`](#insn-00aff130)
  - `FALL_THROUGH` [`00aff0c4`](#insn-00aff0c4) → [`00aff0c8`](#insn-00aff0c8)
- ブロック [`00aff0c8`](#insn-00aff0c8) 範囲 `[['00aff0c8', '00aff0cf']]`
  - `CONDITIONAL_JUMP` [`00aff0cc`](#insn-00aff0cc) → [`00aff0b4`](#insn-00aff0b4)
  - `FALL_THROUGH` [`00aff0cc`](#insn-00aff0cc) → [`00aff0d0`](#insn-00aff0d0)
- ブロック [`00aff0d0`](#insn-00aff0d0) 範囲 `[['00aff0d0', '00aff0d3']]`
  - `FALL_THROUGH` [`00aff0d0`](#insn-00aff0d0) → [`00aff0d4`](#insn-00aff0d4)
- ブロック [`00aff0d4`](#insn-00aff0d4) 範囲 `[['00aff0d4', '00aff113']]`
  - `CONDITIONAL_JUMP` [`00aff110`](#insn-00aff110) → [`00aff11c`](#insn-00aff11c)
  - `FALL_THROUGH` [`00aff110`](#insn-00aff110) → [`00aff114`](#insn-00aff114)
- ブロック [`00aff114`](#insn-00aff114) 範囲 `[['00aff114', '00aff11b']]`
  - `FALL_THROUGH` [`00aff118`](#insn-00aff118) → [`00aff11c`](#insn-00aff11c)
- ブロック [`00aff11c`](#insn-00aff11c) 範囲 `[['00aff11c', '00aff12f']]`
  - `FALL_THROUGH` [`00aff12c`](#insn-00aff12c) → [`00aff130`](#insn-00aff130)
- ブロック [`00aff130`](#insn-00aff130) 範囲 `[['00aff130', '00aff14f']]`
  - `CONDITIONAL_JUMP` [`00aff14c`](#insn-00aff14c) → [`00aff168`](#insn-00aff168)
  - `FALL_THROUGH` [`00aff14c`](#insn-00aff14c) → [`00aff150`](#insn-00aff150)
- ブロック [`00aff150`](#insn-00aff150) 範囲 `[['00aff150', '00aff15b']]`
  - `UNCONDITIONAL_JUMP` [`00aff158`](#insn-00aff158) → [`00aff188`](#insn-00aff188)
- ブロック [`00aff15c`](#insn-00aff15c) 範囲 `[['00aff15c', '00aff167']]`
  - `CONDITIONAL_JUMP` [`00aff164`](#insn-00aff164) → [`00aff188`](#insn-00aff188)
  - `FALL_THROUGH` [`00aff164`](#insn-00aff164) → [`00aff168`](#insn-00aff168)
- ブロック [`00aff168`](#insn-00aff168) 範囲 `[['00aff168', '00aff177']]`
  - `CONDITIONAL_JUMP` [`00aff174`](#insn-00aff174) → [`00aff15c`](#insn-00aff15c)
  - `FALL_THROUGH` [`00aff174`](#insn-00aff174) → [`00aff178`](#insn-00aff178)
- ブロック [`00aff178`](#insn-00aff178) 範囲 `[['00aff178', '00aff17b']]`
  - `CONDITIONAL_JUMP` [`00aff178`](#insn-00aff178) → [`00aff1e4`](#insn-00aff1e4)
  - `FALL_THROUGH` [`00aff178`](#insn-00aff178) → [`00aff17c`](#insn-00aff17c)
- ブロック [`00aff17c`](#insn-00aff17c) 範囲 `[['00aff17c', '00aff183']]`
  - `CONDITIONAL_JUMP` [`00aff180`](#insn-00aff180) → [`00aff168`](#insn-00aff168)
  - `FALL_THROUGH` [`00aff180`](#insn-00aff180) → [`00aff184`](#insn-00aff184)
- ブロック [`00aff184`](#insn-00aff184) 範囲 `[['00aff184', '00aff187']]`
  - `FALL_THROUGH` [`00aff184`](#insn-00aff184) → [`00aff188`](#insn-00aff188)
- ブロック [`00aff188`](#insn-00aff188) 範囲 `[['00aff188', '00aff1c7']]`
  - `CONDITIONAL_JUMP` [`00aff1c4`](#insn-00aff1c4) → [`00aff1d0`](#insn-00aff1d0)
  - `FALL_THROUGH` [`00aff1c4`](#insn-00aff1c4) → [`00aff1c8`](#insn-00aff1c8)
- ブロック [`00aff1c8`](#insn-00aff1c8) 範囲 `[['00aff1c8', '00aff1cf']]`
  - `FALL_THROUGH` [`00aff1cc`](#insn-00aff1cc) → [`00aff1d0`](#insn-00aff1d0)
- ブロック [`00aff1d0`](#insn-00aff1d0) 範囲 `[['00aff1d0', '00aff1e3']]`
  - `FALL_THROUGH` [`00aff1e0`](#insn-00aff1e0) → [`00aff1e4`](#insn-00aff1e4)
- ブロック [`00aff1e4`](#insn-00aff1e4) 範囲 `[['00aff1e4', '00aff20f']]`
  - `CONDITIONAL_JUMP` [`00aff20c`](#insn-00aff20c) → [`00aff228`](#insn-00aff228)
  - `FALL_THROUGH` [`00aff20c`](#insn-00aff20c) → [`00aff210`](#insn-00aff210)
- ブロック [`00aff210`](#insn-00aff210) 範囲 `[['00aff210', '00aff21b']]`
  - `UNCONDITIONAL_JUMP` [`00aff218`](#insn-00aff218) → [`00aff248`](#insn-00aff248)
- ブロック [`00aff21c`](#insn-00aff21c) 範囲 `[['00aff21c', '00aff227']]`
  - `CONDITIONAL_JUMP` [`00aff224`](#insn-00aff224) → [`00aff248`](#insn-00aff248)
  - `FALL_THROUGH` [`00aff224`](#insn-00aff224) → [`00aff228`](#insn-00aff228)
- ブロック [`00aff228`](#insn-00aff228) 範囲 `[['00aff228', '00aff237']]`
  - `CONDITIONAL_JUMP` [`00aff234`](#insn-00aff234) → [`00aff21c`](#insn-00aff21c)
  - `FALL_THROUGH` [`00aff234`](#insn-00aff234) → [`00aff238`](#insn-00aff238)
- ブロック [`00aff238`](#insn-00aff238) 範囲 `[['00aff238', '00aff23b']]`
  - `CONDITIONAL_JUMP` [`00aff238`](#insn-00aff238) → [`00aff2a4`](#insn-00aff2a4)
  - `FALL_THROUGH` [`00aff238`](#insn-00aff238) → [`00aff23c`](#insn-00aff23c)
- ブロック [`00aff23c`](#insn-00aff23c) 範囲 `[['00aff23c', '00aff243']]`
  - `CONDITIONAL_JUMP` [`00aff240`](#insn-00aff240) → [`00aff228`](#insn-00aff228)
  - `FALL_THROUGH` [`00aff240`](#insn-00aff240) → [`00aff244`](#insn-00aff244)
- ブロック [`00aff244`](#insn-00aff244) 範囲 `[['00aff244', '00aff247']]`
  - `FALL_THROUGH` [`00aff244`](#insn-00aff244) → [`00aff248`](#insn-00aff248)
- ブロック [`00aff248`](#insn-00aff248) 範囲 `[['00aff248', '00aff257']]`
  - `FALL_THROUGH` [`00aff254`](#insn-00aff254) → [`00aff258`](#insn-00aff258)
- ブロック [`00aff258`](#insn-00aff258) 範囲 `[['00aff258', '00aff287']]`
  - `CONDITIONAL_JUMP` [`00aff284`](#insn-00aff284) → [`00aff290`](#insn-00aff290)
  - `FALL_THROUGH` [`00aff284`](#insn-00aff284) → [`00aff288`](#insn-00aff288)
- ブロック [`00aff288`](#insn-00aff288) 範囲 `[['00aff288', '00aff28f']]`
  - `FALL_THROUGH` [`00aff28c`](#insn-00aff28c) → [`00aff290`](#insn-00aff290)
- ブロック [`00aff290`](#insn-00aff290) 範囲 `[['00aff290', '00aff2a3']]`
  - `FALL_THROUGH` [`00aff2a0`](#insn-00aff2a0) → [`00aff2a4`](#insn-00aff2a4)
- ブロック [`00aff2a4`](#insn-00aff2a4) 範囲 `[['00aff2a4', '00aff2ab']]`
  - `FALL_THROUGH` [`00aff2a8`](#insn-00aff2a8) → [`00aff2ac`](#insn-00aff2ac)
- ブロック [`00aff2ac`](#insn-00aff2ac) 範囲 `[['00aff2ac', '00aff2c7']]`
  - `UNCONDITIONAL_JUMP` [`00aff2c4`](#insn-00aff2c4) → [`00afec50`](#insn-00afec50)
- ブロック [`00aff2c8`](#insn-00aff2c8) 範囲 `[['00aff2c8', '00aff2cb']]`

## 命令位置別の参照

- [`00afeaec`](#insn-00afeaec) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeaf0`](#insn-00afeaf0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeaf4`](#insn-00afeaf4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeaf8`](#insn-00afeaf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeafc`](#insn-00afeafc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb00`](#insn-00afeb00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb1c`](#insn-00afeb1c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb20`](#insn-00afeb20) → [`00b0272c`](../00b02/00b0272c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00b0272c` · 推定シンボル `None` · 推定型 `None`
- [`00afeb24`](#insn-00afeb24) → [`00afec4c`](#insn-00afec4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb28`](#insn-00afeb28) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afeb38`](#insn-00afeb38) → [`009e0fc0`](../009e0/009e0fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e0fc0` · 推定シンボル `None` · 推定型 `None`
- [`00afeb3c`](#insn-00afeb3c) → [`00afeb80`](#insn-00afeb80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb40`](#insn-00afeb40) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afeb5c`](#insn-00afeb5c) → [`009e3ea8`](../009e3/009e3ea8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009e3ea8` · 推定シンボル `None` · 推定型 `None`
- [`00afeb60`](#insn-00afeb60) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb64`](#insn-00afeb64) → [`00afec4c`](#insn-00afec4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb68`](#insn-00afeb68) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb70`](#insn-00afeb70) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb74`](#insn-00afeb74) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00afeb7c`](#insn-00afeb7c) → [`00afec50`](#insn-00afec50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeb88`](#insn-00afeb88) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afeb90`](#insn-00afeb90) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afeb94`](#insn-00afeb94) → [`00afebb0`](#insn-00afebb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeba0`](#insn-00afeba0) → [`00afebd0`](#insn-00afebd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afebac`](#insn-00afebac) → [`00afebd0`](#insn-00afebd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afebbc`](#insn-00afebbc) → [`00afeba4`](#insn-00afeba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afebc0`](#insn-00afebc0) → [`00afec2c`](#insn-00afec2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afebc8`](#insn-00afebc8) → [`00afebb0`](#insn-00afebb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afebd8`](#insn-00afebd8) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00afebf0`](#insn-00afebf0) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`00afec00`](#insn-00afec00) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afec04`](#insn-00afec04) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afec0c`](#insn-00afec0c) → [`00afec18`](#insn-00afec18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec10`](#insn-00afec10) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afec14`](#insn-00afec14) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afec18`](#insn-00afec18) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afec1c`](#insn-00afec1c) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00afec20`](#insn-00afec20) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afec28`](#insn-00afec28) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afec3c`](#insn-00afec3c) → [`00afec80`](#insn-00afec80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec48`](#insn-00afec48) → [`00afeb88`](#insn-00afeb88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec54`](#insn-00afec54) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec5c`](#insn-00afec5c) → [`00aff2c8`](#insn-00aff2c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec60`](#insn-00afec60) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec64`](#insn-00afec64) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec68`](#insn-00afec68) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec6c`](#insn-00afec6c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec70`](#insn-00afec70) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec74`](#insn-00afec74) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec80`](#insn-00afec80) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afec88`](#insn-00afec88) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afec8c`](#insn-00afec8c) → [`00afeca8`](#insn-00afeca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afec98`](#insn-00afec98) → [`00afecc8`](#insn-00afecc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeca4`](#insn-00afeca4) → [`00afecc8`](#insn-00afecc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afecb4`](#insn-00afecb4) → [`00afec9c`](#insn-00afec9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afecb8`](#insn-00afecb8) → [`00afed24`](#insn-00afed24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afecc0`](#insn-00afecc0) → [`00afeca8`](#insn-00afeca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afecd0`](#insn-00afecd0) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00afece8`](#insn-00afece8) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`00afecf8`](#insn-00afecf8) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afecfc`](#insn-00afecfc) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afed04`](#insn-00afed04) → [`00afed10`](#insn-00afed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed08`](#insn-00afed08) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afed0c`](#insn-00afed0c) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afed10`](#insn-00afed10) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afed14`](#insn-00afed14) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00afed18`](#insn-00afed18) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afed20`](#insn-00afed20) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afed30`](#insn-00afed30) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afed3c`](#insn-00afed3c) → [`00afedf0`](#insn-00afedf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed40`](#insn-00afed40) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afed44`](#insn-00afed44) → [`00afed60`](#insn-00afed60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed50`](#insn-00afed50) → [`00afed80`](#insn-00afed80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed5c`](#insn-00afed5c) → [`00afed80`](#insn-00afed80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed6c`](#insn-00afed6c) → [`00afed54`](#insn-00afed54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed70`](#insn-00afed70) → [`00afeddc`](#insn-00afeddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed78`](#insn-00afed78) → [`00afed60`](#insn-00afed60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afed88`](#insn-00afed88) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00afeda0`](#insn-00afeda0) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`00afedb0`](#insn-00afedb0) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afedb4`](#insn-00afedb4) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afedbc`](#insn-00afedbc) → [`00afedc8`](#insn-00afedc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afedc0`](#insn-00afedc0) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afedc4`](#insn-00afedc4) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afedc8`](#insn-00afedc8) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afedcc`](#insn-00afedcc) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00afedd0`](#insn-00afedd0) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afedd8`](#insn-00afedd8) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afedec`](#insn-00afedec) → [`00afec50`](#insn-00afec50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afedf0`](#insn-00afedf0) → `0023d250`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afedf4`](#insn-00afedf4) → [`00afee10`](#insn-00afee10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afee00`](#insn-00afee00) → [`00afee30`](#insn-00afee30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afee0c`](#insn-00afee0c) → [`00afee30`](#insn-00afee30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afee1c`](#insn-00afee1c) → [`00afee04`](#insn-00afee04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afee20`](#insn-00afee20) → [`00afee8c`](#insn-00afee8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afee28`](#insn-00afee28) → [`00afee10`](#insn-00afee10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afee38`](#insn-00afee38) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00afee5c`](#insn-00afee5c) → `0023d250`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afee60`](#insn-00afee60) → `0023d248`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afee6c`](#insn-00afee6c) → [`00afee78`](#insn-00afee78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afee70`](#insn-00afee70) → `0023d248`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afee74`](#insn-00afee74) → `0023d250`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afee78`](#insn-00afee78) → `0023d250`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afee7c`](#insn-00afee7c) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00afee80`](#insn-00afee80) → `0023d258`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afee88`](#insn-00afee88) → `0023d258`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afee8c`](#insn-00afee8c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afee94`](#insn-00afee94) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afee98`](#insn-00afee98) → [`00afeeb4`](#insn-00afeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeea4`](#insn-00afeea4) → [`00afeed4`](#insn-00afeed4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeeb0`](#insn-00afeeb0) → [`00afeed4`](#insn-00afeed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeec0`](#insn-00afeec0) → [`00afeea8`](#insn-00afeea8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeec4`](#insn-00afeec4) → [`00afef30`](#insn-00afef30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeecc`](#insn-00afeecc) → [`00afeeb4`](#insn-00afeeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeedc`](#insn-00afeedc) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00afeef4`](#insn-00afeef4) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`00afef04`](#insn-00afef04) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afef08`](#insn-00afef08) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afef10`](#insn-00afef10) → [`00afef1c`](#insn-00afef1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef14`](#insn-00afef14) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afef18`](#insn-00afef18) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afef1c`](#insn-00afef1c) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afef20`](#insn-00afef20) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00afef24`](#insn-00afef24) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afef2c`](#insn-00afef2c) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afef44`](#insn-00afef44) → [`00afef5c`](#insn-00afef5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef4c`](#insn-00afef4c) → [`00afef80`](#insn-00afef80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef58`](#insn-00afef58) → [`00afef80`](#insn-00afef80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef68`](#insn-00afef68) → [`00afef50`](#insn-00afef50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef70`](#insn-00afef70) → [`00afefcc`](#insn-00afefcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef78`](#insn-00afef78) → [`00afef5c`](#insn-00afef5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afef88`](#insn-00afef88) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00afefac`](#insn-00afefac) → [`00afefb8`](#insn-00afefb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afefbc`](#insn-00afefbc) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00afefd0`](#insn-00afefd0) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afefd8`](#insn-00afefd8) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00afefdc`](#insn-00afefdc) → [`00afeff8`](#insn-00afeff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afefe8`](#insn-00afefe8) → [`00aff018`](#insn-00aff018) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afeff4`](#insn-00afeff4) → [`00aff018`](#insn-00aff018) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff004`](#insn-00aff004) → [`00afefec`](#insn-00afefec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff008`](#insn-00aff008) → [`00aff074`](#insn-00aff074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff010`](#insn-00aff010) → [`00afeff8`](#insn-00afeff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff020`](#insn-00aff020) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00aff038`](#insn-00aff038) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`00aff048`](#insn-00aff048) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff04c`](#insn-00aff04c) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff054`](#insn-00aff054) → [`00aff060`](#insn-00aff060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff058`](#insn-00aff058) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff05c`](#insn-00aff05c) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff060`](#insn-00aff060) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff064`](#insn-00aff064) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00aff068`](#insn-00aff068) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff070`](#insn-00aff070) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff088`](#insn-00aff088) → `Stack[-0x8c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff08c`](#insn-00aff08c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aff094`](#insn-00aff094) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff098`](#insn-00aff098) → [`00aff0b4`](#insn-00aff0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff0a4`](#insn-00aff0a4) → [`00aff0d4`](#insn-00aff0d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff0b0`](#insn-00aff0b0) → [`00aff0d4`](#insn-00aff0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff0c0`](#insn-00aff0c0) → [`00aff0a8`](#insn-00aff0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff0c4`](#insn-00aff0c4) → [`00aff130`](#insn-00aff130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff0cc`](#insn-00aff0cc) → [`00aff0b4`](#insn-00aff0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff0dc`](#insn-00aff0dc) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00aff0f4`](#insn-00aff0f4) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`00aff104`](#insn-00aff104) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff108`](#insn-00aff108) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff110`](#insn-00aff110) → [`00aff11c`](#insn-00aff11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff114`](#insn-00aff114) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff118`](#insn-00aff118) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff11c`](#insn-00aff11c) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff120`](#insn-00aff120) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00aff124`](#insn-00aff124) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff12c`](#insn-00aff12c) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff140`](#insn-00aff140) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aff148`](#insn-00aff148) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff14c`](#insn-00aff14c) → [`00aff168`](#insn-00aff168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff158`](#insn-00aff158) → [`00aff188`](#insn-00aff188) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff164`](#insn-00aff164) → [`00aff188`](#insn-00aff188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff174`](#insn-00aff174) → [`00aff15c`](#insn-00aff15c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff178`](#insn-00aff178) → [`00aff1e4`](#insn-00aff1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff180`](#insn-00aff180) → [`00aff168`](#insn-00aff168) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff190`](#insn-00aff190) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00aff1a8`](#insn-00aff1a8) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`00aff1b8`](#insn-00aff1b8) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff1bc`](#insn-00aff1bc) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff1c4`](#insn-00aff1c4) → [`00aff1d0`](#insn-00aff1d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff1c8`](#insn-00aff1c8) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff1cc`](#insn-00aff1cc) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff1d0`](#insn-00aff1d0) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff1d4`](#insn-00aff1d4) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00aff1d8`](#insn-00aff1d8) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff1e0`](#insn-00aff1e0) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff200`](#insn-00aff200) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aff208`](#insn-00aff208) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff20c`](#insn-00aff20c) → [`00aff228`](#insn-00aff228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff218`](#insn-00aff218) → [`00aff248`](#insn-00aff248) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff224`](#insn-00aff224) → [`00aff248`](#insn-00aff248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff234`](#insn-00aff234) → [`00aff21c`](#insn-00aff21c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff238`](#insn-00aff238) → [`00aff2a4`](#insn-00aff2a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff240`](#insn-00aff240) → [`00aff228`](#insn-00aff228) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff250`](#insn-00aff250) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00aff268`](#insn-00aff268) → [`00c58090`](../00c58/00c58090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58090` · 推定シンボル `None` · 推定型 `None`
- [`00aff278`](#insn-00aff278) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff27c`](#insn-00aff27c) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff284`](#insn-00aff284) → [`00aff290`](#insn-00aff290) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff288`](#insn-00aff288) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff28c`](#insn-00aff28c) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff290`](#insn-00aff290) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff294`](#insn-00aff294) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`00aff298`](#insn-00aff298) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff2a0`](#insn-00aff2a0) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`00aff2a8`](#insn-00aff2a8) → `Stack[-0x8c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff2c4`](#insn-00aff2c4) → [`00afec50`](#insn-00afec50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aff2c8`](#insn-00aff2c8) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afeaec`](#insn-00afeaec)

~~~json
{
  "source": "00afeaec",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeaf0`](#insn-00afeaf0)

~~~json
{
  "source": "00afeaf0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeaf4`](#insn-00afeaf4)

~~~json
{
  "source": "00afeaf4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeaf8`](#insn-00afeaf8)

~~~json
{
  "source": "00afeaf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeafc`](#insn-00afeafc)

~~~json
{
  "source": "00afeafc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb00`](#insn-00afeb00)

~~~json
{
  "source": "00afeb00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb1c`](#insn-00afeb1c)

~~~json
{
  "source": "00afeb1c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb20`](#insn-00afeb20)

~~~json
{
  "source": "00afeb20",
  "target": "00b0272c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeb24`](#insn-00afeb24)

~~~json
{
  "source": "00afeb24",
  "target": "00afec4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb28`](#insn-00afeb28)

~~~json
{
  "source": "00afeb28",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeb38`](#insn-00afeb38)

~~~json
{
  "source": "00afeb38",
  "target": "009e0fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeb3c`](#insn-00afeb3c)

~~~json
{
  "source": "00afeb3c",
  "target": "00afeb80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb40`](#insn-00afeb40)

~~~json
{
  "source": "00afeb40",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeb5c`](#insn-00afeb5c)

~~~json
{
  "source": "00afeb5c",
  "target": "009e3ea8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeb60`](#insn-00afeb60)

~~~json
{
  "source": "00afeb60",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb64`](#insn-00afeb64)

~~~json
{
  "source": "00afeb64",
  "target": "00afec4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb68`](#insn-00afeb68)

~~~json
{
  "source": "00afeb68",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb70`](#insn-00afeb70)

~~~json
{
  "source": "00afeb70",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb74`](#insn-00afeb74)

~~~json
{
  "source": "00afeb74",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeb7c`](#insn-00afeb7c)

~~~json
{
  "source": "00afeb7c",
  "target": "00afec50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeb88`](#insn-00afeb88)

~~~json
{
  "source": "00afeb88",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeb90`](#insn-00afeb90)

~~~json
{
  "source": "00afeb90",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afeb94`](#insn-00afeb94)

~~~json
{
  "source": "00afeb94",
  "target": "00afebb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeba0`](#insn-00afeba0)

~~~json
{
  "source": "00afeba0",
  "target": "00afebd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afebac`](#insn-00afebac)

~~~json
{
  "source": "00afebac",
  "target": "00afebd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afebbc`](#insn-00afebbc)

~~~json
{
  "source": "00afebbc",
  "target": "00afeba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afebc0`](#insn-00afebc0)

~~~json
{
  "source": "00afebc0",
  "target": "00afec2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afebc8`](#insn-00afebc8)

~~~json
{
  "source": "00afebc8",
  "target": "00afebb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afebd8`](#insn-00afebd8)

~~~json
{
  "source": "00afebd8",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afebf0`](#insn-00afebf0)

~~~json
{
  "source": "00afebf0",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afec00`](#insn-00afec00)

~~~json
{
  "source": "00afec00",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afec04`](#insn-00afec04)

~~~json
{
  "source": "00afec04",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afec0c`](#insn-00afec0c)

~~~json
{
  "source": "00afec0c",
  "target": "00afec18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec10`](#insn-00afec10)

~~~json
{
  "source": "00afec10",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afec14`](#insn-00afec14)

~~~json
{
  "source": "00afec14",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afec18`](#insn-00afec18)

~~~json
{
  "source": "00afec18",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afec1c`](#insn-00afec1c)

~~~json
{
  "source": "00afec1c",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afec20`](#insn-00afec20)

~~~json
{
  "source": "00afec20",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afec28`](#insn-00afec28)

~~~json
{
  "source": "00afec28",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afec3c`](#insn-00afec3c)

~~~json
{
  "source": "00afec3c",
  "target": "00afec80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec48`](#insn-00afec48)

~~~json
{
  "source": "00afec48",
  "target": "00afeb88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec54`](#insn-00afec54)

~~~json
{
  "source": "00afec54",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec5c`](#insn-00afec5c)

~~~json
{
  "source": "00afec5c",
  "target": "00aff2c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec60`](#insn-00afec60)

~~~json
{
  "source": "00afec60",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec64`](#insn-00afec64)

~~~json
{
  "source": "00afec64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec68`](#insn-00afec68)

~~~json
{
  "source": "00afec68",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec6c`](#insn-00afec6c)

~~~json
{
  "source": "00afec6c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec70`](#insn-00afec70)

~~~json
{
  "source": "00afec70",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec74`](#insn-00afec74)

~~~json
{
  "source": "00afec74",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec80`](#insn-00afec80)

~~~json
{
  "source": "00afec80",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afec88`](#insn-00afec88)

~~~json
{
  "source": "00afec88",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afec8c`](#insn-00afec8c)

~~~json
{
  "source": "00afec8c",
  "target": "00afeca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afec98`](#insn-00afec98)

~~~json
{
  "source": "00afec98",
  "target": "00afecc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeca4`](#insn-00afeca4)

~~~json
{
  "source": "00afeca4",
  "target": "00afecc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afecb4`](#insn-00afecb4)

~~~json
{
  "source": "00afecb4",
  "target": "00afec9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afecb8`](#insn-00afecb8)

~~~json
{
  "source": "00afecb8",
  "target": "00afed24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afecc0`](#insn-00afecc0)

~~~json
{
  "source": "00afecc0",
  "target": "00afeca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afecd0`](#insn-00afecd0)

~~~json
{
  "source": "00afecd0",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afece8`](#insn-00afece8)

~~~json
{
  "source": "00afece8",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afecf8`](#insn-00afecf8)

~~~json
{
  "source": "00afecf8",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afecfc`](#insn-00afecfc)

~~~json
{
  "source": "00afecfc",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afed04`](#insn-00afed04)

~~~json
{
  "source": "00afed04",
  "target": "00afed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed08`](#insn-00afed08)

~~~json
{
  "source": "00afed08",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afed0c`](#insn-00afed0c)

~~~json
{
  "source": "00afed0c",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afed10`](#insn-00afed10)

~~~json
{
  "source": "00afed10",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afed14`](#insn-00afed14)

~~~json
{
  "source": "00afed14",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afed18`](#insn-00afed18)

~~~json
{
  "source": "00afed18",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afed20`](#insn-00afed20)

~~~json
{
  "source": "00afed20",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afed30`](#insn-00afed30)

~~~json
{
  "source": "00afed30",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afed3c`](#insn-00afed3c)

~~~json
{
  "source": "00afed3c",
  "target": "00afedf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed40`](#insn-00afed40)

~~~json
{
  "source": "00afed40",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afed44`](#insn-00afed44)

~~~json
{
  "source": "00afed44",
  "target": "00afed60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed50`](#insn-00afed50)

~~~json
{
  "source": "00afed50",
  "target": "00afed80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed5c`](#insn-00afed5c)

~~~json
{
  "source": "00afed5c",
  "target": "00afed80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed6c`](#insn-00afed6c)

~~~json
{
  "source": "00afed6c",
  "target": "00afed54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed70`](#insn-00afed70)

~~~json
{
  "source": "00afed70",
  "target": "00afeddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed78`](#insn-00afed78)

~~~json
{
  "source": "00afed78",
  "target": "00afed60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afed88`](#insn-00afed88)

~~~json
{
  "source": "00afed88",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeda0`](#insn-00afeda0)

~~~json
{
  "source": "00afeda0",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afedb0`](#insn-00afedb0)

~~~json
{
  "source": "00afedb0",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afedb4`](#insn-00afedb4)

~~~json
{
  "source": "00afedb4",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afedbc`](#insn-00afedbc)

~~~json
{
  "source": "00afedbc",
  "target": "00afedc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afedc0`](#insn-00afedc0)

~~~json
{
  "source": "00afedc0",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afedc4`](#insn-00afedc4)

~~~json
{
  "source": "00afedc4",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afedc8`](#insn-00afedc8)

~~~json
{
  "source": "00afedc8",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afedcc`](#insn-00afedcc)

~~~json
{
  "source": "00afedcc",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afedd0`](#insn-00afedd0)

~~~json
{
  "source": "00afedd0",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afedd8`](#insn-00afedd8)

~~~json
{
  "source": "00afedd8",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afedec`](#insn-00afedec)

~~~json
{
  "source": "00afedec",
  "target": "00afec50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afedf0`](#insn-00afedf0)

~~~json
{
  "source": "00afedf0",
  "target": "0023d250",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6072,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afedf4`](#insn-00afedf4)

~~~json
{
  "source": "00afedf4",
  "target": "00afee10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afee00`](#insn-00afee00)

~~~json
{
  "source": "00afee00",
  "target": "00afee30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afee0c`](#insn-00afee0c)

~~~json
{
  "source": "00afee0c",
  "target": "00afee30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afee1c`](#insn-00afee1c)

~~~json
{
  "source": "00afee1c",
  "target": "00afee04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afee20`](#insn-00afee20)

~~~json
{
  "source": "00afee20",
  "target": "00afee8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afee28`](#insn-00afee28)

~~~json
{
  "source": "00afee28",
  "target": "00afee10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afee38`](#insn-00afee38)

~~~json
{
  "source": "00afee38",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afee5c`](#insn-00afee5c)

~~~json
{
  "source": "00afee5c",
  "target": "0023d250",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6072,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afee60`](#insn-00afee60)

~~~json
{
  "source": "00afee60",
  "target": "0023d248",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6064,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afee6c`](#insn-00afee6c)

~~~json
{
  "source": "00afee6c",
  "target": "00afee78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afee70`](#insn-00afee70)

~~~json
{
  "source": "00afee70",
  "target": "0023d248",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6064,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afee74`](#insn-00afee74)

~~~json
{
  "source": "00afee74",
  "target": "0023d250",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6072,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afee78`](#insn-00afee78)

~~~json
{
  "source": "00afee78",
  "target": "0023d250",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6072,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afee7c`](#insn-00afee7c)

~~~json
{
  "source": "00afee7c",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afee80`](#insn-00afee80)

~~~json
{
  "source": "00afee80",
  "target": "0023d258",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6080,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afee88`](#insn-00afee88)

~~~json
{
  "source": "00afee88",
  "target": "0023d258",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6080,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afee8c`](#insn-00afee8c)

~~~json
{
  "source": "00afee8c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afee94`](#insn-00afee94)

~~~json
{
  "source": "00afee94",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afee98`](#insn-00afee98)

~~~json
{
  "source": "00afee98",
  "target": "00afeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeea4`](#insn-00afeea4)

~~~json
{
  "source": "00afeea4",
  "target": "00afeed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeeb0`](#insn-00afeeb0)

~~~json
{
  "source": "00afeeb0",
  "target": "00afeed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeec0`](#insn-00afeec0)

~~~json
{
  "source": "00afeec0",
  "target": "00afeea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeec4`](#insn-00afeec4)

~~~json
{
  "source": "00afeec4",
  "target": "00afef30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeecc`](#insn-00afeecc)

~~~json
{
  "source": "00afeecc",
  "target": "00afeeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeedc`](#insn-00afeedc)

~~~json
{
  "source": "00afeedc",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afeef4`](#insn-00afeef4)

~~~json
{
  "source": "00afeef4",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afef04`](#insn-00afef04)

~~~json
{
  "source": "00afef04",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afef08`](#insn-00afef08)

~~~json
{
  "source": "00afef08",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afef10`](#insn-00afef10)

~~~json
{
  "source": "00afef10",
  "target": "00afef1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef14`](#insn-00afef14)

~~~json
{
  "source": "00afef14",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afef18`](#insn-00afef18)

~~~json
{
  "source": "00afef18",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afef1c`](#insn-00afef1c)

~~~json
{
  "source": "00afef1c",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afef20`](#insn-00afef20)

~~~json
{
  "source": "00afef20",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afef24`](#insn-00afef24)

~~~json
{
  "source": "00afef24",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afef2c`](#insn-00afef2c)

~~~json
{
  "source": "00afef2c",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afef44`](#insn-00afef44)

~~~json
{
  "source": "00afef44",
  "target": "00afef5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef4c`](#insn-00afef4c)

~~~json
{
  "source": "00afef4c",
  "target": "00afef80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef58`](#insn-00afef58)

~~~json
{
  "source": "00afef58",
  "target": "00afef80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef68`](#insn-00afef68)

~~~json
{
  "source": "00afef68",
  "target": "00afef50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef70`](#insn-00afef70)

~~~json
{
  "source": "00afef70",
  "target": "00afefcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef78`](#insn-00afef78)

~~~json
{
  "source": "00afef78",
  "target": "00afef5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afef88`](#insn-00afef88)

~~~json
{
  "source": "00afef88",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afefac`](#insn-00afefac)

~~~json
{
  "source": "00afefac",
  "target": "00afefb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afefbc`](#insn-00afefbc)

~~~json
{
  "source": "00afefbc",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afefd0`](#insn-00afefd0)

~~~json
{
  "source": "00afefd0",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afefd8`](#insn-00afefd8)

~~~json
{
  "source": "00afefd8",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00afefdc`](#insn-00afefdc)

~~~json
{
  "source": "00afefdc",
  "target": "00afeff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afefe8`](#insn-00afefe8)

~~~json
{
  "source": "00afefe8",
  "target": "00aff018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afeff4`](#insn-00afeff4)

~~~json
{
  "source": "00afeff4",
  "target": "00aff018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff004`](#insn-00aff004)

~~~json
{
  "source": "00aff004",
  "target": "00afefec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff008`](#insn-00aff008)

~~~json
{
  "source": "00aff008",
  "target": "00aff074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff010`](#insn-00aff010)

~~~json
{
  "source": "00aff010",
  "target": "00afeff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff020`](#insn-00aff020)

~~~json
{
  "source": "00aff020",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff038`](#insn-00aff038)

~~~json
{
  "source": "00aff038",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff048`](#insn-00aff048)

~~~json
{
  "source": "00aff048",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff04c`](#insn-00aff04c)

~~~json
{
  "source": "00aff04c",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff054`](#insn-00aff054)

~~~json
{
  "source": "00aff054",
  "target": "00aff060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff058`](#insn-00aff058)

~~~json
{
  "source": "00aff058",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff05c`](#insn-00aff05c)

~~~json
{
  "source": "00aff05c",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff060`](#insn-00aff060)

~~~json
{
  "source": "00aff060",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff064`](#insn-00aff064)

~~~json
{
  "source": "00aff064",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff068`](#insn-00aff068)

~~~json
{
  "source": "00aff068",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff070`](#insn-00aff070)

~~~json
{
  "source": "00aff070",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff088`](#insn-00aff088)

~~~json
{
  "source": "00aff088",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff08c`](#insn-00aff08c)

~~~json
{
  "source": "00aff08c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff094`](#insn-00aff094)

~~~json
{
  "source": "00aff094",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff098`](#insn-00aff098)

~~~json
{
  "source": "00aff098",
  "target": "00aff0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff0a4`](#insn-00aff0a4)

~~~json
{
  "source": "00aff0a4",
  "target": "00aff0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff0b0`](#insn-00aff0b0)

~~~json
{
  "source": "00aff0b0",
  "target": "00aff0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff0c0`](#insn-00aff0c0)

~~~json
{
  "source": "00aff0c0",
  "target": "00aff0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff0c4`](#insn-00aff0c4)

~~~json
{
  "source": "00aff0c4",
  "target": "00aff130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff0cc`](#insn-00aff0cc)

~~~json
{
  "source": "00aff0cc",
  "target": "00aff0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff0dc`](#insn-00aff0dc)

~~~json
{
  "source": "00aff0dc",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff0f4`](#insn-00aff0f4)

~~~json
{
  "source": "00aff0f4",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff104`](#insn-00aff104)

~~~json
{
  "source": "00aff104",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff108`](#insn-00aff108)

~~~json
{
  "source": "00aff108",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff110`](#insn-00aff110)

~~~json
{
  "source": "00aff110",
  "target": "00aff11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff114`](#insn-00aff114)

~~~json
{
  "source": "00aff114",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff118`](#insn-00aff118)

~~~json
{
  "source": "00aff118",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff11c`](#insn-00aff11c)

~~~json
{
  "source": "00aff11c",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff120`](#insn-00aff120)

~~~json
{
  "source": "00aff120",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff124`](#insn-00aff124)

~~~json
{
  "source": "00aff124",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff12c`](#insn-00aff12c)

~~~json
{
  "source": "00aff12c",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff140`](#insn-00aff140)

~~~json
{
  "source": "00aff140",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff148`](#insn-00aff148)

~~~json
{
  "source": "00aff148",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff14c`](#insn-00aff14c)

~~~json
{
  "source": "00aff14c",
  "target": "00aff168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff158`](#insn-00aff158)

~~~json
{
  "source": "00aff158",
  "target": "00aff188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff164`](#insn-00aff164)

~~~json
{
  "source": "00aff164",
  "target": "00aff188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff174`](#insn-00aff174)

~~~json
{
  "source": "00aff174",
  "target": "00aff15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff178`](#insn-00aff178)

~~~json
{
  "source": "00aff178",
  "target": "00aff1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff180`](#insn-00aff180)

~~~json
{
  "source": "00aff180",
  "target": "00aff168",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff190`](#insn-00aff190)

~~~json
{
  "source": "00aff190",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff1a8`](#insn-00aff1a8)

~~~json
{
  "source": "00aff1a8",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff1b8`](#insn-00aff1b8)

~~~json
{
  "source": "00aff1b8",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff1bc`](#insn-00aff1bc)

~~~json
{
  "source": "00aff1bc",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff1c4`](#insn-00aff1c4)

~~~json
{
  "source": "00aff1c4",
  "target": "00aff1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff1c8`](#insn-00aff1c8)

~~~json
{
  "source": "00aff1c8",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff1cc`](#insn-00aff1cc)

~~~json
{
  "source": "00aff1cc",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff1d0`](#insn-00aff1d0)

~~~json
{
  "source": "00aff1d0",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff1d4`](#insn-00aff1d4)

~~~json
{
  "source": "00aff1d4",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff1d8`](#insn-00aff1d8)

~~~json
{
  "source": "00aff1d8",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff1e0`](#insn-00aff1e0)

~~~json
{
  "source": "00aff1e0",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff200`](#insn-00aff200)

~~~json
{
  "source": "00aff200",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff208`](#insn-00aff208)

~~~json
{
  "source": "00aff208",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff20c`](#insn-00aff20c)

~~~json
{
  "source": "00aff20c",
  "target": "00aff228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff218`](#insn-00aff218)

~~~json
{
  "source": "00aff218",
  "target": "00aff248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff224`](#insn-00aff224)

~~~json
{
  "source": "00aff224",
  "target": "00aff248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff234`](#insn-00aff234)

~~~json
{
  "source": "00aff234",
  "target": "00aff21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff238`](#insn-00aff238)

~~~json
{
  "source": "00aff238",
  "target": "00aff2a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff240`](#insn-00aff240)

~~~json
{
  "source": "00aff240",
  "target": "00aff228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff250`](#insn-00aff250)

~~~json
{
  "source": "00aff250",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff268`](#insn-00aff268)

~~~json
{
  "source": "00aff268",
  "target": "00c58090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff278`](#insn-00aff278)

~~~json
{
  "source": "00aff278",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff27c`](#insn-00aff27c)

~~~json
{
  "source": "00aff27c",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff284`](#insn-00aff284)

~~~json
{
  "source": "00aff284",
  "target": "00aff290",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff288`](#insn-00aff288)

~~~json
{
  "source": "00aff288",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff28c`](#insn-00aff28c)

~~~json
{
  "source": "00aff28c",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff290`](#insn-00aff290)

~~~json
{
  "source": "00aff290",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff294`](#insn-00aff294)

~~~json
{
  "source": "00aff294",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aff298`](#insn-00aff298)

~~~json
{
  "source": "00aff298",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff2a0`](#insn-00aff2a0)

~~~json
{
  "source": "00aff2a0",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "d0beb9000000000002040000010000000000000000000000d8beb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00aff2a8`](#insn-00aff2a8)

~~~json
{
  "source": "00aff2a8",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff2c4`](#insn-00aff2c4)

~~~json
{
  "source": "00aff2c4",
  "target": "00afec50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aff2c8`](#insn-00aff2c8)

~~~json
{
  "source": "00aff2c8",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
