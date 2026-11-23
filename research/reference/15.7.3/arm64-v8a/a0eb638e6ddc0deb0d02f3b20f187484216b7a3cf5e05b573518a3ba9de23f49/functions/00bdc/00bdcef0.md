# 00bdcef0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdce40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdce40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-206daa278e55ba8cb4d3d5e3c9a5dc79)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcf40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcf40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0005.md#compare-0cc3a93bdd4ef17a865a11632cc7e1f3)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcef0",
  "name": "_ZN5Botan8X509_CRLC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "de62897f8a8c2cda13e24edc6c66ad6f6d5490c744d220ca8dafe6125329a5d9",
  "source_text_sha256": "de62897f8a8c2cda13e24edc6c66ad6f6d5490c744d220ca8dafe6125329a5d9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcef0",
        "00bdceff"
      ]
    ],
    "bytes_sha256": "d20c56700dd87c9c04d095950c1c8f7215d28bffae199db21d4ab851eacf6d71",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004ef204](../004ef/004ef204.md)

## 呼び出し先

- [004efb8c](../004ef/004efb8c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 183 bytes

~~~c

void _ZN5Botan8X509_CRLC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE(void)

{
  (*(code *)PTR__ZN5Botan8X509_CRLC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE_00c1d008)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcef0"></a> `00bdcef0` | `10 02 00 b0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdcef4"></a> `00bdcef4` | `11 06 40 f9` | ldr x17,[x16, #0x8] | `FALL_THROUGH`
<a id="insn-00bdcef8"></a> `00bdcef8` | `10 22 00 91` | add x16,x16,#0x8 | `FALL_THROUGH`
<a id="insn-00bdcefc"></a> `00bdcefc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcef0`](#insn-00bdcef0) 範囲 `[['00bdcef0', '00bdceff']]`

## 命令位置別の参照

- [`00bdcef4`](#insn-00bdcef4) → `00c1d008`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcefc`](#insn-00bdcefc) → [`004efb8c`](../004ef/004efb8c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004efb8c` · 推定シンボル `_ZN5Botan8X509_CRLC2ERKNSt6__ndk16vectorIhNS1_9allocatorIhEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcef4`](#insn-00bdcef4)

~~~json
{
  "source": "00bdcef4",
  "target": "00c1d008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d008",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcefc`](#insn-00bdcefc)

~~~json
{
  "source": "00bdcefc",
  "target": "004efb8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
