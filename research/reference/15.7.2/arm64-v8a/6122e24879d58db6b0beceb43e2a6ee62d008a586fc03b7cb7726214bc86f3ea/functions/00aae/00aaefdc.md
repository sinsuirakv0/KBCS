# 00aaefdc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aaf0a4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaf/00aaf0a4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-7d229f861e853d5a6375f36bc54b019e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaefdc",
  "name": "FUN_00aaefdc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "18a316590f89e48711067541018de778bf8f65b796131c55c9ad510006c232b2",
  "source_text_sha256": "18a316590f89e48711067541018de778bf8f65b796131c55c9ad510006c232b2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaefdc",
        "00aaf013"
      ]
    ],
    "bytes_sha256": "e7215790d5513b15b2dc9585e381edef62451840d30dd6261725a06540e27dd0",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009bd6b8](../009bd/009bd6b8.md)

## 呼び出し先

- [0045d518](../0045d/0045d518.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 206 bytes

~~~c

void FUN_00aaefdc(undefined4 *param_1,undefined8 param_2)

{
  undefined4 uVar1;
  
  uVar1 = FUN_0045d518(param_2);
  *param_1 = uVar1;
  uVar1 = FUN_0045d518(param_2);
  param_1[1] = uVar1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaefdc"></a> `00aaefdc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00aaefe0"></a> `00aaefe0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaefe4"></a> `00aaefe4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00aaefe8"></a> `00aaefe8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aaefec"></a> `00aaefec` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00aaeff0"></a> `00aaeff0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00aaeff4"></a> `00aaeff4` | `49 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaeff8"></a> `00aaeff8` | `80 02 00 b9` | str w0,[x20] | `FALL_THROUGH`
<a id="insn-00aaeffc"></a> `00aaeffc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aaf000"></a> `00aaf000` | `46 b9 e6 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00aaf004"></a> `00aaf004` | `80 06 00 b9` | str w0,[x20, #0x4] | `FALL_THROUGH`
<a id="insn-00aaf008"></a> `00aaf008` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaf00c"></a> `00aaf00c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00aaf010"></a> `00aaf010` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaefdc`](#insn-00aaefdc) 範囲 `[['00aaefdc', '00aaf013']]`

## 命令位置別の参照

- [`00aaefdc`](#insn-00aaefdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaefe0`](#insn-00aaefe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaeff4`](#insn-00aaeff4) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaf000`](#insn-00aaf000) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00aaf008`](#insn-00aaf008) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaf00c`](#insn-00aaf00c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaefdc`](#insn-00aaefdc)

~~~json
{
  "source": "00aaefdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaefe0`](#insn-00aaefe0)

~~~json
{
  "source": "00aaefe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaeff4`](#insn-00aaeff4)

~~~json
{
  "source": "00aaeff4",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf000`](#insn-00aaf000)

~~~json
{
  "source": "00aaf000",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaf008`](#insn-00aaf008)

~~~json
{
  "source": "00aaf008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaf00c`](#insn-00aaf00c)

~~~json
{
  "source": "00aaf00c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
