# 00bdaed0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 要確認
  - [v15.7.2 → v15.7.3 候補と検査根拠](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/review-0022.md#review-4a5b66c39e5cf03c957d82523079ed6a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaed0",
  "name": "<EXTERNAL>::__cxa_finalize",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2050b15d6f32d8e6c0eeae8e56b4a6d6f87f340e0cb9062cb029af0994c1748e",
  "source_text_sha256": "2050b15d6f32d8e6c0eeae8e56b4a6d6f87f340e0cb9062cb029af0994c1748e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdaed0",
        "00bdaedf"
      ]
    ],
    "bytes_sha256": "289a9ee61b80adb0b38fc2c905670a630e99280ba1ded325544f6d5ec77c039a",
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
  (*(code *)PTR___cxa_finalize_00c1bfa0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdaed0"></a> `00bdaed0` | `10 02 00 b0` | adrp x16,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bdaed4"></a> `00bdaed4` | `11 d2 47 f9` | ldr x17,[x16, #0xfa0] | `FALL_THROUGH`
<a id="insn-00bdaed8"></a> `00bdaed8` | `10 82 3e 91` | add x16,x16,#0xfa0 | `FALL_THROUGH`
<a id="insn-00bdaedc"></a> `00bdaedc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdaed0`](#insn-00bdaed0) 範囲 `[['00bdaed0', '00bdaedf']]`

## 命令位置別の参照

- [`00bdaed4`](#insn-00bdaed4) → `00c1bfa0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdaedc`](#insn-00bdaedc) → [`010a5000`](../010a5/010a5000.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5000` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdaed4`](#insn-00bdaed4)

~~~json
{
  "source": "00bdaed4",
  "target": "00c1bfa0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bfa0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdaedc`](#insn-00bdaedc)

~~~json
{
  "source": "00bdaedc",
  "target": "010a5000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
