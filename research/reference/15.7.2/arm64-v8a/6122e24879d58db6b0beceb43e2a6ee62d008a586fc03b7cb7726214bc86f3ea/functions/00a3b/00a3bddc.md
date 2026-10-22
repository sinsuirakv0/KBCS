# 00a3bddc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00a3bddc.md)

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
  "source_sha256": "a6a5d1f4a3cb69e32b8925818767039308816e6dfc9529eb4c3339bd7f4a3059",
  "source_text_sha256": "a6a5d1f4a3cb69e32b8925818767039308816e6dfc9529eb4c3339bd7f4a3059"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf60](../00bda/00bdaf60.md)

## 疑似コード 1/1 / UTF-8 1124 bytes

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
          operator_delete((void *)*puVar3);
        }
      } while (puVar3 != puVar2);
      puVar1 = *(undefined8 **)(param_1 + 0x28);
    }
    *(undefined8 **)(param_1 + 0x30) = puVar2;
    operator_delete(puVar1);
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
        operator_delete((void *)*puVar3);
      }
    } while (puVar3 != puVar2);
    puVar1 = *(undefined8 **)(param_1 + 0x10);
  }
  *(undefined8 **)(param_1 + 0x18) = puVar2;
  operator_delete(puVar1);
  return;
}

~~~
