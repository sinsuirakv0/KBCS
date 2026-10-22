# 00afbadc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afbadc.md)

## 関数情報

~~~json
{
  "address": "00afbadc",
  "name": "firebase::callback::AddCallbackWithThreadCheck",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "58514ce418d3979e458bd6ad704bfa89db019792a69481c793b9d5c5678fdc14",
  "source_text_sha256": "58514ce418d3979e458bd6ad704bfa89db019792a69481c793b9d5c5678fdc14"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb6d0](../00bdb/00bdb6d0.md)
- [00bdeb30](../00bde/00bdeb30.md)
- [00bdeb90](../00bde/00bdeb90.md)

## 疑似コード 1/1 / UTF-8 1079 bytes

~~~c

/* firebase::callback::AddCallbackWithThreadCheck(firebase::callback::Callback*) */

undefined8 firebase::callback::AddCallbackWithThreadCheck(Callback *param_1)

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
    (**(code **)(*(long *)param_1 + 0x10))(param_1);
    if (param_1 != (Callback *)0x0) {
                    /* try { // try from 00afbb30 to 00bfbb47 has its CatchHandler @ 00aff424 */
      (**(code **)(*(long *)param_1 + 8))(param_1);
    }
    return 0;
  }
LAB_00afbb54:
                    /* try { // try from 00afbb58 to 00bfbb6f has its CatchHandler @ 00b0037c */
  uVar2 = AddCallback(param_1);
  return uVar2;
}

~~~
