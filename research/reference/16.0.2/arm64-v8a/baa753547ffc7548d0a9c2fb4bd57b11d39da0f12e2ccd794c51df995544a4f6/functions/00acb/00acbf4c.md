# 00acbf4c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acbedc`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acb/00acbedc.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/detail_skipped-0006.md#compare-9db30ceb9584937b7df9a5242da60b2d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00accf40`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00acc/00accf40.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/detail_skipped-0005.md#compare-42f8ef355fb29985891efd18e988964f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbf4c",
  "name": "FUN_00acbf4c",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4d33a67ff2c22311469f73f3493a48782ecd262cb35ef51d78f5853b75ca21fd",
  "source_text_sha256": "4d33a67ff2c22311469f73f3493a48782ecd262cb35ef51d78f5853b75ca21fd",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbf4c",
        "00acbf87"
      ]
    ],
    "bytes_sha256": "7e7e1cda346a3bbb3103eba76ed8c923a01ef901c1edd08adfe9a5a12457a4fb",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00732084](../00732/00732084.md)
- [00935b64](../00935/00935b64.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 458 bytes

~~~c

int FUN_00acbf4c(long param_1)

{
  long lVar1;
  int iVar2;
  long lVar3;
  
  if (*(long *)(param_1 + 0x30) == 0) {
    iVar2 = 0;
  }
  else {
    iVar2 = 0;
    lVar1 = *(long *)(param_1 + 0x30);
    lVar3 = param_1;
    do {
      param_1 = lVar1;
      iVar2 = *(int *)(lVar3 + 0xc) + iVar2;
      lVar1 = *(long *)(param_1 + 0x30);
      lVar3 = param_1;
    } while (*(long *)(param_1 + 0x30) != 0);
  }
  return *(int *)(param_1 + 0xc) + iVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acbf4c"></a> `00acbf4c` | `09 18 40 f9` | ldr x9,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00acbf50"></a> `00acbf50` | `49 01 00 b4` | cbz x9,0x00acbf78 | `CONDITIONAL_JUMP`
<a id="insn-00acbf54"></a> `00acbf54` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acbf58"></a> `00acbf58` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00acbf5c"></a> `00acbf5c` | `4a 0d 40 b9` | ldr w10,[x10, #0xc] | `FALL_THROUGH`
<a id="insn-00acbf60"></a> `00acbf60` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00acbf64"></a> `00acbf64` | `29 19 40 f9` | ldr x9,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00acbf68"></a> `00acbf68` | `48 01 08 0b` | add w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00acbf6c"></a> `00acbf6c` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00acbf70"></a> `00acbf70` | `69 ff ff b5` | cbnz x9,0x00acbf5c | `CONDITIONAL_JUMP`
<a id="insn-00acbf74"></a> `00acbf74` | `02 00 00 14` | b 0x00acbf7c | `UNCONDITIONAL_JUMP`
<a id="insn-00acbf78"></a> `00acbf78` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acbf7c"></a> `00acbf7c` | `09 0c 40 b9` | ldr w9,[x0, #0xc] | `FALL_THROUGH`
<a id="insn-00acbf80"></a> `00acbf80` | `20 01 08 0b` | add w0,w9,w8 | `FALL_THROUGH`
<a id="insn-00acbf84"></a> `00acbf84` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbf4c`](#insn-00acbf4c) 範囲 `[['00acbf4c', '00acbf53']]`
  - `CONDITIONAL_JUMP` [`00acbf50`](#insn-00acbf50) → [`00acbf78`](#insn-00acbf78)
  - `FALL_THROUGH` [`00acbf50`](#insn-00acbf50) → [`00acbf54`](#insn-00acbf54)
- ブロック [`00acbf54`](#insn-00acbf54) 範囲 `[['00acbf54', '00acbf5b']]`
  - `FALL_THROUGH` [`00acbf58`](#insn-00acbf58) → [`00acbf5c`](#insn-00acbf5c)
- ブロック [`00acbf5c`](#insn-00acbf5c) 範囲 `[['00acbf5c', '00acbf73']]`
  - `CONDITIONAL_JUMP` [`00acbf70`](#insn-00acbf70) → [`00acbf5c`](#insn-00acbf5c)
  - `FALL_THROUGH` [`00acbf70`](#insn-00acbf70) → [`00acbf74`](#insn-00acbf74)
- ブロック [`00acbf74`](#insn-00acbf74) 範囲 `[['00acbf74', '00acbf77']]`
  - `UNCONDITIONAL_JUMP` [`00acbf74`](#insn-00acbf74) → [`00acbf7c`](#insn-00acbf7c)
- ブロック [`00acbf78`](#insn-00acbf78) 範囲 `[['00acbf78', '00acbf7b']]`
  - `FALL_THROUGH` [`00acbf78`](#insn-00acbf78) → [`00acbf7c`](#insn-00acbf7c)
- ブロック [`00acbf7c`](#insn-00acbf7c) 範囲 `[['00acbf7c', '00acbf87']]`

## 命令位置別の参照

- [`00acbf50`](#insn-00acbf50) → [`00acbf78`](#insn-00acbf78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf70`](#insn-00acbf70) → [`00acbf5c`](#insn-00acbf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbf74`](#insn-00acbf74) → [`00acbf7c`](#insn-00acbf7c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbf50`](#insn-00acbf50)

~~~json
{
  "source": "00acbf50",
  "target": "00acbf78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf70`](#insn-00acbf70)

~~~json
{
  "source": "00acbf70",
  "target": "00acbf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbf74`](#insn-00acbf74)

~~~json
{
  "source": "00acbf74",
  "target": "00acbf7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
