# 00bdbce0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbc30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbc30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-5664fd7d74c3d8aca578ab7cd7be8d0c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbd30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbd30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-65e1f344321a73189ec0ab659d1f1d47)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbce0",
  "name": "_ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "28676d2fdc3360a5a0a1f175d69b8bd5c1dd4fcd6a64fa31d4dcd558f2696385",
  "source_text_sha256": "28676d2fdc3360a5a0a1f175d69b8bd5c1dd4fcd6a64fa31d4dcd558f2696385",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbce0",
        "00bdbcef"
      ]
    ],
    "bytes_sha256": "3ae85f6898f026d79c27fe3abd4cca8387ca050c0ef328cfa6a756736c681aa7",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00490edc](../00490/00490edc.md)

## 呼び出し先

- [0049100c](../00491/0049100c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 245 bytes

~~~c

void _ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE(void)

{
  (*(code *)
    PTR__ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE_00c1c700
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbce0"></a> `00bdbce0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbce4"></a> `00bdbce4` | `11 82 43 f9` | ldr x17,[x16, #0x700] | `FALL_THROUGH`
<a id="insn-00bdbce8"></a> `00bdbce8` | `10 02 1c 91` | add x16,x16,#0x700 | `FALL_THROUGH`
<a id="insn-00bdbcec"></a> `00bdbcec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbce0`](#insn-00bdbce0) 範囲 `[['00bdbce0', '00bdbcef']]`

## 命令位置別の参照

- [`00bdbce4`](#insn-00bdbce4) → `00c1c700`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcec`](#insn-00bdbcec) → [`0049100c`](../00491/0049100c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0049100c` · 推定シンボル `_ZN5Botan9SCAN_NameC1ENSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbce4`](#insn-00bdbce4)

~~~json
{
  "source": "00bdbce4",
  "target": "00c1c700",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c700",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbcec`](#insn-00bdbcec)

~~~json
{
  "source": "00bdbcec",
  "target": "0049100c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
