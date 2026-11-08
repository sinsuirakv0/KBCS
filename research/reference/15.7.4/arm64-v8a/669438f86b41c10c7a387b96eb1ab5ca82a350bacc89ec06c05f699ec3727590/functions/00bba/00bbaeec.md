# 00bbaeec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00bbaeec",
  "name": "_ZNSt14overflow_errorD1Ev",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "77ec89ca0d940a7fb84d34cbd433ef99148ffbf8ac86c312c0cbe0ddf49f8adc",
  "source_text_sha256": "77ec89ca0d940a7fb84d34cbd433ef99148ffbf8ac86c312c0cbe0ddf49f8adc"
}
~~~

## 呼び出し元

- [00bdda70](../00bdd/00bdda70.md)
- [00be0f70](../00be0/00be0f70.md)
- [00be0fd0](../00be0/00be0fd0.md)
- [00be11a0](../00be1/00be11a0.md)
- [00be1e80](../00be1/00be1e80.md)

## 呼び出し先

- [00bd6e30](../00bd6/00bd6e30.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb490](../00bdb/00bdb490.md)

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt14overflow_errorD1Ev(long *param_1)

{
  int iVar1;
  long lVar2;
  
  lVar2 = param_1[1];
  *param_1 = (long)(PTR__ZTVSt13runtime_error_00c1bc68 + 0x10);
  iVar1 = FUN_00bd6e30(0xffffffff,lVar2 + -8);
  if (iVar1 + -1 < 0) {
    _ZdlPv((void *)(lVar2 + -0x18));
  }
  _ZNSt20bad_array_new_lengthD1Ev(param_1);
  return;
}

~~~
