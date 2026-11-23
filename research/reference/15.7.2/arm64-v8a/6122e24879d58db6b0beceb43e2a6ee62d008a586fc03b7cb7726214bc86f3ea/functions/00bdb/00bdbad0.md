# 00bdbad0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbb80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-7a8894e59cc92419b90360efe189a486)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbad0",
  "name": "_ZN5Botan11BER_Decoder10verify_endEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "08b11d317529a2d8691ced8a395ca39ecddec42c2e32f1cf42f8d8df849b1c00",
  "source_text_sha256": "08b11d317529a2d8691ced8a395ca39ecddec42c2e32f1cf42f8d8df849b1c00",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbad0",
        "00bdbadf"
      ]
    ],
    "bytes_sha256": "b4d3cdd4c84be49bfe164eb88af6f398184b507f3773f61f1e276f10b9c7fe38",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004c05ec](../004c0/004c05ec.md)
- [004c13f0](../004c1/004c13f0.md)
- [004c15a4](../004c1/004c15a4.md)
- [004dcf48](../004dc/004dcf48.md)
- [004e7c0c](../004e7/004e7c0c.md)
- [004e7de0](../004e7/004e7de0.md)
- [004e82ac](../004e8/004e82ac.md)
- [004ea2b0](../004ea/004ea2b0.md)
- [004eb16c](../004eb/004eb16c.md)
- [004f03d8](../004f0/004f03d8.md)
- [004f4778](../004f4/004f4778.md)
- [004f4ba8](../004f4/004f4ba8.md)
- [004f603c](../004f6/004f603c.md)
- [004fb0d8](../004fb/004fb0d8.md)
- [004fbe1c](../004fb/004fbe1c.md)
- [004fdfd8](../004fd/004fdfd8.md)
- [00513c60](../00513/00513c60.md)

## 呼び出し先

- [0048c9bc](../0048c/0048c9bc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 131 bytes

~~~c

void _ZN5Botan11BER_Decoder10verify_endEv(void)

{
  (*(code *)PTR__ZN5Botan11BER_Decoder10verify_endEv_00c1c5a0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbad0"></a> `00bdbad0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbad4"></a> `00bdbad4` | `11 d2 42 f9` | ldr x17,[x16, #0x5a0] | `FALL_THROUGH`
<a id="insn-00bdbad8"></a> `00bdbad8` | `10 82 16 91` | add x16,x16,#0x5a0 | `FALL_THROUGH`
<a id="insn-00bdbadc"></a> `00bdbadc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbad0`](#insn-00bdbad0) 範囲 `[['00bdbad0', '00bdbadf']]`

## 命令位置別の参照

- [`00bdbad4`](#insn-00bdbad4) → `00c1c5a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbadc`](#insn-00bdbadc) → [`0048c9bc`](../0048c/0048c9bc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048c9bc` · 推定シンボル `_ZN5Botan11BER_Decoder10verify_endEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbad4`](#insn-00bdbad4)

~~~json
{
  "source": "00bdbad4",
  "target": "00c1c5a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c5a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbadc`](#insn-00bdbadc)

~~~json
{
  "source": "00bdbadc",
  "target": "0048c9bc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
