# 00bdaa9c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00bdaa9c",
  "name": "_ZN8firebase4auth17PhoneAuthProvider8ListenerD2Ev",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42a6e64f7caf4588f45e8cc16694a9e6c4937499e9b7d92ce0ae99b28d595879",
  "source_text_sha256": "42a6e64f7caf4588f45e8cc16694a9e6c4937499e9b7d92ce0ae99b28d595879"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00574d2c](../00574/00574d2c.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5b330](../00c5b/00c5b330.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

## 疑似コード / UTF-8 614 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider8ListenerD2Ev(long *param_1)

{
  long lVar1;
  long *plVar2;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth17PhoneAuthProvider8ListenerE_00c9bb10 + 0x10);
  lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
  if (lVar1 == 0) {
    _ZN8firebase9LogAssertEPKcz("app != nullptr");
  }
  plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
  FUN_00574d2c(plVar2,*(undefined8 *)param_1[1],DAT_01126dc8);
  (**(code **)(*plVar2 + 0xb0))(plVar2,*(undefined8 *)param_1[1]);
  if ((void *)param_1[1] != (void *)0x0) {
    _ZdlPv((void *)param_1[1]);
    return;
  }
  return;
}

~~~
