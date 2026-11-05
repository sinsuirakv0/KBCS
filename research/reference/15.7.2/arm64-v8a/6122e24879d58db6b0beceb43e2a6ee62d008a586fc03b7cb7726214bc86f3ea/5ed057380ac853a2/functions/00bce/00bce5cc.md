# 00bce5cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bce5cc.md)

## 関数情報

~~~json
{
  "address": "00bce5cc",
  "name": "FUN_00bce5cc",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d2ba983f3b38aabf5ca33bc6a15903bc59bdd2fe2a18c6585388ccf721f894a",
  "source_text_sha256": "1d2ba983f3b38aabf5ca33bc6a15903bc59bdd2fe2a18c6585388ccf721f894a"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 疑似コード 1/1 / UTF-8 1235 bytes

~~~c

void FUN_00bce5cc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *__ptr;
  long lVar2;
  size_t __size;
  long *plVar3;
  
  lVar2 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 6U) {
    __size = param_2[2] * 2;
    uVar1 = lVar2 + 0x3e6;
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
  }
  *(undefined2 *)((undefined4 *)((long)__ptr + lVar2) + 1) = 0x2077;
  *(undefined4 *)((long)__ptr + lVar2) = 0x6f726874;
  plVar3 = *(long **)(param_1 + 0x10);
  lVar2 = *plVar3;
  param_2[1] = param_2[1] + 6;
  (**(code **)(lVar2 + 0x20))(plVar3,param_2);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) == 0x40) {
                    /* try { // try from 00bce678 to 00cce6e7 has its CatchHandler @ 00bcf304 */
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00bce69c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  return;
}

~~~
