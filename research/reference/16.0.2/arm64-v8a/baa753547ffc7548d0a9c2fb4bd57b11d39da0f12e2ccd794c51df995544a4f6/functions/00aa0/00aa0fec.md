# 00aa0fec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00aa0f7c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00aa0/00aa0f7c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-42e9704bba67246acf6150282e8c688f)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00aa1fe0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00aa1/00aa1fe0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0065.md#compare-b47a63cd3c5d8e8327fad75dc6947dca)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aa0fec",
  "name": "FUN_00aa0fec",
  "size": 944,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "80c426338596e1a878d66d5bcdc41229a940cef461b2a678626597a51f97a15d",
  "source_text_sha256": "80c426338596e1a878d66d5bcdc41229a940cef461b2a678626597a51f97a15d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aa0fec",
        "00aa1397"
      ],
      [
        "00aa1458",
        "00aa145b"
      ]
    ],
    "bytes_sha256": "f4a443bf56f3d585b04b363d71d7d7a21f480f0ce9e3b4aca07c570110d2d0c1",
    "instruction_count": 236,
    "instruction_bytes": 944,
    "body_bytes": 944,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a9f6cc](../00a9f/00a9f6cc.md)

## 呼び出し先

- [00470880](../00470/00470880.md)
- [00615f20](../00615/00615f20.md)
- [00674764](../00674/00674764.md)
- [00675b80](../00675/00675b80.md)
- [008003d0](../00800/008003d0.md)
- [00800684](../00800/00800684.md)
- [00851550](../00851/00851550.md)
- [00a65e5c](../00a65/00a65e5c.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c580d0](../00c58/00c580d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 7281 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00aa0fec(undefined8 *param_1,long param_2)

{
  void *pvVar1;
  size_t sVar2;
  long lVar3;
  void *__ptr;
  void *pvVar4;
  long *plVar5;
  bool bVar6;
  undefined4 uVar7;
  undefined4 uVar8;
  int iVar9;
  long lVar10;
  void *__dest;
  void *pvVar11;
  void *pvVar12;
  undefined8 *puVar13;
  long *plVar14;
  long *plVar15;
  void *local_a0;
  void *local_98;
  long local_90;
  undefined4 local_88;
  undefined4 uStack_84;
  void *local_80;
  void *local_78;
  void *local_70;
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  lVar10 = FUN_00851550();
  uVar7 = FUN_00675b80(lVar10 + 0x1438);
  FUN_00674764(&local_88,lVar10 + 0x1438,uVar7);
  pvVar4 = local_80;
  __ptr = (void *)CONCAT44(uStack_84,local_88);
  if (__ptr != (void *)0x0) {
    local_80 = __ptr;
    _ZdlPv(__ptr);
  }
  plVar14 = *(long **)(param_2 + 0x18);
  do {
    if (plVar14 == (long *)(param_2 + 0x20)) {
      if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00a9d0fc with catch @ 00aa1328 */
                    /* catch() { ... } // from try @ 00a9cde8 with catch @ 00aa1340 */
        return;
      }
LAB_00aa1458:
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    pvVar11 = (void *)plVar14[5];
    pvVar12 = (void *)plVar14[6];
    local_88 = (undefined4)plVar14[4];
    local_78 = (void *)0x0;
    local_70 = (void *)0x0;
    sVar2 = (long)pvVar12 - (long)pvVar11;
    local_80 = (void *)0x0;
    if (sVar2 == 0) {
      pvVar11 = (void *)0x0;
      __dest = (void *)0x0;
      if (_DAT_00000020 != 5) goto LAB_00aa12d4;
LAB_00aa1130:
      uVar7 = FUN_008003d0(*(int *)((long)pvVar11 + 0x54) / 100);
      uVar8 = FUN_00800684(*(int *)((long)pvVar11 + 0x54) / 100);
      iVar9 = FUN_00a65e5c(uVar7,uVar8,*(int *)((long)pvVar11 + 0x54) % 100,0,0);
      _ZdlPv(pvVar11);
      pvVar11 = local_80;
      if (iVar9 == 0) {
        local_a0 = (void *)0x0;
        local_98 = (void *)0x0;
        local_90 = 0;
        sVar2 = (long)local_78 - (long)local_80;
        if (sVar2 == 0) {
          pvVar12 = (void *)0x0;
        }
        else {
          if ((long)sVar2 < 0) {
                    /* catch() { ... } // from try @ 00a9cd1c with catch @ 00aa1360 */
                    /* catch() { ... } // from try @ 00a9fc44 with catch @ 00aa1364 */
                    /* catch() { ... } // from try @ 00a9d37c with catch @ 00aa1368 */
                    /* catch() { ... } // from try @ 00aa01e0 with catch @ 00aa136c */
                    /* catch() { ... } // from try @ 00aa0024 with catch @ 00aa1370 */
            if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00aa0fbc with catch @ 00aa1374 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00aa0ab0 with catch @ 00aa1378 */
              FUN_00470880(&local_a0);
            }
            goto LAB_00aa1458;
          }
          pvVar12 = (void *)_Znwm(sVar2);
          local_90 = (long)pvVar12 + sVar2;
          local_a0 = pvVar12;
          memcpy(pvVar12,pvVar11,sVar2);
        }
                    /* try { // try from 00aa11f0 to 00ba1303 has its CatchHandler @ 00aa13a0 */
        uVar7 = FUN_008003d0(*(int *)((long)pvVar12 + 0x50) / 100);
        uVar8 = FUN_00800684(*(int *)((long)pvVar12 + 0x50) / 100);
        iVar9 = FUN_00a65e5c(uVar7,uVar8,*(int *)((long)pvVar12 + 0x50) % 100,0,0);
        local_98 = pvVar12;
        _ZdlPv(pvVar12);
        pvVar11 = local_80;
        if ((__ptr != pvVar4) && (iVar9 != 0)) {
          puVar13 = (undefined8 *)param_1[1];
          if (puVar13 < (undefined8 *)param_1[2]) {
            *puVar13 = 0;
            puVar13[1] = 0;
            puVar13[2] = 0;
            sVar2 = (long)local_78 - (long)local_80;
            if (sVar2 != 0) {
              if ((long)sVar2 < 0) {
                    /* catch() { ... } // from try @ 00a9d460 with catch @ 00aa137c */
                    /* catch() { ... } // from try @ 00a9cedc with catch @ 00aa1380 */
                    /* catch() { ... } // from try @ 00aa0d84 with catch @ 00aa138c */
                if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00a9ea34 with catch @ 00aa1390 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00aa095c with catch @ 00aa1394
                       catch() { ... } // from try @ 00aa0b14 with catch @ 00aa1394 */
                  FUN_00470880(puVar13);
                }
                goto LAB_00aa1458;
              }
              pvVar12 = (void *)_Znwm(sVar2);
              *puVar13 = pvVar12;
              puVar13[1] = pvVar12;
              puVar13[2] = (long)pvVar12 + sVar2;
              memcpy(pvVar12,pvVar11,sVar2);
              puVar13[1] = (long)pvVar12 + sVar2;
            }
            puVar13 = puVar13 + 3;
          }
          else {
            puVar13 = (undefined8 *)FUN_00615f20(param_1,&local_80);
          }
          param_1[1] = puVar13;
        }
      }
      __dest = local_80;
      if (local_80 != (void *)0x0) goto LAB_00aa12d4;
    }
    else {
      if ((long)sVar2 < 0) {
                    /* catch() { ... } // from try @ 00a9d134 with catch @ 00aa1344 */
                    /* catch() { ... } // from try @ 00a9d0cc with catch @ 00aa1348 */
                    /* catch() { ... } // from try @ 00a9cdb8 with catch @ 00aa134c */
                    /* catch() { ... } // from try @ 00a9da34 with catch @ 00aa1350 */
                    /* catch() { ... } // from try @ 00a9d278 with catch @ 00aa1354 */
        if (*(long *)(lVar3 + 0x28) == local_68) {
                    /* catch() { ... } // from try @ 00a9d3b4 with catch @ 00aa1358 */
                    /* WARNING: Subroutine does not return */
                    /* catch() { ... } // from try @ 00a9d5b4 with catch @ 00aa135c */
          FUN_00470880(&local_80);
        }
        goto LAB_00aa1458;
      }
      __dest = (void *)_Znwm(sVar2);
      pvVar1 = (void *)((long)__dest + sVar2);
      local_80 = __dest;
      local_78 = __dest;
      local_70 = pvVar1;
      memcpy(__dest,pvVar11,sVar2);
      if (*(int *)((long)__dest + 0x20) == 5) {
        local_78 = pvVar1;
        if (pvVar12 == pvVar11) {
          pvVar11 = (void *)0x0;
        }
        else {
          pvVar11 = (void *)_Znwm(sVar2);
          memcpy(pvVar11,__dest,sVar2);
        }
        goto LAB_00aa1130;
      }
LAB_00aa12d4:
      local_78 = __dest;
      _ZdlPv(__dest);
    }
    plVar5 = (long *)plVar14[1];
    plVar15 = plVar14;
    if ((long *)plVar14[1] == (long *)0x0) {
      do {
        plVar14 = (long *)plVar15[2];
        bVar6 = (long *)*plVar14 != plVar15;
        plVar15 = plVar14;
                    /* try { // try from 00aa1304 to 00ba13cf has its CatchHandler @ 00a9bac4 */
      } while (bVar6);
    }
    else {
      do {
        plVar14 = plVar5;
        plVar5 = (long *)*plVar14;
      } while ((long *)*plVar14 != (long *)0x0);
    }
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aa0fec"></a> `00aa0fec` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00aa0ff0"></a> `00aa0ff0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aa0ff4"></a> `00aa0ff4` | `fc 6f 07 a9` | stp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aa0ff8"></a> `00aa0ff8` | `fa 67 08 a9` | stp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aa0ffc"></a> `00aa0ffc` | `f8 5f 09 a9` | stp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aa1000"></a> `00aa1000` | `f6 57 0a a9` | stp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aa1004"></a> `00aa1004` | `f4 4f 0b a9` | stp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aa1008"></a> `00aa1008` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00aa100c"></a> `00aa100c` | `49 d0 3b d5` | mrs x9,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aa1010"></a> `00aa1010` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aa1014"></a> `00aa1014` | `e9 23 00 a9` | stp x9,x8,[sp] | `FALL_THROUGH`
<a id="insn-00aa1018"></a> `00aa1018` | `29 15 40 f9` | ldr x9,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00aa101c"></a> `00aa101c` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa1020"></a> `00aa1020` | `1f 7d 00 a9` | stp xzr,xzr,[x8] | `FALL_THROUGH`
<a id="insn-00aa1024"></a> `00aa1024` | `1f 09 00 f9` | str xzr,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1028"></a> `00aa1028` | `4a c1 f6 97` | bl 0x00851550 | `UNCONDITIONAL_CALL`
<a id="insn-00aa102c"></a> `00aa102c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aa1030"></a> `00aa1030` | `13 87 82 52` | mov w19,#0x1438 | `FALL_THROUGH`
<a id="insn-00aa1034"></a> `00aa1034` | `00 00 13 8b` | add x0,x0,x19 | `FALL_THROUGH`
<a id="insn-00aa1038"></a> `00aa1038` | `d2 52 ef 97` | bl 0x00675b80 | `UNCONDITIONAL_CALL`
<a id="insn-00aa103c"></a> `00aa103c` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00aa1040"></a> `00aa1040` | `a8 a3 00 d1` | sub x8,x29,#0x28 | `FALL_THROUGH`
<a id="insn-00aa1044"></a> `00aa1044` | `80 02 13 8b` | add x0,x20,x19 | `FALL_THROUGH`
<a id="insn-00aa1048"></a> `00aa1048` | `c7 4d ef 97` | bl 0x00674764 | `UNCONDITIONAL_CALL`
<a id="insn-00aa104c"></a> `00aa104c` | `b3 a3 7d a9` | ldp x19,x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00aa1050"></a> `00aa1050` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1054"></a> `00aa1054` | `93 00 00 b4` | cbz x19,0x00aa1064 | `CONDITIONAL_JUMP`
<a id="insn-00aa1058"></a> `00aa1058` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa105c"></a> `00aa105c` | `b3 03 1e f8` | stur x19,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aa1060"></a> `00aa1060` | `c8 db 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1064"></a> `00aa1064` | `bc 0e 40 f9` | ldr x28,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00aa1068"></a> `00aa1068` | `bb 82 00 91` | add x27,x21,#0x20 | `FALL_THROUGH`
<a id="insn-00aa106c"></a> `00aa106c` | `f3 0f 00 f9` | str x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aa1070"></a> `00aa1070` | `9f 03 1b eb` | cmp x28,x27 | `FALL_THROUGH`
<a id="insn-00aa1074"></a> `00aa1074` | `e0 14 00 54` | b.eq 0x00aa1310 | `CONDITIONAL_JUMP`
<a id="insn-00aa1078"></a> `00aa1078` | `f8 a3 90 52` | mov w24,#0x851f | `FALL_THROUGH`
<a id="insn-00aa107c"></a> `00aa107c` | `ba a3 00 d1` | sub x26,x29,#0x28 | `FALL_THROUGH`
<a id="insn-00aa1080"></a> `00aa1080` | `99 0c 80 52` | mov w25,#0x64 | `FALL_THROUGH`
<a id="insn-00aa1084"></a> `00aa1084` | `78 3d aa 72` | movk w24,#0x51eb, LSL #16 | `FALL_THROUGH`
<a id="insn-00aa1088"></a> `00aa1088` | `04 00 00 14` | b 0x00aa1098 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa108c"></a> `00aa108c` | `1f 01 1b eb` | cmp x8,x27 | `FALL_THROUGH`
<a id="insn-00aa1090"></a> `00aa1090` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-00aa1094"></a> `00aa1094` | `e0 13 00 54` | b.eq 0x00aa1310 | `CONDITIONAL_JUMP`
<a id="insn-00aa1098"></a> `00aa1098` | `95 cf 42 a9` | ldp x21,x19,[x28, #0x28] | `FALL_THROUGH`
<a id="insn-00aa109c"></a> `00aa109c` | `88 23 40 b9` | ldr w8,[x28, #0x20] | `FALL_THROUGH`
<a id="insn-00aa10a0"></a> `00aa10a0` | `5f 7f 01 a9` | stp xzr,xzr,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00aa10a4"></a> `00aa10a4` | `a8 83 1d b8` | stur w8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00aa10a8"></a> `00aa10a8` | `76 02 15 eb` | subs x22,x19,x21 | `FALL_THROUGH`
<a id="insn-00aa10ac"></a> `00aa10ac` | `5f 83 00 f8` | stur xzr,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00aa10b0"></a> `00aa10b0` | `00 03 00 54` | b.eq 0x00aa1110 | `CONDITIONAL_JUMP`
<a id="insn-00aa10b4"></a> `00aa10b4` | `96 14 f8 b7` | tbnz x22,#0x3f,0x00aa1344 | `CONDITIONAL_JUMP`
<a id="insn-00aa10b8"></a> `00aa10b8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aa10bc"></a> `00aa10bc` | `a9 db 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aa10c0"></a> `00aa10c0` | `14 00 16 8b` | add x20,x0,x22 | `FALL_THROUGH`
<a id="insn-00aa10c4"></a> `00aa10c4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00aa10c8"></a> `00aa10c8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00aa10cc"></a> `00aa10cc` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00aa10d0"></a> `00aa10d0` | `a0 03 3e a9` | stp x0,x0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aa10d4"></a> `00aa10d4` | `b4 03 1f f8` | stur x20,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00aa10d8"></a> `00aa10d8` | `fe db 06 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa10dc"></a> `00aa10dc` | `e8 22 40 b9` | ldr w8,[x23, #0x20] | `FALL_THROUGH`
<a id="insn-00aa10e0"></a> `00aa10e0` | `b4 83 1e f8` | stur x20,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aa10e4"></a> `00aa10e4` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00aa10e8"></a> `00aa10e8` | `61 0f 00 54` | b.ne 0x00aa12d4 | `CONDITIONAL_JUMP`
<a id="insn-00aa10ec"></a> `00aa10ec` | `7f 02 15 eb` | cmp x19,x21 | `FALL_THROUGH`
<a id="insn-00aa10f0"></a> `00aa10f0` | `e0 01 00 54` | b.eq 0x00aa112c | `CONDITIONAL_JUMP`
<a id="insn-00aa10f4"></a> `00aa10f4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aa10f8"></a> `00aa10f8` | `9a db 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aa10fc"></a> `00aa10fc` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00aa1100"></a> `00aa1100` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00aa1104"></a> `00aa1104` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aa1108"></a> `00aa1108` | `f2 db 06 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa110c"></a> `00aa110c` | `09 00 00 14` | b 0x00aa1130 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa1110"></a> `00aa1110` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aa1114"></a> `00aa1114` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00aa1118"></a> `00aa1118` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00aa111c"></a> `00aa111c` | `08 01 40 b9` | ldr w8,[x8] | `FALL_THROUGH`
<a id="insn-00aa1120"></a> `00aa1120` | `1f 15 00 71` | cmp w8,#0x5 | `FALL_THROUGH`
<a id="insn-00aa1124"></a> `00aa1124` | `60 00 00 54` | b.eq 0x00aa1130 | `CONDITIONAL_JUMP`
<a id="insn-00aa1128"></a> `00aa1128` | `6b 00 00 14` | b 0x00aa12d4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa112c"></a> `00aa112c` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00aa1130"></a> `00aa1130` | `a8 56 80 b9` | ldrsw x8,[x21, #0x54] | `FALL_THROUGH`
<a id="insn-00aa1134"></a> `00aa1134` | `08 7d 38 9b` | smull x8,w8,w24 | `FALL_THROUGH`
<a id="insn-00aa1138"></a> `00aa1138` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00aa113c"></a> `00aa113c` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-00aa1140"></a> `00aa1140` | `00 01 09 0b` | add w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00aa1144"></a> `00aa1144` | `a3 7c f5 97` | bl 0x008003d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1148"></a> `00aa1148` | `a8 56 80 b9` | ldrsw x8,[x21, #0x54] | `FALL_THROUGH`
<a id="insn-00aa114c"></a> `00aa114c` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aa1150"></a> `00aa1150` | `08 7d 38 9b` | smull x8,w8,w24 | `FALL_THROUGH`
<a id="insn-00aa1154"></a> `00aa1154` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00aa1158"></a> `00aa1158` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-00aa115c"></a> `00aa115c` | `00 01 09 0b` | add w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00aa1160"></a> `00aa1160` | `49 7d f5 97` | bl 0x00800684 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1164"></a> `00aa1164` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00aa1168"></a> `00aa1168` | `a8 56 80 b9` | ldrsw x8,[x21, #0x54] | `FALL_THROUGH`
<a id="insn-00aa116c"></a> `00aa116c` | `09 7d 38 9b` | smull x9,w8,w24 | `FALL_THROUGH`
<a id="insn-00aa1170"></a> `00aa1170` | `2a fd 7f d3` | lsr x10,x9,#0x3f | `FALL_THROUGH`
<a id="insn-00aa1174"></a> `00aa1174` | `29 fd 65 93` | asr x9,x9,#0x25 | `FALL_THROUGH`
<a id="insn-00aa1178"></a> `00aa1178` | `29 01 0a 0b` | add w9,w9,w10 | `FALL_THROUGH`
<a id="insn-00aa117c"></a> `00aa117c` | `22 a1 19 1b` | msub w2,w9,w25,w8 | `FALL_THROUGH`
<a id="insn-00aa1180"></a> `00aa1180` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00aa1184"></a> `00aa1184` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aa1188"></a> `00aa1188` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aa118c"></a> `00aa118c` | `34 13 ff 97` | bl 0x00a65e5c | `UNCONDITIONAL_CALL`
<a id="insn-00aa1190"></a> `00aa1190` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aa1194"></a> `00aa1194` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aa1198"></a> `00aa1198` | `7a db 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aa119c"></a> `00aa119c` | `96 09 00 35` | cbnz w22,0x00aa12cc | `CONDITIONAL_JUMP`
<a id="insn-00aa11a0"></a> `00aa11a0` | `b6 23 7e a9` | ldp x22,x8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aa11a4"></a> `00aa11a4` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa11a8"></a> `00aa11a8` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa11ac"></a> `00aa11ac` | `17 01 16 eb` | subs x23,x8,x22 | `FALL_THROUGH`
<a id="insn-00aa11b0"></a> `00aa11b0` | `80 01 00 54` | b.eq 0x00aa11e0 | `CONDITIONAL_JUMP`
<a id="insn-00aa11b4"></a> `00aa11b4` | `77 0d f8 b7` | tbnz x23,#0x3f,0x00aa1360 | `CONDITIONAL_JUMP`
<a id="insn-00aa11b8"></a> `00aa11b8` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00aa11bc"></a> `00aa11bc` | `69 db 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aa11c0"></a> `00aa11c0` | `08 00 17 8b` | add x8,x0,x23 | `FALL_THROUGH`
<a id="insn-00aa11c4"></a> `00aa11c4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00aa11c8"></a> `00aa11c8` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00aa11cc"></a> `00aa11cc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aa11d0"></a> `00aa11d0` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aa11d4"></a> `00aa11d4` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aa11d8"></a> `00aa11d8` | `be db 06 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa11dc"></a> `00aa11dc` | `02 00 00 14` | b 0x00aa11e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa11e0"></a> `00aa11e0` | `f5 03 1f aa` | mov x21,xzr | `FALL_THROUGH`
<a id="insn-00aa11e4"></a> `00aa11e4` | `a8 52 80 b9` | ldrsw x8,[x21, #0x50] | `FALL_THROUGH`
<a id="insn-00aa11e8"></a> `00aa11e8` | `08 7d 38 9b` | smull x8,w8,w24 | `FALL_THROUGH`
<a id="insn-00aa11ec"></a> `00aa11ec` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00aa11f0"></a> `00aa11f0` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-00aa11f4"></a> `00aa11f4` | `00 01 09 0b` | add w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00aa11f8"></a> `00aa11f8` | `76 7c f5 97` | bl 0x008003d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa11fc"></a> `00aa11fc` | `a8 52 80 b9` | ldrsw x8,[x21, #0x50] | `FALL_THROUGH`
<a id="insn-00aa1200"></a> `00aa1200` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aa1204"></a> `00aa1204` | `08 7d 38 9b` | smull x8,w8,w24 | `FALL_THROUGH`
<a id="insn-00aa1208"></a> `00aa1208` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00aa120c"></a> `00aa120c` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-00aa1210"></a> `00aa1210` | `00 01 09 0b` | add w0,w8,w9 | `FALL_THROUGH`
<a id="insn-00aa1214"></a> `00aa1214` | `1c 7d f5 97` | bl 0x00800684 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1218"></a> `00aa1218` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00aa121c"></a> `00aa121c` | `a8 52 80 b9` | ldrsw x8,[x21, #0x50] | `FALL_THROUGH`
<a id="insn-00aa1220"></a> `00aa1220` | `09 7d 38 9b` | smull x9,w8,w24 | `FALL_THROUGH`
<a id="insn-00aa1224"></a> `00aa1224` | `2a fd 7f d3` | lsr x10,x9,#0x3f | `FALL_THROUGH`
<a id="insn-00aa1228"></a> `00aa1228` | `29 fd 65 93` | asr x9,x9,#0x25 | `FALL_THROUGH`
<a id="insn-00aa122c"></a> `00aa122c` | `29 01 0a 0b` | add w9,w9,w10 | `FALL_THROUGH`
<a id="insn-00aa1230"></a> `00aa1230` | `22 a1 19 1b` | msub w2,w9,w25,w8 | `FALL_THROUGH`
<a id="insn-00aa1234"></a> `00aa1234` | `e0 03 16 2a` | mov w0,w22 | `FALL_THROUGH`
<a id="insn-00aa1238"></a> `00aa1238` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aa123c"></a> `00aa123c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aa1240"></a> `00aa1240` | `07 13 ff 97` | bl 0x00a65e5c | `UNCONDITIONAL_CALL`
<a id="insn-00aa1244"></a> `00aa1244` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aa1248"></a> `00aa1248` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aa124c"></a> `00aa124c` | `f5 17 00 f9` | str x21,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aa1250"></a> `00aa1250` | `4c db 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1254"></a> `00aa1254` | `e9 23 41 a9` | ldp x9,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aa1258"></a> `00aa1258` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aa125c"></a> `00aa125c` | `80 03 00 54` | b.eq 0x00aa12cc | `CONDITIONAL_JUMP`
<a id="insn-00aa1260"></a> `00aa1260` | `76 03 00 34` | cbz w22,0x00aa12cc | `CONDITIONAL_JUMP`
<a id="insn-00aa1264"></a> `00aa1264` | `f3 07 40 f9` | ldr x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aa1268"></a> `00aa1268` | `75 a2 40 a9` | ldp x21,x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aa126c"></a> `00aa126c` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00aa1270"></a> `00aa1270` | `62 02 00 54` | b.cs 0x00aa12bc | `CONDITIONAL_JUMP`
<a id="insn-00aa1274"></a> `00aa1274` | `bf 7e 00 a9` | stp xzr,xzr,[x21] | `FALL_THROUGH`
<a id="insn-00aa1278"></a> `00aa1278` | `bf 0a 00 f9` | str xzr,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00aa127c"></a> `00aa127c` | `b6 23 7e a9` | ldp x22,x8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aa1280"></a> `00aa1280` | `17 01 16 eb` | subs x23,x8,x22 | `FALL_THROUGH`
<a id="insn-00aa1284"></a> `00aa1284` | `60 01 00 54` | b.eq 0x00aa12b0 | `CONDITIONAL_JUMP`
<a id="insn-00aa1288"></a> `00aa1288` | `b7 07 f8 b7` | tbnz x23,#0x3f,0x00aa137c | `CONDITIONAL_JUMP`
<a id="insn-00aa128c"></a> `00aa128c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00aa1290"></a> `00aa1290` | `34 db 06 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00aa1294"></a> `00aa1294` | `13 00 17 8b` | add x19,x0,x23 | `FALL_THROUGH`
<a id="insn-00aa1298"></a> `00aa1298` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00aa129c"></a> `00aa129c` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00aa12a0"></a> `00aa12a0` | `a0 02 00 a9` | stp x0,x0,[x21] | `FALL_THROUGH`
<a id="insn-00aa12a4"></a> `00aa12a4` | `b3 0a 00 f9` | str x19,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00aa12a8"></a> `00aa12a8` | `8a db 06 94` | bl 0x00c580d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aa12ac"></a> `00aa12ac` | `b3 06 00 f9` | str x19,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00aa12b0"></a> `00aa12b0` | `f3 07 40 f9` | ldr x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aa12b4"></a> `00aa12b4` | `a0 62 00 91` | add x0,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00aa12b8"></a> `00aa12b8` | `04 00 00 14` | b 0x00aa12c8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aa12bc"></a> `00aa12bc` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00aa12c0"></a> `00aa12c0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00aa12c4"></a> `00aa12c4` | `17 d3 ed 97` | bl 0x00615f20 | `UNCONDITIONAL_CALL`
<a id="insn-00aa12c8"></a> `00aa12c8` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00aa12cc"></a> `00aa12cc` | `b7 03 5e f8` | ldur x23,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aa12d0"></a> `00aa12d0` | `97 00 00 b4` | cbz x23,0x00aa12e0 | `CONDITIONAL_JUMP`
<a id="insn-00aa12d4"></a> `00aa12d4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00aa12d8"></a> `00aa12d8` | `b7 83 1e f8` | stur x23,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aa12dc"></a> `00aa12dc` | `29 db 06 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00aa12e0"></a> `00aa12e0` | `89 07 40 f9` | ldr x9,[x28, #0x8] | `FALL_THROUGH`
<a id="insn-00aa12e4"></a> `00aa12e4` | `a9 00 00 b4` | cbz x9,0x00aa12f8 | `CONDITIONAL_JUMP`
<a id="insn-00aa12e8"></a> `00aa12e8` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00aa12ec"></a> `00aa12ec` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aa12f0"></a> `00aa12f0` | `c9 ff ff b5` | cbnz x9,0x00aa12e8 | `CONDITIONAL_JUMP`
<a id="insn-00aa12f4"></a> `00aa12f4` | `66 ff ff 17` | b 0x00aa108c | `UNCONDITIONAL_JUMP`
<a id="insn-00aa12f8"></a> `00aa12f8` | `88 0b 40 f9` | ldr x8,[x28, #0x10] | `FALL_THROUGH`
<a id="insn-00aa12fc"></a> `00aa12fc` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00aa1300"></a> `00aa1300` | `3f 01 1c eb` | cmp x9,x28 | `FALL_THROUGH`
<a id="insn-00aa1304"></a> `00aa1304` | `fc 03 08 aa` | mov x28,x8 | `FALL_THROUGH`
<a id="insn-00aa1308"></a> `00aa1308` | `81 ff ff 54` | b.ne 0x00aa12f8 | `CONDITIONAL_JUMP`
<a id="insn-00aa130c"></a> `00aa130c` | `60 ff ff 17` | b 0x00aa108c | `UNCONDITIONAL_JUMP`
<a id="insn-00aa1310"></a> `00aa1310` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00aa1314"></a> `00aa1314` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aa1318"></a> `00aa1318` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa131c"></a> `00aa131c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aa1320"></a> `00aa1320` | `c1 09 00 54` | b.ne 0x00aa1458 | `CONDITIONAL_JUMP`
<a id="insn-00aa1324"></a> `00aa1324` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aa1328"></a> `00aa1328` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aa132c"></a> `00aa132c` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aa1330"></a> `00aa1330` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aa1334"></a> `00aa1334` | `fc 6f 47 a9` | ldp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aa1338"></a> `00aa1338` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aa133c"></a> `00aa133c` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00aa1340"></a> `00aa1340` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aa1344"></a> `00aa1344` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00aa1348"></a> `00aa1348` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aa134c"></a> `00aa134c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa1350"></a> `00aa1350` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aa1354"></a> `00aa1354` | `21 08 00 54` | b.ne 0x00aa1458 | `CONDITIONAL_JUMP`
<a id="insn-00aa1358"></a> `00aa1358` | `40 23 00 91` | add x0,x26,#0x8 | `FALL_THROUGH`
<a id="insn-00aa135c"></a> `00aa135c` | `49 3d e7 97` | bl 0x00470880 | `CALL_TERMINATOR`
<a id="insn-00aa1360"></a> `00aa1360` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00aa1364"></a> `00aa1364` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aa1368"></a> `00aa1368` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa136c"></a> `00aa136c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aa1370"></a> `00aa1370` | `41 07 00 54` | b.ne 0x00aa1458 | `CONDITIONAL_JUMP`
<a id="insn-00aa1374"></a> `00aa1374` | `e0 83 00 91` | add x0,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00aa1378"></a> `00aa1378` | `42 3d e7 97` | bl 0x00470880 | `CALL_TERMINATOR`
<a id="insn-00aa137c"></a> `00aa137c` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00aa1380"></a> `00aa1380` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aa1384"></a> `00aa1384` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aa1388"></a> `00aa1388` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aa138c"></a> `00aa138c` | `61 06 00 54` | b.ne 0x00aa1458 | `CONDITIONAL_JUMP`
<a id="insn-00aa1390"></a> `00aa1390` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aa1394"></a> `00aa1394` | `3b 3d e7 97` | bl 0x00470880 | `CALL_TERMINATOR`
<a id="insn-00aa1458"></a> `00aa1458` | `d6 da 06 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aa0fec`](#insn-00aa0fec) 範囲 `[['00aa0fec', '00aa1057']]`
  - `CONDITIONAL_JUMP` [`00aa1054`](#insn-00aa1054) → [`00aa1064`](#insn-00aa1064)
  - `FALL_THROUGH` [`00aa1054`](#insn-00aa1054) → [`00aa1058`](#insn-00aa1058)
- ブロック [`00aa1058`](#insn-00aa1058) 範囲 `[['00aa1058', '00aa1063']]`
  - `FALL_THROUGH` [`00aa1060`](#insn-00aa1060) → [`00aa1064`](#insn-00aa1064)
- ブロック [`00aa1064`](#insn-00aa1064) 範囲 `[['00aa1064', '00aa1077']]`
  - `CONDITIONAL_JUMP` [`00aa1074`](#insn-00aa1074) → [`00aa1310`](#insn-00aa1310)
  - `FALL_THROUGH` [`00aa1074`](#insn-00aa1074) → [`00aa1078`](#insn-00aa1078)
- ブロック [`00aa1078`](#insn-00aa1078) 範囲 `[['00aa1078', '00aa108b']]`
  - `UNCONDITIONAL_JUMP` [`00aa1088`](#insn-00aa1088) → [`00aa1098`](#insn-00aa1098)
- ブロック [`00aa108c`](#insn-00aa108c) 範囲 `[['00aa108c', '00aa1097']]`
  - `CONDITIONAL_JUMP` [`00aa1094`](#insn-00aa1094) → [`00aa1310`](#insn-00aa1310)
  - `FALL_THROUGH` [`00aa1094`](#insn-00aa1094) → [`00aa1098`](#insn-00aa1098)
- ブロック [`00aa1098`](#insn-00aa1098) 範囲 `[['00aa1098', '00aa10b3']]`
  - `CONDITIONAL_JUMP` [`00aa10b0`](#insn-00aa10b0) → [`00aa1110`](#insn-00aa1110)
  - `FALL_THROUGH` [`00aa10b0`](#insn-00aa10b0) → [`00aa10b4`](#insn-00aa10b4)
- ブロック [`00aa10b4`](#insn-00aa10b4) 範囲 `[['00aa10b4', '00aa10b7']]`
  - `CONDITIONAL_JUMP` [`00aa10b4`](#insn-00aa10b4) → [`00aa1344`](#insn-00aa1344)
  - `FALL_THROUGH` [`00aa10b4`](#insn-00aa10b4) → [`00aa10b8`](#insn-00aa10b8)
- ブロック [`00aa10b8`](#insn-00aa10b8) 範囲 `[['00aa10b8', '00aa10eb']]`
  - `CONDITIONAL_JUMP` [`00aa10e8`](#insn-00aa10e8) → [`00aa12d4`](#insn-00aa12d4)
  - `FALL_THROUGH` [`00aa10e8`](#insn-00aa10e8) → [`00aa10ec`](#insn-00aa10ec)
- ブロック [`00aa10ec`](#insn-00aa10ec) 範囲 `[['00aa10ec', '00aa10f3']]`
  - `CONDITIONAL_JUMP` [`00aa10f0`](#insn-00aa10f0) → [`00aa112c`](#insn-00aa112c)
  - `FALL_THROUGH` [`00aa10f0`](#insn-00aa10f0) → [`00aa10f4`](#insn-00aa10f4)
- ブロック [`00aa10f4`](#insn-00aa10f4) 範囲 `[['00aa10f4', '00aa110f']]`
  - `UNCONDITIONAL_JUMP` [`00aa110c`](#insn-00aa110c) → [`00aa1130`](#insn-00aa1130)
- ブロック [`00aa1110`](#insn-00aa1110) 範囲 `[['00aa1110', '00aa1127']]`
  - `CONDITIONAL_JUMP` [`00aa1124`](#insn-00aa1124) → [`00aa1130`](#insn-00aa1130)
  - `FALL_THROUGH` [`00aa1124`](#insn-00aa1124) → [`00aa1128`](#insn-00aa1128)
- ブロック [`00aa1128`](#insn-00aa1128) 範囲 `[['00aa1128', '00aa112b']]`
  - `UNCONDITIONAL_JUMP` [`00aa1128`](#insn-00aa1128) → [`00aa12d4`](#insn-00aa12d4)
- ブロック [`00aa112c`](#insn-00aa112c) 範囲 `[['00aa112c', '00aa112f']]`
  - `FALL_THROUGH` [`00aa112c`](#insn-00aa112c) → [`00aa1130`](#insn-00aa1130)
- ブロック [`00aa1130`](#insn-00aa1130) 範囲 `[['00aa1130', '00aa119f']]`
  - `CONDITIONAL_JUMP` [`00aa119c`](#insn-00aa119c) → [`00aa12cc`](#insn-00aa12cc)
  - `FALL_THROUGH` [`00aa119c`](#insn-00aa119c) → [`00aa11a0`](#insn-00aa11a0)
- ブロック [`00aa11a0`](#insn-00aa11a0) 範囲 `[['00aa11a0', '00aa11b3']]`
  - `CONDITIONAL_JUMP` [`00aa11b0`](#insn-00aa11b0) → [`00aa11e0`](#insn-00aa11e0)
  - `FALL_THROUGH` [`00aa11b0`](#insn-00aa11b0) → [`00aa11b4`](#insn-00aa11b4)
- ブロック [`00aa11b4`](#insn-00aa11b4) 範囲 `[['00aa11b4', '00aa11b7']]`
  - `CONDITIONAL_JUMP` [`00aa11b4`](#insn-00aa11b4) → [`00aa1360`](#insn-00aa1360)
  - `FALL_THROUGH` [`00aa11b4`](#insn-00aa11b4) → [`00aa11b8`](#insn-00aa11b8)
- ブロック [`00aa11b8`](#insn-00aa11b8) 範囲 `[['00aa11b8', '00aa11df']]`
  - `UNCONDITIONAL_JUMP` [`00aa11dc`](#insn-00aa11dc) → [`00aa11e4`](#insn-00aa11e4)
- ブロック [`00aa11e0`](#insn-00aa11e0) 範囲 `[['00aa11e0', '00aa11e3']]`
  - `FALL_THROUGH` [`00aa11e0`](#insn-00aa11e0) → [`00aa11e4`](#insn-00aa11e4)
- ブロック [`00aa11e4`](#insn-00aa11e4) 範囲 `[['00aa11e4', '00aa11ef']]`
  - `FALL_THROUGH` [`00aa11ec`](#insn-00aa11ec) → [`00aa11f0`](#insn-00aa11f0)
- ブロック [`00aa11f0`](#insn-00aa11f0) 範囲 `[['00aa11f0', '00aa125f']]`
  - `CONDITIONAL_JUMP` [`00aa125c`](#insn-00aa125c) → [`00aa12cc`](#insn-00aa12cc)
  - `FALL_THROUGH` [`00aa125c`](#insn-00aa125c) → [`00aa1260`](#insn-00aa1260)
- ブロック [`00aa1260`](#insn-00aa1260) 範囲 `[['00aa1260', '00aa1263']]`
  - `CONDITIONAL_JUMP` [`00aa1260`](#insn-00aa1260) → [`00aa12cc`](#insn-00aa12cc)
  - `FALL_THROUGH` [`00aa1260`](#insn-00aa1260) → [`00aa1264`](#insn-00aa1264)
- ブロック [`00aa1264`](#insn-00aa1264) 範囲 `[['00aa1264', '00aa1273']]`
  - `CONDITIONAL_JUMP` [`00aa1270`](#insn-00aa1270) → [`00aa12bc`](#insn-00aa12bc)
  - `FALL_THROUGH` [`00aa1270`](#insn-00aa1270) → [`00aa1274`](#insn-00aa1274)
- ブロック [`00aa1274`](#insn-00aa1274) 範囲 `[['00aa1274', '00aa1287']]`
  - `CONDITIONAL_JUMP` [`00aa1284`](#insn-00aa1284) → [`00aa12b0`](#insn-00aa12b0)
  - `FALL_THROUGH` [`00aa1284`](#insn-00aa1284) → [`00aa1288`](#insn-00aa1288)
- ブロック [`00aa1288`](#insn-00aa1288) 範囲 `[['00aa1288', '00aa128b']]`
  - `CONDITIONAL_JUMP` [`00aa1288`](#insn-00aa1288) → [`00aa137c`](#insn-00aa137c)
  - `FALL_THROUGH` [`00aa1288`](#insn-00aa1288) → [`00aa128c`](#insn-00aa128c)
- ブロック [`00aa128c`](#insn-00aa128c) 範囲 `[['00aa128c', '00aa12af']]`
  - `FALL_THROUGH` [`00aa12ac`](#insn-00aa12ac) → [`00aa12b0`](#insn-00aa12b0)
- ブロック [`00aa12b0`](#insn-00aa12b0) 範囲 `[['00aa12b0', '00aa12bb']]`
  - `UNCONDITIONAL_JUMP` [`00aa12b8`](#insn-00aa12b8) → [`00aa12c8`](#insn-00aa12c8)
- ブロック [`00aa12bc`](#insn-00aa12bc) 範囲 `[['00aa12bc', '00aa12c7']]`
  - `FALL_THROUGH` [`00aa12c4`](#insn-00aa12c4) → [`00aa12c8`](#insn-00aa12c8)
- ブロック [`00aa12c8`](#insn-00aa12c8) 範囲 `[['00aa12c8', '00aa12cb']]`
  - `FALL_THROUGH` [`00aa12c8`](#insn-00aa12c8) → [`00aa12cc`](#insn-00aa12cc)
- ブロック [`00aa12cc`](#insn-00aa12cc) 範囲 `[['00aa12cc', '00aa12d3']]`
  - `CONDITIONAL_JUMP` [`00aa12d0`](#insn-00aa12d0) → [`00aa12e0`](#insn-00aa12e0)
  - `FALL_THROUGH` [`00aa12d0`](#insn-00aa12d0) → [`00aa12d4`](#insn-00aa12d4)
- ブロック [`00aa12d4`](#insn-00aa12d4) 範囲 `[['00aa12d4', '00aa12df']]`
  - `FALL_THROUGH` [`00aa12dc`](#insn-00aa12dc) → [`00aa12e0`](#insn-00aa12e0)
- ブロック [`00aa12e0`](#insn-00aa12e0) 範囲 `[['00aa12e0', '00aa12e7']]`
  - `CONDITIONAL_JUMP` [`00aa12e4`](#insn-00aa12e4) → [`00aa12f8`](#insn-00aa12f8)
  - `FALL_THROUGH` [`00aa12e4`](#insn-00aa12e4) → [`00aa12e8`](#insn-00aa12e8)
- ブロック [`00aa12e8`](#insn-00aa12e8) 範囲 `[['00aa12e8', '00aa12f3']]`
  - `CONDITIONAL_JUMP` [`00aa12f0`](#insn-00aa12f0) → [`00aa12e8`](#insn-00aa12e8)
  - `FALL_THROUGH` [`00aa12f0`](#insn-00aa12f0) → [`00aa12f4`](#insn-00aa12f4)
- ブロック [`00aa12f4`](#insn-00aa12f4) 範囲 `[['00aa12f4', '00aa12f7']]`
  - `UNCONDITIONAL_JUMP` [`00aa12f4`](#insn-00aa12f4) → [`00aa108c`](#insn-00aa108c)
- ブロック [`00aa12f8`](#insn-00aa12f8) 範囲 `[['00aa12f8', '00aa1303']]`
  - `FALL_THROUGH` [`00aa1300`](#insn-00aa1300) → [`00aa1304`](#insn-00aa1304)
- ブロック [`00aa1304`](#insn-00aa1304) 範囲 `[['00aa1304', '00aa130b']]`
  - `CONDITIONAL_JUMP` [`00aa1308`](#insn-00aa1308) → [`00aa12f8`](#insn-00aa12f8)
  - `FALL_THROUGH` [`00aa1308`](#insn-00aa1308) → [`00aa130c`](#insn-00aa130c)
- ブロック [`00aa130c`](#insn-00aa130c) 範囲 `[['00aa130c', '00aa130f']]`
  - `UNCONDITIONAL_JUMP` [`00aa130c`](#insn-00aa130c) → [`00aa108c`](#insn-00aa108c)
- ブロック [`00aa1310`](#insn-00aa1310) 範囲 `[['00aa1310', '00aa1323']]`
  - `CONDITIONAL_JUMP` [`00aa1320`](#insn-00aa1320) → [`00aa1458`](#insn-00aa1458)
  - `FALL_THROUGH` [`00aa1320`](#insn-00aa1320) → [`00aa1324`](#insn-00aa1324)
- ブロック [`00aa1324`](#insn-00aa1324) 範囲 `[['00aa1324', '00aa1327']]`
  - `FALL_THROUGH` [`00aa1324`](#insn-00aa1324) → [`00aa1328`](#insn-00aa1328)
- ブロック [`00aa1328`](#insn-00aa1328) 範囲 `[['00aa1328', '00aa133f']]`
  - `FALL_THROUGH` [`00aa133c`](#insn-00aa133c) → [`00aa1340`](#insn-00aa1340)
- ブロック [`00aa1340`](#insn-00aa1340) 範囲 `[['00aa1340', '00aa1343']]`
- ブロック [`00aa1344`](#insn-00aa1344) 範囲 `[['00aa1344', '00aa1347']]`
  - `FALL_THROUGH` [`00aa1344`](#insn-00aa1344) → [`00aa1348`](#insn-00aa1348)
- ブロック [`00aa1348`](#insn-00aa1348) 範囲 `[['00aa1348', '00aa134b']]`
  - `FALL_THROUGH` [`00aa1348`](#insn-00aa1348) → [`00aa134c`](#insn-00aa134c)
- ブロック [`00aa134c`](#insn-00aa134c) 範囲 `[['00aa134c', '00aa134f']]`
  - `FALL_THROUGH` [`00aa134c`](#insn-00aa134c) → [`00aa1350`](#insn-00aa1350)
- ブロック [`00aa1350`](#insn-00aa1350) 範囲 `[['00aa1350', '00aa1353']]`
  - `FALL_THROUGH` [`00aa1350`](#insn-00aa1350) → [`00aa1354`](#insn-00aa1354)
- ブロック [`00aa1354`](#insn-00aa1354) 範囲 `[['00aa1354', '00aa1357']]`
  - `CONDITIONAL_JUMP` [`00aa1354`](#insn-00aa1354) → [`00aa1458`](#insn-00aa1458)
  - `FALL_THROUGH` [`00aa1354`](#insn-00aa1354) → [`00aa1358`](#insn-00aa1358)
- ブロック [`00aa1358`](#insn-00aa1358) 範囲 `[['00aa1358', '00aa135b']]`
  - `FALL_THROUGH` [`00aa1358`](#insn-00aa1358) → [`00aa135c`](#insn-00aa135c)
- ブロック [`00aa135c`](#insn-00aa135c) 範囲 `[['00aa135c', '00aa135f']]`
- ブロック [`00aa1360`](#insn-00aa1360) 範囲 `[['00aa1360', '00aa1363']]`
  - `FALL_THROUGH` [`00aa1360`](#insn-00aa1360) → [`00aa1364`](#insn-00aa1364)
- ブロック [`00aa1364`](#insn-00aa1364) 範囲 `[['00aa1364', '00aa1367']]`
  - `FALL_THROUGH` [`00aa1364`](#insn-00aa1364) → [`00aa1368`](#insn-00aa1368)
- ブロック [`00aa1368`](#insn-00aa1368) 範囲 `[['00aa1368', '00aa136b']]`
  - `FALL_THROUGH` [`00aa1368`](#insn-00aa1368) → [`00aa136c`](#insn-00aa136c)
- ブロック [`00aa136c`](#insn-00aa136c) 範囲 `[['00aa136c', '00aa136f']]`
  - `FALL_THROUGH` [`00aa136c`](#insn-00aa136c) → [`00aa1370`](#insn-00aa1370)
- ブロック [`00aa1370`](#insn-00aa1370) 範囲 `[['00aa1370', '00aa1373']]`
  - `CONDITIONAL_JUMP` [`00aa1370`](#insn-00aa1370) → [`00aa1458`](#insn-00aa1458)
  - `FALL_THROUGH` [`00aa1370`](#insn-00aa1370) → [`00aa1374`](#insn-00aa1374)
- ブロック [`00aa1374`](#insn-00aa1374) 範囲 `[['00aa1374', '00aa1377']]`
  - `FALL_THROUGH` [`00aa1374`](#insn-00aa1374) → [`00aa1378`](#insn-00aa1378)
- ブロック [`00aa1378`](#insn-00aa1378) 範囲 `[['00aa1378', '00aa137b']]`
- ブロック [`00aa137c`](#insn-00aa137c) 範囲 `[['00aa137c', '00aa137f']]`
  - `FALL_THROUGH` [`00aa137c`](#insn-00aa137c) → [`00aa1380`](#insn-00aa1380)
- ブロック [`00aa1380`](#insn-00aa1380) 範囲 `[['00aa1380', '00aa138b']]`
  - `FALL_THROUGH` [`00aa1388`](#insn-00aa1388) → [`00aa138c`](#insn-00aa138c)
- ブロック [`00aa138c`](#insn-00aa138c) 範囲 `[['00aa138c', '00aa138f']]`
  - `CONDITIONAL_JUMP` [`00aa138c`](#insn-00aa138c) → [`00aa1458`](#insn-00aa1458)
  - `FALL_THROUGH` [`00aa138c`](#insn-00aa138c) → [`00aa1390`](#insn-00aa1390)
- ブロック [`00aa1390`](#insn-00aa1390) 範囲 `[['00aa1390', '00aa1393']]`
  - `FALL_THROUGH` [`00aa1390`](#insn-00aa1390) → [`00aa1394`](#insn-00aa1394)
- ブロック [`00aa1394`](#insn-00aa1394) 範囲 `[['00aa1394', '00aa1397']]`
- ブロック [`00aa1458`](#insn-00aa1458) 範囲 `[['00aa1458', '00aa145b']]`

## 命令位置別の参照

- [`00aa0ff0`](#insn-00aa0ff0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0ff4`](#insn-00aa0ff4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0ff8`](#insn-00aa0ff8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa0ffc`](#insn-00aa0ffc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1000`](#insn-00aa1000) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1004`](#insn-00aa1004) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1014`](#insn-00aa1014) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa101c`](#insn-00aa101c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1028`](#insn-00aa1028) → [`00851550`](../00851/00851550.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00851550` · 推定シンボル `None` · 推定型 `None`
- [`00aa1038`](#insn-00aa1038) → [`00675b80`](../00675/00675b80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00675b80` · 推定シンボル `None` · 推定型 `None`
- [`00aa1048`](#insn-00aa1048) → [`00674764`](../00674/00674764.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00674764` · 推定シンボル `None` · 推定型 `None`
- [`00aa104c`](#insn-00aa104c) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1050`](#insn-00aa1050) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1054`](#insn-00aa1054) → [`00aa1064`](#insn-00aa1064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa105c`](#insn-00aa105c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1060`](#insn-00aa1060) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aa106c`](#insn-00aa106c) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1074`](#insn-00aa1074) → [`00aa1310`](#insn-00aa1310) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1088`](#insn-00aa1088) → [`00aa1098`](#insn-00aa1098) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1094`](#insn-00aa1094) → [`00aa1310`](#insn-00aa1310) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa10a0`](#insn-00aa10a0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa10a4`](#insn-00aa10a4) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa10ac`](#insn-00aa10ac) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa10b0`](#insn-00aa10b0) → [`00aa1110`](#insn-00aa1110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa10b4`](#insn-00aa10b4) → [`00aa1344`](#insn-00aa1344) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa10bc`](#insn-00aa10bc) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aa10d0`](#insn-00aa10d0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa10d4`](#insn-00aa10d4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa10d8`](#insn-00aa10d8) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00aa10e0`](#insn-00aa10e0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa10e8`](#insn-00aa10e8) → [`00aa12d4`](#insn-00aa12d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa10f0`](#insn-00aa10f0) → [`00aa112c`](#insn-00aa112c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa10f8`](#insn-00aa10f8) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aa1108`](#insn-00aa1108) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00aa110c`](#insn-00aa110c) → [`00aa1130`](#insn-00aa1130) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa111c`](#insn-00aa111c) → `00000020`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1124`](#insn-00aa1124) → [`00aa1130`](#insn-00aa1130) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1128`](#insn-00aa1128) → [`00aa12d4`](#insn-00aa12d4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1144`](#insn-00aa1144) → [`008003d0`](../00800/008003d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008003d0` · 推定シンボル `None` · 推定型 `None`
- [`00aa1160`](#insn-00aa1160) → [`00800684`](../00800/00800684.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00800684` · 推定シンボル `None` · 推定型 `None`
- [`00aa118c`](#insn-00aa118c) → [`00a65e5c`](../00a65/00a65e5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a65e5c` · 推定シンボル `None` · 推定型 `None`
- [`00aa1198`](#insn-00aa1198) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aa119c`](#insn-00aa119c) → [`00aa12cc`](#insn-00aa12cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa11a0`](#insn-00aa11a0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa11a4`](#insn-00aa11a4) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa11a8`](#insn-00aa11a8) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa11b0`](#insn-00aa11b0) → [`00aa11e0`](#insn-00aa11e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa11b4`](#insn-00aa11b4) → [`00aa1360`](#insn-00aa1360) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa11bc`](#insn-00aa11bc) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aa11d0`](#insn-00aa11d0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa11d4`](#insn-00aa11d4) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa11d8`](#insn-00aa11d8) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00aa11dc`](#insn-00aa11dc) → [`00aa11e4`](#insn-00aa11e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa11f8`](#insn-00aa11f8) → [`008003d0`](../00800/008003d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008003d0` · 推定シンボル `None` · 推定型 `None`
- [`00aa1214`](#insn-00aa1214) → [`00800684`](../00800/00800684.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00800684` · 推定シンボル `None` · 推定型 `None`
- [`00aa1240`](#insn-00aa1240) → [`00a65e5c`](../00a65/00a65e5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a65e5c` · 推定シンボル `None` · 推定型 `None`
- [`00aa124c`](#insn-00aa124c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1250`](#insn-00aa1250) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aa1254`](#insn-00aa1254) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa125c`](#insn-00aa125c) → [`00aa12cc`](#insn-00aa12cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1260`](#insn-00aa1260) → [`00aa12cc`](#insn-00aa12cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1264`](#insn-00aa1264) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1270`](#insn-00aa1270) → [`00aa12bc`](#insn-00aa12bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa127c`](#insn-00aa127c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1284`](#insn-00aa1284) → [`00aa12b0`](#insn-00aa12b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1288`](#insn-00aa1288) → [`00aa137c`](#insn-00aa137c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1290`](#insn-00aa1290) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00aa12a8`](#insn-00aa12a8) → [`00c580d0`](../00c58/00c580d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580d0` · 推定シンボル `None` · 推定型 `None`
- [`00aa12b0`](#insn-00aa12b0) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa12b8`](#insn-00aa12b8) → [`00aa12c8`](#insn-00aa12c8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa12c4`](#insn-00aa12c4) → [`00615f20`](../00615/00615f20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00615f20` · 推定シンボル `None` · 推定型 `None`
- [`00aa12cc`](#insn-00aa12cc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa12d0`](#insn-00aa12d0) → [`00aa12e0`](#insn-00aa12e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa12d8`](#insn-00aa12d8) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa12dc`](#insn-00aa12dc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00aa12e4`](#insn-00aa12e4) → [`00aa12f8`](#insn-00aa12f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa12f0`](#insn-00aa12f0) → [`00aa12e8`](#insn-00aa12e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa12f4`](#insn-00aa12f4) → [`00aa108c`](#insn-00aa108c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1308`](#insn-00aa1308) → [`00aa12f8`](#insn-00aa12f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa130c`](#insn-00aa130c) → [`00aa108c`](#insn-00aa108c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1310`](#insn-00aa1310) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1318`](#insn-00aa1318) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1320`](#insn-00aa1320) → [`00aa1458`](#insn-00aa1458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1324`](#insn-00aa1324) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1328`](#insn-00aa1328) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa132c`](#insn-00aa132c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1330`](#insn-00aa1330) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1334`](#insn-00aa1334) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1338`](#insn-00aa1338) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1344`](#insn-00aa1344) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa134c`](#insn-00aa134c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1354`](#insn-00aa1354) → [`00aa1458`](#insn-00aa1458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa135c`](#insn-00aa135c) → [`00470880`](../00470/00470880.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470880` · 推定シンボル `None` · 推定型 `None`
- [`00aa1360`](#insn-00aa1360) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1368`](#insn-00aa1368) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1370`](#insn-00aa1370) → [`00aa1458`](#insn-00aa1458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1378`](#insn-00aa1378) → [`00470880`](../00470/00470880.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470880` · 推定シンボル `None` · 推定型 `None`
- [`00aa137c`](#insn-00aa137c) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1384`](#insn-00aa1384) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa138c`](#insn-00aa138c) → [`00aa1458`](#insn-00aa1458) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aa1394`](#insn-00aa1394) → [`00470880`](../00470/00470880.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00470880` · 推定シンボル `None` · 推定型 `None`
- [`00aa1458`](#insn-00aa1458) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aa0ff0`](#insn-00aa0ff0)

~~~json
{
  "source": "00aa0ff0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0ff4`](#insn-00aa0ff4)

~~~json
{
  "source": "00aa0ff4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0ff8`](#insn-00aa0ff8)

~~~json
{
  "source": "00aa0ff8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa0ffc`](#insn-00aa0ffc)

~~~json
{
  "source": "00aa0ffc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1000`](#insn-00aa1000)

~~~json
{
  "source": "00aa1000",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1004`](#insn-00aa1004)

~~~json
{
  "source": "00aa1004",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1014`](#insn-00aa1014)

~~~json
{
  "source": "00aa1014",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa101c`](#insn-00aa101c)

~~~json
{
  "source": "00aa101c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1028`](#insn-00aa1028)

~~~json
{
  "source": "00aa1028",
  "target": "00851550",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1038`](#insn-00aa1038)

~~~json
{
  "source": "00aa1038",
  "target": "00675b80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1048`](#insn-00aa1048)

~~~json
{
  "source": "00aa1048",
  "target": "00674764",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa104c`](#insn-00aa104c)

~~~json
{
  "source": "00aa104c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1050`](#insn-00aa1050)

~~~json
{
  "source": "00aa1050",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1054`](#insn-00aa1054)

~~~json
{
  "source": "00aa1054",
  "target": "00aa1064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa105c`](#insn-00aa105c)

~~~json
{
  "source": "00aa105c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1060`](#insn-00aa1060)

~~~json
{
  "source": "00aa1060",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa106c`](#insn-00aa106c)

~~~json
{
  "source": "00aa106c",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1074`](#insn-00aa1074)

~~~json
{
  "source": "00aa1074",
  "target": "00aa1310",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1088`](#insn-00aa1088)

~~~json
{
  "source": "00aa1088",
  "target": "00aa1098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1094`](#insn-00aa1094)

~~~json
{
  "source": "00aa1094",
  "target": "00aa1310",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa10a0`](#insn-00aa10a0)

~~~json
{
  "source": "00aa10a0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa10a4`](#insn-00aa10a4)

~~~json
{
  "source": "00aa10a4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa10ac`](#insn-00aa10ac)

~~~json
{
  "source": "00aa10ac",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa10b0`](#insn-00aa10b0)

~~~json
{
  "source": "00aa10b0",
  "target": "00aa1110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa10b4`](#insn-00aa10b4)

~~~json
{
  "source": "00aa10b4",
  "target": "00aa1344",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa10bc`](#insn-00aa10bc)

~~~json
{
  "source": "00aa10bc",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa10d0`](#insn-00aa10d0)

~~~json
{
  "source": "00aa10d0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa10d4`](#insn-00aa10d4)

~~~json
{
  "source": "00aa10d4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa10d8`](#insn-00aa10d8)

~~~json
{
  "source": "00aa10d8",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa10e0`](#insn-00aa10e0)

~~~json
{
  "source": "00aa10e0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa10e8`](#insn-00aa10e8)

~~~json
{
  "source": "00aa10e8",
  "target": "00aa12d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa10f0`](#insn-00aa10f0)

~~~json
{
  "source": "00aa10f0",
  "target": "00aa112c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa10f8`](#insn-00aa10f8)

~~~json
{
  "source": "00aa10f8",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1108`](#insn-00aa1108)

~~~json
{
  "source": "00aa1108",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa110c`](#insn-00aa110c)

~~~json
{
  "source": "00aa110c",
  "target": "00aa1130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa111c`](#insn-00aa111c)

~~~json
{
  "source": "00aa111c",
  "target": "00000020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1124`](#insn-00aa1124)

~~~json
{
  "source": "00aa1124",
  "target": "00aa1130",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1128`](#insn-00aa1128)

~~~json
{
  "source": "00aa1128",
  "target": "00aa12d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1144`](#insn-00aa1144)

~~~json
{
  "source": "00aa1144",
  "target": "008003d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1160`](#insn-00aa1160)

~~~json
{
  "source": "00aa1160",
  "target": "00800684",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa118c`](#insn-00aa118c)

~~~json
{
  "source": "00aa118c",
  "target": "00a65e5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1198`](#insn-00aa1198)

~~~json
{
  "source": "00aa1198",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa119c`](#insn-00aa119c)

~~~json
{
  "source": "00aa119c",
  "target": "00aa12cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa11a0`](#insn-00aa11a0)

~~~json
{
  "source": "00aa11a0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa11a4`](#insn-00aa11a4)

~~~json
{
  "source": "00aa11a4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa11a8`](#insn-00aa11a8)

~~~json
{
  "source": "00aa11a8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa11b0`](#insn-00aa11b0)

~~~json
{
  "source": "00aa11b0",
  "target": "00aa11e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa11b4`](#insn-00aa11b4)

~~~json
{
  "source": "00aa11b4",
  "target": "00aa1360",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa11bc`](#insn-00aa11bc)

~~~json
{
  "source": "00aa11bc",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa11d0`](#insn-00aa11d0)

~~~json
{
  "source": "00aa11d0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa11d4`](#insn-00aa11d4)

~~~json
{
  "source": "00aa11d4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa11d8`](#insn-00aa11d8)

~~~json
{
  "source": "00aa11d8",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa11dc`](#insn-00aa11dc)

~~~json
{
  "source": "00aa11dc",
  "target": "00aa11e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa11f8`](#insn-00aa11f8)

~~~json
{
  "source": "00aa11f8",
  "target": "008003d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1214`](#insn-00aa1214)

~~~json
{
  "source": "00aa1214",
  "target": "00800684",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1240`](#insn-00aa1240)

~~~json
{
  "source": "00aa1240",
  "target": "00a65e5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa124c`](#insn-00aa124c)

~~~json
{
  "source": "00aa124c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1250`](#insn-00aa1250)

~~~json
{
  "source": "00aa1250",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1254`](#insn-00aa1254)

~~~json
{
  "source": "00aa1254",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa125c`](#insn-00aa125c)

~~~json
{
  "source": "00aa125c",
  "target": "00aa12cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1260`](#insn-00aa1260)

~~~json
{
  "source": "00aa1260",
  "target": "00aa12cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1264`](#insn-00aa1264)

~~~json
{
  "source": "00aa1264",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1270`](#insn-00aa1270)

~~~json
{
  "source": "00aa1270",
  "target": "00aa12bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa127c`](#insn-00aa127c)

~~~json
{
  "source": "00aa127c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1284`](#insn-00aa1284)

~~~json
{
  "source": "00aa1284",
  "target": "00aa12b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1288`](#insn-00aa1288)

~~~json
{
  "source": "00aa1288",
  "target": "00aa137c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1290`](#insn-00aa1290)

~~~json
{
  "source": "00aa1290",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa12a8`](#insn-00aa12a8)

~~~json
{
  "source": "00aa12a8",
  "target": "00c580d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa12b0`](#insn-00aa12b0)

~~~json
{
  "source": "00aa12b0",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa12b8`](#insn-00aa12b8)

~~~json
{
  "source": "00aa12b8",
  "target": "00aa12c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa12c4`](#insn-00aa12c4)

~~~json
{
  "source": "00aa12c4",
  "target": "00615f20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa12cc`](#insn-00aa12cc)

~~~json
{
  "source": "00aa12cc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa12d0`](#insn-00aa12d0)

~~~json
{
  "source": "00aa12d0",
  "target": "00aa12e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa12d8`](#insn-00aa12d8)

~~~json
{
  "source": "00aa12d8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa12dc`](#insn-00aa12dc)

~~~json
{
  "source": "00aa12dc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa12e4`](#insn-00aa12e4)

~~~json
{
  "source": "00aa12e4",
  "target": "00aa12f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa12f0`](#insn-00aa12f0)

~~~json
{
  "source": "00aa12f0",
  "target": "00aa12e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa12f4`](#insn-00aa12f4)

~~~json
{
  "source": "00aa12f4",
  "target": "00aa108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1308`](#insn-00aa1308)

~~~json
{
  "source": "00aa1308",
  "target": "00aa12f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa130c`](#insn-00aa130c)

~~~json
{
  "source": "00aa130c",
  "target": "00aa108c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1310`](#insn-00aa1310)

~~~json
{
  "source": "00aa1310",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1318`](#insn-00aa1318)

~~~json
{
  "source": "00aa1318",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1320`](#insn-00aa1320)

~~~json
{
  "source": "00aa1320",
  "target": "00aa1458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1324`](#insn-00aa1324)

~~~json
{
  "source": "00aa1324",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1328`](#insn-00aa1328)

~~~json
{
  "source": "00aa1328",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa132c`](#insn-00aa132c)

~~~json
{
  "source": "00aa132c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1330`](#insn-00aa1330)

~~~json
{
  "source": "00aa1330",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1334`](#insn-00aa1334)

~~~json
{
  "source": "00aa1334",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1338`](#insn-00aa1338)

~~~json
{
  "source": "00aa1338",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1344`](#insn-00aa1344)

~~~json
{
  "source": "00aa1344",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa134c`](#insn-00aa134c)

~~~json
{
  "source": "00aa134c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1354`](#insn-00aa1354)

~~~json
{
  "source": "00aa1354",
  "target": "00aa1458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa135c`](#insn-00aa135c)

~~~json
{
  "source": "00aa135c",
  "target": "00470880",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1360`](#insn-00aa1360)

~~~json
{
  "source": "00aa1360",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1368`](#insn-00aa1368)

~~~json
{
  "source": "00aa1368",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1370`](#insn-00aa1370)

~~~json
{
  "source": "00aa1370",
  "target": "00aa1458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1378`](#insn-00aa1378)

~~~json
{
  "source": "00aa1378",
  "target": "00470880",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa137c`](#insn-00aa137c)

~~~json
{
  "source": "00aa137c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1384`](#insn-00aa1384)

~~~json
{
  "source": "00aa1384",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa138c`](#insn-00aa138c)

~~~json
{
  "source": "00aa138c",
  "target": "00aa1458",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aa1394`](#insn-00aa1394)

~~~json
{
  "source": "00aa1394",
  "target": "00470880",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aa1458`](#insn-00aa1458)

~~~json
{
  "source": "00aa1458",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
