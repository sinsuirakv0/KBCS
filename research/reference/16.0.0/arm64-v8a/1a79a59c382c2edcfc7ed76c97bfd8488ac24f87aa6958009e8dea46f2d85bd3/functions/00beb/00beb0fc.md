# 00beb0fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 対応未確定
  - [v15.7.4 → v16.0.0 版の比較一覧](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/README.md)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00beb524`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00beb/00beb524.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/no_difference_in_scope-0013.md#compare-8a348b5749dd44d1e9241e0ec3e4f505)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00beb0fc",
  "name": "FUN_00beb0fc",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8dd1ba89603590d17eb6dfdce1882ed806fc982d23a33e0ed1fbf7bfa9033a3e",
  "source_text_sha256": "8dd1ba89603590d17eb6dfdce1882ed806fc982d23a33e0ed1fbf7bfa9033a3e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00beb0fc",
        "00beb223"
      ]
    ],
    "bytes_sha256": "067d6b89e230520320a5b362002681080171dcb8ef6e8b988d404d966c69fda7",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be4234](../00be4/00be4234.md)
- [00beae3c](../00bea/00beae3c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1497 bytes

~~~c

void FUN_00beb0fc(ushort *param_1,ushort *param_2,ushort *param_3,ushort *param_4,ushort *param_5)

{
  ushort uVar1;
  ushort uVar2;
  ushort uVar3;
  
  uVar1 = *param_2;
  uVar2 = *param_1;
  uVar3 = *param_3;
  if (uVar1 < uVar2) {
    if (uVar3 < uVar1) {
      *param_1 = uVar3;
    }
    else {
      *param_1 = uVar1;
      *param_2 = uVar2;
      uVar3 = *param_3;
      if (uVar2 <= uVar3) goto LAB_00beb17c;
      *param_2 = uVar3;
    }
    *param_3 = uVar2;
    uVar3 = uVar2;
  }
  else if (uVar3 < uVar1) {
    *param_2 = uVar3;
    *param_3 = uVar1;
    uVar2 = *param_1;
    uVar3 = uVar1;
    if (*param_2 < uVar2) {
      *param_1 = *param_2;
      *param_2 = uVar2;
      uVar3 = *param_3;
    }
  }
LAB_00beb17c:
  if (*param_4 < uVar3) {
    *param_3 = *param_4;
    *param_4 = uVar3;
    uVar1 = *param_2;
    if (*param_3 < uVar1) {
      *param_2 = *param_3;
      *param_3 = uVar1;
      uVar1 = *param_1;
      if (*param_2 < uVar1) {
        *param_1 = *param_2;
        *param_2 = uVar1;
      }
    }
  }
  uVar1 = *param_4;
  if (*param_5 < uVar1) {
    *param_4 = *param_5;
    *param_5 = uVar1;
    uVar1 = *param_3;
    if (*param_4 < uVar1) {
      *param_3 = *param_4;
      *param_4 = uVar1;
      uVar1 = *param_2;
      if (*param_3 < uVar1) {
        *param_2 = *param_3;
        *param_3 = uVar1;
        uVar1 = *param_1;
        if (*param_2 < uVar1) {
          *param_1 = *param_2;
          *param_2 = uVar1;
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
<a id="insn-00beb0fc"></a> `00beb0fc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00beb100"></a> `00beb100` | `28 00 40 79` | ldrh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beb104"></a> `00beb104` | `09 00 40 79` | ldrh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beb108"></a> `00beb108` | `4a 00 40 79` | ldrh w10,[x2] | `FALL_THROUGH`
<a id="insn-00beb10c"></a> `00beb10c` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beb110"></a> `00beb110` | `a2 00 00 54` | b.cs 0x00beb124 | `CONDITIONAL_JUMP`
<a id="insn-00beb114"></a> `00beb114` | `5f 01 08 6b` | cmp w10,w8 | `FALL_THROUGH`
<a id="insn-00beb118"></a> `00beb118` | `e2 01 00 54` | b.cs 0x00beb154 | `CONDITIONAL_JUMP`
<a id="insn-00beb11c"></a> `00beb11c` | `0a 00 00 79` | strh w10,[x0] | `FALL_THROUGH`
<a id="insn-00beb120"></a> `00beb120` | `13 00 00 14` | b 0x00beb16c | `UNCONDITIONAL_JUMP`
<a id="insn-00beb124"></a> `00beb124` | `5f 01 08 6b` | cmp w10,w8 | `FALL_THROUGH`
<a id="insn-00beb128"></a> `00beb128` | `82 02 00 54` | b.cs 0x00beb178 | `CONDITIONAL_JUMP`
<a id="insn-00beb12c"></a> `00beb12c` | `2a 00 00 79` | strh w10,[x1] | `FALL_THROUGH`
<a id="insn-00beb130"></a> `00beb130` | `48 00 00 79` | strh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beb134"></a> `00beb134` | `29 00 40 79` | ldrh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beb138"></a> `00beb138` | `0a 00 40 79` | ldrh w10,[x0] | `FALL_THROUGH`
<a id="insn-00beb13c"></a> `00beb13c` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00beb140"></a> `00beb140` | `e2 01 00 54` | b.cs 0x00beb17c | `CONDITIONAL_JUMP`
<a id="insn-00beb144"></a> `00beb144` | `09 00 00 79` | strh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beb148"></a> `00beb148` | `2a 00 00 79` | strh w10,[x1] | `FALL_THROUGH`
<a id="insn-00beb14c"></a> `00beb14c` | `48 00 40 79` | ldrh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beb150"></a> `00beb150` | `0b 00 00 14` | b 0x00beb17c | `UNCONDITIONAL_JUMP`
<a id="insn-00beb154"></a> `00beb154` | `08 00 00 79` | strh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beb158"></a> `00beb158` | `29 00 00 79` | strh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beb15c"></a> `00beb15c` | `48 00 40 79` | ldrh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beb160"></a> `00beb160` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beb164"></a> `00beb164` | `c2 00 00 54` | b.cs 0x00beb17c | `CONDITIONAL_JUMP`
<a id="insn-00beb168"></a> `00beb168` | `28 00 00 79` | strh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beb16c"></a> `00beb16c` | `e8 03 09 2a` | mov w8,w9 | `FALL_THROUGH`
<a id="insn-00beb170"></a> `00beb170` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00beb174"></a> `00beb174` | `02 00 00 14` | b 0x00beb17c | `UNCONDITIONAL_JUMP`
<a id="insn-00beb178"></a> `00beb178` | `e8 03 0a 2a` | mov w8,w10 | `FALL_THROUGH`
<a id="insn-00beb17c"></a> `00beb17c` | `69 00 40 79` | ldrh w9,[x3] | `FALL_THROUGH`
<a id="insn-00beb180"></a> `00beb180` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00beb184"></a> `00beb184` | `e2 01 00 54` | b.cs 0x00beb1c0 | `CONDITIONAL_JUMP`
<a id="insn-00beb188"></a> `00beb188` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00beb18c"></a> `00beb18c` | `68 00 00 79` | strh w8,[x3] | `FALL_THROUGH`
<a id="insn-00beb190"></a> `00beb190` | `48 00 40 79` | ldrh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beb194"></a> `00beb194` | `29 00 40 79` | ldrh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beb198"></a> `00beb198` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beb19c"></a> `00beb19c` | `22 01 00 54` | b.cs 0x00beb1c0 | `CONDITIONAL_JUMP`
<a id="insn-00beb1a0"></a> `00beb1a0` | `28 00 00 79` | strh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beb1a4"></a> `00beb1a4` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00beb1a8"></a> `00beb1a8` | `28 00 40 79` | ldrh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beb1ac"></a> `00beb1ac` | `09 00 40 79` | ldrh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beb1b0"></a> `00beb1b0` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beb1b4"></a> `00beb1b4` | `62 00 00 54` | b.cs 0x00beb1c0 | `CONDITIONAL_JUMP`
<a id="insn-00beb1b8"></a> `00beb1b8` | `08 00 00 79` | strh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beb1bc"></a> `00beb1bc` | `29 00 00 79` | strh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beb1c0"></a> `00beb1c0` | `88 00 40 79` | ldrh w8,[x4] | `FALL_THROUGH`
<a id="insn-00beb1c4"></a> `00beb1c4` | `69 00 40 79` | ldrh w9,[x3] | `FALL_THROUGH`
<a id="insn-00beb1c8"></a> `00beb1c8` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beb1cc"></a> `00beb1cc` | `a2 02 00 54` | b.cs 0x00beb220 | `CONDITIONAL_JUMP`
<a id="insn-00beb1d0"></a> `00beb1d0` | `68 00 00 79` | strh w8,[x3] | `FALL_THROUGH`
<a id="insn-00beb1d4"></a> `00beb1d4` | `89 00 00 79` | strh w9,[x4] | `FALL_THROUGH`
<a id="insn-00beb1d8"></a> `00beb1d8` | `68 00 40 79` | ldrh w8,[x3] | `FALL_THROUGH`
<a id="insn-00beb1dc"></a> `00beb1dc` | `49 00 40 79` | ldrh w9,[x2] | `FALL_THROUGH`
<a id="insn-00beb1e0"></a> `00beb1e0` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beb1e4"></a> `00beb1e4` | `e2 01 00 54` | b.cs 0x00beb220 | `CONDITIONAL_JUMP`
<a id="insn-00beb1e8"></a> `00beb1e8` | `48 00 00 79` | strh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beb1ec"></a> `00beb1ec` | `69 00 00 79` | strh w9,[x3] | `FALL_THROUGH`
<a id="insn-00beb1f0"></a> `00beb1f0` | `48 00 40 79` | ldrh w8,[x2] | `FALL_THROUGH`
<a id="insn-00beb1f4"></a> `00beb1f4` | `29 00 40 79` | ldrh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beb1f8"></a> `00beb1f8` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beb1fc"></a> `00beb1fc` | `22 01 00 54` | b.cs 0x00beb220 | `CONDITIONAL_JUMP`
<a id="insn-00beb200"></a> `00beb200` | `28 00 00 79` | strh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beb204"></a> `00beb204` | `49 00 00 79` | strh w9,[x2] | `FALL_THROUGH`
<a id="insn-00beb208"></a> `00beb208` | `28 00 40 79` | ldrh w8,[x1] | `FALL_THROUGH`
<a id="insn-00beb20c"></a> `00beb20c` | `09 00 40 79` | ldrh w9,[x0] | `FALL_THROUGH`
<a id="insn-00beb210"></a> `00beb210` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00beb214"></a> `00beb214` | `62 00 00 54` | b.cs 0x00beb220 | `CONDITIONAL_JUMP`
<a id="insn-00beb218"></a> `00beb218` | `08 00 00 79` | strh w8,[x0] | `FALL_THROUGH`
<a id="insn-00beb21c"></a> `00beb21c` | `29 00 00 79` | strh w9,[x1] | `FALL_THROUGH`
<a id="insn-00beb220"></a> `00beb220` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00beb0fc`](#insn-00beb0fc) 範囲 `[['00beb0fc', '00beb113']]`
  - `CONDITIONAL_JUMP` [`00beb110`](#insn-00beb110) → [`00beb124`](#insn-00beb124)
  - `FALL_THROUGH` [`00beb110`](#insn-00beb110) → [`00beb114`](#insn-00beb114)
- ブロック [`00beb114`](#insn-00beb114) 範囲 `[['00beb114', '00beb11b']]`
  - `CONDITIONAL_JUMP` [`00beb118`](#insn-00beb118) → [`00beb154`](#insn-00beb154)
  - `FALL_THROUGH` [`00beb118`](#insn-00beb118) → [`00beb11c`](#insn-00beb11c)
- ブロック [`00beb11c`](#insn-00beb11c) 範囲 `[['00beb11c', '00beb123']]`
  - `UNCONDITIONAL_JUMP` [`00beb120`](#insn-00beb120) → [`00beb16c`](#insn-00beb16c)
- ブロック [`00beb124`](#insn-00beb124) 範囲 `[['00beb124', '00beb12b']]`
  - `CONDITIONAL_JUMP` [`00beb128`](#insn-00beb128) → [`00beb178`](#insn-00beb178)
  - `FALL_THROUGH` [`00beb128`](#insn-00beb128) → [`00beb12c`](#insn-00beb12c)
- ブロック [`00beb12c`](#insn-00beb12c) 範囲 `[['00beb12c', '00beb143']]`
  - `CONDITIONAL_JUMP` [`00beb140`](#insn-00beb140) → [`00beb17c`](#insn-00beb17c)
  - `FALL_THROUGH` [`00beb140`](#insn-00beb140) → [`00beb144`](#insn-00beb144)
- ブロック [`00beb144`](#insn-00beb144) 範囲 `[['00beb144', '00beb153']]`
  - `UNCONDITIONAL_JUMP` [`00beb150`](#insn-00beb150) → [`00beb17c`](#insn-00beb17c)
- ブロック [`00beb154`](#insn-00beb154) 範囲 `[['00beb154', '00beb167']]`
  - `CONDITIONAL_JUMP` [`00beb164`](#insn-00beb164) → [`00beb17c`](#insn-00beb17c)
  - `FALL_THROUGH` [`00beb164`](#insn-00beb164) → [`00beb168`](#insn-00beb168)
- ブロック [`00beb168`](#insn-00beb168) 範囲 `[['00beb168', '00beb16b']]`
  - `FALL_THROUGH` [`00beb168`](#insn-00beb168) → [`00beb16c`](#insn-00beb16c)
- ブロック [`00beb16c`](#insn-00beb16c) 範囲 `[['00beb16c', '00beb177']]`
  - `UNCONDITIONAL_JUMP` [`00beb174`](#insn-00beb174) → [`00beb17c`](#insn-00beb17c)
- ブロック [`00beb178`](#insn-00beb178) 範囲 `[['00beb178', '00beb17b']]`
  - `FALL_THROUGH` [`00beb178`](#insn-00beb178) → [`00beb17c`](#insn-00beb17c)
- ブロック [`00beb17c`](#insn-00beb17c) 範囲 `[['00beb17c', '00beb187']]`
  - `CONDITIONAL_JUMP` [`00beb184`](#insn-00beb184) → [`00beb1c0`](#insn-00beb1c0)
  - `FALL_THROUGH` [`00beb184`](#insn-00beb184) → [`00beb188`](#insn-00beb188)
- ブロック [`00beb188`](#insn-00beb188) 範囲 `[['00beb188', '00beb19f']]`
  - `CONDITIONAL_JUMP` [`00beb19c`](#insn-00beb19c) → [`00beb1c0`](#insn-00beb1c0)
  - `FALL_THROUGH` [`00beb19c`](#insn-00beb19c) → [`00beb1a0`](#insn-00beb1a0)
- ブロック [`00beb1a0`](#insn-00beb1a0) 範囲 `[['00beb1a0', '00beb1b7']]`
  - `CONDITIONAL_JUMP` [`00beb1b4`](#insn-00beb1b4) → [`00beb1c0`](#insn-00beb1c0)
  - `FALL_THROUGH` [`00beb1b4`](#insn-00beb1b4) → [`00beb1b8`](#insn-00beb1b8)
- ブロック [`00beb1b8`](#insn-00beb1b8) 範囲 `[['00beb1b8', '00beb1bf']]`
  - `FALL_THROUGH` [`00beb1bc`](#insn-00beb1bc) → [`00beb1c0`](#insn-00beb1c0)
- ブロック [`00beb1c0`](#insn-00beb1c0) 範囲 `[['00beb1c0', '00beb1cf']]`
  - `CONDITIONAL_JUMP` [`00beb1cc`](#insn-00beb1cc) → [`00beb220`](#insn-00beb220)
  - `FALL_THROUGH` [`00beb1cc`](#insn-00beb1cc) → [`00beb1d0`](#insn-00beb1d0)
- ブロック [`00beb1d0`](#insn-00beb1d0) 範囲 `[['00beb1d0', '00beb1e7']]`
  - `CONDITIONAL_JUMP` [`00beb1e4`](#insn-00beb1e4) → [`00beb220`](#insn-00beb220)
  - `FALL_THROUGH` [`00beb1e4`](#insn-00beb1e4) → [`00beb1e8`](#insn-00beb1e8)
- ブロック [`00beb1e8`](#insn-00beb1e8) 範囲 `[['00beb1e8', '00beb1ff']]`
  - `CONDITIONAL_JUMP` [`00beb1fc`](#insn-00beb1fc) → [`00beb220`](#insn-00beb220)
  - `FALL_THROUGH` [`00beb1fc`](#insn-00beb1fc) → [`00beb200`](#insn-00beb200)
- ブロック [`00beb200`](#insn-00beb200) 範囲 `[['00beb200', '00beb217']]`
  - `CONDITIONAL_JUMP` [`00beb214`](#insn-00beb214) → [`00beb220`](#insn-00beb220)
  - `FALL_THROUGH` [`00beb214`](#insn-00beb214) → [`00beb218`](#insn-00beb218)
- ブロック [`00beb218`](#insn-00beb218) 範囲 `[['00beb218', '00beb21f']]`
  - `FALL_THROUGH` [`00beb21c`](#insn-00beb21c) → [`00beb220`](#insn-00beb220)
- ブロック [`00beb220`](#insn-00beb220) 範囲 `[['00beb220', '00beb223']]`

## 命令位置別の参照

- [`00beb110`](#insn-00beb110) → [`00beb124`](#insn-00beb124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb118`](#insn-00beb118) → [`00beb154`](#insn-00beb154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb120`](#insn-00beb120) → [`00beb16c`](#insn-00beb16c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb128`](#insn-00beb128) → [`00beb178`](#insn-00beb178) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb140`](#insn-00beb140) → [`00beb17c`](#insn-00beb17c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb150`](#insn-00beb150) → [`00beb17c`](#insn-00beb17c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb164`](#insn-00beb164) → [`00beb17c`](#insn-00beb17c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb174`](#insn-00beb174) → [`00beb17c`](#insn-00beb17c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb184`](#insn-00beb184) → [`00beb1c0`](#insn-00beb1c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb19c`](#insn-00beb19c) → [`00beb1c0`](#insn-00beb1c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb1b4`](#insn-00beb1b4) → [`00beb1c0`](#insn-00beb1c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb1cc`](#insn-00beb1cc) → [`00beb220`](#insn-00beb220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb1e4`](#insn-00beb1e4) → [`00beb220`](#insn-00beb220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb1fc`](#insn-00beb1fc) → [`00beb220`](#insn-00beb220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00beb214`](#insn-00beb214) → [`00beb220`](#insn-00beb220) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00beb110`](#insn-00beb110)

~~~json
{
  "source": "00beb110",
  "target": "00beb124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb118`](#insn-00beb118)

~~~json
{
  "source": "00beb118",
  "target": "00beb154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb120`](#insn-00beb120)

~~~json
{
  "source": "00beb120",
  "target": "00beb16c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb128`](#insn-00beb128)

~~~json
{
  "source": "00beb128",
  "target": "00beb178",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb140`](#insn-00beb140)

~~~json
{
  "source": "00beb140",
  "target": "00beb17c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb150`](#insn-00beb150)

~~~json
{
  "source": "00beb150",
  "target": "00beb17c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb164`](#insn-00beb164)

~~~json
{
  "source": "00beb164",
  "target": "00beb17c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb174`](#insn-00beb174)

~~~json
{
  "source": "00beb174",
  "target": "00beb17c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb184`](#insn-00beb184)

~~~json
{
  "source": "00beb184",
  "target": "00beb1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb19c`](#insn-00beb19c)

~~~json
{
  "source": "00beb19c",
  "target": "00beb1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb1b4`](#insn-00beb1b4)

~~~json
{
  "source": "00beb1b4",
  "target": "00beb1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb1cc`](#insn-00beb1cc)

~~~json
{
  "source": "00beb1cc",
  "target": "00beb220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb1e4`](#insn-00beb1e4)

~~~json
{
  "source": "00beb1e4",
  "target": "00beb220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb1fc`](#insn-00beb1fc)

~~~json
{
  "source": "00beb1fc",
  "target": "00beb220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00beb214`](#insn-00beb214)

~~~json
{
  "source": "00beb214",
  "target": "00beb220",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
