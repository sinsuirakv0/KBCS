# 00c0ddfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00c0ddfc",
  "name": "_ZNSt6__ndk19__num_getIcE19__stage2_float_loopEcRbRcPcRS4_ccRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSE_RjS4_",
  "size": 636,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9fe7b9923d69c95e3661ff0d6f49d220d061e99b40e2a1feb6525dda3b4013c2",
  "source_text_sha256": "9fe7b9923d69c95e3661ff0d6f49d220d061e99b40e2a1feb6525dda3b4013c2"
}
~~~

## 呼び出し元

- [00c5e160](../00c5e/00c5e160.md)

## 呼び出し先

- [00c57bd0](../00c57/00c57bd0.md)

## 関連文字列（未確認候補）

~~~text
"0123456789abcdefABCDEFxX+-pPiInN"
~~~

## 疑似コード / UTF-8 5309 bytes

~~~c

undefined8
_ZNSt6__ndk19__num_getIcE19__stage2_float_loopEcRbRcPcRS4_ccRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSE_RjS4_
          (byte param_1,char *param_2,byte *param_3,byte *param_4,long *param_5,byte param_6,
          byte param_7,byte *param_8,long param_9,undefined8 *param_10,int *param_11,void *param_12)

{
  void *pvVar1;
  ulong uVar2;
  byte bVar3;
  byte bVar4;
  byte bVar5;
  void *pvVar6;
  undefined1 *puVar7;
  int *piVar8;
  ulong uVar9;
  byte *pbVar10;
  uint uVar11;
  uint uVar12;
  
                    /* try { // try from 00c0de2c to 00d0de47 has its CatchHandler @ 00c0e0e8 */
  if (param_1 == param_6) {
    if (*param_2 != '\0') {
      puVar7 = (undefined1 *)*param_5;
      *param_2 = '\0';
                    /* try { // try from 00c0de48 to 00d0de53 has its CatchHandler @ 00c0e04c */
      *param_5 = (long)(puVar7 + 1);
      *puVar7 = 0x2e;
      uVar9 = (ulong)(*param_8 >> 1);
      if ((*param_8 & 1) != 0) {
        uVar9 = *(ulong *)(param_8 + 8);
      }
      if ((uVar9 != 0) && (piVar8 = (int *)*param_10, (long)piVar8 - param_9 < 0xa0)) {
        *piVar8 = *param_11;
        *param_10 = piVar8 + 1;
        return 0;
                    /* try { // try from 00c0de88 to 00d0de8f has its CatchHandler @ 00c0e0e4 */
      }
      return 0;
    }
  }
  else {
                    /* try { // try from 00c0de90 to 00d0de9b has its CatchHandler @ 00c0e0b4 */
    if (param_1 == param_7) {
      uVar9 = (ulong)(*param_8 >> 1);
      if ((*param_8 & 1) != 0) {
        uVar9 = *(ulong *)(param_8 + 8);
      }
      if (uVar9 != 0) {
        if (*param_2 == '\0') {
          return 0xffffffff;
        }
        piVar8 = (int *)*param_10;
                    /* try { // try from 00c0debc to 00d0dec3 has its CatchHandler @ 00c0e0e0 */
        if (0x9f < (long)piVar8 - param_9) {
          return 0;
        }
                    /* try { // try from 00c0dec4 to 00d0decf has its CatchHandler @ 00c0e0b0 */
        *piVar8 = *param_11;
        *param_10 = piVar8 + 1;
        *param_11 = 0;
        return 0;
      }
    }
                    /* try { // try from 00c0def0 to 00d0def7 has its CatchHandler @ 00c0e010 */
                    /* try { // try from 00c0def8 to 00d0df07 has its CatchHandler @ 00c0e050 */
    pvVar6 = memchr(param_12,(uint)param_1,0x20);
    pvVar1 = (void *)((long)param_12 + 0x20);
    if (pvVar6 != (void *)0x0) {
      pvVar1 = pvVar6;
    }
    uVar9 = (long)pvVar1 - (long)param_12;
    if ((long)uVar9 < 0x20) {
                    /* try { // try from 00c0df48 to 00d0df4f has its CatchHandler @ 00c0e008 */
                    /* try { // try from 00c0df50 to 00d0df63 has its CatchHandler @ 00c0e01c */
      bVar4 = PTR__ZNSt6__ndk114__num_get_base5__srcE_00c9b7c0[uVar9];
      uVar11 = (uint)bVar4;
      if ((uVar9 & 0xfffffffffffffffe) == 0x16) {
        *param_3 = 0x50;
        pbVar10 = (byte *)*param_5;
        *param_5 = (long)(pbVar10 + 1);
        *pbVar10 = bVar4;
        return 0;
      }
                    /* try { // try from 00c0df64 to 00d0e17b has its CatchHandler @ 00c0dadc */
      if ((uVar9 & 0xfffffffffffffffe) == 0x18) {
        pbVar10 = (byte *)*param_5;
        if (pbVar10 != param_4) {
          bVar5 = pbVar10[-1];
          bVar3 = *param_3;
          uVar11 = bVar5 ^ 0x20;
          if (0x19 < bVar5 - 0x61) {
            uVar11 = (uint)bVar5;
          }
          uVar12 = bVar3 ^ 0x20;
          if (0x19 < bVar3 - 0x61) {
            uVar12 = (uint)bVar3;
          }
          if (uVar11 != uVar12) {
            return 0xffffffff;
          }
        }
        *param_5 = (long)(pbVar10 + 1);
        *pbVar10 = bVar4;
        return 0;
      }
      bVar3 = *param_3;
      uVar12 = uVar11 ^ 0x20;
      if (0x19 < uVar11 - 0x61) {
        uVar12 = uVar11;
      }
      if (uVar12 == bVar3) {
        bVar5 = bVar3 | 0x20;
        if (0x19 < uVar12 - 0x41) {
          bVar5 = bVar3;
        }
                    /* catch() { ... } // from try @ 00c0df48 with catch @ 00c0e008 */
        *param_3 = bVar5;
                    /* catch() { ... } // from try @ 00c0df1c with catch @ 00c0e00c */
                    /* catch() { ... } // from try @ 00c0def0 with catch @ 00c0e010 */
        if (*param_2 != '\0') {
          *param_2 = '\0';
                    /* catch() { ... } // from try @ 00c0df50 with catch @ 00c0e01c */
          uVar2 = (ulong)(*param_8 >> 1);
          if ((*param_8 & 1) != 0) {
            uVar2 = *(ulong *)(param_8 + 8);
          }
                    /* catch() { ... } // from try @ 00c0df24 with catch @ 00c0e034 */
          if ((uVar2 != 0) && (piVar8 = (int *)*param_10, (long)piVar8 - param_9 < 0xa0)) {
            *piVar8 = *param_11;
            *param_10 = piVar8 + 1;
          }
        }
      }
                    /* catch() { ... } // from try @ 00c0de48 with catch @ 00c0e04c */
      pbVar10 = (byte *)*param_5;
                    /* catch() { ... } // from try @ 00c0def8 with catch @ 00c0e050 */
      *param_5 = (long)(pbVar10 + 1);
      *pbVar10 = bVar4;
      if ((long)uVar9 < 0x16) {
        *param_11 = *param_11 + 1;
        return 0;
      }
      return 0;
    }
  }
                    /* try { // try from 00c0df1c to 00d0df23 has its CatchHandler @ 00c0e00c */
  return 0xffffffff;
}

~~~
