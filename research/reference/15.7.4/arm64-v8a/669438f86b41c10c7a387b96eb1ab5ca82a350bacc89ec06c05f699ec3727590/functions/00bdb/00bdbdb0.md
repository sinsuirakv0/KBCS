# 00bdbdb0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbd60`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbd60.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-80e98e50f0d307dee91944ecdc0cb3ab)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c58800`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c58/00c58800.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0007.md#compare-4e0314d08b8eb46cf165d2a9470e1ff3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbdb0",
  "name": "_ZN5Botan13base64_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2b62159e1f7a0a8baa6a7dd0fa8bf8ebb5a9238dfbf9340c135fccfc746d6b14",
  "source_text_sha256": "2b62159e1f7a0a8baa6a7dd0fa8bf8ebb5a9238dfbf9340c135fccfc746d6b14",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbdb0",
        "00bdbdbf"
      ]
    ],
    "bytes_sha256": "4b6036d103834828b634a8df3123c7d92d63a8357c3e2740a3e792fa4852caac",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0055dc58](../0055d/0055dc58.md)

## 呼び出し先

- [00493354](../00493/00493354.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 273 bytes

~~~c

void _ZN5Botan13base64_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb
               (void)

{
  (*(code *)
    PTR__ZN5Botan13base64_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb_00c1c790
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbdb0"></a> `00bdbdb0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbdb4"></a> `00bdbdb4` | `11 ca 43 f9` | ldr x17,[x16, #0x790] | `FALL_THROUGH`
<a id="insn-00bdbdb8"></a> `00bdbdb8` | `10 42 1e 91` | add x16,x16,#0x790 | `FALL_THROUGH`
<a id="insn-00bdbdbc"></a> `00bdbdbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbdb0`](#insn-00bdbdb0) 範囲 `[['00bdbdb0', '00bdbdbf']]`

## 命令位置別の参照

- [`00bdbdb4`](#insn-00bdbdb4) → `00c1c790`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdbc`](#insn-00bdbdbc) → [`00493354`](../00493/00493354.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00493354` · 推定シンボル `_ZN5Botan13base64_decodeERKNSt6__ndk112basic_stringIcNS0_11char_traitsIcEENS0_9allocatorIcEEEEb` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbdb4`](#insn-00bdbdb4)

~~~json
{
  "source": "00bdbdb4",
  "target": "00c1c790",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c790",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbdbc`](#insn-00bdbdbc)

~~~json
{
  "source": "00bdbdbc",
  "target": "00493354",
  "target_space": "ram",
  "resolution": "function"
}
~~~
