# 00ad7ebc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad7f84`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad7/00ad7f84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-e1d7556d2ed28c2b0f67286fcd4a2d41)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

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
  "source_sha256": "97bf5f4c6114450b44b65cb4ddf7111c3dc56a7e261cfc68922f7d16cc6a52da",
  "source_text_sha256": "97bf5f4c6114450b44b65cb4ddf7111c3dc56a7e261cfc68922f7d16cc6a52da",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad7ebc",
        "00ad827f"
      ],
      [
        "00ad838c",
        "00ad838f"
      ]
    ],
    "bytes_sha256": "8f41a6c4c4700ec45940303295cd5757a08bb58c92356fcde1bbdfb062a932aa",
    "instruction_count": 242,
    "instruction_bytes": 968,
    "body_bytes": 968,
    "indirect": 12,
    "unresolved": 12
  }
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6792 bytes

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
    _ZdlPv((void *)CONCAT17(uStack_129,CONCAT16(uStack_12a,CONCAT51(acStack_12f,cStack_130))));
  }
  if ((local_120 & 1) != 0) {
    _ZdlPv(local_110);
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
      lVar11 = uVar4 + 1;
      __dest = (void *)_Znwm(lVar11);
      local_140 = (byte)lVar11 | 1;
      cStack_138 = (char)__n;
      acStack_137 = SUB85(__n >> 8,0);
      uStack_132 = (undefined2)(__n >> 0x30);
      cStack_130 = (char)__dest;
      acStack_12f = SUB85((ulong)__dest >> 8,0);
      uStack_12a = (undefined1)((ulong)__dest >> 0x30);
      uStack_129 = (undefined1)((ulong)__dest >> 0x38);
      uStack_13f = (undefined7)((ulong)lVar11 >> 8);
LAB_00ad81d4:
      memcpy(__dest,param_1,__n);
    }
    *(undefined1 *)((long)__dest + __n) = 0;
    FUN_005669f8(&local_120,uVar2,&local_140);
    if ((local_140 & 1) != 0) {
      _ZdlPv((void *)CONCAT17(uStack_129,CONCAT16(uStack_12a,CONCAT51(acStack_12f,cStack_130))));
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

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ad7ebc"></a> `00ad7ebc` | `ff 03 05 d1` | sub sp,sp,#0x140 | `FALL_THROUGH`
<a id="insn-00ad7ec0"></a> `00ad7ec0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00ad7ec4"></a> `00ad7ec4` | `fc 67 10 a9` | stp x28,x25,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00ad7ec8"></a> `00ad7ec8` | `f8 5f 11 a9` | stp x24,x23,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00ad7ecc"></a> `00ad7ecc` | `f6 57 12 a9` | stp x22,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00ad7ed0"></a> `00ad7ed0` | `f4 4f 13 a9` | stp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00ad7ed4"></a> `00ad7ed4` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00ad7ed8"></a> `00ad7ed8` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ad7edc"></a> `00ad7edc` | `f6 03 04 aa` | mov x22,x4 | `FALL_THROUGH`
<a id="insn-00ad7ee0"></a> `00ad7ee0` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00ad7ee4"></a> `00ad7ee4` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00ad7ee8"></a> `00ad7ee8` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00ad7eec"></a> `00ad7eec` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00ad7ef0"></a> `00ad7ef0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ad7ef4"></a> `00ad7ef4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad7ef8"></a> `00ad7ef8` | `27 38 ea 97` | bl 0x00565f94 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7efc"></a> `00ad7efc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ad7f00"></a> `00ad7f00` | `e1 38 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f04"></a> `00ad7f04` | `88 03 80 52` | mov w8,#0x1c | `FALL_THROUGH`
<a id="insn-00ad7f08"></a> `00ad7f08` | `89 be ff 90` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00ad7f0c"></a> `00ad7f0c` | `29 29 00 91` | add x9,x9,#0xa | `FALL_THROUGH`
<a id="insn-00ad7f10"></a> `00ad7f10` | `2a 01 40 f9` | ldr x10,[x9] | `FALL_THROUGH`
<a id="insn-00ad7f14"></a> `00ad7f14` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad7f18"></a> `00ad7f18` | `28 61 40 f8` | ldur x8,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00ad7f1c"></a> `00ad7f1c` | `89 be ff f0` | adrp x9,0x2aa000 | `FALL_THROUGH`
<a id="insn-00ad7f20"></a> `00ad7f20` | `29 7d 1c 91` | add x9,x9,#0x71f | `FALL_THROUGH`
<a id="insn-00ad7f24"></a> `00ad7f24` | `ff bf 00 39` | strb wzr,[sp, #0x2f] | `FALL_THROUGH`
<a id="insn-00ad7f28"></a> `00ad7f28` | `ea 13 02 f8` | stur x10,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00ad7f2c"></a> `00ad7f2c` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00ad7f30"></a> `00ad7f30` | `e8 73 02 f8` | stur x8,[sp, #0x27] | `FALL_THROUGH`
<a id="insn-00ad7f34"></a> `00ad7f34` | `48 05 80 52` | mov w8,#0x2a | `FALL_THROUGH`
<a id="insn-00ad7f38"></a> `00ad7f38` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ad7f3c"></a> `00ad7f3c` | `28 d1 40 f8` | ldur x8,[x9, #0xd] | `FALL_THROUGH`
<a id="insn-00ad7f40"></a> `00ad7f40` | `e0 13 80 3c` | stur q0,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00ad7f44"></a> `00ad7f44` | `e8 e3 00 f8` | stur x8,[sp, #0xe] | `FALL_THROUGH`
<a id="insn-00ad7f48"></a> `00ad7f48` | `ff 5b 00 39` | strb wzr,[sp, #0x16] | `FALL_THROUGH`
<a id="insn-00ad7f4c"></a> `00ad7f4c` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad7f50"></a> `00ad7f50` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00ad7f54"></a> `00ad7f54` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00ad7f58"></a> `00ad7f58` | `3c 39 ea 97` | bl 0x00566448 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f5c"></a> `00ad7f5c` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ad7f60"></a> `00ad7f60` | `e0 0f 00 f9` | str x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad7f64"></a> `00ad7f64` | `68 00 00 36` | tbz w8,#0x0,0x00ad7f70 | `CONDITIONAL_JUMP`
<a id="insn-00ad7f68"></a> `00ad7f68` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad7f6c"></a> `00ad7f6c` | `fd 0b 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f70"></a> `00ad7f70` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad7f74"></a> `00ad7f74` | `68 00 00 36` | tbz w8,#0x0,0x00ad7f80 | `CONDITIONAL_JUMP`
<a id="insn-00ad7f78"></a> `00ad7f78` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad7f7c"></a> `00ad7f7c` | `f9 0b 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f80"></a> `00ad7f80` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00ad7f84"></a> `00ad7f84` | `ba 38 ea 97` | bl 0x0056626c | `UNCONDITIONAL_CALL`
<a id="insn-00ad7f88"></a> `00ad7f88` | `a0 15 00 36` | tbz w0,#0x0,0x00ad823c | `CONDITIONAL_JUMP`
<a id="insn-00ad7f8c"></a> `00ad7f8c` | `a0 12 40 f9` | ldr x0,[x21, #0x20] | `FALL_THROUGH`
<a id="insn-00ad7f90"></a> `00ad7f90` | `00 01 00 b4` | cbz x0,0x00ad7fb0 | `CONDITIONAL_JUMP`
<a id="insn-00ad7f94"></a> `00ad7f94` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00ad7f98"></a> `00ad7f98` | `00 01 00 54` | b.eq 0x00ad7fb8 | `CONDITIONAL_JUMP`
<a id="insn-00ad7f9c"></a> `00ad7f9c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad7fa0"></a> `00ad7fa0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad7fa4"></a> `00ad7fa4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad7fa8"></a> `00ad7fa8` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad7fac"></a> `00ad7fac` | `0a 00 00 14` | b 0x00ad7fd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7fb0"></a> `00ad7fb0` | `ff 23 00 f9` | str xzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad7fb4"></a> `00ad7fb4` | `08 00 00 14` | b 0x00ad7fd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad7fb8"></a> `00ad7fb8` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad7fbc"></a> `00ad7fbc` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00ad7fc0"></a> `00ad7fc0` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad7fc4"></a> `00ad7fc4` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad7fc8"></a> `00ad7fc8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ad7fcc"></a> `00ad7fcc` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00ad7fd0"></a> `00ad7fd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad7fd4"></a> `00ad7fd4` | `00 13 40 f9` | ldr x0,[x24, #0x20] | `FALL_THROUGH`
<a id="insn-00ad7fd8"></a> `00ad7fd8` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad7fdc"></a> `00ad7fdc` | `15 c1 00 91` | add x21,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00ad7fe0"></a> `00ad7fe0` | `c0 00 00 b4` | cbz x0,0x00ad7ff8 | `CONDITIONAL_JUMP`
<a id="insn-00ad7fe4"></a> `00ad7fe4` | `1f 00 18 eb` | cmp x0,x24 | `FALL_THROUGH`
<a id="insn-00ad7fe8"></a> `00ad7fe8` | `c0 00 00 54` | b.eq 0x00ad8000 | `CONDITIONAL_JUMP`
<a id="insn-00ad7fec"></a> `00ad7fec` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad7ff0"></a> `00ad7ff0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad7ff4"></a> `00ad7ff4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad7ff8"></a> `00ad7ff8` | `e0 3b 00 f9` | str x0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ad7ffc"></a> `00ad7ffc` | `07 00 00 14` | b 0x00ad8018 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad8000"></a> `00ad8000` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00ad8004"></a> `00ad8004` | `f5 3b 00 f9` | str x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ad8008"></a> `00ad8008` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00ad800c"></a> `00ad800c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00ad8010"></a> `00ad8010` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ad8014"></a> `00ad8014` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8018"></a> `00ad8018` | `e0 12 40 f9` | ldr x0,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00ad801c"></a> `00ad801c` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad8020"></a> `00ad8020` | `18 81 01 91` | add x24,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00ad8024"></a> `00ad8024` | `c0 00 00 b4` | cbz x0,0x00ad803c | `CONDITIONAL_JUMP`
<a id="insn-00ad8028"></a> `00ad8028` | `1f 00 17 eb` | cmp x0,x23 | `FALL_THROUGH`
<a id="insn-00ad802c"></a> `00ad802c` | `c0 00 00 54` | b.eq 0x00ad8044 | `CONDITIONAL_JUMP`
<a id="insn-00ad8030"></a> `00ad8030` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad8034"></a> `00ad8034` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad8038"></a> `00ad8038` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad803c"></a> `00ad803c` | `e0 53 00 f9` | str x0,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ad8040"></a> `00ad8040` | `07 00 00 14` | b 0x00ad805c | `UNCONDITIONAL_JUMP`
<a id="insn-00ad8044"></a> `00ad8044` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00ad8048"></a> `00ad8048` | `f8 53 00 f9` | str x24,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ad804c"></a> `00ad804c` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00ad8050"></a> `00ad8050` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ad8054"></a> `00ad8054` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00ad8058"></a> `00ad8058` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad805c"></a> `00ad805c` | `c0 12 40 f9` | ldr x0,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00ad8060"></a> `00ad8060` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad8064"></a> `00ad8064` | `17 41 02 91` | add x23,x8,#0x90 | `FALL_THROUGH`
<a id="insn-00ad8068"></a> `00ad8068` | `c0 00 00 b4` | cbz x0,0x00ad8080 | `CONDITIONAL_JUMP`
<a id="insn-00ad806c"></a> `00ad806c` | `1f 00 16 eb` | cmp x0,x22 | `FALL_THROUGH`
<a id="insn-00ad8070"></a> `00ad8070` | `c0 00 00 54` | b.eq 0x00ad8088 | `CONDITIONAL_JUMP`
<a id="insn-00ad8074"></a> `00ad8074` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad8078"></a> `00ad8078` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad807c"></a> `00ad807c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8080"></a> `00ad8080` | `e0 6b 00 f9` | str x0,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00ad8084"></a> `00ad8084` | `07 00 00 14` | b 0x00ad80a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad8088"></a> `00ad8088` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00ad808c"></a> `00ad808c` | `f7 6b 00 f9` | str x23,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00ad8090"></a> `00ad8090` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00ad8094"></a> `00ad8094` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ad8098"></a> `00ad8098` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00ad809c"></a> `00ad809c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad80a0"></a> `00ad80a0` | `20 2e 00 f0` | adrp x0,0x109f000 | `FALL_THROUGH`
<a id="insn-00ad80a4"></a> `00ad80a4` | `00 80 35 91` | add x0,x0,#0xd60 | `FALL_THROUGH`
<a id="insn-00ad80a8"></a> `00ad80a8` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad80ac"></a> `00ad80ac` | `b9 00 00 94` | bl 0x00ad8390 | `UNCONDITIONAL_CALL`
<a id="insn-00ad80b0"></a> `00ad80b0` | `e9 6b 40 f9` | ldr x9,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00ad80b4"></a> `00ad80b4` | `3f 01 17 eb` | cmp x9,x23 | `FALL_THROUGH`
<a id="insn-00ad80b8"></a> `00ad80b8` | `a0 00 00 54` | b.eq 0x00ad80cc | `CONDITIONAL_JUMP`
<a id="insn-00ad80bc"></a> `00ad80bc` | `29 01 00 b4` | cbz x9,0x00ad80e0 | `CONDITIONAL_JUMP`
<a id="insn-00ad80c0"></a> `00ad80c0` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ad80c4"></a> `00ad80c4` | `f7 03 09 aa` | mov x23,x9 | `FALL_THROUGH`
<a id="insn-00ad80c8"></a> `00ad80c8` | `02 00 00 14` | b 0x00ad80d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad80cc"></a> `00ad80cc` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ad80d0"></a> `00ad80d0` | `e9 02 40 f9` | ldr x9,[x23] | `FALL_THROUGH`
<a id="insn-00ad80d4"></a> `00ad80d4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ad80d8"></a> `00ad80d8` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad80dc"></a> `00ad80dc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad80e0"></a> `00ad80e0` | `e9 53 40 f9` | ldr x9,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00ad80e4"></a> `00ad80e4` | `3f 01 18 eb` | cmp x9,x24 | `FALL_THROUGH`
<a id="insn-00ad80e8"></a> `00ad80e8` | `a0 00 00 54` | b.eq 0x00ad80fc | `CONDITIONAL_JUMP`
<a id="insn-00ad80ec"></a> `00ad80ec` | `29 01 00 b4` | cbz x9,0x00ad8110 | `CONDITIONAL_JUMP`
<a id="insn-00ad80f0"></a> `00ad80f0` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ad80f4"></a> `00ad80f4` | `f8 03 09 aa` | mov x24,x9 | `FALL_THROUGH`
<a id="insn-00ad80f8"></a> `00ad80f8` | `02 00 00 14` | b 0x00ad8100 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad80fc"></a> `00ad80fc` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ad8100"></a> `00ad8100` | `09 03 40 f9` | ldr x9,[x24] | `FALL_THROUGH`
<a id="insn-00ad8104"></a> `00ad8104` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00ad8108"></a> `00ad8108` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad810c"></a> `00ad810c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8110"></a> `00ad8110` | `e9 3b 40 f9` | ldr x9,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ad8114"></a> `00ad8114` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00ad8118"></a> `00ad8118` | `a0 00 00 54` | b.eq 0x00ad812c | `CONDITIONAL_JUMP`
<a id="insn-00ad811c"></a> `00ad811c` | `29 01 00 b4` | cbz x9,0x00ad8140 | `CONDITIONAL_JUMP`
<a id="insn-00ad8120"></a> `00ad8120` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ad8124"></a> `00ad8124` | `f5 03 09 aa` | mov x21,x9 | `FALL_THROUGH`
<a id="insn-00ad8128"></a> `00ad8128` | `02 00 00 14` | b 0x00ad8130 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad812c"></a> `00ad812c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ad8130"></a> `00ad8130` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00ad8134"></a> `00ad8134` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ad8138"></a> `00ad8138` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad813c"></a> `00ad813c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8140"></a> `00ad8140` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad8144"></a> `00ad8144` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad8148"></a> `00ad8148` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00ad814c"></a> `00ad814c` | `80 00 00 54` | b.eq 0x00ad815c | `CONDITIONAL_JUMP`
<a id="insn-00ad8150"></a> `00ad8150` | `00 01 00 b4` | cbz x0,0x00ad8170 | `CONDITIONAL_JUMP`
<a id="insn-00ad8154"></a> `00ad8154` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ad8158"></a> `00ad8158` | `03 00 00 14` | b 0x00ad8164 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad815c"></a> `00ad815c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ad8160"></a> `00ad8160` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad8164"></a> `00ad8164` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00ad8168"></a> `00ad8168` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ad816c"></a> `00ad816c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8170"></a> `00ad8170` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ad8174"></a> `00ad8174` | `c7 0b 04 94` | bl 0x00bdb090 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8178"></a> `00ad8178` | `1f 20 00 b1` | cmn x0,#0x8 | `FALL_THROUGH`
<a id="insn-00ad817c"></a> `00ad817c` | `62 07 00 54` | b.cs 0x00ad8268 | `CONDITIONAL_JUMP`
<a id="insn-00ad8180"></a> `00ad8180` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ad8184"></a> `00ad8184` | `1f 5c 00 f1` | cmp x0,#0x17 | `FALL_THROUGH`
<a id="insn-00ad8188"></a> `00ad8188` | `e2 00 00 54` | b.cs 0x00ad81a4 | `CONDITIONAL_JUMP`
<a id="insn-00ad818c"></a> `00ad818c` | `a8 7a 1f 53` | lsl w8,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00ad8190"></a> `00ad8190` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-00ad8194"></a> `00ad8194` | `36 01 40 b2` | orr x22,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00ad8198"></a> `00ad8198` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ad819c"></a> `00ad819c` | `d5 01 00 b5` | cbnz x21,0x00ad81d4 | `CONDITIONAL_JUMP`
<a id="insn-00ad81a0"></a> `00ad81a0` | `11 00 00 14` | b 0x00ad81e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad81a4"></a> `00ad81a4` | `a8 f2 7d 92` | and x8,x21,#-0x8 | `FALL_THROUGH`
<a id="insn-00ad81a8"></a> `00ad81a8` | `a9 0a 40 b2` | orr x9,x21,#0x7 | `FALL_THROUGH`
<a id="insn-00ad81ac"></a> `00ad81ac` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00ad81b0"></a> `00ad81b0` | `3f 5d 00 f1` | cmp x9,#0x17 | `FALL_THROUGH`
<a id="insn-00ad81b4"></a> `00ad81b4` | `08 01 89 9a` | csel x8,x8,x9,eq | `FALL_THROUGH`
<a id="insn-00ad81b8"></a> `00ad81b8` | `17 05 00 91` | add x23,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00ad81bc"></a> `00ad81bc` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00ad81c0"></a> `00ad81c0` | `60 0b 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00ad81c4"></a> `00ad81c4` | `e8 02 40 b2` | orr x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00ad81c8"></a> `00ad81c8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00ad81cc"></a> `00ad81cc` | `f5 83 00 a9` | stp x21,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ad81d0"></a> `00ad81d0` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00ad81d4"></a> `00ad81d4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ad81d8"></a> `00ad81d8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ad81dc"></a> `00ad81dc` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00ad81e0"></a> `00ad81e0` | `b4 0b 04 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad81e4"></a> `00ad81e4` | `df 6a 35 38` | strb wzr,[x22, x21, LSL ] | `FALL_THROUGH`
<a id="insn-00ad81e8"></a> `00ad81e8` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad81ec"></a> `00ad81ec` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00ad81f0"></a> `00ad81f0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00ad81f4"></a> `00ad81f4` | `01 3a ea 97` | bl 0x005669f8 | `UNCONDITIONAL_CALL`
<a id="insn-00ad81f8"></a> `00ad81f8` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ad81fc"></a> `00ad81fc` | `68 00 00 36` | tbz w8,#0x0,0x00ad8208 | `CONDITIONAL_JUMP`
<a id="insn-00ad8200"></a> `00ad8200` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad8204"></a> `00ad8204` | `57 0b 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8208"></a> `00ad8208` | `1f 38 ea 97` | bl 0x00566284 | `UNCONDITIONAL_CALL`
<a id="insn-00ad820c"></a> `00ad820c` | `db 39 ea 97` | bl 0x00566978 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8210"></a> `00ad8210` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ad8214"></a> `00ad8214` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad8218"></a> `00ad8218` | `da 39 ea 97` | bl 0x00566980 | `UNCONDITIONAL_CALL`
<a id="insn-00ad821c"></a> `00ad821c` | `e2 0f 40 f9` | ldr x2,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad8220"></a> `00ad8220` | `a2 00 00 b4` | cbz x2,0x00ad8234 | `CONDITIONAL_JUMP`
<a id="insn-00ad8224"></a> `00ad8224` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00ad8228"></a> `00ad8228` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad822c"></a> `00ad822c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00ad8230"></a> `00ad8230` | `f9 e6 e9 97` | bl 0x00551e14 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8234"></a> `00ad8234` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad8238"></a> `00ad8238` | `eb 3d ea 97` | bl 0x005679e4 | `UNCONDITIONAL_CALL`
<a id="insn-00ad823c"></a> `00ad823c` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8240"></a> `00ad8240` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad8244"></a> `00ad8244` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad8248"></a> `00ad8248` | `21 0a 00 54` | b.ne 0x00ad838c | `CONDITIONAL_JUMP`
<a id="insn-00ad824c"></a> `00ad824c` | `f4 4f 53 a9` | ldp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00ad8250"></a> `00ad8250` | `f6 57 52 a9` | ldp x22,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00ad8254"></a> `00ad8254` | `f8 5f 51 a9` | ldp x24,x23,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00ad8258"></a> `00ad8258` | `fc 67 50 a9` | ldp x28,x25,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00ad825c"></a> `00ad825c` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00ad8260"></a> `00ad8260` | `ff 03 05 91` | add sp,sp,#0x140 | `FALL_THROUGH`
<a id="insn-00ad8264"></a> `00ad8264` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ad8268"></a> `00ad8268` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00ad826c"></a> `00ad826c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad8270"></a> `00ad8270` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad8274"></a> `00ad8274` | `c1 08 00 54` | b.ne 0x00ad838c | `CONDITIONAL_JUMP`
<a id="insn-00ad8278"></a> `00ad8278` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00ad827c"></a> `00ad827c` | `6a 02 e5 97` | bl 0x00418c24 | `CALL_TERMINATOR`
<a id="insn-00ad838c"></a> `00ad838c` | `01 0b 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad7ebc`](#insn-00ad7ebc) 範囲 `[['00ad7ebc', '00ad7f67']]`
  - `CONDITIONAL_JUMP` [`00ad7f64`](#insn-00ad7f64) → [`00ad7f70`](#insn-00ad7f70)
  - `FALL_THROUGH` [`00ad7f64`](#insn-00ad7f64) → [`00ad7f68`](#insn-00ad7f68)
- ブロック [`00ad7f68`](#insn-00ad7f68) 範囲 `[['00ad7f68', '00ad7f6f']]`
  - `FALL_THROUGH` [`00ad7f6c`](#insn-00ad7f6c) → [`00ad7f70`](#insn-00ad7f70)
- ブロック [`00ad7f70`](#insn-00ad7f70) 範囲 `[['00ad7f70', '00ad7f77']]`
  - `CONDITIONAL_JUMP` [`00ad7f74`](#insn-00ad7f74) → [`00ad7f80`](#insn-00ad7f80)
  - `FALL_THROUGH` [`00ad7f74`](#insn-00ad7f74) → [`00ad7f78`](#insn-00ad7f78)
- ブロック [`00ad7f78`](#insn-00ad7f78) 範囲 `[['00ad7f78', '00ad7f7f']]`
  - `FALL_THROUGH` [`00ad7f7c`](#insn-00ad7f7c) → [`00ad7f80`](#insn-00ad7f80)
- ブロック [`00ad7f80`](#insn-00ad7f80) 範囲 `[['00ad7f80', '00ad7f8b']]`
  - `CONDITIONAL_JUMP` [`00ad7f88`](#insn-00ad7f88) → [`00ad823c`](#insn-00ad823c)
  - `FALL_THROUGH` [`00ad7f88`](#insn-00ad7f88) → [`00ad7f8c`](#insn-00ad7f8c)
- ブロック [`00ad7f8c`](#insn-00ad7f8c) 範囲 `[['00ad7f8c', '00ad7f93']]`
  - `CONDITIONAL_JUMP` [`00ad7f90`](#insn-00ad7f90) → [`00ad7fb0`](#insn-00ad7fb0)
  - `FALL_THROUGH` [`00ad7f90`](#insn-00ad7f90) → [`00ad7f94`](#insn-00ad7f94)
- ブロック [`00ad7f94`](#insn-00ad7f94) 範囲 `[['00ad7f94', '00ad7f9b']]`
  - `CONDITIONAL_JUMP` [`00ad7f98`](#insn-00ad7f98) → [`00ad7fb8`](#insn-00ad7fb8)
  - `FALL_THROUGH` [`00ad7f98`](#insn-00ad7f98) → [`00ad7f9c`](#insn-00ad7f9c)
- ブロック [`00ad7f9c`](#insn-00ad7f9c) 範囲 `[['00ad7f9c', '00ad7faf']]`
  - `UNCONDITIONAL_JUMP` [`00ad7fac`](#insn-00ad7fac) → [`00ad7fd4`](#insn-00ad7fd4)
- ブロック [`00ad7fb0`](#insn-00ad7fb0) 範囲 `[['00ad7fb0', '00ad7fb7']]`
  - `UNCONDITIONAL_JUMP` [`00ad7fb4`](#insn-00ad7fb4) → [`00ad7fd4`](#insn-00ad7fd4)
- ブロック [`00ad7fb8`](#insn-00ad7fb8) 範囲 `[['00ad7fb8', '00ad7fd3']]`
  - `FALL_THROUGH` [`00ad7fd0`](#insn-00ad7fd0) → [`00ad7fd4`](#insn-00ad7fd4)
- ブロック [`00ad7fd4`](#insn-00ad7fd4) 範囲 `[['00ad7fd4', '00ad7fe3']]`
  - `CONDITIONAL_JUMP` [`00ad7fe0`](#insn-00ad7fe0) → [`00ad7ff8`](#insn-00ad7ff8)
  - `FALL_THROUGH` [`00ad7fe0`](#insn-00ad7fe0) → [`00ad7fe4`](#insn-00ad7fe4)
- ブロック [`00ad7fe4`](#insn-00ad7fe4) 範囲 `[['00ad7fe4', '00ad7feb']]`
  - `CONDITIONAL_JUMP` [`00ad7fe8`](#insn-00ad7fe8) → [`00ad8000`](#insn-00ad8000)
  - `FALL_THROUGH` [`00ad7fe8`](#insn-00ad7fe8) → [`00ad7fec`](#insn-00ad7fec)
- ブロック [`00ad7fec`](#insn-00ad7fec) 範囲 `[['00ad7fec', '00ad7ff7']]`
  - `FALL_THROUGH` [`00ad7ff4`](#insn-00ad7ff4) → [`00ad7ff8`](#insn-00ad7ff8)
- ブロック [`00ad7ff8`](#insn-00ad7ff8) 範囲 `[['00ad7ff8', '00ad7fff']]`
  - `UNCONDITIONAL_JUMP` [`00ad7ffc`](#insn-00ad7ffc) → [`00ad8018`](#insn-00ad8018)
- ブロック [`00ad8000`](#insn-00ad8000) 範囲 `[['00ad8000', '00ad8017']]`
  - `FALL_THROUGH` [`00ad8014`](#insn-00ad8014) → [`00ad8018`](#insn-00ad8018)
- ブロック [`00ad8018`](#insn-00ad8018) 範囲 `[['00ad8018', '00ad8027']]`
  - `CONDITIONAL_JUMP` [`00ad8024`](#insn-00ad8024) → [`00ad803c`](#insn-00ad803c)
  - `FALL_THROUGH` [`00ad8024`](#insn-00ad8024) → [`00ad8028`](#insn-00ad8028)
- ブロック [`00ad8028`](#insn-00ad8028) 範囲 `[['00ad8028', '00ad802f']]`
  - `CONDITIONAL_JUMP` [`00ad802c`](#insn-00ad802c) → [`00ad8044`](#insn-00ad8044)
  - `FALL_THROUGH` [`00ad802c`](#insn-00ad802c) → [`00ad8030`](#insn-00ad8030)
- ブロック [`00ad8030`](#insn-00ad8030) 範囲 `[['00ad8030', '00ad803b']]`
  - `FALL_THROUGH` [`00ad8038`](#insn-00ad8038) → [`00ad803c`](#insn-00ad803c)
- ブロック [`00ad803c`](#insn-00ad803c) 範囲 `[['00ad803c', '00ad8043']]`
  - `UNCONDITIONAL_JUMP` [`00ad8040`](#insn-00ad8040) → [`00ad805c`](#insn-00ad805c)
- ブロック [`00ad8044`](#insn-00ad8044) 範囲 `[['00ad8044', '00ad805b']]`
  - `FALL_THROUGH` [`00ad8058`](#insn-00ad8058) → [`00ad805c`](#insn-00ad805c)
- ブロック [`00ad805c`](#insn-00ad805c) 範囲 `[['00ad805c', '00ad806b']]`
  - `CONDITIONAL_JUMP` [`00ad8068`](#insn-00ad8068) → [`00ad8080`](#insn-00ad8080)
  - `FALL_THROUGH` [`00ad8068`](#insn-00ad8068) → [`00ad806c`](#insn-00ad806c)
- ブロック [`00ad806c`](#insn-00ad806c) 範囲 `[['00ad806c', '00ad8073']]`
  - `CONDITIONAL_JUMP` [`00ad8070`](#insn-00ad8070) → [`00ad8088`](#insn-00ad8088)
  - `FALL_THROUGH` [`00ad8070`](#insn-00ad8070) → [`00ad8074`](#insn-00ad8074)
- ブロック [`00ad8074`](#insn-00ad8074) 範囲 `[['00ad8074', '00ad807f']]`
  - `FALL_THROUGH` [`00ad807c`](#insn-00ad807c) → [`00ad8080`](#insn-00ad8080)
- ブロック [`00ad8080`](#insn-00ad8080) 範囲 `[['00ad8080', '00ad8087']]`
  - `UNCONDITIONAL_JUMP` [`00ad8084`](#insn-00ad8084) → [`00ad80a0`](#insn-00ad80a0)
- ブロック [`00ad8088`](#insn-00ad8088) 範囲 `[['00ad8088', '00ad809f']]`
  - `FALL_THROUGH` [`00ad809c`](#insn-00ad809c) → [`00ad80a0`](#insn-00ad80a0)
- ブロック [`00ad80a0`](#insn-00ad80a0) 範囲 `[['00ad80a0', '00ad80bb']]`
  - `CONDITIONAL_JUMP` [`00ad80b8`](#insn-00ad80b8) → [`00ad80cc`](#insn-00ad80cc)
  - `FALL_THROUGH` [`00ad80b8`](#insn-00ad80b8) → [`00ad80bc`](#insn-00ad80bc)
- ブロック [`00ad80bc`](#insn-00ad80bc) 範囲 `[['00ad80bc', '00ad80bf']]`
  - `CONDITIONAL_JUMP` [`00ad80bc`](#insn-00ad80bc) → [`00ad80e0`](#insn-00ad80e0)
  - `FALL_THROUGH` [`00ad80bc`](#insn-00ad80bc) → [`00ad80c0`](#insn-00ad80c0)
- ブロック [`00ad80c0`](#insn-00ad80c0) 範囲 `[['00ad80c0', '00ad80cb']]`
  - `UNCONDITIONAL_JUMP` [`00ad80c8`](#insn-00ad80c8) → [`00ad80d0`](#insn-00ad80d0)
- ブロック [`00ad80cc`](#insn-00ad80cc) 範囲 `[['00ad80cc', '00ad80cf']]`
  - `FALL_THROUGH` [`00ad80cc`](#insn-00ad80cc) → [`00ad80d0`](#insn-00ad80d0)
- ブロック [`00ad80d0`](#insn-00ad80d0) 範囲 `[['00ad80d0', '00ad80df']]`
  - `FALL_THROUGH` [`00ad80dc`](#insn-00ad80dc) → [`00ad80e0`](#insn-00ad80e0)
- ブロック [`00ad80e0`](#insn-00ad80e0) 範囲 `[['00ad80e0', '00ad80eb']]`
  - `CONDITIONAL_JUMP` [`00ad80e8`](#insn-00ad80e8) → [`00ad80fc`](#insn-00ad80fc)
  - `FALL_THROUGH` [`00ad80e8`](#insn-00ad80e8) → [`00ad80ec`](#insn-00ad80ec)
- ブロック [`00ad80ec`](#insn-00ad80ec) 範囲 `[['00ad80ec', '00ad80ef']]`
  - `CONDITIONAL_JUMP` [`00ad80ec`](#insn-00ad80ec) → [`00ad8110`](#insn-00ad8110)
  - `FALL_THROUGH` [`00ad80ec`](#insn-00ad80ec) → [`00ad80f0`](#insn-00ad80f0)
- ブロック [`00ad80f0`](#insn-00ad80f0) 範囲 `[['00ad80f0', '00ad80fb']]`
  - `UNCONDITIONAL_JUMP` [`00ad80f8`](#insn-00ad80f8) → [`00ad8100`](#insn-00ad8100)
- ブロック [`00ad80fc`](#insn-00ad80fc) 範囲 `[['00ad80fc', '00ad80ff']]`
  - `FALL_THROUGH` [`00ad80fc`](#insn-00ad80fc) → [`00ad8100`](#insn-00ad8100)
- ブロック [`00ad8100`](#insn-00ad8100) 範囲 `[['00ad8100', '00ad810f']]`
  - `FALL_THROUGH` [`00ad810c`](#insn-00ad810c) → [`00ad8110`](#insn-00ad8110)
- ブロック [`00ad8110`](#insn-00ad8110) 範囲 `[['00ad8110', '00ad811b']]`
  - `CONDITIONAL_JUMP` [`00ad8118`](#insn-00ad8118) → [`00ad812c`](#insn-00ad812c)
  - `FALL_THROUGH` [`00ad8118`](#insn-00ad8118) → [`00ad811c`](#insn-00ad811c)
- ブロック [`00ad811c`](#insn-00ad811c) 範囲 `[['00ad811c', '00ad811f']]`
  - `CONDITIONAL_JUMP` [`00ad811c`](#insn-00ad811c) → [`00ad8140`](#insn-00ad8140)
  - `FALL_THROUGH` [`00ad811c`](#insn-00ad811c) → [`00ad8120`](#insn-00ad8120)
- ブロック [`00ad8120`](#insn-00ad8120) 範囲 `[['00ad8120', '00ad812b']]`
  - `UNCONDITIONAL_JUMP` [`00ad8128`](#insn-00ad8128) → [`00ad8130`](#insn-00ad8130)
- ブロック [`00ad812c`](#insn-00ad812c) 範囲 `[['00ad812c', '00ad812f']]`
  - `FALL_THROUGH` [`00ad812c`](#insn-00ad812c) → [`00ad8130`](#insn-00ad8130)
- ブロック [`00ad8130`](#insn-00ad8130) 範囲 `[['00ad8130', '00ad813f']]`
  - `FALL_THROUGH` [`00ad813c`](#insn-00ad813c) → [`00ad8140`](#insn-00ad8140)
- ブロック [`00ad8140`](#insn-00ad8140) 範囲 `[['00ad8140', '00ad814f']]`
  - `CONDITIONAL_JUMP` [`00ad814c`](#insn-00ad814c) → [`00ad815c`](#insn-00ad815c)
  - `FALL_THROUGH` [`00ad814c`](#insn-00ad814c) → [`00ad8150`](#insn-00ad8150)
- ブロック [`00ad8150`](#insn-00ad8150) 範囲 `[['00ad8150', '00ad8153']]`
  - `CONDITIONAL_JUMP` [`00ad8150`](#insn-00ad8150) → [`00ad8170`](#insn-00ad8170)
  - `FALL_THROUGH` [`00ad8150`](#insn-00ad8150) → [`00ad8154`](#insn-00ad8154)
- ブロック [`00ad8154`](#insn-00ad8154) 範囲 `[['00ad8154', '00ad815b']]`
  - `UNCONDITIONAL_JUMP` [`00ad8158`](#insn-00ad8158) → [`00ad8164`](#insn-00ad8164)
- ブロック [`00ad815c`](#insn-00ad815c) 範囲 `[['00ad815c', '00ad8163']]`
  - `FALL_THROUGH` [`00ad8160`](#insn-00ad8160) → [`00ad8164`](#insn-00ad8164)
- ブロック [`00ad8164`](#insn-00ad8164) 範囲 `[['00ad8164', '00ad816f']]`
  - `FALL_THROUGH` [`00ad816c`](#insn-00ad816c) → [`00ad8170`](#insn-00ad8170)
- ブロック [`00ad8170`](#insn-00ad8170) 範囲 `[['00ad8170', '00ad817f']]`
  - `CONDITIONAL_JUMP` [`00ad817c`](#insn-00ad817c) → [`00ad8268`](#insn-00ad8268)
  - `FALL_THROUGH` [`00ad817c`](#insn-00ad817c) → [`00ad8180`](#insn-00ad8180)
- ブロック [`00ad8180`](#insn-00ad8180) 範囲 `[['00ad8180', '00ad818b']]`
  - `CONDITIONAL_JUMP` [`00ad8188`](#insn-00ad8188) → [`00ad81a4`](#insn-00ad81a4)
  - `FALL_THROUGH` [`00ad8188`](#insn-00ad8188) → [`00ad818c`](#insn-00ad818c)
- ブロック [`00ad818c`](#insn-00ad818c) 範囲 `[['00ad818c', '00ad819f']]`
  - `CONDITIONAL_JUMP` [`00ad819c`](#insn-00ad819c) → [`00ad81d4`](#insn-00ad81d4)
  - `FALL_THROUGH` [`00ad819c`](#insn-00ad819c) → [`00ad81a0`](#insn-00ad81a0)
- ブロック [`00ad81a0`](#insn-00ad81a0) 範囲 `[['00ad81a0', '00ad81a3']]`
  - `UNCONDITIONAL_JUMP` [`00ad81a0`](#insn-00ad81a0) → [`00ad81e4`](#insn-00ad81e4)
- ブロック [`00ad81a4`](#insn-00ad81a4) 範囲 `[['00ad81a4', '00ad81d3']]`
  - `FALL_THROUGH` [`00ad81d0`](#insn-00ad81d0) → [`00ad81d4`](#insn-00ad81d4)
- ブロック [`00ad81d4`](#insn-00ad81d4) 範囲 `[['00ad81d4', '00ad81e3']]`
  - `FALL_THROUGH` [`00ad81e0`](#insn-00ad81e0) → [`00ad81e4`](#insn-00ad81e4)
- ブロック [`00ad81e4`](#insn-00ad81e4) 範囲 `[['00ad81e4', '00ad81ff']]`
  - `CONDITIONAL_JUMP` [`00ad81fc`](#insn-00ad81fc) → [`00ad8208`](#insn-00ad8208)
  - `FALL_THROUGH` [`00ad81fc`](#insn-00ad81fc) → [`00ad8200`](#insn-00ad8200)
- ブロック [`00ad8200`](#insn-00ad8200) 範囲 `[['00ad8200', '00ad8207']]`
  - `FALL_THROUGH` [`00ad8204`](#insn-00ad8204) → [`00ad8208`](#insn-00ad8208)
- ブロック [`00ad8208`](#insn-00ad8208) 範囲 `[['00ad8208', '00ad8223']]`
  - `CONDITIONAL_JUMP` [`00ad8220`](#insn-00ad8220) → [`00ad8234`](#insn-00ad8234)
  - `FALL_THROUGH` [`00ad8220`](#insn-00ad8220) → [`00ad8224`](#insn-00ad8224)
- ブロック [`00ad8224`](#insn-00ad8224) 範囲 `[['00ad8224', '00ad8233']]`
  - `FALL_THROUGH` [`00ad8230`](#insn-00ad8230) → [`00ad8234`](#insn-00ad8234)
- ブロック [`00ad8234`](#insn-00ad8234) 範囲 `[['00ad8234', '00ad823b']]`
  - `FALL_THROUGH` [`00ad8238`](#insn-00ad8238) → [`00ad823c`](#insn-00ad823c)
- ブロック [`00ad823c`](#insn-00ad823c) 範囲 `[['00ad823c', '00ad824b']]`
  - `CONDITIONAL_JUMP` [`00ad8248`](#insn-00ad8248) → [`00ad838c`](#insn-00ad838c)
  - `FALL_THROUGH` [`00ad8248`](#insn-00ad8248) → [`00ad824c`](#insn-00ad824c)
- ブロック [`00ad824c`](#insn-00ad824c) 範囲 `[['00ad824c', '00ad8267']]`
- ブロック [`00ad8268`](#insn-00ad8268) 範囲 `[['00ad8268', '00ad8277']]`
  - `CONDITIONAL_JUMP` [`00ad8274`](#insn-00ad8274) → [`00ad838c`](#insn-00ad838c)
  - `FALL_THROUGH` [`00ad8274`](#insn-00ad8274) → [`00ad8278`](#insn-00ad8278)
- ブロック [`00ad8278`](#insn-00ad8278) 範囲 `[['00ad8278', '00ad827f']]`
- ブロック [`00ad838c`](#insn-00ad838c) 範囲 `[['00ad838c', '00ad838f']]`

## 命令位置別の参照

- [`00ad7ec0`](#insn-00ad7ec0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7ec4`](#insn-00ad7ec4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7ec8`](#insn-00ad7ec8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7ecc`](#insn-00ad7ecc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7ed0`](#insn-00ad7ed0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7ef4`](#insn-00ad7ef4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7ef8`](#insn-00ad7ef8) → [`00565f94`](../00565/00565f94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00565f94` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f00`](#insn-00ad7f00) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f10`](#insn-00ad7f10) → `002a700a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ad7f14`](#insn-00ad7f14) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f18`](#insn-00ad7f18) → `002a7010`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ad7f24`](#insn-00ad7f24) → `Stack[-0x111]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f28`](#insn-00ad7f28) → `Stack[-0x11f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f2c`](#insn-00ad7f2c) → `002aa71f`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ad7f30`](#insn-00ad7f30) → `Stack[-0x119]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f38`](#insn-00ad7f38) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f3c`](#insn-00ad7f3c) → `002aa72c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ad7f40`](#insn-00ad7f40) → `Stack[-0x13f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f44`](#insn-00ad7f44) → `Stack[-0x132]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f48`](#insn-00ad7f48) → `Stack[-0x12a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f58`](#insn-00ad7f58) → [`00566448`](../00566/00566448.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566448` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f5c`](#insn-00ad7f5c) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f60`](#insn-00ad7f60) → `Stack[-0x128]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f64`](#insn-00ad7f64) → [`00ad7f70`](#insn-00ad7f70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f68`](#insn-00ad7f68) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f6c`](#insn-00ad7f6c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f70`](#insn-00ad7f70) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f74`](#insn-00ad7f74) → [`00ad7f80`](#insn-00ad7f80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f78`](#insn-00ad7f78) → `Stack[-0x110]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f7c`](#insn-00ad7f7c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f84`](#insn-00ad7f84) → [`0056626c`](../00566/0056626c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0056626c` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f88`](#insn-00ad7f88) → [`00ad823c`](#insn-00ad823c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f90`](#insn-00ad7f90) → [`00ad7fb0`](#insn-00ad7fb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7f98`](#insn-00ad7f98) → [`00ad7fb8`](#insn-00ad7fb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7fa8`](#insn-00ad7fa8) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7fac`](#insn-00ad7fac) → [`00ad7fd4`](#insn-00ad7fd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7fb0`](#insn-00ad7fb0) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7fb4`](#insn-00ad7fb4) → [`00ad7fd4`](#insn-00ad7fd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7fc4`](#insn-00ad7fc4) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7fe0`](#insn-00ad7fe0) → [`00ad7ff8`](#insn-00ad7ff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7fe8`](#insn-00ad7fe8) → [`00ad8000`](#insn-00ad8000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7ff8`](#insn-00ad7ff8) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad7ffc`](#insn-00ad7ffc) → [`00ad8018`](#insn-00ad8018) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8004`](#insn-00ad8004) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8024`](#insn-00ad8024) → [`00ad803c`](#insn-00ad803c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad802c`](#insn-00ad802c) → [`00ad8044`](#insn-00ad8044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad803c`](#insn-00ad803c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8040`](#insn-00ad8040) → [`00ad805c`](#insn-00ad805c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8048`](#insn-00ad8048) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8068`](#insn-00ad8068) → [`00ad8080`](#insn-00ad8080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8070`](#insn-00ad8070) → [`00ad8088`](#insn-00ad8088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8080`](#insn-00ad8080) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8084`](#insn-00ad8084) → [`00ad80a0`](#insn-00ad80a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad808c`](#insn-00ad808c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad80a4`](#insn-00ad80a4) → `0109fd60`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad80ac`](#insn-00ad80ac) → [`00ad8390`](../00ad8/00ad8390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ad8390` · 推定シンボル `None` · 推定型 `None`
- [`00ad80b0`](#insn-00ad80b0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad80b8`](#insn-00ad80b8) → [`00ad80cc`](#insn-00ad80cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad80bc`](#insn-00ad80bc) → [`00ad80e0`](#insn-00ad80e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad80c8`](#insn-00ad80c8) → [`00ad80d0`](#insn-00ad80d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad80d0`](#insn-00ad80d0) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad80e0`](#insn-00ad80e0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad80e8`](#insn-00ad80e8) → [`00ad80fc`](#insn-00ad80fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad80ec`](#insn-00ad80ec) → [`00ad8110`](#insn-00ad8110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad80f8`](#insn-00ad80f8) → [`00ad8100`](#insn-00ad8100) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8100`](#insn-00ad8100) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8110`](#insn-00ad8110) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8118`](#insn-00ad8118) → [`00ad812c`](#insn-00ad812c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad811c`](#insn-00ad811c) → [`00ad8140`](#insn-00ad8140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8128`](#insn-00ad8128) → [`00ad8130`](#insn-00ad8130) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8130`](#insn-00ad8130) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8140`](#insn-00ad8140) → `Stack[-0x100]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad814c`](#insn-00ad814c) → [`00ad815c`](#insn-00ad815c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8150`](#insn-00ad8150) → [`00ad8170`](#insn-00ad8170) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8158`](#insn-00ad8158) → [`00ad8164`](#insn-00ad8164) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8164`](#insn-00ad8164) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8168`](#insn-00ad8168) → `756f736e6f72693c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8174`](#insn-00ad8174) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`
- [`00ad817c`](#insn-00ad817c) → [`00ad8268`](#insn-00ad8268) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8188`](#insn-00ad8188) → [`00ad81a4`](#insn-00ad81a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8198`](#insn-00ad8198) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad819c`](#insn-00ad819c) → [`00ad81d4`](#insn-00ad81d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad81a0`](#insn-00ad81a0) → [`00ad81e4`](#insn-00ad81e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad81c0`](#insn-00ad81c0) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00ad81cc`](#insn-00ad81cc) → `Stack[-0x138]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad81d0`](#insn-00ad81d0) → `Stack[-0x140]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad81e0`](#insn-00ad81e0) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00ad81f4`](#insn-00ad81f4) → [`005669f8`](../00566/005669f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005669f8` · 推定シンボル `None` · 推定型 `None`
- [`00ad81f8`](#insn-00ad81f8) → `Stack[-0x140]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad81fc`](#insn-00ad81fc) → [`00ad8208`](#insn-00ad8208) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8200`](#insn-00ad8200) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8204`](#insn-00ad8204) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ad8208`](#insn-00ad8208) → [`00566284`](../00566/00566284.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566284` · 推定シンボル `None` · 推定型 `None`
- [`00ad820c`](#insn-00ad820c) → [`00566978`](../00566/00566978.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566978` · 推定シンボル `None` · 推定型 `None`
- [`00ad8218`](#insn-00ad8218) → [`00566980`](../00566/00566980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566980` · 推定シンボル `None` · 推定型 `None`
- [`00ad821c`](#insn-00ad821c) → `Stack[-0x128]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8220`](#insn-00ad8220) → [`00ad8234`](#insn-00ad8234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8230`](#insn-00ad8230) → [`00551e14`](../00551/00551e14.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00551e14` · 推定シンボル `None` · 推定型 `None`
- [`00ad8238`](#insn-00ad8238) → [`005679e4`](../00567/005679e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005679e4` · 推定シンボル `None` · 推定型 `None`
- [`00ad8240`](#insn-00ad8240) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8248`](#insn-00ad8248) → [`00ad838c`](#insn-00ad838c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad824c`](#insn-00ad824c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8250`](#insn-00ad8250) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8254`](#insn-00ad8254) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8258`](#insn-00ad8258) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad825c`](#insn-00ad825c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad826c`](#insn-00ad826c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8274`](#insn-00ad8274) → [`00ad838c`](#insn-00ad838c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad827c`](#insn-00ad827c) → [`00418c24`](../00418/00418c24.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00418c24` · 推定シンボル `None` · 推定型 `None`
- [`00ad838c`](#insn-00ad838c) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad7ec0`](#insn-00ad7ec0)

~~~json
{
  "source": "00ad7ec0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7ec4`](#insn-00ad7ec4)

~~~json
{
  "source": "00ad7ec4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7ec8`](#insn-00ad7ec8)

~~~json
{
  "source": "00ad7ec8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7ecc`](#insn-00ad7ecc)

~~~json
{
  "source": "00ad7ecc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7ed0`](#insn-00ad7ed0)

~~~json
{
  "source": "00ad7ed0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7ef4`](#insn-00ad7ef4)

~~~json
{
  "source": "00ad7ef4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7ef8`](#insn-00ad7ef8)

~~~json
{
  "source": "00ad7ef8",
  "target": "00565f94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f00`](#insn-00ad7f00)

~~~json
{
  "source": "00ad7f00",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f10`](#insn-00ad7f10)

~~~json
{
  "source": "00ad7f10",
  "target": "002a700a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a700a",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "69726f6e736f7572636553686f7700",
  "capture_start": "002a700a",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7f14`](#insn-00ad7f14)

~~~json
{
  "source": "00ad7f14",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f18`](#insn-00ad7f18)

~~~json
{
  "source": "00ad7f18",
  "target": "002a7010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a700a",
  "offset": 6,
  "size": 15,
  "datatype": "string",
  "bytes": "69726f6e736f7572636553686f7700",
  "capture_start": "002a700a",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7f24`](#insn-00ad7f24)

~~~json
{
  "source": "00ad7f24",
  "target": "Stack[-0x111]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f28`](#insn-00ad7f28)

~~~json
{
  "source": "00ad7f28",
  "target": "Stack[-0x11f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f2c`](#insn-00ad7f2c)

~~~json
{
  "source": "00ad7f2c",
  "target": "002aa71f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa71f",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b295600",
  "capture_start": "002aa71f",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7f30`](#insn-00ad7f30)

~~~json
{
  "source": "00ad7f30",
  "target": "Stack[-0x119]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f38`](#insn-00ad7f38)

~~~json
{
  "source": "00ad7f38",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f3c`](#insn-00ad7f3c)

~~~json
{
  "source": "00ad7f3c",
  "target": "002aa72c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa71f",
  "offset": 13,
  "size": 22,
  "datatype": "string",
  "bytes": "284c6a6176612f6c616e672f537472696e673b295600",
  "capture_start": "002aa71f",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ad7f40`](#insn-00ad7f40)

~~~json
{
  "source": "00ad7f40",
  "target": "Stack[-0x13f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f44`](#insn-00ad7f44)

~~~json
{
  "source": "00ad7f44",
  "target": "Stack[-0x132]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f48`](#insn-00ad7f48)

~~~json
{
  "source": "00ad7f48",
  "target": "Stack[-0x12a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f58`](#insn-00ad7f58)

~~~json
{
  "source": "00ad7f58",
  "target": "00566448",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f5c`](#insn-00ad7f5c)

~~~json
{
  "source": "00ad7f5c",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f60`](#insn-00ad7f60)

~~~json
{
  "source": "00ad7f60",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f64`](#insn-00ad7f64)

~~~json
{
  "source": "00ad7f64",
  "target": "00ad7f70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f68`](#insn-00ad7f68)

~~~json
{
  "source": "00ad7f68",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f6c`](#insn-00ad7f6c)

~~~json
{
  "source": "00ad7f6c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f70`](#insn-00ad7f70)

~~~json
{
  "source": "00ad7f70",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f74`](#insn-00ad7f74)

~~~json
{
  "source": "00ad7f74",
  "target": "00ad7f80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f78`](#insn-00ad7f78)

~~~json
{
  "source": "00ad7f78",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f7c`](#insn-00ad7f7c)

~~~json
{
  "source": "00ad7f7c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f84`](#insn-00ad7f84)

~~~json
{
  "source": "00ad7f84",
  "target": "0056626c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad7f88`](#insn-00ad7f88)

~~~json
{
  "source": "00ad7f88",
  "target": "00ad823c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f90`](#insn-00ad7f90)

~~~json
{
  "source": "00ad7f90",
  "target": "00ad7fb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7f98`](#insn-00ad7f98)

~~~json
{
  "source": "00ad7f98",
  "target": "00ad7fb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7fa8`](#insn-00ad7fa8)

~~~json
{
  "source": "00ad7fa8",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7fac`](#insn-00ad7fac)

~~~json
{
  "source": "00ad7fac",
  "target": "00ad7fd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7fb0`](#insn-00ad7fb0)

~~~json
{
  "source": "00ad7fb0",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7fb4`](#insn-00ad7fb4)

~~~json
{
  "source": "00ad7fb4",
  "target": "00ad7fd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7fc4`](#insn-00ad7fc4)

~~~json
{
  "source": "00ad7fc4",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7fe0`](#insn-00ad7fe0)

~~~json
{
  "source": "00ad7fe0",
  "target": "00ad7ff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7fe8`](#insn-00ad7fe8)

~~~json
{
  "source": "00ad7fe8",
  "target": "00ad8000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7ff8`](#insn-00ad7ff8)

~~~json
{
  "source": "00ad7ff8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad7ffc`](#insn-00ad7ffc)

~~~json
{
  "source": "00ad7ffc",
  "target": "00ad8018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8004`](#insn-00ad8004)

~~~json
{
  "source": "00ad8004",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8024`](#insn-00ad8024)

~~~json
{
  "source": "00ad8024",
  "target": "00ad803c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad802c`](#insn-00ad802c)

~~~json
{
  "source": "00ad802c",
  "target": "00ad8044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad803c`](#insn-00ad803c)

~~~json
{
  "source": "00ad803c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8040`](#insn-00ad8040)

~~~json
{
  "source": "00ad8040",
  "target": "00ad805c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8048`](#insn-00ad8048)

~~~json
{
  "source": "00ad8048",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8068`](#insn-00ad8068)

~~~json
{
  "source": "00ad8068",
  "target": "00ad8080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8070`](#insn-00ad8070)

~~~json
{
  "source": "00ad8070",
  "target": "00ad8088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8080`](#insn-00ad8080)

~~~json
{
  "source": "00ad8080",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8084`](#insn-00ad8084)

~~~json
{
  "source": "00ad8084",
  "target": "00ad80a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad808c`](#insn-00ad808c)

~~~json
{
  "source": "00ad808c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad80a4`](#insn-00ad80a4)

~~~json
{
  "source": "00ad80a4",
  "target": "0109fd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad80ac`](#insn-00ad80ac)

~~~json
{
  "source": "00ad80ac",
  "target": "00ad8390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad80b0`](#insn-00ad80b0)

~~~json
{
  "source": "00ad80b0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad80b8`](#insn-00ad80b8)

~~~json
{
  "source": "00ad80b8",
  "target": "00ad80cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad80bc`](#insn-00ad80bc)

~~~json
{
  "source": "00ad80bc",
  "target": "00ad80e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad80c8`](#insn-00ad80c8)

~~~json
{
  "source": "00ad80c8",
  "target": "00ad80d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad80d0`](#insn-00ad80d0)

~~~json
{
  "source": "00ad80d0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad80e0`](#insn-00ad80e0)

~~~json
{
  "source": "00ad80e0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad80e8`](#insn-00ad80e8)

~~~json
{
  "source": "00ad80e8",
  "target": "00ad80fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad80ec`](#insn-00ad80ec)

~~~json
{
  "source": "00ad80ec",
  "target": "00ad8110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad80f8`](#insn-00ad80f8)

~~~json
{
  "source": "00ad80f8",
  "target": "00ad8100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8100`](#insn-00ad8100)

~~~json
{
  "source": "00ad8100",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8110`](#insn-00ad8110)

~~~json
{
  "source": "00ad8110",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8118`](#insn-00ad8118)

~~~json
{
  "source": "00ad8118",
  "target": "00ad812c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad811c`](#insn-00ad811c)

~~~json
{
  "source": "00ad811c",
  "target": "00ad8140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8128`](#insn-00ad8128)

~~~json
{
  "source": "00ad8128",
  "target": "00ad8130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8130`](#insn-00ad8130)

~~~json
{
  "source": "00ad8130",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8140`](#insn-00ad8140)

~~~json
{
  "source": "00ad8140",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad814c`](#insn-00ad814c)

~~~json
{
  "source": "00ad814c",
  "target": "00ad815c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8150`](#insn-00ad8150)

~~~json
{
  "source": "00ad8150",
  "target": "00ad8170",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8158`](#insn-00ad8158)

~~~json
{
  "source": "00ad8158",
  "target": "00ad8164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8164`](#insn-00ad8164)

~~~json
{
  "source": "00ad8164",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8168`](#insn-00ad8168)

~~~json
{
  "source": "00ad8168",
  "target": "756f736e6f72693c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8174`](#insn-00ad8174)

~~~json
{
  "source": "00ad8174",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad817c`](#insn-00ad817c)

~~~json
{
  "source": "00ad817c",
  "target": "00ad8268",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8188`](#insn-00ad8188)

~~~json
{
  "source": "00ad8188",
  "target": "00ad81a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8198`](#insn-00ad8198)

~~~json
{
  "source": "00ad8198",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad819c`](#insn-00ad819c)

~~~json
{
  "source": "00ad819c",
  "target": "00ad81d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad81a0`](#insn-00ad81a0)

~~~json
{
  "source": "00ad81a0",
  "target": "00ad81e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad81c0`](#insn-00ad81c0)

~~~json
{
  "source": "00ad81c0",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad81cc`](#insn-00ad81cc)

~~~json
{
  "source": "00ad81cc",
  "target": "Stack[-0x138]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad81d0`](#insn-00ad81d0)

~~~json
{
  "source": "00ad81d0",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad81e0`](#insn-00ad81e0)

~~~json
{
  "source": "00ad81e0",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad81f4`](#insn-00ad81f4)

~~~json
{
  "source": "00ad81f4",
  "target": "005669f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad81f8`](#insn-00ad81f8)

~~~json
{
  "source": "00ad81f8",
  "target": "Stack[-0x140]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad81fc`](#insn-00ad81fc)

~~~json
{
  "source": "00ad81fc",
  "target": "00ad8208",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8200`](#insn-00ad8200)

~~~json
{
  "source": "00ad8200",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8204`](#insn-00ad8204)

~~~json
{
  "source": "00ad8204",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8208`](#insn-00ad8208)

~~~json
{
  "source": "00ad8208",
  "target": "00566284",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad820c`](#insn-00ad820c)

~~~json
{
  "source": "00ad820c",
  "target": "00566978",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8218`](#insn-00ad8218)

~~~json
{
  "source": "00ad8218",
  "target": "00566980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad821c`](#insn-00ad821c)

~~~json
{
  "source": "00ad821c",
  "target": "Stack[-0x128]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8220`](#insn-00ad8220)

~~~json
{
  "source": "00ad8220",
  "target": "00ad8234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8230`](#insn-00ad8230)

~~~json
{
  "source": "00ad8230",
  "target": "00551e14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8238`](#insn-00ad8238)

~~~json
{
  "source": "00ad8238",
  "target": "005679e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8240`](#insn-00ad8240)

~~~json
{
  "source": "00ad8240",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8248`](#insn-00ad8248)

~~~json
{
  "source": "00ad8248",
  "target": "00ad838c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad824c`](#insn-00ad824c)

~~~json
{
  "source": "00ad824c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8250`](#insn-00ad8250)

~~~json
{
  "source": "00ad8250",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8254`](#insn-00ad8254)

~~~json
{
  "source": "00ad8254",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8258`](#insn-00ad8258)

~~~json
{
  "source": "00ad8258",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad825c`](#insn-00ad825c)

~~~json
{
  "source": "00ad825c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad826c`](#insn-00ad826c)

~~~json
{
  "source": "00ad826c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8274`](#insn-00ad8274)

~~~json
{
  "source": "00ad8274",
  "target": "00ad838c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad827c`](#insn-00ad827c)

~~~json
{
  "source": "00ad827c",
  "target": "00418c24",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad838c`](#insn-00ad838c)

~~~json
{
  "source": "00ad838c",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
