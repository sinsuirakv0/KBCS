# 00bdf4dc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdf0b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdf/00bdf0b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0085.md#compare-d6250dc506d099154ee6c20927eec39b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0095.md#compare-3a6bfb742a991cefd3e58dcda6e20787)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdf4dc",
  "name": "_ZNK8firebase4auth22AndroidWrappedUserInfo12display_nameEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8a8567ffe22efd1f1cbc03976c15276957a74a64ce119b98277349c2579e5239",
  "source_text_sha256": "8a8567ffe22efd1f1cbc03976c15276957a74a64ce119b98277349c2579e5239"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497834](../00497/00497834.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b390](../00c5b/00c5b390.md)

## 疑似コード / UTF-8 749 bytes

~~~c

void _ZNK8firebase4auth22AndroidWrappedUserInfo12display_nameEv(undefined8 *param_1,long param_2)

{
  long lVar1;
  undefined8 uVar2;
  long lVar3;
  ulong uVar4;
  
  lVar1 = *(long *)(param_2 + 0xa0);
  uVar2 = _ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x98));
  lVar3 = 0;
  if (lVar1 != 0) {
    lVar3 = FUN_00497834(uVar2,lVar1,DAT_01126dd0);
  }
  uVar4 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(uVar2);
                    /* try { // try from 00bdf524 to 00cdf577 has its CatchHandler @ 00be07b4 */
  if ((lVar3 != 0) && ((uVar4 & 1) == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(param_1,uVar2,lVar3);
    return;
  }
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  return;
}

~~~
