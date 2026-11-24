# 00bfffdc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfff40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bfff40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0042.md#compare-97453beba79cd46d73fa30fd9425cf52)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0039.md#compare-2f1eee283ca7385b1486d096e60b5edd)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfffdc",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsgetnEPwl",
  "size": 212,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "351d37c3ec9ec468fa4b026c45dcd60a979d8f71016d0969542a756df55e5109",
  "source_text_sha256": "351d37c3ec9ec468fa4b026c45dcd60a979d8f71016d0969542a756df55e5109"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58010](../00c58/00c58010.md)

## 疑似コード / UTF-8 1164 bytes

~~~c

long _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE6xsgetnEPwl
               (long *param_1,int *param_2,long param_3)

{
  long lVar1;
  int iVar2;
  void *__src;
  long lVar3;
  long lVar4;
  int *piVar5;
  
  if (param_3 < 1) {
    lVar4 = 0;
  }
  else {
    lVar4 = 0;
    do {
      __src = (void *)param_1[3];
      if (__src < (void *)param_1[4]) {
        lVar3 = param_1[4] - (long)__src >> 2;
        lVar1 = param_3 - lVar4;
        if (lVar3 <= param_3 - lVar4) {
          lVar1 = lVar3;
        }
        lVar3 = lVar1;
        if (0x7ffffffe < lVar1) {
          lVar3 = 0x7fffffff;
        }
        if (lVar1 != 0) {
          memmove(param_2,__src,lVar3 << 2);
          __src = (void *)param_1[3];
        }
        piVar5 = param_2 + lVar3;
        param_1[3] = (long)((long)__src + (long)(int)lVar3 * 4);
      }
      else {
        iVar2 = (**(code **)(*param_1 + 0x50))(param_1);
        if (iVar2 == -1) {
          return lVar4;
        }
        lVar3 = 1;
        piVar5 = param_2 + 1;
        *param_2 = iVar2;
      }
      lVar4 = lVar3 + lVar4;
      param_2 = piVar5;
    } while (lVar4 < param_3);
  }
  return lVar4;
}

~~~
