# 00b6ddac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b6dd10`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b6d/00b6dd10.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0076.md#compare-09c7815b2d5d9921a93520bf5b05f522)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b6eda0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b6e/00b6eda0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0033.md#compare-a0362015e93b43be57b89a90983aea89)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b6ddac",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fb11f312fa2e89dcd03d0ae0e0d5e373b3a90ca3851a59e63053f5e4e9aadbe5",
  "source_text_sha256": "fb11f312fa2e89dcd03d0ae0e0d5e373b3a90ca3851a59e63053f5e4e9aadbe5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b6ddac",
        "00b6ddfb"
      ]
    ],
    "bytes_sha256": "54d8cae23fe0cf9f377ef30f48d66dcb34bd3f8e9090a9520f792d3209f73d3d",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5bb30](../00c5b/00c5bb30.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c5bb30](../00c5b/00c5bb30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 973 bytes

~~~c

void _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE
               (undefined8 param_1,undefined8 *param_2)

{
  if (param_2 != (undefined8 *)0x0) {
    _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE
              (param_1,*param_2);
    _ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE
              (param_1,param_2[1]);
    if ((*(byte *)(param_2 + 4) & 1) != 0) {
      _ZdlPv((void *)param_2[6]);
    }
    _ZdlPv(param_2);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b6ddac"></a> `00b6ddac` | `61 02 00 b4` | cbz x1,0x00b6ddf8 | `CONDITIONAL_JUMP`
<a id="insn-00b6ddb0"></a> `00b6ddb0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00b6ddb4"></a> `00b6ddb4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ddb8"></a> `00b6ddb8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00b6ddbc"></a> `00b6ddbc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b6ddc0"></a> `00b6ddc0` | `21 00 40 f9` | ldr x1,[x1] | `FALL_THROUGH`
<a id="insn-00b6ddc4"></a> `00b6ddc4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b6ddc8"></a> `00b6ddc8` | `5a b7 03 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ddcc"></a> `00b6ddcc` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b6ddd0"></a> `00b6ddd0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b6ddd4"></a> `00b6ddd4` | `57 b7 03 94` | bl 0x00c5bb30 | `UNCONDITIONAL_CALL`
<a id="insn-00b6ddd8"></a> `00b6ddd8` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00b6dddc"></a> `00b6dddc` | `68 00 00 36` | tbz w8,#0x0,0x00b6dde8 | `CONDITIONAL_JUMP`
<a id="insn-00b6dde0"></a> `00b6dde0` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b6dde4"></a> `00b6dde4` | `67 a8 03 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b6dde8"></a> `00b6dde8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b6ddec"></a> `00b6ddec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6ddf0"></a> `00b6ddf0` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00b6ddf4"></a> `00b6ddf4` | `63 a8 03 14` | b 0x00c57f80 | `CALL_TERMINATOR`
<a id="insn-00b6ddf8"></a> `00b6ddf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b6ddac`](#insn-00b6ddac) 範囲 `[['00b6ddac', '00b6ddaf']]`
  - `CONDITIONAL_JUMP` [`00b6ddac`](#insn-00b6ddac) → [`00b6ddf8`](#insn-00b6ddf8)
  - `FALL_THROUGH` [`00b6ddac`](#insn-00b6ddac) → [`00b6ddb0`](#insn-00b6ddb0)
- ブロック [`00b6ddb0`](#insn-00b6ddb0) 範囲 `[['00b6ddb0', '00b6dddf']]`
  - `CONDITIONAL_JUMP` [`00b6dddc`](#insn-00b6dddc) → [`00b6dde8`](#insn-00b6dde8)
  - `FALL_THROUGH` [`00b6dddc`](#insn-00b6dddc) → [`00b6dde0`](#insn-00b6dde0)
- ブロック [`00b6dde0`](#insn-00b6dde0) 範囲 `[['00b6dde0', '00b6dde7']]`
  - `FALL_THROUGH` [`00b6dde4`](#insn-00b6dde4) → [`00b6dde8`](#insn-00b6dde8)
- ブロック [`00b6dde8`](#insn-00b6dde8) 範囲 `[['00b6dde8', '00b6ddf7']]`
- ブロック [`00b6ddf8`](#insn-00b6ddf8) 範囲 `[['00b6ddf8', '00b6ddfb']]`

## 命令位置別の参照

- [`00b6ddac`](#insn-00b6ddac) → [`00b6ddf8`](#insn-00b6ddf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ddb0`](#insn-00b6ddb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ddb4`](#insn-00b6ddb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ddc8`](#insn-00b6ddc8) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00b6ddd4`](#insn-00b6ddd4) → [`00c5bb30`](../00c5b/00c5bb30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bb30` · 推定シンボル `None` · 推定型 `None`
- [`00b6dddc`](#insn-00b6dddc) → [`00b6dde8`](#insn-00b6dde8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6dde4`](#insn-00b6dde4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b6dde8`](#insn-00b6dde8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b6ddf4`](#insn-00b6ddf4) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b6ddac`](#insn-00b6ddac)

~~~json
{
  "source": "00b6ddac",
  "target": "00b6ddf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ddb0`](#insn-00b6ddb0)

~~~json
{
  "source": "00b6ddb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ddb4`](#insn-00b6ddb4)

~~~json
{
  "source": "00b6ddb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ddc8`](#insn-00b6ddc8)

~~~json
{
  "source": "00b6ddc8",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6ddd4`](#insn-00b6ddd4)

~~~json
{
  "source": "00b6ddd4",
  "target": "00c5bb30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6dddc`](#insn-00b6dddc)

~~~json
{
  "source": "00b6dddc",
  "target": "00b6dde8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6dde4`](#insn-00b6dde4)

~~~json
{
  "source": "00b6dde4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6dde8`](#insn-00b6dde8)

~~~json
{
  "source": "00b6dde8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b6ddf4`](#insn-00b6ddf4)

~~~json
{
  "source": "00b6ddf4",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
