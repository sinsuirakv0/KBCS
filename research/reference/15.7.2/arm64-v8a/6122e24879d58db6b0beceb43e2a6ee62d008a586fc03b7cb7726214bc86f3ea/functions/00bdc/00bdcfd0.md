# 00bdcfd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcfd0.md)

## 関数情報

~~~json
{
  "address": "00bdcfd0",
  "name": "Botan::PKIX::merge_revocation_status",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2dac28af49cb3cd1764a679101de0f1f8324dd55c13570403835a06d02923b40",
  "source_text_sha256": "2dac28af49cb3cd1764a679101de0f1f8324dd55c13570403835a06d02923b40"
}
~~~
## 呼び出し元

- [00508860](../00508/00508860.md)

## 呼び出し先

- [00508250](../00508/00508250.md)

## 疑似コード 1/1 / UTF-8 212 bytes

~~~c

void Botan::PKIX::merge_revocation_status
               (vector *param_1,vector *param_2,vector *param_3,bool param_4,bool param_5)

{
  (*(code *)PTR_merge_revocation_status_00c1d020)();
  return;
}

~~~
