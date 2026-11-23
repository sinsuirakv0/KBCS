# 00bddfb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddf00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-b2fed47b3410a3ed326deba68cfa8674)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bde000`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde000.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-a3eb995ca4dcaace84e8b32fa9df2b56)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddfb0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d1e7d8fae5c1281a65ec8052e51acc8a58b38e49b0998937a9acc660fcd8f454",
  "source_text_sha256": "d1e7d8fae5c1281a65ec8052e51acc8a58b38e49b0998937a9acc660fcd8f454",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddfb0",
        "00bddfbf"
      ]
    ],
    "bytes_sha256": "02a36511c13e696c74e504becf341ba8d850839996280f492e57760840323287",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae3554](../00ae3/00ae3554.md)
- [00ae3b80](../00ae3/00ae3b80.md)
- [00ae3ca4](../00ae3/00ae3ca4.md)
- [00ae3e0c](../00ae3/00ae3e0c.md)
- [00b0151c](../00b01/00b0151c.md)
- [00b0df30](../00b0d/00b0df30.md)
- [00b5a058](../00b5a/00b5a058.md)
- [00b5a184](../00b5a/00b5a184.md)
- [00b5a2b4](../00b5a/00b5a2b4.md)
- [00b5a468](../00b5a/00b5a468.md)
- [00b5ffb8](../00b5f/00b5ffb8.md)
- [00b60194](../00b60/00b60194.md)
- [00b604ac](../00b60/00b604ac.md)
- [00b60698](../00b60/00b60698.md)
- [00b60874](../00b60/00b60874.md)
- [00b60a4c](../00b60/00b60a4c.md)
- [00b60c28](../00b60/00b60c28.md)
- [00b6cae8](../00b6c/00b6cae8.md)
- [00b6d2ec](../00b6d/00b6d2ec.md)
- [00b71940](../00b71/00b71940.md)
- [00b71b1c](../00b71/00b71b1c.md)

## 呼び出し先

- [00aff3ac](../00aff/00aff3ac.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 181 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(void)

{
  (*(code *)PTR__ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm_00c1d868)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddfb0"></a> `00bddfb0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddfb4"></a> `00bddfb4` | `11 36 44 f9` | ldr x17,[x16, #0x868] | `FALL_THROUGH`
<a id="insn-00bddfb8"></a> `00bddfb8` | `10 a2 21 91` | add x16,x16,#0x868 | `FALL_THROUGH`
<a id="insn-00bddfbc"></a> `00bddfbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddfb0`](#insn-00bddfb0) 範囲 `[['00bddfb0', '00bddfbf']]`

## 命令位置別の参照

- [`00bddfb4`](#insn-00bddfb4) → `00c1d868`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddfbc`](#insn-00bddfbc) → [`00aff3ac`](../00aff/00aff3ac.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aff3ac` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddfb4`](#insn-00bddfb4)

~~~json
{
  "source": "00bddfb4",
  "target": "00c1d868",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d868",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddfbc`](#insn-00bddfbc)

~~~json
{
  "source": "00bddfbc",
  "target": "00aff3ac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
