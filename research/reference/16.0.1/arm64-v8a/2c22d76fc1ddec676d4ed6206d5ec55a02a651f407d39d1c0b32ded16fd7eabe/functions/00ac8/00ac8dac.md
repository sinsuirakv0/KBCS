# 00ac8dac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00ac8bb0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00ac8/00ac8bb0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/no_difference_in_scope-0012.md#compare-85a4b095cd1456df31fae1801a10858e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ac8e1c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8e1c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0065.md#compare-c8aa17a9edf8bb8eee29d95b7e38d104)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac8dac",
  "name": "FUN_00ac8dac",
  "size": 48,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0055647895b1b708672bdcfa4161ba42d4c01526a2faea2639dba9694dd0fdb9",
  "source_text_sha256": "0055647895b1b708672bdcfa4161ba42d4c01526a2faea2639dba9694dd0fdb9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac8dac",
        "00ac8ddb"
      ]
    ],
    "bytes_sha256": "02584e17ffc9ca219a594a045ed43f1751bd9f1510c204c96aff81a968040751",
    "instruction_count": 12,
    "instruction_bytes": 48,
    "body_bytes": 48,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00789c50](../00789/00789c50.md)
- [0082ac68](../0082a/0082ac68.md)
- [0082cd18](../0082c/0082cd18.md)
- [008c5da4](../008c5/008c5da4.md)
- [00a75dac](../00a75/00a75dac.md)
- [00ac08fc](../00ac0/00ac08fc.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 328 bytes

~~~c

bool FUN_00ac8dac(long param_1)

{
  int iVar1;
  int iVar2;
  
  if ((*(char *)(param_1 + 0x3c) != '\0') && (iVar1 = *(int *)(param_1 + 0x68), iVar1 != 0)) {
    iVar2 = 0;
    if (iVar1 != 0) {
      iVar2 = *(int *)(param_1 + 0x4c) / iVar1;
    }
    return *(int *)(param_1 + 0x4c) != iVar2 * iVar1;
  }
  return false;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ac8dac"></a> `00ac8dac` | `08 f0 40 39` | ldrb w8,[x0, #0x3c] | `FALL_THROUGH`
<a id="insn-00ac8db0"></a> `00ac8db0` | `28 01 00 34` | cbz w8,0x00ac8dd4 | `CONDITIONAL_JUMP`
<a id="insn-00ac8db4"></a> `00ac8db4` | `08 68 40 b9` | ldr w8,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00ac8db8"></a> `00ac8db8` | `e8 00 00 34` | cbz w8,0x00ac8dd4 | `CONDITIONAL_JUMP`
<a id="insn-00ac8dbc"></a> `00ac8dbc` | `09 4c 40 b9` | ldr w9,[x0, #0x4c] | `FALL_THROUGH`
<a id="insn-00ac8dc0"></a> `00ac8dc0` | `2a 0d c8 1a` | sdiv w10,w9,w8 | `FALL_THROUGH`
<a id="insn-00ac8dc4"></a> `00ac8dc4` | `48 a5 08 1b` | msub w8,w10,w8,w9 | `FALL_THROUGH`
<a id="insn-00ac8dc8"></a> `00ac8dc8` | `1f 01 00 71` | cmp w8,#0x0 | `FALL_THROUGH`
<a id="insn-00ac8dcc"></a> `00ac8dcc` | `e0 07 9f 1a` | cset w0,ne | `FALL_THROUGH`
<a id="insn-00ac8dd0"></a> `00ac8dd0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ac8dd4"></a> `00ac8dd4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00ac8dd8"></a> `00ac8dd8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac8dac`](#insn-00ac8dac) 範囲 `[['00ac8dac', '00ac8db3']]`
  - `CONDITIONAL_JUMP` [`00ac8db0`](#insn-00ac8db0) → [`00ac8dd4`](#insn-00ac8dd4)
  - `FALL_THROUGH` [`00ac8db0`](#insn-00ac8db0) → [`00ac8db4`](#insn-00ac8db4)
- ブロック [`00ac8db4`](#insn-00ac8db4) 範囲 `[['00ac8db4', '00ac8dbb']]`
  - `CONDITIONAL_JUMP` [`00ac8db8`](#insn-00ac8db8) → [`00ac8dd4`](#insn-00ac8dd4)
  - `FALL_THROUGH` [`00ac8db8`](#insn-00ac8db8) → [`00ac8dbc`](#insn-00ac8dbc)
- ブロック [`00ac8dbc`](#insn-00ac8dbc) 範囲 `[['00ac8dbc', '00ac8dd3']]`
- ブロック [`00ac8dd4`](#insn-00ac8dd4) 範囲 `[['00ac8dd4', '00ac8ddb']]`

## 命令位置別の参照

- [`00ac8db0`](#insn-00ac8db0) → [`00ac8dd4`](#insn-00ac8dd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac8db8`](#insn-00ac8db8) → [`00ac8dd4`](#insn-00ac8dd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ac8db0`](#insn-00ac8db0)

~~~json
{
  "source": "00ac8db0",
  "target": "00ac8dd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac8db8`](#insn-00ac8db8)

~~~json
{
  "source": "00ac8db8",
  "target": "00ac8dd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
