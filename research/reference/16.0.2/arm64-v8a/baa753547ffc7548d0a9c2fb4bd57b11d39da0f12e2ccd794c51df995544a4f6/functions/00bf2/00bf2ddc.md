# 00bf2ddc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf2d40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf2/00bf2d40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0040.md#compare-75e17246050cbef281a222ecca341f0f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0038.md#compare-b29dbbc3048d2eaf98169fc1179adb5e)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf2ddc",
  "name": "_ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "344907972019704771b42c4eb9611bc61d536bd8c1b26df32591aa8ce217b85d",
  "source_text_sha256": "344907972019704771b42c4eb9611bc61d536bd8c1b26df32591aa8ce217b85d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58520](../00c58/00c58520.md)

## 疑似コード / UTF-8 848 bytes

~~~c

long _ZNKSt6__ndk112basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEE17find_first_not_ofEPKwmm
               (byte *param_1,wchar_t *param_2,ulong param_3,size_t param_4)

{
  ulong uVar1;
  byte *pbVar2;
  wchar_t *pwVar3;
  wchar_t *pwVar4;
  long lVar5;
  
  uVar1 = (ulong)(*param_1 >> 1);
  pbVar2 = param_1 + 4;
  if ((*param_1 & 1) != 0) {
    uVar1 = *(ulong *)(param_1 + 8);
    pbVar2 = *(byte **)(param_1 + 0x10);
  }
  if (param_3 < uVar1) {
    pwVar4 = (wchar_t *)(pbVar2 + param_3 * 4);
    if (param_4 == 0) {
LAB_00bf2e58:
      return (long)pwVar4 - (long)pbVar2 >> 2;
    }
    lVar5 = uVar1 * 4 + param_3 * -4;
    do {
      pwVar3 = wmemchr(param_2,*pwVar4,param_4);
      if (pwVar3 == (wchar_t *)0x0) goto LAB_00bf2e58;
      lVar5 = lVar5 + -4;
      pwVar4 = pwVar4 + 1;
    } while (lVar5 != 0);
  }
  return -1;
}

~~~
