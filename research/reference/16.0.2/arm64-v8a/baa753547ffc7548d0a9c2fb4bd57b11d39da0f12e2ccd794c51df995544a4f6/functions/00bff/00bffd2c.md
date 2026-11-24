# 00bffd2c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffc90`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffc90.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/reference_unresolved-0001.md#compare-ec3a3ec267c1215f4948e64ba189d357)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c00d20`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00d20.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/reference_unresolved-0001.md#compare-33091119010c6f9f3c6abe24c9609c32)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffd2c",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE7sungetcEv",
  "size": 52,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3c7e3fa38c5cdaf0eb2045217860649a6a39ad8d962f37f3f0d6bdc66f92cec",
  "source_text_sha256": "d3c7e3fa38c5cdaf0eb2045217860649a6a39ad8d962f37f3f0d6bdc66f92cec",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffd2c",
        "00bffd5f"
      ]
    ],
    "bytes_sha256": "635ef541483e81fb4a78133e6405dee6087ceeb19399c77c0b6e75bc17d3b24c",
    "instruction_count": 13,
    "instruction_bytes": 52,
    "body_bytes": 52,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 534 bytes

~~~c

ulong _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE7sungetcEv(long *param_1)

{
  uint uVar1;
  ulong uVar2;
  uint *puVar3;
  
  if (param_1[2] != param_1[3]) {
    puVar3 = (uint *)(param_1[3] + -4);
    uVar1 = *puVar3;
    param_1[3] = (long)puVar3;
    return (ulong)uVar1;
  }
                    /* WARNING: Could not recover jumptable at 0x00bffd5c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  uVar2 = (**(code **)(*param_1 + 0x58))(param_1,0xffffffff);
  return uVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffd2c"></a> `00bffd2c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bffd30"></a> `00bffd30` | `0a 24 41 a9` | ldp x10,x9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bffd34"></a> `00bffd34` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bffd38"></a> `00bffd38` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bffd3c"></a> `00bffd3c` | `80 00 00 54` | b.eq 0x00bffd4c | `CONDITIONAL_JUMP`
<a id="insn-00bffd40"></a> `00bffd40` | `20 cd 5f b8` | ldr w0,[x9, #-0x4]! | `FALL_THROUGH`
<a id="insn-00bffd44"></a> `00bffd44` | `09 0d 00 f9` | str x9,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bffd48"></a> `00bffd48` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bffd4c"></a> `00bffd4c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00bffd50"></a> `00bffd50` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bffd54"></a> `00bffd54` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bffd58"></a> `00bffd58` | `30 2d 40 f9` | ldr x16,[x9, #0x58] | `FALL_THROUGH`
<a id="insn-00bffd5c"></a> `00bffd5c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bffd2c`](#insn-00bffd2c) 範囲 `[['00bffd2c', '00bffd3f']]`
  - `CONDITIONAL_JUMP` [`00bffd3c`](#insn-00bffd3c) → [`00bffd4c`](#insn-00bffd4c)
  - `FALL_THROUGH` [`00bffd3c`](#insn-00bffd3c) → [`00bffd40`](#insn-00bffd40)
- ブロック [`00bffd40`](#insn-00bffd40) 範囲 `[['00bffd40', '00bffd4b']]`
- ブロック [`00bffd4c`](#insn-00bffd4c) 範囲 `[['00bffd4c', '00bffd5f']]`

## 命令位置別の参照

- [`00bffd3c`](#insn-00bffd3c) → [`00bffd4c`](#insn-00bffd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffd3c`](#insn-00bffd3c)

~~~json
{
  "source": "00bffd3c",
  "target": "00bffd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
