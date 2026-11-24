# 00bffcf4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffc58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffc58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/reference_unresolved-0001.md#compare-edf712ddd5d28531c47f79844b31686e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/reference_unresolved-0001.md#compare-d9d87f56d1d2aac17f57848a6295dd42)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffcf4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE9sputbackcEw",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99a147f332c44e4b2a67a5b71a02db0c3925e0f4636d54bfb5b1a64a65c60024",
  "source_text_sha256": "99a147f332c44e4b2a67a5b71a02db0c3925e0f4636d54bfb5b1a64a65c60024"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 520 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE9sputbackcEw(long *param_1,uint param_2)

{
  ulong uVar1;
  uint *puVar2;
  
  if ((param_1[2] != param_1[3]) && (puVar2 = (uint *)(param_1[3] + -4), *puVar2 == param_2)) {
    param_1[3] = (long)puVar2;
    return (ulong)param_2;
  }
                    /* WARNING: Could not recover jumptable at 0x00bffd28. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar1 = (**(code **)(*param_1 + 0x58))();
  return uVar1;
}

~~~
