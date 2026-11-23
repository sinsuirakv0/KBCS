# 00b5faac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b5f9e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b5f/00b5f9e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0009.md#compare-f4bd5bb55f5cb33bff78addb81caffc4)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5faac",
  "name": "_ZN8firebase4auth4Auth7SignOutEv",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "57092d213673760e8207ca96b662e375ad0cee67f2e5baabfac9bfdfa9879dda",
  "source_text_sha256": "57092d213673760e8207ca96b662e375ad0cee67f2e5baabfac9bfdfa9879dda"
}
~~~

## 呼び出し元

- [00bddb60](../00bdd/00bddb60.md)

## 呼び出し先

- [00551e14](../00551/00551e14.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bde090](../00bde/00bde090.md)
- [00bde1b0](../00bde/00bde1b0.md)
- [00be0c30](../00be0/00be0c30.md)

## 疑似コード / UTF-8 512 bytes

~~~c

void _ZN8firebase4auth4Auth7SignOutEv(long *param_1)

{
  undefined8 uVar1;
  long lVar2;
  
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
  FUN_00551e14(uVar1,*(undefined8 *)(*param_1 + 0x1f8),DAT_010a1438);
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  lVar2 = *param_1;
  _ZN8firebase5Mutex7AcquireEv(lVar2 + 0x18);
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,*param_1 + 0x200);
  _ZN8firebase5Mutex7ReleaseEv(lVar2 + 0x18);
  return;
}

~~~
