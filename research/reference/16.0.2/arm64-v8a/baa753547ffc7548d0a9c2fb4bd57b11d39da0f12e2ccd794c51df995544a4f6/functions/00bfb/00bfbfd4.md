# 00bfbfd4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfbf38`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfbf38.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-62f7a11f46a8035445f45ad2ad18436f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfcfc8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfcfc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-eda56d0b1c394a09d6471b3212c72753)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbfd4",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_",
  "size": 80,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "87721279f401cc3a527012c9eef0116bd99202df3f17decd80635b1e801ceeb9",
  "source_text_sha256": "87721279f401cc3a527012c9eef0116bd99202df3f17decd80635b1e801ceeb9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbfd4",
        "00bfc023"
      ]
    ],
    "bytes_sha256": "4ee7667012b091fe0e9a59b4cdf810bc99ea50a227ad4317b76f9cc6899f82b3",
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

- [00c5e3b0](../00c5e/00c5e3b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 662 bytes

~~~c

long _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEaSERKS3_(long param_1,long param_2)

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
<a id="insn-00bfbfd4"></a> `00bfbfd4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfbfd8"></a> `00bfbfd8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfbfdc"></a> `00bfbfdc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbfe0"></a> `00bfbfe0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfbfe4"></a> `00bfbfe4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bfbfe8"></a> `00bfbfe8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfbfec"></a> `00bfbfec` | `00 20 00 91` | add x0,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bfbff0"></a> `00bfbff0` | `21 20 00 91` | add x1,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bfbff4"></a> `00bfbff4` | `ef 88 01 94` | bl 0x00c5e3b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfbff8"></a> `00bfbff8` | `60 06 c0 3d` | ldr q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bfbffc"></a> `00bfbffc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfc000"></a> `00bfc000` | `80 06 80 3d` | str q0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bfc004"></a> `00bfc004` | `60 0a c0 3d` | ldr q0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc008"></a> `00bfc008` | `80 0a 80 3d` | str q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc00c"></a> `00bfc00c` | `60 0e c0 3d` | ldr q0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bfc010"></a> `00bfc010` | `80 0e 80 3d` | str q0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bfc014"></a> `00bfc014` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfc018"></a> `00bfc018` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfc01c"></a> `00bfc01c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfc020"></a> `00bfc020` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbfd4`](#insn-00bfbfd4) 範囲 `[['00bfbfd4', '00bfc023']]`

## 命令位置別の参照

- [`00bfbfd8`](#insn-00bfbfd8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbfdc`](#insn-00bfbfdc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfbff4`](#insn-00bfbff4) → [`00c5e3b0`](../00c5e/00c5e3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e3b0` · 推定シンボル `None` · 推定型 `None`
- [`00bfc014`](#insn-00bfc014) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc018`](#insn-00bfc018) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfbfd8`](#insn-00bfbfd8)

~~~json
{
  "source": "00bfbfd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbfdc`](#insn-00bfbfdc)

~~~json
{
  "source": "00bfbfdc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfbff4`](#insn-00bfbff4)

~~~json
{
  "source": "00bfbff4",
  "target": "00c5e3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfc014`](#insn-00bfc014)

~~~json
{
  "source": "00bfc014",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc018`](#insn-00bfc018)

~~~json
{
  "source": "00bfc018",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
