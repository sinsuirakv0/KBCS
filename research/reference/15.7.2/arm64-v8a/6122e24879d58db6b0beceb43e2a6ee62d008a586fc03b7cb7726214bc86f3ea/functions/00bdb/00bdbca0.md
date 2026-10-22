# 00bdbca0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbca0.md)

## 関数情報

~~~json
{
  "address": "00bdbca0",
  "name": "Botan::base64_decode",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5472ef8bd4eab8b775be32860c86af01b10f21728b6ad2d31efdf94d717ec0d2",
  "source_text_sha256": "5472ef8bd4eab8b775be32860c86af01b10f21728b6ad2d31efdf94d717ec0d2"
}
~~~
## 呼び出し元

- [00493268](../00493/00493268.md)
- [00493288](../00493/00493288.md)
- [00493354](../00493/00493354.md)
- [004c2f88](../004c2/004c2f88.md)

## 呼び出し先

- [00493150](../00493/00493150.md)

## 疑似コード 1/1 / UTF-8 151 bytes

~~~c

void Botan::base64_decode(uchar *param_1,char *param_2,ulong param_3,bool param_4)

{
  (*(code *)PTR_base64_decode_00c1c688)();
  return;
}

~~~
