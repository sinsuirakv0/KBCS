# 00afcb4c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afbb58`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afb/00afbb58.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0029.md#compare-a68bcbd601eadbc0ceee147d2a29a760)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afcb4c",
  "name": "FUN_00afcb4c",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8e6e6588674b5bed52c990808a6f3c3030ed3e8bc9294b8b123b56958d92eb52",
  "source_text_sha256": "8e6e6588674b5bed52c990808a6f3c3030ed3e8bc9294b8b123b56958d92eb52",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afcb4c",
        "00afcb8b"
      ]
    ],
    "bytes_sha256": "803808fce95f7a1c7c3a8f4680f4fe130fd5d8f279d96fc529648a577a6a8e4b",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007082e8](../00708/007082e8.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 191 bytes

~~~c

undefined4 FUN_00afcb4c(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008524fc();
  return *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x849d0);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afcb4c"></a> `00afcb4c` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00afcb50"></a> `00afcb50` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcb54"></a> `00afcb54` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afcb58"></a> `00afcb58` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afcb5c"></a> `00afcb5c` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afcb60"></a> `00afcb60` | `67 56 f5 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00afcb64"></a> `00afcb64` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afcb68"></a> `00afcb68` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afcb6c"></a> `00afcb6c` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afcb70"></a> `00afcb70` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afcb74"></a> `00afcb74` | `09 3a 89 52` | mov w9,#0x49d0 | `FALL_THROUGH`
<a id="insn-00afcb78"></a> `00afcb78` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afcb7c"></a> `00afcb7c` | `00 69 69 b8` | ldr w0,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afcb80"></a> `00afcb80` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afcb84"></a> `00afcb84` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afcb88"></a> `00afcb88` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afcb4c`](#insn-00afcb4c) 範囲 `[['00afcb4c', '00afcb8b']]`

## 命令位置別の参照

- [`00afcb4c`](#insn-00afcb4c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcb50`](#insn-00afcb50) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcb60`](#insn-00afcb60) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00afcb80`](#insn-00afcb80) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afcb84`](#insn-00afcb84) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afcb4c`](#insn-00afcb4c)

~~~json
{
  "source": "00afcb4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcb50`](#insn-00afcb50)

~~~json
{
  "source": "00afcb50",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcb60`](#insn-00afcb60)

~~~json
{
  "source": "00afcb60",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afcb80`](#insn-00afcb80)

~~~json
{
  "source": "00afcb80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afcb84`](#insn-00afcb84)

~~~json
{
  "source": "00afcb84",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
