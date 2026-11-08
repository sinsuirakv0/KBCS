# 00afb4cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afb4cc",
  "name": "_ZNK8firebase10LoggerBase10LogMessageENS_8LogLevelEPKcz",
  "size": 220,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5fd7ac18a284de48696e4ad956c25278aa775f5946b14e110818240d96f666c9",
  "source_text_sha256": "5fd7ac18a284de48696e4ad956c25278aa775f5946b14e110818240d96f666c9"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)

## 疑似コード / UTF-8 1734 bytes

~~~c

void _ZNK8firebase10LoggerBase10LogMessageENS_8LogLevelEPKcz
               (long *param_1,int param_2,undefined8 param_3,undefined8 param_4,undefined8 param_5,
               undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  long lVar1;
  int iVar2;
  undefined1 auStack_e0 [8];
  undefined8 local_d8;
  undefined8 uStack_d0;
  undefined8 local_c8;
  undefined8 uStack_c0;
  undefined8 local_b8;
  undefined1 *local_b0;
  undefined1 **ppuStack_a8;
  undefined1 *puStack_a0;
  undefined8 uStack_98;
  undefined1 *local_70;
  undefined1 **ppuStack_68;
  undefined1 *puStack_60;
  undefined8 uStack_58;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  ppuStack_a8 = &local_b0;
  puStack_a0 = auStack_e0;
                    /* try { // try from 00afb528 to 00bfb52f has its CatchHandler @ 00b001d4 */
                    /* try { // try from 00afb530 to 00bfb53f has its CatchHandler @ 00b00224 */
                    /* try { // try from 00afb540 to 00bfb54b has its CatchHandler @ 00b0020c */
  uStack_98 = 0xffffff80ffffffd8;
  local_d8 = param_4;
  uStack_d0 = param_5;
  local_c8 = param_6;
  uStack_c0 = param_7;
  local_b8 = param_8;
  local_b0 = (undefined1 *)register0x00000008;
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 <= param_2) {
    ppuStack_68 = ppuStack_a8;
    local_70 = local_b0;
    uStack_58 = uStack_98;
    puStack_60 = puStack_a0;
    (**(code **)(*param_1 + 0x20))(param_1,param_2,param_3,&local_70);
  }
  if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* try { // try from 00afb594 to 00bfb5d3 has its CatchHandler @ 00b000ec */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
