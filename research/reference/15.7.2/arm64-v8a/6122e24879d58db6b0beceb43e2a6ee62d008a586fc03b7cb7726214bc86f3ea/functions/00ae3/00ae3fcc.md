# 00ae3fcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ae3fcc.md)

## 関数情報

~~~json
{
  "address": "00ae3fcc",
  "name": "firebase::LogDebug",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d3fe119e83d15d044329d31cf62410083365593f110de6d2c4ac8b19ce599ae",
  "source_text_sha256": "4d3fe119e83d15d044329d31cf62410083365593f110de6d2c4ac8b19ce599ae"
}
~~~
## 呼び出し元

- [00bde1b0](../00bde/00bde1b0.md)

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)
- [00bde1a0](../00bde/00bde1a0.md)

## 疑似コード 1/1 / UTF-8 1231 bytes

~~~c

/* firebase::LogDebug(char const*, ...) */

void firebase::LogDebug(char *param_1,...)

{
  long lVar1;
  undefined8 in_x1;
  undefined8 in_x2;
  undefined8 in_x3;
  undefined8 in_x4;
  undefined8 in_x5;
  undefined8 in_x6;
  undefined8 in_x7;
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
  local_a8 = in_x1;
  uStack_a0 = in_x2;
  local_98 = in_x3;
  uStack_90 = in_x4;
  local_88 = in_x5;
  uStack_80 = in_x6;
  local_78 = in_x7;
  local_70 = (undefined1 *)register0x00000008;
  LogMessageWithCallbackV(1,param_1,&local_70);
  if (*(long *)(lVar1 + 0x28) == lVar2) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
