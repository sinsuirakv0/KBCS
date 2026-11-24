# 00bc7dbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc6dc8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc6/00bc6dc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-e23af2aaac11ad7749b7bb564f950e26)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc7dbc",
  "name": "_ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_14ConfigKeyValueEm",
  "size": 996,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5402472dbde4d1a1de71cb7b58783f809c49ef4a2a08252ab10877601963d670",
  "source_text_sha256": "5402472dbde4d1a1de71cb7b58783f809c49ef4a2a08252ab10877601963d670",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc7dbc",
        "00bc819f"
      ]
    ],
    "bytes_sha256": "b2ae69fa1db7824098c4800880f537b00617f6a4d39a7d29fa09266e8d439e72",
    "instruction_count": 249,
    "instruction_bytes": 996,
    "body_bytes": 996,
    "indirect": 7,
    "unresolved": 7
  }
}
~~~

## 呼び出し元

- [00c5e770](../00c5e/00c5e770.md)

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00589a54](../00589/00589a54.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bc50](../00c5b/00c5bc50.md)
- [00c5be40](../00c5b/00c5be40.md)
- [00c5be70](../00c5b/00c5be70.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5bee0](../00c5b/00c5bee0.md)
- [00c5bfe0](../00c5b/00c5bfe0.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c020](../00c5c/00c5c020.md)
- [00c5c050](../00c5c/00c5c050.md)
- [00c5c060](../00c5c/00c5c060.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c660](../00c5c/00c5c660.md)
- [00c5c6f0](../00c5c/00c5c6f0.md)
- [00c5ea20](../00c5e/00c5ea20.md)

## 関連文字列（未確認候補）

~~~text
"SetDefaults native function fails"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5842 bytes

~~~c

void _ZN8firebase13remote_config8internal20RemoteConfigInternal11SetDefaultsEPKNS0_14ConfigKeyValueEm
               (undefined8 param_1,undefined8 *param_2,undefined8 *param_3,long param_4)

{
  undefined8 *puVar1;
  byte bVar2;
  long lVar3;
  byte *pbVar4;
  ulong *puVar5;
  ulong *puVar6;
  byte *pbVar7;
  ulong *puVar8;
  byte *pbVar9;
  ulong *puVar10;
  uint uVar11;
  long *plVar12;
  undefined8 uVar13;
  undefined8 uVar14;
  undefined8 uVar15;
  undefined8 uVar16;
  long lVar17;
  ulong uVar18;
  long *plVar19;
  long lVar20;
  undefined8 *puVar21;
  byte *local_d0;
  byte *local_c8;
  undefined1 auStack_b8 [16];
  ulong *local_a8;
  ulong *local_a0;
  ulong *puStack_98;
  undefined1 auStack_90 [16];
  ulong local_80;
  ulong uStack_78;
  void *local_70;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  puVar1 = param_2 + 1;
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(&local_80,puVar1,4,0,0);
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_90,&local_80);
  _ZN8firebase12FutureHandleD2Ev(&local_80);
  plVar12 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_2);
  uVar13 = _ZN8firebase4util8hash_map8GetClassEv();
  uVar14 = _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE(0);
  uVar13 = FUN_00589a54(plVar12,uVar13,uVar14);
  uVar14 = _ZN8firebase4util3map11GetMethodIdENS1_6MethodE(0);
  if (param_4 != 0) {
    puVar21 = param_3 + 1;
    lVar20 = param_4;
    do {
      uVar15 = (**(code **)(*plVar12 + 0x538))(plVar12,puVar21[-1]);
      uVar16 = (**(code **)(*plVar12 + 0x538))(plVar12,*puVar21);
      lVar17 = FUN_00497b94(plVar12,uVar13,uVar14,uVar15,uVar16);
      uVar11 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar12);
      if (lVar17 != 0 && (uVar11 & 1) == 0) {
        (**(code **)(*plVar12 + 0xb8))(plVar12,lVar17);
      }
      (**(code **)(*plVar12 + 0xb8))(plVar12,uVar16);
      (**(code **)(*plVar12 + 0xb8))(plVar12,uVar15);
      lVar20 = lVar20 + -1;
      puVar21 = puVar21 + 2;
    } while (lVar20 != 0);
  }
  local_a0 = (ulong *)0x0;
  puStack_98 = (ulong *)0x0;
  local_a8 = (ulong *)0x0;
  _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7reserveEm
            (&local_a8,param_4);
  for (; param_4 != 0; param_4 = param_4 + -1) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc(&local_80,*param_3)
    ;
    if (local_a0 < puStack_98) {
      local_a0[2] = (ulong)local_70;
      local_a0[1] = uStack_78;
      *local_a0 = local_80;
      uStack_78 = 0;
      local_70 = (void *)0x0;
      local_80 = 0;
      local_a0 = local_a0 + 3;
    }
    else {
      _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIS6_EEvOT_
                (&local_a8,&local_80);
      if ((local_80 & 1) != 0) {
        _ZdlPv(local_70);
      }
    }
    param_3 = param_3 + 2;
  }
  uVar14 = FUN_00497b94(plVar12,param_2[0x33],DAT_01127570,uVar13);
  uVar18 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar12);
  if ((uVar18 & 1) == 0) {
    plVar19 = (long *)_Znwm(0x38);
    _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC2ERKS8_
              (&local_d0,&local_a8);
    *plVar19 = (long)puVar1;
    _ZN8firebase12FutureHandleC1ERKS0_(plVar19 + 1,auStack_90);
    plVar19[3] = (long)param_2;
    _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC2ERKS8_
              (plVar19 + 4,&local_d0);
    pbVar7 = local_d0;
    if (local_d0 != (byte *)0x0) {
      if (local_c8 != local_d0) {
        bVar2 = local_c8[-0x18];
        pbVar9 = local_c8 + -0x18;
        while( true ) {
          pbVar4 = pbVar9;
          if ((bVar2 & 1) != 0) {
            _ZdlPv(*(void **)(local_c8 + -8));
          }
          if (pbVar7 == pbVar4) break;
          bVar2 = pbVar4[-0x18];
          pbVar9 = pbVar4 + -0x18;
          local_c8 = pbVar4;
        }
      }
      local_c8 = pbVar7;
      _ZdlPv(local_d0);
    }
    if ((*(byte *)(param_2 + 0x40) & 1) == 0) {
      lVar20 = (long)param_2 + 0x201;
    }
    else {
      lVar20 = param_2[0x42];
    }
    _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
              (plVar12,uVar14,
               PTR__ZN8firebase13remote_config8internal19SetDefaultsCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ca08
               ,plVar19,lVar20);
  }
  else {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_b8,auStack_90);
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
              (puVar1,auStack_b8,1,"SetDefaults native function fails",&local_80);
    _ZN8firebase12FutureHandleD2Ev(auStack_b8);
    uVar14 = 0;
  }
  (**(code **)(*plVar12 + 0xb8))(plVar12,uVar14);
  (**(code **)(*plVar12 + 0xb8))(plVar12,uVar13);
  _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar12);
  _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,puVar1,auStack_90);
  puVar8 = local_a8;
  if (local_a8 != (ulong *)0x0) {
    if (local_a0 != local_a8) {
      bVar2 = (byte)local_a0[-3];
      puVar10 = local_a0 + -3;
      puVar6 = local_a0;
      while( true ) {
        puVar5 = puVar10;
        if ((bVar2 & 1) != 0) {
          _ZdlPv((void *)puVar6[-1]);
        }
        if (puVar8 == puVar5) break;
        bVar2 = (byte)puVar5[-3];
        puVar10 = puVar5 + -3;
        puVar6 = puVar5;
      }
    }
    local_a0 = puVar8;
    _ZdlPv(local_a8);
  }
  _ZN8firebase12FutureHandleD2Ev(auStack_90);
  if (*(long *)(lVar3 + 0x28) != local_68) {
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
<a id="insn-00bc7dbc"></a> `00bc7dbc` | `ff c3 03 d1` | sub sp,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00bc7dc0"></a> `00bc7dc0` | `fc 6f 09 a9` | stp x28,x27,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bc7dc4"></a> `00bc7dc4` | `fa 67 0a a9` | stp x26,x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bc7dc8"></a> `00bc7dc8` | `f8 5f 0b a9` | stp x24,x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc7dcc"></a> `00bc7dcc` | `f6 57 0c a9` | stp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bc7dd0"></a> `00bc7dd0` | `f4 4f 0d a9` | stp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bc7dd4"></a> `00bc7dd4` | `fd 7b 0e a9` | stp x29,x30,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bc7dd8"></a> `00bc7dd8` | `fd 83 03 91` | add x29,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00bc7ddc"></a> `00bc7ddc` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bc7de0"></a> `00bc7de0` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bc7de4"></a> `00bc7de4` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00bc7de8"></a> `00bc7de8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bc7dec"></a> `00bc7dec` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bc7df0"></a> `00bc7df0` | `f9 03 01 aa` | mov x25,x1 | `FALL_THROUGH`
<a id="insn-00bc7df4"></a> `00bc7df4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc7df8"></a> `00bc7df8` | `a8 83 1a f8` | stur x8,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00bc7dfc"></a> `00bc7dfc` | `00 20 00 91` | add x0,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bc7e00"></a> `00bc7e00` | `e8 c3 01 91` | add x8,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bc7e04"></a> `00bc7e04` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00bc7e08"></a> `00bc7e08` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bc7e0c"></a> `00bc7e0c` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bc7e10"></a> `00bc7e10` | `e0 0b 00 f9` | str x0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7e14"></a> `00bc7e14` | `33 50 02 94` | bl 0x00c5bee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7e18"></a> `00bc7e18` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bc7e1c"></a> `00bc7e1c` | `e1 c3 01 91` | add x1,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bc7e20"></a> `00bc7e20` | `20 50 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7e24"></a> `00bc7e24` | `e0 c3 01 91` | add x0,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bc7e28"></a> `00bc7e28` | `42 4f 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7e2c"></a> `00bc7e2c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bc7e30"></a> `00bc7e30` | `bc 50 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7e34"></a> `00bc7e34` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bc7e38"></a> `00bc7e38` | `f3 0f 00 f9` | str x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bc7e3c"></a> `00bc7e3c` | `89 50 02 94` | bl 0x00c5c060 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7e40"></a> `00bc7e40` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc7e44"></a> `00bc7e44` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bc7e48"></a> `00bc7e48` | `82 50 02 94` | bl 0x00c5c050 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7e4c"></a> `00bc7e4c` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bc7e50"></a> `00bc7e50` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7e54"></a> `00bc7e54` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc7e58"></a> `00bc7e58` | `ff 06 e7 97` | bl 0x00589a54 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7e5c"></a> `00bc7e5c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bc7e60"></a> `00bc7e60` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bc7e64"></a> `00bc7e64` | `6f 50 02 94` | bl 0x00c5c020 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7e68"></a> `00bc7e68` | `f7 05 00 b4` | cbz x23,0x00bc7f24 | `CONDITIONAL_JUMP`
<a id="insn-00bc7e6c"></a> `00bc7e6c` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bc7e70"></a> `00bc7e70` | `34 23 00 91` | add x20,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00bc7e74"></a> `00bc7e74` | `f8 03 17 aa` | mov x24,x23 | `FALL_THROUGH`
<a id="insn-00bc7e78"></a> `00bc7e78` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc7e7c"></a> `00bc7e7c` | `81 82 5f f8` | ldur x1,[x20, #-0x8] | `FALL_THROUGH`
<a id="insn-00bc7e80"></a> `00bc7e80` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bc7e84"></a> `00bc7e84` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7e88"></a> `00bc7e88` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7e8c"></a> `00bc7e8c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc7e90"></a> `00bc7e90` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bc7e94"></a> `00bc7e94` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00bc7e98"></a> `00bc7e98` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bc7e9c"></a> `00bc7e9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7ea0"></a> `00bc7ea0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7ea4"></a> `00bc7ea4` | `fc 03 00 aa` | mov x28,x0 | `FALL_THROUGH`
<a id="insn-00bc7ea8"></a> `00bc7ea8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7eac"></a> `00bc7eac` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bc7eb0"></a> `00bc7eb0` | `e2 03 1a aa` | mov x2,x26 | `FALL_THROUGH`
<a id="insn-00bc7eb4"></a> `00bc7eb4` | `e3 03 1b aa` | mov x3,x27 | `FALL_THROUGH`
<a id="insn-00bc7eb8"></a> `00bc7eb8` | `e4 03 1c aa` | mov x4,x28 | `FALL_THROUGH`
<a id="insn-00bc7ebc"></a> `00bc7ebc` | `36 3f e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7ec0"></a> `00bc7ec0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc7ec4"></a> `00bc7ec4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7ec8"></a> `00bc7ec8` | `4e 50 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7ecc"></a> `00bc7ecc` | `7f 02 00 f1` | cmp x19,#0x0 | `FALL_THROUGH`
<a id="insn-00bc7ed0"></a> `00bc7ed0` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00bc7ed4"></a> `00bc7ed4` | `08 01 00 2a` | orr w8,w8,w0 | `FALL_THROUGH`
<a id="insn-00bc7ed8"></a> `00bc7ed8` | `c8 00 00 37` | tbnz w8,#0x0,0x00bc7ef0 | `CONDITIONAL_JUMP`
<a id="insn-00bc7edc"></a> `00bc7edc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc7ee0"></a> `00bc7ee0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bc7ee4"></a> `00bc7ee4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7ee8"></a> `00bc7ee8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc7eec"></a> `00bc7eec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7ef0"></a> `00bc7ef0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc7ef4"></a> `00bc7ef4` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bc7ef8"></a> `00bc7ef8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7efc"></a> `00bc7efc` | `e1 03 1c aa` | mov x1,x28 | `FALL_THROUGH`
<a id="insn-00bc7f00"></a> `00bc7f00` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7f04"></a> `00bc7f04` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc7f08"></a> `00bc7f08` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bc7f0c"></a> `00bc7f0c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7f10"></a> `00bc7f10` | `e1 03 1b aa` | mov x1,x27 | `FALL_THROUGH`
<a id="insn-00bc7f14"></a> `00bc7f14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc7f18"></a> `00bc7f18` | `18 07 00 f1` | subs x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7f1c"></a> `00bc7f1c` | `94 42 00 91` | add x20,x20,#0x10 | `FALL_THROUGH`
<a id="insn-00bc7f20"></a> `00bc7f20` | `c1 fa ff 54` | b.ne 0x00bc7e78 | `CONDITIONAL_JUMP`
<a id="insn-00bc7f24"></a> `00bc7f24` | `ff 7f 05 a9` | stp xzr,xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc7f28"></a> `00bc7f28` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bc7f2c"></a> `00bc7f2c` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bc7f30"></a> `00bc7f30` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bc7f34"></a> `00bc7f34` | `47 4f 02 94` | bl 0x00c5bc50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7f38"></a> `00bc7f38` | `fb 0f 40 f9` | ldr x27,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bc7f3c"></a> `00bc7f3c` | `b7 01 00 b5` | cbnz x23,0x00bc7f70 | `CONDITIONAL_JUMP`
<a id="insn-00bc7f40"></a> `00bc7f40` | `1a 00 00 14` | b 0x00bc7fa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc7f44"></a> `00bc7f44` | `e9 43 40 f9` | ldr x9,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bc7f48"></a> `00bc7f48` | `e0 1f c0 3d` | ldr q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bc7f4c"></a> `00bc7f4c` | `0a 61 00 91` | add x10,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00bc7f50"></a> `00bc7f50` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7f54"></a> `00bc7f54` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00bc7f58"></a> `00bc7f58` | `ff ff 07 a9` | stp xzr,xzr,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00bc7f5c"></a> `00bc7f5c` | `ff 3b 00 f9` | str xzr,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bc7f60"></a> `00bc7f60` | `ea 2b 00 f9` | str x10,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc7f64"></a> `00bc7f64` | `f7 06 00 f1` | subs x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7f68"></a> `00bc7f68` | `39 43 00 91` | add x25,x25,#0x10 | `FALL_THROUGH`
<a id="insn-00bc7f6c"></a> `00bc7f6c` | `e0 01 00 54` | b.eq 0x00bc7fa8 | `CONDITIONAL_JUMP`
<a id="insn-00bc7f70"></a> `00bc7f70` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00bc7f74"></a> `00bc7f74` | `e0 c3 01 91` | add x0,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bc7f78"></a> `00bc7f78` | `ba 51 02 94` | bl 0x00c5c660 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7f7c"></a> `00bc7f7c` | `e8 27 45 a9` | ldp x8,x9,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc7f80"></a> `00bc7f80` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bc7f84"></a> `00bc7f84` | `03 fe ff 54` | b.cc 0x00bc7f44 | `CONDITIONAL_JUMP`
<a id="insn-00bc7f88"></a> `00bc7f88` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bc7f8c"></a> `00bc7f8c` | `e1 c3 01 91` | add x1,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bc7f90"></a> `00bc7f90` | `d8 51 02 94` | bl 0x00c5c6f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7f94"></a> `00bc7f94` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bc7f98"></a> `00bc7f98` | `68 fe 07 36` | tbz w8,#0x0,0x00bc7f64 | `CONDITIONAL_JUMP`
<a id="insn-00bc7f9c"></a> `00bc7f9c` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bc7fa0"></a> `00bc7fa0` | `ec 43 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7fa4"></a> `00bc7fa4` | `f0 ff ff 17` | b 0x00bc7f64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc7fa8"></a> `00bc7fa8` | `61 cf 40 f9` | ldr x1,[x27, #0x198] | `FALL_THROUGH`
<a id="insn-00bc7fac"></a> `00bc7fac` | `08 2b 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc7fb0"></a> `00bc7fb0` | `02 b9 42 f9` | ldr x2,[x8, #0x570] | `FALL_THROUGH`
<a id="insn-00bc7fb4"></a> `00bc7fb4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7fb8"></a> `00bc7fb8` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bc7fbc"></a> `00bc7fbc` | `f6 3e e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7fc0"></a> `00bc7fc0` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc7fc4"></a> `00bc7fc4` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bc7fc8"></a> `00bc7fc8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc7fcc"></a> `00bc7fcc` | `0d 50 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7fd0"></a> `00bc7fd0` | `e0 01 00 36` | tbz w0,#0x0,0x00bc800c | `CONDITIONAL_JUMP`
<a id="insn-00bc7fd4"></a> `00bc7fd4` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bc7fd8"></a> `00bc7fd8` | `e1 83 01 91` | add x1,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bc7fdc"></a> `00bc7fdc` | `b1 4f 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7fe0"></a> `00bc7fe0` | `c3 b7 ff b0` | adrp x3,0x2c0000 | `FALL_THROUGH`
<a id="insn-00bc7fe4"></a> `00bc7fe4` | `63 14 31 91` | add x3,x3,#0xc45 | `FALL_THROUGH`
<a id="insn-00bc7fe8"></a> `00bc7fe8` | `e1 e3 00 91` | add x1,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bc7fec"></a> `00bc7fec` | `e4 c3 01 91` | add x4,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bc7ff0"></a> `00bc7ff0` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bc7ff4"></a> `00bc7ff4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bc7ff8"></a> `00bc7ff8` | `92 4f 02 94` | bl 0x00c5be40 | `UNCONDITIONAL_CALL`
<a id="insn-00bc7ffc"></a> `00bc7ffc` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bc8000"></a> `00bc8000` | `cc 4e 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8004"></a> `00bc8004` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00bc8008"></a> `00bc8008` | `31 00 00 14` | b 0x00bc80cc | `UNCONDITIONAL_JUMP`
<a id="insn-00bc800c"></a> `00bc800c` | `00 07 80 52` | mov w0,#0x38 | `FALL_THROUGH`
<a id="insn-00bc8010"></a> `00bc8010` | `c8 43 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8014"></a> `00bc8014` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bc8018"></a> `00bc8018` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bc801c"></a> `00bc801c` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bc8020"></a> `00bc8020` | `80 5a 02 94` | bl 0x00c5ea20 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8024"></a> `00bc8024` | `fa 03 18 aa` | mov x26,x24 | `FALL_THROUGH`
<a id="insn-00bc8028"></a> `00bc8028` | `57 87 00 f8` | str x23,[x26], #0x8 | `FALL_THROUGH`
<a id="insn-00bc802c"></a> `00bc802c` | `e1 83 01 91` | add x1,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bc8030"></a> `00bc8030` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00bc8034"></a> `00bc8034` | `9b 4f 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8038"></a> `00bc8038` | `00 83 00 91` | add x0,x24,#0x20 | `FALL_THROUGH`
<a id="insn-00bc803c"></a> `00bc803c` | `1b 0f 00 f9` | str x27,[x24, #0x18] | `FALL_THROUGH`
<a id="insn-00bc8040"></a> `00bc8040` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bc8044"></a> `00bc8044` | `77 5a 02 94` | bl 0x00c5ea20 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8048"></a> `00bc8048` | `f3 13 40 f9` | ldr x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc804c"></a> `00bc804c` | `93 02 00 b4` | cbz x19,0x00bc809c | `CONDITIONAL_JUMP`
<a id="insn-00bc8050"></a> `00bc8050` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bc8054"></a> `00bc8054` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00bc8058"></a> `00bc8058` | `c0 01 00 54` | b.eq 0x00bc8090 | `CONDITIONAL_JUMP`
<a id="insn-00bc805c"></a> `00bc805c` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bc8060"></a> `00bc8060` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bc8064"></a> `00bc8064` | `c9 00 00 37` | tbnz w9,#0x0,0x00bc807c | `CONDITIONAL_JUMP`
<a id="insn-00bc8068"></a> `00bc8068` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bc806c"></a> `00bc806c` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00bc8070"></a> `00bc8070` | `c0 00 00 54` | b.eq 0x00bc8088 | `CONDITIONAL_JUMP`
<a id="insn-00bc8074"></a> `00bc8074` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bc8078"></a> `00bc8078` | `89 ff 07 36` | tbz w9,#0x0,0x00bc8068 | `CONDITIONAL_JUMP`
<a id="insn-00bc807c"></a> `00bc807c` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bc8080"></a> `00bc8080` | `b4 43 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8084"></a> `00bc8084` | `f9 ff ff 17` | b 0x00bc8068 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc8088"></a> `00bc8088` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc808c"></a> `00bc808c` | `02 00 00 14` | b 0x00bc8094 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc8090"></a> `00bc8090` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc8094"></a> `00bc8094` | `f3 17 00 f9` | str x19,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bc8098"></a> `00bc8098` | `ae 43 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc809c"></a> `00bc809c` | `68 03 48 39` | ldrb w8,[x27, #0x200] | `FALL_THROUGH`
<a id="insn-00bc80a0"></a> `00bc80a0` | `88 00 00 37` | tbnz w8,#0x0,0x00bc80b0 | `CONDITIONAL_JUMP`
<a id="insn-00bc80a4"></a> `00bc80a4` | `68 03 08 91` | add x8,x27,#0x200 | `FALL_THROUGH`
<a id="insn-00bc80a8"></a> `00bc80a8` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc80ac"></a> `00bc80ac` | `02 00 00 14` | b 0x00bc80b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc80b0"></a> `00bc80b0` | `64 0b 41 f9` | ldr x4,[x27, #0x210] | `FALL_THROUGH`
<a id="insn-00bc80b4"></a> `00bc80b4` | `a2 06 00 90` | adrp x2,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bc80b8"></a> `00bc80b8` | `42 04 45 f9` | ldr x2,[x2, #0xa08] | `FALL_THROUGH`
<a id="insn-00bc80bc"></a> `00bc80bc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc80c0"></a> `00bc80c0` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bc80c4"></a> `00bc80c4` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bc80c8"></a> `00bc80c8` | `c6 4f 02 94` | bl 0x00c5bfe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc80cc"></a> `00bc80cc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc80d0"></a> `00bc80d0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bc80d4"></a> `00bc80d4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc80d8"></a> `00bc80d8` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bc80dc"></a> `00bc80dc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc80e0"></a> `00bc80e0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc80e4"></a> `00bc80e4` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bc80e8"></a> `00bc80e8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc80ec"></a> `00bc80ec` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bc80f0"></a> `00bc80f0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc80f4"></a> `00bc80f4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc80f8"></a> `00bc80f8` | `c2 4f 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc80fc"></a> `00bc80fc` | `e0 07 40 f9` | ldr x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bc8100"></a> `00bc8100` | `e2 83 01 91` | add x2,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bc8104"></a> `00bc8104` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bc8108"></a> `00bc8108` | `5a 4f 02 94` | bl 0x00c5be70 | `UNCONDITIONAL_CALL`
<a id="insn-00bc810c"></a> `00bc810c` | `f3 27 40 f9` | ldr x19,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bc8110"></a> `00bc8110` | `93 02 00 b4` | cbz x19,0x00bc8160 | `CONDITIONAL_JUMP`
<a id="insn-00bc8114"></a> `00bc8114` | `e8 2b 40 f9` | ldr x8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc8118"></a> `00bc8118` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00bc811c"></a> `00bc811c` | `c0 01 00 54` | b.eq 0x00bc8154 | `CONDITIONAL_JUMP`
<a id="insn-00bc8120"></a> `00bc8120` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bc8124"></a> `00bc8124` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bc8128"></a> `00bc8128` | `c9 00 00 37` | tbnz w9,#0x0,0x00bc8140 | `CONDITIONAL_JUMP`
<a id="insn-00bc812c"></a> `00bc812c` | `7f 02 14 eb` | cmp x19,x20 | `FALL_THROUGH`
<a id="insn-00bc8130"></a> `00bc8130` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00bc8134"></a> `00bc8134` | `c0 00 00 54` | b.eq 0x00bc814c | `CONDITIONAL_JUMP`
<a id="insn-00bc8138"></a> `00bc8138` | `89 8e 5e 38` | ldrb w9,[x20, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bc813c"></a> `00bc813c` | `89 ff 07 36` | tbz w9,#0x0,0x00bc812c | `CONDITIONAL_JUMP`
<a id="insn-00bc8140"></a> `00bc8140` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bc8144"></a> `00bc8144` | `83 43 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8148"></a> `00bc8148` | `f9 ff ff 17` | b 0x00bc812c | `UNCONDITIONAL_JUMP`
<a id="insn-00bc814c"></a> `00bc814c` | `e0 27 40 f9` | ldr x0,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bc8150"></a> `00bc8150` | `02 00 00 14` | b 0x00bc8158 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc8154"></a> `00bc8154` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc8158"></a> `00bc8158` | `f3 2b 00 f9` | str x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc815c"></a> `00bc815c` | `7d 43 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8160"></a> `00bc8160` | `e0 83 01 91` | add x0,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bc8164"></a> `00bc8164` | `73 4e 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8168"></a> `00bc8168` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00bc816c"></a> `00bc816c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bc8170"></a> `00bc8170` | `a9 83 5a f8` | ldur x9,[x29, #-0x58] | `FALL_THROUGH`
<a id="insn-00bc8174"></a> `00bc8174` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bc8178"></a> `00bc8178` | `21 01 00 54` | b.ne 0x00bc819c | `CONDITIONAL_JUMP`
<a id="insn-00bc817c"></a> `00bc817c` | `fd 7b 4e a9` | ldp x29,x30,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bc8180"></a> `00bc8180` | `f4 4f 4d a9` | ldp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bc8184"></a> `00bc8184` | `f6 57 4c a9` | ldp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bc8188"></a> `00bc8188` | `f8 5f 4b a9` | ldp x24,x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bc818c"></a> `00bc818c` | `fa 67 4a a9` | ldp x26,x25,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bc8190"></a> `00bc8190` | `fc 6f 49 a9` | ldp x28,x27,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bc8194"></a> `00bc8194` | `ff c3 03 91` | add sp,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00bc8198"></a> `00bc8198` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc819c"></a> `00bc819c` | `79 43 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc7dbc`](#insn-00bc7dbc) 範囲 `[['00bc7dbc', '00bc7e6b']]`
  - `CONDITIONAL_JUMP` [`00bc7e68`](#insn-00bc7e68) → [`00bc7f24`](#insn-00bc7f24)
  - `FALL_THROUGH` [`00bc7e68`](#insn-00bc7e68) → [`00bc7e6c`](#insn-00bc7e6c)
- ブロック [`00bc7e6c`](#insn-00bc7e6c) 範囲 `[['00bc7e6c', '00bc7e77']]`
  - `FALL_THROUGH` [`00bc7e74`](#insn-00bc7e74) → [`00bc7e78`](#insn-00bc7e78)
- ブロック [`00bc7e78`](#insn-00bc7e78) 範囲 `[['00bc7e78', '00bc7edb']]`
  - `CONDITIONAL_JUMP` [`00bc7ed8`](#insn-00bc7ed8) → [`00bc7ef0`](#insn-00bc7ef0)
  - `FALL_THROUGH` [`00bc7ed8`](#insn-00bc7ed8) → [`00bc7edc`](#insn-00bc7edc)
- ブロック [`00bc7edc`](#insn-00bc7edc) 範囲 `[['00bc7edc', '00bc7eef']]`
  - `FALL_THROUGH` [`00bc7eec`](#insn-00bc7eec) → [`00bc7ef0`](#insn-00bc7ef0)
- ブロック [`00bc7ef0`](#insn-00bc7ef0) 範囲 `[['00bc7ef0', '00bc7f23']]`
  - `CONDITIONAL_JUMP` [`00bc7f20`](#insn-00bc7f20) → [`00bc7e78`](#insn-00bc7e78)
  - `FALL_THROUGH` [`00bc7f20`](#insn-00bc7f20) → [`00bc7f24`](#insn-00bc7f24)
- ブロック [`00bc7f24`](#insn-00bc7f24) 範囲 `[['00bc7f24', '00bc7f3f']]`
  - `CONDITIONAL_JUMP` [`00bc7f3c`](#insn-00bc7f3c) → [`00bc7f70`](#insn-00bc7f70)
  - `FALL_THROUGH` [`00bc7f3c`](#insn-00bc7f3c) → [`00bc7f40`](#insn-00bc7f40)
- ブロック [`00bc7f40`](#insn-00bc7f40) 範囲 `[['00bc7f40', '00bc7f43']]`
  - `UNCONDITIONAL_JUMP` [`00bc7f40`](#insn-00bc7f40) → [`00bc7fa8`](#insn-00bc7fa8)
- ブロック [`00bc7f44`](#insn-00bc7f44) 範囲 `[['00bc7f44', '00bc7f63']]`
  - `FALL_THROUGH` [`00bc7f60`](#insn-00bc7f60) → [`00bc7f64`](#insn-00bc7f64)
- ブロック [`00bc7f64`](#insn-00bc7f64) 範囲 `[['00bc7f64', '00bc7f6f']]`
  - `CONDITIONAL_JUMP` [`00bc7f6c`](#insn-00bc7f6c) → [`00bc7fa8`](#insn-00bc7fa8)
  - `FALL_THROUGH` [`00bc7f6c`](#insn-00bc7f6c) → [`00bc7f70`](#insn-00bc7f70)
- ブロック [`00bc7f70`](#insn-00bc7f70) 範囲 `[['00bc7f70', '00bc7f87']]`
  - `CONDITIONAL_JUMP` [`00bc7f84`](#insn-00bc7f84) → [`00bc7f44`](#insn-00bc7f44)
  - `FALL_THROUGH` [`00bc7f84`](#insn-00bc7f84) → [`00bc7f88`](#insn-00bc7f88)
- ブロック [`00bc7f88`](#insn-00bc7f88) 範囲 `[['00bc7f88', '00bc7f9b']]`
  - `CONDITIONAL_JUMP` [`00bc7f98`](#insn-00bc7f98) → [`00bc7f64`](#insn-00bc7f64)
  - `FALL_THROUGH` [`00bc7f98`](#insn-00bc7f98) → [`00bc7f9c`](#insn-00bc7f9c)
- ブロック [`00bc7f9c`](#insn-00bc7f9c) 範囲 `[['00bc7f9c', '00bc7fa7']]`
  - `UNCONDITIONAL_JUMP` [`00bc7fa4`](#insn-00bc7fa4) → [`00bc7f64`](#insn-00bc7f64)
- ブロック [`00bc7fa8`](#insn-00bc7fa8) 範囲 `[['00bc7fa8', '00bc7fd3']]`
  - `CONDITIONAL_JUMP` [`00bc7fd0`](#insn-00bc7fd0) → [`00bc800c`](#insn-00bc800c)
  - `FALL_THROUGH` [`00bc7fd0`](#insn-00bc7fd0) → [`00bc7fd4`](#insn-00bc7fd4)
- ブロック [`00bc7fd4`](#insn-00bc7fd4) 範囲 `[['00bc7fd4', '00bc800b']]`
  - `UNCONDITIONAL_JUMP` [`00bc8008`](#insn-00bc8008) → [`00bc80cc`](#insn-00bc80cc)
- ブロック [`00bc800c`](#insn-00bc800c) 範囲 `[['00bc800c', '00bc804f']]`
  - `CONDITIONAL_JUMP` [`00bc804c`](#insn-00bc804c) → [`00bc809c`](#insn-00bc809c)
  - `FALL_THROUGH` [`00bc804c`](#insn-00bc804c) → [`00bc8050`](#insn-00bc8050)
- ブロック [`00bc8050`](#insn-00bc8050) 範囲 `[['00bc8050', '00bc805b']]`
  - `CONDITIONAL_JUMP` [`00bc8058`](#insn-00bc8058) → [`00bc8090`](#insn-00bc8090)
  - `FALL_THROUGH` [`00bc8058`](#insn-00bc8058) → [`00bc805c`](#insn-00bc805c)
- ブロック [`00bc805c`](#insn-00bc805c) 範囲 `[['00bc805c', '00bc8067']]`
  - `CONDITIONAL_JUMP` [`00bc8064`](#insn-00bc8064) → [`00bc807c`](#insn-00bc807c)
  - `FALL_THROUGH` [`00bc8064`](#insn-00bc8064) → [`00bc8068`](#insn-00bc8068)
- ブロック [`00bc8068`](#insn-00bc8068) 範囲 `[['00bc8068', '00bc8073']]`
  - `CONDITIONAL_JUMP` [`00bc8070`](#insn-00bc8070) → [`00bc8088`](#insn-00bc8088)
  - `FALL_THROUGH` [`00bc8070`](#insn-00bc8070) → [`00bc8074`](#insn-00bc8074)
- ブロック [`00bc8074`](#insn-00bc8074) 範囲 `[['00bc8074', '00bc807b']]`
  - `CONDITIONAL_JUMP` [`00bc8078`](#insn-00bc8078) → [`00bc8068`](#insn-00bc8068)
  - `FALL_THROUGH` [`00bc8078`](#insn-00bc8078) → [`00bc807c`](#insn-00bc807c)
- ブロック [`00bc807c`](#insn-00bc807c) 範囲 `[['00bc807c', '00bc8087']]`
  - `UNCONDITIONAL_JUMP` [`00bc8084`](#insn-00bc8084) → [`00bc8068`](#insn-00bc8068)
- ブロック [`00bc8088`](#insn-00bc8088) 範囲 `[['00bc8088', '00bc808f']]`
  - `UNCONDITIONAL_JUMP` [`00bc808c`](#insn-00bc808c) → [`00bc8094`](#insn-00bc8094)
- ブロック [`00bc8090`](#insn-00bc8090) 範囲 `[['00bc8090', '00bc8093']]`
  - `FALL_THROUGH` [`00bc8090`](#insn-00bc8090) → [`00bc8094`](#insn-00bc8094)
- ブロック [`00bc8094`](#insn-00bc8094) 範囲 `[['00bc8094', '00bc809b']]`
  - `FALL_THROUGH` [`00bc8098`](#insn-00bc8098) → [`00bc809c`](#insn-00bc809c)
- ブロック [`00bc809c`](#insn-00bc809c) 範囲 `[['00bc809c', '00bc80a3']]`
  - `CONDITIONAL_JUMP` [`00bc80a0`](#insn-00bc80a0) → [`00bc80b0`](#insn-00bc80b0)
  - `FALL_THROUGH` [`00bc80a0`](#insn-00bc80a0) → [`00bc80a4`](#insn-00bc80a4)
- ブロック [`00bc80a4`](#insn-00bc80a4) 範囲 `[['00bc80a4', '00bc80af']]`
  - `UNCONDITIONAL_JUMP` [`00bc80ac`](#insn-00bc80ac) → [`00bc80b4`](#insn-00bc80b4)
- ブロック [`00bc80b0`](#insn-00bc80b0) 範囲 `[['00bc80b0', '00bc80b3']]`
  - `FALL_THROUGH` [`00bc80b0`](#insn-00bc80b0) → [`00bc80b4`](#insn-00bc80b4)
- ブロック [`00bc80b4`](#insn-00bc80b4) 範囲 `[['00bc80b4', '00bc80cb']]`
  - `FALL_THROUGH` [`00bc80c8`](#insn-00bc80c8) → [`00bc80cc`](#insn-00bc80cc)
- ブロック [`00bc80cc`](#insn-00bc80cc) 範囲 `[['00bc80cc', '00bc8113']]`
  - `CONDITIONAL_JUMP` [`00bc8110`](#insn-00bc8110) → [`00bc8160`](#insn-00bc8160)
  - `FALL_THROUGH` [`00bc8110`](#insn-00bc8110) → [`00bc8114`](#insn-00bc8114)
- ブロック [`00bc8114`](#insn-00bc8114) 範囲 `[['00bc8114', '00bc811f']]`
  - `CONDITIONAL_JUMP` [`00bc811c`](#insn-00bc811c) → [`00bc8154`](#insn-00bc8154)
  - `FALL_THROUGH` [`00bc811c`](#insn-00bc811c) → [`00bc8120`](#insn-00bc8120)
- ブロック [`00bc8120`](#insn-00bc8120) 範囲 `[['00bc8120', '00bc812b']]`
  - `CONDITIONAL_JUMP` [`00bc8128`](#insn-00bc8128) → [`00bc8140`](#insn-00bc8140)
  - `FALL_THROUGH` [`00bc8128`](#insn-00bc8128) → [`00bc812c`](#insn-00bc812c)
- ブロック [`00bc812c`](#insn-00bc812c) 範囲 `[['00bc812c', '00bc8137']]`
  - `CONDITIONAL_JUMP` [`00bc8134`](#insn-00bc8134) → [`00bc814c`](#insn-00bc814c)
  - `FALL_THROUGH` [`00bc8134`](#insn-00bc8134) → [`00bc8138`](#insn-00bc8138)
- ブロック [`00bc8138`](#insn-00bc8138) 範囲 `[['00bc8138', '00bc813f']]`
  - `CONDITIONAL_JUMP` [`00bc813c`](#insn-00bc813c) → [`00bc812c`](#insn-00bc812c)
  - `FALL_THROUGH` [`00bc813c`](#insn-00bc813c) → [`00bc8140`](#insn-00bc8140)
- ブロック [`00bc8140`](#insn-00bc8140) 範囲 `[['00bc8140', '00bc814b']]`
  - `UNCONDITIONAL_JUMP` [`00bc8148`](#insn-00bc8148) → [`00bc812c`](#insn-00bc812c)
- ブロック [`00bc814c`](#insn-00bc814c) 範囲 `[['00bc814c', '00bc8153']]`
  - `UNCONDITIONAL_JUMP` [`00bc8150`](#insn-00bc8150) → [`00bc8158`](#insn-00bc8158)
- ブロック [`00bc8154`](#insn-00bc8154) 範囲 `[['00bc8154', '00bc8157']]`
  - `FALL_THROUGH` [`00bc8154`](#insn-00bc8154) → [`00bc8158`](#insn-00bc8158)
- ブロック [`00bc8158`](#insn-00bc8158) 範囲 `[['00bc8158', '00bc815f']]`
  - `FALL_THROUGH` [`00bc815c`](#insn-00bc815c) → [`00bc8160`](#insn-00bc8160)
- ブロック [`00bc8160`](#insn-00bc8160) 範囲 `[['00bc8160', '00bc817b']]`
  - `CONDITIONAL_JUMP` [`00bc8178`](#insn-00bc8178) → [`00bc819c`](#insn-00bc819c)
  - `FALL_THROUGH` [`00bc8178`](#insn-00bc8178) → [`00bc817c`](#insn-00bc817c)
- ブロック [`00bc817c`](#insn-00bc817c) 範囲 `[['00bc817c', '00bc819b']]`
- ブロック [`00bc819c`](#insn-00bc819c) 範囲 `[['00bc819c', '00bc819f']]`

## 命令位置別の参照

- [`00bc7dc0`](#insn-00bc7dc0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7dc4`](#insn-00bc7dc4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7dc8`](#insn-00bc7dc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7dcc`](#insn-00bc7dcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7dd0`](#insn-00bc7dd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7dd4`](#insn-00bc7dd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7ddc`](#insn-00bc7ddc) → `Stack[-0xe8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7de4`](#insn-00bc7de4) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7df8`](#insn-00bc7df8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e10`](#insn-00bc7e10) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e14`](#insn-00bc7e14) → [`00c5bee0`](../00c5b/00c5bee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bee0` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e20`](#insn-00bc7e20) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e28`](#insn-00bc7e28) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e30`](#insn-00bc7e30) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e38`](#insn-00bc7e38) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e3c`](#insn-00bc7e3c) → [`00c5c060`](../00c5c/00c5c060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c060` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e48`](#insn-00bc7e48) → [`00c5c050`](../00c5c/00c5c050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c050` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e58`](#insn-00bc7e58) → [`00589a54`](../00589/00589a54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00589a54` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e64`](#insn-00bc7e64) → [`00c5c020`](../00c5c/00c5c020.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c020` · 推定シンボル `None` · 推定型 `None`
- [`00bc7e68`](#insn-00bc7e68) → [`00bc7f24`](#insn-00bc7f24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7ebc`](#insn-00bc7ebc) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bc7ec8`](#insn-00bc7ec8) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc7ed8`](#insn-00bc7ed8) → [`00bc7ef0`](#insn-00bc7ef0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f20`](#insn-00bc7f20) → [`00bc7e78`](#insn-00bc7e78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f24`](#insn-00bc7f24) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f28`](#insn-00bc7f28) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f34`](#insn-00bc7f34) → [`00c5bc50`](../00c5b/00c5bc50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc50` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f38`](#insn-00bc7f38) → `Stack[-0xd8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f3c`](#insn-00bc7f3c) → [`00bc7f70`](#insn-00bc7f70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f40`](#insn-00bc7f40) → [`00bc7fa8`](#insn-00bc7fa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f44`](#insn-00bc7f44) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f48`](#insn-00bc7f48) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f58`](#insn-00bc7f58) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f5c`](#insn-00bc7f5c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f60`](#insn-00bc7f60) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f6c`](#insn-00bc7f6c) → [`00bc7fa8`](#insn-00bc7fa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f78`](#insn-00bc7f78) → [`00c5c660`](../00c5c/00c5c660.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c660` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f7c`](#insn-00bc7f7c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f84`](#insn-00bc7f84) → [`00bc7f44`](#insn-00bc7f44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f90`](#insn-00bc7f90) → [`00c5c6f0`](../00c5c/00c5c6f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c6f0` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f94`](#insn-00bc7f94) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f98`](#insn-00bc7f98) → [`00bc7f64`](#insn-00bc7f64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7f9c`](#insn-00bc7f9c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7fa0`](#insn-00bc7fa0) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bc7fa4`](#insn-00bc7fa4) → [`00bc7f64`](#insn-00bc7f64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7fb0`](#insn-00bc7fb0) → `01127570`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc7fbc`](#insn-00bc7fbc) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bc7fc0`](#insn-00bc7fc0) → `Stack[-0xe0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7fcc`](#insn-00bc7fcc) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc7fd0`](#insn-00bc7fd0) → [`00bc800c`](#insn-00bc800c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc7fdc`](#insn-00bc7fdc) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bc7fe4`](#insn-00bc7fe4) → `002c0c45`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc7ff8`](#insn-00bc7ff8) → [`00c5be40`](../00c5b/00c5be40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be40` · 推定シンボル `None` · 推定型 `None`
- [`00bc8000`](#insn-00bc8000) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bc8008`](#insn-00bc8008) → [`00bc80cc`](#insn-00bc80cc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8010`](#insn-00bc8010) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bc8020`](#insn-00bc8020) → [`00c5ea20`](../00c5e/00c5ea20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ea20` · 推定シンボル `None` · 推定型 `None`
- [`00bc8034`](#insn-00bc8034) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bc8044`](#insn-00bc8044) → [`00c5ea20`](../00c5e/00c5ea20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ea20` · 推定シンボル `None` · 推定型 `None`
- [`00bc8048`](#insn-00bc8048) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc804c`](#insn-00bc804c) → [`00bc809c`](#insn-00bc809c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8050`](#insn-00bc8050) → `Stack[-0xc8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8058`](#insn-00bc8058) → [`00bc8090`](#insn-00bc8090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8064`](#insn-00bc8064) → [`00bc807c`](#insn-00bc807c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8070`](#insn-00bc8070) → [`00bc8088`](#insn-00bc8088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8078`](#insn-00bc8078) → [`00bc8068`](#insn-00bc8068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8080`](#insn-00bc8080) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bc8084`](#insn-00bc8084) → [`00bc8068`](#insn-00bc8068) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8088`](#insn-00bc8088) → `Stack[-0xd0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc808c`](#insn-00bc808c) → [`00bc8094`](#insn-00bc8094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8094`](#insn-00bc8094) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8098`](#insn-00bc8098) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bc80a0`](#insn-00bc80a0) → [`00bc80b0`](#insn-00bc80b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc80ac`](#insn-00bc80ac) → [`00bc80b4`](#insn-00bc80b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc80b8`](#insn-00bc80b8) → `00c9ca08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bc80b8`](#insn-00bc80b8) → [`00bc6468`](../00bc6/00bc6468.md) · `PARAM` · `ANALYSIS` · 関数 `00bc6468` · 推定シンボル `_ZN8firebase13remote_config8internal19SetDefaultsCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bc80c8`](#insn-00bc80c8) → [`00c5bfe0`](../00c5b/00c5bfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfe0` · 推定シンボル `None` · 推定型 `None`
- [`00bc80f8`](#insn-00bc80f8) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc80fc`](#insn-00bc80fc) → `Stack[-0xe8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8108`](#insn-00bc8108) → [`00c5be70`](../00c5b/00c5be70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be70` · 推定シンボル `None` · 推定型 `None`
- [`00bc810c`](#insn-00bc810c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8110`](#insn-00bc8110) → [`00bc8160`](#insn-00bc8160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8114`](#insn-00bc8114) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc811c`](#insn-00bc811c) → [`00bc8154`](#insn-00bc8154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8128`](#insn-00bc8128) → [`00bc8140`](#insn-00bc8140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8134`](#insn-00bc8134) → [`00bc814c`](#insn-00bc814c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc813c`](#insn-00bc813c) → [`00bc812c`](#insn-00bc812c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8144`](#insn-00bc8144) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bc8148`](#insn-00bc8148) → [`00bc812c`](#insn-00bc812c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc814c`](#insn-00bc814c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8150`](#insn-00bc8150) → [`00bc8158`](#insn-00bc8158) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8158`](#insn-00bc8158) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc815c`](#insn-00bc815c) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bc8164`](#insn-00bc8164) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bc8168`](#insn-00bc8168) → `Stack[-0xf0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8170`](#insn-00bc8170) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8178`](#insn-00bc8178) → [`00bc819c`](#insn-00bc819c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc817c`](#insn-00bc817c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8180`](#insn-00bc8180) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8184`](#insn-00bc8184) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8188`](#insn-00bc8188) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc818c`](#insn-00bc818c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8190`](#insn-00bc8190) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc819c`](#insn-00bc819c) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc7dc0`](#insn-00bc7dc0)

~~~json
{
  "source": "00bc7dc0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7dc4`](#insn-00bc7dc4)

~~~json
{
  "source": "00bc7dc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7dc8`](#insn-00bc7dc8)

~~~json
{
  "source": "00bc7dc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7dcc`](#insn-00bc7dcc)

~~~json
{
  "source": "00bc7dcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7dd0`](#insn-00bc7dd0)

~~~json
{
  "source": "00bc7dd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7dd4`](#insn-00bc7dd4)

~~~json
{
  "source": "00bc7dd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7ddc`](#insn-00bc7ddc)

~~~json
{
  "source": "00bc7ddc",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7de4`](#insn-00bc7de4)

~~~json
{
  "source": "00bc7de4",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7df8`](#insn-00bc7df8)

~~~json
{
  "source": "00bc7df8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7e10`](#insn-00bc7e10)

~~~json
{
  "source": "00bc7e10",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7e14`](#insn-00bc7e14)

~~~json
{
  "source": "00bc7e14",
  "target": "00c5bee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7e20`](#insn-00bc7e20)

~~~json
{
  "source": "00bc7e20",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7e28`](#insn-00bc7e28)

~~~json
{
  "source": "00bc7e28",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7e30`](#insn-00bc7e30)

~~~json
{
  "source": "00bc7e30",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7e38`](#insn-00bc7e38)

~~~json
{
  "source": "00bc7e38",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7e3c`](#insn-00bc7e3c)

~~~json
{
  "source": "00bc7e3c",
  "target": "00c5c060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7e48`](#insn-00bc7e48)

~~~json
{
  "source": "00bc7e48",
  "target": "00c5c050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7e58`](#insn-00bc7e58)

~~~json
{
  "source": "00bc7e58",
  "target": "00589a54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7e64`](#insn-00bc7e64)

~~~json
{
  "source": "00bc7e64",
  "target": "00c5c020",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7e68`](#insn-00bc7e68)

~~~json
{
  "source": "00bc7e68",
  "target": "00bc7f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7ebc`](#insn-00bc7ebc)

~~~json
{
  "source": "00bc7ebc",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7ec8`](#insn-00bc7ec8)

~~~json
{
  "source": "00bc7ec8",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7ed8`](#insn-00bc7ed8)

~~~json
{
  "source": "00bc7ed8",
  "target": "00bc7ef0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f20`](#insn-00bc7f20)

~~~json
{
  "source": "00bc7f20",
  "target": "00bc7e78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f24`](#insn-00bc7f24)

~~~json
{
  "source": "00bc7f24",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f28`](#insn-00bc7f28)

~~~json
{
  "source": "00bc7f28",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f34`](#insn-00bc7f34)

~~~json
{
  "source": "00bc7f34",
  "target": "00c5bc50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7f38`](#insn-00bc7f38)

~~~json
{
  "source": "00bc7f38",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f3c`](#insn-00bc7f3c)

~~~json
{
  "source": "00bc7f3c",
  "target": "00bc7f70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f40`](#insn-00bc7f40)

~~~json
{
  "source": "00bc7f40",
  "target": "00bc7fa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f44`](#insn-00bc7f44)

~~~json
{
  "source": "00bc7f44",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f48`](#insn-00bc7f48)

~~~json
{
  "source": "00bc7f48",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f58`](#insn-00bc7f58)

~~~json
{
  "source": "00bc7f58",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f5c`](#insn-00bc7f5c)

~~~json
{
  "source": "00bc7f5c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f60`](#insn-00bc7f60)

~~~json
{
  "source": "00bc7f60",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f6c`](#insn-00bc7f6c)

~~~json
{
  "source": "00bc7f6c",
  "target": "00bc7fa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f78`](#insn-00bc7f78)

~~~json
{
  "source": "00bc7f78",
  "target": "00c5c660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7f7c`](#insn-00bc7f7c)

~~~json
{
  "source": "00bc7f7c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f84`](#insn-00bc7f84)

~~~json
{
  "source": "00bc7f84",
  "target": "00bc7f44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f90`](#insn-00bc7f90)

~~~json
{
  "source": "00bc7f90",
  "target": "00c5c6f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7f94`](#insn-00bc7f94)

~~~json
{
  "source": "00bc7f94",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f98`](#insn-00bc7f98)

~~~json
{
  "source": "00bc7f98",
  "target": "00bc7f64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7f9c`](#insn-00bc7f9c)

~~~json
{
  "source": "00bc7f9c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7fa0`](#insn-00bc7fa0)

~~~json
{
  "source": "00bc7fa0",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7fa4`](#insn-00bc7fa4)

~~~json
{
  "source": "00bc7fa4",
  "target": "00bc7f64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7fb0`](#insn-00bc7fb0)

~~~json
{
  "source": "00bc7fb0",
  "target": "01127570",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127570",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc7fbc`](#insn-00bc7fbc)

~~~json
{
  "source": "00bc7fbc",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7fc0`](#insn-00bc7fc0)

~~~json
{
  "source": "00bc7fc0",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7fcc`](#insn-00bc7fcc)

~~~json
{
  "source": "00bc7fcc",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7fd0`](#insn-00bc7fd0)

~~~json
{
  "source": "00bc7fd0",
  "target": "00bc800c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc7fdc`](#insn-00bc7fdc)

~~~json
{
  "source": "00bc7fdc",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc7fe4`](#insn-00bc7fe4)

~~~json
{
  "source": "00bc7fe4",
  "target": "002c0c45",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c0c45",
  "offset": 0,
  "size": 34,
  "datatype": "string",
  "bytes": "53657444656661756c7473206e61746976652066756e6374696f6e206661696c",
  "capture_start": "002c0c45",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc7ff8`](#insn-00bc7ff8)

~~~json
{
  "source": "00bc7ff8",
  "target": "00c5be40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8000`](#insn-00bc8000)

~~~json
{
  "source": "00bc8000",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8008`](#insn-00bc8008)

~~~json
{
  "source": "00bc8008",
  "target": "00bc80cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8010`](#insn-00bc8010)

~~~json
{
  "source": "00bc8010",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8020`](#insn-00bc8020)

~~~json
{
  "source": "00bc8020",
  "target": "00c5ea20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8034`](#insn-00bc8034)

~~~json
{
  "source": "00bc8034",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8044`](#insn-00bc8044)

~~~json
{
  "source": "00bc8044",
  "target": "00c5ea20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8048`](#insn-00bc8048)

~~~json
{
  "source": "00bc8048",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc804c`](#insn-00bc804c)

~~~json
{
  "source": "00bc804c",
  "target": "00bc809c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8050`](#insn-00bc8050)

~~~json
{
  "source": "00bc8050",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8058`](#insn-00bc8058)

~~~json
{
  "source": "00bc8058",
  "target": "00bc8090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8064`](#insn-00bc8064)

~~~json
{
  "source": "00bc8064",
  "target": "00bc807c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8070`](#insn-00bc8070)

~~~json
{
  "source": "00bc8070",
  "target": "00bc8088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8078`](#insn-00bc8078)

~~~json
{
  "source": "00bc8078",
  "target": "00bc8068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8080`](#insn-00bc8080)

~~~json
{
  "source": "00bc8080",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8084`](#insn-00bc8084)

~~~json
{
  "source": "00bc8084",
  "target": "00bc8068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8088`](#insn-00bc8088)

~~~json
{
  "source": "00bc8088",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc808c`](#insn-00bc808c)

~~~json
{
  "source": "00bc808c",
  "target": "00bc8094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8094`](#insn-00bc8094)

~~~json
{
  "source": "00bc8094",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8098`](#insn-00bc8098)

~~~json
{
  "source": "00bc8098",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc80a0`](#insn-00bc80a0)

~~~json
{
  "source": "00bc80a0",
  "target": "00bc80b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc80ac`](#insn-00bc80ac)

~~~json
{
  "source": "00bc80ac",
  "target": "00bc80b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc80b8`](#insn-00bc80b8)

~~~json
{
  "source": "00bc80b8",
  "target": "00c9ca08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca08",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc80b8`](#insn-00bc80b8)

~~~json
{
  "source": "00bc80b8",
  "target": "00bc6468",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc80c8`](#insn-00bc80c8)

~~~json
{
  "source": "00bc80c8",
  "target": "00c5bfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc80f8`](#insn-00bc80f8)

~~~json
{
  "source": "00bc80f8",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc80fc`](#insn-00bc80fc)

~~~json
{
  "source": "00bc80fc",
  "target": "Stack[-0xe8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8108`](#insn-00bc8108)

~~~json
{
  "source": "00bc8108",
  "target": "00c5be70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc810c`](#insn-00bc810c)

~~~json
{
  "source": "00bc810c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8110`](#insn-00bc8110)

~~~json
{
  "source": "00bc8110",
  "target": "00bc8160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8114`](#insn-00bc8114)

~~~json
{
  "source": "00bc8114",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc811c`](#insn-00bc811c)

~~~json
{
  "source": "00bc811c",
  "target": "00bc8154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8128`](#insn-00bc8128)

~~~json
{
  "source": "00bc8128",
  "target": "00bc8140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8134`](#insn-00bc8134)

~~~json
{
  "source": "00bc8134",
  "target": "00bc814c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc813c`](#insn-00bc813c)

~~~json
{
  "source": "00bc813c",
  "target": "00bc812c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8144`](#insn-00bc8144)

~~~json
{
  "source": "00bc8144",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8148`](#insn-00bc8148)

~~~json
{
  "source": "00bc8148",
  "target": "00bc812c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc814c`](#insn-00bc814c)

~~~json
{
  "source": "00bc814c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8150`](#insn-00bc8150)

~~~json
{
  "source": "00bc8150",
  "target": "00bc8158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8158`](#insn-00bc8158)

~~~json
{
  "source": "00bc8158",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc815c`](#insn-00bc815c)

~~~json
{
  "source": "00bc815c",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8164`](#insn-00bc8164)

~~~json
{
  "source": "00bc8164",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8168`](#insn-00bc8168)

~~~json
{
  "source": "00bc8168",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8170`](#insn-00bc8170)

~~~json
{
  "source": "00bc8170",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8178`](#insn-00bc8178)

~~~json
{
  "source": "00bc8178",
  "target": "00bc819c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc817c`](#insn-00bc817c)

~~~json
{
  "source": "00bc817c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8180`](#insn-00bc8180)

~~~json
{
  "source": "00bc8180",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8184`](#insn-00bc8184)

~~~json
{
  "source": "00bc8184",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8188`](#insn-00bc8188)

~~~json
{
  "source": "00bc8188",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc818c`](#insn-00bc818c)

~~~json
{
  "source": "00bc818c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8190`](#insn-00bc8190)

~~~json
{
  "source": "00bc8190",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc819c`](#insn-00bc819c)

~~~json
{
  "source": "00bc819c",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
