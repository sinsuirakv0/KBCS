# 00bfabf0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfa7c8`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfa/00bfa7c8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-a5610e2a13cc9f2dbeb3f3b2b2a10ebb)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfac8c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfa/00bfac8c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-2bbb432faa287affe7cc9baa43ed28ed)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfabf0",
  "name": "_ZNSt6__ndk115__thread_structD1Ev",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e1514a8542a25f4aa387c17e64e04c04f510f9eb235192d5b2ba74cc3dc3421e",
  "source_text_sha256": "e1514a8542a25f4aa387c17e64e04c04f510f9eb235192d5b2ba74cc3dc3421e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfabf0",
        "00bfac33"
      ]
    ],
    "bytes_sha256": "e93a4269434abc21fd8e9bbb849cd8be09623c353e50eeee1caab7c3a340fdf4",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58150](../00c58/00c58150.md)

## 呼び出し先

- [00bfa8fc](../00bfa/00bfa8fc.md)
- [00c57eb0](../00c57/00c57eb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 213 bytes

~~~c

void _ZNSt6__ndk115__thread_structD1Ev(undefined8 *param_1)

{
  void *__ptr;
  
  __ptr = (void *)*param_1;
  if (__ptr != (void *)0x0) {
    FUN_00bfa8fc(__ptr);
    _ZdlPv(__ptr);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfabf0"></a> `00bfabf0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfabf4"></a> `00bfabf4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfabf8"></a> `00bfabf8` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfabfc"></a> `00bfabfc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfac00"></a> `00bfac00` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-00bfac04"></a> `00bfac04` | `13 01 00 b4` | cbz x19,0x00bfac24 | `CONDITIONAL_JUMP`
<a id="insn-00bfac08"></a> `00bfac08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfac0c"></a> `00bfac0c` | `3c ff ff 97` | bl 0x00bfa8fc | `UNCONDITIONAL_CALL`
<a id="insn-00bfac10"></a> `00bfac10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfac14"></a> `00bfac14` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfac18"></a> `00bfac18` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfac1c"></a> `00bfac1c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfac20"></a> `00bfac20` | `a4 74 01 14` | b 0x00c57eb0 | `CALL_TERMINATOR`
<a id="insn-00bfac24"></a> `00bfac24` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfac28"></a> `00bfac28` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfac2c"></a> `00bfac2c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfac30"></a> `00bfac30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfabf0`](#insn-00bfabf0) 範囲 `[['00bfabf0', '00bfac07']]`
  - `CONDITIONAL_JUMP` [`00bfac04`](#insn-00bfac04) → [`00bfac24`](#insn-00bfac24)
  - `FALL_THROUGH` [`00bfac04`](#insn-00bfac04) → [`00bfac08`](#insn-00bfac08)
- ブロック [`00bfac08`](#insn-00bfac08) 範囲 `[['00bfac08', '00bfac23']]`
- ブロック [`00bfac24`](#insn-00bfac24) 範囲 `[['00bfac24', '00bfac33']]`

## 命令位置別の参照

- [`00bfabf4`](#insn-00bfabf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfabf8`](#insn-00bfabf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac04`](#insn-00bfac04) → [`00bfac24`](#insn-00bfac24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac0c`](#insn-00bfac0c) → [`00bfa8fc`](00bfa8fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bfa8fc` · 推定シンボル `None` · 推定型 `None`
- [`00bfac14`](#insn-00bfac14) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac18`](#insn-00bfac18) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac20`](#insn-00bfac20) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bfac24`](#insn-00bfac24) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfac28`](#insn-00bfac28) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfabf4`](#insn-00bfabf4)

~~~json
{
  "source": "00bfabf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfabf8`](#insn-00bfabf8)

~~~json
{
  "source": "00bfabf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac04`](#insn-00bfac04)

~~~json
{
  "source": "00bfac04",
  "target": "00bfac24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac0c`](#insn-00bfac0c)

~~~json
{
  "source": "00bfac0c",
  "target": "00bfa8fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfac14`](#insn-00bfac14)

~~~json
{
  "source": "00bfac14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac18`](#insn-00bfac18)

~~~json
{
  "source": "00bfac18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac20`](#insn-00bfac20)

~~~json
{
  "source": "00bfac20",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfac24`](#insn-00bfac24)

~~~json
{
  "source": "00bfac24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfac28`](#insn-00bfac28)

~~~json
{
  "source": "00bfac28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
