# 00bddfd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddf20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddf20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-36c14c8c42047d2836010b33ddaa1166)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bde020`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bde020.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-d3b8f8e069327ec37e85f69d2d9d5822)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddfd0",
  "name": "_ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4db48e7990615a14e4b22fb62f76243c3b0f49184a3713d9a3ed44c88fc5dbc0",
  "source_text_sha256": "4db48e7990615a14e4b22fb62f76243c3b0f49184a3713d9a3ed44c88fc5dbc0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddfd0",
        "00bddfdf"
      ]
    ],
    "bytes_sha256": "dad7de32851f63da86ca28d1d6f04d824e95085a92a071de49710fc60f4311cd",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae0f70](../00ae0/00ae0f70.md)
- [00b06390](../00b06/00b06390.md)
- [00b0d740](../00b0d/00b0d740.md)
- [00b4c480](../00b4c/00b4c480.md)
- [00b54af4](../00b54/00b54af4.md)
- [00b5dce8](../00b5d/00b5dce8.md)

## 呼び出し先

- [00aee94c](../00aee/00aee94c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 157 bytes

~~~c

void _ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject(void)

{
  (*(code *)PTR__ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject_00c1d878)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddfd0"></a> `00bddfd0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddfd4"></a> `00bddfd4` | `11 3e 44 f9` | ldr x17,[x16, #0x878] | `FALL_THROUGH`
<a id="insn-00bddfd8"></a> `00bddfd8` | `10 e2 21 91` | add x16,x16,#0x878 | `FALL_THROUGH`
<a id="insn-00bddfdc"></a> `00bddfdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddfd0`](#insn-00bddfd0) 範囲 `[['00bddfd0', '00bddfdf']]`

## 命令位置別の参照

- [`00bddfd4`](#insn-00bddfd4) → `00c1d878`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddfdc`](#insn-00bddfdc) → [`00aee94c`](../00aee/00aee94c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00aee94c` · 推定シンボル `_ZN8firebase4util10InitializeEP7_JNIEnvP8_jobject` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddfd4`](#insn-00bddfd4)

~~~json
{
  "source": "00bddfd4",
  "target": "00c1d878",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d878",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddfdc`](#insn-00bddfdc)

~~~json
{
  "source": "00bddfdc",
  "target": "00aee94c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
