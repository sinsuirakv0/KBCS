# 00bc6dbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc5dc8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc5/00bc5dc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-4b435b49ac61142085f59351a6ad10b1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc6dbc",
  "name": "_ZN8firebase13remote_config8internal20RemoteConfigInternal16FetchAndActivateEv",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6026b5fec455701bbadceddffaf201f96671bd8b747df2bb3e27e4afc75631b7",
  "source_text_sha256": "6026b5fec455701bbadceddffaf201f96671bd8b747df2bb3e27e4afc75631b7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc6dbc",
        "00bc6fab"
      ]
    ],
    "bytes_sha256": "8e2f55272f43e7796f8585a468737fa7dc0e2bc07b8a41f4e897b01a2956a84d",
    "instruction_count": 124,
    "instruction_bytes": 496,
    "body_bytes": 496,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00c5e7c0](../00c5e/00c5e7c0.md)

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c58f50](../00c58/00c58f50.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)
- [00c5bea0](../00c5b/00c5bea0.md)
- [00c5bee0](../00c5b/00c5bee0.md)
- [00c5bfe0](../00c5b/00c5bfe0.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5e9a0](../00c5e/00c5e9a0.md)
- [00c5e9c0](../00c5e/00c5e9c0.md)
- [00c5ea20](../00c5e/00c5ea20.md)

## 関連文字列（未確認候補）

~~~text
"FetchAndActivate native function fails"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3222 bytes

~~~c

void _ZN8firebase13remote_config8internal20RemoteConfigInternal16FetchAndActivateEv
               (undefined8 param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  byte bVar2;
  long lVar3;
  byte *pbVar4;
  byte *pbVar5;
  byte *pbVar6;
  byte *pbVar7;
  undefined8 uVar8;
  long *plVar9;
  ulong uVar10;
  long *plVar11;
  long lVar12;
  byte *local_b0;
  byte *local_a8;
  undefined8 uStack_a0;
  undefined1 auStack_98 [16];
  undefined1 auStack_88 [16];
  undefined1 auStack_78 [16];
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  puVar1 = param_2 + 1;
  uVar8 = _Znwm(1);
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E
            (auStack_78,puVar1,3,uVar8,
             PTR__ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv_00c9ca30);
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_78);
  _ZN8firebase12FutureHandleD2Ev(auStack_78);
  plVar9 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_2);
  uVar8 = FUN_00497b94(plVar9,param_2[0x33],DAT_01127560);
  uVar10 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar9);
  if ((uVar10 & 1) == 0) {
    plVar11 = (long *)_Znwm(0x38);
    *plVar11 = (long)puVar1;
    local_a8 = (byte *)0x0;
    uStack_a0 = 0;
    local_b0 = (byte *)0x0;
    _ZN8firebase12FutureHandleC1ERKS0_(plVar11 + 1,auStack_88);
    plVar11[3] = (long)param_2;
    _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEEC2ERKS8_
              (plVar11 + 4,&local_b0);
    pbVar6 = local_b0;
    if (local_b0 != (byte *)0x0) {
      if (local_a8 != local_b0) {
        bVar2 = local_a8[-0x18];
        pbVar7 = local_a8 + -0x18;
        pbVar5 = local_a8;
        while( true ) {
          pbVar4 = pbVar7;
          if ((bVar2 & 1) != 0) {
            _ZdlPv(*(void **)(pbVar5 + -8));
          }
          if (pbVar6 == pbVar4) break;
          bVar2 = pbVar4[-0x18];
          pbVar7 = pbVar4 + -0x18;
          pbVar5 = pbVar4;
        }
      }
      local_a8 = pbVar6;
      _ZdlPv(local_b0);
    }
    if ((*(byte *)(param_2 + 0x40) & 1) == 0) {
      lVar12 = (long)param_2 + 0x201;
    }
    else {
      lVar12 = param_2[0x42];
    }
    _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
              (plVar9,uVar8,
               PTR__ZN8firebase13remote_config8internal18BoolResultCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9ca00
               ,plVar11,lVar12);
  }
  else {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_98,auStack_88);
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIbEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
              (puVar1,auStack_98,1,"FetchAndActivate native function fails",auStack_78);
    _ZN8firebase12FutureHandleD2Ev(auStack_98);
    uVar8 = 0;
  }
  (**(code **)(*plVar9 + 0xb8))(plVar9,uVar8);
  _ZN8firebase6FutureIbEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,puVar1,auStack_88);
  _ZN8firebase12FutureHandleD2Ev(auStack_88);
  if (*(long *)(lVar3 + 0x28) == local_68) {
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
<a id="insn-00bc6dbc"></a> `00bc6dbc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bc6dc0"></a> `00bc6dc0` | `fb 2b 00 f9` | str x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc6dc4"></a> `00bc6dc4` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bc6dc8"></a> `00bc6dc8` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bc6dcc"></a> `00bc6dcc` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bc6dd0"></a> `00bc6dd0` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bc6dd4"></a> `00bc6dd4` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bc6dd8"></a> `00bc6dd8` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bc6ddc"></a> `00bc6ddc` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bc6de0"></a> `00bc6de0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bc6de4"></a> `00bc6de4` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bc6de8"></a> `00bc6de8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bc6dec"></a> `00bc6dec` | `14 20 00 91` | add x20,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bc6df0"></a> `00bc6df0` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bc6df4"></a> `00bc6df4` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bc6df8"></a> `00bc6df8` | `4e 48 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6dfc"></a> `00bc6dfc` | `a3 06 00 d0` | adrp x3,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bc6e00"></a> `00bc6e00` | `63 18 45 f9` | ldr x3,[x3, #0xa30] | `FALL_THROUGH`
<a id="insn-00bc6e04"></a> `00bc6e04` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bc6e08"></a> `00bc6e08` | `e8 e3 00 91` | add x8,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bc6e0c"></a> `00bc6e0c` | `61 00 80 52` | mov w1,#0x3 | `FALL_THROUGH`
<a id="insn-00bc6e10"></a> `00bc6e10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc6e14"></a> `00bc6e14` | `33 54 02 94` | bl 0x00c5bee0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6e18"></a> `00bc6e18` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bc6e1c"></a> `00bc6e1c` | `e1 e3 00 91` | add x1,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bc6e20"></a> `00bc6e20` | `20 54 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6e24"></a> `00bc6e24` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bc6e28"></a> `00bc6e28` | `42 53 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6e2c"></a> `00bc6e2c` | `c0 02 40 f9` | ldr x0,[x22] | `FALL_THROUGH`
<a id="insn-00bc6e30"></a> `00bc6e30` | `bc 54 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6e34"></a> `00bc6e34` | `c1 ce 40 f9` | ldr x1,[x22, #0x198] | `FALL_THROUGH`
<a id="insn-00bc6e38"></a> `00bc6e38` | `08 2b 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bc6e3c"></a> `00bc6e3c` | `02 b1 42 f9` | ldr x2,[x8, #0x560] | `FALL_THROUGH`
<a id="insn-00bc6e40"></a> `00bc6e40` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bc6e44"></a> `00bc6e44` | `54 43 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6e48"></a> `00bc6e48` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bc6e4c"></a> `00bc6e4c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc6e50"></a> `00bc6e50` | `6c 54 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6e54"></a> `00bc6e54` | `e0 01 00 36` | tbz w0,#0x0,0x00bc6e90 | `CONDITIONAL_JUMP`
<a id="insn-00bc6e58"></a> `00bc6e58` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bc6e5c"></a> `00bc6e5c` | `e1 a3 00 91` | add x1,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bc6e60"></a> `00bc6e60` | `10 54 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6e64"></a> `00bc6e64` | `63 b7 ff d0` | adrp x3,0x2b4000 | `FALL_THROUGH`
<a id="insn-00bc6e68"></a> `00bc6e68` | `63 80 22 91` | add x3,x3,#0x8a0 | `FALL_THROUGH`
<a id="insn-00bc6e6c"></a> `00bc6e6c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bc6e70"></a> `00bc6e70` | `e4 e3 00 91` | add x4,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bc6e74"></a> `00bc6e74` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bc6e78"></a> `00bc6e78` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc6e7c"></a> `00bc6e7c` | `c9 5e 02 94` | bl 0x00c5e9a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6e80"></a> `00bc6e80` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bc6e84"></a> `00bc6e84` | `2b 53 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6e88"></a> `00bc6e88` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00bc6e8c"></a> `00bc6e8c` | `30 00 00 14` | b 0x00bc6f4c | `UNCONDITIONAL_JUMP`
<a id="insn-00bc6e90"></a> `00bc6e90` | `00 07 80 52` | mov w0,#0x38 | `FALL_THROUGH`
<a id="insn-00bc6e94"></a> `00bc6e94` | `27 48 02 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6e98"></a> `00bc6e98` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bc6e9c"></a> `00bc6e9c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bc6ea0"></a> `00bc6ea0` | `34 87 00 f8` | str x20,[x25], #0x8 | `FALL_THROUGH`
<a id="insn-00bc6ea4"></a> `00bc6ea4` | `ff ff 00 a9` | stp xzr,xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bc6ea8"></a> `00bc6ea8` | `ff 03 00 f9` | str xzr,[sp] | `FALL_THROUGH`
<a id="insn-00bc6eac"></a> `00bc6eac` | `e1 a3 00 91` | add x1,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bc6eb0"></a> `00bc6eb0` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bc6eb4"></a> `00bc6eb4` | `fb 53 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6eb8"></a> `00bc6eb8` | `e0 82 00 91` | add x0,x23,#0x20 | `FALL_THROUGH`
<a id="insn-00bc6ebc"></a> `00bc6ebc` | `f6 0e 00 f9` | str x22,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00bc6ec0"></a> `00bc6ec0` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bc6ec4"></a> `00bc6ec4` | `d7 5e 02 94` | bl 0x00c5ea20 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6ec8"></a> `00bc6ec8` | `f9 03 40 f9` | ldr x25,[sp] | `FALL_THROUGH`
<a id="insn-00bc6ecc"></a> `00bc6ecc` | `99 02 00 b4` | cbz x25,0x00bc6f1c | `CONDITIONAL_JUMP`
<a id="insn-00bc6ed0"></a> `00bc6ed0` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bc6ed4"></a> `00bc6ed4` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00bc6ed8"></a> `00bc6ed8` | `c0 01 00 54` | b.eq 0x00bc6f10 | `CONDITIONAL_JUMP`
<a id="insn-00bc6edc"></a> `00bc6edc` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00bc6ee0"></a> `00bc6ee0` | `69 8f 5e 38` | ldrb w9,[x27, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bc6ee4"></a> `00bc6ee4` | `c9 00 00 37` | tbnz w9,#0x0,0x00bc6efc | `CONDITIONAL_JUMP`
<a id="insn-00bc6ee8"></a> `00bc6ee8` | `3f 03 1b eb` | cmp x25,x27 | `FALL_THROUGH`
<a id="insn-00bc6eec"></a> `00bc6eec` | `e8 03 1b aa` | mov x8,x27 | `FALL_THROUGH`
<a id="insn-00bc6ef0"></a> `00bc6ef0` | `c0 00 00 54` | b.eq 0x00bc6f08 | `CONDITIONAL_JUMP`
<a id="insn-00bc6ef4"></a> `00bc6ef4` | `69 8f 5e 38` | ldrb w9,[x27, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bc6ef8"></a> `00bc6ef8` | `89 ff 07 36` | tbz w9,#0x0,0x00bc6ee8 | `CONDITIONAL_JUMP`
<a id="insn-00bc6efc"></a> `00bc6efc` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bc6f00"></a> `00bc6f00` | `14 48 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6f04"></a> `00bc6f04` | `f9 ff ff 17` | b 0x00bc6ee8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc6f08"></a> `00bc6f08` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00bc6f0c"></a> `00bc6f0c` | `02 00 00 14` | b 0x00bc6f14 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc6f10"></a> `00bc6f10` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bc6f14"></a> `00bc6f14` | `f9 07 00 f9` | str x25,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bc6f18"></a> `00bc6f18` | `0e 48 02 94` | bl 0x00c58f50 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6f1c"></a> `00bc6f1c` | `c8 02 48 39` | ldrb w8,[x22, #0x200] | `FALL_THROUGH`
<a id="insn-00bc6f20"></a> `00bc6f20` | `88 00 00 37` | tbnz w8,#0x0,0x00bc6f30 | `CONDITIONAL_JUMP`
<a id="insn-00bc6f24"></a> `00bc6f24` | `c8 02 08 91` | add x8,x22,#0x200 | `FALL_THROUGH`
<a id="insn-00bc6f28"></a> `00bc6f28` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bc6f2c"></a> `00bc6f2c` | `02 00 00 14` | b 0x00bc6f34 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc6f30"></a> `00bc6f30` | `c4 0a 41 f9` | ldr x4,[x22, #0x210] | `FALL_THROUGH`
<a id="insn-00bc6f34"></a> `00bc6f34` | `a2 06 00 d0` | adrp x2,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bc6f38"></a> `00bc6f38` | `42 00 45 f9` | ldr x2,[x2, #0xa00] | `FALL_THROUGH`
<a id="insn-00bc6f3c"></a> `00bc6f3c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc6f40"></a> `00bc6f40` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bc6f44"></a> `00bc6f44` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00bc6f48"></a> `00bc6f48` | `26 54 02 94` | bl 0x00c5bfe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6f4c"></a> `00bc6f4c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bc6f50"></a> `00bc6f50` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bc6f54"></a> `00bc6f54` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc6f58"></a> `00bc6f58` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bc6f5c"></a> `00bc6f5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bc6f60"></a> `00bc6f60` | `e2 a3 00 91` | add x2,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bc6f64"></a> `00bc6f64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc6f68"></a> `00bc6f68` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bc6f6c"></a> `00bc6f6c` | `95 5e 02 94` | bl 0x00c5e9c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6f70"></a> `00bc6f70` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bc6f74"></a> `00bc6f74` | `ef 52 02 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6f78"></a> `00bc6f78` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bc6f7c"></a> `00bc6f7c` | `e9 27 40 f9` | ldr x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bc6f80"></a> `00bc6f80` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bc6f84"></a> `00bc6f84` | `21 01 00 54` | b.ne 0x00bc6fa8 | `CONDITIONAL_JUMP`
<a id="insn-00bc6f88"></a> `00bc6f88` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bc6f8c"></a> `00bc6f8c` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bc6f90"></a> `00bc6f90` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bc6f94"></a> `00bc6f94` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bc6f98"></a> `00bc6f98` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bc6f9c"></a> `00bc6f9c` | `fb 2b 40 f9` | ldr x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc6fa0"></a> `00bc6fa0` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bc6fa4"></a> `00bc6fa4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc6fa8"></a> `00bc6fa8` | `f6 47 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc6dbc`](#insn-00bc6dbc) 範囲 `[['00bc6dbc', '00bc6e57']]`
  - `CONDITIONAL_JUMP` [`00bc6e54`](#insn-00bc6e54) → [`00bc6e90`](#insn-00bc6e90)
  - `FALL_THROUGH` [`00bc6e54`](#insn-00bc6e54) → [`00bc6e58`](#insn-00bc6e58)
- ブロック [`00bc6e58`](#insn-00bc6e58) 範囲 `[['00bc6e58', '00bc6e8f']]`
  - `UNCONDITIONAL_JUMP` [`00bc6e8c`](#insn-00bc6e8c) → [`00bc6f4c`](#insn-00bc6f4c)
- ブロック [`00bc6e90`](#insn-00bc6e90) 範囲 `[['00bc6e90', '00bc6ecf']]`
  - `CONDITIONAL_JUMP` [`00bc6ecc`](#insn-00bc6ecc) → [`00bc6f1c`](#insn-00bc6f1c)
  - `FALL_THROUGH` [`00bc6ecc`](#insn-00bc6ecc) → [`00bc6ed0`](#insn-00bc6ed0)
- ブロック [`00bc6ed0`](#insn-00bc6ed0) 範囲 `[['00bc6ed0', '00bc6edb']]`
  - `CONDITIONAL_JUMP` [`00bc6ed8`](#insn-00bc6ed8) → [`00bc6f10`](#insn-00bc6f10)
  - `FALL_THROUGH` [`00bc6ed8`](#insn-00bc6ed8) → [`00bc6edc`](#insn-00bc6edc)
- ブロック [`00bc6edc`](#insn-00bc6edc) 範囲 `[['00bc6edc', '00bc6ee7']]`
  - `CONDITIONAL_JUMP` [`00bc6ee4`](#insn-00bc6ee4) → [`00bc6efc`](#insn-00bc6efc)
  - `FALL_THROUGH` [`00bc6ee4`](#insn-00bc6ee4) → [`00bc6ee8`](#insn-00bc6ee8)
- ブロック [`00bc6ee8`](#insn-00bc6ee8) 範囲 `[['00bc6ee8', '00bc6ef3']]`
  - `CONDITIONAL_JUMP` [`00bc6ef0`](#insn-00bc6ef0) → [`00bc6f08`](#insn-00bc6f08)
  - `FALL_THROUGH` [`00bc6ef0`](#insn-00bc6ef0) → [`00bc6ef4`](#insn-00bc6ef4)
- ブロック [`00bc6ef4`](#insn-00bc6ef4) 範囲 `[['00bc6ef4', '00bc6efb']]`
  - `CONDITIONAL_JUMP` [`00bc6ef8`](#insn-00bc6ef8) → [`00bc6ee8`](#insn-00bc6ee8)
  - `FALL_THROUGH` [`00bc6ef8`](#insn-00bc6ef8) → [`00bc6efc`](#insn-00bc6efc)
- ブロック [`00bc6efc`](#insn-00bc6efc) 範囲 `[['00bc6efc', '00bc6f07']]`
  - `UNCONDITIONAL_JUMP` [`00bc6f04`](#insn-00bc6f04) → [`00bc6ee8`](#insn-00bc6ee8)
- ブロック [`00bc6f08`](#insn-00bc6f08) 範囲 `[['00bc6f08', '00bc6f0f']]`
  - `UNCONDITIONAL_JUMP` [`00bc6f0c`](#insn-00bc6f0c) → [`00bc6f14`](#insn-00bc6f14)
- ブロック [`00bc6f10`](#insn-00bc6f10) 範囲 `[['00bc6f10', '00bc6f13']]`
  - `FALL_THROUGH` [`00bc6f10`](#insn-00bc6f10) → [`00bc6f14`](#insn-00bc6f14)
- ブロック [`00bc6f14`](#insn-00bc6f14) 範囲 `[['00bc6f14', '00bc6f1b']]`
  - `FALL_THROUGH` [`00bc6f18`](#insn-00bc6f18) → [`00bc6f1c`](#insn-00bc6f1c)
- ブロック [`00bc6f1c`](#insn-00bc6f1c) 範囲 `[['00bc6f1c', '00bc6f23']]`
  - `CONDITIONAL_JUMP` [`00bc6f20`](#insn-00bc6f20) → [`00bc6f30`](#insn-00bc6f30)
  - `FALL_THROUGH` [`00bc6f20`](#insn-00bc6f20) → [`00bc6f24`](#insn-00bc6f24)
- ブロック [`00bc6f24`](#insn-00bc6f24) 範囲 `[['00bc6f24', '00bc6f2f']]`
  - `UNCONDITIONAL_JUMP` [`00bc6f2c`](#insn-00bc6f2c) → [`00bc6f34`](#insn-00bc6f34)
- ブロック [`00bc6f30`](#insn-00bc6f30) 範囲 `[['00bc6f30', '00bc6f33']]`
  - `FALL_THROUGH` [`00bc6f30`](#insn-00bc6f30) → [`00bc6f34`](#insn-00bc6f34)
- ブロック [`00bc6f34`](#insn-00bc6f34) 範囲 `[['00bc6f34', '00bc6f4b']]`
  - `FALL_THROUGH` [`00bc6f48`](#insn-00bc6f48) → [`00bc6f4c`](#insn-00bc6f4c)
- ブロック [`00bc6f4c`](#insn-00bc6f4c) 範囲 `[['00bc6f4c', '00bc6f87']]`
  - `CONDITIONAL_JUMP` [`00bc6f84`](#insn-00bc6f84) → [`00bc6fa8`](#insn-00bc6fa8)
  - `FALL_THROUGH` [`00bc6f84`](#insn-00bc6f84) → [`00bc6f88`](#insn-00bc6f88)
- ブロック [`00bc6f88`](#insn-00bc6f88) 範囲 `[['00bc6f88', '00bc6fa7']]`
- ブロック [`00bc6fa8`](#insn-00bc6fa8) 範囲 `[['00bc6fa8', '00bc6fab']]`

## 命令位置別の参照

- [`00bc6dc0`](#insn-00bc6dc0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6dc4`](#insn-00bc6dc4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6dc8`](#insn-00bc6dc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6dcc`](#insn-00bc6dcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6dd0`](#insn-00bc6dd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6dd4`](#insn-00bc6dd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6df4`](#insn-00bc6df4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6df8`](#insn-00bc6df8) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e00`](#insn-00bc6e00) → `00c9ca30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bc6e00`](#insn-00bc6e00) → [`00bcae58`](../00bca/00bcae58.md) · `PARAM` · `ANALYSIS` · 関数 `00bcae58` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl7DeleteTIbEEvPv` · 推定型 `None`
- [`00bc6e14`](#insn-00bc6e14) → [`00c5bee0`](../00c5b/00c5bee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bee0` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e20`](#insn-00bc6e20) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e28`](#insn-00bc6e28) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e30`](#insn-00bc6e30) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e3c`](#insn-00bc6e3c) → `01127560`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bc6e44`](#insn-00bc6e44) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e50`](#insn-00bc6e50) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e54`](#insn-00bc6e54) → [`00bc6e90`](#insn-00bc6e90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e60`](#insn-00bc6e60) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e68`](#insn-00bc6e68) → `002b48a0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc6e7c`](#insn-00bc6e7c) → [`00c5e9a0`](../00c5e/00c5e9a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e9a0` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e84`](#insn-00bc6e84) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e8c`](#insn-00bc6e8c) → [`00bc6f4c`](#insn-00bc6f4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6e94`](#insn-00bc6e94) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00bc6ea4`](#insn-00bc6ea4) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6ea8`](#insn-00bc6ea8) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6eb4`](#insn-00bc6eb4) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bc6ec4`](#insn-00bc6ec4) → [`00c5ea20`](../00c5e/00c5ea20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ea20` · 推定シンボル `None` · 推定型 `None`
- [`00bc6ec8`](#insn-00bc6ec8) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6ecc`](#insn-00bc6ecc) → [`00bc6f1c`](#insn-00bc6f1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6ed0`](#insn-00bc6ed0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6ed8`](#insn-00bc6ed8) → [`00bc6f10`](#insn-00bc6f10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6ee4`](#insn-00bc6ee4) → [`00bc6efc`](#insn-00bc6efc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6ef0`](#insn-00bc6ef0) → [`00bc6f08`](#insn-00bc6f08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6ef8`](#insn-00bc6ef8) → [`00bc6ee8`](#insn-00bc6ee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f00`](#insn-00bc6f00) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f04`](#insn-00bc6f04) → [`00bc6ee8`](#insn-00bc6ee8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f08`](#insn-00bc6f08) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f0c`](#insn-00bc6f0c) → [`00bc6f14`](#insn-00bc6f14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f14`](#insn-00bc6f14) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f18`](#insn-00bc6f18) → [`00c58f50`](../00c58/00c58f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f50` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f20`](#insn-00bc6f20) → [`00bc6f30`](#insn-00bc6f30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f2c`](#insn-00bc6f2c) → [`00bc6f34`](#insn-00bc6f34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f38`](#insn-00bc6f38) → `00c9ca00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bc6f38`](#insn-00bc6f38) → [`00bc61b0`](00bc61b0.md) · `PARAM` · `ANALYSIS` · 関数 `00bc61b0` · 推定シンボル `_ZN8firebase13remote_config8internal18BoolResultCallbackEP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bc6f48`](#insn-00bc6f48) → [`00c5bfe0`](../00c5b/00c5bfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfe0` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f6c`](#insn-00bc6f6c) → [`00c5e9c0`](../00c5e/00c5e9c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e9c0` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f74`](#insn-00bc6f74) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f7c`](#insn-00bc6f7c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f84`](#insn-00bc6f84) → [`00bc6fa8`](#insn-00bc6fa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f88`](#insn-00bc6f88) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f8c`](#insn-00bc6f8c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f90`](#insn-00bc6f90) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f94`](#insn-00bc6f94) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f98`](#insn-00bc6f98) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6f9c`](#insn-00bc6f9c) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6fa8`](#insn-00bc6fa8) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc6dc0`](#insn-00bc6dc0)

~~~json
{
  "source": "00bc6dc0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6dc4`](#insn-00bc6dc4)

~~~json
{
  "source": "00bc6dc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6dc8`](#insn-00bc6dc8)

~~~json
{
  "source": "00bc6dc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6dcc`](#insn-00bc6dcc)

~~~json
{
  "source": "00bc6dcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6dd0`](#insn-00bc6dd0)

~~~json
{
  "source": "00bc6dd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6dd4`](#insn-00bc6dd4)

~~~json
{
  "source": "00bc6dd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6df4`](#insn-00bc6df4)

~~~json
{
  "source": "00bc6df4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6df8`](#insn-00bc6df8)

~~~json
{
  "source": "00bc6df8",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6e00`](#insn-00bc6e00)

~~~json
{
  "source": "00bc6e00",
  "target": "00c9ca30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca30",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc6e00`](#insn-00bc6e00)

~~~json
{
  "source": "00bc6e00",
  "target": "00bcae58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6e14`](#insn-00bc6e14)

~~~json
{
  "source": "00bc6e14",
  "target": "00c5bee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6e20`](#insn-00bc6e20)

~~~json
{
  "source": "00bc6e20",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6e28`](#insn-00bc6e28)

~~~json
{
  "source": "00bc6e28",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6e30`](#insn-00bc6e30)

~~~json
{
  "source": "00bc6e30",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6e3c`](#insn-00bc6e3c)

~~~json
{
  "source": "00bc6e3c",
  "target": "01127560",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127560",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bc6e44`](#insn-00bc6e44)

~~~json
{
  "source": "00bc6e44",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6e50`](#insn-00bc6e50)

~~~json
{
  "source": "00bc6e50",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6e54`](#insn-00bc6e54)

~~~json
{
  "source": "00bc6e54",
  "target": "00bc6e90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6e60`](#insn-00bc6e60)

~~~json
{
  "source": "00bc6e60",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6e68`](#insn-00bc6e68)

~~~json
{
  "source": "00bc6e68",
  "target": "002b48a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b48a0",
  "offset": 0,
  "size": 39,
  "datatype": "string",
  "bytes": "4665746368416e644163746976617465206e61746976652066756e6374696f6e",
  "capture_start": "002b48a0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bc6e7c`](#insn-00bc6e7c)

~~~json
{
  "source": "00bc6e7c",
  "target": "00c5e9a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6e84`](#insn-00bc6e84)

~~~json
{
  "source": "00bc6e84",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6e8c`](#insn-00bc6e8c)

~~~json
{
  "source": "00bc6e8c",
  "target": "00bc6f4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6e94`](#insn-00bc6e94)

~~~json
{
  "source": "00bc6e94",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6ea4`](#insn-00bc6ea4)

~~~json
{
  "source": "00bc6ea4",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6ea8`](#insn-00bc6ea8)

~~~json
{
  "source": "00bc6ea8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6eb4`](#insn-00bc6eb4)

~~~json
{
  "source": "00bc6eb4",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6ec4`](#insn-00bc6ec4)

~~~json
{
  "source": "00bc6ec4",
  "target": "00c5ea20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6ec8`](#insn-00bc6ec8)

~~~json
{
  "source": "00bc6ec8",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6ecc`](#insn-00bc6ecc)

~~~json
{
  "source": "00bc6ecc",
  "target": "00bc6f1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6ed0`](#insn-00bc6ed0)

~~~json
{
  "source": "00bc6ed0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6ed8`](#insn-00bc6ed8)

~~~json
{
  "source": "00bc6ed8",
  "target": "00bc6f10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6ee4`](#insn-00bc6ee4)

~~~json
{
  "source": "00bc6ee4",
  "target": "00bc6efc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6ef0`](#insn-00bc6ef0)

~~~json
{
  "source": "00bc6ef0",
  "target": "00bc6f08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6ef8`](#insn-00bc6ef8)

~~~json
{
  "source": "00bc6ef8",
  "target": "00bc6ee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f00`](#insn-00bc6f00)

~~~json
{
  "source": "00bc6f00",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6f04`](#insn-00bc6f04)

~~~json
{
  "source": "00bc6f04",
  "target": "00bc6ee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f08`](#insn-00bc6f08)

~~~json
{
  "source": "00bc6f08",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f0c`](#insn-00bc6f0c)

~~~json
{
  "source": "00bc6f0c",
  "target": "00bc6f14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f14`](#insn-00bc6f14)

~~~json
{
  "source": "00bc6f14",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f18`](#insn-00bc6f18)

~~~json
{
  "source": "00bc6f18",
  "target": "00c58f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6f20`](#insn-00bc6f20)

~~~json
{
  "source": "00bc6f20",
  "target": "00bc6f30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f2c`](#insn-00bc6f2c)

~~~json
{
  "source": "00bc6f2c",
  "target": "00bc6f34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f38`](#insn-00bc6f38)

~~~json
{
  "source": "00bc6f38",
  "target": "00c9ca00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ca00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc6f38`](#insn-00bc6f38)

~~~json
{
  "source": "00bc6f38",
  "target": "00bc61b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6f48`](#insn-00bc6f48)

~~~json
{
  "source": "00bc6f48",
  "target": "00c5bfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6f6c`](#insn-00bc6f6c)

~~~json
{
  "source": "00bc6f6c",
  "target": "00c5e9c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6f74`](#insn-00bc6f74)

~~~json
{
  "source": "00bc6f74",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6f7c`](#insn-00bc6f7c)

~~~json
{
  "source": "00bc6f7c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f84`](#insn-00bc6f84)

~~~json
{
  "source": "00bc6f84",
  "target": "00bc6fa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f88`](#insn-00bc6f88)

~~~json
{
  "source": "00bc6f88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f8c`](#insn-00bc6f8c)

~~~json
{
  "source": "00bc6f8c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f90`](#insn-00bc6f90)

~~~json
{
  "source": "00bc6f90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f94`](#insn-00bc6f94)

~~~json
{
  "source": "00bc6f94",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f98`](#insn-00bc6f98)

~~~json
{
  "source": "00bc6f98",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6f9c`](#insn-00bc6f9c)

~~~json
{
  "source": "00bc6f9c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6fa8`](#insn-00bc6fa8)

~~~json
{
  "source": "00bc6fa8",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
