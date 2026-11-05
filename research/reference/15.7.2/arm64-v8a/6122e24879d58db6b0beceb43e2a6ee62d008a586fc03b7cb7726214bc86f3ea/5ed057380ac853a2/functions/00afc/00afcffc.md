# 00afcffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00afcffc.md)

## 関数情報

~~~json
{
  "address": "00afcffc",
  "name": "_ZN8firebase4PathC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e61b2db7963c91682f6842f5ef530544b6a2609a167fed726f17950c918b1c41",
  "source_text_sha256": "e61b2db7963c91682f6842f5ef530544b6a2609a167fed726f17950c918b1c41"
}
~~~
## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00afd1a0](../00afd/00afd1a0.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bde1c0](../00bde/00bde1c0.md)
- [00bde630](../00bde/00bde630.md)
- [00bdec30](../00bde/00bdec30.md)

## 疑似コード 1/1 / UTF-8 2256 bytes

~~~c

void _ZN8firebase4PathC2ERKNSt6__ndk16vectorINS1_12basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEENS6_IS8_EEEE
               (undefined8 param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  byte bVar3;
  long lVar4;
  long lVar5;
  byte *pbVar6;
  byte *pbVar7;
  byte *__ptr;
  byte *pbVar8;
  byte local_60 [16];
  void *local_50;
  long local_48;
  
                    /* try { // try from 00afd010 to 00bfd03f has its CatchHandler @ 00af560c */
  lVar5 = tpidr_el0;
  local_48 = *(long *)(lVar5 + 0x28);
  lVar1 = *param_2;
  lVar2 = param_2[1];
  lVar4 = lVar2 - lVar1;
  if (lVar4 == 0) {
    __ptr = (byte *)0x0;
    pbVar8 = (byte *)0x0;
  }
  else {
                    /* try { // try from 00afd040 to 00bfd047 has its CatchHandler @ 00aff388 */
    if (0xaaaaaaaaaaaaaaa < (ulong)((lVar4 >> 3) * -0x5555555555555555)) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    __ptr = (byte *)_Znwm(lVar4);
    pbVar8 = __ptr;
    for (; lVar1 != lVar2; lVar1 = lVar1 + 0x18) {
                    /* try { // try from 00afd070 to 00bfd087 has its CatchHandler @ 00aff384 */
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_(pbVar8,lVar1);
      pbVar8 = pbVar8 + 0x18;
    }
  }
  FUN_00afd1a0(local_60,__ptr,pbVar8);
  _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
            (param_1,local_60);
  if ((local_60[0] & 1) != 0) {
    _ZdlPv(local_50);
  }
                    /* try { // try from 00afd0c0 to 00bfd0d7 has its CatchHandler @ 00aff380 */
  if (__ptr != (byte *)0x0) {
    if (pbVar8 != __ptr) {
      bVar3 = pbVar8[-0x18];
      pbVar7 = pbVar8 + -0x18;
      while( true ) {
        pbVar6 = pbVar7;
        if ((bVar3 & 1) != 0) {
          _ZdlPv(*(void **)(pbVar8 + -8));
        }
        if (__ptr == pbVar6) break;
        bVar3 = pbVar6[-0x18];
        pbVar7 = pbVar6 + -0x18;
        pbVar8 = pbVar6;
      }
    }
    _ZdlPv(__ptr);
  }
  if (*(long *)(lVar5 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
                    /* try { // try from 00afd110 to 00bfd11b has its CatchHandler @ 00aff37c */
  return;
}

~~~
