# 00b3affc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00b3affc",
  "name": "FUN_00b3affc",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "16e3c1ea25b4784a3377ba6f42321a2e9750c75f17af8706fac2732f65183eb5",
  "source_text_sha256": "16e3c1ea25b4784a3377ba6f42321a2e9750c75f17af8706fac2732f65183eb5"
}
~~~

## 呼び出し元

- [00b38f10](../00b38/00b38f10.md)
- [00b3affc](../00b3a/00b3affc.md)

## 呼び出し先

- [00b3affc](../00b3a/00b3affc.md)
- [00c57eb0](../00c57/00c57eb0.md)

## 疑似コード / UTF-8 2023 bytes

~~~c

void FUN_00b3affc(undefined8 param_1,undefined8 *param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  
  if (param_2 == (undefined8 *)0x0) {
    return;
  }
  FUN_00b3affc(param_1,*param_2);
  FUN_00b3affc(param_1,param_2[1]);
                    /* try { // try from 00b3b028 to 00c3b02f has its CatchHandler @ 00b3b034 */
  plVar1 = (long *)param_2[0x12];
  plVar2 = param_2 + 0xe;
                    /* catch() { ... } // from try @ 00b3ad80 with catch @ 00b3b030
                       try { // try from 00b3b030 to 00c3b0bb has its CatchHandler @ 00b3aac8 */
  plVar3 = param_2 + 8;
                    /* catch() { ... } // from try @ 00b3b028 with catch @ 00b3b034 */
  if (plVar1 == plVar2) {
                    /* catch() { ... } // from try @ 00b3ad8c with catch @ 00b3b04c */
    lVar4 = 0x20;
LAB_00b3b054:
    (**(code **)(*plVar2 + lVar4))();
  }
  else if (plVar1 != (long *)0x0) {
    lVar4 = 0x28;
    plVar2 = plVar1;
    goto LAB_00b3b054;
  }
                    /* catch() { ... } // from try @ 00b3af80 with catch @ 00b3b060 */
  plVar2 = (long *)param_2[0xc];
  if (plVar2 == plVar3) {
                    /* catch() { ... } // from try @ 00b3af6c with catch @ 00b3b078 */
    lVar4 = 0x20;
                    /* catch() { ... } // from try @ 00b3acc8 with catch @ 00b3b07c */
  }
  else {
    if (plVar2 == (long *)0x0) goto LAB_00b3b08c;
    lVar4 = 0x28;
    plVar3 = plVar2;
  }
                    /* catch() { ... } // from try @ 00b3ac84 with catch @ 00b3b080 */
                    /* catch() { ... } // from try @ 00b3ab58 with catch @ 00b3b084 */
                    /* catch() { ... } // from try @ 00b3acdc with catch @ 00b3b088
                       catch() { ... } // from try @ 00b3ae84 with catch @ 00b3b088
                       catch() { ... } // from try @ 00b3afb4 with catch @ 00b3b088 */
  (**(code **)(*plVar3 + lVar4))();
LAB_00b3b08c:
  if ((*(byte *)(param_2 + 4) & 1) != 0) {
    _ZdlPv((void *)param_2[6]);
  }
  _ZdlPv(param_2);
  return;
}

~~~
