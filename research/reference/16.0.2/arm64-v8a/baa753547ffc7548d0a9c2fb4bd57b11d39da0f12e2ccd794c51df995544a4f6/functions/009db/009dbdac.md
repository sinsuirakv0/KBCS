# 009dbdac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `009dbd58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009db/009dbd58.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/inspection-0031.md#compare-d968166fa8dc8ed3c10636ada09f36bb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0026.md#compare-469e8f4e90d715c1cc98a5424aa2fe1f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009dbdac",
  "name": "FUN_009dbdac",
  "size": 120,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "431db0eb2e66e9387760b70dbfd65e95d0e3e80412425fee702ae8b9984a4535",
  "source_text_sha256": "431db0eb2e66e9387760b70dbfd65e95d0e3e80412425fee702ae8b9984a4535"
}
~~~

## 呼び出し元

- [00707f38](../00707/00707f38.md)

## 呼び出し先

- [0046bd94](../0046b/0046bd94.md)
- [004700f4](../00470/004700f4.md)

## 疑似コード / UTF-8 643 bytes

~~~c

void FUN_009dbdac(undefined8 param_1,long param_2,undefined8 param_3,undefined4 param_4,
                 undefined4 param_5,undefined4 param_6,int param_7)

{
  long lVar1;
  long lVar2;
  
  lVar1 = 0x1480;
  if (param_7 != 0) {
    lVar1 = 0x1aa0;
  }
  lVar2 = 0x1528;
  if (param_7 != 0) {
    lVar2 = 0x1b48;
  }
  FUN_004700f4(param_2 + lVar1,param_2 + lVar2,param_6,0);
                    /* try { // try from 009dbe04 to 00adbe0f has its CatchHandler @ 009dc118 */
                    /* try { // try from 009dbe10 to 00adbe17 has its CatchHandler @ 009dc110 */
  FUN_0046bd94(param_3,param_2 + lVar1,param_4,param_5);
  return;
}

~~~
