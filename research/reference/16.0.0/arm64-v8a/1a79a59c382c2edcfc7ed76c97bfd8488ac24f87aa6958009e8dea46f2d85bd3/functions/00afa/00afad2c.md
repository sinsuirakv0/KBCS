# 00afad2c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0168.md#review-3336ed2fe31619aa42d5dcdbccc3306d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afb154`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afb/00afb154.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/alignment_unresolved-0006.md#compare-3fbc1bcb367cb56ef82ea9b97ef3e30c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afad2c",
  "name": "FUN_00afad2c",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "685c1bb290581786edacda83c309b9f6a4b5a4711a86668244a7254602b30b5c",
  "source_text_sha256": "685c1bb290581786edacda83c309b9f6a4b5a4711a86668244a7254602b30b5c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afad2c",
        "00afad77"
      ]
    ],
    "bytes_sha256": "64935b4ba7303e4c4677e59b8331c3f4bb940988c6bec61eb5d62e763289f7ac",
    "instruction_count": 19,
    "instruction_bytes": 76,
    "body_bytes": 76,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a4f1bc](../00a4f/00a4f1bc.md)

## 呼び出し先

- [008514b8](../00851/008514b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 209 bytes

~~~c

void FUN_00afad2c(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84b04) = param_3 & 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afad2c"></a> `00afad2c` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afad30"></a> `00afad30` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afad34"></a> `00afad34` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afad38"></a> `00afad38` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afad3c"></a> `00afad3c` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afad40"></a> `00afad40` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afad44"></a> `00afad44` | `55 00 00 12` | and w21,w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afad48"></a> `00afad48` | `dc 59 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afad4c"></a> `00afad4c` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afad50"></a> `00afad50` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afad54"></a> `00afad54` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afad58"></a> `00afad58` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afad5c"></a> `00afad5c` | `89 60 89 52` | mov w9,#0x4b04 | `FALL_THROUGH`
<a id="insn-00afad60"></a> `00afad60` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afad64"></a> `00afad64` | `15 69 29 b8` | str w21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afad68"></a> `00afad68` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afad6c"></a> `00afad6c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afad70"></a> `00afad70` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afad74"></a> `00afad74` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afad2c`](#insn-00afad2c) 範囲 `[['00afad2c', '00afad77']]`

## 命令位置別の参照

- [`00afad2c`](#insn-00afad2c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad30`](#insn-00afad30) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad34`](#insn-00afad34) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad48`](#insn-00afad48) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afad68`](#insn-00afad68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad6c`](#insn-00afad6c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afad70`](#insn-00afad70) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afad2c`](#insn-00afad2c)

~~~json
{
  "source": "00afad2c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad30`](#insn-00afad30)

~~~json
{
  "source": "00afad30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad34`](#insn-00afad34)

~~~json
{
  "source": "00afad34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad48`](#insn-00afad48)

~~~json
{
  "source": "00afad48",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afad68`](#insn-00afad68)

~~~json
{
  "source": "00afad68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad6c`](#insn-00afad6c)

~~~json
{
  "source": "00afad6c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afad70`](#insn-00afad70)

~~~json
{
  "source": "00afad70",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
