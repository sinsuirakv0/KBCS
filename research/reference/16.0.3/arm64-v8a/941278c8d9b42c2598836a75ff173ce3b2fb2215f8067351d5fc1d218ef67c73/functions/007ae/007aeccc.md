# 007aeccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "007aeccc",
  "name": "FUN_007aeccc",
  "size": 116,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a1052e7d967bac5a9b3b2fedc3002c18be60dbc2df07198990f6e43275e37211",
  "source_text_sha256": "a1052e7d967bac5a9b3b2fedc3002c18be60dbc2df07198990f6e43275e37211"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)

## 疑似コード / UTF-8 767 bytes

~~~c

void FUN_007aeccc(undefined8 *param_1)

{
  undefined8 *__ptr;
  
                    /* try { // try from 007aeccc to 008aecd3 has its CatchHandler @ 007af430 */
  __ptr = (undefined8 *)*param_1;
  *param_1 = 0;
  if (__ptr != (undefined8 *)0x0) {
    if ((*(byte *)(__ptr + 7) & 1) != 0) {
      _ZdlPv((void *)__ptr[9]);
    }
    *__ptr = &PTR_FUN_00c6eac0;
    if ((*(byte *)(__ptr + 4) & 1) != 0) {
      _ZdlPv((void *)__ptr[6]);
    }
                    /* try { // try from 007aed18 to 008aed2b has its CatchHandler @ 007af3d4 */
    if ((*(byte *)(__ptr + 1) & 1) != 0) {
      _ZdlPv((void *)__ptr[3]);
    }
                    /* try { // try from 007aed2c to 008aed3f has its CatchHandler @ 007af3b8 */
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~
