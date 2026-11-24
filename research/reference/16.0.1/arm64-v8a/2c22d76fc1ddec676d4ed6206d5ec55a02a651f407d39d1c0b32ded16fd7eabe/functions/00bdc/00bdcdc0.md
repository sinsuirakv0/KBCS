# 00bdcdc0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdc998`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdc/00bdc998.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-7846eff7d206b80389eab9935e167f18)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdce5c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdc/00bdce5c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-251c7161dd9a12177686e99b84e08e88)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdc0",
  "name": "_ZN8firebase4auth19PhoneAuthCredentialC2ERKS1_",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2ff4a5e6b888bed776958bce3c89bc007dd95f72ae91d09bb4ef56becee4deff",
  "source_text_sha256": "2ff4a5e6b888bed776958bce3c89bc007dd95f72ae91d09bb4ef56becee4deff",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcdc0",
        "00bdcdf3"
      ]
    ],
    "bytes_sha256": "89e8986bd9d2d0f75c11f6c3ad8dcde8d44af5edd43bb5a029c7d0103d26d508",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5de30](../00c5d/00c5de30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 302 bytes

~~~c

void _ZN8firebase4auth19PhoneAuthCredentialC2ERKS1_(undefined8 *param_1)

{
  *param_1 = 0;
  *(undefined4 *)(param_1 + 1) = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  _ZN8firebase4auth19PhoneAuthCredentialaSERKS1_();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcdc0"></a> `00bdcdc0` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bdcdc4"></a> `00bdcdc4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcdc8"></a> `00bdcdc8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bdcdcc"></a> `00bdcdcc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdcdd0"></a> `00bdcdd0` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bdcdd4"></a> `00bdcdd4` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bdcdd8"></a> `00bdcdd8` | `1f 08 00 b9` | str wzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bdcddc"></a> `00bdcddc` | `00 80 00 ad` | stp q0,q0,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcde0"></a> `00bdcde0` | `00 0c 80 3d` | str q0,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bdcde4"></a> `00bdcde4` | `13 04 02 94` | bl 0x00c5de30 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcde8"></a> `00bdcde8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcdec"></a> `00bdcdec` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bdcdf0"></a> `00bdcdf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcdc0`](#insn-00bdcdc0) 範囲 `[['00bdcdc0', '00bdcdf3']]`

## 命令位置別の参照

- [`00bdcdc0`](#insn-00bdcdc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcdc4`](#insn-00bdcdc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcde4`](#insn-00bdcde4) → [`00c5de30`](../00c5d/00c5de30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de30` · 推定シンボル `None` · 推定型 `None`
- [`00bdcde8`](#insn-00bdcde8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcdc0`](#insn-00bdcdc0)

~~~json
{
  "source": "00bdcdc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcdc4`](#insn-00bdcdc4)

~~~json
{
  "source": "00bdcdc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcde4`](#insn-00bdcde4)

~~~json
{
  "source": "00bdcde4",
  "target": "00c5de30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcde8`](#insn-00bdcde8)

~~~json
{
  "source": "00bdcde8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
