# 00a3cfbc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00a3cfbc",
  "name": "FUN_00a3cfbc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0c86941d0c824a399303bd0e03766d5530b881d877429b10d651573354c5dcd2",
  "source_text_sha256": "0c86941d0c824a399303bd0e03766d5530b881d877429b10d651573354c5dcd2"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_00a3cfbc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c0d5c8;
  puVar1[1] = uVar2;
  return;
}

~~~
