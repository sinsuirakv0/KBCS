# 004fabbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004fa89c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fa/004fa89c.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0010.md#compare-aeb42146da5509d70a1fdcd42f06f139)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004fabbc",
  "name": "_ZN5Botan12Lookup_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0b0f7754d808756e19a9c7551d0ca09f83df5a85e44fd0e086d0f950451006f9",
  "source_text_sha256": "0b0f7754d808756e19a9c7551d0ca09f83df5a85e44fd0e086d0f950451006f9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004fabbc",
        "004fada7"
      ],
      [
        "004fae14",
        "004fae17"
      ]
    ],
    "bytes_sha256": "97f6eb4498cb31e3c5792d6dd94b2c752ef369dca39424459b413f99483761b0",
    "instruction_count": 124,
    "instruction_bytes": 496,
    "body_bytes": 496,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c59df0](../00c59/00c59df0.md)

## 呼び出し先

- [0043be80](../0043b/0043be80.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c59010](../00c59/00c59010.md)
- [00c59020](../00c59/00c59020.md)
- [00c59150](../00c59/00c59150.md)

## 関連文字列（未確認候補）

~~~text
" for provider "
"Unavailable "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3844 bytes

~~~c

void _ZN5Botan12Lookup_ErrorC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_
               (long *param_1,undefined8 param_2,byte *param_3,byte *param_4)

{
  long lVar1;
  void *pvVar2;
  undefined4 uVar3;
  byte bVar4;
  long lVar5;
  undefined *puVar6;
  ulong *puVar7;
  byte *pbVar8;
  ulong uVar9;
  void *pvVar10;
  void *pvVar11;
  undefined2 local_b0;
  void *local_a8;
  void *local_a0;
  byte local_98 [16];
  void *local_88;
  ulong local_80;
  ulong uStack_78;
  void *local_70;
  ulong local_60;
  ulong uStack_58;
  void *local_50;
  undefined4 local_40;
  undefined3 uStack_3c;
  long local_38;
  
  lVar5 = tpidr_el0;
  local_38 = *(long *)(lVar5 + 0x28);
  _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
            (local_98,"Unavailable ");
  puVar7 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
                              (local_98,&DAT_002a0fba);
  local_70 = (void *)puVar7[2];
  uStack_78 = puVar7[1];
  local_80 = *puVar7;
  puVar7[1] = 0;
  puVar7[2] = 0;
  *puVar7 = 0;
  uVar9 = *(ulong *)(param_3 + 8);
  pbVar8 = *(byte **)(param_3 + 0x10);
  if ((*param_3 & 1) == 0) {
    pbVar8 = param_3 + 1;
    uVar9 = (ulong)(*param_3 >> 1);
  }
  puVar7 = (ulong *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                              (&local_80,pbVar8,uVar9);
  local_50 = (void *)puVar7[2];
  uStack_58 = puVar7[1];
  local_60 = *puVar7;
  puVar7[1] = 0;
  puVar7[2] = 0;
  *puVar7 = 0;
  pvVar10 = *(void **)(param_4 + 8);
  pvVar11 = (void *)(ulong)(*param_4 >> 1);
  pvVar2 = pvVar11;
  if ((*param_4 & 1) != 0) {
    pvVar2 = pvVar10;
  }
  if (pvVar2 == (void *)0x0) {
    local_b0 = 0;
    uVar9 = 0;
  }
  else {
    _ZNSt6__ndk1plIcNS_11char_traitsIcEENS_9allocatorIcEEEENS_12basic_stringIT_T0_T1_EEPKS6_RKS9_
              (&local_b0," for provider ",param_4);
    uVar9 = (ulong)(byte)local_b0;
    pvVar10 = local_a8;
    pvVar11 = local_a0;
  }
  if ((uVar9 & 1) == 0) {
    pvVar11 = (void *)((long)&local_b0 + 1);
    pvVar10 = (void *)(uVar9 >> 1);
  }
  pbVar8 = (byte *)_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKcm
                             (&local_60,pvVar11,pvVar10);
  uVar3 = *(undefined4 *)(pbVar8 + 4);
  lVar1 = *(long *)(pbVar8 + 8);
  pvVar2 = *(void **)(pbVar8 + 0x10);
  pbVar8[0x10] = 0;
  puVar6 = PTR__ZTVN5Botan9ExceptionE_00c9be70;
  pbVar8[0x11] = 0;
  pbVar8[0x12] = 0;
  pbVar8[0x13] = 0;
  pbVar8[0x14] = 0;
  pbVar8[0x15] = 0;
  pbVar8[0x16] = 0;
  pbVar8[0x17] = 0;
  local_40._0_3_ = (undefined3)*(undefined4 *)(pbVar8 + 1);
  local_40._3_1_ = (undefined1)uVar3;
  uStack_3c = (undefined3)((uint)uVar3 >> 8);
  bVar4 = *pbVar8;
  pbVar8[0] = 0;
  pbVar8[1] = 0;
  pbVar8[2] = 0;
  pbVar8[3] = 0;
  pbVar8[4] = 0;
  pbVar8[5] = 0;
  pbVar8[6] = 0;
  pbVar8[7] = 0;
  pbVar8[8] = 0;
  pbVar8[9] = 0;
  pbVar8[10] = 0;
  pbVar8[0xb] = 0;
  pbVar8[0xc] = 0;
  pbVar8[0xd] = 0;
  pbVar8[0xe] = 0;
  pbVar8[0xf] = 0;
  *param_1 = (long)(puVar6 + 0x10);
  if ((bVar4 & 1) == 0) {
    *(byte *)(param_1 + 1) = bVar4;
    param_1[2] = lVar1;
    param_1[3] = (long)pvVar2;
    *(undefined4 *)((long)param_1 + 9) = local_40;
    *(undefined4 *)((long)param_1 + 0xc) = uVar3;
  }
  else {
    FUN_0043be80(param_1 + 1,pvVar2);
    _ZdlPv(pvVar2);
  }
  if ((local_b0 & 1) != 0) {
    _ZdlPv(local_a0);
  }
  if ((local_60 & 1) != 0) {
    _ZdlPv(local_50);
  }
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  if ((local_98[0] & 1) != 0) {
    _ZdlPv(local_88);
  }
  *param_1 = (long)(PTR__ZTVN5Botan12Lookup_ErrorE_00c9c090 + 0x10);
  if (*(long *)(lVar5 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004fabbc"></a> `004fabbc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-004fabc0"></a> `004fabc0` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004fabc4"></a> `004fabc4` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004fabc8"></a> `004fabc8` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004fabcc"></a> `004fabcc` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-004fabd0"></a> `004fabd0` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004fabd4"></a> `004fabd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004fabd8"></a> `004fabd8` | `20 ee ff b0` | adrp x0,0x2bf000 | `FALL_THROUGH`
<a id="insn-004fabdc"></a> `004fabdc` | `00 84 3a 91` | add x0,x0,#0xea1 | `FALL_THROUGH`
<a id="insn-004fabe0"></a> `004fabe0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004fabe4"></a> `004fabe4` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-004fabe8"></a> `004fabe8` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-004fabec"></a> `004fabec` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004fabf0"></a> `004fabf0` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-004fabf4"></a> `004fabf4` | `57 79 1d 94` | bl 0x00c59150 | `UNCONDITIONAL_CALL`
<a id="insn-004fabf8"></a> `004fabf8` | `21 ed ff d0` | adrp x1,0x2a0000 | `FALL_THROUGH`
<a id="insn-004fabfc"></a> `004fabfc` | `21 e8 3e 91` | add x1,x1,#0xfba | `FALL_THROUGH`
<a id="insn-004fac00"></a> `004fac00` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-004fac04"></a> `004fac04` | `03 79 1d 94` | bl 0x00c59010 | `UNCONDITIONAL_CALL`
<a id="insn-004fac08"></a> `004fac08` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004fac0c"></a> `004fac0c` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-004fac10"></a> `004fac10` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fac14"></a> `004fac14` | `e0 0f 80 3d` | str q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fac18"></a> `004fac18` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004fac1c"></a> `004fac1c` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-004fac20"></a> `004fac20` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-004fac24"></a> `004fac24` | `aa a6 40 a9` | ldp x10,x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-004fac28"></a> `004fac28` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fac2c"></a> `004fac2c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fac30"></a> `004fac30` | `21 15 95 9a` | csinc x1,x9,x21,ne | `FALL_THROUGH`
<a id="insn-004fac34"></a> `004fac34` | `62 01 8a 9a` | csel x2,x11,x10,eq | `FALL_THROUGH`
<a id="insn-004fac38"></a> `004fac38` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004fac3c"></a> `004fac3c` | `f9 78 1d 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-004fac40"></a> `004fac40` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004fac44"></a> `004fac44` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-004fac48"></a> `004fac48` | `a8 03 1e f8` | stur x8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004fac4c"></a> `004fac4c` | `a0 03 9d 3c` | stur q0,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004fac50"></a> `004fac50` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004fac54"></a> `004fac54` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-004fac58"></a> `004fac58` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-004fac5c"></a> `004fac5c` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-004fac60"></a> `004fac60` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-004fac64"></a> `004fac64` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fac68"></a> `004fac68` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-004fac6c"></a> `004fac6c` | `28 01 00 b4` | cbz x8,0x004fac90 | `CONDITIONAL_JUMP`
<a id="insn-004fac70"></a> `004fac70` | `80 ed ff d0` | adrp x0,0x2ac000 | `FALL_THROUGH`
<a id="insn-004fac74"></a> `004fac74` | `00 c4 22 91` | add x0,x0,#0x8b1 | `FALL_THROUGH`
<a id="insn-004fac78"></a> `004fac78` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-004fac7c"></a> `004fac7c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004fac80"></a> `004fac80` | `34 79 1d 94` | bl 0x00c59150 | `UNCONDITIONAL_CALL`
<a id="insn-004fac84"></a> `004fac84` | `e9 ab 40 a9` | ldp x9,x10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fac88"></a> `004fac88` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004fac8c"></a> `004fac8c` | `02 00 00 14` | b 0x004fac94 | `UNCONDITIONAL_JUMP`
<a id="insn-004fac90"></a> `004fac90` | `ff 03 00 79` | strh wzr,[sp] | `FALL_THROUGH`
<a id="insn-004fac94"></a> `004fac94` | `0b 7d 01 53` | lsr w11,w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fac98"></a> `004fac98` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-004fac9c"></a> `004fac9c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-004faca0"></a> `004faca0` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-004faca4"></a> `004faca4` | `62 01 89 9a` | csel x2,x11,x9,eq | `FALL_THROUGH`
<a id="insn-004faca8"></a> `004faca8` | `a0 c3 00 d1` | sub x0,x29,#0x30 | `FALL_THROUGH`
<a id="insn-004facac"></a> `004facac` | `dd 78 1d 94` | bl 0x00c59020 | `UNCONDITIONAL_CALL`
<a id="insn-004facb0"></a> `004facb0` | `08 10 40 b8` | ldur w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-004facb4"></a> `004facb4` | `09 04 40 b9` | ldr w9,[x0, #0x4] | `FALL_THROUGH`
<a id="insn-004facb8"></a> `004facb8` | `02 d4 40 a9` | ldp x2,x21,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004facbc"></a> `004facbc` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004facc0"></a> `004facc0` | `a8 03 1f b8` | stur w8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004facc4"></a> `004facc4` | `08 3d 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-004facc8"></a> `004facc8` | `a9 33 1f b8` | stur w9,[x29, #-0xd] | `FALL_THROUGH`
<a id="insn-004faccc"></a> `004faccc` | `08 39 47 f9` | ldr x8,[x8, #0xe70] | `FALL_THROUGH`
<a id="insn-004facd0"></a> `004facd0` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-004facd4"></a> `004facd4` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-004facd8"></a> `004facd8` | `0a 41 00 91` | add x10,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004facdc"></a> `004facdc` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004face0"></a> `004face0` | `0a 85 00 f8` | str x10,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-004face4"></a> `004face4` | `09 04 00 37` | tbnz w9,#0x0,0x004fad64 | `CONDITIONAL_JUMP`
<a id="insn-004face8"></a> `004face8` | `a8 03 5f b8` | ldur w8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004facec"></a> `004facec` | `69 22 00 39` | strb w9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-004facf0"></a> `004facf0` | `a9 33 5f b8` | ldur w9,[x29, #-0xd] | `FALL_THROUGH`
<a id="insn-004facf4"></a> `004facf4` | `62 56 01 a9` | stp x2,x21,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004facf8"></a> `004facf8` | `68 92 00 b8` | stur w8,[x19, #0x9] | `FALL_THROUGH`
<a id="insn-004facfc"></a> `004facfc` | `69 0e 00 b9` | str w9,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-004fad00"></a> `004fad00` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004fad04"></a> `004fad04` | `68 00 00 36` | tbz w8,#0x0,0x004fad10 | `CONDITIONAL_JUMP`
<a id="insn-004fad08"></a> `004fad08` | `e0 0b 40 f9` | ldr x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004fad0c"></a> `004fad0c` | `91 78 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004fad10"></a> `004fad10` | `a8 03 5d 38` | ldurb w8,[x29, #-0x30] | `FALL_THROUGH`
<a id="insn-004fad14"></a> `004fad14` | `88 03 00 37` | tbnz w8,#0x0,0x004fad84 | `CONDITIONAL_JUMP`
<a id="insn-004fad18"></a> `004fad18` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fad1c"></a> `004fad1c` | `c8 03 00 37` | tbnz w8,#0x0,0x004fad94 | `CONDITIONAL_JUMP`
<a id="insn-004fad20"></a> `004fad20` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004fad24"></a> `004fad24` | `68 00 00 36` | tbz w8,#0x0,0x004fad30 | `CONDITIONAL_JUMP`
<a id="insn-004fad28"></a> `004fad28` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004fad2c"></a> `004fad2c` | `89 78 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004fad30"></a> `004fad30` | `08 3d 00 d0` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-004fad34"></a> `004fad34` | `08 49 40 f9` | ldr x8,[x8, #0x90] | `FALL_THROUGH`
<a id="insn-004fad38"></a> `004fad38` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-004fad3c"></a> `004fad3c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-004fad40"></a> `004fad40` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004fad44"></a> `004fad44` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004fad48"></a> `004fad48` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fad4c"></a> `004fad4c` | `41 06 00 54` | b.ne 0x004fae14 | `CONDITIONAL_JUMP`
<a id="insn-004fad50"></a> `004fad50` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004fad54"></a> `004fad54` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004fad58"></a> `004fad58` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004fad5c"></a> `004fad5c` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-004fad60"></a> `004fad60` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004fad64"></a> `004fad64` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-004fad68"></a> `004fad68` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004fad6c"></a> `004fad6c` | `45 04 fd 97` | bl 0x0043be80 | `UNCONDITIONAL_CALL`
<a id="insn-004fad70"></a> `004fad70` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004fad74"></a> `004fad74` | `77 78 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004fad78"></a> `004fad78` | `e8 03 40 39` | ldrb w8,[sp] | `FALL_THROUGH`
<a id="insn-004fad7c"></a> `004fad7c` | `68 fc 07 37` | tbnz w8,#0x0,0x004fad08 | `CONDITIONAL_JUMP`
<a id="insn-004fad80"></a> `004fad80` | `e4 ff ff 17` | b 0x004fad10 | `UNCONDITIONAL_JUMP`
<a id="insn-004fad84"></a> `004fad84` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004fad88"></a> `004fad88` | `72 78 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004fad8c"></a> `004fad8c` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fad90"></a> `004fad90` | `88 fc 07 36` | tbz w8,#0x0,0x004fad20 | `CONDITIONAL_JUMP`
<a id="insn-004fad94"></a> `004fad94` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004fad98"></a> `004fad98` | `6e 78 1d 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-004fad9c"></a> `004fad9c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004fada0"></a> `004fada0` | `48 fc 07 37` | tbnz w8,#0x0,0x004fad28 | `CONDITIONAL_JUMP`
<a id="insn-004fada4"></a> `004fada4` | `e3 ff ff 17` | b 0x004fad30 | `UNCONDITIONAL_JUMP`
<a id="insn-004fae14"></a> `004fae14` | `5b 78 1d 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004fabbc`](#insn-004fabbc) 範囲 `[['004fabbc', '004fac6f']]`
  - `CONDITIONAL_JUMP` [`004fac6c`](#insn-004fac6c) → [`004fac90`](#insn-004fac90)
  - `FALL_THROUGH` [`004fac6c`](#insn-004fac6c) → [`004fac70`](#insn-004fac70)
- ブロック [`004fac70`](#insn-004fac70) 範囲 `[['004fac70', '004fac8f']]`
  - `UNCONDITIONAL_JUMP` [`004fac8c`](#insn-004fac8c) → [`004fac94`](#insn-004fac94)
- ブロック [`004fac90`](#insn-004fac90) 範囲 `[['004fac90', '004fac93']]`
  - `FALL_THROUGH` [`004fac90`](#insn-004fac90) → [`004fac94`](#insn-004fac94)
- ブロック [`004fac94`](#insn-004fac94) 範囲 `[['004fac94', '004face7']]`
  - `CONDITIONAL_JUMP` [`004face4`](#insn-004face4) → [`004fad64`](#insn-004fad64)
  - `FALL_THROUGH` [`004face4`](#insn-004face4) → [`004face8`](#insn-004face8)
- ブロック [`004face8`](#insn-004face8) 範囲 `[['004face8', '004fad07']]`
  - `CONDITIONAL_JUMP` [`004fad04`](#insn-004fad04) → [`004fad10`](#insn-004fad10)
  - `FALL_THROUGH` [`004fad04`](#insn-004fad04) → [`004fad08`](#insn-004fad08)
- ブロック [`004fad08`](#insn-004fad08) 範囲 `[['004fad08', '004fad0f']]`
  - `FALL_THROUGH` [`004fad0c`](#insn-004fad0c) → [`004fad10`](#insn-004fad10)
- ブロック [`004fad10`](#insn-004fad10) 範囲 `[['004fad10', '004fad17']]`
  - `CONDITIONAL_JUMP` [`004fad14`](#insn-004fad14) → [`004fad84`](#insn-004fad84)
  - `FALL_THROUGH` [`004fad14`](#insn-004fad14) → [`004fad18`](#insn-004fad18)
- ブロック [`004fad18`](#insn-004fad18) 範囲 `[['004fad18', '004fad1f']]`
  - `CONDITIONAL_JUMP` [`004fad1c`](#insn-004fad1c) → [`004fad94`](#insn-004fad94)
  - `FALL_THROUGH` [`004fad1c`](#insn-004fad1c) → [`004fad20`](#insn-004fad20)
- ブロック [`004fad20`](#insn-004fad20) 範囲 `[['004fad20', '004fad27']]`
  - `CONDITIONAL_JUMP` [`004fad24`](#insn-004fad24) → [`004fad30`](#insn-004fad30)
  - `FALL_THROUGH` [`004fad24`](#insn-004fad24) → [`004fad28`](#insn-004fad28)
- ブロック [`004fad28`](#insn-004fad28) 範囲 `[['004fad28', '004fad2f']]`
  - `FALL_THROUGH` [`004fad2c`](#insn-004fad2c) → [`004fad30`](#insn-004fad30)
- ブロック [`004fad30`](#insn-004fad30) 範囲 `[['004fad30', '004fad4f']]`
  - `CONDITIONAL_JUMP` [`004fad4c`](#insn-004fad4c) → [`004fae14`](#insn-004fae14)
  - `FALL_THROUGH` [`004fad4c`](#insn-004fad4c) → [`004fad50`](#insn-004fad50)
- ブロック [`004fad50`](#insn-004fad50) 範囲 `[['004fad50', '004fad63']]`
- ブロック [`004fad64`](#insn-004fad64) 範囲 `[['004fad64', '004fad7f']]`
  - `CONDITIONAL_JUMP` [`004fad7c`](#insn-004fad7c) → [`004fad08`](#insn-004fad08)
  - `FALL_THROUGH` [`004fad7c`](#insn-004fad7c) → [`004fad80`](#insn-004fad80)
- ブロック [`004fad80`](#insn-004fad80) 範囲 `[['004fad80', '004fad83']]`
  - `UNCONDITIONAL_JUMP` [`004fad80`](#insn-004fad80) → [`004fad10`](#insn-004fad10)
- ブロック [`004fad84`](#insn-004fad84) 範囲 `[['004fad84', '004fad93']]`
  - `CONDITIONAL_JUMP` [`004fad90`](#insn-004fad90) → [`004fad20`](#insn-004fad20)
  - `FALL_THROUGH` [`004fad90`](#insn-004fad90) → [`004fad94`](#insn-004fad94)
- ブロック [`004fad94`](#insn-004fad94) 範囲 `[['004fad94', '004fada3']]`
  - `CONDITIONAL_JUMP` [`004fada0`](#insn-004fada0) → [`004fad28`](#insn-004fad28)
  - `FALL_THROUGH` [`004fada0`](#insn-004fada0) → [`004fada4`](#insn-004fada4)
- ブロック [`004fada4`](#insn-004fada4) 範囲 `[['004fada4', '004fada7']]`
  - `UNCONDITIONAL_JUMP` [`004fada4`](#insn-004fada4) → [`004fad30`](#insn-004fad30)
- ブロック [`004fae14`](#insn-004fae14) 範囲 `[['004fae14', '004fae17']]`

## 命令位置別の参照

- [`004fabc0`](#insn-004fabc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fabc4`](#insn-004fabc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fabc8`](#insn-004fabc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fabdc`](#insn-004fabdc) → `002bfea1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004fabec`](#insn-004fabec) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fabf4`](#insn-004fabf4) → [`00c59150`](../00c59/00c59150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59150` · 推定シンボル `None` · 推定型 `None`
- [`004fabfc`](#insn-004fabfc) → `002a0fba`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fac04`](#insn-004fac04) → [`00c59010`](../00c59/00c59010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59010` · 推定シンボル `None` · 推定型 `None`
- [`004fac10`](#insn-004fac10) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fac14`](#insn-004fac14) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fac3c`](#insn-004fac3c) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`004fac48`](#insn-004fac48) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fac4c`](#insn-004fac4c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fac6c`](#insn-004fac6c) → [`004fac90`](#insn-004fac90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fac74`](#insn-004fac74) → `002ac8b1`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004fac80`](#insn-004fac80) → [`00c59150`](../00c59/00c59150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59150` · 推定シンボル `None` · 推定型 `None`
- [`004fac84`](#insn-004fac84) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fac88`](#insn-004fac88) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fac8c`](#insn-004fac8c) → [`004fac94`](#insn-004fac94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fac90`](#insn-004fac90) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004facac`](#insn-004facac) → [`00c59020`](../00c59/00c59020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59020` · 推定シンボル `None` · 推定型 `None`
- [`004facc0`](#insn-004facc0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004facc8`](#insn-004facc8) → `Stack[-0x3d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004faccc`](#insn-004faccc) → `00c9be70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004face0`](#insn-004face0) → `00c684c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`004face4`](#insn-004face4) → [`004fad64`](#insn-004fad64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004face8`](#insn-004face8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004facf0`](#insn-004facf0) → `Stack[-0x3d]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad00`](#insn-004fad00) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad04`](#insn-004fad04) → [`004fad10`](#insn-004fad10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad08`](#insn-004fad08) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad0c`](#insn-004fad0c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004fad10`](#insn-004fad10) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad14`](#insn-004fad14) → [`004fad84`](#insn-004fad84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad18`](#insn-004fad18) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad1c`](#insn-004fad1c) → [`004fad94`](#insn-004fad94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad20`](#insn-004fad20) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad24`](#insn-004fad24) → [`004fad30`](#insn-004fad30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad28`](#insn-004fad28) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad2c`](#insn-004fad2c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004fad34`](#insn-004fad34) → `00c9c090`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fad3c`](#insn-004fad3c) → `00c68518`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`004fad44`](#insn-004fad44) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad4c`](#insn-004fad4c) → [`004fae14`](#insn-004fae14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad50`](#insn-004fad50) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad54`](#insn-004fad54) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad58`](#insn-004fad58) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad6c`](#insn-004fad6c) → [`0043be80`](../0043b/0043be80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043be80` · 推定シンボル `None` · 推定型 `None`
- [`004fad74`](#insn-004fad74) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004fad78`](#insn-004fad78) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad7c`](#insn-004fad7c) → [`004fad08`](#insn-004fad08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad80`](#insn-004fad80) → [`004fad10`](#insn-004fad10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad84`](#insn-004fad84) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad88`](#insn-004fad88) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004fad8c`](#insn-004fad8c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad90`](#insn-004fad90) → [`004fad20`](#insn-004fad20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad94`](#insn-004fad94) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fad98`](#insn-004fad98) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`004fad9c`](#insn-004fad9c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fada0`](#insn-004fada0) → [`004fad28`](#insn-004fad28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fada4`](#insn-004fada4) → [`004fad30`](#insn-004fad30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fae14`](#insn-004fae14) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004fabc0`](#insn-004fabc0)

~~~json
{
  "source": "004fabc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fabc4`](#insn-004fabc4)

~~~json
{
  "source": "004fabc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fabc8`](#insn-004fabc8)

~~~json
{
  "source": "004fabc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fabdc`](#insn-004fabdc)

~~~json
{
  "source": "004fabdc",
  "target": "002bfea1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfea1",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "556e617661696c61626c652000",
  "capture_start": "002bfea1",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004fabec`](#insn-004fabec)

~~~json
{
  "source": "004fabec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fabf4`](#insn-004fabf4)

~~~json
{
  "source": "004fabf4",
  "target": "00c59150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fabfc`](#insn-004fabfc)

~~~json
{
  "source": "004fabfc",
  "target": "002a0fba",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fac04`](#insn-004fac04)

~~~json
{
  "source": "004fac04",
  "target": "00c59010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fac10`](#insn-004fac10)

~~~json
{
  "source": "004fac10",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fac14`](#insn-004fac14)

~~~json
{
  "source": "004fac14",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fac3c`](#insn-004fac3c)

~~~json
{
  "source": "004fac3c",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fac48`](#insn-004fac48)

~~~json
{
  "source": "004fac48",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fac4c`](#insn-004fac4c)

~~~json
{
  "source": "004fac4c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fac6c`](#insn-004fac6c)

~~~json
{
  "source": "004fac6c",
  "target": "004fac90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fac74`](#insn-004fac74)

~~~json
{
  "source": "004fac74",
  "target": "002ac8b1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac8b1",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "20666f722070726f76696465722000",
  "capture_start": "002ac8b1",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004fac80`](#insn-004fac80)

~~~json
{
  "source": "004fac80",
  "target": "00c59150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fac84`](#insn-004fac84)

~~~json
{
  "source": "004fac84",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fac88`](#insn-004fac88)

~~~json
{
  "source": "004fac88",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fac8c`](#insn-004fac8c)

~~~json
{
  "source": "004fac8c",
  "target": "004fac94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fac90`](#insn-004fac90)

~~~json
{
  "source": "004fac90",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004facac`](#insn-004facac)

~~~json
{
  "source": "004facac",
  "target": "00c59020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004facc0`](#insn-004facc0)

~~~json
{
  "source": "004facc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004facc8`](#insn-004facc8)

~~~json
{
  "source": "004facc8",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004faccc`](#insn-004faccc)

~~~json
{
  "source": "004faccc",
  "target": "00c9be70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9be70",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004face0`](#insn-004face0)

~~~json
{
  "source": "004face0",
  "target": "00c684c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c684b8",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004face4`](#insn-004face4)

~~~json
{
  "source": "004face4",
  "target": "004fad64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004face8`](#insn-004face8)

~~~json
{
  "source": "004face8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004facf0`](#insn-004facf0)

~~~json
{
  "source": "004facf0",
  "target": "Stack[-0x3d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad00`](#insn-004fad00)

~~~json
{
  "source": "004fad00",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad04`](#insn-004fad04)

~~~json
{
  "source": "004fad04",
  "target": "004fad10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad08`](#insn-004fad08)

~~~json
{
  "source": "004fad08",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad0c`](#insn-004fad0c)

~~~json
{
  "source": "004fad0c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad10`](#insn-004fad10)

~~~json
{
  "source": "004fad10",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad14`](#insn-004fad14)

~~~json
{
  "source": "004fad14",
  "target": "004fad84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad18`](#insn-004fad18)

~~~json
{
  "source": "004fad18",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad1c`](#insn-004fad1c)

~~~json
{
  "source": "004fad1c",
  "target": "004fad94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad20`](#insn-004fad20)

~~~json
{
  "source": "004fad20",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad24`](#insn-004fad24)

~~~json
{
  "source": "004fad24",
  "target": "004fad30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad28`](#insn-004fad28)

~~~json
{
  "source": "004fad28",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad2c`](#insn-004fad2c)

~~~json
{
  "source": "004fad2c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad34`](#insn-004fad34)

~~~json
{
  "source": "004fad34",
  "target": "00c9c090",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c090",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fad3c`](#insn-004fad3c)

~~~json
{
  "source": "004fad3c",
  "target": "00c68518",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c68508",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fad44`](#insn-004fad44)

~~~json
{
  "source": "004fad44",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad4c`](#insn-004fad4c)

~~~json
{
  "source": "004fad4c",
  "target": "004fae14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad50`](#insn-004fad50)

~~~json
{
  "source": "004fad50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad54`](#insn-004fad54)

~~~json
{
  "source": "004fad54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad58`](#insn-004fad58)

~~~json
{
  "source": "004fad58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad6c`](#insn-004fad6c)

~~~json
{
  "source": "004fad6c",
  "target": "0043be80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad74`](#insn-004fad74)

~~~json
{
  "source": "004fad74",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad78`](#insn-004fad78)

~~~json
{
  "source": "004fad78",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad7c`](#insn-004fad7c)

~~~json
{
  "source": "004fad7c",
  "target": "004fad08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad80`](#insn-004fad80)

~~~json
{
  "source": "004fad80",
  "target": "004fad10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad84`](#insn-004fad84)

~~~json
{
  "source": "004fad84",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad88`](#insn-004fad88)

~~~json
{
  "source": "004fad88",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad8c`](#insn-004fad8c)

~~~json
{
  "source": "004fad8c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad90`](#insn-004fad90)

~~~json
{
  "source": "004fad90",
  "target": "004fad20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad94`](#insn-004fad94)

~~~json
{
  "source": "004fad94",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fad98`](#insn-004fad98)

~~~json
{
  "source": "004fad98",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fad9c`](#insn-004fad9c)

~~~json
{
  "source": "004fad9c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fada0`](#insn-004fada0)

~~~json
{
  "source": "004fada0",
  "target": "004fad28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fada4`](#insn-004fada4)

~~~json
{
  "source": "004fada4",
  "target": "004fad30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fae14`](#insn-004fae14)

~~~json
{
  "source": "004fae14",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
