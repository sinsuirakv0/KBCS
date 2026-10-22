# 00ad7ebc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

ページ 1/1。[入口](00ad7ebc.md)

## 関数情報

~~~json
{
  "address": "00ad7ebc",
  "name": "FUN_00ad7ebc",
  "size": 968,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "85d549b260e2e10f727a63ec3bcc454e4badbd023db10e5ad23b719b65259c3e",
  "source_text_sha256": "85d549b260e2e10f727a63ec3bcc454e4badbd023db10e5ad23b719b65259c3e"
}
~~~
## 呼び出し元

- [00855450](../00855/00855450.md)

## 呼び出し先

- [00418c24](../00418/00418c24.md)
- [00551e14](../00551/00551e14.md)
- [00565f94](../00565/00565f94.md)
- [0056626c](../00566/0056626c.md)
- [00566284](../00566/00566284.md)
- [00566448](../00566/00566448.md)
- [00566978](../00566/00566978.md)
- [00566980](../00566/00566980.md)
- [005669f8](../00566/005669f8.md)
- [005679e4](../00567/005679e4.md)
- [00ad8390](../00ad8/00ad8390.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)

## 関連文字列（未確認候補）

~~~text
"(Ljava/lang/String;)V"
"ironsourceShow"
~~~
## 疑似コード 1/1 / UTF-8 7116 bytes

~~~c

void FUN_00ad7ebc(char *param_1,long *param_2,long *param_3,long *param_4,long *param_5)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  ulong uVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  long *plVar8;
  byte *pbVar9;
  size_t __n;
  undefined8 uVar10;
  long lVar11;
  void *__dest;
  byte local_140;
  undefined7 uStack_13f;
  char cStack_138;
  char acStack_137 [5];
  undefined2 uStack_132;
  char cStack_130;
  char acStack_12f [5];
  undefined1 uStack_12a;
  undefined1 uStack_129;
  long local_128;
  byte local_120;
  char acStack_11f [6];
  char acStack_119 [2];
  char acStack_117 [6];
  undefined1 local_111;
  void *local_110;
  byte *local_100;
  long local_f0 [4];
  long *local_d0;
  long local_c0 [4];
  long *local_a0;
  long local_90 [4];
  long *local_70;
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  uVar2 = FUN_00565f94();
  uVar3 = FUN_00566284();
  local_120 = 0x1c;
  local_111 = 0;
  acStack_11f[0] = s_ironsourceShow_002a700a[0];
  acStack_11f[1] = s_ironsourceShow_002a700a[1];
  acStack_11f[2] = s_ironsourceShow_002a700a[2];
  acStack_11f[3] = s_ironsourceShow_002a700a[3];
  acStack_11f[4] = s_ironsourceShow_002a700a[4];
  acStack_11f[5] = s_ironsourceShow_002a700a[5];
  acStack_119[0] = s_ironsourceShow_002a700a[6];
  acStack_119[1] = s_ironsourceShow_002a700a[7];
  acStack_117[0] = s_ironsourceShow_002a700a[8];
  acStack_117[1] = s_ironsourceShow_002a700a[9];
  acStack_117[2] = s_ironsourceShow_002a700a[10];
  acStack_117[3] = s_ironsourceShow_002a700a[0xb];
  acStack_117[4] = s_ironsourceShow_002a700a[0xc];
  acStack_117[5] = s_ironsourceShow_002a700a[0xd];
  local_140 = 0x2a;
  acStack_137[0] = s__Ljava_lang_String__V_002aa71f[8];
  acStack_137[1] = s__Ljava_lang_String__V_002aa71f[9];
  acStack_137[2] = s__Ljava_lang_String__V_002aa71f[10];
  acStack_137[3] = s__Ljava_lang_String__V_002aa71f[0xb];
  acStack_137[4] = s__Ljava_lang_String__V_002aa71f[0xc];
  uStack_13f = (undefined7)s__Ljava_lang_String__V_002aa71f._0_8_;
  cStack_138 = SUB81(s__Ljava_lang_String__V_002aa71f._0_8_,7);
  uStack_132 = (undefined2)s__Ljava_lang_String__V_002aa71f._13_3_;
  cStack_130 = SUB31(s__Ljava_lang_String__V_002aa71f._13_3_,2);
  acStack_12f[0] = s__Ljava_lang_String__V_002aa71f[0x10];
  acStack_12f[1] = s__Ljava_lang_String__V_002aa71f[0x11];
  acStack_12f[2] = s__Ljava_lang_String__V_002aa71f[0x12];
  acStack_12f[3] = s__Ljava_lang_String__V_002aa71f[0x13];
  acStack_12f[4] = s__Ljava_lang_String__V_002aa71f[0x14];
  uStack_12a = 0;
  local_128 = FUN_00566448(uVar3,&local_120,&local_140,uVar2);
  if ((local_140 & 1) != 0) {
    operator_delete((void *)CONCAT17(uStack_129,
                                     CONCAT16(uStack_12a,CONCAT51(acStack_12f,cStack_130))));
  }
  if ((local_120 & 1) != 0) {
    operator_delete(local_110);
  }
  uVar4 = FUN_0056626c(&local_128);
  if ((uVar4 & 1) != 0) {
    plVar5 = (long *)param_2[4];
    if (plVar5 == (long *)0x0) {
      local_100 = (byte *)0x0;
    }
    else if (plVar5 == param_2) {
      local_100 = &local_120;
      (**(code **)(*param_2 + 0x18))(param_2,&local_120);
    }
    else {
      local_100 = (byte *)(**(code **)(*plVar5 + 0x10))();
    }
    plVar6 = (long *)param_3[4];
    plVar5 = local_f0;
    local_d0 = (long *)0x0;
    if (plVar6 != (long *)0x0) {
      if (plVar6 == param_3) {
        local_d0 = plVar5;
        (**(code **)(*param_3 + 0x18))(param_3,plVar5);
      }
      else {
        local_d0 = (long *)(**(code **)(*plVar6 + 0x10))();
      }
    }
    plVar7 = (long *)param_4[4];
    plVar6 = local_c0;
    local_a0 = (long *)0x0;
    if (plVar7 != (long *)0x0) {
      if (plVar7 == param_4) {
        local_a0 = plVar6;
        (**(code **)(*param_4 + 0x18))(param_4,plVar6);
      }
      else {
        local_a0 = (long *)(**(code **)(*plVar7 + 0x10))();
      }
    }
    plVar8 = (long *)param_5[4];
    plVar7 = local_90;
    local_70 = (long *)0x0;
    if (plVar8 != (long *)0x0) {
      if (plVar8 == param_5) {
        local_70 = plVar7;
        (**(code **)(*param_5 + 0x18))(param_5,plVar7);
      }
      else {
        local_70 = (long *)(**(code **)(*plVar8 + 0x10))();
      }
    }
    FUN_00ad8390(&DAT_0109fd60,&local_120);
    if (local_70 == plVar7) {
      lVar11 = 0x20;
LAB_00ad80d0:
      (**(code **)(*plVar7 + lVar11))(plVar7);
    }
    else if (local_70 != (long *)0x0) {
      lVar11 = 0x28;
      plVar7 = local_70;
      goto LAB_00ad80d0;
    }
    if (local_a0 == plVar6) {
      lVar11 = 0x20;
LAB_00ad8100:
      (**(code **)(*plVar6 + lVar11))(plVar6);
    }
    else if (local_a0 != (long *)0x0) {
      lVar11 = 0x28;
      plVar6 = local_a0;
      goto LAB_00ad8100;
    }
    if (local_d0 == plVar5) {
      lVar11 = 0x20;
LAB_00ad8130:
      (**(code **)(*plVar5 + lVar11))(plVar5);
    }
    else if (local_d0 != (long *)0x0) {
      lVar11 = 0x28;
      plVar5 = local_d0;
      goto LAB_00ad8130;
    }
    if (local_100 == &local_120) {
      lVar11 = 0x20;
      pbVar9 = &local_120;
LAB_00ad8164:
      (**(code **)(*(long *)pbVar9 + lVar11))();
    }
    else if (local_100 != (byte *)0x0) {
      lVar11 = 0x28;
      pbVar9 = local_100;
      goto LAB_00ad8164;
    }
    __n = strlen(param_1);
    if (0xfffffffffffffff7 < __n) {
      if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
        FUN_00418c24(&local_140);
      }
      goto LAB_00ad838c;
    }
    if (__n < 0x17) {
      __dest = (void *)((ulong)&local_140 | 1);
      local_140 = (byte)((int)__n << 1);
      if (__n != 0) goto LAB_00ad81d4;
    }
    else {
      uVar4 = (__n & 0xfffffffffffffff8) + 8;
      if ((__n | 7) != 0x17) {
        uVar4 = __n | 7;
      }
      uVar4 = uVar4 + 1;
      __dest = operator_new(uVar4);
      local_140 = (byte)uVar4 | 1;
      cStack_138 = (char)__n;
      acStack_137 = SUB85(__n >> 8,0);
      uStack_132 = (undefined2)(__n >> 0x30);
      cStack_130 = (char)__dest;
      acStack_12f = SUB85((ulong)__dest >> 8,0);
      uStack_12a = (undefined1)((ulong)__dest >> 0x30);
      uStack_129 = (undefined1)((ulong)__dest >> 0x38);
      uStack_13f = (undefined7)(uVar4 >> 8);
LAB_00ad81d4:
      memcpy(__dest,param_1,__n);
    }
    *(undefined1 *)((long)__dest + __n) = 0;
    FUN_005669f8(&local_120,uVar2,&local_140);
    if ((local_140 & 1) != 0) {
      operator_delete((void *)CONCAT17(uStack_129,
                                       CONCAT16(uStack_12a,CONCAT51(acStack_12f,cStack_130))));
    }
    FUN_00566284();
    uVar3 = FUN_00566978();
    uVar10 = FUN_00566980(&local_120);
    if (local_128 != 0) {
      FUN_00551e14(uVar2,uVar3,local_128,uVar10);
    }
    FUN_005679e4(&local_120);
  }
  if (*(long *)(lVar1 + 0x28) == local_58) {
    return;
  }
LAB_00ad838c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~
