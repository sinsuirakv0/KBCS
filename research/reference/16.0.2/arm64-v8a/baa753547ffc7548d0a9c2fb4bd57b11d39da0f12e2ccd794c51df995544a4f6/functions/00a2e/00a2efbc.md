# 00a2efbc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00a2ef68`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00a2e/00a2ef68.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0032.md#compare-1701b3be728696da75682c36c311019f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00a2ffb0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00a2f/00a2ffb0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0010.md#compare-bc5a87173e42edd5dc5960ea96db4c74)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a2efbc",
  "name": "FUN_00a2efbc",
  "size": 800,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "be6d735af67590c0798ff46802c7677a4e8022d588f0299e9b1c2cc265709693",
  "source_text_sha256": "be6d735af67590c0798ff46802c7677a4e8022d588f0299e9b1c2cc265709693",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a2efbc",
        "00a2f2db"
      ]
    ],
    "bytes_sha256": "ace58c20eab39293a1622a35f96de88915009c501b0d97aded516f65d51f7d0b",
    "instruction_count": 200,
    "instruction_bytes": 800,
    "body_bytes": 800,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a26210](../00a26/00a26210.md)

## 呼び出し先

- [0043bbe4](../0043b/0043bbe4.md)
- [0086c30c](../0086c/0086c30c.md)
- [00c57f60](../00c57/00c57f60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6515 bytes

~~~c

void FUN_00a2efbc(long *param_1,long *param_2,long *param_3)

{
  int iVar1;
  undefined4 uVar2;
  bool bVar3;
  undefined8 *puVar4;
  undefined8 *puVar5;
  long *plVar6;
  long *plVar7;
  long *plVar8;
  undefined8 *puVar9;
  long *plVar10;
  
                    /* try { // try from 00a2efd0 to 00b2f137 has its CatchHandler @ 00a2e6c0 */
  if (param_1[2] != 0) {
    puVar5 = (undefined8 *)*param_1;
    plVar10 = param_1 + 1;
    *param_1 = (long)plVar10;
    *(undefined8 *)(*plVar10 + 0x10) = 0;
    param_1[2] = 0;
    *plVar10 = 0;
    puVar4 = (undefined8 *)puVar5[1];
    if (puVar4 != (undefined8 *)0x0) {
      puVar5 = puVar4;
    }
    if (puVar5 == (undefined8 *)0x0) {
      puVar4 = (undefined8 *)0x0;
    }
    else {
      puVar9 = (undefined8 *)puVar5[2];
      if (puVar9 != (undefined8 *)0x0) {
        puVar4 = (undefined8 *)*puVar9;
        if (puVar4 == puVar5) {
          puVar4 = (undefined8 *)puVar9[1];
          *puVar9 = 0;
          while (puVar4 != (undefined8 *)0x0) {
            do {
              puVar9 = puVar4;
              puVar4 = (undefined8 *)*puVar9;
            } while ((undefined8 *)*puVar9 != (undefined8 *)0x0);
            puVar4 = (undefined8 *)puVar9[1];
          }
        }
        else {
          puVar9[1] = 0;
          while (puVar4 != (undefined8 *)0x0) {
            do {
              puVar9 = puVar4;
              puVar4 = (undefined8 *)*puVar9;
            } while ((undefined8 *)*puVar9 != (undefined8 *)0x0);
            puVar4 = (undefined8 *)puVar9[1];
          }
        }
      }
      do {
        puVar4 = puVar9;
        if (param_2 == param_3) break;
        iVar1 = *(int *)((long)param_2 + 0x1c);
        *(int *)((long)puVar5 + 0x1c) = iVar1;
        puVar5[4] = param_2[4];
        plVar8 = (long *)*plVar10;
        plVar6 = plVar10;
        while (plVar7 = plVar6, plVar8 != (long *)0x0) {
          while (plVar6 = plVar8, *(int *)((long)plVar6 + 0x1c) <= iVar1) {
            plVar8 = (long *)plVar6[1];
            if ((long *)plVar6[1] == (long *)0x0) {
              plVar7 = plVar6 + 1;
              goto LAB_00a2f0d8;
            }
          }
          plVar8 = (long *)*plVar6;
        }
LAB_00a2f0d8:
        *puVar5 = 0;
        puVar5[1] = 0;
        puVar5[2] = plVar6;
        *plVar7 = (long)puVar5;
        if (*(long *)*param_1 != 0) {
          *param_1 = *(long *)*param_1;
          puVar5 = (undefined8 *)*plVar7;
        }
        FUN_0043bbe4(param_1[1],puVar5);
        param_1[2] = param_1[2] + 1;
        if (puVar9 == (undefined8 *)0x0) {
          puVar4 = (undefined8 *)0x0;
        }
        else {
          puVar4 = (undefined8 *)puVar9[2];
          if (puVar4 != (undefined8 *)0x0) {
            puVar5 = (undefined8 *)*puVar4;
            if (puVar5 == puVar9) {
              puVar5 = (undefined8 *)puVar4[1];
              *puVar4 = 0;
                    /* try { // try from 00a2f194 to 00b2f2c3 has its CatchHandler @ 00a2e6c0 */
              while (puVar5 != (undefined8 *)0x0) {
                do {
                  puVar4 = puVar5;
                  puVar5 = (undefined8 *)*puVar4;
                } while ((undefined8 *)*puVar4 != (undefined8 *)0x0);
                puVar5 = (undefined8 *)puVar4[1];
              }
            }
            else {
              puVar4[1] = 0;
                    /* try { // try from 00a2f170 to 00b2f193 has its CatchHandler @ 00a2fd04 */
              while (puVar5 != (undefined8 *)0x0) {
                do {
                  puVar4 = puVar5;
                  puVar5 = (undefined8 *)*puVar4;
                } while ((undefined8 *)*puVar4 != (undefined8 *)0x0);
                puVar5 = (undefined8 *)puVar4[1];
              }
            }
          }
        }
        plVar6 = (long *)param_2[1];
        plVar8 = param_2;
        if ((long *)param_2[1] == (long *)0x0) {
          do {
            param_2 = (long *)plVar8[2];
            bVar3 = (long *)*param_2 != plVar8;
            plVar8 = param_2;
                    /* try { // try from 00a2f138 to 00b2f143 has its CatchHandler @ 00a2fde0 */
          } while (bVar3);
        }
        else {
          do {
            param_2 = plVar6;
            plVar6 = (long *)*param_2;
          } while ((long *)*param_2 != (long *)0x0);
        }
        bVar3 = puVar9 != (undefined8 *)0x0;
        puVar5 = puVar9;
        puVar9 = puVar4;
      } while (bVar3);
      FUN_0086c30c(param_1,puVar5);
      if (puVar4 == (undefined8 *)0x0) goto LAB_00a2f1e0;
      puVar5 = (undefined8 *)puVar4[2];
      while (puVar9 = puVar5, puVar9 != (undefined8 *)0x0) {
        puVar4 = puVar9;
        puVar5 = (undefined8 *)puVar9[2];
      }
    }
    FUN_0086c30c(param_1,puVar4);
  }
LAB_00a2f1e0:
  if (param_2 != param_3) {
    plVar10 = param_1 + 1;
    do {
      puVar5 = (undefined8 *)_Znwm(0x28);
      uVar2 = *(undefined4 *)((long)param_2 + 0x24);
      plVar7 = (long *)*plVar10;
      *(undefined8 *)((long)puVar5 + 0x1c) = *(undefined8 *)((long)param_2 + 0x1c);
      *(undefined4 *)((long)puVar5 + 0x24) = uVar2;
      plVar6 = plVar10;
      plVar8 = plVar10;
      if (plVar7 != (long *)0x0) {
        do {
          while (plVar6 = plVar7, *(int *)((long)plVar6 + 0x1c) <= *(int *)((long)puVar5 + 0x1c)) {
            plVar7 = (long *)plVar6[1];
            if ((long *)plVar6[1] == (long *)0x0) {
              plVar8 = plVar6 + 1;
              goto LAB_00a2f260;
            }
          }
          plVar8 = plVar6;
          plVar7 = (long *)*plVar6;
        } while ((long *)*plVar6 != (long *)0x0);
      }
LAB_00a2f260:
      *puVar5 = 0;
      puVar5[1] = 0;
      puVar5[2] = plVar6;
      *plVar8 = (long)puVar5;
      if (*(long *)*param_1 != 0) {
        *param_1 = *(long *)*param_1;
        puVar5 = (undefined8 *)*plVar8;
      }
      FUN_0043bbe4(param_1[1],puVar5);
      plVar6 = (long *)param_2[1];
      param_1[2] = param_1[2] + 1;
      plVar8 = param_2;
      if (plVar6 == (long *)0x0) {
        do {
          param_2 = (long *)plVar8[2];
          bVar3 = (long *)*param_2 != plVar8;
          plVar8 = param_2;
        } while (bVar3);
      }
      else {
        do {
          param_2 = plVar6;
          plVar6 = (long *)*param_2;
        } while ((long *)*param_2 != (long *)0x0);
      }
    } while (param_2 != param_3);
  }
                    /* try { // try from 00a2f2c4 to 00b2f2cb has its CatchHandler @ 00a2fdd4 */
                    /* try { // try from 00a2f2d0 to 00b2f2e7 has its CatchHandler @ 00a2fcfc */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a2efbc"></a> `00a2efbc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00a2efc0"></a> `00a2efc0` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a2efc4"></a> `00a2efc4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a2efc8"></a> `00a2efc8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a2efcc"></a> `00a2efcc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a2efd0"></a> `00a2efd0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00a2efd4"></a> `00a2efd4` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00a2efd8"></a> `00a2efd8` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00a2efdc"></a> `00a2efdc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00a2efe0"></a> `00a2efe0` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00a2efe4"></a> `00a2efe4` | `e8 0f 00 b4` | cbz x8,0x00a2f1e0 | `CONDITIONAL_JUMP`
<a id="insn-00a2efe8"></a> `00a2efe8` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00a2efec"></a> `00a2efec` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00a2eff0"></a> `00a2eff0` | `08 8f 40 f8` | ldr x8,[x24, #0x8]! | `FALL_THROUGH`
<a id="insn-00a2eff4"></a> `00a2eff4` | `98 02 00 f9` | str x24,[x20] | `FALL_THROUGH`
<a id="insn-00a2eff8"></a> `00a2eff8` | `1f 09 00 f9` | str xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a2effc"></a> `00a2effc` | `9f 0a 00 f9` | str xzr,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f000"></a> `00a2f000` | `1f 03 00 f9` | str xzr,[x24] | `FALL_THROUGH`
<a id="insn-00a2f004"></a> `00a2f004` | `28 05 40 f9` | ldr x8,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f008"></a> `00a2f008` | `1f 01 00 f1` | cmp x8,#0x0 | `FALL_THROUGH`
<a id="insn-00a2f00c"></a> `00a2f00c` | `36 01 88 9a` | csel x22,x9,x8,eq | `FALL_THROUGH`
<a id="insn-00a2f010"></a> `00a2f010` | `d6 01 00 b4` | cbz x22,0x00a2f048 | `CONDITIONAL_JUMP`
<a id="insn-00a2f014"></a> `00a2f014` | `d7 0a 40 f9` | ldr x23,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f018"></a> `00a2f018` | `f7 02 00 b4` | cbz x23,0x00a2f074 | `CONDITIONAL_JUMP`
<a id="insn-00a2f01c"></a> `00a2f01c` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00a2f020"></a> `00a2f020` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00a2f024"></a> `00a2f024` | `80 01 00 54` | b.eq 0x00a2f054 | `CONDITIONAL_JUMP`
<a id="insn-00a2f028"></a> `00a2f028` | `ff 06 00 f9` | str xzr,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f02c"></a> `00a2f02c` | `48 02 00 b4` | cbz x8,0x00a2f074 | `CONDITIONAL_JUMP`
<a id="insn-00a2f030"></a> `00a2f030` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00a2f034"></a> `00a2f034` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a2f038"></a> `00a2f038` | `c8 ff ff b5` | cbnz x8,0x00a2f030 | `CONDITIONAL_JUMP`
<a id="insn-00a2f03c"></a> `00a2f03c` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f040"></a> `00a2f040` | `88 ff ff b5` | cbnz x8,0x00a2f030 | `CONDITIONAL_JUMP`
<a id="insn-00a2f044"></a> `00a2f044` | `0c 00 00 14` | b 0x00a2f074 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f048"></a> `00a2f048` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a2f04c"></a> `00a2f04c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00a2f050"></a> `00a2f050` | `63 00 00 14` | b 0x00a2f1dc | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f054"></a> `00a2f054` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f058"></a> `00a2f058` | `ff 02 00 f9` | str xzr,[x23] | `FALL_THROUGH`
<a id="insn-00a2f05c"></a> `00a2f05c` | `c8 00 00 b4` | cbz x8,0x00a2f074 | `CONDITIONAL_JUMP`
<a id="insn-00a2f060"></a> `00a2f060` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00a2f064"></a> `00a2f064` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a2f068"></a> `00a2f068` | `c8 ff ff b5` | cbnz x8,0x00a2f060 | `CONDITIONAL_JUMP`
<a id="insn-00a2f06c"></a> `00a2f06c` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f070"></a> `00a2f070` | `88 ff ff b5` | cbnz x8,0x00a2f060 | `CONDITIONAL_JUMP`
<a id="insn-00a2f074"></a> `00a2f074` | `bf 02 13 eb` | cmp x21,x19 | `FALL_THROUGH`
<a id="insn-00a2f078"></a> `00a2f078` | `c0 09 00 54` | b.eq 0x00a2f1b0 | `CONDITIONAL_JUMP`
<a id="insn-00a2f07c"></a> `00a2f07c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00a2f080"></a> `00a2f080` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00a2f084"></a> `00a2f084` | `29 1f 40 b9` | ldr w9,[x25, #0x1c] | `FALL_THROUGH`
<a id="insn-00a2f088"></a> `00a2f088` | `f6 03 17 aa` | mov x22,x23 | `FALL_THROUGH`
<a id="insn-00a2f08c"></a> `00a2f08c` | `ea 03 18 aa` | mov x10,x24 | `FALL_THROUGH`
<a id="insn-00a2f090"></a> `00a2f090` | `29 1c 00 b9` | str w9,[x1, #0x1c] | `FALL_THROUGH`
<a id="insn-00a2f094"></a> `00a2f094` | `28 13 40 f9` | ldr x8,[x25, #0x20] | `FALL_THROUGH`
<a id="insn-00a2f098"></a> `00a2f098` | `28 10 00 f9` | str x8,[x1, #0x20] | `FALL_THROUGH`
<a id="insn-00a2f09c"></a> `00a2f09c` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00a2f0a0"></a> `00a2f0a0` | `0b 03 40 f9` | ldr x11,[x24] | `FALL_THROUGH`
<a id="insn-00a2f0a4"></a> `00a2f0a4` | `8b 00 00 b5` | cbnz x11,0x00a2f0b4 | `CONDITIONAL_JUMP`
<a id="insn-00a2f0a8"></a> `00a2f0a8` | `0c 00 00 14` | b 0x00a2f0d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f0ac"></a> `00a2f0ac` | `0b 05 40 f9` | ldr x11,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f0b0"></a> `00a2f0b0` | `2b 01 00 b4` | cbz x11,0x00a2f0d4 | `CONDITIONAL_JUMP`
<a id="insn-00a2f0b4"></a> `00a2f0b4` | `6a 1d 40 b9` | ldr w10,[x11, #0x1c] | `FALL_THROUGH`
<a id="insn-00a2f0b8"></a> `00a2f0b8` | `e8 03 0b aa` | mov x8,x11 | `FALL_THROUGH`
<a id="insn-00a2f0bc"></a> `00a2f0bc` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-00a2f0c0"></a> `00a2f0c0` | `6a ff ff 54` | b.ge 0x00a2f0ac | `CONDITIONAL_JUMP`
<a id="insn-00a2f0c4"></a> `00a2f0c4` | `0b 01 40 f9` | ldr x11,[x8] | `FALL_THROUGH`
<a id="insn-00a2f0c8"></a> `00a2f0c8` | `ea 03 08 aa` | mov x10,x8 | `FALL_THROUGH`
<a id="insn-00a2f0cc"></a> `00a2f0cc` | `4b ff ff b5` | cbnz x11,0x00a2f0b4 | `CONDITIONAL_JUMP`
<a id="insn-00a2f0d0"></a> `00a2f0d0` | `02 00 00 14` | b 0x00a2f0d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f0d4"></a> `00a2f0d4` | `0a 21 00 91` | add x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00a2f0d8"></a> `00a2f0d8` | `3f 7c 00 a9` | stp xzr,xzr,[x1] | `FALL_THROUGH`
<a id="insn-00a2f0dc"></a> `00a2f0dc` | `28 08 00 f9` | str x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f0e0"></a> `00a2f0e0` | `41 01 00 f9` | str x1,[x10] | `FALL_THROUGH`
<a id="insn-00a2f0e4"></a> `00a2f0e4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00a2f0e8"></a> `00a2f0e8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a2f0ec"></a> `00a2f0ec` | `68 00 00 b4` | cbz x8,0x00a2f0f8 | `CONDITIONAL_JUMP`
<a id="insn-00a2f0f0"></a> `00a2f0f0` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00a2f0f4"></a> `00a2f0f4` | `41 01 40 f9` | ldr x1,[x10] | `FALL_THROUGH`
<a id="insn-00a2f0f8"></a> `00a2f0f8` | `80 06 40 f9` | ldr x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f0fc"></a> `00a2f0fc` | `ba 32 e8 97` | bl 0x0043bbe4 | `UNCONDITIONAL_CALL`
<a id="insn-00a2f100"></a> `00a2f100` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f104"></a> `00a2f104` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00a2f108"></a> `00a2f108` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f10c"></a> `00a2f10c` | `76 02 00 b5` | cbnz x22,0x00a2f158 | `CONDITIONAL_JUMP`
<a id="insn-00a2f110"></a> `00a2f110` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00a2f114"></a> `00a2f114` | `28 07 40 f9` | ldr x8,[x25, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f118"></a> `00a2f118` | `a8 00 00 b4` | cbz x8,0x00a2f12c | `CONDITIONAL_JUMP`
<a id="insn-00a2f11c"></a> `00a2f11c` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00a2f120"></a> `00a2f120` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a2f124"></a> `00a2f124` | `c8 ff ff b5` | cbnz x8,0x00a2f11c | `CONDITIONAL_JUMP`
<a id="insn-00a2f128"></a> `00a2f128` | `06 00 00 14` | b 0x00a2f140 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f12c"></a> `00a2f12c` | `35 0b 40 f9` | ldr x21,[x25, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f130"></a> `00a2f130` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00a2f134"></a> `00a2f134` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00a2f138"></a> `00a2f138` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00a2f13c"></a> `00a2f13c` | `81 ff ff 54` | b.ne 0x00a2f12c | `CONDITIONAL_JUMP`
<a id="insn-00a2f140"></a> `00a2f140` | `96 03 00 b4` | cbz x22,0x00a2f1b0 | `CONDITIONAL_JUMP`
<a id="insn-00a2f144"></a> `00a2f144` | `bf 02 13 eb` | cmp x21,x19 | `FALL_THROUGH`
<a id="insn-00a2f148"></a> `00a2f148` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00a2f14c"></a> `00a2f14c` | `f9 03 15 aa` | mov x25,x21 | `FALL_THROUGH`
<a id="insn-00a2f150"></a> `00a2f150` | `a1 f9 ff 54` | b.ne 0x00a2f084 | `CONDITIONAL_JUMP`
<a id="insn-00a2f154"></a> `00a2f154` | `17 00 00 14` | b 0x00a2f1b0 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f158"></a> `00a2f158` | `d7 0a 40 f9` | ldr x23,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f15c"></a> `00a2f15c` | `d7 fd ff b4` | cbz x23,0x00a2f114 | `CONDITIONAL_JUMP`
<a id="insn-00a2f160"></a> `00a2f160` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00a2f164"></a> `00a2f164` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00a2f168"></a> `00a2f168` | `20 01 00 54` | b.eq 0x00a2f18c | `CONDITIONAL_JUMP`
<a id="insn-00a2f16c"></a> `00a2f16c` | `ff 06 00 f9` | str xzr,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f170"></a> `00a2f170` | `28 fd ff b4` | cbz x8,0x00a2f114 | `CONDITIONAL_JUMP`
<a id="insn-00a2f174"></a> `00a2f174` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00a2f178"></a> `00a2f178` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a2f17c"></a> `00a2f17c` | `c8 ff ff b5` | cbnz x8,0x00a2f174 | `CONDITIONAL_JUMP`
<a id="insn-00a2f180"></a> `00a2f180` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f184"></a> `00a2f184` | `88 ff ff b5` | cbnz x8,0x00a2f174 | `CONDITIONAL_JUMP`
<a id="insn-00a2f188"></a> `00a2f188` | `e3 ff ff 17` | b 0x00a2f114 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f18c"></a> `00a2f18c` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f190"></a> `00a2f190` | `ff 02 00 f9` | str xzr,[x23] | `FALL_THROUGH`
<a id="insn-00a2f194"></a> `00a2f194` | `08 fc ff b4` | cbz x8,0x00a2f114 | `CONDITIONAL_JUMP`
<a id="insn-00a2f198"></a> `00a2f198` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00a2f19c"></a> `00a2f19c` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a2f1a0"></a> `00a2f1a0` | `c8 ff ff b5` | cbnz x8,0x00a2f198 | `CONDITIONAL_JUMP`
<a id="insn-00a2f1a4"></a> `00a2f1a4` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f1a8"></a> `00a2f1a8` | `88 ff ff b5` | cbnz x8,0x00a2f198 | `CONDITIONAL_JUMP`
<a id="insn-00a2f1ac"></a> `00a2f1ac` | `da ff ff 17` | b 0x00a2f114 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f1b0"></a> `00a2f1b0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a2f1b4"></a> `00a2f1b4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00a2f1b8"></a> `00a2f1b8` | `55 f4 f8 97` | bl 0x0086c30c | `UNCONDITIONAL_CALL`
<a id="insn-00a2f1bc"></a> `00a2f1bc` | `37 01 00 b4` | cbz x23,0x00a2f1e0 | `CONDITIONAL_JUMP`
<a id="insn-00a2f1c0"></a> `00a2f1c0` | `e8 0a 40 f9` | ldr x8,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f1c4"></a> `00a2f1c4` | `88 00 00 b4` | cbz x8,0x00a2f1d4 | `CONDITIONAL_JUMP`
<a id="insn-00a2f1c8"></a> `00a2f1c8` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00a2f1cc"></a> `00a2f1cc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f1d0"></a> `00a2f1d0` | `c8 ff ff b5` | cbnz x8,0x00a2f1c8 | `CONDITIONAL_JUMP`
<a id="insn-00a2f1d4"></a> `00a2f1d4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a2f1d8"></a> `00a2f1d8` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00a2f1dc"></a> `00a2f1dc` | `4c f4 f8 97` | bl 0x0086c30c | `UNCONDITIONAL_CALL`
<a id="insn-00a2f1e0"></a> `00a2f1e0` | `bf 02 13 eb` | cmp x21,x19 | `FALL_THROUGH`
<a id="insn-00a2f1e4"></a> `00a2f1e4` | `00 07 00 54` | b.eq 0x00a2f2c4 | `CONDITIONAL_JUMP`
<a id="insn-00a2f1e8"></a> `00a2f1e8` | `96 22 00 91` | add x22,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00a2f1ec"></a> `00a2f1ec` | `04 00 00 14` | b 0x00a2f1fc | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f1f0"></a> `00a2f1f0` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00a2f1f4"></a> `00a2f1f4` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00a2f1f8"></a> `00a2f1f8` | `60 06 00 54` | b.eq 0x00a2f2c4 | `CONDITIONAL_JUMP`
<a id="insn-00a2f1fc"></a> `00a2f1fc` | `00 05 80 52` | mov w0,#0x28 | `FALL_THROUGH`
<a id="insn-00a2f200"></a> `00a2f200` | `58 a3 08 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00a2f204"></a> `00a2f204` | `a8 c2 41 f8` | ldur x8,[x21, #0x1c] | `FALL_THROUGH`
<a id="insn-00a2f208"></a> `00a2f208` | `a9 26 40 b9` | ldr w9,[x21, #0x24] | `FALL_THROUGH`
<a id="insn-00a2f20c"></a> `00a2f20c` | `eb 03 00 aa` | mov x11,x0 | `FALL_THROUGH`
<a id="insn-00a2f210"></a> `00a2f210` | `ca 02 40 f9` | ldr x10,[x22] | `FALL_THROUGH`
<a id="insn-00a2f214"></a> `00a2f214` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00a2f218"></a> `00a2f218` | `68 cd 01 f8` | str x8,[x11, #0x1c]! | `FALL_THROUGH`
<a id="insn-00a2f21c"></a> `00a2f21c` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00a2f220"></a> `00a2f220` | `09 24 00 b9` | str w9,[x0, #0x24] | `FALL_THROUGH`
<a id="insn-00a2f224"></a> `00a2f224` | `e9 03 16 aa` | mov x9,x22 | `FALL_THROUGH`
<a id="insn-00a2f228"></a> `00a2f228` | `ca 01 00 b4` | cbz x10,0x00a2f260 | `CONDITIONAL_JUMP`
<a id="insn-00a2f22c"></a> `00a2f22c` | `6b 01 40 b9` | ldr w11,[x11] | `FALL_THROUGH`
<a id="insn-00a2f230"></a> `00a2f230` | `03 00 00 14` | b 0x00a2f23c | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f234"></a> `00a2f234` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f238"></a> `00a2f238` | `2a 01 00 b4` | cbz x10,0x00a2f25c | `CONDITIONAL_JUMP`
<a id="insn-00a2f23c"></a> `00a2f23c` | `49 1d 40 b9` | ldr w9,[x10, #0x1c] | `FALL_THROUGH`
<a id="insn-00a2f240"></a> `00a2f240` | `e8 03 0a aa` | mov x8,x10 | `FALL_THROUGH`
<a id="insn-00a2f244"></a> `00a2f244` | `7f 01 09 6b` | cmp w11,w9 | `FALL_THROUGH`
<a id="insn-00a2f248"></a> `00a2f248` | `6a ff ff 54` | b.ge 0x00a2f234 | `CONDITIONAL_JUMP`
<a id="insn-00a2f24c"></a> `00a2f24c` | `0a 01 40 f9` | ldr x10,[x8] | `FALL_THROUGH`
<a id="insn-00a2f250"></a> `00a2f250` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00a2f254"></a> `00a2f254` | `4a ff ff b5` | cbnz x10,0x00a2f23c | `CONDITIONAL_JUMP`
<a id="insn-00a2f258"></a> `00a2f258` | `02 00 00 14` | b 0x00a2f260 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f25c"></a> `00a2f25c` | `09 21 00 91` | add x9,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00a2f260"></a> `00a2f260` | `3f 7c 00 a9` | stp xzr,xzr,[x1] | `FALL_THROUGH`
<a id="insn-00a2f264"></a> `00a2f264` | `28 08 00 f9` | str x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f268"></a> `00a2f268` | `21 01 00 f9` | str x1,[x9] | `FALL_THROUGH`
<a id="insn-00a2f26c"></a> `00a2f26c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00a2f270"></a> `00a2f270` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00a2f274"></a> `00a2f274` | `68 00 00 b4` | cbz x8,0x00a2f280 | `CONDITIONAL_JUMP`
<a id="insn-00a2f278"></a> `00a2f278` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00a2f27c"></a> `00a2f27c` | `21 01 40 f9` | ldr x1,[x9] | `FALL_THROUGH`
<a id="insn-00a2f280"></a> `00a2f280` | `80 06 40 f9` | ldr x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f284"></a> `00a2f284` | `58 32 e8 97` | bl 0x0043bbe4 | `UNCONDITIONAL_CALL`
<a id="insn-00a2f288"></a> `00a2f288` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f28c"></a> `00a2f28c` | `a9 06 40 f9` | ldr x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00a2f290"></a> `00a2f290` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00a2f294"></a> `00a2f294` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f298"></a> `00a2f298` | `a9 00 00 b4` | cbz x9,0x00a2f2ac | `CONDITIONAL_JUMP`
<a id="insn-00a2f29c"></a> `00a2f29c` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00a2f2a0"></a> `00a2f2a0` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00a2f2a4"></a> `00a2f2a4` | `c9 ff ff b5` | cbnz x9,0x00a2f29c | `CONDITIONAL_JUMP`
<a id="insn-00a2f2a8"></a> `00a2f2a8` | `d2 ff ff 17` | b 0x00a2f1f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f2ac"></a> `00a2f2ac` | `a8 0a 40 f9` | ldr x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f2b0"></a> `00a2f2b0` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00a2f2b4"></a> `00a2f2b4` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00a2f2b8"></a> `00a2f2b8` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00a2f2bc"></a> `00a2f2bc` | `81 ff ff 54` | b.ne 0x00a2f2ac | `CONDITIONAL_JUMP`
<a id="insn-00a2f2c0"></a> `00a2f2c0` | `cc ff ff 17` | b 0x00a2f1f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00a2f2c4"></a> `00a2f2c4` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00a2f2c8"></a> `00a2f2c8` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a2f2cc"></a> `00a2f2cc` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00a2f2d0"></a> `00a2f2d0` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a2f2d4"></a> `00a2f2d4` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00a2f2d8"></a> `00a2f2d8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a2efbc`](#insn-00a2efbc) 範囲 `[['00a2efbc', '00a2efcf']]`
  - `FALL_THROUGH` [`00a2efcc`](#insn-00a2efcc) → [`00a2efd0`](#insn-00a2efd0)
- ブロック [`00a2efd0`](#insn-00a2efd0) 範囲 `[['00a2efd0', '00a2efe7']]`
  - `CONDITIONAL_JUMP` [`00a2efe4`](#insn-00a2efe4) → [`00a2f1e0`](#insn-00a2f1e0)
  - `FALL_THROUGH` [`00a2efe4`](#insn-00a2efe4) → [`00a2efe8`](#insn-00a2efe8)
- ブロック [`00a2efe8`](#insn-00a2efe8) 範囲 `[['00a2efe8', '00a2f013']]`
  - `CONDITIONAL_JUMP` [`00a2f010`](#insn-00a2f010) → [`00a2f048`](#insn-00a2f048)
  - `FALL_THROUGH` [`00a2f010`](#insn-00a2f010) → [`00a2f014`](#insn-00a2f014)
- ブロック [`00a2f014`](#insn-00a2f014) 範囲 `[['00a2f014', '00a2f01b']]`
  - `CONDITIONAL_JUMP` [`00a2f018`](#insn-00a2f018) → [`00a2f074`](#insn-00a2f074)
  - `FALL_THROUGH` [`00a2f018`](#insn-00a2f018) → [`00a2f01c`](#insn-00a2f01c)
- ブロック [`00a2f01c`](#insn-00a2f01c) 範囲 `[['00a2f01c', '00a2f027']]`
  - `CONDITIONAL_JUMP` [`00a2f024`](#insn-00a2f024) → [`00a2f054`](#insn-00a2f054)
  - `FALL_THROUGH` [`00a2f024`](#insn-00a2f024) → [`00a2f028`](#insn-00a2f028)
- ブロック [`00a2f028`](#insn-00a2f028) 範囲 `[['00a2f028', '00a2f02f']]`
  - `CONDITIONAL_JUMP` [`00a2f02c`](#insn-00a2f02c) → [`00a2f074`](#insn-00a2f074)
  - `FALL_THROUGH` [`00a2f02c`](#insn-00a2f02c) → [`00a2f030`](#insn-00a2f030)
- ブロック [`00a2f030`](#insn-00a2f030) 範囲 `[['00a2f030', '00a2f03b']]`
  - `CONDITIONAL_JUMP` [`00a2f038`](#insn-00a2f038) → [`00a2f030`](#insn-00a2f030)
  - `FALL_THROUGH` [`00a2f038`](#insn-00a2f038) → [`00a2f03c`](#insn-00a2f03c)
- ブロック [`00a2f03c`](#insn-00a2f03c) 範囲 `[['00a2f03c', '00a2f043']]`
  - `CONDITIONAL_JUMP` [`00a2f040`](#insn-00a2f040) → [`00a2f030`](#insn-00a2f030)
  - `FALL_THROUGH` [`00a2f040`](#insn-00a2f040) → [`00a2f044`](#insn-00a2f044)
- ブロック [`00a2f044`](#insn-00a2f044) 範囲 `[['00a2f044', '00a2f047']]`
  - `UNCONDITIONAL_JUMP` [`00a2f044`](#insn-00a2f044) → [`00a2f074`](#insn-00a2f074)
- ブロック [`00a2f048`](#insn-00a2f048) 範囲 `[['00a2f048', '00a2f053']]`
  - `UNCONDITIONAL_JUMP` [`00a2f050`](#insn-00a2f050) → [`00a2f1dc`](#insn-00a2f1dc)
- ブロック [`00a2f054`](#insn-00a2f054) 範囲 `[['00a2f054', '00a2f05f']]`
  - `CONDITIONAL_JUMP` [`00a2f05c`](#insn-00a2f05c) → [`00a2f074`](#insn-00a2f074)
  - `FALL_THROUGH` [`00a2f05c`](#insn-00a2f05c) → [`00a2f060`](#insn-00a2f060)
- ブロック [`00a2f060`](#insn-00a2f060) 範囲 `[['00a2f060', '00a2f06b']]`
  - `CONDITIONAL_JUMP` [`00a2f068`](#insn-00a2f068) → [`00a2f060`](#insn-00a2f060)
  - `FALL_THROUGH` [`00a2f068`](#insn-00a2f068) → [`00a2f06c`](#insn-00a2f06c)
- ブロック [`00a2f06c`](#insn-00a2f06c) 範囲 `[['00a2f06c', '00a2f073']]`
  - `CONDITIONAL_JUMP` [`00a2f070`](#insn-00a2f070) → [`00a2f060`](#insn-00a2f060)
  - `FALL_THROUGH` [`00a2f070`](#insn-00a2f070) → [`00a2f074`](#insn-00a2f074)
- ブロック [`00a2f074`](#insn-00a2f074) 範囲 `[['00a2f074', '00a2f07b']]`
  - `CONDITIONAL_JUMP` [`00a2f078`](#insn-00a2f078) → [`00a2f1b0`](#insn-00a2f1b0)
  - `FALL_THROUGH` [`00a2f078`](#insn-00a2f078) → [`00a2f07c`](#insn-00a2f07c)
- ブロック [`00a2f07c`](#insn-00a2f07c) 範囲 `[['00a2f07c', '00a2f083']]`
  - `FALL_THROUGH` [`00a2f080`](#insn-00a2f080) → [`00a2f084`](#insn-00a2f084)
- ブロック [`00a2f084`](#insn-00a2f084) 範囲 `[['00a2f084', '00a2f0a7']]`
  - `CONDITIONAL_JUMP` [`00a2f0a4`](#insn-00a2f0a4) → [`00a2f0b4`](#insn-00a2f0b4)
  - `FALL_THROUGH` [`00a2f0a4`](#insn-00a2f0a4) → [`00a2f0a8`](#insn-00a2f0a8)
- ブロック [`00a2f0a8`](#insn-00a2f0a8) 範囲 `[['00a2f0a8', '00a2f0ab']]`
  - `UNCONDITIONAL_JUMP` [`00a2f0a8`](#insn-00a2f0a8) → [`00a2f0d8`](#insn-00a2f0d8)
- ブロック [`00a2f0ac`](#insn-00a2f0ac) 範囲 `[['00a2f0ac', '00a2f0b3']]`
  - `CONDITIONAL_JUMP` [`00a2f0b0`](#insn-00a2f0b0) → [`00a2f0d4`](#insn-00a2f0d4)
  - `FALL_THROUGH` [`00a2f0b0`](#insn-00a2f0b0) → [`00a2f0b4`](#insn-00a2f0b4)
- ブロック [`00a2f0b4`](#insn-00a2f0b4) 範囲 `[['00a2f0b4', '00a2f0c3']]`
  - `CONDITIONAL_JUMP` [`00a2f0c0`](#insn-00a2f0c0) → [`00a2f0ac`](#insn-00a2f0ac)
  - `FALL_THROUGH` [`00a2f0c0`](#insn-00a2f0c0) → [`00a2f0c4`](#insn-00a2f0c4)
- ブロック [`00a2f0c4`](#insn-00a2f0c4) 範囲 `[['00a2f0c4', '00a2f0cf']]`
  - `CONDITIONAL_JUMP` [`00a2f0cc`](#insn-00a2f0cc) → [`00a2f0b4`](#insn-00a2f0b4)
  - `FALL_THROUGH` [`00a2f0cc`](#insn-00a2f0cc) → [`00a2f0d0`](#insn-00a2f0d0)
- ブロック [`00a2f0d0`](#insn-00a2f0d0) 範囲 `[['00a2f0d0', '00a2f0d3']]`
  - `UNCONDITIONAL_JUMP` [`00a2f0d0`](#insn-00a2f0d0) → [`00a2f0d8`](#insn-00a2f0d8)
- ブロック [`00a2f0d4`](#insn-00a2f0d4) 範囲 `[['00a2f0d4', '00a2f0d7']]`
  - `FALL_THROUGH` [`00a2f0d4`](#insn-00a2f0d4) → [`00a2f0d8`](#insn-00a2f0d8)
- ブロック [`00a2f0d8`](#insn-00a2f0d8) 範囲 `[['00a2f0d8', '00a2f0ef']]`
  - `CONDITIONAL_JUMP` [`00a2f0ec`](#insn-00a2f0ec) → [`00a2f0f8`](#insn-00a2f0f8)
  - `FALL_THROUGH` [`00a2f0ec`](#insn-00a2f0ec) → [`00a2f0f0`](#insn-00a2f0f0)
- ブロック [`00a2f0f0`](#insn-00a2f0f0) 範囲 `[['00a2f0f0', '00a2f0f7']]`
  - `FALL_THROUGH` [`00a2f0f4`](#insn-00a2f0f4) → [`00a2f0f8`](#insn-00a2f0f8)
- ブロック [`00a2f0f8`](#insn-00a2f0f8) 範囲 `[['00a2f0f8', '00a2f10f']]`
  - `CONDITIONAL_JUMP` [`00a2f10c`](#insn-00a2f10c) → [`00a2f158`](#insn-00a2f158)
  - `FALL_THROUGH` [`00a2f10c`](#insn-00a2f10c) → [`00a2f110`](#insn-00a2f110)
- ブロック [`00a2f110`](#insn-00a2f110) 範囲 `[['00a2f110', '00a2f113']]`
  - `FALL_THROUGH` [`00a2f110`](#insn-00a2f110) → [`00a2f114`](#insn-00a2f114)
- ブロック [`00a2f114`](#insn-00a2f114) 範囲 `[['00a2f114', '00a2f11b']]`
  - `CONDITIONAL_JUMP` [`00a2f118`](#insn-00a2f118) → [`00a2f12c`](#insn-00a2f12c)
  - `FALL_THROUGH` [`00a2f118`](#insn-00a2f118) → [`00a2f11c`](#insn-00a2f11c)
- ブロック [`00a2f11c`](#insn-00a2f11c) 範囲 `[['00a2f11c', '00a2f127']]`
  - `CONDITIONAL_JUMP` [`00a2f124`](#insn-00a2f124) → [`00a2f11c`](#insn-00a2f11c)
  - `FALL_THROUGH` [`00a2f124`](#insn-00a2f124) → [`00a2f128`](#insn-00a2f128)
- ブロック [`00a2f128`](#insn-00a2f128) 範囲 `[['00a2f128', '00a2f12b']]`
  - `UNCONDITIONAL_JUMP` [`00a2f128`](#insn-00a2f128) → [`00a2f140`](#insn-00a2f140)
- ブロック [`00a2f12c`](#insn-00a2f12c) 範囲 `[['00a2f12c', '00a2f137']]`
  - `FALL_THROUGH` [`00a2f134`](#insn-00a2f134) → [`00a2f138`](#insn-00a2f138)
- ブロック [`00a2f138`](#insn-00a2f138) 範囲 `[['00a2f138', '00a2f13f']]`
  - `CONDITIONAL_JUMP` [`00a2f13c`](#insn-00a2f13c) → [`00a2f12c`](#insn-00a2f12c)
  - `FALL_THROUGH` [`00a2f13c`](#insn-00a2f13c) → [`00a2f140`](#insn-00a2f140)
- ブロック [`00a2f140`](#insn-00a2f140) 範囲 `[['00a2f140', '00a2f143']]`
  - `CONDITIONAL_JUMP` [`00a2f140`](#insn-00a2f140) → [`00a2f1b0`](#insn-00a2f1b0)
  - `FALL_THROUGH` [`00a2f140`](#insn-00a2f140) → [`00a2f144`](#insn-00a2f144)
- ブロック [`00a2f144`](#insn-00a2f144) 範囲 `[['00a2f144', '00a2f153']]`
  - `CONDITIONAL_JUMP` [`00a2f150`](#insn-00a2f150) → [`00a2f084`](#insn-00a2f084)
  - `FALL_THROUGH` [`00a2f150`](#insn-00a2f150) → [`00a2f154`](#insn-00a2f154)
- ブロック [`00a2f154`](#insn-00a2f154) 範囲 `[['00a2f154', '00a2f157']]`
  - `UNCONDITIONAL_JUMP` [`00a2f154`](#insn-00a2f154) → [`00a2f1b0`](#insn-00a2f1b0)
- ブロック [`00a2f158`](#insn-00a2f158) 範囲 `[['00a2f158', '00a2f15f']]`
  - `CONDITIONAL_JUMP` [`00a2f15c`](#insn-00a2f15c) → [`00a2f114`](#insn-00a2f114)
  - `FALL_THROUGH` [`00a2f15c`](#insn-00a2f15c) → [`00a2f160`](#insn-00a2f160)
- ブロック [`00a2f160`](#insn-00a2f160) 範囲 `[['00a2f160', '00a2f16b']]`
  - `CONDITIONAL_JUMP` [`00a2f168`](#insn-00a2f168) → [`00a2f18c`](#insn-00a2f18c)
  - `FALL_THROUGH` [`00a2f168`](#insn-00a2f168) → [`00a2f16c`](#insn-00a2f16c)
- ブロック [`00a2f16c`](#insn-00a2f16c) 範囲 `[['00a2f16c', '00a2f16f']]`
  - `FALL_THROUGH` [`00a2f16c`](#insn-00a2f16c) → [`00a2f170`](#insn-00a2f170)
- ブロック [`00a2f170`](#insn-00a2f170) 範囲 `[['00a2f170', '00a2f173']]`
  - `CONDITIONAL_JUMP` [`00a2f170`](#insn-00a2f170) → [`00a2f114`](#insn-00a2f114)
  - `FALL_THROUGH` [`00a2f170`](#insn-00a2f170) → [`00a2f174`](#insn-00a2f174)
- ブロック [`00a2f174`](#insn-00a2f174) 範囲 `[['00a2f174', '00a2f17f']]`
  - `CONDITIONAL_JUMP` [`00a2f17c`](#insn-00a2f17c) → [`00a2f174`](#insn-00a2f174)
  - `FALL_THROUGH` [`00a2f17c`](#insn-00a2f17c) → [`00a2f180`](#insn-00a2f180)
- ブロック [`00a2f180`](#insn-00a2f180) 範囲 `[['00a2f180', '00a2f187']]`
  - `CONDITIONAL_JUMP` [`00a2f184`](#insn-00a2f184) → [`00a2f174`](#insn-00a2f174)
  - `FALL_THROUGH` [`00a2f184`](#insn-00a2f184) → [`00a2f188`](#insn-00a2f188)
- ブロック [`00a2f188`](#insn-00a2f188) 範囲 `[['00a2f188', '00a2f18b']]`
  - `UNCONDITIONAL_JUMP` [`00a2f188`](#insn-00a2f188) → [`00a2f114`](#insn-00a2f114)
- ブロック [`00a2f18c`](#insn-00a2f18c) 範囲 `[['00a2f18c', '00a2f193']]`
  - `FALL_THROUGH` [`00a2f190`](#insn-00a2f190) → [`00a2f194`](#insn-00a2f194)
- ブロック [`00a2f194`](#insn-00a2f194) 範囲 `[['00a2f194', '00a2f197']]`
  - `CONDITIONAL_JUMP` [`00a2f194`](#insn-00a2f194) → [`00a2f114`](#insn-00a2f114)
  - `FALL_THROUGH` [`00a2f194`](#insn-00a2f194) → [`00a2f198`](#insn-00a2f198)
- ブロック [`00a2f198`](#insn-00a2f198) 範囲 `[['00a2f198', '00a2f1a3']]`
  - `CONDITIONAL_JUMP` [`00a2f1a0`](#insn-00a2f1a0) → [`00a2f198`](#insn-00a2f198)
  - `FALL_THROUGH` [`00a2f1a0`](#insn-00a2f1a0) → [`00a2f1a4`](#insn-00a2f1a4)
- ブロック [`00a2f1a4`](#insn-00a2f1a4) 範囲 `[['00a2f1a4', '00a2f1ab']]`
  - `CONDITIONAL_JUMP` [`00a2f1a8`](#insn-00a2f1a8) → [`00a2f198`](#insn-00a2f198)
  - `FALL_THROUGH` [`00a2f1a8`](#insn-00a2f1a8) → [`00a2f1ac`](#insn-00a2f1ac)
- ブロック [`00a2f1ac`](#insn-00a2f1ac) 範囲 `[['00a2f1ac', '00a2f1af']]`
  - `UNCONDITIONAL_JUMP` [`00a2f1ac`](#insn-00a2f1ac) → [`00a2f114`](#insn-00a2f114)
- ブロック [`00a2f1b0`](#insn-00a2f1b0) 範囲 `[['00a2f1b0', '00a2f1bf']]`
  - `CONDITIONAL_JUMP` [`00a2f1bc`](#insn-00a2f1bc) → [`00a2f1e0`](#insn-00a2f1e0)
  - `FALL_THROUGH` [`00a2f1bc`](#insn-00a2f1bc) → [`00a2f1c0`](#insn-00a2f1c0)
- ブロック [`00a2f1c0`](#insn-00a2f1c0) 範囲 `[['00a2f1c0', '00a2f1c7']]`
  - `CONDITIONAL_JUMP` [`00a2f1c4`](#insn-00a2f1c4) → [`00a2f1d4`](#insn-00a2f1d4)
  - `FALL_THROUGH` [`00a2f1c4`](#insn-00a2f1c4) → [`00a2f1c8`](#insn-00a2f1c8)
- ブロック [`00a2f1c8`](#insn-00a2f1c8) 範囲 `[['00a2f1c8', '00a2f1d3']]`
  - `CONDITIONAL_JUMP` [`00a2f1d0`](#insn-00a2f1d0) → [`00a2f1c8`](#insn-00a2f1c8)
  - `FALL_THROUGH` [`00a2f1d0`](#insn-00a2f1d0) → [`00a2f1d4`](#insn-00a2f1d4)
- ブロック [`00a2f1d4`](#insn-00a2f1d4) 範囲 `[['00a2f1d4', '00a2f1db']]`
  - `FALL_THROUGH` [`00a2f1d8`](#insn-00a2f1d8) → [`00a2f1dc`](#insn-00a2f1dc)
- ブロック [`00a2f1dc`](#insn-00a2f1dc) 範囲 `[['00a2f1dc', '00a2f1df']]`
  - `FALL_THROUGH` [`00a2f1dc`](#insn-00a2f1dc) → [`00a2f1e0`](#insn-00a2f1e0)
- ブロック [`00a2f1e0`](#insn-00a2f1e0) 範囲 `[['00a2f1e0', '00a2f1e7']]`
  - `CONDITIONAL_JUMP` [`00a2f1e4`](#insn-00a2f1e4) → [`00a2f2c4`](#insn-00a2f2c4)
  - `FALL_THROUGH` [`00a2f1e4`](#insn-00a2f1e4) → [`00a2f1e8`](#insn-00a2f1e8)
- ブロック [`00a2f1e8`](#insn-00a2f1e8) 範囲 `[['00a2f1e8', '00a2f1ef']]`
  - `UNCONDITIONAL_JUMP` [`00a2f1ec`](#insn-00a2f1ec) → [`00a2f1fc`](#insn-00a2f1fc)
- ブロック [`00a2f1f0`](#insn-00a2f1f0) 範囲 `[['00a2f1f0', '00a2f1fb']]`
  - `CONDITIONAL_JUMP` [`00a2f1f8`](#insn-00a2f1f8) → [`00a2f2c4`](#insn-00a2f2c4)
  - `FALL_THROUGH` [`00a2f1f8`](#insn-00a2f1f8) → [`00a2f1fc`](#insn-00a2f1fc)
- ブロック [`00a2f1fc`](#insn-00a2f1fc) 範囲 `[['00a2f1fc', '00a2f22b']]`
  - `CONDITIONAL_JUMP` [`00a2f228`](#insn-00a2f228) → [`00a2f260`](#insn-00a2f260)
  - `FALL_THROUGH` [`00a2f228`](#insn-00a2f228) → [`00a2f22c`](#insn-00a2f22c)
- ブロック [`00a2f22c`](#insn-00a2f22c) 範囲 `[['00a2f22c', '00a2f233']]`
  - `UNCONDITIONAL_JUMP` [`00a2f230`](#insn-00a2f230) → [`00a2f23c`](#insn-00a2f23c)
- ブロック [`00a2f234`](#insn-00a2f234) 範囲 `[['00a2f234', '00a2f23b']]`
  - `CONDITIONAL_JUMP` [`00a2f238`](#insn-00a2f238) → [`00a2f25c`](#insn-00a2f25c)
  - `FALL_THROUGH` [`00a2f238`](#insn-00a2f238) → [`00a2f23c`](#insn-00a2f23c)
- ブロック [`00a2f23c`](#insn-00a2f23c) 範囲 `[['00a2f23c', '00a2f24b']]`
  - `CONDITIONAL_JUMP` [`00a2f248`](#insn-00a2f248) → [`00a2f234`](#insn-00a2f234)
  - `FALL_THROUGH` [`00a2f248`](#insn-00a2f248) → [`00a2f24c`](#insn-00a2f24c)
- ブロック [`00a2f24c`](#insn-00a2f24c) 範囲 `[['00a2f24c', '00a2f257']]`
  - `CONDITIONAL_JUMP` [`00a2f254`](#insn-00a2f254) → [`00a2f23c`](#insn-00a2f23c)
  - `FALL_THROUGH` [`00a2f254`](#insn-00a2f254) → [`00a2f258`](#insn-00a2f258)
- ブロック [`00a2f258`](#insn-00a2f258) 範囲 `[['00a2f258', '00a2f25b']]`
  - `UNCONDITIONAL_JUMP` [`00a2f258`](#insn-00a2f258) → [`00a2f260`](#insn-00a2f260)
- ブロック [`00a2f25c`](#insn-00a2f25c) 範囲 `[['00a2f25c', '00a2f25f']]`
  - `FALL_THROUGH` [`00a2f25c`](#insn-00a2f25c) → [`00a2f260`](#insn-00a2f260)
- ブロック [`00a2f260`](#insn-00a2f260) 範囲 `[['00a2f260', '00a2f277']]`
  - `CONDITIONAL_JUMP` [`00a2f274`](#insn-00a2f274) → [`00a2f280`](#insn-00a2f280)
  - `FALL_THROUGH` [`00a2f274`](#insn-00a2f274) → [`00a2f278`](#insn-00a2f278)
- ブロック [`00a2f278`](#insn-00a2f278) 範囲 `[['00a2f278', '00a2f27f']]`
  - `FALL_THROUGH` [`00a2f27c`](#insn-00a2f27c) → [`00a2f280`](#insn-00a2f280)
- ブロック [`00a2f280`](#insn-00a2f280) 範囲 `[['00a2f280', '00a2f29b']]`
  - `CONDITIONAL_JUMP` [`00a2f298`](#insn-00a2f298) → [`00a2f2ac`](#insn-00a2f2ac)
  - `FALL_THROUGH` [`00a2f298`](#insn-00a2f298) → [`00a2f29c`](#insn-00a2f29c)
- ブロック [`00a2f29c`](#insn-00a2f29c) 範囲 `[['00a2f29c', '00a2f2a7']]`
  - `CONDITIONAL_JUMP` [`00a2f2a4`](#insn-00a2f2a4) → [`00a2f29c`](#insn-00a2f29c)
  - `FALL_THROUGH` [`00a2f2a4`](#insn-00a2f2a4) → [`00a2f2a8`](#insn-00a2f2a8)
- ブロック [`00a2f2a8`](#insn-00a2f2a8) 範囲 `[['00a2f2a8', '00a2f2ab']]`
  - `UNCONDITIONAL_JUMP` [`00a2f2a8`](#insn-00a2f2a8) → [`00a2f1f0`](#insn-00a2f1f0)
- ブロック [`00a2f2ac`](#insn-00a2f2ac) 範囲 `[['00a2f2ac', '00a2f2bf']]`
  - `CONDITIONAL_JUMP` [`00a2f2bc`](#insn-00a2f2bc) → [`00a2f2ac`](#insn-00a2f2ac)
  - `FALL_THROUGH` [`00a2f2bc`](#insn-00a2f2bc) → [`00a2f2c0`](#insn-00a2f2c0)
- ブロック [`00a2f2c0`](#insn-00a2f2c0) 範囲 `[['00a2f2c0', '00a2f2c3']]`
  - `UNCONDITIONAL_JUMP` [`00a2f2c0`](#insn-00a2f2c0) → [`00a2f1f0`](#insn-00a2f1f0)
- ブロック [`00a2f2c4`](#insn-00a2f2c4) 範囲 `[['00a2f2c4', '00a2f2cf']]`
  - `FALL_THROUGH` [`00a2f2cc`](#insn-00a2f2cc) → [`00a2f2d0`](#insn-00a2f2d0)
- ブロック [`00a2f2d0`](#insn-00a2f2d0) 範囲 `[['00a2f2d0', '00a2f2db']]`

## 命令位置別の参照

- [`00a2efbc`](#insn-00a2efbc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2efc0`](#insn-00a2efc0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2efc4`](#insn-00a2efc4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2efc8`](#insn-00a2efc8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2efcc`](#insn-00a2efcc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2efe4`](#insn-00a2efe4) → [`00a2f1e0`](#insn-00a2f1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f010`](#insn-00a2f010) → [`00a2f048`](#insn-00a2f048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f018`](#insn-00a2f018) → [`00a2f074`](#insn-00a2f074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f024`](#insn-00a2f024) → [`00a2f054`](#insn-00a2f054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f02c`](#insn-00a2f02c) → [`00a2f074`](#insn-00a2f074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f038`](#insn-00a2f038) → [`00a2f030`](#insn-00a2f030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f040`](#insn-00a2f040) → [`00a2f030`](#insn-00a2f030) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f044`](#insn-00a2f044) → [`00a2f074`](#insn-00a2f074) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f050`](#insn-00a2f050) → [`00a2f1dc`](#insn-00a2f1dc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f05c`](#insn-00a2f05c) → [`00a2f074`](#insn-00a2f074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f068`](#insn-00a2f068) → [`00a2f060`](#insn-00a2f060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f070`](#insn-00a2f070) → [`00a2f060`](#insn-00a2f060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f078`](#insn-00a2f078) → [`00a2f1b0`](#insn-00a2f1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f0a4`](#insn-00a2f0a4) → [`00a2f0b4`](#insn-00a2f0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f0a8`](#insn-00a2f0a8) → [`00a2f0d8`](#insn-00a2f0d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f0b0`](#insn-00a2f0b0) → [`00a2f0d4`](#insn-00a2f0d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f0c0`](#insn-00a2f0c0) → [`00a2f0ac`](#insn-00a2f0ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f0cc`](#insn-00a2f0cc) → [`00a2f0b4`](#insn-00a2f0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f0d0`](#insn-00a2f0d0) → [`00a2f0d8`](#insn-00a2f0d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f0ec`](#insn-00a2f0ec) → [`00a2f0f8`](#insn-00a2f0f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f0fc`](#insn-00a2f0fc) → [`0043bbe4`](../0043b/0043bbe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bbe4` · 推定シンボル `None` · 推定型 `None`
- [`00a2f10c`](#insn-00a2f10c) → [`00a2f158`](#insn-00a2f158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f118`](#insn-00a2f118) → [`00a2f12c`](#insn-00a2f12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f124`](#insn-00a2f124) → [`00a2f11c`](#insn-00a2f11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f128`](#insn-00a2f128) → [`00a2f140`](#insn-00a2f140) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f13c`](#insn-00a2f13c) → [`00a2f12c`](#insn-00a2f12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f140`](#insn-00a2f140) → [`00a2f1b0`](#insn-00a2f1b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f150`](#insn-00a2f150) → [`00a2f084`](#insn-00a2f084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f154`](#insn-00a2f154) → [`00a2f1b0`](#insn-00a2f1b0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f15c`](#insn-00a2f15c) → [`00a2f114`](#insn-00a2f114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f168`](#insn-00a2f168) → [`00a2f18c`](#insn-00a2f18c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f170`](#insn-00a2f170) → [`00a2f114`](#insn-00a2f114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f17c`](#insn-00a2f17c) → [`00a2f174`](#insn-00a2f174) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f184`](#insn-00a2f184) → [`00a2f174`](#insn-00a2f174) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f188`](#insn-00a2f188) → [`00a2f114`](#insn-00a2f114) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f194`](#insn-00a2f194) → [`00a2f114`](#insn-00a2f114) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f1a0`](#insn-00a2f1a0) → [`00a2f198`](#insn-00a2f198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f1a8`](#insn-00a2f1a8) → [`00a2f198`](#insn-00a2f198) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f1ac`](#insn-00a2f1ac) → [`00a2f114`](#insn-00a2f114) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f1b8`](#insn-00a2f1b8) → [`0086c30c`](../0086c/0086c30c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0086c30c` · 推定シンボル `None` · 推定型 `None`
- [`00a2f1bc`](#insn-00a2f1bc) → [`00a2f1e0`](#insn-00a2f1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f1c4`](#insn-00a2f1c4) → [`00a2f1d4`](#insn-00a2f1d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f1d0`](#insn-00a2f1d0) → [`00a2f1c8`](#insn-00a2f1c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f1dc`](#insn-00a2f1dc) → [`0086c30c`](../0086c/0086c30c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0086c30c` · 推定シンボル `None` · 推定型 `None`
- [`00a2f1e4`](#insn-00a2f1e4) → [`00a2f2c4`](#insn-00a2f2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f1ec`](#insn-00a2f1ec) → [`00a2f1fc`](#insn-00a2f1fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f1f8`](#insn-00a2f1f8) → [`00a2f2c4`](#insn-00a2f2c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f200`](#insn-00a2f200) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00a2f228`](#insn-00a2f228) → [`00a2f260`](#insn-00a2f260) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f230`](#insn-00a2f230) → [`00a2f23c`](#insn-00a2f23c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f238`](#insn-00a2f238) → [`00a2f25c`](#insn-00a2f25c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f248`](#insn-00a2f248) → [`00a2f234`](#insn-00a2f234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f254`](#insn-00a2f254) → [`00a2f23c`](#insn-00a2f23c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f258`](#insn-00a2f258) → [`00a2f260`](#insn-00a2f260) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f274`](#insn-00a2f274) → [`00a2f280`](#insn-00a2f280) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f284`](#insn-00a2f284) → [`0043bbe4`](../0043b/0043bbe4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043bbe4` · 推定シンボル `None` · 推定型 `None`
- [`00a2f298`](#insn-00a2f298) → [`00a2f2ac`](#insn-00a2f2ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f2a4`](#insn-00a2f2a4) → [`00a2f29c`](#insn-00a2f29c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f2a8`](#insn-00a2f2a8) → [`00a2f1f0`](#insn-00a2f1f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f2bc`](#insn-00a2f2bc) → [`00a2f2ac`](#insn-00a2f2ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f2c0`](#insn-00a2f2c0) → [`00a2f1f0`](#insn-00a2f1f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f2c4`](#insn-00a2f2c4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f2c8`](#insn-00a2f2c8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f2cc`](#insn-00a2f2cc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f2d0`](#insn-00a2f2d0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a2f2d4`](#insn-00a2f2d4) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a2efbc`](#insn-00a2efbc)

~~~json
{
  "source": "00a2efbc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2efc0`](#insn-00a2efc0)

~~~json
{
  "source": "00a2efc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2efc4`](#insn-00a2efc4)

~~~json
{
  "source": "00a2efc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2efc8`](#insn-00a2efc8)

~~~json
{
  "source": "00a2efc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2efcc`](#insn-00a2efcc)

~~~json
{
  "source": "00a2efcc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2efe4`](#insn-00a2efe4)

~~~json
{
  "source": "00a2efe4",
  "target": "00a2f1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f010`](#insn-00a2f010)

~~~json
{
  "source": "00a2f010",
  "target": "00a2f048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f018`](#insn-00a2f018)

~~~json
{
  "source": "00a2f018",
  "target": "00a2f074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f024`](#insn-00a2f024)

~~~json
{
  "source": "00a2f024",
  "target": "00a2f054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f02c`](#insn-00a2f02c)

~~~json
{
  "source": "00a2f02c",
  "target": "00a2f074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f038`](#insn-00a2f038)

~~~json
{
  "source": "00a2f038",
  "target": "00a2f030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f040`](#insn-00a2f040)

~~~json
{
  "source": "00a2f040",
  "target": "00a2f030",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f044`](#insn-00a2f044)

~~~json
{
  "source": "00a2f044",
  "target": "00a2f074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f050`](#insn-00a2f050)

~~~json
{
  "source": "00a2f050",
  "target": "00a2f1dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f05c`](#insn-00a2f05c)

~~~json
{
  "source": "00a2f05c",
  "target": "00a2f074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f068`](#insn-00a2f068)

~~~json
{
  "source": "00a2f068",
  "target": "00a2f060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f070`](#insn-00a2f070)

~~~json
{
  "source": "00a2f070",
  "target": "00a2f060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f078`](#insn-00a2f078)

~~~json
{
  "source": "00a2f078",
  "target": "00a2f1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f0a4`](#insn-00a2f0a4)

~~~json
{
  "source": "00a2f0a4",
  "target": "00a2f0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f0a8`](#insn-00a2f0a8)

~~~json
{
  "source": "00a2f0a8",
  "target": "00a2f0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f0b0`](#insn-00a2f0b0)

~~~json
{
  "source": "00a2f0b0",
  "target": "00a2f0d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f0c0`](#insn-00a2f0c0)

~~~json
{
  "source": "00a2f0c0",
  "target": "00a2f0ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f0cc`](#insn-00a2f0cc)

~~~json
{
  "source": "00a2f0cc",
  "target": "00a2f0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f0d0`](#insn-00a2f0d0)

~~~json
{
  "source": "00a2f0d0",
  "target": "00a2f0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f0ec`](#insn-00a2f0ec)

~~~json
{
  "source": "00a2f0ec",
  "target": "00a2f0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f0fc`](#insn-00a2f0fc)

~~~json
{
  "source": "00a2f0fc",
  "target": "0043bbe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2f10c`](#insn-00a2f10c)

~~~json
{
  "source": "00a2f10c",
  "target": "00a2f158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f118`](#insn-00a2f118)

~~~json
{
  "source": "00a2f118",
  "target": "00a2f12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f124`](#insn-00a2f124)

~~~json
{
  "source": "00a2f124",
  "target": "00a2f11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f128`](#insn-00a2f128)

~~~json
{
  "source": "00a2f128",
  "target": "00a2f140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f13c`](#insn-00a2f13c)

~~~json
{
  "source": "00a2f13c",
  "target": "00a2f12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f140`](#insn-00a2f140)

~~~json
{
  "source": "00a2f140",
  "target": "00a2f1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f150`](#insn-00a2f150)

~~~json
{
  "source": "00a2f150",
  "target": "00a2f084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f154`](#insn-00a2f154)

~~~json
{
  "source": "00a2f154",
  "target": "00a2f1b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f15c`](#insn-00a2f15c)

~~~json
{
  "source": "00a2f15c",
  "target": "00a2f114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f168`](#insn-00a2f168)

~~~json
{
  "source": "00a2f168",
  "target": "00a2f18c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f170`](#insn-00a2f170)

~~~json
{
  "source": "00a2f170",
  "target": "00a2f114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f17c`](#insn-00a2f17c)

~~~json
{
  "source": "00a2f17c",
  "target": "00a2f174",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f184`](#insn-00a2f184)

~~~json
{
  "source": "00a2f184",
  "target": "00a2f174",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f188`](#insn-00a2f188)

~~~json
{
  "source": "00a2f188",
  "target": "00a2f114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f194`](#insn-00a2f194)

~~~json
{
  "source": "00a2f194",
  "target": "00a2f114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f1a0`](#insn-00a2f1a0)

~~~json
{
  "source": "00a2f1a0",
  "target": "00a2f198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f1a8`](#insn-00a2f1a8)

~~~json
{
  "source": "00a2f1a8",
  "target": "00a2f198",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f1ac`](#insn-00a2f1ac)

~~~json
{
  "source": "00a2f1ac",
  "target": "00a2f114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f1b8`](#insn-00a2f1b8)

~~~json
{
  "source": "00a2f1b8",
  "target": "0086c30c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2f1bc`](#insn-00a2f1bc)

~~~json
{
  "source": "00a2f1bc",
  "target": "00a2f1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f1c4`](#insn-00a2f1c4)

~~~json
{
  "source": "00a2f1c4",
  "target": "00a2f1d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f1d0`](#insn-00a2f1d0)

~~~json
{
  "source": "00a2f1d0",
  "target": "00a2f1c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f1dc`](#insn-00a2f1dc)

~~~json
{
  "source": "00a2f1dc",
  "target": "0086c30c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2f1e4`](#insn-00a2f1e4)

~~~json
{
  "source": "00a2f1e4",
  "target": "00a2f2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f1ec`](#insn-00a2f1ec)

~~~json
{
  "source": "00a2f1ec",
  "target": "00a2f1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f1f8`](#insn-00a2f1f8)

~~~json
{
  "source": "00a2f1f8",
  "target": "00a2f2c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f200`](#insn-00a2f200)

~~~json
{
  "source": "00a2f200",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2f228`](#insn-00a2f228)

~~~json
{
  "source": "00a2f228",
  "target": "00a2f260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f230`](#insn-00a2f230)

~~~json
{
  "source": "00a2f230",
  "target": "00a2f23c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f238`](#insn-00a2f238)

~~~json
{
  "source": "00a2f238",
  "target": "00a2f25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f248`](#insn-00a2f248)

~~~json
{
  "source": "00a2f248",
  "target": "00a2f234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f254`](#insn-00a2f254)

~~~json
{
  "source": "00a2f254",
  "target": "00a2f23c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f258`](#insn-00a2f258)

~~~json
{
  "source": "00a2f258",
  "target": "00a2f260",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f274`](#insn-00a2f274)

~~~json
{
  "source": "00a2f274",
  "target": "00a2f280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f284`](#insn-00a2f284)

~~~json
{
  "source": "00a2f284",
  "target": "0043bbe4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a2f298`](#insn-00a2f298)

~~~json
{
  "source": "00a2f298",
  "target": "00a2f2ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f2a4`](#insn-00a2f2a4)

~~~json
{
  "source": "00a2f2a4",
  "target": "00a2f29c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f2a8`](#insn-00a2f2a8)

~~~json
{
  "source": "00a2f2a8",
  "target": "00a2f1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f2bc`](#insn-00a2f2bc)

~~~json
{
  "source": "00a2f2bc",
  "target": "00a2f2ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f2c0`](#insn-00a2f2c0)

~~~json
{
  "source": "00a2f2c0",
  "target": "00a2f1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f2c4`](#insn-00a2f2c4)

~~~json
{
  "source": "00a2f2c4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f2c8`](#insn-00a2f2c8)

~~~json
{
  "source": "00a2f2c8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f2cc`](#insn-00a2f2cc)

~~~json
{
  "source": "00a2f2cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f2d0`](#insn-00a2f2d0)

~~~json
{
  "source": "00a2f2d0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a2f2d4`](#insn-00a2f2d4)

~~~json
{
  "source": "00a2f2d4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
