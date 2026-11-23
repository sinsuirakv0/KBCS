# 00afa0ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00af9cc4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00af9/00af9cc4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0066.md#compare-5a872a3cf51bd256868e2e55c7889ea6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0072.md#compare-e224c3a64cc8b932c1fb63785383bdb1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afa0ec",
  "name": "FUN_00afa0ec",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "88e97c4bd94636d186d2590cb8a6b4af33041485ae369ae8bdd16dca8a10dc4a",
  "source_text_sha256": "88e97c4bd94636d186d2590cb8a6b4af33041485ae369ae8bdd16dca8a10dc4a"
}
~~~

## 呼び出し元

- [007119f0](../00711/007119f0.md)

## 呼び出し先

- [005e7420](../005e7/005e7420.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 1107 bytes

~~~c

undefined4 FUN_00afa0ec(int param_1,int param_2)

{
  undefined4 uVar1;
  long lVar2;
  ulong uVar3;
  
  lVar2 = FUN_008514f8();
  uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
  if ((uVar3 & 1) == 0) {
    uVar1 = 0;
  }
  else {
    lVar2 = FUN_008514f8();
                    /* try { // try from 00afa138 to 00bfa15b has its CatchHandler @ 00afa9d0 */
    uVar3 = FUN_005e7420(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
                    /* try { // try from 00afa164 to 00bfa16b has its CatchHandler @ 00afaab0 */
    if ((((uVar3 & 1) == 0) ||
        (lVar2 = FUN_008514f8(),
        *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bdc) == 0)) ||
       (lVar2 = FUN_008514f8(),
       *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c60) != 0)) {
      lVar2 = FUN_008514f8();
      uVar1 = *(undefined4 *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84c60);
    }
    else {
      uVar1 = 0x46;
                    /* try { // try from 00afa1c8 to 00bfa1cf has its CatchHandler @ 00afa9cc */
    }
  }
  return uVar1;
}

~~~
