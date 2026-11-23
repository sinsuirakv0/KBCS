# 00bcfcd8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcf8b0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf8b0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0039.md#compare-1e713da92de405a214a90e18205d0aa0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0040.md#compare-67be0d56395de774b626285b05aa89aa)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfcd8",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv",
  "size": 108,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95902d6af978300ab699da4482c5b836442deb89fcc13f69258ba4b59a1cd8bd",
  "source_text_sha256": "95902d6af978300ab699da4482c5b836442deb89fcc13f69258ba4b59a1cd8bd"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5a9f0](../00c5a/00c5a9f0.md)
- [00c5aa50](../00c5a/00c5aa50.md)
- [00c5be20](../00c5b/00c5be20.md)

## 疑似コード / UTF-8 739 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl7DeleteTINS_4auth10AuthResultEEEvPv(byte *param_1)

{
  if (param_1 != (byte *)0x0) {
    _ZN8firebase4auth4UserD2Ev(param_1 + 0x98);
    _ZN8firebase4auth10CredentialD2Ev(param_1 + 0x70);
    _ZN8firebase4auth10CredentialD2Ev(param_1 + 0x48);
    _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
              (param_1 + 0x30,*(undefined8 *)(param_1 + 0x38));
    if ((param_1[0x18] & 1) != 0) {
      _ZdlPv(*(void **)(param_1 + 0x28));
    }
    if ((*param_1 & 1) != 0) {
      _ZdlPv(*(void **)(param_1 + 0x10));
    }
    _ZdlPv(param_1);
    return;
  }
  return;
}

~~~
