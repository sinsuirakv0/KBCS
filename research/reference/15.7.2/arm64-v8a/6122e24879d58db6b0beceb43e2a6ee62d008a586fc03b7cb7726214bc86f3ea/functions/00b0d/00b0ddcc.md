# 00b0ddcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b0de94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b0d/00b0de94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0002.md#compare-37f725e33b34c8b8babab22021e9aa1e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b0ddcc",
  "name": "_ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz",
  "size": 156,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "45cf3cc3e5ab03409c63e8d622c821824c7b1c820a81facbbde049d63b0af31f",
  "source_text_sha256": "45cf3cc3e5ab03409c63e8d622c821824c7b1c820a81facbbde049d63b0af31f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b0ddcc",
        "00b0de67"
      ]
    ],
    "bytes_sha256": "ca91a9c77813615ba1e3593051dc74270121e6ffd4a69778a8b75aa562a06575",
    "instruction_count": 39,
    "instruction_bytes": 156,
    "body_bytes": 156,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bdef90](../00bde/00bdef90.md)

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1111 bytes

~~~c

void _ZN7_JNIEnv23CallStaticBooleanMethodEP7_jclassP10_jmethodIDz
               (long *param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  long lVar1;
  long lVar2;
  undefined1 auStack_a0 [8];
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
  puStack_60 = auStack_a0;
  ppuStack_68 = &local_70;
  uStack_58 = 0xffffff80ffffffd8;
  local_98 = param_4;
  uStack_90 = param_5;
  local_88 = param_6;
  uStack_80 = param_7;
  local_78 = param_8;
  local_70 = (undefined1 *)register0x00000008;
  (**(code **)(*param_1 + 0x3b0))();
  if (*(long *)(lVar1 + 0x28) == lVar2) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00b0de64 to 00c0de6b has its CatchHandler @ 00b0dfec */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b0ddcc"></a> `00b0ddcc` | `ff 83 04 d1` | sub sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00b0ddd0"></a> `00b0ddd0` | `fc 4f 10 a9` | stp x28,x19,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b0ddd4"></a> `00b0ddd4` | `fd 7b 11 a9` | stp x29,x30,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b0ddd8"></a> `00b0ddd8` | `fd 43 04 91` | add x29,sp,#0x110 | `FALL_THROUGH`
<a id="insn-00b0dddc"></a> `00b0dddc` | `e3 93 08 a9` | stp x3,x4,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00b0dde0"></a> `00b0dde0` | `e5 9b 09 a9` | stp x5,x6,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-00b0dde4"></a> `00b0dde4` | `e7 57 00 f9` | str x7,[sp, #0xa8] | `FALL_THROUGH`
<a id="insn-00b0dde8"></a> `00b0dde8` | `e0 07 00 ad` | stp q0,q1,[sp] | `FALL_THROUGH`
<a id="insn-00b0ddec"></a> `00b0ddec` | `e2 0f 01 ad` | stp q2,q3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b0ddf0"></a> `00b0ddf0` | `e4 17 02 ad` | stp q4,q5,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b0ddf4"></a> `00b0ddf4` | `e6 1f 03 ad` | stp q6,q7,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b0ddf8"></a> `00b0ddf8` | `53 d0 3b d5` | mrs x19,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b0ddfc"></a> `00b0ddfc` | `6b 16 40 f9` | ldr x11,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0de00"></a> `00b0de00` | `e8 04 80 92` | mov x8,#-0x28 | `FALL_THROUGH`
<a id="insn-00b0de04"></a> `00b0de04` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-00b0de08"></a> `00b0de08` | `ea 23 02 91` | add x10,sp,#0x88 | `FALL_THROUGH`
<a id="insn-00b0de0c"></a> `00b0de0c` | `08 f0 df f2` | movk x8,#0xff80, LSL #32 | `FALL_THROUGH`
<a id="insn-00b0de10"></a> `00b0de10` | `ac 43 00 91` | add x12,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00b0de14"></a> `00b0de14` | `29 01 02 91` | add x9,x9,#0x80 | `FALL_THROUGH`
<a id="insn-00b0de18"></a> `00b0de18` | `4a a1 00 91` | add x10,x10,#0x28 | `FALL_THROUGH`
<a id="insn-00b0de1c"></a> `00b0de1c` | `ab 83 1e f8` | stur x11,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00b0de20"></a> `00b0de20` | `a9 a3 3d a9` | stp x9,x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00b0de24"></a> `00b0de24` | `ac ab 3c a9` | stp x12,x10,[x29, #-0x38] | `FALL_THROUGH`
<a id="insn-00b0de28"></a> `00b0de28` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00b0de2c"></a> `00b0de2c` | `a9 e3 00 d1` | sub x9,x29,#0x38 | `FALL_THROUGH`
<a id="insn-00b0de30"></a> `00b0de30` | `21 01 40 ad` | ldp q1,q0,[x9] | `FALL_THROUGH`
<a id="insn-00b0de34"></a> `00b0de34` | `a3 83 01 d1` | sub x3,x29,#0x60 | `FALL_THROUGH`
<a id="insn-00b0de38"></a> `00b0de38` | `08 d9 41 f9` | ldr x8,[x8, #0x3b0] | `FALL_THROUGH`
<a id="insn-00b0de3c"></a> `00b0de3c` | `a1 03 3d ad` | stp q1,q0,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00b0de40"></a> `00b0de40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b0de44"></a> `00b0de44` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00b0de48"></a> `00b0de48` | `a9 83 5e f8` | ldur x9,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00b0de4c"></a> `00b0de4c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b0de50"></a> `00b0de50` | `a1 00 00 54` | b.ne 0x00b0de64 | `CONDITIONAL_JUMP`
<a id="insn-00b0de54"></a> `00b0de54` | `fd 7b 51 a9` | ldp x29,x30,[sp, #0x110] | `FALL_THROUGH`
<a id="insn-00b0de58"></a> `00b0de58` | `fc 4f 50 a9` | ldp x28,x19,[sp, #0x100] | `FALL_THROUGH`
<a id="insn-00b0de5c"></a> `00b0de5c` | `ff 83 04 91` | add sp,sp,#0x120 | `FALL_THROUGH`
<a id="insn-00b0de60"></a> `00b0de60` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b0de64"></a> `00b0de64` | `4b 34 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b0ddcc`](#insn-00b0ddcc) 範囲 `[['00b0ddcc', '00b0de53']]`
  - `CONDITIONAL_JUMP` [`00b0de50`](#insn-00b0de50) → [`00b0de64`](#insn-00b0de64)
  - `FALL_THROUGH` [`00b0de50`](#insn-00b0de50) → [`00b0de54`](#insn-00b0de54)
- ブロック [`00b0de54`](#insn-00b0de54) 範囲 `[['00b0de54', '00b0de63']]`
- ブロック [`00b0de64`](#insn-00b0de64) 範囲 `[['00b0de64', '00b0de67']]`

## 命令位置別の参照

- [`00b0ddd0`](#insn-00b0ddd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddd4`](#insn-00b0ddd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dddc`](#insn-00b0dddc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dde0`](#insn-00b0dde0) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dde4`](#insn-00b0dde4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0dde8`](#insn-00b0dde8) → `Stack[-0x120]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddec`](#insn-00b0ddec) → `Stack[-0x100]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddf0`](#insn-00b0ddf0) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0ddf4`](#insn-00b0ddf4) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de1c`](#insn-00b0de1c) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de20`](#insn-00b0de20) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de24`](#insn-00b0de24) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de30`](#insn-00b0de30) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de3c`](#insn-00b0de3c) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de48`](#insn-00b0de48) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de50`](#insn-00b0de50) → [`00b0de64`](#insn-00b0de64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de54`](#insn-00b0de54) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de58`](#insn-00b0de58) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b0de64`](#insn-00b0de64) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b0ddd0`](#insn-00b0ddd0)

~~~json
{
  "source": "00b0ddd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ddd4`](#insn-00b0ddd4)

~~~json
{
  "source": "00b0ddd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dddc`](#insn-00b0dddc)

~~~json
{
  "source": "00b0dddc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dde0`](#insn-00b0dde0)

~~~json
{
  "source": "00b0dde0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dde4`](#insn-00b0dde4)

~~~json
{
  "source": "00b0dde4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0dde8`](#insn-00b0dde8)

~~~json
{
  "source": "00b0dde8",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ddec`](#insn-00b0ddec)

~~~json
{
  "source": "00b0ddec",
  "target": "Stack[-0x100]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ddf0`](#insn-00b0ddf0)

~~~json
{
  "source": "00b0ddf0",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0ddf4`](#insn-00b0ddf4)

~~~json
{
  "source": "00b0ddf4",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de1c`](#insn-00b0de1c)

~~~json
{
  "source": "00b0de1c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de20`](#insn-00b0de20)

~~~json
{
  "source": "00b0de20",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de24`](#insn-00b0de24)

~~~json
{
  "source": "00b0de24",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de30`](#insn-00b0de30)

~~~json
{
  "source": "00b0de30",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de3c`](#insn-00b0de3c)

~~~json
{
  "source": "00b0de3c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de48`](#insn-00b0de48)

~~~json
{
  "source": "00b0de48",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de50`](#insn-00b0de50)

~~~json
{
  "source": "00b0de50",
  "target": "00b0de64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de54`](#insn-00b0de54)

~~~json
{
  "source": "00b0de54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de58`](#insn-00b0de58)

~~~json
{
  "source": "00b0de58",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b0de64`](#insn-00b0de64)

~~~json
{
  "source": "00b0de64",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
