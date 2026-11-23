# 00aefe6c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aefa44`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aef/00aefa44.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0065.md#compare-aebd96c6fe94c2388d2e693c8362ac70)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0070.md#compare-4625e59e93e197a5398fbd14af2c2ef8)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aefe6c",
  "name": "FUN_00aefe6c",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ad8bc11dbd966ed12528034f026cef24d379de05c2ad4782dd03c9d435aa879",
  "source_text_sha256": "2ad8bc11dbd966ed12528034f026cef24d379de05c2ad4782dd03c9d435aa879"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acf4](../0047a/0047acf4.md)
- [0047cdd4](../0047c/0047cdd4.md)
- [008b6ea4](../008b6/008b6ea4.md)
- [008b97a0](../008b9/008b97a0.md)
- [00a468f0](../00a46/00a468f0.md)
- [00a46bb8](../00a46/00a46bb8.md)
- [00aea354](../00aea/00aea354.md)
- [00aea5b0](../00aea/00aea5b0.md)

## 疑似コード / UTF-8 966 bytes

~~~c

void FUN_00aefe6c(long param_1,undefined8 *param_2,int *param_3)

{
  uint uVar1;
  undefined8 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*param_3 == 3) {
    uVar4 = *param_2;
    lVar5 = *(long *)(param_1 + 8);
    uVar2 = FUN_0047acf4();
    FUN_0047cdd4(uVar2,0xb,0);
    *(byte *)(lVar5 + 0x9ec) = *(byte *)(lVar5 + 0x9ec) ^ 1;
    uVar2 = FUN_008b6ea4(uVar4);
    uVar2 = FUN_00a468f0(uVar2,0);
    uVar3 = 0x90;
    if (*(char *)(lVar5 + 0x9ec) == '\0') {
      uVar3 = 0x91;
    }
    FUN_00a46bb8(uVar2,uVar3);
    uVar2 = *(undefined8 *)(param_1 + 0x10);
    uVar1 = FUN_00aea354(lVar5,*(undefined1 *)(lVar5 + 0x9ec));
    FUN_008b97a0(uVar2,0,uVar1 & 1);
    uVar2 = *(undefined8 *)(param_1 + 0x10);
    uVar1 = FUN_00aea5b0(lVar5,*(undefined1 *)(lVar5 + 0x9ec));
    FUN_008b97a0(uVar2,1,uVar1 & 1);
    return;
  }
  if (*param_3 == 0) {
    uVar2 = FUN_0047acf4();
    FUN_0047cdd4(uVar2,10,0);
    return;
  }
  return;
}

~~~
