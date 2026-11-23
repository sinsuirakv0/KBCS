# 00bddea0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddf50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf50.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-062daa3a6afb50b1df0546c9f48bbb0f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddea0",
  "name": "_ZN8firebase12FutureHandleaSERKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "041cb55ffdba257be002bd7ab74edc3fb464f0d5b579fb86c77d4bcb1deb31ab",
  "source_text_sha256": "041cb55ffdba257be002bd7ab74edc3fb464f0d5b579fb86c77d4bcb1deb31ab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddea0",
        "00bddeaf"
      ]
    ],
    "bytes_sha256": "fd42c33e27925947ebb74012be34cd9c61b8b78f8aa20e0af6c4104631b5dccc",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae37cc](../00ae3/00ae37cc.md)

## 呼び出し先

- [00b00cac](../00b00/00b00cac.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 127 bytes

~~~c

void _ZN8firebase12FutureHandleaSERKS0_(void)

{
  (*(code *)PTR__ZN8firebase12FutureHandleaSERKS0__00c1d788)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddea0"></a> `00bddea0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddea4"></a> `00bddea4` | `11 c6 43 f9` | ldr x17,[x16, #0x788] | `FALL_THROUGH`
<a id="insn-00bddea8"></a> `00bddea8` | `10 22 1e 91` | add x16,x16,#0x788 | `FALL_THROUGH`
<a id="insn-00bddeac"></a> `00bddeac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddea0`](#insn-00bddea0) 範囲 `[['00bddea0', '00bddeaf']]`

## 命令位置別の参照

- [`00bddea4`](#insn-00bddea4) → `00c1d788`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddeac`](#insn-00bddeac) → [`00b00cac`](../00b00/00b00cac.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b00cac` · 推定シンボル `_ZN8firebase12FutureHandleaSERKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddea4`](#insn-00bddea4)

~~~json
{
  "source": "00bddea4",
  "target": "00c1d788",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d788",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddeac`](#insn-00bddeac)

~~~json
{
  "source": "00bddeac",
  "target": "00b00cac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
