# 00afbcf4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afbcf4",
  "name": "FUN_00afbcf4",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9969ec7c963893e18f7ada34858b50240ad64215118a042f7857b85bac0b6311",
  "source_text_sha256": "9969ec7c963893e18f7ada34858b50240ad64215118a042f7857b85bac0b6311"
}
~~~

## 呼び出し元

- [005f2d68](../005f2/005f2d68.md)
- [007102d8](../00710/007102d8.md)
- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 217 bytes

~~~c

void FUN_00afbcf4(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849d4) = param_3;
  return;
}

~~~
