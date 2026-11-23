# 00badf9c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00badf58`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00badf58.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/detail_skipped-0023.md#compare-bf2fd6b6aa00be537feff3acaa3e980c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badf9c",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IDsLb0EE9do_lengthER9mbstate_tPKcS5_m",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aecec18433ac70b423049afa4ffad1f023d33637c2d34453d7897c45d2b6c528",
  "source_text_sha256": "aecec18433ac70b423049afa4ffad1f023d33637c2d34453d7897c45d2b6c528"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 842 bytes

~~~c

int _ZNKSt6__ndk115__codecvt_utf16IDsLb0EE9do_lengthER9mbstate_tPKcS5_m
              (long param_1,undefined8 param_2,byte *param_3,long param_4,ulong param_5)

{
  bool bVar1;
  bool bVar2;
  int iVar3;
  ulong uVar4;
  
  iVar3 = (int)param_3;
  if (((1 < param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x18) >> 2 & 1) != 0)) &&
     (*param_3 == 0xfe)) {
    param_3 = param_3 + (ulong)(param_3[1] == 0xff) * 2;
  }
  if ((param_5 != 0) && (param_3 < (byte *)(param_4 + -1))) {
    uVar4 = 1;
    do {
      if ((*param_3 & 0xf8) == 0xd8) break;
      bVar1 = (ulong)CONCAT11(*param_3,param_3[1]) <= *(ulong *)(param_1 + 0x10);
      param_3 = param_3 + (ulong)bVar1 * 2;
      bVar2 = uVar4 < param_5;
      uVar4 = uVar4 + 1;
    } while ((bVar1 && param_3 < (byte *)(param_4 + -1)) && bVar2);
  }
  return (int)param_3 - iVar3;
}

~~~
