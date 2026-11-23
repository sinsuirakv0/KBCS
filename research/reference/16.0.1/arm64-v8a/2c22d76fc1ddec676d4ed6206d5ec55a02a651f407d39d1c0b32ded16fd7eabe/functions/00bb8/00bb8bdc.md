# 00bb8bdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb87b4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb8/00bb87b4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0079.md#compare-c5a48079724fbf0c43c49c394877e67d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0088.md#compare-29ab9791eb62cdde3f71d2ca6f5cc460)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb8bdc",
  "name": "_INIT_285",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8249224c0e645bd9b3999a8e5b43d722ba6c34fd3cfee1d93cd2af7a8e107f5",
  "source_text_sha256": "b8249224c0e645bd9b3999a8e5b43d722ba6c34fd3cfee1d93cd2af7a8e107f5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e30](../00c57/00c57e30.md)
- [00c5abc0](../00c5a/00c5abc0.md)
- [00c5ac80](../00c5a/00c5ac80.md)

## 関連文字列（未確認候補）

~~~text
"messaging"
~~~

## 疑似コード / UTF-8 434 bytes

~~~c

void _INIT_285(void)

{
                    /* try { // try from 00bb8be0 to 00cb8c57 has its CatchHandler @ 00bb910c */
  DAT_011261e8 = "messaging";
  DAT_011261f0 = FUN_00bb66a4;
  DAT_011261f8 = FUN_00bb66e4;
  DAT_01126200 = 0;
  _ZN8firebase11AppCallback11AddCallbackEPS0_();
  _ZN8firebase5MutexC1ENS0_4ModeE(&DAT_01126208,1);
  __cxa_atexit(PTR__ZN8firebase5MutexD1Ev_00c9b678,&DAT_01126208,&PTR_LOOP_00c62f90);
  return;
}

~~~
