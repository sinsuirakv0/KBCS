# 00bbfdb4

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbfdb4",
  "name": "FUN_00bbfdb4",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1be3bcd01121e394c6776b19d8287bfb175c62effe7a1f28d0ade1ab66f085e8",
  "source_text_sha256": "1be3bcd01121e394c6776b19d8287bfb175c62effe7a1f28d0ade1ab66f085e8"
}
~~~

## 呼び出し元

- [00bbde18](../00bbd/00bbde18.md)
- [00bc2ec8](../00bc2/00bc2ec8.md)

## 呼び出し先

- [00bdb0a0](../00bdb/00bdb0a0.md)
- [00bdd180](../00bdd/00bdd180.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

## 疑似コード / UTF-8 1415 bytes

~~~c

void FUN_00bbfdb4(undefined8 *param_1,undefined8 *param_2)

{
  void *__dest;
  undefined8 uVar1;
  size_t __n;
  undefined8 *__src;
  undefined8 *puVar2;
  
                    /* try { // try from 00bbfdc4 to 00cbfdcb has its CatchHandler @ 00bc88e8 */
  puVar2 = (undefined8 *)param_1[1];
                    /* try { // try from 00bbfdd0 to 00cbfddf has its CatchHandler @ 00bc88a8 */
  if (puVar2 == (undefined8 *)param_1[2]) {
    __src = (undefined8 *)*param_1;
    __n = (long)puVar2 - (long)__src;
                    /* try { // try from 00bbfdf4 to 00cbfe2b has its CatchHandler @ 00bc8ae8 */
    if (__src == param_1 + 3) {
      __dest = malloc(__n * 2);
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      if (puVar2 != __src) {
        memmove(__dest,__src,__n);
      }
      *param_1 = __dest;
    }
    else {
      __dest = realloc(__src,__n * 2);
      *param_1 = __dest;
      if (__dest == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
    }
    puVar2 = (undefined8 *)((long)__dest + __n);
    param_1[1] = puVar2;
    param_1[2] = (void *)((long)__dest + ((long)__n >> 2) * 8);
  }
  uVar1 = *param_2;
  param_1[1] = puVar2 + 1;
  *puVar2 = uVar1;
                    /* try { // try from 00bbfe7c to 00cbfe8f has its CatchHandler @ 00bc87a0 */
  return;
}

~~~
