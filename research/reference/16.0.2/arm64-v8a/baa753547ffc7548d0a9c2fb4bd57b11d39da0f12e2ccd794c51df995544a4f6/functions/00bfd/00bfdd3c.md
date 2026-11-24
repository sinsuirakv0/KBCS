# 00bfdd3c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfdca0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfdca0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-0162eee0da6513944a43de132579704e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfed30`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfe/00bfed30.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-bf0d26b4f0776e547803ad8439c34551)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfdd3c",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE7getlineEPclc",
  "size": 468,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "464be215ec48d6ccddf2f177ff6b7cf28733e1b80b3a4beea365c57d0c762f7e",
  "source_text_sha256": "464be215ec48d6ccddf2f177ff6b7cf28733e1b80b3a4beea365c57d0c762f7e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfdd3c",
        "00bfdf0f"
      ]
    ],
    "bytes_sha256": "0b10030ebcf05d9b0d539ef126a20f931ef026c8b70a6e5724f87116c3b9cf1d",
    "instruction_count": 117,
    "instruction_bytes": 468,
    "body_bytes": 468,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5e460](../00c5e/00c5e460.md)

## 呼び出し先

- [00c58370](../00c58/00c58370.md)
- [00c59ea0](../00c59/00c59ea0.md)

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
          goto joined_r0x00bfdea8;
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
        goto joined_r0x00bfdea8;
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
joined_r0x00bfdea8:
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
<a id="insn-00bfdd3c"></a> `00bfdd3c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfdd40"></a> `00bfdd40` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfdd44"></a> `00bfdd44` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfdd48"></a> `00bfdd48` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdd4c"></a> `00bfdd4c` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdd50"></a> `00bfdd50` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfdd54"></a> `00bfdd54` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfdd58"></a> `00bfdd58` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfdd5c"></a> `00bfdd5c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfdd60"></a> `00bfdd60` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bfdd64"></a> `00bfdd64` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bfdd68"></a> `00bfdd68` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdd6c"></a> `00bfdd6c` | `a0 13 00 d1` | sub x0,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfdd70"></a> `00bfdd70` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfdd74"></a> `00bfdd74` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdd78"></a> `00bfdd78` | `f6 03 03 2a` | mov w22,w3 | `FALL_THROUGH`
<a id="insn-00bfdd7c"></a> `00bfdd7c` | `49 70 01 94` | bl 0x00c59ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdd80"></a> `00bfdd80` | `a8 c3 5f 38` | ldurb w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfdd84"></a> `00bfdd84` | `c8 09 00 34` | cbz w8,0x00bfdebc | `CONDITIONAL_JUMP`
<a id="insn-00bfdd88"></a> `00bfdd88` | `d6 1e 00 12` | and w22,w22,#0xff | `FALL_THROUGH`
<a id="insn-00bfdd8c"></a> `00bfdd8c` | `77 a2 00 91` | add x23,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfdd90"></a> `00bfdd90` | `98 06 00 d1` | sub x24,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdd94"></a> `00bfdd94` | `19 00 f0 92` | mov x25,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfdd98"></a> `00bfdd98` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfdd9c"></a> `00bfdd9c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdda0"></a> `00bfdda0` | `e0 6a 68 f8` | ldr x0,[x23, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfdda4"></a> `00bfdda4` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdda8"></a> `00bfdda8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfddac"></a> `00bfddac` | `60 00 00 54` | b.eq 0x00bfddb8 | `CONDITIONAL_JUMP`
<a id="insn-00bfddb0"></a> `00bfddb0` | `00 01 40 39` | ldrb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfddb4"></a> `00bfddb4` | `06 00 00 14` | b 0x00bfddcc | `UNCONDITIONAL_JUMP`
<a id="insn-00bfddb8"></a> `00bfddb8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfddbc"></a> `00bfddbc` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfddc0"></a> `00bfddc0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfddc4"></a> `00bfddc4` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfddc8"></a> `00bfddc8` | `60 05 00 54` | b.eq 0x00bfde74 | `CONDITIONAL_JUMP`
<a id="insn-00bfddcc"></a> `00bfddcc` | `08 1c 00 12` | and w8,w0,#0xff | `FALL_THROUGH`
<a id="insn-00bfddd0"></a> `00bfddd0` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00bfddd4"></a> `00bfddd4` | `40 03 00 54` | b.eq 0x00bfde3c | `CONDITIONAL_JUMP`
<a id="insn-00bfddd8"></a> `00bfddd8` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdddc"></a> `00bfdddc` | `3f 01 18 eb` | cmp x9,x24 | `FALL_THROUGH`
<a id="insn-00bfdde0"></a> `00bfdde0` | `2a 04 00 54` | b.ge 0x00bfde64 | `CONDITIONAL_JUMP`
<a id="insn-00bfdde4"></a> `00bfdde4` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-00bfdde8"></a> `00bfdde8` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bfddec"></a> `00bfddec` | `48 17 00 38` | strb w8,[x26], #0x1 | `FALL_THROUGH`
<a id="insn-00bfddf0"></a> `00bfddf0` | `28 81 5e f8` | ldur x8,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfddf4"></a> `00bfddf4` | `e0 6a 68 f8` | ldr x0,[x23, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfddf8"></a> `00bfddf8` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfddfc"></a> `00bfddfc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfde00"></a> `00bfde00` | `80 00 00 54` | b.eq 0x00bfde10 | `CONDITIONAL_JUMP`
<a id="insn-00bfde04"></a> `00bfde04` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfde08"></a> `00bfde08` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfde0c"></a> `00bfde0c` | `04 00 00 14` | b 0x00bfde1c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfde10"></a> `00bfde10` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfde14"></a> `00bfde14` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfde18"></a> `00bfde18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfde1c"></a> `00bfde1c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfde20"></a> `00bfde20` | `f5 03 1a aa` | mov x21,x26 | `FALL_THROUGH`
<a id="insn-00bfde24"></a> `00bfde24` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00bfde28"></a> `00bfde28` | `80 fb ff 54` | b.eq 0x00bfdd98 | `CONDITIONAL_JUMP`
<a id="insn-00bfde2c"></a> `00bfde2c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfde30"></a> `00bfde30` | `f5 03 1a aa` | mov x21,x26 | `FALL_THROUGH`
<a id="insn-00bfde34"></a> `00bfde34` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfde38"></a> `00bfde38` | `d8 ff ff 17` | b 0x00bfdd98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfde3c"></a> `00bfde3c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfde40"></a> `00bfde40` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfde44"></a> `00bfde44` | `68 02 08 8b` | add x8,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfde48"></a> `00bfde48` | `00 15 40 f9` | ldr x0,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bfde4c"></a> `00bfde4c` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfde50"></a> `00bfde50` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfde54"></a> `00bfde54` | `80 01 00 54` | b.eq 0x00bfde84 | `CONDITIONAL_JUMP`
<a id="insn-00bfde58"></a> `00bfde58` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfde5c"></a> `00bfde5c` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfde60"></a> `00bfde60` | `0c 00 00 14` | b 0x00bfde90 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfde64"></a> `00bfde64` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfde68"></a> `00bfde68` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfde6c"></a> `00bfde6c` | `ca 02 00 54` | b.ge 0x00bfdec4 | `CONDITIONAL_JUMP`
<a id="insn-00bfde70"></a> `00bfde70` | `16 00 00 14` | b 0x00bfdec8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfde74"></a> `00bfde74` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bfde78"></a> `00bfde78` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfde7c"></a> `00bfde7c` | `4a 02 00 54` | b.ge 0x00bfdec4 | `CONDITIONAL_JUMP`
<a id="insn-00bfde80"></a> `00bfde80` | `12 00 00 14` | b 0x00bfdec8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfde84"></a> `00bfde84` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfde88"></a> `00bfde88` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfde8c"></a> `00bfde8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfde90"></a> `00bfde90` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfde94"></a> `00bfde94` | `08 00 f0 92` | mov x8,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfde98"></a> `00bfde98` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfde9c"></a> `00bfde9c` | `a1 00 00 54` | b.ne 0x00bfdeb0 | `CONDITIONAL_JUMP`
<a id="insn-00bfdea0"></a> `00bfdea0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfdea4"></a> `00bfdea4` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdea8"></a> `00bfdea8` | `ea 00 00 54` | b.ge 0x00bfdec4 | `CONDITIONAL_JUMP`
<a id="insn-00bfdeac"></a> `00bfdeac` | `07 00 00 14` | b 0x00bfdec8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdeb0"></a> `00bfdeb0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfdeb4"></a> `00bfdeb4` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdeb8"></a> `00bfdeb8` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdebc"></a> `00bfdebc` | `9f 06 00 f1` | cmp x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdec0"></a> `00bfdec0` | `4b 00 00 54` | b.lt 0x00bfdec8 | `CONDITIONAL_JUMP`
<a id="insn-00bfdec4"></a> `00bfdec4` | `bf 02 00 39` | strb wzr,[x21] | `FALL_THROUGH`
<a id="insn-00bfdec8"></a> `00bfdec8` | `69 2a 40 a9` | ldp x9,x10,[x19] | `FALL_THROUGH`
<a id="insn-00bfdecc"></a> `00bfdecc` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfded0"></a> `00bfded0` | `5f 01 00 f1` | cmp x10,#0x0 | `FALL_THROUGH`
<a id="insn-00bfded4"></a> `00bfded4` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfded8"></a> `00bfded8` | `09 01 1e 32` | orr w9,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfdedc"></a> `00bfdedc` | `0a 20 40 b9` | ldr w10,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdee0"></a> `00bfdee0` | `28 01 88 1a` | csel w8,w9,w8,eq | `FALL_THROUGH`
<a id="insn-00bfdee4"></a> `00bfdee4` | `41 01 08 2a` | orr w1,w10,w8 | `FALL_THROUGH`
<a id="insn-00bfdee8"></a> `00bfdee8` | `22 69 01 94` | bl 0x00c58370 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdeec"></a> `00bfdeec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfdef0"></a> `00bfdef0` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfdef4"></a> `00bfdef4` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfdef8"></a> `00bfdef8` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdefc"></a> `00bfdefc` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdf00"></a> `00bfdf00` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfdf04"></a> `00bfdf04` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfdf08"></a> `00bfdf08` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfdf0c"></a> `00bfdf0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfdd3c`](#insn-00bfdd3c) 範囲 `[['00bfdd3c', '00bfdd87']]`
  - `CONDITIONAL_JUMP` [`00bfdd84`](#insn-00bfdd84) → [`00bfdebc`](#insn-00bfdebc)
  - `FALL_THROUGH` [`00bfdd84`](#insn-00bfdd84) → [`00bfdd88`](#insn-00bfdd88)
- ブロック [`00bfdd88`](#insn-00bfdd88) 範囲 `[['00bfdd88', '00bfdd97']]`
  - `FALL_THROUGH` [`00bfdd94`](#insn-00bfdd94) → [`00bfdd98`](#insn-00bfdd98)
- ブロック [`00bfdd98`](#insn-00bfdd98) 範囲 `[['00bfdd98', '00bfddaf']]`
  - `CONDITIONAL_JUMP` [`00bfddac`](#insn-00bfddac) → [`00bfddb8`](#insn-00bfddb8)
  - `FALL_THROUGH` [`00bfddac`](#insn-00bfddac) → [`00bfddb0`](#insn-00bfddb0)
- ブロック [`00bfddb0`](#insn-00bfddb0) 範囲 `[['00bfddb0', '00bfddb7']]`
  - `UNCONDITIONAL_JUMP` [`00bfddb4`](#insn-00bfddb4) → [`00bfddcc`](#insn-00bfddcc)
- ブロック [`00bfddb8`](#insn-00bfddb8) 範囲 `[['00bfddb8', '00bfddcb']]`
  - `CONDITIONAL_JUMP` [`00bfddc8`](#insn-00bfddc8) → [`00bfde74`](#insn-00bfde74)
  - `FALL_THROUGH` [`00bfddc8`](#insn-00bfddc8) → [`00bfddcc`](#insn-00bfddcc)
- ブロック [`00bfddcc`](#insn-00bfddcc) 範囲 `[['00bfddcc', '00bfddd7']]`
  - `CONDITIONAL_JUMP` [`00bfddd4`](#insn-00bfddd4) → [`00bfde3c`](#insn-00bfde3c)
  - `FALL_THROUGH` [`00bfddd4`](#insn-00bfddd4) → [`00bfddd8`](#insn-00bfddd8)
- ブロック [`00bfddd8`](#insn-00bfddd8) 範囲 `[['00bfddd8', '00bfdde3']]`
  - `CONDITIONAL_JUMP` [`00bfdde0`](#insn-00bfdde0) → [`00bfde64`](#insn-00bfde64)
  - `FALL_THROUGH` [`00bfdde0`](#insn-00bfdde0) → [`00bfdde4`](#insn-00bfdde4)
- ブロック [`00bfdde4`](#insn-00bfdde4) 範囲 `[['00bfdde4', '00bfde03']]`
  - `CONDITIONAL_JUMP` [`00bfde00`](#insn-00bfde00) → [`00bfde10`](#insn-00bfde10)
  - `FALL_THROUGH` [`00bfde00`](#insn-00bfde00) → [`00bfde04`](#insn-00bfde04)
- ブロック [`00bfde04`](#insn-00bfde04) 範囲 `[['00bfde04', '00bfde0f']]`
  - `UNCONDITIONAL_JUMP` [`00bfde0c`](#insn-00bfde0c) → [`00bfde1c`](#insn-00bfde1c)
- ブロック [`00bfde10`](#insn-00bfde10) 範囲 `[['00bfde10', '00bfde1b']]`
  - `FALL_THROUGH` [`00bfde18`](#insn-00bfde18) → [`00bfde1c`](#insn-00bfde1c)
- ブロック [`00bfde1c`](#insn-00bfde1c) 範囲 `[['00bfde1c', '00bfde2b']]`
  - `CONDITIONAL_JUMP` [`00bfde28`](#insn-00bfde28) → [`00bfdd98`](#insn-00bfdd98)
  - `FALL_THROUGH` [`00bfde28`](#insn-00bfde28) → [`00bfde2c`](#insn-00bfde2c)
- ブロック [`00bfde2c`](#insn-00bfde2c) 範囲 `[['00bfde2c', '00bfde3b']]`
  - `UNCONDITIONAL_JUMP` [`00bfde38`](#insn-00bfde38) → [`00bfdd98`](#insn-00bfdd98)
- ブロック [`00bfde3c`](#insn-00bfde3c) 範囲 `[['00bfde3c', '00bfde57']]`
  - `CONDITIONAL_JUMP` [`00bfde54`](#insn-00bfde54) → [`00bfde84`](#insn-00bfde84)
  - `FALL_THROUGH` [`00bfde54`](#insn-00bfde54) → [`00bfde58`](#insn-00bfde58)
- ブロック [`00bfde58`](#insn-00bfde58) 範囲 `[['00bfde58', '00bfde63']]`
  - `UNCONDITIONAL_JUMP` [`00bfde60`](#insn-00bfde60) → [`00bfde90`](#insn-00bfde90)
- ブロック [`00bfde64`](#insn-00bfde64) 範囲 `[['00bfde64', '00bfde6f']]`
  - `CONDITIONAL_JUMP` [`00bfde6c`](#insn-00bfde6c) → [`00bfdec4`](#insn-00bfdec4)
  - `FALL_THROUGH` [`00bfde6c`](#insn-00bfde6c) → [`00bfde70`](#insn-00bfde70)
- ブロック [`00bfde70`](#insn-00bfde70) 範囲 `[['00bfde70', '00bfde73']]`
  - `UNCONDITIONAL_JUMP` [`00bfde70`](#insn-00bfde70) → [`00bfdec8`](#insn-00bfdec8)
- ブロック [`00bfde74`](#insn-00bfde74) 範囲 `[['00bfde74', '00bfde7f']]`
  - `CONDITIONAL_JUMP` [`00bfde7c`](#insn-00bfde7c) → [`00bfdec4`](#insn-00bfdec4)
  - `FALL_THROUGH` [`00bfde7c`](#insn-00bfde7c) → [`00bfde80`](#insn-00bfde80)
- ブロック [`00bfde80`](#insn-00bfde80) 範囲 `[['00bfde80', '00bfde83']]`
  - `UNCONDITIONAL_JUMP` [`00bfde80`](#insn-00bfde80) → [`00bfdec8`](#insn-00bfdec8)
- ブロック [`00bfde84`](#insn-00bfde84) 範囲 `[['00bfde84', '00bfde8f']]`
  - `FALL_THROUGH` [`00bfde8c`](#insn-00bfde8c) → [`00bfde90`](#insn-00bfde90)
- ブロック [`00bfde90`](#insn-00bfde90) 範囲 `[['00bfde90', '00bfde9f']]`
  - `CONDITIONAL_JUMP` [`00bfde9c`](#insn-00bfde9c) → [`00bfdeb0`](#insn-00bfdeb0)
  - `FALL_THROUGH` [`00bfde9c`](#insn-00bfde9c) → [`00bfdea0`](#insn-00bfdea0)
- ブロック [`00bfdea0`](#insn-00bfdea0) 範囲 `[['00bfdea0', '00bfdeab']]`
  - `CONDITIONAL_JUMP` [`00bfdea8`](#insn-00bfdea8) → [`00bfdec4`](#insn-00bfdec4)
  - `FALL_THROUGH` [`00bfdea8`](#insn-00bfdea8) → [`00bfdeac`](#insn-00bfdeac)
- ブロック [`00bfdeac`](#insn-00bfdeac) 範囲 `[['00bfdeac', '00bfdeaf']]`
  - `UNCONDITIONAL_JUMP` [`00bfdeac`](#insn-00bfdeac) → [`00bfdec8`](#insn-00bfdec8)
- ブロック [`00bfdeb0`](#insn-00bfdeb0) 範囲 `[['00bfdeb0', '00bfdebb']]`
  - `FALL_THROUGH` [`00bfdeb8`](#insn-00bfdeb8) → [`00bfdebc`](#insn-00bfdebc)
- ブロック [`00bfdebc`](#insn-00bfdebc) 範囲 `[['00bfdebc', '00bfdec3']]`
  - `CONDITIONAL_JUMP` [`00bfdec0`](#insn-00bfdec0) → [`00bfdec8`](#insn-00bfdec8)
  - `FALL_THROUGH` [`00bfdec0`](#insn-00bfdec0) → [`00bfdec4`](#insn-00bfdec4)
- ブロック [`00bfdec4`](#insn-00bfdec4) 範囲 `[['00bfdec4', '00bfdec7']]`
  - `FALL_THROUGH` [`00bfdec4`](#insn-00bfdec4) → [`00bfdec8`](#insn-00bfdec8)
- ブロック [`00bfdec8`](#insn-00bfdec8) 範囲 `[['00bfdec8', '00bfdf0f']]`

## 命令位置別の参照

- [`00bfdd44`](#insn-00bfdd44) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd48`](#insn-00bfdd48) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd4c`](#insn-00bfdd4c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd50`](#insn-00bfdd50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd54`](#insn-00bfdd54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd7c`](#insn-00bfdd7c) → [`00c59ea0`](../00c59/00c59ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd80`](#insn-00bfdd80) → `Stack[-0x54]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdd84`](#insn-00bfdd84) → [`00bfdebc`](#insn-00bfdebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfddac`](#insn-00bfddac) → [`00bfddb8`](#insn-00bfddb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfddb4`](#insn-00bfddb4) → [`00bfddcc`](#insn-00bfddcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfddc8`](#insn-00bfddc8) → [`00bfde74`](#insn-00bfde74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfddd4`](#insn-00bfddd4) → [`00bfde3c`](#insn-00bfde3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdde0`](#insn-00bfdde0) → [`00bfde64`](#insn-00bfde64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde00`](#insn-00bfde00) → [`00bfde10`](#insn-00bfde10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde0c`](#insn-00bfde0c) → [`00bfde1c`](#insn-00bfde1c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde28`](#insn-00bfde28) → [`00bfdd98`](#insn-00bfdd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde38`](#insn-00bfde38) → [`00bfdd98`](#insn-00bfdd98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde54`](#insn-00bfde54) → [`00bfde84`](#insn-00bfde84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde60`](#insn-00bfde60) → [`00bfde90`](#insn-00bfde90) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde6c`](#insn-00bfde6c) → [`00bfdec4`](#insn-00bfdec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde70`](#insn-00bfde70) → [`00bfdec8`](#insn-00bfdec8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde7c`](#insn-00bfde7c) → [`00bfdec4`](#insn-00bfdec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde80`](#insn-00bfde80) → [`00bfdec8`](#insn-00bfdec8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfde9c`](#insn-00bfde9c) → [`00bfdeb0`](#insn-00bfdeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdea8`](#insn-00bfdea8) → [`00bfdec4`](#insn-00bfdec4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdeac`](#insn-00bfdeac) → [`00bfdec8`](#insn-00bfdec8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdec0`](#insn-00bfdec0) → [`00bfdec8`](#insn-00bfdec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdee8`](#insn-00bfdee8) → [`00c58370`](../00c58/00c58370.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58370` · 推定シンボル `None` · 推定型 `None`
- [`00bfdef0`](#insn-00bfdef0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdef4`](#insn-00bfdef4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdef8`](#insn-00bfdef8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdefc`](#insn-00bfdefc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf00`](#insn-00bfdf00) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfdd44`](#insn-00bfdd44)

~~~json
{
  "source": "00bfdd44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd48`](#insn-00bfdd48)

~~~json
{
  "source": "00bfdd48",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd4c`](#insn-00bfdd4c)

~~~json
{
  "source": "00bfdd4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd50`](#insn-00bfdd50)

~~~json
{
  "source": "00bfdd50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd54`](#insn-00bfdd54)

~~~json
{
  "source": "00bfdd54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd7c`](#insn-00bfdd7c)

~~~json
{
  "source": "00bfdd7c",
  "target": "00c59ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdd80`](#insn-00bfdd80)

~~~json
{
  "source": "00bfdd80",
  "target": "Stack[-0x54]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdd84`](#insn-00bfdd84)

~~~json
{
  "source": "00bfdd84",
  "target": "00bfdebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfddac`](#insn-00bfddac)

~~~json
{
  "source": "00bfddac",
  "target": "00bfddb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfddb4`](#insn-00bfddb4)

~~~json
{
  "source": "00bfddb4",
  "target": "00bfddcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfddc8`](#insn-00bfddc8)

~~~json
{
  "source": "00bfddc8",
  "target": "00bfde74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfddd4`](#insn-00bfddd4)

~~~json
{
  "source": "00bfddd4",
  "target": "00bfde3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdde0`](#insn-00bfdde0)

~~~json
{
  "source": "00bfdde0",
  "target": "00bfde64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde00`](#insn-00bfde00)

~~~json
{
  "source": "00bfde00",
  "target": "00bfde10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde0c`](#insn-00bfde0c)

~~~json
{
  "source": "00bfde0c",
  "target": "00bfde1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde28`](#insn-00bfde28)

~~~json
{
  "source": "00bfde28",
  "target": "00bfdd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde38`](#insn-00bfde38)

~~~json
{
  "source": "00bfde38",
  "target": "00bfdd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde54`](#insn-00bfde54)

~~~json
{
  "source": "00bfde54",
  "target": "00bfde84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde60`](#insn-00bfde60)

~~~json
{
  "source": "00bfde60",
  "target": "00bfde90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde6c`](#insn-00bfde6c)

~~~json
{
  "source": "00bfde6c",
  "target": "00bfdec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde70`](#insn-00bfde70)

~~~json
{
  "source": "00bfde70",
  "target": "00bfdec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde7c`](#insn-00bfde7c)

~~~json
{
  "source": "00bfde7c",
  "target": "00bfdec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde80`](#insn-00bfde80)

~~~json
{
  "source": "00bfde80",
  "target": "00bfdec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfde9c`](#insn-00bfde9c)

~~~json
{
  "source": "00bfde9c",
  "target": "00bfdeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdea8`](#insn-00bfdea8)

~~~json
{
  "source": "00bfdea8",
  "target": "00bfdec4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdeac`](#insn-00bfdeac)

~~~json
{
  "source": "00bfdeac",
  "target": "00bfdec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdec0`](#insn-00bfdec0)

~~~json
{
  "source": "00bfdec0",
  "target": "00bfdec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdee8`](#insn-00bfdee8)

~~~json
{
  "source": "00bfdee8",
  "target": "00c58370",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdef0`](#insn-00bfdef0)

~~~json
{
  "source": "00bfdef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdef4`](#insn-00bfdef4)

~~~json
{
  "source": "00bfdef4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdef8`](#insn-00bfdef8)

~~~json
{
  "source": "00bfdef8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdefc`](#insn-00bfdefc)

~~~json
{
  "source": "00bfdefc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf00`](#insn-00bfdf00)

~~~json
{
  "source": "00bfdf00",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
