# 00bdbbd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbb20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-eb1d39c2dc430d45f1927335a5332aa6)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbc20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0004.md#compare-b3323c219f30735f4d292c85352c8d4e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbd0",
  "name": "_ZN5Botan11BER_Decoder6decodeERmNS_8ASN1_TagES2_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "26dfc1f8521beb611e2f152b985124634951a23aeed817179c5b6678b3191342",
  "source_text_sha256": "26dfc1f8521beb611e2f152b985124634951a23aeed817179c5b6678b3191342",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbbd0",
        "00bdbbdf"
      ]
    ],
    "bytes_sha256": "be7082ede4e76b738384784b77a6fb6cd6968877810bfe2fecf37630e7269fc2",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048dc08](../0048d/0048dc08.md)
- [004c05ec](../004c0/004c05ec.md)
- [004c13f0](../004c1/004c13f0.md)
- [004c5ac8](../004c5/004c5ac8.md)
- [004c9e38](../004c9/004c9e38.md)
- [004cf854](../004cf/004cf854.md)
- [004e6d3c](../004e6/004e6d3c.md)
- [004eb16c](../004eb/004eb16c.md)
- [004fab14](../004fa/004fab14.md)
- [004fae30](../004fa/004fae30.md)

## 呼び出し先

- [0048dc14](../0048d/0048dc14.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 155 bytes

~~~c

void _ZN5Botan11BER_Decoder6decodeERmNS_8ASN1_TagES2_(void)

{
  (*(code *)PTR__ZN5Botan11BER_Decoder6decodeERmNS_8ASN1_TagES2__00c1c678)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbbd0"></a> `00bdbbd0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbbd4"></a> `00bdbbd4` | `11 3e 43 f9` | ldr x17,[x16, #0x678] | `FALL_THROUGH`
<a id="insn-00bdbbd8"></a> `00bdbbd8` | `10 e2 19 91` | add x16,x16,#0x678 | `FALL_THROUGH`
<a id="insn-00bdbbdc"></a> `00bdbbdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbbd0`](#insn-00bdbbd0) 範囲 `[['00bdbbd0', '00bdbbdf']]`

## 命令位置別の参照

- [`00bdbbd4`](#insn-00bdbbd4) → `00c1c678`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbdc`](#insn-00bdbbdc) → [`0048dc14`](../0048d/0048dc14.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048dc14` · 推定シンボル `_ZN5Botan11BER_Decoder6decodeERmNS_8ASN1_TagES2_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbbd4`](#insn-00bdbbd4)

~~~json
{
  "source": "00bdbbd4",
  "target": "00c1c678",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c678",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbbdc`](#insn-00bdbbdc)

~~~json
{
  "source": "00bdbbdc",
  "target": "0048dc14",
  "target_space": "ram",
  "resolution": "function"
}
~~~
