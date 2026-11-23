# 006fffbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `006fff7c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006fff7c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0033.md#compare-cf097cb2521d21d804da4000b9e231a3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0034.md#compare-b04cd619e27dc70563238bbc0e8c4822)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fffbc",
  "name": "FUN_006fffbc",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4b156299903a147c7d08c540d18f5ba2091417b353009a2789221d7379466961",
  "source_text_sha256": "4b156299903a147c7d08c540d18f5ba2091417b353009a2789221d7379466961"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00470840](../00470/00470840.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c58000](../00c58/00c58000.md)

## 疑似コード / UTF-8 759 bytes

~~~c

undefined8 * FUN_006fffbc(long param_1)

{
  undefined8 uVar1;
  void *__src;
  size_t __n;
  undefined8 *puVar2;
  void *__dest;
  long lVar3;
  
  puVar2 = (undefined8 *)_Znwm(0x28);
  uVar1 = *(undefined8 *)(param_1 + 8);
  __src = *(void **)(param_1 + 0x10);
  puVar2[3] = 0;
  puVar2[4] = 0;
  *puVar2 = &PTR_FUN_00c77598;
  puVar2[1] = uVar1;
  lVar3 = *(long *)(param_1 + 0x18);
  puVar2[2] = 0;
  __n = lVar3 - (long)__src;
  if (__n != 0) {
    if ((long)__n < 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00470840(puVar2 + 2);
    }
    __dest = (void *)_Znwm(__n);
    puVar2[2] = __dest;
    puVar2[4] = (long)__dest + __n;
    memcpy(__dest,__src,__n);
    puVar2[3] = (long)__dest + __n;
  }
  return puVar2;
}

~~~
