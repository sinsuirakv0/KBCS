# 00bdefd0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdef20`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef20.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-425229b0c9a306057319e232905c61ce)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdf020`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf020.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0021.md#compare-d655a248f0d8d76eb87022855069b453)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdefd0",
  "name": "_ZN8firebase3App6CreateERKNS_10AppOptionsEPKcP7_JNIEnvP8_jobject",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0f996acac42292c6dae958347ed536a8fc915553f2d566a7465eba215796d18a",
  "source_text_sha256": "0f996acac42292c6dae958347ed536a8fc915553f2d566a7465eba215796d18a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdefd0",
        "00bdefdf"
      ]
    ],
    "bytes_sha256": "357e49f6562463de70d16b1eba4bf0b37978082b845232d4c779ed452cb9ac21",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b06be8](../00b06/00b06be8.md)
- [00b06cc8](../00b06/00b06cc8.md)

## 呼び出し先

- [00b06ce0](../00b06/00b06ce0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 187 bytes

~~~c

void _ZN8firebase3App6CreateERKNS_10AppOptionsEPKcP7_JNIEnvP8_jobject(void)

{
  (*(code *)PTR__ZN8firebase3App6CreateERKNS_10AppOptionsEPKcP7_JNIEnvP8_jobject_00c1e078)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdefd0"></a> `00bdefd0` | `10 02 00 90` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdefd4"></a> `00bdefd4` | `11 3e 40 f9` | ldr x17,[x16, #0x78] | `FALL_THROUGH`
<a id="insn-00bdefd8"></a> `00bdefd8` | `10 e2 01 91` | add x16,x16,#0x78 | `FALL_THROUGH`
<a id="insn-00bdefdc"></a> `00bdefdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdefd0`](#insn-00bdefd0) 範囲 `[['00bdefd0', '00bdefdf']]`

## 命令位置別の参照

- [`00bdefd4`](#insn-00bdefd4) → `00c1e078`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdefdc`](#insn-00bdefdc) → [`00b06ce0`](../00b06/00b06ce0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b06ce0` · 推定シンボル `_ZN8firebase3App6CreateERKNS_10AppOptionsEPKcP7_JNIEnvP8_jobject` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdefd4`](#insn-00bdefd4)

~~~json
{
  "source": "00bdefd4",
  "target": "00c1e078",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e078",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdefdc`](#insn-00bdefdc)

~~~json
{
  "source": "00bdefdc",
  "target": "00b06ce0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
