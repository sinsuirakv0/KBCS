# 00aeb9ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

## 関数情報

~~~json
{
  "address": "00aeb9ac",
  "name": "FUN_00aeb9ac",
  "size": 420,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "70fdb1566cd55805bce5297bda9c319271851acb9ecc43b3635831e42b9bf0ef",
  "source_text_sha256": "70fdb1566cd55805bce5297bda9c319271851acb9ecc43b3635831e42b9bf0ef"
}
~~~

## 呼び出し元

- [00b28f54](../00b28/00b28f54.md)

## 呼び出し先

- [0048791c](../00487/0048791c.md)
- [0048793c](../00487/0048793c.md)
- [00487e20](../00487/00487e20.md)
- [00488658](../00488/00488658.md)
- [00b110ec](../00b11/00b110ec.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57fa0](../00c57/00c57fa0.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)

## 関連文字列（未確認候補）

~~~text
"UnitSlot_UnlockData.csv"
~~~

## 疑似コード / UTF-8 4083 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00aeb9ac(long param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined *puVar4;
  undefined4 uVar5;
  ulong uVar6;
  undefined4 *puVar7;
  long lVar8;
  ulong local_1c0;
  undefined8 uStack_1b8;
  char *local_1b0;
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
  
                    /* try { // try from 00aeb9b4 to 00beb9c3 has its CatchHandler @ 00aebe90 */
                    /* try { // try from 00aeb9c4 to 00beb9d3 has its CatchHandler @ 00aebe88 */
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00aeb9d4 to 00beb9eb has its CatchHandler @ 00aebe80 */
  FUN_00487e20(&local_1a0);
  local_1a0 = &PTR_FUN_00c64d38;
  local_1b0 = (char *)_Znwm(0x19);
  uStack_1b8 = _UNK_002c2458;
  local_1c0 = _DAT_002c2450;
  uVar3 = s_UnitSlot_UnlockData_csv_002a6f6c._0_8_;
  uVar2 = CONCAT71(s_UnitSlot_UnlockData_csv_002a6f6c._16_7_,s_UnitSlot_UnlockData_csv_002a6f6c[0xf]
                  );
                    /* try { // try from 00aeba04 to 00beba13 has its CatchHandler @ 00aebe38 */
  *(ulong *)(local_1b0 + 8) =
       CONCAT17(s_UnitSlot_UnlockData_csv_002a6f6c[0xf],s_UnitSlot_UnlockData_csv_002a6f6c._8_7_);
  *(undefined8 *)local_1b0 = uVar3;
  *(undefined8 *)(local_1b0 + 0xf) = uVar2;
                    /* try { // try from 00aeba14 to 00beba37 has its CatchHandler @ 00aebe78 */
  local_1b0[0x17] = '\0';
  uVar6 = FUN_00b110ec(&local_1a0,&local_1c0,0,0);
  if ((local_1c0 & 1) != 0) {
    _ZdlPv(local_1b0);
  }
  if ((uVar6 & 1) != 0) {
    FUN_0048791c(&local_1a0);
    lVar8 = 0x13;
    puVar7 = (undefined4 *)((long)&QWORD_0039b984 + param_1 + 4);
    do {
      FUN_0048791c(&local_1a0);
      uVar5 = FUN_0048793c(&local_1a0,0);
      puVar7[-1] = uVar5;
      uVar5 = FUN_0048793c(&local_1a0,1);
                    /* try { // try from 00aeba80 to 00beba8f has its CatchHandler @ 00aebe8c */
      lVar8 = lVar8 + -1;
      *puVar7 = uVar5;
      puVar7 = puVar7 + 2;
    } while (lVar8 != 0);
                    /* try { // try from 00aeba90 to 00beba9f has its CatchHandler @ 00aebe84 */
    FUN_00488658(&local_1a0);
  }
  puVar4 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
  ;
                    /* try { // try from 00aebaa0 to 00bebab7 has its CatchHandler @ 00aebe7c */
  local_158 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
  ;
  local_1a0 = (undefined **)(PTR_DAT_00c9abb0 + 0x10);
  *(undefined8 *)((long)&local_158 + *(long *)(local_158 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8 +
        0x18);
                    /* try { // try from 00aebad0 to 00bebadf has its CatchHandler @ 00aebe34 */
  local_150[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0
                 + 0x10;
  if ((local_110 & 1) != 0) {
                    /* try { // try from 00aebae0 to 00bebb03 has its CatchHandler @ 00aebe74 */
    _ZdlPv(local_100);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_150);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_158,puVar4 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_e8);
  if ((local_180 & 1) != 0) {
    _ZdlPv(local_170);
  }
  if (local_198 != (void *)0x0) {
    local_190 = local_198;
    _ZdlPv(local_198);
  }
                    /* try { // try from 00aebb30 to 00bebb3f has its CatchHandler @ 00aebe10 */
  if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* try { // try from 00aebb48 to 00bebb57 has its CatchHandler @ 00aebe08 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
