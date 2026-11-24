# 00bdefe0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdef90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bdef90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0021.md#compare-4e945c400e1ae2559dc236c0f2117edd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c5ba90`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c5b/00c5ba90.md) · 移動量 `+0x7cab0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0014.md#compare-047b45a286d8ba77b4c778469ecc632c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdefe0",
  "name": "<EXTERNAL>::pthread_mutexattr_destroy",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ae8b5842b5a9f1ddb4293020035cad571d220c22d6e2827ebba9772b08dc079d",
  "source_text_sha256": "ae8b5842b5a9f1ddb4293020035cad571d220c22d6e2827ebba9772b08dc079d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdefe0",
        "00bdefef"
      ]
    ],
    "bytes_sha256": "bab4a1e2fb5db0ebc543d05e780fcd23971ef616af6b6e10b6ca5da6cc63e8d2",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b053d4](../00b05/00b053d4.md)
- [00b7d334](../00b7d/00b7d334.md)

## 呼び出し先

- [010a5618](../010a5/010a5618.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 250 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

int pthread_mutexattr_destroy(pthread_mutexattr_t *__attr)

{
  int iVar1;
  
  iVar1 = (*(code *)PTR_pthread_mutexattr_destroy_00c1e0a8)((int)__attr);
  return iVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdefe0"></a> `00bdefe0` | `10 02 00 90` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdefe4"></a> `00bdefe4` | `11 56 40 f9` | ldr x17,[x16, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdefe8"></a> `00bdefe8` | `10 a2 02 91` | add x16,x16,#0xa8 | `FALL_THROUGH`
<a id="insn-00bdefec"></a> `00bdefec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdefe0`](#insn-00bdefe0) 範囲 `[['00bdefe0', '00bdefef']]`

## 命令位置別の参照

- [`00bdefe4`](#insn-00bdefe4) → `00c1e0a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdefec`](#insn-00bdefec) → [`010a5618`](../010a5/010a5618.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5618` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdefe4`](#insn-00bdefe4)

~~~json
{
  "source": "00bdefe4",
  "target": "00c1e0a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e0a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdefec`](#insn-00bdefec)

~~~json
{
  "source": "00bdefec",
  "target": "010a5618",
  "target_space": "ram",
  "resolution": "function"
}
~~~
