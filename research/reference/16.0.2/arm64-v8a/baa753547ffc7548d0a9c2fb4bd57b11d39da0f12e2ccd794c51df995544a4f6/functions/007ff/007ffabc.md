# 007ffabc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `007ffa64`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ff/007ffa64.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0043.md#compare-44c9bbc038e5b48758db003a86c914cd)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0049.md#compare-38219faa0bf38b6df30f64f320c2459b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007ffabc",
  "name": "FUN_007ffabc",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a13e584f36685892168231473bb38016c1d10a91b3ae9492429bde0f0371b1d5",
  "source_text_sha256": "a13e584f36685892168231473bb38016c1d10a91b3ae9492429bde0f0371b1d5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0043bb60](../0043b/0043bb60.md)
- [00c57f60](../00c57/00c57f60.md)

## 疑似コード / UTF-8 928 bytes

~~~c

undefined8 * FUN_007ffabc(long param_1)

{
  byte bVar1;
  undefined1 uVar2;
  undefined8 *puVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  
                    /* try { // try from 007ffac0 to 008ffb23 has its CatchHandler @ 007ff698 */
  puVar3 = (undefined8 *)_Znwm(0x30);
  bVar1 = *(byte *)(param_1 + 0x18);
  uVar4 = *(undefined8 *)(param_1 + 8);
  uVar2 = *(undefined1 *)(param_1 + 0x10);
  *puVar3 = &PTR_FUN_00c7e400;
  puVar3[1] = uVar4;
  *(undefined1 *)(puVar3 + 2) = uVar2;
  if ((bVar1 & 1) == 0) {
    uVar5 = *(undefined8 *)(param_1 + 0x18);
    uVar4 = *(undefined8 *)(param_1 + 0x28);
    puVar3[4] = *(undefined8 *)(param_1 + 0x20);
    puVar3[3] = uVar5;
    puVar3[5] = uVar4;
  }
  else {
    FUN_0043bb60(puVar3 + 3,*(undefined8 *)(param_1 + 0x28),*(undefined8 *)(param_1 + 0x20));
  }
                    /* try { // try from 007ffb24 to 008ffb7b has its CatchHandler @ 007ffdf8 */
  return puVar3;
}

~~~
