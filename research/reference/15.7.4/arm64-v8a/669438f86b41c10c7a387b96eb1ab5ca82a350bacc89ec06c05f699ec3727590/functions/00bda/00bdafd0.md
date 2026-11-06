# 00bdafd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bdafd0",
  "name": "<EXTERNAL>::__cxa_finalize",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee454707ff51c2b811bc691a4bcda28d1b92bd4f7346af5204f67639ee4dd61f",
  "source_text_sha256": "ee454707ff51c2b811bc691a4bcda28d1b92bd4f7346af5204f67639ee4dd61f"
}
~~~

## 呼び出し元

- [004182d0](../00418/004182d0.md)

## 呼び出し先

- [010a5000](../010a5/010a5000.md)

## 疑似コード / UTF-8 87 bytes

~~~c

void __cxa_finalize(void)

{
  (*(code *)PTR___cxa_finalize_00c1c0a0)();
  return;
}

~~~
