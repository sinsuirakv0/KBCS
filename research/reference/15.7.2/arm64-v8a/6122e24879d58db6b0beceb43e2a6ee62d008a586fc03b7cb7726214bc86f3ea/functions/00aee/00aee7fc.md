# 00aee7fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00aee7fc.md)

## 関数情報

~~~json
{
  "address": "00aee7fc",
  "name": "FUN_00aee7fc",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "20468af23f3ecddda8cb4a7860ce461927c25dd0c55392e21369c25b2354882c",
  "source_text_sha256": "20468af23f3ecddda8cb4a7860ce461927c25dd0c55392e21369c25b2354882c"
}
~~~
## 呼び出し元

- [00aee28c](../00aee/00aee28c.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード 1/1 / UTF-8 725 bytes

~~~c

void FUN_00aee7fc(long *param_1)

{
  void *pvVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  
  puVar3 = (undefined8 *)*DAT_010a09b0;
  puVar2 = DAT_010a09b0 + 1;
  if (puVar3 != (undefined8 *)*puVar2) {
    do {
      puVar2 = puVar3 + 1;
      (**(code **)(*param_1 + 0xb0))(param_1,*puVar3);
      puVar3 = puVar2;
    } while (puVar2 != (undefined8 *)DAT_010a09b0[1]);
    puVar2 = DAT_010a09b0 + 1;
  }
  puVar3 = DAT_010a09b0;
  if (DAT_010a09b0 != (undefined8 *)0x0) {
    pvVar1 = (void *)*DAT_010a09b0;
    if (pvVar1 != (void *)0x0) {
      *puVar2 = pvVar1;
      operator_delete(pvVar1);
    }
    operator_delete(puVar3);
  }
  DAT_010a09b0 = (undefined8 *)0x0;
  return;
}

~~~
