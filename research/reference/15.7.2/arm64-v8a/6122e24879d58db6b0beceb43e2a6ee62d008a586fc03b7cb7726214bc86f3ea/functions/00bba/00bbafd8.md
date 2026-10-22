# 00bbafd8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbafd8.md)

## 関数情報

~~~json
{
  "address": "00bbafd8",
  "name": "std::bad_cast::bad_cast",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8fe54ffc1edad7b3a1bd9e93ab5b9b06bd8e55884fe0945cecca98b7df8a2aa5",
  "source_text_sha256": "8fe54ffc1edad7b3a1bd9e93ab5b9b06bd8e55884fe0945cecca98b7df8a2aa5"
}
~~~
## 呼び出し元

- [00be1380](../00be1/00be1380.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 168 bytes

~~~c

/* std::bad_cast::bad_cast() */

void __thiscall std::bad_cast::bad_cast(bad_cast *this)

{
  *(undefined **)this = PTR_vtable_00c1bf38 + 0x10;
  return;
}

~~~
