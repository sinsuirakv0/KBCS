# 00aca4cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6c538`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6c/00a6c538.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/alignment_unresolved-0014.md#compare-c17a1e3007fddd976293bc0bafc4e039)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aca4cc",
  "name": "FUN_00aca4cc",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd969811cc57415e09c371a02acbca34c8a4889f9c1fbe1f908ebec817e29c48",
  "source_text_sha256": "fd969811cc57415e09c371a02acbca34c8a4889f9c1fbe1f908ebec817e29c48"
}
~~~

## 呼び出し元

- [00789da0](../00789/00789da0.md)
- [0082fb2c](../0082f/0082fb2c.md)
- [008cb4a8](../008cb/008cb4a8.md)
- [00a79a0c](../00a79/00a79a0c.md)
- [00ac08a0](../00ac0/00ac08a0.md)

## 呼び出し先

- [00467820](../00467/00467820.md)
- [00467b20](../00467/00467b20.md)
- [00468b9c](../00468/00468b9c.md)
- [00468c20](../00468/00468c20.md)
- [00468f48](../00468/00468f48.md)
- [0046c984](../0046c/0046c984.md)
- [0046d934](../0046d/0046d934.md)
- [008514b8](../00851/008514b8.md)

## 疑似コード / UTF-8 808 bytes

~~~c

void FUN_00aca4cc(int *param_1,undefined8 param_2,int param_3)

{
  int iVar1;
  undefined8 uVar2;
  float fVar3;
  
  if ((char)param_1[0xf] != '\0') {
    uVar2 = FUN_00467820();
    FUN_00467b20(uVar2,0xff,0xff,0xff,0xff);
    FUN_00468b9c(uVar2,0x72);
    if (0 < param_1[0x18]) {
      fVar3 = (float)FUN_0046d934((float)(*param_1 * 0x1e));
      FUN_00468f48(uVar2,param_2,(int)(fVar3 * 10.0 + 24.0),param_3 + 0xff,8);
    }
    FUN_00468c20(uVar2,1);
    if (param_1[0x18] < param_1[0x17] + -1) {
      FUN_008514b8();
      iVar1 = FUN_0046c984();
      fVar3 = (float)FUN_0046d934((float)(*param_1 * 0x1e));
      FUN_00468f48(uVar2,param_2,(int)((float)(iVar1 + -0x56) + fVar3 * -10.0),param_3 + 0xff,8);
    }
    FUN_00468c20(uVar2,0);
    FUN_00468b9c(uVar2,0xff);
    return;
  }
  return;
}

~~~
