# 00acbce0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00acbce0",
  "name": "FUN_00acbce0",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f160912622d3e3e7f1931a0add23f0f25332bb32a6753c41fce813db89c126b3",
  "source_text_sha256": "f160912622d3e3e7f1931a0add23f0f25332bb32a6753c41fce813db89c126b3"
}
~~~

## 呼び出し元

- [00731fec](../00731/00731fec.md)
- [00935974](../00935/00935974.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 458 bytes

~~~c

int FUN_00acbce0(long param_1)

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
      iVar2 = *(int *)(lVar3 + 0xc) + iVar2;
      lVar1 = *(long *)(param_1 + 0x30);
      lVar3 = param_1;
    } while (*(long *)(param_1 + 0x30) != 0);
  }
  return *(int *)(param_1 + 0xc) + iVar2;
}

~~~
