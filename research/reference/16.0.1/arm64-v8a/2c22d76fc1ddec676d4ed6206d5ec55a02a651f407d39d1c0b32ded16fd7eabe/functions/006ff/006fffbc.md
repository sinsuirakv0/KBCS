# 006fffbc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `006fff7c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/006ff/006fff7c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0033.md#compare-cf097cb2521d21d804da4000b9e231a3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00700014`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00700/00700014.md) · 移動量 `+0x58`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0033.md#compare-b04cd619e27dc70563238bbc0e8c4822)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006fffbc",
  "name": "FUN_006fffbc",
  "size": 140,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4b156299903a147c7d08c540d18f5ba2091417b353009a2789221d7379466961",
  "source_text_sha256": "4b156299903a147c7d08c540d18f5ba2091417b353009a2789221d7379466961",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006fffbc",
        "00700047"
      ]
    ],
    "bytes_sha256": "66ddb65add56ddd72c2c5cbb08ba3cf5f10b0aa5dd267df86249c745b0aa44c3",
    "instruction_count": 35,
    "instruction_bytes": 140,
    "body_bytes": 140,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00470840](../00470/00470840.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c58000](../00c58/00c58000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 759 bytes

~~~c

undefined8 * FUN_006fffbc(long param_1)

{
  undefined8 uVar1;
  void *__src;
  size_t __n;
  undefined8 *puVar2;
  void *__dest;
  long lVar3;
  
  puVar2 = (undefined8 *)_Znwm(0x28);
  uVar1 = *(undefined8 *)(param_1 + 8);
  __src = *(void **)(param_1 + 0x10);
  puVar2[3] = 0;
  puVar2[4] = 0;
  *puVar2 = &PTR_FUN_00c77598;
  puVar2[1] = uVar1;
  lVar3 = *(long *)(param_1 + 0x18);
  puVar2[2] = 0;
  __n = lVar3 - (long)__src;
  if (__n != 0) {
    if ((long)__n < 0) {
                    /* WARNING: Subroutine does not return */
      FUN_00470840(puVar2 + 2);
    }
    __dest = (void *)_Znwm(__n);
    puVar2[2] = __dest;
    puVar2[4] = (long)__dest + __n;
    memcpy(__dest,__src,__n);
    puVar2[3] = (long)__dest + __n;
  }
  return puVar2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006fffbc"></a> `006fffbc` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-006fffc0"></a> `006fffc0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006fffc4"></a> `006fffc4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006fffc8"></a> `006fffc8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006fffcc"></a> `006fffcc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-006fffd0"></a> `006fffd0` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-006fffd4"></a> `006fffd4` | `af 5f 15 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-006fffd8"></a> `006fffd8` | `89 d6 40 a9` | ldp x9,x21,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-006fffdc"></a> `006fffdc` | `c8 2b 00 90` | adrp x8,0xc77000 | `FALL_THROUGH`
<a id="insn-006fffe0"></a> `006fffe0` | `08 61 16 91` | add x8,x8,#0x598 | `FALL_THROUGH`
<a id="insn-006fffe4"></a> `006fffe4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-006fffe8"></a> `006fffe8` | `1f fc 01 a9` | stp xzr,xzr,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-006fffec"></a> `006fffec` | `08 24 00 a9` | stp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-006ffff0"></a> `006ffff0` | `88 0e 40 f9` | ldr x8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-006ffff4"></a> `006ffff4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-006ffff8"></a> `006ffff8` | `9f 0e 01 f8` | str xzr,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-006ffffc"></a> `006ffffc` | `16 01 15 eb` | subs x22,x8,x21 | `FALL_THROUGH`
<a id="insn-00700000"></a> `00700000` | `60 01 00 54` | b.eq 0x0070002c | `CONDITIONAL_JUMP`
<a id="insn-00700004"></a> `00700004` | `f6 01 f8 b7` | tbnz x22,#0x3f,0x00700040 | `CONDITIONAL_JUMP`
<a id="insn-00700008"></a> `00700008` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-0070000c"></a> `0070000c` | `a1 5f 15 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00700010"></a> `00700010` | `14 00 16 8b` | add x20,x0,x22 | `FALL_THROUGH`
<a id="insn-00700014"></a> `00700014` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00700018"></a> `00700018` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-0070001c"></a> `0070001c` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00700020"></a> `00700020` | `74 12 00 f9` | str x20,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00700024"></a> `00700024` | `f7 5f 15 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00700028"></a> `00700028` | `74 0e 00 f9` | str x20,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-0070002c"></a> `0070002c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00700030"></a> `00700030` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00700034"></a> `00700034` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00700038"></a> `00700038` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-0070003c"></a> `0070003c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00700040"></a> `00700040` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00700044"></a> `00700044` | `ff c1 f5 97` | bl 0x00470840 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`006fffbc`](#insn-006fffbc) 範囲 `[['006fffbc', '00700003']]`
  - `CONDITIONAL_JUMP` [`00700000`](#insn-00700000) → [`0070002c`](#insn-0070002c)
  - `FALL_THROUGH` [`00700000`](#insn-00700000) → [`00700004`](#insn-00700004)
- ブロック [`00700004`](#insn-00700004) 範囲 `[['00700004', '00700007']]`
  - `CONDITIONAL_JUMP` [`00700004`](#insn-00700004) → [`00700040`](#insn-00700040)
  - `FALL_THROUGH` [`00700004`](#insn-00700004) → [`00700008`](#insn-00700008)
- ブロック [`00700008`](#insn-00700008) 範囲 `[['00700008', '0070002b']]`
  - `FALL_THROUGH` [`00700028`](#insn-00700028) → [`0070002c`](#insn-0070002c)
- ブロック [`0070002c`](#insn-0070002c) 範囲 `[['0070002c', '0070003f']]`
- ブロック [`00700040`](#insn-00700040) 範囲 `[['00700040', '00700047']]`

## 命令位置別の参照

- [`006fffbc`](#insn-006fffbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fffc0`](#insn-006fffc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fffc4`](#insn-006fffc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006fffd4`](#insn-006fffd4) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`006fffec`](#insn-006fffec) → `00c77598`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00700000`](#insn-00700000) → [`0070002c`](#insn-0070002c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00700004`](#insn-00700004) → [`00700040`](#insn-00700040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`0070000c`](#insn-0070000c) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00700024`](#insn-00700024) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00700030`](#insn-00700030) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00700034`](#insn-00700034) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00700038`](#insn-00700038) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00700044`](#insn-00700044) → [`00470840`](../00470/00470840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470840` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006fffbc`](#insn-006fffbc)

~~~json
{
  "source": "006fffbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fffc0`](#insn-006fffc0)

~~~json
{
  "source": "006fffc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fffc4`](#insn-006fffc4)

~~~json
{
  "source": "006fffc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006fffd4`](#insn-006fffd4)

~~~json
{
  "source": "006fffd4",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006fffec`](#insn-006fffec)

~~~json
{
  "source": "006fffec",
  "target": "00c77598",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c77598",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00700000`](#insn-00700000)

~~~json
{
  "source": "00700000",
  "target": "0070002c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00700004`](#insn-00700004)

~~~json
{
  "source": "00700004",
  "target": "00700040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`0070000c`](#insn-0070000c)

~~~json
{
  "source": "0070000c",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00700024`](#insn-00700024)

~~~json
{
  "source": "00700024",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00700030`](#insn-00700030)

~~~json
{
  "source": "00700030",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00700034`](#insn-00700034)

~~~json
{
  "source": "00700034",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00700038`](#insn-00700038)

~~~json
{
  "source": "00700038",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00700044`](#insn-00700044)

~~~json
{
  "source": "00700044",
  "target": "00470840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
