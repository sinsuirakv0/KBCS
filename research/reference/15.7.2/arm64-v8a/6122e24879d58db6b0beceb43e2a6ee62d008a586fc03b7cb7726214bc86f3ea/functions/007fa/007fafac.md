# 007fafac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](007fafac.md)

## 関数情報

~~~json
{
  "address": "007fafac",
  "name": "FUN_007fafac",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "22ea837597b2413136536be6b1ce38d837c4ade4b48a9756f2f5273e1cb1b9b1",
  "source_text_sha256": "22ea837597b2413136536be6b1ce38d837c4ade4b48a9756f2f5273e1cb1b9b1"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf50](../00bda/00bdaf50.md)

## 疑似コード 1/1 / UTF-8 188 bytes

~~~c

void FUN_007fafac(__shared_weak_count *param_1)

{
  *(undefined ***)param_1 = &PTR_FUN_00c00348;
  std::__ndk1::__shared_weak_count::~__shared_weak_count(param_1);
  return;
}

~~~
