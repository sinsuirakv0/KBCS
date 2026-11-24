# 00adb1fc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00adb1b8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00adb/00adb1b8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-7f79f46f87b8ef90839b648fd4e029e8)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b3abd4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b3a/00b3abd4.md) · 移動量 `+0x5f9d8`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0055.md#compare-8a75d8848cfa6338026d5e3120645e40)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adb1fc",
  "name": "FUN_00adb1fc",
  "size": 176,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "51f89bee2858cff0913ea4bfcba00185b89e3358c4f52dfb2a3a740401024cf7",
  "source_text_sha256": "51f89bee2858cff0913ea4bfcba00185b89e3358c4f52dfb2a3a740401024cf7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adb1fc",
        "00adb2ab"
      ]
    ],
    "bytes_sha256": "b9a2c0f0717cece264bdf6981ad92f8752257e33109ac8cdbfc1138b126e9ffa",
    "instruction_count": 44,
    "instruction_bytes": 176,
    "body_bytes": 176,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00ad9110](../00ad9/00ad9110.md)
- [00adb1fc](../00adb/00adb1fc.md)

## 呼び出し先

- [00adb1fc](../00adb/00adb1fc.md)
- [00bdb060](../00bdb/00bdb060.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1075 bytes

~~~c

void FUN_00adb1fc(undefined8 param_1,undefined8 *param_2)

{
  long *plVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  
  if (param_2 == (undefined8 *)0x0) {
    return;
  }
                    /* try { // try from 00adb214 to 00bdb217 has its CatchHandler @ 00adb900 */
  FUN_00adb1fc(param_1,*param_2);
  FUN_00adb1fc(param_1,param_2[1]);
  plVar1 = (long *)param_2[0x12];
  plVar2 = param_2 + 0xe;
  plVar3 = param_2 + 8;
  if (plVar1 == plVar2) {
    lVar4 = 0x20;
LAB_00adb254:
    (**(code **)(*plVar2 + lVar4))();
  }
  else if (plVar1 != (long *)0x0) {
    lVar4 = 0x28;
    plVar2 = plVar1;
    goto LAB_00adb254;
  }
  plVar2 = (long *)param_2[0xc];
  if (plVar2 == plVar3) {
    lVar4 = 0x20;
  }
  else {
    if (plVar2 == (long *)0x0) goto LAB_00adb28c;
    lVar4 = 0x28;
    plVar3 = plVar2;
  }
  (**(code **)(*plVar3 + lVar4))();
LAB_00adb28c:
  if ((*(byte *)(param_2 + 4) & 1) != 0) {
                    /* try { // try from 00adb298 to 00bdb2a3 has its CatchHandler @ 00adb8d0 */
    _ZdlPv((void *)param_2[6]);
  }
  _ZdlPv(param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adb1fc"></a> `00adb1fc` | `61 02 00 b4` | cbz x1,0x00adb248 | `CONDITIONAL_JUMP`
<a id="insn-00adb200"></a> `00adb200` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00adb204"></a> `00adb204` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adb208"></a> `00adb208` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00adb20c"></a> `00adb20c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00adb210"></a> `00adb210` | `21 00 40 f9` | ldr x1,[x1] | `FALL_THROUGH`
<a id="insn-00adb214"></a> `00adb214` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00adb218"></a> `00adb218` | `f9 ff ff 97` | bl 0x00adb1fc | `UNCONDITIONAL_CALL`
<a id="insn-00adb21c"></a> `00adb21c` | `61 06 40 f9` | ldr x1,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00adb220"></a> `00adb220` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adb224"></a> `00adb224` | `f6 ff ff 97` | bl 0x00adb1fc | `UNCONDITIONAL_CALL`
<a id="insn-00adb228"></a> `00adb228` | `60 4a 40 f9` | ldr x0,[x19, #0x90] | `FALL_THROUGH`
<a id="insn-00adb22c"></a> `00adb22c` | `69 c2 01 91` | add x9,x19,#0x70 | `FALL_THROUGH`
<a id="insn-00adb230"></a> `00adb230` | `74 02 01 91` | add x20,x19,#0x40 | `FALL_THROUGH`
<a id="insn-00adb234"></a> `00adb234` | `1f 00 09 eb` | cmp x0,x9 | `FALL_THROUGH`
<a id="insn-00adb238"></a> `00adb238` | `a0 00 00 54` | b.eq 0x00adb24c | `CONDITIONAL_JUMP`
<a id="insn-00adb23c"></a> `00adb23c` | `20 01 00 b4` | cbz x0,0x00adb260 | `CONDITIONAL_JUMP`
<a id="insn-00adb240"></a> `00adb240` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00adb244"></a> `00adb244` | `04 00 00 14` | b 0x00adb254 | `UNCONDITIONAL_JUMP`
<a id="insn-00adb248"></a> `00adb248` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00adb24c"></a> `00adb24c` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00adb250"></a> `00adb250` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-00adb254"></a> `00adb254` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00adb258"></a> `00adb258` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00adb25c"></a> `00adb25c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb260"></a> `00adb260` | `60 32 40 f9` | ldr x0,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00adb264"></a> `00adb264` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00adb268"></a> `00adb268` | `80 00 00 54` | b.eq 0x00adb278 | `CONDITIONAL_JUMP`
<a id="insn-00adb26c"></a> `00adb26c` | `00 01 00 b4` | cbz x0,0x00adb28c | `CONDITIONAL_JUMP`
<a id="insn-00adb270"></a> `00adb270` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00adb274"></a> `00adb274` | `03 00 00 14` | b 0x00adb280 | `UNCONDITIONAL_JUMP`
<a id="insn-00adb278"></a> `00adb278` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00adb27c"></a> `00adb27c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00adb280"></a> `00adb280` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00adb284"></a> `00adb284` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00adb288"></a> `00adb288` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00adb28c"></a> `00adb28c` | `68 82 40 39` | ldrb w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00adb290"></a> `00adb290` | `68 00 00 36` | tbz w8,#0x0,0x00adb29c | `CONDITIONAL_JUMP`
<a id="insn-00adb294"></a> `00adb294` | `60 1a 40 f9` | ldr x0,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00adb298"></a> `00adb298` | `72 ff 03 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00adb29c"></a> `00adb29c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00adb2a0"></a> `00adb2a0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adb2a4"></a> `00adb2a4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00adb2a8"></a> `00adb2a8` | `6e ff 03 14` | b 0x00bdb060 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adb1fc`](#insn-00adb1fc) 範囲 `[['00adb1fc', '00adb1ff']]`
  - `CONDITIONAL_JUMP` [`00adb1fc`](#insn-00adb1fc) → [`00adb248`](#insn-00adb248)
  - `FALL_THROUGH` [`00adb1fc`](#insn-00adb1fc) → [`00adb200`](#insn-00adb200)
- ブロック [`00adb200`](#insn-00adb200) 範囲 `[['00adb200', '00adb213']]`
  - `FALL_THROUGH` [`00adb210`](#insn-00adb210) → [`00adb214`](#insn-00adb214)
- ブロック [`00adb214`](#insn-00adb214) 範囲 `[['00adb214', '00adb23b']]`
  - `CONDITIONAL_JUMP` [`00adb238`](#insn-00adb238) → [`00adb24c`](#insn-00adb24c)
  - `FALL_THROUGH` [`00adb238`](#insn-00adb238) → [`00adb23c`](#insn-00adb23c)
- ブロック [`00adb23c`](#insn-00adb23c) 範囲 `[['00adb23c', '00adb23f']]`
  - `CONDITIONAL_JUMP` [`00adb23c`](#insn-00adb23c) → [`00adb260`](#insn-00adb260)
  - `FALL_THROUGH` [`00adb23c`](#insn-00adb23c) → [`00adb240`](#insn-00adb240)
- ブロック [`00adb240`](#insn-00adb240) 範囲 `[['00adb240', '00adb247']]`
  - `UNCONDITIONAL_JUMP` [`00adb244`](#insn-00adb244) → [`00adb254`](#insn-00adb254)
- ブロック [`00adb248`](#insn-00adb248) 範囲 `[['00adb248', '00adb24b']]`
- ブロック [`00adb24c`](#insn-00adb24c) 範囲 `[['00adb24c', '00adb253']]`
  - `FALL_THROUGH` [`00adb250`](#insn-00adb250) → [`00adb254`](#insn-00adb254)
- ブロック [`00adb254`](#insn-00adb254) 範囲 `[['00adb254', '00adb25f']]`
  - `FALL_THROUGH` [`00adb25c`](#insn-00adb25c) → [`00adb260`](#insn-00adb260)
- ブロック [`00adb260`](#insn-00adb260) 範囲 `[['00adb260', '00adb26b']]`
  - `CONDITIONAL_JUMP` [`00adb268`](#insn-00adb268) → [`00adb278`](#insn-00adb278)
  - `FALL_THROUGH` [`00adb268`](#insn-00adb268) → [`00adb26c`](#insn-00adb26c)
- ブロック [`00adb26c`](#insn-00adb26c) 範囲 `[['00adb26c', '00adb26f']]`
  - `CONDITIONAL_JUMP` [`00adb26c`](#insn-00adb26c) → [`00adb28c`](#insn-00adb28c)
  - `FALL_THROUGH` [`00adb26c`](#insn-00adb26c) → [`00adb270`](#insn-00adb270)
- ブロック [`00adb270`](#insn-00adb270) 範囲 `[['00adb270', '00adb277']]`
  - `UNCONDITIONAL_JUMP` [`00adb274`](#insn-00adb274) → [`00adb280`](#insn-00adb280)
- ブロック [`00adb278`](#insn-00adb278) 範囲 `[['00adb278', '00adb27f']]`
  - `FALL_THROUGH` [`00adb27c`](#insn-00adb27c) → [`00adb280`](#insn-00adb280)
- ブロック [`00adb280`](#insn-00adb280) 範囲 `[['00adb280', '00adb28b']]`
  - `FALL_THROUGH` [`00adb288`](#insn-00adb288) → [`00adb28c`](#insn-00adb28c)
- ブロック [`00adb28c`](#insn-00adb28c) 範囲 `[['00adb28c', '00adb293']]`
  - `CONDITIONAL_JUMP` [`00adb290`](#insn-00adb290) → [`00adb29c`](#insn-00adb29c)
  - `FALL_THROUGH` [`00adb290`](#insn-00adb290) → [`00adb294`](#insn-00adb294)
- ブロック [`00adb294`](#insn-00adb294) 範囲 `[['00adb294', '00adb297']]`
  - `FALL_THROUGH` [`00adb294`](#insn-00adb294) → [`00adb298`](#insn-00adb298)
- ブロック [`00adb298`](#insn-00adb298) 範囲 `[['00adb298', '00adb29b']]`
  - `FALL_THROUGH` [`00adb298`](#insn-00adb298) → [`00adb29c`](#insn-00adb29c)
- ブロック [`00adb29c`](#insn-00adb29c) 範囲 `[['00adb29c', '00adb2ab']]`

## 命令位置別の参照

- [`00adb1fc`](#insn-00adb1fc) → [`00adb248`](#insn-00adb248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb200`](#insn-00adb200) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb204`](#insn-00adb204) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb218`](#insn-00adb218) → [`00adb1fc`](#insn-00adb1fc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adb1fc` · 推定シンボル `None` · 推定型 `None`
- [`00adb224`](#insn-00adb224) → [`00adb1fc`](#insn-00adb1fc) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00adb1fc` · 推定シンボル `None` · 推定型 `None`
- [`00adb238`](#insn-00adb238) → [`00adb24c`](#insn-00adb24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb23c`](#insn-00adb23c) → [`00adb260`](#insn-00adb260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb244`](#insn-00adb244) → [`00adb254`](#insn-00adb254) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb268`](#insn-00adb268) → [`00adb278`](#insn-00adb278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb26c`](#insn-00adb26c) → [`00adb28c`](#insn-00adb28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb274`](#insn-00adb274) → [`00adb280`](#insn-00adb280) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb290`](#insn-00adb290) → [`00adb29c`](#insn-00adb29c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb298`](#insn-00adb298) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00adb2a0`](#insn-00adb2a0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb2a4`](#insn-00adb2a4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adb2a8`](#insn-00adb2a8) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adb1fc`](#insn-00adb1fc)

~~~json
{
  "source": "00adb1fc",
  "target": "00adb248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb200`](#insn-00adb200)

~~~json
{
  "source": "00adb200",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb204`](#insn-00adb204)

~~~json
{
  "source": "00adb204",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb218`](#insn-00adb218)

~~~json
{
  "source": "00adb218",
  "target": "00adb1fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adb224`](#insn-00adb224)

~~~json
{
  "source": "00adb224",
  "target": "00adb1fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adb238`](#insn-00adb238)

~~~json
{
  "source": "00adb238",
  "target": "00adb24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb23c`](#insn-00adb23c)

~~~json
{
  "source": "00adb23c",
  "target": "00adb260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb244`](#insn-00adb244)

~~~json
{
  "source": "00adb244",
  "target": "00adb254",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb268`](#insn-00adb268)

~~~json
{
  "source": "00adb268",
  "target": "00adb278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb26c`](#insn-00adb26c)

~~~json
{
  "source": "00adb26c",
  "target": "00adb28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb274`](#insn-00adb274)

~~~json
{
  "source": "00adb274",
  "target": "00adb280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb290`](#insn-00adb290)

~~~json
{
  "source": "00adb290",
  "target": "00adb29c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb298`](#insn-00adb298)

~~~json
{
  "source": "00adb298",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adb2a0`](#insn-00adb2a0)

~~~json
{
  "source": "00adb2a0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb2a4`](#insn-00adb2a4)

~~~json
{
  "source": "00adb2a4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adb2a8`](#insn-00adb2a8)

~~~json
{
  "source": "00adb2a8",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
