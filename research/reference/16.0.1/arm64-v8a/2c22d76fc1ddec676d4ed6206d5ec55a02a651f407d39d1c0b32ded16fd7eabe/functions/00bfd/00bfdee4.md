# 00bfdee4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfdabc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfd/00bfdabc.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-55f6fe04cd72333891f7f148aec12d98)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfdf80`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfd/00bfdf80.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-8cdebc5a98e4816ee9be1490adc2238d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfdee4",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7dfa5252499c1a3dbe60a27c1e381642438f41986725c598e63fe52262f04e7a",
  "source_text_sha256": "7dfa5252499c1a3dbe60a27c1e381642438f41986725c598e63fe52262f04e7a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfdee4",
        "00bfe04b"
      ]
    ],
    "bytes_sha256": "f53cc6d0b9e4ea1644d5e99d3f4076d778c6a3e0d71d3ee41ffeeabd933d941a",
    "instruction_count": 90,
    "instruction_bytes": 360,
    "body_bytes": 360,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c582a0](../00c58/00c582a0.md)
- [00c59dd0](../00c59/00c59dd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1832 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6ignoreEli
                 (long *param_1,long param_2,uint param_3)

{
  byte *pbVar1;
  uint uVar2;
  long *plVar3;
  long lVar4;
  char local_24 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_24,param_1,1);
  if (local_24[0] == '\0') {
    return param_1;
  }
  if (param_2 == 0x7fffffffffffffff) {
    do {
      plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
      pbVar1 = (byte *)plVar3[3];
      if (pbVar1 == (byte *)plVar3[4]) {
        uVar2 = (**(code **)(*plVar3 + 0x50))();
        if (uVar2 == 0xffffffff) goto LAB_00bfe014;
      }
      else {
        plVar3[3] = (long)(pbVar1 + 1);
        uVar2 = (uint)*pbVar1;
      }
      if (param_1[1] != 0x7fffffffffffffff) {
        param_1[1] = param_1[1] + 1;
      }
    } while (uVar2 != param_3);
  }
  else {
    lVar4 = param_1[1];
    if (lVar4 < param_2) {
      do {
        plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
        pbVar1 = (byte *)plVar3[3];
        if (pbVar1 == (byte *)plVar3[4]) {
          uVar2 = (**(code **)(*plVar3 + 0x50))();
          if (uVar2 == 0xffffffff) goto LAB_00bfe014;
          lVar4 = param_1[1];
          if (lVar4 != 0x7fffffffffffffff) goto LAB_00bfdfb8;
          lVar4 = param_1[1];
        }
        else {
          plVar3[3] = (long)(pbVar1 + 1);
          uVar2 = (uint)*pbVar1;
LAB_00bfdfb8:
          lVar4 = lVar4 + 1;
          param_1[1] = lVar4;
        }
      } while (uVar2 != param_3 && lVar4 < param_2);
    }
  }
  uVar2 = 0;
LAB_00bfe018:
  lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | uVar2);
  return param_1;
LAB_00bfe014:
  uVar2 = 2;
  goto LAB_00bfe018;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfdee4"></a> `00bfdee4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfdee8"></a> `00bfdee8` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bfdeec"></a> `00bfdeec` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfdef0"></a> `00bfdef0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfdef4"></a> `00bfdef4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfdef8"></a> `00bfdef8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfdefc"></a> `00bfdefc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfdf00"></a> `00bfdf00` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-00bfdf04"></a> `00bfdf04` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bfdf08"></a> `00bfdf08` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdf0c"></a> `00bfdf0c` | `a0 73 00 91` | add x0,x29,#0x1c | `FALL_THROUGH`
<a id="insn-00bfdf10"></a> `00bfdf10` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfdf14"></a> `00bfdf14` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdf18"></a> `00bfdf18` | `ae 6f 01 94` | bl 0x00c59dd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfdf1c"></a> `00bfdf1c` | `a8 73 40 39` | ldrb w8,[x29, #0x1c] | `FALL_THROUGH`
<a id="insn-00bfdf20"></a> `00bfdf20` | `88 08 00 34` | cbz w8,0x00bfe030 | `CONDITIONAL_JUMP`
<a id="insn-00bfdf24"></a> `00bfdf24` | `16 00 f0 92` | mov x22,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfdf28"></a> `00bfdf28` | `bf 02 16 eb` | cmp x21,x22 | `FALL_THROUGH`
<a id="insn-00bfdf2c"></a> `00bfdf2c` | `41 03 00 54` | b.ne 0x00bfdf94 | `CONDITIONAL_JUMP`
<a id="insn-00bfdf30"></a> `00bfdf30` | `75 a2 00 91` | add x21,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfdf34"></a> `00bfdf34` | `03 00 00 14` | b 0x00bfdf40 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdf38"></a> `00bfdf38` | `1f 00 14 6b` | cmp w0,w20 | `FALL_THROUGH`
<a id="insn-00bfdf3c"></a> `00bfdf3c` | `80 06 00 54` | b.eq 0x00bfe00c | `CONDITIONAL_JUMP`
<a id="insn-00bfdf40"></a> `00bfdf40` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfdf44"></a> `00bfdf44` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdf48"></a> `00bfdf48` | `a0 6a 68 f8` | ldr x0,[x21, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfdf4c"></a> `00bfdf4c` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdf50"></a> `00bfdf50` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfdf54"></a> `00bfdf54` | `a0 00 00 54` | b.eq 0x00bfdf68 | `CONDITIONAL_JUMP`
<a id="insn-00bfdf58"></a> `00bfdf58` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdf5c"></a> `00bfdf5c` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdf60"></a> `00bfdf60` | `00 01 40 39` | ldrb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfdf64"></a> `00bfdf64` | `06 00 00 14` | b 0x00bfdf7c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdf68"></a> `00bfdf68` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfdf6c"></a> `00bfdf6c` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfdf70"></a> `00bfdf70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfdf74"></a> `00bfdf74` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdf78"></a> `00bfdf78` | `e0 04 00 54` | b.eq 0x00bfe014 | `CONDITIONAL_JUMP`
<a id="insn-00bfdf7c"></a> `00bfdf7c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdf80"></a> `00bfdf80` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bfdf84"></a> `00bfdf84` | `a0 fd ff 54` | b.eq 0x00bfdf38 | `CONDITIONAL_JUMP`
<a id="insn-00bfdf88"></a> `00bfdf88` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdf8c"></a> `00bfdf8c` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdf90"></a> `00bfdf90` | `ea ff ff 17` | b 0x00bfdf38 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdf94"></a> `00bfdf94` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdf98"></a> `00bfdf98` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bfdf9c"></a> `00bfdf9c` | `8a 03 00 54` | b.ge 0x00bfe00c | `CONDITIONAL_JUMP`
<a id="insn-00bfdfa0"></a> `00bfdfa0` | `76 a2 00 91` | add x22,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfdfa4"></a> `00bfdfa4` | `17 00 f0 92` | mov x23,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfdfa8"></a> `00bfdfa8` | `09 00 00 14` | b 0x00bfdfcc | `UNCONDITIONAL_JUMP`
<a id="insn-00bfdfac"></a> `00bfdfac` | `2a 05 00 91` | add x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdfb0"></a> `00bfdfb0` | `0a 0c 00 f9` | str x10,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdfb4"></a> `00bfdfb4` | `20 01 40 39` | ldrb w0,[x9] | `FALL_THROUGH`
<a id="insn-00bfdfb8"></a> `00bfdfb8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdfbc"></a> `00bfdfbc` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdfc0"></a> `00bfdfc0` | `1f 00 14 6b` | cmp w0,w20 | `FALL_THROUGH`
<a id="insn-00bfdfc4"></a> `00bfdfc4` | `00 11 55 fa` | ccmp x8,x21,#0x0,ne | `FALL_THROUGH`
<a id="insn-00bfdfc8"></a> `00bfdfc8` | `2a 02 00 54` | b.ge 0x00bfe00c | `CONDITIONAL_JUMP`
<a id="insn-00bfdfcc"></a> `00bfdfcc` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bfdfd0"></a> `00bfdfd0` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfdfd4"></a> `00bfdfd4` | `c0 6a 69 f8` | ldr x0,[x22, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfdfd8"></a> `00bfdfd8` | `09 a8 41 a9` | ldp x9,x10,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfdfdc"></a> `00bfdfdc` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bfdfe0"></a> `00bfdfe0` | `61 fe ff 54` | b.ne 0x00bfdfac | `CONDITIONAL_JUMP`
<a id="insn-00bfdfe4"></a> `00bfdfe4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfdfe8"></a> `00bfdfe8` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfdfec"></a> `00bfdfec` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfdff0"></a> `00bfdff0` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfdff4"></a> `00bfdff4` | `00 01 00 54` | b.eq 0x00bfe014 | `CONDITIONAL_JUMP`
<a id="insn-00bfdff8"></a> `00bfdff8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfdffc"></a> `00bfdffc` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00bfe000"></a> `00bfe000` | `c1 fd ff 54` | b.ne 0x00bfdfb8 | `CONDITIONAL_JUMP`
<a id="insn-00bfe004"></a> `00bfe004` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfe008"></a> `00bfe008` | `ee ff ff 17` | b 0x00bfdfc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfe00c"></a> `00bfe00c` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfe010"></a> `00bfe010` | `02 00 00 14` | b 0x00bfe018 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfe014"></a> `00bfe014` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bfe018"></a> `00bfe018` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00bfe01c"></a> `00bfe01c` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfe020"></a> `00bfe020` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfe024"></a> `00bfe024` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfe028"></a> `00bfe028` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfe02c"></a> `00bfe02c` | `9d 68 01 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe030"></a> `00bfe030` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfe034"></a> `00bfe034` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfe038"></a> `00bfe038` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfe03c"></a> `00bfe03c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfe040"></a> `00bfe040` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bfe044"></a> `00bfe044` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfe048"></a> `00bfe048` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfdee4`](#insn-00bfdee4) 範囲 `[['00bfdee4', '00bfdf23']]`
  - `CONDITIONAL_JUMP` [`00bfdf20`](#insn-00bfdf20) → [`00bfe030`](#insn-00bfe030)
  - `FALL_THROUGH` [`00bfdf20`](#insn-00bfdf20) → [`00bfdf24`](#insn-00bfdf24)
- ブロック [`00bfdf24`](#insn-00bfdf24) 範囲 `[['00bfdf24', '00bfdf2f']]`
  - `CONDITIONAL_JUMP` [`00bfdf2c`](#insn-00bfdf2c) → [`00bfdf94`](#insn-00bfdf94)
  - `FALL_THROUGH` [`00bfdf2c`](#insn-00bfdf2c) → [`00bfdf30`](#insn-00bfdf30)
- ブロック [`00bfdf30`](#insn-00bfdf30) 範囲 `[['00bfdf30', '00bfdf37']]`
  - `UNCONDITIONAL_JUMP` [`00bfdf34`](#insn-00bfdf34) → [`00bfdf40`](#insn-00bfdf40)
- ブロック [`00bfdf38`](#insn-00bfdf38) 範囲 `[['00bfdf38', '00bfdf3f']]`
  - `CONDITIONAL_JUMP` [`00bfdf3c`](#insn-00bfdf3c) → [`00bfe00c`](#insn-00bfe00c)
  - `FALL_THROUGH` [`00bfdf3c`](#insn-00bfdf3c) → [`00bfdf40`](#insn-00bfdf40)
- ブロック [`00bfdf40`](#insn-00bfdf40) 範囲 `[['00bfdf40', '00bfdf57']]`
  - `CONDITIONAL_JUMP` [`00bfdf54`](#insn-00bfdf54) → [`00bfdf68`](#insn-00bfdf68)
  - `FALL_THROUGH` [`00bfdf54`](#insn-00bfdf54) → [`00bfdf58`](#insn-00bfdf58)
- ブロック [`00bfdf58`](#insn-00bfdf58) 範囲 `[['00bfdf58', '00bfdf67']]`
  - `UNCONDITIONAL_JUMP` [`00bfdf64`](#insn-00bfdf64) → [`00bfdf7c`](#insn-00bfdf7c)
- ブロック [`00bfdf68`](#insn-00bfdf68) 範囲 `[['00bfdf68', '00bfdf7b']]`
  - `CONDITIONAL_JUMP` [`00bfdf78`](#insn-00bfdf78) → [`00bfe014`](#insn-00bfe014)
  - `FALL_THROUGH` [`00bfdf78`](#insn-00bfdf78) → [`00bfdf7c`](#insn-00bfdf7c)
- ブロック [`00bfdf7c`](#insn-00bfdf7c) 範囲 `[['00bfdf7c', '00bfdf87']]`
  - `CONDITIONAL_JUMP` [`00bfdf84`](#insn-00bfdf84) → [`00bfdf38`](#insn-00bfdf38)
  - `FALL_THROUGH` [`00bfdf84`](#insn-00bfdf84) → [`00bfdf88`](#insn-00bfdf88)
- ブロック [`00bfdf88`](#insn-00bfdf88) 範囲 `[['00bfdf88', '00bfdf93']]`
  - `UNCONDITIONAL_JUMP` [`00bfdf90`](#insn-00bfdf90) → [`00bfdf38`](#insn-00bfdf38)
- ブロック [`00bfdf94`](#insn-00bfdf94) 範囲 `[['00bfdf94', '00bfdf9f']]`
  - `CONDITIONAL_JUMP` [`00bfdf9c`](#insn-00bfdf9c) → [`00bfe00c`](#insn-00bfe00c)
  - `FALL_THROUGH` [`00bfdf9c`](#insn-00bfdf9c) → [`00bfdfa0`](#insn-00bfdfa0)
- ブロック [`00bfdfa0`](#insn-00bfdfa0) 範囲 `[['00bfdfa0', '00bfdfab']]`
  - `UNCONDITIONAL_JUMP` [`00bfdfa8`](#insn-00bfdfa8) → [`00bfdfcc`](#insn-00bfdfcc)
- ブロック [`00bfdfac`](#insn-00bfdfac) 範囲 `[['00bfdfac', '00bfdfb7']]`
  - `FALL_THROUGH` [`00bfdfb4`](#insn-00bfdfb4) → [`00bfdfb8`](#insn-00bfdfb8)
- ブロック [`00bfdfb8`](#insn-00bfdfb8) 範囲 `[['00bfdfb8', '00bfdfbf']]`
  - `FALL_THROUGH` [`00bfdfbc`](#insn-00bfdfbc) → [`00bfdfc0`](#insn-00bfdfc0)
- ブロック [`00bfdfc0`](#insn-00bfdfc0) 範囲 `[['00bfdfc0', '00bfdfcb']]`
  - `CONDITIONAL_JUMP` [`00bfdfc8`](#insn-00bfdfc8) → [`00bfe00c`](#insn-00bfe00c)
  - `FALL_THROUGH` [`00bfdfc8`](#insn-00bfdfc8) → [`00bfdfcc`](#insn-00bfdfcc)
- ブロック [`00bfdfcc`](#insn-00bfdfcc) 範囲 `[['00bfdfcc', '00bfdfe3']]`
  - `CONDITIONAL_JUMP` [`00bfdfe0`](#insn-00bfdfe0) → [`00bfdfac`](#insn-00bfdfac)
  - `FALL_THROUGH` [`00bfdfe0`](#insn-00bfdfe0) → [`00bfdfe4`](#insn-00bfdfe4)
- ブロック [`00bfdfe4`](#insn-00bfdfe4) 範囲 `[['00bfdfe4', '00bfdff7']]`
  - `CONDITIONAL_JUMP` [`00bfdff4`](#insn-00bfdff4) → [`00bfe014`](#insn-00bfe014)
  - `FALL_THROUGH` [`00bfdff4`](#insn-00bfdff4) → [`00bfdff8`](#insn-00bfdff8)
- ブロック [`00bfdff8`](#insn-00bfdff8) 範囲 `[['00bfdff8', '00bfe003']]`
  - `CONDITIONAL_JUMP` [`00bfe000`](#insn-00bfe000) → [`00bfdfb8`](#insn-00bfdfb8)
  - `FALL_THROUGH` [`00bfe000`](#insn-00bfe000) → [`00bfe004`](#insn-00bfe004)
- ブロック [`00bfe004`](#insn-00bfe004) 範囲 `[['00bfe004', '00bfe00b']]`
  - `UNCONDITIONAL_JUMP` [`00bfe008`](#insn-00bfe008) → [`00bfdfc0`](#insn-00bfdfc0)
- ブロック [`00bfe00c`](#insn-00bfe00c) 範囲 `[['00bfe00c', '00bfe013']]`
  - `UNCONDITIONAL_JUMP` [`00bfe010`](#insn-00bfe010) → [`00bfe018`](#insn-00bfe018)
- ブロック [`00bfe014`](#insn-00bfe014) 範囲 `[['00bfe014', '00bfe017']]`
  - `FALL_THROUGH` [`00bfe014`](#insn-00bfe014) → [`00bfe018`](#insn-00bfe018)
- ブロック [`00bfe018`](#insn-00bfe018) 範囲 `[['00bfe018', '00bfe02f']]`
  - `FALL_THROUGH` [`00bfe02c`](#insn-00bfe02c) → [`00bfe030`](#insn-00bfe030)
- ブロック [`00bfe030`](#insn-00bfe030) 範囲 `[['00bfe030', '00bfe04b']]`

## 命令位置別の参照

- [`00bfdee8`](#insn-00bfdee8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdeec`](#insn-00bfdeec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdef0`](#insn-00bfdef0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdef4`](#insn-00bfdef4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf18`](#insn-00bfdf18) → [`00c59dd0`](../00c59/00c59dd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59dd0` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf1c`](#insn-00bfdf1c) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf20`](#insn-00bfdf20) → [`00bfe030`](#insn-00bfe030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf2c`](#insn-00bfdf2c) → [`00bfdf94`](#insn-00bfdf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf34`](#insn-00bfdf34) → [`00bfdf40`](#insn-00bfdf40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf3c`](#insn-00bfdf3c) → [`00bfe00c`](#insn-00bfe00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf54`](#insn-00bfdf54) → [`00bfdf68`](#insn-00bfdf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf64`](#insn-00bfdf64) → [`00bfdf7c`](#insn-00bfdf7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf78`](#insn-00bfdf78) → [`00bfe014`](#insn-00bfe014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf84`](#insn-00bfdf84) → [`00bfdf38`](#insn-00bfdf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf90`](#insn-00bfdf90) → [`00bfdf38`](#insn-00bfdf38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdf9c`](#insn-00bfdf9c) → [`00bfe00c`](#insn-00bfe00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdfa8`](#insn-00bfdfa8) → [`00bfdfcc`](#insn-00bfdfcc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdfc8`](#insn-00bfdfc8) → [`00bfe00c`](#insn-00bfe00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdfe0`](#insn-00bfdfe0) → [`00bfdfac`](#insn-00bfdfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfdff4`](#insn-00bfdff4) → [`00bfe014`](#insn-00bfe014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe000`](#insn-00bfe000) → [`00bfdfb8`](#insn-00bfdfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe008`](#insn-00bfe008) → [`00bfdfc0`](#insn-00bfdfc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe010`](#insn-00bfe010) → [`00bfe018`](#insn-00bfe018) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe02c`](#insn-00bfe02c) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00bfe034`](#insn-00bfe034) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe038`](#insn-00bfe038) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe03c`](#insn-00bfe03c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe040`](#insn-00bfe040) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfdee8`](#insn-00bfdee8)

~~~json
{
  "source": "00bfdee8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdeec`](#insn-00bfdeec)

~~~json
{
  "source": "00bfdeec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdef0`](#insn-00bfdef0)

~~~json
{
  "source": "00bfdef0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdef4`](#insn-00bfdef4)

~~~json
{
  "source": "00bfdef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf18`](#insn-00bfdf18)

~~~json
{
  "source": "00bfdf18",
  "target": "00c59dd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfdf1c`](#insn-00bfdf1c)

~~~json
{
  "source": "00bfdf1c",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf20`](#insn-00bfdf20)

~~~json
{
  "source": "00bfdf20",
  "target": "00bfe030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf2c`](#insn-00bfdf2c)

~~~json
{
  "source": "00bfdf2c",
  "target": "00bfdf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf34`](#insn-00bfdf34)

~~~json
{
  "source": "00bfdf34",
  "target": "00bfdf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf3c`](#insn-00bfdf3c)

~~~json
{
  "source": "00bfdf3c",
  "target": "00bfe00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf54`](#insn-00bfdf54)

~~~json
{
  "source": "00bfdf54",
  "target": "00bfdf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf64`](#insn-00bfdf64)

~~~json
{
  "source": "00bfdf64",
  "target": "00bfdf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf78`](#insn-00bfdf78)

~~~json
{
  "source": "00bfdf78",
  "target": "00bfe014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf84`](#insn-00bfdf84)

~~~json
{
  "source": "00bfdf84",
  "target": "00bfdf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf90`](#insn-00bfdf90)

~~~json
{
  "source": "00bfdf90",
  "target": "00bfdf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdf9c`](#insn-00bfdf9c)

~~~json
{
  "source": "00bfdf9c",
  "target": "00bfe00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdfa8`](#insn-00bfdfa8)

~~~json
{
  "source": "00bfdfa8",
  "target": "00bfdfcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdfc8`](#insn-00bfdfc8)

~~~json
{
  "source": "00bfdfc8",
  "target": "00bfe00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdfe0`](#insn-00bfdfe0)

~~~json
{
  "source": "00bfdfe0",
  "target": "00bfdfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfdff4`](#insn-00bfdff4)

~~~json
{
  "source": "00bfdff4",
  "target": "00bfe014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe000`](#insn-00bfe000)

~~~json
{
  "source": "00bfe000",
  "target": "00bfdfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe008`](#insn-00bfe008)

~~~json
{
  "source": "00bfe008",
  "target": "00bfdfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe010`](#insn-00bfe010)

~~~json
{
  "source": "00bfe010",
  "target": "00bfe018",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe02c`](#insn-00bfe02c)

~~~json
{
  "source": "00bfe02c",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfe034`](#insn-00bfe034)

~~~json
{
  "source": "00bfe034",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe038`](#insn-00bfe038)

~~~json
{
  "source": "00bfe038",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe03c`](#insn-00bfe03c)

~~~json
{
  "source": "00bfe03c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe040`](#insn-00bfe040)

~~~json
{
  "source": "00bfe040",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
