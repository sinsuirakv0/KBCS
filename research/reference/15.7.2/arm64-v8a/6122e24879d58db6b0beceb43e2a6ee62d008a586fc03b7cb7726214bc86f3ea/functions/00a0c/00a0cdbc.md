# 00a0cdbc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a0cdbc`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0c/00a0cdbc.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/no_difference_in_scope-0018.md#compare-bbd5bffd9173b9508c38ff161d418472)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a0cdbc",
  "name": "FUN_00a0cdbc",
  "size": 36,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97c3bedd2ceb5fd60cd3c0667f584bd026556dd77f01fc045ba48b6591157948",
  "source_text_sha256": "97c3bedd2ceb5fd60cd3c0667f584bd026556dd77f01fc045ba48b6591157948",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a0cdbc",
        "00a0cddf"
      ]
    ],
    "bytes_sha256": "001cea629d01b9470bf8b8efae88d1c5ab48bb7279c1fd14d17f4d82694d11e2",
    "instruction_count": 9,
    "instruction_bytes": 36,
    "body_bytes": 36,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006d6d04](../006d6/006d6d04.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 224 bytes

~~~c

void FUN_00a0cdbc(long param_1)

{
  if ((*(int *)(param_1 + 0x84) != -1) && (*(int *)(param_1 + 0x84) <= *(int *)(param_1 + 0x80))) {
    return;
  }
  *(int *)(param_1 + 0x80) = *(int *)(param_1 + 0x80) + 1;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a0cdbc"></a> `00a0cdbc` | `08 24 50 29` | ldp w8,w9,[x0, #0x80] | `FALL_THROUGH`
<a id="insn-00a0cdc0"></a> `00a0cdc0` | `3f 05 00 31` | cmn w9,#0x1 | `FALL_THROUGH`
<a id="insn-00a0cdc4"></a> `00a0cdc4` | `80 00 00 54` | b.eq 0x00a0cdd4 | `CONDITIONAL_JUMP`
<a id="insn-00a0cdc8"></a> `00a0cdc8` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00a0cdcc"></a> `00a0cdcc` | `4c 00 00 54` | b.gt 0x00a0cdd4 | `CONDITIONAL_JUMP`
<a id="insn-00a0cdd0"></a> `00a0cdd0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a0cdd4"></a> `00a0cdd4` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00a0cdd8"></a> `00a0cdd8` | `08 80 00 b9` | str w8,[x0, #0x80] | `FALL_THROUGH`
<a id="insn-00a0cddc"></a> `00a0cddc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a0cdbc`](#insn-00a0cdbc) 範囲 `[['00a0cdbc', '00a0cdc7']]`
  - `CONDITIONAL_JUMP` [`00a0cdc4`](#insn-00a0cdc4) → [`00a0cdd4`](#insn-00a0cdd4)
  - `FALL_THROUGH` [`00a0cdc4`](#insn-00a0cdc4) → [`00a0cdc8`](#insn-00a0cdc8)
- ブロック [`00a0cdc8`](#insn-00a0cdc8) 範囲 `[['00a0cdc8', '00a0cdcf']]`
  - `CONDITIONAL_JUMP` [`00a0cdcc`](#insn-00a0cdcc) → [`00a0cdd4`](#insn-00a0cdd4)
  - `FALL_THROUGH` [`00a0cdcc`](#insn-00a0cdcc) → [`00a0cdd0`](#insn-00a0cdd0)
- ブロック [`00a0cdd0`](#insn-00a0cdd0) 範囲 `[['00a0cdd0', '00a0cdd3']]`
- ブロック [`00a0cdd4`](#insn-00a0cdd4) 範囲 `[['00a0cdd4', '00a0cddf']]`

## 命令位置別の参照

- [`00a0cdc4`](#insn-00a0cdc4) → [`00a0cdd4`](#insn-00a0cdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0cdcc`](#insn-00a0cdcc) → [`00a0cdd4`](#insn-00a0cdd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a0cdc4`](#insn-00a0cdc4)

~~~json
{
  "source": "00a0cdc4",
  "target": "00a0cdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0cdcc`](#insn-00a0cdcc)

~~~json
{
  "source": "00a0cdcc",
  "target": "00a0cdd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
