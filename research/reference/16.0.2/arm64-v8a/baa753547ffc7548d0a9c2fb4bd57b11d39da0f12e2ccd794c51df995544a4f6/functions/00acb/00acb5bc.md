# 00acb5bc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acb54c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acb54c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0065.md#compare-0a59bb60fec1e93a2aefcc79a56ac106)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0077.md#compare-b20d18dbf84886bea94d7ef8c72043e0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acb5bc",
  "name": "FUN_00acb5bc",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fd0e0a7b69894b5ecb65515f7850890b1551c75360e91d754865fd6689846a07",
  "source_text_sha256": "fd0e0a7b69894b5ecb65515f7850890b1551c75360e91d754865fd6689846a07"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047ad34](../0047a/0047ad34.md)
- [0047ce14](../0047c/0047ce14.md)
- [0047d1fc](../0047d/0047d1fc.md)
- [00851550](../00851/00851550.md)
- [00b3bf30](../00b3b/00b3bf30.md)

## 疑似コード / UTF-8 1676 bytes

~~~c

void FUN_00acb5bc(undefined8 param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  undefined8 uVar4;
  
  iVar1 = *param_3;
  if (iVar1 != 4) {
    if (iVar1 == 3) {
      uVar2 = FUN_0047ad34();
      uVar4 = 0xb;
    }
    else {
      if (iVar1 != 0) {
        return;
      }
      uVar2 = FUN_0047ad34();
      uVar4 = 10;
    }
    FUN_0047ce14(uVar2,uVar4,0);
    return;
  }
  lVar3 = FUN_00851550();
  iVar1 = *(int *)(lVar3 + 0x4a818);
  lVar3 = FUN_00851550();
  if (iVar1 != 0) {
    iVar1 = FUN_00b3bf30(lVar3 + 0xc400);
    lVar3 = FUN_00851550();
    if (iVar1 < 900000) {
      *(undefined4 *)(lVar3 + 0x3478) = 0;
      lVar3 = FUN_00851550();
      *(undefined1 *)(lVar3 + 0x3480) = 1;
    }
    else {
      *(undefined1 *)((long)&fde_table_entry_00335f18.initial_loc + lVar3 + 2) = 1;
      lVar3 = FUN_00851550();
      *(undefined4 *)((long)&fde_table_entry_00335f30.data_loc + lVar3) = 10000;
    }
    return;
  }
  *(undefined4 *)(lVar3 + 0x4a818) = 1;
  lVar3 = FUN_00851550();
  *(undefined1 *)((long)&fde_table_entry_00336f50.data_loc + lVar3) = 1;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f58.initial_loc + lVar3) = 0;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f58.data_loc + lVar3) = 0;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f60.initial_loc + lVar3) = 0;
  FUN_00851550();
  lVar3 = FUN_00851550();
  *(undefined4 *)((long)&fde_table_entry_00336f60.data_loc + lVar3) = 0;
  FUN_00851550();
  uVar2 = FUN_0047ad34();
  FUN_0047d1fc(uVar2,0x32);
  return;
}

~~~
