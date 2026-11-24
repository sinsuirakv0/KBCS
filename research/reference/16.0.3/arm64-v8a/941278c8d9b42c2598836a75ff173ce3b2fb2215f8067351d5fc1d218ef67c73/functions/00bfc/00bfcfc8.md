# 00bfcfc8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfbfd4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfb/00bfbfd4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-eda56d0b1c394a09d6471b3212c72753)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfcfc8",
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
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfcfc8",
        "00bfd017"
      ]
    ],
    "bytes_sha256": "101f7a384fd0293e6e136a69c488cfb47916e81ca778fc66fe59646adfe18c49",
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

- [00c5f380](../00c5f/00c5f380.md)

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
<a id="insn-00bfcfc8"></a> `00bfcfc8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfcfcc"></a> `00bfcfcc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfcfd0"></a> `00bfcfd0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcfd4"></a> `00bfcfd4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfcfd8"></a> `00bfcfd8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bfcfdc"></a> `00bfcfdc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfcfe0"></a> `00bfcfe0` | `00 20 00 91` | add x0,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcfe4"></a> `00bfcfe4` | `21 20 00 91` | add x1,x1,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcfe8"></a> `00bfcfe8` | `e6 88 01 94` | bl 0x00c5f380 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcfec"></a> `00bfcfec` | `60 06 c0 3d` | ldr q0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcff0"></a> `00bfcff0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfcff4"></a> `00bfcff4` | `80 06 80 3d` | str q0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcff8"></a> `00bfcff8` | `60 0a c0 3d` | ldr q0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcffc"></a> `00bfcffc` | `80 0a 80 3d` | str q0,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bfd000"></a> `00bfd000` | `60 0e c0 3d` | ldr q0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bfd004"></a> `00bfd004` | `80 0e 80 3d` | str q0,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bfd008"></a> `00bfd008` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfd00c"></a> `00bfd00c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfd010"></a> `00bfd010` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfd014"></a> `00bfd014` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfcfc8`](#insn-00bfcfc8) 範囲 `[['00bfcfc8', '00bfd017']]`

## 命令位置別の参照

- [`00bfcfcc`](#insn-00bfcfcc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcfd0`](#insn-00bfcfd0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcfe8`](#insn-00bfcfe8) → [`00c5f380`](../00c5f/00c5f380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f380` · 推定シンボル `None` · 推定型 `None`
- [`00bfd008`](#insn-00bfd008) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd00c`](#insn-00bfd00c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfcfcc`](#insn-00bfcfcc)

~~~json
{
  "source": "00bfcfcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcfd0`](#insn-00bfcfd0)

~~~json
{
  "source": "00bfcfd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcfe8`](#insn-00bfcfe8)

~~~json
{
  "source": "00bfcfe8",
  "target": "00c5f380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfd008`](#insn-00bfd008)

~~~json
{
  "source": "00bfd008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd00c`](#insn-00bfd00c)

~~~json
{
  "source": "00bfd00c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
