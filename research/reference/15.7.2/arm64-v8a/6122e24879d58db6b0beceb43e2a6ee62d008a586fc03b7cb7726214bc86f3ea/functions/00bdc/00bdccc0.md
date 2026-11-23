# 00bdccc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcd70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd70.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-493e393c85a50c041bf934c29d8de6a2)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdccc0",
  "name": "_ZNK5Botan16X509_Certificate23load_subject_public_keyEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ea4a5abd34ad1d84e91d79072aa95e8753af1f8ff9e294a1c85f49c9822c8f9f",
  "source_text_sha256": "ea4a5abd34ad1d84e91d79072aa95e8753af1f8ff9e294a1c85f49c9822c8f9f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdccc0",
        "00bdcccf"
      ]
    ],
    "bytes_sha256": "663ec6fd4f02ab237f08f19a81d43c7530fdeec958e610e635114330152543d5",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e85ec](../004e8/004e85ec.md)
- [00501b08](../00501/00501b08.md)
- [00503af8](../00503/00503af8.md)
- [005054cc](../00505/005054cc.md)

## 呼び出し先

- [00500f10](../00500/00500f10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 266 bytes

~~~c

void _ZNK5Botan16X509_Certificate23load_subject_public_keyEv(void)

{
                    /* try { // try from 00bdccc0 to 00cdcdc7 has its CatchHandler @ 00bdcbcc */
  (*(code *)PTR__ZNK5Botan16X509_Certificate23load_subject_public_keyEv_00c1ce98)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdccc0"></a> `00bdccc0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdccc4"></a> `00bdccc4` | `11 4e 47 f9` | ldr x17,[x16, #0xe98] | `FALL_THROUGH`
<a id="insn-00bdccc8"></a> `00bdccc8` | `10 62 3a 91` | add x16,x16,#0xe98 | `FALL_THROUGH`
<a id="insn-00bdcccc"></a> `00bdcccc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdccc0`](#insn-00bdccc0) 範囲 `[['00bdccc0', '00bdcccf']]`

## 命令位置別の参照

- [`00bdccc4`](#insn-00bdccc4) → `00c1ce98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcccc`](#insn-00bdcccc) → [`00500f10`](../00500/00500f10.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00500f10` · 推定シンボル `_ZNK5Botan16X509_Certificate23load_subject_public_keyEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdccc4`](#insn-00bdccc4)

~~~json
{
  "source": "00bdccc4",
  "target": "00c1ce98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce98",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcccc`](#insn-00bdcccc)

~~~json
{
  "source": "00bdcccc",
  "target": "00500f10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
