# 00afbadc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00afbbe8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbbe8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00afbadc",
  "name": "_ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3ba0cdb4831309a5362a50af0c188d6a2bbdf7fe91a6e96776a8e7ecddee8356",
  "source_text_sha256": "3ba0cdb4831309a5362a50af0c188d6a2bbdf7fe91a6e96776a8e7ecddee8356"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb6d0](../00bdb/00bdb6d0.md)
- [00bdeb30](../00bde/00bdeb30.md)
- [00bdeb90](../00bde/00bdeb90.md)

## 疑似コード / UTF-8 995 bytes

~~~c

undefined8 _ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE(long *param_1)

{
  int iVar1;
  pthread_t __thread1;
  undefined8 uVar2;
  
  if (DAT_010a0c38 == '\x01') {
    __thread1 = pthread_self();
                    /* try { // try from 00afbb00 to 00bfbb07 has its CatchHandler @ 00aff428 */
    if ((__thread1 == 0) || (DAT_010a0c40 == 0)) {
      if (DAT_010a0c40 != 0 || __thread1 != 0) goto LAB_00afbb54;
    }
    else {
      iVar1 = pthread_equal(__thread1,DAT_010a0c40);
      if (iVar1 == 0) goto LAB_00afbb54;
    }
    (**(code **)(*param_1 + 0x10))(param_1);
    if (param_1 != (long *)0x0) {
                    /* try { // try from 00afbb30 to 00bfbb47 has its CatchHandler @ 00aff424 */
      (**(code **)(*param_1 + 8))(param_1);
    }
    return 0;
  }
LAB_00afbb54:
                    /* try { // try from 00afbb58 to 00bfbb6f has its CatchHandler @ 00b0037c */
  uVar2 = _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE(param_1);
  return uVar2;
}

~~~
