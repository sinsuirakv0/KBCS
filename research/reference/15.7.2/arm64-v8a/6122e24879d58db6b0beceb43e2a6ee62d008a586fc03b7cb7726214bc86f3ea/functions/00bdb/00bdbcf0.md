# 00bdbcf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbcf0.md)

## 関数情報

~~~json
{
  "address": "00bdbcf0",
  "name": "Botan::BigInt::operator-=",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8cbe36df062b77c7cb4ae266bbc942339aac200ec4f899114ba24b09fc518d76",
  "source_text_sha256": "8cbe36df062b77c7cb4ae266bbc942339aac200ec4f899114ba24b09fc518d76"
}
~~~
## 呼び出し元

- [00493850](../00493/00493850.md)
- [004989ec](../00498/004989ec.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8aa0](../004b8/004b8aa0.md)
- [004b8bd8](../004b8/004b8bd8.md)
- [004b8e58](../004b8/004b8e58.md)
- [004ba430](../004ba/004ba430.md)
- [004bcf24](../004bc/004bcf24.md)
- [004be0f4](../004be/004be0f4.md)

## 呼び出し先

- [00495e3c](../00495/00495e3c.md)

## 疑似コード 1/1 / UTF-8 235 bytes

~~~c

void __thiscall Botan::BigInt::operator-=(BigInt *this,BigInt *param_1)

{
                    /* try { // try from 00bdbcf8 to 00cdbf53 has its CatchHandler @ 00bdbb1c */
  (*(code *)PTR_operator___00c1c6b0)();
  return;
}

~~~
