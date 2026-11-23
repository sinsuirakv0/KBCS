# 00bba8ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bba8a8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bba8a8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0078.md#compare-8c68c0bdfaca03d78c29ea18673b32e6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bba8ec",
  "name": "__cxa_guard_abort",
  "size": 152,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "544ae8e0fab000b7dda7d4ac760ffbb2625bf40ab7a31884540f1271ca9e2787",
  "source_text_sha256": "544ae8e0fab000b7dda7d4ac760ffbb2625bf40ab7a31884540f1271ca9e2787"
}
~~~

## 呼び出し元

- [00bdb140](../00bdb/00bdb140.md)

## 呼び出し先

- [00bbb19c](../00bbb/00bbb19c.md)
- [00bde820](../00bde/00bde820.md)
- [00bde830](../00bde/00bde830.md)
- [00be11c0](../00be1/00be11c0.md)

## 関連文字列（未確認候補）

~~~text
"%s failed to acquire mutex"
"%s failed to broadcast"
"%s failed to release mutex"
"__cxa_guard_abort"
~~~

## 疑似コード / UTF-8 1558 bytes

~~~c

void __cxa_guard_abort(long param_1)

{
  byte bVar1;
  int iVar2;
  char *pcVar3;
  
                    /* catch() { ... } // from try @ 00bb50a0 with catch @ 00bba8f0 */
                    /* catch() { ... } // from try @ 00bb4cdc with catch @ 00bba8f4 */
  iVar2 = pthread_mutex_lock((pthread_mutex_t *)&DAT_010a3700);
  if (iVar2 == 0) {
    bVar1 = *(byte *)(param_1 + 1);
    *(undefined4 *)(param_1 + 4) = 0;
    *(undefined1 *)(param_1 + 1) = 0;
                    /* catch() { ... } // from try @ 00bb4ccc with catch @ 00bba920 */
    iVar2 = pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a3700);
    if (iVar2 != 0) {
                    /* catch() { ... } // from try @ 00bb48ec with catch @ 00bba964 */
                    /* WARNING: Subroutine does not return */
      FUN_00bbb19c("%s failed to release mutex","__cxa_guard_abort");
    }
                    /* catch() { ... } // from try @ 00bb4cc0 with catch @ 00bba934 */
                    /* catch() { ... } // from try @ 00bb48fc with catch @ 00bba938 */
    if (((bVar1 >> 2 & 1) == 0) ||
       (iVar2 = pthread_cond_broadcast((pthread_cond_t *)&DAT_010a3728), iVar2 == 0)) {
      return;
    }
    pcVar3 = "%s failed to broadcast";
  }
  else {
    pcVar3 = "%s failed to acquire mutex";
  }
                    /* catch() { ... } // from try @ 00bb48e0 with catch @ 00bba978 */
                    /* catch() { ... } // from try @ 00bb453c with catch @ 00bba97c */
                    /* WARNING: Subroutine does not return */
  FUN_00bbb19c(pcVar3,"__cxa_guard_abort");
}

~~~
