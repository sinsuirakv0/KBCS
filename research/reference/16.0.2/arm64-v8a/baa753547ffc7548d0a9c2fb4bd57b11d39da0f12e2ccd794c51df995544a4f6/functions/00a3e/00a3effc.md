# 00a3effc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a3efa8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a3e/00a3efa8.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0033.md#compare-45e1c215b356c8fe88d737e673eeb8f7)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00a3fff0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a3f/00a3fff0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0027.md#compare-b70b6624145ea070b925f5b89f11a539)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a3effc",
  "name": "FUN_00a3effc",
  "size": 56,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6abdffaf70bff64d912889ba9af11670bde7847b85d8212fa9ea4696f7fb36a9",
  "source_text_sha256": "6abdffaf70bff64d912889ba9af11670bde7847b85d8212fa9ea4696f7fb36a9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a3effc",
        "00a3f033"
      ]
    ],
    "bytes_sha256": "023b8c0b2700209a88b8cde462f3c39363fae8aa037d6395a6083b51d0ae6fbd",
    "instruction_count": 14,
    "instruction_bytes": 56,
    "body_bytes": 56,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a3ea24](../00a3e/00a3ea24.md)

## 呼び出し先

- [005c17dc](../005c1/005c17dc.md)
- [00c57f80](../00c57/00c57f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 221 bytes

~~~c

void FUN_00a3effc(void *param_1)

{
  FUN_005c17dc((long)param_1 + 0x28,*(undefined8 *)((long)param_1 + 0x30));
  FUN_005c17dc((long)param_1 + 0x10,*(undefined8 *)((long)param_1 + 0x18));
  _ZdlPv(param_1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a3effc"></a> `00a3effc` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00a3f000"></a> `00a3f000` | `f3 0b 00 f9` | str x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3f004"></a> `00a3f004` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a3f008"></a> `00a3f008` | `01 18 40 f9` | ldr x1,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00a3f00c"></a> `00a3f00c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a3f010"></a> `00a3f010` | `00 a0 00 91` | add x0,x0,#0x28 | `FALL_THROUGH`
<a id="insn-00a3f014"></a> `00a3f014` | `f2 09 ee 97` | bl 0x005c17dc | `UNCONDITIONAL_CALL`
<a id="insn-00a3f018"></a> `00a3f018` | `61 0e 40 f9` | ldr x1,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a3f01c"></a> `00a3f01c` | `60 42 00 91` | add x0,x19,#0x10 | `FALL_THROUGH`
<a id="insn-00a3f020"></a> `00a3f020` | `ef 09 ee 97` | bl 0x005c17dc | `UNCONDITIONAL_CALL`
<a id="insn-00a3f024"></a> `00a3f024` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00a3f028"></a> `00a3f028` | `f3 0b 40 f9` | ldr x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a3f02c"></a> `00a3f02c` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00a3f030"></a> `00a3f030` | `d4 63 08 14` | b 0x00c57f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a3effc`](#insn-00a3effc) 範囲 `[['00a3effc', '00a3f033']]`

## 命令位置別の参照

- [`00a3effc`](#insn-00a3effc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3f000`](#insn-00a3f000) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3f014`](#insn-00a3f014) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`
- [`00a3f020`](#insn-00a3f020) → [`005c17dc`](../005c1/005c17dc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c17dc` · 推定シンボル `None` · 推定型 `None`
- [`00a3f028`](#insn-00a3f028) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3f02c`](#insn-00a3f02c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a3f030`](#insn-00a3f030) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a3effc`](#insn-00a3effc)

~~~json
{
  "source": "00a3effc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3f000`](#insn-00a3f000)

~~~json
{
  "source": "00a3f000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3f014`](#insn-00a3f014)

~~~json
{
  "source": "00a3f014",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3f020`](#insn-00a3f020)

~~~json
{
  "source": "00a3f020",
  "target": "005c17dc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a3f028`](#insn-00a3f028)

~~~json
{
  "source": "00a3f028",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3f02c`](#insn-00a3f02c)

~~~json
{
  "source": "00a3f02c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a3f030`](#insn-00a3f030)

~~~json
{
  "source": "00a3f030",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
