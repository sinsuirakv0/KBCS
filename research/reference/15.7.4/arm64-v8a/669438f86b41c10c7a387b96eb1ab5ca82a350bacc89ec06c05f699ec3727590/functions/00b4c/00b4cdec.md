# 00b4cdec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b4cda8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b4c/00b4cda8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0068.md#compare-9001914785fb4b8f110ad0b928c59d8f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b4cdec",
  "name": "FUN_00b4cdec",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9b8cf8c57a9744ec295cd175bd91cb7630a2a9f9811284cd6ddf4a511a70832b",
  "source_text_sha256": "9b8cf8c57a9744ec295cd175bd91cb7630a2a9f9811284cd6ddf4a511a70832b"
}
~~~

## 呼び出し元

- [00b4c4c4](../00b4c/00b4c4c4.md)
- [00b4cc40](../00b4c/00b4cc40.md)

## 呼び出し先

- [00848b34](../00848/00848b34.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)
- [00bdde40](../00bdd/00bdde40.md)
- [00bde180](../00bde/00bde180.md)
- [00be05e0](../00be0/00be05e0.md)

## 関連文字列（未確認候補）

~~~text
"Messaging not initialized."
"internal::IsInitialized()"
~~~

## 疑似コード / UTF-8 1237 bytes

~~~c

void FUN_00b4cdec(void)

{
  long lVar1;
  undefined1 auStack_80 [24];
  undefined1 auStack_68 [40];
  long *local_40;
  undefined1 auStack_38 [16];
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  if (DAT_010a10a0 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
  }
  else {
                    /* try { // try from 00b4ce14 to 00c4ce1f has its CatchHandler @ 00b4d9dc */
    _ZN8firebase9messaging8GetTokenEv(auStack_68);
    _ZN8firebase5Mutex7AcquireEv(auStack_68);
    if (local_40 != (long *)0x0) {
                    /* try { // try from 00b4ce38 to 00c4ce43 has its CatchHandler @ 00b4d9cc */
      (**(code **)(*local_40 + 0x40))(auStack_80,local_40,auStack_38,FUN_00b4ea90,0,0,1);
    }
    _ZN8firebase5Mutex7ReleaseEv(auStack_68);
                    /* try { // try from 00b4ce64 to 00c4ce6f has its CatchHandler @ 00b4d980 */
    FUN_00848b34(auStack_68);
  }
                    /* try { // try from 00b4ce88 to 00c4ce93 has its CatchHandler @ 00b4d97c */
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
