# 00bfbad4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfb6ac`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfb/00bfb6ac.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-3e768ae9c5bbccbaa17d1988cd22ca76)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbb70`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbb70.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-686367bb3a1373a06790f21bf03b1a05)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbad4",
  "name": "_ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "08c71a162cc8ec6eb4b76c7bf0c4505c479a9e4053ba788bab7caf6832b6d909",
  "source_text_sha256": "08c71a162cc8ec6eb4b76c7bf0c4505c479a9e4053ba788bab7caf6832b6d909",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbad4",
        "00bfbaff"
      ]
    ],
    "bytes_sha256": "be6b37b0eb151662defec5bac95f53b9de1ae7b7c309797b237cbb0d980a426d",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e330](../00c5e/00c5e330.md)

## 呼び出し先

- [00c58500](../00c58/00c58500.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 360 bytes

~~~c

ulong _ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv(ulong param_1)

{
  undefined1 uVar1;
  ulong uVar2;
  
  *(uint *)(param_1 + 0x20) = *(uint *)(param_1 + 0x20) | 4;
  if ((*(byte *)(param_1 + 0x24) >> 2 & 1) == 0) {
    return param_1;
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
<a id="insn-00bfbad4"></a> `00bfbad4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfbad8"></a> `00bfbad8` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbadc"></a> `00bfbadc` | `09 90 40 39` | ldrb w9,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-00bfbae0"></a> `00bfbae0` | `08 01 1e 32` | orr w8,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfbae4"></a> `00bfbae4` | `08 20 00 b9` | str w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfbae8"></a> `00bfbae8` | `49 00 10 37` | tbnz w9,#0x2,0x00bfbaf0 | `CONDITIONAL_JUMP`
<a id="insn-00bfbaec"></a> `00bfbaec` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfbaf0"></a> `00bfbaf0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbaf4"></a> `00bfbaf4` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfbaf8"></a> `00bfbaf8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbafc"></a> `00bfbafc` | `81 72 01 94` | bl 0x00c58500 | `UNCONDITIONAL_CALL`

## 基本ブロックと分岐先

- ブロック [`00bfbad4`](#insn-00bfbad4) 範囲 `[['00bfbad4', '00bfbaeb']]`
  - `CONDITIONAL_JUMP` [`00bfbae8`](#insn-00bfbae8) → [`00bfbaf0`](#insn-00bfbaf0)
  - `FALL_THROUGH` [`00bfbae8`](#insn-00bfbae8) → [`00bfbaec`](#insn-00bfbaec)
- ブロック [`00bfbaec`](#insn-00bfbaec) 範囲 `[['00bfbaec', '00bfbaef']]`
- ブロック [`00bfbaf0`](#insn-00bfbaf0) 範囲 `[['00bfbaf0', '00bfbaff']]`
  - `FALL_THROUGH` [`00bfbafc`](#insn-00bfbafc) → [`00bfbb00`](00bfbb00.md)

## 命令位置別の参照

- [`00bfbae8`](#insn-00bfbae8) → [`00bfbaf0`](#insn-00bfbaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbaf4`](#insn-00bfbaf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbafc`](#insn-00bfbafc) → [`00c58500`](../00c58/00c58500.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58500` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbae8`](#insn-00bfbae8)

~~~json
{
  "source": "00bfbae8",
  "target": "00bfbaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbaf4`](#insn-00bfbaf4)

~~~json
{
  "source": "00bfbaf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbafc`](#insn-00bfbafc)

~~~json
{
  "source": "00bfbafc",
  "target": "00c58500",
  "target_space": "ram",
  "resolution": "function"
}
~~~
