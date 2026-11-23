# 00bddee0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddf90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddf90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-b576134ccdbac67b91be3075a2668f8f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddee0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "01f9b4d4bdb750c05f3fb0d93da9157b50738266e0770e3c09b51bfe6c2846d4",
  "source_text_sha256": "01f9b4d4bdb750c05f3fb0d93da9157b50738266e0770e3c09b51bfe6c2846d4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddee0",
        "00bddeef"
      ]
    ],
    "bytes_sha256": "373c7e0bbeb80ddc59ad79005ad52b162fc2435e8ede940bf36d9a9d0b26c0bd",
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

- [00aff234](../00aff/00aff234.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 218 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(void)

{
  (*(code *)
    PTR__ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE_00c1d7a8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddee0"></a> `00bddee0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddee4"></a> `00bddee4` | `11 d6 43 f9` | ldr x17,[x16, #0x7a8] | `FALL_THROUGH`
<a id="insn-00bddee8"></a> `00bddee8` | `10 a2 1e 91` | add x16,x16,#0x7a8 | `FALL_THROUGH`
<a id="insn-00bddeec"></a> `00bddeec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddee0`](#insn-00bddee0) 範囲 `[['00bddee0', '00bddeef']]`

## 命令位置別の参照

- [`00bddee4`](#insn-00bddee4) → `00c1d7a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddeec`](#insn-00bddeec) → [`00aff234`](../00aff/00aff234.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aff234` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddee4`](#insn-00bddee4)

~~~json
{
  "source": "00bddee4",
  "target": "00c1d7a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d7a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddeec`](#insn-00bddeec)

~~~json
{
  "source": "00bddeec",
  "target": "00aff234",
  "target_space": "ram",
  "resolution": "function"
}
~~~
