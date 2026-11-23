# 00bdcca0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcbf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcbf0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-a56f003661a6cb50054d1812e8f4e663)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdccf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdccf0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-f3ed6f752d60f16fcf0721907e28c1cf)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcca0",
  "name": "_ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "166ca9367fcc38e1ba9f7c3cb0e1ea9ce48e1eb22365820ed07ea1480ca87316",
  "source_text_sha256": "166ca9367fcc38e1ba9f7c3cb0e1ea9ce48e1eb22365820ed07ea1480ca87316",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcca0",
        "00bdccaf"
      ]
    ],
    "bytes_sha256": "a2c2c9c5ab2991d57bf2ee2d6fde145c89ff2872a10b496c5845ae345ba4d33e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e3840](../004e3/004e3840.md)

## 呼び出し先

- [004e40b8](../004e4/004e40b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 157 bytes

~~~c

void _ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE(void)

{
  (*(code *)PTR__ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE_00c1cee0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcca0"></a> `00bdcca0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcca4"></a> `00bdcca4` | `11 72 47 f9` | ldr x17,[x16, #0xee0] | `FALL_THROUGH`
<a id="insn-00bdcca8"></a> `00bdcca8` | `10 82 3b 91` | add x16,x16,#0xee0 | `FALL_THROUGH`
<a id="insn-00bdccac"></a> `00bdccac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcca0`](#insn-00bdcca0) 範囲 `[['00bdcca0', '00bdccaf']]`

## 命令位置別の参照

- [`00bdcca4`](#insn-00bdcca4) → `00c1cee0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdccac`](#insn-00bdccac) → [`004e40b8`](../004e4/004e40b8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e40b8` · 推定シンボル `_ZN5Botan7X509_DN11decode_fromERNS_11BER_DecoderE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcca4`](#insn-00bdcca4)

~~~json
{
  "source": "00bdcca4",
  "target": "00c1cee0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cee0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdccac`](#insn-00bdccac)

~~~json
{
  "source": "00bdccac",
  "target": "004e40b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
