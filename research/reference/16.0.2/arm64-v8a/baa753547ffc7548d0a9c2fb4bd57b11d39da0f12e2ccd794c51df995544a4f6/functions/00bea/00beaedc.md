# 00beaedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00beae40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bea/00beae40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/no_difference_in_scope-0014.md#compare-84c73ebbb4fccad8332d4ffa060fb1a6)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bebed0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00beb/00bebed0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/no_difference_in_scope-0013.md#compare-c87963a3e21e631496440d91576976e2)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beaedc",
  "name": "FUN_00beaedc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c45a72cf2ffda3dadceac383fe92453732998a122c9f231fa1e67a16bf9d6912",
  "source_text_sha256": "c45a72cf2ffda3dadceac383fe92453732998a122c9f231fa1e67a16bf9d6912",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beaedc",
        "00beb003"
      ]
    ],
    "bytes_sha256": "b5200948dd1e3aaaffd41d55a0a924df7f49c5b1e4216c9b93c1ad07d69f5c43",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be3fbc](../00be3/00be3fbc.md)
- [00beac1c](../00bea/00beac1c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1767 bytes

~~~c

void FUN_00beaedc(short *param_1,short *param_2,short *param_3,short *param_4,short *param_5)

{
  short sVar1;
  short sVar2;
  short sVar3;
  
  sVar1 = *param_2;
  sVar2 = *param_1;
  sVar3 = *param_3;
  if (sVar1 < sVar2) {
    if (sVar3 < sVar1) {
      *param_1 = sVar3;
    }
    else {
      *param_1 = sVar1;
      *param_2 = sVar2;
      sVar3 = *param_3;
      if (sVar2 <= sVar3) goto LAB_00beaf5c;
      *param_2 = sVar3;
    }
    *param_3 = sVar2;
    sVar3 = sVar2;
  }
  else if (sVar3 < sVar1) {
    *param_2 = sVar3;
    *param_3 = sVar1;
    sVar2 = *param_1;
    sVar3 = sVar1;
    if (*param_2 < sVar2) {
      *param_1 = *param_2;
      *param_2 = sVar2;
      sVar3 = *param_3;
    }
  }
LAB_00beaf5c:
  if (*param_4 < sVar3) {
    *param_3 = *param_4;
    *param_4 = sVar3;
    sVar3 = *param_2;
    if (*param_3 < sVar3) {
      *param_2 = *param_3;
      *param_3 = sVar3;
      sVar3 = *param_1;
      if (*param_2 < sVar3) {
        *param_1 = *param_2;
        *param_2 = sVar3;
      }
    }
  }
  sVar3 = *param_4;
  if (*param_5 < sVar3) {
    *param_4 = *param_5;
    *param_5 = sVar3;
    sVar3 = *param_3;
    if (*param_4 < sVar3) {
      *param_3 = *param_4;
      *param_4 = sVar3;
      sVar3 = *param_2;
      if (*param_3 < sVar3) {
        *param_2 = *param_3;
        *param_3 = sVar3;
        sVar3 = *param_1;
                    /* try { // try from 00beaff0 to 00ceaff7 has its CatchHandler @ 00beaff8 */
        if (*param_2 < sVar3) {
                    /* catch() { ... } // from try @ 00beaff0 with catch @ 00beaff8
                       try { // try from 00beaff8 to 00ceb02f has its CatchHandler @ 00beae8c */
          *param_1 = *param_2;
          *param_2 = sVar3;
        }
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
<a id="insn-00beaedc"></a> `00beaedc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00beaee0"></a> `00beaee0` | `28 00 c0 79` | ldrsh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beaee4"></a> `00beaee4` | `09 00 c0 79` | ldrsh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beaee8"></a> `00beaee8` | `4a 00 c0 79` | ldrsh w10,[x2] | `FALL_THROUGH`
<a id="insn-00beaeec"></a> `00beaeec` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beaef0"></a> `00beaef0` | `aa 00 00 54` | b.ge 0x00beaf04 | `CONDITIONAL_JUMP`
<a id="insn-00beaef4"></a> `00beaef4` | `5f 01 08 6b` | cmp w10,w8 | `FALL_THROUGH`
<a id="insn-00beaef8"></a> `00beaef8` | `ea 01 00 54` | b.ge 0x00beaf34 | `CONDITIONAL_JUMP`
<a id="insn-00beaefc"></a> `00beaefc` | `0a 00 00 79` | strh w10,[x0] | `FALL_THROUGH`
<a id="insn-00beaf00"></a> `00beaf00` | `13 00 00 14` | b 0x00beaf4c | `UNCONDITIONAL_JUMP`
<a id="insn-00beaf04"></a> `00beaf04` | `5f 01 08 6b` | cmp w10,w8 | `FALL_THROUGH`
<a id="insn-00beaf08"></a> `00beaf08` | `8a 02 00 54` | b.ge 0x00beaf58 | `CONDITIONAL_JUMP`
<a id="insn-00beaf0c"></a> `00beaf0c` | `2a 00 00 79` | strh w10,[x1] | `FALL_THROUGH`
<a id="insn-00beaf10"></a> `00beaf10` | `48 00 00 79` | strh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beaf14"></a> `00beaf14` | `29 00 c0 79` | ldrsh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beaf18"></a> `00beaf18` | `0a 00 c0 79` | ldrsh w10,[x0] | `FALL_THROUGH`
<a id="insn-00beaf1c"></a> `00beaf1c` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00beaf20"></a> `00beaf20` | `ea 01 00 54` | b.ge 0x00beaf5c | `CONDITIONAL_JUMP`
<a id="insn-00beaf24"></a> `00beaf24` | `09 00 00 79` | strh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beaf28"></a> `00beaf28` | `2a 00 00 79` | strh w10,[x1] | `FALL_THROUGH`
<a id="insn-00beaf2c"></a> `00beaf2c` | `48 00 40 79` | ldrh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beaf30"></a> `00beaf30` | `0b 00 00 14` | b 0x00beaf5c | `UNCONDITIONAL_JUMP`
<a id="insn-00beaf34"></a> `00beaf34` | `08 00 00 79` | strh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beaf38"></a> `00beaf38` | `29 00 00 79` | strh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beaf3c"></a> `00beaf3c` | `48 00 c0 79` | ldrsh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beaf40"></a> `00beaf40` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beaf44"></a> `00beaf44` | `ca 00 00 54` | b.ge 0x00beaf5c | `CONDITIONAL_JUMP`
<a id="insn-00beaf48"></a> `00beaf48` | `28 00 00 79` | strh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beaf4c"></a> `00beaf4c` | `e8 03 09 2a` | mov w8,w9 | `FALL_THROUGH`
<a id="insn-00beaf50"></a> `00beaf50` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00beaf54"></a> `00beaf54` | `02 00 00 14` | b 0x00beaf5c | `UNCONDITIONAL_JUMP`
<a id="insn-00beaf58"></a> `00beaf58` | `e8 03 0a 2a` | mov w8,w10 | `FALL_THROUGH`
<a id="insn-00beaf5c"></a> `00beaf5c` | `69 00 c0 79` | ldrsh w9,[x3] | `FALL_THROUGH`
<a id="insn-00beaf60"></a> `00beaf60` | `3f a1 28 6b` | cmp w9,w8, SXTH  | `FALL_THROUGH`
<a id="insn-00beaf64"></a> `00beaf64` | `ea 01 00 54` | b.ge 0x00beafa0 | `CONDITIONAL_JUMP`
<a id="insn-00beaf68"></a> `00beaf68` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00beaf6c"></a> `00beaf6c` | `68 00 00 79` | strh w8,[x3] | `FALL_THROUGH`
<a id="insn-00beaf70"></a> `00beaf70` | `48 00 c0 79` | ldrsh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beaf74"></a> `00beaf74` | `29 00 c0 79` | ldrsh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beaf78"></a> `00beaf78` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beaf7c"></a> `00beaf7c` | `2a 01 00 54` | b.ge 0x00beafa0 | `CONDITIONAL_JUMP`
<a id="insn-00beaf80"></a> `00beaf80` | `28 00 00 79` | strh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beaf84"></a> `00beaf84` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00beaf88"></a> `00beaf88` | `28 00 c0 79` | ldrsh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beaf8c"></a> `00beaf8c` | `09 00 c0 79` | ldrsh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beaf90"></a> `00beaf90` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beaf94"></a> `00beaf94` | `6a 00 00 54` | b.ge 0x00beafa0 | `CONDITIONAL_JUMP`
<a id="insn-00beaf98"></a> `00beaf98` | `08 00 00 79` | strh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beaf9c"></a> `00beaf9c` | `29 00 00 79` | strh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beafa0"></a> `00beafa0` | `88 00 c0 79` | ldrsh w8,[x4] | `FALL_THROUGH`
<a id="insn-00beafa4"></a> `00beafa4` | `69 00 c0 79` | ldrsh w9,[x3] | `FALL_THROUGH`
<a id="insn-00beafa8"></a> `00beafa8` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beafac"></a> `00beafac` | `aa 02 00 54` | b.ge 0x00beb000 | `CONDITIONAL_JUMP`
<a id="insn-00beafb0"></a> `00beafb0` | `68 00 00 79` | strh w8,[x3] | `FALL_THROUGH`
<a id="insn-00beafb4"></a> `00beafb4` | `89 00 00 79` | strh w9,[x4] | `FALL_THROUGH`
<a id="insn-00beafb8"></a> `00beafb8` | `68 00 c0 79` | ldrsh w8,[x3] | `FALL_THROUGH`
<a id="insn-00beafbc"></a> `00beafbc` | `49 00 c0 79` | ldrsh w9,[x2] | `FALL_THROUGH`
<a id="insn-00beafc0"></a> `00beafc0` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beafc4"></a> `00beafc4` | `ea 01 00 54` | b.ge 0x00beb000 | `CONDITIONAL_JUMP`
<a id="insn-00beafc8"></a> `00beafc8` | `48 00 00 79` | strh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beafcc"></a> `00beafcc` | `69 00 00 79` | strh w9,[x3] | `FALL_THROUGH`
<a id="insn-00beafd0"></a> `00beafd0` | `48 00 c0 79` | ldrsh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beafd4"></a> `00beafd4` | `29 00 c0 79` | ldrsh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beafd8"></a> `00beafd8` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beafdc"></a> `00beafdc` | `2a 01 00 54` | b.ge 0x00beb000 | `CONDITIONAL_JUMP`
<a id="insn-00beafe0"></a> `00beafe0` | `28 00 00 79` | strh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beafe4"></a> `00beafe4` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00beafe8"></a> `00beafe8` | `28 00 c0 79` | ldrsh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beafec"></a> `00beafec` | `09 00 c0 79` | ldrsh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beaff0"></a> `00beaff0` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beaff4"></a> `00beaff4` | `6a 00 00 54` | b.ge 0x00beb000 | `CONDITIONAL_JUMP`
<a id="insn-00beaff8"></a> `00beaff8` | `08 00 00 79` | strh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beaffc"></a> `00beaffc` | `29 00 00 79` | strh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beb000"></a> `00beb000` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00beaedc`](#insn-00beaedc) 範囲 `[['00beaedc', '00beaef3']]`
  - `CONDITIONAL_JUMP` [`00beaef0`](#insn-00beaef0) → [`00beaf04`](#insn-00beaf04)
  - `FALL_THROUGH` [`00beaef0`](#insn-00beaef0) → [`00beaef4`](#insn-00beaef4)
- ブロック [`00beaef4`](#insn-00beaef4) 範囲 `[['00beaef4', '00beaefb']]`
  - `CONDITIONAL_JUMP` [`00beaef8`](#insn-00beaef8) → [`00beaf34`](#insn-00beaf34)
  - `FALL_THROUGH` [`00beaef8`](#insn-00beaef8) → [`00beaefc`](#insn-00beaefc)
- ブロック [`00beaefc`](#insn-00beaefc) 範囲 `[['00beaefc', '00beaf03']]`
  - `UNCONDITIONAL_JUMP` [`00beaf00`](#insn-00beaf00) → [`00beaf4c`](#insn-00beaf4c)
- ブロック [`00beaf04`](#insn-00beaf04) 範囲 `[['00beaf04', '00beaf0b']]`
  - `CONDITIONAL_JUMP` [`00beaf08`](#insn-00beaf08) → [`00beaf58`](#insn-00beaf58)
  - `FALL_THROUGH` [`00beaf08`](#insn-00beaf08) → [`00beaf0c`](#insn-00beaf0c)
- ブロック [`00beaf0c`](#insn-00beaf0c) 範囲 `[['00beaf0c', '00beaf23']]`
  - `CONDITIONAL_JUMP` [`00beaf20`](#insn-00beaf20) → [`00beaf5c`](#insn-00beaf5c)
  - `FALL_THROUGH` [`00beaf20`](#insn-00beaf20) → [`00beaf24`](#insn-00beaf24)
- ブロック [`00beaf24`](#insn-00beaf24) 範囲 `[['00beaf24', '00beaf33']]`
  - `UNCONDITIONAL_JUMP` [`00beaf30`](#insn-00beaf30) → [`00beaf5c`](#insn-00beaf5c)
- ブロック [`00beaf34`](#insn-00beaf34) 範囲 `[['00beaf34', '00beaf47']]`
  - `CONDITIONAL_JUMP` [`00beaf44`](#insn-00beaf44) → [`00beaf5c`](#insn-00beaf5c)
  - `FALL_THROUGH` [`00beaf44`](#insn-00beaf44) → [`00beaf48`](#insn-00beaf48)
- ブロック [`00beaf48`](#insn-00beaf48) 範囲 `[['00beaf48', '00beaf4b']]`
  - `FALL_THROUGH` [`00beaf48`](#insn-00beaf48) → [`00beaf4c`](#insn-00beaf4c)
- ブロック [`00beaf4c`](#insn-00beaf4c) 範囲 `[['00beaf4c', '00beaf57']]`
  - `UNCONDITIONAL_JUMP` [`00beaf54`](#insn-00beaf54) → [`00beaf5c`](#insn-00beaf5c)
- ブロック [`00beaf58`](#insn-00beaf58) 範囲 `[['00beaf58', '00beaf5b']]`
  - `FALL_THROUGH` [`00beaf58`](#insn-00beaf58) → [`00beaf5c`](#insn-00beaf5c)
- ブロック [`00beaf5c`](#insn-00beaf5c) 範囲 `[['00beaf5c', '00beaf67']]`
  - `CONDITIONAL_JUMP` [`00beaf64`](#insn-00beaf64) → [`00beafa0`](#insn-00beafa0)
  - `FALL_THROUGH` [`00beaf64`](#insn-00beaf64) → [`00beaf68`](#insn-00beaf68)
- ブロック [`00beaf68`](#insn-00beaf68) 範囲 `[['00beaf68', '00beaf7f']]`
  - `CONDITIONAL_JUMP` [`00beaf7c`](#insn-00beaf7c) → [`00beafa0`](#insn-00beafa0)
  - `FALL_THROUGH` [`00beaf7c`](#insn-00beaf7c) → [`00beaf80`](#insn-00beaf80)
- ブロック [`00beaf80`](#insn-00beaf80) 範囲 `[['00beaf80', '00beaf97']]`
  - `CONDITIONAL_JUMP` [`00beaf94`](#insn-00beaf94) → [`00beafa0`](#insn-00beafa0)
  - `FALL_THROUGH` [`00beaf94`](#insn-00beaf94) → [`00beaf98`](#insn-00beaf98)
- ブロック [`00beaf98`](#insn-00beaf98) 範囲 `[['00beaf98', '00beaf9f']]`
  - `FALL_THROUGH` [`00beaf9c`](#insn-00beaf9c) → [`00beafa0`](#insn-00beafa0)
- ブロック [`00beafa0`](#insn-00beafa0) 範囲 `[['00beafa0', '00beafaf']]`
  - `CONDITIONAL_JUMP` [`00beafac`](#insn-00beafac) → [`00beb000`](#insn-00beb000)
  - `FALL_THROUGH` [`00beafac`](#insn-00beafac) → [`00beafb0`](#insn-00beafb0)
- ブロック [`00beafb0`](#insn-00beafb0) 範囲 `[['00beafb0', '00beafc7']]`
  - `CONDITIONAL_JUMP` [`00beafc4`](#insn-00beafc4) → [`00beb000`](#insn-00beb000)
  - `FALL_THROUGH` [`00beafc4`](#insn-00beafc4) → [`00beafc8`](#insn-00beafc8)
- ブロック [`00beafc8`](#insn-00beafc8) 範囲 `[['00beafc8', '00beafdf']]`
  - `CONDITIONAL_JUMP` [`00beafdc`](#insn-00beafdc) → [`00beb000`](#insn-00beb000)
  - `FALL_THROUGH` [`00beafdc`](#insn-00beafdc) → [`00beafe0`](#insn-00beafe0)
- ブロック [`00beafe0`](#insn-00beafe0) 範囲 `[['00beafe0', '00beafef']]`
  - `FALL_THROUGH` [`00beafec`](#insn-00beafec) → [`00beaff0`](#insn-00beaff0)
- ブロック [`00beaff0`](#insn-00beaff0) 範囲 `[['00beaff0', '00beaff7']]`
  - `CONDITIONAL_JUMP` [`00beaff4`](#insn-00beaff4) → [`00beb000`](#insn-00beb000)
  - `FALL_THROUGH` [`00beaff4`](#insn-00beaff4) → [`00beaff8`](#insn-00beaff8)
- ブロック [`00beaff8`](#insn-00beaff8) 範囲 `[['00beaff8', '00beafff']]`
  - `FALL_THROUGH` [`00beaffc`](#insn-00beaffc) → [`00beb000`](#insn-00beb000)
- ブロック [`00beb000`](#insn-00beb000) 範囲 `[['00beb000', '00beb003']]`

## 命令位置別の参照

- [`00beaef0`](#insn-00beaef0) → [`00beaf04`](#insn-00beaf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaef8`](#insn-00beaef8) → [`00beaf34`](#insn-00beaf34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf00`](#insn-00beaf00) → [`00beaf4c`](#insn-00beaf4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf08`](#insn-00beaf08) → [`00beaf58`](#insn-00beaf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf20`](#insn-00beaf20) → [`00beaf5c`](#insn-00beaf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf30`](#insn-00beaf30) → [`00beaf5c`](#insn-00beaf5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf44`](#insn-00beaf44) → [`00beaf5c`](#insn-00beaf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf54`](#insn-00beaf54) → [`00beaf5c`](#insn-00beaf5c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf64`](#insn-00beaf64) → [`00beafa0`](#insn-00beafa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf7c`](#insn-00beaf7c) → [`00beafa0`](#insn-00beafa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaf94`](#insn-00beaf94) → [`00beafa0`](#insn-00beafa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beafac`](#insn-00beafac) → [`00beb000`](#insn-00beb000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beafc4`](#insn-00beafc4) → [`00beb000`](#insn-00beb000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beafdc`](#insn-00beafdc) → [`00beb000`](#insn-00beb000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beaff4`](#insn-00beaff4) → [`00beb000`](#insn-00beb000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beaef0`](#insn-00beaef0)

~~~json
{
  "source": "00beaef0",
  "target": "00beaf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaef8`](#insn-00beaef8)

~~~json
{
  "source": "00beaef8",
  "target": "00beaf34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf00`](#insn-00beaf00)

~~~json
{
  "source": "00beaf00",
  "target": "00beaf4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf08`](#insn-00beaf08)

~~~json
{
  "source": "00beaf08",
  "target": "00beaf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf20`](#insn-00beaf20)

~~~json
{
  "source": "00beaf20",
  "target": "00beaf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf30`](#insn-00beaf30)

~~~json
{
  "source": "00beaf30",
  "target": "00beaf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf44`](#insn-00beaf44)

~~~json
{
  "source": "00beaf44",
  "target": "00beaf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf54`](#insn-00beaf54)

~~~json
{
  "source": "00beaf54",
  "target": "00beaf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf64`](#insn-00beaf64)

~~~json
{
  "source": "00beaf64",
  "target": "00beafa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf7c`](#insn-00beaf7c)

~~~json
{
  "source": "00beaf7c",
  "target": "00beafa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaf94`](#insn-00beaf94)

~~~json
{
  "source": "00beaf94",
  "target": "00beafa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beafac`](#insn-00beafac)

~~~json
{
  "source": "00beafac",
  "target": "00beb000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beafc4`](#insn-00beafc4)

~~~json
{
  "source": "00beafc4",
  "target": "00beb000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beafdc`](#insn-00beafdc)

~~~json
{
  "source": "00beafdc",
  "target": "00beb000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beaff4`](#insn-00beaff4)

~~~json
{
  "source": "00beaff4",
  "target": "00beb000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
