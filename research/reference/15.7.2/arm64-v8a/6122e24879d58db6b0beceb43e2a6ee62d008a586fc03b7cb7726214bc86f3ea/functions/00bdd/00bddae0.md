# 00bddae0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddb90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddb90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-bda18710cf1681154df5865c4de25a95)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddae0",
  "name": "_ZN8firebase4auth4UserD1Ev",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e4f0019f56409b466df05c1f01cd7ce45997b5f0df050005585e5ee0de562684",
  "source_text_sha256": "e4f0019f56409b466df05c1f01cd7ce45997b5f0df050005585e5ee0de562684",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddae0",
        "00bddaef"
      ]
    ],
    "bytes_sha256": "a424241325e758ba69d0035061fb0c48e0390cf651f36720abc9d3d6d9fe8153",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [008480ec](../00848/008480ec.md)
- [0084859c](../00848/0084859c.md)
- [0084914c](../00849/0084914c.md)
- [00ad4f2c](../00ad4/00ad4f2c.md)
- [00b5b264](../00b5b/00b5b264.md)
- [00b602a4](../00b60/00b602a4.md)
- [00b64df8](../00b64/00b64df8.md)
- [00b65208](../00b65/00b65208.md)
- [00b6be60](../00b6b/00b6be60.md)
- [00b6c444](../00b6c/00b6c444.md)
- [00b6c71c](../00b6c/00b6c71c.md)

## 呼び出し先

- [00b6e828](../00b6e/00b6e828.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 111 bytes

~~~c

void _ZN8firebase4auth4UserD1Ev(void)

{
  (*(code *)PTR__ZN8firebase4auth4UserD1Ev_00c1d5a8)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddae0"></a> `00bddae0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddae4"></a> `00bddae4` | `11 d6 42 f9` | ldr x17,[x16, #0x5a8] | `FALL_THROUGH`
<a id="insn-00bddae8"></a> `00bddae8` | `10 a2 16 91` | add x16,x16,#0x5a8 | `FALL_THROUGH`
<a id="insn-00bddaec"></a> `00bddaec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddae0`](#insn-00bddae0) 範囲 `[['00bddae0', '00bddaef']]`

## 命令位置別の参照

- [`00bddae4`](#insn-00bddae4) → `00c1d5a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddaec`](#insn-00bddaec) → [`00b6e828`](../00b6e/00b6e828.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b6e828` · 推定シンボル `_ZN8firebase4auth4UserD1Ev` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddae4`](#insn-00bddae4)

~~~json
{
  "source": "00bddae4",
  "target": "00c1d5a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d5a8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddaec`](#insn-00bddaec)

~~~json
{
  "source": "00bddaec",
  "target": "00b6e828",
  "target_space": "ram",
  "resolution": "function"
}
~~~
