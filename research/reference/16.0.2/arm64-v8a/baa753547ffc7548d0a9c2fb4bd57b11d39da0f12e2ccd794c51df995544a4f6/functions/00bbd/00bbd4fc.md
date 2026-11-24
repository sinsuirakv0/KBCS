# 00bbd4fc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbd460`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbd/00bbd460.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/alignment_unresolved-0010.md#compare-4fffdbebe539addb396e03ac0f3ab154)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/inspection-0036.md#compare-4722b768005a7160228ec861ebf2b6e5)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbd4fc",
  "name": "FUN_00bbd4fc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ac5edd45d20957f33e04eb3fda0bc93f5ee7a911d2ea60af88b3df77e3f1fb3b",
  "source_text_sha256": "ac5edd45d20957f33e04eb3fda0bc93f5ee7a911d2ea60af88b3df77e3f1fb3b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ae70](../00c5a/00c5ae70.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5d340](../00c5d/00c5d340.md)

## 疑似コード / UTF-8 976 bytes

~~~c

void FUN_00bbd4fc(undefined8 param_1,undefined8 param_2,int param_3,undefined8 param_4,void *param_5
                 )

{
  long lVar1;
  undefined8 uVar2;
  undefined1 auStack_60 [16];
  undefined1 auStack_50 [8];
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  uVar2 = _ZN8firebase9messaging10FutureData3GetEv();
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_60,param_5);
                    /* try { // try from 00bbd554 to 00cbd59b has its CatchHandler @ 00bbd73c */
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
            (uVar2,auStack_60,(ulong)(param_3 != 0) << 2,param_4,auStack_50);
  _ZN8firebase12FutureHandleD2Ev(auStack_60);
  _ZN8firebase12FutureHandleD2Ev(param_5);
  _ZdlPv(param_5);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
