# 00bdbdb0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbe60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe60.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-01be651832264cadbcddf7137ed33027)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbdb0",
  "name": "_ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "52572f4c9276568c177464f703d1213e83d36b48c6ec567d96776bce8273c19f",
  "source_text_sha256": "52572f4c9276568c177464f703d1213e83d36b48c6ec567d96776bce8273c19f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbdb0",
        "00bdbdbf"
      ]
    ],
    "bytes_sha256": "d82c882184d9a879da171abf53764d206d03217c077188a47c32f12d2bcc32b2",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004b5c14](../004b5/004b5c14.md)
- [005141ac](../00514/005141ac.md)

## 呼び出し先

- [00497bf4](../00497/00497bf4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 197 bytes

~~~c

void _ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4_(void)

{
  (*(code *)PTR__ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4__00c1c710)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbdb0"></a> `00bdbdb0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbdb4"></a> `00bdbdb4` | `11 8a 43 f9` | ldr x17,[x16, #0x710] | `FALL_THROUGH`
<a id="insn-00bdbdb8"></a> `00bdbdb8` | `10 42 1c 91` | add x16,x16,#0x710 | `FALL_THROUGH`
<a id="insn-00bdbdbc"></a> `00bdbdbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbdb0`](#insn-00bdbdb0) 範囲 `[['00bdbdb0', '00bdbdbf']]`

## 命令位置別の参照

- [`00bdbdb4`](#insn-00bdbdb4) → `00c1c710`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdbc`](#insn-00bdbdbc) → [`00497bf4`](../00497/00497bf4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00497bf4` · 推定シンボル `_ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbdb4`](#insn-00bdbdb4)

~~~json
{
  "source": "00bdbdb4",
  "target": "00c1c710",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c710",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbdbc`](#insn-00bdbdbc)

~~~json
{
  "source": "00bdbdbc",
  "target": "00497bf4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
