# 00a0aaec

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00a0aaa8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00a0a/00a0aaa8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0053.md#compare-7ba4325ea72c6b0998ed1647221ec58d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a687bc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a68/00a687bc.md) · 移動量 `+0x5dcd0`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0050.md#compare-027fa412b5b8b83ff4e72968fe70e5b5)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a0aaec",
  "name": "FUN_00a0aaec",
  "size": 564,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "318774da2d4363d542683adb9f287c8a7e1b225d93e1c2009fd99976799ca391",
  "source_text_sha256": "318774da2d4363d542683adb9f287c8a7e1b225d93e1c2009fd99976799ca391",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a0aaec",
        "00a0ad1f"
      ]
    ],
    "bytes_sha256": "2f51e1eb123e0c61ea054fa763fe6d07745f7c879d9cce592b50e8af078753f5",
    "instruction_count": 141,
    "instruction_bytes": 564,
    "body_bytes": 564,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a0b228](../00a0b/00a0b228.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0045d518](../0045d/0045d518.md)
- [0059d170](../0059d/0059d170.md)
- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4160 bytes

~~~c

void FUN_00a0aaec(undefined4 *param_1,undefined8 param_2)

{
  undefined4 uVar1;
  int iVar2;
  int iVar3;
  int iVar4;
  int iVar5;
  undefined8 *puVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  long *plVar9;
  int iVar10;
  int iVar11;
  undefined8 *puVar12;
  undefined8 *puVar13;
  undefined8 *puVar14;
  
  puVar12 = (undefined8 *)(param_1 + 4);
  FUN_0059d170(param_1 + 2,*puVar12);
  *(undefined8 **)(param_1 + 2) = puVar12;
  *(undefined8 *)(param_1 + 6) = 0;
  *puVar12 = 0;
  uVar1 = FUN_0045d518(param_2);
  *param_1 = uVar1;
  iVar2 = FUN_0045d518(param_2);
  if (0 < iVar2) {
    iVar10 = 0;
    do {
      iVar3 = FUN_0045d518(param_2);
      iVar4 = FUN_0045d518(param_2);
      if (iVar4 != 0) {
        iVar11 = 0;
        do {
                    /* try { // try from 00a0abcc to 00b0abd3 has its CatchHandler @ 00a0d628 */
          iVar5 = FUN_0045d518(param_2);
          uVar1 = FUN_0045d518(param_2);
          puVar8 = (undefined8 *)*puVar12;
          puVar13 = puVar12;
          puVar14 = puVar12;
          if ((undefined8 *)*puVar12 != (undefined8 *)0x0) {
            do {
                    /* try { // try from 00a0ac00 to 00b0ac07 has its CatchHandler @ 00a0d5f0 */
              while (puVar6 = puVar8, puVar14 = puVar6, iVar3 < *(int *)(puVar6 + 4)) {
                puVar8 = (undefined8 *)*puVar6;
                puVar13 = puVar6;
                if ((undefined8 *)*puVar6 == (undefined8 *)0x0) goto LAB_00a0ac24;
              }
              if (iVar3 <= *(int *)(puVar6 + 4)) goto LAB_00a0ac80;
              puVar8 = (undefined8 *)puVar6[1];
            } while ((undefined8 *)puVar6[1] != (undefined8 *)0x0);
            puVar13 = puVar6 + 1;
          }
LAB_00a0ac24:
                    /* try { // try from 00a0ac24 to 00b0ac2b has its CatchHandler @ 00a0d604 */
          puVar6 = (undefined8 *)_Znwm(0x40);
          puVar6[7] = 0;
          puVar6[6] = 0;
          puVar6[5] = puVar6 + 6;
          *puVar6 = 0;
          puVar6[1] = 0;
          puVar6[2] = puVar14;
          *puVar13 = puVar6;
          plVar9 = *(long **)(param_1 + 2);
          *(int *)(puVar6 + 4) = iVar3;
          puVar8 = puVar6;
          if (*plVar9 != 0) {
            *(long *)(param_1 + 2) = *plVar9;
            puVar8 = (undefined8 *)*puVar13;
          }
          FUN_00419064(*(undefined8 *)(param_1 + 4),puVar8);
          *(long *)(param_1 + 6) = *(long *)(param_1 + 6) + 1;
LAB_00a0ac80:
          puVar13 = puVar6 + 6;
          puVar8 = (undefined8 *)*puVar13;
          puVar14 = puVar13;
          if ((undefined8 *)*puVar13 != (undefined8 *)0x0) {
            do {
              while (puVar7 = puVar8, puVar14 = puVar7, iVar5 < *(int *)((long)puVar7 + 0x1c)) {
                puVar8 = (undefined8 *)*puVar7;
                puVar13 = puVar7;
                if ((undefined8 *)*puVar7 == (undefined8 *)0x0) goto LAB_00a0acc4;
              }
              if (iVar5 <= *(int *)((long)puVar7 + 0x1c)) goto LAB_00a0abb0;
              puVar8 = (undefined8 *)puVar7[1];
            } while ((undefined8 *)puVar7[1] != (undefined8 *)0x0);
            puVar13 = puVar7 + 1;
          }
LAB_00a0acc4:
          puVar7 = (undefined8 *)_Znwm(0x28);
          *puVar7 = 0;
          puVar7[1] = 0;
                    /* try { // try from 00a0acdc to 00b0ace3 has its CatchHandler @ 00a0d5b0 */
          puVar7[2] = puVar14;
          *puVar13 = puVar7;
          plVar9 = (long *)puVar6[5];
          *(int *)((long)puVar7 + 0x1c) = iVar5;
          *(undefined4 *)(puVar7 + 4) = 0;
          puVar8 = puVar7;
          if (*plVar9 != 0) {
            puVar6[5] = *plVar9;
            puVar8 = (undefined8 *)*puVar13;
          }
                    /* try { // try from 00a0aba0 to 00b0aba7 has its CatchHandler @ 00a0d5f8 */
          FUN_00419064(puVar6[6],puVar8);
          puVar6[7] = puVar6[7] + 1;
LAB_00a0abb0:
          iVar11 = iVar11 + 1;
          *(undefined4 *)(puVar7 + 4) = uVar1;
        } while (iVar11 != iVar4);
      }
      iVar10 = iVar10 + 1;
    } while (iVar10 != iVar2);
  }
                    /* try { // try from 00a0ad08 to 00b0ad0f has its CatchHandler @ 00a0d5dc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a0aaec"></a> `00a0aaec` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00a0aaf0"></a> `00a0aaf0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a0aaf4"></a> `00a0aaf4` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a0aaf8"></a> `00a0aaf8` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a0aafc"></a> `00a0aafc` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a0ab00"></a> `00a0ab00` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a0ab04"></a> `00a0ab04` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a0ab08"></a> `00a0ab08` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00a0ab0c"></a> `00a0ab0c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00a0ab10"></a> `00a0ab10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00a0ab14"></a> `00a0ab14` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00a0ab18"></a> `00a0ab18` | `e8 0e 41 f8` | ldr x8,[x23, #0x10]! | `FALL_THROUGH`
<a id="insn-00a0ab1c"></a> `00a0ab1c` | `00 20 00 91` | add x0,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ab20"></a> `00a0ab20` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00a0ab24"></a> `00a0ab24` | `93 49 ee 97` | bl 0x0059d170 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ab28"></a> `00a0ab28` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a0ab2c"></a> `00a0ab2c` | `77 06 00 f9` | str x23,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a0ab30"></a> `00a0ab30` | `7f 0e 00 f9` | str xzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a0ab34"></a> `00a0ab34` | `ff 02 00 f9` | str xzr,[x23] | `FALL_THROUGH`
<a id="insn-00a0ab38"></a> `00a0ab38` | `78 4a e9 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ab3c"></a> `00a0ab3c` | `60 02 00 b9` | str w0,[x19] | `FALL_THROUGH`
<a id="insn-00a0ab40"></a> `00a0ab40` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a0ab44"></a> `00a0ab44` | `b4 83 1f f8` | stur x20,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a0ab48"></a> `00a0ab48` | `74 4a e9 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ab4c"></a> `00a0ab4c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00a0ab50"></a> `00a0ab50` | `e0 0f 00 b9` | str w0,[sp, #0xc] | `FALL_THROUGH`
<a id="insn-00a0ab54"></a> `00a0ab54` | `6b 0d 00 54` | b.lt 0x00a0ad00 | `CONDITIONAL_JUMP`
<a id="insn-00a0ab58"></a> `00a0ab58` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-00a0ab5c"></a> `00a0ab5c` | `05 00 00 14` | b 0x00a0ab70 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ab60"></a> `00a0ab60` | `e8 a7 41 29` | ldp w8,w9,[sp, #0xc] | `FALL_THROUGH`
<a id="insn-00a0ab64"></a> `00a0ab64` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00a0ab68"></a> `00a0ab68` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00a0ab6c"></a> `00a0ab6c` | `a0 0c 00 54` | b.eq 0x00a0ad00 | `CONDITIONAL_JUMP`
<a id="insn-00a0ab70"></a> `00a0ab70` | `b4 83 5f f8` | ldur x20,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a0ab74"></a> `00a0ab74` | `e9 13 00 b9` | str w9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a0ab78"></a> `00a0ab78` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a0ab7c"></a> `00a0ab7c` | `67 4a e9 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ab80"></a> `00a0ab80` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00a0ab84"></a> `00a0ab84` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a0ab88"></a> `00a0ab88` | `64 4a e9 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ab8c"></a> `00a0ab8c` | `a0 43 1f b8` | stur w0,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00a0ab90"></a> `00a0ab90` | `80 fe ff 34` | cbz w0,0x00a0ab60 | `CONDITIONAL_JUMP`
<a id="insn-00a0ab94"></a> `00a0ab94` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00a0ab98"></a> `00a0ab98` | `0b 00 00 14` | b 0x00a0abc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ab9c"></a> `00a0ab9c` | `80 1b 40 f9` | ldr x0,[x28, #0x30] | `FALL_THROUGH`
<a id="insn-00a0aba0"></a> `00a0aba0` | `31 39 e8 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00a0aba4"></a> `00a0aba4` | `88 1f 40 f9` | ldr x8,[x28, #0x38] | `FALL_THROUGH`
<a id="insn-00a0aba8"></a> `00a0aba8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00a0abac"></a> `00a0abac` | `88 1f 00 f9` | str x8,[x28, #0x38] | `FALL_THROUGH`
<a id="insn-00a0abb0"></a> `00a0abb0` | `a8 43 5f b8` | ldur w8,[x29, #-0xc] | `FALL_THROUGH`
<a id="insn-00a0abb4"></a> `00a0abb4` | `b5 06 00 11` | add w21,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00a0abb8"></a> `00a0abb8` | `78 23 00 b9` | str w24,[x27, #0x20] | `FALL_THROUGH`
<a id="insn-00a0abbc"></a> `00a0abbc` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00a0abc0"></a> `00a0abc0` | `00 fd ff 54` | b.eq 0x00a0ab60 | `CONDITIONAL_JUMP`
<a id="insn-00a0abc4"></a> `00a0abc4` | `b4 83 5f f8` | ldur x20,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a0abc8"></a> `00a0abc8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a0abcc"></a> `00a0abcc` | `53 4a e9 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00a0abd0"></a> `00a0abd0` | `fa 03 00 2a` | mov w26,w0 | `FALL_THROUGH`
<a id="insn-00a0abd4"></a> `00a0abd4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a0abd8"></a> `00a0abd8` | `50 4a e9 97` | bl 0x0045d518 | `UNCONDITIONAL_CALL`
<a id="insn-00a0abdc"></a> `00a0abdc` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00a0abe0"></a> `00a0abe0` | `f8 03 00 2a` | mov w24,w0 | `FALL_THROUGH`
<a id="insn-00a0abe4"></a> `00a0abe4` | `f9 03 17 aa` | mov x25,x23 | `FALL_THROUGH`
<a id="insn-00a0abe8"></a> `00a0abe8` | `fc 03 17 aa` | mov x28,x23 | `FALL_THROUGH`
<a id="insn-00a0abec"></a> `00a0abec` | `a8 00 00 b5` | cbnz x8,0x00a0ac00 | `CONDITIONAL_JUMP`
<a id="insn-00a0abf0"></a> `00a0abf0` | `0d 00 00 14` | b 0x00a0ac24 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0abf4"></a> `00a0abf4` | `88 03 40 f9` | ldr x8,[x28] | `FALL_THROUGH`
<a id="insn-00a0abf8"></a> `00a0abf8` | `f9 03 1c aa` | mov x25,x28 | `FALL_THROUGH`
<a id="insn-00a0abfc"></a> `00a0abfc` | `48 01 00 b4` | cbz x8,0x00a0ac24 | `CONDITIONAL_JUMP`
<a id="insn-00a0ac00"></a> `00a0ac00` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-00a0ac04"></a> `00a0ac04` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00a0ac08"></a> `00a0ac08` | `df 02 08 6b` | cmp w22,w8 | `FALL_THROUGH`
<a id="insn-00a0ac0c"></a> `00a0ac0c` | `4b ff ff 54` | b.lt 0x00a0abf4 | `CONDITIONAL_JUMP`
<a id="insn-00a0ac10"></a> `00a0ac10` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00a0ac14"></a> `00a0ac14` | `6a 03 00 54` | b.ge 0x00a0ac80 | `CONDITIONAL_JUMP`
<a id="insn-00a0ac18"></a> `00a0ac18` | `88 07 40 f9` | ldr x8,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-00a0ac1c"></a> `00a0ac1c` | `28 ff ff b5` | cbnz x8,0x00a0ac00 | `CONDITIONAL_JUMP`
<a id="insn-00a0ac20"></a> `00a0ac20` | `99 23 00 91` | add x25,x28,#0x8 | `FALL_THROUGH`
<a id="insn-00a0ac24"></a> `00a0ac24` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00a0ac28"></a> `00a0ac28` | `fb 03 1c aa` | mov x27,x28 | `FALL_THROUGH`
<a id="insn-00a0ac2c"></a> `00a0ac2c` | `05 41 07 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ac30"></a> `00a0ac30` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00a0ac34"></a> `00a0ac34` | `1f 1c 00 f9` | str xzr,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00a0ac38"></a> `00a0ac38` | `fc 03 00 aa` | mov x28,x0 | `FALL_THROUGH`
<a id="insn-00a0ac3c"></a> `00a0ac3c` | `1f 0d 03 f8` | str xzr,[x8, #0x30]! | `FALL_THROUGH`
<a id="insn-00a0ac40"></a> `00a0ac40` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00a0ac44"></a> `00a0ac44` | `08 14 00 f9` | str x8,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00a0ac48"></a> `00a0ac48` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00a0ac4c"></a> `00a0ac4c` | `1b 08 00 f9` | str x27,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00a0ac50"></a> `00a0ac50` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00a0ac54"></a> `00a0ac54` | `68 82 40 f8` | ldur x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a0ac58"></a> `00a0ac58` | `16 20 00 b9` | str w22,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00a0ac5c"></a> `00a0ac5c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a0ac60"></a> `00a0ac60` | `68 00 00 b4` | cbz x8,0x00a0ac6c | `CONDITIONAL_JUMP`
<a id="insn-00a0ac64"></a> `00a0ac64` | `68 82 00 f8` | stur x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00a0ac68"></a> `00a0ac68` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00a0ac6c"></a> `00a0ac6c` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00a0ac70"></a> `00a0ac70` | `fd 38 e8 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00a0ac74"></a> `00a0ac74` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a0ac78"></a> `00a0ac78` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00a0ac7c"></a> `00a0ac7c` | `68 0e 00 f9` | str x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00a0ac80"></a> `00a0ac80` | `f9 03 1c aa` | mov x25,x28 | `FALL_THROUGH`
<a id="insn-00a0ac84"></a> `00a0ac84` | `28 0f 43 f8` | ldr x8,[x25, #0x30]! | `FALL_THROUGH`
<a id="insn-00a0ac88"></a> `00a0ac88` | `c8 00 00 b5` | cbnz x8,0x00a0aca0 | `CONDITIONAL_JUMP`
<a id="insn-00a0ac8c"></a> `00a0ac8c` | `fb 03 19 aa` | mov x27,x25 | `FALL_THROUGH`
<a id="insn-00a0ac90"></a> `00a0ac90` | `0d 00 00 14` | b 0x00a0acc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ac94"></a> `00a0ac94` | `68 03 40 f9` | ldr x8,[x27] | `FALL_THROUGH`
<a id="insn-00a0ac98"></a> `00a0ac98` | `f9 03 1b aa` | mov x25,x27 | `FALL_THROUGH`
<a id="insn-00a0ac9c"></a> `00a0ac9c` | `48 01 00 b4` | cbz x8,0x00a0acc4 | `CONDITIONAL_JUMP`
<a id="insn-00a0aca0"></a> `00a0aca0` | `fb 03 08 aa` | mov x27,x8 | `FALL_THROUGH`
<a id="insn-00a0aca4"></a> `00a0aca4` | `08 1d 40 b9` | ldr w8,[x8, #0x1c] | `FALL_THROUGH`
<a id="insn-00a0aca8"></a> `00a0aca8` | `5f 03 08 6b` | cmp w26,w8 | `FALL_THROUGH`
<a id="insn-00a0acac"></a> `00a0acac` | `4b ff ff 54` | b.lt 0x00a0ac94 | `CONDITIONAL_JUMP`
<a id="insn-00a0acb0"></a> `00a0acb0` | `1f 01 1a 6b` | cmp w8,w26 | `FALL_THROUGH`
<a id="insn-00a0acb4"></a> `00a0acb4` | `ea f7 ff 54` | b.ge 0x00a0abb0 | `CONDITIONAL_JUMP`
<a id="insn-00a0acb8"></a> `00a0acb8` | `68 07 40 f9` | ldr x8,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00a0acbc"></a> `00a0acbc` | `28 ff ff b5` | cbnz x8,0x00a0aca0 | `CONDITIONAL_JUMP`
<a id="insn-00a0acc0"></a> `00a0acc0` | `79 23 00 91` | add x25,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00a0acc4"></a> `00a0acc4` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00a0acc8"></a> `00a0acc8` | `f4 03 1b aa` | mov x20,x27 | `FALL_THROUGH`
<a id="insn-00a0accc"></a> `00a0accc` | `dd 40 07 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00a0acd0"></a> `00a0acd0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00a0acd4"></a> `00a0acd4` | `fb 03 00 aa` | mov x27,x0 | `FALL_THROUGH`
<a id="insn-00a0acd8"></a> `00a0acd8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00a0acdc"></a> `00a0acdc` | `14 08 00 f9` | str x20,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00a0ace0"></a> `00a0ace0` | `20 03 00 f9` | str x0,[x25] | `FALL_THROUGH`
<a id="insn-00a0ace4"></a> `00a0ace4` | `88 17 40 f9` | ldr x8,[x28, #0x28] | `FALL_THROUGH`
<a id="insn-00a0ace8"></a> `00a0ace8` | `1a fc 03 29` | stp w26,wzr,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-00a0acec"></a> `00a0acec` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a0acf0"></a> `00a0acf0` | `68 f5 ff b4` | cbz x8,0x00a0ab9c | `CONDITIONAL_JUMP`
<a id="insn-00a0acf4"></a> `00a0acf4` | `88 17 00 f9` | str x8,[x28, #0x28] | `FALL_THROUGH`
<a id="insn-00a0acf8"></a> `00a0acf8` | `21 03 40 f9` | ldr x1,[x25] | `FALL_THROUGH`
<a id="insn-00a0acfc"></a> `00a0acfc` | `a8 ff ff 17` | b 0x00a0ab9c | `UNCONDITIONAL_JUMP`
<a id="insn-00a0ad00"></a> `00a0ad00` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a0ad04"></a> `00a0ad04` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a0ad08"></a> `00a0ad08` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a0ad0c"></a> `00a0ad0c` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a0ad10"></a> `00a0ad10` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a0ad14"></a> `00a0ad14` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a0ad18"></a> `00a0ad18` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00a0ad1c"></a> `00a0ad1c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a0aaec`](#insn-00a0aaec) 範囲 `[['00a0aaec', '00a0ab57']]`
  - `CONDITIONAL_JUMP` [`00a0ab54`](#insn-00a0ab54) → [`00a0ad00`](#insn-00a0ad00)
  - `FALL_THROUGH` [`00a0ab54`](#insn-00a0ab54) → [`00a0ab58`](#insn-00a0ab58)
- ブロック [`00a0ab58`](#insn-00a0ab58) 範囲 `[['00a0ab58', '00a0ab5f']]`
  - `UNCONDITIONAL_JUMP` [`00a0ab5c`](#insn-00a0ab5c) → [`00a0ab70`](#insn-00a0ab70)
- ブロック [`00a0ab60`](#insn-00a0ab60) 範囲 `[['00a0ab60', '00a0ab6f']]`
  - `CONDITIONAL_JUMP` [`00a0ab6c`](#insn-00a0ab6c) → [`00a0ad00`](#insn-00a0ad00)
  - `FALL_THROUGH` [`00a0ab6c`](#insn-00a0ab6c) → [`00a0ab70`](#insn-00a0ab70)
- ブロック [`00a0ab70`](#insn-00a0ab70) 範囲 `[['00a0ab70', '00a0ab93']]`
  - `CONDITIONAL_JUMP` [`00a0ab90`](#insn-00a0ab90) → [`00a0ab60`](#insn-00a0ab60)
  - `FALL_THROUGH` [`00a0ab90`](#insn-00a0ab90) → [`00a0ab94`](#insn-00a0ab94)
- ブロック [`00a0ab94`](#insn-00a0ab94) 範囲 `[['00a0ab94', '00a0ab9b']]`
  - `UNCONDITIONAL_JUMP` [`00a0ab98`](#insn-00a0ab98) → [`00a0abc4`](#insn-00a0abc4)
- ブロック [`00a0ab9c`](#insn-00a0ab9c) 範囲 `[['00a0ab9c', '00a0ab9f']]`
  - `FALL_THROUGH` [`00a0ab9c`](#insn-00a0ab9c) → [`00a0aba0`](#insn-00a0aba0)
- ブロック [`00a0aba0`](#insn-00a0aba0) 範囲 `[['00a0aba0', '00a0abaf']]`
  - `FALL_THROUGH` [`00a0abac`](#insn-00a0abac) → [`00a0abb0`](#insn-00a0abb0)
- ブロック [`00a0abb0`](#insn-00a0abb0) 範囲 `[['00a0abb0', '00a0abc3']]`
  - `CONDITIONAL_JUMP` [`00a0abc0`](#insn-00a0abc0) → [`00a0ab60`](#insn-00a0ab60)
  - `FALL_THROUGH` [`00a0abc0`](#insn-00a0abc0) → [`00a0abc4`](#insn-00a0abc4)
- ブロック [`00a0abc4`](#insn-00a0abc4) 範囲 `[['00a0abc4', '00a0abcb']]`
  - `FALL_THROUGH` [`00a0abc8`](#insn-00a0abc8) → [`00a0abcc`](#insn-00a0abcc)
- ブロック [`00a0abcc`](#insn-00a0abcc) 範囲 `[['00a0abcc', '00a0abef']]`
  - `CONDITIONAL_JUMP` [`00a0abec`](#insn-00a0abec) → [`00a0ac00`](#insn-00a0ac00)
  - `FALL_THROUGH` [`00a0abec`](#insn-00a0abec) → [`00a0abf0`](#insn-00a0abf0)
- ブロック [`00a0abf0`](#insn-00a0abf0) 範囲 `[['00a0abf0', '00a0abf3']]`
  - `UNCONDITIONAL_JUMP` [`00a0abf0`](#insn-00a0abf0) → [`00a0ac24`](#insn-00a0ac24)
- ブロック [`00a0abf4`](#insn-00a0abf4) 範囲 `[['00a0abf4', '00a0abff']]`
  - `CONDITIONAL_JUMP` [`00a0abfc`](#insn-00a0abfc) → [`00a0ac24`](#insn-00a0ac24)
  - `FALL_THROUGH` [`00a0abfc`](#insn-00a0abfc) → [`00a0ac00`](#insn-00a0ac00)
- ブロック [`00a0ac00`](#insn-00a0ac00) 範囲 `[['00a0ac00', '00a0ac0f']]`
  - `CONDITIONAL_JUMP` [`00a0ac0c`](#insn-00a0ac0c) → [`00a0abf4`](#insn-00a0abf4)
  - `FALL_THROUGH` [`00a0ac0c`](#insn-00a0ac0c) → [`00a0ac10`](#insn-00a0ac10)
- ブロック [`00a0ac10`](#insn-00a0ac10) 範囲 `[['00a0ac10', '00a0ac17']]`
  - `CONDITIONAL_JUMP` [`00a0ac14`](#insn-00a0ac14) → [`00a0ac80`](#insn-00a0ac80)
  - `FALL_THROUGH` [`00a0ac14`](#insn-00a0ac14) → [`00a0ac18`](#insn-00a0ac18)
- ブロック [`00a0ac18`](#insn-00a0ac18) 範囲 `[['00a0ac18', '00a0ac1f']]`
  - `CONDITIONAL_JUMP` [`00a0ac1c`](#insn-00a0ac1c) → [`00a0ac00`](#insn-00a0ac00)
  - `FALL_THROUGH` [`00a0ac1c`](#insn-00a0ac1c) → [`00a0ac20`](#insn-00a0ac20)
- ブロック [`00a0ac20`](#insn-00a0ac20) 範囲 `[['00a0ac20', '00a0ac23']]`
  - `FALL_THROUGH` [`00a0ac20`](#insn-00a0ac20) → [`00a0ac24`](#insn-00a0ac24)
- ブロック [`00a0ac24`](#insn-00a0ac24) 範囲 `[['00a0ac24', '00a0ac63']]`
  - `CONDITIONAL_JUMP` [`00a0ac60`](#insn-00a0ac60) → [`00a0ac6c`](#insn-00a0ac6c)
  - `FALL_THROUGH` [`00a0ac60`](#insn-00a0ac60) → [`00a0ac64`](#insn-00a0ac64)
- ブロック [`00a0ac64`](#insn-00a0ac64) 範囲 `[['00a0ac64', '00a0ac6b']]`
  - `FALL_THROUGH` [`00a0ac68`](#insn-00a0ac68) → [`00a0ac6c`](#insn-00a0ac6c)
- ブロック [`00a0ac6c`](#insn-00a0ac6c) 範囲 `[['00a0ac6c', '00a0ac7f']]`
  - `FALL_THROUGH` [`00a0ac7c`](#insn-00a0ac7c) → [`00a0ac80`](#insn-00a0ac80)
- ブロック [`00a0ac80`](#insn-00a0ac80) 範囲 `[['00a0ac80', '00a0ac8b']]`
  - `CONDITIONAL_JUMP` [`00a0ac88`](#insn-00a0ac88) → [`00a0aca0`](#insn-00a0aca0)
  - `FALL_THROUGH` [`00a0ac88`](#insn-00a0ac88) → [`00a0ac8c`](#insn-00a0ac8c)
- ブロック [`00a0ac8c`](#insn-00a0ac8c) 範囲 `[['00a0ac8c', '00a0ac93']]`
  - `UNCONDITIONAL_JUMP` [`00a0ac90`](#insn-00a0ac90) → [`00a0acc4`](#insn-00a0acc4)
- ブロック [`00a0ac94`](#insn-00a0ac94) 範囲 `[['00a0ac94', '00a0ac9f']]`
  - `CONDITIONAL_JUMP` [`00a0ac9c`](#insn-00a0ac9c) → [`00a0acc4`](#insn-00a0acc4)
  - `FALL_THROUGH` [`00a0ac9c`](#insn-00a0ac9c) → [`00a0aca0`](#insn-00a0aca0)
- ブロック [`00a0aca0`](#insn-00a0aca0) 範囲 `[['00a0aca0', '00a0acaf']]`
  - `CONDITIONAL_JUMP` [`00a0acac`](#insn-00a0acac) → [`00a0ac94`](#insn-00a0ac94)
  - `FALL_THROUGH` [`00a0acac`](#insn-00a0acac) → [`00a0acb0`](#insn-00a0acb0)
- ブロック [`00a0acb0`](#insn-00a0acb0) 範囲 `[['00a0acb0', '00a0acb7']]`
  - `CONDITIONAL_JUMP` [`00a0acb4`](#insn-00a0acb4) → [`00a0abb0`](#insn-00a0abb0)
  - `FALL_THROUGH` [`00a0acb4`](#insn-00a0acb4) → [`00a0acb8`](#insn-00a0acb8)
- ブロック [`00a0acb8`](#insn-00a0acb8) 範囲 `[['00a0acb8', '00a0acbf']]`
  - `CONDITIONAL_JUMP` [`00a0acbc`](#insn-00a0acbc) → [`00a0aca0`](#insn-00a0aca0)
  - `FALL_THROUGH` [`00a0acbc`](#insn-00a0acbc) → [`00a0acc0`](#insn-00a0acc0)
- ブロック [`00a0acc0`](#insn-00a0acc0) 範囲 `[['00a0acc0', '00a0acc3']]`
  - `FALL_THROUGH` [`00a0acc0`](#insn-00a0acc0) → [`00a0acc4`](#insn-00a0acc4)
- ブロック [`00a0acc4`](#insn-00a0acc4) 範囲 `[['00a0acc4', '00a0acdb']]`
  - `FALL_THROUGH` [`00a0acd8`](#insn-00a0acd8) → [`00a0acdc`](#insn-00a0acdc)
- ブロック [`00a0acdc`](#insn-00a0acdc) 範囲 `[['00a0acdc', '00a0acf3']]`
  - `CONDITIONAL_JUMP` [`00a0acf0`](#insn-00a0acf0) → [`00a0ab9c`](#insn-00a0ab9c)
  - `FALL_THROUGH` [`00a0acf0`](#insn-00a0acf0) → [`00a0acf4`](#insn-00a0acf4)
- ブロック [`00a0acf4`](#insn-00a0acf4) 範囲 `[['00a0acf4', '00a0acff']]`
  - `UNCONDITIONAL_JUMP` [`00a0acfc`](#insn-00a0acfc) → [`00a0ab9c`](#insn-00a0ab9c)
- ブロック [`00a0ad00`](#insn-00a0ad00) 範囲 `[['00a0ad00', '00a0ad07']]`
  - `FALL_THROUGH` [`00a0ad04`](#insn-00a0ad04) → [`00a0ad08`](#insn-00a0ad08)
- ブロック [`00a0ad08`](#insn-00a0ad08) 範囲 `[['00a0ad08', '00a0ad1f']]`

## 命令位置別の参照

- [`00a0aaf0`](#insn-00a0aaf0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aaf4`](#insn-00a0aaf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aaf8`](#insn-00a0aaf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aafc`](#insn-00a0aafc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab00`](#insn-00a0ab00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab04`](#insn-00a0ab04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab24`](#insn-00a0ab24) → [`0059d170`](../0059d/0059d170.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0059d170` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab38`](#insn-00a0ab38) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab44`](#insn-00a0ab44) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab48`](#insn-00a0ab48) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab50`](#insn-00a0ab50) → `Stack[-0x74]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab54`](#insn-00a0ab54) → [`00a0ad00`](#insn-00a0ad00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab5c`](#insn-00a0ab5c) → [`00a0ab70`](#insn-00a0ab70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab60`](#insn-00a0ab60) → `Stack[-0x74]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab6c`](#insn-00a0ab6c) → [`00a0ad00`](#insn-00a0ad00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab70`](#insn-00a0ab70) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab74`](#insn-00a0ab74) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab7c`](#insn-00a0ab7c) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab88`](#insn-00a0ab88) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab8c`](#insn-00a0ab8c) → `Stack[-0x6c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab90`](#insn-00a0ab90) → [`00a0ab60`](#insn-00a0ab60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ab98`](#insn-00a0ab98) → [`00a0abc4`](#insn-00a0abc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0aba0`](#insn-00a0aba0) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00a0abb0`](#insn-00a0abb0) → `Stack[-0x6c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0abc0`](#insn-00a0abc0) → [`00a0ab60`](#insn-00a0ab60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0abc4`](#insn-00a0abc4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0abcc`](#insn-00a0abcc) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00a0abd8`](#insn-00a0abd8) → [`0045d518`](../0045d/0045d518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045d518` · 推定シンボル `None` · 推定型 `None`
- [`00a0abec`](#insn-00a0abec) → [`00a0ac00`](#insn-00a0ac00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0abf0`](#insn-00a0abf0) → [`00a0ac24`](#insn-00a0ac24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0abfc`](#insn-00a0abfc) → [`00a0ac24`](#insn-00a0ac24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ac0c`](#insn-00a0ac0c) → [`00a0abf4`](#insn-00a0abf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ac14`](#insn-00a0ac14) → [`00a0ac80`](#insn-00a0ac80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ac1c`](#insn-00a0ac1c) → [`00a0ac00`](#insn-00a0ac00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ac2c`](#insn-00a0ac2c) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00a0ac60`](#insn-00a0ac60) → [`00a0ac6c`](#insn-00a0ac6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ac70`](#insn-00a0ac70) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00a0ac88`](#insn-00a0ac88) → [`00a0aca0`](#insn-00a0aca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ac90`](#insn-00a0ac90) → [`00a0acc4`](#insn-00a0acc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ac9c`](#insn-00a0ac9c) → [`00a0acc4`](#insn-00a0acc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0acac`](#insn-00a0acac) → [`00a0ac94`](#insn-00a0ac94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0acb4`](#insn-00a0acb4) → [`00a0abb0`](#insn-00a0abb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0acbc`](#insn-00a0acbc) → [`00a0aca0`](#insn-00a0aca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0accc`](#insn-00a0accc) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00a0acf0`](#insn-00a0acf0) → [`00a0ab9c`](#insn-00a0ab9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0acfc`](#insn-00a0acfc) → [`00a0ab9c`](#insn-00a0ab9c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad00`](#insn-00a0ad00) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad04`](#insn-00a0ad04) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad08`](#insn-00a0ad08) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad0c`](#insn-00a0ad0c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad10`](#insn-00a0ad10) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a0ad14`](#insn-00a0ad14) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a0aaf0`](#insn-00a0aaf0)

~~~json
{
  "source": "00a0aaf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aaf4`](#insn-00a0aaf4)

~~~json
{
  "source": "00a0aaf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aaf8`](#insn-00a0aaf8)

~~~json
{
  "source": "00a0aaf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aafc`](#insn-00a0aafc)

~~~json
{
  "source": "00a0aafc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab00`](#insn-00a0ab00)

~~~json
{
  "source": "00a0ab00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab04`](#insn-00a0ab04)

~~~json
{
  "source": "00a0ab04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab24`](#insn-00a0ab24)

~~~json
{
  "source": "00a0ab24",
  "target": "0059d170",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ab38`](#insn-00a0ab38)

~~~json
{
  "source": "00a0ab38",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ab44`](#insn-00a0ab44)

~~~json
{
  "source": "00a0ab44",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab48`](#insn-00a0ab48)

~~~json
{
  "source": "00a0ab48",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ab50`](#insn-00a0ab50)

~~~json
{
  "source": "00a0ab50",
  "target": "Stack[-0x74]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab54`](#insn-00a0ab54)

~~~json
{
  "source": "00a0ab54",
  "target": "00a0ad00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab5c`](#insn-00a0ab5c)

~~~json
{
  "source": "00a0ab5c",
  "target": "00a0ab70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab60`](#insn-00a0ab60)

~~~json
{
  "source": "00a0ab60",
  "target": "Stack[-0x74]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab6c`](#insn-00a0ab6c)

~~~json
{
  "source": "00a0ab6c",
  "target": "00a0ad00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab70`](#insn-00a0ab70)

~~~json
{
  "source": "00a0ab70",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab74`](#insn-00a0ab74)

~~~json
{
  "source": "00a0ab74",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab7c`](#insn-00a0ab7c)

~~~json
{
  "source": "00a0ab7c",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ab88`](#insn-00a0ab88)

~~~json
{
  "source": "00a0ab88",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ab8c`](#insn-00a0ab8c)

~~~json
{
  "source": "00a0ab8c",
  "target": "Stack[-0x6c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab90`](#insn-00a0ab90)

~~~json
{
  "source": "00a0ab90",
  "target": "00a0ab60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ab98`](#insn-00a0ab98)

~~~json
{
  "source": "00a0ab98",
  "target": "00a0abc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0aba0`](#insn-00a0aba0)

~~~json
{
  "source": "00a0aba0",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0abb0`](#insn-00a0abb0)

~~~json
{
  "source": "00a0abb0",
  "target": "Stack[-0x6c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0abc0`](#insn-00a0abc0)

~~~json
{
  "source": "00a0abc0",
  "target": "00a0ab60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0abc4`](#insn-00a0abc4)

~~~json
{
  "source": "00a0abc4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0abcc`](#insn-00a0abcc)

~~~json
{
  "source": "00a0abcc",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0abd8`](#insn-00a0abd8)

~~~json
{
  "source": "00a0abd8",
  "target": "0045d518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0abec`](#insn-00a0abec)

~~~json
{
  "source": "00a0abec",
  "target": "00a0ac00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0abf0`](#insn-00a0abf0)

~~~json
{
  "source": "00a0abf0",
  "target": "00a0ac24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0abfc`](#insn-00a0abfc)

~~~json
{
  "source": "00a0abfc",
  "target": "00a0ac24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ac0c`](#insn-00a0ac0c)

~~~json
{
  "source": "00a0ac0c",
  "target": "00a0abf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ac14`](#insn-00a0ac14)

~~~json
{
  "source": "00a0ac14",
  "target": "00a0ac80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ac1c`](#insn-00a0ac1c)

~~~json
{
  "source": "00a0ac1c",
  "target": "00a0ac00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ac2c`](#insn-00a0ac2c)

~~~json
{
  "source": "00a0ac2c",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ac60`](#insn-00a0ac60)

~~~json
{
  "source": "00a0ac60",
  "target": "00a0ac6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ac70`](#insn-00a0ac70)

~~~json
{
  "source": "00a0ac70",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0ac88`](#insn-00a0ac88)

~~~json
{
  "source": "00a0ac88",
  "target": "00a0aca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ac90`](#insn-00a0ac90)

~~~json
{
  "source": "00a0ac90",
  "target": "00a0acc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ac9c`](#insn-00a0ac9c)

~~~json
{
  "source": "00a0ac9c",
  "target": "00a0acc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0acac`](#insn-00a0acac)

~~~json
{
  "source": "00a0acac",
  "target": "00a0ac94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0acb4`](#insn-00a0acb4)

~~~json
{
  "source": "00a0acb4",
  "target": "00a0abb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0acbc`](#insn-00a0acbc)

~~~json
{
  "source": "00a0acbc",
  "target": "00a0aca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0accc`](#insn-00a0accc)

~~~json
{
  "source": "00a0accc",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a0acf0`](#insn-00a0acf0)

~~~json
{
  "source": "00a0acf0",
  "target": "00a0ab9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0acfc`](#insn-00a0acfc)

~~~json
{
  "source": "00a0acfc",
  "target": "00a0ab9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad00`](#insn-00a0ad00)

~~~json
{
  "source": "00a0ad00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad04`](#insn-00a0ad04)

~~~json
{
  "source": "00a0ad04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad08`](#insn-00a0ad08)

~~~json
{
  "source": "00a0ad08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad0c`](#insn-00a0ad0c)

~~~json
{
  "source": "00a0ad0c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad10`](#insn-00a0ad10)

~~~json
{
  "source": "00a0ad10",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a0ad14`](#insn-00a0ad14)

~~~json
{
  "source": "00a0ad14",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
