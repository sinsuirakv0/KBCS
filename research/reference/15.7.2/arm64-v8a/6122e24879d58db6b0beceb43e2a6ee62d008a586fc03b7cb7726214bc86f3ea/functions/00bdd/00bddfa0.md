# 00bddfa0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bde050`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde050.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-7ab2f528f9afa45dd9afd1329135765a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddfa0",
  "name": "_ZN8firebase4util15JStringToStringEP7_JNIEnvP8_jobject",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fafa19966ec4d882810b89d972a5ee9cdbed63e5445dd401db7086e9b6bd1cdd",
  "source_text_sha256": "fafa19966ec4d882810b89d972a5ee9cdbed63e5445dd401db7086e9b6bd1cdd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddfa0",
        "00bddfaf"
      ]
    ],
    "bytes_sha256": "0cfc9686d09b1510aa3c3d9c2822b70e8662e6f45680ce100a6d1e40201061c4",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae3268](../00ae3/00ae3268.md)
- [00af1e20](../00af1/00af1e20.md)
- [00af26fc](../00af2/00af26fc.md)
- [00af2e14](../00af2/00af2e14.md)
- [00af3094](../00af3/00af3094.md)
- [00af31b0](../00af3/00af31b0.md)
- [00af3498](../00af3/00af3498.md)
- [00af36ec](../00af3/00af36ec.md)
- [00af3bac](../00af3/00af3bac.md)
- [00af57bc](../00af5/00af57bc.md)
- [00af5df4](../00af5/00af5df4.md)
- [00af65e0](../00af6/00af65e0.md)
- [00af6fc8](../00af6/00af6fc8.md)
- [00af707c](../00af7/00af707c.md)
- [00af7190](../00af7/00af7190.md)
- [00af7334](../00af7/00af7334.md)
- [00af8750](../00af8/00af8750.md)
- [00b58fa4](../00b58/00b58fa4.md)
- [00b6b8ac](../00b6b/00b6b8ac.md)

## 呼び出し先

- [00af22dc](../00af2/00af22dc.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 167 bytes

~~~c

void _ZN8firebase4util15JStringToStringEP7_JNIEnvP8_jobject(void)

{
  (*(code *)PTR__ZN8firebase4util15JStringToStringEP7_JNIEnvP8_jobject_00c1d808)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddfa0"></a> `00bddfa0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddfa4"></a> `00bddfa4` | `11 06 44 f9` | ldr x17,[x16, #0x808] | `FALL_THROUGH`
<a id="insn-00bddfa8"></a> `00bddfa8` | `10 22 20 91` | add x16,x16,#0x808 | `FALL_THROUGH`
<a id="insn-00bddfac"></a> `00bddfac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddfa0`](#insn-00bddfa0) 範囲 `[['00bddfa0', '00bddfaf']]`

## 命令位置別の参照

- [`00bddfa4`](#insn-00bddfa4) → `00c1d808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddfac`](#insn-00bddfac) → [`00af22dc`](../00af2/00af22dc.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00af22dc` · 推定シンボル `_ZN8firebase4util15JStringToStringEP7_JNIEnvP8_jobject` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddfa4`](#insn-00bddfa4)

~~~json
{
  "source": "00bddfa4",
  "target": "00c1d808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d808",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddfac`](#insn-00bddfac)

~~~json
{
  "source": "00bddfac",
  "target": "00af22dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
