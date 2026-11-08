# 00afb6bc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afb6bc",
  "name": "_ZNK8firebase6Logger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list",
  "size": 152,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f2a0e09251b25d8dde5c5af4d102d3669284e1ef63decdc2b279fe7e95bd512",
  "source_text_sha256": "2f2a0e09251b25d8dde5c5af4d102d3669284e1ef63decdc2b279fe7e95bd512"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 1351 bytes

~~~c

void _ZNK8firebase6Logger15LogMessageImplVENS_8LogLevelEPKcSt9__va_list
               (long param_1,int param_2,undefined8 param_3,undefined8 *param_4)

{
  long lVar1;
  int iVar2;
  long *plVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 uVar7;
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 uStack_50;
  undefined8 uStack_48;
  long local_38;
  
                    /* try { // try from 00afb6c4 to 00bfb6db has its CatchHandler @ 00aff468 */
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar7 = param_4[1];
  uVar6 = *param_4;
  uVar5 = param_4[3];
  uVar4 = param_4[2];
  plVar3 = *(long **)(param_1 + 8);
                    /* try { // try from 00afb6ec to 00bfb6f3 has its CatchHandler @ 00aff464 */
  iVar2 = (**(code **)(*plVar3 + 0x18))(plVar3);
  if (iVar2 <= param_2) {
                    /* try { // try from 00afb71c to 00bfb72f has its CatchHandler @ 00aff460 */
    local_60 = uVar6;
    uStack_58 = uVar7;
    uStack_50 = uVar4;
    uStack_48 = uVar5;
    (**(code **)(*plVar3 + 0x20))(plVar3,param_2,param_3,&local_60);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00afb740 to 00bfb757 has its CatchHandler @ 00b0037c */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
