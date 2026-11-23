# 00bcf3bc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bcf484`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bcf/00bcf484.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-73d03f3f143e462d561a5c561bcc206a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcf3bc",
  "name": "FUN_00bcf3bc",
  "size": 440,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "95ab01379ade3343dabbd9c9d896475439b6002fa6aae7d564d915b287b02bbf",
  "source_text_sha256": "95ab01379ade3343dabbd9c9d896475439b6002fa6aae7d564d915b287b02bbf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcf3bc",
        "00bcf573"
      ]
    ],
    "bytes_sha256": "a620c8f4b05459dd03268ef217b18ac3f10b310279cb27b4c51306a6f6540b03",
    "instruction_count": 110,
    "instruction_bytes": 440,
    "body_bytes": 440,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00bbb090](../00bbb/00bbb090.md)
- [00bdb0b0](../00bdb/00bdb0b0.md)
- [00bdd150](../00bdd/00bdd150.md)
- [00bde1c0](../00bde/00bde1c0.md)

## 関連文字列（未確認候補）

~~~text
"%s:%d: %s"
"basic_iostream"
"basic_istream"
"basic_ostream"
"basic_string"
"out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2355 bytes

~~~c

void FUN_00bcf3bc(long param_1,undefined8 *param_2)

{
  ulong uVar1;
  int iVar2;
  void *pvVar3;
  size_t __size;
  long lVar4;
  size_t sVar5;
  char *pcVar6;
  
                    /* catch() { ... } // from try @ 00bcf5a8 with catch @ 00bcf3cc */
  lVar4 = param_2[1];
  pvVar3 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar4 + 5U) {
    sVar5 = param_2[2] * 2;
    uVar1 = lVar4 + 0x3e5;
    if (sVar5 < uVar1 || sVar5 - uVar1 == 0) {
      sVar5 = uVar1;
    }
    param_2[2] = sVar5;
    pvVar3 = realloc(pvVar3,sVar5);
    *param_2 = pvVar3;
    if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar4 = param_2[1];
  }
  *(undefined1 *)((undefined4 *)((long)pvVar3 + lVar4) + 1) = 0x3a;
  *(undefined4 *)((long)pvVar3 + lVar4) = 0x3a647473;
  iVar2 = *(int *)(param_1 + 0xc);
  lVar4 = param_2[1] + 5;
  param_2[1] = lVar4;
  if (iVar2 < 3) {
    if (iVar2 == 0) {
      pcVar6 = "allocator";
      sVar5 = 9;
      goto LAB_00bcf4e4;
    }
    if (iVar2 == 1) {
      pcVar6 = "basic_string";
      sVar5 = 0xc;
      goto LAB_00bcf4e4;
    }
    pcVar6 = "basic_string";
    sVar5 = 6;
  }
  else if (iVar2 == 3) {
    pcVar6 = "basic_istream";
    sVar5 = 7;
  }
  else if (iVar2 == 4) {
    pcVar6 = "basic_ostream";
    sVar5 = 7;
  }
  else {
    pcVar6 = "basic_iostream";
    sVar5 = 8;
  }
  if (*(int *)pcVar6 != 0x69736162 || (short)*(int *)((long)pcVar6 + 4) != 0x5f63) {
                    /* WARNING: Subroutine does not return */
    FUN_00bbb090("%s:%d: %s","out/llvm-project/libcxxabi/src/demangle/ItaniumDemangle.h",0x6a9,
                 &DAT_002967d9);
  }
  pcVar6 = (char *)((long)pcVar6 + 6);
LAB_00bcf4e4:
  pvVar3 = (void *)*param_2;
  if ((ulong)param_2[2] < lVar4 + sVar5) {
    __size = param_2[2] * 2;
    uVar1 = lVar4 + sVar5 + 0x3e0;
    if (__size < uVar1 || __size - uVar1 == 0) {
      __size = uVar1;
    }
    param_2[2] = __size;
    pvVar3 = realloc(pvVar3,__size);
    *param_2 = pvVar3;
    if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
      abort();
    }
    lVar4 = param_2[1];
  }
                    /* try { // try from 00bcf520 to 00ccf5a7 has its CatchHandler @ 00bcf68c */
  memcpy((void *)((long)pvVar3 + lVar4),pcVar6,sVar5);
  param_2[1] = param_2[1] + sVar5;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcf3bc"></a> `00bcf3bc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bcf3c0"></a> `00bcf3c0` | `fd 7b bd a9` | stp x29,x30,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bcf3c4"></a> `00bcf3c4` | `f5 0b 00 f9` | str x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf3c8"></a> `00bcf3c8` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf3cc"></a> `00bcf3cc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bcf3d0"></a> `00bcf3d0` | `29 a8 40 a9` | ldp x9,x10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf3d4"></a> `00bcf3d4` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcf3d8"></a> `00bcf3d8` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-00bcf3dc"></a> `00bcf3dc` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bcf3e0"></a> `00bcf3e0` | `2b 15 00 91` | add x11,x9,#0x5 | `FALL_THROUGH`
<a id="insn-00bcf3e4"></a> `00bcf3e4` | `7f 01 0a eb` | cmp x11,x10 | `FALL_THROUGH`
<a id="insn-00bcf3e8"></a> `00bcf3e8` | `89 01 00 54` | b.ls 0x00bcf418 | `CONDITIONAL_JUMP`
<a id="insn-00bcf3ec"></a> `00bcf3ec` | `4a f9 7f d3` | lsl x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcf3f0"></a> `00bcf3f0` | `29 95 0f 91` | add x9,x9,#0x3e5 | `FALL_THROUGH`
<a id="insn-00bcf3f4"></a> `00bcf3f4` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bcf3f8"></a> `00bcf3f8` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bcf3fc"></a> `00bcf3fc` | `41 81 89 9a` | csel x1,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00bcf400"></a> `00bcf400` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf404"></a> `00bcf404` | `53 37 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf408"></a> `00bcf408` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcf40c"></a> `00bcf40c` | `00 0b 00 b4` | cbz x0,0x00bcf56c | `CONDITIONAL_JUMP`
<a id="insn-00bcf410"></a> `00bcf410` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf414"></a> `00bcf414` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bcf418"></a> `00bcf418` | `6a 8e 8e 52` | mov w10,#0x7473 | `FALL_THROUGH`
<a id="insn-00bcf41c"></a> `00bcf41c` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00bcf420"></a> `00bcf420` | `49 07 80 52` | mov w9,#0x3a | `FALL_THROUGH`
<a id="insn-00bcf424"></a> `00bcf424` | `8a 4c a7 72` | movk w10,#0x3a64, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcf428"></a> `00bcf428` | `09 11 00 39` | strb w9,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bcf42c"></a> `00bcf42c` | `0a 01 00 b9` | str w10,[x8] | `FALL_THROUGH`
<a id="insn-00bcf430"></a> `00bcf430` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf434"></a> `00bcf434` | `89 0e 40 b9` | ldr w9,[x20, #0xc] | `FALL_THROUGH`
<a id="insn-00bcf438"></a> `00bcf438` | `08 15 00 91` | add x8,x8,#0x5 | `FALL_THROUGH`
<a id="insn-00bcf43c"></a> `00bcf43c` | `3f 09 00 71` | cmp w9,#0x2 | `FALL_THROUGH`
<a id="insn-00bcf440"></a> `00bcf440` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf444"></a> `00bcf444` | `0c 01 00 54` | b.gt 0x00bcf464 | `CONDITIONAL_JUMP`
<a id="insn-00bcf448"></a> `00bcf448` | `e9 01 00 34` | cbz w9,0x00bcf484 | `CONDITIONAL_JUMP`
<a id="insn-00bcf44c"></a> `00bcf44c` | `3f 05 00 71` | cmp w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bcf450"></a> `00bcf450` | `a1 02 00 54` | b.ne 0x00bcf4a4 | `CONDITIONAL_JUMP`
<a id="insn-00bcf454"></a> `00bcf454` | `d5 b6 ff d0` | adrp x21,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bcf458"></a> `00bcf458` | `b5 1a 09 91` | add x21,x21,#0x246 | `FALL_THROUGH`
<a id="insn-00bcf45c"></a> `00bcf45c` | `94 01 80 52` | mov w20,#0xc | `FALL_THROUGH`
<a id="insn-00bcf460"></a> `00bcf460` | `21 00 00 14` | b 0x00bcf4e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf464"></a> `00bcf464` | `3f 0d 00 71` | cmp w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bcf468"></a> `00bcf468` | `60 01 00 54` | b.eq 0x00bcf494 | `CONDITIONAL_JUMP`
<a id="insn-00bcf46c"></a> `00bcf46c` | `3f 11 00 71` | cmp w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bcf470"></a> `00bcf470` | `21 02 00 54` | b.ne 0x00bcf4b4 | `CONDITIONAL_JUMP`
<a id="insn-00bcf474"></a> `00bcf474` | `e9 b6 ff b0` | adrp x9,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bcf478"></a> `00bcf478` | `29 c1 17 91` | add x9,x9,#0x5f0 | `FALL_THROUGH`
<a id="insn-00bcf47c"></a> `00bcf47c` | `f4 00 80 52` | mov w20,#0x7 | `FALL_THROUGH`
<a id="insn-00bcf480"></a> `00bcf480` | `10 00 00 14` | b 0x00bcf4c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf484"></a> `00bcf484` | `d5 b6 ff 90` | adrp x21,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bcf488"></a> `00bcf488` | `b5 ba 09 91` | add x21,x21,#0x26e | `FALL_THROUGH`
<a id="insn-00bcf48c"></a> `00bcf48c` | `34 01 80 52` | mov w20,#0x9 | `FALL_THROUGH`
<a id="insn-00bcf490"></a> `00bcf490` | `15 00 00 14` | b 0x00bcf4e4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf494"></a> `00bcf494` | `e9 b6 ff f0` | adrp x9,0x2ae000 | `FALL_THROUGH`
<a id="insn-00bcf498"></a> `00bcf498` | `29 29 1b 91` | add x9,x9,#0x6ca | `FALL_THROUGH`
<a id="insn-00bcf49c"></a> `00bcf49c` | `f4 00 80 52` | mov w20,#0x7 | `FALL_THROUGH`
<a id="insn-00bcf4a0"></a> `00bcf4a0` | `08 00 00 14` | b 0x00bcf4c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf4a4"></a> `00bcf4a4` | `c9 b6 ff d0` | adrp x9,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bcf4a8"></a> `00bcf4a8` | `29 19 09 91` | add x9,x9,#0x246 | `FALL_THROUGH`
<a id="insn-00bcf4ac"></a> `00bcf4ac` | `d4 00 80 52` | mov w20,#0x6 | `FALL_THROUGH`
<a id="insn-00bcf4b0"></a> `00bcf4b0` | `04 00 00 14` | b 0x00bcf4c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcf4b4"></a> `00bcf4b4` | `c9 b6 ff b0` | adrp x9,0x2a8000 | `FALL_THROUGH`
<a id="insn-00bcf4b8"></a> `00bcf4b8` | `29 c1 02 91` | add x9,x9,#0xb0 | `FALL_THROUGH`
<a id="insn-00bcf4bc"></a> `00bcf4bc` | `14 01 80 52` | mov w20,#0x8 | `FALL_THROUGH`
<a id="insn-00bcf4c0"></a> `00bcf4c0` | `2a 01 40 b9` | ldr w10,[x9] | `FALL_THROUGH`
<a id="insn-00bcf4c4"></a> `00bcf4c4` | `4c 2c 8c 52` | mov w12,#0x6162 | `FALL_THROUGH`
<a id="insn-00bcf4c8"></a> `00bcf4c8` | `2b 09 40 79` | ldrh w11,[x9, #0x4] | `FALL_THROUGH`
<a id="insn-00bcf4cc"></a> `00bcf4cc` | `6c 2e ad 72` | movk w12,#0x6973, LSL #16 | `FALL_THROUGH`
<a id="insn-00bcf4d0"></a> `00bcf4d0` | `5f 01 0c 6b` | cmp w10,w12 | `FALL_THROUGH`
<a id="insn-00bcf4d4"></a> `00bcf4d4` | `6a ec 8b 52` | mov w10,#0x5f63 | `FALL_THROUGH`
<a id="insn-00bcf4d8"></a> `00bcf4d8` | `60 01 4a 7a` | ccmp w11,w10,#0x0,eq | `FALL_THROUGH`
<a id="insn-00bcf4dc"></a> `00bcf4dc` | `81 03 00 54` | b.ne 0x00bcf54c | `CONDITIONAL_JUMP`
<a id="insn-00bcf4e0"></a> `00bcf4e0` | `35 19 00 91` | add x21,x9,#0x6 | `FALL_THROUGH`
<a id="insn-00bcf4e4"></a> `00bcf4e4` | `6a 0a 40 f9` | ldr x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf4e8"></a> `00bcf4e8` | `09 01 14 8b` | add x9,x8,x20 | `FALL_THROUGH`
<a id="insn-00bcf4ec"></a> `00bcf4ec` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcf4f0"></a> `00bcf4f0` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bcf4f4"></a> `00bcf4f4` | `49 01 00 54` | b.ls 0x00bcf51c | `CONDITIONAL_JUMP`
<a id="insn-00bcf4f8"></a> `00bcf4f8` | `48 f9 7f d3` | lsl x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcf4fc"></a> `00bcf4fc` | `29 81 0f 91` | add x9,x9,#0x3e0 | `FALL_THROUGH`
<a id="insn-00bcf500"></a> `00bcf500` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcf504"></a> `00bcf504` | `01 81 89 9a` | csel x1,x8,x9,hi | `FALL_THROUGH`
<a id="insn-00bcf508"></a> `00bcf508` | `61 0a 00 f9` | str x1,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf50c"></a> `00bcf50c` | `11 37 00 94` | bl 0x00bdd150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf510"></a> `00bcf510` | `60 02 00 f9` | str x0,[x19] | `FALL_THROUGH`
<a id="insn-00bcf514"></a> `00bcf514` | `e0 02 00 b4` | cbz x0,0x00bcf570 | `CONDITIONAL_JUMP`
<a id="insn-00bcf518"></a> `00bcf518` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf51c"></a> `00bcf51c` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00bcf520"></a> `00bcf520` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcf524"></a> `00bcf524` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bcf528"></a> `00bcf528` | `e2 2e 00 94` | bl 0x00bdb0b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcf52c"></a> `00bcf52c` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf530"></a> `00bcf530` | `08 01 14 8b` | add x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00bcf534"></a> `00bcf534` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bcf538"></a> `00bcf538` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcf53c"></a> `00bcf53c` | `f5 0b 40 f9` | ldr x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcf540"></a> `00bcf540` | `fd 7b c3 a8` | ldp x29,x30,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bcf544"></a> `00bcf544` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bcf548"></a> `00bcf548` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcf54c"></a> `00bcf54c` | `00 b6 ff d0` | adrp x0,0x291000 | `FALL_THROUGH`
<a id="insn-00bcf550"></a> `00bcf550` | `00 f0 1f 91` | add x0,x0,#0x7fc | `FALL_THROUGH`
<a id="insn-00bcf554"></a> `00bcf554` | `81 b6 ff f0` | adrp x1,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bcf558"></a> `00bcf558` | `21 f4 01 91` | add x1,x1,#0x7d | `FALL_THROUGH`
<a id="insn-00bcf55c"></a> `00bcf55c` | `23 b6 ff f0` | adrp x3,0x296000 | `FALL_THROUGH`
<a id="insn-00bcf560"></a> `00bcf560` | `63 64 1f 91` | add x3,x3,#0x7d9 | `FALL_THROUGH`
<a id="insn-00bcf564"></a> `00bcf564` | `22 d5 80 52` | mov w2,#0x6a9 | `FALL_THROUGH`
<a id="insn-00bcf568"></a> `00bcf568` | `ca ae ff 97` | bl 0x00bbb090 | `CALL_TERMINATOR`
<a id="insn-00bcf56c"></a> `00bcf56c` | `15 3b 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`
<a id="insn-00bcf570"></a> `00bcf570` | `14 3b 00 94` | bl 0x00bde1c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcf3bc`](#insn-00bcf3bc) 範囲 `[['00bcf3bc', '00bcf3cb']]`
  - `FALL_THROUGH` [`00bcf3c8`](#insn-00bcf3c8) → [`00bcf3cc`](#insn-00bcf3cc)
- ブロック [`00bcf3cc`](#insn-00bcf3cc) 範囲 `[['00bcf3cc', '00bcf3eb']]`
  - `CONDITIONAL_JUMP` [`00bcf3e8`](#insn-00bcf3e8) → [`00bcf418`](#insn-00bcf418)
  - `FALL_THROUGH` [`00bcf3e8`](#insn-00bcf3e8) → [`00bcf3ec`](#insn-00bcf3ec)
- ブロック [`00bcf3ec`](#insn-00bcf3ec) 範囲 `[['00bcf3ec', '00bcf40f']]`
  - `CONDITIONAL_JUMP` [`00bcf40c`](#insn-00bcf40c) → [`00bcf56c`](#insn-00bcf56c)
  - `FALL_THROUGH` [`00bcf40c`](#insn-00bcf40c) → [`00bcf410`](#insn-00bcf410)
- ブロック [`00bcf410`](#insn-00bcf410) 範囲 `[['00bcf410', '00bcf417']]`
  - `FALL_THROUGH` [`00bcf414`](#insn-00bcf414) → [`00bcf418`](#insn-00bcf418)
- ブロック [`00bcf418`](#insn-00bcf418) 範囲 `[['00bcf418', '00bcf447']]`
  - `CONDITIONAL_JUMP` [`00bcf444`](#insn-00bcf444) → [`00bcf464`](#insn-00bcf464)
  - `FALL_THROUGH` [`00bcf444`](#insn-00bcf444) → [`00bcf448`](#insn-00bcf448)
- ブロック [`00bcf448`](#insn-00bcf448) 範囲 `[['00bcf448', '00bcf44b']]`
  - `CONDITIONAL_JUMP` [`00bcf448`](#insn-00bcf448) → [`00bcf484`](#insn-00bcf484)
  - `FALL_THROUGH` [`00bcf448`](#insn-00bcf448) → [`00bcf44c`](#insn-00bcf44c)
- ブロック [`00bcf44c`](#insn-00bcf44c) 範囲 `[['00bcf44c', '00bcf453']]`
  - `CONDITIONAL_JUMP` [`00bcf450`](#insn-00bcf450) → [`00bcf4a4`](#insn-00bcf4a4)
  - `FALL_THROUGH` [`00bcf450`](#insn-00bcf450) → [`00bcf454`](#insn-00bcf454)
- ブロック [`00bcf454`](#insn-00bcf454) 範囲 `[['00bcf454', '00bcf463']]`
  - `UNCONDITIONAL_JUMP` [`00bcf460`](#insn-00bcf460) → [`00bcf4e4`](#insn-00bcf4e4)
- ブロック [`00bcf464`](#insn-00bcf464) 範囲 `[['00bcf464', '00bcf46b']]`
  - `CONDITIONAL_JUMP` [`00bcf468`](#insn-00bcf468) → [`00bcf494`](#insn-00bcf494)
  - `FALL_THROUGH` [`00bcf468`](#insn-00bcf468) → [`00bcf46c`](#insn-00bcf46c)
- ブロック [`00bcf46c`](#insn-00bcf46c) 範囲 `[['00bcf46c', '00bcf473']]`
  - `CONDITIONAL_JUMP` [`00bcf470`](#insn-00bcf470) → [`00bcf4b4`](#insn-00bcf4b4)
  - `FALL_THROUGH` [`00bcf470`](#insn-00bcf470) → [`00bcf474`](#insn-00bcf474)
- ブロック [`00bcf474`](#insn-00bcf474) 範囲 `[['00bcf474', '00bcf483']]`
  - `UNCONDITIONAL_JUMP` [`00bcf480`](#insn-00bcf480) → [`00bcf4c0`](#insn-00bcf4c0)
- ブロック [`00bcf484`](#insn-00bcf484) 範囲 `[['00bcf484', '00bcf493']]`
  - `UNCONDITIONAL_JUMP` [`00bcf490`](#insn-00bcf490) → [`00bcf4e4`](#insn-00bcf4e4)
- ブロック [`00bcf494`](#insn-00bcf494) 範囲 `[['00bcf494', '00bcf4a3']]`
  - `UNCONDITIONAL_JUMP` [`00bcf4a0`](#insn-00bcf4a0) → [`00bcf4c0`](#insn-00bcf4c0)
- ブロック [`00bcf4a4`](#insn-00bcf4a4) 範囲 `[['00bcf4a4', '00bcf4b3']]`
  - `UNCONDITIONAL_JUMP` [`00bcf4b0`](#insn-00bcf4b0) → [`00bcf4c0`](#insn-00bcf4c0)
- ブロック [`00bcf4b4`](#insn-00bcf4b4) 範囲 `[['00bcf4b4', '00bcf4bf']]`
  - `FALL_THROUGH` [`00bcf4bc`](#insn-00bcf4bc) → [`00bcf4c0`](#insn-00bcf4c0)
- ブロック [`00bcf4c0`](#insn-00bcf4c0) 範囲 `[['00bcf4c0', '00bcf4df']]`
  - `CONDITIONAL_JUMP` [`00bcf4dc`](#insn-00bcf4dc) → [`00bcf54c`](#insn-00bcf54c)
  - `FALL_THROUGH` [`00bcf4dc`](#insn-00bcf4dc) → [`00bcf4e0`](#insn-00bcf4e0)
- ブロック [`00bcf4e0`](#insn-00bcf4e0) 範囲 `[['00bcf4e0', '00bcf4e3']]`
  - `FALL_THROUGH` [`00bcf4e0`](#insn-00bcf4e0) → [`00bcf4e4`](#insn-00bcf4e4)
- ブロック [`00bcf4e4`](#insn-00bcf4e4) 範囲 `[['00bcf4e4', '00bcf4f7']]`
  - `CONDITIONAL_JUMP` [`00bcf4f4`](#insn-00bcf4f4) → [`00bcf51c`](#insn-00bcf51c)
  - `FALL_THROUGH` [`00bcf4f4`](#insn-00bcf4f4) → [`00bcf4f8`](#insn-00bcf4f8)
- ブロック [`00bcf4f8`](#insn-00bcf4f8) 範囲 `[['00bcf4f8', '00bcf517']]`
  - `CONDITIONAL_JUMP` [`00bcf514`](#insn-00bcf514) → [`00bcf570`](#insn-00bcf570)
  - `FALL_THROUGH` [`00bcf514`](#insn-00bcf514) → [`00bcf518`](#insn-00bcf518)
- ブロック [`00bcf518`](#insn-00bcf518) 範囲 `[['00bcf518', '00bcf51b']]`
  - `FALL_THROUGH` [`00bcf518`](#insn-00bcf518) → [`00bcf51c`](#insn-00bcf51c)
- ブロック [`00bcf51c`](#insn-00bcf51c) 範囲 `[['00bcf51c', '00bcf51f']]`
  - `FALL_THROUGH` [`00bcf51c`](#insn-00bcf51c) → [`00bcf520`](#insn-00bcf520)
- ブロック [`00bcf520`](#insn-00bcf520) 範囲 `[['00bcf520', '00bcf54b']]`
- ブロック [`00bcf54c`](#insn-00bcf54c) 範囲 `[['00bcf54c', '00bcf56b']]`
- ブロック [`00bcf56c`](#insn-00bcf56c) 範囲 `[['00bcf56c', '00bcf56f']]`
- ブロック [`00bcf570`](#insn-00bcf570) 範囲 `[['00bcf570', '00bcf573']]`

## 命令位置別の参照

- [`00bcf3c0`](#insn-00bcf3c0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf3c4`](#insn-00bcf3c4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf3c8`](#insn-00bcf3c8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf3e8`](#insn-00bcf3e8) → [`00bcf418`](#insn-00bcf418) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf404`](#insn-00bcf404) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcf40c`](#insn-00bcf40c) → [`00bcf56c`](#insn-00bcf56c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf444`](#insn-00bcf444) → [`00bcf464`](#insn-00bcf464) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf448`](#insn-00bcf448) → [`00bcf484`](#insn-00bcf484) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf450`](#insn-00bcf450) → [`00bcf4a4`](#insn-00bcf4a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf460`](#insn-00bcf460) → [`00bcf4e4`](#insn-00bcf4e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf468`](#insn-00bcf468) → [`00bcf494`](#insn-00bcf494) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf470`](#insn-00bcf470) → [`00bcf4b4`](#insn-00bcf4b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf480`](#insn-00bcf480) → [`00bcf4c0`](#insn-00bcf4c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf490`](#insn-00bcf490) → [`00bcf4e4`](#insn-00bcf4e4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf4a0`](#insn-00bcf4a0) → [`00bcf4c0`](#insn-00bcf4c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf4b0`](#insn-00bcf4b0) → [`00bcf4c0`](#insn-00bcf4c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf4c0`](#insn-00bcf4c0) → `002a9246`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf4c0`](#insn-00bcf4c0) → `002ac5f0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf4c0`](#insn-00bcf4c0) → `002a80b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf4c0`](#insn-00bcf4c0) → `002ae6ca`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf4c8`](#insn-00bcf4c8) → `002a924a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf4c8`](#insn-00bcf4c8) → `002ac5f4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf4c8`](#insn-00bcf4c8) → `002a80b4`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf4c8`](#insn-00bcf4c8) → `002ae6ce`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf4dc`](#insn-00bcf4dc) → [`00bcf54c`](#insn-00bcf54c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf4f4`](#insn-00bcf4f4) → [`00bcf51c`](#insn-00bcf51c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf50c`](#insn-00bcf50c) → [`00bdd150`](../00bdd/00bdd150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd150` · 推定シンボル `None` · 推定型 `None`
- [`00bcf514`](#insn-00bcf514) → [`00bcf570`](#insn-00bcf570) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf520`](#insn-00bcf520) → `002a9246`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf528`](#insn-00bcf528) → [`00bdb0b0`](../00bdb/00bdb0b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0b0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf538`](#insn-00bcf538) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf53c`](#insn-00bcf53c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf540`](#insn-00bcf540) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcf550`](#insn-00bcf550) → `002917fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf558`](#insn-00bcf558) → `002a207d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcf560`](#insn-00bcf560) → `002967d9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bcf568`](#insn-00bcf568) → [`00bbb090`](../00bbb/00bbb090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbb090` · 推定シンボル `None` · 推定型 `None`
- [`00bcf56c`](#insn-00bcf56c) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`
- [`00bcf570`](#insn-00bcf570) → [`00bde1c0`](../00bde/00bde1c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcf3c0`](#insn-00bcf3c0)

~~~json
{
  "source": "00bcf3c0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf3c4`](#insn-00bcf3c4)

~~~json
{
  "source": "00bcf3c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf3c8`](#insn-00bcf3c8)

~~~json
{
  "source": "00bcf3c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf3e8`](#insn-00bcf3e8)

~~~json
{
  "source": "00bcf3e8",
  "target": "00bcf418",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf404`](#insn-00bcf404)

~~~json
{
  "source": "00bcf404",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf40c`](#insn-00bcf40c)

~~~json
{
  "source": "00bcf40c",
  "target": "00bcf56c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf444`](#insn-00bcf444)

~~~json
{
  "source": "00bcf444",
  "target": "00bcf464",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf448`](#insn-00bcf448)

~~~json
{
  "source": "00bcf448",
  "target": "00bcf484",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf450`](#insn-00bcf450)

~~~json
{
  "source": "00bcf450",
  "target": "00bcf4a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf460`](#insn-00bcf460)

~~~json
{
  "source": "00bcf460",
  "target": "00bcf4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf468`](#insn-00bcf468)

~~~json
{
  "source": "00bcf468",
  "target": "00bcf494",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf470`](#insn-00bcf470)

~~~json
{
  "source": "00bcf470",
  "target": "00bcf4b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf480`](#insn-00bcf480)

~~~json
{
  "source": "00bcf480",
  "target": "00bcf4c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf490`](#insn-00bcf490)

~~~json
{
  "source": "00bcf490",
  "target": "00bcf4e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf4a0`](#insn-00bcf4a0)

~~~json
{
  "source": "00bcf4a0",
  "target": "00bcf4c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf4b0`](#insn-00bcf4b0)

~~~json
{
  "source": "00bcf4b0",
  "target": "00bcf4c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf4c0`](#insn-00bcf4c0)

~~~json
{
  "source": "00bcf4c0",
  "target": "002a9246",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9246",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "62617369635f737472696e6700",
  "capture_start": "002a9246",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf4c0`](#insn-00bcf4c0)

~~~json
{
  "source": "00bcf4c0",
  "target": "002ac5f0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac5f0",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "62617369635f6f73747265616d00",
  "capture_start": "002ac5f0",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf4c0`](#insn-00bcf4c0)

~~~json
{
  "source": "00bcf4c0",
  "target": "002a80b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a80b0",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "62617369635f696f73747265616d00",
  "capture_start": "002a80b0",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf4c0`](#insn-00bcf4c0)

~~~json
{
  "source": "00bcf4c0",
  "target": "002ae6ca",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ae6ca",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "62617369635f6973747265616d00",
  "capture_start": "002ae6ca",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf4c8`](#insn-00bcf4c8)

~~~json
{
  "source": "00bcf4c8",
  "target": "002a924a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9246",
  "offset": 4,
  "size": 13,
  "datatype": "string",
  "bytes": "62617369635f737472696e6700",
  "capture_start": "002a9246",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf4c8`](#insn-00bcf4c8)

~~~json
{
  "source": "00bcf4c8",
  "target": "002ac5f4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac5f0",
  "offset": 4,
  "size": 14,
  "datatype": "string",
  "bytes": "62617369635f6f73747265616d00",
  "capture_start": "002ac5f0",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf4c8`](#insn-00bcf4c8)

~~~json
{
  "source": "00bcf4c8",
  "target": "002a80b4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a80b0",
  "offset": 4,
  "size": 15,
  "datatype": "string",
  "bytes": "62617369635f696f73747265616d00",
  "capture_start": "002a80b0",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf4c8`](#insn-00bcf4c8)

~~~json
{
  "source": "00bcf4c8",
  "target": "002ae6ce",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ae6ca",
  "offset": 4,
  "size": 14,
  "datatype": "string",
  "bytes": "62617369635f6973747265616d00",
  "capture_start": "002ae6ca",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf4dc`](#insn-00bcf4dc)

~~~json
{
  "source": "00bcf4dc",
  "target": "00bcf54c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf4f4`](#insn-00bcf4f4)

~~~json
{
  "source": "00bcf4f4",
  "target": "00bcf51c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf50c`](#insn-00bcf50c)

~~~json
{
  "source": "00bcf50c",
  "target": "00bdd150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf514`](#insn-00bcf514)

~~~json
{
  "source": "00bcf514",
  "target": "00bcf570",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf520`](#insn-00bcf520)

~~~json
{
  "source": "00bcf520",
  "target": "002a9246",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9246",
  "offset": 0,
  "size": 13,
  "datatype": "string",
  "bytes": "62617369635f737472696e6700",
  "capture_start": "002a9246",
  "capture_bytes": 13,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf528`](#insn-00bcf528)

~~~json
{
  "source": "00bcf528",
  "target": "00bdb0b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf538`](#insn-00bcf538)

~~~json
{
  "source": "00bcf538",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf53c`](#insn-00bcf53c)

~~~json
{
  "source": "00bcf53c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf540`](#insn-00bcf540)

~~~json
{
  "source": "00bcf540",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcf550`](#insn-00bcf550)

~~~json
{
  "source": "00bcf550",
  "target": "002917fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002917fc",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "25733a25643a20257300",
  "capture_start": "002917fc",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf558`](#insn-00bcf558)

~~~json
{
  "source": "00bcf558",
  "target": "002a207d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a207d",
  "offset": 0,
  "size": 58,
  "datatype": "string",
  "bytes": "6f75742f6c6c766d2d70726f6a6563742f6c69626378786162692f7372632f64",
  "capture_start": "002a207d",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcf560`](#insn-00bcf560)

~~~json
{
  "source": "00bcf560",
  "target": "002967d9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002967d9",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002967d9",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bcf568`](#insn-00bcf568)

~~~json
{
  "source": "00bcf568",
  "target": "00bbb090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf56c`](#insn-00bcf56c)

~~~json
{
  "source": "00bcf56c",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcf570`](#insn-00bcf570)

~~~json
{
  "source": "00bcf570",
  "target": "00bde1c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
