# 00bcfcd4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bcfcd4",
  "name": "_ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "85482b0b1c773adf6c6a6f341e9d2aef955fa3b1ab594b0b984525cb1477f947",
  "source_text_sha256": "85482b0b1c773adf6c6a6f341e9d2aef955fa3b1ab594b0b984525cb1477f947"
}
~~~

## 呼び出し元

- [00c5de10](../00c5d/00c5de10.md)

## 呼び出し先

- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5aec0](../00c5a/00c5aec0.md)
- [00c5aed0](../00c5a/00c5aed0.md)

## 疑似コード / UTF-8 1349 bytes

~~~c

void _ZN8firebase6FutureINS_4auth4Auth20FetchProvidersResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
               (long param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = param_2;
  lVar1 = param_1 + 0x30;
  _ZN8firebase12FutureHandleC1ERKS0_(lVar1,param_3);
  (**(code **)(**(long **)(param_1 + 0x28) + 0x10))(*(long **)(param_1 + 0x28),lVar1);
  _ZN8firebase12FutureHandle6DetachEv(lVar1);
  plVar2 = *(long **)(param_1 + 0x28);
  if (plVar2 != (long *)0x0) {
                    /* try { // try from 00bcfd30 to 00ccff0f has its CatchHandler @ 00bcfd30
                       catch() { ... } // from try @ 00bcfd30 with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bcff1c with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bcff98 with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bcfff8 with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bd01d8 with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bd0234 with catch @ 00bcfd30
                       catch() { ... } // from try @ 00bd02f8 with catch @ 00bcfd30 */
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
  return;
}

~~~
