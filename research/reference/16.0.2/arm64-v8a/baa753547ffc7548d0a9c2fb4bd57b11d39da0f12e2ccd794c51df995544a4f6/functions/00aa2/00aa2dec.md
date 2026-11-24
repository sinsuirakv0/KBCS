# 00aa2dec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aa2d7c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa2/00aa2d7c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0064.md#compare-3e3cd8097e039e717fe01f59a1ef53b8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0075.md#compare-161269ca4bbaaac8905009ab54af4db0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa2dec",
  "name": "FUN_00aa2dec",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e86789b79749c592de946316583745e79699d066f1d180b69ed47742c716edf6",
  "source_text_sha256": "e86789b79749c592de946316583745e79699d066f1d180b69ed47742c716edf6"
}
~~~

## 呼び出し元

- [007ccf44](../007cc/007ccf44.md)

## 呼び出し先

- [00442970](../00442/00442970.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

## 疑似コード / UTF-8 947 bytes

~~~c

undefined4 FUN_00aa2dec(long param_1,int param_2)

{
  long *plVar1;
  long *plVar2;
  
  plVar1 = *(long **)(param_1 + 0x20);
  plVar2 = plVar1;
  do {
    if (plVar2 == (long *)0x0) {
      return 0;
    }
    if (*(int *)((long)plVar2 + 0x1c) <= param_2) {
      if (param_2 <= *(int *)((long)plVar2 + 0x1c)) {
        do {
          if (param_2 < *(int *)((long)plVar1 + 0x1c)) {
            plVar1 = (long *)*plVar1;
          }
          else {
            if (param_2 <= *(int *)((long)plVar1 + 0x1c)) {
                    /* catch() { ... } // from try @ 00aa314c with catch @ 00aa2e60 */
              return (int)plVar1[4];
            }
            plVar1 = (long *)plVar1[1];
          }
        } while (plVar1 != (long *)0x0);
                    /* WARNING: Subroutine does not return */
        FUN_00442970("map::at:  key not found");
      }
      plVar2 = plVar2 + 1;
    }
    plVar2 = (long *)*plVar2;
  } while( true );
}

~~~
