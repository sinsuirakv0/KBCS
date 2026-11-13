# 00aefac8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aefac8",
  "name": "FUN_00aefac8",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e03d5ab5ee8e70d7158562d2405ae134db6b0ca87d6f8f2c556a7ae6763ef98d",
  "source_text_sha256": "e03d5ab5ee8e70d7158562d2405ae134db6b0ca87d6f8f2c556a7ae6763ef98d"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008b6ab4](../008b6/008b6ab4.md)
- [008b6f68](../008b6/008b6f68.md)
- [008b7a20](../008b7/008b7a20.md)

## 疑似コード / UTF-8 193 bytes

~~~c

void FUN_00aefac8(long param_1)

{
  undefined8 uVar1;
  
  uVar1 = FUN_008b7a20(*(long *)(param_1 + 8) + 0x2f38,0x326);
  uVar1 = FUN_008b6f68(uVar1,1);
  FUN_008b6ab4(uVar1,0);
  return;
}

~~~
