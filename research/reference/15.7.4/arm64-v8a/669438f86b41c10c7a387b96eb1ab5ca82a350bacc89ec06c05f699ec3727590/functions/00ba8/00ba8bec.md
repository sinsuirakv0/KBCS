# 00ba8bec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ba8ba8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba8/00ba8ba8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0077.md#compare-cb38e3c0cdd608857135e5425da7efbe)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c25634`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c25/00c25634.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0075.md#compare-32e82e70d638b67ddd823fd3cfa3bb56)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba8bec",
  "name": "_ZNSt6__ndk114collate_bynameIcED1Ev",
  "size": 64,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8fb404fda7b2729c94782a5773f6886e54c9755a72452fc37259e79afc567ef8",
  "source_text_sha256": "8fb404fda7b2729c94782a5773f6886e54c9755a72452fc37259e79afc567ef8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba8bec",
        "00ba8c2b"
      ]
    ],
    "bytes_sha256": "d5f5323b7a1c1ee57311bfb648b3640633636079f2fc98d196c34b546bc20d12",
    "instruction_count": 16,
    "instruction_bytes": 64,
    "body_bytes": 64,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1940](../00be1/00be1940.md)

## 呼び出し先

- [00bdb4b0](../00bdb/00bdb4b0.md)
- [00be1930](../00be1/00be1930.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 335 bytes

~~~c

void _ZNSt6__ndk114collate_bynameIcED1Ev(long *param_1)

{
  *param_1 = (long)(PTR__ZTVNSt6__ndk114collate_bynameIcEE_00c1bf88 + 0x10);
                    /* try { // try from 00ba8c14 to 00ca8c1f has its CatchHandler @ 00ba8df4 */
  freelocale((__locale_t)param_1[2]);
  _ZNSt6__ndk119__shared_weak_countD2Ev(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba8bec"></a> `00ba8bec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00ba8bf0"></a> `00ba8bf0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00ba8bf4"></a> `00ba8bf4` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba8bf8"></a> `00ba8bf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ba8bfc"></a> `00ba8bfc` | `88 03 00 f0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00ba8c00"></a> `00ba8c00` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ba8c04"></a> `00ba8c04` | `08 c5 47 f9` | ldr x8,[x8, #0xf88] | `FALL_THROUGH`
<a id="insn-00ba8c08"></a> `00ba8c08` | `00 08 40 f9` | ldr x0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00ba8c0c"></a> `00ba8c0c` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00ba8c10"></a> `00ba8c10` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00ba8c14"></a> `00ba8c14` | `47 e3 00 94` | bl 0x00be1930 | `UNCONDITIONAL_CALL`
<a id="insn-00ba8c18"></a> `00ba8c18` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba8c1c"></a> `00ba8c1c` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba8c20"></a> `00ba8c20` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00ba8c24"></a> `00ba8c24` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00ba8c28"></a> `00ba8c28` | `22 ca 00 14` | b 0x00bdb4b0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba8bec`](#insn-00ba8bec) 範囲 `[['00ba8bec', '00ba8c13']]`
  - `FALL_THROUGH` [`00ba8c10`](#insn-00ba8c10) → [`00ba8c14`](#insn-00ba8c14)
- ブロック [`00ba8c14`](#insn-00ba8c14) 範囲 `[['00ba8c14', '00ba8c2b']]`

## 命令位置別の参照

- [`00ba8bf0`](#insn-00ba8bf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8bf4`](#insn-00ba8bf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8c04`](#insn-00ba8c04) → `00c1bf88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00ba8c10`](#insn-00ba8c10) → `00c13940`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[64]`
- [`00ba8c14`](#insn-00ba8c14) → [`00be1930`](../00be1/00be1930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1930` · 推定シンボル `None` · 推定型 `None`
- [`00ba8c1c`](#insn-00ba8c1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8c20`](#insn-00ba8c20) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba8c28`](#insn-00ba8c28) → [`00bdb4b0`](../00bdb/00bdb4b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb4b0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba8bf0`](#insn-00ba8bf0)

~~~json
{
  "source": "00ba8bf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8bf4`](#insn-00ba8bf4)

~~~json
{
  "source": "00ba8bf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8c04`](#insn-00ba8c04)

~~~json
{
  "source": "00ba8c04",
  "target": "00c1bf88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ba8c10`](#insn-00ba8c10)

~~~json
{
  "source": "00ba8c10",
  "target": "00c13940",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13930",
  "offset": 16,
  "size": 64,
  "datatype": "undefined1[64]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00ba8c14`](#insn-00ba8c14)

~~~json
{
  "source": "00ba8c14",
  "target": "00be1930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba8c1c`](#insn-00ba8c1c)

~~~json
{
  "source": "00ba8c1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8c20`](#insn-00ba8c20)

~~~json
{
  "source": "00ba8c20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba8c28`](#insn-00ba8c28)

~~~json
{
  "source": "00ba8c28",
  "target": "00bdb4b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
