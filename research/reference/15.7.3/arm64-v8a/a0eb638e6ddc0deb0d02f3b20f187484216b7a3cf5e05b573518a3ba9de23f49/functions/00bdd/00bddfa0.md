# 00bddfa0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddef0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddef0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-b3c3bc28f437f1439108e7063fd4ebbf)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddff0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddff0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-d1eafa5968725722ef35192b85198237)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddfa0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b6bc5f2feb4fadfc09de45a487fb1f3d62459473aa723e8f02c3a611458ec81f",
  "source_text_sha256": "b6bc5f2feb4fadfc09de45a487fb1f3d62459473aa723e8f02c3a611458ec81f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddfa0",
        "00bddfaf"
      ]
    ],
    "bytes_sha256": "fd58324ebcbd55694a1abc8f44eec9a0d52008a8bab34f0806ac4e4c15b690d9",
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

- [00aff1d8](../00aff/00aff1d8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 239 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc(void)

{
  (*(code *)
    PTR__ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc_00c1d860
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddfa0"></a> `00bddfa0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddfa4"></a> `00bddfa4` | `11 32 44 f9` | ldr x17,[x16, #0x860] | `FALL_THROUGH`
<a id="insn-00bddfa8"></a> `00bddfa8` | `10 82 21 91` | add x16,x16,#0x860 | `FALL_THROUGH`
<a id="insn-00bddfac"></a> `00bddfac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddfa0`](#insn-00bddfa0) 範囲 `[['00bddfa0', '00bddfaf']]`

## 命令位置別の参照

- [`00bddfa4`](#insn-00bddfa4) → `00c1d860`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddfac`](#insn-00bddfac) → [`00aff1d8`](../00aff/00aff1d8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aff1d8` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddfa4`](#insn-00bddfa4)

~~~json
{
  "source": "00bddfa4",
  "target": "00c1d860",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d860",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddfac`](#insn-00bddfac)

~~~json
{
  "source": "00bddfac",
  "target": "00aff1d8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
