# 00bbaca8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbad70`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bba/00bbad70.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/high-0010.md#compare-99eabba2dd6cdeefdc4dbcf79755d25b)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbaca8",
  "name": "_ZNSt9bad_allocC2Ev",
  "size": 24,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab239339990f66e97b88d6d7336060653fea683e9f5986b26d582ba337ecda4d",
  "source_text_sha256": "ab239339990f66e97b88d6d7336060653fea683e9f5986b26d582ba337ecda4d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbaca8",
        "00bbacbf"
      ]
    ],
    "bytes_sha256": "c00cc74b2c92341b4eeb9a0982617a554aa2f208610ccb4420e88a9678b8a781",
    "instruction_count": 6,
    "instruction_bytes": 24,
    "body_bytes": 24,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdbaf0](../00bdb/00bdbaf0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 551 bytes

~~~c

void _ZNSt9bad_allocC2Ev(long *param_1)

{
                    /* catch() { ... } // from try @ 00bb45ec with catch @ 00bbacac */
                    /* catch() { ... } // from try @ 00bb7594 with catch @ 00bbacb0 */
                    /* catch() { ... } // from try @ 00bb75ac with catch @ 00bbacb4 */
                    /* catch() { ... } // from try @ 00bb71e4 with catch @ 00bbacb8 */
  *param_1 = (long)(PTR__ZTVSt9bad_alloc_00c1bf18 + 0x10);
                    /* catch() { ... } // from try @ 00bb71fc with catch @ 00bbacbc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbaca8"></a> `00bbaca8` | `5f 24 03 d5` | bti c | `FALL_THROUGH`
<a id="insn-00bbacac"></a> `00bbacac` | `08 03 00 b0` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00bbacb0"></a> `00bbacb0` | `08 8d 47 f9` | ldr x8,[x8, #0xf18] | `FALL_THROUGH`
<a id="insn-00bbacb4"></a> `00bbacb4` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bbacb8"></a> `00bbacb8` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbacbc"></a> `00bbacbc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbaca8`](#insn-00bbaca8) 範囲 `[['00bbaca8', '00bbacab']]`
  - `FALL_THROUGH` [`00bbaca8`](#insn-00bbaca8) → [`00bbacac`](#insn-00bbacac)
- ブロック [`00bbacac`](#insn-00bbacac) 範囲 `[['00bbacac', '00bbacaf']]`
  - `FALL_THROUGH` [`00bbacac`](#insn-00bbacac) → [`00bbacb0`](#insn-00bbacb0)
- ブロック [`00bbacb0`](#insn-00bbacb0) 範囲 `[['00bbacb0', '00bbacb3']]`
  - `FALL_THROUGH` [`00bbacb0`](#insn-00bbacb0) → [`00bbacb4`](#insn-00bbacb4)
- ブロック [`00bbacb4`](#insn-00bbacb4) 範囲 `[['00bbacb4', '00bbacb7']]`
  - `FALL_THROUGH` [`00bbacb4`](#insn-00bbacb4) → [`00bbacb8`](#insn-00bbacb8)
- ブロック [`00bbacb8`](#insn-00bbacb8) 範囲 `[['00bbacb8', '00bbacbb']]`
  - `FALL_THROUGH` [`00bbacb8`](#insn-00bbacb8) → [`00bbacbc`](#insn-00bbacbc)
- ブロック [`00bbacbc`](#insn-00bbacbc) 範囲 `[['00bbacbc', '00bbacbf']]`

## 命令位置別の参照

- [`00bbacb0`](#insn-00bbacb0) → `00c1bf18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bbacb8`](#insn-00bbacb8) → `00c16738`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbacb0`](#insn-00bbacb0)

~~~json
{
  "source": "00bbacb0",
  "target": "00c1bf18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bf18",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbacb8`](#insn-00bbacb8)

~~~json
{
  "source": "00bbacb8",
  "target": "00c16738",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c16728",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
