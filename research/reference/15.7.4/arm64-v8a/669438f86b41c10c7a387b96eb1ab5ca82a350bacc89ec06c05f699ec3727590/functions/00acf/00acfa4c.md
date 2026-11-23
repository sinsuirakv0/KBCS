# 00acfa4c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acfa08`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acfa08.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/priority-0060.md#compare-1292b421a0502cc6c3359b8eed828515)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfa4c",
  "name": "FUN_00acfa4c",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4c43125907101778fd059897f3742812b91a35f18aebbfa39270cecc62c27b62",
  "source_text_sha256": "4c43125907101778fd059897f3742812b91a35f18aebbfa39270cecc62c27b62"
}
~~~

## 呼び出し元

- [006e34b0](../006e3/006e34b0.md)
- [0072f020](../0072f/0072f020.md)
- [0092bc08](../0092b/0092bc08.md)
- [0092d380](../0092d/0092d380.md)
- [009a9ce0](../009a9/009a9ce0.md)
- [00add818](../00add/00add818.md)

## 呼び出し先

- [00adc060](../00adc/00adc060.md)
- [00adc094](../00adc/00adc094.md)

## 疑似コード / UTF-8 627 bytes

~~~c

void FUN_00acfa4c(undefined8 param_1,int param_2)

{
  uint uVar1;
  uint uVar2;
  uint uVar3;
  undefined8 uVar4;
  
  uVar4 = FUN_00adc094();
  uVar1 = 50000;
  if ((uint)uVar4 < 0xc3510000) {
    uVar1 = (uint)((ulong)uVar4 >> 0x10) & 0xffff;
  }
  uVar3 = FUN_00adc094(param_1);
  uVar3 = uVar3 & 0xffff;
  if (49999 < uVar3) {
    uVar3 = 50000;
  }
  uVar2 = 0xc3500000;
  if (uVar1 < 0xc351) {
    uVar2 = uVar1 << 0x10;
  }
  uVar1 = uVar3 + param_2 & ((int)(uVar3 + param_2) >> 0x1f ^ 0xffffffffU);
  if (49999 < uVar1) {
    uVar1 = 50000;
  }
  FUN_00adc060(param_1,uVar1 | uVar2);
  DAT_00c23fb4 = 1;
  return;
}

~~~
