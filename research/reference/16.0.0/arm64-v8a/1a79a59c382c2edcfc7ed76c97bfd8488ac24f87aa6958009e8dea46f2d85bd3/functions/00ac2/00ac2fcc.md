# 00ac2fcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/review-0161.md#review-e9d67d5fc573362ca34220e3f5167ad4)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac2fcc",
  "name": "FUN_00ac2fcc",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "96fd3067ed80ab2c33226bb442bdfca2b8b6b367e4bec66491b56c721d7919b8",
  "source_text_sha256": "96fd3067ed80ab2c33226bb442bdfca2b8b6b367e4bec66491b56c721d7919b8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008b79cc](../008b7/008b79cc.md)
- [00abf2b4](../00abf/00abf2b4.md)

## 疑似コード / UTF-8 552 bytes

~~~c

void FUN_00ac2fcc(long param_1)

{
  long lVar1;
  
  lVar1 = *(long *)(param_1 + 8);
  FUN_00abf2b4(param_1,1);
  if ((*(byte *)(lVar1 + 0x1aec) & 1) != 0) {
                    /* try { // try from 00ac2ff8 to 00bc2ffb has its CatchHandler @ 00ac3114 */
                    /* try { // try from 00ac2ffc to 00bc30b3 has its CatchHandler @ 00ac2c48 */
    return;
  }
  *(undefined1 *)(lVar1 + 0x1aec) = 1;
  *(undefined4 *)((long)&QWORD_0039b1b4 + lVar1) = 2;
  *(undefined4 *)(lVar1 + 0x3478) = 0x22;
  FUN_008b79cc(lVar1 + 0x2f38,0);
  return;
}

~~~
