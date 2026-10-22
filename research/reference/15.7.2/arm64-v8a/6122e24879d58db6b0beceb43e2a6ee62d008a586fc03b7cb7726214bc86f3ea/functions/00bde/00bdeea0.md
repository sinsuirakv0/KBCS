# 00bdeea0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bdeea0.md)

## 関数情報

~~~json
{
  "address": "00bdeea0",
  "name": "operator.new[]",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "caaeb225cdc3a415920f10c9bee12623a774a95492f9ed5fcfc3545930318ec2",
  "source_text_sha256": "caaeb225cdc3a415920f10c9bee12623a774a95492f9ed5fcfc3545930318ec2"
}
~~~
## 呼び出し元

- [00b034b4](../00b03/00b034b4.md)
- [00b2e528](../00b2e/00b2e528.md)
- [00b47b50](../00b47/00b47b50.md)
- [00b47c40](../00b47/00b47c40.md)
- [00b5732c](../00b57/00b5732c.md)
- [00b58fa4](../00b58/00b58fa4.md)
- [00bd4dd4](../00bd4/00bd4dd4.md)

## 呼び出し先

- [00bdae08](../00bda/00bdae08.md)

## 疑似コード 1/1 / UTF-8 151 bytes

~~~c

void * operator_new__(ulong param_1)

{
  void *pvVar1;
  
  pvVar1 = (void *)(*(code *)PTR_operator_new___00c1df88)();
  return pvVar1;
}

~~~
