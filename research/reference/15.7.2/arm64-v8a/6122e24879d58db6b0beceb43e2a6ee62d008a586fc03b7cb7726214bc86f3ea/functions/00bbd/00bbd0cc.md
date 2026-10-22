# 00bbd0cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbd0cc.md)

## 関数情報

~~~json
{
  "address": "00bbd0cc",
  "name": "FUN_00bbd0cc",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4c8c181501334a4881446542c44ee70ece832c50d85b833f2b50ce4043dbc102",
  "source_text_sha256": "4c8c181501334a4881446542c44ee70ece832c50d85b833f2b50ce4043dbc102"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb710](../00bdb/00bdb710.md)

## 疑似コード 1/1 / UTF-8 2399 bytes

~~~c

void FUN_00bbd0cc(long param_1)

{
  undefined8 *puVar1;
  undefined8 *__ptr;
  undefined8 *puVar2;
  
                    /* catch() { ... } // from try @ 00bbbe9c with catch @ 00bbd0dc */
                    /* catch() { ... } // from try @ 00bbbe5c with catch @ 00bbd0e0 */
                    /* catch() { ... } // from try @ 00bbbde0 with catch @ 00bbd0e4 */
  puVar1 = (undefined8 *)(param_1 + 0x330);
  __ptr = *(undefined8 **)(param_1 + 0x1330);
  while (__ptr != (undefined8 *)0x0) {
    while( true ) {
      puVar2 = (undefined8 *)*__ptr;
      *(undefined8 **)(param_1 + 0x1330) = puVar2;
      if (__ptr != puVar1) break;
                    /* catch() { ... } // from try @ 00bbbc48 with catch @ 00bbd10c */
      __ptr = puVar2;
      if (puVar2 == (undefined8 *)0x0) goto LAB_00bbd114;
    }
    free(__ptr);
                    /* catch() { ... } // from try @ 00bbbc58 with catch @ 00bbd0f4 */
    __ptr = *(undefined8 **)(param_1 + 0x1330);
  }
LAB_00bbd114:
  *puVar1 = 0;
  *(undefined8 *)(param_1 + 0x338) = 0;
                    /* catch() { ... } // from try @ 00bbbc3c with catch @ 00bbd120 */
  *(undefined8 **)(param_1 + 0x1330) = puVar1;
                    /* catch() { ... } // from try @ 00bbbbf8 with catch @ 00bbd124 */
                    /* catch() { ... } // from try @ 00bbbaf8 with catch @ 00bbd128 */
  if (*(void **)(param_1 + 0x2d0) != (void *)(param_1 + 0x2e8)) {
    free(*(void **)(param_1 + 0x2d0));
  }
  if (*(void **)(param_1 + 0x298) != (void *)(param_1 + 0x2b0)) {
                    /* catch() { ... } // from try @ 00bbbae8 with catch @ 00bbd140 */
    free(*(void **)(param_1 + 0x298));
  }
  if (*(void **)(param_1 + 0x240) != (void *)(param_1 + 600)) {
                    /* catch() { ... } // from try @ 00bbbadc with catch @ 00bbd154 */
    free(*(void **)(param_1 + 0x240));
  }
                    /* catch() { ... } // from try @ 00bbba94 with catch @ 00bbd158 */
                    /* catch() { ... } // from try @ 00bbb8e4 with catch @ 00bbd15c */
  if (*(void **)(param_1 + 0x128) != (void *)(param_1 + 0x140)) {
    free(*(void **)(param_1 + 0x128));
  }
                    /* catch() { ... } // from try @ 00bbb8d4 with catch @ 00bbd174 */
  if (*(void **)(param_1 + 0x10) != (void *)(param_1 + 0x28)) {
    free(*(void **)(param_1 + 0x10));
    return;
  }
  return;
}

~~~
