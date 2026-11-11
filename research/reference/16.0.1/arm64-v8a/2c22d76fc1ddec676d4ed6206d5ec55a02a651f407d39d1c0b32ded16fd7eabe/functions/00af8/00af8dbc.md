# 00af8dbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00af8dbc",
  "name": "FUN_00af8dbc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "32af45fae7140d3e92a34fbe5301802304b7df0d7b3dca07d1254a0224f9aee3",
  "source_text_sha256": "32af45fae7140d3e92a34fbe5301802304b7df0d7b3dca07d1254a0224f9aee3"
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)
- [00af3500](../00af3/00af3500.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00af8dbc(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84994) = param_3;
  return;
}

~~~
