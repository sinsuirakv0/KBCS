# 00adffcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00adffcc.md)

## 関数情報

~~~json
{
  "address": "00adffcc",
  "name": "firebase::analytics::internal::FutureData::Create",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3d347c7f55fe569e01d9709f2f2474b2b9bbefae870244bba24fd9a64ef25b3",
  "source_text_sha256": "d3d347c7f55fe569e01d9709f2f2474b2b9bbefae870244bba24fd9a64ef25b3"
}
~~~
## 呼び出し元

- [00bddd60](../00bdd/00bddd60.md)

## 呼び出し先

- [00bdaf40](../00bda/00bdaf40.md)
- [00bddce0](../00bdd/00bddce0.md)

## 疑似コード 1/1 / UTF-8 385 bytes

~~~c

/* firebase::analytics::internal::FutureData::Create() */

ReferenceCountedFutureImpl * firebase::analytics::internal::FutureData::Create(void)

{
  ReferenceCountedFutureImpl *this;
  
  this = operator_new(0x130);
  ReferenceCountedFutureImpl::ReferenceCountedFutureImpl(this,2);
  *(ReferenceCountedFutureImpl **)PTR_s_future_data__00c1b7a0 = this;
  return this;
}

~~~
