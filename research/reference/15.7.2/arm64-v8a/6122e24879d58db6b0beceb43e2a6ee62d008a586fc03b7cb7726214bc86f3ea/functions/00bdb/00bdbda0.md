# 00bdbda0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdbda0.md)

## 関数情報

~~~json
{
  "address": "00bdbda0",
  "name": "Botan::BigInt::randomize",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "020d5242d68fa6a4d400ec84ca156bc32fb61331086dd6dd14eec90d0256c88b",
  "source_text_sha256": "020d5242d68fa6a4d400ec84ca156bc32fb61331086dd6dd14eec90d0256c88b"
}
~~~
## 呼び出し元

- [00497bf4](../00497/00497bf4.md)
- [0049811c](../00498/0049811c.md)

## 呼び出し先

- [00497a4c](../00497/00497a4c.md)

## 疑似コード 1/1 / UTF-8 178 bytes

~~~c

void __thiscall
Botan::BigInt::randomize(BigInt *this,RandomNumberGenerator *param_1,ulong param_2,bool param_3)

{
  (*(code *)PTR_randomize_00c1c708)();
  return;
}

~~~
