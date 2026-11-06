# 00ad9efc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00ad9efc",
  "name": "FUN_00ad9efc",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "88452dd1eea19638c9f26b352c68bf35a82f262c8eccd2b158e369859ed6652c",
  "source_text_sha256": "88452dd1eea19638c9f26b352c68bf35a82f262c8eccd2b158e369859ed6652c"
}
~~~

## 呼び出し元

- [00ad9b64](../00ad9/00ad9b64.md)

## 呼び出し先

解決済みの記録なし。

## 疑似コード / UTF-8 2499 bytes

~~~c

long * FUN_00ad9efc(long *param_1,long param_2)

{
  long *plVar1;
  long lVar2;
  long *plVar3;
  long *plVar4;
  
  plVar3 = param_1 + 4;
                    /* catch() { ... } // from try @ 00ad9be0 with catch @ 00ad9f14 */
                    /* catch() { ... } // from try @ 00ad9adc with catch @ 00ad9f18 */
  plVar1 = (long *)*plVar3;
                    /* catch() { ... } // from try @ 00ad9d9c with catch @ 00ad9f1c */
  *plVar3 = 0;
                    /* catch() { ... } // from try @ 00ad9dac with catch @ 00ad9f24 */
  if (plVar1 == param_1) {
    lVar2 = 0x20;
    plVar1 = param_1;
LAB_00ad9f3c:
    (**(code **)(*plVar1 + lVar2))();
  }
  else {
                    /* catch() { ... } // from try @ 00ad9df4 with catch @ 00ad9f28 */
    if (plVar1 != (long *)0x0) {
      lVar2 = 0x28;
                    /* catch() { ... } // from try @ 00ad9e04 with catch @ 00ad9f30 */
      goto LAB_00ad9f3c;
    }
  }
  plVar1 = (long *)(param_2 + 0x20);
  lVar2 = *plVar1;
  if (lVar2 == 0) {
LAB_00ad9f68:
    *plVar3 = 0;
  }
  else {
    if (lVar2 != param_2) {
      *plVar3 = lVar2;
      plVar3 = plVar1;
      goto LAB_00ad9f68;
    }
    param_1[4] = (long)param_1;
    (**(code **)(*(long *)*plVar1 + 0x18))((long *)*plVar1,param_1);
  }
  plVar3 = param_1 + 10;
  plVar1 = (long *)*plVar3;
  plVar4 = param_1 + 6;
  *plVar3 = 0;
  if (plVar1 == plVar4) {
    lVar2 = 0x20;
    plVar1 = plVar4;
LAB_00ad9fb4:
    (**(code **)(*plVar1 + lVar2))();
  }
  else if (plVar1 != (long *)0x0) {
    lVar2 = 0x28;
    goto LAB_00ad9fb4;
  }
  plVar1 = (long *)(param_2 + 0x50);
  lVar2 = *plVar1;
  if (lVar2 == 0) {
LAB_00ad9fe4:
    *plVar3 = 0;
  }
  else {
    if (lVar2 != param_2 + 0x30) {
      *plVar3 = lVar2;
      plVar3 = plVar1;
      goto LAB_00ad9fe4;
    }
    *plVar3 = (long)plVar4;
    (**(code **)(*(long *)*plVar1 + 0x18))((long *)*plVar1,plVar4);
  }
  plVar3 = param_1 + 0x10;
  plVar1 = (long *)*plVar3;
  plVar4 = param_1 + 0xc;
  *plVar3 = 0;
  if (plVar1 == plVar4) {
    lVar2 = 0x20;
    plVar1 = plVar4;
  }
  else {
    if (plVar1 == (long *)0x0) goto LAB_00ada03c;
    lVar2 = 0x28;
  }
  (**(code **)(*plVar1 + lVar2))();
LAB_00ada03c:
  plVar1 = (long *)(param_2 + 0x80);
  lVar2 = *plVar1;
  if (lVar2 != 0) {
    if (lVar2 == param_2 + 0x60) {
      *plVar3 = (long)plVar4;
      (**(code **)(*(long *)*plVar1 + 0x18))((long *)*plVar1,plVar4);
      return param_1;
    }
    *plVar3 = lVar2;
    plVar3 = plVar1;
  }
  *plVar3 = 0;
  return param_1;
}

~~~
