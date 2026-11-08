# 00bbcac8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00bbcac8",
  "name": "FUN_00bbcac8",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fcb55918311e486ff2611679b123a6c6928c55ac1a9ed8063237c4eb368f959b",
  "source_text_sha256": "fcb55918311e486ff2611679b123a6c6928c55ac1a9ed8063237c4eb368f959b"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde980](../00bde/00bde980.md)

## 疑似コード / UTF-8 1713 bytes

~~~c

void FUN_00bbcac8(long param_1,long param_2,long param_3,long param_4,int param_5,uint param_6)

{
  int iVar1;
  long lVar2;
  
  lVar2 = *(long *)(param_2 + 0x10);
  if ((param_6 & 1) == 0) {
    if (*(long *)(param_1 + 8) != *(long *)(lVar2 + 8)) {
      return;
    }
  }
  else {
                    /* try { // try from 00bbcb20 to 00cbcb23 has its CatchHandler @ 00bbd2c0 */
                    /* try { // try from 00bbcb24 to 00cbcb6b has its CatchHandler @ 00bbb8ec */
    if ((lVar2 != param_1) &&
       (iVar1 = strcmp(*(char **)(param_1 + 8),*(char **)(lVar2 + 8)), iVar1 != 0)) {
      return;
    }
  }
  *(undefined1 *)(param_2 + 0x4d) = 1;
  if (*(long *)(param_2 + 8) == param_4) {
    *(undefined1 *)(param_2 + 0x4c) = 1;
    if (*(long *)(param_2 + 0x20) == 0) {
      *(long *)(param_2 + 0x20) = param_3;
      *(int *)(param_2 + 0x30) = param_5;
      *(undefined4 *)(param_2 + 0x3c) = 1;
      iVar1 = param_5;
    }
    else {
                    /* try { // try from 00bbcb6c to 00cbcb73 has its CatchHandler @ 00bbd2e8 */
      if (*(long *)(param_2 + 0x20) != param_3) {
                    /* try { // try from 00bbcb74 to 00cbcb7b has its CatchHandler @ 00bbd0d0 */
        *(int *)(param_2 + 0x3c) = *(int *)(param_2 + 0x3c) + 1;
        goto LAB_00bbcbc0;
      }
      iVar1 = *(int *)(param_2 + 0x30);
      if (*(int *)(param_2 + 0x30) == 2) {
                    /* try { // try from 00bbcba8 to 00cbcbbb has its CatchHandler @ 00bbd0cc */
        *(int *)(param_2 + 0x30) = param_5;
        iVar1 = param_5;
      }
    }
    if ((iVar1 == 1) && (*(int *)(param_2 + 0x48) == 1)) {
LAB_00bbcbc0:
      *(undefined1 *)(param_2 + 0x4e) = 1;
      return;
    }
  }
  return;
}

~~~
