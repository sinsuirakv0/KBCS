# 00bdcee0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcf90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcf90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0015.md#compare-d96d1d1ccb79768bc6e853bf7188472d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcee0",
  "name": "_ZN5Botan11BER_Decoder11decode_listINS_3OIDEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "42df370e02b485bbc194fb4f41344216b1b22173b32e0492f6d6994d8b2255a4",
  "source_text_sha256": "42df370e02b485bbc194fb4f41344216b1b22173b32e0492f6d6994d8b2255a4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcee0",
        "00bdceef"
      ]
    ],
    "bytes_sha256": "91a123aa8a46080a8ad89267739356353e882d60068d6037b6a557f1424a6df2",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004f6e58](../004f6/004f6e58.md)

## 呼び出し先

- [004f6f28](../004f6/004f6f28.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 301 bytes

~~~c

void _ZN5Botan11BER_Decoder11decode_listINS_3OIDEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB_
               (void)

{
  (*(code *)
    PTR__ZN5Botan11BER_Decoder11decode_listINS_3OIDEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB__00c1cfa8
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcee0"></a> `00bdcee0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcee4"></a> `00bdcee4` | `11 d6 47 f9` | ldr x17,[x16, #0xfa8] | `FALL_THROUGH`
<a id="insn-00bdcee8"></a> `00bdcee8` | `10 a2 3e 91` | add x16,x16,#0xfa8 | `FALL_THROUGH`
<a id="insn-00bdceec"></a> `00bdceec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcee0`](#insn-00bdcee0) 範囲 `[['00bdcee0', '00bdceef']]`

## 命令位置別の参照

- [`00bdcee4`](#insn-00bdcee4) → `00c1cfa8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdceec`](#insn-00bdceec) → [`004f6f28`](../004f6/004f6f28.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f6f28` · 推定シンボル `_ZN5Botan11BER_Decoder11decode_listINS_3OIDEEERS0_RNSt6__ndk16vectorIT_NS4_9allocatorIS6_EEEENS_8ASN1_TagESB_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcee4`](#insn-00bdcee4)

~~~json
{
  "source": "00bdcee4",
  "target": "00c1cfa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cfa8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdceec`](#insn-00bdceec)

~~~json
{
  "source": "00bdceec",
  "target": "004f6f28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
