# 00b6adbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b6a994`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b6a/00b6a994.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0076.md#compare-790a8b8edb98e2b86b81ae4abb168585)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b6ae58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b6a/00b6ae58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0076.md#compare-f473cf416150375910f4271998793d1d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6adbc",
  "name": "_ZN8firebase10AppOptions28PopulateRequiredWithDefaultsEP7_JNIEnvP8_jobject",
  "size": 572,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "64c8523f169b6ea991e31901ef4e9cce3c2d5766440658720d5a2353ee9d7640",
  "source_text_sha256": "64c8523f169b6ea991e31901ef4e9cce3c2d5766440658720d5a2353ee9d7640",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6adbc",
        "00b6aff7"
      ]
    ],
    "bytes_sha256": "e5da6c01d90cb6530fbccc0b0dd7beed1a6768aa038c51068b7fdba096c08d16",
    "instruction_count": 143,
    "instruction_bytes": 572,
    "body_bytes": 572,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5b930](../00c5b/00c5b930.md)

## 呼び出し先

- [00879c88](../00879/00879c88.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aca0](../00c5a/00c5aca0.md)
- [00c5b0b0](../00c5b/00c5b0b0.md)
- [00c5bec0](../00c5b/00c5bec0.md)

## 関連文字列（未確認候補）

~~~text
"App ID, API key, and Project ID must be specified in App options."
"Failed to load default options when attempting to populate missing fields"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5541 bytes

~~~c

void _ZN8firebase10AppOptions28PopulateRequiredWithDefaultsEP7_JNIEnvP8_jobject(undefined1 *param_1)

{
  ulong uVar1;
  byte bVar2;
  long lVar3;
  long lVar4;
  undefined8 uVar5;
  byte *pbVar6;
  undefined8 local_110;
  undefined8 uStack_108;
  undefined8 local_100;
  undefined8 uStack_f8;
  ulong local_f0;
  long lStack_e8;
  undefined8 local_e0;
  ulong uStack_d8;
  long lStack_d0;
  undefined8 uStack_c8;
  undefined8 local_c0;
  undefined8 uStack_b8;
  undefined8 uStack_b0;
  undefined8 uStack_a8;
  undefined8 local_a0;
  undefined8 uStack_98;
  undefined8 uStack_90;
  undefined8 uStack_88;
  undefined8 local_80;
  undefined8 uStack_78;
  undefined8 uStack_70;
  undefined8 uStack_68;
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  ulong local_48;
  long local_40;
  long local_38;
  
                    /* try { // try from 00b6add0 to 00c6add7 has its CatchHandler @ 00b6ae48 */
  lVar3 = tpidr_el0;
  local_38 = *(long *)(lVar3 + 0x28);
  pbVar6 = param_1 + 0x30;
  bVar2 = *pbVar6;
  if ((bVar2 & 1) == 0) {
    if (bVar2 >> 1 == 0) goto LAB_00b6ae70;
LAB_00b6adf4:
    if ((param_1[0x18] & 1) != 0) {
                    /* catch() { ... } // from try @ 00b6ad40 with catch @ 00b6ae50 */
      if (*(long *)(param_1 + 0x20) != 0) goto LAB_00b6ae04;
      goto LAB_00b6ae70;
    }
    if ((byte)param_1[0x18] >> 1 == 0) goto LAB_00b6ae70;
LAB_00b6ae04:
    if ((param_1[0xc0] & 1) == 0) {
      if ((byte)param_1[0xc0] >> 1 == 0) goto LAB_00b6ae70;
    }
    else if (*(long *)(param_1 + 200) == 0) goto LAB_00b6ae70;
    if ((bVar2 & 1) != 0) goto LAB_00b6afa4;
LAB_00b6ae18:
    if (bVar2 >> 1 != 0) {
LAB_00b6ae20:
      if ((param_1[0x18] & 1) == 0) {
        if ((byte)param_1[0x18] >> 1 != 0) {
LAB_00b6ae30:
          if ((param_1[0xc0] & 1) == 0) {
            if ((byte)param_1[0xc0] >> 1 != 0) {
LAB_00b6afb8:
              uVar5 = 1;
              goto LAB_00b6afd0;
            }
          }
          else if (*(long *)(param_1 + 200) != 0) goto LAB_00b6afb8;
        }
      }
      else {
                    /* catch() { ... } // from try @ 00b6ad08 with catch @ 00b6ae5c
                       catch() { ... } // from try @ 00b6ae40 with catch @ 00b6ae5c */
        if (*(long *)(param_1 + 0x20) != 0) goto LAB_00b6ae30;
      }
    }
  }
  else {
                    /* catch() { ... } // from try @ 00b6add0 with catch @ 00b6ae48
                       try { // try from 00b6ae48 to 00c6ae8f has its CatchHandler @ 00b6ac9c */
    if (*(long *)(param_1 + 0x38) != 0) goto LAB_00b6adf4;
LAB_00b6ae70:
    local_40 = 0;
    uStack_58 = 0;
    local_60 = 0;
    local_48 = 0;
    local_50 = 0;
    uStack_78 = 0;
    local_80 = 0;
    uStack_68 = 0;
    uStack_70 = 0;
    uStack_98 = 0;
    local_a0 = 0;
    uStack_88 = 0;
    uStack_90 = 0;
    uStack_b8 = 0;
    local_c0 = 0;
    uStack_a8 = 0;
    uStack_b0 = 0;
    uStack_d8 = 0;
    local_e0 = 0;
    uStack_c8 = 0;
    lStack_d0 = 0;
    uStack_f8 = 0;
    local_100 = 0;
    lStack_e8 = 0;
    local_f0 = 0;
    uStack_108 = 0;
    local_110 = 0;
    lVar4 = _ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject(&local_110);
    if (lVar4 == 0) {
      _ZN8firebase8LogErrorEPKcz
                ("Failed to load default options when attempting to populate missing fields");
    }
    else {
      if ((*pbVar6 & 1) == 0) {
        if (*pbVar6 >> 1 == 0) {
LAB_00b6aecc:
          if (&local_110 != (undefined8 *)param_1) {
            uVar1 = uStack_d8;
            lVar4 = lStack_d0;
            if ((local_e0 & 1) == 0) {
              uVar1 = local_e0 >> 1 & 0x7f;
              lVar4 = (long)&local_e0 + 1;
            }
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                      (pbVar6,lVar4,uVar1);
          }
        }
      }
      else if (*(long *)(param_1 + 0x38) == 0) goto LAB_00b6aecc;
      bVar2 = param_1[0x18];
      if ((bVar2 & 1) == 0) {
        if (bVar2 >> 1 == 0) {
LAB_00b6af1c:
          if (&local_110 != (undefined8 *)param_1) {
            uVar1 = local_f0;
            lVar4 = lStack_e8;
            if ((uStack_f8 & 1) == 0) {
              uVar1 = uStack_f8 >> 1 & 0x7f;
              lVar4 = (long)&uStack_f8 + 1;
            }
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                      (param_1 + 0x18,lVar4,uVar1);
          }
        }
      }
      else if (*(long *)(param_1 + 0x20) == 0) goto LAB_00b6af1c;
      bVar2 = param_1[0xc0];
      if ((bVar2 & 1) == 0) {
        if (bVar2 >> 1 == 0) {
LAB_00b6af68:
          if (&local_110 != (undefined8 *)param_1) {
            uVar1 = local_48;
            lVar4 = local_40;
            if ((local_50 & 1) == 0) {
              uVar1 = local_50 >> 1 & 0x7f;
              lVar4 = (long)&local_50 + 1;
            }
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEPKcm
                      (param_1 + 0xc0,lVar4,uVar1);
          }
        }
      }
      else if (*(long *)(param_1 + 200) == 0) goto LAB_00b6af68;
    }
    FUN_00879c88(&local_110);
    bVar2 = *pbVar6;
    if ((bVar2 & 1) == 0) goto LAB_00b6ae18;
LAB_00b6afa4:
    if (*(long *)(param_1 + 0x38) != 0) goto LAB_00b6ae20;
  }
  _ZN8firebase8LogErrorEPKcz("App ID, API key, and Project ID must be specified in App options.");
  uVar5 = 0;
LAB_00b6afd0:
  if (*(long *)(lVar3 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar5);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6adbc"></a> `00b6adbc` | `ff 43 04 d1` | sub sp,sp,#0x110 | `FALL_THROUGH`
<a id="insn-00b6adc0"></a> `00b6adc0` | `fc 57 0e a9` | stp x28,x21,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00b6adc4"></a> `00b6adc4` | `f4 4f 0f a9` | stp x20,x19,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00b6adc8"></a> `00b6adc8` | `fd 7b 10 a9` | stp x29,x30,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b6adcc"></a> `00b6adcc` | `fd 03 04 91` | add x29,sp,#0x100 | `FALL_THROUGH`
<a id="insn-00b6add0"></a> `00b6add0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b6add4"></a> `00b6add4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b6add8"></a> `00b6add8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6addc"></a> `00b6addc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b6ade0"></a> `00b6ade0` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00b6ade4"></a> `00b6ade4` | `88 0e 43 38` | ldrb w8,[x20, #0x30]! | `FALL_THROUGH`
<a id="insn-00b6ade8"></a> `00b6ade8` | `e8 02 00 37` | tbnz w8,#0x0,0x00b6ae44 | `CONDITIONAL_JUMP`
<a id="insn-00b6adec"></a> `00b6adec` | `09 fd 41 d3` | lsr x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6adf0"></a> `00b6adf0` | `09 04 00 b4` | cbz x9,0x00b6ae70 | `CONDITIONAL_JUMP`
<a id="insn-00b6adf4"></a> `00b6adf4` | `69 62 40 39` | ldrb w9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b6adf8"></a> `00b6adf8` | `c9 02 00 37` | tbnz w9,#0x0,0x00b6ae50 | `CONDITIONAL_JUMP`
<a id="insn-00b6adfc"></a> `00b6adfc` | `29 fd 41 d3` | lsr x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b6ae00"></a> `00b6ae00` | `89 03 00 b4` | cbz x9,0x00b6ae70 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae04"></a> `00b6ae04` | `69 02 43 39` | ldrb w9,[x19, #0xc0] | `FALL_THROUGH`
<a id="insn-00b6ae08"></a> `00b6ae08` | `09 03 00 37` | tbnz w9,#0x0,0x00b6ae68 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae0c"></a> `00b6ae0c` | `29 fd 41 d3` | lsr x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b6ae10"></a> `00b6ae10` | `09 03 00 b4` | cbz x9,0x00b6ae70 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae14"></a> `00b6ae14` | `88 0c 00 37` | tbnz w8,#0x0,0x00b6afa4 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae18"></a> `00b6ae18` | `08 7d 01 53` | lsr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6ae1c"></a> `00b6ae1c` | `28 0d 00 b4` | cbz x8,0x00b6afc0 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae20"></a> `00b6ae20` | `68 62 40 39` | ldrb w8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b6ae24"></a> `00b6ae24` | `c8 01 00 37` | tbnz w8,#0x0,0x00b6ae5c | `CONDITIONAL_JUMP`
<a id="insn-00b6ae28"></a> `00b6ae28` | `08 fd 41 d3` | lsr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6ae2c"></a> `00b6ae2c` | `a8 0c 00 b4` | cbz x8,0x00b6afc0 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae30"></a> `00b6ae30` | `68 02 43 39` | ldrb w8,[x19, #0xc0] | `FALL_THROUGH`
<a id="insn-00b6ae34"></a> `00b6ae34` | `e8 0b 00 37` | tbnz w8,#0x0,0x00b6afb0 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae38"></a> `00b6ae38` | `08 fd 41 d3` | lsr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6ae3c"></a> `00b6ae3c` | `e8 0b 00 b5` | cbnz x8,0x00b6afb8 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae40"></a> `00b6ae40` | `60 00 00 14` | b 0x00b6afc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6ae44"></a> `00b6ae44` | `69 1e 40 f9` | ldr x9,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00b6ae48"></a> `00b6ae48` | `69 fd ff b5` | cbnz x9,0x00b6adf4 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae4c"></a> `00b6ae4c` | `09 00 00 14` | b 0x00b6ae70 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6ae50"></a> `00b6ae50` | `69 12 40 f9` | ldr x9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b6ae54"></a> `00b6ae54` | `89 fd ff b5` | cbnz x9,0x00b6ae04 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae58"></a> `00b6ae58` | `06 00 00 14` | b 0x00b6ae70 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6ae5c"></a> `00b6ae5c` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b6ae60"></a> `00b6ae60` | `88 fe ff b5` | cbnz x8,0x00b6ae30 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae64"></a> `00b6ae64` | `57 00 00 14` | b 0x00b6afc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6ae68"></a> `00b6ae68` | `69 66 40 f9` | ldr x9,[x19, #0xc8] | `FALL_THROUGH`
<a id="insn-00b6ae6c"></a> `00b6ae6c` | `49 fd ff b5` | cbnz x9,0x00b6ae14 | `CONDITIONAL_JUMP`
<a id="insn-00b6ae70"></a> `00b6ae70` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00b6ae74"></a> `00b6ae74` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00b6ae78"></a> `00b6ae78` | `ff 6b 00 f9` | str xzr,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00b6ae7c"></a> `00b6ae7c` | `e0 83 05 ad` | stp q0,q0,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00b6ae80"></a> `00b6ae80` | `e0 83 04 ad` | stp q0,q0,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00b6ae84"></a> `00b6ae84` | `e0 83 03 ad` | stp q0,q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00b6ae88"></a> `00b6ae88` | `e0 83 02 ad` | stp q0,q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b6ae8c"></a> `00b6ae8c` | `e0 83 01 ad` | stp q0,q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6ae90"></a> `00b6ae90` | `e0 83 00 ad` | stp q0,q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ae94"></a> `00b6ae94` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00b6ae98"></a> `00b6ae98` | `0a c4 03 94` | bl 0x00c5bec0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ae9c"></a> `00b6ae9c` | `c0 00 00 b4` | cbz x0,0x00b6aeb4 | `CONDITIONAL_JUMP`
<a id="insn-00b6aea0"></a> `00b6aea0` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00b6aea4"></a> `00b6aea4` | `08 01 00 37` | tbnz w8,#0x0,0x00b6aec4 | `CONDITIONAL_JUMP`
<a id="insn-00b6aea8"></a> `00b6aea8` | `08 fd 41 d3` | lsr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6aeac"></a> `00b6aeac` | `88 02 00 b5` | cbnz x8,0x00b6aefc | `CONDITIONAL_JUMP`
<a id="insn-00b6aeb0"></a> `00b6aeb0` | `07 00 00 14` | b 0x00b6aecc | `UNCONDITIONAL_JUMP`
<a id="insn-00b6aeb4"></a> `00b6aeb4` | `e0 b9 ff f0` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00b6aeb8"></a> `00b6aeb8` | `00 94 19 91` | add x0,x0,#0x665 | `FALL_THROUGH`
<a id="insn-00b6aebc"></a> `00b6aebc` | `79 bf 03 94` | bl 0x00c5aca0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6aec0"></a> `00b6aec0` | `35 00 00 14` | b 0x00b6af94 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6aec4"></a> `00b6aec4` | `68 1e 40 f9` | ldr x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00b6aec8"></a> `00b6aec8` | `a8 01 00 b5` | cbnz x8,0x00b6aefc | `CONDITIONAL_JUMP`
<a id="insn-00b6aecc"></a> `00b6aecc` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00b6aed0"></a> `00b6aed0` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00b6aed4"></a> `00b6aed4` | `40 01 00 54` | b.eq 0x00b6aefc | `CONDITIONAL_JUMP`
<a id="insn-00b6aed8"></a> `00b6aed8` | `e9 c3 40 39` | ldrb w9,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6aedc"></a> `00b6aedc` | `eb ab 43 a9` | ldp x11,x10,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00b6aee0"></a> `00b6aee0` | `08 c1 00 91` | add x8,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00b6aee4"></a> `00b6aee4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6aee8"></a> `00b6aee8` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b6aeec"></a> `00b6aeec` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b6aef0"></a> `00b6aef0` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00b6aef4"></a> `00b6aef4` | `82 01 8b 9a` | csel x2,x12,x11,eq | `FALL_THROUGH`
<a id="insn-00b6aef8"></a> `00b6aef8` | `6e c0 03 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6aefc"></a> `00b6aefc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6af00"></a> `00b6af00` | `08 8c 41 38` | ldrb w8,[x0, #0x18]! | `FALL_THROUGH`
<a id="insn-00b6af04"></a> `00b6af04` | `88 00 00 37` | tbnz w8,#0x0,0x00b6af14 | `CONDITIONAL_JUMP`
<a id="insn-00b6af08"></a> `00b6af08` | `08 fd 41 d3` | lsr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6af0c"></a> `00b6af0c` | `e8 01 00 b5` | cbnz x8,0x00b6af48 | `CONDITIONAL_JUMP`
<a id="insn-00b6af10"></a> `00b6af10` | `03 00 00 14` | b 0x00b6af1c | `UNCONDITIONAL_JUMP`
<a id="insn-00b6af14"></a> `00b6af14` | `68 12 40 f9` | ldr x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b6af18"></a> `00b6af18` | `88 01 00 b5` | cbnz x8,0x00b6af48 | `CONDITIONAL_JUMP`
<a id="insn-00b6af1c"></a> `00b6af1c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00b6af20"></a> `00b6af20` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00b6af24"></a> `00b6af24` | `20 01 00 54` | b.eq 0x00b6af48 | `CONDITIONAL_JUMP`
<a id="insn-00b6af28"></a> `00b6af28` | `e9 63 40 39` | ldrb w9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b6af2c"></a> `00b6af2c` | `eb 2b 42 a9` | ldp x11,x10,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b6af30"></a> `00b6af30` | `08 61 00 91` | add x8,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00b6af34"></a> `00b6af34` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b6af38"></a> `00b6af38` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b6af3c"></a> `00b6af3c` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00b6af40"></a> `00b6af40` | `82 01 8b 9a` | csel x2,x12,x11,eq | `FALL_THROUGH`
<a id="insn-00b6af44"></a> `00b6af44` | `5b c0 03 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6af48"></a> `00b6af48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6af4c"></a> `00b6af4c` | `08 0c 4c 38` | ldrb w8,[x0, #0xc0]! | `FALL_THROUGH`
<a id="insn-00b6af50"></a> `00b6af50` | `88 00 00 37` | tbnz w8,#0x0,0x00b6af60 | `CONDITIONAL_JUMP`
<a id="insn-00b6af54"></a> `00b6af54` | `08 fd 41 d3` | lsr x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b6af58"></a> `00b6af58` | `e8 01 00 b5` | cbnz x8,0x00b6af94 | `CONDITIONAL_JUMP`
<a id="insn-00b6af5c"></a> `00b6af5c` | `03 00 00 14` | b 0x00b6af68 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6af60"></a> `00b6af60` | `68 66 40 f9` | ldr x8,[x19, #0xc8] | `FALL_THROUGH`
<a id="insn-00b6af64"></a> `00b6af64` | `88 01 00 b5` | cbnz x8,0x00b6af94 | `CONDITIONAL_JUMP`
<a id="insn-00b6af68"></a> `00b6af68` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00b6af6c"></a> `00b6af6c` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00b6af70"></a> `00b6af70` | `20 01 00 54` | b.eq 0x00b6af94 | `CONDITIONAL_JUMP`
<a id="insn-00b6af74"></a> `00b6af74` | `e9 03 43 39` | ldrb w9,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00b6af78"></a> `00b6af78` | `eb ab 4c a9` | ldp x11,x10,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-00b6af7c"></a> `00b6af7c` | `08 01 03 91` | add x8,x8,#0xc0 | `FALL_THROUGH`
<a id="insn-00b6af80"></a> `00b6af80` | `2c fd 41 d3` | lsr x12,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b6af84"></a> `00b6af84` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b6af88"></a> `00b6af88` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00b6af8c"></a> `00b6af8c` | `82 01 8b 9a` | csel x2,x12,x11,eq | `FALL_THROUGH`
<a id="insn-00b6af90"></a> `00b6af90` | `48 c0 03 94` | bl 0x00c5b0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6af94"></a> `00b6af94` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00b6af98"></a> `00b6af98` | `3c 3b f4 97` | bl 0x00879c88 | `UNCONDITIONAL_CALL`
<a id="insn-00b6af9c"></a> `00b6af9c` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00b6afa0"></a> `00b6afa0` | `c8 f3 07 36` | tbz w8,#0x0,0x00b6ae18 | `CONDITIONAL_JUMP`
<a id="insn-00b6afa4"></a> `00b6afa4` | `68 1e 40 f9` | ldr x8,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00b6afa8"></a> `00b6afa8` | `c8 f3 ff b5` | cbnz x8,0x00b6ae20 | `CONDITIONAL_JUMP`
<a id="insn-00b6afac"></a> `00b6afac` | `05 00 00 14` | b 0x00b6afc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6afb0"></a> `00b6afb0` | `68 66 40 f9` | ldr x8,[x19, #0xc8] | `FALL_THROUGH`
<a id="insn-00b6afb4"></a> `00b6afb4` | `68 00 00 b4` | cbz x8,0x00b6afc0 | `CONDITIONAL_JUMP`
<a id="insn-00b6afb8"></a> `00b6afb8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b6afbc"></a> `00b6afbc` | `05 00 00 14` | b 0x00b6afd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b6afc0"></a> `00b6afc0` | `c0 b9 ff d0` | adrp x0,0x2a4000 | `FALL_THROUGH`
<a id="insn-00b6afc4"></a> `00b6afc4` | `00 24 37 91` | add x0,x0,#0xdc9 | `FALL_THROUGH`
<a id="insn-00b6afc8"></a> `00b6afc8` | `36 bf 03 94` | bl 0x00c5aca0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6afcc"></a> `00b6afcc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b6afd0"></a> `00b6afd0` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00b6afd4"></a> `00b6afd4` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00b6afd8"></a> `00b6afd8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b6afdc"></a> `00b6afdc` | `c1 00 00 54` | b.ne 0x00b6aff4 | `CONDITIONAL_JUMP`
<a id="insn-00b6afe0"></a> `00b6afe0` | `fd 7b 50 a9` | ldp x29,x30,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b6afe4"></a> `00b6afe4` | `f4 4f 4f a9` | ldp x20,x19,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00b6afe8"></a> `00b6afe8` | `fc 57 4e a9` | ldp x28,x21,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00b6afec"></a> `00b6afec` | `ff 43 04 91` | add sp,sp,#0x110 | `FALL_THROUGH`
<a id="insn-00b6aff0"></a> `00b6aff0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b6aff4"></a> `00b6aff4` | `bb b3 03 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6adbc`](#insn-00b6adbc) 範囲 `[['00b6adbc', '00b6adcf']]`
  - `FALL_THROUGH` [`00b6adcc`](#insn-00b6adcc) → [`00b6add0`](#insn-00b6add0)
- ブロック [`00b6add0`](#insn-00b6add0) 範囲 `[['00b6add0', '00b6adeb']]`
  - `CONDITIONAL_JUMP` [`00b6ade8`](#insn-00b6ade8) → [`00b6ae44`](#insn-00b6ae44)
  - `FALL_THROUGH` [`00b6ade8`](#insn-00b6ade8) → [`00b6adec`](#insn-00b6adec)
- ブロック [`00b6adec`](#insn-00b6adec) 範囲 `[['00b6adec', '00b6adf3']]`
  - `CONDITIONAL_JUMP` [`00b6adf0`](#insn-00b6adf0) → [`00b6ae70`](#insn-00b6ae70)
  - `FALL_THROUGH` [`00b6adf0`](#insn-00b6adf0) → [`00b6adf4`](#insn-00b6adf4)
- ブロック [`00b6adf4`](#insn-00b6adf4) 範囲 `[['00b6adf4', '00b6adfb']]`
  - `CONDITIONAL_JUMP` [`00b6adf8`](#insn-00b6adf8) → [`00b6ae50`](#insn-00b6ae50)
  - `FALL_THROUGH` [`00b6adf8`](#insn-00b6adf8) → [`00b6adfc`](#insn-00b6adfc)
- ブロック [`00b6adfc`](#insn-00b6adfc) 範囲 `[['00b6adfc', '00b6ae03']]`
  - `CONDITIONAL_JUMP` [`00b6ae00`](#insn-00b6ae00) → [`00b6ae70`](#insn-00b6ae70)
  - `FALL_THROUGH` [`00b6ae00`](#insn-00b6ae00) → [`00b6ae04`](#insn-00b6ae04)
- ブロック [`00b6ae04`](#insn-00b6ae04) 範囲 `[['00b6ae04', '00b6ae0b']]`
  - `CONDITIONAL_JUMP` [`00b6ae08`](#insn-00b6ae08) → [`00b6ae68`](#insn-00b6ae68)
  - `FALL_THROUGH` [`00b6ae08`](#insn-00b6ae08) → [`00b6ae0c`](#insn-00b6ae0c)
- ブロック [`00b6ae0c`](#insn-00b6ae0c) 範囲 `[['00b6ae0c', '00b6ae13']]`
  - `CONDITIONAL_JUMP` [`00b6ae10`](#insn-00b6ae10) → [`00b6ae70`](#insn-00b6ae70)
  - `FALL_THROUGH` [`00b6ae10`](#insn-00b6ae10) → [`00b6ae14`](#insn-00b6ae14)
- ブロック [`00b6ae14`](#insn-00b6ae14) 範囲 `[['00b6ae14', '00b6ae17']]`
  - `CONDITIONAL_JUMP` [`00b6ae14`](#insn-00b6ae14) → [`00b6afa4`](#insn-00b6afa4)
  - `FALL_THROUGH` [`00b6ae14`](#insn-00b6ae14) → [`00b6ae18`](#insn-00b6ae18)
- ブロック [`00b6ae18`](#insn-00b6ae18) 範囲 `[['00b6ae18', '00b6ae1f']]`
  - `CONDITIONAL_JUMP` [`00b6ae1c`](#insn-00b6ae1c) → [`00b6afc0`](#insn-00b6afc0)
  - `FALL_THROUGH` [`00b6ae1c`](#insn-00b6ae1c) → [`00b6ae20`](#insn-00b6ae20)
- ブロック [`00b6ae20`](#insn-00b6ae20) 範囲 `[['00b6ae20', '00b6ae27']]`
  - `CONDITIONAL_JUMP` [`00b6ae24`](#insn-00b6ae24) → [`00b6ae5c`](#insn-00b6ae5c)
  - `FALL_THROUGH` [`00b6ae24`](#insn-00b6ae24) → [`00b6ae28`](#insn-00b6ae28)
- ブロック [`00b6ae28`](#insn-00b6ae28) 範囲 `[['00b6ae28', '00b6ae2f']]`
  - `CONDITIONAL_JUMP` [`00b6ae2c`](#insn-00b6ae2c) → [`00b6afc0`](#insn-00b6afc0)
  - `FALL_THROUGH` [`00b6ae2c`](#insn-00b6ae2c) → [`00b6ae30`](#insn-00b6ae30)
- ブロック [`00b6ae30`](#insn-00b6ae30) 範囲 `[['00b6ae30', '00b6ae37']]`
  - `CONDITIONAL_JUMP` [`00b6ae34`](#insn-00b6ae34) → [`00b6afb0`](#insn-00b6afb0)
  - `FALL_THROUGH` [`00b6ae34`](#insn-00b6ae34) → [`00b6ae38`](#insn-00b6ae38)
- ブロック [`00b6ae38`](#insn-00b6ae38) 範囲 `[['00b6ae38', '00b6ae3f']]`
  - `CONDITIONAL_JUMP` [`00b6ae3c`](#insn-00b6ae3c) → [`00b6afb8`](#insn-00b6afb8)
  - `FALL_THROUGH` [`00b6ae3c`](#insn-00b6ae3c) → [`00b6ae40`](#insn-00b6ae40)
- ブロック [`00b6ae40`](#insn-00b6ae40) 範囲 `[['00b6ae40', '00b6ae43']]`
  - `UNCONDITIONAL_JUMP` [`00b6ae40`](#insn-00b6ae40) → [`00b6afc0`](#insn-00b6afc0)
- ブロック [`00b6ae44`](#insn-00b6ae44) 範囲 `[['00b6ae44', '00b6ae47']]`
  - `FALL_THROUGH` [`00b6ae44`](#insn-00b6ae44) → [`00b6ae48`](#insn-00b6ae48)
- ブロック [`00b6ae48`](#insn-00b6ae48) 範囲 `[['00b6ae48', '00b6ae4b']]`
  - `CONDITIONAL_JUMP` [`00b6ae48`](#insn-00b6ae48) → [`00b6adf4`](#insn-00b6adf4)
  - `FALL_THROUGH` [`00b6ae48`](#insn-00b6ae48) → [`00b6ae4c`](#insn-00b6ae4c)
- ブロック [`00b6ae4c`](#insn-00b6ae4c) 範囲 `[['00b6ae4c', '00b6ae4f']]`
  - `UNCONDITIONAL_JUMP` [`00b6ae4c`](#insn-00b6ae4c) → [`00b6ae70`](#insn-00b6ae70)
- ブロック [`00b6ae50`](#insn-00b6ae50) 範囲 `[['00b6ae50', '00b6ae57']]`
  - `CONDITIONAL_JUMP` [`00b6ae54`](#insn-00b6ae54) → [`00b6ae04`](#insn-00b6ae04)
  - `FALL_THROUGH` [`00b6ae54`](#insn-00b6ae54) → [`00b6ae58`](#insn-00b6ae58)
- ブロック [`00b6ae58`](#insn-00b6ae58) 範囲 `[['00b6ae58', '00b6ae5b']]`
  - `UNCONDITIONAL_JUMP` [`00b6ae58`](#insn-00b6ae58) → [`00b6ae70`](#insn-00b6ae70)
- ブロック [`00b6ae5c`](#insn-00b6ae5c) 範囲 `[['00b6ae5c', '00b6ae63']]`
  - `CONDITIONAL_JUMP` [`00b6ae60`](#insn-00b6ae60) → [`00b6ae30`](#insn-00b6ae30)
  - `FALL_THROUGH` [`00b6ae60`](#insn-00b6ae60) → [`00b6ae64`](#insn-00b6ae64)
- ブロック [`00b6ae64`](#insn-00b6ae64) 範囲 `[['00b6ae64', '00b6ae67']]`
  - `UNCONDITIONAL_JUMP` [`00b6ae64`](#insn-00b6ae64) → [`00b6afc0`](#insn-00b6afc0)
- ブロック [`00b6ae68`](#insn-00b6ae68) 範囲 `[['00b6ae68', '00b6ae6f']]`
  - `CONDITIONAL_JUMP` [`00b6ae6c`](#insn-00b6ae6c) → [`00b6ae14`](#insn-00b6ae14)
  - `FALL_THROUGH` [`00b6ae6c`](#insn-00b6ae6c) → [`00b6ae70`](#insn-00b6ae70)
- ブロック [`00b6ae70`](#insn-00b6ae70) 範囲 `[['00b6ae70', '00b6ae9f']]`
  - `CONDITIONAL_JUMP` [`00b6ae9c`](#insn-00b6ae9c) → [`00b6aeb4`](#insn-00b6aeb4)
  - `FALL_THROUGH` [`00b6ae9c`](#insn-00b6ae9c) → [`00b6aea0`](#insn-00b6aea0)
- ブロック [`00b6aea0`](#insn-00b6aea0) 範囲 `[['00b6aea0', '00b6aea7']]`
  - `CONDITIONAL_JUMP` [`00b6aea4`](#insn-00b6aea4) → [`00b6aec4`](#insn-00b6aec4)
  - `FALL_THROUGH` [`00b6aea4`](#insn-00b6aea4) → [`00b6aea8`](#insn-00b6aea8)
- ブロック [`00b6aea8`](#insn-00b6aea8) 範囲 `[['00b6aea8', '00b6aeaf']]`
  - `CONDITIONAL_JUMP` [`00b6aeac`](#insn-00b6aeac) → [`00b6aefc`](#insn-00b6aefc)
  - `FALL_THROUGH` [`00b6aeac`](#insn-00b6aeac) → [`00b6aeb0`](#insn-00b6aeb0)
- ブロック [`00b6aeb0`](#insn-00b6aeb0) 範囲 `[['00b6aeb0', '00b6aeb3']]`
  - `UNCONDITIONAL_JUMP` [`00b6aeb0`](#insn-00b6aeb0) → [`00b6aecc`](#insn-00b6aecc)
- ブロック [`00b6aeb4`](#insn-00b6aeb4) 範囲 `[['00b6aeb4', '00b6aec3']]`
  - `UNCONDITIONAL_JUMP` [`00b6aec0`](#insn-00b6aec0) → [`00b6af94`](#insn-00b6af94)
- ブロック [`00b6aec4`](#insn-00b6aec4) 範囲 `[['00b6aec4', '00b6aecb']]`
  - `CONDITIONAL_JUMP` [`00b6aec8`](#insn-00b6aec8) → [`00b6aefc`](#insn-00b6aefc)
  - `FALL_THROUGH` [`00b6aec8`](#insn-00b6aec8) → [`00b6aecc`](#insn-00b6aecc)
- ブロック [`00b6aecc`](#insn-00b6aecc) 範囲 `[['00b6aecc', '00b6aed7']]`
  - `CONDITIONAL_JUMP` [`00b6aed4`](#insn-00b6aed4) → [`00b6aefc`](#insn-00b6aefc)
  - `FALL_THROUGH` [`00b6aed4`](#insn-00b6aed4) → [`00b6aed8`](#insn-00b6aed8)
- ブロック [`00b6aed8`](#insn-00b6aed8) 範囲 `[['00b6aed8', '00b6aefb']]`
  - `FALL_THROUGH` [`00b6aef8`](#insn-00b6aef8) → [`00b6aefc`](#insn-00b6aefc)
- ブロック [`00b6aefc`](#insn-00b6aefc) 範囲 `[['00b6aefc', '00b6af07']]`
  - `CONDITIONAL_JUMP` [`00b6af04`](#insn-00b6af04) → [`00b6af14`](#insn-00b6af14)
  - `FALL_THROUGH` [`00b6af04`](#insn-00b6af04) → [`00b6af08`](#insn-00b6af08)
- ブロック [`00b6af08`](#insn-00b6af08) 範囲 `[['00b6af08', '00b6af0f']]`
  - `CONDITIONAL_JUMP` [`00b6af0c`](#insn-00b6af0c) → [`00b6af48`](#insn-00b6af48)
  - `FALL_THROUGH` [`00b6af0c`](#insn-00b6af0c) → [`00b6af10`](#insn-00b6af10)
- ブロック [`00b6af10`](#insn-00b6af10) 範囲 `[['00b6af10', '00b6af13']]`
  - `UNCONDITIONAL_JUMP` [`00b6af10`](#insn-00b6af10) → [`00b6af1c`](#insn-00b6af1c)
- ブロック [`00b6af14`](#insn-00b6af14) 範囲 `[['00b6af14', '00b6af1b']]`
  - `CONDITIONAL_JUMP` [`00b6af18`](#insn-00b6af18) → [`00b6af48`](#insn-00b6af48)
  - `FALL_THROUGH` [`00b6af18`](#insn-00b6af18) → [`00b6af1c`](#insn-00b6af1c)
- ブロック [`00b6af1c`](#insn-00b6af1c) 範囲 `[['00b6af1c', '00b6af27']]`
  - `CONDITIONAL_JUMP` [`00b6af24`](#insn-00b6af24) → [`00b6af48`](#insn-00b6af48)
  - `FALL_THROUGH` [`00b6af24`](#insn-00b6af24) → [`00b6af28`](#insn-00b6af28)
- ブロック [`00b6af28`](#insn-00b6af28) 範囲 `[['00b6af28', '00b6af47']]`
  - `FALL_THROUGH` [`00b6af44`](#insn-00b6af44) → [`00b6af48`](#insn-00b6af48)
- ブロック [`00b6af48`](#insn-00b6af48) 範囲 `[['00b6af48', '00b6af53']]`
  - `CONDITIONAL_JUMP` [`00b6af50`](#insn-00b6af50) → [`00b6af60`](#insn-00b6af60)
  - `FALL_THROUGH` [`00b6af50`](#insn-00b6af50) → [`00b6af54`](#insn-00b6af54)
- ブロック [`00b6af54`](#insn-00b6af54) 範囲 `[['00b6af54', '00b6af5b']]`
  - `CONDITIONAL_JUMP` [`00b6af58`](#insn-00b6af58) → [`00b6af94`](#insn-00b6af94)
  - `FALL_THROUGH` [`00b6af58`](#insn-00b6af58) → [`00b6af5c`](#insn-00b6af5c)
- ブロック [`00b6af5c`](#insn-00b6af5c) 範囲 `[['00b6af5c', '00b6af5f']]`
  - `UNCONDITIONAL_JUMP` [`00b6af5c`](#insn-00b6af5c) → [`00b6af68`](#insn-00b6af68)
- ブロック [`00b6af60`](#insn-00b6af60) 範囲 `[['00b6af60', '00b6af67']]`
  - `CONDITIONAL_JUMP` [`00b6af64`](#insn-00b6af64) → [`00b6af94`](#insn-00b6af94)
  - `FALL_THROUGH` [`00b6af64`](#insn-00b6af64) → [`00b6af68`](#insn-00b6af68)
- ブロック [`00b6af68`](#insn-00b6af68) 範囲 `[['00b6af68', '00b6af73']]`
  - `CONDITIONAL_JUMP` [`00b6af70`](#insn-00b6af70) → [`00b6af94`](#insn-00b6af94)
  - `FALL_THROUGH` [`00b6af70`](#insn-00b6af70) → [`00b6af74`](#insn-00b6af74)
- ブロック [`00b6af74`](#insn-00b6af74) 範囲 `[['00b6af74', '00b6af93']]`
  - `FALL_THROUGH` [`00b6af90`](#insn-00b6af90) → [`00b6af94`](#insn-00b6af94)
- ブロック [`00b6af94`](#insn-00b6af94) 範囲 `[['00b6af94', '00b6afa3']]`
  - `CONDITIONAL_JUMP` [`00b6afa0`](#insn-00b6afa0) → [`00b6ae18`](#insn-00b6ae18)
  - `FALL_THROUGH` [`00b6afa0`](#insn-00b6afa0) → [`00b6afa4`](#insn-00b6afa4)
- ブロック [`00b6afa4`](#insn-00b6afa4) 範囲 `[['00b6afa4', '00b6afab']]`
  - `CONDITIONAL_JUMP` [`00b6afa8`](#insn-00b6afa8) → [`00b6ae20`](#insn-00b6ae20)
  - `FALL_THROUGH` [`00b6afa8`](#insn-00b6afa8) → [`00b6afac`](#insn-00b6afac)
- ブロック [`00b6afac`](#insn-00b6afac) 範囲 `[['00b6afac', '00b6afaf']]`
  - `UNCONDITIONAL_JUMP` [`00b6afac`](#insn-00b6afac) → [`00b6afc0`](#insn-00b6afc0)
- ブロック [`00b6afb0`](#insn-00b6afb0) 範囲 `[['00b6afb0', '00b6afb7']]`
  - `CONDITIONAL_JUMP` [`00b6afb4`](#insn-00b6afb4) → [`00b6afc0`](#insn-00b6afc0)
  - `FALL_THROUGH` [`00b6afb4`](#insn-00b6afb4) → [`00b6afb8`](#insn-00b6afb8)
- ブロック [`00b6afb8`](#insn-00b6afb8) 範囲 `[['00b6afb8', '00b6afbf']]`
  - `UNCONDITIONAL_JUMP` [`00b6afbc`](#insn-00b6afbc) → [`00b6afd0`](#insn-00b6afd0)
- ブロック [`00b6afc0`](#insn-00b6afc0) 範囲 `[['00b6afc0', '00b6afcf']]`
  - `FALL_THROUGH` [`00b6afcc`](#insn-00b6afcc) → [`00b6afd0`](#insn-00b6afd0)
- ブロック [`00b6afd0`](#insn-00b6afd0) 範囲 `[['00b6afd0', '00b6afdf']]`
  - `CONDITIONAL_JUMP` [`00b6afdc`](#insn-00b6afdc) → [`00b6aff4`](#insn-00b6aff4)
  - `FALL_THROUGH` [`00b6afdc`](#insn-00b6afdc) → [`00b6afe0`](#insn-00b6afe0)
- ブロック [`00b6afe0`](#insn-00b6afe0) 範囲 `[['00b6afe0', '00b6aff3']]`
- ブロック [`00b6aff4`](#insn-00b6aff4) 範囲 `[['00b6aff4', '00b6aff7']]`

## 命令位置別の参照

- [`00b6adc0`](#insn-00b6adc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6adc4`](#insn-00b6adc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6adc8`](#insn-00b6adc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ade0`](#insn-00b6ade0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ade8`](#insn-00b6ade8) → [`00b6ae44`](#insn-00b6ae44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6adf0`](#insn-00b6adf0) → [`00b6ae70`](#insn-00b6ae70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6adf8`](#insn-00b6adf8) → [`00b6ae50`](#insn-00b6ae50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae00`](#insn-00b6ae00) → [`00b6ae70`](#insn-00b6ae70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae08`](#insn-00b6ae08) → [`00b6ae68`](#insn-00b6ae68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae10`](#insn-00b6ae10) → [`00b6ae70`](#insn-00b6ae70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae14`](#insn-00b6ae14) → [`00b6afa4`](#insn-00b6afa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae1c`](#insn-00b6ae1c) → [`00b6afc0`](#insn-00b6afc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae24`](#insn-00b6ae24) → [`00b6ae5c`](#insn-00b6ae5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae2c`](#insn-00b6ae2c) → [`00b6afc0`](#insn-00b6afc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae34`](#insn-00b6ae34) → [`00b6afb0`](#insn-00b6afb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae3c`](#insn-00b6ae3c) → [`00b6afb8`](#insn-00b6afb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae40`](#insn-00b6ae40) → [`00b6afc0`](#insn-00b6afc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae48`](#insn-00b6ae48) → [`00b6adf4`](#insn-00b6adf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae4c`](#insn-00b6ae4c) → [`00b6ae70`](#insn-00b6ae70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae54`](#insn-00b6ae54) → [`00b6ae04`](#insn-00b6ae04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae58`](#insn-00b6ae58) → [`00b6ae70`](#insn-00b6ae70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae60`](#insn-00b6ae60) → [`00b6ae30`](#insn-00b6ae30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae64`](#insn-00b6ae64) → [`00b6afc0`](#insn-00b6afc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae6c`](#insn-00b6ae6c) → [`00b6ae14`](#insn-00b6ae14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae78`](#insn-00b6ae78) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae7c`](#insn-00b6ae7c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae80`](#insn-00b6ae80) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae84`](#insn-00b6ae84) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae88`](#insn-00b6ae88) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae8c`](#insn-00b6ae8c) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae90`](#insn-00b6ae90) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae94`](#insn-00b6ae94) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae98`](#insn-00b6ae98) → [`00c5bec0`](../00c5b/00c5bec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bec0` · 推定シンボル `None` · 推定型 `None`
- [`00b6ae9c`](#insn-00b6ae9c) → [`00b6aeb4`](#insn-00b6aeb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6aea4`](#insn-00b6aea4) → [`00b6aec4`](#insn-00b6aec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6aeac`](#insn-00b6aeac) → [`00b6aefc`](#insn-00b6aefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6aeb0`](#insn-00b6aeb0) → [`00b6aecc`](#insn-00b6aecc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6aeb8`](#insn-00b6aeb8) → `002a9665`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b6aebc`](#insn-00b6aebc) → [`00c5aca0`](../00c5a/00c5aca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aca0` · 推定シンボル `None` · 推定型 `None`
- [`00b6aec0`](#insn-00b6aec0) → [`00b6af94`](#insn-00b6af94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6aec8`](#insn-00b6aec8) → [`00b6aefc`](#insn-00b6aefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6aed4`](#insn-00b6aed4) → [`00b6aefc`](#insn-00b6aefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6aed8`](#insn-00b6aed8) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6aedc`](#insn-00b6aedc) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6aef8`](#insn-00b6aef8) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00b6af04`](#insn-00b6af04) → [`00b6af14`](#insn-00b6af14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af0c`](#insn-00b6af0c) → [`00b6af48`](#insn-00b6af48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af10`](#insn-00b6af10) → [`00b6af1c`](#insn-00b6af1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af18`](#insn-00b6af18) → [`00b6af48`](#insn-00b6af48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af24`](#insn-00b6af24) → [`00b6af48`](#insn-00b6af48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af28`](#insn-00b6af28) → `Stack[-0xf8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af2c`](#insn-00b6af2c) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af44`](#insn-00b6af44) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00b6af50`](#insn-00b6af50) → [`00b6af60`](#insn-00b6af60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af58`](#insn-00b6af58) → [`00b6af94`](#insn-00b6af94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af5c`](#insn-00b6af5c) → [`00b6af68`](#insn-00b6af68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af64`](#insn-00b6af64) → [`00b6af94`](#insn-00b6af94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af70`](#insn-00b6af70) → [`00b6af94`](#insn-00b6af94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af74`](#insn-00b6af74) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af78`](#insn-00b6af78) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6af90`](#insn-00b6af90) → [`00c5b0b0`](../00c5b/00c5b0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0b0` · 推定シンボル `None` · 推定型 `None`
- [`00b6af98`](#insn-00b6af98) → [`00879c88`](../00879/00879c88.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00879c88` · 推定シンボル `None` · 推定型 `None`
- [`00b6afa0`](#insn-00b6afa0) → [`00b6ae18`](#insn-00b6ae18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6afa8`](#insn-00b6afa8) → [`00b6ae20`](#insn-00b6ae20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6afac`](#insn-00b6afac) → [`00b6afc0`](#insn-00b6afc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6afb4`](#insn-00b6afb4) → [`00b6afc0`](#insn-00b6afc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6afbc`](#insn-00b6afbc) → [`00b6afd0`](#insn-00b6afd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6afc4`](#insn-00b6afc4) → `002a4dc9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b6afc8`](#insn-00b6afc8) → [`00c5aca0`](../00c5a/00c5aca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aca0` · 推定シンボル `None` · 推定型 `None`
- [`00b6afd4`](#insn-00b6afd4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6afdc`](#insn-00b6afdc) → [`00b6aff4`](#insn-00b6aff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6afe0`](#insn-00b6afe0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6afe4`](#insn-00b6afe4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6afe8`](#insn-00b6afe8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6aff4`](#insn-00b6aff4) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6adc0`](#insn-00b6adc0)

~~~json
{
  "source": "00b6adc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6adc4`](#insn-00b6adc4)

~~~json
{
  "source": "00b6adc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6adc8`](#insn-00b6adc8)

~~~json
{
  "source": "00b6adc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ade0`](#insn-00b6ade0)

~~~json
{
  "source": "00b6ade0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ade8`](#insn-00b6ade8)

~~~json
{
  "source": "00b6ade8",
  "target": "00b6ae44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6adf0`](#insn-00b6adf0)

~~~json
{
  "source": "00b6adf0",
  "target": "00b6ae70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6adf8`](#insn-00b6adf8)

~~~json
{
  "source": "00b6adf8",
  "target": "00b6ae50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae00`](#insn-00b6ae00)

~~~json
{
  "source": "00b6ae00",
  "target": "00b6ae70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae08`](#insn-00b6ae08)

~~~json
{
  "source": "00b6ae08",
  "target": "00b6ae68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae10`](#insn-00b6ae10)

~~~json
{
  "source": "00b6ae10",
  "target": "00b6ae70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae14`](#insn-00b6ae14)

~~~json
{
  "source": "00b6ae14",
  "target": "00b6afa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae1c`](#insn-00b6ae1c)

~~~json
{
  "source": "00b6ae1c",
  "target": "00b6afc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae24`](#insn-00b6ae24)

~~~json
{
  "source": "00b6ae24",
  "target": "00b6ae5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae2c`](#insn-00b6ae2c)

~~~json
{
  "source": "00b6ae2c",
  "target": "00b6afc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae34`](#insn-00b6ae34)

~~~json
{
  "source": "00b6ae34",
  "target": "00b6afb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae3c`](#insn-00b6ae3c)

~~~json
{
  "source": "00b6ae3c",
  "target": "00b6afb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae40`](#insn-00b6ae40)

~~~json
{
  "source": "00b6ae40",
  "target": "00b6afc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae48`](#insn-00b6ae48)

~~~json
{
  "source": "00b6ae48",
  "target": "00b6adf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae4c`](#insn-00b6ae4c)

~~~json
{
  "source": "00b6ae4c",
  "target": "00b6ae70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae54`](#insn-00b6ae54)

~~~json
{
  "source": "00b6ae54",
  "target": "00b6ae04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae58`](#insn-00b6ae58)

~~~json
{
  "source": "00b6ae58",
  "target": "00b6ae70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae60`](#insn-00b6ae60)

~~~json
{
  "source": "00b6ae60",
  "target": "00b6ae30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae64`](#insn-00b6ae64)

~~~json
{
  "source": "00b6ae64",
  "target": "00b6afc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae6c`](#insn-00b6ae6c)

~~~json
{
  "source": "00b6ae6c",
  "target": "00b6ae14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae78`](#insn-00b6ae78)

~~~json
{
  "source": "00b6ae78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae7c`](#insn-00b6ae7c)

~~~json
{
  "source": "00b6ae7c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae80`](#insn-00b6ae80)

~~~json
{
  "source": "00b6ae80",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae84`](#insn-00b6ae84)

~~~json
{
  "source": "00b6ae84",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae88`](#insn-00b6ae88)

~~~json
{
  "source": "00b6ae88",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae8c`](#insn-00b6ae8c)

~~~json
{
  "source": "00b6ae8c",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae90`](#insn-00b6ae90)

~~~json
{
  "source": "00b6ae90",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae94`](#insn-00b6ae94)

~~~json
{
  "source": "00b6ae94",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ae98`](#insn-00b6ae98)

~~~json
{
  "source": "00b6ae98",
  "target": "00c5bec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ae9c`](#insn-00b6ae9c)

~~~json
{
  "source": "00b6ae9c",
  "target": "00b6aeb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6aea4`](#insn-00b6aea4)

~~~json
{
  "source": "00b6aea4",
  "target": "00b6aec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6aeac`](#insn-00b6aeac)

~~~json
{
  "source": "00b6aeac",
  "target": "00b6aefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6aeb0`](#insn-00b6aeb0)

~~~json
{
  "source": "00b6aeb0",
  "target": "00b6aecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6aeb8`](#insn-00b6aeb8)

~~~json
{
  "source": "00b6aeb8",
  "target": "002a9665",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9665",
  "offset": 0,
  "size": 74,
  "datatype": "string",
  "bytes": "4661696c656420746f206c6f61642064656661756c74206f7074696f6e732077",
  "capture_start": "002a9665",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b6aebc`](#insn-00b6aebc)

~~~json
{
  "source": "00b6aebc",
  "target": "00c5aca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6aec0`](#insn-00b6aec0)

~~~json
{
  "source": "00b6aec0",
  "target": "00b6af94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6aec8`](#insn-00b6aec8)

~~~json
{
  "source": "00b6aec8",
  "target": "00b6aefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6aed4`](#insn-00b6aed4)

~~~json
{
  "source": "00b6aed4",
  "target": "00b6aefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6aed8`](#insn-00b6aed8)

~~~json
{
  "source": "00b6aed8",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6aedc`](#insn-00b6aedc)

~~~json
{
  "source": "00b6aedc",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6aef8`](#insn-00b6aef8)

~~~json
{
  "source": "00b6aef8",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6af04`](#insn-00b6af04)

~~~json
{
  "source": "00b6af04",
  "target": "00b6af14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af0c`](#insn-00b6af0c)

~~~json
{
  "source": "00b6af0c",
  "target": "00b6af48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af10`](#insn-00b6af10)

~~~json
{
  "source": "00b6af10",
  "target": "00b6af1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af18`](#insn-00b6af18)

~~~json
{
  "source": "00b6af18",
  "target": "00b6af48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af24`](#insn-00b6af24)

~~~json
{
  "source": "00b6af24",
  "target": "00b6af48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af28`](#insn-00b6af28)

~~~json
{
  "source": "00b6af28",
  "target": "Stack[-0xf8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af2c`](#insn-00b6af2c)

~~~json
{
  "source": "00b6af2c",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af44`](#insn-00b6af44)

~~~json
{
  "source": "00b6af44",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6af50`](#insn-00b6af50)

~~~json
{
  "source": "00b6af50",
  "target": "00b6af60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af58`](#insn-00b6af58)

~~~json
{
  "source": "00b6af58",
  "target": "00b6af94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af5c`](#insn-00b6af5c)

~~~json
{
  "source": "00b6af5c",
  "target": "00b6af68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af64`](#insn-00b6af64)

~~~json
{
  "source": "00b6af64",
  "target": "00b6af94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af70`](#insn-00b6af70)

~~~json
{
  "source": "00b6af70",
  "target": "00b6af94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af74`](#insn-00b6af74)

~~~json
{
  "source": "00b6af74",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af78`](#insn-00b6af78)

~~~json
{
  "source": "00b6af78",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6af90`](#insn-00b6af90)

~~~json
{
  "source": "00b6af90",
  "target": "00c5b0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6af98`](#insn-00b6af98)

~~~json
{
  "source": "00b6af98",
  "target": "00879c88",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6afa0`](#insn-00b6afa0)

~~~json
{
  "source": "00b6afa0",
  "target": "00b6ae18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6afa8`](#insn-00b6afa8)

~~~json
{
  "source": "00b6afa8",
  "target": "00b6ae20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6afac`](#insn-00b6afac)

~~~json
{
  "source": "00b6afac",
  "target": "00b6afc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6afb4`](#insn-00b6afb4)

~~~json
{
  "source": "00b6afb4",
  "target": "00b6afc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6afbc`](#insn-00b6afbc)

~~~json
{
  "source": "00b6afbc",
  "target": "00b6afd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6afc4`](#insn-00b6afc4)

~~~json
{
  "source": "00b6afc4",
  "target": "002a4dc9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a4dc9",
  "offset": 0,
  "size": 66,
  "datatype": "string",
  "bytes": "4170702049442c20415049206b65792c20616e642050726f6a65637420494420",
  "capture_start": "002a4dc9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b6afc8`](#insn-00b6afc8)

~~~json
{
  "source": "00b6afc8",
  "target": "00c5aca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6afd4`](#insn-00b6afd4)

~~~json
{
  "source": "00b6afd4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6afdc`](#insn-00b6afdc)

~~~json
{
  "source": "00b6afdc",
  "target": "00b6aff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6afe0`](#insn-00b6afe0)

~~~json
{
  "source": "00b6afe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6afe4`](#insn-00b6afe4)

~~~json
{
  "source": "00b6afe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6afe8`](#insn-00b6afe8)

~~~json
{
  "source": "00b6afe8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6aff4`](#insn-00b6aff4)

~~~json
{
  "source": "00b6aff4",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
