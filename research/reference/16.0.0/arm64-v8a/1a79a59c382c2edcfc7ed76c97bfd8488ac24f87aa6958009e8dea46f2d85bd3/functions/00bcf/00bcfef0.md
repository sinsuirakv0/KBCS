# 00bcfef0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcfef0",
  "name": "_ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4f5959084491e868f9ae074070ee72b2d66fb689cd5118b55cb0c78065665764",
  "source_text_sha256": "4f5959084491e868f9ae074070ee72b2d66fb689cd5118b55cb0c78065665764"
}
~~~

## 呼び出し元

- [00c5d950](../00c5d/00c5d950.md)

## 呼び出し先

- [00c5a870](../00c5a/00c5a870.md)
- [00c5a9f0](../00c5a/00c5a9f0.md)
- [00c5aa00](../00c5a/00c5aa00.md)

## 疑似コード / UTF-8 739 bytes

~~~c

void _ZN8firebase6FutureINS_4auth4UserEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
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
                    /* try { // try from 00bcff54 to 00ccff6b has its CatchHandler @ 00bd0170 */
    (**(code **)(*plVar2 + 0x58))(plVar2,param_1);
  }
  return;
}

~~~
