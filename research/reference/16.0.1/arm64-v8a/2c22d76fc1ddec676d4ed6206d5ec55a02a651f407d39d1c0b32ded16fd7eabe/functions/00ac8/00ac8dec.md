# 00ac8dec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ac8bf0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8bf0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/no_difference_in_scope-0012.md#compare-d769317c8dda0cc632e2de6bf4d76e23)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0069.md#compare-392b451976fba97a6851b6d97dc86f59)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac8dec",
  "name": "FUN_00ac8dec",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "30f8019ac84cc0bee76d0f4deaaaf02da004582d94e1f1944f6f7ca1b591c81c",
  "source_text_sha256": "30f8019ac84cc0bee76d0f4deaaaf02da004582d94e1f1944f6f7ca1b591c81c"
}
~~~

## 呼び出し元

- [00789de0](../00789/00789de0.md)
- [0082ac68](../0082a/0082ac68.md)
- [008c87f8](../008c8/008c87f8.md)
- [008c89fc](../008c8/008c89fc.md)
- [008c990c](../008c9/008c990c.md)
- [008c9da8](../008c9/008c9da8.md)
- [00a75dac](../00a75/00a75dac.md)
- [00a79c04](../00a79/00a79c04.md)
- [00ac0a9c](../00ac0/00ac0a9c.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 184 bytes

~~~c

undefined4 FUN_00ac8dec(long param_1)

{
                    /* try { // try from 00ac8df0 to 00bc8ecb has its CatchHandler @ 00ac8bcc */
  return *(undefined4 *)(param_1 + 0x68);
}

~~~
