# 00bdbdc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbd10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbd10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-efa36f17dc68aea92aab9485f447e005)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbe10`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbe10.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-3e4199daf3e1f0ce85987755f3e7dfbd)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbdc0",
  "name": "_ZN5Botan6BigInt11encode_1363EPhmRKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f30aad7f9f003d369e7b9acce4a4c8f07f6614b0b56db9559ac566be0a446cb4",
  "source_text_sha256": "f30aad7f9f003d369e7b9acce4a4c8f07f6614b0b56db9559ac566be0a446cb4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbdc0",
        "00bdbdcf"
      ]
    ],
    "bytes_sha256": "8b858f13f51a6d69ab2cdfe0713d775c48021c44bae9aba6b8cc090e2056226e",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004945e8](../00494/004945e8.md)
- [004947cc](../00494/004947cc.md)
- [004cd86c](../004cd/004cd86c.md)
- [00516464](../00516/00516464.md)
- [005168d8](../00516/005168d8.md)

## 呼び出し先

- [00494634](../00494/00494634.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 232 bytes

~~~c

void _ZN5Botan6BigInt11encode_1363EPhmRKS0_(void)

{
                    /* try { // try from 00bdbdc0 to 00cdc01b has its CatchHandler @ 00bdbbe4 */
  (*(code *)PTR__ZN5Botan6BigInt11encode_1363EPhmRKS0__00c1c770)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbdc0"></a> `00bdbdc0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbdc4"></a> `00bdbdc4` | `11 ba 43 f9` | ldr x17,[x16, #0x770] | `FALL_THROUGH`
<a id="insn-00bdbdc8"></a> `00bdbdc8` | `10 c2 1d 91` | add x16,x16,#0x770 | `FALL_THROUGH`
<a id="insn-00bdbdcc"></a> `00bdbdcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbdc0`](#insn-00bdbdc0) 範囲 `[['00bdbdc0', '00bdbdcf']]`

## 命令位置別の参照

- [`00bdbdc4`](#insn-00bdbdc4) → `00c1c770`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdcc`](#insn-00bdbdcc) → [`00494634`](../00494/00494634.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00494634` · 推定シンボル `_ZN5Botan6BigInt11encode_1363EPhmRKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbdc4`](#insn-00bdbdc4)

~~~json
{
  "source": "00bdbdc4",
  "target": "00c1c770",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c770",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbdcc`](#insn-00bdbdcc)

~~~json
{
  "source": "00bdbdcc",
  "target": "00494634",
  "target_space": "ram",
  "resolution": "function"
}
~~~
