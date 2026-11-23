# 00ba7ebc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ba7e78`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba7/00ba7e78.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0077.md#compare-c102ea3805a79702a9fa526fe298761f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba7ebc",
  "name": "_ZNSt6__ndk16localeC1Ev",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "75a869019b350a52e6a44e00c6e08cf1576434dde76ac88eee9e1b1d40ebc570",
  "source_text_sha256": "75a869019b350a52e6a44e00c6e08cf1576434dde76ac88eee9e1b1d40ebc570"
}
~~~

## 呼び出し元

- [00bdd950](../00bdd/00bdd950.md)

## 呼び出し先

- [00bd6e60](../00bd6/00bd6e60.md)
- [00bdb000](../00bdb/00bdb000.md)
- [00bdb020](../00bdb/00bdb020.md)
- [00bdd980](../00bdd/00bdd980.md)
- [00be18d0](../00be1/00be18d0.md)

## 疑似コード / UTF-8 617 bytes

~~~c

void _ZNSt6__ndk16localeC1Ev(undefined8 *param_1)

{
  undefined *puVar1;
  bool bVar2;
  int iVar3;
  undefined8 uVar4;
  
  if (((DAT_010a2af0 & 1) == 0) && (iVar3 = __cxa_guard_acquire(&DAT_010a2af0), iVar3 != 0)) {
    uVar4 = _ZNSt6__ndk16locale7classicEv();
    _ZNSt6__ndk16localeC1ERKS0_(&DAT_010a2ae8,uVar4);
    __cxa_guard_release(&DAT_010a2af0);
  }
  puVar1 = DAT_010a2ae8;
  bVar2 = DAT_010a2ae8 != &DAT_010a29a0;
                    /* try { // try from 00ba7ef4 to 00ca7eff has its CatchHandler @ 00ba8d5c */
  *param_1 = DAT_010a2ae8;
  if (bVar2) {
    FUN_00bd6e60(1,puVar1 + 8);
  }
  return;
}

~~~
