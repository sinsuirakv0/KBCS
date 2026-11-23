# 00bff7cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b82d84`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b82d84.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/reference_unresolved-0001.md#compare-a73708c9f221455a434a55a8c9fc3652)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bff7cc",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6sbumpcEv",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b9be2bd443faab84ed7b31135866e848e6df90da16ed6a133379c3c225bc19ce",
  "source_text_sha256": "b9be2bd443faab84ed7b31135866e848e6df90da16ed6a133379c3c225bc19ce"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 523 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6sbumpcEv(long *param_1)

{
  uint *puVar1;
  uint uVar2;
  ulong uVar3;
  
  puVar1 = (uint *)param_1[3];
  if (puVar1 != (uint *)param_1[4]) {
    uVar2 = *puVar1;
    param_1[3] = (long)(puVar1 + 1);
    return (ulong)uVar2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bff7f8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar3 = (**(code **)(*param_1 + 0x50))(param_1);
  return uVar3;
}

~~~
