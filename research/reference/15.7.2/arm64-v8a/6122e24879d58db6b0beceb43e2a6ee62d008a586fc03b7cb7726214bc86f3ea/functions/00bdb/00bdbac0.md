# 00bdbac0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbb70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb70.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-469829456bcf07f92525d92743089efc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbac0",
  "name": "_ZNSt6__ndk16chrono12system_clock11from_time_tEl",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "000dceaec71577e049648abcd0949856b85fe6c15756b023cb3b1705b3fc7550",
  "source_text_sha256": "000dceaec71577e049648abcd0949856b85fe6c15756b023cb3b1705b3fc7550",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbac0",
        "00bdbacf"
      ]
    ],
    "bytes_sha256": "1d8b9e35f2a5ddda13c4208a0d923fa66daadab454d02b6cd2c528a04b5bdac4",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048c2e0](../0048c/0048c2e0.md)

## 呼び出し先

- [00b728b8](../00b72/00b728b8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 155 bytes

~~~c

void _ZNSt6__ndk16chrono12system_clock11from_time_tEl(void)

{
  (*(code *)PTR__ZNSt6__ndk16chrono12system_clock11from_time_tEl_00c1c598)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbac0"></a> `00bdbac0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbac4"></a> `00bdbac4` | `11 ce 42 f9` | ldr x17,[x16, #0x598] | `FALL_THROUGH`
<a id="insn-00bdbac8"></a> `00bdbac8` | `10 62 16 91` | add x16,x16,#0x598 | `FALL_THROUGH`
<a id="insn-00bdbacc"></a> `00bdbacc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbac0`](#insn-00bdbac0) 範囲 `[['00bdbac0', '00bdbacf']]`

## 命令位置別の参照

- [`00bdbac4`](#insn-00bdbac4) → `00c1c598`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbacc`](#insn-00bdbacc) → [`00b728b8`](../00b72/00b728b8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b728b8` · 推定シンボル `_ZNSt6__ndk16chrono12system_clock11from_time_tEl` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbac4`](#insn-00bdbac4)

~~~json
{
  "source": "00bdbac4",
  "target": "00c1c598",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c598",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbacc`](#insn-00bdbacc)

~~~json
{
  "source": "00bdbacc",
  "target": "00b728b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
