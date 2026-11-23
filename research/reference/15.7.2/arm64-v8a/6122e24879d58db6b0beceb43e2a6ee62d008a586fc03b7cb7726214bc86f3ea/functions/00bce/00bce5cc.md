# 00bce5cc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bce694`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bce/00bce694.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-ea6dbc05f3204744a1c9dc70bc76d61a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bce5cc",
  "name": "FUN_00bce5cc",
  "size": 216,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1d2ba983f3b38aabf5ca33bc6a15903bc59bdd2fe2a18c6585388ccf721f894a",
  "source_text_sha256": "1d2ba983f3b38aabf5ca33bc6a15903bc59bdd2fe2a18c6585388ccf721f894a",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bce5cc",
        "00bce6a3"
      ]
    ],
    "bytes_sha256": "04f4ff6db8ce41f2105aa612b14790e72b59960e37b0a205150f9fc1b3df11df",
    "instruction_count": 54,
    "instruction_bytes": 216,
    "body_bytes": 216,
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

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1235 bytes

~~~c

void FUN_00bce5cc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *__ptr;
  long lVar2;
  size_t __size;
  long *plVar3;
  
  lVar2 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 6U) {
    __size = param_2[2] * 2;
    uVar1 = lVar2 + 0x3e6;
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
    lVar2 = param_2[1];
  }
  *(undefined2 *)((undefined4 *)((long)__ptr + lVar2) + 1) = 0x2077;
  *(undefined4 *)((long)__ptr + lVar2) = 0x6f726874;
  plVar3 = *(long **)(param_1 + 0x10);
  lVar2 = *plVar3;
  param_2[1] = param_2[1] + 6;
  (**(code **)(lVar2 + 0x20))(plVar3,param_2);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) == 0x40) {
                    /* try { // try from 00bce678 to 00cce6e7 has its CatchHandler @ 00bcf304 */
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00bce69c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bce5cc"></a> `00bce5cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bce5d0"></a> `00bce5d0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bce5d4"></a> `00bce5d4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce5d8"></a> `00bce5d8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bce5dc"></a> `00bce5dc` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bce5e0"></a> `00bce5e0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bce5e4"></a> `00bce5e4` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bce5e8"></a> `00bce5e8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bce5ec"></a> `00bce5ec` | `2b 19 00 91` | add x11,x9,#0x6 | `FALL_THROUGH`
<a id="insn-00bce5f0"></a> `00bce5f0` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bce5f4"></a> `00bce5f4` | `89 01 00 54` | b.ls 0x00bce624 | `CONDITIONAL_JUMP`
<a id="insn-00bce5f8"></a> `00bce5f8` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bce5fc"></a> `00bce5fc` | `29 99 0f 91` | add x9,x9,#0x3e6 | `FALL_THROUGH`
<a id="insn-00bce600"></a> `00bce600` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bce604"></a> `00bce604` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bce608"></a> `00bce608` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bce60c"></a> `00bce60c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bce610"></a> `00bce610` | `d0 3a 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bce614"></a> `00bce614` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bce618"></a> `00bce618` | `40 04 00 b4` | cbz x0,0x00bce6a0 | `CONDITIONAL_JUMP`
<a id="insn-00bce61c"></a> `00bce61c` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce620"></a> `00bce620` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bce624"></a> `00bce624` | `8a 0e 8d 52` | mov w10,#0x6874 | `FALL_THROUGH`
<a id="insn-00bce628"></a> `00bce628` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bce62c"></a> `00bce62c` | `e9 0e 84 52` | mov w9,#0x2077 | `FALL_THROUGH`
<a id="insn-00bce630"></a> `00bce630` | `4a ee ad 72` | movk w10,#0x6f72, LSL #16 | `FALL_THROUGH`
<a id="insn-00bce634"></a> `00bce634` | `09 09 00 79` | strh w9,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bce638"></a> `00bce638` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bce63c"></a> `00bce63c` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00bce640"></a> `00bce640` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce644"></a> `00bce644` | `94 0a 40 f9` | ldr x20,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bce648"></a> `00bce648` | `08 19 00 91` | add x8,x8,#0x6 | `FALL_THROUGH`
<a id="insn-00bce64c"></a> `00bce64c` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bce650"></a> `00bce650` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce654"></a> `00bce654` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bce658"></a> `00bce658` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bce65c"></a> `00bce65c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce660"></a> `00bce660` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bce664"></a> `00bce664` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bce668"></a> `00bce668` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bce66c"></a> `00bce66c` | `a1 00 00 54` | b.ne 0x00bce680 | `CONDITIONAL_JUMP`
<a id="insn-00bce670"></a> `00bce670` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce674"></a> `00bce674` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bce678"></a> `00bce678` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bce67c"></a> `00bce67c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bce680"></a> `00bce680` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bce684"></a> `00bce684` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce688"></a> `00bce688` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bce68c"></a> `00bce68c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bce690"></a> `00bce690` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce694"></a> `00bce694` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bce698"></a> `00bce698` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bce69c"></a> `00bce69c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bce6a0"></a> `00bce6a0` | `c8 3e 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bce5cc`](#insn-00bce5cc) 範囲 `[['00bce5cc', '00bce5f7']]`
  - `CONDITIONAL_JUMP` [`00bce5f4`](#insn-00bce5f4) → [`00bce624`](#insn-00bce624)
  - `FALL_THROUGH` [`00bce5f4`](#insn-00bce5f4) → [`00bce5f8`](#insn-00bce5f8)
- ブロック [`00bce5f8`](#insn-00bce5f8) 範囲 `[['00bce5f8', '00bce61b']]`
  - `CONDITIONAL_JUMP` [`00bce618`](#insn-00bce618) → [`00bce6a0`](#insn-00bce6a0)
  - `FALL_THROUGH` [`00bce618`](#insn-00bce618) → [`00bce61c`](#insn-00bce61c)
- ブロック [`00bce61c`](#insn-00bce61c) 範囲 `[['00bce61c', '00bce623']]`
  - `FALL_THROUGH` [`00bce620`](#insn-00bce620) → [`00bce624`](#insn-00bce624)
- ブロック [`00bce624`](#insn-00bce624) 範囲 `[['00bce624', '00bce66f']]`
  - `CONDITIONAL_JUMP` [`00bce66c`](#insn-00bce66c) → [`00bce680`](#insn-00bce680)
  - `FALL_THROUGH` [`00bce66c`](#insn-00bce66c) → [`00bce670`](#insn-00bce670)
- ブロック [`00bce670`](#insn-00bce670) 範囲 `[['00bce670', '00bce677']]`
  - `FALL_THROUGH` [`00bce674`](#insn-00bce674) → [`00bce678`](#insn-00bce678)
- ブロック [`00bce678`](#insn-00bce678) 範囲 `[['00bce678', '00bce67f']]`
- ブロック [`00bce680`](#insn-00bce680) 範囲 `[['00bce680', '00bce69f']]`
- ブロック [`00bce6a0`](#insn-00bce6a0) 範囲 `[['00bce6a0', '00bce6a3']]`

## 命令位置別の参照

- [`00bce5d0`](#insn-00bce5d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce5d4`](#insn-00bce5d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce5f4`](#insn-00bce5f4) → [`00bce624`](#insn-00bce624) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce610`](#insn-00bce610) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bce618`](#insn-00bce618) → [`00bce6a0`](#insn-00bce6a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce66c`](#insn-00bce66c) → [`00bce680`](#insn-00bce680) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce670`](#insn-00bce670) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce674`](#insn-00bce674) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce690`](#insn-00bce690) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce694`](#insn-00bce694) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce6a0`](#insn-00bce6a0) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bce5d0`](#insn-00bce5d0)

~~~json
{
  "source": "00bce5d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce5d4`](#insn-00bce5d4)

~~~json
{
  "source": "00bce5d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce5f4`](#insn-00bce5f4)

~~~json
{
  "source": "00bce5f4",
  "target": "00bce624",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce610`](#insn-00bce610)

~~~json
{
  "source": "00bce610",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce618`](#insn-00bce618)

~~~json
{
  "source": "00bce618",
  "target": "00bce6a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce66c`](#insn-00bce66c)

~~~json
{
  "source": "00bce66c",
  "target": "00bce680",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce670`](#insn-00bce670)

~~~json
{
  "source": "00bce670",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce674`](#insn-00bce674)

~~~json
{
  "source": "00bce674",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce690`](#insn-00bce690)

~~~json
{
  "source": "00bce690",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce694`](#insn-00bce694)

~~~json
{
  "source": "00bce694",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce6a0`](#insn-00bce6a0)

~~~json
{
  "source": "00bce6a0",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
