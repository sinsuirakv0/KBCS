# 00afa7bc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afa7bc",
  "name": "FUN_00afa7bc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d9260173c934c0c37ccd2c5e53c09ec7b3306868c32cd513ec416eea75d8ef8",
  "source_text_sha256": "4d9260173c934c0c37ccd2c5e53c09ec7b3306868c32cd513ec416eea75d8ef8"
}
~~~

## 呼び出し元

- [0070eab4](../0070e/0070eab4.md)
- [00710330](../00710/00710330.md)
- [00711a48](../00711/00711a48.md)

## 呼び出し先

- [005e7460](../005e7/005e7460.md)
- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 579 bytes

~~~c

bool FUN_00afa7bc(int param_1,int param_2)

{
  bool bVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_00851550();
  uVar3 = FUN_005e7460(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    bVar1 = false;
  }
  else {
    lVar2 = FUN_00851550();
                    /* try { // try from 00afa810 to 00bfa823 has its CatchHandler @ 00afab7c */
    bVar1 = *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c28) != 0;
  }
                    /* try { // try from 00afa828 to 00bfa83f has its CatchHandler @ 00afaa48 */
  return bVar1;
}

~~~
