# 00acabc8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00acabc8",
  "name": "FUN_00acabc8",
  "size": 244,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cbf5375189537341c74eb5ffc1547e923419cdb5b1dc0b79d793b3329b139605",
  "source_text_sha256": "cbf5375189537341c74eb5ffc1547e923419cdb5b1dc0b79d793b3329b139605"
}
~~~

## 呼び出し元

- [00aca940](../00aca/00aca940.md)

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

## 疑似コード / UTF-8 1829 bytes

~~~c

void FUN_00acabc8(undefined8 param_1,undefined8 *param_2,undefined8 *param_3,undefined8 *param_4)

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
      if ((*(byte *)(param_2 + 9) & 1) == 0) {
        if ((*(byte *)(param_2 + 6) & 1) == 0) goto LAB_00acac78;
LAB_00acac94:
        _ZdlPv((void *)param_2[8]);
        __ptr = (void *)param_2[3];
      }
      else {
        _ZdlPv((void *)param_2[0xb]);
        if ((*(byte *)(param_2 + 6) & 1) != 0) goto LAB_00acac94;
LAB_00acac78:
        __ptr = (void *)param_2[3];
      }
      if (__ptr != (void *)0x0) {
                    /* try { // try from 00acaca4 to 00bcacaf has its CatchHandler @ 00acd6cc */
        param_2[4] = __ptr;
        _ZdlPv(__ptr);
      }
    }
  }
  return;
}

~~~
