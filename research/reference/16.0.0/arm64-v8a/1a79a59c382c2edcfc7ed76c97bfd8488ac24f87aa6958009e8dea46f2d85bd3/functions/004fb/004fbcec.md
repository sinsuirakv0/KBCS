# 004fbcec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `004d8e54`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/004d8/004d8e54.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0010.md#compare-fb13e921795aba31ca8f8cd6a3f5999f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
