# 00bcadb8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcadb8",
  "name": "_ZN8firebase6FutureINS_13remote_config10ConfigInfoEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5418a7ba363a030e813aad6945ceb5c31dc1827568d7e4e4bca058fa3bae09e5",
  "source_text_sha256": "5418a7ba363a030e813aad6945ceb5c31dc1827568d7e4e4bca058fa3bae09e5"
}
~~~

## 呼び出し元

- [00c5e9b0](../00c5e/00c5e9b0.md)

## 呼び出し先

- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5be90](../00c5b/00c5be90.md)
- [00c5bea0](../00c5b/00c5bea0.md)

## 疑似コード / UTF-8 853 bytes

~~~c

void _ZN8firebase6FutureINS_13remote_config10ConfigInfoEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
               (long param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = param_2;
  lVar1 = param_1 + 0x30;
  _ZN8firebase12FutureHandleC1ERKS0_(lVar1,param_3);
                    /* try { // try from 00bcadfc to 00ccadff has its CatchHandler @ 00bcaf84 */
  (**(code **)(**(long **)(param_1 + 0x28) + 0x10))(*(long **)(param_1 + 0x28),lVar1);
  _ZN8firebase12FutureHandle6DetachEv(lVar1);
  plVar2 = *(long **)(param_1 + 0x28);
  if (plVar2 != (long *)0x0) {
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
                    /* try { // try from 00bcae24 to 00ccae53 has its CatchHandler @ 00bcaf44 */
  return;
}

~~~
