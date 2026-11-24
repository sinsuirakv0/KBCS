# 00befb8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bef764`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef764.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-5c934df6712def2892a7ad823941719c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00befc28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befc28.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-18a9c3fdfdf55644b0aeb380da6ea642)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befb8c",
  "name": "_ZNSt16nested_exceptionD0Ev",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5f9b4c3ecb8743b3c446c82624c10459684c79cd235c4c6fe645e9a2f4b704da",
  "source_text_sha256": "5f9b4c3ecb8743b3c446c82624c10459684c79cd235c4c6fe645e9a2f4b704da",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befb8c",
        "00befbb7"
      ]
    ],
    "bytes_sha256": "b0fa9da53699f967216f965223d838d98f11e7f06ded39d949c2f49bdd0b5ac5",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c5df50](../00c5d/00c5df50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 117 bytes

~~~c

void _ZNSt16nested_exceptionD0Ev(void *param_1)

{
  _ZNSt16nested_exceptionD2Ev();
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befb8c"></a> `00befb8c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00befb90"></a> `00befb90` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00befb94"></a> `00befb94` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befb98"></a> `00befb98` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00befb9c"></a> `00befb9c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00befba0"></a> `00befba0` | `ec b8 01 94` | bl 0x00c5df50 | `UNCONDITIONAL_CALL`
<a id="insn-00befba4"></a> `00befba4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00befba8"></a> `00befba8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befbac"></a> `00befbac` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00befbb0"></a> `00befbb0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00befbb4"></a> `00befbb4` | `bf a0 01 14` | b 0x00c57eb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befb8c`](#insn-00befb8c) 範囲 `[['00befb8c', '00befbb7']]`

## 命令位置別の参照

- [`00befb90`](#insn-00befb90) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befb94`](#insn-00befb94) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befba0`](#insn-00befba0) → [`00c5df50`](../00c5d/00c5df50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5df50` · 推定シンボル `None` · 推定型 `None`
- [`00befba8`](#insn-00befba8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbac`](#insn-00befbac) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befbb4`](#insn-00befbb4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befb90`](#insn-00befb90)

~~~json
{
  "source": "00befb90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befb94`](#insn-00befb94)

~~~json
{
  "source": "00befb94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befba0`](#insn-00befba0)

~~~json
{
  "source": "00befba0",
  "target": "00c5df50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befba8`](#insn-00befba8)

~~~json
{
  "source": "00befba8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbac`](#insn-00befbac)

~~~json
{
  "source": "00befbac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befbb4`](#insn-00befbb4)

~~~json
{
  "source": "00befbb4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
