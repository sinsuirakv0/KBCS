# 00abceb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00abccb8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00abc/00abccb8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-ac067c6849500c36bcde454e8bb2520d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00abcf24`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00abc/00abcf24.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-e8959fa294605869a512856e74de8959)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abceb4",
  "name": "FUN_00abceb4",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "53c07d8d6994f238979e2160b6c4fb7ba453d513b55f1713c7bc305ee1223df3",
  "source_text_sha256": "53c07d8d6994f238979e2160b6c4fb7ba453d513b55f1713c7bc305ee1223df3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abceb4",
        "00abd00f"
      ]
    ],
    "bytes_sha256": "09a499d9cb7d7373d3ea948cc94544ad2b1b75b06f7467809881714e0d450e82",
    "instruction_count": 87,
    "instruction_bytes": 348,
    "body_bytes": 348,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00abc8d8](../00abc/00abc8d8.md)

## 呼び出し先

- [00800378](../00800/00800378.md)
- [0080062c](../00800/0080062c.md)
- [008056ec](../00805/008056ec.md)
- [008514f8](../00851/008514f8.md)
- [00a65dec](../00a65/00a65dec.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1548 bytes

~~~c

bool FUN_00abceb4(long param_1,undefined4 param_2)

{
  byte *pbVar1;
  uint uVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  long lVar8;
  bool bVar9;
  long lVar10;
  
  iVar3 = FUN_00800378(param_2);
  iVar4 = FUN_0080062c(param_2);
  iVar5 = *(int *)(param_1 + 0x68);
  if (iVar5 == -1) {
    iVar5 = FUN_008056ec(iVar3,iVar4);
    iVar5 = iVar5 + -1;
  }
  iVar5 = FUN_00a65dec(iVar3,iVar4,iVar5,*(undefined4 *)(param_1 + 0x70),0);
  if (iVar5 == 0) {
LAB_00abcf5c:
    bVar9 = false;
  }
  else {
    if (*(int *)(param_1 + 0x6c) == -1) {
      return true;
    }
    if (*(int *)(param_1 + 0x68) != -1) {
      return true;
    }
    if (iVar3 == -7) {
      iVar4 = iVar4 + 7;
    }
    else if (iVar3 != -2) {
      if (iVar3 != -3) goto LAB_00abcf5c;
      iVar4 = iVar4 + 4;
    }
    FUN_008514f8();
    lVar10 = 0x30;
    lVar8 = (long)iVar4 * 200 + 0xd443;
    do {
      lVar6 = FUN_008514f8();
      lVar7 = lVar6 + (long)iVar4 * 200;
      pbVar1 = (byte *)(lVar6 + lVar8);
      uVar2 = (uint)(*(byte *)(lVar7 + 0xd506) ^ pbVar1[-1]) << 0x10 |
              (uint)(*(byte *)(lVar7 + 0xd507) ^ *pbVar1) << 0x18 |
              (uint)(*(byte *)(lVar7 + 0xd505) ^ pbVar1[-2]) << 8 |
              (uint)(*(byte *)(lVar7 + 0xd504) ^ pbVar1[-3]);
      bVar9 = *(int *)(param_1 + 0x6c) < (int)uVar2;
      if ((int)uVar2 <= *(int *)(param_1 + 0x6c)) {
        return bVar9;
      }
      FUN_008514f8();
      lVar10 = lVar10 + -1;
      lVar8 = lVar8 + 4;
    } while (lVar10 != 0);
  }
  return bVar9;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abceb4"></a> `00abceb4` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00abceb8"></a> `00abceb8` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abcebc"></a> `00abcebc` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abcec0"></a> `00abcec0` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abcec4"></a> `00abcec4` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abcec8"></a> `00abcec8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abcecc"></a> `00abcecc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abced0"></a> `00abced0` | `e0 03 01 2a` | mov w0,w1 | `FALL_THROUGH`
<a id="insn-00abced4"></a> `00abced4` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00abced8"></a> `00abced8` | `28 0d f5 97` | bl 0x00800378 | `UNCONDITIONAL_CALL`
<a id="insn-00abcedc"></a> `00abcedc` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00abcee0"></a> `00abcee0` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00abcee4"></a> `00abcee4` | `d2 0d f5 97` | bl 0x0080062c | `UNCONDITIONAL_CALL`
<a id="insn-00abcee8"></a> `00abcee8` | `62 6a 40 b9` | ldr w2,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00abceec"></a> `00abceec` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abcef0"></a> `00abcef0` | `5f 04 00 31` | cmn w2,#0x1 | `FALL_THROUGH`
<a id="insn-00abcef4"></a> `00abcef4` | `a1 00 00 54` | b.ne 0x00abcf08 | `CONDITIONAL_JUMP`
<a id="insn-00abcef8"></a> `00abcef8` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00abcefc"></a> `00abcefc` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abcf00"></a> `00abcf00` | `fb 21 f5 97` | bl 0x008056ec | `UNCONDITIONAL_CALL`
<a id="insn-00abcf04"></a> `00abcf04` | `02 04 00 51` | sub w2,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00abcf08"></a> `00abcf08` | `63 72 40 b9` | ldr w3,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00abcf0c"></a> `00abcf0c` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00abcf10"></a> `00abcf10` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abcf14"></a> `00abcf14` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00abcf18"></a> `00abcf18` | `b5 a3 fe 97` | bl 0x00a65dec | `UNCONDITIONAL_CALL`
<a id="insn-00abcf1c"></a> `00abcf1c` | `00 02 00 34` | cbz w0,0x00abcf5c | `CONDITIONAL_JUMP`
<a id="insn-00abcf20"></a> `00abcf20` | `68 6e 40 b9` | ldr w8,[x19, #0x6c] | `FALL_THROUGH`
<a id="insn-00abcf24"></a> `00abcf24` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-00abcf28"></a> `00abcf28` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abcf2c"></a> `00abcf2c` | `40 06 00 54` | b.eq 0x00abcff4 | `CONDITIONAL_JUMP`
<a id="insn-00abcf30"></a> `00abcf30` | `68 6a 40 b9` | ldr w8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00abcf34"></a> `00abcf34` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abcf38"></a> `00abcf38` | `e1 05 00 54` | b.ne 0x00abcff4 | `CONDITIONAL_JUMP`
<a id="insn-00abcf3c"></a> `00abcf3c` | `bf 1e 00 31` | cmn w21,#0x7 | `FALL_THROUGH`
<a id="insn-00abcf40"></a> `00abcf40` | `20 01 00 54` | b.eq 0x00abcf64 | `CONDITIONAL_JUMP`
<a id="insn-00abcf44"></a> `00abcf44` | `bf 0a 00 31` | cmn w21,#0x2 | `FALL_THROUGH`
<a id="insn-00abcf48"></a> `00abcf48` | `00 01 00 54` | b.eq 0x00abcf68 | `CONDITIONAL_JUMP`
<a id="insn-00abcf4c"></a> `00abcf4c` | `bf 0e 00 31` | cmn w21,#0x3 | `FALL_THROUGH`
<a id="insn-00abcf50"></a> `00abcf50` | `61 00 00 54` | b.ne 0x00abcf5c | `CONDITIONAL_JUMP`
<a id="insn-00abcf54"></a> `00abcf54` | `94 12 00 11` | add w20,w20,#0x4 | `FALL_THROUGH`
<a id="insn-00abcf58"></a> `00abcf58` | `04 00 00 14` | b 0x00abcf68 | `UNCONDITIONAL_JUMP`
<a id="insn-00abcf5c"></a> `00abcf5c` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00abcf60"></a> `00abcf60` | `25 00 00 14` | b 0x00abcff4 | `UNCONDITIONAL_JUMP`
<a id="insn-00abcf64"></a> `00abcf64` | `94 1e 00 11` | add w20,w20,#0x7 | `FALL_THROUGH`
<a id="insn-00abcf68"></a> `00abcf68` | `95 7e 40 93` | sxtw x21,w20 | `FALL_THROUGH`
<a id="insn-00abcf6c"></a> `00abcf6c` | `63 51 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00abcf70"></a> `00abcf70` | `17 19 80 52` | mov w23,#0xc8 | `FALL_THROUGH`
<a id="insn-00abcf74"></a> `00abcf74` | `68 88 9a 52` | mov w8,#0xd443 | `FALL_THROUGH`
<a id="insn-00abcf78"></a> `00abcf78` | `18 06 80 52` | mov w24,#0x30 | `FALL_THROUGH`
<a id="insn-00abcf7c"></a> `00abcf7c` | `94 22 37 9b` | smaddl x20,w20,w23,x8 | `FALL_THROUGH`
<a id="insn-00abcf80"></a> `00abcf80` | `19 88 9a 52` | mov w25,#0xd440 | `FALL_THROUGH`
<a id="insn-00abcf84"></a> `00abcf84` | `5d 51 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00abcf88"></a> `00abcf88` | `a8 02 37 9b` | smaddl x8,w21,w23,x0 | `FALL_THROUGH`
<a id="insn-00abcf8c"></a> `00abcf8c` | `09 00 14 8b` | add x9,x0,x20 | `FALL_THROUGH`
<a id="insn-00abcf90"></a> `00abcf90` | `2a f1 5f 38` | ldurb w10,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-00abcf94"></a> `00abcf94` | `2d e1 5f 38` | ldurb w13,[x9, #-0x2] | `FALL_THROUGH`
<a id="insn-00abcf98"></a> `00abcf98` | `08 01 19 8b` | add x8,x8,x25 | `FALL_THROUGH`
<a id="insn-00abcf9c"></a> `00abcf9c` | `0b 19 43 39` | ldrb w11,[x8, #0xc6] | `FALL_THROUGH`
<a id="insn-00abcfa0"></a> `00abcfa0` | `0c 1d 43 39` | ldrb w12,[x8, #0xc7] | `FALL_THROUGH`
<a id="insn-00abcfa4"></a> `00abcfa4` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00abcfa8"></a> `00abcfa8` | `2b 01 40 39` | ldrb w11,[x9] | `FALL_THROUGH`
<a id="insn-00abcfac"></a> `00abcfac` | `29 d1 5f 38` | ldurb w9,[x9, #-0x3] | `FALL_THROUGH`
<a id="insn-00abcfb0"></a> `00abcfb0` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00abcfb4"></a> `00abcfb4` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00abcfb8"></a> `00abcfb8` | `0c 15 43 39` | ldrb w12,[x8, #0xc5] | `FALL_THROUGH`
<a id="insn-00abcfbc"></a> `00abcfbc` | `08 11 43 39` | ldrb w8,[x8, #0xc4] | `FALL_THROUGH`
<a id="insn-00abcfc0"></a> `00abcfc0` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00abcfc4"></a> `00abcfc4` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00abcfc8"></a> `00abcfc8` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00abcfcc"></a> `00abcfcc` | `69 6e 40 b9` | ldr w9,[x19, #0x6c] | `FALL_THROUGH`
<a id="insn-00abcfd0"></a> `00abcfd0` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00abcfd4"></a> `00abcfd4` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00abcfd8"></a> `00abcfd8` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00abcfdc"></a> `00abcfdc` | `f6 d7 9f 1a` | cset w22,gt | `FALL_THROUGH`
<a id="insn-00abcfe0"></a> `00abcfe0` | `ad 00 00 54` | b.le 0x00abcff4 | `CONDITIONAL_JUMP`
<a id="insn-00abcfe4"></a> `00abcfe4` | `45 51 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00abcfe8"></a> `00abcfe8` | `18 07 00 f1` | subs x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00abcfec"></a> `00abcfec` | `94 12 00 91` | add x20,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00abcff0"></a> `00abcff0` | `a1 fc ff 54` | b.ne 0x00abcf84 | `CONDITIONAL_JUMP`
<a id="insn-00abcff4"></a> `00abcff4` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00abcff8"></a> `00abcff8` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abcffc"></a> `00abcffc` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abd000"></a> `00abd000` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abd004"></a> `00abd004` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abd008"></a> `00abd008` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00abd00c"></a> `00abd00c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abceb4`](#insn-00abceb4) 範囲 `[['00abceb4', '00abcef7']]`
  - `CONDITIONAL_JUMP` [`00abcef4`](#insn-00abcef4) → [`00abcf08`](#insn-00abcf08)
  - `FALL_THROUGH` [`00abcef4`](#insn-00abcef4) → [`00abcef8`](#insn-00abcef8)
- ブロック [`00abcef8`](#insn-00abcef8) 範囲 `[['00abcef8', '00abcf07']]`
  - `FALL_THROUGH` [`00abcf04`](#insn-00abcf04) → [`00abcf08`](#insn-00abcf08)
- ブロック [`00abcf08`](#insn-00abcf08) 範囲 `[['00abcf08', '00abcf1f']]`
  - `CONDITIONAL_JUMP` [`00abcf1c`](#insn-00abcf1c) → [`00abcf5c`](#insn-00abcf5c)
  - `FALL_THROUGH` [`00abcf1c`](#insn-00abcf1c) → [`00abcf20`](#insn-00abcf20)
- ブロック [`00abcf20`](#insn-00abcf20) 範囲 `[['00abcf20', '00abcf2f']]`
  - `CONDITIONAL_JUMP` [`00abcf2c`](#insn-00abcf2c) → [`00abcff4`](#insn-00abcff4)
  - `FALL_THROUGH` [`00abcf2c`](#insn-00abcf2c) → [`00abcf30`](#insn-00abcf30)
- ブロック [`00abcf30`](#insn-00abcf30) 範囲 `[['00abcf30', '00abcf3b']]`
  - `CONDITIONAL_JUMP` [`00abcf38`](#insn-00abcf38) → [`00abcff4`](#insn-00abcff4)
  - `FALL_THROUGH` [`00abcf38`](#insn-00abcf38) → [`00abcf3c`](#insn-00abcf3c)
- ブロック [`00abcf3c`](#insn-00abcf3c) 範囲 `[['00abcf3c', '00abcf43']]`
  - `CONDITIONAL_JUMP` [`00abcf40`](#insn-00abcf40) → [`00abcf64`](#insn-00abcf64)
  - `FALL_THROUGH` [`00abcf40`](#insn-00abcf40) → [`00abcf44`](#insn-00abcf44)
- ブロック [`00abcf44`](#insn-00abcf44) 範囲 `[['00abcf44', '00abcf4b']]`
  - `CONDITIONAL_JUMP` [`00abcf48`](#insn-00abcf48) → [`00abcf68`](#insn-00abcf68)
  - `FALL_THROUGH` [`00abcf48`](#insn-00abcf48) → [`00abcf4c`](#insn-00abcf4c)
- ブロック [`00abcf4c`](#insn-00abcf4c) 範囲 `[['00abcf4c', '00abcf53']]`
  - `CONDITIONAL_JUMP` [`00abcf50`](#insn-00abcf50) → [`00abcf5c`](#insn-00abcf5c)
  - `FALL_THROUGH` [`00abcf50`](#insn-00abcf50) → [`00abcf54`](#insn-00abcf54)
- ブロック [`00abcf54`](#insn-00abcf54) 範囲 `[['00abcf54', '00abcf5b']]`
  - `UNCONDITIONAL_JUMP` [`00abcf58`](#insn-00abcf58) → [`00abcf68`](#insn-00abcf68)
- ブロック [`00abcf5c`](#insn-00abcf5c) 範囲 `[['00abcf5c', '00abcf63']]`
  - `UNCONDITIONAL_JUMP` [`00abcf60`](#insn-00abcf60) → [`00abcff4`](#insn-00abcff4)
- ブロック [`00abcf64`](#insn-00abcf64) 範囲 `[['00abcf64', '00abcf67']]`
  - `FALL_THROUGH` [`00abcf64`](#insn-00abcf64) → [`00abcf68`](#insn-00abcf68)
- ブロック [`00abcf68`](#insn-00abcf68) 範囲 `[['00abcf68', '00abcf83']]`
  - `FALL_THROUGH` [`00abcf80`](#insn-00abcf80) → [`00abcf84`](#insn-00abcf84)
- ブロック [`00abcf84`](#insn-00abcf84) 範囲 `[['00abcf84', '00abcfe3']]`
  - `CONDITIONAL_JUMP` [`00abcfe0`](#insn-00abcfe0) → [`00abcff4`](#insn-00abcff4)
  - `FALL_THROUGH` [`00abcfe0`](#insn-00abcfe0) → [`00abcfe4`](#insn-00abcfe4)
- ブロック [`00abcfe4`](#insn-00abcfe4) 範囲 `[['00abcfe4', '00abcff3']]`
  - `CONDITIONAL_JUMP` [`00abcff0`](#insn-00abcff0) → [`00abcf84`](#insn-00abcf84)
  - `FALL_THROUGH` [`00abcff0`](#insn-00abcff0) → [`00abcff4`](#insn-00abcff4)
- ブロック [`00abcff4`](#insn-00abcff4) 範囲 `[['00abcff4', '00abd00f']]`

## 命令位置別の参照

- [`00abceb4`](#insn-00abceb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abceb8`](#insn-00abceb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcebc`](#insn-00abcebc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcec0`](#insn-00abcec0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcec4`](#insn-00abcec4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abced8`](#insn-00abced8) → [`00800378`](../00800/00800378.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00800378` · 推定シンボル `None` · 推定型 `None`
- [`00abcee4`](#insn-00abcee4) → [`0080062c`](../00800/0080062c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0080062c` · 推定シンボル `None` · 推定型 `None`
- [`00abcef4`](#insn-00abcef4) → [`00abcf08`](#insn-00abcf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcf00`](#insn-00abcf00) → [`008056ec`](../00805/008056ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008056ec` · 推定シンボル `None` · 推定型 `None`
- [`00abcf18`](#insn-00abcf18) → [`00a65dec`](../00a65/00a65dec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a65dec` · 推定シンボル `None` · 推定型 `None`
- [`00abcf1c`](#insn-00abcf1c) → [`00abcf5c`](#insn-00abcf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcf2c`](#insn-00abcf2c) → [`00abcff4`](#insn-00abcff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcf38`](#insn-00abcf38) → [`00abcff4`](#insn-00abcff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcf40`](#insn-00abcf40) → [`00abcf64`](#insn-00abcf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcf48`](#insn-00abcf48) → [`00abcf68`](#insn-00abcf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcf50`](#insn-00abcf50) → [`00abcf5c`](#insn-00abcf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcf58`](#insn-00abcf58) → [`00abcf68`](#insn-00abcf68) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcf60`](#insn-00abcf60) → [`00abcff4`](#insn-00abcff4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcf6c`](#insn-00abcf6c) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00abcf84`](#insn-00abcf84) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00abcfe0`](#insn-00abcfe0) → [`00abcff4`](#insn-00abcff4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcfe4`](#insn-00abcfe4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00abcff0`](#insn-00abcff0) → [`00abcf84`](#insn-00abcf84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcff8`](#insn-00abcff8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcffc`](#insn-00abcffc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd000`](#insn-00abd000) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd004`](#insn-00abd004) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abd008`](#insn-00abd008) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abceb4`](#insn-00abceb4)

~~~json
{
  "source": "00abceb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abceb8`](#insn-00abceb8)

~~~json
{
  "source": "00abceb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcebc`](#insn-00abcebc)

~~~json
{
  "source": "00abcebc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcec0`](#insn-00abcec0)

~~~json
{
  "source": "00abcec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcec4`](#insn-00abcec4)

~~~json
{
  "source": "00abcec4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abced8`](#insn-00abced8)

~~~json
{
  "source": "00abced8",
  "target": "00800378",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcee4`](#insn-00abcee4)

~~~json
{
  "source": "00abcee4",
  "target": "0080062c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcef4`](#insn-00abcef4)

~~~json
{
  "source": "00abcef4",
  "target": "00abcf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcf00`](#insn-00abcf00)

~~~json
{
  "source": "00abcf00",
  "target": "008056ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcf18`](#insn-00abcf18)

~~~json
{
  "source": "00abcf18",
  "target": "00a65dec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcf1c`](#insn-00abcf1c)

~~~json
{
  "source": "00abcf1c",
  "target": "00abcf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcf2c`](#insn-00abcf2c)

~~~json
{
  "source": "00abcf2c",
  "target": "00abcff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcf38`](#insn-00abcf38)

~~~json
{
  "source": "00abcf38",
  "target": "00abcff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcf40`](#insn-00abcf40)

~~~json
{
  "source": "00abcf40",
  "target": "00abcf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcf48`](#insn-00abcf48)

~~~json
{
  "source": "00abcf48",
  "target": "00abcf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcf50`](#insn-00abcf50)

~~~json
{
  "source": "00abcf50",
  "target": "00abcf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcf58`](#insn-00abcf58)

~~~json
{
  "source": "00abcf58",
  "target": "00abcf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcf60`](#insn-00abcf60)

~~~json
{
  "source": "00abcf60",
  "target": "00abcff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcf6c`](#insn-00abcf6c)

~~~json
{
  "source": "00abcf6c",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcf84`](#insn-00abcf84)

~~~json
{
  "source": "00abcf84",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcfe0`](#insn-00abcfe0)

~~~json
{
  "source": "00abcfe0",
  "target": "00abcff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcfe4`](#insn-00abcfe4)

~~~json
{
  "source": "00abcfe4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcff0`](#insn-00abcff0)

~~~json
{
  "source": "00abcff0",
  "target": "00abcf84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcff8`](#insn-00abcff8)

~~~json
{
  "source": "00abcff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcffc`](#insn-00abcffc)

~~~json
{
  "source": "00abcffc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd000`](#insn-00abd000)

~~~json
{
  "source": "00abd000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd004`](#insn-00abd004)

~~~json
{
  "source": "00abd004",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abd008`](#insn-00abd008)

~~~json
{
  "source": "00abd008",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
