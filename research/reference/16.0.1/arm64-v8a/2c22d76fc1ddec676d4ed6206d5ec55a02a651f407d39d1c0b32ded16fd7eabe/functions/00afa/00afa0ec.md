# 00afa0ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afa0ec",
  "name": "FUN_00afa0ec",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "88e97c4bd94636d186d2590cb8a6b4af33041485ae369ae8bdd16dca8a10dc4a",
  "source_text_sha256": "88e97c4bd94636d186d2590cb8a6b4af33041485ae369ae8bdd16dca8a10dc4a"
}
~~~

## 呼び出し元

- [007119f0](../00711/007119f0.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 1107 bytes

~~~c

undefined4 FUN_00afa0ec(int param_1,int param_2)

{
  undefined4 uVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514f8();
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    uVar1 = 0;
  }
  else {
    lVar2 = FUN_008514f8();
                    /* try { // try from 00afa138 to 00bfa15b has its CatchHandler @ 00afa9d0 */
    uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
                    /* try { // try from 00afa164 to 00bfa16b has its CatchHandler @ 00afaab0 */
    if ((((uVar3 & 1) == 0) ||
        (lVar2 = FUN_008514f8(),
        *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bdc) == 0)) ||
       (lVar2 = FUN_008514f8(),
       *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c60) != 0)) {
      lVar2 = FUN_008514f8();
      uVar1 = *(undefined4 *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c60);
    }
    else {
      uVar1 = 0x46;
                    /* try { // try from 00afa1c8 to 00bfa1cf has its CatchHandler @ 00afa9cc */
    }
  }
  return uVar1;
}

~~~
