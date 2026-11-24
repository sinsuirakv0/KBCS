# 00bfdca0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfd878`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd878.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-7cddab659c7c13d86dbee737f7e5b936)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfdd3c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdd3c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-0162eee0da6513944a43de132579704e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfdca0",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5ad19d36ac03fc6dacd11d2b0f0d953df77c81c6465359db2821dd90fb4bca36",
  "source_text_sha256": "5ad19d36ac03fc6dacd11d2b0f0d953df77c81c6465359db2821dd90fb4bca36",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfdca0",
        "00bfde73"
      ]
    ],
    "bytes_sha256": "d6f581057d7e8aef78ea107f538e102ef8d0d25d32e74ce6876b0162c4fc7f01",
    "instruction_count": 117,
    "instruction_bytes": 468,
    "body_bytes": 468,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5e390](../00c5e/00c5e390.md)

## 呼び出し先

- [00c582a0](../00c58/00c582a0.md)
- [00c59dd0](../00c59/00c59dd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2043 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc
                 (long *param_1,undefined1 *param_2,long param_3,uint param_4)

{
  uint uVar1;
  long *plVar2;
  uint uVar3;
  long lVar4;
  undefined1 *puVar5;
  byte local_54 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_54,param_1,1);
  uVar3 = (uint)local_54[0];
  if (local_54[0] != 0) {
    while( true ) {
      plVar2 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      if ((byte *)plVar2[3] == (byte *)plVar2[4]) {
        uVar3 = (**(code **)(*plVar2 + 0x48))();
        if (uVar3 == 0xffffffff) {
          uVar3 = 2;
          goto joined_r0x00bfde0c;
        }
      }
      else {
        uVar3 = (uint)*(byte *)plVar2[3];
      }
      if ((uVar3 & 0xff) == (param_4 & 0xff)) {
        plVar2 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
        if (plVar2[3] == plVar2[4]) {
          (**(code **)(*plVar2 + 0x50))();
        }
        else {
          plVar2[3] = plVar2[3] + 1;
        }
        if (param_1[1] == 0x7fffffffffffffff) {
          uVar3 = 0;
        }
        else {
          uVar3 = 0;
          param_1[1] = param_1[1] + 1;
        }
        goto joined_r0x00bfde0c;
      }
      if (param_3 + -1 <= param_1[1]) break;
      lVar4 = *param_1;
      puVar5 = param_2 + 1;
      *param_2 = (char)uVar3;
      plVar2 = *(long **)((long)param_1 + *(long *)(lVar4 + -0x18) + 0x28);
      if (plVar2[3] == plVar2[4]) {
        (**(code **)(*plVar2 + 0x50))();
      }
      else {
        plVar2[3] = plVar2[3] + 1;
      }
      param_2 = puVar5;
      if (param_1[1] != 0x7fffffffffffffff) {
        param_1[1] = param_1[1] + 1;
      }
    }
    uVar3 = 4;
  }
joined_r0x00bfde0c:
  if (0 < param_3) {
    *param_2 = 0;
  }
  lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
  uVar1 = uVar3 | 4;
  if (param_1[1] != 0) {
    uVar1 = uVar3;
  }
  _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | uVar1);
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfdca0"></a> `00bfdca0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfdca4"></a> `00bfdca4` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfdca8"></a> `00bfdca8` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfdcac"></a> `00bfdcac` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdcb0"></a> `00bfdcb0` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdcb4"></a> `00bfdcb4` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfdcb8"></a> `00bfdcb8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfdcbc"></a> `00bfdcbc` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfdcc0"></a> `00bfdcc0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfdcc4"></a> `00bfdcc4` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bfdcc8"></a> `00bfdcc8` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bfdccc"></a> `00bfdccc` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdcd0"></a> `00bfdcd0` | `a0 13 00 d1` | sub x0,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfdcd4"></a> `00bfdcd4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfdcd8"></a> `00bfdcd8` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdcdc"></a> `00bfdcdc` | `f6 03 03 2a` | mov w22,w3 | `FALL_THROUGH`
<a id="insn-00bfdce0"></a> `00bfdce0` | `3c 70 01 94` | bl 0x00c59dd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdce4"></a> `00bfdce4` | `a8 c3 5f 38` | ldurb w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfdce8"></a> `00bfdce8` | `c8 09 00 34` | cbz w8,0x00bfde20 | `CONDITIONAL_JUMP`
<a id="insn-00bfdcec"></a> `00bfdcec` | `d6 1e 00 12` | and w22,w22,#0xff | `FALL_THROUGH`
<a id="insn-00bfdcf0"></a> `00bfdcf0` | `77 a2 00 91` | add x23,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfdcf4"></a> `00bfdcf4` | `98 06 00 d1` | sub x24,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdcf8"></a> `00bfdcf8` | `19 00 f0 92` | mov x25,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfdcfc"></a> `00bfdcfc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfdd00"></a> `00bfdd00` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdd04"></a> `00bfdd04` | `e0 6a 68 f8` | ldr x0,[x23, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfdd08"></a> `00bfdd08` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdd0c"></a> `00bfdd0c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfdd10"></a> `00bfdd10` | `60 00 00 54` | b.eq 0x00bfdd1c | `CONDITIONAL_JUMP`
<a id="insn-00bfdd14"></a> `00bfdd14` | `00 01 40 39` | ldrb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfdd18"></a> `00bfdd18` | `06 00 00 14` | b 0x00bfdd30 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdd1c"></a> `00bfdd1c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfdd20"></a> `00bfdd20` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfdd24"></a> `00bfdd24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfdd28"></a> `00bfdd28` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdd2c"></a> `00bfdd2c` | `60 05 00 54` | b.eq 0x00bfddd8 | `CONDITIONAL_JUMP`
<a id="insn-00bfdd30"></a> `00bfdd30` | `08 1c 00 12` | and w8,w0,#0xff | `FALL_THROUGH`
<a id="insn-00bfdd34"></a> `00bfdd34` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00bfdd38"></a> `00bfdd38` | `40 03 00 54` | b.eq 0x00bfdda0 | `CONDITIONAL_JUMP`
<a id="insn-00bfdd3c"></a> `00bfdd3c` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdd40"></a> `00bfdd40` | `3f 01 18 eb` | cmp x9,x24 | `FALL_THROUGH`
<a id="insn-00bfdd44"></a> `00bfdd44` | `2a 04 00 54` | b.ge 0x00bfddc8 | `CONDITIONAL_JUMP`
<a id="insn-00bfdd48"></a> `00bfdd48` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-00bfdd4c"></a> `00bfdd4c` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bfdd50"></a> `00bfdd50` | `48 17 00 38` | strb w8,[x26], #0x1 | `FALL_THROUGH`
<a id="insn-00bfdd54"></a> `00bfdd54` | `28 81 5e f8` | ldur x8,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdd58"></a> `00bfdd58` | `e0 6a 68 f8` | ldr x0,[x23, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfdd5c"></a> `00bfdd5c` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdd60"></a> `00bfdd60` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfdd64"></a> `00bfdd64` | `80 00 00 54` | b.eq 0x00bfdd74 | `CONDITIONAL_JUMP`
<a id="insn-00bfdd68"></a> `00bfdd68` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdd6c"></a> `00bfdd6c` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdd70"></a> `00bfdd70` | `04 00 00 14` | b 0x00bfdd80 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdd74"></a> `00bfdd74` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfdd78"></a> `00bfdd78` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfdd7c"></a> `00bfdd7c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfdd80"></a> `00bfdd80` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdd84"></a> `00bfdd84` | `f5 03 1a aa` | mov x21,x26 | `FALL_THROUGH`
<a id="insn-00bfdd88"></a> `00bfdd88` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00bfdd8c"></a> `00bfdd8c` | `80 fb ff 54` | b.eq 0x00bfdcfc | `CONDITIONAL_JUMP`
<a id="insn-00bfdd90"></a> `00bfdd90` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdd94"></a> `00bfdd94` | `f5 03 1a aa` | mov x21,x26 | `FALL_THROUGH`
<a id="insn-00bfdd98"></a> `00bfdd98` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdd9c"></a> `00bfdd9c` | `d8 ff ff 17` | b 0x00bfdcfc | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdda0"></a> `00bfdda0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfdda4"></a> `00bfdda4` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdda8"></a> `00bfdda8` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfddac"></a> `00bfddac` | `00 15 40 f9` | ldr x0,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bfddb0"></a> `00bfddb0` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfddb4"></a> `00bfddb4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfddb8"></a> `00bfddb8` | `80 01 00 54` | b.eq 0x00bfdde8 | `CONDITIONAL_JUMP`
<a id="insn-00bfddbc"></a> `00bfddbc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfddc0"></a> `00bfddc0` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfddc4"></a> `00bfddc4` | `0c 00 00 14` | b 0x00bfddf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfddc8"></a> `00bfddc8` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfddcc"></a> `00bfddcc` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfddd0"></a> `00bfddd0` | `ca 02 00 54` | b.ge 0x00bfde28 | `CONDITIONAL_JUMP`
<a id="insn-00bfddd4"></a> `00bfddd4` | `16 00 00 14` | b 0x00bfde2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfddd8"></a> `00bfddd8` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bfdddc"></a> `00bfdddc` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdde0"></a> `00bfdde0` | `4a 02 00 54` | b.ge 0x00bfde28 | `CONDITIONAL_JUMP`
<a id="insn-00bfdde4"></a> `00bfdde4` | `12 00 00 14` | b 0x00bfde2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdde8"></a> `00bfdde8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfddec"></a> `00bfddec` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfddf0"></a> `00bfddf0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfddf4"></a> `00bfddf4` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfddf8"></a> `00bfddf8` | `08 00 f0 92` | mov x8,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfddfc"></a> `00bfddfc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfde00"></a> `00bfde00` | `a1 00 00 54` | b.ne 0x00bfde14 | `CONDITIONAL_JUMP`
<a id="insn-00bfde04"></a> `00bfde04` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfde08"></a> `00bfde08` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfde0c"></a> `00bfde0c` | `ea 00 00 54` | b.ge 0x00bfde28 | `CONDITIONAL_JUMP`
<a id="insn-00bfde10"></a> `00bfde10` | `07 00 00 14` | b 0x00bfde2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfde14"></a> `00bfde14` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfde18"></a> `00bfde18` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfde1c"></a> `00bfde1c` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfde20"></a> `00bfde20` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfde24"></a> `00bfde24` | `4b 00 00 54` | b.lt 0x00bfde2c | `CONDITIONAL_JUMP`
<a id="insn-00bfde28"></a> `00bfde28` | `bf 02 00 39` | strb wzr,[x21] | `FALL_THROUGH`
<a id="insn-00bfde2c"></a> `00bfde2c` | `69 2a 40 a9` | ldp x9,x10,[x19] | `FALL_THROUGH`
<a id="insn-00bfde30"></a> `00bfde30` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfde34"></a> `00bfde34` | `5f 01 00 f1` | cmp x10,#0x0 | `FALL_THROUGH`
<a id="insn-00bfde38"></a> `00bfde38` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfde3c"></a> `00bfde3c` | `09 01 1e 32` | orr w9,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfde40"></a> `00bfde40` | `0a 20 40 b9` | ldr w10,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfde44"></a> `00bfde44` | `28 01 88 1a` | csel w8,w9,w8,eq | `FALL_THROUGH`
<a id="insn-00bfde48"></a> `00bfde48` | `41 01 08 2a` | orr w1,w10,w8 | `FALL_THROUGH`
<a id="insn-00bfde4c"></a> `00bfde4c` | `15 69 01 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfde50"></a> `00bfde50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfde54"></a> `00bfde54` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfde58"></a> `00bfde58` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfde5c"></a> `00bfde5c` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfde60"></a> `00bfde60` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfde64"></a> `00bfde64` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfde68"></a> `00bfde68` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfde6c"></a> `00bfde6c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfde70"></a> `00bfde70` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfdca0`](#insn-00bfdca0) 範囲 `[['00bfdca0', '00bfdceb']]`
  - `CONDITIONAL_JUMP` [`00bfdce8`](#insn-00bfdce8) → [`00bfde20`](#insn-00bfde20)
  - `FALL_THROUGH` [`00bfdce8`](#insn-00bfdce8) → [`00bfdcec`](#insn-00bfdcec)
- ブロック [`00bfdcec`](#insn-00bfdcec) 範囲 `[['00bfdcec', '00bfdcfb']]`
  - `FALL_THROUGH` [`00bfdcf8`](#insn-00bfdcf8) → [`00bfdcfc`](#insn-00bfdcfc)
- ブロック [`00bfdcfc`](#insn-00bfdcfc) 範囲 `[['00bfdcfc', '00bfdd13']]`
  - `CONDITIONAL_JUMP` [`00bfdd10`](#insn-00bfdd10) → [`00bfdd1c`](#insn-00bfdd1c)
  - `FALL_THROUGH` [`00bfdd10`](#insn-00bfdd10) → [`00bfdd14`](#insn-00bfdd14)
- ブロック [`00bfdd14`](#insn-00bfdd14) 範囲 `[['00bfdd14', '00bfdd1b']]`
  - `UNCONDITIONAL_JUMP` [`00bfdd18`](#insn-00bfdd18) → [`00bfdd30`](#insn-00bfdd30)
- ブロック [`00bfdd1c`](#insn-00bfdd1c) 範囲 `[['00bfdd1c', '00bfdd2f']]`
  - `CONDITIONAL_JUMP` [`00bfdd2c`](#insn-00bfdd2c) → [`00bfddd8`](#insn-00bfddd8)
  - `FALL_THROUGH` [`00bfdd2c`](#insn-00bfdd2c) → [`00bfdd30`](#insn-00bfdd30)
- ブロック [`00bfdd30`](#insn-00bfdd30) 範囲 `[['00bfdd30', '00bfdd3b']]`
  - `CONDITIONAL_JUMP` [`00bfdd38`](#insn-00bfdd38) → [`00bfdda0`](#insn-00bfdda0)
  - `FALL_THROUGH` [`00bfdd38`](#insn-00bfdd38) → [`00bfdd3c`](#insn-00bfdd3c)
- ブロック [`00bfdd3c`](#insn-00bfdd3c) 範囲 `[['00bfdd3c', '00bfdd47']]`
  - `CONDITIONAL_JUMP` [`00bfdd44`](#insn-00bfdd44) → [`00bfddc8`](#insn-00bfddc8)
  - `FALL_THROUGH` [`00bfdd44`](#insn-00bfdd44) → [`00bfdd48`](#insn-00bfdd48)
- ブロック [`00bfdd48`](#insn-00bfdd48) 範囲 `[['00bfdd48', '00bfdd67']]`
  - `CONDITIONAL_JUMP` [`00bfdd64`](#insn-00bfdd64) → [`00bfdd74`](#insn-00bfdd74)
  - `FALL_THROUGH` [`00bfdd64`](#insn-00bfdd64) → [`00bfdd68`](#insn-00bfdd68)
- ブロック [`00bfdd68`](#insn-00bfdd68) 範囲 `[['00bfdd68', '00bfdd73']]`
  - `UNCONDITIONAL_JUMP` [`00bfdd70`](#insn-00bfdd70) → [`00bfdd80`](#insn-00bfdd80)
- ブロック [`00bfdd74`](#insn-00bfdd74) 範囲 `[['00bfdd74', '00bfdd7f']]`
  - `FALL_THROUGH` [`00bfdd7c`](#insn-00bfdd7c) → [`00bfdd80`](#insn-00bfdd80)
- ブロック [`00bfdd80`](#insn-00bfdd80) 範囲 `[['00bfdd80', '00bfdd8f']]`
  - `CONDITIONAL_JUMP` [`00bfdd8c`](#insn-00bfdd8c) → [`00bfdcfc`](#insn-00bfdcfc)
  - `FALL_THROUGH` [`00bfdd8c`](#insn-00bfdd8c) → [`00bfdd90`](#insn-00bfdd90)
- ブロック [`00bfdd90`](#insn-00bfdd90) 範囲 `[['00bfdd90', '00bfdd9f']]`
  - `UNCONDITIONAL_JUMP` [`00bfdd9c`](#insn-00bfdd9c) → [`00bfdcfc`](#insn-00bfdcfc)
- ブロック [`00bfdda0`](#insn-00bfdda0) 範囲 `[['00bfdda0', '00bfddbb']]`
  - `CONDITIONAL_JUMP` [`00bfddb8`](#insn-00bfddb8) → [`00bfdde8`](#insn-00bfdde8)
  - `FALL_THROUGH` [`00bfddb8`](#insn-00bfddb8) → [`00bfddbc`](#insn-00bfddbc)
- ブロック [`00bfddbc`](#insn-00bfddbc) 範囲 `[['00bfddbc', '00bfddc7']]`
  - `UNCONDITIONAL_JUMP` [`00bfddc4`](#insn-00bfddc4) → [`00bfddf4`](#insn-00bfddf4)
- ブロック [`00bfddc8`](#insn-00bfddc8) 範囲 `[['00bfddc8', '00bfddd3']]`
  - `CONDITIONAL_JUMP` [`00bfddd0`](#insn-00bfddd0) → [`00bfde28`](#insn-00bfde28)
  - `FALL_THROUGH` [`00bfddd0`](#insn-00bfddd0) → [`00bfddd4`](#insn-00bfddd4)
- ブロック [`00bfddd4`](#insn-00bfddd4) 範囲 `[['00bfddd4', '00bfddd7']]`
  - `UNCONDITIONAL_JUMP` [`00bfddd4`](#insn-00bfddd4) → [`00bfde2c`](#insn-00bfde2c)
- ブロック [`00bfddd8`](#insn-00bfddd8) 範囲 `[['00bfddd8', '00bfdde3']]`
  - `CONDITIONAL_JUMP` [`00bfdde0`](#insn-00bfdde0) → [`00bfde28`](#insn-00bfde28)
  - `FALL_THROUGH` [`00bfdde0`](#insn-00bfdde0) → [`00bfdde4`](#insn-00bfdde4)
- ブロック [`00bfdde4`](#insn-00bfdde4) 範囲 `[['00bfdde4', '00bfdde7']]`
  - `UNCONDITIONAL_JUMP` [`00bfdde4`](#insn-00bfdde4) → [`00bfde2c`](#insn-00bfde2c)
- ブロック [`00bfdde8`](#insn-00bfdde8) 範囲 `[['00bfdde8', '00bfddf3']]`
  - `FALL_THROUGH` [`00bfddf0`](#insn-00bfddf0) → [`00bfddf4`](#insn-00bfddf4)
- ブロック [`00bfddf4`](#insn-00bfddf4) 範囲 `[['00bfddf4', '00bfde03']]`
  - `CONDITIONAL_JUMP` [`00bfde00`](#insn-00bfde00) → [`00bfde14`](#insn-00bfde14)
  - `FALL_THROUGH` [`00bfde00`](#insn-00bfde00) → [`00bfde04`](#insn-00bfde04)
- ブロック [`00bfde04`](#insn-00bfde04) 範囲 `[['00bfde04', '00bfde0f']]`
  - `CONDITIONAL_JUMP` [`00bfde0c`](#insn-00bfde0c) → [`00bfde28`](#insn-00bfde28)
  - `FALL_THROUGH` [`00bfde0c`](#insn-00bfde0c) → [`00bfde10`](#insn-00bfde10)
- ブロック [`00bfde10`](#insn-00bfde10) 範囲 `[['00bfde10', '00bfde13']]`
  - `UNCONDITIONAL_JUMP` [`00bfde10`](#insn-00bfde10) → [`00bfde2c`](#insn-00bfde2c)
- ブロック [`00bfde14`](#insn-00bfde14) 範囲 `[['00bfde14', '00bfde1f']]`
  - `FALL_THROUGH` [`00bfde1c`](#insn-00bfde1c) → [`00bfde20`](#insn-00bfde20)
- ブロック [`00bfde20`](#insn-00bfde20) 範囲 `[['00bfde20', '00bfde27']]`
  - `CONDITIONAL_JUMP` [`00bfde24`](#insn-00bfde24) → [`00bfde2c`](#insn-00bfde2c)
  - `FALL_THROUGH` [`00bfde24`](#insn-00bfde24) → [`00bfde28`](#insn-00bfde28)
- ブロック [`00bfde28`](#insn-00bfde28) 範囲 `[['00bfde28', '00bfde2b']]`
  - `FALL_THROUGH` [`00bfde28`](#insn-00bfde28) → [`00bfde2c`](#insn-00bfde2c)
- ブロック [`00bfde2c`](#insn-00bfde2c) 範囲 `[['00bfde2c', '00bfde73']]`

## 命令位置別の参照

- [`00bfdca8`](#insn-00bfdca8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdcac`](#insn-00bfdcac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdcb0`](#insn-00bfdcb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdcb4`](#insn-00bfdcb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdcb8`](#insn-00bfdcb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdce0`](#insn-00bfdce0) → [`00c59dd0`](../00c59/00c59dd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59dd0` · 推定シンボル `None` · 推定型 `None`
- [`00bfdce4`](#insn-00bfdce4) → `Stack[-0x54]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdce8`](#insn-00bfdce8) → [`00bfde20`](#insn-00bfde20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd10`](#insn-00bfdd10) → [`00bfdd1c`](#insn-00bfdd1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd18`](#insn-00bfdd18) → [`00bfdd30`](#insn-00bfdd30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd2c`](#insn-00bfdd2c) → [`00bfddd8`](#insn-00bfddd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd38`](#insn-00bfdd38) → [`00bfdda0`](#insn-00bfdda0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd44`](#insn-00bfdd44) → [`00bfddc8`](#insn-00bfddc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd64`](#insn-00bfdd64) → [`00bfdd74`](#insn-00bfdd74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd70`](#insn-00bfdd70) → [`00bfdd80`](#insn-00bfdd80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd8c`](#insn-00bfdd8c) → [`00bfdcfc`](#insn-00bfdcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd9c`](#insn-00bfdd9c) → [`00bfdcfc`](#insn-00bfdcfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfddb8`](#insn-00bfddb8) → [`00bfdde8`](#insn-00bfdde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfddc4`](#insn-00bfddc4) → [`00bfddf4`](#insn-00bfddf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfddd0`](#insn-00bfddd0) → [`00bfde28`](#insn-00bfde28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfddd4`](#insn-00bfddd4) → [`00bfde2c`](#insn-00bfde2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdde0`](#insn-00bfdde0) → [`00bfde28`](#insn-00bfde28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdde4`](#insn-00bfdde4) → [`00bfde2c`](#insn-00bfde2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde00`](#insn-00bfde00) → [`00bfde14`](#insn-00bfde14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde0c`](#insn-00bfde0c) → [`00bfde28`](#insn-00bfde28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde10`](#insn-00bfde10) → [`00bfde2c`](#insn-00bfde2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde24`](#insn-00bfde24) → [`00bfde2c`](#insn-00bfde2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde4c`](#insn-00bfde4c) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00bfde54`](#insn-00bfde54) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde58`](#insn-00bfde58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde5c`](#insn-00bfde5c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde60`](#insn-00bfde60) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde64`](#insn-00bfde64) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfdca8`](#insn-00bfdca8)

~~~json
{
  "source": "00bfdca8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdcac`](#insn-00bfdcac)

~~~json
{
  "source": "00bfdcac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdcb0`](#insn-00bfdcb0)

~~~json
{
  "source": "00bfdcb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdcb4`](#insn-00bfdcb4)

~~~json
{
  "source": "00bfdcb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdcb8`](#insn-00bfdcb8)

~~~json
{
  "source": "00bfdcb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdce0`](#insn-00bfdce0)

~~~json
{
  "source": "00bfdce0",
  "target": "00c59dd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdce4`](#insn-00bfdce4)

~~~json
{
  "source": "00bfdce4",
  "target": "Stack[-0x54]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdce8`](#insn-00bfdce8)

~~~json
{
  "source": "00bfdce8",
  "target": "00bfde20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd10`](#insn-00bfdd10)

~~~json
{
  "source": "00bfdd10",
  "target": "00bfdd1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd18`](#insn-00bfdd18)

~~~json
{
  "source": "00bfdd18",
  "target": "00bfdd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd2c`](#insn-00bfdd2c)

~~~json
{
  "source": "00bfdd2c",
  "target": "00bfddd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd38`](#insn-00bfdd38)

~~~json
{
  "source": "00bfdd38",
  "target": "00bfdda0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd44`](#insn-00bfdd44)

~~~json
{
  "source": "00bfdd44",
  "target": "00bfddc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd64`](#insn-00bfdd64)

~~~json
{
  "source": "00bfdd64",
  "target": "00bfdd74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd70`](#insn-00bfdd70)

~~~json
{
  "source": "00bfdd70",
  "target": "00bfdd80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd8c`](#insn-00bfdd8c)

~~~json
{
  "source": "00bfdd8c",
  "target": "00bfdcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd9c`](#insn-00bfdd9c)

~~~json
{
  "source": "00bfdd9c",
  "target": "00bfdcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfddb8`](#insn-00bfddb8)

~~~json
{
  "source": "00bfddb8",
  "target": "00bfdde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfddc4`](#insn-00bfddc4)

~~~json
{
  "source": "00bfddc4",
  "target": "00bfddf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfddd0`](#insn-00bfddd0)

~~~json
{
  "source": "00bfddd0",
  "target": "00bfde28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfddd4`](#insn-00bfddd4)

~~~json
{
  "source": "00bfddd4",
  "target": "00bfde2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdde0`](#insn-00bfdde0)

~~~json
{
  "source": "00bfdde0",
  "target": "00bfde28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdde4`](#insn-00bfdde4)

~~~json
{
  "source": "00bfdde4",
  "target": "00bfde2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde00`](#insn-00bfde00)

~~~json
{
  "source": "00bfde00",
  "target": "00bfde14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde0c`](#insn-00bfde0c)

~~~json
{
  "source": "00bfde0c",
  "target": "00bfde28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde10`](#insn-00bfde10)

~~~json
{
  "source": "00bfde10",
  "target": "00bfde2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde24`](#insn-00bfde24)

~~~json
{
  "source": "00bfde24",
  "target": "00bfde2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde4c`](#insn-00bfde4c)

~~~json
{
  "source": "00bfde4c",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfde54`](#insn-00bfde54)

~~~json
{
  "source": "00bfde54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde58`](#insn-00bfde58)

~~~json
{
  "source": "00bfde58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde5c`](#insn-00bfde5c)

~~~json
{
  "source": "00bfde5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde60`](#insn-00bfde60)

~~~json
{
  "source": "00bfde60",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde64`](#insn-00bfde64)

~~~json
{
  "source": "00bfde64",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
