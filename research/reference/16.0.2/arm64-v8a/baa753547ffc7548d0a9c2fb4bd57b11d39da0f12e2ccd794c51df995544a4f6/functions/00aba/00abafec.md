# 00abafec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abaf7c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aba/00abaf7c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/2-3/priority-0064.md#compare-562909f98e3f9544068b4e7c6f9d7e62)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 対応先詳細の検証待ち
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/1-2/priority-0076.md#compare-ab93fb14e88558ead76a93b31c2b9a61)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abafec",
  "name": "FUN_00abafec",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fe3ac32cd5f508273222196571c2422b2b6c804ce2e1360b37b3a4f6596d77a8",
  "source_text_sha256": "fe3ac32cd5f508273222196571c2422b2b6c804ce2e1360b37b3a4f6596d77a8"
}
~~~

## 呼び出し元

- [00a84df8](../00a84/00a84df8.md)
- [00a85304](../00a85/00a85304.md)
- [00a8677c](../00a86/00a8677c.md)
- [00a86880](../00a86/00a86880.md)

## 呼び出し先

- [0043bbe4](../0043b/0043bbe4.md)
- [00851550](../00851/00851550.md)
- [00c57f60](../00c57/00c57f60.md)

## 疑似コード / UTF-8 3836 bytes

~~~c

int FUN_00abafec(void)

{
  long lVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  undefined8 *puVar4;
  long *plVar5;
  long lVar6;
  int iVar7;
  undefined8 *puVar8;
  int iVar9;
  undefined8 *puVar10;
  
  iVar7 = 0;
                    /* try { // try from 00abb008 to 00bbb017 has its CatchHandler @ 00abcaac */
  iVar9 = 0;
  do {
    if (iVar9 != 3) {
      lVar1 = FUN_00851550();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1);
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar2 = puVar4, puVar8 = puVar2, iVar9 < *(int *)(puVar2 + 4)) {
            puVar4 = (undefined8 *)*puVar2;
            puVar10 = puVar2;
            if ((undefined8 *)*puVar2 == (undefined8 *)0x0) goto LAB_00abb098;
          }
          if (iVar9 <= *(int *)(puVar2 + 4)) goto LAB_00abb0f4;
                    /* try { // try from 00abb08c to 00bbb097 has its CatchHandler @ 00abca54 */
          puVar4 = (undefined8 *)puVar2[1];
        } while ((undefined8 *)puVar2[1] != (undefined8 *)0x0);
        puVar10 = puVar2 + 1;
      }
LAB_00abb098:
                    /* try { // try from 00abb098 to 00bbb0a7 has its CatchHandler @ 00abca34 */
      puVar2 = (undefined8 *)_Znwm(0x40);
                    /* try { // try from 00abb0a8 to 00bbb0c3 has its CatchHandler @ 00abc9e8 */
      puVar2[7] = 0;
      puVar2[6] = 0;
      puVar2[5] = puVar2 + 6;
      *puVar2 = 0;
      puVar2[1] = 0;
      puVar2[2] = puVar8;
                    /* try { // try from 00abb0c4 to 00bbb18f has its CatchHandler @ 00abad54 */
      *puVar10 = puVar2;
      plVar5 = *(long **)((long)&fde_table_entry_003380d0.initial_loc + lVar1);
      *(int *)(puVar2 + 4) = iVar9;
      lVar6 = *plVar5;
      puVar4 = puVar2;
      if (lVar6 != 0) {
        *(long *)((long)&fde_table_entry_003380d0.initial_loc + lVar1) = lVar6;
        puVar4 = (undefined8 *)*puVar10;
      }
      FUN_0043bbe4(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1),puVar4);
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) + 1;
LAB_00abb0f4:
      puVar8 = puVar2 + 6;
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar4, puVar8 = puVar3, 0x2f < *(int *)((long)puVar3 + 0x1c)) {
            puVar4 = (undefined8 *)*puVar3;
            puVar10 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abb138;
          }
          if (*(int *)((long)puVar3 + 0x1c) == 0x2f) goto LAB_00abb028;
          puVar4 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar10 = puVar3 + 1;
      }
LAB_00abb138:
      puVar3 = (undefined8 *)_Znwm(0x28);
      *puVar3 = 0;
      puVar3[1] = 0;
      puVar3[2] = puVar8;
      *puVar10 = puVar3;
      plVar5 = (long *)puVar2[5];
      *(undefined4 *)((long)puVar3 + 0x1c) = 0x2f;
      *(undefined1 *)(puVar3 + 4) = 0;
      puVar4 = puVar3;
      if (*plVar5 != 0) {
        puVar2[5] = *plVar5;
        puVar4 = (undefined8 *)*puVar10;
      }
      FUN_0043bbe4(puVar2[6],puVar4);
      puVar2[7] = puVar2[7] + 1;
LAB_00abb028:
                    /* try { // try from 00abb034 to 00bbb03f has its CatchHandler @ 00abcaa8 */
      if (*(char *)(puVar3 + 4) != '\0') {
        iVar7 = iVar7 + 0x32;
      }
    }
    iVar9 = iVar9 + 1;
                    /* try { // try from 00abb040 to 00bbb053 has its CatchHandler @ 00abca94 */
    if (iVar9 == 10) {
                    /* try { // try from 00abb190 to 00bbb197 has its CatchHandler @ 00abcd44 */
      return iVar7;
    }
  } while( true );
}

~~~
