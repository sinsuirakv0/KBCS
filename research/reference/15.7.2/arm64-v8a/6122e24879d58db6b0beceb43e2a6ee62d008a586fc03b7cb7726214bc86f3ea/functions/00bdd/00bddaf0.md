# 00bddaf0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bddba0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdd/00bddba0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-508993ad7423d24d72eaa2f1b1ed8a5d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddaf0",
  "name": "_ZNK8firebase4auth4User8is_validEv",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e2c95d9627de68267fab293c49ab35d03b7a018a11a8f582ffed7610d16db5a9",
  "source_text_sha256": "e2c95d9627de68267fab293c49ab35d03b7a018a11a8f582ffed7610d16db5a9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddaf0",
        "00bddaff"
      ]
    ],
    "bytes_sha256": "f41d98001b72d6a0b294dd32109a6c821ea79529052cf429bbba809edff67eff",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00848250](../00848/00848250.md)
- [0084859c](../00848/0084859c.md)
- [00ad4f2c](../00ad4/00ad4f2c.md)
- [00b5c870](../00b5c/00b5c870.md)
- [00b5c8a4](../00b5c/00b5c8a4.md)

## 呼び出し先

- [00b6e878](../00b6e/00b6e878.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 127 bytes

~~~c

void _ZNK8firebase4auth4User8is_validEv(void)

{
  (*(code *)PTR__ZNK8firebase4auth4User8is_validEv_00c1d5b0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddaf0"></a> `00bddaf0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddaf4"></a> `00bddaf4` | `11 da 42 f9` | ldr x17,[x16, #0x5b0] | `FALL_THROUGH`
<a id="insn-00bddaf8"></a> `00bddaf8` | `10 c2 16 91` | add x16,x16,#0x5b0 | `FALL_THROUGH`
<a id="insn-00bddafc"></a> `00bddafc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddaf0`](#insn-00bddaf0) 範囲 `[['00bddaf0', '00bddaff']]`

## 命令位置別の参照

- [`00bddaf4`](#insn-00bddaf4) → `00c1d5b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddafc`](#insn-00bddafc) → [`00b6e878`](../00b6e/00b6e878.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b6e878` · 推定シンボル `_ZNK8firebase4auth4User8is_validEv` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddaf4`](#insn-00bddaf4)

~~~json
{
  "source": "00bddaf4",
  "target": "00c1d5b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d5b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddafc`](#insn-00bddafc)

~~~json
{
  "source": "00bddafc",
  "target": "00b6e878",
  "target_space": "ram",
  "resolution": "function"
}
~~~
