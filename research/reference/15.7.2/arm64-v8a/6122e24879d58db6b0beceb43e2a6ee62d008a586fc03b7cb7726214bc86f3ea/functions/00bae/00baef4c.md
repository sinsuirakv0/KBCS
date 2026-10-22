# 00baef4c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baef4c.md)

## 関数情報

~~~json
{
  "address": "00baef4c",
  "name": "std::__ndk1::numpunct<char>::~numpunct",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c3b1de10e692dd7b362c2d2aaeed852bc151fb96df7d10553989d218379f01e3",
  "source_text_sha256": "c3b1de10e692dd7b362c2d2aaeed852bc151fb96df7d10553989d218379f01e3"
}
~~~
## 呼び出し元

- [00be1b30](../00be1/00be1b30.md)
- [00be1b40](../00be1/00be1b40.md)
- [00be1b90](../00be1/00be1b90.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb3b0](../00bdb/00bdb3b0.md)

## 疑似コード 1/1 / UTF-8 369 bytes

~~~c

/* std::__ndk1::numpunct<char>::~numpunct() */

void __thiscall std::__ndk1::numpunct<char>::~numpunct(numpunct<char> *this)

{
  *(undefined **)this = PTR_vtable_00c1beb8 + 0x10;
  if (((byte)this[0x18] & 1) != 0) {
    operator_delete(*(void **)(this + 0x28));
  }
  __shared_weak_count::~__shared_weak_count((__shared_weak_count *)this);
  return;
}

~~~
