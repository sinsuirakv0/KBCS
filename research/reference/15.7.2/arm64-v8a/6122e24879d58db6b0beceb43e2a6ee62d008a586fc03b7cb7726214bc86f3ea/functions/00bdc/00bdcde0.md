# 00bdcde0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdcde0.md)

## 関数情報

~~~json
{
  "address": "00bdcde0",
  "name": "Botan::Extensions::replace",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e68a9c5bfcffaac155403629ba726a741d269fce26e11e537e272354324d9469",
  "source_text_sha256": "e68a9c5bfcffaac155403629ba726a741d269fce26e11e537e272354324d9469"
}
~~~
## 呼び出し元

- [004ede80](../004ed/004ede80.md)

## 呼び出し先

- [004ee4f4](../004ee/004ee4f4.md)

## 疑似コード 1/1 / UTF-8 286 bytes

~~~c

void __thiscall
Botan::Extensions::replace(Extensions *this,Certificate_Extension *param_1,bool param_2)

{
                    /* try { // try from 00bdcde0 to 00cdce3b has its CatchHandler @ 00bdcbcc */
  (*(code *)PTR_replace_00c1cf28)(this,param_1,param_2);
  return;
}

~~~
