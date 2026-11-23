# 00b7ebcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b7ec94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b7e/00b7ec94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0043.md#compare-09a44a7667addeec86ee8be461beaa29)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7ebcc",
  "name": "_ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev",
  "size": 8,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7aad78d5ee02cd9a543a3b578a4fbc03a1974e4f9f0c76a3d883e486885d4b06",
  "source_text_sha256": "7aad78d5ee02cd9a543a3b578a4fbc03a1974e4f9f0c76a3d883e486885d4b06",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7ebcc",
        "00b7ebd3"
      ]
    ],
    "bytes_sha256": "da93580e93d2e6cc4a188da0c68f3038218a209cdbfbeebb7a354f29f117998b",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdb070](../00bdb/00bdb070.md)
- [00be1240](../00be1/00be1240.md)

## 呼び出し先

- [00be00e0](../00be0/00be00e0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 109 bytes

~~~c

void _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(void)

{
  _ZNSt6__ndk18ios_baseD1Ev();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7ebcc"></a> `00b7ebcc` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00b7ebd0"></a> `00b7ebd0` | `44 85 01 14` | b 0x00be00e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7ebcc`](#insn-00b7ebcc) 範囲 `[['00b7ebcc', '00b7ebd3']]`

## 命令位置別の参照

- [`00b7ebd0`](#insn-00b7ebd0) → [`00be00e0`](../00be0/00be00e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be00e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7ebd0`](#insn-00b7ebd0)

~~~json
{
  "source": "00b7ebd0",
  "target": "00be00e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
