# 00aeafe8

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aeaf20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aea/00aeaf20.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0060.md#compare-8c6e9508373ca7c80014bf45945e9cb3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aeb02c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aeb/00aeb02c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0064.md#compare-6e052fb969759d5f309a73047e29c13f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aeafe8",
  "name": "_ZN8firebase4util8hash_map10GetFieldIdENS1_5FieldE",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "08fd95d6ea55828a8f99f4ab7b9e350368fefa2312df11a2cfb0edb9f036afce",
  "source_text_sha256": "08fd95d6ea55828a8f99f4ab7b9e350368fefa2312df11a2cfb0edb9f036afce",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aeafe8",
        "00aeb023"
      ]
    ],
    "bytes_sha256": "5c4bd175319f2a600f9f453d01da4500a64b05bcf8ba7d51c2bb2f2031295dbd",
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
"field < kFieldCount"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 231 bytes

~~~c

undefined8 _ZN8firebase4util8hash_map10GetFieldIdENS1_5FieldE(uint param_1)

{
  if (0 < (int)param_1) {
    _ZN8firebase9LogAssertEPKcz("field < kFieldCount");
  }
  return *(undefined8 *)(&DAT_010a0828 + (ulong)param_1 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aeafe8"></a> `00aeafe8` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aeafec"></a> `00aeafec` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeaff0"></a> `00aeaff0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aeaff4"></a> `00aeaff4` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00aeaff8"></a> `00aeaff8` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aeaffc"></a> `00aeaffc` | `8b 00 00 54` | b.lt 0x00aeb00c | `CONDITIONAL_JUMP`
<a id="insn-00aeb000"></a> `00aeb000` | `60 bd ff d0` | adrp x0,0x299000 | `FALL_THROUGH`
<a id="insn-00aeb004"></a> `00aeb004` | `00 fc 19 91` | add x0,x0,#0x67f | `FALL_THROUGH`
<a id="insn-00aeb008"></a> `00aeb008` | `4a cc 03 94` | bl 0x00bde130 | `UNCONDITIONAL_CALL`
<a id="insn-00aeb00c"></a> `00aeb00c` | `a8 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00aeb010"></a> `00aeb010` | `08 a1 20 91` | add x8,x8,#0x828 | `FALL_THROUGH`
<a id="insn-00aeb014"></a> `00aeb014` | `00 59 73 f8` | ldr x0,[x8, w19, UXTW #0x3] | `FALL_THROUGH`
<a id="insn-00aeb018"></a> `00aeb018` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aeb01c"></a> `00aeb01c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aeb020"></a> `00aeb020` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aeafe8`](#insn-00aeafe8) 範囲 `[['00aeafe8', '00aeafff']]`
  - `CONDITIONAL_JUMP` [`00aeaffc`](#insn-00aeaffc) → [`00aeb00c`](#insn-00aeb00c)
  - `FALL_THROUGH` [`00aeaffc`](#insn-00aeaffc) → [`00aeb000`](#insn-00aeb000)
- ブロック [`00aeb000`](#insn-00aeb000) 範囲 `[['00aeb000', '00aeb00b']]`
  - `FALL_THROUGH` [`00aeb008`](#insn-00aeb008) → [`00aeb00c`](#insn-00aeb00c)
- ブロック [`00aeb00c`](#insn-00aeb00c) 範囲 `[['00aeb00c', '00aeb023']]`

## 命令位置別の参照

- [`00aeafe8`](#insn-00aeafe8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeafec`](#insn-00aeafec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeaffc`](#insn-00aeaffc) → [`00aeb00c`](#insn-00aeb00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb004`](#insn-00aeb004) → `0029967f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aeb008`](#insn-00aeb008) → [`00bde130`](../00bde/00bde130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde130` · 推定シンボル `None` · 推定型 `None`
- [`00aeb014`](#insn-00aeb014) → `010a0828`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aeb018`](#insn-00aeb018) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aeafe8`](#insn-00aeafe8)

~~~json
{
  "source": "00aeafe8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeafec`](#insn-00aeafec)

~~~json
{
  "source": "00aeafec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeaffc`](#insn-00aeaffc)

~~~json
{
  "source": "00aeaffc",
  "target": "00aeb00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb004`](#insn-00aeb004)

~~~json
{
  "source": "00aeb004",
  "target": "0029967f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0029967f",
  "offset": 0,
  "size": 20,
  "datatype": "string",
  "bytes": "6669656c64203c206b4669656c64436f756e7400",
  "capture_start": "0029967f",
  "capture_bytes": 20,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aeb008`](#insn-00aeb008)

~~~json
{
  "source": "00aeb008",
  "target": "00bde130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aeb014`](#insn-00aeb014)

~~~json
{
  "source": "00aeb014",
  "target": "010a0828",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aeb018`](#insn-00aeb018)

~~~json
{
  "source": "00aeb018",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
