# 00bdbbc0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbc70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc70.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-1d6f9ff49258f4e6302ac2899cb4a64d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbc0",
  "name": "_ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "25eedfb0cac24fe1adaae3a9cfa9adca384e16b686938468d9dfed8700b13c43",
  "source_text_sha256": "25eedfb0cac24fe1adaae3a9cfa9adca384e16b686938468d9dfed8700b13c43",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbbc0",
        "00bdbbcf"
      ]
    ],
    "bytes_sha256": "10e205378ca1258239718c5c5bdab784b947e03eb2e7e01a581aa98c974c12ec",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048fe68](../0048f/0048fe68.md)
- [0049025c](../00490/0049025c.md)
- [00490480](../00490/00490480.md)
- [0049f624](../0049f/0049f624.md)
- [004bf57c](../004bf/004bf57c.md)
- [004c73c4](../004c7/004c73c4.md)
- [004ccf4c](../004cc/004ccf4c.md)
- [004cf1d8](../004cf/004cf1d8.md)
- [004cf634](../004cf/004cf634.md)
- [004e0734](../004e0/004e0734.md)
- [004e6aac](../004e6/004e6aac.md)
- [004e9d4c](../004e9/004e9d4c.md)
- [004ee7d8](../004ee/004ee7d8.md)
- [004ef204](../004ef/004ef204.md)
- [004f5078](../004f5/004f5078.md)
- [004fa9b0](../004fa/004fa9b0.md)
- [004faccc](../004fa/004faccc.md)
- [0050b45c](../0050b/0050b45c.md)

## 呼び出し先

- [0048ff2c](../0048f/0048ff2c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 177 bytes

~~~c

void _ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_(void)

{
  (*(code *)PTR__ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4__00c1c618)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbbc0"></a> `00bdbbc0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbbc4"></a> `00bdbbc4` | `11 0e 43 f9` | ldr x17,[x16, #0x618] | `FALL_THROUGH`
<a id="insn-00bdbbc8"></a> `00bdbbc8` | `10 62 18 91` | add x16,x16,#0x618 | `FALL_THROUGH`
<a id="insn-00bdbbcc"></a> `00bdbbcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbbc0`](#insn-00bdbbc0) 範囲 `[['00bdbbc0', '00bdbbcf']]`

## 命令位置別の参照

- [`00bdbbc4`](#insn-00bdbbc4) → `00c1c618`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbcc`](#insn-00bdbbcc) → [`0048ff2c`](../0048f/0048ff2c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `0048ff2c` · 推定シンボル `_ZN5Botan11DER_Encoder6encodeERKNS_6BigIntENS_8ASN1_TagES4_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbbc4`](#insn-00bdbbc4)

~~~json
{
  "source": "00bdbbc4",
  "target": "00c1c618",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c618",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbbcc`](#insn-00bdbbcc)

~~~json
{
  "source": "00bdbbcc",
  "target": "0048ff2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
