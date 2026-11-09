# 009dbbbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "009dbbbc",
  "name": "FUN_009dbbbc",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a57cd388689d2c07aecf392818f884a1a9b77722938eda515f038e1a5458f34b",
  "source_text_sha256": "a57cd388689d2c07aecf392818f884a1a9b77722938eda515f038e1a5458f34b"
}
~~~

## 呼び出し元

- [00707ea0](../00707/00707ea0.md)

## 呼び出し先

- [0046bd14](../0046b/0046bd14.md)
- [00470074](../00470/00470074.md)

## 疑似コード / UTF-8 643 bytes

~~~c

void FUN_009dbbbc(undefined8 param_1,long param_2,undefined8 param_3,undefined4 param_4,
                 undefined4 param_5,undefined4 param_6,int param_7)

{
  long lVar1;
  long lVar2;
  
  lVar1 = 0x1480;
  if (param_7 != 0) {
    lVar1 = 0x1aa0;
  }
  lVar2 = 0x1528;
  if (param_7 != 0) {
    lVar2 = 0x1b48;
  }
  FUN_00470074(param_2 + lVar1,param_2 + lVar2,param_6,0);
                    /* try { // try from 009dbc14 to 00adbc1f has its CatchHandler @ 009dbf28 */
                    /* try { // try from 009dbc20 to 00adbc27 has its CatchHandler @ 009dbf20 */
  FUN_0046bd14(param_3,param_2 + lVar1,param_4,param_5);
  return;
}

~~~
