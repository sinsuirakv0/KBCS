# 00baece0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00baeda8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bae/00baeda8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/detail_skipped-0024.md#compare-9bb2e9c2c58c43e02ef9d8a71cf83a29)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baece0",
  "name": "_ZNKSt6__ndk120__codecvt_utf8_utf16IDsE13do_max_lengthEv",
  "size": 28,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "da5a424c7b74816960d92f78e8c319b2b1b75a45fbe465f432da523cb6a7b040",
  "source_text_sha256": "da5a424c7b74816960d92f78e8c319b2b1b75a45fbe465f432da523cb6a7b040",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baece0",
        "00baecfb"
      ]
    ],
    "bytes_sha256": "adc1de3f95a0fc13bbae1fe920a8bbfd2f620bc6861cad58fc4d35ada03be607",
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

## 疑似コード / UTF-8 206 bytes

~~~c

undefined4 _ZNKSt6__ndk120__codecvt_utf8_utf16IDsE13do_max_lengthEv(long param_1)

{
  undefined4 uVar1;
  
  uVar1 = 4;
  if ((*(byte *)(param_1 + 0x18) & 4) != 0) {
    uVar1 = 7;
  }
  return uVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baece0"></a> `00baece0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00baece4"></a> `00baece4` | `09 60 40 39` | ldrb w9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00baece8"></a> `00baece8` | `e8 00 80 52` | mov w8,#0x7 | `FALL_THROUGH`
<a id="insn-00baecec"></a> `00baecec` | `3f 01 1e 72` | tst w9,#0x4 | `FALL_THROUGH`
<a id="insn-00baecf0"></a> `00baecf0` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00baecf4"></a> `00baecf4` | `20 01 88 1a` | csel w0,w9,w8,eq | `FALL_THROUGH`
<a id="insn-00baecf8"></a> `00baecf8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baece0`](#insn-00baece0) 範囲 `[['00baece0', '00baecfb']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

