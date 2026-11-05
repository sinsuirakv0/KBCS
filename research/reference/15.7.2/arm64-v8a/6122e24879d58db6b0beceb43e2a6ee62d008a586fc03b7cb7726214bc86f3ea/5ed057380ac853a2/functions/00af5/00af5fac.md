# 00af5fac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00af5fac.md)

## 関数情報

~~~json
{
  "address": "00af5fac",
  "name": "_ZN8firebase4util17JavaThreadContext24ReleaseExecuteCancelLockEv",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "02ac5efe381d4f01ce8780b12600580e01a0281f66e74f02418f33b1382cff1d",
  "source_text_sha256": "02ac5efe381d4f01ce8780b12600580e01a0281f66e74f02418f33b1382cff1d"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bde260](../00bde/00bde260.md)

## 疑似コード 1/1 / UTF-8 855 bytes

~~~c

void _ZN8firebase4util17JavaThreadContext24ReleaseExecuteCancelLockEv(long param_1)

{
  char cVar1;
  long *plVar2;
  
  plVar2 = (long *)_ZNK8firebase8internal16JObjectReference9GetJNIEnvEv();
  if (*(long *)(param_1 + 8) != 0) {
    FUN_00551e14(plVar2,*(long *)(param_1 + 8),DAT_010a02d8);
    cVar1 = (**(code **)(*plVar2 + 0x720))(plVar2);
    if (cVar1 != '\0') {
                    /* try { // try from 00af5ff0 to 00bf5ff7 has its CatchHandler @ 00affb08 */
      (**(code **)(*plVar2 + 0x80))(plVar2);
                    /* try { // try from 00af6000 to 00bf6007 has its CatchHandler @ 00affb00 */
                    /* WARNING: Could not recover jumptable at 0x00af6014. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      (**(code **)(*plVar2 + 0x88))(plVar2);
      return;
    }
  }
  return;
}

~~~
