# 00bcdeb4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcda8c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcda8c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-87739202910b90951405e2749b1fed9f)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcdf50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcdf50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-f02944682cf35d84488e91fd9869818c)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdeb4",
  "name": "FUN_00bcdeb4",
  "size": 532,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "158de284abcd4cdaff92e024303dc3efb7cf5179f35fbee733fb7b316c188a4e",
  "source_text_sha256": "158de284abcd4cdaff92e024303dc3efb7cf5179f35fbee733fb7b316c188a4e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdeb4",
        "00bce0c7"
      ]
    ],
    "bytes_sha256": "f34aaba9881acc215a830f1cba7f0c5d0799e45f354e335c9eb15157389e5a3c",
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

- [00497834](../00497/00497834.md)
- [005762b8](../00576/005762b8.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b000](../00c5b/00c5b000.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b390](../00c5b/00c5b390.md)
- [00c5b520](../00c5b/00c5b520.md)
- [00c5d560](../00c5d/00c5d560.md)

## 関連文字列（未確認候補）

~~~text
"!success || result != nullptr"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4162 bytes

~~~c

void FUN_00bcdeb4(long param_1,long param_2,ulong param_3,long *param_4)

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
  
                    /* try { // try from 00bcdeb4 to 00ccdf47 has its CatchHandler @ 00bcc5d0 */
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
    lVar7 = FUN_00497834(plVar6,param_1,DAT_011267e0);
    uVar8 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar6);
    if (((uVar8 & 1) == 0) && (lVar7 != 0)) {
      uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(2);
                    /* try { // try from 00bcdf48 to 00ccdf4f has its CatchHandler @ 00bce8b0 */
      uVar5 = FUN_005762b8(plVar6,lVar7,uVar9);
      pbVar1 = (byte *)param_4[1];
      uVar12 = (ulong)(int)uVar5;
      lVar10 = (long)pbVar1 - *param_4 >> 3;
      uVar8 = lVar10 * -0x5555555555555555;
                    /* try { // try from 00bcdf78 to 00ccdf8f has its CatchHandler @ 00bce8ac */
      if (uVar8 < uVar12) {
        _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE8__appendEm
                  (param_4,uVar12 + lVar10 * 0x5555555555555555);
      }
      else {
                    /* try { // try from 00bcdfa0 to 00ccdfbf has its CatchHandler @ 00bce8a8 */
        if (uVar8 - uVar12 != 0) {
          pbVar11 = (byte *)(*param_4 + uVar12 * 0x18);
          if (pbVar11 != pbVar1) {
            bVar2 = pbVar1[-0x18];
            pbVar4 = pbVar1 + -0x18;
            while( true ) {
              if ((bVar2 & 1) != 0) {
                _ZdlPv(*(void **)(pbVar1 + -8));
              }
                    /* try { // try from 00bcdfc0 to 00cce077 has its CatchHandler @ 00bcc5d0 */
              if (pbVar11 == pbVar4) break;
              bVar2 = pbVar4[-0x18];
              pbVar1 = pbVar4;
              pbVar4 = pbVar4 + -0x18;
            }
          }
          param_4[1] = (long)pbVar11;
        }
      }
      if (0 < (int)uVar5) {
        lVar10 = 0;
        uVar8 = 0;
        do {
          uVar9 = _ZN8firebase4util4list11GetMethodIdENS1_6MethodE(0);
          uVar9 = FUN_00497834(plVar6,lVar7,uVar9,uVar8 & 0xffffffff);
          _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_80,plVar6,uVar9);
          lVar13 = *param_4;
          pbVar1 = (byte *)(lVar13 + lVar10);
          if ((*pbVar1 & 1) == 0) {
            *(undefined2 *)(lVar13 + lVar10) = 0;
          }
          else {
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
                    /* try { // try from 00bce078 to 00cce08f has its CatchHandler @ 00bce8a4 */
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
                    /* try { // try from 00bce0a0 to 00cce0bf has its CatchHandler @ 00bce8a0 */
  if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* try { // try from 00bce0c0 to 00cce153 has its CatchHandler @ 00bcc5d0 */
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
<a id="insn-00bcdeb4"></a> `00bcdeb4` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcdeb8"></a> `00bcdeb8` | `fb 13 00 f9` | str x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdebc"></a> `00bcdebc` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcdec0"></a> `00bcdec0` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcdec4"></a> `00bcdec4` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcdec8"></a> `00bcdec8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcdecc"></a> `00bcdecc` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcded0"></a> `00bcded0` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcded4"></a> `00bcded4` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcded8"></a> `00bcded8` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdedc"></a> `00bcdedc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcdee0"></a> `00bcdee0` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-00bcdee4"></a> `00bcdee4` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bcdee8"></a> `00bcdee8` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcdeec"></a> `00bcdeec` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdef0"></a> `00bcdef0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bcdef4"></a> `00bcdef4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcdef8"></a> `00bcdef8` | `62 34 02 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdefc"></a> `00bcdefc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcdf00"></a> `00bcdf00` | `b6 00 00 b5` | cbnz x22,0x00bcdf14 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf04"></a> `00bcdf04` | `95 00 00 36` | tbz w21,#0x0,0x00bcdf14 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf08"></a> `00bcdf08` | `80 b6 ff f0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00bcdf0c"></a> `00bcdf0c` | `00 94 34 91` | add x0,x0,#0xd25 | `FALL_THROUGH`
<a id="insn-00bcdf10"></a> `00bcdf10` | `3c 34 02 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf14"></a> `00bcdf14` | `15 04 00 36` | tbz w21,#0x0,0x00bcdf94 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf18"></a> `00bcdf18` | `c8 2a 00 b0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcdf1c"></a> `00bcdf1c` | `02 f1 43 f9` | ldr x2,[x8, #0x7e0] | `FALL_THROUGH`
<a id="insn-00bcdf20"></a> `00bcdf20` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdf24"></a> `00bcdf24` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcdf28"></a> `00bcdf28` | `43 26 e3 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf2c"></a> `00bcdf2c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcdf30"></a> `00bcdf30` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdf34"></a> `00bcdf34` | `0b 34 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf38"></a> `00bcdf38` | `e0 0a 00 37` | tbnz w0,#0x0,0x00bce094 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf3c"></a> `00bcdf3c` | `d5 0a 00 b4` | cbz x21,0x00bce094 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf40"></a> `00bcdf40` | `40 00 80 52` | mov w0,#0x2 | `FALL_THROUGH`
<a id="insn-00bcdf44"></a> `00bcdf44` | `77 35 02 94` | bl 0x00c5b520 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf48"></a> `00bcdf48` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bcdf4c"></a> `00bcdf4c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdf50"></a> `00bcdf50` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcdf54"></a> `00bcdf54` | `d9 a0 e6 97` | bl 0x005762b8 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf58"></a> `00bcdf58` | `69 22 40 a9` | ldp x9,x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcdf5c"></a> `00bcdf5c` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00bcdf60"></a> `00bcdf60` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00bcdf64"></a> `00bcdf64` | `19 7c 40 93` | sxtw x25,w0 | `FALL_THROUGH`
<a id="insn-00bcdf68"></a> `00bcdf68` | `0a 01 09 cb` | sub x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00bcdf6c"></a> `00bcdf6c` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bcdf70"></a> `00bcdf70` | `4a 7d 0b 9b` | mul x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bcdf74"></a> `00bcdf74` | `5f 01 19 eb` | cmp x10,x25 | `FALL_THROUGH`
<a id="insn-00bcdf78"></a> `00bcdf78` | `42 01 00 54` | b.cs 0x00bcdfa0 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf7c"></a> `00bcdf7c` | `21 03 0a cb` | sub x1,x25,x10 | `FALL_THROUGH`
<a id="insn-00bcdf80"></a> `00bcdf80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdf84"></a> `00bcdf84` | `77 3d 02 94` | bl 0x00c5d560 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf88"></a> `00bcdf88` | `3f 07 00 71` | cmp w25,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdf8c"></a> `00bcdf8c` | `0a 03 00 54` | b.ge 0x00bcdfec | `CONDITIONAL_JUMP`
<a id="insn-00bcdf90"></a> `00bcdf90` | `3c 00 00 14` | b 0x00bce080 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdf94"></a> `00bcdf94` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdf98"></a> `00bcdf98` | `f2 33 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdf9c"></a> `00bcdf9c` | `3e 00 00 14` | b 0x00bce094 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdfa0"></a> `00bcdfa0` | `29 02 00 54` | b.ls 0x00bcdfe4 | `CONDITIONAL_JUMP`
<a id="insn-00bcdfa4"></a> `00bcdfa4` | `0a 03 80 52` | mov w10,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdfa8"></a> `00bcdfa8` | `36 27 0a 9b` | madd x22,x25,x10,x9 | `FALL_THROUGH`
<a id="insn-00bcdfac"></a> `00bcdfac` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bcdfb0"></a> `00bcdfb0` | `80 01 00 54` | b.eq 0x00bcdfe0 | `CONDITIONAL_JUMP`
<a id="insn-00bcdfb4"></a> `00bcdfb4` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00bcdfb8"></a> `00bcdfb8` | `09 8f 5e 38` | ldrb w9,[x24, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bcdfbc"></a> `00bcdfbc` | `c9 00 00 37` | tbnz w9,#0x0,0x00bcdfd4 | `CONDITIONAL_JUMP`
<a id="insn-00bcdfc0"></a> `00bcdfc0` | `df 02 18 eb` | cmp x22,x24 | `FALL_THROUGH`
<a id="insn-00bcdfc4"></a> `00bcdfc4` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00bcdfc8"></a> `00bcdfc8` | `c0 00 00 54` | b.eq 0x00bcdfe0 | `CONDITIONAL_JUMP`
<a id="insn-00bcdfcc"></a> `00bcdfcc` | `09 8f 5e 38` | ldrb w9,[x24, #-0x18]! | `FALL_THROUGH`
<a id="insn-00bcdfd0"></a> `00bcdfd0` | `89 ff 07 36` | tbz w9,#0x0,0x00bcdfc0 | `CONDITIONAL_JUMP`
<a id="insn-00bcdfd4"></a> `00bcdfd4` | `00 81 5f f8` | ldur x0,[x8, #-0x8] | `FALL_THROUGH`
<a id="insn-00bcdfd8"></a> `00bcdfd8` | `b6 27 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdfdc"></a> `00bcdfdc` | `f9 ff ff 17` | b 0x00bcdfc0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdfe0"></a> `00bcdfe0` | `76 06 00 f9` | str x22,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcdfe4"></a> `00bcdfe4` | `3f 07 00 71` | cmp w25,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdfe8"></a> `00bcdfe8` | `cb 04 00 54` | b.lt 0x00bce080 | `CONDITIONAL_JUMP`
<a id="insn-00bcdfec"></a> `00bcdfec` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00bcdff0"></a> `00bcdff0` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00bcdff4"></a> `00bcdff4` | `39 7f 40 92` | and x25,x25,#0xffffffff | `FALL_THROUGH`
<a id="insn-00bcdff8"></a> `00bcdff8` | `0a 00 00 14` | b 0x00bce020 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdffc"></a> `00bcdffc` | `7f 6b 38 78` | strh wzr,[x27, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bce000"></a> `00bce000` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce004"></a> `00bce004` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bce008"></a> `00bce008` | `d6 06 00 91` | add x22,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00bce00c"></a> `00bce00c` | `3f 03 16 eb` | cmp x25,x22 | `FALL_THROUGH`
<a id="insn-00bce010"></a> `00bce010` | `18 63 00 91` | add x24,x24,#0x18 | `FALL_THROUGH`
<a id="insn-00bce014"></a> `00bce014` | `48 0b 00 f9` | str x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bce018"></a> `00bce018` | `40 03 80 3d` | str q0,[x26] | `FALL_THROUGH`
<a id="insn-00bce01c"></a> `00bce01c` | `20 03 00 54` | b.eq 0x00bce080 | `CONDITIONAL_JUMP`
<a id="insn-00bce020"></a> `00bce020` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bce024"></a> `00bce024` | `3f 35 02 94` | bl 0x00c5b520 | `UNCONDITIONAL_CALL`
<a id="insn-00bce028"></a> `00bce028` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bce02c"></a> `00bce02c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce030"></a> `00bce030` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bce034"></a> `00bce034` | `e3 03 16 2a` | mov w3,w22 | `FALL_THROUGH`
<a id="insn-00bce038"></a> `00bce038` | `ff 25 e3 97` | bl 0x00497834 | `UNCONDITIONAL_CALL`
<a id="insn-00bce03c"></a> `00bce03c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bce040"></a> `00bce040` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00bce044"></a> `00bce044` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce048"></a> `00bce048` | `d2 34 02 94` | bl 0x00c5b390 | `UNCONDITIONAL_CALL`
<a id="insn-00bce04c"></a> `00bce04c` | `7b 02 40 f9` | ldr x27,[x19] | `FALL_THROUGH`
<a id="insn-00bce050"></a> `00bce050` | `7a 03 18 8b` | add x26,x27,x24 | `FALL_THROUGH`
<a id="insn-00bce054"></a> `00bce054` | `48 03 40 39` | ldrb w8,[x26] | `FALL_THROUGH`
<a id="insn-00bce058"></a> `00bce058` | `28 fd 07 36` | tbz w8,#0x0,0x00bcdffc | `CONDITIONAL_JUMP`
<a id="insn-00bce05c"></a> `00bce05c` | `48 0b 40 f9` | ldr x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bce060"></a> `00bce060` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bce064"></a> `00bce064` | `48 03 40 39` | ldrb w8,[x26] | `FALL_THROUGH`
<a id="insn-00bce068"></a> `00bce068` | `5f 07 00 f9` | str xzr,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bce06c"></a> `00bce06c` | `a8 fc 07 36` | tbz w8,#0x0,0x00bce000 | `CONDITIONAL_JUMP`
<a id="insn-00bce070"></a> `00bce070` | `40 0b 40 f9` | ldr x0,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bce074"></a> `00bce074` | `8f 27 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce078"></a> `00bce078` | `7f 6b 38 f8` | str xzr,[x27, x24, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bce07c"></a> `00bce07c` | `e1 ff ff 17` | b 0x00bce000 | `UNCONDITIONAL_JUMP`
<a id="insn-00bce080"></a> `00bce080` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bce084"></a> `00bce084` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bce088"></a> `00bce088` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bce08c"></a> `00bce08c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bce090"></a> `00bce090` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce094"></a> `00bce094` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00bce098"></a> `00bce098` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bce09c"></a> `00bce09c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bce0a0"></a> `00bce0a0` | `21 01 00 54` | b.ne 0x00bce0c4 | `CONDITIONAL_JUMP`
<a id="insn-00bce0a4"></a> `00bce0a4` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bce0a8"></a> `00bce0a8` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bce0ac"></a> `00bce0ac` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bce0b0"></a> `00bce0b0` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bce0b4"></a> `00bce0b4` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bce0b8"></a> `00bce0b8` | `fb 13 40 f9` | ldr x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce0bc"></a> `00bce0bc` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bce0c0"></a> `00bce0c0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bce0c4"></a> `00bce0c4` | `87 27 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdeb4`](#insn-00bcdeb4) 範囲 `[['00bcdeb4', '00bcdf03']]`
  - `CONDITIONAL_JUMP` [`00bcdf00`](#insn-00bcdf00) → [`00bcdf14`](#insn-00bcdf14)
  - `FALL_THROUGH` [`00bcdf00`](#insn-00bcdf00) → [`00bcdf04`](#insn-00bcdf04)
- ブロック [`00bcdf04`](#insn-00bcdf04) 範囲 `[['00bcdf04', '00bcdf07']]`
  - `CONDITIONAL_JUMP` [`00bcdf04`](#insn-00bcdf04) → [`00bcdf14`](#insn-00bcdf14)
  - `FALL_THROUGH` [`00bcdf04`](#insn-00bcdf04) → [`00bcdf08`](#insn-00bcdf08)
- ブロック [`00bcdf08`](#insn-00bcdf08) 範囲 `[['00bcdf08', '00bcdf13']]`
  - `FALL_THROUGH` [`00bcdf10`](#insn-00bcdf10) → [`00bcdf14`](#insn-00bcdf14)
- ブロック [`00bcdf14`](#insn-00bcdf14) 範囲 `[['00bcdf14', '00bcdf17']]`
  - `CONDITIONAL_JUMP` [`00bcdf14`](#insn-00bcdf14) → [`00bcdf94`](#insn-00bcdf94)
  - `FALL_THROUGH` [`00bcdf14`](#insn-00bcdf14) → [`00bcdf18`](#insn-00bcdf18)
- ブロック [`00bcdf18`](#insn-00bcdf18) 範囲 `[['00bcdf18', '00bcdf3b']]`
  - `CONDITIONAL_JUMP` [`00bcdf38`](#insn-00bcdf38) → [`00bce094`](#insn-00bce094)
  - `FALL_THROUGH` [`00bcdf38`](#insn-00bcdf38) → [`00bcdf3c`](#insn-00bcdf3c)
- ブロック [`00bcdf3c`](#insn-00bcdf3c) 範囲 `[['00bcdf3c', '00bcdf3f']]`
  - `CONDITIONAL_JUMP` [`00bcdf3c`](#insn-00bcdf3c) → [`00bce094`](#insn-00bce094)
  - `FALL_THROUGH` [`00bcdf3c`](#insn-00bcdf3c) → [`00bcdf40`](#insn-00bcdf40)
- ブロック [`00bcdf40`](#insn-00bcdf40) 範囲 `[['00bcdf40', '00bcdf47']]`
  - `FALL_THROUGH` [`00bcdf44`](#insn-00bcdf44) → [`00bcdf48`](#insn-00bcdf48)
- ブロック [`00bcdf48`](#insn-00bcdf48) 範囲 `[['00bcdf48', '00bcdf77']]`
  - `FALL_THROUGH` [`00bcdf74`](#insn-00bcdf74) → [`00bcdf78`](#insn-00bcdf78)
- ブロック [`00bcdf78`](#insn-00bcdf78) 範囲 `[['00bcdf78', '00bcdf7b']]`
  - `CONDITIONAL_JUMP` [`00bcdf78`](#insn-00bcdf78) → [`00bcdfa0`](#insn-00bcdfa0)
  - `FALL_THROUGH` [`00bcdf78`](#insn-00bcdf78) → [`00bcdf7c`](#insn-00bcdf7c)
- ブロック [`00bcdf7c`](#insn-00bcdf7c) 範囲 `[['00bcdf7c', '00bcdf8f']]`
  - `CONDITIONAL_JUMP` [`00bcdf8c`](#insn-00bcdf8c) → [`00bcdfec`](#insn-00bcdfec)
  - `FALL_THROUGH` [`00bcdf8c`](#insn-00bcdf8c) → [`00bcdf90`](#insn-00bcdf90)
- ブロック [`00bcdf90`](#insn-00bcdf90) 範囲 `[['00bcdf90', '00bcdf93']]`
  - `UNCONDITIONAL_JUMP` [`00bcdf90`](#insn-00bcdf90) → [`00bce080`](#insn-00bce080)
- ブロック [`00bcdf94`](#insn-00bcdf94) 範囲 `[['00bcdf94', '00bcdf9f']]`
  - `UNCONDITIONAL_JUMP` [`00bcdf9c`](#insn-00bcdf9c) → [`00bce094`](#insn-00bce094)
- ブロック [`00bcdfa0`](#insn-00bcdfa0) 範囲 `[['00bcdfa0', '00bcdfa3']]`
  - `CONDITIONAL_JUMP` [`00bcdfa0`](#insn-00bcdfa0) → [`00bcdfe4`](#insn-00bcdfe4)
  - `FALL_THROUGH` [`00bcdfa0`](#insn-00bcdfa0) → [`00bcdfa4`](#insn-00bcdfa4)
- ブロック [`00bcdfa4`](#insn-00bcdfa4) 範囲 `[['00bcdfa4', '00bcdfb3']]`
  - `CONDITIONAL_JUMP` [`00bcdfb0`](#insn-00bcdfb0) → [`00bcdfe0`](#insn-00bcdfe0)
  - `FALL_THROUGH` [`00bcdfb0`](#insn-00bcdfb0) → [`00bcdfb4`](#insn-00bcdfb4)
- ブロック [`00bcdfb4`](#insn-00bcdfb4) 範囲 `[['00bcdfb4', '00bcdfbf']]`
  - `CONDITIONAL_JUMP` [`00bcdfbc`](#insn-00bcdfbc) → [`00bcdfd4`](#insn-00bcdfd4)
  - `FALL_THROUGH` [`00bcdfbc`](#insn-00bcdfbc) → [`00bcdfc0`](#insn-00bcdfc0)
- ブロック [`00bcdfc0`](#insn-00bcdfc0) 範囲 `[['00bcdfc0', '00bcdfcb']]`
  - `CONDITIONAL_JUMP` [`00bcdfc8`](#insn-00bcdfc8) → [`00bcdfe0`](#insn-00bcdfe0)
  - `FALL_THROUGH` [`00bcdfc8`](#insn-00bcdfc8) → [`00bcdfcc`](#insn-00bcdfcc)
- ブロック [`00bcdfcc`](#insn-00bcdfcc) 範囲 `[['00bcdfcc', '00bcdfd3']]`
  - `CONDITIONAL_JUMP` [`00bcdfd0`](#insn-00bcdfd0) → [`00bcdfc0`](#insn-00bcdfc0)
  - `FALL_THROUGH` [`00bcdfd0`](#insn-00bcdfd0) → [`00bcdfd4`](#insn-00bcdfd4)
- ブロック [`00bcdfd4`](#insn-00bcdfd4) 範囲 `[['00bcdfd4', '00bcdfdf']]`
  - `UNCONDITIONAL_JUMP` [`00bcdfdc`](#insn-00bcdfdc) → [`00bcdfc0`](#insn-00bcdfc0)
- ブロック [`00bcdfe0`](#insn-00bcdfe0) 範囲 `[['00bcdfe0', '00bcdfe3']]`
  - `FALL_THROUGH` [`00bcdfe0`](#insn-00bcdfe0) → [`00bcdfe4`](#insn-00bcdfe4)
- ブロック [`00bcdfe4`](#insn-00bcdfe4) 範囲 `[['00bcdfe4', '00bcdfeb']]`
  - `CONDITIONAL_JUMP` [`00bcdfe8`](#insn-00bcdfe8) → [`00bce080`](#insn-00bce080)
  - `FALL_THROUGH` [`00bcdfe8`](#insn-00bcdfe8) → [`00bcdfec`](#insn-00bcdfec)
- ブロック [`00bcdfec`](#insn-00bcdfec) 範囲 `[['00bcdfec', '00bcdffb']]`
  - `UNCONDITIONAL_JUMP` [`00bcdff8`](#insn-00bcdff8) → [`00bce020`](#insn-00bce020)
- ブロック [`00bcdffc`](#insn-00bcdffc) 範囲 `[['00bcdffc', '00bcdfff']]`
  - `FALL_THROUGH` [`00bcdffc`](#insn-00bcdffc) → [`00bce000`](#insn-00bce000)
- ブロック [`00bce000`](#insn-00bce000) 範囲 `[['00bce000', '00bce01f']]`
  - `CONDITIONAL_JUMP` [`00bce01c`](#insn-00bce01c) → [`00bce080`](#insn-00bce080)
  - `FALL_THROUGH` [`00bce01c`](#insn-00bce01c) → [`00bce020`](#insn-00bce020)
- ブロック [`00bce020`](#insn-00bce020) 範囲 `[['00bce020', '00bce05b']]`
  - `CONDITIONAL_JUMP` [`00bce058`](#insn-00bce058) → [`00bcdffc`](#insn-00bcdffc)
  - `FALL_THROUGH` [`00bce058`](#insn-00bce058) → [`00bce05c`](#insn-00bce05c)
- ブロック [`00bce05c`](#insn-00bce05c) 範囲 `[['00bce05c', '00bce06f']]`
  - `CONDITIONAL_JUMP` [`00bce06c`](#insn-00bce06c) → [`00bce000`](#insn-00bce000)
  - `FALL_THROUGH` [`00bce06c`](#insn-00bce06c) → [`00bce070`](#insn-00bce070)
- ブロック [`00bce070`](#insn-00bce070) 範囲 `[['00bce070', '00bce077']]`
  - `FALL_THROUGH` [`00bce074`](#insn-00bce074) → [`00bce078`](#insn-00bce078)
- ブロック [`00bce078`](#insn-00bce078) 範囲 `[['00bce078', '00bce07f']]`
  - `UNCONDITIONAL_JUMP` [`00bce07c`](#insn-00bce07c) → [`00bce000`](#insn-00bce000)
- ブロック [`00bce080`](#insn-00bce080) 範囲 `[['00bce080', '00bce093']]`
  - `FALL_THROUGH` [`00bce090`](#insn-00bce090) → [`00bce094`](#insn-00bce094)
- ブロック [`00bce094`](#insn-00bce094) 範囲 `[['00bce094', '00bce09f']]`
  - `FALL_THROUGH` [`00bce09c`](#insn-00bce09c) → [`00bce0a0`](#insn-00bce0a0)
- ブロック [`00bce0a0`](#insn-00bce0a0) 範囲 `[['00bce0a0', '00bce0a3']]`
  - `CONDITIONAL_JUMP` [`00bce0a0`](#insn-00bce0a0) → [`00bce0c4`](#insn-00bce0c4)
  - `FALL_THROUGH` [`00bce0a0`](#insn-00bce0a0) → [`00bce0a4`](#insn-00bce0a4)
- ブロック [`00bce0a4`](#insn-00bce0a4) 範囲 `[['00bce0a4', '00bce0bf']]`
  - `FALL_THROUGH` [`00bce0bc`](#insn-00bce0bc) → [`00bce0c0`](#insn-00bce0c0)
- ブロック [`00bce0c0`](#insn-00bce0c0) 範囲 `[['00bce0c0', '00bce0c3']]`
- ブロック [`00bce0c4`](#insn-00bce0c4) 範囲 `[['00bce0c4', '00bce0c7']]`

## 命令位置別の参照

- [`00bcdeb8`](#insn-00bcdeb8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdebc`](#insn-00bcdebc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdec0`](#insn-00bcdec0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdec4`](#insn-00bcdec4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdec8`](#insn-00bcdec8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdecc`](#insn-00bcdecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdee8`](#insn-00bcdee8) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdef8`](#insn-00bcdef8) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf00`](#insn-00bcdf00) → [`00bcdf14`](#insn-00bcdf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf04`](#insn-00bcdf04) → [`00bcdf14`](#insn-00bcdf14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf0c`](#insn-00bcdf0c) → `002a0d25`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcdf10`](#insn-00bcdf10) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf14`](#insn-00bcdf14) → [`00bcdf94`](#insn-00bcdf94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf1c`](#insn-00bcdf1c) → `011267e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdf28`](#insn-00bcdf28) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf34`](#insn-00bcdf34) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf38`](#insn-00bcdf38) → [`00bce094`](#insn-00bce094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf3c`](#insn-00bcdf3c) → [`00bce094`](#insn-00bce094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf44`](#insn-00bcdf44) → [`00c5b520`](../00c5b/00c5b520.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b520` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf54`](#insn-00bcdf54) → [`005762b8`](../00576/005762b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005762b8` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf78`](#insn-00bcdf78) → [`00bcdfa0`](#insn-00bcdfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf84`](#insn-00bcdf84) → [`00c5d560`](../00c5d/00c5d560.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d560` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf8c`](#insn-00bcdf8c) → [`00bcdfec`](#insn-00bcdfec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf90`](#insn-00bcdf90) → [`00bce080`](#insn-00bce080) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf98`](#insn-00bcdf98) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf9c`](#insn-00bcdf9c) → [`00bce094`](#insn-00bce094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfa0`](#insn-00bcdfa0) → [`00bcdfe4`](#insn-00bcdfe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfb0`](#insn-00bcdfb0) → [`00bcdfe0`](#insn-00bcdfe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfbc`](#insn-00bcdfbc) → [`00bcdfd4`](#insn-00bcdfd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfc8`](#insn-00bcdfc8) → [`00bcdfe0`](#insn-00bcdfe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfd0`](#insn-00bcdfd0) → [`00bcdfc0`](#insn-00bcdfc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfd8`](#insn-00bcdfd8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfdc`](#insn-00bcdfdc) → [`00bcdfc0`](#insn-00bcdfc0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfe8`](#insn-00bcdfe8) → [`00bce080`](#insn-00bce080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdff8`](#insn-00bcdff8) → [`00bce020`](#insn-00bce020) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce000`](#insn-00bce000) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce004`](#insn-00bce004) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce01c`](#insn-00bce01c) → [`00bce080`](#insn-00bce080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce024`](#insn-00bce024) → [`00c5b520`](../00c5b/00c5b520.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b520` · 推定シンボル `None` · 推定型 `None`
- [`00bce038`](#insn-00bce038) → [`00497834`](../00497/00497834.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497834` · 推定シンボル `None` · 推定型 `None`
- [`00bce048`](#insn-00bce048) → [`00c5b390`](../00c5b/00c5b390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b390` · 推定シンボル `None` · 推定型 `None`
- [`00bce058`](#insn-00bce058) → [`00bcdffc`](#insn-00bcdffc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce06c`](#insn-00bce06c) → [`00bce000`](#insn-00bce000) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce074`](#insn-00bce074) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bce07c`](#insn-00bce07c) → [`00bce000`](#insn-00bce000) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce098`](#insn-00bce098) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0a0`](#insn-00bce0a0) → [`00bce0c4`](#insn-00bce0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0a4`](#insn-00bce0a4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0a8`](#insn-00bce0a8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0ac`](#insn-00bce0ac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0b0`](#insn-00bce0b0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0b4`](#insn-00bce0b4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0b8`](#insn-00bce0b8) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0c4`](#insn-00bce0c4) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdeb8`](#insn-00bcdeb8)

~~~json
{
  "source": "00bcdeb8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdebc`](#insn-00bcdebc)

~~~json
{
  "source": "00bcdebc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdec0`](#insn-00bcdec0)

~~~json
{
  "source": "00bcdec0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdec4`](#insn-00bcdec4)

~~~json
{
  "source": "00bcdec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdec8`](#insn-00bcdec8)

~~~json
{
  "source": "00bcdec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdecc`](#insn-00bcdecc)

~~~json
{
  "source": "00bcdecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdee8`](#insn-00bcdee8)

~~~json
{
  "source": "00bcdee8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdef8`](#insn-00bcdef8)

~~~json
{
  "source": "00bcdef8",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf00`](#insn-00bcdf00)

~~~json
{
  "source": "00bcdf00",
  "target": "00bcdf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf04`](#insn-00bcdf04)

~~~json
{
  "source": "00bcdf04",
  "target": "00bcdf14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf0c`](#insn-00bcdf0c)

~~~json
{
  "source": "00bcdf0c",
  "target": "002a0d25",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a0d25",
  "offset": 0,
  "size": 30,
  "datatype": "string",
  "bytes": "2173756363657373207c7c20726573756c7420213d206e756c6c70747200",
  "capture_start": "002a0d25",
  "capture_bytes": 30,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcdf10`](#insn-00bcdf10)

~~~json
{
  "source": "00bcdf10",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf14`](#insn-00bcdf14)

~~~json
{
  "source": "00bcdf14",
  "target": "00bcdf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf1c`](#insn-00bcdf1c)

~~~json
{
  "source": "00bcdf1c",
  "target": "011267e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011267e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdf28`](#insn-00bcdf28)

~~~json
{
  "source": "00bcdf28",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf34`](#insn-00bcdf34)

~~~json
{
  "source": "00bcdf34",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf38`](#insn-00bcdf38)

~~~json
{
  "source": "00bcdf38",
  "target": "00bce094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf3c`](#insn-00bcdf3c)

~~~json
{
  "source": "00bcdf3c",
  "target": "00bce094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf44`](#insn-00bcdf44)

~~~json
{
  "source": "00bcdf44",
  "target": "00c5b520",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf54`](#insn-00bcdf54)

~~~json
{
  "source": "00bcdf54",
  "target": "005762b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf78`](#insn-00bcdf78)

~~~json
{
  "source": "00bcdf78",
  "target": "00bcdfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf84`](#insn-00bcdf84)

~~~json
{
  "source": "00bcdf84",
  "target": "00c5d560",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf8c`](#insn-00bcdf8c)

~~~json
{
  "source": "00bcdf8c",
  "target": "00bcdfec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf90`](#insn-00bcdf90)

~~~json
{
  "source": "00bcdf90",
  "target": "00bce080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf98`](#insn-00bcdf98)

~~~json
{
  "source": "00bcdf98",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdf9c`](#insn-00bcdf9c)

~~~json
{
  "source": "00bcdf9c",
  "target": "00bce094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfa0`](#insn-00bcdfa0)

~~~json
{
  "source": "00bcdfa0",
  "target": "00bcdfe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfb0`](#insn-00bcdfb0)

~~~json
{
  "source": "00bcdfb0",
  "target": "00bcdfe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfbc`](#insn-00bcdfbc)

~~~json
{
  "source": "00bcdfbc",
  "target": "00bcdfd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfc8`](#insn-00bcdfc8)

~~~json
{
  "source": "00bcdfc8",
  "target": "00bcdfe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfd0`](#insn-00bcdfd0)

~~~json
{
  "source": "00bcdfd0",
  "target": "00bcdfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfd8`](#insn-00bcdfd8)

~~~json
{
  "source": "00bcdfd8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdfdc`](#insn-00bcdfdc)

~~~json
{
  "source": "00bcdfdc",
  "target": "00bcdfc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfe8`](#insn-00bcdfe8)

~~~json
{
  "source": "00bcdfe8",
  "target": "00bce080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdff8`](#insn-00bcdff8)

~~~json
{
  "source": "00bcdff8",
  "target": "00bce020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce000`](#insn-00bce000)

~~~json
{
  "source": "00bce000",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce004`](#insn-00bce004)

~~~json
{
  "source": "00bce004",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce01c`](#insn-00bce01c)

~~~json
{
  "source": "00bce01c",
  "target": "00bce080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce024`](#insn-00bce024)

~~~json
{
  "source": "00bce024",
  "target": "00c5b520",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce038`](#insn-00bce038)

~~~json
{
  "source": "00bce038",
  "target": "00497834",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce048`](#insn-00bce048)

~~~json
{
  "source": "00bce048",
  "target": "00c5b390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce058`](#insn-00bce058)

~~~json
{
  "source": "00bce058",
  "target": "00bcdffc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce06c`](#insn-00bce06c)

~~~json
{
  "source": "00bce06c",
  "target": "00bce000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce074`](#insn-00bce074)

~~~json
{
  "source": "00bce074",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce07c`](#insn-00bce07c)

~~~json
{
  "source": "00bce07c",
  "target": "00bce000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce098`](#insn-00bce098)

~~~json
{
  "source": "00bce098",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0a0`](#insn-00bce0a0)

~~~json
{
  "source": "00bce0a0",
  "target": "00bce0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0a4`](#insn-00bce0a4)

~~~json
{
  "source": "00bce0a4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0a8`](#insn-00bce0a8)

~~~json
{
  "source": "00bce0a8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0ac`](#insn-00bce0ac)

~~~json
{
  "source": "00bce0ac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0b0`](#insn-00bce0b0)

~~~json
{
  "source": "00bce0b0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0b4`](#insn-00bce0b4)

~~~json
{
  "source": "00bce0b4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0b8`](#insn-00bce0b8)

~~~json
{
  "source": "00bce0b8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0c4`](#insn-00bce0c4)

~~~json
{
  "source": "00bce0c4",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
