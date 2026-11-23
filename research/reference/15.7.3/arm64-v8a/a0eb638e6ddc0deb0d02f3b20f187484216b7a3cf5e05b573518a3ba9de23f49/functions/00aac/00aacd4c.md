# 00aacd4c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aacc84`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aac/00aacc84.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0056.md#compare-146ad11ddafe24e0c8abaa35abae17a6)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aacd90`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aac/00aacd90.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-28eb40b501444b2c8e47a37632630537)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aacd4c",
  "name": "FUN_00aacd4c",
  "size": 712,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fb07569cbfc2a5e64dddcd2c4f9b4fb3af0e930eb2d36e0eceea280e729723db",
  "source_text_sha256": "fb07569cbfc2a5e64dddcd2c4f9b4fb3af0e930eb2d36e0eceea280e729723db",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aacd4c",
        "00aad00f"
      ],
      [
        "00aad140",
        "00aad143"
      ]
    ],
    "bytes_sha256": "8bb8bb17a0f5e57dfeb8e00edf6158b3c03f2048a5a2670bb9218ad26c1ec023",
    "instruction_count": 178,
    "instruction_bytes": 712,
    "body_bytes": 712,
    "indirect": 2,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004253b4](../00425/004253b4.md)
- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [00469f7c](../00469/00469f7c.md)
- [0081f580](../0081f/0081f580.md)
- [00883d34](../00883/00883d34.md)
- [008847e4](../00884/008847e4.md)
- [00885f80](../00885/00885f80.md)
- [008865b0](../00886/008865b0.md)
- [00887e18](../00887/00887e18.md)
- [00aad1d0](../00aad/00aad1d0.md)
- [00aad1d4](../00aad/00aad1d4.md)
- [00aad2ec](../00aad/00aad2ec.md)
- [00aad2f0](../00aad/00aad2f0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

## 関連文字列（未確認候補）

~~~text
"backstage_reset3"
"backstage_reset4"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4607 bytes

~~~c

void FUN_00aacd4c(long param_1,undefined8 *param_2,int *param_3,int *param_4)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  long lVar4;
  undefined ***pppuVar5;
  void *__ptr;
  undefined8 uVar6;
  long lVar7;
  byte local_c8;
  char local_c7 [8];
  undefined7 uStack_bf;
  char cStack_b8;
  undefined1 uStack_b7;
  undefined6 uStack_b6;
  byte local_b0;
  char local_af [8];
  undefined7 uStack_a7;
  char cStack_a0;
  undefined1 uStack_9f;
  undefined6 uStack_9e;
  byte local_98 [16];
  void *local_88;
  undefined **local_80;
  long lStack_78;
  undefined8 local_70;
  undefined8 uStack_68;
  undefined ***local_60;
  long local_48;
  
  lVar2 = tpidr_el0;
  local_48 = *(long *)(lVar2 + 0x28);
  iVar1 = *param_4;
  if (*param_3 == 5) {
    lVar7 = *(long *)(param_1 + 8);
    lVar4 = FUN_0081f580();
    uVar3 = FUN_008847e4(lVar4 + 0x2e48,0x329);
    FUN_00883d34(uVar3,0);
    lVar4 = FUN_0081f580();
    uVar3 = FUN_008847e4(lVar4 + 0x2e48,0x32a);
    FUN_00883d34(uVar3,0);
    if (iVar1 == 1) {
      lVar4 = FUN_0081f580();
      uStack_9f = 0;
      local_b0 = 0x20;
      uStack_a7 = (undefined7)s_backstage_reset4_0029fdf5._8_8_;
      cStack_a0 = SUB81(s_backstage_reset4_0029fdf5._8_8_,7);
      local_af[0] = s_backstage_reset4_0029fdf5[0];
      local_af[1] = s_backstage_reset4_0029fdf5[1];
      local_af[2] = s_backstage_reset4_0029fdf5[2];
      local_af[3] = s_backstage_reset4_0029fdf5[3];
      local_af[4] = s_backstage_reset4_0029fdf5[4];
      local_af[5] = s_backstage_reset4_0029fdf5[5];
      local_af[6] = s_backstage_reset4_0029fdf5[6];
      local_af[7] = s_backstage_reset4_0029fdf5[7];
      FUN_00469f7c(local_98,&local_b0);
      uStack_68 = *(undefined8 *)(param_1 + 0x18);
      local_70 = *(undefined8 *)(param_1 + 0x10);
      local_80 = &PTR_FUN_00c0f378;
      local_60 = &local_80;
      lStack_78 = lVar7;
      uVar3 = FUN_00887e18(lVar4 + 0x2e18,local_98,0,0,0x24,&local_80);
      FUN_008865b0(uVar3,1);
      if (local_60 == &local_80) {
        lVar4 = 0x20;
        pppuVar5 = &local_80;
LAB_00aacf64:
        (**(code **)((long)*pppuVar5 + lVar4))();
      }
      else if (local_60 != (undefined ***)0x0) {
        lVar4 = 0x28;
        pppuVar5 = local_60;
        goto LAB_00aacf64;
      }
      if ((local_98[0] & 1) != 0) {
        _ZdlPv(local_88);
      }
      if ((local_b0 & 1) == 0) goto LAB_00aacfe8;
      __ptr = (void *)CONCAT62(uStack_9e,CONCAT11(uStack_9f,cStack_a0));
    }
    else {
      if (iVar1 != 0) goto LAB_00aacfe8;
      lVar4 = FUN_0081f580();
      uStack_b7 = 0;
      local_c8 = 0x20;
      uStack_bf = (undefined7)s_backstage_reset3_00294099._8_8_;
      cStack_b8 = SUB81(s_backstage_reset3_00294099._8_8_,7);
      local_c7[0] = s_backstage_reset3_00294099[0];
      local_c7[1] = s_backstage_reset3_00294099[1];
      local_c7[2] = s_backstage_reset3_00294099[2];
      local_c7[3] = s_backstage_reset3_00294099[3];
      local_c7[4] = s_backstage_reset3_00294099[4];
      local_c7[5] = s_backstage_reset3_00294099[5];
      local_c7[6] = s_backstage_reset3_00294099[6];
      local_c7[7] = s_backstage_reset3_00294099[7];
      FUN_00469f7c(&local_b0,&local_c8);
      FUN_004253b4(local_98,&local_b0,0,*(int *)(lVar7 + 0x48) + 1);
      uStack_68 = *(undefined8 *)(param_1 + 0x18);
      local_70 = *(undefined8 *)(param_1 + 0x10);
      local_80 = &PTR_FUN_00c0f2f8;
      local_60 = &local_80;
      lStack_78 = lVar7;
      uVar3 = FUN_00887e18(lVar4 + 0x2e18,local_98,0,0,0x24,&local_80);
      FUN_008865b0(uVar3,1);
      if (local_60 == &local_80) {
        lVar4 = 0x20;
        pppuVar5 = &local_80;
LAB_00aacf98:
        (**(code **)((long)*pppuVar5 + lVar4))();
      }
      else if (local_60 != (undefined ***)0x0) {
        lVar4 = 0x28;
        pppuVar5 = local_60;
        goto LAB_00aacf98;
      }
      if ((local_98[0] & 1) != 0) {
        _ZdlPv(local_88);
      }
      if ((local_b0 & 1) != 0) {
        _ZdlPv((void *)CONCAT62(uStack_9e,CONCAT11(uStack_9f,cStack_a0)));
      }
      if ((local_c8 & 1) == 0) goto LAB_00aacfe8;
      __ptr = (void *)CONCAT62(uStack_b6,CONCAT11(uStack_b7,cStack_b8));
    }
    _ZdlPv(__ptr);
  }
  else if (((*param_3 == 2) && (iVar1 + 2U < 4)) && (iVar1 + 2U != 1)) {
    uVar6 = *param_2;
    uVar3 = FUN_00457e1c();
    FUN_00459efc(uVar3,0xb,0);
    if (*(long *)(lVar2 + 0x28) == local_48) {
      FUN_00885f80(uVar6);
      return;
    }
    goto LAB_00aad140;
  }
LAB_00aacfe8:
  if (*(long *)(lVar2 + 0x28) == local_48) {
    return;
  }
LAB_00aad140:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aacd4c"></a> `00aacd4c` | `ff 43 03 d1` | sub sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00aacd50"></a> `00aacd50` | `fd 7b 09 a9` | stp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aacd54"></a> `00aacd54` | `f7 53 00 f9` | str x23,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aacd58"></a> `00aacd58` | `f6 57 0b a9` | stp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aacd5c"></a> `00aacd5c` | `f4 4f 0c a9` | stp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aacd60"></a> `00aacd60` | `fd 43 02 91` | add x29,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00aacd64"></a> `00aacd64` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aacd68"></a> `00aacd68` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aacd6c"></a> `00aacd6c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aacd70"></a> `00aacd70` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00aacd74"></a> `00aacd74` | `73 00 40 b9` | ldr w19,[x3] | `FALL_THROUGH`
<a id="insn-00aacd78"></a> `00aacd78` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00aacd7c"></a> `00aacd7c` | `00 03 00 54` | b.eq 0x00aacddc | `CONDITIONAL_JUMP`
<a id="insn-00aacd80"></a> `00aacd80` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aacd84"></a> `00aacd84` | `21 13 00 54` | b.ne 0x00aacfe8 | `CONDITIONAL_JUMP`
<a id="insn-00aacd88"></a> `00aacd88` | `68 0a 00 11` | add w8,w19,#0x2 | `FALL_THROUGH`
<a id="insn-00aacd8c"></a> `00aacd8c` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00aacd90"></a> `00aacd90` | `c8 12 00 54` | b.hi 0x00aacfe8 | `CONDITIONAL_JUMP`
<a id="insn-00aacd94"></a> `00aacd94` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aacd98"></a> `00aacd98` | `80 12 00 54` | b.eq 0x00aacfe8 | `CONDITIONAL_JUMP`
<a id="insn-00aacd9c"></a> `00aacd9c` | `33 00 40 f9` | ldr x19,[x1] | `FALL_THROUGH`
<a id="insn-00aacda0"></a> `00aacda0` | `1f ac e6 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-00aacda4"></a> `00aacda4` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00aacda8"></a> `00aacda8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00aacdac"></a> `00aacdac` | `54 b4 e6 97` | bl 0x00459efc | `UNCONDITIONAL_CALL`
<a id="insn-00aacdb0"></a> `00aacdb0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aacdb4"></a> `00aacdb4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aacdb8"></a> `00aacdb8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aacdbc"></a> `00aacdbc` | `21 1c 00 54` | b.ne 0x00aad140 | `CONDITIONAL_JUMP`
<a id="insn-00aacdc0"></a> `00aacdc0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aacdc4"></a> `00aacdc4` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aacdc8"></a> `00aacdc8` | `f7 53 40 f9` | ldr x23,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aacdcc"></a> `00aacdcc` | `f6 57 4b a9` | ldp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aacdd0"></a> `00aacdd0` | `fd 7b 49 a9` | ldp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aacdd4"></a> `00aacdd4` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00aacdd8"></a> `00aacdd8` | `6a 64 f7 17` | b 0x00885f80 | `CALL_TERMINATOR`
<a id="insn-00aacddc"></a> `00aacddc` | `15 04 40 f9` | ldr x21,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00aacde0"></a> `00aacde0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aacde4"></a> `00aacde4` | `e7 c9 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aacde8"></a> `00aacde8` | `17 c9 85 52` | mov w23,#0x2e48 | `FALL_THROUGH`
<a id="insn-00aacdec"></a> `00aacdec` | `21 65 80 52` | mov w1,#0x329 | `FALL_THROUGH`
<a id="insn-00aacdf0"></a> `00aacdf0` | `00 00 17 8b` | add x0,x0,x23 | `FALL_THROUGH`
<a id="insn-00aacdf4"></a> `00aacdf4` | `7c 5e f7 97` | bl 0x008847e4 | `UNCONDITIONAL_CALL`
<a id="insn-00aacdf8"></a> `00aacdf8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aacdfc"></a> `00aacdfc` | `ce 5b f7 97` | bl 0x00883d34 | `UNCONDITIONAL_CALL`
<a id="insn-00aace00"></a> `00aace00` | `e0 c9 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aace04"></a> `00aace04` | `00 00 17 8b` | add x0,x0,x23 | `FALL_THROUGH`
<a id="insn-00aace08"></a> `00aace08` | `41 65 80 52` | mov w1,#0x32a | `FALL_THROUGH`
<a id="insn-00aace0c"></a> `00aace0c` | `76 5e f7 97` | bl 0x008847e4 | `UNCONDITIONAL_CALL`
<a id="insn-00aace10"></a> `00aace10` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aace14"></a> `00aace14` | `c8 5b f7 97` | bl 0x00883d34 | `UNCONDITIONAL_CALL`
<a id="insn-00aace18"></a> `00aace18` | `7f 06 00 71` | cmp w19,#0x1 | `FALL_THROUGH`
<a id="insn-00aace1c"></a> `00aace1c` | `80 05 00 54` | b.eq 0x00aacecc | `CONDITIONAL_JUMP`
<a id="insn-00aace20"></a> `00aace20` | `53 0e 00 35` | cbnz w19,0x00aacfe8 | `CONDITIONAL_JUMP`
<a id="insn-00aace24"></a> `00aace24` | `d7 c9 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aace28"></a> `00aace28` | `49 bf ff 90` | adrp x9,0x294000 | `FALL_THROUGH`
<a id="insn-00aace2c"></a> `00aace2c` | `29 65 02 91` | add x9,x9,#0x99 | `FALL_THROUGH`
<a id="insn-00aace30"></a> `00aace30` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aace34"></a> `00aace34` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aace38"></a> `00aace38` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aace3c"></a> `00aace3c` | `ff 67 00 39` | strb wzr,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00aace40"></a> `00aace40` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aace44"></a> `00aace44` | `e0 93 80 3c` | stur q0,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-00aace48"></a> `00aace48` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aace4c"></a> `00aace4c` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00aace50"></a> `00aace50` | `4b f4 e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00aace54"></a> `00aace54` | `a9 4a 40 b9` | ldr w9,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00aace58"></a> `00aace58` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00aace5c"></a> `00aace5c` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aace60"></a> `00aace60` | `22 05 00 11` | add w2,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aace64"></a> `00aace64` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00aace68"></a> `00aace68` | `53 e1 e5 97` | bl 0x004253b4 | `UNCONDITIONAL_CALL`
<a id="insn-00aace6c"></a> `00aace6c` | `08 0b 00 f0` | adrp x8,0xc0f000 | `FALL_THROUGH`
<a id="insn-00aace70"></a> `00aace70` | `08 e1 0b 91` | add x8,x8,#0x2f8 | `FALL_THROUGH`
<a id="insn-00aace74"></a> `00aace74` | `c0 06 c0 3d` | ldr q0,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00aace78"></a> `00aace78` | `a8 57 3c a9` | stp x8,x21,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00aace7c"></a> `00aace7c` | `b5 03 01 d1` | sub x21,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aace80"></a> `00aace80` | `08 c3 85 52` | mov w8,#0x2e18 | `FALL_THROUGH`
<a id="insn-00aace84"></a> `00aace84` | `a0 03 9d 3c` | stur q0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00aace88"></a> `00aace88` | `b5 03 1e f8` | stur x21,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aace8c"></a> `00aace8c` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00aace90"></a> `00aace90` | `e1 e3 00 91` | add x1,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00aace94"></a> `00aace94` | `a5 03 01 d1` | sub x5,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aace98"></a> `00aace98` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aace9c"></a> `00aace9c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aacea0"></a> `00aacea0` | `84 04 80 52` | mov w4,#0x24 | `FALL_THROUGH`
<a id="insn-00aacea4"></a> `00aacea4` | `dd 6b f7 97` | bl 0x00887e18 | `UNCONDITIONAL_CALL`
<a id="insn-00aacea8"></a> `00aacea8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aaceac"></a> `00aaceac` | `c1 65 f7 97` | bl 0x008865b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaceb0"></a> `00aaceb0` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aaceb4"></a> `00aaceb4` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aaceb8"></a> `00aaceb8` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00aacebc"></a> `00aacebc` | `a0 06 00 54` | b.eq 0x00aacf90 | `CONDITIONAL_JUMP`
<a id="insn-00aacec0"></a> `00aacec0` | `20 07 00 b4` | cbz x0,0x00aacfa4 | `CONDITIONAL_JUMP`
<a id="insn-00aacec4"></a> `00aacec4` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aacec8"></a> `00aacec8` | `34 00 00 14` | b 0x00aacf98 | `UNCONDITIONAL_JUMP`
<a id="insn-00aacecc"></a> `00aacecc` | `ad c9 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aaced0"></a> `00aaced0` | `89 bf ff f0` | adrp x9,0x29f000 | `FALL_THROUGH`
<a id="insn-00aaced4"></a> `00aaced4` | `29 d5 37 91` | add x9,x9,#0xdf5 | `FALL_THROUGH`
<a id="insn-00aaced8"></a> `00aaced8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aacedc"></a> `00aacedc` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aacee0"></a> `00aacee0` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aacee4"></a> `00aacee4` | `ff c7 00 39` | strb wzr,[sp, #0x31] | `FALL_THROUGH`
<a id="insn-00aacee8"></a> `00aacee8` | `e8 83 00 39` | strb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaceec"></a> `00aaceec` | `e0 13 82 3c` | stur q0,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00aacef0"></a> `00aacef0` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00aacef4"></a> `00aacef4` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aacef8"></a> `00aacef8` | `21 f4 e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00aacefc"></a> `00aacefc` | `08 0b 00 f0` | adrp x8,0xc0f000 | `FALL_THROUGH`
<a id="insn-00aacf00"></a> `00aacf00` | `08 e1 0d 91` | add x8,x8,#0x378 | `FALL_THROUGH`
<a id="insn-00aacf04"></a> `00aacf04` | `c0 06 c0 3d` | ldr q0,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00aacf08"></a> `00aacf08` | `a8 57 3c a9` | stp x8,x21,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00aacf0c"></a> `00aacf0c` | `b5 03 01 d1` | sub x21,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aacf10"></a> `00aacf10` | `08 c3 85 52` | mov w8,#0x2e18 | `FALL_THROUGH`
<a id="insn-00aacf14"></a> `00aacf14` | `a0 03 9d 3c` | stur q0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00aacf18"></a> `00aacf18` | `b5 03 1e f8` | stur x21,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aacf1c"></a> `00aacf1c` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00aacf20"></a> `00aacf20` | `e1 e3 00 91` | add x1,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00aacf24"></a> `00aacf24` | `a5 03 01 d1` | sub x5,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aacf28"></a> `00aacf28` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aacf2c"></a> `00aacf2c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aacf30"></a> `00aacf30` | `84 04 80 52` | mov w4,#0x24 | `FALL_THROUGH`
<a id="insn-00aacf34"></a> `00aacf34` | `b9 6b f7 97` | bl 0x00887e18 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf38"></a> `00aacf38` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aacf3c"></a> `00aacf3c` | `9d 65 f7 97` | bl 0x008865b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf40"></a> `00aacf40` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aacf44"></a> `00aacf44` | `a8 03 01 d1` | sub x8,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aacf48"></a> `00aacf48` | `1f 00 08 eb` | cmp x0,x8 | `FALL_THROUGH`
<a id="insn-00aacf4c"></a> `00aacf4c` | `80 00 00 54` | b.eq 0x00aacf5c | `CONDITIONAL_JUMP`
<a id="insn-00aacf50"></a> `00aacf50` | `00 01 00 b4` | cbz x0,0x00aacf70 | `CONDITIONAL_JUMP`
<a id="insn-00aacf54"></a> `00aacf54` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00aacf58"></a> `00aacf58` | `03 00 00 14` | b 0x00aacf64 | `UNCONDITIONAL_JUMP`
<a id="insn-00aacf5c"></a> `00aacf5c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aacf60"></a> `00aacf60` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aacf64"></a> `00aacf64` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00aacf68"></a> `00aacf68` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aacf6c"></a> `00aacf6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aacf70"></a> `00aacf70` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aacf74"></a> `00aacf74` | `68 00 00 36` | tbz w8,#0x0,0x00aacf80 | `CONDITIONAL_JUMP`
<a id="insn-00aacf78"></a> `00aacf78` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aacf7c"></a> `00aacf7c` | `25 b8 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00aacf80"></a> `00aacf80` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aacf84"></a> `00aacf84` | `28 03 00 36` | tbz w8,#0x0,0x00aacfe8 | `CONDITIONAL_JUMP`
<a id="insn-00aacf88"></a> `00aacf88` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aacf8c"></a> `00aacf8c` | `16 00 00 14` | b 0x00aacfe4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aacf90"></a> `00aacf90` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aacf94"></a> `00aacf94` | `a0 03 01 d1` | sub x0,x29,#0x40 | `FALL_THROUGH`
<a id="insn-00aacf98"></a> `00aacf98` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00aacf9c"></a> `00aacf9c` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aacfa0"></a> `00aacfa0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aacfa4"></a> `00aacfa4` | `e8 e3 40 39` | ldrb w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aacfa8"></a> `00aacfa8` | `c8 00 00 37` | tbnz w8,#0x0,0x00aacfc0 | `CONDITIONAL_JUMP`
<a id="insn-00aacfac"></a> `00aacfac` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aacfb0"></a> `00aacfb0` | `08 01 00 37` | tbnz w8,#0x0,0x00aacfd0 | `CONDITIONAL_JUMP`
<a id="insn-00aacfb4"></a> `00aacfb4` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aacfb8"></a> `00aacfb8` | `48 01 00 37` | tbnz w8,#0x0,0x00aacfe0 | `CONDITIONAL_JUMP`
<a id="insn-00aacfbc"></a> `00aacfbc` | `0b 00 00 14` | b 0x00aacfe8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aacfc0"></a> `00aacfc0` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aacfc4"></a> `00aacfc4` | `13 b8 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00aacfc8"></a> `00aacfc8` | `e8 83 40 39` | ldrb w8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aacfcc"></a> `00aacfcc` | `48 ff 07 36` | tbz w8,#0x0,0x00aacfb4 | `CONDITIONAL_JUMP`
<a id="insn-00aacfd0"></a> `00aacfd0` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aacfd4"></a> `00aacfd4` | `0f b8 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00aacfd8"></a> `00aacfd8` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aacfdc"></a> `00aacfdc` | `68 00 00 36` | tbz w8,#0x0,0x00aacfe8 | `CONDITIONAL_JUMP`
<a id="insn-00aacfe0"></a> `00aacfe0` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aacfe4"></a> `00aacfe4` | `0b b8 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00aacfe8"></a> `00aacfe8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aacfec"></a> `00aacfec` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aacff0"></a> `00aacff0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aacff4"></a> `00aacff4` | `61 0a 00 54` | b.ne 0x00aad140 | `CONDITIONAL_JUMP`
<a id="insn-00aacff8"></a> `00aacff8` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aacffc"></a> `00aacffc` | `f7 53 40 f9` | ldr x23,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aad000"></a> `00aad000` | `f6 57 4b a9` | ldp x22,x21,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aad004"></a> `00aad004` | `fd 7b 49 a9` | ldp x29,x30,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aad008"></a> `00aad008` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00aad00c"></a> `00aad00c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aad140"></a> `00aad140` | `c0 b7 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aacd4c`](#insn-00aacd4c) 範囲 `[['00aacd4c', '00aacd7f']]`
  - `CONDITIONAL_JUMP` [`00aacd7c`](#insn-00aacd7c) → [`00aacddc`](#insn-00aacddc)
  - `FALL_THROUGH` [`00aacd7c`](#insn-00aacd7c) → [`00aacd80`](#insn-00aacd80)
- ブロック [`00aacd80`](#insn-00aacd80) 範囲 `[['00aacd80', '00aacd87']]`
  - `CONDITIONAL_JUMP` [`00aacd84`](#insn-00aacd84) → [`00aacfe8`](#insn-00aacfe8)
  - `FALL_THROUGH` [`00aacd84`](#insn-00aacd84) → [`00aacd88`](#insn-00aacd88)
- ブロック [`00aacd88`](#insn-00aacd88) 範囲 `[['00aacd88', '00aacd93']]`
  - `CONDITIONAL_JUMP` [`00aacd90`](#insn-00aacd90) → [`00aacfe8`](#insn-00aacfe8)
  - `FALL_THROUGH` [`00aacd90`](#insn-00aacd90) → [`00aacd94`](#insn-00aacd94)
- ブロック [`00aacd94`](#insn-00aacd94) 範囲 `[['00aacd94', '00aacd9b']]`
  - `CONDITIONAL_JUMP` [`00aacd98`](#insn-00aacd98) → [`00aacfe8`](#insn-00aacfe8)
  - `FALL_THROUGH` [`00aacd98`](#insn-00aacd98) → [`00aacd9c`](#insn-00aacd9c)
- ブロック [`00aacd9c`](#insn-00aacd9c) 範囲 `[['00aacd9c', '00aacdbf']]`
  - `CONDITIONAL_JUMP` [`00aacdbc`](#insn-00aacdbc) → [`00aad140`](#insn-00aad140)
  - `FALL_THROUGH` [`00aacdbc`](#insn-00aacdbc) → [`00aacdc0`](#insn-00aacdc0)
- ブロック [`00aacdc0`](#insn-00aacdc0) 範囲 `[['00aacdc0', '00aacddb']]`
- ブロック [`00aacddc`](#insn-00aacddc) 範囲 `[['00aacddc', '00aace1f']]`
  - `CONDITIONAL_JUMP` [`00aace1c`](#insn-00aace1c) → [`00aacecc`](#insn-00aacecc)
  - `FALL_THROUGH` [`00aace1c`](#insn-00aace1c) → [`00aace20`](#insn-00aace20)
- ブロック [`00aace20`](#insn-00aace20) 範囲 `[['00aace20', '00aace23']]`
  - `CONDITIONAL_JUMP` [`00aace20`](#insn-00aace20) → [`00aacfe8`](#insn-00aacfe8)
  - `FALL_THROUGH` [`00aace20`](#insn-00aace20) → [`00aace24`](#insn-00aace24)
- ブロック [`00aace24`](#insn-00aace24) 範囲 `[['00aace24', '00aacebf']]`
  - `CONDITIONAL_JUMP` [`00aacebc`](#insn-00aacebc) → [`00aacf90`](#insn-00aacf90)
  - `FALL_THROUGH` [`00aacebc`](#insn-00aacebc) → [`00aacec0`](#insn-00aacec0)
- ブロック [`00aacec0`](#insn-00aacec0) 範囲 `[['00aacec0', '00aacec3']]`
  - `CONDITIONAL_JUMP` [`00aacec0`](#insn-00aacec0) → [`00aacfa4`](#insn-00aacfa4)
  - `FALL_THROUGH` [`00aacec0`](#insn-00aacec0) → [`00aacec4`](#insn-00aacec4)
- ブロック [`00aacec4`](#insn-00aacec4) 範囲 `[['00aacec4', '00aacecb']]`
  - `UNCONDITIONAL_JUMP` [`00aacec8`](#insn-00aacec8) → [`00aacf98`](#insn-00aacf98)
- ブロック [`00aacecc`](#insn-00aacecc) 範囲 `[['00aacecc', '00aacf4f']]`
  - `CONDITIONAL_JUMP` [`00aacf4c`](#insn-00aacf4c) → [`00aacf5c`](#insn-00aacf5c)
  - `FALL_THROUGH` [`00aacf4c`](#insn-00aacf4c) → [`00aacf50`](#insn-00aacf50)
- ブロック [`00aacf50`](#insn-00aacf50) 範囲 `[['00aacf50', '00aacf53']]`
  - `CONDITIONAL_JUMP` [`00aacf50`](#insn-00aacf50) → [`00aacf70`](#insn-00aacf70)
  - `FALL_THROUGH` [`00aacf50`](#insn-00aacf50) → [`00aacf54`](#insn-00aacf54)
- ブロック [`00aacf54`](#insn-00aacf54) 範囲 `[['00aacf54', '00aacf5b']]`
  - `UNCONDITIONAL_JUMP` [`00aacf58`](#insn-00aacf58) → [`00aacf64`](#insn-00aacf64)
- ブロック [`00aacf5c`](#insn-00aacf5c) 範囲 `[['00aacf5c', '00aacf63']]`
  - `FALL_THROUGH` [`00aacf60`](#insn-00aacf60) → [`00aacf64`](#insn-00aacf64)
- ブロック [`00aacf64`](#insn-00aacf64) 範囲 `[['00aacf64', '00aacf6f']]`
  - `FALL_THROUGH` [`00aacf6c`](#insn-00aacf6c) → [`00aacf70`](#insn-00aacf70)
- ブロック [`00aacf70`](#insn-00aacf70) 範囲 `[['00aacf70', '00aacf77']]`
  - `CONDITIONAL_JUMP` [`00aacf74`](#insn-00aacf74) → [`00aacf80`](#insn-00aacf80)
  - `FALL_THROUGH` [`00aacf74`](#insn-00aacf74) → [`00aacf78`](#insn-00aacf78)
- ブロック [`00aacf78`](#insn-00aacf78) 範囲 `[['00aacf78', '00aacf7f']]`
  - `FALL_THROUGH` [`00aacf7c`](#insn-00aacf7c) → [`00aacf80`](#insn-00aacf80)
- ブロック [`00aacf80`](#insn-00aacf80) 範囲 `[['00aacf80', '00aacf87']]`
  - `CONDITIONAL_JUMP` [`00aacf84`](#insn-00aacf84) → [`00aacfe8`](#insn-00aacfe8)
  - `FALL_THROUGH` [`00aacf84`](#insn-00aacf84) → [`00aacf88`](#insn-00aacf88)
- ブロック [`00aacf88`](#insn-00aacf88) 範囲 `[['00aacf88', '00aacf8f']]`
  - `UNCONDITIONAL_JUMP` [`00aacf8c`](#insn-00aacf8c) → [`00aacfe4`](#insn-00aacfe4)
- ブロック [`00aacf90`](#insn-00aacf90) 範囲 `[['00aacf90', '00aacf97']]`
  - `FALL_THROUGH` [`00aacf94`](#insn-00aacf94) → [`00aacf98`](#insn-00aacf98)
- ブロック [`00aacf98`](#insn-00aacf98) 範囲 `[['00aacf98', '00aacfa3']]`
  - `FALL_THROUGH` [`00aacfa0`](#insn-00aacfa0) → [`00aacfa4`](#insn-00aacfa4)
- ブロック [`00aacfa4`](#insn-00aacfa4) 範囲 `[['00aacfa4', '00aacfab']]`
  - `CONDITIONAL_JUMP` [`00aacfa8`](#insn-00aacfa8) → [`00aacfc0`](#insn-00aacfc0)
  - `FALL_THROUGH` [`00aacfa8`](#insn-00aacfa8) → [`00aacfac`](#insn-00aacfac)
- ブロック [`00aacfac`](#insn-00aacfac) 範囲 `[['00aacfac', '00aacfb3']]`
  - `CONDITIONAL_JUMP` [`00aacfb0`](#insn-00aacfb0) → [`00aacfd0`](#insn-00aacfd0)
  - `FALL_THROUGH` [`00aacfb0`](#insn-00aacfb0) → [`00aacfb4`](#insn-00aacfb4)
- ブロック [`00aacfb4`](#insn-00aacfb4) 範囲 `[['00aacfb4', '00aacfbb']]`
  - `CONDITIONAL_JUMP` [`00aacfb8`](#insn-00aacfb8) → [`00aacfe0`](#insn-00aacfe0)
  - `FALL_THROUGH` [`00aacfb8`](#insn-00aacfb8) → [`00aacfbc`](#insn-00aacfbc)
- ブロック [`00aacfbc`](#insn-00aacfbc) 範囲 `[['00aacfbc', '00aacfbf']]`
  - `UNCONDITIONAL_JUMP` [`00aacfbc`](#insn-00aacfbc) → [`00aacfe8`](#insn-00aacfe8)
- ブロック [`00aacfc0`](#insn-00aacfc0) 範囲 `[['00aacfc0', '00aacfcf']]`
  - `CONDITIONAL_JUMP` [`00aacfcc`](#insn-00aacfcc) → [`00aacfb4`](#insn-00aacfb4)
  - `FALL_THROUGH` [`00aacfcc`](#insn-00aacfcc) → [`00aacfd0`](#insn-00aacfd0)
- ブロック [`00aacfd0`](#insn-00aacfd0) 範囲 `[['00aacfd0', '00aacfdf']]`
  - `CONDITIONAL_JUMP` [`00aacfdc`](#insn-00aacfdc) → [`00aacfe8`](#insn-00aacfe8)
  - `FALL_THROUGH` [`00aacfdc`](#insn-00aacfdc) → [`00aacfe0`](#insn-00aacfe0)
- ブロック [`00aacfe0`](#insn-00aacfe0) 範囲 `[['00aacfe0', '00aacfe3']]`
  - `FALL_THROUGH` [`00aacfe0`](#insn-00aacfe0) → [`00aacfe4`](#insn-00aacfe4)
- ブロック [`00aacfe4`](#insn-00aacfe4) 範囲 `[['00aacfe4', '00aacfe7']]`
  - `FALL_THROUGH` [`00aacfe4`](#insn-00aacfe4) → [`00aacfe8`](#insn-00aacfe8)
- ブロック [`00aacfe8`](#insn-00aacfe8) 範囲 `[['00aacfe8', '00aacff7']]`
  - `CONDITIONAL_JUMP` [`00aacff4`](#insn-00aacff4) → [`00aad140`](#insn-00aad140)
  - `FALL_THROUGH` [`00aacff4`](#insn-00aacff4) → [`00aacff8`](#insn-00aacff8)
- ブロック [`00aacff8`](#insn-00aacff8) 範囲 `[['00aacff8', '00aad00f']]`
- ブロック [`00aad140`](#insn-00aad140) 範囲 `[['00aad140', '00aad143']]`

## 命令位置別の参照

- [`00aacd50`](#insn-00aacd50) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd54`](#insn-00aacd54) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd58`](#insn-00aacd58) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd5c`](#insn-00aacd5c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd6c`](#insn-00aacd6c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd7c`](#insn-00aacd7c) → [`00aacddc`](#insn-00aacddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd84`](#insn-00aacd84) → [`00aacfe8`](#insn-00aacfe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd90`](#insn-00aacd90) → [`00aacfe8`](#insn-00aacfe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacd98`](#insn-00aacd98) → [`00aacfe8`](#insn-00aacfe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacda0`](#insn-00aacda0) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`00aacdac`](#insn-00aacdac) → [`00459efc`](../00459/00459efc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459efc` · 推定シンボル `None` · 推定型 `None`
- [`00aacdb4`](#insn-00aacdb4) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacdbc`](#insn-00aacdbc) → [`00aad140`](#insn-00aad140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacdc4`](#insn-00aacdc4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacdc8`](#insn-00aacdc8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacdcc`](#insn-00aacdcc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacdd0`](#insn-00aacdd0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacdd8`](#insn-00aacdd8) → [`00885f80`](../00885/00885f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00885f80` · 推定シンボル `None` · 推定型 `None`
- [`00aacde4`](#insn-00aacde4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aacdf4`](#insn-00aacdf4) → [`008847e4`](../00884/008847e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008847e4` · 推定シンボル `None` · 推定型 `None`
- [`00aacdfc`](#insn-00aacdfc) → [`00883d34`](../00883/00883d34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00883d34` · 推定シンボル `None` · 推定型 `None`
- [`00aace00`](#insn-00aace00) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aace0c`](#insn-00aace0c) → [`008847e4`](../00884/008847e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008847e4` · 推定シンボル `None` · 推定型 `None`
- [`00aace14`](#insn-00aace14) → [`00883d34`](../00883/00883d34.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00883d34` · 推定シンボル `None` · 推定型 `None`
- [`00aace1c`](#insn-00aace1c) → [`00aacecc`](#insn-00aacecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace20`](#insn-00aace20) → [`00aacfe8`](#insn-00aacfe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace24`](#insn-00aace24) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aace34`](#insn-00aace34) → `00294099`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aace3c`](#insn-00aace3c) → `Stack[-0xb7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace40`](#insn-00aace40) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace44`](#insn-00aace44) → `Stack[-0xc7]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace50`](#insn-00aace50) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00aace68`](#insn-00aace68) → [`004253b4`](../00425/004253b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004253b4` · 推定シンボル `None` · 推定型 `None`
- [`00aace78`](#insn-00aace78) → `00c0f2f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aace78`](#insn-00aace78) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace84`](#insn-00aace84) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aace88`](#insn-00aace88) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacea4`](#insn-00aacea4) → [`00887e18`](../00887/00887e18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00887e18` · 推定シンボル `None` · 推定型 `None`
- [`00aaceac`](#insn-00aaceac) → [`008865b0`](../00886/008865b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008865b0` · 推定シンボル `None` · 推定型 `None`
- [`00aaceb0`](#insn-00aaceb0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacebc`](#insn-00aacebc) → [`00aacf90`](#insn-00aacf90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacec0`](#insn-00aacec0) → [`00aacfa4`](#insn-00aacfa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacec8`](#insn-00aacec8) → [`00aacf98`](#insn-00aacf98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacecc`](#insn-00aacecc) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aacedc`](#insn-00aacedc) → `0029fdf5`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aacee4`](#insn-00aacee4) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacee8`](#insn-00aacee8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaceec`](#insn-00aaceec) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacef8`](#insn-00aacef8) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00aacf08`](#insn-00aacf08) → `00c0f378`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aacf08`](#insn-00aacf08) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf14`](#insn-00aacf14) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf18`](#insn-00aacf18) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf34`](#insn-00aacf34) → [`00887e18`](../00887/00887e18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00887e18` · 推定シンボル `None` · 推定型 `None`
- [`00aacf3c`](#insn-00aacf3c) → [`008865b0`](../00886/008865b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008865b0` · 推定シンボル `None` · 推定型 `None`
- [`00aacf40`](#insn-00aacf40) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf4c`](#insn-00aacf4c) → [`00aacf5c`](#insn-00aacf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf50`](#insn-00aacf50) → [`00aacf70`](#insn-00aacf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf58`](#insn-00aacf58) → [`00aacf64`](#insn-00aacf64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf64`](#insn-00aacf64) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf68`](#insn-00aacf68) → `00c0f398`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aacf68`](#insn-00aacf68) → `00c0f3a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aacf6c`](#insn-00aacf6c) → [`00aad2ec`](../00aad/00aad2ec.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aad2ec` · 推定シンボル `None` · 推定型 `None`
- [`00aacf6c`](#insn-00aacf6c) → [`00aad2f0`](../00aad/00aad2f0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aad2f0` · 推定シンボル `None` · 推定型 `None`
- [`00aacf70`](#insn-00aacf70) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf74`](#insn-00aacf74) → [`00aacf80`](#insn-00aacf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf78`](#insn-00aacf78) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf7c`](#insn-00aacf7c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00aacf80`](#insn-00aacf80) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf84`](#insn-00aacf84) → [`00aacfe8`](#insn-00aacfe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf88`](#insn-00aacf88) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf8c`](#insn-00aacf8c) → [`00aacfe4`](#insn-00aacfe4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf98`](#insn-00aacf98) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacf9c`](#insn-00aacf9c) → `00c0f318`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aacf9c`](#insn-00aacf9c) → `00c0f320`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00aacfa0`](#insn-00aacfa0) → [`00aad1d0`](../00aad/00aad1d0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aad1d0` · 推定シンボル `None` · 推定型 `None`
- [`00aacfa0`](#insn-00aacfa0) → [`00aad1d4`](../00aad/00aad1d4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aad1d4` · 推定シンボル `None` · 推定型 `None`
- [`00aacfa4`](#insn-00aacfa4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfa8`](#insn-00aacfa8) → [`00aacfc0`](#insn-00aacfc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfac`](#insn-00aacfac) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfb0`](#insn-00aacfb0) → [`00aacfd0`](#insn-00aacfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfb4`](#insn-00aacfb4) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfb8`](#insn-00aacfb8) → [`00aacfe0`](#insn-00aacfe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfbc`](#insn-00aacfbc) → [`00aacfe8`](#insn-00aacfe8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfc0`](#insn-00aacfc0) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfc4`](#insn-00aacfc4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00aacfc8`](#insn-00aacfc8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfcc`](#insn-00aacfcc) → [`00aacfb4`](#insn-00aacfb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfd0`](#insn-00aacfd0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfd4`](#insn-00aacfd4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00aacfd8`](#insn-00aacfd8) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfdc`](#insn-00aacfdc) → [`00aacfe8`](#insn-00aacfe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfe0`](#insn-00aacfe0) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacfe4`](#insn-00aacfe4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00aacfec`](#insn-00aacfec) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacff4`](#insn-00aacff4) → [`00aad140`](#insn-00aad140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacff8`](#insn-00aacff8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aacffc`](#insn-00aacffc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad000`](#insn-00aad000) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad004`](#insn-00aad004) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad140`](#insn-00aad140) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aacd50`](#insn-00aacd50)

~~~json
{
  "source": "00aacd50",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd54`](#insn-00aacd54)

~~~json
{
  "source": "00aacd54",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd58`](#insn-00aacd58)

~~~json
{
  "source": "00aacd58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd5c`](#insn-00aacd5c)

~~~json
{
  "source": "00aacd5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd6c`](#insn-00aacd6c)

~~~json
{
  "source": "00aacd6c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd7c`](#insn-00aacd7c)

~~~json
{
  "source": "00aacd7c",
  "target": "00aacddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd84`](#insn-00aacd84)

~~~json
{
  "source": "00aacd84",
  "target": "00aacfe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd90`](#insn-00aacd90)

~~~json
{
  "source": "00aacd90",
  "target": "00aacfe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacd98`](#insn-00aacd98)

~~~json
{
  "source": "00aacd98",
  "target": "00aacfe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacda0`](#insn-00aacda0)

~~~json
{
  "source": "00aacda0",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacdac`](#insn-00aacdac)

~~~json
{
  "source": "00aacdac",
  "target": "00459efc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacdb4`](#insn-00aacdb4)

~~~json
{
  "source": "00aacdb4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacdbc`](#insn-00aacdbc)

~~~json
{
  "source": "00aacdbc",
  "target": "00aad140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacdc4`](#insn-00aacdc4)

~~~json
{
  "source": "00aacdc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacdc8`](#insn-00aacdc8)

~~~json
{
  "source": "00aacdc8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacdcc`](#insn-00aacdcc)

~~~json
{
  "source": "00aacdcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacdd0`](#insn-00aacdd0)

~~~json
{
  "source": "00aacdd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacdd8`](#insn-00aacdd8)

~~~json
{
  "source": "00aacdd8",
  "target": "00885f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacde4`](#insn-00aacde4)

~~~json
{
  "source": "00aacde4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacdf4`](#insn-00aacdf4)

~~~json
{
  "source": "00aacdf4",
  "target": "008847e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacdfc`](#insn-00aacdfc)

~~~json
{
  "source": "00aacdfc",
  "target": "00883d34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace00`](#insn-00aace00)

~~~json
{
  "source": "00aace00",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace0c`](#insn-00aace0c)

~~~json
{
  "source": "00aace0c",
  "target": "008847e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace14`](#insn-00aace14)

~~~json
{
  "source": "00aace14",
  "target": "00883d34",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace1c`](#insn-00aace1c)

~~~json
{
  "source": "00aace1c",
  "target": "00aacecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace20`](#insn-00aace20)

~~~json
{
  "source": "00aace20",
  "target": "00aacfe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace24`](#insn-00aace24)

~~~json
{
  "source": "00aace24",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace34`](#insn-00aace34)

~~~json
{
  "source": "00aace34",
  "target": "00294099",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00294099",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6261636b73746167655f72657365743300",
  "capture_start": "00294099",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aace3c`](#insn-00aace3c)

~~~json
{
  "source": "00aace3c",
  "target": "Stack[-0xb7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace40`](#insn-00aace40)

~~~json
{
  "source": "00aace40",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace44`](#insn-00aace44)

~~~json
{
  "source": "00aace44",
  "target": "Stack[-0xc7]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace50`](#insn-00aace50)

~~~json
{
  "source": "00aace50",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace68`](#insn-00aace68)

~~~json
{
  "source": "00aace68",
  "target": "004253b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aace78`](#insn-00aace78)

~~~json
{
  "source": "00aace78",
  "target": "00c0f2f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f2f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aace78`](#insn-00aace78)

~~~json
{
  "source": "00aace78",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace84`](#insn-00aace84)

~~~json
{
  "source": "00aace84",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aace88`](#insn-00aace88)

~~~json
{
  "source": "00aace88",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacea4`](#insn-00aacea4)

~~~json
{
  "source": "00aacea4",
  "target": "00887e18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaceac`](#insn-00aaceac)

~~~json
{
  "source": "00aaceac",
  "target": "008865b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaceb0`](#insn-00aaceb0)

~~~json
{
  "source": "00aaceb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacebc`](#insn-00aacebc)

~~~json
{
  "source": "00aacebc",
  "target": "00aacf90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacec0`](#insn-00aacec0)

~~~json
{
  "source": "00aacec0",
  "target": "00aacfa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacec8`](#insn-00aacec8)

~~~json
{
  "source": "00aacec8",
  "target": "00aacf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacecc`](#insn-00aacecc)

~~~json
{
  "source": "00aacecc",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacedc`](#insn-00aacedc)

~~~json
{
  "source": "00aacedc",
  "target": "0029fdf5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029fdf5",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6261636b73746167655f72657365743400",
  "capture_start": "0029fdf5",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aacee4`](#insn-00aacee4)

~~~json
{
  "source": "00aacee4",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacee8`](#insn-00aacee8)

~~~json
{
  "source": "00aacee8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaceec`](#insn-00aaceec)

~~~json
{
  "source": "00aaceec",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacef8`](#insn-00aacef8)

~~~json
{
  "source": "00aacef8",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf08`](#insn-00aacf08)

~~~json
{
  "source": "00aacf08",
  "target": "00c0f378",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f378",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aacf08`](#insn-00aacf08)

~~~json
{
  "source": "00aacf08",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf14`](#insn-00aacf14)

~~~json
{
  "source": "00aacf14",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf18`](#insn-00aacf18)

~~~json
{
  "source": "00aacf18",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf34`](#insn-00aacf34)

~~~json
{
  "source": "00aacf34",
  "target": "00887e18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf3c`](#insn-00aacf3c)

~~~json
{
  "source": "00aacf3c",
  "target": "008865b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf40`](#insn-00aacf40)

~~~json
{
  "source": "00aacf40",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf4c`](#insn-00aacf4c)

~~~json
{
  "source": "00aacf4c",
  "target": "00aacf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf50`](#insn-00aacf50)

~~~json
{
  "source": "00aacf50",
  "target": "00aacf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf58`](#insn-00aacf58)

~~~json
{
  "source": "00aacf58",
  "target": "00aacf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf64`](#insn-00aacf64)

~~~json
{
  "source": "00aacf64",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf68`](#insn-00aacf68)

~~~json
{
  "source": "00aacf68",
  "target": "00c0f398",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f398",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aacf68`](#insn-00aacf68)

~~~json
{
  "source": "00aacf68",
  "target": "00c0f3a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f3a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aacf6c`](#insn-00aacf6c)

~~~json
{
  "source": "00aacf6c",
  "target": "00aad2ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf6c`](#insn-00aacf6c)

~~~json
{
  "source": "00aacf6c",
  "target": "00aad2f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf70`](#insn-00aacf70)

~~~json
{
  "source": "00aacf70",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf74`](#insn-00aacf74)

~~~json
{
  "source": "00aacf74",
  "target": "00aacf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf78`](#insn-00aacf78)

~~~json
{
  "source": "00aacf78",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf7c`](#insn-00aacf7c)

~~~json
{
  "source": "00aacf7c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacf80`](#insn-00aacf80)

~~~json
{
  "source": "00aacf80",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf84`](#insn-00aacf84)

~~~json
{
  "source": "00aacf84",
  "target": "00aacfe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf88`](#insn-00aacf88)

~~~json
{
  "source": "00aacf88",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf8c`](#insn-00aacf8c)

~~~json
{
  "source": "00aacf8c",
  "target": "00aacfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf98`](#insn-00aacf98)

~~~json
{
  "source": "00aacf98",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacf9c`](#insn-00aacf9c)

~~~json
{
  "source": "00aacf9c",
  "target": "00c0f318",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f318",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aacf9c`](#insn-00aacf9c)

~~~json
{
  "source": "00aacf9c",
  "target": "00c0f320",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f320",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aacfa0`](#insn-00aacfa0)

~~~json
{
  "source": "00aacfa0",
  "target": "00aad1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacfa0`](#insn-00aacfa0)

~~~json
{
  "source": "00aacfa0",
  "target": "00aad1d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacfa4`](#insn-00aacfa4)

~~~json
{
  "source": "00aacfa4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfa8`](#insn-00aacfa8)

~~~json
{
  "source": "00aacfa8",
  "target": "00aacfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfac`](#insn-00aacfac)

~~~json
{
  "source": "00aacfac",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfb0`](#insn-00aacfb0)

~~~json
{
  "source": "00aacfb0",
  "target": "00aacfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfb4`](#insn-00aacfb4)

~~~json
{
  "source": "00aacfb4",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfb8`](#insn-00aacfb8)

~~~json
{
  "source": "00aacfb8",
  "target": "00aacfe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfbc`](#insn-00aacfbc)

~~~json
{
  "source": "00aacfbc",
  "target": "00aacfe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfc0`](#insn-00aacfc0)

~~~json
{
  "source": "00aacfc0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfc4`](#insn-00aacfc4)

~~~json
{
  "source": "00aacfc4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacfc8`](#insn-00aacfc8)

~~~json
{
  "source": "00aacfc8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfcc`](#insn-00aacfcc)

~~~json
{
  "source": "00aacfcc",
  "target": "00aacfb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfd0`](#insn-00aacfd0)

~~~json
{
  "source": "00aacfd0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfd4`](#insn-00aacfd4)

~~~json
{
  "source": "00aacfd4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacfd8`](#insn-00aacfd8)

~~~json
{
  "source": "00aacfd8",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfdc`](#insn-00aacfdc)

~~~json
{
  "source": "00aacfdc",
  "target": "00aacfe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfe0`](#insn-00aacfe0)

~~~json
{
  "source": "00aacfe0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacfe4`](#insn-00aacfe4)

~~~json
{
  "source": "00aacfe4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aacfec`](#insn-00aacfec)

~~~json
{
  "source": "00aacfec",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacff4`](#insn-00aacff4)

~~~json
{
  "source": "00aacff4",
  "target": "00aad140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacff8`](#insn-00aacff8)

~~~json
{
  "source": "00aacff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aacffc`](#insn-00aacffc)

~~~json
{
  "source": "00aacffc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad000`](#insn-00aad000)

~~~json
{
  "source": "00aad000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad004`](#insn-00aad004)

~~~json
{
  "source": "00aad004",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad140`](#insn-00aad140)

~~~json
{
  "source": "00aad140",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
