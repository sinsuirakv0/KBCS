# 00bddfc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bde070`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde070.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-2ee880bd272f122f2d00331490763a5d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddfc0",
  "name": "_ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "136985cc0a24462147817563c8f6a8c0e0664998b92359c9c5eb7bc55db38684",
  "source_text_sha256": "136985cc0a24462147817563c8f6a8c0e0664998b92359c9c5eb7bc55db38684",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddfc0",
        "00bddfcf"
      ]
    ],
    "bytes_sha256": "389dee89522a5ed6b6e25e72f2df3b082934224054d9c32bc6fd86cd0396748c",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae2b00](../00ae2/00ae2b00.md)
- [00ae2ec8](../00ae2/00ae2ec8.md)
- [00b4d40c](../00b4d/00b4d40c.md)
- [00b4d9b0](../00b4d/00b4d9b0.md)
- [00b4dd3c](../00b4d/00b4dd3c.md)
- [00b4e378](../00b4e/00b4e378.md)
- [00b563e8](../00b56/00b563e8.md)
- [00b56714](../00b56/00b56714.md)
- [00b56a40](../00b56/00b56a40.md)
- [00b56d6c](../00b56/00b56d6c.md)
- [00b57094](../00b57/00b57094.md)
- [00b5732c](../00b57/00b5732c.md)
- [00b57a40](../00b57/00b57a40.md)
- [00b57ffc](../00b57/00b57ffc.md)
- [00b5e17c](../00b5e/00b5e17c.md)
- [00b5e694](../00b5e/00b5e694.md)
- [00b5eaa8](../00b5e/00b5eaa8.md)
- [00b5ee5c](../00b5e/00b5ee5c.md)
- [00b5f0cc](../00b5f/00b5f0cc.md)
- [00b5f258](../00b5f/00b5f258.md)
- [00b5f4e4](../00b5f/00b5f4e4.md)
- [00b5fa7c](../00b5f/00b5fa7c.md)
- [00b6be60](../00b6b/00b6be60.md)
- [00b6c444](../00b6c/00b6c444.md)
- [00b6c71c](../00b6c/00b6c71c.md)
- [00b6ede4](../00b6e/00b6ede4.md)
- [00b6fd1c](../00b6f/00b6fd1c.md)
- [00b6ff44](../00b6f/00b6ff44.md)
- [00b7036c](../00b70/00b7036c.md)
- [00b705c8](../00b70/00b705c8.md)
- [00b707d0](../00b70/00b707d0.md)
- [00b70a1c](../00b70/00b70a1c.md)
- [00b70c0c](../00b70/00b70c0c.md)
- [00b70e04](../00b70/00b70e04.md)
- [00b71060](../00b71/00b71060.md)
- [00b71250](../00b71/00b71250.md)
- [00b71478](../00b71/00b71478.md)

## 呼び出し先

- [00af5bec](../00af5/00af5bec.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 285 bytes

~~~c

void _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
               (void)

{
  (*(code *)
    PTR__ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7__00c1d818
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddfc0"></a> `00bddfc0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddfc4"></a> `00bddfc4` | `11 0e 44 f9` | ldr x17,[x16, #0x818] | `FALL_THROUGH`
<a id="insn-00bddfc8"></a> `00bddfc8` | `10 62 20 91` | add x16,x16,#0x818 | `FALL_THROUGH`
<a id="insn-00bddfcc"></a> `00bddfcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddfc0`](#insn-00bddfc0) 範囲 `[['00bddfc0', '00bddfcf']]`

## 命令位置別の参照

- [`00bddfc4`](#insn-00bddfc4) → `00c1d818`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddfcc`](#insn-00bddfcc) → [`00af5bec`](../00af5/00af5bec.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00af5bec` · 推定シンボル `_ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddfc4`](#insn-00bddfc4)

~~~json
{
  "source": "00bddfc4",
  "target": "00c1d818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d818",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddfcc`](#insn-00bddfcc)

~~~json
{
  "source": "00bddfcc",
  "target": "00af5bec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
