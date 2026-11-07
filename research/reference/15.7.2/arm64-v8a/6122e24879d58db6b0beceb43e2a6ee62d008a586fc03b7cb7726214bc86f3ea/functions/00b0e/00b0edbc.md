# 00b0edbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00b0eec8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b0e/00b0eec8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00b0edbc",
  "name": "_ZN11flatbuffers6Parser7WarningERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "526837294ef7c76c6897889cfd7d09d9b4fe24c3135eea067c8f684130c2aa8c",
  "source_text_sha256": "526837294ef7c76c6897889cfd7d09d9b4fe24c3135eea067c8f684130c2aa8c"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdf8d0](../00bdf/00bdf8d0.md)

## 関連文字列（未確認候補）

~~~text
"warning: "
~~~

## 疑似コード / UTF-8 1607 bytes

~~~c

void _ZN11flatbuffers6Parser7WarningERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (undefined8 param_1)

{
  long lVar1;
  byte local_40 [16];
  void *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (local_40,"warning: ");
  _ZN11flatbuffers6Parser7MessageERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,local_40);
  if ((local_40[0] & 1) != 0) {
    _ZdlPv(local_30);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00b0ee28 to 00c0eef7 has its CatchHandler @ 00b0ee28
                       catch() { ... } // from try @ 00b0ee28 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0ef18 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f028 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f0a8 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f17c with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f2b0 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f4b4 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f5d4 with catch @ 00b0ee28
                       catch() { ... } // from try @ 00b0f744 with catch @ 00b0ee28 */
  __stack_chk_fail();
}

~~~
