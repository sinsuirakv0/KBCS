# 00bdb8ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00bdb8ac",
  "name": "_ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokeneqERKS2_",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ba18306884232b3b50d7c26c635b9c9edd3b0c5597c57b4ed90e9242e5c79ba1",
  "source_text_sha256": "ba18306884232b3b50d7c26c635b9c9edd3b0c5597c57b4ed90e9242e5c79ba1"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c300](../00c5c/00c5c300.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

## 疑似コード / UTF-8 486 bytes

~~~c

bool _ZNK8firebase4auth17PhoneAuthProvider19ForceResendingTokeneqERKS2_
               (undefined8 *param_1,undefined8 *param_2)

{
  char cVar1;
  long lVar2;
  long *plVar3;
  
  lVar2 = _ZN8firebase10app_common9GetAnyAppEv();
  if (lVar2 == 0) {
    _ZN8firebase9LogAssertEPKcz("app != nullptr");
  }
  plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar2);
  cVar1 = (**(code **)(*plVar3 + 0xc0))(plVar3,*(undefined8 *)*param_1,*(undefined8 *)*param_2);
  return cVar1 != '\0';
}

~~~
