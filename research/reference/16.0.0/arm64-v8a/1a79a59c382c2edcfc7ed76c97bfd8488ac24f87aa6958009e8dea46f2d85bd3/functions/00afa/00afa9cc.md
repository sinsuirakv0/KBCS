# 00afa9cc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0168.md#review-69348fe18fd4d3848a639c3ca5eb450b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00afadf4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00afa/00afadf4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0066.md#compare-f99978b428ad3802a282f602847236f5)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afa9cc",
  "name": "FUN_00afa9cc",
  "size": 76,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d493171bc6afc0e019390b7e69432ecc45a7c24b36aaf2940671b2cc34aa895d",
  "source_text_sha256": "d493171bc6afc0e019390b7e69432ecc45a7c24b36aaf2940671b2cc34aa895d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afa9cc",
        "00afaa17"
      ]
    ],
    "bytes_sha256": "99047fa4c963ade68f15ada7b352f6a01d39c637881ecdb21b9023d27b780872",
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

void FUN_00afa9cc(int param_1,int param_2,uint param_3)

{
  long lVar1;
  
  lVar1 = FUN_008514b8();
  *(uint *)(lVar1 + (long)param_1 * 0xc804 + (long)param_2 * 0x3ec + 0x84a84) = param_3 & 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afa9cc"></a> `00afa9cc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00afa9d0"></a> `00afa9d0` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afa9d4"></a> `00afa9d4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afa9d8"></a> `00afa9d8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00afa9dc"></a> `00afa9dc` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00afa9e0"></a> `00afa9e0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00afa9e4"></a> `00afa9e4` | `55 00 00 12` | and w21,w2,#0x1 | `FALL_THROUGH`
<a id="insn-00afa9e8"></a> `00afa9e8` | `b4 5a f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00afa9ec"></a> `00afa9ec` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00afa9f0"></a> `00afa9f0` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00afa9f4"></a> `00afa9f4` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00afa9f8"></a> `00afa9f8` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00afa9fc"></a> `00afa9fc` | `89 50 89 52` | mov w9,#0x4a84 | `FALL_THROUGH`
<a id="insn-00afaa00"></a> `00afaa00` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00afaa04"></a> `00afaa04` | `15 69 29 b8` | str w21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00afaa08"></a> `00afaa08` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaa0c"></a> `00afaa0c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afaa10"></a> `00afaa10` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00afaa14"></a> `00afaa14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afa9cc`](#insn-00afa9cc) 範囲 `[['00afa9cc', '00afaa17']]`

## 命令位置別の参照

- [`00afa9cc`](#insn-00afa9cc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa9d0`](#insn-00afa9d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa9d4`](#insn-00afa9d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afa9e8`](#insn-00afa9e8) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00afaa08`](#insn-00afaa08) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaa0c`](#insn-00afaa0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaa10`](#insn-00afaa10) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afa9cc`](#insn-00afa9cc)

~~~json
{
  "source": "00afa9cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa9d0`](#insn-00afa9d0)

~~~json
{
  "source": "00afa9d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa9d4`](#insn-00afa9d4)

~~~json
{
  "source": "00afa9d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afa9e8`](#insn-00afa9e8)

~~~json
{
  "source": "00afa9e8",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afaa08`](#insn-00afaa08)

~~~json
{
  "source": "00afaa08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaa0c`](#insn-00afaa0c)

~~~json
{
  "source": "00afaa0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaa10`](#insn-00afaa10)

~~~json
{
  "source": "00afaa10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
