# 00abccb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a5ed00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ed00.md) · 移動量 `+0x5dfb8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0052.md#compare-1851a3e46036cfad694daaa274315e5b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00abceb4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00abc/00abceb4.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-ac067c6849500c36bcde454e8bb2520d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abccb8",
  "name": "FUN_00abccb8",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6c8205d29d591b250d297ac7a7ed7dadb4349e5ece4746864e6eb3fefb490495",
  "source_text_sha256": "6c8205d29d591b250d297ac7a7ed7dadb4349e5ece4746864e6eb3fefb490495",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abccb8",
        "00abce13"
      ]
    ],
    "bytes_sha256": "7a0ada2326be4b455446b413de5f4ada08ae18e618c77f32b5d1b456874bb57e",
    "instruction_count": 87,
    "instruction_bytes": 348,
    "body_bytes": 348,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00abc6dc](../00abc/00abc6dc.md)

## 呼び出し先

- [00800338](../00800/00800338.md)
- [008005ec](../00800/008005ec.md)
- [008056ac](../00805/008056ac.md)
- [008514b8](../00851/008514b8.md)
- [00a65bf4](../00a65/00a65bf4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1548 bytes

~~~c

bool FUN_00abccb8(long param_1,undefined4 param_2)

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
  
  iVar3 = FUN_00800338(param_2);
  iVar4 = FUN_008005ec(param_2);
  iVar5 = *(int *)(param_1 + 0x68);
  if (iVar5 == -1) {
    iVar5 = FUN_008056ac(iVar3,iVar4);
    iVar5 = iVar5 + -1;
  }
  iVar5 = FUN_00a65bf4(iVar3,iVar4,iVar5,*(undefined4 *)(param_1 + 0x70),0);
  if (iVar5 == 0) {
LAB_00abcd60:
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
      if (iVar3 != -3) goto LAB_00abcd60;
      iVar4 = iVar4 + 4;
    }
    FUN_008514b8();
    lVar10 = 0x30;
    lVar8 = (long)iVar4 * 200 + 0xd443;
    do {
      lVar6 = FUN_008514b8();
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
      FUN_008514b8();
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
<a id="insn-00abccb8"></a> `00abccb8` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00abccbc"></a> `00abccbc` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abccc0"></a> `00abccc0` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abccc4"></a> `00abccc4` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abccc8"></a> `00abccc8` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abcccc"></a> `00abcccc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abccd0"></a> `00abccd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00abccd4"></a> `00abccd4` | `e0 03 01 2a` | mov w0,w1 | `FALL_THROUGH`
<a id="insn-00abccd8"></a> `00abccd8` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00abccdc"></a> `00abccdc` | `97 0d f5 97` | bl 0x00800338 | `UNCONDITIONAL_CALL`
<a id="insn-00abcce0"></a> `00abcce0` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00abcce4"></a> `00abcce4` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00abcce8"></a> `00abcce8` | `41 0e f5 97` | bl 0x008005ec | `UNCONDITIONAL_CALL`
<a id="insn-00abccec"></a> `00abccec` | `62 6a 40 b9` | ldr w2,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00abccf0"></a> `00abccf0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00abccf4"></a> `00abccf4` | `5f 04 00 31` | cmn w2,#0x1 | `FALL_THROUGH`
<a id="insn-00abccf8"></a> `00abccf8` | `a1 00 00 54` | b.ne 0x00abcd0c | `CONDITIONAL_JUMP`
<a id="insn-00abccfc"></a> `00abccfc` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00abcd00"></a> `00abcd00` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abcd04"></a> `00abcd04` | `6a 22 f5 97` | bl 0x008056ac | `UNCONDITIONAL_CALL`
<a id="insn-00abcd08"></a> `00abcd08` | `02 04 00 51` | sub w2,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00abcd0c"></a> `00abcd0c` | `63 72 40 b9` | ldr w3,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00abcd10"></a> `00abcd10` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00abcd14"></a> `00abcd14` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00abcd18"></a> `00abcd18` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00abcd1c"></a> `00abcd1c` | `b6 a3 fe 97` | bl 0x00a65bf4 | `UNCONDITIONAL_CALL`
<a id="insn-00abcd20"></a> `00abcd20` | `00 02 00 34` | cbz w0,0x00abcd60 | `CONDITIONAL_JUMP`
<a id="insn-00abcd24"></a> `00abcd24` | `68 6e 40 b9` | ldr w8,[x19, #0x6c] | `FALL_THROUGH`
<a id="insn-00abcd28"></a> `00abcd28` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-00abcd2c"></a> `00abcd2c` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abcd30"></a> `00abcd30` | `40 06 00 54` | b.eq 0x00abcdf8 | `CONDITIONAL_JUMP`
<a id="insn-00abcd34"></a> `00abcd34` | `68 6a 40 b9` | ldr w8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00abcd38"></a> `00abcd38` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00abcd3c"></a> `00abcd3c` | `e1 05 00 54` | b.ne 0x00abcdf8 | `CONDITIONAL_JUMP`
<a id="insn-00abcd40"></a> `00abcd40` | `bf 1e 00 31` | cmn w21,#0x7 | `FALL_THROUGH`
<a id="insn-00abcd44"></a> `00abcd44` | `20 01 00 54` | b.eq 0x00abcd68 | `CONDITIONAL_JUMP`
<a id="insn-00abcd48"></a> `00abcd48` | `bf 0a 00 31` | cmn w21,#0x2 | `FALL_THROUGH`
<a id="insn-00abcd4c"></a> `00abcd4c` | `00 01 00 54` | b.eq 0x00abcd6c | `CONDITIONAL_JUMP`
<a id="insn-00abcd50"></a> `00abcd50` | `bf 0e 00 31` | cmn w21,#0x3 | `FALL_THROUGH`
<a id="insn-00abcd54"></a> `00abcd54` | `61 00 00 54` | b.ne 0x00abcd60 | `CONDITIONAL_JUMP`
<a id="insn-00abcd58"></a> `00abcd58` | `94 12 00 11` | add w20,w20,#0x4 | `FALL_THROUGH`
<a id="insn-00abcd5c"></a> `00abcd5c` | `04 00 00 14` | b 0x00abcd6c | `UNCONDITIONAL_JUMP`
<a id="insn-00abcd60"></a> `00abcd60` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00abcd64"></a> `00abcd64` | `25 00 00 14` | b 0x00abcdf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00abcd68"></a> `00abcd68` | `94 1e 00 11` | add w20,w20,#0x7 | `FALL_THROUGH`
<a id="insn-00abcd6c"></a> `00abcd6c` | `95 7e 40 93` | sxtw x21,w20 | `FALL_THROUGH`
<a id="insn-00abcd70"></a> `00abcd70` | `d2 51 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abcd74"></a> `00abcd74` | `17 19 80 52` | mov w23,#0xc8 | `FALL_THROUGH`
<a id="insn-00abcd78"></a> `00abcd78` | `68 88 9a 52` | mov w8,#0xd443 | `FALL_THROUGH`
<a id="insn-00abcd7c"></a> `00abcd7c` | `18 06 80 52` | mov w24,#0x30 | `FALL_THROUGH`
<a id="insn-00abcd80"></a> `00abcd80` | `94 22 37 9b` | smaddl x20,w20,w23,x8 | `FALL_THROUGH`
<a id="insn-00abcd84"></a> `00abcd84` | `19 88 9a 52` | mov w25,#0xd440 | `FALL_THROUGH`
<a id="insn-00abcd88"></a> `00abcd88` | `cc 51 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abcd8c"></a> `00abcd8c` | `a8 02 37 9b` | smaddl x8,w21,w23,x0 | `FALL_THROUGH`
<a id="insn-00abcd90"></a> `00abcd90` | `09 00 14 8b` | add x9,x0,x20 | `FALL_THROUGH`
<a id="insn-00abcd94"></a> `00abcd94` | `2a f1 5f 38` | ldurb w10,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-00abcd98"></a> `00abcd98` | `2d e1 5f 38` | ldurb w13,[x9, #-0x2] | `FALL_THROUGH`
<a id="insn-00abcd9c"></a> `00abcd9c` | `08 01 19 8b` | add x8,x8,x25 | `FALL_THROUGH`
<a id="insn-00abcda0"></a> `00abcda0` | `0b 19 43 39` | ldrb w11,[x8, #0xc6] | `FALL_THROUGH`
<a id="insn-00abcda4"></a> `00abcda4` | `0c 1d 43 39` | ldrb w12,[x8, #0xc7] | `FALL_THROUGH`
<a id="insn-00abcda8"></a> `00abcda8` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00abcdac"></a> `00abcdac` | `2b 01 40 39` | ldrb w11,[x9] | `FALL_THROUGH`
<a id="insn-00abcdb0"></a> `00abcdb0` | `29 d1 5f 38` | ldurb w9,[x9, #-0x3] | `FALL_THROUGH`
<a id="insn-00abcdb4"></a> `00abcdb4` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00abcdb8"></a> `00abcdb8` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00abcdbc"></a> `00abcdbc` | `0c 15 43 39` | ldrb w12,[x8, #0xc5] | `FALL_THROUGH`
<a id="insn-00abcdc0"></a> `00abcdc0` | `08 11 43 39` | ldrb w8,[x8, #0xc4] | `FALL_THROUGH`
<a id="insn-00abcdc4"></a> `00abcdc4` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00abcdc8"></a> `00abcdc8` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00abcdcc"></a> `00abcdcc` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00abcdd0"></a> `00abcdd0` | `69 6e 40 b9` | ldr w9,[x19, #0x6c] | `FALL_THROUGH`
<a id="insn-00abcdd4"></a> `00abcdd4` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00abcdd8"></a> `00abcdd8` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00abcddc"></a> `00abcddc` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00abcde0"></a> `00abcde0` | `f6 d7 9f 1a` | cset w22,gt | `FALL_THROUGH`
<a id="insn-00abcde4"></a> `00abcde4` | `ad 00 00 54` | b.le 0x00abcdf8 | `CONDITIONAL_JUMP`
<a id="insn-00abcde8"></a> `00abcde8` | `b4 51 f6 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00abcdec"></a> `00abcdec` | `18 07 00 f1` | subs x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00abcdf0"></a> `00abcdf0` | `94 12 00 91` | add x20,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00abcdf4"></a> `00abcdf4` | `a1 fc ff 54` | b.ne 0x00abcd88 | `CONDITIONAL_JUMP`
<a id="insn-00abcdf8"></a> `00abcdf8` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00abcdfc"></a> `00abcdfc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00abce00"></a> `00abce00` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abce04"></a> `00abce04` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abce08"></a> `00abce08` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abce0c"></a> `00abce0c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00abce10"></a> `00abce10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abccb8`](#insn-00abccb8) 範囲 `[['00abccb8', '00abccfb']]`
  - `CONDITIONAL_JUMP` [`00abccf8`](#insn-00abccf8) → [`00abcd0c`](#insn-00abcd0c)
  - `FALL_THROUGH` [`00abccf8`](#insn-00abccf8) → [`00abccfc`](#insn-00abccfc)
- ブロック [`00abccfc`](#insn-00abccfc) 範囲 `[['00abccfc', '00abcd0b']]`
  - `FALL_THROUGH` [`00abcd08`](#insn-00abcd08) → [`00abcd0c`](#insn-00abcd0c)
- ブロック [`00abcd0c`](#insn-00abcd0c) 範囲 `[['00abcd0c', '00abcd23']]`
  - `CONDITIONAL_JUMP` [`00abcd20`](#insn-00abcd20) → [`00abcd60`](#insn-00abcd60)
  - `FALL_THROUGH` [`00abcd20`](#insn-00abcd20) → [`00abcd24`](#insn-00abcd24)
- ブロック [`00abcd24`](#insn-00abcd24) 範囲 `[['00abcd24', '00abcd33']]`
  - `CONDITIONAL_JUMP` [`00abcd30`](#insn-00abcd30) → [`00abcdf8`](#insn-00abcdf8)
  - `FALL_THROUGH` [`00abcd30`](#insn-00abcd30) → [`00abcd34`](#insn-00abcd34)
- ブロック [`00abcd34`](#insn-00abcd34) 範囲 `[['00abcd34', '00abcd3f']]`
  - `CONDITIONAL_JUMP` [`00abcd3c`](#insn-00abcd3c) → [`00abcdf8`](#insn-00abcdf8)
  - `FALL_THROUGH` [`00abcd3c`](#insn-00abcd3c) → [`00abcd40`](#insn-00abcd40)
- ブロック [`00abcd40`](#insn-00abcd40) 範囲 `[['00abcd40', '00abcd47']]`
  - `CONDITIONAL_JUMP` [`00abcd44`](#insn-00abcd44) → [`00abcd68`](#insn-00abcd68)
  - `FALL_THROUGH` [`00abcd44`](#insn-00abcd44) → [`00abcd48`](#insn-00abcd48)
- ブロック [`00abcd48`](#insn-00abcd48) 範囲 `[['00abcd48', '00abcd4f']]`
  - `CONDITIONAL_JUMP` [`00abcd4c`](#insn-00abcd4c) → [`00abcd6c`](#insn-00abcd6c)
  - `FALL_THROUGH` [`00abcd4c`](#insn-00abcd4c) → [`00abcd50`](#insn-00abcd50)
- ブロック [`00abcd50`](#insn-00abcd50) 範囲 `[['00abcd50', '00abcd57']]`
  - `CONDITIONAL_JUMP` [`00abcd54`](#insn-00abcd54) → [`00abcd60`](#insn-00abcd60)
  - `FALL_THROUGH` [`00abcd54`](#insn-00abcd54) → [`00abcd58`](#insn-00abcd58)
- ブロック [`00abcd58`](#insn-00abcd58) 範囲 `[['00abcd58', '00abcd5f']]`
  - `UNCONDITIONAL_JUMP` [`00abcd5c`](#insn-00abcd5c) → [`00abcd6c`](#insn-00abcd6c)
- ブロック [`00abcd60`](#insn-00abcd60) 範囲 `[['00abcd60', '00abcd67']]`
  - `UNCONDITIONAL_JUMP` [`00abcd64`](#insn-00abcd64) → [`00abcdf8`](#insn-00abcdf8)
- ブロック [`00abcd68`](#insn-00abcd68) 範囲 `[['00abcd68', '00abcd6b']]`
  - `FALL_THROUGH` [`00abcd68`](#insn-00abcd68) → [`00abcd6c`](#insn-00abcd6c)
- ブロック [`00abcd6c`](#insn-00abcd6c) 範囲 `[['00abcd6c', '00abcd87']]`
  - `FALL_THROUGH` [`00abcd84`](#insn-00abcd84) → [`00abcd88`](#insn-00abcd88)
- ブロック [`00abcd88`](#insn-00abcd88) 範囲 `[['00abcd88', '00abcde7']]`
  - `CONDITIONAL_JUMP` [`00abcde4`](#insn-00abcde4) → [`00abcdf8`](#insn-00abcdf8)
  - `FALL_THROUGH` [`00abcde4`](#insn-00abcde4) → [`00abcde8`](#insn-00abcde8)
- ブロック [`00abcde8`](#insn-00abcde8) 範囲 `[['00abcde8', '00abcdf7']]`
  - `CONDITIONAL_JUMP` [`00abcdf4`](#insn-00abcdf4) → [`00abcd88`](#insn-00abcd88)
  - `FALL_THROUGH` [`00abcdf4`](#insn-00abcdf4) → [`00abcdf8`](#insn-00abcdf8)
- ブロック [`00abcdf8`](#insn-00abcdf8) 範囲 `[['00abcdf8', '00abce13']]`

## 命令位置別の参照

- [`00abccb8`](#insn-00abccb8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abccbc`](#insn-00abccbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abccc0`](#insn-00abccc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abccc4`](#insn-00abccc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abccc8`](#insn-00abccc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abccdc`](#insn-00abccdc) → [`00800338`](../00800/00800338.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00800338` · 推定シンボル `None` · 推定型 `None`
- [`00abcce8`](#insn-00abcce8) → [`008005ec`](../00800/008005ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008005ec` · 推定シンボル `None` · 推定型 `None`
- [`00abccf8`](#insn-00abccf8) → [`00abcd0c`](#insn-00abcd0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcd04`](#insn-00abcd04) → [`008056ac`](../00805/008056ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008056ac` · 推定シンボル `None` · 推定型 `None`
- [`00abcd1c`](#insn-00abcd1c) → [`00a65bf4`](../00a65/00a65bf4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a65bf4` · 推定シンボル `None` · 推定型 `None`
- [`00abcd20`](#insn-00abcd20) → [`00abcd60`](#insn-00abcd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcd30`](#insn-00abcd30) → [`00abcdf8`](#insn-00abcdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcd3c`](#insn-00abcd3c) → [`00abcdf8`](#insn-00abcdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcd44`](#insn-00abcd44) → [`00abcd68`](#insn-00abcd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcd4c`](#insn-00abcd4c) → [`00abcd6c`](#insn-00abcd6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcd54`](#insn-00abcd54) → [`00abcd60`](#insn-00abcd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcd5c`](#insn-00abcd5c) → [`00abcd6c`](#insn-00abcd6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcd64`](#insn-00abcd64) → [`00abcdf8`](#insn-00abcdf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcd70`](#insn-00abcd70) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abcd88`](#insn-00abcd88) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abcde4`](#insn-00abcde4) → [`00abcdf8`](#insn-00abcdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcde8`](#insn-00abcde8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00abcdf4`](#insn-00abcdf4) → [`00abcd88`](#insn-00abcd88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abcdfc`](#insn-00abcdfc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abce00`](#insn-00abce00) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abce04`](#insn-00abce04) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abce08`](#insn-00abce08) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abce0c`](#insn-00abce0c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abccb8`](#insn-00abccb8)

~~~json
{
  "source": "00abccb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abccbc`](#insn-00abccbc)

~~~json
{
  "source": "00abccbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abccc0`](#insn-00abccc0)

~~~json
{
  "source": "00abccc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abccc4`](#insn-00abccc4)

~~~json
{
  "source": "00abccc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abccc8`](#insn-00abccc8)

~~~json
{
  "source": "00abccc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abccdc`](#insn-00abccdc)

~~~json
{
  "source": "00abccdc",
  "target": "00800338",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcce8`](#insn-00abcce8)

~~~json
{
  "source": "00abcce8",
  "target": "008005ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abccf8`](#insn-00abccf8)

~~~json
{
  "source": "00abccf8",
  "target": "00abcd0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcd04`](#insn-00abcd04)

~~~json
{
  "source": "00abcd04",
  "target": "008056ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcd1c`](#insn-00abcd1c)

~~~json
{
  "source": "00abcd1c",
  "target": "00a65bf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcd20`](#insn-00abcd20)

~~~json
{
  "source": "00abcd20",
  "target": "00abcd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcd30`](#insn-00abcd30)

~~~json
{
  "source": "00abcd30",
  "target": "00abcdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcd3c`](#insn-00abcd3c)

~~~json
{
  "source": "00abcd3c",
  "target": "00abcdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcd44`](#insn-00abcd44)

~~~json
{
  "source": "00abcd44",
  "target": "00abcd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcd4c`](#insn-00abcd4c)

~~~json
{
  "source": "00abcd4c",
  "target": "00abcd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcd54`](#insn-00abcd54)

~~~json
{
  "source": "00abcd54",
  "target": "00abcd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcd5c`](#insn-00abcd5c)

~~~json
{
  "source": "00abcd5c",
  "target": "00abcd6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcd64`](#insn-00abcd64)

~~~json
{
  "source": "00abcd64",
  "target": "00abcdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcd70`](#insn-00abcd70)

~~~json
{
  "source": "00abcd70",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcd88`](#insn-00abcd88)

~~~json
{
  "source": "00abcd88",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcde4`](#insn-00abcde4)

~~~json
{
  "source": "00abcde4",
  "target": "00abcdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcde8`](#insn-00abcde8)

~~~json
{
  "source": "00abcde8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abcdf4`](#insn-00abcdf4)

~~~json
{
  "source": "00abcdf4",
  "target": "00abcd88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abcdfc`](#insn-00abcdfc)

~~~json
{
  "source": "00abcdfc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abce00`](#insn-00abce00)

~~~json
{
  "source": "00abce00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abce04`](#insn-00abce04)

~~~json
{
  "source": "00abce04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abce08`](#insn-00abce08)

~~~json
{
  "source": "00abce08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abce0c`](#insn-00abce0c)

~~~json
{
  "source": "00abce0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
