# 00bafa1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00baf954`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00baf/00baf954.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0024.md#compare-4ca1e1289fec89ef001cca143eed990c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bafa60`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00baf/00bafa60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/detail_skipped-0023.md#compare-3ad2faba641b2b4677980ec5d3b3a815)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bafa1c",
  "name": "_ZNSt6__ndk114__num_get_base10__get_baseERNS_8ios_baseE",
  "size": 68,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c0d4b8c48462c2023c559e49b874327904d4646fc23798d600e2d25ca9b3cf01",
  "source_text_sha256": "c0d4b8c48462c2023c559e49b874327904d4646fc23798d600e2d25ca9b3cf01",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bafa1c",
        "00bafa5f"
      ]
    ],
    "bytes_sha256": "828c2ed23295576df44223495bcf4e634e480e5b2e4e57653e238c65c1ef14cf",
    "instruction_count": 17,
    "instruction_bytes": 68,
    "body_bytes": 68,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 285 bytes

~~~c

undefined8 _ZNSt6__ndk114__num_get_base10__get_baseERNS_8ios_baseE(long param_1)

{
  uint uVar1;
  
  uVar1 = *(uint *)(param_1 + 8) & 0x4a;
  if (uVar1 == 0) {
    return 0;
  }
  if (uVar1 != 0x40) {
    if (uVar1 == 8) {
      return 0x10;
    }
    return 10;
  }
  return 8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bafa1c"></a> `00bafa1c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bafa20"></a> `00bafa20` | `08 08 40 b9` | ldr w8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bafa24"></a> `00bafa24` | `49 09 80 52` | mov w9,#0x4a | `FALL_THROUGH`
<a id="insn-00bafa28"></a> `00bafa28` | `08 01 09 6a` | ands w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00bafa2c"></a> `00bafa2c` | `20 01 00 54` | b.eq 0x00bafa50 | `CONDITIONAL_JUMP`
<a id="insn-00bafa30"></a> `00bafa30` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bafa34"></a> `00bafa34` | `a0 00 00 54` | b.eq 0x00bafa48 | `CONDITIONAL_JUMP`
<a id="insn-00bafa38"></a> `00bafa38` | `1f 21 00 71` | cmp w8,#0x8 | `FALL_THROUGH`
<a id="insn-00bafa3c"></a> `00bafa3c` | `e1 00 00 54` | b.ne 0x00bafa58 | `CONDITIONAL_JUMP`
<a id="insn-00bafa40"></a> `00bafa40` | `00 02 80 52` | mov w0,#0x10 | `FALL_THROUGH`
<a id="insn-00bafa44"></a> `00bafa44` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bafa48"></a> `00bafa48` | `00 01 80 52` | mov w0,#0x8 | `FALL_THROUGH`
<a id="insn-00bafa4c"></a> `00bafa4c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bafa50"></a> `00bafa50` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bafa54"></a> `00bafa54` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bafa58"></a> `00bafa58` | `40 01 80 52` | mov w0,#0xa | `FALL_THROUGH`
<a id="insn-00bafa5c"></a> `00bafa5c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bafa1c`](#insn-00bafa1c) 範囲 `[['00bafa1c', '00bafa2f']]`
  - `CONDITIONAL_JUMP` [`00bafa2c`](#insn-00bafa2c) → [`00bafa50`](#insn-00bafa50)
  - `FALL_THROUGH` [`00bafa2c`](#insn-00bafa2c) → [`00bafa30`](#insn-00bafa30)
- ブロック [`00bafa30`](#insn-00bafa30) 範囲 `[['00bafa30', '00bafa37']]`
  - `CONDITIONAL_JUMP` [`00bafa34`](#insn-00bafa34) → [`00bafa48`](#insn-00bafa48)
  - `FALL_THROUGH` [`00bafa34`](#insn-00bafa34) → [`00bafa38`](#insn-00bafa38)
- ブロック [`00bafa38`](#insn-00bafa38) 範囲 `[['00bafa38', '00bafa3f']]`
  - `CONDITIONAL_JUMP` [`00bafa3c`](#insn-00bafa3c) → [`00bafa58`](#insn-00bafa58)
  - `FALL_THROUGH` [`00bafa3c`](#insn-00bafa3c) → [`00bafa40`](#insn-00bafa40)
- ブロック [`00bafa40`](#insn-00bafa40) 範囲 `[['00bafa40', '00bafa47']]`
- ブロック [`00bafa48`](#insn-00bafa48) 範囲 `[['00bafa48', '00bafa4f']]`
- ブロック [`00bafa50`](#insn-00bafa50) 範囲 `[['00bafa50', '00bafa57']]`
- ブロック [`00bafa58`](#insn-00bafa58) 範囲 `[['00bafa58', '00bafa5f']]`

## 命令位置別の参照

- [`00bafa2c`](#insn-00bafa2c) → [`00bafa50`](#insn-00bafa50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafa34`](#insn-00bafa34) → [`00bafa48`](#insn-00bafa48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bafa3c`](#insn-00bafa3c) → [`00bafa58`](#insn-00bafa58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bafa2c`](#insn-00bafa2c)

~~~json
{
  "source": "00bafa2c",
  "target": "00bafa50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafa34`](#insn-00bafa34)

~~~json
{
  "source": "00bafa34",
  "target": "00bafa48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bafa3c`](#insn-00bafa3c)

~~~json
{
  "source": "00bafa3c",
  "target": "00bafa58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
