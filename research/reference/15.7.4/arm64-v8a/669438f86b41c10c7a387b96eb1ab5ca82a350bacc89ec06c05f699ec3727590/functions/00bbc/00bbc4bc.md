# 00bbc4bc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

<!-- kbcs-version-previous -->
**別版の対応** [v15.7.2 `00bbc3b0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bbc/00bbc3b0.md)
<!-- /kbcs-version-previous -->

## 関数情報

~~~json
{
  "address": "00bbc4bc",
  "name": "FUN_00bbc4bc",
  "size": 432,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "32fa779c2f54bd1397fca2c97ffabe5012b2d02a149589f0e3ebeaa1ac5a1dd3",
  "source_text_sha256": "32fa779c2f54bd1397fca2c97ffabe5012b2d02a149589f0e3ebeaa1ac5a1dd3"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde9d0](../00bde/00bde9d0.md)

## 疑似コード / UTF-8 2866 bytes

~~~c

void FUN_00bbc4bc(long param_1,long *param_2,long param_3,ulong param_4,uint param_5)

{
  int iVar1;
  long lVar2;
  char *__s1;
  
                    /* try { // try from 00bbc4c8 to 00cbc4d3 has its CatchHandler @ 00bbd318 */
  lVar2 = param_2[2];
  if ((param_5 & 1) == 0) {
                    /* try { // try from 00bbc59c to 00cbc5a3 has its CatchHandler @ 00bbd150 */
    if (*(long *)(param_1 + 8) != *(long *)(lVar2 + 8)) {
      if (*(long *)(param_1 + 8) != *(long *)(*param_2 + 8)) {
LAB_00bbc5bc:
                    /* try { // try from 00bbc5c4 to 00cbc5d3 has its CatchHandler @ 00bbd140 */
                    /* try { // try from 00bbc5d4 to 00cbc5e7 has its CatchHandler @ 00bbd128 */
                    /* WARNING: Could not recover jumptable at 0x00bbc5e8. Too many branches */
                    /* WARNING: Treating indirect jump as call */
        (**(code **)(**(long **)(param_1 + 0x10) + 0x30))
                  (*(long **)(param_1 + 0x10),param_2,param_3,param_4,param_5 & 1);
        return;
      }
LAB_00bbc530:
      if ((param_2[4] == param_3) || (param_2[5] == param_3)) {
                    /* try { // try from 00bbc610 to 00cbc617 has its CatchHandler @ 00bbd3c4 */
        if ((int)param_4 != 1) {
          return;
        }
                    /* try { // try from 00bbc618 to 00cbc693 has its CatchHandler @ 00bbd424 */
        *(undefined4 *)(param_2 + 7) = 1;
        return;
      }
      *(int *)(param_2 + 7) = (int)param_4;
      if (*(int *)((long)param_2 + 0x44) != 4) {
        *(undefined2 *)((long)param_2 + 0x4c) = 0;
        (**(code **)(**(long **)(param_1 + 0x10) + 0x28))
                  (*(long **)(param_1 + 0x10),param_2,param_3,param_3,1,param_5 & 1);
        if (*(char *)((long)param_2 + 0x4d) == '\0') {
          *(undefined4 *)((long)param_2 + 0x44) = 4;
        }
        else {
          *(undefined4 *)((long)param_2 + 0x44) = 3;
                    /* try { // try from 00bbc594 to 00cbc59b has its CatchHandler @ 00bbd32c */
          if (*(char *)((long)param_2 + 0x4c) != '\0') {
            return;
          }
        }
      }
      param_2[5] = param_3;
      *(int *)(param_2 + 8) = (int)param_2[8] + 1;
      if (*(int *)((long)param_2 + 0x3c) != 1) {
        return;
      }
      if ((int)param_2[6] != 2) {
        return;
      }
      *(undefined1 *)((long)param_2 + 0x4e) = 1;
      return;
    }
  }
  else if (lVar2 != param_1) {
    __s1 = *(char **)(param_1 + 8);
    param_4 = param_4 & 0xffffffff;
    iVar1 = strcmp(__s1,*(char **)(lVar2 + 8));
    if (iVar1 != 0) {
      if ((*param_2 != param_1) && (iVar1 = strcmp(__s1,*(char **)(*param_2 + 8)), iVar1 != 0))
      goto LAB_00bbc5bc;
      goto LAB_00bbc530;
    }
  }
  if ((param_2[1] == param_3) && (*(int *)((long)param_2 + 0x34) != 1)) {
    *(int *)((long)param_2 + 0x34) = (int)param_4;
  }
  return;
}

~~~
