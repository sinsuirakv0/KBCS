# 00bffef4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b834ac`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b83/00b834ac.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-6acd595454765148259a801839c7ac6c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00c0031c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00c00/00c0031c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0087.md#compare-614bd4045480f7d9f2f5348c512599b0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffef4",
  "name": "_ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6sentryC1ERS3_b",
  "size": 476,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97fc733b2d7801eb2c1893d1a192f4a003aba6a01ea5d4bb6364dd9aec12926b",
  "source_text_sha256": "97fc733b2d7801eb2c1893d1a192f4a003aba6a01ea5d4bb6364dd9aec12926b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffef4",
        "00c000cf"
      ]
    ],
    "bytes_sha256": "bd0eb490002f8183c4f3269bb211cf0a79e607269e1c528086949bfb92533e5e",
    "instruction_count": 119,
    "instruction_bytes": 476,
    "body_bytes": 476,
    "indirect": 5,
    "unresolved": 5
  }
}
~~~

## 呼び出し元

- [00c5e020](../00c5e/00c5e020.md)

## 呼び出し先

- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ea0](../00c57/00c57ea0.md)
- [00c5dff0](../00c5d/00c5dff0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2464 bytes

~~~c

void _ZNSt6__ndk113basic_istreamIwNS_11char_traitsIwEEE6sentryC1ERS3_b
               (undefined1 *param_1,long *param_2,ulong param_3)

{
  long lVar1;
  undefined4 uVar2;
  int iVar3;
  long *plVar4;
  ulong uVar5;
  long lVar6;
  long *plVar7;
  undefined1 auStack_38 [8];
  
  lVar6 = *param_2;
  *param_1 = 0;
  lVar1 = (long)param_2 + *(long *)(lVar6 + -0x18);
  if (*(uint *)(lVar1 + 0x20) != 0) {
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | 4);
    return;
  }
  if (*(long *)(lVar1 + 0x88) != 0) {
    param_3 = param_3 & 0xffffffff;
    _ZNSt6__ndk113basic_ostreamIwNS_11char_traitsIwEEE5flushEv();
    lVar6 = *param_2;
  }
  if (((param_3 & 1) == 0) &&
     ((*(byte *)((long)param_2 + *(long *)(lVar6 + -0x18) + 9) >> 4 & 1) != 0)) {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_38);
    plVar4 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_38,PTR__ZNSt6__ndk15ctypeIwE2idE_00c9b740);
    _ZNSt6__ndk16localeD1Ev(auStack_38);
    plVar7 = *(long **)((long)param_2 + *(long *)(*param_2 + -0x18) + 0x28);
    while (plVar7 != (long *)0x0) {
      while( true ) {
        if ((int *)plVar7[3] == (int *)plVar7[4]) {
          iVar3 = (**(code **)(*plVar7 + 0x48))(plVar7);
        }
        else {
          iVar3 = *(int *)plVar7[3];
        }
        if (iVar3 == -1) goto LAB_00c00050;
        if ((undefined4 *)plVar7[3] == (undefined4 *)plVar7[4]) {
          uVar2 = (**(code **)(*plVar7 + 0x48))(plVar7);
        }
        else {
          uVar2 = *(undefined4 *)plVar7[3];
        }
        uVar5 = (**(code **)(*plVar4 + 0x18))(plVar4,1,uVar2);
        if ((uVar5 & 1) == 0) {
          if ((int *)plVar7[3] == (int *)plVar7[4]) {
            iVar3 = (**(code **)(*plVar7 + 0x48))(plVar7);
          }
          else {
            iVar3 = *(int *)plVar7[3];
          }
          lVar6 = *param_2;
          if (iVar3 != -1) goto LAB_00c0006c;
          goto LAB_00c00054;
        }
        if (plVar7[3] == plVar7[4]) break;
        plVar7[3] = plVar7[3] + 4;
        if (plVar7 == (long *)0x0) goto LAB_00c00050;
      }
      (**(code **)(*plVar7 + 0x50))(plVar7);
    }
LAB_00c00050:
    lVar6 = *param_2;
LAB_00c00054:
    lVar1 = (long)param_2 + *(long *)(lVar6 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | 6);
    lVar6 = *param_2;
  }
LAB_00c0006c:
  *param_1 = *(int *)((long)param_2 + *(long *)(lVar6 + -0x18) + 0x20) == 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffef4"></a> `00bffef4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bffef8"></a> `00bffef8` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bffefc"></a> `00bffefc` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfff00"></a> `00bfff00` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfff04"></a> `00bfff04` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfff08"></a> `00bfff08` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfff0c"></a> `00bfff0c` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bfff10"></a> `00bfff10` | `1f 00 00 39` | strb wzr,[x0] | `FALL_THROUGH`
<a id="insn-00bfff14"></a> `00bfff14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfff18"></a> `00bfff18` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfff1c"></a> `00bfff1c` | `20 00 09 8b` | add x0,x1,x9 | `FALL_THROUGH`
<a id="insn-00bfff20"></a> `00bfff20` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfff24"></a> `00bfff24` | `09 01 00 34` | cbz w9,0x00bfff44 | `CONDITIONAL_JUMP`
<a id="insn-00bfff28"></a> `00bfff28` | `21 01 1e 32` | orr w1,w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bfff2c"></a> `00bfff2c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfff30"></a> `00bfff30` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfff34"></a> `00bfff34` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfff38"></a> `00bfff38` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfff3c"></a> `00bfff3c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfff40"></a> `00bfff40` | `d8 5f 01 14` | b 0x00c57ea0 | `CALL_TERMINATOR`
<a id="insn-00bfff44"></a> `00bfff44` | `00 44 40 f9` | ldr x0,[x0, #0x88] | `FALL_THROUGH`
<a id="insn-00bfff48"></a> `00bfff48` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfff4c"></a> `00bfff4c` | `a0 00 00 b4` | cbz x0,0x00bfff60 | `CONDITIONAL_JUMP`
<a id="insn-00bfff50"></a> `00bfff50` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bfff54"></a> `00bfff54` | `27 78 01 94` | bl 0x00c5dff0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfff58"></a> `00bfff58` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfff5c"></a> `00bfff5c` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bfff60"></a> `00bfff60` | `62 08 00 37` | tbnz w2,#0x0,0x00c0006c | `CONDITIONAL_JUMP`
<a id="insn-00bfff64"></a> `00bfff64` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfff68"></a> `00bfff68` | `80 02 09 8b` | add x0,x20,x9 | `FALL_THROUGH`
<a id="insn-00bfff6c"></a> `00bfff6c` | `09 24 40 39` | ldrb w9,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bfff70"></a> `00bfff70` | `e9 07 20 36` | tbz w9,#0x4,0x00c0006c | `CONDITIONAL_JUMP`
<a id="insn-00bfff74"></a> `00bfff74` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfff78"></a> `00bfff78` | `be 5f 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfff7c"></a> `00bfff7c` | `e1 04 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfff80"></a> `00bfff80` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfff84"></a> `00bfff84` | `21 a0 43 f9` | ldr x1,[x1, #0x740] | `FALL_THROUGH`
<a id="insn-00bfff88"></a> `00bfff88` | `be 5f 01 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bfff8c"></a> `00bfff8c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bfff90"></a> `00bfff90` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfff94"></a> `00bfff94` | `bf 5f 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfff98"></a> `00bfff98` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfff9c"></a> `00bfff9c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfffa0"></a> `00bfffa0` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00bfffa4"></a> `00bfffa4` | `16 15 40 f9` | ldr x22,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bfffa8"></a> `00bfffa8` | `f6 00 00 b5` | cbnz x22,0x00bfffc4 | `CONDITIONAL_JUMP`
<a id="insn-00bfffac"></a> `00bfffac` | `29 00 00 14` | b 0x00c00050 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfffb0"></a> `00bfffb0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bfffb4"></a> `00bfffb4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bfffb8"></a> `00bfffb8` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfffbc"></a> `00bfffbc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfffc0"></a> `00bfffc0` | `96 04 00 b4` | cbz x22,0x00c00050 | `CONDITIONAL_JUMP`
<a id="insn-00bfffc4"></a> `00bfffc4` | `c8 a6 41 a9` | ldp x8,x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00bfffc8"></a> `00bfffc8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfffcc"></a> `00bfffcc` | `a0 00 00 54` | b.eq 0x00bfffe0 | `CONDITIONAL_JUMP`
<a id="insn-00bfffd0"></a> `00bfffd0` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfffd4"></a> `00bfffd4` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfffd8"></a> `00bfffd8` | `01 01 00 54` | b.ne 0x00bffff8 | `CONDITIONAL_JUMP`
<a id="insn-00bfffdc"></a> `00bfffdc` | `1d 00 00 14` | b 0x00c00050 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfffe0"></a> `00bfffe0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bfffe4"></a> `00bfffe4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bfffe8"></a> `00bfffe8` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfffec"></a> `00bfffec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bffff0"></a> `00bffff0` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bffff4"></a> `00bffff4` | `e0 02 00 54` | b.eq 0x00c00050 | `CONDITIONAL_JUMP`
<a id="insn-00bffff8"></a> `00bffff8` | `c8 a6 41 a9` | ldp x8,x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00bffffc"></a> `00bffffc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c00000"></a> `00c00000` | `60 00 00 54` | b.eq 0x00c0000c | `CONDITIONAL_JUMP`
<a id="insn-00c00004"></a> `00c00004` | `02 01 40 b9` | ldr w2,[x8] | `FALL_THROUGH`
<a id="insn-00c00008"></a> `00c00008` | `06 00 00 14` | b 0x00c00020 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0000c"></a> `00c0000c` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00c00010"></a> `00c00010` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00c00014"></a> `00c00014` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00c00018"></a> `00c00018` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c0001c"></a> `00c0001c` | `e2 03 00 2a` | mov w2,w0 | `FALL_THROUGH`
<a id="insn-00c00020"></a> `00c00020` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c00024"></a> `00c00024` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c00028"></a> `00c00028` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00c0002c"></a> `00c0002c` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00c00030"></a> `00c00030` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c00034"></a> `00c00034` | `40 03 00 36` | tbz w0,#0x0,0x00c0009c | `CONDITIONAL_JUMP`
<a id="insn-00c00038"></a> `00c00038` | `c8 a6 41 a9` | ldp x8,x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00c0003c"></a> `00c0003c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c00040"></a> `00c00040` | `80 fb ff 54` | b.eq 0x00bfffb0 | `CONDITIONAL_JUMP`
<a id="insn-00c00044"></a> `00c00044` | `08 11 00 91` | add x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00c00048"></a> `00c00048` | `c8 0e 00 f9` | str x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00c0004c"></a> `00c0004c` | `d6 fb ff b5` | cbnz x22,0x00bfffc4 | `CONDITIONAL_JUMP`
<a id="insn-00c00050"></a> `00c00050` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c00054"></a> `00c00054` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00c00058"></a> `00c00058` | `80 02 08 8b` | add x0,x20,x8 | `FALL_THROUGH`
<a id="insn-00c0005c"></a> `00c0005c` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00c00060"></a> `00c00060` | `01 05 1f 32` | orr w1,w8,#0x6 | `FALL_THROUGH`
<a id="insn-00c00064"></a> `00c00064` | `8f 5f 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00c00068"></a> `00c00068` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c0006c"></a> `00c0006c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00c00070"></a> `00c00070` | `88 02 08 8b` | add x8,x20,x8 | `FALL_THROUGH`
<a id="insn-00c00074"></a> `00c00074` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00c00078"></a> `00c00078` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00c0007c"></a> `00c0007c` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00c00080"></a> `00c00080` | `68 02 00 39` | strb w8,[x19] | `FALL_THROUGH`
<a id="insn-00c00084"></a> `00c00084` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c00088"></a> `00c00088` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c0008c"></a> `00c0008c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c00090"></a> `00c00090` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00c00094"></a> `00c00094` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c00098"></a> `00c00098` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c0009c"></a> `00c0009c` | `c8 a6 41 a9` | ldp x8,x9,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00c000a0"></a> `00c000a0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c000a4"></a> `00c000a4` | `60 00 00 54` | b.eq 0x00c000b0 | `CONDITIONAL_JUMP`
<a id="insn-00c000a8"></a> `00c000a8` | `00 01 40 b9` | ldr w0,[x8] | `FALL_THROUGH`
<a id="insn-00c000ac"></a> `00c000ac` | `05 00 00 14` | b 0x00c000c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00c000b0"></a> `00c000b0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00c000b4"></a> `00c000b4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00c000b8"></a> `00c000b8` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00c000bc"></a> `00c000bc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c000c0"></a> `00c000c0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00c000c4"></a> `00c000c4` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00c000c8"></a> `00c000c8` | `21 fd ff 54` | b.ne 0x00c0006c | `CONDITIONAL_JUMP`
<a id="insn-00c000cc"></a> `00c000cc` | `e2 ff ff 17` | b 0x00c00054 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bffef4`](#insn-00bffef4) 範囲 `[['00bffef4', '00bfff27']]`
  - `CONDITIONAL_JUMP` [`00bfff24`](#insn-00bfff24) → [`00bfff44`](#insn-00bfff44)
  - `FALL_THROUGH` [`00bfff24`](#insn-00bfff24) → [`00bfff28`](#insn-00bfff28)
- ブロック [`00bfff28`](#insn-00bfff28) 範囲 `[['00bfff28', '00bfff43']]`
- ブロック [`00bfff44`](#insn-00bfff44) 範囲 `[['00bfff44', '00bfff4f']]`
  - `CONDITIONAL_JUMP` [`00bfff4c`](#insn-00bfff4c) → [`00bfff60`](#insn-00bfff60)
  - `FALL_THROUGH` [`00bfff4c`](#insn-00bfff4c) → [`00bfff50`](#insn-00bfff50)
- ブロック [`00bfff50`](#insn-00bfff50) 範囲 `[['00bfff50', '00bfff5f']]`
  - `FALL_THROUGH` [`00bfff5c`](#insn-00bfff5c) → [`00bfff60`](#insn-00bfff60)
- ブロック [`00bfff60`](#insn-00bfff60) 範囲 `[['00bfff60', '00bfff63']]`
  - `CONDITIONAL_JUMP` [`00bfff60`](#insn-00bfff60) → [`00c0006c`](#insn-00c0006c)
  - `FALL_THROUGH` [`00bfff60`](#insn-00bfff60) → [`00bfff64`](#insn-00bfff64)
- ブロック [`00bfff64`](#insn-00bfff64) 範囲 `[['00bfff64', '00bfff73']]`
  - `CONDITIONAL_JUMP` [`00bfff70`](#insn-00bfff70) → [`00c0006c`](#insn-00c0006c)
  - `FALL_THROUGH` [`00bfff70`](#insn-00bfff70) → [`00bfff74`](#insn-00bfff74)
- ブロック [`00bfff74`](#insn-00bfff74) 範囲 `[['00bfff74', '00bfffab']]`
  - `CONDITIONAL_JUMP` [`00bfffa8`](#insn-00bfffa8) → [`00bfffc4`](#insn-00bfffc4)
  - `FALL_THROUGH` [`00bfffa8`](#insn-00bfffa8) → [`00bfffac`](#insn-00bfffac)
- ブロック [`00bfffac`](#insn-00bfffac) 範囲 `[['00bfffac', '00bfffaf']]`
  - `UNCONDITIONAL_JUMP` [`00bfffac`](#insn-00bfffac) → [`00c00050`](#insn-00c00050)
- ブロック [`00bfffb0`](#insn-00bfffb0) 範囲 `[['00bfffb0', '00bfffc3']]`
  - `CONDITIONAL_JUMP` [`00bfffc0`](#insn-00bfffc0) → [`00c00050`](#insn-00c00050)
  - `FALL_THROUGH` [`00bfffc0`](#insn-00bfffc0) → [`00bfffc4`](#insn-00bfffc4)
- ブロック [`00bfffc4`](#insn-00bfffc4) 範囲 `[['00bfffc4', '00bfffcf']]`
  - `CONDITIONAL_JUMP` [`00bfffcc`](#insn-00bfffcc) → [`00bfffe0`](#insn-00bfffe0)
  - `FALL_THROUGH` [`00bfffcc`](#insn-00bfffcc) → [`00bfffd0`](#insn-00bfffd0)
- ブロック [`00bfffd0`](#insn-00bfffd0) 範囲 `[['00bfffd0', '00bfffdb']]`
  - `CONDITIONAL_JUMP` [`00bfffd8`](#insn-00bfffd8) → [`00bffff8`](#insn-00bffff8)
  - `FALL_THROUGH` [`00bfffd8`](#insn-00bfffd8) → [`00bfffdc`](#insn-00bfffdc)
- ブロック [`00bfffdc`](#insn-00bfffdc) 範囲 `[['00bfffdc', '00bfffdf']]`
  - `UNCONDITIONAL_JUMP` [`00bfffdc`](#insn-00bfffdc) → [`00c00050`](#insn-00c00050)
- ブロック [`00bfffe0`](#insn-00bfffe0) 範囲 `[['00bfffe0', '00bffff7']]`
  - `CONDITIONAL_JUMP` [`00bffff4`](#insn-00bffff4) → [`00c00050`](#insn-00c00050)
  - `FALL_THROUGH` [`00bffff4`](#insn-00bffff4) → [`00bffff8`](#insn-00bffff8)
- ブロック [`00bffff8`](#insn-00bffff8) 範囲 `[['00bffff8', '00c00003']]`
  - `CONDITIONAL_JUMP` [`00c00000`](#insn-00c00000) → [`00c0000c`](#insn-00c0000c)
  - `FALL_THROUGH` [`00c00000`](#insn-00c00000) → [`00c00004`](#insn-00c00004)
- ブロック [`00c00004`](#insn-00c00004) 範囲 `[['00c00004', '00c0000b']]`
  - `UNCONDITIONAL_JUMP` [`00c00008`](#insn-00c00008) → [`00c00020`](#insn-00c00020)
- ブロック [`00c0000c`](#insn-00c0000c) 範囲 `[['00c0000c', '00c0001f']]`
  - `FALL_THROUGH` [`00c0001c`](#insn-00c0001c) → [`00c00020`](#insn-00c00020)
- ブロック [`00c00020`](#insn-00c00020) 範囲 `[['00c00020', '00c00037']]`
  - `CONDITIONAL_JUMP` [`00c00034`](#insn-00c00034) → [`00c0009c`](#insn-00c0009c)
  - `FALL_THROUGH` [`00c00034`](#insn-00c00034) → [`00c00038`](#insn-00c00038)
- ブロック [`00c00038`](#insn-00c00038) 範囲 `[['00c00038', '00c00043']]`
  - `CONDITIONAL_JUMP` [`00c00040`](#insn-00c00040) → [`00bfffb0`](#insn-00bfffb0)
  - `FALL_THROUGH` [`00c00040`](#insn-00c00040) → [`00c00044`](#insn-00c00044)
- ブロック [`00c00044`](#insn-00c00044) 範囲 `[['00c00044', '00c0004f']]`
  - `CONDITIONAL_JUMP` [`00c0004c`](#insn-00c0004c) → [`00bfffc4`](#insn-00bfffc4)
  - `FALL_THROUGH` [`00c0004c`](#insn-00c0004c) → [`00c00050`](#insn-00c00050)
- ブロック [`00c00050`](#insn-00c00050) 範囲 `[['00c00050', '00c00053']]`
  - `FALL_THROUGH` [`00c00050`](#insn-00c00050) → [`00c00054`](#insn-00c00054)
- ブロック [`00c00054`](#insn-00c00054) 範囲 `[['00c00054', '00c0006b']]`
  - `FALL_THROUGH` [`00c00068`](#insn-00c00068) → [`00c0006c`](#insn-00c0006c)
- ブロック [`00c0006c`](#insn-00c0006c) 範囲 `[['00c0006c', '00c0009b']]`
- ブロック [`00c0009c`](#insn-00c0009c) 範囲 `[['00c0009c', '00c000a7']]`
  - `CONDITIONAL_JUMP` [`00c000a4`](#insn-00c000a4) → [`00c000b0`](#insn-00c000b0)
  - `FALL_THROUGH` [`00c000a4`](#insn-00c000a4) → [`00c000a8`](#insn-00c000a8)
- ブロック [`00c000a8`](#insn-00c000a8) 範囲 `[['00c000a8', '00c000af']]`
  - `UNCONDITIONAL_JUMP` [`00c000ac`](#insn-00c000ac) → [`00c000c0`](#insn-00c000c0)
- ブロック [`00c000b0`](#insn-00c000b0) 範囲 `[['00c000b0', '00c000bf']]`
  - `FALL_THROUGH` [`00c000bc`](#insn-00c000bc) → [`00c000c0`](#insn-00c000c0)
- ブロック [`00c000c0`](#insn-00c000c0) 範囲 `[['00c000c0', '00c000cb']]`
  - `CONDITIONAL_JUMP` [`00c000c8`](#insn-00c000c8) → [`00c0006c`](#insn-00c0006c)
  - `FALL_THROUGH` [`00c000c8`](#insn-00c000c8) → [`00c000cc`](#insn-00c000cc)
- ブロック [`00c000cc`](#insn-00c000cc) 範囲 `[['00c000cc', '00c000cf']]`
  - `UNCONDITIONAL_JUMP` [`00c000cc`](#insn-00c000cc) → [`00c00054`](#insn-00c00054)

## 命令位置別の参照

- [`00bffefc`](#insn-00bffefc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfff00`](#insn-00bfff00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfff04`](#insn-00bfff04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfff24`](#insn-00bfff24) → [`00bfff44`](#insn-00bfff44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfff2c`](#insn-00bfff2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfff30`](#insn-00bfff30) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfff34`](#insn-00bfff34) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfff40`](#insn-00bfff40) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfff4c`](#insn-00bfff4c) → [`00bfff60`](#insn-00bfff60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfff54`](#insn-00bfff54) → [`00c5dff0`](../00c5d/00c5dff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dff0` · 推定シンボル `None` · 推定型 `None`
- [`00bfff60`](#insn-00bfff60) → [`00c0006c`](#insn-00c0006c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfff70`](#insn-00bfff70) → [`00c0006c`](#insn-00c0006c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfff78`](#insn-00bfff78) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bfff84`](#insn-00bfff84) → `00c9b740`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfff84`](#insn-00bfff84) → `01127a08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIwE2idE` · 推定型 `undefined8`
- [`00bfff88`](#insn-00bfff88) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bfff94`](#insn-00bfff94) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfffa8`](#insn-00bfffa8) → [`00bfffc4`](#insn-00bfffc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffac`](#insn-00bfffac) → [`00c00050`](#insn-00c00050) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffc0`](#insn-00bfffc0) → [`00c00050`](#insn-00c00050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffcc`](#insn-00bfffcc) → [`00bfffe0`](#insn-00bfffe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffd8`](#insn-00bfffd8) → [`00bffff8`](#insn-00bffff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffdc`](#insn-00bfffdc) → [`00c00050`](#insn-00c00050) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffff4`](#insn-00bffff4) → [`00c00050`](#insn-00c00050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00000`](#insn-00c00000) → [`00c0000c`](#insn-00c0000c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00008`](#insn-00c00008) → [`00c00020`](#insn-00c00020) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00034`](#insn-00c00034) → [`00c0009c`](#insn-00c0009c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00040`](#insn-00c00040) → [`00bfffb0`](#insn-00bfffb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0004c`](#insn-00c0004c) → [`00bfffc4`](#insn-00bfffc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00064`](#insn-00c00064) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00c00084`](#insn-00c00084) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c00088`](#insn-00c00088) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0008c`](#insn-00c0008c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c000a4`](#insn-00c000a4) → [`00c000b0`](#insn-00c000b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c000ac`](#insn-00c000ac) → [`00c000c0`](#insn-00c000c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c000c8`](#insn-00c000c8) → [`00c0006c`](#insn-00c0006c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c000cc`](#insn-00c000cc) → [`00c00054`](#insn-00c00054) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffefc`](#insn-00bffefc)

~~~json
{
  "source": "00bffefc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfff00`](#insn-00bfff00)

~~~json
{
  "source": "00bfff00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfff04`](#insn-00bfff04)

~~~json
{
  "source": "00bfff04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfff24`](#insn-00bfff24)

~~~json
{
  "source": "00bfff24",
  "target": "00bfff44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfff2c`](#insn-00bfff2c)

~~~json
{
  "source": "00bfff2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfff30`](#insn-00bfff30)

~~~json
{
  "source": "00bfff30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfff34`](#insn-00bfff34)

~~~json
{
  "source": "00bfff34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfff40`](#insn-00bfff40)

~~~json
{
  "source": "00bfff40",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfff4c`](#insn-00bfff4c)

~~~json
{
  "source": "00bfff4c",
  "target": "00bfff60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfff54`](#insn-00bfff54)

~~~json
{
  "source": "00bfff54",
  "target": "00c5dff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfff60`](#insn-00bfff60)

~~~json
{
  "source": "00bfff60",
  "target": "00c0006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfff70`](#insn-00bfff70)

~~~json
{
  "source": "00bfff70",
  "target": "00c0006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfff78`](#insn-00bfff78)

~~~json
{
  "source": "00bfff78",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfff84`](#insn-00bfff84)

~~~json
{
  "source": "00bfff84",
  "target": "00c9b740",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b740",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfff84`](#insn-00bfff84)

~~~json
{
  "source": "00bfff84",
  "target": "01127a08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfff88`](#insn-00bfff88)

~~~json
{
  "source": "00bfff88",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfff94`](#insn-00bfff94)

~~~json
{
  "source": "00bfff94",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfffa8`](#insn-00bfffa8)

~~~json
{
  "source": "00bfffa8",
  "target": "00bfffc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffac`](#insn-00bfffac)

~~~json
{
  "source": "00bfffac",
  "target": "00c00050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffc0`](#insn-00bfffc0)

~~~json
{
  "source": "00bfffc0",
  "target": "00c00050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffcc`](#insn-00bfffcc)

~~~json
{
  "source": "00bfffcc",
  "target": "00bfffe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffd8`](#insn-00bfffd8)

~~~json
{
  "source": "00bfffd8",
  "target": "00bffff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffdc`](#insn-00bfffdc)

~~~json
{
  "source": "00bfffdc",
  "target": "00c00050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffff4`](#insn-00bffff4)

~~~json
{
  "source": "00bffff4",
  "target": "00c00050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00000`](#insn-00c00000)

~~~json
{
  "source": "00c00000",
  "target": "00c0000c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00008`](#insn-00c00008)

~~~json
{
  "source": "00c00008",
  "target": "00c00020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00034`](#insn-00c00034)

~~~json
{
  "source": "00c00034",
  "target": "00c0009c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00040`](#insn-00c00040)

~~~json
{
  "source": "00c00040",
  "target": "00bfffb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0004c`](#insn-00c0004c)

~~~json
{
  "source": "00c0004c",
  "target": "00bfffc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00064`](#insn-00c00064)

~~~json
{
  "source": "00c00064",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c00084`](#insn-00c00084)

~~~json
{
  "source": "00c00084",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c00088`](#insn-00c00088)

~~~json
{
  "source": "00c00088",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0008c`](#insn-00c0008c)

~~~json
{
  "source": "00c0008c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c000a4`](#insn-00c000a4)

~~~json
{
  "source": "00c000a4",
  "target": "00c000b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c000ac`](#insn-00c000ac)

~~~json
{
  "source": "00c000ac",
  "target": "00c000c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c000c8`](#insn-00c000c8)

~~~json
{
  "source": "00c000c8",
  "target": "00c0006c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c000cc`](#insn-00c000cc)

~~~json
{
  "source": "00c000cc",
  "target": "00c00054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
