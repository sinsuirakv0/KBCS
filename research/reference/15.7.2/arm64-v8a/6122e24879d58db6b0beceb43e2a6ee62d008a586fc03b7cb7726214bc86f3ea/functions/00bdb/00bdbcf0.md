# 00bdbcf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbda0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbda0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-f22cf87cb8d3451b97785c449ceaa2cc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbcf0",
  "name": "_ZN5Botan6BigIntmIERKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "714be60cc442fbaae70fdea8f72a509381e6fa34954e094348ae2d543f1e1f5d",
  "source_text_sha256": "714be60cc442fbaae70fdea8f72a509381e6fa34954e094348ae2d543f1e1f5d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbcf0",
        "00bdbcff"
      ]
    ],
    "bytes_sha256": "255eeb5e59c18736f1aec26cd94d9cfee74df01555f0a5f22ce3e2cd6a40c294",
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
- [004989ec](../00498/004989ec.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8aa0](../004b8/004b8aa0.md)
- [004b8bd8](../004b8/004b8bd8.md)
- [004b8e58](../004b8/004b8e58.md)
- [004ba430](../004ba/004ba430.md)
- [004bcf24](../004bc/004bcf24.md)
- [004be0f4](../004be/004be0f4.md)

## 呼び出し先

- [00495e3c](../00495/00495e3c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 204 bytes

~~~c

void _ZN5Botan6BigIntmIERKS0_(void)

{
                    /* try { // try from 00bdbcf8 to 00cdbf53 has its CatchHandler @ 00bdbb1c */
  (*(code *)PTR__ZN5Botan6BigIntmIERKS0__00c1c6b0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbcf0"></a> `00bdbcf0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbcf4"></a> `00bdbcf4` | `11 5a 43 f9` | ldr x17,[x16, #0x6b0] | `FALL_THROUGH`
<a id="insn-00bdbcf8"></a> `00bdbcf8` | `10 c2 1a 91` | add x16,x16,#0x6b0 | `FALL_THROUGH`
<a id="insn-00bdbcfc"></a> `00bdbcfc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbcf0`](#insn-00bdbcf0) 範囲 `[['00bdbcf0', '00bdbcf7']]`
  - `FALL_THROUGH` [`00bdbcf4`](#insn-00bdbcf4) → [`00bdbcf8`](#insn-00bdbcf8)
- ブロック [`00bdbcf8`](#insn-00bdbcf8) 範囲 `[['00bdbcf8', '00bdbcff']]`

## 命令位置別の参照

- [`00bdbcf4`](#insn-00bdbcf4) → `00c1c6b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcfc`](#insn-00bdbcfc) → [`00495e3c`](../00495/00495e3c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00495e3c` · 推定シンボル `_ZN5Botan6BigIntmIERKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbcf4`](#insn-00bdbcf4)

~~~json
{
  "source": "00bdbcf4",
  "target": "00c1c6b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c6b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbcfc`](#insn-00bdbcfc)

~~~json
{
  "source": "00bdbcfc",
  "target": "00495e3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
