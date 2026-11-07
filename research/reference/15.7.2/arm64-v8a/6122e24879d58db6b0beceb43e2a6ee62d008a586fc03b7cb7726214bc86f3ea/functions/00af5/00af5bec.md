# 00af5bec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00af5cf8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af5/00af5cf8.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00af5bec",
  "name": "_ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "afa9c1d15e8a8d8b7216e84dad9482c837aaa477259a8aafd19f3928f249dd0e",
  "source_text_sha256": "afa9c1d15e8a8d8b7216e84dad9482c837aaa477259a8aafd19f3928f249dd0e"
}
~~~

## 呼び出し元

- [00bddfc0](../00bdd/00bddfc0.md)

## 呼び出し先

- [0056681c](../00566/0056681c.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bde660](../00bde/00bde660.md)
- [00bde720](../00bde/00bde720.md)
- [00bde730](../00bde/00bde730.md)

## 疑似コード / UTF-8 5215 bytes

~~~c

void _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
               (long *param_1,undefined8 param_2,undefined8 param_3,long param_4,ulong param_5)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  undefined8 *puVar4;
  long lVar5;
  undefined8 *puVar6;
  long *plVar7;
  long *plVar8;
  long *plVar9;
  long *plVar10;
  
                    /* try { // try from 00af5bec to 00bf5bf3 has its CatchHandler @ 00affc2c */
                    /* try { // try from 00af5bf8 to 00bf5bff has its CatchHandler @ 00affc20 */
                    /* try { // try from 00af5c04 to 00bf5c0b has its CatchHandler @ 00affc08 */
                    /* try { // try from 00af5c10 to 00bf5c17 has its CatchHandler @ 00affbfc */
                    /* try { // try from 00af5c1c to 00bf5c23 has its CatchHandler @ 00affbe4 */
  pthread_mutex_lock((pthread_mutex_t *)&DAT_010a09c8);
  plVar7 = DAT_010a09c0;
  plVar8 = DAT_010a09c0 + 1;
                    /* try { // try from 00af5c28 to 00bf5c2f has its CatchHandler @ 00affbd8 */
                    /* try { // try from 00af5c34 to 00bf5c3b has its CatchHandler @ 00affbc0 */
  plVar9 = (long *)*plVar8;
  plVar2 = plVar8;
  if (plVar9 == (long *)0x0) {
LAB_00af5c7c:
    puVar6 = (undefined8 *)*plVar8;
    plVar10 = plVar8;
  }
  else {
    plVar8 = DAT_010a09c0 + 1;
    do {
      while (plVar10 = plVar9, plVar2 = plVar10, (ulong)plVar10[4] <= param_5) {
        if (param_5 <= (ulong)plVar10[4]) goto LAB_00af5c7c;
        plVar8 = plVar10 + 1;
        plVar9 = (long *)*plVar8;
        if ((long *)*plVar8 == (long *)0x0) goto LAB_00af5c7c;
      }
      plVar8 = plVar10;
      plVar9 = (long *)*plVar10;
    } while ((long *)*plVar10 != (long *)0x0);
    puVar6 = (undefined8 *)*plVar10;
                    /* try { // try from 00af5cc8 to 00bf5ccf has its CatchHandler @ 00affb6c */
  }
                    /* try { // try from 00af5c80 to 00bf5c87 has its CatchHandler @ 00affbb4 */
  if (puVar6 == (undefined8 *)0x0) {
    puVar6 = (undefined8 *)_Znwm(0x40);
                    /* try { // try from 00af5c8c to 00bf5c93 has its CatchHandler @ 00affba8 */
    *puVar6 = 0;
    puVar6[1] = 0;
    puVar6[2] = plVar2;
                    /* try { // try from 00af5c98 to 00bf5c9f has its CatchHandler @ 00affb9c */
    puVar6[4] = param_5;
    puVar6[5] = puVar6 + 5;
    puVar6[6] = puVar6 + 5;
    puVar6[7] = 0;
    *plVar10 = (long)puVar6;
                    /* try { // try from 00af5ca4 to 00bf5cab has its CatchHandler @ 00affb90 */
                    /* try { // try from 00af5cb0 to 00bf5cb7 has its CatchHandler @ 00affb84 */
    puVar4 = puVar6;
    if (*(long *)*plVar7 != 0) {
      *plVar7 = *(long *)*plVar7;
      puVar4 = (undefined8 *)*plVar10;
                    /* try { // try from 00af5cbc to 00bf5cc3 has its CatchHandler @ 00affb78 */
    }
                    /* try { // try from 00af5cd4 to 00bf5cdb has its CatchHandler @ 00affb54 */
    _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_(plVar7[1],puVar4);
                    /* try { // try from 00af5ce0 to 00bf5ce7 has its CatchHandler @ 00affb48 */
    plVar7[2] = plVar7[2] + 1;
  }
                    /* try { // try from 00af5cec to 00bf5cf3 has its CatchHandler @ 00affb30 */
  plVar2 = (long *)_Znwm(0x38);
  plVar2[5] = 0;
  plVar2[6] = 0;
                    /* try { // try from 00af5cf8 to 00bf5cff has its CatchHandler @ 00affb28 */
  plVar2[4] = 0;
  plVar2[1] = (long)(puVar6 + 5);
  lVar5 = puVar6[5];
                    /* try { // try from 00af5d04 to 00bf5d17 has its CatchHandler @ 00afffd8 */
  *plVar2 = lVar5;
  *(long **)(lVar5 + 8) = plVar2;
  puVar6[5] = plVar2;
                    /* try { // try from 00af5d20 to 00bf5d27 has its CatchHandler @ 00affb20 */
  puVar6[7] = puVar6[7] + 1;
  plVar7 = plVar2 + 2;
  *plVar7 = 0;
  plVar2[3] = param_4;
  plVar2[4] = (long)plVar2;
                    /* try { // try from 00af5d2c to 00bf5d3f has its CatchHandler @ 00afff94 */
  plVar2[5] = (long)(puVar6 + 5);
  *(undefined1 *)(plVar2 + 6) = 0;
                    /* try { // try from 00af5d40 to 00bf5d5b has its CatchHandler @ 00af560c */
  pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a09c8);
                    /* try { // try from 00af5d5c to 00bf5d63 has its CatchHandler @ 00affb18 */
                    /* try { // try from 00af5d64 to 00bf5ee7 has its CatchHandler @ 00af560c */
  uVar3 = FUN_0056681c(param_1,DAT_010a0290,DAT_010a02a0,param_2,param_3,plVar7);
  pthread_mutex_lock((pthread_mutex_t *)&DAT_010a09c8);
  if ((char)plVar2[6] == '\0') {
    lVar5 = (**(code **)(*param_1 + 0xa8))(param_1,uVar3);
    *plVar7 = lVar5;
  }
  else {
    plVar7 = (long *)plVar2[4];
    lVar1 = plVar2[5];
    lVar5 = *plVar7;
    *(long *)(lVar5 + 8) = plVar7[1];
    *(long *)plVar7[1] = lVar5;
    *(long *)(lVar1 + 0x10) = *(long *)(lVar1 + 0x10) + -1;
    _ZdlPv(plVar7);
  }
  pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a09c8);
                    /* WARNING: Could not recover jumptable at 0x00af5df0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 0xb8))(param_1,uVar3);
  return;
}

~~~
