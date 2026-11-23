# 00aaedf8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aaeec0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aae/00aaeec0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-78dc7aba048dd086a81a7cabb1bf89c9)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaedf8",
  "name": "FUN_00aaedf8",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b4e9f31556700badd071858af53fb8f4d44086096e2300c3e4cacbd7a179780e",
  "source_text_sha256": "b4e9f31556700badd071858af53fb8f4d44086096e2300c3e4cacbd7a179780e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaedf8",
        "00aaef17"
      ]
    ],
    "bytes_sha256": "844429616cecd959a200ebc0afc16d904209ec6019fabb2c3f04e13cfebd45bc",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009bd6b8](../009bd/009bd6b8.md)

## 呼び出し先

- [0045d420](../0045d/0045d420.md)
- [0045d518](../0045d/0045d518.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1132 bytes

~~~c

void FUN_00aaedf8(undefined4 *param_1,undefined8 param_2,uint param_3)

{
  byte bVar1;
  undefined4 uVar2;
  int iVar3;
  
  uVar2 = FUN_0045d518(param_2);
  *param_1 = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[3] = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[5] = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[4] = uVar2;
  uVar2 = FUN_0045d518(param_2);
  param_1[1] = uVar2;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)(param_1 + 7) = iVar3 != 0;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)((long)param_1 + 0x1d) = iVar3 != 0;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)((long)param_1 + 0x1e) = iVar3 != 0;
  iVar3 = FUN_0045d518(param_2);
  *(bool *)((long)param_1 + 0x1f) = iVar3 != 0;
  uVar2 = FUN_0045d518(param_2);
  param_1[2] = uVar2;
  if (0x23 < (int)param_3) {
    iVar3 = FUN_0045d518(param_2);
    *(bool *)(param_1 + 8) = iVar3 != 0;
    if (0x9dc < param_3 >> 5) {
      iVar3 = FUN_0045d518(param_2);
      *(bool *)(param_1 + 9) = iVar3 != 0;
      if (0x18703 < param_3) {
        bVar1 = FUN_0045d420(param_2);
        *(byte *)(param_1 + 0xb) = bVar1 & 1;
      }
    }
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaedf8"></a> `00aaedf8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00aaedfc"></a> `00aaedfc` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaee00"></a> `00aaee00` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaee04"></a> `00aaee04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aaee08"></a> `00aaee08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aaee0c"></a> `00aaee0c` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00aaee10"></a> `00aaee10` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00aaee14"></a> `00aaee14` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00aaee18"></a> `00aaee18` | `c0 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaee1c"></a> `00aaee1c` | `60 02 00 b9` | str w0,[x19] | `FALL_THROUGH`
<a id="insn-00aaee20"></a> `00aaee20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaee24"></a> `00aaee24` | `bd b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaee28"></a> `00aaee28` | `60 0e 00 b9` | str w0,[x19, #0xc] | `FALL_THROUGH`
<a id="insn-00aaee2c"></a> `00aaee2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaee30"></a> `00aaee30` | `ba b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaee34"></a> `00aaee34` | `60 16 00 b9` | str w0,[x19, #0x14] | `FALL_THROUGH`
<a id="insn-00aaee38"></a> `00aaee38` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaee3c"></a> `00aaee3c` | `b7 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaee40"></a> `00aaee40` | `60 12 00 b9` | str w0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00aaee44"></a> `00aaee44` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaee48"></a> `00aaee48` | `b4 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaee4c"></a> `00aaee4c` | `60 06 00 b9` | str w0,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00aaee50"></a> `00aaee50` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaee54"></a> `00aaee54` | `b1 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaee58"></a> `00aaee58` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaee5c"></a> `00aaee5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaee60"></a> `00aaee60` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00aaee64"></a> `00aaee64` | `68 72 00 39` | strb w8,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00aaee68"></a> `00aaee68` | `ac b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaee6c"></a> `00aaee6c` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaee70"></a> `00aaee70` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaee74"></a> `00aaee74` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00aaee78"></a> `00aaee78` | `68 76 00 39` | strb w8,[x19, #0x1d] | `FALL_THROUGH`
<a id="insn-00aaee7c"></a> `00aaee7c` | `a7 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaee80"></a> `00aaee80` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaee84"></a> `00aaee84` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaee88"></a> `00aaee88` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00aaee8c"></a> `00aaee8c` | `68 7a 00 39` | strb w8,[x19, #0x1e] | `FALL_THROUGH`
<a id="insn-00aaee90"></a> `00aaee90` | `a2 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaee94"></a> `00aaee94` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaee98"></a> `00aaee98` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaee9c"></a> `00aaee9c` | `e8 07 9f 1a` | cset w8,ne | `FALL_THROUGH`
<a id="insn-00aaeea0"></a> `00aaeea0` | `68 7e 00 39` | strb w8,[x19, #0x1f] | `FALL_THROUGH`
<a id="insn-00aaeea4"></a> `00aaeea4` | `9d b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeea8"></a> `00aaeea8` | `bf 92 00 71` | cmp w21,#0x24 | `FALL_THROUGH`
<a id="insn-00aaeeac"></a> `00aaeeac` | `60 0a 00 b9` | str w0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aaeeb0"></a> `00aaeeb0` | `cb 02 00 54` | b.lt 0x00aaef08 | `CONDITIONAL_JUMP`
<a id="insn-00aaeeb4"></a> `00aaeeb4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaeeb8"></a> `00aaeeb8` | `98 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeebc"></a> `00aaeebc` | `a8 7e 05 53` | lsr w8,w21,#0x5 | `FALL_THROUGH`
<a id="insn-00aaeec0"></a> `00aaeec0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaeec4"></a> `00aaeec4` | `e9 07 9f 1a` | cset w9,ne | `FALL_THROUGH`
<a id="insn-00aaeec8"></a> `00aaeec8` | `1f 75 27 71` | cmp w8,#0x9dd | `FALL_THROUGH`
<a id="insn-00aaeecc"></a> `00aaeecc` | `69 82 00 39` | strb w9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00aaeed0"></a> `00aaeed0` | `c3 01 00 54` | b.cc 0x00aaef08 | `CONDITIONAL_JUMP`
<a id="insn-00aaeed4"></a> `00aaeed4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaeed8"></a> `00aaeed8` | `90 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeedc"></a> `00aaeedc` | `88 e0 90 52` | mov w8,#0x8704 | `FALL_THROUGH`
<a id="insn-00aaeee0"></a> `00aaeee0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00aaeee4"></a> `00aaeee4` | `28 00 a0 72` | movk w8,#0x1, LSL #16 | `FALL_THROUGH`
<a id="insn-00aaeee8"></a> `00aaeee8` | `e9 07 9f 1a` | cset w9,ne | `FALL_THROUGH`
<a id="insn-00aaeeec"></a> `00aaeeec` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00aaeef0"></a> `00aaeef0` | `69 92 00 39` | strb w9,[x19, #0x24] | `FALL_THROUGH`
<a id="insn-00aaeef4"></a> `00aaeef4` | `a3 00 00 54` | b.cc 0x00aaef08 | `CONDITIONAL_JUMP`
<a id="insn-00aaeef8"></a> `00aaeef8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaeefc"></a> `00aaeefc` | `49 b9 e6 97` | bl 0x0045d420 | `UNCONDITIONAL_CALL`
<a id="insn-00aaef00"></a> `00aaef00` | `08 00 00 12` | and w8,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aaef04"></a> `00aaef04` | `68 b2 00 39` | strb w8,[x19, #0x2c] | `FALL_THROUGH`
<a id="insn-00aaef08"></a> `00aaef08` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaef0c"></a> `00aaef0c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaef10"></a> `00aaef10` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00aaef14"></a> `00aaef14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaedf8`](#insn-00aaedf8) 範囲 `[['00aaedf8', '00aaeeb3']]`
  - `CONDITIONAL_JUMP` [`00aaeeb0`](#insn-00aaeeb0) → [`00aaef08`](#insn-00aaef08)
  - `FALL_THROUGH` [`00aaeeb0`](#insn-00aaeeb0) → [`00aaeeb4`](#insn-00aaeeb4)
- ブロック [`00aaeeb4`](#insn-00aaeeb4) 範囲 `[['00aaeeb4', '00aaeed3']]`
  - `CONDITIONAL_JUMP` [`00aaeed0`](#insn-00aaeed0) → [`00aaef08`](#insn-00aaef08)
  - `FALL_THROUGH` [`00aaeed0`](#insn-00aaeed0) → [`00aaeed4`](#insn-00aaeed4)
- ブロック [`00aaeed4`](#insn-00aaeed4) 範囲 `[['00aaeed4', '00aaeef7']]`
  - `CONDITIONAL_JUMP` [`00aaeef4`](#insn-00aaeef4) → [`00aaef08`](#insn-00aaef08)
  - `FALL_THROUGH` [`00aaeef4`](#insn-00aaeef4) → [`00aaeef8`](#insn-00aaeef8)
- ブロック [`00aaeef8`](#insn-00aaeef8) 範囲 `[['00aaeef8', '00aaef07']]`
  - `FALL_THROUGH` [`00aaef04`](#insn-00aaef04) → [`00aaef08`](#insn-00aaef08)
- ブロック [`00aaef08`](#insn-00aaef08) 範囲 `[['00aaef08', '00aaef17']]`

## 命令位置別の参照

- [`00aaedf8`](#insn-00aaedf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaedfc`](#insn-00aaedfc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaee00`](#insn-00aaee00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaee18`](#insn-00aaee18) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaee24`](#insn-00aaee24) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaee30`](#insn-00aaee30) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaee3c`](#insn-00aaee3c) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaee48`](#insn-00aaee48) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaee54`](#insn-00aaee54) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaee68`](#insn-00aaee68) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaee7c`](#insn-00aaee7c) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaee90`](#insn-00aaee90) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaeea4`](#insn-00aaeea4) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaeeb0`](#insn-00aaeeb0) → [`00aaef08`](#insn-00aaef08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeeb8`](#insn-00aaeeb8) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaeed0`](#insn-00aaeed0) → [`00aaef08`](#insn-00aaef08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeed8`](#insn-00aaeed8) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaeef4`](#insn-00aaeef4) → [`00aaef08`](#insn-00aaef08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeefc`](#insn-00aaeefc) → [`0045d420`](../0045d/0045d420.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d420` · 推定シンボル `None` · 推定型 `None`
- [`00aaef08`](#insn-00aaef08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaef0c`](#insn-00aaef0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaef10`](#insn-00aaef10) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaedf8`](#insn-00aaedf8)

~~~json
{
  "source": "00aaedf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaedfc`](#insn-00aaedfc)

~~~json
{
  "source": "00aaedfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaee00`](#insn-00aaee00)

~~~json
{
  "source": "00aaee00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaee18`](#insn-00aaee18)

~~~json
{
  "source": "00aaee18",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaee24`](#insn-00aaee24)

~~~json
{
  "source": "00aaee24",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaee30`](#insn-00aaee30)

~~~json
{
  "source": "00aaee30",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaee3c`](#insn-00aaee3c)

~~~json
{
  "source": "00aaee3c",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaee48`](#insn-00aaee48)

~~~json
{
  "source": "00aaee48",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaee54`](#insn-00aaee54)

~~~json
{
  "source": "00aaee54",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaee68`](#insn-00aaee68)

~~~json
{
  "source": "00aaee68",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaee7c`](#insn-00aaee7c)

~~~json
{
  "source": "00aaee7c",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaee90`](#insn-00aaee90)

~~~json
{
  "source": "00aaee90",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeea4`](#insn-00aaeea4)

~~~json
{
  "source": "00aaeea4",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeeb0`](#insn-00aaeeb0)

~~~json
{
  "source": "00aaeeb0",
  "target": "00aaef08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeeb8`](#insn-00aaeeb8)

~~~json
{
  "source": "00aaeeb8",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeed0`](#insn-00aaeed0)

~~~json
{
  "source": "00aaeed0",
  "target": "00aaef08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeed8`](#insn-00aaeed8)

~~~json
{
  "source": "00aaeed8",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaeef4`](#insn-00aaeef4)

~~~json
{
  "source": "00aaeef4",
  "target": "00aaef08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeefc`](#insn-00aaeefc)

~~~json
{
  "source": "00aaeefc",
  "target": "0045d420",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaef08`](#insn-00aaef08)

~~~json
{
  "source": "00aaef08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaef0c`](#insn-00aaef0c)

~~~json
{
  "source": "00aaef0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaef10`](#insn-00aaef10)

~~~json
{
  "source": "00aaef10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
