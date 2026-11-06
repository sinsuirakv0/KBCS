# 00afd2ac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00afd2ac.md)

## 関数情報

~~~json
{
  "address": "00afd2ac",
  "name": "FUN_00afd2ac",
  "size": 480,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e35b21d1eb9576f80ba0bb4126a497039eefeb8770c72d9b303f7a85c2b36504",
  "source_text_sha256": "e35b21d1eb9576f80ba0bb4126a497039eefeb8770c72d9b303f7a85c2b36504"
}
~~~
## 呼び出し元

- [00afd108](../00afd/00afd108.md)
- [00afd23c](../00afd/00afd23c.md)
- [00afdc48](../00afd/00afdc48.md)
- [00afddf8](../00afd/00afddf8.md)

## 呼び出し先

- [00bdb130](../00bdb/00bdb130.md)
- [00bdb7a0](../00bdb/00bdb7a0.md)
- [00bded80](../00bde/00bded80.md)

## 疑似コード 1/1 / UTF-8 3503 bytes

~~~c

void FUN_00afd2ac(undefined8 *param_1,byte *param_2,byte *param_3)

{
  ulong uVar1;
  byte bVar2;
  byte bVar3;
  int iVar4;
  int iVar5;
  uint uVar6;
  undefined8 extraout_x1;
  undefined8 uVar7;
  uint uVar8;
  byte *pbVar9;
  int iVar10;
  int iVar11;
  ulong uVar12;
  byte *pbVar13;
  ulong uVar14;
  undefined8 extraout_x17;
  undefined8 uVar15;
  
                    /* try { // try from 00afd2c8 to 00bfd373 has its CatchHandler @ 00af5650 */
  *param_1 = 0;
  param_1[1] = 0;
  iVar4 = (int)((ulong)((long)param_3 - (long)param_2) >> 3) * -0x55555555;
  param_1[2] = 0;
  if (iVar4 != 0) {
    iVar4 = iVar4 + -1;
    iVar5 = __strlen_chk(&DAT_0029583d,2);
    if (param_2 == param_3) {
                    /* try { // try from 00afd374 to 00bfd3fb has its CatchHandler @ 00b00180 */
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm
                (param_1,(long)(iVar4 * iVar5));
      return;
    }
    uVar1 = (((long)param_3 - (long)param_2) - 0x18U) / 0x18 + 1;
    if (uVar1 < 2) {
      iVar10 = 0;
      bVar2 = *param_2;
      pbVar9 = param_2;
      if ((bVar2 & 1) != 0) goto LAB_00afd354;
      goto LAB_00afd338;
    }
    uVar12 = uVar1 & 0x1ffffffffffffffe;
    iVar11 = 0;
    iVar10 = 0;
    pbVar9 = param_2 + uVar12 * 0x18;
    pbVar13 = param_2 + 0x20;
    uVar7 = extraout_x1;
    uVar14 = uVar12;
    uVar15 = extraout_x17;
    do {
      bVar2 = pbVar13[-0x20];
      bVar3 = pbVar13[-8];
      if ((bVar2 & 1) != 0) {
        uVar15 = *(undefined8 *)(pbVar13 + -0x18);
      }
      if ((bVar3 & 1) != 0) {
        uVar7 = *(undefined8 *)pbVar13;
      }
      uVar8 = (uint)(bVar2 >> 1);
      if ((bVar2 & 1) != 0) {
        uVar8 = (uint)uVar15;
      }
      uVar6 = (uint)(bVar3 >> 1);
      if ((bVar3 & 1) != 0) {
        uVar6 = (uint)uVar7;
      }
      iVar11 = iVar11 + uVar8;
      uVar14 = uVar14 - 2;
      iVar10 = iVar10 + uVar6;
      pbVar13 = pbVar13 + 0x30;
    } while (uVar14 != 0);
    iVar10 = iVar10 + iVar11;
    if (uVar1 != uVar12) {
      do {
        bVar2 = *pbVar9;
        if ((bVar2 & 1) == 0) {
LAB_00afd338:
          uVar8 = (uint)(bVar2 >> 1);
        }
        else {
LAB_00afd354:
          uVar8 = (uint)*(undefined8 *)(pbVar9 + 8);
        }
        pbVar9 = pbVar9 + 0x18;
        iVar10 = iVar10 + uVar8;
      } while (param_3 != pbVar9);
    }
                    /* try { // try from 00afd3fc to 00bfdb2f has its CatchHandler @ 00af5650 */
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7reserveEm
              (param_1,(long)(iVar10 + iVar4 * iVar5));
    if (param_2 != param_3) {
      uVar1 = *(ulong *)(param_2 + 8);
      pbVar9 = *(byte **)(param_2 + 0x10);
      if ((*param_2 & 1) == 0) {
        pbVar9 = param_2 + 1;
        uVar1 = (ulong)(*param_2 >> 1);
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                (param_1,pbVar9,uVar1);
      while (param_2 = param_2 + 0x18, param_2 != param_3) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                  (param_1,&DAT_0029583d,1);
        uVar1 = *(ulong *)(param_2 + 8);
        pbVar9 = *(byte **)(param_2 + 0x10);
        if ((*param_2 & 1) == 0) {
          pbVar9 = param_2 + 1;
          uVar1 = (ulong)(*param_2 >> 1);
        }
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                  (param_1,pbVar9,uVar1);
      }
    }
  }
  return;
}

~~~
