# 00bcaf6c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bcaf6c",
  "name": "_ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b1394661667b48d43d4049ef2ad9660c6060fa0f88646ea5664d06d0eee4569b",
  "source_text_sha256": "b1394661667b48d43d4049ef2ad9660c6060fa0f88646ea5664d06d0eee4569b"
}
~~~

## 呼び出し元

- [00c5e9c0](../00c5e/00c5e9c0.md)

## 呼び出し先

- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5be90](../00c5b/00c5be90.md)
- [00c5bea0](../00c5b/00c5bea0.md)

## 疑似コード / UTF-8 1236 bytes

~~~c

void _ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
               (long param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  
                    /* catch() { ... } // from try @ 00bcac44 with catch @ 00bcaf84
                       catch() { ... } // from try @ 00bcadfc with catch @ 00bcaf84 */
                    /* catch() { ... } // from try @ 00bcad4c with catch @ 00bcaf8c */
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = param_2;
  lVar1 = param_1 + 0x30;
  _ZN8firebase12FutureHandleC1ERKS0_(lVar1,param_3);
  (**(code **)(**(long **)(param_1 + 0x28) + 0x10))(*(long **)(param_1 + 0x28),lVar1);
  _ZN8firebase12FutureHandle6DetachEv(lVar1);
  plVar2 = *(long **)(param_1 + 0x28);
                    /* try { // try from 00bcafc4 to 00ccb03f has its CatchHandler @ 00bcafc4
                       catch() { ... } // from try @ 00bcafc4 with catch @ 00bcafc4
                       catch() { ... } // from try @ 00bcb094 with catch @ 00bcafc4
                       catch() { ... } // from try @ 00bcb174 with catch @ 00bcafc4 */
  if (plVar2 != (long *)0x0) {
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
  return;
}

~~~
