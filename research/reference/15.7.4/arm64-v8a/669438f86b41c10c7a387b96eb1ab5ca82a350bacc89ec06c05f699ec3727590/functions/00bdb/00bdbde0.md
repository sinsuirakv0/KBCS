# 00bdbde0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbd90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-f1a27047fc819072a0a0bc715e8c51f7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58830`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58830.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-368b4ef431a723d57fe1c051465c56f1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbde0",
  "name": "_ZN5Botan6BigIntrSEm",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3115225f0bad69cca1cc643d3245cb62e211992596fc407e4456dfbb74fd2f41",
  "source_text_sha256": "3115225f0bad69cca1cc643d3245cb62e211992596fc407e4456dfbb74fd2f41",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbde0",
        "00bdbdef"
      ]
    ],
    "bytes_sha256": "ba329f58e9241ae76ed09a20cb8899cf151844e592e996a54586c80275430e05",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00493850](../00493/00493850.md)
- [004963cc](../00496/004963cc.md)

## 呼び出し先

- [00496564](../00496/00496564.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 99 bytes

~~~c

void _ZN5Botan6BigIntrSEm(void)

{
  (*(code *)PTR__ZN5Botan6BigIntrSEm_00c1c7a8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbde0"></a> `00bdbde0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbde4"></a> `00bdbde4` | `11 d6 43 f9` | ldr x17,[x16, #0x7a8] | `FALL_THROUGH`
<a id="insn-00bdbde8"></a> `00bdbde8` | `10 a2 1e 91` | add x16,x16,#0x7a8 | `FALL_THROUGH`
<a id="insn-00bdbdec"></a> `00bdbdec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbde0`](#insn-00bdbde0) 範囲 `[['00bdbde0', '00bdbdef']]`

## 命令位置別の参照

- [`00bdbde4`](#insn-00bdbde4) → `00c1c7a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdec`](#insn-00bdbdec) → [`00496564`](../00496/00496564.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00496564` · 推定シンボル `_ZN5Botan6BigIntrSEm` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbde4`](#insn-00bdbde4)

~~~json
{
  "source": "00bdbde4",
  "target": "00c1c7a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c7a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbdec`](#insn-00bdbdec)

~~~json
{
  "source": "00bdbdec",
  "target": "00496564",
  "target_space": "ram",
  "resolution": "function"
}
~~~
