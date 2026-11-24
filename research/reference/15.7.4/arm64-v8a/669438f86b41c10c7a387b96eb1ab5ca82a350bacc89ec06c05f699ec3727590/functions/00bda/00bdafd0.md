# 00bdafd0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 要確認
  - [v15.7.3 → v15.7.4 候補と検査根拠](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/review-0039.md#review-31c843b0b6b3aeb52e7d220fcefc4128)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0093.md#review-31c843b0b6b3aeb52e7d220fcefc4128)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdafd0",
  "name": "<EXTERNAL>::__cxa_finalize",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ee454707ff51c2b811bc691a4bcda28d1b92bd4f7346af5204f67639ee4dd61f",
  "source_text_sha256": "ee454707ff51c2b811bc691a4bcda28d1b92bd4f7346af5204f67639ee4dd61f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdafd0",
        "00bdafdf"
      ]
    ],
    "bytes_sha256": "5f3ecc2db703d74913a65d22ca66ef80c2b26e66f82703804e41b28e880a0a17",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004182d0](../00418/004182d0.md)

## 呼び出し先

- [010a5000](../010a5/010a5000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 87 bytes

~~~c

void __cxa_finalize(void)

{
  (*(code *)PTR___cxa_finalize_00c1c0a0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdafd0"></a> `00bdafd0` | `10 02 00 d0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdafd4"></a> `00bdafd4` | `11 52 40 f9` | ldr x17,[x16, #0xa0] | `FALL_THROUGH`
<a id="insn-00bdafd8"></a> `00bdafd8` | `10 82 02 91` | add x16,x16,#0xa0 | `FALL_THROUGH`
<a id="insn-00bdafdc"></a> `00bdafdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdafd0`](#insn-00bdafd0) 範囲 `[['00bdafd0', '00bdafdf']]`

## 命令位置別の参照

- [`00bdafd4`](#insn-00bdafd4) → `00c1c0a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdafdc`](#insn-00bdafdc) → [`010a5000`](../010a5/010a5000.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5000` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdafd4`](#insn-00bdafd4)

~~~json
{
  "source": "00bdafd4",
  "target": "00c1c0a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c0a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdafdc`](#insn-00bdafdc)

~~~json
{
  "source": "00bdafdc",
  "target": "010a5000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
