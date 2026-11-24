# 00bcbdac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcb984`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcb/00bcb984.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-5923f121c960db3dea897a3304495711)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcbe48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbe48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-2ad1fb899e83589fd4886086248dfe2b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbdac",
  "name": "FUN_00bcbdac",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6333242f5190f9f5b97284a83378a72a71de6e96678dfefc28f1ca4978042440",
  "source_text_sha256": "6333242f5190f9f5b97284a83378a72a71de6e96678dfefc28f1ca4978042440",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbdac",
        "00bcbde3"
      ]
    ],
    "bytes_sha256": "f7be95ade796597208dd474427f9a1258afaf50dbcef089ccb72326111ec3da1",
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

- [00c5ade0](../00c5a/00c5ade0.md)
- [00c5da30](../00c5d/00c5da30.md)

## 関連文字列（未確認候補）

~~~text
"Auth object 0x%08x should be deleted before the App 0x%08x it depends upon."
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 300 bytes

~~~c

void FUN_00bcbdac(undefined8 *param_1)

{
  _ZN8firebase10LogWarningEPKcz
            ("Auth object 0x%08x should be deleted before the App 0x%08x it depends upon.",
             (ulong)param_1 & 0xffffffff,*(undefined4 *)*param_1);
  _ZN8firebase4auth4Auth14DeleteInternalEv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbdac"></a> `00bcbdac` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcbdb0"></a> `00bcbdb0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbdb4"></a> `00bcbdb4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcbdb8"></a> `00bcbdb8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcbdbc"></a> `00bcbdbc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcbdc0"></a> `00bcbdc0` | `c0 b6 ff 90` | adrp x0,0x2a3000 | `FALL_THROUGH`
<a id="insn-00bcbdc4"></a> `00bcbdc4` | `00 70 31 91` | add x0,x0,#0xc5c | `FALL_THROUGH`
<a id="insn-00bcbdc8"></a> `00bcbdc8` | `02 01 40 b9` | ldr w2,[x8] | `FALL_THROUGH`
<a id="insn-00bcbdcc"></a> `00bcbdcc` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00bcbdd0"></a> `00bcbdd0` | `04 3c 02 94` | bl 0x00c5ade0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbdd4"></a> `00bcbdd4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbdd8"></a> `00bcbdd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcbddc"></a> `00bcbddc` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcbde0"></a> `00bcbde0` | `14 47 02 14` | b 0x00c5da30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbdac`](#insn-00bcbdac) 範囲 `[['00bcbdac', '00bcbde3']]`

## 命令位置別の参照

- [`00bcbdac`](#insn-00bcbdac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdb0`](#insn-00bcbdb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdc4`](#insn-00bcbdc4) → `002a3c5c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbdd0`](#insn-00bcbdd0) → [`00c5ade0`](../00c5a/00c5ade0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ade0` · 推定シンボル `None` · 推定型 `None`
- [`00bcbdd4`](#insn-00bcbdd4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbde0`](#insn-00bcbde0) → [`00c5da30`](../00c5d/00c5da30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5da30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbdac`](#insn-00bcbdac)

~~~json
{
  "source": "00bcbdac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdb0`](#insn-00bcbdb0)

~~~json
{
  "source": "00bcbdb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbdc4`](#insn-00bcbdc4)

~~~json
{
  "source": "00bcbdc4",
  "target": "002a3c5c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3c5c",
  "offset": 0,
  "size": 76,
  "datatype": "string",
  "bytes": "41757468206f626a656374203078253038782073686f756c642062652064656c",
  "capture_start": "002a3c5c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcbdd0`](#insn-00bcbdd0)

~~~json
{
  "source": "00bcbdd0",
  "target": "00c5ade0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbdd4`](#insn-00bcbdd4)

~~~json
{
  "source": "00bcbdd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbde0`](#insn-00bcbde0)

~~~json
{
  "source": "00bcbde0",
  "target": "00c5da30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
