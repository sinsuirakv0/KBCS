# 00bdaea0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdaf58`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdaf58.md) · 移動量 `+0xb8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0045.md#compare-ef5b32fa76e5498cb5ebd427bba662b7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaea0",
  "name": "_ZnamSt11align_val_t",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a2b00da2d42b48e594a9c1b5ae3e23e29113eb1a9f3fbeece28090b5ee7e52d5",
  "source_text_sha256": "a2b00da2d42b48e594a9c1b5ae3e23e29113eb1a9f3fbeece28090b5ee7e52d5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdaea0",
        "00bdaea7"
      ]
    ],
    "bytes_sha256": "790013974c6aeb386142c313988f1c708b49fb8172c5e7b63f0c783d3ece8009",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1e20](../00be1/00be1e20.md)

## 呼び出し先

- [00be1e00](../00be1/00be1e00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 75 bytes

~~~c

void _ZnamSt11align_val_t(void)

{
  _ZnwmSt11align_val_t();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdaea0"></a> `00bdaea0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bdaea4"></a> `00bdaea4` | `d7 1b 00 14` | b 0x00be1e00 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdaea0`](#insn-00bdaea0) 範囲 `[['00bdaea0', '00bdaea7']]`

## 命令位置別の参照

- [`00bdaea4`](#insn-00bdaea4) → [`00be1e00`](../00be1/00be1e00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be1e00` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdaea4`](#insn-00bdaea4)

~~~json
{
  "source": "00bdaea4",
  "target": "00be1e00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
