# 00b5deec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5dac4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5d/00b5dac4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0037.md#compare-9c85b1e86f33d973589b272c48d06d3f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0038.md#compare-7ad541359170d1da9bc586cc24894822)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5deec",
  "name": "_ZN8firebase4Path11GetRelativeERKS0_S2_PS0_",
  "size": 184,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e9bfd83e72f7c2defd46b4702b7e7b3ad1c4e32d36160edcdc54aaeddb952065",
  "source_text_sha256": "e9bfd83e72f7c2defd46b4702b7e7b3ad1c4e32d36160edcdc54aaeddb952065"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5b0b0](../00c5b/00c5b0b0.md)
- [00c5bbe0](../00c5b/00c5bbe0.md)

## 疑似コード / UTF-8 1124 bytes

~~~c

void _ZN8firebase4Path11GetRelativeERKS0_S2_PS0_
               (undefined8 param_1,undefined8 param_2,byte *param_3)

{
  ulong uVar1;
  long lVar2;
  void *pvVar3;
  undefined8 uVar4;
  byte local_58 [8];
  ulong local_50;
  void *local_48;
  char local_40;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  _ZN8firebase4Path11GetRelativeERKS0_S2_(local_58);
  if (local_40 == '\0') {
    uVar4 = 0;
    goto LAB_00b5df7c;
  }
  if (local_58 == param_3) {
LAB_00b5df5c:
    if ((local_58[0] & 1) != 0) {
      _ZdlPv(local_48);
    }
    local_40 = '\0';
  }
  else {
    uVar1 = (ulong)(local_58[0] >> 1);
    pvVar3 = (void *)((ulong)local_58 | 1);
    if ((local_58[0] & 1) != 0) {
      uVar1 = local_50;
      pvVar3 = local_48;
    }
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
              (param_3,pvVar3,uVar1);
    if (local_40 != '\0') goto LAB_00b5df5c;
  }
  uVar4 = 1;
LAB_00b5df7c:
  if (*(long *)(lVar2 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar4);
  }
  return;
}

~~~
