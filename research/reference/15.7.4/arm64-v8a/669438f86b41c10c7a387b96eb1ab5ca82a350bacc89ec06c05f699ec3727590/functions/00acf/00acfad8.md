# 00acfad8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acfa94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa94.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/inspection-0007.md#compare-7ea5f5dfa073704bf5aae6dbfcb38a54)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfad8",
  "name": "FUN_00acfad8",
  "size": 84,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "905df1cef6b353b8dfe03748090259438697144471b685adbb05bc2beb942f7b",
  "source_text_sha256": "905df1cef6b353b8dfe03748090259438697144471b685adbb05bc2beb942f7b"
}
~~~

## 呼び出し元

- [0058b674](../0058b/0058b674.md)
- [005d8f58](../005d8/005d8f58.md)
- [00617dec](../00617/00617dec.md)
- [00624a0c](../00624/00624a0c.md)
- [0062da7c](../0062d/0062da7c.md)
- [0063eb28](../0063e/0063eb28.md)
- [00680234](../00680/00680234.md)
- [00680a7c](../00680/00680a7c.md)
- [006a7120](../006a7/006a7120.md)
- [006aef04](../006ae/006aef04.md)
- [006d6d04](../006d6/006d6d04.md)
- [0072f3c8](../0072f/0072f3c8.md)
- [00730204](../00730/00730204.md)
- [00733374](../00733/00733374.md)
- [0088f740](../0088f/0088f740.md)
- [008a76c0](../008a7/008a76c0.md)
- [008b9174](../008b9/008b9174.md)
- [008be650](../008be/008be650.md)
- [0092bc08](../0092b/0092bc08.md)
- [0092d380](../0092d/0092d380.md)
- [0094f64c](../0094f/0094f64c.md)
- [0094f7d0](../0094f/0094f7d0.md)
- [00957320](../00957/00957320.md)
- [00957f9c](../00957/00957f9c.md)
- [009613bc](../00961/009613bc.md)
- [00963004](../00963/00963004.md)
- [00a26d00](../00a26/00a26d00.md)
- [00a2720c](../00a27/00a2720c.md)
- [00a28684](../00a28/00a28684.md)
- [00a28788](../00a28/00a28788.md)
- [00a7268c](../00a72/00a7268c.md)
- [00a788d0](../00a78/00a788d0.md)
- [00a823d8](../00a82/00a823d8.md)

## 呼び出し先

- [00adc094](../00adc/00adc094.md)

## 疑似コード / UTF-8 356 bytes

~~~c

int FUN_00acfad8(undefined8 param_1)

{
  uint uVar1;
  uint uVar2;
  undefined8 uVar3;
  
  uVar3 = FUN_00adc094();
  uVar1 = 50000;
  if ((uint)uVar3 < 0xc3510000) {
    uVar1 = (uint)((ulong)uVar3 >> 0x10) & 0xffff;
  }
  uVar2 = FUN_00adc094(param_1);
  uVar2 = uVar2 & 0xffff;
  if (49999 < uVar2) {
    uVar2 = 50000;
  }
  return uVar2 + uVar1;
}

~~~
