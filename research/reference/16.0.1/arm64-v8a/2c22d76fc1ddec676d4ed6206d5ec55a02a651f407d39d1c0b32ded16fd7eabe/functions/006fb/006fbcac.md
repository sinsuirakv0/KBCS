# 006fbcac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `006fbc6c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006fb/006fbc6c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0033.md#compare-32967e116013e26acd9b20dc906c7762)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0034.md#compare-5b0dd6ecb2dfffe2c62ebefe8bf91742)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fbcac",
  "name": "FUN_006fbcac",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "050b265eda0f381fe7403dcf9bc204d76ddc9893d9032ed43f53900f667bb255",
  "source_text_sha256": "050b265eda0f381fe7403dcf9bc204d76ddc9893d9032ed43f53900f667bb255"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [006b2424](../006b2/006b2424.md)
- [006ea588](../006ea/006ea588.md)
- [006f0500](../006f0/006f0500.md)
- [006fb074](../006fb/006fb074.md)
- [008514f8](../00851/008514f8.md)
- [008b9178](../008b9/008b9178.md)
- [00a83260](../00a83/00a83260.md)

## 疑似コード / UTF-8 1199 bytes

~~~c

void FUN_006fbcac(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  undefined8 uVar1;
  long lVar2;
  undefined1 *puVar3;
  undefined8 uVar4;
  undefined8 *puVar5;
  
  puVar3 = *(undefined1 **)(param_1 + 8);
  if ((*param_3 == 2) && (*param_4 != -1)) {
    uVar4 = *param_2;
    uVar1 = FUN_0047acf4();
    FUN_0047cdd4(uVar1,0xb,0);
    FUN_008b9178(uVar4);
    return;
  }
  if ((*param_3 == 5) && (*param_4 == 0)) {
    *puVar3 = 0;
    puVar5 = (undefined8 *)(puVar3 + 0x28);
    FUN_006fb074(puVar3 + 0x20,*puVar5);
    *(undefined8 **)(puVar3 + 0x20) = puVar5;
    *(undefined8 *)(puVar3 + 0x30) = 0;
    *puVar5 = 0;
    lVar2 = FUN_008514f8();
    *(undefined4 *)((long)&fde_table_entry_00332070.data_loc + lVar2) = 0;
    lVar2 = FUN_008514f8();
    *(undefined4 *)((long)&fde_table_entry_00332098.initial_loc + lVar2) = 0;
    lVar2 = FUN_008514f8();
    FUN_00a83260(lVar2 + 0x3078,0x14);
    lVar2 = FUN_008514f8();
    FUN_006b2424(lVar2 + 0x42ef60);
    lVar2 = FUN_008514f8();
    FUN_006f0500(lVar2 + 0x42ef90,*(undefined4 *)(puVar3 + 4),*(undefined4 *)(puVar3 + 0x14));
    lVar2 = FUN_008514f8();
    FUN_006ea588(lVar2 + 0x42ef90,1);
    return;
  }
  return;
}

~~~
