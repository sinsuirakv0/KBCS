# 00b0ddcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00b0ddcc",
  "name": "_ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45cf3cc3e5ab03409c63e8d622c821824c7b1c820a81facbbde049d63b0af31f",
  "source_text_sha256": "45cf3cc3e5ab03409c63e8d622c821824c7b1c820a81facbbde049d63b0af31f"
}
~~~

## 呼び出し元

- [00bdef90](../00bde/00bdef90.md)

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード / UTF-8 1111 bytes

~~~c

void _ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz
               (long *param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  long lVar1;
  long lVar2;
  undefined1 auStack_a0 [8];
  undefined8 local_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined1 *local_70;
  undefined1 **ppuStack_68;
  undefined1 *puStack_60;
  undefined8 uStack_58;
  
  lVar1 = tpidr_el0;
  lVar2 = *(long *)(lVar1 + 0x28);
  puStack_60 = auStack_a0;
  ppuStack_68 = &local_70;
  uStack_58 = 0xffffff80ffffffd8;
  local_98 = param_4;
  uStack_90 = param_5;
  local_88 = param_6;
  uStack_80 = param_7;
  local_78 = param_8;
  local_70 = (undefined1 *)register0x00000008;
  (**(code **)(*param_1 + 0x3b0))();
  if (*(long *)(lVar1 + 0x28) == lVar2) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00b0de64 to 00c0de6b has its CatchHandler @ 00b0dfec */
  __stack_chk_fail();
}

~~~
