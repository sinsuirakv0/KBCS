# 00bfacb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfa88c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa88c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0086.md#compare-be93438562e67bc96becebe03ab9fdd6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0096.md#compare-47a8a3b4d645834483eb3d70d4e4c034)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfacb4",
  "name": "_ZNSt6__ndk113random_deviceC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "36b58cce38a11c2386bd499de5f82c52de0ab6a0f5711b84de4cdde2d82d0a41",
  "source_text_sha256": "36b58cce38a11c2386bd499de5f82c52de0ab6a0f5711b84de4cdde2d82d0a41"
}
~~~

## 呼び出し元

- [00c583a0](../00c58/00c583a0.md)

## 呼び出し先

- [00c580b0](../00c58/00c580b0.md)
- [00c580c0](../00c58/00c580c0.md)
- [00c58120](../00c58/00c58120.md)
- [00c5d610](../00c5d/00c5d610.md)

## 関連文字列（未確認候補）

~~~text
"random_device failed to open "
~~~

## 疑似コード / UTF-8 877 bytes

~~~c

void _ZNSt6__ndk113random_deviceC2ERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEE
               (int *param_1,byte *param_2)

{
  undefined4 uVar1;
  int iVar2;
  undefined4 *puVar3;
  byte *__file;
  byte local_38;
  undefined1 auStack_37 [15];
  undefined1 *local_28;
  
  __file = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    __file = param_2 + 1;
  }
  iVar2 = open((char *)__file,0);
  *param_1 = iVar2;
  if (-1 < iVar2) {
    return;
  }
  puVar3 = (undefined4 *)__errno();
  uVar1 = *puVar3;
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (&local_38,"random_device failed to open ",param_2);
  if ((local_38 & 1) == 0) {
    local_28 = auStack_37;
  }
                    /* WARNING: Subroutine does not return */
  _ZNSt6__ndk120__throw_system_errorEiPKc(uVar1,local_28);
}

~~~
