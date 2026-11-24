# 00bfadf4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfad58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfa/00bfad58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-20003a1c7729fa1dcfeba1f37098c86c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfbde8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfb/00bfbde8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-d2af5fa10dd6cc688fe5eb764313944c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfadf4",
  "name": "_ZNSt6__ndk113random_deviceD1Ev",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "972ed633fa8eb8b3ab5a15472706f5ea320d386143d89d93d243c151d808cea3",
  "source_text_sha256": "972ed633fa8eb8b3ab5a15472706f5ea320d386143d89d93d243c151d808cea3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfadf4",
        "00bfae13"
      ]
    ],
    "bytes_sha256": "de6acee7a5d27fb51ad40ef0de4a17d81caf472360d660b3824015b7542ae37a",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c584a0](../00c58/00c584a0.md)

## 呼び出し先

- [00c598a0](../00c59/00c598a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 116 bytes

~~~c

int _ZNSt6__ndk113random_deviceD1Ev(int *param_1)

{
  int iVar1;
  
  iVar1 = close(*param_1);
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfadf4"></a> `00bfadf4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfadf8"></a> `00bfadf8` | `fd 7b bf a9` | stp x29,x30,[sp, #-0x10]! | `FALL_THROUGH`
<a id="insn-00bfadfc"></a> `00bfadfc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfae00"></a> `00bfae00` | `00 00 40 b9` | ldr w0,[x0] | `FALL_THROUGH`
<a id="insn-00bfae04"></a> `00bfae04` | `a7 7a 01 94` | bl 0x00c598a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfae08"></a> `00bfae08` | `fd 7b c1 a8` | ldp x29,x30,[sp], #0x10 | `FALL_THROUGH`
<a id="insn-00bfae0c"></a> `00bfae0c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfae10"></a> `00bfae10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfadf4`](#insn-00bfadf4) 範囲 `[['00bfadf4', '00bfae13']]`

## 命令位置別の参照

- [`00bfadf8`](#insn-00bfadf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfae04`](#insn-00bfae04) → [`00c598a0`](../00c59/00c598a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c598a0` · 推定シンボル `None` · 推定型 `None`
- [`00bfae08`](#insn-00bfae08) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfadf8`](#insn-00bfadf8)

~~~json
{
  "source": "00bfadf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfae04`](#insn-00bfae04)

~~~json
{
  "source": "00bfae04",
  "target": "00c598a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfae08`](#insn-00bfae08)

~~~json
{
  "source": "00bfae08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
