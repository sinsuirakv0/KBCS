# 00b5aebc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00b5aebc",
  "name": "_ZNK8firebase10LoggerBase17FilterLogMessageVENS_8LogLevelEPKcSt9__va_list",
  "size": 152,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b12e40e55e0bae70cda92cdd48c75d9a489ce9dbe3cfec071e7830de9d594cd4",
  "source_text_sha256": "b12e40e55e0bae70cda92cdd48c75d9a489ce9dbe3cfec071e7830de9d594cd4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)

## 疑似コード / UTF-8 768 bytes

~~~c

void _ZNK8firebase10LoggerBase17FilterLogMessageVENS_8LogLevelEPKcSt9__va_list
               (long *param_1,int param_2,undefined8 param_3,undefined8 *param_4)

{
  long lVar1;
  int iVar2;
  undefined8 local_70;
  undefined8 uStack_68;
  undefined8 uStack_60;
  undefined8 uStack_58;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 <= param_2) {
    uStack_68 = param_4[1];
    local_70 = *param_4;
    uStack_58 = param_4[3];
    uStack_60 = param_4[2];
    (**(code **)(*param_1 + 0x20))(param_1,param_2,param_3,&local_70);
  }
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
