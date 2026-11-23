# 00a0addc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a0addc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a0a/00a0addc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/af8e2f5c5fc38f06774ff85c/0-1/machine_only_observed-0039.md#compare-251d4a6a5957428a5832709d9c4e91f2)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 構造資料不足
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a0addc",
  "name": "FUN_00a0addc",
  "size": 608,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45c44d40e76d6c2e6a71388718e787e112b802f96d17071a5193f84e92d50935",
  "source_text_sha256": "45c44d40e76d6c2e6a71388718e787e112b802f96d17071a5193f84e92d50935"
}
~~~

## 呼び出し元

- [00a0bbd8](../00a0b/00a0bbd8.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0041fdf0](../0041f/0041fdf0.md)
- [00bdaff0](../00bda/00bdaff0.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

## 疑似コード / UTF-8 4655 bytes

~~~c

void FUN_00a0addc(long param_1,int param_2,int param_3,int param_4)

{
  int iVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  long *plVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  
  puVar7 = (undefined8 *)(param_1 + 0x10);
  puVar3 = (undefined8 *)*puVar7;
  puVar6 = puVar3;
  puVar5 = puVar7;
  if (puVar3 != (undefined8 *)0x0) {
    do {
      iVar1 = param_4;
      if (*(int *)(puVar6 + 4) <= param_2) {
        puVar5 = puVar3;
        if (param_2 <= *(int *)(puVar6 + 4)) goto LAB_00a0ae50;
        puVar6 = puVar6 + 1;
      }
      puVar6 = (undefined8 *)*puVar6;
    } while (puVar6 != (undefined8 *)0x0);
LAB_00a0af10:
    do {
      param_4 = iVar1;
      puVar7 = puVar3;
      iVar1 = param_4;
      if (*(int *)(puVar7 + 4) <= param_2) {
        puVar6 = puVar7;
        if (param_2 <= *(int *)(puVar7 + 4)) goto LAB_00a0af94;
        puVar3 = (undefined8 *)puVar7[1];
        if ((undefined8 *)puVar7[1] == (undefined8 *)0x0) {
          puVar5 = puVar7 + 1;
          break;
        }
        goto LAB_00a0af10;
      }
      puVar3 = (undefined8 *)*puVar7;
      puVar5 = puVar7;
    } while ((undefined8 *)*puVar7 != (undefined8 *)0x0);
  }
  puVar6 = (undefined8 *)_Znwm(0x40);
  puVar6[7] = 0;
  puVar6[6] = 0;
  puVar6[5] = puVar6 + 6;
  *puVar6 = 0;
  puVar6[1] = 0;
  puVar6[2] = puVar7;
  *puVar5 = puVar6;
                    /* try { // try from 00a0af68 to 00b0af73 has its CatchHandler @ 00a0d0f4 */
  plVar4 = *(long **)(param_1 + 8);
  *(int *)(puVar6 + 4) = param_2;
  puVar3 = puVar6;
  if (*plVar4 != 0) {
    *(long *)(param_1 + 8) = *plVar4;
    puVar3 = (undefined8 *)*puVar5;
  }
  FUN_00419064(*(undefined8 *)(param_1 + 0x10),puVar3);
  *(long *)(param_1 + 0x18) = *(long *)(param_1 + 0x18) + 1;
LAB_00a0af94:
  puVar5 = (undefined8 *)puVar6[6];
  puVar3 = puVar6 + 6;
  do {
    puVar7 = puVar3;
    if (puVar5 == (undefined8 *)0x0) {
LAB_00a0afd4:
      puVar2 = (undefined8 *)_Znwm(0x28);
      *puVar2 = 0;
      puVar2[1] = 0;
      puVar2[2] = puVar3;
      *puVar7 = puVar2;
      plVar4 = (long *)puVar6[5];
      *(int *)((long)puVar2 + 0x1c) = param_3;
      *(undefined4 *)(puVar2 + 4) = 0;
      puVar3 = puVar2;
      if (*plVar4 != 0) {
        puVar6[5] = *plVar4;
        puVar3 = (undefined8 *)*puVar7;
      }
      FUN_00419064(puVar6[6],puVar3);
      puVar6[7] = puVar6[7] + 1;
LAB_00a0b020:
      *(int *)(puVar2 + 4) = param_4;
                    /* try { // try from 00a0b030 to 00b0b03b has its CatchHandler @ 00a0d26c */
      return;
    }
    while (puVar2 = puVar5, puVar3 = puVar2, *(int *)((long)puVar2 + 0x1c) <= param_3) {
      if (param_3 <= *(int *)((long)puVar2 + 0x1c)) goto LAB_00a0b020;
      puVar5 = (undefined8 *)puVar2[1];
      if ((undefined8 *)puVar2[1] == (undefined8 *)0x0) {
        puVar7 = puVar2 + 1;
        goto LAB_00a0afd4;
      }
    }
    puVar5 = (undefined8 *)*puVar2;
  } while( true );
  while (puVar5 != (undefined8 *)0x0) {
LAB_00a0ae50:
    if (param_2 < *(int *)(puVar5 + 4)) {
      puVar5 = (undefined8 *)*puVar5;
    }
    else {
      if (param_2 <= *(int *)(puVar5 + 4)) {
        plVar4 = (long *)puVar5[6];
        goto joined_r0x00a0ae78;
      }
      puVar5 = (undefined8 *)puVar5[1];
    }
  }
  goto LAB_00a0ae68;
joined_r0x00a0ae78:
  if (plVar4 == (long *)0x0) goto LAB_00a0af10;
  if (*(int *)((long)plVar4 + 0x1c) <= param_3) {
    puVar6 = puVar3;
    if (param_3 <= *(int *)((long)plVar4 + 0x1c)) goto LAB_00a0aeac;
    plVar4 = plVar4 + 1;
  }
  plVar4 = (long *)*plVar4;
  goto joined_r0x00a0ae78;
  while (puVar6 != (undefined8 *)0x0) {
LAB_00a0aeac:
    if (param_2 < *(int *)(puVar6 + 4)) {
      puVar6 = (undefined8 *)*puVar6;
    }
    else {
      if (param_2 <= *(int *)(puVar6 + 4)) {
        plVar4 = (long *)puVar6[6];
        goto joined_r0x00a0aecc;
      }
                    /* try { // try from 00a0aebc to 00b0aec7 has its CatchHandler @ 00a0d11c */
      puVar6 = (undefined8 *)puVar6[1];
    }
  }
  goto LAB_00a0ae68;
joined_r0x00a0aecc:
  if (plVar4 != (long *)0x0) {
    if (param_3 < *(int *)((long)plVar4 + 0x1c)) {
      plVar4 = (long *)*plVar4;
    }
    else {
      if (param_3 <= *(int *)((long)plVar4 + 0x1c)) {
        iVar1 = *(int *)(plVar4 + 4);
        if (*(int *)(plVar4 + 4) <= param_4) {
          iVar1 = param_4;
        }
        goto LAB_00a0af10;
      }
                    /* try { // try from 00a0aeec to 00b0aef7 has its CatchHandler @ 00a0d118 */
      plVar4 = (long *)plVar4[1];
    }
    goto joined_r0x00a0aecc;
  }
LAB_00a0ae68:
                    /* WARNING: Subroutine does not return */
  FUN_0041fdf0("map::at:  key not found");
}

~~~
