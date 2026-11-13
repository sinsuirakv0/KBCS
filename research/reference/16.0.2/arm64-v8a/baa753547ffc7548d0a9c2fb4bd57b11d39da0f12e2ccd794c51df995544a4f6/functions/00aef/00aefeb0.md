# 00aefeb0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aefeb0",
  "name": "FUN_00aefeb0",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a447de63664fa33eecdc9263be5f6b781a64ca84b2b7455bad6f411480263154",
  "source_text_sha256": "a447de63664fa33eecdc9263be5f6b781a64ca84b2b7455bad6f411480263154"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)

## 疑似コード / UTF-8 308 bytes

~~~c

void FUN_00aefeb0(long param_1)

{
  undefined8 *puVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  
  puVar1 = (undefined8 *)_Znwm(0x18);
  uVar3 = *(undefined8 *)(param_1 + 0x10);
  uVar2 = *(undefined8 *)(param_1 + 8);
  *puVar1 = &PTR_FUN_00c8e2b8;
  puVar1[2] = uVar3;
  puVar1[1] = uVar2;
  return;
}

~~~
