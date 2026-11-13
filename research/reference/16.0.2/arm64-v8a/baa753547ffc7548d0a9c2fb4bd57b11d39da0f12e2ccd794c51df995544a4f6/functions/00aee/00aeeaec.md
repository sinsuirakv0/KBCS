# 00aeeaec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00aeeaec",
  "name": "FUN_00aeeaec",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1cbd3648d3e25e98306ebbec4fde43ac9416bf6252f7b498b3bc1c77932188f4",
  "source_text_sha256": "1cbd3648d3e25e98306ebbec4fde43ac9416bf6252f7b498b3bc1c77932188f4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [008b91d0](../008b9/008b91d0.md)
- [008b98a8](../008b9/008b98a8.md)
- [008bb568](../008bb/008bb568.md)

## 疑似コード / UTF-8 666 bytes

~~~c

void FUN_00aeeaec(long param_1,undefined8 param_2,int *param_3)

{
  undefined8 uVar1;
  long lVar2;
  
  if (*param_3 == 3) {
    lVar2 = *(long *)(param_1 + 8);
    uVar1 = FUN_0047ad34();
    FUN_0047ce14(uVar1,0xb,0);
    uVar1 = FUN_008bb568(lVar2 + 0x2f08);
    FUN_008b98a8(uVar1,2);
    FUN_008bb568(lVar2 + 0x2f08);
    FUN_008b91d0();
    return;
  }
                    /* try { // try from 00aeeb04 to 00beeb0f has its CatchHandler @ 00aeecac */
  if (*param_3 == 0) {
    uVar1 = FUN_0047ad34();
                    /* try { // try from 00aeeb10 to 00beeca7 has its CatchHandler @ 00aee9c4 */
    FUN_0047ce14(uVar1,10,0);
    return;
  }
  return;
}

~~~
