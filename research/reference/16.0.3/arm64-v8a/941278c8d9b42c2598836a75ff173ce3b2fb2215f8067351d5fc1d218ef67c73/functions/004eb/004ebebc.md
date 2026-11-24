# 004ebebc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004ebb9c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004eb/004ebb9c.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/machine_only_observed-0002.md#compare-a8aa1de6eb3e74794c8172366d426f58)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004ebebc",
  "name": "_ZN5Botan5PKCS810BER_encodeERKNS_11Private_KeyE",
  "size": 4,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1b7c384ec0fbd83b6a4156adc49448b65032b682ed55a8d295ff0748818bf585",
  "source_text_sha256": "1b7c384ec0fbd83b6a4156adc49448b65032b682ed55a8d295ff0748818bf585",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004ebebc",
        "004ebebf"
      ]
    ],
    "bytes_sha256": "474f502fc4fa739decd8c6924e3e01c74425161e0658eaf207a0efe31282e2e4",
    "instruction_count": 1,
    "instruction_bytes": 4,
    "body_bytes": 4,
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

## 疑似コード / UTF-8 149 bytes

~~~c

void _ZN5Botan5PKCS810BER_encodeERKNS_11Private_KeyE(void)

{
  (*(code *)PTR__ZNK5Botan11Private_Key16private_key_infoEv_00c9db50)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004ebebc"></a> `004ebebc` | `f1 b9 1d 14` | b 0x00c5a680 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`004ebebc`](#insn-004ebebc) 範囲 `[['004ebebc', '004ebebf']]`
  - `UNCONDITIONAL_JUMP` [`004ebebc`](#insn-004ebebc) → [`00c5a680`](../00c5a/00c5a680.md)

## 命令位置別の参照

- [`004ebebc`](#insn-004ebebc) → [`00c5a680`](../00c5a/00c5a680.md) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `00c5a680` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004ebebc`](#insn-004ebebc)

~~~json
{
  "source": "004ebebc",
  "target": "00c5a680",
  "target_space": "ram",
  "resolution": "function"
}
~~~
