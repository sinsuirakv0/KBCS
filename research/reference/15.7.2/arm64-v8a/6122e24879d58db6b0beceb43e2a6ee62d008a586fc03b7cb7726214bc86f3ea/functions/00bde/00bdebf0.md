# 00bdebf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdeca0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdeca0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-7d59ecd7338a8ffd561f3ecbc10e4f3c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdebf0",
  "name": "_ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6f8c168d469c235c57a637730c1b3e597ca98cd48fda240b5f354c7c62e63074",
  "source_text_sha256": "6f8c168d469c235c57a637730c1b3e597ca98cd48fda240b5f354c7c62e63074",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdebf0",
        "00bdebff"
      ]
    ],
    "bytes_sha256": "5471330f5f6ae7f4094bb1fa934c8b9797ffe1a2ccf4909f557736464ec1a9d5",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00afc4e4](../00afc/00afc4e4.md)

## 呼び出し先

- [00afc63c](../00afc/00afc63c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 163 bytes

~~~c

void _ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv(void)

{
  (*(code *)PTR__ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv_00c1de30)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdebf0"></a> `00bdebf0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdebf4"></a> `00bdebf4` | `11 1a 47 f9` | ldr x17,[x16, #0xe30] | `FALL_THROUGH`
<a id="insn-00bdebf8"></a> `00bdebf8` | `10 c2 38 91` | add x16,x16,#0xe30 | `FALL_THROUGH`
<a id="insn-00bdebfc"></a> `00bdebfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdebf0`](#insn-00bdebf0) 範囲 `[['00bdebf0', '00bdebff']]`

## 命令位置別の参照

- [`00bdebf4`](#insn-00bdebf4) → `00c1de30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdebfc`](#insn-00bdebfc) → [`00afc63c`](../00afc/00afc63c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afc63c` · 推定シンボル `_ZN8firebase15CleanupNotifier19UnregisterAllOwnersEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdebf4`](#insn-00bdebf4)

~~~json
{
  "source": "00bdebf4",
  "target": "00c1de30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1de30",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdebfc`](#insn-00bdebfc)

~~~json
{
  "source": "00bdebfc",
  "target": "00afc63c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
