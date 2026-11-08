# 00aee7fc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

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
  "source_sha256": "127f3aecc5ccaf514eb262fa56069a8ddb38f2993ce75f5c89d721732e14817b",
  "source_text_sha256": "127f3aecc5ccaf514eb262fa56069a8ddb38f2993ce75f5c89d721732e14817b"
}
~~~

## 呼び出し元

- [00aee28c](../00aee/00aee28c.md)

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード / UTF-8 671 bytes

~~~c

void FUN_00aee7fc(long *param_1)

{
  void *__ptr;
  undefined8 *puVar1;
  undefined8 *puVar2;
  
  puVar2 = (undefined8 *)*DAT_010a09b0;
  puVar1 = DAT_010a09b0 + 1;
  if (puVar2 != (undefined8 *)*puVar1) {
    do {
      puVar1 = puVar2 + 1;
      (**(code **)(*param_1 + 0xb0))(param_1,*puVar2);
      puVar2 = puVar1;
    } while (puVar1 != (undefined8 *)DAT_010a09b0[1]);
    puVar1 = DAT_010a09b0 + 1;
  }
  puVar2 = DAT_010a09b0;
  if (DAT_010a09b0 != (undefined8 *)0x0) {
    __ptr = (void *)*DAT_010a09b0;
    if (__ptr != (void *)0x0) {
      *puVar1 = __ptr;
      _ZdlPv(__ptr);
    }
    _ZdlPv(puVar2);
  }
  DAT_010a09b0 = (undefined8 *)0x0;
  return;
}

~~~
