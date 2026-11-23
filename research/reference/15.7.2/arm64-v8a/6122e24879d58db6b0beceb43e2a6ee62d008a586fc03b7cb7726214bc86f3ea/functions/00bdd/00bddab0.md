# 00bddab0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddb60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-6bbaedc2254303c456bf45306da8f96d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddab0",
  "name": "_ZN8firebase4auth4Auth7SignOutEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c4c9af862d9f1c321c1f725f2e625827098c0125ecbde110458841252e50e907",
  "source_text_sha256": "c4c9af862d9f1c321c1f725f2e625827098c0125ecbde110458841252e50e907",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddab0",
        "00bddabf"
      ]
    ],
    "bytes_sha256": "31d6307713cf17808f6e435f4a854cc290038c53ff3fa5f7f09b5792aa488f7f",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [008480dc](../00848/008480dc.md)

## 呼び出し先

- [00b5f9e4](../00b5f/00b5f9e4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 123 bytes

~~~c

void _ZN8firebase4auth4Auth7SignOutEv(void)

{
  (*(code *)PTR__ZN8firebase4auth4Auth7SignOutEv_00c1d590)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddab0"></a> `00bddab0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddab4"></a> `00bddab4` | `11 ca 42 f9` | ldr x17,[x16, #0x590] | `FALL_THROUGH`
<a id="insn-00bddab8"></a> `00bddab8` | `10 42 16 91` | add x16,x16,#0x590 | `FALL_THROUGH`
<a id="insn-00bddabc"></a> `00bddabc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddab0`](#insn-00bddab0) 範囲 `[['00bddab0', '00bddabf']]`

## 命令位置別の参照

- [`00bddab4`](#insn-00bddab4) → `00c1d590`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddabc`](#insn-00bddabc) → [`00b5f9e4`](../00b5f/00b5f9e4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b5f9e4` · 推定シンボル `_ZN8firebase4auth4Auth7SignOutEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddab4`](#insn-00bddab4)

~~~json
{
  "source": "00bddab4",
  "target": "00c1d590",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d590",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddabc`](#insn-00bddabc)

~~~json
{
  "source": "00bddabc",
  "target": "00b5f9e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
