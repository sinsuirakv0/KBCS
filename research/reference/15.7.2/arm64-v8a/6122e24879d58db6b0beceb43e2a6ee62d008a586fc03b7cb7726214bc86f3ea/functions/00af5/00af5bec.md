# 00af5bec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00af5bec.md)

## 関数情報

~~~json
{
  "address": "00af5bec",
  "name": "firebase::util::RegisterCallbackOnTask",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07d5977578993757619abd63546a6d4150cd207c0047adbf8bf70728c28bf350",
  "source_text_sha256": "07d5977578993757619abd63546a6d4150cd207c0047adbf8bf70728c28bf350"
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

## 疑似コード 1/1 / UTF-8 5795 bytes

~~~c

/* firebase::util::RegisterCallbackOnTask(_JNIEnv*, _jobject*, void (*)(_JNIEnv*, _jobject*,
   firebase::util::FutureResult, char const*, void*), void*, char const*) */

void firebase::util::RegisterCallbackOnTask
               (_JNIEnv *param_1,_jobject *param_2,
               _func_void__JNIEnv_ptr__jobject_ptr_FutureResult_char_ptr_void_ptr *param_3,
               void *param_4,char *param_5)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  undefined8 uVar4;
  __tree_node_base *p_Var5;
  long lVar6;
  __tree_node_base *p_Var7;
  long *plVar8;
  long *plVar9;
  
                    /* try { // try from 00af5bec to 00bf5bf3 has its CatchHandler @ 00affc2c */
                    /* try { // try from 00af5bf8 to 00bf5bff has its CatchHandler @ 00affc20 */
                    /* try { // try from 00af5c04 to 00bf5c0b has its CatchHandler @ 00affc08 */
                    /* try { // try from 00af5c10 to 00bf5c17 has its CatchHandler @ 00affbfc */
                    /* try { // try from 00af5c1c to 00bf5c23 has its CatchHandler @ 00affbe4 */
  pthread_mutex_lock((pthread_mutex_t *)&DAT_010a09c8);
  plVar2 = DAT_010a09c0;
  plVar3 = DAT_010a09c0 + 1;
                    /* try { // try from 00af5c28 to 00bf5c2f has its CatchHandler @ 00affbd8 */
                    /* try { // try from 00af5c34 to 00bf5c3b has its CatchHandler @ 00affbc0 */
  plVar8 = (long *)*plVar3;
  plVar9 = plVar3;
  if (plVar8 != (long *)0x0) {
    plVar3 = DAT_010a09c0 + 1;
    do {
      while (plVar9 = plVar8, param_5 < (char *)plVar9[4]) {
        plVar3 = plVar9;
        plVar8 = (long *)*plVar9;
        if ((long *)*plVar9 == (long *)0x0) {
          p_Var7 = (__tree_node_base *)*plVar9;
          goto joined_r0x00af5cc8;
        }
      }
      if (param_5 <= (char *)plVar9[4]) break;
      plVar3 = plVar9 + 1;
      plVar8 = (long *)*plVar3;
    } while ((long *)*plVar3 != (long *)0x0);
  }
  p_Var7 = (__tree_node_base *)*plVar3;
                    /* try { // try from 00af5c80 to 00bf5c87 has its CatchHandler @ 00affbb4 */
joined_r0x00af5cc8:
                    /* try { // try from 00af5cc8 to 00bf5ccf has its CatchHandler @ 00affb6c */
  if (p_Var7 == (__tree_node_base *)0x0) {
    p_Var7 = operator_new(0x40);
                    /* try { // try from 00af5c8c to 00bf5c93 has its CatchHandler @ 00affba8 */
    *(undefined8 *)p_Var7 = 0;
    *(undefined8 *)(p_Var7 + 8) = 0;
    *(long **)(p_Var7 + 0x10) = plVar9;
                    /* try { // try from 00af5c98 to 00bf5c9f has its CatchHandler @ 00affb9c */
    *(char **)(p_Var7 + 0x20) = param_5;
    *(__tree_node_base **)(p_Var7 + 0x28) = p_Var7 + 0x28;
    *(__tree_node_base **)(p_Var7 + 0x30) = p_Var7 + 0x28;
    *(undefined8 *)(p_Var7 + 0x38) = 0;
    *plVar3 = (long)p_Var7;
                    /* try { // try from 00af5ca4 to 00bf5cab has its CatchHandler @ 00affb90 */
                    /* try { // try from 00af5cb0 to 00bf5cb7 has its CatchHandler @ 00affb84 */
    p_Var5 = p_Var7;
    if (*(long *)*plVar2 != 0) {
      *plVar2 = *(long *)*plVar2;
      p_Var5 = (__tree_node_base *)*plVar3;
                    /* try { // try from 00af5cbc to 00bf5cc3 has its CatchHandler @ 00affb78 */
    }
                    /* try { // try from 00af5cd4 to 00bf5cdb has its CatchHandler @ 00affb54 */
    std::__ndk1::__tree_balance_after_insert<std::__ndk1::__tree_node_base<void*>*>
              ((__tree_node_base *)plVar2[1],p_Var5);
                    /* try { // try from 00af5ce0 to 00bf5ce7 has its CatchHandler @ 00affb48 */
    plVar2[2] = plVar2[2] + 1;
  }
                    /* try { // try from 00af5cec to 00bf5cf3 has its CatchHandler @ 00affb30 */
  plVar3 = operator_new(0x38);
  plVar3[5] = 0;
  plVar3[6] = 0;
                    /* try { // try from 00af5cf8 to 00bf5cff has its CatchHandler @ 00affb28 */
  plVar3[4] = 0;
  plVar3[1] = (long)(p_Var7 + 0x28);
  lVar6 = *(long *)(p_Var7 + 0x28);
                    /* try { // try from 00af5d04 to 00bf5d17 has its CatchHandler @ 00afffd8 */
  *plVar3 = lVar6;
  *(long **)(lVar6 + 8) = plVar3;
  *(long **)(p_Var7 + 0x28) = plVar3;
                    /* try { // try from 00af5d20 to 00bf5d27 has its CatchHandler @ 00affb20 */
  *(long *)(p_Var7 + 0x38) = *(long *)(p_Var7 + 0x38) + 1;
  plVar9 = plVar3 + 2;
  *plVar9 = 0;
  plVar3[3] = (long)param_4;
  plVar3[4] = (long)plVar3;
                    /* try { // try from 00af5d2c to 00bf5d3f has its CatchHandler @ 00afff94 */
  plVar3[5] = (long)(p_Var7 + 0x28);
  *(undefined1 *)(plVar3 + 6) = 0;
                    /* try { // try from 00af5d40 to 00bf5d5b has its CatchHandler @ 00af560c */
  pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a09c8);
                    /* try { // try from 00af5d5c to 00bf5d63 has its CatchHandler @ 00affb18 */
                    /* try { // try from 00af5d64 to 00bf5ee7 has its CatchHandler @ 00af560c */
  uVar4 = FUN_0056681c(param_1,DAT_010a0290,DAT_010a02a0,param_2,param_3,plVar9);
  pthread_mutex_lock((pthread_mutex_t *)&DAT_010a09c8);
  if ((char)plVar3[6] == '\0') {
    lVar6 = (**(code **)(*(long *)param_1 + 0xa8))(param_1,uVar4);
    *plVar9 = lVar6;
  }
  else {
    plVar9 = (long *)plVar3[4];
    lVar1 = plVar3[5];
    lVar6 = *plVar9;
    *(long *)(lVar6 + 8) = plVar9[1];
    *(long *)plVar9[1] = lVar6;
    *(long *)(lVar1 + 0x10) = *(long *)(lVar1 + 0x10) + -1;
    operator_delete(plVar9);
  }
  pthread_mutex_unlock((pthread_mutex_t *)&DAT_010a09c8);
                    /* WARNING: Could not recover jumptable at 0x00af5df0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*(long *)param_1 + 0xb8))(param_1,uVar4);
  return;
}

~~~
