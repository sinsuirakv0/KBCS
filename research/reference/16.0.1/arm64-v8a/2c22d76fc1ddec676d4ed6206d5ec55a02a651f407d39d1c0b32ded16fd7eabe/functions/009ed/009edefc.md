# 009edefc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `009edd60`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/009ed/009edd60.md) · 移動量 `+0x19c`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0033.md#compare-c43ebb93d8ff0c913493a4fdcbcd3d8f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `009edf50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/009ed/009edf50.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0032.md#compare-4178be7cb49b418883781462085f3623)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009edefc",
  "name": "FUN_009edefc",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "90cdd9e44e04f9ae6daad79aa190d88e5d60dcdb7414f6e5bd83da7b102aa1d7",
  "source_text_sha256": "90cdd9e44e04f9ae6daad79aa190d88e5d60dcdb7414f6e5bd83da7b102aa1d7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009edefc",
        "009ee107"
      ],
      [
        "009ee134",
        "009ee137"
      ]
    ],
    "bytes_sha256": "1e825a85440fa72dbc7eb57b9da33a78faf55bc9f298e91afe4f2693b916b74a",
    "instruction_count": 132,
    "instruction_bytes": 528,
    "body_bytes": 528,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009ee138](../009ee/009ee138.md)

## 呼び出し先

- [0043bba4](../0043b/0043bba4.md)
- [0044108c](../00441/0044108c.md)
- [009edb3c](../009ed/009edb3c.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58060](../00c58/00c58060.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3677 bytes

~~~c

void FUN_009edefc(long *param_1,long param_2,undefined8 param_3)

{
  long lVar1;
  bool bVar2;
  int iVar3;
  long lVar4;
  undefined8 uVar5;
  long *plVar6;
  ulong uVar7;
  long *plVar8;
  long *plVar9;
  long lVar10;
  long *plVar11;
  long *plVar12;
  byte local_80 [16];
  void *local_70;
  long local_68;
  
                    /* try { // try from 009edefc to 00aedf0b has its CatchHandler @ 009ef734 */
                    /* try { // try from 009edf0c to 00aedf17 has its CatchHandler @ 009ef714 */
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  local_80[0] = 0x10;
  local_80[9] = 0;
  local_80[1] = 0x42;
  local_80[2] = 0x6f;
  local_80[3] = 0x6e;
  local_80[4] = 0x75;
  local_80[5] = 0x73;
  local_80[6] = 0x4e;
  local_80[7] = 0x75;
  local_80[8] = 0x6d;
                    /* try { // try from 009edf58 to 00aedf5f has its CatchHandler @ 009ef3dc */
  lVar4 = FUN_0044108c(param_2 + 0x10,local_80);
                    /* try { // try from 009edf60 to 00aedf6f has its CatchHandler @ 009ef6d4 */
  if (param_2 + 0x18 == lVar4) {
    lVar4 = 0;
  }
  else {
    lVar4 = *(long *)(lVar4 + 0x38);
                    /* try { // try from 009edf70 to 00aedf7b has its CatchHandler @ 009ef6b4 */
    if (*(int *)(lVar4 + 8) != 7) {
      lVar4 = 0;
    }
  }
  if ((local_80[0] & 1) != 0) {
    _ZdlPv(local_70);
  }
                    /* try { // try from 009edf98 to 00aee103 has its CatchHandler @ 009ed1b8 */
  plVar11 = *(long **)(lVar4 + 0x10);
  if (plVar11 != (long *)(lVar4 + 0x18)) {
    do {
      iVar3 = _ZNSt6__ndk14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
                        (plVar11 + 4,0,10);
      lVar10 = plVar11[7];
      uVar5 = 0;
      if ((lVar10 == 0) || (*(int *)(lVar10 + 8) != 7)) goto LAB_009ee0d4;
      plVar9 = (long *)param_1[1];
      plVar8 = param_1 + 1;
      while (plVar12 = plVar8, plVar9 != (long *)0x0) {
        while (plVar6 = plVar9, plVar8 = plVar6, (int)plVar6[4] <= iVar3) {
          if (iVar3 <= (int)plVar6[4]) goto LAB_009ee084;
          plVar9 = (long *)plVar6[1];
          if ((long *)plVar6[1] == (long *)0x0) {
            plVar12 = plVar6 + 1;
            goto LAB_009ee02c;
          }
        }
        plVar9 = (long *)*plVar6;
      }
LAB_009ee02c:
      plVar6 = (long *)_Znwm(0x48);
      *plVar6 = 0;
      plVar6[1] = 0;
      plVar6[7] = 0;
      plVar6[8] = 0;
      plVar6[6] = 0;
      plVar6[2] = (long)plVar8;
      *plVar12 = (long)plVar6;
      plVar9 = (long *)*param_1;
      *(int *)(plVar6 + 4) = iVar3;
      *(undefined4 *)(plVar6 + 5) = 0;
      plVar8 = plVar6;
      if (*plVar9 != 0) {
        *param_1 = *plVar9;
        plVar8 = (long *)*plVar12;
      }
      FUN_0043bba4(param_1[1],plVar8);
      param_1[2] = param_1[2] + 1;
LAB_009ee084:
      uVar7 = FUN_009edb3c(plVar6 + 5,lVar10,param_3);
      if ((uVar7 & 1) == 0) {
        uVar5 = 0;
        goto LAB_009ee0d4;
      }
      plVar8 = (long *)plVar11[1];
      plVar9 = plVar11;
      if ((long *)plVar11[1] == (long *)0x0) {
        do {
          plVar11 = (long *)plVar9[2];
          bVar2 = (long *)*plVar11 != plVar9;
          plVar9 = plVar11;
        } while (bVar2);
      }
      else {
        do {
          plVar11 = plVar8;
          plVar8 = (long *)*plVar11;
        } while ((long *)*plVar11 != (long *)0x0);
      }
    } while (plVar11 != (long *)(lVar4 + 0x18));
  }
  uVar5 = 1;
LAB_009ee0d4:
  if (*(long *)(lVar1 + 0x28) == local_68) {
                    /* try { // try from 009ee104 to 00aee10b has its CatchHandler @ 009ef3d4 */
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar5);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009edefc"></a> `009edefc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-009edf00"></a> `009edf00` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009edf04"></a> `009edf04` | `fc 6f 04 a9` | stp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009edf08"></a> `009edf08` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009edf0c"></a> `009edf0c` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009edf10"></a> `009edf10` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009edf14"></a> `009edf14` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009edf18"></a> `009edf18` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-009edf1c"></a> `009edf1c` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009edf20"></a> `009edf20` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-009edf24"></a> `009edf24` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-009edf28"></a> `009edf28` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-009edf2c"></a> `009edf2c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-009edf30"></a> `009edf30` | `09 02 80 52` | mov w9,#0x10 | `FALL_THROUGH`
<a id="insn-009edf34"></a> `009edf34` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009edf38"></a> `009edf38` | `48 e8 8d d2` | mov x8,#0x6f42 | `FALL_THROUGH`
<a id="insn-009edf3c"></a> `009edf3c` | `c8 ad ae f2` | movk x8,#0x756e, LSL #16 | `FALL_THROUGH`
<a id="insn-009edf40"></a> `009edf40` | `e9 43 00 39` | strb w9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009edf44"></a> `009edf44` | `68 ce c9 f2` | movk x8,#0x4e73, LSL #32 | `FALL_THROUGH`
<a id="insn-009edf48"></a> `009edf48` | `ff 67 00 39` | strb wzr,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-009edf4c"></a> `009edf4c` | `a8 ae ed f2` | movk x8,#0x6d75, LSL #48 | `FALL_THROUGH`
<a id="insn-009edf50"></a> `009edf50` | `e8 13 01 f8` | stur x8,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-009edf54"></a> `009edf54` | `20 40 00 91` | add x0,x1,#0x10 | `FALL_THROUGH`
<a id="insn-009edf58"></a> `009edf58` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-009edf5c"></a> `009edf5c` | `4c 4c e9 97` | bl 0x0044108c | `UNCONDITIONAL_CALL`
<a id="insn-009edf60"></a> `009edf60` | `a8 62 00 91` | add x8,x21,#0x18 | `FALL_THROUGH`
<a id="insn-009edf64"></a> `009edf64` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-009edf68"></a> `009edf68` | `c0 00 00 54` | b.eq 0x009edf80 | `CONDITIONAL_JUMP`
<a id="insn-009edf6c"></a> `009edf6c` | `08 1c 40 f9` | ldr x8,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-009edf70"></a> `009edf70` | `09 09 40 b9` | ldr w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-009edf74"></a> `009edf74` | `3f 1d 00 71` | cmp w9,#0x7 | `FALL_THROUGH`
<a id="insn-009edf78"></a> `009edf78` | `15 01 9f 9a` | csel x21,x8,xzr,eq | `FALL_THROUGH`
<a id="insn-009edf7c"></a> `009edf7c` | `02 00 00 14` | b 0x009edf84 | `UNCONDITIONAL_JUMP`
<a id="insn-009edf80"></a> `009edf80` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-009edf84"></a> `009edf84` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-009edf88"></a> `009edf88` | `f6 07 00 f9` | str x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009edf8c"></a> `009edf8c` | `68 00 00 36` | tbz w8,#0x0,0x009edf98 | `CONDITIONAL_JUMP`
<a id="insn-009edf90"></a> `009edf90` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009edf94"></a> `009edf94` | `c7 a7 09 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-009edf98"></a> `009edf98` | `bb 0a 40 f9` | ldr x27,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-009edf9c"></a> `009edf9c` | `b9 62 00 91` | add x25,x21,#0x18 | `FALL_THROUGH`
<a id="insn-009edfa0"></a> `009edfa0` | `7f 03 19 eb` | cmp x27,x25 | `FALL_THROUGH`
<a id="insn-009edfa4"></a> `009edfa4` | `20 09 00 54` | b.eq 0x009ee0c8 | `CONDITIONAL_JUMP`
<a id="insn-009edfa8"></a> `009edfa8` | `9a 22 00 91` | add x26,x20,#0x8 | `FALL_THROUGH`
<a id="insn-009edfac"></a> `009edfac` | `04 00 00 14` | b 0x009edfbc | `UNCONDITIONAL_JUMP`
<a id="insn-009edfb0"></a> `009edfb0` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-009edfb4"></a> `009edfb4` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-009edfb8"></a> `009edfb8` | `80 08 00 54` | b.eq 0x009ee0c8 | `CONDITIONAL_JUMP`
<a id="insn-009edfbc"></a> `009edfbc` | `60 83 00 91` | add x0,x27,#0x20 | `FALL_THROUGH`
<a id="insn-009edfc0"></a> `009edfc0` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-009edfc4"></a> `009edfc4` | `42 01 80 52` | mov w2,#0xa | `FALL_THROUGH`
<a id="insn-009edfc8"></a> `009edfc8` | `26 a8 09 94` | bl 0x00c58060 | `UNCONDITIONAL_CALL`
<a id="insn-009edfcc"></a> `009edfcc` | `75 1f 40 f9` | ldr x21,[x27, #0x38] | `FALL_THROUGH`
<a id="insn-009edfd0"></a> `009edfd0` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-009edfd4"></a> `009edfd4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-009edfd8"></a> `009edfd8` | `f5 07 00 b4` | cbz x21,0x009ee0d4 | `CONDITIONAL_JUMP`
<a id="insn-009edfdc"></a> `009edfdc` | `a8 0a 40 b9` | ldr w8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-009edfe0"></a> `009edfe0` | `1f 1d 00 71` | cmp w8,#0x7 | `FALL_THROUGH`
<a id="insn-009edfe4"></a> `009edfe4` | `81 07 00 54` | b.ne 0x009ee0d4 | `CONDITIONAL_JUMP`
<a id="insn-009edfe8"></a> `009edfe8` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-009edfec"></a> `009edfec` | `fc 03 1a aa` | mov x28,x26 | `FALL_THROUGH`
<a id="insn-009edff0"></a> `009edff0` | `f6 03 1a aa` | mov x22,x26 | `FALL_THROUGH`
<a id="insn-009edff4"></a> `009edff4` | `a8 00 00 b5` | cbnz x8,0x009ee008 | `CONDITIONAL_JUMP`
<a id="insn-009edff8"></a> `009edff8` | `0d 00 00 14` | b 0x009ee02c | `UNCONDITIONAL_JUMP`
<a id="insn-009edffc"></a> `009edffc` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-009ee000"></a> `009ee000` | `fc 03 16 aa` | mov x28,x22 | `FALL_THROUGH`
<a id="insn-009ee004"></a> `009ee004` | `48 01 00 b4` | cbz x8,0x009ee02c | `CONDITIONAL_JUMP`
<a id="insn-009ee008"></a> `009ee008` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-009ee00c"></a> `009ee00c` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-009ee010"></a> `009ee010` | `ff 02 08 6b` | cmp w23,w8 | `FALL_THROUGH`
<a id="insn-009ee014"></a> `009ee014` | `4b ff ff 54` | b.lt 0x009edffc | `CONDITIONAL_JUMP`
<a id="insn-009ee018"></a> `009ee018` | `1f 01 17 6b` | cmp w8,w23 | `FALL_THROUGH`
<a id="insn-009ee01c"></a> `009ee01c` | `4a 03 00 54` | b.ge 0x009ee084 | `CONDITIONAL_JUMP`
<a id="insn-009ee020"></a> `009ee020` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-009ee024"></a> `009ee024` | `28 ff ff b5` | cbnz x8,0x009ee008 | `CONDITIONAL_JUMP`
<a id="insn-009ee028"></a> `009ee028` | `dc 22 00 91` | add x28,x22,#0x8 | `FALL_THROUGH`
<a id="insn-009ee02c"></a> `009ee02c` | `00 09 80 52` | mov w0,#0x48 | `FALL_THROUGH`
<a id="insn-009ee030"></a> `009ee030` | `f8 03 16 aa` | mov x24,x22 | `FALL_THROUGH`
<a id="insn-009ee034"></a> `009ee034` | `97 a7 09 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-009ee038"></a> `009ee038` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-009ee03c"></a> `009ee03c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-009ee040"></a> `009ee040` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-009ee044"></a> `009ee044` | `1f fc 03 a9` | stp xzr,xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-009ee048"></a> `009ee048` | `1f 18 00 f9` | str xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-009ee04c"></a> `009ee04c` | `18 08 00 f9` | str x24,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-009ee050"></a> `009ee050` | `80 03 00 f9` | str x0,[x28] | `FALL_THROUGH`
<a id="insn-009ee054"></a> `009ee054` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-009ee058"></a> `009ee058` | `17 20 00 b9` | str w23,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-009ee05c"></a> `009ee05c` | `1f 28 00 b9` | str wzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-009ee060"></a> `009ee060` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-009ee064"></a> `009ee064` | `68 00 00 b4` | cbz x8,0x009ee070 | `CONDITIONAL_JUMP`
<a id="insn-009ee068"></a> `009ee068` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-009ee06c"></a> `009ee06c` | `81 03 40 f9` | ldr x1,[x28] | `FALL_THROUGH`
<a id="insn-009ee070"></a> `009ee070` | `80 06 40 f9` | ldr x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-009ee074"></a> `009ee074` | `cc 36 e9 97` | bl 0x0043bba4 | `UNCONDITIONAL_CALL`
<a id="insn-009ee078"></a> `009ee078` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-009ee07c"></a> `009ee07c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-009ee080"></a> `009ee080` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-009ee084"></a> `009ee084` | `c0 a2 00 91` | add x0,x22,#0x28 | `FALL_THROUGH`
<a id="insn-009ee088"></a> `009ee088` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-009ee08c"></a> `009ee08c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-009ee090"></a> `009ee090` | `ab fe ff 97` | bl 0x009edb3c | `UNCONDITIONAL_CALL`
<a id="insn-009ee094"></a> `009ee094` | `e0 01 00 36` | tbz w0,#0x0,0x009ee0d0 | `CONDITIONAL_JUMP`
<a id="insn-009ee098"></a> `009ee098` | `69 07 40 f9` | ldr x9,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-009ee09c"></a> `009ee09c` | `a9 00 00 b4` | cbz x9,0x009ee0b0 | `CONDITIONAL_JUMP`
<a id="insn-009ee0a0"></a> `009ee0a0` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-009ee0a4"></a> `009ee0a4` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-009ee0a8"></a> `009ee0a8` | `c9 ff ff b5` | cbnz x9,0x009ee0a0 | `CONDITIONAL_JUMP`
<a id="insn-009ee0ac"></a> `009ee0ac` | `c1 ff ff 17` | b 0x009edfb0 | `UNCONDITIONAL_JUMP`
<a id="insn-009ee0b0"></a> `009ee0b0` | `68 0b 40 f9` | ldr x8,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-009ee0b4"></a> `009ee0b4` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-009ee0b8"></a> `009ee0b8` | `3f 01 1b eb` | cmp x9,x27 | `FALL_THROUGH`
<a id="insn-009ee0bc"></a> `009ee0bc` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-009ee0c0"></a> `009ee0c0` | `81 ff ff 54` | b.ne 0x009ee0b0 | `CONDITIONAL_JUMP`
<a id="insn-009ee0c4"></a> `009ee0c4` | `bb ff ff 17` | b 0x009edfb0 | `UNCONDITIONAL_JUMP`
<a id="insn-009ee0c8"></a> `009ee0c8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009ee0cc"></a> `009ee0cc` | `02 00 00 14` | b 0x009ee0d4 | `UNCONDITIONAL_JUMP`
<a id="insn-009ee0d0"></a> `009ee0d0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-009ee0d4"></a> `009ee0d4` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009ee0d8"></a> `009ee0d8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-009ee0dc"></a> `009ee0dc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009ee0e0"></a> `009ee0e0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009ee0e4"></a> `009ee0e4` | `81 02 00 54` | b.ne 0x009ee134 | `CONDITIONAL_JUMP`
<a id="insn-009ee0e8"></a> `009ee0e8` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-009ee0ec"></a> `009ee0ec` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-009ee0f0"></a> `009ee0f0` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009ee0f4"></a> `009ee0f4` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009ee0f8"></a> `009ee0f8` | `fc 6f 44 a9` | ldp x28,x27,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009ee0fc"></a> `009ee0fc` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009ee100"></a> `009ee100` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-009ee104"></a> `009ee104` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009ee134"></a> `009ee134` | `6b a7 09 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009edefc`](#insn-009edefc) 範囲 `[['009edefc', '009edf0b']]`
  - `FALL_THROUGH` [`009edf08`](#insn-009edf08) → [`009edf0c`](#insn-009edf0c)
- ブロック [`009edf0c`](#insn-009edf0c) 範囲 `[['009edf0c', '009edf57']]`
  - `FALL_THROUGH` [`009edf54`](#insn-009edf54) → [`009edf58`](#insn-009edf58)
- ブロック [`009edf58`](#insn-009edf58) 範囲 `[['009edf58', '009edf5f']]`
  - `FALL_THROUGH` [`009edf5c`](#insn-009edf5c) → [`009edf60`](#insn-009edf60)
- ブロック [`009edf60`](#insn-009edf60) 範囲 `[['009edf60', '009edf6b']]`
  - `CONDITIONAL_JUMP` [`009edf68`](#insn-009edf68) → [`009edf80`](#insn-009edf80)
  - `FALL_THROUGH` [`009edf68`](#insn-009edf68) → [`009edf6c`](#insn-009edf6c)
- ブロック [`009edf6c`](#insn-009edf6c) 範囲 `[['009edf6c', '009edf6f']]`
  - `FALL_THROUGH` [`009edf6c`](#insn-009edf6c) → [`009edf70`](#insn-009edf70)
- ブロック [`009edf70`](#insn-009edf70) 範囲 `[['009edf70', '009edf7b']]`
  - `FALL_THROUGH` [`009edf78`](#insn-009edf78) → [`009edf7c`](#insn-009edf7c)
- ブロック [`009edf7c`](#insn-009edf7c) 範囲 `[['009edf7c', '009edf7f']]`
  - `UNCONDITIONAL_JUMP` [`009edf7c`](#insn-009edf7c) → [`009edf84`](#insn-009edf84)
- ブロック [`009edf80`](#insn-009edf80) 範囲 `[['009edf80', '009edf83']]`
  - `FALL_THROUGH` [`009edf80`](#insn-009edf80) → [`009edf84`](#insn-009edf84)
- ブロック [`009edf84`](#insn-009edf84) 範囲 `[['009edf84', '009edf8f']]`
  - `CONDITIONAL_JUMP` [`009edf8c`](#insn-009edf8c) → [`009edf98`](#insn-009edf98)
  - `FALL_THROUGH` [`009edf8c`](#insn-009edf8c) → [`009edf90`](#insn-009edf90)
- ブロック [`009edf90`](#insn-009edf90) 範囲 `[['009edf90', '009edf97']]`
  - `FALL_THROUGH` [`009edf94`](#insn-009edf94) → [`009edf98`](#insn-009edf98)
- ブロック [`009edf98`](#insn-009edf98) 範囲 `[['009edf98', '009edfa7']]`
  - `CONDITIONAL_JUMP` [`009edfa4`](#insn-009edfa4) → [`009ee0c8`](#insn-009ee0c8)
  - `FALL_THROUGH` [`009edfa4`](#insn-009edfa4) → [`009edfa8`](#insn-009edfa8)
- ブロック [`009edfa8`](#insn-009edfa8) 範囲 `[['009edfa8', '009edfaf']]`
  - `UNCONDITIONAL_JUMP` [`009edfac`](#insn-009edfac) → [`009edfbc`](#insn-009edfbc)
- ブロック [`009edfb0`](#insn-009edfb0) 範囲 `[['009edfb0', '009edfbb']]`
  - `CONDITIONAL_JUMP` [`009edfb8`](#insn-009edfb8) → [`009ee0c8`](#insn-009ee0c8)
  - `FALL_THROUGH` [`009edfb8`](#insn-009edfb8) → [`009edfbc`](#insn-009edfbc)
- ブロック [`009edfbc`](#insn-009edfbc) 範囲 `[['009edfbc', '009edfdb']]`
  - `CONDITIONAL_JUMP` [`009edfd8`](#insn-009edfd8) → [`009ee0d4`](#insn-009ee0d4)
  - `FALL_THROUGH` [`009edfd8`](#insn-009edfd8) → [`009edfdc`](#insn-009edfdc)
- ブロック [`009edfdc`](#insn-009edfdc) 範囲 `[['009edfdc', '009edfe7']]`
  - `CONDITIONAL_JUMP` [`009edfe4`](#insn-009edfe4) → [`009ee0d4`](#insn-009ee0d4)
  - `FALL_THROUGH` [`009edfe4`](#insn-009edfe4) → [`009edfe8`](#insn-009edfe8)
- ブロック [`009edfe8`](#insn-009edfe8) 範囲 `[['009edfe8', '009edff7']]`
  - `CONDITIONAL_JUMP` [`009edff4`](#insn-009edff4) → [`009ee008`](#insn-009ee008)
  - `FALL_THROUGH` [`009edff4`](#insn-009edff4) → [`009edff8`](#insn-009edff8)
- ブロック [`009edff8`](#insn-009edff8) 範囲 `[['009edff8', '009edffb']]`
  - `UNCONDITIONAL_JUMP` [`009edff8`](#insn-009edff8) → [`009ee02c`](#insn-009ee02c)
- ブロック [`009edffc`](#insn-009edffc) 範囲 `[['009edffc', '009ee007']]`
  - `CONDITIONAL_JUMP` [`009ee004`](#insn-009ee004) → [`009ee02c`](#insn-009ee02c)
  - `FALL_THROUGH` [`009ee004`](#insn-009ee004) → [`009ee008`](#insn-009ee008)
- ブロック [`009ee008`](#insn-009ee008) 範囲 `[['009ee008', '009ee017']]`
  - `CONDITIONAL_JUMP` [`009ee014`](#insn-009ee014) → [`009edffc`](#insn-009edffc)
  - `FALL_THROUGH` [`009ee014`](#insn-009ee014) → [`009ee018`](#insn-009ee018)
- ブロック [`009ee018`](#insn-009ee018) 範囲 `[['009ee018', '009ee01f']]`
  - `CONDITIONAL_JUMP` [`009ee01c`](#insn-009ee01c) → [`009ee084`](#insn-009ee084)
  - `FALL_THROUGH` [`009ee01c`](#insn-009ee01c) → [`009ee020`](#insn-009ee020)
- ブロック [`009ee020`](#insn-009ee020) 範囲 `[['009ee020', '009ee027']]`
  - `CONDITIONAL_JUMP` [`009ee024`](#insn-009ee024) → [`009ee008`](#insn-009ee008)
  - `FALL_THROUGH` [`009ee024`](#insn-009ee024) → [`009ee028`](#insn-009ee028)
- ブロック [`009ee028`](#insn-009ee028) 範囲 `[['009ee028', '009ee02b']]`
  - `FALL_THROUGH` [`009ee028`](#insn-009ee028) → [`009ee02c`](#insn-009ee02c)
- ブロック [`009ee02c`](#insn-009ee02c) 範囲 `[['009ee02c', '009ee067']]`
  - `CONDITIONAL_JUMP` [`009ee064`](#insn-009ee064) → [`009ee070`](#insn-009ee070)
  - `FALL_THROUGH` [`009ee064`](#insn-009ee064) → [`009ee068`](#insn-009ee068)
- ブロック [`009ee068`](#insn-009ee068) 範囲 `[['009ee068', '009ee06f']]`
  - `FALL_THROUGH` [`009ee06c`](#insn-009ee06c) → [`009ee070`](#insn-009ee070)
- ブロック [`009ee070`](#insn-009ee070) 範囲 `[['009ee070', '009ee083']]`
  - `FALL_THROUGH` [`009ee080`](#insn-009ee080) → [`009ee084`](#insn-009ee084)
- ブロック [`009ee084`](#insn-009ee084) 範囲 `[['009ee084', '009ee097']]`
  - `CONDITIONAL_JUMP` [`009ee094`](#insn-009ee094) → [`009ee0d0`](#insn-009ee0d0)
  - `FALL_THROUGH` [`009ee094`](#insn-009ee094) → [`009ee098`](#insn-009ee098)
- ブロック [`009ee098`](#insn-009ee098) 範囲 `[['009ee098', '009ee09f']]`
  - `CONDITIONAL_JUMP` [`009ee09c`](#insn-009ee09c) → [`009ee0b0`](#insn-009ee0b0)
  - `FALL_THROUGH` [`009ee09c`](#insn-009ee09c) → [`009ee0a0`](#insn-009ee0a0)
- ブロック [`009ee0a0`](#insn-009ee0a0) 範囲 `[['009ee0a0', '009ee0ab']]`
  - `CONDITIONAL_JUMP` [`009ee0a8`](#insn-009ee0a8) → [`009ee0a0`](#insn-009ee0a0)
  - `FALL_THROUGH` [`009ee0a8`](#insn-009ee0a8) → [`009ee0ac`](#insn-009ee0ac)
- ブロック [`009ee0ac`](#insn-009ee0ac) 範囲 `[['009ee0ac', '009ee0af']]`
  - `UNCONDITIONAL_JUMP` [`009ee0ac`](#insn-009ee0ac) → [`009edfb0`](#insn-009edfb0)
- ブロック [`009ee0b0`](#insn-009ee0b0) 範囲 `[['009ee0b0', '009ee0c3']]`
  - `CONDITIONAL_JUMP` [`009ee0c0`](#insn-009ee0c0) → [`009ee0b0`](#insn-009ee0b0)
  - `FALL_THROUGH` [`009ee0c0`](#insn-009ee0c0) → [`009ee0c4`](#insn-009ee0c4)
- ブロック [`009ee0c4`](#insn-009ee0c4) 範囲 `[['009ee0c4', '009ee0c7']]`
  - `UNCONDITIONAL_JUMP` [`009ee0c4`](#insn-009ee0c4) → [`009edfb0`](#insn-009edfb0)
- ブロック [`009ee0c8`](#insn-009ee0c8) 範囲 `[['009ee0c8', '009ee0cf']]`
  - `UNCONDITIONAL_JUMP` [`009ee0cc`](#insn-009ee0cc) → [`009ee0d4`](#insn-009ee0d4)
- ブロック [`009ee0d0`](#insn-009ee0d0) 範囲 `[['009ee0d0', '009ee0d3']]`
  - `FALL_THROUGH` [`009ee0d0`](#insn-009ee0d0) → [`009ee0d4`](#insn-009ee0d4)
- ブロック [`009ee0d4`](#insn-009ee0d4) 範囲 `[['009ee0d4', '009ee0e7']]`
  - `CONDITIONAL_JUMP` [`009ee0e4`](#insn-009ee0e4) → [`009ee134`](#insn-009ee134)
  - `FALL_THROUGH` [`009ee0e4`](#insn-009ee0e4) → [`009ee0e8`](#insn-009ee0e8)
- ブロック [`009ee0e8`](#insn-009ee0e8) 範囲 `[['009ee0e8', '009ee103']]`
  - `FALL_THROUGH` [`009ee100`](#insn-009ee100) → [`009ee104`](#insn-009ee104)
- ブロック [`009ee104`](#insn-009ee104) 範囲 `[['009ee104', '009ee107']]`
- ブロック [`009ee134`](#insn-009ee134) 範囲 `[['009ee134', '009ee137']]`

## 命令位置別の参照

- [`009edf00`](#insn-009edf00) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf04`](#insn-009edf04) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf08`](#insn-009edf08) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf0c`](#insn-009edf0c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf10`](#insn-009edf10) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf14`](#insn-009edf14) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf34`](#insn-009edf34) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf40`](#insn-009edf40) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf48`](#insn-009edf48) → `Stack[-0x77]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf50`](#insn-009edf50) → `Stack[-0x7f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf5c`](#insn-009edf5c) → [`0044108c`](../00441/0044108c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044108c` · 推定シンボル `None` · 推定型 `None`
- [`009edf68`](#insn-009edf68) → [`009edf80`](#insn-009edf80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf7c`](#insn-009edf7c) → [`009edf84`](#insn-009edf84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf84`](#insn-009edf84) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf88`](#insn-009edf88) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf8c`](#insn-009edf8c) → [`009edf98`](#insn-009edf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf90`](#insn-009edf90) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edf94`](#insn-009edf94) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`009edfa4`](#insn-009edfa4) → [`009ee0c8`](#insn-009ee0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edfac`](#insn-009edfac) → [`009edfbc`](#insn-009edfbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edfb8`](#insn-009edfb8) → [`009ee0c8`](#insn-009ee0c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edfc8`](#insn-009edfc8) → [`00c58060`](../00c58/00c58060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58060` · 推定シンボル `None` · 推定型 `None`
- [`009edfd8`](#insn-009edfd8) → [`009ee0d4`](#insn-009ee0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edfe4`](#insn-009edfe4) → [`009ee0d4`](#insn-009ee0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edff4`](#insn-009edff4) → [`009ee008`](#insn-009ee008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009edff8`](#insn-009edff8) → [`009ee02c`](#insn-009ee02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee004`](#insn-009ee004) → [`009ee02c`](#insn-009ee02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee014`](#insn-009ee014) → [`009edffc`](#insn-009edffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee01c`](#insn-009ee01c) → [`009ee084`](#insn-009ee084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee024`](#insn-009ee024) → [`009ee008`](#insn-009ee008) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee034`](#insn-009ee034) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`009ee064`](#insn-009ee064) → [`009ee070`](#insn-009ee070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee074`](#insn-009ee074) → [`0043bba4`](../0043b/0043bba4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bba4` · 推定シンボル `None` · 推定型 `None`
- [`009ee090`](#insn-009ee090) → [`009edb3c`](009edb3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009edb3c` · 推定シンボル `None` · 推定型 `None`
- [`009ee094`](#insn-009ee094) → [`009ee0d0`](#insn-009ee0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee09c`](#insn-009ee09c) → [`009ee0b0`](#insn-009ee0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0a8`](#insn-009ee0a8) → [`009ee0a0`](#insn-009ee0a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0ac`](#insn-009ee0ac) → [`009edfb0`](#insn-009edfb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0c0`](#insn-009ee0c0) → [`009ee0b0`](#insn-009ee0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0c4`](#insn-009ee0c4) → [`009edfb0`](#insn-009edfb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0cc`](#insn-009ee0cc) → [`009ee0d4`](#insn-009ee0d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0d4`](#insn-009ee0d4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0dc`](#insn-009ee0dc) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0e4`](#insn-009ee0e4) → [`009ee134`](#insn-009ee134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0e8`](#insn-009ee0e8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0ec`](#insn-009ee0ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0f0`](#insn-009ee0f0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0f4`](#insn-009ee0f4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0f8`](#insn-009ee0f8) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee0fc`](#insn-009ee0fc) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009ee134`](#insn-009ee134) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009edf00`](#insn-009edf00)

~~~json
{
  "source": "009edf00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf04`](#insn-009edf04)

~~~json
{
  "source": "009edf04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf08`](#insn-009edf08)

~~~json
{
  "source": "009edf08",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf0c`](#insn-009edf0c)

~~~json
{
  "source": "009edf0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf10`](#insn-009edf10)

~~~json
{
  "source": "009edf10",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf14`](#insn-009edf14)

~~~json
{
  "source": "009edf14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf34`](#insn-009edf34)

~~~json
{
  "source": "009edf34",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf40`](#insn-009edf40)

~~~json
{
  "source": "009edf40",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf48`](#insn-009edf48)

~~~json
{
  "source": "009edf48",
  "target": "Stack[-0x77]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf50`](#insn-009edf50)

~~~json
{
  "source": "009edf50",
  "target": "Stack[-0x7f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf5c`](#insn-009edf5c)

~~~json
{
  "source": "009edf5c",
  "target": "0044108c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009edf68`](#insn-009edf68)

~~~json
{
  "source": "009edf68",
  "target": "009edf80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf7c`](#insn-009edf7c)

~~~json
{
  "source": "009edf7c",
  "target": "009edf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf84`](#insn-009edf84)

~~~json
{
  "source": "009edf84",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf88`](#insn-009edf88)

~~~json
{
  "source": "009edf88",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf8c`](#insn-009edf8c)

~~~json
{
  "source": "009edf8c",
  "target": "009edf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf90`](#insn-009edf90)

~~~json
{
  "source": "009edf90",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edf94`](#insn-009edf94)

~~~json
{
  "source": "009edf94",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009edfa4`](#insn-009edfa4)

~~~json
{
  "source": "009edfa4",
  "target": "009ee0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edfac`](#insn-009edfac)

~~~json
{
  "source": "009edfac",
  "target": "009edfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edfb8`](#insn-009edfb8)

~~~json
{
  "source": "009edfb8",
  "target": "009ee0c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edfc8`](#insn-009edfc8)

~~~json
{
  "source": "009edfc8",
  "target": "00c58060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009edfd8`](#insn-009edfd8)

~~~json
{
  "source": "009edfd8",
  "target": "009ee0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edfe4`](#insn-009edfe4)

~~~json
{
  "source": "009edfe4",
  "target": "009ee0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edff4`](#insn-009edff4)

~~~json
{
  "source": "009edff4",
  "target": "009ee008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009edff8`](#insn-009edff8)

~~~json
{
  "source": "009edff8",
  "target": "009ee02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee004`](#insn-009ee004)

~~~json
{
  "source": "009ee004",
  "target": "009ee02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee014`](#insn-009ee014)

~~~json
{
  "source": "009ee014",
  "target": "009edffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee01c`](#insn-009ee01c)

~~~json
{
  "source": "009ee01c",
  "target": "009ee084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee024`](#insn-009ee024)

~~~json
{
  "source": "009ee024",
  "target": "009ee008",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee034`](#insn-009ee034)

~~~json
{
  "source": "009ee034",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ee064`](#insn-009ee064)

~~~json
{
  "source": "009ee064",
  "target": "009ee070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee074`](#insn-009ee074)

~~~json
{
  "source": "009ee074",
  "target": "0043bba4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ee090`](#insn-009ee090)

~~~json
{
  "source": "009ee090",
  "target": "009edb3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009ee094`](#insn-009ee094)

~~~json
{
  "source": "009ee094",
  "target": "009ee0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee09c`](#insn-009ee09c)

~~~json
{
  "source": "009ee09c",
  "target": "009ee0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0a8`](#insn-009ee0a8)

~~~json
{
  "source": "009ee0a8",
  "target": "009ee0a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0ac`](#insn-009ee0ac)

~~~json
{
  "source": "009ee0ac",
  "target": "009edfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0c0`](#insn-009ee0c0)

~~~json
{
  "source": "009ee0c0",
  "target": "009ee0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0c4`](#insn-009ee0c4)

~~~json
{
  "source": "009ee0c4",
  "target": "009edfb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0cc`](#insn-009ee0cc)

~~~json
{
  "source": "009ee0cc",
  "target": "009ee0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0d4`](#insn-009ee0d4)

~~~json
{
  "source": "009ee0d4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0dc`](#insn-009ee0dc)

~~~json
{
  "source": "009ee0dc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0e4`](#insn-009ee0e4)

~~~json
{
  "source": "009ee0e4",
  "target": "009ee134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0e8`](#insn-009ee0e8)

~~~json
{
  "source": "009ee0e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0ec`](#insn-009ee0ec)

~~~json
{
  "source": "009ee0ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0f0`](#insn-009ee0f0)

~~~json
{
  "source": "009ee0f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0f4`](#insn-009ee0f4)

~~~json
{
  "source": "009ee0f4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0f8`](#insn-009ee0f8)

~~~json
{
  "source": "009ee0f8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee0fc`](#insn-009ee0fc)

~~~json
{
  "source": "009ee0fc",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009ee134`](#insn-009ee134)

~~~json
{
  "source": "009ee134",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
