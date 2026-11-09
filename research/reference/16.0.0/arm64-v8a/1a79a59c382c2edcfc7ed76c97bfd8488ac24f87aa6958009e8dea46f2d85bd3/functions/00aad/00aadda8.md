# 00aadda8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aadda8",
  "name": "FUN_00aadda8",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "33a86f8414a1dc6ddd9eb117f430b9555ce8055b9cb8945ae9d1706464bdb9a7",
  "source_text_sha256": "33a86f8414a1dc6ddd9eb117f430b9555ce8055b9cb8945ae9d1706464bdb9a7"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

## 疑似コード / UTF-8 542 bytes

~~~c

void FUN_00aadda8(long param_1)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  
  pbVar2 = *(byte **)(param_1 + 8);
  if (pbVar2 == (byte *)0x0) {
    return;
  }
  pbVar1 = *(byte **)(param_1 + 0x10);
  pbVar3 = pbVar2;
  if (pbVar1 != pbVar2) {
    do {
      pbVar3 = pbVar1 + -0x18;
      if ((*pbVar3 & 1) != 0) {
        _ZdlPv(*(void **)(pbVar1 + -8));
      }
      pbVar1 = pbVar3;
    } while (pbVar3 != pbVar2);
    pbVar3 = *(byte **)(param_1 + 8);
  }
  *(byte **)(param_1 + 0x10) = pbVar2;
  _ZdlPv(pbVar3);
  return;
}

~~~
