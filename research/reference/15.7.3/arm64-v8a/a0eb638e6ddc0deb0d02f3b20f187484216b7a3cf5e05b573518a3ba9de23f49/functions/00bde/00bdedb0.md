# 00bdedb0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bded00`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bde/00bded00.md) · 移動量 `+0xb0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0007.md#compare-3316ab83ee2c1450da5f27ca091e79c4)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bdee00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bde/00bdee00.md) · 移動量 `+0x50`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0020.md#compare-b860086581d00427151cf9160e474788)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdedb0",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_",
  "size": 16,
  "external": 0,
  "thunk": 1,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3b866cc501bed6aac47765152fb4d534fa4e307256fba3ce1b9ae231c1046a99",
  "source_text_sha256": "3b866cc501bed6aac47765152fb4d534fa4e307256fba3ce1b9ae231c1046a99",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdedb0",
        "00bdedbf"
      ]
    ],
    "bytes_sha256": "49b5450116fa7c4bd8c0c35cb1a109463b24aca324aabfd47e9bd30695aef50c",
    "instruction_count": 4,
    "instruction_bytes": 16,
    "body_bytes": 16,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aff21c](../00aff/00aff21c.md)
- [00b016d0](../00b01/00b016d0.md)
- [00b02854](../00b02/00b02854.md)
- [00b0ddbc](../00b0d/00b0ddbc.md)
- [00b0df30](../00b0d/00b0df30.md)
- [00b0e1e8](../00b0e/00b0e1e8.md)
- [00b4b688](../00b4b/00b4b688.md)
- [00b4d204](../00b4d/00b4d204.md)
- [00b4d4d4](../00b4d/00b4d4d4.md)
- [00b4d7a8](../00b4d/00b4d7a8.md)
- [00b4da78](../00b4d/00b4da78.md)
- [00b4e440](../00b4e/00b4e440.md)
- [00b4e6a8](../00b4e/00b4e6a8.md)
- [00b4eb14](../00b4e/00b4eb14.md)
- [00b5602c](../00b56/00b5602c.md)
- [00b56e34](../00b56/00b56e34.md)
- [00b5715c](../00b57/00b5715c.md)
- [00b573f4](../00b57/00b573f4.md)
- [00b57b08](../00b57/00b57b08.md)
- [00b580c4](../00b58/00b580c4.md)
- [00b5fb44](../00b5f/00b5fb44.md)
- [00b5fd90](../00b5f/00b5fd90.md)
- [00b7000c](../00b70/00b7000c.md)

## 呼び出し先

- [00b00f3c](../00b00/00b00f3c.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 351 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_
               (void)

{
  (*(code *)
    PTR__ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0__00c1df68
  )();
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdedb0"></a> `00bdedb0` | `f0 01 00 f0` | adrp x16,0xc1d000 | `FALL_THROUGH`
<a id="insn-00bdedb4"></a> `00bdedb4` | `11 b6 47 f9` | ldr x17,[x16, #0xf68] | `FALL_THROUGH`
<a id="insn-00bdedb8"></a> `00bdedb8` | `10 a2 3d 91` | add x16,x16,#0xf68 | `FALL_THROUGH`
<a id="insn-00bdedbc"></a> `00bdedbc` | `20 02 1f d6` | br x17 | `COMPUTED_CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdedb0`](#insn-00bdedb0) 範囲 `[['00bdedb0', '00bdedbf']]`

## 命令位置別の参照

- [`00bdedb4`](#insn-00bdedb4) → `00c1df68`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bdedbc`](#insn-00bdedbc) → [`00b00f3c`](../00b00/00b00f3c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00b00f3c` · 推定シンボル `_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalIvEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS5_iS7_RKT0_` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdedb4`](#insn-00bdedb4)

~~~json
{
  "source": "00bdedb4",
  "target": "00c1df68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1df68",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bdedbc`](#insn-00bdedbc)

~~~json
{
  "source": "00bdedbc",
  "target": "00b00f3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
