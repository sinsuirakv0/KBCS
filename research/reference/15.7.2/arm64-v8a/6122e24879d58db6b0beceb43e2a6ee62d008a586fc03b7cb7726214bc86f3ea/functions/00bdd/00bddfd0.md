# 00bddfd0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bde080`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bde/00bde080.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-119611168db8731c9843348d9c38264c)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddfd0",
  "name": "_ZN8firebase4util23GetMessageFromExceptionEP7_JNIEnvP8_jobject",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c75c68c4a8001d7496f3f9a2bfe594ffc4ca63714143f1d742daf6f18ed0cce8",
  "source_text_sha256": "c75c68c4a8001d7496f3f9a2bfe594ffc4ca63714143f1d742daf6f18ed0cce8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddfd0",
        "00bddfdf"
      ]
    ],
    "bytes_sha256": "f0cfccb7c78094dfea8bddade8e5bf48170feb8766b1207908dcf8428df36e86",
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
- [00af710c](../00af7/00af710c.md)
- [00b4d40c](../00b4d/00b4d40c.md)
- [00b4d9b0](../00b4d/00b4d9b0.md)
- [00b647c4](../00b64/00b647c4.md)
- [00b64c44](../00b64/00b64c44.md)

## 呼び出し先

- [00af7190](../00af7/00af7190.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 183 bytes

~~~c

void _ZN8firebase4util23GetMessageFromExceptionEP7_JNIEnvP8_jobject(void)

{
  (*(code *)PTR__ZN8firebase4util23GetMessageFromExceptionEP7_JNIEnvP8_jobject_00c1d820)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddfd0"></a> `00bddfd0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddfd4"></a> `00bddfd4` | `11 12 44 f9` | ldr x17,[x16, #0x820] | `FALL_THROUGH`
<a id="insn-00bddfd8"></a> `00bddfd8` | `10 82 20 91` | add x16,x16,#0x820 | `FALL_THROUGH`
<a id="insn-00bddfdc"></a> `00bddfdc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddfd0`](#insn-00bddfd0) 範囲 `[['00bddfd0', '00bddfdf']]`

## 命令位置別の参照

- [`00bddfd4`](#insn-00bddfd4) → `00c1d820`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddfdc`](#insn-00bddfdc) → [`00af7190`](../00af7/00af7190.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00af7190` · 推定シンボル `_ZN8firebase4util23GetMessageFromExceptionEP7_JNIEnvP8_jobject` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddfd4`](#insn-00bddfd4)

~~~json
{
  "source": "00bddfd4",
  "target": "00c1d820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d820",
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
  "target": "00af7190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
