# 00bcdcac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcdd74`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcd/00bcdd74.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-8c3143be155cc5bb08982ea3c6900be1)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdcac",
  "name": "FUN_00bcdcac",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "648125c47e990814163c6a8b21f75669d1484c90757764f0dc06dae32ed57b87",
  "source_text_sha256": "648125c47e990814163c6a8b21f75669d1484c90757764f0dc06dae32ed57b87",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdcac",
        "00bcddc7"
      ]
    ],
    "bytes_sha256": "bf5f06dca8eba5aeaa763cca9c24188f77de79a0d8e4217e946cf6ce26b65e24",
    "instruction_count": 71,
    "instruction_bytes": 284,
    "body_bytes": 284,
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
" requires "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1856 bytes

~~~c

void FUN_00bcdcac(long param_1,undefined8 *param_2)

{
  char *pcVar1;
  undefined8 uVar2;
  void *pvVar3;
  long lVar4;
  ulong uVar5;
  size_t sVar6;
  long *plVar7;
  
  lVar4 = param_2[1];
  pvVar3 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar4 + 10U) {
    sVar6 = param_2[2] * 2;
    uVar5 = lVar4 + 0x3ea;
    if (sVar6 < uVar5 || sVar6 - uVar5 == 0) {
      sVar6 = uVar5;
    }
    param_2[2] = sVar6;
    pvVar3 = realloc(pvVar3,sVar6);
                    /* catch() { ... } // from try @ 00bce050 with catch @ 00bcdcf4
                       catch() { ... } // from try @ 00bce148 with catch @ 00bcdcf4 */
    *param_2 = pvVar3;
    if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar4 = param_2[1];
  }
  uVar2 = s_requires_002af880._0_8_;
  pcVar1 = (char *)((long)pvVar3 + lVar4);
  pcVar1[8] = 's';
  pcVar1[9] = ' ';
  *(undefined8 *)pcVar1 = uVar2;
  plVar7 = *(long **)(param_1 + 0x10);
  lVar4 = *plVar7;
  param_2[1] = param_2[1] + 10;
  (**(code **)(lVar4 + 0x20))(plVar7,param_2);
  if ((*(ushort *)((long)plVar7 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar7 + 0x28))(plVar7,param_2);
  }
  lVar4 = param_2[1];
  pvVar3 = (void *)*param_2;
  uVar5 = lVar4 + 1;
  if ((ulong)param_2[2] < uVar5) {
    sVar6 = param_2[2] * 2;
    uVar5 = lVar4 + 0x3e1;
    if (sVar6 < uVar5 || sVar6 - uVar5 == 0) {
      sVar6 = uVar5;
    }
    param_2[2] = sVar6;
    pvVar3 = realloc(pvVar3,sVar6);
    *param_2 = pvVar3;
    if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar4 = param_2[1];
    uVar5 = lVar4 + 1;
  }
                    /* try { // try from 00bcdda4 to 00ccddbf has its CatchHandler @ 00bce480 */
  param_2[1] = uVar5;
  *(undefined1 *)((long)pvVar3 + lVar4) = 0x3b;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdcac"></a> `00bcdcac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcdcb0"></a> `00bcdcb0` | `fd 7b be a9` | stp x29,x30,[sp, #-0x20]! | `FALL_THROUGH`
<a id="insn-00bcdcb4"></a> `00bcdcb4` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdcb8"></a> `00bcdcb8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcdcbc"></a> `00bcdcbc` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdcc0"></a> `00bcdcc0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcdcc4"></a> `00bcdcc4` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcdcc8"></a> `00bcdcc8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcdccc"></a> `00bcdccc` | `2b 29 00 91` | add x11,x9,#0xa | `FALL_THROUGH`
<a id="insn-00bcdcd0"></a> `00bcdcd0` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcdcd4"></a> `00bcdcd4` | `89 01 00 54` | b.ls 0x00bcdd04 | `CONDITIONAL_JUMP`
<a id="insn-00bcdcd8"></a> `00bcdcd8` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdcdc"></a> `00bcdcdc` | `29 a9 0f 91` | add x9,x9,#0x3ea | `FALL_THROUGH`
<a id="insn-00bcdce0"></a> `00bcdce0` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcdce4"></a> `00bcdce4` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcdce8"></a> `00bcdce8` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bcdcec"></a> `00bcdcec` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdcf0"></a> `00bcdcf0` | `18 3d 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdcf4"></a> `00bcdcf4` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdcf8"></a> `00bcdcf8` | `40 06 00 b4` | cbz x0,0x00bcddc0 | `CONDITIONAL_JUMP`
<a id="insn-00bcdcfc"></a> `00bcdcfc` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdd00"></a> `00bcdd00` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcdd04"></a> `00bcdd04` | `0a b7 ff d0` | adrp x10,0x2af000 | `FALL_THROUGH`
<a id="insn-00bcdd08"></a> `00bcdd08` | `4a 01 22 91` | add x10,x10,#0x880 | `FALL_THROUGH`
<a id="insn-00bcdd0c"></a> `00bcdd0c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bcdd10"></a> `00bcdd10` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-00bcdd14"></a> `00bcdd14` | `69 0e 84 52` | mov w9,#0x2073 | `FALL_THROUGH`
<a id="insn-00bcdd18"></a> `00bcdd18` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcdd1c"></a> `00bcdd1c` | `09 11 00 79` | strh w9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdd20"></a> `00bcdd20` | `0a 01 00 f9` | str x10,[x8] | `FALL_THROUGH`
<a id="insn-00bcdd24"></a> `00bcdd24` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdd28"></a> `00bcdd28` | `94 0a 40 f9` | ldr x20,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdd2c"></a> `00bcdd2c` | `08 29 00 91` | add x8,x8,#0xa | `FALL_THROUGH`
<a id="insn-00bcdd30"></a> `00bcdd30` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bcdd34"></a> `00bcdd34` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdd38"></a> `00bcdd38` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdd3c"></a> `00bcdd3c` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdd40"></a> `00bcdd40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdd44"></a> `00bcdd44` | `88 92 40 78` | ldurh w8,[x20, #0x9] | `FALL_THROUGH`
<a id="insn-00bcdd48"></a> `00bcdd48` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcdd4c"></a> `00bcdd4c` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcdd50"></a> `00bcdd50` | `c0 00 00 54` | b.eq 0x00bcdd68 | `CONDITIONAL_JUMP`
<a id="insn-00bcdd54"></a> `00bcdd54` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcdd58"></a> `00bcdd58` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdd5c"></a> `00bcdd5c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcdd60"></a> `00bcdd60` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdd64"></a> `00bcdd64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdd68"></a> `00bcdd68` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdd6c"></a> `00bcdd6c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdd70"></a> `00bcdd70` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdd74"></a> `00bcdd74` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcdd78"></a> `00bcdd78` | `69 01 00 54` | b.ls 0x00bcdda4 | `CONDITIONAL_JUMP`
<a id="insn-00bcdd7c"></a> `00bcdd7c` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdd80"></a> `00bcdd80` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcdd84"></a> `00bcdd84` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcdd88"></a> `00bcdd88` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcdd8c"></a> `00bcdd8c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdd90"></a> `00bcdd90` | `f0 3c 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd94"></a> `00bcdd94` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcdd98"></a> `00bcdd98` | `60 01 00 b4` | cbz x0,0x00bcddc4 | `CONDITIONAL_JUMP`
<a id="insn-00bcdd9c"></a> `00bcdd9c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdda0"></a> `00bcdda0` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdda4"></a> `00bcdda4` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdda8"></a> `00bcdda8` | `69 07 80 52` | mov w9,#0x3b | `FALL_THROUGH`
<a id="insn-00bcddac"></a> `00bcddac` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcddb0"></a> `00bcddb0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcddb4"></a> `00bcddb4` | `fd 7b c2 a8` | ldp x29,x30,[sp], #0x20 | `FALL_THROUGH`
<a id="insn-00bcddb8"></a> `00bcddb8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcddbc"></a> `00bcddbc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcddc0"></a> `00bcddc0` | `00 41 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bcddc4"></a> `00bcddc4` | `ff 40 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdcac`](#insn-00bcdcac) 範囲 `[['00bcdcac', '00bcdcd7']]`
  - `CONDITIONAL_JUMP` [`00bcdcd4`](#insn-00bcdcd4) → [`00bcdd04`](#insn-00bcdd04)
  - `FALL_THROUGH` [`00bcdcd4`](#insn-00bcdcd4) → [`00bcdcd8`](#insn-00bcdcd8)
- ブロック [`00bcdcd8`](#insn-00bcdcd8) 範囲 `[['00bcdcd8', '00bcdcf3']]`
  - `FALL_THROUGH` [`00bcdcf0`](#insn-00bcdcf0) → [`00bcdcf4`](#insn-00bcdcf4)
- ブロック [`00bcdcf4`](#insn-00bcdcf4) 範囲 `[['00bcdcf4', '00bcdcfb']]`
  - `CONDITIONAL_JUMP` [`00bcdcf8`](#insn-00bcdcf8) → [`00bcddc0`](#insn-00bcddc0)
  - `FALL_THROUGH` [`00bcdcf8`](#insn-00bcdcf8) → [`00bcdcfc`](#insn-00bcdcfc)
- ブロック [`00bcdcfc`](#insn-00bcdcfc) 範囲 `[['00bcdcfc', '00bcdd03']]`
  - `FALL_THROUGH` [`00bcdd00`](#insn-00bcdd00) → [`00bcdd04`](#insn-00bcdd04)
- ブロック [`00bcdd04`](#insn-00bcdd04) 範囲 `[['00bcdd04', '00bcdd53']]`
  - `CONDITIONAL_JUMP` [`00bcdd50`](#insn-00bcdd50) → [`00bcdd68`](#insn-00bcdd68)
  - `FALL_THROUGH` [`00bcdd50`](#insn-00bcdd50) → [`00bcdd54`](#insn-00bcdd54)
- ブロック [`00bcdd54`](#insn-00bcdd54) 範囲 `[['00bcdd54', '00bcdd67']]`
  - `FALL_THROUGH` [`00bcdd64`](#insn-00bcdd64) → [`00bcdd68`](#insn-00bcdd68)
- ブロック [`00bcdd68`](#insn-00bcdd68) 範囲 `[['00bcdd68', '00bcdd7b']]`
  - `CONDITIONAL_JUMP` [`00bcdd78`](#insn-00bcdd78) → [`00bcdda4`](#insn-00bcdda4)
  - `FALL_THROUGH` [`00bcdd78`](#insn-00bcdd78) → [`00bcdd7c`](#insn-00bcdd7c)
- ブロック [`00bcdd7c`](#insn-00bcdd7c) 範囲 `[['00bcdd7c', '00bcdd9b']]`
  - `CONDITIONAL_JUMP` [`00bcdd98`](#insn-00bcdd98) → [`00bcddc4`](#insn-00bcddc4)
  - `FALL_THROUGH` [`00bcdd98`](#insn-00bcdd98) → [`00bcdd9c`](#insn-00bcdd9c)
- ブロック [`00bcdd9c`](#insn-00bcdd9c) 範囲 `[['00bcdd9c', '00bcdda3']]`
  - `FALL_THROUGH` [`00bcdda0`](#insn-00bcdda0) → [`00bcdda4`](#insn-00bcdda4)
- ブロック [`00bcdda4`](#insn-00bcdda4) 範囲 `[['00bcdda4', '00bcddbf']]`
- ブロック [`00bcddc0`](#insn-00bcddc0) 範囲 `[['00bcddc0', '00bcddc3']]`
- ブロック [`00bcddc4`](#insn-00bcddc4) 範囲 `[['00bcddc4', '00bcddc7']]`

## 命令位置別の参照

- [`00bcdcb0`](#insn-00bcdcb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcb4`](#insn-00bcdcb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcd4`](#insn-00bcdcd4) → [`00bcdd04`](#insn-00bcdd04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcf0`](#insn-00bcdcf0) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcf8`](#insn-00bcdcf8) → [`00bcddc0`](#insn-00bcddc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd10`](#insn-00bcdd10) → `002af880`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcdd50`](#insn-00bcdd50) → [`00bcdd68`](#insn-00bcdd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd78`](#insn-00bcdd78) → [`00bcdda4`](#insn-00bcdda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd90`](#insn-00bcdd90) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd98`](#insn-00bcdd98) → [`00bcddc4`](#insn-00bcddc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddb0`](#insn-00bcddb0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddb4`](#insn-00bcddb4) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddc0`](#insn-00bcddc0) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcddc4`](#insn-00bcddc4) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdcb0`](#insn-00bcdcb0)

~~~json
{
  "source": "00bcdcb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdcb4`](#insn-00bcdcb4)

~~~json
{
  "source": "00bcdcb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdcd4`](#insn-00bcdcd4)

~~~json
{
  "source": "00bcdcd4",
  "target": "00bcdd04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdcf0`](#insn-00bcdcf0)

~~~json
{
  "source": "00bcdcf0",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcf8`](#insn-00bcdcf8)

~~~json
{
  "source": "00bcdcf8",
  "target": "00bcddc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd10`](#insn-00bcdd10)

~~~json
{
  "source": "00bcdd10",
  "target": "002af880",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002af880",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "2072657175697265732000",
  "capture_start": "002af880",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcdd50`](#insn-00bcdd50)

~~~json
{
  "source": "00bcdd50",
  "target": "00bcdd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd78`](#insn-00bcdd78)

~~~json
{
  "source": "00bcdd78",
  "target": "00bcdda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd90`](#insn-00bcdd90)

~~~json
{
  "source": "00bcdd90",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd98`](#insn-00bcdd98)

~~~json
{
  "source": "00bcdd98",
  "target": "00bcddc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddb0`](#insn-00bcddb0)

~~~json
{
  "source": "00bcddb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddb4`](#insn-00bcddb4)

~~~json
{
  "source": "00bcddb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddc0`](#insn-00bcddc0)

~~~json
{
  "source": "00bcddc0",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcddc4`](#insn-00bcddc4)

~~~json
{
  "source": "00bcddc4",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
