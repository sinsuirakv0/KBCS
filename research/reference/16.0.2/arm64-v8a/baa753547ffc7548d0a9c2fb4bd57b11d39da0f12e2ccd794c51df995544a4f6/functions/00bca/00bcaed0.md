# 00bcaed0

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcae34`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcae34.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-dc8611aea392bf331bcb4e09a0236ab3)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcbec4`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcb/00bcbec4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-db094e18973a806cf209e09db37ae581)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcaed0",
  "name": "_ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6fcebf31b0a40717da51e14f5ce70d129d18ee95f1ef7a07bf9a372424a6ae38",
  "source_text_sha256": "6fcebf31b0a40717da51e14f5ce70d129d18ee95f1ef7a07bf9a372424a6ae38",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcaed0",
        "00bcb083"
      ]
    ],
    "bytes_sha256": "ac41caf6eab20ab0476dc20581efbce21a09fadd5211f5ab99874889353ac3bc",
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

- [00c57fb0](../00c57/00c57fb0.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5dbc0](../00c5d/00c5dbc0.md)
- [00c5dbe0](../00c5d/00c5dbe0.md)

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
  if (*param_1 == 0) goto LAB_00bcb058;
  lVar3 = *param_1 + 0x268;
  _ZN8firebase5Mutex7AcquireEv(lVar3);
  lVar7 = *param_1;
  plVar10 = *(long **)(lVar7 + 0x230);
  plVar8 = *(long **)(lVar7 + 0x238);
  local_58 = param_1;
  plStack_50 = param_2;
  if ((plVar10 == plVar8) || ((long *)*plVar10 == param_2)) {
    if (plVar10 == plVar8) goto LAB_00bcaf70;
LAB_00bcaf5c:
    bVar6 = false;
  }
  else {
    do {
      if (plVar8 + -1 == plVar10) goto LAB_00bcaf70;
      plVar1 = plVar10 + 1;
      plVar10 = plVar10 + 1;
    } while ((long *)*plVar1 != param_2);
    if (plVar10 != plVar8) goto LAB_00bcaf5c;
LAB_00bcaf70:
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
    if (puVar9 == puVar4) goto LAB_00bcaff0;
LAB_00bcafdc:
    if (bVar6) {
LAB_00bcb044:
      _ZN8firebase9LogAssertEPKcz("listener_added == auth_added");
    }
  }
  else {
    do {
      if (puVar4 + -1 == puVar9) goto LAB_00bcaff0;
      puVar2 = puVar9 + 1;
      puVar9 = puVar9 + 1;
    } while ((long *)*puVar2 != local_58);
    if (puVar9 != puVar4) goto LAB_00bcafdc;
LAB_00bcaff0:
    if (puVar4 == (undefined8 *)param_2[3]) {
      _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (param_2 + 1,&local_58);
    }
    else {
      *puVar4 = local_58;
      param_2[2] = (long)(puVar4 + 1);
    }
    if (!bVar6) goto LAB_00bcb044;
    if (*(char *)(*param_1 + 0x2b9) == '\0') {
      (**(code **)(*param_2 + 0x10))(param_2,param_1);
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar3);
LAB_00bcb058:
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
<a id="insn-00bcaed0"></a> `00bcaed0` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcaed4"></a> `00bcaed4` | `f7 13 00 f9` | str x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcaed8"></a> `00bcaed8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcaedc"></a> `00bcaedc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcaee0"></a> `00bcaee0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcaee4"></a> `00bcaee4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bcaee8"></a> `00bcaee8` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcaeec"></a> `00bcaeec` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcaef0"></a> `00bcaef0` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcaef4"></a> `00bcaef4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcaef8"></a> `00bcaef8` | `08 0b 00 b4` | cbz x8,0x00bcb058 | `CONDITIONAL_JUMP`
<a id="insn-00bcaefc"></a> `00bcaefc` | `13 a1 09 91` | add x19,x8,#0x268 | `FALL_THROUGH`
<a id="insn-00bcaf00"></a> `00bcaf00` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcaf04"></a> `00bcaf04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcaf08"></a> `00bcaf08` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bcaf0c"></a> `00bcaf0c` | `f1 3e 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaf10"></a> `00bcaf10` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcaf14"></a> `00bcaf14` | `f4 d7 00 a9` | stp x20,x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaf18"></a> `00bcaf18` | `0a 19 41 f9` | ldr x10,[x8, #0x230] | `FALL_THROUGH`
<a id="insn-00bcaf1c"></a> `00bcaf1c` | `09 1d 41 f9` | ldr x9,[x8, #0x238] | `FALL_THROUGH`
<a id="insn-00bcaf20"></a> `00bcaf20` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcaf24"></a> `00bcaf24` | `00 02 00 54` | b.eq 0x00bcaf64 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf28"></a> `00bcaf28` | `4b 01 40 f9` | ldr x11,[x10] | `FALL_THROUGH`
<a id="insn-00bcaf2c"></a> `00bcaf2c` | `7f 01 15 eb` | cmp x11,x21 | `FALL_THROUGH`
<a id="insn-00bcaf30"></a> `00bcaf30` | `a0 01 00 54` | b.eq 0x00bcaf64 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf34"></a> `00bcaf34` | `2b 21 00 d1` | sub x11,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaf38"></a> `00bcaf38` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcaf3c"></a> `00bcaf3c` | `a0 01 00 54` | b.eq 0x00bcaf70 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf40"></a> `00bcaf40` | `4d 05 40 f9` | ldr x13,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaf44"></a> `00bcaf44` | `4c 21 00 91` | add x12,x10,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaf48"></a> `00bcaf48` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bcaf4c"></a> `00bcaf4c` | `bf 01 15 eb` | cmp x13,x21 | `FALL_THROUGH`
<a id="insn-00bcaf50"></a> `00bcaf50` | `41 ff ff 54` | b.ne 0x00bcaf38 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf54"></a> `00bcaf54` | `9f 01 09 eb` | cmp x12,x9 | `FALL_THROUGH`
<a id="insn-00bcaf58"></a> `00bcaf58` | `c0 00 00 54` | b.eq 0x00bcaf70 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf5c"></a> `00bcaf5c` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00bcaf60"></a> `00bcaf60` | `0e 00 00 14` | b 0x00bcaf98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcaf64"></a> `00bcaf64` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00bcaf68"></a> `00bcaf68` | `9f 01 09 eb` | cmp x12,x9 | `FALL_THROUGH`
<a id="insn-00bcaf6c"></a> `00bcaf6c` | `81 ff ff 54` | b.ne 0x00bcaf5c | `CONDITIONAL_JUMP`
<a id="insn-00bcaf70"></a> `00bcaf70` | `0a 21 41 f9` | ldr x10,[x8, #0x240] | `FALL_THROUGH`
<a id="insn-00bcaf74"></a> `00bcaf74` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcaf78"></a> `00bcaf78` | `80 00 00 54` | b.eq 0x00bcaf88 | `CONDITIONAL_JUMP`
<a id="insn-00bcaf7c"></a> `00bcaf7c` | `35 85 00 f8` | str x21,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-00bcaf80"></a> `00bcaf80` | `09 1d 01 f9` | str x9,[x8, #0x238] | `FALL_THROUGH`
<a id="insn-00bcaf84"></a> `00bcaf84` | `04 00 00 14` | b 0x00bcaf94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcaf88"></a> `00bcaf88` | `00 c1 08 91` | add x0,x8,#0x230 | `FALL_THROUGH`
<a id="insn-00bcaf8c"></a> `00bcaf8c` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcaf90"></a> `00bcaf90` | `0c 4b 02 94` | bl 0x00c5dbc0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaf94"></a> `00bcaf94` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bcaf98"></a> `00bcaf98` | `a9 a2 40 a9` | ldp x9,x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaf9c"></a> `00bcaf9c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcafa0"></a> `00bcafa0` | `20 02 00 54` | b.eq 0x00bcafe4 | `CONDITIONAL_JUMP`
<a id="insn-00bcafa4"></a> `00bcafa4` | `ea 07 40 f9` | ldr x10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcafa8"></a> `00bcafa8` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bcafac"></a> `00bcafac` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcafb0"></a> `00bcafb0` | `a0 01 00 54` | b.eq 0x00bcafe4 | `CONDITIONAL_JUMP`
<a id="insn-00bcafb4"></a> `00bcafb4` | `0b 21 00 d1` | sub x11,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcafb8"></a> `00bcafb8` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00bcafbc"></a> `00bcafbc` | `a0 01 00 54` | b.eq 0x00bcaff0 | `CONDITIONAL_JUMP`
<a id="insn-00bcafc0"></a> `00bcafc0` | `2d 05 40 f9` | ldr x13,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bcafc4"></a> `00bcafc4` | `2c 21 00 91` | add x12,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcafc8"></a> `00bcafc8` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bcafcc"></a> `00bcafcc` | `bf 01 0a eb` | cmp x13,x10 | `FALL_THROUGH`
<a id="insn-00bcafd0"></a> `00bcafd0` | `41 ff ff 54` | b.ne 0x00bcafb8 | `CONDITIONAL_JUMP`
<a id="insn-00bcafd4"></a> `00bcafd4` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bcafd8"></a> `00bcafd8` | `c0 00 00 54` | b.eq 0x00bcaff0 | `CONDITIONAL_JUMP`
<a id="insn-00bcafdc"></a> `00bcafdc` | `57 03 00 35` | cbnz w23,0x00bcb044 | `CONDITIONAL_JUMP`
<a id="insn-00bcafe0"></a> `00bcafe0` | `1c 00 00 14` | b 0x00bcb050 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcafe4"></a> `00bcafe4` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bcafe8"></a> `00bcafe8` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bcafec"></a> `00bcafec` | `81 ff ff 54` | b.ne 0x00bcafdc | `CONDITIONAL_JUMP`
<a id="insn-00bcaff0"></a> `00bcaff0` | `a9 0e 40 f9` | ldr x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bcaff4"></a> `00bcaff4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcaff8"></a> `00bcaff8` | `c0 00 00 54` | b.eq 0x00bcb010 | `CONDITIONAL_JUMP`
<a id="insn-00bcaffc"></a> `00bcaffc` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcb000"></a> `00bcb000` | `09 85 00 f8` | str x9,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-00bcb004"></a> `00bcb004` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb008"></a> `00bcb008` | `d7 00 00 37` | tbnz w23,#0x0,0x00bcb020 | `CONDITIONAL_JUMP`
<a id="insn-00bcb00c"></a> `00bcb00c` | `0e 00 00 14` | b 0x00bcb044 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcb010"></a> `00bcb010` | `a0 22 00 91` | add x0,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bcb014"></a> `00bcb014` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcb018"></a> `00bcb018` | `f2 4a 02 94` | bl 0x00c5dbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb01c"></a> `00bcb01c` | `57 01 00 36` | tbz w23,#0x0,0x00bcb044 | `CONDITIONAL_JUMP`
<a id="insn-00bcb020"></a> `00bcb020` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcb024"></a> `00bcb024` | `08 e5 4a 39` | ldrb w8,[x8, #0x2b9] | `FALL_THROUGH`
<a id="insn-00bcb028"></a> `00bcb028` | `48 01 00 35` | cbnz w8,0x00bcb050 | `CONDITIONAL_JUMP`
<a id="insn-00bcb02c"></a> `00bcb02c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcb030"></a> `00bcb030` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bcb034"></a> `00bcb034` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcb038"></a> `00bcb038` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcb03c"></a> `00bcb03c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcb040"></a> `00bcb040` | `04 00 00 14` | b 0x00bcb050 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcb044"></a> `00bcb044` | `60 b7 ff b0` | adrp x0,0x2b8000 | `FALL_THROUGH`
<a id="insn-00bcb048"></a> `00bcb048` | `00 60 30 91` | add x0,x0,#0xc18 | `FALL_THROUGH`
<a id="insn-00bcb04c"></a> `00bcb04c` | `21 40 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb050"></a> `00bcb050` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcb054"></a> `00bcb054` | `a3 3e 02 94` | bl 0x00c5aae0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcb058"></a> `00bcb058` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcb05c"></a> `00bcb05c` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcb060"></a> `00bcb060` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcb064"></a> `00bcb064` | `e1 00 00 54` | b.ne 0x00bcb080 | `CONDITIONAL_JUMP`
<a id="insn-00bcb068"></a> `00bcb068` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcb06c"></a> `00bcb06c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcb070"></a> `00bcb070` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcb074"></a> `00bcb074` | `f7 13 40 f9` | ldr x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcb078"></a> `00bcb078` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcb07c"></a> `00bcb07c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcb080"></a> `00bcb080` | `cc 33 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcaed0`](#insn-00bcaed0) 範囲 `[['00bcaed0', '00bcaefb']]`
  - `CONDITIONAL_JUMP` [`00bcaef8`](#insn-00bcaef8) → [`00bcb058`](#insn-00bcb058)
  - `FALL_THROUGH` [`00bcaef8`](#insn-00bcaef8) → [`00bcaefc`](#insn-00bcaefc)
- ブロック [`00bcaefc`](#insn-00bcaefc) 範囲 `[['00bcaefc', '00bcaf27']]`
  - `CONDITIONAL_JUMP` [`00bcaf24`](#insn-00bcaf24) → [`00bcaf64`](#insn-00bcaf64)
  - `FALL_THROUGH` [`00bcaf24`](#insn-00bcaf24) → [`00bcaf28`](#insn-00bcaf28)
- ブロック [`00bcaf28`](#insn-00bcaf28) 範囲 `[['00bcaf28', '00bcaf33']]`
  - `CONDITIONAL_JUMP` [`00bcaf30`](#insn-00bcaf30) → [`00bcaf64`](#insn-00bcaf64)
  - `FALL_THROUGH` [`00bcaf30`](#insn-00bcaf30) → [`00bcaf34`](#insn-00bcaf34)
- ブロック [`00bcaf34`](#insn-00bcaf34) 範囲 `[['00bcaf34', '00bcaf37']]`
  - `FALL_THROUGH` [`00bcaf34`](#insn-00bcaf34) → [`00bcaf38`](#insn-00bcaf38)
- ブロック [`00bcaf38`](#insn-00bcaf38) 範囲 `[['00bcaf38', '00bcaf3f']]`
  - `CONDITIONAL_JUMP` [`00bcaf3c`](#insn-00bcaf3c) → [`00bcaf70`](#insn-00bcaf70)
  - `FALL_THROUGH` [`00bcaf3c`](#insn-00bcaf3c) → [`00bcaf40`](#insn-00bcaf40)
- ブロック [`00bcaf40`](#insn-00bcaf40) 範囲 `[['00bcaf40', '00bcaf53']]`
  - `CONDITIONAL_JUMP` [`00bcaf50`](#insn-00bcaf50) → [`00bcaf38`](#insn-00bcaf38)
  - `FALL_THROUGH` [`00bcaf50`](#insn-00bcaf50) → [`00bcaf54`](#insn-00bcaf54)
- ブロック [`00bcaf54`](#insn-00bcaf54) 範囲 `[['00bcaf54', '00bcaf5b']]`
  - `CONDITIONAL_JUMP` [`00bcaf58`](#insn-00bcaf58) → [`00bcaf70`](#insn-00bcaf70)
  - `FALL_THROUGH` [`00bcaf58`](#insn-00bcaf58) → [`00bcaf5c`](#insn-00bcaf5c)
- ブロック [`00bcaf5c`](#insn-00bcaf5c) 範囲 `[['00bcaf5c', '00bcaf63']]`
  - `UNCONDITIONAL_JUMP` [`00bcaf60`](#insn-00bcaf60) → [`00bcaf98`](#insn-00bcaf98)
- ブロック [`00bcaf64`](#insn-00bcaf64) 範囲 `[['00bcaf64', '00bcaf6f']]`
  - `CONDITIONAL_JUMP` [`00bcaf6c`](#insn-00bcaf6c) → [`00bcaf5c`](#insn-00bcaf5c)
  - `FALL_THROUGH` [`00bcaf6c`](#insn-00bcaf6c) → [`00bcaf70`](#insn-00bcaf70)
- ブロック [`00bcaf70`](#insn-00bcaf70) 範囲 `[['00bcaf70', '00bcaf7b']]`
  - `CONDITIONAL_JUMP` [`00bcaf78`](#insn-00bcaf78) → [`00bcaf88`](#insn-00bcaf88)
  - `FALL_THROUGH` [`00bcaf78`](#insn-00bcaf78) → [`00bcaf7c`](#insn-00bcaf7c)
- ブロック [`00bcaf7c`](#insn-00bcaf7c) 範囲 `[['00bcaf7c', '00bcaf87']]`
  - `UNCONDITIONAL_JUMP` [`00bcaf84`](#insn-00bcaf84) → [`00bcaf94`](#insn-00bcaf94)
- ブロック [`00bcaf88`](#insn-00bcaf88) 範囲 `[['00bcaf88', '00bcaf93']]`
  - `FALL_THROUGH` [`00bcaf90`](#insn-00bcaf90) → [`00bcaf94`](#insn-00bcaf94)
- ブロック [`00bcaf94`](#insn-00bcaf94) 範囲 `[['00bcaf94', '00bcaf97']]`
  - `FALL_THROUGH` [`00bcaf94`](#insn-00bcaf94) → [`00bcaf98`](#insn-00bcaf98)
- ブロック [`00bcaf98`](#insn-00bcaf98) 範囲 `[['00bcaf98', '00bcafa3']]`
  - `CONDITIONAL_JUMP` [`00bcafa0`](#insn-00bcafa0) → [`00bcafe4`](#insn-00bcafe4)
  - `FALL_THROUGH` [`00bcafa0`](#insn-00bcafa0) → [`00bcafa4`](#insn-00bcafa4)
- ブロック [`00bcafa4`](#insn-00bcafa4) 範囲 `[['00bcafa4', '00bcafb3']]`
  - `CONDITIONAL_JUMP` [`00bcafb0`](#insn-00bcafb0) → [`00bcafe4`](#insn-00bcafe4)
  - `FALL_THROUGH` [`00bcafb0`](#insn-00bcafb0) → [`00bcafb4`](#insn-00bcafb4)
- ブロック [`00bcafb4`](#insn-00bcafb4) 範囲 `[['00bcafb4', '00bcafb7']]`
  - `FALL_THROUGH` [`00bcafb4`](#insn-00bcafb4) → [`00bcafb8`](#insn-00bcafb8)
- ブロック [`00bcafb8`](#insn-00bcafb8) 範囲 `[['00bcafb8', '00bcafbf']]`
  - `CONDITIONAL_JUMP` [`00bcafbc`](#insn-00bcafbc) → [`00bcaff0`](#insn-00bcaff0)
  - `FALL_THROUGH` [`00bcafbc`](#insn-00bcafbc) → [`00bcafc0`](#insn-00bcafc0)
- ブロック [`00bcafc0`](#insn-00bcafc0) 範囲 `[['00bcafc0', '00bcafd3']]`
  - `CONDITIONAL_JUMP` [`00bcafd0`](#insn-00bcafd0) → [`00bcafb8`](#insn-00bcafb8)
  - `FALL_THROUGH` [`00bcafd0`](#insn-00bcafd0) → [`00bcafd4`](#insn-00bcafd4)
- ブロック [`00bcafd4`](#insn-00bcafd4) 範囲 `[['00bcafd4', '00bcafdb']]`
  - `CONDITIONAL_JUMP` [`00bcafd8`](#insn-00bcafd8) → [`00bcaff0`](#insn-00bcaff0)
  - `FALL_THROUGH` [`00bcafd8`](#insn-00bcafd8) → [`00bcafdc`](#insn-00bcafdc)
- ブロック [`00bcafdc`](#insn-00bcafdc) 範囲 `[['00bcafdc', '00bcafdf']]`
  - `CONDITIONAL_JUMP` [`00bcafdc`](#insn-00bcafdc) → [`00bcb044`](#insn-00bcb044)
  - `FALL_THROUGH` [`00bcafdc`](#insn-00bcafdc) → [`00bcafe0`](#insn-00bcafe0)
- ブロック [`00bcafe0`](#insn-00bcafe0) 範囲 `[['00bcafe0', '00bcafe3']]`
  - `UNCONDITIONAL_JUMP` [`00bcafe0`](#insn-00bcafe0) → [`00bcb050`](#insn-00bcb050)
- ブロック [`00bcafe4`](#insn-00bcafe4) 範囲 `[['00bcafe4', '00bcafef']]`
  - `CONDITIONAL_JUMP` [`00bcafec`](#insn-00bcafec) → [`00bcafdc`](#insn-00bcafdc)
  - `FALL_THROUGH` [`00bcafec`](#insn-00bcafec) → [`00bcaff0`](#insn-00bcaff0)
- ブロック [`00bcaff0`](#insn-00bcaff0) 範囲 `[['00bcaff0', '00bcaffb']]`
  - `CONDITIONAL_JUMP` [`00bcaff8`](#insn-00bcaff8) → [`00bcb010`](#insn-00bcb010)
  - `FALL_THROUGH` [`00bcaff8`](#insn-00bcaff8) → [`00bcaffc`](#insn-00bcaffc)
- ブロック [`00bcaffc`](#insn-00bcaffc) 範囲 `[['00bcaffc', '00bcb00b']]`
  - `CONDITIONAL_JUMP` [`00bcb008`](#insn-00bcb008) → [`00bcb020`](#insn-00bcb020)
  - `FALL_THROUGH` [`00bcb008`](#insn-00bcb008) → [`00bcb00c`](#insn-00bcb00c)
- ブロック [`00bcb00c`](#insn-00bcb00c) 範囲 `[['00bcb00c', '00bcb00f']]`
  - `UNCONDITIONAL_JUMP` [`00bcb00c`](#insn-00bcb00c) → [`00bcb044`](#insn-00bcb044)
- ブロック [`00bcb010`](#insn-00bcb010) 範囲 `[['00bcb010', '00bcb01f']]`
  - `CONDITIONAL_JUMP` [`00bcb01c`](#insn-00bcb01c) → [`00bcb044`](#insn-00bcb044)
  - `FALL_THROUGH` [`00bcb01c`](#insn-00bcb01c) → [`00bcb020`](#insn-00bcb020)
- ブロック [`00bcb020`](#insn-00bcb020) 範囲 `[['00bcb020', '00bcb02b']]`
  - `CONDITIONAL_JUMP` [`00bcb028`](#insn-00bcb028) → [`00bcb050`](#insn-00bcb050)
  - `FALL_THROUGH` [`00bcb028`](#insn-00bcb028) → [`00bcb02c`](#insn-00bcb02c)
- ブロック [`00bcb02c`](#insn-00bcb02c) 範囲 `[['00bcb02c', '00bcb043']]`
  - `UNCONDITIONAL_JUMP` [`00bcb040`](#insn-00bcb040) → [`00bcb050`](#insn-00bcb050)
- ブロック [`00bcb044`](#insn-00bcb044) 範囲 `[['00bcb044', '00bcb04f']]`
  - `FALL_THROUGH` [`00bcb04c`](#insn-00bcb04c) → [`00bcb050`](#insn-00bcb050)
- ブロック [`00bcb050`](#insn-00bcb050) 範囲 `[['00bcb050', '00bcb057']]`
  - `FALL_THROUGH` [`00bcb054`](#insn-00bcb054) → [`00bcb058`](#insn-00bcb058)
- ブロック [`00bcb058`](#insn-00bcb058) 範囲 `[['00bcb058', '00bcb067']]`
  - `CONDITIONAL_JUMP` [`00bcb064`](#insn-00bcb064) → [`00bcb080`](#insn-00bcb080)
  - `FALL_THROUGH` [`00bcb064`](#insn-00bcb064) → [`00bcb068`](#insn-00bcb068)
- ブロック [`00bcb068`](#insn-00bcb068) 範囲 `[['00bcb068', '00bcb07f']]`
- ブロック [`00bcb080`](#insn-00bcb080) 範囲 `[['00bcb080', '00bcb083']]`

## 命令位置別の参照

- [`00bcaed4`](#insn-00bcaed4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaed8`](#insn-00bcaed8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaedc`](#insn-00bcaedc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaee0`](#insn-00bcaee0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaef0`](#insn-00bcaef0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaef8`](#insn-00bcaef8) → [`00bcb058`](#insn-00bcb058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf0c`](#insn-00bcaf0c) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf14`](#insn-00bcaf14) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf24`](#insn-00bcaf24) → [`00bcaf64`](#insn-00bcaf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf30`](#insn-00bcaf30) → [`00bcaf64`](#insn-00bcaf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf3c`](#insn-00bcaf3c) → [`00bcaf70`](#insn-00bcaf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf50`](#insn-00bcaf50) → [`00bcaf38`](#insn-00bcaf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf58`](#insn-00bcaf58) → [`00bcaf70`](#insn-00bcaf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf60`](#insn-00bcaf60) → [`00bcaf98`](#insn-00bcaf98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf6c`](#insn-00bcaf6c) → [`00bcaf5c`](#insn-00bcaf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf78`](#insn-00bcaf78) → [`00bcaf88`](#insn-00bcaf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf84`](#insn-00bcaf84) → [`00bcaf94`](#insn-00bcaf94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaf90`](#insn-00bcaf90) → [`00c5dbc0`](../00c5d/00c5dbc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dbc0` · 推定シンボル `None` · 推定型 `None`
- [`00bcafa0`](#insn-00bcafa0) → [`00bcafe4`](#insn-00bcafe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafa4`](#insn-00bcafa4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafb0`](#insn-00bcafb0) → [`00bcafe4`](#insn-00bcafe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafbc`](#insn-00bcafbc) → [`00bcaff0`](#insn-00bcaff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafd0`](#insn-00bcafd0) → [`00bcafb8`](#insn-00bcafb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafd8`](#insn-00bcafd8) → [`00bcaff0`](#insn-00bcaff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafdc`](#insn-00bcafdc) → [`00bcb044`](#insn-00bcb044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafe0`](#insn-00bcafe0) → [`00bcb050`](#insn-00bcb050) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcafec`](#insn-00bcafec) → [`00bcafdc`](#insn-00bcafdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaff8`](#insn-00bcaff8) → [`00bcb010`](#insn-00bcb010) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaffc`](#insn-00bcaffc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb008`](#insn-00bcb008) → [`00bcb020`](#insn-00bcb020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb00c`](#insn-00bcb00c) → [`00bcb044`](#insn-00bcb044) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb018`](#insn-00bcb018) → [`00c5dbe0`](../00c5d/00c5dbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dbe0` · 推定シンボル `None` · 推定型 `None`
- [`00bcb01c`](#insn-00bcb01c) → [`00bcb044`](#insn-00bcb044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb028`](#insn-00bcb028) → [`00bcb050`](#insn-00bcb050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb040`](#insn-00bcb040) → [`00bcb050`](#insn-00bcb050) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb048`](#insn-00bcb048) → `002b8c18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcb04c`](#insn-00bcb04c) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcb054`](#insn-00bcb054) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bcb05c`](#insn-00bcb05c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb064`](#insn-00bcb064) → [`00bcb080`](#insn-00bcb080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb068`](#insn-00bcb068) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb06c`](#insn-00bcb06c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb070`](#insn-00bcb070) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb074`](#insn-00bcb074) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcb080`](#insn-00bcb080) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcaed4`](#insn-00bcaed4)

~~~json
{
  "source": "00bcaed4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaed8`](#insn-00bcaed8)

~~~json
{
  "source": "00bcaed8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaedc`](#insn-00bcaedc)

~~~json
{
  "source": "00bcaedc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaee0`](#insn-00bcaee0)

~~~json
{
  "source": "00bcaee0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaef0`](#insn-00bcaef0)

~~~json
{
  "source": "00bcaef0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaef8`](#insn-00bcaef8)

~~~json
{
  "source": "00bcaef8",
  "target": "00bcb058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf0c`](#insn-00bcaf0c)

~~~json
{
  "source": "00bcaf0c",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaf14`](#insn-00bcaf14)

~~~json
{
  "source": "00bcaf14",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf24`](#insn-00bcaf24)

~~~json
{
  "source": "00bcaf24",
  "target": "00bcaf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf30`](#insn-00bcaf30)

~~~json
{
  "source": "00bcaf30",
  "target": "00bcaf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf3c`](#insn-00bcaf3c)

~~~json
{
  "source": "00bcaf3c",
  "target": "00bcaf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf50`](#insn-00bcaf50)

~~~json
{
  "source": "00bcaf50",
  "target": "00bcaf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf58`](#insn-00bcaf58)

~~~json
{
  "source": "00bcaf58",
  "target": "00bcaf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf60`](#insn-00bcaf60)

~~~json
{
  "source": "00bcaf60",
  "target": "00bcaf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf6c`](#insn-00bcaf6c)

~~~json
{
  "source": "00bcaf6c",
  "target": "00bcaf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf78`](#insn-00bcaf78)

~~~json
{
  "source": "00bcaf78",
  "target": "00bcaf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf84`](#insn-00bcaf84)

~~~json
{
  "source": "00bcaf84",
  "target": "00bcaf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaf90`](#insn-00bcaf90)

~~~json
{
  "source": "00bcaf90",
  "target": "00c5dbc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcafa0`](#insn-00bcafa0)

~~~json
{
  "source": "00bcafa0",
  "target": "00bcafe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafa4`](#insn-00bcafa4)

~~~json
{
  "source": "00bcafa4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafb0`](#insn-00bcafb0)

~~~json
{
  "source": "00bcafb0",
  "target": "00bcafe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafbc`](#insn-00bcafbc)

~~~json
{
  "source": "00bcafbc",
  "target": "00bcaff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafd0`](#insn-00bcafd0)

~~~json
{
  "source": "00bcafd0",
  "target": "00bcafb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafd8`](#insn-00bcafd8)

~~~json
{
  "source": "00bcafd8",
  "target": "00bcaff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafdc`](#insn-00bcafdc)

~~~json
{
  "source": "00bcafdc",
  "target": "00bcb044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafe0`](#insn-00bcafe0)

~~~json
{
  "source": "00bcafe0",
  "target": "00bcb050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcafec`](#insn-00bcafec)

~~~json
{
  "source": "00bcafec",
  "target": "00bcafdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaff8`](#insn-00bcaff8)

~~~json
{
  "source": "00bcaff8",
  "target": "00bcb010",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaffc`](#insn-00bcaffc)

~~~json
{
  "source": "00bcaffc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb008`](#insn-00bcb008)

~~~json
{
  "source": "00bcb008",
  "target": "00bcb020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb00c`](#insn-00bcb00c)

~~~json
{
  "source": "00bcb00c",
  "target": "00bcb044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb018`](#insn-00bcb018)

~~~json
{
  "source": "00bcb018",
  "target": "00c5dbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb01c`](#insn-00bcb01c)

~~~json
{
  "source": "00bcb01c",
  "target": "00bcb044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb028`](#insn-00bcb028)

~~~json
{
  "source": "00bcb028",
  "target": "00bcb050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb040`](#insn-00bcb040)

~~~json
{
  "source": "00bcb040",
  "target": "00bcb050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb048`](#insn-00bcb048)

~~~json
{
  "source": "00bcb048",
  "target": "002b8c18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8c18",
  "offset": 0,
  "size": 29,
  "datatype": "string",
  "bytes": "6c697374656e65725f6164646564203d3d20617574685f616464656400",
  "capture_start": "002b8c18",
  "capture_bytes": 29,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcb04c`](#insn-00bcb04c)

~~~json
{
  "source": "00bcb04c",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb054`](#insn-00bcb054)

~~~json
{
  "source": "00bcb054",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcb05c`](#insn-00bcb05c)

~~~json
{
  "source": "00bcb05c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb064`](#insn-00bcb064)

~~~json
{
  "source": "00bcb064",
  "target": "00bcb080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb068`](#insn-00bcb068)

~~~json
{
  "source": "00bcb068",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb06c`](#insn-00bcb06c)

~~~json
{
  "source": "00bcb06c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb070`](#insn-00bcb070)

~~~json
{
  "source": "00bcb070",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb074`](#insn-00bcb074)

~~~json
{
  "source": "00bcb074",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcb080`](#insn-00bcb080)

~~~json
{
  "source": "00bcb080",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
