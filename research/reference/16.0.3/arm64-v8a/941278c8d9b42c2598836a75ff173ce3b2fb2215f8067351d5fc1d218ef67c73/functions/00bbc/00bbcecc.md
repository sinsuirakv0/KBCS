# 00bbcecc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bbcecc",
  "name": "_ZN8firebase9messaging21UnsubscribeLastResultEv",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d8b13a43e87a17ffff4af9f4090a472f3d8cc91a6c10f23c44a412fa9ba7bc68",
  "source_text_sha256": "d8b13a43e87a17ffff4af9f4090a472f3d8cc91a6c10f23c44a412fa9ba7bc68"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bc80](../00c5b/00c5bc80.md)
- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5bdf0](../00c5b/00c5bdf0.md)
- [00c5beb0](../00c5b/00c5beb0.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5e310](../00c5e/00c5e310.md)

## 関連文字列（未確認候補）

~~~text
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 976 bytes

~~~c

void _ZN8firebase9messaging21UnsubscribeLastResultEv(long param_1)

{
  long lVar1;
  long lVar2;
  
                    /* try { // try from 00bbced0 to 00cbcf5f has its CatchHandler @ 00bbc990 */
  if (DAT_01127420 == 0) {
    _ZN8firebase9LogAssertEPKcz("internal::IsInitialized()");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* try { // try from 00bbcf60 to 00cbcf83 has its CatchHandler @ 00bbd800 */
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar1 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase5Mutex7AcquireEv(lVar1 + 8);
    lVar2 = *(long *)(lVar1 + 0x50);
    _ZN8firebase5Mutex7ReleaseEv(lVar1 + 8);
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
    _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0x80);
  }
  return;
}

~~~
