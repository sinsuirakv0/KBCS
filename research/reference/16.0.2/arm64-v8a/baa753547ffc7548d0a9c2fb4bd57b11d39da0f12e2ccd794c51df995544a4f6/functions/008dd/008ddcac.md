# 008ddcac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "008ddcac",
  "name": "FUN_008ddcac",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bb80e9339875cc955f5c3349ee642e34b5b55734f7d47ea33dfd6f5fb9785598",
  "source_text_sha256": "bb80e9339875cc955f5c3349ee642e34b5b55734f7d47ea33dfd6f5fb9785598"
}
~~~

## 呼び出し元

- [008ddff4](../008dd/008ddff4.md)

## 呼び出し先

- [008dc174](../008dc/008dc174.md)

## 疑似コード / UTF-8 464 bytes

~~~c

void FUN_008ddcac(long param_1)

{
  int *piVar1;
  undefined8 *puVar2;
  int *piVar3;
  
  puVar2 = (undefined8 *)(*(long *)(param_1 + 0x38) + (long)*(int *)(param_1 + 4) * 0x18);
  piVar1 = (int *)puVar2[1];
                    /* try { // try from 008ddcd8 to 009ddcdf has its CatchHandler @ 008de4a4 */
  for (piVar3 = (int *)*puVar2; piVar3 != piVar1; piVar3 = piVar3 + 1) {
    FUN_008dc174(*(long *)(param_1 + 8) + (long)*piVar3 * 0x100);
  }
  return;
}

~~~
