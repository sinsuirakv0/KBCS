# 00bdefc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdef10`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bdef10.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0019.md#compare-0d60bd0e3621bb5c97a46e9bccd74610)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdf010`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdf/00bdf010.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0021.md#compare-26fb2d98e0526d9e43d9e012bd191270)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdefc0",
  "name": "_ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ce1d6cde9c75e3057e58dade9b1b64fd565e2f7da86eaf77d2bd749b8006205e",
  "source_text_sha256": "ce1d6cde9c75e3057e58dade9b1b64fd565e2f7da86eaf77d2bd749b8006205e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdefc0",
        "00bdefcf"
      ]
    ],
    "bytes_sha256": "23b6fab803966d50b96626a89ad51dfbbd67caa27cb0f62ac5ef8a3801a931c3",
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
- [00b0a968](../00b0a/00b0a968.md)

## 呼び出し先

- [00b061ec](../00b06/00b061ec.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 181 bytes

~~~c

void _ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject(void)

{
  (*(code *)PTR__ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject_00c1e070)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdefc0"></a> `00bdefc0` | `10 02 00 90` | adrp x16,0xc1e000 | `FALL_THROUGH`
<a id="insn-00bdefc4"></a> `00bdefc4` | `11 3a 40 f9` | ldr x17,[x16, #0x70] | `FALL_THROUGH`
<a id="insn-00bdefc8"></a> `00bdefc8` | `10 c2 01 91` | add x16,x16,#0x70 | `FALL_THROUGH`
<a id="insn-00bdefcc"></a> `00bdefcc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdefc0`](#insn-00bdefc0) 範囲 `[['00bdefc0', '00bdefcf']]`

## 命令位置別の参照

- [`00bdefc4`](#insn-00bdefc4) → `00c1e070`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdefcc`](#insn-00bdefcc) → [`00b061ec`](../00b06/00b061ec.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b061ec` · 推定シンボル `_ZN8firebase10AppOptions11LoadDefaultEPS0_P7_JNIEnvP8_jobject` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdefc4`](#insn-00bdefc4)

~~~json
{
  "source": "00bdefc4",
  "target": "00c1e070",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1e070",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdefcc`](#insn-00bdefcc)

~~~json
{
  "source": "00bdefcc",
  "target": "00b061ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
