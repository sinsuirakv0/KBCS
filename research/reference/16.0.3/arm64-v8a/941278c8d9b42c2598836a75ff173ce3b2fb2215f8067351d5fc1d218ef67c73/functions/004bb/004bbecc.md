# 004bbecc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "004bbecc",
  "name": "FUN_004bbecc",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3efdc80386d9acf97fd9a152dca3856c19e4031ffe4a3d7d947df2f709b28d8f",
  "source_text_sha256": "3efdc80386d9acf97fd9a152dca3856c19e4031ffe4a3d7d947df2f709b28d8f"
}
~~~

## 呼び出し元

- [004b6a88](../004b6/004b6a88.md)
- [004b9c5c](../004b9/004b9c5c.md)
- [004ba7f8](../004ba/004ba7f8.md)
- [004de268](../004de/004de268.md)

## 呼び出し先

- [0043e138](../0043e/0043e138.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c58f90](../00c58/00c58f90.md)
- [00c58fb0](../00c58/00c58fb0.md)
- [00c59710](../00c59/00c59710.md)

## 関連文字列（未確認候補）

~~~text
"bigint_divop divide by zero"
~~~

## 疑似コード / UTF-8 972 bytes

~~~c

ulong FUN_004bbecc(long param_1,ulong param_2,uint param_3)

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
    FUN_0043e138(auStack_50,"bigint_divop divide by zero");
    _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (uVar3,auStack_50);
    if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar3,PTR__ZTIN5Botan16Invalid_ArgumentE_00c9bdd0,FUN_00535bc8);
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
