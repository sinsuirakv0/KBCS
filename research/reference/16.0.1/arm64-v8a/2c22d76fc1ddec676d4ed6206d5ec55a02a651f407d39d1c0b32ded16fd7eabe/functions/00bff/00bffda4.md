# 00bffda4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bff97c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bff/00bff97c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-b5c23849e7f2c8b2d96230faf4fc4a77)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bffe40`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bffe40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0042.md#compare-b5d1f72c69485fe3caf4079bc5c9fe1f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffda4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEaSERKS3_",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1338ed022f3c25442f31437bf8378aef620ea83f4a08f5b98136f3ce0f7dab10",
  "source_text_sha256": "1338ed022f3c25442f31437bf8378aef620ea83f4a08f5b98136f3ce0f7dab10",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffda4",
        "00bffdf3"
      ]
    ],
    "bytes_sha256": "43b57d8d44f1c4d4ab92601ecca07ce24b0f5425c72832a12521425ebe0aaeb5",
    "instruction_count": 20,
    "instruction_bytes": 80,
    "body_bytes": 80,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5e2e0](../00c5e/00c5e2e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 662 bytes

~~~c

long _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEEaSERKS3_(long param_1,long param_2)

{
  undefined8 uVar1;
  
  _ZNSt6__ndk16localeaSERKS0_(param_1 + 8,param_2 + 8);
  uVar1 = *(undefined8 *)(param_2 + 0x10);
  *(undefined8 *)(param_1 + 0x18) = *(undefined8 *)(param_2 + 0x18);
  *(undefined8 *)(param_1 + 0x10) = uVar1;
  uVar1 = *(undefined8 *)(param_2 + 0x20);
  *(undefined8 *)(param_1 + 0x28) = *(undefined8 *)(param_2 + 0x28);
  *(undefined8 *)(param_1 + 0x20) = uVar1;
  uVar1 = *(undefined8 *)(param_2 + 0x30);
  *(undefined8 *)(param_1 + 0x38) = *(undefined8 *)(param_2 + 0x38);
  *(undefined8 *)(param_1 + 0x30) = uVar1;
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffda4"></a> `00bffda4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bffda8"></a> `00bffda8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bffdac"></a> `00bffdac` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffdb0"></a> `00bffdb0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bffdb4"></a> `00bffdb4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bffdb8"></a> `00bffdb8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bffdbc"></a> `00bffdbc` | `00 20 00 91` | add x0,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bffdc0"></a> `00bffdc0` | `21 20 00 91` | add x1,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bffdc4"></a> `00bffdc4` | `47 79 01 94` | bl 0x00c5e2e0 | `UNCONDITIONAL_CALL`
<a id="insn-00bffdc8"></a> `00bffdc8` | `60 06 c0 3d` | ldr q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bffdcc"></a> `00bffdcc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bffdd0"></a> `00bffdd0` | `80 06 80 3d` | str q0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bffdd4"></a> `00bffdd4` | `60 0a c0 3d` | ldr q0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bffdd8"></a> `00bffdd8` | `80 0a 80 3d` | str q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bffddc"></a> `00bffddc` | `60 0e c0 3d` | ldr q0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bffde0"></a> `00bffde0` | `80 0e 80 3d` | str q0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bffde4"></a> `00bffde4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bffde8"></a> `00bffde8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bffdec"></a> `00bffdec` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bffdf0"></a> `00bffdf0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffda4`](#insn-00bffda4) 範囲 `[['00bffda4', '00bffdf3']]`

## 命令位置別の参照

- [`00bffda8`](#insn-00bffda8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffdac`](#insn-00bffdac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffdc4`](#insn-00bffdc4) → [`00c5e2e0`](../00c5e/00c5e2e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e2e0` · 推定シンボル `None` · 推定型 `None`
- [`00bffde4`](#insn-00bffde4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffde8`](#insn-00bffde8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffda8`](#insn-00bffda8)

~~~json
{
  "source": "00bffda8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffdac`](#insn-00bffdac)

~~~json
{
  "source": "00bffdac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffdc4`](#insn-00bffdc4)

~~~json
{
  "source": "00bffdc4",
  "target": "00c5e2e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffde4`](#insn-00bffde4)

~~~json
{
  "source": "00bffde4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffde8`](#insn-00bffde8)

~~~json
{
  "source": "00bffde8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
