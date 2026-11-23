# 00aa2bfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a44cf8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a44/00a44cf8.md) · 移動量 `+0x5df04`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/2-3/priority-0052.md#compare-f95e4cdda8a54129821c04de11551ea3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 構造資料不足
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa2bfc",
  "name": "FUN_00aa2bfc",
  "size": 124,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e269cb7a9155463c7f64c3a6ea6843bdf42c2a946ca918575ff6bca744eb2bcb",
  "source_text_sha256": "e269cb7a9155463c7f64c3a6ea6843bdf42c2a946ca918575ff6bca744eb2bcb"
}
~~~

## 呼び出し元

- [005fe62c](../005fe/005fe62c.md)
- [007bda04](../007bd/007bda04.md)
- [007cceac](../007cc/007cceac.md)
- [007df0a8](../007df/007df0a8.md)

## 呼び出し先

- [004428f0](../00442/004428f0.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

## 疑似コード / UTF-8 969 bytes

~~~c

undefined4 FUN_00aa2bfc(long param_1,int param_2)

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
                    /* catch() { ... } // from try @ 00aa2f5c with catch @ 00aa2c70 */
              return *(undefined4 *)((long)plVar1 + 0x24);
            }
            plVar1 = (long *)plVar1[1];
          }
        } while (plVar1 != (long *)0x0);
                    /* WARNING: Subroutine does not return */
        FUN_004428f0("map::at:  key not found");
      }
      plVar2 = plVar2 + 1;
    }
    plVar2 = (long *)*plVar2;
  } while( true );
}

~~~
