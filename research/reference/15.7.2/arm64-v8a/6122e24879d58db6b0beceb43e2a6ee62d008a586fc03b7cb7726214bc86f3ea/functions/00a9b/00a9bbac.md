# 00a9bbac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a9bbac`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a9b/00a9bbac.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0024.md#compare-45fa88b6bef61b827ce97f98ad6294f3)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9bbac",
  "name": "FUN_00a9bbac",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2112b0f97cea77fd2af031dbd24a3e8b06eefd668ebfb36fb1841078ed8e2fbb",
  "source_text_sha256": "2112b0f97cea77fd2af031dbd24a3e8b06eefd668ebfb36fb1841078ed8e2fbb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9bbac",
        "00a9bd43"
      ]
    ],
    "bytes_sha256": "e18b2fdcc67e7ba92e0e6a0e8590563a952d68a651c6b038610a3e02e78114bc",
    "instruction_count": 102,
    "instruction_bytes": 408,
    "body_bytes": 408,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005ced48](../005ce/005ced48.md)
- [005d6c3c](../005d6/005d6c3c.md)
- [006d6d04](../006d6/006d6d04.md)
- [006e4aec](../006e4/006e4aec.md)
- [006e79bc](../006e7/006e79bc.md)
- [006eccf4](../006ec/006eccf4.md)

## 呼び出し先

- [005bb5f0](../005bb/005bb5f0.md)
- [005bbbc8](../005bb/005bbbc8.md)
- [005bbc10](../005bb/005bbc10.md)
- [005bbc90](../005bb/005bbc90.md)
- [0081f580](../0081f/0081f580.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1418 bytes

~~~c

void FUN_00a9bbac(int param_1,int param_2,int param_3)

{
  int iVar1;
  ulong uVar2;
  long lVar3;
  
  if (param_1 == 1) {
    uVar2 = FUN_005bbbc8();
    if ((uVar2 & 1) == 0) {
      if (param_2 != 0) goto LAB_00a9bc28;
    }
    else {
      iVar1 = FUN_005bbc10();
      if (iVar1 != param_2) goto LAB_00a9bc28;
    }
    uVar2 = FUN_005bbc90();
    if ((uVar2 & 1) != 0) {
      lVar3 = FUN_0081f580();
      FUN_005bb5f0(lVar3 + 0x898,1);
      return;
    }
  }
LAB_00a9bc28:
  lVar3 = FUN_0081f580();
  lVar3 = lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar3 + 0x840cc) = *(int *)(lVar3 + 0x840cc) + param_3;
  lVar3 = FUN_0081f580();
  lVar3 = lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec;
  *(int *)(lVar3 + 0x84240) = *(int *)(lVar3 + 0x84240) + param_3;
  lVar3 = FUN_0081f580();
  if (((0 < *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84288)) &&
      (lVar3 = FUN_0081f580(),
      *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84288) < param_3)) &&
     (lVar3 = FUN_0081f580(),
     *(int *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8428c) == 0)) {
    lVar3 = FUN_0081f580();
    *(undefined4 *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x8428c) = 1;
  }
  lVar3 = FUN_0081f580();
  *(undefined4 *)(lVar3 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84308) = 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a9bbac"></a> `00a9bbac` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00a9bbb0"></a> `00a9bbb0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9bbb4"></a> `00a9bbb4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9bbb8"></a> `00a9bbb8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a9bbbc"></a> `00a9bbbc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a9bbc0"></a> `00a9bbc0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a9bbc4"></a> `00a9bbc4` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00a9bbc8"></a> `00a9bbc8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00a9bbcc"></a> `00a9bbcc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00a9bbd0"></a> `00a9bbd0` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00a9bbd4"></a> `00a9bbd4` | `a1 02 00 54` | b.ne 0x00a9bc28 | `CONDITIONAL_JUMP`
<a id="insn-00a9bbd8"></a> `00a9bbd8` | `fc 7f ec 97` | bl 0x005bbbc8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9bbdc"></a> `00a9bbdc` | `a0 00 00 36` | tbz w0,#0x0,0x00a9bbf0 | `CONDITIONAL_JUMP`
<a id="insn-00a9bbe0"></a> `00a9bbe0` | `0c 80 ec 97` | bl 0x005bbc10 | `UNCONDITIONAL_CALL`
<a id="insn-00a9bbe4"></a> `00a9bbe4` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-00a9bbe8"></a> `00a9bbe8` | `a0 00 00 54` | b.eq 0x00a9bbfc | `CONDITIONAL_JUMP`
<a id="insn-00a9bbec"></a> `00a9bbec` | `0f 00 00 14` | b 0x00a9bc28 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9bbf0"></a> `00a9bbf0` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00a9bbf4"></a> `00a9bbf4` | `1f 00 15 6b` | cmp w0,w21 | `FALL_THROUGH`
<a id="insn-00a9bbf8"></a> `00a9bbf8` | `81 01 00 54` | b.ne 0x00a9bc28 | `CONDITIONAL_JUMP`
<a id="insn-00a9bbfc"></a> `00a9bbfc` | `25 80 ec 97` | bl 0x005bbc90 | `UNCONDITIONAL_CALL`
<a id="insn-00a9bc00"></a> `00a9bc00` | `40 01 00 36` | tbz w0,#0x0,0x00a9bc28 | `CONDITIONAL_JUMP`
<a id="insn-00a9bc04"></a> `00a9bc04` | `5f 0e f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9bc08"></a> `00a9bc08` | `00 60 22 91` | add x0,x0,#0x898 | `FALL_THROUGH`
<a id="insn-00a9bc0c"></a> `00a9bc0c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00a9bc10"></a> `00a9bc10` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a9bc14"></a> `00a9bc14` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9bc18"></a> `00a9bc18` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a9bc1c"></a> `00a9bc1c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9bc20"></a> `00a9bc20` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00a9bc24"></a> `00a9bc24` | `73 7e ec 17` | b 0x005bb5f0 | `CALL_TERMINATOR`
<a id="insn-00a9bc28"></a> `00a9bc28` | `56 0e f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9bc2c"></a> `00a9bc2c` | `98 00 99 52` | mov w24,#0xc804 | `FALL_THROUGH`
<a id="insn-00a9bc30"></a> `00a9bc30` | `99 7d 80 52` | mov w25,#0x3ec | `FALL_THROUGH`
<a id="insn-00a9bc34"></a> `00a9bc34` | `89 19 88 52` | mov w9,#0x40cc | `FALL_THROUGH`
<a id="insn-00a9bc38"></a> `00a9bc38` | `88 02 38 9b` | smaddl x8,w20,w24,x0 | `FALL_THROUGH`
<a id="insn-00a9bc3c"></a> `00a9bc3c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9bc40"></a> `00a9bc40` | `97 7e 40 93` | sxtw x23,w20 | `FALL_THROUGH`
<a id="insn-00a9bc44"></a> `00a9bc44` | `a8 22 39 9b` | smaddl x8,w21,w25,x8 | `FALL_THROUGH`
<a id="insn-00a9bc48"></a> `00a9bc48` | `b6 7e 40 93` | sxtw x22,w21 | `FALL_THROUGH`
<a id="insn-00a9bc4c"></a> `00a9bc4c` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9bc50"></a> `00a9bc50` | `4a 01 13 0b` | add w10,w10,w19 | `FALL_THROUGH`
<a id="insn-00a9bc54"></a> `00a9bc54` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9bc58"></a> `00a9bc58` | `4a 0e f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9bc5c"></a> `00a9bc5c` | `88 02 38 9b` | smaddl x8,w20,w24,x0 | `FALL_THROUGH`
<a id="insn-00a9bc60"></a> `00a9bc60` | `09 48 88 52` | mov w9,#0x4240 | `FALL_THROUGH`
<a id="insn-00a9bc64"></a> `00a9bc64` | `a8 22 39 9b` | smaddl x8,w21,w25,x8 | `FALL_THROUGH`
<a id="insn-00a9bc68"></a> `00a9bc68` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9bc6c"></a> `00a9bc6c` | `0a 69 69 b8` | ldr w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9bc70"></a> `00a9bc70` | `4a 01 13 0b` | add w10,w10,w19 | `FALL_THROUGH`
<a id="insn-00a9bc74"></a> `00a9bc74` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9bc78"></a> `00a9bc78` | `42 0e f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9bc7c"></a> `00a9bc7c` | `88 02 38 9b` | smaddl x8,w20,w24,x0 | `FALL_THROUGH`
<a id="insn-00a9bc80"></a> `00a9bc80` | `09 51 88 52` | mov w9,#0x4288 | `FALL_THROUGH`
<a id="insn-00a9bc84"></a> `00a9bc84` | `a8 22 39 9b` | smaddl x8,w21,w25,x8 | `FALL_THROUGH`
<a id="insn-00a9bc88"></a> `00a9bc88` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9bc8c"></a> `00a9bc8c` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9bc90"></a> `00a9bc90` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a9bc94"></a> `00a9bc94` | `ab 03 00 54` | b.lt 0x00a9bd08 | `CONDITIONAL_JUMP`
<a id="insn-00a9bc98"></a> `00a9bc98` | `3a 0e f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9bc9c"></a> `00a9bc9c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00a9bca0"></a> `00a9bca0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00a9bca4"></a> `00a9bca4` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9bca8"></a> `00a9bca8` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9bcac"></a> `00a9bcac` | `09 51 88 52` | mov w9,#0x4288 | `FALL_THROUGH`
<a id="insn-00a9bcb0"></a> `00a9bcb0` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9bcb4"></a> `00a9bcb4` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9bcb8"></a> `00a9bcb8` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00a9bcbc"></a> `00a9bcbc` | `6a 02 00 54` | b.ge 0x00a9bd08 | `CONDITIONAL_JUMP`
<a id="insn-00a9bcc0"></a> `00a9bcc0` | `30 0e f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9bcc4"></a> `00a9bcc4` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00a9bcc8"></a> `00a9bcc8` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00a9bccc"></a> `00a9bccc` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9bcd0"></a> `00a9bcd0` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9bcd4"></a> `00a9bcd4` | `89 51 88 52` | mov w9,#0x428c | `FALL_THROUGH`
<a id="insn-00a9bcd8"></a> `00a9bcd8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9bcdc"></a> `00a9bcdc` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9bce0"></a> `00a9bce0` | `48 01 00 35` | cbnz w8,0x00a9bd08 | `CONDITIONAL_JUMP`
<a id="insn-00a9bce4"></a> `00a9bce4` | `27 0e f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9bce8"></a> `00a9bce8` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00a9bcec"></a> `00a9bcec` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00a9bcf0"></a> `00a9bcf0` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00a9bcf4"></a> `00a9bcf4` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9bcf8"></a> `00a9bcf8` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9bcfc"></a> `00a9bcfc` | `89 51 88 52` | mov w9,#0x428c | `FALL_THROUGH`
<a id="insn-00a9bd00"></a> `00a9bd00` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9bd04"></a> `00a9bd04` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9bd08"></a> `00a9bd08` | `1e 0e f6 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a9bd0c"></a> `00a9bd0c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00a9bd10"></a> `00a9bd10` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00a9bd14"></a> `00a9bd14` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00a9bd18"></a> `00a9bd18` | `e8 02 28 9b` | smaddl x8,w23,w8,x0 | `FALL_THROUGH`
<a id="insn-00a9bd1c"></a> `00a9bd1c` | `c8 22 29 9b` | smaddl x8,w22,w9,x8 | `FALL_THROUGH`
<a id="insn-00a9bd20"></a> `00a9bd20` | `09 61 88 52` | mov w9,#0x4308 | `FALL_THROUGH`
<a id="insn-00a9bd24"></a> `00a9bd24` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00a9bd28"></a> `00a9bd28` | `0a 69 29 b8` | str w10,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00a9bd2c"></a> `00a9bd2c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a9bd30"></a> `00a9bd30` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9bd34"></a> `00a9bd34` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a9bd38"></a> `00a9bd38` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9bd3c"></a> `00a9bd3c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00a9bd40"></a> `00a9bd40` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9bbac`](#insn-00a9bbac) 範囲 `[['00a9bbac', '00a9bbd7']]`
  - `CONDITIONAL_JUMP` [`00a9bbd4`](#insn-00a9bbd4) → [`00a9bc28`](#insn-00a9bc28)
  - `FALL_THROUGH` [`00a9bbd4`](#insn-00a9bbd4) → [`00a9bbd8`](#insn-00a9bbd8)
- ブロック [`00a9bbd8`](#insn-00a9bbd8) 範囲 `[['00a9bbd8', '00a9bbdf']]`
  - `CONDITIONAL_JUMP` [`00a9bbdc`](#insn-00a9bbdc) → [`00a9bbf0`](#insn-00a9bbf0)
  - `FALL_THROUGH` [`00a9bbdc`](#insn-00a9bbdc) → [`00a9bbe0`](#insn-00a9bbe0)
- ブロック [`00a9bbe0`](#insn-00a9bbe0) 範囲 `[['00a9bbe0', '00a9bbeb']]`
  - `CONDITIONAL_JUMP` [`00a9bbe8`](#insn-00a9bbe8) → [`00a9bbfc`](#insn-00a9bbfc)
  - `FALL_THROUGH` [`00a9bbe8`](#insn-00a9bbe8) → [`00a9bbec`](#insn-00a9bbec)
- ブロック [`00a9bbec`](#insn-00a9bbec) 範囲 `[['00a9bbec', '00a9bbef']]`
  - `UNCONDITIONAL_JUMP` [`00a9bbec`](#insn-00a9bbec) → [`00a9bc28`](#insn-00a9bc28)
- ブロック [`00a9bbf0`](#insn-00a9bbf0) 範囲 `[['00a9bbf0', '00a9bbfb']]`
  - `CONDITIONAL_JUMP` [`00a9bbf8`](#insn-00a9bbf8) → [`00a9bc28`](#insn-00a9bc28)
  - `FALL_THROUGH` [`00a9bbf8`](#insn-00a9bbf8) → [`00a9bbfc`](#insn-00a9bbfc)
- ブロック [`00a9bbfc`](#insn-00a9bbfc) 範囲 `[['00a9bbfc', '00a9bc03']]`
  - `CONDITIONAL_JUMP` [`00a9bc00`](#insn-00a9bc00) → [`00a9bc28`](#insn-00a9bc28)
  - `FALL_THROUGH` [`00a9bc00`](#insn-00a9bc00) → [`00a9bc04`](#insn-00a9bc04)
- ブロック [`00a9bc04`](#insn-00a9bc04) 範囲 `[['00a9bc04', '00a9bc27']]`
- ブロック [`00a9bc28`](#insn-00a9bc28) 範囲 `[['00a9bc28', '00a9bc97']]`
  - `CONDITIONAL_JUMP` [`00a9bc94`](#insn-00a9bc94) → [`00a9bd08`](#insn-00a9bd08)
  - `FALL_THROUGH` [`00a9bc94`](#insn-00a9bc94) → [`00a9bc98`](#insn-00a9bc98)
- ブロック [`00a9bc98`](#insn-00a9bc98) 範囲 `[['00a9bc98', '00a9bcbf']]`
  - `CONDITIONAL_JUMP` [`00a9bcbc`](#insn-00a9bcbc) → [`00a9bd08`](#insn-00a9bd08)
  - `FALL_THROUGH` [`00a9bcbc`](#insn-00a9bcbc) → [`00a9bcc0`](#insn-00a9bcc0)
- ブロック [`00a9bcc0`](#insn-00a9bcc0) 範囲 `[['00a9bcc0', '00a9bce3']]`
  - `CONDITIONAL_JUMP` [`00a9bce0`](#insn-00a9bce0) → [`00a9bd08`](#insn-00a9bd08)
  - `FALL_THROUGH` [`00a9bce0`](#insn-00a9bce0) → [`00a9bce4`](#insn-00a9bce4)
- ブロック [`00a9bce4`](#insn-00a9bce4) 範囲 `[['00a9bce4', '00a9bd07']]`
  - `FALL_THROUGH` [`00a9bd04`](#insn-00a9bd04) → [`00a9bd08`](#insn-00a9bd08)
- ブロック [`00a9bd08`](#insn-00a9bd08) 範囲 `[['00a9bd08', '00a9bd43']]`

## 命令位置別の参照

- [`00a9bbac`](#insn-00a9bbac) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbb0`](#insn-00a9bbb0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbb4`](#insn-00a9bbb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbb8`](#insn-00a9bbb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbbc`](#insn-00a9bbbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbd4`](#insn-00a9bbd4) → [`00a9bc28`](#insn-00a9bc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbd8`](#insn-00a9bbd8) → [`005bbbc8`](../005bb/005bbbc8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bbbc8` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbdc`](#insn-00a9bbdc) → [`00a9bbf0`](#insn-00a9bbf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbe0`](#insn-00a9bbe0) → [`005bbc10`](../005bb/005bbc10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bbc10` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbe8`](#insn-00a9bbe8) → [`00a9bbfc`](#insn-00a9bbfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbec`](#insn-00a9bbec) → [`00a9bc28`](#insn-00a9bc28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbf8`](#insn-00a9bbf8) → [`00a9bc28`](#insn-00a9bc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bbfc`](#insn-00a9bbfc) → [`005bbc90`](../005bb/005bbc90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bbc90` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc00`](#insn-00a9bc00) → [`00a9bc28`](#insn-00a9bc28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc04`](#insn-00a9bc04) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc10`](#insn-00a9bc10) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc14`](#insn-00a9bc14) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc18`](#insn-00a9bc18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc1c`](#insn-00a9bc1c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc20`](#insn-00a9bc20) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc24`](#insn-00a9bc24) → [`005bb5f0`](../005bb/005bb5f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005bb5f0` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc28`](#insn-00a9bc28) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc58`](#insn-00a9bc58) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc78`](#insn-00a9bc78) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc94`](#insn-00a9bc94) → [`00a9bd08`](#insn-00a9bd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bc98`](#insn-00a9bc98) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9bcbc`](#insn-00a9bcbc) → [`00a9bd08`](#insn-00a9bd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bcc0`](#insn-00a9bcc0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9bce0`](#insn-00a9bce0) → [`00a9bd08`](#insn-00a9bd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bce4`](#insn-00a9bce4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9bd08`](#insn-00a9bd08) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a9bd2c`](#insn-00a9bd2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bd30`](#insn-00a9bd30) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bd34`](#insn-00a9bd34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bd38`](#insn-00a9bd38) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9bd3c`](#insn-00a9bd3c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9bbac`](#insn-00a9bbac)

~~~json
{
  "source": "00a9bbac",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bbb0`](#insn-00a9bbb0)

~~~json
{
  "source": "00a9bbb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bbb4`](#insn-00a9bbb4)

~~~json
{
  "source": "00a9bbb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bbb8`](#insn-00a9bbb8)

~~~json
{
  "source": "00a9bbb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bbbc`](#insn-00a9bbbc)

~~~json
{
  "source": "00a9bbbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bbd4`](#insn-00a9bbd4)

~~~json
{
  "source": "00a9bbd4",
  "target": "00a9bc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bbd8`](#insn-00a9bbd8)

~~~json
{
  "source": "00a9bbd8",
  "target": "005bbbc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bbdc`](#insn-00a9bbdc)

~~~json
{
  "source": "00a9bbdc",
  "target": "00a9bbf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bbe0`](#insn-00a9bbe0)

~~~json
{
  "source": "00a9bbe0",
  "target": "005bbc10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bbe8`](#insn-00a9bbe8)

~~~json
{
  "source": "00a9bbe8",
  "target": "00a9bbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bbec`](#insn-00a9bbec)

~~~json
{
  "source": "00a9bbec",
  "target": "00a9bc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bbf8`](#insn-00a9bbf8)

~~~json
{
  "source": "00a9bbf8",
  "target": "00a9bc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bbfc`](#insn-00a9bbfc)

~~~json
{
  "source": "00a9bbfc",
  "target": "005bbc90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bc00`](#insn-00a9bc00)

~~~json
{
  "source": "00a9bc00",
  "target": "00a9bc28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bc04`](#insn-00a9bc04)

~~~json
{
  "source": "00a9bc04",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bc10`](#insn-00a9bc10)

~~~json
{
  "source": "00a9bc10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bc14`](#insn-00a9bc14)

~~~json
{
  "source": "00a9bc14",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bc18`](#insn-00a9bc18)

~~~json
{
  "source": "00a9bc18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bc1c`](#insn-00a9bc1c)

~~~json
{
  "source": "00a9bc1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bc20`](#insn-00a9bc20)

~~~json
{
  "source": "00a9bc20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bc24`](#insn-00a9bc24)

~~~json
{
  "source": "00a9bc24",
  "target": "005bb5f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bc28`](#insn-00a9bc28)

~~~json
{
  "source": "00a9bc28",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bc58`](#insn-00a9bc58)

~~~json
{
  "source": "00a9bc58",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bc78`](#insn-00a9bc78)

~~~json
{
  "source": "00a9bc78",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bc94`](#insn-00a9bc94)

~~~json
{
  "source": "00a9bc94",
  "target": "00a9bd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bc98`](#insn-00a9bc98)

~~~json
{
  "source": "00a9bc98",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bcbc`](#insn-00a9bcbc)

~~~json
{
  "source": "00a9bcbc",
  "target": "00a9bd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bcc0`](#insn-00a9bcc0)

~~~json
{
  "source": "00a9bcc0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bce0`](#insn-00a9bce0)

~~~json
{
  "source": "00a9bce0",
  "target": "00a9bd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bce4`](#insn-00a9bce4)

~~~json
{
  "source": "00a9bce4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bd08`](#insn-00a9bd08)

~~~json
{
  "source": "00a9bd08",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9bd2c`](#insn-00a9bd2c)

~~~json
{
  "source": "00a9bd2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bd30`](#insn-00a9bd30)

~~~json
{
  "source": "00a9bd30",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bd34`](#insn-00a9bd34)

~~~json
{
  "source": "00a9bd34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bd38`](#insn-00a9bd38)

~~~json
{
  "source": "00a9bd38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9bd3c`](#insn-00a9bd3c)

~~~json
{
  "source": "00a9bd3c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
