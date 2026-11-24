# 00a3edac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a3ed58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ed58.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0033.md#compare-857e42a00fe8bb91c4e8c287a5cb9f3f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00a3fda0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3fda0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0027.md#compare-ae0ffbe9ae5f1c7254f362e8ab29bde4)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3edac",
  "name": "FUN_00a3edac",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "70b53bac0092c9ecd8ac4b345da496910cc3256026ff3e7019feceb66c0fe935",
  "source_text_sha256": "70b53bac0092c9ecd8ac4b345da496910cc3256026ff3e7019feceb66c0fe935",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3edac",
        "00a3eddb"
      ]
    ],
    "bytes_sha256": "3efdc1635d29dc1a15d9e77c17229d533b3906bb5b5140b4be3a1cadc0fbcff6",
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

## 疑似コード / UTF-8 174 bytes

~~~c

void FUN_00a3edac(long param_1)

{
  FUN_005c17dc(param_1 + 0x20,*(undefined8 *)(param_1 + 0x28));
  FUN_005c17dc(param_1 + 8,*(undefined8 *)(param_1 + 0x10));
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3edac"></a> `00a3edac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a3edb0"></a> `00a3edb0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3edb4"></a> `00a3edb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3edb8"></a> `00a3edb8` | `01 14 40 f9` | ldr x1,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00a3edbc"></a> `00a3edbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a3edc0"></a> `00a3edc0` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00a3edc4"></a> `00a3edc4` | `86 0a ee 97` | bl 0x005c17dc | `UNCONDITIONAL_CALL`
<a id="insn-00a3edc8"></a> `00a3edc8` | `61 0a 40 f9` | ldr x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a3edcc"></a> `00a3edcc` | `60 22 00 91` | add x0,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00a3edd0"></a> `00a3edd0` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3edd4"></a> `00a3edd4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a3edd8"></a> `00a3edd8` | `81 0a ee 17` | b 0x005c17dc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3edac`](#insn-00a3edac) 範囲 `[['00a3edac', '00a3eddb']]`

## 命令位置別の参照

- [`00a3edac`](#insn-00a3edac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3edb0`](#insn-00a3edb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3edc4`](#insn-00a3edc4) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`
- [`00a3edd0`](#insn-00a3edd0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3edd4`](#insn-00a3edd4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3edd8`](#insn-00a3edd8) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3edac`](#insn-00a3edac)

~~~json
{
  "source": "00a3edac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3edb0`](#insn-00a3edb0)

~~~json
{
  "source": "00a3edb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3edc4`](#insn-00a3edc4)

~~~json
{
  "source": "00a3edc4",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3edd0`](#insn-00a3edd0)

~~~json
{
  "source": "00a3edd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3edd4`](#insn-00a3edd4)

~~~json
{
  "source": "00a3edd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3edd8`](#insn-00a3edd8)

~~~json
{
  "source": "00a3edd8",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
