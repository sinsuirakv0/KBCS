# 00bfb2cc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfb230`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb230.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0086.md#compare-00d986ea682c9ef189e1b5fbdde1cfe8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0099.md#compare-a83f688a62cb4331ceae4a6b8664fe5f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb2cc",
  "name": "_ZNSt6__ndk18ios_base5pwordEi",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9611b7119b6fe70e63528bceffcb321031120284ab2e966513aebd7c8abf5dd0",
  "source_text_sha256": "9611b7119b6fe70e63528bceffcb321031120284ab2e966513aebd7c8abf5dd0"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bfb5e0](../00bfb/00bfb5e0.md)
- [00c58160](../00c58/00c58160.md)
- [00c5a170](../00c5a/00c5a170.md)

## 関連文字列（未確認候補）

~~~text
"ios_base::clear"
~~~

## 疑似コード / UTF-8 1569 bytes

~~~c

undefined8 * _ZNSt6__ndk18ios_base5pwordEi(long param_1,int param_2)

{
  ulong uVar1;
  void *pvVar2;
  void *pvVar3;
  void *__s;
  uint uVar4;
  void *pvVar5;
  ulong uVar6;
  ulong uVar7;
  
  uVar1 = (long)param_2 + 1;
  if (*(ulong *)(param_1 + 0x80) < uVar1) {
    uVar6 = *(long *)(param_1 + 0x68) * 2;
    if (uVar6 < uVar1 || uVar6 - uVar1 == 0) {
      uVar6 = uVar1;
    }
    if (0xffffffffffffffe < uVar1) {
      uVar6 = 0x1fffffffffffffff;
    }
    pvVar5 = realloc(*(void **)(param_1 + 0x70),uVar6 * 8);
    if (pvVar5 == (void *)0x0) {
      uVar4 = *(uint *)(param_1 + 0x20) | 1;
      *(uint *)(param_1 + 0x20) = uVar4;
      if ((*(uint *)(param_1 + 0x24) & uVar4) == 0) {
        DAT_011274a8 = 0;
        return &DAT_011274a8;
      }
                    /* WARNING: Subroutine does not return */
      FUN_00bfb5e0("ios_base::clear");
    }
    uVar7 = *(ulong *)(param_1 + 0x78);
    *(void **)(param_1 + 0x70) = pvVar5;
    if ((long)uVar7 < (long)uVar6) {
      pvVar3 = (void *)(uVar6 * 8 + (long)pvVar5);
      __s = (void *)((long)pvVar5 + uVar7 * 8);
      pvVar2 = (void *)((long)__s + 8);
      if (pvVar2 <= pvVar3) {
        pvVar2 = pvVar3;
      }
      memset(__s,0,((long)pvVar2 + uVar7 * -8 + ~(ulong)pvVar5 & 0xfffffffffffffff8) + 8);
    }
    *(ulong *)(param_1 + 0x80) = uVar6;
  }
  else {
    pvVar5 = *(void **)(param_1 + 0x70);
    uVar7 = *(ulong *)(param_1 + 0x78);
  }
  if (uVar7 <= uVar1) {
    uVar7 = uVar1;
  }
  *(ulong *)(param_1 + 0x78) = uVar7;
  return (undefined8 *)((long)pvVar5 + (long)param_2 * 8);
}

~~~
