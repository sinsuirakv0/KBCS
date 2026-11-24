# 00bc8dcc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b598cc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b59/00b598cc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-983a1feff210698847fbdefb8f0fcc1c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bc91f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc9/00bc91f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-9f7feea1189c793d74bb75fcbf5739fa)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc8dcc",
  "name": "_ZN8firebase13remote_config8internal20RemoteConfigInternal25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17RemoteConfigErrorEEEE",
  "size": 576,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e5a3f66648fccafb2bc3ecd6385e96bc59f649be4162cf30bdb1462c1ba42c9",
  "source_text_sha256": "1e5a3f66648fccafb2bc3ecd6385e96bc59f649be4162cf30bdb1462c1ba42c9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc8dcc",
        "00bc900b"
      ]
    ],
    "bytes_sha256": "2ed8c0dd306809010b97e0c19255bb307e5a3b1f41d93c0adf877bb8799e02c6",
    "instruction_count": 144,
    "instruction_bytes": 576,
    "body_bytes": 576,
    "indirect": 8,
    "unresolved": 7
  }
}
~~~

## 呼び出し元

- [00c5d390](../00c5d/00c5d390.md)

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [005896b4](../00589/005896b4.md)
- [00bc9ba8](../00bc9/00bc9ba8.md)
- [00bc9bac](../00bc9/00bc9bac.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a800](../00c5a/00c5a800.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5d260](../00c5d/00c5d260.md)
- [00c5d280](../00c5d/00c5d280.md)

## 関連文字列（未確認候補）

~~~text
"!util::CheckAndClearJniExceptions(env)"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3081 bytes

~~~c

void _ZN8firebase13remote_config8internal20RemoteConfigInternal25AddOnConfigUpdateListenerENSt6__ndk18functionIFvONS0_12ConfigUpdateENS0_17RemoteConfigErrorEEEE
               (undefined8 param_1,undefined8 *param_2,long *param_3)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  undefined8 uVar4;
  ulong uVar5;
  undefined8 uVar6;
  long *plVar7;
  code *pcVar8;
  undefined **local_b0;
  undefined8 uStack_a8;
  long *local_90;
  long local_80 [4];
  long *local_60;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_2);
  lVar3 = _Znwm(0x30);
  plVar7 = (long *)param_3[4];
  if (plVar7 == (long *)0x0) {
    local_60 = (long *)0x0;
    *(undefined8 *)(lVar3 + 0x20) = 0;
  }
  else {
    if (param_3 == plVar7) {
      local_60 = local_80;
      (**(code **)(*plVar7 + 0x18))(plVar7,local_80);
    }
    else {
      local_60 = (long *)(**(code **)(*plVar7 + 0x10))(plVar7);
    }
    if (local_60 == (long *)0x0) {
      *(undefined8 *)(lVar3 + 0x20) = 0;
    }
    else {
      if (local_80 == local_60) {
        *(long *)(lVar3 + 0x20) = lVar3;
        (**(code **)(*local_60 + 0x18))(local_60,lVar3);
      }
      else {
        uVar4 = (**(code **)(*local_60 + 0x10))();
        *(undefined8 *)(lVar3 + 0x20) = uVar4;
      }
      if (local_80 == local_60) {
        pcVar8 = *(code **)(*local_60 + 0x20);
      }
      else {
        if (local_60 == (long *)0x0) goto LAB_00bc8ed4;
        pcVar8 = *(code **)(*local_60 + 0x28);
      }
      (*pcVar8)();
    }
  }
LAB_00bc8ed4:
  uVar4 = FUN_005896b4(plVar2,DAT_01126258,DAT_01126268,lVar3);
  uVar5 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
  if ((uVar5 & 1) != 0) {
    _ZN8firebase9LogAssertEPKcz("!util::CheckAndClearJniExceptions(env)");
  }
  uVar4 = FUN_004977f4(plVar2,param_2[0x33],DAT_01126110,uVar4);
  uVar5 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
  if ((uVar5 & 1) != 0) {
    _ZN8firebase9LogAssertEPKcz("!util::CheckAndClearJniExceptions(env)");
  }
  uVar6 = (**(code **)(*plVar2 + 0xa8))(plVar2,uVar4);
  (**(code **)(*plVar2 + 0xb8))(plVar2,uVar4);
  uVar4 = _Znwm(0x50);
  local_b0 = &PTR_FUN_00c91428;
  uStack_a8 = uVar6;
  local_90 = (long *)&local_b0;
  _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternalC2EPNS1_20RemoteConfigInternalENSt6__ndk18functionIFvvEEE
            (uVar4,param_2,&local_b0);
  if (&local_b0 == (undefined ***)local_90) {
    pcVar8 = *(code **)(*local_90 + 0x20);
  }
  else {
    if (local_90 == (long *)0x0) goto LAB_00bc8fc0;
    pcVar8 = *(code **)(*local_90 + 0x28);
  }
  (*pcVar8)();
LAB_00bc8fc0:
  _ZN8firebase15CleanupNotifier14RegisterObjectEPvPFvS1_E(param_2 + 0x27,uVar4,FUN_00bc9570);
  _ZN8firebase13remote_config32ConfigUpdateListenerRegistrationC1EPNS0_8internal40ConfigUpdateListenerRegistrationInternalE
            (param_1,uVar4);
  if (*(long *)(lVar1 + 0x28) != local_48) {
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
<a id="insn-00bc8dcc"></a> `00bc8dcc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bc8dd0"></a> `00bc8dd0` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bc8dd4"></a> `00bc8dd4` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bc8dd8"></a> `00bc8dd8` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bc8ddc"></a> `00bc8ddc` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bc8de0"></a> `00bc8de0` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bc8de4"></a> `00bc8de4` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bc8de8"></a> `00bc8de8` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bc8dec"></a> `00bc8dec` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bc8df0"></a> `00bc8df0` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bc8df4"></a> `00bc8df4` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bc8df8"></a> `00bc8df8` | `a9 83 1c f8` | stur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bc8dfc"></a> `00bc8dfc` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bc8e00"></a> `00bc8e00` | `a0 47 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8e04"></a> `00bc8e04` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bc8e08"></a> `00bc8e08` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-00bc8e0c"></a> `00bc8e0c` | `21 3b 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8e10"></a> `00bc8e10` | `e8 12 40 f9` | ldr x8,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00bc8e14"></a> `00bc8e14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc8e18"></a> `00bc8e18` | `28 02 00 b4` | cbz x8,0x00bc8e5c | `CONDITIONAL_JUMP`
<a id="insn-00bc8e1c"></a> `00bc8e1c` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00bc8e20"></a> `00bc8e20` | `40 02 00 54` | b.eq 0x00bc8e68 | `CONDITIONAL_JUMP`
<a id="insn-00bc8e24"></a> `00bc8e24` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00bc8e28"></a> `00bc8e28` | `29 09 40 f9` | ldr x9,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00bc8e2c"></a> `00bc8e2c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bc8e30"></a> `00bc8e30` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bc8e34"></a> `00bc8e34` | `e0 2b 00 f9` | str x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc8e38"></a> `00bc8e38` | `a0 02 00 b4` | cbz x0,0x00bc8e8c | `CONDITIONAL_JUMP`
<a id="insn-00bc8e3c"></a> `00bc8e3c` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bc8e40"></a> `00bc8e40` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00bc8e44"></a> `00bc8e44` | `80 02 00 54` | b.eq 0x00bc8e94 | `CONDITIONAL_JUMP`
<a id="insn-00bc8e48"></a> `00bc8e48` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc8e4c"></a> `00bc8e4c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bc8e50"></a> `00bc8e50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc8e54"></a> `00bc8e54` | `60 12 00 f9` | str x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc8e58"></a> `00bc8e58` | `14 00 00 14` | b 0x00bc8ea8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc8e5c"></a> `00bc8e5c` | `ff 2b 00 f9` | str xzr,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc8e60"></a> `00bc8e60` | `7f 12 00 f9` | str xzr,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc8e64"></a> `00bc8e64` | `1c 00 00 14` | b 0x00bc8ed4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc8e68"></a> `00bc8e68` | `e9 c3 00 91` | add x9,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bc8e6c"></a> `00bc8e6c` | `e9 2b 00 f9` | str x9,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc8e70"></a> `00bc8e70` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00bc8e74"></a> `00bc8e74` | `29 0d 40 f9` | ldr x9,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00bc8e78"></a> `00bc8e78` | `e1 c3 00 91` | add x1,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bc8e7c"></a> `00bc8e7c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bc8e80"></a> `00bc8e80` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bc8e84"></a> `00bc8e84` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc8e88"></a> `00bc8e88` | `a0 fd ff b5` | cbnz x0,0x00bc8e3c | `CONDITIONAL_JUMP`
<a id="insn-00bc8e8c"></a> `00bc8e8c` | `7f 12 00 f9` | str xzr,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc8e90"></a> `00bc8e90` | `11 00 00 14` | b 0x00bc8ed4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc8e94"></a> `00bc8e94` | `73 12 00 f9` | str x19,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc8e98"></a> `00bc8e98` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc8e9c"></a> `00bc8e9c` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bc8ea0"></a> `00bc8ea0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc8ea4"></a> `00bc8ea4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc8ea8"></a> `00bc8ea8` | `e0 2b 40 f9` | ldr x0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc8eac"></a> `00bc8eac` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bc8eb0"></a> `00bc8eb0` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00bc8eb4"></a> `00bc8eb4` | `a0 00 00 54` | b.eq 0x00bc8ec8 | `CONDITIONAL_JUMP`
<a id="insn-00bc8eb8"></a> `00bc8eb8` | `e0 00 00 b4` | cbz x0,0x00bc8ed4 | `CONDITIONAL_JUMP`
<a id="insn-00bc8ebc"></a> `00bc8ebc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc8ec0"></a> `00bc8ec0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bc8ec4"></a> `00bc8ec4` | `03 00 00 14` | b 0x00bc8ed0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc8ec8"></a> `00bc8ec8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc8ecc"></a> `00bc8ecc` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bc8ed0"></a> `00bc8ed0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc8ed4"></a> `00bc8ed4` | `e8 2a 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc8ed8"></a> `00bc8ed8` | `e9 2a 00 d0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc8edc"></a> `00bc8edc` | `01 2d 41 f9` | ldr x1,[x8, #0x258] | `FALL_THROUGH`
<a id="insn-00bc8ee0"></a> `00bc8ee0` | `22 35 41 f9` | ldr x2,[x9, #0x268] | `FALL_THROUGH`
<a id="insn-00bc8ee4"></a> `00bc8ee4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bc8ee8"></a> `00bc8ee8` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bc8eec"></a> `00bc8eec` | `f2 01 e7 97` | bl 0x005896b4 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8ef0"></a> `00bc8ef0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc8ef4"></a> `00bc8ef4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bc8ef8"></a> `00bc8ef8` | `1a 47 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8efc"></a> `00bc8efc` | `80 00 00 36` | tbz w0,#0x0,0x00bc8f0c | `CONDITIONAL_JUMP`
<a id="insn-00bc8f00"></a> `00bc8f00` | `c0 b6 ff b0` | adrp x0,0x2a1000 | `FALL_THROUGH`
<a id="insn-00bc8f04"></a> `00bc8f04` | `00 6c 2d 91` | add x0,x0,#0xb5b | `FALL_THROUGH`
<a id="insn-00bc8f08"></a> `00bc8f08` | `3e 47 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8f0c"></a> `00bc8f0c` | `e8 2a 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc8f10"></a> `00bc8f10` | `a1 ce 40 f9` | ldr x1,[x21, #0x198] | `FALL_THROUGH`
<a id="insn-00bc8f14"></a> `00bc8f14` | `02 89 40 f9` | ldr x2,[x8, #0x110] | `FALL_THROUGH`
<a id="insn-00bc8f18"></a> `00bc8f18` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bc8f1c"></a> `00bc8f1c` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bc8f20"></a> `00bc8f20` | `35 3a e3 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8f24"></a> `00bc8f24` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc8f28"></a> `00bc8f28` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bc8f2c"></a> `00bc8f2c` | `0d 47 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8f30"></a> `00bc8f30` | `80 00 00 36` | tbz w0,#0x0,0x00bc8f40 | `CONDITIONAL_JUMP`
<a id="insn-00bc8f34"></a> `00bc8f34` | `c0 b6 ff b0` | adrp x0,0x2a1000 | `FALL_THROUGH`
<a id="insn-00bc8f38"></a> `00bc8f38` | `00 6c 2d 91` | add x0,x0,#0xb5b | `FALL_THROUGH`
<a id="insn-00bc8f3c"></a> `00bc8f3c` | `31 47 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8f40"></a> `00bc8f40` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bc8f44"></a> `00bc8f44` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bc8f48"></a> `00bc8f48` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc8f4c"></a> `00bc8f4c` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bc8f50"></a> `00bc8f50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc8f54"></a> `00bc8f54` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bc8f58"></a> `00bc8f58` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bc8f5c"></a> `00bc8f5c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bc8f60"></a> `00bc8f60` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc8f64"></a> `00bc8f64` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bc8f68"></a> `00bc8f68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc8f6c"></a> `00bc8f6c` | `00 0a 80 52` | mov w0,#0x50 | `FALL_THROUGH`
<a id="insn-00bc8f70"></a> `00bc8f70` | `c8 3a 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8f74"></a> `00bc8f74` | `48 06 00 b0` | adrp x8,0xc91000 | `FALL_THROUGH`
<a id="insn-00bc8f78"></a> `00bc8f78` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc8f7c"></a> `00bc8f7c` | `08 a1 10 91` | add x8,x8,#0x428 | `FALL_THROUGH`
<a id="insn-00bc8f80"></a> `00bc8f80` | `f6 03 00 91` | mov x22,sp | `FALL_THROUGH`
<a id="insn-00bc8f84"></a> `00bc8f84` | `e8 5f 00 a9` | stp x8,x23,[sp] | `FALL_THROUGH`
<a id="insn-00bc8f88"></a> `00bc8f88` | `f6 13 00 f9` | str x22,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc8f8c"></a> `00bc8f8c` | `e2 03 00 91` | mov x2,sp | `FALL_THROUGH`
<a id="insn-00bc8f90"></a> `00bc8f90` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bc8f94"></a> `00bc8f94` | `bb 50 02 94` | bl 0x00c5d280 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8f98"></a> `00bc8f98` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc8f9c"></a> `00bc8f9c` | `df 02 00 eb` | cmp x22,x0 | `FALL_THROUGH`
<a id="insn-00bc8fa0"></a> `00bc8fa0` | `a0 00 00 54` | b.eq 0x00bc8fb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc8fa4"></a> `00bc8fa4` | `e0 00 00 b4` | cbz x0,0x00bc8fc0 | `CONDITIONAL_JUMP`
<a id="insn-00bc8fa8"></a> `00bc8fa8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc8fac"></a> `00bc8fac` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bc8fb0"></a> `00bc8fb0` | `03 00 00 14` | b 0x00bc8fbc | `UNCONDITIONAL_JUMP`
<a id="insn-00bc8fb4"></a> `00bc8fb4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc8fb8"></a> `00bc8fb8` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bc8fbc"></a> `00bc8fbc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc8fc0"></a> `00bc8fc0` | `02 00 00 b0` | adrp x2,0xbc9000 | `FALL_THROUGH`
<a id="insn-00bc8fc4"></a> `00bc8fc4` | `a0 e2 04 91` | add x0,x21,#0x138 | `FALL_THROUGH`
<a id="insn-00bc8fc8"></a> `00bc8fc8` | `42 c0 15 91` | add x2,x2,#0x570 | `FALL_THROUGH`
<a id="insn-00bc8fcc"></a> `00bc8fcc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc8fd0"></a> `00bc8fd0` | `0c 46 02 94` | bl 0x00c5a800 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8fd4"></a> `00bc8fd4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc8fd8"></a> `00bc8fd8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bc8fdc"></a> `00bc8fdc` | `a1 50 02 94` | bl 0x00c5d260 | `UNCONDITIONAL_CALL`
<a id="insn-00bc8fe0"></a> `00bc8fe0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bc8fe4"></a> `00bc8fe4` | `a9 83 5c f8` | ldur x9,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00bc8fe8"></a> `00bc8fe8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bc8fec"></a> `00bc8fec` | `e1 00 00 54` | b.ne 0x00bc9008 | `CONDITIONAL_JUMP`
<a id="insn-00bc8ff0"></a> `00bc8ff0` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bc8ff4"></a> `00bc8ff4` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bc8ff8"></a> `00bc8ff8` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bc8ffc"></a> `00bc8ffc` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bc9000"></a> `00bc9000` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bc9004"></a> `00bc9004` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc9008"></a> `00bc9008` | `b6 3a 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc8dcc`](#insn-00bc8dcc) 範囲 `[['00bc8dcc', '00bc8e1b']]`
  - `CONDITIONAL_JUMP` [`00bc8e18`](#insn-00bc8e18) → [`00bc8e5c`](#insn-00bc8e5c)
  - `FALL_THROUGH` [`00bc8e18`](#insn-00bc8e18) → [`00bc8e1c`](#insn-00bc8e1c)
- ブロック [`00bc8e1c`](#insn-00bc8e1c) 範囲 `[['00bc8e1c', '00bc8e23']]`
  - `CONDITIONAL_JUMP` [`00bc8e20`](#insn-00bc8e20) → [`00bc8e68`](#insn-00bc8e68)
  - `FALL_THROUGH` [`00bc8e20`](#insn-00bc8e20) → [`00bc8e24`](#insn-00bc8e24)
- ブロック [`00bc8e24`](#insn-00bc8e24) 範囲 `[['00bc8e24', '00bc8e3b']]`
  - `CONDITIONAL_JUMP` [`00bc8e38`](#insn-00bc8e38) → [`00bc8e8c`](#insn-00bc8e8c)
  - `FALL_THROUGH` [`00bc8e38`](#insn-00bc8e38) → [`00bc8e3c`](#insn-00bc8e3c)
- ブロック [`00bc8e3c`](#insn-00bc8e3c) 範囲 `[['00bc8e3c', '00bc8e47']]`
  - `CONDITIONAL_JUMP` [`00bc8e44`](#insn-00bc8e44) → [`00bc8e94`](#insn-00bc8e94)
  - `FALL_THROUGH` [`00bc8e44`](#insn-00bc8e44) → [`00bc8e48`](#insn-00bc8e48)
- ブロック [`00bc8e48`](#insn-00bc8e48) 範囲 `[['00bc8e48', '00bc8e5b']]`
  - `UNCONDITIONAL_JUMP` [`00bc8e58`](#insn-00bc8e58) → [`00bc8ea8`](#insn-00bc8ea8)
- ブロック [`00bc8e5c`](#insn-00bc8e5c) 範囲 `[['00bc8e5c', '00bc8e67']]`
  - `UNCONDITIONAL_JUMP` [`00bc8e64`](#insn-00bc8e64) → [`00bc8ed4`](#insn-00bc8ed4)
- ブロック [`00bc8e68`](#insn-00bc8e68) 範囲 `[['00bc8e68', '00bc8e8b']]`
  - `CONDITIONAL_JUMP` [`00bc8e88`](#insn-00bc8e88) → [`00bc8e3c`](#insn-00bc8e3c)
  - `FALL_THROUGH` [`00bc8e88`](#insn-00bc8e88) → [`00bc8e8c`](#insn-00bc8e8c)
- ブロック [`00bc8e8c`](#insn-00bc8e8c) 範囲 `[['00bc8e8c', '00bc8e93']]`
  - `UNCONDITIONAL_JUMP` [`00bc8e90`](#insn-00bc8e90) → [`00bc8ed4`](#insn-00bc8ed4)
- ブロック [`00bc8e94`](#insn-00bc8e94) 範囲 `[['00bc8e94', '00bc8ea7']]`
  - `FALL_THROUGH` [`00bc8ea4`](#insn-00bc8ea4) → [`00bc8ea8`](#insn-00bc8ea8)
- ブロック [`00bc8ea8`](#insn-00bc8ea8) 範囲 `[['00bc8ea8', '00bc8eb7']]`
  - `CONDITIONAL_JUMP` [`00bc8eb4`](#insn-00bc8eb4) → [`00bc8ec8`](#insn-00bc8ec8)
  - `FALL_THROUGH` [`00bc8eb4`](#insn-00bc8eb4) → [`00bc8eb8`](#insn-00bc8eb8)
- ブロック [`00bc8eb8`](#insn-00bc8eb8) 範囲 `[['00bc8eb8', '00bc8ebb']]`
  - `CONDITIONAL_JUMP` [`00bc8eb8`](#insn-00bc8eb8) → [`00bc8ed4`](#insn-00bc8ed4)
  - `FALL_THROUGH` [`00bc8eb8`](#insn-00bc8eb8) → [`00bc8ebc`](#insn-00bc8ebc)
- ブロック [`00bc8ebc`](#insn-00bc8ebc) 範囲 `[['00bc8ebc', '00bc8ec7']]`
  - `UNCONDITIONAL_JUMP` [`00bc8ec4`](#insn-00bc8ec4) → [`00bc8ed0`](#insn-00bc8ed0)
- ブロック [`00bc8ec8`](#insn-00bc8ec8) 範囲 `[['00bc8ec8', '00bc8ecf']]`
  - `FALL_THROUGH` [`00bc8ecc`](#insn-00bc8ecc) → [`00bc8ed0`](#insn-00bc8ed0)
- ブロック [`00bc8ed0`](#insn-00bc8ed0) 範囲 `[['00bc8ed0', '00bc8ed3']]`
  - `FALL_THROUGH` [`00bc8ed0`](#insn-00bc8ed0) → [`00bc8ed4`](#insn-00bc8ed4)
- ブロック [`00bc8ed4`](#insn-00bc8ed4) 範囲 `[['00bc8ed4', '00bc8eff']]`
  - `CONDITIONAL_JUMP` [`00bc8efc`](#insn-00bc8efc) → [`00bc8f0c`](#insn-00bc8f0c)
  - `FALL_THROUGH` [`00bc8efc`](#insn-00bc8efc) → [`00bc8f00`](#insn-00bc8f00)
- ブロック [`00bc8f00`](#insn-00bc8f00) 範囲 `[['00bc8f00', '00bc8f0b']]`
  - `FALL_THROUGH` [`00bc8f08`](#insn-00bc8f08) → [`00bc8f0c`](#insn-00bc8f0c)
- ブロック [`00bc8f0c`](#insn-00bc8f0c) 範囲 `[['00bc8f0c', '00bc8f33']]`
  - `CONDITIONAL_JUMP` [`00bc8f30`](#insn-00bc8f30) → [`00bc8f40`](#insn-00bc8f40)
  - `FALL_THROUGH` [`00bc8f30`](#insn-00bc8f30) → [`00bc8f34`](#insn-00bc8f34)
- ブロック [`00bc8f34`](#insn-00bc8f34) 範囲 `[['00bc8f34', '00bc8f3f']]`
  - `FALL_THROUGH` [`00bc8f3c`](#insn-00bc8f3c) → [`00bc8f40`](#insn-00bc8f40)
- ブロック [`00bc8f40`](#insn-00bc8f40) 範囲 `[['00bc8f40', '00bc8fa3']]`
  - `CONDITIONAL_JUMP` [`00bc8fa0`](#insn-00bc8fa0) → [`00bc8fb4`](#insn-00bc8fb4)
  - `FALL_THROUGH` [`00bc8fa0`](#insn-00bc8fa0) → [`00bc8fa4`](#insn-00bc8fa4)
- ブロック [`00bc8fa4`](#insn-00bc8fa4) 範囲 `[['00bc8fa4', '00bc8fa7']]`
  - `CONDITIONAL_JUMP` [`00bc8fa4`](#insn-00bc8fa4) → [`00bc8fc0`](#insn-00bc8fc0)
  - `FALL_THROUGH` [`00bc8fa4`](#insn-00bc8fa4) → [`00bc8fa8`](#insn-00bc8fa8)
- ブロック [`00bc8fa8`](#insn-00bc8fa8) 範囲 `[['00bc8fa8', '00bc8fb3']]`
  - `UNCONDITIONAL_JUMP` [`00bc8fb0`](#insn-00bc8fb0) → [`00bc8fbc`](#insn-00bc8fbc)
- ブロック [`00bc8fb4`](#insn-00bc8fb4) 範囲 `[['00bc8fb4', '00bc8fbb']]`
  - `FALL_THROUGH` [`00bc8fb8`](#insn-00bc8fb8) → [`00bc8fbc`](#insn-00bc8fbc)
- ブロック [`00bc8fbc`](#insn-00bc8fbc) 範囲 `[['00bc8fbc', '00bc8fbf']]`
  - `FALL_THROUGH` [`00bc8fbc`](#insn-00bc8fbc) → [`00bc8fc0`](#insn-00bc8fc0)
- ブロック [`00bc8fc0`](#insn-00bc8fc0) 範囲 `[['00bc8fc0', '00bc8fef']]`
  - `CONDITIONAL_JUMP` [`00bc8fec`](#insn-00bc8fec) → [`00bc9008`](#insn-00bc9008)
  - `FALL_THROUGH` [`00bc8fec`](#insn-00bc8fec) → [`00bc8ff0`](#insn-00bc8ff0)
- ブロック [`00bc8ff0`](#insn-00bc8ff0) 範囲 `[['00bc8ff0', '00bc9007']]`
- ブロック [`00bc9008`](#insn-00bc9008) 範囲 `[['00bc9008', '00bc900b']]`

## 命令位置別の参照

- [`00bc8dd0`](#insn-00bc8dd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8dd4`](#insn-00bc8dd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8dd8`](#insn-00bc8dd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8ddc`](#insn-00bc8ddc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8df8`](#insn-00bc8df8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e00`](#insn-00bc8e00) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e0c`](#insn-00bc8e0c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e18`](#insn-00bc8e18) → [`00bc8e5c`](#insn-00bc8e5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e20`](#insn-00bc8e20) → [`00bc8e68`](#insn-00bc8e68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e34`](#insn-00bc8e34) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e38`](#insn-00bc8e38) → [`00bc8e8c`](#insn-00bc8e8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e44`](#insn-00bc8e44) → [`00bc8e94`](#insn-00bc8e94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e48`](#insn-00bc8e48) → `Stack[-0x80]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e58`](#insn-00bc8e58) → [`00bc8ea8`](#insn-00bc8ea8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e5c`](#insn-00bc8e5c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e64`](#insn-00bc8e64) → [`00bc8ed4`](#insn-00bc8ed4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e6c`](#insn-00bc8e6c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e84`](#insn-00bc8e84) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e88`](#insn-00bc8e88) → [`00bc8e3c`](#insn-00bc8e3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8e90`](#insn-00bc8e90) → [`00bc8ed4`](#insn-00bc8ed4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8ea8`](#insn-00bc8ea8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8eb4`](#insn-00bc8eb4) → [`00bc8ec8`](#insn-00bc8ec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8eb8`](#insn-00bc8eb8) → [`00bc8ed4`](#insn-00bc8ed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8ec4`](#insn-00bc8ec4) → [`00bc8ed0`](#insn-00bc8ed0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8edc`](#insn-00bc8edc) → `01126258`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc8ee0`](#insn-00bc8ee0) → `01126268`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc8eec`](#insn-00bc8eec) → [`005896b4`](../00589/005896b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005896b4` · 推定シンボル `None` · 推定型 `None`
- [`00bc8ef8`](#insn-00bc8ef8) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bc8efc`](#insn-00bc8efc) → [`00bc8f0c`](#insn-00bc8f0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8f04`](#insn-00bc8f04) → `002a1b5b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc8f08`](#insn-00bc8f08) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bc8f14`](#insn-00bc8f14) → `01126110`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc8f20`](#insn-00bc8f20) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bc8f2c`](#insn-00bc8f2c) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bc8f30`](#insn-00bc8f30) → [`00bc8f40`](#insn-00bc8f40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8f38`](#insn-00bc8f38) → `002a1b5b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc8f3c`](#insn-00bc8f3c) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bc8f70`](#insn-00bc8f70) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bc8f84`](#insn-00bc8f84) → `00c91428`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bc8f84`](#insn-00bc8f84) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8f88`](#insn-00bc8f88) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8f94`](#insn-00bc8f94) → [`00c5d280`](../00c5d/00c5d280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d280` · 推定シンボル `None` · 推定型 `None`
- [`00bc8f98`](#insn-00bc8f98) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fa0`](#insn-00bc8fa0) → [`00bc8fb4`](#insn-00bc8fb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fa4`](#insn-00bc8fa4) → [`00bc8fc0`](#insn-00bc8fc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fa8`](#insn-00bc8fa8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fac`](#insn-00bc8fac) → `00c91450`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bc8fb0`](#insn-00bc8fb0) → [`00bc8fbc`](#insn-00bc8fbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fb4`](#insn-00bc8fb4) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fb8`](#insn-00bc8fb8) → `00c91448`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bc8fbc`](#insn-00bc8fbc) → [`00bc9ba8`](../00bc9/00bc9ba8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00bc9ba8` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fbc`](#insn-00bc8fbc) → [`00bc9bac`](../00bc9/00bc9bac.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00bc9bac` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fc8`](#insn-00bc8fc8) → [`00bc9570`](../00bc9/00bc9570.md) · `PARAM` · `ANALYSIS` · 関数 `00bc9570` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fd0`](#insn-00bc8fd0) → [`00c5a800`](../00c5a/00c5a800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a800` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fdc`](#insn-00bc8fdc) → [`00c5d260`](../00c5d/00c5d260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d260` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fe4`](#insn-00bc8fe4) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8fec`](#insn-00bc8fec) → [`00bc9008`](#insn-00bc9008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8ff0`](#insn-00bc8ff0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8ff4`](#insn-00bc8ff4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8ff8`](#insn-00bc8ff8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc8ffc`](#insn-00bc8ffc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9008`](#insn-00bc9008) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc8dd0`](#insn-00bc8dd0)

~~~json
{
  "source": "00bc8dd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8dd4`](#insn-00bc8dd4)

~~~json
{
  "source": "00bc8dd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8dd8`](#insn-00bc8dd8)

~~~json
{
  "source": "00bc8dd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8ddc`](#insn-00bc8ddc)

~~~json
{
  "source": "00bc8ddc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8df8`](#insn-00bc8df8)

~~~json
{
  "source": "00bc8df8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e00`](#insn-00bc8e00)

~~~json
{
  "source": "00bc8e00",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8e0c`](#insn-00bc8e0c)

~~~json
{
  "source": "00bc8e0c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8e18`](#insn-00bc8e18)

~~~json
{
  "source": "00bc8e18",
  "target": "00bc8e5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e20`](#insn-00bc8e20)

~~~json
{
  "source": "00bc8e20",
  "target": "00bc8e68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e34`](#insn-00bc8e34)

~~~json
{
  "source": "00bc8e34",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e38`](#insn-00bc8e38)

~~~json
{
  "source": "00bc8e38",
  "target": "00bc8e8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e44`](#insn-00bc8e44)

~~~json
{
  "source": "00bc8e44",
  "target": "00bc8e94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e48`](#insn-00bc8e48)

~~~json
{
  "source": "00bc8e48",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e58`](#insn-00bc8e58)

~~~json
{
  "source": "00bc8e58",
  "target": "00bc8ea8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e5c`](#insn-00bc8e5c)

~~~json
{
  "source": "00bc8e5c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e64`](#insn-00bc8e64)

~~~json
{
  "source": "00bc8e64",
  "target": "00bc8ed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e6c`](#insn-00bc8e6c)

~~~json
{
  "source": "00bc8e6c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e84`](#insn-00bc8e84)

~~~json
{
  "source": "00bc8e84",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e88`](#insn-00bc8e88)

~~~json
{
  "source": "00bc8e88",
  "target": "00bc8e3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8e90`](#insn-00bc8e90)

~~~json
{
  "source": "00bc8e90",
  "target": "00bc8ed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8ea8`](#insn-00bc8ea8)

~~~json
{
  "source": "00bc8ea8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8eb4`](#insn-00bc8eb4)

~~~json
{
  "source": "00bc8eb4",
  "target": "00bc8ec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8eb8`](#insn-00bc8eb8)

~~~json
{
  "source": "00bc8eb8",
  "target": "00bc8ed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8ec4`](#insn-00bc8ec4)

~~~json
{
  "source": "00bc8ec4",
  "target": "00bc8ed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8edc`](#insn-00bc8edc)

~~~json
{
  "source": "00bc8edc",
  "target": "01126258",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126258",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc8ee0`](#insn-00bc8ee0)

~~~json
{
  "source": "00bc8ee0",
  "target": "01126268",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126268",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc8eec`](#insn-00bc8eec)

~~~json
{
  "source": "00bc8eec",
  "target": "005896b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8ef8`](#insn-00bc8ef8)

~~~json
{
  "source": "00bc8ef8",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8efc`](#insn-00bc8efc)

~~~json
{
  "source": "00bc8efc",
  "target": "00bc8f0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8f04`](#insn-00bc8f04)

~~~json
{
  "source": "00bc8f04",
  "target": "002a1b5b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1b5b",
  "offset": 0,
  "size": 39,
  "datatype": "string",
  "bytes": "217574696c3a3a436865636b416e64436c6561724a6e69457863657074696f6e",
  "capture_start": "002a1b5b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc8f08`](#insn-00bc8f08)

~~~json
{
  "source": "00bc8f08",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8f14`](#insn-00bc8f14)

~~~json
{
  "source": "00bc8f14",
  "target": "01126110",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126110",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc8f20`](#insn-00bc8f20)

~~~json
{
  "source": "00bc8f20",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8f2c`](#insn-00bc8f2c)

~~~json
{
  "source": "00bc8f2c",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8f30`](#insn-00bc8f30)

~~~json
{
  "source": "00bc8f30",
  "target": "00bc8f40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8f38`](#insn-00bc8f38)

~~~json
{
  "source": "00bc8f38",
  "target": "002a1b5b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a1b5b",
  "offset": 0,
  "size": 39,
  "datatype": "string",
  "bytes": "217574696c3a3a436865636b416e64436c6561724a6e69457863657074696f6e",
  "capture_start": "002a1b5b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc8f3c`](#insn-00bc8f3c)

~~~json
{
  "source": "00bc8f3c",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8f70`](#insn-00bc8f70)

~~~json
{
  "source": "00bc8f70",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8f84`](#insn-00bc8f84)

~~~json
{
  "source": "00bc8f84",
  "target": "00c91428",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91428",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc8f84`](#insn-00bc8f84)

~~~json
{
  "source": "00bc8f84",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8f88`](#insn-00bc8f88)

~~~json
{
  "source": "00bc8f88",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8f94`](#insn-00bc8f94)

~~~json
{
  "source": "00bc8f94",
  "target": "00c5d280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8f98`](#insn-00bc8f98)

~~~json
{
  "source": "00bc8f98",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8fa0`](#insn-00bc8fa0)

~~~json
{
  "source": "00bc8fa0",
  "target": "00bc8fb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8fa4`](#insn-00bc8fa4)

~~~json
{
  "source": "00bc8fa4",
  "target": "00bc8fc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8fa8`](#insn-00bc8fa8)

~~~json
{
  "source": "00bc8fa8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8fac`](#insn-00bc8fac)

~~~json
{
  "source": "00bc8fac",
  "target": "00c91450",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91450",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc8fb0`](#insn-00bc8fb0)

~~~json
{
  "source": "00bc8fb0",
  "target": "00bc8fbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8fb4`](#insn-00bc8fb4)

~~~json
{
  "source": "00bc8fb4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8fb8`](#insn-00bc8fb8)

~~~json
{
  "source": "00bc8fb8",
  "target": "00c91448",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91448",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc8fbc`](#insn-00bc8fbc)

~~~json
{
  "source": "00bc8fbc",
  "target": "00bc9ba8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8fbc`](#insn-00bc8fbc)

~~~json
{
  "source": "00bc8fbc",
  "target": "00bc9bac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8fc8`](#insn-00bc8fc8)

~~~json
{
  "source": "00bc8fc8",
  "target": "00bc9570",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8fd0`](#insn-00bc8fd0)

~~~json
{
  "source": "00bc8fd0",
  "target": "00c5a800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8fdc`](#insn-00bc8fdc)

~~~json
{
  "source": "00bc8fdc",
  "target": "00c5d260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc8fe4`](#insn-00bc8fe4)

~~~json
{
  "source": "00bc8fe4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8fec`](#insn-00bc8fec)

~~~json
{
  "source": "00bc8fec",
  "target": "00bc9008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8ff0`](#insn-00bc8ff0)

~~~json
{
  "source": "00bc8ff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8ff4`](#insn-00bc8ff4)

~~~json
{
  "source": "00bc8ff4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8ff8`](#insn-00bc8ff8)

~~~json
{
  "source": "00bc8ff8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc8ffc`](#insn-00bc8ffc)

~~~json
{
  "source": "00bc8ffc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9008`](#insn-00bc9008)

~~~json
{
  "source": "00bc9008",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
