# 00bdbae0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdba30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdba30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-526166dddfe9e3576166e8e4f61775b9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbb30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-d52356d8358c9ab36089656894d2dea8)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbae0",
  "name": "_ZN5Botan12ucs2_to_utf8EPKhm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3aa9fe8b71afdf07641a9d2c0189ce59341f5a36b16ea3108b586dd9250d9dbb",
  "source_text_sha256": "3aa9fe8b71afdf07641a9d2c0189ce59341f5a36b16ea3108b586dd9250d9dbb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbae0",
        "00bdbaef"
      ]
    ],
    "bytes_sha256": "dec2edb3e2944a1000d05b69a05a7a14224132b5c1660ff0d16b2535350a26f7",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048a89c](../0048a/0048a89c.md)

## 呼び出し先

- [0048aad4](../0048a/0048aad4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 115 bytes

~~~c

void _ZN5Botan12ucs2_to_utf8EPKhm(void)

{
  (*(code *)PTR__ZN5Botan12ucs2_to_utf8EPKhm_00c1c600)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbae0"></a> `00bdbae0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbae4"></a> `00bdbae4` | `11 02 43 f9` | ldr x17,[x16, #0x600] | `FALL_THROUGH`
<a id="insn-00bdbae8"></a> `00bdbae8` | `10 02 18 91` | add x16,x16,#0x600 | `FALL_THROUGH`
<a id="insn-00bdbaec"></a> `00bdbaec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbae0`](#insn-00bdbae0) 範囲 `[['00bdbae0', '00bdbaef']]`

## 命令位置別の参照

- [`00bdbae4`](#insn-00bdbae4) → `00c1c600`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbaec`](#insn-00bdbaec) → [`0048aad4`](../0048a/0048aad4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048aad4` · 推定シンボル `_ZN5Botan12ucs2_to_utf8EPKhm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbae4`](#insn-00bdbae4)

~~~json
{
  "source": "00bdbae4",
  "target": "00c1c600",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c600",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbaec`](#insn-00bdbaec)

~~~json
{
  "source": "00bdbaec",
  "target": "0048aad4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
