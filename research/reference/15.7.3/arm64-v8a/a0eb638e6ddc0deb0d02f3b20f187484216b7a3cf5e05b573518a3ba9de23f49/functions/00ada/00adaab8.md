# 00adaab8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00adaab8",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyConnect",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "12edb31acbfd47cf2d5dda15505b40729a5b7ad3ce51b9b3d9e55d4948ecb157",
  "source_text_sha256": "12edb31acbfd47cf2d5dda15505b40729a5b7ad3ce51b9b3d9e55d4948ecb157"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 550 bytes

~~~c

void Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyConnect
               (undefined8 param_1,undefined8 param_2,char param_3)

{
  long lVar1;
  undefined1 local_2c [4];
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  if (DAT_0109ff50 != (long *)0x0) {
    local_2c[0] = param_3 != '\0';
    (**(code **)(*DAT_0109ff50 + 0x30))(DAT_0109ff50,local_2c);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
