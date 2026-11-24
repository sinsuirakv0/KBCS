# 00bd0fbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bd0b94`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bd0/00bd0b94.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-fa0b76391513826173912e6c6e0a797c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd1058`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd1/00bd1058.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0011.md#compare-84f775391011025a50c223969c525375)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd0fbc",
  "name": "_ZN8firebase4auth27api_not_available_exception11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a204969b5e00d4544d4797b02427fbc7ace04d6188b6782f7d4532321d6cedf2",
  "source_text_sha256": "a204969b5e00d4544d4797b02427fbc7ace04d6188b6782f7d4532321d6cedf2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd0fbc",
        "00bd0ff7"
      ]
    ],
    "bytes_sha256": "9edcf3842d814cccc9c40d282f9bb24769f163bbed2b898baa19e78736e909ab",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 255 bytes

~~~c

undefined8 _ZN8firebase4auth27api_not_available_exception11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_011268b8 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd0fbc"></a> `00bd0fbc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bd0fc0"></a> `00bd0fc0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0fc4"></a> `00bd0fc4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd0fc8"></a> `00bd0fc8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bd0fcc"></a> `00bd0fcc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bd0fd0"></a> `00bd0fd0` | `8b 00 00 54` | b.lt 0x00bd0fe0 | `CONDITIONAL_JUMP`
<a id="insn-00bd0fd4"></a> `00bd0fd4` | `c0 b6 ff 90` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bd0fd8"></a> `00bd0fd8` | `00 9c 0d 91` | add x0,x0,#0x367 | `FALL_THROUGH`
<a id="insn-00bd0fdc"></a> `00bd0fdc` | `09 28 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0fe0"></a> `00bd0fe0` | `a8 2a 00 d0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bd0fe4"></a> `00bd0fe4` | `08 e1 22 91` | add x8,x8,#0x8b8 | `FALL_THROUGH`
<a id="insn-00bd0fe8"></a> `00bd0fe8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bd0fec"></a> `00bd0fec` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0ff0"></a> `00bd0ff0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bd0ff4"></a> `00bd0ff4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd0fbc`](#insn-00bd0fbc) 範囲 `[['00bd0fbc', '00bd0fd3']]`
  - `CONDITIONAL_JUMP` [`00bd0fd0`](#insn-00bd0fd0) → [`00bd0fe0`](#insn-00bd0fe0)
  - `FALL_THROUGH` [`00bd0fd0`](#insn-00bd0fd0) → [`00bd0fd4`](#insn-00bd0fd4)
- ブロック [`00bd0fd4`](#insn-00bd0fd4) 範囲 `[['00bd0fd4', '00bd0fdf']]`
  - `FALL_THROUGH` [`00bd0fdc`](#insn-00bd0fdc) → [`00bd0fe0`](#insn-00bd0fe0)
- ブロック [`00bd0fe0`](#insn-00bd0fe0) 範囲 `[['00bd0fe0', '00bd0ff7']]`

## 命令位置別の参照

- [`00bd0fbc`](#insn-00bd0fbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0fc0`](#insn-00bd0fc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0fd0`](#insn-00bd0fd0) → [`00bd0fe0`](#insn-00bd0fe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0fd8`](#insn-00bd0fd8) → `002a8367`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bd0fdc`](#insn-00bd0fdc) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bd0fe8`](#insn-00bd0fe8) → `011268b8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0fec`](#insn-00bd0fec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd0fbc`](#insn-00bd0fbc)

~~~json
{
  "source": "00bd0fbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0fc0`](#insn-00bd0fc0)

~~~json
{
  "source": "00bd0fc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0fd0`](#insn-00bd0fd0)

~~~json
{
  "source": "00bd0fd0",
  "target": "00bd0fe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0fd8`](#insn-00bd0fd8)

~~~json
{
  "source": "00bd0fd8",
  "target": "002a8367",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a8367",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002a8367",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bd0fdc`](#insn-00bd0fdc)

~~~json
{
  "source": "00bd0fdc",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0fe8`](#insn-00bd0fe8)

~~~json
{
  "source": "00bd0fe8",
  "target": "011268b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0fec`](#insn-00bd0fec)

~~~json
{
  "source": "00bd0fec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
