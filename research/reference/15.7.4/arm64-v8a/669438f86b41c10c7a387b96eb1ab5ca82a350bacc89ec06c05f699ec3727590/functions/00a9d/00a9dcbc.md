# 00a9dcbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00a9dc78`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a9d/00a9dc78.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00a9dcbc",
  "name": "FUN_00a9dcbc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d67f69fd8b550b395c44cf12ce6b2cce8564298f8ce7f33383dc517cad175541",
  "source_text_sha256": "d67f69fd8b550b395c44cf12ce6b2cce8564298f8ce7f33383dc517cad175541"
}
~~~

## 呼び出し元

- [006d6d04](../006d6/006d6d04.md)

## 呼び出し先

- [005c2710](../005c2/005c2710.md)
- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 385 bytes

~~~c

bool FUN_00a9dcbc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_0081f580();
  uVar3 = FUN_005c2710(lVar2 + (long)param_1 * 0x1f0 + 0x2678);
  if ((uVar3 & 1) == 0) {
    lVar2 = FUN_0081f580();
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8422c) != 0;
  }
  else {
    bVar1 = false;
  }
  return bVar1;
}

~~~
