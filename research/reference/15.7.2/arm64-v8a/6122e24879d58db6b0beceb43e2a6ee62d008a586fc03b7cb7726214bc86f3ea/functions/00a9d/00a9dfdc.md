# 00a9dfdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a9dfdc.md)

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
  "source_sha256": "12f6118f59fa8ebc8e943e192a28d029627d89da307284eb0712ea424c46ee24",
  "source_text_sha256": "12f6118f59fa8ebc8e943e192a28d029627d89da307284eb0712ea424c46ee24"
}
~~~
## 呼び出し元

- [006eb464](../006eb/006eb464.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 201 bytes

~~~c

undefined4 FUN_00a9dfdc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_0081f580();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x842f0);
}

~~~
