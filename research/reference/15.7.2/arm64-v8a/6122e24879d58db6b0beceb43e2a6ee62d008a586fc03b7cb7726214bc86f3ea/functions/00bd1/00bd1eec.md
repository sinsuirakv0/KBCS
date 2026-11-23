# 00bd1eec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bd1fb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bd1/00bd1fb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-914a633a1bbfd443d383e5e7312afe95)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd1eec",
  "name": "FUN_00bd1eec",
  "size": 700,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f441ea3fceb138e8af9c22f97e5ed0e5a87ca748b657facb0c1d15f11c090d6",
  "source_text_sha256": "9f441ea3fceb138e8af9c22f97e5ed0e5a87ca748b657facb0c1d15f11c090d6",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd1eec",
        "00bd21a7"
      ]
    ],
    "bytes_sha256": "58a13f5231a94120f424bbf2f8f407a9ffd956a825353fc055e054007ac7c111",
    "instruction_count": 175,
    "instruction_bytes": 700,
    "body_bytes": 700,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbdd50](../00bbd/00bbdd50.md)

## 呼び出し先

- [00bbdd50](../00bbd/00bbdd50.md)
- [00bc2e00](../00bc2/00bc2e00.md)
- [00bd38b4](../00bd3/00bd38b4.md)
- [00bd3954](../00bd3/00bd3954.md)
- [00bdb0d0](../00bdb/00bdb0d0.md)
- [00bdd0d0](../00bdd/00bdd0d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5763 bytes

~~~c

undefined8 * FUN_00bd1eec(long *param_1)

{
  byte *pbVar1;
  char *pcVar2;
  short *psVar3;
  char *pcVar4;
  byte *pbVar5;
  byte bVar6;
  undefined8 *puVar7;
  undefined8 *puVar8;
  ushort uVar9;
  long lVar10;
  long lVar11;
  byte *pbVar12;
  long lVar13;
  byte *pbVar14;
  byte *pbVar15;
  void *pvVar16;
  long local_40;
  undefined8 *local_38;
  
  psVar3 = (short *)*param_1;
  pbVar5 = (byte *)param_1[1];
                    /* try { // try from 00bd1f20 to 00cd1f33 has its CatchHandler @ 00bd2840 */
  if (((ulong)((long)pbVar5 - (long)psVar3) < 2) || (*psVar3 != 0x7644)) {
LAB_00bd1f24:
    puVar7 = (undefined8 *)0x0;
  }
  else {
    pbVar1 = (byte *)(psVar3 + 1);
    *param_1 = (long)pbVar1;
    if ((pbVar5 == pbVar1) || (bVar6 = *pbVar1, bVar6 < 0x31)) {
LAB_00bd20d8:
      lVar13 = FUN_00bc2e00();
      if (lVar13 == 0) {
        return (undefined8 *)0x0;
      }
      pcVar4 = (char *)*param_1;
                    /* try { // try from 00bd20ec to 00cd20f3 has its CatchHandler @ 00bd2944 */
      if ((pcVar4 == (char *)param_1[1]) || (*pcVar4 != '_')) goto LAB_00bd1f24;
      *param_1 = (long)(pcVar4 + 1);
      lVar10 = FUN_00bbdd50(param_1);
      if (lVar10 == 0) {
        return (undefined8 *)0x0;
      }
      pvVar16 = (void *)param_1[0x266];
                    /* try { // try from 00bd211c to 00cd2123 has its CatchHandler @ 00bd2934 */
      lVar11 = *(long *)((long)pvVar16 + 8);
      puVar8 = pvVar16;
      if (lVar11 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) {
LAB_00bd21a4:
                    /* WARNING: Subroutine does not return */
          _ZSt9terminatev();
        }
        lVar11 = 0;
        *puVar8 = pvVar16;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
                    /* try { // try from 00bd2148 to 00cd214f has its CatchHandler @ 00bd2904 */
                    /* try { // try from 00bd2150 to 00cd216f has its CatchHandler @ 00bd2994 */
      *(long *)((long)puVar8 + 8) = lVar11 + 0x20;
      puVar7 = (undefined8 *)((long)puVar8 + lVar11 + 0x10);
      *puVar7 = &PTR_FUN_00c19e78;
      uVar9 = *(ushort *)((long)puVar8 + lVar11 + 0x19);
      *(long *)((long)puVar8 + lVar11 + 0x20) = lVar10;
      *(long *)((long)puVar8 + lVar11 + 0x28) = lVar13;
    }
    else {
      if (bVar6 < 0x3a) {
        pbVar14 = (byte *)(psVar3 + 1);
        pbVar12 = pbVar1;
        do {
          pbVar15 = pbVar14;
          if (*pbVar12 - 0x3a < 0xfffffff6) break;
          pbVar12 = pbVar12 + 1;
                    /* try { // try from 00bd1f84 to 00cd1f8f has its CatchHandler @ 00bd29d8 */
          pbVar14 = pbVar14 + 1;
          *param_1 = (long)pbVar12;
          pbVar15 = pbVar5;
        } while (pbVar12 != pbVar5);
        pvVar16 = (void *)param_1[0x266];
        lVar13 = *(long *)((long)pvVar16 + 8);
        puVar7 = pvVar16;
        if (lVar13 - 0xfd0U < 0xfffffffffffff010) {
          puVar7 = malloc(0x1000);
          if (puVar7 == (void *)0x0) goto LAB_00bd21a4;
          lVar13 = 0;
          *puVar7 = pvVar16;
          puVar7[1] = 0;
          param_1[0x266] = (long)puVar7;
        }
        *(long *)((long)puVar7 + 8) = lVar13 + 0x20;
        local_38 = (undefined8 *)((long)puVar7 + lVar13 + 0x10);
        *local_38 = &PTR_FUN_00c17798;
        *(byte **)((long)puVar7 + lVar13 + 0x20) = pbVar1;
        *(undefined1 *)((long)puVar7 + lVar13 + 0x18) = 8;
                    /* try { // try from 00bd2008 to 00cd200f has its CatchHandler @ 00bd2864 */
        *(long *)((long)puVar7 + lVar13 + 0x28) = (long)pbVar15 - (long)pbVar1;
        *(ushort *)((long)puVar7 + lVar13 + 0x19) =
             *(ushort *)((long)puVar7 + lVar13 + 0x19) & 0xf000 | 0x540;
        pcVar4 = (char *)*param_1;
        if ((pcVar4 != (char *)param_1[1]) && (*pcVar4 == '_')) {
                    /* try { // try from 00bd202c to 00cd2033 has its CatchHandler @ 00bd2a04 */
          pcVar2 = pcVar4 + 1;
                    /* try { // try from 00bd2034 to 00cd2073 has its CatchHandler @ 00bd1b6c */
          *param_1 = (long)pcVar2;
          if ((pcVar2 != (char *)param_1[1]) && (*pcVar2 == 'p')) {
            *param_1 = (long)(pcVar4 + 2);
            puVar7 = (undefined8 *)FUN_00bd38b4(param_1,&local_38);
            return puVar7;
          }
          local_40 = FUN_00bbdd50();
          if (local_40 == 0) {
            return (undefined8 *)0x0;
          }
          puVar7 = (undefined8 *)FUN_00bd3954(param_1,&local_40,&local_38);
          return puVar7;
        }
        goto LAB_00bd1f24;
      }
      if (bVar6 != 0x5f) goto LAB_00bd20d8;
      *param_1 = (long)psVar3 + 3;
      lVar13 = FUN_00bbdd50();
      if (lVar13 == 0) {
        return (undefined8 *)0x0;
      }
                    /* try { // try from 00bd2074 to 00cd20c7 has its CatchHandler @ 00bd29ec */
      pvVar16 = (void *)param_1[0x266];
      lVar10 = *(long *)((long)pvVar16 + 8);
      puVar8 = pvVar16;
      if (lVar10 - 0xfd0U < 0xfffffffffffff010) {
        puVar8 = malloc(0x1000);
        if (puVar8 == (void *)0x0) goto LAB_00bd21a4;
        lVar10 = 0;
        *puVar8 = pvVar16;
        puVar8[1] = 0;
        param_1[0x266] = (long)puVar8;
      }
      *(long *)((long)puVar8 + 8) = lVar10 + 0x20;
      puVar7 = (undefined8 *)((long)puVar8 + lVar10 + 0x10);
      *puVar7 = &PTR_FUN_00c19e78;
      uVar9 = *(ushort *)((long)puVar8 + lVar10 + 0x19);
      *(long *)((long)puVar8 + lVar10 + 0x20) = lVar13;
      *(undefined8 *)((long)puVar8 + lVar10 + 0x28) = 0;
    }
    *(undefined1 *)(puVar7 + 1) = 0x1d;
    *(ushort *)((long)puVar7 + 9) = uVar9 & 0xf000 | 0x540;
  }
                    /* try { // try from 00bd1f38 to 00cd1f4b has its CatchHandler @ 00bd2860 */
  return puVar7;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bd1eec"></a> `00bd1eec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bd1ef0"></a> `00bd1ef0` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bd1ef4"></a> `00bd1ef4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1ef8"></a> `00bd1ef8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd1efc"></a> `00bd1efc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bd1f00"></a> `00bd1f00` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bd1f04"></a> `00bd1f04` | `09 20 40 a9` | ldp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd1f08"></a> `00bd1f08` | `0a 01 09 cb` | sub x10,x8,x9 | `FALL_THROUGH`
<a id="insn-00bd1f0c"></a> `00bd1f0c` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bd1f10"></a> `00bd1f10` | `a3 00 00 54` | b.cc 0x00bd1f24 | `CONDITIONAL_JUMP`
<a id="insn-00bd1f14"></a> `00bd1f14` | `2a 01 40 79` | ldrh w10,[x9] | `FALL_THROUGH`
<a id="insn-00bd1f18"></a> `00bd1f18` | `8b c8 8e 52` | mov w11,#0x7644 | `FALL_THROUGH`
<a id="insn-00bd1f1c"></a> `00bd1f1c` | `5f 01 0b 6b` | cmp w10,w11 | `FALL_THROUGH`
<a id="insn-00bd1f20"></a> `00bd1f20` | `00 01 00 54` | b.eq 0x00bd1f40 | `CONDITIONAL_JUMP`
<a id="insn-00bd1f24"></a> `00bd1f24` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bd1f28"></a> `00bd1f28` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bd1f2c"></a> `00bd1f2c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bd1f30"></a> `00bd1f30` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1f34"></a> `00bd1f34` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bd1f38"></a> `00bd1f38` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bd1f3c"></a> `00bd1f3c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd1f40"></a> `00bd1f40` | `34 09 00 91` | add x20,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bd1f44"></a> `00bd1f44` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bd1f48"></a> `00bd1f48` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bd1f4c"></a> `00bd1f4c` | `14 00 00 f9` | str x20,[x0] | `FALL_THROUGH`
<a id="insn-00bd1f50"></a> `00bd1f50` | `40 0c 00 54` | b.eq 0x00bd20d8 | `CONDITIONAL_JUMP`
<a id="insn-00bd1f54"></a> `00bd1f54` | `8a 02 40 39` | ldrb w10,[x20] | `FALL_THROUGH`
<a id="insn-00bd1f58"></a> `00bd1f58` | `5f c5 00 71` | cmp w10,#0x31 | `FALL_THROUGH`
<a id="insn-00bd1f5c"></a> `00bd1f5c` | `e3 0b 00 54` | b.cc 0x00bd20d8 | `CONDITIONAL_JUMP`
<a id="insn-00bd1f60"></a> `00bd1f60` | `5f e5 00 71` | cmp w10,#0x39 | `FALL_THROUGH`
<a id="insn-00bd1f64"></a> `00bd1f64` | `c8 07 00 54` | b.hi 0x00bd205c | `CONDITIONAL_JUMP`
<a id="insn-00bd1f68"></a> `00bd1f68` | `35 09 00 91` | add x21,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bd1f6c"></a> `00bd1f6c` | `e9 03 14 aa` | mov x9,x20 | `FALL_THROUGH`
<a id="insn-00bd1f70"></a> `00bd1f70` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bd1f74"></a> `00bd1f74` | `4a e9 00 51` | sub w10,w10,#0x3a | `FALL_THROUGH`
<a id="insn-00bd1f78"></a> `00bd1f78` | `5f 29 00 31` | cmn w10,#0xa | `FALL_THROUGH`
<a id="insn-00bd1f7c"></a> `00bd1f7c` | `e3 00 00 54` | b.cc 0x00bd1f98 | `CONDITIONAL_JUMP`
<a id="insn-00bd1f80"></a> `00bd1f80` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd1f84"></a> `00bd1f84` | `b5 06 00 91` | add x21,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bd1f88"></a> `00bd1f88` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bd1f8c"></a> `00bd1f8c` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00bd1f90"></a> `00bd1f90` | `01 ff ff 54` | b.ne 0x00bd1f70 | `CONDITIONAL_JUMP`
<a id="insn-00bd1f94"></a> `00bd1f94` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bd1f98"></a> `00bd1f98` | `16 98 49 f9` | ldr x22,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd1f9c"></a> `00bd1f9c` | `c9 06 40 f9` | ldr x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bd1fa0"></a> `00bd1fa0` | `28 41 3f d1` | sub x8,x9,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bd1fa4"></a> `00bd1fa4` | `1f c5 3f b1` | cmn x8,#0xff1 | `FALL_THROUGH`
<a id="insn-00bd1fa8"></a> `00bd1fa8` | `48 01 00 54` | b.hi 0x00bd1fd0 | `CONDITIONAL_JUMP`
<a id="insn-00bd1fac"></a> `00bd1fac` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bd1fb0"></a> `00bd1fb0` | `48 2c 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd1fb4"></a> `00bd1fb4` | `80 0f 00 b4` | cbz x0,0x00bd21a4 | `CONDITIONAL_JUMP`
<a id="insn-00bd1fb8"></a> `00bd1fb8` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bd1fbc"></a> `00bd1fbc` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00bd1fc0"></a> `00bd1fc0` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bd1fc4"></a> `00bd1fc4` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bd1fc8"></a> `00bd1fc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd1fcc"></a> `00bd1fcc` | `68 9a 09 f9` | str x8,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd1fd0"></a> `00bd1fd0` | `28 81 00 91` | add x8,x9,#0x20 | `FALL_THROUGH`
<a id="insn-00bd1fd4"></a> `00bd1fd4` | `ca 02 09 8b` | add x10,x22,x9 | `FALL_THROUGH`
<a id="insn-00bd1fd8"></a> `00bd1fd8` | `09 a8 80 52` | mov w9,#0x540 | `FALL_THROUGH`
<a id="insn-00bd1fdc"></a> `00bd1fdc` | `c8 06 00 f9` | str x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bd1fe0"></a> `00bd1fe0` | `28 02 00 d0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bd1fe4"></a> `00bd1fe4` | `08 61 1e 91` | add x8,x8,#0x798 | `FALL_THROUGH`
<a id="insn-00bd1fe8"></a> `00bd1fe8` | `48 0d 01 f8` | str x8,[x10, #0x10]! | `FALL_THROUGH`
<a id="insn-00bd1fec"></a> `00bd1fec` | `48 91 40 78` | ldurh w8,[x10, #0x9] | `FALL_THROUGH`
<a id="insn-00bd1ff0"></a> `00bd1ff0` | `54 09 00 f9` | str x20,[x10, #0x10] | `FALL_THROUGH`
<a id="insn-00bd1ff4"></a> `00bd1ff4` | `ab 02 14 cb` | sub x11,x21,x20 | `FALL_THROUGH`
<a id="insn-00bd1ff8"></a> `00bd1ff8` | `0c 01 80 52` | mov w12,#0x8 | `FALL_THROUGH`
<a id="insn-00bd1ffc"></a> `00bd1ffc` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bd2000"></a> `00bd2000` | `4c 21 00 39` | strb w12,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2004"></a> `00bd2004` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00bd2008"></a> `00bd2008` | `4b 0d 00 f9` | str x11,[x10, #0x18] | `FALL_THROUGH`
<a id="insn-00bd200c"></a> `00bd200c` | `48 91 00 78` | sturh w8,[x10, #0x9] | `FALL_THROUGH`
<a id="insn-00bd2010"></a> `00bd2010` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bd2014"></a> `00bd2014` | `ea 07 00 f9` | str x10,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2018"></a> `00bd2018` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bd201c"></a> `00bd201c` | `40 f8 ff 54` | b.eq 0x00bd1f24 | `CONDITIONAL_JUMP`
<a id="insn-00bd2020"></a> `00bd2020` | `0a 01 40 39` | ldrb w10,[x8] | `FALL_THROUGH`
<a id="insn-00bd2024"></a> `00bd2024` | `5f 7d 01 71` | cmp w10,#0x5f | `FALL_THROUGH`
<a id="insn-00bd2028"></a> `00bd2028` | `e1 f7 ff 54` | b.ne 0x00bd1f24 | `CONDITIONAL_JUMP`
<a id="insn-00bd202c"></a> `00bd202c` | `0a 05 00 91` | add x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2030"></a> `00bd2030` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bd2034"></a> `00bd2034` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00bd2038"></a> `00bd2038` | `60 0a 00 54` | b.eq 0x00bd2184 | `CONDITIONAL_JUMP`
<a id="insn-00bd203c"></a> `00bd203c` | `49 01 40 39` | ldrb w9,[x10] | `FALL_THROUGH`
<a id="insn-00bd2040"></a> `00bd2040` | `3f c1 01 71` | cmp w9,#0x70 | `FALL_THROUGH`
<a id="insn-00bd2044"></a> `00bd2044` | `01 0a 00 54` | b.ne 0x00bd2184 | `CONDITIONAL_JUMP`
<a id="insn-00bd2048"></a> `00bd2048` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bd204c"></a> `00bd204c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bd2050"></a> `00bd2050` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd2054"></a> `00bd2054` | `18 06 00 94` | bl 0x00bd38b4 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2058"></a> `00bd2058` | `b4 ff ff 17` | b 0x00bd1f28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd205c"></a> `00bd205c` | `5f 7d 01 71` | cmp w10,#0x5f | `FALL_THROUGH`
<a id="insn-00bd2060"></a> `00bd2060` | `c1 03 00 54` | b.ne 0x00bd20d8 | `CONDITIONAL_JUMP`
<a id="insn-00bd2064"></a> `00bd2064` | `28 0d 00 91` | add x8,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bd2068"></a> `00bd2068` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00bd206c"></a> `00bd206c` | `39 af ff 97` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2070"></a> `00bd2070` | `c0 f5 ff b4` | cbz x0,0x00bd1f28 | `CONDITIONAL_JUMP`
<a id="insn-00bd2074"></a> `00bd2074` | `75 9a 49 f9` | ldr x21,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd2078"></a> `00bd2078` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bd207c"></a> `00bd207c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd2080"></a> `00bd2080` | `a8 06 40 f9` | ldr x8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2084"></a> `00bd2084` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bd2088"></a> `00bd2088` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bd208c"></a> `00bd208c` | `08 01 00 54` | b.hi 0x00bd20ac | `CONDITIONAL_JUMP`
<a id="insn-00bd2090"></a> `00bd2090` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bd2094"></a> `00bd2094` | `0f 2c 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2098"></a> `00bd2098` | `60 08 00 b4` | cbz x0,0x00bd21a4 | `CONDITIONAL_JUMP`
<a id="insn-00bd209c"></a> `00bd209c` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bd20a0"></a> `00bd20a0` | `15 7c 00 a9` | stp x21,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bd20a4"></a> `00bd20a4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd20a8"></a> `00bd20a8` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd20ac"></a> `00bd20ac` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bd20b0"></a> `00bd20b0` | `a0 02 08 8b` | add x0,x21,x8 | `FALL_THROUGH`
<a id="insn-00bd20b4"></a> `00bd20b4` | `28 02 00 f0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bd20b8"></a> `00bd20b8` | `08 e1 39 91` | add x8,x8,#0xe78 | `FALL_THROUGH`
<a id="insn-00bd20bc"></a> `00bd20bc` | `a9 06 00 f9` | str x9,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bd20c0"></a> `00bd20c0` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bd20c4"></a> `00bd20c4` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bd20c8"></a> `00bd20c8` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bd20cc"></a> `00bd20cc` | `a9 03 80 52` | mov w9,#0x1d | `FALL_THROUGH`
<a id="insn-00bd20d0"></a> `00bd20d0` | `14 7c 01 a9` | stp x20,xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bd20d4"></a> `00bd20d4` | `27 00 00 14` | b 0x00bd2170 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd20d8"></a> `00bd20d8` | `4a c3 ff 97` | bl 0x00bc2e00 | `UNCONDITIONAL_CALL`
<a id="insn-00bd20dc"></a> `00bd20dc` | `60 f2 ff b4` | cbz x0,0x00bd1f28 | `CONDITIONAL_JUMP`
<a id="insn-00bd20e0"></a> `00bd20e0` | `69 2a 40 a9` | ldp x9,x10,[x19] | `FALL_THROUGH`
<a id="insn-00bd20e4"></a> `00bd20e4` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bd20e8"></a> `00bd20e8` | `e0 f1 ff 54` | b.eq 0x00bd1f24 | `CONDITIONAL_JUMP`
<a id="insn-00bd20ec"></a> `00bd20ec` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bd20f0"></a> `00bd20f0` | `5f 7d 01 71` | cmp w10,#0x5f | `FALL_THROUGH`
<a id="insn-00bd20f4"></a> `00bd20f4` | `81 f1 ff 54` | b.ne 0x00bd1f24 | `CONDITIONAL_JUMP`
<a id="insn-00bd20f8"></a> `00bd20f8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd20fc"></a> `00bd20fc` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bd2100"></a> `00bd2100` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd2104"></a> `00bd2104` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00bd2108"></a> `00bd2108` | `12 af ff 97` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bd210c"></a> `00bd210c` | `e0 f0 ff b4` | cbz x0,0x00bd1f28 | `CONDITIONAL_JUMP`
<a id="insn-00bd2110"></a> `00bd2110` | `76 9a 49 f9` | ldr x22,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd2114"></a> `00bd2114` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00bd2118"></a> `00bd2118` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bd211c"></a> `00bd211c` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2120"></a> `00bd2120` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bd2124"></a> `00bd2124` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bd2128"></a> `00bd2128` | `08 01 00 54` | b.hi 0x00bd2148 | `CONDITIONAL_JUMP`
<a id="insn-00bd212c"></a> `00bd212c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bd2130"></a> `00bd2130` | `e8 2b 00 94` | bl 0x00bdd0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2134"></a> `00bd2134` | `80 03 00 b4` | cbz x0,0x00bd21a4 | `CONDITIONAL_JUMP`
<a id="insn-00bd2138"></a> `00bd2138` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bd213c"></a> `00bd213c` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bd2140"></a> `00bd2140` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bd2144"></a> `00bd2144` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bd2148"></a> `00bd2148` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bd214c"></a> `00bd214c` | `c0 02 08 8b` | add x0,x22,x8 | `FALL_THROUGH`
<a id="insn-00bd2150"></a> `00bd2150` | `28 02 00 f0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bd2154"></a> `00bd2154` | `08 e1 39 91` | add x8,x8,#0xe78 | `FALL_THROUGH`
<a id="insn-00bd2158"></a> `00bd2158` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bd215c"></a> `00bd215c` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bd2160"></a> `00bd2160` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bd2164"></a> `00bd2164` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bd2168"></a> `00bd2168` | `a9 03 80 52` | mov w9,#0x1d | `FALL_THROUGH`
<a id="insn-00bd216c"></a> `00bd216c` | `14 54 01 a9` | stp x20,x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bd2170"></a> `00bd2170` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bd2174"></a> `00bd2174` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bd2178"></a> `00bd2178` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bd217c"></a> `00bd217c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bd2180"></a> `00bd2180` | `6a ff ff 17` | b 0x00bd1f28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd2184"></a> `00bd2184` | `f3 ae ff 97` | bl 0x00bbdd50 | `UNCONDITIONAL_CALL`
<a id="insn-00bd2188"></a> `00bd2188` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-00bd218c"></a> `00bd218c` | `e0 ec ff b4` | cbz x0,0x00bd1f28 | `CONDITIONAL_JUMP`
<a id="insn-00bd2190"></a> `00bd2190` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bd2194"></a> `00bd2194` | `e2 23 00 91` | add x2,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bd2198"></a> `00bd2198` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd219c"></a> `00bd219c` | `ee 05 00 94` | bl 0x00bd3954 | `UNCONDITIONAL_CALL`
<a id="insn-00bd21a0"></a> `00bd21a0` | `62 ff ff 17` | b 0x00bd1f28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bd21a4"></a> `00bd21a4` | `cb 23 00 94` | bl 0x00bdb0d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd1eec`](#insn-00bd1eec) 範囲 `[['00bd1eec', '00bd1f13']]`
  - `CONDITIONAL_JUMP` [`00bd1f10`](#insn-00bd1f10) → [`00bd1f24`](#insn-00bd1f24)
  - `FALL_THROUGH` [`00bd1f10`](#insn-00bd1f10) → [`00bd1f14`](#insn-00bd1f14)
- ブロック [`00bd1f14`](#insn-00bd1f14) 範囲 `[['00bd1f14', '00bd1f1f']]`
  - `FALL_THROUGH` [`00bd1f1c`](#insn-00bd1f1c) → [`00bd1f20`](#insn-00bd1f20)
- ブロック [`00bd1f20`](#insn-00bd1f20) 範囲 `[['00bd1f20', '00bd1f23']]`
  - `CONDITIONAL_JUMP` [`00bd1f20`](#insn-00bd1f20) → [`00bd1f40`](#insn-00bd1f40)
  - `FALL_THROUGH` [`00bd1f20`](#insn-00bd1f20) → [`00bd1f24`](#insn-00bd1f24)
- ブロック [`00bd1f24`](#insn-00bd1f24) 範囲 `[['00bd1f24', '00bd1f27']]`
  - `FALL_THROUGH` [`00bd1f24`](#insn-00bd1f24) → [`00bd1f28`](#insn-00bd1f28)
- ブロック [`00bd1f28`](#insn-00bd1f28) 範囲 `[['00bd1f28', '00bd1f37']]`
  - `FALL_THROUGH` [`00bd1f34`](#insn-00bd1f34) → [`00bd1f38`](#insn-00bd1f38)
- ブロック [`00bd1f38`](#insn-00bd1f38) 範囲 `[['00bd1f38', '00bd1f3f']]`
- ブロック [`00bd1f40`](#insn-00bd1f40) 範囲 `[['00bd1f40', '00bd1f53']]`
  - `CONDITIONAL_JUMP` [`00bd1f50`](#insn-00bd1f50) → [`00bd20d8`](#insn-00bd20d8)
  - `FALL_THROUGH` [`00bd1f50`](#insn-00bd1f50) → [`00bd1f54`](#insn-00bd1f54)
- ブロック [`00bd1f54`](#insn-00bd1f54) 範囲 `[['00bd1f54', '00bd1f5f']]`
  - `CONDITIONAL_JUMP` [`00bd1f5c`](#insn-00bd1f5c) → [`00bd20d8`](#insn-00bd20d8)
  - `FALL_THROUGH` [`00bd1f5c`](#insn-00bd1f5c) → [`00bd1f60`](#insn-00bd1f60)
- ブロック [`00bd1f60`](#insn-00bd1f60) 範囲 `[['00bd1f60', '00bd1f67']]`
  - `CONDITIONAL_JUMP` [`00bd1f64`](#insn-00bd1f64) → [`00bd205c`](#insn-00bd205c)
  - `FALL_THROUGH` [`00bd1f64`](#insn-00bd1f64) → [`00bd1f68`](#insn-00bd1f68)
- ブロック [`00bd1f68`](#insn-00bd1f68) 範囲 `[['00bd1f68', '00bd1f6f']]`
  - `FALL_THROUGH` [`00bd1f6c`](#insn-00bd1f6c) → [`00bd1f70`](#insn-00bd1f70)
- ブロック [`00bd1f70`](#insn-00bd1f70) 範囲 `[['00bd1f70', '00bd1f7f']]`
  - `CONDITIONAL_JUMP` [`00bd1f7c`](#insn-00bd1f7c) → [`00bd1f98`](#insn-00bd1f98)
  - `FALL_THROUGH` [`00bd1f7c`](#insn-00bd1f7c) → [`00bd1f80`](#insn-00bd1f80)
- ブロック [`00bd1f80`](#insn-00bd1f80) 範囲 `[['00bd1f80', '00bd1f83']]`
  - `FALL_THROUGH` [`00bd1f80`](#insn-00bd1f80) → [`00bd1f84`](#insn-00bd1f84)
- ブロック [`00bd1f84`](#insn-00bd1f84) 範囲 `[['00bd1f84', '00bd1f93']]`
  - `CONDITIONAL_JUMP` [`00bd1f90`](#insn-00bd1f90) → [`00bd1f70`](#insn-00bd1f70)
  - `FALL_THROUGH` [`00bd1f90`](#insn-00bd1f90) → [`00bd1f94`](#insn-00bd1f94)
- ブロック [`00bd1f94`](#insn-00bd1f94) 範囲 `[['00bd1f94', '00bd1f97']]`
  - `FALL_THROUGH` [`00bd1f94`](#insn-00bd1f94) → [`00bd1f98`](#insn-00bd1f98)
- ブロック [`00bd1f98`](#insn-00bd1f98) 範囲 `[['00bd1f98', '00bd1fab']]`
  - `CONDITIONAL_JUMP` [`00bd1fa8`](#insn-00bd1fa8) → [`00bd1fd0`](#insn-00bd1fd0)
  - `FALL_THROUGH` [`00bd1fa8`](#insn-00bd1fa8) → [`00bd1fac`](#insn-00bd1fac)
- ブロック [`00bd1fac`](#insn-00bd1fac) 範囲 `[['00bd1fac', '00bd1fb7']]`
  - `CONDITIONAL_JUMP` [`00bd1fb4`](#insn-00bd1fb4) → [`00bd21a4`](#insn-00bd21a4)
  - `FALL_THROUGH` [`00bd1fb4`](#insn-00bd1fb4) → [`00bd1fb8`](#insn-00bd1fb8)
- ブロック [`00bd1fb8`](#insn-00bd1fb8) 範囲 `[['00bd1fb8', '00bd1fcf']]`
  - `FALL_THROUGH` [`00bd1fcc`](#insn-00bd1fcc) → [`00bd1fd0`](#insn-00bd1fd0)
- ブロック [`00bd1fd0`](#insn-00bd1fd0) 範囲 `[['00bd1fd0', '00bd2007']]`
  - `FALL_THROUGH` [`00bd2004`](#insn-00bd2004) → [`00bd2008`](#insn-00bd2008)
- ブロック [`00bd2008`](#insn-00bd2008) 範囲 `[['00bd2008', '00bd201f']]`
  - `CONDITIONAL_JUMP` [`00bd201c`](#insn-00bd201c) → [`00bd1f24`](#insn-00bd1f24)
  - `FALL_THROUGH` [`00bd201c`](#insn-00bd201c) → [`00bd2020`](#insn-00bd2020)
- ブロック [`00bd2020`](#insn-00bd2020) 範囲 `[['00bd2020', '00bd202b']]`
  - `CONDITIONAL_JUMP` [`00bd2028`](#insn-00bd2028) → [`00bd1f24`](#insn-00bd1f24)
  - `FALL_THROUGH` [`00bd2028`](#insn-00bd2028) → [`00bd202c`](#insn-00bd202c)
- ブロック [`00bd202c`](#insn-00bd202c) 範囲 `[['00bd202c', '00bd2033']]`
  - `FALL_THROUGH` [`00bd2030`](#insn-00bd2030) → [`00bd2034`](#insn-00bd2034)
- ブロック [`00bd2034`](#insn-00bd2034) 範囲 `[['00bd2034', '00bd203b']]`
  - `CONDITIONAL_JUMP` [`00bd2038`](#insn-00bd2038) → [`00bd2184`](#insn-00bd2184)
  - `FALL_THROUGH` [`00bd2038`](#insn-00bd2038) → [`00bd203c`](#insn-00bd203c)
- ブロック [`00bd203c`](#insn-00bd203c) 範囲 `[['00bd203c', '00bd2047']]`
  - `CONDITIONAL_JUMP` [`00bd2044`](#insn-00bd2044) → [`00bd2184`](#insn-00bd2184)
  - `FALL_THROUGH` [`00bd2044`](#insn-00bd2044) → [`00bd2048`](#insn-00bd2048)
- ブロック [`00bd2048`](#insn-00bd2048) 範囲 `[['00bd2048', '00bd205b']]`
  - `UNCONDITIONAL_JUMP` [`00bd2058`](#insn-00bd2058) → [`00bd1f28`](#insn-00bd1f28)
- ブロック [`00bd205c`](#insn-00bd205c) 範囲 `[['00bd205c', '00bd2063']]`
  - `CONDITIONAL_JUMP` [`00bd2060`](#insn-00bd2060) → [`00bd20d8`](#insn-00bd20d8)
  - `FALL_THROUGH` [`00bd2060`](#insn-00bd2060) → [`00bd2064`](#insn-00bd2064)
- ブロック [`00bd2064`](#insn-00bd2064) 範囲 `[['00bd2064', '00bd2073']]`
  - `CONDITIONAL_JUMP` [`00bd2070`](#insn-00bd2070) → [`00bd1f28`](#insn-00bd1f28)
  - `FALL_THROUGH` [`00bd2070`](#insn-00bd2070) → [`00bd2074`](#insn-00bd2074)
- ブロック [`00bd2074`](#insn-00bd2074) 範囲 `[['00bd2074', '00bd208f']]`
  - `CONDITIONAL_JUMP` [`00bd208c`](#insn-00bd208c) → [`00bd20ac`](#insn-00bd20ac)
  - `FALL_THROUGH` [`00bd208c`](#insn-00bd208c) → [`00bd2090`](#insn-00bd2090)
- ブロック [`00bd2090`](#insn-00bd2090) 範囲 `[['00bd2090', '00bd209b']]`
  - `CONDITIONAL_JUMP` [`00bd2098`](#insn-00bd2098) → [`00bd21a4`](#insn-00bd21a4)
  - `FALL_THROUGH` [`00bd2098`](#insn-00bd2098) → [`00bd209c`](#insn-00bd209c)
- ブロック [`00bd209c`](#insn-00bd209c) 範囲 `[['00bd209c', '00bd20ab']]`
  - `FALL_THROUGH` [`00bd20a8`](#insn-00bd20a8) → [`00bd20ac`](#insn-00bd20ac)
- ブロック [`00bd20ac`](#insn-00bd20ac) 範囲 `[['00bd20ac', '00bd20d7']]`
  - `UNCONDITIONAL_JUMP` [`00bd20d4`](#insn-00bd20d4) → [`00bd2170`](#insn-00bd2170)
- ブロック [`00bd20d8`](#insn-00bd20d8) 範囲 `[['00bd20d8', '00bd20df']]`
  - `CONDITIONAL_JUMP` [`00bd20dc`](#insn-00bd20dc) → [`00bd1f28`](#insn-00bd1f28)
  - `FALL_THROUGH` [`00bd20dc`](#insn-00bd20dc) → [`00bd20e0`](#insn-00bd20e0)
- ブロック [`00bd20e0`](#insn-00bd20e0) 範囲 `[['00bd20e0', '00bd20eb']]`
  - `CONDITIONAL_JUMP` [`00bd20e8`](#insn-00bd20e8) → [`00bd1f24`](#insn-00bd1f24)
  - `FALL_THROUGH` [`00bd20e8`](#insn-00bd20e8) → [`00bd20ec`](#insn-00bd20ec)
- ブロック [`00bd20ec`](#insn-00bd20ec) 範囲 `[['00bd20ec', '00bd20f7']]`
  - `CONDITIONAL_JUMP` [`00bd20f4`](#insn-00bd20f4) → [`00bd1f24`](#insn-00bd1f24)
  - `FALL_THROUGH` [`00bd20f4`](#insn-00bd20f4) → [`00bd20f8`](#insn-00bd20f8)
- ブロック [`00bd20f8`](#insn-00bd20f8) 範囲 `[['00bd20f8', '00bd210f']]`
  - `CONDITIONAL_JUMP` [`00bd210c`](#insn-00bd210c) → [`00bd1f28`](#insn-00bd1f28)
  - `FALL_THROUGH` [`00bd210c`](#insn-00bd210c) → [`00bd2110`](#insn-00bd2110)
- ブロック [`00bd2110`](#insn-00bd2110) 範囲 `[['00bd2110', '00bd211b']]`
  - `FALL_THROUGH` [`00bd2118`](#insn-00bd2118) → [`00bd211c`](#insn-00bd211c)
- ブロック [`00bd211c`](#insn-00bd211c) 範囲 `[['00bd211c', '00bd212b']]`
  - `CONDITIONAL_JUMP` [`00bd2128`](#insn-00bd2128) → [`00bd2148`](#insn-00bd2148)
  - `FALL_THROUGH` [`00bd2128`](#insn-00bd2128) → [`00bd212c`](#insn-00bd212c)
- ブロック [`00bd212c`](#insn-00bd212c) 範囲 `[['00bd212c', '00bd2137']]`
  - `CONDITIONAL_JUMP` [`00bd2134`](#insn-00bd2134) → [`00bd21a4`](#insn-00bd21a4)
  - `FALL_THROUGH` [`00bd2134`](#insn-00bd2134) → [`00bd2138`](#insn-00bd2138)
- ブロック [`00bd2138`](#insn-00bd2138) 範囲 `[['00bd2138', '00bd2147']]`
  - `FALL_THROUGH` [`00bd2144`](#insn-00bd2144) → [`00bd2148`](#insn-00bd2148)
- ブロック [`00bd2148`](#insn-00bd2148) 範囲 `[['00bd2148', '00bd214f']]`
  - `FALL_THROUGH` [`00bd214c`](#insn-00bd214c) → [`00bd2150`](#insn-00bd2150)
- ブロック [`00bd2150`](#insn-00bd2150) 範囲 `[['00bd2150', '00bd216f']]`
  - `FALL_THROUGH` [`00bd216c`](#insn-00bd216c) → [`00bd2170`](#insn-00bd2170)
- ブロック [`00bd2170`](#insn-00bd2170) 範囲 `[['00bd2170', '00bd2183']]`
  - `UNCONDITIONAL_JUMP` [`00bd2180`](#insn-00bd2180) → [`00bd1f28`](#insn-00bd1f28)
- ブロック [`00bd2184`](#insn-00bd2184) 範囲 `[['00bd2184', '00bd218f']]`
  - `CONDITIONAL_JUMP` [`00bd218c`](#insn-00bd218c) → [`00bd1f28`](#insn-00bd1f28)
  - `FALL_THROUGH` [`00bd218c`](#insn-00bd218c) → [`00bd2190`](#insn-00bd2190)
- ブロック [`00bd2190`](#insn-00bd2190) 範囲 `[['00bd2190', '00bd21a3']]`
  - `UNCONDITIONAL_JUMP` [`00bd21a0`](#insn-00bd21a0) → [`00bd1f28`](#insn-00bd1f28)
- ブロック [`00bd21a4`](#insn-00bd21a4) 範囲 `[['00bd21a4', '00bd21a7']]`

## 命令位置別の参照

- [`00bd1ef4`](#insn-00bd1ef4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1ef8`](#insn-00bd1ef8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1efc`](#insn-00bd1efc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1f10`](#insn-00bd1f10) → [`00bd1f24`](#insn-00bd1f24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1f20`](#insn-00bd1f20) → [`00bd1f40`](#insn-00bd1f40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1f28`](#insn-00bd1f28) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1f2c`](#insn-00bd1f2c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1f30`](#insn-00bd1f30) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1f50`](#insn-00bd1f50) → [`00bd20d8`](#insn-00bd20d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1f5c`](#insn-00bd1f5c) → [`00bd20d8`](#insn-00bd20d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1f64`](#insn-00bd1f64) → [`00bd205c`](#insn-00bd205c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1f7c`](#insn-00bd1f7c) → [`00bd1f98`](#insn-00bd1f98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1f90`](#insn-00bd1f90) → [`00bd1f70`](#insn-00bd1f70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1fa8`](#insn-00bd1fa8) → [`00bd1fd0`](#insn-00bd1fd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1fb0`](#insn-00bd1fb0) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bd1fb4`](#insn-00bd1fb4) → [`00bd21a4`](#insn-00bd21a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd1fe8`](#insn-00bd1fe8) → `00c17798`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bd2014`](#insn-00bd2014) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd201c`](#insn-00bd201c) → [`00bd1f24`](#insn-00bd1f24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2028`](#insn-00bd2028) → [`00bd1f24`](#insn-00bd1f24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2038`](#insn-00bd2038) → [`00bd2184`](#insn-00bd2184) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2044`](#insn-00bd2044) → [`00bd2184`](#insn-00bd2184) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2054`](#insn-00bd2054) → [`00bd38b4`](../00bd3/00bd38b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd38b4` · 推定シンボル `None` · 推定型 `None`
- [`00bd2058`](#insn-00bd2058) → [`00bd1f28`](#insn-00bd1f28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2060`](#insn-00bd2060) → [`00bd20d8`](#insn-00bd20d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd206c`](#insn-00bd206c) → [`00bbdd50`](../00bbd/00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bd2070`](#insn-00bd2070) → [`00bd1f28`](#insn-00bd1f28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd208c`](#insn-00bd208c) → [`00bd20ac`](#insn-00bd20ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2094`](#insn-00bd2094) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bd2098`](#insn-00bd2098) → [`00bd21a4`](#insn-00bd21a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd20c4`](#insn-00bd20c4) → `00c19e78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bd20d4`](#insn-00bd20d4) → [`00bd2170`](#insn-00bd2170) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd20d8`](#insn-00bd20d8) → [`00bc2e00`](../00bc2/00bc2e00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2e00` · 推定シンボル `None` · 推定型 `None`
- [`00bd20dc`](#insn-00bd20dc) → [`00bd1f28`](#insn-00bd1f28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd20e8`](#insn-00bd20e8) → [`00bd1f24`](#insn-00bd1f24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd20f4`](#insn-00bd20f4) → [`00bd1f24`](#insn-00bd1f24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2108`](#insn-00bd2108) → [`00bbdd50`](../00bbd/00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bd210c`](#insn-00bd210c) → [`00bd1f28`](#insn-00bd1f28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2128`](#insn-00bd2128) → [`00bd2148`](#insn-00bd2148) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2130`](#insn-00bd2130) → [`00bdd0d0`](../00bdd/00bdd0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bd2134`](#insn-00bd2134) → [`00bd21a4`](#insn-00bd21a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2160`](#insn-00bd2160) → `00c19e78`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bd2180`](#insn-00bd2180) → [`00bd1f28`](#insn-00bd1f28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd2184`](#insn-00bd2184) → [`00bbdd50`](../00bbd/00bbdd50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbdd50` · 推定シンボル `None` · 推定型 `None`
- [`00bd2188`](#insn-00bd2188) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd218c`](#insn-00bd218c) → [`00bd1f28`](#insn-00bd1f28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd219c`](#insn-00bd219c) → [`00bd3954`](../00bd3/00bd3954.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd3954` · 推定シンボル `None` · 推定型 `None`
- [`00bd21a0`](#insn-00bd21a0) → [`00bd1f28`](#insn-00bd1f28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd21a4`](#insn-00bd21a4) → [`00bdb0d0`](../00bdb/00bdb0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd1ef4`](#insn-00bd1ef4)

~~~json
{
  "source": "00bd1ef4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1ef8`](#insn-00bd1ef8)

~~~json
{
  "source": "00bd1ef8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1efc`](#insn-00bd1efc)

~~~json
{
  "source": "00bd1efc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1f10`](#insn-00bd1f10)

~~~json
{
  "source": "00bd1f10",
  "target": "00bd1f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1f20`](#insn-00bd1f20)

~~~json
{
  "source": "00bd1f20",
  "target": "00bd1f40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1f28`](#insn-00bd1f28)

~~~json
{
  "source": "00bd1f28",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1f2c`](#insn-00bd1f2c)

~~~json
{
  "source": "00bd1f2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1f30`](#insn-00bd1f30)

~~~json
{
  "source": "00bd1f30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1f50`](#insn-00bd1f50)

~~~json
{
  "source": "00bd1f50",
  "target": "00bd20d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1f5c`](#insn-00bd1f5c)

~~~json
{
  "source": "00bd1f5c",
  "target": "00bd20d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1f64`](#insn-00bd1f64)

~~~json
{
  "source": "00bd1f64",
  "target": "00bd205c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1f7c`](#insn-00bd1f7c)

~~~json
{
  "source": "00bd1f7c",
  "target": "00bd1f98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1f90`](#insn-00bd1f90)

~~~json
{
  "source": "00bd1f90",
  "target": "00bd1f70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1fa8`](#insn-00bd1fa8)

~~~json
{
  "source": "00bd1fa8",
  "target": "00bd1fd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1fb0`](#insn-00bd1fb0)

~~~json
{
  "source": "00bd1fb0",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd1fb4`](#insn-00bd1fb4)

~~~json
{
  "source": "00bd1fb4",
  "target": "00bd21a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd1fe8`](#insn-00bd1fe8)

~~~json
{
  "source": "00bd1fe8",
  "target": "00c17798",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17798",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bd2014`](#insn-00bd2014)

~~~json
{
  "source": "00bd2014",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd201c`](#insn-00bd201c)

~~~json
{
  "source": "00bd201c",
  "target": "00bd1f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2028`](#insn-00bd2028)

~~~json
{
  "source": "00bd2028",
  "target": "00bd1f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2038`](#insn-00bd2038)

~~~json
{
  "source": "00bd2038",
  "target": "00bd2184",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2044`](#insn-00bd2044)

~~~json
{
  "source": "00bd2044",
  "target": "00bd2184",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2054`](#insn-00bd2054)

~~~json
{
  "source": "00bd2054",
  "target": "00bd38b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2058`](#insn-00bd2058)

~~~json
{
  "source": "00bd2058",
  "target": "00bd1f28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2060`](#insn-00bd2060)

~~~json
{
  "source": "00bd2060",
  "target": "00bd20d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd206c`](#insn-00bd206c)

~~~json
{
  "source": "00bd206c",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2070`](#insn-00bd2070)

~~~json
{
  "source": "00bd2070",
  "target": "00bd1f28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd208c`](#insn-00bd208c)

~~~json
{
  "source": "00bd208c",
  "target": "00bd20ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2094`](#insn-00bd2094)

~~~json
{
  "source": "00bd2094",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2098`](#insn-00bd2098)

~~~json
{
  "source": "00bd2098",
  "target": "00bd21a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd20c4`](#insn-00bd20c4)

~~~json
{
  "source": "00bd20c4",
  "target": "00c19e78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19e78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bd20d4`](#insn-00bd20d4)

~~~json
{
  "source": "00bd20d4",
  "target": "00bd2170",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd20d8`](#insn-00bd20d8)

~~~json
{
  "source": "00bd20d8",
  "target": "00bc2e00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd20dc`](#insn-00bd20dc)

~~~json
{
  "source": "00bd20dc",
  "target": "00bd1f28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd20e8`](#insn-00bd20e8)

~~~json
{
  "source": "00bd20e8",
  "target": "00bd1f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd20f4`](#insn-00bd20f4)

~~~json
{
  "source": "00bd20f4",
  "target": "00bd1f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2108`](#insn-00bd2108)

~~~json
{
  "source": "00bd2108",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd210c`](#insn-00bd210c)

~~~json
{
  "source": "00bd210c",
  "target": "00bd1f28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2128`](#insn-00bd2128)

~~~json
{
  "source": "00bd2128",
  "target": "00bd2148",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2130`](#insn-00bd2130)

~~~json
{
  "source": "00bd2130",
  "target": "00bdd0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2134`](#insn-00bd2134)

~~~json
{
  "source": "00bd2134",
  "target": "00bd21a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2160`](#insn-00bd2160)

~~~json
{
  "source": "00bd2160",
  "target": "00c19e78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19e78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bd2180`](#insn-00bd2180)

~~~json
{
  "source": "00bd2180",
  "target": "00bd1f28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd2184`](#insn-00bd2184)

~~~json
{
  "source": "00bd2184",
  "target": "00bbdd50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd2188`](#insn-00bd2188)

~~~json
{
  "source": "00bd2188",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd218c`](#insn-00bd218c)

~~~json
{
  "source": "00bd218c",
  "target": "00bd1f28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd219c`](#insn-00bd219c)

~~~json
{
  "source": "00bd219c",
  "target": "00bd3954",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd21a0`](#insn-00bd21a0)

~~~json
{
  "source": "00bd21a0",
  "target": "00bd1f28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd21a4`](#insn-00bd21a4)

~~~json
{
  "source": "00bd21a4",
  "target": "00bdb0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
