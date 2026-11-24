# 00a3efcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a3ef78`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ef78.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0033.md#compare-b74378806ff738f872e5086fbabc85fc)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00a3ffc0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3ffc0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0027.md#compare-8bb425f0582f122baf392478ae41ffaf)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3efcc",
  "name": "FUN_00a3efcc",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c9d77ba0f99f80804e90d1d88865340cc2e85c68cc8e02c4b383142dbd568e7b",
  "source_text_sha256": "c9d77ba0f99f80804e90d1d88865340cc2e85c68cc8e02c4b383142dbd568e7b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3efcc",
        "00a3effb"
      ]
    ],
    "bytes_sha256": "b1cbcd685f9497b9e80e0db638c72fa12e896a2bbc247dd604487b93ba77aa74",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [005c17dc](../005c1/005c17dc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 177 bytes

~~~c

void FUN_00a3efcc(long param_1)

{
  FUN_005c17dc(param_1 + 0x28,*(undefined8 *)(param_1 + 0x30));
  FUN_005c17dc(param_1 + 0x10,*(undefined8 *)(param_1 + 0x18));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3efcc"></a> `00a3efcc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a3efd0"></a> `00a3efd0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3efd4"></a> `00a3efd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3efd8"></a> `00a3efd8` | `01 18 40 f9` | ldr x1,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00a3efdc"></a> `00a3efdc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a3efe0"></a> `00a3efe0` | `00 a0 00 91` | add x0,x0,#0x28 | `FALL_THROUGH`
<a id="insn-00a3efe4"></a> `00a3efe4` | `fe 09 ee 97` | bl 0x005c17dc | `UNCONDITIONAL_CALL`
<a id="insn-00a3efe8"></a> `00a3efe8` | `61 0e 40 f9` | ldr x1,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a3efec"></a> `00a3efec` | `60 42 00 91` | add x0,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00a3eff0"></a> `00a3eff0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3eff4"></a> `00a3eff4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a3eff8"></a> `00a3eff8` | `f9 09 ee 17` | b 0x005c17dc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3efcc`](#insn-00a3efcc) 範囲 `[['00a3efcc', '00a3effb']]`

## 命令位置別の参照

- [`00a3efcc`](#insn-00a3efcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3efd0`](#insn-00a3efd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3efe4`](#insn-00a3efe4) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`
- [`00a3eff0`](#insn-00a3eff0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3eff4`](#insn-00a3eff4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3eff8`](#insn-00a3eff8) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3efcc`](#insn-00a3efcc)

~~~json
{
  "source": "00a3efcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3efd0`](#insn-00a3efd0)

~~~json
{
  "source": "00a3efd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3efe4`](#insn-00a3efe4)

~~~json
{
  "source": "00a3efe4",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3eff0`](#insn-00a3eff0)

~~~json
{
  "source": "00a3eff0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3eff4`](#insn-00a3eff4)

~~~json
{
  "source": "00a3eff4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3eff8`](#insn-00a3eff8)

~~~json
{
  "source": "00a3eff8",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
