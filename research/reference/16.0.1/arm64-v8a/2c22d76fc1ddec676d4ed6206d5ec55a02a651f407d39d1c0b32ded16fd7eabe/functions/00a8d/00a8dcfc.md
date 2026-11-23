# 00a8dcfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a8db04`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a8d/00a8db04.md) · 移動量 `+0x1f8`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0062.md#compare-5d3920838802e21d982ea20b936868ad)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0066.md#compare-3857806d850c411eca34349379916af6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a8dcfc",
  "name": "FUN_00a8dcfc",
  "size": 188,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4ea9204233f5bd8f1ee5d25803793bdafb647bdb03c885f85ed56c11ce30e602",
  "source_text_sha256": "4ea9204233f5bd8f1ee5d25803793bdafb647bdb03c885f85ed56c11ce30e602"
}
~~~

## 呼び出し元

- [00851a0c](../00851/00851a0c.md)
- [00a8a418](../00a8a/00a8a418.md)

## 呼び出し先

- [007683d8](../00768/007683d8.md)
- [00a91af8](../00a91/00a91af8.md)
- [00a91e10](../00a91/00a91e10.md)
- [00c57e30](../00c57/00c57e30.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)

## 疑似コード / UTF-8 677 bytes

~~~c

void FUN_00a8dcfc(long param_1)

{
  int iVar1;
  ulong uVar2;
  
  uVar2 = FUN_007683d8();
  if ((uVar2 & 1) != 0) {
    *(undefined1 *)(param_1 + 0x2030) = 0;
    if (((DAT_00ca4f38 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_00ca4f38), iVar1 != 0)) {
      DAT_00ca4f08 = 0;
      DAT_00ca4f00 = &DAT_00ca4f08;
      DAT_00ca4f28 = 0;
      DAT_00ca4f30 = 0;
      DAT_00ca4f20 = 0;
      DAT_00ca4f10 = 0;
      DAT_00ca4f18 = &DAT_00ca4f20;
      __cxa_atexit(FUN_0047edb4,&DAT_00ca4f00,&PTR_LOOP_00c62f90);
      __cxa_guard_release(&DAT_00ca4f38);
    }
    FUN_00a91af8(param_1,&DAT_00ca4f00);
    FUN_00a91e10(param_1,&DAT_00ca4f00);
    return;
  }
  return;
}

~~~
