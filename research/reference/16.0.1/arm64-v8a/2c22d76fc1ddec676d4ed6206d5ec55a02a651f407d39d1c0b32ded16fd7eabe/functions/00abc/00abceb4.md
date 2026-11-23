# 00abceb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00abccb8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abc/00abccb8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0063.md#compare-ac067c6849500c36bcde454e8bb2520d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/inspection-0035.md#compare-e8959fa294605869a512856e74de8959)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abceb4",
  "name": "FUN_00abceb4",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53c07d8d6994f238979e2160b6c4fb7ba453d513b55f1713c7bc305ee1223df3",
  "source_text_sha256": "53c07d8d6994f238979e2160b6c4fb7ba453d513b55f1713c7bc305ee1223df3"
}
~~~

## 呼び出し元

- [00abc8d8](../00abc/00abc8d8.md)

## 呼び出し先

- [00800378](../00800/00800378.md)
- [0080062c](../00800/0080062c.md)
- [008056ec](../00805/008056ec.md)
- [008514f8](../00851/008514f8.md)
- [00a65dec](../00a65/00a65dec.md)

## 疑似コード / UTF-8 1548 bytes

~~~c

bool FUN_00abceb4(long param_1,undefined4 param_2)

{
  byte *pbVar1;
  uint uVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  long lVar8;
  bool bVar9;
  long lVar10;
  
  iVar3 = FUN_00800378(param_2);
  iVar4 = FUN_0080062c(param_2);
  iVar5 = *(int *)(param_1 + 0x68);
  if (iVar5 == -1) {
    iVar5 = FUN_008056ec(iVar3,iVar4);
    iVar5 = iVar5 + -1;
  }
  iVar5 = FUN_00a65dec(iVar3,iVar4,iVar5,*(undefined4 *)(param_1 + 0x70),0);
  if (iVar5 == 0) {
LAB_00abcf5c:
    bVar9 = false;
  }
  else {
    if (*(int *)(param_1 + 0x6c) == -1) {
      return true;
    }
    if (*(int *)(param_1 + 0x68) != -1) {
      return true;
    }
    if (iVar3 == -7) {
      iVar4 = iVar4 + 7;
    }
    else if (iVar3 != -2) {
      if (iVar3 != -3) goto LAB_00abcf5c;
      iVar4 = iVar4 + 4;
    }
    FUN_008514f8();
    lVar10 = 0x30;
    lVar8 = (long)iVar4 * 200 + 0xd443;
    do {
      lVar6 = FUN_008514f8();
      lVar7 = lVar6 + (long)iVar4 * 200;
      pbVar1 = (byte *)(lVar6 + lVar8);
      uVar2 = (uint)(*(byte *)(lVar7 + 0xd506) ^ pbVar1[-1]) << 0x10 |
              (uint)(*(byte *)(lVar7 + 0xd507) ^ *pbVar1) << 0x18 |
              (uint)(*(byte *)(lVar7 + 0xd505) ^ pbVar1[-2]) << 8 |
              (uint)(*(byte *)(lVar7 + 0xd504) ^ pbVar1[-3]);
      bVar9 = *(int *)(param_1 + 0x6c) < (int)uVar2;
      if ((int)uVar2 <= *(int *)(param_1 + 0x6c)) {
        return bVar9;
      }
      FUN_008514f8();
      lVar10 = lVar10 + -1;
      lVar8 = lVar8 + 4;
    } while (lVar10 != 0);
  }
  return bVar9;
}

~~~
