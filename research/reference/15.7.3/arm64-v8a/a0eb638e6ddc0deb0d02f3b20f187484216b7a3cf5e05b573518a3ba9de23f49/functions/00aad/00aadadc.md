# 00aadadc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aada14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aad/00aada14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/inspection-0001.md#compare-1c0f3b3445aec4986efc55c0c2daeffc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aadadc",
  "name": "FUN_00aadadc",
  "size": 160,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7a4ddff42a06a5d8b2d36b9360c6c90a6298c23fb12c3892e248e370d11004c3",
  "source_text_sha256": "7a4ddff42a06a5d8b2d36b9360c6c90a6298c23fb12c3892e248e370d11004c3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [00aab488](../00aab/00aab488.md)
- [00aabe04](../00aab/00aabe04.md)

## 疑似コード / UTF-8 726 bytes

~~~c

void FUN_00aadadc(long param_1,undefined8 param_2,int *param_3)

{
  long lVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  
  iVar2 = *param_3;
  if (iVar2 == 4) {
    lVar1 = *(long *)(param_1 + 8);
    uVar5 = *(undefined8 *)(param_1 + 0x10);
    iVar2 = *(int *)(lVar1 + 0x48) + 1;
    iVar4 = FUN_00aab488(lVar1,0xffffffff,0,0);
    iVar3 = 0;
    if (iVar4 != 0) {
      iVar3 = iVar2 / iVar4;
    }
    FUN_00aabe04(lVar1,uVar5,iVar2 - iVar3 * iVar4);
    return;
  }
  if (iVar2 == 3) {
    uVar5 = FUN_00457e1c();
    uVar6 = 0xb;
  }
  else {
    if (iVar2 != 0) {
      return;
    }
    uVar5 = FUN_00457e1c();
    uVar6 = 10;
  }
  FUN_00459efc(uVar5,uVar6,0);
  return;
}

~~~
