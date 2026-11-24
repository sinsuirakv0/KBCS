# 00befab0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bef688`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bef/00bef688.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0039.md#compare-0d577db7ffbe559d04c97246427bd82f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00befb4c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bef/00befb4c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0040.md#compare-263d816a7f0177b15b6e1057f9e24e27)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00befab0",
  "name": "_ZNSt13exception_ptraSERKS_",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6a4f2b6986ae6b3efb7483c629be87c5306bc0480dbf480a3c7b17005fe96bd8",
  "source_text_sha256": "6a4f2b6986ae6b3efb7483c629be87c5306bc0480dbf480a3c7b17005fe96bd8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00befab0",
        "00befaff"
      ]
    ],
    "bytes_sha256": "841d7d27c52e920ab2f95be95a76889bf699a2f89c61ea4d3b6d55dbdd9e3280",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5df30](../00c5d/00c5df30.md)

## 呼び出し先

- [00c5df10](../00c5d/00c5df10.md)
- [00c5df20](../00c5d/00c5df20.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 240 bytes

~~~c

long * _ZNSt13exception_ptraSERKS_(long *param_1,long *param_2)

{
  if (*param_1 != *param_2) {
    __cxa_increment_exception_refcount();
    __cxa_decrement_exception_refcount(*param_1);
    *param_1 = *param_2;
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00befab0"></a> `00befab0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00befab4"></a> `00befab4` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00befab8"></a> `00befab8` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befabc"></a> `00befabc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00befac0"></a> `00befac0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00befac4"></a> `00befac4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00befac8"></a> `00befac8` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00befacc"></a> `00befacc` | `1f 01 00 eb` | cmp x8,x0 | `FALL_THROUGH`
<a id="insn-00befad0"></a> `00befad0` | `e0 00 00 54` | b.eq 0x00befaec | `CONDITIONAL_JUMP`
<a id="insn-00befad4"></a> `00befad4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00befad8"></a> `00befad8` | `12 b9 01 94` | bl 0x00c5df20 | `UNCONDITIONAL_CALL`
<a id="insn-00befadc"></a> `00befadc` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00befae0"></a> `00befae0` | `0c b9 01 94` | bl 0x00c5df10 | `UNCONDITIONAL_CALL`
<a id="insn-00befae4"></a> `00befae4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00befae8"></a> `00befae8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00befaec"></a> `00befaec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00befaf0"></a> `00befaf0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00befaf4"></a> `00befaf4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00befaf8"></a> `00befaf8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00befafc"></a> `00befafc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00befab0`](#insn-00befab0) 範囲 `[['00befab0', '00befad3']]`
  - `CONDITIONAL_JUMP` [`00befad0`](#insn-00befad0) → [`00befaec`](#insn-00befaec)
  - `FALL_THROUGH` [`00befad0`](#insn-00befad0) → [`00befad4`](#insn-00befad4)
- ブロック [`00befad4`](#insn-00befad4) 範囲 `[['00befad4', '00befaeb']]`
  - `FALL_THROUGH` [`00befae8`](#insn-00befae8) → [`00befaec`](#insn-00befaec)
- ブロック [`00befaec`](#insn-00befaec) 範囲 `[['00befaec', '00befaff']]`

## 命令位置別の参照

- [`00befab4`](#insn-00befab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befab8`](#insn-00befab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befad0`](#insn-00befad0) → [`00befaec`](#insn-00befaec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befad8`](#insn-00befad8) → [`00c5df20`](../00c5d/00c5df20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5df20` · 推定シンボル `None` · 推定型 `None`
- [`00befae0`](#insn-00befae0) → [`00c5df10`](../00c5d/00c5df10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5df10` · 推定シンボル `None` · 推定型 `None`
- [`00befaf0`](#insn-00befaf0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00befaf4`](#insn-00befaf4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00befab4`](#insn-00befab4)

~~~json
{
  "source": "00befab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befab8`](#insn-00befab8)

~~~json
{
  "source": "00befab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befad0`](#insn-00befad0)

~~~json
{
  "source": "00befad0",
  "target": "00befaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befad8`](#insn-00befad8)

~~~json
{
  "source": "00befad8",
  "target": "00c5df20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befae0`](#insn-00befae0)

~~~json
{
  "source": "00befae0",
  "target": "00c5df10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00befaf0`](#insn-00befaf0)

~~~json
{
  "source": "00befaf0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00befaf4`](#insn-00befaf4)

~~~json
{
  "source": "00befaf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
