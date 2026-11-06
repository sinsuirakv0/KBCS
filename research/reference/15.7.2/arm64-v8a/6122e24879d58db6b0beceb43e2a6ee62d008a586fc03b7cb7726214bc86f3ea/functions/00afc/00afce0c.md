# 00afce0c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00afce0c",
  "name": "_ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f410c2961d0cc37920bcca1d75b34288fa05830a36c44a9421bc9d2b197a0f46",
  "source_text_sha256": "f410c2961d0cc37920bcca1d75b34288fa05830a36c44a9421bc9d2b197a0f46"
}
~~~

## 呼び出し元

- [00bdec30](../00bde/00bdec30.md)

## 呼び出し先

- [00bdb030](../00bdb/00bdb030.md)
- [00bdec50](../00bde/00bdec50.md)
- [00bdec70](../00bde/00bdec70.md)

## 疑似コード / UTF-8 4052 bytes

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
    pbVar1 = param_2 + 1;
    bVar11 = true;
    do {
      uVar2 = (ulong)(bVar3 >> 1);
      pbVar4 = pbVar1;
                    /* try { // try from 00afceac to 00bfcec3 has its CatchHandler @ 00aff3ac */
      if (!bVar5) {
        uVar2 = uVar8;
        pbVar4 = pbVar9;
      }
      pbVar9 = pbVar10;
                    /* try { // try from 00afcec4 to 00bfcf27 has its CatchHandler @ 00af560c */
      if ((pbVar4 + uVar2 != pbVar10) &&
         (lVar6 = __strchr_chk(&DAT_0029583d,*pbVar10,2), lVar6 != 0)) {
        do {
          pbVar9 = pbVar4 + uVar2;
          if (pbVar4 + (uVar2 - 1) == pbVar10) break;
          pbVar9 = pbVar10 + 1;
          lVar6 = __strchr_chk(&DAT_0029583d,pbVar10[1],2);
          pbVar10 = pbVar9;
        } while (lVar6 != 0);
      }
      uVar8 = (ulong)(*param_2 >> 1);
      pbVar4 = pbVar1;
      if ((*param_2 & 1) != 0) {
        uVar8 = *(ulong *)(param_2 + 8);
        pbVar4 = *(byte **)(param_2 + 0x10);
      }
                    /* try { // try from 00afcf28 to 00bfcf2f has its CatchHandler @ 00aff3a8 */
      pbVar10 = pbVar9;
      if ((pbVar4 + uVar8 != pbVar9) && (lVar6 = __strchr_chk(&DAT_0029583d,*pbVar9,2), lVar6 == 0))
      {
        pbVar7 = pbVar9;
        do {
          pbVar10 = pbVar4 + uVar8;
          if (pbVar4 + (uVar8 - 1) == pbVar7) break;
                    /* try { // try from 00afcf58 to 00bfcf6f has its CatchHandler @ 00aff3a4 */
          pbVar10 = pbVar7 + 1;
          pbVar7 = pbVar7 + 1;
          lVar6 = __strchr_chk(&DAT_0029583d,*pbVar10,2);
          pbVar10 = pbVar7;
        } while (lVar6 == 0);
        if (pbVar10 != pbVar9) {
          if (!bVar11) {
                    /* try { // try from 00afcf80 to 00bfcf87 has its CatchHandler @ 00aff3a0 */
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                      (param_1,&DAT_0029583d,1);
          }
          uVar8 = (ulong)(*param_1 >> 1);
          pbVar4 = param_1 + 1;
                    /* try { // try from 00afcfb0 to 00bfcfc7 has its CatchHandler @ 00aff39c */
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
      if (!bVar5) {
        uVar2 = uVar8;
        pbVar4 = pbVar9;
      }
    } while (pbVar4 + uVar2 != pbVar10);
  }
                    /* try { // try from 00afcff8 to 00bfd00f has its CatchHandler @ 00aff38c */
  return;
}

~~~
