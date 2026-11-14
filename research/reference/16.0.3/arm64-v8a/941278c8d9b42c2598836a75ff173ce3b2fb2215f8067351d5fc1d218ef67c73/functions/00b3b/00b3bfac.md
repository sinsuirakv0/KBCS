# 00b3bfac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00b3bfac",
  "name": "FUN_00b3bfac",
  "size": 224,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a711561be0e9413fb360f6317e63e0bda80508af5ec4f8f184b9d33fcf0ab15e",
  "source_text_sha256": "a711561be0e9413fb360f6317e63e0bda80508af5ec4f8f184b9d33fcf0ab15e"
}
~~~

## 呼び出し元

- [00b39f98](../00b39/00b39f98.md)
- [00b3bfac](../00b3b/00b3bfac.md)

## 呼び出し先

- [00b3bfac](../00b3b/00b3bfac.md)
- [00c58f50](../00c58/00c58f50.md)

## 疑似コード / UTF-8 1800 bytes

~~~c

void FUN_00b3bfac(undefined8 param_1,undefined8 *param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  
  if (param_2 == (undefined8 *)0x0) {
    return;
  }
                    /* try { // try from 00b3bfb4 to 00c3bfc3 has its CatchHandler @ 00b3c0c0 */
                    /* try { // try from 00b3bfc8 to 00c3bfdf has its CatchHandler @ 00b3c0a8 */
  FUN_00b3bfac(param_1,*param_2);
  FUN_00b3bfac(param_1,param_2[1]);
  plVar1 = (long *)param_2[0x18];
  plVar3 = param_2 + 0x14;
  if (plVar1 == plVar3) {
    lVar4 = 0x20;
                    /* try { // try from 00b3bffc to 00c3c027 has its CatchHandler @ 00b3c0d0 */
LAB_00b3c000:
    (**(code **)(*plVar3 + lVar4))();
  }
  else if (plVar1 != (long *)0x0) {
    lVar4 = 0x28;
    plVar3 = plVar1;
    goto LAB_00b3c000;
  }
  plVar2 = (long *)param_2[0x12];
  plVar3 = param_2 + 0xe;
  plVar1 = param_2 + 8;
  if (plVar2 == plVar3) {
    lVar4 = 0x20;
LAB_00b3c034:
    (**(code **)(*plVar3 + lVar4))();
  }
  else if (plVar2 != (long *)0x0) {
    lVar4 = 0x28;
    plVar3 = plVar2;
    goto LAB_00b3c034;
  }
  plVar3 = (long *)param_2[0xc];
  if (plVar3 == plVar1) {
    lVar4 = 0x20;
  }
  else {
    if (plVar3 == (long *)0x0) goto LAB_00b3c06c;
    lVar4 = 0x28;
    plVar1 = plVar3;
  }
  (**(code **)(*plVar1 + lVar4))();
LAB_00b3c06c:
                    /* try { // try from 00b3c070 to 00c3c077 has its CatchHandler @ 00b3c07c */
  if ((*(byte *)(param_2 + 4) & 1) != 0) {
                    /* catch() { ... } // from try @ 00b3bdc8 with catch @ 00b3c078
                       try { // try from 00b3c078 to 00c3c103 has its CatchHandler @ 00b3bb10 */
    _ZdlPv((void *)param_2[6]);
  }
                    /* catch() { ... } // from try @ 00b3c070 with catch @ 00b3c07c */
  _ZdlPv(param_2);
  return;
}

~~~
