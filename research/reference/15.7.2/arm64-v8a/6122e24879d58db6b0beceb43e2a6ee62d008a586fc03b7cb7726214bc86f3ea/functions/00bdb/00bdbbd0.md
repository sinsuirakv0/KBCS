# 00bdbbd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbc80`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbc80.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-1480714d03e8baeaaa6e93fa56a276ad)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbbd0",
  "name": "_ZNK5Botan6BigInt3cmpERKS0_b",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a5d60df237006bf73e2f46905c9a63382cdb66e9794da7f0f9d1d81a1d96b63c",
  "source_text_sha256": "a5d60df237006bf73e2f46905c9a63382cdb66e9794da7f0f9d1d81a1d96b63c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbbd0",
        "00bdbbdf"
      ]
    ],
    "bytes_sha256": "83c29ce50603e6119c87eb31a2b08e55f8e52402c4fd3efcc951e885e0e24792",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048ff2c](../0048f/0048ff2c.md)
- [00493850](../00493/00493850.md)
- [00495378](../00495/00495378.md)
- [004967a4](../00496/004967a4.md)
- [00497bf4](../00497/00497bf4.md)
- [004b5c14](../004b5/004b5c14.md)
- [004b6640](../004b6/004b6640.md)
- [004b6d50](../004b6/004b6d50.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8e58](../004b8/004b8e58.md)
- [004b9948](../004b9/004b9948.md)
- [004ba430](../004ba/004ba430.md)
- [004bb928](../004bb/004bb928.md)
- [004bbdd8](../004bb/004bbdd8.md)
- [004bcf24](../004bc/004bcf24.md)
- [004bdd7c](../004bd/004bdd7c.md)
- [004be0f4](../004be/004be0f4.md)
- [004cf4d8](../004cf/004cf4d8.md)
- [004cfcb0](../004cf/004cfcb0.md)
- [004d04c0](../004d0/004d04c0.md)
- [004d1904](../004d1/004d1904.md)
- [004e939c](../004e9/004e939c.md)
- [00513fc4](../00513/00513fc4.md)
- [00514cc0](../00514/00514cc0.md)
- [00516464](../00516/00516464.md)
- [005168d8](../00516/005168d8.md)

## 呼び出し先

- [00498160](../00498/00498160.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 115 bytes

~~~c

void _ZNK5Botan6BigInt3cmpERKS0_b(void)

{
  (*(code *)PTR__ZNK5Botan6BigInt3cmpERKS0_b_00c1c620)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbbd0"></a> `00bdbbd0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbbd4"></a> `00bdbbd4` | `11 12 43 f9` | ldr x17,[x16, #0x620] | `FALL_THROUGH`
<a id="insn-00bdbbd8"></a> `00bdbbd8` | `10 82 18 91` | add x16,x16,#0x620 | `FALL_THROUGH`
<a id="insn-00bdbbdc"></a> `00bdbbdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbbd0`](#insn-00bdbbd0) 範囲 `[['00bdbbd0', '00bdbbdf']]`

## 命令位置別の参照

- [`00bdbbd4`](#insn-00bdbbd4) → `00c1c620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbbdc`](#insn-00bdbbdc) → [`00498160`](../00498/00498160.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00498160` · 推定シンボル `_ZNK5Botan6BigInt3cmpERKS0_b` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbbd4`](#insn-00bdbbd4)

~~~json
{
  "source": "00bdbbd4",
  "target": "00c1c620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c620",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbbdc`](#insn-00bdbbdc)

~~~json
{
  "source": "00bdbbdc",
  "target": "00498160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
