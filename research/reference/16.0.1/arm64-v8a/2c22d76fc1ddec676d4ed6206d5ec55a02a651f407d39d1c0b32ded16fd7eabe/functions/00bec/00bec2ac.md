# 00bec2ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 要確認
  - [v16.0.0 → v16.0.1 候補と検査根拠](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/review-0005.md#review-46668671ef1e8969e8525f64129cdd03)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 要確認
  - [v16.0.1 → v16.0.2 候補と検査根拠](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/review-0003.md#review-46668671ef1e8969e8525f64129cdd03)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bec2ac",
  "name": "FUN_00bec2ac",
  "size": 296,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fea8122f93300977feac1bedfec3737a0d6e4805c5f5d302478f2b193e9f4ee3",
  "source_text_sha256": "fea8122f93300977feac1bedfec3737a0d6e4805c5f5d302478f2b193e9f4ee3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bec2ac",
        "00bec3d3"
      ]
    ],
    "bytes_sha256": "54ceae893e1f992d6b8a29e0deb252a10562ceafadb0e91e8fa56f29a378983e",
    "instruction_count": 74,
    "instruction_bytes": 296,
    "body_bytes": 296,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be54b0](../00be5/00be54b0.md)
- [00bec00c](../00bec/00bec00c.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1481 bytes

~~~c

void FUN_00bec2ac(uint *param_1,uint *param_2,uint *param_3,uint *param_4,uint *param_5)

{
  uint uVar1;
  uint uVar2;
  uint uVar3;
  
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
      if (uVar2 <= uVar3) goto LAB_00bec32c;
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
LAB_00bec32c:
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
<a id="insn-00bec2ac"></a> `00bec2ac` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bec2b0"></a> `00bec2b0` | `28 00 40 b9` | ldr w8,[x1] | `FALL_THROUGH`
<a id="insn-00bec2b4"></a> `00bec2b4` | `09 00 40 b9` | ldr w9,[x0] | `FALL_THROUGH`
<a id="insn-00bec2b8"></a> `00bec2b8` | `4a 00 40 b9` | ldr w10,[x2] | `FALL_THROUGH`
<a id="insn-00bec2bc"></a> `00bec2bc` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bec2c0"></a> `00bec2c0` | `a2 00 00 54` | b.cs 0x00bec2d4 | `CONDITIONAL_JUMP`
<a id="insn-00bec2c4"></a> `00bec2c4` | `5f 01 08 6b` | cmp w10,w8 | `FALL_THROUGH`
<a id="insn-00bec2c8"></a> `00bec2c8` | `e2 01 00 54` | b.cs 0x00bec304 | `CONDITIONAL_JUMP`
<a id="insn-00bec2cc"></a> `00bec2cc` | `0a 00 00 b9` | str w10,[x0] | `FALL_THROUGH`
<a id="insn-00bec2d0"></a> `00bec2d0` | `13 00 00 14` | b 0x00bec31c | `UNCONDITIONAL_JUMP`
<a id="insn-00bec2d4"></a> `00bec2d4` | `5f 01 08 6b` | cmp w10,w8 | `FALL_THROUGH`
<a id="insn-00bec2d8"></a> `00bec2d8` | `82 02 00 54` | b.cs 0x00bec328 | `CONDITIONAL_JUMP`
<a id="insn-00bec2dc"></a> `00bec2dc` | `2a 00 00 b9` | str w10,[x1] | `FALL_THROUGH`
<a id="insn-00bec2e0"></a> `00bec2e0` | `48 00 00 b9` | str w8,[x2] | `FALL_THROUGH`
<a id="insn-00bec2e4"></a> `00bec2e4` | `29 00 40 b9` | ldr w9,[x1] | `FALL_THROUGH`
<a id="insn-00bec2e8"></a> `00bec2e8` | `0a 00 40 b9` | ldr w10,[x0] | `FALL_THROUGH`
<a id="insn-00bec2ec"></a> `00bec2ec` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00bec2f0"></a> `00bec2f0` | `e2 01 00 54` | b.cs 0x00bec32c | `CONDITIONAL_JUMP`
<a id="insn-00bec2f4"></a> `00bec2f4` | `09 00 00 b9` | str w9,[x0] | `FALL_THROUGH`
<a id="insn-00bec2f8"></a> `00bec2f8` | `2a 00 00 b9` | str w10,[x1] | `FALL_THROUGH`
<a id="insn-00bec2fc"></a> `00bec2fc` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00bec300"></a> `00bec300` | `0b 00 00 14` | b 0x00bec32c | `UNCONDITIONAL_JUMP`
<a id="insn-00bec304"></a> `00bec304` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00bec308"></a> `00bec308` | `29 00 00 b9` | str w9,[x1] | `FALL_THROUGH`
<a id="insn-00bec30c"></a> `00bec30c` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00bec310"></a> `00bec310` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bec314"></a> `00bec314` | `c2 00 00 54` | b.cs 0x00bec32c | `CONDITIONAL_JUMP`
<a id="insn-00bec318"></a> `00bec318` | `28 00 00 b9` | str w8,[x1] | `FALL_THROUGH`
<a id="insn-00bec31c"></a> `00bec31c` | `e8 03 09 2a` | mov w8,w9 | `FALL_THROUGH`
<a id="insn-00bec320"></a> `00bec320` | `49 00 00 b9` | str w9,[x2] | `FALL_THROUGH`
<a id="insn-00bec324"></a> `00bec324` | `02 00 00 14` | b 0x00bec32c | `UNCONDITIONAL_JUMP`
<a id="insn-00bec328"></a> `00bec328` | `e8 03 0a 2a` | mov w8,w10 | `FALL_THROUGH`
<a id="insn-00bec32c"></a> `00bec32c` | `69 00 40 b9` | ldr w9,[x3] | `FALL_THROUGH`
<a id="insn-00bec330"></a> `00bec330` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00bec334"></a> `00bec334` | `e2 01 00 54` | b.cs 0x00bec370 | `CONDITIONAL_JUMP`
<a id="insn-00bec338"></a> `00bec338` | `49 00 00 b9` | str w9,[x2] | `FALL_THROUGH`
<a id="insn-00bec33c"></a> `00bec33c` | `68 00 00 b9` | str w8,[x3] | `FALL_THROUGH`
<a id="insn-00bec340"></a> `00bec340` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00bec344"></a> `00bec344` | `29 00 40 b9` | ldr w9,[x1] | `FALL_THROUGH`
<a id="insn-00bec348"></a> `00bec348` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bec34c"></a> `00bec34c` | `22 01 00 54` | b.cs 0x00bec370 | `CONDITIONAL_JUMP`
<a id="insn-00bec350"></a> `00bec350` | `28 00 00 b9` | str w8,[x1] | `FALL_THROUGH`
<a id="insn-00bec354"></a> `00bec354` | `49 00 00 b9` | str w9,[x2] | `FALL_THROUGH`
<a id="insn-00bec358"></a> `00bec358` | `28 00 40 b9` | ldr w8,[x1] | `FALL_THROUGH`
<a id="insn-00bec35c"></a> `00bec35c` | `09 00 40 b9` | ldr w9,[x0] | `FALL_THROUGH`
<a id="insn-00bec360"></a> `00bec360` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bec364"></a> `00bec364` | `62 00 00 54` | b.cs 0x00bec370 | `CONDITIONAL_JUMP`
<a id="insn-00bec368"></a> `00bec368` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00bec36c"></a> `00bec36c` | `29 00 00 b9` | str w9,[x1] | `FALL_THROUGH`
<a id="insn-00bec370"></a> `00bec370` | `88 00 40 b9` | ldr w8,[x4] | `FALL_THROUGH`
<a id="insn-00bec374"></a> `00bec374` | `69 00 40 b9` | ldr w9,[x3] | `FALL_THROUGH`
<a id="insn-00bec378"></a> `00bec378` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bec37c"></a> `00bec37c` | `a2 02 00 54` | b.cs 0x00bec3d0 | `CONDITIONAL_JUMP`
<a id="insn-00bec380"></a> `00bec380` | `68 00 00 b9` | str w8,[x3] | `FALL_THROUGH`
<a id="insn-00bec384"></a> `00bec384` | `89 00 00 b9` | str w9,[x4] | `FALL_THROUGH`
<a id="insn-00bec388"></a> `00bec388` | `68 00 40 b9` | ldr w8,[x3] | `FALL_THROUGH`
<a id="insn-00bec38c"></a> `00bec38c` | `49 00 40 b9` | ldr w9,[x2] | `FALL_THROUGH`
<a id="insn-00bec390"></a> `00bec390` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bec394"></a> `00bec394` | `e2 01 00 54` | b.cs 0x00bec3d0 | `CONDITIONAL_JUMP`
<a id="insn-00bec398"></a> `00bec398` | `48 00 00 b9` | str w8,[x2] | `FALL_THROUGH`
<a id="insn-00bec39c"></a> `00bec39c` | `69 00 00 b9` | str w9,[x3] | `FALL_THROUGH`
<a id="insn-00bec3a0"></a> `00bec3a0` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00bec3a4"></a> `00bec3a4` | `29 00 40 b9` | ldr w9,[x1] | `FALL_THROUGH`
<a id="insn-00bec3a8"></a> `00bec3a8` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bec3ac"></a> `00bec3ac` | `22 01 00 54` | b.cs 0x00bec3d0 | `CONDITIONAL_JUMP`
<a id="insn-00bec3b0"></a> `00bec3b0` | `28 00 00 b9` | str w8,[x1] | `FALL_THROUGH`
<a id="insn-00bec3b4"></a> `00bec3b4` | `49 00 00 b9` | str w9,[x2] | `FALL_THROUGH`
<a id="insn-00bec3b8"></a> `00bec3b8` | `28 00 40 b9` | ldr w8,[x1] | `FALL_THROUGH`
<a id="insn-00bec3bc"></a> `00bec3bc` | `09 00 40 b9` | ldr w9,[x0] | `FALL_THROUGH`
<a id="insn-00bec3c0"></a> `00bec3c0` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00bec3c4"></a> `00bec3c4` | `62 00 00 54` | b.cs 0x00bec3d0 | `CONDITIONAL_JUMP`
<a id="insn-00bec3c8"></a> `00bec3c8` | `08 00 00 b9` | str w8,[x0] | `FALL_THROUGH`
<a id="insn-00bec3cc"></a> `00bec3cc` | `29 00 00 b9` | str w9,[x1] | `FALL_THROUGH`
<a id="insn-00bec3d0"></a> `00bec3d0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bec2ac`](#insn-00bec2ac) 範囲 `[['00bec2ac', '00bec2c3']]`
  - `CONDITIONAL_JUMP` [`00bec2c0`](#insn-00bec2c0) → [`00bec2d4`](#insn-00bec2d4)
  - `FALL_THROUGH` [`00bec2c0`](#insn-00bec2c0) → [`00bec2c4`](#insn-00bec2c4)
- ブロック [`00bec2c4`](#insn-00bec2c4) 範囲 `[['00bec2c4', '00bec2cb']]`
  - `CONDITIONAL_JUMP` [`00bec2c8`](#insn-00bec2c8) → [`00bec304`](#insn-00bec304)
  - `FALL_THROUGH` [`00bec2c8`](#insn-00bec2c8) → [`00bec2cc`](#insn-00bec2cc)
- ブロック [`00bec2cc`](#insn-00bec2cc) 範囲 `[['00bec2cc', '00bec2d3']]`
  - `UNCONDITIONAL_JUMP` [`00bec2d0`](#insn-00bec2d0) → [`00bec31c`](#insn-00bec31c)
- ブロック [`00bec2d4`](#insn-00bec2d4) 範囲 `[['00bec2d4', '00bec2db']]`
  - `CONDITIONAL_JUMP` [`00bec2d8`](#insn-00bec2d8) → [`00bec328`](#insn-00bec328)
  - `FALL_THROUGH` [`00bec2d8`](#insn-00bec2d8) → [`00bec2dc`](#insn-00bec2dc)
- ブロック [`00bec2dc`](#insn-00bec2dc) 範囲 `[['00bec2dc', '00bec2f3']]`
  - `CONDITIONAL_JUMP` [`00bec2f0`](#insn-00bec2f0) → [`00bec32c`](#insn-00bec32c)
  - `FALL_THROUGH` [`00bec2f0`](#insn-00bec2f0) → [`00bec2f4`](#insn-00bec2f4)
- ブロック [`00bec2f4`](#insn-00bec2f4) 範囲 `[['00bec2f4', '00bec303']]`
  - `UNCONDITIONAL_JUMP` [`00bec300`](#insn-00bec300) → [`00bec32c`](#insn-00bec32c)
- ブロック [`00bec304`](#insn-00bec304) 範囲 `[['00bec304', '00bec317']]`
  - `CONDITIONAL_JUMP` [`00bec314`](#insn-00bec314) → [`00bec32c`](#insn-00bec32c)
  - `FALL_THROUGH` [`00bec314`](#insn-00bec314) → [`00bec318`](#insn-00bec318)
- ブロック [`00bec318`](#insn-00bec318) 範囲 `[['00bec318', '00bec31b']]`
  - `FALL_THROUGH` [`00bec318`](#insn-00bec318) → [`00bec31c`](#insn-00bec31c)
- ブロック [`00bec31c`](#insn-00bec31c) 範囲 `[['00bec31c', '00bec327']]`
  - `UNCONDITIONAL_JUMP` [`00bec324`](#insn-00bec324) → [`00bec32c`](#insn-00bec32c)
- ブロック [`00bec328`](#insn-00bec328) 範囲 `[['00bec328', '00bec32b']]`
  - `FALL_THROUGH` [`00bec328`](#insn-00bec328) → [`00bec32c`](#insn-00bec32c)
- ブロック [`00bec32c`](#insn-00bec32c) 範囲 `[['00bec32c', '00bec337']]`
  - `CONDITIONAL_JUMP` [`00bec334`](#insn-00bec334) → [`00bec370`](#insn-00bec370)
  - `FALL_THROUGH` [`00bec334`](#insn-00bec334) → [`00bec338`](#insn-00bec338)
- ブロック [`00bec338`](#insn-00bec338) 範囲 `[['00bec338', '00bec34f']]`
  - `CONDITIONAL_JUMP` [`00bec34c`](#insn-00bec34c) → [`00bec370`](#insn-00bec370)
  - `FALL_THROUGH` [`00bec34c`](#insn-00bec34c) → [`00bec350`](#insn-00bec350)
- ブロック [`00bec350`](#insn-00bec350) 範囲 `[['00bec350', '00bec367']]`
  - `CONDITIONAL_JUMP` [`00bec364`](#insn-00bec364) → [`00bec370`](#insn-00bec370)
  - `FALL_THROUGH` [`00bec364`](#insn-00bec364) → [`00bec368`](#insn-00bec368)
- ブロック [`00bec368`](#insn-00bec368) 範囲 `[['00bec368', '00bec36f']]`
  - `FALL_THROUGH` [`00bec36c`](#insn-00bec36c) → [`00bec370`](#insn-00bec370)
- ブロック [`00bec370`](#insn-00bec370) 範囲 `[['00bec370', '00bec37f']]`
  - `CONDITIONAL_JUMP` [`00bec37c`](#insn-00bec37c) → [`00bec3d0`](#insn-00bec3d0)
  - `FALL_THROUGH` [`00bec37c`](#insn-00bec37c) → [`00bec380`](#insn-00bec380)
- ブロック [`00bec380`](#insn-00bec380) 範囲 `[['00bec380', '00bec397']]`
  - `CONDITIONAL_JUMP` [`00bec394`](#insn-00bec394) → [`00bec3d0`](#insn-00bec3d0)
  - `FALL_THROUGH` [`00bec394`](#insn-00bec394) → [`00bec398`](#insn-00bec398)
- ブロック [`00bec398`](#insn-00bec398) 範囲 `[['00bec398', '00bec3af']]`
  - `CONDITIONAL_JUMP` [`00bec3ac`](#insn-00bec3ac) → [`00bec3d0`](#insn-00bec3d0)
  - `FALL_THROUGH` [`00bec3ac`](#insn-00bec3ac) → [`00bec3b0`](#insn-00bec3b0)
- ブロック [`00bec3b0`](#insn-00bec3b0) 範囲 `[['00bec3b0', '00bec3c7']]`
  - `CONDITIONAL_JUMP` [`00bec3c4`](#insn-00bec3c4) → [`00bec3d0`](#insn-00bec3d0)
  - `FALL_THROUGH` [`00bec3c4`](#insn-00bec3c4) → [`00bec3c8`](#insn-00bec3c8)
- ブロック [`00bec3c8`](#insn-00bec3c8) 範囲 `[['00bec3c8', '00bec3cf']]`
  - `FALL_THROUGH` [`00bec3cc`](#insn-00bec3cc) → [`00bec3d0`](#insn-00bec3d0)
- ブロック [`00bec3d0`](#insn-00bec3d0) 範囲 `[['00bec3d0', '00bec3d3']]`

## 命令位置別の参照

- [`00bec2c0`](#insn-00bec2c0) → [`00bec2d4`](#insn-00bec2d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec2c8`](#insn-00bec2c8) → [`00bec304`](#insn-00bec304) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec2d0`](#insn-00bec2d0) → [`00bec31c`](#insn-00bec31c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec2d8`](#insn-00bec2d8) → [`00bec328`](#insn-00bec328) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec2f0`](#insn-00bec2f0) → [`00bec32c`](#insn-00bec32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec300`](#insn-00bec300) → [`00bec32c`](#insn-00bec32c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec314`](#insn-00bec314) → [`00bec32c`](#insn-00bec32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec324`](#insn-00bec324) → [`00bec32c`](#insn-00bec32c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec334`](#insn-00bec334) → [`00bec370`](#insn-00bec370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec34c`](#insn-00bec34c) → [`00bec370`](#insn-00bec370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec364`](#insn-00bec364) → [`00bec370`](#insn-00bec370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec37c`](#insn-00bec37c) → [`00bec3d0`](#insn-00bec3d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec394`](#insn-00bec394) → [`00bec3d0`](#insn-00bec3d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec3ac`](#insn-00bec3ac) → [`00bec3d0`](#insn-00bec3d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bec3c4`](#insn-00bec3c4) → [`00bec3d0`](#insn-00bec3d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bec2c0`](#insn-00bec2c0)

~~~json
{
  "source": "00bec2c0",
  "target": "00bec2d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec2c8`](#insn-00bec2c8)

~~~json
{
  "source": "00bec2c8",
  "target": "00bec304",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec2d0`](#insn-00bec2d0)

~~~json
{
  "source": "00bec2d0",
  "target": "00bec31c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec2d8`](#insn-00bec2d8)

~~~json
{
  "source": "00bec2d8",
  "target": "00bec328",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec2f0`](#insn-00bec2f0)

~~~json
{
  "source": "00bec2f0",
  "target": "00bec32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec300`](#insn-00bec300)

~~~json
{
  "source": "00bec300",
  "target": "00bec32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec314`](#insn-00bec314)

~~~json
{
  "source": "00bec314",
  "target": "00bec32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec324`](#insn-00bec324)

~~~json
{
  "source": "00bec324",
  "target": "00bec32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec334`](#insn-00bec334)

~~~json
{
  "source": "00bec334",
  "target": "00bec370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec34c`](#insn-00bec34c)

~~~json
{
  "source": "00bec34c",
  "target": "00bec370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec364`](#insn-00bec364)

~~~json
{
  "source": "00bec364",
  "target": "00bec370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec37c`](#insn-00bec37c)

~~~json
{
  "source": "00bec37c",
  "target": "00bec3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec394`](#insn-00bec394)

~~~json
{
  "source": "00bec394",
  "target": "00bec3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec3ac`](#insn-00bec3ac)

~~~json
{
  "source": "00bec3ac",
  "target": "00bec3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bec3c4`](#insn-00bec3c4)

~~~json
{
  "source": "00bec3c4",
  "target": "00bec3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
