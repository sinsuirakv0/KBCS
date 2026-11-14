# 00bdb9fc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdb9fc",
  "name": "_ZN8firebase4auth17PhoneAuthProvider8ListenerC2Ev",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9b66e6e0a8cdbb69f614b359eb1ba52b20ba1d3f52188938b9ad3797cf0384d6",
  "source_text_sha256": "9b66e6e0a8cdbb69f614b359eb1ba52b20ba1d3f52188938b9ad3797cf0384d6"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00589a54](../00589/00589a54.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c300](../00c5c/00c5c300.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

## 疑似コード / UTF-8 672 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider8ListenerC2Ev(long *param_1)

{
  undefined8 *puVar1;
  long lVar2;
  long *plVar3;
  undefined8 uVar4;
  
  *param_1 = (long)(PTR__ZTVN8firebase4auth17PhoneAuthProvider8ListenerE_00c9cae0 + 0x10);
  puVar1 = (undefined8 *)_Znwm(8);
  *puVar1 = 0;
  param_1[1] = (long)puVar1;
  lVar2 = _ZN8firebase10app_common9GetAnyAppEv();
  if (lVar2 == 0) {
    _ZN8firebase9LogAssertEPKcz("app != nullptr");
  }
  plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar2);
  uVar4 = FUN_00589a54(plVar3,DAT_01127d70,DAT_01127d80,param_1);
  uVar4 = (**(code **)(*plVar3 + 0xa8))(plVar3,uVar4);
  *(undefined8 *)param_1[1] = uVar4;
  return;
}

~~~
