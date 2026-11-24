# 00babaf4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bab6cc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bab/00bab6cc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-c5fddd7c5db75ba7cc0341e0c56af64f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00babb90`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bab/00babb90.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-2b98396616a723260d5d507d7ce7f780)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00babaf4",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEs",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b05840f61492bac19e648aede583f55db4b354bb06cd82bf8de47846ed193008",
  "source_text_sha256": "b05840f61492bac19e648aede583f55db4b354bb06cd82bf8de47846ed193008",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00babaf4",
        "00babcc7"
      ]
    ],
    "bytes_sha256": "976fefc904b4e857840483bfca0bb57164035173e19010cee1bd67d70939e8b2",
    "instruction_count": 117,
    "instruction_bytes": 468,
    "body_bytes": 468,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5cb50](../00c5c/00c5cb50.md)

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

## 疑似コード / UTF-8 6716 bytes

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
  
                    /* catch() { ... } // from try @ 00bab144 with catch @ 00babafc */
                    /* catch() { ... } // from try @ 00bab124 with catch @ 00babb00 */
                    /* catch() { ... } // from try @ 00baae38 with catch @ 00babb10 */
  lVar2 = tpidr_el0;
                    /* catch() { ... } // from try @ 00baae1c with catch @ 00babb14 */
  local_58 = *(long *)(lVar2 + 0x28);
                    /* catch() { ... } // from try @ 00baa458 with catch @ 00babb24 */
  lVar8 = *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00baa438 with catch @ 00babb28 */
  if (*(int *)((long)param_1 + lVar8 + 0x20) == 0) {
                    /* catch() { ... } // from try @ 00baa140 with catch @ 00babb38 */
                    /* catch() { ... } // from try @ 00baa120 with catch @ 00babb3c */
    if (*(long *)((long)param_1 + lVar8 + 0x88) != 0) {
      _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5flushEv();
      lVar8 = *(long *)(*param_1 + -0x18);
    }
                    /* catch() { ... } // from try @ 00bab0f8 with catch @ 00babb4c */
                    /* catch() { ... } // from try @ 00bab0d4 with catch @ 00babb50 */
    uVar1 = *(uint *)((long)param_1 + lVar8 + 8) & 0x4a;
                    /* catch() { ... } // from try @ 00baadf0 with catch @ 00babb60 */
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_60);
                    /* catch() { ... } // from try @ 00baadcc with catch @ 00babb64 */
    plVar5 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_60,
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b838
                               );
                    /* catch() { ... } // from try @ 00baa40c with catch @ 00babb74 */
                    /* catch() { ... } // from try @ 00baa3e8 with catch @ 00babb78 */
    _ZNSt6__ndk16localeD1Ev(auStack_60);
                    /* catch() { ... } // from try @ 00baa0f4 with catch @ 00babb88 */
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00baa0d0 with catch @ 00babb8c */
    uVar3 = *(uint *)(lVar8 + 0x90);
    uVar9 = *(undefined8 *)(lVar8 + 0x28);
    if (uVar3 == 0xffffffff) {
                    /* catch() { ... } // from try @ 00bab0a8 with catch @ 00babb9c */
                    /* catch() { ... } // from try @ 00bab084 with catch @ 00babba0 */
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_60,lVar8);
                    /* catch() { ... } // from try @ 00baada0 with catch @ 00babbb0 */
                    /* catch() { ... } // from try @ 00baad7c with catch @ 00babbb4 */
      plVar6 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_60,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ac30);
                    /* catch() { ... } // from try @ 00baa3bc with catch @ 00babbc4 */
      uVar3 = (**(code **)(*plVar6 + 0x38))(plVar6,0x20);
                    /* catch() { ... } // from try @ 00baa3a0 with catch @ 00babbc8 */
      _ZNSt6__ndk16localeD1Ev(auStack_60);
      uVar3 = uVar3 & 0xff;
                    /* catch() { ... } // from try @ 00baa0a4 with catch @ 00babbd8 */
      *(uint *)(lVar8 + 0x90) = uVar3;
    }
                    /* catch() { ... } // from try @ 00baa088 with catch @ 00babbdc */
                    /* catch() { ... } // from try @ 00bab058 with catch @ 00babbec */
                    /* catch() { ... } // from try @ 00baad50 with catch @ 00babbf0 */
                    /* catch() { ... } // from try @ 00baa374 with catch @ 00babbf4 */
    uVar7 = (ulong)param_2;
                    /* catch() { ... } // from try @ 00baa05c with catch @ 00babbf8 */
    if (uVar1 != 8 && uVar1 != 0x40) {
      uVar7 = (long)(short)param_2;
    }
                    /* catch() { ... } // from try @ 00bab034 with catch @ 00babbfc */
    lVar8 = (**(code **)(*plVar5 + 0x20))(plVar5,uVar9,lVar8,uVar3,uVar7);
                    /* catch() { ... } // from try @ 00bab008 with catch @ 00babc0c */
    if (lVar8 == 0) {
                    /* catch() { ... } // from try @ 00baad2c with catch @ 00babc10 */
      lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00baad00 with catch @ 00babc20 */
                    /* catch() { ... } // from try @ 00baa350 with catch @ 00babc24 */
      _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 5);
    }
  }
  lVar8 = *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00baa324 with catch @ 00babc34 */
                    /* catch() { ... } // from try @ 00baa038 with catch @ 00babc38 */
                    /* catch() { ... } // from try @ 00baa00c with catch @ 00babc48 */
                    /* catch() { ... } // from try @ 00baafe8 with catch @ 00babc4c */
                    /* catch() { ... } // from try @ 00baafbc with catch @ 00babc5c */
                    /* catch() { ... } // from try @ 00baace0 with catch @ 00babc60 */
                    /* catch() { ... } // from try @ 00baacb4 with catch @ 00babc70 */
                    /* catch() { ... } // from try @ 00baa304 with catch @ 00babc74 */
  if ((((*(long *)((long)param_1 + lVar8 + 0x28) != 0) &&
       (*(int *)((long)param_1 + lVar8 + 0x20) == 0)) &&
      ((*(byte *)((long)param_1 + lVar8 + 9) >> 5 & 1) != 0)) &&
     ((uVar7 = _ZSt18uncaught_exceptionv(), (uVar7 & 1) == 0 &&
      (iVar4 = (**(code **)(**(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28) + 0x30))
                         (), iVar4 == -1)))) {
                    /* catch() { ... } // from try @ 00baa2d8 with catch @ 00babc84 */
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
                    /* catch() { ... } // from try @ 00ba9fec with catch @ 00babc88 */
    _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 1);
  }
                    /* catch() { ... } // from try @ 00ba9fc0 with catch @ 00babc98 */
                    /* catch() { ... } // from try @ 00baaf98 with catch @ 00babc9c */
  if (*(long *)(lVar2 + 0x28) == local_58) {
                    /* catch() { ... } // from try @ 00baac90 with catch @ 00babcac */
                    /* catch() { ... } // from try @ 00baa2b4 with catch @ 00babcbc */
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
<a id="insn-00babaf4"></a> `00babaf4` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00babaf8"></a> `00babaf8` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babafc"></a> `00babafc` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babb00"></a> `00babb00` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babb04"></a> `00babb04` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00babb08"></a> `00babb08` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00babb0c"></a> `00babb0c` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00babb10"></a> `00babb10` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00babb14"></a> `00babb14` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00babb18"></a> `00babb18` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00babb1c"></a> `00babb1c` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00babb20"></a> `00babb20` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00babb24"></a> `00babb24` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babb28"></a> `00babb28` | `09 00 08 8b` | add x9,x0,x8 | `FALL_THROUGH`
<a id="insn-00babb2c"></a> `00babb2c` | `2a 21 40 b9` | ldr w10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00babb30"></a> `00babb30` | `ea 07 00 35` | cbnz w10,0x00babc2c | `CONDITIONAL_JUMP`
<a id="insn-00babb34"></a> `00babb34` | `20 45 40 f9` | ldr x0,[x9, #0x88] | `FALL_THROUGH`
<a id="insn-00babb38"></a> `00babb38` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00babb3c"></a> `00babb3c` | `80 00 00 b4` | cbz x0,0x00babb4c | `CONDITIONAL_JUMP`
<a id="insn-00babb40"></a> `00babb40` | `ec b4 02 94` | bl 0x00c58ef0 | `UNCONDITIONAL_CALL`
<a id="insn-00babb44"></a> `00babb44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babb48"></a> `00babb48` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babb4c"></a> `00babb4c` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00babb50"></a> `00babb50` | `08 08 40 b9` | ldr w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00babb54"></a> `00babb54` | `49 09 80 52` | mov w9,#0x4a | `FALL_THROUGH`
<a id="insn-00babb58"></a> `00babb58` | `1a 01 09 0a` | and w26,w8,w9 | `FALL_THROUGH`
<a id="insn-00babb5c"></a> `00babb5c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00babb60"></a> `00babb60` | `c4 b1 02 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00babb64"></a> `00babb64` | `81 07 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00babb68"></a> `00babb68` | `21 1c 44 f9` | ldr x1,[x1, #0x838] | `FALL_THROUGH`
<a id="insn-00babb6c"></a> `00babb6c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00babb70"></a> `00babb70` | `c4 b1 02 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00babb74"></a> `00babb74` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00babb78"></a> `00babb78` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00babb7c"></a> `00babb7c` | `c5 b1 02 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00babb80"></a> `00babb80` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babb84"></a> `00babb84` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babb88"></a> `00babb88` | `76 02 08 8b` | add x22,x19,x8 | `FALL_THROUGH`
<a id="insn-00babb8c"></a> `00babb8c` | `c3 92 40 b9` | ldr w3,[x22, #0x90] | `FALL_THROUGH`
<a id="insn-00babb90"></a> `00babb90` | `d7 16 40 f9` | ldr x23,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00babb94"></a> `00babb94` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00babb98"></a> `00babb98` | `21 02 00 54` | b.ne 0x00babbdc | `CONDITIONAL_JUMP`
<a id="insn-00babb9c"></a> `00babb9c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00babba0"></a> `00babba0` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00babba4"></a> `00babba4` | `b3 b1 02 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00babba8"></a> `00babba8` | `61 07 00 f0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00babbac"></a> `00babbac` | `21 18 46 f9` | ldr x1,[x1, #0xc30] | `FALL_THROUGH`
<a id="insn-00babbb0"></a> `00babbb0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00babbb4"></a> `00babbb4` | `b3 b1 02 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00babbb8"></a> `00babbb8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00babbbc"></a> `00babbbc` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00babbc0"></a> `00babbc0` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00babbc4"></a> `00babbc4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00babbc8"></a> `00babbc8` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00babbcc"></a> `00babbcc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00babbd0"></a> `00babbd0` | `b0 b1 02 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00babbd4"></a> `00babbd4` | `03 1f 00 12` | and w3,w24,#0xff | `FALL_THROUGH`
<a id="insn-00babbd8"></a> `00babbd8` | `c3 92 00 b9` | str w3,[x22, #0x90] | `FALL_THROUGH`
<a id="insn-00babbdc"></a> `00babbdc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00babbe0"></a> `00babbe0` | `5f 23 00 71` | cmp w26,#0x8 | `FALL_THROUGH`
<a id="insn-00babbe4"></a> `00babbe4` | `09 08 80 52` | mov w9,#0x40 | `FALL_THROUGH`
<a id="insn-00babbe8"></a> `00babbe8` | `44 13 49 7a` | ccmp w26,w9,#0x4,ne | `FALL_THROUGH`
<a id="insn-00babbec"></a> `00babbec` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00babbf0"></a> `00babbf0` | `89 3e 40 92` | and x9,x20,#0xffff | `FALL_THROUGH`
<a id="insn-00babbf4"></a> `00babbf4` | `8a 3e 40 93` | sxth x10,w20 | `FALL_THROUGH`
<a id="insn-00babbf8"></a> `00babbf8` | `24 01 8a 9a` | csel x4,x9,x10,eq | `FALL_THROUGH`
<a id="insn-00babbfc"></a> `00babbfc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00babc00"></a> `00babc00` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00babc04"></a> `00babc04` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00babc08"></a> `00babc08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00babc0c"></a> `00babc0c` | `00 01 00 b5` | cbnz x0,0x00babc2c | `CONDITIONAL_JUMP`
<a id="insn-00babc10"></a> `00babc10` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babc14"></a> `00babc14` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00babc18"></a> `00babc18` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babc1c"></a> `00babc1c` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00babc20"></a> `00babc20` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00babc24"></a> `00babc24` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00babc28"></a> `00babc28` | `9e b1 02 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00babc2c"></a> `00babc2c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babc30"></a> `00babc30` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babc34"></a> `00babc34` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00babc38"></a> `00babc38` | `09 15 40 f9` | ldr x9,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00babc3c"></a> `00babc3c` | `c9 02 00 b4` | cbz x9,0x00babc94 | `CONDITIONAL_JUMP`
<a id="insn-00babc40"></a> `00babc40` | `09 21 40 b9` | ldr w9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00babc44"></a> `00babc44` | `89 02 00 35` | cbnz w9,0x00babc94 | `CONDITIONAL_JUMP`
<a id="insn-00babc48"></a> `00babc48` | `08 25 40 39` | ldrb w8,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00babc4c"></a> `00babc4c` | `48 02 28 36` | tbz w8,#0x5,0x00babc94 | `CONDITIONAL_JUMP`
<a id="insn-00babc50"></a> `00babc50` | `28 c5 02 94` | bl 0x00c5d0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00babc54"></a> `00babc54` | `00 02 00 37` | tbnz w0,#0x0,0x00babc94 | `CONDITIONAL_JUMP`
<a id="insn-00babc58"></a> `00babc58` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babc5c"></a> `00babc5c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babc60"></a> `00babc60` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00babc64"></a> `00babc64` | `00 15 40 f9` | ldr x0,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00babc68"></a> `00babc68` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00babc6c"></a> `00babc6c` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00babc70"></a> `00babc70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00babc74"></a> `00babc74` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00babc78"></a> `00babc78` | `e1 00 00 54` | b.ne 0x00babc94 | `CONDITIONAL_JUMP`
<a id="insn-00babc7c"></a> `00babc7c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00babc80"></a> `00babc80` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00babc84"></a> `00babc84` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00babc88"></a> `00babc88` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00babc8c"></a> `00babc8c` | `01 01 00 32` | orr w1,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00babc90"></a> `00babc90` | `84 b1 02 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00babc94"></a> `00babc94` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00babc98"></a> `00babc98` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00babc9c"></a> `00babc9c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00babca0"></a> `00babca0` | `21 01 00 54` | b.ne 0x00babcc4 | `CONDITIONAL_JUMP`
<a id="insn-00babca4"></a> `00babca4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00babca8"></a> `00babca8` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00babcac"></a> `00babcac` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00babcb0"></a> `00babcb0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00babcb4"></a> `00babcb4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00babcb8"></a> `00babcb8` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00babcbc"></a> `00babcbc` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00babcc0"></a> `00babcc0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00babcc4"></a> `00babcc4` | `87 b0 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00babaf4`](#insn-00babaf4) 範囲 `[['00babaf4', '00babafb']]`
  - `FALL_THROUGH` [`00babaf8`](#insn-00babaf8) → [`00babafc`](#insn-00babafc)
- ブロック [`00babafc`](#insn-00babafc) 範囲 `[['00babafc', '00babaff']]`
  - `FALL_THROUGH` [`00babafc`](#insn-00babafc) → [`00babb00`](#insn-00babb00)
- ブロック [`00babb00`](#insn-00babb00) 範囲 `[['00babb00', '00babb0f']]`
  - `FALL_THROUGH` [`00babb0c`](#insn-00babb0c) → [`00babb10`](#insn-00babb10)
- ブロック [`00babb10`](#insn-00babb10) 範囲 `[['00babb10', '00babb13']]`
  - `FALL_THROUGH` [`00babb10`](#insn-00babb10) → [`00babb14`](#insn-00babb14)
- ブロック [`00babb14`](#insn-00babb14) 範囲 `[['00babb14', '00babb23']]`
  - `FALL_THROUGH` [`00babb20`](#insn-00babb20) → [`00babb24`](#insn-00babb24)
- ブロック [`00babb24`](#insn-00babb24) 範囲 `[['00babb24', '00babb27']]`
  - `FALL_THROUGH` [`00babb24`](#insn-00babb24) → [`00babb28`](#insn-00babb28)
- ブロック [`00babb28`](#insn-00babb28) 範囲 `[['00babb28', '00babb33']]`
  - `CONDITIONAL_JUMP` [`00babb30`](#insn-00babb30) → [`00babc2c`](#insn-00babc2c)
  - `FALL_THROUGH` [`00babb30`](#insn-00babb30) → [`00babb34`](#insn-00babb34)
- ブロック [`00babb34`](#insn-00babb34) 範囲 `[['00babb34', '00babb37']]`
  - `FALL_THROUGH` [`00babb34`](#insn-00babb34) → [`00babb38`](#insn-00babb38)
- ブロック [`00babb38`](#insn-00babb38) 範囲 `[['00babb38', '00babb3b']]`
  - `FALL_THROUGH` [`00babb38`](#insn-00babb38) → [`00babb3c`](#insn-00babb3c)
- ブロック [`00babb3c`](#insn-00babb3c) 範囲 `[['00babb3c', '00babb3f']]`
  - `CONDITIONAL_JUMP` [`00babb3c`](#insn-00babb3c) → [`00babb4c`](#insn-00babb4c)
  - `FALL_THROUGH` [`00babb3c`](#insn-00babb3c) → [`00babb40`](#insn-00babb40)
- ブロック [`00babb40`](#insn-00babb40) 範囲 `[['00babb40', '00babb4b']]`
  - `FALL_THROUGH` [`00babb48`](#insn-00babb48) → [`00babb4c`](#insn-00babb4c)
- ブロック [`00babb4c`](#insn-00babb4c) 範囲 `[['00babb4c', '00babb4f']]`
  - `FALL_THROUGH` [`00babb4c`](#insn-00babb4c) → [`00babb50`](#insn-00babb50)
- ブロック [`00babb50`](#insn-00babb50) 範囲 `[['00babb50', '00babb5f']]`
  - `FALL_THROUGH` [`00babb5c`](#insn-00babb5c) → [`00babb60`](#insn-00babb60)
- ブロック [`00babb60`](#insn-00babb60) 範囲 `[['00babb60', '00babb63']]`
  - `FALL_THROUGH` [`00babb60`](#insn-00babb60) → [`00babb64`](#insn-00babb64)
- ブロック [`00babb64`](#insn-00babb64) 範囲 `[['00babb64', '00babb73']]`
  - `FALL_THROUGH` [`00babb70`](#insn-00babb70) → [`00babb74`](#insn-00babb74)
- ブロック [`00babb74`](#insn-00babb74) 範囲 `[['00babb74', '00babb77']]`
  - `FALL_THROUGH` [`00babb74`](#insn-00babb74) → [`00babb78`](#insn-00babb78)
- ブロック [`00babb78`](#insn-00babb78) 範囲 `[['00babb78', '00babb87']]`
  - `FALL_THROUGH` [`00babb84`](#insn-00babb84) → [`00babb88`](#insn-00babb88)
- ブロック [`00babb88`](#insn-00babb88) 範囲 `[['00babb88', '00babb8b']]`
  - `FALL_THROUGH` [`00babb88`](#insn-00babb88) → [`00babb8c`](#insn-00babb8c)
- ブロック [`00babb8c`](#insn-00babb8c) 範囲 `[['00babb8c', '00babb9b']]`
  - `CONDITIONAL_JUMP` [`00babb98`](#insn-00babb98) → [`00babbdc`](#insn-00babbdc)
  - `FALL_THROUGH` [`00babb98`](#insn-00babb98) → [`00babb9c`](#insn-00babb9c)
- ブロック [`00babb9c`](#insn-00babb9c) 範囲 `[['00babb9c', '00babb9f']]`
  - `FALL_THROUGH` [`00babb9c`](#insn-00babb9c) → [`00babba0`](#insn-00babba0)
- ブロック [`00babba0`](#insn-00babba0) 範囲 `[['00babba0', '00babbaf']]`
  - `FALL_THROUGH` [`00babbac`](#insn-00babbac) → [`00babbb0`](#insn-00babbb0)
- ブロック [`00babbb0`](#insn-00babbb0) 範囲 `[['00babbb0', '00babbb3']]`
  - `FALL_THROUGH` [`00babbb0`](#insn-00babbb0) → [`00babbb4`](#insn-00babbb4)
- ブロック [`00babbb4`](#insn-00babbb4) 範囲 `[['00babbb4', '00babbc3']]`
  - `FALL_THROUGH` [`00babbc0`](#insn-00babbc0) → [`00babbc4`](#insn-00babbc4)
- ブロック [`00babbc4`](#insn-00babbc4) 範囲 `[['00babbc4', '00babbc7']]`
  - `FALL_THROUGH` [`00babbc4`](#insn-00babbc4) → [`00babbc8`](#insn-00babbc8)
- ブロック [`00babbc8`](#insn-00babbc8) 範囲 `[['00babbc8', '00babbd7']]`
  - `FALL_THROUGH` [`00babbd4`](#insn-00babbd4) → [`00babbd8`](#insn-00babbd8)
- ブロック [`00babbd8`](#insn-00babbd8) 範囲 `[['00babbd8', '00babbdb']]`
  - `FALL_THROUGH` [`00babbd8`](#insn-00babbd8) → [`00babbdc`](#insn-00babbdc)
- ブロック [`00babbdc`](#insn-00babbdc) 範囲 `[['00babbdc', '00babbeb']]`
  - `FALL_THROUGH` [`00babbe8`](#insn-00babbe8) → [`00babbec`](#insn-00babbec)
- ブロック [`00babbec`](#insn-00babbec) 範囲 `[['00babbec', '00babbef']]`
  - `FALL_THROUGH` [`00babbec`](#insn-00babbec) → [`00babbf0`](#insn-00babbf0)
- ブロック [`00babbf0`](#insn-00babbf0) 範囲 `[['00babbf0', '00babbf3']]`
  - `FALL_THROUGH` [`00babbf0`](#insn-00babbf0) → [`00babbf4`](#insn-00babbf4)
- ブロック [`00babbf4`](#insn-00babbf4) 範囲 `[['00babbf4', '00babbf7']]`
  - `FALL_THROUGH` [`00babbf4`](#insn-00babbf4) → [`00babbf8`](#insn-00babbf8)
- ブロック [`00babbf8`](#insn-00babbf8) 範囲 `[['00babbf8', '00babbfb']]`
  - `FALL_THROUGH` [`00babbf8`](#insn-00babbf8) → [`00babbfc`](#insn-00babbfc)
- ブロック [`00babbfc`](#insn-00babbfc) 範囲 `[['00babbfc', '00babc0b']]`
  - `FALL_THROUGH` [`00babc08`](#insn-00babc08) → [`00babc0c`](#insn-00babc0c)
- ブロック [`00babc0c`](#insn-00babc0c) 範囲 `[['00babc0c', '00babc0f']]`
  - `CONDITIONAL_JUMP` [`00babc0c`](#insn-00babc0c) → [`00babc2c`](#insn-00babc2c)
  - `FALL_THROUGH` [`00babc0c`](#insn-00babc0c) → [`00babc10`](#insn-00babc10)
- ブロック [`00babc10`](#insn-00babc10) 範囲 `[['00babc10', '00babc1f']]`
  - `FALL_THROUGH` [`00babc1c`](#insn-00babc1c) → [`00babc20`](#insn-00babc20)
- ブロック [`00babc20`](#insn-00babc20) 範囲 `[['00babc20', '00babc23']]`
  - `FALL_THROUGH` [`00babc20`](#insn-00babc20) → [`00babc24`](#insn-00babc24)
- ブロック [`00babc24`](#insn-00babc24) 範囲 `[['00babc24', '00babc2b']]`
  - `FALL_THROUGH` [`00babc28`](#insn-00babc28) → [`00babc2c`](#insn-00babc2c)
- ブロック [`00babc2c`](#insn-00babc2c) 範囲 `[['00babc2c', '00babc33']]`
  - `FALL_THROUGH` [`00babc30`](#insn-00babc30) → [`00babc34`](#insn-00babc34)
- ブロック [`00babc34`](#insn-00babc34) 範囲 `[['00babc34', '00babc37']]`
  - `FALL_THROUGH` [`00babc34`](#insn-00babc34) → [`00babc38`](#insn-00babc38)
- ブロック [`00babc38`](#insn-00babc38) 範囲 `[['00babc38', '00babc3f']]`
  - `CONDITIONAL_JUMP` [`00babc3c`](#insn-00babc3c) → [`00babc94`](#insn-00babc94)
  - `FALL_THROUGH` [`00babc3c`](#insn-00babc3c) → [`00babc40`](#insn-00babc40)
- ブロック [`00babc40`](#insn-00babc40) 範囲 `[['00babc40', '00babc47']]`
  - `CONDITIONAL_JUMP` [`00babc44`](#insn-00babc44) → [`00babc94`](#insn-00babc94)
  - `FALL_THROUGH` [`00babc44`](#insn-00babc44) → [`00babc48`](#insn-00babc48)
- ブロック [`00babc48`](#insn-00babc48) 範囲 `[['00babc48', '00babc4b']]`
  - `FALL_THROUGH` [`00babc48`](#insn-00babc48) → [`00babc4c`](#insn-00babc4c)
- ブロック [`00babc4c`](#insn-00babc4c) 範囲 `[['00babc4c', '00babc4f']]`
  - `CONDITIONAL_JUMP` [`00babc4c`](#insn-00babc4c) → [`00babc94`](#insn-00babc94)
  - `FALL_THROUGH` [`00babc4c`](#insn-00babc4c) → [`00babc50`](#insn-00babc50)
- ブロック [`00babc50`](#insn-00babc50) 範囲 `[['00babc50', '00babc57']]`
  - `CONDITIONAL_JUMP` [`00babc54`](#insn-00babc54) → [`00babc94`](#insn-00babc94)
  - `FALL_THROUGH` [`00babc54`](#insn-00babc54) → [`00babc58`](#insn-00babc58)
- ブロック [`00babc58`](#insn-00babc58) 範囲 `[['00babc58', '00babc5b']]`
  - `FALL_THROUGH` [`00babc58`](#insn-00babc58) → [`00babc5c`](#insn-00babc5c)
- ブロック [`00babc5c`](#insn-00babc5c) 範囲 `[['00babc5c', '00babc5f']]`
  - `FALL_THROUGH` [`00babc5c`](#insn-00babc5c) → [`00babc60`](#insn-00babc60)
- ブロック [`00babc60`](#insn-00babc60) 範囲 `[['00babc60', '00babc6f']]`
  - `FALL_THROUGH` [`00babc6c`](#insn-00babc6c) → [`00babc70`](#insn-00babc70)
- ブロック [`00babc70`](#insn-00babc70) 範囲 `[['00babc70', '00babc73']]`
  - `FALL_THROUGH` [`00babc70`](#insn-00babc70) → [`00babc74`](#insn-00babc74)
- ブロック [`00babc74`](#insn-00babc74) 範囲 `[['00babc74', '00babc7b']]`
  - `CONDITIONAL_JUMP` [`00babc78`](#insn-00babc78) → [`00babc94`](#insn-00babc94)
  - `FALL_THROUGH` [`00babc78`](#insn-00babc78) → [`00babc7c`](#insn-00babc7c)
- ブロック [`00babc7c`](#insn-00babc7c) 範囲 `[['00babc7c', '00babc83']]`
  - `FALL_THROUGH` [`00babc80`](#insn-00babc80) → [`00babc84`](#insn-00babc84)
- ブロック [`00babc84`](#insn-00babc84) 範囲 `[['00babc84', '00babc87']]`
  - `FALL_THROUGH` [`00babc84`](#insn-00babc84) → [`00babc88`](#insn-00babc88)
- ブロック [`00babc88`](#insn-00babc88) 範囲 `[['00babc88', '00babc93']]`
  - `FALL_THROUGH` [`00babc90`](#insn-00babc90) → [`00babc94`](#insn-00babc94)
- ブロック [`00babc94`](#insn-00babc94) 範囲 `[['00babc94', '00babc97']]`
  - `FALL_THROUGH` [`00babc94`](#insn-00babc94) → [`00babc98`](#insn-00babc98)
- ブロック [`00babc98`](#insn-00babc98) 範囲 `[['00babc98', '00babc9b']]`
  - `FALL_THROUGH` [`00babc98`](#insn-00babc98) → [`00babc9c`](#insn-00babc9c)
- ブロック [`00babc9c`](#insn-00babc9c) 範囲 `[['00babc9c', '00babca3']]`
  - `CONDITIONAL_JUMP` [`00babca0`](#insn-00babca0) → [`00babcc4`](#insn-00babcc4)
  - `FALL_THROUGH` [`00babca0`](#insn-00babca0) → [`00babca4`](#insn-00babca4)
- ブロック [`00babca4`](#insn-00babca4) 範囲 `[['00babca4', '00babcab']]`
  - `FALL_THROUGH` [`00babca8`](#insn-00babca8) → [`00babcac`](#insn-00babcac)
- ブロック [`00babcac`](#insn-00babcac) 範囲 `[['00babcac', '00babcbb']]`
  - `FALL_THROUGH` [`00babcb8`](#insn-00babcb8) → [`00babcbc`](#insn-00babcbc)
- ブロック [`00babcbc`](#insn-00babcbc) 範囲 `[['00babcbc', '00babcc3']]`
- ブロック [`00babcc4`](#insn-00babcc4) 範囲 `[['00babcc4', '00babcc7']]`

## 命令位置別の参照

- [`00babaf8`](#insn-00babaf8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babafc`](#insn-00babafc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb00`](#insn-00babb00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb04`](#insn-00babb04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb08`](#insn-00babb08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb1c`](#insn-00babb1c) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb30`](#insn-00babb30) → [`00babc2c`](#insn-00babc2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb3c`](#insn-00babb3c) → [`00babb4c`](#insn-00babb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babb40`](#insn-00babb40) → [`00c58ef0`](../00c58/00c58ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ef0` · 推定シンボル `None` · 推定型 `None`
- [`00babb60`](#insn-00babb60) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00babb68`](#insn-00babb68) → `00c9b838`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00babb68`](#insn-00babb68) → `01127b98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00babb70`](#insn-00babb70) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00babb7c`](#insn-00babb7c) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00babb98`](#insn-00babb98) → [`00babbdc`](#insn-00babbdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babba4`](#insn-00babba4) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00babbac`](#insn-00babbac) → `00c9ac30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00babbac`](#insn-00babbac) → `01127e18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00babbb4`](#insn-00babbb4) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00babbd0`](#insn-00babbd0) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00babc0c`](#insn-00babc0c) → [`00babc2c`](#insn-00babc2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc28`](#insn-00babc28) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00babc3c`](#insn-00babc3c) → [`00babc94`](#insn-00babc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc44`](#insn-00babc44) → [`00babc94`](#insn-00babc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc4c`](#insn-00babc4c) → [`00babc94`](#insn-00babc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc50`](#insn-00babc50) → [`00c5d0f0`](../00c5d/00c5d0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d0f0` · 推定シンボル `None` · 推定型 `None`
- [`00babc54`](#insn-00babc54) → [`00babc94`](#insn-00babc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc78`](#insn-00babc78) → [`00babc94`](#insn-00babc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babc90`](#insn-00babc90) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00babc98`](#insn-00babc98) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babca0`](#insn-00babca0) → [`00babcc4`](#insn-00babcc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babca8`](#insn-00babca8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babcac`](#insn-00babcac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babcb0`](#insn-00babcb0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babcb4`](#insn-00babcb4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babcb8`](#insn-00babcb8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00babcc4`](#insn-00babcc4) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00babaf8`](#insn-00babaf8)

~~~json
{
  "source": "00babaf8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babafc`](#insn-00babafc)

~~~json
{
  "source": "00babafc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb00`](#insn-00babb00)

~~~json
{
  "source": "00babb00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb04`](#insn-00babb04)

~~~json
{
  "source": "00babb04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb08`](#insn-00babb08)

~~~json
{
  "source": "00babb08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb1c`](#insn-00babb1c)

~~~json
{
  "source": "00babb1c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb30`](#insn-00babb30)

~~~json
{
  "source": "00babb30",
  "target": "00babc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb3c`](#insn-00babb3c)

~~~json
{
  "source": "00babb3c",
  "target": "00babb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babb40`](#insn-00babb40)

~~~json
{
  "source": "00babb40",
  "target": "00c58ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babb60`](#insn-00babb60)

~~~json
{
  "source": "00babb60",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babb68`](#insn-00babb68)

~~~json
{
  "source": "00babb68",
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
- 参照命令 [`00babb68`](#insn-00babb68)

~~~json
{
  "source": "00babb68",
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
- 参照命令 [`00babb70`](#insn-00babb70)

~~~json
{
  "source": "00babb70",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babb7c`](#insn-00babb7c)

~~~json
{
  "source": "00babb7c",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babb98`](#insn-00babb98)

~~~json
{
  "source": "00babb98",
  "target": "00babbdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babba4`](#insn-00babba4)

~~~json
{
  "source": "00babba4",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babbac`](#insn-00babbac)

~~~json
{
  "source": "00babbac",
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
- 参照命令 [`00babbac`](#insn-00babbac)

~~~json
{
  "source": "00babbac",
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
- 参照命令 [`00babbb4`](#insn-00babbb4)

~~~json
{
  "source": "00babbb4",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babbd0`](#insn-00babbd0)

~~~json
{
  "source": "00babbd0",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babc0c`](#insn-00babc0c)

~~~json
{
  "source": "00babc0c",
  "target": "00babc2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc28`](#insn-00babc28)

~~~json
{
  "source": "00babc28",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babc3c`](#insn-00babc3c)

~~~json
{
  "source": "00babc3c",
  "target": "00babc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc44`](#insn-00babc44)

~~~json
{
  "source": "00babc44",
  "target": "00babc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc4c`](#insn-00babc4c)

~~~json
{
  "source": "00babc4c",
  "target": "00babc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc50`](#insn-00babc50)

~~~json
{
  "source": "00babc50",
  "target": "00c5d0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babc54`](#insn-00babc54)

~~~json
{
  "source": "00babc54",
  "target": "00babc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc78`](#insn-00babc78)

~~~json
{
  "source": "00babc78",
  "target": "00babc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babc90`](#insn-00babc90)

~~~json
{
  "source": "00babc90",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00babc98`](#insn-00babc98)

~~~json
{
  "source": "00babc98",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babca0`](#insn-00babca0)

~~~json
{
  "source": "00babca0",
  "target": "00babcc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babca8`](#insn-00babca8)

~~~json
{
  "source": "00babca8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babcac`](#insn-00babcac)

~~~json
{
  "source": "00babcac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babcb0`](#insn-00babcb0)

~~~json
{
  "source": "00babcb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babcb4`](#insn-00babcb4)

~~~json
{
  "source": "00babcb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babcb8`](#insn-00babcb8)

~~~json
{
  "source": "00babcb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00babcc4`](#insn-00babcc4)

~~~json
{
  "source": "00babcc4",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
