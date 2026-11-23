# 00b2bbcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2b7a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b7a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/inspection-0037.md#compare-387d9c5267477bc66d5039aca8d08a23)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0038.md#compare-d14324d9d9d8ea65f9eb49a9c0b601b6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2bbcc",
  "name": "FUN_00b2bbcc",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d8c41251ed4f0e61202543efc59a7f011f3f41e739595dccc5e1bb5f529c7d1d",
  "source_text_sha256": "d8c41251ed4f0e61202543efc59a7f011f3f41e739595dccc5e1bb5f529c7d1d"
}
~~~

## 呼び出し元

- [0043b5a8](../0043b/0043b5a8.md)
- [0043b658](../0043b/0043b658.md)

## 呼び出し先

- [0046caa4](../0046c/0046caa4.md)
- [0046cabc](../0046c/0046cabc.md)
- [0046cac8](../0046c/0046cac8.md)
- [008514f8](../00851/008514f8.md)

## 疑似コード / UTF-8 679 bytes

~~~c

void FUN_00b2bbcc(undefined8 param_1,ulong param_2)

{
  long *plVar1;
  undefined4 uVar2;
  uint uVar3;
  long lVar4;
  
  uVar2 = FUN_008514f8();
  if ((param_2 & 1) == 0) {
    FUN_0046caa4(uVar2,0);
    lVar4 = 0x18;
  }
  else {
    uVar3 = FUN_0046cabc();
    if ((uVar3 & 1) != 0) {
      uVar2 = FUN_008514f8();
      FUN_0046cac8(uVar2,0);
    }
    uVar2 = FUN_008514f8();
    FUN_0046caa4(uVar2,1);
    lVar4 = 0x10;
  }
  plVar1 = (long *)FUN_008514f8();
                    /* WARNING: Could not recover jumptable at 0x00b2bc2c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + lVar4))();
  return;
}

~~~
