# 00bdddd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddd20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddd20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-be886df6dbad382d76daca213a952652)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdde20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bdde20.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-533fe5b9d0acde2ec151d6bf3524b3ab)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdddd0",
  "name": "_ZN8firebase5MutexC2ENS0_4ModeE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a457361e07bba4b80be789ccc62fcecfacdc9c2429316cf94dc891cfd2f2db23",
  "source_text_sha256": "a457361e07bba4b80be789ccc62fcecfacdc9c2429316cf94dc891cfd2f2db23",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdddd0",
        "00bddddf"
      ]
    ],
    "bytes_sha256": "e2c95e6c59e413fac28e0635b7871475c795d6033012107f448c4b349ef0ee55",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae01c8](../00ae0/00ae01c8.md)
- [00ae3f60](../00ae3/00ae3f60.md)
- [00ae456c](../00ae4/00ae456c.md)
- [00afafcc](../00afa/00afafcc.md)
- [00afb754](../00afb/00afb754.md)
- [00afba04](../00afb/00afba04.md)
- [00afbd1c](../00afb/00afbd1c.md)
- [00afbe48](../00afb/00afbe48.md)
- [00afc4f0](../00afc/00afc4f0.md)
- [00afc52c](../00afc/00afc52c.md)
- [00afce80](../00afc/00afce80.md)
- [00b00638](../00b00/00b00638.md)
- [00b02e24](../00b02/00b02e24.md)
- [00b48f30](../00b48/00b48f30.md)
- [00b4aa58](../00b4a/00b4aa58.md)
- [00b4c480](../00b4c/00b4c480.md)
- [00b4ee14](../00b4e/00b4ee14.md)
- [00b52cf8](../00b52/00b52cf8.md)
- [00b54af4](../00b54/00b54af4.md)
- [00b5a6f0](../00b5a/00b5a6f0.md)
- [00b5af48](../00b5a/00b5af48.md)
- [00b5c7a0](../00b5c/00b5c7a0.md)

## 呼び出し先

- [00b05390](../00b05/00b05390.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 121 bytes

~~~c

void _ZN8firebase5MutexC2ENS0_4ModeE(void)

{
  (*(code *)PTR__ZN8firebase5MutexC2ENS0_4ModeE_00c1d778)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdddd0"></a> `00bdddd0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdddd4"></a> `00bdddd4` | `11 be 43 f9` | ldr x17,[x16, #0x778] | `FALL_THROUGH`
<a id="insn-00bdddd8"></a> `00bdddd8` | `10 e2 1d 91` | add x16,x16,#0x778 | `FALL_THROUGH`
<a id="insn-00bddddc"></a> `00bddddc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdddd0`](#insn-00bdddd0) 範囲 `[['00bdddd0', '00bddddf']]`

## 命令位置別の参照

- [`00bdddd4`](#insn-00bdddd4) → `00c1d778`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddddc`](#insn-00bddddc) → [`00b05390`](../00b05/00b05390.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b05390` · 推定シンボル `_ZN8firebase5MutexC2ENS0_4ModeE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdddd4`](#insn-00bdddd4)

~~~json
{
  "source": "00bdddd4",
  "target": "00c1d778",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d778",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddddc`](#insn-00bddddc)

~~~json
{
  "source": "00bddddc",
  "target": "00b05390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
