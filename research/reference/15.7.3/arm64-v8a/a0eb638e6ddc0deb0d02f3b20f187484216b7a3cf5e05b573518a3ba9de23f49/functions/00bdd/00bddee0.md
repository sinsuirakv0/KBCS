# 00bddee0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bdde30`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bdde30.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0017.md#compare-affb4887ecd6df98c54260532c9cab49)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddf30`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddf30.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-9412a110a8f9b7087e249efd14c820e6)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddee0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalImZNS0_26CompleteWithResultInternalImEEvRKNS_12FutureHandleEiPKcRKT_EUlPmE_EEvS5_iS7_RKT0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b45a29577eec0762946fc14e6a7110cdb53868d36af2a60417454141455596a3",
  "source_text_sha256": "b45a29577eec0762946fc14e6a7110cdb53868d36af2a60417454141455596a3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddee0",
        "00bddeef"
      ]
    ],
    "bytes_sha256": "cc7cfe8a253f8f3b84d21acc2eea57a9cd822407d8ec0e3b8b84afac1ad9b78a",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae3a08](../00ae3/00ae3a08.md)

## 呼び出し先

- [00ae3b80](../00ae3/00ae3b80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 379 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalImZNS0_26CompleteWithResultInternalImEEvRKNS_12FutureHandleEiPKcRKT_EUlPmE_EEvS5_iS7_RKT0_
               (void)

{
  (*(code *)
    PTR__ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalImZNS0_26CompleteWithResultInternalImEEvRKNS_12FutureHandleEiPKcRKT_EUlPmE_EEvS5_iS7_RKT0__00c1d800
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddee0"></a> `00bddee0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddee4"></a> `00bddee4` | `11 02 44 f9` | ldr x17,[x16, #0x800] | `FALL_THROUGH`
<a id="insn-00bddee8"></a> `00bddee8` | `10 02 20 91` | add x16,x16,#0x800 | `FALL_THROUGH`
<a id="insn-00bddeec"></a> `00bddeec` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddee0`](#insn-00bddee0) 範囲 `[['00bddee0', '00bddeef']]`

## 命令位置別の参照

- [`00bddee4`](#insn-00bddee4) → `00c1d800`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddeec`](#insn-00bddeec) → [`00ae3b80`](../00ae3/00ae3b80.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00ae3b80` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalImZNS0_26CompleteWithResultInternalImEEvRKNS_12FutureHandleEiPKcRKT_EUlPmE_EEvS5_iS7_RKT0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddee4`](#insn-00bddee4)

~~~json
{
  "source": "00bddee4",
  "target": "00c1d800",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d800",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddeec`](#insn-00bddeec)

~~~json
{
  "source": "00bddeec",
  "target": "00ae3b80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
