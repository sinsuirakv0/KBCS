# 00acba3c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acb9f8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb9f8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0059.md#compare-a109c083c3e51c334ee8bee194ca518a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b2b4cc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b2b/00b2b4cc.md) · 移動量 `+0x5fa90`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0054.md#compare-f25d9909a6f926040750ce6c6754b89b)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acba3c",
  "name": "FUN_00acba3c",
  "size": 628,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ada82b445c61c9efe80fb990ca05310b08417c89e9553abb9ce3478562cf85fa",
  "source_text_sha256": "ada82b445c61c9efe80fb990ca05310b08417c89e9553abb9ce3478562cf85fa",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acba3c",
        "00acbcab"
      ],
      [
        "00acbd10",
        "00acbd13"
      ]
    ],
    "bytes_sha256": "829a8881655e318a9539e6f025d3bdce5017ccd2e01436aa8262322aae4304bb",
    "instruction_count": 157,
    "instruction_bytes": 628,
    "body_bytes": 628,
    "indirect": 5,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [004184bc](../00418/004184bc.md)

## 呼び出し先

- [0041be0c](../0041b/0041be0c.md)
- [0041c9e0](../0041c/0041c9e0.md)
- [00449bb8](../00449/00449bb8.md)
- [00449be4](../00449/00449be4.md)
- [004723a8](../00472/004723a8.md)
- [0052e34c](../0052e/0052e34c.md)
- [00574768](../00574/00574768.md)
- [0081f580](../0081f/0081f580.md)
- [00828e20](../00828/00828e20.md)
- [00acd52c](../00acd/00acd52c.md)
- [00acd530](../00acd/00acd530.md)
- [00acd5b0](../00acd/00acd5b0.md)
- [00acd5b4](../00acd/00acd5b4.md)
- [00bd6558](../00bd6/00bd6558.md)
- [00bd65f8](../00bd6/00bd65f8.md)
- [00bd6e90](../00bd6/00bd6e90.md)
- [00bdb030](../00bdb/00bdb030.md)
- [00bdb070](../00bdb/00bdb070.md)
- [00bdb090](../00bdb/00bdb090.md)
- [00bdb640](../00bdb/00bdb640.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3442 bytes

~~~c

/* WARNING: Globals starting with '_' overlap smaller symbols at the same address */

void FUN_00acba3c(void)

{
  long lVar1;
  long *plVar2;
  int iVar3;
  ulong uVar4;
  long lVar5;
  undefined ***pppuVar6;
  long lVar7;
  float fVar8;
  undefined4 uVar9;
  undefined8 local_80;
  long *local_78;
  undefined **local_70 [4];
  undefined ***local_50;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  FUN_0081f580();
  uVar4 = FUN_00449be4();
  if ((uVar4 & 1) != 0) {
    if (*(long *)(lVar1 + 0x28) == local_38) {
      thunk_FUN_00569550();
      return;
    }
    goto LAB_00acbd10;
  }
  FUN_0081f580();
  uVar4 = FUN_00449bb8();
  if ((uVar4 & 1) != 0) {
    lVar5 = _ZNSt6__ndk16chrono12steady_clock3nowEv();
    FUN_0041be0c();
    FUN_0041c9e0();
    uVar4 = FUN_004723a8();
    if ((uVar4 & 1) != 0) {
      FUN_0081f580();
      iVar3 = FUN_00828e20();
      if (iVar3 != 0x65) {
        FUN_0081f580();
        iVar3 = FUN_00828e20();
        if (iVar3 != 0x67) {
          FUN_0081f580();
          iVar3 = FUN_00828e20();
          if (iVar3 != 0x61) {
            local_80 = 0;
            local_78 = (long *)0x0;
            local_70[0] = &PTR_FUN_00c0f748;
            local_50 = local_70;
            (**(code **)(**(long **)PTR_DAT_00c1b450 + 0xe8))
                      (*(long **)PTR_DAT_00c1b450,&local_80,local_70);
            if (local_50 == local_70) {
              lVar5 = 0x20;
              pppuVar6 = local_70;
LAB_00acbc70:
              (**(code **)((long)*pppuVar6 + lVar5))();
            }
            else if (local_50 != (undefined ***)0x0) {
              lVar5 = 0x28;
              pppuVar6 = local_50;
              goto LAB_00acbc70;
            }
            FUN_0052e34c(&local_80);
            goto LAB_00acbc84;
          }
        }
      }
    }
    local_80 = 0;
    local_78 = (long *)0x0;
    local_70[0] = &PTR_FUN_00c0f7c8;
    local_50 = local_70;
    (**(code **)(**(long **)PTR_DAT_00c1b450 + 0xe8))(*(long **)PTR_DAT_00c1b450,&local_80,local_70)
    ;
    if (local_50 == local_70) {
      lVar7 = 0x20;
      pppuVar6 = local_70;
LAB_00acbb40:
      (**(code **)((long)*pppuVar6 + lVar7))();
    }
    else if (local_50 != (undefined ***)0x0) {
      lVar7 = 0x28;
      pppuVar6 = local_50;
      goto LAB_00acbb40;
    }
    plVar2 = local_78;
    if ((local_78 != (long *)0x0) &&
       (lVar7 = FUN_00bd6e90(0xffffffffffffffff,local_78 + 1), lVar7 == 0)) {
      (**(code **)(*plVar2 + 0x10))(plVar2);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    }
    lVar7 = _ZNSt6__ndk16chrono12steady_clock3nowEv();
    fVar8 = (float)(lVar7 - lVar5) / 1e+09;
    if ((fVar8 < 0.033333335) && (fVar8 = 0.033333335 - fVar8, 0.0 < fVar8)) {
      uVar9 = FUN_00bd65f8(fVar8);
      iVar3 = FUN_00bd6558(uVar9,_DAT_002b0de0);
      if (iVar3 < 0) {
        local_70[0] = (undefined **)(long)(fVar8 * 1e+09);
        if ((float)(long)local_70[0] < fVar8 * 1e+09) {
          local_70[0] = (undefined **)((long)local_70[0] + 1);
        }
      }
      else {
        local_70[0] = (undefined **)0x7fffffffffffffff;
      }
      _ZNSt6__ndk111this_thread9sleep_forERKNS_6chrono8durationIxNS_5ratioILl1ELl1000000000EEEEE
                (local_70);
    }
  }
LAB_00acbc84:
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
LAB_00acbd10:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acba3c"></a> `00acba3c` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00acba40"></a> `00acba40` | `e8 2b 00 fd` | str d8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acba44"></a> `00acba44` | `fd fb 05 a9` | stp x29,x30,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00acba48"></a> `00acba48` | `f5 37 00 f9` | str x21,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00acba4c"></a> `00acba4c` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acba50"></a> `00acba50` | `fd 63 01 91` | add x29,sp,#0x58 | `FALL_THROUGH`
<a id="insn-00acba54"></a> `00acba54` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acba58"></a> `00acba58` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acba5c"></a> `00acba5c` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acba60"></a> `00acba60` | `c8 4e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acba64"></a> `00acba64` | `60 f8 e5 97` | bl 0x00449be4 | `UNCONDITIONAL_CALL`
<a id="insn-00acba68"></a> `00acba68` | `60 01 00 36` | tbz w0,#0x0,0x00acba94 | `CONDITIONAL_JUMP`
<a id="insn-00acba6c"></a> `00acba6c` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acba70"></a> `00acba70` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acba74"></a> `00acba74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acba78"></a> `00acba78` | `c1 14 00 54` | b.ne 0x00acbd10 | `CONDITIONAL_JUMP`
<a id="insn-00acba7c"></a> `00acba7c` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acba80"></a> `00acba80` | `f5 37 40 f9` | ldr x21,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00acba84"></a> `00acba84` | `fd fb 45 a9` | ldp x29,x30,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00acba88"></a> `00acba88` | `e8 2b 40 fd` | ldr d8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acba8c"></a> `00acba8c` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00acba90"></a> `00acba90` | `36 a3 ea 17` | b 0x00574768 | `CALL_TERMINATOR`
<a id="insn-00acba94"></a> `00acba94` | `bb 4e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acba98"></a> `00acba98` | `48 f8 e5 97` | bl 0x00449bb8 | `UNCONDITIONAL_CALL`
<a id="insn-00acba9c"></a> `00acba9c` | `40 0f 00 36` | tbz w0,#0x0,0x00acbc84 | `CONDITIONAL_JUMP`
<a id="insn-00acbaa0"></a> `00acbaa0` | `74 3d 04 94` | bl 0x00bdb070 | `UNCONDITIONAL_CALL`
<a id="insn-00acbaa4"></a> `00acbaa4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acbaa8"></a> `00acbaa8` | `d9 40 e5 97` | bl 0x0041be0c | `UNCONDITIONAL_CALL`
<a id="insn-00acbaac"></a> `00acbaac` | `cd 43 e5 97` | bl 0x0041c9e0 | `UNCONDITIONAL_CALL`
<a id="insn-00acbab0"></a> `00acbab0` | `3e 9a e6 97` | bl 0x004723a8 | `UNCONDITIONAL_CALL`
<a id="insn-00acbab4"></a> `00acbab4` | `a0 01 00 36` | tbz w0,#0x0,0x00acbae8 | `CONDITIONAL_JUMP`
<a id="insn-00acbab8"></a> `00acbab8` | `b2 4e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acbabc"></a> `00acbabc` | `d9 74 f5 97` | bl 0x00828e20 | `UNCONDITIONAL_CALL`
<a id="insn-00acbac0"></a> `00acbac0` | `1f 94 01 71` | cmp w0,#0x65 | `FALL_THROUGH`
<a id="insn-00acbac4"></a> `00acbac4` | `20 01 00 54` | b.eq 0x00acbae8 | `CONDITIONAL_JUMP`
<a id="insn-00acbac8"></a> `00acbac8` | `ae 4e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acbacc"></a> `00acbacc` | `d5 74 f5 97` | bl 0x00828e20 | `UNCONDITIONAL_CALL`
<a id="insn-00acbad0"></a> `00acbad0` | `1f 9c 01 71` | cmp w0,#0x67 | `FALL_THROUGH`
<a id="insn-00acbad4"></a> `00acbad4` | `a0 00 00 54` | b.eq 0x00acbae8 | `CONDITIONAL_JUMP`
<a id="insn-00acbad8"></a> `00acbad8` | `aa 4e f5 97` | bl 0x0081f580 | `UNCONDITIONAL_CALL`
<a id="insn-00acbadc"></a> `00acbadc` | `d1 74 f5 97` | bl 0x00828e20 | `UNCONDITIONAL_CALL`
<a id="insn-00acbae0"></a> `00acbae0` | `1f 84 01 71` | cmp w0,#0x61 | `FALL_THROUGH`
<a id="insn-00acbae4"></a> `00acbae4` | `a1 09 00 54` | b.ne 0x00acbc18 | `CONDITIONAL_JUMP`
<a id="insn-00acbae8"></a> `00acbae8` | `88 0a 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00acbaec"></a> `00acbaec` | `29 0a 00 90` | adrp x9,0xc0f000 | `FALL_THROUGH`
<a id="insn-00acbaf0"></a> `00acbaf0` | `29 21 1f 91` | add x9,x9,#0x7c8 | `FALL_THROUGH`
<a id="insn-00acbaf4"></a> `00acbaf4` | `08 29 42 f9` | ldr x8,[x8, #0x450] | `FALL_THROUGH`
<a id="insn-00acbaf8"></a> `00acbaf8` | `f4 43 00 91` | add x20,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acbafc"></a> `00acbafc` | `ff 7f 00 a9` | stp xzr,xzr,[sp] | `FALL_THROUGH`
<a id="insn-00acbb00"></a> `00acbb00` | `e9 0b 00 f9` | str x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbb04"></a> `00acbb04` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00acbb08"></a> `00acbb08` | `f4 1b 00 f9` | str x20,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbb0c"></a> `00acbb0c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acbb10"></a> `00acbb10` | `08 75 40 f9` | ldr x8,[x8, #0xe8] | `FALL_THROUGH`
<a id="insn-00acbb14"></a> `00acbb14` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acbb18"></a> `00acbb18` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acbb1c"></a> `00acbb1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbb20"></a> `00acbb20` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbb24"></a> `00acbb24` | `1f 00 14 eb` | cmp x0,x20 | `FALL_THROUGH`
<a id="insn-00acbb28"></a> `00acbb28` | `80 00 00 54` | b.eq 0x00acbb38 | `CONDITIONAL_JUMP`
<a id="insn-00acbb2c"></a> `00acbb2c` | `00 01 00 b4` | cbz x0,0x00acbb4c | `CONDITIONAL_JUMP`
<a id="insn-00acbb30"></a> `00acbb30` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00acbb34"></a> `00acbb34` | `03 00 00 14` | b 0x00acbb40 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbb38"></a> `00acbb38` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00acbb3c"></a> `00acbb3c` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acbb40"></a> `00acbb40` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00acbb44"></a> `00acbb44` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acbb48"></a> `00acbb48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbb4c"></a> `00acbb4c` | `f4 07 40 f9` | ldr x20,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acbb50"></a> `00acbb50` | `74 01 00 b4` | cbz x20,0x00acbb7c | `CONDITIONAL_JUMP`
<a id="insn-00acbb54"></a> `00acbb54` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acbb58"></a> `00acbb58` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00acbb5c"></a> `00acbb5c` | `cd 2c 04 94` | bl 0x00bd6e90 | `UNCONDITIONAL_CALL`
<a id="insn-00acbb60"></a> `00acbb60` | `e0 00 00 b5` | cbnz x0,0x00acbb7c | `CONDITIONAL_JUMP`
<a id="insn-00acbb64"></a> `00acbb64` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00acbb68"></a> `00acbb68` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbb6c"></a> `00acbb6c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00acbb70"></a> `00acbb70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbb74"></a> `00acbb74` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acbb78"></a> `00acbb78` | `2e 3d 04 94` | bl 0x00bdb030 | `UNCONDITIONAL_CALL`
<a id="insn-00acbb7c"></a> `00acbb7c` | `3d 3d 04 94` | bl 0x00bdb070 | `UNCONDITIONAL_CALL`
<a id="insn-00acbb80"></a> `00acbb80` | `08 00 13 cb` | sub x8,x0,x19 | `FALL_THROUGH`
<a id="insn-00acbb84"></a> `00acbb84` | `00 01 22 9e` | scvtf s0,x8 | `FALL_THROUGH`
<a id="insn-00acbb88"></a> `00acbb88` | `08 65 8d 52` | mov w8,#0x6b28 | `FALL_THROUGH`
<a id="insn-00acbb8c"></a> `00acbb8c` | `c8 cd a9 72` | movk w8,#0x4e6e, LSL #16 | `FALL_THROUGH`
<a id="insn-00acbb90"></a> `00acbb90` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-00acbb94"></a> `00acbb94` | `28 11 91 52` | mov w8,#0x8889 | `FALL_THROUGH`
<a id="insn-00acbb98"></a> `00acbb98` | `08 a1 a7 72` | movk w8,#0x3d08, LSL #16 | `FALL_THROUGH`
<a id="insn-00acbb9c"></a> `00acbb9c` | `00 18 21 1e` | fdiv s0,s0,s1 | `FALL_THROUGH`
<a id="insn-00acbba0"></a> `00acbba0` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-00acbba4"></a> `00acbba4` | `00 20 21 1e` | fcmp s0,s1 | `FALL_THROUGH`
<a id="insn-00acbba8"></a> `00acbba8` | `e5 06 00 54` | b.pl 0x00acbc84 | `CONDITIONAL_JUMP`
<a id="insn-00acbbac"></a> `00acbbac` | `01 01 27 1e` | fmov s1,w8 | `FALL_THROUGH`
<a id="insn-00acbbb0"></a> `00acbbb0` | `28 38 20 1e` | fsub s8,s1,s0 | `FALL_THROUGH`
<a id="insn-00acbbb4"></a> `00acbbb4` | `08 21 20 1e` | fcmp s8,#0.0 | `FALL_THROUGH`
<a id="insn-00acbbb8"></a> `00acbbb8` | `6d 06 00 54` | b.le 0x00acbc84 | `CONDITIONAL_JUMP`
<a id="insn-00acbbbc"></a> `00acbbbc` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-00acbbc0"></a> `00acbbc0` | `8e 2a 04 94` | bl 0x00bd65f8 | `UNCONDITIONAL_CALL`
<a id="insn-00acbbc4"></a> `00acbbc4` | `28 bf ff b0` | adrp x8,0x2b0000 | `FALL_THROUGH`
<a id="insn-00acbbc8"></a> `00acbbc8` | `01 79 c3 3d` | ldr q1,[x8, #0xde0] | `FALL_THROUGH`
<a id="insn-00acbbcc"></a> `00acbbcc` | `63 2a 04 94` | bl 0x00bd6558 | `UNCONDITIONAL_CALL`
<a id="insn-00acbbd0"></a> `00acbbd0` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00acbbd4"></a> `00acbbd4` | `8a 01 00 54` | b.ge 0x00acbc04 | `CONDITIONAL_JUMP`
<a id="insn-00acbbd8"></a> `00acbbd8` | `08 65 8d 52` | mov w8,#0x6b28 | `FALL_THROUGH`
<a id="insn-00acbbdc"></a> `00acbbdc` | `c8 cd a9 72` | movk w8,#0x4e6e, LSL #16 | `FALL_THROUGH`
<a id="insn-00acbbe0"></a> `00acbbe0` | `00 01 27 1e` | fmov s0,w8 | `FALL_THROUGH`
<a id="insn-00acbbe4"></a> `00acbbe4` | `00 09 20 1e` | fmul s0,s8,s0 | `FALL_THROUGH`
<a id="insn-00acbbe8"></a> `00acbbe8` | `08 00 38 9e` | fcvtzs x8,s0 | `FALL_THROUGH`
<a id="insn-00acbbec"></a> `00acbbec` | `01 01 22 9e` | scvtf s1,x8 | `FALL_THROUGH`
<a id="insn-00acbbf0"></a> `00acbbf0` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbbf4"></a> `00acbbf4` | `00 20 21 1e` | fcmp s0,s1 | `FALL_THROUGH`
<a id="insn-00acbbf8"></a> `00acbbf8` | `ad 00 00 54` | b.le 0x00acbc0c | `CONDITIONAL_JUMP`
<a id="insn-00acbbfc"></a> `00acbbfc` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00acbc00"></a> `00acbc00` | `02 00 00 14` | b 0x00acbc08 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbc04"></a> `00acbc04` | `08 00 f0 92` | mov x8,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00acbc08"></a> `00acbc08` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbc0c"></a> `00acbc0c` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acbc10"></a> `00acbc10` | `8c 3e 04 94` | bl 0x00bdb640 | `UNCONDITIONAL_CALL`
<a id="insn-00acbc14"></a> `00acbc14` | `1c 00 00 14` | b 0x00acbc84 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbc18"></a> `00acbc18` | `88 0a 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00acbc1c"></a> `00acbc1c` | `29 0a 00 90` | adrp x9,0xc0f000 | `FALL_THROUGH`
<a id="insn-00acbc20"></a> `00acbc20` | `29 21 1d 91` | add x9,x9,#0x748 | `FALL_THROUGH`
<a id="insn-00acbc24"></a> `00acbc24` | `08 29 42 f9` | ldr x8,[x8, #0x450] | `FALL_THROUGH`
<a id="insn-00acbc28"></a> `00acbc28` | `f3 43 00 91` | add x19,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acbc2c"></a> `00acbc2c` | `ff 7f 00 a9` | stp xzr,xzr,[sp] | `FALL_THROUGH`
<a id="insn-00acbc30"></a> `00acbc30` | `e9 0b 00 f9` | str x9,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acbc34"></a> `00acbc34` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00acbc38"></a> `00acbc38` | `f3 1b 00 f9` | str x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbc3c"></a> `00acbc3c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00acbc40"></a> `00acbc40` | `08 75 40 f9` | ldr x8,[x8, #0xe8] | `FALL_THROUGH`
<a id="insn-00acbc44"></a> `00acbc44` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acbc48"></a> `00acbc48` | `e2 43 00 91` | add x2,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acbc4c"></a> `00acbc4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbc50"></a> `00acbc50` | `e0 1b 40 f9` | ldr x0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acbc54"></a> `00acbc54` | `1f 00 13 eb` | cmp x0,x19 | `FALL_THROUGH`
<a id="insn-00acbc58"></a> `00acbc58` | `80 00 00 54` | b.eq 0x00acbc68 | `CONDITIONAL_JUMP`
<a id="insn-00acbc5c"></a> `00acbc5c` | `00 01 00 b4` | cbz x0,0x00acbc7c | `CONDITIONAL_JUMP`
<a id="insn-00acbc60"></a> `00acbc60` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00acbc64"></a> `00acbc64` | `03 00 00 14` | b 0x00acbc70 | `UNCONDITIONAL_JUMP`
<a id="insn-00acbc68"></a> `00acbc68` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00acbc6c"></a> `00acbc6c` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00acbc70"></a> `00acbc70` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00acbc74"></a> `00acbc74` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00acbc78"></a> `00acbc78` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00acbc7c"></a> `00acbc7c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acbc80"></a> `00acbc80` | `b3 89 e9 97` | bl 0x0052e34c | `UNCONDITIONAL_CALL`
<a id="insn-00acbc84"></a> `00acbc84` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00acbc88"></a> `00acbc88` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acbc8c"></a> `00acbc8c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acbc90"></a> `00acbc90` | `01 04 00 54` | b.ne 0x00acbd10 | `CONDITIONAL_JUMP`
<a id="insn-00acbc94"></a> `00acbc94` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acbc98"></a> `00acbc98` | `f5 37 40 f9` | ldr x21,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00acbc9c"></a> `00acbc9c` | `fd fb 45 a9` | ldp x29,x30,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00acbca0"></a> `00acbca0` | `e8 2b 40 fd` | ldr d8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acbca4"></a> `00acbca4` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00acbca8"></a> `00acbca8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acbd10"></a> `00acbd10` | `e0 3c 04 94` | bl 0x00bdb090 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acba3c`](#insn-00acba3c) 範囲 `[['00acba3c', '00acba6b']]`
  - `CONDITIONAL_JUMP` [`00acba68`](#insn-00acba68) → [`00acba94`](#insn-00acba94)
  - `FALL_THROUGH` [`00acba68`](#insn-00acba68) → [`00acba6c`](#insn-00acba6c)
- ブロック [`00acba6c`](#insn-00acba6c) 範囲 `[['00acba6c', '00acba7b']]`
  - `CONDITIONAL_JUMP` [`00acba78`](#insn-00acba78) → [`00acbd10`](#insn-00acbd10)
  - `FALL_THROUGH` [`00acba78`](#insn-00acba78) → [`00acba7c`](#insn-00acba7c)
- ブロック [`00acba7c`](#insn-00acba7c) 範囲 `[['00acba7c', '00acba93']]`
- ブロック [`00acba94`](#insn-00acba94) 範囲 `[['00acba94', '00acba9f']]`
  - `CONDITIONAL_JUMP` [`00acba9c`](#insn-00acba9c) → [`00acbc84`](#insn-00acbc84)
  - `FALL_THROUGH` [`00acba9c`](#insn-00acba9c) → [`00acbaa0`](#insn-00acbaa0)
- ブロック [`00acbaa0`](#insn-00acbaa0) 範囲 `[['00acbaa0', '00acbab7']]`
  - `CONDITIONAL_JUMP` [`00acbab4`](#insn-00acbab4) → [`00acbae8`](#insn-00acbae8)
  - `FALL_THROUGH` [`00acbab4`](#insn-00acbab4) → [`00acbab8`](#insn-00acbab8)
- ブロック [`00acbab8`](#insn-00acbab8) 範囲 `[['00acbab8', '00acbac7']]`
  - `CONDITIONAL_JUMP` [`00acbac4`](#insn-00acbac4) → [`00acbae8`](#insn-00acbae8)
  - `FALL_THROUGH` [`00acbac4`](#insn-00acbac4) → [`00acbac8`](#insn-00acbac8)
- ブロック [`00acbac8`](#insn-00acbac8) 範囲 `[['00acbac8', '00acbad7']]`
  - `CONDITIONAL_JUMP` [`00acbad4`](#insn-00acbad4) → [`00acbae8`](#insn-00acbae8)
  - `FALL_THROUGH` [`00acbad4`](#insn-00acbad4) → [`00acbad8`](#insn-00acbad8)
- ブロック [`00acbad8`](#insn-00acbad8) 範囲 `[['00acbad8', '00acbae7']]`
  - `CONDITIONAL_JUMP` [`00acbae4`](#insn-00acbae4) → [`00acbc18`](#insn-00acbc18)
  - `FALL_THROUGH` [`00acbae4`](#insn-00acbae4) → [`00acbae8`](#insn-00acbae8)
- ブロック [`00acbae8`](#insn-00acbae8) 範囲 `[['00acbae8', '00acbb2b']]`
  - `CONDITIONAL_JUMP` [`00acbb28`](#insn-00acbb28) → [`00acbb38`](#insn-00acbb38)
  - `FALL_THROUGH` [`00acbb28`](#insn-00acbb28) → [`00acbb2c`](#insn-00acbb2c)
- ブロック [`00acbb2c`](#insn-00acbb2c) 範囲 `[['00acbb2c', '00acbb2f']]`
  - `CONDITIONAL_JUMP` [`00acbb2c`](#insn-00acbb2c) → [`00acbb4c`](#insn-00acbb4c)
  - `FALL_THROUGH` [`00acbb2c`](#insn-00acbb2c) → [`00acbb30`](#insn-00acbb30)
- ブロック [`00acbb30`](#insn-00acbb30) 範囲 `[['00acbb30', '00acbb37']]`
  - `UNCONDITIONAL_JUMP` [`00acbb34`](#insn-00acbb34) → [`00acbb40`](#insn-00acbb40)
- ブロック [`00acbb38`](#insn-00acbb38) 範囲 `[['00acbb38', '00acbb3f']]`
  - `FALL_THROUGH` [`00acbb3c`](#insn-00acbb3c) → [`00acbb40`](#insn-00acbb40)
- ブロック [`00acbb40`](#insn-00acbb40) 範囲 `[['00acbb40', '00acbb4b']]`
  - `FALL_THROUGH` [`00acbb48`](#insn-00acbb48) → [`00acbb4c`](#insn-00acbb4c)
- ブロック [`00acbb4c`](#insn-00acbb4c) 範囲 `[['00acbb4c', '00acbb53']]`
  - `CONDITIONAL_JUMP` [`00acbb50`](#insn-00acbb50) → [`00acbb7c`](#insn-00acbb7c)
  - `FALL_THROUGH` [`00acbb50`](#insn-00acbb50) → [`00acbb54`](#insn-00acbb54)
- ブロック [`00acbb54`](#insn-00acbb54) 範囲 `[['00acbb54', '00acbb63']]`
  - `CONDITIONAL_JUMP` [`00acbb60`](#insn-00acbb60) → [`00acbb7c`](#insn-00acbb7c)
  - `FALL_THROUGH` [`00acbb60`](#insn-00acbb60) → [`00acbb64`](#insn-00acbb64)
- ブロック [`00acbb64`](#insn-00acbb64) 範囲 `[['00acbb64', '00acbb7b']]`
  - `FALL_THROUGH` [`00acbb78`](#insn-00acbb78) → [`00acbb7c`](#insn-00acbb7c)
- ブロック [`00acbb7c`](#insn-00acbb7c) 範囲 `[['00acbb7c', '00acbbab']]`
  - `CONDITIONAL_JUMP` [`00acbba8`](#insn-00acbba8) → [`00acbc84`](#insn-00acbc84)
  - `FALL_THROUGH` [`00acbba8`](#insn-00acbba8) → [`00acbbac`](#insn-00acbbac)
- ブロック [`00acbbac`](#insn-00acbbac) 範囲 `[['00acbbac', '00acbbbb']]`
  - `CONDITIONAL_JUMP` [`00acbbb8`](#insn-00acbbb8) → [`00acbc84`](#insn-00acbc84)
  - `FALL_THROUGH` [`00acbbb8`](#insn-00acbbb8) → [`00acbbbc`](#insn-00acbbbc)
- ブロック [`00acbbbc`](#insn-00acbbbc) 範囲 `[['00acbbbc', '00acbbd7']]`
  - `CONDITIONAL_JUMP` [`00acbbd4`](#insn-00acbbd4) → [`00acbc04`](#insn-00acbc04)
  - `FALL_THROUGH` [`00acbbd4`](#insn-00acbbd4) → [`00acbbd8`](#insn-00acbbd8)
- ブロック [`00acbbd8`](#insn-00acbbd8) 範囲 `[['00acbbd8', '00acbbfb']]`
  - `CONDITIONAL_JUMP` [`00acbbf8`](#insn-00acbbf8) → [`00acbc0c`](#insn-00acbc0c)
  - `FALL_THROUGH` [`00acbbf8`](#insn-00acbbf8) → [`00acbbfc`](#insn-00acbbfc)
- ブロック [`00acbbfc`](#insn-00acbbfc) 範囲 `[['00acbbfc', '00acbc03']]`
  - `UNCONDITIONAL_JUMP` [`00acbc00`](#insn-00acbc00) → [`00acbc08`](#insn-00acbc08)
- ブロック [`00acbc04`](#insn-00acbc04) 範囲 `[['00acbc04', '00acbc07']]`
  - `FALL_THROUGH` [`00acbc04`](#insn-00acbc04) → [`00acbc08`](#insn-00acbc08)
- ブロック [`00acbc08`](#insn-00acbc08) 範囲 `[['00acbc08', '00acbc0b']]`
  - `FALL_THROUGH` [`00acbc08`](#insn-00acbc08) → [`00acbc0c`](#insn-00acbc0c)
- ブロック [`00acbc0c`](#insn-00acbc0c) 範囲 `[['00acbc0c', '00acbc17']]`
  - `UNCONDITIONAL_JUMP` [`00acbc14`](#insn-00acbc14) → [`00acbc84`](#insn-00acbc84)
- ブロック [`00acbc18`](#insn-00acbc18) 範囲 `[['00acbc18', '00acbc5b']]`
  - `CONDITIONAL_JUMP` [`00acbc58`](#insn-00acbc58) → [`00acbc68`](#insn-00acbc68)
  - `FALL_THROUGH` [`00acbc58`](#insn-00acbc58) → [`00acbc5c`](#insn-00acbc5c)
- ブロック [`00acbc5c`](#insn-00acbc5c) 範囲 `[['00acbc5c', '00acbc5f']]`
  - `CONDITIONAL_JUMP` [`00acbc5c`](#insn-00acbc5c) → [`00acbc7c`](#insn-00acbc7c)
  - `FALL_THROUGH` [`00acbc5c`](#insn-00acbc5c) → [`00acbc60`](#insn-00acbc60)
- ブロック [`00acbc60`](#insn-00acbc60) 範囲 `[['00acbc60', '00acbc67']]`
  - `UNCONDITIONAL_JUMP` [`00acbc64`](#insn-00acbc64) → [`00acbc70`](#insn-00acbc70)
- ブロック [`00acbc68`](#insn-00acbc68) 範囲 `[['00acbc68', '00acbc6f']]`
  - `FALL_THROUGH` [`00acbc6c`](#insn-00acbc6c) → [`00acbc70`](#insn-00acbc70)
- ブロック [`00acbc70`](#insn-00acbc70) 範囲 `[['00acbc70', '00acbc7b']]`
  - `FALL_THROUGH` [`00acbc78`](#insn-00acbc78) → [`00acbc7c`](#insn-00acbc7c)
- ブロック [`00acbc7c`](#insn-00acbc7c) 範囲 `[['00acbc7c', '00acbc83']]`
  - `FALL_THROUGH` [`00acbc80`](#insn-00acbc80) → [`00acbc84`](#insn-00acbc84)
- ブロック [`00acbc84`](#insn-00acbc84) 範囲 `[['00acbc84', '00acbc93']]`
  - `CONDITIONAL_JUMP` [`00acbc90`](#insn-00acbc90) → [`00acbd10`](#insn-00acbd10)
  - `FALL_THROUGH` [`00acbc90`](#insn-00acbc90) → [`00acbc94`](#insn-00acbc94)
- ブロック [`00acbc94`](#insn-00acbc94) 範囲 `[['00acbc94', '00acbcab']]`
- ブロック [`00acbd10`](#insn-00acbd10) 範囲 `[['00acbd10', '00acbd13']]`

## 命令位置別の参照

- [`00acba40`](#insn-00acba40) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba44`](#insn-00acba44) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba48`](#insn-00acba48) → `Stack[-0x18]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba4c`](#insn-00acba4c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba5c`](#insn-00acba5c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba60`](#insn-00acba60) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acba64`](#insn-00acba64) → [`00449be4`](../00449/00449be4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449be4` · 推定シンボル `None` · 推定型 `None`
- [`00acba68`](#insn-00acba68) → [`00acba94`](#insn-00acba94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba70`](#insn-00acba70) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba78`](#insn-00acba78) → [`00acbd10`](#insn-00acbd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba7c`](#insn-00acba7c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba80`](#insn-00acba80) → `Stack[-0x18]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba84`](#insn-00acba84) → `Stack[-0x28]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba88`](#insn-00acba88) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acba90`](#insn-00acba90) → [`00574768`](../00574/00574768.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574768` · 推定シンボル `None` · 推定型 `None`
- [`00acba94`](#insn-00acba94) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acba98`](#insn-00acba98) → [`00449bb8`](../00449/00449bb8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00449bb8` · 推定シンボル `None` · 推定型 `None`
- [`00acba9c`](#insn-00acba9c) → [`00acbc84`](#insn-00acbc84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbaa0`](#insn-00acbaa0) → [`00bdb070`](../00bdb/00bdb070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb070` · 推定シンボル `None` · 推定型 `None`
- [`00acbaa8`](#insn-00acbaa8) → [`0041be0c`](../0041b/0041be0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041be0c` · 推定シンボル `None` · 推定型 `None`
- [`00acbaac`](#insn-00acbaac) → [`0041c9e0`](../0041c/0041c9e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041c9e0` · 推定シンボル `None` · 推定型 `None`
- [`00acbab0`](#insn-00acbab0) → [`004723a8`](../00472/004723a8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004723a8` · 推定シンボル `None` · 推定型 `None`
- [`00acbab4`](#insn-00acbab4) → [`00acbae8`](#insn-00acbae8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbab8`](#insn-00acbab8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acbabc`](#insn-00acbabc) → [`00828e20`](../00828/00828e20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00828e20` · 推定シンボル `None` · 推定型 `None`
- [`00acbac4`](#insn-00acbac4) → [`00acbae8`](#insn-00acbae8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbac8`](#insn-00acbac8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acbacc`](#insn-00acbacc) → [`00828e20`](../00828/00828e20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00828e20` · 推定シンボル `None` · 推定型 `None`
- [`00acbad4`](#insn-00acbad4) → [`00acbae8`](#insn-00acbae8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbad8`](#insn-00acbad8) → [`0081f580`](../0081f/0081f580.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0081f580` · 推定シンボル `None` · 推定型 `None`
- [`00acbadc`](#insn-00acbadc) → [`00828e20`](../00828/00828e20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00828e20` · 推定シンボル `None` · 推定型 `None`
- [`00acbae4`](#insn-00acbae4) → [`00acbc18`](#insn-00acbc18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbaf4`](#insn-00acbaf4) → `00c1b450`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acbafc`](#insn-00acbafc) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb00`](#insn-00acbb00) → `00c0f7c8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acbb00`](#insn-00acbb00) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb04`](#insn-00acbb04) → `00c26650`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acbb08`](#insn-00acbb08) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb20`](#insn-00acbb20) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb28`](#insn-00acbb28) → [`00acbb38`](#insn-00acbb38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb2c`](#insn-00acbb2c) → [`00acbb4c`](#insn-00acbb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb34`](#insn-00acbb34) → [`00acbb40`](#insn-00acbb40) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb40`](#insn-00acbb40) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb44`](#insn-00acbb44) → `00c0f7e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acbb44`](#insn-00acbb44) → `00c0f7f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acbb48`](#insn-00acbb48) → [`00acd5b0`](../00acd/00acd5b0.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00acd5b0` · 推定シンボル `None` · 推定型 `None`
- [`00acbb48`](#insn-00acbb48) → [`00acd5b4`](../00acd/00acd5b4.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00acd5b4` · 推定シンボル `None` · 推定型 `None`
- [`00acbb4c`](#insn-00acbb4c) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb50`](#insn-00acbb50) → [`00acbb7c`](#insn-00acbb7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb5c`](#insn-00acbb5c) → [`00bd6e90`](../00bd6/00bd6e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e90` · 推定シンボル `None` · 推定型 `None`
- [`00acbb60`](#insn-00acbb60) → [`00acbb7c`](#insn-00acbb7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbb78`](#insn-00acbb78) → [`00bdb030`](../00bdb/00bdb030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb030` · 推定シンボル `None` · 推定型 `None`
- [`00acbb7c`](#insn-00acbb7c) → [`00bdb070`](../00bdb/00bdb070.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb070` · 推定シンボル `None` · 推定型 `None`
- [`00acbba8`](#insn-00acbba8) → [`00acbc84`](#insn-00acbc84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbb8`](#insn-00acbbb8) → [`00acbc84`](#insn-00acbc84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbc0`](#insn-00acbbc0) → [`00bd65f8`](../00bd6/00bd65f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd65f8` · 推定シンボル `None` · 推定型 `None`
- [`00acbbc8`](#insn-00acbbc8) → `002b0de0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbcc`](#insn-00acbbcc) → [`00bd6558`](../00bd6/00bd6558.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6558` · 推定シンボル `None` · 推定型 `None`
- [`00acbbd4`](#insn-00acbbd4) → [`00acbc04`](#insn-00acbc04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbf0`](#insn-00acbbf0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbbf8`](#insn-00acbbf8) → [`00acbc0c`](#insn-00acbc0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc00`](#insn-00acbc00) → [`00acbc08`](#insn-00acbc08) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc08`](#insn-00acbc08) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc10`](#insn-00acbc10) → [`00bdb640`](../00bdb/00bdb640.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb640` · 推定シンボル `None` · 推定型 `None`
- [`00acbc14`](#insn-00acbc14) → [`00acbc84`](#insn-00acbc84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc24`](#insn-00acbc24) → `00c1b450`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acbc2c`](#insn-00acbc2c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc30`](#insn-00acbc30) → `00c0f748`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acbc30`](#insn-00acbc30) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc34`](#insn-00acbc34) → `00c26650`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00acbc38`](#insn-00acbc38) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc50`](#insn-00acbc50) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc58`](#insn-00acbc58) → [`00acbc68`](#insn-00acbc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc5c`](#insn-00acbc5c) → [`00acbc7c`](#insn-00acbc7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc64`](#insn-00acbc64) → [`00acbc70`](#insn-00acbc70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc70`](#insn-00acbc70) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc74`](#insn-00acbc74) → `00c0f768`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00acbc74`](#insn-00acbc74) → `00c0f770`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00acbc78`](#insn-00acbc78) → [`00acd52c`](../00acd/00acd52c.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00acd52c` · 推定シンボル `None` · 推定型 `None`
- [`00acbc78`](#insn-00acbc78) → [`00acd530`](../00acd/00acd530.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00acd530` · 推定シンボル `None` · 推定型 `None`
- [`00acbc80`](#insn-00acbc80) → [`0052e34c`](../0052e/0052e34c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0052e34c` · 推定シンボル `None` · 推定型 `None`
- [`00acbc88`](#insn-00acbc88) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc90`](#insn-00acbc90) → [`00acbd10`](#insn-00acbd10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc94`](#insn-00acbc94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc98`](#insn-00acbc98) → `Stack[-0x18]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbc9c`](#insn-00acbc9c) → `Stack[-0x28]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbca0`](#insn-00acbca0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acbd10`](#insn-00acbd10) → [`00bdb090`](../00bdb/00bdb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb090` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acba40`](#insn-00acba40)

~~~json
{
  "source": "00acba40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba44`](#insn-00acba44)

~~~json
{
  "source": "00acba44",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba48`](#insn-00acba48)

~~~json
{
  "source": "00acba48",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba4c`](#insn-00acba4c)

~~~json
{
  "source": "00acba4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba5c`](#insn-00acba5c)

~~~json
{
  "source": "00acba5c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba60`](#insn-00acba60)

~~~json
{
  "source": "00acba60",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba64`](#insn-00acba64)

~~~json
{
  "source": "00acba64",
  "target": "00449be4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba68`](#insn-00acba68)

~~~json
{
  "source": "00acba68",
  "target": "00acba94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba70`](#insn-00acba70)

~~~json
{
  "source": "00acba70",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba78`](#insn-00acba78)

~~~json
{
  "source": "00acba78",
  "target": "00acbd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba7c`](#insn-00acba7c)

~~~json
{
  "source": "00acba7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba80`](#insn-00acba80)

~~~json
{
  "source": "00acba80",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba84`](#insn-00acba84)

~~~json
{
  "source": "00acba84",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba88`](#insn-00acba88)

~~~json
{
  "source": "00acba88",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acba90`](#insn-00acba90)

~~~json
{
  "source": "00acba90",
  "target": "00574768",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba94`](#insn-00acba94)

~~~json
{
  "source": "00acba94",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba98`](#insn-00acba98)

~~~json
{
  "source": "00acba98",
  "target": "00449bb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acba9c`](#insn-00acba9c)

~~~json
{
  "source": "00acba9c",
  "target": "00acbc84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbaa0`](#insn-00acbaa0)

~~~json
{
  "source": "00acbaa0",
  "target": "00bdb070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbaa8`](#insn-00acbaa8)

~~~json
{
  "source": "00acbaa8",
  "target": "0041be0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbaac`](#insn-00acbaac)

~~~json
{
  "source": "00acbaac",
  "target": "0041c9e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbab0`](#insn-00acbab0)

~~~json
{
  "source": "00acbab0",
  "target": "004723a8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbab4`](#insn-00acbab4)

~~~json
{
  "source": "00acbab4",
  "target": "00acbae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbab8`](#insn-00acbab8)

~~~json
{
  "source": "00acbab8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbabc`](#insn-00acbabc)

~~~json
{
  "source": "00acbabc",
  "target": "00828e20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbac4`](#insn-00acbac4)

~~~json
{
  "source": "00acbac4",
  "target": "00acbae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbac8`](#insn-00acbac8)

~~~json
{
  "source": "00acbac8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbacc`](#insn-00acbacc)

~~~json
{
  "source": "00acbacc",
  "target": "00828e20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbad4`](#insn-00acbad4)

~~~json
{
  "source": "00acbad4",
  "target": "00acbae8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbad8`](#insn-00acbad8)

~~~json
{
  "source": "00acbad8",
  "target": "0081f580",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbadc`](#insn-00acbadc)

~~~json
{
  "source": "00acbadc",
  "target": "00828e20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbae4`](#insn-00acbae4)

~~~json
{
  "source": "00acbae4",
  "target": "00acbc18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbaf4`](#insn-00acbaf4)

~~~json
{
  "source": "00acbaf4",
  "target": "00c1b450",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b450",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbafc`](#insn-00acbafc)

~~~json
{
  "source": "00acbafc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb00`](#insn-00acbb00)

~~~json
{
  "source": "00acbb00",
  "target": "00c0f7c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f7c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbb00`](#insn-00acbb00)

~~~json
{
  "source": "00acbb00",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb04`](#insn-00acbb04)

~~~json
{
  "source": "00acbb04",
  "target": "00c26650",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26650",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acbb08`](#insn-00acbb08)

~~~json
{
  "source": "00acbb08",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb20`](#insn-00acbb20)

~~~json
{
  "source": "00acbb20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb28`](#insn-00acbb28)

~~~json
{
  "source": "00acbb28",
  "target": "00acbb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb2c`](#insn-00acbb2c)

~~~json
{
  "source": "00acbb2c",
  "target": "00acbb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb34`](#insn-00acbb34)

~~~json
{
  "source": "00acbb34",
  "target": "00acbb40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb40`](#insn-00acbb40)

~~~json
{
  "source": "00acbb40",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb44`](#insn-00acbb44)

~~~json
{
  "source": "00acbb44",
  "target": "00c0f7e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f7e8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbb44`](#insn-00acbb44)

~~~json
{
  "source": "00acbb44",
  "target": "00c0f7f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f7f0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbb48`](#insn-00acbb48)

~~~json
{
  "source": "00acbb48",
  "target": "00acd5b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb48`](#insn-00acbb48)

~~~json
{
  "source": "00acbb48",
  "target": "00acd5b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb4c`](#insn-00acbb4c)

~~~json
{
  "source": "00acbb4c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb50`](#insn-00acbb50)

~~~json
{
  "source": "00acbb50",
  "target": "00acbb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb5c`](#insn-00acbb5c)

~~~json
{
  "source": "00acbb5c",
  "target": "00bd6e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb60`](#insn-00acbb60)

~~~json
{
  "source": "00acbb60",
  "target": "00acbb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbb78`](#insn-00acbb78)

~~~json
{
  "source": "00acbb78",
  "target": "00bdb030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbb7c`](#insn-00acbb7c)

~~~json
{
  "source": "00acbb7c",
  "target": "00bdb070",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbba8`](#insn-00acbba8)

~~~json
{
  "source": "00acbba8",
  "target": "00acbc84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbb8`](#insn-00acbbb8)

~~~json
{
  "source": "00acbbb8",
  "target": "00acbc84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbc0`](#insn-00acbbc0)

~~~json
{
  "source": "00acbbc0",
  "target": "00bd65f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbbc8`](#insn-00acbbc8)

~~~json
{
  "source": "00acbbc8",
  "target": "002b0de0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbcc`](#insn-00acbbcc)

~~~json
{
  "source": "00acbbcc",
  "target": "00bd6558",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbbd4`](#insn-00acbbd4)

~~~json
{
  "source": "00acbbd4",
  "target": "00acbc04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbf0`](#insn-00acbbf0)

~~~json
{
  "source": "00acbbf0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbbf8`](#insn-00acbbf8)

~~~json
{
  "source": "00acbbf8",
  "target": "00acbc0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc00`](#insn-00acbc00)

~~~json
{
  "source": "00acbc00",
  "target": "00acbc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc08`](#insn-00acbc08)

~~~json
{
  "source": "00acbc08",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc10`](#insn-00acbc10)

~~~json
{
  "source": "00acbc10",
  "target": "00bdb640",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbc14`](#insn-00acbc14)

~~~json
{
  "source": "00acbc14",
  "target": "00acbc84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc24`](#insn-00acbc24)

~~~json
{
  "source": "00acbc24",
  "target": "00c1b450",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b450",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbc2c`](#insn-00acbc2c)

~~~json
{
  "source": "00acbc2c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc30`](#insn-00acbc30)

~~~json
{
  "source": "00acbc30",
  "target": "00c0f748",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f748",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbc30`](#insn-00acbc30)

~~~json
{
  "source": "00acbc30",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc34`](#insn-00acbc34)

~~~json
{
  "source": "00acbc34",
  "target": "00c26650",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c26650",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00acbc38`](#insn-00acbc38)

~~~json
{
  "source": "00acbc38",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc50`](#insn-00acbc50)

~~~json
{
  "source": "00acbc50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc58`](#insn-00acbc58)

~~~json
{
  "source": "00acbc58",
  "target": "00acbc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc5c`](#insn-00acbc5c)

~~~json
{
  "source": "00acbc5c",
  "target": "00acbc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc64`](#insn-00acbc64)

~~~json
{
  "source": "00acbc64",
  "target": "00acbc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc70`](#insn-00acbc70)

~~~json
{
  "source": "00acbc70",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc74`](#insn-00acbc74)

~~~json
{
  "source": "00acbc74",
  "target": "00c0f768",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f768",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbc74`](#insn-00acbc74)

~~~json
{
  "source": "00acbc74",
  "target": "00c0f770",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c0f770",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00acbc78`](#insn-00acbc78)

~~~json
{
  "source": "00acbc78",
  "target": "00acd52c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbc78`](#insn-00acbc78)

~~~json
{
  "source": "00acbc78",
  "target": "00acd530",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbc80`](#insn-00acbc80)

~~~json
{
  "source": "00acbc80",
  "target": "0052e34c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acbc88`](#insn-00acbc88)

~~~json
{
  "source": "00acbc88",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc90`](#insn-00acbc90)

~~~json
{
  "source": "00acbc90",
  "target": "00acbd10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc94`](#insn-00acbc94)

~~~json
{
  "source": "00acbc94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc98`](#insn-00acbc98)

~~~json
{
  "source": "00acbc98",
  "target": "Stack[-0x18]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbc9c`](#insn-00acbc9c)

~~~json
{
  "source": "00acbc9c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbca0`](#insn-00acbca0)

~~~json
{
  "source": "00acbca0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acbd10`](#insn-00acbd10)

~~~json
{
  "source": "00acbd10",
  "target": "00bdb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
