# 00ae3fcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ae4094`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ae4/00ae4094.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-adab28b6a6854c980686bec203c42498)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ae3fcc",
  "name": "_ZN8firebase8LogDebugEPKcz",
  "size": 164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b193ea10af8a68dbc6dd8abe2e4151710e390d3aa175357c441a0f4d0805455b",
  "source_text_sha256": "b193ea10af8a68dbc6dd8abe2e4151710e390d3aa175357c441a0f4d0805455b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ae3fcc",
        "00ae406f"
      ]
    ],
    "bytes_sha256": "309aad4706576d1beaf17d2f5ac135e5d782d518b7b5aaa604a195d991515715",
    "instruction_count": 41,
    "instruction_bytes": 164,
    "body_bytes": 164,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bde1b0](../00bde/00bde1b0.md)

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)
- [00bde1a0](../00bde/00bde1a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1228 bytes

~~~c

void _ZN8firebase8LogDebugEPKcz
               (undefined8 param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  long lVar1;
  long lVar2;
  undefined1 auStack_b0 [8];
  undefined8 local_a8;
  undefined8 uStack_a0;
  undefined8 local_98;
  undefined8 uStack_90;
  undefined8 local_88;
  undefined8 uStack_80;
  undefined8 local_78;
  undefined1 *local_70;
  undefined1 **ppuStack_68;
  undefined1 *puStack_60;
  undefined8 uStack_58;
  
  lVar1 = tpidr_el0;
  lVar2 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00ae4010 to 00be4097 has its CatchHandler @ 00ae417c */
  ppuStack_68 = &local_70;
  puStack_60 = auStack_b0;
  uStack_58 = 0xffffff80ffffffc8;
  local_a8 = param_2;
  uStack_a0 = param_3;
  local_98 = param_4;
  uStack_90 = param_5;
  local_88 = param_6;
  uStack_80 = param_7;
  local_78 = param_8;
  local_70 = (undefined1 *)register0x00000008;
  _ZN8firebase23LogMessageWithCallbackVENS_8LogLevelEPKcSt9__va_list(1,param_1,&local_70);
  if (*(long *)(lVar1 + 0x28) == lVar2) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ae3fcc"></a> `00ae3fcc` | `ff c3 04 d1` | sub sp,sp,#0x130 | `FALL_THROUGH`
<a id="insn-00ae3fd0"></a> `00ae3fd0` | `fc 4f 11 a9` | stp x28,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00ae3fd4"></a> `00ae3fd4` | `fd 7b 12 a9` | stp x29,x30,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00ae3fd8"></a> `00ae3fd8` | `fd 83 04 91` | add x29,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00ae3fdc"></a> `00ae3fdc` | `e1 8b 08 a9` | stp x1,x2,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00ae3fe0"></a> `00ae3fe0` | `e3 93 09 a9` | stp x3,x4,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00ae3fe4"></a> `00ae3fe4` | `e5 9b 0a a9` | stp x5,x6,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00ae3fe8"></a> `00ae3fe8` | `e7 5f 00 f9` | str x7,[sp, #0xb8] | `FALL_THROUGH`
<a id="insn-00ae3fec"></a> `00ae3fec` | `e0 07 00 ad` | stp q0,q1,[sp] | `FALL_THROUGH`
<a id="insn-00ae3ff0"></a> `00ae3ff0` | `e2 0f 01 ad` | stp q2,q3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ae3ff4"></a> `00ae3ff4` | `e4 17 02 ad` | stp q4,q5,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ae3ff8"></a> `00ae3ff8` | `e6 1f 03 ad` | stp q6,q7,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ae3ffc"></a> `00ae3ffc` | `53 d0 3b d5` | mrs x19,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ae4000"></a> `00ae4000` | `6d 16 40 f9` | ldr x13,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00ae4004"></a> `00ae4004` | `ea 23 02 91` | add x10,sp,#0x88 | `FALL_THROUGH`
<a id="insn-00ae4008"></a> `00ae4008` | `ec 06 80 92` | mov x12,#-0x38 | `FALL_THROUGH`
<a id="insn-00ae400c"></a> `00ae400c` | `ee 03 00 91` | mov x14,sp | `FALL_THROUGH`
<a id="insn-00ae4010"></a> `00ae4010` | `ab 43 00 91` | add x11,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00ae4014"></a> `00ae4014` | `0c f0 df f2` | movk x12,#0xff80, LSL #32 | `FALL_THROUGH`
<a id="insn-00ae4018"></a> `00ae4018` | `4a e1 00 91` | add x10,x10,#0x38 | `FALL_THROUGH`
<a id="insn-00ae401c"></a> `00ae401c` | `ce 01 02 91` | add x14,x14,#0x80 | `FALL_THROUGH`
<a id="insn-00ae4020"></a> `00ae4020` | `a9 e3 00 d1` | sub x9,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00ae4024"></a> `00ae4024` | `ad 83 1e f8` | stur x13,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00ae4028"></a> `00ae4028` | `ab ab 3c a9` | stp x11,x10,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00ae402c"></a> `00ae402c` | `ae b3 3d a9` | stp x14,x12,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00ae4030"></a> `00ae4030` | `21 01 40 ad` | ldp q1,q0,[x9] | `FALL_THROUGH`
<a id="insn-00ae4034"></a> `00ae4034` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00ae4038"></a> `00ae4038` | `a2 83 01 d1` | sub x2,x29,#0x60 | `FALL_THROUGH`
<a id="insn-00ae403c"></a> `00ae403c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ae4040"></a> `00ae4040` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00ae4044"></a> `00ae4044` | `a1 03 3d ad` | stp q1,q0,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00ae4048"></a> `00ae4048` | `56 e8 03 94` | bl 0x00bde1a0 | `UNCONDITIONAL_CALL`
<a id="insn-00ae404c"></a> `00ae404c` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00ae4050"></a> `00ae4050` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00ae4054"></a> `00ae4054` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ae4058"></a> `00ae4058` | `a1 00 00 54` | b.ne 0x00ae406c | `CONDITIONAL_JUMP`
<a id="insn-00ae405c"></a> `00ae405c` | `fd 7b 52 a9` | ldp x29,x30,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00ae4060"></a> `00ae4060` | `fc 4f 51 a9` | ldp x28,x19,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00ae4064"></a> `00ae4064` | `ff c3 04 91` | add sp,sp,#0x130 | `FALL_THROUGH`
<a id="insn-00ae4068"></a> `00ae4068` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ae406c"></a> `00ae406c` | `c9 db 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ae3fcc`](#insn-00ae3fcc) 範囲 `[['00ae3fcc', '00ae400f']]`
  - `FALL_THROUGH` [`00ae400c`](#insn-00ae400c) → [`00ae4010`](#insn-00ae4010)
- ブロック [`00ae4010`](#insn-00ae4010) 範囲 `[['00ae4010', '00ae405b']]`
  - `CONDITIONAL_JUMP` [`00ae4058`](#insn-00ae4058) → [`00ae406c`](#insn-00ae406c)
  - `FALL_THROUGH` [`00ae4058`](#insn-00ae4058) → [`00ae405c`](#insn-00ae405c)
- ブロック [`00ae405c`](#insn-00ae405c) 範囲 `[['00ae405c', '00ae406b']]`
- ブロック [`00ae406c`](#insn-00ae406c) 範囲 `[['00ae406c', '00ae406f']]`

## 命令位置別の参照

- [`00ae3fd0`](#insn-00ae3fd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3fd4`](#insn-00ae3fd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3fdc`](#insn-00ae3fdc) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3fe0`](#insn-00ae3fe0) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3fe4`](#insn-00ae3fe4) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3fe8`](#insn-00ae3fe8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3fec`](#insn-00ae3fec) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3ff0`](#insn-00ae3ff0) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3ff4`](#insn-00ae3ff4) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae3ff8`](#insn-00ae3ff8) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4024`](#insn-00ae4024) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4028`](#insn-00ae4028) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae402c`](#insn-00ae402c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4030`](#insn-00ae4030) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4044`](#insn-00ae4044) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4048`](#insn-00ae4048) → [`00bde1a0`](../00bde/00bde1a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1a0` · 推定シンボル `None` · 推定型 `None`
- [`00ae4050`](#insn-00ae4050) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4058`](#insn-00ae4058) → [`00ae406c`](#insn-00ae406c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae405c`](#insn-00ae405c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae4060`](#insn-00ae4060) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ae406c`](#insn-00ae406c) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ae3fd0`](#insn-00ae3fd0)

~~~json
{
  "source": "00ae3fd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3fd4`](#insn-00ae3fd4)

~~~json
{
  "source": "00ae3fd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3fdc`](#insn-00ae3fdc)

~~~json
{
  "source": "00ae3fdc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3fe0`](#insn-00ae3fe0)

~~~json
{
  "source": "00ae3fe0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3fe4`](#insn-00ae3fe4)

~~~json
{
  "source": "00ae3fe4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3fe8`](#insn-00ae3fe8)

~~~json
{
  "source": "00ae3fe8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3fec`](#insn-00ae3fec)

~~~json
{
  "source": "00ae3fec",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3ff0`](#insn-00ae3ff0)

~~~json
{
  "source": "00ae3ff0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3ff4`](#insn-00ae3ff4)

~~~json
{
  "source": "00ae3ff4",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae3ff8`](#insn-00ae3ff8)

~~~json
{
  "source": "00ae3ff8",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4024`](#insn-00ae4024)

~~~json
{
  "source": "00ae4024",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4028`](#insn-00ae4028)

~~~json
{
  "source": "00ae4028",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae402c`](#insn-00ae402c)

~~~json
{
  "source": "00ae402c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4030`](#insn-00ae4030)

~~~json
{
  "source": "00ae4030",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4044`](#insn-00ae4044)

~~~json
{
  "source": "00ae4044",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4048`](#insn-00ae4048)

~~~json
{
  "source": "00ae4048",
  "target": "00bde1a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ae4050`](#insn-00ae4050)

~~~json
{
  "source": "00ae4050",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4058`](#insn-00ae4058)

~~~json
{
  "source": "00ae4058",
  "target": "00ae406c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae405c`](#insn-00ae405c)

~~~json
{
  "source": "00ae405c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae4060`](#insn-00ae4060)

~~~json
{
  "source": "00ae4060",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ae406c`](#insn-00ae406c)

~~~json
{
  "source": "00ae406c",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
