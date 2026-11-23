# 00bdbbe0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbb30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbb30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-66034a554436ea6bd50f5be6e72b49f8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbc30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbc30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/alignment_unresolved-0004.md#compare-927b422bf3cd76bae178dc97b031825f)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbe0",
  "name": "_ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEENS_8ASN1_TagES7_S7_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f61ca84977f8552b4759cae577718f6b6861b2de17020a651ab17063cd4368fd",
  "source_text_sha256": "f61ca84977f8552b4759cae577718f6b6861b2de17020a651ab17063cd4368fd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbbe0",
        "00bdbbef"
      ]
    ],
    "bytes_sha256": "144a2bb12907d8f59989673b9d3b0c9e19cd008708d58ec41bab1ebbae6bd9d2",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048ddf0](../0048d/0048ddf0.md)
- [004c05ec](../004c0/004c05ec.md)
- [004c9e38](../004c9/004c9e38.md)
- [00513c60](../00513/00513c60.md)

## 呼び出し先

- [0048e994](../0048e/0048e994.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 362 bytes

~~~c

void _ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEENS_8ASN1_TagES7_S7_
               (void)

{
                    /* catch() { ... } // from try @ 00bdbdc0 with catch @ 00bdbbe4 */
  (*(code *)
    PTR__ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEENS_8ASN1_TagES7_S7__00c1c680
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbbe0"></a> `00bdbbe0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbbe4"></a> `00bdbbe4` | `11 42 43 f9` | ldr x17,[x16, #0x680] | `FALL_THROUGH`
<a id="insn-00bdbbe8"></a> `00bdbbe8` | `10 02 1a 91` | add x16,x16,#0x680 | `FALL_THROUGH`
<a id="insn-00bdbbec"></a> `00bdbbec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbbe0`](#insn-00bdbbe0) 範囲 `[['00bdbbe0', '00bdbbe3']]`
  - `FALL_THROUGH` [`00bdbbe0`](#insn-00bdbbe0) → [`00bdbbe4`](#insn-00bdbbe4)
- ブロック [`00bdbbe4`](#insn-00bdbbe4) 範囲 `[['00bdbbe4', '00bdbbef']]`

## 命令位置別の参照

- [`00bdbbe4`](#insn-00bdbbe4) → `00c1c680`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbec`](#insn-00bdbbec) → [`0048e994`](../0048e/0048e994.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048e994` · 推定シンボル `_ZN5Botan11BER_Decoder6decodeERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEENS_8ASN1_TagES7_S7_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbbe4`](#insn-00bdbbe4)

~~~json
{
  "source": "00bdbbe4",
  "target": "00c1c680",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c680",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbbec`](#insn-00bdbbec)

~~~json
{
  "source": "00bdbbec",
  "target": "0048e994",
  "target_space": "ram",
  "resolution": "function"
}
~~~
