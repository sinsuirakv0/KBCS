# 00bbafa4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b4d248`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b4d/00b4d248.md) · 移動量 `+0x6dd5c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0064.md#compare-a4369f2c73bc3de2bcf4ea8413f26ddc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bbb3cc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bbb/00bbb3cc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-f23c2d3e91b7faf7af3b667ae1d1ffec)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbafa4",
  "name": "_ZN8firebase9messaging9SubscribeEPKc",
  "size": 552,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3439126adee9b63aa92f22cfc892e9716863e313cc4c4d7b91487fda5c837238",
  "source_text_sha256": "3439126adee9b63aa92f22cfc892e9716863e313cc4c4d7b91487fda5c837238",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbafa4",
        "00bbb1cb"
      ]
    ],
    "bytes_sha256": "c0310f1f0d8cda90203f69924f1c4da54220b5f68423cc94966e13dae12f1bf4",
    "instruction_count": 138,
    "instruction_bytes": 552,
    "body_bytes": 552,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb274](../00bbb/00bbb274.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5a690](../00c5a/00c5a690.md)
- [00c5a7e0](../00c5a/00c5a7e0.md)
- [00c5a870](../00c5a/00c5a870.md)
- [00c5a8a0](../00c5a/00c5a8a0.md)
- [00c5a9a0](../00c5a/00c5a9a0.md)
- [00c5a9d0](../00c5a/00c5a9d0.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa40](../00c5a/00c5aa40.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5b1c0](../00c5b/00c5b1c0.md)
- [00c5b860](../00c5b/00c5b860.md)
- [00c5ce70](../00c5c/00c5ce70.md)
- [00c5d1d0](../00c5d/00c5d1d0.md)

## 関連文字列（未確認候補）

~~~text
"Cannot update subscription for unknown reason."
"Cannot update subscription when SetTokenRegistrationOnInitEnabled is set to false."
"Messaging not initialized."
"internal::IsInitialized()"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3640 bytes

~~~c

void _ZN8firebase9messaging9SubscribeEPKc(long param_1,undefined8 param_2)

{
  ulong *puVar1;
  long lVar2;
  undefined8 uVar3;
  long lVar4;
  undefined8 uVar5;
  undefined1 *puVar6;
  undefined1 auStack_b0 [16];
  ulong local_a0;
  ulong uStack_98;
  void *local_90;
  undefined1 auStack_88 [16];
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
  uVar3 = DAT_01125f70;
  puVar6 = auStack_b0;
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  if (DAT_01125f60 == 0) {
    _ZN8firebase8LogErrorEPKcz("internal::IsInitialized()");
    _ZN8firebase9LogAssertEPKcz("Messaging not initialized.");
    _ZN8firebase5MutexC1ENS0_4ModeE(param_1,0);
    *(undefined8 *)(param_1 + 0x28) = 0;
    _ZN8firebase12FutureHandleC1EmPNS_6detail18FutureApiInterfaceE(param_1 + 0x30,0,0);
    goto LAB_00bbb174;
  }
  _ZN8firebase5Mutex7AcquireEv(DAT_01125f70);
  uVar5 = _ZN8firebase9messaging10FutureData3GetEv();
  _ZN8firebase26ReferenceCountedFutureImpl13AllocInternalEiPvPFvS1_E(&local_a0,uVar5,1,0,0);
                    /* catch() { ... } // from try @ 00bbb1ec with catch @ 00bbb010 */
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_68,&local_a0);
  _ZN8firebase12FutureHandleD2Ev(&local_a0);
  lVar4 = DAT_01125f78;
  if (DAT_01126008 == '\x01') {
    FUN_00bbb274(param_2,auStack_68);
  }
  else {
    if (DAT_01126000 == 2) {
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_78,3,
                 "Cannot update subscription when SetTokenRegistrationOnInitEnabled is set to false."
                 ,&local_a0);
      puVar6 = auStack_78;
    }
    else {
      if (DAT_01125f78 != 0) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
                  (&local_a0,param_2);
        _ZN8firebase12FutureHandleC1ERKS0_(auStack_88,auStack_68);
        puVar1 = *(ulong **)(lVar4 + 8);
        if (puVar1 < *(ulong **)(lVar4 + 0x10)) {
          puVar1[2] = (ulong)local_90;
          puVar1[1] = uStack_98;
          *puVar1 = local_a0;
          uStack_98 = 0;
          local_90 = (void *)0x0;
          local_a0 = 0;
          _ZN8firebase12FutureHandleC1EOS0_(puVar1 + 3,auStack_88);
          *(ulong **)(lVar4 + 8) = puVar1 + 5;
        }
        else {
          _ZNSt6__ndk16vectorINS_4pairINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN8firebase16SafeFutureHandleIvEEEENS5_ISB_EEE21__push_back_slow_pathISB_EEvOT_
                    (lVar4,&local_a0);
        }
        _ZN8firebase12FutureHandleD2Ev(auStack_88);
        if ((local_a0 & 1) != 0) {
          _ZdlPv(local_90);
        }
        goto LAB_00bbb154;
      }
      _ZN8firebase12FutureHandleC1ERKS0_(auStack_b0,auStack_68);
      _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
                (uVar5,auStack_b0,4,"Cannot update subscription for unknown reason.",&local_a0);
    }
    _ZN8firebase12FutureHandleD2Ev(puVar6);
  }
LAB_00bbb154:
  _ZN8firebase6FutureIvEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,uVar5,auStack_68);
                    /* try { // try from 00bbb164 to 00cbb1eb has its CatchHandler @ 00bbb2d0 */
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
  _ZN8firebase5Mutex7ReleaseEv(uVar3);
LAB_00bbb174:
  if (*(long *)(lVar2 + 0x28) == local_58) {
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
<a id="insn-00bbafa4"></a> `00bbafa4` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bbafa8"></a> `00bbafa8` | `f9 33 00 f9` | str x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbafac"></a> `00bbafac` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbafb0"></a> `00bbafb0` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbafb4"></a> `00bbafb4` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbafb8"></a> `00bbafb8` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbafbc"></a> `00bbafbc` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbafc0"></a> `00bbafc0` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbafc4"></a> `00bbafc4` | `09 17 40 f9` | ldr x9,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbafc8"></a> `00bbafc8` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00bbafcc"></a> `00bbafcc` | `a9 83 1b f8` | stur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00bbafd0"></a> `00bbafd0` | `49 2b 00 f0` | adrp x9,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbafd4"></a> `00bbafd4` | `29 b1 47 f9` | ldr x9,[x9, #0xf60] | `FALL_THROUGH`
<a id="insn-00bbafd8"></a> `00bbafd8` | `49 03 00 b4` | cbz x9,0x00bbb040 | `CONDITIONAL_JUMP`
<a id="insn-00bbafdc"></a> `00bbafdc` | `48 2b 00 f0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbafe0"></a> `00bbafe0` | `13 b9 47 f9` | ldr x19,[x8, #0xf70] | `FALL_THROUGH`
<a id="insn-00bbafe4"></a> `00bbafe4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbafe8"></a> `00bbafe8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbafec"></a> `00bbafec` | `85 7d 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaff0"></a> `00bbaff0` | `a0 87 02 94` | bl 0x00c5ce70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbaff4"></a> `00bbaff4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbaff8"></a> `00bbaff8` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbaffc"></a> `00bbaffc` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb000"></a> `00bbb000` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbb004"></a> `00bbb004` | `e3 03 1f aa` | mov x3,xzr | `FALL_THROUGH`
<a id="insn-00bbb008"></a> `00bbb008` | `8e 7e 02 94` | bl 0x00c5aa40 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb00c"></a> `00bbb00c` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb010"></a> `00bbb010` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb014"></a> `00bbb014` | `7b 7e 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb018"></a> `00bbb018` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb01c"></a> `00bbb01c` | `9d 7d 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb020"></a> `00bbb020` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbb024"></a> `00bbb024` | `08 21 40 39` | ldrb w8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb028"></a> `00bbb028` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb02c"></a> `00bbb02c` | `81 02 00 54` | b.ne 0x00bbb07c | `CONDITIONAL_JUMP`
<a id="insn-00bbb030"></a> `00bbb030` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb034"></a> `00bbb034` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbb038"></a> `00bbb038` | `8f 00 00 94` | bl 0x00bbb274 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb03c"></a> `00bbb03c` | `46 00 00 14` | b 0x00bbb154 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb040"></a> `00bbb040` | `20 b7 ff f0` | adrp x0,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bbb044"></a> `00bbb044` | `00 20 21 91` | add x0,x0,#0x848 | `FALL_THROUGH`
<a id="insn-00bbb048"></a> `00bbb048` | `16 7e 02 94` | bl 0x00c5a8a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb04c"></a> `00bbb04c` | `a0 b7 ff b0` | adrp x0,0x2b0000 | `FALL_THROUGH`
<a id="insn-00bbb050"></a> `00bbb050` | `00 dc 1c 91` | add x0,x0,#0x737 | `FALL_THROUGH`
<a id="insn-00bbb054"></a> `00bbb054` | `eb 7e 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb058"></a> `00bbb058` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbb05c"></a> `00bbb05c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbb060"></a> `00bbb060` | `04 7e 02 94` | bl 0x00c5a870 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb064"></a> `00bbb064` | `80 c2 00 91` | add x0,x20,#0x30 | `FALL_THROUGH`
<a id="insn-00bbb068"></a> `00bbb068` | `9f 16 00 f9` | str xzr,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb06c"></a> `00bbb06c` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbb070"></a> `00bbb070` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bbb074"></a> `00bbb074` | `db 7d 02 94` | bl 0x00c5a7e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb078"></a> `00bbb078` | `3f 00 00 14` | b 0x00bbb174 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb07c"></a> `00bbb07c` | `48 2b 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbb080"></a> `00bbb080` | `08 01 40 b9` | ldr w8,[x8] | `FALL_THROUGH`
<a id="insn-00bbb084"></a> `00bbb084` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbb088"></a> `00bbb088` | `a1 01 00 54` | b.ne 0x00bbb0bc | `CONDITIONAL_JUMP`
<a id="insn-00bbb08c"></a> `00bbb08c` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbb090"></a> `00bbb090` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb094"></a> `00bbb094` | `5b 7e 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb098"></a> `00bbb098` | `83 ba ff f0` | adrp x3,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbb09c"></a> `00bbb09c` | `63 2c 1e 91` | add x3,x3,#0x78b | `FALL_THROUGH`
<a id="insn-00bbb0a0"></a> `00bbb0a0` | `e1 e3 00 91` | add x1,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbb0a4"></a> `00bbb0a4` | `e4 43 00 91` | add x4,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb0a8"></a> `00bbb0a8` | `62 00 80 52` | mov w2,#0x3 | `FALL_THROUGH`
<a id="insn-00bbb0ac"></a> `00bbb0ac` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbb0b0"></a> `00bbb0b0` | `3c 7e 02 94` | bl 0x00c5a9a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb0b4"></a> `00bbb0b4` | `e0 e3 00 91` | add x0,sp,#0x38 | `FALL_THROUGH`
<a id="insn-00bbb0b8"></a> `00bbb0b8` | `26 00 00 14` | b 0x00bbb150 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb0bc"></a> `00bbb0bc` | `48 2b 00 d0` | adrp x8,0x1125000 | `FALL_THROUGH`
<a id="insn-00bbb0c0"></a> `00bbb0c0` | `17 bd 47 f9` | ldr x23,[x8, #0xf78] | `FALL_THROUGH`
<a id="insn-00bbb0c4"></a> `00bbb0c4` | `17 03 00 b4` | cbz x23,0x00bbb124 | `CONDITIONAL_JUMP`
<a id="insn-00bbb0c8"></a> `00bbb0c8` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb0cc"></a> `00bbb0cc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbb0d0"></a> `00bbb0d0` | `f9 43 00 91` | add x25,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb0d4"></a> `00bbb0d4` | `3b 80 02 94` | bl 0x00c5b1c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb0d8"></a> `00bbb0d8` | `36 63 00 91` | add x22,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00bbb0dc"></a> `00bbb0dc` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb0e0"></a> `00bbb0e0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbb0e4"></a> `00bbb0e4` | `47 7e 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb0e8"></a> `00bbb0e8` | `f9 a2 40 a9` | ldp x25,x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb0ec"></a> `00bbb0ec` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-00bbb0f0"></a> `00bbb0f0` | `82 05 00 54` | b.cs 0x00bbb1a0 | `CONDITIONAL_JUMP`
<a id="insn-00bbb0f4"></a> `00bbb0f4` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbb0f8"></a> `00bbb0f8` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb0fc"></a> `00bbb0fc` | `20 63 00 91` | add x0,x25,#0x18 | `FALL_THROUGH`
<a id="insn-00bbb100"></a> `00bbb100` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbb104"></a> `00bbb104` | `28 0b 00 f9` | str x8,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb108"></a> `00bbb108` | `20 03 80 3d` | str q0,[x25] | `FALL_THROUGH`
<a id="insn-00bbb10c"></a> `00bbb10c` | `ff ff 01 a9` | stp xzr,xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbb110"></a> `00bbb110` | `ff 0b 00 f9` | str xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb114"></a> `00bbb114` | `d3 81 02 94` | bl 0x00c5b860 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb118"></a> `00bbb118` | `28 a3 00 91` | add x8,x25,#0x28 | `FALL_THROUGH`
<a id="insn-00bbb11c"></a> `00bbb11c` | `e8 06 00 f9` | str x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb120"></a> `00bbb120` | `23 00 00 14` | b 0x00bbb1ac | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb124"></a> `00bbb124` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bbb128"></a> `00bbb128` | `e1 23 01 91` | add x1,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb12c"></a> `00bbb12c` | `35 7e 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb130"></a> `00bbb130` | `83 ba ff f0` | adrp x3,0x30e000 | `FALL_THROUGH`
<a id="insn-00bbb134"></a> `00bbb134` | `63 78 1f 91` | add x3,x3,#0x7de | `FALL_THROUGH`
<a id="insn-00bbb138"></a> `00bbb138` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bbb13c"></a> `00bbb13c` | `e4 43 00 91` | add x4,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb140"></a> `00bbb140` | `82 00 80 52` | mov w2,#0x4 | `FALL_THROUGH`
<a id="insn-00bbb144"></a> `00bbb144` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbb148"></a> `00bbb148` | `16 7e 02 94` | bl 0x00c5a9a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb14c"></a> `00bbb14c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bbb150"></a> `00bbb150` | `50 7d 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb154"></a> `00bbb154` | `e2 23 01 91` | add x2,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb158"></a> `00bbb158` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbb15c"></a> `00bbb15c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbb160"></a> `00bbb160` | `1c 7e 02 94` | bl 0x00c5a9d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb164"></a> `00bbb164` | `e0 23 01 91` | add x0,sp,#0x48 | `FALL_THROUGH`
<a id="insn-00bbb168"></a> `00bbb168` | `4a 7d 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb16c"></a> `00bbb16c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbb170"></a> `00bbb170` | `28 7d 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb174"></a> `00bbb174` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb178"></a> `00bbb178` | `a9 83 5b f8` | ldur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00bbb17c"></a> `00bbb17c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbb180"></a> `00bbb180` | `41 02 00 54` | b.ne 0x00bbb1c8 | `CONDITIONAL_JUMP`
<a id="insn-00bbb184"></a> `00bbb184` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbb188"></a> `00bbb188` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbb18c"></a> `00bbb18c` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbb190"></a> `00bbb190` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbb194"></a> `00bbb194` | `f9 33 40 f9` | ldr x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbb198"></a> `00bbb198` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bbb19c"></a> `00bbb19c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbb1a0"></a> `00bbb1a0` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbb1a4"></a> `00bbb1a4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbb1a8"></a> `00bbb1a8` | `0a 88 02 94` | bl 0x00c5d1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb1ac"></a> `00bbb1ac` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bbb1b0"></a> `00bbb1b0` | `38 7d 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb1b4"></a> `00bbb1b4` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbb1b8"></a> `00bbb1b8` | `e8 fc 07 36` | tbz w8,#0x0,0x00bbb154 | `CONDITIONAL_JUMP`
<a id="insn-00bbb1bc"></a> `00bbb1bc` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbb1c0"></a> `00bbb1c0` | `3c 72 02 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbb1c4"></a> `00bbb1c4` | `e4 ff ff 17` | b 0x00bbb154 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb1c8"></a> `00bbb1c8` | `46 72 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbafa4`](#insn-00bbafa4) 範囲 `[['00bbafa4', '00bbafdb']]`
  - `CONDITIONAL_JUMP` [`00bbafd8`](#insn-00bbafd8) → [`00bbb040`](#insn-00bbb040)
  - `FALL_THROUGH` [`00bbafd8`](#insn-00bbafd8) → [`00bbafdc`](#insn-00bbafdc)
- ブロック [`00bbafdc`](#insn-00bbafdc) 範囲 `[['00bbafdc', '00bbb00f']]`
  - `FALL_THROUGH` [`00bbb00c`](#insn-00bbb00c) → [`00bbb010`](#insn-00bbb010)
- ブロック [`00bbb010`](#insn-00bbb010) 範囲 `[['00bbb010', '00bbb02f']]`
  - `CONDITIONAL_JUMP` [`00bbb02c`](#insn-00bbb02c) → [`00bbb07c`](#insn-00bbb07c)
  - `FALL_THROUGH` [`00bbb02c`](#insn-00bbb02c) → [`00bbb030`](#insn-00bbb030)
- ブロック [`00bbb030`](#insn-00bbb030) 範囲 `[['00bbb030', '00bbb03f']]`
  - `UNCONDITIONAL_JUMP` [`00bbb03c`](#insn-00bbb03c) → [`00bbb154`](#insn-00bbb154)
- ブロック [`00bbb040`](#insn-00bbb040) 範囲 `[['00bbb040', '00bbb07b']]`
  - `UNCONDITIONAL_JUMP` [`00bbb078`](#insn-00bbb078) → [`00bbb174`](#insn-00bbb174)
- ブロック [`00bbb07c`](#insn-00bbb07c) 範囲 `[['00bbb07c', '00bbb08b']]`
  - `CONDITIONAL_JUMP` [`00bbb088`](#insn-00bbb088) → [`00bbb0bc`](#insn-00bbb0bc)
  - `FALL_THROUGH` [`00bbb088`](#insn-00bbb088) → [`00bbb08c`](#insn-00bbb08c)
- ブロック [`00bbb08c`](#insn-00bbb08c) 範囲 `[['00bbb08c', '00bbb0bb']]`
  - `UNCONDITIONAL_JUMP` [`00bbb0b8`](#insn-00bbb0b8) → [`00bbb150`](#insn-00bbb150)
- ブロック [`00bbb0bc`](#insn-00bbb0bc) 範囲 `[['00bbb0bc', '00bbb0c7']]`
  - `CONDITIONAL_JUMP` [`00bbb0c4`](#insn-00bbb0c4) → [`00bbb124`](#insn-00bbb124)
  - `FALL_THROUGH` [`00bbb0c4`](#insn-00bbb0c4) → [`00bbb0c8`](#insn-00bbb0c8)
- ブロック [`00bbb0c8`](#insn-00bbb0c8) 範囲 `[['00bbb0c8', '00bbb0f3']]`
  - `CONDITIONAL_JUMP` [`00bbb0f0`](#insn-00bbb0f0) → [`00bbb1a0`](#insn-00bbb1a0)
  - `FALL_THROUGH` [`00bbb0f0`](#insn-00bbb0f0) → [`00bbb0f4`](#insn-00bbb0f4)
- ブロック [`00bbb0f4`](#insn-00bbb0f4) 範囲 `[['00bbb0f4', '00bbb123']]`
  - `UNCONDITIONAL_JUMP` [`00bbb120`](#insn-00bbb120) → [`00bbb1ac`](#insn-00bbb1ac)
- ブロック [`00bbb124`](#insn-00bbb124) 範囲 `[['00bbb124', '00bbb14f']]`
  - `FALL_THROUGH` [`00bbb14c`](#insn-00bbb14c) → [`00bbb150`](#insn-00bbb150)
- ブロック [`00bbb150`](#insn-00bbb150) 範囲 `[['00bbb150', '00bbb153']]`
  - `FALL_THROUGH` [`00bbb150`](#insn-00bbb150) → [`00bbb154`](#insn-00bbb154)
- ブロック [`00bbb154`](#insn-00bbb154) 範囲 `[['00bbb154', '00bbb163']]`
  - `FALL_THROUGH` [`00bbb160`](#insn-00bbb160) → [`00bbb164`](#insn-00bbb164)
- ブロック [`00bbb164`](#insn-00bbb164) 範囲 `[['00bbb164', '00bbb173']]`
  - `FALL_THROUGH` [`00bbb170`](#insn-00bbb170) → [`00bbb174`](#insn-00bbb174)
- ブロック [`00bbb174`](#insn-00bbb174) 範囲 `[['00bbb174', '00bbb183']]`
  - `CONDITIONAL_JUMP` [`00bbb180`](#insn-00bbb180) → [`00bbb1c8`](#insn-00bbb1c8)
  - `FALL_THROUGH` [`00bbb180`](#insn-00bbb180) → [`00bbb184`](#insn-00bbb184)
- ブロック [`00bbb184`](#insn-00bbb184) 範囲 `[['00bbb184', '00bbb19f']]`
- ブロック [`00bbb1a0`](#insn-00bbb1a0) 範囲 `[['00bbb1a0', '00bbb1ab']]`
  - `FALL_THROUGH` [`00bbb1a8`](#insn-00bbb1a8) → [`00bbb1ac`](#insn-00bbb1ac)
- ブロック [`00bbb1ac`](#insn-00bbb1ac) 範囲 `[['00bbb1ac', '00bbb1bb']]`
  - `CONDITIONAL_JUMP` [`00bbb1b8`](#insn-00bbb1b8) → [`00bbb154`](#insn-00bbb154)
  - `FALL_THROUGH` [`00bbb1b8`](#insn-00bbb1b8) → [`00bbb1bc`](#insn-00bbb1bc)
- ブロック [`00bbb1bc`](#insn-00bbb1bc) 範囲 `[['00bbb1bc', '00bbb1c7']]`
  - `UNCONDITIONAL_JUMP` [`00bbb1c4`](#insn-00bbb1c4) → [`00bbb154`](#insn-00bbb154)
- ブロック [`00bbb1c8`](#insn-00bbb1c8) 範囲 `[['00bbb1c8', '00bbb1cb']]`

## 命令位置別の参照

- [`00bbafa8`](#insn-00bbafa8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafac`](#insn-00bbafac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafb0`](#insn-00bbafb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafb4`](#insn-00bbafb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafb8`](#insn-00bbafb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafcc`](#insn-00bbafcc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafd4`](#insn-00bbafd4) → `01125f60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbafd8`](#insn-00bbafd8) → [`00bbb040`](#insn-00bbb040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbafe0`](#insn-00bbafe0) → `01125f70`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbafec`](#insn-00bbafec) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bbaff0`](#insn-00bbaff0) → [`00c5ce70`](../00c5c/00c5ce70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ce70` · 推定シンボル `None` · 推定型 `None`
- [`00bbb008`](#insn-00bbb008) → [`00c5aa40`](../00c5a/00c5aa40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa40` · 推定シンボル `None` · 推定型 `None`
- [`00bbb014`](#insn-00bbb014) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbb01c`](#insn-00bbb01c) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bbb024`](#insn-00bbb024) → `01126008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbb02c`](#insn-00bbb02c) → [`00bbb07c`](#insn-00bbb07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb038`](#insn-00bbb038) → [`00bbb274`](../00bbb/00bbb274.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb274` · 推定シンボル `None` · 推定型 `None`
- [`00bbb03c`](#insn-00bbb03c) → [`00bbb154`](#insn-00bbb154) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb044`](#insn-00bbb044) → `002a2848`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb048`](#insn-00bbb048) → [`00c5a8a0`](../00c5a/00c5a8a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a8a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb050`](#insn-00bbb050) → `002b0737`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb054`](#insn-00bbb054) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bbb060`](#insn-00bbb060) → [`00c5a870`](../00c5a/00c5a870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a870` · 推定シンボル `None` · 推定型 `None`
- [`00bbb074`](#insn-00bbb074) → [`00c5a7e0`](../00c5a/00c5a7e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a7e0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb078`](#insn-00bbb078) → [`00bbb174`](#insn-00bbb174) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb080`](#insn-00bbb080) → `01126000`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00bbb088`](#insn-00bbb088) → [`00bbb0bc`](#insn-00bbb0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb094`](#insn-00bbb094) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbb09c`](#insn-00bbb09c) → `0030e78b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb0b0`](#insn-00bbb0b0) → [`00c5a9a0`](../00c5a/00c5a9a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a9a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0b8`](#insn-00bbb0b8) → [`00bbb150`](#insn-00bbb150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0c0`](#insn-00bbb0c0) → `01125f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bbb0c4`](#insn-00bbb0c4) → [`00bbb124`](#insn-00bbb124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0d4`](#insn-00bbb0d4) → [`00c5b1c0`](../00c5b/00c5b1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0e4`](#insn-00bbb0e4) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0f0`](#insn-00bbb0f0) → [`00bbb1a0`](#insn-00bbb1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0f4`](#insn-00bbb0f4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb0f8`](#insn-00bbb0f8) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb10c`](#insn-00bbb10c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb110`](#insn-00bbb110) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb114`](#insn-00bbb114) → [`00c5b860`](../00c5b/00c5b860.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b860` · 推定シンボル `None` · 推定型 `None`
- [`00bbb120`](#insn-00bbb120) → [`00bbb1ac`](#insn-00bbb1ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb12c`](#insn-00bbb12c) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbb134`](#insn-00bbb134) → `0030e7de`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbb148`](#insn-00bbb148) → [`00c5a9a0`](../00c5a/00c5a9a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a9a0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb150`](#insn-00bbb150) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bbb160`](#insn-00bbb160) → [`00c5a9d0`](../00c5a/00c5a9d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a9d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb168`](#insn-00bbb168) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bbb170`](#insn-00bbb170) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bbb178`](#insn-00bbb178) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb180`](#insn-00bbb180) → [`00bbb1c8`](#insn-00bbb1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb184`](#insn-00bbb184) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb188`](#insn-00bbb188) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb18c`](#insn-00bbb18c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb190`](#insn-00bbb190) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb194`](#insn-00bbb194) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1a8`](#insn-00bbb1a8) → [`00c5d1d0`](../00c5d/00c5d1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1b0`](#insn-00bbb1b0) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1b4`](#insn-00bbb1b4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1b8`](#insn-00bbb1b8) → [`00bbb154`](#insn-00bbb154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1bc`](#insn-00bbb1bc) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1c0`](#insn-00bbb1c0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1c4`](#insn-00bbb1c4) → [`00bbb154`](#insn-00bbb154) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb1c8`](#insn-00bbb1c8) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbafa8`](#insn-00bbafa8)

~~~json
{
  "source": "00bbafa8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafac`](#insn-00bbafac)

~~~json
{
  "source": "00bbafac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafb0`](#insn-00bbafb0)

~~~json
{
  "source": "00bbafb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafb4`](#insn-00bbafb4)

~~~json
{
  "source": "00bbafb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafb8`](#insn-00bbafb8)

~~~json
{
  "source": "00bbafb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafcc`](#insn-00bbafcc)

~~~json
{
  "source": "00bbafcc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafd4`](#insn-00bbafd4)

~~~json
{
  "source": "00bbafd4",
  "target": "01125f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbafd8`](#insn-00bbafd8)

~~~json
{
  "source": "00bbafd8",
  "target": "00bbb040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbafe0`](#insn-00bbafe0)

~~~json
{
  "source": "00bbafe0",
  "target": "01125f70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbafec`](#insn-00bbafec)

~~~json
{
  "source": "00bbafec",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbaff0`](#insn-00bbaff0)

~~~json
{
  "source": "00bbaff0",
  "target": "00c5ce70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb008`](#insn-00bbb008)

~~~json
{
  "source": "00bbb008",
  "target": "00c5aa40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb014`](#insn-00bbb014)

~~~json
{
  "source": "00bbb014",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb01c`](#insn-00bbb01c)

~~~json
{
  "source": "00bbb01c",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb024`](#insn-00bbb024)

~~~json
{
  "source": "00bbb024",
  "target": "01126008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126008",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb02c`](#insn-00bbb02c)

~~~json
{
  "source": "00bbb02c",
  "target": "00bbb07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb038`](#insn-00bbb038)

~~~json
{
  "source": "00bbb038",
  "target": "00bbb274",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb03c`](#insn-00bbb03c)

~~~json
{
  "source": "00bbb03c",
  "target": "00bbb154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb044`](#insn-00bbb044)

~~~json
{
  "source": "00bbb044",
  "target": "002a2848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2848",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "696e7465726e616c3a3a4973496e697469616c697a6564282900",
  "capture_start": "002a2848",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbb048`](#insn-00bbb048)

~~~json
{
  "source": "00bbb048",
  "target": "00c5a8a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb050`](#insn-00bbb050)

~~~json
{
  "source": "00bbb050",
  "target": "002b0737",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b0737",
  "offset": 0,
  "size": 27,
  "datatype": "string",
  "bytes": "4d6573736167696e67206e6f7420696e697469616c697a65642e00",
  "capture_start": "002b0737",
  "capture_bytes": 27,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbb054`](#insn-00bbb054)

~~~json
{
  "source": "00bbb054",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb060`](#insn-00bbb060)

~~~json
{
  "source": "00bbb060",
  "target": "00c5a870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb074`](#insn-00bbb074)

~~~json
{
  "source": "00bbb074",
  "target": "00c5a7e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb078`](#insn-00bbb078)

~~~json
{
  "source": "00bbb078",
  "target": "00bbb174",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb080`](#insn-00bbb080)

~~~json
{
  "source": "00bbb080",
  "target": "01126000",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126000",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb088`](#insn-00bbb088)

~~~json
{
  "source": "00bbb088",
  "target": "00bbb0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb094`](#insn-00bbb094)

~~~json
{
  "source": "00bbb094",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb09c`](#insn-00bbb09c)

~~~json
{
  "source": "00bbb09c",
  "target": "0030e78b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e78b",
  "offset": 0,
  "size": 83,
  "datatype": "string",
  "bytes": "43616e6e6f742075706461746520737562736372697074696f6e207768656e20",
  "capture_start": "0030e78b",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbb0b0`](#insn-00bbb0b0)

~~~json
{
  "source": "00bbb0b0",
  "target": "00c5a9a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb0b8`](#insn-00bbb0b8)

~~~json
{
  "source": "00bbb0b8",
  "target": "00bbb150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb0c0`](#insn-00bbb0c0)

~~~json
{
  "source": "00bbb0c0",
  "target": "01125f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01125f78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bbb0c4`](#insn-00bbb0c4)

~~~json
{
  "source": "00bbb0c4",
  "target": "00bbb124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb0d4`](#insn-00bbb0d4)

~~~json
{
  "source": "00bbb0d4",
  "target": "00c5b1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb0e4`](#insn-00bbb0e4)

~~~json
{
  "source": "00bbb0e4",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb0f0`](#insn-00bbb0f0)

~~~json
{
  "source": "00bbb0f0",
  "target": "00bbb1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb0f4`](#insn-00bbb0f4)

~~~json
{
  "source": "00bbb0f4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb0f8`](#insn-00bbb0f8)

~~~json
{
  "source": "00bbb0f8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb10c`](#insn-00bbb10c)

~~~json
{
  "source": "00bbb10c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb110`](#insn-00bbb110)

~~~json
{
  "source": "00bbb110",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb114`](#insn-00bbb114)

~~~json
{
  "source": "00bbb114",
  "target": "00c5b860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb120`](#insn-00bbb120)

~~~json
{
  "source": "00bbb120",
  "target": "00bbb1ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb12c`](#insn-00bbb12c)

~~~json
{
  "source": "00bbb12c",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb134`](#insn-00bbb134)

~~~json
{
  "source": "00bbb134",
  "target": "0030e7de",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0030e7de",
  "offset": 0,
  "size": 47,
  "datatype": "string",
  "bytes": "43616e6e6f742075706461746520737562736372697074696f6e20666f722075",
  "capture_start": "0030e7de",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbb148`](#insn-00bbb148)

~~~json
{
  "source": "00bbb148",
  "target": "00c5a9a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb150`](#insn-00bbb150)

~~~json
{
  "source": "00bbb150",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb160`](#insn-00bbb160)

~~~json
{
  "source": "00bbb160",
  "target": "00c5a9d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb168`](#insn-00bbb168)

~~~json
{
  "source": "00bbb168",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb170`](#insn-00bbb170)

~~~json
{
  "source": "00bbb170",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb178`](#insn-00bbb178)

~~~json
{
  "source": "00bbb178",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb180`](#insn-00bbb180)

~~~json
{
  "source": "00bbb180",
  "target": "00bbb1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb184`](#insn-00bbb184)

~~~json
{
  "source": "00bbb184",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb188`](#insn-00bbb188)

~~~json
{
  "source": "00bbb188",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb18c`](#insn-00bbb18c)

~~~json
{
  "source": "00bbb18c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb190`](#insn-00bbb190)

~~~json
{
  "source": "00bbb190",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb194`](#insn-00bbb194)

~~~json
{
  "source": "00bbb194",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1a8`](#insn-00bbb1a8)

~~~json
{
  "source": "00bbb1a8",
  "target": "00c5d1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb1b0`](#insn-00bbb1b0)

~~~json
{
  "source": "00bbb1b0",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb1b4`](#insn-00bbb1b4)

~~~json
{
  "source": "00bbb1b4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1b8`](#insn-00bbb1b8)

~~~json
{
  "source": "00bbb1b8",
  "target": "00bbb154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1bc`](#insn-00bbb1bc)

~~~json
{
  "source": "00bbb1bc",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1c0`](#insn-00bbb1c0)

~~~json
{
  "source": "00bbb1c0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbb1c4`](#insn-00bbb1c4)

~~~json
{
  "source": "00bbb1c4",
  "target": "00bbb154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb1c8`](#insn-00bbb1c8)

~~~json
{
  "source": "00bbb1c8",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
