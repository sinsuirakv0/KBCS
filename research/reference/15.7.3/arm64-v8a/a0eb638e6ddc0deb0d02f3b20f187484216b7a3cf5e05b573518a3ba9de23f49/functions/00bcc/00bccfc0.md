# 00bccfc0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bccef8`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcc/00bccef8.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-0ebed47433609f751b19241e79f87592)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bcd004`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd004.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-5eecc5068ccab37e9af33cd31bfcfa83)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bccfc0",
  "name": "FUN_00bccfc0",
  "size": 424,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e4488ffb81103c67441714cce8c9a0e3f7441617a22d2faf718b87a85177407d",
  "source_text_sha256": "e4488ffb81103c67441714cce8c9a0e3f7441617a22d2faf718b87a85177407d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bccfc0",
        "00bcd167"
      ]
    ],
    "bytes_sha256": "cc5102a9b3cfd4faf4dc501cd765baa9f93976a8e79b7ae111dce0c1a187896d",
    "instruction_count": 106,
    "instruction_bytes": 424,
    "body_bytes": 424,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

- [00bcc83c](../00bcc/00bcc83c.md)
- [00bce500](../00bce/00bce500.md)

## 呼び出し先

- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2623 bytes

~~~c

void FUN_00bccfc0(long param_1,undefined8 *param_2)

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
  
                    /* try { // try from 00bccfc8 to 00ccd347 has its CatchHandler @ 00bccf4c */
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
    goto LAB_00bcd140;
  }
  param_2[1] = lVar10;
LAB_00bcd140:
  *(undefined4 *)(param_2 + 3) = uVar2;
  *(undefined4 *)((long)param_2 + 0x1c) = uVar3;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bccfc0"></a> `00bccfc0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bccfc4"></a> `00bccfc4` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bccfc8"></a> `00bccfc8` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bccfcc"></a> `00bccfcc` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bccfd0"></a> `00bccfd0` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bccfd4"></a> `00bccfd4` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bccfd8"></a> `00bccfd8` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bccfdc"></a> `00bccfdc` | `e0 e7 07 6f` | movi v0.2D,#-0x1 | `FALL_THROUGH`
<a id="insn-00bccfe0"></a> `00bccfe0` | `15 08 40 f9` | ldr x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bccfe4"></a> `00bccfe4` | `39 04 40 f9` | ldr x25,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bccfe8"></a> `00bccfe8` | `36 5c 43 29` | ldp w22,w23,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bccfec"></a> `00bccfec` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bccff0"></a> `00bccff0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bccff4"></a> `00bccff4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bccff8"></a> `00bccff8` | `20 0c 00 fd` | str d0,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bccffc"></a> `00bccffc` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd000"></a> `00bcd000` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd004"></a> `00bcd004` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd008"></a> `00bcd008` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcd00c"></a> `00bcd00c` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcd010"></a> `00bcd010` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcd014"></a> `00bcd014` | `c0 00 00 54` | b.eq 0x00bcd02c | `CONDITIONAL_JUMP`
<a id="insn-00bcd018"></a> `00bcd018` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcd01c"></a> `00bcd01c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcd020"></a> `00bcd020` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd024"></a> `00bcd024` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcd028"></a> `00bcd028` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd02c"></a> `00bcd02c` | `78 1e 40 b9` | ldr w24,[x19, #0x1c] | `FALL_THROUGH`
<a id="insn-00bcd030"></a> `00bcd030` | `1f 07 00 31` | cmn w24,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd034"></a> `00bcd034` | `a0 05 00 54` | b.eq 0x00bcd0e8 | `CONDITIONAL_JUMP`
<a id="insn-00bcd038"></a> `00bcd038` | `38 08 00 34` | cbz w24,0x00bcd13c | `CONDITIONAL_JUMP`
<a id="insn-00bcd03c"></a> `00bcd03c` | `1f 0b 00 71` | cmp w24,#0x2 | `FALL_THROUGH`
<a id="insn-00bcd040"></a> `00bcd040` | `03 08 00 54` | b.cc 0x00bcd140 | `CONDITIONAL_JUMP`
<a id="insn-00bcd044"></a> `00bcd044` | `39 00 80 52` | mov w25,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd048"></a> `00bcd048` | `9a 05 84 52` | mov w26,#0x202c | `FALL_THROUGH`
<a id="insn-00bcd04c"></a> `00bcd04c` | `04 00 00 14` | b 0x00bcd05c | `UNCONDITIONAL_JUMP`
<a id="insn-00bcd050"></a> `00bcd050` | `39 07 00 11` | add w25,w25,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd054"></a> `00bcd054` | `1f 03 19 6b` | cmp w24,w25 | `FALL_THROUGH`
<a id="insn-00bcd058"></a> `00bcd058` | `40 07 00 54` | b.eq 0x00bcd140 | `CONDITIONAL_JUMP`
<a id="insn-00bcd05c"></a> `00bcd05c` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd060"></a> `00bcd060` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd064"></a> `00bcd064` | `0a 09 00 91` | add x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bcd068"></a> `00bcd068` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcd06c"></a> `00bcd06c` | `49 01 00 54` | b.ls 0x00bcd094 | `CONDITIONAL_JUMP`
<a id="insn-00bcd070"></a> `00bcd070` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd074"></a> `00bcd074` | `08 89 0f 91` | add x8,x8,#0x3e2 | `FALL_THROUGH`
<a id="insn-00bcd078"></a> `00bcd078` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcd07c"></a> `00bcd07c` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcd080"></a> `00bcd080` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd084"></a> `00bcd084` | `5f 40 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd088"></a> `00bcd088` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd08c"></a> `00bcd08c` | `a0 06 00 b4` | cbz x0,0x00bcd160 | `CONDITIONAL_JUMP`
<a id="insn-00bcd090"></a> `00bcd090` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd094"></a> `00bcd094` | `1a 68 28 78` | strh w26,[x0, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bcd098"></a> `00bcd098` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd09c"></a> `00bcd09c` | `95 0a 40 f9` | ldr x21,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd0a0"></a> `00bcd0a0` | `79 1a 00 b9` | str w25,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bcd0a4"></a> `00bcd0a4` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bcd0a8"></a> `00bcd0a8` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00bcd0ac"></a> `00bcd0ac` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd0b0"></a> `00bcd0b0` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd0b4"></a> `00bcd0b4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd0b8"></a> `00bcd0b8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcd0bc"></a> `00bcd0bc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd0c0"></a> `00bcd0c0` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcd0c4"></a> `00bcd0c4` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcd0c8"></a> `00bcd0c8` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcd0cc"></a> `00bcd0cc` | `20 fc ff 54` | b.eq 0x00bcd050 | `CONDITIONAL_JUMP`
<a id="insn-00bcd0d0"></a> `00bcd0d0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcd0d4"></a> `00bcd0d4` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcd0d8"></a> `00bcd0d8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd0dc"></a> `00bcd0dc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcd0e0"></a> `00bcd0e0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd0e4"></a> `00bcd0e4` | `db ff ff 17` | b 0x00bcd050 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcd0e8"></a> `00bcd0e8` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd0ec"></a> `00bcd0ec` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd0f0"></a> `00bcd0f0` | `0a 0d 00 91` | add x10,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bcd0f4"></a> `00bcd0f4` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcd0f8"></a> `00bcd0f8` | `49 01 00 54` | b.ls 0x00bcd120 | `CONDITIONAL_JUMP`
<a id="insn-00bcd0fc"></a> `00bcd0fc` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd100"></a> `00bcd100` | `08 8d 0f 91` | add x8,x8,#0x3e3 | `FALL_THROUGH`
<a id="insn-00bcd104"></a> `00bcd104` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcd108"></a> `00bcd108` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcd10c"></a> `00bcd10c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd110"></a> `00bcd110` | `3c 40 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd114"></a> `00bcd114` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd118"></a> `00bcd118` | `60 02 00 b4` | cbz x0,0x00bcd164 | `CONDITIONAL_JUMP`
<a id="insn-00bcd11c"></a> `00bcd11c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd120"></a> `00bcd120` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcd124"></a> `00bcd124` | `c9 05 80 52` | mov w9,#0x2e | `FALL_THROUGH`
<a id="insn-00bcd128"></a> `00bcd128` | `ca c5 85 52` | mov w10,#0x2e2e | `FALL_THROUGH`
<a id="insn-00bcd12c"></a> `00bcd12c` | `09 09 00 39` | strb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bcd130"></a> `00bcd130` | `0a 01 00 79` | strh w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcd134"></a> `00bcd134` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd138"></a> `00bcd138` | `19 0d 00 91` | add x25,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bcd13c"></a> `00bcd13c` | `79 06 00 f9` | str x25,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd140"></a> `00bcd140` | `76 5e 03 29` | stp w22,w23,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bcd144"></a> `00bcd144` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcd148"></a> `00bcd148` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcd14c"></a> `00bcd14c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd150"></a> `00bcd150` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd154"></a> `00bcd154` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcd158"></a> `00bcd158` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcd15c"></a> `00bcd15c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcd160"></a> `00bcd160` | `44 44 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bcd164"></a> `00bcd164` | `43 44 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bccfc0`](#insn-00bccfc0) 範囲 `[['00bccfc0', '00bccfc7']]`
  - `FALL_THROUGH` [`00bccfc4`](#insn-00bccfc4) → [`00bccfc8`](#insn-00bccfc8)
- ブロック [`00bccfc8`](#insn-00bccfc8) 範囲 `[['00bccfc8', '00bcd017']]`
  - `CONDITIONAL_JUMP` [`00bcd014`](#insn-00bcd014) → [`00bcd02c`](#insn-00bcd02c)
  - `FALL_THROUGH` [`00bcd014`](#insn-00bcd014) → [`00bcd018`](#insn-00bcd018)
- ブロック [`00bcd018`](#insn-00bcd018) 範囲 `[['00bcd018', '00bcd02b']]`
  - `FALL_THROUGH` [`00bcd028`](#insn-00bcd028) → [`00bcd02c`](#insn-00bcd02c)
- ブロック [`00bcd02c`](#insn-00bcd02c) 範囲 `[['00bcd02c', '00bcd037']]`
  - `CONDITIONAL_JUMP` [`00bcd034`](#insn-00bcd034) → [`00bcd0e8`](#insn-00bcd0e8)
  - `FALL_THROUGH` [`00bcd034`](#insn-00bcd034) → [`00bcd038`](#insn-00bcd038)
- ブロック [`00bcd038`](#insn-00bcd038) 範囲 `[['00bcd038', '00bcd03b']]`
  - `CONDITIONAL_JUMP` [`00bcd038`](#insn-00bcd038) → [`00bcd13c`](#insn-00bcd13c)
  - `FALL_THROUGH` [`00bcd038`](#insn-00bcd038) → [`00bcd03c`](#insn-00bcd03c)
- ブロック [`00bcd03c`](#insn-00bcd03c) 範囲 `[['00bcd03c', '00bcd043']]`
  - `CONDITIONAL_JUMP` [`00bcd040`](#insn-00bcd040) → [`00bcd140`](#insn-00bcd140)
  - `FALL_THROUGH` [`00bcd040`](#insn-00bcd040) → [`00bcd044`](#insn-00bcd044)
- ブロック [`00bcd044`](#insn-00bcd044) 範囲 `[['00bcd044', '00bcd04f']]`
  - `UNCONDITIONAL_JUMP` [`00bcd04c`](#insn-00bcd04c) → [`00bcd05c`](#insn-00bcd05c)
- ブロック [`00bcd050`](#insn-00bcd050) 範囲 `[['00bcd050', '00bcd05b']]`
  - `CONDITIONAL_JUMP` [`00bcd058`](#insn-00bcd058) → [`00bcd140`](#insn-00bcd140)
  - `FALL_THROUGH` [`00bcd058`](#insn-00bcd058) → [`00bcd05c`](#insn-00bcd05c)
- ブロック [`00bcd05c`](#insn-00bcd05c) 範囲 `[['00bcd05c', '00bcd06f']]`
  - `CONDITIONAL_JUMP` [`00bcd06c`](#insn-00bcd06c) → [`00bcd094`](#insn-00bcd094)
  - `FALL_THROUGH` [`00bcd06c`](#insn-00bcd06c) → [`00bcd070`](#insn-00bcd070)
- ブロック [`00bcd070`](#insn-00bcd070) 範囲 `[['00bcd070', '00bcd08f']]`
  - `CONDITIONAL_JUMP` [`00bcd08c`](#insn-00bcd08c) → [`00bcd160`](#insn-00bcd160)
  - `FALL_THROUGH` [`00bcd08c`](#insn-00bcd08c) → [`00bcd090`](#insn-00bcd090)
- ブロック [`00bcd090`](#insn-00bcd090) 範囲 `[['00bcd090', '00bcd093']]`
  - `FALL_THROUGH` [`00bcd090`](#insn-00bcd090) → [`00bcd094`](#insn-00bcd094)
- ブロック [`00bcd094`](#insn-00bcd094) 範囲 `[['00bcd094', '00bcd0cf']]`
  - `CONDITIONAL_JUMP` [`00bcd0cc`](#insn-00bcd0cc) → [`00bcd050`](#insn-00bcd050)
  - `FALL_THROUGH` [`00bcd0cc`](#insn-00bcd0cc) → [`00bcd0d0`](#insn-00bcd0d0)
- ブロック [`00bcd0d0`](#insn-00bcd0d0) 範囲 `[['00bcd0d0', '00bcd0e7']]`
  - `UNCONDITIONAL_JUMP` [`00bcd0e4`](#insn-00bcd0e4) → [`00bcd050`](#insn-00bcd050)
- ブロック [`00bcd0e8`](#insn-00bcd0e8) 範囲 `[['00bcd0e8', '00bcd0fb']]`
  - `CONDITIONAL_JUMP` [`00bcd0f8`](#insn-00bcd0f8) → [`00bcd120`](#insn-00bcd120)
  - `FALL_THROUGH` [`00bcd0f8`](#insn-00bcd0f8) → [`00bcd0fc`](#insn-00bcd0fc)
- ブロック [`00bcd0fc`](#insn-00bcd0fc) 範囲 `[['00bcd0fc', '00bcd11b']]`
  - `CONDITIONAL_JUMP` [`00bcd118`](#insn-00bcd118) → [`00bcd164`](#insn-00bcd164)
  - `FALL_THROUGH` [`00bcd118`](#insn-00bcd118) → [`00bcd11c`](#insn-00bcd11c)
- ブロック [`00bcd11c`](#insn-00bcd11c) 範囲 `[['00bcd11c', '00bcd11f']]`
  - `FALL_THROUGH` [`00bcd11c`](#insn-00bcd11c) → [`00bcd120`](#insn-00bcd120)
- ブロック [`00bcd120`](#insn-00bcd120) 範囲 `[['00bcd120', '00bcd13b']]`
  - `FALL_THROUGH` [`00bcd138`](#insn-00bcd138) → [`00bcd13c`](#insn-00bcd13c)
- ブロック [`00bcd13c`](#insn-00bcd13c) 範囲 `[['00bcd13c', '00bcd13f']]`
  - `FALL_THROUGH` [`00bcd13c`](#insn-00bcd13c) → [`00bcd140`](#insn-00bcd140)
- ブロック [`00bcd140`](#insn-00bcd140) 範囲 `[['00bcd140', '00bcd15f']]`
- ブロック [`00bcd160`](#insn-00bcd160) 範囲 `[['00bcd160', '00bcd163']]`
- ブロック [`00bcd164`](#insn-00bcd164) 範囲 `[['00bcd164', '00bcd167']]`

## 命令位置別の参照

- [`00bccfc4`](#insn-00bccfc4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfc8`](#insn-00bccfc8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfcc`](#insn-00bccfcc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfd0`](#insn-00bccfd0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bccfd4`](#insn-00bccfd4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd014`](#insn-00bcd014) → [`00bcd02c`](#insn-00bcd02c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd034`](#insn-00bcd034) → [`00bcd0e8`](#insn-00bcd0e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd038`](#insn-00bcd038) → [`00bcd13c`](#insn-00bcd13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd040`](#insn-00bcd040) → [`00bcd140`](#insn-00bcd140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd04c`](#insn-00bcd04c) → [`00bcd05c`](#insn-00bcd05c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd058`](#insn-00bcd058) → [`00bcd140`](#insn-00bcd140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd06c`](#insn-00bcd06c) → [`00bcd094`](#insn-00bcd094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd084`](#insn-00bcd084) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcd08c`](#insn-00bcd08c) → [`00bcd160`](#insn-00bcd160) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd0cc`](#insn-00bcd0cc) → [`00bcd050`](#insn-00bcd050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd0e4`](#insn-00bcd0e4) → [`00bcd050`](#insn-00bcd050) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd0f8`](#insn-00bcd0f8) → [`00bcd120`](#insn-00bcd120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd110`](#insn-00bcd110) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcd118`](#insn-00bcd118) → [`00bcd164`](#insn-00bcd164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd144`](#insn-00bcd144) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd148`](#insn-00bcd148) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd14c`](#insn-00bcd14c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd150`](#insn-00bcd150) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd154`](#insn-00bcd154) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd160`](#insn-00bcd160) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bcd164`](#insn-00bcd164) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bccfc4`](#insn-00bccfc4)

~~~json
{
  "source": "00bccfc4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfc8`](#insn-00bccfc8)

~~~json
{
  "source": "00bccfc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfcc`](#insn-00bccfcc)

~~~json
{
  "source": "00bccfcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfd0`](#insn-00bccfd0)

~~~json
{
  "source": "00bccfd0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bccfd4`](#insn-00bccfd4)

~~~json
{
  "source": "00bccfd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd014`](#insn-00bcd014)

~~~json
{
  "source": "00bcd014",
  "target": "00bcd02c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd034`](#insn-00bcd034)

~~~json
{
  "source": "00bcd034",
  "target": "00bcd0e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd038`](#insn-00bcd038)

~~~json
{
  "source": "00bcd038",
  "target": "00bcd13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd040`](#insn-00bcd040)

~~~json
{
  "source": "00bcd040",
  "target": "00bcd140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd04c`](#insn-00bcd04c)

~~~json
{
  "source": "00bcd04c",
  "target": "00bcd05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd058`](#insn-00bcd058)

~~~json
{
  "source": "00bcd058",
  "target": "00bcd140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd06c`](#insn-00bcd06c)

~~~json
{
  "source": "00bcd06c",
  "target": "00bcd094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd084`](#insn-00bcd084)

~~~json
{
  "source": "00bcd084",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd08c`](#insn-00bcd08c)

~~~json
{
  "source": "00bcd08c",
  "target": "00bcd160",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd0cc`](#insn-00bcd0cc)

~~~json
{
  "source": "00bcd0cc",
  "target": "00bcd050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd0e4`](#insn-00bcd0e4)

~~~json
{
  "source": "00bcd0e4",
  "target": "00bcd050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd0f8`](#insn-00bcd0f8)

~~~json
{
  "source": "00bcd0f8",
  "target": "00bcd120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd110`](#insn-00bcd110)

~~~json
{
  "source": "00bcd110",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd118`](#insn-00bcd118)

~~~json
{
  "source": "00bcd118",
  "target": "00bcd164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd144`](#insn-00bcd144)

~~~json
{
  "source": "00bcd144",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd148`](#insn-00bcd148)

~~~json
{
  "source": "00bcd148",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd14c`](#insn-00bcd14c)

~~~json
{
  "source": "00bcd14c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd150`](#insn-00bcd150)

~~~json
{
  "source": "00bcd150",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd154`](#insn-00bcd154)

~~~json
{
  "source": "00bcd154",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd160`](#insn-00bcd160)

~~~json
{
  "source": "00bcd160",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd164`](#insn-00bcd164)

~~~json
{
  "source": "00bcd164",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
