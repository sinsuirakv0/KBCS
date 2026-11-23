# 00bdcde0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdce90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdc/00bdce90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-4b2e15580b9541147cec6d476a324bd1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcde0",
  "name": "_ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1ed4898350a77cefcddb44b4c1ef6c3bc0f81a918762ac92e183cebfcc8e702a",
  "source_text_sha256": "1ed4898350a77cefcddb44b4c1ef6c3bc0f81a918762ac92e183cebfcc8e702a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcde0",
        "00bdcdef"
      ]
    ],
    "bytes_sha256": "3598234cfe6dfc0a4b81800cb498ca68d667975f9d6f770334111bfbc192fe06",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004ede80](../004ed/004ede80.md)

## 呼び出し先

- [004ee4f4](../004ee/004ee4f4.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 274 bytes

~~~c

void _ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb(void)

{
                    /* try { // try from 00bdcde0 to 00cdce3b has its CatchHandler @ 00bdcbcc */
  (*(code *)PTR__ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb_00c1cf28)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcde0"></a> `00bdcde0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcde4"></a> `00bdcde4` | `11 96 47 f9` | ldr x17,[x16, #0xf28] | `FALL_THROUGH`
<a id="insn-00bdcde8"></a> `00bdcde8` | `10 a2 3c 91` | add x16,x16,#0xf28 | `FALL_THROUGH`
<a id="insn-00bdcdec"></a> `00bdcdec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcde0`](#insn-00bdcde0) 範囲 `[['00bdcde0', '00bdcdef']]`

## 命令位置別の参照

- [`00bdcde4`](#insn-00bdcde4) → `00c1cf28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcdec`](#insn-00bdcdec) → [`004ee4f4`](../004ee/004ee4f4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004ee4f4` · 推定シンボル `_ZN5Botan10Extensions7replaceEPNS_21Certificate_ExtensionEb` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcde4`](#insn-00bdcde4)

~~~json
{
  "source": "00bdcde4",
  "target": "00c1cf28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1cf28",
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
  "target": "004ee4f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
