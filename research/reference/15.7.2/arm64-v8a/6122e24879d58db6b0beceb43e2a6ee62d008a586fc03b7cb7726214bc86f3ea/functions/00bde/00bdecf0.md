# 00bdecf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdecf0.md)

## 関数情報

~~~json
{
  "address": "00bdecf0",
  "name": "firebase::ReferenceCountedFutureImpl::LastResultProxy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d956de2b385983bc5a5c6b14b6356869a9fa2bf072de0a9a778595c87a9eea6a",
  "source_text_sha256": "d956de2b385983bc5a5c6b14b6356869a9fa2bf072de0a9a778595c87a9eea6a"
}
~~~
## 呼び出し元

- [00b72564](../00b72/00b72564.md)

## 呼び出し先

- [00b00570](../00b00/00b00570.md)

## 疑似コード 1/1 / UTF-8 149 bytes

~~~c

void firebase::ReferenceCountedFutureImpl::LastResultProxy(int param_1)

{
  (*(code *)PTR_LastResultProxy_00c1deb0)(param_1);
  return;
}

~~~
