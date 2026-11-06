# 00acac0c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00acac0c.md)

## 関数情報

~~~json
{
  "address": "00acac0c",
  "name": "FUN_00acac0c",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f66f8c502ba04a4bfa4a7ff743ebc796731b8525eac42ce4fc20f591744f9a8c",
  "source_text_sha256": "f66f8c502ba04a4bfa4a7ff743ebc796731b8525eac42ce4fc20f591744f9a8c"
}
~~~
## 呼び出し元

- [00aca984](../00aca/00aca984.md)

## 呼び出し先

- [00bdb060](../00bdb/00bdb060.md)

## 疑似コード 1/1 / UTF-8 1926 bytes

~~~c

void FUN_00acac0c(undefined8 param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4)

{
  undefined1 uVar1;
  void *__ptr;
  undefined8 *puVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  
  puVar2 = param_2;
  if (param_2 != param_3) {
    do {
      uVar1 = *(undefined1 *)(puVar2 + 2);
      uVar4 = puVar2[1];
      uVar3 = *puVar2;
      param_4[4] = 0;
      param_4[5] = 0;
      param_4[3] = 0;
      *(undefined1 *)(param_4 + 2) = uVar1;
      param_4[1] = uVar4;
      *param_4 = uVar3;
      uVar3 = puVar2[3];
      param_4[4] = puVar2[4];
      param_4[3] = uVar3;
      param_4[5] = puVar2[5];
      uVar4 = puVar2[7];
      uVar3 = puVar2[6];
      puVar2[3] = 0;
      puVar2[4] = 0;
      puVar2[5] = 0;
      param_4[8] = puVar2[8];
      param_4[7] = uVar4;
      param_4[6] = uVar3;
      uVar4 = puVar2[10];
      uVar3 = puVar2[9];
      puVar2[7] = 0;
      puVar2[8] = 0;
      puVar2[6] = 0;
      param_4[0xb] = puVar2[0xb];
      param_4[10] = uVar4;
      param_4[9] = uVar3;
      param_4 = param_4 + 0xc;
      puVar2[10] = 0;
      puVar2[0xb] = 0;
      puVar2[9] = 0;
      puVar2 = puVar2 + 0xc;
    } while (puVar2 != param_3);
    for (; param_2 != param_3; param_2 = param_2 + 0xc) {
                    /* try { // try from 00acacb0 to 00bcacbb has its CatchHandler @ 00acd710 */
      if ((*(byte *)(param_2 + 9) & 1) == 0) {
        if ((*(byte *)(param_2 + 6) & 1) == 0) goto LAB_00acacbc;
LAB_00acacd8:
        _ZdlPv((void *)param_2[8]);
        __ptr = (void *)param_2[3];
      }
      else {
        _ZdlPv((void *)param_2[0xb]);
        if ((*(byte *)(param_2 + 6) & 1) != 0) goto LAB_00acacd8;
LAB_00acacbc:
                    /* try { // try from 00acacbc to 00bcc0ab has its CatchHandler @ 00ac9134 */
        __ptr = (void *)param_2[3];
      }
      if (__ptr != (void *)0x0) {
        param_2[4] = __ptr;
        _ZdlPv(__ptr);
      }
    }
  }
  return;
}

~~~
