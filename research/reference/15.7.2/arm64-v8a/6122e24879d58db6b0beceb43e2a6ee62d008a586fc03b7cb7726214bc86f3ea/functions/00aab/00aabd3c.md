# 00aabd3c

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00aabe04`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00aab/00aabe04.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0055.md#compare-fcfb2c5c8f633b961d378368aa60ec38)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aabd3c",
  "name": "FUN_00aabd3c",
  "size": 1164,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ba93b90c370b5ae14008eaeb6a90fde7690019dfc276752ae97f42c3f2558129",
  "source_text_sha256": "ba93b90c370b5ae14008eaeb6a90fde7690019dfc276752ae97f42c3f2558129",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aabd3c",
        "00aac1c3"
      ],
      [
        "00aac28c",
        "00aac28f"
      ]
    ],
    "bytes_sha256": "fbf3f77331c2df90c75f2d87fcf420b890be67c8b8d64a1d9da84d05fbf89ee3",
    "instruction_count": 291,
    "instruction_bytes": 1164,
    "body_bytes": 1164,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

- [00aab67c](../00aab/00aab67c.md)
- [00aad8d8](../00aad/00aad8d8.md)
- [00aada14](../00aad/00aada14.md)

## 呼び出し先

- [0041fdf0](../0041f/0041fdf0.md)
- [004253b4](../00425/004253b4.md)
- [0045b734](../0045b/0045b734.md)
- [00469f7c](../00469/00469f7c.md)
- [0063fa4c](../0063f/0063fa4c.md)
- [0081f580](../0081f/0081f580.md)
- [00883d2c](../00883/00883d2c.md)
- [008847e4](../00884/008847e4.md)
- [00a25194](../00a25/00a25194.md)
- [00a25380](../00a25/00a25380.md)
- [00aab3c0](../00aab/00aab3c0.md)
- [00aab518](../00aab/00aab518.md)
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaee0](../00bda/00bdaee0.md)
- [00bdaf00](../00bda/00bdaf00.md)
- [00bdaf20](../00bda/00bdaf20.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

## 関連文字列（未確認候補）

~~~text
"array::at"
"backstage_reset1"
"uni.imgcut"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5984 bytes

~~~c

void FUN_00aabd3c(long param_1,long param_2,undefined4 param_3)

{
  ulong uVar1;
  long lVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  long *plVar5;
  int iVar6;
  long *plVar7;
  long lVar8;
  undefined8 uVar9;
  uint uVar10;
  ulong uVar11;
  long lVar12;
  long *plVar13;
  long *plVar14;
  undefined8 *puVar15;
  long lVar16;
  char *pcVar17;
  byte local_b0;
  undefined7 uStack_af;
  char cStack_a8;
  undefined7 uStack_a7;
  char local_a0;
  undefined1 uStack_9f;
  undefined6 uStack_9e;
  byte local_98 [11];
  undefined1 local_8d;
  void *local_88;
  ulong local_80;
  long *plStack_78;
  void *local_70;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  *(undefined4 *)(param_1 + 0x48) = param_3;
  plVar7 = (long *)FUN_00aab518(param_1,param_3,0xffffffff,0,0);
  lVar8 = *plVar7;
  if (plVar7[1] == lVar8) {
    uVar11 = 0;
  }
  else {
    lVar12 = 0;
    plVar14 = (long *)(param_2 + 8);
    lVar16 = -10;
    do {
      FUN_0063fa4c(&local_80,*(undefined4 *)(lVar8 + lVar12),((undefined4 *)(lVar8 + lVar12))[1],0);
      plVar5 = plStack_78;
      uVar11 = local_80;
      if (lVar16 == 0) {
        if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_0041fdf0("array::at");
        }
        goto LAB_00aac28c;
      }
      plVar13 = (long *)*plVar14;
      local_80 = 0;
      plStack_78 = (long *)0x0;
      *plVar14 = (long)plVar5;
      plVar14[-1] = uVar11;
      plVar5 = plStack_78;
      if ((plVar13 != (long *)0x0) &&
         (lVar8 = FUN_00bd6d90(0xffffffffffffffff,plVar13 + 1), plVar5 = plStack_78, lVar8 == 0)) {
        (**(code **)(*plVar13 + 0x10))(plVar13);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar13);
        plVar5 = plStack_78;
      }
      plStack_78 = plVar5;
      if ((plVar5 != (long *)0x0) &&
         (lVar8 = FUN_00bd6d90(0xffffffffffffffff,plVar5 + 1), lVar8 == 0)) {
        (**(code **)(*plVar5 + 0x10))(plVar5);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
      }
      lVar8 = *plVar7;
      uVar1 = lVar16 + 0xb;
      lVar16 = lVar16 + 1;
      plVar14 = plVar14 + 2;
      lVar12 = lVar12 + 8;
      uVar11 = plVar7[1] - lVar8 >> 3;
    } while (uVar1 < uVar11);
  }
  uVar9 = s_uni_imgcut_002a77c6._0_8_;
  uVar10 = (uint)uVar11;
  if ((int)uVar10 < 10) {
    if (uVar10 < 0xb) {
      uVar10 = 10;
    }
    pcVar17 = (char *)((ulong)local_98 | 1);
    lVar8 = -(uVar11 & 0xffffffff);
    puVar15 = (undefined8 *)(param_2 + (uVar11 & 0xffffffff) * 0x10 + 8);
    do {
      if (((DAT_00c24f78 & 1) == 0) && (iVar6 = __cxa_guard_acquire(&DAT_00c24f78), iVar6 != 0)) {
        DAT_00c24f48 = 0;
        DAT_00c24f40 = &DAT_00c24f48;
        DAT_00c24f68 = 0;
        DAT_00c24f70 = 0;
        DAT_00c24f60 = 0;
        DAT_00c24f50 = 0;
        DAT_00c24f58 = &DAT_00c24f60;
        __cxa_atexit(FUN_0045bedc,&DAT_00c24f40,&PTR_LOOP_00be5ed0);
        __cxa_guard_release(&DAT_00c24f78);
      }
      plStack_78 = (long *)((ulong)plStack_78 & 0xffffffffffffff00);
      local_80 = CONCAT71(local_80._1_7_,0xe);
      local_98[0] = 0x14;
      *(undefined4 *)((ulong)&local_80 | 1) = 0x2e696e75;
      *(undefined4 *)((long)((ulong)&local_80 | 1) + 3) = 0x676e702e;
      pcVar17[8] = 'u';
      pcVar17[9] = 't';
      *(undefined8 *)pcVar17 = uVar9;
      local_8d = 0;
      FUN_0045b734(&local_b0,&DAT_00c24f40,&local_80,local_98,0x2601);
      if (-(ulong)uVar10 == lVar8) {
        if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
          FUN_0041fdf0("array::at");
        }
        goto LAB_00aac28c;
      }
      uVar4 = CONCAT71(uStack_a7,cStack_a8);
      uVar3 = CONCAT71(uStack_af,local_b0);
      plVar7 = (long *)*puVar15;
      local_b0 = 0;
      uStack_af = 0;
      cStack_a8 = '\0';
      uStack_a7 = 0;
      *puVar15 = uVar4;
      puVar15[-1] = uVar3;
      if ((plVar7 == (long *)0x0) ||
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,plVar7 + 1), lVar16 != 0)) {
        plVar7 = (long *)CONCAT71(uStack_a7,cStack_a8);
      }
      else {
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
        plVar7 = (long *)CONCAT71(uStack_a7,cStack_a8);
      }
      if ((plVar7 != (long *)0x0) &&
         (lVar16 = FUN_00bd6d90(0xffffffffffffffff,plVar7 + 1), lVar16 == 0)) {
        (**(code **)(*plVar7 + 0x10))(plVar7);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar7);
      }
      if ((local_98[0] & 1) != 0) {
        _ZdlPv(local_88);
      }
      if ((local_80 & 1) != 0) {
        _ZdlPv(local_70);
      }
      lVar8 = lVar8 + -1;
      puVar15 = puVar15 + 2;
    } while (lVar8 != -10);
  }
  lVar8 = FUN_0081f580();
  uVar9 = FUN_008847e4(lVar8 + 0x2e48,0x329);
  iVar6 = FUN_00aab3c0(param_1,0xffffffff,0,0);
  FUN_00883d2c(uVar9,1 < iVar6);
  lVar8 = FUN_0081f580();
  uVar9 = FUN_008847e4(lVar8 + 0x2e48,0x32a);
  iVar6 = FUN_00aab3c0(param_1,0xffffffff,0,0);
  FUN_00883d2c(uVar9,1 < iVar6);
  lVar8 = FUN_0081f580();
  FUN_00a25194(lVar8 + 0x2f88,0x66);
  lVar8 = FUN_0081f580();
  uStack_9f = 0;
  local_b0 = 0x20;
  uStack_a7 = (undefined7)s_backstage_reset1_002951bc._8_8_;
  local_a0 = SUB81(s_backstage_reset1_002951bc._8_8_,7);
  uStack_af = (undefined7)s_backstage_reset1_002951bc._0_8_;
  cStack_a8 = SUB81(s_backstage_reset1_002951bc._0_8_,7);
  FUN_00469f7c(local_98,&local_b0);
  FUN_004253b4(&local_80,local_98,0,*(int *)(param_1 + 0x48) + 1);
  FUN_00a25380(lVar8 + 0x2f88,0x66,&local_80,0x1e,0);
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  if ((local_98[0] & 1) != 0) {
    _ZdlPv(local_88);
  }
  if ((local_b0 & 1) != 0) {
    _ZdlPv((void *)CONCAT62(uStack_9e,CONCAT11(uStack_9f,local_a0)));
  }
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return;
  }
LAB_00aac28c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aabd3c"></a> `00aabd3c` | `ff 03 03 d1` | sub sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00aabd40"></a> `00aabd40` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aabd44"></a> `00aabd44` | `fc 6f 07 a9` | stp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aabd48"></a> `00aabd48` | `fa 67 08 a9` | stp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aabd4c"></a> `00aabd4c` | `f8 5f 09 a9` | stp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aabd50"></a> `00aabd50` | `f6 57 0a a9` | stp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aabd54"></a> `00aabd54` | `f4 4f 0b a9` | stp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aabd58"></a> `00aabd58` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00aabd5c"></a> `00aabd5c` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aabd60"></a> `00aabd60` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00aabd64"></a> `00aabd64` | `e1 03 02 2a` | mov w1,w2 | `FALL_THROUGH`
<a id="insn-00aabd68"></a> `00aabd68` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00aabd6c"></a> `00aabd6c` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aabd70"></a> `00aabd70` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aabd74"></a> `00aabd74` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00aabd78"></a> `00aabd78` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aabd7c"></a> `00aabd7c` | `02 48 00 b9` | str w2,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00aabd80"></a> `00aabd80` | `02 00 80 12` | mov w2,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aabd84"></a> `00aabd84` | `e5 fd ff 97` | bl 0x00aab518 | `UNCONDITIONAL_CALL`
<a id="insn-00aabd88"></a> `00aabd88` | `09 20 40 a9` | ldp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00aabd8c"></a> `00aabd8c` | `fa 67 00 a9` | stp x26,x25,[sp] | `FALL_THROUGH`
<a id="insn-00aabd90"></a> `00aabd90` | `08 01 09 eb` | subs x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aabd94"></a> `00aabd94` | `80 06 00 54` | b.eq 0x00aabe64 | `CONDITIONAL_JUMP`
<a id="insn-00aabd98"></a> `00aabd98` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aabd9c"></a> `00aabd9c` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00aabda0"></a> `00aabda0` | `97 22 00 91` | add x23,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aabda4"></a> `00aabda4` | `38 01 80 92` | mov x24,#-0xa | `FALL_THROUGH`
<a id="insn-00aabda8"></a> `00aabda8` | `0a 00 00 14` | b 0x00aabdd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00aabdac"></a> `00aabdac` | `a9 22 40 a9` | ldp x9,x8,[x21] | `FALL_THROUGH`
<a id="insn-00aabdb0"></a> `00aabdb0` | `0a 2f 00 91` | add x10,x24,#0xb | `FALL_THROUGH`
<a id="insn-00aabdb4"></a> `00aabdb4` | `18 07 00 91` | add x24,x24,#0x1 | `FALL_THROUGH`
<a id="insn-00aabdb8"></a> `00aabdb8` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-00aabdbc"></a> `00aabdbc` | `73 22 00 91` | add x19,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00aabdc0"></a> `00aabdc0` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00aabdc4"></a> `00aabdc4` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00aabdc8"></a> `00aabdc8` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00aabdcc"></a> `00aabdcc` | `e9 04 00 54` | b.ls 0x00aabe68 | `CONDITIONAL_JUMP`
<a id="insn-00aabdd0"></a> `00aabdd0` | `28 01 13 8b` | add x8,x9,x19 | `FALL_THROUGH`
<a id="insn-00aabdd4"></a> `00aabdd4` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aabdd8"></a> `00aabdd8` | `00 05 40 29` | ldp w0,w1,[x8] | `FALL_THROUGH`
<a id="insn-00aabddc"></a> `00aabddc` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00aabde0"></a> `00aabde0` | `1b 4f ee 97` | bl 0x0063fa4c | `UNCONDITIONAL_CALL`
<a id="insn-00aabde4"></a> `00aabde4` | `38 1d 00 b4` | cbz x24,0x00aac188 | `CONDITIONAL_JUMP`
<a id="insn-00aabde8"></a> `00aabde8` | `a0 03 de 3c` | ldur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aabdec"></a> `00aabdec` | `f6 02 40 f9` | ldr x22,[x23] | `FALL_THROUGH`
<a id="insn-00aabdf0"></a> `00aabdf0` | `bf 7f 3e a9` | stp xzr,xzr,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aabdf4"></a> `00aabdf4` | `e0 82 9f 3c` | stur q0,[x23, #-0x8] | `FALL_THROUGH`
<a id="insn-00aabdf8"></a> `00aabdf8` | `b6 00 00 b4` | cbz x22,0x00aabe0c | `CONDITIONAL_JUMP`
<a id="insn-00aabdfc"></a> `00aabdfc` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aabe00"></a> `00aabe00` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aabe04"></a> `00aabe04` | `e3 ab 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00aabe08"></a> `00aabe08` | `c0 01 00 b4` | cbz x0,0x00aabe40 | `CONDITIONAL_JUMP`
<a id="insn-00aabe0c"></a> `00aabe0c` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aabe10"></a> `00aabe10` | `f6 fc ff b4` | cbz x22,0x00aabdac | `CONDITIONAL_JUMP`
<a id="insn-00aabe14"></a> `00aabe14` | `c1 22 00 91` | add x1,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00aabe18"></a> `00aabe18` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aabe1c"></a> `00aabe1c` | `dd ab 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00aabe20"></a> `00aabe20` | `60 fc ff b5` | cbnz x0,0x00aabdac | `CONDITIONAL_JUMP`
<a id="insn-00aabe24"></a> `00aabe24` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00aabe28"></a> `00aabe28` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aabe2c"></a> `00aabe2c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aabe30"></a> `00aabe30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aabe34"></a> `00aabe34` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aabe38"></a> `00aabe38` | `3e bc 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00aabe3c"></a> `00aabe3c` | `dc ff ff 17` | b 0x00aabdac | `UNCONDITIONAL_JUMP`
<a id="insn-00aabe40"></a> `00aabe40` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00aabe44"></a> `00aabe44` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aabe48"></a> `00aabe48` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aabe4c"></a> `00aabe4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aabe50"></a> `00aabe50` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00aabe54"></a> `00aabe54` | `37 bc 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00aabe58"></a> `00aabe58` | `b6 83 5e f8` | ldur x22,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aabe5c"></a> `00aabe5c` | `d6 fd ff b5` | cbnz x22,0x00aabe14 | `CONDITIONAL_JUMP`
<a id="insn-00aabe60"></a> `00aabe60` | `d3 ff ff 17` | b 0x00aabdac | `UNCONDITIONAL_JUMP`
<a id="insn-00aabe64"></a> `00aabe64` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00aabe68"></a> `00aabe68` | `1f 25 00 71` | cmp w8,#0x9 | `FALL_THROUGH`
<a id="insn-00aabe6c"></a> `00aabe6c` | `cc 0d 00 54` | b.gt 0x00aac024 | `CONDITIONAL_JUMP`
<a id="insn-00aabe70"></a> `00aabe70` | `aa 83 00 d1` | sub x10,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00aabe74"></a> `00aabe74` | `1f 29 00 71` | cmp w8,#0xa | `FALL_THROUGH`
<a id="insn-00aabe78"></a> `00aabe78` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00aabe7c"></a> `00aabe7c` | `5a 01 40 b2` | orr x26,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00aabe80"></a> `00aabe80` | `4a 01 80 52` | mov w10,#0xa | `FALL_THROUGH`
<a id="insn-00aabe84"></a> `00aabe84` | `eb a3 00 91` | add x11,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00aabe88"></a> `00aabe88` | `0a 81 8a 1a` | csel w10,w8,w10,hi | `FALL_THROUGH`
<a id="insn-00aabe8c"></a> `00aabe8c` | `d6 05 8e 52` | mov w22,#0x702e | `FALL_THROUGH`
<a id="insn-00aabe90"></a> `00aabe90` | `7b 01 40 b2` | orr x27,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00aabe94"></a> `00aabe94` | `3c 01 0a cb` | sub x28,x9,x10 | `FALL_THROUGH`
<a id="insn-00aabe98"></a> `00aabe98` | `8a 52 28 8b` | add x10,x20,w8, UXTW  #0x4 | `FALL_THROUGH`
<a id="insn-00aabe9c"></a> `00aabe9c` | `34 41 28 cb` | sub x20,x9,w8, UXTW  | `FALL_THROUGH`
<a id="insn-00aabea0"></a> `00aabea0` | `e8 bf ff 90` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aabea4"></a> `00aabea4` | `08 19 1f 91` | add x8,x8,#0x7c6 | `FALL_THROUGH`
<a id="insn-00aabea8"></a> `00aabea8` | `d6 ed ac 72` | movk w22,#0x676e, LSL #16 | `FALL_THROUGH`
<a id="insn-00aabeac"></a> `00aabeac` | `15 01 40 f9` | ldr x21,[x8] | `FALL_THROUGH`
<a id="insn-00aabeb0"></a> `00aabeb0` | `57 21 00 91` | add x23,x10,#0x8 | `FALL_THROUGH`
<a id="insn-00aabeb4"></a> `00aabeb4` | `99 02 80 52` | mov w25,#0x14 | `FALL_THROUGH`
<a id="insn-00aabeb8"></a> `00aabeb8` | `b3 8e 8e 52` | mov w19,#0x7475 | `FALL_THROUGH`
<a id="insn-00aabebc"></a> `00aabebc` | `05 00 00 14` | b 0x00aabed0 | `UNCONDITIONAL_JUMP`
<a id="insn-00aabec0"></a> `00aabec0` | `94 06 00 d1` | sub x20,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00aabec4"></a> `00aabec4` | `f7 42 00 91` | add x23,x23,#0x10 | `FALL_THROUGH`
<a id="insn-00aabec8"></a> `00aabec8` | `9f 2a 00 b1` | cmn x20,#0xa | `FALL_THROUGH`
<a id="insn-00aabecc"></a> `00aabecc` | `c0 0a 00 54` | b.eq 0x00aac024 | `CONDITIONAL_JUMP`
<a id="insn-00aabed0"></a> `00aabed0` | `c8 0b 00 b0` | adrp x8,0xc24000 | `FALL_THROUGH`
<a id="insn-00aabed4"></a> `00aabed4` | `08 e1 3d 91` | add x8,x8,#0xf78 | `FALL_THROUGH`
<a id="insn-00aabed8"></a> `00aabed8` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00aabedc"></a> `00aabedc` | `88 07 00 36` | tbz w8,#0x0,0x00aabfcc | `CONDITIONAL_JUMP`
<a id="insn-00aabee0"></a> `00aabee0` | `c8 01 80 52` | mov w8,#0xe | `FALL_THROUGH`
<a id="insn-00aabee4"></a> `00aabee4` | `bf 83 1e 38` | sturb wzr,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00aabee8"></a> `00aabee8` | `a8 03 1e 38` | sturb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aabeec"></a> `00aabeec` | `a8 ce 8d 52` | mov w8,#0x6e75 | `FALL_THROUGH`
<a id="insn-00aabef0"></a> `00aabef0` | `28 cd a5 72` | movk w8,#0x2e69, LSL #16 | `FALL_THROUGH`
<a id="insn-00aabef4"></a> `00aabef4` | `f9 a3 00 39` | strb w25,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aabef8"></a> `00aabef8` | `48 03 00 b9` | str w8,[x26] | `FALL_THROUGH`
<a id="insn-00aabefc"></a> `00aabefc` | `56 33 00 b8` | stur w22,[x26, #0x3] | `FALL_THROUGH`
<a id="insn-00aabf00"></a> `00aabf00` | `73 13 00 79` | strh w19,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00aabf04"></a> `00aabf04` | `75 03 00 f9` | str x21,[x27] | `FALL_THROUGH`
<a id="insn-00aabf08"></a> `00aabf08` | `ff cf 00 39` | strb wzr,[sp, #0x33] | `FALL_THROUGH`
<a id="insn-00aabf0c"></a> `00aabf0c` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aabf10"></a> `00aabf10` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00aabf14"></a> `00aabf14` | `e2 a3 00 91` | add x2,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00aabf18"></a> `00aabf18` | `c0 0b 00 b0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00aabf1c"></a> `00aabf1c` | `00 00 3d 91` | add x0,x0,#0xf40 | `FALL_THROUGH`
<a id="insn-00aabf20"></a> `00aabf20` | `23 c0 84 52` | mov w3,#0x2601 | `FALL_THROUGH`
<a id="insn-00aabf24"></a> `00aabf24` | `04 be e6 97` | bl 0x0045b734 | `UNCONDITIONAL_CALL`
<a id="insn-00aabf28"></a> `00aabf28` | `9f 03 14 eb` | cmp x28,x20 | `FALL_THROUGH`
<a id="insn-00aabf2c"></a> `00aabf2c` | `c0 13 00 54` | b.eq 0x00aac1a4 | `CONDITIONAL_JUMP`
<a id="insn-00aabf30"></a> `00aabf30` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aabf34"></a> `00aabf34` | `f8 02 40 f9` | ldr x24,[x23] | `FALL_THROUGH`
<a id="insn-00aabf38"></a> `00aabf38` | `ff 7f 01 a9` | stp xzr,xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aabf3c"></a> `00aabf3c` | `e0 82 9f 3c` | stur q0,[x23, #-0x8] | `FALL_THROUGH`
<a id="insn-00aabf40"></a> `00aabf40` | `b8 00 00 b4` | cbz x24,0x00aabf54 | `CONDITIONAL_JUMP`
<a id="insn-00aabf44"></a> `00aabf44` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00aabf48"></a> `00aabf48` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aabf4c"></a> `00aabf4c` | `91 ab 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00aabf50"></a> `00aabf50` | `c0 01 00 b4` | cbz x0,0x00aabf88 | `CONDITIONAL_JUMP`
<a id="insn-00aabf54"></a> `00aabf54` | `f8 0f 40 f9` | ldr x24,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aabf58"></a> `00aabf58` | `98 02 00 b4` | cbz x24,0x00aabfa8 | `CONDITIONAL_JUMP`
<a id="insn-00aabf5c"></a> `00aabf5c` | `01 23 00 91` | add x1,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00aabf60"></a> `00aabf60` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00aabf64"></a> `00aabf64` | `8b ab 04 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00aabf68"></a> `00aabf68` | `00 02 00 b5` | cbnz x0,0x00aabfa8 | `CONDITIONAL_JUMP`
<a id="insn-00aabf6c"></a> `00aabf6c` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00aabf70"></a> `00aabf70` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00aabf74"></a> `00aabf74` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aabf78"></a> `00aabf78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aabf7c"></a> `00aabf7c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00aabf80"></a> `00aabf80` | `ec bb 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00aabf84"></a> `00aabf84` | `09 00 00 14` | b 0x00aabfa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aabf88"></a> `00aabf88` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00aabf8c"></a> `00aabf8c` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00aabf90"></a> `00aabf90` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00aabf94"></a> `00aabf94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00aabf98"></a> `00aabf98` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00aabf9c"></a> `00aabf9c` | `e5 bb 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00aabfa0"></a> `00aabfa0` | `f8 0f 40 f9` | ldr x24,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aabfa4"></a> `00aabfa4` | `d8 fd ff b5` | cbnz x24,0x00aabf5c | `CONDITIONAL_JUMP`
<a id="insn-00aabfa8"></a> `00aabfa8` | `e8 a3 40 39` | ldrb w8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aabfac"></a> `00aabfac` | `68 00 00 36` | tbz w8,#0x0,0x00aabfb8 | `CONDITIONAL_JUMP`
<a id="insn-00aabfb0"></a> `00aabfb0` | `e0 1f 40 f9` | ldr x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aabfb4"></a> `00aabfb4` | `eb bb 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aabfb8"></a> `00aabfb8` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aabfbc"></a> `00aabfbc` | `28 f8 07 36` | tbz w8,#0x0,0x00aabec0 | `CONDITIONAL_JUMP`
<a id="insn-00aabfc0"></a> `00aabfc0` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00aabfc4"></a> `00aabfc4` | `e7 bb 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aabfc8"></a> `00aabfc8` | `be ff ff 17` | b 0x00aabec0 | `UNCONDITIONAL_JUMP`
<a id="insn-00aabfcc"></a> `00aabfcc` | `c0 0b 00 b0` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00aabfd0"></a> `00aabfd0` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00aabfd4"></a> `00aabfd4` | `cb bb 04 94` | bl 0x00bdaf00 | `UNCONDITIONAL_CALL`
<a id="insn-00aabfd8"></a> `00aabfd8` | `40 f8 ff 34` | cbz w0,0x00aabee0 | `CONDITIONAL_JUMP`
<a id="insn-00aabfdc"></a> `00aabfdc` | `c1 0b 00 b0` | adrp x1,0xc24000 | `FALL_THROUGH`
<a id="insn-00aabfe0"></a> `00aabfe0` | `21 00 3d 91` | add x1,x1,#0xf40 | `FALL_THROUGH`
<a id="insn-00aabfe4"></a> `00aabfe4` | `80 cd ff 90` | adrp x0,0x45b000 | `FALL_THROUGH`
<a id="insn-00aabfe8"></a> `00aabfe8` | `00 70 3b 91` | add x0,x0,#0xedc | `FALL_THROUGH`
<a id="insn-00aabfec"></a> `00aabfec` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aabff0"></a> `00aabff0` | `c2 09 00 d0` | adrp x2,0xbe5000 | `FALL_THROUGH`
<a id="insn-00aabff4"></a> `00aabff4` | `42 40 3b 91` | add x2,x2,#0xed0 | `FALL_THROUGH`
<a id="insn-00aabff8"></a> `00aabff8` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00aabffc"></a> `00aabffc` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-00aac000"></a> `00aac000` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-00aac004"></a> `00aac004` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-00aac008"></a> `00aac008` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00aac00c"></a> `00aac00c` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00aac010"></a> `00aac010` | `b4 bb 04 94` | bl 0x00bdaee0 | `UNCONDITIONAL_CALL`
<a id="insn-00aac014"></a> `00aac014` | `c0 0b 00 90` | adrp x0,0xc24000 | `FALL_THROUGH`
<a id="insn-00aac018"></a> `00aac018` | `00 e0 3d 91` | add x0,x0,#0xf78 | `FALL_THROUGH`
<a id="insn-00aac01c"></a> `00aac01c` | `c1 bb 04 94` | bl 0x00bdaf20 | `UNCONDITIONAL_CALL`
<a id="insn-00aac020"></a> `00aac020` | `b0 ff ff 17` | b 0x00aabee0 | `UNCONDITIONAL_JUMP`
<a id="insn-00aac024"></a> `00aac024` | `57 cd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aac028"></a> `00aac028` | `13 c9 85 52` | mov w19,#0x2e48 | `FALL_THROUGH`
<a id="insn-00aac02c"></a> `00aac02c` | `21 65 80 52` | mov w1,#0x329 | `FALL_THROUGH`
<a id="insn-00aac030"></a> `00aac030` | `00 00 13 8b` | add x0,x0,x19 | `FALL_THROUGH`
<a id="insn-00aac034"></a> `00aac034` | `ec 61 f7 97` | bl 0x008847e4 | `UNCONDITIONAL_CALL`
<a id="insn-00aac038"></a> `00aac038` | `f5 03 40 f9` | ldr x21,[sp] | `FALL_THROUGH`
<a id="insn-00aac03c"></a> `00aac03c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aac040"></a> `00aac040` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aac044"></a> `00aac044` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aac048"></a> `00aac048` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aac04c"></a> `00aac04c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aac050"></a> `00aac050` | `dc fc ff 97` | bl 0x00aab3c0 | `UNCONDITIONAL_CALL`
<a id="insn-00aac054"></a> `00aac054` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aac058"></a> `00aac058` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aac05c"></a> `00aac05c` | `e1 d7 9f 1a` | cset w1,gt | `FALL_THROUGH`
<a id="insn-00aac060"></a> `00aac060` | `33 5f f7 97` | bl 0x00883d2c | `UNCONDITIONAL_CALL`
<a id="insn-00aac064"></a> `00aac064` | `47 cd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aac068"></a> `00aac068` | `00 00 13 8b` | add x0,x0,x19 | `FALL_THROUGH`
<a id="insn-00aac06c"></a> `00aac06c` | `41 65 80 52` | mov w1,#0x32a | `FALL_THROUGH`
<a id="insn-00aac070"></a> `00aac070` | `dd 61 f7 97` | bl 0x008847e4 | `UNCONDITIONAL_CALL`
<a id="insn-00aac074"></a> `00aac074` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aac078"></a> `00aac078` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aac07c"></a> `00aac07c` | `01 00 80 12` | mov w1,#0xffffffff | `FALL_THROUGH`
<a id="insn-00aac080"></a> `00aac080` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00aac084"></a> `00aac084` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-00aac088"></a> `00aac088` | `ce fc ff 97` | bl 0x00aab3c0 | `UNCONDITIONAL_CALL`
<a id="insn-00aac08c"></a> `00aac08c` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00aac090"></a> `00aac090` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aac094"></a> `00aac094` | `e1 d7 9f 1a` | cset w1,gt | `FALL_THROUGH`
<a id="insn-00aac098"></a> `00aac098` | `25 5f f7 97` | bl 0x00883d2c | `UNCONDITIONAL_CALL`
<a id="insn-00aac09c"></a> `00aac09c` | `39 cd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aac0a0"></a> `00aac0a0` | `13 f1 85 52` | mov w19,#0x2f88 | `FALL_THROUGH`
<a id="insn-00aac0a4"></a> `00aac0a4` | `c1 0c 80 52` | mov w1,#0x66 | `FALL_THROUGH`
<a id="insn-00aac0a8"></a> `00aac0a8` | `00 00 13 8b` | add x0,x0,x19 | `FALL_THROUGH`
<a id="insn-00aac0ac"></a> `00aac0ac` | `3a e4 fd 97` | bl 0x00a25194 | `UNCONDITIONAL_CALL`
<a id="insn-00aac0b0"></a> `00aac0b0` | `34 cd f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00aac0b4"></a> `00aac0b4` | `49 bf ff b0` | adrp x9,0x295000 | `FALL_THROUGH`
<a id="insn-00aac0b8"></a> `00aac0b8` | `29 f1 06 91` | add x9,x9,#0x1bc | `FALL_THROUGH`
<a id="insn-00aac0bc"></a> `00aac0bc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00aac0c0"></a> `00aac0c0` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00aac0c4"></a> `00aac0c4` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00aac0c8"></a> `00aac0c8` | `ff 87 00 39` | strb wzr,[sp, #0x21] | `FALL_THROUGH`
<a id="insn-00aac0cc"></a> `00aac0cc` | `e8 43 00 39` | strb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aac0d0"></a> `00aac0d0` | `e0 13 81 3c` | stur q0,[sp, #0x11] | `FALL_THROUGH`
<a id="insn-00aac0d4"></a> `00aac0d4` | `e8 a3 00 91` | add x8,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00aac0d8"></a> `00aac0d8` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aac0dc"></a> `00aac0dc` | `a8 f7 e6 97` | bl 0x00469f7c | `UNCONDITIONAL_CALL`
<a id="insn-00aac0e0"></a> `00aac0e0` | `a9 4a 40 b9` | ldr w9,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00aac0e4"></a> `00aac0e4` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00aac0e8"></a> `00aac0e8` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00aac0ec"></a> `00aac0ec` | `22 05 00 11` | add w2,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00aac0f0"></a> `00aac0f0` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00aac0f4"></a> `00aac0f4` | `b0 e4 e5 97` | bl 0x004253b4 | `UNCONDITIONAL_CALL`
<a id="insn-00aac0f8"></a> `00aac0f8` | `80 02 13 8b` | add x0,x20,x19 | `FALL_THROUGH`
<a id="insn-00aac0fc"></a> `00aac0fc` | `a2 83 00 d1` | sub x2,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00aac100"></a> `00aac100` | `c1 0c 80 52` | mov w1,#0x66 | `FALL_THROUGH`
<a id="insn-00aac104"></a> `00aac104` | `c3 03 80 52` | mov w3,#0x1e | `FALL_THROUGH`
<a id="insn-00aac108"></a> `00aac108` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00aac10c"></a> `00aac10c` | `f3 07 40 f9` | ldr x19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aac110"></a> `00aac110` | `9c e4 fd 97` | bl 0x00a25380 | `UNCONDITIONAL_CALL`
<a id="insn-00aac114"></a> `00aac114` | `a8 03 5e 38` | ldurb w8,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00aac118"></a> `00aac118` | `68 02 00 37` | tbnz w8,#0x0,0x00aac164 | `CONDITIONAL_JUMP`
<a id="insn-00aac11c"></a> `00aac11c` | `e8 a3 40 39` | ldrb w8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aac120"></a> `00aac120` | `a8 02 00 37` | tbnz w8,#0x0,0x00aac174 | `CONDITIONAL_JUMP`
<a id="insn-00aac124"></a> `00aac124` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aac128"></a> `00aac128` | `68 00 00 36` | tbz w8,#0x0,0x00aac134 | `CONDITIONAL_JUMP`
<a id="insn-00aac12c"></a> `00aac12c` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aac130"></a> `00aac130` | `8c bb 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aac134"></a> `00aac134` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aac138"></a> `00aac138` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aac13c"></a> `00aac13c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aac140"></a> `00aac140` | `61 0a 00 54` | b.ne 0x00aac28c | `CONDITIONAL_JUMP`
<a id="insn-00aac144"></a> `00aac144` | `f4 4f 4b a9` | ldp x20,x19,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aac148"></a> `00aac148` | `f6 57 4a a9` | ldp x22,x21,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aac14c"></a> `00aac14c` | `f8 5f 49 a9` | ldp x24,x23,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00aac150"></a> `00aac150` | `fa 67 48 a9` | ldp x26,x25,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aac154"></a> `00aac154` | `fc 6f 47 a9` | ldp x28,x27,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00aac158"></a> `00aac158` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aac15c"></a> `00aac15c` | `ff 03 03 91` | add sp,sp,#0xc0 | `FALL_THROUGH`
<a id="insn-00aac160"></a> `00aac160` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aac164"></a> `00aac164` | `a0 03 5f f8` | ldur x0,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00aac168"></a> `00aac168` | `7e bb 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aac16c"></a> `00aac16c` | `e8 a3 40 39` | ldrb w8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aac170"></a> `00aac170` | `a8 fd 07 36` | tbz w8,#0x0,0x00aac124 | `CONDITIONAL_JUMP`
<a id="insn-00aac174"></a> `00aac174` | `e0 1f 40 f9` | ldr x0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aac178"></a> `00aac178` | `7a bb 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00aac17c"></a> `00aac17c` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aac180"></a> `00aac180` | `68 fd 07 37` | tbnz w8,#0x0,0x00aac12c | `CONDITIONAL_JUMP`
<a id="insn-00aac184"></a> `00aac184` | `ec ff ff 17` | b 0x00aac134 | `UNCONDITIONAL_JUMP`
<a id="insn-00aac188"></a> `00aac188` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00aac18c"></a> `00aac18c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aac190"></a> `00aac190` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aac194"></a> `00aac194` | `c1 07 00 54` | b.ne 0x00aac28c | `CONDITIONAL_JUMP`
<a id="insn-00aac198"></a> `00aac198` | `a0 bf ff f0` | adrp x0,0x2a3000 | `FALL_THROUGH`
<a id="insn-00aac19c"></a> `00aac19c` | `00 58 17 91` | add x0,x0,#0x5d6 | `FALL_THROUGH`
<a id="insn-00aac1a0"></a> `00aac1a0` | `14 cf e5 97` | bl 0x0041fdf0 | `CALL_TERMINATOR`
<a id="insn-00aac1a4"></a> `00aac1a4` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aac1a8"></a> `00aac1a8` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00aac1ac"></a> `00aac1ac` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aac1b0"></a> `00aac1b0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aac1b4"></a> `00aac1b4` | `c1 06 00 54` | b.ne 0x00aac28c | `CONDITIONAL_JUMP`
<a id="insn-00aac1b8"></a> `00aac1b8` | `a0 bf ff f0` | adrp x0,0x2a3000 | `FALL_THROUGH`
<a id="insn-00aac1bc"></a> `00aac1bc` | `00 58 17 91` | add x0,x0,#0x5d6 | `FALL_THROUGH`
<a id="insn-00aac1c0"></a> `00aac1c0` | `0c cf e5 97` | bl 0x0041fdf0 | `CALL_TERMINATOR`
<a id="insn-00aac28c"></a> `00aac28c` | `41 bb 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aabd3c`](#insn-00aabd3c) 範囲 `[['00aabd3c', '00aabd97']]`
  - `CONDITIONAL_JUMP` [`00aabd94`](#insn-00aabd94) → [`00aabe64`](#insn-00aabe64)
  - `FALL_THROUGH` [`00aabd94`](#insn-00aabd94) → [`00aabd98`](#insn-00aabd98)
- ブロック [`00aabd98`](#insn-00aabd98) 範囲 `[['00aabd98', '00aabdab']]`
  - `UNCONDITIONAL_JUMP` [`00aabda8`](#insn-00aabda8) → [`00aabdd0`](#insn-00aabdd0)
- ブロック [`00aabdac`](#insn-00aabdac) 範囲 `[['00aabdac', '00aabdcf']]`
  - `CONDITIONAL_JUMP` [`00aabdcc`](#insn-00aabdcc) → [`00aabe68`](#insn-00aabe68)
  - `FALL_THROUGH` [`00aabdcc`](#insn-00aabdcc) → [`00aabdd0`](#insn-00aabdd0)
- ブロック [`00aabdd0`](#insn-00aabdd0) 範囲 `[['00aabdd0', '00aabde7']]`
  - `CONDITIONAL_JUMP` [`00aabde4`](#insn-00aabde4) → [`00aac188`](#insn-00aac188)
  - `FALL_THROUGH` [`00aabde4`](#insn-00aabde4) → [`00aabde8`](#insn-00aabde8)
- ブロック [`00aabde8`](#insn-00aabde8) 範囲 `[['00aabde8', '00aabdfb']]`
  - `CONDITIONAL_JUMP` [`00aabdf8`](#insn-00aabdf8) → [`00aabe0c`](#insn-00aabe0c)
  - `FALL_THROUGH` [`00aabdf8`](#insn-00aabdf8) → [`00aabdfc`](#insn-00aabdfc)
- ブロック [`00aabdfc`](#insn-00aabdfc) 範囲 `[['00aabdfc', '00aabe0b']]`
  - `CONDITIONAL_JUMP` [`00aabe08`](#insn-00aabe08) → [`00aabe40`](#insn-00aabe40)
  - `FALL_THROUGH` [`00aabe08`](#insn-00aabe08) → [`00aabe0c`](#insn-00aabe0c)
- ブロック [`00aabe0c`](#insn-00aabe0c) 範囲 `[['00aabe0c', '00aabe13']]`
  - `CONDITIONAL_JUMP` [`00aabe10`](#insn-00aabe10) → [`00aabdac`](#insn-00aabdac)
  - `FALL_THROUGH` [`00aabe10`](#insn-00aabe10) → [`00aabe14`](#insn-00aabe14)
- ブロック [`00aabe14`](#insn-00aabe14) 範囲 `[['00aabe14', '00aabe23']]`
  - `CONDITIONAL_JUMP` [`00aabe20`](#insn-00aabe20) → [`00aabdac`](#insn-00aabdac)
  - `FALL_THROUGH` [`00aabe20`](#insn-00aabe20) → [`00aabe24`](#insn-00aabe24)
- ブロック [`00aabe24`](#insn-00aabe24) 範囲 `[['00aabe24', '00aabe3f']]`
  - `UNCONDITIONAL_JUMP` [`00aabe3c`](#insn-00aabe3c) → [`00aabdac`](#insn-00aabdac)
- ブロック [`00aabe40`](#insn-00aabe40) 範囲 `[['00aabe40', '00aabe5f']]`
  - `CONDITIONAL_JUMP` [`00aabe5c`](#insn-00aabe5c) → [`00aabe14`](#insn-00aabe14)
  - `FALL_THROUGH` [`00aabe5c`](#insn-00aabe5c) → [`00aabe60`](#insn-00aabe60)
- ブロック [`00aabe60`](#insn-00aabe60) 範囲 `[['00aabe60', '00aabe63']]`
  - `UNCONDITIONAL_JUMP` [`00aabe60`](#insn-00aabe60) → [`00aabdac`](#insn-00aabdac)
- ブロック [`00aabe64`](#insn-00aabe64) 範囲 `[['00aabe64', '00aabe67']]`
  - `FALL_THROUGH` [`00aabe64`](#insn-00aabe64) → [`00aabe68`](#insn-00aabe68)
- ブロック [`00aabe68`](#insn-00aabe68) 範囲 `[['00aabe68', '00aabe6f']]`
  - `CONDITIONAL_JUMP` [`00aabe6c`](#insn-00aabe6c) → [`00aac024`](#insn-00aac024)
  - `FALL_THROUGH` [`00aabe6c`](#insn-00aabe6c) → [`00aabe70`](#insn-00aabe70)
- ブロック [`00aabe70`](#insn-00aabe70) 範囲 `[['00aabe70', '00aabebf']]`
  - `UNCONDITIONAL_JUMP` [`00aabebc`](#insn-00aabebc) → [`00aabed0`](#insn-00aabed0)
- ブロック [`00aabec0`](#insn-00aabec0) 範囲 `[['00aabec0', '00aabecf']]`
  - `CONDITIONAL_JUMP` [`00aabecc`](#insn-00aabecc) → [`00aac024`](#insn-00aac024)
  - `FALL_THROUGH` [`00aabecc`](#insn-00aabecc) → [`00aabed0`](#insn-00aabed0)
- ブロック [`00aabed0`](#insn-00aabed0) 範囲 `[['00aabed0', '00aabedf']]`
  - `CONDITIONAL_JUMP` [`00aabedc`](#insn-00aabedc) → [`00aabfcc`](#insn-00aabfcc)
  - `FALL_THROUGH` [`00aabedc`](#insn-00aabedc) → [`00aabee0`](#insn-00aabee0)
- ブロック [`00aabee0`](#insn-00aabee0) 範囲 `[['00aabee0', '00aabf2f']]`
  - `CONDITIONAL_JUMP` [`00aabf2c`](#insn-00aabf2c) → [`00aac1a4`](#insn-00aac1a4)
  - `FALL_THROUGH` [`00aabf2c`](#insn-00aabf2c) → [`00aabf30`](#insn-00aabf30)
- ブロック [`00aabf30`](#insn-00aabf30) 範囲 `[['00aabf30', '00aabf43']]`
  - `CONDITIONAL_JUMP` [`00aabf40`](#insn-00aabf40) → [`00aabf54`](#insn-00aabf54)
  - `FALL_THROUGH` [`00aabf40`](#insn-00aabf40) → [`00aabf44`](#insn-00aabf44)
- ブロック [`00aabf44`](#insn-00aabf44) 範囲 `[['00aabf44', '00aabf53']]`
  - `CONDITIONAL_JUMP` [`00aabf50`](#insn-00aabf50) → [`00aabf88`](#insn-00aabf88)
  - `FALL_THROUGH` [`00aabf50`](#insn-00aabf50) → [`00aabf54`](#insn-00aabf54)
- ブロック [`00aabf54`](#insn-00aabf54) 範囲 `[['00aabf54', '00aabf5b']]`
  - `CONDITIONAL_JUMP` [`00aabf58`](#insn-00aabf58) → [`00aabfa8`](#insn-00aabfa8)
  - `FALL_THROUGH` [`00aabf58`](#insn-00aabf58) → [`00aabf5c`](#insn-00aabf5c)
- ブロック [`00aabf5c`](#insn-00aabf5c) 範囲 `[['00aabf5c', '00aabf6b']]`
  - `CONDITIONAL_JUMP` [`00aabf68`](#insn-00aabf68) → [`00aabfa8`](#insn-00aabfa8)
  - `FALL_THROUGH` [`00aabf68`](#insn-00aabf68) → [`00aabf6c`](#insn-00aabf6c)
- ブロック [`00aabf6c`](#insn-00aabf6c) 範囲 `[['00aabf6c', '00aabf87']]`
  - `UNCONDITIONAL_JUMP` [`00aabf84`](#insn-00aabf84) → [`00aabfa8`](#insn-00aabfa8)
- ブロック [`00aabf88`](#insn-00aabf88) 範囲 `[['00aabf88', '00aabfa7']]`
  - `CONDITIONAL_JUMP` [`00aabfa4`](#insn-00aabfa4) → [`00aabf5c`](#insn-00aabf5c)
  - `FALL_THROUGH` [`00aabfa4`](#insn-00aabfa4) → [`00aabfa8`](#insn-00aabfa8)
- ブロック [`00aabfa8`](#insn-00aabfa8) 範囲 `[['00aabfa8', '00aabfaf']]`
  - `CONDITIONAL_JUMP` [`00aabfac`](#insn-00aabfac) → [`00aabfb8`](#insn-00aabfb8)
  - `FALL_THROUGH` [`00aabfac`](#insn-00aabfac) → [`00aabfb0`](#insn-00aabfb0)
- ブロック [`00aabfb0`](#insn-00aabfb0) 範囲 `[['00aabfb0', '00aabfb7']]`
  - `FALL_THROUGH` [`00aabfb4`](#insn-00aabfb4) → [`00aabfb8`](#insn-00aabfb8)
- ブロック [`00aabfb8`](#insn-00aabfb8) 範囲 `[['00aabfb8', '00aabfbf']]`
  - `CONDITIONAL_JUMP` [`00aabfbc`](#insn-00aabfbc) → [`00aabec0`](#insn-00aabec0)
  - `FALL_THROUGH` [`00aabfbc`](#insn-00aabfbc) → [`00aabfc0`](#insn-00aabfc0)
- ブロック [`00aabfc0`](#insn-00aabfc0) 範囲 `[['00aabfc0', '00aabfcb']]`
  - `UNCONDITIONAL_JUMP` [`00aabfc8`](#insn-00aabfc8) → [`00aabec0`](#insn-00aabec0)
- ブロック [`00aabfcc`](#insn-00aabfcc) 範囲 `[['00aabfcc', '00aabfdb']]`
  - `CONDITIONAL_JUMP` [`00aabfd8`](#insn-00aabfd8) → [`00aabee0`](#insn-00aabee0)
  - `FALL_THROUGH` [`00aabfd8`](#insn-00aabfd8) → [`00aabfdc`](#insn-00aabfdc)
- ブロック [`00aabfdc`](#insn-00aabfdc) 範囲 `[['00aabfdc', '00aac023']]`
  - `UNCONDITIONAL_JUMP` [`00aac020`](#insn-00aac020) → [`00aabee0`](#insn-00aabee0)
- ブロック [`00aac024`](#insn-00aac024) 範囲 `[['00aac024', '00aac11b']]`
  - `CONDITIONAL_JUMP` [`00aac118`](#insn-00aac118) → [`00aac164`](#insn-00aac164)
  - `FALL_THROUGH` [`00aac118`](#insn-00aac118) → [`00aac11c`](#insn-00aac11c)
- ブロック [`00aac11c`](#insn-00aac11c) 範囲 `[['00aac11c', '00aac123']]`
  - `CONDITIONAL_JUMP` [`00aac120`](#insn-00aac120) → [`00aac174`](#insn-00aac174)
  - `FALL_THROUGH` [`00aac120`](#insn-00aac120) → [`00aac124`](#insn-00aac124)
- ブロック [`00aac124`](#insn-00aac124) 範囲 `[['00aac124', '00aac12b']]`
  - `CONDITIONAL_JUMP` [`00aac128`](#insn-00aac128) → [`00aac134`](#insn-00aac134)
  - `FALL_THROUGH` [`00aac128`](#insn-00aac128) → [`00aac12c`](#insn-00aac12c)
- ブロック [`00aac12c`](#insn-00aac12c) 範囲 `[['00aac12c', '00aac133']]`
  - `FALL_THROUGH` [`00aac130`](#insn-00aac130) → [`00aac134`](#insn-00aac134)
- ブロック [`00aac134`](#insn-00aac134) 範囲 `[['00aac134', '00aac143']]`
  - `CONDITIONAL_JUMP` [`00aac140`](#insn-00aac140) → [`00aac28c`](#insn-00aac28c)
  - `FALL_THROUGH` [`00aac140`](#insn-00aac140) → [`00aac144`](#insn-00aac144)
- ブロック [`00aac144`](#insn-00aac144) 範囲 `[['00aac144', '00aac163']]`
- ブロック [`00aac164`](#insn-00aac164) 範囲 `[['00aac164', '00aac173']]`
  - `CONDITIONAL_JUMP` [`00aac170`](#insn-00aac170) → [`00aac124`](#insn-00aac124)
  - `FALL_THROUGH` [`00aac170`](#insn-00aac170) → [`00aac174`](#insn-00aac174)
- ブロック [`00aac174`](#insn-00aac174) 範囲 `[['00aac174', '00aac183']]`
  - `CONDITIONAL_JUMP` [`00aac180`](#insn-00aac180) → [`00aac12c`](#insn-00aac12c)
  - `FALL_THROUGH` [`00aac180`](#insn-00aac180) → [`00aac184`](#insn-00aac184)
- ブロック [`00aac184`](#insn-00aac184) 範囲 `[['00aac184', '00aac187']]`
  - `UNCONDITIONAL_JUMP` [`00aac184`](#insn-00aac184) → [`00aac134`](#insn-00aac134)
- ブロック [`00aac188`](#insn-00aac188) 範囲 `[['00aac188', '00aac197']]`
  - `CONDITIONAL_JUMP` [`00aac194`](#insn-00aac194) → [`00aac28c`](#insn-00aac28c)
  - `FALL_THROUGH` [`00aac194`](#insn-00aac194) → [`00aac198`](#insn-00aac198)
- ブロック [`00aac198`](#insn-00aac198) 範囲 `[['00aac198', '00aac1a3']]`
- ブロック [`00aac1a4`](#insn-00aac1a4) 範囲 `[['00aac1a4', '00aac1b7']]`
  - `CONDITIONAL_JUMP` [`00aac1b4`](#insn-00aac1b4) → [`00aac28c`](#insn-00aac28c)
  - `FALL_THROUGH` [`00aac1b4`](#insn-00aac1b4) → [`00aac1b8`](#insn-00aac1b8)
- ブロック [`00aac1b8`](#insn-00aac1b8) 範囲 `[['00aac1b8', '00aac1c3']]`
- ブロック [`00aac28c`](#insn-00aac28c) 範囲 `[['00aac28c', '00aac28f']]`

## 命令位置別の参照

- [`00aabd40`](#insn-00aabd40) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabd44`](#insn-00aabd44) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabd48`](#insn-00aabd48) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabd4c`](#insn-00aabd4c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabd50`](#insn-00aabd50) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabd54`](#insn-00aabd54) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabd78`](#insn-00aabd78) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabd84`](#insn-00aabd84) → [`00aab518`](00aab518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aab518` · 推定シンボル `None` · 推定型 `None`
- [`00aabd8c`](#insn-00aabd8c) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabd94`](#insn-00aabd94) → [`00aabe64`](#insn-00aabe64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabda8`](#insn-00aabda8) → [`00aabdd0`](#insn-00aabdd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabdcc`](#insn-00aabdcc) → [`00aabe68`](#insn-00aabe68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabde0`](#insn-00aabde0) → [`0063fa4c`](../0063f/0063fa4c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0063fa4c` · 推定シンボル `None` · 推定型 `None`
- [`00aabde4`](#insn-00aabde4) → [`00aac188`](#insn-00aac188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabde8`](#insn-00aabde8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabdf0`](#insn-00aabdf0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabdf8`](#insn-00aabdf8) → [`00aabe0c`](#insn-00aabe0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabe04`](#insn-00aabe04) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00aabe08`](#insn-00aabe08) → [`00aabe40`](#insn-00aabe40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabe0c`](#insn-00aabe0c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabe10`](#insn-00aabe10) → [`00aabdac`](#insn-00aabdac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabe1c`](#insn-00aabe1c) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00aabe20`](#insn-00aabe20) → [`00aabdac`](#insn-00aabdac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabe38`](#insn-00aabe38) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00aabe3c`](#insn-00aabe3c) → [`00aabdac`](#insn-00aabdac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabe54`](#insn-00aabe54) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00aabe58`](#insn-00aabe58) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabe5c`](#insn-00aabe5c) → [`00aabe14`](#insn-00aabe14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabe60`](#insn-00aabe60) → [`00aabdac`](#insn-00aabdac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabe6c`](#insn-00aabe6c) → [`00aac024`](#insn-00aac024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabeac`](#insn-00aabeac) → `002a77c6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aabebc`](#insn-00aabebc) → [`00aabed0`](#insn-00aabed0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabecc`](#insn-00aabecc) → [`00aac024`](#insn-00aac024) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabed8`](#insn-00aabed8) → `00c24f78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aabedc`](#insn-00aabedc) → [`00aabfcc`](#insn-00aabfcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabee4`](#insn-00aabee4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabee8`](#insn-00aabee8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabef4`](#insn-00aabef4) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabf08`](#insn-00aabf08) → `Stack[-0x8d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabf1c`](#insn-00aabf1c) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aabf24`](#insn-00aabf24) → [`0045b734`](../0045b/0045b734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0045b734` · 推定シンボル `None` · 推定型 `None`
- [`00aabf2c`](#insn-00aabf2c) → [`00aac1a4`](#insn-00aac1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabf30`](#insn-00aabf30) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabf38`](#insn-00aabf38) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabf40`](#insn-00aabf40) → [`00aabf54`](#insn-00aabf54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabf4c`](#insn-00aabf4c) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00aabf50`](#insn-00aabf50) → [`00aabf88`](#insn-00aabf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabf54`](#insn-00aabf54) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabf58`](#insn-00aabf58) → [`00aabfa8`](#insn-00aabfa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabf64`](#insn-00aabf64) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00aabf68`](#insn-00aabf68) → [`00aabfa8`](#insn-00aabfa8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabf80`](#insn-00aabf80) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00aabf84`](#insn-00aabf84) → [`00aabfa8`](#insn-00aabfa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabf9c`](#insn-00aabf9c) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00aabfa0`](#insn-00aabfa0) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabfa4`](#insn-00aabfa4) → [`00aabf5c`](#insn-00aabf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabfa8`](#insn-00aabfa8) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabfac`](#insn-00aabfac) → [`00aabfb8`](#insn-00aabfb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabfb0`](#insn-00aabfb0) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabfb4`](#insn-00aabfb4) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aabfb8`](#insn-00aabfb8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabfbc`](#insn-00aabfbc) → [`00aabec0`](#insn-00aabec0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabfc0`](#insn-00aabfc0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabfc4`](#insn-00aabfc4) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aabfc8`](#insn-00aabfc8) → [`00aabec0`](#insn-00aabec0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabfd0`](#insn-00aabfd0) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aabfd4`](#insn-00aabfd4) → [`00bdaf00`](../00bda/00bdaf00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf00` · 推定シンボル `None` · 推定型 `None`
- [`00aabfd8`](#insn-00aabfd8) → [`00aabee0`](#insn-00aabee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aabfe0`](#insn-00aabfe0) → `00c24f40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aabfe8`](#insn-00aabfe8) → [`0045bedc`](../0045b/0045bedc.md) · `PARAM` · `ANALYSIS` · 関数 `0045bedc` · 推定シンボル `None` · 推定型 `None`
- [`00aabff4`](#insn-00aabff4) → `00be5ed0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00aabff8`](#insn-00aabff8) → `00c24f48`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aabffc`](#insn-00aabffc) → `00c24f40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aabffc`](#insn-00aabffc) → `00c24f48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aac004`](#insn-00aac004) → `00c24f68`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aac004`](#insn-00aac004) → `00c24f70`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aac008`](#insn-00aac008) → `00c24f60`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aac00c`](#insn-00aac00c) → `00c24f50`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aac00c`](#insn-00aac00c) → `00c24f58`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aac00c`](#insn-00aac00c) → `00c24f60`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00aac010`](#insn-00aac010) → [`00bdaee0`](../00bda/00bdaee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaee0` · 推定シンボル `None` · 推定型 `None`
- [`00aac018`](#insn-00aac018) → `00c24f78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00aac01c`](#insn-00aac01c) → [`00bdaf20`](../00bda/00bdaf20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf20` · 推定シンボル `None` · 推定型 `None`
- [`00aac020`](#insn-00aac020) → [`00aabee0`](#insn-00aabee0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac024`](#insn-00aac024) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aac034`](#insn-00aac034) → [`008847e4`](../00884/008847e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008847e4` · 推定シンボル `None` · 推定型 `None`
- [`00aac038`](#insn-00aac038) → `Stack[-0xc0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac050`](#insn-00aac050) → [`00aab3c0`](00aab3c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aab3c0` · 推定シンボル `None` · 推定型 `None`
- [`00aac060`](#insn-00aac060) → [`00883d2c`](../00883/00883d2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00883d2c` · 推定シンボル `None` · 推定型 `None`
- [`00aac064`](#insn-00aac064) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aac070`](#insn-00aac070) → [`008847e4`](../00884/008847e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008847e4` · 推定シンボル `None` · 推定型 `None`
- [`00aac088`](#insn-00aac088) → [`00aab3c0`](00aab3c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00aab3c0` · 推定シンボル `None` · 推定型 `None`
- [`00aac098`](#insn-00aac098) → [`00883d2c`](../00883/00883d2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00883d2c` · 推定シンボル `None` · 推定型 `None`
- [`00aac09c`](#insn-00aac09c) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aac0ac`](#insn-00aac0ac) → [`00a25194`](../00a25/00a25194.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a25194` · 推定シンボル `None` · 推定型 `None`
- [`00aac0b0`](#insn-00aac0b0) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00aac0c0`](#insn-00aac0c0) → `002951bc`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aac0c8`](#insn-00aac0c8) → `Stack[-0x9f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac0cc`](#insn-00aac0cc) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac0d0`](#insn-00aac0d0) → `Stack[-0xaf]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac0dc`](#insn-00aac0dc) → [`00469f7c`](../00469/00469f7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00469f7c` · 推定シンボル `None` · 推定型 `None`
- [`00aac0f4`](#insn-00aac0f4) → [`004253b4`](../00425/004253b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004253b4` · 推定シンボル `None` · 推定型 `None`
- [`00aac10c`](#insn-00aac10c) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac110`](#insn-00aac110) → [`00a25380`](../00a25/00a25380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a25380` · 推定シンボル `None` · 推定型 `None`
- [`00aac114`](#insn-00aac114) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac118`](#insn-00aac118) → [`00aac164`](#insn-00aac164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac11c`](#insn-00aac11c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac120`](#insn-00aac120) → [`00aac174`](#insn-00aac174) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac124`](#insn-00aac124) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac128`](#insn-00aac128) → [`00aac134`](#insn-00aac134) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac12c`](#insn-00aac12c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac130`](#insn-00aac130) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aac138`](#insn-00aac138) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac140`](#insn-00aac140) → [`00aac28c`](#insn-00aac28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac144`](#insn-00aac144) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac148`](#insn-00aac148) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac14c`](#insn-00aac14c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac150`](#insn-00aac150) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac154`](#insn-00aac154) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac158`](#insn-00aac158) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac164`](#insn-00aac164) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac168`](#insn-00aac168) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aac16c`](#insn-00aac16c) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac170`](#insn-00aac170) → [`00aac124`](#insn-00aac124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac174`](#insn-00aac174) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac178`](#insn-00aac178) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00aac17c`](#insn-00aac17c) → `Stack[-0xb0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac180`](#insn-00aac180) → [`00aac12c`](#insn-00aac12c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac184`](#insn-00aac184) → [`00aac134`](#insn-00aac134) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac18c`](#insn-00aac18c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac194`](#insn-00aac194) → [`00aac28c`](#insn-00aac28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac19c`](#insn-00aac19c) → `002a35d6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aac1a0`](#insn-00aac1a0) → [`0041fdf0`](../0041f/0041fdf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041fdf0` · 推定シンボル `None` · 推定型 `None`
- [`00aac1a4`](#insn-00aac1a4) → `Stack[-0xb8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac1ac`](#insn-00aac1ac) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac1b4`](#insn-00aac1b4) → [`00aac28c`](#insn-00aac28c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac1bc`](#insn-00aac1bc) → `002a35d6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aac1c0`](#insn-00aac1c0) → [`0041fdf0`](../0041f/0041fdf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041fdf0` · 推定シンボル `None` · 推定型 `None`
- [`00aac28c`](#insn-00aac28c) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aabd40`](#insn-00aabd40)

~~~json
{
  "source": "00aabd40",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabd44`](#insn-00aabd44)

~~~json
{
  "source": "00aabd44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabd48`](#insn-00aabd48)

~~~json
{
  "source": "00aabd48",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabd4c`](#insn-00aabd4c)

~~~json
{
  "source": "00aabd4c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabd50`](#insn-00aabd50)

~~~json
{
  "source": "00aabd50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabd54`](#insn-00aabd54)

~~~json
{
  "source": "00aabd54",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabd78`](#insn-00aabd78)

~~~json
{
  "source": "00aabd78",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabd84`](#insn-00aabd84)

~~~json
{
  "source": "00aabd84",
  "target": "00aab518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabd8c`](#insn-00aabd8c)

~~~json
{
  "source": "00aabd8c",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabd94`](#insn-00aabd94)

~~~json
{
  "source": "00aabd94",
  "target": "00aabe64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabda8`](#insn-00aabda8)

~~~json
{
  "source": "00aabda8",
  "target": "00aabdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabdcc`](#insn-00aabdcc)

~~~json
{
  "source": "00aabdcc",
  "target": "00aabe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabde0`](#insn-00aabde0)

~~~json
{
  "source": "00aabde0",
  "target": "0063fa4c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabde4`](#insn-00aabde4)

~~~json
{
  "source": "00aabde4",
  "target": "00aac188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabde8`](#insn-00aabde8)

~~~json
{
  "source": "00aabde8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabdf0`](#insn-00aabdf0)

~~~json
{
  "source": "00aabdf0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabdf8`](#insn-00aabdf8)

~~~json
{
  "source": "00aabdf8",
  "target": "00aabe0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabe04`](#insn-00aabe04)

~~~json
{
  "source": "00aabe04",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabe08`](#insn-00aabe08)

~~~json
{
  "source": "00aabe08",
  "target": "00aabe40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabe0c`](#insn-00aabe0c)

~~~json
{
  "source": "00aabe0c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabe10`](#insn-00aabe10)

~~~json
{
  "source": "00aabe10",
  "target": "00aabdac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabe1c`](#insn-00aabe1c)

~~~json
{
  "source": "00aabe1c",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabe20`](#insn-00aabe20)

~~~json
{
  "source": "00aabe20",
  "target": "00aabdac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabe38`](#insn-00aabe38)

~~~json
{
  "source": "00aabe38",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabe3c`](#insn-00aabe3c)

~~~json
{
  "source": "00aabe3c",
  "target": "00aabdac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabe54`](#insn-00aabe54)

~~~json
{
  "source": "00aabe54",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabe58`](#insn-00aabe58)

~~~json
{
  "source": "00aabe58",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabe5c`](#insn-00aabe5c)

~~~json
{
  "source": "00aabe5c",
  "target": "00aabe14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabe60`](#insn-00aabe60)

~~~json
{
  "source": "00aabe60",
  "target": "00aabdac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabe6c`](#insn-00aabe6c)

~~~json
{
  "source": "00aabe6c",
  "target": "00aac024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabeac`](#insn-00aabeac)

~~~json
{
  "source": "00aabeac",
  "target": "002a77c6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a77c6",
  "offset": 0,
  "size": 11,
  "datatype": "string",
  "bytes": "756e692e696d6763757400",
  "capture_start": "002a77c6",
  "capture_bytes": 11,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aabebc`](#insn-00aabebc)

~~~json
{
  "source": "00aabebc",
  "target": "00aabed0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabecc`](#insn-00aabecc)

~~~json
{
  "source": "00aabecc",
  "target": "00aac024",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabed8`](#insn-00aabed8)

~~~json
{
  "source": "00aabed8",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aabedc`](#insn-00aabedc)

~~~json
{
  "source": "00aabedc",
  "target": "00aabfcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabee4`](#insn-00aabee4)

~~~json
{
  "source": "00aabee4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabee8`](#insn-00aabee8)

~~~json
{
  "source": "00aabee8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabef4`](#insn-00aabef4)

~~~json
{
  "source": "00aabef4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabf08`](#insn-00aabf08)

~~~json
{
  "source": "00aabf08",
  "target": "Stack[-0x8d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabf1c`](#insn-00aabf1c)

~~~json
{
  "source": "00aabf1c",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aabf24`](#insn-00aabf24)

~~~json
{
  "source": "00aabf24",
  "target": "0045b734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabf2c`](#insn-00aabf2c)

~~~json
{
  "source": "00aabf2c",
  "target": "00aac1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabf30`](#insn-00aabf30)

~~~json
{
  "source": "00aabf30",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabf38`](#insn-00aabf38)

~~~json
{
  "source": "00aabf38",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabf40`](#insn-00aabf40)

~~~json
{
  "source": "00aabf40",
  "target": "00aabf54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabf4c`](#insn-00aabf4c)

~~~json
{
  "source": "00aabf4c",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabf50`](#insn-00aabf50)

~~~json
{
  "source": "00aabf50",
  "target": "00aabf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabf54`](#insn-00aabf54)

~~~json
{
  "source": "00aabf54",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabf58`](#insn-00aabf58)

~~~json
{
  "source": "00aabf58",
  "target": "00aabfa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabf64`](#insn-00aabf64)

~~~json
{
  "source": "00aabf64",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabf68`](#insn-00aabf68)

~~~json
{
  "source": "00aabf68",
  "target": "00aabfa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabf80`](#insn-00aabf80)

~~~json
{
  "source": "00aabf80",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabf84`](#insn-00aabf84)

~~~json
{
  "source": "00aabf84",
  "target": "00aabfa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabf9c`](#insn-00aabf9c)

~~~json
{
  "source": "00aabf9c",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabfa0`](#insn-00aabfa0)

~~~json
{
  "source": "00aabfa0",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabfa4`](#insn-00aabfa4)

~~~json
{
  "source": "00aabfa4",
  "target": "00aabf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabfa8`](#insn-00aabfa8)

~~~json
{
  "source": "00aabfa8",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabfac`](#insn-00aabfac)

~~~json
{
  "source": "00aabfac",
  "target": "00aabfb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabfb0`](#insn-00aabfb0)

~~~json
{
  "source": "00aabfb0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabfb4`](#insn-00aabfb4)

~~~json
{
  "source": "00aabfb4",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabfb8`](#insn-00aabfb8)

~~~json
{
  "source": "00aabfb8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabfbc`](#insn-00aabfbc)

~~~json
{
  "source": "00aabfbc",
  "target": "00aabec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabfc0`](#insn-00aabfc0)

~~~json
{
  "source": "00aabfc0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabfc4`](#insn-00aabfc4)

~~~json
{
  "source": "00aabfc4",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabfc8`](#insn-00aabfc8)

~~~json
{
  "source": "00aabfc8",
  "target": "00aabec0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabfd0`](#insn-00aabfd0)

~~~json
{
  "source": "00aabfd0",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aabfd4`](#insn-00aabfd4)

~~~json
{
  "source": "00aabfd4",
  "target": "00bdaf00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabfd8`](#insn-00aabfd8)

~~~json
{
  "source": "00aabfd8",
  "target": "00aabee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aabfe0`](#insn-00aabfe0)

~~~json
{
  "source": "00aabfe0",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aabfe8`](#insn-00aabfe8)

~~~json
{
  "source": "00aabfe8",
  "target": "0045bedc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aabff4`](#insn-00aabff4)

~~~json
{
  "source": "00aabff4",
  "target": "00be5ed0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00be5ed0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00aabff8`](#insn-00aabff8)

~~~json
{
  "source": "00aabff8",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aabffc`](#insn-00aabffc)

~~~json
{
  "source": "00aabffc",
  "target": "00c24f40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aabffc`](#insn-00aabffc)

~~~json
{
  "source": "00aabffc",
  "target": "00c24f48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aac004`](#insn-00aac004)

~~~json
{
  "source": "00aac004",
  "target": "00c24f68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aac004`](#insn-00aac004)

~~~json
{
  "source": "00aac004",
  "target": "00c24f70",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f70",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aac008`](#insn-00aac008)

~~~json
{
  "source": "00aac008",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aac00c`](#insn-00aac00c)

~~~json
{
  "source": "00aac00c",
  "target": "00c24f50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aac00c`](#insn-00aac00c)

~~~json
{
  "source": "00aac00c",
  "target": "00c24f58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aac00c`](#insn-00aac00c)

~~~json
{
  "source": "00aac00c",
  "target": "00c24f60",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f60",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aac010`](#insn-00aac010)

~~~json
{
  "source": "00aac010",
  "target": "00bdaee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac018`](#insn-00aac018)

~~~json
{
  "source": "00aac018",
  "target": "00c24f78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c24f78",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00aac01c`](#insn-00aac01c)

~~~json
{
  "source": "00aac01c",
  "target": "00bdaf20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac020`](#insn-00aac020)

~~~json
{
  "source": "00aac020",
  "target": "00aabee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac024`](#insn-00aac024)

~~~json
{
  "source": "00aac024",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac034`](#insn-00aac034)

~~~json
{
  "source": "00aac034",
  "target": "008847e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac038`](#insn-00aac038)

~~~json
{
  "source": "00aac038",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac050`](#insn-00aac050)

~~~json
{
  "source": "00aac050",
  "target": "00aab3c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac060`](#insn-00aac060)

~~~json
{
  "source": "00aac060",
  "target": "00883d2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac064`](#insn-00aac064)

~~~json
{
  "source": "00aac064",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac070`](#insn-00aac070)

~~~json
{
  "source": "00aac070",
  "target": "008847e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac088`](#insn-00aac088)

~~~json
{
  "source": "00aac088",
  "target": "00aab3c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac098`](#insn-00aac098)

~~~json
{
  "source": "00aac098",
  "target": "00883d2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac09c`](#insn-00aac09c)

~~~json
{
  "source": "00aac09c",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac0ac`](#insn-00aac0ac)

~~~json
{
  "source": "00aac0ac",
  "target": "00a25194",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac0b0`](#insn-00aac0b0)

~~~json
{
  "source": "00aac0b0",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac0c0`](#insn-00aac0c0)

~~~json
{
  "source": "00aac0c0",
  "target": "002951bc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002951bc",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "6261636b73746167655f72657365743100",
  "capture_start": "002951bc",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aac0c8`](#insn-00aac0c8)

~~~json
{
  "source": "00aac0c8",
  "target": "Stack[-0x9f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac0cc`](#insn-00aac0cc)

~~~json
{
  "source": "00aac0cc",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac0d0`](#insn-00aac0d0)

~~~json
{
  "source": "00aac0d0",
  "target": "Stack[-0xaf]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac0dc`](#insn-00aac0dc)

~~~json
{
  "source": "00aac0dc",
  "target": "00469f7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac0f4`](#insn-00aac0f4)

~~~json
{
  "source": "00aac0f4",
  "target": "004253b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac10c`](#insn-00aac10c)

~~~json
{
  "source": "00aac10c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac110`](#insn-00aac110)

~~~json
{
  "source": "00aac110",
  "target": "00a25380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac114`](#insn-00aac114)

~~~json
{
  "source": "00aac114",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac118`](#insn-00aac118)

~~~json
{
  "source": "00aac118",
  "target": "00aac164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac11c`](#insn-00aac11c)

~~~json
{
  "source": "00aac11c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac120`](#insn-00aac120)

~~~json
{
  "source": "00aac120",
  "target": "00aac174",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac124`](#insn-00aac124)

~~~json
{
  "source": "00aac124",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac128`](#insn-00aac128)

~~~json
{
  "source": "00aac128",
  "target": "00aac134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac12c`](#insn-00aac12c)

~~~json
{
  "source": "00aac12c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac130`](#insn-00aac130)

~~~json
{
  "source": "00aac130",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac138`](#insn-00aac138)

~~~json
{
  "source": "00aac138",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac140`](#insn-00aac140)

~~~json
{
  "source": "00aac140",
  "target": "00aac28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac144`](#insn-00aac144)

~~~json
{
  "source": "00aac144",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac148`](#insn-00aac148)

~~~json
{
  "source": "00aac148",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac14c`](#insn-00aac14c)

~~~json
{
  "source": "00aac14c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac150`](#insn-00aac150)

~~~json
{
  "source": "00aac150",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac154`](#insn-00aac154)

~~~json
{
  "source": "00aac154",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac158`](#insn-00aac158)

~~~json
{
  "source": "00aac158",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac164`](#insn-00aac164)

~~~json
{
  "source": "00aac164",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac168`](#insn-00aac168)

~~~json
{
  "source": "00aac168",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac16c`](#insn-00aac16c)

~~~json
{
  "source": "00aac16c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac170`](#insn-00aac170)

~~~json
{
  "source": "00aac170",
  "target": "00aac124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac174`](#insn-00aac174)

~~~json
{
  "source": "00aac174",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac178`](#insn-00aac178)

~~~json
{
  "source": "00aac178",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac17c`](#insn-00aac17c)

~~~json
{
  "source": "00aac17c",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac180`](#insn-00aac180)

~~~json
{
  "source": "00aac180",
  "target": "00aac12c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac184`](#insn-00aac184)

~~~json
{
  "source": "00aac184",
  "target": "00aac134",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac18c`](#insn-00aac18c)

~~~json
{
  "source": "00aac18c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac194`](#insn-00aac194)

~~~json
{
  "source": "00aac194",
  "target": "00aac28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac19c`](#insn-00aac19c)

~~~json
{
  "source": "00aac19c",
  "target": "002a35d6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a35d6",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "61727261793a3a617400",
  "capture_start": "002a35d6",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aac1a0`](#insn-00aac1a0)

~~~json
{
  "source": "00aac1a0",
  "target": "0041fdf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac1a4`](#insn-00aac1a4)

~~~json
{
  "source": "00aac1a4",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac1ac`](#insn-00aac1ac)

~~~json
{
  "source": "00aac1ac",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac1b4`](#insn-00aac1b4)

~~~json
{
  "source": "00aac1b4",
  "target": "00aac28c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac1bc`](#insn-00aac1bc)

~~~json
{
  "source": "00aac1bc",
  "target": "002a35d6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a35d6",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "61727261793a3a617400",
  "capture_start": "002a35d6",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aac1c0`](#insn-00aac1c0)

~~~json
{
  "source": "00aac1c0",
  "target": "0041fdf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac28c`](#insn-00aac28c)

~~~json
{
  "source": "00aac28c",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
