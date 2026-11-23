# 00bdcbe0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdcb30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdc/00bdcb30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0014.md#compare-b01f5683684e085dbfbac523453b94c3)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdcc30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdc/00bdcc30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0015.md#compare-1e5ee1d0e41c443995a0d55ffe4e5b53)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdcbe0",
  "name": "_ZN5Botan10Extensions3addEPNS_21Certificate_ExtensionEb",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f6f5fd43a239adfc81d7736c400406bc1ac519fe2d0f2398753bf996040ba4cc",
  "source_text_sha256": "f6f5fd43a239adfc81d7736c400406bc1ac519fe2d0f2398753bf996040ba4cc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdcbe0",
        "00bdcbef"
      ]
    ],
    "bytes_sha256": "b9245e47d5c966fa97d005b337d6352d34e2123a7e43d2384eac50fbb472ce26",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [004e0038](../004e0/004e0038.md)
- [004ef204](../004ef/004ef204.md)
- [0050a638](../0050a/0050a638.md)
- [0050b45c](../0050b/0050b45c.md)

## 呼び出し先

- [004e01ec](../004e0/004e01ec.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 169 bytes

~~~c

void _ZN5Botan10Extensions3addEPNS_21Certificate_ExtensionEb(void)

{
  (*(code *)PTR__ZN5Botan10Extensions3addEPNS_21Certificate_ExtensionEb_00c1ce80)();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdcbe0"></a> `00bdcbe0` | `10 02 00 90` | adrp x16,0xc1c000 | `FALL_THROUGH`
<a id="insn-00bdcbe4"></a> `00bdcbe4` | `11 42 47 f9` | ldr x17,[x16, #0xe80] | `FALL_THROUGH`
<a id="insn-00bdcbe8"></a> `00bdcbe8` | `10 02 3a 91` | add x16,x16,#0xe80 | `FALL_THROUGH`
<a id="insn-00bdcbec"></a> `00bdcbec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdcbe0`](#insn-00bdcbe0) 範囲 `[['00bdcbe0', '00bdcbef']]`

## 命令位置別の参照

- [`00bdcbe4`](#insn-00bdcbe4) → `00c1ce80`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdcbec`](#insn-00bdcbec) → [`004e01ec`](../004e0/004e01ec.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `004e01ec` · 推定シンボル `_ZN5Botan10Extensions3addEPNS_21Certificate_ExtensionEb` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcbe4`](#insn-00bdcbe4)

~~~json
{
  "source": "00bdcbe4",
  "target": "00c1ce80",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1ce80",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdcbec`](#insn-00bdcbec)

~~~json
{
  "source": "00bdcbec",
  "target": "004e01ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
