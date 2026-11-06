# 00bba8ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bba8ec.md)

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
## 疑似コード 1/1 / UTF-8 1558 bytes

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
