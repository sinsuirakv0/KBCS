# 00afb5ec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

ページ 1/1。[入口](00afb5ec.md)

## 関数情報

~~~json
{
  "address": "00afb5ec",
  "name": "_ZNK8firebase10LoggerBase11LogMessageVENS_8LogLevelEPKcSt9__va_list",
  "size": 148,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "249303df8d695d249fe860e2ad2c86c58b79d88d9de964987ccc208df50de769",
  "source_text_sha256": "249303df8d695d249fe860e2ad2c86c58b79d88d9de964987ccc208df50de769"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb090](../00bdb/00bdb090.md)

## 疑似コード 1/1 / UTF-8 1201 bytes

~~~c

void _ZNK8firebase10LoggerBase11LogMessageVENS_8LogLevelEPKcSt9__va_list
               (long *param_1,int param_2,undefined8 param_3,undefined8 *param_4)

{
  long lVar1;
  int iVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 uStack_50;
  undefined8 uStack_48;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  uVar6 = param_4[1];
  uVar5 = *param_4;
                    /* try { // try from 00afb618 to 00bfb61f has its CatchHandler @ 00aff4c0 */
  uVar4 = param_4[3];
  uVar3 = param_4[2];
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 <= param_2) {
                    /* try { // try from 00afb648 to 00bfb65f has its CatchHandler @ 00aff4bc */
    local_60 = uVar5;
    uStack_58 = uVar6;
    uStack_50 = uVar3;
    uStack_48 = uVar4;
    (**(code **)(*param_1 + 0x20))(param_1,param_2,param_3,&local_60);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* try { // try from 00afb670 to 00bfb677 has its CatchHandler @ 00aff4b8 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
