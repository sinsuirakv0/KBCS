# 009cfffc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "009cfffc",
  "name": "FUN_009cfffc",
  "size": 724,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3835e6ae4a0a51e1ff7801217d9de4ec9f697bdc8ea3e6510104dd3cfee72e98",
  "source_text_sha256": "3835e6ae4a0a51e1ff7801217d9de4ec9f697bdc8ea3e6510104dd3cfee72e98"
}
~~~

## 呼び出し元

- [00b1f428](../00b1f/00b1f428.md)

## 呼び出し先

- [0048791c](../00487/0048791c.md)
- [0048793c](../00487/0048793c.md)
- [00487e20](../00487/00487e20.md)
- [00488558](../00488/00488558.md)
- [00488658](../00488/00488658.md)
- [00b110ec](../00b11/00b110ec.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57fa0](../00c57/00c57fa0.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c58090](../00c58/00c58090.md)

## 関連文字列（未確認候補）

~~~text
"rankGift.csv"
"unitlimit.csv"
~~~

## 疑似コード / UTF-8 13111 bytes

~~~c

void FUN_009cfffc(long param_1)

{
  long lVar1;
  byte *pbVar2;
  undefined *puVar3;
  undefined *puVar4;
  bool bVar5;
  int iVar6;
  ulong uVar7;
  void *__s;
  byte *pbVar8;
  long lVar9;
  byte local_1b8;
  undefined5 local_1b7;
  undefined3 uStack_1b2;
  undefined4 local_1af;
  char local_1ab;
  undefined1 local_1aa;
  void *local_1a8;
  undefined **local_1a0;
  void *local_198;
  void *local_190;
  byte local_180;
  void *local_170;
  long local_158;
  undefined *local_150 [8];
  byte local_110;
  void *local_100;
  undefined1 auStack_e8 [160];
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  FUN_00487e20(&local_1a0);
  local_1a0 = &PTR_FUN_00c64d38;
  local_1b8 = 0x18;
  local_1af = 0x7673632e;
  local_1ab = 0;
  local_1b7 = (undefined5)s_rankGift_csv_002be0c0._0_8_;
  uStack_1b2 = SUB83(s_rankGift_csv_002be0c0._0_8_,5);
  FUN_00b110ec(&local_1a0,&local_1b8,0,0);
  if ((local_1b8 & 1) != 0) {
    _ZdlPv(local_1a8);
  }
  __s = (void *)((long)&DWORD_0039e51c + param_1);
  memset(__s,0xff,0x8340);
  lVar9 = 0;
                    /* try { // try from 009d00a0 to 00ad00b3 has its CatchHandler @ 009d02bc */
  do {
    uVar7 = FUN_0048791c(&local_1a0);
    if (((uVar7 & 1) == 0) || (iVar6 = FUN_00488558(&local_1a0), iVar6 == 1)) break;
    uVar7 = 0;
    do {
                    /* try { // try from 009d00d8 to 00ad0133 has its CatchHandler @ 009d02c4 */
      iVar6 = FUN_0048793c(&local_1a0,uVar7 & 0xffffffff);
      *(int *)((long)__s + uVar7 * 4) = iVar6;
      if (iVar6 == -1) break;
      bVar5 = uVar7 < 0x14;
      uVar7 = uVar7 + 1;
    } while (bVar5);
    lVar9 = lVar9 + 1;
    __s = (void *)((long)__s + 0x54);
  } while (lVar9 != 400);
  FUN_00488658(&local_1a0);
  local_1b8 = 0x1a;
  local_1aa = 0;
  local_1b7._0_1_ = s_unitlimit_csv_002a5d1b[0];
  local_1b7._1_1_ = s_unitlimit_csv_002a5d1b[1];
  local_1b7._2_1_ = s_unitlimit_csv_002a5d1b[2];
  local_1b7._3_1_ = s_unitlimit_csv_002a5d1b[3];
  local_1b7._4_1_ = s_unitlimit_csv_002a5d1b[4];
  uStack_1b2._0_1_ = s_unitlimit_csv_002a5d1b[5];
  uStack_1b2._1_1_ = s_unitlimit_csv_002a5d1b[6];
  uStack_1b2._2_1_ = s_unitlimit_csv_002a5d1b[7];
  local_1af = (undefined4)s_unitlimit_csv_002a5d1b._8_5_;
  local_1ab = SUB51(s_unitlimit_csv_002a5d1b._8_5_,4);
  FUN_00b110ec(&local_1a0,&local_1b8,0,0);
  if ((local_1b8 & 1) != 0) {
    _ZdlPv(local_1a8);
  }
  pbVar8 = BYTE_ARRAY_003a8dd1 + param_1 + 0xf;
  memset(pbVar8,0xff,0x8ac0);
  lVar9 = 0;
  do {
    uVar7 = FUN_0048791c(&local_1a0);
    if ((uVar7 & 1) != 0) {
      FUN_00488558(&local_1a0);
    }
    uVar7 = 0;
    do {
                    /* try { // try from 009d019c to 00ad01c3 has its CatchHandler @ 009d02c0 */
      iVar6 = FUN_0048793c(&local_1a0,uVar7 & 0xffffffff);
      *(int *)(pbVar8 + uVar7 * 4) = iVar6;
      if (iVar6 == -1) break;
      bVar5 = uVar7 < 9;
      uVar7 = uVar7 + 1;
    } while (bVar5);
    lVar9 = lVar9 + 1;
    pbVar8 = pbVar8 + 0x28;
    if (lVar9 == 0x378) {
      FUN_00488658(&local_1a0);
                    /* try { // try from 009d01c8 to 00ad0277 has its CatchHandler @ 009d02bc */
      pbVar8 = BYTE_ARRAY_003b1a2d + param_1 + 0x23;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&DWORD_003b18f8 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&fde_003b18f0 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1908 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&QWORD_003b18fc + param_1 + 4) = 0xffffffffffffffff;
      *(undefined8 *)((long)&fde_003b1918 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&QWORD_003b1910 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&QWORD_003b1924 + param_1 + 4) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1920 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&QWORD_003b1938 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1930 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1948 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&fde_003b1940 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1958 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&QWORD_003b194c + param_1 + 4) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b1965 + param_1 + 3;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&DWORD_003b1960 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b1965 + param_1 + 0xb;
      pbVar2 = BYTE_ARRAY_003b1965 + param_1 + 0x13;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b1965 + param_1 + 0x1b;
      pbVar2 = BYTE_ARRAY_003b1965 + param_1 + 0x23;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&DWORD_003b1998 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&fde_003b1990 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b19a1 + param_1 + 7;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)(&uleb128_003b19a0 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b19a1 + param_1 + 0xf;
      pbVar2 = BYTE_ARRAY_003b19a1 + param_1 + 0x17;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b19a1 + param_1 + 0x1f;
      pbVar2 = BYTE_ARRAY_003b19a1 + param_1 + 0x27;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b19a1 + param_1 + 0x2f;
      pbVar2 = BYTE_ARRAY_003b19a1 + param_1 + 0x37;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b19a1 + param_1 + 0x3f;
      *(undefined8 *)((long)&DWORD_003b19e8 + param_1) = 0xffffffffffffffff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b19f5 + param_1 + 3;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&DWORD_003b19f0 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b19f5 + param_1 + 0xb;
      pbVar2 = BYTE_ARRAY_003b19f5 + param_1 + 0x13;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b19f5 + param_1 + 0x1b;
      pbVar2 = BYTE_ARRAY_003b19f5 + param_1 + 0x23;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&DWORD_003b1a28 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b1a20 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b1a2d + param_1 + 3;
      pbVar2 = BYTE_ARRAY_003b1a2d + param_1 + 0xb;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      pbVar8 = BYTE_ARRAY_003b1a2d + param_1 + 0x13;
      pbVar2 = BYTE_ARRAY_003b1a2d + param_1 + 0x1b;
      pbVar2[0] = 0xff;
      pbVar2[1] = 0xff;
      pbVar2[2] = 0xff;
      pbVar2[3] = 0xff;
      pbVar2[4] = 0xff;
      pbVar2[5] = 0xff;
      pbVar2[6] = 0xff;
      pbVar2[7] = 0xff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&QWORD_003b18e8 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b18e0 + param_1) = 0xffffffffffffffff;
      puVar3 = PTR_DAT_00c9abb0;
      pbVar8 = BYTE_ARRAY_003b18b1 + param_1 + 0xf;
      *(undefined8 *)((long)&fde_003b18c8 + param_1) = 0xffffffffffffffff;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)((long)&QWORD_003b18d4 + param_1 + 4) = 0xffffffffffffffff;
      *(undefined8 *)((long)&DWORD_003b18d0 + param_1) = 0xffffffffffffffff;
      puVar4 = 
      PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8;
      *(undefined8 *)((long)&DWORD_003b18a8 + param_1) = 0xffffffffffffffff;
      *(undefined8 *)((long)&fde_003b18a0 + param_1) = 0xffffffffffffffff;
      pbVar8 = BYTE_ARRAY_003b18b1 + param_1 + 7;
      pbVar8[0] = 0xff;
      pbVar8[1] = 0xff;
      pbVar8[2] = 0xff;
      pbVar8[3] = 0xff;
      pbVar8[4] = 0xff;
      pbVar8[5] = 0xff;
      pbVar8[6] = 0xff;
      pbVar8[7] = 0xff;
      *(undefined8 *)(&uleb128_003b18b0 + param_1) = 0xffffffffffffffff;
      local_1a0 = (undefined **)(puVar3 + 0x10);
      local_158 = *(long *)puVar4;
      *(undefined8 *)((long)&local_158 + *(long *)(local_158 + -0x18)) =
           *(undefined8 *)(puVar4 + 0x18);
      local_150[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0
                     + 0x10;
      if ((local_110 & 1) != 0) {
        _ZdlPv(local_100);
      }
      _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_150);
      _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_158,puVar4 + 8);
                    /* try { // try from 009d0278 to 00ad02f7 has its CatchHandler @ 009cfe24 */
      _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_e8);
      if ((local_180 & 1) != 0) {
        _ZdlPv(local_170);
      }
      if (local_198 != (void *)0x0) {
        local_190 = local_198;
        _ZdlPv(local_198);
      }
      if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
        __stack_chk_fail();
      }
                    /* catch() { ... } // from try @ 009d00a0 with catch @ 009d02bc
                       catch() { ... } // from try @ 009d01c8 with catch @ 009d02bc */
                    /* catch() { ... } // from try @ 009d019c with catch @ 009d02c0 */
                    /* catch() { ... } // from try @ 009d00d8 with catch @ 009d02c4 */
      return;
    }
  } while( true );
}

~~~
