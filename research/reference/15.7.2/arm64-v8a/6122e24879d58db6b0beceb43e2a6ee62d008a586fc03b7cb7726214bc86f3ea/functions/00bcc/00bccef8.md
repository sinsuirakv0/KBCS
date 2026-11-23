# 00bccef8

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bccfc0`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcc/00bccfc0.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-0ebed47433609f751b19241e79f87592)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccef8",
  "name": "FUN_00bccef8",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df18a9da23c95f4cb2b17bd6d7b8c79ba37e105eb2297fe62f30dd73a4539464",
  "source_text_sha256": "df18a9da23c95f4cb2b17bd6d7b8c79ba37e105eb2297fe62f30dd73a4539464",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccef8",
        "00bcd09f"
      ]
    ],
    "bytes_sha256": "24523c875cfa7276e131b98f3e80dcc6a5c3ac9ff78537f2800ee7ff0993c1e9",
    "instruction_count": 106,
    "instruction_bytes": 424,
    "body_bytes": 424,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

- [00bcc774](../00bcc/00bcc774.md)
- [00bce438](../00bce/00bce438.md)

## 呼び出し先

- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2623 bytes

~~~c

void FUN_00bccef8(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  undefined4 uVar2;
  undefined4 uVar3;
  uint uVar4;
  void *pvVar5;
  long lVar6;
  size_t sVar7;
  long *plVar8;
  uint uVar9;
  long lVar10;
  
                    /* try { // try from 00bccf00 to 00ccd27f has its CatchHandler @ 00bcce84 */
  plVar8 = *(long **)(param_1 + 0x10);
  lVar10 = param_2[1];
  uVar2 = *(undefined4 *)(param_2 + 3);
  uVar3 = *(undefined4 *)((long)param_2 + 0x1c);
  lVar6 = *plVar8;
  param_2[3] = 0xffffffffffffffff;
  (**(code **)(lVar6 + 0x20))(plVar8);
  if ((*(ushort *)((long)plVar8 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar8 + 0x28))(plVar8,param_2);
  }
  uVar4 = *(uint *)((long)param_2 + 0x1c);
  if (uVar4 == 0xffffffff) {
    lVar10 = param_2[1];
    pvVar5 = (void *)*param_2;
    if ((ulong)param_2[2] < lVar10 + 3U) {
      sVar7 = param_2[2] * 2;
      uVar1 = lVar10 + 0x3e3;
      if (sVar7 < uVar1 || sVar7 - uVar1 == 0) {
        sVar7 = uVar1;
      }
      param_2[2] = sVar7;
      pvVar5 = realloc(pvVar5,sVar7);
      *param_2 = pvVar5;
      if (pvVar5 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar10 = param_2[1];
    }
    *(undefined1 *)((undefined2 *)((long)pvVar5 + lVar10) + 1) = 0x2e;
    *(undefined2 *)((long)pvVar5 + lVar10) = 0x2e2e;
    lVar10 = param_2[1] + 3;
  }
  else if (uVar4 != 0) {
    if (1 < uVar4) {
      uVar9 = 1;
      do {
        lVar10 = param_2[1];
        pvVar5 = (void *)*param_2;
        if ((ulong)param_2[2] < lVar10 + 2U) {
          sVar7 = param_2[2] * 2;
          uVar1 = lVar10 + 0x3e2;
          if (sVar7 < uVar1 || sVar7 - uVar1 == 0) {
            sVar7 = uVar1;
          }
          param_2[2] = sVar7;
          pvVar5 = realloc(pvVar5,sVar7);
          *param_2 = pvVar5;
          if (pvVar5 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
            abort();
          }
          lVar10 = param_2[1];
        }
        *(undefined2 *)((long)pvVar5 + lVar10) = 0x202c;
        plVar8 = *(long **)(param_1 + 0x10);
        *(uint *)(param_2 + 3) = uVar9;
        lVar10 = *plVar8;
        param_2[1] = param_2[1] + 2;
        (**(code **)(lVar10 + 0x20))(plVar8,param_2);
        if ((*(ushort *)((long)plVar8 + 9) & 0xc0) != 0x40) {
          (**(code **)(*plVar8 + 0x28))(plVar8,param_2);
        }
        uVar9 = uVar9 + 1;
      } while (uVar4 != uVar9);
    }
    goto LAB_00bcd078;
  }
  param_2[1] = lVar10;
LAB_00bcd078:
  *(undefined4 *)(param_2 + 3) = uVar2;
  *(undefined4 *)((long)param_2 + 0x1c) = uVar3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccef8"></a> `00bccef8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bccefc"></a> `00bccefc` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bccf00"></a> `00bccf00` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccf04"></a> `00bccf04` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccf08"></a> `00bccf08` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bccf0c"></a> `00bccf0c` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bccf10"></a> `00bccf10` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bccf14"></a> `00bccf14` | `e0 e7 07 6f` | movi v0.2D,#-0x1 | `FALL_THROUGH`
<a id="insn-00bccf18"></a> `00bccf18` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bccf1c"></a> `00bccf1c` | `39 04 40 f9` | ldr x25,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bccf20"></a> `00bccf20` | `36 5c 43 29` | ldp w22,w23,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bccf24"></a> `00bccf24` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bccf28"></a> `00bccf28` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bccf2c"></a> `00bccf2c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bccf30"></a> `00bccf30` | `20 0c 00 fd` | str d0,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bccf34"></a> `00bccf34` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bccf38"></a> `00bccf38` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bccf3c"></a> `00bccf3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bccf40"></a> `00bccf40` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bccf44"></a> `00bccf44` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bccf48"></a> `00bccf48` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bccf4c"></a> `00bccf4c` | `c0 00 00 54` | b.eq 0x00bccf64 | `CONDITIONAL_JUMP`
<a id="insn-00bccf50"></a> `00bccf50` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bccf54"></a> `00bccf54` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bccf58"></a> `00bccf58` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bccf5c"></a> `00bccf5c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bccf60"></a> `00bccf60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bccf64"></a> `00bccf64` | `78 1e 40 b9` | ldr w24,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00bccf68"></a> `00bccf68` | `1f 07 00 31` | cmn w24,#0x1 | `FALL_THROUGH`
<a id="insn-00bccf6c"></a> `00bccf6c` | `a0 05 00 54` | b.eq 0x00bcd020 | `CONDITIONAL_JUMP`
<a id="insn-00bccf70"></a> `00bccf70` | `38 08 00 34` | cbz w24,0x00bcd074 | `CONDITIONAL_JUMP`
<a id="insn-00bccf74"></a> `00bccf74` | `1f 0b 00 71` | cmp w24,#0x2 | `FALL_THROUGH`
<a id="insn-00bccf78"></a> `00bccf78` | `03 08 00 54` | b.cc 0x00bcd078 | `CONDITIONAL_JUMP`
<a id="insn-00bccf7c"></a> `00bccf7c` | `39 00 80 52` | mov w25,#0x1 | `FALL_THROUGH`
<a id="insn-00bccf80"></a> `00bccf80` | `9a 05 84 52` | mov w26,#0x202c | `FALL_THROUGH`
<a id="insn-00bccf84"></a> `00bccf84` | `04 00 00 14` | b 0x00bccf94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bccf88"></a> `00bccf88` | `39 07 00 11` | add w25,w25,#0x1 | `FALL_THROUGH`
<a id="insn-00bccf8c"></a> `00bccf8c` | `1f 03 19 6b` | cmp w24,w25 | `FALL_THROUGH`
<a id="insn-00bccf90"></a> `00bccf90` | `40 07 00 54` | b.eq 0x00bcd078 | `CONDITIONAL_JUMP`
<a id="insn-00bccf94"></a> `00bccf94` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bccf98"></a> `00bccf98` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bccf9c"></a> `00bccf9c` | `0a 09 00 91` | add x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bccfa0"></a> `00bccfa0` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bccfa4"></a> `00bccfa4` | `49 01 00 54` | b.ls 0x00bccfcc | `CONDITIONAL_JUMP`
<a id="insn-00bccfa8"></a> `00bccfa8` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bccfac"></a> `00bccfac` | `08 89 0f 91` | add x8,x8,#0x3e2 | `FALL_THROUGH`
<a id="insn-00bccfb0"></a> `00bccfb0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bccfb4"></a> `00bccfb4` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bccfb8"></a> `00bccfb8` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bccfbc"></a> `00bccfbc` | `65 40 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bccfc0"></a> `00bccfc0` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bccfc4"></a> `00bccfc4` | `a0 06 00 b4` | cbz x0,0x00bcd098 | `CONDITIONAL_JUMP`
<a id="insn-00bccfc8"></a> `00bccfc8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bccfcc"></a> `00bccfcc` | `1a 68 28 78` | strh w26,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bccfd0"></a> `00bccfd0` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bccfd4"></a> `00bccfd4` | `95 0a 40 f9` | ldr x21,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bccfd8"></a> `00bccfd8` | `79 1a 00 b9` | str w25,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bccfdc"></a> `00bccfdc` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bccfe0"></a> `00bccfe0` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00bccfe4"></a> `00bccfe4` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bccfe8"></a> `00bccfe8` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bccfec"></a> `00bccfec` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bccff0"></a> `00bccff0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bccff4"></a> `00bccff4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bccff8"></a> `00bccff8` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bccffc"></a> `00bccffc` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcd000"></a> `00bcd000` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcd004"></a> `00bcd004` | `20 fc ff 54` | b.eq 0x00bccf88 | `CONDITIONAL_JUMP`
<a id="insn-00bcd008"></a> `00bcd008` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcd00c"></a> `00bcd00c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcd010"></a> `00bcd010` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd014"></a> `00bcd014` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcd018"></a> `00bcd018` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd01c"></a> `00bcd01c` | `db ff ff 17` | b 0x00bccf88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcd020"></a> `00bcd020` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd024"></a> `00bcd024` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd028"></a> `00bcd028` | `0a 0d 00 91` | add x10,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bcd02c"></a> `00bcd02c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcd030"></a> `00bcd030` | `49 01 00 54` | b.ls 0x00bcd058 | `CONDITIONAL_JUMP`
<a id="insn-00bcd034"></a> `00bcd034` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd038"></a> `00bcd038` | `08 8d 0f 91` | add x8,x8,#0x3e3 | `FALL_THROUGH`
<a id="insn-00bcd03c"></a> `00bcd03c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcd040"></a> `00bcd040` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcd044"></a> `00bcd044` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd048"></a> `00bcd048` | `42 40 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd04c"></a> `00bcd04c` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd050"></a> `00bcd050` | `60 02 00 b4` | cbz x0,0x00bcd09c | `CONDITIONAL_JUMP`
<a id="insn-00bcd054"></a> `00bcd054` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd058"></a> `00bcd058` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcd05c"></a> `00bcd05c` | `c9 05 80 52` | mov w9,#0x2e | `FALL_THROUGH`
<a id="insn-00bcd060"></a> `00bcd060` | `ca c5 85 52` | mov w10,#0x2e2e | `FALL_THROUGH`
<a id="insn-00bcd064"></a> `00bcd064` | `09 09 00 39` | strb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bcd068"></a> `00bcd068` | `0a 01 00 79` | strh w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcd06c"></a> `00bcd06c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd070"></a> `00bcd070` | `19 0d 00 91` | add x25,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bcd074"></a> `00bcd074` | `79 06 00 f9` | str x25,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd078"></a> `00bcd078` | `76 5e 03 29` | stp w22,w23,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bcd07c"></a> `00bcd07c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcd080"></a> `00bcd080` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcd084"></a> `00bcd084` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd088"></a> `00bcd088` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd08c"></a> `00bcd08c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcd090"></a> `00bcd090` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcd094"></a> `00bcd094` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcd098"></a> `00bcd098` | `4a 44 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bcd09c"></a> `00bcd09c` | `49 44 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccef8`](#insn-00bccef8) 範囲 `[['00bccef8', '00bcceff']]`
  - `FALL_THROUGH` [`00bccefc`](#insn-00bccefc) → [`00bccf00`](#insn-00bccf00)
- ブロック [`00bccf00`](#insn-00bccf00) 範囲 `[['00bccf00', '00bccf4f']]`
  - `CONDITIONAL_JUMP` [`00bccf4c`](#insn-00bccf4c) → [`00bccf64`](#insn-00bccf64)
  - `FALL_THROUGH` [`00bccf4c`](#insn-00bccf4c) → [`00bccf50`](#insn-00bccf50)
- ブロック [`00bccf50`](#insn-00bccf50) 範囲 `[['00bccf50', '00bccf63']]`
  - `FALL_THROUGH` [`00bccf60`](#insn-00bccf60) → [`00bccf64`](#insn-00bccf64)
- ブロック [`00bccf64`](#insn-00bccf64) 範囲 `[['00bccf64', '00bccf6f']]`
  - `CONDITIONAL_JUMP` [`00bccf6c`](#insn-00bccf6c) → [`00bcd020`](#insn-00bcd020)
  - `FALL_THROUGH` [`00bccf6c`](#insn-00bccf6c) → [`00bccf70`](#insn-00bccf70)
- ブロック [`00bccf70`](#insn-00bccf70) 範囲 `[['00bccf70', '00bccf73']]`
  - `CONDITIONAL_JUMP` [`00bccf70`](#insn-00bccf70) → [`00bcd074`](#insn-00bcd074)
  - `FALL_THROUGH` [`00bccf70`](#insn-00bccf70) → [`00bccf74`](#insn-00bccf74)
- ブロック [`00bccf74`](#insn-00bccf74) 範囲 `[['00bccf74', '00bccf7b']]`
  - `CONDITIONAL_JUMP` [`00bccf78`](#insn-00bccf78) → [`00bcd078`](#insn-00bcd078)
  - `FALL_THROUGH` [`00bccf78`](#insn-00bccf78) → [`00bccf7c`](#insn-00bccf7c)
- ブロック [`00bccf7c`](#insn-00bccf7c) 範囲 `[['00bccf7c', '00bccf87']]`
  - `UNCONDITIONAL_JUMP` [`00bccf84`](#insn-00bccf84) → [`00bccf94`](#insn-00bccf94)
- ブロック [`00bccf88`](#insn-00bccf88) 範囲 `[['00bccf88', '00bccf93']]`
  - `CONDITIONAL_JUMP` [`00bccf90`](#insn-00bccf90) → [`00bcd078`](#insn-00bcd078)
  - `FALL_THROUGH` [`00bccf90`](#insn-00bccf90) → [`00bccf94`](#insn-00bccf94)
- ブロック [`00bccf94`](#insn-00bccf94) 範囲 `[['00bccf94', '00bccfa7']]`
  - `CONDITIONAL_JUMP` [`00bccfa4`](#insn-00bccfa4) → [`00bccfcc`](#insn-00bccfcc)
  - `FALL_THROUGH` [`00bccfa4`](#insn-00bccfa4) → [`00bccfa8`](#insn-00bccfa8)
- ブロック [`00bccfa8`](#insn-00bccfa8) 範囲 `[['00bccfa8', '00bccfc7']]`
  - `CONDITIONAL_JUMP` [`00bccfc4`](#insn-00bccfc4) → [`00bcd098`](#insn-00bcd098)
  - `FALL_THROUGH` [`00bccfc4`](#insn-00bccfc4) → [`00bccfc8`](#insn-00bccfc8)
- ブロック [`00bccfc8`](#insn-00bccfc8) 範囲 `[['00bccfc8', '00bccfcb']]`
  - `FALL_THROUGH` [`00bccfc8`](#insn-00bccfc8) → [`00bccfcc`](#insn-00bccfcc)
- ブロック [`00bccfcc`](#insn-00bccfcc) 範囲 `[['00bccfcc', '00bcd007']]`
  - `CONDITIONAL_JUMP` [`00bcd004`](#insn-00bcd004) → [`00bccf88`](#insn-00bccf88)
  - `FALL_THROUGH` [`00bcd004`](#insn-00bcd004) → [`00bcd008`](#insn-00bcd008)
- ブロック [`00bcd008`](#insn-00bcd008) 範囲 `[['00bcd008', '00bcd01f']]`
  - `UNCONDITIONAL_JUMP` [`00bcd01c`](#insn-00bcd01c) → [`00bccf88`](#insn-00bccf88)
- ブロック [`00bcd020`](#insn-00bcd020) 範囲 `[['00bcd020', '00bcd033']]`
  - `CONDITIONAL_JUMP` [`00bcd030`](#insn-00bcd030) → [`00bcd058`](#insn-00bcd058)
  - `FALL_THROUGH` [`00bcd030`](#insn-00bcd030) → [`00bcd034`](#insn-00bcd034)
- ブロック [`00bcd034`](#insn-00bcd034) 範囲 `[['00bcd034', '00bcd053']]`
  - `CONDITIONAL_JUMP` [`00bcd050`](#insn-00bcd050) → [`00bcd09c`](#insn-00bcd09c)
  - `FALL_THROUGH` [`00bcd050`](#insn-00bcd050) → [`00bcd054`](#insn-00bcd054)
- ブロック [`00bcd054`](#insn-00bcd054) 範囲 `[['00bcd054', '00bcd057']]`
  - `FALL_THROUGH` [`00bcd054`](#insn-00bcd054) → [`00bcd058`](#insn-00bcd058)
- ブロック [`00bcd058`](#insn-00bcd058) 範囲 `[['00bcd058', '00bcd073']]`
  - `FALL_THROUGH` [`00bcd070`](#insn-00bcd070) → [`00bcd074`](#insn-00bcd074)
- ブロック [`00bcd074`](#insn-00bcd074) 範囲 `[['00bcd074', '00bcd077']]`
  - `FALL_THROUGH` [`00bcd074`](#insn-00bcd074) → [`00bcd078`](#insn-00bcd078)
- ブロック [`00bcd078`](#insn-00bcd078) 範囲 `[['00bcd078', '00bcd097']]`
- ブロック [`00bcd098`](#insn-00bcd098) 範囲 `[['00bcd098', '00bcd09b']]`
- ブロック [`00bcd09c`](#insn-00bcd09c) 範囲 `[['00bcd09c', '00bcd09f']]`

## 命令位置別の参照

- [`00bccefc`](#insn-00bccefc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf00`](#insn-00bccf00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf04`](#insn-00bccf04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf08`](#insn-00bccf08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf0c`](#insn-00bccf0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf4c`](#insn-00bccf4c) → [`00bccf64`](#insn-00bccf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf6c`](#insn-00bccf6c) → [`00bcd020`](#insn-00bcd020) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf70`](#insn-00bccf70) → [`00bcd074`](#insn-00bcd074) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf78`](#insn-00bccf78) → [`00bcd078`](#insn-00bcd078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf84`](#insn-00bccf84) → [`00bccf94`](#insn-00bccf94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccf90`](#insn-00bccf90) → [`00bcd078`](#insn-00bcd078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfa4`](#insn-00bccfa4) → [`00bccfcc`](#insn-00bccfcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfbc`](#insn-00bccfbc) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bccfc4`](#insn-00bccfc4) → [`00bcd098`](#insn-00bcd098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd004`](#insn-00bcd004) → [`00bccf88`](#insn-00bccf88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd01c`](#insn-00bcd01c) → [`00bccf88`](#insn-00bccf88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd030`](#insn-00bcd030) → [`00bcd058`](#insn-00bcd058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd048`](#insn-00bcd048) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcd050`](#insn-00bcd050) → [`00bcd09c`](#insn-00bcd09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd07c`](#insn-00bcd07c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd080`](#insn-00bcd080) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd084`](#insn-00bcd084) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd088`](#insn-00bcd088) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd08c`](#insn-00bcd08c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd098`](#insn-00bcd098) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcd09c`](#insn-00bcd09c) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccefc`](#insn-00bccefc)

~~~json
{
  "source": "00bccefc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf00`](#insn-00bccf00)

~~~json
{
  "source": "00bccf00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf04`](#insn-00bccf04)

~~~json
{
  "source": "00bccf04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf08`](#insn-00bccf08)

~~~json
{
  "source": "00bccf08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf0c`](#insn-00bccf0c)

~~~json
{
  "source": "00bccf0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf4c`](#insn-00bccf4c)

~~~json
{
  "source": "00bccf4c",
  "target": "00bccf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf6c`](#insn-00bccf6c)

~~~json
{
  "source": "00bccf6c",
  "target": "00bcd020",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf70`](#insn-00bccf70)

~~~json
{
  "source": "00bccf70",
  "target": "00bcd074",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf78`](#insn-00bccf78)

~~~json
{
  "source": "00bccf78",
  "target": "00bcd078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf84`](#insn-00bccf84)

~~~json
{
  "source": "00bccf84",
  "target": "00bccf94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccf90`](#insn-00bccf90)

~~~json
{
  "source": "00bccf90",
  "target": "00bcd078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfa4`](#insn-00bccfa4)

~~~json
{
  "source": "00bccfa4",
  "target": "00bccfcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfbc`](#insn-00bccfbc)

~~~json
{
  "source": "00bccfbc",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bccfc4`](#insn-00bccfc4)

~~~json
{
  "source": "00bccfc4",
  "target": "00bcd098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd004`](#insn-00bcd004)

~~~json
{
  "source": "00bcd004",
  "target": "00bccf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd01c`](#insn-00bcd01c)

~~~json
{
  "source": "00bcd01c",
  "target": "00bccf88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd030`](#insn-00bcd030)

~~~json
{
  "source": "00bcd030",
  "target": "00bcd058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd048`](#insn-00bcd048)

~~~json
{
  "source": "00bcd048",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd050`](#insn-00bcd050)

~~~json
{
  "source": "00bcd050",
  "target": "00bcd09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd07c`](#insn-00bcd07c)

~~~json
{
  "source": "00bcd07c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd080`](#insn-00bcd080)

~~~json
{
  "source": "00bcd080",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd084`](#insn-00bcd084)

~~~json
{
  "source": "00bcd084",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd088`](#insn-00bcd088)

~~~json
{
  "source": "00bcd088",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd08c`](#insn-00bcd08c)

~~~json
{
  "source": "00bcd08c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd098`](#insn-00bcd098)

~~~json
{
  "source": "00bcd098",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd09c`](#insn-00bcd09c)

~~~json
{
  "source": "00bcd09c",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
