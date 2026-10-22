# 00bdccc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdccc0.md)

## 関数情報

~~~json
{
  "address": "00bdccc0",
  "name": "Botan::X509_Certificate::load_subject_public_key",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9642562eb9149c97da14ebccaf860c01782b6754f39c4f2816ac5852dd23ac9d",
  "source_text_sha256": "9642562eb9149c97da14ebccaf860c01782b6754f39c4f2816ac5852dd23ac9d"
}
~~~
## 呼び出し元

- [004e85ec](../004e8/004e85ec.md)
- [00501b08](../00501/00501b08.md)
- [00503af8](../00503/00503af8.md)
- [005054cc](../00505/005054cc.md)

## 呼び出し先

- [00500f10](../00500/00500f10.md)

## 疑似コード 1/1 / UTF-8 236 bytes

~~~c

void Botan::X509_Certificate::load_subject_public_key(void)

{
                    /* try { // try from 00bdccc0 to 00cdcdc7 has its CatchHandler @ 00bdcbcc */
  (*(code *)PTR_load_subject_public_key_00c1ce98)();
  return;
}

~~~
