# 00bbcdd8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bbcdd8",
  "name": "_ZN8firebase9messaging18GetTokenLastResultEv",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "830ca9807bb9bb77d453e7800f0488170a1d2ee71a07b0093e9b48ace8ffe6c8",
  "source_text_sha256": "830ca9807bb9bb77d453e7800f0488170a1d2ee71a07b0093e9b48ace8ffe6c8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5acb0](../00c5a/00c5acb0.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5ae20](../00c5a/00c5ae20.md)
- [00c5aee0](../00c5a/00c5aee0.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5d340](../00c5d/00c5d340.md)

## 関連文字列（未確認候補）

~~~text
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 1167 bytes

~~~c

void _ZN8firebase9messaging18GetTokenLastResultEv(long param_1)

{
  long lVar1;
  long lVar2;
  
  if (DAT_01126460 == 0) {
                    /* try { // try from 00bbce4c to 00cbce53 has its CatchHandler @ 00bbcee0 */
    _ZN8firebase9LogAssertEPKcz("internal::IsInitialized()");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
                    /* try { // try from 00bbce68 to 00cbce87 has its CatchHandler @ 00bbceec */
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
  }
  else {
    lVar1 = _ZN8firebase9messaging10FutureData3GetEv();
    _ZN8firebase5Mutex7AcquireEv(lVar1 + 8);
    lVar2 = *(long *)(lVar1 + 0x50);
    _ZN8firebase5Mutex7ReleaseEv(lVar1 + 8);
                    /* try { // try from 00bbce18 to 00cbce1f has its CatchHandler @ 00bbceec */
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC2Ev(param_1 + 0x30);
                    /* try { // try from 00bbce34 to 00cbce3b has its CatchHandler @ 00bbcee4 */
    _ZN8firebase10FutureBaseaSERKS0_(param_1,lVar2 + 0xc0);
  }
  return;
}

~~~
