# 00acaff8

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00acadfc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aca/00acadfc.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0007.md#compare-06e74ba9e3d2d11635162168c2322b03)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00acb068`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00acb/00acb068.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0008.md#compare-f6cfdade836a0d46c5fb97434c27a032)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acaff8",
  "name": "FUN_00acaff8",
  "size": 112,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "36d92829ea4bca1d4583f3b7a4436cce2ece5843f5b82ee612df3fa2b882b77c",
  "source_text_sha256": "36d92829ea4bca1d4583f3b7a4436cce2ece5843f5b82ee612df3fa2b882b77c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acaff8",
        "00acb067"
      ]
    ],
    "bytes_sha256": "aa184a18de0907a1f77e9b8e323138f78128c91d20e4ba6f258b7794466b8dd7",
    "instruction_count": 28,
    "instruction_bytes": 112,
    "body_bytes": 112,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00789de0](../00789/00789de0.md)
- [0082fb6c](../0082f/0082fb6c.md)
- [008ff040](../008ff/008ff040.md)
- [00a3e524](../00a3e/00a3e524.md)
- [00ac0a9c](../00ac0/00ac0a9c.md)

## 呼び出し先

- [00759114](../00759/00759114.md)
- [008514f8](../00851/008514f8.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 444 bytes

~~~c

void FUN_00acaff8(long param_1)

{
  int iVar1;
  undefined8 uVar2;
  undefined4 uVar3;
  
  iVar1 = *(int *)(param_1 + 0x9c);
  if (iVar1 == 0) {
    uVar2 = FUN_008514f8();
    uVar3 = 0;
  }
  else {
    if ((iVar1 != 1) && (iVar1 != 2)) {
      return;
    }
    uVar2 = FUN_008514f8();
    FUN_008514f8();
    uVar3 = *(undefined4 *)(PTR_DAT_00c9b508 + (long)*(int *)(param_1 + 0x98) * 4);
  }
  FUN_00759114(uVar2,uVar3,0);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acaff8"></a> `00acaff8` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00acaffc"></a> `00acaffc` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb000"></a> `00acb000` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00acb004"></a> `00acb004` | `08 9c 40 b9` | ldr w8,[x0, #0x9c] | `FALL_THROUGH`
<a id="insn-00acb008"></a> `00acb008` | `e8 01 00 34` | cbz w8,0x00acb044 | `CONDITIONAL_JUMP`
<a id="insn-00acb00c"></a> `00acb00c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acb010"></a> `00acb010` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00acb014"></a> `00acb014` | `60 00 00 54` | b.eq 0x00acb020 | `CONDITIONAL_JUMP`
<a id="insn-00acb018"></a> `00acb018` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00acb01c"></a> `00acb01c` | `01 02 00 54` | b.ne 0x00acb05c | `CONDITIONAL_JUMP`
<a id="insn-00acb020"></a> `00acb020` | `36 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb024"></a> `00acb024` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acb028"></a> `00acb028` | `34 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb02c"></a> `00acb02c` | `89 0e 00 90` | adrp x9,0xc9b000 | `FALL_THROUGH`
<a id="insn-00acb030"></a> `00acb030` | `68 9a 80 b9` | ldrsw x8,[x19, #0x98] | `FALL_THROUGH`
<a id="insn-00acb034"></a> `00acb034` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb038"></a> `00acb038` | `29 85 42 f9` | ldr x9,[x9, #0x508] | `FALL_THROUGH`
<a id="insn-00acb03c"></a> `00acb03c` | `21 79 68 b8` | ldr w1,[x9, x8, LSL #0x2] | `FALL_THROUGH`
<a id="insn-00acb040"></a> `00acb040` | `03 00 00 14` | b 0x00acb04c | `UNCONDITIONAL_JUMP`
<a id="insn-00acb044"></a> `00acb044` | `2d 19 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acb048"></a> `00acb048` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00acb04c"></a> `00acb04c` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00acb050"></a> `00acb050` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb054"></a> `00acb054` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acb058"></a> `00acb058` | `2f 38 f2 17` | b 0x00759114 | `CALL_TERMINATOR`
<a id="insn-00acb05c"></a> `00acb05c` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb060"></a> `00acb060` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00acb064"></a> `00acb064` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acaff8`](#insn-00acaff8) 範囲 `[['00acaff8', '00acb00b']]`
  - `CONDITIONAL_JUMP` [`00acb008`](#insn-00acb008) → [`00acb044`](#insn-00acb044)
  - `FALL_THROUGH` [`00acb008`](#insn-00acb008) → [`00acb00c`](#insn-00acb00c)
- ブロック [`00acb00c`](#insn-00acb00c) 範囲 `[['00acb00c', '00acb017']]`
  - `CONDITIONAL_JUMP` [`00acb014`](#insn-00acb014) → [`00acb020`](#insn-00acb020)
  - `FALL_THROUGH` [`00acb014`](#insn-00acb014) → [`00acb018`](#insn-00acb018)
- ブロック [`00acb018`](#insn-00acb018) 範囲 `[['00acb018', '00acb01f']]`
  - `CONDITIONAL_JUMP` [`00acb01c`](#insn-00acb01c) → [`00acb05c`](#insn-00acb05c)
  - `FALL_THROUGH` [`00acb01c`](#insn-00acb01c) → [`00acb020`](#insn-00acb020)
- ブロック [`00acb020`](#insn-00acb020) 範囲 `[['00acb020', '00acb043']]`
  - `UNCONDITIONAL_JUMP` [`00acb040`](#insn-00acb040) → [`00acb04c`](#insn-00acb04c)
- ブロック [`00acb044`](#insn-00acb044) 範囲 `[['00acb044', '00acb04b']]`
  - `FALL_THROUGH` [`00acb048`](#insn-00acb048) → [`00acb04c`](#insn-00acb04c)
- ブロック [`00acb04c`](#insn-00acb04c) 範囲 `[['00acb04c', '00acb05b']]`
- ブロック [`00acb05c`](#insn-00acb05c) 範囲 `[['00acb05c', '00acb067']]`

## 命令位置別の参照

- [`00acaff8`](#insn-00acaff8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaffc`](#insn-00acaffc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb008`](#insn-00acb008) → [`00acb044`](#insn-00acb044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb014`](#insn-00acb014) → [`00acb020`](#insn-00acb020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb01c`](#insn-00acb01c) → [`00acb05c`](#insn-00acb05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb020`](#insn-00acb020) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acb028`](#insn-00acb028) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acb038`](#insn-00acb038) → `00c9b508`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acb03c`](#insn-00acb03c) → `00ca4120`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb040`](#insn-00acb040) → [`00acb04c`](#insn-00acb04c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb044`](#insn-00acb044) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00acb050`](#insn-00acb050) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb054`](#insn-00acb054) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb058`](#insn-00acb058) → [`00759114`](../00759/00759114.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00759114` · 推定シンボル `None` · 推定型 `None`
- [`00acb05c`](#insn-00acb05c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb060`](#insn-00acb060) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acaff8`](#insn-00acaff8)

~~~json
{
  "source": "00acaff8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaffc`](#insn-00acaffc)

~~~json
{
  "source": "00acaffc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb008`](#insn-00acb008)

~~~json
{
  "source": "00acb008",
  "target": "00acb044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb014`](#insn-00acb014)

~~~json
{
  "source": "00acb014",
  "target": "00acb020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb01c`](#insn-00acb01c)

~~~json
{
  "source": "00acb01c",
  "target": "00acb05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb020`](#insn-00acb020)

~~~json
{
  "source": "00acb020",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb028`](#insn-00acb028)

~~~json
{
  "source": "00acb028",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb038`](#insn-00acb038)

~~~json
{
  "source": "00acb038",
  "target": "00c9b508",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b508",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acb03c`](#insn-00acb03c)

~~~json
{
  "source": "00acb03c",
  "target": "00ca4120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb040`](#insn-00acb040)

~~~json
{
  "source": "00acb040",
  "target": "00acb04c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb044`](#insn-00acb044)

~~~json
{
  "source": "00acb044",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb050`](#insn-00acb050)

~~~json
{
  "source": "00acb050",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb054`](#insn-00acb054)

~~~json
{
  "source": "00acb054",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb058`](#insn-00acb058)

~~~json
{
  "source": "00acb058",
  "target": "00759114",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb05c`](#insn-00acb05c)

~~~json
{
  "source": "00acb05c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb060`](#insn-00acb060)

~~~json
{
  "source": "00acb060",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
