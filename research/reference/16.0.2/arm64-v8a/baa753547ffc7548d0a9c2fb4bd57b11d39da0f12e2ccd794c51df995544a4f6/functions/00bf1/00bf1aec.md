# 00bf1aec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf1a50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf1/00bf1a50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-9fae1b943a125ccd22ba65d2e074b8ec)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf2ae0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf2/00bf2ae0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0037.md#compare-5ec908784888bdf777793ec6479c7ff7)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf1aec",
  "name": "_ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEmc",
  "size": 324,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e68af0ce8082cbba452f8bf0e8131ae8829714faf584dfca52abdb6b01bfef0d",
  "source_text_sha256": "e68af0ce8082cbba452f8bf0e8131ae8829714faf584dfca52abdb6b01bfef0d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf1aec",
        "00bf1c2f"
      ]
    ],
    "bytes_sha256": "85d61cd9e152a3a3ef34abc3e0b6a2e15a271ec7536a1231018280f538aed8f6",
    "instruction_count": 81,
    "instruction_bytes": 324,
    "body_bytes": 324,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5a7b0](../00c5a/00c5a7b0.md)

## 呼び出し先

- [0043b7a4](../0043b/0043b7a4.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c58160](../00c58/00c58160.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1668 bytes

~~~c

ulong * _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6assignEmc
                  (ulong *param_1,ulong param_2,int param_3)

{
  ulong uVar1;
  byte *__s;
  ulong uVar2;
  byte *__ptr;
  ulong uVar3;
  
  uVar2 = *param_1;
  uVar1 = *param_1;
  uVar3 = 0x16;
  if ((uVar1 & 1) != 0) {
    uVar3 = (uVar2 & 0xfffffffffffffffe) - 1;
  }
  if (uVar3 < param_2) {
    if (-uVar3 - 9 < param_2 - uVar3) {
                    /* WARNING: Subroutine does not return */
      FUN_0043b7a4(param_1);
    }
    __ptr = (byte *)param_1[2];
    if ((uVar2 & 1) == 0) {
      __ptr = (byte *)((long)param_1 + 1);
    }
    if (uVar3 < 0x7ffffffffffffff3) {
      uVar2 = param_2;
      if (param_2 <= uVar3 * 2) {
        uVar2 = uVar3 * 2;
      }
      if (uVar2 < 0x17) {
        uVar3 = 0x17;
      }
      else {
        uVar3 = (uVar2 & 0xfffffffffffffff8) + 8;
        if ((uVar2 | 7) != 0x17) {
          uVar3 = uVar2 | 7;
        }
        uVar3 = uVar3 + 1;
      }
    }
    else {
      uVar3 = 0xfffffffffffffff7;
    }
    __s = (byte *)_Znwm(uVar3);
    if ((uVar1 & 1) != 0) {
      _ZdlPv(__ptr);
    }
    param_1[1] = 0;
    param_1[2] = (ulong)__s;
    *param_1 = uVar3 | 1;
LAB_00bf1be8:
    memset(__s,param_3,param_2);
    if ((*param_1 & 1) == 0) {
LAB_00bf1b98:
      *(byte *)param_1 = (byte)((int)param_2 << 1);
      goto LAB_00bf1c04;
    }
  }
  else {
    __s = (byte *)param_1[2];
    if ((uVar2 & 1) == 0) {
      __s = (byte *)((long)param_1 + 1);
    }
    if (param_2 != 0) goto LAB_00bf1be8;
    if ((uVar2 & 1) == 0) goto LAB_00bf1b98;
  }
  param_1[1] = param_2;
LAB_00bf1c04:
  __s[param_2] = 0;
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf1aec"></a> `00bf1aec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf1af0"></a> `00bf1af0` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bf1af4"></a> `00bf1af4` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf1af8"></a> `00bf1af8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf1afc"></a> `00bf1afc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf1b00"></a> `00bf1b00` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf1b04"></a> `00bf1b04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bf1b08"></a> `00bf1b08` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bf1b0c"></a> `00bf1b0c` | `19 00 40 39` | ldrb w25,[x0] | `FALL_THROUGH`
<a id="insn-00bf1b10"></a> `00bf1b10` | `ca 02 80 52` | mov w10,#0x16 | `FALL_THROUGH`
<a id="insn-00bf1b14"></a> `00bf1b14` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bf1b18"></a> `00bf1b18` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bf1b1c"></a> `00bf1b1c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bf1b20"></a> `00bf1b20` | `09 f9 7f 92` | and x9,x8,#-0x2 | `FALL_THROUGH`
<a id="insn-00bf1b24"></a> `00bf1b24` | `3f 03 00 72` | tst w25,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1b28"></a> `00bf1b28` | `08 1d 00 12` | and w8,w8,#0xff | `FALL_THROUGH`
<a id="insn-00bf1b2c"></a> `00bf1b2c` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1b30"></a> `00bf1b30` | `49 01 89 9a` | csel x9,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bf1b34"></a> `00bf1b34` | `2a 00 09 eb` | subs x10,x1,x9 | `FALL_THROUGH`
<a id="insn-00bf1b38"></a> `00bf1b38` | `69 02 00 54` | b.ls 0x00bf1b84 | `CONDITIONAL_JUMP`
<a id="insn-00bf1b3c"></a> `00bf1b3c` | `0b 01 80 92` | mov x11,#-0x9 | `FALL_THROUGH`
<a id="insn-00bf1b40"></a> `00bf1b40` | `6b 01 09 cb` | sub x11,x11,x9 | `FALL_THROUGH`
<a id="insn-00bf1b44"></a> `00bf1b44` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bf1b48"></a> `00bf1b48` | `03 07 00 54` | b.cc 0x00bf1c28 | `CONDITIONAL_JUMP`
<a id="insn-00bf1b4c"></a> `00bf1b4c` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bf1b50"></a> `00bf1b50` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1b54"></a> `00bf1b54` | `a8 01 80 92` | mov x8,#-0xe | `FALL_THROUGH`
<a id="insn-00bf1b58"></a> `00bf1b58` | `e8 ff ef f2` | movk x8,#0x7fff, LSL #48 | `FALL_THROUGH`
<a id="insn-00bf1b5c"></a> `00bf1b5c` | `57 15 93 9a` | csinc x23,x10,x19,ne | `FALL_THROUGH`
<a id="insn-00bf1b60"></a> `00bf1b60` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bf1b64"></a> `00bf1b64` | `08 02 00 54` | b.hi 0x00bf1ba4 | `CONDITIONAL_JUMP`
<a id="insn-00bf1b68"></a> `00bf1b68` | `28 f9 7f d3` | lsl x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1b6c"></a> `00bf1b6c` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bf1b70"></a> `00bf1b70` | `88 82 88 9a` | csel x8,x20,x8,hi | `FALL_THROUGH`
<a id="insn-00bf1b74"></a> `00bf1b74` | `1f 5d 00 f1` | cmp x8,#0x17 | `FALL_THROUGH`
<a id="insn-00bf1b78"></a> `00bf1b78` | `a2 01 00 54` | b.cs 0x00bf1bac | `CONDITIONAL_JUMP`
<a id="insn-00bf1b7c"></a> `00bf1b7c` | `f8 02 80 52` | mov w24,#0x17 | `FALL_THROUGH`
<a id="insn-00bf1b80"></a> `00bf1b80` | `11 00 00 14` | b 0x00bf1bc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf1b84"></a> `00bf1b84` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bf1b88"></a> `00bf1b88` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1b8c"></a> `00bf1b8c` | `36 15 93 9a` | csinc x22,x9,x19,ne | `FALL_THROUGH`
<a id="insn-00bf1b90"></a> `00bf1b90` | `d4 02 00 b5` | cbnz x20,0x00bf1be8 | `CONDITIONAL_JUMP`
<a id="insn-00bf1b94"></a> `00bf1b94` | `68 03 00 37` | tbnz w8,#0x0,0x00bf1c00 | `CONDITIONAL_JUMP`
<a id="insn-00bf1b98"></a> `00bf1b98` | `88 7a 1f 53` | lsl w8,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1b9c"></a> `00bf1b9c` | `68 02 00 39` | strb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bf1ba0"></a> `00bf1ba0` | `19 00 00 14` | b 0x00bf1c04 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf1ba4"></a> `00bf1ba4` | `18 01 80 92` | mov x24,#-0x9 | `FALL_THROUGH`
<a id="insn-00bf1ba8"></a> `00bf1ba8` | `07 00 00 14` | b 0x00bf1bc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf1bac"></a> `00bf1bac` | `09 f1 7d 92` | and x9,x8,#-0x8 | `FALL_THROUGH`
<a id="insn-00bf1bb0"></a> `00bf1bb0` | `08 09 40 b2` | orr x8,x8,#0x7 | `FALL_THROUGH`
<a id="insn-00bf1bb4"></a> `00bf1bb4` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bf1bb8"></a> `00bf1bb8` | `1f 5d 00 f1` | cmp x8,#0x17 | `FALL_THROUGH`
<a id="insn-00bf1bbc"></a> `00bf1bbc` | `28 01 88 9a` | csel x8,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00bf1bc0"></a> `00bf1bc0` | `18 05 00 91` | add x24,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1bc4"></a> `00bf1bc4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bf1bc8"></a> `00bf1bc8` | `e6 98 01 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bf1bcc"></a> `00bf1bcc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bf1bd0"></a> `00bf1bd0` | `79 00 00 36` | tbz w25,#0x0,0x00bf1bdc | `CONDITIONAL_JUMP`
<a id="insn-00bf1bd4"></a> `00bf1bd4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bf1bd8"></a> `00bf1bd8` | `ea 98 01 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bf1bdc"></a> `00bf1bdc` | `08 03 40 b2` | orr x8,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00bf1be0"></a> `00bf1be0` | `7f da 00 a9` | stp xzr,x22,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bf1be4"></a> `00bf1be4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bf1be8"></a> `00bf1be8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bf1bec"></a> `00bf1bec` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00bf1bf0"></a> `00bf1bf0` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bf1bf4"></a> `00bf1bf4` | `5b 99 01 94` | bl 0x00c58160 | `UNCONDITIONAL_CALL`
<a id="insn-00bf1bf8"></a> `00bf1bf8` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00bf1bfc"></a> `00bf1bfc` | `e8 fc 07 36` | tbz w8,#0x0,0x00bf1b98 | `CONDITIONAL_JUMP`
<a id="insn-00bf1c00"></a> `00bf1c00` | `74 06 00 f9` | str x20,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bf1c04"></a> `00bf1c04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bf1c08"></a> `00bf1c08` | `df 6a 34 38` | strb wzr,[x22, x20, LSL ] | `FALL_THROUGH`
<a id="insn-00bf1c0c"></a> `00bf1c0c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf1c10"></a> `00bf1c10` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bf1c14"></a> `00bf1c14` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf1c18"></a> `00bf1c18` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bf1c1c"></a> `00bf1c1c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bf1c20"></a> `00bf1c20` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf1c24"></a> `00bf1c24` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf1c28"></a> `00bf1c28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bf1c2c"></a> `00bf1c2c` | `de 26 e1 97` | bl 0x0043b7a4 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf1aec`](#insn-00bf1aec) 範囲 `[['00bf1aec', '00bf1b3b']]`
  - `CONDITIONAL_JUMP` [`00bf1b38`](#insn-00bf1b38) → [`00bf1b84`](#insn-00bf1b84)
  - `FALL_THROUGH` [`00bf1b38`](#insn-00bf1b38) → [`00bf1b3c`](#insn-00bf1b3c)
- ブロック [`00bf1b3c`](#insn-00bf1b3c) 範囲 `[['00bf1b3c', '00bf1b4b']]`
  - `CONDITIONAL_JUMP` [`00bf1b48`](#insn-00bf1b48) → [`00bf1c28`](#insn-00bf1c28)
  - `FALL_THROUGH` [`00bf1b48`](#insn-00bf1b48) → [`00bf1b4c`](#insn-00bf1b4c)
- ブロック [`00bf1b4c`](#insn-00bf1b4c) 範囲 `[['00bf1b4c', '00bf1b67']]`
  - `CONDITIONAL_JUMP` [`00bf1b64`](#insn-00bf1b64) → [`00bf1ba4`](#insn-00bf1ba4)
  - `FALL_THROUGH` [`00bf1b64`](#insn-00bf1b64) → [`00bf1b68`](#insn-00bf1b68)
- ブロック [`00bf1b68`](#insn-00bf1b68) 範囲 `[['00bf1b68', '00bf1b7b']]`
  - `CONDITIONAL_JUMP` [`00bf1b78`](#insn-00bf1b78) → [`00bf1bac`](#insn-00bf1bac)
  - `FALL_THROUGH` [`00bf1b78`](#insn-00bf1b78) → [`00bf1b7c`](#insn-00bf1b7c)
- ブロック [`00bf1b7c`](#insn-00bf1b7c) 範囲 `[['00bf1b7c', '00bf1b83']]`
  - `UNCONDITIONAL_JUMP` [`00bf1b80`](#insn-00bf1b80) → [`00bf1bc4`](#insn-00bf1bc4)
- ブロック [`00bf1b84`](#insn-00bf1b84) 範囲 `[['00bf1b84', '00bf1b93']]`
  - `CONDITIONAL_JUMP` [`00bf1b90`](#insn-00bf1b90) → [`00bf1be8`](#insn-00bf1be8)
  - `FALL_THROUGH` [`00bf1b90`](#insn-00bf1b90) → [`00bf1b94`](#insn-00bf1b94)
- ブロック [`00bf1b94`](#insn-00bf1b94) 範囲 `[['00bf1b94', '00bf1b97']]`
  - `CONDITIONAL_JUMP` [`00bf1b94`](#insn-00bf1b94) → [`00bf1c00`](#insn-00bf1c00)
  - `FALL_THROUGH` [`00bf1b94`](#insn-00bf1b94) → [`00bf1b98`](#insn-00bf1b98)
- ブロック [`00bf1b98`](#insn-00bf1b98) 範囲 `[['00bf1b98', '00bf1ba3']]`
  - `UNCONDITIONAL_JUMP` [`00bf1ba0`](#insn-00bf1ba0) → [`00bf1c04`](#insn-00bf1c04)
- ブロック [`00bf1ba4`](#insn-00bf1ba4) 範囲 `[['00bf1ba4', '00bf1bab']]`
  - `UNCONDITIONAL_JUMP` [`00bf1ba8`](#insn-00bf1ba8) → [`00bf1bc4`](#insn-00bf1bc4)
- ブロック [`00bf1bac`](#insn-00bf1bac) 範囲 `[['00bf1bac', '00bf1bc3']]`
  - `FALL_THROUGH` [`00bf1bc0`](#insn-00bf1bc0) → [`00bf1bc4`](#insn-00bf1bc4)
- ブロック [`00bf1bc4`](#insn-00bf1bc4) 範囲 `[['00bf1bc4', '00bf1bd3']]`
  - `CONDITIONAL_JUMP` [`00bf1bd0`](#insn-00bf1bd0) → [`00bf1bdc`](#insn-00bf1bdc)
  - `FALL_THROUGH` [`00bf1bd0`](#insn-00bf1bd0) → [`00bf1bd4`](#insn-00bf1bd4)
- ブロック [`00bf1bd4`](#insn-00bf1bd4) 範囲 `[['00bf1bd4', '00bf1bdb']]`
  - `FALL_THROUGH` [`00bf1bd8`](#insn-00bf1bd8) → [`00bf1bdc`](#insn-00bf1bdc)
- ブロック [`00bf1bdc`](#insn-00bf1bdc) 範囲 `[['00bf1bdc', '00bf1be7']]`
  - `FALL_THROUGH` [`00bf1be4`](#insn-00bf1be4) → [`00bf1be8`](#insn-00bf1be8)
- ブロック [`00bf1be8`](#insn-00bf1be8) 範囲 `[['00bf1be8', '00bf1bff']]`
  - `CONDITIONAL_JUMP` [`00bf1bfc`](#insn-00bf1bfc) → [`00bf1b98`](#insn-00bf1b98)
  - `FALL_THROUGH` [`00bf1bfc`](#insn-00bf1bfc) → [`00bf1c00`](#insn-00bf1c00)
- ブロック [`00bf1c00`](#insn-00bf1c00) 範囲 `[['00bf1c00', '00bf1c03']]`
  - `FALL_THROUGH` [`00bf1c00`](#insn-00bf1c00) → [`00bf1c04`](#insn-00bf1c04)
- ブロック [`00bf1c04`](#insn-00bf1c04) 範囲 `[['00bf1c04', '00bf1c27']]`
- ブロック [`00bf1c28`](#insn-00bf1c28) 範囲 `[['00bf1c28', '00bf1c2f']]`

## 命令位置別の参照

- [`00bf1af0`](#insn-00bf1af0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1af4`](#insn-00bf1af4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1af8`](#insn-00bf1af8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1afc`](#insn-00bf1afc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1b00`](#insn-00bf1b00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1b38`](#insn-00bf1b38) → [`00bf1b84`](#insn-00bf1b84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1b48`](#insn-00bf1b48) → [`00bf1c28`](#insn-00bf1c28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1b64`](#insn-00bf1b64) → [`00bf1ba4`](#insn-00bf1ba4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1b78`](#insn-00bf1b78) → [`00bf1bac`](#insn-00bf1bac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1b80`](#insn-00bf1b80) → [`00bf1bc4`](#insn-00bf1bc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1b90`](#insn-00bf1b90) → [`00bf1be8`](#insn-00bf1be8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1b94`](#insn-00bf1b94) → [`00bf1c00`](#insn-00bf1c00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1ba0`](#insn-00bf1ba0) → [`00bf1c04`](#insn-00bf1c04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1ba8`](#insn-00bf1ba8) → [`00bf1bc4`](#insn-00bf1bc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1bc8`](#insn-00bf1bc8) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bf1bd0`](#insn-00bf1bd0) → [`00bf1bdc`](#insn-00bf1bdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1bd8`](#insn-00bf1bd8) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bf1bf4`](#insn-00bf1bf4) → [`00c58160`](../00c58/00c58160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58160` · 推定シンボル `None` · 推定型 `None`
- [`00bf1bfc`](#insn-00bf1bfc) → [`00bf1b98`](#insn-00bf1b98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c0c`](#insn-00bf1c0c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c10`](#insn-00bf1c10) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c14`](#insn-00bf1c14) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c18`](#insn-00bf1c18) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c1c`](#insn-00bf1c1c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf1c2c`](#insn-00bf1c2c) → [`0043b7a4`](../0043b/0043b7a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043b7a4` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf1af0`](#insn-00bf1af0)

~~~json
{
  "source": "00bf1af0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1af4`](#insn-00bf1af4)

~~~json
{
  "source": "00bf1af4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1af8`](#insn-00bf1af8)

~~~json
{
  "source": "00bf1af8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1afc`](#insn-00bf1afc)

~~~json
{
  "source": "00bf1afc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1b00`](#insn-00bf1b00)

~~~json
{
  "source": "00bf1b00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1b38`](#insn-00bf1b38)

~~~json
{
  "source": "00bf1b38",
  "target": "00bf1b84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1b48`](#insn-00bf1b48)

~~~json
{
  "source": "00bf1b48",
  "target": "00bf1c28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1b64`](#insn-00bf1b64)

~~~json
{
  "source": "00bf1b64",
  "target": "00bf1ba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1b78`](#insn-00bf1b78)

~~~json
{
  "source": "00bf1b78",
  "target": "00bf1bac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1b80`](#insn-00bf1b80)

~~~json
{
  "source": "00bf1b80",
  "target": "00bf1bc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1b90`](#insn-00bf1b90)

~~~json
{
  "source": "00bf1b90",
  "target": "00bf1be8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1b94`](#insn-00bf1b94)

~~~json
{
  "source": "00bf1b94",
  "target": "00bf1c00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1ba0`](#insn-00bf1ba0)

~~~json
{
  "source": "00bf1ba0",
  "target": "00bf1c04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1ba8`](#insn-00bf1ba8)

~~~json
{
  "source": "00bf1ba8",
  "target": "00bf1bc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1bc8`](#insn-00bf1bc8)

~~~json
{
  "source": "00bf1bc8",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf1bd0`](#insn-00bf1bd0)

~~~json
{
  "source": "00bf1bd0",
  "target": "00bf1bdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1bd8`](#insn-00bf1bd8)

~~~json
{
  "source": "00bf1bd8",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf1bf4`](#insn-00bf1bf4)

~~~json
{
  "source": "00bf1bf4",
  "target": "00c58160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf1bfc`](#insn-00bf1bfc)

~~~json
{
  "source": "00bf1bfc",
  "target": "00bf1b98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c0c`](#insn-00bf1c0c)

~~~json
{
  "source": "00bf1c0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c10`](#insn-00bf1c10)

~~~json
{
  "source": "00bf1c10",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c14`](#insn-00bf1c14)

~~~json
{
  "source": "00bf1c14",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c18`](#insn-00bf1c18)

~~~json
{
  "source": "00bf1c18",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c1c`](#insn-00bf1c1c)

~~~json
{
  "source": "00bf1c1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf1c2c`](#insn-00bf1c2c)

~~~json
{
  "source": "00bf1c2c",
  "target": "0043b7a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
