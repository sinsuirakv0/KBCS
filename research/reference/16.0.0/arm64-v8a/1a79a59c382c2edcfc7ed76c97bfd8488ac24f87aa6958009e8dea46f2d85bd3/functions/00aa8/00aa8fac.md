# 00aa8fac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00aa8fac",
  "name": "FUN_00aa8fac",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "17edc4ad4be8c15296ae8fe1599524eea718f3206d2cf0a3d7837317564c9e8d",
  "source_text_sha256": "17edc4ad4be8c15296ae8fe1599524eea718f3206d2cf0a3d7837317564c9e8d"
}
~~~

## 呼び出し元

- [00aa3c28](../00aa3/00aa3c28.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)
- [0087925c](../00879/0087925c.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a430](../00c5a/00c5a430.md)
- [00c5a440](../00c5a/00c5a440.md)

## 関連文字列（未確認候補）

~~~text
"BcResExUnit"
"CharaID"
"Price"
"sec1_id"
"sec1_type"
"sec2_id"
"sec2_type"
~~~

## 疑似コード / UTF-8 2079 bytes

~~~c

void FUN_00aa8fac(int param_1,ulong param_2)

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
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
  local_d8 = "CharaID";
  _ZN8firebase7VariantaSEOS0_(local_c0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_a0[0] = 0;
  local_a8 = "sec1_id";
  local_98 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,1);
  local_d8 = (char *)(long)param_1;
  _ZN8firebase7VariantaSEOS0_(local_a0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_80[0] = 0;
  local_88 = "sec2_type";
  local_78 = 0;
                    /* catch() { ... } // from try @ 00aa8e8c with catch @ 00aa9094 */
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
  local_d8 = "Price";
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
  lVar2 = FUN_008514b8();
  FUN_0087925c(*(undefined8 *)(lVar2 + 0x22b0),"BcResExUnit",&local_c8,4);
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
