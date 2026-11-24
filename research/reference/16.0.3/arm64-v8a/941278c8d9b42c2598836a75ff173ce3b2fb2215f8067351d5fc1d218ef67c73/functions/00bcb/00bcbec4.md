# 00bcbec4

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcaed0`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bca/00bcaed0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-db094e18973a806cf209e09db37ae581)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbec4",
  "name": "_ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "39ca2dbe07b691bb668a63215a3f1fcff553652631c68dd0cacee5226a7e9063",
  "source_text_sha256": "39ca2dbe07b691bb668a63215a3f1fcff553652631c68dd0cacee5226a7e9063",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbec4",
        "00bcc077"
      ]
    ],
    "bytes_sha256": "93bd1add3fd73627fc1824d20e99b957265c0c875aaf4daf611d5963e23e72e3",
    "instruction_count": 109,
    "instruction_bytes": 436,
    "body_bytes": 436,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f80](../00c58/00c58f80.md)
- [00c5baa0](../00c5b/00c5baa0.md)
- [00c5bab0](../00c5b/00c5bab0.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5eb90](../00c5e/00c5eb90.md)
- [00c5ebb0](../00c5e/00c5ebb0.md)

## 関連文字列（未確認候補）

~~~text
"listener_added == auth_added"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2525 bytes

~~~c

void _ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE
               (long *param_1,long *param_2)

{
  long *plVar1;
  undefined8 *puVar2;
  long lVar3;
  undefined8 *puVar4;
  long lVar5;
  bool bVar6;
  long lVar7;
  long *plVar8;
  undefined8 *puVar9;
  long *plVar10;
  long *local_58;
  long *plStack_50;
  long local_48;
  
  lVar5 = tpidr_el0;
  local_48 = *(long *)(lVar5 + 0x28);
  if (*param_1 == 0) goto LAB_00bcc04c;
  lVar3 = *param_1 + 0x268;
  _ZN8firebase5Mutex7AcquireEv(lVar3);
  lVar7 = *param_1;
  plVar10 = *(long **)(lVar7 + 0x230);
  plVar8 = *(long **)(lVar7 + 0x238);
  local_58 = param_1;
  plStack_50 = param_2;
  if ((plVar10 == plVar8) || ((long *)*plVar10 == param_2)) {
    if (plVar10 == plVar8) goto LAB_00bcbf64;
LAB_00bcbf50:
    bVar6 = false;
  }
  else {
    do {
      if (plVar8 + -1 == plVar10) goto LAB_00bcbf64;
      plVar1 = plVar10 + 1;
      plVar10 = plVar10 + 1;
    } while ((long *)*plVar1 != param_2);
    if (plVar10 != plVar8) goto LAB_00bcbf50;
LAB_00bcbf64:
    if (plVar8 == *(long **)(lVar7 + 0x240)) {
      _ZNSt6__ndk16vectorIPN8firebase4auth17AuthStateListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (lVar7 + 0x230,&plStack_50);
    }
    else {
      *plVar8 = (long)param_2;
      *(long **)(lVar7 + 0x238) = plVar8 + 1;
    }
    bVar6 = true;
  }
  puVar9 = (undefined8 *)param_2[1];
  puVar4 = (undefined8 *)param_2[2];
  if ((puVar9 == puVar4) || ((long *)*puVar9 == local_58)) {
    if (puVar9 == puVar4) goto LAB_00bcbfe4;
LAB_00bcbfd0:
    if (bVar6) {
LAB_00bcc038:
      _ZN8firebase9LogAssertEPKcz("listener_added == auth_added");
    }
  }
  else {
    do {
      if (puVar4 + -1 == puVar9) goto LAB_00bcbfe4;
      puVar2 = puVar9 + 1;
      puVar9 = puVar9 + 1;
    } while ((long *)*puVar2 != local_58);
    if (puVar9 != puVar4) goto LAB_00bcbfd0;
LAB_00bcbfe4:
    if (puVar4 == (undefined8 *)param_2[3]) {
      _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (param_2 + 1,&local_58);
    }
    else {
      *puVar4 = local_58;
      param_2[2] = (long)(puVar4 + 1);
    }
    if (!bVar6) goto LAB_00bcc038;
    if (*(char *)(*param_1 + 0x2b9) == '\0') {
      (**(code **)(*param_2 + 0x10))(param_2,param_1);
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar3);
LAB_00bcc04c:
  if (*(long *)(lVar5 + 0x28) == local_48) {
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
<a id="insn-00bcbec4"></a> `00bcbec4` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcbec8"></a> `00bcbec8` | `f7 13 00 f9` | str x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbecc"></a> `00bcbecc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcbed0"></a> `00bcbed0` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcbed4"></a> `00bcbed4` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcbed8"></a> `00bcbed8` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bcbedc"></a> `00bcbedc` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcbee0"></a> `00bcbee0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcbee4"></a> `00bcbee4` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcbee8"></a> `00bcbee8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbeec"></a> `00bcbeec` | `08 0b 00 b4` | cbz x8,0x00bcc04c | `CONDITIONAL_JUMP`
<a id="insn-00bcbef0"></a> `00bcbef0` | `13 a1 09 91` | add x19,x8,#0x268 | `FALL_THROUGH`
<a id="insn-00bcbef4"></a> `00bcbef4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcbef8"></a> `00bcbef8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbefc"></a> `00bcbefc` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bcbf00"></a> `00bcbf00` | `e8 3e 02 94` | bl 0x00c5baa0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbf04"></a> `00bcbf04` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcbf08"></a> `00bcbf08` | `f4 d7 00 a9` | stp x20,x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf0c"></a> `00bcbf0c` | `0a 19 41 f9` | ldr x10,[x8, #0x230] | `FALL_THROUGH`
<a id="insn-00bcbf10"></a> `00bcbf10` | `09 1d 41 f9` | ldr x9,[x8, #0x238] | `FALL_THROUGH`
<a id="insn-00bcbf14"></a> `00bcbf14` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbf18"></a> `00bcbf18` | `00 02 00 54` | b.eq 0x00bcbf58 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf1c"></a> `00bcbf1c` | `4b 01 40 f9` | ldr x11,[x10] | `FALL_THROUGH`
<a id="insn-00bcbf20"></a> `00bcbf20` | `7f 01 15 eb` | cmp x11,x21 | `FALL_THROUGH`
<a id="insn-00bcbf24"></a> `00bcbf24` | `a0 01 00 54` | b.eq 0x00bcbf58 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf28"></a> `00bcbf28` | `2b 21 00 d1` | sub x11,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcbf2c"></a> `00bcbf2c` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcbf30"></a> `00bcbf30` | `a0 01 00 54` | b.eq 0x00bcbf64 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf34"></a> `00bcbf34` | `4d 05 40 f9` | ldr x13,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf38"></a> `00bcbf38` | `4c 21 00 91` | add x12,x10,#0x8 | `FALL_THROUGH`
<a id="insn-00bcbf3c"></a> `00bcbf3c` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bcbf40"></a> `00bcbf40` | `bf 01 15 eb` | cmp x13,x21 | `FALL_THROUGH`
<a id="insn-00bcbf44"></a> `00bcbf44` | `41 ff ff 54` | b.ne 0x00bcbf2c | `CONDITIONAL_JUMP`
<a id="insn-00bcbf48"></a> `00bcbf48` | `9f 01 09 eb` | cmp x12,x9 | `FALL_THROUGH`
<a id="insn-00bcbf4c"></a> `00bcbf4c` | `c0 00 00 54` | b.eq 0x00bcbf64 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf50"></a> `00bcbf50` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00bcbf54"></a> `00bcbf54` | `0e 00 00 14` | b 0x00bcbf8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbf58"></a> `00bcbf58` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00bcbf5c"></a> `00bcbf5c` | `9f 01 09 eb` | cmp x12,x9 | `FALL_THROUGH`
<a id="insn-00bcbf60"></a> `00bcbf60` | `81 ff ff 54` | b.ne 0x00bcbf50 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf64"></a> `00bcbf64` | `0a 21 41 f9` | ldr x10,[x8, #0x240] | `FALL_THROUGH`
<a id="insn-00bcbf68"></a> `00bcbf68` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcbf6c"></a> `00bcbf6c` | `80 00 00 54` | b.eq 0x00bcbf7c | `CONDITIONAL_JUMP`
<a id="insn-00bcbf70"></a> `00bcbf70` | `35 85 00 f8` | str x21,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-00bcbf74"></a> `00bcbf74` | `09 1d 01 f9` | str x9,[x8, #0x238] | `FALL_THROUGH`
<a id="insn-00bcbf78"></a> `00bcbf78` | `04 00 00 14` | b 0x00bcbf88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbf7c"></a> `00bcbf7c` | `00 c1 08 91` | add x0,x8,#0x230 | `FALL_THROUGH`
<a id="insn-00bcbf80"></a> `00bcbf80` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcbf84"></a> `00bcbf84` | `03 4b 02 94` | bl 0x00c5eb90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbf88"></a> `00bcbf88` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbf8c"></a> `00bcbf8c` | `a9 a2 40 a9` | ldp x9,x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf90"></a> `00bcbf90` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbf94"></a> `00bcbf94` | `20 02 00 54` | b.eq 0x00bcbfd8 | `CONDITIONAL_JUMP`
<a id="insn-00bcbf98"></a> `00bcbf98` | `ea 07 40 f9` | ldr x10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbf9c"></a> `00bcbf9c` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bcbfa0"></a> `00bcbfa0` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcbfa4"></a> `00bcbfa4` | `a0 01 00 54` | b.eq 0x00bcbfd8 | `CONDITIONAL_JUMP`
<a id="insn-00bcbfa8"></a> `00bcbfa8` | `0b 21 00 d1` | sub x11,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcbfac"></a> `00bcbfac` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00bcbfb0"></a> `00bcbfb0` | `a0 01 00 54` | b.eq 0x00bcbfe4 | `CONDITIONAL_JUMP`
<a id="insn-00bcbfb4"></a> `00bcbfb4` | `2d 05 40 f9` | ldr x13,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbfb8"></a> `00bcbfb8` | `2c 21 00 91` | add x12,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcbfbc"></a> `00bcbfbc` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bcbfc0"></a> `00bcbfc0` | `bf 01 0a eb` | cmp x13,x10 | `FALL_THROUGH`
<a id="insn-00bcbfc4"></a> `00bcbfc4` | `41 ff ff 54` | b.ne 0x00bcbfac | `CONDITIONAL_JUMP`
<a id="insn-00bcbfc8"></a> `00bcbfc8` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bcbfcc"></a> `00bcbfcc` | `c0 00 00 54` | b.eq 0x00bcbfe4 | `CONDITIONAL_JUMP`
<a id="insn-00bcbfd0"></a> `00bcbfd0` | `57 03 00 35` | cbnz w23,0x00bcc038 | `CONDITIONAL_JUMP`
<a id="insn-00bcbfd4"></a> `00bcbfd4` | `1c 00 00 14` | b 0x00bcc044 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcbfd8"></a> `00bcbfd8` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bcbfdc"></a> `00bcbfdc` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bcbfe0"></a> `00bcbfe0` | `81 ff ff 54` | b.ne 0x00bcbfd0 | `CONDITIONAL_JUMP`
<a id="insn-00bcbfe4"></a> `00bcbfe4` | `a9 0e 40 f9` | ldr x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bcbfe8"></a> `00bcbfe8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcbfec"></a> `00bcbfec` | `c0 00 00 54` | b.eq 0x00bcc004 | `CONDITIONAL_JUMP`
<a id="insn-00bcbff0"></a> `00bcbff0` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbff4"></a> `00bcbff4` | `09 85 00 f8` | str x9,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-00bcbff8"></a> `00bcbff8` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbffc"></a> `00bcbffc` | `d7 00 00 37` | tbnz w23,#0x0,0x00bcc014 | `CONDITIONAL_JUMP`
<a id="insn-00bcc000"></a> `00bcc000` | `0e 00 00 14` | b 0x00bcc038 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcc004"></a> `00bcc004` | `a0 22 00 91` | add x0,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bcc008"></a> `00bcc008` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcc00c"></a> `00bcc00c` | `e9 4a 02 94` | bl 0x00c5ebb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc010"></a> `00bcc010` | `57 01 00 36` | tbz w23,#0x0,0x00bcc038 | `CONDITIONAL_JUMP`
<a id="insn-00bcc014"></a> `00bcc014` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcc018"></a> `00bcc018` | `08 e5 4a 39` | ldrb w8,[x8, #0x2b9] | `FALL_THROUGH`
<a id="insn-00bcc01c"></a> `00bcc01c` | `48 01 00 35` | cbnz w8,0x00bcc044 | `CONDITIONAL_JUMP`
<a id="insn-00bcc020"></a> `00bcc020` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcc024"></a> `00bcc024` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bcc028"></a> `00bcc028` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcc02c"></a> `00bcc02c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcc030"></a> `00bcc030` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcc034"></a> `00bcc034` | `04 00 00 14` | b 0x00bcc044 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcc038"></a> `00bcc038` | `60 b7 ff 90` | adrp x0,0x2b8000 | `FALL_THROUGH`
<a id="insn-00bcc03c"></a> `00bcc03c` | `00 9c 33 91` | add x0,x0,#0xce7 | `FALL_THROUGH`
<a id="insn-00bcc040"></a> `00bcc040` | `18 40 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc044"></a> `00bcc044` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcc048"></a> `00bcc048` | `9a 3e 02 94` | bl 0x00c5bab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcc04c"></a> `00bcc04c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcc050"></a> `00bcc050` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcc054"></a> `00bcc054` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcc058"></a> `00bcc058` | `e1 00 00 54` | b.ne 0x00bcc074 | `CONDITIONAL_JUMP`
<a id="insn-00bcc05c"></a> `00bcc05c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcc060"></a> `00bcc060` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcc064"></a> `00bcc064` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcc068"></a> `00bcc068` | `f7 13 40 f9` | ldr x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcc06c"></a> `00bcc06c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcc070"></a> `00bcc070` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcc074"></a> `00bcc074` | `c3 33 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbec4`](#insn-00bcbec4) 範囲 `[['00bcbec4', '00bcbeef']]`
  - `CONDITIONAL_JUMP` [`00bcbeec`](#insn-00bcbeec) → [`00bcc04c`](#insn-00bcc04c)
  - `FALL_THROUGH` [`00bcbeec`](#insn-00bcbeec) → [`00bcbef0`](#insn-00bcbef0)
- ブロック [`00bcbef0`](#insn-00bcbef0) 範囲 `[['00bcbef0', '00bcbf1b']]`
  - `CONDITIONAL_JUMP` [`00bcbf18`](#insn-00bcbf18) → [`00bcbf58`](#insn-00bcbf58)
  - `FALL_THROUGH` [`00bcbf18`](#insn-00bcbf18) → [`00bcbf1c`](#insn-00bcbf1c)
- ブロック [`00bcbf1c`](#insn-00bcbf1c) 範囲 `[['00bcbf1c', '00bcbf27']]`
  - `CONDITIONAL_JUMP` [`00bcbf24`](#insn-00bcbf24) → [`00bcbf58`](#insn-00bcbf58)
  - `FALL_THROUGH` [`00bcbf24`](#insn-00bcbf24) → [`00bcbf28`](#insn-00bcbf28)
- ブロック [`00bcbf28`](#insn-00bcbf28) 範囲 `[['00bcbf28', '00bcbf2b']]`
  - `FALL_THROUGH` [`00bcbf28`](#insn-00bcbf28) → [`00bcbf2c`](#insn-00bcbf2c)
- ブロック [`00bcbf2c`](#insn-00bcbf2c) 範囲 `[['00bcbf2c', '00bcbf33']]`
  - `CONDITIONAL_JUMP` [`00bcbf30`](#insn-00bcbf30) → [`00bcbf64`](#insn-00bcbf64)
  - `FALL_THROUGH` [`00bcbf30`](#insn-00bcbf30) → [`00bcbf34`](#insn-00bcbf34)
- ブロック [`00bcbf34`](#insn-00bcbf34) 範囲 `[['00bcbf34', '00bcbf47']]`
  - `CONDITIONAL_JUMP` [`00bcbf44`](#insn-00bcbf44) → [`00bcbf2c`](#insn-00bcbf2c)
  - `FALL_THROUGH` [`00bcbf44`](#insn-00bcbf44) → [`00bcbf48`](#insn-00bcbf48)
- ブロック [`00bcbf48`](#insn-00bcbf48) 範囲 `[['00bcbf48', '00bcbf4f']]`
  - `CONDITIONAL_JUMP` [`00bcbf4c`](#insn-00bcbf4c) → [`00bcbf64`](#insn-00bcbf64)
  - `FALL_THROUGH` [`00bcbf4c`](#insn-00bcbf4c) → [`00bcbf50`](#insn-00bcbf50)
- ブロック [`00bcbf50`](#insn-00bcbf50) 範囲 `[['00bcbf50', '00bcbf57']]`
  - `UNCONDITIONAL_JUMP` [`00bcbf54`](#insn-00bcbf54) → [`00bcbf8c`](#insn-00bcbf8c)
- ブロック [`00bcbf58`](#insn-00bcbf58) 範囲 `[['00bcbf58', '00bcbf63']]`
  - `CONDITIONAL_JUMP` [`00bcbf60`](#insn-00bcbf60) → [`00bcbf50`](#insn-00bcbf50)
  - `FALL_THROUGH` [`00bcbf60`](#insn-00bcbf60) → [`00bcbf64`](#insn-00bcbf64)
- ブロック [`00bcbf64`](#insn-00bcbf64) 範囲 `[['00bcbf64', '00bcbf6f']]`
  - `CONDITIONAL_JUMP` [`00bcbf6c`](#insn-00bcbf6c) → [`00bcbf7c`](#insn-00bcbf7c)
  - `FALL_THROUGH` [`00bcbf6c`](#insn-00bcbf6c) → [`00bcbf70`](#insn-00bcbf70)
- ブロック [`00bcbf70`](#insn-00bcbf70) 範囲 `[['00bcbf70', '00bcbf7b']]`
  - `UNCONDITIONAL_JUMP` [`00bcbf78`](#insn-00bcbf78) → [`00bcbf88`](#insn-00bcbf88)
- ブロック [`00bcbf7c`](#insn-00bcbf7c) 範囲 `[['00bcbf7c', '00bcbf87']]`
  - `FALL_THROUGH` [`00bcbf84`](#insn-00bcbf84) → [`00bcbf88`](#insn-00bcbf88)
- ブロック [`00bcbf88`](#insn-00bcbf88) 範囲 `[['00bcbf88', '00bcbf8b']]`
  - `FALL_THROUGH` [`00bcbf88`](#insn-00bcbf88) → [`00bcbf8c`](#insn-00bcbf8c)
- ブロック [`00bcbf8c`](#insn-00bcbf8c) 範囲 `[['00bcbf8c', '00bcbf97']]`
  - `CONDITIONAL_JUMP` [`00bcbf94`](#insn-00bcbf94) → [`00bcbfd8`](#insn-00bcbfd8)
  - `FALL_THROUGH` [`00bcbf94`](#insn-00bcbf94) → [`00bcbf98`](#insn-00bcbf98)
- ブロック [`00bcbf98`](#insn-00bcbf98) 範囲 `[['00bcbf98', '00bcbfa7']]`
  - `CONDITIONAL_JUMP` [`00bcbfa4`](#insn-00bcbfa4) → [`00bcbfd8`](#insn-00bcbfd8)
  - `FALL_THROUGH` [`00bcbfa4`](#insn-00bcbfa4) → [`00bcbfa8`](#insn-00bcbfa8)
- ブロック [`00bcbfa8`](#insn-00bcbfa8) 範囲 `[['00bcbfa8', '00bcbfab']]`
  - `FALL_THROUGH` [`00bcbfa8`](#insn-00bcbfa8) → [`00bcbfac`](#insn-00bcbfac)
- ブロック [`00bcbfac`](#insn-00bcbfac) 範囲 `[['00bcbfac', '00bcbfb3']]`
  - `CONDITIONAL_JUMP` [`00bcbfb0`](#insn-00bcbfb0) → [`00bcbfe4`](#insn-00bcbfe4)
  - `FALL_THROUGH` [`00bcbfb0`](#insn-00bcbfb0) → [`00bcbfb4`](#insn-00bcbfb4)
- ブロック [`00bcbfb4`](#insn-00bcbfb4) 範囲 `[['00bcbfb4', '00bcbfc7']]`
  - `CONDITIONAL_JUMP` [`00bcbfc4`](#insn-00bcbfc4) → [`00bcbfac`](#insn-00bcbfac)
  - `FALL_THROUGH` [`00bcbfc4`](#insn-00bcbfc4) → [`00bcbfc8`](#insn-00bcbfc8)
- ブロック [`00bcbfc8`](#insn-00bcbfc8) 範囲 `[['00bcbfc8', '00bcbfcf']]`
  - `CONDITIONAL_JUMP` [`00bcbfcc`](#insn-00bcbfcc) → [`00bcbfe4`](#insn-00bcbfe4)
  - `FALL_THROUGH` [`00bcbfcc`](#insn-00bcbfcc) → [`00bcbfd0`](#insn-00bcbfd0)
- ブロック [`00bcbfd0`](#insn-00bcbfd0) 範囲 `[['00bcbfd0', '00bcbfd3']]`
  - `CONDITIONAL_JUMP` [`00bcbfd0`](#insn-00bcbfd0) → [`00bcc038`](#insn-00bcc038)
  - `FALL_THROUGH` [`00bcbfd0`](#insn-00bcbfd0) → [`00bcbfd4`](#insn-00bcbfd4)
- ブロック [`00bcbfd4`](#insn-00bcbfd4) 範囲 `[['00bcbfd4', '00bcbfd7']]`
  - `UNCONDITIONAL_JUMP` [`00bcbfd4`](#insn-00bcbfd4) → [`00bcc044`](#insn-00bcc044)
- ブロック [`00bcbfd8`](#insn-00bcbfd8) 範囲 `[['00bcbfd8', '00bcbfe3']]`
  - `CONDITIONAL_JUMP` [`00bcbfe0`](#insn-00bcbfe0) → [`00bcbfd0`](#insn-00bcbfd0)
  - `FALL_THROUGH` [`00bcbfe0`](#insn-00bcbfe0) → [`00bcbfe4`](#insn-00bcbfe4)
- ブロック [`00bcbfe4`](#insn-00bcbfe4) 範囲 `[['00bcbfe4', '00bcbfef']]`
  - `CONDITIONAL_JUMP` [`00bcbfec`](#insn-00bcbfec) → [`00bcc004`](#insn-00bcc004)
  - `FALL_THROUGH` [`00bcbfec`](#insn-00bcbfec) → [`00bcbff0`](#insn-00bcbff0)
- ブロック [`00bcbff0`](#insn-00bcbff0) 範囲 `[['00bcbff0', '00bcbfff']]`
  - `CONDITIONAL_JUMP` [`00bcbffc`](#insn-00bcbffc) → [`00bcc014`](#insn-00bcc014)
  - `FALL_THROUGH` [`00bcbffc`](#insn-00bcbffc) → [`00bcc000`](#insn-00bcc000)
- ブロック [`00bcc000`](#insn-00bcc000) 範囲 `[['00bcc000', '00bcc003']]`
  - `UNCONDITIONAL_JUMP` [`00bcc000`](#insn-00bcc000) → [`00bcc038`](#insn-00bcc038)
- ブロック [`00bcc004`](#insn-00bcc004) 範囲 `[['00bcc004', '00bcc013']]`
  - `CONDITIONAL_JUMP` [`00bcc010`](#insn-00bcc010) → [`00bcc038`](#insn-00bcc038)
  - `FALL_THROUGH` [`00bcc010`](#insn-00bcc010) → [`00bcc014`](#insn-00bcc014)
- ブロック [`00bcc014`](#insn-00bcc014) 範囲 `[['00bcc014', '00bcc01f']]`
  - `CONDITIONAL_JUMP` [`00bcc01c`](#insn-00bcc01c) → [`00bcc044`](#insn-00bcc044)
  - `FALL_THROUGH` [`00bcc01c`](#insn-00bcc01c) → [`00bcc020`](#insn-00bcc020)
- ブロック [`00bcc020`](#insn-00bcc020) 範囲 `[['00bcc020', '00bcc037']]`
  - `UNCONDITIONAL_JUMP` [`00bcc034`](#insn-00bcc034) → [`00bcc044`](#insn-00bcc044)
- ブロック [`00bcc038`](#insn-00bcc038) 範囲 `[['00bcc038', '00bcc043']]`
  - `FALL_THROUGH` [`00bcc040`](#insn-00bcc040) → [`00bcc044`](#insn-00bcc044)
- ブロック [`00bcc044`](#insn-00bcc044) 範囲 `[['00bcc044', '00bcc04b']]`
  - `FALL_THROUGH` [`00bcc048`](#insn-00bcc048) → [`00bcc04c`](#insn-00bcc04c)
- ブロック [`00bcc04c`](#insn-00bcc04c) 範囲 `[['00bcc04c', '00bcc05b']]`
  - `CONDITIONAL_JUMP` [`00bcc058`](#insn-00bcc058) → [`00bcc074`](#insn-00bcc074)
  - `FALL_THROUGH` [`00bcc058`](#insn-00bcc058) → [`00bcc05c`](#insn-00bcc05c)
- ブロック [`00bcc05c`](#insn-00bcc05c) 範囲 `[['00bcc05c', '00bcc073']]`
- ブロック [`00bcc074`](#insn-00bcc074) 範囲 `[['00bcc074', '00bcc077']]`

## 命令位置別の参照

- [`00bcbec8`](#insn-00bcbec8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbecc`](#insn-00bcbecc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbed0`](#insn-00bcbed0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbed4`](#insn-00bcbed4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbee4`](#insn-00bcbee4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbeec`](#insn-00bcbeec) → [`00bcc04c`](#insn-00bcc04c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf00`](#insn-00bcbf00) → [`00c5baa0`](../00c5b/00c5baa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baa0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf08`](#insn-00bcbf08) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf18`](#insn-00bcbf18) → [`00bcbf58`](#insn-00bcbf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf24`](#insn-00bcbf24) → [`00bcbf58`](#insn-00bcbf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf30`](#insn-00bcbf30) → [`00bcbf64`](#insn-00bcbf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf44`](#insn-00bcbf44) → [`00bcbf2c`](#insn-00bcbf2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf4c`](#insn-00bcbf4c) → [`00bcbf64`](#insn-00bcbf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf54`](#insn-00bcbf54) → [`00bcbf8c`](#insn-00bcbf8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf60`](#insn-00bcbf60) → [`00bcbf50`](#insn-00bcbf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf6c`](#insn-00bcbf6c) → [`00bcbf7c`](#insn-00bcbf7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf78`](#insn-00bcbf78) → [`00bcbf88`](#insn-00bcbf88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf84`](#insn-00bcbf84) → [`00c5eb90`](../00c5e/00c5eb90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5eb90` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf94`](#insn-00bcbf94) → [`00bcbfd8`](#insn-00bcbfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbf98`](#insn-00bcbf98) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfa4`](#insn-00bcbfa4) → [`00bcbfd8`](#insn-00bcbfd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfb0`](#insn-00bcbfb0) → [`00bcbfe4`](#insn-00bcbfe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfc4`](#insn-00bcbfc4) → [`00bcbfac`](#insn-00bcbfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfcc`](#insn-00bcbfcc) → [`00bcbfe4`](#insn-00bcbfe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfd0`](#insn-00bcbfd0) → [`00bcc038`](#insn-00bcc038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfd4`](#insn-00bcbfd4) → [`00bcc044`](#insn-00bcc044) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfe0`](#insn-00bcbfe0) → [`00bcbfd0`](#insn-00bcbfd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbfec`](#insn-00bcbfec) → [`00bcc004`](#insn-00bcc004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbff0`](#insn-00bcbff0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbffc`](#insn-00bcbffc) → [`00bcc014`](#insn-00bcc014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc000`](#insn-00bcc000) → [`00bcc038`](#insn-00bcc038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc00c`](#insn-00bcc00c) → [`00c5ebb0`](../00c5e/00c5ebb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ebb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcc010`](#insn-00bcc010) → [`00bcc038`](#insn-00bcc038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc01c`](#insn-00bcc01c) → [`00bcc044`](#insn-00bcc044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc034`](#insn-00bcc034) → [`00bcc044`](#insn-00bcc044) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc03c`](#insn-00bcc03c) → `002b8ce7`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcc040`](#insn-00bcc040) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bcc048`](#insn-00bcc048) → [`00c5bab0`](../00c5b/00c5bab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcc050`](#insn-00bcc050) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc058`](#insn-00bcc058) → [`00bcc074`](#insn-00bcc074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc05c`](#insn-00bcc05c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc060`](#insn-00bcc060) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc064`](#insn-00bcc064) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc068`](#insn-00bcc068) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcc074`](#insn-00bcc074) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbec8`](#insn-00bcbec8)

~~~json
{
  "source": "00bcbec8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbecc`](#insn-00bcbecc)

~~~json
{
  "source": "00bcbecc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbed0`](#insn-00bcbed0)

~~~json
{
  "source": "00bcbed0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbed4`](#insn-00bcbed4)

~~~json
{
  "source": "00bcbed4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbee4`](#insn-00bcbee4)

~~~json
{
  "source": "00bcbee4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbeec`](#insn-00bcbeec)

~~~json
{
  "source": "00bcbeec",
  "target": "00bcc04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf00`](#insn-00bcbf00)

~~~json
{
  "source": "00bcbf00",
  "target": "00c5baa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf08`](#insn-00bcbf08)

~~~json
{
  "source": "00bcbf08",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf18`](#insn-00bcbf18)

~~~json
{
  "source": "00bcbf18",
  "target": "00bcbf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf24`](#insn-00bcbf24)

~~~json
{
  "source": "00bcbf24",
  "target": "00bcbf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf30`](#insn-00bcbf30)

~~~json
{
  "source": "00bcbf30",
  "target": "00bcbf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf44`](#insn-00bcbf44)

~~~json
{
  "source": "00bcbf44",
  "target": "00bcbf2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf4c`](#insn-00bcbf4c)

~~~json
{
  "source": "00bcbf4c",
  "target": "00bcbf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf54`](#insn-00bcbf54)

~~~json
{
  "source": "00bcbf54",
  "target": "00bcbf8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf60`](#insn-00bcbf60)

~~~json
{
  "source": "00bcbf60",
  "target": "00bcbf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf6c`](#insn-00bcbf6c)

~~~json
{
  "source": "00bcbf6c",
  "target": "00bcbf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf78`](#insn-00bcbf78)

~~~json
{
  "source": "00bcbf78",
  "target": "00bcbf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf84`](#insn-00bcbf84)

~~~json
{
  "source": "00bcbf84",
  "target": "00c5eb90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbf94`](#insn-00bcbf94)

~~~json
{
  "source": "00bcbf94",
  "target": "00bcbfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbf98`](#insn-00bcbf98)

~~~json
{
  "source": "00bcbf98",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfa4`](#insn-00bcbfa4)

~~~json
{
  "source": "00bcbfa4",
  "target": "00bcbfd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfb0`](#insn-00bcbfb0)

~~~json
{
  "source": "00bcbfb0",
  "target": "00bcbfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfc4`](#insn-00bcbfc4)

~~~json
{
  "source": "00bcbfc4",
  "target": "00bcbfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfcc`](#insn-00bcbfcc)

~~~json
{
  "source": "00bcbfcc",
  "target": "00bcbfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfd0`](#insn-00bcbfd0)

~~~json
{
  "source": "00bcbfd0",
  "target": "00bcc038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfd4`](#insn-00bcbfd4)

~~~json
{
  "source": "00bcbfd4",
  "target": "00bcc044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfe0`](#insn-00bcbfe0)

~~~json
{
  "source": "00bcbfe0",
  "target": "00bcbfd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbfec`](#insn-00bcbfec)

~~~json
{
  "source": "00bcbfec",
  "target": "00bcc004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbff0`](#insn-00bcbff0)

~~~json
{
  "source": "00bcbff0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbffc`](#insn-00bcbffc)

~~~json
{
  "source": "00bcbffc",
  "target": "00bcc014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc000`](#insn-00bcc000)

~~~json
{
  "source": "00bcc000",
  "target": "00bcc038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc00c`](#insn-00bcc00c)

~~~json
{
  "source": "00bcc00c",
  "target": "00c5ebb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc010`](#insn-00bcc010)

~~~json
{
  "source": "00bcc010",
  "target": "00bcc038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc01c`](#insn-00bcc01c)

~~~json
{
  "source": "00bcc01c",
  "target": "00bcc044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc034`](#insn-00bcc034)

~~~json
{
  "source": "00bcc034",
  "target": "00bcc044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc03c`](#insn-00bcc03c)

~~~json
{
  "source": "00bcc03c",
  "target": "002b8ce7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8ce7",
  "offset": 0,
  "size": 29,
  "datatype": "string",
  "bytes": "6c697374656e65725f6164646564203d3d20617574685f616464656400",
  "capture_start": "002b8ce7",
  "capture_bytes": 29,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcc040`](#insn-00bcc040)

~~~json
{
  "source": "00bcc040",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc048`](#insn-00bcc048)

~~~json
{
  "source": "00bcc048",
  "target": "00c5bab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcc050`](#insn-00bcc050)

~~~json
{
  "source": "00bcc050",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc058`](#insn-00bcc058)

~~~json
{
  "source": "00bcc058",
  "target": "00bcc074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc05c`](#insn-00bcc05c)

~~~json
{
  "source": "00bcc05c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc060`](#insn-00bcc060)

~~~json
{
  "source": "00bcc060",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc064`](#insn-00bcc064)

~~~json
{
  "source": "00bcc064",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc068`](#insn-00bcc068)

~~~json
{
  "source": "00bcc068",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcc074`](#insn-00bcc074)

~~~json
{
  "source": "00bcc074",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
