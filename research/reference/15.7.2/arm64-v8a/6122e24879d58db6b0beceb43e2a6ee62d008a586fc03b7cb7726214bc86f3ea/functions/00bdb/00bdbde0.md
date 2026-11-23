# 00bdbde0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbe90`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbe90.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-86c17b244d65d15612d91f842b4f4ea1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbde0",
  "name": "_ZN5Botan11BlockCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "30ada28634bb2c746c63614fb3d9519073babe7ed53e652e611f564fffbf62be",
  "source_text_sha256": "30ada28634bb2c746c63614fb3d9519073babe7ed53e652e611f564fffbf62be",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbde0",
        "00bdbdef"
      ]
    ],
    "bytes_sha256": "bdb68c06cce365bcd5ac6228bd5458e7726c719471dc7b96cfa8db798b3464d2",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00499128](../00499/00499128.md)
- [004993a0](../00499/004993a0.md)
- [004a3d70](../004a3/004a3d70.md)

## 呼び出し先

- [00498d9c](../00498/00498d9c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 287 bytes

~~~c

void _ZN5Botan11BlockCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_
               (void)

{
  (*(code *)
    PTR__ZN5Botan11BlockCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9__00c1c728
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbde0"></a> `00bdbde0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbde4"></a> `00bdbde4` | `11 96 43 f9` | ldr x17,[x16, #0x728] | `FALL_THROUGH`
<a id="insn-00bdbde8"></a> `00bdbde8` | `10 a2 1c 91` | add x16,x16,#0x728 | `FALL_THROUGH`
<a id="insn-00bdbdec"></a> `00bdbdec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbde0`](#insn-00bdbde0) 範囲 `[['00bdbde0', '00bdbdef']]`

## 命令位置別の参照

- [`00bdbde4`](#insn-00bdbde4) → `00c1c728`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbdec`](#insn-00bdbdec) → [`00498d9c`](../00498/00498d9c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00498d9c` · 推定シンボル `_ZN5Botan11BlockCipher6createERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEES9_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbde4`](#insn-00bdbde4)

~~~json
{
  "source": "00bdbde4",
  "target": "00c1c728",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c728",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbdec`](#insn-00bdbdec)

~~~json
{
  "source": "00bdbdec",
  "target": "00498d9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
