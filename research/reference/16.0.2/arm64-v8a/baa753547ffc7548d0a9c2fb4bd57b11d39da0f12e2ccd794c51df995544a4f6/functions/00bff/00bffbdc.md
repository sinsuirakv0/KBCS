# 00bffbdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffb40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffb40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/reference_unresolved-0001.md#compare-047f56273b254c92e3e0773514710951)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/reference_unresolved-0001.md#compare-dbe79fd03b25247be313dcf098457a9a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffbdc",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8in_availEv",
  "size": 40,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a5242ff87ed926a138a0843e7934c1af57247d4450860301d6706786a46b3dc8",
  "source_text_sha256": "a5242ff87ed926a138a0843e7934c1af57247d4450860301d6706786a46b3dc8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 422 bytes

~~~c

long _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE8in_availEv(long *param_1)

{
  long lVar1;
  
  if ((ulong)param_1[3] < (ulong)param_1[4]) {
    return param_1[4] - param_1[3] >> 2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bffc00. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  lVar1 = (**(code **)(*param_1 + 0x38))();
  return lVar1;
}

~~~
