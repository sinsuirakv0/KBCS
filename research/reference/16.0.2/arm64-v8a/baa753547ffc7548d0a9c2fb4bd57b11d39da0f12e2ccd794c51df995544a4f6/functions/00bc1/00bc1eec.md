# 00bc1eec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bc1e50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bc1/00bc1e50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0080.md#compare-d27ed271fe1332acf1c25e548886e9ea)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bc2ee0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bc2/00bc2ee0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0080.md#compare-037d1e2f60e06542c6cd50ea81464ebd)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc1eec",
  "name": "_ZN8firebase13remote_config8internal6config10GetFieldIdENS2_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a903860e94b047b7667ea0ee766018de32a8f597ca8512f42d6aef816087b704",
  "source_text_sha256": "a903860e94b047b7667ea0ee766018de32a8f597ca8512f42d6aef816087b704",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc1eec",
        "00bc1f27"
      ]
    ],
    "bytes_sha256": "f5c728f279c65784e81a44b5374bd2dcce548435ae2871f9362f4dd40195afa3",
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
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 248 bytes

~~~c

undefined8 _ZN8firebase13remote_config8internal6config10GetFieldIdENS2_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_01126618 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc1eec"></a> `00bc1eec` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc1ef0"></a> `00bc1ef0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1ef4"></a> `00bc1ef4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc1ef8"></a> `00bc1ef8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00bc1efc"></a> `00bc1efc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bc1f00"></a> `00bc1f00` | `8b 00 00 54` | b.lt 0x00bc1f10 | `CONDITIONAL_JUMP`
<a id="insn-00bc1f04"></a> `00bc1f04` | `40 b7 ff 90` | adrp x0,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bc1f08"></a> `00bc1f08` | `00 34 15 91` | add x0,x0,#0x54d | `FALL_THROUGH`
<a id="insn-00bc1f0c"></a> `00bc1f0c` | `71 64 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc1f10"></a> `00bc1f10` | `28 2b 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bc1f14"></a> `00bc1f14` | `08 61 18 91` | add x8,x8,#0x618 | `FALL_THROUGH`
<a id="insn-00bc1f18"></a> `00bc1f18` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00bc1f1c"></a> `00bc1f1c` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1f20"></a> `00bc1f20` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc1f24"></a> `00bc1f24` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc1eec`](#insn-00bc1eec) 範囲 `[['00bc1eec', '00bc1f03']]`
  - `CONDITIONAL_JUMP` [`00bc1f00`](#insn-00bc1f00) → [`00bc1f10`](#insn-00bc1f10)
  - `FALL_THROUGH` [`00bc1f00`](#insn-00bc1f00) → [`00bc1f04`](#insn-00bc1f04)
- ブロック [`00bc1f04`](#insn-00bc1f04) 範囲 `[['00bc1f04', '00bc1f0f']]`
  - `FALL_THROUGH` [`00bc1f0c`](#insn-00bc1f0c) → [`00bc1f10`](#insn-00bc1f10)
- ブロック [`00bc1f10`](#insn-00bc1f10) 範囲 `[['00bc1f10', '00bc1f27']]`

## 命令位置別の参照

- [`00bc1eec`](#insn-00bc1eec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ef0`](#insn-00bc1ef0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1f00`](#insn-00bc1f00) → [`00bc1f10`](#insn-00bc1f10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1f08`](#insn-00bc1f08) → `002a954d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bc1f0c`](#insn-00bc1f0c) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bc1f18`](#insn-00bc1f18) → `01126618`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1f1c`](#insn-00bc1f1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc1eec`](#insn-00bc1eec)

~~~json
{
  "source": "00bc1eec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ef0`](#insn-00bc1ef0)

~~~json
{
  "source": "00bc1ef0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1f00`](#insn-00bc1f00)

~~~json
{
  "source": "00bc1f00",
  "target": "00bc1f10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1f08`](#insn-00bc1f08)

~~~json
{
  "source": "00bc1f08",
  "target": "002a954d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a954d",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "002a954d",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bc1f0c`](#insn-00bc1f0c)

~~~json
{
  "source": "00bc1f0c",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc1f18`](#insn-00bc1f18)

~~~json
{
  "source": "00bc1f18",
  "target": "01126618",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1f1c`](#insn-00bc1f1c)

~~~json
{
  "source": "00bc1f1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
