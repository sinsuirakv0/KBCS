# 00baee6c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baee6c.md)

## 関数情報

~~~json
{
  "address": "00baee6c",
  "name": "std::__ndk1::__narrow_to_utf8<32ul>::~__narrow_to_utf8",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ce453c86e9c83dd21067b02b326f8f0704855475ecfd17731006b9b7898e3469",
  "source_text_sha256": "ce453c86e9c83dd21067b02b326f8f0704855475ecfd17731006b9b7898e3469"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1b00](../00be1/00be1b00.md)

## 疑似コード 1/1 / UTF-8 245 bytes

~~~c

/* std::__ndk1::__narrow_to_utf8<32ul>::~__narrow_to_utf8() */

void __thiscall std::__ndk1::__narrow_to_utf8<32ul>::~__narrow_to_utf8(__narrow_to_utf8<32ul> *this)

{
  ~__narrow_to_utf8(this);
  operator_delete(this);
  return;
}

~~~
