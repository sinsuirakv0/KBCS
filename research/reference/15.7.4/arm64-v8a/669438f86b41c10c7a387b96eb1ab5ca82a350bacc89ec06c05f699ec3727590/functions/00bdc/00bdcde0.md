# 00bdcde0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdcd90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdcd90.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-a149a76c3fcc96731f667accb2670cc1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c59830`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c59/00c59830.md) · 移動量 `+0x7ca50`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/high-0009.md#compare-ac27c1a59c8fddfe803dc49c52cc714f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcde0",
  "name": "_ZNK5Botan16X509_Certificate33subject_public_key_bitstring_sha1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ef828222c1d55798e22bc544f3954887d46ad1447b70c021059a325f62f45779",
  "source_text_sha256": "ef828222c1d55798e22bc544f3954887d46ad1447b70c021059a325f62f45779",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcde0",
        "00bdcdef"
      ]
    ],
    "bytes_sha256": "91a123aa8a46080a8ad89267739356353e882d60068d6037b6a557f1424a6df2",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e8a14](../004e8/004e8a14.md)

## 呼び出し先

- [004e8fec](../004e8/004e8fec.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 189 bytes

~~~c

void _ZNK5Botan16X509_Certificate33subject_public_key_bitstring_sha1Ev(void)

{
  (*(code *)PTR__ZNK5Botan16X509_Certificate33subject_public_key_bitstring_sha1Ev_00c1cfa8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcde0"></a> `00bdcde0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcde4"></a> `00bdcde4` | `11 d6 47 f9` | ldr x17,[x16, #0xfa8] | `FALL_THROUGH`
<a id="insn-00bdcde8"></a> `00bdcde8` | `10 a2 3e 91` | add x16,x16,#0xfa8 | `FALL_THROUGH`
<a id="insn-00bdcdec"></a> `00bdcdec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcde0`](#insn-00bdcde0) 範囲 `[['00bdcde0', '00bdcdef']]`

## 命令位置別の参照

- [`00bdcde4`](#insn-00bdcde4) → `00c1cfa8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcdec`](#insn-00bdcdec) → [`004e8fec`](../004e8/004e8fec.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e8fec` · 推定シンボル `_ZNK5Botan16X509_Certificate33subject_public_key_bitstring_sha1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcde4`](#insn-00bdcde4)

~~~json
{
  "source": "00bdcde4",
  "target": "00c1cfa8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cfa8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcdec`](#insn-00bdcdec)

~~~json
{
  "source": "00bdcdec",
  "target": "004e8fec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
