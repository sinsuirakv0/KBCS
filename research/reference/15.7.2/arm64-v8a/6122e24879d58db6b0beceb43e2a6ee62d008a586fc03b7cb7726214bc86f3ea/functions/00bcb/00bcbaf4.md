# 00bcbaf4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bcbaf4.md)

## 関数情報

~~~json
{
  "address": "00bcbaf4",
  "name": "FUN_00bcbaf4",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "da19f24501c146829701465e75831c8da57e61774b45f449bd4e3f794ee33f4d",
  "source_text_sha256": "da19f24501c146829701465e75831c8da57e61774b45f449bd4e3f794ee33f4d"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bc81c8](../00bc8/00bc81c8.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 関連文字列（未確認候補）

~~~text
"> typename "
"template<"
~~~
## 疑似コード 1/1 / UTF-8 2048 bytes

~~~c

void FUN_00bcbaf4(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  char *pcVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  void *pvVar5;
  long lVar6;
  size_t sVar7;
  
  lVar6 = param_2[1];
  pvVar5 = (void *)*param_2;
  uVar3 = *(undefined4 *)(param_2 + 4);
  *(undefined4 *)(param_2 + 4) = 0;
  if ((ulong)param_2[2] < lVar6 + 9U) {
    sVar7 = param_2[2] * 2;
    uVar1 = lVar6 + 0x3e9;
                    /* try { // try from 00bcbb38 to 00ccbb43 has its CatchHandler @ 00bcbba0 */
    if (sVar7 < uVar1 || sVar7 - uVar1 == 0) {
      sVar7 = uVar1;
    }
    param_2[2] = sVar7;
    pvVar5 = realloc(pvVar5,sVar7);
                    /* try { // try from 00bcbb44 to 00ccbc07 has its CatchHandler @ 00bcb930 */
    *param_2 = pvVar5;
    if (pvVar5 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar6 = param_2[1];
  }
  uVar4 = s_template<_002ae6c0._0_8_;
  ((char *)((long)pvVar5 + lVar6))[8] = '<';
  *(undefined8 *)((long)pvVar5 + lVar6) = uVar4;
  param_2[1] = param_2[1] + 9;
  FUN_00bc81c8(param_1 + 0x18,param_2);
  lVar6 = param_2[1];
  pvVar5 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar6 + 0xbU) {
    sVar7 = param_2[2] * 2;
    uVar1 = lVar6 + 0x3eb;
                    /* catch() { ... } // from try @ 00bcbb38 with catch @ 00bcbba0 */
    if (sVar7 < uVar1 || sVar7 - uVar1 == 0) {
      sVar7 = uVar1;
    }
    param_2[2] = sVar7;
    pvVar5 = realloc(pvVar5,sVar7);
    *param_2 = pvVar5;
    if (pvVar5 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar6 = param_2[1];
  }
                    /* catch() { ... } // from try @ 00bcba08 with catch @ 00bcbbbc */
  pcVar2 = (char *)((long)pvVar5 + lVar6);
  *(undefined8 *)pcVar2 = s_>_typename_002a0244._0_8_;
  pcVar2[7] = 'a';
  pcVar2[8] = 'm';
  pcVar2[9] = 'e';
  pcVar2[10] = ' ';
  param_2[1] = param_2[1] + 0xb;
  *(undefined4 *)(param_2 + 4) = uVar3;
  return;
}

~~~
