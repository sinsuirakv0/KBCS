# 00bfbc1c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b7f1d4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b7f/00b7f1d4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/detail_skipped-0004.md#compare-8139d33acab04afeec046801e5d6f053)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfc044`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc044.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0006.md#compare-cc6d9ee8b5411f719439f330e95b1a31)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfbc1c",
  "name": "_ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5gbumpEi",
  "size": 20,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "47b19452d05e66a35de33bbf920d6544362c648cca1e548d9785c8a85daffc15",
  "source_text_sha256": "47b19452d05e66a35de33bbf920d6544362c648cca1e548d9785c8a85daffc15",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfbc1c",
        "00bfbc2f"
      ]
    ],
    "bytes_sha256": "ce8a22209341188c6fb58637e95673f887a46f90122fe34e19621180e44d1ff6",
    "instruction_count": 5,
    "instruction_bytes": 20,
    "body_bytes": 20,
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

## 疑似コード / UTF-8 182 bytes

~~~c

void _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEE5gbumpEi(long param_1,int param_2)

{
  *(long *)(param_1 + 0x18) = *(long *)(param_1 + 0x18) + (long)param_2;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfbc1c"></a> `00bfbc1c` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bfbc20"></a> `00bfbc20` | `08 0c 40 f9` | ldr x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbc24"></a> `00bfbc24` | `08 c1 21 8b` | add x8,x8,w1, SXTW  | `FALL_THROUGH`
<a id="insn-00bfbc28"></a> `00bfbc28` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfbc2c"></a> `00bfbc2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfbc1c`](#insn-00bfbc1c) 範囲 `[['00bfbc1c', '00bfbc2f']]`

## 命令位置別の参照


## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

