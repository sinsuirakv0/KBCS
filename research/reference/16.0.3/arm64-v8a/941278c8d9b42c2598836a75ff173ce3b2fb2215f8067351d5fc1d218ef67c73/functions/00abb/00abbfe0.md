# 00abbfe0

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00abbfe0",
  "name": "FUN_00abbfe0",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1cda622f2e57fc18f1c2301670f4bccaa4e3e8604fcc2e9586e58400f3c01fc3",
  "source_text_sha256": "1cda622f2e57fc18f1c2301670f4bccaa4e3e8604fcc2e9586e58400f3c01fc3"
}
~~~

## 呼び出し元

- [00a85dec](../00a85/00a85dec.md)
- [00a862f8](../00a86/00a862f8.md)
- [00a87770](../00a87/00a87770.md)
- [00a87874](../00a87/00a87874.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [008524fc](../00852/008524fc.md)
- [00c58f30](../00c58/00c58f30.md)

## 疑似コード / UTF-8 3836 bytes

~~~c

int FUN_00abbfe0(void)

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
  
                    /* try { // try from 00abbfe0 to 00bbbfeb has its CatchHandler @ 00abda54 */
                    /* try { // try from 00abbfec to 00bbbfff has its CatchHandler @ 00abda40 */
  iVar7 = 0;
  iVar9 = 0;
  do {
                    /* try { // try from 00abc038 to 00bbc043 has its CatchHandler @ 00abda00 */
    if (iVar9 != 3) {
      lVar1 = FUN_008524fc();
      puVar8 = (undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1);
                    /* try { // try from 00abc044 to 00bbc053 has its CatchHandler @ 00abd9e0 */
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
                    /* try { // try from 00abc070 to 00bbc13b has its CatchHandler @ 00abbd00 */
          while (puVar2 = puVar4, puVar8 = puVar2, iVar9 < *(int *)(puVar2 + 4)) {
            puVar4 = (undefined8 *)*puVar2;
            puVar10 = puVar2;
            if ((undefined8 *)*puVar2 == (undefined8 *)0x0) goto LAB_00abc08c;
          }
          if (iVar9 <= *(int *)(puVar2 + 4)) goto LAB_00abc0e8;
          puVar4 = (undefined8 *)puVar2[1];
        } while ((undefined8 *)puVar2[1] != (undefined8 *)0x0);
        puVar10 = puVar2 + 1;
      }
LAB_00abc08c:
      puVar2 = (undefined8 *)_Znwm(0x40);
      puVar2[7] = 0;
      puVar2[6] = 0;
      puVar2[5] = puVar2 + 6;
      *puVar2 = 0;
      puVar2[1] = 0;
      puVar2[2] = puVar8;
      *puVar10 = puVar2;
      plVar5 = *(long **)((long)&fde_table_entry_003380d0.initial_loc + lVar1);
      *(int *)(puVar2 + 4) = iVar9;
      lVar6 = *plVar5;
      puVar4 = puVar2;
      if (lVar6 != 0) {
        *(long *)((long)&fde_table_entry_003380d0.initial_loc + lVar1) = lVar6;
        puVar4 = (undefined8 *)*puVar10;
      }
      FUN_0043bf04(*(undefined8 *)((long)&fde_table_entry_003380d8.initial_loc + lVar1),puVar4);
      *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) =
           *(long *)((long)&fde_table_entry_003380e0.initial_loc + lVar1) + 1;
LAB_00abc0e8:
      puVar8 = puVar2 + 6;
      puVar4 = (undefined8 *)*puVar8;
      puVar10 = puVar8;
      if ((undefined8 *)*puVar8 != (undefined8 *)0x0) {
        do {
          while (puVar3 = puVar4, puVar8 = puVar3, 0x2f < *(int *)((long)puVar3 + 0x1c)) {
            puVar4 = (undefined8 *)*puVar3;
            puVar10 = puVar3;
            if ((undefined8 *)*puVar3 == (undefined8 *)0x0) goto LAB_00abc12c;
          }
          if (*(int *)((long)puVar3 + 0x1c) == 0x2f) goto LAB_00abc01c;
          puVar4 = (undefined8 *)puVar3[1];
        } while ((undefined8 *)puVar3[1] != (undefined8 *)0x0);
        puVar10 = puVar3 + 1;
      }
LAB_00abc12c:
      puVar3 = (undefined8 *)_Znwm(0x28);
      *puVar3 = 0;
      puVar3[1] = 0;
                    /* try { // try from 00abc13c to 00bbc143 has its CatchHandler @ 00abdcf0 */
      puVar3[2] = puVar8;
      *puVar10 = puVar3;
      plVar5 = (long *)puVar2[5];
      *(undefined4 *)((long)puVar3 + 0x1c) = 0x2f;
      *(undefined1 *)(puVar3 + 4) = 0;
      puVar4 = puVar3;
      if (*plVar5 != 0) {
                    /* try { // try from 00abc160 to 00bbc16b has its CatchHandler @ 00abdcd4 */
        puVar2[5] = *plVar5;
        puVar4 = (undefined8 *)*puVar10;
      }
      FUN_0043bf04(puVar2[6],puVar4);
      puVar2[7] = puVar2[7] + 1;
LAB_00abc01c:
      if (*(char *)(puVar3 + 4) != '\0') {
        iVar7 = iVar7 + 0x32;
      }
    }
    iVar9 = iVar9 + 1;
    if (iVar9 == 10) {
                    /* try { // try from 00abc16c to 00bbc17f has its CatchHandler @ 00abdc9c */
      return iVar7;
    }
  } while( true );
}

~~~
