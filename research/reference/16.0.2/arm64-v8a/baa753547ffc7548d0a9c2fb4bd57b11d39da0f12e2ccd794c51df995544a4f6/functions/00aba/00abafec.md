# 00abafec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

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
