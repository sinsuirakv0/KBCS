# 00abaf7c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00abad80`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aba/00abad80.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/2-3/priority-0063.md#compare-ad61e09f663c5f744ebf3ff243d59006)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 対応先詳細の検証待ち
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/c6e4dfc940403d119ed8b991/0-1/priority-0068.md#compare-562909f98e3f9544068b4e7c6f9d7e62)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abaf7c",
  "name": "FUN_00abaf7c",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "de5a7817fca7de86d24bc2642b06a1fd48120dfee6b8de531e1b695a73a05916",
  "source_text_sha256": "de5a7817fca7de86d24bc2642b06a1fd48120dfee6b8de531e1b695a73a05916"
}
~~~

## 呼び出し元

- [00a84d88](../00a84/00a84d88.md)
- [00a85294](../00a85/00a85294.md)
- [00a8670c](../00a86/00a8670c.md)
- [00a86810](../00a86/00a86810.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [008514f8](../00851/008514f8.md)
- [00c57e90](../00c57/00c57e90.md)

## 疑似コード / UTF-8 3739 bytes

~~~c

int FUN_00abaf7c(void)

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
  iVar9 = 0;
  do {
    if (iVar9 != 3) {
      lVar1 = FUN_008514f8();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1);
                    /* try { // try from 00abafe0 to 00bbafeb has its CatchHandler @ 00abca54 */
                    /* try { // try from 00abafec to 00bbafff has its CatchHandler @ 00abca40 */
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar2 = puVar4, puVar8 = puVar2, iVar9 < *(int *)(puVar2 + 4)) {
            puVar4 = (undefined8 *)*puVar2;
            puVar10 = puVar2;
            if ((undefined8 *)*puVar2 == (undefined8 *)0x0) goto LAB_00abb028;
          }
          if (iVar9 <= *(int *)(puVar2 + 4)) goto LAB_00abb084;
          puVar4 = (undefined8 *)puVar2[1];
        } while ((undefined8 *)puVar2[1] != (undefined8 *)0x0);
        puVar10 = puVar2 + 1;
      }
LAB_00abb028:
      puVar2 = (undefined8 *)_Znwm(0x40);
                    /* try { // try from 00abb038 to 00bbb043 has its CatchHandler @ 00abca00 */
      puVar2[7] = 0;
      puVar2[6] = 0;
                    /* try { // try from 00abb044 to 00bbb053 has its CatchHandler @ 00abc9e0 */
      puVar2[5] = puVar2 + 6;
      *puVar2 = 0;
      puVar2[1] = 0;
      puVar2[2] = puVar8;
                    /* try { // try from 00abb054 to 00bbb06f has its CatchHandler @ 00abc994 */
      *puVar10 = puVar2;
      plVar5 = *(long **)((long)&fde_table_entry_003380d0.initial_loc + lVar1);
      *(int *)(puVar2 + 4) = iVar9;
      lVar6 = *plVar5;
      puVar4 = puVar2;
      if (lVar6 != 0) {
        *(long *)((long)&fde_table_entry_003380d0.initial_loc + lVar1) = lVar6;
        puVar4 = (undefined8 *)*puVar10;
      }
                    /* try { // try from 00abb070 to 00bbb13b has its CatchHandler @ 00abad00 */
      FUN_0043bba4(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1),puVar4);
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) + 1;
LAB_00abb084:
      puVar8 = puVar2 + 6;
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar4, puVar8 = puVar3, 0x2f < *(int *)((long)puVar3 + 0x1c)) {
            puVar4 = (undefined8 *)*puVar3;
            puVar10 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abb0c8;
          }
          if (*(int *)((long)puVar3 + 0x1c) == 0x2f) goto LAB_00abafb8;
          puVar4 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar10 = puVar3 + 1;
      }
LAB_00abb0c8:
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
      FUN_0043bba4(puVar2[6],puVar4);
                    /* try { // try from 00abafb4 to 00bbafc3 has its CatchHandler @ 00abca58 */
      puVar2[7] = puVar2[7] + 1;
LAB_00abafb8:
      if (*(char *)(puVar3 + 4) != '\0') {
        iVar7 = iVar7 + 0x32;
      }
    }
    iVar9 = iVar9 + 1;
    if (iVar9 == 10) {
      return iVar7;
    }
  } while( true );
}

~~~
