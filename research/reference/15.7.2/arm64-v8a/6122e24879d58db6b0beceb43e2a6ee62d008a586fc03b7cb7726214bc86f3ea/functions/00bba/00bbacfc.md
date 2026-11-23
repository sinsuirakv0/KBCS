# 00bbacfc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbadc4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbadc4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-b71d350f77db38cafd40d15b925aa9f4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbacfc",
  "name": "_ZNSt20bad_array_new_lengthC1Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6196d8070b1d6bc29ba5e69f10645f5e8986372285e0e91f25b63e127945297f",
  "source_text_sha256": "6196d8070b1d6bc29ba5e69f10645f5e8986372285e0e91f25b63e127945297f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbacfc",
        "00bbad13"
      ]
    ],
    "bytes_sha256": "dc425fe49f512fd76fd95e235619519eee6a8c8fde2d73c1bc675fd71cdaa14d",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdb0e0](../00bdb/00bdb0e0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 575 bytes

~~~c

void _ZNSt20bad_array_new_lengthC1Ev(long *param_1)

{
                    /* catch() { ... } // from try @ 00bb4c88 with catch @ 00bbad00 */
                    /* catch() { ... } // from try @ 00bb4ca0 with catch @ 00bbad04 */
                    /* catch() { ... } // from try @ 00bb48c0 with catch @ 00bbad08 */
                    /* catch() { ... } // from try @ 00bb48a8 with catch @ 00bbad0c */
  *param_1 = (long)(PTR__ZTVSt20bad_array_new_length_00c1bf20 + 0x10);
                    /* catch() { ... } // from try @ 00bb4500 with catch @ 00bbad10 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbacfc"></a> `00bbacfc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbad00"></a> `00bbad00` | `08 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbad04"></a> `00bbad04` | `08 91 47 f9` | ldr x8,[x8, #0xf20] | `FALL_THROUGH`
<a id="insn-00bbad08"></a> `00bbad08` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbad0c"></a> `00bbad0c` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbad10"></a> `00bbad10` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbacfc`](#insn-00bbacfc) 範囲 `[['00bbacfc', '00bbacff']]`
  - `FALL_THROUGH` [`00bbacfc`](#insn-00bbacfc) → [`00bbad00`](#insn-00bbad00)
- ブロック [`00bbad00`](#insn-00bbad00) 範囲 `[['00bbad00', '00bbad03']]`
  - `FALL_THROUGH` [`00bbad00`](#insn-00bbad00) → [`00bbad04`](#insn-00bbad04)
- ブロック [`00bbad04`](#insn-00bbad04) 範囲 `[['00bbad04', '00bbad07']]`
  - `FALL_THROUGH` [`00bbad04`](#insn-00bbad04) → [`00bbad08`](#insn-00bbad08)
- ブロック [`00bbad08`](#insn-00bbad08) 範囲 `[['00bbad08', '00bbad0b']]`
  - `FALL_THROUGH` [`00bbad08`](#insn-00bbad08) → [`00bbad0c`](#insn-00bbad0c)
- ブロック [`00bbad0c`](#insn-00bbad0c) 範囲 `[['00bbad0c', '00bbad0f']]`
  - `FALL_THROUGH` [`00bbad0c`](#insn-00bbad0c) → [`00bbad10`](#insn-00bbad10)
- ブロック [`00bbad10`](#insn-00bbad10) 範囲 `[['00bbad10', '00bbad13']]`

## 命令位置別の参照

- [`00bbad04`](#insn-00bbad04) → `00c1bf20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbad0c`](#insn-00bbad0c) → `00c16760`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbad04`](#insn-00bbad04)

~~~json
{
  "source": "00bbad04",
  "target": "00c1bf20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf20",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbad0c`](#insn-00bbad0c)

~~~json
{
  "source": "00bbad0c",
  "target": "00c16760",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16750",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
