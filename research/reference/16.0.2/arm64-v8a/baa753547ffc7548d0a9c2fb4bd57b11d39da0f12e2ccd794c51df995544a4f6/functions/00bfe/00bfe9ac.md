# 00bfe9ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfe910`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfe910.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-f5a3f60cfd1c6df2b5fd151844b46626)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bff9a0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bff9a0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-3aad40a159f1fdf987951255e39f4d67)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfe9ac",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_",
  "size": 100,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3edf5b601679214f4dddc088638730a102550e7244bff11003a452390bb6685a",
  "source_text_sha256": "3edf5b601679214f4dddc088638730a102550e7244bff11003a452390bb6685a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfe9ac",
        "00bfea0f"
      ]
    ],
    "bytes_sha256": "f34051f677b9c3aa26e72e78ca3782717b3223aa504f7cc522be785a55c13231",
    "instruction_count": 25,
    "instruction_bytes": 100,
    "body_bytes": 100,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c5e3f0](../00c5e/00c5e3f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 672 bytes

~~~c

void _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE4swapERS3_(long *param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  undefined4 uVar3;
  undefined4 uVar4;
  undefined8 uVar5;
  
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  lVar2 = (long)param_2 + *(long *)(*param_2 + -0x18);
  _ZNSt6__ndk18ios_base4swapERS0_(lVar1,lVar2);
  uVar5 = *(undefined8 *)(lVar1 + 0x88);
  uVar3 = *(undefined4 *)(lVar2 + 0x90);
  *(undefined8 *)(lVar1 + 0x88) = *(undefined8 *)(lVar2 + 0x88);
  uVar4 = *(undefined4 *)(lVar1 + 0x90);
  *(undefined8 *)(lVar2 + 0x88) = uVar5;
  *(undefined4 *)(lVar1 + 0x90) = uVar3;
  *(undefined4 *)(lVar2 + 0x90) = uVar4;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfe9ac"></a> `00bfe9ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfe9b0"></a> `00bfe9b0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bfe9b4"></a> `00bfe9b4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfe9b8"></a> `00bfe9b8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfe9bc"></a> `00bfe9bc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfe9c0"></a> `00bfe9c0` | `29 00 40 f9` | ldr x9,[x1] | `FALL_THROUGH`
<a id="insn-00bfe9c4"></a> `00bfe9c4` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfe9c8"></a> `00bfe9c8` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfe9cc"></a> `00bfe9cc` | `13 00 08 8b` | add x19,x0,x8 | `FALL_THROUGH`
<a id="insn-00bfe9d0"></a> `00bfe9d0` | `34 00 09 8b` | add x20,x1,x9 | `FALL_THROUGH`
<a id="insn-00bfe9d4"></a> `00bfe9d4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfe9d8"></a> `00bfe9d8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfe9dc"></a> `00bfe9dc` | `85 7e 01 94` | bl 0x00c5e3f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfe9e0"></a> `00bfe9e0` | `88 46 40 f9` | ldr x8,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00bfe9e4"></a> `00bfe9e4` | `69 46 40 f9` | ldr x9,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00bfe9e8"></a> `00bfe9e8` | `8a 92 40 b9` | ldr w10,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-00bfe9ec"></a> `00bfe9ec` | `68 46 00 f9` | str x8,[x19, #0x88] | `FALL_THROUGH`
<a id="insn-00bfe9f0"></a> `00bfe9f0` | `68 92 40 b9` | ldr w8,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00bfe9f4"></a> `00bfe9f4` | `89 46 00 f9` | str x9,[x20, #0x88] | `FALL_THROUGH`
<a id="insn-00bfe9f8"></a> `00bfe9f8` | `6a 92 00 b9` | str w10,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00bfe9fc"></a> `00bfe9fc` | `88 92 00 b9` | str w8,[x20, #0x90] | `FALL_THROUGH`
<a id="insn-00bfea00"></a> `00bfea00` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfea04"></a> `00bfea04` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bfea08"></a> `00bfea08` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfea0c"></a> `00bfea0c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfe9ac`](#insn-00bfe9ac) 範囲 `[['00bfe9ac', '00bfea0f']]`

## 命令位置別の参照

- [`00bfe9b0`](#insn-00bfe9b0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe9b4`](#insn-00bfe9b4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfe9dc`](#insn-00bfe9dc) → [`00c5e3f0`](../00c5e/00c5e3f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e3f0` · 推定シンボル `None` · 推定型 `None`
- [`00bfea00`](#insn-00bfea00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfea04`](#insn-00bfea04) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfe9b0`](#insn-00bfe9b0)

~~~json
{
  "source": "00bfe9b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe9b4`](#insn-00bfe9b4)

~~~json
{
  "source": "00bfe9b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfe9dc`](#insn-00bfe9dc)

~~~json
{
  "source": "00bfe9dc",
  "target": "00c5e3f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfea00`](#insn-00bfea00)

~~~json
{
  "source": "00bfea00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfea04`](#insn-00bfea04)

~~~json
{
  "source": "00bfea04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
