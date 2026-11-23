# 00bdeca0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bded50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bded50.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-a3e1e78a6b034395c41a40193235d540)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdeca0",
  "name": "_ZN8firebase12FutureHandleC1EOS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d4c347adbdc68473dbb84d8b93f86347253569507bc8e097b10b73c2a07dcfa9",
  "source_text_sha256": "d4c347adbdc68473dbb84d8b93f86347253569507bc8e097b10b73c2a07dcfa9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdeca0",
        "00bdecaf"
      ]
    ],
    "bytes_sha256": "b27bbc341fc3ea8856ba2b5deb80f7b8a717ccd46a8d12c34616019b6c2f4990",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b4d13c](../00b4d/00b4d13c.md)
- [00b4d6e0](../00b4d/00b4d6e0.md)
- [00b4eba8](../00b4e/00b4eba8.md)

## 呼び出し先

- [00b00d38](../00b00/00b00d38.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 125 bytes

~~~c

void _ZN8firebase12FutureHandleC1EOS0_(void)

{
  (*(code *)PTR__ZN8firebase12FutureHandleC1EOS0__00c1de88)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdeca0"></a> `00bdeca0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdeca4"></a> `00bdeca4` | `11 46 47 f9` | ldr x17,[x16, #0xe88] | `FALL_THROUGH`
<a id="insn-00bdeca8"></a> `00bdeca8` | `10 22 3a 91` | add x16,x16,#0xe88 | `FALL_THROUGH`
<a id="insn-00bdecac"></a> `00bdecac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdeca0`](#insn-00bdeca0) 範囲 `[['00bdeca0', '00bdecaf']]`

## 命令位置別の参照

- [`00bdeca4`](#insn-00bdeca4) → `00c1de88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdecac`](#insn-00bdecac) → [`00b00d38`](../00b00/00b00d38.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b00d38` · 推定シンボル `_ZN8firebase12FutureHandleC1EOS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdeca4`](#insn-00bdeca4)

~~~json
{
  "source": "00bdeca4",
  "target": "00c1de88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1de88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdecac`](#insn-00bdecac)

~~~json
{
  "source": "00bdecac",
  "target": "00b00d38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
