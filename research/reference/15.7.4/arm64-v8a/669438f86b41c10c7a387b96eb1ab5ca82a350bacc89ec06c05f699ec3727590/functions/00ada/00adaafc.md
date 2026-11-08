# 00adaafc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00adaafc",
  "name": "Java_jp_co_ponos_battlecats_TapjoyImplementation_onTapjoyConnect",
  "size": 104,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "edbe38aa15474fa56acc4f265088daf9a4580a132c62cbc60847b690940ba761",
  "source_text_sha256": "edbe38aa15474fa56acc4f265088daf9a4580a132c62cbc60847b690940ba761"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb090](../00bdb/00bdb090.md)

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
  if (DAT_0109ff90 != (long *)0x0) {
    local_2c[0] = param_3 != '\0';
    (**(code **)(*DAT_0109ff90 + 0x30))(DAT_0109ff90,local_2c);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
