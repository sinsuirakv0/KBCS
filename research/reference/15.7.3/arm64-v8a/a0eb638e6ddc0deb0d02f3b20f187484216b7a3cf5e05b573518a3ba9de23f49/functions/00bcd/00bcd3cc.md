# 00bcd3cc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bcd304`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bcd/00bcd304.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0007.md#compare-9d814f48a4c83374fd40e5614b78f65f)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bcd410`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bcd/00bcd410.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-23929170774dc34ffa16809d4568e17b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcd3cc",
  "name": "FUN_00bcd3cc",
  "size": 612,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "308d65aa80ccf1647ae6c76b167c944c97ee94578590ed51a39904aa9c9e0ace",
  "source_text_sha256": "308d65aa80ccf1647ae6c76b167c944c97ee94578590ed51a39904aa9c9e0ace",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcd3cc",
        "00bcd62f"
      ]
    ],
    "bytes_sha256": "4cdefe2edfea790e62415e3f5946093cdd25d570ab6f6c071232e8989df5d40f",
    "instruction_count": 153,
    "instruction_bytes": 612,
    "body_bytes": 612,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3691 bytes

~~~c

void FUN_00bcd3cc(long param_1,undefined8 *param_2)

{
  void *pvVar1;
  long lVar2;
  ulong uVar3;
  size_t sVar4;
  long *plVar5;
  
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar3 = lVar2 + 1;
  if ((ulong)param_2[2] < uVar3) {
    sVar4 = param_2[2] * 2;
    uVar3 = lVar2 + 0x3e1;
    if (sVar4 < uVar3 || sVar4 - uVar3 == 0) {
      sVar4 = uVar3;
    }
    param_2[2] = sVar4;
    pvVar1 = realloc(pvVar1,sVar4);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar3 = lVar2 + 1;
  }
  param_2[1] = uVar3;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x5b;
  plVar5 = *(long **)(param_1 + 0x10);
  (**(code **)(*plVar5 + 0x20))(plVar5,param_2);
  if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
  }
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar2 + 5U) {
    sVar4 = param_2[2] * 2;
    uVar3 = lVar2 + 0x3e5;
    if (sVar4 < uVar3 || sVar4 - uVar3 == 0) {
      sVar4 = uVar3;
    }
    param_2[2] = sVar4;
    pvVar1 = realloc(pvVar1,sVar4);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
  }
  *(undefined1 *)((undefined4 *)((long)pvVar1 + lVar2) + 1) = 0x20;
  *(undefined4 *)((long)pvVar1 + lVar2) = 0x2e2e2e20;
  plVar5 = *(long **)(param_1 + 0x18);
  lVar2 = *plVar5;
  param_2[1] = param_2[1] + 5;
  (**(code **)(lVar2 + 0x20))(plVar5,param_2);
  if ((*(ushort *)((long)plVar5 + 9) & 0xc0) != 0x40) {
    (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
  }
  lVar2 = param_2[1];
  pvVar1 = (void *)*param_2;
  uVar3 = lVar2 + 1;
  if ((ulong)param_2[2] < uVar3) {
    sVar4 = param_2[2] * 2;
    uVar3 = lVar2 + 0x3e1;
    if (sVar4 < uVar3 || sVar4 - uVar3 == 0) {
      sVar4 = uVar3;
    }
    param_2[2] = sVar4;
    pvVar1 = realloc(pvVar1,sVar4);
    *param_2 = pvVar1;
    if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar2 = param_2[1];
    uVar3 = lVar2 + 1;
  }
  param_2[1] = uVar3;
  *(undefined1 *)((long)pvVar1 + lVar2) = 0x5d;
  plVar5 = *(long **)(param_1 + 0x20);
  if (1 < *(byte *)(plVar5 + 1) - 0x51) {
    lVar2 = param_2[1];
    pvVar1 = (void *)*param_2;
    if ((ulong)param_2[2] < lVar2 + 3U) {
      sVar4 = param_2[2] * 2;
      uVar3 = lVar2 + 0x3e3;
      if (sVar4 < uVar3 || sVar4 - uVar3 == 0) {
        sVar4 = uVar3;
      }
      param_2[2] = sVar4;
      pvVar1 = realloc(pvVar1,sVar4);
      *param_2 = pvVar1;
      if (pvVar1 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
        abort();
      }
      lVar2 = param_2[1];
    }
    *(undefined1 *)((undefined2 *)((long)pvVar1 + lVar2) + 1) = 0x20;
    *(undefined2 *)((long)pvVar1 + lVar2) = 0x3d20;
                    /* try { // try from 00bcd5b8 to 00ccd69b has its CatchHandler @ 00bcd5b8
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcd5b8 with catch @ 00bcd5b8
                       catch(type#1 @ 00000000) { ... } // from try @ 00bcd72c with catch @ 00bcd5b8
                        */
    plVar5 = *(long **)(param_1 + 0x20);
    param_2[1] = param_2[1] + 3;
  }
  (**(code **)(*plVar5 + 0x20))(plVar5,param_2);
  if ((*(ushort *)((long)plVar5 + 9) & 0xc0) == 0x40) {
    return;
  }
                    /* WARNING: Could not recover jumptable at 0x00bcd61c. Too many branches */
                    /* WARNING: Treating indirect jump as call */
  (**(code **)(*plVar5 + 0x28))(plVar5,param_2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcd3cc"></a> `00bcd3cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcd3d0"></a> `00bcd3d0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcd3d4"></a> `00bcd3d4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd3d8"></a> `00bcd3d8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd3dc"></a> `00bcd3dc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcd3e0"></a> `00bcd3e0` | `29 ac 40 a9` | ldp x9,x11,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd3e4"></a> `00bcd3e4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcd3e8"></a> `00bcd3e8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcd3ec"></a> `00bcd3ec` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcd3f0"></a> `00bcd3f0` | `2a 05 00 91` | add x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd3f4"></a> `00bcd3f4` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bcd3f8"></a> `00bcd3f8` | `a9 01 00 54` | b.ls 0x00bcd42c | `CONDITIONAL_JUMP`
<a id="insn-00bcd3fc"></a> `00bcd3fc` | `6a f9 7f d3` | lsl x10,x11,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd400"></a> `00bcd400` | `29 85 0f 91` | add x9,x9,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcd404"></a> `00bcd404` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcd408"></a> `00bcd408` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcd40c"></a> `00bcd40c` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bcd410"></a> `00bcd410` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd414"></a> `00bcd414` | `7b 3f 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd418"></a> `00bcd418` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd41c"></a> `00bcd41c` | `20 10 00 b4` | cbz x0,0x00bcd620 | `CONDITIONAL_JUMP`
<a id="insn-00bcd420"></a> `00bcd420` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd424"></a> `00bcd424` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcd428"></a> `00bcd428` | `2a 05 00 91` | add x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd42c"></a> `00bcd42c` | `6a 06 00 f9` | str x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd430"></a> `00bcd430` | `6a 0b 80 52` | mov w10,#0x5b | `FALL_THROUGH`
<a id="insn-00bcd434"></a> `00bcd434` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcd438"></a> `00bcd438` | `0a 69 29 38` | strb w10,[x8, x9, LSL ] | `FALL_THROUGH`
<a id="insn-00bcd43c"></a> `00bcd43c` | `95 0a 40 f9` | ldr x21,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd440"></a> `00bcd440` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcd444"></a> `00bcd444` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd448"></a> `00bcd448` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd44c"></a> `00bcd44c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd450"></a> `00bcd450` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcd454"></a> `00bcd454` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcd458"></a> `00bcd458` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcd45c"></a> `00bcd45c` | `c0 00 00 54` | b.eq 0x00bcd474 | `CONDITIONAL_JUMP`
<a id="insn-00bcd460"></a> `00bcd460` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcd464"></a> `00bcd464` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd468"></a> `00bcd468` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcd46c"></a> `00bcd46c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcd470"></a> `00bcd470` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd474"></a> `00bcd474` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd478"></a> `00bcd478` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd47c"></a> `00bcd47c` | `0a 15 00 91` | add x10,x8,#0x5 | `FALL_THROUGH`
<a id="insn-00bcd480"></a> `00bcd480` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcd484"></a> `00bcd484` | `49 01 00 54` | b.ls 0x00bcd4ac | `CONDITIONAL_JUMP`
<a id="insn-00bcd488"></a> `00bcd488` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd48c"></a> `00bcd48c` | `08 95 0f 91` | add x8,x8,#0x3e5 | `FALL_THROUGH`
<a id="insn-00bcd490"></a> `00bcd490` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcd494"></a> `00bcd494` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcd498"></a> `00bcd498` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd49c"></a> `00bcd49c` | `59 3f 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd4a0"></a> `00bcd4a0` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd4a4"></a> `00bcd4a4` | `00 0c 00 b4` | cbz x0,0x00bcd624 | `CONDITIONAL_JUMP`
<a id="insn-00bcd4a8"></a> `00bcd4a8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd4ac"></a> `00bcd4ac` | `0a c4 85 52` | mov w10,#0x2e20 | `FALL_THROUGH`
<a id="insn-00bcd4b0"></a> `00bcd4b0` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcd4b4"></a> `00bcd4b4` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bcd4b8"></a> `00bcd4b8` | `ca c5 a5 72` | movk w10,#0x2e2e, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcd4bc"></a> `00bcd4bc` | `09 11 00 39` | strb w9,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bcd4c0"></a> `00bcd4c0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcd4c4"></a> `00bcd4c4` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcd4c8"></a> `00bcd4c8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd4cc"></a> `00bcd4cc` | `95 0e 40 f9` | ldr x21,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bcd4d0"></a> `00bcd4d0` | `08 15 00 91` | add x8,x8,#0x5 | `FALL_THROUGH`
<a id="insn-00bcd4d4"></a> `00bcd4d4` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00bcd4d8"></a> `00bcd4d8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd4dc"></a> `00bcd4dc` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd4e0"></a> `00bcd4e0` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd4e4"></a> `00bcd4e4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd4e8"></a> `00bcd4e8` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcd4ec"></a> `00bcd4ec` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcd4f0"></a> `00bcd4f0` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcd4f4"></a> `00bcd4f4` | `c0 00 00 54` | b.eq 0x00bcd50c | `CONDITIONAL_JUMP`
<a id="insn-00bcd4f8"></a> `00bcd4f8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcd4fc"></a> `00bcd4fc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd500"></a> `00bcd500` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcd504"></a> `00bcd504` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcd508"></a> `00bcd508` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd50c"></a> `00bcd50c` | `68 aa 40 a9` | ldp x8,x10,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd510"></a> `00bcd510` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd514"></a> `00bcd514` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd518"></a> `00bcd518` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcd51c"></a> `00bcd51c` | `69 01 00 54` | b.ls 0x00bcd548 | `CONDITIONAL_JUMP`
<a id="insn-00bcd520"></a> `00bcd520` | `49 f9 7f d3` | lsl x9,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd524"></a> `00bcd524` | `08 85 0f 91` | add x8,x8,#0x3e1 | `FALL_THROUGH`
<a id="insn-00bcd528"></a> `00bcd528` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcd52c"></a> `00bcd52c` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcd530"></a> `00bcd530` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd534"></a> `00bcd534` | `33 3f 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd538"></a> `00bcd538` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd53c"></a> `00bcd53c` | `60 07 00 b4` | cbz x0,0x00bcd628 | `CONDITIONAL_JUMP`
<a id="insn-00bcd540"></a> `00bcd540` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd544"></a> `00bcd544` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd548"></a> `00bcd548` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd54c"></a> `00bcd54c` | `a9 0b 80 52` | mov w9,#0x5d | `FALL_THROUGH`
<a id="insn-00bcd550"></a> `00bcd550` | `09 68 28 38` | strb w9,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bcd554"></a> `00bcd554` | `95 12 40 f9` | ldr x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd558"></a> `00bcd558` | `a8 22 40 39` | ldrb w8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd55c"></a> `00bcd55c` | `08 45 01 51` | sub w8,w8,#0x51 | `FALL_THROUGH`
<a id="insn-00bcd560"></a> `00bcd560` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bcd564"></a> `00bcd564` | `03 03 00 54` | b.cc 0x00bcd5c4 | `CONDITIONAL_JUMP`
<a id="insn-00bcd568"></a> `00bcd568` | `68 a6 40 a9` | ldp x8,x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd56c"></a> `00bcd56c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd570"></a> `00bcd570` | `0a 0d 00 91` | add x10,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bcd574"></a> `00bcd574` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcd578"></a> `00bcd578` | `49 01 00 54` | b.ls 0x00bcd5a0 | `CONDITIONAL_JUMP`
<a id="insn-00bcd57c"></a> `00bcd57c` | `29 f9 7f d3` | lsl x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcd580"></a> `00bcd580` | `08 8d 0f 91` | add x8,x8,#0x3e3 | `FALL_THROUGH`
<a id="insn-00bcd584"></a> `00bcd584` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bcd588"></a> `00bcd588` | `21 81 88 9a` | csel x1,x9,x8,hi | `FALL_THROUGH`
<a id="insn-00bcd58c"></a> `00bcd58c` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd590"></a> `00bcd590` | `1c 3f 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bcd594"></a> `00bcd594` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcd598"></a> `00bcd598` | `a0 04 00 b4` | cbz x0,0x00bcd62c | `CONDITIONAL_JUMP`
<a id="insn-00bcd59c"></a> `00bcd59c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd5a0"></a> `00bcd5a0` | `08 00 08 8b` | add x8,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcd5a4"></a> `00bcd5a4` | `09 04 80 52` | mov w9,#0x20 | `FALL_THROUGH`
<a id="insn-00bcd5a8"></a> `00bcd5a8` | `0a a4 87 52` | mov w10,#0x3d20 | `FALL_THROUGH`
<a id="insn-00bcd5ac"></a> `00bcd5ac` | `09 09 00 39` | strb w9,[x8, #0x2] | `FALL_THROUGH`
<a id="insn-00bcd5b0"></a> `00bcd5b0` | `0a 01 00 79` | strh w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcd5b4"></a> `00bcd5b4` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd5b8"></a> `00bcd5b8` | `95 12 40 f9` | ldr x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd5bc"></a> `00bcd5bc` | `08 0d 00 91` | add x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bcd5c0"></a> `00bcd5c0` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcd5c4"></a> `00bcd5c4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcd5c8"></a> `00bcd5c8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd5cc"></a> `00bcd5cc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcd5d0"></a> `00bcd5d0` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd5d4"></a> `00bcd5d4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcd5d8"></a> `00bcd5d8` | `a8 92 40 78` | ldurh w8,[x21, #0x9] | `FALL_THROUGH`
<a id="insn-00bcd5dc"></a> `00bcd5dc` | `08 05 1a 12` | and w8,w8,#0xc0 | `FALL_THROUGH`
<a id="insn-00bcd5e0"></a> `00bcd5e0` | `1f 01 01 71` | cmp w8,#0x40 | `FALL_THROUGH`
<a id="insn-00bcd5e4"></a> `00bcd5e4` | `c1 00 00 54` | b.ne 0x00bcd5fc | `CONDITIONAL_JUMP`
<a id="insn-00bcd5e8"></a> `00bcd5e8` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd5ec"></a> `00bcd5ec` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd5f0"></a> `00bcd5f0` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcd5f4"></a> `00bcd5f4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcd5f8"></a> `00bcd5f8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcd5fc"></a> `00bcd5fc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcd600"></a> `00bcd600` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcd604"></a> `00bcd604` | `10 15 40 f9` | ldr x16,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bcd608"></a> `00bcd608` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bcd60c"></a> `00bcd60c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcd610"></a> `00bcd610` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcd614"></a> `00bcd614` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcd618"></a> `00bcd618` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcd61c"></a> `00bcd61c` | `00 02 1f d6` | br x16 | `COMPUTED_JUMP`
<a id="insn-00bcd620"></a> `00bcd620` | `14 43 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bcd624"></a> `00bcd624` | `13 43 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bcd628"></a> `00bcd628` | `12 43 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bcd62c"></a> `00bcd62c` | `11 43 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcd3cc`](#insn-00bcd3cc) 範囲 `[['00bcd3cc', '00bcd3fb']]`
  - `CONDITIONAL_JUMP` [`00bcd3f8`](#insn-00bcd3f8) → [`00bcd42c`](#insn-00bcd42c)
  - `FALL_THROUGH` [`00bcd3f8`](#insn-00bcd3f8) → [`00bcd3fc`](#insn-00bcd3fc)
- ブロック [`00bcd3fc`](#insn-00bcd3fc) 範囲 `[['00bcd3fc', '00bcd41f']]`
  - `CONDITIONAL_JUMP` [`00bcd41c`](#insn-00bcd41c) → [`00bcd620`](#insn-00bcd620)
  - `FALL_THROUGH` [`00bcd41c`](#insn-00bcd41c) → [`00bcd420`](#insn-00bcd420)
- ブロック [`00bcd420`](#insn-00bcd420) 範囲 `[['00bcd420', '00bcd42b']]`
  - `FALL_THROUGH` [`00bcd428`](#insn-00bcd428) → [`00bcd42c`](#insn-00bcd42c)
- ブロック [`00bcd42c`](#insn-00bcd42c) 範囲 `[['00bcd42c', '00bcd45f']]`
  - `CONDITIONAL_JUMP` [`00bcd45c`](#insn-00bcd45c) → [`00bcd474`](#insn-00bcd474)
  - `FALL_THROUGH` [`00bcd45c`](#insn-00bcd45c) → [`00bcd460`](#insn-00bcd460)
- ブロック [`00bcd460`](#insn-00bcd460) 範囲 `[['00bcd460', '00bcd473']]`
  - `FALL_THROUGH` [`00bcd470`](#insn-00bcd470) → [`00bcd474`](#insn-00bcd474)
- ブロック [`00bcd474`](#insn-00bcd474) 範囲 `[['00bcd474', '00bcd487']]`
  - `CONDITIONAL_JUMP` [`00bcd484`](#insn-00bcd484) → [`00bcd4ac`](#insn-00bcd4ac)
  - `FALL_THROUGH` [`00bcd484`](#insn-00bcd484) → [`00bcd488`](#insn-00bcd488)
- ブロック [`00bcd488`](#insn-00bcd488) 範囲 `[['00bcd488', '00bcd4a7']]`
  - `CONDITIONAL_JUMP` [`00bcd4a4`](#insn-00bcd4a4) → [`00bcd624`](#insn-00bcd624)
  - `FALL_THROUGH` [`00bcd4a4`](#insn-00bcd4a4) → [`00bcd4a8`](#insn-00bcd4a8)
- ブロック [`00bcd4a8`](#insn-00bcd4a8) 範囲 `[['00bcd4a8', '00bcd4ab']]`
  - `FALL_THROUGH` [`00bcd4a8`](#insn-00bcd4a8) → [`00bcd4ac`](#insn-00bcd4ac)
- ブロック [`00bcd4ac`](#insn-00bcd4ac) 範囲 `[['00bcd4ac', '00bcd4f7']]`
  - `CONDITIONAL_JUMP` [`00bcd4f4`](#insn-00bcd4f4) → [`00bcd50c`](#insn-00bcd50c)
  - `FALL_THROUGH` [`00bcd4f4`](#insn-00bcd4f4) → [`00bcd4f8`](#insn-00bcd4f8)
- ブロック [`00bcd4f8`](#insn-00bcd4f8) 範囲 `[['00bcd4f8', '00bcd50b']]`
  - `FALL_THROUGH` [`00bcd508`](#insn-00bcd508) → [`00bcd50c`](#insn-00bcd50c)
- ブロック [`00bcd50c`](#insn-00bcd50c) 範囲 `[['00bcd50c', '00bcd51f']]`
  - `CONDITIONAL_JUMP` [`00bcd51c`](#insn-00bcd51c) → [`00bcd548`](#insn-00bcd548)
  - `FALL_THROUGH` [`00bcd51c`](#insn-00bcd51c) → [`00bcd520`](#insn-00bcd520)
- ブロック [`00bcd520`](#insn-00bcd520) 範囲 `[['00bcd520', '00bcd53f']]`
  - `CONDITIONAL_JUMP` [`00bcd53c`](#insn-00bcd53c) → [`00bcd628`](#insn-00bcd628)
  - `FALL_THROUGH` [`00bcd53c`](#insn-00bcd53c) → [`00bcd540`](#insn-00bcd540)
- ブロック [`00bcd540`](#insn-00bcd540) 範囲 `[['00bcd540', '00bcd547']]`
  - `FALL_THROUGH` [`00bcd544`](#insn-00bcd544) → [`00bcd548`](#insn-00bcd548)
- ブロック [`00bcd548`](#insn-00bcd548) 範囲 `[['00bcd548', '00bcd567']]`
  - `CONDITIONAL_JUMP` [`00bcd564`](#insn-00bcd564) → [`00bcd5c4`](#insn-00bcd5c4)
  - `FALL_THROUGH` [`00bcd564`](#insn-00bcd564) → [`00bcd568`](#insn-00bcd568)
- ブロック [`00bcd568`](#insn-00bcd568) 範囲 `[['00bcd568', '00bcd57b']]`
  - `CONDITIONAL_JUMP` [`00bcd578`](#insn-00bcd578) → [`00bcd5a0`](#insn-00bcd5a0)
  - `FALL_THROUGH` [`00bcd578`](#insn-00bcd578) → [`00bcd57c`](#insn-00bcd57c)
- ブロック [`00bcd57c`](#insn-00bcd57c) 範囲 `[['00bcd57c', '00bcd59b']]`
  - `CONDITIONAL_JUMP` [`00bcd598`](#insn-00bcd598) → [`00bcd62c`](#insn-00bcd62c)
  - `FALL_THROUGH` [`00bcd598`](#insn-00bcd598) → [`00bcd59c`](#insn-00bcd59c)
- ブロック [`00bcd59c`](#insn-00bcd59c) 範囲 `[['00bcd59c', '00bcd59f']]`
  - `FALL_THROUGH` [`00bcd59c`](#insn-00bcd59c) → [`00bcd5a0`](#insn-00bcd5a0)
- ブロック [`00bcd5a0`](#insn-00bcd5a0) 範囲 `[['00bcd5a0', '00bcd5b7']]`
  - `FALL_THROUGH` [`00bcd5b4`](#insn-00bcd5b4) → [`00bcd5b8`](#insn-00bcd5b8)
- ブロック [`00bcd5b8`](#insn-00bcd5b8) 範囲 `[['00bcd5b8', '00bcd5c3']]`
  - `FALL_THROUGH` [`00bcd5c0`](#insn-00bcd5c0) → [`00bcd5c4`](#insn-00bcd5c4)
- ブロック [`00bcd5c4`](#insn-00bcd5c4) 範囲 `[['00bcd5c4', '00bcd5e7']]`
  - `CONDITIONAL_JUMP` [`00bcd5e4`](#insn-00bcd5e4) → [`00bcd5fc`](#insn-00bcd5fc)
  - `FALL_THROUGH` [`00bcd5e4`](#insn-00bcd5e4) → [`00bcd5e8`](#insn-00bcd5e8)
- ブロック [`00bcd5e8`](#insn-00bcd5e8) 範囲 `[['00bcd5e8', '00bcd5fb']]`
- ブロック [`00bcd5fc`](#insn-00bcd5fc) 範囲 `[['00bcd5fc', '00bcd61f']]`
- ブロック [`00bcd620`](#insn-00bcd620) 範囲 `[['00bcd620', '00bcd623']]`
- ブロック [`00bcd624`](#insn-00bcd624) 範囲 `[['00bcd624', '00bcd627']]`
- ブロック [`00bcd628`](#insn-00bcd628) 範囲 `[['00bcd628', '00bcd62b']]`
- ブロック [`00bcd62c`](#insn-00bcd62c) 範囲 `[['00bcd62c', '00bcd62f']]`

## 命令位置別の参照

- [`00bcd3d0`](#insn-00bcd3d0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd3d4`](#insn-00bcd3d4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd3d8`](#insn-00bcd3d8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd3f8`](#insn-00bcd3f8) → [`00bcd42c`](#insn-00bcd42c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd414`](#insn-00bcd414) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcd41c`](#insn-00bcd41c) → [`00bcd620`](#insn-00bcd620) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd45c`](#insn-00bcd45c) → [`00bcd474`](#insn-00bcd474) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd484`](#insn-00bcd484) → [`00bcd4ac`](#insn-00bcd4ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd49c`](#insn-00bcd49c) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcd4a4`](#insn-00bcd4a4) → [`00bcd624`](#insn-00bcd624) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd4f4`](#insn-00bcd4f4) → [`00bcd50c`](#insn-00bcd50c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd51c`](#insn-00bcd51c) → [`00bcd548`](#insn-00bcd548) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd534`](#insn-00bcd534) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcd53c`](#insn-00bcd53c) → [`00bcd628`](#insn-00bcd628) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd564`](#insn-00bcd564) → [`00bcd5c4`](#insn-00bcd5c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd578`](#insn-00bcd578) → [`00bcd5a0`](#insn-00bcd5a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd590`](#insn-00bcd590) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bcd598`](#insn-00bcd598) → [`00bcd62c`](#insn-00bcd62c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd5e4`](#insn-00bcd5e4) → [`00bcd5fc`](#insn-00bcd5fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd5e8`](#insn-00bcd5e8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd5ec`](#insn-00bcd5ec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd5f0`](#insn-00bcd5f0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd60c`](#insn-00bcd60c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd610`](#insn-00bcd610) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd614`](#insn-00bcd614) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcd620`](#insn-00bcd620) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bcd624`](#insn-00bcd624) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bcd628`](#insn-00bcd628) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bcd62c`](#insn-00bcd62c) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcd3d0`](#insn-00bcd3d0)

~~~json
{
  "source": "00bcd3d0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd3d4`](#insn-00bcd3d4)

~~~json
{
  "source": "00bcd3d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd3d8`](#insn-00bcd3d8)

~~~json
{
  "source": "00bcd3d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd3f8`](#insn-00bcd3f8)

~~~json
{
  "source": "00bcd3f8",
  "target": "00bcd42c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd414`](#insn-00bcd414)

~~~json
{
  "source": "00bcd414",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd41c`](#insn-00bcd41c)

~~~json
{
  "source": "00bcd41c",
  "target": "00bcd620",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd45c`](#insn-00bcd45c)

~~~json
{
  "source": "00bcd45c",
  "target": "00bcd474",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd484`](#insn-00bcd484)

~~~json
{
  "source": "00bcd484",
  "target": "00bcd4ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd49c`](#insn-00bcd49c)

~~~json
{
  "source": "00bcd49c",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd4a4`](#insn-00bcd4a4)

~~~json
{
  "source": "00bcd4a4",
  "target": "00bcd624",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd4f4`](#insn-00bcd4f4)

~~~json
{
  "source": "00bcd4f4",
  "target": "00bcd50c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd51c`](#insn-00bcd51c)

~~~json
{
  "source": "00bcd51c",
  "target": "00bcd548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd534`](#insn-00bcd534)

~~~json
{
  "source": "00bcd534",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd53c`](#insn-00bcd53c)

~~~json
{
  "source": "00bcd53c",
  "target": "00bcd628",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd564`](#insn-00bcd564)

~~~json
{
  "source": "00bcd564",
  "target": "00bcd5c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd578`](#insn-00bcd578)

~~~json
{
  "source": "00bcd578",
  "target": "00bcd5a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd590`](#insn-00bcd590)

~~~json
{
  "source": "00bcd590",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd598`](#insn-00bcd598)

~~~json
{
  "source": "00bcd598",
  "target": "00bcd62c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd5e4`](#insn-00bcd5e4)

~~~json
{
  "source": "00bcd5e4",
  "target": "00bcd5fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd5e8`](#insn-00bcd5e8)

~~~json
{
  "source": "00bcd5e8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd5ec`](#insn-00bcd5ec)

~~~json
{
  "source": "00bcd5ec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd5f0`](#insn-00bcd5f0)

~~~json
{
  "source": "00bcd5f0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd60c`](#insn-00bcd60c)

~~~json
{
  "source": "00bcd60c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd610`](#insn-00bcd610)

~~~json
{
  "source": "00bcd610",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd614`](#insn-00bcd614)

~~~json
{
  "source": "00bcd614",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcd620`](#insn-00bcd620)

~~~json
{
  "source": "00bcd620",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd624`](#insn-00bcd624)

~~~json
{
  "source": "00bcd624",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd628`](#insn-00bcd628)

~~~json
{
  "source": "00bcd628",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcd62c`](#insn-00bcd62c)

~~~json
{
  "source": "00bcd62c",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
