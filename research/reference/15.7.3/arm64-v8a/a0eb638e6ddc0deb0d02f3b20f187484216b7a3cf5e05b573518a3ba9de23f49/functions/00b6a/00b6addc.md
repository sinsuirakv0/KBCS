# 00b6addc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b6ad14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b6a/00b6ad14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0073.md#compare-98e9c4f2f5e485c6ff2e29b1bb47d532)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6addc",
  "name": "_ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed2a9fe3c2749cc7e0759da0b730520b864554c075b5221630560ebc436a316a",
  "source_text_sha256": "ed2a9fe3c2749cc7e0759da0b730520b864554c075b5221630560ebc436a316a"
}
~~~

## 呼び出し元

- [00be0df0](../00be0/00be0df0.md)

## 呼び出し先

- [00bde130](../00bde/00bde130.md)
- [00bde1b0](../00bde/00bde1b0.md)
- [00bde390](../00bde/00bde390.md)

## 関連文字列（未確認候補）

~~~text
"app != nullptr"
~~~

## 疑似コード / UTF-8 748 bytes

~~~c

void _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject(long *param_1,long param_2)

{
  long lVar1;
  long *plVar2;
  
  if (*param_1 != 0) {
    lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
    if (lVar1 == 0) {
      _ZN8firebase9LogAssertEPKcz("app != nullptr");
    }
    plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
    (**(code **)(*plVar2 + 0xb0))(plVar2,*param_1);
    *param_1 = 0;
  }
  lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
  if (lVar1 == 0) {
    _ZN8firebase9LogAssertEPKcz("app != nullptr");
  }
  plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
  if (param_2 == 0) {
    lVar1 = 0;
  }
  else {
    lVar1 = (**(code **)(*plVar2 + 0xa8))(plVar2,param_2);
  }
  *param_1 = lVar1;
  return;
}

~~~
