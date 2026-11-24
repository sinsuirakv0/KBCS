# 00acaaa8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acaa38`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aca/00acaa38.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/high-0008.md#compare-cc0307774229d70b4c0de9cccf10fa3b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/high-0007.md#compare-47bf4286e5fc5eee79ca3df72e2faaed)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acaaa8",
  "name": "FUN_00acaaa8",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae02632717f98fe77b5f90be10db20dcf17cec2d43cd6ef05ba1f4a9f5aa9d5d",
  "source_text_sha256": "ae02632717f98fe77b5f90be10db20dcf17cec2d43cd6ef05ba1f4a9f5aa9d5d"
}
~~~

## 呼び出し元

- [0082fbc4](../0082f/0082fbc4.md)
- [00997090](../00997/00997090.md)

## 呼び出し先

- [004678a0](../00467/004678a0.md)
- [00467b6c](../00467/00467b6c.md)
- [00467f94](../00467/00467f94.md)
- [0046ca04](../0046c/0046ca04.md)
- [0046cac4](../0046c/0046cac4.md)
- [00851550](../00851/00851550.md)

## 疑似コード / UTF-8 603 bytes

~~~c

void FUN_00acaaa8(long param_1)

{
  int iVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  long lVar5;
  
  if (*(char *)(param_1 + 0xa0) != '\0') {
    uVar4 = FUN_004678a0();
    iVar1 = *(int *)(param_1 + 0xa4) * 0x14;
    if (0xfe < iVar1) {
      iVar1 = 0xff;
    }
    FUN_00467b6c(uVar4,0,0,0,iVar1);
    lVar5 = FUN_00851550();
    iVar1 = *(int *)((long)&fde_table_entry_003339e8.initial_loc + lVar5);
    FUN_00851550();
    uVar2 = FUN_0046ca04();
    FUN_00851550();
    uVar3 = FUN_0046cac4();
    FUN_00467f94(uVar4,0,-iVar1,uVar2,uVar3);
    return;
  }
  return;
}

~~~
