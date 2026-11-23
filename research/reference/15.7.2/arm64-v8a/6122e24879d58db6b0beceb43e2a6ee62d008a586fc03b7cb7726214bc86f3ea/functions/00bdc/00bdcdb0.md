# 00bdcdb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdce60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-73d668272634e3a6e3e77498c8f11368)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcdb0",
  "name": "_ZNK5Botan14PKCS10_Request5is_CAEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fbb9075479c1f020ca08a639ff178b61db03f0253161b4b113c921a0767b237d",
  "source_text_sha256": "fbb9075479c1f020ca08a639ff178b61db03f0253161b4b113c921a0767b237d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcdb0",
        "00bdcdbf"
      ]
    ],
    "bytes_sha256": "e9fc084a77bb70dada2c0b33ca5c9455a1e5891620749650ead7f02092137118",
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

## 呼び出し先

- [004ec73c](../004ec/004ec73c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 127 bytes

~~~c

void _ZNK5Botan14PKCS10_Request5is_CAEv(void)

{
  (*(code *)PTR__ZNK5Botan14PKCS10_Request5is_CAEv_00c1cf10)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcdb0"></a> `00bdcdb0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcdb4"></a> `00bdcdb4` | `11 8a 47 f9` | ldr x17,[x16, #0xf10] | `FALL_THROUGH`
<a id="insn-00bdcdb8"></a> `00bdcdb8` | `10 42 3c 91` | add x16,x16,#0xf10 | `FALL_THROUGH`
<a id="insn-00bdcdbc"></a> `00bdcdbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcdb0`](#insn-00bdcdb0) 範囲 `[['00bdcdb0', '00bdcdbf']]`

## 命令位置別の参照

- [`00bdcdb4`](#insn-00bdcdb4) → `00c1cf10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcdbc`](#insn-00bdcdbc) → [`004ec73c`](../004ec/004ec73c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004ec73c` · 推定シンボル `_ZNK5Botan14PKCS10_Request5is_CAEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcdb4`](#insn-00bdcdb4)

~~~json
{
  "source": "00bdcdb4",
  "target": "00c1cf10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf10",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcdbc`](#insn-00bdcdbc)

~~~json
{
  "source": "00bdcdbc",
  "target": "004ec73c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
