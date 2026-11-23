# 00adf9fc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00adf934`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00adf/00adf934.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-9e7fef9a423e72c5ba910bdd58bf707e)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00adfa40`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00adf/00adfa40.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-93250923e018157d30ec7c57e91d5f6e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00adf9fc",
  "name": "FUN_00adf9fc",
  "size": 284,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "04dcc758f7687751d0ece695b02abd7fd04f201fc81bd29e73a4077730969695",
  "source_text_sha256": "04dcc758f7687751d0ece695b02abd7fd04f201fc81bd29e73a4077730969695",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00adf9fc",
        "00adfb17"
      ]
    ],
    "bytes_sha256": "fe41f379db040bb40a809ec70ec40ac0ca1d46243a5d3dc35cb80b173c297983",
    "instruction_count": 71,
    "instruction_bytes": 284,
    "body_bytes": 284,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00419064](../00419/00419064.md)
- [00457e1c](../00457/00457e1c.md)
- [00459efc](../00459/00459efc.md)
- [0081f580](../0081f/0081f580.md)
- [00885f80](../00885/00885f80.md)
- [00add7d4](../00add/00add7d4.md)
- [00bdaff0](../00bda/00bdaff0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2744 bytes

~~~c

void FUN_00adf9fc(undefined8 param_1,undefined8 *param_2,int *param_3)

{
  int iVar1;
  undefined8 uVar2;
  long lVar3;
  long lVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  long *plVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  
                    /* try { // try from 00adf9fc to 00bdfa1b has its CatchHandler @ 00adfc58 */
  if (*param_3 == 5) {
                    /* try { // try from 00adfa4c to 00bdfa53 has its CatchHandler @ 00adfc38 */
    lVar3 = FUN_0081f580();
    lVar4 = FUN_0081f580();
    iVar1 = *(int *)(lVar4 + 0x2290);
    puVar6 = *(undefined8 **)(lVar3 + 0x2280);
    if (*(undefined8 **)(lVar3 + 0x2280) == (undefined8 *)0x0) {
                    /* try { // try from 00adfa68 to 00bdfa6b has its CatchHandler @ 00adfc44 */
      puVar8 = (undefined8 *)(lVar3 + 0x2280);
      puVar9 = (undefined8 *)(lVar3 + 0x2280);
    }
    else {
      do {
        while( true ) {
                    /* try { // try from 00adfa80 to 00bdfa87 has its CatchHandler @ 00adfc30 */
          puVar5 = puVar6;
          puVar8 = puVar5;
          if (iVar1 < *(int *)((long)puVar5 + 0x1c)) break;
          if (iVar1 <= *(int *)((long)puVar5 + 0x1c)) goto LAB_00adfaf0;
                    /* try { // try from 00adfa98 to 00bdfa9f has its CatchHandler @ 00adfc14 */
          puVar6 = (undefined8 *)puVar5[1];
          if ((undefined8 *)puVar5[1] == (undefined8 *)0x0) {
            puVar9 = puVar5 + 1;
            goto LAB_00adfaa4;
          }
        }
        puVar6 = (undefined8 *)*puVar5;
        puVar9 = puVar5;
      } while ((undefined8 *)*puVar5 != (undefined8 *)0x0);
    }
LAB_00adfaa4:
    puVar5 = (undefined8 *)_Znwm(0x70);
    *puVar5 = 0;
    puVar5[1] = 0;
                    /* try { // try from 00adfab4 to 00bdfabb has its CatchHandler @ 00adfc0c */
    puVar5[2] = puVar8;
    *puVar9 = puVar5;
    plVar7 = *(long **)(lVar3 + 0x2278);
    *(int *)((long)puVar5 + 0x1c) = iVar1;
                    /* try { // try from 00adfad0 to 00bdfad7 has its CatchHandler @ 00adfc30 */
    puVar6 = puVar5;
    if (*plVar7 != 0) {
      *(long *)(lVar3 + 0x2278) = *plVar7;
      puVar6 = (undefined8 *)*puVar9;
    }
    FUN_00419064(*(undefined8 *)(lVar3 + 0x2280),puVar6);
                    /* try { // try from 00adfaec to 00bdfb0b has its CatchHandler @ 00adfc0c */
    *(long *)(lVar3 + 0x2288) = *(long *)(lVar3 + 0x2288) + 1;
LAB_00adfaf0:
    FUN_00add7d4(puVar5 + 4);
    lVar3 = FUN_0081f580();
    *(undefined4 *)(lVar3 + 0x2290) = 0xffffffff;
  }
  else if (*param_3 == 2) {
    FUN_00885f80(*param_2);
    uVar2 = FUN_00457e1c();
                    /* try { // try from 00adfa30 to 00bdfa37 has its CatchHandler @ 00adfc44 */
    FUN_00459efc(uVar2,0xb,0);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00adf9fc"></a> `00adf9fc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00adfa00"></a> `00adfa00` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfa04"></a> `00adfa04` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adfa08"></a> `00adfa08` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfa0c"></a> `00adfa0c` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00adfa10"></a> `00adfa10` | `48 00 40 b9` | ldr w8,[x2] | `FALL_THROUGH`
<a id="insn-00adfa14"></a> `00adfa14` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00adfa18"></a> `00adfa18` | `a0 01 00 54` | b.eq 0x00adfa4c | `CONDITIONAL_JUMP`
<a id="insn-00adfa1c"></a> `00adfa1c` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00adfa20"></a> `00adfa20` | `21 07 00 54` | b.ne 0x00adfb04 | `CONDITIONAL_JUMP`
<a id="insn-00adfa24"></a> `00adfa24` | `20 00 40 f9` | ldr x0,[x1] | `FALL_THROUGH`
<a id="insn-00adfa28"></a> `00adfa28` | `56 99 f6 97` | bl 0x00885f80 | `UNCONDITIONAL_CALL`
<a id="insn-00adfa2c"></a> `00adfa2c` | `fc e0 e5 97` | bl 0x00457e1c | `UNCONDITIONAL_CALL`
<a id="insn-00adfa30"></a> `00adfa30` | `61 01 80 52` | mov w1,#0xb | `FALL_THROUGH`
<a id="insn-00adfa34"></a> `00adfa34` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00adfa38"></a> `00adfa38` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfa3c"></a> `00adfa3c` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfa40"></a> `00adfa40` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adfa44"></a> `00adfa44` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00adfa48"></a> `00adfa48` | `2d e9 e5 17` | b 0x00459efc | `CALL_TERMINATOR`
<a id="insn-00adfa4c"></a> `00adfa4c` | `cd fe f4 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00adfa50"></a> `00adfa50` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00adfa54"></a> `00adfa54` | `cb fe f4 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00adfa58"></a> `00adfa58` | `68 42 51 f9` | ldr x8,[x19, #0x2280] | `FALL_THROUGH`
<a id="insn-00adfa5c"></a> `00adfa5c` | `15 90 62 b9` | ldr w21,[x0, #0x2290] | `FALL_THROUGH`
<a id="insn-00adfa60"></a> `00adfa60` | `08 01 00 b5` | cbnz x8,0x00adfa80 | `CONDITIONAL_JUMP`
<a id="insn-00adfa64"></a> `00adfa64` | `08 50 84 52` | mov w8,#0x2280 | `FALL_THROUGH`
<a id="insn-00adfa68"></a> `00adfa68` | `76 02 08 8b` | add x22,x19,x8 | `FALL_THROUGH`
<a id="insn-00adfa6c"></a> `00adfa6c` | `f4 03 16 aa` | mov x20,x22 | `FALL_THROUGH`
<a id="insn-00adfa70"></a> `00adfa70` | `0d 00 00 14` | b 0x00adfaa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00adfa74"></a> `00adfa74` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00adfa78"></a> `00adfa78` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00adfa7c"></a> `00adfa7c` | `48 01 00 b4` | cbz x8,0x00adfaa4 | `CONDITIONAL_JUMP`
<a id="insn-00adfa80"></a> `00adfa80` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00adfa84"></a> `00adfa84` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00adfa88"></a> `00adfa88` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00adfa8c"></a> `00adfa8c` | `4b ff ff 54` | b.lt 0x00adfa74 | `CONDITIONAL_JUMP`
<a id="insn-00adfa90"></a> `00adfa90` | `1f 01 15 6b` | cmp w8,w21 | `FALL_THROUGH`
<a id="insn-00adfa94"></a> `00adfa94` | `ea 02 00 54` | b.ge 0x00adfaf0 | `CONDITIONAL_JUMP`
<a id="insn-00adfa98"></a> `00adfa98` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00adfa9c"></a> `00adfa9c` | `28 ff ff b5` | cbnz x8,0x00adfa80 | `CONDITIONAL_JUMP`
<a id="insn-00adfaa0"></a> `00adfaa0` | `96 22 00 91` | add x22,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00adfaa4"></a> `00adfaa4` | `00 0e 80 52` | mov w0,#0x70 | `FALL_THROUGH`
<a id="insn-00adfaa8"></a> `00adfaa8` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-00adfaac"></a> `00adfaac` | `51 ed 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00adfab0"></a> `00adfab0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00adfab4"></a> `00adfab4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00adfab8"></a> `00adfab8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00adfabc"></a> `00adfabc` | `17 08 00 f9` | str x23,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00adfac0"></a> `00adfac0` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00adfac4"></a> `00adfac4` | `68 3e 51 f9` | ldr x8,[x19, #0x2278] | `FALL_THROUGH`
<a id="insn-00adfac8"></a> `00adfac8` | `15 1c 00 b9` | str w21,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00adfacc"></a> `00adfacc` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00adfad0"></a> `00adfad0` | `68 00 00 b4` | cbz x8,0x00adfadc | `CONDITIONAL_JUMP`
<a id="insn-00adfad4"></a> `00adfad4` | `68 3e 11 f9` | str x8,[x19, #0x2278] | `FALL_THROUGH`
<a id="insn-00adfad8"></a> `00adfad8` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00adfadc"></a> `00adfadc` | `60 42 51 f9` | ldr x0,[x19, #0x2280] | `FALL_THROUGH`
<a id="insn-00adfae0"></a> `00adfae0` | `61 e5 e4 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00adfae4"></a> `00adfae4` | `68 46 51 f9` | ldr x8,[x19, #0x2288] | `FALL_THROUGH`
<a id="insn-00adfae8"></a> `00adfae8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00adfaec"></a> `00adfaec` | `68 46 11 f9` | str x8,[x19, #0x2288] | `FALL_THROUGH`
<a id="insn-00adfaf0"></a> `00adfaf0` | `80 82 00 91` | add x0,x20,#0x20 | `FALL_THROUGH`
<a id="insn-00adfaf4"></a> `00adfaf4` | `38 f7 ff 97` | bl 0x00add7d4 | `UNCONDITIONAL_CALL`
<a id="insn-00adfaf8"></a> `00adfaf8` | `a2 fe f4 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00adfafc"></a> `00adfafc` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-00adfb00"></a> `00adfb00` | `08 90 22 b9` | str w8,[x0, #0x2290] | `FALL_THROUGH`
<a id="insn-00adfb04"></a> `00adfb04` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00adfb08"></a> `00adfb08` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00adfb0c"></a> `00adfb0c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00adfb10"></a> `00adfb10` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00adfb14"></a> `00adfb14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00adf9fc`](#insn-00adf9fc) 範囲 `[['00adf9fc', '00adfa1b']]`
  - `CONDITIONAL_JUMP` [`00adfa18`](#insn-00adfa18) → [`00adfa4c`](#insn-00adfa4c)
  - `FALL_THROUGH` [`00adfa18`](#insn-00adfa18) → [`00adfa1c`](#insn-00adfa1c)
- ブロック [`00adfa1c`](#insn-00adfa1c) 範囲 `[['00adfa1c', '00adfa23']]`
  - `CONDITIONAL_JUMP` [`00adfa20`](#insn-00adfa20) → [`00adfb04`](#insn-00adfb04)
  - `FALL_THROUGH` [`00adfa20`](#insn-00adfa20) → [`00adfa24`](#insn-00adfa24)
- ブロック [`00adfa24`](#insn-00adfa24) 範囲 `[['00adfa24', '00adfa2f']]`
  - `FALL_THROUGH` [`00adfa2c`](#insn-00adfa2c) → [`00adfa30`](#insn-00adfa30)
- ブロック [`00adfa30`](#insn-00adfa30) 範囲 `[['00adfa30', '00adfa4b']]`
- ブロック [`00adfa4c`](#insn-00adfa4c) 範囲 `[['00adfa4c', '00adfa63']]`
  - `CONDITIONAL_JUMP` [`00adfa60`](#insn-00adfa60) → [`00adfa80`](#insn-00adfa80)
  - `FALL_THROUGH` [`00adfa60`](#insn-00adfa60) → [`00adfa64`](#insn-00adfa64)
- ブロック [`00adfa64`](#insn-00adfa64) 範囲 `[['00adfa64', '00adfa67']]`
  - `FALL_THROUGH` [`00adfa64`](#insn-00adfa64) → [`00adfa68`](#insn-00adfa68)
- ブロック [`00adfa68`](#insn-00adfa68) 範囲 `[['00adfa68', '00adfa73']]`
  - `UNCONDITIONAL_JUMP` [`00adfa70`](#insn-00adfa70) → [`00adfaa4`](#insn-00adfaa4)
- ブロック [`00adfa74`](#insn-00adfa74) 範囲 `[['00adfa74', '00adfa7f']]`
  - `CONDITIONAL_JUMP` [`00adfa7c`](#insn-00adfa7c) → [`00adfaa4`](#insn-00adfaa4)
  - `FALL_THROUGH` [`00adfa7c`](#insn-00adfa7c) → [`00adfa80`](#insn-00adfa80)
- ブロック [`00adfa80`](#insn-00adfa80) 範囲 `[['00adfa80', '00adfa8f']]`
  - `CONDITIONAL_JUMP` [`00adfa8c`](#insn-00adfa8c) → [`00adfa74`](#insn-00adfa74)
  - `FALL_THROUGH` [`00adfa8c`](#insn-00adfa8c) → [`00adfa90`](#insn-00adfa90)
- ブロック [`00adfa90`](#insn-00adfa90) 範囲 `[['00adfa90', '00adfa97']]`
  - `CONDITIONAL_JUMP` [`00adfa94`](#insn-00adfa94) → [`00adfaf0`](#insn-00adfaf0)
  - `FALL_THROUGH` [`00adfa94`](#insn-00adfa94) → [`00adfa98`](#insn-00adfa98)
- ブロック [`00adfa98`](#insn-00adfa98) 範囲 `[['00adfa98', '00adfa9f']]`
  - `CONDITIONAL_JUMP` [`00adfa9c`](#insn-00adfa9c) → [`00adfa80`](#insn-00adfa80)
  - `FALL_THROUGH` [`00adfa9c`](#insn-00adfa9c) → [`00adfaa0`](#insn-00adfaa0)
- ブロック [`00adfaa0`](#insn-00adfaa0) 範囲 `[['00adfaa0', '00adfaa3']]`
  - `FALL_THROUGH` [`00adfaa0`](#insn-00adfaa0) → [`00adfaa4`](#insn-00adfaa4)
- ブロック [`00adfaa4`](#insn-00adfaa4) 範囲 `[['00adfaa4', '00adfab3']]`
  - `FALL_THROUGH` [`00adfab0`](#insn-00adfab0) → [`00adfab4`](#insn-00adfab4)
- ブロック [`00adfab4`](#insn-00adfab4) 範囲 `[['00adfab4', '00adfacf']]`
  - `FALL_THROUGH` [`00adfacc`](#insn-00adfacc) → [`00adfad0`](#insn-00adfad0)
- ブロック [`00adfad0`](#insn-00adfad0) 範囲 `[['00adfad0', '00adfad3']]`
  - `CONDITIONAL_JUMP` [`00adfad0`](#insn-00adfad0) → [`00adfadc`](#insn-00adfadc)
  - `FALL_THROUGH` [`00adfad0`](#insn-00adfad0) → [`00adfad4`](#insn-00adfad4)
- ブロック [`00adfad4`](#insn-00adfad4) 範囲 `[['00adfad4', '00adfadb']]`
  - `FALL_THROUGH` [`00adfad8`](#insn-00adfad8) → [`00adfadc`](#insn-00adfadc)
- ブロック [`00adfadc`](#insn-00adfadc) 範囲 `[['00adfadc', '00adfaeb']]`
  - `FALL_THROUGH` [`00adfae8`](#insn-00adfae8) → [`00adfaec`](#insn-00adfaec)
- ブロック [`00adfaec`](#insn-00adfaec) 範囲 `[['00adfaec', '00adfaef']]`
  - `FALL_THROUGH` [`00adfaec`](#insn-00adfaec) → [`00adfaf0`](#insn-00adfaf0)
- ブロック [`00adfaf0`](#insn-00adfaf0) 範囲 `[['00adfaf0', '00adfb03']]`
  - `FALL_THROUGH` [`00adfb00`](#insn-00adfb00) → [`00adfb04`](#insn-00adfb04)
- ブロック [`00adfb04`](#insn-00adfb04) 範囲 `[['00adfb04', '00adfb17']]`

## 命令位置別の参照

- [`00adf9fc`](#insn-00adf9fc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa00`](#insn-00adfa00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa04`](#insn-00adfa04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa08`](#insn-00adfa08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa18`](#insn-00adfa18) → [`00adfa4c`](#insn-00adfa4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa20`](#insn-00adfa20) → [`00adfb04`](#insn-00adfb04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa28`](#insn-00adfa28) → [`00885f80`](../00885/00885f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00885f80` · 推定シンボル `None` · 推定型 `None`
- [`00adfa2c`](#insn-00adfa2c) → [`00457e1c`](../00457/00457e1c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00457e1c` · 推定シンボル `None` · 推定型 `None`
- [`00adfa38`](#insn-00adfa38) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa3c`](#insn-00adfa3c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa40`](#insn-00adfa40) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa44`](#insn-00adfa44) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa48`](#insn-00adfa48) → [`00459efc`](../00459/00459efc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459efc` · 推定シンボル `None` · 推定型 `None`
- [`00adfa4c`](#insn-00adfa4c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00adfa54`](#insn-00adfa54) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00adfa60`](#insn-00adfa60) → [`00adfa80`](#insn-00adfa80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa70`](#insn-00adfa70) → [`00adfaa4`](#insn-00adfaa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa7c`](#insn-00adfa7c) → [`00adfaa4`](#insn-00adfaa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa8c`](#insn-00adfa8c) → [`00adfa74`](#insn-00adfa74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa94`](#insn-00adfa94) → [`00adfaf0`](#insn-00adfaf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfa9c`](#insn-00adfa9c) → [`00adfa80`](#insn-00adfa80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfaac`](#insn-00adfaac) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00adfad0`](#insn-00adfad0) → [`00adfadc`](#insn-00adfadc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfae0`](#insn-00adfae0) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00adfaf4`](#insn-00adfaf4) → [`00add7d4`](../00add/00add7d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00add7d4` · 推定シンボル `None` · 推定型 `None`
- [`00adfaf8`](#insn-00adfaf8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00adfb04`](#insn-00adfb04) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfb08`](#insn-00adfb08) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfb0c`](#insn-00adfb0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00adfb10`](#insn-00adfb10) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00adf9fc`](#insn-00adf9fc)

~~~json
{
  "source": "00adf9fc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa00`](#insn-00adfa00)

~~~json
{
  "source": "00adfa00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa04`](#insn-00adfa04)

~~~json
{
  "source": "00adfa04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa08`](#insn-00adfa08)

~~~json
{
  "source": "00adfa08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa18`](#insn-00adfa18)

~~~json
{
  "source": "00adfa18",
  "target": "00adfa4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa20`](#insn-00adfa20)

~~~json
{
  "source": "00adfa20",
  "target": "00adfb04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa28`](#insn-00adfa28)

~~~json
{
  "source": "00adfa28",
  "target": "00885f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfa2c`](#insn-00adfa2c)

~~~json
{
  "source": "00adfa2c",
  "target": "00457e1c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfa38`](#insn-00adfa38)

~~~json
{
  "source": "00adfa38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa3c`](#insn-00adfa3c)

~~~json
{
  "source": "00adfa3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa40`](#insn-00adfa40)

~~~json
{
  "source": "00adfa40",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa44`](#insn-00adfa44)

~~~json
{
  "source": "00adfa44",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa48`](#insn-00adfa48)

~~~json
{
  "source": "00adfa48",
  "target": "00459efc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfa4c`](#insn-00adfa4c)

~~~json
{
  "source": "00adfa4c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfa54`](#insn-00adfa54)

~~~json
{
  "source": "00adfa54",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfa60`](#insn-00adfa60)

~~~json
{
  "source": "00adfa60",
  "target": "00adfa80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa70`](#insn-00adfa70)

~~~json
{
  "source": "00adfa70",
  "target": "00adfaa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa7c`](#insn-00adfa7c)

~~~json
{
  "source": "00adfa7c",
  "target": "00adfaa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa8c`](#insn-00adfa8c)

~~~json
{
  "source": "00adfa8c",
  "target": "00adfa74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa94`](#insn-00adfa94)

~~~json
{
  "source": "00adfa94",
  "target": "00adfaf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfa9c`](#insn-00adfa9c)

~~~json
{
  "source": "00adfa9c",
  "target": "00adfa80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfaac`](#insn-00adfaac)

~~~json
{
  "source": "00adfaac",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfad0`](#insn-00adfad0)

~~~json
{
  "source": "00adfad0",
  "target": "00adfadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfae0`](#insn-00adfae0)

~~~json
{
  "source": "00adfae0",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfaf4`](#insn-00adfaf4)

~~~json
{
  "source": "00adfaf4",
  "target": "00add7d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfaf8`](#insn-00adfaf8)

~~~json
{
  "source": "00adfaf8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00adfb04`](#insn-00adfb04)

~~~json
{
  "source": "00adfb04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfb08`](#insn-00adfb08)

~~~json
{
  "source": "00adfb08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfb0c`](#insn-00adfb0c)

~~~json
{
  "source": "00adfb0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00adfb10`](#insn-00adfb10)

~~~json
{
  "source": "00adfb10",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
