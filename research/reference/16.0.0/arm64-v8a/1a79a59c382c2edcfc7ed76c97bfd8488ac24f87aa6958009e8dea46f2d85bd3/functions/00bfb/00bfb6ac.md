# 00bfb6ac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7ec64`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7e/00b7ec64.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/inspection-0020.md#compare-696f31e15d0853d335de88ec087b3f45)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbad4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbad4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-3e768ae9c5bbccbaa17d1988cd22ca76)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb6ac",
  "name": "_ZNSt6__ndk18ios_base34__set_failbit_and_consider_rethrowEv",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ccb94dbdabd3f2a88123c9c9a5c0d6240a09456125c6af1715840440cd1bc37f",
  "source_text_sha256": "ccb94dbdabd3f2a88123c9c9a5c0d6240a09456125c6af1715840440cd1bc37f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfb6ac",
        "00bfb6d7"
      ]
    ],
    "bytes_sha256": "bc872bfc72cef51c757fb6447a0ed04b225dd7b58a847b49e2f15cb7290fecfa",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5df30](../00c5d/00c5df30.md)

## 呼び出し先

- [00c58100](../00c58/00c58100.md)

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
  uVar2 = (ulong)DAT_00ca4408;
  DAT_00ca4408 = uVar1;
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfb6ac"></a> `00bfb6ac` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfb6b0"></a> `00bfb6b0` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb6b4"></a> `00bfb6b4` | `09 90 40 39` | ldrb w9,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-00bfb6b8"></a> `00bfb6b8` | `08 01 1e 32` | orr w8,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfb6bc"></a> `00bfb6bc` | `08 20 00 b9` | str w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb6c0"></a> `00bfb6c0` | `49 00 10 37` | tbnz w9,#0x2,0x00bfb6c8 | `CONDITIONAL_JUMP`
<a id="insn-00bfb6c4"></a> `00bfb6c4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfb6c8"></a> `00bfb6c8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfb6cc"></a> `00bfb6cc` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfb6d0"></a> `00bfb6d0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfb6d4"></a> `00bfb6d4` | `8b 72 01 94` | bl 0x00c58100 | `UNCONDITIONAL_CALL`

## 基本ブロックと分岐先

- ブロック [`00bfb6ac`](#insn-00bfb6ac) 範囲 `[['00bfb6ac', '00bfb6c3']]`
  - `CONDITIONAL_JUMP` [`00bfb6c0`](#insn-00bfb6c0) → [`00bfb6c8`](#insn-00bfb6c8)
  - `FALL_THROUGH` [`00bfb6c0`](#insn-00bfb6c0) → [`00bfb6c4`](#insn-00bfb6c4)
- ブロック [`00bfb6c4`](#insn-00bfb6c4) 範囲 `[['00bfb6c4', '00bfb6c7']]`
- ブロック [`00bfb6c8`](#insn-00bfb6c8) 範囲 `[['00bfb6c8', '00bfb6d7']]`
  - `FALL_THROUGH` [`00bfb6d4`](#insn-00bfb6d4) → [`00bfb6d8`](00bfb6d8.md)

## 命令位置別の参照

- [`00bfb6c0`](#insn-00bfb6c0) → [`00bfb6c8`](#insn-00bfb6c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb6cc`](#insn-00bfb6cc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb6d4`](#insn-00bfb6d4) → [`00c58100`](../00c58/00c58100.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58100` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfb6c0`](#insn-00bfb6c0)

~~~json
{
  "source": "00bfb6c0",
  "target": "00bfb6c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb6cc`](#insn-00bfb6cc)

~~~json
{
  "source": "00bfb6cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb6d4`](#insn-00bfb6d4)

~~~json
{
  "source": "00bfb6d4",
  "target": "00c58100",
  "target_space": "ram",
  "resolution": "function"
}
~~~
