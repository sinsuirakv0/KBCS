# 00bbfdf8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00bbfdf8.md)

## 関数情報

~~~json
{
  "address": "00bbfdf8",
  "name": "FUN_00bbfdf8",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "18133ecfa9ecf78487356c25d8054d1c1113ba80452cd2b036d7bbc8d295e988",
  "source_text_sha256": "18133ecfa9ecf78487356c25d8054d1c1113ba80452cd2b036d7bbc8d295e988"
}
~~~
## 呼び出し元

- [00bbde5c](../00bbd/00bbde5c.md)
- [00bc2f0c](../00bc2/00bc2f0c.md)

## 呼び出し先

- [00bdb0f0](../00bdb/00bdb0f0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 疑似コード 1/1 / UTF-8 1415 bytes

~~~c

void FUN_00bbfdf8(undefined8 *param_1,undefined8 *param_2)

{
  void *__dest;
  undefined8 uVar1;
  size_t __n;
  undefined8 *__src;
  undefined8 *puVar2;
  
                    /* try { // try from 00bbfe08 to 00cbfe0f has its CatchHandler @ 00bc892c */
  puVar2 = (undefined8 *)param_1[1];
                    /* try { // try from 00bbfe14 to 00cbfe23 has its CatchHandler @ 00bc88ec */
  if (puVar2 == (undefined8 *)param_1[2]) {
    __src = (undefined8 *)*param_1;
    __n = (long)puVar2 - (long)__src;
                    /* try { // try from 00bbfe38 to 00cbfe6f has its CatchHandler @ 00bc8b2c */
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
                    /* try { // try from 00bbfec0 to 00cbfed3 has its CatchHandler @ 00bc87e4 */
  return;
}

~~~
