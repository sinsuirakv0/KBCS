# 00baeec4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baeec4.md)

## 関数情報

~~~json
{
  "address": "00baeec4",
  "name": "std::__ndk1::__widen_from_utf8<32ul>::~__widen_from_utf8",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "03345e80761502006cbbc77c93113189359329325ac23b6c4887740bddef6918",
  "source_text_sha256": "03345e80761502006cbbc77c93113189359329325ac23b6c4887740bddef6918"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00be1b20](../00be1/00be1b20.md)

## 疑似コード 1/1 / UTF-8 301 bytes

~~~c

/* std::__ndk1::__widen_from_utf8<32ul>::~__widen_from_utf8() */

void __thiscall
std::__ndk1::__widen_from_utf8<32ul>::~__widen_from_utf8(__widen_from_utf8<32ul> *this)

{
  __narrow_to_utf8<32ul>::~__narrow_to_utf8((__narrow_to_utf8<32ul> *)this);
  operator_delete(this);
  return;
}

~~~
