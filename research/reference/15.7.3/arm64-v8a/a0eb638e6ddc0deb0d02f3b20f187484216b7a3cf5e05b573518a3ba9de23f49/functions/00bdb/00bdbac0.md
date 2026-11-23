# 00bdbac0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdba10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdba10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-90966029ee12f460f094438398393edc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbb10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbb10.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-45a110896a9e33bf249e5526cf17f4eb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbac0",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEj",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e99c8b0dcc31b48ac5b0fcb83dc5a084e54b49fcfdcac19686f97073ec61a88",
  "source_text_sha256": "0e99c8b0dcc31b48ac5b0fcb83dc5a084e54b49fcfdcac19686f97073ec61a88",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbac0",
        "00bdbacf"
      ]
    ],
    "bytes_sha256": "ba32e1ab2cc714c9d6e18455096977251ca7f0d2bf1f2766bc88b1fec48d5f9d",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048930c](../00489/0048930c.md)
- [004d60c4](../004d6/004d60c4.md)
- [004dbd04](../004db/004dbd04.md)
- [00501b08](../00501/00501b08.md)
- [00b1567c](../00b15/00b1567c.md)

## 呼び出し先

- [00b3f9c0](../00b3f/00b3f9c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 167 bytes

~~~c

void _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEj(void)

{
  (*(code *)PTR__ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEj_00c1c5f0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbac0"></a> `00bdbac0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbac4"></a> `00bdbac4` | `11 fa 42 f9` | ldr x17,[x16, #0x5f0] | `FALL_THROUGH`
<a id="insn-00bdbac8"></a> `00bdbac8` | `10 c2 17 91` | add x16,x16,#0x5f0 | `FALL_THROUGH`
<a id="insn-00bdbacc"></a> `00bdbacc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbac0`](#insn-00bdbac0) 範囲 `[['00bdbac0', '00bdbacf']]`

## 命令位置別の参照

- [`00bdbac4`](#insn-00bdbac4) → `00c1c5f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbacc`](#insn-00bdbacc) → [`00b3f9c0`](../00b3f/00b3f9c0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b3f9c0` · 推定シンボル `_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEj` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbac4`](#insn-00bdbac4)

~~~json
{
  "source": "00bdbac4",
  "target": "00c1c5f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c5f0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbacc`](#insn-00bdbacc)

~~~json
{
  "source": "00bdbacc",
  "target": "00b3f9c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
