# 00bbbdc8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbbdc8",
  "name": "FUN_00bbbdc8",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b8f85adf2d1d77183254cdffc1891810a24b5a2a61ba3fe02bb27ca0ff3764ee",
  "source_text_sha256": "b8f85adf2d1d77183254cdffc1891810a24b5a2a61ba3fe02bb27ca0ff3764ee"
}
~~~

## 呼び出し元

- [00bbbb0c](../00bbb/00bbbb0c.md)

## 呼び出し先

- [00bbbebc](../00bbb/00bbbebc.md)
- [00bdb770](../00bdb/00bdb770.md)

## 疑似コード / UTF-8 1347 bytes

~~~c

undefined8 FUN_00bbbdc8(long param_1,long param_2)

{
  undefined *puVar1;
  undefined *puVar2;
  long lVar3;
  undefined8 uVar4;
  long lVar5;
  
  puVar2 = PTR__ZTIN10__cxxabiv119__pointer_type_infoE_00c1c018;
  puVar1 = PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8;
  while( true ) {
    if (param_2 == 0) {
      return 0;
    }
    lVar3 = __dynamic_cast(param_2,puVar1,puVar2,0);
    if (lVar3 == 0) {
      return 0;
    }
    if ((*(uint *)(lVar3 + 0x10) & (*(uint *)(param_1 + 0x10) ^ 0xffffffff)) != 0) {
      return 0;
    }
    lVar5 = *(long *)(param_1 + 0x18);
    param_2 = *(long *)(lVar3 + 0x18);
    if (*(long *)(lVar5 + 8) == *(long *)(param_2 + 8)) break;
    if ((*(uint *)(param_1 + 0x10) & 1) == 0) {
      return 0;
    }
    param_1 = __dynamic_cast(lVar5,puVar1,puVar2,0);
    if (param_1 == 0) {
      lVar3 = __dynamic_cast(lVar5,PTR__ZTIN10__cxxabiv116__shim_type_infoE_00c1bff8,
                             PTR__ZTIN10__cxxabiv129__pointer_to_member_type_infoE_00c1c030,0);
                    /* try { // try from 00bbbe78 to 00cbbe7f has its CatchHandler @ 00bbd2e8 */
      if (lVar3 != 0) {
        uVar4 = FUN_00bbbebc(lVar3,param_2);
        return uVar4;
      }
                    /* try { // try from 00bbbea8 to 00cbbebb has its CatchHandler @ 00bbd1ac */
      return 0;
    }
  }
  return 1;
}

~~~
