# 00bf9aac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf9a10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf9/00bf9a10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0086.md#compare-8bddcb0b2f8db2f602d36a3608f0ab25)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0098.md#compare-43f74062764d7bc20437fd90b0ee5a1a)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf9aac",
  "name": "_ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE",
  "size": 144,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5cac8a2745ea7a00e46c3c8060bca9e60be786e48a4e49c1f283941c0870eb0",
  "source_text_sha256": "e5cac8a2745ea7a00e46c3c8060bca9e60be786e48a4e49c1f283941c0870eb0"
}
~~~

## 呼び出し元

- [00c58570](../00c58/00c58570.md)

## 呼び出し先

- [00c581c0](../00c58/00c581c0.md)
- [00c581f0](../00c58/00c581f0.md)
- [00c58550](../00c58/00c58550.md)

## 関連文字列（未確認候補）

~~~text
"unique_lock::unlock: not locked"
~~~

## 疑似コード / UTF-8 1079 bytes

~~~c

void _ZNSt6__ndk117__assoc_sub_state10__sub_waitERNS_11unique_lockINS_5mutexEEE
               (long *param_1,undefined8 *param_2)

{
  uint uVar1;
  byte bVar2;
  long lVar3;
  
  uVar1 = *(uint *)(param_1 + 0xe);
  if ((uVar1 >> 2 & 1) == 0) {
    if ((uVar1 >> 3 & 1) != 0) {
      bVar2 = *(byte *)(param_2 + 1);
      *(uint *)(param_1 + 0xe) = uVar1 & 0xfffffff3;
      if ((bVar2 & 1) != 0) {
        _ZNSt6__ndk15mutex6unlockEv(*param_2);
        lVar3 = *param_1;
        *(undefined1 *)(param_2 + 1) = 0;
                    /* WARNING: Could not recover jumptable at 0x00bf9b28. Too many branches */
                    /* WARNING: Treating indirect jump as call */
        (**(code **)(lVar3 + 0x18))(param_1);
        return;
      }
                    /* WARNING: Subroutine does not return */
      _ZNSt6__ndk120__throw_system_errorEiPKc(1,"unique_lock::unlock: not locked");
    }
    do {
      _ZNSt6__ndk118condition_variable4waitERNS_11unique_lockINS_5mutexEEE(param_1 + 8,param_2);
    } while ((*(byte *)(param_1 + 0xe) >> 2 & 1) == 0);
  }
  return;
}

~~~
