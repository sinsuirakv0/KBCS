# 007aeedc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0128.md#review-2a6e5ac6d516cd6862cc73a3429f9111)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `007aef1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007ae/007aef1c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0025.md#compare-737ff426ebded2cdebb75027a8fdbac6)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007aeedc",
  "name": "FUN_007aeedc",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0edc2898be99fbe0cbd645cc583a434960bf48e6337505d89e5de3b4b5f2fd78",
  "source_text_sha256": "0edc2898be99fbe0cbd645cc583a434960bf48e6337505d89e5de3b4b5f2fd78",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007aeedc",
        "007aef0f"
      ]
    ],
    "bytes_sha256": "68a89c567a13328833a20b916dd1601ed8ba7e654d67b98c5171ca647cb51b62",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007ad944](../007ad/007ad944.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 168 bytes

~~~c

void FUN_007aeedc(void *param_1)

{
  if ((*(byte *)((long)param_1 + 8) & 1) != 0) {
    _ZdlPv(*(void **)((long)param_1 + 0x18));
  }
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007aeedc"></a> `007aeedc` | `08 20 40 39` | ldrb w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-007aeee0"></a> `007aeee0` | `68 01 00 36` | tbz w8,#0x0,0x007aef0c | `CONDITIONAL_JUMP`
<a id="insn-007aeee4"></a> `007aeee4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007aeee8"></a> `007aeee8` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007aeeec"></a> `007aeeec` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007aeef0"></a> `007aeef0` | `08 0c 40 f9` | ldr x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-007aeef4"></a> `007aeef4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007aeef8"></a> `007aeef8` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-007aeefc"></a> `007aeefc` | `ed a2 12 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-007aef00"></a> `007aef00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007aef04"></a> `007aef04` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007aef08"></a> `007aef08` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007aef0c"></a> `007aef0c` | `e9 a2 12 14` | b 0x00c57ab0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007aeedc`](#insn-007aeedc) 範囲 `[['007aeedc', '007aeee3']]`
  - `CONDITIONAL_JUMP` [`007aeee0`](#insn-007aeee0) → [`007aef0c`](#insn-007aef0c)
  - `FALL_THROUGH` [`007aeee0`](#insn-007aeee0) → [`007aeee4`](#insn-007aeee4)
- ブロック [`007aeee4`](#insn-007aeee4) 範囲 `[['007aeee4', '007aef0b']]`
  - `FALL_THROUGH` [`007aef08`](#insn-007aef08) → [`007aef0c`](#insn-007aef0c)
- ブロック [`007aef0c`](#insn-007aef0c) 範囲 `[['007aef0c', '007aef0f']]`

## 命令位置別の参照

- [`007aeee0`](#insn-007aeee0) → [`007aef0c`](#insn-007aef0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aeee4`](#insn-007aeee4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aeee8`](#insn-007aeee8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aeefc`](#insn-007aeefc) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`007aef04`](#insn-007aef04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aef08`](#insn-007aef08) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007aef0c`](#insn-007aef0c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007aeee0`](#insn-007aeee0)

~~~json
{
  "source": "007aeee0",
  "target": "007aef0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aeee4`](#insn-007aeee4)

~~~json
{
  "source": "007aeee4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aeee8`](#insn-007aeee8)

~~~json
{
  "source": "007aeee8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aeefc`](#insn-007aeefc)

~~~json
{
  "source": "007aeefc",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007aef04`](#insn-007aef04)

~~~json
{
  "source": "007aef04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aef08`](#insn-007aef08)

~~~json
{
  "source": "007aef08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007aef0c`](#insn-007aef0c)

~~~json
{
  "source": "007aef0c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
