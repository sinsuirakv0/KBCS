# 00afdb3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

<!-- kbcs-version-next -->
**別版の対応** [v15.7.4 `00afdc48`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afd/00afdc48.md) · [本文差分](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/changes/00afdc48.md)
<!-- /kbcs-version-next -->

## 関数情報

~~~json
{
  "address": "00afdb3c",
  "name": "_ZNK8firebase4Path17PopFrontDirectoryEv",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a4564bd10acc91dcec4463139f5c7b9c83920fe2d0adfac13ced124f9f03f892",
  "source_text_sha256": "a4564bd10acc91dcec4463139f5c7b9c83920fe2d0adfac13ced124f9f03f892"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00afd1a0](../00afd/00afd1a0.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdec30](../00bde/00bdec30.md)
- [00bdec40](../00bde/00bdec40.md)

## 疑似コード / UTF-8 1871 bytes

~~~c

void _ZNK8firebase4Path17PopFrontDirectoryEv(undefined8 *param_1,byte *param_2)

{
  byte bVar1;
  long lVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  byte *local_68;
  byte *local_60;
  byte local_50 [16];
  void *local_40;
  long local_38;
  
                    /* try { // try from 00afdb40 to 00bfdb5b has its CatchHandler @ 00afecd4 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00afdb60 to 00bfdb6f has its CatchHandler @ 00b0037c */
  if ((*param_2 & 1) == 0) {
    if (*param_2 >> 1 == 0) {
LAB_00afdbec:
      *param_1 = 0;
      param_1[1] = 0;
      param_1[2] = 0;
      goto LAB_00afdc0c;
    }
  }
  else if (*(long *)(param_2 + 8) == 0) goto LAB_00afdbec;
  _ZNK8firebase4Path14GetDirectoriesEv(&local_68);
  FUN_00afd1a0(local_50,local_68 + 0x18,local_60);
  _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,local_50);
  if ((local_50[0] & 1) != 0) {
    _ZdlPv(local_40);
  }
  pbVar4 = local_68;
  if (local_68 != (byte *)0x0) {
                    /* try { // try from 00afdbb0 to 00bfdbbb has its CatchHandler @ 00afecd0 */
    if (local_60 != local_68) {
      bVar1 = local_60[-0x18];
      pbVar5 = local_60 + -0x18;
      while( true ) {
        pbVar3 = pbVar5;
                    /* try { // try from 00afdbc0 to 00bfdbdb has its CatchHandler @ 00afeccc */
        if ((bVar1 & 1) != 0) {
          _ZdlPv(*(void **)(local_60 + -8));
        }
        if (pbVar4 == pbVar3) break;
        bVar1 = pbVar3[-0x18];
        pbVar5 = pbVar3 + -0x18;
        local_60 = pbVar3;
      }
    }
    local_60 = pbVar4;
    _ZdlPv(local_68);
  }
LAB_00afdc0c:
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
