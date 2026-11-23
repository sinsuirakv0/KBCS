# 00bddeb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddf60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-fd7f77f2264b052fb74840535ab435c1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddeb0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f3fbea85d5e1c4d8dd60af30c37e77f20c96ecd1907e0007f5524fc65e11921",
  "source_text_sha256": "9f3fbea85d5e1c4d8dd60af30c37e77f20c96ecd1907e0007f5524fc65e11921",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddeb0",
        "00bddebf"
      ]
    ],
    "bytes_sha256": "441d1e071885db566b298c54e917bd0e6d14894b48322af2c62d5b6facaf782e",
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

- [00aff108](../00aff/00aff108.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 220 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE(void)

{
  (*(code *)
    PTR__ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE_00c1d790)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddeb0"></a> `00bddeb0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddeb4"></a> `00bddeb4` | `11 ca 43 f9` | ldr x17,[x16, #0x790] | `FALL_THROUGH`
<a id="insn-00bddeb8"></a> `00bddeb8` | `10 42 1e 91` | add x16,x16,#0x790 | `FALL_THROUGH`
<a id="insn-00bddebc"></a> `00bddebc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddeb0`](#insn-00bddeb0) 範囲 `[['00bddeb0', '00bddebf']]`

## 命令位置別の参照

- [`00bddeb4`](#insn-00bddeb4) → `00c1d790`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddebc`](#insn-00bddebc) → [`00aff108`](../00aff/00aff108.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aff108` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddeb4`](#insn-00bddeb4)

~~~json
{
  "source": "00bddeb4",
  "target": "00c1d790",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d790",
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
  "target": "00aff108",
  "target_space": "ram",
  "resolution": "function"
}
~~~
