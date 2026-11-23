# 005dfdec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `005dfdec`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/005df/005dfdec.md) · 移動量 `+0x0`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/machine_only_observed-0014.md#compare-2c573f0519bffd14856ed5f03c603b31)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "005dfdec",
  "name": "FUN_005dfdec",
  "size": 196,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2fe0e202d96459d874a9cfbf5a68e09cba4926ccdbd719bb12a2716c1511ad29",
  "source_text_sha256": "2fe0e202d96459d874a9cfbf5a68e09cba4926ccdbd719bb12a2716c1511ad29",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "005dfdec",
        "005dfeaf"
      ]
    ],
    "bytes_sha256": "a7d0d32aacfe40edcd701a4e2ebc039b16c0f1dc8d98232b3a829ee9a5c668fc",
    "instruction_count": 49,
    "instruction_bytes": 196,
    "body_bytes": 196,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005e1a5c](../005e1/005e1a5c.md)
- [006d6d04](../006d6/006d6d04.md)
- [00713660](../00713/00713660.md)
- [007317b0](../00731/007317b0.md)
- [0079bdf0](../0079b/0079bdf0.md)
- [007e228c](../007e2/007e228c.md)
- [009121c4](../00912/009121c4.md)
- [0099a654](../0099a/0099a654.md)
- [009a9ce0](../009a9/009a9ce0.md)
- [00a806b4](../00a80/00a806b4.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [00bdaf40](../00bda/00bdaf40.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1498 bytes

~~~c

long * FUN_005dfdec(long *param_1,int *param_2)

{
  int iVar1;
  long *plVar2;
  long *plVar3;
  long *plVar4;
  long *plVar5;
  
                    /* try { // try from 005dfe04 to 006dfe0b has its CatchHandler @ 005dff0c */
  iVar1 = *param_2;
  plVar4 = param_1 + 1;
  plVar3 = (long *)*plVar4;
  plVar5 = plVar4;
  if ((long *)*plVar4 != (long *)0x0) {
    do {
      while (plVar2 = plVar3, plVar4 = plVar2, iVar1 < *(int *)((long)plVar2 + 0x1c)) {
                    /* try { // try from 005dfe1c to 006dfe27 has its CatchHandler @ 005dfef0 */
        plVar3 = (long *)*plVar2;
        plVar5 = plVar2;
        if ((long *)*plVar2 == (long *)0x0) goto LAB_005dfe4c;
      }
      if (iVar1 <= *(int *)((long)plVar2 + 0x1c)) goto LAB_005dfe98;
      plVar3 = (long *)plVar2[1];
    } while ((long *)plVar2[1] != (long *)0x0);
    plVar5 = plVar2 + 1;
  }
LAB_005dfe4c:
                    /* try { // try from 005dfe54 to 006dfe5f has its CatchHandler @ 005dfed4 */
  plVar2 = (long *)_Znwm(0x28);
  *plVar2 = 0;
  plVar2[1] = 0;
                    /* try { // try from 005dfe60 to 006dff23 has its CatchHandler @ 005dfd64 */
  plVar2[2] = (long)plVar4;
  *plVar5 = (long)plVar2;
  plVar4 = (long *)*param_1;
  *(int *)((long)plVar2 + 0x1c) = iVar1;
  *(undefined4 *)(plVar2 + 4) = 0;
  plVar3 = plVar2;
  if (*plVar4 != 0) {
    *param_1 = *plVar4;
    plVar3 = (long *)*plVar5;
  }
  FUN_00419064(param_1[1],plVar3);
  param_1[2] = param_1[2] + 1;
LAB_005dfe98:
  return plVar2 + 4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-005dfdec"></a> `005dfdec` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-005dfdf0"></a> `005dfdf0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005dfdf4"></a> `005dfdf4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005dfdf8"></a> `005dfdf8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005dfdfc"></a> `005dfdfc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-005dfe00"></a> `005dfe00` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-005dfe04"></a> `005dfe04` | `35 00 40 b9` | ldr w21,[x1] | `FALL_THROUGH`
<a id="insn-005dfe08"></a> `005dfe08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-005dfe0c"></a> `005dfe0c` | `c8 8e 40 f8` | ldr x8,[x22, #0x8]! | `FALL_THROUGH`
<a id="insn-005dfe10"></a> `005dfe10` | `c8 00 00 b5` | cbnz x8,0x005dfe28 | `CONDITIONAL_JUMP`
<a id="insn-005dfe14"></a> `005dfe14` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-005dfe18"></a> `005dfe18` | `0d 00 00 14` | b 0x005dfe4c | `UNCONDITIONAL_JUMP`
<a id="insn-005dfe1c"></a> `005dfe1c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-005dfe20"></a> `005dfe20` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-005dfe24"></a> `005dfe24` | `48 01 00 b4` | cbz x8,0x005dfe4c | `CONDITIONAL_JUMP`
<a id="insn-005dfe28"></a> `005dfe28` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-005dfe2c"></a> `005dfe2c` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-005dfe30"></a> `005dfe30` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-005dfe34"></a> `005dfe34` | `4b ff ff 54` | b.lt 0x005dfe1c | `CONDITIONAL_JUMP`
<a id="insn-005dfe38"></a> `005dfe38` | `1f 01 15 6b` | cmp w8,w21 | `FALL_THROUGH`
<a id="insn-005dfe3c"></a> `005dfe3c` | `ea 02 00 54` | b.ge 0x005dfe98 | `CONDITIONAL_JUMP`
<a id="insn-005dfe40"></a> `005dfe40` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-005dfe44"></a> `005dfe44` | `28 ff ff b5` | cbnz x8,0x005dfe28 | `CONDITIONAL_JUMP`
<a id="insn-005dfe48"></a> `005dfe48` | `96 22 00 91` | add x22,x20,#0x8 | `FALL_THROUGH`
<a id="insn-005dfe4c"></a> `005dfe4c` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-005dfe50"></a> `005dfe50` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-005dfe54"></a> `005dfe54` | `3b ec 17 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-005dfe58"></a> `005dfe58` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-005dfe5c"></a> `005dfe5c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-005dfe60"></a> `005dfe60` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-005dfe64"></a> `005dfe64` | `17 08 00 f9` | str x23,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-005dfe68"></a> `005dfe68` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-005dfe6c"></a> `005dfe6c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-005dfe70"></a> `005dfe70` | `15 fc 03 29` | stp w21,wzr,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-005dfe74"></a> `005dfe74` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-005dfe78"></a> `005dfe78` | `68 00 00 b4` | cbz x8,0x005dfe84 | `CONDITIONAL_JUMP`
<a id="insn-005dfe7c"></a> `005dfe7c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-005dfe80"></a> `005dfe80` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-005dfe84"></a> `005dfe84` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-005dfe88"></a> `005dfe88` | `77 e4 f8 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-005dfe8c"></a> `005dfe8c` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-005dfe90"></a> `005dfe90` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-005dfe94"></a> `005dfe94` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-005dfe98"></a> `005dfe98` | `80 82 00 91` | add x0,x20,#0x20 | `FALL_THROUGH`
<a id="insn-005dfe9c"></a> `005dfe9c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-005dfea0"></a> `005dfea0` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-005dfea4"></a> `005dfea4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-005dfea8"></a> `005dfea8` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-005dfeac"></a> `005dfeac` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`005dfdec`](#insn-005dfdec) 範囲 `[['005dfdec', '005dfe03']]`
  - `FALL_THROUGH` [`005dfe00`](#insn-005dfe00) → [`005dfe04`](#insn-005dfe04)
- ブロック [`005dfe04`](#insn-005dfe04) 範囲 `[['005dfe04', '005dfe13']]`
  - `CONDITIONAL_JUMP` [`005dfe10`](#insn-005dfe10) → [`005dfe28`](#insn-005dfe28)
  - `FALL_THROUGH` [`005dfe10`](#insn-005dfe10) → [`005dfe14`](#insn-005dfe14)
- ブロック [`005dfe14`](#insn-005dfe14) 範囲 `[['005dfe14', '005dfe1b']]`
  - `UNCONDITIONAL_JUMP` [`005dfe18`](#insn-005dfe18) → [`005dfe4c`](#insn-005dfe4c)
- ブロック [`005dfe1c`](#insn-005dfe1c) 範囲 `[['005dfe1c', '005dfe27']]`
  - `CONDITIONAL_JUMP` [`005dfe24`](#insn-005dfe24) → [`005dfe4c`](#insn-005dfe4c)
  - `FALL_THROUGH` [`005dfe24`](#insn-005dfe24) → [`005dfe28`](#insn-005dfe28)
- ブロック [`005dfe28`](#insn-005dfe28) 範囲 `[['005dfe28', '005dfe37']]`
  - `CONDITIONAL_JUMP` [`005dfe34`](#insn-005dfe34) → [`005dfe1c`](#insn-005dfe1c)
  - `FALL_THROUGH` [`005dfe34`](#insn-005dfe34) → [`005dfe38`](#insn-005dfe38)
- ブロック [`005dfe38`](#insn-005dfe38) 範囲 `[['005dfe38', '005dfe3f']]`
  - `CONDITIONAL_JUMP` [`005dfe3c`](#insn-005dfe3c) → [`005dfe98`](#insn-005dfe98)
  - `FALL_THROUGH` [`005dfe3c`](#insn-005dfe3c) → [`005dfe40`](#insn-005dfe40)
- ブロック [`005dfe40`](#insn-005dfe40) 範囲 `[['005dfe40', '005dfe47']]`
  - `CONDITIONAL_JUMP` [`005dfe44`](#insn-005dfe44) → [`005dfe28`](#insn-005dfe28)
  - `FALL_THROUGH` [`005dfe44`](#insn-005dfe44) → [`005dfe48`](#insn-005dfe48)
- ブロック [`005dfe48`](#insn-005dfe48) 範囲 `[['005dfe48', '005dfe4b']]`
  - `FALL_THROUGH` [`005dfe48`](#insn-005dfe48) → [`005dfe4c`](#insn-005dfe4c)
- ブロック [`005dfe4c`](#insn-005dfe4c) 範囲 `[['005dfe4c', '005dfe53']]`
  - `FALL_THROUGH` [`005dfe50`](#insn-005dfe50) → [`005dfe54`](#insn-005dfe54)
- ブロック [`005dfe54`](#insn-005dfe54) 範囲 `[['005dfe54', '005dfe5f']]`
  - `FALL_THROUGH` [`005dfe5c`](#insn-005dfe5c) → [`005dfe60`](#insn-005dfe60)
- ブロック [`005dfe60`](#insn-005dfe60) 範囲 `[['005dfe60', '005dfe7b']]`
  - `CONDITIONAL_JUMP` [`005dfe78`](#insn-005dfe78) → [`005dfe84`](#insn-005dfe84)
  - `FALL_THROUGH` [`005dfe78`](#insn-005dfe78) → [`005dfe7c`](#insn-005dfe7c)
- ブロック [`005dfe7c`](#insn-005dfe7c) 範囲 `[['005dfe7c', '005dfe83']]`
  - `FALL_THROUGH` [`005dfe80`](#insn-005dfe80) → [`005dfe84`](#insn-005dfe84)
- ブロック [`005dfe84`](#insn-005dfe84) 範囲 `[['005dfe84', '005dfe97']]`
  - `FALL_THROUGH` [`005dfe94`](#insn-005dfe94) → [`005dfe98`](#insn-005dfe98)
- ブロック [`005dfe98`](#insn-005dfe98) 範囲 `[['005dfe98', '005dfeaf']]`

## 命令位置別の参照

- [`005dfdec`](#insn-005dfdec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdf0`](#insn-005dfdf0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdf4`](#insn-005dfdf4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfdf8`](#insn-005dfdf8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe10`](#insn-005dfe10) → [`005dfe28`](#insn-005dfe28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe18`](#insn-005dfe18) → [`005dfe4c`](#insn-005dfe4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe24`](#insn-005dfe24) → [`005dfe4c`](#insn-005dfe4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe34`](#insn-005dfe34) → [`005dfe1c`](#insn-005dfe1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe3c`](#insn-005dfe3c) → [`005dfe98`](#insn-005dfe98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe44`](#insn-005dfe44) → [`005dfe28`](#insn-005dfe28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe54`](#insn-005dfe54) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`005dfe78`](#insn-005dfe78) → [`005dfe84`](#insn-005dfe84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfe88`](#insn-005dfe88) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`005dfe9c`](#insn-005dfe9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfea0`](#insn-005dfea0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfea4`](#insn-005dfea4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`005dfea8`](#insn-005dfea8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`005dfdec`](#insn-005dfdec)

~~~json
{
  "source": "005dfdec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdf0`](#insn-005dfdf0)

~~~json
{
  "source": "005dfdf0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdf4`](#insn-005dfdf4)

~~~json
{
  "source": "005dfdf4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfdf8`](#insn-005dfdf8)

~~~json
{
  "source": "005dfdf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe10`](#insn-005dfe10)

~~~json
{
  "source": "005dfe10",
  "target": "005dfe28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe18`](#insn-005dfe18)

~~~json
{
  "source": "005dfe18",
  "target": "005dfe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe24`](#insn-005dfe24)

~~~json
{
  "source": "005dfe24",
  "target": "005dfe4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe34`](#insn-005dfe34)

~~~json
{
  "source": "005dfe34",
  "target": "005dfe1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe3c`](#insn-005dfe3c)

~~~json
{
  "source": "005dfe3c",
  "target": "005dfe98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe44`](#insn-005dfe44)

~~~json
{
  "source": "005dfe44",
  "target": "005dfe28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe54`](#insn-005dfe54)

~~~json
{
  "source": "005dfe54",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfe78`](#insn-005dfe78)

~~~json
{
  "source": "005dfe78",
  "target": "005dfe84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfe88`](#insn-005dfe88)

~~~json
{
  "source": "005dfe88",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`005dfe9c`](#insn-005dfe9c)

~~~json
{
  "source": "005dfe9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfea0`](#insn-005dfea0)

~~~json
{
  "source": "005dfea0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfea4`](#insn-005dfea4)

~~~json
{
  "source": "005dfea4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`005dfea8`](#insn-005dfea8)

~~~json
{
  "source": "005dfea8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
