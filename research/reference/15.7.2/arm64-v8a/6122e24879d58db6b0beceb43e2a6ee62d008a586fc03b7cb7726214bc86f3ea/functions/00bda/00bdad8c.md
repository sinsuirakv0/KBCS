# 00bdad8c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdae4c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bda/00bdae4c.md) · 移動量 `+0xc0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-c455b3f7d3d5a9f38afc1cb1a5d4f541)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdad8c",
  "name": "FUN_00bdad8c",
  "size": 8,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "db215d7a83bb93635bedcc20f9e1744dccb3ebeec04a25fedb164591499feece",
  "source_text_sha256": "db215d7a83bb93635bedcc20f9e1744dccb3ebeec04a25fedb164591499feece",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdad8c",
        "00bdad93"
      ]
    ],
    "bytes_sha256": "b2e329668519cea45a5cbbe101b0b6e3220be3d188a350ede60284739f2a9636",
    "instruction_count": 2,
    "instruction_bytes": 8,
    "body_bytes": 8,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [009613bc](../00961/009613bc.md)

## 呼び出し先

- [00963004](../00963/00963004.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 146 bytes

~~~c

void FUN_00bdad8c(void)

{
                    /* catch() { ... } // from try @ 00bdad04 with catch @ 00bdad8c */
  FUN_00963004();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdad8c"></a> `00bdad8c` | `29 d9 42 f9` | ldr x9,[x9, #0x5b0] | `FALL_THROUGH`
<a id="insn-00bdad90"></a> `00bdad90` | `9d 20 f6 17` | b 0x00963004 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdad8c`](#insn-00bdad8c) 範囲 `[['00bdad8c', '00bdad93']]`

## 命令位置別の参照

- [`00bdad90`](#insn-00bdad90) → [`00963004`](../00963/00963004.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00963004` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdad90`](#insn-00bdad90)

~~~json
{
  "source": "00bdad90",
  "target": "00963004",
  "target_space": "ram",
  "resolution": "function"
}
~~~
