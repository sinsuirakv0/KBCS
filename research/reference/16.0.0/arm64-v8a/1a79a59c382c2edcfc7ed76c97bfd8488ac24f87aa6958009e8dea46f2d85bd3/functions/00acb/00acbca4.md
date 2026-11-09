# 00acbca4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acbca4",
  "name": "FUN_00acbca4",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e7ed64b461765637d5d447747b9918164b0e2c3e6b5093d718309d5387424b8",
  "source_text_sha256": "1e7ed64b461765637d5d447747b9918164b0e2c3e6b5093d718309d5387424b8"
}
~~~

## 呼び出し元

- [00731fec](../00731/00731fec.md)
- [00935974](../00935/00935974.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 454 bytes

~~~c

int FUN_00acbca4(long param_1)

{
  long lVar1;
  int iVar2;
  long lVar3;
  
  if (*(long *)(param_1 + 0x30) == 0) {
    iVar2 = 0;
  }
  else {
    iVar2 = 0;
    lVar1 = *(long *)(param_1 + 0x30);
    lVar3 = param_1;
    do {
      param_1 = lVar1;
      iVar2 = *(int *)(lVar3 + 8) + iVar2;
      lVar1 = *(long *)(param_1 + 0x30);
      lVar3 = param_1;
    } while (*(long *)(param_1 + 0x30) != 0);
  }
  return *(int *)(param_1 + 8) + iVar2;
}

~~~
