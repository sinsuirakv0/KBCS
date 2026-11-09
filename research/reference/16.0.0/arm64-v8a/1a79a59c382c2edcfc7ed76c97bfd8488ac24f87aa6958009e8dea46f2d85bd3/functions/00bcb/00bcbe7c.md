# 00bcbe7c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00bcbe7c",
  "name": "_ZNK8firebase4auth4UsereqERKS1_",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a3e3e008a9d41adde8e32b844c122f3798375b2af003a9e889e306cd4679cacf",
  "source_text_sha256": "a3e3e008a9d41adde8e32b844c122f3798375b2af003a9e889e306cd4679cacf"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5a660](../00c5a/00c5a660.md)

## 疑似コード / UTF-8 260 bytes

~~~c

uint _ZNK8firebase4auth4UsereqERKS1_(undefined8 param_1,undefined8 param_2)

{
  uint uVar1;
  uint uVar2;
  
  uVar1 = _ZNK8firebase4auth4User8is_validEv();
  uVar2 = _ZNK8firebase4auth4User8is_validEv(param_2);
  return (uVar1 ^ uVar2 ^ 0xffffffff) & 1;
}

~~~
