# 00baefc8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00baefc8.md)

## 関数情報

~~~json
{
  "address": "00baefc8",
  "name": "std::__ndk1::numpunct<wchar_t>::~numpunct",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e8b151bcf4f32c6ea164f8b33587c78eeff888f261b2a4b280dcc58aaea578a9",
  "source_text_sha256": "e8b151bcf4f32c6ea164f8b33587c78eeff888f261b2a4b280dcc58aaea578a9"
}
~~~
## 呼び出し元

- [00be1b50](../00be1/00be1b50.md)
- [00be1b60](../00be1/00be1b60.md)
- [00be1bb0](../00be1/00be1bb0.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdb3b0](../00bdb/00bdb3b0.md)

## 疑似コード 1/1 / UTF-8 378 bytes

~~~c

/* std::__ndk1::numpunct<wchar_t>::~numpunct() */

void __thiscall std::__ndk1::numpunct<wchar_t>::~numpunct(numpunct<wchar_t> *this)

{
  *(undefined **)this = PTR_vtable_00c1bec0 + 0x10;
  if (((byte)this[0x18] & 1) != 0) {
    operator_delete(*(void **)(this + 0x28));
  }
  __shared_weak_count::~__shared_weak_count((__shared_weak_count *)this);
  return;
}

~~~
