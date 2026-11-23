# 00bdbaa0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bdbb50`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bdb/00bdbb50.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0012.md#compare-5140073310a7712138827508d570c121)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbaa0",
  "name": "_ZNSt6__ndk15stoulERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f11e3a988f6023f3ad23bec6ed3694f033c1012a46db53a6f6e9003aed9ee6a5",
  "source_text_sha256": "f11e3a988f6023f3ad23bec6ed3694f033c1012a46db53a6f6e9003aed9ee6a5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbaa0",
        "00bdbaaf"
      ]
    ],
    "bytes_sha256": "dd894e3abc1bedda41401251fc1fe83cda784dcee9a8c525484a5d28741d94e0",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0048bf84](../0048b/0048bf84.md)

## 呼び出し先

- [00b77e98](../00b77/00b77e98.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 241 bytes

~~~c

void _ZNSt6__ndk15stoulERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi(void)

{
  (*(code *)
    PTR__ZNSt6__ndk15stoulERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi_00c1c588)
            ();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdbaa0"></a> `00bdbaa0` | `10 02 00 b0` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdbaa4"></a> `00bdbaa4` | `11 c6 42 f9` | ldr x17,[x16, #0x588] | `FALL_THROUGH`
<a id="insn-00bdbaa8"></a> `00bdbaa8` | `10 22 16 91` | add x16,x16,#0x588 | `FALL_THROUGH`
<a id="insn-00bdbaac"></a> `00bdbaac` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbaa0`](#insn-00bdbaa0) 範囲 `[['00bdbaa0', '00bdbaaf']]`

## 命令位置別の参照

- [`00bdbaa4`](#insn-00bdbaa4) → `00c1c588`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdbaac`](#insn-00bdbaac) → [`00b77e98`](../00b77/00b77e98.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b77e98` · 推定シンボル `_ZNSt6__ndk15stoulERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbaa4`](#insn-00bdbaa4)

~~~json
{
  "source": "00bdbaa4",
  "target": "00c1c588",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1c588",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdbaac`](#insn-00bdbaac)

~~~json
{
  "source": "00bdbaac",
  "target": "00b77e98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
