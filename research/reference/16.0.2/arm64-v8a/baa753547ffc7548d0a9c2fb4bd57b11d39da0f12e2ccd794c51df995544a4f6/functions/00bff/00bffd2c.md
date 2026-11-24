# 00bffd2c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffc90`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffc90.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/reference_unresolved-0001.md#compare-ec3a3ec267c1215f4948e64ba189d357)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/reference_unresolved-0001.md#compare-33091119010c6f9f3c6abe24c9609c32)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffd2c",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE7sungetcEv",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3c7e3fa38c5cdaf0eb2045217860649a6a39ad8d962f37f3f0d6bdc66f92cec",
  "source_text_sha256": "d3c7e3fa38c5cdaf0eb2045217860649a6a39ad8d962f37f3f0d6bdc66f92cec"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 534 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE7sungetcEv(long *param_1)

{
  uint uVar1;
  ulong uVar2;
  uint *puVar3;
  
  if (param_1[2] != param_1[3]) {
    puVar3 = (uint *)(param_1[3] + -4);
    uVar1 = *puVar3;
    param_1[3] = (long)puVar3;
    return (ulong)uVar1;
  }
                    /* WARNING: Could not recover jumptable at 0x00bffd5c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar2 = (**(code **)(*param_1 + 0x58))(param_1,0xffffffff);
  return uVar2;
}

~~~
