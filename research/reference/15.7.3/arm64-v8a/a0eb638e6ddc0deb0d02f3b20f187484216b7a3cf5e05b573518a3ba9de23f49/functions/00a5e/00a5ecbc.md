# 00a5ecbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00a5ecbc`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00a5e/00a5ecbc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0019.md#compare-7299c66383e518a9cec832bcf81d3e6d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a5ed00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a5e/00a5ed00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0002.md#compare-c9b1436a00ff9870a250e6bd8be721dd)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a5ecbc",
  "name": "FUN_00a5ecbc",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "227a006f24049b3ed9b9c06c9d42eabbb44c5f6ade7adc37f7b6fc3c2175856b",
  "source_text_sha256": "227a006f24049b3ed9b9c06c9d42eabbb44c5f6ade7adc37f7b6fc3c2175856b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a5ecbc",
        "00a5ee17"
      ]
    ],
    "bytes_sha256": "08a4b353a0b8920fb1991a740345f1d3fa9e8bc269a8fb5a80abf0dccf275267",
    "instruction_count": 87,
    "instruction_bytes": 348,
    "body_bytes": 348,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a5e6e0](../00a5e/00a5e6e0.md)

## 呼び出し先

- [007cd2ac](../007cd/007cd2ac.md)
- [007cd560](../007cd/007cd560.md)
- [007d22d4](../007d2/007d22d4.md)
- [0081f580](../0081f/0081f580.md)
- [00a08564](../00a08/00a08564.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1548 bytes

~~~c

bool FUN_00a5ecbc(long param_1,undefined4 param_2)

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
  
  iVar3 = FUN_007cd2ac(param_2);
  iVar4 = FUN_007cd560(param_2);
  iVar5 = *(int *)(param_1 + 0x68);
  if (iVar5 == -1) {
    iVar5 = FUN_007d22d4(iVar3,iVar4);
    iVar5 = iVar5 + -1;
  }
  iVar5 = FUN_00a08564(iVar3,iVar4,iVar5,*(undefined4 *)(param_1 + 0x70),0);
  if (iVar5 == 0) {
LAB_00a5ed64:
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
      if (iVar3 != -3) goto LAB_00a5ed64;
      iVar4 = iVar4 + 4;
    }
    FUN_0081f580();
    lVar10 = 0x30;
    lVar8 = (long)iVar4 * 200 + 0xd28b;
    do {
      lVar6 = FUN_0081f580();
      lVar7 = lVar6 + (long)iVar4 * 200;
      pbVar1 = (byte *)(lVar6 + lVar8);
      uVar2 = (uint)(*(byte *)(lVar7 + 0xd34e) ^ pbVar1[-1]) << 0x10 |
              (uint)(*(byte *)(lVar7 + 0xd34f) ^ *pbVar1) << 0x18 |
              (uint)(*(byte *)(lVar7 + 0xd34d) ^ pbVar1[-2]) << 8 |
              (uint)(*(byte *)(lVar7 + 0xd34c) ^ pbVar1[-3]);
      bVar9 = *(int *)(param_1 + 0x6c) < (int)uVar2;
      if ((int)uVar2 <= *(int *)(param_1 + 0x6c)) {
        return bVar9;
      }
      FUN_0081f580();
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
<a id="insn-00a5ecbc"></a> `00a5ecbc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00a5ecc0"></a> `00a5ecc0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a5ecc4"></a> `00a5ecc4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a5ecc8"></a> `00a5ecc8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a5eccc"></a> `00a5eccc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a5ecd0"></a> `00a5ecd0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a5ecd4"></a> `00a5ecd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a5ecd8"></a> `00a5ecd8` | `e0 03 01 2a` | mov w0,w1 | `FALL_THROUGH`
<a id="insn-00a5ecdc"></a> `00a5ecdc` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00a5ece0"></a> `00a5ece0` | `73 b9 f5 97` | bl 0x007cd2ac | `UNCONDITIONAL_CALL`
<a id="insn-00a5ece4"></a> `00a5ece4` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00a5ece8"></a> `00a5ece8` | `e0 03 14 2a` | mov w0,w20 | `FALL_THROUGH`
<a id="insn-00a5ecec"></a> `00a5ecec` | `1d ba f5 97` | bl 0x007cd560 | `UNCONDITIONAL_CALL`
<a id="insn-00a5ecf0"></a> `00a5ecf0` | `62 6a 40 b9` | ldr w2,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00a5ecf4"></a> `00a5ecf4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00a5ecf8"></a> `00a5ecf8` | `5f 04 00 31` | cmn w2,#0x1 | `FALL_THROUGH`
<a id="insn-00a5ecfc"></a> `00a5ecfc` | `a1 00 00 54` | b.ne 0x00a5ed10 | `CONDITIONAL_JUMP`
<a id="insn-00a5ed00"></a> `00a5ed00` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00a5ed04"></a> `00a5ed04` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00a5ed08"></a> `00a5ed08` | `73 cd f5 97` | bl 0x007d22d4 | `UNCONDITIONAL_CALL`
<a id="insn-00a5ed0c"></a> `00a5ed0c` | `02 04 00 51` | sub w2,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00a5ed10"></a> `00a5ed10` | `63 72 40 b9` | ldr w3,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00a5ed14"></a> `00a5ed14` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00a5ed18"></a> `00a5ed18` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00a5ed1c"></a> `00a5ed1c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00a5ed20"></a> `00a5ed20` | `11 a6 fe 97` | bl 0x00a08564 | `UNCONDITIONAL_CALL`
<a id="insn-00a5ed24"></a> `00a5ed24` | `00 02 00 34` | cbz w0,0x00a5ed64 | `CONDITIONAL_JUMP`
<a id="insn-00a5ed28"></a> `00a5ed28` | `68 6e 40 b9` | ldr w8,[x19, #0x6c] | `FALL_THROUGH`
<a id="insn-00a5ed2c"></a> `00a5ed2c` | `36 00 80 52` | mov w22,#0x1 | `FALL_THROUGH`
<a id="insn-00a5ed30"></a> `00a5ed30` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a5ed34"></a> `00a5ed34` | `40 06 00 54` | b.eq 0x00a5edfc | `CONDITIONAL_JUMP`
<a id="insn-00a5ed38"></a> `00a5ed38` | `68 6a 40 b9` | ldr w8,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00a5ed3c"></a> `00a5ed3c` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a5ed40"></a> `00a5ed40` | `e1 05 00 54` | b.ne 0x00a5edfc | `CONDITIONAL_JUMP`
<a id="insn-00a5ed44"></a> `00a5ed44` | `bf 1e 00 31` | cmn w21,#0x7 | `FALL_THROUGH`
<a id="insn-00a5ed48"></a> `00a5ed48` | `20 01 00 54` | b.eq 0x00a5ed6c | `CONDITIONAL_JUMP`
<a id="insn-00a5ed4c"></a> `00a5ed4c` | `bf 0a 00 31` | cmn w21,#0x2 | `FALL_THROUGH`
<a id="insn-00a5ed50"></a> `00a5ed50` | `00 01 00 54` | b.eq 0x00a5ed70 | `CONDITIONAL_JUMP`
<a id="insn-00a5ed54"></a> `00a5ed54` | `bf 0e 00 31` | cmn w21,#0x3 | `FALL_THROUGH`
<a id="insn-00a5ed58"></a> `00a5ed58` | `61 00 00 54` | b.ne 0x00a5ed64 | `CONDITIONAL_JUMP`
<a id="insn-00a5ed5c"></a> `00a5ed5c` | `94 12 00 11` | add w20,w20,#0x4 | `FALL_THROUGH`
<a id="insn-00a5ed60"></a> `00a5ed60` | `04 00 00 14` | b 0x00a5ed70 | `UNCONDITIONAL_JUMP`
<a id="insn-00a5ed64"></a> `00a5ed64` | `f6 03 1f 2a` | mov w22,wzr | `FALL_THROUGH`
<a id="insn-00a5ed68"></a> `00a5ed68` | `25 00 00 14` | b 0x00a5edfc | `UNCONDITIONAL_JUMP`
<a id="insn-00a5ed6c"></a> `00a5ed6c` | `94 1e 00 11` | add w20,w20,#0x7 | `FALL_THROUGH`
<a id="insn-00a5ed70"></a> `00a5ed70` | `95 7e 40 93` | sxtw x21,w20 | `FALL_THROUGH`
<a id="insn-00a5ed74"></a> `00a5ed74` | `03 02 f7 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a5ed78"></a> `00a5ed78` | `17 19 80 52` | mov w23,#0xc8 | `FALL_THROUGH`
<a id="insn-00a5ed7c"></a> `00a5ed7c` | `68 51 9a 52` | mov w8,#0xd28b | `FALL_THROUGH`
<a id="insn-00a5ed80"></a> `00a5ed80` | `18 06 80 52` | mov w24,#0x30 | `FALL_THROUGH`
<a id="insn-00a5ed84"></a> `00a5ed84` | `94 22 37 9b` | smaddl x20,w20,w23,x8 | `FALL_THROUGH`
<a id="insn-00a5ed88"></a> `00a5ed88` | `19 51 9a 52` | mov w25,#0xd288 | `FALL_THROUGH`
<a id="insn-00a5ed8c"></a> `00a5ed8c` | `fd 01 f7 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a5ed90"></a> `00a5ed90` | `a8 02 37 9b` | smaddl x8,w21,w23,x0 | `FALL_THROUGH`
<a id="insn-00a5ed94"></a> `00a5ed94` | `09 00 14 8b` | add x9,x0,x20 | `FALL_THROUGH`
<a id="insn-00a5ed98"></a> `00a5ed98` | `2a f1 5f 38` | ldurb w10,[x9, #-0x1] | `FALL_THROUGH`
<a id="insn-00a5ed9c"></a> `00a5ed9c` | `2d e1 5f 38` | ldurb w13,[x9, #-0x2] | `FALL_THROUGH`
<a id="insn-00a5eda0"></a> `00a5eda0` | `08 01 19 8b` | add x8,x8,x25 | `FALL_THROUGH`
<a id="insn-00a5eda4"></a> `00a5eda4` | `0b 19 43 39` | ldrb w11,[x8, #0xc6] | `FALL_THROUGH`
<a id="insn-00a5eda8"></a> `00a5eda8` | `0c 1d 43 39` | ldrb w12,[x8, #0xc7] | `FALL_THROUGH`
<a id="insn-00a5edac"></a> `00a5edac` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00a5edb0"></a> `00a5edb0` | `2b 01 40 39` | ldrb w11,[x9] | `FALL_THROUGH`
<a id="insn-00a5edb4"></a> `00a5edb4` | `29 d1 5f 38` | ldurb w9,[x9, #-0x3] | `FALL_THROUGH`
<a id="insn-00a5edb8"></a> `00a5edb8` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00a5edbc"></a> `00a5edbc` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00a5edc0"></a> `00a5edc0` | `0c 15 43 39` | ldrb w12,[x8, #0xc5] | `FALL_THROUGH`
<a id="insn-00a5edc4"></a> `00a5edc4` | `08 11 43 39` | ldrb w8,[x8, #0xc4] | `FALL_THROUGH`
<a id="insn-00a5edc8"></a> `00a5edc8` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00a5edcc"></a> `00a5edcc` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00a5edd0"></a> `00a5edd0` | `08 01 09 4a` | eor w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00a5edd4"></a> `00a5edd4` | `69 6e 40 b9` | ldr w9,[x19, #0x6c] | `FALL_THROUGH`
<a id="insn-00a5edd8"></a> `00a5edd8` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00a5eddc"></a> `00a5eddc` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00a5ede0"></a> `00a5ede0` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00a5ede4"></a> `00a5ede4` | `f6 d7 9f 1a` | cset w22,gt | `FALL_THROUGH`
<a id="insn-00a5ede8"></a> `00a5ede8` | `ad 00 00 54` | b.le 0x00a5edfc | `CONDITIONAL_JUMP`
<a id="insn-00a5edec"></a> `00a5edec` | `e5 01 f7 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00a5edf0"></a> `00a5edf0` | `18 07 00 f1` | subs x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00a5edf4"></a> `00a5edf4` | `94 12 00 91` | add x20,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00a5edf8"></a> `00a5edf8` | `a1 fc ff 54` | b.ne 0x00a5ed8c | `CONDITIONAL_JUMP`
<a id="insn-00a5edfc"></a> `00a5edfc` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00a5ee00"></a> `00a5ee00` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a5ee04"></a> `00a5ee04` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a5ee08"></a> `00a5ee08` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a5ee0c"></a> `00a5ee0c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a5ee10"></a> `00a5ee10` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00a5ee14"></a> `00a5ee14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a5ecbc`](#insn-00a5ecbc) 範囲 `[['00a5ecbc', '00a5ecff']]`
  - `CONDITIONAL_JUMP` [`00a5ecfc`](#insn-00a5ecfc) → [`00a5ed10`](#insn-00a5ed10)
  - `FALL_THROUGH` [`00a5ecfc`](#insn-00a5ecfc) → [`00a5ed00`](#insn-00a5ed00)
- ブロック [`00a5ed00`](#insn-00a5ed00) 範囲 `[['00a5ed00', '00a5ed0f']]`
  - `FALL_THROUGH` [`00a5ed0c`](#insn-00a5ed0c) → [`00a5ed10`](#insn-00a5ed10)
- ブロック [`00a5ed10`](#insn-00a5ed10) 範囲 `[['00a5ed10', '00a5ed27']]`
  - `CONDITIONAL_JUMP` [`00a5ed24`](#insn-00a5ed24) → [`00a5ed64`](#insn-00a5ed64)
  - `FALL_THROUGH` [`00a5ed24`](#insn-00a5ed24) → [`00a5ed28`](#insn-00a5ed28)
- ブロック [`00a5ed28`](#insn-00a5ed28) 範囲 `[['00a5ed28', '00a5ed37']]`
  - `CONDITIONAL_JUMP` [`00a5ed34`](#insn-00a5ed34) → [`00a5edfc`](#insn-00a5edfc)
  - `FALL_THROUGH` [`00a5ed34`](#insn-00a5ed34) → [`00a5ed38`](#insn-00a5ed38)
- ブロック [`00a5ed38`](#insn-00a5ed38) 範囲 `[['00a5ed38', '00a5ed43']]`
  - `CONDITIONAL_JUMP` [`00a5ed40`](#insn-00a5ed40) → [`00a5edfc`](#insn-00a5edfc)
  - `FALL_THROUGH` [`00a5ed40`](#insn-00a5ed40) → [`00a5ed44`](#insn-00a5ed44)
- ブロック [`00a5ed44`](#insn-00a5ed44) 範囲 `[['00a5ed44', '00a5ed4b']]`
  - `CONDITIONAL_JUMP` [`00a5ed48`](#insn-00a5ed48) → [`00a5ed6c`](#insn-00a5ed6c)
  - `FALL_THROUGH` [`00a5ed48`](#insn-00a5ed48) → [`00a5ed4c`](#insn-00a5ed4c)
- ブロック [`00a5ed4c`](#insn-00a5ed4c) 範囲 `[['00a5ed4c', '00a5ed53']]`
  - `CONDITIONAL_JUMP` [`00a5ed50`](#insn-00a5ed50) → [`00a5ed70`](#insn-00a5ed70)
  - `FALL_THROUGH` [`00a5ed50`](#insn-00a5ed50) → [`00a5ed54`](#insn-00a5ed54)
- ブロック [`00a5ed54`](#insn-00a5ed54) 範囲 `[['00a5ed54', '00a5ed5b']]`
  - `CONDITIONAL_JUMP` [`00a5ed58`](#insn-00a5ed58) → [`00a5ed64`](#insn-00a5ed64)
  - `FALL_THROUGH` [`00a5ed58`](#insn-00a5ed58) → [`00a5ed5c`](#insn-00a5ed5c)
- ブロック [`00a5ed5c`](#insn-00a5ed5c) 範囲 `[['00a5ed5c', '00a5ed63']]`
  - `UNCONDITIONAL_JUMP` [`00a5ed60`](#insn-00a5ed60) → [`00a5ed70`](#insn-00a5ed70)
- ブロック [`00a5ed64`](#insn-00a5ed64) 範囲 `[['00a5ed64', '00a5ed6b']]`
  - `UNCONDITIONAL_JUMP` [`00a5ed68`](#insn-00a5ed68) → [`00a5edfc`](#insn-00a5edfc)
- ブロック [`00a5ed6c`](#insn-00a5ed6c) 範囲 `[['00a5ed6c', '00a5ed6f']]`
  - `FALL_THROUGH` [`00a5ed6c`](#insn-00a5ed6c) → [`00a5ed70`](#insn-00a5ed70)
- ブロック [`00a5ed70`](#insn-00a5ed70) 範囲 `[['00a5ed70', '00a5ed8b']]`
  - `FALL_THROUGH` [`00a5ed88`](#insn-00a5ed88) → [`00a5ed8c`](#insn-00a5ed8c)
- ブロック [`00a5ed8c`](#insn-00a5ed8c) 範囲 `[['00a5ed8c', '00a5edeb']]`
  - `CONDITIONAL_JUMP` [`00a5ede8`](#insn-00a5ede8) → [`00a5edfc`](#insn-00a5edfc)
  - `FALL_THROUGH` [`00a5ede8`](#insn-00a5ede8) → [`00a5edec`](#insn-00a5edec)
- ブロック [`00a5edec`](#insn-00a5edec) 範囲 `[['00a5edec', '00a5edfb']]`
  - `CONDITIONAL_JUMP` [`00a5edf8`](#insn-00a5edf8) → [`00a5ed8c`](#insn-00a5ed8c)
  - `FALL_THROUGH` [`00a5edf8`](#insn-00a5edf8) → [`00a5edfc`](#insn-00a5edfc)
- ブロック [`00a5edfc`](#insn-00a5edfc) 範囲 `[['00a5edfc', '00a5ee17']]`

## 命令位置別の参照

- [`00a5ecbc`](#insn-00a5ecbc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ecc0`](#insn-00a5ecc0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ecc4`](#insn-00a5ecc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ecc8`](#insn-00a5ecc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5eccc`](#insn-00a5eccc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ece0`](#insn-00a5ece0) → [`007cd2ac`](../007cd/007cd2ac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cd2ac` · 推定シンボル `None` · 推定型 `None`
- [`00a5ecec`](#insn-00a5ecec) → [`007cd560`](../007cd/007cd560.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cd560` · 推定シンボル `None` · 推定型 `None`
- [`00a5ecfc`](#insn-00a5ecfc) → [`00a5ed10`](#insn-00a5ed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed08`](#insn-00a5ed08) → [`007d22d4`](../007d2/007d22d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007d22d4` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed20`](#insn-00a5ed20) → [`00a08564`](../00a08/00a08564.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a08564` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed24`](#insn-00a5ed24) → [`00a5ed64`](#insn-00a5ed64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed34`](#insn-00a5ed34) → [`00a5edfc`](#insn-00a5edfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed40`](#insn-00a5ed40) → [`00a5edfc`](#insn-00a5edfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed48`](#insn-00a5ed48) → [`00a5ed6c`](#insn-00a5ed6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed50`](#insn-00a5ed50) → [`00a5ed70`](#insn-00a5ed70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed58`](#insn-00a5ed58) → [`00a5ed64`](#insn-00a5ed64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed60`](#insn-00a5ed60) → [`00a5ed70`](#insn-00a5ed70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed68`](#insn-00a5ed68) → [`00a5edfc`](#insn-00a5edfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed74`](#insn-00a5ed74) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a5ed8c`](#insn-00a5ed8c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a5ede8`](#insn-00a5ede8) → [`00a5edfc`](#insn-00a5edfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5edec`](#insn-00a5edec) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00a5edf8`](#insn-00a5edf8) → [`00a5ed8c`](#insn-00a5ed8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ee00`](#insn-00a5ee00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ee04`](#insn-00a5ee04) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ee08`](#insn-00a5ee08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ee0c`](#insn-00a5ee0c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a5ee10`](#insn-00a5ee10) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a5ecbc`](#insn-00a5ecbc)

~~~json
{
  "source": "00a5ecbc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ecc0`](#insn-00a5ecc0)

~~~json
{
  "source": "00a5ecc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ecc4`](#insn-00a5ecc4)

~~~json
{
  "source": "00a5ecc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ecc8`](#insn-00a5ecc8)

~~~json
{
  "source": "00a5ecc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5eccc`](#insn-00a5eccc)

~~~json
{
  "source": "00a5eccc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ece0`](#insn-00a5ece0)

~~~json
{
  "source": "00a5ece0",
  "target": "007cd2ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a5ecec`](#insn-00a5ecec)

~~~json
{
  "source": "00a5ecec",
  "target": "007cd560",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a5ecfc`](#insn-00a5ecfc)

~~~json
{
  "source": "00a5ecfc",
  "target": "00a5ed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ed08`](#insn-00a5ed08)

~~~json
{
  "source": "00a5ed08",
  "target": "007d22d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a5ed20`](#insn-00a5ed20)

~~~json
{
  "source": "00a5ed20",
  "target": "00a08564",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a5ed24`](#insn-00a5ed24)

~~~json
{
  "source": "00a5ed24",
  "target": "00a5ed64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ed34`](#insn-00a5ed34)

~~~json
{
  "source": "00a5ed34",
  "target": "00a5edfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ed40`](#insn-00a5ed40)

~~~json
{
  "source": "00a5ed40",
  "target": "00a5edfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ed48`](#insn-00a5ed48)

~~~json
{
  "source": "00a5ed48",
  "target": "00a5ed6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ed50`](#insn-00a5ed50)

~~~json
{
  "source": "00a5ed50",
  "target": "00a5ed70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ed58`](#insn-00a5ed58)

~~~json
{
  "source": "00a5ed58",
  "target": "00a5ed64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ed60`](#insn-00a5ed60)

~~~json
{
  "source": "00a5ed60",
  "target": "00a5ed70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ed68`](#insn-00a5ed68)

~~~json
{
  "source": "00a5ed68",
  "target": "00a5edfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ed74`](#insn-00a5ed74)

~~~json
{
  "source": "00a5ed74",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a5ed8c`](#insn-00a5ed8c)

~~~json
{
  "source": "00a5ed8c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a5ede8`](#insn-00a5ede8)

~~~json
{
  "source": "00a5ede8",
  "target": "00a5edfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5edec`](#insn-00a5edec)

~~~json
{
  "source": "00a5edec",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a5edf8`](#insn-00a5edf8)

~~~json
{
  "source": "00a5edf8",
  "target": "00a5ed8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ee00`](#insn-00a5ee00)

~~~json
{
  "source": "00a5ee00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ee04`](#insn-00a5ee04)

~~~json
{
  "source": "00a5ee04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ee08`](#insn-00a5ee08)

~~~json
{
  "source": "00a5ee08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ee0c`](#insn-00a5ee0c)

~~~json
{
  "source": "00a5ee0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a5ee10`](#insn-00a5ee10)

~~~json
{
  "source": "00a5ee10",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
