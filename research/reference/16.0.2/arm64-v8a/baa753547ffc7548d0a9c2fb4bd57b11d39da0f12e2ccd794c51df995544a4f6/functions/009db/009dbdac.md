# 009dbdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "009dbdac",
  "name": "FUN_009dbdac",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "431db0eb2e66e9387760b70dbfd65e95d0e3e80412425fee702ae8b9984a4535",
  "source_text_sha256": "431db0eb2e66e9387760b70dbfd65e95d0e3e80412425fee702ae8b9984a4535"
}
~~~

## 呼び出し元

- [00707f38](../00707/00707f38.md)

## 呼び出し先

- [0046bd94](../0046b/0046bd94.md)
- [004700f4](../00470/004700f4.md)

## 疑似コード / UTF-8 643 bytes

~~~c

void FUN_009dbdac(undefined8 param_1,long param_2,undefined8 param_3,undefined4 param_4,
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
  FUN_004700f4(param_2 + lVar1,param_2 + lVar2,param_6,0);
                    /* try { // try from 009dbe04 to 00adbe0f has its CatchHandler @ 009dc118 */
                    /* try { // try from 009dbe10 to 00adbe17 has its CatchHandler @ 009dc110 */
  FUN_0046bd94(param_3,param_2 + lVar1,param_4,param_5);
  return;
}

~~~
