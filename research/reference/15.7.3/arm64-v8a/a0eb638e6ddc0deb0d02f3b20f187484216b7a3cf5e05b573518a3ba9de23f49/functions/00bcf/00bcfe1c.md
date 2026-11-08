# 00bcfe1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bcfe1c",
  "name": "FUN_00bcfe1c",
  "size": 256,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c0fb4a399350135fab51fb3637df072a90c8159fc6c94e6a3f4804a75f136bf7",
  "source_text_sha256": "c0fb4a399350135fab51fb3637df072a90c8159fc6c94e6a3f4804a75f136bf7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

## 疑似コード / UTF-8 1829 bytes

~~~c

void FUN_00bcfe1c(long param_1,undefined8 *param_2)

{
  void *__ptr;
  long lVar1;
  size_t __size;
  ulong uVar2;
  long *plVar3;
  
  plVar3 = *(long **)(param_1 + 0x18);
  (**(code **)(*plVar3 + 0x20))(plVar3);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  }
  lVar1 = param_2[1];
                    /* try { // try from 00bcfe74 to 00ccfe7b has its CatchHandler @ 00bcff0c */
  __ptr = (void *)*param_2;
  uVar2 = lVar1 + 1;
                    /* try { // try from 00bcfe7c to 00ccfea7 has its CatchHandler @ 00bcfe1c */
  if ((ulong)param_2[2] < uVar2) {
    __size = param_2[2] * 2;
    uVar2 = lVar1 + 0x3e1;
    if (__size < uVar2 || __size - uVar2 == 0) {
      __size = uVar2;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar1 = param_2[1];
                    /* try { // try from 00bcfea8 to 00ccfec3 has its CatchHandler @ 00bcff14 */
    uVar2 = lVar1 + 1;
  }
  param_2[1] = uVar2;
  *(undefined1 *)((long)__ptr + lVar1) = 0x40;
  plVar3 = *(long **)(param_1 + 0x10);
                    /* try { // try from 00bcfec4 to 00ccff53 has its CatchHandler @ 00bcfe1c */
  (**(code **)(*plVar3 + 0x20))(plVar3,param_2);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* catch() { ... } // from try @ 00bcfe74 with catch @ 00bcff0c */
                    /* WARNING: Could not recover jumptable at 0x00bcff14. Too many branches */
                    /* WARNING: Treating indirect jump as call */
                    /* catch() { ... } // from try @ 00bcfea8 with catch @ 00bcff14 */
  (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  return;
}

~~~
