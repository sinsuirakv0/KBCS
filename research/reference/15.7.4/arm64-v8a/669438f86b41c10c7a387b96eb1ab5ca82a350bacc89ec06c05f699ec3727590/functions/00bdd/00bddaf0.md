# 00bddaf0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddaa0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddaa0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0017.md#compare-1e286e01c8e4cad19b346794e287353d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddaf0",
  "name": "_ZN8firebase9analytics9TerminateEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c752812b7995c2ca0ba1e40d0818cbfeb17dffc2781495309f1053945d2ff8f7",
  "source_text_sha256": "c752812b7995c2ca0ba1e40d0818cbfeb17dffc2781495309f1053945d2ff8f7"
}
~~~

## 呼び出し元

- [00845f00](../00845/00845f00.md)
- [00ae00a4](../00ae0/00ae00a4.md)
- [00ae0580](../00ae0/00ae0580.md)

## 呼び出し先

- [00ae1358](../00ae1/00ae1358.md)

## 疑似コード / UTF-8 127 bytes

~~~c

void _ZN8firebase9analytics9TerminateEv(void)

{
  (*(code *)PTR__ZN8firebase9analytics9TerminateEv_00c1d630)();
  return;
}

~~~
