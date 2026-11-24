# 00bc9efc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5a9fc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5a/00b5a9fc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0017.md#compare-6e13f6f1e25571bda661fdd0a3cde6b1)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bca324`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bca/00bca324.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-329b749aa1f3fb0b9df348194ccc7424)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc9efc",
  "name": "_ZN8firebase13remote_config32ConfigUpdateListenerRegistration6RemoveEv",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d61a4ea68098e3fc1c2db92f55cf7cb8a42f04c03ba4dab36aa66a2fd1e662d3",
  "source_text_sha256": "d61a4ea68098e3fc1c2db92f55cf7cb8a42f04c03ba4dab36aa66a2fd1e662d3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc9efc",
        "00bc9f2f"
      ]
    ],
    "bytes_sha256": "29fb139e5cc9885e6f9aa2c535a58e095cb96c513328b82c3cf0c14dd8fb9321",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5d270](../00c5d/00c5d270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 419 bytes

~~~c

void _ZN8firebase13remote_config32ConfigUpdateListenerRegistration6RemoveEv(long param_1)

{
                    /* try { // try from 00bc9f14 to 00cca073 has its CatchHandler @ 00bc9d64 */
  if ((*(long *)(param_1 + 0x10) != 0) && (*(long *)(param_1 + 8) != 0)) {
    _ZN8firebase13remote_config8internal40ConfigUpdateListenerRegistrationInternal6RemoveEv();
    *(undefined8 *)(param_1 + 0x10) = 0;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc9efc"></a> `00bc9efc` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bc9f00"></a> `00bc9f00` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9f04"></a> `00bc9f04` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc9f08"></a> `00bc9f08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc9f0c"></a> `00bc9f0c` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9f10"></a> `00bc9f10` | `a0 00 00 b4` | cbz x0,0x00bc9f24 | `CONDITIONAL_JUMP`
<a id="insn-00bc9f14"></a> `00bc9f14` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc9f18"></a> `00bc9f18` | `68 00 00 b4` | cbz x8,0x00bc9f24 | `CONDITIONAL_JUMP`
<a id="insn-00bc9f1c"></a> `00bc9f1c` | `d5 4c 02 94` | bl 0x00c5d270 | `UNCONDITIONAL_CALL`
<a id="insn-00bc9f20"></a> `00bc9f20` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9f24"></a> `00bc9f24` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc9f28"></a> `00bc9f28` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bc9f2c"></a> `00bc9f2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc9efc`](#insn-00bc9efc) 範囲 `[['00bc9efc', '00bc9f13']]`
  - `CONDITIONAL_JUMP` [`00bc9f10`](#insn-00bc9f10) → [`00bc9f24`](#insn-00bc9f24)
  - `FALL_THROUGH` [`00bc9f10`](#insn-00bc9f10) → [`00bc9f14`](#insn-00bc9f14)
- ブロック [`00bc9f14`](#insn-00bc9f14) 範囲 `[['00bc9f14', '00bc9f1b']]`
  - `CONDITIONAL_JUMP` [`00bc9f18`](#insn-00bc9f18) → [`00bc9f24`](#insn-00bc9f24)
  - `FALL_THROUGH` [`00bc9f18`](#insn-00bc9f18) → [`00bc9f1c`](#insn-00bc9f1c)
- ブロック [`00bc9f1c`](#insn-00bc9f1c) 範囲 `[['00bc9f1c', '00bc9f23']]`
  - `FALL_THROUGH` [`00bc9f20`](#insn-00bc9f20) → [`00bc9f24`](#insn-00bc9f24)
- ブロック [`00bc9f24`](#insn-00bc9f24) 範囲 `[['00bc9f24', '00bc9f2f']]`

## 命令位置別の参照

- [`00bc9efc`](#insn-00bc9efc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9f00`](#insn-00bc9f00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9f10`](#insn-00bc9f10) → [`00bc9f24`](#insn-00bc9f24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9f18`](#insn-00bc9f18) → [`00bc9f24`](#insn-00bc9f24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc9f1c`](#insn-00bc9f1c) → [`00c5d270`](../00c5d/00c5d270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d270` · 推定シンボル `None` · 推定型 `None`
- [`00bc9f24`](#insn-00bc9f24) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc9efc`](#insn-00bc9efc)

~~~json
{
  "source": "00bc9efc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9f00`](#insn-00bc9f00)

~~~json
{
  "source": "00bc9f00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9f10`](#insn-00bc9f10)

~~~json
{
  "source": "00bc9f10",
  "target": "00bc9f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9f18`](#insn-00bc9f18)

~~~json
{
  "source": "00bc9f18",
  "target": "00bc9f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc9f1c`](#insn-00bc9f1c)

~~~json
{
  "source": "00bc9f1c",
  "target": "00c5d270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc9f24`](#insn-00bc9f24)

~~~json
{
  "source": "00bc9f24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
