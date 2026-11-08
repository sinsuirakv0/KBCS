# 00afdb2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

## 関数情報

~~~json
{
  "address": "00afdb2c",
  "name": "_ZNK8firebase4Path14FrontDirectoryEv",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ade0712361917ed5e6ad4a47f106a04c135a2fd8a8c301c36b046f40a168bd3e",
  "source_text_sha256": "ade0712361917ed5e6ad4a47f106a04c135a2fd8a8c301c36b046f40a168bd3e"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdece0](../00bde/00bdece0.md)
- [00bdecf0](../00bde/00bdecf0.md)

## 疑似コード / UTF-8 1816 bytes

~~~c

void _ZNK8firebase4Path14FrontDirectoryEv(undefined8 *param_1,byte *param_2)

{
  byte bVar1;
  long lVar2;
  byte *pbVar3;
  byte *pbVar4;
  byte *pbVar5;
  byte *local_50;
  byte *local_48;
  long local_38;
  
                    /* try { // try from 00afdb30 to 00bfdb3b has its CatchHandler @ 00afecd8 */
                    /* try { // try from 00afdb40 to 00bfdb5b has its CatchHandler @ 00afecd4 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  if ((*param_2 & 1) == 0) {
    if (*param_2 >> 1 == 0) {
LAB_00afdbbc:
      *param_1 = 0;
      param_1[1] = 0;
                    /* try { // try from 00afdbc0 to 00bfdbdb has its CatchHandler @ 00afeccc */
      param_1[2] = 0;
      goto LAB_00afdbdc;
    }
  }
  else if (*(long *)(param_2 + 8) == 0) goto LAB_00afdbbc;
                    /* try { // try from 00afdb60 to 00bfdb6f has its CatchHandler @ 00b0037c */
  _ZNK8firebase4Path14GetDirectoriesEv(&local_50);
  _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,local_50);
  pbVar4 = local_50;
  if (local_50 != (byte *)0x0) {
    if (local_48 != local_50) {
      bVar1 = local_48[-0x18];
      pbVar5 = local_48 + -0x18;
      while( true ) {
        pbVar3 = pbVar5;
        if ((bVar1 & 1) != 0) {
          _ZdlPv(*(void **)(local_48 + -8));
                    /* try { // try from 00afdbb0 to 00bfdbbb has its CatchHandler @ 00afecd0 */
        }
        if (pbVar4 == pbVar3) break;
        bVar1 = pbVar3[-0x18];
        pbVar5 = pbVar3 + -0x18;
        local_48 = pbVar3;
      }
    }
    local_48 = pbVar4;
    _ZdlPv(local_50);
  }
LAB_00afdbdc:
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
