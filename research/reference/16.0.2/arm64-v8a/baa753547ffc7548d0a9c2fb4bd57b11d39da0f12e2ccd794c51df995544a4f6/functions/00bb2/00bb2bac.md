# 00bb2bac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb2b10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb2b10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0078.md#compare-e4322aae82520c02edc418e9d7cb1a8e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0091.md#compare-cae41d574db5844793fc5c99a9d6c6f8)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb2bac",
  "name": "_ZN11flatbuffers21SetFileExistsFunctionEPFbPKcE",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e69b3f3ae5656ee822b49a48234c2efa13be03e785e304766e36a4bd976ca8a4",
  "source_text_sha256": "e69b3f3ae5656ee822b49a48234c2efa13be03e785e304766e36a4bd976ca8a4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 377 bytes

~~~c

undefined * _ZN11flatbuffers21SetFileExistsFunctionEPFbPKcE(code *param_1)

{
  code *pcVar1;
  undefined *puVar2;
  
                    /* try { // try from 00bb2bac to 00cb2ea7 has its CatchHandler @ 00bb2b48 */
  pcVar1 = FUN_00bb2bd0;
  if (param_1 != (code *)0x0) {
    pcVar1 = param_1;
  }
  puVar2 = PTR_FUN_00ca4780;
  PTR_FUN_00ca4780 = pcVar1;
  return puVar2;
}

~~~
