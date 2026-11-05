# 00ae3fcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae3fcc.md)

## 関数情報

~~~json
{
  "address": "00ae3fcc",
  "name": "_ZN8firebase8LogDebugEPKcz",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b193ea10af8a68dbc6dd8abe2e4151710e390d3aa175357c441a0f4d0805455b",
  "source_text_sha256": "b193ea10af8a68dbc6dd8abe2e4151710e390d3aa175357c441a0f4d0805455b"
}
~~~
## 呼び出し元

- [00bde1b0](../00bde/00bde1b0.md)

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)
- [00bde1a0](../00bde/00bde1a0.md)

## 疑似コード 1/1 / UTF-8 1228 bytes

~~~c

void _ZN8firebase8LogDebugEPKcz
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  long lVar1;
  long lVar2;
  undefined1 auStack_b0 [8];
  undefined8 local_a8;
  undefined8 uStack_a0;
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
                    /* try { // try from 00ae4010 to 00be4097 has its CatchHandler @ 00ae417c */
  ppuStack_68 = &local_70;
  puStack_60 = auStack_b0;
  uStack_58 = 0xffffff80ffffffc8;
  local_a8 = param_2;
  uStack_a0 = param_3;
  local_98 = param_4;
  uStack_90 = param_5;
  local_88 = param_6;
  uStack_80 = param_7;
  local_78 = param_8;
  local_70 = (undefined1 *)register0x00000008;
  _ZN8firebase23LogMessageWithCallbackVENS_8LogLevelEPKcSt9__va_list(1,param_1,&local_70);
  if (*(long *)(lVar1 + 0x28) == lVar2) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
