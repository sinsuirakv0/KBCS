# 00badbfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00badbb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00badbb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/detail_skipped-0023.md#compare-c901337b986a0c4a65facd4cea7c7620)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badbfc",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "37837acb92e09c9e84a57dcd6c519b24eb27631f185b0fd061e2022485a11d23",
  "source_text_sha256": "37837acb92e09c9e84a57dcd6c519b24eb27631f185b0fd061e2022485a11d23"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 1783 bytes

~~~c

ulong _ZNKSt6__ndk115__codecvt_utf16IwLb1EE5do_inER9mbstate_tPKcS5_RS5_PwS7_RS7_
                (long param_1,undefined8 param_2,ushort *param_3,ushort *param_4,ulong *param_5,
                uint *param_6,uint *param_7,undefined8 *param_8)

{
  byte bVar1;
  ulong uVar2;
  uint *puVar3;
  ulong uVar4;
  uint uVar5;
  
  if (((1 < (long)param_4 - (long)param_3) && ((*(uint *)(param_1 + 0x20) >> 2 & 1) != 0)) &&
     ((char)*param_3 == -1)) {
    param_3 = param_3 + (*(char *)((long)param_3 + 1) == -2);
  }
  if (param_3 < (ushort *)((long)param_4 + -1)) {
    uVar4 = *(ulong *)(param_1 + 0x18);
    puVar3 = param_6;
    do {
      param_6 = puVar3;
      if (param_7 <= puVar3) break;
      uVar5 = (uint)*param_3;
      bVar1 = *(byte *)((long)param_3 + 1) & 0xfc;
      if (bVar1 == 0xd8) {
        if ((long)param_4 - (long)param_3 < 4) {
          uVar2 = 1;
          goto LAB_00badcdc;
        }
                    /* catch() { ... } // from try @ 00bade98 with catch @ 00badcbc */
        if (((*(byte *)((long)param_3 + 3) & 0xfc) != 0xdc) ||
           (uVar5 = ((uint)(byte)param_3[1] | (*(byte *)((long)param_3 + 3) & 3) << 8 |
                    (uVar5 & 0x3ff) << 10) + 0x10000, uVar4 < uVar5)) goto LAB_00badce8;
        uVar2 = 4;
      }
      else {
        if (bVar1 == 0xdc) {
LAB_00badce8:
          uVar2 = 2;
          goto LAB_00badcdc;
        }
        uVar2 = 2;
        if (uVar4 < uVar5) goto LAB_00badcdc;
      }
      param_3 = (ushort *)((long)param_3 + uVar2);
      param_6 = puVar3 + 1;
      *puVar3 = uVar5;
      puVar3 = param_6;
    } while (param_3 < (ushort *)((long)param_4 + -1));
  }
  uVar2 = (ulong)(param_3 < param_4);
  puVar3 = param_6;
LAB_00badcdc:
  *param_5 = (ulong)param_3;
  *param_8 = puVar3;
  return uVar2;
}

~~~
