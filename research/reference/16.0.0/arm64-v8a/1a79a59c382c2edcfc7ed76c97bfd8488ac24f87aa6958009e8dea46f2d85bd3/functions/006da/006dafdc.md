# 006dafdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `006b1220`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/006b1/006b1220.md) · 移動量 `+0x29dbc`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/inspection-0014.md#compare-fb1e3c1cc3d05193270a42974583fd30)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006dafdc",
  "name": "FUN_006dafdc",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "01727eb86aa498afba91932f53d48032b909896b0ad395ae6d5328cbc0caf44a",
  "source_text_sha256": "01727eb86aa498afba91932f53d48032b909896b0ad395ae6d5328cbc0caf44a"
}
~~~

## 呼び出し元

- [00a2b0f0](../00a2b/00a2b0f0.md)

## 呼び出し先

- [00480af8](../00480/00480af8.md)
- [00480b50](../00480/00480b50.md)
- [00480d08](../00480/00480d08.md)
- [00481058](../00481/00481058.md)

## 疑似コード / UTF-8 255 bytes

~~~c

void FUN_006dafdc(undefined4 *param_1,undefined8 param_2)

{
  FUN_00480b50(param_2,*param_1);
  FUN_00481058(*(undefined8 *)(param_1 + 2),param_2);
  FUN_00480af8(param_2,param_1[4]);
  FUN_00480d08(param_2,*(undefined1 *)(param_1 + 0xe));
  return;
}

~~~
