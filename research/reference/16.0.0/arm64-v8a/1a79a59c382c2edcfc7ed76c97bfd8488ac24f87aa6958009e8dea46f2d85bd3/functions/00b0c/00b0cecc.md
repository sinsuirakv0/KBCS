# 00b0cecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0171.md#review-523c6e96c348b3d39b7af58deaec8be5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0cecc",
  "name": "FUN_00b0cecc",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "256583e0ab5f7d7f2cb539fca4fe436018423e7245de8effc70dba737a675b76",
  "source_text_sha256": "256583e0ab5f7d7f2cb539fca4fe436018423e7245de8effc70dba737a675b76"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008514b8](../00851/008514b8.md)
- [008b6a18](../008b6/008b6a18.md)
- [008b7984](../008b7/008b7984.md)

## 疑似コード / UTF-8 272 bytes

~~~c

void FUN_00b0cecc(void)

{
  long lVar1;
  undefined8 uVar2;
  
  lVar1 = FUN_008514b8();
  uVar2 = FUN_008b7984(lVar1 + 0x2f38,0x329);
  FUN_008b6a18(uVar2,0);
  lVar1 = FUN_008514b8();
  uVar2 = FUN_008b7984(lVar1 + 0x2f38,0x32a);
  FUN_008b6a18(uVar2,0);
  return;
}

~~~
