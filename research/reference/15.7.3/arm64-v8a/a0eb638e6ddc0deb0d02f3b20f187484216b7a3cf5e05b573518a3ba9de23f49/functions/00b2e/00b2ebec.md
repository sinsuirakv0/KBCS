# 00b2ebec

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00b2ebec",
  "name": "_ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA_",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "10b8e6cca61a1454143af334a03dd898111c183b542edfc91065939c51e660e6",
  "source_text_sha256": "10b8e6cca61a1454143af334a03dd898111c183b542edfc91065939c51e660e6"
}
~~~

## 呼び出し元

- [00be0070](../00be0/00be0070.md)

## 呼び出し先

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bde270](../00bde/00bde270.md)

## 疑似コード / UTF-8 2385 bytes

~~~c

void _ZNSt6__ndk16vectorIPN11flatbuffers7EnumDefENS_9allocatorIS3_EEE6assignIPS3_EENS_9enable_ifIXaasr21__is_forward_iteratorIT_EE5valuesr16is_constructibleIS3_NS_15iterator_traitsISA_E9referenceEEE5valueEvE4typeESA_SA_
               (undefined8 *param_1,void *param_2,void *param_3)

{
  void *__src;
  long lVar1;
  ulong uVar2;
  size_t sVar3;
  void *pvVar4;
  ulong uVar5;
  
                    /* try { // try from 00b2ebf8 to 00c2eccb has its CatchHandler @ 00b2c36c */
  lVar1 = param_1[2];
  pvVar4 = (void *)*param_1;
  sVar3 = (long)param_3 - (long)param_2;
  uVar5 = (long)sVar3 >> 3;
  if ((ulong)(lVar1 - (long)pvVar4 >> 3) < uVar5) {
    if (pvVar4 != (void *)0x0) {
      param_1[1] = pvVar4;
      _ZdlPv(pvVar4);
      lVar1 = 0;
      *param_1 = 0;
      param_1[1] = 0;
      param_1[2] = 0;
    }
    if (uVar5 >> 0x3d != 0) {
LAB_00b2ec70:
                    /* WARNING: Subroutine does not return */
      abort();
    }
    if ((ulong)(lVar1 >> 3) < 0xfffffffffffffff) {
      uVar2 = lVar1 >> 2;
      if ((uVar5 <= uVar2) && (uVar5 = uVar2, uVar2 >> 0x3d != 0)) goto LAB_00b2ec70;
    }
    else {
      uVar5 = 0x1fffffffffffffff;
    }
    pvVar4 = (void *)_Znwm(uVar5 * 8);
                    /* try { // try from 00b2ed04 to 00c2ee77 has its CatchHandler @ 00b2c36c */
    *param_1 = pvVar4;
    param_1[1] = pvVar4;
    param_1[2] = (void *)((long)pvVar4 + uVar5 * 8);
    if (0 < (long)sVar3) {
      memcpy(pvVar4,param_2,sVar3);
      pvVar4 = (void *)((long)pvVar4 + sVar3);
    }
    param_1[1] = pvVar4;
  }
  else {
    uVar2 = param_1[1] - (long)pvVar4 >> 3;
    __src = (void *)((long)param_2 + (param_1[1] - (long)pvVar4));
    if (uVar5 <= uVar2) {
      __src = param_3;
    }
    sVar3 = (long)__src - (long)param_2;
    if (sVar3 != 0) {
      memmove(pvVar4,param_2,sVar3);
    }
    if (uVar2 < uVar5) {
      pvVar4 = (void *)param_1[1];
      sVar3 = (long)param_3 - (long)__src;
      if (0 < (long)sVar3) {
                    /* try { // try from 00b2eccc to 00c2ecd7 has its CatchHandler @ 00b2f890 */
        memcpy(pvVar4,__src,sVar3);
        pvVar4 = (void *)((long)pvVar4 + sVar3);
      }
      param_1[1] = pvVar4;
                    /* try { // try from 00b2ecd8 to 00c2ed03 has its CatchHandler @ 00b2f88c */
    }
    else {
      param_1[1] = (void *)((long)pvVar4 + ((long)sVar3 >> 3) * 8);
    }
  }
  return;
}

~~~
