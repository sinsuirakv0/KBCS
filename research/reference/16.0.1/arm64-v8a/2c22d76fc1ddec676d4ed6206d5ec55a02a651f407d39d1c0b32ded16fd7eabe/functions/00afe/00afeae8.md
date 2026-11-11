# 00afeae8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

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
  "source_text_sha256": "ef39ebe1212841dd57aaafaa6b1750c180b7d3490bd596278490752324bdeb56"
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
