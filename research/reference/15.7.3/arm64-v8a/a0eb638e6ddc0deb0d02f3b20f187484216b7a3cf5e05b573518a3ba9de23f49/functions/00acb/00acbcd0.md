# 00acbcd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acbc08`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00acb/00acbc08.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/inspection-0001.md#compare-97f074ca5982662c546c823a8415ff7f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbcd0",
  "name": "FUN_00acbcd0",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9fb3503de6ea8e6319996223104deb850f8e32c1948d81fb86b005babff31e77",
  "source_text_sha256": "9fb3503de6ea8e6319996223104deb850f8e32c1948d81fb86b005babff31e77"
}
~~~

## 呼び出し元

- [00418a68](../00418/00418a68.md)
- [00418b18](../00418/00418b18.md)

## 呼び出し先

- [00449bcc](../00449/00449bcc.md)
- [00449be4](../00449/00449be4.md)
- [00449bf0](../00449/00449bf0.md)
- [0081f580](../0081f/0081f580.md)

## 疑似コード / UTF-8 679 bytes

~~~c

void FUN_00acbcd0(undefined8 param_1,ulong param_2)

{
  long *plVar1;
  undefined4 uVar2;
  uint uVar3;
  long lVar4;
  
  uVar2 = FUN_0081f580();
  if ((param_2 & 1) == 0) {
    FUN_00449bcc(uVar2,0);
    lVar4 = 0x18;
  }
  else {
    uVar3 = FUN_00449be4();
    if ((uVar3 & 1) != 0) {
      uVar2 = FUN_0081f580();
      FUN_00449bf0(uVar2,0);
    }
    uVar2 = FUN_0081f580();
    FUN_00449bcc(uVar2,1);
    lVar4 = 0x10;
  }
  plVar1 = (long *)FUN_0081f580();
                    /* WARNING: Could not recover jumptable at 0x00acbd30. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar1 + lVar4))();
  return;
}

~~~
