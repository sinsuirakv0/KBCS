# 00bbc8bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00bbc8bc.md)

## 関数情報

~~~json
{
  "address": "00bbc8bc",
  "name": "FUN_00bbc8bc",
  "size": 324,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9376dd69bfb6fa7e0c50920801985ba9b0430317d224063424da575f575b278b",
  "source_text_sha256": "9376dd69bfb6fa7e0c50920801985ba9b0430317d224063424da575f575b278b"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bde8d0](../00bde/00bde8d0.md)

## 疑似コード 1/1 / UTF-8 1680 bytes

~~~c

void FUN_00bbc8bc(long param_1,long param_2,long param_3,long param_4,int param_5,ulong param_6)

{
  int iVar1;
  long lVar2;
  
  lVar2 = *(long *)(param_2 + 0x10);
  if ((param_6 & 1) == 0) {
    if (*(long *)(param_1 + 8) != *(long *)(lVar2 + 8)) goto LAB_00bbc978;
  }
  else if ((lVar2 != param_1) &&
          (iVar1 = strcmp(*(char **)(param_1 + 8),*(char **)(lVar2 + 8)), iVar1 != 0)) {
LAB_00bbc978:
                    /* try { // try from 00bbc98c to 00cbc9a3 has its CatchHandler @ 00bbd31c */
                    /* WARNING: Could not recover jumptable at 0x00bbc99c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(**(long **)(param_1 + 0x10) + 0x28))();
    return;
  }
                    /* try { // try from 00bbc930 to 00cbc947 has its CatchHandler @ 00bbd2dc */
  *(undefined1 *)(param_2 + 0x4d) = 1;
  if (*(long *)(param_2 + 8) != param_4) {
    return;
  }
  *(undefined1 *)(param_2 + 0x4c) = 1;
  if (*(long *)(param_2 + 0x20) == 0) {
    *(long *)(param_2 + 0x20) = param_3;
    *(int *)(param_2 + 0x30) = param_5;
    *(undefined4 *)(param_2 + 0x3c) = 1;
    iVar1 = param_5;
  }
  else {
    if (*(long *)(param_2 + 0x20) != param_3) {
      *(int *)(param_2 + 0x3c) = *(int *)(param_2 + 0x3c) + 1;
      goto LAB_00bbc9e0;
    }
    iVar1 = *(int *)(param_2 + 0x30);
    if (*(int *)(param_2 + 0x30) == 2) {
      *(int *)(param_2 + 0x30) = param_5;
      iVar1 = param_5;
    }
  }
  if (iVar1 != 1) {
    return;
  }
  if (*(int *)(param_2 + 0x48) != 1) {
    return;
  }
LAB_00bbc9e0:
  *(undefined1 *)(param_2 + 0x4e) = 1;
  return;
}

~~~
