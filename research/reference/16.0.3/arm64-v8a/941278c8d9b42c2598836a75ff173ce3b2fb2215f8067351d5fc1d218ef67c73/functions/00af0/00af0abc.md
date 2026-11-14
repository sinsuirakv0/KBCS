# 00af0abc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00af0abc",
  "name": "FUN_00af0abc",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b10d7c74d1f05181470338cea8b79af75ea853ab334c06ecfc0fcd45949fcdd8",
  "source_text_sha256": "b10d7c74d1f05181470338cea8b79af75ea853ab334c06ecfc0fcd45949fcdd8"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [008b7a60](../008b7/008b7a60.md)
- [008b7f14](../008b7/008b7f14.md)
- [008b89cc](../008b8/008b89cc.md)

## 疑似コード / UTF-8 387 bytes

~~~c

void FUN_00af0abc(long param_1)

{
  undefined8 uVar1;
  
                    /* try { // try from 00af0ac8 to 00bf0acf has its CatchHandler @ 00af0dac */
                    /* try { // try from 00af0ad0 to 00bf0b47 has its CatchHandler @ 00af08e0 */
  uVar1 = FUN_008b89cc(*(long *)(param_1 + 8) + 0x2f38,0x326);
  uVar1 = FUN_008b7f14(uVar1,1);
  FUN_008b7a60(uVar1,0);
  return;
}

~~~
