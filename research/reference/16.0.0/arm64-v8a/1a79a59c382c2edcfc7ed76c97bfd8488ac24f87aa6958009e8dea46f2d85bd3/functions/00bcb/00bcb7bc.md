# 00bcb7bc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcb7bc",
  "name": "_ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "629c335216e227598cd1c1a8fb6b2e2ab3f48f4c25505a8f4814be4fa3587722",
  "source_text_sha256": "629c335216e227598cd1c1a8fb6b2e2ab3f48f4c25505a8f4814be4fa3587722"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5a870](../00c5a/00c5a870.md)
- [00c5a950](../00c5a/00c5a950.md)
- [00c5aa10](../00c5a/00c5aa10.md)

## 疑似コード / UTF-8 487 bytes

~~~c

void _ZNK8firebase4auth4Auth27SignInAnonymouslyLastResultEv(long param_1,long *param_2)

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
  _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0x100);
  return;
}

~~~
