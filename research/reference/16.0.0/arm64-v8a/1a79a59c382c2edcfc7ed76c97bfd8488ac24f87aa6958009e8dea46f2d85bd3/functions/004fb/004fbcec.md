# 004fbcec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "004fbcec",
  "name": "_ZN5Botan15Stream_IO_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 180,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a53690425b88d565ba180c8f3be2191e3fca97f7a2038660ced3c381cf5d3814",
  "source_text_sha256": "a53690425b88d565ba180c8f3be2191e3fca97f7a2038660ced3c381cf5d3814"
}
~~~

## 呼び出し元

- [00c583b0](../00c58/00c583b0.md)

## 呼び出し先

- [0043bae0](../0043b/0043bae0.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57cb0](../00c57/00c57cb0.md)

## 関連文字列（未確認候補）

~~~text
"I/O error: "
~~~

## 疑似コード / UTF-8 994 bytes

~~~c

void _ZN5Botan15Stream_IO_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (long *param_1)

{
  long lVar1;
  byte local_50;
  undefined7 uStack_4f;
  long lStack_48;
  void *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_50,"I/O error: ");
  *param_1 = (long)(PTR__ZTVN5Botan9ExceptionE_00c9a9d0 + 0x10);
  if ((local_50 & 1) == 0) {
    param_1[2] = lStack_48;
    param_1[1] = CONCAT71(uStack_4f,local_50);
    param_1[3] = (long)local_40;
  }
  else {
    FUN_0043bae0(param_1 + 1,local_40,lStack_48);
    if ((local_50 & 1) != 0) {
      _ZdlPv(local_40);
    }
  }
  *param_1 = (long)(PTR__ZTVN5Botan15Stream_IO_ErrorE_00c9aca8 + 0x10);
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
