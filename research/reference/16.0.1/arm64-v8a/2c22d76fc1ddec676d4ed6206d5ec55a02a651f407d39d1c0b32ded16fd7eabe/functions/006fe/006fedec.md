# 006fedec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/review-0060.md#review-0aebd8082be51e3b2dde07d58e7cba65)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/review-0021.md#review-0aebd8082be51e3b2dde07d58e7cba65)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fedec",
  "name": "FUN_006fedec",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f8a847fc7bb5a80d23b9f78a61765e8d8af95e14c7cf5f584a174ecf402af3d4",
  "source_text_sha256": "f8a847fc7bb5a80d23b9f78a61765e8d8af95e14c7cf5f584a174ecf402af3d4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 204 bytes

~~~c

void FUN_006fedec(undefined8 param_1,undefined8 *param_2)

{
  *param_2 = &PTR_FUN_00c77118;
                    /* try { // try from 006fedf8 to 007fedff has its CatchHandler @ 00704900 */
  return;
}

~~~
