# 00bfda8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfd664`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfd664.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-fae917165a8156680828cabd24f722e2)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfdb28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdb28.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-7e0564eeecf6497eaa9b6dc6367a5345)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfda8c",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "696d3ad6676e0f0528d26a011671b2ce4fafb22e2519b18da9c04409b7dc3d8e",
  "source_text_sha256": "696d3ad6676e0f0528d26a011671b2ce4fafb22e2519b18da9c04409b7dc3d8e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfda8c",
        "00bfdbe7"
      ]
    ],
    "bytes_sha256": "3b8988e52151c77b859353e5751d9cfd5fd4f03fc6ca3b0515f2a213c0be690f",
    "instruction_count": 87,
    "instruction_bytes": 348,
    "body_bytes": 348,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5e380](../00c5e/00c5e380.md)

## 呼び出し先

- [00c582a0](../00c58/00c582a0.md)
- [00c59dd0](../00c59/00c59dd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1699 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getERNS_15basic_streambufIcS2_EEc
                 (long *param_1,long *param_2,uint param_3)

{
  long lVar1;
  uint uVar2;
  undefined1 *puVar3;
  uint uVar4;
  int iVar5;
  long *plVar6;
  char local_24 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_24,param_1,1);
  if (local_24[0] != '\0') {
    while( true ) {
      plVar6 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      if ((byte *)plVar6[3] == (byte *)plVar6[4]) {
        uVar4 = (**(code **)(*plVar6 + 0x48))();
        if (uVar4 == 0xffffffff) {
          uVar4 = 2;
          goto LAB_00bfdba8;
        }
      }
      else {
        uVar4 = (uint)*(byte *)plVar6[3];
      }
      if ((uVar4 & 0xff) == (param_3 & 0xff)) break;
      puVar3 = (undefined1 *)param_2[6];
      if (puVar3 == (undefined1 *)param_2[7]) {
        iVar5 = (**(code **)(*param_2 + 0x68))(param_2,uVar4 & 0xff);
        if (iVar5 == -1) break;
      }
      else {
        param_2[6] = (long)(puVar3 + 1);
        *puVar3 = (char)uVar4;
      }
      if (param_1[1] != 0x7fffffffffffffff) {
        param_1[1] = param_1[1] + 1;
      }
      plVar6 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      if (plVar6[3] == plVar6[4]) {
        (**(code **)(*plVar6 + 0x50))();
      }
      else {
        plVar6[3] = plVar6[3] + 1;
      }
    }
    uVar4 = 0;
LAB_00bfdba8:
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar2 = uVar4 | 4;
    if (param_1[1] != 0) {
      uVar2 = uVar4;
    }
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | uVar2);
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfda8c"></a> `00bfda8c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfda90"></a> `00bfda90` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bfda94"></a> `00bfda94` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfda98"></a> `00bfda98` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfda9c"></a> `00bfda9c` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdaa0"></a> `00bfdaa0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfdaa4"></a> `00bfdaa4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfdaa8"></a> `00bfdaa8` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bfdaac"></a> `00bfdaac` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfdab0"></a> `00bfdab0` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdab4"></a> `00bfdab4` | `a0 73 00 91` | add x0,x29,#0x1c | `FALL_THROUGH`
<a id="insn-00bfdab8"></a> `00bfdab8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfdabc"></a> `00bfdabc` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdac0"></a> `00bfdac0` | `c4 70 01 94` | bl 0x00c59dd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdac4"></a> `00bfdac4` | `a8 73 40 39` | ldrb w8,[x29, #0x1c] | `FALL_THROUGH`
<a id="insn-00bfdac8"></a> `00bfdac8` | `28 08 00 34` | cbz w8,0x00bfdbcc | `CONDITIONAL_JUMP`
<a id="insn-00bfdacc"></a> `00bfdacc` | `b5 1e 00 12` | and w21,w21,#0xff | `FALL_THROUGH`
<a id="insn-00bfdad0"></a> `00bfdad0` | `76 a2 00 91` | add x22,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfdad4"></a> `00bfdad4` | `17 00 f0 92` | mov x23,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfdad8"></a> `00bfdad8` | `09 00 00 14` | b 0x00bfdafc | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdadc"></a> `00bfdadc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfdae0"></a> `00bfdae0` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdae4"></a> `00bfdae4` | `c0 6a 68 f8` | ldr x0,[x22, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfdae8"></a> `00bfdae8` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdaec"></a> `00bfdaec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfdaf0"></a> `00bfdaf0` | `e0 04 00 54` | b.eq 0x00bfdb8c | `CONDITIONAL_JUMP`
<a id="insn-00bfdaf4"></a> `00bfdaf4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdaf8"></a> `00bfdaf8` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdafc"></a> `00bfdafc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfdb00"></a> `00bfdb00` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdb04"></a> `00bfdb04` | `c0 6a 68 f8` | ldr x0,[x22, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfdb08"></a> `00bfdb08` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdb0c"></a> `00bfdb0c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfdb10"></a> `00bfdb10` | `60 00 00 54` | b.eq 0x00bfdb1c | `CONDITIONAL_JUMP`
<a id="insn-00bfdb14"></a> `00bfdb14` | `00 01 40 39` | ldrb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfdb18"></a> `00bfdb18` | `06 00 00 14` | b 0x00bfdb30 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdb1c"></a> `00bfdb1c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfdb20"></a> `00bfdb20` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfdb24"></a> `00bfdb24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfdb28"></a> `00bfdb28` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdb2c"></a> `00bfdb2c` | `c0 03 00 54` | b.eq 0x00bfdba4 | `CONDITIONAL_JUMP`
<a id="insn-00bfdb30"></a> `00bfdb30` | `08 1c 00 12` | and w8,w0,#0xff | `FALL_THROUGH`
<a id="insn-00bfdb34"></a> `00bfdb34` | `1f 01 15 6b` | cmp w8,w21 | `FALL_THROUGH`
<a id="insn-00bfdb38"></a> `00bfdb38` | `20 03 00 54` | b.eq 0x00bfdb9c | `CONDITIONAL_JUMP`
<a id="insn-00bfdb3c"></a> `00bfdb3c` | `89 2a 43 a9` | ldp x9,x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdb40"></a> `00bfdb40` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bfdb44"></a> `00bfdb44` | `a0 00 00 54` | b.eq 0x00bfdb58 | `CONDITIONAL_JUMP`
<a id="insn-00bfdb48"></a> `00bfdb48` | `2a 05 00 91` | add x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdb4c"></a> `00bfdb4c` | `8a 1a 00 f9` | str x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdb50"></a> `00bfdb50` | `28 01 00 39` | strb w8,[x9] | `FALL_THROUGH`
<a id="insn-00bfdb54"></a> `00bfdb54` | `08 00 00 14` | b 0x00bfdb74 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdb58"></a> `00bfdb58` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfdb5c"></a> `00bfdb5c` | `08 35 40 f9` | ldr x8,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-00bfdb60"></a> `00bfdb60` | `01 1c 00 12` | and w1,w0,#0xff | `FALL_THROUGH`
<a id="insn-00bfdb64"></a> `00bfdb64` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfdb68"></a> `00bfdb68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfdb6c"></a> `00bfdb6c` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdb70"></a> `00bfdb70` | `60 01 00 54` | b.eq 0x00bfdb9c | `CONDITIONAL_JUMP`
<a id="insn-00bfdb74"></a> `00bfdb74` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdb78"></a> `00bfdb78` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00bfdb7c"></a> `00bfdb7c` | `00 fb ff 54` | b.eq 0x00bfdadc | `CONDITIONAL_JUMP`
<a id="insn-00bfdb80"></a> `00bfdb80` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdb84"></a> `00bfdb84` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdb88"></a> `00bfdb88` | `d5 ff ff 17` | b 0x00bfdadc | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdb8c"></a> `00bfdb8c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfdb90"></a> `00bfdb90` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfdb94"></a> `00bfdb94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfdb98"></a> `00bfdb98` | `d9 ff ff 17` | b 0x00bfdafc | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdb9c"></a> `00bfdb9c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfdba0"></a> `00bfdba0` | `02 00 00 14` | b 0x00bfdba8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdba4"></a> `00bfdba4` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bfdba8"></a> `00bfdba8` | `69 2a 40 a9` | ldp x9,x10,[x19] | `FALL_THROUGH`
<a id="insn-00bfdbac"></a> `00bfdbac` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdbb0"></a> `00bfdbb0` | `5f 01 00 f1` | cmp x10,#0x0 | `FALL_THROUGH`
<a id="insn-00bfdbb4"></a> `00bfdbb4` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfdbb8"></a> `00bfdbb8` | `09 01 1e 32` | orr w9,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfdbbc"></a> `00bfdbbc` | `0a 20 40 b9` | ldr w10,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdbc0"></a> `00bfdbc0` | `28 01 88 1a` | csel w8,w9,w8,eq | `FALL_THROUGH`
<a id="insn-00bfdbc4"></a> `00bfdbc4` | `41 01 08 2a` | orr w1,w10,w8 | `FALL_THROUGH`
<a id="insn-00bfdbc8"></a> `00bfdbc8` | `b6 69 01 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdbcc"></a> `00bfdbcc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfdbd0"></a> `00bfdbd0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdbd4"></a> `00bfdbd4` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfdbd8"></a> `00bfdbd8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdbdc"></a> `00bfdbdc` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bfdbe0"></a> `00bfdbe0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfdbe4"></a> `00bfdbe4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfda8c`](#insn-00bfda8c) 範囲 `[['00bfda8c', '00bfdacb']]`
  - `CONDITIONAL_JUMP` [`00bfdac8`](#insn-00bfdac8) → [`00bfdbcc`](#insn-00bfdbcc)
  - `FALL_THROUGH` [`00bfdac8`](#insn-00bfdac8) → [`00bfdacc`](#insn-00bfdacc)
- ブロック [`00bfdacc`](#insn-00bfdacc) 範囲 `[['00bfdacc', '00bfdadb']]`
  - `UNCONDITIONAL_JUMP` [`00bfdad8`](#insn-00bfdad8) → [`00bfdafc`](#insn-00bfdafc)
- ブロック [`00bfdadc`](#insn-00bfdadc) 範囲 `[['00bfdadc', '00bfdaf3']]`
  - `CONDITIONAL_JUMP` [`00bfdaf0`](#insn-00bfdaf0) → [`00bfdb8c`](#insn-00bfdb8c)
  - `FALL_THROUGH` [`00bfdaf0`](#insn-00bfdaf0) → [`00bfdaf4`](#insn-00bfdaf4)
- ブロック [`00bfdaf4`](#insn-00bfdaf4) 範囲 `[['00bfdaf4', '00bfdafb']]`
  - `FALL_THROUGH` [`00bfdaf8`](#insn-00bfdaf8) → [`00bfdafc`](#insn-00bfdafc)
- ブロック [`00bfdafc`](#insn-00bfdafc) 範囲 `[['00bfdafc', '00bfdb13']]`
  - `CONDITIONAL_JUMP` [`00bfdb10`](#insn-00bfdb10) → [`00bfdb1c`](#insn-00bfdb1c)
  - `FALL_THROUGH` [`00bfdb10`](#insn-00bfdb10) → [`00bfdb14`](#insn-00bfdb14)
- ブロック [`00bfdb14`](#insn-00bfdb14) 範囲 `[['00bfdb14', '00bfdb1b']]`
  - `UNCONDITIONAL_JUMP` [`00bfdb18`](#insn-00bfdb18) → [`00bfdb30`](#insn-00bfdb30)
- ブロック [`00bfdb1c`](#insn-00bfdb1c) 範囲 `[['00bfdb1c', '00bfdb2f']]`
  - `CONDITIONAL_JUMP` [`00bfdb2c`](#insn-00bfdb2c) → [`00bfdba4`](#insn-00bfdba4)
  - `FALL_THROUGH` [`00bfdb2c`](#insn-00bfdb2c) → [`00bfdb30`](#insn-00bfdb30)
- ブロック [`00bfdb30`](#insn-00bfdb30) 範囲 `[['00bfdb30', '00bfdb3b']]`
  - `CONDITIONAL_JUMP` [`00bfdb38`](#insn-00bfdb38) → [`00bfdb9c`](#insn-00bfdb9c)
  - `FALL_THROUGH` [`00bfdb38`](#insn-00bfdb38) → [`00bfdb3c`](#insn-00bfdb3c)
- ブロック [`00bfdb3c`](#insn-00bfdb3c) 範囲 `[['00bfdb3c', '00bfdb47']]`
  - `CONDITIONAL_JUMP` [`00bfdb44`](#insn-00bfdb44) → [`00bfdb58`](#insn-00bfdb58)
  - `FALL_THROUGH` [`00bfdb44`](#insn-00bfdb44) → [`00bfdb48`](#insn-00bfdb48)
- ブロック [`00bfdb48`](#insn-00bfdb48) 範囲 `[['00bfdb48', '00bfdb57']]`
  - `UNCONDITIONAL_JUMP` [`00bfdb54`](#insn-00bfdb54) → [`00bfdb74`](#insn-00bfdb74)
- ブロック [`00bfdb58`](#insn-00bfdb58) 範囲 `[['00bfdb58', '00bfdb73']]`
  - `CONDITIONAL_JUMP` [`00bfdb70`](#insn-00bfdb70) → [`00bfdb9c`](#insn-00bfdb9c)
  - `FALL_THROUGH` [`00bfdb70`](#insn-00bfdb70) → [`00bfdb74`](#insn-00bfdb74)
- ブロック [`00bfdb74`](#insn-00bfdb74) 範囲 `[['00bfdb74', '00bfdb7f']]`
  - `CONDITIONAL_JUMP` [`00bfdb7c`](#insn-00bfdb7c) → [`00bfdadc`](#insn-00bfdadc)
  - `FALL_THROUGH` [`00bfdb7c`](#insn-00bfdb7c) → [`00bfdb80`](#insn-00bfdb80)
- ブロック [`00bfdb80`](#insn-00bfdb80) 範囲 `[['00bfdb80', '00bfdb8b']]`
  - `UNCONDITIONAL_JUMP` [`00bfdb88`](#insn-00bfdb88) → [`00bfdadc`](#insn-00bfdadc)
- ブロック [`00bfdb8c`](#insn-00bfdb8c) 範囲 `[['00bfdb8c', '00bfdb9b']]`
  - `UNCONDITIONAL_JUMP` [`00bfdb98`](#insn-00bfdb98) → [`00bfdafc`](#insn-00bfdafc)
- ブロック [`00bfdb9c`](#insn-00bfdb9c) 範囲 `[['00bfdb9c', '00bfdba3']]`
  - `UNCONDITIONAL_JUMP` [`00bfdba0`](#insn-00bfdba0) → [`00bfdba8`](#insn-00bfdba8)
- ブロック [`00bfdba4`](#insn-00bfdba4) 範囲 `[['00bfdba4', '00bfdba7']]`
  - `FALL_THROUGH` [`00bfdba4`](#insn-00bfdba4) → [`00bfdba8`](#insn-00bfdba8)
- ブロック [`00bfdba8`](#insn-00bfdba8) 範囲 `[['00bfdba8', '00bfdbcb']]`
  - `FALL_THROUGH` [`00bfdbc8`](#insn-00bfdbc8) → [`00bfdbcc`](#insn-00bfdbcc)
- ブロック [`00bfdbcc`](#insn-00bfdbcc) 範囲 `[['00bfdbcc', '00bfdbe7']]`

## 命令位置別の参照

- [`00bfda90`](#insn-00bfda90) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfda94`](#insn-00bfda94) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfda98`](#insn-00bfda98) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfda9c`](#insn-00bfda9c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdac0`](#insn-00bfdac0) → [`00c59dd0`](../00c59/00c59dd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59dd0` · 推定シンボル `None` · 推定型 `None`
- [`00bfdac4`](#insn-00bfdac4) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdac8`](#insn-00bfdac8) → [`00bfdbcc`](#insn-00bfdbcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdad8`](#insn-00bfdad8) → [`00bfdafc`](#insn-00bfdafc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdaf0`](#insn-00bfdaf0) → [`00bfdb8c`](#insn-00bfdb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb10`](#insn-00bfdb10) → [`00bfdb1c`](#insn-00bfdb1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb18`](#insn-00bfdb18) → [`00bfdb30`](#insn-00bfdb30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb2c`](#insn-00bfdb2c) → [`00bfdba4`](#insn-00bfdba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb38`](#insn-00bfdb38) → [`00bfdb9c`](#insn-00bfdb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb44`](#insn-00bfdb44) → [`00bfdb58`](#insn-00bfdb58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb54`](#insn-00bfdb54) → [`00bfdb74`](#insn-00bfdb74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb70`](#insn-00bfdb70) → [`00bfdb9c`](#insn-00bfdb9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb7c`](#insn-00bfdb7c) → [`00bfdadc`](#insn-00bfdadc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb88`](#insn-00bfdb88) → [`00bfdadc`](#insn-00bfdadc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdb98`](#insn-00bfdb98) → [`00bfdafc`](#insn-00bfdafc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdba0`](#insn-00bfdba0) → [`00bfdba8`](#insn-00bfdba8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdbc8`](#insn-00bfdbc8) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00bfdbd0`](#insn-00bfdbd0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdbd4`](#insn-00bfdbd4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdbd8`](#insn-00bfdbd8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdbdc`](#insn-00bfdbdc) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfda90`](#insn-00bfda90)

~~~json
{
  "source": "00bfda90",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfda94`](#insn-00bfda94)

~~~json
{
  "source": "00bfda94",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfda98`](#insn-00bfda98)

~~~json
{
  "source": "00bfda98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfda9c`](#insn-00bfda9c)

~~~json
{
  "source": "00bfda9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdac0`](#insn-00bfdac0)

~~~json
{
  "source": "00bfdac0",
  "target": "00c59dd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdac4`](#insn-00bfdac4)

~~~json
{
  "source": "00bfdac4",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdac8`](#insn-00bfdac8)

~~~json
{
  "source": "00bfdac8",
  "target": "00bfdbcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdad8`](#insn-00bfdad8)

~~~json
{
  "source": "00bfdad8",
  "target": "00bfdafc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdaf0`](#insn-00bfdaf0)

~~~json
{
  "source": "00bfdaf0",
  "target": "00bfdb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb10`](#insn-00bfdb10)

~~~json
{
  "source": "00bfdb10",
  "target": "00bfdb1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb18`](#insn-00bfdb18)

~~~json
{
  "source": "00bfdb18",
  "target": "00bfdb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb2c`](#insn-00bfdb2c)

~~~json
{
  "source": "00bfdb2c",
  "target": "00bfdba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb38`](#insn-00bfdb38)

~~~json
{
  "source": "00bfdb38",
  "target": "00bfdb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb44`](#insn-00bfdb44)

~~~json
{
  "source": "00bfdb44",
  "target": "00bfdb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb54`](#insn-00bfdb54)

~~~json
{
  "source": "00bfdb54",
  "target": "00bfdb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb70`](#insn-00bfdb70)

~~~json
{
  "source": "00bfdb70",
  "target": "00bfdb9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb7c`](#insn-00bfdb7c)

~~~json
{
  "source": "00bfdb7c",
  "target": "00bfdadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb88`](#insn-00bfdb88)

~~~json
{
  "source": "00bfdb88",
  "target": "00bfdadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdb98`](#insn-00bfdb98)

~~~json
{
  "source": "00bfdb98",
  "target": "00bfdafc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdba0`](#insn-00bfdba0)

~~~json
{
  "source": "00bfdba0",
  "target": "00bfdba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdbc8`](#insn-00bfdbc8)

~~~json
{
  "source": "00bfdbc8",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdbd0`](#insn-00bfdbd0)

~~~json
{
  "source": "00bfdbd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdbd4`](#insn-00bfdbd4)

~~~json
{
  "source": "00bfdbd4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdbd8`](#insn-00bfdbd8)

~~~json
{
  "source": "00bfdbd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdbdc`](#insn-00bfdbdc)

~~~json
{
  "source": "00bfdbdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
