# 00bddcb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bddc00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bdd/00bddc00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0016.md#compare-350185569d3f0c5f960d3f8ee70611d9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bddd00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bdd/00bddd00.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0018.md#compare-cc954493029dd7822c67d4f83e09dfac)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddcb0",
  "name": "<EXTERNAL>::atan2",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5727e89c50c7d863d5de3f52de6e7268294db7a53acdeca34ac82841257e4bc8",
  "source_text_sha256": "5727e89c50c7d863d5de3f52de6e7268294db7a53acdeca34ac82841257e4bc8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddcb0",
        "00bddcbf"
      ]
    ],
    "bytes_sha256": "e4f31301889faae26089dd26b7791a52486a4ad0be23bc3fead4f4f7888e6778",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a17ce0](../00a17/00a17ce0.md)

## 呼び出し先

- [010a5568](../010a5/010a5568.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 207 bytes

~~~c

/* WARNING: Unknown calling convention -- yet parameter storage is locked */

double atan2(double __y,double __x)

{
  double dVar1;
  
  dVar1 = (double)(*(code *)PTR_atan2_00c1d6e8)();
  return dVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddcb0"></a> `00bddcb0` | `10 02 00 90` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bddcb4"></a> `00bddcb4` | `11 76 43 f9` | ldr x17,[x16, #0x6e8] | `FALL_THROUGH`
<a id="insn-00bddcb8"></a> `00bddcb8` | `10 a2 1b 91` | add x16,x16,#0x6e8 | `FALL_THROUGH`
<a id="insn-00bddcbc"></a> `00bddcbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddcb0`](#insn-00bddcb0) 範囲 `[['00bddcb0', '00bddcbf']]`

## 命令位置別の参照

- [`00bddcb4`](#insn-00bddcb4) → `00c1d6e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddcbc`](#insn-00bddcbc) → [`010a5568`](../010a5/010a5568.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `010a5568` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddcb4`](#insn-00bddcb4)

~~~json
{
  "source": "00bddcb4",
  "target": "00c1d6e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1d6e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddcbc`](#insn-00bddcbc)

~~~json
{
  "source": "00bddcbc",
  "target": "010a5568",
  "target_space": "ram",
  "resolution": "function"
}
~~~
