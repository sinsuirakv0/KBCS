# 00bcfa9c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bcfa9c.md)

## 関数情報

~~~json
{
  "address": "00bcfa9c",
  "name": "FUN_00bcfa9c",
  "size": 228,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2bf0aee19f35e94f43b033aa5f8dfef0c9df2049db13e12f7a2d05427e00758e",
  "source_text_sha256": "2bf0aee19f35e94f43b033aa5f8dfef0c9df2049db13e12f7a2d05427e00758e"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bc81c8](../00bc8/00bc81c8.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 疑似コード 1/1 / UTF-8 1841 bytes

~~~c

void FUN_00bcfa9c(long param_1,undefined8 *param_2)

{
  void *pvVar1;
  long lVar2;
  size_t sVar3;
  ulong uVar4;
  
                    /* try { // try from 00bcfaa8 to 00ccfaaf has its CatchHandler @ 00bcfc6c */
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + 1;
                    /* try { // try from 00bcfad0 to 00ccfad7 has its CatchHandler @ 00bcfcec */
  if ((ulong)param_2[2] < uVar4) {
    sVar3 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar3 < uVar4 || sVar3 - uVar4 == 0) {
      sVar3 = uVar4;
    }
    param_2[2] = sVar3;
    pvVar1 = realloc(pvVar1,sVar3);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
                    /* try { // try from 00bcfb04 to 00ccfb0b has its CatchHandler @ 00bcfcdc */
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x5b;
                    /* try { // try from 00bcfb0c to 00ccfb6b has its CatchHandler @ 00bcfd04 */
  FUN_00bc81c8(param_1 + 0x10,param_2);
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar4 = lVar2 + 1;
  *(int *)(param_2 + 4) = *(int *)(param_2 + 4) + -1;
  if ((ulong)param_2[2] < uVar4) {
    sVar3 = param_2[2] * 2;
    uVar4 = lVar2 + 0x3e1;
    if (sVar3 < uVar4 || sVar3 - uVar4 == 0) {
      sVar3 = uVar4;
    }
    param_2[2] = sVar3;
    pvVar1 = realloc(pvVar1,sVar3);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar4 = lVar2 + 1;
  }
  param_2[1] = uVar4;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x5d;
  return;
}

~~~
