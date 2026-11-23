# 007ecdec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `007ecdec`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/007ec/007ecdec.md) · 移動量 `+0x0`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/97ee0756e9de6c746e3ce399/1-2/no_difference_in_scope-0012.md#compare-a6de0b624d4fde0d1a5b7fcc5601580f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 構造資料不足
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007ecdec",
  "name": "FUN_007ecdec",
  "size": 292,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d4988251fa489bd0d905c7e76869ed85affd989d2cf1c1da7d43afe781fa626a",
  "source_text_sha256": "d4988251fa489bd0d905c7e76869ed85affd989d2cf1c1da7d43afe781fa626a"
}
~~~

## 呼び出し元

- [0099a654](../0099a/0099a654.md)

## 呼び出し先

- [0041fdf0](../0041f/0041fdf0.md)
- [007eca30](../007ec/007eca30.md)
- [007ecd04](../007ec/007ecd04.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

## 疑似コード / UTF-8 2007 bytes

~~~c

byte FUN_007ecdec(long param_1,int param_2,long param_3)

{
  long *plVar1;
  byte bVar2;
  byte bVar3;
  byte bVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  long *plVar8;
  
  plVar5 = (long *)(param_1 + 200);
  plVar6 = (long *)*plVar5;
  plVar7 = plVar5;
  if (plVar6 != (long *)0x0) {
    do {
      if (param_2 <= *(int *)((long)plVar6 + 0x1c)) {
        plVar7 = plVar6;
      }
      plVar6 = (long *)plVar6[*(int *)((long)plVar6 + 0x1c) < param_2];
    } while (plVar6 != (long *)0x0);
                    /* try { // try from 007ece34 to 008ece43 has its CatchHandler @ 007ee4ac */
    if ((plVar7 != plVar5) && (*(int *)((long)plVar7 + 0x1c) <= param_2)) {
      bVar2 = FUN_007ecd04();
      bVar3 = FUN_007eca30(param_1,param_2);
      bVar4 = bVar2 & bVar3;
      if (((bVar2 & 1) != 0) || ((bVar3 & 1) == 0)) goto LAB_007ece40;
      plVar8 = (long *)(param_1 + 0xe0);
      plVar6 = (long *)*plVar8;
      plVar7 = plVar8;
      plVar5 = plVar6;
      if (plVar6 != (long *)0x0) {
        do {
          if (param_2 <= (int)plVar5[4]) {
            plVar7 = plVar5;
          }
          plVar1 = plVar5 + ((int)plVar5[4] < param_2);
          plVar5 = (long *)*plVar1;
        } while ((long *)*plVar1 != (long *)0x0);
        if ((plVar7 != plVar8) && ((int)plVar7[4] <= param_2)) {
          do {
            while (param_2 < (int)plVar6[4]) {
              plVar6 = (long *)*plVar6;
              if (plVar6 == (long *)0x0) goto LAB_007ecef4;
            }
            if (param_2 <= (int)plVar6[4]) {
              bVar4 = plVar6[5] < param_3;
              goto LAB_007ece40;
            }
            plVar6 = (long *)plVar6[1];
          } while (plVar6 != (long *)0x0);
LAB_007ecef4:
                    /* WARNING: Subroutine does not return */
          FUN_0041fdf0("map::at:  key not found");
        }
      }
    }
  }
  bVar4 = 1;
LAB_007ece40:
                    /* try { // try from 007ece50 to 008ed057 has its CatchHandler @ 007ee4d4 */
  return bVar4 & 1;
}

~~~
