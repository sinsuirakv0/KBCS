# 00baaba0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "00baaba0",
  "name": "FUN_00baaba0",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b72ac015a6a1e5728ac5ad8444421111ad0a83164e380374e0c1729eaf9c258c",
  "source_text_sha256": "b72ac015a6a1e5728ac5ad8444421111ad0a83164e380374e0c1729eaf9c258c"
}
~~~

## 呼び出し元

- [00b7b314](../00b7b/00b7b314.md)

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)
- [00c5b210](../00c5b/00c5b210.md)
- [00c5c600](../00c5c/00c5c600.md)
- [00c5d110](../00c5d/00c5d110.md)

## 疑似コード / UTF-8 5171 bytes

~~~c

void FUN_00baaba0(char *param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  ulong __n;
  void *__src;
  void *__dest;
  undefined8 *puVar7;
  ulong uVar8;
  undefined8 local_130;
  ulong uStack_128;
  void *local_120;
  undefined2 local_118;
  undefined8 local_110;
  undefined8 local_100;
  undefined8 uStack_f8;
  undefined8 uStack_f0;
  undefined8 uStack_e8;
  ulong local_e0;
  ulong uStack_d8;
  void *local_d0;
  undefined2 local_c8;
  undefined8 local_c0;
  undefined8 local_b0;
  undefined2 uStack_a8;
  undefined6 uStack_a6;
  undefined2 uStack_a0;
  undefined6 uStack_9e;
  undefined2 uStack_98;
  undefined6 uStack_96;
  ulong local_90;
  ulong uStack_88;
  void *local_80;
  undefined2 local_78;
  long local_68;
  
                    /* try { // try from 00baabbc to 00caabbf has its CatchHandler @ 00babe34 */
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  puVar7 = (undefined8 *)*param_2;
  lVar1 = param_2[1];
  uStack_88 = 0;
  local_80 = (void *)0x0;
                    /* try { // try from 00baabf8 to 00caac0b has its CatchHandler @ 00babb50 */
  local_90 = 0x3002;
  local_78 = 0xffff;
  local_b0 = *puVar7;
  uStack_9e = (undefined6)*(undefined8 *)((long)puVar7 + 0x12);
  uStack_98 = (undefined2)((ulong)*(undefined8 *)((long)puVar7 + 0x12) >> 0x30);
  uStack_a0 = (undefined2)((ulong)*(undefined8 *)((long)puVar7 + 10) >> 0x30);
  uStack_a8 = (undefined2)puVar7[1];
  uStack_a6 = (undefined6)((ulong)puVar7[1] >> 0x10);
  _ZN11flatbuffers6Parser13ParseAnyValueERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefEmb
            (param_1,lVar1,&local_b0,*(undefined8 *)param_2[2],*(undefined8 *)param_2[3],0,
             *(undefined8 *)param_2[4],1);
  __src = local_80;
  __n = uStack_88;
  uVar6 = local_b0;
  param_1[1] = '\x01';
  if (*param_1 != '\0') goto joined_r0x00baade8;
  uVar3 = CONCAT62(uStack_a6,uStack_a8);
  uVar5 = CONCAT62(uStack_96,uStack_98);
  uVar4 = CONCAT62(uStack_9e,uStack_a0);
                    /* try { // try from 00baac94 to 00caac97 has its CatchHandler @ 00babdc0 */
  local_130 = 0;
  uStack_128 = 0;
  local_120 = (void *)0x0;
  if ((local_90 & 1) == 0) {
                    /* try { // try from 00baacb4 to 00caacbf has its CatchHandler @ 00babd64 */
    local_120 = local_80;
    uStack_128 = uStack_88;
    local_130 = local_90;
  }
  else {
    if (0xffffffffffffffef < uStack_88) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
                    /* try { // try from 00baacd4 to 00caacdf has its CatchHandler @ 00babd60 */
    if (uStack_88 < 0x17) {
      __dest = (void *)((long)&local_130 + 1);
      local_130 = (ulong)(byte)((int)uStack_88 << 1);
      if (uStack_88 != 0) goto LAB_00baad10;
    }
    else {
      uVar8 = uStack_88 + 0x10 & 0xfffffffffffffff0;
      __dest = (void *)_Znwm(uVar8);
                    /* try { // try from 00baad00 to 00caad0b has its CatchHandler @ 00babd1c */
      local_130 = uVar8 | 1;
      uStack_128 = __n;
      local_120 = __dest;
LAB_00baad10:
      memcpy(__dest,__src,__n);
    }
    *(undefined1 *)((long)__dest + __n) = 0;
  }
                    /* try { // try from 00baad24 to 00caad2f has its CatchHandler @ 00babce0 */
  local_d0 = local_120;
  uStack_d8 = uStack_128;
  local_e0 = local_130;
  local_110 = 0;
  local_c0 = 0;
  local_118 = local_78;
  local_100 = uVar6;
  local_c8 = local_78;
  uStack_128 = 0;
  local_120 = (void *)0x0;
  local_130 = 0;
                    /* try { // try from 00baad50 to 00caad5b has its CatchHandler @ 00babcd0 */
  puVar7 = *(undefined8 **)(lVar1 + 0x5b8);
  uStack_f8 = uVar3;
  uStack_f0 = uVar4;
  uStack_e8 = uVar5;
  if (puVar7 < *(undefined8 **)(lVar1 + 0x5c0)) {
                    /* try { // try from 00baad70 to 00caad7b has its CatchHandler @ 00babc90 */
    puVar7[1] = uVar3;
    *puVar7 = uVar6;
    puVar7[3] = uVar5;
    puVar7[2] = uVar4;
    puVar7[6] = local_d0;
    puVar7[5] = uStack_d8;
    puVar7[4] = local_e0;
    uStack_d8 = 0;
    local_d0 = (void *)0x0;
    local_e0 = 0;
    *(undefined2 *)(puVar7 + 7) = local_78;
                    /* try { // try from 00baad9c to 00caada7 has its CatchHandler @ 00babc80 */
    puVar7[8] = 0;
    *(undefined8 **)(lVar1 + 0x5b8) = puVar7 + 9;
  }
  else {
    _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_
              (lVar1 + 0x5b0,&local_100);
                    /* try { // try from 00baadc0 to 00caadcb has its CatchHandler @ 00babc60 */
    if ((local_e0 & 1) != 0) {
      _ZdlPv(local_d0);
    }
    if ((local_130 & 1) != 0) {
      _ZdlPv(local_120);
    }
  }
  param_1[0] = '\0';
  param_1[1] = '\0';
joined_r0x00baade8:
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
                    /* try { // try from 00baac5c to 00caac67 has its CatchHandler @ 00babe30 */
  if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* try { // try from 00baac80 to 00caac8b has its CatchHandler @ 00babde0 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
