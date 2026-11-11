# 00afbeec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00afbeec",
  "name": "FUN_00afbeec",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "986bc7af9f6ec0d601ee8a3cb591cbb76c426e44e3c48c9bdf5b95353eee0406",
  "source_text_sha256": "986bc7af9f6ec0d601ee8a3cb591cbb76c426e44e3c48c9bdf5b95353eee0406"
}
~~~

## 呼び出し元

- [005f2d68](../005f2/005f2d68.md)
- [007102d8](../00710/007102d8.md)
- [00a4f3b4](../00a4f/00a4f3b4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 411 bytes

~~~c

void FUN_00afbeec(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00afbef0 to 00bfbef3 has its CatchHandler @ 00afcbb0 */
                    /* try { // try from 00afbef4 to 00bfc033 has its CatchHandler @ 00afb44c */
  lVar1 = FUN_008514f8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849f8) = param_3;
  return;
}

~~~
