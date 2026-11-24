# 00bffce4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bffc48`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bffc48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/reference_unresolved-0001.md#compare-85a053fc34b4e0db87e8c19245b6d73d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00c00cd8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00c00/00c00cd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/reference_unresolved-0001.md#compare-2c2a0b2852bb19ce75e15e0394080235)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffce4",
  "name": "_ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sgetnEPwl",
  "size": 16,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "83e4a0ea83a0c36edfa89a6d56dc29e760c12c9d64eee60109a084404c8e6a54",
  "source_text_sha256": "83e4a0ea83a0c36edfa89a6d56dc29e760c12c9d64eee60109a084404c8e6a54",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffce4",
        "00bffcf3"
      ]
    ],
    "bytes_sha256": "4661a99447e2b4f582b8d8713238adf75ffc7b54250e90c643e9676dc56aa588",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 298 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIwNS_11char_traitsIwEEE5sgetnEPwl(long *param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bffcf0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*param_1 + 0x40))();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bffce4"></a> `00bffce4` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bffce8"></a> `00bffce8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bffcec"></a> `00bffcec` | `10 21 40 f9` | ldr x16,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00bffcf0"></a> `00bffcf0` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bffce4`](#insn-00bffce4) 範囲 `[['00bffce4', '00bffcf3']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

