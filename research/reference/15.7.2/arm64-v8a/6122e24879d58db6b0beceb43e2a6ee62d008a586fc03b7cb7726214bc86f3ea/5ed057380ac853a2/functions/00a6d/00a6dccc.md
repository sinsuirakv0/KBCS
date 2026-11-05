# 00a6dccc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a6dccc.md)

## 関数情報

~~~json
{
  "address": "00a6dccc",
  "name": "FUN_00a6dccc",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0c7d514cea52e14a368d9f9e179c04ce973ea6e439527e75dcd0cd2518fe85f2",
  "source_text_sha256": "0c7d514cea52e14a368d9f9e179c04ce973ea6e439527e75dcd0cd2518fe85f2"
}
~~~
## 呼び出し元

- [00707eec](../00707/00707eec.md)
- [00900f40](../00900/00900f40.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード 1/1 / UTF-8 454 bytes

~~~c

int FUN_00a6dccc(long param_1)

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
