# 00aface4

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0168.md#review-9818d04c2b0cc9b690756317bd93d46a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afb10c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afb/00afb10c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0006.md#compare-de42abd23d5382c4af6ced1aeb41f0f5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aface4",
  "name": "FUN_00aface4",
  "size": 72,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ee0d7769dce7e8e432b156fa828181ab84d4d55e86564c170553bed31b4cc27",
  "source_text_sha256": "2ee0d7769dce7e8e432b156fa828181ab84d4d55e86564c170553bed31b4cc27",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aface4",
        "00afad2b"
      ]
    ],
    "bytes_sha256": "656d4f3f9aa1acd4d2a783c6490c1a01a6eaa48d6ea42885f48cb765eae95085",
    "instruction_count": 18,
    "instruction_bytes": 72,
    "body_bytes": 72,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00710298](../00710/00710298.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 183 bytes

~~~c

bool FUN_00aface4(int param_1,int param_2)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  return *(int *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b04) != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aface4"></a> `00aface4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aface8"></a> `00aface8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afacec"></a> `00afacec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afacf0"></a> `00afacf0` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afacf4"></a> `00afacf4` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afacf8"></a> `00afacf8` | `f0 59 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afacfc"></a> `00afacfc` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afad00"></a> `00afad00` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afad04"></a> `00afad04` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afad08"></a> `00afad08` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afad0c"></a> `00afad0c` | `89 60 89 52` | mov w9,#0x4b04 | `FALL_THROUGH`
<a id="insn-00afad10"></a> `00afad10` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afad14"></a> `00afad14` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afad18"></a> `00afad18` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00afad1c"></a> `00afad1c` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00afad20"></a> `00afad20` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afad24"></a> `00afad24` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00afad28"></a> `00afad28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aface4`](#insn-00aface4) 範囲 `[['00aface4', '00afad2b']]`

## 命令位置別の参照

- [`00aface4`](#insn-00aface4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aface8`](#insn-00aface8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afacf8`](#insn-00afacf8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afad20`](#insn-00afad20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad24`](#insn-00afad24) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aface4`](#insn-00aface4)

~~~json
{
  "source": "00aface4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aface8`](#insn-00aface8)

~~~json
{
  "source": "00aface8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afacf8`](#insn-00afacf8)

~~~json
{
  "source": "00afacf8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad20`](#insn-00afad20)

~~~json
{
  "source": "00afad20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad24`](#insn-00afad24)

~~~json
{
  "source": "00afad24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
