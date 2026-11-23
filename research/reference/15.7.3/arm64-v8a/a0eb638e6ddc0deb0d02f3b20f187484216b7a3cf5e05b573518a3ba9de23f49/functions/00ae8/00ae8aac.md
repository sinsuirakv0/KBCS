# 00ae8aac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ae89e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ae8/00ae89e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0002.md#compare-080b5c01c0d09bd496ab6f9bd9f83c1e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ae8af0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ae8/00ae8af0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0063.md#compare-eba45e896acda623ad03dd9e464f87a6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae8aac",
  "name": "_ZN8firebase4util15character_class11GetMethodIdENS1_6MethodE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dc824f59f2133c781e728e1ec8531d1d2e82007ebb40524591ee1f4553040800",
  "source_text_sha256": "dc824f59f2133c781e728e1ec8531d1d2e82007ebb40524591ee1f4553040800",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae8aac",
        "00ae8ae7"
      ]
    ],
    "bytes_sha256": "a46f19fe3ff16f774efdf61b96109b3d2aff295b9f308ebed6cd437c4c85903e",
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

- [00bde130](../00bde/00bde130.md)

## 関連文字列（未確認候補）

~~~text
"method < kMethodCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 417 bytes

~~~c

undefined8 _ZN8firebase4util15character_class11GetMethodIdENS1_6MethodE(uint param_1)

{
                    /* catch() { ... } // from try @ 00ae63f4 with catch @ 00ae8ab0 */
                    /* catch() { ... } // from try @ 00ae6bbc with catch @ 00ae8ab4 */
  if (1 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("method < kMethodCount");
  }
  return *(undefined8 *)(&DAT_010a0640 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae8aac"></a> `00ae8aac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ae8ab0"></a> `00ae8ab0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae8ab4"></a> `00ae8ab4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00ae8ab8"></a> `00ae8ab8` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00ae8abc"></a> `00ae8abc` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00ae8ac0"></a> `00ae8ac0` | `8b 00 00 54` | b.lt 0x00ae8ad0 | `CONDITIONAL_JUMP`
<a id="insn-00ae8ac4"></a> `00ae8ac4` | `80 bd ff 90` | adrp x0,0x298000 | `FALL_THROUGH`
<a id="insn-00ae8ac8"></a> `00ae8ac8` | `00 50 17 91` | add x0,x0,#0x5d4 | `FALL_THROUGH`
<a id="insn-00ae8acc"></a> `00ae8acc` | `99 d5 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00ae8ad0"></a> `00ae8ad0` | `c8 2d 00 90` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00ae8ad4"></a> `00ae8ad4` | `08 01 19 91` | add x8,x8,#0x640 | `FALL_THROUGH`
<a id="insn-00ae8ad8"></a> `00ae8ad8` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00ae8adc"></a> `00ae8adc` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ae8ae0"></a> `00ae8ae0` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ae8ae4"></a> `00ae8ae4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae8aac`](#insn-00ae8aac) 範囲 `[['00ae8aac', '00ae8aaf']]`
  - `FALL_THROUGH` [`00ae8aac`](#insn-00ae8aac) → [`00ae8ab0`](#insn-00ae8ab0)
- ブロック [`00ae8ab0`](#insn-00ae8ab0) 範囲 `[['00ae8ab0', '00ae8ab3']]`
  - `FALL_THROUGH` [`00ae8ab0`](#insn-00ae8ab0) → [`00ae8ab4`](#insn-00ae8ab4)
- ブロック [`00ae8ab4`](#insn-00ae8ab4) 範囲 `[['00ae8ab4', '00ae8ac3']]`
  - `CONDITIONAL_JUMP` [`00ae8ac0`](#insn-00ae8ac0) → [`00ae8ad0`](#insn-00ae8ad0)
  - `FALL_THROUGH` [`00ae8ac0`](#insn-00ae8ac0) → [`00ae8ac4`](#insn-00ae8ac4)
- ブロック [`00ae8ac4`](#insn-00ae8ac4) 範囲 `[['00ae8ac4', '00ae8acf']]`
  - `FALL_THROUGH` [`00ae8acc`](#insn-00ae8acc) → [`00ae8ad0`](#insn-00ae8ad0)
- ブロック [`00ae8ad0`](#insn-00ae8ad0) 範囲 `[['00ae8ad0', '00ae8ae7']]`

## 命令位置別の参照

- [`00ae8aac`](#insn-00ae8aac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8ab0`](#insn-00ae8ab0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8ac0`](#insn-00ae8ac0) → [`00ae8ad0`](#insn-00ae8ad0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8ac8`](#insn-00ae8ac8) → `002985d4`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00ae8acc`](#insn-00ae8acc) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00ae8ad8`](#insn-00ae8ad8) → `010a0640`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae8adc`](#insn-00ae8adc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae8aac`](#insn-00ae8aac)

~~~json
{
  "source": "00ae8aac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8ab0`](#insn-00ae8ab0)

~~~json
{
  "source": "00ae8ab0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8ac0`](#insn-00ae8ac0)

~~~json
{
  "source": "00ae8ac0",
  "target": "00ae8ad0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8ac8`](#insn-00ae8ac8)

~~~json
{
  "source": "00ae8ac8",
  "target": "002985d4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002985d4",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "6d6574686f64203c206b4d6574686f64436f756e7400",
  "capture_start": "002985d4",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00ae8acc`](#insn-00ae8acc)

~~~json
{
  "source": "00ae8acc",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae8ad8`](#insn-00ae8ad8)

~~~json
{
  "source": "00ae8ad8",
  "target": "010a0640",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae8adc`](#insn-00ae8adc)

~~~json
{
  "source": "00ae8adc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
