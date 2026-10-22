# 00afaf5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afaf5c.md)

## 関数情報

~~~json
{
  "address": "00afaf5c",
  "name": "firebase::LoggerBase::LogDebug",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "466cd0d17f59a5c4ae0545625b629cee9dc06b50faa8a89d6fa7179f511450f2",
  "source_text_sha256": "466cd0d17f59a5c4ae0545625b629cee9dc06b50faa8a89d6fa7179f511450f2"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)

## 疑似コード 1/1 / UTF-8 2021 bytes

~~~c

/* firebase::LoggerBase::LogDebug(char const*, ...) const */

void firebase::LoggerBase::LogDebug(char *param_1,...)

{
  long lVar1;
  int iVar2;
  undefined8 in_x1;
  undefined8 in_x2;
  undefined8 in_x3;
  undefined8 in_x4;
  undefined8 in_x5;
  undefined8 in_x6;
  undefined8 in_x7;
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
  local_d0 = in_x2;
  uStack_c8 = in_x3;
  local_c0 = in_x4;
  uStack_b8 = in_x5;
  local_b0 = in_x6;
  uStack_a8 = in_x7;
  local_a0 = (undefined1 *)register0x00000008;
                    /* try { // try from 00afafd4 to 00bfafdb has its CatchHandler @ 00aff4d4 */
  iVar2 = (**(code **)(*(long *)param_1 + 0x18))();
  if (iVar2 < 2) {
    ppuStack_58 = ppuStack_98;
    local_60 = local_a0;
    uStack_48 = uStack_88;
    puStack_50 = puStack_90;
    (**(code **)(*(long *)param_1 + 0x20))(param_1,1,in_x1,&local_60);
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
