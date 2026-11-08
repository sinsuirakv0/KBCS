# 00a9cdfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00a9cdfc",
  "name": "FUN_00a9cdfc",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1fd4fafc93ea5c76fa068c0c047d814f9efe7cc9e611448c56918f1de443d7d2",
  "source_text_sha256": "1fd4fafc93ea5c76fa068c0c047d814f9efe7cc9e611448c56918f1de443d7d2"
}
~~~

## 呼び出し元

- [005ce03c](../005ce/005ce03c.md)

## 呼び出し先

- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 248 bytes

~~~c

void FUN_00a9cdfc(int param_1,int param_2,int param_3)

{
  long lVar1;
  
  lVar1 = FUN_0081f580();
  lVar1 = lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar1 + 0x84324) = *(int *)(lVar1 + 0x84324) + param_3;
  return;
}

~~~
