# 00bfbaa8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfb680`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb680.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-c62b2ab8d297bd0ab97f7243d6235d93)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbb44`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbb44.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-88132b8f589595a3de6bbd3b71748b2a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbaa8",
  "name": "_ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "54b1080809d51488145875c832f580a81e87c981d15c92371446a7849832a727",
  "source_text_sha256": "54b1080809d51488145875c832f580a81e87c981d15c92371446a7849832a727",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbaa8",
        "00bfbad3"
      ]
    ],
    "bytes_sha256": "8bde66a11a3f14c379683e62aefae02e623b9925905ee013f2ad4877d0d57ddb",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c582c0](../00c58/00c582c0.md)

## 呼び出し先

- [00c58500](../00c58/00c58500.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 509 bytes

~~~c

ulong _ZNSt6__ndk18ios_base33__set_badbit_and_consider_rethrowEv(ulong param_1)

{
  undefined1 uVar1;
  ulong uVar2;
  
  *(uint *)(param_1 + 0x20) = *(uint *)(param_1 + 0x20) | 1;
  if ((*(byte *)(param_1 + 0x24) & 1) == 0) {
    return param_1;
  }
  uVar2 = __cxa_rethrow();
  *(uint *)(uVar2 + 0x20) = *(uint *)(uVar2 + 0x20) | 4;
  if ((*(byte *)(uVar2 + 0x24) >> 2 & 1) == 0) {
    return uVar2;
  }
  uVar1 = __cxa_rethrow();
  uVar2 = (ulong)DAT_00ca4808;
  DAT_00ca4808 = uVar1;
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbaa8"></a> `00bfbaa8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfbaac"></a> `00bfbaac` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbab0"></a> `00bfbab0` | `09 90 40 39` | ldrb w9,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-00bfbab4"></a> `00bfbab4` | `08 01 00 32` | orr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfbab8"></a> `00bfbab8` | `08 20 00 b9` | str w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbabc"></a> `00bfbabc` | `49 00 00 37` | tbnz w9,#0x0,0x00bfbac4 | `CONDITIONAL_JUMP`
<a id="insn-00bfbac0"></a> `00bfbac0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfbac4"></a> `00bfbac4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbac8"></a> `00bfbac8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfbacc"></a> `00bfbacc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbad0"></a> `00bfbad0` | `8c 72 01 94` | bl 0x00c58500 | `UNCONDITIONAL_CALL`

## 基本ブロックと分岐先

- ブロック [`00bfbaa8`](#insn-00bfbaa8) 範囲 `[['00bfbaa8', '00bfbabf']]`
  - `CONDITIONAL_JUMP` [`00bfbabc`](#insn-00bfbabc) → [`00bfbac4`](#insn-00bfbac4)
  - `FALL_THROUGH` [`00bfbabc`](#insn-00bfbabc) → [`00bfbac0`](#insn-00bfbac0)
- ブロック [`00bfbac0`](#insn-00bfbac0) 範囲 `[['00bfbac0', '00bfbac3']]`
- ブロック [`00bfbac4`](#insn-00bfbac4) 範囲 `[['00bfbac4', '00bfbad3']]`
  - `FALL_THROUGH` [`00bfbad0`](#insn-00bfbad0) → [`00bfbad4`](00bfbad4.md)

## 命令位置別の参照

- [`00bfbabc`](#insn-00bfbabc) → [`00bfbac4`](#insn-00bfbac4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbac8`](#insn-00bfbac8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbad0`](#insn-00bfbad0) → [`00c58500`](../00c58/00c58500.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58500` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbabc`](#insn-00bfbabc)

~~~json
{
  "source": "00bfbabc",
  "target": "00bfbac4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbac8`](#insn-00bfbac8)

~~~json
{
  "source": "00bfbac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbad0`](#insn-00bfbad0)

~~~json
{
  "source": "00bfbad0",
  "target": "00c58500",
  "target_space": "ram",
  "resolution": "function"
}
~~~
