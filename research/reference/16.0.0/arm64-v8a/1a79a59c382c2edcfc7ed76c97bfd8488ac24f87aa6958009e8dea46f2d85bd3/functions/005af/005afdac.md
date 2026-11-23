# 005afdac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0107.md#review-3bf4fefacfde7341708a327e98bc0317)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005afdac",
  "name": "FUN_005afdac",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b626c87be87a169afa6794e450f8b168ca8106dd384550259414c3273e488ed9",
  "source_text_sha256": "b626c87be87a169afa6794e450f8b168ca8106dd384550259414c3273e488ed9"
}
~~~

## 呼び出し元

- [00a47d08](../00a47/00a47d08.md)

## 呼び出し先

- [005afc38](../005af/005afc38.md)

## 疑似コード / UTF-8 190 bytes

~~~c

int FUN_005afdac(void)

{
  int iVar1;
  
  iVar1 = FUN_005afc38(2);
                    /* try { // try from 005afdc0 to 006afdcf has its CatchHandler @ 005b028c */
  return iVar1 + 3;
}

~~~
