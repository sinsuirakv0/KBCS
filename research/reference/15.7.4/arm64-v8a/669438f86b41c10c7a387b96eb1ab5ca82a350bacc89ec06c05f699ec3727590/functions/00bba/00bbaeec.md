# 00bbaeec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbaea8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbaea8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0078.md#compare-1d802bfb403122a36c84e212e615ae07)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaeec",
  "name": "_ZNSt14overflow_errorD1Ev",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77ec89ca0d940a7fb84d34cbd433ef99148ffbf8ac86c312c0cbe0ddf49f8adc",
  "source_text_sha256": "77ec89ca0d940a7fb84d34cbd433ef99148ffbf8ac86c312c0cbe0ddf49f8adc"
}
~~~

## 呼び出し元

- [00bdda70](../00bdd/00bdda70.md)
- [00be0f70](../00be0/00be0f70.md)
- [00be0fd0](../00be0/00be0fd0.md)
- [00be11a0](../00be1/00be11a0.md)
- [00be1e80](../00be1/00be1e80.md)

## 呼び出し先

- [00bd6e30](../00bd6/00bd6e30.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb490](../00bdb/00bdb490.md)

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt14overflow_errorD1Ev(long *param_1)

{
  int iVar1;
  long lVar2;
  
  lVar2 = param_1[1];
  *param_1 = (long)(PTR__ZTVSt13runtime_error_00c1bc68 + 0x10);
  iVar1 = FUN_00bd6e30(0xffffffff,lVar2 + -8);
  if (iVar1 + -1 < 0) {
    _ZdlPv((void *)(lVar2 + -0x18));
  }
  _ZNSt20bad_array_new_lengthD1Ev(param_1);
  return;
}

~~~
