# 008ddabc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "008ddabc",
  "name": "FUN_008ddabc",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2e710bd00e72cca244ed2a96407fa0790520c01418db34b061195ad45c7708c7",
  "source_text_sha256": "2e710bd00e72cca244ed2a96407fa0790520c01418db34b061195ad45c7708c7"
}
~~~

## 呼び出し元

- [008dde04](../008dd/008dde04.md)

## 呼び出し先

- [008dbf84](../008db/008dbf84.md)

## 疑似コード / UTF-8 367 bytes

~~~c

void FUN_008ddabc(long param_1)

{
  int *piVar1;
  undefined8 *puVar2;
  int *piVar3;
  
  puVar2 = (undefined8 *)(*(long *)(param_1 + 0x38) + (long)*(int *)(param_1 + 4) * 0x18);
  piVar1 = (int *)puVar2[1];
  for (piVar3 = (int *)*puVar2; piVar3 != piVar1; piVar3 = piVar3 + 1) {
    FUN_008dbf84(*(long *)(param_1 + 8) + (long)*piVar3 * 0x100);
  }
  return;
}

~~~
