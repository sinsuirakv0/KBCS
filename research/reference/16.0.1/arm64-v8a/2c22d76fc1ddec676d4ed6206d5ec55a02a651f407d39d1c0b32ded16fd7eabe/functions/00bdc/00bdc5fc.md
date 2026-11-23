# 00bdc5fc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdc1d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc1d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0085.md#compare-dcb19dcd85359e1b5b817709b5af940a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0095.md#compare-f88f6c6cd42d16f76ce390092d4b2bb5)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdc5fc",
  "name": "_ZN8firebase4auth10AuthResultC2ERKS1_",
  "size": 92,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c84ead858a85688626a5dca834c5dbd377a1758b8a81b627f3eda33861fb56a6",
  "source_text_sha256": "c84ead858a85688626a5dca834c5dbd377a1758b8a81b627f3eda33861fb56a6"
}
~~~

## 呼び出し元

- [00c5ddf0](../00c5d/00c5ddf0.md)

## 呼び出し先

- [00c5aa40](../00c5a/00c5aa40.md)
- [00c5dd60](../00c5d/00c5dd60.md)
- [00c5de20](../00c5d/00c5de20.md)

## 疑似コード / UTF-8 680 bytes

~~~c

void _ZN8firebase4auth10AuthResultC2ERKS1_(long param_1,long param_2)

{
  _ZN8firebase4auth18AdditionalUserInfoC2ERKS1_();
  *(undefined8 *)(param_1 + 0x70) = 0;
  *(undefined4 *)(param_1 + 0x78) = 0;
  *(undefined8 *)(param_1 + 0x80) = 0;
  *(undefined8 *)(param_1 + 0x88) = 0;
  *(undefined8 *)(param_1 + 0x90) = 0;
  _ZN8firebase4auth10CredentialaSERKS1_((undefined8 *)(param_1 + 0x70),param_2 + 0x70);
                    /* try { // try from 00bdc640 to 00cdc64b has its CatchHandler @ 00bdee78 */
  _ZN8firebase4auth4UserC1ERKS1_(param_1 + 0x98,param_2 + 0x98);
                    /* try { // try from 00bdc650 to 00cdc68f has its CatchHandler @ 00bdeecc */
  return;
}

~~~
