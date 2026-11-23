# 00bbcb0c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbcac8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbc/00bbcac8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0018.md#compare-914d337d18c1732d2adc52b0fbf7f268)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcb0c",
  "name": "FUN_00bbcb0c",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be3b2d48250300ecacc2a2302f2378420278221aa6d4b3315adc5775d04d9b76",
  "source_text_sha256": "be3b2d48250300ecacc2a2302f2378420278221aa6d4b3315adc5775d04d9b76"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde9d0](../00bde/00bde9d0.md)

## 疑似コード / UTF-8 1713 bytes

~~~c

void FUN_00bbcb0c(long param_1,long param_2,long param_3,long param_4,int param_5,uint param_6)

{
  int iVar1;
  long lVar2;
  
  lVar2 = *(long *)(param_2 + 0x10);
  if ((param_6 & 1) == 0) {
    if (*(long *)(param_1 + 8) != *(long *)(lVar2 + 8)) {
      return;
    }
  }
  else {
                    /* try { // try from 00bbcb64 to 00cbcb67 has its CatchHandler @ 00bbd304 */
                    /* try { // try from 00bbcb68 to 00cbcbaf has its CatchHandler @ 00bbb930 */
    if ((lVar2 != param_1) &&
       (iVar1 = strcmp(*(char **)(param_1 + 8),*(char **)(lVar2 + 8)), iVar1 != 0)) {
      return;
    }
  }
  *(undefined1 *)(param_2 + 0x4d) = 1;
  if (*(long *)(param_2 + 8) == param_4) {
    *(undefined1 *)(param_2 + 0x4c) = 1;
    if (*(long *)(param_2 + 0x20) == 0) {
      *(long *)(param_2 + 0x20) = param_3;
      *(int *)(param_2 + 0x30) = param_5;
      *(undefined4 *)(param_2 + 0x3c) = 1;
      iVar1 = param_5;
    }
    else {
                    /* try { // try from 00bbcbb0 to 00cbcbb7 has its CatchHandler @ 00bbd32c */
      if (*(long *)(param_2 + 0x20) != param_3) {
                    /* try { // try from 00bbcbb8 to 00cbcbbf has its CatchHandler @ 00bbd114 */
        *(int *)(param_2 + 0x3c) = *(int *)(param_2 + 0x3c) + 1;
        goto LAB_00bbcc04;
      }
      iVar1 = *(int *)(param_2 + 0x30);
      if (*(int *)(param_2 + 0x30) == 2) {
                    /* try { // try from 00bbcbec to 00cbcbff has its CatchHandler @ 00bbd110 */
        *(int *)(param_2 + 0x30) = param_5;
        iVar1 = param_5;
      }
    }
    if ((iVar1 == 1) && (*(int *)(param_2 + 0x48) == 1)) {
LAB_00bbcc04:
      *(undefined1 *)(param_2 + 0x4e) = 1;
      return;
    }
  }
  return;
}

~~~
