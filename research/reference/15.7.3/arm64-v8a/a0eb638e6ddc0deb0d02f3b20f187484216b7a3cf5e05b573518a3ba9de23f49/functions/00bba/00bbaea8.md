# 00bbaea8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbaea8",
  "name": "_ZNSt14overflow_errorD1Ev",
  "size": 88,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7c1c1b207874b7a02478d51f6ed2561bd12c44e46c57bbcb19c27f331c911174",
  "source_text_sha256": "7c1c1b207874b7a02478d51f6ed2561bd12c44e46c57bbcb19c27f331c911174"
}
~~~

## 呼び出し元

- [00bdda20](../00bdd/00bdda20.md)
- [00be0f20](../00be0/00be0f20.md)
- [00be0f80](../00be0/00be0f80.md)
- [00be1150](../00be1/00be1150.md)
- [00be1e30](../00be1/00be1e30.md)

## 呼び出し先

- [00bd6df0](../00bd6/00bd6df0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb440](../00bdb/00bdb440.md)

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt14overflow_errorD1Ev(long *param_1)

{
  int iVar1;
  long lVar2;
  
  lVar2 = param_1[1];
  *param_1 = (long)(PTR__ZTVSt13runtime_error_00c1bc18 + 0x10);
  iVar1 = FUN_00bd6df0(0xffffffff,lVar2 + -8);
  if (iVar1 + -1 < 0) {
    _ZdlPv((void *)(lVar2 + -0x18));
  }
  _ZNSt20bad_array_new_lengthD1Ev(param_1);
  return;
}

~~~
