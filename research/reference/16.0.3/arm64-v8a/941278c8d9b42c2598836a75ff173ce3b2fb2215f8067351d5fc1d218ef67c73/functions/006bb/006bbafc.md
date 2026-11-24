# 006bbafc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `006bb74c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/006bb/006bb74c.md) · 移動量 `+0x3b0`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0004.md#compare-a29ba5fa2b002eba3034cfce0e9bdd2d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "006bbafc",
  "name": "FUN_006bbafc",
  "size": 532,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e3cdf8cdf387af11326651d34dd3f91097d7d24ffc1b16ad928f2c28f9e61378",
  "source_text_sha256": "e3cdf8cdf387af11326651d34dd3f91097d7d24ffc1b16ad928f2c28f9e61378",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "006bbafc",
        "006bbd0f"
      ]
    ],
    "bytes_sha256": "69503a5e132c7fa22cda17f4b567bf3b6c29c637e297a07ee5897e8e6f578966",
    "instruction_count": 133,
    "instruction_bytes": 532,
    "body_bytes": 532,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ae027c](../00ae0/00ae027c.md)

## 呼び出し先

- [0043bf04](../0043b/0043bf04.md)
- [008524fc](../00852/008524fc.md)
- [00c58f30](../00c58/00c58f30.md)
- [00c59130](../00c59/00c59130.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4583 bytes

~~~c

bool FUN_006bbafc(int param_1,int param_2)

{
  ulong uVar1;
  long lVar2;
  undefined8 *puVar3;
  long *plVar4;
  ulong uVar5;
  undefined8 *puVar6;
  long lVar7;
  undefined8 *puVar8;
  undefined8 *puVar9;
  
  lVar2 = FUN_008524fc();
  plVar4 = *(long **)((long)&__DT_JMPREL[0xfc].r_offset + lVar2);
  do {
    if (plVar4 == (long *)0x0) {
      return false;
    }
    if (*(int *)((long)plVar4 + 0x1c) <= param_1) {
      if (param_1 <= *(int *)((long)plVar4 + 0x1c)) {
        uVar1 = 0;
        do {
          uVar5 = uVar1;
          lVar2 = FUN_008524fc();
          puVar6 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar2);
          if (puVar6 == (undefined8 *)0x0) {
            puVar8 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar2);
            puVar9 = puVar8;
          }
          else {
            do {
                    /* try { // try from 006bbbd8 to 007bc193 has its CatchHandler @ 006bc2cc */
              while (puVar3 = puVar6, puVar8 = puVar3, *(int *)((long)puVar3 + 0x1c) <= param_1) {
                if (param_1 <= *(int *)((long)puVar3 + 0x1c)) goto code_r0x006bbc58;
                puVar6 = (undefined8 *)puVar3[1];
                if ((undefined8 *)puVar3[1] == (undefined8 *)0x0) {
                  puVar9 = puVar3 + 1;
                  goto LAB_006bbbf8;
                }
              }
                    /* try { // try from 006bbbcc to 007bbbd3 has its CatchHandler @ 006bc2c8 */
              puVar6 = (undefined8 *)*puVar3;
              puVar9 = puVar3;
            } while ((undefined8 *)*puVar3 != (undefined8 *)0x0);
          }
LAB_006bbbf8:
          puVar3 = (undefined8 *)_Znwm(0x290);
          *(int *)((long)puVar3 + 0x1c) = param_1;
          memset(puVar3 + 4,0,0x26c);
          *puVar3 = 0;
          puVar3[1] = 0;
          puVar3[2] = puVar8;
          *puVar9 = puVar3;
          lVar7 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar2);
          puVar6 = puVar3;
          if (lVar7 != 0) {
            *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar2) = lVar7;
            puVar6 = (undefined8 *)*puVar9;
          }
          FUN_0043bf04(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar2),puVar6);
          *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar2) =
               *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar2) + 1;
code_r0x006bbc58:
          if (*(int *)((long)puVar3 + uVar5 * 0x38 + 0x24) == param_2) {
            lVar2 = FUN_008524fc();
            puVar6 = *(undefined8 **)((long)&__DT_JMPREL[0xfc].r_offset + lVar2);
            if (puVar6 == (undefined8 *)0x0) {
              puVar8 = (undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar2);
              puVar9 = puVar8;
            }
            else {
              do {
                while (puVar3 = puVar6, puVar8 = puVar3, *(int *)((long)puVar3 + 0x1c) <= param_1) {
                  if (param_1 <= *(int *)((long)puVar3 + 0x1c)) goto code_r0x006bbb90;
                  puVar6 = (undefined8 *)puVar3[1];
                  if ((undefined8 *)puVar3[1] == (undefined8 *)0x0) {
                    puVar9 = puVar3 + 1;
                    goto LAB_006bbcb0;
                  }
                }
                puVar6 = (undefined8 *)*puVar3;
                puVar9 = puVar3;
              } while ((undefined8 *)*puVar3 != (undefined8 *)0x0);
            }
LAB_006bbcb0:
            puVar3 = (undefined8 *)_Znwm(0x290);
            *(int *)((long)puVar3 + 0x1c) = param_1;
            memset(puVar3 + 4,0,0x26c);
            *puVar3 = 0;
            puVar3[1] = 0;
            puVar3[2] = puVar8;
            *puVar9 = puVar3;
            lVar7 = **(long **)((long)&__DT_JMPREL[0xfb].r_addend + lVar2);
            puVar6 = puVar3;
            if (lVar7 != 0) {
              *(long *)((long)&__DT_JMPREL[0xfb].r_addend + lVar2) = lVar7;
              puVar6 = (undefined8 *)*puVar9;
            }
            FUN_0043bf04(*(undefined8 *)((long)&__DT_JMPREL[0xfc].r_offset + lVar2),puVar6);
            *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar2) =
                 *(long *)((long)&__DT_JMPREL[0xfc].r_info + lVar2) + 1;
code_r0x006bbb90:
            if (*(int *)(puVar3 + uVar5 * 7 + 0xb) == 1) {
              return true;
            }
          }
          uVar1 = uVar5 + 1;
          if (uVar5 + 1 == 0xb) {
            return uVar5 < 10;
          }
        } while( true );
      }
                    /* try { // try from 006bbb64 to 007bbb77 has its CatchHandler @ 006bc2a8 */
      plVar4 = plVar4 + 1;
    }
    plVar4 = (long *)*plVar4;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-006bbafc"></a> `006bbafc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-006bbb00"></a> `006bbb00` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006bbb04"></a> `006bbb04` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006bbb08"></a> `006bbb08` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006bbb0c"></a> `006bbb0c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006bbb10"></a> `006bbb10` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-006bbb14"></a> `006bbb14` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-006bbb18"></a> `006bbb18` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-006bbb1c"></a> `006bbb1c` | `78 5a 06 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-006bbb20"></a> `006bbb20` | `08 47 9a 52` | mov w8,#0xd238 | `FALL_THROUGH`
<a id="insn-006bbb24"></a> `006bbb24` | `68 04 a0 72` | movk w8,#0x23, LSL #16 | `FALL_THROUGH`
<a id="insn-006bbb28"></a> `006bbb28` | `08 68 68 f8` | ldr x8,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-006bbb2c"></a> `006bbb2c` | `48 01 00 b5` | cbnz x8,0x006bbb54 | `CONDITIONAL_JUMP`
<a id="insn-006bbb30"></a> `006bbb30` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-006bbb34"></a> `006bbb34` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-006bbb38"></a> `006bbb38` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-006bbb3c"></a> `006bbb3c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-006bbb40"></a> `006bbb40` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-006bbb44"></a> `006bbb44` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-006bbb48"></a> `006bbb48` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-006bbb4c"></a> `006bbb4c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-006bbb50"></a> `006bbb50` | `08 ff ff b4` | cbz x8,0x006bbb30 | `CONDITIONAL_JUMP`
<a id="insn-006bbb54"></a> `006bbb54` | `09 1d 40 b9` | ldr w9,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-006bbb58"></a> `006bbb58` | `3f 01 14 6b` | cmp w9,w20 | `FALL_THROUGH`
<a id="insn-006bbb5c"></a> `006bbb5c` | `8c ff ff 54` | b.gt 0x006bbb4c | `CONDITIONAL_JUMP`
<a id="insn-006bbb60"></a> `006bbb60` | `6a 00 00 54` | b.ge 0x006bbb6c | `CONDITIONAL_JUMP`
<a id="insn-006bbb64"></a> `006bbb64` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-006bbb68"></a> `006bbb68` | `f9 ff ff 17` | b 0x006bbb4c | `UNCONDITIONAL_JUMP`
<a id="insn-006bbb6c"></a> `006bbb6c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-006bbb70"></a> `006bbb70` | `16 07 80 52` | mov w22,#0x38 | `FALL_THROUGH`
<a id="insn-006bbb74"></a> `006bbb74` | `0e 00 00 14` | b 0x006bbbac | `UNCONDITIONAL_JUMP`
<a id="insn-006bbb78"></a> `006bbb78` | `00 1f 41 f9` | ldr x0,[x24, #0x238] | `FALL_THROUGH`
<a id="insn-006bbb7c"></a> `006bbb7c` | `e2 00 f6 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-006bbb80"></a> `006bbb80` | `08 23 41 f9` | ldr x8,[x24, #0x240] | `FALL_THROUGH`
<a id="insn-006bbb84"></a> `006bbb84` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006bbb88"></a> `006bbb88` | `08 23 01 f9` | str x8,[x24, #0x240] | `FALL_THROUGH`
<a id="insn-006bbb8c"></a> `006bbb8c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-006bbb90"></a> `006bbb90` | `e8 56 16 9b` | madd x8,x23,x22,x21 | `FALL_THROUGH`
<a id="insn-006bbb94"></a> `006bbb94` | `08 59 40 b9` | ldr w8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-006bbb98"></a> `006bbb98` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-006bbb9c"></a> `006bbb9c` | `60 0b 00 54` | b.eq 0x006bbd08 | `CONDITIONAL_JUMP`
<a id="insn-006bbba0"></a> `006bbba0` | `e8 06 00 91` | add x8,x23,#0x1 | `FALL_THROUGH`
<a id="insn-006bbba4"></a> `006bbba4` | `1f 2d 00 f1` | cmp x8,#0xb | `FALL_THROUGH`
<a id="insn-006bbba8"></a> `006bbba8` | `a0 0a 00 54` | b.eq 0x006bbcfc | `CONDITIONAL_JUMP`
<a id="insn-006bbbac"></a> `006bbbac` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-006bbbb0"></a> `006bbbb0` | `53 5a 06 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-006bbbb4"></a> `006bbbb4` | `18 f4 48 91` | add x24,x0,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-006bbbb8"></a> `006bbbb8` | `08 1f 41 f9` | ldr x8,[x24, #0x238] | `FALL_THROUGH`
<a id="insn-006bbbbc"></a> `006bbbbc` | `e8 00 00 b5` | cbnz x8,0x006bbbd8 | `CONDITIONAL_JUMP`
<a id="insn-006bbbc0"></a> `006bbbc0` | `19 e3 08 91` | add x25,x24,#0x238 | `FALL_THROUGH`
<a id="insn-006bbbc4"></a> `006bbbc4` | `f5 03 19 aa` | mov x21,x25 | `FALL_THROUGH`
<a id="insn-006bbbc8"></a> `006bbbc8` | `0c 00 00 14` | b 0x006bbbf8 | `UNCONDITIONAL_JUMP`
<a id="insn-006bbbcc"></a> `006bbbcc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-006bbbd0"></a> `006bbbd0` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-006bbbd4"></a> `006bbbd4` | `28 01 00 b4` | cbz x8,0x006bbbf8 | `CONDITIONAL_JUMP`
<a id="insn-006bbbd8"></a> `006bbbd8` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-006bbbdc"></a> `006bbbdc` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-006bbbe0"></a> `006bbbe0` | `1f 01 14 6b` | cmp w8,w20 | `FALL_THROUGH`
<a id="insn-006bbbe4"></a> `006bbbe4` | `4c ff ff 54` | b.gt 0x006bbbcc | `CONDITIONAL_JUMP`
<a id="insn-006bbbe8"></a> `006bbbe8` | `6a 03 00 54` | b.ge 0x006bbc54 | `CONDITIONAL_JUMP`
<a id="insn-006bbbec"></a> `006bbbec` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-006bbbf0"></a> `006bbbf0` | `48 ff ff b5` | cbnz x8,0x006bbbd8 | `CONDITIONAL_JUMP`
<a id="insn-006bbbf4"></a> `006bbbf4` | `b9 22 00 91` | add x25,x21,#0x8 | `FALL_THROUGH`
<a id="insn-006bbbf8"></a> `006bbbf8` | `00 52 80 52` | mov w0,#0x290 | `FALL_THROUGH`
<a id="insn-006bbbfc"></a> `006bbbfc` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-006bbc00"></a> `006bbc00` | `cc 74 16 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-006bbc04"></a> `006bbc04` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-006bbc08"></a> `006bbc08` | `14 1c 00 b9` | str w20,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-006bbc0c"></a> `006bbc0c` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-006bbc10"></a> `006bbc10` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006bbc14"></a> `006bbc14` | `82 4d 80 52` | mov w2,#0x26c | `FALL_THROUGH`
<a id="insn-006bbc18"></a> `006bbc18` | `46 75 16 94` | bl 0x00c59130 | `UNCONDITIONAL_CALL`
<a id="insn-006bbc1c"></a> `006bbc1c` | `bf 7e 00 a9` | stp xzr,xzr,[x21] | `FALL_THROUGH`
<a id="insn-006bbc20"></a> `006bbc20` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-006bbc24"></a> `006bbc24` | `ba 0a 00 f9` | str x26,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-006bbc28"></a> `006bbc28` | `35 03 00 f9` | str x21,[x25] | `FALL_THROUGH`
<a id="insn-006bbc2c"></a> `006bbc2c` | `08 1b 41 f9` | ldr x8,[x24, #0x230] | `FALL_THROUGH`
<a id="insn-006bbc30"></a> `006bbc30` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-006bbc34"></a> `006bbc34` | `68 00 00 b4` | cbz x8,0x006bbc40 | `CONDITIONAL_JUMP`
<a id="insn-006bbc38"></a> `006bbc38` | `08 1b 01 f9` | str x8,[x24, #0x230] | `FALL_THROUGH`
<a id="insn-006bbc3c"></a> `006bbc3c` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-006bbc40"></a> `006bbc40` | `00 1f 41 f9` | ldr x0,[x24, #0x238] | `FALL_THROUGH`
<a id="insn-006bbc44"></a> `006bbc44` | `b0 00 f6 97` | bl 0x0043bf04 | `UNCONDITIONAL_CALL`
<a id="insn-006bbc48"></a> `006bbc48` | `08 23 41 f9` | ldr x8,[x24, #0x240] | `FALL_THROUGH`
<a id="insn-006bbc4c"></a> `006bbc4c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-006bbc50"></a> `006bbc50` | `08 23 01 f9` | str x8,[x24, #0x240] | `FALL_THROUGH`
<a id="insn-006bbc54"></a> `006bbc54` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-006bbc58"></a> `006bbc58` | `e8 56 16 9b` | madd x8,x23,x22,x21 | `FALL_THROUGH`
<a id="insn-006bbc5c"></a> `006bbc5c` | `08 25 40 b9` | ldr w8,[x8, #0x24] | `FALL_THROUGH`
<a id="insn-006bbc60"></a> `006bbc60` | `1f 01 13 6b` | cmp w8,w19 | `FALL_THROUGH`
<a id="insn-006bbc64"></a> `006bbc64` | `e1 f9 ff 54` | b.ne 0x006bbba0 | `CONDITIONAL_JUMP`
<a id="insn-006bbc68"></a> `006bbc68` | `25 5a 06 94` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-006bbc6c"></a> `006bbc6c` | `18 f4 48 91` | add x24,x0,#0x23d, LSL #12 | `FALL_THROUGH`
<a id="insn-006bbc70"></a> `006bbc70` | `08 1f 41 f9` | ldr x8,[x24, #0x238] | `FALL_THROUGH`
<a id="insn-006bbc74"></a> `006bbc74` | `e8 00 00 b5` | cbnz x8,0x006bbc90 | `CONDITIONAL_JUMP`
<a id="insn-006bbc78"></a> `006bbc78` | `19 e3 08 91` | add x25,x24,#0x238 | `FALL_THROUGH`
<a id="insn-006bbc7c"></a> `006bbc7c` | `f5 03 19 aa` | mov x21,x25 | `FALL_THROUGH`
<a id="insn-006bbc80"></a> `006bbc80` | `0c 00 00 14` | b 0x006bbcb0 | `UNCONDITIONAL_JUMP`
<a id="insn-006bbc84"></a> `006bbc84` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-006bbc88"></a> `006bbc88` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-006bbc8c"></a> `006bbc8c` | `28 01 00 b4` | cbz x8,0x006bbcb0 | `CONDITIONAL_JUMP`
<a id="insn-006bbc90"></a> `006bbc90` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-006bbc94"></a> `006bbc94` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-006bbc98"></a> `006bbc98` | `1f 01 14 6b` | cmp w8,w20 | `FALL_THROUGH`
<a id="insn-006bbc9c"></a> `006bbc9c` | `4c ff ff 54` | b.gt 0x006bbc84 | `CONDITIONAL_JUMP`
<a id="insn-006bbca0"></a> `006bbca0` | `6a f7 ff 54` | b.ge 0x006bbb8c | `CONDITIONAL_JUMP`
<a id="insn-006bbca4"></a> `006bbca4` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-006bbca8"></a> `006bbca8` | `48 ff ff b5` | cbnz x8,0x006bbc90 | `CONDITIONAL_JUMP`
<a id="insn-006bbcac"></a> `006bbcac` | `b9 22 00 91` | add x25,x21,#0x8 | `FALL_THROUGH`
<a id="insn-006bbcb0"></a> `006bbcb0` | `00 52 80 52` | mov w0,#0x290 | `FALL_THROUGH`
<a id="insn-006bbcb4"></a> `006bbcb4` | `fa 03 15 aa` | mov x26,x21 | `FALL_THROUGH`
<a id="insn-006bbcb8"></a> `006bbcb8` | `9e 74 16 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-006bbcbc"></a> `006bbcbc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-006bbcc0"></a> `006bbcc0` | `14 1c 00 b9` | str w20,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-006bbcc4"></a> `006bbcc4` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-006bbcc8"></a> `006bbcc8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-006bbccc"></a> `006bbccc` | `82 4d 80 52` | mov w2,#0x26c | `FALL_THROUGH`
<a id="insn-006bbcd0"></a> `006bbcd0` | `18 75 16 94` | bl 0x00c59130 | `UNCONDITIONAL_CALL`
<a id="insn-006bbcd4"></a> `006bbcd4` | `bf 7e 00 a9` | stp xzr,xzr,[x21] | `FALL_THROUGH`
<a id="insn-006bbcd8"></a> `006bbcd8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-006bbcdc"></a> `006bbcdc` | `ba 0a 00 f9` | str x26,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-006bbce0"></a> `006bbce0` | `35 03 00 f9` | str x21,[x25] | `FALL_THROUGH`
<a id="insn-006bbce4"></a> `006bbce4` | `08 1b 41 f9` | ldr x8,[x24, #0x230] | `FALL_THROUGH`
<a id="insn-006bbce8"></a> `006bbce8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-006bbcec"></a> `006bbcec` | `68 f4 ff b4` | cbz x8,0x006bbb78 | `CONDITIONAL_JUMP`
<a id="insn-006bbcf0"></a> `006bbcf0` | `08 1b 01 f9` | str x8,[x24, #0x230] | `FALL_THROUGH`
<a id="insn-006bbcf4"></a> `006bbcf4` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-006bbcf8"></a> `006bbcf8` | `a0 ff ff 17` | b 0x006bbb78 | `UNCONDITIONAL_JUMP`
<a id="insn-006bbcfc"></a> `006bbcfc` | `ff 2a 00 f1` | cmp x23,#0xa | `FALL_THROUGH`
<a id="insn-006bbd00"></a> `006bbd00` | `e0 27 9f 1a` | cset w0,cc | `FALL_THROUGH`
<a id="insn-006bbd04"></a> `006bbd04` | `8c ff ff 17` | b 0x006bbb34 | `UNCONDITIONAL_JUMP`
<a id="insn-006bbd08"></a> `006bbd08` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-006bbd0c"></a> `006bbd0c` | `8a ff ff 17` | b 0x006bbb34 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`006bbafc`](#insn-006bbafc) 範囲 `[['006bbafc', '006bbb2f']]`
  - `CONDITIONAL_JUMP` [`006bbb2c`](#insn-006bbb2c) → [`006bbb54`](#insn-006bbb54)
  - `FALL_THROUGH` [`006bbb2c`](#insn-006bbb2c) → [`006bbb30`](#insn-006bbb30)
- ブロック [`006bbb30`](#insn-006bbb30) 範囲 `[['006bbb30', '006bbb33']]`
  - `FALL_THROUGH` [`006bbb30`](#insn-006bbb30) → [`006bbb34`](#insn-006bbb34)
- ブロック [`006bbb34`](#insn-006bbb34) 範囲 `[['006bbb34', '006bbb4b']]`
- ブロック [`006bbb4c`](#insn-006bbb4c) 範囲 `[['006bbb4c', '006bbb53']]`
  - `CONDITIONAL_JUMP` [`006bbb50`](#insn-006bbb50) → [`006bbb30`](#insn-006bbb30)
  - `FALL_THROUGH` [`006bbb50`](#insn-006bbb50) → [`006bbb54`](#insn-006bbb54)
- ブロック [`006bbb54`](#insn-006bbb54) 範囲 `[['006bbb54', '006bbb5f']]`
  - `CONDITIONAL_JUMP` [`006bbb5c`](#insn-006bbb5c) → [`006bbb4c`](#insn-006bbb4c)
  - `FALL_THROUGH` [`006bbb5c`](#insn-006bbb5c) → [`006bbb60`](#insn-006bbb60)
- ブロック [`006bbb60`](#insn-006bbb60) 範囲 `[['006bbb60', '006bbb63']]`
  - `CONDITIONAL_JUMP` [`006bbb60`](#insn-006bbb60) → [`006bbb6c`](#insn-006bbb6c)
  - `FALL_THROUGH` [`006bbb60`](#insn-006bbb60) → [`006bbb64`](#insn-006bbb64)
- ブロック [`006bbb64`](#insn-006bbb64) 範囲 `[['006bbb64', '006bbb6b']]`
  - `UNCONDITIONAL_JUMP` [`006bbb68`](#insn-006bbb68) → [`006bbb4c`](#insn-006bbb4c)
- ブロック [`006bbb6c`](#insn-006bbb6c) 範囲 `[['006bbb6c', '006bbb77']]`
  - `UNCONDITIONAL_JUMP` [`006bbb74`](#insn-006bbb74) → [`006bbbac`](#insn-006bbbac)
- ブロック [`006bbb78`](#insn-006bbb78) 範囲 `[['006bbb78', '006bbb8b']]`
  - `FALL_THROUGH` [`006bbb88`](#insn-006bbb88) → [`006bbb8c`](#insn-006bbb8c)
- ブロック [`006bbb8c`](#insn-006bbb8c) 範囲 `[['006bbb8c', '006bbb9f']]`
  - `CONDITIONAL_JUMP` [`006bbb9c`](#insn-006bbb9c) → [`006bbd08`](#insn-006bbd08)
  - `FALL_THROUGH` [`006bbb9c`](#insn-006bbb9c) → [`006bbba0`](#insn-006bbba0)
- ブロック [`006bbba0`](#insn-006bbba0) 範囲 `[['006bbba0', '006bbbab']]`
  - `CONDITIONAL_JUMP` [`006bbba8`](#insn-006bbba8) → [`006bbcfc`](#insn-006bbcfc)
  - `FALL_THROUGH` [`006bbba8`](#insn-006bbba8) → [`006bbbac`](#insn-006bbbac)
- ブロック [`006bbbac`](#insn-006bbbac) 範囲 `[['006bbbac', '006bbbbf']]`
  - `CONDITIONAL_JUMP` [`006bbbbc`](#insn-006bbbbc) → [`006bbbd8`](#insn-006bbbd8)
  - `FALL_THROUGH` [`006bbbbc`](#insn-006bbbbc) → [`006bbbc0`](#insn-006bbbc0)
- ブロック [`006bbbc0`](#insn-006bbbc0) 範囲 `[['006bbbc0', '006bbbcb']]`
  - `UNCONDITIONAL_JUMP` [`006bbbc8`](#insn-006bbbc8) → [`006bbbf8`](#insn-006bbbf8)
- ブロック [`006bbbcc`](#insn-006bbbcc) 範囲 `[['006bbbcc', '006bbbd7']]`
  - `CONDITIONAL_JUMP` [`006bbbd4`](#insn-006bbbd4) → [`006bbbf8`](#insn-006bbbf8)
  - `FALL_THROUGH` [`006bbbd4`](#insn-006bbbd4) → [`006bbbd8`](#insn-006bbbd8)
- ブロック [`006bbbd8`](#insn-006bbbd8) 範囲 `[['006bbbd8', '006bbbe7']]`
  - `CONDITIONAL_JUMP` [`006bbbe4`](#insn-006bbbe4) → [`006bbbcc`](#insn-006bbbcc)
  - `FALL_THROUGH` [`006bbbe4`](#insn-006bbbe4) → [`006bbbe8`](#insn-006bbbe8)
- ブロック [`006bbbe8`](#insn-006bbbe8) 範囲 `[['006bbbe8', '006bbbeb']]`
  - `CONDITIONAL_JUMP` [`006bbbe8`](#insn-006bbbe8) → [`006bbc54`](#insn-006bbc54)
  - `FALL_THROUGH` [`006bbbe8`](#insn-006bbbe8) → [`006bbbec`](#insn-006bbbec)
- ブロック [`006bbbec`](#insn-006bbbec) 範囲 `[['006bbbec', '006bbbf3']]`
  - `CONDITIONAL_JUMP` [`006bbbf0`](#insn-006bbbf0) → [`006bbbd8`](#insn-006bbbd8)
  - `FALL_THROUGH` [`006bbbf0`](#insn-006bbbf0) → [`006bbbf4`](#insn-006bbbf4)
- ブロック [`006bbbf4`](#insn-006bbbf4) 範囲 `[['006bbbf4', '006bbbf7']]`
  - `FALL_THROUGH` [`006bbbf4`](#insn-006bbbf4) → [`006bbbf8`](#insn-006bbbf8)
- ブロック [`006bbbf8`](#insn-006bbbf8) 範囲 `[['006bbbf8', '006bbc37']]`
  - `CONDITIONAL_JUMP` [`006bbc34`](#insn-006bbc34) → [`006bbc40`](#insn-006bbc40)
  - `FALL_THROUGH` [`006bbc34`](#insn-006bbc34) → [`006bbc38`](#insn-006bbc38)
- ブロック [`006bbc38`](#insn-006bbc38) 範囲 `[['006bbc38', '006bbc3f']]`
  - `FALL_THROUGH` [`006bbc3c`](#insn-006bbc3c) → [`006bbc40`](#insn-006bbc40)
- ブロック [`006bbc40`](#insn-006bbc40) 範囲 `[['006bbc40', '006bbc53']]`
  - `FALL_THROUGH` [`006bbc50`](#insn-006bbc50) → [`006bbc54`](#insn-006bbc54)
- ブロック [`006bbc54`](#insn-006bbc54) 範囲 `[['006bbc54', '006bbc67']]`
  - `CONDITIONAL_JUMP` [`006bbc64`](#insn-006bbc64) → [`006bbba0`](#insn-006bbba0)
  - `FALL_THROUGH` [`006bbc64`](#insn-006bbc64) → [`006bbc68`](#insn-006bbc68)
- ブロック [`006bbc68`](#insn-006bbc68) 範囲 `[['006bbc68', '006bbc77']]`
  - `CONDITIONAL_JUMP` [`006bbc74`](#insn-006bbc74) → [`006bbc90`](#insn-006bbc90)
  - `FALL_THROUGH` [`006bbc74`](#insn-006bbc74) → [`006bbc78`](#insn-006bbc78)
- ブロック [`006bbc78`](#insn-006bbc78) 範囲 `[['006bbc78', '006bbc83']]`
  - `UNCONDITIONAL_JUMP` [`006bbc80`](#insn-006bbc80) → [`006bbcb0`](#insn-006bbcb0)
- ブロック [`006bbc84`](#insn-006bbc84) 範囲 `[['006bbc84', '006bbc8f']]`
  - `CONDITIONAL_JUMP` [`006bbc8c`](#insn-006bbc8c) → [`006bbcb0`](#insn-006bbcb0)
  - `FALL_THROUGH` [`006bbc8c`](#insn-006bbc8c) → [`006bbc90`](#insn-006bbc90)
- ブロック [`006bbc90`](#insn-006bbc90) 範囲 `[['006bbc90', '006bbc9f']]`
  - `CONDITIONAL_JUMP` [`006bbc9c`](#insn-006bbc9c) → [`006bbc84`](#insn-006bbc84)
  - `FALL_THROUGH` [`006bbc9c`](#insn-006bbc9c) → [`006bbca0`](#insn-006bbca0)
- ブロック [`006bbca0`](#insn-006bbca0) 範囲 `[['006bbca0', '006bbca3']]`
  - `CONDITIONAL_JUMP` [`006bbca0`](#insn-006bbca0) → [`006bbb8c`](#insn-006bbb8c)
  - `FALL_THROUGH` [`006bbca0`](#insn-006bbca0) → [`006bbca4`](#insn-006bbca4)
- ブロック [`006bbca4`](#insn-006bbca4) 範囲 `[['006bbca4', '006bbcab']]`
  - `CONDITIONAL_JUMP` [`006bbca8`](#insn-006bbca8) → [`006bbc90`](#insn-006bbc90)
  - `FALL_THROUGH` [`006bbca8`](#insn-006bbca8) → [`006bbcac`](#insn-006bbcac)
- ブロック [`006bbcac`](#insn-006bbcac) 範囲 `[['006bbcac', '006bbcaf']]`
  - `FALL_THROUGH` [`006bbcac`](#insn-006bbcac) → [`006bbcb0`](#insn-006bbcb0)
- ブロック [`006bbcb0`](#insn-006bbcb0) 範囲 `[['006bbcb0', '006bbcef']]`
  - `CONDITIONAL_JUMP` [`006bbcec`](#insn-006bbcec) → [`006bbb78`](#insn-006bbb78)
  - `FALL_THROUGH` [`006bbcec`](#insn-006bbcec) → [`006bbcf0`](#insn-006bbcf0)
- ブロック [`006bbcf0`](#insn-006bbcf0) 範囲 `[['006bbcf0', '006bbcfb']]`
  - `UNCONDITIONAL_JUMP` [`006bbcf8`](#insn-006bbcf8) → [`006bbb78`](#insn-006bbb78)
- ブロック [`006bbcfc`](#insn-006bbcfc) 範囲 `[['006bbcfc', '006bbd07']]`
  - `UNCONDITIONAL_JUMP` [`006bbd04`](#insn-006bbd04) → [`006bbb34`](#insn-006bbb34)
- ブロック [`006bbd08`](#insn-006bbd08) 範囲 `[['006bbd08', '006bbd0f']]`
  - `UNCONDITIONAL_JUMP` [`006bbd0c`](#insn-006bbd0c) → [`006bbb34`](#insn-006bbb34)

## 命令位置別の参照

- [`006bbafc`](#insn-006bbafc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb00`](#insn-006bbb00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb04`](#insn-006bbb04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb08`](#insn-006bbb08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb0c`](#insn-006bbb0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb1c`](#insn-006bbb1c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`006bbb28`](#insn-006bbb28) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbb2c`](#insn-006bbb2c) → [`006bbb54`](#insn-006bbb54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb34`](#insn-006bbb34) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb38`](#insn-006bbb38) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb3c`](#insn-006bbb3c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb40`](#insn-006bbb40) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb44`](#insn-006bbb44) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb50`](#insn-006bbb50) → [`006bbb30`](#insn-006bbb30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb5c`](#insn-006bbb5c) → [`006bbb4c`](#insn-006bbb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb60`](#insn-006bbb60) → [`006bbb6c`](#insn-006bbb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb68`](#insn-006bbb68) → [`006bbb4c`](#insn-006bbb4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb74`](#insn-006bbb74) → [`006bbbac`](#insn-006bbbac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbb78`](#insn-006bbb78) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbb7c`](#insn-006bbb7c) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`006bbb80`](#insn-006bbb80) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbb88`](#insn-006bbb88) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbb9c`](#insn-006bbb9c) → [`006bbd08`](#insn-006bbd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbba8`](#insn-006bbba8) → [`006bbcfc`](#insn-006bbcfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbbb0`](#insn-006bbbb0) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`006bbbb8`](#insn-006bbbb8) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbbbc`](#insn-006bbbbc) → [`006bbbd8`](#insn-006bbbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbbc8`](#insn-006bbbc8) → [`006bbbf8`](#insn-006bbbf8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbbd4`](#insn-006bbbd4) → [`006bbbf8`](#insn-006bbbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbbe4`](#insn-006bbbe4) → [`006bbbcc`](#insn-006bbbcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbbe8`](#insn-006bbbe8) → [`006bbc54`](#insn-006bbc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbbf0`](#insn-006bbbf0) → [`006bbbd8`](#insn-006bbbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbc00`](#insn-006bbc00) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`006bbc18`](#insn-006bbc18) → [`00c59130`](../00c59/00c59130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59130` · 推定シンボル `None` · 推定型 `None`
- [`006bbc28`](#insn-006bbc28) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbc2c`](#insn-006bbc2c) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbc34`](#insn-006bbc34) → [`006bbc40`](#insn-006bbc40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbc38`](#insn-006bbc38) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbc3c`](#insn-006bbc3c) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbc40`](#insn-006bbc40) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbc44`](#insn-006bbc44) → [`0043bf04`](../0043b/0043bf04.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bf04` · 推定シンボル `None` · 推定型 `None`
- [`006bbc48`](#insn-006bbc48) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbc50`](#insn-006bbc50) → `0023d240`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbc64`](#insn-006bbc64) → [`006bbba0`](#insn-006bbba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbc68`](#insn-006bbc68) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`006bbc70`](#insn-006bbc70) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbc74`](#insn-006bbc74) → [`006bbc90`](#insn-006bbc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbc80`](#insn-006bbc80) → [`006bbcb0`](#insn-006bbcb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbc8c`](#insn-006bbc8c) → [`006bbcb0`](#insn-006bbcb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbc9c`](#insn-006bbc9c) → [`006bbc84`](#insn-006bbc84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbca0`](#insn-006bbca0) → [`006bbb8c`](#insn-006bbb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbca8`](#insn-006bbca8) → [`006bbc90`](#insn-006bbc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbcb8`](#insn-006bbcb8) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`006bbcd0`](#insn-006bbcd0) → [`00c59130`](../00c59/00c59130.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59130` · 推定シンボル `None` · 推定型 `None`
- [`006bbce0`](#insn-006bbce0) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbce4`](#insn-006bbce4) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbcec`](#insn-006bbcec) → [`006bbb78`](#insn-006bbb78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbcf0`](#insn-006bbcf0) → `0023d230`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbcf4`](#insn-006bbcf4) → `0023d238`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `Elf64_Rela[1815]`
- [`006bbcf8`](#insn-006bbcf8) → [`006bbb78`](#insn-006bbb78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbd04`](#insn-006bbd04) → [`006bbb34`](#insn-006bbb34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`006bbd0c`](#insn-006bbd0c) → [`006bbb34`](#insn-006bbb34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`006bbafc`](#insn-006bbafc)

~~~json
{
  "source": "006bbafc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb00`](#insn-006bbb00)

~~~json
{
  "source": "006bbb00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb04`](#insn-006bbb04)

~~~json
{
  "source": "006bbb04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb08`](#insn-006bbb08)

~~~json
{
  "source": "006bbb08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb0c`](#insn-006bbb0c)

~~~json
{
  "source": "006bbb0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb1c`](#insn-006bbb1c)

~~~json
{
  "source": "006bbb1c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006bbb28`](#insn-006bbb28)

~~~json
{
  "source": "006bbb28",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbb2c`](#insn-006bbb2c)

~~~json
{
  "source": "006bbb2c",
  "target": "006bbb54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb34`](#insn-006bbb34)

~~~json
{
  "source": "006bbb34",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb38`](#insn-006bbb38)

~~~json
{
  "source": "006bbb38",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb3c`](#insn-006bbb3c)

~~~json
{
  "source": "006bbb3c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb40`](#insn-006bbb40)

~~~json
{
  "source": "006bbb40",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb44`](#insn-006bbb44)

~~~json
{
  "source": "006bbb44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb50`](#insn-006bbb50)

~~~json
{
  "source": "006bbb50",
  "target": "006bbb30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb5c`](#insn-006bbb5c)

~~~json
{
  "source": "006bbb5c",
  "target": "006bbb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb60`](#insn-006bbb60)

~~~json
{
  "source": "006bbb60",
  "target": "006bbb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb68`](#insn-006bbb68)

~~~json
{
  "source": "006bbb68",
  "target": "006bbb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb74`](#insn-006bbb74)

~~~json
{
  "source": "006bbb74",
  "target": "006bbbac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbb78`](#insn-006bbb78)

~~~json
{
  "source": "006bbb78",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbb7c`](#insn-006bbb7c)

~~~json
{
  "source": "006bbb7c",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006bbb80`](#insn-006bbb80)

~~~json
{
  "source": "006bbb80",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbb88`](#insn-006bbb88)

~~~json
{
  "source": "006bbb88",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbb9c`](#insn-006bbb9c)

~~~json
{
  "source": "006bbb9c",
  "target": "006bbd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbba8`](#insn-006bbba8)

~~~json
{
  "source": "006bbba8",
  "target": "006bbcfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbbb0`](#insn-006bbbb0)

~~~json
{
  "source": "006bbbb0",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006bbbb8`](#insn-006bbbb8)

~~~json
{
  "source": "006bbbb8",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbbbc`](#insn-006bbbbc)

~~~json
{
  "source": "006bbbbc",
  "target": "006bbbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbbc8`](#insn-006bbbc8)

~~~json
{
  "source": "006bbbc8",
  "target": "006bbbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbbd4`](#insn-006bbbd4)

~~~json
{
  "source": "006bbbd4",
  "target": "006bbbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbbe4`](#insn-006bbbe4)

~~~json
{
  "source": "006bbbe4",
  "target": "006bbbcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbbe8`](#insn-006bbbe8)

~~~json
{
  "source": "006bbbe8",
  "target": "006bbc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbbf0`](#insn-006bbbf0)

~~~json
{
  "source": "006bbbf0",
  "target": "006bbbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbc00`](#insn-006bbc00)

~~~json
{
  "source": "006bbc00",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006bbc18`](#insn-006bbc18)

~~~json
{
  "source": "006bbc18",
  "target": "00c59130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006bbc28`](#insn-006bbc28)

~~~json
{
  "source": "006bbc28",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbc2c`](#insn-006bbc2c)

~~~json
{
  "source": "006bbc2c",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbc34`](#insn-006bbc34)

~~~json
{
  "source": "006bbc34",
  "target": "006bbc40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbc38`](#insn-006bbc38)

~~~json
{
  "source": "006bbc38",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbc3c`](#insn-006bbc3c)

~~~json
{
  "source": "006bbc3c",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbc40`](#insn-006bbc40)

~~~json
{
  "source": "006bbc40",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbc44`](#insn-006bbc44)

~~~json
{
  "source": "006bbc44",
  "target": "0043bf04",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006bbc48`](#insn-006bbc48)

~~~json
{
  "source": "006bbc48",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbc50`](#insn-006bbc50)

~~~json
{
  "source": "006bbc50",
  "target": "0023d240",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6056,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbc64`](#insn-006bbc64)

~~~json
{
  "source": "006bbc64",
  "target": "006bbba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbc68`](#insn-006bbc68)

~~~json
{
  "source": "006bbc68",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006bbc70`](#insn-006bbc70)

~~~json
{
  "source": "006bbc70",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbc74`](#insn-006bbc74)

~~~json
{
  "source": "006bbc74",
  "target": "006bbc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbc80`](#insn-006bbc80)

~~~json
{
  "source": "006bbc80",
  "target": "006bbcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbc8c`](#insn-006bbc8c)

~~~json
{
  "source": "006bbc8c",
  "target": "006bbcb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbc9c`](#insn-006bbc9c)

~~~json
{
  "source": "006bbc9c",
  "target": "006bbc84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbca0`](#insn-006bbca0)

~~~json
{
  "source": "006bbca0",
  "target": "006bbb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbca8`](#insn-006bbca8)

~~~json
{
  "source": "006bbca8",
  "target": "006bbc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbcb8`](#insn-006bbcb8)

~~~json
{
  "source": "006bbcb8",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006bbcd0`](#insn-006bbcd0)

~~~json
{
  "source": "006bbcd0",
  "target": "00c59130",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`006bbce0`](#insn-006bbce0)

~~~json
{
  "source": "006bbce0",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbce4`](#insn-006bbce4)

~~~json
{
  "source": "006bbce4",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbcec`](#insn-006bbcec)

~~~json
{
  "source": "006bbcec",
  "target": "006bbb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbcf0`](#insn-006bbcf0)

~~~json
{
  "source": "006bbcf0",
  "target": "0023d230",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6040,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbcf4`](#insn-006bbcf4)

~~~json
{
  "source": "006bbcf4",
  "target": "0023d238",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0023ba98",
  "offset": 6048,
  "size": 43560,
  "datatype": "Elf64_Rela[1815]",
  "bytes": "70cfb900000000000204000001000000000000000000000078cfb90000000000",
  "capture_start": "0023ba98",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`006bbcf8`](#insn-006bbcf8)

~~~json
{
  "source": "006bbcf8",
  "target": "006bbb78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbd04`](#insn-006bbd04)

~~~json
{
  "source": "006bbd04",
  "target": "006bbb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`006bbd0c`](#insn-006bbd0c)

~~~json
{
  "source": "006bbd0c",
  "target": "006bbb34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
