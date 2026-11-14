# 00aeca3c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aeca3c",
  "name": "FUN_00aeca3c",
  "size": 420,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7aee08561ca9960b29b52f7fab8ca70984c55d98c80871e92ae699f694a3f337",
  "source_text_sha256": "7aee08561ca9960b29b52f7fab8ca70984c55d98c80871e92ae699f694a3f337"
}
~~~

## 呼び出し元

- [00b29fe4](../00b29/00b29fe4.md)

## 呼び出し先

- [00487c7c](../00487/00487c7c.md)
- [00487c9c](../00487/00487c9c.md)
- [00488180](../00488/00488180.md)
- [004889b8](../00488/004889b8.md)
- [00b1217c](../00b12/00b1217c.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59040](../00c59/00c59040.md)
- [00c59050](../00c59/00c59050.md)
- [00c59060](../00c59/00c59060.md)

## 関連文字列（未確認候補）

~~~text
"UnitSlot_UnlockData.csv"
~~~

## 疑似コード / UTF-8 3788 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00aeca3c(long param_1)

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
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  FUN_00488180(&local_1a0);
  local_1a0 = &PTR_FUN_00c65dd8;
  local_1b0 = (char *)_Znwm(0x19);
  uStack_1b8 = _UNK_002c24e8;
  local_1c0 = _DAT_002c24e0;
  uVar3 = s_UnitSlot_UnlockData_csv_002a7068._0_8_;
                    /* try { // try from 00aeca80 to 00beca8f has its CatchHandler @ 00aece8c */
                    /* try { // try from 00aeca90 to 00beca9f has its CatchHandler @ 00aece84 */
  uVar2 = CONCAT71(s_UnitSlot_UnlockData_csv_002a7068._16_7_,s_UnitSlot_UnlockData_csv_002a7068[0xf]
                  );
  *(ulong *)(local_1b0 + 8) =
       CONCAT17(s_UnitSlot_UnlockData_csv_002a7068[0xf],s_UnitSlot_UnlockData_csv_002a7068._8_7_);
  *(undefined8 *)local_1b0 = uVar3;
                    /* try { // try from 00aecaa0 to 00becab7 has its CatchHandler @ 00aece7c */
  *(undefined8 *)(local_1b0 + 0xf) = uVar2;
  local_1b0[0x17] = '\0';
  uVar6 = FUN_00b1217c(&local_1a0,&local_1c0,0,0);
  if ((local_1c0 & 1) != 0) {
                    /* try { // try from 00aecad0 to 00becadf has its CatchHandler @ 00aece34 */
    _ZdlPv(local_1b0);
  }
  if ((uVar6 & 1) != 0) {
    FUN_00487c7c(&local_1a0);
                    /* try { // try from 00aecae0 to 00becb03 has its CatchHandler @ 00aece74 */
    lVar8 = 0x13;
    puVar7 = (undefined4 *)((long)&DWORD_0039b988 + param_1);
    do {
      FUN_00487c7c(&local_1a0);
      uVar5 = FUN_00487c9c(&local_1a0,0);
      puVar7[-1] = uVar5;
      uVar5 = FUN_00487c9c(&local_1a0,1);
      lVar8 = lVar8 + -1;
      *puVar7 = uVar5;
      puVar7 = puVar7 + 2;
    } while (lVar8 != 0);
    FUN_004889b8(&local_1a0);
  }
  puVar4 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9bc58
  ;
                    /* try { // try from 00aecb30 to 00becb3f has its CatchHandler @ 00aece10 */
  local_158 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9bc58
  ;
  local_1a0 = (undefined **)(PTR_DAT_00c9bc50 + 0x10);
                    /* try { // try from 00aecb48 to 00becb57 has its CatchHandler @ 00aece08 */
  *(undefined8 *)((long)&local_158 + *(long *)(local_158 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9bc58 +
        0x18);
  local_150[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9bc60
                 + 0x10;
                    /* try { // try from 00aecb68 to 00becb6f has its CatchHandler @ 00aece4c */
  if ((local_110 & 1) != 0) {
                    /* try { // try from 00aecb70 to 00becbff has its CatchHandler @ 00aebf84 */
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
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
