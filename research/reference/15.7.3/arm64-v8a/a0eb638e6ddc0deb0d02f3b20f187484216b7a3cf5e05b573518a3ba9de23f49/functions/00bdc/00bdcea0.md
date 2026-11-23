# 00bdcea0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcdf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcdf0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-2d3389a0651f7f8f05d2edc8d2b1b8e2)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcef0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcef0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0005.md#compare-0274388667c9e1c2ec084264e4759284)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcea0",
  "name": "_ZN5Botan14Cert_Extension14Subject_Key_IDC2ERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c6393ccaf501c3ffa9dd65c9e8d1e9f694f872cd050c99001014c04a5e13050b",
  "source_text_sha256": "c6393ccaf501c3ffa9dd65c9e8d1e9f694f872cd050c99001014c04a5e13050b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcea0",
        "00bdceaf"
      ]
    ],
    "bytes_sha256": "0ccb4bc7a4a7ca71e6311c3a5ab402a2f4ef95d7a291e0a2d5c381410c849929",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004ede80](../004ed/004ede80.md)
- [0050a638](../0050a/0050a638.md)

## 呼び出し先

- [004f61e8](../004f6/004f61e8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 456 bytes

~~~c

void _ZN5Botan14Cert_Extension14Subject_Key_IDC2ERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEE
               (void)

{
                    /* try { // try from 00bdcea8 to 00cdcf03 has its CatchHandler @ 00bdcc94 */
  (*(code *)
    PTR__ZN5Botan14Cert_Extension14Subject_Key_IDC2ERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEE_00c1cfe0
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcea0"></a> `00bdcea0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcea4"></a> `00bdcea4` | `11 f2 47 f9` | ldr x17,[x16, #0xfe0] | `FALL_THROUGH`
<a id="insn-00bdcea8"></a> `00bdcea8` | `10 82 3f 91` | add x16,x16,#0xfe0 | `FALL_THROUGH`
<a id="insn-00bdceac"></a> `00bdceac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcea0`](#insn-00bdcea0) 範囲 `[['00bdcea0', '00bdcea7']]`
  - `FALL_THROUGH` [`00bdcea4`](#insn-00bdcea4) → [`00bdcea8`](#insn-00bdcea8)
- ブロック [`00bdcea8`](#insn-00bdcea8) 範囲 `[['00bdcea8', '00bdceaf']]`

## 命令位置別の参照

- [`00bdcea4`](#insn-00bdcea4) → `00c1cfe0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdceac`](#insn-00bdceac) → [`004f61e8`](../004f6/004f61e8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004f61e8` · 推定シンボル `_ZN5Botan14Cert_Extension14Subject_Key_IDC2ERKNSt6__ndk16vectorIhNS2_9allocatorIhEEEERKNS2_12basic_stringIcNS2_11char_traitsIcEENS4_IcEEEE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcea4`](#insn-00bdcea4)

~~~json
{
  "source": "00bdcea4",
  "target": "00c1cfe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cfe0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdceac`](#insn-00bdceac)

~~~json
{
  "source": "00bdceac",
  "target": "004f61e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
