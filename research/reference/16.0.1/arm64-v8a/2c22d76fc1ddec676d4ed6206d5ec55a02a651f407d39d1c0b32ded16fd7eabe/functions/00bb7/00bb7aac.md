# 00bb7aac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bb7684`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bb7/00bb7684.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-2e3d36214ae42444c184bd8bc4ae8caa)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bb7b48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bb7/00bb7b48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-5cb16f31a23deb7ab9139d43415d1912)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb7aac",
  "name": "_ZN8firebase9messaging7MessageC2ERKS1_",
  "size": 136,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4f13c5569bbdf0d80889de3869c13db4ce7dcab10f1118eefa942a9a5cde055b",
  "source_text_sha256": "4f13c5569bbdf0d80889de3869c13db4ce7dcab10f1118eefa942a9a5cde055b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb7aac",
        "00bb7b33"
      ]
    ],
    "bytes_sha256": "aa03a4fd4bd7749cc74e41ffe19da5d843ca7319a3b29cf0dfef9cb3540891dd",
    "instruction_count": 34,
    "instruction_bytes": 136,
    "body_bytes": 136,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d3e0](../00c5d/00c5d3e0.md)

## 呼び出し先

- [00c5d400](../00c5d/00c5d400.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 875 bytes

~~~c

void _ZN8firebase9messaging7MessageC2ERKS1_(undefined8 *param_1)

{
  param_1[10] = 0;
  param_1[9] = param_1 + 10;
  param_1[0xb] = 0;
  param_1[1] = 0;
  *param_1 = 0;
  param_1[3] = 0;
  param_1[2] = 0;
  param_1[5] = 0;
  param_1[4] = 0;
  param_1[7] = 0;
  param_1[6] = 0;
  param_1[8] = 0;
  param_1[0xd] = 0;
  param_1[0xc] = 0;
  param_1[0x1a] = 0;
  param_1[0x19] = 0;
  param_1[0xf] = 0;
  param_1[0xe] = 0;
  param_1[0x11] = 0;
  param_1[0x10] = 0;
  param_1[0x13] = 0;
  param_1[0x12] = 0;
  param_1[0x15] = 0;
  param_1[0x14] = 0;
  param_1[0x17] = 0;
  param_1[0x16] = 0;
  param_1[0x1c] = 0;
  param_1[0x1b] = 0;
  param_1[0x1e] = 0;
  param_1[0x1d] = 0;
  param_1[0x1f] = 0;
  param_1[0x24] = 0;
  param_1[0x23] = 0;
  param_1[0x26] = 0;
  param_1[0x25] = 0;
  param_1[0x22] = 0;
  param_1[0x21] = 0;
  _ZN8firebase9messaging7MessageaSERKS1_();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb7aac"></a> `00bb7aac` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bb7ab0"></a> `00bb7ab0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb7ab4"></a> `00bb7ab4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb7ab8"></a> `00bb7ab8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb7abc"></a> `00bb7abc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bb7ac0"></a> `00bb7ac0` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bb7ac4"></a> `00bb7ac4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bb7ac8"></a> `00bb7ac8` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bb7acc"></a> `00bb7acc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bb7ad0"></a> `00bb7ad0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bb7ad4"></a> `00bb7ad4` | `1f 0d 05 f8` | str xzr,[x8, #0x50]! | `FALL_THROUGH`
<a id="insn-00bb7ad8"></a> `00bb7ad8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb7adc"></a> `00bb7adc` | `88 8e 04 f8` | str x8,[x20, #0x48]! | `FALL_THROUGH`
<a id="insn-00bb7ae0"></a> `00bb7ae0` | `18 20 04 91` | add x24,x0,#0x108 | `FALL_THROUGH`
<a id="insn-00bb7ae4"></a> `00bb7ae4` | `1f 2c 00 f9` | str xzr,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00bb7ae8"></a> `00bb7ae8` | `00 00 00 ad` | stp q0,q0,[x0] | `FALL_THROUGH`
<a id="insn-00bb7aec"></a> `00bb7aec` | `00 00 01 ad` | stp q0,q0,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bb7af0"></a> `00bb7af0` | `1f 20 00 f9` | str xzr,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bb7af4"></a> `00bb7af4` | `c0 0e 86 3c` | str q0,[x22, #0x60]! | `FALL_THROUGH`
<a id="insn-00bb7af8"></a> `00bb7af8` | `e0 8e 8c 3c` | str q0,[x23, #0xc8]! | `FALL_THROUGH`
<a id="insn-00bb7afc"></a> `00bb7afc` | `00 80 03 ad` | stp q0,q0,[x0, #0x70] | `FALL_THROUGH`
<a id="insn-00bb7b00"></a> `00bb7b00` | `00 80 04 ad` | stp q0,q0,[x0, #0x90] | `FALL_THROUGH`
<a id="insn-00bb7b04"></a> `00bb7b04` | `00 2c 80 3d` | str q0,[x0, #0xb0] | `FALL_THROUGH`
<a id="insn-00bb7b08"></a> `00bb7b08` | `00 80 8d 3c` | stur q0,[x0, #0xd8] | `FALL_THROUGH`
<a id="insn-00bb7b0c"></a> `00bb7b0c` | `00 80 8e 3c` | stur q0,[x0, #0xe8] | `FALL_THROUGH`
<a id="insn-00bb7b10"></a> `00bb7b10` | `1f 7c 00 f9` | str xzr,[x0, #0xf8] | `FALL_THROUGH`
<a id="insn-00bb7b14"></a> `00bb7b14` | `00 83 00 ad` | stp q0,q0,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bb7b18"></a> `00bb7b18` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00bb7b1c"></a> `00bb7b1c` | `39 96 02 94` | bl 0x00c5d400 | `UNCONDITIONAL_CALL`
<a id="insn-00bb7b20"></a> `00bb7b20` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb7b24"></a> `00bb7b24` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb7b28"></a> `00bb7b28` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb7b2c"></a> `00bb7b2c` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bb7b30"></a> `00bb7b30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb7aac`](#insn-00bb7aac) 範囲 `[['00bb7aac', '00bb7b33']]`

## 命令位置別の参照

- [`00bb7aac`](#insn-00bb7aac) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7ab0`](#insn-00bb7ab0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7ab4`](#insn-00bb7ab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7ab8`](#insn-00bb7ab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7b1c`](#insn-00bb7b1c) → [`00c5d400`](../00c5d/00c5d400.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d400` · 推定シンボル `None` · 推定型 `None`
- [`00bb7b20`](#insn-00bb7b20) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7b24`](#insn-00bb7b24) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb7b28`](#insn-00bb7b28) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb7aac`](#insn-00bb7aac)

~~~json
{
  "source": "00bb7aac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7ab0`](#insn-00bb7ab0)

~~~json
{
  "source": "00bb7ab0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7ab4`](#insn-00bb7ab4)

~~~json
{
  "source": "00bb7ab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7ab8`](#insn-00bb7ab8)

~~~json
{
  "source": "00bb7ab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7b1c`](#insn-00bb7b1c)

~~~json
{
  "source": "00bb7b1c",
  "target": "00c5d400",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb7b20`](#insn-00bb7b20)

~~~json
{
  "source": "00bb7b20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7b24`](#insn-00bb7b24)

~~~json
{
  "source": "00bb7b24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb7b28`](#insn-00bb7b28)

~~~json
{
  "source": "00bb7b28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
