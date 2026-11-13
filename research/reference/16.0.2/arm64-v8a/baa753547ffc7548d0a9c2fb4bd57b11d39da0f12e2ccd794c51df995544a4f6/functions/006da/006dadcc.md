# 006dadcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

## 関数情報

~~~json
{
  "address": "006dadcc",
  "name": "FUN_006dadcc",
  "size": 400,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9188979e18b5a60d774cce7363860d5932b3b295313e576c6853858b3861bfbd",
  "source_text_sha256": "9188979e18b5a60d774cce7363860d5932b3b295313e576c6853858b3861bfbd"
}
~~~

## 呼び出し元

- [00b11e20](../00b11/00b11e20.md)

## 呼び出し先

- [00487e60](../00487/00487e60.md)
- [00488698](../00488/00488698.md)
- [006dac04](../006da/006dac04.md)
- [00b11188](../00b11/00b11188.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c58070](../00c58/00c58070.md)
- [00c58080](../00c58/00c58080.md)
- [00c58090](../00c58/00c58090.md)

## 関連文字列（未確認候補）

~~~text
"Gamatoto_Bonus.csv"
~~~

## 疑似コード / UTF-8 5341 bytes

~~~c

void FUN_006dadcc(long param_1)

{
  long lVar1;
  undefined *puVar2;
  ulong uVar3;
  void *__ptr;
  byte local_1c0;
  undefined7 uStack_1bf;
  char cStack_1b8;
  undefined7 uStack_1b7;
  char cStack_1b0;
  undefined2 uStack_1af;
  undefined1 uStack_1ad;
  undefined4 uStack_1ac;
  undefined8 local_1a8;
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
  
                    /* try { // try from 006dadcc to 007daddb has its CatchHandler @ 006daf04 */
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  FUN_00487e60(&local_1a0);
  local_1a0 = &PTR_FUN_00c64e08;
                    /* try { // try from 006dae0c to 007dae1f has its CatchHandler @ 006daf30 */
  local_1c0 = 0x24;
  uStack_1af = 0x7673;
                    /* try { // try from 006dae24 to 007dae5b has its CatchHandler @ 006daf48 */
  uStack_1ad = 0;
  uStack_1b7 = (undefined7)s_Gamatoto_Bonus_csv_002b76bb._8_8_;
  cStack_1b0 = SUB81(s_Gamatoto_Bonus_csv_002b76bb._8_8_,7);
  uStack_1bf = (undefined7)s_Gamatoto_Bonus_csv_002b76bb._0_8_;
  cStack_1b8 = SUB81(s_Gamatoto_Bonus_csv_002b76bb._0_8_,7);
  uVar3 = FUN_00b11188(&local_1a0,&local_1c0,0,0);
  if ((local_1c0 & 1) != 0) {
    _ZdlPv((void *)CONCAT44(uStack_1ac,CONCAT13(uStack_1ad,CONCAT21(uStack_1af,cStack_1b0))));
  }
  if ((uVar3 & 1) != 0) {
                    /* try { // try from 006dae5c to 007daecb has its CatchHandler @ 006da6ec */
    FUN_006dac04(&local_1c0,&local_1a0);
    __ptr = *(void **)(param_1 + 0x20);
    *(ulong *)(param_1 + 0x18) = CONCAT71(uStack_1bf,local_1c0);
    if (__ptr != (void *)0x0) {
      *(void **)(param_1 + 0x28) = __ptr;
      _ZdlPv(__ptr);
      *(undefined8 *)(param_1 + 0x20) = 0;
      *(undefined8 *)(param_1 + 0x28) = 0;
      *(undefined8 *)(param_1 + 0x30) = 0;
    }
    *(ulong *)(param_1 + 0x28) =
         CONCAT44(uStack_1ac,CONCAT13(uStack_1ad,CONCAT21(uStack_1af,cStack_1b0)));
    *(ulong *)(param_1 + 0x20) = CONCAT71(uStack_1b7,cStack_1b8);
    *(undefined8 *)(param_1 + 0x30) = local_1a8;
    FUN_00488698(&local_1a0);
  }
  puVar2 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
  ;
  local_158 = *(long *)
               PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
  ;
  local_1a0 = (undefined **)(PTR_DAT_00c9ac80 + 0x10);
                    /* try { // try from 006daecc to 007daed3 has its CatchHandler @ 006daf70 */
  *(undefined8 *)((long)&local_158 + *(long *)(local_158 + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88 +
        0x18);
  local_150[0] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac90
                 + 0x10;
                    /* try { // try from 006daee4 to 007daeeb has its CatchHandler @ 006daf68 */
  if ((local_110 & 1) != 0) {
                    /* catch() { ... } // from try @ 006dad34 with catch @ 006daeec
                       try { // try from 006daeec to 007dafcb has its CatchHandler @ 006da6ec */
    _ZdlPv(local_100);
  }
                    /* catch() { ... } // from try @ 006dacf8 with catch @ 006daef4 */
                    /* catch() { ... } // from try @ 006dace8 with catch @ 006daef8 */
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_150);
                    /* catch() { ... } // from try @ 006dacd0 with catch @ 006daf00 */
                    /* catch() { ... } // from try @ 006dadcc with catch @ 006daf04 */
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(&local_158,puVar2 + 8);
                    /* catch() { ... } // from try @ 006daa80 with catch @ 006daf08
                       catch() { ... } // from try @ 006dadbc with catch @ 006daf08 */
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(auStack_e8);
                    /* catch() { ... } // from try @ 006dad68 with catch @ 006daf10 */
  if ((local_180 & 1) != 0) {
                    /* catch() { ... } // from try @ 006daa3c with catch @ 006daf18 */
                    /* catch() { ... } // from try @ 006daa2c with catch @ 006daf1c */
    _ZdlPv(local_170);
  }
                    /* catch() { ... } // from try @ 006dacc0 with catch @ 006daf24 */
  if (local_198 != (void *)0x0) {
                    /* catch() { ... } // from try @ 006daa9c with catch @ 006daf28 */
    local_190 = local_198;
                    /* catch() { ... } // from try @ 006dad80 with catch @ 006daf2c */
    _ZdlPv(local_198);
  }
                    /* catch() { ... } // from try @ 006dae0c with catch @ 006daf30 */
                    /* catch() { ... } // from try @ 006dac80 with catch @ 006daf38 */
  if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* catch() { ... } // from try @ 006daaac with catch @ 006daf40 */
                    /* catch() { ... } // from try @ 006da9d0 with catch @ 006daf44 */
                    /* catch() { ... } // from try @ 006dae24 with catch @ 006daf48 */
                    /* catch() { ... } // from try @ 006dac38 with catch @ 006daf4c */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
