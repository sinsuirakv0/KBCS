# 00aaafe8

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aaafa4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-fb9a421efdf5205024bc3fd4c377f8a7)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b0aa78`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b0a/00b0aa78.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0053.md#compare-c35d63ee3cb625412a08984776f39d51)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaafe8",
  "name": "FUN_00aaafe8",
  "size": 1200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e40ef3e44cb31c80623460784238beae069f9147df6135d241dffa6e57a84e35",
  "source_text_sha256": "e40ef3e44cb31c80623460784238beae069f9147df6135d241dffa6e57a84e35",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaafe8",
        "00aab493"
      ],
      [
        "00aab4c8",
        "00aab4cb"
      ]
    ],
    "bytes_sha256": "998804ae60f2ab4478cc6744de7414afaac1f9679776e867dc09292860ec817f",
    "instruction_count": 300,
    "instruction_bytes": 1200,
    "body_bytes": 1200,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [005d996c](../005d9/005d996c.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0041e380](../0041e/0041e380.md)
- [007cf950](../007cf/007cf950.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [0081f580](../0081f/0081f580.md)
- [00aacb84](../00aac/00aacb84.md)
- [00aacb98](../00aac/00aacb98.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb060](../00bdb/00bdb060.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7699 bytes

~~~c

void FUN_00aaafe8(long param_1,int param_2,int param_3,int param_4)

{
  ulong uVar1;
  byte *pbVar2;
  undefined4 uVar3;
  byte bVar4;
  byte bVar5;
  byte bVar6;
  byte bVar7;
  byte bVar8;
  byte bVar9;
  byte bVar10;
  byte bVar11;
  int iVar12;
  int iVar13;
  long lVar14;
  undefined8 *puVar15;
  undefined8 uVar16;
  long lVar17;
  undefined8 *puVar18;
  void *__dest;
  undefined8 *puVar19;
  long *plVar20;
  ulong uVar21;
  undefined8 *puVar22;
  ulong uVar23;
  undefined8 *puVar24;
  void *__src;
  long lVar25;
  long lVar26;
  void *local_80;
  void *local_78;
  undefined8 local_70;
  long local_68;
  
  lVar14 = tpidr_el0;
  local_68 = *(long *)(lVar14 + 0x28);
  if (param_2 == -1) {
    param_2 = FUN_007cf950(0);
    param_3 = FUN_007cfaa0();
    param_4 = FUN_007cfcd8();
  }
  iVar12 = param_4 + param_3 * 10 + param_2 * 1000;
  puVar22 = (undefined8 *)(param_1 + 0x20);
  puVar19 = (undefined8 *)*puVar22;
  puVar18 = puVar22;
  puVar24 = puVar22;
  if ((undefined8 *)*puVar22 != (undefined8 *)0x0) {
    do {
      while (puVar15 = puVar19, puVar24 = puVar15, iVar12 < *(int *)(puVar15 + 4)) {
        puVar19 = (undefined8 *)*puVar15;
        puVar18 = puVar15;
        if ((undefined8 *)*puVar15 == (undefined8 *)0x0) goto LAB_00aab0a4;
      }
      if (iVar12 <= *(int *)(puVar15 + 4)) goto LAB_00aab0f8;
      puVar19 = (undefined8 *)puVar15[1];
    } while ((undefined8 *)puVar15[1] != (undefined8 *)0x0);
    puVar18 = puVar15 + 1;
  }
LAB_00aab0a4:
  puVar15 = (undefined8 *)_Znwm(0x40);
  puVar15[6] = 0;
  puVar15[7] = 0;
  puVar15[5] = 0;
  *puVar15 = 0;
  puVar15[1] = 0;
  puVar15[2] = puVar24;
  *puVar18 = puVar15;
  plVar20 = *(long **)(param_1 + 0x18);
  *(int *)(puVar15 + 4) = iVar12;
  puVar19 = puVar15;
  if (*plVar20 != 0) {
    *(long *)(param_1 + 0x18) = *plVar20;
    puVar19 = (undefined8 *)*puVar18;
  }
  FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar19);
  *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aab0f8:
  if ((ulong)(((long)(puVar15[6] - puVar15[5]) >> 3) * -0x5555555555555555) < 10) {
    puVar19 = (undefined8 *)*puVar22;
    puVar18 = puVar22;
    puVar24 = puVar22;
    if ((undefined8 *)*puVar22 != (undefined8 *)0x0) {
      do {
        while (puVar15 = puVar19, puVar24 = puVar15, iVar12 < *(int *)(puVar15 + 4)) {
          puVar19 = (undefined8 *)*puVar15;
          puVar18 = puVar15;
          if ((undefined8 *)*puVar15 == (undefined8 *)0x0) goto LAB_00aab190;
        }
        if (iVar12 <= *(int *)(puVar15 + 4)) goto LAB_00aab1e4;
        puVar19 = (undefined8 *)puVar15[1];
      } while ((undefined8 *)puVar15[1] != (undefined8 *)0x0);
      puVar18 = puVar15 + 1;
    }
LAB_00aab190:
    puVar15 = (undefined8 *)_Znwm(0x40);
    puVar15[6] = 0;
    puVar15[7] = 0;
    puVar15[5] = 0;
    *puVar15 = 0;
    puVar15[1] = 0;
    puVar15[2] = puVar24;
    *puVar18 = puVar15;
    plVar20 = *(long **)(param_1 + 0x18);
    *(int *)(puVar15 + 4) = iVar12;
    puVar19 = puVar15;
    if (*plVar20 != 0) {
      *(long *)(param_1 + 0x18) = *plVar20;
      puVar19 = (undefined8 *)*puVar18;
    }
    FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar19);
    *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aab1e4:
    puVar19 = (undefined8 *)puVar15[6];
    local_80 = (void *)0x0;
    local_78 = (void *)0x0;
    local_70 = 0;
    if (puVar19 < (undefined8 *)puVar15[7]) {
      *puVar19 = 0;
      puVar19[1] = 0;
      puVar19[2] = 0;
      puVar15[6] = puVar19 + 3;
    }
    else {
      uVar16 = FUN_00aacb98(puVar15 + 5,&local_80);
      puVar15[6] = uVar16;
      if (local_80 != (void *)0x0) {
        local_78 = local_80;
        _ZdlPv(local_80);
      }
    }
    lVar26 = 0;
    while( true ) {
      lVar17 = FUN_0081f580();
      pbVar2 = (byte *)(lVar17 + 0xc744 + lVar26 * 4);
      if (((uint)(*(byte *)(lVar17 + 0xc76e) ^ pbVar2[2]) << 0x10 |
           (uint)(*(byte *)(lVar17 + 0xc76f) ^ pbVar2[3]) << 0x18 |
           (uint)(*(byte *)(lVar17 + 0xc76d) ^ pbVar2[1]) << 8 |
          (uint)(*(byte *)(lVar17 + 0xc76c) ^ *pbVar2)) == 0xffffffff) break;
      lVar17 = FUN_0081f580();
      pbVar2 = (byte *)(lVar17 + 0xc744 + lVar26 * 4);
      bVar4 = *(byte *)(lVar17 + 0xc76c);
      bVar5 = *(byte *)(lVar17 + 0xc76d);
      bVar6 = *pbVar2;
      bVar7 = pbVar2[1];
      bVar8 = pbVar2[2];
      bVar9 = *(byte *)(lVar17 + 0xc76e);
      bVar10 = pbVar2[3];
      bVar11 = *(byte *)(lVar17 + 0xc76f);
      puVar19 = (undefined8 *)*puVar22;
      puVar18 = puVar22;
      while (puVar15 = puVar18, puVar24 = puVar18, puVar19 != (undefined8 *)0x0) {
        while (puVar18 = puVar19, *(int *)(puVar18 + 4) <= iVar12) {
          if (iVar12 <= *(int *)(puVar18 + 4)) goto LAB_00aab38c;
          puVar19 = (undefined8 *)puVar18[1];
          if ((undefined8 *)puVar18[1] == (undefined8 *)0x0) {
            puVar24 = puVar18 + 1;
            puVar15 = puVar18;
            goto LAB_00aab324;
          }
        }
        puVar19 = (undefined8 *)*puVar18;
      }
LAB_00aab324:
      puVar18 = (undefined8 *)_Znwm(0x40);
      puVar18[2] = puVar15;
      puVar18[6] = 0;
      puVar18[7] = 0;
      puVar18[5] = 0;
      *puVar18 = 0;
      puVar18[1] = 0;
      *puVar24 = puVar18;
      plVar20 = *(long **)(param_1 + 0x18);
      *(int *)(puVar18 + 4) = iVar12;
      puVar19 = puVar18;
      if (*plVar20 != 0) {
        *(long *)(param_1 + 0x18) = *plVar20;
        puVar19 = (undefined8 *)*puVar24;
      }
      FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar19);
      *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
LAB_00aab38c:
      lVar25 = puVar18[6];
      iVar13 = CONCAT13(bVar11 ^ bVar10,
                        CONCAT12(bVar9 ^ bVar8,CONCAT11(bVar5 ^ bVar7,bVar4 ^ bVar6))) + -2;
      lVar17 = FUN_0081f580();
      puVar19 = *(undefined8 **)(lVar25 + -0x10);
      uVar3 = *(undefined4 *)(lVar17 + (long)iVar13 * 4 + 0x49734);
      if (puVar19 < *(undefined8 **)(lVar25 + -8)) {
        puVar18 = puVar19 + 1;
        *puVar19 = CONCAT44(uVar3,iVar13);
      }
      else {
        __src = *(void **)(lVar25 + -0x18);
        lVar17 = (long)puVar19 - (long)__src >> 3;
        uVar1 = lVar17 + 1;
        if (uVar1 >> 0x3d != 0) {
          if (*(long *)(lVar14 + 0x28) == local_68) {
            FUN_00aacb84();
LAB_00aab47c:
            if (*(long *)(lVar14 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_0041e380();
            }
          }
          goto LAB_00aab4c8;
        }
        uVar21 = (long)*(undefined8 **)(lVar25 + -8) - (long)__src;
        uVar23 = (long)uVar21 >> 2;
        if (uVar23 <= uVar1) {
          uVar23 = uVar1;
        }
        if (0x7ffffffffffffff7 < uVar21) {
          uVar23 = 0x1fffffffffffffff;
        }
        if (uVar23 == 0) {
          __dest = (void *)0x0;
        }
        else {
          if (uVar23 >> 0x3d != 0) goto LAB_00aab47c;
          __dest = (void *)_Znwm(uVar23 << 3);
        }
        puVar24 = (undefined8 *)((long)__dest + lVar17 * 8);
        puVar18 = puVar24 + 1;
        *puVar24 = CONCAT44(uVar3,iVar13);
        memcpy(__dest,__src,(long)puVar19 - (long)__src);
        *(void **)(lVar25 + -0x18) = __dest;
        *(undefined8 **)(lVar25 + -0x10) = puVar18;
        *(void **)(lVar25 + -8) = (void *)((long)__dest + uVar23 * 8);
        if (__src != (void *)0x0) {
          _ZdlPv(__src);
        }
      }
      lVar26 = lVar26 + 1;
      *(undefined8 **)(lVar25 + -0x10) = puVar18;
      if (lVar26 == 10) break;
    }
  }
  if (*(long *)(lVar14 + 0x28) == local_68) {
    return;
  }
LAB_00aab4c8:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaafe8"></a> `00aaafe8` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00aaafec"></a> `00aaafec` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aaaff0"></a> `00aaaff0` | `fc 6f 06 a9` | stp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aaaff4"></a> `00aaaff4` | `fa 67 07 a9` | stp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aaaff8"></a> `00aaaff8` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aaaffc"></a> `00aaaffc` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aab000"></a> `00aab000` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aab004"></a> `00aab004` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aab008"></a> `00aab008` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aab00c"></a> `00aab00c` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00aab010"></a> `00aab010` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aab014"></a> `00aab014` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aab018"></a> `00aab018` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aab01c"></a> `00aab01c` | `3f 04 00 31` | cmn w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aab020"></a> `00aab020` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aab024"></a> `00aab024` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab028"></a> `00aab028` | `01 01 00 54` | b.ne 0x00aab048 | `CONDITIONAL_JUMP`
<a id="insn-00aab02c"></a> `00aab02c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aab030"></a> `00aab030` | `48 92 f4 97` | bl 0x007cf950 | `UNCONDITIONAL_CALL`
<a id="insn-00aab034"></a> `00aab034` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aab038"></a> `00aab038` | `9a 92 f4 97` | bl 0x007cfaa0 | `UNCONDITIONAL_CALL`
<a id="insn-00aab03c"></a> `00aab03c` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aab040"></a> `00aab040` | `26 93 f4 97` | bl 0x007cfcd8 | `UNCONDITIONAL_CALL`
<a id="insn-00aab044"></a> `00aab044` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-00aab048"></a> `00aab048` | `48 01 80 52` | mov w8,#0xa | `FALL_THROUGH`
<a id="insn-00aab04c"></a> `00aab04c` | `09 7d 80 52` | mov w9,#0x3e8 | `FALL_THROUGH`
<a id="insn-00aab050"></a> `00aab050` | `ea 03 16 aa` | mov x10,x22 | `FALL_THROUGH`
<a id="insn-00aab054"></a> `00aab054` | `a8 0e 08 1b` | madd w8,w21,w8,w3 | `FALL_THROUGH`
<a id="insn-00aab058"></a> `00aab058` | `99 22 09 1b` | madd w25,w20,w9,w8 | `FALL_THROUGH`
<a id="insn-00aab05c"></a> `00aab05c` | `48 0d 42 f8` | ldr x8,[x10, #0x20]! | `FALL_THROUGH`
<a id="insn-00aab060"></a> `00aab060` | `f3 03 0a aa` | mov x19,x10 | `FALL_THROUGH`
<a id="insn-00aab064"></a> `00aab064` | `f4 03 0a aa` | mov x20,x10 | `FALL_THROUGH`
<a id="insn-00aab068"></a> `00aab068` | `f6 2b 01 a9` | stp x22,x10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aab06c"></a> `00aab06c` | `a8 00 00 b5` | cbnz x8,0x00aab080 | `CONDITIONAL_JUMP`
<a id="insn-00aab070"></a> `00aab070` | `0d 00 00 14` | b 0x00aab0a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab074"></a> `00aab074` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab078"></a> `00aab078` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00aab07c"></a> `00aab07c` | `48 01 00 b4` | cbz x8,0x00aab0a4 | `CONDITIONAL_JUMP`
<a id="insn-00aab080"></a> `00aab080` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aab084"></a> `00aab084` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aab088"></a> `00aab088` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00aab08c"></a> `00aab08c` | `4b ff ff 54` | b.lt 0x00aab074 | `CONDITIONAL_JUMP`
<a id="insn-00aab090"></a> `00aab090` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00aab094"></a> `00aab094` | `2a 03 00 54` | b.ge 0x00aab0f8 | `CONDITIONAL_JUMP`
<a id="insn-00aab098"></a> `00aab098` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aab09c"></a> `00aab09c` | `28 ff ff b5` | cbnz x8,0x00aab080 | `CONDITIONAL_JUMP`
<a id="insn-00aab0a0"></a> `00aab0a0` | `93 22 00 91` | add x19,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aab0a4"></a> `00aab0a4` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aab0a8"></a> `00aab0a8` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-00aab0ac"></a> `00aab0ac` | `e5 bf 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00aab0b0"></a> `00aab0b0` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aab0b4"></a> `00aab0b4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aab0b8"></a> `00aab0b8` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aab0bc"></a> `00aab0bc` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aab0c0"></a> `00aab0c0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aab0c4"></a> `00aab0c4` | `15 08 00 f9` | str x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aab0c8"></a> `00aab0c8` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00aab0cc"></a> `00aab0cc` | `c8 0e 40 f9` | ldr x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aab0d0"></a> `00aab0d0` | `19 20 00 b9` | str w25,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aab0d4"></a> `00aab0d4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aab0d8"></a> `00aab0d8` | `68 00 00 b4` | cbz x8,0x00aab0e4 | `CONDITIONAL_JUMP`
<a id="insn-00aab0dc"></a> `00aab0dc` | `c8 0e 00 f9` | str x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aab0e0"></a> `00aab0e0` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00aab0e4"></a> `00aab0e4` | `c0 12 40 f9` | ldr x0,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00aab0e8"></a> `00aab0e8` | `df b7 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aab0ec"></a> `00aab0ec` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aab0f0"></a> `00aab0f0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab0f4"></a> `00aab0f4` | `c8 16 00 f9` | str x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aab0f8"></a> `00aab0f8` | `89 a2 42 a9` | ldp x9,x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aab0fc"></a> `00aab0fc` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aab100"></a> `00aab100` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00aab104"></a> `00aab104` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00aab108"></a> `00aab108` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00aab10c"></a> `00aab10c` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aab110"></a> `00aab110` | `1f 25 00 f1` | cmp x8,#0x9 | `FALL_THROUGH`
<a id="insn-00aab114"></a> `00aab114` | `c9 01 00 54` | b.ls 0x00aab14c | `CONDITIONAL_JUMP`
<a id="insn-00aab118"></a> `00aab118` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aab11c"></a> `00aab11c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aab120"></a> `00aab120` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab124"></a> `00aab124` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab128"></a> `00aab128` | `01 1d 00 54` | b.ne 0x00aab4c8 | `CONDITIONAL_JUMP`
<a id="insn-00aab12c"></a> `00aab12c` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aab130"></a> `00aab130` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aab134"></a> `00aab134` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aab138"></a> `00aab138` | `fa 67 47 a9` | ldp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aab13c"></a> `00aab13c` | `fc 6f 46 a9` | ldp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aab140"></a> `00aab140` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aab144"></a> `00aab144` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00aab148"></a> `00aab148` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aab14c"></a> `00aab14c` | `f6 53 41 a9` | ldp x22,x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aab150"></a> `00aab150` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab154"></a> `00aab154` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00aab158"></a> `00aab158` | `a8 00 00 b5` | cbnz x8,0x00aab16c | `CONDITIONAL_JUMP`
<a id="insn-00aab15c"></a> `00aab15c` | `0d 00 00 14` | b 0x00aab190 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab160"></a> `00aab160` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab164"></a> `00aab164` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00aab168"></a> `00aab168` | `48 01 00 b4` | cbz x8,0x00aab190 | `CONDITIONAL_JUMP`
<a id="insn-00aab16c"></a> `00aab16c` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aab170"></a> `00aab170` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aab174"></a> `00aab174` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00aab178"></a> `00aab178` | `4b ff ff 54` | b.lt 0x00aab160 | `CONDITIONAL_JUMP`
<a id="insn-00aab17c"></a> `00aab17c` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00aab180"></a> `00aab180` | `2a 03 00 54` | b.ge 0x00aab1e4 | `CONDITIONAL_JUMP`
<a id="insn-00aab184"></a> `00aab184` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aab188"></a> `00aab188` | `28 ff ff b5` | cbnz x8,0x00aab16c | `CONDITIONAL_JUMP`
<a id="insn-00aab18c"></a> `00aab18c` | `93 22 00 91` | add x19,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aab190"></a> `00aab190` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aab194"></a> `00aab194` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-00aab198"></a> `00aab198` | `aa bf 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00aab19c"></a> `00aab19c` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aab1a0"></a> `00aab1a0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aab1a4"></a> `00aab1a4` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aab1a8"></a> `00aab1a8` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aab1ac"></a> `00aab1ac` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aab1b0"></a> `00aab1b0` | `15 08 00 f9` | str x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aab1b4"></a> `00aab1b4` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00aab1b8"></a> `00aab1b8` | `c8 0e 40 f9` | ldr x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aab1bc"></a> `00aab1bc` | `19 20 00 b9` | str w25,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aab1c0"></a> `00aab1c0` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aab1c4"></a> `00aab1c4` | `68 00 00 b4` | cbz x8,0x00aab1d0 | `CONDITIONAL_JUMP`
<a id="insn-00aab1c8"></a> `00aab1c8` | `c8 0e 00 f9` | str x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aab1cc"></a> `00aab1cc` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00aab1d0"></a> `00aab1d0` | `c0 12 40 f9` | ldr x0,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00aab1d4"></a> `00aab1d4` | `a4 b7 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aab1d8"></a> `00aab1d8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aab1dc"></a> `00aab1dc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab1e0"></a> `00aab1e0` | `c8 16 00 f9` | str x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aab1e4"></a> `00aab1e4` | `88 26 43 a9` | ldp x8,x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab1e8"></a> `00aab1e8` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aab1ec"></a> `00aab1ec` | `bf 03 1f f8` | stur xzr,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab1f0"></a> `00aab1f0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab1f4"></a> `00aab1f4` | `e2 00 00 54` | b.cs 0x00aab210 | `CONDITIONAL_JUMP`
<a id="insn-00aab1f8"></a> `00aab1f8` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00aab1fc"></a> `00aab1fc` | `0a 61 00 91` | add x10,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00aab200"></a> `00aab200` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab204"></a> `00aab204` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aab208"></a> `00aab208` | `8a 1a 00 f9` | str x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab20c"></a> `00aab20c` | `0a 00 00 14` | b 0x00aab234 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab210"></a> `00aab210` | `80 a2 00 91` | add x0,x20,#0x28 | `FALL_THROUGH`
<a id="insn-00aab214"></a> `00aab214` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00aab218"></a> `00aab218` | `60 06 00 94` | bl 0x00aacb98 | `UNCONDITIONAL_CALL`
<a id="insn-00aab21c"></a> `00aab21c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aab220"></a> `00aab220` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aab224"></a> `00aab224` | `88 1a 00 f9` | str x8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab228"></a> `00aab228` | `60 00 00 b4` | cbz x0,0x00aab234 | `CONDITIONAL_JUMP`
<a id="insn-00aab22c"></a> `00aab22c` | `a0 83 1e f8` | stur x0,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aab230"></a> `00aab230` | `8c bf 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aab234"></a> `00aab234` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00aab238"></a> `00aab238` | `95 e8 98 52` | mov w21,#0xc744 | `FALL_THROUGH`
<a id="insn-00aab23c"></a> `00aab23c` | `08 00 00 14` | b 0x00aab25c | `UNCONDITIONAL_JUMP`
<a id="insn-00aab240"></a> `00aab240` | `68 82 1b aa` | orr x8,x19,x27, LSL #0x20 | `FALL_THROUGH`
<a id="insn-00aab244"></a> `00aab244` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00aab248"></a> `00aab248` | `5a 07 00 91` | add x26,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00aab24c"></a> `00aab24c` | `95 e8 98 52` | mov w21,#0xc744 | `FALL_THROUGH`
<a id="insn-00aab250"></a> `00aab250` | `f8 02 1f f8` | stur x24,[x23, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab254"></a> `00aab254` | `5f 2b 00 f1` | cmp x26,#0xa | `FALL_THROUGH`
<a id="insn-00aab258"></a> `00aab258` | `00 f6 ff 54` | b.eq 0x00aab118 | `CONDITIONAL_JUMP`
<a id="insn-00aab25c"></a> `00aab25c` | `c9 d0 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aab260"></a> `00aab260` | `53 f7 7e d3` | lsl x19,x26,#0x2 | `FALL_THROUGH`
<a id="insn-00aab264"></a> `00aab264` | `08 00 15 8b` | add x8,x0,x21 | `FALL_THROUGH`
<a id="insn-00aab268"></a> `00aab268` | `09 30 40 91` | add x9,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aab26c"></a> `00aab26c` | `2b b9 5d 39` | ldrb w11,[x9, #0x76e] | `FALL_THROUGH`
<a id="insn-00aab270"></a> `00aab270` | `2c bd 5d 39` | ldrb w12,[x9, #0x76f] | `FALL_THROUGH`
<a id="insn-00aab274"></a> `00aab274` | `08 01 13 8b` | add x8,x8,x19 | `FALL_THROUGH`
<a id="insn-00aab278"></a> `00aab278` | `0a 09 40 39` | ldrb w10,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aab27c"></a> `00aab27c` | `0d 05 40 39` | ldrb w13,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aab280"></a> `00aab280` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aab284"></a> `00aab284` | `0b 0d 40 39` | ldrb w11,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00aab288"></a> `00aab288` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00aab28c"></a> `00aab28c` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00aab290"></a> `00aab290` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00aab294"></a> `00aab294` | `2c b5 5d 39` | ldrb w12,[x9, #0x76d] | `FALL_THROUGH`
<a id="insn-00aab298"></a> `00aab298` | `29 b1 5d 39` | ldrb w9,[x9, #0x76c] | `FALL_THROUGH`
<a id="insn-00aab29c"></a> `00aab29c` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aab2a0"></a> `00aab2a0` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aab2a4"></a> `00aab2a4` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aab2a8"></a> `00aab2a8` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aab2ac"></a> `00aab2ac` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00aab2b0"></a> `00aab2b0` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab2b4"></a> `00aab2b4` | `20 f3 ff 54` | b.eq 0x00aab118 | `CONDITIONAL_JUMP`
<a id="insn-00aab2b8"></a> `00aab2b8` | `b2 d0 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aab2bc"></a> `00aab2bc` | `f4 0f 40 f9` | ldr x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aab2c0"></a> `00aab2c0` | `0a 00 15 8b` | add x10,x0,x21 | `FALL_THROUGH`
<a id="insn-00aab2c4"></a> `00aab2c4` | `09 30 40 91` | add x9,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aab2c8"></a> `00aab2c8` | `4a 01 13 8b` | add x10,x10,x19 | `FALL_THROUGH`
<a id="insn-00aab2cc"></a> `00aab2cc` | `38 b1 5d 39` | ldrb w24,[x9, #0x76c] | `FALL_THROUGH`
<a id="insn-00aab2d0"></a> `00aab2d0` | `33 b5 5d 39` | ldrb w19,[x9, #0x76d] | `FALL_THROUGH`
<a id="insn-00aab2d4"></a> `00aab2d4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab2d8"></a> `00aab2d8` | `50 01 40 39` | ldrb w16,[x10] | `FALL_THROUGH`
<a id="insn-00aab2dc"></a> `00aab2dc` | `51 05 40 39` | ldrb w17,[x10, #0x1] | `FALL_THROUGH`
<a id="insn-00aab2e0"></a> `00aab2e0` | `5b 09 40 39` | ldrb w27,[x10, #0x2] | `FALL_THROUGH`
<a id="insn-00aab2e4"></a> `00aab2e4` | `35 b9 5d 39` | ldrb w21,[x9, #0x76e] | `FALL_THROUGH`
<a id="insn-00aab2e8"></a> `00aab2e8` | `5c 0d 40 39` | ldrb w28,[x10, #0x3] | `FALL_THROUGH`
<a id="insn-00aab2ec"></a> `00aab2ec` | `2f bd 5d 39` | ldrb w15,[x9, #0x76f] | `FALL_THROUGH`
<a id="insn-00aab2f0"></a> `00aab2f0` | `02 00 00 14` | b 0x00aab2f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab2f4"></a> `00aab2f4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab2f8"></a> `00aab2f8` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00aab2fc"></a> `00aab2fc` | `48 01 00 b4` | cbz x8,0x00aab324 | `CONDITIONAL_JUMP`
<a id="insn-00aab300"></a> `00aab300` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aab304"></a> `00aab304` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aab308"></a> `00aab308` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00aab30c"></a> `00aab30c` | `4b ff ff 54` | b.lt 0x00aab2f4 | `CONDITIONAL_JUMP`
<a id="insn-00aab310"></a> `00aab310` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00aab314"></a> `00aab314` | `ca 03 00 54` | b.ge 0x00aab38c | `CONDITIONAL_JUMP`
<a id="insn-00aab318"></a> `00aab318` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aab31c"></a> `00aab31c` | `28 ff ff b5` | cbnz x8,0x00aab300 | `CONDITIONAL_JUMP`
<a id="insn-00aab320"></a> `00aab320` | `96 22 00 91` | add x22,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aab324"></a> `00aab324` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aab328"></a> `00aab328` | `f1 c3 04 29` | stp w17,w16,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aab32c"></a> `00aab32c` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-00aab330"></a> `00aab330` | `af c3 1d b8` | stur w15,[x29, #-0x24] | `FALL_THROUGH`
<a id="insn-00aab334"></a> `00aab334` | `43 bf 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00aab338"></a> `00aab338` | `17 08 00 f9` | str x23,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aab33c"></a> `00aab33c` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aab340"></a> `00aab340` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aab344"></a> `00aab344` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aab348"></a> `00aab348` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aab34c"></a> `00aab34c` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aab350"></a> `00aab350` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aab354"></a> `00aab354` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00aab358"></a> `00aab358` | `e8 0e 40 f9` | ldr x8,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00aab35c"></a> `00aab35c` | `19 20 00 b9` | str w25,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aab360"></a> `00aab360` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aab364"></a> `00aab364` | `68 00 00 b4` | cbz x8,0x00aab370 | `CONDITIONAL_JUMP`
<a id="insn-00aab368"></a> `00aab368` | `e8 0e 00 f9` | str x8,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00aab36c"></a> `00aab36c` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00aab370"></a> `00aab370` | `e0 12 40 f9` | ldr x0,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00aab374"></a> `00aab374` | `3c b7 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aab378"></a> `00aab378` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aab37c"></a> `00aab37c` | `af c3 5d b8` | ldur w15,[x29, #-0x24] | `FALL_THROUGH`
<a id="insn-00aab380"></a> `00aab380` | `f1 c3 44 29` | ldp w17,w16,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aab384"></a> `00aab384` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab388"></a> `00aab388` | `e8 16 00 f9` | str x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aab38c"></a> `00aab38c` | `08 03 10 4a` | eor w8,w24,w16 | `FALL_THROUGH`
<a id="insn-00aab390"></a> `00aab390` | `69 02 11 4a` | eor w9,w19,w17 | `FALL_THROUGH`
<a id="insn-00aab394"></a> `00aab394` | `97 1a 40 f9` | ldr x23,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab398"></a> `00aab398` | `08 21 09 2a` | orr w8,w8,w9, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aab39c"></a> `00aab39c` | `a9 02 1b 4a` | eor w9,w21,w27 | `FALL_THROUGH`
<a id="insn-00aab3a0"></a> `00aab3a0` | `08 41 09 2a` | orr w8,w8,w9, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00aab3a4"></a> `00aab3a4` | `e9 01 1c 4a` | eor w9,w15,w28 | `FALL_THROUGH`
<a id="insn-00aab3a8"></a> `00aab3a8` | `08 61 09 2a` | orr w8,w8,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aab3ac"></a> `00aab3ac` | `13 09 00 51` | sub w19,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aab3b0"></a> `00aab3b0` | `74 d0 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aab3b4"></a> `00aab3b4` | `f8 22 7f a9` | ldp x24,x8,[x23, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab3b8"></a> `00aab3b8` | `09 c8 33 8b` | add x9,x0,w19, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00aab3bc"></a> `00aab3bc` | `8a e6 92 52` | mov w10,#0x9734 | `FALL_THROUGH`
<a id="insn-00aab3c0"></a> `00aab3c0` | `8a 00 a0 72` | movk w10,#0x4, LSL #16 | `FALL_THROUGH`
<a id="insn-00aab3c4"></a> `00aab3c4` | `3b 69 6a b8` | ldr w27,[x9, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aab3c8"></a> `00aab3c8` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00aab3cc"></a> `00aab3cc` | `a3 f3 ff 54` | b.cc 0x00aab240 | `CONDITIONAL_JUMP`
<a id="insn-00aab3d0"></a> `00aab3d0` | `e0 62 00 d1` | sub x0,x23,#0x18 | `FALL_THROUGH`
<a id="insn-00aab3d4"></a> `00aab3d4` | `14 00 40 f9` | ldr x20,[x0] | `FALL_THROUGH`
<a id="insn-00aab3d8"></a> `00aab3d8` | `15 03 14 cb` | sub x21,x24,x20 | `FALL_THROUGH`
<a id="insn-00aab3dc"></a> `00aab3dc` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00aab3e0"></a> `00aab3e0` | `09 07 00 91` | add x9,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00aab3e4"></a> `00aab3e4` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-00aab3e8"></a> `00aab3e8` | `ea 03 00 b5` | cbnz x10,0x00aab464 | `CONDITIONAL_JUMP`
<a id="insn-00aab3ec"></a> `00aab3ec` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00aab3f0"></a> `00aab3f0` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aab3f4"></a> `00aab3f4` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00aab3f8"></a> `00aab3f8` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00aab3fc"></a> `00aab3fc` | `ea ef 7d b2` | orr x10,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00aab400"></a> `00aab400` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00aab404"></a> `00aab404` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00aab408"></a> `00aab408` | `3c 31 88 9a` | csel x28,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00aab40c"></a> `00aab40c` | `fc 00 00 b4` | cbz x28,0x00aab428 | `CONDITIONAL_JUMP`
<a id="insn-00aab410"></a> `00aab410` | `88 ff 7d d3` | lsr x8,x28,#0x3d | `FALL_THROUGH`
<a id="insn-00aab414"></a> `00aab414` | `48 03 00 b5` | cbnz x8,0x00aab47c | `CONDITIONAL_JUMP`
<a id="insn-00aab418"></a> `00aab418` | `80 f3 7d d3` | lsl x0,x28,#0x3 | `FALL_THROUGH`
<a id="insn-00aab41c"></a> `00aab41c` | `09 bf 04 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00aab420"></a> `00aab420` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aab424"></a> `00aab424` | `02 00 00 14` | b 0x00aab42c | `UNCONDITIONAL_JUMP`
<a id="insn-00aab428"></a> `00aab428` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00aab42c"></a> `00aab42c` | `d8 0e 18 8b` | add x24,x22,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aab430"></a> `00aab430` | `68 82 1b aa` | orr x8,x19,x27, LSL #0x20 | `FALL_THROUGH`
<a id="insn-00aab434"></a> `00aab434` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aab438"></a> `00aab438` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00aab43c"></a> `00aab43c` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00aab440"></a> `00aab440` | `d3 0e 1c 8b` | add x19,x22,x28, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aab444"></a> `00aab444` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00aab448"></a> `00aab448` | `5a bf 04 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aab44c"></a> `00aab44c` | `f6 e2 3e a9` | stp x22,x24,[x23, #-0x18] | `FALL_THROUGH`
<a id="insn-00aab450"></a> `00aab450` | `f3 82 1f f8` | stur x19,[x23, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab454"></a> `00aab454` | `b4 ef ff b4` | cbz x20,0x00aab248 | `CONDITIONAL_JUMP`
<a id="insn-00aab458"></a> `00aab458` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aab45c"></a> `00aab45c` | `01 bf 04 94` | bl 0x00bdb060 | `UNCONDITIONAL_CALL`
<a id="insn-00aab460"></a> `00aab460` | `7a ff ff 17` | b 0x00aab248 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab464"></a> `00aab464` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aab468"></a> `00aab468` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aab46c"></a> `00aab46c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab470"></a> `00aab470` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab474"></a> `00aab474` | `a1 02 00 54` | b.ne 0x00aab4c8 | `CONDITIONAL_JUMP`
<a id="insn-00aab478"></a> `00aab478` | `c3 05 00 94` | bl 0x00aacb84 | `UNCONDITIONAL_CALL`
<a id="insn-00aab47c"></a> `00aab47c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aab480"></a> `00aab480` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aab484"></a> `00aab484` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab488"></a> `00aab488` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab48c"></a> `00aab48c` | `e1 01 00 54` | b.ne 0x00aab4c8 | `CONDITIONAL_JUMP`
<a id="insn-00aab490"></a> `00aab490` | `bc cb e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-00aab4c8"></a> `00aab4c8` | `f2 be 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaafe8`](#insn-00aaafe8) 範囲 `[['00aaafe8', '00aab02b']]`
  - `CONDITIONAL_JUMP` [`00aab028`](#insn-00aab028) → [`00aab048`](#insn-00aab048)
  - `FALL_THROUGH` [`00aab028`](#insn-00aab028) → [`00aab02c`](#insn-00aab02c)
- ブロック [`00aab02c`](#insn-00aab02c) 範囲 `[['00aab02c', '00aab047']]`
  - `FALL_THROUGH` [`00aab044`](#insn-00aab044) → [`00aab048`](#insn-00aab048)
- ブロック [`00aab048`](#insn-00aab048) 範囲 `[['00aab048', '00aab06f']]`
  - `CONDITIONAL_JUMP` [`00aab06c`](#insn-00aab06c) → [`00aab080`](#insn-00aab080)
  - `FALL_THROUGH` [`00aab06c`](#insn-00aab06c) → [`00aab070`](#insn-00aab070)
- ブロック [`00aab070`](#insn-00aab070) 範囲 `[['00aab070', '00aab073']]`
  - `UNCONDITIONAL_JUMP` [`00aab070`](#insn-00aab070) → [`00aab0a4`](#insn-00aab0a4)
- ブロック [`00aab074`](#insn-00aab074) 範囲 `[['00aab074', '00aab07f']]`
  - `CONDITIONAL_JUMP` [`00aab07c`](#insn-00aab07c) → [`00aab0a4`](#insn-00aab0a4)
  - `FALL_THROUGH` [`00aab07c`](#insn-00aab07c) → [`00aab080`](#insn-00aab080)
- ブロック [`00aab080`](#insn-00aab080) 範囲 `[['00aab080', '00aab08f']]`
  - `CONDITIONAL_JUMP` [`00aab08c`](#insn-00aab08c) → [`00aab074`](#insn-00aab074)
  - `FALL_THROUGH` [`00aab08c`](#insn-00aab08c) → [`00aab090`](#insn-00aab090)
- ブロック [`00aab090`](#insn-00aab090) 範囲 `[['00aab090', '00aab097']]`
  - `CONDITIONAL_JUMP` [`00aab094`](#insn-00aab094) → [`00aab0f8`](#insn-00aab0f8)
  - `FALL_THROUGH` [`00aab094`](#insn-00aab094) → [`00aab098`](#insn-00aab098)
- ブロック [`00aab098`](#insn-00aab098) 範囲 `[['00aab098', '00aab09f']]`
  - `CONDITIONAL_JUMP` [`00aab09c`](#insn-00aab09c) → [`00aab080`](#insn-00aab080)
  - `FALL_THROUGH` [`00aab09c`](#insn-00aab09c) → [`00aab0a0`](#insn-00aab0a0)
- ブロック [`00aab0a0`](#insn-00aab0a0) 範囲 `[['00aab0a0', '00aab0a3']]`
  - `FALL_THROUGH` [`00aab0a0`](#insn-00aab0a0) → [`00aab0a4`](#insn-00aab0a4)
- ブロック [`00aab0a4`](#insn-00aab0a4) 範囲 `[['00aab0a4', '00aab0db']]`
  - `CONDITIONAL_JUMP` [`00aab0d8`](#insn-00aab0d8) → [`00aab0e4`](#insn-00aab0e4)
  - `FALL_THROUGH` [`00aab0d8`](#insn-00aab0d8) → [`00aab0dc`](#insn-00aab0dc)
- ブロック [`00aab0dc`](#insn-00aab0dc) 範囲 `[['00aab0dc', '00aab0e3']]`
  - `FALL_THROUGH` [`00aab0e0`](#insn-00aab0e0) → [`00aab0e4`](#insn-00aab0e4)
- ブロック [`00aab0e4`](#insn-00aab0e4) 範囲 `[['00aab0e4', '00aab0f7']]`
  - `FALL_THROUGH` [`00aab0f4`](#insn-00aab0f4) → [`00aab0f8`](#insn-00aab0f8)
- ブロック [`00aab0f8`](#insn-00aab0f8) 範囲 `[['00aab0f8', '00aab117']]`
  - `CONDITIONAL_JUMP` [`00aab114`](#insn-00aab114) → [`00aab14c`](#insn-00aab14c)
  - `FALL_THROUGH` [`00aab114`](#insn-00aab114) → [`00aab118`](#insn-00aab118)
- ブロック [`00aab118`](#insn-00aab118) 範囲 `[['00aab118', '00aab12b']]`
  - `CONDITIONAL_JUMP` [`00aab128`](#insn-00aab128) → [`00aab4c8`](#insn-00aab4c8)
  - `FALL_THROUGH` [`00aab128`](#insn-00aab128) → [`00aab12c`](#insn-00aab12c)
- ブロック [`00aab12c`](#insn-00aab12c) 範囲 `[['00aab12c', '00aab14b']]`
- ブロック [`00aab14c`](#insn-00aab14c) 範囲 `[['00aab14c', '00aab15b']]`
  - `CONDITIONAL_JUMP` [`00aab158`](#insn-00aab158) → [`00aab16c`](#insn-00aab16c)
  - `FALL_THROUGH` [`00aab158`](#insn-00aab158) → [`00aab15c`](#insn-00aab15c)
- ブロック [`00aab15c`](#insn-00aab15c) 範囲 `[['00aab15c', '00aab15f']]`
  - `UNCONDITIONAL_JUMP` [`00aab15c`](#insn-00aab15c) → [`00aab190`](#insn-00aab190)
- ブロック [`00aab160`](#insn-00aab160) 範囲 `[['00aab160', '00aab16b']]`
  - `CONDITIONAL_JUMP` [`00aab168`](#insn-00aab168) → [`00aab190`](#insn-00aab190)
  - `FALL_THROUGH` [`00aab168`](#insn-00aab168) → [`00aab16c`](#insn-00aab16c)
- ブロック [`00aab16c`](#insn-00aab16c) 範囲 `[['00aab16c', '00aab17b']]`
  - `CONDITIONAL_JUMP` [`00aab178`](#insn-00aab178) → [`00aab160`](#insn-00aab160)
  - `FALL_THROUGH` [`00aab178`](#insn-00aab178) → [`00aab17c`](#insn-00aab17c)
- ブロック [`00aab17c`](#insn-00aab17c) 範囲 `[['00aab17c', '00aab183']]`
  - `CONDITIONAL_JUMP` [`00aab180`](#insn-00aab180) → [`00aab1e4`](#insn-00aab1e4)
  - `FALL_THROUGH` [`00aab180`](#insn-00aab180) → [`00aab184`](#insn-00aab184)
- ブロック [`00aab184`](#insn-00aab184) 範囲 `[['00aab184', '00aab18b']]`
  - `CONDITIONAL_JUMP` [`00aab188`](#insn-00aab188) → [`00aab16c`](#insn-00aab16c)
  - `FALL_THROUGH` [`00aab188`](#insn-00aab188) → [`00aab18c`](#insn-00aab18c)
- ブロック [`00aab18c`](#insn-00aab18c) 範囲 `[['00aab18c', '00aab18f']]`
  - `FALL_THROUGH` [`00aab18c`](#insn-00aab18c) → [`00aab190`](#insn-00aab190)
- ブロック [`00aab190`](#insn-00aab190) 範囲 `[['00aab190', '00aab1c7']]`
  - `CONDITIONAL_JUMP` [`00aab1c4`](#insn-00aab1c4) → [`00aab1d0`](#insn-00aab1d0)
  - `FALL_THROUGH` [`00aab1c4`](#insn-00aab1c4) → [`00aab1c8`](#insn-00aab1c8)
- ブロック [`00aab1c8`](#insn-00aab1c8) 範囲 `[['00aab1c8', '00aab1cf']]`
  - `FALL_THROUGH` [`00aab1cc`](#insn-00aab1cc) → [`00aab1d0`](#insn-00aab1d0)
- ブロック [`00aab1d0`](#insn-00aab1d0) 範囲 `[['00aab1d0', '00aab1e3']]`
  - `FALL_THROUGH` [`00aab1e0`](#insn-00aab1e0) → [`00aab1e4`](#insn-00aab1e4)
- ブロック [`00aab1e4`](#insn-00aab1e4) 範囲 `[['00aab1e4', '00aab1f7']]`
  - `CONDITIONAL_JUMP` [`00aab1f4`](#insn-00aab1f4) → [`00aab210`](#insn-00aab210)
  - `FALL_THROUGH` [`00aab1f4`](#insn-00aab1f4) → [`00aab1f8`](#insn-00aab1f8)
- ブロック [`00aab1f8`](#insn-00aab1f8) 範囲 `[['00aab1f8', '00aab20f']]`
  - `UNCONDITIONAL_JUMP` [`00aab20c`](#insn-00aab20c) → [`00aab234`](#insn-00aab234)
- ブロック [`00aab210`](#insn-00aab210) 範囲 `[['00aab210', '00aab22b']]`
  - `CONDITIONAL_JUMP` [`00aab228`](#insn-00aab228) → [`00aab234`](#insn-00aab234)
  - `FALL_THROUGH` [`00aab228`](#insn-00aab228) → [`00aab22c`](#insn-00aab22c)
- ブロック [`00aab22c`](#insn-00aab22c) 範囲 `[['00aab22c', '00aab233']]`
  - `FALL_THROUGH` [`00aab230`](#insn-00aab230) → [`00aab234`](#insn-00aab234)
- ブロック [`00aab234`](#insn-00aab234) 範囲 `[['00aab234', '00aab23f']]`
  - `UNCONDITIONAL_JUMP` [`00aab23c`](#insn-00aab23c) → [`00aab25c`](#insn-00aab25c)
- ブロック [`00aab240`](#insn-00aab240) 範囲 `[['00aab240', '00aab247']]`
  - `FALL_THROUGH` [`00aab244`](#insn-00aab244) → [`00aab248`](#insn-00aab248)
- ブロック [`00aab248`](#insn-00aab248) 範囲 `[['00aab248', '00aab25b']]`
  - `CONDITIONAL_JUMP` [`00aab258`](#insn-00aab258) → [`00aab118`](#insn-00aab118)
  - `FALL_THROUGH` [`00aab258`](#insn-00aab258) → [`00aab25c`](#insn-00aab25c)
- ブロック [`00aab25c`](#insn-00aab25c) 範囲 `[['00aab25c', '00aab2b7']]`
  - `CONDITIONAL_JUMP` [`00aab2b4`](#insn-00aab2b4) → [`00aab118`](#insn-00aab118)
  - `FALL_THROUGH` [`00aab2b4`](#insn-00aab2b4) → [`00aab2b8`](#insn-00aab2b8)
- ブロック [`00aab2b8`](#insn-00aab2b8) 範囲 `[['00aab2b8', '00aab2f3']]`
  - `UNCONDITIONAL_JUMP` [`00aab2f0`](#insn-00aab2f0) → [`00aab2f8`](#insn-00aab2f8)
- ブロック [`00aab2f4`](#insn-00aab2f4) 範囲 `[['00aab2f4', '00aab2f7']]`
  - `FALL_THROUGH` [`00aab2f4`](#insn-00aab2f4) → [`00aab2f8`](#insn-00aab2f8)
- ブロック [`00aab2f8`](#insn-00aab2f8) 範囲 `[['00aab2f8', '00aab2ff']]`
  - `CONDITIONAL_JUMP` [`00aab2fc`](#insn-00aab2fc) → [`00aab324`](#insn-00aab324)
  - `FALL_THROUGH` [`00aab2fc`](#insn-00aab2fc) → [`00aab300`](#insn-00aab300)
- ブロック [`00aab300`](#insn-00aab300) 範囲 `[['00aab300', '00aab30f']]`
  - `CONDITIONAL_JUMP` [`00aab30c`](#insn-00aab30c) → [`00aab2f4`](#insn-00aab2f4)
  - `FALL_THROUGH` [`00aab30c`](#insn-00aab30c) → [`00aab310`](#insn-00aab310)
- ブロック [`00aab310`](#insn-00aab310) 範囲 `[['00aab310', '00aab317']]`
  - `CONDITIONAL_JUMP` [`00aab314`](#insn-00aab314) → [`00aab38c`](#insn-00aab38c)
  - `FALL_THROUGH` [`00aab314`](#insn-00aab314) → [`00aab318`](#insn-00aab318)
- ブロック [`00aab318`](#insn-00aab318) 範囲 `[['00aab318', '00aab31f']]`
  - `CONDITIONAL_JUMP` [`00aab31c`](#insn-00aab31c) → [`00aab300`](#insn-00aab300)
  - `FALL_THROUGH` [`00aab31c`](#insn-00aab31c) → [`00aab320`](#insn-00aab320)
- ブロック [`00aab320`](#insn-00aab320) 範囲 `[['00aab320', '00aab323']]`
  - `FALL_THROUGH` [`00aab320`](#insn-00aab320) → [`00aab324`](#insn-00aab324)
- ブロック [`00aab324`](#insn-00aab324) 範囲 `[['00aab324', '00aab367']]`
  - `CONDITIONAL_JUMP` [`00aab364`](#insn-00aab364) → [`00aab370`](#insn-00aab370)
  - `FALL_THROUGH` [`00aab364`](#insn-00aab364) → [`00aab368`](#insn-00aab368)
- ブロック [`00aab368`](#insn-00aab368) 範囲 `[['00aab368', '00aab36f']]`
  - `FALL_THROUGH` [`00aab36c`](#insn-00aab36c) → [`00aab370`](#insn-00aab370)
- ブロック [`00aab370`](#insn-00aab370) 範囲 `[['00aab370', '00aab38b']]`
  - `FALL_THROUGH` [`00aab388`](#insn-00aab388) → [`00aab38c`](#insn-00aab38c)
- ブロック [`00aab38c`](#insn-00aab38c) 範囲 `[['00aab38c', '00aab3cf']]`
  - `CONDITIONAL_JUMP` [`00aab3cc`](#insn-00aab3cc) → [`00aab240`](#insn-00aab240)
  - `FALL_THROUGH` [`00aab3cc`](#insn-00aab3cc) → [`00aab3d0`](#insn-00aab3d0)
- ブロック [`00aab3d0`](#insn-00aab3d0) 範囲 `[['00aab3d0', '00aab3eb']]`
  - `CONDITIONAL_JUMP` [`00aab3e8`](#insn-00aab3e8) → [`00aab464`](#insn-00aab464)
  - `FALL_THROUGH` [`00aab3e8`](#insn-00aab3e8) → [`00aab3ec`](#insn-00aab3ec)
- ブロック [`00aab3ec`](#insn-00aab3ec) 範囲 `[['00aab3ec', '00aab40f']]`
  - `CONDITIONAL_JUMP` [`00aab40c`](#insn-00aab40c) → [`00aab428`](#insn-00aab428)
  - `FALL_THROUGH` [`00aab40c`](#insn-00aab40c) → [`00aab410`](#insn-00aab410)
- ブロック [`00aab410`](#insn-00aab410) 範囲 `[['00aab410', '00aab417']]`
  - `CONDITIONAL_JUMP` [`00aab414`](#insn-00aab414) → [`00aab47c`](#insn-00aab47c)
  - `FALL_THROUGH` [`00aab414`](#insn-00aab414) → [`00aab418`](#insn-00aab418)
- ブロック [`00aab418`](#insn-00aab418) 範囲 `[['00aab418', '00aab427']]`
  - `UNCONDITIONAL_JUMP` [`00aab424`](#insn-00aab424) → [`00aab42c`](#insn-00aab42c)
- ブロック [`00aab428`](#insn-00aab428) 範囲 `[['00aab428', '00aab42b']]`
  - `FALL_THROUGH` [`00aab428`](#insn-00aab428) → [`00aab42c`](#insn-00aab42c)
- ブロック [`00aab42c`](#insn-00aab42c) 範囲 `[['00aab42c', '00aab457']]`
  - `CONDITIONAL_JUMP` [`00aab454`](#insn-00aab454) → [`00aab248`](#insn-00aab248)
  - `FALL_THROUGH` [`00aab454`](#insn-00aab454) → [`00aab458`](#insn-00aab458)
- ブロック [`00aab458`](#insn-00aab458) 範囲 `[['00aab458', '00aab463']]`
  - `UNCONDITIONAL_JUMP` [`00aab460`](#insn-00aab460) → [`00aab248`](#insn-00aab248)
- ブロック [`00aab464`](#insn-00aab464) 範囲 `[['00aab464', '00aab477']]`
  - `CONDITIONAL_JUMP` [`00aab474`](#insn-00aab474) → [`00aab4c8`](#insn-00aab4c8)
  - `FALL_THROUGH` [`00aab474`](#insn-00aab474) → [`00aab478`](#insn-00aab478)
- ブロック [`00aab478`](#insn-00aab478) 範囲 `[['00aab478', '00aab47b']]`
  - `FALL_THROUGH` [`00aab478`](#insn-00aab478) → [`00aab47c`](#insn-00aab47c)
- ブロック [`00aab47c`](#insn-00aab47c) 範囲 `[['00aab47c', '00aab48f']]`
  - `CONDITIONAL_JUMP` [`00aab48c`](#insn-00aab48c) → [`00aab4c8`](#insn-00aab4c8)
  - `FALL_THROUGH` [`00aab48c`](#insn-00aab48c) → [`00aab490`](#insn-00aab490)
- ブロック [`00aab490`](#insn-00aab490) 範囲 `[['00aab490', '00aab493']]`
- ブロック [`00aab4c8`](#insn-00aab4c8) 範囲 `[['00aab4c8', '00aab4cb']]`

## 命令位置別の参照

- [`00aaafec`](#insn-00aaafec) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaff0`](#insn-00aaaff0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaff4`](#insn-00aaaff4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaff8`](#insn-00aaaff8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaffc`](#insn-00aaaffc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab000`](#insn-00aab000) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab014`](#insn-00aab014) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab024`](#insn-00aab024) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab028`](#insn-00aab028) → [`00aab048`](#insn-00aab048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab030`](#insn-00aab030) → [`007cf950`](../007cf/007cf950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf950` · 推定シンボル `None` · 推定型 `None`
- [`00aab038`](#insn-00aab038) → [`007cfaa0`](../007cf/007cfaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfaa0` · 推定シンボル `None` · 推定型 `None`
- [`00aab040`](#insn-00aab040) → [`007cfcd8`](../007cf/007cfcd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfcd8` · 推定シンボル `None` · 推定型 `None`
- [`00aab068`](#insn-00aab068) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab06c`](#insn-00aab06c) → [`00aab080`](#insn-00aab080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab070`](#insn-00aab070) → [`00aab0a4`](#insn-00aab0a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab07c`](#insn-00aab07c) → [`00aab0a4`](#insn-00aab0a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab08c`](#insn-00aab08c) → [`00aab074`](#insn-00aab074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab094`](#insn-00aab094) → [`00aab0f8`](#insn-00aab0f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab09c`](#insn-00aab09c) → [`00aab080`](#insn-00aab080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0ac`](#insn-00aab0ac) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00aab0d8`](#insn-00aab0d8) → [`00aab0e4`](#insn-00aab0e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0e8`](#insn-00aab0e8) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aab114`](#insn-00aab114) → [`00aab14c`](#insn-00aab14c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab118`](#insn-00aab118) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab120`](#insn-00aab120) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab128`](#insn-00aab128) → [`00aab4c8`](#insn-00aab4c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab12c`](#insn-00aab12c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab130`](#insn-00aab130) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab134`](#insn-00aab134) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab138`](#insn-00aab138) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab13c`](#insn-00aab13c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab140`](#insn-00aab140) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab14c`](#insn-00aab14c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab158`](#insn-00aab158) → [`00aab16c`](#insn-00aab16c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab15c`](#insn-00aab15c) → [`00aab190`](#insn-00aab190) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab168`](#insn-00aab168) → [`00aab190`](#insn-00aab190) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab178`](#insn-00aab178) → [`00aab160`](#insn-00aab160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab180`](#insn-00aab180) → [`00aab1e4`](#insn-00aab1e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab188`](#insn-00aab188) → [`00aab16c`](#insn-00aab16c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab198`](#insn-00aab198) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00aab1c4`](#insn-00aab1c4) → [`00aab1d0`](#insn-00aab1d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1d4`](#insn-00aab1d4) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aab1e8`](#insn-00aab1e8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1ec`](#insn-00aab1ec) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1f4`](#insn-00aab1f4) → [`00aab210`](#insn-00aab210) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab200`](#insn-00aab200) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab20c`](#insn-00aab20c) → [`00aab234`](#insn-00aab234) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab218`](#insn-00aab218) → [`00aacb98`](../00aac/00aacb98.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aacb98` · 推定シンボル `None` · 推定型 `None`
- [`00aab220`](#insn-00aab220) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab228`](#insn-00aab228) → [`00aab234`](#insn-00aab234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab22c`](#insn-00aab22c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab230`](#insn-00aab230) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aab23c`](#insn-00aab23c) → [`00aab25c`](#insn-00aab25c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab258`](#insn-00aab258) → [`00aab118`](#insn-00aab118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab25c`](#insn-00aab25c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aab2b4`](#insn-00aab2b4) → [`00aab118`](#insn-00aab118) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2b8`](#insn-00aab2b8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aab2bc`](#insn-00aab2bc) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2f0`](#insn-00aab2f0) → [`00aab2f8`](#insn-00aab2f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2fc`](#insn-00aab2fc) → [`00aab324`](#insn-00aab324) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab30c`](#insn-00aab30c) → [`00aab2f4`](#insn-00aab2f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab314`](#insn-00aab314) → [`00aab38c`](#insn-00aab38c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab31c`](#insn-00aab31c) → [`00aab300`](#insn-00aab300) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab328`](#insn-00aab328) → `Stack[-0x8c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab330`](#insn-00aab330) → `Stack[-0x84]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab334`](#insn-00aab334) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00aab33c`](#insn-00aab33c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab364`](#insn-00aab364) → [`00aab370`](#insn-00aab370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab374`](#insn-00aab374) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aab37c`](#insn-00aab37c) → `Stack[-0x84]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab380`](#insn-00aab380) → `Stack[-0x8c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab3b0`](#insn-00aab3b0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aab3cc`](#insn-00aab3cc) → [`00aab240`](#insn-00aab240) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab3e8`](#insn-00aab3e8) → [`00aab464`](#insn-00aab464) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab40c`](#insn-00aab40c) → [`00aab428`](#insn-00aab428) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab414`](#insn-00aab414) → [`00aab47c`](#insn-00aab47c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab41c`](#insn-00aab41c) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00aab424`](#insn-00aab424) → [`00aab42c`](#insn-00aab42c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab448`](#insn-00aab448) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00aab454`](#insn-00aab454) → [`00aab248`](#insn-00aab248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab45c`](#insn-00aab45c) → [`00bdb060`](../00bdb/00bdb060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb060` · 推定シンボル `None` · 推定型 `None`
- [`00aab460`](#insn-00aab460) → [`00aab248`](#insn-00aab248) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab464`](#insn-00aab464) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab46c`](#insn-00aab46c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab474`](#insn-00aab474) → [`00aab4c8`](#insn-00aab4c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab478`](#insn-00aab478) → [`00aacb84`](../00aac/00aacb84.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aacb84` · 推定シンボル `None` · 推定型 `None`
- [`00aab47c`](#insn-00aab47c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab484`](#insn-00aab484) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab48c`](#insn-00aab48c) → [`00aab4c8`](#insn-00aab4c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab490`](#insn-00aab490) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`00aab4c8`](#insn-00aab4c8) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaafec`](#insn-00aaafec)

~~~json
{
  "source": "00aaafec",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaff0`](#insn-00aaaff0)

~~~json
{
  "source": "00aaaff0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaff4`](#insn-00aaaff4)

~~~json
{
  "source": "00aaaff4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaff8`](#insn-00aaaff8)

~~~json
{
  "source": "00aaaff8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaffc`](#insn-00aaaffc)

~~~json
{
  "source": "00aaaffc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab000`](#insn-00aab000)

~~~json
{
  "source": "00aab000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab014`](#insn-00aab014)

~~~json
{
  "source": "00aab014",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab024`](#insn-00aab024)

~~~json
{
  "source": "00aab024",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab028`](#insn-00aab028)

~~~json
{
  "source": "00aab028",
  "target": "00aab048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab030`](#insn-00aab030)

~~~json
{
  "source": "00aab030",
  "target": "007cf950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab038`](#insn-00aab038)

~~~json
{
  "source": "00aab038",
  "target": "007cfaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab040`](#insn-00aab040)

~~~json
{
  "source": "00aab040",
  "target": "007cfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab068`](#insn-00aab068)

~~~json
{
  "source": "00aab068",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab06c`](#insn-00aab06c)

~~~json
{
  "source": "00aab06c",
  "target": "00aab080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab070`](#insn-00aab070)

~~~json
{
  "source": "00aab070",
  "target": "00aab0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab07c`](#insn-00aab07c)

~~~json
{
  "source": "00aab07c",
  "target": "00aab0a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab08c`](#insn-00aab08c)

~~~json
{
  "source": "00aab08c",
  "target": "00aab074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab094`](#insn-00aab094)

~~~json
{
  "source": "00aab094",
  "target": "00aab0f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab09c`](#insn-00aab09c)

~~~json
{
  "source": "00aab09c",
  "target": "00aab080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0ac`](#insn-00aab0ac)

~~~json
{
  "source": "00aab0ac",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab0d8`](#insn-00aab0d8)

~~~json
{
  "source": "00aab0d8",
  "target": "00aab0e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0e8`](#insn-00aab0e8)

~~~json
{
  "source": "00aab0e8",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab114`](#insn-00aab114)

~~~json
{
  "source": "00aab114",
  "target": "00aab14c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab118`](#insn-00aab118)

~~~json
{
  "source": "00aab118",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab120`](#insn-00aab120)

~~~json
{
  "source": "00aab120",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab128`](#insn-00aab128)

~~~json
{
  "source": "00aab128",
  "target": "00aab4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab12c`](#insn-00aab12c)

~~~json
{
  "source": "00aab12c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab130`](#insn-00aab130)

~~~json
{
  "source": "00aab130",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab134`](#insn-00aab134)

~~~json
{
  "source": "00aab134",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab138`](#insn-00aab138)

~~~json
{
  "source": "00aab138",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab13c`](#insn-00aab13c)

~~~json
{
  "source": "00aab13c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab140`](#insn-00aab140)

~~~json
{
  "source": "00aab140",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab14c`](#insn-00aab14c)

~~~json
{
  "source": "00aab14c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab158`](#insn-00aab158)

~~~json
{
  "source": "00aab158",
  "target": "00aab16c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab15c`](#insn-00aab15c)

~~~json
{
  "source": "00aab15c",
  "target": "00aab190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab168`](#insn-00aab168)

~~~json
{
  "source": "00aab168",
  "target": "00aab190",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab178`](#insn-00aab178)

~~~json
{
  "source": "00aab178",
  "target": "00aab160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab180`](#insn-00aab180)

~~~json
{
  "source": "00aab180",
  "target": "00aab1e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab188`](#insn-00aab188)

~~~json
{
  "source": "00aab188",
  "target": "00aab16c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab198`](#insn-00aab198)

~~~json
{
  "source": "00aab198",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab1c4`](#insn-00aab1c4)

~~~json
{
  "source": "00aab1c4",
  "target": "00aab1d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1d4`](#insn-00aab1d4)

~~~json
{
  "source": "00aab1d4",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab1e8`](#insn-00aab1e8)

~~~json
{
  "source": "00aab1e8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1ec`](#insn-00aab1ec)

~~~json
{
  "source": "00aab1ec",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1f4`](#insn-00aab1f4)

~~~json
{
  "source": "00aab1f4",
  "target": "00aab210",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab200`](#insn-00aab200)

~~~json
{
  "source": "00aab200",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab20c`](#insn-00aab20c)

~~~json
{
  "source": "00aab20c",
  "target": "00aab234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab218`](#insn-00aab218)

~~~json
{
  "source": "00aab218",
  "target": "00aacb98",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab220`](#insn-00aab220)

~~~json
{
  "source": "00aab220",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab228`](#insn-00aab228)

~~~json
{
  "source": "00aab228",
  "target": "00aab234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab22c`](#insn-00aab22c)

~~~json
{
  "source": "00aab22c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab230`](#insn-00aab230)

~~~json
{
  "source": "00aab230",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab23c`](#insn-00aab23c)

~~~json
{
  "source": "00aab23c",
  "target": "00aab25c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab258`](#insn-00aab258)

~~~json
{
  "source": "00aab258",
  "target": "00aab118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab25c`](#insn-00aab25c)

~~~json
{
  "source": "00aab25c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab2b4`](#insn-00aab2b4)

~~~json
{
  "source": "00aab2b4",
  "target": "00aab118",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2b8`](#insn-00aab2b8)

~~~json
{
  "source": "00aab2b8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab2bc`](#insn-00aab2bc)

~~~json
{
  "source": "00aab2bc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2f0`](#insn-00aab2f0)

~~~json
{
  "source": "00aab2f0",
  "target": "00aab2f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2fc`](#insn-00aab2fc)

~~~json
{
  "source": "00aab2fc",
  "target": "00aab324",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab30c`](#insn-00aab30c)

~~~json
{
  "source": "00aab30c",
  "target": "00aab2f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab314`](#insn-00aab314)

~~~json
{
  "source": "00aab314",
  "target": "00aab38c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab31c`](#insn-00aab31c)

~~~json
{
  "source": "00aab31c",
  "target": "00aab300",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab328`](#insn-00aab328)

~~~json
{
  "source": "00aab328",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab330`](#insn-00aab330)

~~~json
{
  "source": "00aab330",
  "target": "Stack[-0x84]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab334`](#insn-00aab334)

~~~json
{
  "source": "00aab334",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab33c`](#insn-00aab33c)

~~~json
{
  "source": "00aab33c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab364`](#insn-00aab364)

~~~json
{
  "source": "00aab364",
  "target": "00aab370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab374`](#insn-00aab374)

~~~json
{
  "source": "00aab374",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab37c`](#insn-00aab37c)

~~~json
{
  "source": "00aab37c",
  "target": "Stack[-0x84]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab380`](#insn-00aab380)

~~~json
{
  "source": "00aab380",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab3b0`](#insn-00aab3b0)

~~~json
{
  "source": "00aab3b0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab3cc`](#insn-00aab3cc)

~~~json
{
  "source": "00aab3cc",
  "target": "00aab240",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab3e8`](#insn-00aab3e8)

~~~json
{
  "source": "00aab3e8",
  "target": "00aab464",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab40c`](#insn-00aab40c)

~~~json
{
  "source": "00aab40c",
  "target": "00aab428",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab414`](#insn-00aab414)

~~~json
{
  "source": "00aab414",
  "target": "00aab47c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab41c`](#insn-00aab41c)

~~~json
{
  "source": "00aab41c",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab424`](#insn-00aab424)

~~~json
{
  "source": "00aab424",
  "target": "00aab42c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab448`](#insn-00aab448)

~~~json
{
  "source": "00aab448",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab454`](#insn-00aab454)

~~~json
{
  "source": "00aab454",
  "target": "00aab248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab45c`](#insn-00aab45c)

~~~json
{
  "source": "00aab45c",
  "target": "00bdb060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab460`](#insn-00aab460)

~~~json
{
  "source": "00aab460",
  "target": "00aab248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab464`](#insn-00aab464)

~~~json
{
  "source": "00aab464",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab46c`](#insn-00aab46c)

~~~json
{
  "source": "00aab46c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab474`](#insn-00aab474)

~~~json
{
  "source": "00aab474",
  "target": "00aab4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab478`](#insn-00aab478)

~~~json
{
  "source": "00aab478",
  "target": "00aacb84",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab47c`](#insn-00aab47c)

~~~json
{
  "source": "00aab47c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab484`](#insn-00aab484)

~~~json
{
  "source": "00aab484",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab48c`](#insn-00aab48c)

~~~json
{
  "source": "00aab48c",
  "target": "00aab4c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab490`](#insn-00aab490)

~~~json
{
  "source": "00aab490",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab4c8`](#insn-00aab4c8)

~~~json
{
  "source": "00aab4c8",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
