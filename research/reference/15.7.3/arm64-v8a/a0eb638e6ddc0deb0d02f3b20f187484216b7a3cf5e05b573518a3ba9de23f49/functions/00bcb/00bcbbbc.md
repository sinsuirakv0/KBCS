# 00bcbbbc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bcbaf4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcb/00bcbaf4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-5ead316249c4ff943142e91a70242bdd)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bcbc00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcb/00bcbc00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0079.md#compare-8ce073aa81d1f35360106603af9cbc6d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcbbbc",
  "name": "FUN_00bcbbbc",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d2e487028fc3cc3d44501ca44e796d4838245ee2a29fff448a1462119065f7ab",
  "source_text_sha256": "d2e487028fc3cc3d44501ca44e796d4838245ee2a29fff448a1462119065f7ab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcbbbc",
        "00bcbccf"
      ]
    ],
    "bytes_sha256": "fe71669d32e5f5c47e457c65a3d0ab333f5d8cee08c948748a397b7866a8c3e8",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bc8290](../00bc8/00bc8290.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

## 関連文字列（未確認候補）

~~~text
"> typename "
"template<"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1980 bytes

~~~c

void FUN_00bcbbbc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  char *pcVar2;
  undefined4 uVar3;
  undefined8 uVar4;
  void *pvVar5;
  long lVar6;
  size_t sVar7;
  
  lVar6 = param_2[1];
  pvVar5 = (void *)*param_2;
  uVar3 = *(undefined4 *)(param_2 + 4);
  *(undefined4 *)(param_2 + 4) = 0;
  if ((ulong)param_2[2] < lVar6 + 9U) {
    sVar7 = param_2[2] * 2;
    uVar1 = lVar6 + 0x3e9;
                    /* try { // try from 00bcbc00 to 00ccbc0b has its CatchHandler @ 00bcbc68 */
    if (sVar7 < uVar1 || sVar7 - uVar1 == 0) {
      sVar7 = uVar1;
    }
    param_2[2] = sVar7;
    pvVar5 = realloc(pvVar5,sVar7);
                    /* try { // try from 00bcbc0c to 00ccbccf has its CatchHandler @ 00bcb9f8 */
    *param_2 = pvVar5;
    if (pvVar5 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar6 = param_2[1];
  }
  uVar4 = s_template<_002ae62c._0_8_;
  ((char *)((long)pvVar5 + lVar6))[8] = '<';
  *(undefined8 *)((long)pvVar5 + lVar6) = uVar4;
  param_2[1] = param_2[1] + 9;
  FUN_00bc8290(param_1 + 0x18,param_2);
  lVar6 = param_2[1];
  pvVar5 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar6 + 0xbU) {
    sVar7 = param_2[2] * 2;
    uVar1 = lVar6 + 0x3eb;
                    /* catch() { ... } // from try @ 00bcbc00 with catch @ 00bcbc68 */
    if (sVar7 < uVar1 || sVar7 - uVar1 == 0) {
      sVar7 = uVar1;
    }
    param_2[2] = sVar7;
    pvVar5 = realloc(pvVar5,sVar7);
    *param_2 = pvVar5;
    if (pvVar5 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar6 = param_2[1];
  }
                    /* catch() { ... } // from try @ 00bcbad0 with catch @ 00bcbc84 */
  pcVar2 = (char *)((long)pvVar5 + lVar6);
  *(undefined8 *)pcVar2 = s_>_typename_002a02d1._0_8_;
  pcVar2[7] = 'a';
  pcVar2[8] = 'm';
  pcVar2[9] = 'e';
  pcVar2[10] = ' ';
  param_2[1] = param_2[1] + 0xb;
  *(undefined4 *)(param_2 + 4) = uVar3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcbbbc"></a> `00bcbbbc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcbbc0"></a> `00bcbbc0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcbbc4"></a> `00bcbbc4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbbc8"></a> `00bcbbc8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbbcc"></a> `00bcbbcc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcbbd0"></a> `00bcbbd0` | `28 a4 40 a9` | ldp x8,x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbbd4"></a> `00bcbbd4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcbbd8"></a> `00bcbbd8` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00bcbbdc"></a> `00bcbbdc` | `35 20 40 b9` | ldr w21,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbbe0"></a> `00bcbbe0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcbbe4"></a> `00bcbbe4` | `3f 20 00 b9` | str wzr,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbbe8"></a> `00bcbbe8` | `0a 25 00 91` | add x10,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bcbbec"></a> `00bcbbec` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbbf0"></a> `00bcbbf0` | `49 01 00 54` | b.ls 0x00bcbc18 | `CONDITIONAL_JUMP`
<a id="insn-00bcbbf4"></a> `00bcbbf4` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbbf8"></a> `00bcbbf8` | `08 a5 0f 91` | add x8,x8,#0x3e9 | `FALL_THROUGH`
<a id="insn-00bcbbfc"></a> `00bcbbfc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbc00"></a> `00bcbc00` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcbc04"></a> `00bcbc04` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbc08"></a> `00bcbc08` | `7e 45 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc0c"></a> `00bcbc0c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbc10"></a> `00bcbc10` | `c0 05 00 b4` | cbz x0,0x00bcbcc8 | `CONDITIONAL_JUMP`
<a id="insn-00bcbc14"></a> `00bcbc14` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbc18"></a> `00bcbc18` | `09 b7 ff f0` | adrp x9,0x2ae000 | `FALL_THROUGH`
<a id="insn-00bcbc1c"></a> `00bcbc1c` | `29 b1 18 91` | add x9,x9,#0x62c | `FALL_THROUGH`
<a id="insn-00bcbc20"></a> `00bcbc20` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbc24"></a> `00bcbc24` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcbc28"></a> `00bcbc28` | `8a 07 80 52` | mov w10,#0x3c | `FALL_THROUGH`
<a id="insn-00bcbc2c"></a> `00bcbc2c` | `0a 21 00 39` | strb w10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbc30"></a> `00bcbc30` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bcbc34"></a> `00bcbc34` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbc38"></a> `00bcbc38` | `08 25 00 91` | add x8,x8,#0x9 | `FALL_THROUGH`
<a id="insn-00bcbc3c"></a> `00bcbc3c` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbc40"></a> `00bcbc40` | `80 62 00 91` | add x0,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00bcbc44"></a> `00bcbc44` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcbc48"></a> `00bcbc48` | `92 f1 ff 97` | bl 0x00bc8290 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc4c"></a> `00bcbc4c` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbc50"></a> `00bcbc50` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbc54"></a> `00bcbc54` | `0a 2d 00 91` | add x10,x8,#0xb | `FALL_THROUGH`
<a id="insn-00bcbc58"></a> `00bcbc58` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcbc5c"></a> `00bcbc5c` | `49 01 00 54` | b.ls 0x00bcbc84 | `CONDITIONAL_JUMP`
<a id="insn-00bcbc60"></a> `00bcbc60` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcbc64"></a> `00bcbc64` | `08 ad 0f 91` | add x8,x8,#0x3eb | `FALL_THROUGH`
<a id="insn-00bcbc68"></a> `00bcbc68` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcbc6c"></a> `00bcbc6c` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcbc70"></a> `00bcbc70` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbc74"></a> `00bcbc74` | `63 45 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcbc78"></a> `00bcbc78` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcbc7c"></a> `00bcbc7c` | `80 02 00 b4` | cbz x0,0x00bcbccc | `CONDITIONAL_JUMP`
<a id="insn-00bcbc80"></a> `00bcbc80` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbc84"></a> `00bcbc84` | `a9 b6 ff b0` | adrp x9,0x2a0000 | `FALL_THROUGH`
<a id="insn-00bcbc88"></a> `00bcbc88` | `29 45 0b 91` | add x9,x9,#0x2d1 | `FALL_THROUGH`
<a id="insn-00bcbc8c"></a> `00bcbc8c` | `2a ac 8d 52` | mov w10,#0x6d61 | `FALL_THROUGH`
<a id="insn-00bcbc90"></a> `00bcbc90` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00bcbc94"></a> `00bcbc94` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcbc98"></a> `00bcbc98` | `aa 0c a4 72` | movk w10,#0x2065, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcbc9c"></a> `00bcbc9c` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00bcbca0"></a> `00bcbca0` | `0a 71 00 b8` | stur w10,[x8, #0x7] | `FALL_THROUGH`
<a id="insn-00bcbca4"></a> `00bcbca4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbca8"></a> `00bcbca8` | `08 2d 00 91` | add x8,x8,#0xb | `FALL_THROUGH`
<a id="insn-00bcbcac"></a> `00bcbcac` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcbcb0"></a> `00bcbcb0` | `75 22 00 b9` | str w21,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbcb4"></a> `00bcbcb4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcbcb8"></a> `00bcbcb8` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcbcbc"></a> `00bcbcbc` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcbcc0"></a> `00bcbcc0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcbcc4"></a> `00bcbcc4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcbcc8"></a> `00bcbcc8` | `6a 49 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bcbccc"></a> `00bcbccc` | `69 49 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcbbbc`](#insn-00bcbbbc) 範囲 `[['00bcbbbc', '00bcbbf3']]`
  - `CONDITIONAL_JUMP` [`00bcbbf0`](#insn-00bcbbf0) → [`00bcbc18`](#insn-00bcbc18)
  - `FALL_THROUGH` [`00bcbbf0`](#insn-00bcbbf0) → [`00bcbbf4`](#insn-00bcbbf4)
- ブロック [`00bcbbf4`](#insn-00bcbbf4) 範囲 `[['00bcbbf4', '00bcbbff']]`
  - `FALL_THROUGH` [`00bcbbfc`](#insn-00bcbbfc) → [`00bcbc00`](#insn-00bcbc00)
- ブロック [`00bcbc00`](#insn-00bcbc00) 範囲 `[['00bcbc00', '00bcbc0b']]`
  - `FALL_THROUGH` [`00bcbc08`](#insn-00bcbc08) → [`00bcbc0c`](#insn-00bcbc0c)
- ブロック [`00bcbc0c`](#insn-00bcbc0c) 範囲 `[['00bcbc0c', '00bcbc13']]`
  - `CONDITIONAL_JUMP` [`00bcbc10`](#insn-00bcbc10) → [`00bcbcc8`](#insn-00bcbcc8)
  - `FALL_THROUGH` [`00bcbc10`](#insn-00bcbc10) → [`00bcbc14`](#insn-00bcbc14)
- ブロック [`00bcbc14`](#insn-00bcbc14) 範囲 `[['00bcbc14', '00bcbc17']]`
  - `FALL_THROUGH` [`00bcbc14`](#insn-00bcbc14) → [`00bcbc18`](#insn-00bcbc18)
- ブロック [`00bcbc18`](#insn-00bcbc18) 範囲 `[['00bcbc18', '00bcbc5f']]`
  - `CONDITIONAL_JUMP` [`00bcbc5c`](#insn-00bcbc5c) → [`00bcbc84`](#insn-00bcbc84)
  - `FALL_THROUGH` [`00bcbc5c`](#insn-00bcbc5c) → [`00bcbc60`](#insn-00bcbc60)
- ブロック [`00bcbc60`](#insn-00bcbc60) 範囲 `[['00bcbc60', '00bcbc67']]`
  - `FALL_THROUGH` [`00bcbc64`](#insn-00bcbc64) → [`00bcbc68`](#insn-00bcbc68)
- ブロック [`00bcbc68`](#insn-00bcbc68) 範囲 `[['00bcbc68', '00bcbc7f']]`
  - `CONDITIONAL_JUMP` [`00bcbc7c`](#insn-00bcbc7c) → [`00bcbccc`](#insn-00bcbccc)
  - `FALL_THROUGH` [`00bcbc7c`](#insn-00bcbc7c) → [`00bcbc80`](#insn-00bcbc80)
- ブロック [`00bcbc80`](#insn-00bcbc80) 範囲 `[['00bcbc80', '00bcbc83']]`
  - `FALL_THROUGH` [`00bcbc80`](#insn-00bcbc80) → [`00bcbc84`](#insn-00bcbc84)
- ブロック [`00bcbc84`](#insn-00bcbc84) 範囲 `[['00bcbc84', '00bcbcc7']]`
- ブロック [`00bcbcc8`](#insn-00bcbcc8) 範囲 `[['00bcbcc8', '00bcbccb']]`
- ブロック [`00bcbccc`](#insn-00bcbccc) 範囲 `[['00bcbccc', '00bcbccf']]`

## 命令位置別の参照

- [`00bcbbc0`](#insn-00bcbbc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbc4`](#insn-00bcbbc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbc8`](#insn-00bcbbc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbbf0`](#insn-00bcbbf0) → [`00bcbc18`](#insn-00bcbc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc08`](#insn-00bcbc08) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc10`](#insn-00bcbc10) → [`00bcbcc8`](#insn-00bcbcc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc24`](#insn-00bcbc24) → `002ae62c`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbc48`](#insn-00bcbc48) → [`00bc8290`](../00bc8/00bc8290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc8290` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc5c`](#insn-00bcbc5c) → [`00bcbc84`](#insn-00bcbc84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc74`](#insn-00bcbc74) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc7c`](#insn-00bcbc7c) → [`00bcbccc`](#insn-00bcbccc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbc90`](#insn-00bcbc90) → `002a02d1`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcbcb4`](#insn-00bcbcb4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcb8`](#insn-00bcbcb8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcbc`](#insn-00bcbcbc) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcbcc8`](#insn-00bcbcc8) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bcbccc`](#insn-00bcbccc) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcbbc0`](#insn-00bcbbc0)

~~~json
{
  "source": "00bcbbc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbc4`](#insn-00bcbbc4)

~~~json
{
  "source": "00bcbbc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbc8`](#insn-00bcbbc8)

~~~json
{
  "source": "00bcbbc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbbf0`](#insn-00bcbbf0)

~~~json
{
  "source": "00bcbbf0",
  "target": "00bcbc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc08`](#insn-00bcbc08)

~~~json
{
  "source": "00bcbc08",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc10`](#insn-00bcbc10)

~~~json
{
  "source": "00bcbc10",
  "target": "00bcbcc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc24`](#insn-00bcbc24)

~~~json
{
  "source": "00bcbc24",
  "target": "002ae62c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ae62c",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "74656d706c6174653c00",
  "capture_start": "002ae62c",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcbc48`](#insn-00bcbc48)

~~~json
{
  "source": "00bcbc48",
  "target": "00bc8290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc5c`](#insn-00bcbc5c)

~~~json
{
  "source": "00bcbc5c",
  "target": "00bcbc84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc74`](#insn-00bcbc74)

~~~json
{
  "source": "00bcbc74",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbc7c`](#insn-00bcbc7c)

~~~json
{
  "source": "00bcbc7c",
  "target": "00bcbccc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbc90`](#insn-00bcbc90)

~~~json
{
  "source": "00bcbc90",
  "target": "002a02d1",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a02d1",
  "offset": 0,
  "size": 12,
  "datatype": "string",
  "bytes": "3e20747970656e616d652000",
  "capture_start": "002a02d1",
  "capture_bytes": 12,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcbcb4`](#insn-00bcbcb4)

~~~json
{
  "source": "00bcbcb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcb8`](#insn-00bcbcb8)

~~~json
{
  "source": "00bcbcb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcbc`](#insn-00bcbcbc)

~~~json
{
  "source": "00bcbcbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcbcc8`](#insn-00bcbcc8)

~~~json
{
  "source": "00bcbcc8",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcbccc`](#insn-00bcbccc)

~~~json
{
  "source": "00bcbccc",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
