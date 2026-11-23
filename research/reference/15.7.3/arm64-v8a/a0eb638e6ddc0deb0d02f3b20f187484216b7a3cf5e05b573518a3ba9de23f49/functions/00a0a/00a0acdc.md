# 00a0acdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a0acdc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a0a/00a0acdc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/no_difference_in_scope-0018.md#compare-4d9821a3f08bd75f16c03a8bd185ee38)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a0acdc",
  "name": "FUN_00a0acdc",
  "size": 256,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0446610eac66ad2109b41d950116ea9ac1dc16629308f2e77e10dc3e3ff790f7",
  "source_text_sha256": "0446610eac66ad2109b41d950116ea9ac1dc16629308f2e77e10dc3e3ff790f7"
}
~~~

## 呼び出し元

- [00a0baf4](../00a0b/00a0baf4.md)

## 呼び出し先

- [0041fdf0](../0041f/0041fdf0.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

## 疑似コード / UTF-8 2297 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

undefined4 FUN_00a0acdc(long param_1,int param_2,int param_3)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  
                    /* try { // try from 00a0acdc to 00b0ace3 has its CatchHandler @ 00a0d5b0 */
  plVar1 = *(long **)(param_1 + 0x10);
  plVar2 = plVar1;
  do {
    if (plVar2 == (long *)0x0) {
      return 0;
    }
    if (*(int *)(plVar2 + 4) <= param_2) {
                    /* try { // try from 00a0ad08 to 00b0ad0f has its CatchHandler @ 00a0d5dc */
      plVar3 = plVar1;
      if (param_2 <= *(int *)(plVar2 + 4)) break;
      plVar2 = plVar2 + 1;
    }
    plVar2 = (long *)*plVar2;
  } while( true );
  while (plVar3 != (long *)0x0) {
    if (param_2 < (int)plVar3[4]) {
      plVar3 = (long *)*plVar3;
    }
    else {
      if (param_2 <= (int)plVar3[4]) {
        plVar2 = (long *)plVar3[6];
        goto joined_r0x00a0ad4c;
      }
      plVar3 = (long *)plVar3[1];
    }
  }
  goto LAB_00a0ad3c;
joined_r0x00a0ad4c:
  if (plVar2 == (long *)0x0) {
    return 0;
  }
                    /* try { // try from 00a0ad68 to 00b0aebb has its CatchHandler @ 00a0a31c */
  if (*(int *)((long)plVar2 + 0x1c) <= param_3) {
    if (param_3 <= *(int *)((long)plVar2 + 0x1c)) goto LAB_00a0ad84;
    plVar2 = plVar2 + 1;
  }
                    /* try { // try from 00a0ad60 to 00b0ad67 has its CatchHandler @ 00a0d5bc */
  plVar2 = (long *)*plVar2;
  goto joined_r0x00a0ad4c;
LAB_00a0ad84:
  do {
    if (param_2 < (int)plVar1[4]) {
      plVar1 = (long *)*plVar1;
    }
    else {
      if (param_2 <= (int)plVar1[4]) {
        for (plVar2 = (long *)plVar1[6]; plVar2 != (long *)0x0; plVar2 = (long *)*plVar2) {
          while (*(int *)((long)plVar2 + 0x1c) <= param_3) {
            if (param_3 <= *(int *)((long)plVar2 + 0x1c)) {
              return (int)plVar2[4];
            }
            plVar2 = (long *)plVar2[1];
            if (plVar2 == (long *)0x0) goto LAB_00a0ad3c;
          }
        }
        break;
      }
      plVar1 = (long *)plVar1[1];
    }
  } while (plVar1 != (long *)0x0);
LAB_00a0ad3c:
                    /* try { // try from 00a0ad3c to 00b0ad43 has its CatchHandler @ 00a0d5b4 */
                    /* WARNING: Subroutine does not return */
  FUN_0041fdf0("map::at:  key not found");
}

~~~
