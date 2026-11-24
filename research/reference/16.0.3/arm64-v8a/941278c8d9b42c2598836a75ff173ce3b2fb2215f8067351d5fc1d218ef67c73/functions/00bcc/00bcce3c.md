# 00bcce3c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcbe48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcb/00bcbe48.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-141b4402a01dae944c70d5434e01534e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcce3c",
  "name": "FUN_00bcce3c",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dcdcbc5712e9bd4d70955456f8732326787ed9bd573207f373a35c30a728c09b",
  "source_text_sha256": "dcdcbc5712e9bd4d70955456f8732326787ed9bd573207f373a35c30a728c09b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcce3c",
        "00bcce73"
      ]
    ],
    "bytes_sha256": "27ed9a55a72c474365a398772b5b6ca6ee813a2c7048ab3c227f6c504ae9b976",
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

- [00c5be80](../00c5b/00c5be80.md)
- [00c5ead0](../00c5e/00c5ead0.md)

## 関連文字列（未確認候補）

~~~text
"Auth object 0x%08x should be deleted before the App 0x%08x it depends upon."
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 300 bytes

~~~c

void FUN_00bcce3c(undefined8 *param_1)

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
<a id="insn-00bcce3c"></a> `00bcce3c` | `f3 0f 1e f8` | str x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcce40"></a> `00bcce40` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcce44"></a> `00bcce44` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bcce48"></a> `00bcce48` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcce4c"></a> `00bcce4c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcce50"></a> `00bcce50` | `a0 b6 ff f0` | adrp x0,0x2a3000 | `FALL_THROUGH`
<a id="insn-00bcce54"></a> `00bcce54` | `00 68 33 91` | add x0,x0,#0xcda | `FALL_THROUGH`
<a id="insn-00bcce58"></a> `00bcce58` | `02 01 40 b9` | ldr w2,[x8] | `FALL_THROUGH`
<a id="insn-00bcce5c"></a> `00bcce5c` | `e1 03 13 2a` | mov w1,w19 | `FALL_THROUGH`
<a id="insn-00bcce60"></a> `00bcce60` | `08 3c 02 94` | bl 0x00c5be80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcce64"></a> `00bcce64` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcce68"></a> `00bcce68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcce6c"></a> `00bcce6c` | `f3 07 42 f8` | ldr x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcce70"></a> `00bcce70` | `18 47 02 14` | b 0x00c5ead0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcce3c`](#insn-00bcce3c) 範囲 `[['00bcce3c', '00bcce73']]`

## 命令位置別の参照

- [`00bcce3c`](#insn-00bcce3c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcce40`](#insn-00bcce40) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcce54`](#insn-00bcce54) → `002a3cda`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcce60`](#insn-00bcce60) → [`00c5be80`](../00c5b/00c5be80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be80` · 推定シンボル `None` · 推定型 `None`
- [`00bcce64`](#insn-00bcce64) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcce70`](#insn-00bcce70) → [`00c5ead0`](../00c5e/00c5ead0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ead0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcce3c`](#insn-00bcce3c)

~~~json
{
  "source": "00bcce3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcce40`](#insn-00bcce40)

~~~json
{
  "source": "00bcce40",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcce54`](#insn-00bcce54)

~~~json
{
  "source": "00bcce54",
  "target": "002a3cda",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a3cda",
  "offset": 0,
  "size": 76,
  "datatype": "string",
  "bytes": "41757468206f626a656374203078253038782073686f756c642062652064656c",
  "capture_start": "002a3cda",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcce60`](#insn-00bcce60)

~~~json
{
  "source": "00bcce60",
  "target": "00c5be80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcce64`](#insn-00bcce64)

~~~json
{
  "source": "00bcce64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcce70`](#insn-00bcce70)

~~~json
{
  "source": "00bcce70",
  "target": "00c5ead0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
