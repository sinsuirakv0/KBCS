# 00afbba4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afbba4",
  "name": "_ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dbd6d642174386cc5168a210f0d0a0c753e24a59318cfb949d0041beea435a41",
  "source_text_sha256": "dbd6d642174386cc5168a210f0d0a0c753e24a59318cfb949d0041beea435a41"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb780](../00bdb/00bdb780.md)
- [00bdebe0](../00bde/00bdebe0.md)
- [00bdec40](../00bde/00bdec40.md)

## 疑似コード / UTF-8 995 bytes

~~~c

undefined8 _ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE(long *param_1)

{
  int iVar1;
  pthread_t __thread1;
  undefined8 uVar2;
  
  if (DAT_010a0cf8 == '\x01') {
    __thread1 = pthread_self();
                    /* try { // try from 00afbbcc to 00bfbbd3 has its CatchHandler @ 00aff418 */
    if ((__thread1 == 0) || (DAT_010a0d00 == 0)) {
      if (DAT_010a0d00 != 0 || __thread1 != 0) goto LAB_00afbc1c;
    }
    else {
      iVar1 = pthread_equal(__thread1,DAT_010a0d00);
      if (iVar1 == 0) goto LAB_00afbc1c;
    }
    (**(code **)(*param_1 + 0x10))(param_1);
    if (param_1 != (long *)0x0) {
                    /* try { // try from 00afbbfc to 00bfbc13 has its CatchHandler @ 00aff414 */
      (**(code **)(*param_1 + 8))(param_1);
    }
    return 0;
  }
LAB_00afbc1c:
                    /* try { // try from 00afbc24 to 00bfbc3b has its CatchHandler @ 00b0037c */
  uVar2 = _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE(param_1);
  return uVar2;
}

~~~
