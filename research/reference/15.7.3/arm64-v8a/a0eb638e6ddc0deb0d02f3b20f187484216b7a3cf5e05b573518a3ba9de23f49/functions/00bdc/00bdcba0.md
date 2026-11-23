# 00bdcba0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcaf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcaf0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-5a81db92f487c8c9db2f6daa59029e1e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcbf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcbf0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0015.md#compare-332741f8394784af70cb659b2ba1d86d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcba0",
  "name": "_ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0ac6501bc0f89257f835464c4f57e6ca9912167620c93909ea8593a35a4a966e",
  "source_text_sha256": "0ac6501bc0f89257f835464c4f57e6ca9912167620c93909ea8593a35a4a966e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcba0",
        "00bdcbaf"
      ]
    ],
    "bytes_sha256": "1efe957b1d0b325bd32ad215d7c4dad4f11a90ecde26bc94fd3b9d4c08f22676",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004df5b0](../004df/004df5b0.md)

## 呼び出し先

- [004df724](../004df/004df724.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 239 bytes

~~~c

void _ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE(void)

{
  (*(code *)
    PTR__ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE_00c1ce60
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcba0"></a> `00bdcba0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcba4"></a> `00bdcba4` | `11 32 47 f9` | ldr x17,[x16, #0xe60] | `FALL_THROUGH`
<a id="insn-00bdcba8"></a> `00bdcba8` | `10 82 39 91` | add x16,x16,#0xe60 | `FALL_THROUGH`
<a id="insn-00bdcbac"></a> `00bdcbac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcba0`](#insn-00bdcba0) 範囲 `[['00bdcba0', '00bdcbaf']]`

## 命令位置別の参照

- [`00bdcba4`](#insn-00bdcba4) → `00c1ce60`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcbac`](#insn-00bdcbac) → [`004df724`](../004df/004df724.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004df724` · 推定シンボル `_ZN5Botan27Certificate_Store_In_Memory7add_crlENSt6__ndk110shared_ptrIKNS_8X509_CRLEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcba4`](#insn-00bdcba4)

~~~json
{
  "source": "00bdcba4",
  "target": "00c1ce60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce60",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcbac`](#insn-00bdcbac)

~~~json
{
  "source": "00bdcbac",
  "target": "004df724",
  "target_space": "ram",
  "resolution": "function"
}
~~~
