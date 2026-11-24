# 00bddaec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdda50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdda50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-758c1b970145903a7ff4451fcbc66c51)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdeae0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdeae0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-4f7d2190852b5db850f572e82b1bb594)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddaec",
  "name": "_ZN8firebase4auth8metadata11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e122451b092633373b17d282fe6c6e42f5b1f97bcda9fdca23923bd98d9c048c",
  "source_text_sha256": "e122451b092633373b17d282fe6c6e42f5b1f97bcda9fdca23923bd98d9c048c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddaec",
        "00bddb27"
      ]
    ],
    "bytes_sha256": "4edcfa8b5cfbbfbee0766b766097efbf80d001dbba260d48550d1408d1913bb3",
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

- [00c5b0d0](../00c5b/00c5b0d0.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 208 bytes

~~~c

undefined8 _ZN8firebase4auth8metadata11GetMethodIdENS1_6MethodE(uint param_1)

{
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return (&DAT_01126f10)[param_1];
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddaec"></a> `00bddaec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bddaf0"></a> `00bddaf0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddaf4"></a> `00bddaf4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bddaf8"></a> `00bddaf8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bddafc"></a> `00bddafc` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bddb00"></a> `00bddb00` | `8b 00 00 54` | b.lt 0x00bddb10 | `CONDITIONAL_JUMP`
<a id="insn-00bddb04"></a> `00bddb04` | `40 b6 ff f0` | adrp x0,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bddb08"></a> `00bddb08` | `00 2c 0c 91` | add x0,x0,#0x30b | `FALL_THROUGH`
<a id="insn-00bddb0c"></a> `00bddb0c` | `71 f5 01 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddb10"></a> `00bddb10` | `48 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddb14"></a> `00bddb14` | `08 41 3c 91` | add x8,x8,#0xf10 | `FALL_THROUGH`
<a id="insn-00bddb18"></a> `00bddb18` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bddb1c"></a> `00bddb1c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddb20"></a> `00bddb20` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bddb24"></a> `00bddb24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddaec`](#insn-00bddaec) 範囲 `[['00bddaec', '00bddb03']]`
  - `CONDITIONAL_JUMP` [`00bddb00`](#insn-00bddb00) → [`00bddb10`](#insn-00bddb10)
  - `FALL_THROUGH` [`00bddb00`](#insn-00bddb00) → [`00bddb04`](#insn-00bddb04)
- ブロック [`00bddb04`](#insn-00bddb04) 範囲 `[['00bddb04', '00bddb0f']]`
  - `FALL_THROUGH` [`00bddb0c`](#insn-00bddb0c) → [`00bddb10`](#insn-00bddb10)
- ブロック [`00bddb10`](#insn-00bddb10) 範囲 `[['00bddb10', '00bddb27']]`

## 命令位置別の参照

- [`00bddaec`](#insn-00bddaec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddaf0`](#insn-00bddaf0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddb00`](#insn-00bddb00) → [`00bddb10`](#insn-00bddb10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddb08`](#insn-00bddb08) → `002a830b`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddb0c`](#insn-00bddb0c) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bddb18`](#insn-00bddb18) → `01126f10`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddb1c`](#insn-00bddb1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddaec`](#insn-00bddaec)

~~~json
{
  "source": "00bddaec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddaf0`](#insn-00bddaf0)

~~~json
{
  "source": "00bddaf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddb00`](#insn-00bddb00)

~~~json
{
  "source": "00bddb00",
  "target": "00bddb10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddb08`](#insn-00bddb08)

~~~json
{
  "source": "00bddb08",
  "target": "002a830b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a830b",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002a830b",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bddb0c`](#insn-00bddb0c)

~~~json
{
  "source": "00bddb0c",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddb18`](#insn-00bddb18)

~~~json
{
  "source": "00bddb18",
  "target": "01126f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddb1c`](#insn-00bddb1c)

~~~json
{
  "source": "00bddb1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
