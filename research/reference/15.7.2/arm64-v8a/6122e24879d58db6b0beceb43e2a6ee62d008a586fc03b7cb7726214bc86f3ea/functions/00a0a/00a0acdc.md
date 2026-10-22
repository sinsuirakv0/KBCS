# 00a0acdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a0acdc.md)

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
  "source_sha256": "f69a4a059361db539878a2cdd97bd8459c34bd19fe695adbc44e5dd98b18834a",
  "source_text_sha256": "f69a4a059361db539878a2cdd97bd8459c34bd19fe695adbc44e5dd98b18834a"
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
## 疑似コード 1/1 / UTF-8 2374 bytes

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
