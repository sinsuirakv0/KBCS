# 00bddef0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdde40`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde40.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-328c94992fecd157e2b705954d619e2a)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddf40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf40.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-8bd2a1f794a41372e97f5f7487bf8a51)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddef0",
  "name": "_ZN8firebase6FutureINSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "09f823d6f68272c8629b074f44066f166434fc1308a10d0be9070f7949ffc2cc",
  "source_text_sha256": "09f823d6f68272c8629b074f44066f166434fc1308a10d0be9070f7949ffc2cc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddef0",
        "00bddeff"
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

- [00ae2bc8](../00ae2/00ae2bc8.md)
- [00b4de04](../00b4d/00b4de04.md)
- [00b6eeac](../00b6e/00b6eeac.md)

## 呼び出し先

- [00ae2ef0](../00ae2/00ae2ef0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 369 bytes

~~~c

void _ZN8firebase6FutureINSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
               (void)

{
  (*(code *)
    PTR__ZN8firebase6FutureINSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE_00c1d808
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddef0"></a> `00bddef0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddef4"></a> `00bddef4` | `11 06 44 f9` | ldr x17,[x16, #0x808] | `FALL_THROUGH`
<a id="insn-00bddef8"></a> `00bddef8` | `10 22 20 91` | add x16,x16,#0x808 | `FALL_THROUGH`
<a id="insn-00bddefc"></a> `00bddefc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddef0`](#insn-00bddef0) 範囲 `[['00bddef0', '00bddeff']]`

## 命令位置別の参照

- [`00bddef4`](#insn-00bddef4) → `00c1d808`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddefc`](#insn-00bddefc) → [`00ae2ef0`](../00ae2/00ae2ef0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae2ef0` · 推定シンボル `_ZN8firebase6FutureINSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddef4`](#insn-00bddef4)

~~~json
{
  "source": "00bddef4",
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
- 参照命令 [`00bddefc`](#insn-00bddefc)

~~~json
{
  "source": "00bddefc",
  "target": "00ae2ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
