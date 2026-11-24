# 005badcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `005bad8c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/005ba/005bad8c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0016.md#compare-fa535daf5b7d44a45d3d715d9f240410)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `005bae0c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/005ba/005bae0c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0016.md#compare-6d512faeba20462fbc7988191fc7282e)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005badcc",
  "name": "FUN_005badcc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3927f9875075bf785219f1a4e1220474854815864f78628d56406ed918b6ec2",
  "source_text_sha256": "e3927f9875075bf785219f1a4e1220474854815864f78628d56406ed918b6ec2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005badcc",
        "005badef"
      ]
    ],
    "bytes_sha256": "cd8956658c2acb2b0452c572a4720e1806292969d6446b08406cef2bc956a66e",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005ba958](../005ba/005ba958.md)

## 呼び出し先

- [00c58530](../00c58/00c58530.md)
- [00c58540](../00c58/00c58540.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 260 bytes

~~~c

void FUN_005badcc(undefined8 param_1)

{
                    /* try { // try from 005badd4 to 006bade3 has its CatchHandler @ 005baec8 */
  _ZNSt6__ndk117__assoc_sub_state4waitEv();
  _ZNSt6__ndk117__assoc_sub_state16__on_zero_sharedEv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005badcc"></a> `005badcc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-005badd0"></a> `005badd0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005badd4"></a> `005badd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005badd8"></a> `005badd8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005baddc"></a> `005baddc` | `d5 75 1a 94` | bl 0x00c58530 | `UNCONDITIONAL_CALL`
<a id="insn-005bade0"></a> `005bade0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-005bade4"></a> `005bade4` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005bade8"></a> `005bade8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-005badec"></a> `005badec` | `d5 75 1a 14` | b 0x00c58540 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005badcc`](#insn-005badcc) 範囲 `[['005badcc', '005badd3']]`
  - `FALL_THROUGH` [`005badd0`](#insn-005badd0) → [`005badd4`](#insn-005badd4)
- ブロック [`005badd4`](#insn-005badd4) 範囲 `[['005badd4', '005badef']]`

## 命令位置別の参照

- [`005badcc`](#insn-005badcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005badd0`](#insn-005badd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005baddc`](#insn-005baddc) → [`00c58530`](../00c58/00c58530.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58530` · 推定シンボル `None` · 推定型 `None`
- [`005bade4`](#insn-005bade4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005bade8`](#insn-005bade8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005badec`](#insn-005badec) → [`00c58540`](../00c58/00c58540.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58540` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005badcc`](#insn-005badcc)

~~~json
{
  "source": "005badcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005badd0`](#insn-005badd0)

~~~json
{
  "source": "005badd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005baddc`](#insn-005baddc)

~~~json
{
  "source": "005baddc",
  "target": "00c58530",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005bade4`](#insn-005bade4)

~~~json
{
  "source": "005bade4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005bade8`](#insn-005bade8)

~~~json
{
  "source": "005bade8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005badec`](#insn-005badec)

~~~json
{
  "source": "005badec",
  "target": "00c58540",
  "target_space": "ram",
  "resolution": "function"
}
~~~
