# 00bccbe4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bccbe4",
  "name": "_ZNK8firebase4auth4Auth45SignInAndRetrieveDataWithCredentialLastResultEv",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41f3fd47da22ca213fa72c117123d81561bf718ec543db87b647d60f26555c73",
  "source_text_sha256": "41f3fd47da22ca213fa72c117123d81561bf718ec543db87b647d60f26555c73"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5bd10](../00c5b/00c5bd10.md)
- [00c5bdf0](../00c5b/00c5bdf0.md)
- [00c5beb0](../00c5b/00c5beb0.md)

## 疑似コード / UTF-8 714 bytes

~~~c

void _ZNK8firebase4auth4Auth45SignInAndRetrieveDataWithCredentialLastResultEv
               (long param_1,long *param_2)

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
                    /* try { // try from 00bccc2c to 00cccc37 has its CatchHandler @ 00bccc90 */
  _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
                    /* try { // try from 00bccc38 to 00ccccb7 has its CatchHandler @ 00bccbc0 */
  _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0xc0);
  return;
}

~~~
