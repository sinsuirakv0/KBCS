# 00badd1c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00badde4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bad/00badde4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0024.md#compare-8cd99cd9acead9b93adf273140d9452f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00badd1c",
  "name": "_ZNKSt6__ndk115__codecvt_utf16IwLb1EE13do_max_lengthEv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c576fe512f5773049e5eb747299a130e78932f72f5526c854a9257f40724ba7c",
  "source_text_sha256": "c576fe512f5773049e5eb747299a130e78932f72f5526c854a9257f40724ba7c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00badd1c",
        "00badd37"
      ]
    ],
    "bytes_sha256": "ea1d8dd57a36c95e9091b58a001224082a8827e6f30525bf1571408bdf74121e",
    "instruction_count": 7,
    "instruction_bytes": 28,
    "body_bytes": 28,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 204 bytes

~~~c

undefined4 _ZNKSt6__ndk115__codecvt_utf16IwLb1EE13do_max_lengthEv(long param_1)

{
  undefined4 uVar1;
  
  uVar1 = 4;
  if ((*(byte *)(param_1 + 0x20) & 4) != 0) {
    uVar1 = 6;
  }
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00badd1c"></a> `00badd1c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00badd20"></a> `00badd20` | `09 80 40 39` | ldrb w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00badd24"></a> `00badd24` | `c8 00 80 52` | mov w8,#0x6 | `FALL_THROUGH`
<a id="insn-00badd28"></a> `00badd28` | `3f 01 1e 72` | tst w9,#0x4 | `FALL_THROUGH`
<a id="insn-00badd2c"></a> `00badd2c` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00badd30"></a> `00badd30` | `20 01 88 1a` | csel w0,w9,w8,eq | `FALL_THROUGH`
<a id="insn-00badd34"></a> `00badd34` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00badd1c`](#insn-00badd1c) 範囲 `[['00badd1c', '00badd37']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

