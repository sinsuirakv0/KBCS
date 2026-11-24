# 00bde2ac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bdde84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bdd/00bdde84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/no_difference_in_scope-0013.md#compare-4c0719b819124ed0320ef38e134c2b2b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bde348`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bde/00bde348.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/no_difference_in_scope-0013.md#compare-48cfb6ade89d8f764030416beeba5215)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bde2ac",
  "name": "_ZNK8firebase4auth4User8is_validEv",
  "size": 32,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6fd6b615520bf22e6337b7f1c1f35d308921f20a39fcc03aeabadc0b2a6b79f0",
  "source_text_sha256": "6fd6b615520bf22e6337b7f1c1f35d308921f20a39fcc03aeabadc0b2a6b79f0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bde2ac",
        "00bde2cb"
      ]
    ],
    "bytes_sha256": "2e32fe1a840a5bcafb48f453c262822f6868339600f07bb2eff95e31d315a31d",
    "instruction_count": 8,
    "instruction_bytes": 32,
    "body_bytes": 32,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5aa60](../00c5a/00c5aa60.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 183 bytes

~~~c

bool _ZNK8firebase4auth4User8is_validEv(long param_1)

{
  if (*(long *)(param_1 + 0x98) != 0) {
    return *(long *)(*(long *)(param_1 + 0x98) + 0x200) != 0;
  }
  return false;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bde2ac"></a> `00bde2ac` | `08 4c 40 f9` | ldr x8,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00bde2b0"></a> `00bde2b0` | `a8 00 00 b4` | cbz x8,0x00bde2c4 | `CONDITIONAL_JUMP`
<a id="insn-00bde2b4"></a> `00bde2b4` | `08 01 41 f9` | ldr x8,[x8, #0x200] | `FALL_THROUGH`
<a id="insn-00bde2b8"></a> `00bde2b8` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bde2bc"></a> `00bde2bc` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bde2c0"></a> `00bde2c0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bde2c4"></a> `00bde2c4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bde2c8"></a> `00bde2c8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bde2ac`](#insn-00bde2ac) 範囲 `[['00bde2ac', '00bde2b3']]`
  - `CONDITIONAL_JUMP` [`00bde2b0`](#insn-00bde2b0) → [`00bde2c4`](#insn-00bde2c4)
  - `FALL_THROUGH` [`00bde2b0`](#insn-00bde2b0) → [`00bde2b4`](#insn-00bde2b4)
- ブロック [`00bde2b4`](#insn-00bde2b4) 範囲 `[['00bde2b4', '00bde2c3']]`
- ブロック [`00bde2c4`](#insn-00bde2c4) 範囲 `[['00bde2c4', '00bde2cb']]`

## 命令位置別の参照

- [`00bde2b0`](#insn-00bde2b0) → [`00bde2c4`](#insn-00bde2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bde2b0`](#insn-00bde2b0)

~~~json
{
  "source": "00bde2b0",
  "target": "00bde2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
