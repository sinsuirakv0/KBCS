# 00add5ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00add5ac.md)

## 関数情報

~~~json
{
  "address": "00add5ac",
  "name": "FUN_00add5ac",
  "size": 352,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "07c5be8a6f33e5e186309bd5860aedb379083a641ff1c071897b7e704910a8d8",
  "source_text_sha256": "07c5be8a6f33e5e186309bd5860aedb379083a641ff1c071897b7e704910a8d8"
}
~~~
## 呼び出し元

- [00ade630](../00ade/00ade630.md)

## 呼び出し先

- [00464a64](../00464/00464a64.md)

## 疑似コード 1/1 / UTF-8 1402 bytes

~~~c

void FUN_00add5ac(undefined4 *param_1,undefined8 param_2)

{
  undefined4 uVar1;
  int iVar2;
  
  uVar1 = FUN_00464a64(param_2,0);
  *param_1 = uVar1;
  iVar2 = FUN_00464a64(param_2,1);
  *(bool *)(param_1 + 1) = iVar2 == 1;
  uVar1 = FUN_00464a64(param_2,3);
  param_1[2] = uVar1;
                    /* catch() { ... } // from try @ 00add490 with catch @ 00add5fc */
  uVar1 = FUN_00464a64(param_2,4);
  param_1[3] = uVar1;
  uVar1 = FUN_00464a64(param_2,5);
  param_1[4] = uVar1;
  uVar1 = FUN_00464a64(param_2,6);
  param_1[5] = uVar1;
  uVar1 = FUN_00464a64(param_2,7);
  param_1[6] = uVar1;
  uVar1 = FUN_00464a64(param_2,8);
  param_1[10] = uVar1;
  uVar1 = FUN_00464a64(param_2,9);
  param_1[0xb] = uVar1;
  uVar1 = FUN_00464a64(param_2,10);
  param_1[0xd] = uVar1;
  uVar1 = FUN_00464a64(param_2,0xb);
  param_1[0xc] = uVar1;
  uVar1 = FUN_00464a64(param_2,0xc);
  param_1[0xe] = uVar1;
  uVar1 = FUN_00464a64(param_2,0xd);
  param_1[0xf] = uVar1;
  uVar1 = FUN_00464a64(param_2,0xe);
  param_1[0x10] = uVar1;
  uVar1 = FUN_00464a64(param_2,0xf);
  param_1[9] = uVar1;
  uVar1 = FUN_00464a64(param_2,0x10);
  param_1[7] = uVar1;
  uVar1 = FUN_00464a64(param_2,0x11);
  param_1[8] = uVar1;
  uVar1 = FUN_00464a64(param_2,2);
  param_1[0x11] = uVar1;
  iVar2 = FUN_00464a64(param_2,0x12);
  *(bool *)(param_1 + 0x12) = iVar2 != 0;
  return;
}

~~~
