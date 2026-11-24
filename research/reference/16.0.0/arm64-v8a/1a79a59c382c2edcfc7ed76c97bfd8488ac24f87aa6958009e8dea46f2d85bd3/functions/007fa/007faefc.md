# 007faefc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0133.md#review-27f212fbba9467d097c5dd25b5d486e0)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `007faf3c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/007fa/007faf3c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0040.md#compare-733c97fd3eefb119c8e8fd82802d4578)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "007faefc",
  "name": "FUN_007faefc",
  "size": 428,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "1a3cc31cadc09f8e917d942f1e6c39f44e63b5b2a51cedb72907b910ae2446ef",
  "source_text_sha256": "1a3cc31cadc09f8e917d942f1e6c39f44e63b5b2a51cedb72907b910ae2446ef",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "007faefc",
        "007fb0a3"
      ],
      [
        "007fb0d0",
        "007fb0d3"
      ]
    ],
    "bytes_sha256": "a0ff7d3f9c65df23537d11cfd19dc1746f98df0c359385662294f7b2777ae7ff",
    "instruction_count": 107,
    "instruction_bytes": 428,
    "body_bytes": 428,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [007fa950](../007fa/007fa950.md)
- [007fbdc8](../007fb/007fbdc8.md)

## 呼び出し先

- [0047e89c](../0047e/0047e89c.md)
- [00664860](../00664/00664860.md)
- [00744158](../00744/00744158.md)
- [00c538e0](../00c53/00c538e0.md)
- [00c57a30](../00c57/00c57a30.md)
- [00c57a50](../00c57/00c57a50.md)
- [00c57a70](../00c57/00c57a70.md)
- [00c57a80](../00c57/00c57a80.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2011 bytes

~~~c

void FUN_007faefc(long *param_1)

{
  undefined4 uVar1;
  long lVar2;
  undefined8 uVar3;
  long *plVar4;
  int iVar5;
  ulong uVar6;
  ulong uVar7;
  long *plVar8;
  long lVar9;
  byte local_68 [16];
  void *local_58;
  undefined8 local_50;
  long *plStack_48;
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  lVar9 = *param_1;
  uVar6 = FUN_00744158(lVar9 + 0xbe0,*(undefined4 *)(lVar9 + 0xa24));
  uVar1 = *(undefined4 *)(lVar9 + (long)(int)uVar6 * 4 + 0x49934);
  uVar7 = uVar6;
  if ((DAT_00ca4b38 & 1) == 0) {
    iVar5 = __cxa_guard_acquire(&DAT_00ca4b38);
    uVar7 = uVar6 & 0xffffffff;
    if (iVar5 != 0) {
      DAT_00ca4b08 = 0;
      DAT_00ca4b00 = &DAT_00ca4b08;
      DAT_00ca4b28 = 0;
      DAT_00ca4b30 = 0;
      DAT_00ca4b20 = 0;
      DAT_00ca4b10 = 0;
      DAT_00ca4b18 = &DAT_00ca4b20;
      __cxa_atexit(FUN_0047ed74,&DAT_00ca4b00,&PTR_LOOP_00c62b90);
      __cxa_guard_release(&DAT_00ca4b38);
      uVar7 = uVar6 & 0xffffffff;
    }
  }
  FUN_00664860(local_68,uVar7,uVar1);
  FUN_0047e89c(&local_50,&DAT_00ca4b00,local_68,PTR_DAT_00c9a8a0,0x1e,1,0,0);
  plVar4 = plStack_48;
  uVar3 = local_50;
  lVar9 = param_1[1];
  local_50 = 0;
  plStack_48 = (long *)0x0;
  plVar8 = *(long **)(lVar9 + 0xca0);
  *(long **)(lVar9 + 0xca0) = plVar4;
  *(undefined8 *)(lVar9 + 0xc98) = uVar3;
  if ((plVar8 != (long *)0x0) && (lVar9 = FUN_00c538e0(0xffffffffffffffff,plVar8 + 1), lVar9 == 0))
  {
    (**(code **)(*plVar8 + 0x10))(plVar8);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar8);
  }
  plVar4 = plStack_48;
  if ((plStack_48 != (long *)0x0) &&
     (lVar9 = FUN_00c538e0(0xffffffffffffffff,plStack_48 + 1), lVar9 == 0)) {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
  if ((local_68[0] & 1) != 0) {
    _ZdlPv(local_58);
  }
  if (*(long *)(lVar2 + 0x28) != local_38) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-007faefc"></a> `007faefc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-007faf00"></a> `007faf00` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007faf04"></a> `007faf04` | `f5 2b 00 f9` | str x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007faf08"></a> `007faf08` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007faf0c"></a> `007faf0c` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-007faf10"></a> `007faf10` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-007faf14"></a> `007faf14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-007faf18"></a> `007faf18` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-007faf1c"></a> `007faf1c` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007faf20"></a> `007faf20` | `15 00 40 f9` | ldr x21,[x0] | `FALL_THROUGH`
<a id="insn-007faf24"></a> `007faf24` | `a1 26 4a b9` | ldr w1,[x21, #0xa24] | `FALL_THROUGH`
<a id="insn-007faf28"></a> `007faf28` | `a0 82 2f 91` | add x0,x21,#0xbe0 | `FALL_THROUGH`
<a id="insn-007faf2c"></a> `007faf2c` | `8b 24 fd 97` | bl 0x00744158 | `UNCONDITIONAL_CALL`
<a id="insn-007faf30"></a> `007faf30` | `a8 ca 20 8b` | add x8,x21,w0, SXTW  #0x2 | `FALL_THROUGH`
<a id="insn-007faf34"></a> `007faf34` | `89 26 93 52` | mov w9,#0x9934 | `FALL_THROUGH`
<a id="insn-007faf38"></a> `007faf38` | `89 00 a0 72` | movk w9,#0x4, LSL #16 | `FALL_THROUGH`
<a id="insn-007faf3c"></a> `007faf3c` | `01 69 69 b8` | ldr w1,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-007faf40"></a> `007faf40` | `48 25 00 d0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-007faf44"></a> `007faf44` | `08 e1 2c 91` | add x8,x8,#0xb38 | `FALL_THROUGH`
<a id="insn-007faf48"></a> `007faf48` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-007faf4c"></a> `007faf4c` | `68 07 00 36` | tbz w8,#0x0,0x007fb038 | `CONDITIONAL_JUMP`
<a id="insn-007faf50"></a> `007faf50` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-007faf54"></a> `007faf54` | `43 a6 f9 97` | bl 0x00664860 | `UNCONDITIONAL_CALL`
<a id="insn-007faf58"></a> `007faf58` | `02 25 00 90` | adrp x2,0xc9a000 | `FALL_THROUGH`
<a id="insn-007faf5c"></a> `007faf5c` | `40 25 00 d0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-007faf60"></a> `007faf60` | `00 00 2c 91` | add x0,x0,#0xb00 | `FALL_THROUGH`
<a id="insn-007faf64"></a> `007faf64` | `42 50 44 f9` | ldr x2,[x2, #0x8a0] | `FALL_THROUGH`
<a id="insn-007faf68"></a> `007faf68` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-007faf6c"></a> `007faf6c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-007faf70"></a> `007faf70` | `c3 03 80 52` | mov w3,#0x1e | `FALL_THROUGH`
<a id="insn-007faf74"></a> `007faf74` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-007faf78"></a> `007faf78` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-007faf7c"></a> `007faf7c` | `e6 03 1f 2a` | mov w6,wzr | `FALL_THROUGH`
<a id="insn-007faf80"></a> `007faf80` | `47 0e f2 97` | bl 0x0047e89c | `UNCONDITIONAL_CALL`
<a id="insn-007faf84"></a> `007faf84` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-007faf88"></a> `007faf88` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007faf8c"></a> `007faf8c` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-007faf90"></a> `007faf90` | `13 51 46 f9` | ldr x19,[x8, #0xca0] | `FALL_THROUGH`
<a id="insn-007faf94"></a> `007faf94` | `08 61 32 91` | add x8,x8,#0xc98 | `FALL_THROUGH`
<a id="insn-007faf98"></a> `007faf98` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-007faf9c"></a> `007faf9c` | `73 01 00 b4` | cbz x19,0x007fafc8 | `CONDITIONAL_JUMP`
<a id="insn-007fafa0"></a> `007fafa0` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007fafa4"></a> `007fafa4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-007fafa8"></a> `007fafa8` | `4e 62 11 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-007fafac"></a> `007fafac` | `e0 00 00 b5` | cbnz x0,0x007fafc8 | `CONDITIONAL_JUMP`
<a id="insn-007fafb0"></a> `007fafb0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-007fafb4"></a> `007fafb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fafb8"></a> `007fafb8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007fafbc"></a> `007fafbc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007fafc0"></a> `007fafc0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fafc4"></a> `007fafc4` | `af 72 11 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-007fafc8"></a> `007fafc8` | `f3 17 40 f9` | ldr x19,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-007fafcc"></a> `007fafcc` | `b3 00 00 b4` | cbz x19,0x007fafe0 | `CONDITIONAL_JUMP`
<a id="insn-007fafd0"></a> `007fafd0` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-007fafd4"></a> `007fafd4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-007fafd8"></a> `007fafd8` | `42 62 11 94` | bl 0x00c538e0 | `UNCONDITIONAL_CALL`
<a id="insn-007fafdc"></a> `007fafdc` | `c0 01 00 b4` | cbz x0,0x007fb014 | `CONDITIONAL_JUMP`
<a id="insn-007fafe0"></a> `007fafe0` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007fafe4"></a> `007fafe4` | `68 00 00 36` | tbz w8,#0x0,0x007faff0 | `CONDITIONAL_JUMP`
<a id="insn-007fafe8"></a> `007fafe8` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-007fafec"></a> `007fafec` | `b1 72 11 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-007faff0"></a> `007faff0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-007faff4"></a> `007faff4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-007faff8"></a> `007faff8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-007faffc"></a> `007faffc` | `a1 06 00 54` | b.ne 0x007fb0d0 | `CONDITIONAL_JUMP`
<a id="insn-007fb000"></a> `007fb000` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-007fb004"></a> `007fb004` | `f5 2b 40 f9` | ldr x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-007fb008"></a> `007fb008` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-007fb00c"></a> `007fb00c` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-007fb010"></a> `007fb010` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-007fb014"></a> `007fb014` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-007fb018"></a> `007fb018` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fb01c"></a> `007fb01c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-007fb020"></a> `007fb020` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-007fb024"></a> `007fb024` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-007fb028"></a> `007fb028` | `96 72 11 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-007fb02c"></a> `007fb02c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-007fb030"></a> `007fb030` | `c8 fd 07 37` | tbnz w8,#0x0,0x007fafe8 | `CONDITIONAL_JUMP`
<a id="insn-007fb034"></a> `007fb034` | `ef ff ff 17` | b 0x007faff0 | `UNCONDITIONAL_JUMP`
<a id="insn-007fb038"></a> `007fb038` | `48 25 00 b0` | adrp x8,0xca4000 | `FALL_THROUGH`
<a id="insn-007fb03c"></a> `007fb03c` | `08 e1 2c 91` | add x8,x8,#0xb38 | `FALL_THROUGH`
<a id="insn-007fb040"></a> `007fb040` | `e1 03 00 29` | stp w1,w0,[sp] | `FALL_THROUGH`
<a id="insn-007fb044"></a> `007fb044` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-007fb048"></a> `007fb048` | `82 72 11 94` | bl 0x00c57a50 | `UNCONDITIONAL_CALL`
<a id="insn-007fb04c"></a> `007fb04c` | `e8 03 00 2a` | mov w8,w0 | `FALL_THROUGH`
<a id="insn-007fb050"></a> `007fb050` | `e1 03 40 29` | ldp w1,w0,[sp] | `FALL_THROUGH`
<a id="insn-007fb054"></a> `007fb054` | `e8 f7 ff 34` | cbz w8,0x007faf50 | `CONDITIONAL_JUMP`
<a id="insn-007fb058"></a> `007fb058` | `41 25 00 b0` | adrp x1,0xca4000 | `FALL_THROUGH`
<a id="insn-007fb05c"></a> `007fb05c` | `21 00 2c 91` | add x1,x1,#0xb00 | `FALL_THROUGH`
<a id="insn-007fb060"></a> `007fb060` | `00 e4 ff f0` | adrp x0,0x47e000 | `FALL_THROUGH`
<a id="insn-007fb064"></a> `007fb064` | `00 d0 35 91` | add x0,x0,#0xd74 | `FALL_THROUGH`
<a id="insn-007fb068"></a> `007fb068` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-007fb06c"></a> `007fb06c` | `22 23 00 f0` | adrp x2,0xc62000 | `FALL_THROUGH`
<a id="insn-007fb070"></a> `007fb070` | `42 40 2e 91` | add x2,x2,#0xb90 | `FALL_THROUGH`
<a id="insn-007fb074"></a> `007fb074` | `1f 8d 00 f8` | str xzr,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-007fb078"></a> `007fb078` | `28 00 00 f9` | str x8,[x1] | `FALL_THROUGH`
<a id="insn-007fb07c"></a> `007fb07c` | `e8 03 01 aa` | mov x8,x1 | `FALL_THROUGH`
<a id="insn-007fb080"></a> `007fb080` | `3f fc 02 a9` | stp xzr,xzr,[x1, #0x28] | `FALL_THROUGH`
<a id="insn-007fb084"></a> `007fb084` | `1f 0d 02 f8` | str xzr,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-007fb088"></a> `007fb088` | `3f 20 01 a9` | stp xzr,x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-007fb08c"></a> `007fb08c` | `69 72 11 94` | bl 0x00c57a30 | `UNCONDITIONAL_CALL`
<a id="insn-007fb090"></a> `007fb090` | `40 25 00 b0` | adrp x0,0xca4000 | `FALL_THROUGH`
<a id="insn-007fb094"></a> `007fb094` | `00 e0 2c 91` | add x0,x0,#0xb38 | `FALL_THROUGH`
<a id="insn-007fb098"></a> `007fb098` | `76 72 11 94` | bl 0x00c57a70 | `UNCONDITIONAL_CALL`
<a id="insn-007fb09c"></a> `007fb09c` | `e1 03 40 29` | ldp w1,w0,[sp] | `FALL_THROUGH`
<a id="insn-007fb0a0"></a> `007fb0a0` | `ac ff ff 17` | b 0x007faf50 | `UNCONDITIONAL_JUMP`
<a id="insn-007fb0d0"></a> `007fb0d0` | `84 72 11 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`007faefc`](#insn-007faefc) 範囲 `[['007faefc', '007faf4f']]`
  - `CONDITIONAL_JUMP` [`007faf4c`](#insn-007faf4c) → [`007fb038`](#insn-007fb038)
  - `FALL_THROUGH` [`007faf4c`](#insn-007faf4c) → [`007faf50`](#insn-007faf50)
- ブロック [`007faf50`](#insn-007faf50) 範囲 `[['007faf50', '007faf9f']]`
  - `CONDITIONAL_JUMP` [`007faf9c`](#insn-007faf9c) → [`007fafc8`](#insn-007fafc8)
  - `FALL_THROUGH` [`007faf9c`](#insn-007faf9c) → [`007fafa0`](#insn-007fafa0)
- ブロック [`007fafa0`](#insn-007fafa0) 範囲 `[['007fafa0', '007fafaf']]`
  - `CONDITIONAL_JUMP` [`007fafac`](#insn-007fafac) → [`007fafc8`](#insn-007fafc8)
  - `FALL_THROUGH` [`007fafac`](#insn-007fafac) → [`007fafb0`](#insn-007fafb0)
- ブロック [`007fafb0`](#insn-007fafb0) 範囲 `[['007fafb0', '007fafc7']]`
  - `FALL_THROUGH` [`007fafc4`](#insn-007fafc4) → [`007fafc8`](#insn-007fafc8)
- ブロック [`007fafc8`](#insn-007fafc8) 範囲 `[['007fafc8', '007fafcf']]`
  - `CONDITIONAL_JUMP` [`007fafcc`](#insn-007fafcc) → [`007fafe0`](#insn-007fafe0)
  - `FALL_THROUGH` [`007fafcc`](#insn-007fafcc) → [`007fafd0`](#insn-007fafd0)
- ブロック [`007fafd0`](#insn-007fafd0) 範囲 `[['007fafd0', '007fafdf']]`
  - `CONDITIONAL_JUMP` [`007fafdc`](#insn-007fafdc) → [`007fb014`](#insn-007fb014)
  - `FALL_THROUGH` [`007fafdc`](#insn-007fafdc) → [`007fafe0`](#insn-007fafe0)
- ブロック [`007fafe0`](#insn-007fafe0) 範囲 `[['007fafe0', '007fafe7']]`
  - `CONDITIONAL_JUMP` [`007fafe4`](#insn-007fafe4) → [`007faff0`](#insn-007faff0)
  - `FALL_THROUGH` [`007fafe4`](#insn-007fafe4) → [`007fafe8`](#insn-007fafe8)
- ブロック [`007fafe8`](#insn-007fafe8) 範囲 `[['007fafe8', '007fafef']]`
  - `FALL_THROUGH` [`007fafec`](#insn-007fafec) → [`007faff0`](#insn-007faff0)
- ブロック [`007faff0`](#insn-007faff0) 範囲 `[['007faff0', '007fafff']]`
  - `CONDITIONAL_JUMP` [`007faffc`](#insn-007faffc) → [`007fb0d0`](#insn-007fb0d0)
  - `FALL_THROUGH` [`007faffc`](#insn-007faffc) → [`007fb000`](#insn-007fb000)
- ブロック [`007fb000`](#insn-007fb000) 範囲 `[['007fb000', '007fb013']]`
- ブロック [`007fb014`](#insn-007fb014) 範囲 `[['007fb014', '007fb033']]`
  - `CONDITIONAL_JUMP` [`007fb030`](#insn-007fb030) → [`007fafe8`](#insn-007fafe8)
  - `FALL_THROUGH` [`007fb030`](#insn-007fb030) → [`007fb034`](#insn-007fb034)
- ブロック [`007fb034`](#insn-007fb034) 範囲 `[['007fb034', '007fb037']]`
  - `UNCONDITIONAL_JUMP` [`007fb034`](#insn-007fb034) → [`007faff0`](#insn-007faff0)
- ブロック [`007fb038`](#insn-007fb038) 範囲 `[['007fb038', '007fb057']]`
  - `CONDITIONAL_JUMP` [`007fb054`](#insn-007fb054) → [`007faf50`](#insn-007faf50)
  - `FALL_THROUGH` [`007fb054`](#insn-007fb054) → [`007fb058`](#insn-007fb058)
- ブロック [`007fb058`](#insn-007fb058) 範囲 `[['007fb058', '007fb0a3']]`
  - `UNCONDITIONAL_JUMP` [`007fb0a0`](#insn-007fb0a0) → [`007faf50`](#insn-007faf50)
- ブロック [`007fb0d0`](#insn-007fb0d0) 範囲 `[['007fb0d0', '007fb0d3']]`

## 命令位置別の参照

- [`007faf00`](#insn-007faf00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007faf04`](#insn-007faf04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007faf08`](#insn-007faf08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007faf1c`](#insn-007faf1c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007faf2c`](#insn-007faf2c) → [`00744158`](../00744/00744158.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00744158` · 推定シンボル `None` · 推定型 `None`
- [`007faf48`](#insn-007faf48) → `00ca4b38`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`007faf4c`](#insn-007faf4c) → [`007fb038`](#insn-007fb038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007faf54`](#insn-007faf54) → [`00664860`](../00664/00664860.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00664860` · 推定シンボル `None` · 推定型 `None`
- [`007faf60`](#insn-007faf60) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007faf64`](#insn-007faf64) → `00c9a8a0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007faf64`](#insn-007faf64) → `00ca4bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`007faf80`](#insn-007faf80) → [`0047e89c`](../0047e/0047e89c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047e89c` · 推定シンボル `None` · 推定型 `None`
- [`007faf88`](#insn-007faf88) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007faf8c`](#insn-007faf8c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007faf9c`](#insn-007faf9c) → [`007fafc8`](#insn-007fafc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafa8`](#insn-007fafa8) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`007fafac`](#insn-007fafac) → [`007fafc8`](#insn-007fafc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafc4`](#insn-007fafc4) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`007fafc8`](#insn-007fafc8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafcc`](#insn-007fafcc) → [`007fafe0`](#insn-007fafe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafd8`](#insn-007fafd8) → [`00c538e0`](../00c53/00c538e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c538e0` · 推定シンボル `None` · 推定型 `None`
- [`007fafdc`](#insn-007fafdc) → [`007fb014`](#insn-007fb014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafe0`](#insn-007fafe0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafe4`](#insn-007fafe4) → [`007faff0`](#insn-007faff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafe8`](#insn-007fafe8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fafec`](#insn-007fafec) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`007faff4`](#insn-007faff4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007faffc`](#insn-007faffc) → [`007fb0d0`](#insn-007fb0d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb000`](#insn-007fb000) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb004`](#insn-007fb004) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb008`](#insn-007fb008) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb028`](#insn-007fb028) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`007fb02c`](#insn-007fb02c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb030`](#insn-007fb030) → [`007fafe8`](#insn-007fafe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb034`](#insn-007fb034) → [`007faff0`](#insn-007faff0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb040`](#insn-007fb040) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb044`](#insn-007fb044) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`007fb048`](#insn-007fb048) → [`00c57a50`](../00c57/00c57a50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a50` · 推定シンボル `None` · 推定型 `None`
- [`007fb050`](#insn-007fb050) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb054`](#insn-007fb054) → [`007faf50`](#insn-007faf50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb05c`](#insn-007fb05c) → `00ca4b00`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fb064`](#insn-007fb064) → [`0047ed74`](../0047e/0047ed74.md) · `PARAM` · `ANALYSIS` · 関数 `0047ed74` · 推定シンボル `None` · 推定型 `None`
- [`007fb070`](#insn-007fb070) → `00c62b90`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`007fb074`](#insn-007fb074) → `00ca4b08`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fb078`](#insn-007fb078) → `00ca4b00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fb078`](#insn-007fb078) → `00ca4b08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fb080`](#insn-007fb080) → `00ca4b28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fb080`](#insn-007fb080) → `00ca4b30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fb084`](#insn-007fb084) → `00ca4b20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fb088`](#insn-007fb088) → `00ca4b10`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fb088`](#insn-007fb088) → `00ca4b18`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fb088`](#insn-007fb088) → `00ca4b20`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`007fb08c`](#insn-007fb08c) → [`00c57a30`](../00c57/00c57a30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a30` · 推定シンボル `None` · 推定型 `None`
- [`007fb094`](#insn-007fb094) → `00ca4b38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`007fb098`](#insn-007fb098) → [`00c57a70`](../00c57/00c57a70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a70` · 推定シンボル `None` · 推定型 `None`
- [`007fb09c`](#insn-007fb09c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb0a0`](#insn-007fb0a0) → [`007faf50`](#insn-007faf50) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`007fb0d0`](#insn-007fb0d0) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`007faf00`](#insn-007faf00)

~~~json
{
  "source": "007faf00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007faf04`](#insn-007faf04)

~~~json
{
  "source": "007faf04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007faf08`](#insn-007faf08)

~~~json
{
  "source": "007faf08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007faf1c`](#insn-007faf1c)

~~~json
{
  "source": "007faf1c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007faf2c`](#insn-007faf2c)

~~~json
{
  "source": "007faf2c",
  "target": "00744158",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007faf48`](#insn-007faf48)

~~~json
{
  "source": "007faf48",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007faf4c`](#insn-007faf4c)

~~~json
{
  "source": "007faf4c",
  "target": "007fb038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007faf54`](#insn-007faf54)

~~~json
{
  "source": "007faf54",
  "target": "00664860",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007faf60`](#insn-007faf60)

~~~json
{
  "source": "007faf60",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007faf64`](#insn-007faf64)

~~~json
{
  "source": "007faf64",
  "target": "00c9a8a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a8a0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007faf64`](#insn-007faf64)

~~~json
{
  "source": "007faf64",
  "target": "00ca4bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4bd8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007faf80`](#insn-007faf80)

~~~json
{
  "source": "007faf80",
  "target": "0047e89c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007faf88`](#insn-007faf88)

~~~json
{
  "source": "007faf88",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007faf8c`](#insn-007faf8c)

~~~json
{
  "source": "007faf8c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007faf9c`](#insn-007faf9c)

~~~json
{
  "source": "007faf9c",
  "target": "007fafc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafa8`](#insn-007fafa8)

~~~json
{
  "source": "007fafa8",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fafac`](#insn-007fafac)

~~~json
{
  "source": "007fafac",
  "target": "007fafc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafc4`](#insn-007fafc4)

~~~json
{
  "source": "007fafc4",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fafc8`](#insn-007fafc8)

~~~json
{
  "source": "007fafc8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafcc`](#insn-007fafcc)

~~~json
{
  "source": "007fafcc",
  "target": "007fafe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafd8`](#insn-007fafd8)

~~~json
{
  "source": "007fafd8",
  "target": "00c538e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fafdc`](#insn-007fafdc)

~~~json
{
  "source": "007fafdc",
  "target": "007fb014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafe0`](#insn-007fafe0)

~~~json
{
  "source": "007fafe0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafe4`](#insn-007fafe4)

~~~json
{
  "source": "007fafe4",
  "target": "007faff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafe8`](#insn-007fafe8)

~~~json
{
  "source": "007fafe8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fafec`](#insn-007fafec)

~~~json
{
  "source": "007fafec",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007faff4`](#insn-007faff4)

~~~json
{
  "source": "007faff4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007faffc`](#insn-007faffc)

~~~json
{
  "source": "007faffc",
  "target": "007fb0d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb000`](#insn-007fb000)

~~~json
{
  "source": "007fb000",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb004`](#insn-007fb004)

~~~json
{
  "source": "007fb004",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb008`](#insn-007fb008)

~~~json
{
  "source": "007fb008",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb028`](#insn-007fb028)

~~~json
{
  "source": "007fb028",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fb02c`](#insn-007fb02c)

~~~json
{
  "source": "007fb02c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb030`](#insn-007fb030)

~~~json
{
  "source": "007fb030",
  "target": "007fafe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb034`](#insn-007fb034)

~~~json
{
  "source": "007fb034",
  "target": "007faff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb040`](#insn-007fb040)

~~~json
{
  "source": "007fb040",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb044`](#insn-007fb044)

~~~json
{
  "source": "007fb044",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb048`](#insn-007fb048)

~~~json
{
  "source": "007fb048",
  "target": "00c57a50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fb050`](#insn-007fb050)

~~~json
{
  "source": "007fb050",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb054`](#insn-007fb054)

~~~json
{
  "source": "007fb054",
  "target": "007faf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb05c`](#insn-007fb05c)

~~~json
{
  "source": "007fb05c",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb064`](#insn-007fb064)

~~~json
{
  "source": "007fb064",
  "target": "0047ed74",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fb070`](#insn-007fb070)

~~~json
{
  "source": "007fb070",
  "target": "00c62b90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c62b90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`007fb074`](#insn-007fb074)

~~~json
{
  "source": "007fb074",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb078`](#insn-007fb078)

~~~json
{
  "source": "007fb078",
  "target": "00ca4b00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb078`](#insn-007fb078)

~~~json
{
  "source": "007fb078",
  "target": "00ca4b08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb080`](#insn-007fb080)

~~~json
{
  "source": "007fb080",
  "target": "00ca4b28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb080`](#insn-007fb080)

~~~json
{
  "source": "007fb080",
  "target": "00ca4b30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb084`](#insn-007fb084)

~~~json
{
  "source": "007fb084",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb088`](#insn-007fb088)

~~~json
{
  "source": "007fb088",
  "target": "00ca4b10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb088`](#insn-007fb088)

~~~json
{
  "source": "007fb088",
  "target": "00ca4b18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb088`](#insn-007fb088)

~~~json
{
  "source": "007fb088",
  "target": "00ca4b20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb08c`](#insn-007fb08c)

~~~json
{
  "source": "007fb08c",
  "target": "00c57a30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fb094`](#insn-007fb094)

~~~json
{
  "source": "007fb094",
  "target": "00ca4b38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00ca4b38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`007fb098`](#insn-007fb098)

~~~json
{
  "source": "007fb098",
  "target": "00c57a70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`007fb09c`](#insn-007fb09c)

~~~json
{
  "source": "007fb09c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb0a0`](#insn-007fb0a0)

~~~json
{
  "source": "007fb0a0",
  "target": "007faf50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`007fb0d0`](#insn-007fb0d0)

~~~json
{
  "source": "007fb0d0",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
