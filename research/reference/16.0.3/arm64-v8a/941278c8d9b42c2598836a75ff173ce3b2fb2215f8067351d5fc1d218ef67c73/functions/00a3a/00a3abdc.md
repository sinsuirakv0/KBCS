# 00a3abdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00a3abdc",
  "name": "FUN_00a3abdc",
  "size": 168,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "471eb7a49fc555a6caafbff2d89c09bcc9310a1576dec1ae428c944f7bdf094e",
  "source_text_sha256": "471eb7a49fc555a6caafbff2d89c09bcc9310a1576dec1ae428c944f7bdf094e"
}
~~~

## 呼び出し元

- [00a3aa18](../00a3a/00a3aa18.md)

## 呼び出し先

- [00c58f50](../00c58/00c58f50.md)

## 疑似コード / UTF-8 1106 bytes

~~~c

void FUN_00a3abdc(undefined8 param_1,long param_2,long param_3)

{
  void *pvVar1;
  void *pvVar2;
  void *pvVar3;
  
  for (; param_2 != param_3; param_2 = param_2 + 0x80) {
    pvVar1 = *(void **)(param_2 + 0x60);
    if (pvVar1 != (void *)0x0) {
      *(void **)(param_2 + 0x68) = pvVar1;
      _ZdlPv(pvVar1);
    }
    pvVar1 = *(void **)(param_2 + 0x38);
    if (pvVar1 != (void *)0x0) {
      pvVar3 = *(void **)(param_2 + 0x40);
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
        pvVar2 = *(void **)(param_2 + 0x38);
      }
      *(void **)(param_2 + 0x40) = pvVar1;
      _ZdlPv(pvVar2);
    }
  }
  return;
}

~~~
