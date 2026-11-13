# 00bcbad0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bcbad0",
  "name": "_ZNK8firebase4auth4Auth32SendPasswordResetEmailLastResultEv",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd61d4afd284a2487dfeedb852752e43213e584e6c9b9dfe3826461096ac633a",
  "source_text_sha256": "fd61d4afd284a2487dfeedb852752e43213e584e6c9b9dfe3826461096ac633a"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5ae20](../00c5a/00c5ae20.md)
- [00c5aee0](../00c5a/00c5aee0.md)

## 疑似コード / UTF-8 492 bytes

~~~c

void _ZNK8firebase4auth4Auth32SendPasswordResetEmailLastResultEv(long param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  
  lVar2 = *param_2;
  lVar1 = lVar2 + 0x18;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  lVar2 = *(long *)(lVar2 + 0x60);
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
  *(undefined8 *)(param_1 + 0x28) = 0;
  _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
  _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0x200);
  return;
}

~~~
