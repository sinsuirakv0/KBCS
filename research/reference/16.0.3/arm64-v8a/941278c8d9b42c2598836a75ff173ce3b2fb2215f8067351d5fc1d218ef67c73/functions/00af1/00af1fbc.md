# 00af1fbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af1fbc",
  "name": "FUN_00af1fbc",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f0b5381d6ecbf1920abedd87bb2466d8ef552dba9ca4d78266ae8c6f4aca43d",
  "source_text_sha256": "6f0b5381d6ecbf1920abedd87bb2466d8ef552dba9ca4d78266ae8c6f4aca43d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 625 bytes

~~~c

void FUN_00af1fbc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
                    /* catch() { ... } // from try @ 00af1e20 with catch @ 00af1fbc
                       try { // try from 00af1fbc to 00bf2047 has its CatchHandler @ 00af1d34 */
  uVar1 = *(undefined8 *)(param_1 + 8);
                    /* catch() { ... } // from try @ 00af1de0 with catch @ 00af1fc4 */
  *param_2 = &PTR_FUN_00c8f818;
  param_2[1] = uVar1;
                    /* catch() { ... } // from try @ 00af1e44 with catch @ 00af1fcc
                       catch() { ... } // from try @ 00af1fb8 with catch @ 00af1fcc */
  return;
}

~~~
