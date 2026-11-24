# 00af4cec

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00af3cf8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00af3/00af3cf8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0068.md#compare-052f5b657abda7b38db59ef84ae5ba1f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af4cec",
  "name": "FUN_00af4cec",
  "size": 360,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4a7f5ca513c426055eda8231a69f6af0d39e01ce368bfa3bdfb3b2782b9e745c",
  "source_text_sha256": "4a7f5ca513c426055eda8231a69f6af0d39e01ce368bfa3bdfb3b2782b9e745c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af4cec",
        "00af4e53"
      ]
    ],
    "bytes_sha256": "513ad71ae9853a16fbd39483512caa697c6f44e91d0a667cdc9b64965a045400",
    "instruction_count": 90,
    "instruction_bytes": 360,
    "body_bytes": 360,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005fea5c](../005fe/005fea5c.md)
- [006bc0a0](../006bc/006bc0a0.md)
- [00700f00](../00700/00700f00.md)
- [00715908](../00715/00715908.md)
- [00716e98](../00716/00716e98.md)
- [00716f88](../00716/00716f88.md)
- [00717198](../00717/00717198.md)
- [00a50418](../00a50/00a50418.md)
- [00a53028](../00a53/00a53028.md)

## 呼び出し先

- [0046db10](../0046d/0046db10.md)
- [0047b054](../0047b/0047b054.md)
- [0047d134](../0047d/0047d134.md)
- [005e7810](../005e7/005e7810.md)
- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1271 bytes

~~~c

void FUN_00af4cec(int param_1,int param_2,int param_3)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  ulong uVar4;
  
  if (param_3 == 0) {
    lVar2 = FUN_008524fc();
    if (*(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848f0) == 0) {
      param_3 = 1;
    }
    else {
      lVar2 = FUN_008524fc();
      uVar4 = FUN_005e7810(lVar2 + (long)param_1 * 0x1f0 + 0x2768);
      if ((uVar4 & 1) == 0) {
        lVar2 = FUN_008524fc();
        param_3 = 0xe;
        if (*(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bfc) < 1) {
          param_3 = 0;
        }
      }
      else {
        param_3 = 0;
      }
    }
  }
  else if (param_3 == 4) {
    lVar2 = FUN_008524fc();
    if (*(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bb0) != 0) {
      iVar1 = FUN_0046db10(100);
      lVar2 = FUN_008524fc();
      if (iVar1 < *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84bb0)) {
        uVar3 = FUN_0047b054();
        FUN_0047d134(uVar3,0x8f,0);
        param_3 = 0x15;
        goto LAB_00af4e24;
      }
    }
    param_3 = 4;
  }
LAB_00af4e24:
  lVar2 = FUN_008524fc();
  *(int *)(lVar2 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x848cc) = param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af4cec"></a> `00af4cec` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00af4cf0"></a> `00af4cf0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af4cf4"></a> `00af4cf4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af4cf8"></a> `00af4cf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00af4cfc"></a> `00af4cfc` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af4d00"></a> `00af4d00` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00af4d04"></a> `00af4d04` | `42 04 00 34` | cbz w2,0x00af4d8c | `CONDITIONAL_JUMP`
<a id="insn-00af4d08"></a> `00af4d08` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00af4d0c"></a> `00af4d0c` | `5f 10 00 71` | cmp w2,#0x4 | `FALL_THROUGH`
<a id="insn-00af4d10"></a> `00af4d10` | `a1 07 00 54` | b.ne 0x00af4e04 | `CONDITIONAL_JUMP`
<a id="insn-00af4d14"></a> `00af4d14` | `fa 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4d18"></a> `00af4d18` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4d1c"></a> `00af4d1c` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4d20"></a> `00af4d20` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4d24"></a> `00af4d24` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4d28"></a> `00af4d28` | `09 76 89 52` | mov w9,#0x4bb0 | `FALL_THROUGH`
<a id="insn-00af4d2c"></a> `00af4d2c` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00af4d30"></a> `00af4d30` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4d34"></a> `00af4d34` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00af4d38"></a> `00af4d38` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4d3c"></a> `00af4d3c` | `a8 06 00 34` | cbz w8,0x00af4e10 | `CONDITIONAL_JUMP`
<a id="insn-00af4d40"></a> `00af4d40` | `80 0c 80 52` | mov w0,#0x64 | `FALL_THROUGH`
<a id="insn-00af4d44"></a> `00af4d44` | `73 e3 e5 97` | bl 0x0046db10 | `UNCONDITIONAL_CALL`
<a id="insn-00af4d48"></a> `00af4d48` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00af4d4c"></a> `00af4d4c` | `ec 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4d50"></a> `00af4d50` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4d54"></a> `00af4d54` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4d58"></a> `00af4d58` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4d5c"></a> `00af4d5c` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4d60"></a> `00af4d60` | `09 76 89 52` | mov w9,#0x4bb0 | `FALL_THROUGH`
<a id="insn-00af4d64"></a> `00af4d64` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4d68"></a> `00af4d68` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4d6c"></a> `00af4d6c` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-00af4d70"></a> `00af4d70` | `0d 05 00 54` | b.le 0x00af4e10 | `CONDITIONAL_JUMP`
<a id="insn-00af4d74"></a> `00af4d74` | `b8 18 e6 97` | bl 0x0047b054 | `UNCONDITIONAL_CALL`
<a id="insn-00af4d78"></a> `00af4d78` | `e1 11 80 52` | mov w1,#0x8f | `FALL_THROUGH`
<a id="insn-00af4d7c"></a> `00af4d7c` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00af4d80"></a> `00af4d80` | `ed 20 e6 97` | bl 0x0047d134 | `UNCONDITIONAL_CALL`
<a id="insn-00af4d84"></a> `00af4d84` | `b3 02 80 52` | mov w19,#0x15 | `FALL_THROUGH`
<a id="insn-00af4d88"></a> `00af4d88` | `27 00 00 14` | b 0x00af4e24 | `UNCONDITIONAL_JUMP`
<a id="insn-00af4d8c"></a> `00af4d8c` | `dc 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4d90"></a> `00af4d90` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4d94"></a> `00af4d94` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4d98"></a> `00af4d98` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4d9c"></a> `00af4d9c` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00af4da0"></a> `00af4da0` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4da4"></a> `00af4da4` | `09 1e 89 52` | mov w9,#0x48f0 | `FALL_THROUGH`
<a id="insn-00af4da8"></a> `00af4da8` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00af4dac"></a> `00af4dac` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4db0"></a> `00af4db0` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4db4"></a> `00af4db4` | `28 03 00 34` | cbz w8,0x00af4e18 | `CONDITIONAL_JUMP`
<a id="insn-00af4db8"></a> `00af4db8` | `d1 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4dbc"></a> `00af4dbc` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00af4dc0"></a> `00af4dc0` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00af4dc4"></a> `00af4dc4` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4dc8"></a> `00af4dc8` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00af4dcc"></a> `00af4dcc` | `91 ca eb 97` | bl 0x005e7810 | `UNCONDITIONAL_CALL`
<a id="insn-00af4dd0"></a> `00af4dd0` | `80 02 00 37` | tbnz w0,#0x0,0x00af4e20 | `CONDITIONAL_JUMP`
<a id="insn-00af4dd4"></a> `00af4dd4` | `ca 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4dd8"></a> `00af4dd8` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4ddc"></a> `00af4ddc` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4de0"></a> `00af4de0` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4de4"></a> `00af4de4` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4de8"></a> `00af4de8` | `89 7f 89 52` | mov w9,#0x4bfc | `FALL_THROUGH`
<a id="insn-00af4dec"></a> `00af4dec` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4df0"></a> `00af4df0` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4df4"></a> `00af4df4` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00af4df8"></a> `00af4df8` | `c8 01 80 52` | mov w8,#0xe | `FALL_THROUGH`
<a id="insn-00af4dfc"></a> `00af4dfc` | `13 c1 9f 1a` | csel w19,w8,wzr,gt | `FALL_THROUGH`
<a id="insn-00af4e00"></a> `00af4e00` | `09 00 00 14` | b 0x00af4e24 | `UNCONDITIONAL_JUMP`
<a id="insn-00af4e04"></a> `00af4e04` | `b5 7e 40 93` | sxtw x21,w21 | `FALL_THROUGH`
<a id="insn-00af4e08"></a> `00af4e08` | `94 7e 40 93` | sxtw x20,w20 | `FALL_THROUGH`
<a id="insn-00af4e0c"></a> `00af4e0c` | `06 00 00 14` | b 0x00af4e24 | `UNCONDITIONAL_JUMP`
<a id="insn-00af4e10"></a> `00af4e10` | `93 00 80 52` | mov w19,#0x4 | `FALL_THROUGH`
<a id="insn-00af4e14"></a> `00af4e14` | `04 00 00 14` | b 0x00af4e24 | `UNCONDITIONAL_JUMP`
<a id="insn-00af4e18"></a> `00af4e18` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00af4e1c"></a> `00af4e1c` | `02 00 00 14` | b 0x00af4e24 | `UNCONDITIONAL_JUMP`
<a id="insn-00af4e20"></a> `00af4e20` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00af4e24"></a> `00af4e24` | `b6 75 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00af4e28"></a> `00af4e28` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4e2c"></a> `00af4e2c` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4e30"></a> `00af4e30` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af4e34"></a> `00af4e34` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4e38"></a> `00af4e38` | `89 19 89 52` | mov w9,#0x48cc | `FALL_THROUGH`
<a id="insn-00af4e3c"></a> `00af4e3c` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4e40"></a> `00af4e40` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4e44"></a> `00af4e44` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af4e48"></a> `00af4e48` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af4e4c"></a> `00af4e4c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00af4e50"></a> `00af4e50` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af4cec`](#insn-00af4cec) 範囲 `[['00af4cec', '00af4d07']]`
  - `CONDITIONAL_JUMP` [`00af4d04`](#insn-00af4d04) → [`00af4d8c`](#insn-00af4d8c)
  - `FALL_THROUGH` [`00af4d04`](#insn-00af4d04) → [`00af4d08`](#insn-00af4d08)
- ブロック [`00af4d08`](#insn-00af4d08) 範囲 `[['00af4d08', '00af4d13']]`
  - `CONDITIONAL_JUMP` [`00af4d10`](#insn-00af4d10) → [`00af4e04`](#insn-00af4e04)
  - `FALL_THROUGH` [`00af4d10`](#insn-00af4d10) → [`00af4d14`](#insn-00af4d14)
- ブロック [`00af4d14`](#insn-00af4d14) 範囲 `[['00af4d14', '00af4d3f']]`
  - `CONDITIONAL_JUMP` [`00af4d3c`](#insn-00af4d3c) → [`00af4e10`](#insn-00af4e10)
  - `FALL_THROUGH` [`00af4d3c`](#insn-00af4d3c) → [`00af4d40`](#insn-00af4d40)
- ブロック [`00af4d40`](#insn-00af4d40) 範囲 `[['00af4d40', '00af4d73']]`
  - `CONDITIONAL_JUMP` [`00af4d70`](#insn-00af4d70) → [`00af4e10`](#insn-00af4e10)
  - `FALL_THROUGH` [`00af4d70`](#insn-00af4d70) → [`00af4d74`](#insn-00af4d74)
- ブロック [`00af4d74`](#insn-00af4d74) 範囲 `[['00af4d74', '00af4d8b']]`
  - `UNCONDITIONAL_JUMP` [`00af4d88`](#insn-00af4d88) → [`00af4e24`](#insn-00af4e24)
- ブロック [`00af4d8c`](#insn-00af4d8c) 範囲 `[['00af4d8c', '00af4db7']]`
  - `CONDITIONAL_JUMP` [`00af4db4`](#insn-00af4db4) → [`00af4e18`](#insn-00af4e18)
  - `FALL_THROUGH` [`00af4db4`](#insn-00af4db4) → [`00af4db8`](#insn-00af4db8)
- ブロック [`00af4db8`](#insn-00af4db8) 範囲 `[['00af4db8', '00af4dd3']]`
  - `CONDITIONAL_JUMP` [`00af4dd0`](#insn-00af4dd0) → [`00af4e20`](#insn-00af4e20)
  - `FALL_THROUGH` [`00af4dd0`](#insn-00af4dd0) → [`00af4dd4`](#insn-00af4dd4)
- ブロック [`00af4dd4`](#insn-00af4dd4) 範囲 `[['00af4dd4', '00af4e03']]`
  - `UNCONDITIONAL_JUMP` [`00af4e00`](#insn-00af4e00) → [`00af4e24`](#insn-00af4e24)
- ブロック [`00af4e04`](#insn-00af4e04) 範囲 `[['00af4e04', '00af4e0f']]`
  - `UNCONDITIONAL_JUMP` [`00af4e0c`](#insn-00af4e0c) → [`00af4e24`](#insn-00af4e24)
- ブロック [`00af4e10`](#insn-00af4e10) 範囲 `[['00af4e10', '00af4e17']]`
  - `UNCONDITIONAL_JUMP` [`00af4e14`](#insn-00af4e14) → [`00af4e24`](#insn-00af4e24)
- ブロック [`00af4e18`](#insn-00af4e18) 範囲 `[['00af4e18', '00af4e1f']]`
  - `UNCONDITIONAL_JUMP` [`00af4e1c`](#insn-00af4e1c) → [`00af4e24`](#insn-00af4e24)
- ブロック [`00af4e20`](#insn-00af4e20) 範囲 `[['00af4e20', '00af4e23']]`
  - `FALL_THROUGH` [`00af4e20`](#insn-00af4e20) → [`00af4e24`](#insn-00af4e24)
- ブロック [`00af4e24`](#insn-00af4e24) 範囲 `[['00af4e24', '00af4e53']]`

## 命令位置別の参照

- [`00af4cec`](#insn-00af4cec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4cf0`](#insn-00af4cf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4cf4`](#insn-00af4cf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4d04`](#insn-00af4d04) → [`00af4d8c`](#insn-00af4d8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4d10`](#insn-00af4d10) → [`00af4e04`](#insn-00af4e04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4d14`](#insn-00af4d14) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4d3c`](#insn-00af4d3c) → [`00af4e10`](#insn-00af4e10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4d44`](#insn-00af4d44) → [`0046db10`](../0046d/0046db10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046db10` · 推定シンボル `None` · 推定型 `None`
- [`00af4d4c`](#insn-00af4d4c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4d70`](#insn-00af4d70) → [`00af4e10`](#insn-00af4e10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4d74`](#insn-00af4d74) → [`0047b054`](../0047b/0047b054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047b054` · 推定シンボル `None` · 推定型 `None`
- [`00af4d80`](#insn-00af4d80) → [`0047d134`](../0047d/0047d134.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047d134` · 推定シンボル `None` · 推定型 `None`
- [`00af4d88`](#insn-00af4d88) → [`00af4e24`](#insn-00af4e24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4d8c`](#insn-00af4d8c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4db4`](#insn-00af4db4) → [`00af4e18`](#insn-00af4e18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4db8`](#insn-00af4db8) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4dcc`](#insn-00af4dcc) → [`005e7810`](../005e7/005e7810.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e7810` · 推定シンボル `None` · 推定型 `None`
- [`00af4dd0`](#insn-00af4dd0) → [`00af4e20`](#insn-00af4e20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4dd4`](#insn-00af4dd4) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4e00`](#insn-00af4e00) → [`00af4e24`](#insn-00af4e24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e0c`](#insn-00af4e0c) → [`00af4e24`](#insn-00af4e24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e14`](#insn-00af4e14) → [`00af4e24`](#insn-00af4e24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e1c`](#insn-00af4e1c) → [`00af4e24`](#insn-00af4e24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e24`](#insn-00af4e24) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00af4e44`](#insn-00af4e44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e48`](#insn-00af4e48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4e4c`](#insn-00af4e4c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af4cec`](#insn-00af4cec)

~~~json
{
  "source": "00af4cec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4cf0`](#insn-00af4cf0)

~~~json
{
  "source": "00af4cf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4cf4`](#insn-00af4cf4)

~~~json
{
  "source": "00af4cf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4d04`](#insn-00af4d04)

~~~json
{
  "source": "00af4d04",
  "target": "00af4d8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4d10`](#insn-00af4d10)

~~~json
{
  "source": "00af4d10",
  "target": "00af4e04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4d14`](#insn-00af4d14)

~~~json
{
  "source": "00af4d14",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4d3c`](#insn-00af4d3c)

~~~json
{
  "source": "00af4d3c",
  "target": "00af4e10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4d44`](#insn-00af4d44)

~~~json
{
  "source": "00af4d44",
  "target": "0046db10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4d4c`](#insn-00af4d4c)

~~~json
{
  "source": "00af4d4c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4d70`](#insn-00af4d70)

~~~json
{
  "source": "00af4d70",
  "target": "00af4e10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4d74`](#insn-00af4d74)

~~~json
{
  "source": "00af4d74",
  "target": "0047b054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4d80`](#insn-00af4d80)

~~~json
{
  "source": "00af4d80",
  "target": "0047d134",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4d88`](#insn-00af4d88)

~~~json
{
  "source": "00af4d88",
  "target": "00af4e24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4d8c`](#insn-00af4d8c)

~~~json
{
  "source": "00af4d8c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4db4`](#insn-00af4db4)

~~~json
{
  "source": "00af4db4",
  "target": "00af4e18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4db8`](#insn-00af4db8)

~~~json
{
  "source": "00af4db8",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4dcc`](#insn-00af4dcc)

~~~json
{
  "source": "00af4dcc",
  "target": "005e7810",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4dd0`](#insn-00af4dd0)

~~~json
{
  "source": "00af4dd0",
  "target": "00af4e20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4dd4`](#insn-00af4dd4)

~~~json
{
  "source": "00af4dd4",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4e00`](#insn-00af4e00)

~~~json
{
  "source": "00af4e00",
  "target": "00af4e24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e0c`](#insn-00af4e0c)

~~~json
{
  "source": "00af4e0c",
  "target": "00af4e24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e14`](#insn-00af4e14)

~~~json
{
  "source": "00af4e14",
  "target": "00af4e24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e1c`](#insn-00af4e1c)

~~~json
{
  "source": "00af4e1c",
  "target": "00af4e24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e24`](#insn-00af4e24)

~~~json
{
  "source": "00af4e24",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4e44`](#insn-00af4e44)

~~~json
{
  "source": "00af4e44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e48`](#insn-00af4e48)

~~~json
{
  "source": "00af4e48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4e4c`](#insn-00af4e4c)

~~~json
{
  "source": "00af4e4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
