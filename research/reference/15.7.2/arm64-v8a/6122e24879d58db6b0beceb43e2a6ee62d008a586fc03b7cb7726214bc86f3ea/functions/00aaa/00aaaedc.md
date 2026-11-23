# 00aaaedc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aaafa4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aaa/00aaafa4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-5f71ef8828c78c35851f11bd38981c2e)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaaedc",
  "name": "FUN_00aaaedc",
  "size": 1200,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7b7fca21868bc26a91479ea88d9f9a6290219030567bbd4d65a04d01960456ca",
  "source_text_sha256": "7b7fca21868bc26a91479ea88d9f9a6290219030567bbd4d65a04d01960456ca",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaaedc",
        "00aab387"
      ],
      [
        "00aab3bc",
        "00aab3bf"
      ]
    ],
    "bytes_sha256": "409b119d60714f5666f7675d6496f0174a0d1d5cf2cc3e0134490318d6132282",
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
- [00aaca78](../00aac/00aaca78.md)
- [00aaca8c](../00aac/00aaca8c.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7699 bytes

~~~c

void FUN_00aaaedc(long param_1,int param_2,int param_3,int param_4)

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
        if ((undefined8 *)*puVar15 == (undefined8 *)0x0) goto LAB_00aaaf98;
      }
      if (iVar12 <= *(int *)(puVar15 + 4)) goto LAB_00aaafec;
      puVar19 = (undefined8 *)puVar15[1];
    } while ((undefined8 *)puVar15[1] != (undefined8 *)0x0);
    puVar18 = puVar15 + 1;
  }
LAB_00aaaf98:
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
LAB_00aaafec:
  if ((ulong)(((long)(puVar15[6] - puVar15[5]) >> 3) * -0x5555555555555555) < 10) {
    puVar19 = (undefined8 *)*puVar22;
    puVar18 = puVar22;
    puVar24 = puVar22;
    if ((undefined8 *)*puVar22 != (undefined8 *)0x0) {
      do {
        while (puVar15 = puVar19, puVar24 = puVar15, iVar12 < *(int *)(puVar15 + 4)) {
          puVar19 = (undefined8 *)*puVar15;
          puVar18 = puVar15;
          if ((undefined8 *)*puVar15 == (undefined8 *)0x0) goto LAB_00aab084;
        }
        if (iVar12 <= *(int *)(puVar15 + 4)) goto LAB_00aab0d8;
        puVar19 = (undefined8 *)puVar15[1];
      } while ((undefined8 *)puVar15[1] != (undefined8 *)0x0);
      puVar18 = puVar15 + 1;
    }
LAB_00aab084:
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
LAB_00aab0d8:
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
      uVar16 = FUN_00aaca8c(puVar15 + 5,&local_80);
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
          if (iVar12 <= *(int *)(puVar18 + 4)) goto LAB_00aab280;
          puVar19 = (undefined8 *)puVar18[1];
          if ((undefined8 *)puVar18[1] == (undefined8 *)0x0) {
            puVar24 = puVar18 + 1;
            puVar15 = puVar18;
            goto LAB_00aab218;
          }
        }
        puVar19 = (undefined8 *)*puVar18;
      }
LAB_00aab218:
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
LAB_00aab280:
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
            FUN_00aaca78();
LAB_00aab370:
            if (*(long *)(lVar14 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_0041e380();
            }
          }
          goto LAB_00aab3bc;
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
          if (uVar23 >> 0x3d != 0) goto LAB_00aab370;
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
LAB_00aab3bc:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaaedc"></a> `00aaaedc` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00aaaee0"></a> `00aaaee0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aaaee4"></a> `00aaaee4` | `fc 6f 06 a9` | stp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aaaee8"></a> `00aaaee8` | `fa 67 07 a9` | stp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aaaeec"></a> `00aaaeec` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aaaef0"></a> `00aaaef0` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aaaef4"></a> `00aaaef4` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aaaef8"></a> `00aaaef8` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00aaaefc"></a> `00aaaefc` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aaaf00"></a> `00aaaf00` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00aaaf04"></a> `00aaaf04` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00aaaf08"></a> `00aaaf08` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aaaf0c"></a> `00aaaf0c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aaaf10"></a> `00aaaf10` | `3f 04 00 31` | cmn w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aaaf14"></a> `00aaaf14` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aaaf18"></a> `00aaaf18` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aaaf1c"></a> `00aaaf1c` | `01 01 00 54` | b.ne 0x00aaaf3c | `CONDITIONAL_JUMP`
<a id="insn-00aaaf20"></a> `00aaaf20` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aaaf24"></a> `00aaaf24` | `8b 92 f4 97` | bl 0x007cf950 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaf28"></a> `00aaaf28` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aaaf2c"></a> `00aaaf2c` | `dd 92 f4 97` | bl 0x007cfaa0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaf30"></a> `00aaaf30` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aaaf34"></a> `00aaaf34` | `69 93 f4 97` | bl 0x007cfcd8 | `UNCONDITIONAL_CALL`
<a id="insn-00aaaf38"></a> `00aaaf38` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-00aaaf3c"></a> `00aaaf3c` | `48 01 80 52` | mov w8,#0xa | `FALL_THROUGH`
<a id="insn-00aaaf40"></a> `00aaaf40` | `09 7d 80 52` | mov w9,#0x3e8 | `FALL_THROUGH`
<a id="insn-00aaaf44"></a> `00aaaf44` | `ea 03 16 aa` | mov x10,x22 | `FALL_THROUGH`
<a id="insn-00aaaf48"></a> `00aaaf48` | `a8 0e 08 1b` | madd w8,w21,w8,w3 | `FALL_THROUGH`
<a id="insn-00aaaf4c"></a> `00aaaf4c` | `99 22 09 1b` | madd w25,w20,w9,w8 | `FALL_THROUGH`
<a id="insn-00aaaf50"></a> `00aaaf50` | `48 0d 42 f8` | ldr x8,[x10, #0x20]! | `FALL_THROUGH`
<a id="insn-00aaaf54"></a> `00aaaf54` | `f3 03 0a aa` | mov x19,x10 | `FALL_THROUGH`
<a id="insn-00aaaf58"></a> `00aaaf58` | `f4 03 0a aa` | mov x20,x10 | `FALL_THROUGH`
<a id="insn-00aaaf5c"></a> `00aaaf5c` | `f6 2b 01 a9` | stp x22,x10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaaf60"></a> `00aaaf60` | `a8 00 00 b5` | cbnz x8,0x00aaaf74 | `CONDITIONAL_JUMP`
<a id="insn-00aaaf64"></a> `00aaaf64` | `0d 00 00 14` | b 0x00aaaf98 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaaf68"></a> `00aaaf68` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aaaf6c"></a> `00aaaf6c` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00aaaf70"></a> `00aaaf70` | `48 01 00 b4` | cbz x8,0x00aaaf98 | `CONDITIONAL_JUMP`
<a id="insn-00aaaf74"></a> `00aaaf74` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aaaf78"></a> `00aaaf78` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aaaf7c"></a> `00aaaf7c` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00aaaf80"></a> `00aaaf80` | `4b ff ff 54` | b.lt 0x00aaaf68 | `CONDITIONAL_JUMP`
<a id="insn-00aaaf84"></a> `00aaaf84` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00aaaf88"></a> `00aaaf88` | `2a 03 00 54` | b.ge 0x00aaafec | `CONDITIONAL_JUMP`
<a id="insn-00aaaf8c"></a> `00aaaf8c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aaaf90"></a> `00aaaf90` | `28 ff ff b5` | cbnz x8,0x00aaaf74 | `CONDITIONAL_JUMP`
<a id="insn-00aaaf94"></a> `00aaaf94` | `93 22 00 91` | add x19,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aaaf98"></a> `00aaaf98` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aaaf9c"></a> `00aaaf9c` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-00aaafa0"></a> `00aaafa0` | `e8 bf 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00aaafa4"></a> `00aaafa4` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aaafa8"></a> `00aaafa8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aaafac"></a> `00aaafac` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aaafb0"></a> `00aaafb0` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aaafb4"></a> `00aaafb4` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aaafb8"></a> `00aaafb8` | `15 08 00 f9` | str x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aaafbc"></a> `00aaafbc` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00aaafc0"></a> `00aaafc0` | `c8 0e 40 f9` | ldr x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aaafc4"></a> `00aaafc4` | `19 20 00 b9` | str w25,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aaafc8"></a> `00aaafc8` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aaafcc"></a> `00aaafcc` | `68 00 00 b4` | cbz x8,0x00aaafd8 | `CONDITIONAL_JUMP`
<a id="insn-00aaafd0"></a> `00aaafd0` | `c8 0e 00 f9` | str x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aaafd4"></a> `00aaafd4` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00aaafd8"></a> `00aaafd8` | `c0 12 40 f9` | ldr x0,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00aaafdc"></a> `00aaafdc` | `22 b8 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aaafe0"></a> `00aaafe0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aaafe4"></a> `00aaafe4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aaafe8"></a> `00aaafe8` | `c8 16 00 f9` | str x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aaafec"></a> `00aaafec` | `89 a2 42 a9` | ldp x9,x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00aaaff0"></a> `00aaaff0` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aaaff4"></a> `00aaaff4` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00aaaff8"></a> `00aaaff8` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00aaaffc"></a> `00aaaffc` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00aab000"></a> `00aab000` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aab004"></a> `00aab004` | `1f 25 00 f1` | cmp x8,#0x9 | `FALL_THROUGH`
<a id="insn-00aab008"></a> `00aab008` | `c9 01 00 54` | b.ls 0x00aab040 | `CONDITIONAL_JUMP`
<a id="insn-00aab00c"></a> `00aab00c` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aab010"></a> `00aab010` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aab014"></a> `00aab014` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab018"></a> `00aab018` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab01c"></a> `00aab01c` | `01 1d 00 54` | b.ne 0x00aab3bc | `CONDITIONAL_JUMP`
<a id="insn-00aab020"></a> `00aab020` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aab024"></a> `00aab024` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aab028"></a> `00aab028` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aab02c"></a> `00aab02c` | `fa 67 47 a9` | ldp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aab030"></a> `00aab030` | `fc 6f 46 a9` | ldp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aab034"></a> `00aab034` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aab038"></a> `00aab038` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00aab03c"></a> `00aab03c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aab040"></a> `00aab040` | `f6 53 41 a9` | ldp x22,x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aab044"></a> `00aab044` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab048"></a> `00aab048` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00aab04c"></a> `00aab04c` | `a8 00 00 b5` | cbnz x8,0x00aab060 | `CONDITIONAL_JUMP`
<a id="insn-00aab050"></a> `00aab050` | `0d 00 00 14` | b 0x00aab084 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab054"></a> `00aab054` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab058"></a> `00aab058` | `f3 03 14 aa` | mov x19,x20 | `FALL_THROUGH`
<a id="insn-00aab05c"></a> `00aab05c` | `48 01 00 b4` | cbz x8,0x00aab084 | `CONDITIONAL_JUMP`
<a id="insn-00aab060"></a> `00aab060` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aab064"></a> `00aab064` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aab068"></a> `00aab068` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00aab06c"></a> `00aab06c` | `4b ff ff 54` | b.lt 0x00aab054 | `CONDITIONAL_JUMP`
<a id="insn-00aab070"></a> `00aab070` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00aab074"></a> `00aab074` | `2a 03 00 54` | b.ge 0x00aab0d8 | `CONDITIONAL_JUMP`
<a id="insn-00aab078"></a> `00aab078` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aab07c"></a> `00aab07c` | `28 ff ff b5` | cbnz x8,0x00aab060 | `CONDITIONAL_JUMP`
<a id="insn-00aab080"></a> `00aab080` | `93 22 00 91` | add x19,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aab084"></a> `00aab084` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aab088"></a> `00aab088` | `f5 03 14 aa` | mov x21,x20 | `FALL_THROUGH`
<a id="insn-00aab08c"></a> `00aab08c` | `ad bf 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00aab090"></a> `00aab090` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aab094"></a> `00aab094` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aab098"></a> `00aab098` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aab09c"></a> `00aab09c` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aab0a0"></a> `00aab0a0` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aab0a4"></a> `00aab0a4` | `15 08 00 f9` | str x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aab0a8"></a> `00aab0a8` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00aab0ac"></a> `00aab0ac` | `c8 0e 40 f9` | ldr x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aab0b0"></a> `00aab0b0` | `19 20 00 b9` | str w25,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aab0b4"></a> `00aab0b4` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aab0b8"></a> `00aab0b8` | `68 00 00 b4` | cbz x8,0x00aab0c4 | `CONDITIONAL_JUMP`
<a id="insn-00aab0bc"></a> `00aab0bc` | `c8 0e 00 f9` | str x8,[x22, #0x18] | `FALL_THROUGH`
<a id="insn-00aab0c0"></a> `00aab0c0` | `61 02 40 f9` | ldr x1,[x19] | `FALL_THROUGH`
<a id="insn-00aab0c4"></a> `00aab0c4` | `c0 12 40 f9` | ldr x0,[x22, #0x20] | `FALL_THROUGH`
<a id="insn-00aab0c8"></a> `00aab0c8` | `e7 b7 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aab0cc"></a> `00aab0cc` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aab0d0"></a> `00aab0d0` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab0d4"></a> `00aab0d4` | `c8 16 00 f9` | str x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00aab0d8"></a> `00aab0d8` | `88 26 43 a9` | ldp x8,x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab0dc"></a> `00aab0dc` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aab0e0"></a> `00aab0e0` | `bf 03 1f f8` | stur xzr,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab0e4"></a> `00aab0e4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab0e8"></a> `00aab0e8` | `e2 00 00 54` | b.cs 0x00aab104 | `CONDITIONAL_JUMP`
<a id="insn-00aab0ec"></a> `00aab0ec` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00aab0f0"></a> `00aab0f0` | `0a 61 00 91` | add x10,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00aab0f4"></a> `00aab0f4` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab0f8"></a> `00aab0f8` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aab0fc"></a> `00aab0fc` | `8a 1a 00 f9` | str x10,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab100"></a> `00aab100` | `0a 00 00 14` | b 0x00aab128 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab104"></a> `00aab104` | `80 a2 00 91` | add x0,x20,#0x28 | `FALL_THROUGH`
<a id="insn-00aab108"></a> `00aab108` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00aab10c"></a> `00aab10c` | `60 06 00 94` | bl 0x00aaca8c | `UNCONDITIONAL_CALL`
<a id="insn-00aab110"></a> `00aab110` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00aab114"></a> `00aab114` | `a0 03 5e f8` | ldur x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aab118"></a> `00aab118` | `88 1a 00 f9` | str x8,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab11c"></a> `00aab11c` | `60 00 00 b4` | cbz x0,0x00aab128 | `CONDITIONAL_JUMP`
<a id="insn-00aab120"></a> `00aab120` | `a0 83 1e f8` | stur x0,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aab124"></a> `00aab124` | `8f bf 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aab128"></a> `00aab128` | `fa 03 1f aa` | mov x26,xzr | `FALL_THROUGH`
<a id="insn-00aab12c"></a> `00aab12c` | `95 e8 98 52` | mov w21,#0xc744 | `FALL_THROUGH`
<a id="insn-00aab130"></a> `00aab130` | `08 00 00 14` | b 0x00aab150 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab134"></a> `00aab134` | `68 82 1b aa` | orr x8,x19,x27, LSL #0x20 | `FALL_THROUGH`
<a id="insn-00aab138"></a> `00aab138` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00aab13c"></a> `00aab13c` | `5a 07 00 91` | add x26,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00aab140"></a> `00aab140` | `95 e8 98 52` | mov w21,#0xc744 | `FALL_THROUGH`
<a id="insn-00aab144"></a> `00aab144` | `f8 02 1f f8` | stur x24,[x23, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab148"></a> `00aab148` | `5f 2b 00 f1` | cmp x26,#0xa | `FALL_THROUGH`
<a id="insn-00aab14c"></a> `00aab14c` | `00 f6 ff 54` | b.eq 0x00aab00c | `CONDITIONAL_JUMP`
<a id="insn-00aab150"></a> `00aab150` | `0c d1 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aab154"></a> `00aab154` | `53 f7 7e d3` | lsl x19,x26,#0x2 | `FALL_THROUGH`
<a id="insn-00aab158"></a> `00aab158` | `08 00 15 8b` | add x8,x0,x21 | `FALL_THROUGH`
<a id="insn-00aab15c"></a> `00aab15c` | `09 30 40 91` | add x9,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aab160"></a> `00aab160` | `2b b9 5d 39` | ldrb w11,[x9, #0x76e] | `FALL_THROUGH`
<a id="insn-00aab164"></a> `00aab164` | `2c bd 5d 39` | ldrb w12,[x9, #0x76f] | `FALL_THROUGH`
<a id="insn-00aab168"></a> `00aab168` | `08 01 13 8b` | add x8,x8,x19 | `FALL_THROUGH`
<a id="insn-00aab16c"></a> `00aab16c` | `0a 09 40 39` | ldrb w10,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00aab170"></a> `00aab170` | `0d 05 40 39` | ldrb w13,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00aab174"></a> `00aab174` | `6a 01 0a 4a` | eor w10,w11,w10 | `FALL_THROUGH`
<a id="insn-00aab178"></a> `00aab178` | `0b 0d 40 39` | ldrb w11,[x8, #0x3] | `FALL_THROUGH`
<a id="insn-00aab17c"></a> `00aab17c` | `08 01 40 39` | ldrb w8,[x8] | `FALL_THROUGH`
<a id="insn-00aab180"></a> `00aab180` | `4a 3d 10 53` | lsl w10,w10,#0x10 | `FALL_THROUGH`
<a id="insn-00aab184"></a> `00aab184` | `8b 01 0b 4a` | eor w11,w12,w11 | `FALL_THROUGH`
<a id="insn-00aab188"></a> `00aab188` | `2c b5 5d 39` | ldrb w12,[x9, #0x76d] | `FALL_THROUGH`
<a id="insn-00aab18c"></a> `00aab18c` | `29 b1 5d 39` | ldrb w9,[x9, #0x76c] | `FALL_THROUGH`
<a id="insn-00aab190"></a> `00aab190` | `4a 61 0b 2a` | orr w10,w10,w11, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aab194"></a> `00aab194` | `8b 01 0d 4a` | eor w11,w12,w13 | `FALL_THROUGH`
<a id="insn-00aab198"></a> `00aab198` | `28 01 08 4a` | eor w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00aab19c"></a> `00aab19c` | `4a 21 0b 2a` | orr w10,w10,w11, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aab1a0"></a> `00aab1a0` | `48 01 08 2a` | orr w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00aab1a4"></a> `00aab1a4` | `1f 05 00 31` | cmn w8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab1a8"></a> `00aab1a8` | `20 f3 ff 54` | b.eq 0x00aab00c | `CONDITIONAL_JUMP`
<a id="insn-00aab1ac"></a> `00aab1ac` | `f5 d0 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aab1b0"></a> `00aab1b0` | `f4 0f 40 f9` | ldr x20,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aab1b4"></a> `00aab1b4` | `0a 00 15 8b` | add x10,x0,x21 | `FALL_THROUGH`
<a id="insn-00aab1b8"></a> `00aab1b8` | `09 30 40 91` | add x9,x0,#0xc, LSL #12 | `FALL_THROUGH`
<a id="insn-00aab1bc"></a> `00aab1bc` | `4a 01 13 8b` | add x10,x10,x19 | `FALL_THROUGH`
<a id="insn-00aab1c0"></a> `00aab1c0` | `38 b1 5d 39` | ldrb w24,[x9, #0x76c] | `FALL_THROUGH`
<a id="insn-00aab1c4"></a> `00aab1c4` | `33 b5 5d 39` | ldrb w19,[x9, #0x76d] | `FALL_THROUGH`
<a id="insn-00aab1c8"></a> `00aab1c8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab1cc"></a> `00aab1cc` | `50 01 40 39` | ldrb w16,[x10] | `FALL_THROUGH`
<a id="insn-00aab1d0"></a> `00aab1d0` | `51 05 40 39` | ldrb w17,[x10, #0x1] | `FALL_THROUGH`
<a id="insn-00aab1d4"></a> `00aab1d4` | `5b 09 40 39` | ldrb w27,[x10, #0x2] | `FALL_THROUGH`
<a id="insn-00aab1d8"></a> `00aab1d8` | `35 b9 5d 39` | ldrb w21,[x9, #0x76e] | `FALL_THROUGH`
<a id="insn-00aab1dc"></a> `00aab1dc` | `5c 0d 40 39` | ldrb w28,[x10, #0x3] | `FALL_THROUGH`
<a id="insn-00aab1e0"></a> `00aab1e0` | `2f bd 5d 39` | ldrb w15,[x9, #0x76f] | `FALL_THROUGH`
<a id="insn-00aab1e4"></a> `00aab1e4` | `02 00 00 14` | b 0x00aab1ec | `UNCONDITIONAL_JUMP`
<a id="insn-00aab1e8"></a> `00aab1e8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00aab1ec"></a> `00aab1ec` | `f6 03 14 aa` | mov x22,x20 | `FALL_THROUGH`
<a id="insn-00aab1f0"></a> `00aab1f0` | `48 01 00 b4` | cbz x8,0x00aab218 | `CONDITIONAL_JUMP`
<a id="insn-00aab1f4"></a> `00aab1f4` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00aab1f8"></a> `00aab1f8` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aab1fc"></a> `00aab1fc` | `3f 03 08 6b` | cmp w25,w8 | `FALL_THROUGH`
<a id="insn-00aab200"></a> `00aab200` | `4b ff ff 54` | b.lt 0x00aab1e8 | `CONDITIONAL_JUMP`
<a id="insn-00aab204"></a> `00aab204` | `1f 01 19 6b` | cmp w8,w25 | `FALL_THROUGH`
<a id="insn-00aab208"></a> `00aab208` | `ca 03 00 54` | b.ge 0x00aab280 | `CONDITIONAL_JUMP`
<a id="insn-00aab20c"></a> `00aab20c` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aab210"></a> `00aab210` | `28 ff ff b5` | cbnz x8,0x00aab1f4 | `CONDITIONAL_JUMP`
<a id="insn-00aab214"></a> `00aab214` | `96 22 00 91` | add x22,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aab218"></a> `00aab218` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aab21c"></a> `00aab21c` | `f1 c3 04 29` | stp w17,w16,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aab220"></a> `00aab220` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-00aab224"></a> `00aab224` | `af c3 1d b8` | stur w15,[x29, #-0x24] | `FALL_THROUGH`
<a id="insn-00aab228"></a> `00aab228` | `46 bf 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00aab22c"></a> `00aab22c` | `17 08 00 f9` | str x23,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aab230"></a> `00aab230` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aab234"></a> `00aab234` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aab238"></a> `00aab238` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aab23c"></a> `00aab23c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aab240"></a> `00aab240` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aab244"></a> `00aab244` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aab248"></a> `00aab248` | `c0 02 00 f9` | str x0,[x22] | `FALL_THROUGH`
<a id="insn-00aab24c"></a> `00aab24c` | `e8 0e 40 f9` | ldr x8,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00aab250"></a> `00aab250` | `19 20 00 b9` | str w25,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aab254"></a> `00aab254` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aab258"></a> `00aab258` | `68 00 00 b4` | cbz x8,0x00aab264 | `CONDITIONAL_JUMP`
<a id="insn-00aab25c"></a> `00aab25c` | `e8 0e 00 f9` | str x8,[x23, #0x18] | `FALL_THROUGH`
<a id="insn-00aab260"></a> `00aab260` | `c1 02 40 f9` | ldr x1,[x22] | `FALL_THROUGH`
<a id="insn-00aab264"></a> `00aab264` | `e0 12 40 f9` | ldr x0,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00aab268"></a> `00aab268` | `7f b7 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aab26c"></a> `00aab26c` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aab270"></a> `00aab270` | `af c3 5d b8` | ldur w15,[x29, #-0x24] | `FALL_THROUGH`
<a id="insn-00aab274"></a> `00aab274` | `f1 c3 44 29` | ldp w17,w16,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00aab278"></a> `00aab278` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aab27c"></a> `00aab27c` | `e8 16 00 f9` | str x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aab280"></a> `00aab280` | `08 03 10 4a` | eor w8,w24,w16 | `FALL_THROUGH`
<a id="insn-00aab284"></a> `00aab284` | `69 02 11 4a` | eor w9,w19,w17 | `FALL_THROUGH`
<a id="insn-00aab288"></a> `00aab288` | `97 1a 40 f9` | ldr x23,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00aab28c"></a> `00aab28c` | `08 21 09 2a` | orr w8,w8,w9, LSL #0x8 | `FALL_THROUGH`
<a id="insn-00aab290"></a> `00aab290` | `a9 02 1b 4a` | eor w9,w21,w27 | `FALL_THROUGH`
<a id="insn-00aab294"></a> `00aab294` | `08 41 09 2a` | orr w8,w8,w9, LSL #0x10 | `FALL_THROUGH`
<a id="insn-00aab298"></a> `00aab298` | `e9 01 1c 4a` | eor w9,w15,w28 | `FALL_THROUGH`
<a id="insn-00aab29c"></a> `00aab29c` | `08 61 09 2a` | orr w8,w8,w9, LSL #0x18 | `FALL_THROUGH`
<a id="insn-00aab2a0"></a> `00aab2a0` | `13 09 00 51` | sub w19,w8,#0x2 | `FALL_THROUGH`
<a id="insn-00aab2a4"></a> `00aab2a4` | `b7 d0 f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aab2a8"></a> `00aab2a8` | `f8 22 7f a9` | ldp x24,x8,[x23, #-0x10] | `FALL_THROUGH`
<a id="insn-00aab2ac"></a> `00aab2ac` | `09 c8 33 8b` | add x9,x0,w19, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-00aab2b0"></a> `00aab2b0` | `8a e6 92 52` | mov w10,#0x9734 | `FALL_THROUGH`
<a id="insn-00aab2b4"></a> `00aab2b4` | `8a 00 a0 72` | movk w10,#0x4, LSL #16 | `FALL_THROUGH`
<a id="insn-00aab2b8"></a> `00aab2b8` | `3b 69 6a b8` | ldr w27,[x9, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00aab2bc"></a> `00aab2bc` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00aab2c0"></a> `00aab2c0` | `a3 f3 ff 54` | b.cc 0x00aab134 | `CONDITIONAL_JUMP`
<a id="insn-00aab2c4"></a> `00aab2c4` | `e0 62 00 d1` | sub x0,x23,#0x18 | `FALL_THROUGH`
<a id="insn-00aab2c8"></a> `00aab2c8` | `14 00 40 f9` | ldr x20,[x0] | `FALL_THROUGH`
<a id="insn-00aab2cc"></a> `00aab2cc` | `15 03 14 cb` | sub x21,x24,x20 | `FALL_THROUGH`
<a id="insn-00aab2d0"></a> `00aab2d0` | `b8 fe 43 93` | asr x24,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00aab2d4"></a> `00aab2d4` | `09 07 00 91` | add x9,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00aab2d8"></a> `00aab2d8` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-00aab2dc"></a> `00aab2dc` | `ea 03 00 b5` | cbnz x10,0x00aab358 | `CONDITIONAL_JUMP`
<a id="insn-00aab2e0"></a> `00aab2e0` | `08 01 14 cb` | sub x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00aab2e4"></a> `00aab2e4` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00aab2e8"></a> `00aab2e8` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00aab2ec"></a> `00aab2ec` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00aab2f0"></a> `00aab2f0` | `ea ef 7d b2` | orr x10,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00aab2f4"></a> `00aab2f4` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00aab2f8"></a> `00aab2f8` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00aab2fc"></a> `00aab2fc` | `3c 31 88 9a` | csel x28,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00aab300"></a> `00aab300` | `fc 00 00 b4` | cbz x28,0x00aab31c | `CONDITIONAL_JUMP`
<a id="insn-00aab304"></a> `00aab304` | `88 ff 7d d3` | lsr x8,x28,#0x3d | `FALL_THROUGH`
<a id="insn-00aab308"></a> `00aab308` | `48 03 00 b5` | cbnz x8,0x00aab370 | `CONDITIONAL_JUMP`
<a id="insn-00aab30c"></a> `00aab30c` | `80 f3 7d d3` | lsl x0,x28,#0x3 | `FALL_THROUGH`
<a id="insn-00aab310"></a> `00aab310` | `0c bf 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00aab314"></a> `00aab314` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00aab318"></a> `00aab318` | `02 00 00 14` | b 0x00aab320 | `UNCONDITIONAL_JUMP`
<a id="insn-00aab31c"></a> `00aab31c` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00aab320"></a> `00aab320` | `d8 0e 18 8b` | add x24,x22,x24, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aab324"></a> `00aab324` | `68 82 1b aa` | orr x8,x19,x27, LSL #0x20 | `FALL_THROUGH`
<a id="insn-00aab328"></a> `00aab328` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aab32c"></a> `00aab32c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00aab330"></a> `00aab330` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00aab334"></a> `00aab334` | `d3 0e 1c 8b` | add x19,x22,x28, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00aab338"></a> `00aab338` | `08 87 00 f8` | str x8,[x24], #0x8 | `FALL_THROUGH`
<a id="insn-00aab33c"></a> `00aab33c` | `5d bf 04 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00aab340"></a> `00aab340` | `f6 e2 3e a9` | stp x22,x24,[x23, #-0x18] | `FALL_THROUGH`
<a id="insn-00aab344"></a> `00aab344` | `f3 82 1f f8` | stur x19,[x23, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab348"></a> `00aab348` | `b4 ef ff b4` | cbz x20,0x00aab13c | `CONDITIONAL_JUMP`
<a id="insn-00aab34c"></a> `00aab34c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aab350"></a> `00aab350` | `04 bf 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aab354"></a> `00aab354` | `7a ff ff 17` | b 0x00aab13c | `UNCONDITIONAL_JUMP`
<a id="insn-00aab358"></a> `00aab358` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aab35c"></a> `00aab35c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aab360"></a> `00aab360` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab364"></a> `00aab364` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab368"></a> `00aab368` | `a1 02 00 54` | b.ne 0x00aab3bc | `CONDITIONAL_JUMP`
<a id="insn-00aab36c"></a> `00aab36c` | `c3 05 00 94` | bl 0x00aaca78 | `UNCONDITIONAL_CALL`
<a id="insn-00aab370"></a> `00aab370` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aab374"></a> `00aab374` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aab378"></a> `00aab378` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aab37c"></a> `00aab37c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aab380"></a> `00aab380` | `e1 01 00 54` | b.ne 0x00aab3bc | `CONDITIONAL_JUMP`
<a id="insn-00aab384"></a> `00aab384` | `ff cb e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-00aab3bc"></a> `00aab3bc` | `f5 be 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaaedc`](#insn-00aaaedc) 範囲 `[['00aaaedc', '00aaaf1f']]`
  - `CONDITIONAL_JUMP` [`00aaaf1c`](#insn-00aaaf1c) → [`00aaaf3c`](#insn-00aaaf3c)
  - `FALL_THROUGH` [`00aaaf1c`](#insn-00aaaf1c) → [`00aaaf20`](#insn-00aaaf20)
- ブロック [`00aaaf20`](#insn-00aaaf20) 範囲 `[['00aaaf20', '00aaaf3b']]`
  - `FALL_THROUGH` [`00aaaf38`](#insn-00aaaf38) → [`00aaaf3c`](#insn-00aaaf3c)
- ブロック [`00aaaf3c`](#insn-00aaaf3c) 範囲 `[['00aaaf3c', '00aaaf63']]`
  - `CONDITIONAL_JUMP` [`00aaaf60`](#insn-00aaaf60) → [`00aaaf74`](#insn-00aaaf74)
  - `FALL_THROUGH` [`00aaaf60`](#insn-00aaaf60) → [`00aaaf64`](#insn-00aaaf64)
- ブロック [`00aaaf64`](#insn-00aaaf64) 範囲 `[['00aaaf64', '00aaaf67']]`
  - `UNCONDITIONAL_JUMP` [`00aaaf64`](#insn-00aaaf64) → [`00aaaf98`](#insn-00aaaf98)
- ブロック [`00aaaf68`](#insn-00aaaf68) 範囲 `[['00aaaf68', '00aaaf73']]`
  - `CONDITIONAL_JUMP` [`00aaaf70`](#insn-00aaaf70) → [`00aaaf98`](#insn-00aaaf98)
  - `FALL_THROUGH` [`00aaaf70`](#insn-00aaaf70) → [`00aaaf74`](#insn-00aaaf74)
- ブロック [`00aaaf74`](#insn-00aaaf74) 範囲 `[['00aaaf74', '00aaaf83']]`
  - `CONDITIONAL_JUMP` [`00aaaf80`](#insn-00aaaf80) → [`00aaaf68`](#insn-00aaaf68)
  - `FALL_THROUGH` [`00aaaf80`](#insn-00aaaf80) → [`00aaaf84`](#insn-00aaaf84)
- ブロック [`00aaaf84`](#insn-00aaaf84) 範囲 `[['00aaaf84', '00aaaf8b']]`
  - `CONDITIONAL_JUMP` [`00aaaf88`](#insn-00aaaf88) → [`00aaafec`](#insn-00aaafec)
  - `FALL_THROUGH` [`00aaaf88`](#insn-00aaaf88) → [`00aaaf8c`](#insn-00aaaf8c)
- ブロック [`00aaaf8c`](#insn-00aaaf8c) 範囲 `[['00aaaf8c', '00aaaf93']]`
  - `CONDITIONAL_JUMP` [`00aaaf90`](#insn-00aaaf90) → [`00aaaf74`](#insn-00aaaf74)
  - `FALL_THROUGH` [`00aaaf90`](#insn-00aaaf90) → [`00aaaf94`](#insn-00aaaf94)
- ブロック [`00aaaf94`](#insn-00aaaf94) 範囲 `[['00aaaf94', '00aaaf97']]`
  - `FALL_THROUGH` [`00aaaf94`](#insn-00aaaf94) → [`00aaaf98`](#insn-00aaaf98)
- ブロック [`00aaaf98`](#insn-00aaaf98) 範囲 `[['00aaaf98', '00aaafcf']]`
  - `CONDITIONAL_JUMP` [`00aaafcc`](#insn-00aaafcc) → [`00aaafd8`](#insn-00aaafd8)
  - `FALL_THROUGH` [`00aaafcc`](#insn-00aaafcc) → [`00aaafd0`](#insn-00aaafd0)
- ブロック [`00aaafd0`](#insn-00aaafd0) 範囲 `[['00aaafd0', '00aaafd7']]`
  - `FALL_THROUGH` [`00aaafd4`](#insn-00aaafd4) → [`00aaafd8`](#insn-00aaafd8)
- ブロック [`00aaafd8`](#insn-00aaafd8) 範囲 `[['00aaafd8', '00aaafeb']]`
  - `FALL_THROUGH` [`00aaafe8`](#insn-00aaafe8) → [`00aaafec`](#insn-00aaafec)
- ブロック [`00aaafec`](#insn-00aaafec) 範囲 `[['00aaafec', '00aab00b']]`
  - `CONDITIONAL_JUMP` [`00aab008`](#insn-00aab008) → [`00aab040`](#insn-00aab040)
  - `FALL_THROUGH` [`00aab008`](#insn-00aab008) → [`00aab00c`](#insn-00aab00c)
- ブロック [`00aab00c`](#insn-00aab00c) 範囲 `[['00aab00c', '00aab01f']]`
  - `CONDITIONAL_JUMP` [`00aab01c`](#insn-00aab01c) → [`00aab3bc`](#insn-00aab3bc)
  - `FALL_THROUGH` [`00aab01c`](#insn-00aab01c) → [`00aab020`](#insn-00aab020)
- ブロック [`00aab020`](#insn-00aab020) 範囲 `[['00aab020', '00aab03f']]`
- ブロック [`00aab040`](#insn-00aab040) 範囲 `[['00aab040', '00aab04f']]`
  - `CONDITIONAL_JUMP` [`00aab04c`](#insn-00aab04c) → [`00aab060`](#insn-00aab060)
  - `FALL_THROUGH` [`00aab04c`](#insn-00aab04c) → [`00aab050`](#insn-00aab050)
- ブロック [`00aab050`](#insn-00aab050) 範囲 `[['00aab050', '00aab053']]`
  - `UNCONDITIONAL_JUMP` [`00aab050`](#insn-00aab050) → [`00aab084`](#insn-00aab084)
- ブロック [`00aab054`](#insn-00aab054) 範囲 `[['00aab054', '00aab05f']]`
  - `CONDITIONAL_JUMP` [`00aab05c`](#insn-00aab05c) → [`00aab084`](#insn-00aab084)
  - `FALL_THROUGH` [`00aab05c`](#insn-00aab05c) → [`00aab060`](#insn-00aab060)
- ブロック [`00aab060`](#insn-00aab060) 範囲 `[['00aab060', '00aab06f']]`
  - `CONDITIONAL_JUMP` [`00aab06c`](#insn-00aab06c) → [`00aab054`](#insn-00aab054)
  - `FALL_THROUGH` [`00aab06c`](#insn-00aab06c) → [`00aab070`](#insn-00aab070)
- ブロック [`00aab070`](#insn-00aab070) 範囲 `[['00aab070', '00aab077']]`
  - `CONDITIONAL_JUMP` [`00aab074`](#insn-00aab074) → [`00aab0d8`](#insn-00aab0d8)
  - `FALL_THROUGH` [`00aab074`](#insn-00aab074) → [`00aab078`](#insn-00aab078)
- ブロック [`00aab078`](#insn-00aab078) 範囲 `[['00aab078', '00aab07f']]`
  - `CONDITIONAL_JUMP` [`00aab07c`](#insn-00aab07c) → [`00aab060`](#insn-00aab060)
  - `FALL_THROUGH` [`00aab07c`](#insn-00aab07c) → [`00aab080`](#insn-00aab080)
- ブロック [`00aab080`](#insn-00aab080) 範囲 `[['00aab080', '00aab083']]`
  - `FALL_THROUGH` [`00aab080`](#insn-00aab080) → [`00aab084`](#insn-00aab084)
- ブロック [`00aab084`](#insn-00aab084) 範囲 `[['00aab084', '00aab0bb']]`
  - `CONDITIONAL_JUMP` [`00aab0b8`](#insn-00aab0b8) → [`00aab0c4`](#insn-00aab0c4)
  - `FALL_THROUGH` [`00aab0b8`](#insn-00aab0b8) → [`00aab0bc`](#insn-00aab0bc)
- ブロック [`00aab0bc`](#insn-00aab0bc) 範囲 `[['00aab0bc', '00aab0c3']]`
  - `FALL_THROUGH` [`00aab0c0`](#insn-00aab0c0) → [`00aab0c4`](#insn-00aab0c4)
- ブロック [`00aab0c4`](#insn-00aab0c4) 範囲 `[['00aab0c4', '00aab0d7']]`
  - `FALL_THROUGH` [`00aab0d4`](#insn-00aab0d4) → [`00aab0d8`](#insn-00aab0d8)
- ブロック [`00aab0d8`](#insn-00aab0d8) 範囲 `[['00aab0d8', '00aab0eb']]`
  - `CONDITIONAL_JUMP` [`00aab0e8`](#insn-00aab0e8) → [`00aab104`](#insn-00aab104)
  - `FALL_THROUGH` [`00aab0e8`](#insn-00aab0e8) → [`00aab0ec`](#insn-00aab0ec)
- ブロック [`00aab0ec`](#insn-00aab0ec) 範囲 `[['00aab0ec', '00aab103']]`
  - `UNCONDITIONAL_JUMP` [`00aab100`](#insn-00aab100) → [`00aab128`](#insn-00aab128)
- ブロック [`00aab104`](#insn-00aab104) 範囲 `[['00aab104', '00aab11f']]`
  - `CONDITIONAL_JUMP` [`00aab11c`](#insn-00aab11c) → [`00aab128`](#insn-00aab128)
  - `FALL_THROUGH` [`00aab11c`](#insn-00aab11c) → [`00aab120`](#insn-00aab120)
- ブロック [`00aab120`](#insn-00aab120) 範囲 `[['00aab120', '00aab127']]`
  - `FALL_THROUGH` [`00aab124`](#insn-00aab124) → [`00aab128`](#insn-00aab128)
- ブロック [`00aab128`](#insn-00aab128) 範囲 `[['00aab128', '00aab133']]`
  - `UNCONDITIONAL_JUMP` [`00aab130`](#insn-00aab130) → [`00aab150`](#insn-00aab150)
- ブロック [`00aab134`](#insn-00aab134) 範囲 `[['00aab134', '00aab13b']]`
  - `FALL_THROUGH` [`00aab138`](#insn-00aab138) → [`00aab13c`](#insn-00aab13c)
- ブロック [`00aab13c`](#insn-00aab13c) 範囲 `[['00aab13c', '00aab14f']]`
  - `CONDITIONAL_JUMP` [`00aab14c`](#insn-00aab14c) → [`00aab00c`](#insn-00aab00c)
  - `FALL_THROUGH` [`00aab14c`](#insn-00aab14c) → [`00aab150`](#insn-00aab150)
- ブロック [`00aab150`](#insn-00aab150) 範囲 `[['00aab150', '00aab1ab']]`
  - `CONDITIONAL_JUMP` [`00aab1a8`](#insn-00aab1a8) → [`00aab00c`](#insn-00aab00c)
  - `FALL_THROUGH` [`00aab1a8`](#insn-00aab1a8) → [`00aab1ac`](#insn-00aab1ac)
- ブロック [`00aab1ac`](#insn-00aab1ac) 範囲 `[['00aab1ac', '00aab1e7']]`
  - `UNCONDITIONAL_JUMP` [`00aab1e4`](#insn-00aab1e4) → [`00aab1ec`](#insn-00aab1ec)
- ブロック [`00aab1e8`](#insn-00aab1e8) 範囲 `[['00aab1e8', '00aab1eb']]`
  - `FALL_THROUGH` [`00aab1e8`](#insn-00aab1e8) → [`00aab1ec`](#insn-00aab1ec)
- ブロック [`00aab1ec`](#insn-00aab1ec) 範囲 `[['00aab1ec', '00aab1f3']]`
  - `CONDITIONAL_JUMP` [`00aab1f0`](#insn-00aab1f0) → [`00aab218`](#insn-00aab218)
  - `FALL_THROUGH` [`00aab1f0`](#insn-00aab1f0) → [`00aab1f4`](#insn-00aab1f4)
- ブロック [`00aab1f4`](#insn-00aab1f4) 範囲 `[['00aab1f4', '00aab203']]`
  - `CONDITIONAL_JUMP` [`00aab200`](#insn-00aab200) → [`00aab1e8`](#insn-00aab1e8)
  - `FALL_THROUGH` [`00aab200`](#insn-00aab200) → [`00aab204`](#insn-00aab204)
- ブロック [`00aab204`](#insn-00aab204) 範囲 `[['00aab204', '00aab20b']]`
  - `CONDITIONAL_JUMP` [`00aab208`](#insn-00aab208) → [`00aab280`](#insn-00aab280)
  - `FALL_THROUGH` [`00aab208`](#insn-00aab208) → [`00aab20c`](#insn-00aab20c)
- ブロック [`00aab20c`](#insn-00aab20c) 範囲 `[['00aab20c', '00aab213']]`
  - `CONDITIONAL_JUMP` [`00aab210`](#insn-00aab210) → [`00aab1f4`](#insn-00aab1f4)
  - `FALL_THROUGH` [`00aab210`](#insn-00aab210) → [`00aab214`](#insn-00aab214)
- ブロック [`00aab214`](#insn-00aab214) 範囲 `[['00aab214', '00aab217']]`
  - `FALL_THROUGH` [`00aab214`](#insn-00aab214) → [`00aab218`](#insn-00aab218)
- ブロック [`00aab218`](#insn-00aab218) 範囲 `[['00aab218', '00aab25b']]`
  - `CONDITIONAL_JUMP` [`00aab258`](#insn-00aab258) → [`00aab264`](#insn-00aab264)
  - `FALL_THROUGH` [`00aab258`](#insn-00aab258) → [`00aab25c`](#insn-00aab25c)
- ブロック [`00aab25c`](#insn-00aab25c) 範囲 `[['00aab25c', '00aab263']]`
  - `FALL_THROUGH` [`00aab260`](#insn-00aab260) → [`00aab264`](#insn-00aab264)
- ブロック [`00aab264`](#insn-00aab264) 範囲 `[['00aab264', '00aab27f']]`
  - `FALL_THROUGH` [`00aab27c`](#insn-00aab27c) → [`00aab280`](#insn-00aab280)
- ブロック [`00aab280`](#insn-00aab280) 範囲 `[['00aab280', '00aab2c3']]`
  - `CONDITIONAL_JUMP` [`00aab2c0`](#insn-00aab2c0) → [`00aab134`](#insn-00aab134)
  - `FALL_THROUGH` [`00aab2c0`](#insn-00aab2c0) → [`00aab2c4`](#insn-00aab2c4)
- ブロック [`00aab2c4`](#insn-00aab2c4) 範囲 `[['00aab2c4', '00aab2df']]`
  - `CONDITIONAL_JUMP` [`00aab2dc`](#insn-00aab2dc) → [`00aab358`](#insn-00aab358)
  - `FALL_THROUGH` [`00aab2dc`](#insn-00aab2dc) → [`00aab2e0`](#insn-00aab2e0)
- ブロック [`00aab2e0`](#insn-00aab2e0) 範囲 `[['00aab2e0', '00aab303']]`
  - `CONDITIONAL_JUMP` [`00aab300`](#insn-00aab300) → [`00aab31c`](#insn-00aab31c)
  - `FALL_THROUGH` [`00aab300`](#insn-00aab300) → [`00aab304`](#insn-00aab304)
- ブロック [`00aab304`](#insn-00aab304) 範囲 `[['00aab304', '00aab30b']]`
  - `CONDITIONAL_JUMP` [`00aab308`](#insn-00aab308) → [`00aab370`](#insn-00aab370)
  - `FALL_THROUGH` [`00aab308`](#insn-00aab308) → [`00aab30c`](#insn-00aab30c)
- ブロック [`00aab30c`](#insn-00aab30c) 範囲 `[['00aab30c', '00aab31b']]`
  - `UNCONDITIONAL_JUMP` [`00aab318`](#insn-00aab318) → [`00aab320`](#insn-00aab320)
- ブロック [`00aab31c`](#insn-00aab31c) 範囲 `[['00aab31c', '00aab31f']]`
  - `FALL_THROUGH` [`00aab31c`](#insn-00aab31c) → [`00aab320`](#insn-00aab320)
- ブロック [`00aab320`](#insn-00aab320) 範囲 `[['00aab320', '00aab34b']]`
  - `CONDITIONAL_JUMP` [`00aab348`](#insn-00aab348) → [`00aab13c`](#insn-00aab13c)
  - `FALL_THROUGH` [`00aab348`](#insn-00aab348) → [`00aab34c`](#insn-00aab34c)
- ブロック [`00aab34c`](#insn-00aab34c) 範囲 `[['00aab34c', '00aab357']]`
  - `UNCONDITIONAL_JUMP` [`00aab354`](#insn-00aab354) → [`00aab13c`](#insn-00aab13c)
- ブロック [`00aab358`](#insn-00aab358) 範囲 `[['00aab358', '00aab36b']]`
  - `CONDITIONAL_JUMP` [`00aab368`](#insn-00aab368) → [`00aab3bc`](#insn-00aab3bc)
  - `FALL_THROUGH` [`00aab368`](#insn-00aab368) → [`00aab36c`](#insn-00aab36c)
- ブロック [`00aab36c`](#insn-00aab36c) 範囲 `[['00aab36c', '00aab36f']]`
  - `FALL_THROUGH` [`00aab36c`](#insn-00aab36c) → [`00aab370`](#insn-00aab370)
- ブロック [`00aab370`](#insn-00aab370) 範囲 `[['00aab370', '00aab383']]`
  - `CONDITIONAL_JUMP` [`00aab380`](#insn-00aab380) → [`00aab3bc`](#insn-00aab3bc)
  - `FALL_THROUGH` [`00aab380`](#insn-00aab380) → [`00aab384`](#insn-00aab384)
- ブロック [`00aab384`](#insn-00aab384) 範囲 `[['00aab384', '00aab387']]`
- ブロック [`00aab3bc`](#insn-00aab3bc) 範囲 `[['00aab3bc', '00aab3bf']]`

## 命令位置別の参照

- [`00aaaee0`](#insn-00aaaee0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaee4`](#insn-00aaaee4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaee8`](#insn-00aaaee8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaeec`](#insn-00aaaeec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaef0`](#insn-00aaaef0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaef4`](#insn-00aaaef4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf08`](#insn-00aaaf08) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf18`](#insn-00aaaf18) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf1c`](#insn-00aaaf1c) → [`00aaaf3c`](#insn-00aaaf3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf24`](#insn-00aaaf24) → [`007cf950`](../007cf/007cf950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf950` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf2c`](#insn-00aaaf2c) → [`007cfaa0`](../007cf/007cfaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfaa0` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf34`](#insn-00aaaf34) → [`007cfcd8`](../007cf/007cfcd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfcd8` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf5c`](#insn-00aaaf5c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf60`](#insn-00aaaf60) → [`00aaaf74`](#insn-00aaaf74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf64`](#insn-00aaaf64) → [`00aaaf98`](#insn-00aaaf98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf70`](#insn-00aaaf70) → [`00aaaf98`](#insn-00aaaf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf80`](#insn-00aaaf80) → [`00aaaf68`](#insn-00aaaf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf88`](#insn-00aaaf88) → [`00aaafec`](#insn-00aaafec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaaf90`](#insn-00aaaf90) → [`00aaaf74`](#insn-00aaaf74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafa0`](#insn-00aaafa0) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00aaafcc`](#insn-00aaafcc) → [`00aaafd8`](#insn-00aaafd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaafdc`](#insn-00aaafdc) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aab008`](#insn-00aab008) → [`00aab040`](#insn-00aab040) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab00c`](#insn-00aab00c) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab014`](#insn-00aab014) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab01c`](#insn-00aab01c) → [`00aab3bc`](#insn-00aab3bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab020`](#insn-00aab020) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab024`](#insn-00aab024) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab028`](#insn-00aab028) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab02c`](#insn-00aab02c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab030`](#insn-00aab030) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab034`](#insn-00aab034) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab040`](#insn-00aab040) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab04c`](#insn-00aab04c) → [`00aab060`](#insn-00aab060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab050`](#insn-00aab050) → [`00aab084`](#insn-00aab084) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab05c`](#insn-00aab05c) → [`00aab084`](#insn-00aab084) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab06c`](#insn-00aab06c) → [`00aab054`](#insn-00aab054) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab074`](#insn-00aab074) → [`00aab0d8`](#insn-00aab0d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab07c`](#insn-00aab07c) → [`00aab060`](#insn-00aab060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab08c`](#insn-00aab08c) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00aab0b8`](#insn-00aab0b8) → [`00aab0c4`](#insn-00aab0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0c8`](#insn-00aab0c8) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aab0dc`](#insn-00aab0dc) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0e0`](#insn-00aab0e0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0e8`](#insn-00aab0e8) → [`00aab104`](#insn-00aab104) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab0f4`](#insn-00aab0f4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab100`](#insn-00aab100) → [`00aab128`](#insn-00aab128) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab10c`](#insn-00aab10c) → [`00aaca8c`](../00aac/00aaca8c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aaca8c` · 推定シンボル `None` · 推定型 `None`
- [`00aab114`](#insn-00aab114) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab11c`](#insn-00aab11c) → [`00aab128`](#insn-00aab128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab120`](#insn-00aab120) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab124`](#insn-00aab124) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aab130`](#insn-00aab130) → [`00aab150`](#insn-00aab150) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab14c`](#insn-00aab14c) → [`00aab00c`](#insn-00aab00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab150`](#insn-00aab150) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aab1a8`](#insn-00aab1a8) → [`00aab00c`](#insn-00aab00c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1ac`](#insn-00aab1ac) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aab1b0`](#insn-00aab1b0) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1e4`](#insn-00aab1e4) → [`00aab1ec`](#insn-00aab1ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab1f0`](#insn-00aab1f0) → [`00aab218`](#insn-00aab218) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab200`](#insn-00aab200) → [`00aab1e8`](#insn-00aab1e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab208`](#insn-00aab208) → [`00aab280`](#insn-00aab280) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab210`](#insn-00aab210) → [`00aab1f4`](#insn-00aab1f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab21c`](#insn-00aab21c) → `Stack[-0x8c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab224`](#insn-00aab224) → `Stack[-0x84]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab228`](#insn-00aab228) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00aab230`](#insn-00aab230) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab258`](#insn-00aab258) → [`00aab264`](#insn-00aab264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab268`](#insn-00aab268) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aab270`](#insn-00aab270) → `Stack[-0x84]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab274`](#insn-00aab274) → `Stack[-0x8c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2a4`](#insn-00aab2a4) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aab2c0`](#insn-00aab2c0) → [`00aab134`](#insn-00aab134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab2dc`](#insn-00aab2dc) → [`00aab358`](#insn-00aab358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab300`](#insn-00aab300) → [`00aab31c`](#insn-00aab31c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab308`](#insn-00aab308) → [`00aab370`](#insn-00aab370) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab310`](#insn-00aab310) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00aab318`](#insn-00aab318) → [`00aab320`](#insn-00aab320) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab33c`](#insn-00aab33c) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00aab348`](#insn-00aab348) → [`00aab13c`](#insn-00aab13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab350`](#insn-00aab350) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aab354`](#insn-00aab354) → [`00aab13c`](#insn-00aab13c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab358`](#insn-00aab358) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab360`](#insn-00aab360) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab368`](#insn-00aab368) → [`00aab3bc`](#insn-00aab3bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab36c`](#insn-00aab36c) → [`00aaca78`](../00aac/00aaca78.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aaca78` · 推定シンボル `None` · 推定型 `None`
- [`00aab370`](#insn-00aab370) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab378`](#insn-00aab378) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab380`](#insn-00aab380) → [`00aab3bc`](#insn-00aab3bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aab384`](#insn-00aab384) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`00aab3bc`](#insn-00aab3bc) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaaee0`](#insn-00aaaee0)

~~~json
{
  "source": "00aaaee0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaee4`](#insn-00aaaee4)

~~~json
{
  "source": "00aaaee4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaee8`](#insn-00aaaee8)

~~~json
{
  "source": "00aaaee8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaeec`](#insn-00aaaeec)

~~~json
{
  "source": "00aaaeec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaef0`](#insn-00aaaef0)

~~~json
{
  "source": "00aaaef0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaef4`](#insn-00aaaef4)

~~~json
{
  "source": "00aaaef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf08`](#insn-00aaaf08)

~~~json
{
  "source": "00aaaf08",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf18`](#insn-00aaaf18)

~~~json
{
  "source": "00aaaf18",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf1c`](#insn-00aaaf1c)

~~~json
{
  "source": "00aaaf1c",
  "target": "00aaaf3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf24`](#insn-00aaaf24)

~~~json
{
  "source": "00aaaf24",
  "target": "007cf950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaf2c`](#insn-00aaaf2c)

~~~json
{
  "source": "00aaaf2c",
  "target": "007cfaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaf34`](#insn-00aaaf34)

~~~json
{
  "source": "00aaaf34",
  "target": "007cfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaaf5c`](#insn-00aaaf5c)

~~~json
{
  "source": "00aaaf5c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf60`](#insn-00aaaf60)

~~~json
{
  "source": "00aaaf60",
  "target": "00aaaf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf64`](#insn-00aaaf64)

~~~json
{
  "source": "00aaaf64",
  "target": "00aaaf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf70`](#insn-00aaaf70)

~~~json
{
  "source": "00aaaf70",
  "target": "00aaaf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf80`](#insn-00aaaf80)

~~~json
{
  "source": "00aaaf80",
  "target": "00aaaf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf88`](#insn-00aaaf88)

~~~json
{
  "source": "00aaaf88",
  "target": "00aaafec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaaf90`](#insn-00aaaf90)

~~~json
{
  "source": "00aaaf90",
  "target": "00aaaf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafa0`](#insn-00aaafa0)

~~~json
{
  "source": "00aaafa0",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaafcc`](#insn-00aaafcc)

~~~json
{
  "source": "00aaafcc",
  "target": "00aaafd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaafdc`](#insn-00aaafdc)

~~~json
{
  "source": "00aaafdc",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab008`](#insn-00aab008)

~~~json
{
  "source": "00aab008",
  "target": "00aab040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab00c`](#insn-00aab00c)

~~~json
{
  "source": "00aab00c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab014`](#insn-00aab014)

~~~json
{
  "source": "00aab014",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab01c`](#insn-00aab01c)

~~~json
{
  "source": "00aab01c",
  "target": "00aab3bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab020`](#insn-00aab020)

~~~json
{
  "source": "00aab020",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab024`](#insn-00aab024)

~~~json
{
  "source": "00aab024",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab028`](#insn-00aab028)

~~~json
{
  "source": "00aab028",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab02c`](#insn-00aab02c)

~~~json
{
  "source": "00aab02c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab030`](#insn-00aab030)

~~~json
{
  "source": "00aab030",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab034`](#insn-00aab034)

~~~json
{
  "source": "00aab034",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab040`](#insn-00aab040)

~~~json
{
  "source": "00aab040",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab04c`](#insn-00aab04c)

~~~json
{
  "source": "00aab04c",
  "target": "00aab060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab050`](#insn-00aab050)

~~~json
{
  "source": "00aab050",
  "target": "00aab084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab05c`](#insn-00aab05c)

~~~json
{
  "source": "00aab05c",
  "target": "00aab084",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab06c`](#insn-00aab06c)

~~~json
{
  "source": "00aab06c",
  "target": "00aab054",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab074`](#insn-00aab074)

~~~json
{
  "source": "00aab074",
  "target": "00aab0d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab07c`](#insn-00aab07c)

~~~json
{
  "source": "00aab07c",
  "target": "00aab060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab08c`](#insn-00aab08c)

~~~json
{
  "source": "00aab08c",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab0b8`](#insn-00aab0b8)

~~~json
{
  "source": "00aab0b8",
  "target": "00aab0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0c8`](#insn-00aab0c8)

~~~json
{
  "source": "00aab0c8",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab0dc`](#insn-00aab0dc)

~~~json
{
  "source": "00aab0dc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0e0`](#insn-00aab0e0)

~~~json
{
  "source": "00aab0e0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0e8`](#insn-00aab0e8)

~~~json
{
  "source": "00aab0e8",
  "target": "00aab104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab0f4`](#insn-00aab0f4)

~~~json
{
  "source": "00aab0f4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab100`](#insn-00aab100)

~~~json
{
  "source": "00aab100",
  "target": "00aab128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab10c`](#insn-00aab10c)

~~~json
{
  "source": "00aab10c",
  "target": "00aaca8c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab114`](#insn-00aab114)

~~~json
{
  "source": "00aab114",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab11c`](#insn-00aab11c)

~~~json
{
  "source": "00aab11c",
  "target": "00aab128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab120`](#insn-00aab120)

~~~json
{
  "source": "00aab120",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab124`](#insn-00aab124)

~~~json
{
  "source": "00aab124",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab130`](#insn-00aab130)

~~~json
{
  "source": "00aab130",
  "target": "00aab150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab14c`](#insn-00aab14c)

~~~json
{
  "source": "00aab14c",
  "target": "00aab00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab150`](#insn-00aab150)

~~~json
{
  "source": "00aab150",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab1a8`](#insn-00aab1a8)

~~~json
{
  "source": "00aab1a8",
  "target": "00aab00c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1ac`](#insn-00aab1ac)

~~~json
{
  "source": "00aab1ac",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab1b0`](#insn-00aab1b0)

~~~json
{
  "source": "00aab1b0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1e4`](#insn-00aab1e4)

~~~json
{
  "source": "00aab1e4",
  "target": "00aab1ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab1f0`](#insn-00aab1f0)

~~~json
{
  "source": "00aab1f0",
  "target": "00aab218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab200`](#insn-00aab200)

~~~json
{
  "source": "00aab200",
  "target": "00aab1e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab208`](#insn-00aab208)

~~~json
{
  "source": "00aab208",
  "target": "00aab280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab210`](#insn-00aab210)

~~~json
{
  "source": "00aab210",
  "target": "00aab1f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab21c`](#insn-00aab21c)

~~~json
{
  "source": "00aab21c",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab224`](#insn-00aab224)

~~~json
{
  "source": "00aab224",
  "target": "Stack[-0x84]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab228`](#insn-00aab228)

~~~json
{
  "source": "00aab228",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab230`](#insn-00aab230)

~~~json
{
  "source": "00aab230",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab258`](#insn-00aab258)

~~~json
{
  "source": "00aab258",
  "target": "00aab264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab268`](#insn-00aab268)

~~~json
{
  "source": "00aab268",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab270`](#insn-00aab270)

~~~json
{
  "source": "00aab270",
  "target": "Stack[-0x84]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab274`](#insn-00aab274)

~~~json
{
  "source": "00aab274",
  "target": "Stack[-0x8c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2a4`](#insn-00aab2a4)

~~~json
{
  "source": "00aab2a4",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab2c0`](#insn-00aab2c0)

~~~json
{
  "source": "00aab2c0",
  "target": "00aab134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab2dc`](#insn-00aab2dc)

~~~json
{
  "source": "00aab2dc",
  "target": "00aab358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab300`](#insn-00aab300)

~~~json
{
  "source": "00aab300",
  "target": "00aab31c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab308`](#insn-00aab308)

~~~json
{
  "source": "00aab308",
  "target": "00aab370",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab310`](#insn-00aab310)

~~~json
{
  "source": "00aab310",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab318`](#insn-00aab318)

~~~json
{
  "source": "00aab318",
  "target": "00aab320",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab33c`](#insn-00aab33c)

~~~json
{
  "source": "00aab33c",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab348`](#insn-00aab348)

~~~json
{
  "source": "00aab348",
  "target": "00aab13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab350`](#insn-00aab350)

~~~json
{
  "source": "00aab350",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab354`](#insn-00aab354)

~~~json
{
  "source": "00aab354",
  "target": "00aab13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab358`](#insn-00aab358)

~~~json
{
  "source": "00aab358",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab360`](#insn-00aab360)

~~~json
{
  "source": "00aab360",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab368`](#insn-00aab368)

~~~json
{
  "source": "00aab368",
  "target": "00aab3bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab36c`](#insn-00aab36c)

~~~json
{
  "source": "00aab36c",
  "target": "00aaca78",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab370`](#insn-00aab370)

~~~json
{
  "source": "00aab370",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab378`](#insn-00aab378)

~~~json
{
  "source": "00aab378",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab380`](#insn-00aab380)

~~~json
{
  "source": "00aab380",
  "target": "00aab3bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aab384`](#insn-00aab384)

~~~json
{
  "source": "00aab384",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aab3bc`](#insn-00aab3bc)

~~~json
{
  "source": "00aab3bc",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
