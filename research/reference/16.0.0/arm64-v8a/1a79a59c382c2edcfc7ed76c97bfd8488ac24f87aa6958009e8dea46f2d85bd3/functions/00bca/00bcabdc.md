# 00bcabdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5b6dc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5b/00b5b6dc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-3d43daa303f7d6cef0453c970139b580)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcb004`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcb/00bcb004.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-e22b7275a268ee6e93fe075596277361)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcabdc",
  "name": "_ZN8firebase4auth4Auth18AddIdTokenListenerEPNS0_15IdTokenListenerE",
  "size": 444,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a80823bf55d0e2dbc21b7ff941933b87a91f6f001da373ad23dc18375a591e25",
  "source_text_sha256": "a80823bf55d0e2dbc21b7ff941933b87a91f6f001da373ad23dc18375a591e25",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcabdc",
        "00bcad97"
      ]
    ],
    "bytes_sha256": "5a5640755054cd416f0cec642a142b400de213a71504a92efd6cc8f5776ebb6d",
    "instruction_count": 111,
    "instruction_bytes": 444,
    "body_bytes": 444,
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
- [00c5d5e0](../00c5d/00c5d5e0.md)
- [00c5d6d0](../00c5d/00c5d6d0.md)
- [00c5d710](../00c5d/00c5d710.md)

## 関連文字列（未確認候補）

~~~text
"listener_added == auth_added"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2614 bytes

~~~c

void _ZN8firebase4auth4Auth18AddIdTokenListenerEPNS0_15IdTokenListenerE(long *param_1,long *param_2)

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
  if (*param_1 == 0) goto LAB_00bcad6c;
  lVar3 = *param_1 + 0x268;
  _ZN8firebase5Mutex7AcquireEv(lVar3);
  lVar7 = *param_1;
  plVar10 = *(long **)(lVar7 + 0x248);
  plVar8 = *(long **)(lVar7 + 0x250);
  local_58 = param_1;
  plStack_50 = param_2;
  if ((plVar10 == plVar8) || ((long *)*plVar10 == param_2)) {
    if (plVar10 == plVar8) goto LAB_00bcac7c;
LAB_00bcac68:
    bVar6 = false;
  }
  else {
    do {
      if (plVar8 + -1 == plVar10) goto LAB_00bcac7c;
      plVar1 = plVar10 + 1;
      plVar10 = plVar10 + 1;
    } while ((long *)*plVar1 != param_2);
    if (plVar10 != plVar8) goto LAB_00bcac68;
LAB_00bcac7c:
    if (plVar8 == *(long **)(lVar7 + 600)) {
      _ZNSt6__ndk16vectorIPN8firebase4auth15IdTokenListenerENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (lVar7 + 0x248,&plStack_50);
    }
    else {
      *plVar8 = (long)param_2;
      *(long **)(lVar7 + 0x250) = plVar8 + 1;
    }
    bVar6 = true;
  }
  puVar9 = (undefined8 *)param_2[1];
  puVar4 = (undefined8 *)param_2[2];
  if ((puVar9 == puVar4) || ((long *)*puVar9 == local_58)) {
    if (puVar9 == puVar4) goto LAB_00bcacfc;
LAB_00bcace8:
    if (bVar6) {
LAB_00bcad58:
      _ZN8firebase9LogAssertEPKcz("listener_added == auth_added");
    }
  }
  else {
    do {
      if (puVar4 + -1 == puVar9) goto LAB_00bcacfc;
      puVar2 = puVar9 + 1;
      puVar9 = puVar9 + 1;
    } while ((long *)*puVar2 != local_58);
    if (puVar9 != puVar4) goto LAB_00bcace8;
LAB_00bcacfc:
    if (puVar4 == (undefined8 *)param_2[3]) {
      _ZNSt6__ndk16vectorIPN8firebase4auth4AuthENS_9allocatorIS4_EEE21__push_back_slow_pathIRKS4_EEvOT_
                (param_2 + 1,&local_58);
    }
    else {
      *puVar4 = local_58;
      param_2[2] = (long)(puVar4 + 1);
    }
    if (!bVar6) goto LAB_00bcad58;
    lVar7 = *param_1;
    if (*(char *)(lVar7 + 0x2b9) == '\0') {
      (**(code **)(*param_2 + 0x10))(param_2,param_1);
      lVar7 = *param_1;
    }
    _ZN8firebase4auth22EnableTokenAutoRefreshEPNS0_8AuthDataE(lVar7);
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar3);
LAB_00bcad6c:
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
<a id="insn-00bcabdc"></a> `00bcabdc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcabe0"></a> `00bcabe0` | `f7 13 00 f9` | str x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcabe4"></a> `00bcabe4` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcabe8"></a> `00bcabe8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcabec"></a> `00bcabec` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcabf0"></a> `00bcabf0` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bcabf4"></a> `00bcabf4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcabf8"></a> `00bcabf8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcabfc"></a> `00bcabfc` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcac00"></a> `00bcac00` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcac04"></a> `00bcac04` | `48 0b 00 b4` | cbz x8,0x00bcad6c | `CONDITIONAL_JUMP`
<a id="insn-00bcac08"></a> `00bcac08` | `13 a1 09 91` | add x19,x8,#0x268 | `FALL_THROUGH`
<a id="insn-00bcac0c"></a> `00bcac0c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcac10"></a> `00bcac10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcac14"></a> `00bcac14` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bcac18"></a> `00bcac18` | `7a 3e 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bcac1c"></a> `00bcac1c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcac20"></a> `00bcac20` | `f4 d7 00 a9` | stp x20,x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcac24"></a> `00bcac24` | `0a 25 41 f9` | ldr x10,[x8, #0x248] | `FALL_THROUGH`
<a id="insn-00bcac28"></a> `00bcac28` | `09 29 41 f9` | ldr x9,[x8, #0x250] | `FALL_THROUGH`
<a id="insn-00bcac2c"></a> `00bcac2c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcac30"></a> `00bcac30` | `00 02 00 54` | b.eq 0x00bcac70 | `CONDITIONAL_JUMP`
<a id="insn-00bcac34"></a> `00bcac34` | `4b 01 40 f9` | ldr x11,[x10] | `FALL_THROUGH`
<a id="insn-00bcac38"></a> `00bcac38` | `7f 01 15 eb` | cmp x11,x21 | `FALL_THROUGH`
<a id="insn-00bcac3c"></a> `00bcac3c` | `a0 01 00 54` | b.eq 0x00bcac70 | `CONDITIONAL_JUMP`
<a id="insn-00bcac40"></a> `00bcac40` | `2b 21 00 d1` | sub x11,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcac44"></a> `00bcac44` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcac48"></a> `00bcac48` | `a0 01 00 54` | b.eq 0x00bcac7c | `CONDITIONAL_JUMP`
<a id="insn-00bcac4c"></a> `00bcac4c` | `4d 05 40 f9` | ldr x13,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00bcac50"></a> `00bcac50` | `4c 21 00 91` | add x12,x10,#0x8 | `FALL_THROUGH`
<a id="insn-00bcac54"></a> `00bcac54` | `ea 03 0c aa` | mov x10,x12 | `FALL_THROUGH`
<a id="insn-00bcac58"></a> `00bcac58` | `bf 01 15 eb` | cmp x13,x21 | `FALL_THROUGH`
<a id="insn-00bcac5c"></a> `00bcac5c` | `41 ff ff 54` | b.ne 0x00bcac44 | `CONDITIONAL_JUMP`
<a id="insn-00bcac60"></a> `00bcac60` | `9f 01 09 eb` | cmp x12,x9 | `FALL_THROUGH`
<a id="insn-00bcac64"></a> `00bcac64` | `c0 00 00 54` | b.eq 0x00bcac7c | `CONDITIONAL_JUMP`
<a id="insn-00bcac68"></a> `00bcac68` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00bcac6c"></a> `00bcac6c` | `0e 00 00 14` | b 0x00bcaca4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcac70"></a> `00bcac70` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00bcac74"></a> `00bcac74` | `9f 01 09 eb` | cmp x12,x9 | `FALL_THROUGH`
<a id="insn-00bcac78"></a> `00bcac78` | `81 ff ff 54` | b.ne 0x00bcac68 | `CONDITIONAL_JUMP`
<a id="insn-00bcac7c"></a> `00bcac7c` | `0a 2d 41 f9` | ldr x10,[x8, #0x258] | `FALL_THROUGH`
<a id="insn-00bcac80"></a> `00bcac80` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcac84"></a> `00bcac84` | `80 00 00 54` | b.eq 0x00bcac94 | `CONDITIONAL_JUMP`
<a id="insn-00bcac88"></a> `00bcac88` | `35 85 00 f8` | str x21,[x9], #0x8 | `FALL_THROUGH`
<a id="insn-00bcac8c"></a> `00bcac8c` | `09 29 01 f9` | str x9,[x8, #0x250] | `FALL_THROUGH`
<a id="insn-00bcac90"></a> `00bcac90` | `04 00 00 14` | b 0x00bcaca0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcac94"></a> `00bcac94` | `00 21 09 91` | add x0,x8,#0x248 | `FALL_THROUGH`
<a id="insn-00bcac98"></a> `00bcac98` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcac9c"></a> `00bcac9c` | `8d 4a 02 94` | bl 0x00c5d6d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcaca0"></a> `00bcaca0` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bcaca4"></a> `00bcaca4` | `a9 a2 40 a9` | ldp x9,x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcaca8"></a> `00bcaca8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcacac"></a> `00bcacac` | `20 02 00 54` | b.eq 0x00bcacf0 | `CONDITIONAL_JUMP`
<a id="insn-00bcacb0"></a> `00bcacb0` | `ea 07 40 f9` | ldr x10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcacb4"></a> `00bcacb4` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bcacb8"></a> `00bcacb8` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcacbc"></a> `00bcacbc` | `a0 01 00 54` | b.eq 0x00bcacf0 | `CONDITIONAL_JUMP`
<a id="insn-00bcacc0"></a> `00bcacc0` | `0b 21 00 d1` | sub x11,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bcacc4"></a> `00bcacc4` | `7f 01 09 eb` | cmp x11,x9 | `FALL_THROUGH`
<a id="insn-00bcacc8"></a> `00bcacc8` | `a0 01 00 54` | b.eq 0x00bcacfc | `CONDITIONAL_JUMP`
<a id="insn-00bcaccc"></a> `00bcaccc` | `2d 05 40 f9` | ldr x13,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00bcacd0"></a> `00bcacd0` | `2c 21 00 91` | add x12,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bcacd4"></a> `00bcacd4` | `e9 03 0c aa` | mov x9,x12 | `FALL_THROUGH`
<a id="insn-00bcacd8"></a> `00bcacd8` | `bf 01 0a eb` | cmp x13,x10 | `FALL_THROUGH`
<a id="insn-00bcacdc"></a> `00bcacdc` | `41 ff ff 54` | b.ne 0x00bcacc4 | `CONDITIONAL_JUMP`
<a id="insn-00bcace0"></a> `00bcace0` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bcace4"></a> `00bcace4` | `c0 00 00 54` | b.eq 0x00bcacfc | `CONDITIONAL_JUMP`
<a id="insn-00bcace8"></a> `00bcace8` | `97 03 00 35` | cbnz w23,0x00bcad58 | `CONDITIONAL_JUMP`
<a id="insn-00bcacec"></a> `00bcacec` | `1e 00 00 14` | b 0x00bcad64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcacf0"></a> `00bcacf0` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bcacf4"></a> `00bcacf4` | `9f 01 08 eb` | cmp x12,x8 | `FALL_THROUGH`
<a id="insn-00bcacf8"></a> `00bcacf8` | `81 ff ff 54` | b.ne 0x00bcace8 | `CONDITIONAL_JUMP`
<a id="insn-00bcacfc"></a> `00bcacfc` | `a9 0e 40 f9` | ldr x9,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00bcad00"></a> `00bcad00` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcad04"></a> `00bcad04` | `c0 00 00 54` | b.eq 0x00bcad1c | `CONDITIONAL_JUMP`
<a id="insn-00bcad08"></a> `00bcad08` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bcad0c"></a> `00bcad0c` | `09 85 00 f8` | str x9,[x8], #0x8 | `FALL_THROUGH`
<a id="insn-00bcad10"></a> `00bcad10` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bcad14"></a> `00bcad14` | `d7 00 00 37` | tbnz w23,#0x0,0x00bcad2c | `CONDITIONAL_JUMP`
<a id="insn-00bcad18"></a> `00bcad18` | `10 00 00 14` | b 0x00bcad58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcad1c"></a> `00bcad1c` | `a0 22 00 91` | add x0,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bcad20"></a> `00bcad20` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcad24"></a> `00bcad24` | `7b 4a 02 94` | bl 0x00c5d710 | `UNCONDITIONAL_CALL`
<a id="insn-00bcad28"></a> `00bcad28` | `97 01 00 36` | tbz w23,#0x0,0x00bcad58 | `CONDITIONAL_JUMP`
<a id="insn-00bcad2c"></a> `00bcad2c` | `80 02 40 f9` | ldr x0,[x20] | `FALL_THROUGH`
<a id="insn-00bcad30"></a> `00bcad30` | `08 e4 4a 39` | ldrb w8,[x0, #0x2b9] | `FALL_THROUGH`
<a id="insn-00bcad34"></a> `00bcad34` | `e8 00 00 35` | cbnz w8,0x00bcad50 | `CONDITIONAL_JUMP`
<a id="insn-00bcad38"></a> `00bcad38` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcad3c"></a> `00bcad3c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00bcad40"></a> `00bcad40` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcad44"></a> `00bcad44` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcad48"></a> `00bcad48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcad4c"></a> `00bcad4c` | `80 02 40 f9` | ldr x0,[x20] | `FALL_THROUGH`
<a id="insn-00bcad50"></a> `00bcad50` | `24 4a 02 94` | bl 0x00c5d5e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcad54"></a> `00bcad54` | `04 00 00 14` | b 0x00bcad64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcad58"></a> `00bcad58` | `60 b7 ff d0` | adrp x0,0x2b8000 | `FALL_THROUGH`
<a id="insn-00bcad5c"></a> `00bcad5c` | `00 b0 30 91` | add x0,x0,#0xc2c | `FALL_THROUGH`
<a id="insn-00bcad60"></a> `00bcad60` | `a8 3f 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcad64"></a> `00bcad64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcad68"></a> `00bcad68` | `2a 3e 02 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00bcad6c"></a> `00bcad6c` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcad70"></a> `00bcad70` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcad74"></a> `00bcad74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcad78"></a> `00bcad78` | `e1 00 00 54` | b.ne 0x00bcad94 | `CONDITIONAL_JUMP`
<a id="insn-00bcad7c"></a> `00bcad7c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcad80"></a> `00bcad80` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcad84"></a> `00bcad84` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcad88"></a> `00bcad88` | `f7 13 40 f9` | ldr x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcad8c"></a> `00bcad8c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcad90"></a> `00bcad90` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcad94"></a> `00bcad94` | `53 33 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcabdc`](#insn-00bcabdc) 範囲 `[['00bcabdc', '00bcac07']]`
  - `CONDITIONAL_JUMP` [`00bcac04`](#insn-00bcac04) → [`00bcad6c`](#insn-00bcad6c)
  - `FALL_THROUGH` [`00bcac04`](#insn-00bcac04) → [`00bcac08`](#insn-00bcac08)
- ブロック [`00bcac08`](#insn-00bcac08) 範囲 `[['00bcac08', '00bcac33']]`
  - `CONDITIONAL_JUMP` [`00bcac30`](#insn-00bcac30) → [`00bcac70`](#insn-00bcac70)
  - `FALL_THROUGH` [`00bcac30`](#insn-00bcac30) → [`00bcac34`](#insn-00bcac34)
- ブロック [`00bcac34`](#insn-00bcac34) 範囲 `[['00bcac34', '00bcac3f']]`
  - `CONDITIONAL_JUMP` [`00bcac3c`](#insn-00bcac3c) → [`00bcac70`](#insn-00bcac70)
  - `FALL_THROUGH` [`00bcac3c`](#insn-00bcac3c) → [`00bcac40`](#insn-00bcac40)
- ブロック [`00bcac40`](#insn-00bcac40) 範囲 `[['00bcac40', '00bcac43']]`
  - `FALL_THROUGH` [`00bcac40`](#insn-00bcac40) → [`00bcac44`](#insn-00bcac44)
- ブロック [`00bcac44`](#insn-00bcac44) 範囲 `[['00bcac44', '00bcac4b']]`
  - `CONDITIONAL_JUMP` [`00bcac48`](#insn-00bcac48) → [`00bcac7c`](#insn-00bcac7c)
  - `FALL_THROUGH` [`00bcac48`](#insn-00bcac48) → [`00bcac4c`](#insn-00bcac4c)
- ブロック [`00bcac4c`](#insn-00bcac4c) 範囲 `[['00bcac4c', '00bcac5f']]`
  - `CONDITIONAL_JUMP` [`00bcac5c`](#insn-00bcac5c) → [`00bcac44`](#insn-00bcac44)
  - `FALL_THROUGH` [`00bcac5c`](#insn-00bcac5c) → [`00bcac60`](#insn-00bcac60)
- ブロック [`00bcac60`](#insn-00bcac60) 範囲 `[['00bcac60', '00bcac67']]`
  - `CONDITIONAL_JUMP` [`00bcac64`](#insn-00bcac64) → [`00bcac7c`](#insn-00bcac7c)
  - `FALL_THROUGH` [`00bcac64`](#insn-00bcac64) → [`00bcac68`](#insn-00bcac68)
- ブロック [`00bcac68`](#insn-00bcac68) 範囲 `[['00bcac68', '00bcac6f']]`
  - `UNCONDITIONAL_JUMP` [`00bcac6c`](#insn-00bcac6c) → [`00bcaca4`](#insn-00bcaca4)
- ブロック [`00bcac70`](#insn-00bcac70) 範囲 `[['00bcac70', '00bcac7b']]`
  - `CONDITIONAL_JUMP` [`00bcac78`](#insn-00bcac78) → [`00bcac68`](#insn-00bcac68)
  - `FALL_THROUGH` [`00bcac78`](#insn-00bcac78) → [`00bcac7c`](#insn-00bcac7c)
- ブロック [`00bcac7c`](#insn-00bcac7c) 範囲 `[['00bcac7c', '00bcac87']]`
  - `CONDITIONAL_JUMP` [`00bcac84`](#insn-00bcac84) → [`00bcac94`](#insn-00bcac94)
  - `FALL_THROUGH` [`00bcac84`](#insn-00bcac84) → [`00bcac88`](#insn-00bcac88)
- ブロック [`00bcac88`](#insn-00bcac88) 範囲 `[['00bcac88', '00bcac93']]`
  - `UNCONDITIONAL_JUMP` [`00bcac90`](#insn-00bcac90) → [`00bcaca0`](#insn-00bcaca0)
- ブロック [`00bcac94`](#insn-00bcac94) 範囲 `[['00bcac94', '00bcac9f']]`
  - `FALL_THROUGH` [`00bcac9c`](#insn-00bcac9c) → [`00bcaca0`](#insn-00bcaca0)
- ブロック [`00bcaca0`](#insn-00bcaca0) 範囲 `[['00bcaca0', '00bcaca3']]`
  - `FALL_THROUGH` [`00bcaca0`](#insn-00bcaca0) → [`00bcaca4`](#insn-00bcaca4)
- ブロック [`00bcaca4`](#insn-00bcaca4) 範囲 `[['00bcaca4', '00bcacaf']]`
  - `CONDITIONAL_JUMP` [`00bcacac`](#insn-00bcacac) → [`00bcacf0`](#insn-00bcacf0)
  - `FALL_THROUGH` [`00bcacac`](#insn-00bcacac) → [`00bcacb0`](#insn-00bcacb0)
- ブロック [`00bcacb0`](#insn-00bcacb0) 範囲 `[['00bcacb0', '00bcacbf']]`
  - `CONDITIONAL_JUMP` [`00bcacbc`](#insn-00bcacbc) → [`00bcacf0`](#insn-00bcacf0)
  - `FALL_THROUGH` [`00bcacbc`](#insn-00bcacbc) → [`00bcacc0`](#insn-00bcacc0)
- ブロック [`00bcacc0`](#insn-00bcacc0) 範囲 `[['00bcacc0', '00bcacc3']]`
  - `FALL_THROUGH` [`00bcacc0`](#insn-00bcacc0) → [`00bcacc4`](#insn-00bcacc4)
- ブロック [`00bcacc4`](#insn-00bcacc4) 範囲 `[['00bcacc4', '00bcaccb']]`
  - `CONDITIONAL_JUMP` [`00bcacc8`](#insn-00bcacc8) → [`00bcacfc`](#insn-00bcacfc)
  - `FALL_THROUGH` [`00bcacc8`](#insn-00bcacc8) → [`00bcaccc`](#insn-00bcaccc)
- ブロック [`00bcaccc`](#insn-00bcaccc) 範囲 `[['00bcaccc', '00bcacdf']]`
  - `CONDITIONAL_JUMP` [`00bcacdc`](#insn-00bcacdc) → [`00bcacc4`](#insn-00bcacc4)
  - `FALL_THROUGH` [`00bcacdc`](#insn-00bcacdc) → [`00bcace0`](#insn-00bcace0)
- ブロック [`00bcace0`](#insn-00bcace0) 範囲 `[['00bcace0', '00bcace7']]`
  - `CONDITIONAL_JUMP` [`00bcace4`](#insn-00bcace4) → [`00bcacfc`](#insn-00bcacfc)
  - `FALL_THROUGH` [`00bcace4`](#insn-00bcace4) → [`00bcace8`](#insn-00bcace8)
- ブロック [`00bcace8`](#insn-00bcace8) 範囲 `[['00bcace8', '00bcaceb']]`
  - `CONDITIONAL_JUMP` [`00bcace8`](#insn-00bcace8) → [`00bcad58`](#insn-00bcad58)
  - `FALL_THROUGH` [`00bcace8`](#insn-00bcace8) → [`00bcacec`](#insn-00bcacec)
- ブロック [`00bcacec`](#insn-00bcacec) 範囲 `[['00bcacec', '00bcacef']]`
  - `UNCONDITIONAL_JUMP` [`00bcacec`](#insn-00bcacec) → [`00bcad64`](#insn-00bcad64)
- ブロック [`00bcacf0`](#insn-00bcacf0) 範囲 `[['00bcacf0', '00bcacfb']]`
  - `CONDITIONAL_JUMP` [`00bcacf8`](#insn-00bcacf8) → [`00bcace8`](#insn-00bcace8)
  - `FALL_THROUGH` [`00bcacf8`](#insn-00bcacf8) → [`00bcacfc`](#insn-00bcacfc)
- ブロック [`00bcacfc`](#insn-00bcacfc) 範囲 `[['00bcacfc', '00bcad07']]`
  - `CONDITIONAL_JUMP` [`00bcad04`](#insn-00bcad04) → [`00bcad1c`](#insn-00bcad1c)
  - `FALL_THROUGH` [`00bcad04`](#insn-00bcad04) → [`00bcad08`](#insn-00bcad08)
- ブロック [`00bcad08`](#insn-00bcad08) 範囲 `[['00bcad08', '00bcad17']]`
  - `CONDITIONAL_JUMP` [`00bcad14`](#insn-00bcad14) → [`00bcad2c`](#insn-00bcad2c)
  - `FALL_THROUGH` [`00bcad14`](#insn-00bcad14) → [`00bcad18`](#insn-00bcad18)
- ブロック [`00bcad18`](#insn-00bcad18) 範囲 `[['00bcad18', '00bcad1b']]`
  - `UNCONDITIONAL_JUMP` [`00bcad18`](#insn-00bcad18) → [`00bcad58`](#insn-00bcad58)
- ブロック [`00bcad1c`](#insn-00bcad1c) 範囲 `[['00bcad1c', '00bcad2b']]`
  - `CONDITIONAL_JUMP` [`00bcad28`](#insn-00bcad28) → [`00bcad58`](#insn-00bcad58)
  - `FALL_THROUGH` [`00bcad28`](#insn-00bcad28) → [`00bcad2c`](#insn-00bcad2c)
- ブロック [`00bcad2c`](#insn-00bcad2c) 範囲 `[['00bcad2c', '00bcad37']]`
  - `CONDITIONAL_JUMP` [`00bcad34`](#insn-00bcad34) → [`00bcad50`](#insn-00bcad50)
  - `FALL_THROUGH` [`00bcad34`](#insn-00bcad34) → [`00bcad38`](#insn-00bcad38)
- ブロック [`00bcad38`](#insn-00bcad38) 範囲 `[['00bcad38', '00bcad4f']]`
  - `FALL_THROUGH` [`00bcad4c`](#insn-00bcad4c) → [`00bcad50`](#insn-00bcad50)
- ブロック [`00bcad50`](#insn-00bcad50) 範囲 `[['00bcad50', '00bcad57']]`
  - `UNCONDITIONAL_JUMP` [`00bcad54`](#insn-00bcad54) → [`00bcad64`](#insn-00bcad64)
- ブロック [`00bcad58`](#insn-00bcad58) 範囲 `[['00bcad58', '00bcad63']]`
  - `FALL_THROUGH` [`00bcad60`](#insn-00bcad60) → [`00bcad64`](#insn-00bcad64)
- ブロック [`00bcad64`](#insn-00bcad64) 範囲 `[['00bcad64', '00bcad6b']]`
  - `FALL_THROUGH` [`00bcad68`](#insn-00bcad68) → [`00bcad6c`](#insn-00bcad6c)
- ブロック [`00bcad6c`](#insn-00bcad6c) 範囲 `[['00bcad6c', '00bcad7b']]`
  - `CONDITIONAL_JUMP` [`00bcad78`](#insn-00bcad78) → [`00bcad94`](#insn-00bcad94)
  - `FALL_THROUGH` [`00bcad78`](#insn-00bcad78) → [`00bcad7c`](#insn-00bcad7c)
- ブロック [`00bcad7c`](#insn-00bcad7c) 範囲 `[['00bcad7c', '00bcad93']]`
- ブロック [`00bcad94`](#insn-00bcad94) 範囲 `[['00bcad94', '00bcad97']]`

## 命令位置別の参照

- [`00bcabe0`](#insn-00bcabe0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabe4`](#insn-00bcabe4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabe8`](#insn-00bcabe8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabec`](#insn-00bcabec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcabfc`](#insn-00bcabfc) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac04`](#insn-00bcac04) → [`00bcad6c`](#insn-00bcad6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac18`](#insn-00bcac18) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bcac20`](#insn-00bcac20) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac30`](#insn-00bcac30) → [`00bcac70`](#insn-00bcac70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac3c`](#insn-00bcac3c) → [`00bcac70`](#insn-00bcac70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac48`](#insn-00bcac48) → [`00bcac7c`](#insn-00bcac7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac5c`](#insn-00bcac5c) → [`00bcac44`](#insn-00bcac44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac64`](#insn-00bcac64) → [`00bcac7c`](#insn-00bcac7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac6c`](#insn-00bcac6c) → [`00bcaca4`](#insn-00bcaca4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac78`](#insn-00bcac78) → [`00bcac68`](#insn-00bcac68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac84`](#insn-00bcac84) → [`00bcac94`](#insn-00bcac94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac90`](#insn-00bcac90) → [`00bcaca0`](#insn-00bcaca0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcac9c`](#insn-00bcac9c) → [`00c5d6d0`](../00c5d/00c5d6d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d6d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcacac`](#insn-00bcacac) → [`00bcacf0`](#insn-00bcacf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacb0`](#insn-00bcacb0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacbc`](#insn-00bcacbc) → [`00bcacf0`](#insn-00bcacf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacc8`](#insn-00bcacc8) → [`00bcacfc`](#insn-00bcacfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacdc`](#insn-00bcacdc) → [`00bcacc4`](#insn-00bcacc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcace4`](#insn-00bcace4) → [`00bcacfc`](#insn-00bcacfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcace8`](#insn-00bcace8) → [`00bcad58`](#insn-00bcad58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacec`](#insn-00bcacec) → [`00bcad64`](#insn-00bcad64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcacf8`](#insn-00bcacf8) → [`00bcace8`](#insn-00bcace8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad04`](#insn-00bcad04) → [`00bcad1c`](#insn-00bcad1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad08`](#insn-00bcad08) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad14`](#insn-00bcad14) → [`00bcad2c`](#insn-00bcad2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad18`](#insn-00bcad18) → [`00bcad58`](#insn-00bcad58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad24`](#insn-00bcad24) → [`00c5d710`](../00c5d/00c5d710.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d710` · 推定シンボル `None` · 推定型 `None`
- [`00bcad28`](#insn-00bcad28) → [`00bcad58`](#insn-00bcad58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad34`](#insn-00bcad34) → [`00bcad50`](#insn-00bcad50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad50`](#insn-00bcad50) → [`00c5d5e0`](../00c5d/00c5d5e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d5e0` · 推定シンボル `None` · 推定型 `None`
- [`00bcad54`](#insn-00bcad54) → [`00bcad64`](#insn-00bcad64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad5c`](#insn-00bcad5c) → `002b8c2c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcad60`](#insn-00bcad60) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bcad68`](#insn-00bcad68) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bcad70`](#insn-00bcad70) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad78`](#insn-00bcad78) → [`00bcad94`](#insn-00bcad94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad7c`](#insn-00bcad7c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad80`](#insn-00bcad80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad84`](#insn-00bcad84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad88`](#insn-00bcad88) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcad94`](#insn-00bcad94) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcabe0`](#insn-00bcabe0)

~~~json
{
  "source": "00bcabe0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabe4`](#insn-00bcabe4)

~~~json
{
  "source": "00bcabe4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabe8`](#insn-00bcabe8)

~~~json
{
  "source": "00bcabe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabec`](#insn-00bcabec)

~~~json
{
  "source": "00bcabec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcabfc`](#insn-00bcabfc)

~~~json
{
  "source": "00bcabfc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac04`](#insn-00bcac04)

~~~json
{
  "source": "00bcac04",
  "target": "00bcad6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac18`](#insn-00bcac18)

~~~json
{
  "source": "00bcac18",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcac20`](#insn-00bcac20)

~~~json
{
  "source": "00bcac20",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac30`](#insn-00bcac30)

~~~json
{
  "source": "00bcac30",
  "target": "00bcac70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac3c`](#insn-00bcac3c)

~~~json
{
  "source": "00bcac3c",
  "target": "00bcac70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac48`](#insn-00bcac48)

~~~json
{
  "source": "00bcac48",
  "target": "00bcac7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac5c`](#insn-00bcac5c)

~~~json
{
  "source": "00bcac5c",
  "target": "00bcac44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac64`](#insn-00bcac64)

~~~json
{
  "source": "00bcac64",
  "target": "00bcac7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac6c`](#insn-00bcac6c)

~~~json
{
  "source": "00bcac6c",
  "target": "00bcaca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac78`](#insn-00bcac78)

~~~json
{
  "source": "00bcac78",
  "target": "00bcac68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac84`](#insn-00bcac84)

~~~json
{
  "source": "00bcac84",
  "target": "00bcac94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac90`](#insn-00bcac90)

~~~json
{
  "source": "00bcac90",
  "target": "00bcaca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcac9c`](#insn-00bcac9c)

~~~json
{
  "source": "00bcac9c",
  "target": "00c5d6d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcacac`](#insn-00bcacac)

~~~json
{
  "source": "00bcacac",
  "target": "00bcacf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacb0`](#insn-00bcacb0)

~~~json
{
  "source": "00bcacb0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacbc`](#insn-00bcacbc)

~~~json
{
  "source": "00bcacbc",
  "target": "00bcacf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacc8`](#insn-00bcacc8)

~~~json
{
  "source": "00bcacc8",
  "target": "00bcacfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacdc`](#insn-00bcacdc)

~~~json
{
  "source": "00bcacdc",
  "target": "00bcacc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcace4`](#insn-00bcace4)

~~~json
{
  "source": "00bcace4",
  "target": "00bcacfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcace8`](#insn-00bcace8)

~~~json
{
  "source": "00bcace8",
  "target": "00bcad58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacec`](#insn-00bcacec)

~~~json
{
  "source": "00bcacec",
  "target": "00bcad64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcacf8`](#insn-00bcacf8)

~~~json
{
  "source": "00bcacf8",
  "target": "00bcace8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad04`](#insn-00bcad04)

~~~json
{
  "source": "00bcad04",
  "target": "00bcad1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad08`](#insn-00bcad08)

~~~json
{
  "source": "00bcad08",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad14`](#insn-00bcad14)

~~~json
{
  "source": "00bcad14",
  "target": "00bcad2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad18`](#insn-00bcad18)

~~~json
{
  "source": "00bcad18",
  "target": "00bcad58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad24`](#insn-00bcad24)

~~~json
{
  "source": "00bcad24",
  "target": "00c5d710",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcad28`](#insn-00bcad28)

~~~json
{
  "source": "00bcad28",
  "target": "00bcad58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad34`](#insn-00bcad34)

~~~json
{
  "source": "00bcad34",
  "target": "00bcad50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad50`](#insn-00bcad50)

~~~json
{
  "source": "00bcad50",
  "target": "00c5d5e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcad54`](#insn-00bcad54)

~~~json
{
  "source": "00bcad54",
  "target": "00bcad64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad5c`](#insn-00bcad5c)

~~~json
{
  "source": "00bcad5c",
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
- 参照命令 [`00bcad60`](#insn-00bcad60)

~~~json
{
  "source": "00bcad60",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcad68`](#insn-00bcad68)

~~~json
{
  "source": "00bcad68",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcad70`](#insn-00bcad70)

~~~json
{
  "source": "00bcad70",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad78`](#insn-00bcad78)

~~~json
{
  "source": "00bcad78",
  "target": "00bcad94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad7c`](#insn-00bcad7c)

~~~json
{
  "source": "00bcad7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad80`](#insn-00bcad80)

~~~json
{
  "source": "00bcad80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad84`](#insn-00bcad84)

~~~json
{
  "source": "00bcad84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad88`](#insn-00bcad88)

~~~json
{
  "source": "00bcad88",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcad94`](#insn-00bcad94)

~~~json
{
  "source": "00bcad94",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
