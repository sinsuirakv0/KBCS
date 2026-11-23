# 00afb8bc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afb494`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afb/00afb494.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0036.md#compare-5f74ae60bb290bcbfb3876746a35b4dd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0073.md#compare-9e1be7234d8f04c7cc9b5705ab001dcb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb8bc",
  "name": "FUN_00afb8bc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "71397090cad051e4d0f58bdd6b3c9002b1113c308832cce5edb5eadc01a6ff5e",
  "source_text_sha256": "71397090cad051e4d0f58bdd6b3c9002b1113c308832cce5edb5eadc01a6ff5e"
}
~~~

## 呼び出し元

- [00700af8](../00700/00700af8.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 183 bytes

~~~c

bool FUN_00afb8bc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849b8) != 0;
}

~~~
