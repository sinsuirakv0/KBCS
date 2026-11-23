# 00bdded0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddf80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-35d06b430575ba25bc997b2463bf9506)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdded0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "21fa6dae1fc5853af44ac7868599bf0bd3790c32dfd0657d4ea0c9a420c9f238",
  "source_text_sha256": "21fa6dae1fc5853af44ac7868599bf0bd3790c32dfd0657d4ea0c9a420c9f238",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdded0",
        "00bddedf"
      ]
    ],
    "bytes_sha256": "c31d4328042e62cafb156c5231e4f76657a46717d554b705b7c220eeea55cdb8",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae348c](../00ae3/00ae348c.md)
- [00ae3ab8](../00ae3/00ae3ab8.md)
- [00ae3bdc](../00ae3/00ae3bdc.md)
- [00ae3d44](../00ae3/00ae3d44.md)
- [00b00e74](../00b00/00b00e74.md)
- [00b59f90](../00b59/00b59f90.md)
- [00b5a0bc](../00b5a/00b5a0bc.md)
- [00b5a1ec](../00b5a/00b5a1ec.md)
- [00b5a3a0](../00b5a/00b5a3a0.md)
- [00b5fef0](../00b5f/00b5fef0.md)
- [00b600cc](../00b60/00b600cc.md)
- [00b603e4](../00b60/00b603e4.md)
- [00b605d0](../00b60/00b605d0.md)
- [00b607ac](../00b60/00b607ac.md)
- [00b60984](../00b60/00b60984.md)
- [00b60b60](../00b60/00b60b60.md)
- [00b6ca20](../00b6c/00b6ca20.md)
- [00b6d224](../00b6d/00b6d224.md)
- [00b71878](../00b71/00b71878.md)
- [00b71a54](../00b71/00b71a54.md)

## 呼び出し先

- [00aff154](../00aff/00aff154.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 227 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(void)

{
  (*(code *)
    PTR__ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE_00c1d7a0)()
  ;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdded0"></a> `00bdded0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdded4"></a> `00bdded4` | `11 d2 43 f9` | ldr x17,[x16, #0x7a0] | `FALL_THROUGH`
<a id="insn-00bdded8"></a> `00bdded8` | `10 82 1e 91` | add x16,x16,#0x7a0 | `FALL_THROUGH`
<a id="insn-00bddedc"></a> `00bddedc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdded0`](#insn-00bdded0) 範囲 `[['00bdded0', '00bddedf']]`

## 命令位置別の参照

- [`00bdded4`](#insn-00bdded4) → `00c1d7a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddedc`](#insn-00bddedc) → [`00aff154`](../00aff/00aff154.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aff154` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdded4`](#insn-00bdded4)

~~~json
{
  "source": "00bdded4",
  "target": "00c1d7a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d7a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddedc`](#insn-00bddedc)

~~~json
{
  "source": "00bddedc",
  "target": "00aff154",
  "target_space": "ram",
  "resolution": "function"
}
~~~
