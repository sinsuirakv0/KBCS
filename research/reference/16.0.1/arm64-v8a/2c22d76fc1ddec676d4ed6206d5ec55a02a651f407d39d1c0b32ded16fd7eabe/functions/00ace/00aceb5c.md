# 00aceb5c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ace960`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ace/00ace960.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-4010e9ef0e8a51fc8eab22229cb8b9ec)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acebcc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ace/00acebcc.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-5c2b10d5954148e001ef5fff822fe59e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aceb5c",
  "name": "FUN_00aceb5c",
  "size": 248,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bd078ecf97f3b2218232503918f40ba73ba4ac5b132d9ceca682ec726317fb6b",
  "source_text_sha256": "bd078ecf97f3b2218232503918f40ba73ba4ac5b132d9ceca682ec726317fb6b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aceb5c",
        "00acec53"
      ]
    ],
    "bytes_sha256": "408a83343412a43189f350c37a06e409be54ce071d531b120263c1a5d10e649c",
    "instruction_count": 62,
    "instruction_bytes": 248,
    "body_bytes": 248,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005e12a4](../005e1/005e12a4.md)
- [005e1620](../005e1/005e1620.md)
- [005e1750](../005e1/005e1750.md)
- [006623ec](../00662/006623ec.md)
- [00662490](../00662/00662490.md)
- [00662534](../00662/00662534.md)
- [007cceec](../007cc/007cceec.md)
- [007de8c0](../007de/007de8c0.md)
- [008c4290](../008c4/008c4290.md)
- [00a42194](../00a42/00a42194.md)
- [00a47f00](../00a47/00a47f00.md)
- [00acc5d0](../00acc/00acc5d0.md)
- [00ad0958](../00ad0/00ad0958.md)
- [00ad6f4c](../00ad6/00ad6f4c.md)
- [00aeaf94](../00aea/00aeaf94.md)
- [00aec960](../00aec/00aec960.md)

## 呼び出し先

- [0067674c](../00676/0067674c.md)
- [007bbd48](../007bb/007bbd48.md)
- [008001ec](../00800/008001ec.md)
- [008026b8](../00802/008026b8.md)
- [00802b58](../00802/00802b58.md)
- [00802ca8](../00802/00802ca8.md)
- [00802ee0](../00802/00802ee0.md)
- [008514f8](../00851/008514f8.md)
- [00a32a04](../00a32/00a32a04.md)
- [00a32e08](../00a32/00a32e08.md)
- [00a32e98](../00a32/00a32e98.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1235 bytes

~~~c

int FUN_00aceb5c(long param_1)

{
  int iVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  ulong uVar5;
  long lVar6;
  undefined8 uVar7;
  
  iVar1 = FUN_00802b58(0);
  iVar2 = FUN_00802ca8();
  iVar3 = FUN_00802ee0();
  iVar4 = 1000000000;
  if (iVar3 != 3) {
    iVar4 = 0;
  }
  uVar5 = FUN_00a32a04(param_1 + 0x530,0xffffffff,0xffffffff);
  if ((uVar5 & 1) != 0) {
    iVar1 = FUN_00a32e98(param_1 + 0x530,iVar1);
    return iVar4 + iVar2 + iVar1 * 1000;
  }
  uVar5 = FUN_00a32e08(param_1 + 0x530);
  if ((uVar5 & 1) == 0) {
    iVar3 = FUN_008026b8(0);
    if (iVar3 == -8) {
      lVar6 = FUN_008514f8();
      return *(int *)(lVar6 + 0x33a0);
    }
                    /* try { // try from 00acec04 to 00bcec37 has its CatchHandler @ 00acf96c */
    uVar5 = FUN_0067674c(param_1 + 0x13d8,1);
    if ((uVar5 & 1) == 0) {
      uVar5 = FUN_007bbd48(param_1,1);
      if ((uVar5 & 1) == 0) goto LAB_00acebd4;
      uVar7 = 0x44;
    }
    else {
      uVar7 = 0x2a;
    }
                    /* try { // try from 00acec38 to 00bcec43 has its CatchHandler @ 00acf630 */
    iVar4 = FUN_008001ec(0xfffffff8,uVar7);
    iVar4 = iVar4 * 1000;
  }
  else {
LAB_00acebd4:
    iVar4 = iVar2 + iVar1 * 1000 + iVar4;
  }
  return iVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aceb5c"></a> `00aceb5c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aceb60"></a> `00aceb60` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aceb64"></a> `00aceb64` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aceb68"></a> `00aceb68` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aceb6c"></a> `00aceb6c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aceb70"></a> `00aceb70` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aceb74"></a> `00aceb74` | `f9 cf f4 97` | bl 0x00802b58 | `UNCONDITIONAL_CALL`
<a id="insn-00aceb78"></a> `00aceb78` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aceb7c"></a> `00aceb7c` | `4b d0 f4 97` | bl 0x00802ca8 | `UNCONDITIONAL_CALL`
<a id="insn-00aceb80"></a> `00aceb80` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aceb84"></a> `00aceb84` | `d7 d0 f4 97` | bl 0x00802ee0 | `UNCONDITIONAL_CALL`
<a id="insn-00aceb88"></a> `00aceb88` | `08 40 99 52` | mov w8,#0xca00 | `FALL_THROUGH`
<a id="insn-00aceb8c"></a> `00aceb8c` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00aceb90"></a> `00aceb90` | `a0 c2 14 91` | add x0,x21,#0x530 | `FALL_THROUGH`
<a id="insn-00aceb94"></a> `00aceb94` | `48 73 a7 72` | movk w8,#0x3b9a, LSL #16 | `FALL_THROUGH`
<a id="insn-00aceb98"></a> `00aceb98` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aceb9c"></a> `00aceb9c` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aceba0"></a> `00aceba0` | `16 01 9f 1a` | csel w22,w8,wzr,eq | `FALL_THROUGH`
<a id="insn-00aceba4"></a> `00aceba4` | `98 8f fd 97` | bl 0x00a32a04 | `UNCONDITIONAL_CALL`
<a id="insn-00aceba8"></a> `00aceba8` | `00 01 00 36` | tbz w0,#0x0,0x00acebc8 | `CONDITIONAL_JUMP`
<a id="insn-00acebac"></a> `00acebac` | `a0 c2 14 91` | add x0,x21,#0x530 | `FALL_THROUGH`
<a id="insn-00acebb0"></a> `00acebb0` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00acebb4"></a> `00acebb4` | `b9 90 fd 97` | bl 0x00a32e98 | `UNCONDITIONAL_CALL`
<a id="insn-00acebb8"></a> `00acebb8` | `08 7d 80 52` | mov w8,#0x3e8 | `FALL_THROUGH`
<a id="insn-00acebbc"></a> `00acebbc` | `c9 02 13 0b` | add w9,w22,w19 | `FALL_THROUGH`
<a id="insn-00acebc0"></a> `00acebc0` | `00 24 08 1b` | madd w0,w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00acebc4"></a> `00acebc4` | `20 00 00 14` | b 0x00acec44 | `UNCONDITIONAL_JUMP`
<a id="insn-00acebc8"></a> `00acebc8` | `a0 c2 14 91` | add x0,x21,#0x530 | `FALL_THROUGH`
<a id="insn-00acebcc"></a> `00acebcc` | `8f 90 fd 97` | bl 0x00a32e08 | `UNCONDITIONAL_CALL`
<a id="insn-00acebd0"></a> `00acebd0` | `a0 00 00 36` | tbz w0,#0x0,0x00acebe4 | `CONDITIONAL_JUMP`
<a id="insn-00acebd4"></a> `00acebd4` | `08 7d 80 52` | mov w8,#0x3e8 | `FALL_THROUGH`
<a id="insn-00acebd8"></a> `00acebd8` | `88 4e 08 1b` | madd w8,w20,w8,w19 | `FALL_THROUGH`
<a id="insn-00acebdc"></a> `00acebdc` | `00 01 16 0b` | add w0,w8,w22 | `FALL_THROUGH`
<a id="insn-00acebe0"></a> `00acebe0` | `19 00 00 14` | b 0x00acec44 | `UNCONDITIONAL_JUMP`
<a id="insn-00acebe4"></a> `00acebe4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acebe8"></a> `00acebe8` | `b4 ce f4 97` | bl 0x008026b8 | `UNCONDITIONAL_CALL`
<a id="insn-00acebec"></a> `00acebec` | `1f 20 00 31` | cmn w0,#0x8 | `FALL_THROUGH`
<a id="insn-00acebf0"></a> `00acebf0` | `81 00 00 54` | b.ne 0x00acec00 | `CONDITIONAL_JUMP`
<a id="insn-00acebf4"></a> `00acebf4` | `41 0a f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acebf8"></a> `00acebf8` | `00 a0 73 b9` | ldr w0,[x0, #0x33a0] | `FALL_THROUGH`
<a id="insn-00acebfc"></a> `00acebfc` | `12 00 00 14` | b 0x00acec44 | `UNCONDITIONAL_JUMP`
<a id="insn-00acec00"></a> `00acec00` | `08 7b 82 52` | mov w8,#0x13d8 | `FALL_THROUGH`
<a id="insn-00acec04"></a> `00acec04` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acec08"></a> `00acec08` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00acec0c"></a> `00acec0c` | `d0 9e ee 97` | bl 0x0067674c | `UNCONDITIONAL_CALL`
<a id="insn-00acec10"></a> `00acec10` | `80 00 00 36` | tbz w0,#0x0,0x00acec20 | `CONDITIONAL_JUMP`
<a id="insn-00acec14"></a> `00acec14` | `e0 00 80 12` | mov w0,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00acec18"></a> `00acec18` | `41 05 80 52` | mov w1,#0x2a | `FALL_THROUGH`
<a id="insn-00acec1c"></a> `00acec1c` | `07 00 00 14` | b 0x00acec38 | `UNCONDITIONAL_JUMP`
<a id="insn-00acec20"></a> `00acec20` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acec24"></a> `00acec24` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acec28"></a> `00acec28` | `48 b4 f3 97` | bl 0x007bbd48 | `UNCONDITIONAL_CALL`
<a id="insn-00acec2c"></a> `00acec2c` | `40 fd 07 36` | tbz w0,#0x0,0x00acebd4 | `CONDITIONAL_JUMP`
<a id="insn-00acec30"></a> `00acec30` | `e0 00 80 12` | mov w0,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00acec34"></a> `00acec34` | `81 08 80 52` | mov w1,#0x44 | `FALL_THROUGH`
<a id="insn-00acec38"></a> `00acec38` | `6d c5 f4 97` | bl 0x008001ec | `UNCONDITIONAL_CALL`
<a id="insn-00acec3c"></a> `00acec3c` | `08 7d 80 52` | mov w8,#0x3e8 | `FALL_THROUGH`
<a id="insn-00acec40"></a> `00acec40` | `00 7c 08 1b` | mul w0,w0,w8 | `FALL_THROUGH`
<a id="insn-00acec44"></a> `00acec44` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acec48"></a> `00acec48` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acec4c"></a> `00acec4c` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00acec50"></a> `00acec50` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aceb5c`](#insn-00aceb5c) 範囲 `[['00aceb5c', '00acebab']]`
  - `CONDITIONAL_JUMP` [`00aceba8`](#insn-00aceba8) → [`00acebc8`](#insn-00acebc8)
  - `FALL_THROUGH` [`00aceba8`](#insn-00aceba8) → [`00acebac`](#insn-00acebac)
- ブロック [`00acebac`](#insn-00acebac) 範囲 `[['00acebac', '00acebc7']]`
  - `UNCONDITIONAL_JUMP` [`00acebc4`](#insn-00acebc4) → [`00acec44`](#insn-00acec44)
- ブロック [`00acebc8`](#insn-00acebc8) 範囲 `[['00acebc8', '00acebd3']]`
  - `CONDITIONAL_JUMP` [`00acebd0`](#insn-00acebd0) → [`00acebe4`](#insn-00acebe4)
  - `FALL_THROUGH` [`00acebd0`](#insn-00acebd0) → [`00acebd4`](#insn-00acebd4)
- ブロック [`00acebd4`](#insn-00acebd4) 範囲 `[['00acebd4', '00acebe3']]`
  - `UNCONDITIONAL_JUMP` [`00acebe0`](#insn-00acebe0) → [`00acec44`](#insn-00acec44)
- ブロック [`00acebe4`](#insn-00acebe4) 範囲 `[['00acebe4', '00acebf3']]`
  - `CONDITIONAL_JUMP` [`00acebf0`](#insn-00acebf0) → [`00acec00`](#insn-00acec00)
  - `FALL_THROUGH` [`00acebf0`](#insn-00acebf0) → [`00acebf4`](#insn-00acebf4)
- ブロック [`00acebf4`](#insn-00acebf4) 範囲 `[['00acebf4', '00acebff']]`
  - `UNCONDITIONAL_JUMP` [`00acebfc`](#insn-00acebfc) → [`00acec44`](#insn-00acec44)
- ブロック [`00acec00`](#insn-00acec00) 範囲 `[['00acec00', '00acec03']]`
  - `FALL_THROUGH` [`00acec00`](#insn-00acec00) → [`00acec04`](#insn-00acec04)
- ブロック [`00acec04`](#insn-00acec04) 範囲 `[['00acec04', '00acec13']]`
  - `CONDITIONAL_JUMP` [`00acec10`](#insn-00acec10) → [`00acec20`](#insn-00acec20)
  - `FALL_THROUGH` [`00acec10`](#insn-00acec10) → [`00acec14`](#insn-00acec14)
- ブロック [`00acec14`](#insn-00acec14) 範囲 `[['00acec14', '00acec1f']]`
  - `UNCONDITIONAL_JUMP` [`00acec1c`](#insn-00acec1c) → [`00acec38`](#insn-00acec38)
- ブロック [`00acec20`](#insn-00acec20) 範囲 `[['00acec20', '00acec2f']]`
  - `CONDITIONAL_JUMP` [`00acec2c`](#insn-00acec2c) → [`00acebd4`](#insn-00acebd4)
  - `FALL_THROUGH` [`00acec2c`](#insn-00acec2c) → [`00acec30`](#insn-00acec30)
- ブロック [`00acec30`](#insn-00acec30) 範囲 `[['00acec30', '00acec37']]`
  - `FALL_THROUGH` [`00acec34`](#insn-00acec34) → [`00acec38`](#insn-00acec38)
- ブロック [`00acec38`](#insn-00acec38) 範囲 `[['00acec38', '00acec43']]`
  - `FALL_THROUGH` [`00acec40`](#insn-00acec40) → [`00acec44`](#insn-00acec44)
- ブロック [`00acec44`](#insn-00acec44) 範囲 `[['00acec44', '00acec53']]`

## 命令位置別の参照

- [`00aceb5c`](#insn-00aceb5c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceb60`](#insn-00aceb60) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceb64`](#insn-00aceb64) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceb74`](#insn-00aceb74) → [`00802b58`](../00802/00802b58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802b58` · 推定シンボル `None` · 推定型 `None`
- [`00aceb7c`](#insn-00aceb7c) → [`00802ca8`](../00802/00802ca8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802ca8` · 推定シンボル `None` · 推定型 `None`
- [`00aceb84`](#insn-00aceb84) → [`00802ee0`](../00802/00802ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00802ee0` · 推定シンボル `None` · 推定型 `None`
- [`00aceba4`](#insn-00aceba4) → [`00a32a04`](../00a32/00a32a04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a32a04` · 推定シンボル `None` · 推定型 `None`
- [`00aceba8`](#insn-00aceba8) → [`00acebc8`](#insn-00acebc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acebb4`](#insn-00acebb4) → [`00a32e98`](../00a32/00a32e98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a32e98` · 推定シンボル `None` · 推定型 `None`
- [`00acebc4`](#insn-00acebc4) → [`00acec44`](#insn-00acec44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acebcc`](#insn-00acebcc) → [`00a32e08`](../00a32/00a32e08.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a32e08` · 推定シンボル `None` · 推定型 `None`
- [`00acebd0`](#insn-00acebd0) → [`00acebe4`](#insn-00acebe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acebe0`](#insn-00acebe0) → [`00acec44`](#insn-00acec44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acebe8`](#insn-00acebe8) → [`008026b8`](../00802/008026b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008026b8` · 推定シンボル `None` · 推定型 `None`
- [`00acebf0`](#insn-00acebf0) → [`00acec00`](#insn-00acec00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acebf4`](#insn-00acebf4) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acebfc`](#insn-00acebfc) → [`00acec44`](#insn-00acec44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec0c`](#insn-00acec0c) → [`0067674c`](../00676/0067674c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0067674c` · 推定シンボル `None` · 推定型 `None`
- [`00acec10`](#insn-00acec10) → [`00acec20`](#insn-00acec20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec1c`](#insn-00acec1c) → [`00acec38`](#insn-00acec38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec28`](#insn-00acec28) → [`007bbd48`](../007bb/007bbd48.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007bbd48` · 推定シンボル `None` · 推定型 `None`
- [`00acec2c`](#insn-00acec2c) → [`00acebd4`](#insn-00acebd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec38`](#insn-00acec38) → [`008001ec`](../00800/008001ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008001ec` · 推定シンボル `None` · 推定型 `None`
- [`00acec44`](#insn-00acec44) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec48`](#insn-00acec48) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acec4c`](#insn-00acec4c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aceb5c`](#insn-00aceb5c)

~~~json
{
  "source": "00aceb5c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceb60`](#insn-00aceb60)

~~~json
{
  "source": "00aceb60",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceb64`](#insn-00aceb64)

~~~json
{
  "source": "00aceb64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceb74`](#insn-00aceb74)

~~~json
{
  "source": "00aceb74",
  "target": "00802b58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceb7c`](#insn-00aceb7c)

~~~json
{
  "source": "00aceb7c",
  "target": "00802ca8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceb84`](#insn-00aceb84)

~~~json
{
  "source": "00aceb84",
  "target": "00802ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceba4`](#insn-00aceba4)

~~~json
{
  "source": "00aceba4",
  "target": "00a32a04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceba8`](#insn-00aceba8)

~~~json
{
  "source": "00aceba8",
  "target": "00acebc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acebb4`](#insn-00acebb4)

~~~json
{
  "source": "00acebb4",
  "target": "00a32e98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acebc4`](#insn-00acebc4)

~~~json
{
  "source": "00acebc4",
  "target": "00acec44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acebcc`](#insn-00acebcc)

~~~json
{
  "source": "00acebcc",
  "target": "00a32e08",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acebd0`](#insn-00acebd0)

~~~json
{
  "source": "00acebd0",
  "target": "00acebe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acebe0`](#insn-00acebe0)

~~~json
{
  "source": "00acebe0",
  "target": "00acec44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acebe8`](#insn-00acebe8)

~~~json
{
  "source": "00acebe8",
  "target": "008026b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acebf0`](#insn-00acebf0)

~~~json
{
  "source": "00acebf0",
  "target": "00acec00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acebf4`](#insn-00acebf4)

~~~json
{
  "source": "00acebf4",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acebfc`](#insn-00acebfc)

~~~json
{
  "source": "00acebfc",
  "target": "00acec44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec0c`](#insn-00acec0c)

~~~json
{
  "source": "00acec0c",
  "target": "0067674c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec10`](#insn-00acec10)

~~~json
{
  "source": "00acec10",
  "target": "00acec20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec1c`](#insn-00acec1c)

~~~json
{
  "source": "00acec1c",
  "target": "00acec38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec28`](#insn-00acec28)

~~~json
{
  "source": "00acec28",
  "target": "007bbd48",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec2c`](#insn-00acec2c)

~~~json
{
  "source": "00acec2c",
  "target": "00acebd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec38`](#insn-00acec38)

~~~json
{
  "source": "00acec38",
  "target": "008001ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acec44`](#insn-00acec44)

~~~json
{
  "source": "00acec44",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec48`](#insn-00acec48)

~~~json
{
  "source": "00acec48",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acec4c`](#insn-00acec4c)

~~~json
{
  "source": "00acec4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
