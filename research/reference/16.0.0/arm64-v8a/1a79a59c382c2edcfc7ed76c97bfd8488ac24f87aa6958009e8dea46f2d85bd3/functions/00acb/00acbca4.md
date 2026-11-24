# 00acbca4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a6dd10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a6d/00a6dd10.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/no_difference_in_scope-0008.md#compare-c8c1e11d6004af955081f8c0d412a10d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acbea0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbea0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0005.md#compare-1a1aa87b39f3dd60edd0ef794df1195e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbca4",
  "name": "FUN_00acbca4",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1e7ed64b461765637d5d447747b9918164b0e2c3e6b5093d718309d5387424b8",
  "source_text_sha256": "1e7ed64b461765637d5d447747b9918164b0e2c3e6b5093d718309d5387424b8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbca4",
        "00acbcdf"
      ]
    ],
    "bytes_sha256": "d740f6e81e44900d593a8109a669a4af56062ffa417116484b6ee3dcab302ba3",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00731fec](../00731/00731fec.md)
- [00935974](../00935/00935974.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 454 bytes

~~~c

int FUN_00acbca4(long param_1)

{
  long lVar1;
  int iVar2;
  long lVar3;
  
  if (*(long *)(param_1 + 0x30) == 0) {
    iVar2 = 0;
  }
  else {
    iVar2 = 0;
    lVar1 = *(long *)(param_1 + 0x30);
    lVar3 = param_1;
    do {
      param_1 = lVar1;
      iVar2 = *(int *)(lVar3 + 8) + iVar2;
      lVar1 = *(long *)(param_1 + 0x30);
      lVar3 = param_1;
    } while (*(long *)(param_1 + 0x30) != 0);
  }
  return *(int *)(param_1 + 8) + iVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acbca4"></a> `00acbca4` | `09 18 40 f9` | ldr x9,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00acbca8"></a> `00acbca8` | `49 01 00 b4` | cbz x9,0x00acbcd0 | `CONDITIONAL_JUMP`
<a id="insn-00acbcac"></a> `00acbcac` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acbcb0"></a> `00acbcb0` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00acbcb4"></a> `00acbcb4` | `4a 09 40 b9` | ldr w10,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00acbcb8"></a> `00acbcb8` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00acbcbc"></a> `00acbcbc` | `29 19 40 f9` | ldr x9,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00acbcc0"></a> `00acbcc0` | `48 01 08 0b` | add w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00acbcc4"></a> `00acbcc4` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00acbcc8"></a> `00acbcc8` | `69 ff ff b5` | cbnz x9,0x00acbcb4 | `CONDITIONAL_JUMP`
<a id="insn-00acbccc"></a> `00acbccc` | `02 00 00 14` | b 0x00acbcd4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbcd0"></a> `00acbcd0` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acbcd4"></a> `00acbcd4` | `09 08 40 b9` | ldr w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00acbcd8"></a> `00acbcd8` | `20 01 08 0b` | add w0,w9,w8 | `FALL_THROUGH`
<a id="insn-00acbcdc"></a> `00acbcdc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbca4`](#insn-00acbca4) 範囲 `[['00acbca4', '00acbcab']]`
  - `CONDITIONAL_JUMP` [`00acbca8`](#insn-00acbca8) → [`00acbcd0`](#insn-00acbcd0)
  - `FALL_THROUGH` [`00acbca8`](#insn-00acbca8) → [`00acbcac`](#insn-00acbcac)
- ブロック [`00acbcac`](#insn-00acbcac) 範囲 `[['00acbcac', '00acbcb3']]`
  - `FALL_THROUGH` [`00acbcb0`](#insn-00acbcb0) → [`00acbcb4`](#insn-00acbcb4)
- ブロック [`00acbcb4`](#insn-00acbcb4) 範囲 `[['00acbcb4', '00acbccb']]`
  - `CONDITIONAL_JUMP` [`00acbcc8`](#insn-00acbcc8) → [`00acbcb4`](#insn-00acbcb4)
  - `FALL_THROUGH` [`00acbcc8`](#insn-00acbcc8) → [`00acbccc`](#insn-00acbccc)
- ブロック [`00acbccc`](#insn-00acbccc) 範囲 `[['00acbccc', '00acbccf']]`
  - `UNCONDITIONAL_JUMP` [`00acbccc`](#insn-00acbccc) → [`00acbcd4`](#insn-00acbcd4)
- ブロック [`00acbcd0`](#insn-00acbcd0) 範囲 `[['00acbcd0', '00acbcd3']]`
  - `FALL_THROUGH` [`00acbcd0`](#insn-00acbcd0) → [`00acbcd4`](#insn-00acbcd4)
- ブロック [`00acbcd4`](#insn-00acbcd4) 範囲 `[['00acbcd4', '00acbcdf']]`

## 命令位置別の参照

- [`00acbca8`](#insn-00acbca8) → [`00acbcd0`](#insn-00acbcd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbcc8`](#insn-00acbcc8) → [`00acbcb4`](#insn-00acbcb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbccc`](#insn-00acbccc) → [`00acbcd4`](#insn-00acbcd4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbca8`](#insn-00acbca8)

~~~json
{
  "source": "00acbca8",
  "target": "00acbcd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbcc8`](#insn-00acbcc8)

~~~json
{
  "source": "00acbcc8",
  "target": "00acbcb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbccc`](#insn-00acbccc)

~~~json
{
  "source": "00acbccc",
  "target": "00acbcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
