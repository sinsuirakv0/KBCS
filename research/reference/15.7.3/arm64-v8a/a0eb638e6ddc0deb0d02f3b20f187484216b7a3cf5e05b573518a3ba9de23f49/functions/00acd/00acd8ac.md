# 00acd8ac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00acd8ac",
  "name": "FUN_00acd8ac",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c7e2b6aebdcf688cad29ecacd582b15328ced32f8212d8752354bf4dc78f24a5",
  "source_text_sha256": "c7e2b6aebdcf688cad29ecacd582b15328ced32f8212d8752354bf4dc78f24a5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00418fe0](../00418/00418fe0.md)

## 疑似コード / UTF-8 549 bytes

~~~c

void FUN_00acd8ac(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  undefined8 uVar2;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  *param_2 = &PTR_FUN_00c0f7f8;
  param_2[1] = uVar1;
  if ((*(byte *)(param_1 + 0x10) & 1) == 0) {
    uVar2 = *(undefined8 *)(param_1 + 0x18);
    uVar1 = *(undefined8 *)(param_1 + 0x10);
    param_2[4] = *(undefined8 *)(param_1 + 0x20);
    param_2[3] = uVar2;
    param_2[2] = uVar1;
    return;
  }
  FUN_00418fe0(param_2 + 2,*(undefined8 *)(param_1 + 0x20),*(undefined8 *)(param_1 + 0x18));
  return;
}

~~~
