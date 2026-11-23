# 00bceff0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5faf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5f/00b5faf0.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/high-0004.md#compare-1239ed369c78fee28a0eb44aa08b8796)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bceff0",
  "name": "_ZN8firebase4auth4Auth7SignOutEv",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df63bb06c0cce2caf2c8595bf4e4173c06290723b8d1dc90a4b3c3630b0cc19d",
  "source_text_sha256": "df63bb06c0cce2caf2c8595bf4e4173c06290723b8d1dc90a4b3c3630b0cc19d"
}
~~~

## 呼び出し元

- [00c5a620](../00c5a/00c5a620.md)

## 呼び出し先

- [00574cac](../00574/00574cac.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5d880](../00c5d/00c5d880.md)

## 疑似コード / UTF-8 512 bytes

~~~c

void _ZN8firebase4auth4Auth7SignOutEv(long *param_1)

{
  undefined8 uVar1;
  long lVar2;
  
  uVar1 = _ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_1);
  FUN_00574cac(uVar1,*(undefined8 *)(*param_1 + 0x1f8),DAT_01126380);
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar1);
  lVar2 = *param_1;
  _ZN8firebase5Mutex7AcquireEv(lVar2 + 0x18);
  _ZN8firebase4auth19SetImplFromLocalRefEP7_JNIEnvP8_jobjectPPv(uVar1,0,*param_1 + 0x200);
  _ZN8firebase5Mutex7ReleaseEv(lVar2 + 0x18);
  return;
}

~~~
