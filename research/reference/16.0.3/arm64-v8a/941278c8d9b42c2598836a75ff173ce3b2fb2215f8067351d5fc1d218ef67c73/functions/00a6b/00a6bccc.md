# 00a6bccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00a6bccc",
  "name": "FUN_00a6bccc",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "841ef45efd7e22230c16931357d189e9bd87434d65fadd4ced56eeb65589a5a5",
  "source_text_sha256": "841ef45efd7e22230c16931357d189e9bd87434d65fadd4ced56eeb65589a5a5"
}
~~~

## 呼び出し元

- [00700f00](../00700/00700f00.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 320 bytes

~~~c

void FUN_00a6bccc(long param_1)

{
  if ((*(int *)(param_1 + 0x84) != 0) && (*(int *)(param_1 + 0x84) <= *(int *)(param_1 + 0x80))) {
                    /* try { // try from 00a6bcdc to 00b6bceb has its CatchHandler @ 00a78e60 */
    return;
  }
  *(int *)(param_1 + 0x80) = *(int *)(param_1 + 0x80) + 1;
  return;
}

~~~
