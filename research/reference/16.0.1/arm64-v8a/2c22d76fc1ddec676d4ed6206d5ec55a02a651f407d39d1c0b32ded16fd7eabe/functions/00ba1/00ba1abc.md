# 00ba1abc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ba1694`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ba1/00ba1694.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-03e2b991ba3af551ff9aa923c455ff21)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ba1b58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ba1/00ba1b58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0078.md#compare-85d08b7ce0ff19906bf0dab3bc3a77b2)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba1abc",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEi",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "12a32c3f17f6cffd9ebe3703bd764c502ca556b71b4bbe1aa341d5ecaf206bc1",
  "source_text_sha256": "12a32c3f17f6cffd9ebe3703bd764c502ca556b71b4bbe1aa341d5ecaf206bc1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba1abc",
        "00ba1c8f"
      ]
    ],
    "bytes_sha256": "f0c985c2c855016fef85f8ba32ccc753239fa0ac70b373b50f62f8d42ade8ce9",
    "instruction_count": 117,
    "instruction_bytes": 468,
    "body_bytes": 468,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c584d0](../00c58/00c584d0.md)

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

## 疑似コード / UTF-8 2972 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEi(long *param_1,uint param_2)

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
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b838
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_60);
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar3 = *(uint *)(lVar8 + 0x90);
    uVar9 = *(undefined8 *)(lVar8 + 0x28);
    if (uVar3 == 0xffffffff) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_60,lVar8);
      plVar6 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_60,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ac30);
      uVar3 = (**(code **)(*plVar6 + 0x38))(plVar6,0x20);
      _ZNSt6__ndk16localeD1Ev(auStack_60);
      uVar3 = uVar3 & 0xff;
      *(uint *)(lVar8 + 0x90) = uVar3;
    }
    uVar7 = (ulong)param_2;
    if (uVar1 != 8 && uVar1 != 0x40) {
      uVar7 = (long)(int)param_2;
    }
    lVar8 = (**(code **)(*plVar5 + 0x20))(plVar5,uVar9,lVar8,uVar3,uVar7);
    if (lVar8 == 0) {
      lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
      _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 5);
    }
  }
  lVar8 = *(long *)(*param_1 + -0x18);
  if ((((*(long *)((long)param_1 + lVar8 + 0x28) != 0) &&
       (*(int *)((long)param_1 + lVar8 + 0x20) == 0)) &&
      ((*(byte *)((long)param_1 + lVar8 + 9) >> 5 & 1) != 0)) &&
     ((uVar7 = _ZSt18uncaught_exceptionv(), (uVar7 & 1) == 0 &&
      (iVar4 = (**(code **)(**(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28) + 0x30))
                         (), iVar4 == -1)))) {
                    /* try { // try from 00ba1c48 to 00ca1c9f has its CatchHandler @ 00ba1c48
                       catch() { ... } // from try @ 00ba1c48 with catch @ 00ba1c48
                       catch() { ... } // from try @ 00ba1ca8 with catch @ 00ba1c48
                       catch() { ... } // from try @ 00ba1ce8 with catch @ 00ba1c48 */
    lVar8 = (long)param_1 + *(long *)(*param_1 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar8,*(uint *)(lVar8 + 0x20) | 1);
  }
  if (*(long *)(lVar2 + 0x28) == local_58) {
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
<a id="insn-00ba1abc"></a> `00ba1abc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00ba1ac0"></a> `00ba1ac0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba1ac4"></a> `00ba1ac4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba1ac8"></a> `00ba1ac8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba1acc"></a> `00ba1acc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba1ad0"></a> `00ba1ad0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba1ad4"></a> `00ba1ad4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00ba1ad8"></a> `00ba1ad8` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ba1adc"></a> `00ba1adc` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00ba1ae0"></a> `00ba1ae0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ba1ae4"></a> `00ba1ae4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba1ae8"></a> `00ba1ae8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ba1aec"></a> `00ba1aec` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00ba1af0"></a> `00ba1af0` | `09 00 08 8b` | add x9,x0,x8 | `FALL_THROUGH`
<a id="insn-00ba1af4"></a> `00ba1af4` | `2a 21 40 b9` | ldr w10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00ba1af8"></a> `00ba1af8` | `ea 07 00 35` | cbnz w10,0x00ba1bf4 | `CONDITIONAL_JUMP`
<a id="insn-00ba1afc"></a> `00ba1afc` | `20 45 40 f9` | ldr x0,[x9, #0x88] | `FALL_THROUGH`
<a id="insn-00ba1b00"></a> `00ba1b00` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00ba1b04"></a> `00ba1b04` | `80 00 00 b4` | cbz x0,0x00ba1b14 | `CONDITIONAL_JUMP`
<a id="insn-00ba1b08"></a> `00ba1b08` | `fa dc 02 94` | bl 0x00c58ef0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba1b0c"></a> `00ba1b0c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ba1b10"></a> `00ba1b10` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00ba1b14"></a> `00ba1b14` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00ba1b18"></a> `00ba1b18` | `08 08 40 b9` | ldr w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00ba1b1c"></a> `00ba1b1c` | `49 09 80 52` | mov w9,#0x4a | `FALL_THROUGH`
<a id="insn-00ba1b20"></a> `00ba1b20` | `1a 01 09 0a` | and w26,w8,w9 | `FALL_THROUGH`
<a id="insn-00ba1b24"></a> `00ba1b24` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00ba1b28"></a> `00ba1b28` | `d2 d9 02 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00ba1b2c"></a> `00ba1b2c` | `c1 07 00 d0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00ba1b30"></a> `00ba1b30` | `21 1c 44 f9` | ldr x1,[x1, #0x838] | `FALL_THROUGH`
<a id="insn-00ba1b34"></a> `00ba1b34` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00ba1b38"></a> `00ba1b38` | `d2 d9 02 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00ba1b3c"></a> `00ba1b3c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00ba1b40"></a> `00ba1b40` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00ba1b44"></a> `00ba1b44` | `d3 d9 02 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00ba1b48"></a> `00ba1b48` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ba1b4c"></a> `00ba1b4c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00ba1b50"></a> `00ba1b50` | `76 02 08 8b` | add x22,x19,x8 | `FALL_THROUGH`
<a id="insn-00ba1b54"></a> `00ba1b54` | `c3 92 40 b9` | ldr w3,[x22, #0x90] | `FALL_THROUGH`
<a id="insn-00ba1b58"></a> `00ba1b58` | `d7 16 40 f9` | ldr x23,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00ba1b5c"></a> `00ba1b5c` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00ba1b60"></a> `00ba1b60` | `21 02 00 54` | b.ne 0x00ba1ba4 | `CONDITIONAL_JUMP`
<a id="insn-00ba1b64"></a> `00ba1b64` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00ba1b68"></a> `00ba1b68` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00ba1b6c"></a> `00ba1b6c` | `c1 d9 02 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00ba1b70"></a> `00ba1b70` | `c1 07 00 b0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00ba1b74"></a> `00ba1b74` | `21 18 46 f9` | ldr x1,[x1, #0xc30] | `FALL_THROUGH`
<a id="insn-00ba1b78"></a> `00ba1b78` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00ba1b7c"></a> `00ba1b7c` | `c1 d9 02 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00ba1b80"></a> `00ba1b80` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ba1b84"></a> `00ba1b84` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00ba1b88"></a> `00ba1b88` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00ba1b8c"></a> `00ba1b8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ba1b90"></a> `00ba1b90` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00ba1b94"></a> `00ba1b94` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00ba1b98"></a> `00ba1b98` | `be d9 02 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00ba1b9c"></a> `00ba1b9c` | `03 1f 00 12` | and w3,w24,#0xff | `FALL_THROUGH`
<a id="insn-00ba1ba0"></a> `00ba1ba0` | `c3 92 00 b9` | str w3,[x22, #0x90] | `FALL_THROUGH`
<a id="insn-00ba1ba4"></a> `00ba1ba4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00ba1ba8"></a> `00ba1ba8` | `5f 23 00 71` | cmp w26,#0x8 | `FALL_THROUGH`
<a id="insn-00ba1bac"></a> `00ba1bac` | `09 08 80 52` | mov w9,#0x40 | `FALL_THROUGH`
<a id="insn-00ba1bb0"></a> `00ba1bb0` | `44 13 49 7a` | ccmp w26,w9,#0x4,ne | `FALL_THROUGH`
<a id="insn-00ba1bb4"></a> `00ba1bb4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ba1bb8"></a> `00ba1bb8` | `e9 03 14 2a` | mov w9,w20 | `FALL_THROUGH`
<a id="insn-00ba1bbc"></a> `00ba1bbc` | `8a 7e 40 93` | sxtw x10,w20 | `FALL_THROUGH`
<a id="insn-00ba1bc0"></a> `00ba1bc0` | `24 01 8a 9a` | csel x4,x9,x10,eq | `FALL_THROUGH`
<a id="insn-00ba1bc4"></a> `00ba1bc4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00ba1bc8"></a> `00ba1bc8` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00ba1bcc"></a> `00ba1bcc` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00ba1bd0"></a> `00ba1bd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ba1bd4"></a> `00ba1bd4` | `00 01 00 b5` | cbnz x0,0x00ba1bf4 | `CONDITIONAL_JUMP`
<a id="insn-00ba1bd8"></a> `00ba1bd8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ba1bdc"></a> `00ba1bdc` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00ba1be0"></a> `00ba1be0` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00ba1be4"></a> `00ba1be4` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00ba1be8"></a> `00ba1be8` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ba1bec"></a> `00ba1bec` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00ba1bf0"></a> `00ba1bf0` | `ac d9 02 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba1bf4"></a> `00ba1bf4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ba1bf8"></a> `00ba1bf8` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00ba1bfc"></a> `00ba1bfc` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00ba1c00"></a> `00ba1c00` | `09 15 40 f9` | ldr x9,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ba1c04"></a> `00ba1c04` | `c9 02 00 b4` | cbz x9,0x00ba1c5c | `CONDITIONAL_JUMP`
<a id="insn-00ba1c08"></a> `00ba1c08` | `09 21 40 b9` | ldr w9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00ba1c0c"></a> `00ba1c0c` | `89 02 00 35` | cbnz w9,0x00ba1c5c | `CONDITIONAL_JUMP`
<a id="insn-00ba1c10"></a> `00ba1c10` | `08 25 40 39` | ldrb w8,[x8, #0x9] | `FALL_THROUGH`
<a id="insn-00ba1c14"></a> `00ba1c14` | `48 02 28 36` | tbz w8,#0x5,0x00ba1c5c | `CONDITIONAL_JUMP`
<a id="insn-00ba1c18"></a> `00ba1c18` | `36 ed 02 94` | bl 0x00c5d0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba1c1c"></a> `00ba1c1c` | `00 02 00 37` | tbnz w0,#0x0,0x00ba1c5c | `CONDITIONAL_JUMP`
<a id="insn-00ba1c20"></a> `00ba1c20` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ba1c24"></a> `00ba1c24` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00ba1c28"></a> `00ba1c28` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00ba1c2c"></a> `00ba1c2c` | `00 15 40 f9` | ldr x0,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00ba1c30"></a> `00ba1c30` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ba1c34"></a> `00ba1c34` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00ba1c38"></a> `00ba1c38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ba1c3c"></a> `00ba1c3c` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ba1c40"></a> `00ba1c40` | `e1 00 00 54` | b.ne 0x00ba1c5c | `CONDITIONAL_JUMP`
<a id="insn-00ba1c44"></a> `00ba1c44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ba1c48"></a> `00ba1c48` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00ba1c4c"></a> `00ba1c4c` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00ba1c50"></a> `00ba1c50` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00ba1c54"></a> `00ba1c54` | `01 01 00 32` | orr w1,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba1c58"></a> `00ba1c58` | `92 d9 02 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba1c5c"></a> `00ba1c5c` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00ba1c60"></a> `00ba1c60` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ba1c64"></a> `00ba1c64` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ba1c68"></a> `00ba1c68` | `21 01 00 54` | b.ne 0x00ba1c8c | `CONDITIONAL_JUMP`
<a id="insn-00ba1c6c"></a> `00ba1c6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba1c70"></a> `00ba1c70` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ba1c74"></a> `00ba1c74` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ba1c78"></a> `00ba1c78` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba1c7c"></a> `00ba1c7c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba1c80"></a> `00ba1c80` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba1c84"></a> `00ba1c84` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00ba1c88"></a> `00ba1c88` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ba1c8c"></a> `00ba1c8c` | `95 d8 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba1abc`](#insn-00ba1abc) 範囲 `[['00ba1abc', '00ba1afb']]`
  - `CONDITIONAL_JUMP` [`00ba1af8`](#insn-00ba1af8) → [`00ba1bf4`](#insn-00ba1bf4)
  - `FALL_THROUGH` [`00ba1af8`](#insn-00ba1af8) → [`00ba1afc`](#insn-00ba1afc)
- ブロック [`00ba1afc`](#insn-00ba1afc) 範囲 `[['00ba1afc', '00ba1b07']]`
  - `CONDITIONAL_JUMP` [`00ba1b04`](#insn-00ba1b04) → [`00ba1b14`](#insn-00ba1b14)
  - `FALL_THROUGH` [`00ba1b04`](#insn-00ba1b04) → [`00ba1b08`](#insn-00ba1b08)
- ブロック [`00ba1b08`](#insn-00ba1b08) 範囲 `[['00ba1b08', '00ba1b13']]`
  - `FALL_THROUGH` [`00ba1b10`](#insn-00ba1b10) → [`00ba1b14`](#insn-00ba1b14)
- ブロック [`00ba1b14`](#insn-00ba1b14) 範囲 `[['00ba1b14', '00ba1b63']]`
  - `CONDITIONAL_JUMP` [`00ba1b60`](#insn-00ba1b60) → [`00ba1ba4`](#insn-00ba1ba4)
  - `FALL_THROUGH` [`00ba1b60`](#insn-00ba1b60) → [`00ba1b64`](#insn-00ba1b64)
- ブロック [`00ba1b64`](#insn-00ba1b64) 範囲 `[['00ba1b64', '00ba1ba3']]`
  - `FALL_THROUGH` [`00ba1ba0`](#insn-00ba1ba0) → [`00ba1ba4`](#insn-00ba1ba4)
- ブロック [`00ba1ba4`](#insn-00ba1ba4) 範囲 `[['00ba1ba4', '00ba1bd7']]`
  - `CONDITIONAL_JUMP` [`00ba1bd4`](#insn-00ba1bd4) → [`00ba1bf4`](#insn-00ba1bf4)
  - `FALL_THROUGH` [`00ba1bd4`](#insn-00ba1bd4) → [`00ba1bd8`](#insn-00ba1bd8)
- ブロック [`00ba1bd8`](#insn-00ba1bd8) 範囲 `[['00ba1bd8', '00ba1bf3']]`
  - `FALL_THROUGH` [`00ba1bf0`](#insn-00ba1bf0) → [`00ba1bf4`](#insn-00ba1bf4)
- ブロック [`00ba1bf4`](#insn-00ba1bf4) 範囲 `[['00ba1bf4', '00ba1c07']]`
  - `CONDITIONAL_JUMP` [`00ba1c04`](#insn-00ba1c04) → [`00ba1c5c`](#insn-00ba1c5c)
  - `FALL_THROUGH` [`00ba1c04`](#insn-00ba1c04) → [`00ba1c08`](#insn-00ba1c08)
- ブロック [`00ba1c08`](#insn-00ba1c08) 範囲 `[['00ba1c08', '00ba1c0f']]`
  - `CONDITIONAL_JUMP` [`00ba1c0c`](#insn-00ba1c0c) → [`00ba1c5c`](#insn-00ba1c5c)
  - `FALL_THROUGH` [`00ba1c0c`](#insn-00ba1c0c) → [`00ba1c10`](#insn-00ba1c10)
- ブロック [`00ba1c10`](#insn-00ba1c10) 範囲 `[['00ba1c10', '00ba1c17']]`
  - `CONDITIONAL_JUMP` [`00ba1c14`](#insn-00ba1c14) → [`00ba1c5c`](#insn-00ba1c5c)
  - `FALL_THROUGH` [`00ba1c14`](#insn-00ba1c14) → [`00ba1c18`](#insn-00ba1c18)
- ブロック [`00ba1c18`](#insn-00ba1c18) 範囲 `[['00ba1c18', '00ba1c1f']]`
  - `CONDITIONAL_JUMP` [`00ba1c1c`](#insn-00ba1c1c) → [`00ba1c5c`](#insn-00ba1c5c)
  - `FALL_THROUGH` [`00ba1c1c`](#insn-00ba1c1c) → [`00ba1c20`](#insn-00ba1c20)
- ブロック [`00ba1c20`](#insn-00ba1c20) 範囲 `[['00ba1c20', '00ba1c43']]`
  - `CONDITIONAL_JUMP` [`00ba1c40`](#insn-00ba1c40) → [`00ba1c5c`](#insn-00ba1c5c)
  - `FALL_THROUGH` [`00ba1c40`](#insn-00ba1c40) → [`00ba1c44`](#insn-00ba1c44)
- ブロック [`00ba1c44`](#insn-00ba1c44) 範囲 `[['00ba1c44', '00ba1c47']]`
  - `FALL_THROUGH` [`00ba1c44`](#insn-00ba1c44) → [`00ba1c48`](#insn-00ba1c48)
- ブロック [`00ba1c48`](#insn-00ba1c48) 範囲 `[['00ba1c48', '00ba1c5b']]`
  - `FALL_THROUGH` [`00ba1c58`](#insn-00ba1c58) → [`00ba1c5c`](#insn-00ba1c5c)
- ブロック [`00ba1c5c`](#insn-00ba1c5c) 範囲 `[['00ba1c5c', '00ba1c6b']]`
  - `CONDITIONAL_JUMP` [`00ba1c68`](#insn-00ba1c68) → [`00ba1c8c`](#insn-00ba1c8c)
  - `FALL_THROUGH` [`00ba1c68`](#insn-00ba1c68) → [`00ba1c6c`](#insn-00ba1c6c)
- ブロック [`00ba1c6c`](#insn-00ba1c6c) 範囲 `[['00ba1c6c', '00ba1c8b']]`
- ブロック [`00ba1c8c`](#insn-00ba1c8c) 範囲 `[['00ba1c8c', '00ba1c8f']]`

## 命令位置別の参照

- [`00ba1ac0`](#insn-00ba1ac0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1ac4`](#insn-00ba1ac4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1ac8`](#insn-00ba1ac8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1acc`](#insn-00ba1acc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1ad0`](#insn-00ba1ad0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1ae4`](#insn-00ba1ae4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1af8`](#insn-00ba1af8) → [`00ba1bf4`](#insn-00ba1bf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1b04`](#insn-00ba1b04) → [`00ba1b14`](#insn-00ba1b14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1b08`](#insn-00ba1b08) → [`00c58ef0`](../00c58/00c58ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ef0` · 推定シンボル `None` · 推定型 `None`
- [`00ba1b28`](#insn-00ba1b28) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00ba1b30`](#insn-00ba1b30) → `00c9b838`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba1b30`](#insn-00ba1b30) → `01127b98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00ba1b38`](#insn-00ba1b38) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00ba1b44`](#insn-00ba1b44) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00ba1b60`](#insn-00ba1b60) → [`00ba1ba4`](#insn-00ba1ba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1b6c`](#insn-00ba1b6c) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00ba1b74`](#insn-00ba1b74) → `00c9ac30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba1b74`](#insn-00ba1b74) → `01127e18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00ba1b7c`](#insn-00ba1b7c) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00ba1b98`](#insn-00ba1b98) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00ba1bd4`](#insn-00ba1bd4) → [`00ba1bf4`](#insn-00ba1bf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1bf0`](#insn-00ba1bf0) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c04`](#insn-00ba1c04) → [`00ba1c5c`](#insn-00ba1c5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c0c`](#insn-00ba1c0c) → [`00ba1c5c`](#insn-00ba1c5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c14`](#insn-00ba1c14) → [`00ba1c5c`](#insn-00ba1c5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c18`](#insn-00ba1c18) → [`00c5d0f0`](../00c5d/00c5d0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d0f0` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c1c`](#insn-00ba1c1c) → [`00ba1c5c`](#insn-00ba1c5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c40`](#insn-00ba1c40) → [`00ba1c5c`](#insn-00ba1c5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c58`](#insn-00ba1c58) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c60`](#insn-00ba1c60) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c68`](#insn-00ba1c68) → [`00ba1c8c`](#insn-00ba1c8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c70`](#insn-00ba1c70) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c74`](#insn-00ba1c74) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c78`](#insn-00ba1c78) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c7c`](#insn-00ba1c7c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c80`](#insn-00ba1c80) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba1c8c`](#insn-00ba1c8c) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba1ac0`](#insn-00ba1ac0)

~~~json
{
  "source": "00ba1ac0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1ac4`](#insn-00ba1ac4)

~~~json
{
  "source": "00ba1ac4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1ac8`](#insn-00ba1ac8)

~~~json
{
  "source": "00ba1ac8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1acc`](#insn-00ba1acc)

~~~json
{
  "source": "00ba1acc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1ad0`](#insn-00ba1ad0)

~~~json
{
  "source": "00ba1ad0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1ae4`](#insn-00ba1ae4)

~~~json
{
  "source": "00ba1ae4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1af8`](#insn-00ba1af8)

~~~json
{
  "source": "00ba1af8",
  "target": "00ba1bf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1b04`](#insn-00ba1b04)

~~~json
{
  "source": "00ba1b04",
  "target": "00ba1b14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1b08`](#insn-00ba1b08)

~~~json
{
  "source": "00ba1b08",
  "target": "00c58ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba1b28`](#insn-00ba1b28)

~~~json
{
  "source": "00ba1b28",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba1b30`](#insn-00ba1b30)

~~~json
{
  "source": "00ba1b30",
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
- 参照命令 [`00ba1b30`](#insn-00ba1b30)

~~~json
{
  "source": "00ba1b30",
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
- 参照命令 [`00ba1b38`](#insn-00ba1b38)

~~~json
{
  "source": "00ba1b38",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba1b44`](#insn-00ba1b44)

~~~json
{
  "source": "00ba1b44",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba1b60`](#insn-00ba1b60)

~~~json
{
  "source": "00ba1b60",
  "target": "00ba1ba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1b6c`](#insn-00ba1b6c)

~~~json
{
  "source": "00ba1b6c",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba1b74`](#insn-00ba1b74)

~~~json
{
  "source": "00ba1b74",
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
- 参照命令 [`00ba1b74`](#insn-00ba1b74)

~~~json
{
  "source": "00ba1b74",
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
- 参照命令 [`00ba1b7c`](#insn-00ba1b7c)

~~~json
{
  "source": "00ba1b7c",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba1b98`](#insn-00ba1b98)

~~~json
{
  "source": "00ba1b98",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba1bd4`](#insn-00ba1bd4)

~~~json
{
  "source": "00ba1bd4",
  "target": "00ba1bf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1bf0`](#insn-00ba1bf0)

~~~json
{
  "source": "00ba1bf0",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba1c04`](#insn-00ba1c04)

~~~json
{
  "source": "00ba1c04",
  "target": "00ba1c5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c0c`](#insn-00ba1c0c)

~~~json
{
  "source": "00ba1c0c",
  "target": "00ba1c5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c14`](#insn-00ba1c14)

~~~json
{
  "source": "00ba1c14",
  "target": "00ba1c5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c18`](#insn-00ba1c18)

~~~json
{
  "source": "00ba1c18",
  "target": "00c5d0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba1c1c`](#insn-00ba1c1c)

~~~json
{
  "source": "00ba1c1c",
  "target": "00ba1c5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c40`](#insn-00ba1c40)

~~~json
{
  "source": "00ba1c40",
  "target": "00ba1c5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c58`](#insn-00ba1c58)

~~~json
{
  "source": "00ba1c58",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba1c60`](#insn-00ba1c60)

~~~json
{
  "source": "00ba1c60",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c68`](#insn-00ba1c68)

~~~json
{
  "source": "00ba1c68",
  "target": "00ba1c8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c70`](#insn-00ba1c70)

~~~json
{
  "source": "00ba1c70",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c74`](#insn-00ba1c74)

~~~json
{
  "source": "00ba1c74",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c78`](#insn-00ba1c78)

~~~json
{
  "source": "00ba1c78",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c7c`](#insn-00ba1c7c)

~~~json
{
  "source": "00ba1c7c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c80`](#insn-00ba1c80)

~~~json
{
  "source": "00ba1c80",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba1c8c`](#insn-00ba1c8c)

~~~json
{
  "source": "00ba1c8c",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
