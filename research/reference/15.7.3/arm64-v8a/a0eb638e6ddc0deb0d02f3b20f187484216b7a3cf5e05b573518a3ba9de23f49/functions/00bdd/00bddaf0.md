# 00bddaf0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdda40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdda40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-2ec01ffda0cf37164693c1ccd8fbf0ea)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddb40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddb40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0017.md#compare-8d5e0e14c8121a93bab4040489bf730e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddaf0",
  "name": "_ZN8firebase9analytics8LogEventEPKcPKNS0_9ParameterEm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8ec17d0c06ae019f5bb32a3003177e99766d2fed76a696a9ba357c35685c0d07",
  "source_text_sha256": "8ec17d0c06ae019f5bb32a3003177e99766d2fed76a696a9ba357c35685c0d07",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddaf0",
        "00bddaff"
      ]
    ],
    "bytes_sha256": "a1f2c47e4f07ce2338fe2b1facf94d25c5853af936e56d5d330da655330ff48d",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0084642c](../00846/0084642c.md)
- [00846bdc](../00846/00846bdc.md)
- [00ae2548](../00ae2/00ae2548.md)
- [00ae26c8](../00ae2/00ae26c8.md)

## 呼び出し先

- [00ae2554](../00ae2/00ae2554.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 165 bytes

~~~c

void _ZN8firebase9analytics8LogEventEPKcPKNS0_9ParameterEm(void)

{
  (*(code *)PTR__ZN8firebase9analytics8LogEventEPKcPKNS0_9ParameterEm_00c1d608)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddaf0"></a> `00bddaf0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddaf4"></a> `00bddaf4` | `11 06 43 f9` | ldr x17,[x16, #0x608] | `FALL_THROUGH`
<a id="insn-00bddaf8"></a> `00bddaf8` | `10 22 18 91` | add x16,x16,#0x608 | `FALL_THROUGH`
<a id="insn-00bddafc"></a> `00bddafc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddaf0`](#insn-00bddaf0) 範囲 `[['00bddaf0', '00bddaff']]`

## 命令位置別の参照

- [`00bddaf4`](#insn-00bddaf4) → `00c1d608`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddafc`](#insn-00bddafc) → [`00ae2554`](../00ae2/00ae2554.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae2554` · 推定シンボル `_ZN8firebase9analytics8LogEventEPKcPKNS0_9ParameterEm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddaf4`](#insn-00bddaf4)

~~~json
{
  "source": "00bddaf4",
  "target": "00c1d608",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d608",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddafc`](#insn-00bddafc)

~~~json
{
  "source": "00bddafc",
  "target": "00ae2554",
  "target_space": "ram",
  "resolution": "function"
}
~~~
