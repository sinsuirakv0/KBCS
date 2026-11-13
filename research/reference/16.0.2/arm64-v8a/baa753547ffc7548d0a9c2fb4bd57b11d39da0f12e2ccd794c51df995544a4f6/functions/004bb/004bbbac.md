# 004bbbac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "004bbbac",
  "name": "FUN_004bbbac",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a11b6a34913c387246c1e152b8b6a23339d5f0b7084457f2a8ad996e25cab1ac",
  "source_text_sha256": "a11b6a34913c387246c1e152b8b6a23339d5f0b7084457f2a8ad996e25cab1ac"
}
~~~

## 呼び出し元

- [004b6768](../004b6/004b6768.md)
- [004b993c](../004b9/004b993c.md)
- [004ba4d8](../004ba/004ba4d8.md)
- [004ddf48](../004dd/004ddf48.md)

## 呼び出し先

- [0043de18](../0043d/0043de18.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c57fe0](../00c57/00c57fe0.md)
- [00c58740](../00c58/00c58740.md)

## 関連文字列（未確認候補）

~~~text
"bigint_divop divide by zero"
~~~

## 疑似コード / UTF-8 972 bytes

~~~c

ulong FUN_004bbbac(long param_1,ulong param_2,uint param_3)

{
  ulong uVar1;
  long lVar2;
  undefined8 uVar3;
  undefined1 auStack_50 [24];
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  if (param_3 == 0) {
    uVar3 = __cxa_allocate_exception(0x20);
    FUN_0043de18(auStack_50,"bigint_divop divide by zero");
    _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (uVar3,auStack_50);
    if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar3,PTR__ZTIN5Botan16Invalid_ArgumentE_00c9ae00,FUN_005358a8);
    }
  }
  else if (*(long *)(lVar2 + 0x28) == local_38) {
    uVar1 = 0;
    if ((ulong)param_3 != 0) {
      uVar1 = (param_2 & 0xffffffff | param_1 << 0x20) / (ulong)param_3;
    }
    return uVar1;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
