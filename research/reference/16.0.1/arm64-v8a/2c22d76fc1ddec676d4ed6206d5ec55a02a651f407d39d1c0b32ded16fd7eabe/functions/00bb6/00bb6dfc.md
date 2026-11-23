# 00bb6dfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb69d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb6/00bb69d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0038.md#compare-58f06c77bffdb782946978a8e8e88ed9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0039.md#compare-a08d57c442b6a77b0ee2a91754e0e4bd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb6dfc",
  "name": "_ZN8firebase9messaging20PollableListenerImplD2Ev",
  "size": 192,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f96052cd26fa01dc0141841a55a15085ff204f83b468cec7303ea8c800b32d88",
  "source_text_sha256": "f96052cd26fa01dc0141841a55a15085ff204f83b468cec7303ea8c800b32d88"
}
~~~

## 呼び出し元

- [00c5d380](../00c5d/00c5d380.md)

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5aaa0](../00c5a/00c5aaa0.md)
- [00c5d460](../00c5d/00c5d460.md)

## 疑似コード / UTF-8 1349 bytes

~~~c

void _ZN8firebase9messaging20PollableListenerImplD2Ev(long param_1)

{
  undefined8 *puVar1;
  byte bVar2;
  long lVar3;
  void *__ptr;
  undefined8 *puVar4;
  undefined8 *puVar5;
  
  _ZNSt6__ndk112__deque_baseIN8firebase9messaging7MessageENS_9allocatorIS3_EEE5clearEv
            ((undefined8 *)(param_1 + 0x70));
  puVar1 = *(undefined8 **)(param_1 + 0x80);
  puVar4 = *(undefined8 **)(param_1 + 0x78);
  if (*(undefined8 **)(param_1 + 0x78) != puVar1) {
    do {
      puVar5 = puVar4 + 1;
      _ZdlPv((void *)*puVar4);
      puVar4 = puVar5;
    } while (puVar1 != puVar5);
    lVar3 = *(long *)(param_1 + 0x80) - *(long *)(param_1 + 0x78);
    if (lVar3 != 0) {
      *(ulong *)(param_1 + 0x80) =
           *(long *)(param_1 + 0x80) + (lVar3 - 8U >> 3 ^ 0xffffffffffffffff) * 8;
    }
  }
  __ptr = *(void **)(param_1 + 0x70);
  if (__ptr != (void *)0x0) {
    _ZdlPv(__ptr);
  }
  if ((*(byte *)(param_1 + 0x58) & 1) == 0) {
    bVar2 = *(byte *)(param_1 + 0x40);
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x68));
    bVar2 = *(byte *)(param_1 + 0x40);
  }
  if ((bVar2 & 1) == 0) {
    bVar2 = *(byte *)(param_1 + 0x28);
  }
  else {
    _ZdlPv(*(void **)(param_1 + 0x50));
    bVar2 = *(byte *)(param_1 + 0x28);
  }
  if ((bVar2 & 1) != 0) {
    _ZdlPv(*(void **)(param_1 + 0x38));
  }
  _ZN8firebase5MutexD1Ev(param_1);
  return;
}

~~~
