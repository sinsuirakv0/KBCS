# 00b7dafc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b7d6d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b7d/00b7d6d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/alignment_unresolved-0009.md#compare-c309d669ce7d94f761482477d509b16c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0085.md#compare-cdf76a072035d17934a8800cee38ed1f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7dafc",
  "name": "_ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementIsEEvtT_",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "630dfb6656e7f902d2088276921fc3222257c96c911a8dffcd966fd042305e76",
  "source_text_sha256": "630dfb6656e7f902d2088276921fc3222257c96c911a8dffcd966fd042305e76"
}
~~~

## 呼び出し元

- [00c5c1f0](../00c5c/00c5c1f0.md)

## 呼び出し先

- [00c5c1a0](../00c5c/00c5c1a0.md)

## 疑似コード / UTF-8 1915 bytes

~~~c

void _ZN11flatbuffers21FlatBufferBuilderImplILb0EE10AddElementIsEEvtT_
               (long param_1,uint param_2,undefined2 param_3)

{
  int iVar1;
  uint uVar2;
  ulong *puVar3;
  long lVar4;
  ulong uVar5;
  
                    /* catch() { ... } // from try @ 00b7d28c with catch @ 00b7db0c */
                    /* catch() { ... } // from try @ 00b7d2bc with catch @ 00b7db14 */
  if (*(ulong *)(param_1 + 0x68) < 2) {
    *(undefined8 *)(param_1 + 0x68) = 2;
  }
  uVar2 = *(uint *)(param_1 + 0x30);
  uVar5 = (ulong)uVar2 & 1;
  if ((int)uVar5 != 0) {
    lVar4 = *(long *)(param_1 + 0x40);
    if ((uint)((int)lVar4 - *(int *)(param_1 + 0x48)) < uVar5) {
      _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar5);
      lVar4 = *(long *)(param_1 + 0x40);
      uVar2 = *(uint *)(param_1 + 0x30);
    }
    *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar4 - uVar5);
    *(uint *)(param_1 + 0x30) = uVar2 + (int)uVar5;
    *(undefined1 *)(lVar4 - uVar5) = 0;
  }
  lVar4 = *(long *)(param_1 + 0x40);
  puVar3 = *(ulong **)(param_1 + 0x48);
  if (((int)lVar4 - (int)puVar3 & 0xfffffffeU) == 0) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,2);
    lVar4 = *(long *)(param_1 + 0x40);
    puVar3 = *(ulong **)(param_1 + 0x48);
  }
  *(long *)(param_1 + 0x40) = lVar4 + -2;
  iVar1 = *(int *)(param_1 + 0x30) + 2;
  *(int *)(param_1 + 0x30) = iVar1;
  *(undefined2 *)(lVar4 + -2) = param_3;
  if (((int)(lVar4 + -2) - (int)puVar3 & 0xfffffff8U) == 0) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,8);
    puVar3 = *(ulong **)(param_1 + 0x48);
  }
  *puVar3 = CONCAT44(param_2,iVar1) & 0xffffffffffff;
  *(long *)(param_1 + 0x48) = *(long *)(param_1 + 0x48) + 8;
  *(int *)(param_1 + 0x50) = *(int *)(param_1 + 0x50) + 1;
  if ((uint)*(ushort *)(param_1 + 0x54) < (param_2 & 0xffff)) {
    *(short *)(param_1 + 0x54) = (short)param_2;
  }
  return;
}

~~~
