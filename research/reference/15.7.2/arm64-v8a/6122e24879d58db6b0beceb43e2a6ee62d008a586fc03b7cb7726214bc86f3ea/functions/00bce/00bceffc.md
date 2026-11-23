# 00bceffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcf0c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf0c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-5e29ee8b497615417d3c9ae027e6db34)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bceffc",
  "name": "FUN_00bceffc",
  "size": 220,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab343c6ed7d1721edbbe0729ced4c7d2c4fce65d123f09c4bd8dbe0f43ccd399",
  "source_text_sha256": "ab343c6ed7d1721edbbe0729ced4c7d2c4fce65d123f09c4bd8dbe0f43ccd399",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bceffc",
        "00bcf0d7"
      ]
    ],
    "bytes_sha256": "7ab663597b15d766c428ffb78ee2db65dfa5cc525acd60f6aed59ee5180ff058",
    "instruction_count": 55,
    "instruction_bytes": 220,
    "body_bytes": 220,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 関連文字列（未確認候補）

~~~text
"operator "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1165 bytes

~~~c

void FUN_00bceffc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined8 uVar2;
  void *__ptr;
  long lVar3;
  size_t __size;
  long *plVar4;
  
  lVar3 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar3 + 9U) {
    __size = param_2[2] * 2;
    uVar1 = lVar3 + 0x3e9;
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
    __ptr = realloc(__ptr,__size);
    *param_2 = __ptr;
    if (__ptr == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar3 = param_2[1];
  }
  uVar2 = s_operator_002ac5e6._0_8_;
  ((char *)((long)__ptr + lVar3))[8] = ' ';
  *(undefined8 *)((long)__ptr + lVar3) = uVar2;
  plVar4 = *(long **)(param_1 + 0x10);
  lVar3 = *plVar4;
  param_2[1] = param_2[1] + 9;
  (**(code **)(lVar3 + 0x20))(plVar4,param_2);
  if ((*(ushort *)((long)plVar4 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00bcf0d0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar4 + 0x28))(plVar4,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bceffc"></a> `00bceffc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcf000"></a> `00bcf000` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcf004"></a> `00bcf004` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf008"></a> `00bcf008` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcf00c"></a> `00bcf00c` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf010"></a> `00bcf010` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcf014"></a> `00bcf014` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcf018"></a> `00bcf018` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcf01c"></a> `00bcf01c` | `2b 25 00 91` | add x11,x9,#0x9 | `FALL_THROUGH`
<a id="insn-00bcf020"></a> `00bcf020` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcf024"></a> `00bcf024` | `89 01 00 54` | b.ls 0x00bcf054 | `CONDITIONAL_JUMP`
<a id="insn-00bcf028"></a> `00bcf028` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcf02c"></a> `00bcf02c` | `29 a5 0f 91` | add x9,x9,#0x3e9 | `FALL_THROUGH`
<a id="insn-00bcf030"></a> `00bcf030` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcf034"></a> `00bcf034` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcf038"></a> `00bcf038` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bcf03c"></a> `00bcf03c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf040"></a> `00bcf040` | `44 38 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf044"></a> `00bcf044` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcf048"></a> `00bcf048` | `60 04 00 b4` | cbz x0,0x00bcf0d4 | `CONDITIONAL_JUMP`
<a id="insn-00bcf04c"></a> `00bcf04c` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf050"></a> `00bcf050` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcf054"></a> `00bcf054` | `ea b6 ff b0` | adrp x10,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bcf058"></a> `00bcf058` | `4a 99 17 91` | add x10,x10,#0x5e6 | `FALL_THROUGH`
<a id="insn-00bcf05c"></a> `00bcf05c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bcf060"></a> `00bcf060` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-00bcf064"></a> `00bcf064` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bcf068"></a> `00bcf068` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcf06c"></a> `00bcf06c` | `09 21 00 39` | strb w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf070"></a> `00bcf070` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00bcf074"></a> `00bcf074` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf078"></a> `00bcf078` | `94 0a 40 f9` | ldr x20,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf07c"></a> `00bcf07c` | `08 25 00 91` | add x8,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bcf080"></a> `00bcf080` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bcf084"></a> `00bcf084` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcf088"></a> `00bcf088` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf08c"></a> `00bcf08c` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf090"></a> `00bcf090` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcf094"></a> `00bcf094` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bcf098"></a> `00bcf098` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcf09c"></a> `00bcf09c` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcf0a0"></a> `00bcf0a0` | `a1 00 00 54` | b.ne 0x00bcf0b4 | `CONDITIONAL_JUMP`
<a id="insn-00bcf0a4"></a> `00bcf0a4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf0a8"></a> `00bcf0a8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcf0ac"></a> `00bcf0ac` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcf0b0"></a> `00bcf0b0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcf0b4"></a> `00bcf0b4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcf0b8"></a> `00bcf0b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcf0bc"></a> `00bcf0bc` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcf0c0"></a> `00bcf0c0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcf0c4"></a> `00bcf0c4` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf0c8"></a> `00bcf0c8` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcf0cc"></a> `00bcf0cc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcf0d0"></a> `00bcf0d0` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bcf0d4"></a> `00bcf0d4` | `3b 3c 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bceffc`](#insn-00bceffc) 範囲 `[['00bceffc', '00bcf027']]`
  - `CONDITIONAL_JUMP` [`00bcf024`](#insn-00bcf024) → [`00bcf054`](#insn-00bcf054)
  - `FALL_THROUGH` [`00bcf024`](#insn-00bcf024) → [`00bcf028`](#insn-00bcf028)
- ブロック [`00bcf028`](#insn-00bcf028) 範囲 `[['00bcf028', '00bcf04b']]`
  - `CONDITIONAL_JUMP` [`00bcf048`](#insn-00bcf048) → [`00bcf0d4`](#insn-00bcf0d4)
  - `FALL_THROUGH` [`00bcf048`](#insn-00bcf048) → [`00bcf04c`](#insn-00bcf04c)
- ブロック [`00bcf04c`](#insn-00bcf04c) 範囲 `[['00bcf04c', '00bcf053']]`
  - `FALL_THROUGH` [`00bcf050`](#insn-00bcf050) → [`00bcf054`](#insn-00bcf054)
- ブロック [`00bcf054`](#insn-00bcf054) 範囲 `[['00bcf054', '00bcf0a3']]`
  - `CONDITIONAL_JUMP` [`00bcf0a0`](#insn-00bcf0a0) → [`00bcf0b4`](#insn-00bcf0b4)
  - `FALL_THROUGH` [`00bcf0a0`](#insn-00bcf0a0) → [`00bcf0a4`](#insn-00bcf0a4)
- ブロック [`00bcf0a4`](#insn-00bcf0a4) 範囲 `[['00bcf0a4', '00bcf0b3']]`
- ブロック [`00bcf0b4`](#insn-00bcf0b4) 範囲 `[['00bcf0b4', '00bcf0d3']]`
- ブロック [`00bcf0d4`](#insn-00bcf0d4) 範囲 `[['00bcf0d4', '00bcf0d7']]`

## 命令位置別の参照

- [`00bcf000`](#insn-00bcf000) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf004`](#insn-00bcf004) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf024`](#insn-00bcf024) → [`00bcf054`](#insn-00bcf054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf040`](#insn-00bcf040) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcf048`](#insn-00bcf048) → [`00bcf0d4`](#insn-00bcf0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf060`](#insn-00bcf060) → `002ac5e6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf0a0`](#insn-00bcf0a0) → [`00bcf0b4`](#insn-00bcf0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0a4`](#insn-00bcf0a4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0a8`](#insn-00bcf0a8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0c4`](#insn-00bcf0c4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0c8`](#insn-00bcf0c8) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf0d4`](#insn-00bcf0d4) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcf000`](#insn-00bcf000)

~~~json
{
  "source": "00bcf000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf004`](#insn-00bcf004)

~~~json
{
  "source": "00bcf004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf024`](#insn-00bcf024)

~~~json
{
  "source": "00bcf024",
  "target": "00bcf054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf040`](#insn-00bcf040)

~~~json
{
  "source": "00bcf040",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf048`](#insn-00bcf048)

~~~json
{
  "source": "00bcf048",
  "target": "00bcf0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf060`](#insn-00bcf060)

~~~json
{
  "source": "00bcf060",
  "target": "002ac5e6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac5e6",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "6f70657261746f722000",
  "capture_start": "002ac5e6",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf0a0`](#insn-00bcf0a0)

~~~json
{
  "source": "00bcf0a0",
  "target": "00bcf0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf0a4`](#insn-00bcf0a4)

~~~json
{
  "source": "00bcf0a4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf0a8`](#insn-00bcf0a8)

~~~json
{
  "source": "00bcf0a8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf0c4`](#insn-00bcf0c4)

~~~json
{
  "source": "00bcf0c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf0c8`](#insn-00bcf0c8)

~~~json
{
  "source": "00bcf0c8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf0d4`](#insn-00bcf0d4)

~~~json
{
  "source": "00bcf0d4",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
