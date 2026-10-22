# 00bdaea0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdaea0.md)

## 関数情報

~~~json
{
  "address": "00bdaea0",
  "name": "operator.new[]",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cba2f05a076d432a99edd9e23e9893a62604bf1a7c96d3adf66be59753c23220",
  "source_text_sha256": "cba2f05a076d432a99edd9e23e9893a62604bf1a7c96d3adf66be59753c23220"
}
~~~
## 呼び出し元

- [00be1e20](../00be1/00be1e20.md)

## 呼び出し先

- [00be1e00](../00be1/00be1e00.md)

## 疑似コード 1/1 / UTF-8 165 bytes

~~~c

/* operator new[](unsigned long, std::align_val_t) */

void * operator_new__(void)

{
  void *pvVar1;
  
  pvVar1 = operator_new();
  return pvVar1;
}

~~~
