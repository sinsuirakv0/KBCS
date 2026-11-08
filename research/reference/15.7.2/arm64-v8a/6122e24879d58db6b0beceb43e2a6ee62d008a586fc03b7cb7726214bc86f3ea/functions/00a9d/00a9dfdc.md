# 00a9dfdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00a9dfdc",
  "name": "FUN_00a9dfdc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7e5ae2de7bd1243794ffd1ff2c07ac335429736407423b35588fcc15d78b9c46",
  "source_text_sha256": "7e5ae2de7bd1243794ffd1ff2c07ac335429736407423b35588fcc15d78b9c46"
}
~~~

## 呼び出し元

- [006eb464](../006eb/006eb464.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00a9dfdc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_0081f580();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x842f0);
}

~~~
