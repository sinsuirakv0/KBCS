# 00bdece0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdec30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdec30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-2440594b160425342ef39e8c435dabca)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bded30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bded30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-3d078964433b06b1034b9778e18f8c17)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdece0",
  "name": "_ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "99e6fa8a7839e46f5e2f8a6a896d23358dc711510588c71321b7024968f39caa",
  "source_text_sha256": "99e6fa8a7839e46f5e2f8a6a896d23358dc711510588c71321b7024968f39caa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdece0",
        "00bdecef"
      ]
    ],
    "bytes_sha256": "73b9fa6e5fc653b06bddf7a7e84ddd72c86f013aeb95deb7947b8ec85fb5ffe7",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afceb8](../00afc/00afceb8.md)
- [00afd0c4](../00afd/00afd0c4.md)
- [00afd1f8](../00afd/00afd1f8.md)
- [00afd448](../00afd/00afd448.md)
- [00afd50c](../00afd/00afd50c.md)
- [00afdb2c](../00afd/00afdb2c.md)
- [00afdc04](../00afd/00afdc04.md)

## 呼び出し先

- [00afced4](../00afc/00afced4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 293 bytes

~~~c

void _ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
               (void)

{
  (*(code *)
    PTR__ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE_00c1df00
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdece0"></a> `00bdece0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdece4"></a> `00bdece4` | `11 82 47 f9` | ldr x17,[x16, #0xf00] | `FALL_THROUGH`
<a id="insn-00bdece8"></a> `00bdece8` | `10 02 3c 91` | add x16,x16,#0xf00 | `FALL_THROUGH`
<a id="insn-00bdecec"></a> `00bdecec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdece0`](#insn-00bdece0) 範囲 `[['00bdece0', '00bdecef']]`

## 命令位置別の参照

- [`00bdece4`](#insn-00bdece4) → `00c1df00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdecec`](#insn-00bdecec) → [`00afced4`](../00afc/00afced4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afced4` · 推定シンボル `_ZN8firebase4Path16NormalizeSlashesERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdece4`](#insn-00bdece4)

~~~json
{
  "source": "00bdece4",
  "target": "00c1df00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1df00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdecec`](#insn-00bdecec)

~~~json
{
  "source": "00bdecec",
  "target": "00afced4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
