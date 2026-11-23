# 00afaf5c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afb024`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afb024.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-f7030b443e349da7ea8364f1d09b0b47)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afaf5c",
  "name": "_ZNK8firebase10LoggerBase8LogDebugEPKcz",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "72514155a64a7b2e786966e752710d5fb7c66576861bc9360c209d6c223492e4",
  "source_text_sha256": "72514155a64a7b2e786966e752710d5fb7c66576861bc9360c209d6c223492e4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afaf5c",
        "00afb02b"
      ]
    ],
    "bytes_sha256": "91f035c266085f4af5f44e794bffb277e45a74775febae7cd2761251f9bfee7c",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1923 bytes

~~~c

void _ZNK8firebase10LoggerBase8LogDebugEPKcz
               (long *param_1,undefined8 param_2,undefined8 param_3,undefined8 param_4,
               undefined8 param_5,undefined8 param_6,undefined8 param_7,undefined8 param_8)

{
  long lVar1;
  int iVar2;
  undefined8 local_d0;
  undefined8 uStack_c8;
  undefined8 local_c0;
  undefined8 uStack_b8;
  undefined8 local_b0;
  undefined8 uStack_a8;
  undefined1 *local_a0;
  undefined1 **ppuStack_98;
  undefined8 *puStack_90;
  undefined8 uStack_88;
  undefined1 *local_60;
  undefined1 **ppuStack_58;
  undefined8 *puStack_50;
  undefined8 uStack_48;
  long local_38;
  
                    /* try { // try from 00afaf6c to 00bfaf7f has its CatchHandler @ 00aff4d8 */
                    /* try { // try from 00afaf80 to 00bfafaf has its CatchHandler @ 00af560c */
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  ppuStack_98 = &local_a0;
  puStack_90 = &local_d0;
                    /* try { // try from 00afafb0 to 00bfafd3 has its CatchHandler @ 00b0037c */
  uStack_88 = 0xffffff80ffffffd0;
  local_d0 = param_3;
  uStack_c8 = param_4;
  local_c0 = param_5;
  uStack_b8 = param_6;
  local_b0 = param_7;
  uStack_a8 = param_8;
  local_a0 = (undefined1 *)register0x00000008;
                    /* try { // try from 00afafd4 to 00bfafdb has its CatchHandler @ 00aff4d4 */
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 < 2) {
    ppuStack_58 = ppuStack_98;
    local_60 = local_a0;
    uStack_48 = uStack_88;
    puStack_50 = puStack_90;
    (**(code **)(*param_1 + 0x20))(param_1,1,param_2,&local_60);
  }
                    /* try { // try from 00afb004 to 00bfb017 has its CatchHandler @ 00aff4d0 */
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
                    /* try { // try from 00afb028 to 00bfb02f has its CatchHandler @ 00aff4cc */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afaf5c"></a> `00afaf5c` | `ff 43 05 d1` | sub sp,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00afaf60"></a> `00afaf60` | `fc 57 12 a9` | stp x28,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00afaf64"></a> `00afaf64` | `f4 4f 13 a9` | stp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00afaf68"></a> `00afaf68` | `fd 7b 14 a9` | stp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00afaf6c"></a> `00afaf6c` | `fd 03 05 91` | add x29,sp,#0x140 | `FALL_THROUGH`
<a id="insn-00afaf70"></a> `00afaf70` | `e2 0f 08 a9` | stp x2,x3,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00afaf74"></a> `00afaf74` | `e4 17 09 a9` | stp x4,x5,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00afaf78"></a> `00afaf78` | `e6 1f 0a a9` | stp x6,x7,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00afaf7c"></a> `00afaf7c` | `e0 07 00 ad` | stp q0,q1,[sp] | `FALL_THROUGH`
<a id="insn-00afaf80"></a> `00afaf80` | `e2 0f 01 ad` | stp q2,q3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afaf84"></a> `00afaf84` | `e4 17 02 ad` | stp q4,q5,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afaf88"></a> `00afaf88` | `e6 1f 03 ad` | stp q6,q7,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afaf8c"></a> `00afaf8c` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afaf90"></a> `00afaf90` | `ab 16 40 f9` | ldr x11,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00afaf94"></a> `00afaf94` | `e8 03 02 91` | add x8,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00afaf98"></a> `00afaf98` | `ea 05 80 92` | mov x10,#-0x30 | `FALL_THROUGH`
<a id="insn-00afaf9c"></a> `00afaf9c` | `ec 03 00 91` | mov x12,sp | `FALL_THROUGH`
<a id="insn-00afafa0"></a> `00afafa0` | `a9 43 00 91` | add x9,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00afafa4"></a> `00afafa4` | `0a f0 df f2` | movk x10,#0xff80, LSL #32 | `FALL_THROUGH`
<a id="insn-00afafa8"></a> `00afafa8` | `08 c1 00 91` | add x8,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00afafac"></a> `00afafac` | `8c 01 02 91` | add x12,x12,#0x80 | `FALL_THROUGH`
<a id="insn-00afafb0"></a> `00afafb0` | `ab 83 1d f8` | stur x11,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00afafb4"></a> `00afafb4` | `a9 23 39 a9` | stp x9,x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00afafb8"></a> `00afafb8` | `ac 2b 3a a9` | stp x12,x10,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00afafbc"></a> `00afafbc` | `a1 83 7c ad` | ldp q1,q0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00afafc0"></a> `00afafc0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afafc4"></a> `00afafc4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00afafc8"></a> `00afafc8` | `a1 83 3b ad` | stp q1,q0,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00afafcc"></a> `00afafcc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afafd0"></a> `00afafd0` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00afafd4"></a> `00afafd4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afafd8"></a> `00afafd8` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00afafdc"></a> `00afafdc` | `4c 01 00 54` | b.gt 0x00afb004 | `CONDITIONAL_JUMP`
<a id="insn-00afafe0"></a> `00afafe0` | `a0 87 7b ad` | ldp q0,q1,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00afafe4"></a> `00afafe4` | `a3 43 01 d1` | sub x3,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00afafe8"></a> `00afafe8` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00afafec"></a> `00afafec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afaff0"></a> `00afaff0` | `a0 87 3d ad` | stp q0,q1,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00afaff4"></a> `00afaff4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afaff8"></a> `00afaff8` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00afaffc"></a> `00afaffc` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00afb000"></a> `00afb000` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afb004"></a> `00afb004` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00afb008"></a> `00afb008` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00afb00c"></a> `00afb00c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afb010"></a> `00afb010` | `c1 00 00 54` | b.ne 0x00afb028 | `CONDITIONAL_JUMP`
<a id="insn-00afb014"></a> `00afb014` | `fd 7b 54 a9` | ldp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00afb018"></a> `00afb018` | `f4 4f 53 a9` | ldp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00afb01c"></a> `00afb01c` | `fc 57 52 a9` | ldp x28,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00afb020"></a> `00afb020` | `ff 43 05 91` | add sp,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00afb024"></a> `00afb024` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afb028"></a> `00afb028` | `da 7f 03 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afaf5c`](#insn-00afaf5c) 範囲 `[['00afaf5c', '00afaf6b']]`
  - `FALL_THROUGH` [`00afaf68`](#insn-00afaf68) → [`00afaf6c`](#insn-00afaf6c)
- ブロック [`00afaf6c`](#insn-00afaf6c) 範囲 `[['00afaf6c', '00afaf7f']]`
  - `FALL_THROUGH` [`00afaf7c`](#insn-00afaf7c) → [`00afaf80`](#insn-00afaf80)
- ブロック [`00afaf80`](#insn-00afaf80) 範囲 `[['00afaf80', '00afafaf']]`
  - `FALL_THROUGH` [`00afafac`](#insn-00afafac) → [`00afafb0`](#insn-00afafb0)
- ブロック [`00afafb0`](#insn-00afafb0) 範囲 `[['00afafb0', '00afafd3']]`
  - `FALL_THROUGH` [`00afafd0`](#insn-00afafd0) → [`00afafd4`](#insn-00afafd4)
- ブロック [`00afafd4`](#insn-00afafd4) 範囲 `[['00afafd4', '00afafdf']]`
  - `CONDITIONAL_JUMP` [`00afafdc`](#insn-00afafdc) → [`00afb004`](#insn-00afb004)
  - `FALL_THROUGH` [`00afafdc`](#insn-00afafdc) → [`00afafe0`](#insn-00afafe0)
- ブロック [`00afafe0`](#insn-00afafe0) 範囲 `[['00afafe0', '00afb003']]`
  - `FALL_THROUGH` [`00afb000`](#insn-00afb000) → [`00afb004`](#insn-00afb004)
- ブロック [`00afb004`](#insn-00afb004) 範囲 `[['00afb004', '00afb013']]`
  - `CONDITIONAL_JUMP` [`00afb010`](#insn-00afb010) → [`00afb028`](#insn-00afb028)
  - `FALL_THROUGH` [`00afb010`](#insn-00afb010) → [`00afb014`](#insn-00afb014)
- ブロック [`00afb014`](#insn-00afb014) 範囲 `[['00afb014', '00afb027']]`
- ブロック [`00afb028`](#insn-00afb028) 範囲 `[['00afb028', '00afb02b']]`

## 命令位置別の参照

- [`00afaf60`](#insn-00afaf60) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf64`](#insn-00afaf64) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf68`](#insn-00afaf68) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf70`](#insn-00afaf70) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf74`](#insn-00afaf74) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf78`](#insn-00afaf78) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf7c`](#insn-00afaf7c) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf80`](#insn-00afaf80) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf84`](#insn-00afaf84) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaf88`](#insn-00afaf88) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafb0`](#insn-00afafb0) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafb4`](#insn-00afafb4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafb8`](#insn-00afafb8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafbc`](#insn-00afafbc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafc8`](#insn-00afafc8) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafdc`](#insn-00afafdc) → [`00afb004`](#insn-00afb004) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afafe0`](#insn-00afafe0) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afaff0`](#insn-00afaff0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb008`](#insn-00afb008) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb010`](#insn-00afb010) → [`00afb028`](#insn-00afb028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb014`](#insn-00afb014) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb018`](#insn-00afb018) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb01c`](#insn-00afb01c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb028`](#insn-00afb028) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afaf60`](#insn-00afaf60)

~~~json
{
  "source": "00afaf60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf64`](#insn-00afaf64)

~~~json
{
  "source": "00afaf64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf68`](#insn-00afaf68)

~~~json
{
  "source": "00afaf68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf70`](#insn-00afaf70)

~~~json
{
  "source": "00afaf70",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf74`](#insn-00afaf74)

~~~json
{
  "source": "00afaf74",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf78`](#insn-00afaf78)

~~~json
{
  "source": "00afaf78",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf7c`](#insn-00afaf7c)

~~~json
{
  "source": "00afaf7c",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf80`](#insn-00afaf80)

~~~json
{
  "source": "00afaf80",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf84`](#insn-00afaf84)

~~~json
{
  "source": "00afaf84",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaf88`](#insn-00afaf88)

~~~json
{
  "source": "00afaf88",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafb0`](#insn-00afafb0)

~~~json
{
  "source": "00afafb0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafb4`](#insn-00afafb4)

~~~json
{
  "source": "00afafb4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafb8`](#insn-00afafb8)

~~~json
{
  "source": "00afafb8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafbc`](#insn-00afafbc)

~~~json
{
  "source": "00afafbc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafc8`](#insn-00afafc8)

~~~json
{
  "source": "00afafc8",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafdc`](#insn-00afafdc)

~~~json
{
  "source": "00afafdc",
  "target": "00afb004",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afafe0`](#insn-00afafe0)

~~~json
{
  "source": "00afafe0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afaff0`](#insn-00afaff0)

~~~json
{
  "source": "00afaff0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb008`](#insn-00afb008)

~~~json
{
  "source": "00afb008",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb010`](#insn-00afb010)

~~~json
{
  "source": "00afb010",
  "target": "00afb028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb014`](#insn-00afb014)

~~~json
{
  "source": "00afb014",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb018`](#insn-00afb018)

~~~json
{
  "source": "00afb018",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb01c`](#insn-00afb01c)

~~~json
{
  "source": "00afb01c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb028`](#insn-00afb028)

~~~json
{
  "source": "00afb028",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
