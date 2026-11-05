# 00b8daec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00b8daec.md)

## 関数情報

~~~json
{
  "address": "00b8daec",
  "name": "_ZNSt6__ndk19__num_getIcE17__stage2_int_loopEciPcRS2_RjcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSD_S2_",
  "size": 448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d95eb14fe7d21627aa66f75316d492d5077a5f452ed18833db516ba4f4f56d34",
  "source_text_sha256": "d95eb14fe7d21627aa66f75316d492d5077a5f452ed18833db516ba4f4f56d34"
}
~~~
## 呼び出し元

- [00be1430](../00be1/00be1430.md)

## 呼び出し先

- [00bdb080](../00bdb/00bdb080.md)

## 関連文字列（未確認候補）

~~~text
"0123456789abcdefABCDEFxX+-pPiInN"
~~~
## 疑似コード 1/1 / UTF-8 2738 bytes

~~~c

undefined8
_ZNSt6__ndk19__num_getIcE17__stage2_int_loopEciPcRS2_RjcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSD_S2_
          (byte param_1,uint param_2,undefined1 *param_3,long *param_4,int *param_5,byte param_6,
          byte *param_7,long param_8,undefined8 *param_9,void *param_10)

{
  ulong uVar1;
  void *pvVar2;
  undefined *puVar3;
  void *pvVar4;
  undefined8 uVar5;
  undefined1 uVar6;
  long lVar7;
  int *piVar8;
  undefined1 *puVar9;
  
  puVar9 = (undefined1 *)*param_4;
  if (puVar9 == param_3) {
    if (*(byte *)((long)param_10 + 0x18) == param_1) {
      uVar6 = 0x2b;
LAB_00b8dbd0:
      *param_4 = (long)(param_3 + 1);
      *param_3 = uVar6;
      *param_5 = 0;
      return 0;
    }
    if (*(byte *)((long)param_10 + 0x19) == param_1) {
      uVar6 = 0x2d;
      goto LAB_00b8dbd0;
    }
  }
  uVar1 = (ulong)(*param_7 >> 1);
  if ((*param_7 & 1) != 0) {
    uVar1 = *(ulong *)(param_7 + 8);
  }
  if ((param_1 == param_6) && (uVar1 != 0)) {
    piVar8 = (int *)*param_9;
                    /* try { // try from 00b8db4c to 00c8dc97 has its CatchHandler @ 00b8db4c
                       catch() { ... } // from try @ 00b8db4c with catch @ 00b8db4c
                       catch() { ... } // from try @ 00b8dca4 with catch @ 00b8db4c */
    if ((long)piVar8 - param_8 < 0xa0) {
      *piVar8 = *param_5;
      *param_9 = piVar8 + 1;
      *param_5 = 0;
      return 0;
    }
    return 0;
  }
  pvVar4 = memchr(param_10,(uint)param_1,0x1a);
  puVar3 = PTR__ZNSt6__ndk114__num_get_base5__srcE_00c1bc90;
  pvVar2 = (void *)((long)param_10 + 0x1a);
  if (pvVar4 != (void *)0x0) {
    pvVar2 = pvVar4;
  }
  lVar7 = (long)pvVar2 - (long)param_10;
  if (lVar7 < 0x18) {
    if (param_2 == 8) {
LAB_00b8dc08:
      if ((long)(ulong)param_2 <= lVar7) goto LAB_00b8dbb8;
    }
    else if (param_2 == 0x10) {
      if (0x15 < lVar7) {
        if (puVar9 == param_3) {
          return 0xffffffff;
        }
        if (2 < (long)puVar9 - (long)param_3) {
          return 0xffffffff;
        }
        if (puVar9[-1] != '0') {
          return 0xffffffff;
        }
        *param_5 = 0;
                    /* try { // try from 00b8dc98 to 00c8dca3 has its CatchHandler @ 00b8dd24 */
        uVar6 = puVar3[lVar7];
        *param_4 = (long)(puVar9 + 1);
                    /* try { // try from 00b8dca4 to 00c8dd4b has its CatchHandler @ 00b8db4c */
        *puVar9 = uVar6;
        return 0;
      }
    }
    else if (param_2 == 10) goto LAB_00b8dc08;
    uVar5 = 0;
    uVar6 = PTR__ZNSt6__ndk114__num_get_base5__srcE_00c1bc90[lVar7];
    *param_4 = (long)(puVar9 + 1);
    *puVar9 = uVar6;
    *param_5 = *param_5 + 1;
  }
  else {
LAB_00b8dbb8:
    uVar5 = 0xffffffff;
  }
  return uVar5;
}

~~~
