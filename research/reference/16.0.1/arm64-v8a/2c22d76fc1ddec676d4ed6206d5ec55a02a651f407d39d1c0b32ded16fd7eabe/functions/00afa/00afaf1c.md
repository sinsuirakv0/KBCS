# 00afaf1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00afaaf4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00afa/00afaaf4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-532cc50039a89d4165405ad259303c48)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00afafb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00afa/00afafb8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0007.md#compare-d6ce66cec41803acd1539873217dc883)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaf1c",
  "name": "FUN_00afaf1c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e0cf2e86e9ec0896181c2ff26cfe211846c9b94ac05135f0377c9cc5d5a4a878",
  "source_text_sha256": "e0cf2e86e9ec0896181c2ff26cfe211846c9b94ac05135f0377c9cc5d5a4a878",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaf1c",
        "00afaf67"
      ]
    ],
    "bytes_sha256": "e70e9dd0587e2124b687f348ff8984ccd267b177be772907183f804dffe9f70e",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f3b4](../00a4f/00a4f3b4.md)
- [00a51fc4](../00a51/00a51fc4.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 209 bytes

~~~c

void FUN_00afaf1c(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514f8();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a98) = param_3 & 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaf1c"></a> `00afaf1c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afaf20"></a> `00afaf20` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaf24"></a> `00afaf24` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaf28"></a> `00afaf28` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afaf2c"></a> `00afaf2c` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afaf30"></a> `00afaf30` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afaf34"></a> `00afaf34` | `55 00 00 12` | and w21,w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afaf38"></a> `00afaf38` | `70 59 f5 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00afaf3c"></a> `00afaf3c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afaf40"></a> `00afaf40` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afaf44"></a> `00afaf44` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afaf48"></a> `00afaf48` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afaf4c"></a> `00afaf4c` | `09 53 89 52` | mov w9,#0x4a98 | `FALL_THROUGH`
<a id="insn-00afaf50"></a> `00afaf50` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afaf54"></a> `00afaf54` | `15 69 29 b8` | str w21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afaf58"></a> `00afaf58` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaf5c"></a> `00afaf5c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaf60"></a> `00afaf60` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afaf64"></a> `00afaf64` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaf1c`](#insn-00afaf1c) 範囲 `[['00afaf1c', '00afaf67']]`

## 命令位置別の参照

- [`00afaf1c`](#insn-00afaf1c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf20`](#insn-00afaf20) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf24`](#insn-00afaf24) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf38`](#insn-00afaf38) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00afaf58`](#insn-00afaf58) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf5c`](#insn-00afaf5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf60`](#insn-00afaf60) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaf1c`](#insn-00afaf1c)

~~~json
{
  "source": "00afaf1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf20`](#insn-00afaf20)

~~~json
{
  "source": "00afaf20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf24`](#insn-00afaf24)

~~~json
{
  "source": "00afaf24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf38`](#insn-00afaf38)

~~~json
{
  "source": "00afaf38",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaf58`](#insn-00afaf58)

~~~json
{
  "source": "00afaf58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf5c`](#insn-00afaf5c)

~~~json
{
  "source": "00afaf5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf60`](#insn-00afaf60)

~~~json
{
  "source": "00afaf60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
