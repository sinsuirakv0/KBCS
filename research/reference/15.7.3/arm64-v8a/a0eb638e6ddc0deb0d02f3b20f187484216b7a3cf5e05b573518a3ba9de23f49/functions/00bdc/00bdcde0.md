# 00bdcde0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcd30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcd30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-8708da37aabb2b4598001e47bccff1d9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdce30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdce30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0016.md#compare-016786f346a8bbec8092ee5ad1b89fcb)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcde0",
  "name": "_ZN5Botan11X509_Object9load_dataERNS_10DataSourceE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "255ff6144cf7860550418e9f3d06b76b3bd164796eb8f7cf0db7cac84e6cf9c1",
  "source_text_sha256": "255ff6144cf7860550418e9f3d06b76b3bd164796eb8f7cf0db7cac84e6cf9c1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcde0",
        "00bdcdef"
      ]
    ],
    "bytes_sha256": "0a53430026fae71df9f913ac8a4e9eaeb582f0dbddd07c21c969d7785365a2ef",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004ea55c](../004ea/004ea55c.md)
- [004eaec8](../004ea/004eaec8.md)
- [004eb040](../004eb/004eb040.md)
- [004efa38](../004ef/004efa38.md)
- [004efb8c](../004ef/004efb8c.md)
- [004efd04](../004ef/004efd04.md)
- [004fdbe0](../004fd/004fdbe0.md)
- [004fdd34](../004fd/004fdd34.md)
- [004fdeac](../004fd/004fdeac.md)

## 呼び出し先

- [004ea660](../004ea/004ea660.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 159 bytes

~~~c

void _ZN5Botan11X509_Object9load_dataERNS_10DataSourceE(void)

{
  (*(code *)PTR__ZN5Botan11X509_Object9load_dataERNS_10DataSourceE_00c1cf80)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcde0"></a> `00bdcde0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcde4"></a> `00bdcde4` | `11 c2 47 f9` | ldr x17,[x16, #0xf80] | `FALL_THROUGH`
<a id="insn-00bdcde8"></a> `00bdcde8` | `10 02 3e 91` | add x16,x16,#0xf80 | `FALL_THROUGH`
<a id="insn-00bdcdec"></a> `00bdcdec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcde0`](#insn-00bdcde0) 範囲 `[['00bdcde0', '00bdcdef']]`

## 命令位置別の参照

- [`00bdcde4`](#insn-00bdcde4) → `00c1cf80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcdec`](#insn-00bdcdec) → [`004ea660`](../004ea/004ea660.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004ea660` · 推定シンボル `_ZN5Botan11X509_Object9load_dataERNS_10DataSourceE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcde4`](#insn-00bdcde4)

~~~json
{
  "source": "00bdcde4",
  "target": "00c1cf80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf80",
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
  "target": "004ea660",
  "target_space": "ram",
  "resolution": "function"
}
~~~
