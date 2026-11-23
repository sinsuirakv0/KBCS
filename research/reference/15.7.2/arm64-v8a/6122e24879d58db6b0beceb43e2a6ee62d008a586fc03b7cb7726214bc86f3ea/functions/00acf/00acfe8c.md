# 00acfe8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acff54`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acf/00acff54.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-fec073a58d33505ac858bbb3d588de6f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acfe8c",
  "name": "FUN_00acfe8c",
  "size": 448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e8ab791f74e1c2ca22e39abbf41e001430122562a301081ac618cbb7acf6a8ec",
  "source_text_sha256": "e8ab791f74e1c2ca22e39abbf41e001430122562a301081ac618cbb7acf6a8ec",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acfe8c",
        "00ad0047"
      ],
      [
        "00ad00ac",
        "00ad00af"
      ]
    ],
    "bytes_sha256": "5f5d2bc0296cb0b805e9580a3a4cc4ae70c2a9a28283f1ef37ee3ce0e0ac1e79",
    "instruction_count": 112,
    "instruction_bytes": 448,
    "body_bytes": 448,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00acfa20](../00acf/00acfa20.md)

## 呼び出し先

- [0053d580](../0053d/0053d580.md)
- [00574730](../00574/00574730.md)
- [00574744](../00574/00574744.md)
- [0057474c](../00574/0057474c.md)
- [00574fec](../00574/00574fec.md)
- [00728090](../00728/00728090.md)
- [00ad05f0](../00ad0/00ad05f0.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"{\n  \"client\":{\n    \"version\":\"%d\",\n    \"countryCode\":\"%s\"\n  },\n  \"os\":{\n    \"type\":\"%s\",\n    \"version\":\"%s\"\n  },\n  \"device\":{\n    \"model\":\"%s\"\n  }\n}"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3752 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */
/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00acfe8c(undefined8 param_1)

{
  long lVar1;
  undefined8 uVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  long lVar7;
  byte local_d0 [16];
  void *local_c0;
  byte local_b8 [16];
  void *local_a8;
  byte local_a0 [16];
  void *local_90;
  byte local_88 [16];
  void *local_78;
  ulong local_70;
  undefined8 uStack_68;
  char *local_60;
  byte local_50 [16];
  void *local_40;
  undefined1 auStack_38 [8];
  long *local_30;
  long local_28;
  
  lVar1 = tpidr_el0;
  local_28 = *(long *)(lVar1 + 0x28);
  local_60 = (char *)_Znwm(0x98);
  uStack_68 = _UNK_002b1198;
  local_70 = _DAT_002b1190;
  local_60[0x94] = '\0';
  local_60[0x90] = ' ';
  uVar6 = s____client_____version____d____co_0029a50b._136_8_;
  uVar5 = s____client_____version____d____co_0029a50b._128_8_;
  uVar4 = s____client_____version____d____co_0029a50b._120_8_;
  uVar3 = s____client_____version____d____co_0029a50b._112_8_;
  uVar2 = s____client_____version____d____co_0029a50b._96_8_;
  local_60[0x91] = '}';
  local_60[0x92] = '\n';
  local_60[0x93] = '}';
  *(undefined8 *)(local_60 + 0x68) = s____client_____version____d____co_0029a50b._104_8_;
  *(undefined8 *)(local_60 + 0x60) = uVar2;
  *(undefined8 *)(local_60 + 0x78) = uVar4;
  *(undefined8 *)(local_60 + 0x70) = uVar3;
  *(undefined8 *)(local_60 + 0x88) = uVar6;
  *(undefined8 *)(local_60 + 0x80) = uVar5;
  uVar4 = s____client_____version____d____co_0029a50b._56_8_;
  uVar3 = s____client_____version____d____co_0029a50b._48_8_;
  uVar2 = s____client_____version____d____co_0029a50b._32_8_;
  *(undefined8 *)(local_60 + 0x28) = s____client_____version____d____co_0029a50b._40_8_;
  *(undefined8 *)(local_60 + 0x20) = uVar2;
  *(undefined8 *)(local_60 + 0x38) = uVar4;
  *(undefined8 *)(local_60 + 0x30) = uVar3;
  uVar4 = s____client_____version____d____co_0029a50b._88_8_;
  uVar3 = s____client_____version____d____co_0029a50b._80_8_;
  uVar2 = s____client_____version____d____co_0029a50b._64_8_;
  *(undefined8 *)(local_60 + 0x48) = s____client_____version____d____co_0029a50b._72_8_;
  *(undefined8 *)(local_60 + 0x40) = uVar2;
  *(undefined8 *)(local_60 + 0x58) = uVar4;
  *(undefined8 *)(local_60 + 0x50) = uVar3;
  uVar4 = s____client_____version____d____co_0029a50b._24_8_;
  uVar3 = s____client_____version____d____co_0029a50b._16_8_;
  uVar2 = s____client_____version____d____co_0029a50b._0_8_;
  *(undefined8 *)(local_60 + 8) = s____client_____version____d____co_0029a50b._8_8_;
  *(undefined8 *)local_60 = uVar2;
  *(undefined8 *)(local_60 + 0x18) = uVar4;
  *(undefined8 *)(local_60 + 0x10) = uVar3;
  FUN_00728090(local_88);
  thunk_FUN_00568a44(local_a0);
  thunk_FUN_0056bfc8(local_b8);
  thunk_FUN_00568c04(local_d0);
  FUN_00ad05f0(local_50,&local_70,0x24cae,local_88,local_a0,local_b8,local_d0);
  thunk_FUN_00567ef0(auStack_38,local_50);
  thunk_FUN_0055dbb0(param_1,auStack_38,0);
  if ((local_30 != (long *)0x0) &&
     (lVar7 = FUN_00bd6d90(0xffffffffffffffff,local_30 + 1), lVar7 == 0)) {
    (**(code **)(*local_30 + 0x10))(local_30);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_30);
  }
  if ((local_50[0] & 1) != 0) {
    _ZdlPv(local_40);
  }
  if ((local_d0[0] & 1) != 0) {
    _ZdlPv(local_c0);
  }
  if ((local_b8[0] & 1) != 0) {
    _ZdlPv(local_a8);
  }
  if ((local_a0[0] & 1) != 0) {
    _ZdlPv(local_90);
  }
  if ((local_88[0] & 1) != 0) {
    _ZdlPv(local_78);
  }
  if ((local_70 & 1) != 0) {
    _ZdlPv(local_60);
  }
  if (*(long *)(lVar1 + 0x28) == local_28) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acfe8c"></a> `00acfe8c` | `ff 43 03 d1` | sub sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00acfe90"></a> `00acfe90` | `fd 7b 0b a9` | stp x29,x30,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acfe94"></a> `00acfe94` | `f4 4f 0c a9` | stp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00acfe98"></a> `00acfe98` | `fd c3 02 91` | add x29,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00acfe9c"></a> `00acfe9c` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acfea0"></a> `00acfea0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00acfea4"></a> `00acfea4` | `00 13 80 52` | mov w0,#0x98 | `FALL_THROUGH`
<a id="insn-00acfea8"></a> `00acfea8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00acfeac"></a> `00acfeac` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acfeb0"></a> `00acfeb0` | `24 2c 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00acfeb4"></a> `00acfeb4` | `08 bf ff d0` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00acfeb8"></a> `00acfeb8` | `a0 03 1c f8` | stur x0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00acfebc"></a> `00acfebc` | `00 65 c0 3d` | ldr q0,[x8, #0x190] | `FALL_THROUGH`
<a id="insn-00acfec0"></a> `00acfec0` | `08 a4 8f 52` | mov w8,#0x7d20 | `FALL_THROUGH`
<a id="insn-00acfec4"></a> `00acfec4` | `1f 50 02 39` | strb wzr,[x0, #0x94] | `FALL_THROUGH`
<a id="insn-00acfec8"></a> `00acfec8` | `48 a1 af 72` | movk w8,#0x7d0a, LSL #16 | `FALL_THROUGH`
<a id="insn-00acfecc"></a> `00acfecc` | `08 90 00 b9` | str w8,[x0, #0x90] | `FALL_THROUGH`
<a id="insn-00acfed0"></a> `00acfed0` | `48 be ff f0` | adrp x8,0x29a000 | `FALL_THROUGH`
<a id="insn-00acfed4"></a> `00acfed4` | `08 2d 14 91` | add x8,x8,#0x50b | `FALL_THROUGH`
<a id="insn-00acfed8"></a> `00acfed8` | `01 09 43 ad` | ldp q1,q2,[x8, #0x60] | `FALL_THROUGH`
<a id="insn-00acfedc"></a> `00acfedc` | `a0 03 9b 3c` | stur q0,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00acfee0"></a> `00acfee0` | `00 21 c0 3d` | ldr q0,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00acfee4"></a> `00acfee4` | `01 08 03 ad` | stp q1,q2,[x0, #0x60] | `FALL_THROUGH`
<a id="insn-00acfee8"></a> `00acfee8` | `00 20 80 3d` | str q0,[x0, #0x80] | `FALL_THROUGH`
<a id="insn-00acfeec"></a> `00acfeec` | `01 01 41 ad` | ldp q1,q0,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00acfef0"></a> `00acfef0` | `01 00 01 ad` | stp q1,q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00acfef4"></a> `00acfef4` | `00 09 42 ad` | ldp q0,q2,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00acfef8"></a> `00acfef8` | `00 08 02 ad` | stp q0,q2,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00acfefc"></a> `00acfefc` | `00 05 40 ad` | ldp q0,q1,[x8] | `FALL_THROUGH`
<a id="insn-00acff00"></a> `00acff00` | `00 04 00 ad` | stp q0,q1,[x0] | `FALL_THROUGH`
<a id="insn-00acff04"></a> `00acff04` | `e8 23 01 91` | add x8,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00acff08"></a> `00acff08` | `62 60 f1 97` | bl 0x00728090 | `UNCONDITIONAL_CALL`
<a id="insn-00acff0c"></a> `00acff0c` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00acff10"></a> `00acff10` | `0d 92 ea 97` | bl 0x00574744 | `UNCONDITIONAL_CALL`
<a id="insn-00acff14"></a> `00acff14` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00acff18"></a> `00acff18` | `35 94 ea 97` | bl 0x00574fec | `UNCONDITIONAL_CALL`
<a id="insn-00acff1c"></a> `00acff1c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00acff20"></a> `00acff20` | `0b 92 ea 97` | bl 0x0057474c | `UNCONDITIONAL_CALL`
<a id="insn-00acff24"></a> `00acff24` | `c1 95 89 52` | mov w1,#0x4cae | `FALL_THROUGH`
<a id="insn-00acff28"></a> `00acff28` | `a8 c3 00 d1` | sub x8,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00acff2c"></a> `00acff2c` | `a0 43 01 d1` | sub x0,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00acff30"></a> `00acff30` | `e2 23 01 91` | add x2,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00acff34"></a> `00acff34` | `e3 c3 00 91` | add x3,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00acff38"></a> `00acff38` | `e4 63 00 91` | add x4,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00acff3c"></a> `00acff3c` | `e5 03 00 91` | mov x5,sp | `FALL_THROUGH`
<a id="insn-00acff40"></a> `00acff40` | `41 00 a0 72` | movk w1,#0x2, LSL #16 | `FALL_THROUGH`
<a id="insn-00acff44"></a> `00acff44` | `ab 01 00 94` | bl 0x00ad05f0 | `UNCONDITIONAL_CALL`
<a id="insn-00acff48"></a> `00acff48` | `a8 63 00 d1` | sub x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acff4c"></a> `00acff4c` | `a0 c3 00 d1` | sub x0,x29,#0x30 | `FALL_THROUGH`
<a id="insn-00acff50"></a> `00acff50` | `f8 91 ea 97` | bl 0x00574730 | `UNCONDITIONAL_CALL`
<a id="insn-00acff54"></a> `00acff54` | `a0 63 00 d1` | sub x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acff58"></a> `00acff58` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00acff5c"></a> `00acff5c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acff60"></a> `00acff60` | `88 b5 e9 97` | bl 0x0053d580 | `UNCONDITIONAL_CALL`
<a id="insn-00acff64"></a> `00acff64` | `b3 03 5f f8` | ldur x19,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acff68"></a> `00acff68` | `b3 00 00 b4` | cbz x19,0x00acff7c | `CONDITIONAL_JUMP`
<a id="insn-00acff6c"></a> `00acff6c` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00acff70"></a> `00acff70` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acff74"></a> `00acff74` | `87 1b 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00acff78"></a> `00acff78` | `e0 02 00 b4` | cbz x0,0x00acffd4 | `CONDITIONAL_JUMP`
<a id="insn-00acff7c"></a> `00acff7c` | `a8 03 5d 38` | ldurb w8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00acff80"></a> `00acff80` | `a8 03 00 37` | tbnz w8,#0x0,0x00acfff4 | `CONDITIONAL_JUMP`
<a id="insn-00acff84"></a> `00acff84` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00acff88"></a> `00acff88` | `e8 03 00 37` | tbnz w8,#0x0,0x00ad0004 | `CONDITIONAL_JUMP`
<a id="insn-00acff8c"></a> `00acff8c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00acff90"></a> `00acff90` | `28 04 00 37` | tbnz w8,#0x0,0x00ad0014 | `CONDITIONAL_JUMP`
<a id="insn-00acff94"></a> `00acff94` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acff98"></a> `00acff98` | `68 04 00 37` | tbnz w8,#0x0,0x00ad0024 | `CONDITIONAL_JUMP`
<a id="insn-00acff9c"></a> `00acff9c` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00acffa0"></a> `00acffa0` | `a8 04 00 37` | tbnz w8,#0x0,0x00ad0034 | `CONDITIONAL_JUMP`
<a id="insn-00acffa4"></a> `00acffa4` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00acffa8"></a> `00acffa8` | `68 00 00 36` | tbz w8,#0x0,0x00acffb4 | `CONDITIONAL_JUMP`
<a id="insn-00acffac"></a> `00acffac` | `a0 03 5c f8` | ldur x0,[x29, #-0x40] | `FALL_THROUGH`
<a id="insn-00acffb0"></a> `00acffb0` | `ec 2b 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acffb4"></a> `00acffb4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00acffb8"></a> `00acffb8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acffbc"></a> `00acffbc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acffc0"></a> `00acffc0` | `61 07 00 54` | b.ne 0x00ad00ac | `CONDITIONAL_JUMP`
<a id="insn-00acffc4"></a> `00acffc4` | `f4 4f 4c a9` | ldp x20,x19,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00acffc8"></a> `00acffc8` | `fd 7b 4b a9` | ldp x29,x30,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acffcc"></a> `00acffcc` | `ff 43 03 91` | add sp,sp,#0xd0 | `FALL_THROUGH`
<a id="insn-00acffd0"></a> `00acffd0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acffd4"></a> `00acffd4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acffd8"></a> `00acffd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acffdc"></a> `00acffdc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acffe0"></a> `00acffe0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acffe4"></a> `00acffe4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acffe8"></a> `00acffe8` | `d2 2b 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00acffec"></a> `00acffec` | `a8 03 5d 38` | ldurb w8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-00acfff0"></a> `00acfff0` | `a8 fc 07 36` | tbz w8,#0x0,0x00acff84 | `CONDITIONAL_JUMP`
<a id="insn-00acfff4"></a> `00acfff4` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00acfff8"></a> `00acfff8` | `da 2b 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acfffc"></a> `00acfffc` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-00ad0000"></a> `00ad0000` | `68 fc 07 36` | tbz w8,#0x0,0x00acff8c | `CONDITIONAL_JUMP`
<a id="insn-00ad0004"></a> `00ad0004` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ad0008"></a> `00ad0008` | `d6 2b 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ad000c"></a> `00ad000c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad0010"></a> `00ad0010` | `28 fc 07 36` | tbz w8,#0x0,0x00acff94 | `CONDITIONAL_JUMP`
<a id="insn-00ad0014"></a> `00ad0014` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ad0018"></a> `00ad0018` | `d2 2b 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ad001c"></a> `00ad001c` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad0020"></a> `00ad0020` | `e8 fb 07 36` | tbz w8,#0x0,0x00acff9c | `CONDITIONAL_JUMP`
<a id="insn-00ad0024"></a> `00ad0024` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ad0028"></a> `00ad0028` | `ce 2b 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ad002c"></a> `00ad002c` | `e8 23 41 39` | ldrb w8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00ad0030"></a> `00ad0030` | `a8 fb 07 36` | tbz w8,#0x0,0x00acffa4 | `CONDITIONAL_JUMP`
<a id="insn-00ad0034"></a> `00ad0034` | `e0 2f 40 f9` | ldr x0,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00ad0038"></a> `00ad0038` | `ca 2b 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ad003c"></a> `00ad003c` | `a8 03 5b 38` | ldurb w8,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00ad0040"></a> `00ad0040` | `68 fb 07 37` | tbnz w8,#0x0,0x00acffac | `CONDITIONAL_JUMP`
<a id="insn-00ad0044"></a> `00ad0044` | `dc ff ff 17` | b 0x00acffb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad00ac"></a> `00ad00ac` | `b9 2b 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acfe8c`](#insn-00acfe8c) 範囲 `[['00acfe8c', '00acff6b']]`
  - `CONDITIONAL_JUMP` [`00acff68`](#insn-00acff68) → [`00acff7c`](#insn-00acff7c)
  - `FALL_THROUGH` [`00acff68`](#insn-00acff68) → [`00acff6c`](#insn-00acff6c)
- ブロック [`00acff6c`](#insn-00acff6c) 範囲 `[['00acff6c', '00acff7b']]`
  - `CONDITIONAL_JUMP` [`00acff78`](#insn-00acff78) → [`00acffd4`](#insn-00acffd4)
  - `FALL_THROUGH` [`00acff78`](#insn-00acff78) → [`00acff7c`](#insn-00acff7c)
- ブロック [`00acff7c`](#insn-00acff7c) 範囲 `[['00acff7c', '00acff83']]`
  - `CONDITIONAL_JUMP` [`00acff80`](#insn-00acff80) → [`00acfff4`](#insn-00acfff4)
  - `FALL_THROUGH` [`00acff80`](#insn-00acff80) → [`00acff84`](#insn-00acff84)
- ブロック [`00acff84`](#insn-00acff84) 範囲 `[['00acff84', '00acff8b']]`
  - `CONDITIONAL_JUMP` [`00acff88`](#insn-00acff88) → [`00ad0004`](#insn-00ad0004)
  - `FALL_THROUGH` [`00acff88`](#insn-00acff88) → [`00acff8c`](#insn-00acff8c)
- ブロック [`00acff8c`](#insn-00acff8c) 範囲 `[['00acff8c', '00acff93']]`
  - `CONDITIONAL_JUMP` [`00acff90`](#insn-00acff90) → [`00ad0014`](#insn-00ad0014)
  - `FALL_THROUGH` [`00acff90`](#insn-00acff90) → [`00acff94`](#insn-00acff94)
- ブロック [`00acff94`](#insn-00acff94) 範囲 `[['00acff94', '00acff9b']]`
  - `CONDITIONAL_JUMP` [`00acff98`](#insn-00acff98) → [`00ad0024`](#insn-00ad0024)
  - `FALL_THROUGH` [`00acff98`](#insn-00acff98) → [`00acff9c`](#insn-00acff9c)
- ブロック [`00acff9c`](#insn-00acff9c) 範囲 `[['00acff9c', '00acffa3']]`
  - `CONDITIONAL_JUMP` [`00acffa0`](#insn-00acffa0) → [`00ad0034`](#insn-00ad0034)
  - `FALL_THROUGH` [`00acffa0`](#insn-00acffa0) → [`00acffa4`](#insn-00acffa4)
- ブロック [`00acffa4`](#insn-00acffa4) 範囲 `[['00acffa4', '00acffab']]`
  - `CONDITIONAL_JUMP` [`00acffa8`](#insn-00acffa8) → [`00acffb4`](#insn-00acffb4)
  - `FALL_THROUGH` [`00acffa8`](#insn-00acffa8) → [`00acffac`](#insn-00acffac)
- ブロック [`00acffac`](#insn-00acffac) 範囲 `[['00acffac', '00acffb3']]`
  - `FALL_THROUGH` [`00acffb0`](#insn-00acffb0) → [`00acffb4`](#insn-00acffb4)
- ブロック [`00acffb4`](#insn-00acffb4) 範囲 `[['00acffb4', '00acffc3']]`
  - `CONDITIONAL_JUMP` [`00acffc0`](#insn-00acffc0) → [`00ad00ac`](#insn-00ad00ac)
  - `FALL_THROUGH` [`00acffc0`](#insn-00acffc0) → [`00acffc4`](#insn-00acffc4)
- ブロック [`00acffc4`](#insn-00acffc4) 範囲 `[['00acffc4', '00acffd3']]`
- ブロック [`00acffd4`](#insn-00acffd4) 範囲 `[['00acffd4', '00acfff3']]`
  - `CONDITIONAL_JUMP` [`00acfff0`](#insn-00acfff0) → [`00acff84`](#insn-00acff84)
  - `FALL_THROUGH` [`00acfff0`](#insn-00acfff0) → [`00acfff4`](#insn-00acfff4)
- ブロック [`00acfff4`](#insn-00acfff4) 範囲 `[['00acfff4', '00ad0003']]`
  - `CONDITIONAL_JUMP` [`00ad0000`](#insn-00ad0000) → [`00acff8c`](#insn-00acff8c)
  - `FALL_THROUGH` [`00ad0000`](#insn-00ad0000) → [`00ad0004`](#insn-00ad0004)
- ブロック [`00ad0004`](#insn-00ad0004) 範囲 `[['00ad0004', '00ad0013']]`
  - `CONDITIONAL_JUMP` [`00ad0010`](#insn-00ad0010) → [`00acff94`](#insn-00acff94)
  - `FALL_THROUGH` [`00ad0010`](#insn-00ad0010) → [`00ad0014`](#insn-00ad0014)
- ブロック [`00ad0014`](#insn-00ad0014) 範囲 `[['00ad0014', '00ad0023']]`
  - `CONDITIONAL_JUMP` [`00ad0020`](#insn-00ad0020) → [`00acff9c`](#insn-00acff9c)
  - `FALL_THROUGH` [`00ad0020`](#insn-00ad0020) → [`00ad0024`](#insn-00ad0024)
- ブロック [`00ad0024`](#insn-00ad0024) 範囲 `[['00ad0024', '00ad0033']]`
  - `CONDITIONAL_JUMP` [`00ad0030`](#insn-00ad0030) → [`00acffa4`](#insn-00acffa4)
  - `FALL_THROUGH` [`00ad0030`](#insn-00ad0030) → [`00ad0034`](#insn-00ad0034)
- ブロック [`00ad0034`](#insn-00ad0034) 範囲 `[['00ad0034', '00ad0043']]`
  - `CONDITIONAL_JUMP` [`00ad0040`](#insn-00ad0040) → [`00acffac`](#insn-00acffac)
  - `FALL_THROUGH` [`00ad0040`](#insn-00ad0040) → [`00ad0044`](#insn-00ad0044)
- ブロック [`00ad0044`](#insn-00ad0044) 範囲 `[['00ad0044', '00ad0047']]`
  - `UNCONDITIONAL_JUMP` [`00ad0044`](#insn-00ad0044) → [`00acffb4`](#insn-00acffb4)
- ブロック [`00ad00ac`](#insn-00ad00ac) 範囲 `[['00ad00ac', '00ad00af']]`

## 命令位置別の参照

- [`00acfe90`](#insn-00acfe90) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfe94`](#insn-00acfe94) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfeac`](#insn-00acfeac) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfeb0`](#insn-00acfeb0) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00acfeb8`](#insn-00acfeb8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfebc`](#insn-00acfebc) → `002b1190`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfed8`](#insn-00acfed8) → `0029a56b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfed8`](#insn-00acfed8) → `0029a57b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfedc`](#insn-00acfedc) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfee0`](#insn-00acfee0) → `0029a58b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfeec`](#insn-00acfeec) → `0029a52b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfeec`](#insn-00acfeec) → `0029a53b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfef4`](#insn-00acfef4) → `0029a54b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfef4`](#insn-00acfef4) → `0029a55b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfefc`](#insn-00acfefc) → `0029a50b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acfefc`](#insn-00acfefc) → `0029a51b`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acff08`](#insn-00acff08) → [`00728090`](../00728/00728090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00728090` · 推定シンボル `None` · 推定型 `None`
- [`00acff10`](#insn-00acff10) → [`00574744`](../00574/00574744.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574744` · 推定シンボル `None` · 推定型 `None`
- [`00acff18`](#insn-00acff18) → [`00574fec`](../00574/00574fec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574fec` · 推定シンボル `None` · 推定型 `None`
- [`00acff20`](#insn-00acff20) → [`0057474c`](../00574/0057474c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057474c` · 推定シンボル `None` · 推定型 `None`
- [`00acff44`](#insn-00acff44) → [`00ad05f0`](../00ad0/00ad05f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ad05f0` · 推定シンボル `None` · 推定型 `None`
- [`00acff50`](#insn-00acff50) → [`00574730`](../00574/00574730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574730` · 推定シンボル `None` · 推定型 `None`
- [`00acff60`](#insn-00acff60) → [`0053d580`](../0053d/0053d580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0053d580` · 推定シンボル `None` · 推定型 `None`
- [`00acff64`](#insn-00acff64) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff68`](#insn-00acff68) → [`00acff7c`](#insn-00acff7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff74`](#insn-00acff74) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00acff78`](#insn-00acff78) → [`00acffd4`](#insn-00acffd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff7c`](#insn-00acff7c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff80`](#insn-00acff80) → [`00acfff4`](#insn-00acfff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff84`](#insn-00acff84) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff88`](#insn-00acff88) → [`00ad0004`](#insn-00ad0004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff8c`](#insn-00acff8c) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff90`](#insn-00acff90) → [`00ad0014`](#insn-00ad0014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff94`](#insn-00acff94) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff98`](#insn-00acff98) → [`00ad0024`](#insn-00ad0024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acff9c`](#insn-00acff9c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffa0`](#insn-00acffa0) → [`00ad0034`](#insn-00ad0034) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffa4`](#insn-00acffa4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffa8`](#insn-00acffa8) → [`00acffb4`](#insn-00acffb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffac`](#insn-00acffac) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffb0`](#insn-00acffb0) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acffb8`](#insn-00acffb8) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffc0`](#insn-00acffc0) → [`00ad00ac`](#insn-00ad00ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffc4`](#insn-00acffc4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffc8`](#insn-00acffc8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acffe8`](#insn-00acffe8) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00acffec`](#insn-00acffec) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfff0`](#insn-00acfff0) → [`00acff84`](#insn-00acff84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfff4`](#insn-00acfff4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acfff8`](#insn-00acfff8) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acfffc`](#insn-00acfffc) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0000`](#insn-00ad0000) → [`00acff8c`](#insn-00acff8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0004`](#insn-00ad0004) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0008`](#insn-00ad0008) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ad000c`](#insn-00ad000c) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0010`](#insn-00ad0010) → [`00acff94`](#insn-00acff94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0014`](#insn-00ad0014) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0018`](#insn-00ad0018) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ad001c`](#insn-00ad001c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0020`](#insn-00ad0020) → [`00acff9c`](#insn-00acff9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0024`](#insn-00ad0024) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0028`](#insn-00ad0028) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ad002c`](#insn-00ad002c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0030`](#insn-00ad0030) → [`00acffa4`](#insn-00acffa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0034`](#insn-00ad0034) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0038`](#insn-00ad0038) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ad003c`](#insn-00ad003c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0040`](#insn-00ad0040) → [`00acffac`](#insn-00acffac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad0044`](#insn-00ad0044) → [`00acffb4`](#insn-00acffb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad00ac`](#insn-00ad00ac) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acfe90`](#insn-00acfe90)

~~~json
{
  "source": "00acfe90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfe94`](#insn-00acfe94)

~~~json
{
  "source": "00acfe94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfeac`](#insn-00acfeac)

~~~json
{
  "source": "00acfeac",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfeb0`](#insn-00acfeb0)

~~~json
{
  "source": "00acfeb0",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfeb8`](#insn-00acfeb8)

~~~json
{
  "source": "00acfeb8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfebc`](#insn-00acfebc)

~~~json
{
  "source": "00acfebc",
  "target": "002b1190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfed8`](#insn-00acfed8)

~~~json
{
  "source": "00acfed8",
  "target": "0029a56b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a50b",
  "offset": 96,
  "size": 149,
  "datatype": "string",
  "bytes": "7b0a202022636c69656e74223a7b0a202020202276657273696f6e223a222564",
  "capture_start": "0029a50b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfed8`](#insn-00acfed8)

~~~json
{
  "source": "00acfed8",
  "target": "0029a57b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a50b",
  "offset": 112,
  "size": 149,
  "datatype": "string",
  "bytes": "7b0a202022636c69656e74223a7b0a202020202276657273696f6e223a222564",
  "capture_start": "0029a50b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfedc`](#insn-00acfedc)

~~~json
{
  "source": "00acfedc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfee0`](#insn-00acfee0)

~~~json
{
  "source": "00acfee0",
  "target": "0029a58b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a50b",
  "offset": 128,
  "size": 149,
  "datatype": "string",
  "bytes": "7b0a202022636c69656e74223a7b0a202020202276657273696f6e223a222564",
  "capture_start": "0029a50b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfeec`](#insn-00acfeec)

~~~json
{
  "source": "00acfeec",
  "target": "0029a52b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a50b",
  "offset": 32,
  "size": 149,
  "datatype": "string",
  "bytes": "7b0a202022636c69656e74223a7b0a202020202276657273696f6e223a222564",
  "capture_start": "0029a50b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfeec`](#insn-00acfeec)

~~~json
{
  "source": "00acfeec",
  "target": "0029a53b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a50b",
  "offset": 48,
  "size": 149,
  "datatype": "string",
  "bytes": "7b0a202022636c69656e74223a7b0a202020202276657273696f6e223a222564",
  "capture_start": "0029a50b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfef4`](#insn-00acfef4)

~~~json
{
  "source": "00acfef4",
  "target": "0029a54b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a50b",
  "offset": 64,
  "size": 149,
  "datatype": "string",
  "bytes": "7b0a202022636c69656e74223a7b0a202020202276657273696f6e223a222564",
  "capture_start": "0029a50b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfef4`](#insn-00acfef4)

~~~json
{
  "source": "00acfef4",
  "target": "0029a55b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a50b",
  "offset": 80,
  "size": 149,
  "datatype": "string",
  "bytes": "7b0a202022636c69656e74223a7b0a202020202276657273696f6e223a222564",
  "capture_start": "0029a50b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfefc`](#insn-00acfefc)

~~~json
{
  "source": "00acfefc",
  "target": "0029a50b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a50b",
  "offset": 0,
  "size": 149,
  "datatype": "string",
  "bytes": "7b0a202022636c69656e74223a7b0a202020202276657273696f6e223a222564",
  "capture_start": "0029a50b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acfefc`](#insn-00acfefc)

~~~json
{
  "source": "00acfefc",
  "target": "0029a51b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029a50b",
  "offset": 16,
  "size": 149,
  "datatype": "string",
  "bytes": "7b0a202022636c69656e74223a7b0a202020202276657273696f6e223a222564",
  "capture_start": "0029a50b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00acff08`](#insn-00acff08)

~~~json
{
  "source": "00acff08",
  "target": "00728090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff10`](#insn-00acff10)

~~~json
{
  "source": "00acff10",
  "target": "00574744",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff18`](#insn-00acff18)

~~~json
{
  "source": "00acff18",
  "target": "00574fec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff20`](#insn-00acff20)

~~~json
{
  "source": "00acff20",
  "target": "0057474c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff44`](#insn-00acff44)

~~~json
{
  "source": "00acff44",
  "target": "00ad05f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff50`](#insn-00acff50)

~~~json
{
  "source": "00acff50",
  "target": "00574730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff60`](#insn-00acff60)

~~~json
{
  "source": "00acff60",
  "target": "0053d580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff64`](#insn-00acff64)

~~~json
{
  "source": "00acff64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff68`](#insn-00acff68)

~~~json
{
  "source": "00acff68",
  "target": "00acff7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff74`](#insn-00acff74)

~~~json
{
  "source": "00acff74",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acff78`](#insn-00acff78)

~~~json
{
  "source": "00acff78",
  "target": "00acffd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff7c`](#insn-00acff7c)

~~~json
{
  "source": "00acff7c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff80`](#insn-00acff80)

~~~json
{
  "source": "00acff80",
  "target": "00acfff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff84`](#insn-00acff84)

~~~json
{
  "source": "00acff84",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff88`](#insn-00acff88)

~~~json
{
  "source": "00acff88",
  "target": "00ad0004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff8c`](#insn-00acff8c)

~~~json
{
  "source": "00acff8c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff90`](#insn-00acff90)

~~~json
{
  "source": "00acff90",
  "target": "00ad0014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff94`](#insn-00acff94)

~~~json
{
  "source": "00acff94",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff98`](#insn-00acff98)

~~~json
{
  "source": "00acff98",
  "target": "00ad0024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acff9c`](#insn-00acff9c)

~~~json
{
  "source": "00acff9c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffa0`](#insn-00acffa0)

~~~json
{
  "source": "00acffa0",
  "target": "00ad0034",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffa4`](#insn-00acffa4)

~~~json
{
  "source": "00acffa4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffa8`](#insn-00acffa8)

~~~json
{
  "source": "00acffa8",
  "target": "00acffb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffac`](#insn-00acffac)

~~~json
{
  "source": "00acffac",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffb0`](#insn-00acffb0)

~~~json
{
  "source": "00acffb0",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acffb8`](#insn-00acffb8)

~~~json
{
  "source": "00acffb8",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffc0`](#insn-00acffc0)

~~~json
{
  "source": "00acffc0",
  "target": "00ad00ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffc4`](#insn-00acffc4)

~~~json
{
  "source": "00acffc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffc8`](#insn-00acffc8)

~~~json
{
  "source": "00acffc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acffe8`](#insn-00acffe8)

~~~json
{
  "source": "00acffe8",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acffec`](#insn-00acffec)

~~~json
{
  "source": "00acffec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfff0`](#insn-00acfff0)

~~~json
{
  "source": "00acfff0",
  "target": "00acff84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfff4`](#insn-00acfff4)

~~~json
{
  "source": "00acfff4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acfff8`](#insn-00acfff8)

~~~json
{
  "source": "00acfff8",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acfffc`](#insn-00acfffc)

~~~json
{
  "source": "00acfffc",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0000`](#insn-00ad0000)

~~~json
{
  "source": "00ad0000",
  "target": "00acff8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0004`](#insn-00ad0004)

~~~json
{
  "source": "00ad0004",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0008`](#insn-00ad0008)

~~~json
{
  "source": "00ad0008",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad000c`](#insn-00ad000c)

~~~json
{
  "source": "00ad000c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0010`](#insn-00ad0010)

~~~json
{
  "source": "00ad0010",
  "target": "00acff94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0014`](#insn-00ad0014)

~~~json
{
  "source": "00ad0014",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0018`](#insn-00ad0018)

~~~json
{
  "source": "00ad0018",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad001c`](#insn-00ad001c)

~~~json
{
  "source": "00ad001c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0020`](#insn-00ad0020)

~~~json
{
  "source": "00ad0020",
  "target": "00acff9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0024`](#insn-00ad0024)

~~~json
{
  "source": "00ad0024",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0028`](#insn-00ad0028)

~~~json
{
  "source": "00ad0028",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad002c`](#insn-00ad002c)

~~~json
{
  "source": "00ad002c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0030`](#insn-00ad0030)

~~~json
{
  "source": "00ad0030",
  "target": "00acffa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0034`](#insn-00ad0034)

~~~json
{
  "source": "00ad0034",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0038`](#insn-00ad0038)

~~~json
{
  "source": "00ad0038",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad003c`](#insn-00ad003c)

~~~json
{
  "source": "00ad003c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0040`](#insn-00ad0040)

~~~json
{
  "source": "00ad0040",
  "target": "00acffac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad0044`](#insn-00ad0044)

~~~json
{
  "source": "00ad0044",
  "target": "00acffb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad00ac`](#insn-00ad00ac)

~~~json
{
  "source": "00ad00ac",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
