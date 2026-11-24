# 00bfbf7c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfaf88`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfaf88.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-45a68be5f8a530b45ab4ba4746ccd23c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbf7c",
  "name": "_ZNSt6__ndk117iostream_categoryEv",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "dce136c0224875bfd9511dc82621a8ceaf038f0778d5671f2820e9a63e98776c",
  "source_text_sha256": "dce136c0224875bfd9511dc82621a8ceaf038f0778d5671f2820e9a63e98776c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbf7c",
        "00bfbfcb"
      ]
    ],
    "bytes_sha256": "b9149de887f52e4612859ab7e6922c59560e7e3ff4fbbdfbccb65cdb28bff1fe",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58ef0](../00c58/00c58ef0.md)
- [00c58f10](../00c58/00c58f10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 243 bytes

~~~c

undefined ** _ZNSt6__ndk117iostream_categoryEv(void)

{
  int iVar1;
  
  if (((DAT_01128450 & 1) == 0) && (iVar1 = __cxa_guard_acquire(&DAT_01128450), iVar1 != 0)) {
    __cxa_guard_release(&DAT_01128450);
  }
  return &PTR_PTR_00ca58a0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbf7c"></a> `00bfbf7c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbf80"></a> `00bfbf80` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfbf84"></a> `00bfbf84` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbf88"></a> `00bfbf88` | `68 29 00 b0` | adrp x8,0x1128000 | `FALL_THROUGH`
<a id="insn-00bfbf8c"></a> `00bfbf8c` | `08 41 11 91` | add x8,x8,#0x450 | `FALL_THROUGH`
<a id="insn-00bfbf90"></a> `00bfbf90` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00bfbf94"></a> `00bfbf94` | `c8 00 00 36` | tbz w8,#0x0,0x00bfbfac | `CONDITIONAL_JUMP`
<a id="insn-00bfbf98"></a> `00bfbf98` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bfbf9c"></a> `00bfbf9c` | `20 c8 54 10` | adr x0,0xca58a0 | `FALL_THROUGH`
<a id="insn-00bfbfa0"></a> `00bfbfa0` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bfbfa4"></a> `00bfbfa4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfbfa8"></a> `00bfbfa8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfbfac"></a> `00bfbfac` | `60 29 00 b0` | adrp x0,0x1128000 | `FALL_THROUGH`
<a id="insn-00bfbfb0"></a> `00bfbfb0` | `00 40 11 91` | add x0,x0,#0x450 | `FALL_THROUGH`
<a id="insn-00bfbfb4"></a> `00bfbfb4` | `cf 73 01 94` | bl 0x00c58ef0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbfb8"></a> `00bfbfb8` | `00 ff ff 34` | cbz w0,0x00bfbf98 | `CONDITIONAL_JUMP`
<a id="insn-00bfbfbc"></a> `00bfbfbc` | `60 29 00 b0` | adrp x0,0x1128000 | `FALL_THROUGH`
<a id="insn-00bfbfc0"></a> `00bfbfc0` | `00 40 11 91` | add x0,x0,#0x450 | `FALL_THROUGH`
<a id="insn-00bfbfc4"></a> `00bfbfc4` | `d3 73 01 94` | bl 0x00c58f10 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbfc8"></a> `00bfbfc8` | `f4 ff ff 17` | b 0x00bfbf98 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfbf7c`](#insn-00bfbf7c) 範囲 `[['00bfbf7c', '00bfbf97']]`
  - `CONDITIONAL_JUMP` [`00bfbf94`](#insn-00bfbf94) → [`00bfbfac`](#insn-00bfbfac)
  - `FALL_THROUGH` [`00bfbf94`](#insn-00bfbf94) → [`00bfbf98`](#insn-00bfbf98)
- ブロック [`00bfbf98`](#insn-00bfbf98) 範囲 `[['00bfbf98', '00bfbfab']]`
- ブロック [`00bfbfac`](#insn-00bfbfac) 範囲 `[['00bfbfac', '00bfbfbb']]`
  - `CONDITIONAL_JUMP` [`00bfbfb8`](#insn-00bfbfb8) → [`00bfbf98`](#insn-00bfbf98)
  - `FALL_THROUGH` [`00bfbfb8`](#insn-00bfbfb8) → [`00bfbfbc`](#insn-00bfbfbc)
- ブロック [`00bfbfbc`](#insn-00bfbfbc) 範囲 `[['00bfbfbc', '00bfbfcb']]`
  - `UNCONDITIONAL_JUMP` [`00bfbfc8`](#insn-00bfbfc8) → [`00bfbf98`](#insn-00bfbf98)

## 命令位置別の参照

- [`00bfbf80`](#insn-00bfbf80) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbf90`](#insn-00bfbf90) → `01128450`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfbf94`](#insn-00bfbf94) → [`00bfbfac`](#insn-00bfbfac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbf9c`](#insn-00bfbf9c) → `00ca58a0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfbfa0`](#insn-00bfbfa0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbfb0`](#insn-00bfbfb0) → `01128450`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfbfb4`](#insn-00bfbfb4) → [`00c58ef0`](../00c58/00c58ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58ef0` · 推定シンボル `None` · 推定型 `None`
- [`00bfbfb8`](#insn-00bfbfb8) → [`00bfbf98`](#insn-00bfbf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbfc0`](#insn-00bfbfc0) → `01128450`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bfbfc4`](#insn-00bfbfc4) → [`00c58f10`](../00c58/00c58f10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f10` · 推定シンボル `None` · 推定型 `None`
- [`00bfbfc8`](#insn-00bfbfc8) → [`00bfbf98`](#insn-00bfbf98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbf80`](#insn-00bfbf80)

~~~json
{
  "source": "00bfbf80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbf90`](#insn-00bfbf90)

~~~json
{
  "source": "00bfbf90",
  "target": "01128450",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128450",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfbf94`](#insn-00bfbf94)

~~~json
{
  "source": "00bfbf94",
  "target": "00bfbfac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbf9c`](#insn-00bfbf9c)

~~~json
{
  "source": "00bfbf9c",
  "target": "00ca58a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca58a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfbfa0`](#insn-00bfbfa0)

~~~json
{
  "source": "00bfbfa0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbfb0`](#insn-00bfbfb0)

~~~json
{
  "source": "00bfbfb0",
  "target": "01128450",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128450",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfbfb4`](#insn-00bfbfb4)

~~~json
{
  "source": "00bfbfb4",
  "target": "00c58ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbfb8`](#insn-00bfbfb8)

~~~json
{
  "source": "00bfbfb8",
  "target": "00bfbf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbfc0`](#insn-00bfbfc0)

~~~json
{
  "source": "00bfbfc0",
  "target": "01128450",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128450",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfbfc4`](#insn-00bfbfc4)

~~~json
{
  "source": "00bfbfc4",
  "target": "00c58f10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfbfc8`](#insn-00bfbfc8)

~~~json
{
  "source": "00bfbfc8",
  "target": "00bfbf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
