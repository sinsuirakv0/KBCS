# 00bcffa4

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bd006c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd0/00bd006c.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-7cf167b0436f5f061b6880ced1b10892)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcffa4",
  "name": "FUN_00bcffa4",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d0826f46958eb0c24b9f1df83c4de29b9352f809a22a9e2fc2a17fd61440da5",
  "source_text_sha256": "9d0826f46958eb0c24b9f1df83c4de29b9352f809a22a9e2fc2a17fd61440da5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcffa4",
        "00bd00a7"
      ]
    ],
    "bytes_sha256": "176e7b9fb629108b136298c2bc8854e1cbd2df8b28018756063326d7eb0f1a69",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 4,
    "unresolved": 4
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

## 疑似コード / UTF-8 1430 bytes

~~~c

void FUN_00bcffa4(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  void *__ptr;
  long lVar2;
  size_t __size;
  long *plVar3;
  
  plVar3 = *(long **)(param_1 + 0x10);
  (**(code **)(*plVar3 + 0x20))(plVar3);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  }
  lVar2 = param_2[1];
  __ptr = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 2U) {
    __size = param_2[2] * 2;
    uVar1 = lVar2 + 0x3e2;
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
  *(undefined2 *)((long)__ptr + lVar2) = 0x3a3a;
  plVar3 = *(long **)(param_1 + 0x18);
                    /* catch() { ... } // from try @ 00bcff54 with catch @ 00bd0048 */
  lVar2 = *plVar3;
  param_2[1] = param_2[1] + 2;
                    /* catch() { ... } // from try @ 00bcff48 with catch @ 00bd0058 */
  (**(code **)(lVar2 + 0x20))(plVar3,param_2);
  if ((*(ushort *)((long)plVar3 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00bd00a0. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar3 + 0x28))(plVar3,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcffa4"></a> `00bcffa4` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcffa8"></a> `00bcffa8` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcffac"></a> `00bcffac` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcffb0"></a> `00bcffb0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcffb4"></a> `00bcffb4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcffb8"></a> `00bcffb8` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bcffbc"></a> `00bcffbc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcffc0"></a> `00bcffc0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcffc4"></a> `00bcffc4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcffc8"></a> `00bcffc8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcffcc"></a> `00bcffcc` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcffd0"></a> `00bcffd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcffd4"></a> `00bcffd4` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcffd8"></a> `00bcffd8` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcffdc"></a> `00bcffdc` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcffe0"></a> `00bcffe0` | `c0 00 00 54` | b.eq 0x00bcfff8 | `CONDITIONAL_JUMP`
<a id="insn-00bcffe4"></a> `00bcffe4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcffe8"></a> `00bcffe8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcffec"></a> `00bcffec` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcfff0"></a> `00bcfff0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcfff4"></a> `00bcfff4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfff8"></a> `00bcfff8` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfffc"></a> `00bcfffc` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd0000"></a> `00bd0000` | `0a 09 00 91` | add x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bd0004"></a> `00bd0004` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd0008"></a> `00bd0008` | `49 01 00 54` | b.ls 0x00bd0030 | `CONDITIONAL_JUMP`
<a id="insn-00bd000c"></a> `00bd000c` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd0010"></a> `00bd0010` | `08 89 0f 91` | add x8,x8,#0x3e2 | `FALL_THROUGH`
<a id="insn-00bd0014"></a> `00bd0014` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd0018"></a> `00bd0018` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bd001c"></a> `00bd001c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0020"></a> `00bd0020` | `4c 34 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bd0024"></a> `00bd0024` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bd0028"></a> `00bd0028` | `e0 03 00 b4` | cbz x0,0x00bd00a4 | `CONDITIONAL_JUMP`
<a id="insn-00bd002c"></a> `00bd002c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd0030"></a> `00bd0030` | `49 47 87 52` | mov w9,#0x3a3a | `FALL_THROUGH`
<a id="insn-00bd0034"></a> `00bd0034` | `09 68 28 78` | strh w9,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bd0038"></a> `00bd0038` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd003c"></a> `00bd003c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd0040"></a> `00bd0040` | `94 0e 40 f9` | ldr x20,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bd0044"></a> `00bd0044` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bd0048"></a> `00bd0048` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bd004c"></a> `00bd004c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd0050"></a> `00bd0050` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bd0054"></a> `00bd0054` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bd0058"></a> `00bd0058` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd005c"></a> `00bd005c` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bd0060"></a> `00bd0060` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bd0064"></a> `00bd0064` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bd0068"></a> `00bd0068` | `c1 00 00 54` | b.ne 0x00bd0080 | `CONDITIONAL_JUMP`
<a id="insn-00bd006c"></a> `00bd006c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd0070"></a> `00bd0070` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0074"></a> `00bd0074` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd0078"></a> `00bd0078` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd007c"></a> `00bd007c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd0080"></a> `00bd0080` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bd0084"></a> `00bd0084` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bd0088"></a> `00bd0088` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bd008c"></a> `00bd008c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bd0090"></a> `00bd0090` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd0094"></a> `00bd0094` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd0098"></a> `00bd0098` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bd009c"></a> `00bd009c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd00a0"></a> `00bd00a0` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bd00a4"></a> `00bd00a4` | `47 38 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcffa4`](#insn-00bcffa4) 範囲 `[['00bcffa4', '00bcffe3']]`
  - `CONDITIONAL_JUMP` [`00bcffe0`](#insn-00bcffe0) → [`00bcfff8`](#insn-00bcfff8)
  - `FALL_THROUGH` [`00bcffe0`](#insn-00bcffe0) → [`00bcffe4`](#insn-00bcffe4)
- ブロック [`00bcffe4`](#insn-00bcffe4) 範囲 `[['00bcffe4', '00bcfff7']]`
  - `FALL_THROUGH` [`00bcfff4`](#insn-00bcfff4) → [`00bcfff8`](#insn-00bcfff8)
- ブロック [`00bcfff8`](#insn-00bcfff8) 範囲 `[['00bcfff8', '00bd000b']]`
  - `CONDITIONAL_JUMP` [`00bd0008`](#insn-00bd0008) → [`00bd0030`](#insn-00bd0030)
  - `FALL_THROUGH` [`00bd0008`](#insn-00bd0008) → [`00bd000c`](#insn-00bd000c)
- ブロック [`00bd000c`](#insn-00bd000c) 範囲 `[['00bd000c', '00bd002b']]`
  - `CONDITIONAL_JUMP` [`00bd0028`](#insn-00bd0028) → [`00bd00a4`](#insn-00bd00a4)
  - `FALL_THROUGH` [`00bd0028`](#insn-00bd0028) → [`00bd002c`](#insn-00bd002c)
- ブロック [`00bd002c`](#insn-00bd002c) 範囲 `[['00bd002c', '00bd002f']]`
  - `FALL_THROUGH` [`00bd002c`](#insn-00bd002c) → [`00bd0030`](#insn-00bd0030)
- ブロック [`00bd0030`](#insn-00bd0030) 範囲 `[['00bd0030', '00bd0047']]`
  - `FALL_THROUGH` [`00bd0044`](#insn-00bd0044) → [`00bd0048`](#insn-00bd0048)
- ブロック [`00bd0048`](#insn-00bd0048) 範囲 `[['00bd0048', '00bd0057']]`
  - `FALL_THROUGH` [`00bd0054`](#insn-00bd0054) → [`00bd0058`](#insn-00bd0058)
- ブロック [`00bd0058`](#insn-00bd0058) 範囲 `[['00bd0058', '00bd006b']]`
  - `CONDITIONAL_JUMP` [`00bd0068`](#insn-00bd0068) → [`00bd0080`](#insn-00bd0080)
  - `FALL_THROUGH` [`00bd0068`](#insn-00bd0068) → [`00bd006c`](#insn-00bd006c)
- ブロック [`00bd006c`](#insn-00bd006c) 範囲 `[['00bd006c', '00bd007f']]`
- ブロック [`00bd0080`](#insn-00bd0080) 範囲 `[['00bd0080', '00bd00a3']]`
- ブロック [`00bd00a4`](#insn-00bd00a4) 範囲 `[['00bd00a4', '00bd00a7']]`

## 命令位置別の参照

- [`00bcffa8`](#insn-00bcffa8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffac`](#insn-00bcffac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffb0`](#insn-00bcffb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcffe0`](#insn-00bcffe0) → [`00bcfff8`](#insn-00bcfff8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0008`](#insn-00bd0008) → [`00bd0030`](#insn-00bd0030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0020`](#insn-00bd0020) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bd0028`](#insn-00bd0028) → [`00bd00a4`](#insn-00bd00a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0068`](#insn-00bd0068) → [`00bd0080`](#insn-00bd0080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd006c`](#insn-00bd006c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0070`](#insn-00bd0070) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0074`](#insn-00bd0074) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0090`](#insn-00bd0090) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0094`](#insn-00bd0094) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd0098`](#insn-00bd0098) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd00a4`](#insn-00bd00a4) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcffa8`](#insn-00bcffa8)

~~~json
{
  "source": "00bcffa8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffac`](#insn-00bcffac)

~~~json
{
  "source": "00bcffac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffb0`](#insn-00bcffb0)

~~~json
{
  "source": "00bcffb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcffe0`](#insn-00bcffe0)

~~~json
{
  "source": "00bcffe0",
  "target": "00bcfff8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0008`](#insn-00bd0008)

~~~json
{
  "source": "00bd0008",
  "target": "00bd0030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0020`](#insn-00bd0020)

~~~json
{
  "source": "00bd0020",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd0028`](#insn-00bd0028)

~~~json
{
  "source": "00bd0028",
  "target": "00bd00a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0068`](#insn-00bd0068)

~~~json
{
  "source": "00bd0068",
  "target": "00bd0080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd006c`](#insn-00bd006c)

~~~json
{
  "source": "00bd006c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0070`](#insn-00bd0070)

~~~json
{
  "source": "00bd0070",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0074`](#insn-00bd0074)

~~~json
{
  "source": "00bd0074",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0090`](#insn-00bd0090)

~~~json
{
  "source": "00bd0090",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0094`](#insn-00bd0094)

~~~json
{
  "source": "00bd0094",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd0098`](#insn-00bd0098)

~~~json
{
  "source": "00bd0098",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd00a4`](#insn-00bd00a4)

~~~json
{
  "source": "00bd00a4",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
