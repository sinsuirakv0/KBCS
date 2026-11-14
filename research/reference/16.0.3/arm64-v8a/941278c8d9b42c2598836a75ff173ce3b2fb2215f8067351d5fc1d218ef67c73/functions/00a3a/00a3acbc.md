# 00a3acbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00a3acbc",
  "name": "FUN_00a3acbc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ead6bc07aee2e5737c5e784daceafe1ad58d5133c3ceb01eb66559b06cf1fd65",
  "source_text_sha256": "ead6bc07aee2e5737c5e784daceafe1ad58d5133c3ceb01eb66559b06cf1fd65"
}
~~~

## 呼び出し元

- [00a3ac84](../00a3a/00a3ac84.md)

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)

## 疑似コード / UTF-8 1266 bytes

~~~c

void FUN_00a3acbc(undefined8 param_1,undefined8 param_2,long param_3,undefined8 param_4,long param_5
                 )

{
  void *pvVar1;
  void *pvVar2;
  void *pvVar3;
  
  for (; param_3 != param_5; param_3 = param_3 + -0x80) {
    pvVar1 = *(void **)(param_3 + -0x20);
    if (pvVar1 != (void *)0x0) {
      *(void **)(param_3 + -0x18) = pvVar1;
      _ZdlPv(pvVar1);
    }
    pvVar1 = *(void **)(param_3 + -0x48);
    if (pvVar1 != (void *)0x0) {
                    /* try { // try from 00a3ad10 to 00b3ad17 has its CatchHandler @ 00a3b0f4 */
      pvVar3 = *(void **)(param_3 + -0x40);
      pvVar2 = pvVar1;
      if (pvVar3 != pvVar1) {
        do {
          pvVar2 = *(void **)((long)pvVar3 + -0x18);
          if (pvVar2 != (void *)0x0) {
            *(void **)((long)pvVar3 + -0x10) = pvVar2;
            _ZdlPv(pvVar2);
          }
          pvVar2 = *(void **)((long)pvVar3 + -0x30);
          if (pvVar2 != (void *)0x0) {
            *(void **)((long)pvVar3 + -0x28) = pvVar2;
            _ZdlPv(pvVar2);
          }
          pvVar3 = (void *)((long)pvVar3 + -0x88);
        } while (pvVar3 != pvVar1);
        pvVar2 = *(void **)(param_3 + -0x48);
      }
      *(void **)(param_3 + -0x40) = pvVar1;
      _ZdlPv(pvVar2);
    }
  }
  return;
}

~~~
