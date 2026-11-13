# 00aeef3c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aeef3c",
  "name": "FUN_00aeef3c",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "01433974e8fcfdea6a655ddf880a581a6f166268b17ce418eb9c01d1e6e11fed",
  "source_text_sha256": "01433974e8fcfdea6a655ddf880a581a6f166268b17ce418eb9c01d1e6e11fed"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)

## 疑似コード / UTF-8 502 bytes

~~~c

void FUN_00aeef3c(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  puVar1 = (undefined8 *)_Znwm(0x18);
                    /* try { // try from 00aeef54 to 00beef5b has its CatchHandler @ 00aef048 */
  uVar3 = *(undefined8 *)(param_1 + 0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
                    /* try { // try from 00aeef5c to 00bef077 has its CatchHandler @ 00aeee7c */
  *puVar1 = &PTR_FUN_00c8dfc8;
  puVar1[2] = uVar3;
  puVar1[1] = uVar2;
  return;
}

~~~
