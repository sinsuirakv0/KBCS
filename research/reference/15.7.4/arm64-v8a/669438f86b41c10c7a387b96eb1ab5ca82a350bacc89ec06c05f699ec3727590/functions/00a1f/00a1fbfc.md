# 00a1fbfc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00a1fbfc",
  "name": "FUN_00a1fbfc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "98bdd9b385e3e40723d856df45b1fdbfa866e71c21f54929f550e65052adae55",
  "source_text_sha256": "98bdd9b385e3e40723d856df45b1fdbfa866e71c21f54929f550e65052adae55"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_00a1fbfc(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  
  puVar1 = (undefined8 *)_Znwm(0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c0c300;
  puVar1[1] = uVar2;
  return;
}

~~~
