# 005dfdec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](005dfdec.md)

## 関数情報

~~~json
{
  "address": "005dfdec",
  "name": "FUN_005dfdec",
  "size": 196,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4335960973e81ebaa8c02f65a5597dfcb653e7d0ece2f9c6c6d1825f183d0478",
  "source_text_sha256": "4335960973e81ebaa8c02f65a5597dfcb653e7d0ece2f9c6c6d1825f183d0478"
}
~~~
## 呼び出し元

- [005e1a5c](../005e1/005e1a5c.md)
- [006d6d04](../006d6/006d6d04.md)
- [00713660](../00713/00713660.md)
- [007317b0](../00731/007317b0.md)
- [0079bdf0](../0079b/0079bdf0.md)
- [007e228c](../007e2/007e228c.md)
- [009121c4](../00912/009121c4.md)
- [0099a654](../0099a/0099a654.md)
- [009a9ce0](../009a9/009a9ce0.md)
- [00a806b4](../00a80/00a806b4.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [00bdaf40](../00bda/00bdaf40.md)

## 疑似コード 1/1 / UTF-8 1547 bytes

~~~c

long * FUN_005dfdec(long *param_1,int *param_2)

{
  int iVar1;
  long *plVar2;
  long *plVar3;
  long *plVar4;
  long *plVar5;
  
                    /* try { // try from 005dfe04 to 006dfe0b has its CatchHandler @ 005dff0c */
  iVar1 = *param_2;
  plVar4 = param_1 + 1;
  plVar3 = (long *)*plVar4;
  plVar5 = plVar4;
  if ((long *)*plVar4 != (long *)0x0) {
    do {
      while (plVar2 = plVar3, plVar4 = plVar2, iVar1 < *(int *)((long)plVar2 + 0x1c)) {
                    /* try { // try from 005dfe1c to 006dfe27 has its CatchHandler @ 005dfef0 */
        plVar3 = (long *)*plVar2;
        plVar5 = plVar2;
        if ((long *)*plVar2 == (long *)0x0) goto LAB_005dfe4c;
      }
      if (iVar1 <= *(int *)((long)plVar2 + 0x1c)) goto LAB_005dfe98;
      plVar3 = (long *)plVar2[1];
    } while ((long *)plVar2[1] != (long *)0x0);
    plVar5 = plVar2 + 1;
  }
LAB_005dfe4c:
                    /* try { // try from 005dfe54 to 006dfe5f has its CatchHandler @ 005dfed4 */
  plVar2 = operator_new(0x28);
  *plVar2 = 0;
  plVar2[1] = 0;
                    /* try { // try from 005dfe60 to 006dff23 has its CatchHandler @ 005dfd64 */
  plVar2[2] = (long)plVar4;
  *plVar5 = (long)plVar2;
  plVar4 = (long *)*param_1;
  *(int *)((long)plVar2 + 0x1c) = iVar1;
  *(undefined4 *)(plVar2 + 4) = 0;
  plVar3 = plVar2;
  if (*plVar4 != 0) {
    *param_1 = *plVar4;
    plVar3 = (long *)*plVar5;
  }
  FUN_00419064(param_1[1],plVar3);
  param_1[2] = param_1[2] + 1;
LAB_005dfe98:
  return plVar2 + 4;
}

~~~
