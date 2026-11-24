# 00bdfea0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdfe50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdf/00bdfe50.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0023.md#compare-ada17c163c0ce3dc460b1e4a6be5bcdf)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0095.md#review-5722e4e4271076c4bbb0644ecd45eb80)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdfea0",
  "name": "_ZNSt6__ndk16__sortIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEvT0_SA_T_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be4f07886b8e915a06dbff504001914385334e27feb21ee682d854c119f16c5e",
  "source_text_sha256": "be4f07886b8e915a06dbff504001914385334e27feb21ee682d854c119f16c5e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdfea0",
        "00bdfeaf"
      ]
    ],
    "bytes_sha256": "97117a45688e47117d0c2e020b90c72a1d8896a094c49735ceaf157452effbbc",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b290d4](../00b29/00b290d4.md)
- [00b45728](../00b45/00b45728.md)

## 呼び出し先

- [00b45728](../00b45/00b45728.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 197 bytes

~~~c

void _ZNSt6__ndk16__sortIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEvT0_SA_T_(void)

{
  (*(code *)PTR__ZNSt6__ndk16__sortIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEvT0_SA_T__00c1e808)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdfea0"></a> `00bdfea0` | `f0 01 00 f0` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdfea4"></a> `00bdfea4` | `11 06 44 f9` | ldr x17,[x16, #0x808] | `FALL_THROUGH`
<a id="insn-00bdfea8"></a> `00bdfea8` | `10 22 20 91` | add x16,x16,#0x808 | `FALL_THROUGH`
<a id="insn-00bdfeac"></a> `00bdfeac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdfea0`](#insn-00bdfea0) 範囲 `[['00bdfea0', '00bdfeaf']]`

## 命令位置別の参照

- [`00bdfea4`](#insn-00bdfea4) → `00c1e808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdfeac`](#insn-00bdfeac) → [`00b45728`](../00b45/00b45728.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b45728` · 推定シンボル `_ZNSt6__ndk16__sortIRPFbPKN11flatbuffers7EnumDefES4_EPPS2_EEvT0_SA_T_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdfea4`](#insn-00bdfea4)

~~~json
{
  "source": "00bdfea4",
  "target": "00c1e808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e808",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdfeac`](#insn-00bdfeac)

~~~json
{
  "source": "00bdfeac",
  "target": "00b45728",
  "target_space": "ram",
  "resolution": "function"
}
~~~
