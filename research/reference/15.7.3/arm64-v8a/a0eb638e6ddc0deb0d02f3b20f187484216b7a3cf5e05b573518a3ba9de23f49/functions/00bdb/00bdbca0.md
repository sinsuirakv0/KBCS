# 00bdbca0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdbbf0`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdb/00bdbbf0.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-bdacdf470227bf16c7272e634080c249)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdbcf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdb/00bdbcf0.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0013.md#compare-cfb3c4399130bc8396521de38bd503f6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbca0",
  "name": "_ZN5Botan6BigIntC1ERKS0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0bd4fb36b72dc115210993372953bebc9acd5221055c0cdb561649103ecbb807",
  "source_text_sha256": "0bd4fb36b72dc115210993372953bebc9acd5221055c0cdb561649103ecbb807",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbca0",
        "00bdbcaf"
      ]
    ],
    "bytes_sha256": "efd3fbd0bd7abbd4f108e3b78366d9104f461c40cd5d72af2abf6c6463294cc4",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00490728](../00490/00490728.md)
- [00493850](../00493/00493850.md)
- [00494d38](../00494/00494d38.md)
- [004967a4](../00496/004967a4.md)
- [00497724](../00497/00497724.md)
- [00497874](../00497/00497874.md)
- [00498754](../00498/00498754.md)
- [004987cc](../00498/004987cc.md)
- [004989ec](../00498/004989ec.md)
- [004b6640](../004b6/004b6640.md)
- [004b77d0](../004b7/004b77d0.md)
- [004b8aa0](../004b8/004b8aa0.md)
- [004b8bd8](../004b8/004b8bd8.md)
- [004b8e58](../004b8/004b8e58.md)
- [004b9948](../004b9/004b9948.md)
- [004ba430](../004ba/004ba430.md)
- [004bb1c0](../004bb/004bb1c0.md)
- [004bcf24](../004bc/004bcf24.md)
- [004bd550](../004bd/004bd550.md)
- [004bd8d4](../004bd/004bd8d4.md)
- [004be0f4](../004be/004be0f4.md)
- [004cfcb0](../004cf/004cfcb0.md)
- [004d04c0](../004d0/004d04c0.md)
- [0050fea8](../0050f/0050fea8.md)
- [005150ac](../00515/005150ac.md)
- [0051ce40](../0051c/0051ce40.md)
- [0051d0c8](../0051d/0051d0c8.md)
- [005221e4](../00522/005221e4.md)
- [00526bb4](../00526/00526bb4.md)

## 呼び出し先

- [00497dc8](../00497/00497dc8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 107 bytes

~~~c

void _ZN5Botan6BigIntC1ERKS0_(void)

{
  (*(code *)PTR__ZN5Botan6BigIntC1ERKS0__00c1c6e0)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbca0"></a> `00bdbca0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbca4"></a> `00bdbca4` | `11 72 43 f9` | ldr x17,[x16, #0x6e0] | `FALL_THROUGH`
<a id="insn-00bdbca8"></a> `00bdbca8` | `10 82 1b 91` | add x16,x16,#0x6e0 | `FALL_THROUGH`
<a id="insn-00bdbcac"></a> `00bdbcac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbca0`](#insn-00bdbca0) 範囲 `[['00bdbca0', '00bdbcaf']]`

## 命令位置別の参照

- [`00bdbca4`](#insn-00bdbca4) → `00c1c6e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbcac`](#insn-00bdbcac) → [`00497dc8`](../00497/00497dc8.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00497dc8` · 推定シンボル `_ZN5Botan6BigIntC1ERKS0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbca4`](#insn-00bdbca4)

~~~json
{
  "source": "00bdbca4",
  "target": "00c1c6e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c6e0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbcac`](#insn-00bdbcac)

~~~json
{
  "source": "00bdbcac",
  "target": "00497dc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
