# 00a3becc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00a3becc",
  "name": "FUN_00a3becc",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "aaa34ca97ea40b64d5919b9afac0dcf6e3155840fadb654f5137ac211273d543",
  "source_text_sha256": "aaa34ca97ea40b64d5919b9afac0dcf6e3155840fadb654f5137ac211273d543"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [0081f580](../0081f/0081f580.md)
- [008f9c04](../008f9/008f9c04.md)

## 疑似コード / UTF-8 547 bytes

~~~c

void FUN_00a3becc(undefined8 param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  undefined8 uVar4;
  
  iVar1 = *param_3;
  if (iVar1 == 4) {
    lVar3 = FUN_0081f580();
    *(undefined1 *)(lVar3 + 0x20ff) = 0;
    lVar3 = FUN_0081f580();
    FUN_008f9c04(lVar3 + 0x472450,1);
    return;
  }
  if (iVar1 == 3) {
    uVar2 = FUN_00457e1c();
    uVar4 = 0xb;
  }
  else {
    if (iVar1 != 0) {
      return;
    }
    uVar2 = FUN_00457e1c();
    uVar4 = 10;
  }
  FUN_00459efc(uVar2,uVar4,0);
  return;
}

~~~
