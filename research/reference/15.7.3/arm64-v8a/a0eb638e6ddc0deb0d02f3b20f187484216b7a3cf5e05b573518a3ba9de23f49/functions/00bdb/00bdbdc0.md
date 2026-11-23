# 00bdbdc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbd10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbd10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/high-0012.md#compare-efa36f17dc68aea92aab9485f447e005)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbdc0",
  "name": "_ZN5Botan6BigInt11encode_1363EPhmRKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f30aad7f9f003d369e7b9acce4a4c8f07f6614b0b56db9559ac566be0a446cb4",
  "source_text_sha256": "f30aad7f9f003d369e7b9acce4a4c8f07f6614b0b56db9559ac566be0a446cb4"
}
~~~

## 呼び出し元

- [004945e8](../00494/004945e8.md)
- [004947cc](../00494/004947cc.md)
- [004cd86c](../004cd/004cd86c.md)
- [00516464](../00516/00516464.md)
- [005168d8](../00516/005168d8.md)

## 呼び出し先

- [00494634](../00494/00494634.md)

## 疑似コード / UTF-8 232 bytes

~~~c

void _ZN5Botan6BigInt11encode_1363EPhmRKS0_(void)

{
                    /* try { // try from 00bdbdc0 to 00cdc01b has its CatchHandler @ 00bdbbe4 */
  (*(code *)PTR__ZN5Botan6BigInt11encode_1363EPhmRKS0__00c1c770)();
  return;
}

~~~
