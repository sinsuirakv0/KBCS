# 00aebdc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aebe88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aeb/00aebe88.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-18baf4344d92e4c944cc3a1f4e86aaef)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aebdc0",
  "name": "_ZN8firebase4util8iterator10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "732e47a7f9336cf2c2dc92822ffe6a8210af9911982072b063032d03056de93f",
  "source_text_sha256": "732e47a7f9336cf2c2dc92822ffe6a8210af9911982072b063032d03056de93f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aebdc0",
        "00aebdfb"
      ]
    ],
    "bytes_sha256": "6a22181e3b24610a2f16c97d60cecaa1a74d28984c6491fec5bbfa737d02289b",
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

- [00bde080](../00bde/00bde080.md)

## 関連文字列（未確認候補）

~~~text
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 231 bytes

~~~c

undefined8 _ZN8firebase4util8iterator10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_010a0818 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aebdc0"></a> `00aebdc0` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aebdc4"></a> `00aebdc4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebdc8"></a> `00aebdc8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aebdcc"></a> `00aebdcc` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aebdd0"></a> `00aebdd0` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aebdd4"></a> `00aebdd4` | `8b 00 00 54` | b.lt 0x00aebde4 | `CONDITIONAL_JUMP`
<a id="insn-00aebdd8"></a> `00aebdd8` | `60 bd ff d0` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00aebddc"></a> `00aebddc` | `00 c8 17 91` | add x0,x0,#0x5f2 | `FALL_THROUGH`
<a id="insn-00aebde0"></a> `00aebde0` | `a8 c8 03 94` | bl 0x00bde080 | `UNCONDITIONAL_CALL`
<a id="insn-00aebde4"></a> `00aebde4` | `a8 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aebde8"></a> `00aebde8` | `08 61 20 91` | add x8,x8,#0x818 | `FALL_THROUGH`
<a id="insn-00aebdec"></a> `00aebdec` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aebdf0"></a> `00aebdf0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aebdf4"></a> `00aebdf4` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aebdf8"></a> `00aebdf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aebdc0`](#insn-00aebdc0) 範囲 `[['00aebdc0', '00aebdd7']]`
  - `CONDITIONAL_JUMP` [`00aebdd4`](#insn-00aebdd4) → [`00aebde4`](#insn-00aebde4)
  - `FALL_THROUGH` [`00aebdd4`](#insn-00aebdd4) → [`00aebdd8`](#insn-00aebdd8)
- ブロック [`00aebdd8`](#insn-00aebdd8) 範囲 `[['00aebdd8', '00aebde3']]`
  - `FALL_THROUGH` [`00aebde0`](#insn-00aebde0) → [`00aebde4`](#insn-00aebde4)
- ブロック [`00aebde4`](#insn-00aebde4) 範囲 `[['00aebde4', '00aebdfb']]`

## 命令位置別の参照

- [`00aebdc0`](#insn-00aebdc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdc4`](#insn-00aebdc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdd4`](#insn-00aebdd4) → [`00aebde4`](#insn-00aebde4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebddc`](#insn-00aebddc) → `002995f2`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aebde0`](#insn-00aebde0) → [`00bde080`](../00bde/00bde080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde080` · 推定シンボル `None` · 推定型 `None`
- [`00aebdec`](#insn-00aebdec) → `010a0818`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aebdf0`](#insn-00aebdf0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aebdc0`](#insn-00aebdc0)

~~~json
{
  "source": "00aebdc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdc4`](#insn-00aebdc4)

~~~json
{
  "source": "00aebdc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdd4`](#insn-00aebdd4)

~~~json
{
  "source": "00aebdd4",
  "target": "00aebde4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebddc`](#insn-00aebddc)

~~~json
{
  "source": "00aebddc",
  "target": "002995f2",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002995f2",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "002995f2",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aebde0`](#insn-00aebde0)

~~~json
{
  "source": "00aebde0",
  "target": "00bde080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aebdec`](#insn-00aebdec)

~~~json
{
  "source": "00aebdec",
  "target": "010a0818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aebdf0`](#insn-00aebdf0)

~~~json
{
  "source": "00aebdf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
