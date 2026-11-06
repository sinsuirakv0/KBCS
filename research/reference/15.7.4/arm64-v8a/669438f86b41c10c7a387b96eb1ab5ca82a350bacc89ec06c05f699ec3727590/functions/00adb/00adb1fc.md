# 00adb1fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00adb1fc",
  "name": "FUN_00adb1fc",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "51f89bee2858cff0913ea4bfcba00185b89e3358c4f52dfb2a3a740401024cf7",
  "source_text_sha256": "51f89bee2858cff0913ea4bfcba00185b89e3358c4f52dfb2a3a740401024cf7"
}
~~~

## 呼び出し元

- [00ad9110](../00ad9/00ad9110.md)
- [00adb1fc](../00adb/00adb1fc.md)

## 呼び出し先

- [00adb1fc](../00adb/00adb1fc.md)
- [00bdb060](../00bdb/00bdb060.md)

## 疑似コード / UTF-8 1075 bytes

~~~c

void FUN_00adb1fc(undefined8 param_1,undefined8 *param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  
  if (param_2 == (undefined8 *)0x0) {
    return;
  }
                    /* try { // try from 00adb214 to 00bdb217 has its CatchHandler @ 00adb900 */
  FUN_00adb1fc(param_1,*param_2);
  FUN_00adb1fc(param_1,param_2[1]);
  plVar1 = (long *)param_2[0x12];
  plVar2 = param_2 + 0xe;
  plVar3 = param_2 + 8;
  if (plVar1 == plVar2) {
    lVar4 = 0x20;
LAB_00adb254:
    (**(code **)(*plVar2 + lVar4))();
  }
  else if (plVar1 != (long *)0x0) {
    lVar4 = 0x28;
    plVar2 = plVar1;
    goto LAB_00adb254;
  }
  plVar2 = (long *)param_2[0xc];
  if (plVar2 == plVar3) {
    lVar4 = 0x20;
  }
  else {
    if (plVar2 == (long *)0x0) goto LAB_00adb28c;
    lVar4 = 0x28;
    plVar3 = plVar2;
  }
  (**(code **)(*plVar3 + lVar4))();
LAB_00adb28c:
  if ((*(byte *)(param_2 + 4) & 1) != 0) {
                    /* try { // try from 00adb298 to 00bdb2a3 has its CatchHandler @ 00adb8d0 */
    _ZdlPv((void *)param_2[6]);
  }
  _ZdlPv(param_2);
  return;
}

~~~
