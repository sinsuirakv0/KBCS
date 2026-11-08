# 00afced4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afced4",
  "name": "_ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2f4fac85ef9e39a3868625f68d002a13d13fdd1d7f10b55db8260c3e0ec16cb",
  "source_text_sha256": "d2f4fac85ef9e39a3868625f68d002a13d13fdd1d7f10b55db8260c3e0ec16cb"
}
~~~

## 呼び出し元

- [00bdece0](../00bde/00bdece0.md)

## 呼び出し先

- [00bdb0e0](../00bdb/00bdb0e0.md)
- [00bded00](../00bde/00bded00.md)
- [00bded20](../00bde/00bded20.md)

## 疑似コード / UTF-8 4246 bytes

~~~c

void _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (byte *param_1,byte *param_2)

{
  byte *pbVar1;
  ulong uVar2;
  byte bVar3;
  byte *pbVar4;
  bool bVar5;
  long lVar6;
  byte *pbVar7;
  ulong uVar8;
  byte *pbVar9;
  byte *pbVar10;
  bool bVar11;
  
  param_1[0] = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[5] = 0;
  param_1[6] = 0;
  param_1[7] = 0;
  param_1[8] = 0;
  param_1[9] = 0;
  param_1[10] = 0;
  param_1[0xb] = 0;
  param_1[0xc] = 0;
  param_1[0xd] = 0;
  param_1[0xe] = 0;
  param_1[0xf] = 0;
  param_1[0x10] = 0;
  param_1[0x11] = 0;
  param_1[0x12] = 0;
  param_1[0x13] = 0;
  param_1[0x14] = 0;
  param_1[0x15] = 0;
  param_1[0x16] = 0;
  param_1[0x17] = 0;
  bVar3 = *param_2;
  uVar8 = *(ulong *)(param_2 + 8);
  pbVar9 = *(byte **)(param_2 + 0x10);
  bVar5 = (bVar3 & 1) == 0;
  pbVar10 = pbVar9;
  uVar2 = uVar8;
  if (bVar5) {
    pbVar10 = param_2 + 1;
    uVar2 = (ulong)(bVar3 >> 1);
  }
  if (uVar2 != 0) {
                    /* try { // try from 00afcf28 to 00bfcf2f has its CatchHandler @ 00aff3a8 */
    pbVar1 = param_2 + 1;
    bVar11 = true;
    do {
      uVar2 = (ulong)(bVar3 >> 1);
      pbVar4 = pbVar1;
      if (!bVar5) {
        uVar2 = uVar8;
        pbVar4 = pbVar9;
      }
                    /* try { // try from 00afcf80 to 00bfcf87 has its CatchHandler @ 00aff3a0 */
      pbVar9 = pbVar10;
      if ((pbVar4 + uVar2 != pbVar10) &&
         (lVar6 = __strchr_chk(&DAT_002958ca,*pbVar10,2), lVar6 != 0)) {
        do {
          pbVar9 = pbVar4 + uVar2;
          if (pbVar4 + (uVar2 - 1) == pbVar10) break;
                    /* try { // try from 00afcfb0 to 00bfcfc7 has its CatchHandler @ 00aff39c */
          pbVar9 = pbVar10 + 1;
          lVar6 = __strchr_chk(&DAT_002958ca,pbVar10[1],2);
                    /* try { // try from 00afcfc8 to 00bfcff7 has its CatchHandler @ 00af560c */
          pbVar10 = pbVar9;
        } while (lVar6 != 0);
      }
      uVar8 = (ulong)(*param_2 >> 1);
      pbVar4 = pbVar1;
      if ((*param_2 & 1) != 0) {
        uVar8 = *(ulong *)(param_2 + 8);
        pbVar4 = *(byte **)(param_2 + 0x10);
      }
      pbVar10 = pbVar9;
                    /* try { // try from 00afcff8 to 00bfd00f has its CatchHandler @ 00aff38c */
      if ((pbVar4 + uVar8 != pbVar9) && (lVar6 = __strchr_chk(&DAT_002958ca,*pbVar9,2), lVar6 == 0))
      {
                    /* try { // try from 00afd010 to 00bfd03f has its CatchHandler @ 00af560c */
        pbVar7 = pbVar9;
        do {
          pbVar10 = pbVar4 + uVar8;
          if (pbVar4 + (uVar8 - 1) == pbVar7) break;
          pbVar10 = pbVar7 + 1;
          pbVar7 = pbVar7 + 1;
          lVar6 = __strchr_chk(&DAT_002958ca,*pbVar10,2);
          pbVar10 = pbVar7;
        } while (lVar6 == 0);
        if (pbVar10 != pbVar9) {
          if (!bVar11) {
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                      (param_1,&DAT_002958ca,1);
          }
          uVar8 = (ulong)(*param_1 >> 1);
          pbVar4 = param_1 + 1;
                    /* try { // try from 00afd070 to 00bfd087 has its CatchHandler @ 00aff384 */
          if ((*param_1 & 1) != 0) {
            uVar8 = *(ulong *)(param_1 + 8);
            pbVar4 = *(byte **)(param_1 + 0x10);
          }
          _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertINS_11__wrap_iterIPKcEEEENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr38__libcpp_string_gets_noexcept_iteratorISC_EE5valueENS7_IPcEEE4typeESA_SC_SC_
                    (param_1,pbVar4 + uVar8,pbVar9,pbVar10);
          bVar11 = false;
        }
      }
      bVar3 = *param_2;
      uVar8 = *(ulong *)(param_2 + 8);
      pbVar9 = *(byte **)(param_2 + 0x10);
      bVar5 = (bVar3 & 1) == 0;
      uVar2 = (ulong)(bVar3 >> 1);
      pbVar4 = pbVar1;
                    /* try { // try from 00afcf58 to 00bfcf6f has its CatchHandler @ 00aff3a4 */
      if (!bVar5) {
        uVar2 = uVar8;
        pbVar4 = pbVar9;
      }
    } while (pbVar4 + uVar2 != pbVar10);
  }
                    /* try { // try from 00afd0c0 to 00bfd0d7 has its CatchHandler @ 00aff380 */
  return;
}

~~~
