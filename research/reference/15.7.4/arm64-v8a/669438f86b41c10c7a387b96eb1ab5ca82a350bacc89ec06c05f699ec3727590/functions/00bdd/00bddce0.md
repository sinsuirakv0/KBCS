# 00bddce0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddc90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-5631ccfb861163d619f10e12bfa1b795)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5a730`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5a/00c5a730.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0011.md#compare-8e66796f385cd70088ca2491572444d0)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddce0",
  "name": "_ZN8firebase13remote_config12RemoteConfig11GetInstanceEPNS_3AppE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f9ab891945138fc9963dfe5a85741be7a51422b16b85ec5323d361f07b1e1c2",
  "source_text_sha256": "2f9ab891945138fc9963dfe5a85741be7a51422b16b85ec5323d361f07b1e1c2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddce0",
        "00bddcef"
      ]
    ],
    "bytes_sha256": "a634b5b3735883125afd0c9839a10f44fcd5e7c8f405aab285884607bd0ceb79",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0084b5fc](../0084b/0084b5fc.md)

## 呼び出し先

- [00b525c0](../00b52/00b525c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 187 bytes

~~~c

void _ZN8firebase13remote_config12RemoteConfig11GetInstanceEPNS_3AppE(void)

{
  (*(code *)PTR__ZN8firebase13remote_config12RemoteConfig11GetInstanceEPNS_3AppE_00c1d728)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddce0"></a> `00bddce0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddce4"></a> `00bddce4` | `11 96 43 f9` | ldr x17,[x16, #0x728] | `FALL_THROUGH`
<a id="insn-00bddce8"></a> `00bddce8` | `10 a2 1c 91` | add x16,x16,#0x728 | `FALL_THROUGH`
<a id="insn-00bddcec"></a> `00bddcec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddce0`](#insn-00bddce0) 範囲 `[['00bddce0', '00bddcef']]`

## 命令位置別の参照

- [`00bddce4`](#insn-00bddce4) → `00c1d728`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddcec`](#insn-00bddcec) → [`00b525c0`](../00b52/00b525c0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b525c0` · 推定シンボル `_ZN8firebase13remote_config12RemoteConfig11GetInstanceEPNS_3AppE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddce4`](#insn-00bddce4)

~~~json
{
  "source": "00bddce4",
  "target": "00c1d728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d728",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddcec`](#insn-00bddcec)

~~~json
{
  "source": "00bddcec",
  "target": "00b525c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
