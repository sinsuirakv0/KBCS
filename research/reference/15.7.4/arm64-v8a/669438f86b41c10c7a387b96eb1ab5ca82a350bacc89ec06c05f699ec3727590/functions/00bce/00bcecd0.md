# 00bcecd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 要確認
  - [v15.7.3 → v15.7.4 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/review-0038.md#review-4cf72dda445ff945e96a45bb726b8b5f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0093.md#review-4cf72dda445ff945e96a45bb726b8b5f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcecd0",
  "name": "FUN_00bcecd0",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b72cf1868abfd5ee791525ebc5a396962c2da99d3cd6f1dbeadbc26ee11c0f70",
  "source_text_sha256": "b72cf1868abfd5ee791525ebc5a396962c2da99d3cd6f1dbeadbc26ee11c0f70",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcecd0",
        "00bcece3"
      ]
    ],
    "bytes_sha256": "58235d9561b5955f9aaf3de3dbc99af15937162ae4b24f451814e03388fc7cb9",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
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

## 疑似コード / UTF-8 266 bytes

~~~c

void FUN_00bcecd0(long param_1)

{
                    /* WARNING: Could not recover jumptable at 0x00bcece0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(**(long **)(param_1 + 0x18) + 0x30))();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcecd0"></a> `00bcecd0` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bcecd4"></a> `00bcecd4` | `00 0c 40 f9` | ldr x0,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bcecd8"></a> `00bcecd8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcecdc"></a> `00bcecdc` | `10 19 40 f9` | ldr x16,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00bcece0"></a> `00bcece0` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bcecd0`](#insn-00bcecd0) 範囲 `[['00bcecd0', '00bcece3']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

