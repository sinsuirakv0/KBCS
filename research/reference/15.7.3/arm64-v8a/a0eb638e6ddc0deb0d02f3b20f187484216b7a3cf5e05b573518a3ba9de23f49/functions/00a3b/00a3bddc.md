# 00a3bddc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00a3bddc",
  "name": "FUN_00a3bddc",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e4f63d3d92b2d7da3765b5aa8405437a901c5e308177673d2e77e15faae6f5db",
  "source_text_sha256": "e4f63d3d92b2d7da3765b5aa8405437a901c5e308177673d2e77e15faae6f5db"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)

## 疑似コード / UTF-8 1044 bytes

~~~c

void FUN_00a3bddc(long param_1)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  undefined8 *puVar3;
  
  puVar2 = *(undefined8 **)(param_1 + 0x28);
  if (puVar2 != (undefined8 *)0x0) {
    puVar3 = *(undefined8 **)(param_1 + 0x30);
    puVar1 = puVar2;
    if (puVar3 != puVar2) {
      do {
        puVar3 = puVar3 + -3;
        if ((void *)*puVar3 != (void *)0x0) {
          _ZdlPv((void *)*puVar3);
        }
      } while (puVar3 != puVar2);
      puVar1 = *(undefined8 **)(param_1 + 0x28);
    }
    *(undefined8 **)(param_1 + 0x30) = puVar2;
    _ZdlPv(puVar1);
  }
  puVar2 = *(undefined8 **)(param_1 + 0x10);
  if (puVar2 == (undefined8 *)0x0) {
    return;
  }
  puVar3 = *(undefined8 **)(param_1 + 0x18);
  puVar1 = puVar2;
  if (puVar3 != puVar2) {
    do {
      puVar3 = puVar3 + -3;
      if ((void *)*puVar3 != (void *)0x0) {
        _ZdlPv((void *)*puVar3);
      }
    } while (puVar3 != puVar2);
    puVar1 = *(undefined8 **)(param_1 + 0x10);
  }
  *(undefined8 **)(param_1 + 0x18) = puVar2;
  _ZdlPv(puVar1);
  return;
}

~~~
