# 00afcec4

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afce80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afc/00afce80.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/high-0008.md#compare-8349615a16dee2126080fb89ee4907d4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcec4",
  "name": "_INIT_273",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ed2407d1fecac19070c8fa3707bcafd87a42391a30f22b0ad0fed4214b1af04e",
  "source_text_sha256": "ed2407d1fecac19070c8fa3707bcafd87a42391a30f22b0ad0fed4214b1af04e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdde20](../00bdd/00bdde20.md)

## 疑似コード / UTF-8 337 bytes

~~~c

void _INIT_273(void)

{
  undefined8 uVar1;
  
  uVar1 = _Znwm(0x28);
  _ZN8firebase5MutexC2ENS0_4ModeE(uVar1,1);
                    /* try { // try from 00afcef0 to 00bfcf07 has its CatchHandler @ 00aff3f0 */
  *(undefined8 *)PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c1b998 =
       uVar1;
  return;
}

~~~
