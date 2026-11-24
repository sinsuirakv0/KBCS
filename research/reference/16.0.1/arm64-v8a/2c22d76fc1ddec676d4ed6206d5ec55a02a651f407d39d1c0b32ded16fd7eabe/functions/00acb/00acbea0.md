# 00acbea0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acbca4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00acb/00acbca4.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/detail_skipped-0005.md#compare-1a1aa87b39f3dd60edd0ef794df1195e)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acbf10`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acbf10.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/detail_skipped-0006.md#compare-99b1c1540466820bd2782a6f79ac1148)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acbea0",
  "name": "FUN_00acbea0",
  "size": 60,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b089ddbdd9f80c5b274189f9e05c05ec6395569ded36eec3a3b15bc878989392",
  "source_text_sha256": "b089ddbdd9f80c5b274189f9e05c05ec6395569ded36eec3a3b15bc878989392",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acbea0",
        "00acbedb"
      ]
    ],
    "bytes_sha256": "d740f6e81e44900d593a8109a669a4af56062ffa417116484b6ee3dcab302ba3",
    "instruction_count": 15,
    "instruction_bytes": 60,
    "body_bytes": 60,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [0073202c](../00732/0073202c.md)
- [00935b10](../00935/00935b10.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 454 bytes

~~~c

int FUN_00acbea0(long param_1)

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
      iVar2 = *(int *)(lVar3 + 8) + iVar2;
      lVar1 = *(long *)(param_1 + 0x30);
      lVar3 = param_1;
    } while (*(long *)(param_1 + 0x30) != 0);
  }
  return *(int *)(param_1 + 8) + iVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acbea0"></a> `00acbea0` | `09 18 40 f9` | ldr x9,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00acbea4"></a> `00acbea4` | `49 01 00 b4` | cbz x9,0x00acbecc | `CONDITIONAL_JUMP`
<a id="insn-00acbea8"></a> `00acbea8` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acbeac"></a> `00acbeac` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00acbeb0"></a> `00acbeb0` | `4a 09 40 b9` | ldr w10,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00acbeb4"></a> `00acbeb4` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00acbeb8"></a> `00acbeb8` | `29 19 40 f9` | ldr x9,[x9, #0x30] | `FALL_THROUGH`
<a id="insn-00acbebc"></a> `00acbebc` | `48 01 08 0b` | add w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00acbec0"></a> `00acbec0` | `ea 03 00 aa` | mov x10,x0 | `FALL_THROUGH`
<a id="insn-00acbec4"></a> `00acbec4` | `69 ff ff b5` | cbnz x9,0x00acbeb0 | `CONDITIONAL_JUMP`
<a id="insn-00acbec8"></a> `00acbec8` | `02 00 00 14` | b 0x00acbed0 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbecc"></a> `00acbecc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00acbed0"></a> `00acbed0` | `09 08 40 b9` | ldr w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00acbed4"></a> `00acbed4` | `20 01 08 0b` | add w0,w9,w8 | `FALL_THROUGH`
<a id="insn-00acbed8"></a> `00acbed8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acbea0`](#insn-00acbea0) 範囲 `[['00acbea0', '00acbea7']]`
  - `CONDITIONAL_JUMP` [`00acbea4`](#insn-00acbea4) → [`00acbecc`](#insn-00acbecc)
  - `FALL_THROUGH` [`00acbea4`](#insn-00acbea4) → [`00acbea8`](#insn-00acbea8)
- ブロック [`00acbea8`](#insn-00acbea8) 範囲 `[['00acbea8', '00acbeaf']]`
  - `FALL_THROUGH` [`00acbeac`](#insn-00acbeac) → [`00acbeb0`](#insn-00acbeb0)
- ブロック [`00acbeb0`](#insn-00acbeb0) 範囲 `[['00acbeb0', '00acbec7']]`
  - `CONDITIONAL_JUMP` [`00acbec4`](#insn-00acbec4) → [`00acbeb0`](#insn-00acbeb0)
  - `FALL_THROUGH` [`00acbec4`](#insn-00acbec4) → [`00acbec8`](#insn-00acbec8)
- ブロック [`00acbec8`](#insn-00acbec8) 範囲 `[['00acbec8', '00acbecb']]`
  - `UNCONDITIONAL_JUMP` [`00acbec8`](#insn-00acbec8) → [`00acbed0`](#insn-00acbed0)
- ブロック [`00acbecc`](#insn-00acbecc) 範囲 `[['00acbecc', '00acbecf']]`
  - `FALL_THROUGH` [`00acbecc`](#insn-00acbecc) → [`00acbed0`](#insn-00acbed0)
- ブロック [`00acbed0`](#insn-00acbed0) 範囲 `[['00acbed0', '00acbedb']]`

## 命令位置別の参照

- [`00acbea4`](#insn-00acbea4) → [`00acbecc`](#insn-00acbecc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbec4`](#insn-00acbec4) → [`00acbeb0`](#insn-00acbeb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbec8`](#insn-00acbec8) → [`00acbed0`](#insn-00acbed0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acbea4`](#insn-00acbea4)

~~~json
{
  "source": "00acbea4",
  "target": "00acbecc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbec4`](#insn-00acbec4)

~~~json
{
  "source": "00acbec4",
  "target": "00acbeb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbec8`](#insn-00acbec8)

~~~json
{
  "source": "00acbec8",
  "target": "00acbed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
