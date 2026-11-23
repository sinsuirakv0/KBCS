# 00bdbdd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbd20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbd20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-24c5bfbf8fc2f6113c25aa0de0da8e65)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbe20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-1aa410ada712ecb7e70180cff138d3ec)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbdd0",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5writeEPKcl",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b938e0d9894838a39d914afe17547ecd4319b103df93a5beb069528239d6ff21",
  "source_text_sha256": "b938e0d9894838a39d914afe17547ecd4319b103df93a5beb069528239d6ff21",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbdd0",
        "00bdbddf"
      ]
    ],
    "bytes_sha256": "3173e2d09e4a389b4095af6d4c1377a5d4c0273060a49c3dadb65b7afed00095",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00495378](../00495/00495378.md)
- [004a32dc](../004a3/004a32dc.md)
- [004a6378](../004a6/004a6378.md)
- [00b46ee0](../00b46/00b46ee0.md)

## 呼び出し先

- [00b4704c](../00b47/00b4704c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 181 bytes

~~~c

void _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5writeEPKcl(void)

{
  (*(code *)PTR__ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5writeEPKcl_00c1c778)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbdd0"></a> `00bdbdd0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbdd4"></a> `00bdbdd4` | `11 be 43 f9` | ldr x17,[x16, #0x778] | `FALL_THROUGH`
<a id="insn-00bdbdd8"></a> `00bdbdd8` | `10 e2 1d 91` | add x16,x16,#0x778 | `FALL_THROUGH`
<a id="insn-00bdbddc"></a> `00bdbddc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbdd0`](#insn-00bdbdd0) 範囲 `[['00bdbdd0', '00bdbddf']]`

## 命令位置別の参照

- [`00bdbdd4`](#insn-00bdbdd4) → `00c1c778`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbddc`](#insn-00bdbddc) → [`00b4704c`](../00b47/00b4704c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b4704c` · 推定シンボル `_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE5writeEPKcl` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbdd4`](#insn-00bdbdd4)

~~~json
{
  "source": "00bdbdd4",
  "target": "00c1c778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c778",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbddc`](#insn-00bdbddc)

~~~json
{
  "source": "00bdbddc",
  "target": "00b4704c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
