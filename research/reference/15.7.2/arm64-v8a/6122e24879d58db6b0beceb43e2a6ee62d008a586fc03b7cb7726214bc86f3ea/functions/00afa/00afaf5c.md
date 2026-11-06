# 00afaf5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

## 関数情報

~~~json
{
  "address": "00afaf5c",
  "name": "_ZNK8firebase10LoggerBase8LogDebugEPKcz",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72514155a64a7b2e786966e752710d5fb7c66576861bc9360c209d6c223492e4",
  "source_text_sha256": "72514155a64a7b2e786966e752710d5fb7c66576861bc9360c209d6c223492e4"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード / UTF-8 1923 bytes

~~~c

void _ZNK8firebase10LoggerBase8LogDebugEPKcz
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
  
                    /* try { // try from 00afaf6c to 00bfaf7f has its CatchHandler @ 00aff4d8 */
                    /* try { // try from 00afaf80 to 00bfafaf has its CatchHandler @ 00af560c */
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  ppuStack_98 = &local_a0;
  puStack_90 = &local_d0;
                    /* try { // try from 00afafb0 to 00bfafd3 has its CatchHandler @ 00b0037c */
  uStack_88 = 0xffffff80ffffffd0;
  local_d0 = param_3;
  uStack_c8 = param_4;
  local_c0 = param_5;
  uStack_b8 = param_6;
  local_b0 = param_7;
  uStack_a8 = param_8;
  local_a0 = (undefined1 *)register0x00000008;
                    /* try { // try from 00afafd4 to 00bfafdb has its CatchHandler @ 00aff4d4 */
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 < 2) {
    ppuStack_58 = ppuStack_98;
    local_60 = local_a0;
    uStack_48 = uStack_88;
    puStack_50 = puStack_90;
    (**(code **)(*param_1 + 0x20))(param_1,1,param_2,&local_60);
  }
                    /* try { // try from 00afb004 to 00bfb017 has its CatchHandler @ 00aff4d0 */
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00afb028 to 00bfb02f has its CatchHandler @ 00aff4cc */
  __stack_chk_fail();
}

~~~
