# 00bd2aac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bd29a0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bd2/00bd29a0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bd2aac",
  "name": "FUN_00bd2aac",
  "size": 132,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "705bb0285fc4a5f3b8edddbef23a514b224b604afb59771c6b4c8c9d189609cb",
  "source_text_sha256": "705bb0285fc4a5f3b8edddbef23a514b224b604afb59771c6b4c8c9d189609cb"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 疑似コード / UTF-8 1404 bytes

~~~c

void FUN_00bd2aac(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *__ptr;
  long lVar2;
  size_t __size;
  
  (**(code **)(**(long **)(param_1 + 0x10) + 0x20))();
  lVar2 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 1U) {
                    /* catch() { ... } // from try @ 00bd2090 with catch @ 00bd2ae4 */
    __size = param_2[2] * 2;
                    /* catch() { ... } // from try @ 00bd1de8 with catch @ 00bd2ae8 */
    uVar1 = lVar2 + 0x3e1;
                    /* catch() { ... } // from try @ 00bd232c with catch @ 00bd2aec */
                    /* catch() { ... } // from try @ 00bd2300 with catch @ 00bd2af0
                       catch() { ... } // from try @ 00bd2850 with catch @ 00bd2af0 */
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
                    /* catch() { ... } // from try @ 00bd2180 with catch @ 00bd2af8 */
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
  }
  *(undefined1 *)((long)__ptr + lVar2) = 0x20;
                    /* catch() { ... } // from try @ 00bd2138 with catch @ 00bd2b10
                       catch() { ... } // from try @ 00bd2834 with catch @ 00bd2b10 */
  param_2[1] = param_2[1] + 1;
  return;
}

~~~
