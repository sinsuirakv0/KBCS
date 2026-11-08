# 00b6afcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00b6afcc",
  "name": "_ZN8firebase4auth17PhoneAuthProvider8ListenerD1Ev",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f456947af486f0c6c6ff6cd0df263c6609dbcd1ac3b1e78d19c92cc1113c79b4",
  "source_text_sha256": "f456947af486f0c6c6ff6cd0df263c6609dbcd1ac3b1e78d19c92cc1113c79b4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bde080](../00bde/00bde080.md)
- [00bde100](../00bde/00bde100.md)
- [00bde2e0](../00bde/00bde2e0.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

## 疑似コード / UTF-8 614 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider8ListenerD1Ev(long *param_1)

{
  long lVar1;
  long *plVar2;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth17PhoneAuthProvider8ListenerE_00c1bb10 + 0x10);
  lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
  if (lVar1 == 0) {
    _ZN8firebase9LogAssertEPKcz("app != nullptr");
  }
  plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
  FUN_00551e14(plVar2,*(undefined8 *)param_1[1],DAT_010a18c0);
  (**(code **)(*plVar2 + 0xb0))(plVar2,*(undefined8 *)param_1[1]);
  if ((void *)param_1[1] != (void *)0x0) {
    _ZdlPv((void *)param_1[1]);
    return;
  }
  return;
}

~~~
