# 00babab8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baba74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bab/00baba74.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0017.md#compare-c52527a8b393cabfcecc8e421183ffe2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babab8",
  "name": "_ZNKSt6__ndk17codecvtIwc9mbstate_tE10do_unshiftERS1_PcS4_RS4_",
  "size": 200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "38abbb1846e44cfddf0788602584ee7b5eb4b9c71323d15148a4041ef18792ed",
  "source_text_sha256": "38abbb1846e44cfddf0788602584ee7b5eb4b9c71323d15148a4041ef18792ed"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00be1580](../00be1/00be1580.md)
- [00be1b50](../00be1/00be1b50.md)

## 疑似コード / UTF-8 1336 bytes

~~~c

undefined8
_ZNKSt6__ndk17codecvtIwc9mbstate_tE10do_unshiftERS1_PcS4_RS4_
          (long param_1,mbstate_t *param_2,long param_3,long param_4,long *param_5)

{
  char cVar1;
  __locale_t __dataset;
  size_t sVar2;
  undefined8 uVar3;
  ulong uVar4;
  char *pcVar5;
  char *pcVar6;
  char acStack_3c [4];
  __locale_t local_38;
  
  *param_5 = param_3;
  __dataset = uselocale(*(__locale_t *)(param_1 + 0x10));
  local_38 = __dataset;
  sVar2 = wcrtomb(acStack_3c,L'\0',param_2);
  if (__dataset != (__locale_t)0x0) {
                    /* try { // try from 00babb0c to 00cabb23 has its CatchHandler @ 00babd78 */
    uselocale(__dataset);
  }
  if (sVar2 + 1 < 2) {
    uVar3 = 2;
  }
  else {
    uVar4 = sVar2 - 1;
    if ((ulong)(param_4 - *param_5) < uVar4) {
      uVar3 = 1;
    }
    else {
      if (uVar4 != 0) {
        pcVar5 = acStack_3c;
        do {
          pcVar6 = (char *)*param_5;
          cVar1 = *pcVar5;
                    /* try { // try from 00babb50 to 00cabb6f has its CatchHandler @ 00babd08 */
          uVar4 = uVar4 - 1;
          *param_5 = (long)(pcVar6 + 1);
          *pcVar6 = cVar1;
          pcVar5 = pcVar5 + 1;
        } while (uVar4 != 0);
      }
      uVar3 = 0;
    }
  }
                    /* try { // try from 00babb70 to 00cabc63 has its CatchHandler @ 00bab788 */
  return uVar3;
}

~~~
