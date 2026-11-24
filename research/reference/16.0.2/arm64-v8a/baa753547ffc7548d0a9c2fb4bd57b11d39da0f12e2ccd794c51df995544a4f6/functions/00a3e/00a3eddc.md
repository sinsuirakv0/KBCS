# 00a3eddc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a3ed88`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3ed88.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0061.md#compare-100f728ce77fd40c2b303539e53d7dcd)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00a3fdd0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3fdd0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0062.md#compare-8d4233a5561a872d78c6ca006dd49afd)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3eddc",
  "name": "FUN_00a3eddc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "177b9095678c4e1f1d887c33d46ad3bc013c7c2bff626579125703f5614ec235",
  "source_text_sha256": "177b9095678c4e1f1d887c33d46ad3bc013c7c2bff626579125703f5614ec235",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3eddc",
        "00a3ee13"
      ]
    ],
    "bytes_sha256": "51940c310d70e0dd258bb3845d21d5601eafce76ff7cc7184eb2fed7de5f9d20",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
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

## 疑似コード / UTF-8 168 bytes

~~~c

void FUN_00a3eddc(undefined8 *param_1)

{
  *param_1 = &PTR_FUN_00c8b578;
  FUN_005c17dc(param_1 + 5,param_1[6]);
  FUN_005c17dc(param_1 + 2,param_1[3]);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3eddc"></a> `00a3eddc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a3ede0"></a> `00a3ede0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3ede4"></a> `00a3ede4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3ede8"></a> `00a3ede8` | `01 18 40 f9` | ldr x1,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00a3edec"></a> `00a3edec` | `68 12 00 b0` | adrp x8,0xc8b000 | `FALL_THROUGH`
<a id="insn-00a3edf0"></a> `00a3edf0` | `08 e1 15 91` | add x8,x8,#0x578 | `FALL_THROUGH`
<a id="insn-00a3edf4"></a> `00a3edf4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a3edf8"></a> `00a3edf8` | `08 84 02 f8` | str x8,[x0], #0x28 | `FALL_THROUGH`
<a id="insn-00a3edfc"></a> `00a3edfc` | `78 0a ee 97` | bl 0x005c17dc | `UNCONDITIONAL_CALL`
<a id="insn-00a3ee00"></a> `00a3ee00` | `61 0e 40 f9` | ldr x1,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a3ee04"></a> `00a3ee04` | `60 42 00 91` | add x0,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00a3ee08"></a> `00a3ee08` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3ee0c"></a> `00a3ee0c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a3ee10"></a> `00a3ee10` | `73 0a ee 17` | b 0x005c17dc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3eddc`](#insn-00a3eddc) 範囲 `[['00a3eddc', '00a3ee13']]`

## 命令位置別の参照

- [`00a3eddc`](#insn-00a3eddc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ede0`](#insn-00a3ede0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3edf8`](#insn-00a3edf8) → `00c8b578`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00a3edfc`](#insn-00a3edfc) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`
- [`00a3ee08`](#insn-00a3ee08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ee0c`](#insn-00a3ee0c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3ee10`](#insn-00a3ee10) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3eddc`](#insn-00a3eddc)

~~~json
{
  "source": "00a3eddc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ede0`](#insn-00a3ede0)

~~~json
{
  "source": "00a3ede0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3edf8`](#insn-00a3edf8)

~~~json
{
  "source": "00a3edf8",
  "target": "00c8b578",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c8b578",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00a3edfc`](#insn-00a3edfc)

~~~json
{
  "source": "00a3edfc",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3ee08`](#insn-00a3ee08)

~~~json
{
  "source": "00a3ee08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ee0c`](#insn-00a3ee0c)

~~~json
{
  "source": "00a3ee0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3ee10`](#insn-00a3ee10)

~~~json
{
  "source": "00a3ee10",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
