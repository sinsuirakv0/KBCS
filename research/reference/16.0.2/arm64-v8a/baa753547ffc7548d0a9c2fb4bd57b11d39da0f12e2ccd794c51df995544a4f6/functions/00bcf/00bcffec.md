# 00bcffec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bcffec",
  "name": "_ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c978b6a19a360d3ead809f673307e1ee601625444d56061f63f61acb6b8b78f3",
  "source_text_sha256": "c978b6a19a360d3ead809f673307e1ee601625444d56061f63f61acb6b8b78f3"
}
~~~

## 呼び出し元

- [00c5de00](../00c5d/00c5de00.md)

## 呼び出し先

- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5aec0](../00c5a/00c5aec0.md)
- [00c5aed0](../00c5a/00c5aed0.md)

## 疑似コード / UTF-8 843 bytes

~~~c

void _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
               (long param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  
                    /* try { // try from 00bcffec to 00ccfff7 has its CatchHandler @ 00bd03e4 */
                    /* try { // try from 00bcfff8 to 00cd01bf has its CatchHandler @ 00bcfd30 */
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = param_2;
  lVar1 = param_1 + 0x30;
  _ZN8firebase12FutureHandleC1ERKS0_(lVar1,param_3);
  (**(code **)(**(long **)(param_1 + 0x28) + 0x10))(*(long **)(param_1 + 0x28),lVar1);
  _ZN8firebase12FutureHandle6DetachEv(lVar1);
  plVar2 = *(long **)(param_1 + 0x28);
  if (plVar2 != (long *)0x0) {
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
  return;
}

~~~
