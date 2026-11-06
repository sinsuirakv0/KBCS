# 00a9cffc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00a9cffc.md)

## 関数情報

~~~json
{
  "address": "00a9cffc",
  "name": "FUN_00a9cffc",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c2743541775df4556005b0997e4faf6823589d8b992f61c9ddb36fee4142a891",
  "source_text_sha256": "c2743541775df4556005b0997e4faf6823589d8b992f61c9ddb36fee4142a891"
}
~~~
## 呼び出し元

- [006d6d04](../006d6/006d6d04.md)
- [006ddfb8](../006dd/006ddfb8.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード 1/1 / UTF-8 191 bytes

~~~c

undefined4 FUN_00a9cffc(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_0081f580();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84380);
}

~~~
