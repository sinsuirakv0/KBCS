# 00afbfb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0018.md#review-5a7211e938afd56b8ff6fd4ae516485f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afc3e0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afc/00afc3e0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0006.md#compare-bc77c498f936451538da606410493972)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbfb8",
  "name": "FUN_00afbfb8",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d137a61fb6c4e013b4c4c6bc21b9ec03b295347b077674a50b720fd6903e4a99",
  "source_text_sha256": "d137a61fb6c4e013b4c4c6bc21b9ec03b295347b077674a50b720fd6903e4a99",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbfb8",
        "00afc003"
      ]
    ],
    "bytes_sha256": "7d9b8f015458c994f977af53e853147c62e38983fbc2a11ecf6ca1cf06fb764e",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00700ab8](../00700/00700ab8.md)
- [00710298](../00710/00710298.md)
- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 314 bytes

~~~c

void FUN_00afbfb8(int param_1,int param_2,undefined4 param_3)

{
  long lVar1;
  
                    /* try { // try from 00afbfc0 to 00bfc097 has its CatchHandler @ 00afb2b0 */
  lVar1 = FUN_008514b8();
  *(undefined4 *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84af4) = param_3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbfb8"></a> `00afbfb8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afbfbc"></a> `00afbfbc` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbfc0"></a> `00afbfc0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbfc4"></a> `00afbfc4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afbfc8"></a> `00afbfc8` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00afbfcc"></a> `00afbfcc` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00afbfd0"></a> `00afbfd0` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00afbfd4"></a> `00afbfd4` | `39 55 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afbfd8"></a> `00afbfd8` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afbfdc"></a> `00afbfdc` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afbfe0"></a> `00afbfe0` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00afbfe4"></a> `00afbfe4` | `88 22 29 9b` | smaddl x8,w20,w9,x8 | `FALL_THROUGH`
<a id="insn-00afbfe8"></a> `00afbfe8` | `89 5e 89 52` | mov w9,#0x4af4 | `FALL_THROUGH`
<a id="insn-00afbfec"></a> `00afbfec` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afbff0"></a> `00afbff0` | `13 69 29 b8` | str w19,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afbff4"></a> `00afbff4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbff8"></a> `00afbff8` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbffc"></a> `00afbffc` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afc000"></a> `00afc000` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbfb8`](#insn-00afbfb8) 範囲 `[['00afbfb8', '00afbfbf']]`
  - `FALL_THROUGH` [`00afbfbc`](#insn-00afbfbc) → [`00afbfc0`](#insn-00afbfc0)
- ブロック [`00afbfc0`](#insn-00afbfc0) 範囲 `[['00afbfc0', '00afc003']]`

## 命令位置別の参照

- [`00afbfb8`](#insn-00afbfb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbfbc`](#insn-00afbfbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbfc0`](#insn-00afbfc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbfd4`](#insn-00afbfd4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afbff4`](#insn-00afbff4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbff8`](#insn-00afbff8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbffc`](#insn-00afbffc) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbfb8`](#insn-00afbfb8)

~~~json
{
  "source": "00afbfb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbfbc`](#insn-00afbfbc)

~~~json
{
  "source": "00afbfbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbfc0`](#insn-00afbfc0)

~~~json
{
  "source": "00afbfc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbfd4`](#insn-00afbfd4)

~~~json
{
  "source": "00afbfd4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbff4`](#insn-00afbff4)

~~~json
{
  "source": "00afbff4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbff8`](#insn-00afbff8)

~~~json
{
  "source": "00afbff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbffc`](#insn-00afbffc)

~~~json
{
  "source": "00afbffc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
