# 00bb6dbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bb6dbc",
  "name": "_ZN8firebase9messaging16PollableListenerC2Ev",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8671ffee3722dd7f2b13eb49dcac3ea5b81e9a2e701563500db93948506967c5",
  "source_text_sha256": "8671ffee3722dd7f2b13eb49dcac3ea5b81e9a2e701563500db93948506967c5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)
- [00c5ad50](../00c5a/00c5ad50.md)

## 疑似コード / UTF-8 829 bytes

~~~c

void _ZN8firebase9messaging16PollableListenerC2Ev(long *param_1)

{
  long lVar1;
  
  *param_1 = (long)(PTR__ZTVN8firebase9messaging16PollableListenerE_00c9b9d0 + 0x10);
  lVar1 = _Znwm(0xa0);
  _ZN8firebase5MutexC1ENS0_4ModeE(lVar1,1);
  *(undefined8 *)(lVar1 + 0x98) = 0;
  *(undefined8 *)(lVar1 + 0x90) = 0;
  *(undefined8 *)(lVar1 + 0x88) = 0;
  *(undefined8 *)(lVar1 + 0x80) = 0;
  *(undefined8 *)(lVar1 + 0x78) = 0;
  *(undefined8 *)(lVar1 + 0x70) = 0;
  *(undefined8 *)(lVar1 + 0x68) = 0;
  *(undefined8 *)(lVar1 + 0x60) = 0;
  *(undefined8 *)(lVar1 + 0x58) = 0;
  *(undefined8 *)(lVar1 + 0x50) = 0;
  *(undefined8 *)(lVar1 + 0x48) = 0;
  *(undefined8 *)(lVar1 + 0x40) = 0;
  *(undefined8 *)(lVar1 + 0x38) = 0;
  *(undefined8 *)(lVar1 + 0x30) = 0;
  *(undefined8 *)(lVar1 + 0x28) = 0;
  param_1[1] = lVar1;
  return;
}

~~~
