# 00bda7ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bda710`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda710.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0039.md#compare-69258b05a5d3918e5277c5a92473c853)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdb7a0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb7a0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-e07d4cfa9d68599085d2427b1d5c2f3f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bda7ac",
  "name": "_ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC1ERKS2_",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8461a732894340cba5f93a8ee5041f79c84087c0df4d80f95179447bdb5d5cee",
  "source_text_sha256": "8461a732894340cba5f93a8ee5041f79c84087c0df4d80f95179447bdb5d5cee",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bda7ac",
        "00bda7e3"
      ]
    ],
    "bytes_sha256": "2d57e7f0c3fc4e9260ad18ce3abbd3bef687b4e072b8d6ab6be35fa50839ee37",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57f60](../00c57/00c57f60.md)
- [00c5df10](../00c5d/00c5df10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 337 bytes

~~~c

void _ZN8firebase4auth17PhoneAuthProvider19ForceResendingTokenC1ERKS2_
               (undefined8 *param_1,undefined8 *param_2)

{
  undefined8 *puVar1;
  
  puVar1 = (undefined8 *)_Znwm(8);
  *puVar1 = 0;
  *param_1 = puVar1;
  _ZN8firebase4auth23ForceResendingTokenData6SetRefEP8_jobject(puVar1,*(undefined8 *)*param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bda7ac"></a> `00bda7ac` | `f4 4f be a9` | stp x20,x19,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bda7b0"></a> `00bda7b0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda7b4"></a> `00bda7b4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bda7b8"></a> `00bda7b8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bda7bc"></a> `00bda7bc` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00bda7c0"></a> `00bda7c0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bda7c4"></a> `00bda7c4` | `e7 f5 01 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bda7c8"></a> `00bda7c8` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bda7cc"></a> `00bda7cc` | `80 02 00 f9` | str x0,[x20] | `FALL_THROUGH`
<a id="insn-00bda7d0"></a> `00bda7d0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bda7d4"></a> `00bda7d4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda7d8"></a> `00bda7d8` | `01 01 40 f9` | ldr x1,[x8] | `FALL_THROUGH`
<a id="insn-00bda7dc"></a> `00bda7dc` | `f4 4f c2 a8` | ldp x20,x19,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bda7e0"></a> `00bda7e0` | `cc 0d 02 14` | b 0x00c5df10 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bda7ac`](#insn-00bda7ac) 範囲 `[['00bda7ac', '00bda7e3']]`

## 命令位置別の参照

- [`00bda7ac`](#insn-00bda7ac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7b0`](#insn-00bda7b0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7c4`](#insn-00bda7c4) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bda7d4`](#insn-00bda7d4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda7e0`](#insn-00bda7e0) → [`00c5df10`](../00c5d/00c5df10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5df10` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bda7ac`](#insn-00bda7ac)

~~~json
{
  "source": "00bda7ac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7b0`](#insn-00bda7b0)

~~~json
{
  "source": "00bda7b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7c4`](#insn-00bda7c4)

~~~json
{
  "source": "00bda7c4",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda7d4`](#insn-00bda7d4)

~~~json
{
  "source": "00bda7d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda7e0`](#insn-00bda7e0)

~~~json
{
  "source": "00bda7e0",
  "target": "00c5df10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
