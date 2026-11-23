# 00bdbec0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbe10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbe10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-eef56a694b603e854a8dd4e94427807c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbf10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbf10.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0014.md#compare-8bca26ee70c765a9f84b863d42880516)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbec0",
  "name": "_ZN5Botan8CBC_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "39edc1d4f24f57318b50ad16f4d269743de53376c02940c31bce3e22562d009a",
  "source_text_sha256": "39edc1d4f24f57318b50ad16f4d269743de53376c02940c31bce3e22562d009a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbec0",
        "00bdbecf"
      ]
    ],
    "bytes_sha256": "07b9970b6cb7cdefe73ce39c7165e0ab6efa03dd5e2d18d7114dfd34f8d6b9df",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004a3d70](../004a3/004a3d70.md)
- [004aec4c](../004ae/004aec4c.md)
- [004aece4](../004ae/004aece4.md)

## 呼び出し先

- [004994e0](../00499/004994e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 220 bytes

~~~c

void _ZN5Botan8CBC_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE(void)

{
  (*(code *)PTR__ZN5Botan8CBC_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE_00c1c7f0)
            ();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbec0"></a> `00bdbec0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbec4"></a> `00bdbec4` | `11 fa 43 f9` | ldr x17,[x16, #0x7f0] | `FALL_THROUGH`
<a id="insn-00bdbec8"></a> `00bdbec8` | `10 c2 1f 91` | add x16,x16,#0x7f0 | `FALL_THROUGH`
<a id="insn-00bdbecc"></a> `00bdbecc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbec0`](#insn-00bdbec0) 範囲 `[['00bdbec0', '00bdbecf']]`

## 命令位置別の参照

- [`00bdbec4`](#insn-00bdbec4) → `00c1c7f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbecc`](#insn-00bdbecc) → [`004994e0`](../00499/004994e0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004994e0` · 推定シンボル `_ZN5Botan8CBC_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbec4`](#insn-00bdbec4)

~~~json
{
  "source": "00bdbec4",
  "target": "00c1c7f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c7f0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbecc`](#insn-00bdbecc)

~~~json
{
  "source": "00bdbecc",
  "target": "004994e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
