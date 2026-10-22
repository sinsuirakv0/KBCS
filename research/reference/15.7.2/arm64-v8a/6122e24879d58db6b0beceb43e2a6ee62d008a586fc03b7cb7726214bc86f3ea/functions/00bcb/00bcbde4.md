# 00bcbde4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bcbde4.md)

## 関数情報

~~~json
{
  "address": "00bcbde4",
  "name": "FUN_00bcbde4",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "93b35ec34c667a8bc49b88b5ea798c4392c5e57d58452d6983975ab0ce30fade",
  "source_text_sha256": "93b35ec34c667a8bc49b88b5ea798c4392c5e57d58452d6983975ab0ce30fade"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bcbf44](../00bcb/00bcbf44.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 疑似コード 1/1 / UTF-8 2623 bytes

~~~c

void FUN_00bcbde4(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *pvVar2;
  size_t __size;
  long lVar3;
  size_t sVar4;
  void *__src;
  
  lVar3 = param_2[1];
  pvVar2 = (void *)*param_2;
                    /* try { // try from 00bcbe04 to 00ccbe67 has its CatchHandler @ 00bcbe04
                       catch() { ... } // from try @ 00bcbe04 with catch @ 00bcbe04
                       catch() { ... } // from try @ 00bcbe78 with catch @ 00bcbe04 */
  if ((ulong)param_2[2] < lVar3 + 7U) {
    sVar4 = param_2[2] * 2;
    uVar1 = lVar3 + 999;
    if (sVar4 < uVar1 || sVar4 - uVar1 == 0) {
      sVar4 = uVar1;
    }
    param_2[2] = sVar4;
    pvVar2 = realloc(pvVar2,sVar4);
    *param_2 = pvVar2;
    if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bcbe68 with catch @ 00bcbf30 */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined4 *)((long)pvVar2 + lVar3 + 3) = 0x6164626d;
  *(undefined4 *)((long)pvVar2 + lVar3) = 0x6d616c27;
  lVar3 = param_2[1] + 7;
  param_2[1] = lVar3;
                    /* try { // try from 00bcbe68 to 00ccbe77 has its CatchHandler @ 00bcbf30 */
  sVar4 = *(size_t *)(param_1 + 0x48);
  if (sVar4 != 0) {
                    /* try { // try from 00bcbe78 to 00ccbf6f has its CatchHandler @ 00bcbe04 */
    __src = *(void **)(param_1 + 0x40);
    pvVar2 = (void *)*param_2;
    if ((ulong)param_2[2] < lVar3 + sVar4) {
      __size = param_2[2] * 2;
      uVar1 = lVar3 + sVar4 + 0x3e0;
      if (__size < uVar1 || __size - uVar1 == 0) {
        __size = uVar1;
      }
      param_2[2] = __size;
      pvVar2 = realloc(pvVar2,__size);
      *param_2 = pvVar2;
      if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar3 = param_2[1];
    }
    memcpy((void *)((long)pvVar2 + lVar3),__src,sVar4);
    lVar3 = param_2[1] + sVar4;
    param_2[1] = lVar3;
  }
  pvVar2 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 1U) {
    sVar4 = param_2[2] * 2;
    uVar1 = lVar3 + 0x3e1;
    if (sVar4 < uVar1 || sVar4 - uVar1 == 0) {
      sVar4 = uVar1;
    }
    param_2[2] = sVar4;
    pvVar2 = realloc(pvVar2,sVar4);
    *param_2 = pvVar2;
    if (pvVar2 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
  *(undefined1 *)((long)pvVar2 + lVar3) = 0x27;
  param_2[1] = param_2[1] + 1;
  FUN_00bcbf44(param_1,param_2);
  return;
}

~~~
