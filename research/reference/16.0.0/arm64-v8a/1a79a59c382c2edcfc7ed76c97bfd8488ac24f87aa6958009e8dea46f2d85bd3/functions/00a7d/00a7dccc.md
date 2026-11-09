# 00a7dccc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

## 関数情報

~~~json
{
  "address": "00a7dccc",
  "name": "FUN_00a7dccc",
  "size": 452,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3ee0e29b134af75aa520adb5b50f39fbcc31fd79dcac008d375a57ed19d506b5",
  "source_text_sha256": "3ee0e29b134af75aa520adb5b50f39fbcc31fd79dcac008d375a57ed19d506b5"
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0047acb4](../0047a/0047acb4.md)
- [0047cd94](../0047c/0047cd94.md)
- [0048ce10](../0048c/0048ce10.md)
- [0048ce14](../0048c/0048ce14.md)
- [008b79cc](../008b7/008b79cc.md)
- [008ba824](../008ba/008ba824.md)
- [00a7df80](../00a7d/00a7df80.md)
- [00a7df84](../00a7d/00a7df84.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

## 関連文字列（未確認候補）

~~~text
"network_unavailable"
~~~

## 疑似コード / UTF-8 2781 bytes

~~~c

void FUN_00a7dccc(long param_1,undefined8 param_2,int *param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  ulong uVar4;
  undefined ***pppuVar5;
  undefined8 uVar6;
  long lVar7;
  byte local_a0;
  char local_9f [8];
  undefined7 uStack_97;
  undefined4 uStack_90;
  uint uStack_8c;
  byte local_88 [16];
  void *local_78;
  undefined **local_70 [4];
  undefined ***local_50;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_3;
  lVar7 = *(long *)(param_1 + 8);
  if (iVar1 == 4) {
    uVar4 = thunk_FUN_00497890();
    if ((uVar4 & 1) != 0) {
      *(undefined4 *)(lVar7 + 0x3478) = 0x2f;
      *(undefined4 *)((long)&QWORD_0039b1b4 + lVar7) = 2;
      if (*(long *)(lVar2 + 0x28) == local_38) {
        FUN_008b79cc(lVar7 + 0x2f38,0);
        return;
      }
      goto LAB_00a7dedc;
    }
    local_a0 = 0x26;
    uStack_97 = (undefined7)s_network_unavailable_002b4b6a._8_8_;
    uStack_90 = CONCAT31(0x656c62,SUB81(s_network_unavailable_002b4b6a._8_8_,7));
    local_9f[0] = s_network_unavailable_002b4b6a[0];
    local_9f[1] = s_network_unavailable_002b4b6a[1];
    local_9f[2] = s_network_unavailable_002b4b6a[2];
    local_9f[3] = s_network_unavailable_002b4b6a[3];
    local_9f[4] = s_network_unavailable_002b4b6a[4];
    local_9f[5] = s_network_unavailable_002b4b6a[5];
    local_9f[6] = s_network_unavailable_002b4b6a[6];
    local_9f[7] = s_network_unavailable_002b4b6a[7];
    uStack_8c = uStack_8c & 0xffffff00;
    FUN_0048ce14(local_88,&local_a0);
    local_70[0] = &PTR_FUN_00c8ba90;
    local_50 = local_70;
    FUN_008ba824(lVar7 + 0x2f08,local_88,0,0,0x24,local_70);
    if (local_50 == local_70) {
      lVar7 = 0x20;
      pppuVar5 = local_70;
LAB_00a7de3c:
      (**(code **)((long)*pppuVar5 + lVar7))();
    }
    else if (local_50 != (undefined ***)0x0) {
      lVar7 = 0x28;
      pppuVar5 = local_50;
      goto LAB_00a7de3c;
    }
    if ((local_88[0] & 1) != 0) {
      _ZdlPv(local_78);
    }
    if ((local_a0 & 1) != 0) {
      _ZdlPv((void *)CONCAT44(uStack_8c,uStack_90));
    }
  }
  else {
    if (iVar1 == 3) {
      uVar3 = FUN_0047acb4();
      if (*(long *)(lVar2 + 0x28) != local_38) goto LAB_00a7dedc;
      uVar6 = 0xb;
LAB_00a7dd4c:
      FUN_0047cd94(uVar3,uVar6,0);
      return;
    }
    if (iVar1 == 0) {
      *(undefined1 *)((long)&fde_table_entry_0033e360.initial_loc + lVar7) = 0;
      *(undefined1 *)((long)&fde_table_entry_0033e368.initial_loc + lVar7) = 0;
      uVar3 = FUN_0047acb4();
      if (*(long *)(lVar2 + 0x28) != local_38) goto LAB_00a7dedc;
      uVar6 = 10;
      goto LAB_00a7dd4c;
    }
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
LAB_00a7dedc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
