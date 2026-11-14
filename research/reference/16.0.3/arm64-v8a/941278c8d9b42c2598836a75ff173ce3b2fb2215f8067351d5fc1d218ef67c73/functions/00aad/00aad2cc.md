# 00aad2cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aad2cc",
  "name": "FUN_00aad2cc",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "988a4494a452b591acbff2f957c37f4372a0676be638e9a0d58c2f0c4992a537",
  "source_text_sha256": "988a4494a452b591acbff2f957c37f4372a0676be638e9a0d58c2f0c4992a537"
}
~~~

## 呼び出し元

- [00aa4e88](../00aa4/00aa4e88.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)
- [0087a2a0](../0087a/0087a2a0.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5b8d0](../00c5b/00c5b8d0.md)
- [00c5b8e0](../00c5b/00c5b8e0.md)

## 関連文字列（未確認候補）

~~~text
"BcResSlot"
"Sale"
"SlotID"
"sec1_id"
"sec1_type"
"sec2_id"
"sec2_type"
~~~

## 疑似コード / UTF-8 2718 bytes

~~~c

void FUN_00aad2cc(int param_1,ulong param_2)

{
  long lVar1;
  long lVar2;
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
                    /* try { // try from 00aad318 to 00bad31b has its CatchHandler @ 00aad3c4 */
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
  local_d8 = "SlotID";
  _ZN8firebase7VariantaSEOS0_(local_c0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_a0[0] = 0;
  local_a8 = "sec1_id";
                    /* try { // try from 00aad358 to 00bad35f has its CatchHandler @ 00aad3cc */
  local_98 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,1);
  local_d8 = (char *)(long)param_1;
  _ZN8firebase7VariantaSEOS0_(local_a0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_80[0] = 0;
  local_88 = "sec2_type";
  local_78 = 0;
  local_e0[0] = 0;
                    /* try { // try from 00aad3bc to 00bad3c3 has its CatchHandler @ 00aad3c4 */
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
                    /* catch() { ... } // from try @ 00aad318 with catch @ 00aad3c4
                       catch() { ... } // from try @ 00aad3bc with catch @ 00aad3c4
                       try { // try from 00aad3c4 to 00bad3ff has its CatchHandler @ 00aad2b8 */
                    /* catch() { ... } // from try @ 00aad358 with catch @ 00aad3cc */
  local_d8 = "Sale";
  _ZN8firebase7VariantaSEOS0_(local_80,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_60[0] = 0;
  local_68 = "sec2_id";
  local_58 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,1);
  local_d8 = (char *)(param_2 & 1);
  _ZN8firebase7VariantaSEOS0_(local_60,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  lVar2 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00aad620 with catch @ 00aad444 */
  FUN_0087a2a0(*(undefined8 *)(lVar2 + 0x22b0),"BcResSlot",&local_c8,4);
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
