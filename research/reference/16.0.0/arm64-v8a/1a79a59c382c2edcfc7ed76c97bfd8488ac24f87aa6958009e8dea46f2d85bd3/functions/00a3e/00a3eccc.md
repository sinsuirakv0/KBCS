# 00a3eccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00a3eccc",
  "name": "FUN_00a3eccc",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c3a949852d9d09b5fb8101efa48d200fafe5bffbdaaeb1a8db622b1352048e9",
  "source_text_sha256": "9c3a949852d9d09b5fb8101efa48d200fafe5bffbdaaeb1a8db622b1352048e9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [006917c0](../00691/006917c0.md)

## 疑似コード / UTF-8 483 bytes

~~~c

void FUN_00a3eccc(long param_1,undefined8 *param_2)

{
  undefined8 uVar1;
  
  uVar1 = *(undefined8 *)(param_1 + 8);
  param_2[3] = 0;
  param_2[2] = param_2 + 3;
  param_2[1] = uVar1;
  param_2[4] = 0;
  uVar1 = *(undefined8 *)(param_1 + 0x10);
  *param_2 = &PTR_FUN_00c8b0a8;
  FUN_006917c0(param_2 + 2,uVar1,param_1 + 0x18);
  param_2[6] = 0;
  param_2[5] = param_2 + 6;
  param_2[7] = 0;
  FUN_006917c0(param_2 + 5,*(undefined8 *)(param_1 + 0x28),param_1 + 0x30);
  return;
}

~~~
