# 00a6acac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a6ac3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a6a/00a6ac3c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0034.md#compare-078e701a844d7ab81da7ca312636cb69)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00a6bca0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a6b/00a6bca0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0027.md#compare-988227c55cc2ada6df5d661d7b50bc90)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a6acac",
  "name": "FUN_00a6acac",
  "size": 44,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c43e35222444f9898d40f3c5777f9985a8c0f5d1a9a92430044818e368ee3929",
  "source_text_sha256": "c43e35222444f9898d40f3c5777f9985a8c0f5d1a9a92430044818e368ee3929",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a6acac",
        "00a6acd7"
      ]
    ],
    "bytes_sha256": "7212e6b69f07aa93c98612143f45162f0ec3e2195ab3a1deb49065ee9175c28f",
    "instruction_count": 11,
    "instruction_bytes": 44,
    "body_bytes": 44,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [007ccf44](../007cc/007ccf44.md)
- [009d7bd0](../009d7/009d7bd0.md)
- [00a47f54](../00a47/00a47f54.md)

## 呼び出し先

- [005e08f0](../005e0/005e08f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 230 bytes

~~~c

void FUN_00a6acac(long param_1,undefined4 param_2)

{
  uint uVar1;
  
  *(undefined4 *)(param_1 + 0x7c) = param_2;
  uVar1 = FUN_005e08f0();
  *(uint *)(param_1 + 0x84) = uVar1 & ((int)uVar1 >> 0x1f ^ 0xffffffffU);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a6acac"></a> `00a6acac` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a6acb0"></a> `00a6acb0` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6acb4"></a> `00a6acb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a6acb8"></a> `00a6acb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a6acbc"></a> `00a6acbc` | `01 7c 00 b9` | str w1,[x0, #0x7c] | `FALL_THROUGH`
<a id="insn-00a6acc0"></a> `00a6acc0` | `0c d7 ed 97` | bl 0x005e08f0 | `UNCONDITIONAL_CALL`
<a id="insn-00a6acc4"></a> `00a6acc4` | `08 7c a0 0a` | bic w8,w0,w0, ASR #0x1f | `FALL_THROUGH`
<a id="insn-00a6acc8"></a> `00a6acc8` | `68 86 00 b9` | str w8,[x19, #0x84] | `FALL_THROUGH`
<a id="insn-00a6accc"></a> `00a6accc` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a6acd0"></a> `00a6acd0` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a6acd4"></a> `00a6acd4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a6acac`](#insn-00a6acac) 範囲 `[['00a6acac', '00a6acd7']]`

## 命令位置別の参照

- [`00a6acac`](#insn-00a6acac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6acb0`](#insn-00a6acb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6acc0`](#insn-00a6acc0) → [`005e08f0`](../005e0/005e08f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e08f0` · 推定シンボル `None` · 推定型 `None`
- [`00a6accc`](#insn-00a6accc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a6acd0`](#insn-00a6acd0) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a6acac`](#insn-00a6acac)

~~~json
{
  "source": "00a6acac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6acb0`](#insn-00a6acb0)

~~~json
{
  "source": "00a6acb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6acc0`](#insn-00a6acc0)

~~~json
{
  "source": "00a6acc0",
  "target": "005e08f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a6accc`](#insn-00a6accc)

~~~json
{
  "source": "00a6accc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a6acd0`](#insn-00a6acd0)

~~~json
{
  "source": "00a6acd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
