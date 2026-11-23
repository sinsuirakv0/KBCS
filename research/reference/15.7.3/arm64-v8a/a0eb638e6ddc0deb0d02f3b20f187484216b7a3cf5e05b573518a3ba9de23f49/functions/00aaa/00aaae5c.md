# 00aaae5c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aaad94`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaad94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/inspection-0001.md#compare-d48bc6efc042c3ee0fd168bc0dd52431)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaae5c",
  "name": "FUN_00aaae5c",
  "size": 328,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9de3ab0e60effabf0bfe5d87df3af35b7affd9262c87c4e0493cb9162c8d36d",
  "source_text_sha256": "e9de3ab0e60effabf0bfe5d87df3af35b7affd9262c87c4e0493cb9162c8d36d"
}
~~~

## 呼び出し元

- [0079bdf0](../0079b/0079bdf0.md)
- [00a72648](../00a72/00a72648.md)

## 呼び出し先

- [007cf950](../007cf/007cf950.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [0081f580](../0081f/0081f580.md)
- [00aaa6bc](../00aaa/00aaa6bc.md)
- [00bdb5b0](../00bdb/00bdb5b0.md)

## 疑似コード / UTF-8 1823 bytes

~~~c

undefined8 FUN_00aaae5c(long param_1,ulong param_2,ulong param_3,ulong param_4)

{
  long lVar1;
  wchar_t *pwVar2;
  long lVar3;
  wchar_t *pwVar4;
  long lVar5;
  
  if ((int)param_2 == -1) {
    param_2 = FUN_007cf950(0);
    param_2 = param_2 & 0xffffffff;
    param_3 = FUN_007cfaa0();
    param_3 = param_3 & 0xffffffff;
    param_4 = FUN_007cfcd8();
    param_4 = param_4 & 0xffffffff;
  }
  FUN_00aaa6bc(param_1,param_2,param_3,param_4);
  lVar5 = 0;
  while( true ) {
    lVar3 = FUN_0081f580();
    lVar1 = lVar3 + lVar5;
    if (((uint)(*(byte *)(lVar3 + 0xc76e) ^ *(byte *)(lVar1 + 0xc746)) << 0x10 |
         (uint)(*(byte *)(lVar3 + 0xc76f) ^ *(byte *)(lVar1 + 0xc747)) << 0x18 |
         (uint)(*(byte *)(lVar3 + 0xc76d) ^ *(byte *)(lVar1 + 0xc745)) << 8 |
        (uint)(*(byte *)(lVar3 + 0xc76c) ^ *(byte *)(lVar1 + 0xc744))) == 0xffffffff) {
      return 0;
    }
    lVar3 = FUN_0081f580();
    lVar1 = lVar3 + lVar5;
    pwVar2 = *(wchar_t **)(param_1 + 0x38);
    pwVar4 = wmemchr(*(wchar_t **)(param_1 + 0x30),
                     CONCAT13(*(byte *)(lVar3 + 0xc76f) ^ *(byte *)(lVar1 + 0xc747),
                              CONCAT12(*(byte *)(lVar3 + 0xc76e) ^ *(byte *)(lVar1 + 0xc746),
                                       CONCAT11(*(byte *)(lVar3 + 0xc76d) ^
                                                *(byte *)(lVar1 + 0xc745),
                                                *(byte *)(lVar3 + 0xc76c) ^
                                                *(byte *)(lVar1 + 0xc744)))) + L'\xfffffffe',
                     (long)pwVar2 - (long)*(wchar_t **)(param_1 + 0x30) >> 2);
    if (pwVar4 != (wchar_t *)0x0) {
      pwVar2 = pwVar4;
    }
    if (pwVar2 != *(wchar_t **)(param_1 + 0x38)) break;
    lVar5 = lVar5 + 4;
    if (lVar5 == 0x28) {
      return 0;
    }
  }
  return 1;
}

~~~
