# 00bcda8c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5e58c`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e58c.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-b90181b5ee744e92b5eb295a0e2a5f8c)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcdeb4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcdeb4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-87739202910b90951405e2749b1fed9f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcda8c",
  "name": "FUN_00bcda8c",
  "size": 532,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "397d1e0ac0006c0069af0f06299e75eb91d2b0ef50709f29e0b249a4a943fc7d",
  "source_text_sha256": "397d1e0ac0006c0069af0f06299e75eb91d2b0ef50709f29e0b249a4a943fc7d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcda8c",
        "00bcdc9f"
      ]
    ],
    "bytes_sha256": "0100f51802e5d4014d136cef18925ee46349eb3df538c90eb40ab311978fe981",
    "instruction_count": 133,
    "instruction_bytes": 532,
    "body_bytes": 532,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00576278](../00576/00576278.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5af90](../00c5a/00c5af90.md)
- [00c5b120](../00c5b/00c5b120.md)
- [00c5d160](../00c5d/00c5d160.md)

## 関連文字列（未確認候補）

~~~text
"!success || result != nullptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3821 bytes

~~~c

void FUN_00bcda8c(long param_1,long param_2,ulong param_3,long *param_4)

{
  byte *pbVar1;
  byte bVar2;
  long lVar3;
  byte *pbVar4;
  uint uVar5;
  long *plVar6;
  long lVar7;
  ulong uVar8;
  undefined8 uVar9;
  long lVar10;
  byte *pbVar11;
  ulong uVar12;
  long lVar13;
  undefined8 local_80;
  undefined8 uStack_78;
  undefined8 local_70;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  plVar6 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x10));
  if ((param_1 == 0) && ((param_3 & 1) != 0)) {
    _ZN8firebase9LogAssertEPKcz("!success || result != nullptr");
  }
  if ((param_3 & 1) == 0) {
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
  }
  else {
    lVar7 = FUN_004977f4(plVar6,param_1,DAT_011263e0);
    uVar8 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
    if (((uVar8 & 1) == 0) && (lVar7 != 0)) {
      uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(2);
      uVar5 = FUN_00576278(plVar6,lVar7,uVar9);
      pbVar1 = (byte *)param_4[1];
      uVar12 = (ulong)(int)uVar5;
      lVar10 = (long)pbVar1 - *param_4 >> 3;
      uVar8 = lVar10 * -0x5555555555555555;
      if (uVar8 < uVar12) {
        _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm
                  (param_4,uVar12 + lVar10 * 0x5555555555555555);
                    /* try { // try from 00bcdb64 to 00ccdb7b has its CatchHandler @ 00bce818 */
      }
      else if (uVar8 - uVar12 != 0) {
        pbVar11 = (byte *)(*param_4 + uVar12 * 0x18);
        if (pbVar11 != pbVar1) {
          bVar2 = pbVar1[-0x18];
          pbVar4 = pbVar1 + -0x18;
          while( true ) {
            if ((bVar2 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar1 + -8));
            }
            if (pbVar11 == pbVar4) break;
            bVar2 = pbVar4[-0x18];
            pbVar1 = pbVar4;
            pbVar4 = pbVar4 + -0x18;
          }
        }
        param_4[1] = (long)pbVar11;
      }
      if (0 < (int)uVar5) {
        lVar10 = 0;
        uVar8 = 0;
        do {
                    /* try { // try from 00bcdbfc to 00ccdc03 has its CatchHandler @ 00bce6e4 */
          uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(0);
          uVar9 = FUN_004977f4(plVar6,lVar7,uVar9,uVar8 & 0xffffffff);
          _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_80,plVar6,uVar9);
          lVar13 = *param_4;
          pbVar1 = (byte *)(lVar13 + lVar10);
          if ((*pbVar1 & 1) == 0) {
            *(undefined2 *)(lVar13 + lVar10) = 0;
          }
          else {
                    /* try { // try from 00bcdc38 to 00ccdc3f has its CatchHandler @ 00bce6dc */
            **(undefined1 **)(pbVar1 + 0x10) = 0;
            pbVar1[8] = 0;
            pbVar1[9] = 0;
            pbVar1[10] = 0;
            pbVar1[0xb] = 0;
            pbVar1[0xc] = 0;
            pbVar1[0xd] = 0;
            pbVar1[0xe] = 0;
            pbVar1[0xf] = 0;
            if ((*pbVar1 & 1) != 0) {
              _ZdlPv(*(void **)(pbVar1 + 0x10));
              *(undefined8 *)(lVar13 + lVar10) = 0;
            }
          }
          uVar8 = uVar8 + 1;
          lVar10 = lVar10 + 0x18;
          *(undefined8 *)(pbVar1 + 0x10) = local_70;
          *(undefined8 *)(pbVar1 + 8) = uStack_78;
          *(undefined8 *)pbVar1 = local_80;
        } while (uVar5 != uVar8);
      }
      (**(code **)(*plVar6 + 0xb8))(plVar6,lVar7);
    }
  }
                    /* try { // try from 00bcdc6c to 00ccdc8b has its CatchHandler @ 00bce6cc */
  if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* try { // try from 00bcdc98 to 00ccdcb7 has its CatchHandler @ 00bce6bc */
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
<a id="insn-00bcda8c"></a> `00bcda8c` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcda90"></a> `00bcda90` | `fb 13 00 f9` | str x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcda94"></a> `00bcda94` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcda98"></a> `00bcda98` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcda9c"></a> `00bcda9c` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcdaa0"></a> `00bcdaa0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcdaa4"></a> `00bcdaa4` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcdaa8"></a> `00bcdaa8` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcdaac"></a> `00bcdaac` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcdab0"></a> `00bcdab0` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdab4"></a> `00bcdab4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcdab8"></a> `00bcdab8` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-00bcdabc"></a> `00bcdabc` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bcdac0"></a> `00bcdac0` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcdac4"></a> `00bcdac4` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdac8"></a> `00bcdac8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bcdacc"></a> `00bcdacc` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcdad0"></a> `00bcdad0` | `6c 34 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdad4"></a> `00bcdad4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcdad8"></a> `00bcdad8` | `b6 00 00 b5` | cbnz x22,0x00bcdaec | `CONDITIONAL_JUMP`
<a id="insn-00bcdadc"></a> `00bcdadc` | `95 00 00 36` | tbz w21,#0x0,0x00bcdaec | `CONDITIONAL_JUMP`
<a id="insn-00bcdae0"></a> `00bcdae0` | `80 b6 ff f0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00bcdae4"></a> `00bcdae4` | `00 60 31 91` | add x0,x0,#0xc58 | `FALL_THROUGH`
<a id="insn-00bcdae8"></a> `00bcdae8` | `46 34 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdaec"></a> `00bcdaec` | `15 04 00 36` | tbz w21,#0x0,0x00bcdb6c | `CONDITIONAL_JUMP`
<a id="insn-00bcdaf0"></a> `00bcdaf0` | `c8 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcdaf4"></a> `00bcdaf4` | `02 f1 41 f9` | ldr x2,[x8, #0x3e0] | `FALL_THROUGH`
<a id="insn-00bcdaf8"></a> `00bcdaf8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdafc"></a> `00bcdafc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcdb00"></a> `00bcdb00` | `3d 27 e3 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb04"></a> `00bcdb04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcdb08"></a> `00bcdb08` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdb0c"></a> `00bcdb0c` | `15 34 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb10"></a> `00bcdb10` | `e0 0a 00 37` | tbnz w0,#0x0,0x00bcdc6c | `CONDITIONAL_JUMP`
<a id="insn-00bcdb14"></a> `00bcdb14` | `d5 0a 00 b4` | cbz x21,0x00bcdc6c | `CONDITIONAL_JUMP`
<a id="insn-00bcdb18"></a> `00bcdb18` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bcdb1c"></a> `00bcdb1c` | `81 35 02 94` | bl 0x00c5b120 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb20"></a> `00bcdb20` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bcdb24"></a> `00bcdb24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdb28"></a> `00bcdb28` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcdb2c"></a> `00bcdb2c` | `d3 a1 e6 97` | bl 0x00576278 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb30"></a> `00bcdb30` | `69 22 40 a9` | ldp x9,x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcdb34"></a> `00bcdb34` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00bcdb38"></a> `00bcdb38` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00bcdb3c"></a> `00bcdb3c` | `19 7c 40 93` | sxtw x25,w0 | `FALL_THROUGH`
<a id="insn-00bcdb40"></a> `00bcdb40` | `0a 01 09 cb` | sub x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00bcdb44"></a> `00bcdb44` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bcdb48"></a> `00bcdb48` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bcdb4c"></a> `00bcdb4c` | `5f 01 19 eb` | cmp x10,x25 | `FALL_THROUGH`
<a id="insn-00bcdb50"></a> `00bcdb50` | `42 01 00 54` | b.cs 0x00bcdb78 | `CONDITIONAL_JUMP`
<a id="insn-00bcdb54"></a> `00bcdb54` | `21 03 0a cb` | sub x1,x25,x10 | `FALL_THROUGH`
<a id="insn-00bcdb58"></a> `00bcdb58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdb5c"></a> `00bcdb5c` | `81 3d 02 94` | bl 0x00c5d160 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb60"></a> `00bcdb60` | `3f 07 00 71` | cmp w25,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdb64"></a> `00bcdb64` | `0a 03 00 54` | b.ge 0x00bcdbc4 | `CONDITIONAL_JUMP`
<a id="insn-00bcdb68"></a> `00bcdb68` | `3c 00 00 14` | b 0x00bcdc58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdb6c"></a> `00bcdb6c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdb70"></a> `00bcdb70` | `fc 33 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdb74"></a> `00bcdb74` | `3e 00 00 14` | b 0x00bcdc6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdb78"></a> `00bcdb78` | `29 02 00 54` | b.ls 0x00bcdbbc | `CONDITIONAL_JUMP`
<a id="insn-00bcdb7c"></a> `00bcdb7c` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdb80"></a> `00bcdb80` | `36 27 0a 9b` | madd x22,x25,x10,x9 | `FALL_THROUGH`
<a id="insn-00bcdb84"></a> `00bcdb84` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bcdb88"></a> `00bcdb88` | `80 01 00 54` | b.eq 0x00bcdbb8 | `CONDITIONAL_JUMP`
<a id="insn-00bcdb8c"></a> `00bcdb8c` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00bcdb90"></a> `00bcdb90` | `09 8f 5e 38` | ldrb w9,[x24, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bcdb94"></a> `00bcdb94` | `c9 00 00 37` | tbnz w9,#0x0,0x00bcdbac | `CONDITIONAL_JUMP`
<a id="insn-00bcdb98"></a> `00bcdb98` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bcdb9c"></a> `00bcdb9c` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00bcdba0"></a> `00bcdba0` | `c0 00 00 54` | b.eq 0x00bcdbb8 | `CONDITIONAL_JUMP`
<a id="insn-00bcdba4"></a> `00bcdba4` | `09 8f 5e 38` | ldrb w9,[x24, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bcdba8"></a> `00bcdba8` | `89 ff 07 36` | tbz w9,#0x0,0x00bcdb98 | `CONDITIONAL_JUMP`
<a id="insn-00bcdbac"></a> `00bcdbac` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bcdbb0"></a> `00bcdbb0` | `c0 27 02 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdbb4"></a> `00bcdbb4` | `f9 ff ff 17` | b 0x00bcdb98 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdbb8"></a> `00bcdbb8` | `76 06 00 f9` | str x22,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdbbc"></a> `00bcdbbc` | `3f 07 00 71` | cmp w25,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdbc0"></a> `00bcdbc0` | `cb 04 00 54` | b.lt 0x00bcdc58 | `CONDITIONAL_JUMP`
<a id="insn-00bcdbc4"></a> `00bcdbc4` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00bcdbc8"></a> `00bcdbc8` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00bcdbcc"></a> `00bcdbcc` | `39 7f 40 92` | and x25,x25,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bcdbd0"></a> `00bcdbd0` | `0a 00 00 14` | b 0x00bcdbf8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdbd4"></a> `00bcdbd4` | `7f 6b 38 78` | strh wzr,[x27, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bcdbd8"></a> `00bcdbd8` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdbdc"></a> `00bcdbdc` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bcdbe0"></a> `00bcdbe0` | `d6 06 00 91` | add x22,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdbe4"></a> `00bcdbe4` | `3f 03 16 eb` | cmp x25,x22 | `FALL_THROUGH`
<a id="insn-00bcdbe8"></a> `00bcdbe8` | `18 63 00 91` | add x24,x24,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdbec"></a> `00bcdbec` | `48 0b 00 f9` | str x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdbf0"></a> `00bcdbf0` | `40 03 80 3d` | str q0,[x26] | `FALL_THROUGH`
<a id="insn-00bcdbf4"></a> `00bcdbf4` | `20 03 00 54` | b.eq 0x00bcdc58 | `CONDITIONAL_JUMP`
<a id="insn-00bcdbf8"></a> `00bcdbf8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bcdbfc"></a> `00bcdbfc` | `49 35 02 94` | bl 0x00c5b120 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc00"></a> `00bcdc00` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bcdc04"></a> `00bcdc04` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdc08"></a> `00bcdc08` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcdc0c"></a> `00bcdc0c` | `e3 03 16 2a` | mov w3,w22 | `FALL_THROUGH`
<a id="insn-00bcdc10"></a> `00bcdc10` | `f9 26 e3 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc14"></a> `00bcdc14` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bcdc18"></a> `00bcdc18` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bcdc1c"></a> `00bcdc1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdc20"></a> `00bcdc20` | `dc 34 02 94` | bl 0x00c5af90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc24"></a> `00bcdc24` | `7b 02 40 f9` | ldr x27,[x19] | `FALL_THROUGH`
<a id="insn-00bcdc28"></a> `00bcdc28` | `7a 03 18 8b` | add x26,x27,x24 | `FALL_THROUGH`
<a id="insn-00bcdc2c"></a> `00bcdc2c` | `48 03 40 39` | ldrb w8,[x26] | `FALL_THROUGH`
<a id="insn-00bcdc30"></a> `00bcdc30` | `28 fd 07 36` | tbz w8,#0x0,0x00bcdbd4 | `CONDITIONAL_JUMP`
<a id="insn-00bcdc34"></a> `00bcdc34` | `48 0b 40 f9` | ldr x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdc38"></a> `00bcdc38` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bcdc3c"></a> `00bcdc3c` | `48 03 40 39` | ldrb w8,[x26] | `FALL_THROUGH`
<a id="insn-00bcdc40"></a> `00bcdc40` | `5f 07 00 f9` | str xzr,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdc44"></a> `00bcdc44` | `a8 fc 07 36` | tbz w8,#0x0,0x00bcdbd8 | `CONDITIONAL_JUMP`
<a id="insn-00bcdc48"></a> `00bcdc48` | `40 0b 40 f9` | ldr x0,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdc4c"></a> `00bcdc4c` | `99 27 02 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdc50"></a> `00bcdc50` | `7f 6b 38 f8` | str xzr,[x27, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bcdc54"></a> `00bcdc54` | `e1 ff ff 17` | b 0x00bcdbd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdc58"></a> `00bcdc58` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bcdc5c"></a> `00bcdc5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdc60"></a> `00bcdc60` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcdc64"></a> `00bcdc64` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcdc68"></a> `00bcdc68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdc6c"></a> `00bcdc6c` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdc70"></a> `00bcdc70` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcdc74"></a> `00bcdc74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcdc78"></a> `00bcdc78` | `21 01 00 54` | b.ne 0x00bcdc9c | `CONDITIONAL_JUMP`
<a id="insn-00bcdc7c"></a> `00bcdc7c` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcdc80"></a> `00bcdc80` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcdc84"></a> `00bcdc84` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcdc88"></a> `00bcdc88` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcdc8c"></a> `00bcdc8c` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcdc90"></a> `00bcdc90` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdc94"></a> `00bcdc94` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcdc98"></a> `00bcdc98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcdc9c"></a> `00bcdc9c` | `91 27 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcda8c`](#insn-00bcda8c) 範囲 `[['00bcda8c', '00bcdadb']]`
  - `CONDITIONAL_JUMP` [`00bcdad8`](#insn-00bcdad8) → [`00bcdaec`](#insn-00bcdaec)
  - `FALL_THROUGH` [`00bcdad8`](#insn-00bcdad8) → [`00bcdadc`](#insn-00bcdadc)
- ブロック [`00bcdadc`](#insn-00bcdadc) 範囲 `[['00bcdadc', '00bcdadf']]`
  - `CONDITIONAL_JUMP` [`00bcdadc`](#insn-00bcdadc) → [`00bcdaec`](#insn-00bcdaec)
  - `FALL_THROUGH` [`00bcdadc`](#insn-00bcdadc) → [`00bcdae0`](#insn-00bcdae0)
- ブロック [`00bcdae0`](#insn-00bcdae0) 範囲 `[['00bcdae0', '00bcdaeb']]`
  - `FALL_THROUGH` [`00bcdae8`](#insn-00bcdae8) → [`00bcdaec`](#insn-00bcdaec)
- ブロック [`00bcdaec`](#insn-00bcdaec) 範囲 `[['00bcdaec', '00bcdaef']]`
  - `CONDITIONAL_JUMP` [`00bcdaec`](#insn-00bcdaec) → [`00bcdb6c`](#insn-00bcdb6c)
  - `FALL_THROUGH` [`00bcdaec`](#insn-00bcdaec) → [`00bcdaf0`](#insn-00bcdaf0)
- ブロック [`00bcdaf0`](#insn-00bcdaf0) 範囲 `[['00bcdaf0', '00bcdb13']]`
  - `CONDITIONAL_JUMP` [`00bcdb10`](#insn-00bcdb10) → [`00bcdc6c`](#insn-00bcdc6c)
  - `FALL_THROUGH` [`00bcdb10`](#insn-00bcdb10) → [`00bcdb14`](#insn-00bcdb14)
- ブロック [`00bcdb14`](#insn-00bcdb14) 範囲 `[['00bcdb14', '00bcdb17']]`
  - `CONDITIONAL_JUMP` [`00bcdb14`](#insn-00bcdb14) → [`00bcdc6c`](#insn-00bcdc6c)
  - `FALL_THROUGH` [`00bcdb14`](#insn-00bcdb14) → [`00bcdb18`](#insn-00bcdb18)
- ブロック [`00bcdb18`](#insn-00bcdb18) 範囲 `[['00bcdb18', '00bcdb53']]`
  - `CONDITIONAL_JUMP` [`00bcdb50`](#insn-00bcdb50) → [`00bcdb78`](#insn-00bcdb78)
  - `FALL_THROUGH` [`00bcdb50`](#insn-00bcdb50) → [`00bcdb54`](#insn-00bcdb54)
- ブロック [`00bcdb54`](#insn-00bcdb54) 範囲 `[['00bcdb54', '00bcdb63']]`
  - `FALL_THROUGH` [`00bcdb60`](#insn-00bcdb60) → [`00bcdb64`](#insn-00bcdb64)
- ブロック [`00bcdb64`](#insn-00bcdb64) 範囲 `[['00bcdb64', '00bcdb67']]`
  - `CONDITIONAL_JUMP` [`00bcdb64`](#insn-00bcdb64) → [`00bcdbc4`](#insn-00bcdbc4)
  - `FALL_THROUGH` [`00bcdb64`](#insn-00bcdb64) → [`00bcdb68`](#insn-00bcdb68)
- ブロック [`00bcdb68`](#insn-00bcdb68) 範囲 `[['00bcdb68', '00bcdb6b']]`
  - `UNCONDITIONAL_JUMP` [`00bcdb68`](#insn-00bcdb68) → [`00bcdc58`](#insn-00bcdc58)
- ブロック [`00bcdb6c`](#insn-00bcdb6c) 範囲 `[['00bcdb6c', '00bcdb77']]`
  - `UNCONDITIONAL_JUMP` [`00bcdb74`](#insn-00bcdb74) → [`00bcdc6c`](#insn-00bcdc6c)
- ブロック [`00bcdb78`](#insn-00bcdb78) 範囲 `[['00bcdb78', '00bcdb7b']]`
  - `CONDITIONAL_JUMP` [`00bcdb78`](#insn-00bcdb78) → [`00bcdbbc`](#insn-00bcdbbc)
  - `FALL_THROUGH` [`00bcdb78`](#insn-00bcdb78) → [`00bcdb7c`](#insn-00bcdb7c)
- ブロック [`00bcdb7c`](#insn-00bcdb7c) 範囲 `[['00bcdb7c', '00bcdb8b']]`
  - `CONDITIONAL_JUMP` [`00bcdb88`](#insn-00bcdb88) → [`00bcdbb8`](#insn-00bcdbb8)
  - `FALL_THROUGH` [`00bcdb88`](#insn-00bcdb88) → [`00bcdb8c`](#insn-00bcdb8c)
- ブロック [`00bcdb8c`](#insn-00bcdb8c) 範囲 `[['00bcdb8c', '00bcdb97']]`
  - `CONDITIONAL_JUMP` [`00bcdb94`](#insn-00bcdb94) → [`00bcdbac`](#insn-00bcdbac)
  - `FALL_THROUGH` [`00bcdb94`](#insn-00bcdb94) → [`00bcdb98`](#insn-00bcdb98)
- ブロック [`00bcdb98`](#insn-00bcdb98) 範囲 `[['00bcdb98', '00bcdba3']]`
  - `CONDITIONAL_JUMP` [`00bcdba0`](#insn-00bcdba0) → [`00bcdbb8`](#insn-00bcdbb8)
  - `FALL_THROUGH` [`00bcdba0`](#insn-00bcdba0) → [`00bcdba4`](#insn-00bcdba4)
- ブロック [`00bcdba4`](#insn-00bcdba4) 範囲 `[['00bcdba4', '00bcdbab']]`
  - `CONDITIONAL_JUMP` [`00bcdba8`](#insn-00bcdba8) → [`00bcdb98`](#insn-00bcdb98)
  - `FALL_THROUGH` [`00bcdba8`](#insn-00bcdba8) → [`00bcdbac`](#insn-00bcdbac)
- ブロック [`00bcdbac`](#insn-00bcdbac) 範囲 `[['00bcdbac', '00bcdbb7']]`
  - `UNCONDITIONAL_JUMP` [`00bcdbb4`](#insn-00bcdbb4) → [`00bcdb98`](#insn-00bcdb98)
- ブロック [`00bcdbb8`](#insn-00bcdbb8) 範囲 `[['00bcdbb8', '00bcdbbb']]`
  - `FALL_THROUGH` [`00bcdbb8`](#insn-00bcdbb8) → [`00bcdbbc`](#insn-00bcdbbc)
- ブロック [`00bcdbbc`](#insn-00bcdbbc) 範囲 `[['00bcdbbc', '00bcdbc3']]`
  - `CONDITIONAL_JUMP` [`00bcdbc0`](#insn-00bcdbc0) → [`00bcdc58`](#insn-00bcdc58)
  - `FALL_THROUGH` [`00bcdbc0`](#insn-00bcdbc0) → [`00bcdbc4`](#insn-00bcdbc4)
- ブロック [`00bcdbc4`](#insn-00bcdbc4) 範囲 `[['00bcdbc4', '00bcdbd3']]`
  - `UNCONDITIONAL_JUMP` [`00bcdbd0`](#insn-00bcdbd0) → [`00bcdbf8`](#insn-00bcdbf8)
- ブロック [`00bcdbd4`](#insn-00bcdbd4) 範囲 `[['00bcdbd4', '00bcdbd7']]`
  - `FALL_THROUGH` [`00bcdbd4`](#insn-00bcdbd4) → [`00bcdbd8`](#insn-00bcdbd8)
- ブロック [`00bcdbd8`](#insn-00bcdbd8) 範囲 `[['00bcdbd8', '00bcdbf7']]`
  - `CONDITIONAL_JUMP` [`00bcdbf4`](#insn-00bcdbf4) → [`00bcdc58`](#insn-00bcdc58)
  - `FALL_THROUGH` [`00bcdbf4`](#insn-00bcdbf4) → [`00bcdbf8`](#insn-00bcdbf8)
- ブロック [`00bcdbf8`](#insn-00bcdbf8) 範囲 `[['00bcdbf8', '00bcdbfb']]`
  - `FALL_THROUGH` [`00bcdbf8`](#insn-00bcdbf8) → [`00bcdbfc`](#insn-00bcdbfc)
- ブロック [`00bcdbfc`](#insn-00bcdbfc) 範囲 `[['00bcdbfc', '00bcdc33']]`
  - `CONDITIONAL_JUMP` [`00bcdc30`](#insn-00bcdc30) → [`00bcdbd4`](#insn-00bcdbd4)
  - `FALL_THROUGH` [`00bcdc30`](#insn-00bcdc30) → [`00bcdc34`](#insn-00bcdc34)
- ブロック [`00bcdc34`](#insn-00bcdc34) 範囲 `[['00bcdc34', '00bcdc37']]`
  - `FALL_THROUGH` [`00bcdc34`](#insn-00bcdc34) → [`00bcdc38`](#insn-00bcdc38)
- ブロック [`00bcdc38`](#insn-00bcdc38) 範囲 `[['00bcdc38', '00bcdc47']]`
  - `CONDITIONAL_JUMP` [`00bcdc44`](#insn-00bcdc44) → [`00bcdbd8`](#insn-00bcdbd8)
  - `FALL_THROUGH` [`00bcdc44`](#insn-00bcdc44) → [`00bcdc48`](#insn-00bcdc48)
- ブロック [`00bcdc48`](#insn-00bcdc48) 範囲 `[['00bcdc48', '00bcdc57']]`
  - `UNCONDITIONAL_JUMP` [`00bcdc54`](#insn-00bcdc54) → [`00bcdbd8`](#insn-00bcdbd8)
- ブロック [`00bcdc58`](#insn-00bcdc58) 範囲 `[['00bcdc58', '00bcdc6b']]`
  - `FALL_THROUGH` [`00bcdc68`](#insn-00bcdc68) → [`00bcdc6c`](#insn-00bcdc6c)
- ブロック [`00bcdc6c`](#insn-00bcdc6c) 範囲 `[['00bcdc6c', '00bcdc7b']]`
  - `CONDITIONAL_JUMP` [`00bcdc78`](#insn-00bcdc78) → [`00bcdc9c`](#insn-00bcdc9c)
  - `FALL_THROUGH` [`00bcdc78`](#insn-00bcdc78) → [`00bcdc7c`](#insn-00bcdc7c)
- ブロック [`00bcdc7c`](#insn-00bcdc7c) 範囲 `[['00bcdc7c', '00bcdc97']]`
  - `FALL_THROUGH` [`00bcdc94`](#insn-00bcdc94) → [`00bcdc98`](#insn-00bcdc98)
- ブロック [`00bcdc98`](#insn-00bcdc98) 範囲 `[['00bcdc98', '00bcdc9b']]`
- ブロック [`00bcdc9c`](#insn-00bcdc9c) 範囲 `[['00bcdc9c', '00bcdc9f']]`

## 命令位置別の参照

- [`00bcda90`](#insn-00bcda90) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcda94`](#insn-00bcda94) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcda98`](#insn-00bcda98) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcda9c`](#insn-00bcda9c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdaa0`](#insn-00bcdaa0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdaa4`](#insn-00bcdaa4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdac0`](#insn-00bcdac0) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdad0`](#insn-00bcdad0) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bcdad8`](#insn-00bcdad8) → [`00bcdaec`](#insn-00bcdaec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdadc`](#insn-00bcdadc) → [`00bcdaec`](#insn-00bcdaec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdae4`](#insn-00bcdae4) → `002a0c58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcdae8`](#insn-00bcdae8) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bcdaec`](#insn-00bcdaec) → [`00bcdb6c`](#insn-00bcdb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdaf4`](#insn-00bcdaf4) → `011263e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdb00`](#insn-00bcdb00) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb0c`](#insn-00bcdb0c) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb10`](#insn-00bcdb10) → [`00bcdc6c`](#insn-00bcdc6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb14`](#insn-00bcdb14) → [`00bcdc6c`](#insn-00bcdc6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb1c`](#insn-00bcdb1c) → [`00c5b120`](../00c5b/00c5b120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b120` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb2c`](#insn-00bcdb2c) → [`00576278`](../00576/00576278.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00576278` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb50`](#insn-00bcdb50) → [`00bcdb78`](#insn-00bcdb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb5c`](#insn-00bcdb5c) → [`00c5d160`](../00c5d/00c5d160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d160` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb64`](#insn-00bcdb64) → [`00bcdbc4`](#insn-00bcdbc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb68`](#insn-00bcdb68) → [`00bcdc58`](#insn-00bcdc58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb70`](#insn-00bcdb70) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb74`](#insn-00bcdb74) → [`00bcdc6c`](#insn-00bcdc6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb78`](#insn-00bcdb78) → [`00bcdbbc`](#insn-00bcdbbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb88`](#insn-00bcdb88) → [`00bcdbb8`](#insn-00bcdbb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdb94`](#insn-00bcdb94) → [`00bcdbac`](#insn-00bcdbac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdba0`](#insn-00bcdba0) → [`00bcdbb8`](#insn-00bcdbb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdba8`](#insn-00bcdba8) → [`00bcdb98`](#insn-00bcdb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbb0`](#insn-00bcdbb0) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbb4`](#insn-00bcdbb4) → [`00bcdb98`](#insn-00bcdb98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbc0`](#insn-00bcdbc0) → [`00bcdc58`](#insn-00bcdc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbd0`](#insn-00bcdbd0) → [`00bcdbf8`](#insn-00bcdbf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbd8`](#insn-00bcdbd8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbdc`](#insn-00bcdbdc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbf4`](#insn-00bcdbf4) → [`00bcdc58`](#insn-00bcdc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdbfc`](#insn-00bcdbfc) → [`00c5b120`](../00c5b/00c5b120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b120` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc10`](#insn-00bcdc10) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc20`](#insn-00bcdc20) → [`00c5af90`](../00c5a/00c5af90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af90` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc30`](#insn-00bcdc30) → [`00bcdbd4`](#insn-00bcdbd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc44`](#insn-00bcdc44) → [`00bcdbd8`](#insn-00bcdbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc4c`](#insn-00bcdc4c) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc54`](#insn-00bcdc54) → [`00bcdbd8`](#insn-00bcdbd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc70`](#insn-00bcdc70) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc78`](#insn-00bcdc78) → [`00bcdc9c`](#insn-00bcdc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc7c`](#insn-00bcdc7c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc80`](#insn-00bcdc80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc84`](#insn-00bcdc84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc88`](#insn-00bcdc88) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc8c`](#insn-00bcdc8c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc90`](#insn-00bcdc90) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdc9c`](#insn-00bcdc9c) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcda90`](#insn-00bcda90)

~~~json
{
  "source": "00bcda90",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcda94`](#insn-00bcda94)

~~~json
{
  "source": "00bcda94",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcda98`](#insn-00bcda98)

~~~json
{
  "source": "00bcda98",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcda9c`](#insn-00bcda9c)

~~~json
{
  "source": "00bcda9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdaa0`](#insn-00bcdaa0)

~~~json
{
  "source": "00bcdaa0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdaa4`](#insn-00bcdaa4)

~~~json
{
  "source": "00bcdaa4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdac0`](#insn-00bcdac0)

~~~json
{
  "source": "00bcdac0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdad0`](#insn-00bcdad0)

~~~json
{
  "source": "00bcdad0",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdad8`](#insn-00bcdad8)

~~~json
{
  "source": "00bcdad8",
  "target": "00bcdaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdadc`](#insn-00bcdadc)

~~~json
{
  "source": "00bcdadc",
  "target": "00bcdaec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdae4`](#insn-00bcdae4)

~~~json
{
  "source": "00bcdae4",
  "target": "002a0c58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0c58",
  "offset": 0,
  "size": 30,
  "datatype": "string",
  "bytes": "2173756363657373207c7c20726573756c7420213d206e756c6c70747200",
  "capture_start": "002a0c58",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcdae8`](#insn-00bcdae8)

~~~json
{
  "source": "00bcdae8",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdaec`](#insn-00bcdaec)

~~~json
{
  "source": "00bcdaec",
  "target": "00bcdb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdaf4`](#insn-00bcdaf4)

~~~json
{
  "source": "00bcdaf4",
  "target": "011263e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011263e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdb00`](#insn-00bcdb00)

~~~json
{
  "source": "00bcdb00",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb0c`](#insn-00bcdb0c)

~~~json
{
  "source": "00bcdb0c",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb10`](#insn-00bcdb10)

~~~json
{
  "source": "00bcdb10",
  "target": "00bcdc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb14`](#insn-00bcdb14)

~~~json
{
  "source": "00bcdb14",
  "target": "00bcdc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb1c`](#insn-00bcdb1c)

~~~json
{
  "source": "00bcdb1c",
  "target": "00c5b120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb2c`](#insn-00bcdb2c)

~~~json
{
  "source": "00bcdb2c",
  "target": "00576278",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb50`](#insn-00bcdb50)

~~~json
{
  "source": "00bcdb50",
  "target": "00bcdb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb5c`](#insn-00bcdb5c)

~~~json
{
  "source": "00bcdb5c",
  "target": "00c5d160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb64`](#insn-00bcdb64)

~~~json
{
  "source": "00bcdb64",
  "target": "00bcdbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb68`](#insn-00bcdb68)

~~~json
{
  "source": "00bcdb68",
  "target": "00bcdc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb70`](#insn-00bcdb70)

~~~json
{
  "source": "00bcdb70",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdb74`](#insn-00bcdb74)

~~~json
{
  "source": "00bcdb74",
  "target": "00bcdc6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb78`](#insn-00bcdb78)

~~~json
{
  "source": "00bcdb78",
  "target": "00bcdbbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb88`](#insn-00bcdb88)

~~~json
{
  "source": "00bcdb88",
  "target": "00bcdbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdb94`](#insn-00bcdb94)

~~~json
{
  "source": "00bcdb94",
  "target": "00bcdbac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdba0`](#insn-00bcdba0)

~~~json
{
  "source": "00bcdba0",
  "target": "00bcdbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdba8`](#insn-00bcdba8)

~~~json
{
  "source": "00bcdba8",
  "target": "00bcdb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbb0`](#insn-00bcdbb0)

~~~json
{
  "source": "00bcdbb0",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdbb4`](#insn-00bcdbb4)

~~~json
{
  "source": "00bcdbb4",
  "target": "00bcdb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbc0`](#insn-00bcdbc0)

~~~json
{
  "source": "00bcdbc0",
  "target": "00bcdc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbd0`](#insn-00bcdbd0)

~~~json
{
  "source": "00bcdbd0",
  "target": "00bcdbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbd8`](#insn-00bcdbd8)

~~~json
{
  "source": "00bcdbd8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbdc`](#insn-00bcdbdc)

~~~json
{
  "source": "00bcdbdc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbf4`](#insn-00bcdbf4)

~~~json
{
  "source": "00bcdbf4",
  "target": "00bcdc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdbfc`](#insn-00bcdbfc)

~~~json
{
  "source": "00bcdbfc",
  "target": "00c5b120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc10`](#insn-00bcdc10)

~~~json
{
  "source": "00bcdc10",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc20`](#insn-00bcdc20)

~~~json
{
  "source": "00bcdc20",
  "target": "00c5af90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc30`](#insn-00bcdc30)

~~~json
{
  "source": "00bcdc30",
  "target": "00bcdbd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc44`](#insn-00bcdc44)

~~~json
{
  "source": "00bcdc44",
  "target": "00bcdbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc4c`](#insn-00bcdc4c)

~~~json
{
  "source": "00bcdc4c",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdc54`](#insn-00bcdc54)

~~~json
{
  "source": "00bcdc54",
  "target": "00bcdbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc70`](#insn-00bcdc70)

~~~json
{
  "source": "00bcdc70",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc78`](#insn-00bcdc78)

~~~json
{
  "source": "00bcdc78",
  "target": "00bcdc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc7c`](#insn-00bcdc7c)

~~~json
{
  "source": "00bcdc7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc80`](#insn-00bcdc80)

~~~json
{
  "source": "00bcdc80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc84`](#insn-00bcdc84)

~~~json
{
  "source": "00bcdc84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc88`](#insn-00bcdc88)

~~~json
{
  "source": "00bcdc88",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc8c`](#insn-00bcdc8c)

~~~json
{
  "source": "00bcdc8c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc90`](#insn-00bcdc90)

~~~json
{
  "source": "00bcdc90",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdc9c`](#insn-00bcdc9c)

~~~json
{
  "source": "00bcdc9c",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
