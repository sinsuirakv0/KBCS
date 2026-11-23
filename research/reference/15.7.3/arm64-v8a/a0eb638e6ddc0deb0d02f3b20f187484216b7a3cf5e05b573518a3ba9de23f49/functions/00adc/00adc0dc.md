# 00adc0dc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00adc014`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adc/00adc014.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/priority-0057.md#compare-7a297b9ce059b3756b65f87233b5e25c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adc0dc",
  "name": "FUN_00adc0dc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "475c0d95432c2d38b7ccc53a5e26b4fb8edef1c47afac613649f58b1e13873a7",
  "source_text_sha256": "475c0d95432c2d38b7ccc53a5e26b4fb8edef1c47afac613649f58b1e13873a7"
}
~~~

## 呼び出し元

- [005b726c](../005b7/005b726c.md)
- [00670de0](../00670/00670de0.md)
- [006f4518](../006f4/006f4518.md)
- [008b0960](../008b0/008b0960.md)
- [008b11a4](../008b1/008b11a4.md)

## 呼び出し先

- [005c3468](../005c3/005c3468.md)

## 疑似コード / UTF-8 549 bytes

~~~c

void FUN_00adc0dc(byte *param_1,int param_2)

{
                    /* try { // try from 00adc0e4 to 00bdc203 has its CatchHandler @ 00adc0e4
                       catch() { ... } // from try @ 00adc0e4 with catch @ 00adc0e4
                       catch() { ... } // from try @ 00adc228 with catch @ 00adc0e4 */
  *(uint *)param_1 =
       (((uint)(param_1[5] ^ param_1[2]) << 0x10 | (uint)(param_1[4] ^ param_1[3]) << 0x18 |
        (uint)(param_1[6] ^ param_1[1]) << 8) - param_2) + (uint)(param_1[7] ^ *param_1);
  FUN_005c3468();
  return;
}

~~~
