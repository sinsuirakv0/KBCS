# 00bddba0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddaf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddaf0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-508993ad7423d24d72eaa2f1b1ed8a5d)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddbf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddbf0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-e70494a55431612d2e786ae0a9244be7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddba0",
  "name": "_ZNK8firebase4auth4User8is_validEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b43feb871b8adac85229cfa7e7c0254caf5a84f7abab06a2889eaa37ca405e57",
  "source_text_sha256": "b43feb871b8adac85229cfa7e7c0254caf5a84f7abab06a2889eaa37ca405e57",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddba0",
        "00bddbaf"
      ]
    ],
    "bytes_sha256": "72ecd214cbacb288bacfa3e3ed2d9278ed5bf458e9836691576595669b2d6a8a",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00848250](../00848/00848250.md)
- [0084859c](../00848/0084859c.md)
- [00ad4ff4](../00ad4/00ad4ff4.md)
- [00b5c938](../00b5c/00b5c938.md)
- [00b5c96c](../00b5c/00b5c96c.md)

## 呼び出し先

- [00b6e940](../00b6e/00b6e940.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 127 bytes

~~~c

void _ZNK8firebase4auth4User8is_validEv(void)

{
  (*(code *)PTR__ZNK8firebase4auth4User8is_validEv_00c1d660)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddba0"></a> `00bddba0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddba4"></a> `00bddba4` | `11 32 43 f9` | ldr x17,[x16, #0x660] | `FALL_THROUGH`
<a id="insn-00bddba8"></a> `00bddba8` | `10 82 19 91` | add x16,x16,#0x660 | `FALL_THROUGH`
<a id="insn-00bddbac"></a> `00bddbac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddba0`](#insn-00bddba0) 範囲 `[['00bddba0', '00bddbaf']]`

## 命令位置別の参照

- [`00bddba4`](#insn-00bddba4) → `00c1d660`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddbac`](#insn-00bddbac) → [`00b6e940`](../00b6e/00b6e940.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b6e940` · 推定シンボル `_ZNK8firebase4auth4User8is_validEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddba4`](#insn-00bddba4)

~~~json
{
  "source": "00bddba4",
  "target": "00c1d660",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d660",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddbac`](#insn-00bddbac)

~~~json
{
  "source": "00bddbac",
  "target": "00b6e940",
  "target_space": "ram",
  "resolution": "function"
}
~~~
