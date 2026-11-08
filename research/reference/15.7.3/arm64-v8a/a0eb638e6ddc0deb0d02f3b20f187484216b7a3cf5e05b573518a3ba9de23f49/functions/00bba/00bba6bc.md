# 00bba6bc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bba6bc",
  "name": "__cxa_guard_acquire",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3f305b0ed2b1ee80b214a9efca506681cf6c727a281c9d09a2fd5b2015883e43",
  "source_text_sha256": "3f305b0ed2b1ee80b214a9efca506681cf6c727a281c9d09a2fd5b2015883e43"
}
~~~

## 呼び出し元

- [00bdafb0](../00bda/00bdafb0.md)

## 呼び出し先

- [00bbb158](../00bbb/00bbb158.md)
- [00bde7d0](../00bde/00bde7d0.md)
- [00bde7e0](../00bde/00bde7e0.md)
- [00be1180](../00be1/00be1180.md)
- [00be1da0](../00be1/00be1da0.md)

## 関連文字列（未確認候補）

~~~text
"%s failed to acquire mutex"
"%s failed to release mutex"
"__cxa_guard_acquire"
"__cxa_guard_acquire detected recursive initialization: do you have a function-local static variable whose initialization depends on that function?"
~~~

## 疑似コード / UTF-8 2774 bytes

~~~c

bool __cxa_guard_acquire(char *param_1)

{
  byte bVar1;
  byte bVar2;
  bool bVar3;
  int iVar4;
  long lVar5;
  int unaff_w20;
  
                    /* catch() { ... } // from try @ 00bb6a7c with catch @ 00bba6c4 */
                    /* catch() { ... } // from try @ 00bb6a70 with catch @ 00bba6d8 */
                    /* catch() { ... } // from try @ 00bb66d8 with catch @ 00bba6dc */
  if (*param_1 == '\0') {
                    /* catch() { ... } // from try @ 00bb66c8 with catch @ 00bba6f4 */
    iVar4 = pthread_mutex_lock((pthread_mutex_t *)&DAT_010a36c0);
    if (iVar4 != 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00bbb158("%s failed to acquire mutex","__cxa_guard_acquire");
    }
    bVar1 = param_1[1];
    if ((bVar1 >> 1 & 1) != 0) {
      iVar4 = *(int *)(param_1 + 4);
                    /* catch() { ... } // from try @ 00bb66bc with catch @ 00bba714 */
                    /* catch() { ... } // from try @ 00bb6324 with catch @ 00bba718 */
      lVar5 = syscall(0xb2);
      unaff_w20 = (int)lVar5;
      if (iVar4 == unaff_w20) {
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00bb5b94 with catch @ 00bba7e0 */
        FUN_00bbb158(
                    "__cxa_guard_acquire detected recursive initialization: do you have a function-local static variable whose initialization depends on that function?"
                    );
      }
    }
    while (bVar2 = param_1[1], (bVar2 >> 1 & 1) != 0) {
                    /* catch() { ... } // from try @ 00bb6314 with catch @ 00bba744 */
      param_1[1] = bVar2 | 4;
      pthread_cond_wait((pthread_cond_t *)&DAT_010a36e8,(pthread_mutex_t *)&DAT_010a36c0);
    }
                    /* catch() { ... } // from try @ 00bb6308 with catch @ 00bba758 */
                    /* catch() { ... } // from try @ 00bb5f70 with catch @ 00bba75c */
    if (bVar2 != 1) {
      if ((bVar1 >> 1 & 1) == 0) {
        lVar5 = syscall(0xb2);
        unaff_w20 = (int)lVar5;
      }
      *(int *)(param_1 + 4) = unaff_w20;
      param_1[1] = '\x02';
    }
    iVar4 = pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a36c0);
                    /* catch() { ... } // from try @ 00bb5f60 with catch @ 00bba788 */
    if (iVar4 != 0) {
                    /* catch() { ... } // from try @ 00bb5ba0 with catch @ 00bba7cc */
                    /* WARNING: Subroutine does not return */
      FUN_00bbb158("%s failed to release mutex","__cxa_guard_acquire");
    }
    bVar3 = bVar2 != 1;
  }
  else {
    bVar3 = false;
  }
                    /* catch() { ... } // from try @ 00bb5f54 with catch @ 00bba79c */
                    /* catch() { ... } // from try @ 00bb5bb0 with catch @ 00bba7a0 */
  return bVar3;
}

~~~
