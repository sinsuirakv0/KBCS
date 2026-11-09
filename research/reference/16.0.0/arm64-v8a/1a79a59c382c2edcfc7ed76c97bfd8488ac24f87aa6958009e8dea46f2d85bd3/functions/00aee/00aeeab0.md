# 00aeeab0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aeeab0",
  "name": "FUN_00aeeab0",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "538cf5337134cfd5903c664793a25b88caa27e836ee19e65de170f3cd5101ebe",
  "source_text_sha256": "538cf5337134cfd5903c664793a25b88caa27e836ee19e65de170f3cd5101ebe"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 512 bytes

~~~c

void FUN_00aeeab0(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
                    /* try { // try from 00aeeab8 to 00beeabb has its CatchHandler @ 00aeead4 */
  *param_2 = &PTR_FUN_00c8daf8;
                    /* catch() { ... } // from try @ 00aee914 with catch @ 00aeeabc
                       try { // try from 00aeeabc to 00beeb13 has its CatchHandler @ 00aee7d4 */
  uVar1 = *(undefined8 *)(param_1 + 8);
  param_2[2] = *(undefined8 *)(param_1 + 0x10);
  param_2[1] = uVar1;
  return;
}

~~~
