# 00afbea8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00afbea8",
  "name": "FUN_00afbea8",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "12224eefa1dc0951074b8aad3869cc066764f2f2fbce33fc6b4b4c311dbce4db",
  "source_text_sha256": "12224eefa1dc0951074b8aad3869cc066764f2f2fbce33fc6b4b4c311dbce4db"
}
~~~

## 呼び出し元

- [00700b50](../00700/00700b50.md)
- [00710330](../00710/00710330.md)
- [00a4f424](../00a4f/00a4f424.md)

## 呼び出し先

- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 314 bytes

~~~c

void FUN_00afbea8(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_00851550();
                    /* try { // try from 00afbec8 to 00bfbedb has its CatchHandler @ 00afcccc */
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849f4) = param_3;
  return;
}

~~~
