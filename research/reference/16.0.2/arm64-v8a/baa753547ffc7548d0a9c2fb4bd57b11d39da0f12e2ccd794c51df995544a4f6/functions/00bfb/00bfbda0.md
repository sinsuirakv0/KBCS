# 00bfbda0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbd04`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbd04.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0041.md#compare-47be016882b36d68a0ecee7aed54f7cb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0039.md#compare-73e7e2afa4e92a4181ec0a119faa6062)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbda0",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bdc166147001eed9a20f9ac35b4d392885538b25e366131393c3a8bd8c799fc0",
  "source_text_sha256": "bdc166147001eed9a20f9ac35b4d392885538b25e366131393c3a8bd8c799fc0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 764 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE6snextcEv(long *param_1)

{
  ulong uVar1;
  byte *pbVar2;
  
  if ((byte *)param_1[3] == (byte *)param_1[4]) {
    uVar1 = (**(code **)(*param_1 + 0x50))();
    if ((int)uVar1 == -1) {
      return uVar1;
    }
    pbVar2 = (byte *)param_1[3];
    if (pbVar2 == (byte *)param_1[4]) goto LAB_00bfbdfc;
  }
  else {
    pbVar2 = (byte *)param_1[3] + 1;
    param_1[3] = (long)pbVar2;
    if (pbVar2 == (byte *)param_1[4]) {
LAB_00bfbdfc:
                    /* WARNING: Could not recover jumptable at 0x00bfbe10. Too many branches */
                    /* WARNING: Treating indirect jump as call */
      uVar1 = (**(code **)(*param_1 + 0x48))();
      return uVar1;
    }
  }
  return (ulong)*pbVar2;
}

~~~
