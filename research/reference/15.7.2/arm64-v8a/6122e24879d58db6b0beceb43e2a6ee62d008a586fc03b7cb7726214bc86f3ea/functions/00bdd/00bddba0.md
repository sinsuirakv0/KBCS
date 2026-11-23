# 00bddba0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddc50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddc50.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-ef541cb052df923c1d60500e5d3a7c86)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddba0",
  "name": "_ZNK8firebase7Variant7AsInt64Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "adf0b5d23ee8013097c811a73066ddd686ae3566a80966a7e15adda0a4bc3ae8",
  "source_text_sha256": "adf0b5d23ee8013097c811a73066ddd686ae3566a80966a7e15adda0a4bc3ae8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddba0",
        "00bddbaf"
      ]
    ],
    "bytes_sha256": "a1f2c47e4f07ce2338fe2b1facf94d25c5853af936e56d5d330da655330ff48d",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0084a918](../0084a/0084a918.md)

## 呼び出し先

- [00b04800](../00b04/00b04800.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 121 bytes

~~~c

void _ZNK8firebase7Variant7AsInt64Ev(void)

{
  (*(code *)PTR__ZNK8firebase7Variant7AsInt64Ev_00c1d608)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddba0"></a> `00bddba0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddba4"></a> `00bddba4` | `11 06 43 f9` | ldr x17,[x16, #0x608] | `FALL_THROUGH`
<a id="insn-00bddba8"></a> `00bddba8` | `10 22 18 91` | add x16,x16,#0x608 | `FALL_THROUGH`
<a id="insn-00bddbac"></a> `00bddbac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddba0`](#insn-00bddba0) 範囲 `[['00bddba0', '00bddbaf']]`

## 命令位置別の参照

- [`00bddba4`](#insn-00bddba4) → `00c1d608`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddbac`](#insn-00bddbac) → [`00b04800`](../00b04/00b04800.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b04800` · 推定シンボル `_ZNK8firebase7Variant7AsInt64Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddba4`](#insn-00bddba4)

~~~json
{
  "source": "00bddba4",
  "target": "00c1d608",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d608",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddbac`](#insn-00bddbac)

~~~json
{
  "source": "00bddbac",
  "target": "00b04800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
