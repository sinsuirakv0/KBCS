# 00a9bfcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a9bfcc.md)

## 関数情報

~~~json
{
  "address": "00a9bfcc",
  "name": "FUN_00a9bfcc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0705056bb127283acd4a904f3068480f912f41842448d7d5d2c7049a755f2c6f",
  "source_text_sha256": "0705056bb127283acd4a904f3068480f912f41842448d7d5d2c7049a755f2c6f"
}
~~~
## 呼び出し元

- [005ce03c](../005ce/005ce03c.md)
- [006d6d04](../006d6/006d6d04.md)
- [006ddfb8](../006dd/006ddfb8.md)
- [006eb464](../006eb/006eb464.md)
- [006eccf4](../006ec/006eccf4.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 201 bytes

~~~c

undefined4 FUN_00a9bfcc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_0081f580();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84174);
}

~~~
