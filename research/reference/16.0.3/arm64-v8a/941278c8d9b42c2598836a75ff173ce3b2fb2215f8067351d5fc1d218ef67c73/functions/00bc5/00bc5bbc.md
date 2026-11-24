# 00bc5bbc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bc4bc8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bc4/00bc4bc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/detail_skipped-0006.md#compare-a081d357e5b01eb01a09cdda1b1e7a99)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc5bbc",
  "name": "_ZNK8firebase13remote_config8internal20RemoteConfigInternal11InitializedEv",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "764e26167b4431b9a1e02d10842c7068e6e4b96622bb95044d19dc2f656452c3",
  "source_text_sha256": "764e26167b4431b9a1e02d10842c7068e6e4b96622bb95044d19dc2f656452c3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc5bbc",
        "00bc5bcb"
      ]
    ],
    "bytes_sha256": "8528ae01b10b6da611a36e7457d9c7c90456f384f6e0817e1c6341750ebc1384",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e930](../00c5e/00c5e930.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 143 bytes

~~~c

bool _ZNK8firebase13remote_config8internal20RemoteConfigInternal11InitializedEv(long param_1)

{
  return *(long *)(param_1 + 0x198) != 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc5bbc"></a> `00bc5bbc` | `08 cc 40 f9` | ldr x8,[x0, #0x198] | `FALL_THROUGH`
<a id="insn-00bc5bc0"></a> `00bc5bc0` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00bc5bc4"></a> `00bc5bc4` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00bc5bc8"></a> `00bc5bc8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc5bbc`](#insn-00bc5bbc) 範囲 `[['00bc5bbc', '00bc5bcb']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

