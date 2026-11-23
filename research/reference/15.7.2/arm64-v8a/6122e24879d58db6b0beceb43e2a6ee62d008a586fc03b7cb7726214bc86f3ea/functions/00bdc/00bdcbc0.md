# 00bdcbc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcc70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc70.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-4e3b824d072def65b20d9e9608cc3db6)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcbc0",
  "name": "_ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "542679bd0c9142346da44a44782740d1864b9f0a86160bcf7e9ae37e3416376b",
  "source_text_sha256": "542679bd0c9142346da44a44782740d1864b9f0a86160bcf7e9ae37e3416376b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcbc0",
        "00bdcbcf"
      ]
    ],
    "bytes_sha256": "c01673bd8209e7b19f9d2e0313f2fae68c5598112f37ecce343214e990792eef",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e21a8](../004e2/004e21a8.md)
- [004f27ec](../004f2/004f27ec.md)
- [004fb978](../004fb/004fb978.md)
- [0050a638](../0050a/0050a638.md)
- [0050af44](../0050a/0050af44.md)
- [0050b45c](../0050b/0050b45c.md)
- [005185dc](../00518/005185dc.md)
- [0051a694](../0051a/0051a694.md)
- [0051ac6c](../0051a/0051ac6c.md)

## 呼び出し先

- [004dbf98](../004db/004dbf98.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 720 bytes

~~~c

void _ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_
               (void)

{
                    /* catch() { ... } // from try @ 00bdccc0 with catch @ 00bdcbcc
                       catch() { ... } // from try @ 00bdcde0 with catch @ 00bdcbcc
                       catch() { ... } // from try @ 00bdce58 with catch @ 00bdcbcc
                       catch() { ... } // from try @ 00bdcf2c with catch @ 00bdcbcc
                       catch() { ... } // from try @ 00bdcfb0 with catch @ 00bdcbcc */
  (*(code *)
    PTR__ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9__00c1ce18
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcbc0"></a> `00bdcbc0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcbc4"></a> `00bdcbc4` | `11 0e 47 f9` | ldr x17,[x16, #0xe18] | `FALL_THROUGH`
<a id="insn-00bdcbc8"></a> `00bdcbc8` | `10 62 38 91` | add x16,x16,#0xe18 | `FALL_THROUGH`
<a id="insn-00bdcbcc"></a> `00bdcbcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcbc0`](#insn-00bdcbc0) 範囲 `[['00bdcbc0', '00bdcbcb']]`
  - `FALL_THROUGH` [`00bdcbc8`](#insn-00bdcbc8) → [`00bdcbcc`](#insn-00bdcbcc)
- ブロック [`00bdcbcc`](#insn-00bdcbcc) 範囲 `[['00bdcbcc', '00bdcbcf']]`

## 命令位置別の参照

- [`00bdcbc4`](#insn-00bdcbc4) → `00c1ce18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcbcc`](#insn-00bdcbcc) → [`004dbf98`](../004db/004dbf98.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004dbf98` · 推定シンボル `_ZN5Botan15AlternativeNameC1ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_S9_S9_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcbc4`](#insn-00bdcbc4)

~~~json
{
  "source": "00bdcbc4",
  "target": "00c1ce18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcbcc`](#insn-00bdcbcc)

~~~json
{
  "source": "00bdcbcc",
  "target": "004dbf98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
