# 00acefbc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00a71028`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00a71/00a71028.md) · 移動量 `+0x5df94`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-6b79b06e2c44c3ceb6874abbfb6bb050)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00acf1b8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00acf/00acf1b8.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0064.md#compare-f19bf68541bfe83f2d724b68974ba4ab)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acefbc",
  "name": "FUN_00acefbc",
  "size": 664,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b111b6ba1fb67dfbbe1229164038f1d4fa380d86d3dc0e14077388953ff3e08f",
  "source_text_sha256": "b111b6ba1fb67dfbbe1229164038f1d4fa380d86d3dc0e14077388953ff3e08f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acefbc",
        "00acf24f"
      ],
      [
        "00acf284",
        "00acf287"
      ]
    ],
    "bytes_sha256": "48dfdd4ba47f3c8af163b9b60ab67dedd42f57d2727cac45c9c7f8f848e7e719",
    "instruction_count": 166,
    "instruction_bytes": 664,
    "body_bytes": 664,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [006623ac](../00662/006623ac.md)
- [00662450](../00662/00662450.md)
- [006624f4](../00662/006624f4.md)
- [007de880](../007de/007de880.md)
- [00acc3d4](../00acc/00acc3d4.md)
- [00aec538](../00aec/00aec538.md)

## 呼び出し先

- [004428f0](../00442/004428f0.md)
- [00470800](../00470/00470800.md)
- [00acea58](../00ace/00acea58.md)
- [00aea9c8](../00aea/00aea9c8.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57c00](../00c57/00c57c00.md)

## 関連文字列（未確認候補）

~~~text
"map::at:  key not found"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 8405 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

ulong FUN_00acefbc(long param_1,int param_2)

{
  void *__src;
  long lVar1;
  short sVar2;
  size_t __n;
  long lVar3;
  int *piVar4;
  int *piVar5;
  undefined1 auVar6 [16];
  undefined1 auVar7 [16];
  undefined1 auVar8 [16];
  undefined1 auVar9 [16];
  undefined1 auVar10 [16];
  undefined8 uVar11;
  undefined8 uVar12;
  undefined8 uVar13;
  long *plVar14;
  bool bVar15;
  int iVar16;
  ulong uVar17;
  int *__dest;
  int *piVar18;
  ulong uVar20;
  ulong uVar21;
  long *plVar22;
  long *plVar23;
  uint uVar24;
  int iVar28;
  int iVar29;
  undefined1 auVar26 [16];
  int iVar30;
  char cVar31;
  undefined1 uVar32;
  undefined1 uVar33;
  undefined1 auVar34 [16];
  undefined8 local_80;
  undefined8 local_78;
  undefined8 uStack_70;
  long local_68;
  int *piVar19;
  undefined1 auVar25 [12];
  undefined1 auVar27 [16];
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  uVar17 = FUN_00acea58();
  uVar13 = _DAT_002c2928;
  uVar12 = _DAT_002c2920;
  if ((uVar17 & 1) == 0) {
    uVar17 = 0;
  }
  else {
    plVar22 = *(long **)(param_1 + 0x33c0);
    if (plVar22 == (long *)(param_1 + 0x33c8)) {
      iVar16 = -1;
    }
    else {
      iVar16 = -1;
      do {
        __src = (void *)plVar22[5];
        lVar1 = plVar22[6];
        sVar2 = (short)plVar22[4];
        local_78 = 0;
        uStack_70 = 0;
        __n = lVar1 - (long)__src;
        local_80 = 0;
        if (__n != 0) {
          if ((long)__n < 0) {
            if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_00470800(&local_80);
            }
            goto LAB_00acf284;
          }
          __dest = (int *)_Znwm(__n);
          memcpy(__dest,__src,__n);
          lVar1 = lVar1 - (long)__src;
          if (lVar1 != 0) {
            uVar17 = lVar1 - 4;
            piVar18 = __dest;
            if (0x1b < uVar17) {
              auVar26._0_8_ = CONCAT44(iVar16,iVar16);
              auVar26._8_4_ = iVar16;
              auVar26._12_4_ = iVar16;
              cVar31 = (char)(sVar2 >> 0xf);
              uVar32 = (undefined1)sVar2;
              uVar33 = (undefined1)((ushort)sVar2 >> 8);
              piVar18 = __dest + 4;
              uVar17 = (uVar17 >> 2) + 1;
              uVar20 = uVar17 & 0x7ffffffffffffff8;
              auVar34._8_8_ = auVar26._8_8_;
              auVar34._0_8_ = auVar26._0_8_;
              uVar21 = uVar20;
              do {
                piVar19 = piVar18 + -4;
                piVar4 = piVar18 + -2;
                piVar5 = piVar18 + 2;
                uVar11 = *(undefined8 *)piVar18;
                uVar21 = uVar21 - 8;
                piVar18 = piVar18 + 8;
                auVar6[3] = cVar31;
                auVar6._0_3_ = (int3)sVar2;
                auVar6[4] = uVar32;
                auVar6[5] = uVar33;
                auVar6[6] = cVar31;
                auVar6[7] = cVar31;
                auVar6[8] = uVar32;
                auVar6[9] = uVar33;
                auVar6[10] = cVar31;
                auVar6[0xb] = cVar31;
                auVar6[0xc] = uVar32;
                auVar6[0xd] = uVar33;
                auVar6[0xe] = cVar31;
                auVar6[0xf] = cVar31;
                auVar8._4_4_ = -(uint)((int)((ulong)*(undefined8 *)piVar19 >> 0x20) == param_2);
                auVar8._0_4_ = -(uint)((int)*(undefined8 *)piVar19 == param_2);
                auVar8._8_4_ = -(uint)((int)*(undefined8 *)piVar4 == param_2);
                auVar8._12_4_ = -(uint)((int)((ulong)*(undefined8 *)piVar4 >> 0x20) == param_2);
                auVar26 = auVar26 ^ (auVar26 ^ auVar6) & auVar8;
                auVar7[3] = cVar31;
                auVar7._0_3_ = (int3)sVar2;
                auVar7[4] = uVar32;
                auVar7[5] = uVar33;
                auVar7[6] = cVar31;
                auVar7[7] = cVar31;
                auVar7[8] = uVar32;
                auVar7[9] = uVar33;
                auVar7[10] = cVar31;
                auVar7[0xb] = cVar31;
                auVar7[0xc] = uVar32;
                auVar7[0xd] = uVar33;
                auVar7[0xe] = cVar31;
                auVar7[0xf] = cVar31;
                auVar10._4_4_ = -(uint)((int)((ulong)uVar11 >> 0x20) == param_2);
                auVar10._0_4_ = -(uint)((int)uVar11 == param_2);
                auVar10._8_4_ = -(uint)((int)*(undefined8 *)piVar5 == param_2);
                auVar10._12_4_ = -(uint)((int)((ulong)*(undefined8 *)piVar5 >> 0x20) == param_2);
                auVar34 = auVar34 ^ (auVar34 ^ auVar7) & auVar10;
              } while (uVar21 != 0);
              auVar9._4_4_ = -(uint)(auVar26._4_4_ == iVar16);
              auVar9._0_4_ = -(uint)(auVar26._0_4_ == iVar16);
              auVar9._8_4_ = -(uint)(auVar26._8_4_ == iVar16);
              auVar9._12_4_ = -(uint)(auVar26._12_4_ == iVar16);
              auVar26 = auVar26 ^ (auVar26 ^ auVar34) & auVar9;
              iVar28 = -(uint)(auVar26._4_4_ == iVar16);
              iVar29 = -(uint)(auVar26._8_4_ == iVar16);
              iVar30 = -(uint)(auVar26._12_4_ == iVar16);
              uVar24 = (uint)(byte)((byte)uVar12 & ~-(auVar26._0_4_ == iVar16));
              auVar25._0_8_ =
                   CONCAT17((byte)((ulong)uVar12 >> 0x38) & ~(byte)((uint)iVar28 >> 0x18),
                            (uint7)CONCAT14((byte)((ulong)uVar12 >> 0x20) & ~(byte)iVar28,uVar24));
              auVar25[8] = (byte)uVar13 & ~(byte)iVar29;
              auVar25[9] = (byte)((ulong)uVar13 >> 8) & ~(byte)((uint)iVar29 >> 8);
              auVar25[10] = (byte)((ulong)uVar13 >> 0x10) & ~(byte)((uint)iVar29 >> 0x10);
              auVar25[0xb] = (byte)((ulong)uVar13 >> 0x18) & ~(byte)((uint)iVar29 >> 0x18);
              auVar27[0xc] = (byte)((ulong)uVar13 >> 0x20) & ~(byte)iVar30;
              auVar27._0_12_ = auVar25;
              auVar27[0xd] = (byte)((ulong)uVar13 >> 0x28) & ~(byte)((uint)iVar30 >> 8);
              auVar27[0xe] = (byte)((ulong)uVar13 >> 0x30) & ~(byte)((uint)iVar30 >> 0x10);
              auVar27[0xf] = (byte)((ulong)uVar13 >> 0x38) & ~(byte)((uint)iVar30 >> 0x18);
              if ((uVar24 + (int)((ulong)auVar25._0_8_ >> 0x20) + auVar25._8_4_ + auVar27._12_4_ &
                  0xf) != 0) {
                iVar16 = (int)sVar2;
              }
              piVar18 = __dest + uVar20;
              if (uVar17 == uVar20) goto LAB_00acf11c;
            }
            iVar28 = iVar16;
            do {
              piVar19 = piVar18 + 1;
              iVar16 = (int)sVar2;
              if (*piVar18 != param_2) {
                iVar16 = iVar28;
              }
              piVar18 = piVar19;
              iVar28 = iVar16;
            } while (piVar19 != (int *)((long)__dest + __n));
          }
LAB_00acf11c:
          _ZdlPv(__dest);
        }
        plVar14 = (long *)plVar22[1];
        plVar23 = plVar22;
        if ((long *)plVar22[1] == (long *)0x0) {
          do {
            plVar22 = (long *)plVar23[2];
            bVar15 = (long *)*plVar22 != plVar23;
            plVar23 = plVar22;
          } while (bVar15);
        }
        else {
          do {
            plVar22 = plVar14;
            plVar14 = (long *)*plVar22;
          } while ((long *)*plVar22 != (long *)0x0);
        }
      } while (plVar22 != (long *)(param_1 + 0x33c8));
    }
    if ((999999999 < param_2) && (iVar16 == -1)) {
      iVar16 = FUN_00aea9c8(param_1,param_2);
    }
    if (iVar16 != -1) {
      for (plVar22 = *(long **)(param_1 + 0x33b0); plVar22 != (long *)0x0;
          plVar22 = (long *)*plVar22) {
        while( true ) {
          if ((short)iVar16 < *(short *)((long)plVar22 + 0x1a)) break;
          if ((short)iVar16 <= *(short *)((long)plVar22 + 0x1a)) {
            uVar17 = (ulong)*(uint3 *)((long)plVar22 + 0x44);
            goto LAB_00acf204;
          }
          plVar22 = (long *)plVar22[1];
          if (plVar22 == (long *)0x0) goto LAB_00acf1c0;
        }
      }
LAB_00acf1c0:
      if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
        FUN_004428f0("map::at:  key not found");
      }
      goto LAB_00acf284;
    }
    uVar17 = 0;
  }
LAB_00acf204:
  if (*(long *)(lVar3 + 0x28) == local_68) {
    return uVar17;
  }
LAB_00acf284:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acefbc"></a> `00acefbc` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00acefc0"></a> `00acefc0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acefc4"></a> `00acefc4` | `fc 6f 07 a9` | stp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acefc8"></a> `00acefc8` | `fa 67 08 a9` | stp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acefcc"></a> `00acefcc` | `f8 5f 09 a9` | stp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acefd0"></a> `00acefd0` | `f6 57 0a a9` | stp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acefd4"></a> `00acefd4` | `f4 4f 0b a9` | stp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acefd8"></a> `00acefd8` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00acefdc"></a> `00acefdc` | `53 d0 3b d5` | mrs x19,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acefe0"></a> `00acefe0` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-00acefe4"></a> `00acefe4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00acefe8"></a> `00acefe8` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00acefec"></a> `00acefec` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aceff0"></a> `00aceff0` | `9a fe ff 97` | bl 0x00acea58 | `UNCONDITIONAL_CALL`
<a id="insn-00aceff4"></a> `00aceff4` | `00 0b 00 36` | tbz w0,#0x0,0x00acf154 | `CONDITIONAL_JUMP`
<a id="insn-00aceff8"></a> `00aceff8` | `9c e2 59 f9` | ldr x28,[x20, #0x33c0] | `FALL_THROUGH`
<a id="insn-00aceffc"></a> `00aceffc` | `08 79 86 52` | mov w8,#0x33c8 | `FALL_THROUGH`
<a id="insn-00acf000"></a> `00acf000` | `f4 4f 00 a9` | stp x20,x19,[sp] | `FALL_THROUGH`
<a id="insn-00acf004"></a> `00acf004` | `9a 02 08 8b` | add x26,x20,x8 | `FALL_THROUGH`
<a id="insn-00acf008"></a> `00acf008` | `9f 03 1a eb` | cmp x28,x26 | `FALL_THROUGH`
<a id="insn-00acf00c"></a> `00acf00c` | `80 0a 00 54` | b.eq 0x00acf15c | `CONDITIONAL_JUMP`
<a id="insn-00acf010"></a> `00acf010` | `a0 0e 04 4e` | dup v0.4S,w21 | `FALL_THROUGH`
<a id="insn-00acf014"></a> `00acf014` | `88 bf ff f0` | adrp x8,0x2c2000 | `FALL_THROUGH`
<a id="insn-00acf018"></a> `00acf018` | `bb a3 00 d1` | sub x27,x29,#0x28 | `FALL_THROUGH`
<a id="insn-00acf01c"></a> `00acf01c` | `01 49 c2 3d` | ldr q1,[x8, #0x920] | `FALL_THROUGH`
<a id="insn-00acf020"></a> `00acf020` | `14 00 80 12` | mov w20,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acf024"></a> `00acf024` | `e1 83 00 ad` | stp q1,q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acf028"></a> `00acf028` | `04 00 00 14` | b 0x00acf038 | `UNCONDITIONAL_JUMP`
<a id="insn-00acf02c"></a> `00acf02c` | `1f 01 1a eb` | cmp x8,x26 | `FALL_THROUGH`
<a id="insn-00acf030"></a> `00acf030` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-00acf034"></a> `00acf034` | `60 09 00 54` | b.eq 0x00acf160 | `CONDITIONAL_JUMP`
<a id="insn-00acf038"></a> `00acf038` | `98 cf 42 a9` | ldp x24,x19,[x28, #0x28] | `FALL_THROUGH`
<a id="insn-00acf03c"></a> `00acf03c` | `99 43 c0 79` | ldrsh w25,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00acf040"></a> `00acf040` | `7f 7f 01 a9` | stp xzr,xzr,[x27, #0x10] | `FALL_THROUGH`
<a id="insn-00acf044"></a> `00acf044` | `b9 83 1d 78` | sturh w25,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00acf048"></a> `00acf048` | `77 02 18 eb` | subs x23,x19,x24 | `FALL_THROUGH`
<a id="insn-00acf04c"></a> `00acf04c` | `7f 83 00 f8` | stur xzr,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00acf050"></a> `00acf050` | `a0 06 00 54` | b.eq 0x00acf124 | `CONDITIONAL_JUMP`
<a id="insn-00acf054"></a> `00acf054` | `17 0f f8 b7` | tbnz x23,#0x3f,0x00acf234 | `CONDITIONAL_JUMP`
<a id="insn-00acf058"></a> `00acf058` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00acf05c"></a> `00acf05c` | `8d 22 06 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00acf060"></a> `00acf060` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00acf064"></a> `00acf064` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00acf068"></a> `00acf068` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00acf06c"></a> `00acf06c` | `e5 22 06 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-00acf070"></a> `00acf070` | `68 02 18 eb` | subs x8,x19,x24 | `FALL_THROUGH`
<a id="insn-00acf074"></a> `00acf074` | `40 05 00 54` | b.eq 0x00acf11c | `CONDITIONAL_JUMP`
<a id="insn-00acf078"></a> `00acf078` | `08 11 00 d1` | sub x8,x8,#0x4 | `FALL_THROUGH`
<a id="insn-00acf07c"></a> `00acf07c` | `1f 71 00 f1` | cmp x8,#0x1c | `FALL_THROUGH`
<a id="insn-00acf080"></a> `00acf080` | `62 00 00 54` | b.cs 0x00acf08c | `CONDITIONAL_JUMP`
<a id="insn-00acf084"></a> `00acf084` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00acf088"></a> `00acf088` | `1f 00 00 14` | b 0x00acf104 | `UNCONDITIONAL_JUMP`
<a id="insn-00acf08c"></a> `00acf08c` | `08 fd 42 d3` | lsr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00acf090"></a> `00acf090` | `80 0e 04 4e` | dup v0.4S,w20 | `FALL_THROUGH`
<a id="insn-00acf094"></a> `00acf094` | `21 0f 04 4e` | dup v1.4S,w25 | `FALL_THROUGH`
<a id="insn-00acf098"></a> `00acf098` | `e5 0b c0 3d` | ldr q5,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acf09c"></a> `00acf09c` | `cb 42 00 91` | add x11,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00acf0a0"></a> `00acf0a0` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00acf0a4"></a> `00acf0a4` | `2a ed 7d 92` | and x10,x9,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00acf0a8"></a> `00acf0a8` | `02 1c a0 4e` | mov v2.16B,v0.16B | `FALL_THROUGH`
<a id="insn-00acf0ac"></a> `00acf0ac` | `c8 0a 0a 8b` | add x8,x22,x10, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00acf0b0"></a> `00acf0b0` | `ec 03 0a aa` | mov x12,x10 | `FALL_THROUGH`
<a id="insn-00acf0b4"></a> `00acf0b4` | `63 91 7f ad` | ldp q3,q4,[x11, #-0x10] | `FALL_THROUGH`
<a id="insn-00acf0b8"></a> `00acf0b8` | `8c 21 00 f1` | subs x12,x12,#0x8 | `FALL_THROUGH`
<a id="insn-00acf0bc"></a> `00acf0bc` | `6b 81 00 91` | add x11,x11,#0x20 | `FALL_THROUGH`
<a id="insn-00acf0c0"></a> `00acf0c0` | `63 8c a5 6e` | cmeq v3.4S,v3.4S,v5.4S | `FALL_THROUGH`
<a id="insn-00acf0c4"></a> `00acf0c4` | `84 8c a5 6e` | cmeq v4.4S,v4.4S,v5.4S | `FALL_THROUGH`
<a id="insn-00acf0c8"></a> `00acf0c8` | `20 1c a3 6e` | bit v0.16B,v1.16B,v3.16B | `FALL_THROUGH`
<a id="insn-00acf0cc"></a> `00acf0cc` | `22 1c a4 6e` | bit v2.16B,v1.16B,v4.16B | `FALL_THROUGH`
<a id="insn-00acf0d0"></a> `00acf0d0` | `21 ff ff 54` | b.ne 0x00acf0b4 | `CONDITIONAL_JUMP`
<a id="insn-00acf0d4"></a> `00acf0d4` | `81 0e 04 4e` | dup v1.4S,w20 | `FALL_THROUGH`
<a id="insn-00acf0d8"></a> `00acf0d8` | `03 8c a1 6e` | cmeq v3.4S,v0.4S,v1.4S | `FALL_THROUGH`
<a id="insn-00acf0dc"></a> `00acf0dc` | `40 1c a3 6e` | bit v0.16B,v2.16B,v3.16B | `FALL_THROUGH`
<a id="insn-00acf0e0"></a> `00acf0e0` | `00 8c a1 6e` | cmeq v0.4S,v0.4S,v1.4S | `FALL_THROUGH`
<a id="insn-00acf0e4"></a> `00acf0e4` | `e1 07 c0 3d` | ldr q1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acf0e8"></a> `00acf0e8` | `20 1c 60 4e` | bic v0.16B,v1.16B,v0.16B | `FALL_THROUGH`
<a id="insn-00acf0ec"></a> `00acf0ec` | `00 b8 b1 4e` | addv s0,v0.4S | `FALL_THROUGH`
<a id="insn-00acf0f0"></a> `00acf0f0` | `0b 00 26 1e` | fmov w11,s0 | `FALL_THROUGH`
<a id="insn-00acf0f4"></a> `00acf0f4` | `7f 0d 00 72` | tst w11,#0xf | `FALL_THROUGH`
<a id="insn-00acf0f8"></a> `00acf0f8` | `94 02 99 1a` | csel w20,w20,w25,eq | `FALL_THROUGH`
<a id="insn-00acf0fc"></a> `00acf0fc` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00acf100"></a> `00acf100` | `e0 00 00 54` | b.eq 0x00acf11c | `CONDITIONAL_JUMP`
<a id="insn-00acf104"></a> `00acf104` | `c9 02 17 8b` | add x9,x22,x23 | `FALL_THROUGH`
<a id="insn-00acf108"></a> `00acf108` | `0a 45 40 b8` | ldr w10,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00acf10c"></a> `00acf10c` | `5f 01 15 6b` | cmp w10,w21 | `FALL_THROUGH`
<a id="insn-00acf110"></a> `00acf110` | `34 03 94 1a` | csel w20,w25,w20,eq | `FALL_THROUGH`
<a id="insn-00acf114"></a> `00acf114` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acf118"></a> `00acf118` | `81 ff ff 54` | b.ne 0x00acf108 | `CONDITIONAL_JUMP`
<a id="insn-00acf11c"></a> `00acf11c` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00acf120"></a> `00acf120` | `64 22 06 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00acf124"></a> `00acf124` | `89 07 40 f9` | ldr x9,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-00acf128"></a> `00acf128` | `a9 00 00 b4` | cbz x9,0x00acf13c | `CONDITIONAL_JUMP`
<a id="insn-00acf12c"></a> `00acf12c` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00acf130"></a> `00acf130` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00acf134"></a> `00acf134` | `c9 ff ff b5` | cbnz x9,0x00acf12c | `CONDITIONAL_JUMP`
<a id="insn-00acf138"></a> `00acf138` | `bd ff ff 17` | b 0x00acf02c | `UNCONDITIONAL_JUMP`
<a id="insn-00acf13c"></a> `00acf13c` | `88 0b 40 f9` | ldr x8,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-00acf140"></a> `00acf140` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00acf144"></a> `00acf144` | `3f 01 1c eb` | cmp x9,x28 | `FALL_THROUGH`
<a id="insn-00acf148"></a> `00acf148` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-00acf14c"></a> `00acf14c` | `81 ff ff 54` | b.ne 0x00acf13c | `CONDITIONAL_JUMP`
<a id="insn-00acf150"></a> `00acf150` | `b7 ff ff 17` | b 0x00acf02c | `UNCONDITIONAL_JUMP`
<a id="insn-00acf154"></a> `00acf154` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acf158"></a> `00acf158` | `2b 00 00 14` | b 0x00acf204 | `UNCONDITIONAL_JUMP`
<a id="insn-00acf15c"></a> `00acf15c` | `14 00 80 12` | mov w20,#0xffffffff | `FALL_THROUGH`
<a id="insn-00acf160"></a> `00acf160` | `08 40 99 52` | mov w8,#0xca00 | `FALL_THROUGH`
<a id="insn-00acf164"></a> `00acf164` | `48 73 a7 72` | movk w8,#0x3b9a, LSL #16 | `FALL_THROUGH`
<a id="insn-00acf168"></a> `00acf168` | `bf 02 08 6b` | cmp w21,w8 | `FALL_THROUGH`
<a id="insn-00acf16c"></a> `00acf16c` | `2b 04 00 54` | b.lt 0x00acf1f0 | `CONDITIONAL_JUMP`
<a id="insn-00acf170"></a> `00acf170` | `f3 03 40 f9` | ldr x19,[sp] | `FALL_THROUGH`
<a id="insn-00acf174"></a> `00acf174` | `9f 06 00 31` | cmn w20,#0x1 | `FALL_THROUGH`
<a id="insn-00acf178"></a> `00acf178` | `a1 00 00 54` | b.ne 0x00acf18c | `CONDITIONAL_JUMP`
<a id="insn-00acf17c"></a> `00acf17c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acf180"></a> `00acf180` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-00acf184"></a> `00acf184` | `11 6e 00 94` | bl 0x00aea9c8 | `UNCONDITIONAL_CALL`
<a id="insn-00acf188"></a> `00acf188` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00acf18c"></a> `00acf18c` | `9f 06 00 31` | cmn w20,#0x1 | `FALL_THROUGH`
<a id="insn-00acf190"></a> `00acf190` | `60 03 00 54` | b.eq 0x00acf1fc | `CONDITIONAL_JUMP`
<a id="insn-00acf194"></a> `00acf194` | `68 da 59 f9` | ldr x8,[x19, #0x33b0] | `FALL_THROUGH`
<a id="insn-00acf198"></a> `00acf198` | `88 00 00 b5` | cbnz x8,0x00acf1a8 | `CONDITIONAL_JUMP`
<a id="insn-00acf19c"></a> `00acf19c` | `09 00 00 14` | b 0x00acf1c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00acf1a0"></a> `00acf1a0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00acf1a4"></a> `00acf1a4` | `e8 00 00 b4` | cbz x8,0x00acf1c0 | `CONDITIONAL_JUMP`
<a id="insn-00acf1a8"></a> `00acf1a8` | `09 35 c0 79` | ldrsh w9,[x8, #0x1a] | `FALL_THROUGH`
<a id="insn-00acf1ac"></a> `00acf1ac` | `3f a1 34 6b` | cmp w9,w20, SXTH  | `FALL_THROUGH`
<a id="insn-00acf1b0"></a> `00acf1b0` | `8c ff ff 54` | b.gt 0x00acf1a0 | `CONDITIONAL_JUMP`
<a id="insn-00acf1b4"></a> `00acf1b4` | `6a 01 00 54` | b.ge 0x00acf1e0 | `CONDITIONAL_JUMP`
<a id="insn-00acf1b8"></a> `00acf1b8` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00acf1bc"></a> `00acf1bc` | `68 ff ff b5` | cbnz x8,0x00acf1a8 | `CONDITIONAL_JUMP`
<a id="insn-00acf1c0"></a> `00acf1c0` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acf1c4"></a> `00acf1c4` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00acf1c8"></a> `00acf1c8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acf1cc"></a> `00acf1cc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acf1d0"></a> `00acf1d0` | `a1 05 00 54` | b.ne 0x00acf284 | `CONDITIONAL_JUMP`
<a id="insn-00acf1d4"></a> `00acf1d4` | `80 be ff b0` | adrp x0,0x2a0000 | `FALL_THROUGH`
<a id="insn-00acf1d8"></a> `00acf1d8` | `00 c0 03 91` | add x0,x0,#0xf0 | `FALL_THROUGH`
<a id="insn-00acf1dc"></a> `00acf1dc` | `c5 cd e5 97` | bl 0x004428f0 | `CALL_TERMINATOR`
<a id="insn-00acf1e0"></a> `00acf1e0` | `09 19 41 39` | ldrb w9,[x8, #0x46] | `FALL_THROUGH`
<a id="insn-00acf1e4"></a> `00acf1e4` | `08 89 40 79` | ldrh w8,[x8, #0x44] | `FALL_THROUGH`
<a id="insn-00acf1e8"></a> `00acf1e8` | `00 41 09 2a` | orr w0,w8,w9, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00acf1ec"></a> `00acf1ec` | `05 00 00 14` | b 0x00acf200 | `UNCONDITIONAL_JUMP`
<a id="insn-00acf1f0"></a> `00acf1f0` | `f3 03 40 f9` | ldr x19,[sp] | `FALL_THROUGH`
<a id="insn-00acf1f4"></a> `00acf1f4` | `9f 06 00 31` | cmn w20,#0x1 | `FALL_THROUGH`
<a id="insn-00acf1f8"></a> `00acf1f8` | `e1 fc ff 54` | b.ne 0x00acf194 | `CONDITIONAL_JUMP`
<a id="insn-00acf1fc"></a> `00acf1fc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00acf200"></a> `00acf200` | `f3 07 40 f9` | ldr x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acf204"></a> `00acf204` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00acf208"></a> `00acf208` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acf20c"></a> `00acf20c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acf210"></a> `00acf210` | `a1 03 00 54` | b.ne 0x00acf284 | `CONDITIONAL_JUMP`
<a id="insn-00acf214"></a> `00acf214` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00acf218"></a> `00acf218` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00acf21c"></a> `00acf21c` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00acf220"></a> `00acf220` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acf224"></a> `00acf224` | `fc 6f 47 a9` | ldp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acf228"></a> `00acf228` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acf22c"></a> `00acf22c` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00acf230"></a> `00acf230` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acf234"></a> `00acf234` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acf238"></a> `00acf238` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00acf23c"></a> `00acf23c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acf240"></a> `00acf240` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acf244"></a> `00acf244` | `01 02 00 54` | b.ne 0x00acf284 | `CONDITIONAL_JUMP`
<a id="insn-00acf248"></a> `00acf248` | `60 23 00 91` | add x0,x27,#0x8 | `FALL_THROUGH`
<a id="insn-00acf24c"></a> `00acf24c` | `6d 85 e6 97` | bl 0x00470800 | `CALL_TERMINATOR`
<a id="insn-00acf284"></a> `00acf284` | `17 22 06 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acefbc`](#insn-00acefbc) 範囲 `[['00acefbc', '00aceff7']]`
  - `CONDITIONAL_JUMP` [`00aceff4`](#insn-00aceff4) → [`00acf154`](#insn-00acf154)
  - `FALL_THROUGH` [`00aceff4`](#insn-00aceff4) → [`00aceff8`](#insn-00aceff8)
- ブロック [`00aceff8`](#insn-00aceff8) 範囲 `[['00aceff8', '00acf00f']]`
  - `CONDITIONAL_JUMP` [`00acf00c`](#insn-00acf00c) → [`00acf15c`](#insn-00acf15c)
  - `FALL_THROUGH` [`00acf00c`](#insn-00acf00c) → [`00acf010`](#insn-00acf010)
- ブロック [`00acf010`](#insn-00acf010) 範囲 `[['00acf010', '00acf02b']]`
  - `UNCONDITIONAL_JUMP` [`00acf028`](#insn-00acf028) → [`00acf038`](#insn-00acf038)
- ブロック [`00acf02c`](#insn-00acf02c) 範囲 `[['00acf02c', '00acf037']]`
  - `CONDITIONAL_JUMP` [`00acf034`](#insn-00acf034) → [`00acf160`](#insn-00acf160)
  - `FALL_THROUGH` [`00acf034`](#insn-00acf034) → [`00acf038`](#insn-00acf038)
- ブロック [`00acf038`](#insn-00acf038) 範囲 `[['00acf038', '00acf053']]`
  - `CONDITIONAL_JUMP` [`00acf050`](#insn-00acf050) → [`00acf124`](#insn-00acf124)
  - `FALL_THROUGH` [`00acf050`](#insn-00acf050) → [`00acf054`](#insn-00acf054)
- ブロック [`00acf054`](#insn-00acf054) 範囲 `[['00acf054', '00acf057']]`
  - `CONDITIONAL_JUMP` [`00acf054`](#insn-00acf054) → [`00acf234`](#insn-00acf234)
  - `FALL_THROUGH` [`00acf054`](#insn-00acf054) → [`00acf058`](#insn-00acf058)
- ブロック [`00acf058`](#insn-00acf058) 範囲 `[['00acf058', '00acf077']]`
  - `CONDITIONAL_JUMP` [`00acf074`](#insn-00acf074) → [`00acf11c`](#insn-00acf11c)
  - `FALL_THROUGH` [`00acf074`](#insn-00acf074) → [`00acf078`](#insn-00acf078)
- ブロック [`00acf078`](#insn-00acf078) 範囲 `[['00acf078', '00acf083']]`
  - `CONDITIONAL_JUMP` [`00acf080`](#insn-00acf080) → [`00acf08c`](#insn-00acf08c)
  - `FALL_THROUGH` [`00acf080`](#insn-00acf080) → [`00acf084`](#insn-00acf084)
- ブロック [`00acf084`](#insn-00acf084) 範囲 `[['00acf084', '00acf08b']]`
  - `UNCONDITIONAL_JUMP` [`00acf088`](#insn-00acf088) → [`00acf104`](#insn-00acf104)
- ブロック [`00acf08c`](#insn-00acf08c) 範囲 `[['00acf08c', '00acf0b3']]`
  - `FALL_THROUGH` [`00acf0b0`](#insn-00acf0b0) → [`00acf0b4`](#insn-00acf0b4)
- ブロック [`00acf0b4`](#insn-00acf0b4) 範囲 `[['00acf0b4', '00acf0d3']]`
  - `CONDITIONAL_JUMP` [`00acf0d0`](#insn-00acf0d0) → [`00acf0b4`](#insn-00acf0b4)
  - `FALL_THROUGH` [`00acf0d0`](#insn-00acf0d0) → [`00acf0d4`](#insn-00acf0d4)
- ブロック [`00acf0d4`](#insn-00acf0d4) 範囲 `[['00acf0d4', '00acf103']]`
  - `CONDITIONAL_JUMP` [`00acf100`](#insn-00acf100) → [`00acf11c`](#insn-00acf11c)
  - `FALL_THROUGH` [`00acf100`](#insn-00acf100) → [`00acf104`](#insn-00acf104)
- ブロック [`00acf104`](#insn-00acf104) 範囲 `[['00acf104', '00acf107']]`
  - `FALL_THROUGH` [`00acf104`](#insn-00acf104) → [`00acf108`](#insn-00acf108)
- ブロック [`00acf108`](#insn-00acf108) 範囲 `[['00acf108', '00acf11b']]`
  - `CONDITIONAL_JUMP` [`00acf118`](#insn-00acf118) → [`00acf108`](#insn-00acf108)
  - `FALL_THROUGH` [`00acf118`](#insn-00acf118) → [`00acf11c`](#insn-00acf11c)
- ブロック [`00acf11c`](#insn-00acf11c) 範囲 `[['00acf11c', '00acf123']]`
  - `FALL_THROUGH` [`00acf120`](#insn-00acf120) → [`00acf124`](#insn-00acf124)
- ブロック [`00acf124`](#insn-00acf124) 範囲 `[['00acf124', '00acf12b']]`
  - `CONDITIONAL_JUMP` [`00acf128`](#insn-00acf128) → [`00acf13c`](#insn-00acf13c)
  - `FALL_THROUGH` [`00acf128`](#insn-00acf128) → [`00acf12c`](#insn-00acf12c)
- ブロック [`00acf12c`](#insn-00acf12c) 範囲 `[['00acf12c', '00acf137']]`
  - `CONDITIONAL_JUMP` [`00acf134`](#insn-00acf134) → [`00acf12c`](#insn-00acf12c)
  - `FALL_THROUGH` [`00acf134`](#insn-00acf134) → [`00acf138`](#insn-00acf138)
- ブロック [`00acf138`](#insn-00acf138) 範囲 `[['00acf138', '00acf13b']]`
  - `UNCONDITIONAL_JUMP` [`00acf138`](#insn-00acf138) → [`00acf02c`](#insn-00acf02c)
- ブロック [`00acf13c`](#insn-00acf13c) 範囲 `[['00acf13c', '00acf14f']]`
  - `CONDITIONAL_JUMP` [`00acf14c`](#insn-00acf14c) → [`00acf13c`](#insn-00acf13c)
  - `FALL_THROUGH` [`00acf14c`](#insn-00acf14c) → [`00acf150`](#insn-00acf150)
- ブロック [`00acf150`](#insn-00acf150) 範囲 `[['00acf150', '00acf153']]`
  - `UNCONDITIONAL_JUMP` [`00acf150`](#insn-00acf150) → [`00acf02c`](#insn-00acf02c)
- ブロック [`00acf154`](#insn-00acf154) 範囲 `[['00acf154', '00acf15b']]`
  - `UNCONDITIONAL_JUMP` [`00acf158`](#insn-00acf158) → [`00acf204`](#insn-00acf204)
- ブロック [`00acf15c`](#insn-00acf15c) 範囲 `[['00acf15c', '00acf15f']]`
  - `FALL_THROUGH` [`00acf15c`](#insn-00acf15c) → [`00acf160`](#insn-00acf160)
- ブロック [`00acf160`](#insn-00acf160) 範囲 `[['00acf160', '00acf16f']]`
  - `CONDITIONAL_JUMP` [`00acf16c`](#insn-00acf16c) → [`00acf1f0`](#insn-00acf1f0)
  - `FALL_THROUGH` [`00acf16c`](#insn-00acf16c) → [`00acf170`](#insn-00acf170)
- ブロック [`00acf170`](#insn-00acf170) 範囲 `[['00acf170', '00acf17b']]`
  - `CONDITIONAL_JUMP` [`00acf178`](#insn-00acf178) → [`00acf18c`](#insn-00acf18c)
  - `FALL_THROUGH` [`00acf178`](#insn-00acf178) → [`00acf17c`](#insn-00acf17c)
- ブロック [`00acf17c`](#insn-00acf17c) 範囲 `[['00acf17c', '00acf18b']]`
  - `FALL_THROUGH` [`00acf188`](#insn-00acf188) → [`00acf18c`](#insn-00acf18c)
- ブロック [`00acf18c`](#insn-00acf18c) 範囲 `[['00acf18c', '00acf193']]`
  - `CONDITIONAL_JUMP` [`00acf190`](#insn-00acf190) → [`00acf1fc`](#insn-00acf1fc)
  - `FALL_THROUGH` [`00acf190`](#insn-00acf190) → [`00acf194`](#insn-00acf194)
- ブロック [`00acf194`](#insn-00acf194) 範囲 `[['00acf194', '00acf19b']]`
  - `CONDITIONAL_JUMP` [`00acf198`](#insn-00acf198) → [`00acf1a8`](#insn-00acf1a8)
  - `FALL_THROUGH` [`00acf198`](#insn-00acf198) → [`00acf19c`](#insn-00acf19c)
- ブロック [`00acf19c`](#insn-00acf19c) 範囲 `[['00acf19c', '00acf19f']]`
  - `UNCONDITIONAL_JUMP` [`00acf19c`](#insn-00acf19c) → [`00acf1c0`](#insn-00acf1c0)
- ブロック [`00acf1a0`](#insn-00acf1a0) 範囲 `[['00acf1a0', '00acf1a7']]`
  - `CONDITIONAL_JUMP` [`00acf1a4`](#insn-00acf1a4) → [`00acf1c0`](#insn-00acf1c0)
  - `FALL_THROUGH` [`00acf1a4`](#insn-00acf1a4) → [`00acf1a8`](#insn-00acf1a8)
- ブロック [`00acf1a8`](#insn-00acf1a8) 範囲 `[['00acf1a8', '00acf1b3']]`
  - `CONDITIONAL_JUMP` [`00acf1b0`](#insn-00acf1b0) → [`00acf1a0`](#insn-00acf1a0)
  - `FALL_THROUGH` [`00acf1b0`](#insn-00acf1b0) → [`00acf1b4`](#insn-00acf1b4)
- ブロック [`00acf1b4`](#insn-00acf1b4) 範囲 `[['00acf1b4', '00acf1b7']]`
  - `CONDITIONAL_JUMP` [`00acf1b4`](#insn-00acf1b4) → [`00acf1e0`](#insn-00acf1e0)
  - `FALL_THROUGH` [`00acf1b4`](#insn-00acf1b4) → [`00acf1b8`](#insn-00acf1b8)
- ブロック [`00acf1b8`](#insn-00acf1b8) 範囲 `[['00acf1b8', '00acf1bf']]`
  - `CONDITIONAL_JUMP` [`00acf1bc`](#insn-00acf1bc) → [`00acf1a8`](#insn-00acf1a8)
  - `FALL_THROUGH` [`00acf1bc`](#insn-00acf1bc) → [`00acf1c0`](#insn-00acf1c0)
- ブロック [`00acf1c0`](#insn-00acf1c0) 範囲 `[['00acf1c0', '00acf1d3']]`
  - `CONDITIONAL_JUMP` [`00acf1d0`](#insn-00acf1d0) → [`00acf284`](#insn-00acf284)
  - `FALL_THROUGH` [`00acf1d0`](#insn-00acf1d0) → [`00acf1d4`](#insn-00acf1d4)
- ブロック [`00acf1d4`](#insn-00acf1d4) 範囲 `[['00acf1d4', '00acf1df']]`
- ブロック [`00acf1e0`](#insn-00acf1e0) 範囲 `[['00acf1e0', '00acf1ef']]`
  - `UNCONDITIONAL_JUMP` [`00acf1ec`](#insn-00acf1ec) → [`00acf200`](#insn-00acf200)
- ブロック [`00acf1f0`](#insn-00acf1f0) 範囲 `[['00acf1f0', '00acf1fb']]`
  - `CONDITIONAL_JUMP` [`00acf1f8`](#insn-00acf1f8) → [`00acf194`](#insn-00acf194)
  - `FALL_THROUGH` [`00acf1f8`](#insn-00acf1f8) → [`00acf1fc`](#insn-00acf1fc)
- ブロック [`00acf1fc`](#insn-00acf1fc) 範囲 `[['00acf1fc', '00acf1ff']]`
  - `FALL_THROUGH` [`00acf1fc`](#insn-00acf1fc) → [`00acf200`](#insn-00acf200)
- ブロック [`00acf200`](#insn-00acf200) 範囲 `[['00acf200', '00acf203']]`
  - `FALL_THROUGH` [`00acf200`](#insn-00acf200) → [`00acf204`](#insn-00acf204)
- ブロック [`00acf204`](#insn-00acf204) 範囲 `[['00acf204', '00acf213']]`
  - `CONDITIONAL_JUMP` [`00acf210`](#insn-00acf210) → [`00acf284`](#insn-00acf284)
  - `FALL_THROUGH` [`00acf210`](#insn-00acf210) → [`00acf214`](#insn-00acf214)
- ブロック [`00acf214`](#insn-00acf214) 範囲 `[['00acf214', '00acf233']]`
- ブロック [`00acf234`](#insn-00acf234) 範囲 `[['00acf234', '00acf247']]`
  - `CONDITIONAL_JUMP` [`00acf244`](#insn-00acf244) → [`00acf284`](#insn-00acf284)
  - `FALL_THROUGH` [`00acf244`](#insn-00acf244) → [`00acf248`](#insn-00acf248)
- ブロック [`00acf248`](#insn-00acf248) 範囲 `[['00acf248', '00acf24f']]`
- ブロック [`00acf284`](#insn-00acf284) 範囲 `[['00acf284', '00acf287']]`

## 命令位置別の参照

- [`00acefc0`](#insn-00acefc0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acefc4`](#insn-00acefc4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acefc8`](#insn-00acefc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acefcc`](#insn-00acefcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acefd0`](#insn-00acefd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acefd4`](#insn-00acefd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acefec`](#insn-00acefec) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aceff0`](#insn-00aceff0) → [`00acea58`](00acea58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acea58` · 推定シンボル `None` · 推定型 `None`
- [`00aceff4`](#insn-00aceff4) → [`00acf154`](#insn-00acf154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf000`](#insn-00acf000) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf00c`](#insn-00acf00c) → [`00acf15c`](#insn-00acf15c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf01c`](#insn-00acf01c) → `002c2920`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf024`](#insn-00acf024) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf028`](#insn-00acf028) → [`00acf038`](#insn-00acf038) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf034`](#insn-00acf034) → [`00acf160`](#insn-00acf160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf040`](#insn-00acf040) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf044`](#insn-00acf044) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf04c`](#insn-00acf04c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf050`](#insn-00acf050) → [`00acf124`](#insn-00acf124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf054`](#insn-00acf054) → [`00acf234`](#insn-00acf234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf05c`](#insn-00acf05c) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00acf06c`](#insn-00acf06c) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`00acf074`](#insn-00acf074) → [`00acf11c`](#insn-00acf11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf080`](#insn-00acf080) → [`00acf08c`](#insn-00acf08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf088`](#insn-00acf088) → [`00acf104`](#insn-00acf104) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf098`](#insn-00acf098) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf0d0`](#insn-00acf0d0) → [`00acf0b4`](#insn-00acf0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf0e4`](#insn-00acf0e4) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf100`](#insn-00acf100) → [`00acf11c`](#insn-00acf11c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf118`](#insn-00acf118) → [`00acf108`](#insn-00acf108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf120`](#insn-00acf120) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00acf128`](#insn-00acf128) → [`00acf13c`](#insn-00acf13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf134`](#insn-00acf134) → [`00acf12c`](#insn-00acf12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf138`](#insn-00acf138) → [`00acf02c`](#insn-00acf02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf14c`](#insn-00acf14c) → [`00acf13c`](#insn-00acf13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf150`](#insn-00acf150) → [`00acf02c`](#insn-00acf02c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf158`](#insn-00acf158) → [`00acf204`](#insn-00acf204) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf16c`](#insn-00acf16c) → [`00acf1f0`](#insn-00acf1f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf170`](#insn-00acf170) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf178`](#insn-00acf178) → [`00acf18c`](#insn-00acf18c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf184`](#insn-00acf184) → [`00aea9c8`](../00aea/00aea9c8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aea9c8` · 推定シンボル `None` · 推定型 `None`
- [`00acf190`](#insn-00acf190) → [`00acf1fc`](#insn-00acf1fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf198`](#insn-00acf198) → [`00acf1a8`](#insn-00acf1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf19c`](#insn-00acf19c) → [`00acf1c0`](#insn-00acf1c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf1a4`](#insn-00acf1a4) → [`00acf1c0`](#insn-00acf1c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf1b0`](#insn-00acf1b0) → [`00acf1a0`](#insn-00acf1a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf1b4`](#insn-00acf1b4) → [`00acf1e0`](#insn-00acf1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf1bc`](#insn-00acf1bc) → [`00acf1a8`](#insn-00acf1a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf1c0`](#insn-00acf1c0) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf1c8`](#insn-00acf1c8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf1d0`](#insn-00acf1d0) → [`00acf284`](#insn-00acf284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf1d8`](#insn-00acf1d8) → `002a00f0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00acf1dc`](#insn-00acf1dc) → [`004428f0`](../00442/004428f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004428f0` · 推定シンボル `None` · 推定型 `None`
- [`00acf1ec`](#insn-00acf1ec) → [`00acf200`](#insn-00acf200) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf1f0`](#insn-00acf1f0) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf1f8`](#insn-00acf1f8) → [`00acf194`](#insn-00acf194) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf200`](#insn-00acf200) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf208`](#insn-00acf208) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf210`](#insn-00acf210) → [`00acf284`](#insn-00acf284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf214`](#insn-00acf214) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf218`](#insn-00acf218) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf21c`](#insn-00acf21c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf220`](#insn-00acf220) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf224`](#insn-00acf224) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf228`](#insn-00acf228) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf234`](#insn-00acf234) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf23c`](#insn-00acf23c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf244`](#insn-00acf244) → [`00acf284`](#insn-00acf284) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acf24c`](#insn-00acf24c) → [`00470800`](../00470/00470800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470800` · 推定シンボル `None` · 推定型 `None`
- [`00acf284`](#insn-00acf284) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acefc0`](#insn-00acefc0)

~~~json
{
  "source": "00acefc0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acefc4`](#insn-00acefc4)

~~~json
{
  "source": "00acefc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acefc8`](#insn-00acefc8)

~~~json
{
  "source": "00acefc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acefcc`](#insn-00acefcc)

~~~json
{
  "source": "00acefcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acefd0`](#insn-00acefd0)

~~~json
{
  "source": "00acefd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acefd4`](#insn-00acefd4)

~~~json
{
  "source": "00acefd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acefec`](#insn-00acefec)

~~~json
{
  "source": "00acefec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aceff0`](#insn-00aceff0)

~~~json
{
  "source": "00aceff0",
  "target": "00acea58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aceff4`](#insn-00aceff4)

~~~json
{
  "source": "00aceff4",
  "target": "00acf154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf000`](#insn-00acf000)

~~~json
{
  "source": "00acf000",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf00c`](#insn-00acf00c)

~~~json
{
  "source": "00acf00c",
  "target": "00acf15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf01c`](#insn-00acf01c)

~~~json
{
  "source": "00acf01c",
  "target": "002c2920",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf024`](#insn-00acf024)

~~~json
{
  "source": "00acf024",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf028`](#insn-00acf028)

~~~json
{
  "source": "00acf028",
  "target": "00acf038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf034`](#insn-00acf034)

~~~json
{
  "source": "00acf034",
  "target": "00acf160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf040`](#insn-00acf040)

~~~json
{
  "source": "00acf040",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf044`](#insn-00acf044)

~~~json
{
  "source": "00acf044",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf04c`](#insn-00acf04c)

~~~json
{
  "source": "00acf04c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf050`](#insn-00acf050)

~~~json
{
  "source": "00acf050",
  "target": "00acf124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf054`](#insn-00acf054)

~~~json
{
  "source": "00acf054",
  "target": "00acf234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf05c`](#insn-00acf05c)

~~~json
{
  "source": "00acf05c",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf06c`](#insn-00acf06c)

~~~json
{
  "source": "00acf06c",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf074`](#insn-00acf074)

~~~json
{
  "source": "00acf074",
  "target": "00acf11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf080`](#insn-00acf080)

~~~json
{
  "source": "00acf080",
  "target": "00acf08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf088`](#insn-00acf088)

~~~json
{
  "source": "00acf088",
  "target": "00acf104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf098`](#insn-00acf098)

~~~json
{
  "source": "00acf098",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf0d0`](#insn-00acf0d0)

~~~json
{
  "source": "00acf0d0",
  "target": "00acf0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf0e4`](#insn-00acf0e4)

~~~json
{
  "source": "00acf0e4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf100`](#insn-00acf100)

~~~json
{
  "source": "00acf100",
  "target": "00acf11c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf118`](#insn-00acf118)

~~~json
{
  "source": "00acf118",
  "target": "00acf108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf120`](#insn-00acf120)

~~~json
{
  "source": "00acf120",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf128`](#insn-00acf128)

~~~json
{
  "source": "00acf128",
  "target": "00acf13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf134`](#insn-00acf134)

~~~json
{
  "source": "00acf134",
  "target": "00acf12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf138`](#insn-00acf138)

~~~json
{
  "source": "00acf138",
  "target": "00acf02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf14c`](#insn-00acf14c)

~~~json
{
  "source": "00acf14c",
  "target": "00acf13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf150`](#insn-00acf150)

~~~json
{
  "source": "00acf150",
  "target": "00acf02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf158`](#insn-00acf158)

~~~json
{
  "source": "00acf158",
  "target": "00acf204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf16c`](#insn-00acf16c)

~~~json
{
  "source": "00acf16c",
  "target": "00acf1f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf170`](#insn-00acf170)

~~~json
{
  "source": "00acf170",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf178`](#insn-00acf178)

~~~json
{
  "source": "00acf178",
  "target": "00acf18c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf184`](#insn-00acf184)

~~~json
{
  "source": "00acf184",
  "target": "00aea9c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf190`](#insn-00acf190)

~~~json
{
  "source": "00acf190",
  "target": "00acf1fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf198`](#insn-00acf198)

~~~json
{
  "source": "00acf198",
  "target": "00acf1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf19c`](#insn-00acf19c)

~~~json
{
  "source": "00acf19c",
  "target": "00acf1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf1a4`](#insn-00acf1a4)

~~~json
{
  "source": "00acf1a4",
  "target": "00acf1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf1b0`](#insn-00acf1b0)

~~~json
{
  "source": "00acf1b0",
  "target": "00acf1a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf1b4`](#insn-00acf1b4)

~~~json
{
  "source": "00acf1b4",
  "target": "00acf1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf1bc`](#insn-00acf1bc)

~~~json
{
  "source": "00acf1bc",
  "target": "00acf1a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf1c0`](#insn-00acf1c0)

~~~json
{
  "source": "00acf1c0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf1c8`](#insn-00acf1c8)

~~~json
{
  "source": "00acf1c8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf1d0`](#insn-00acf1d0)

~~~json
{
  "source": "00acf1d0",
  "target": "00acf284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf1d8`](#insn-00acf1d8)

~~~json
{
  "source": "00acf1d8",
  "target": "002a00f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a00f0",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "6d61703a3a61743a20206b6579206e6f7420666f756e6400",
  "capture_start": "002a00f0",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00acf1dc`](#insn-00acf1dc)

~~~json
{
  "source": "00acf1dc",
  "target": "004428f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf1ec`](#insn-00acf1ec)

~~~json
{
  "source": "00acf1ec",
  "target": "00acf200",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf1f0`](#insn-00acf1f0)

~~~json
{
  "source": "00acf1f0",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf1f8`](#insn-00acf1f8)

~~~json
{
  "source": "00acf1f8",
  "target": "00acf194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf200`](#insn-00acf200)

~~~json
{
  "source": "00acf200",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf208`](#insn-00acf208)

~~~json
{
  "source": "00acf208",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf210`](#insn-00acf210)

~~~json
{
  "source": "00acf210",
  "target": "00acf284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf214`](#insn-00acf214)

~~~json
{
  "source": "00acf214",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf218`](#insn-00acf218)

~~~json
{
  "source": "00acf218",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf21c`](#insn-00acf21c)

~~~json
{
  "source": "00acf21c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf220`](#insn-00acf220)

~~~json
{
  "source": "00acf220",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf224`](#insn-00acf224)

~~~json
{
  "source": "00acf224",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf228`](#insn-00acf228)

~~~json
{
  "source": "00acf228",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf234`](#insn-00acf234)

~~~json
{
  "source": "00acf234",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf23c`](#insn-00acf23c)

~~~json
{
  "source": "00acf23c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf244`](#insn-00acf244)

~~~json
{
  "source": "00acf244",
  "target": "00acf284",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acf24c`](#insn-00acf24c)

~~~json
{
  "source": "00acf24c",
  "target": "00470800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acf284`](#insn-00acf284)

~~~json
{
  "source": "00acf284",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
