# 00bab6cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b41388`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b41/00b41388.md) · 移動量 `+0x6a344`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0063.md#compare-cebc5a664874fb3d574cd91986c66442)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00babaf4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bab/00babaf4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-c5fddd7c5db75ba7cc0341e0c56af64f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bab6cc",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEs",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fe5207afacb334e1c653378fc6879cb0a2c4adb6bb4126955b832c82dde9df62",
  "source_text_sha256": "fe5207afacb334e1c653378fc6879cb0a2c4adb6bb4126955b832c82dde9df62",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bab6cc",
        "00bab89f"
      ]
    ],
    "bytes_sha256": "090e2f7c89562af1b4ec1b300549980c46da36af6382943db7baba8c25fa864f",
    "instruction_count": 117,
    "instruction_bytes": 468,
    "body_bytes": 468,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5c750](../00c5c/00c5c750.md)

## 呼び出し先

- [00c57ae0](../00c57/00c57ae0.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ea0](../00c57/00c57ea0.md)
- [00c58af0](../00c58/00c58af0.md)
- [00c5ccf0](../00c5c/00c5ccf0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5689 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEs(long *param_1,ushort param_2)

{
  uint uVar1;
  long lVar2;
  uint uVar3;
  int iVar4;
  long *plVar5;
  long *plVar6;
  ulong uVar7;
  long lVar8;
  undefined8 uVar9;
  undefined1 auStack_60 [8];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar8 = *(long *)(*param_1 + -0x18);
  if (*(int *)((long)param_1 + lVar8 + 0x20) == 0) {
    if (*(long *)((long)param_1 + lVar8 + 0x88) != 0) {
      _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv();
      lVar8 = *(long *)(*param_1 + -0x18);
    }
    uVar1 = *(uint *)((long)param_1 + lVar8 + 8) & 0x4a;
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_60);
    plVar5 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_60,
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b438
                               );
                    /* try { // try from 00bab754 to 00cab75f has its CatchHandler @ 00babffc */
    _ZNSt6__ndk16localeD1Ev(auStack_60);
                    /* catch() { ... } // from try @ 00bab390 with catch @ 00bab760
                       try { // try from 00bab760 to 00cac06b has its CatchHandler @ 00ba9230 */
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00bab380 with catch @ 00bab764 */
    uVar3 = *(uint *)(lVar8 + 0x90);
                    /* catch() { ... } // from try @ 00baaff8 with catch @ 00bab768 */
    uVar9 = *(undefined8 *)(lVar8 + 0x28);
                    /* catch() { ... } // from try @ 00baafe8 with catch @ 00bab76c */
                    /* catch() { ... } // from try @ 00bab684 with catch @ 00bab770 */
    if (uVar3 == 0xffffffff) {
                    /* catch() { ... } // from try @ 00bab65c with catch @ 00bab774 */
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_60,lVar8);
                    /* catch() { ... } // from try @ 00bab630 with catch @ 00bab784 */
                    /* catch() { ... } // from try @ 00bab2e0 with catch @ 00bab788 */
                    /* catch() { ... } // from try @ 00bab2c4 with catch @ 00bab78c */
      plVar6 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_60,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9a830);
                    /* catch() { ... } // from try @ 00bab298 with catch @ 00bab79c */
      uVar3 = (**(code **)(*plVar6 + 0x38))(plVar6,0x20);
                    /* catch() { ... } // from try @ 00bab60c with catch @ 00bab7a0 */
      _ZNSt6__ndk16localeD1Ev(auStack_60);
      uVar3 = uVar3 & 0xff;
                    /* catch() { ... } // from try @ 00bab5e0 with catch @ 00bab7b0 */
      *(uint *)(lVar8 + 0x90) = uVar3;
    }
                    /* catch() { ... } // from try @ 00bab5bc with catch @ 00bab7b4 */
                    /* catch() { ... } // from try @ 00bab274 with catch @ 00bab7c4 */
    uVar7 = (ulong)param_2;
    if (uVar1 != 8 && uVar1 != 0x40) {
      uVar7 = (long)(short)param_2;
    }
                    /* catch() { ... } // from try @ 00bab248 with catch @ 00bab7d4 */
                    /* catch() { ... } // from try @ 00bab224 with catch @ 00bab7d8 */
    lVar8 = (**(code **)(*plVar5 + 0x20))(plVar5,uVar9,lVar8,uVar3,uVar7);
    if (lVar8 == 0) {
                    /* catch() { ... } // from try @ 00bab590 with catch @ 00bab7e8 */
                    /* catch() { ... } // from try @ 00bab56c with catch @ 00bab7ec */
      lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00bab540 with catch @ 00bab7fc */
                    /* catch() { ... } // from try @ 00bab1f8 with catch @ 00bab800 */
      _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 5);
    }
  }
                    /* catch() { ... } // from try @ 00bab1d4 with catch @ 00bab804 */
  lVar8 = *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00bab1a8 with catch @ 00bab814 */
                    /* catch() { ... } // from try @ 00bab520 with catch @ 00bab818 */
                    /* catch() { ... } // from try @ 00bab4f4 with catch @ 00bab828 */
                    /* catch() { ... } // from try @ 00bab4d0 with catch @ 00bab82c */
                    /* catch() { ... } // from try @ 00bab188 with catch @ 00bab83c */
                    /* catch() { ... } // from try @ 00bab15c with catch @ 00bab84c */
                    /* catch() { ... } // from try @ 00bab138 with catch @ 00bab850 */
  if ((((*(long *)((long)param_1 + lVar8 + 0x28) != 0) &&
       (*(int *)((long)param_1 + lVar8 + 0x20) == 0)) &&
      ((*(byte *)((long)param_1 + lVar8 + 9) >> 5 & 1) != 0)) &&
     ((uVar7 = _ZSt18uncaught_exceptionv(), (uVar7 & 1) == 0 &&
      (iVar4 = (**(code **)(**(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28) + 0x30))
                         (), iVar4 == -1)))) {
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00bab4a4 with catch @ 00bab860 */
                    /* catch() { ... } // from try @ 00bab484 with catch @ 00bab864 */
    _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 1);
  }
                    /* catch() { ... } // from try @ 00bab10c with catch @ 00bab874 */
                    /* catch() { ... } // from try @ 00bab0ec with catch @ 00bab878 */
  if (*(long *)(lVar2 + 0x28) == local_58) {
                    /* catch() { ... } // from try @ 00bab464 with catch @ 00bab888 */
    return param_1;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bab6cc"></a> `00bab6cc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bab6d0"></a> `00bab6d0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab6d4"></a> `00bab6d4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab6d8"></a> `00bab6d8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab6dc"></a> `00bab6dc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab6e0"></a> `00bab6e0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bab6e4"></a> `00bab6e4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bab6e8"></a> `00bab6e8` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bab6ec"></a> `00bab6ec` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bab6f0"></a> `00bab6f0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bab6f4"></a> `00bab6f4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab6f8"></a> `00bab6f8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bab6fc"></a> `00bab6fc` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bab700"></a> `00bab700` | `09 00 08 8b` | add x9,x0,x8 | `FALL_THROUGH`
<a id="insn-00bab704"></a> `00bab704` | `2a 21 40 b9` | ldr w10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bab708"></a> `00bab708` | `ea 07 00 35` | cbnz w10,0x00bab804 | `CONDITIONAL_JUMP`
<a id="insn-00bab70c"></a> `00bab70c` | `20 45 40 f9` | ldr x0,[x9, #0x88] | `FALL_THROUGH`
<a id="insn-00bab710"></a> `00bab710` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00bab714"></a> `00bab714` | `80 00 00 b4` | cbz x0,0x00bab724 | `CONDITIONAL_JUMP`
<a id="insn-00bab718"></a> `00bab718` | `f6 b4 02 94` | bl 0x00c58af0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab71c"></a> `00bab71c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bab720"></a> `00bab720` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bab724"></a> `00bab724` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bab728"></a> `00bab728` | `08 08 40 b9` | ldr w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bab72c"></a> `00bab72c` | `49 09 80 52` | mov w9,#0x4a | `FALL_THROUGH`
<a id="insn-00bab730"></a> `00bab730` | `1a 01 09 0a` | and w26,w8,w9 | `FALL_THROUGH`
<a id="insn-00bab734"></a> `00bab734` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bab738"></a> `00bab738` | `ce b1 02 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bab73c"></a> `00bab73c` | `81 07 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bab740"></a> `00bab740` | `21 1c 42 f9` | ldr x1,[x1, #0x438] | `FALL_THROUGH`
<a id="insn-00bab744"></a> `00bab744` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bab748"></a> `00bab748` | `ce b1 02 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bab74c"></a> `00bab74c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bab750"></a> `00bab750` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bab754"></a> `00bab754` | `cf b1 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bab758"></a> `00bab758` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bab75c"></a> `00bab75c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bab760"></a> `00bab760` | `76 02 08 8b` | add x22,x19,x8 | `FALL_THROUGH`
<a id="insn-00bab764"></a> `00bab764` | `c3 92 40 b9` | ldr w3,[x22, #0x90] | `FALL_THROUGH`
<a id="insn-00bab768"></a> `00bab768` | `d7 16 40 f9` | ldr x23,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bab76c"></a> `00bab76c` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bab770"></a> `00bab770` | `21 02 00 54` | b.ne 0x00bab7b4 | `CONDITIONAL_JUMP`
<a id="insn-00bab774"></a> `00bab774` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bab778"></a> `00bab778` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bab77c"></a> `00bab77c` | `bd b1 02 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bab780"></a> `00bab780` | `61 07 00 f0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00bab784"></a> `00bab784` | `21 18 44 f9` | ldr x1,[x1, #0x830] | `FALL_THROUGH`
<a id="insn-00bab788"></a> `00bab788` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bab78c"></a> `00bab78c` | `bd b1 02 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bab790"></a> `00bab790` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bab794"></a> `00bab794` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bab798"></a> `00bab798` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bab79c"></a> `00bab79c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bab7a0"></a> `00bab7a0` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00bab7a4"></a> `00bab7a4` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bab7a8"></a> `00bab7a8` | `ba b1 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bab7ac"></a> `00bab7ac` | `03 1f 00 12` | and w3,w24,#0xff | `FALL_THROUGH`
<a id="insn-00bab7b0"></a> `00bab7b0` | `c3 92 00 b9` | str w3,[x22, #0x90] | `FALL_THROUGH`
<a id="insn-00bab7b4"></a> `00bab7b4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bab7b8"></a> `00bab7b8` | `5f 23 00 71` | cmp w26,#0x8 | `FALL_THROUGH`
<a id="insn-00bab7bc"></a> `00bab7bc` | `09 08 80 52` | mov w9,#0x40 | `FALL_THROUGH`
<a id="insn-00bab7c0"></a> `00bab7c0` | `44 13 49 7a` | ccmp w26,w9,#0x4,ne | `FALL_THROUGH`
<a id="insn-00bab7c4"></a> `00bab7c4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bab7c8"></a> `00bab7c8` | `89 3e 40 92` | and x9,x20,#0xffff | `FALL_THROUGH`
<a id="insn-00bab7cc"></a> `00bab7cc` | `8a 3e 40 93` | sxth x10,w20 | `FALL_THROUGH`
<a id="insn-00bab7d0"></a> `00bab7d0` | `24 01 8a 9a` | csel x4,x9,x10,eq | `FALL_THROUGH`
<a id="insn-00bab7d4"></a> `00bab7d4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bab7d8"></a> `00bab7d8` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bab7dc"></a> `00bab7dc` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bab7e0"></a> `00bab7e0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bab7e4"></a> `00bab7e4` | `00 01 00 b5` | cbnz x0,0x00bab804 | `CONDITIONAL_JUMP`
<a id="insn-00bab7e8"></a> `00bab7e8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bab7ec"></a> `00bab7ec` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bab7f0"></a> `00bab7f0` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bab7f4"></a> `00bab7f4` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bab7f8"></a> `00bab7f8` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bab7fc"></a> `00bab7fc` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00bab800"></a> `00bab800` | `a8 b1 02 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab804"></a> `00bab804` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bab808"></a> `00bab808` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bab80c"></a> `00bab80c` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00bab810"></a> `00bab810` | `09 15 40 f9` | ldr x9,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bab814"></a> `00bab814` | `c9 02 00 b4` | cbz x9,0x00bab86c | `CONDITIONAL_JUMP`
<a id="insn-00bab818"></a> `00bab818` | `09 21 40 b9` | ldr w9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bab81c"></a> `00bab81c` | `89 02 00 35` | cbnz w9,0x00bab86c | `CONDITIONAL_JUMP`
<a id="insn-00bab820"></a> `00bab820` | `08 25 40 39` | ldrb w8,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00bab824"></a> `00bab824` | `48 02 28 36` | tbz w8,#0x5,0x00bab86c | `CONDITIONAL_JUMP`
<a id="insn-00bab828"></a> `00bab828` | `32 c5 02 94` | bl 0x00c5ccf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab82c"></a> `00bab82c` | `00 02 00 37` | tbnz w0,#0x0,0x00bab86c | `CONDITIONAL_JUMP`
<a id="insn-00bab830"></a> `00bab830` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bab834"></a> `00bab834` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bab838"></a> `00bab838` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00bab83c"></a> `00bab83c` | `00 15 40 f9` | ldr x0,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bab840"></a> `00bab840` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bab844"></a> `00bab844` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00bab848"></a> `00bab848` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bab84c"></a> `00bab84c` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bab850"></a> `00bab850` | `e1 00 00 54` | b.ne 0x00bab86c | `CONDITIONAL_JUMP`
<a id="insn-00bab854"></a> `00bab854` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bab858"></a> `00bab858` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bab85c"></a> `00bab85c` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bab860"></a> `00bab860` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bab864"></a> `00bab864` | `01 01 00 32` | orr w1,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bab868"></a> `00bab868` | `8e b1 02 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bab86c"></a> `00bab86c` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bab870"></a> `00bab870` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bab874"></a> `00bab874` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bab878"></a> `00bab878` | `21 01 00 54` | b.ne 0x00bab89c | `CONDITIONAL_JUMP`
<a id="insn-00bab87c"></a> `00bab87c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bab880"></a> `00bab880` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bab884"></a> `00bab884` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bab888"></a> `00bab888` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bab88c"></a> `00bab88c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bab890"></a> `00bab890` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bab894"></a> `00bab894` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bab898"></a> `00bab898` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bab89c"></a> `00bab89c` | `91 b0 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bab6cc`](#insn-00bab6cc) 範囲 `[['00bab6cc', '00bab70b']]`
  - `CONDITIONAL_JUMP` [`00bab708`](#insn-00bab708) → [`00bab804`](#insn-00bab804)
  - `FALL_THROUGH` [`00bab708`](#insn-00bab708) → [`00bab70c`](#insn-00bab70c)
- ブロック [`00bab70c`](#insn-00bab70c) 範囲 `[['00bab70c', '00bab717']]`
  - `CONDITIONAL_JUMP` [`00bab714`](#insn-00bab714) → [`00bab724`](#insn-00bab724)
  - `FALL_THROUGH` [`00bab714`](#insn-00bab714) → [`00bab718`](#insn-00bab718)
- ブロック [`00bab718`](#insn-00bab718) 範囲 `[['00bab718', '00bab723']]`
  - `FALL_THROUGH` [`00bab720`](#insn-00bab720) → [`00bab724`](#insn-00bab724)
- ブロック [`00bab724`](#insn-00bab724) 範囲 `[['00bab724', '00bab753']]`
  - `FALL_THROUGH` [`00bab750`](#insn-00bab750) → [`00bab754`](#insn-00bab754)
- ブロック [`00bab754`](#insn-00bab754) 範囲 `[['00bab754', '00bab75f']]`
  - `FALL_THROUGH` [`00bab75c`](#insn-00bab75c) → [`00bab760`](#insn-00bab760)
- ブロック [`00bab760`](#insn-00bab760) 範囲 `[['00bab760', '00bab763']]`
  - `FALL_THROUGH` [`00bab760`](#insn-00bab760) → [`00bab764`](#insn-00bab764)
- ブロック [`00bab764`](#insn-00bab764) 範囲 `[['00bab764', '00bab767']]`
  - `FALL_THROUGH` [`00bab764`](#insn-00bab764) → [`00bab768`](#insn-00bab768)
- ブロック [`00bab768`](#insn-00bab768) 範囲 `[['00bab768', '00bab76b']]`
  - `FALL_THROUGH` [`00bab768`](#insn-00bab768) → [`00bab76c`](#insn-00bab76c)
- ブロック [`00bab76c`](#insn-00bab76c) 範囲 `[['00bab76c', '00bab76f']]`
  - `FALL_THROUGH` [`00bab76c`](#insn-00bab76c) → [`00bab770`](#insn-00bab770)
- ブロック [`00bab770`](#insn-00bab770) 範囲 `[['00bab770', '00bab773']]`
  - `CONDITIONAL_JUMP` [`00bab770`](#insn-00bab770) → [`00bab7b4`](#insn-00bab7b4)
  - `FALL_THROUGH` [`00bab770`](#insn-00bab770) → [`00bab774`](#insn-00bab774)
- ブロック [`00bab774`](#insn-00bab774) 範囲 `[['00bab774', '00bab783']]`
  - `FALL_THROUGH` [`00bab780`](#insn-00bab780) → [`00bab784`](#insn-00bab784)
- ブロック [`00bab784`](#insn-00bab784) 範囲 `[['00bab784', '00bab787']]`
  - `FALL_THROUGH` [`00bab784`](#insn-00bab784) → [`00bab788`](#insn-00bab788)
- ブロック [`00bab788`](#insn-00bab788) 範囲 `[['00bab788', '00bab78b']]`
  - `FALL_THROUGH` [`00bab788`](#insn-00bab788) → [`00bab78c`](#insn-00bab78c)
- ブロック [`00bab78c`](#insn-00bab78c) 範囲 `[['00bab78c', '00bab79b']]`
  - `FALL_THROUGH` [`00bab798`](#insn-00bab798) → [`00bab79c`](#insn-00bab79c)
- ブロック [`00bab79c`](#insn-00bab79c) 範囲 `[['00bab79c', '00bab79f']]`
  - `FALL_THROUGH` [`00bab79c`](#insn-00bab79c) → [`00bab7a0`](#insn-00bab7a0)
- ブロック [`00bab7a0`](#insn-00bab7a0) 範囲 `[['00bab7a0', '00bab7af']]`
  - `FALL_THROUGH` [`00bab7ac`](#insn-00bab7ac) → [`00bab7b0`](#insn-00bab7b0)
- ブロック [`00bab7b0`](#insn-00bab7b0) 範囲 `[['00bab7b0', '00bab7b3']]`
  - `FALL_THROUGH` [`00bab7b0`](#insn-00bab7b0) → [`00bab7b4`](#insn-00bab7b4)
- ブロック [`00bab7b4`](#insn-00bab7b4) 範囲 `[['00bab7b4', '00bab7c3']]`
  - `FALL_THROUGH` [`00bab7c0`](#insn-00bab7c0) → [`00bab7c4`](#insn-00bab7c4)
- ブロック [`00bab7c4`](#insn-00bab7c4) 範囲 `[['00bab7c4', '00bab7d3']]`
  - `FALL_THROUGH` [`00bab7d0`](#insn-00bab7d0) → [`00bab7d4`](#insn-00bab7d4)
- ブロック [`00bab7d4`](#insn-00bab7d4) 範囲 `[['00bab7d4', '00bab7d7']]`
  - `FALL_THROUGH` [`00bab7d4`](#insn-00bab7d4) → [`00bab7d8`](#insn-00bab7d8)
- ブロック [`00bab7d8`](#insn-00bab7d8) 範囲 `[['00bab7d8', '00bab7e7']]`
  - `CONDITIONAL_JUMP` [`00bab7e4`](#insn-00bab7e4) → [`00bab804`](#insn-00bab804)
  - `FALL_THROUGH` [`00bab7e4`](#insn-00bab7e4) → [`00bab7e8`](#insn-00bab7e8)
- ブロック [`00bab7e8`](#insn-00bab7e8) 範囲 `[['00bab7e8', '00bab7eb']]`
  - `FALL_THROUGH` [`00bab7e8`](#insn-00bab7e8) → [`00bab7ec`](#insn-00bab7ec)
- ブロック [`00bab7ec`](#insn-00bab7ec) 範囲 `[['00bab7ec', '00bab7fb']]`
  - `FALL_THROUGH` [`00bab7f8`](#insn-00bab7f8) → [`00bab7fc`](#insn-00bab7fc)
- ブロック [`00bab7fc`](#insn-00bab7fc) 範囲 `[['00bab7fc', '00bab7ff']]`
  - `FALL_THROUGH` [`00bab7fc`](#insn-00bab7fc) → [`00bab800`](#insn-00bab800)
- ブロック [`00bab800`](#insn-00bab800) 範囲 `[['00bab800', '00bab803']]`
  - `FALL_THROUGH` [`00bab800`](#insn-00bab800) → [`00bab804`](#insn-00bab804)
- ブロック [`00bab804`](#insn-00bab804) 範囲 `[['00bab804', '00bab813']]`
  - `FALL_THROUGH` [`00bab810`](#insn-00bab810) → [`00bab814`](#insn-00bab814)
- ブロック [`00bab814`](#insn-00bab814) 範囲 `[['00bab814', '00bab817']]`
  - `CONDITIONAL_JUMP` [`00bab814`](#insn-00bab814) → [`00bab86c`](#insn-00bab86c)
  - `FALL_THROUGH` [`00bab814`](#insn-00bab814) → [`00bab818`](#insn-00bab818)
- ブロック [`00bab818`](#insn-00bab818) 範囲 `[['00bab818', '00bab81f']]`
  - `CONDITIONAL_JUMP` [`00bab81c`](#insn-00bab81c) → [`00bab86c`](#insn-00bab86c)
  - `FALL_THROUGH` [`00bab81c`](#insn-00bab81c) → [`00bab820`](#insn-00bab820)
- ブロック [`00bab820`](#insn-00bab820) 範囲 `[['00bab820', '00bab827']]`
  - `CONDITIONAL_JUMP` [`00bab824`](#insn-00bab824) → [`00bab86c`](#insn-00bab86c)
  - `FALL_THROUGH` [`00bab824`](#insn-00bab824) → [`00bab828`](#insn-00bab828)
- ブロック [`00bab828`](#insn-00bab828) 範囲 `[['00bab828', '00bab82b']]`
  - `FALL_THROUGH` [`00bab828`](#insn-00bab828) → [`00bab82c`](#insn-00bab82c)
- ブロック [`00bab82c`](#insn-00bab82c) 範囲 `[['00bab82c', '00bab82f']]`
  - `CONDITIONAL_JUMP` [`00bab82c`](#insn-00bab82c) → [`00bab86c`](#insn-00bab86c)
  - `FALL_THROUGH` [`00bab82c`](#insn-00bab82c) → [`00bab830`](#insn-00bab830)
- ブロック [`00bab830`](#insn-00bab830) 範囲 `[['00bab830', '00bab83b']]`
  - `FALL_THROUGH` [`00bab838`](#insn-00bab838) → [`00bab83c`](#insn-00bab83c)
- ブロック [`00bab83c`](#insn-00bab83c) 範囲 `[['00bab83c', '00bab84b']]`
  - `FALL_THROUGH` [`00bab848`](#insn-00bab848) → [`00bab84c`](#insn-00bab84c)
- ブロック [`00bab84c`](#insn-00bab84c) 範囲 `[['00bab84c', '00bab84f']]`
  - `FALL_THROUGH` [`00bab84c`](#insn-00bab84c) → [`00bab850`](#insn-00bab850)
- ブロック [`00bab850`](#insn-00bab850) 範囲 `[['00bab850', '00bab853']]`
  - `CONDITIONAL_JUMP` [`00bab850`](#insn-00bab850) → [`00bab86c`](#insn-00bab86c)
  - `FALL_THROUGH` [`00bab850`](#insn-00bab850) → [`00bab854`](#insn-00bab854)
- ブロック [`00bab854`](#insn-00bab854) 範囲 `[['00bab854', '00bab85f']]`
  - `FALL_THROUGH` [`00bab85c`](#insn-00bab85c) → [`00bab860`](#insn-00bab860)
- ブロック [`00bab860`](#insn-00bab860) 範囲 `[['00bab860', '00bab863']]`
  - `FALL_THROUGH` [`00bab860`](#insn-00bab860) → [`00bab864`](#insn-00bab864)
- ブロック [`00bab864`](#insn-00bab864) 範囲 `[['00bab864', '00bab86b']]`
  - `FALL_THROUGH` [`00bab868`](#insn-00bab868) → [`00bab86c`](#insn-00bab86c)
- ブロック [`00bab86c`](#insn-00bab86c) 範囲 `[['00bab86c', '00bab873']]`
  - `FALL_THROUGH` [`00bab870`](#insn-00bab870) → [`00bab874`](#insn-00bab874)
- ブロック [`00bab874`](#insn-00bab874) 範囲 `[['00bab874', '00bab877']]`
  - `FALL_THROUGH` [`00bab874`](#insn-00bab874) → [`00bab878`](#insn-00bab878)
- ブロック [`00bab878`](#insn-00bab878) 範囲 `[['00bab878', '00bab87b']]`
  - `CONDITIONAL_JUMP` [`00bab878`](#insn-00bab878) → [`00bab89c`](#insn-00bab89c)
  - `FALL_THROUGH` [`00bab878`](#insn-00bab878) → [`00bab87c`](#insn-00bab87c)
- ブロック [`00bab87c`](#insn-00bab87c) 範囲 `[['00bab87c', '00bab887']]`
  - `FALL_THROUGH` [`00bab884`](#insn-00bab884) → [`00bab888`](#insn-00bab888)
- ブロック [`00bab888`](#insn-00bab888) 範囲 `[['00bab888', '00bab89b']]`
- ブロック [`00bab89c`](#insn-00bab89c) 範囲 `[['00bab89c', '00bab89f']]`

## 命令位置別の参照

- [`00bab6d0`](#insn-00bab6d0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6d4`](#insn-00bab6d4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6d8`](#insn-00bab6d8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6dc`](#insn-00bab6dc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6e0`](#insn-00bab6e0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab6f4`](#insn-00bab6f4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab708`](#insn-00bab708) → [`00bab804`](#insn-00bab804) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab714`](#insn-00bab714) → [`00bab724`](#insn-00bab724) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab718`](#insn-00bab718) → [`00c58af0`](../00c58/00c58af0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58af0` · 推定シンボル `None` · 推定型 `None`
- [`00bab738`](#insn-00bab738) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bab740`](#insn-00bab740) → `00c9b438`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab740`](#insn-00bab740) → `01127798`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bab748`](#insn-00bab748) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bab754`](#insn-00bab754) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bab770`](#insn-00bab770) → [`00bab7b4`](#insn-00bab7b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab77c`](#insn-00bab77c) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bab784`](#insn-00bab784) → `00c9a830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bab784`](#insn-00bab784) → `01127a18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bab78c`](#insn-00bab78c) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bab7a8`](#insn-00bab7a8) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bab7e4`](#insn-00bab7e4) → [`00bab804`](#insn-00bab804) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab800`](#insn-00bab800) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bab814`](#insn-00bab814) → [`00bab86c`](#insn-00bab86c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab81c`](#insn-00bab81c) → [`00bab86c`](#insn-00bab86c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab824`](#insn-00bab824) → [`00bab86c`](#insn-00bab86c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab828`](#insn-00bab828) → [`00c5ccf0`](../00c5c/00c5ccf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ccf0` · 推定シンボル `None` · 推定型 `None`
- [`00bab82c`](#insn-00bab82c) → [`00bab86c`](#insn-00bab86c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab850`](#insn-00bab850) → [`00bab86c`](#insn-00bab86c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab868`](#insn-00bab868) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bab870`](#insn-00bab870) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab878`](#insn-00bab878) → [`00bab89c`](#insn-00bab89c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab880`](#insn-00bab880) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab884`](#insn-00bab884) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab888`](#insn-00bab888) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab88c`](#insn-00bab88c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab890`](#insn-00bab890) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bab89c`](#insn-00bab89c) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bab6d0`](#insn-00bab6d0)

~~~json
{
  "source": "00bab6d0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6d4`](#insn-00bab6d4)

~~~json
{
  "source": "00bab6d4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6d8`](#insn-00bab6d8)

~~~json
{
  "source": "00bab6d8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6dc`](#insn-00bab6dc)

~~~json
{
  "source": "00bab6dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6e0`](#insn-00bab6e0)

~~~json
{
  "source": "00bab6e0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab6f4`](#insn-00bab6f4)

~~~json
{
  "source": "00bab6f4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab708`](#insn-00bab708)

~~~json
{
  "source": "00bab708",
  "target": "00bab804",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab714`](#insn-00bab714)

~~~json
{
  "source": "00bab714",
  "target": "00bab724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab718`](#insn-00bab718)

~~~json
{
  "source": "00bab718",
  "target": "00c58af0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab738`](#insn-00bab738)

~~~json
{
  "source": "00bab738",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab740`](#insn-00bab740)

~~~json
{
  "source": "00bab740",
  "target": "00c9b438",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b438",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab740`](#insn-00bab740)

~~~json
{
  "source": "00bab740",
  "target": "01127798",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127798",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab748`](#insn-00bab748)

~~~json
{
  "source": "00bab748",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab754`](#insn-00bab754)

~~~json
{
  "source": "00bab754",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab770`](#insn-00bab770)

~~~json
{
  "source": "00bab770",
  "target": "00bab7b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab77c`](#insn-00bab77c)

~~~json
{
  "source": "00bab77c",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab784`](#insn-00bab784)

~~~json
{
  "source": "00bab784",
  "target": "00c9a830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bab784`](#insn-00bab784)

~~~json
{
  "source": "00bab784",
  "target": "01127a18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bab78c`](#insn-00bab78c)

~~~json
{
  "source": "00bab78c",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab7a8`](#insn-00bab7a8)

~~~json
{
  "source": "00bab7a8",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab7e4`](#insn-00bab7e4)

~~~json
{
  "source": "00bab7e4",
  "target": "00bab804",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab800`](#insn-00bab800)

~~~json
{
  "source": "00bab800",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab814`](#insn-00bab814)

~~~json
{
  "source": "00bab814",
  "target": "00bab86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab81c`](#insn-00bab81c)

~~~json
{
  "source": "00bab81c",
  "target": "00bab86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab824`](#insn-00bab824)

~~~json
{
  "source": "00bab824",
  "target": "00bab86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab828`](#insn-00bab828)

~~~json
{
  "source": "00bab828",
  "target": "00c5ccf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab82c`](#insn-00bab82c)

~~~json
{
  "source": "00bab82c",
  "target": "00bab86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab850`](#insn-00bab850)

~~~json
{
  "source": "00bab850",
  "target": "00bab86c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab868`](#insn-00bab868)

~~~json
{
  "source": "00bab868",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bab870`](#insn-00bab870)

~~~json
{
  "source": "00bab870",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab878`](#insn-00bab878)

~~~json
{
  "source": "00bab878",
  "target": "00bab89c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab880`](#insn-00bab880)

~~~json
{
  "source": "00bab880",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab884`](#insn-00bab884)

~~~json
{
  "source": "00bab884",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab888`](#insn-00bab888)

~~~json
{
  "source": "00bab888",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab88c`](#insn-00bab88c)

~~~json
{
  "source": "00bab88c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab890`](#insn-00bab890)

~~~json
{
  "source": "00bab890",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bab89c`](#insn-00bab89c)

~~~json
{
  "source": "00bab89c",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
