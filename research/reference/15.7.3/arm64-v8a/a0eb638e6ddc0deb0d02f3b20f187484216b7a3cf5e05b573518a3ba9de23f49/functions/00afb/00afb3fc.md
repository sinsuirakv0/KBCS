# 00afb3fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afb3fc",
  "name": "_ZNK8firebase10LoggerBase9LogAssertEPKcz",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f6fa6a25958c0338ff31fcc96fc43d93ca42c74e8a6fa6c344168643733b379",
  "source_text_sha256": "2f6fa6a25958c0338ff31fcc96fc43d93ca42c74e8a6fa6c344168643733b379"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 1633 bytes

~~~c

void _ZNK8firebase10LoggerBase9LogAssertEPKcz
               (long *param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  long lVar1;
  int iVar2;
  undefined8 local_d0;
  undefined8 uStack_c8;
  undefined8 local_c0;
  undefined8 uStack_b8;
  undefined8 local_b0;
  undefined8 uStack_a8;
  undefined1 *local_a0;
  undefined1 **ppuStack_98;
  undefined8 *puStack_90;
  undefined8 uStack_88;
  undefined1 *local_60;
  undefined1 **ppuStack_58;
  undefined8 *puStack_50;
  undefined8 uStack_48;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00afb438 to 00bfb447 has its CatchHandler @ 00aff488 */
  ppuStack_98 = &local_a0;
  puStack_90 = &local_d0;
                    /* try { // try from 00afb458 to 00bfb45f has its CatchHandler @ 00aff484 */
  uStack_88 = 0xffffff80ffffffd0;
  local_d0 = param_3;
  uStack_c8 = param_4;
  local_c0 = param_5;
  uStack_b8 = param_6;
  local_b0 = param_7;
  uStack_a8 = param_8;
  local_a0 = (undefined1 *)register0x00000008;
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 < 6) {
                    /* try { // try from 00afb488 to 00bfb49b has its CatchHandler @ 00aff480 */
    ppuStack_58 = ppuStack_98;
    local_60 = local_a0;
    uStack_48 = uStack_88;
    puStack_50 = puStack_90;
    (**(code **)(*param_1 + 0x20))(param_1,5,param_2,&local_60);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
