# 00babcc8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bab8a0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bab/00bab8a0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-7c9f340efe7242bb80cd97f24e22f523)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00babd64`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00babd64.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-bae1723dabf4c45e326dfe9f284b670c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babcc8",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEt",
  "size": 436,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e1e7d791faaa9151d6b36ad9a68f5a528b109f34c903cd5d1db52f34531ae5a6",
  "source_text_sha256": "e1e7d791faaa9151d6b36ad9a68f5a528b109f34c903cd5d1db52f34531ae5a6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babcc8",
        "00babe7b"
      ]
    ],
    "bytes_sha256": "685879f6b98cfce3c005c32638b268c6b1896e2c26554dfee9126b9c6a649148",
    "instruction_count": 109,
    "instruction_bytes": 436,
    "body_bytes": 436,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5cb60](../00c5c/00c5cb60.md)

## 呼び出し先

- [00c57ee0](../00c57/00c57ee0.md)
- [00c58270](../00c58/00c58270.md)
- [00c58280](../00c58/00c58280.md)
- [00c58290](../00c58/00c58290.md)
- [00c582a0](../00c58/00c582a0.md)
- [00c58ef0](../00c58/00c58ef0.md)
- [00c5d0f0](../00c5d/00c5d0f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5172 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEt(long *param_1,undefined2 param_2)

{
  long lVar1;
  uint uVar2;
  int iVar3;
  long *plVar4;
  long *plVar5;
  ulong uVar6;
  long lVar7;
  undefined8 uVar8;
  undefined1 auStack_60 [8];
  long local_58;
  
                    /* catch() { ... } // from try @ 00ba9f9c with catch @ 00babccc */
                    /* catch() { ... } // from try @ 00baaf6c with catch @ 00babcdc */
                    /* catch() { ... } // from try @ 00baaf4c with catch @ 00babce0 */
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
                    /* catch() { ... } // from try @ 00baac64 with catch @ 00babcf0 */
                    /* catch() { ... } // from try @ 00baac44 with catch @ 00babcf4 */
  lVar7 = *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00baa288 with catch @ 00babd04 */
  if (*(int *)((long)param_1 + lVar7 + 0x20) == 0) {
                    /* catch() { ... } // from try @ 00baa268 with catch @ 00babd08 */
    if (*(long *)((long)param_1 + lVar7 + 0x88) != 0) {
      _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv();
                    /* catch() { ... } // from try @ 00ba9f70 with catch @ 00babd18 */
                    /* catch() { ... } // from try @ 00ba9f50 with catch @ 00babd1c */
      lVar7 = *(long *)(*param_1 + -0x18);
    }
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_60,(long)param_1 + lVar7);
                    /* catch() { ... } // from try @ 00baaf2c with catch @ 00babd2c */
    plVar4 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_60,
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b838
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_60);
                    /* catch() { ... } // from try @ 00baaf18 with catch @ 00babd4c */
                    /* catch() { ... } // from try @ 00baac24 with catch @ 00babd50 */
    lVar7 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar2 = *(uint *)(lVar7 + 0x90);
    uVar8 = *(undefined8 *)(lVar7 + 0x28);
    if (uVar2 == 0xffffffff) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_60,lVar7);
                    /* catch() { ... } // from try @ 00baac10 with catch @ 00babd70 */
                    /* catch() { ... } // from try @ 00baa248 with catch @ 00babd74 */
      plVar5 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_60,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ac30);
      uVar2 = (**(code **)(*plVar5 + 0x38))(plVar5,0x20);
                    /* catch() { ... } // from try @ 00baa234 with catch @ 00babd94 */
                    /* catch() { ... } // from try @ 00ba9f30 with catch @ 00babd98 */
      _ZNSt6__ndk16localeD1Ev(auStack_60);
      uVar2 = uVar2 & 0xff;
      *(uint *)(lVar7 + 0x90) = uVar2;
    }
                    /* catch() { ... } // from try @ 00ba9f1c with catch @ 00babdb8 */
                    /* catch() { ... } // from try @ 00baaef4 with catch @ 00babdbc */
    lVar7 = (**(code **)(*plVar4 + 0x30))(plVar4,uVar8,lVar7,uVar2,param_2);
                    /* catch() { ... } // from try @ 00baabec with catch @ 00babdc0 */
    if (lVar7 == 0) {
                    /* catch() { ... } // from try @ 00baab4c with catch @ 00babdc4 */
                    /* catch() { ... } // from try @ 00baaac4 with catch @ 00babdc8 */
                    /* catch() { ... } // from try @ 00baa210 with catch @ 00babdd0 */
      lVar7 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00ba9ef8 with catch @ 00babdd4 */
                    /* catch() { ... } // from try @ 00bab88c with catch @ 00babdd8 */
                    /* catch() { ... } // from try @ 00bab4e8 with catch @ 00babddc */
      _ZNSt6__ndk18ios_base5clearEj(lVar7,*(uint *)(lVar7 + 0x20) | 5);
    }
  }
  lVar7 = *(long *)(*param_1 + -0x18);
  if ((((*(long *)((long)param_1 + lVar7 + 0x28) != 0) &&
       (*(int *)((long)param_1 + lVar7 + 0x20) == 0)) &&
      ((*(byte *)((long)param_1 + lVar7 + 9) >> 5 & 1) != 0)) &&
     ((uVar6 = _ZSt18uncaught_exceptionv(), (uVar6 & 1) == 0 &&
      (iVar3 = (**(code **)(**(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28) + 0x30))
                         (), iVar3 == -1)))) {
    lVar7 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00bab5e0 with catch @ 00babe44 */
    _ZNSt6__ndk18ios_base5clearEj(lVar7,*(uint *)(lVar7 + 0x20) | 1);
  }
                    /* catch() { ... } // from try @ 00bab248 with catch @ 00babe48 */
  if (*(long *)(lVar1 + 0x28) == local_58) {
                    /* catch() { ... } // from try @ 00bab150 with catch @ 00babe5c */
                    /* catch() { ... } // from try @ 00baae44 with catch @ 00babe60 */
                    /* catch() { ... } // from try @ 00baa464 with catch @ 00babe64 */
                    /* catch() { ... } // from try @ 00baa14c with catch @ 00babe68 */
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
<a id="insn-00babcc8"></a> `00babcc8` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00babccc"></a> `00babccc` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babcd0"></a> `00babcd0` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babcd4"></a> `00babcd4` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babcd8"></a> `00babcd8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00babcdc"></a> `00babcdc` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00babce0"></a> `00babce0` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00babce4"></a> `00babce4` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00babce8"></a> `00babce8` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00babcec"></a> `00babcec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00babcf0"></a> `00babcf0` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00babcf4"></a> `00babcf4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00babcf8"></a> `00babcf8` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babcfc"></a> `00babcfc` | `09 00 08 8b` | add x9,x0,x8 | `FALL_THROUGH`
<a id="insn-00babd00"></a> `00babd00` | `2a 21 40 b9` | ldr w10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00babd04"></a> `00babd04` | `ea 06 00 35` | cbnz w10,0x00babde0 | `CONDITIONAL_JUMP`
<a id="insn-00babd08"></a> `00babd08` | `20 45 40 f9` | ldr x0,[x9, #0x88] | `FALL_THROUGH`
<a id="insn-00babd0c"></a> `00babd0c` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00babd10"></a> `00babd10` | `80 00 00 b4` | cbz x0,0x00babd20 | `CONDITIONAL_JUMP`
<a id="insn-00babd14"></a> `00babd14` | `77 b4 02 94` | bl 0x00c58ef0 | `UNCONDITIONAL_CALL`
<a id="insn-00babd18"></a> `00babd18` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babd1c"></a> `00babd1c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babd20"></a> `00babd20` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00babd24"></a> `00babd24` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00babd28"></a> `00babd28` | `52 b1 02 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00babd2c"></a> `00babd2c` | `81 07 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00babd30"></a> `00babd30` | `21 1c 44 f9` | ldr x1,[x1, #0x838] | `FALL_THROUGH`
<a id="insn-00babd34"></a> `00babd34` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00babd38"></a> `00babd38` | `52 b1 02 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00babd3c"></a> `00babd3c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00babd40"></a> `00babd40` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00babd44"></a> `00babd44` | `53 b1 02 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00babd48"></a> `00babd48` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babd4c"></a> `00babd4c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babd50"></a> `00babd50` | `76 02 08 8b` | add x22,x19,x8 | `FALL_THROUGH`
<a id="insn-00babd54"></a> `00babd54` | `c3 92 40 b9` | ldr w3,[x22, #0x90] | `FALL_THROUGH`
<a id="insn-00babd58"></a> `00babd58` | `d7 16 40 f9` | ldr x23,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00babd5c"></a> `00babd5c` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00babd60"></a> `00babd60` | `21 02 00 54` | b.ne 0x00babda4 | `CONDITIONAL_JUMP`
<a id="insn-00babd64"></a> `00babd64` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00babd68"></a> `00babd68` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00babd6c"></a> `00babd6c` | `41 b1 02 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00babd70"></a> `00babd70` | `61 07 00 f0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00babd74"></a> `00babd74` | `21 18 46 f9` | ldr x1,[x1, #0xc30] | `FALL_THROUGH`
<a id="insn-00babd78"></a> `00babd78` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00babd7c"></a> `00babd7c` | `41 b1 02 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00babd80"></a> `00babd80` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00babd84"></a> `00babd84` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00babd88"></a> `00babd88` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00babd8c"></a> `00babd8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00babd90"></a> `00babd90` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00babd94"></a> `00babd94` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00babd98"></a> `00babd98` | `3e b1 02 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00babd9c"></a> `00babd9c` | `03 1f 00 12` | and w3,w24,#0xff | `FALL_THROUGH`
<a id="insn-00babda0"></a> `00babda0` | `c3 92 00 b9` | str w3,[x22, #0x90] | `FALL_THROUGH`
<a id="insn-00babda4"></a> `00babda4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00babda8"></a> `00babda8` | `84 3e 40 92` | and x4,x20,#0xffff | `FALL_THROUGH`
<a id="insn-00babdac"></a> `00babdac` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00babdb0"></a> `00babdb0` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00babdb4"></a> `00babdb4` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00babdb8"></a> `00babdb8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00babdbc"></a> `00babdbc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00babdc0"></a> `00babdc0` | `00 01 00 b5` | cbnz x0,0x00babde0 | `CONDITIONAL_JUMP`
<a id="insn-00babdc4"></a> `00babdc4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babdc8"></a> `00babdc8` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00babdcc"></a> `00babdcc` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babdd0"></a> `00babdd0` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00babdd4"></a> `00babdd4` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00babdd8"></a> `00babdd8` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00babddc"></a> `00babddc` | `31 b1 02 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00babde0"></a> `00babde0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babde4"></a> `00babde4` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babde8"></a> `00babde8` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00babdec"></a> `00babdec` | `09 15 40 f9` | ldr x9,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00babdf0"></a> `00babdf0` | `c9 02 00 b4` | cbz x9,0x00babe48 | `CONDITIONAL_JUMP`
<a id="insn-00babdf4"></a> `00babdf4` | `09 21 40 b9` | ldr w9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00babdf8"></a> `00babdf8` | `89 02 00 35` | cbnz w9,0x00babe48 | `CONDITIONAL_JUMP`
<a id="insn-00babdfc"></a> `00babdfc` | `08 25 40 39` | ldrb w8,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00babe00"></a> `00babe00` | `48 02 28 36` | tbz w8,#0x5,0x00babe48 | `CONDITIONAL_JUMP`
<a id="insn-00babe04"></a> `00babe04` | `bb c4 02 94` | bl 0x00c5d0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00babe08"></a> `00babe08` | `00 02 00 37` | tbnz w0,#0x0,0x00babe48 | `CONDITIONAL_JUMP`
<a id="insn-00babe0c"></a> `00babe0c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babe10"></a> `00babe10` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babe14"></a> `00babe14` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00babe18"></a> `00babe18` | `00 15 40 f9` | ldr x0,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00babe1c"></a> `00babe1c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00babe20"></a> `00babe20` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00babe24"></a> `00babe24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00babe28"></a> `00babe28` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00babe2c"></a> `00babe2c` | `e1 00 00 54` | b.ne 0x00babe48 | `CONDITIONAL_JUMP`
<a id="insn-00babe30"></a> `00babe30` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babe34"></a> `00babe34` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babe38"></a> `00babe38` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00babe3c"></a> `00babe3c` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00babe40"></a> `00babe40` | `01 01 00 32` | orr w1,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00babe44"></a> `00babe44` | `17 b1 02 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00babe48"></a> `00babe48` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00babe4c"></a> `00babe4c` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00babe50"></a> `00babe50` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00babe54"></a> `00babe54` | `21 01 00 54` | b.ne 0x00babe78 | `CONDITIONAL_JUMP`
<a id="insn-00babe58"></a> `00babe58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00babe5c"></a> `00babe5c` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00babe60"></a> `00babe60` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00babe64"></a> `00babe64` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babe68"></a> `00babe68` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babe6c"></a> `00babe6c` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babe70"></a> `00babe70` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00babe74"></a> `00babe74` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00babe78"></a> `00babe78` | `1a b0 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babcc8`](#insn-00babcc8) 範囲 `[['00babcc8', '00babccb']]`
  - `FALL_THROUGH` [`00babcc8`](#insn-00babcc8) → [`00babccc`](#insn-00babccc)
- ブロック [`00babccc`](#insn-00babccc) 範囲 `[['00babccc', '00babcdb']]`
  - `FALL_THROUGH` [`00babcd8`](#insn-00babcd8) → [`00babcdc`](#insn-00babcdc)
- ブロック [`00babcdc`](#insn-00babcdc) 範囲 `[['00babcdc', '00babcdf']]`
  - `FALL_THROUGH` [`00babcdc`](#insn-00babcdc) → [`00babce0`](#insn-00babce0)
- ブロック [`00babce0`](#insn-00babce0) 範囲 `[['00babce0', '00babcef']]`
  - `FALL_THROUGH` [`00babcec`](#insn-00babcec) → [`00babcf0`](#insn-00babcf0)
- ブロック [`00babcf0`](#insn-00babcf0) 範囲 `[['00babcf0', '00babcf3']]`
  - `FALL_THROUGH` [`00babcf0`](#insn-00babcf0) → [`00babcf4`](#insn-00babcf4)
- ブロック [`00babcf4`](#insn-00babcf4) 範囲 `[['00babcf4', '00babd03']]`
  - `FALL_THROUGH` [`00babd00`](#insn-00babd00) → [`00babd04`](#insn-00babd04)
- ブロック [`00babd04`](#insn-00babd04) 範囲 `[['00babd04', '00babd07']]`
  - `CONDITIONAL_JUMP` [`00babd04`](#insn-00babd04) → [`00babde0`](#insn-00babde0)
  - `FALL_THROUGH` [`00babd04`](#insn-00babd04) → [`00babd08`](#insn-00babd08)
- ブロック [`00babd08`](#insn-00babd08) 範囲 `[['00babd08', '00babd13']]`
  - `CONDITIONAL_JUMP` [`00babd10`](#insn-00babd10) → [`00babd20`](#insn-00babd20)
  - `FALL_THROUGH` [`00babd10`](#insn-00babd10) → [`00babd14`](#insn-00babd14)
- ブロック [`00babd14`](#insn-00babd14) 範囲 `[['00babd14', '00babd17']]`
  - `FALL_THROUGH` [`00babd14`](#insn-00babd14) → [`00babd18`](#insn-00babd18)
- ブロック [`00babd18`](#insn-00babd18) 範囲 `[['00babd18', '00babd1b']]`
  - `FALL_THROUGH` [`00babd18`](#insn-00babd18) → [`00babd1c`](#insn-00babd1c)
- ブロック [`00babd1c`](#insn-00babd1c) 範囲 `[['00babd1c', '00babd1f']]`
  - `FALL_THROUGH` [`00babd1c`](#insn-00babd1c) → [`00babd20`](#insn-00babd20)
- ブロック [`00babd20`](#insn-00babd20) 範囲 `[['00babd20', '00babd2b']]`
  - `FALL_THROUGH` [`00babd28`](#insn-00babd28) → [`00babd2c`](#insn-00babd2c)
- ブロック [`00babd2c`](#insn-00babd2c) 範囲 `[['00babd2c', '00babd4b']]`
  - `FALL_THROUGH` [`00babd48`](#insn-00babd48) → [`00babd4c`](#insn-00babd4c)
- ブロック [`00babd4c`](#insn-00babd4c) 範囲 `[['00babd4c', '00babd4f']]`
  - `FALL_THROUGH` [`00babd4c`](#insn-00babd4c) → [`00babd50`](#insn-00babd50)
- ブロック [`00babd50`](#insn-00babd50) 範囲 `[['00babd50', '00babd63']]`
  - `CONDITIONAL_JUMP` [`00babd60`](#insn-00babd60) → [`00babda4`](#insn-00babda4)
  - `FALL_THROUGH` [`00babd60`](#insn-00babd60) → [`00babd64`](#insn-00babd64)
- ブロック [`00babd64`](#insn-00babd64) 範囲 `[['00babd64', '00babd6f']]`
  - `FALL_THROUGH` [`00babd6c`](#insn-00babd6c) → [`00babd70`](#insn-00babd70)
- ブロック [`00babd70`](#insn-00babd70) 範囲 `[['00babd70', '00babd73']]`
  - `FALL_THROUGH` [`00babd70`](#insn-00babd70) → [`00babd74`](#insn-00babd74)
- ブロック [`00babd74`](#insn-00babd74) 範囲 `[['00babd74', '00babd93']]`
  - `FALL_THROUGH` [`00babd90`](#insn-00babd90) → [`00babd94`](#insn-00babd94)
- ブロック [`00babd94`](#insn-00babd94) 範囲 `[['00babd94', '00babd97']]`
  - `FALL_THROUGH` [`00babd94`](#insn-00babd94) → [`00babd98`](#insn-00babd98)
- ブロック [`00babd98`](#insn-00babd98) 範囲 `[['00babd98', '00babda3']]`
  - `FALL_THROUGH` [`00babda0`](#insn-00babda0) → [`00babda4`](#insn-00babda4)
- ブロック [`00babda4`](#insn-00babda4) 範囲 `[['00babda4', '00babdb7']]`
  - `FALL_THROUGH` [`00babdb4`](#insn-00babdb4) → [`00babdb8`](#insn-00babdb8)
- ブロック [`00babdb8`](#insn-00babdb8) 範囲 `[['00babdb8', '00babdbb']]`
  - `FALL_THROUGH` [`00babdb8`](#insn-00babdb8) → [`00babdbc`](#insn-00babdbc)
- ブロック [`00babdbc`](#insn-00babdbc) 範囲 `[['00babdbc', '00babdbf']]`
  - `FALL_THROUGH` [`00babdbc`](#insn-00babdbc) → [`00babdc0`](#insn-00babdc0)
- ブロック [`00babdc0`](#insn-00babdc0) 範囲 `[['00babdc0', '00babdc3']]`
  - `CONDITIONAL_JUMP` [`00babdc0`](#insn-00babdc0) → [`00babde0`](#insn-00babde0)
  - `FALL_THROUGH` [`00babdc0`](#insn-00babdc0) → [`00babdc4`](#insn-00babdc4)
- ブロック [`00babdc4`](#insn-00babdc4) 範囲 `[['00babdc4', '00babdc7']]`
  - `FALL_THROUGH` [`00babdc4`](#insn-00babdc4) → [`00babdc8`](#insn-00babdc8)
- ブロック [`00babdc8`](#insn-00babdc8) 範囲 `[['00babdc8', '00babdcf']]`
  - `FALL_THROUGH` [`00babdcc`](#insn-00babdcc) → [`00babdd0`](#insn-00babdd0)
- ブロック [`00babdd0`](#insn-00babdd0) 範囲 `[['00babdd0', '00babdd3']]`
  - `FALL_THROUGH` [`00babdd0`](#insn-00babdd0) → [`00babdd4`](#insn-00babdd4)
- ブロック [`00babdd4`](#insn-00babdd4) 範囲 `[['00babdd4', '00babdd7']]`
  - `FALL_THROUGH` [`00babdd4`](#insn-00babdd4) → [`00babdd8`](#insn-00babdd8)
- ブロック [`00babdd8`](#insn-00babdd8) 範囲 `[['00babdd8', '00babddb']]`
  - `FALL_THROUGH` [`00babdd8`](#insn-00babdd8) → [`00babddc`](#insn-00babddc)
- ブロック [`00babddc`](#insn-00babddc) 範囲 `[['00babddc', '00babddf']]`
  - `FALL_THROUGH` [`00babddc`](#insn-00babddc) → [`00babde0`](#insn-00babde0)
- ブロック [`00babde0`](#insn-00babde0) 範囲 `[['00babde0', '00babdf3']]`
  - `CONDITIONAL_JUMP` [`00babdf0`](#insn-00babdf0) → [`00babe48`](#insn-00babe48)
  - `FALL_THROUGH` [`00babdf0`](#insn-00babdf0) → [`00babdf4`](#insn-00babdf4)
- ブロック [`00babdf4`](#insn-00babdf4) 範囲 `[['00babdf4', '00babdfb']]`
  - `CONDITIONAL_JUMP` [`00babdf8`](#insn-00babdf8) → [`00babe48`](#insn-00babe48)
  - `FALL_THROUGH` [`00babdf8`](#insn-00babdf8) → [`00babdfc`](#insn-00babdfc)
- ブロック [`00babdfc`](#insn-00babdfc) 範囲 `[['00babdfc', '00babe03']]`
  - `CONDITIONAL_JUMP` [`00babe00`](#insn-00babe00) → [`00babe48`](#insn-00babe48)
  - `FALL_THROUGH` [`00babe00`](#insn-00babe00) → [`00babe04`](#insn-00babe04)
- ブロック [`00babe04`](#insn-00babe04) 範囲 `[['00babe04', '00babe0b']]`
  - `CONDITIONAL_JUMP` [`00babe08`](#insn-00babe08) → [`00babe48`](#insn-00babe48)
  - `FALL_THROUGH` [`00babe08`](#insn-00babe08) → [`00babe0c`](#insn-00babe0c)
- ブロック [`00babe0c`](#insn-00babe0c) 範囲 `[['00babe0c', '00babe2f']]`
  - `CONDITIONAL_JUMP` [`00babe2c`](#insn-00babe2c) → [`00babe48`](#insn-00babe48)
  - `FALL_THROUGH` [`00babe2c`](#insn-00babe2c) → [`00babe30`](#insn-00babe30)
- ブロック [`00babe30`](#insn-00babe30) 範囲 `[['00babe30', '00babe43']]`
  - `FALL_THROUGH` [`00babe40`](#insn-00babe40) → [`00babe44`](#insn-00babe44)
- ブロック [`00babe44`](#insn-00babe44) 範囲 `[['00babe44', '00babe47']]`
  - `FALL_THROUGH` [`00babe44`](#insn-00babe44) → [`00babe48`](#insn-00babe48)
- ブロック [`00babe48`](#insn-00babe48) 範囲 `[['00babe48', '00babe57']]`
  - `CONDITIONAL_JUMP` [`00babe54`](#insn-00babe54) → [`00babe78`](#insn-00babe78)
  - `FALL_THROUGH` [`00babe54`](#insn-00babe54) → [`00babe58`](#insn-00babe58)
- ブロック [`00babe58`](#insn-00babe58) 範囲 `[['00babe58', '00babe5b']]`
  - `FALL_THROUGH` [`00babe58`](#insn-00babe58) → [`00babe5c`](#insn-00babe5c)
- ブロック [`00babe5c`](#insn-00babe5c) 範囲 `[['00babe5c', '00babe5f']]`
  - `FALL_THROUGH` [`00babe5c`](#insn-00babe5c) → [`00babe60`](#insn-00babe60)
- ブロック [`00babe60`](#insn-00babe60) 範囲 `[['00babe60', '00babe63']]`
  - `FALL_THROUGH` [`00babe60`](#insn-00babe60) → [`00babe64`](#insn-00babe64)
- ブロック [`00babe64`](#insn-00babe64) 範囲 `[['00babe64', '00babe67']]`
  - `FALL_THROUGH` [`00babe64`](#insn-00babe64) → [`00babe68`](#insn-00babe68)
- ブロック [`00babe68`](#insn-00babe68) 範囲 `[['00babe68', '00babe77']]`
- ブロック [`00babe78`](#insn-00babe78) 範囲 `[['00babe78', '00babe7b']]`

## 命令位置別の参照

- [`00babccc`](#insn-00babccc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babcd0`](#insn-00babcd0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babcd4`](#insn-00babcd4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babcd8`](#insn-00babcd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babcdc`](#insn-00babcdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babcf0`](#insn-00babcf0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd04`](#insn-00babd04) → [`00babde0`](#insn-00babde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd10`](#insn-00babd10) → [`00babd20`](#insn-00babd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd14`](#insn-00babd14) → [`00c58ef0`](../00c58/00c58ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ef0` · 推定シンボル `None` · 推定型 `None`
- [`00babd28`](#insn-00babd28) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00babd30`](#insn-00babd30) → `00c9b838`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00babd30`](#insn-00babd30) → `01127b98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00babd38`](#insn-00babd38) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00babd44`](#insn-00babd44) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00babd60`](#insn-00babd60) → [`00babda4`](#insn-00babda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babd6c`](#insn-00babd6c) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00babd74`](#insn-00babd74) → `00c9ac30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00babd74`](#insn-00babd74) → `01127e18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00babd7c`](#insn-00babd7c) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00babd98`](#insn-00babd98) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00babdc0`](#insn-00babdc0) → [`00babde0`](#insn-00babde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babddc`](#insn-00babddc) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00babdf0`](#insn-00babdf0) → [`00babe48`](#insn-00babe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babdf8`](#insn-00babdf8) → [`00babe48`](#insn-00babe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe00`](#insn-00babe00) → [`00babe48`](#insn-00babe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe04`](#insn-00babe04) → [`00c5d0f0`](../00c5d/00c5d0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d0f0` · 推定シンボル `None` · 推定型 `None`
- [`00babe08`](#insn-00babe08) → [`00babe48`](#insn-00babe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe2c`](#insn-00babe2c) → [`00babe48`](#insn-00babe48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe44`](#insn-00babe44) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00babe4c`](#insn-00babe4c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe54`](#insn-00babe54) → [`00babe78`](#insn-00babe78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe5c`](#insn-00babe5c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe60`](#insn-00babe60) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe64`](#insn-00babe64) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe68`](#insn-00babe68) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe6c`](#insn-00babe6c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babe78`](#insn-00babe78) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babccc`](#insn-00babccc)

~~~json
{
  "source": "00babccc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babcd0`](#insn-00babcd0)

~~~json
{
  "source": "00babcd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babcd4`](#insn-00babcd4)

~~~json
{
  "source": "00babcd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babcd8`](#insn-00babcd8)

~~~json
{
  "source": "00babcd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babcdc`](#insn-00babcdc)

~~~json
{
  "source": "00babcdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babcf0`](#insn-00babcf0)

~~~json
{
  "source": "00babcf0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd04`](#insn-00babd04)

~~~json
{
  "source": "00babd04",
  "target": "00babde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd10`](#insn-00babd10)

~~~json
{
  "source": "00babd10",
  "target": "00babd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd14`](#insn-00babd14)

~~~json
{
  "source": "00babd14",
  "target": "00c58ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babd28`](#insn-00babd28)

~~~json
{
  "source": "00babd28",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babd30`](#insn-00babd30)

~~~json
{
  "source": "00babd30",
  "target": "00c9b838",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b838",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00babd30`](#insn-00babd30)

~~~json
{
  "source": "00babd30",
  "target": "01127b98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00babd38`](#insn-00babd38)

~~~json
{
  "source": "00babd38",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babd44`](#insn-00babd44)

~~~json
{
  "source": "00babd44",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babd60`](#insn-00babd60)

~~~json
{
  "source": "00babd60",
  "target": "00babda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babd6c`](#insn-00babd6c)

~~~json
{
  "source": "00babd6c",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babd74`](#insn-00babd74)

~~~json
{
  "source": "00babd74",
  "target": "00c9ac30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac30",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00babd74`](#insn-00babd74)

~~~json
{
  "source": "00babd74",
  "target": "01127e18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00babd7c`](#insn-00babd7c)

~~~json
{
  "source": "00babd7c",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babd98`](#insn-00babd98)

~~~json
{
  "source": "00babd98",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babdc0`](#insn-00babdc0)

~~~json
{
  "source": "00babdc0",
  "target": "00babde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babddc`](#insn-00babddc)

~~~json
{
  "source": "00babddc",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babdf0`](#insn-00babdf0)

~~~json
{
  "source": "00babdf0",
  "target": "00babe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babdf8`](#insn-00babdf8)

~~~json
{
  "source": "00babdf8",
  "target": "00babe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe00`](#insn-00babe00)

~~~json
{
  "source": "00babe00",
  "target": "00babe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe04`](#insn-00babe04)

~~~json
{
  "source": "00babe04",
  "target": "00c5d0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babe08`](#insn-00babe08)

~~~json
{
  "source": "00babe08",
  "target": "00babe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe2c`](#insn-00babe2c)

~~~json
{
  "source": "00babe2c",
  "target": "00babe48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe44`](#insn-00babe44)

~~~json
{
  "source": "00babe44",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babe4c`](#insn-00babe4c)

~~~json
{
  "source": "00babe4c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe54`](#insn-00babe54)

~~~json
{
  "source": "00babe54",
  "target": "00babe78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe5c`](#insn-00babe5c)

~~~json
{
  "source": "00babe5c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe60`](#insn-00babe60)

~~~json
{
  "source": "00babe60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe64`](#insn-00babe64)

~~~json
{
  "source": "00babe64",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe68`](#insn-00babe68)

~~~json
{
  "source": "00babe68",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe6c`](#insn-00babe6c)

~~~json
{
  "source": "00babe6c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babe78`](#insn-00babe78)

~~~json
{
  "source": "00babe78",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
