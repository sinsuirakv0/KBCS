# 00aed3dc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/review-0080.md#review-62f66a7437aae4688f0fbcb4c95da57f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 要確認
  - [v16.0.2 → v16.0.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/review-0043.md#review-62f66a7437aae4688f0fbcb4c95da57f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aed3dc",
  "name": "FUN_00aed3dc",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41e9e37a363196f36b7ef52571d4204b8c5840bd18c34c7b3f0726d79fca1b8e",
  "source_text_sha256": "41e9e37a363196f36b7ef52571d4204b8c5840bd18c34c7b3f0726d79fca1b8e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 383 bytes

~~~c

long FUN_00aed3dc(long param_1,long param_2)

{
                    /* try { // try from 00aed3e8 to 00bed3f3 has its CatchHandler @ 00aed5a4 */
  param_1 = param_1 + 8;
  if (*(char **)(param_2 + 8) != "ZN13MyApplication9pasteSlotEvE3$_0") {
    param_1 = 0;
  }
                    /* try { // try from 00aed3f4 to 00bed58b has its CatchHandler @ 00aed16c */
  return param_1;
}

~~~
