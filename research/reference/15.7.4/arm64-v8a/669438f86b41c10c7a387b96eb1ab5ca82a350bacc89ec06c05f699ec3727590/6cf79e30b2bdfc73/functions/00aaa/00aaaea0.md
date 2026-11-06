# 00aaaea0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00aaaea0.md)

## 関数情報

~~~json
{
  "address": "00aaaea0",
  "name": "FUN_00aaaea0",
  "size": 328,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "02399844d3cc14da89562dd5da46bd3f82a6fceb8c31005e5a16757316d74e99",
  "source_text_sha256": "02399844d3cc14da89562dd5da46bd3f82a6fceb8c31005e5a16757316d74e99"
}
~~~
## 呼び出し元

- [0079bdf0](../0079b/0079bdf0.md)
- [00a7268c](../00a72/00a7268c.md)

## 呼び出し先

- [007cf950](../007cf/007cf950.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [0081f580](../0081f/0081f580.md)
- [00aaa700](../00aaa/00aaa700.md)
- [00bdb600](../00bdb/00bdb600.md)

## 疑似コード 1/1 / UTF-8 1823 bytes

~~~c

undefined8 FUN_00aaaea0(long param_1,ulong param_2,ulong param_3,ulong param_4)

{
  long lVar1;
  wchar_t *pwVar2;
  long lVar3;
  wchar_t *pwVar4;
  long lVar5;
  
  if ((int)param_2 == -1) {
    param_2 = FUN_007cf950(0);
    param_2 = param_2 & 0xffffffff;
    param_3 = FUN_007cfaa0();
    param_3 = param_3 & 0xffffffff;
    param_4 = FUN_007cfcd8();
    param_4 = param_4 & 0xffffffff;
  }
  FUN_00aaa700(param_1,param_2,param_3,param_4);
  lVar5 = 0;
  while( true ) {
    lVar3 = FUN_0081f580();
    lVar1 = lVar3 + lVar5;
    if (((uint)(*(byte *)(lVar3 + 0xc76e) ^ *(byte *)(lVar1 + 0xc746)) << 0x10 |
         (uint)(*(byte *)(lVar3 + 0xc76f) ^ *(byte *)(lVar1 + 0xc747)) << 0x18 |
         (uint)(*(byte *)(lVar3 + 0xc76d) ^ *(byte *)(lVar1 + 0xc745)) << 8 |
        (uint)(*(byte *)(lVar3 + 0xc76c) ^ *(byte *)(lVar1 + 0xc744))) == 0xffffffff) {
      return 0;
    }
    lVar3 = FUN_0081f580();
    lVar1 = lVar3 + lVar5;
    pwVar2 = *(wchar_t **)(param_1 + 0x38);
    pwVar4 = wmemchr(*(wchar_t **)(param_1 + 0x30),
                     CONCAT13(*(byte *)(lVar3 + 0xc76f) ^ *(byte *)(lVar1 + 0xc747),
                              CONCAT12(*(byte *)(lVar3 + 0xc76e) ^ *(byte *)(lVar1 + 0xc746),
                                       CONCAT11(*(byte *)(lVar3 + 0xc76d) ^
                                                *(byte *)(lVar1 + 0xc745),
                                                *(byte *)(lVar3 + 0xc76c) ^
                                                *(byte *)(lVar1 + 0xc744)))) + L'\xfffffffe',
                     (long)pwVar2 - (long)*(wchar_t **)(param_1 + 0x30) >> 2);
    if (pwVar4 != (wchar_t *)0x0) {
      pwVar2 = pwVar4;
    }
    if (pwVar2 != *(wchar_t **)(param_1 + 0x38)) break;
    lVar5 = lVar5 + 4;
    if (lVar5 == 0x28) {
      return 0;
    }
  }
  return 1;
}

~~~
