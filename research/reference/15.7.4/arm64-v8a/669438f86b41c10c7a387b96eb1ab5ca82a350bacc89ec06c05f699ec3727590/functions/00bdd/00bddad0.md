# 00bddad0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bddad0",
  "name": "<EXTERNAL>::cosf",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ba9a34e10348d3e5e729add6dde9cf70dd03b0cbe96291dc2e360fb625ea0ec",
  "source_text_sha256": "0ba9a34e10348d3e5e729add6dde9cf70dd03b0cbe96291dc2e360fb625ea0ec"
}
~~~

## 呼び出し元

- [007acf88](../007ac/007acf88.md)

## 呼び出し先

- [010a5558](../010a5/010a5558.md)

## 疑似コード / UTF-8 190 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

float cosf(float __x)

{
  float fVar1;
  
  fVar1 = (float)(*(code *)PTR_cosf_00c1d620)();
  return fVar1;
}

~~~
