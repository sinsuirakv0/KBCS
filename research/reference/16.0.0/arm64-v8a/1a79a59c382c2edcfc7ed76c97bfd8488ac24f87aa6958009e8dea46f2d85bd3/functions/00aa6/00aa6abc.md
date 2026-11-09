# 00aa6abc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aa6abc",
  "name": "FUN_00aa6abc",
  "size": 520,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f3bbcc15dcc3a7eeb3de8de76ea00570de7db0b9731d6662fffca4c8ad286f6",
  "source_text_sha256": "2f3bbcc15dcc3a7eeb3de8de76ea00570de7db0b9731d6662fffca4c8ad286f6"
}
~~~

## 呼び出し元

- [00aa3c28](../00aa3/00aa3c28.md)

## 呼び出し先

- [006ea4b4](../006ea/006ea4b4.md)
- [00784240](../00784/00784240.md)
- [008514b8](../00851/008514b8.md)
- [0087925c](../00879/0087925c.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a430](../00c5a/00c5a430.md)
- [00c5a440](../00c5a/00c5a440.md)
- [00c5a4f0](../00c5a/00c5a4f0.md)

## 関連文字列（未確認候補）

~~~text
"BcResGamatoto"
"Message"
"StageName"
"sec1_id"
"sec1_type"
"sec2_id"
"sec2_type"
~~~

## 疑似コード / UTF-8 2559 bytes

~~~c

void FUN_00aa6abc(undefined4 param_1,int param_2)

{
  long lVar1;
  long lVar2;
  undefined1 auStack_128 [24];
  byte local_110 [16];
  void *local_100;
  undefined1 auStack_f8 [24];
  undefined4 local_e0 [2];
  char *local_d8;
  char *local_c8;
  undefined4 local_c0 [2];
  undefined8 local_b8;
  char *local_a8;
  undefined4 local_a0 [2];
  undefined8 local_98;
  char *local_88;
  undefined4 local_80 [2];
  undefined8 local_78;
  char *local_68;
  undefined4 local_60 [2];
  undefined8 local_58;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  local_c8 = "sec1_type";
  local_c0[0] = 0;
  local_b8 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
  local_d8 = "StageName";
  _ZN8firebase7VariantaSEOS0_(local_c0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  lVar2 = FUN_008514b8(&local_c8);
  FUN_006ea4b4(local_110,lVar2 + 0x42ef90,param_1);
  FUN_00784240(auStack_f8,local_110);
                    /* catch() { ... } // from try @ 00aa6bcc with catch @ 00aa6b60 */
  local_a8 = "sec1_id";
  local_a0[0] = 0;
  local_98 = 0;
  _ZN8firebase7VariantaSERKS0_(local_a0,auStack_f8);
  local_88 = "sec2_type";
  local_80[0] = 0;
  local_78 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
  local_d8 = "Message";
                    /* try { // try from 00aa6bc0 to 00ba6bcb has its CatchHandler @ 00aa6c28 */
  _ZN8firebase7VariantaSEOS0_(local_80,local_e0);
                    /* try { // try from 00aa6bcc to 00ba6c67 has its CatchHandler @ 00aa6b60 */
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  lVar2 = FUN_008514b8(&local_c8);
  FUN_00784240(auStack_128,lVar2 + (long)param_2 * 0x78 + 0x44abf8);
  local_68 = "sec2_id";
  local_60[0] = 0;
  local_58 = 0;
  _ZN8firebase7VariantaSERKS0_(local_60,auStack_128);
  _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_128,0);
                    /* catch() { ... } // from try @ 00aa6bc0 with catch @ 00aa6c28 */
  _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_f8,0);
  if ((local_110[0] & 1) != 0) {
    _ZdlPv(local_100);
  }
  lVar2 = FUN_008514b8();
  FUN_0087925c(*(undefined8 *)(lVar2 + 0x22b0),"BcResGamatoto",&local_c8,4);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_60,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_80,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_a0,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_c0,0);
  if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
