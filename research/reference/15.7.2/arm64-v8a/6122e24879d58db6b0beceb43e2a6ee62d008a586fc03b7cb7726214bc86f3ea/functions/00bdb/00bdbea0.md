# 00bdbea0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbf50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbf50.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-ebed13a8f8d92d79e3a2230509fb502c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbea0",
  "name": "_ZN5Botan12HashFunction6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "23d8834e5c77c0768c7bf27e1abf2b2629f95986edf8dc95df3553f2cd91554d",
  "source_text_sha256": "23d8834e5c77c0768c7bf27e1abf2b2629f95986edf8dc95df3553f2cd91554d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbea0",
        "00bdbeaf"
      ]
    ],
    "bytes_sha256": "f118bf6a6c7086d3fb2e96e9b086098ce5f2d0e3016c6fd91d6ab6b80e3b5d08",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0049e24c](../0049e/0049e24c.md)
- [004a19c4](../004a1/004a19c4.md)
- [004a9174](../004a9/004a9174.md)
- [004ab3f4](../004ab/004ab3f4.md)
- [004c3c00](../004c3/004c3c00.md)
- [004def78](../004de/004def78.md)
- [004df290](../004df/004df290.md)
- [004e939c](../004e9/004e939c.md)
- [004fdfd8](../004fd/004fdfd8.md)
- [00501274](../00501/00501274.md)
- [0055f8e0](../0055f/0055f8e0.md)

## 呼び出し先

- [0049e3f4](../0049e/0049e3f4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 289 bytes

~~~c

void _ZN5Botan12HashFunction6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_
               (void)

{
  (*(code *)
    PTR__ZN5Botan12HashFunction6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9__00c1c788
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbea0"></a> `00bdbea0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbea4"></a> `00bdbea4` | `11 c6 43 f9` | ldr x17,[x16, #0x788] | `FALL_THROUGH`
<a id="insn-00bdbea8"></a> `00bdbea8` | `10 22 1e 91` | add x16,x16,#0x788 | `FALL_THROUGH`
<a id="insn-00bdbeac"></a> `00bdbeac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbea0`](#insn-00bdbea0) 範囲 `[['00bdbea0', '00bdbeaf']]`

## 命令位置別の参照

- [`00bdbea4`](#insn-00bdbea4) → `00c1c788`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbeac`](#insn-00bdbeac) → [`0049e3f4`](../0049e/0049e3f4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0049e3f4` · 推定シンボル `_ZN5Botan12HashFunction6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbea4`](#insn-00bdbea4)

~~~json
{
  "source": "00bdbea4",
  "target": "00c1c788",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c788",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbeac`](#insn-00bdbeac)

~~~json
{
  "source": "00bdbeac",
  "target": "0049e3f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
