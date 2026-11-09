# 00baa6dc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00baa6dc",
  "name": "FUN_00baa6dc",
  "size": 600,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "16fb3248daae4abff53821a947195b3471d4d1d71ddf12629e3ca6795de835bb",
  "source_text_sha256": "16fb3248daae4abff53821a947195b3471d4d1d71ddf12629e3ca6795de835bb"
}
~~~

## 呼び出し元

- [00b7ae50](../00b7a/00b7ae50.md)

## 呼び出し先

- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57c00](../00c57/00c57c00.md)
- [00c5ad40](../00c5a/00c5ad40.md)
- [00c5c130](../00c5c/00c5c130.md)
- [00c5cc40](../00c5c/00c5cc40.md)

## 疑似コード / UTF-8 4977 bytes

~~~c

void FUN_00baa6dc(char *param_1,long *param_2)

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
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00baa710 to 00caa71b has its CatchHandler @ 00babe10 */
  puVar7 = (undefined8 *)*param_2;
  lVar1 = param_2[1];
  uStack_88 = 0;
  local_80 = (void *)0x0;
                    /* try { // try from 00baa734 to 00caa73f has its CatchHandler @ 00babe00 */
  local_90 = 0x3002;
  local_78 = 0xffff;
  local_b0 = *puVar7;
  uStack_9e = (undefined6)*(undefined8 *)((long)puVar7 + 0x12);
  uStack_98 = (undefined2)((ulong)*(undefined8 *)((long)puVar7 + 0x12) >> 0x30);
                    /* try { // try from 00baa748 to 00caa74b has its CatchHandler @ 00babda0 */
  uStack_a0 = (undefined2)((ulong)*(undefined8 *)((long)puVar7 + 10) >> 0x30);
  uStack_a8 = (undefined2)puVar7[1];
  uStack_a6 = (undefined6)((ulong)puVar7[1] >> 0x10);
                    /* try { // try from 00baa768 to 00caa773 has its CatchHandler @ 00babd60 */
  _ZN11flatbuffers6Parser13ParseAnyValueERNS_5ValueEPNS_8FieldDefEmPKNS_9StructDefEmb
            (param_1,lVar1,&local_b0,*(undefined8 *)param_2[2],*(undefined8 *)param_2[3],0,
             *(undefined8 *)param_2[4],1);
  __src = local_80;
  __n = uStack_88;
  uVar6 = local_b0;
  param_1[1] = '\x01';
  if (*param_1 != '\0') goto joined_r0x00baa924;
  uVar3 = CONCAT62(uStack_a6,uStack_a8);
  uVar5 = CONCAT62(uStack_96,uStack_98);
  uVar4 = CONCAT62(uStack_9e,uStack_a0);
                    /* try { // try from 00baa7d8 to 00caa7e3 has its CatchHandler @ 00babd00 */
  local_130 = 0;
  uStack_128 = 0;
  local_120 = (void *)0x0;
  if ((local_90 & 1) == 0) {
    local_120 = local_80;
    uStack_128 = uStack_88;
    local_130 = local_90;
  }
  else {
                    /* try { // try from 00baa804 to 00caa80f has its CatchHandler @ 00babcc0 */
    if (0xffffffffffffffef < uStack_88) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    if (uStack_88 < 0x17) {
      __dest = (void *)((long)&local_130 + 1);
      local_130 = (ulong)(byte)((int)uStack_88 << 1);
      if (uStack_88 != 0) goto LAB_00baa84c;
    }
    else {
      uVar8 = uStack_88 + 0x10 & 0xfffffffffffffff0;
                    /* try { // try from 00baa834 to 00caa853 has its CatchHandler @ 00babe60 */
      __dest = (void *)_Znwm(uVar8);
      local_130 = uVar8 | 1;
      uStack_128 = __n;
      local_120 = __dest;
LAB_00baa84c:
                    /* try { // try from 00baa854 to 00caa88b has its CatchHandler @ 00babed0 */
      memcpy(__dest,__src,__n);
    }
    *(undefined1 *)((long)__dest + __n) = 0;
  }
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
  puVar7 = *(undefined8 **)(lVar1 + 0x5b8);
  uStack_f8 = uVar3;
  uStack_f0 = uVar4;
  uStack_e8 = uVar5;
  if (puVar7 < *(undefined8 **)(lVar1 + 0x5c0)) {
    puVar7[1] = uVar3;
    *puVar7 = uVar6;
    puVar7[3] = uVar5;
    puVar7[2] = uVar4;
    puVar7[6] = local_d0;
    puVar7[5] = uStack_d8;
    puVar7[4] = local_e0;
    uStack_d8 = 0;
    local_d0 = (void *)0x0;
                    /* try { // try from 00baa8c8 to 00caa8cb has its CatchHandler @ 00babbcc */
    local_e0 = 0;
    *(undefined2 *)(puVar7 + 7) = local_78;
    puVar7[8] = 0;
    *(undefined8 **)(lVar1 + 0x5b8) = puVar7 + 9;
  }
  else {
    _ZNSt6__ndk16vectorINS_4pairIN11flatbuffers5ValueEPNS2_8FieldDefEEENS_9allocatorIS6_EEE21__push_back_slow_pathIS6_EEvOT_
              (lVar1 + 0x5b0,&local_100);
    if ((local_e0 & 1) != 0) {
                    /* try { // try from 00baa908 to 00caa91b has its CatchHandler @ 00bab8e8 */
      _ZdlPv(local_d0);
    }
    if ((local_130 & 1) != 0) {
      _ZdlPv(local_120);
    }
  }
  param_1[0] = '\0';
  param_1[1] = '\0';
joined_r0x00baa924:
  if ((local_90 & 1) != 0) {
    _ZdlPv(local_80);
  }
  if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* try { // try from 00baa7b4 to 00caa7bf has its CatchHandler @ 00babd10 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
