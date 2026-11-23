# 00afb3fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afb334`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb334.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-55d2e4e48378d40fb397223313113bfb)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afb440`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afb440.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0008.md#compare-317ea18519d360e2a28bdfb7a4342da0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afb3fc",
  "name": "_ZNK8firebase10LoggerBase9LogAssertEPKcz",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2f6fa6a25958c0338ff31fcc96fc43d93ca42c74e8a6fa6c344168643733b379",
  "source_text_sha256": "2f6fa6a25958c0338ff31fcc96fc43d93ca42c74e8a6fa6c344168643733b379",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afb3fc",
        "00afb4cb"
      ]
    ],
    "bytes_sha256": "e4921d944ed4b86f73babd0c133511a3b2c12a31ddeeefa64eb04ddfc48337d2",
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

- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1633 bytes

~~~c

void _ZNK8firebase10LoggerBase9LogAssertEPKcz
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
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
                    /* try { // try from 00afb438 to 00bfb447 has its CatchHandler @ 00aff488 */
  ppuStack_98 = &local_a0;
  puStack_90 = &local_d0;
                    /* try { // try from 00afb458 to 00bfb45f has its CatchHandler @ 00aff484 */
  uStack_88 = 0xffffff80ffffffd0;
  local_d0 = param_3;
  uStack_c8 = param_4;
  local_c0 = param_5;
  uStack_b8 = param_6;
  local_b0 = param_7;
  uStack_a8 = param_8;
  local_a0 = (undefined1 *)register0x00000008;
  iVar2 = (**(code **)(*param_1 + 0x18))();
  if (iVar2 < 6) {
                    /* try { // try from 00afb488 to 00bfb49b has its CatchHandler @ 00aff480 */
    ppuStack_58 = ppuStack_98;
    local_60 = local_a0;
    uStack_48 = uStack_88;
    puStack_50 = puStack_90;
    (**(code **)(*param_1 + 0x20))(param_1,5,param_2,&local_60);
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-00afb3fc"></a> `00afb3fc` | `ff 43 05 d1` | sub sp,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00afb400"></a> `00afb400` | `fc 57 12 a9` | stp x28,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00afb404"></a> `00afb404` | `f4 4f 13 a9` | stp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00afb408"></a> `00afb408` | `fd 7b 14 a9` | stp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00afb40c"></a> `00afb40c` | `fd 03 05 91` | add x29,sp,#0x140 | `FALL_THROUGH`
<a id="insn-00afb410"></a> `00afb410` | `e2 0f 08 a9` | stp x2,x3,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00afb414"></a> `00afb414` | `e4 17 09 a9` | stp x4,x5,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00afb418"></a> `00afb418` | `e6 1f 0a a9` | stp x6,x7,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00afb41c"></a> `00afb41c` | `e0 07 00 ad` | stp q0,q1,[sp] | `FALL_THROUGH`
<a id="insn-00afb420"></a> `00afb420` | `e2 0f 01 ad` | stp q2,q3,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afb424"></a> `00afb424` | `e4 17 02 ad` | stp q4,q5,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afb428"></a> `00afb428` | `e6 1f 03 ad` | stp q6,q7,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00afb42c"></a> `00afb42c` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afb430"></a> `00afb430` | `ab 16 40 f9` | ldr x11,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00afb434"></a> `00afb434` | `e8 03 02 91` | add x8,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00afb438"></a> `00afb438` | `ea 05 80 92` | mov x10,#-0x30 | `FALL_THROUGH`
<a id="insn-00afb43c"></a> `00afb43c` | `ec 03 00 91` | mov x12,sp | `FALL_THROUGH`
<a id="insn-00afb440"></a> `00afb440` | `a9 43 00 91` | add x9,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00afb444"></a> `00afb444` | `0a f0 df f2` | movk x10,#0xff80, LSL #32 | `FALL_THROUGH`
<a id="insn-00afb448"></a> `00afb448` | `08 c1 00 91` | add x8,x8,#0x30 | `FALL_THROUGH`
<a id="insn-00afb44c"></a> `00afb44c` | `8c 01 02 91` | add x12,x12,#0x80 | `FALL_THROUGH`
<a id="insn-00afb450"></a> `00afb450` | `ab 83 1d f8` | stur x11,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00afb454"></a> `00afb454` | `a9 23 39 a9` | stp x9,x8,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00afb458"></a> `00afb458` | `ac 2b 3a a9` | stp x12,x10,[x29, #-0x60] | `FALL_THROUGH`
<a id="insn-00afb45c"></a> `00afb45c` | `a1 83 7c ad` | ldp q1,q0,[x29, #-0x70] | `FALL_THROUGH`
<a id="insn-00afb460"></a> `00afb460` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afb464"></a> `00afb464` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00afb468"></a> `00afb468` | `a1 83 3b ad` | stp q1,q0,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00afb46c"></a> `00afb46c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00afb470"></a> `00afb470` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00afb474"></a> `00afb474` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afb478"></a> `00afb478` | `1f 14 00 71` | cmp w0,#0x5 | `FALL_THROUGH`
<a id="insn-00afb47c"></a> `00afb47c` | `4c 01 00 54` | b.gt 0x00afb4a4 | `CONDITIONAL_JUMP`
<a id="insn-00afb480"></a> `00afb480` | `a0 87 7b ad` | ldp q0,q1,[x29, #-0x90] | `FALL_THROUGH`
<a id="insn-00afb484"></a> `00afb484` | `a3 43 01 d1` | sub x3,x29,#0x50 | `FALL_THROUGH`
<a id="insn-00afb488"></a> `00afb488` | `a1 00 80 52` | mov w1,#0x5 | `FALL_THROUGH`
<a id="insn-00afb48c"></a> `00afb48c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afb490"></a> `00afb490` | `a0 87 3d ad` | stp q0,q1,[x29, #-0x50] | `FALL_THROUGH`
<a id="insn-00afb494"></a> `00afb494` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afb498"></a> `00afb498` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00afb49c"></a> `00afb49c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00afb4a0"></a> `00afb4a0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afb4a4"></a> `00afb4a4` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00afb4a8"></a> `00afb4a8` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00afb4ac"></a> `00afb4ac` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afb4b0"></a> `00afb4b0` | `c1 00 00 54` | b.ne 0x00afb4c8 | `CONDITIONAL_JUMP`
<a id="insn-00afb4b4"></a> `00afb4b4` | `fd 7b 54 a9` | ldp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-00afb4b8"></a> `00afb4b8` | `f4 4f 53 a9` | ldp x20,x19,[sp, #0x130] | `FALL_THROUGH`
<a id="insn-00afb4bc"></a> `00afb4bc` | `fc 57 52 a9` | ldp x28,x21,[sp, #0x120] | `FALL_THROUGH`
<a id="insn-00afb4c0"></a> `00afb4c0` | `ff 43 05 91` | add sp,sp,#0x150 | `FALL_THROUGH`
<a id="insn-00afb4c4"></a> `00afb4c4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afb4c8"></a> `00afb4c8` | `de 7e 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afb3fc`](#insn-00afb3fc) 範囲 `[['00afb3fc', '00afb437']]`
  - `FALL_THROUGH` [`00afb434`](#insn-00afb434) → [`00afb438`](#insn-00afb438)
- ブロック [`00afb438`](#insn-00afb438) 範囲 `[['00afb438', '00afb457']]`
  - `FALL_THROUGH` [`00afb454`](#insn-00afb454) → [`00afb458`](#insn-00afb458)
- ブロック [`00afb458`](#insn-00afb458) 範囲 `[['00afb458', '00afb47f']]`
  - `CONDITIONAL_JUMP` [`00afb47c`](#insn-00afb47c) → [`00afb4a4`](#insn-00afb4a4)
  - `FALL_THROUGH` [`00afb47c`](#insn-00afb47c) → [`00afb480`](#insn-00afb480)
- ブロック [`00afb480`](#insn-00afb480) 範囲 `[['00afb480', '00afb487']]`
  - `FALL_THROUGH` [`00afb484`](#insn-00afb484) → [`00afb488`](#insn-00afb488)
- ブロック [`00afb488`](#insn-00afb488) 範囲 `[['00afb488', '00afb4a3']]`
  - `FALL_THROUGH` [`00afb4a0`](#insn-00afb4a0) → [`00afb4a4`](#insn-00afb4a4)
- ブロック [`00afb4a4`](#insn-00afb4a4) 範囲 `[['00afb4a4', '00afb4b3']]`
  - `CONDITIONAL_JUMP` [`00afb4b0`](#insn-00afb4b0) → [`00afb4c8`](#insn-00afb4c8)
  - `FALL_THROUGH` [`00afb4b0`](#insn-00afb4b0) → [`00afb4b4`](#insn-00afb4b4)
- ブロック [`00afb4b4`](#insn-00afb4b4) 範囲 `[['00afb4b4', '00afb4c7']]`
- ブロック [`00afb4c8`](#insn-00afb4c8) 範囲 `[['00afb4c8', '00afb4cb']]`

## 命令位置別の参照

- [`00afb400`](#insn-00afb400) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb404`](#insn-00afb404) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb408`](#insn-00afb408) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb410`](#insn-00afb410) → `Stack[-0xd0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb414`](#insn-00afb414) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb418`](#insn-00afb418) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb41c`](#insn-00afb41c) → `Stack[-0x150]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb420`](#insn-00afb420) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb424`](#insn-00afb424) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb428`](#insn-00afb428) → `Stack[-0xf0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb450`](#insn-00afb450) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb454`](#insn-00afb454) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb458`](#insn-00afb458) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb45c`](#insn-00afb45c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb468`](#insn-00afb468) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb47c`](#insn-00afb47c) → [`00afb4a4`](#insn-00afb4a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb480`](#insn-00afb480) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb490`](#insn-00afb490) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4a8`](#insn-00afb4a8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4b0`](#insn-00afb4b0) → [`00afb4c8`](#insn-00afb4c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4b4`](#insn-00afb4b4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4b8`](#insn-00afb4b8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4bc`](#insn-00afb4bc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afb4c8`](#insn-00afb4c8) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afb400`](#insn-00afb400)

~~~json
{
  "source": "00afb400",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb404`](#insn-00afb404)

~~~json
{
  "source": "00afb404",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb408`](#insn-00afb408)

~~~json
{
  "source": "00afb408",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb410`](#insn-00afb410)

~~~json
{
  "source": "00afb410",
  "target": "Stack[-0xd0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb414`](#insn-00afb414)

~~~json
{
  "source": "00afb414",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb418`](#insn-00afb418)

~~~json
{
  "source": "00afb418",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb41c`](#insn-00afb41c)

~~~json
{
  "source": "00afb41c",
  "target": "Stack[-0x150]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb420`](#insn-00afb420)

~~~json
{
  "source": "00afb420",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb424`](#insn-00afb424)

~~~json
{
  "source": "00afb424",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb428`](#insn-00afb428)

~~~json
{
  "source": "00afb428",
  "target": "Stack[-0xf0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb450`](#insn-00afb450)

~~~json
{
  "source": "00afb450",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb454`](#insn-00afb454)

~~~json
{
  "source": "00afb454",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb458`](#insn-00afb458)

~~~json
{
  "source": "00afb458",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb45c`](#insn-00afb45c)

~~~json
{
  "source": "00afb45c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb468`](#insn-00afb468)

~~~json
{
  "source": "00afb468",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb47c`](#insn-00afb47c)

~~~json
{
  "source": "00afb47c",
  "target": "00afb4a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb480`](#insn-00afb480)

~~~json
{
  "source": "00afb480",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb490`](#insn-00afb490)

~~~json
{
  "source": "00afb490",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4a8`](#insn-00afb4a8)

~~~json
{
  "source": "00afb4a8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4b0`](#insn-00afb4b0)

~~~json
{
  "source": "00afb4b0",
  "target": "00afb4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4b4`](#insn-00afb4b4)

~~~json
{
  "source": "00afb4b4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4b8`](#insn-00afb4b8)

~~~json
{
  "source": "00afb4b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4bc`](#insn-00afb4bc)

~~~json
{
  "source": "00afb4bc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afb4c8`](#insn-00afb4c8)

~~~json
{
  "source": "00afb4c8",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
