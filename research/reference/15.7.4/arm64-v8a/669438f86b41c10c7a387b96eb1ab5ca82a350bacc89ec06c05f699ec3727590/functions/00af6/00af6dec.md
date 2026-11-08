# 00af6dec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

## 関数情報

~~~json
{
  "address": "00af6dec",
  "name": "_ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_S6_",
  "size": 304,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c36baa881dffca3c1b89128b5208207d18c87e327d9850b41ad67d5fcfdc0750",
  "source_text_sha256": "c36baa881dffca3c1b89128b5208207d18c87e327d9850b41ad67d5fcfdc0750"
}
~~~

## 呼び出し元

- [00bde7f0](../00bde/00bde7f0.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bdda90](../00bdd/00bdda90.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 疑似コード / UTF-8 2173 bytes

~~~c

void _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EERKS9_S6_
               (ulong *param_1,byte *param_2,undefined1 param_3)

{
  size_t __n;
  byte *__src;
  bool bVar1;
  ulong uVar2;
  byte bVar3;
  ulong uVar4;
  void *__dest;
  
                    /* try { // try from 00af6e00 to 00bf6e0b has its CatchHandler @ 00afefe8 */
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
                    /* try { // try from 00af6e0c to 00bf6e27 has its CatchHandler @ 00afef6c */
  __src = *(byte **)(param_2 + 0x10);
  bVar1 = (*param_2 & 1) != 0;
  __n = (ulong)(*param_2 >> 1);
  if (bVar1) {
    __n = *(size_t *)(param_2 + 8);
  }
  if (!bVar1) {
    __src = param_2 + 1;
  }
                    /* try { // try from 00af6e28 to 00bf6eef has its CatchHandler @ 00af5650 */
  if (0xffffffffffffffef < __n + 1) {
                    /* WARNING: Subroutine does not return */
    abort();
  }
  if (__n + 1 < 0x17) {
    __dest = (void *)((long)param_1 + 1);
    *(char *)param_1 = (char)((int)__n << 1);
    if (__n != 0) goto LAB_00af6e70;
  }
  else {
    uVar4 = __n + 0x11 & 0xfffffffffffffff0;
    __dest = (void *)_Znwm(uVar4);
    param_1[1] = __n;
    param_1[2] = (ulong)__dest;
    *param_1 = uVar4 | 1;
LAB_00af6e70:
    memcpy(__dest,__src,__n);
  }
  *(undefined1 *)((long)__dest + __n) = 0;
  bVar3 = (byte)*param_1;
  if ((bVar3 & 1) == 0) {
    uVar4 = (ulong)(bVar3 >> 1);
    uVar2 = 0x16;
    if (uVar4 != 0x16) goto LAB_00af6ed4;
  }
  else {
    uVar4 = param_1[1];
    uVar2 = (*param_1 & 0xfffffffffffffffe) - 1;
    if (uVar4 != uVar2) goto LAB_00af6ed4;
  }
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9__grow_byEmmmmmm
            (param_1,uVar2,1,uVar2,uVar2,0,0);
  bVar3 = (byte)*param_1;
LAB_00af6ed4:
  if ((bVar3 & 1) == 0) {
                    /* try { // try from 00af6ef0 to 00bf6f07 has its CatchHandler @ 00b003c0 */
    uVar2 = (long)param_1 + 1;
    *(char *)param_1 = (char)uVar4 * '\x02' + '\x02';
  }
  else {
    uVar2 = param_1[2];
    param_1[1] = uVar4 + 1;
  }
  *(undefined1 *)(uVar2 + uVar4) = param_3;
  ((undefined1 *)(uVar2 + uVar4))[1] = 0;
  return;
}

~~~
