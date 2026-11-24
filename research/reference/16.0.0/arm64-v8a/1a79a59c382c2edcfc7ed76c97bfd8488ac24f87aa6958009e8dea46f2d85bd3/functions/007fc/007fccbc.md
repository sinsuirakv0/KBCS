# 007fccbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0134.md#review-9d54e028b7caea143ca169db2d3035de)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `007fccfc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fc/007fccfc.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0041.md#compare-2b7d16f4b9f8a370ccb9e2267b2800d9)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007fccbc",
  "name": "FUN_007fccbc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e5019a43f7e16b215ed9b471587b5532c7df8d845c6432208a1d594505a96d24",
  "source_text_sha256": "e5019a43f7e16b215ed9b471587b5532c7df8d845c6432208a1d594505a96d24",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007fccbc",
        "007fccf3"
      ]
    ],
    "bytes_sha256": "1d82a9794896b7bf25b9e817a9fea2bb741bfdd47544d7616d5c834b21bb7a76",
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

- [00c57a90](../00c57/00c57a90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 242 bytes

~~~c

void FUN_007fccbc(long param_1)

{
  undefined4 uVar1;
  undefined8 *puVar2;
  
  puVar2 = (undefined8 *)_Znwm(0x10);
  uVar1 = *(undefined4 *)(param_1 + 8);
  *puVar2 = &PTR_FUN_00c7d330;
  *(undefined4 *)(puVar2 + 1) = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007fccbc"></a> `007fccbc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-007fccc0"></a> `007fccc0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fccc4"></a> `007fccc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-007fccc8"></a> `007fccc8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007fcccc"></a> `007fcccc` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-007fccd0"></a> `007fccd0` | `70 6b 11 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-007fccd4"></a> `007fccd4` | `69 0a 40 b9` | ldr w9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-007fccd8"></a> `007fccd8` | `08 24 00 b0` | adrp x8,0xc7d000 | `FALL_THROUGH`
<a id="insn-007fccdc"></a> `007fccdc` | `08 c1 0c 91` | add x8,x8,#0x330 | `FALL_THROUGH`
<a id="insn-007fcce0"></a> `007fcce0` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-007fcce4"></a> `007fcce4` | `09 08 00 b9` | str w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-007fcce8"></a> `007fcce8` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-007fccec"></a> `007fccec` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-007fccf0"></a> `007fccf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007fccbc`](#insn-007fccbc) 範囲 `[['007fccbc', '007fccf3']]`

## 命令位置別の参照

- [`007fccbc`](#insn-007fccbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fccc0`](#insn-007fccc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fccd0`](#insn-007fccd0) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`007fcce0`](#insn-007fcce0) → `00c7d330`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`007fcce8`](#insn-007fcce8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fccec`](#insn-007fccec) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007fccbc`](#insn-007fccbc)

~~~json
{
  "source": "007fccbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fccc0`](#insn-007fccc0)

~~~json
{
  "source": "007fccc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fccd0`](#insn-007fccd0)

~~~json
{
  "source": "007fccd0",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fcce0`](#insn-007fcce0)

~~~json
{
  "source": "007fcce0",
  "target": "00c7d330",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c7d330",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007fcce8`](#insn-007fcce8)

~~~json
{
  "source": "007fcce8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fccec`](#insn-007fccec)

~~~json
{
  "source": "007fccec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
