# 00bdcbe0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcc90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcc90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0006.md#compare-cf5785c934712bc04a288867e0298f68)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcbe0",
  "name": "_ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9518b6fcba3eb24c2c97d7883890d8b6e84939f9ea5f39041dd3977f4506f4f1",
  "source_text_sha256": "9518b6fcba3eb24c2c97d7883890d8b6e84939f9ea5f39041dd3977f4506f4f1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcbe0",
        "00bdcbef"
      ]
    ],
    "bytes_sha256": "2048e101f97426e9254192ee1e151b7342c2a8fc24b55f0f3aec20c159ca7679",
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
- [0050b45c](../0050b/0050b45c.md)

## 呼び出し先

- [004e3024](../004e3/004e3024.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 269 bytes

~~~c

void _ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE
               (void)

{
  (*(code *)
    PTR__ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE_00c1ce28
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcbe0"></a> `00bdcbe0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcbe4"></a> `00bdcbe4` | `11 16 47 f9` | ldr x17,[x16, #0xe28] | `FALL_THROUGH`
<a id="insn-00bdcbe8"></a> `00bdcbe8` | `10 a2 38 91` | add x16,x16,#0xe28 | `FALL_THROUGH`
<a id="insn-00bdcbec"></a> `00bdcbec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcbe0`](#insn-00bdcbe0) 範囲 `[['00bdcbe0', '00bdcbef']]`

## 命令位置別の参照

- [`00bdcbe4`](#insn-00bdcbe4) → `00c1ce28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcbec`](#insn-00bdcbec) → [`004e3024`](../004e3/004e3024.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e3024` · 推定シンボル `_ZN5Botan42verify_cert_constraints_valid_for_key_typeERKNS_10Public_KeyENS_15Key_ConstraintsE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcbe4`](#insn-00bdcbe4)

~~~json
{
  "source": "00bdcbe4",
  "target": "00c1ce28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcbec`](#insn-00bdcbec)

~~~json
{
  "source": "00bdcbec",
  "target": "004e3024",
  "target_space": "ram",
  "resolution": "function"
}
~~~
