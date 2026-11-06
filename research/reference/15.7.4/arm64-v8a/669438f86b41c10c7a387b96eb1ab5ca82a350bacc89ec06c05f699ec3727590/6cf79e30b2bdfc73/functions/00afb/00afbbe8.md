# 00afbbe8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00afbbe8.md)

## 関数情報

~~~json
{
  "address": "00afbbe8",
  "name": "_ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d5d1048d31b0a3b121267079c9a70ce196d8b98637eb32659875934cfb998bb6",
  "source_text_sha256": "d5d1048d31b0a3b121267079c9a70ce196d8b98637eb32659875934cfb998bb6"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb7d0](../00bdb/00bdb7d0.md)
- [00bdec30](../00bde/00bdec30.md)
- [00bdec90](../00bde/00bdec90.md)

## 疑似コード 1/1 / UTF-8 995 bytes

~~~c

undefined8 _ZN8firebase8callback26AddCallbackWithThreadCheckEPNS0_8CallbackE(long *param_1)

{
  int iVar1;
  pthread_t __thread1;
  undefined8 uVar2;
  
  if (DAT_010a0d38 == '\x01') {
    __thread1 = pthread_self();
                    /* try { // try from 00afbc10 to 00bfbc17 has its CatchHandler @ 00aff45c */
    if ((__thread1 == 0) || (DAT_010a0d40 == 0)) {
      if (DAT_010a0d40 != 0 || __thread1 != 0) goto LAB_00afbc60;
    }
    else {
      iVar1 = pthread_equal(__thread1,DAT_010a0d40);
      if (iVar1 == 0) goto LAB_00afbc60;
    }
    (**(code **)(*param_1 + 0x10))(param_1);
    if (param_1 != (long *)0x0) {
                    /* try { // try from 00afbc40 to 00bfbc57 has its CatchHandler @ 00aff458 */
      (**(code **)(*param_1 + 8))(param_1);
    }
    return 0;
  }
LAB_00afbc60:
                    /* try { // try from 00afbc68 to 00bfbc7f has its CatchHandler @ 00b003c0 */
  uVar2 = _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE(param_1);
  return uVar2;
}

~~~
