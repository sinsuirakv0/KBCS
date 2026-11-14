# 00aa9fec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

## 関数情報

~~~json
{
  "address": "00aa9fec",
  "name": "FUN_00aa9fec",
  "size": 372,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9c7411e2e1d756415dfaa541f48ec0d8b0d90858882d1744240916f02fc22cc9",
  "source_text_sha256": "9c7411e2e1d756415dfaa541f48ec0d8b0d90858882d1744240916f02fc22cc9"
}
~~~

## 呼び出し元

- [00aa4e88](../00aa4/00aa4e88.md)

## 呼び出し先

- [007846b4](../00784/007846b4.md)
- [008524fc](../00852/008524fc.md)
- [0087a2a0](../0087a/0087a2a0.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c590a0](../00c59/00c590a0.md)
- [00c5b8d0](../00c5b/00c5b8d0.md)
- [00c5b8e0](../00c5b/00c5b8e0.md)
- [00c5b990](../00c5b/00c5b990.md)

## 関連文字列（未確認候補）

~~~text
"BcResBeaconCharacter"
"BcResBeaconItem"
"CharaID"
"ItemID"
"sec1_id"
"sec1_type"
~~~

## 疑似コード / UTF-8 1907 bytes

~~~c

void FUN_00aa9fec(int param_1,int param_2)

{
  size_t __n;
  char *pcVar1;
  long lVar2;
  bool bVar3;
  long lVar4;
  undefined1 auStack_d0 [24];
  byte local_b8 [16];
  void *local_a8;
  undefined4 local_a0 [2];
  long local_98;
  char *local_88;
  undefined4 local_80 [2];
  undefined8 local_78;
  char *local_68;
  undefined4 local_60 [2];
  undefined8 local_58;
  long local_48;
  
  lVar2 = tpidr_el0;
  bVar3 = param_1 != 0x34;
  local_48 = *(long *)(lVar2 + 0x28);
  __n = 6;
  if (bVar3) {
    __n = 7;
  }
                    /* try { // try from 00aaa028 to 00baa0af has its CatchHandler @ 00aaa230 */
  pcVar1 = "ItemID";
  if (bVar3) {
    pcVar1 = "CharaID";
  }
  local_b8[0] = (byte)((int)__n << 1);
  lVar4 = 7;
  if (bVar3) {
    lVar4 = 8;
  }
  memcpy((void *)((ulong)local_b8 | 1),pcVar1,__n);
  local_b8[lVar4] = 0;
  FUN_007846b4(auStack_d0,local_b8);
  local_88 = "sec1_type";
  local_80[0] = 0;
  local_78 = 0;
  _ZN8firebase7VariantaSERKS0_(local_80,auStack_d0);
  local_60[0] = 0;
  local_68 = "sec1_id";
  local_58 = 0;
  local_a0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_a0,1);
  local_98 = (long)param_2;
                    /* try { // try from 00aaa0b0 to 00baa2ff has its CatchHandler @ 00aa9ed4 */
  _ZN8firebase7VariantaSEOS0_(local_60,local_a0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_a0,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(auStack_d0,0);
  lVar4 = FUN_008524fc();
  pcVar1 = "BcResBeaconItem";
  if (param_1 != 0x34) {
    pcVar1 = "BcResBeaconCharacter";
  }
  FUN_0087a2a0(*(undefined8 *)(lVar4 + 0x22b0),pcVar1,&local_88,2);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_60,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_80,0);
  if ((local_b8[0] & 1) != 0) {
    _ZdlPv(local_a8);
  }
  if (*(long *)(lVar2 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
