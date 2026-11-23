# 00bddeb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdde00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-056c204806eb42301a12ca64eedc95fc)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddf00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf00.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-52da5fe75a1de2ed912519f2c6809c37)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddeb0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26CompleteWithResultInternalIS8_EEvRKNS_12FutureHandleEiPKcRKT_EUlPS8_E_EEvSC_iSE_RKT0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "24a291e05bd9e267f2116d0884ad46646d45d958da1cdde851088961e3e1a45c",
  "source_text_sha256": "24a291e05bd9e267f2116d0884ad46646d45d958da1cdde851088961e3e1a45c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddeb0",
        "00bddebf"
      ]
    ],
    "bytes_sha256": "8e0bb748e616c7c66d28b5528ce118e4be3d810491cbe89b6e522c266fa74242",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae2bc8](../00ae2/00ae2bc8.md)
- [00ae3330](../00ae3/00ae3330.md)
- [00b4de04](../00b4d/00b4de04.md)
- [00b4e0e0](../00b4e/00b4e0e0.md)

## 呼び出し先

- [00ae3554](../00ae3/00ae3554.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 519 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26CompleteWithResultInternalIS8_EEvRKNS_12FutureHandleEiPKcRKT_EUlPS8_E_EEvSC_iSE_RKT0_
               (void)

{
  (*(code *)
    PTR__ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26CompleteWithResultInternalIS8_EEvRKNS_12FutureHandleEiPKcRKT_EUlPS8_E_EEvSC_iSE_RKT0__00c1d7e8
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddeb0"></a> `00bddeb0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddeb4"></a> `00bddeb4` | `11 f6 43 f9` | ldr x17,[x16, #0x7e8] | `FALL_THROUGH`
<a id="insn-00bddeb8"></a> `00bddeb8` | `10 a2 1f 91` | add x16,x16,#0x7e8 | `FALL_THROUGH`
<a id="insn-00bddebc"></a> `00bddebc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddeb0`](#insn-00bddeb0) 範囲 `[['00bddeb0', '00bddebf']]`

## 命令位置別の参照

- [`00bddeb4`](#insn-00bddeb4) → `00c1d7e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddebc`](#insn-00bddebc) → [`00ae3554`](../00ae3/00ae3554.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae3554` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26CompleteWithResultInternalIS8_EEvRKNS_12FutureHandleEiPKcRKT_EUlPS8_E_EEvSC_iSE_RKT0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddeb4`](#insn-00bddeb4)

~~~json
{
  "source": "00bddeb4",
  "target": "00c1d7e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d7e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddebc`](#insn-00bddebc)

~~~json
{
  "source": "00bddebc",
  "target": "00ae3554",
  "target_space": "ram",
  "resolution": "function"
}
~~~
