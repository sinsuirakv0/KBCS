# 00bcaa0c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5b50c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b50c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-fea2bfaa0b4950a158f97bc0db699d51)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcae34`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bcae34.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-811dae6f2e0e59422f6b370aa9ad246b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcaa0c",
  "name": "_ZN8firebase4auth4Auth20AddAuthStateListenerEPNS0_17AuthStateListenerE",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7001db8ca6205a502177ed7d5103b82795e7db2305a8d6f73ef57f98fd5e54b7",
  "source_text_sha256": "7001db8ca6205a502177ed7d5103b82795e7db2305a8d6f73ef57f98fd5e54b7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcaa0c",
        "00bcabbf"
      ]
    ],
    "bytes_sha256": "fa0ba3d57c41afa318eb7082d61e91a2f7d9f2419db62ed2b1a5f2f0bedae483",
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

- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5d6f0](../00c5d/00c5d6f0.md)
- [00c5d710](../00c5d/00c5d710.md)

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
  if (*param_1 == 0) goto LAB_00bcab94;
  lVar3 = *param_1 + 0x268;
  _ZN8firebase5Mutex7AcquireEv(lVar3);
  lVar7 = *param_1;
  plVar10 = *(long **)(lVar7 + 0x230);
  plVar8 = *(long **)(lVar7 + 0x238);
  local_58 = param_1;
  plStack_50 = param_2;
  if ((plVar10 == plVar8) || ((long *)*plVar10 == param_2)) {
    if (plVar10 == plVar8) goto LAB_00bcaaac;
LAB_00bcaa98:
    bVar6 = false;
  }
  else {
    do {
      if (plVar8 + -1 == plVar10) goto LAB_00bcaaac;
      plVar1 = plVar10 + 1;
      plVar10 = plVar10 + 1;
    } while ((long *)*plVar1 != param_2);
    if (plVar10 != plVar8) goto LAB_00bcaa98;
LAB_00bcaaac:
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
    if (puVar9 == puVar4) goto LAB_00bcab2c;
LAB_00bcab18:
    if (bVar6) {
LAB_00bcab80:
      _ZN8firebase9LogAssertEPKcz("listener_added == auth_added");
    }
  }
  else {
    do {
      if (puVar4 + -1 == puVar9) goto LAB_00bcab2c;
      puVar2 = puVar9 + 1;
      puVar9 = puVar9 + 1;
    } while ((long *)*puVar2 != local_58);
    if (puVar9 != puVar4) goto LAB_00bcab18;
LAB_00bcab2c:
    if (puVar4 == (undefined8 *)param_2[3]) {
      _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (param_2 + 1,&local_58);
    }
    else {
      *puVar4 = local_58;
      param_2[2] = (long)(puVar4 + 1);
    }
    if (!bVar6) goto LAB_00bcab80;
    if (*(char *)(*param_1 + 0x2b9) == '\0') {
      (**(code **)(*param_2 + 0x10))(param_2,param_1);
    }
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar3);
LAB_00bcab94:
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
<a id="insn-00bcaa0c"></a> `00bcaa0c` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcaa10"></a> `00bcaa10` | `f7 13 00 f9` | str x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcaa14"></a> `00bcaa14` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcaa18"></a> `00bcaa18` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcaa1c"></a> `00bcaa1c` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcaa20"></a> `00bcaa20` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bcaa24"></a> `00bcaa24` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcaa28"></a> `00bcaa28` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcaa2c"></a> `00bcaa2c` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcaa30"></a> `00bcaa30` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcaa34"></a> `00bcaa34` | `08 0b 00 b4` | cbz x8,0x00bcab94 | `CONDITIONAL_JUMP`
<a id="insn-00bcaa38"></a> `00bcaa38` | `13 a1 09 91` | add x19,x8,#0x268 | `FALL_THROUGH`
<a id="insn-00bcaa3c"></a> `00bcaa3c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcaa40"></a> `00bcaa40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcaa44"></a> `00bcaa44` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bcaa48"></a> `00bcaa48` | `ee 3e 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaa4c"></a> `00bcaa4c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcaa50"></a> `00bcaa50` | `f4 d7 00 a9` | stp x20,x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaa54"></a> `00bcaa54` | `0a 19 41 f9` | ldr x10,[x8, #0x230] | `FALL_THROUGH`
<a id="insn-00bcaa58"></a> `00bcaa58` | `09 1d 41 f9` | ldr x9,[x8, #0x238] | `FALL_THROUGH`
<a id="insn-00bcaa5c"></a> `00bcaa5c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcaa60"></a> `00bcaa60` | `00 02 00 54` | b.eq 0x00bcaaa0 | `CONDITIONAL_JUMP`
<a id="insn-00bcaa64"></a> `00bcaa64` | `4b 01 40 f9` | ldr x11,[x10] | `FALL_THROUGH`
<a id="insn-00bcaa68"></a> `00bcaa68` | `7f 01 15 eb` | cmp x11,x21 | `FALL_THROUGH`
<a id="insn-00bcaa6c"></a> `00bcaa6c` | `a0 01 00 54` | b.eq 0x00bcaaa0 | `CONDITIONAL_JUMP`
<a id="insn-00bcaa70"></a> `00bcaa70` | `2b 21 00 d1` | sub x11,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaa74"></a> `00bcaa74` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcaa78"></a> `00bcaa78` | `a0 01 00 54` | b.eq 0x00bcaaac | `CONDITIONAL_JUMP`
<a id="insn-00bcaa7c"></a> `00bcaa7c` | `4d 05 40 f9` | ldr x13,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaa80"></a> `00bcaa80` | `4c 21 00 91` | add x12,x10,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaa84"></a> `00bcaa84` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bcaa88"></a> `00bcaa88` | `bf 01 15 eb` | cmp x13,x21 | `FALL_THROUGH`
<a id="insn-00bcaa8c"></a> `00bcaa8c` | `41 ff ff 54` | b.ne 0x00bcaa74 | `CONDITIONAL_JUMP`
<a id="insn-00bcaa90"></a> `00bcaa90` | `9f 01 09 eb` | cmp x12,x9 | `FALL_THROUGH`
<a id="insn-00bcaa94"></a> `00bcaa94` | `c0 00 00 54` | b.eq 0x00bcaaac | `CONDITIONAL_JUMP`
<a id="insn-00bcaa98"></a> `00bcaa98` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00bcaa9c"></a> `00bcaa9c` | `0e 00 00 14` | b 0x00bcaad4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcaaa0"></a> `00bcaaa0` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00bcaaa4"></a> `00bcaaa4` | `9f 01 09 eb` | cmp x12,x9 | `FALL_THROUGH`
<a id="insn-00bcaaa8"></a> `00bcaaa8` | `81 ff ff 54` | b.ne 0x00bcaa98 | `CONDITIONAL_JUMP`
<a id="insn-00bcaaac"></a> `00bcaaac` | `0a 21 41 f9` | ldr x10,[x8, #0x240] | `FALL_THROUGH`
<a id="insn-00bcaab0"></a> `00bcaab0` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcaab4"></a> `00bcaab4` | `80 00 00 54` | b.eq 0x00bcaac4 | `CONDITIONAL_JUMP`
<a id="insn-00bcaab8"></a> `00bcaab8` | `35 85 00 f8` | str x21,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-00bcaabc"></a> `00bcaabc` | `09 1d 01 f9` | str x9,[x8, #0x238] | `FALL_THROUGH`
<a id="insn-00bcaac0"></a> `00bcaac0` | `04 00 00 14` | b 0x00bcaad0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcaac4"></a> `00bcaac4` | `00 c1 08 91` | add x0,x8,#0x230 | `FALL_THROUGH`
<a id="insn-00bcaac8"></a> `00bcaac8` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcaacc"></a> `00bcaacc` | `09 4b 02 94` | bl 0x00c5d6f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaad0"></a> `00bcaad0` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bcaad4"></a> `00bcaad4` | `a9 a2 40 a9` | ldp x9,x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaad8"></a> `00bcaad8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcaadc"></a> `00bcaadc` | `20 02 00 54` | b.eq 0x00bcab20 | `CONDITIONAL_JUMP`
<a id="insn-00bcaae0"></a> `00bcaae0` | `ea 07 40 f9` | ldr x10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaae4"></a> `00bcaae4` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bcaae8"></a> `00bcaae8` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcaaec"></a> `00bcaaec` | `a0 01 00 54` | b.eq 0x00bcab20 | `CONDITIONAL_JUMP`
<a id="insn-00bcaaf0"></a> `00bcaaf0` | `0b 21 00 d1` | sub x11,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcaaf4"></a> `00bcaaf4` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00bcaaf8"></a> `00bcaaf8` | `a0 01 00 54` | b.eq 0x00bcab2c | `CONDITIONAL_JUMP`
<a id="insn-00bcaafc"></a> `00bcaafc` | `2d 05 40 f9` | ldr x13,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bcab00"></a> `00bcab00` | `2c 21 00 91` | add x12,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcab04"></a> `00bcab04` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bcab08"></a> `00bcab08` | `bf 01 0a eb` | cmp x13,x10 | `FALL_THROUGH`
<a id="insn-00bcab0c"></a> `00bcab0c` | `41 ff ff 54` | b.ne 0x00bcaaf4 | `CONDITIONAL_JUMP`
<a id="insn-00bcab10"></a> `00bcab10` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bcab14"></a> `00bcab14` | `c0 00 00 54` | b.eq 0x00bcab2c | `CONDITIONAL_JUMP`
<a id="insn-00bcab18"></a> `00bcab18` | `57 03 00 35` | cbnz w23,0x00bcab80 | `CONDITIONAL_JUMP`
<a id="insn-00bcab1c"></a> `00bcab1c` | `1c 00 00 14` | b 0x00bcab8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcab20"></a> `00bcab20` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bcab24"></a> `00bcab24` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bcab28"></a> `00bcab28` | `81 ff ff 54` | b.ne 0x00bcab18 | `CONDITIONAL_JUMP`
<a id="insn-00bcab2c"></a> `00bcab2c` | `a9 0e 40 f9` | ldr x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bcab30"></a> `00bcab30` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcab34"></a> `00bcab34` | `c0 00 00 54` | b.eq 0x00bcab4c | `CONDITIONAL_JUMP`
<a id="insn-00bcab38"></a> `00bcab38` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcab3c"></a> `00bcab3c` | `09 85 00 f8` | str x9,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-00bcab40"></a> `00bcab40` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bcab44"></a> `00bcab44` | `d7 00 00 37` | tbnz w23,#0x0,0x00bcab5c | `CONDITIONAL_JUMP`
<a id="insn-00bcab48"></a> `00bcab48` | `0e 00 00 14` | b 0x00bcab80 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcab4c"></a> `00bcab4c` | `a0 22 00 91` | add x0,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bcab50"></a> `00bcab50` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcab54"></a> `00bcab54` | `ef 4a 02 94` | bl 0x00c5d710 | `UNCONDITIONAL_CALL`
<a id="insn-00bcab58"></a> `00bcab58` | `57 01 00 36` | tbz w23,#0x0,0x00bcab80 | `CONDITIONAL_JUMP`
<a id="insn-00bcab5c"></a> `00bcab5c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcab60"></a> `00bcab60` | `08 e5 4a 39` | ldrb w8,[x8, #0x2b9] | `FALL_THROUGH`
<a id="insn-00bcab64"></a> `00bcab64` | `48 01 00 35` | cbnz w8,0x00bcab8c | `CONDITIONAL_JUMP`
<a id="insn-00bcab68"></a> `00bcab68` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcab6c"></a> `00bcab6c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bcab70"></a> `00bcab70` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcab74"></a> `00bcab74` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcab78"></a> `00bcab78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcab7c"></a> `00bcab7c` | `04 00 00 14` | b 0x00bcab8c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcab80"></a> `00bcab80` | `60 b7 ff d0` | adrp x0,0x2b8000 | `FALL_THROUGH`
<a id="insn-00bcab84"></a> `00bcab84` | `00 b0 30 91` | add x0,x0,#0xc2c | `FALL_THROUGH`
<a id="insn-00bcab88"></a> `00bcab88` | `1e 40 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcab8c"></a> `00bcab8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcab90"></a> `00bcab90` | `a0 3e 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bcab94"></a> `00bcab94` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcab98"></a> `00bcab98` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcab9c"></a> `00bcab9c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcaba0"></a> `00bcaba0` | `e1 00 00 54` | b.ne 0x00bcabbc | `CONDITIONAL_JUMP`
<a id="insn-00bcaba4"></a> `00bcaba4` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcaba8"></a> `00bcaba8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcabac"></a> `00bcabac` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcabb0"></a> `00bcabb0` | `f7 13 40 f9` | ldr x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcabb4"></a> `00bcabb4` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcabb8"></a> `00bcabb8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcabbc"></a> `00bcabbc` | `c9 33 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcaa0c`](#insn-00bcaa0c) 範囲 `[['00bcaa0c', '00bcaa37']]`
  - `CONDITIONAL_JUMP` [`00bcaa34`](#insn-00bcaa34) → [`00bcab94`](#insn-00bcab94)
  - `FALL_THROUGH` [`00bcaa34`](#insn-00bcaa34) → [`00bcaa38`](#insn-00bcaa38)
- ブロック [`00bcaa38`](#insn-00bcaa38) 範囲 `[['00bcaa38', '00bcaa63']]`
  - `CONDITIONAL_JUMP` [`00bcaa60`](#insn-00bcaa60) → [`00bcaaa0`](#insn-00bcaaa0)
  - `FALL_THROUGH` [`00bcaa60`](#insn-00bcaa60) → [`00bcaa64`](#insn-00bcaa64)
- ブロック [`00bcaa64`](#insn-00bcaa64) 範囲 `[['00bcaa64', '00bcaa6f']]`
  - `CONDITIONAL_JUMP` [`00bcaa6c`](#insn-00bcaa6c) → [`00bcaaa0`](#insn-00bcaaa0)
  - `FALL_THROUGH` [`00bcaa6c`](#insn-00bcaa6c) → [`00bcaa70`](#insn-00bcaa70)
- ブロック [`00bcaa70`](#insn-00bcaa70) 範囲 `[['00bcaa70', '00bcaa73']]`
  - `FALL_THROUGH` [`00bcaa70`](#insn-00bcaa70) → [`00bcaa74`](#insn-00bcaa74)
- ブロック [`00bcaa74`](#insn-00bcaa74) 範囲 `[['00bcaa74', '00bcaa7b']]`
  - `CONDITIONAL_JUMP` [`00bcaa78`](#insn-00bcaa78) → [`00bcaaac`](#insn-00bcaaac)
  - `FALL_THROUGH` [`00bcaa78`](#insn-00bcaa78) → [`00bcaa7c`](#insn-00bcaa7c)
- ブロック [`00bcaa7c`](#insn-00bcaa7c) 範囲 `[['00bcaa7c', '00bcaa8f']]`
  - `CONDITIONAL_JUMP` [`00bcaa8c`](#insn-00bcaa8c) → [`00bcaa74`](#insn-00bcaa74)
  - `FALL_THROUGH` [`00bcaa8c`](#insn-00bcaa8c) → [`00bcaa90`](#insn-00bcaa90)
- ブロック [`00bcaa90`](#insn-00bcaa90) 範囲 `[['00bcaa90', '00bcaa97']]`
  - `CONDITIONAL_JUMP` [`00bcaa94`](#insn-00bcaa94) → [`00bcaaac`](#insn-00bcaaac)
  - `FALL_THROUGH` [`00bcaa94`](#insn-00bcaa94) → [`00bcaa98`](#insn-00bcaa98)
- ブロック [`00bcaa98`](#insn-00bcaa98) 範囲 `[['00bcaa98', '00bcaa9f']]`
  - `UNCONDITIONAL_JUMP` [`00bcaa9c`](#insn-00bcaa9c) → [`00bcaad4`](#insn-00bcaad4)
- ブロック [`00bcaaa0`](#insn-00bcaaa0) 範囲 `[['00bcaaa0', '00bcaaab']]`
  - `CONDITIONAL_JUMP` [`00bcaaa8`](#insn-00bcaaa8) → [`00bcaa98`](#insn-00bcaa98)
  - `FALL_THROUGH` [`00bcaaa8`](#insn-00bcaaa8) → [`00bcaaac`](#insn-00bcaaac)
- ブロック [`00bcaaac`](#insn-00bcaaac) 範囲 `[['00bcaaac', '00bcaab7']]`
  - `CONDITIONAL_JUMP` [`00bcaab4`](#insn-00bcaab4) → [`00bcaac4`](#insn-00bcaac4)
  - `FALL_THROUGH` [`00bcaab4`](#insn-00bcaab4) → [`00bcaab8`](#insn-00bcaab8)
- ブロック [`00bcaab8`](#insn-00bcaab8) 範囲 `[['00bcaab8', '00bcaac3']]`
  - `UNCONDITIONAL_JUMP` [`00bcaac0`](#insn-00bcaac0) → [`00bcaad0`](#insn-00bcaad0)
- ブロック [`00bcaac4`](#insn-00bcaac4) 範囲 `[['00bcaac4', '00bcaacf']]`
  - `FALL_THROUGH` [`00bcaacc`](#insn-00bcaacc) → [`00bcaad0`](#insn-00bcaad0)
- ブロック [`00bcaad0`](#insn-00bcaad0) 範囲 `[['00bcaad0', '00bcaad3']]`
  - `FALL_THROUGH` [`00bcaad0`](#insn-00bcaad0) → [`00bcaad4`](#insn-00bcaad4)
- ブロック [`00bcaad4`](#insn-00bcaad4) 範囲 `[['00bcaad4', '00bcaadf']]`
  - `CONDITIONAL_JUMP` [`00bcaadc`](#insn-00bcaadc) → [`00bcab20`](#insn-00bcab20)
  - `FALL_THROUGH` [`00bcaadc`](#insn-00bcaadc) → [`00bcaae0`](#insn-00bcaae0)
- ブロック [`00bcaae0`](#insn-00bcaae0) 範囲 `[['00bcaae0', '00bcaaef']]`
  - `CONDITIONAL_JUMP` [`00bcaaec`](#insn-00bcaaec) → [`00bcab20`](#insn-00bcab20)
  - `FALL_THROUGH` [`00bcaaec`](#insn-00bcaaec) → [`00bcaaf0`](#insn-00bcaaf0)
- ブロック [`00bcaaf0`](#insn-00bcaaf0) 範囲 `[['00bcaaf0', '00bcaaf3']]`
  - `FALL_THROUGH` [`00bcaaf0`](#insn-00bcaaf0) → [`00bcaaf4`](#insn-00bcaaf4)
- ブロック [`00bcaaf4`](#insn-00bcaaf4) 範囲 `[['00bcaaf4', '00bcaafb']]`
  - `CONDITIONAL_JUMP` [`00bcaaf8`](#insn-00bcaaf8) → [`00bcab2c`](#insn-00bcab2c)
  - `FALL_THROUGH` [`00bcaaf8`](#insn-00bcaaf8) → [`00bcaafc`](#insn-00bcaafc)
- ブロック [`00bcaafc`](#insn-00bcaafc) 範囲 `[['00bcaafc', '00bcab0f']]`
  - `CONDITIONAL_JUMP` [`00bcab0c`](#insn-00bcab0c) → [`00bcaaf4`](#insn-00bcaaf4)
  - `FALL_THROUGH` [`00bcab0c`](#insn-00bcab0c) → [`00bcab10`](#insn-00bcab10)
- ブロック [`00bcab10`](#insn-00bcab10) 範囲 `[['00bcab10', '00bcab17']]`
  - `CONDITIONAL_JUMP` [`00bcab14`](#insn-00bcab14) → [`00bcab2c`](#insn-00bcab2c)
  - `FALL_THROUGH` [`00bcab14`](#insn-00bcab14) → [`00bcab18`](#insn-00bcab18)
- ブロック [`00bcab18`](#insn-00bcab18) 範囲 `[['00bcab18', '00bcab1b']]`
  - `CONDITIONAL_JUMP` [`00bcab18`](#insn-00bcab18) → [`00bcab80`](#insn-00bcab80)
  - `FALL_THROUGH` [`00bcab18`](#insn-00bcab18) → [`00bcab1c`](#insn-00bcab1c)
- ブロック [`00bcab1c`](#insn-00bcab1c) 範囲 `[['00bcab1c', '00bcab1f']]`
  - `UNCONDITIONAL_JUMP` [`00bcab1c`](#insn-00bcab1c) → [`00bcab8c`](#insn-00bcab8c)
- ブロック [`00bcab20`](#insn-00bcab20) 範囲 `[['00bcab20', '00bcab2b']]`
  - `CONDITIONAL_JUMP` [`00bcab28`](#insn-00bcab28) → [`00bcab18`](#insn-00bcab18)
  - `FALL_THROUGH` [`00bcab28`](#insn-00bcab28) → [`00bcab2c`](#insn-00bcab2c)
- ブロック [`00bcab2c`](#insn-00bcab2c) 範囲 `[['00bcab2c', '00bcab37']]`
  - `CONDITIONAL_JUMP` [`00bcab34`](#insn-00bcab34) → [`00bcab4c`](#insn-00bcab4c)
  - `FALL_THROUGH` [`00bcab34`](#insn-00bcab34) → [`00bcab38`](#insn-00bcab38)
- ブロック [`00bcab38`](#insn-00bcab38) 範囲 `[['00bcab38', '00bcab47']]`
  - `CONDITIONAL_JUMP` [`00bcab44`](#insn-00bcab44) → [`00bcab5c`](#insn-00bcab5c)
  - `FALL_THROUGH` [`00bcab44`](#insn-00bcab44) → [`00bcab48`](#insn-00bcab48)
- ブロック [`00bcab48`](#insn-00bcab48) 範囲 `[['00bcab48', '00bcab4b']]`
  - `UNCONDITIONAL_JUMP` [`00bcab48`](#insn-00bcab48) → [`00bcab80`](#insn-00bcab80)
- ブロック [`00bcab4c`](#insn-00bcab4c) 範囲 `[['00bcab4c', '00bcab5b']]`
  - `CONDITIONAL_JUMP` [`00bcab58`](#insn-00bcab58) → [`00bcab80`](#insn-00bcab80)
  - `FALL_THROUGH` [`00bcab58`](#insn-00bcab58) → [`00bcab5c`](#insn-00bcab5c)
- ブロック [`00bcab5c`](#insn-00bcab5c) 範囲 `[['00bcab5c', '00bcab67']]`
  - `CONDITIONAL_JUMP` [`00bcab64`](#insn-00bcab64) → [`00bcab8c`](#insn-00bcab8c)
  - `FALL_THROUGH` [`00bcab64`](#insn-00bcab64) → [`00bcab68`](#insn-00bcab68)
- ブロック [`00bcab68`](#insn-00bcab68) 範囲 `[['00bcab68', '00bcab7f']]`
  - `UNCONDITIONAL_JUMP` [`00bcab7c`](#insn-00bcab7c) → [`00bcab8c`](#insn-00bcab8c)
- ブロック [`00bcab80`](#insn-00bcab80) 範囲 `[['00bcab80', '00bcab8b']]`
  - `FALL_THROUGH` [`00bcab88`](#insn-00bcab88) → [`00bcab8c`](#insn-00bcab8c)
- ブロック [`00bcab8c`](#insn-00bcab8c) 範囲 `[['00bcab8c', '00bcab93']]`
  - `FALL_THROUGH` [`00bcab90`](#insn-00bcab90) → [`00bcab94`](#insn-00bcab94)
- ブロック [`00bcab94`](#insn-00bcab94) 範囲 `[['00bcab94', '00bcaba3']]`
  - `CONDITIONAL_JUMP` [`00bcaba0`](#insn-00bcaba0) → [`00bcabbc`](#insn-00bcabbc)
  - `FALL_THROUGH` [`00bcaba0`](#insn-00bcaba0) → [`00bcaba4`](#insn-00bcaba4)
- ブロック [`00bcaba4`](#insn-00bcaba4) 範囲 `[['00bcaba4', '00bcabbb']]`
- ブロック [`00bcabbc`](#insn-00bcabbc) 範囲 `[['00bcabbc', '00bcabbf']]`

## 命令位置別の参照

- [`00bcaa10`](#insn-00bcaa10) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa14`](#insn-00bcaa14) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa18`](#insn-00bcaa18) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa1c`](#insn-00bcaa1c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa2c`](#insn-00bcaa2c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa34`](#insn-00bcaa34) → [`00bcab94`](#insn-00bcab94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa48`](#insn-00bcaa48) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa50`](#insn-00bcaa50) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa60`](#insn-00bcaa60) → [`00bcaaa0`](#insn-00bcaaa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa6c`](#insn-00bcaa6c) → [`00bcaaa0`](#insn-00bcaaa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa78`](#insn-00bcaa78) → [`00bcaaac`](#insn-00bcaaac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa8c`](#insn-00bcaa8c) → [`00bcaa74`](#insn-00bcaa74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa94`](#insn-00bcaa94) → [`00bcaaac`](#insn-00bcaaac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaa9c`](#insn-00bcaa9c) → [`00bcaad4`](#insn-00bcaad4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaaa8`](#insn-00bcaaa8) → [`00bcaa98`](#insn-00bcaa98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaab4`](#insn-00bcaab4) → [`00bcaac4`](#insn-00bcaac4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaac0`](#insn-00bcaac0) → [`00bcaad0`](#insn-00bcaad0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaacc`](#insn-00bcaacc) → [`00c5d6f0`](../00c5d/00c5d6f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d6f0` · 推定シンボル `None` · 推定型 `None`
- [`00bcaadc`](#insn-00bcaadc) → [`00bcab20`](#insn-00bcab20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaae0`](#insn-00bcaae0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaaec`](#insn-00bcaaec) → [`00bcab20`](#insn-00bcab20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaaf8`](#insn-00bcaaf8) → [`00bcab2c`](#insn-00bcab2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab0c`](#insn-00bcab0c) → [`00bcaaf4`](#insn-00bcaaf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab14`](#insn-00bcab14) → [`00bcab2c`](#insn-00bcab2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab18`](#insn-00bcab18) → [`00bcab80`](#insn-00bcab80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab1c`](#insn-00bcab1c) → [`00bcab8c`](#insn-00bcab8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab28`](#insn-00bcab28) → [`00bcab18`](#insn-00bcab18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab34`](#insn-00bcab34) → [`00bcab4c`](#insn-00bcab4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab38`](#insn-00bcab38) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab44`](#insn-00bcab44) → [`00bcab5c`](#insn-00bcab5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab48`](#insn-00bcab48) → [`00bcab80`](#insn-00bcab80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab54`](#insn-00bcab54) → [`00c5d710`](../00c5d/00c5d710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d710` · 推定シンボル `None` · 推定型 `None`
- [`00bcab58`](#insn-00bcab58) → [`00bcab80`](#insn-00bcab80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab64`](#insn-00bcab64) → [`00bcab8c`](#insn-00bcab8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab7c`](#insn-00bcab7c) → [`00bcab8c`](#insn-00bcab8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcab84`](#insn-00bcab84) → `002b8c2c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcab88`](#insn-00bcab88) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bcab90`](#insn-00bcab90) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bcab98`](#insn-00bcab98) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaba0`](#insn-00bcaba0) → [`00bcabbc`](#insn-00bcabbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaba4`](#insn-00bcaba4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcaba8`](#insn-00bcaba8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabac`](#insn-00bcabac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabb0`](#insn-00bcabb0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabbc`](#insn-00bcabbc) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcaa10`](#insn-00bcaa10)

~~~json
{
  "source": "00bcaa10",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa14`](#insn-00bcaa14)

~~~json
{
  "source": "00bcaa14",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa18`](#insn-00bcaa18)

~~~json
{
  "source": "00bcaa18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa1c`](#insn-00bcaa1c)

~~~json
{
  "source": "00bcaa1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa2c`](#insn-00bcaa2c)

~~~json
{
  "source": "00bcaa2c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa34`](#insn-00bcaa34)

~~~json
{
  "source": "00bcaa34",
  "target": "00bcab94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa48`](#insn-00bcaa48)

~~~json
{
  "source": "00bcaa48",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaa50`](#insn-00bcaa50)

~~~json
{
  "source": "00bcaa50",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa60`](#insn-00bcaa60)

~~~json
{
  "source": "00bcaa60",
  "target": "00bcaaa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa6c`](#insn-00bcaa6c)

~~~json
{
  "source": "00bcaa6c",
  "target": "00bcaaa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa78`](#insn-00bcaa78)

~~~json
{
  "source": "00bcaa78",
  "target": "00bcaaac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa8c`](#insn-00bcaa8c)

~~~json
{
  "source": "00bcaa8c",
  "target": "00bcaa74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa94`](#insn-00bcaa94)

~~~json
{
  "source": "00bcaa94",
  "target": "00bcaaac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaa9c`](#insn-00bcaa9c)

~~~json
{
  "source": "00bcaa9c",
  "target": "00bcaad4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaaa8`](#insn-00bcaaa8)

~~~json
{
  "source": "00bcaaa8",
  "target": "00bcaa98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaab4`](#insn-00bcaab4)

~~~json
{
  "source": "00bcaab4",
  "target": "00bcaac4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaac0`](#insn-00bcaac0)

~~~json
{
  "source": "00bcaac0",
  "target": "00bcaad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaacc`](#insn-00bcaacc)

~~~json
{
  "source": "00bcaacc",
  "target": "00c5d6f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcaadc`](#insn-00bcaadc)

~~~json
{
  "source": "00bcaadc",
  "target": "00bcab20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaae0`](#insn-00bcaae0)

~~~json
{
  "source": "00bcaae0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaaec`](#insn-00bcaaec)

~~~json
{
  "source": "00bcaaec",
  "target": "00bcab20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaaf8`](#insn-00bcaaf8)

~~~json
{
  "source": "00bcaaf8",
  "target": "00bcab2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab0c`](#insn-00bcab0c)

~~~json
{
  "source": "00bcab0c",
  "target": "00bcaaf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab14`](#insn-00bcab14)

~~~json
{
  "source": "00bcab14",
  "target": "00bcab2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab18`](#insn-00bcab18)

~~~json
{
  "source": "00bcab18",
  "target": "00bcab80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab1c`](#insn-00bcab1c)

~~~json
{
  "source": "00bcab1c",
  "target": "00bcab8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab28`](#insn-00bcab28)

~~~json
{
  "source": "00bcab28",
  "target": "00bcab18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab34`](#insn-00bcab34)

~~~json
{
  "source": "00bcab34",
  "target": "00bcab4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab38`](#insn-00bcab38)

~~~json
{
  "source": "00bcab38",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab44`](#insn-00bcab44)

~~~json
{
  "source": "00bcab44",
  "target": "00bcab5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab48`](#insn-00bcab48)

~~~json
{
  "source": "00bcab48",
  "target": "00bcab80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab54`](#insn-00bcab54)

~~~json
{
  "source": "00bcab54",
  "target": "00c5d710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcab58`](#insn-00bcab58)

~~~json
{
  "source": "00bcab58",
  "target": "00bcab80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab64`](#insn-00bcab64)

~~~json
{
  "source": "00bcab64",
  "target": "00bcab8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab7c`](#insn-00bcab7c)

~~~json
{
  "source": "00bcab7c",
  "target": "00bcab8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcab84`](#insn-00bcab84)

~~~json
{
  "source": "00bcab84",
  "target": "002b8c2c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8c2c",
  "offset": 0,
  "size": 29,
  "datatype": "string",
  "bytes": "6c697374656e65725f6164646564203d3d20617574685f616464656400",
  "capture_start": "002b8c2c",
  "capture_bytes": 29,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcab88`](#insn-00bcab88)

~~~json
{
  "source": "00bcab88",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcab90`](#insn-00bcab90)

~~~json
{
  "source": "00bcab90",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcab98`](#insn-00bcab98)

~~~json
{
  "source": "00bcab98",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaba0`](#insn-00bcaba0)

~~~json
{
  "source": "00bcaba0",
  "target": "00bcabbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaba4`](#insn-00bcaba4)

~~~json
{
  "source": "00bcaba4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcaba8`](#insn-00bcaba8)

~~~json
{
  "source": "00bcaba8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabac`](#insn-00bcabac)

~~~json
{
  "source": "00bcabac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabb0`](#insn-00bcabb0)

~~~json
{
  "source": "00bcabb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabbc`](#insn-00bcabbc)

~~~json
{
  "source": "00bcabbc",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
