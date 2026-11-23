# 00bc5fdc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00bc5f14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00bc5/00bc5f14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0079.md#compare-fc41b07ef895fcee90f73e79313a30cd)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00bc6020`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00bc6/00bc6020.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-0b432108463ec1bc734fc458e9b8ab39)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc5fdc",
  "name": "FUN_00bc5fdc",
  "size": 852,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "461851f9a14e893071ec627cd161c9efc926b9f801de5ea372b5ceecd34943de",
  "source_text_sha256": "461851f9a14e893071ec627cd161c9efc926b9f801de5ea372b5ceecd34943de",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc5fdc",
        "00bc632f"
      ]
    ],
    "bytes_sha256": "cd506ea0043c8cf078983b17de7f5aa13cfb425b89ff919556971a2ba0d8cf98",
    "instruction_count": 213,
    "instruction_bytes": 852,
    "body_bytes": 852,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bc2ec8](../00bc2/00bc2ec8.md)

## 呼び出し先

- [00bbde18](../00bbd/00bbde18.md)
- [00bbff2c](../00bbf/00bbff2c.md)
- [00bc2ec8](../00bc2/00bc2ec8.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bdb180](../00bdb/00bdb180.md)
- [00bdd180](../00bdd/00bdd180.md)
- [00bdd200](../00bdd/00bdd200.md)
- [00bde270](../00bde/00bde270.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6851 bytes

~~~c

undefined8 * FUN_00bc5fdc(long *param_1)

{
  long *__src;
  long lVar1;
  long lVar2;
  long lVar3;
  long *__ptr;
  undefined8 *puVar4;
  byte *pbVar5;
  long lVar6;
  long lVar7;
  byte *pbVar8;
  byte *pbVar9;
  long lVar10;
  long *plVar11;
  void *pvVar12;
  undefined1 uVar13;
  byte *pbVar14;
  size_t __n;
  long lVar15;
  byte *pbVar16;
  undefined8 *puVar17;
  undefined1 auVar18 [16];
  
  lVar2 = FUN_00bbde18();
  if ((lVar2 != 0) && (lVar3 = FUN_00bc2ec8(param_1), lVar3 != 0)) {
    pbVar16 = (byte *)*param_1;
    pbVar5 = (byte *)param_1[1];
    pbVar14 = pbVar16;
    if ((pbVar16 != pbVar5) && (*pbVar16 == 0x6e)) {
      pbVar14 = pbVar16 + 1;
      *param_1 = (long)pbVar14;
    }
    if (pbVar5 != pbVar14) {
      if (*pbVar14 - 0x3a < 0xfffffff6) {
        pbVar16 = (byte *)0x0;
        lVar10 = 0;
      }
      else {
        do {
          pbVar8 = pbVar14;
          if (*pbVar14 - 0x3a < 0xfffffff6) break;
          pbVar14 = pbVar14 + 1;
                    /* try { // try from 00bc6084 to 00cc608b has its CatchHandler @ 00bc8ae8 */
          *param_1 = (long)pbVar14;
          pbVar8 = pbVar5;
        } while (pbVar14 != pbVar5);
        lVar10 = (long)pbVar8 - (long)pbVar16;
        pbVar14 = pbVar8;
      }
      if (pbVar14 != pbVar5) {
        lVar7 = param_1[2];
        lVar1 = param_1[3];
        __src = param_1 + 5;
                    /* try { // try from 00bc60c8 to 00cc60d3 has its CatchHandler @ 00bc8538 */
        do {
          if (*pbVar14 != 0x5f) {
                    /* try { // try from 00bc6228 to 00cc6233 has its CatchHandler @ 00bc8504 */
            if ((pbVar14 == pbVar5) || (*pbVar14 != 0x70)) {
                    /* try { // try from 00bc6244 to 00cc6257 has its CatchHandler @ 00bc84d8 */
              uVar13 = 0;
            }
            else {
              pbVar14 = pbVar14 + 1;
              uVar13 = 1;
                    /* try { // try from 00bc6234 to 00cc6243 has its CatchHandler @ 00bc84f0 */
              *param_1 = (long)pbVar14;
            }
            if (pbVar14 == pbVar5) {
              return (undefined8 *)0x0;
            }
            if (*pbVar14 != 0x45) {
              return (undefined8 *)0x0;
            }
            *param_1 = (long)(pbVar14 + 1);
            auVar18 = FUN_00bbff2c(param_1,lVar1 - lVar7 >> 3);
            pvVar12 = (void *)param_1[0x266];
            lVar7 = *(long *)((long)pvVar12 + 8);
            puVar4 = pvVar12;
            if (lVar7 - 4000U < 0xfffffffffffff010) {
              puVar4 = malloc(0x1000);
              if (puVar4 == (void *)0x0) goto LAB_00bc6324;
              lVar7 = 0;
              *puVar4 = pvVar12;
              puVar4[1] = 0;
              param_1[0x266] = (long)puVar4;
            }
            *(long *)((long)puVar4 + 8) = lVar7 + 0x50;
            puVar17 = (undefined8 *)((long)puVar4 + lVar7 + 0x10);
            *puVar17 = &PTR_FUN_00c18e88;
            *(undefined1 *)((long)puVar4 + lVar7 + 0x18) = 0x3b;
            *(undefined1 (*) [16])((long)puVar4 + lVar7 + 0x40) = auVar18;
                    /* try { // try from 00bc62e4 to 00cc62ef has its CatchHandler @ 00bc8964 */
            *(undefined1 *)((long)puVar4 + lVar7 + 0x50) = uVar13;
            *(ushort *)((long)puVar4 + lVar7 + 0x19) =
                 *(ushort *)((long)puVar4 + lVar7 + 0x19) & 0xf000 | 0x540;
            *(long *)((long)puVar4 + lVar7 + 0x20) = lVar2;
            *(long *)((long)puVar4 + lVar7 + 0x28) = lVar3;
            *(byte **)((long)puVar4 + lVar7 + 0x30) = pbVar16;
            *(long *)((long)puVar4 + lVar7 + 0x38) = lVar10;
            return puVar17;
          }
          pbVar14 = pbVar14 + 1;
          *param_1 = (long)pbVar14;
          if ((pbVar5 == pbVar14) || (pbVar8 = pbVar14, *pbVar14 - 0x3a < 0xfffffff6)) {
            pbVar14 = (byte *)0x0;
            lVar15 = 0;
          }
          else {
            do {
              pbVar9 = pbVar8;
              if (*pbVar8 - 0x3a < 0xfffffff6) break;
              pbVar8 = pbVar8 + 1;
              *param_1 = (long)pbVar8;
              pbVar9 = pbVar5;
            } while (pbVar8 != pbVar5);
            lVar15 = (long)pbVar9 - (long)pbVar14;
          }
          pvVar12 = (void *)param_1[0x266];
          lVar6 = *(long *)((long)pvVar12 + 8);
                    /* try { // try from 00bc61bc to 00cc61cb has its CatchHandler @ 00bc8d04 */
          puVar4 = pvVar12;
          if (lVar6 - 0xfd0U < 0xfffffffffffff010) {
            puVar4 = malloc(0x1000);
            if (puVar4 == (void *)0x0) {
LAB_00bc6324:
                    /* WARNING: Subroutine does not return */
              _ZSt9terminatev();
            }
            lVar6 = 0;
            *puVar4 = pvVar12;
            puVar4[1] = 0;
                    /* try { // try from 00bc60d4 to 00cc60e3 has its CatchHandler @ 00bc8524 */
            param_1[0x266] = (long)puVar4;
          }
                    /* try { // try from 00bc60e4 to 00cc60f7 has its CatchHandler @ 00bc850c */
          *(long *)((long)puVar4 + 8) = lVar6 + 0x20;
          puVar17 = (undefined8 *)((long)puVar4 + lVar6 + 0x10);
          *puVar17 = &PTR_FUN_00c17848;
          *(byte **)((long)puVar4 + lVar6 + 0x20) = pbVar14;
          *(undefined1 *)((long)puVar4 + lVar6 + 0x18) = 8;
          *(long *)((long)puVar4 + lVar6 + 0x28) = lVar15;
          *(ushort *)((long)puVar4 + lVar6 + 0x19) =
               *(ushort *)((long)puVar4 + lVar6 + 0x19) & 0xf000 | 0x540;
          plVar11 = (long *)param_1[3];
          if (plVar11 == (long *)param_1[4]) {
            __ptr = (long *)param_1[2];
            __n = (long)plVar11 - (long)__ptr;
            if (__ptr == __src) {
              pvVar12 = malloc(__n * 2);
                    /* try { // try from 00bc61e0 to 00cc61e7 has its CatchHandler @ 00bc8ae8 */
              if (pvVar12 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                abort();
              }
              if (plVar11 != __src) {
                memcpy(pvVar12,__src,__n);
              }
              param_1[2] = (long)pvVar12;
            }
            else {
              pvVar12 = realloc(__ptr,__n * 2);
              param_1[2] = (long)pvVar12;
              if (pvVar12 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                abort();
              }
            }
            plVar11 = (long *)((long)pvVar12 + __n);
            param_1[4] = (long)((long)pvVar12 + ((long)__n >> 2) * 8);
          }
          param_1[3] = (long)(plVar11 + 1);
          *plVar11 = (long)puVar17;
          pbVar14 = (byte *)*param_1;
          pbVar5 = (byte *)param_1[1];
        } while (pbVar14 != pbVar5);
      }
    }
  }
                    /* try { // try from 00bc631c to 00cc632b has its CatchHandler @ 00bc8cfc */
  return (undefined8 *)0x0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bc5fdc"></a> `00bc5fdc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bc5fe0"></a> `00bc5fe0` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bc5fe4"></a> `00bc5fe4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc5fe8"></a> `00bc5fe8` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc5fec"></a> `00bc5fec` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bc5ff0"></a> `00bc5ff0` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc5ff4"></a> `00bc5ff4` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bc5ff8"></a> `00bc5ff8` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bc5ffc"></a> `00bc5ffc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bc6000"></a> `00bc6000` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bc6004"></a> `00bc6004` | `85 df ff 97` | bl 0x00bbde18 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6008"></a> `00bc6008` | `c0 17 00 b4` | cbz x0,0x00bc6300 | `CONDITIONAL_JUMP`
<a id="insn-00bc600c"></a> `00bc600c` | `a0 83 1f f8` | stur x0,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bc6010"></a> `00bc6010` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc6014"></a> `00bc6014` | `ad f3 ff 97` | bl 0x00bc2ec8 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6018"></a> `00bc6018` | `40 17 00 b4` | cbz x0,0x00bc6300 | `CONDITIONAL_JUMP`
<a id="insn-00bc601c"></a> `00bc601c` | `99 22 40 a9` | ldp x25,x8,[x20] | `FALL_THROUGH`
<a id="insn-00bc6020"></a> `00bc6020` | `3f 03 08 eb` | cmp x25,x8 | `FALL_THROUGH`
<a id="insn-00bc6024"></a> `00bc6024` | `e9 03 19 aa` | mov x9,x25 | `FALL_THROUGH`
<a id="insn-00bc6028"></a> `00bc6028` | `e0 00 00 54` | b.eq 0x00bc6044 | `CONDITIONAL_JUMP`
<a id="insn-00bc602c"></a> `00bc602c` | `29 03 40 39` | ldrb w9,[x25] | `FALL_THROUGH`
<a id="insn-00bc6030"></a> `00bc6030` | `3f b9 01 71` | cmp w9,#0x6e | `FALL_THROUGH`
<a id="insn-00bc6034"></a> `00bc6034` | `e9 03 19 aa` | mov x9,x25 | `FALL_THROUGH`
<a id="insn-00bc6038"></a> `00bc6038` | `61 00 00 54` | b.ne 0x00bc6044 | `CONDITIONAL_JUMP`
<a id="insn-00bc603c"></a> `00bc603c` | `29 07 00 91` | add x9,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00bc6040"></a> `00bc6040` | `89 02 00 f9` | str x9,[x20] | `FALL_THROUGH`
<a id="insn-00bc6044"></a> `00bc6044` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bc6048"></a> `00bc6048` | `a0 15 00 54` | b.eq 0x00bc62fc | `CONDITIONAL_JUMP`
<a id="insn-00bc604c"></a> `00bc604c` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bc6050"></a> `00bc6050` | `4a e9 00 51` | sub w10,w10,#0x3a | `FALL_THROUGH`
<a id="insn-00bc6054"></a> `00bc6054` | `5f 29 00 31` | cmn w10,#0xa | `FALL_THROUGH`
<a id="insn-00bc6058"></a> `00bc6058` | `c2 00 00 54` | b.cs 0x00bc6070 | `CONDITIONAL_JUMP`
<a id="insn-00bc605c"></a> `00bc605c` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00bc6060"></a> `00bc6060` | `ea 03 1f aa` | mov x10,xzr | `FALL_THROUGH`
<a id="insn-00bc6064"></a> `00bc6064` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc6068"></a> `00bc6068` | `c1 01 00 54` | b.ne 0x00bc60a0 | `CONDITIONAL_JUMP`
<a id="insn-00bc606c"></a> `00bc606c` | `a4 00 00 14` | b 0x00bc62fc | `UNCONDITIONAL_JUMP`
<a id="insn-00bc6070"></a> `00bc6070` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bc6074"></a> `00bc6074` | `4a e9 00 51` | sub w10,w10,#0x3a | `FALL_THROUGH`
<a id="insn-00bc6078"></a> `00bc6078` | `5f 29 00 31` | cmn w10,#0xa | `FALL_THROUGH`
<a id="insn-00bc607c"></a> `00bc607c` | `c3 00 00 54` | b.cc 0x00bc6094 | `CONDITIONAL_JUMP`
<a id="insn-00bc6080"></a> `00bc6080` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bc6084"></a> `00bc6084` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc6088"></a> `00bc6088` | `89 02 00 f9` | str x9,[x20] | `FALL_THROUGH`
<a id="insn-00bc608c"></a> `00bc608c` | `21 ff ff 54` | b.ne 0x00bc6070 | `CONDITIONAL_JUMP`
<a id="insn-00bc6090"></a> `00bc6090` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00bc6094"></a> `00bc6094` | `2a 01 19 cb` | sub x10,x9,x25 | `FALL_THROUGH`
<a id="insn-00bc6098"></a> `00bc6098` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc609c"></a> `00bc609c` | `00 13 00 54` | b.eq 0x00bc62fc | `CONDITIONAL_JUMP`
<a id="insn-00bc60a0"></a> `00bc60a0` | `ea 03 00 a9` | stp x10,x0,[sp] | `FALL_THROUGH`
<a id="insn-00bc60a4"></a> `00bc60a4` | `8b 2a 41 a9` | ldp x11,x10,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bc60a8"></a> `00bc60a8` | `9c 02 00 b0` | adrp x28,0xc17000 | `FALL_THROUGH`
<a id="insn-00bc60ac"></a> `00bc60ac` | `9c 23 21 91` | add x28,x28,#0x848 | `FALL_THROUGH`
<a id="insn-00bc60b0"></a> `00bc60b0` | `96 a2 00 91` | add x22,x20,#0x28 | `FALL_THROUGH`
<a id="insn-00bc60b4"></a> `00bc60b4` | `15 01 80 52` | mov w21,#0x8 | `FALL_THROUGH`
<a id="insn-00bc60b8"></a> `00bc60b8` | `1b a8 80 52` | mov w27,#0x540 | `FALL_THROUGH`
<a id="insn-00bc60bc"></a> `00bc60bc` | `4a 01 0b cb` | sub x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bc60c0"></a> `00bc60c0` | `4a fd 43 93` | asr x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bc60c4"></a> `00bc60c4` | `ea 0b 00 f9` | str x10,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc60c8"></a> `00bc60c8` | `19 00 00 14` | b 0x00bc612c | `UNCONDITIONAL_JUMP`
<a id="insn-00bc60cc"></a> `00bc60cc` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bc60d0"></a> `00bc60d0` | `13 7c 00 a9` | stp x19,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bc60d4"></a> `00bc60d4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc60d8"></a> `00bc60d8` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc60dc"></a> `00bc60dc` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bc60e0"></a> `00bc60e0` | `7a 02 08 8b` | add x26,x19,x8 | `FALL_THROUGH`
<a id="insn-00bc60e4"></a> `00bc60e4` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc60e8"></a> `00bc60e8` | `5c 0f 01 f8` | str x28,[x26, #0x10]! | `FALL_THROUGH`
<a id="insn-00bc60ec"></a> `00bc60ec` | `48 93 40 78` | ldurh w8,[x26, #0x9] | `FALL_THROUGH`
<a id="insn-00bc60f0"></a> `00bc60f0` | `57 0b 00 f9` | str x23,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00bc60f4"></a> `00bc60f4` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bc60f8"></a> `00bc60f8` | `55 23 00 39` | strb w21,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-00bc60fc"></a> `00bc60fc` | `08 01 1b 2a` | orr w8,w8,w27 | `FALL_THROUGH`
<a id="insn-00bc6100"></a> `00bc6100` | `58 0f 00 f9` | str x24,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-00bc6104"></a> `00bc6104` | `48 93 00 78` | sturh w8,[x26, #0x9] | `FALL_THROUGH`
<a id="insn-00bc6108"></a> `00bc6108` | `93 a2 41 a9` | ldp x19,x8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bc610c"></a> `00bc610c` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00bc6110"></a> `00bc6110` | `a0 02 00 54` | b.eq 0x00bc6164 | `CONDITIONAL_JUMP`
<a id="insn-00bc6114"></a> `00bc6114` | `68 22 00 91` | add x8,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00bc6118"></a> `00bc6118` | `88 0e 00 f9` | str x8,[x20, #0x18] | `FALL_THROUGH`
<a id="insn-00bc611c"></a> `00bc611c` | `7a 02 00 f9` | str x26,[x19] | `FALL_THROUGH`
<a id="insn-00bc6120"></a> `00bc6120` | `89 22 40 a9` | ldp x9,x8,[x20] | `FALL_THROUGH`
<a id="insn-00bc6124"></a> `00bc6124` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc6128"></a> `00bc6128` | `a0 0e 00 54` | b.eq 0x00bc62fc | `CONDITIONAL_JUMP`
<a id="insn-00bc612c"></a> `00bc612c` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bc6130"></a> `00bc6130` | `5f 7d 01 71` | cmp w10,#0x5f | `FALL_THROUGH`
<a id="insn-00bc6134"></a> `00bc6134` | `21 07 00 54` | b.ne 0x00bc6218 | `CONDITIONAL_JUMP`
<a id="insn-00bc6138"></a> `00bc6138` | `37 05 00 91` | add x23,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bc613c"></a> `00bc613c` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00bc6140"></a> `00bc6140` | `97 02 00 f9` | str x23,[x20] | `FALL_THROUGH`
<a id="insn-00bc6144"></a> `00bc6144` | `a0 00 00 54` | b.eq 0x00bc6158 | `CONDITIONAL_JUMP`
<a id="insn-00bc6148"></a> `00bc6148` | `e9 02 40 39` | ldrb w9,[x23] | `FALL_THROUGH`
<a id="insn-00bc614c"></a> `00bc614c` | `29 e9 00 51` | sub w9,w9,#0x3a | `FALL_THROUGH`
<a id="insn-00bc6150"></a> `00bc6150` | `3f 29 00 31` | cmn w9,#0xa | `FALL_THROUGH`
<a id="insn-00bc6154"></a> `00bc6154` | `a2 01 00 54` | b.cs 0x00bc6188 | `CONDITIONAL_JUMP`
<a id="insn-00bc6158"></a> `00bc6158` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bc615c"></a> `00bc615c` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00bc6160"></a> `00bc6160` | `15 00 00 14` | b 0x00bc61b4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc6164"></a> `00bc6164` | `80 0a 40 f9` | ldr x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bc6168"></a> `00bc6168` | `77 02 00 cb` | sub x23,x19,x0 | `FALL_THROUGH`
<a id="insn-00bc616c"></a> `00bc616c` | `1f 00 16 eb` | cmp x0,x22 | `FALL_THROUGH`
<a id="insn-00bc6170"></a> `00bc6170` | `e1 fa 7f d3` | lsl x1,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bc6174"></a> `00bc6174` | `20 03 00 54` | b.eq 0x00bc61d8 | `CONDITIONAL_JUMP`
<a id="insn-00bc6178"></a> `00bc6178` | `22 5c 00 94` | bl 0x00bdd200 | `UNCONDITIONAL_CALL`
<a id="insn-00bc617c"></a> `00bc617c` | `80 0a 00 f9` | str x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bc6180"></a> `00bc6180` | `20 04 00 b5` | cbnz x0,0x00bc6204 | `CONDITIONAL_JUMP`
<a id="insn-00bc6184"></a> `00bc6184` | `69 00 00 14` | b 0x00bc6328 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc6188"></a> `00bc6188` | `e9 03 17 aa` | mov x9,x23 | `FALL_THROUGH`
<a id="insn-00bc618c"></a> `00bc618c` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bc6190"></a> `00bc6190` | `4a e9 00 51` | sub w10,w10,#0x3a | `FALL_THROUGH`
<a id="insn-00bc6194"></a> `00bc6194` | `5f 29 00 31` | cmn w10,#0xa | `FALL_THROUGH`
<a id="insn-00bc6198"></a> `00bc6198` | `c3 00 00 54` | b.cc 0x00bc61b0 | `CONDITIONAL_JUMP`
<a id="insn-00bc619c"></a> `00bc619c` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bc61a0"></a> `00bc61a0` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc61a4"></a> `00bc61a4` | `89 02 00 f9` | str x9,[x20] | `FALL_THROUGH`
<a id="insn-00bc61a8"></a> `00bc61a8` | `21 ff ff 54` | b.ne 0x00bc618c | `CONDITIONAL_JUMP`
<a id="insn-00bc61ac"></a> `00bc61ac` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00bc61b0"></a> `00bc61b0` | `38 01 17 cb` | sub x24,x9,x23 | `FALL_THROUGH`
<a id="insn-00bc61b4"></a> `00bc61b4` | `93 9a 49 f9` | ldr x19,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc61b8"></a> `00bc61b8` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc61bc"></a> `00bc61bc` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bc61c0"></a> `00bc61c0` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bc61c4"></a> `00bc61c4` | `c8 f8 ff 54` | b.hi 0x00bc60dc | `CONDITIONAL_JUMP`
<a id="insn-00bc61c8"></a> `00bc61c8` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bc61cc"></a> `00bc61cc` | `ed 5b 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bc61d0"></a> `00bc61d0` | `e0 f7 ff b5` | cbnz x0,0x00bc60cc | `CONDITIONAL_JUMP`
<a id="insn-00bc61d4"></a> `00bc61d4` | `54 00 00 14` | b 0x00bc6324 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc61d8"></a> `00bc61d8` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bc61dc"></a> `00bc61dc` | `e9 5b 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bc61e0"></a> `00bc61e0` | `60 0a 00 b4` | cbz x0,0x00bc632c | `CONDITIONAL_JUMP`
<a id="insn-00bc61e4"></a> `00bc61e4` | `7f 02 16 eb` | cmp x19,x22 | `FALL_THROUGH`
<a id="insn-00bc61e8"></a> `00bc61e8` | `c0 00 00 54` | b.eq 0x00bc6200 | `CONDITIONAL_JUMP`
<a id="insn-00bc61ec"></a> `00bc61ec` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bc61f0"></a> `00bc61f0` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00bc61f4"></a> `00bc61f4` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bc61f8"></a> `00bc61f8` | `da 53 00 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00bc61fc"></a> `00bc61fc` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bc6200"></a> `00bc6200` | `80 0a 00 f9` | str x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bc6204"></a> `00bc6204` | `e8 fe 42 93` | asr x8,x23,#0x2 | `FALL_THROUGH`
<a id="insn-00bc6208"></a> `00bc6208` | `13 00 17 8b` | add x19,x0,x23 | `FALL_THROUGH`
<a id="insn-00bc620c"></a> `00bc620c` | `08 0c 08 8b` | add x8,x0,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bc6210"></a> `00bc6210` | `88 12 00 f9` | str x8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00bc6214"></a> `00bc6214` | `c0 ff ff 17` | b 0x00bc6114 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc6218"></a> `00bc6218` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc621c"></a> `00bc621c` | `40 01 00 54` | b.eq 0x00bc6244 | `CONDITIONAL_JUMP`
<a id="insn-00bc6220"></a> `00bc6220` | `2a 01 40 39` | ldrb w10,[x9] | `FALL_THROUGH`
<a id="insn-00bc6224"></a> `00bc6224` | `5f c1 01 71` | cmp w10,#0x70 | `FALL_THROUGH`
<a id="insn-00bc6228"></a> `00bc6228` | `e1 00 00 54` | b.ne 0x00bc6244 | `CONDITIONAL_JUMP`
<a id="insn-00bc622c"></a> `00bc622c` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bc6230"></a> `00bc6230` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bc6234"></a> `00bc6234` | `89 02 00 f9` | str x9,[x20] | `FALL_THROUGH`
<a id="insn-00bc6238"></a> `00bc6238` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc623c"></a> `00bc623c` | `a1 00 00 54` | b.ne 0x00bc6250 | `CONDITIONAL_JUMP`
<a id="insn-00bc6240"></a> `00bc6240` | `2f 00 00 14` | b 0x00bc62fc | `UNCONDITIONAL_JUMP`
<a id="insn-00bc6244"></a> `00bc6244` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-00bc6248"></a> `00bc6248` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc624c"></a> `00bc624c` | `80 05 00 54` | b.eq 0x00bc62fc | `CONDITIONAL_JUMP`
<a id="insn-00bc6250"></a> `00bc6250` | `28 01 40 39` | ldrb w8,[x9] | `FALL_THROUGH`
<a id="insn-00bc6254"></a> `00bc6254` | `1f 15 01 71` | cmp w8,#0x45 | `FALL_THROUGH`
<a id="insn-00bc6258"></a> `00bc6258` | `21 05 00 54` | b.ne 0x00bc62fc | `CONDITIONAL_JUMP`
<a id="insn-00bc625c"></a> `00bc625c` | `e1 0b 40 f9` | ldr x1,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc6260"></a> `00bc6260` | `28 05 00 91` | add x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bc6264"></a> `00bc6264` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc6268"></a> `00bc6268` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00bc626c"></a> `00bc626c` | `30 e7 ff 97` | bl 0x00bbff2c | `UNCONDITIONAL_CALL`
<a id="insn-00bc6270"></a> `00bc6270` | `98 9a 49 f9` | ldr x24,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc6274"></a> `00bc6274` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bc6278"></a> `00bc6278` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bc627c"></a> `00bc627c` | `08 07 40 f9` | ldr x8,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bc6280"></a> `00bc6280` | `09 81 3e d1` | sub x9,x8,#0xfa0 | `FALL_THROUGH`
<a id="insn-00bc6284"></a> `00bc6284` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bc6288"></a> `00bc6288` | `08 01 00 54` | b.hi 0x00bc62a8 | `CONDITIONAL_JUMP`
<a id="insn-00bc628c"></a> `00bc628c` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bc6290"></a> `00bc6290` | `bc 5b 00 94` | bl 0x00bdd180 | `UNCONDITIONAL_CALL`
<a id="insn-00bc6294"></a> `00bc6294` | `80 04 00 b4` | cbz x0,0x00bc6324 | `CONDITIONAL_JUMP`
<a id="insn-00bc6298"></a> `00bc6298` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bc629c"></a> `00bc629c` | `18 7c 00 a9` | stp x24,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bc62a0"></a> `00bc62a0` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bc62a4"></a> `00bc62a4` | `80 9a 09 f9` | str x0,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc62a8"></a> `00bc62a8` | `0a 41 01 91` | add x10,x8,#0x50 | `FALL_THROUGH`
<a id="insn-00bc62ac"></a> `00bc62ac` | `00 03 08 8b` | add x0,x24,x8 | `FALL_THROUGH`
<a id="insn-00bc62b0"></a> `00bc62b0` | `88 02 00 d0` | adrp x8,0xc18000 | `FALL_THROUGH`
<a id="insn-00bc62b4"></a> `00bc62b4` | `08 21 3a 91` | add x8,x8,#0xe88 | `FALL_THROUGH`
<a id="insn-00bc62b8"></a> `00bc62b8` | `0a 07 00 f9` | str x10,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00bc62bc"></a> `00bc62bc` | `6a 07 80 52` | mov w10,#0x3b | `FALL_THROUGH`
<a id="insn-00bc62c0"></a> `00bc62c0` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bc62c4"></a> `00bc62c4` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bc62c8"></a> `00bc62c8` | `0a 20 00 39` | strb w10,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bc62cc"></a> `00bc62cc` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bc62d0"></a> `00bc62d0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bc62d4"></a> `00bc62d4` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bc62d8"></a> `00bc62d8` | `eb 07 40 f9` | ldr x11,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bc62dc"></a> `00bc62dc` | `15 58 03 a9` | stp x21,x22,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00bc62e0"></a> `00bc62e0` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bc62e4"></a> `00bc62e4` | `17 00 01 39` | strb w23,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bc62e8"></a> `00bc62e8` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bc62ec"></a> `00bc62ec` | `e8 03 40 f9` | ldr x8,[sp] | `FALL_THROUGH`
<a id="insn-00bc62f0"></a> `00bc62f0` | `09 2c 01 a9` | stp x9,x11,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bc62f4"></a> `00bc62f4` | `19 20 02 a9` | stp x25,x8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bc62f8"></a> `00bc62f8` | `02 00 00 14` | b 0x00bc6300 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc62fc"></a> `00bc62fc` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bc6300"></a> `00bc6300` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bc6304"></a> `00bc6304` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bc6308"></a> `00bc6308` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bc630c"></a> `00bc630c` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bc6310"></a> `00bc6310` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc6314"></a> `00bc6314` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc6318"></a> `00bc6318` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bc631c"></a> `00bc631c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bc6320"></a> `00bc6320` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc6324"></a> `00bc6324` | `97 53 00 94` | bl 0x00bdb180 | `CALL_TERMINATOR`
<a id="insn-00bc6328"></a> `00bc6328` | `d2 5f 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00bc632c"></a> `00bc632c` | `d1 5f 00 94` | bl 0x00bde270 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc5fdc`](#insn-00bc5fdc) 範囲 `[['00bc5fdc', '00bc600b']]`
  - `CONDITIONAL_JUMP` [`00bc6008`](#insn-00bc6008) → [`00bc6300`](#insn-00bc6300)
  - `FALL_THROUGH` [`00bc6008`](#insn-00bc6008) → [`00bc600c`](#insn-00bc600c)
- ブロック [`00bc600c`](#insn-00bc600c) 範囲 `[['00bc600c', '00bc601b']]`
  - `CONDITIONAL_JUMP` [`00bc6018`](#insn-00bc6018) → [`00bc6300`](#insn-00bc6300)
  - `FALL_THROUGH` [`00bc6018`](#insn-00bc6018) → [`00bc601c`](#insn-00bc601c)
- ブロック [`00bc601c`](#insn-00bc601c) 範囲 `[['00bc601c', '00bc602b']]`
  - `CONDITIONAL_JUMP` [`00bc6028`](#insn-00bc6028) → [`00bc6044`](#insn-00bc6044)
  - `FALL_THROUGH` [`00bc6028`](#insn-00bc6028) → [`00bc602c`](#insn-00bc602c)
- ブロック [`00bc602c`](#insn-00bc602c) 範囲 `[['00bc602c', '00bc603b']]`
  - `CONDITIONAL_JUMP` [`00bc6038`](#insn-00bc6038) → [`00bc6044`](#insn-00bc6044)
  - `FALL_THROUGH` [`00bc6038`](#insn-00bc6038) → [`00bc603c`](#insn-00bc603c)
- ブロック [`00bc603c`](#insn-00bc603c) 範囲 `[['00bc603c', '00bc6043']]`
  - `FALL_THROUGH` [`00bc6040`](#insn-00bc6040) → [`00bc6044`](#insn-00bc6044)
- ブロック [`00bc6044`](#insn-00bc6044) 範囲 `[['00bc6044', '00bc604b']]`
  - `CONDITIONAL_JUMP` [`00bc6048`](#insn-00bc6048) → [`00bc62fc`](#insn-00bc62fc)
  - `FALL_THROUGH` [`00bc6048`](#insn-00bc6048) → [`00bc604c`](#insn-00bc604c)
- ブロック [`00bc604c`](#insn-00bc604c) 範囲 `[['00bc604c', '00bc605b']]`
  - `CONDITIONAL_JUMP` [`00bc6058`](#insn-00bc6058) → [`00bc6070`](#insn-00bc6070)
  - `FALL_THROUGH` [`00bc6058`](#insn-00bc6058) → [`00bc605c`](#insn-00bc605c)
- ブロック [`00bc605c`](#insn-00bc605c) 範囲 `[['00bc605c', '00bc606b']]`
  - `CONDITIONAL_JUMP` [`00bc6068`](#insn-00bc6068) → [`00bc60a0`](#insn-00bc60a0)
  - `FALL_THROUGH` [`00bc6068`](#insn-00bc6068) → [`00bc606c`](#insn-00bc606c)
- ブロック [`00bc606c`](#insn-00bc606c) 範囲 `[['00bc606c', '00bc606f']]`
  - `UNCONDITIONAL_JUMP` [`00bc606c`](#insn-00bc606c) → [`00bc62fc`](#insn-00bc62fc)
- ブロック [`00bc6070`](#insn-00bc6070) 範囲 `[['00bc6070', '00bc607f']]`
  - `CONDITIONAL_JUMP` [`00bc607c`](#insn-00bc607c) → [`00bc6094`](#insn-00bc6094)
  - `FALL_THROUGH` [`00bc607c`](#insn-00bc607c) → [`00bc6080`](#insn-00bc6080)
- ブロック [`00bc6080`](#insn-00bc6080) 範囲 `[['00bc6080', '00bc6083']]`
  - `FALL_THROUGH` [`00bc6080`](#insn-00bc6080) → [`00bc6084`](#insn-00bc6084)
- ブロック [`00bc6084`](#insn-00bc6084) 範囲 `[['00bc6084', '00bc608f']]`
  - `CONDITIONAL_JUMP` [`00bc608c`](#insn-00bc608c) → [`00bc6070`](#insn-00bc6070)
  - `FALL_THROUGH` [`00bc608c`](#insn-00bc608c) → [`00bc6090`](#insn-00bc6090)
- ブロック [`00bc6090`](#insn-00bc6090) 範囲 `[['00bc6090', '00bc6093']]`
  - `FALL_THROUGH` [`00bc6090`](#insn-00bc6090) → [`00bc6094`](#insn-00bc6094)
- ブロック [`00bc6094`](#insn-00bc6094) 範囲 `[['00bc6094', '00bc609f']]`
  - `CONDITIONAL_JUMP` [`00bc609c`](#insn-00bc609c) → [`00bc62fc`](#insn-00bc62fc)
  - `FALL_THROUGH` [`00bc609c`](#insn-00bc609c) → [`00bc60a0`](#insn-00bc60a0)
- ブロック [`00bc60a0`](#insn-00bc60a0) 範囲 `[['00bc60a0', '00bc60c7']]`
  - `FALL_THROUGH` [`00bc60c4`](#insn-00bc60c4) → [`00bc60c8`](#insn-00bc60c8)
- ブロック [`00bc60c8`](#insn-00bc60c8) 範囲 `[['00bc60c8', '00bc60cb']]`
  - `UNCONDITIONAL_JUMP` [`00bc60c8`](#insn-00bc60c8) → [`00bc612c`](#insn-00bc612c)
- ブロック [`00bc60cc`](#insn-00bc60cc) 範囲 `[['00bc60cc', '00bc60d3']]`
  - `FALL_THROUGH` [`00bc60d0`](#insn-00bc60d0) → [`00bc60d4`](#insn-00bc60d4)
- ブロック [`00bc60d4`](#insn-00bc60d4) 範囲 `[['00bc60d4', '00bc60db']]`
  - `FALL_THROUGH` [`00bc60d8`](#insn-00bc60d8) → [`00bc60dc`](#insn-00bc60dc)
- ブロック [`00bc60dc`](#insn-00bc60dc) 範囲 `[['00bc60dc', '00bc60e3']]`
  - `FALL_THROUGH` [`00bc60e0`](#insn-00bc60e0) → [`00bc60e4`](#insn-00bc60e4)
- ブロック [`00bc60e4`](#insn-00bc60e4) 範囲 `[['00bc60e4', '00bc6113']]`
  - `CONDITIONAL_JUMP` [`00bc6110`](#insn-00bc6110) → [`00bc6164`](#insn-00bc6164)
  - `FALL_THROUGH` [`00bc6110`](#insn-00bc6110) → [`00bc6114`](#insn-00bc6114)
- ブロック [`00bc6114`](#insn-00bc6114) 範囲 `[['00bc6114', '00bc612b']]`
  - `CONDITIONAL_JUMP` [`00bc6128`](#insn-00bc6128) → [`00bc62fc`](#insn-00bc62fc)
  - `FALL_THROUGH` [`00bc6128`](#insn-00bc6128) → [`00bc612c`](#insn-00bc612c)
- ブロック [`00bc612c`](#insn-00bc612c) 範囲 `[['00bc612c', '00bc6137']]`
  - `CONDITIONAL_JUMP` [`00bc6134`](#insn-00bc6134) → [`00bc6218`](#insn-00bc6218)
  - `FALL_THROUGH` [`00bc6134`](#insn-00bc6134) → [`00bc6138`](#insn-00bc6138)
- ブロック [`00bc6138`](#insn-00bc6138) 範囲 `[['00bc6138', '00bc6147']]`
  - `CONDITIONAL_JUMP` [`00bc6144`](#insn-00bc6144) → [`00bc6158`](#insn-00bc6158)
  - `FALL_THROUGH` [`00bc6144`](#insn-00bc6144) → [`00bc6148`](#insn-00bc6148)
- ブロック [`00bc6148`](#insn-00bc6148) 範囲 `[['00bc6148', '00bc6157']]`
  - `CONDITIONAL_JUMP` [`00bc6154`](#insn-00bc6154) → [`00bc6188`](#insn-00bc6188)
  - `FALL_THROUGH` [`00bc6154`](#insn-00bc6154) → [`00bc6158`](#insn-00bc6158)
- ブロック [`00bc6158`](#insn-00bc6158) 範囲 `[['00bc6158', '00bc6163']]`
  - `UNCONDITIONAL_JUMP` [`00bc6160`](#insn-00bc6160) → [`00bc61b4`](#insn-00bc61b4)
- ブロック [`00bc6164`](#insn-00bc6164) 範囲 `[['00bc6164', '00bc6177']]`
  - `CONDITIONAL_JUMP` [`00bc6174`](#insn-00bc6174) → [`00bc61d8`](#insn-00bc61d8)
  - `FALL_THROUGH` [`00bc6174`](#insn-00bc6174) → [`00bc6178`](#insn-00bc6178)
- ブロック [`00bc6178`](#insn-00bc6178) 範囲 `[['00bc6178', '00bc6183']]`
  - `CONDITIONAL_JUMP` [`00bc6180`](#insn-00bc6180) → [`00bc6204`](#insn-00bc6204)
  - `FALL_THROUGH` [`00bc6180`](#insn-00bc6180) → [`00bc6184`](#insn-00bc6184)
- ブロック [`00bc6184`](#insn-00bc6184) 範囲 `[['00bc6184', '00bc6187']]`
  - `UNCONDITIONAL_JUMP` [`00bc6184`](#insn-00bc6184) → [`00bc6328`](#insn-00bc6328)
- ブロック [`00bc6188`](#insn-00bc6188) 範囲 `[['00bc6188', '00bc618b']]`
  - `FALL_THROUGH` [`00bc6188`](#insn-00bc6188) → [`00bc618c`](#insn-00bc618c)
- ブロック [`00bc618c`](#insn-00bc618c) 範囲 `[['00bc618c', '00bc619b']]`
  - `CONDITIONAL_JUMP` [`00bc6198`](#insn-00bc6198) → [`00bc61b0`](#insn-00bc61b0)
  - `FALL_THROUGH` [`00bc6198`](#insn-00bc6198) → [`00bc619c`](#insn-00bc619c)
- ブロック [`00bc619c`](#insn-00bc619c) 範囲 `[['00bc619c', '00bc61ab']]`
  - `CONDITIONAL_JUMP` [`00bc61a8`](#insn-00bc61a8) → [`00bc618c`](#insn-00bc618c)
  - `FALL_THROUGH` [`00bc61a8`](#insn-00bc61a8) → [`00bc61ac`](#insn-00bc61ac)
- ブロック [`00bc61ac`](#insn-00bc61ac) 範囲 `[['00bc61ac', '00bc61af']]`
  - `FALL_THROUGH` [`00bc61ac`](#insn-00bc61ac) → [`00bc61b0`](#insn-00bc61b0)
- ブロック [`00bc61b0`](#insn-00bc61b0) 範囲 `[['00bc61b0', '00bc61b3']]`
  - `FALL_THROUGH` [`00bc61b0`](#insn-00bc61b0) → [`00bc61b4`](#insn-00bc61b4)
- ブロック [`00bc61b4`](#insn-00bc61b4) 範囲 `[['00bc61b4', '00bc61bb']]`
  - `FALL_THROUGH` [`00bc61b8`](#insn-00bc61b8) → [`00bc61bc`](#insn-00bc61bc)
- ブロック [`00bc61bc`](#insn-00bc61bc) 範囲 `[['00bc61bc', '00bc61c7']]`
  - `CONDITIONAL_JUMP` [`00bc61c4`](#insn-00bc61c4) → [`00bc60dc`](#insn-00bc60dc)
  - `FALL_THROUGH` [`00bc61c4`](#insn-00bc61c4) → [`00bc61c8`](#insn-00bc61c8)
- ブロック [`00bc61c8`](#insn-00bc61c8) 範囲 `[['00bc61c8', '00bc61d3']]`
  - `CONDITIONAL_JUMP` [`00bc61d0`](#insn-00bc61d0) → [`00bc60cc`](#insn-00bc60cc)
  - `FALL_THROUGH` [`00bc61d0`](#insn-00bc61d0) → [`00bc61d4`](#insn-00bc61d4)
- ブロック [`00bc61d4`](#insn-00bc61d4) 範囲 `[['00bc61d4', '00bc61d7']]`
  - `UNCONDITIONAL_JUMP` [`00bc61d4`](#insn-00bc61d4) → [`00bc6324`](#insn-00bc6324)
- ブロック [`00bc61d8`](#insn-00bc61d8) 範囲 `[['00bc61d8', '00bc61df']]`
  - `FALL_THROUGH` [`00bc61dc`](#insn-00bc61dc) → [`00bc61e0`](#insn-00bc61e0)
- ブロック [`00bc61e0`](#insn-00bc61e0) 範囲 `[['00bc61e0', '00bc61e3']]`
  - `CONDITIONAL_JUMP` [`00bc61e0`](#insn-00bc61e0) → [`00bc632c`](#insn-00bc632c)
  - `FALL_THROUGH` [`00bc61e0`](#insn-00bc61e0) → [`00bc61e4`](#insn-00bc61e4)
- ブロック [`00bc61e4`](#insn-00bc61e4) 範囲 `[['00bc61e4', '00bc61eb']]`
  - `CONDITIONAL_JUMP` [`00bc61e8`](#insn-00bc61e8) → [`00bc6200`](#insn-00bc6200)
  - `FALL_THROUGH` [`00bc61e8`](#insn-00bc61e8) → [`00bc61ec`](#insn-00bc61ec)
- ブロック [`00bc61ec`](#insn-00bc61ec) 範囲 `[['00bc61ec', '00bc61ff']]`
  - `FALL_THROUGH` [`00bc61fc`](#insn-00bc61fc) → [`00bc6200`](#insn-00bc6200)
- ブロック [`00bc6200`](#insn-00bc6200) 範囲 `[['00bc6200', '00bc6203']]`
  - `FALL_THROUGH` [`00bc6200`](#insn-00bc6200) → [`00bc6204`](#insn-00bc6204)
- ブロック [`00bc6204`](#insn-00bc6204) 範囲 `[['00bc6204', '00bc6217']]`
  - `UNCONDITIONAL_JUMP` [`00bc6214`](#insn-00bc6214) → [`00bc6114`](#insn-00bc6114)
- ブロック [`00bc6218`](#insn-00bc6218) 範囲 `[['00bc6218', '00bc621f']]`
  - `CONDITIONAL_JUMP` [`00bc621c`](#insn-00bc621c) → [`00bc6244`](#insn-00bc6244)
  - `FALL_THROUGH` [`00bc621c`](#insn-00bc621c) → [`00bc6220`](#insn-00bc6220)
- ブロック [`00bc6220`](#insn-00bc6220) 範囲 `[['00bc6220', '00bc6227']]`
  - `FALL_THROUGH` [`00bc6224`](#insn-00bc6224) → [`00bc6228`](#insn-00bc6228)
- ブロック [`00bc6228`](#insn-00bc6228) 範囲 `[['00bc6228', '00bc622b']]`
  - `CONDITIONAL_JUMP` [`00bc6228`](#insn-00bc6228) → [`00bc6244`](#insn-00bc6244)
  - `FALL_THROUGH` [`00bc6228`](#insn-00bc6228) → [`00bc622c`](#insn-00bc622c)
- ブロック [`00bc622c`](#insn-00bc622c) 範囲 `[['00bc622c', '00bc6233']]`
  - `FALL_THROUGH` [`00bc6230`](#insn-00bc6230) → [`00bc6234`](#insn-00bc6234)
- ブロック [`00bc6234`](#insn-00bc6234) 範囲 `[['00bc6234', '00bc623f']]`
  - `CONDITIONAL_JUMP` [`00bc623c`](#insn-00bc623c) → [`00bc6250`](#insn-00bc6250)
  - `FALL_THROUGH` [`00bc623c`](#insn-00bc623c) → [`00bc6240`](#insn-00bc6240)
- ブロック [`00bc6240`](#insn-00bc6240) 範囲 `[['00bc6240', '00bc6243']]`
  - `UNCONDITIONAL_JUMP` [`00bc6240`](#insn-00bc6240) → [`00bc62fc`](#insn-00bc62fc)
- ブロック [`00bc6244`](#insn-00bc6244) 範囲 `[['00bc6244', '00bc624f']]`
  - `CONDITIONAL_JUMP` [`00bc624c`](#insn-00bc624c) → [`00bc62fc`](#insn-00bc62fc)
  - `FALL_THROUGH` [`00bc624c`](#insn-00bc624c) → [`00bc6250`](#insn-00bc6250)
- ブロック [`00bc6250`](#insn-00bc6250) 範囲 `[['00bc6250', '00bc625b']]`
  - `CONDITIONAL_JUMP` [`00bc6258`](#insn-00bc6258) → [`00bc62fc`](#insn-00bc62fc)
  - `FALL_THROUGH` [`00bc6258`](#insn-00bc6258) → [`00bc625c`](#insn-00bc625c)
- ブロック [`00bc625c`](#insn-00bc625c) 範囲 `[['00bc625c', '00bc628b']]`
  - `CONDITIONAL_JUMP` [`00bc6288`](#insn-00bc6288) → [`00bc62a8`](#insn-00bc62a8)
  - `FALL_THROUGH` [`00bc6288`](#insn-00bc6288) → [`00bc628c`](#insn-00bc628c)
- ブロック [`00bc628c`](#insn-00bc628c) 範囲 `[['00bc628c', '00bc6297']]`
  - `CONDITIONAL_JUMP` [`00bc6294`](#insn-00bc6294) → [`00bc6324`](#insn-00bc6324)
  - `FALL_THROUGH` [`00bc6294`](#insn-00bc6294) → [`00bc6298`](#insn-00bc6298)
- ブロック [`00bc6298`](#insn-00bc6298) 範囲 `[['00bc6298', '00bc62a7']]`
  - `FALL_THROUGH` [`00bc62a4`](#insn-00bc62a4) → [`00bc62a8`](#insn-00bc62a8)
- ブロック [`00bc62a8`](#insn-00bc62a8) 範囲 `[['00bc62a8', '00bc62e3']]`
  - `FALL_THROUGH` [`00bc62e0`](#insn-00bc62e0) → [`00bc62e4`](#insn-00bc62e4)
- ブロック [`00bc62e4`](#insn-00bc62e4) 範囲 `[['00bc62e4', '00bc62fb']]`
  - `UNCONDITIONAL_JUMP` [`00bc62f8`](#insn-00bc62f8) → [`00bc6300`](#insn-00bc6300)
- ブロック [`00bc62fc`](#insn-00bc62fc) 範囲 `[['00bc62fc', '00bc62ff']]`
  - `FALL_THROUGH` [`00bc62fc`](#insn-00bc62fc) → [`00bc6300`](#insn-00bc6300)
- ブロック [`00bc6300`](#insn-00bc6300) 範囲 `[['00bc6300', '00bc631b']]`
  - `FALL_THROUGH` [`00bc6318`](#insn-00bc6318) → [`00bc631c`](#insn-00bc631c)
- ブロック [`00bc631c`](#insn-00bc631c) 範囲 `[['00bc631c', '00bc6323']]`
- ブロック [`00bc6324`](#insn-00bc6324) 範囲 `[['00bc6324', '00bc6327']]`
- ブロック [`00bc6328`](#insn-00bc6328) 範囲 `[['00bc6328', '00bc632b']]`
- ブロック [`00bc632c`](#insn-00bc632c) 範囲 `[['00bc632c', '00bc632f']]`

## 命令位置別の参照

- [`00bc5fe4`](#insn-00bc5fe4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5fe8`](#insn-00bc5fe8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5fec`](#insn-00bc5fec) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5ff0`](#insn-00bc5ff0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5ff4`](#insn-00bc5ff4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc5ff8`](#insn-00bc5ff8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6004`](#insn-00bc6004) → [`00bbde18`](../00bbd/00bbde18.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde18` · 推定シンボル `None` · 推定型 `None`
- [`00bc6008`](#insn-00bc6008) → [`00bc6300`](#insn-00bc6300) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc600c`](#insn-00bc600c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6014`](#insn-00bc6014) → [`00bc2ec8`](../00bc2/00bc2ec8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2ec8` · 推定シンボル `None` · 推定型 `None`
- [`00bc6018`](#insn-00bc6018) → [`00bc6300`](#insn-00bc6300) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6028`](#insn-00bc6028) → [`00bc6044`](#insn-00bc6044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6038`](#insn-00bc6038) → [`00bc6044`](#insn-00bc6044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6048`](#insn-00bc6048) → [`00bc62fc`](#insn-00bc62fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6058`](#insn-00bc6058) → [`00bc6070`](#insn-00bc6070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6068`](#insn-00bc6068) → [`00bc60a0`](#insn-00bc60a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc606c`](#insn-00bc606c) → [`00bc62fc`](#insn-00bc62fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc607c`](#insn-00bc607c) → [`00bc6094`](#insn-00bc6094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc608c`](#insn-00bc608c) → [`00bc6070`](#insn-00bc6070) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc609c`](#insn-00bc609c) → [`00bc62fc`](#insn-00bc62fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc60a0`](#insn-00bc60a0) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc60c4`](#insn-00bc60c4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc60c8`](#insn-00bc60c8) → [`00bc612c`](#insn-00bc612c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc60e8`](#insn-00bc60e8) → `00c17848`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bc6110`](#insn-00bc6110) → [`00bc6164`](#insn-00bc6164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6128`](#insn-00bc6128) → [`00bc62fc`](#insn-00bc62fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6134`](#insn-00bc6134) → [`00bc6218`](#insn-00bc6218) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6144`](#insn-00bc6144) → [`00bc6158`](#insn-00bc6158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6154`](#insn-00bc6154) → [`00bc6188`](#insn-00bc6188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6160`](#insn-00bc6160) → [`00bc61b4`](#insn-00bc61b4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6174`](#insn-00bc6174) → [`00bc61d8`](#insn-00bc61d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6178`](#insn-00bc6178) → [`00bdd200`](../00bdd/00bdd200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd200` · 推定シンボル `None` · 推定型 `None`
- [`00bc6180`](#insn-00bc6180) → [`00bc6204`](#insn-00bc6204) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6184`](#insn-00bc6184) → [`00bc6328`](#insn-00bc6328) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6198`](#insn-00bc6198) → [`00bc61b0`](#insn-00bc61b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc61a8`](#insn-00bc61a8) → [`00bc618c`](#insn-00bc618c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc61c4`](#insn-00bc61c4) → [`00bc60dc`](#insn-00bc60dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc61cc`](#insn-00bc61cc) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bc61d0`](#insn-00bc61d0) → [`00bc60cc`](#insn-00bc60cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc61d4`](#insn-00bc61d4) → [`00bc6324`](#insn-00bc6324) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc61dc`](#insn-00bc61dc) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bc61e0`](#insn-00bc61e0) → [`00bc632c`](#insn-00bc632c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc61e8`](#insn-00bc61e8) → [`00bc6200`](#insn-00bc6200) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc61f8`](#insn-00bc61f8) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00bc6214`](#insn-00bc6214) → [`00bc6114`](#insn-00bc6114) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc621c`](#insn-00bc621c) → [`00bc6244`](#insn-00bc6244) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6228`](#insn-00bc6228) → [`00bc6244`](#insn-00bc6244) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc623c`](#insn-00bc623c) → [`00bc6250`](#insn-00bc6250) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6240`](#insn-00bc6240) → [`00bc62fc`](#insn-00bc62fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc624c`](#insn-00bc624c) → [`00bc62fc`](#insn-00bc62fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6258`](#insn-00bc6258) → [`00bc62fc`](#insn-00bc62fc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc625c`](#insn-00bc625c) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc626c`](#insn-00bc626c) → [`00bbff2c`](../00bbf/00bbff2c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbff2c` · 推定シンボル `None` · 推定型 `None`
- [`00bc6288`](#insn-00bc6288) → [`00bc62a8`](#insn-00bc62a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6290`](#insn-00bc6290) → [`00bdd180`](../00bdd/00bdd180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd180` · 推定シンボル `None` · 推定型 `None`
- [`00bc6294`](#insn-00bc6294) → [`00bc6324`](#insn-00bc6324) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc62c0`](#insn-00bc62c0) → `00c18e88`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bc62d0`](#insn-00bc62d0) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc62d8`](#insn-00bc62d8) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc62ec`](#insn-00bc62ec) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc62f8`](#insn-00bc62f8) → [`00bc6300`](#insn-00bc6300) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6300`](#insn-00bc6300) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6304`](#insn-00bc6304) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6308`](#insn-00bc6308) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc630c`](#insn-00bc630c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6310`](#insn-00bc6310) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6314`](#insn-00bc6314) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc6324`](#insn-00bc6324) → [`00bdb180`](../00bdb/00bdb180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb180` · 推定シンボル `None` · 推定型 `None`
- [`00bc6328`](#insn-00bc6328) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00bc632c`](#insn-00bc632c) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc5fe4`](#insn-00bc5fe4)

~~~json
{
  "source": "00bc5fe4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5fe8`](#insn-00bc5fe8)

~~~json
{
  "source": "00bc5fe8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5fec`](#insn-00bc5fec)

~~~json
{
  "source": "00bc5fec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5ff0`](#insn-00bc5ff0)

~~~json
{
  "source": "00bc5ff0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5ff4`](#insn-00bc5ff4)

~~~json
{
  "source": "00bc5ff4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc5ff8`](#insn-00bc5ff8)

~~~json
{
  "source": "00bc5ff8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6004`](#insn-00bc6004)

~~~json
{
  "source": "00bc6004",
  "target": "00bbde18",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6008`](#insn-00bc6008)

~~~json
{
  "source": "00bc6008",
  "target": "00bc6300",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc600c`](#insn-00bc600c)

~~~json
{
  "source": "00bc600c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6014`](#insn-00bc6014)

~~~json
{
  "source": "00bc6014",
  "target": "00bc2ec8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6018`](#insn-00bc6018)

~~~json
{
  "source": "00bc6018",
  "target": "00bc6300",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6028`](#insn-00bc6028)

~~~json
{
  "source": "00bc6028",
  "target": "00bc6044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6038`](#insn-00bc6038)

~~~json
{
  "source": "00bc6038",
  "target": "00bc6044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6048`](#insn-00bc6048)

~~~json
{
  "source": "00bc6048",
  "target": "00bc62fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6058`](#insn-00bc6058)

~~~json
{
  "source": "00bc6058",
  "target": "00bc6070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6068`](#insn-00bc6068)

~~~json
{
  "source": "00bc6068",
  "target": "00bc60a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc606c`](#insn-00bc606c)

~~~json
{
  "source": "00bc606c",
  "target": "00bc62fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc607c`](#insn-00bc607c)

~~~json
{
  "source": "00bc607c",
  "target": "00bc6094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc608c`](#insn-00bc608c)

~~~json
{
  "source": "00bc608c",
  "target": "00bc6070",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc609c`](#insn-00bc609c)

~~~json
{
  "source": "00bc609c",
  "target": "00bc62fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc60a0`](#insn-00bc60a0)

~~~json
{
  "source": "00bc60a0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc60c4`](#insn-00bc60c4)

~~~json
{
  "source": "00bc60c4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc60c8`](#insn-00bc60c8)

~~~json
{
  "source": "00bc60c8",
  "target": "00bc612c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc60e8`](#insn-00bc60e8)

~~~json
{
  "source": "00bc60e8",
  "target": "00c17848",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17848",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc6110`](#insn-00bc6110)

~~~json
{
  "source": "00bc6110",
  "target": "00bc6164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6128`](#insn-00bc6128)

~~~json
{
  "source": "00bc6128",
  "target": "00bc62fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6134`](#insn-00bc6134)

~~~json
{
  "source": "00bc6134",
  "target": "00bc6218",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6144`](#insn-00bc6144)

~~~json
{
  "source": "00bc6144",
  "target": "00bc6158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6154`](#insn-00bc6154)

~~~json
{
  "source": "00bc6154",
  "target": "00bc6188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6160`](#insn-00bc6160)

~~~json
{
  "source": "00bc6160",
  "target": "00bc61b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6174`](#insn-00bc6174)

~~~json
{
  "source": "00bc6174",
  "target": "00bc61d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6178`](#insn-00bc6178)

~~~json
{
  "source": "00bc6178",
  "target": "00bdd200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6180`](#insn-00bc6180)

~~~json
{
  "source": "00bc6180",
  "target": "00bc6204",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6184`](#insn-00bc6184)

~~~json
{
  "source": "00bc6184",
  "target": "00bc6328",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6198`](#insn-00bc6198)

~~~json
{
  "source": "00bc6198",
  "target": "00bc61b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc61a8`](#insn-00bc61a8)

~~~json
{
  "source": "00bc61a8",
  "target": "00bc618c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc61c4`](#insn-00bc61c4)

~~~json
{
  "source": "00bc61c4",
  "target": "00bc60dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc61cc`](#insn-00bc61cc)

~~~json
{
  "source": "00bc61cc",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc61d0`](#insn-00bc61d0)

~~~json
{
  "source": "00bc61d0",
  "target": "00bc60cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc61d4`](#insn-00bc61d4)

~~~json
{
  "source": "00bc61d4",
  "target": "00bc6324",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc61dc`](#insn-00bc61dc)

~~~json
{
  "source": "00bc61dc",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc61e0`](#insn-00bc61e0)

~~~json
{
  "source": "00bc61e0",
  "target": "00bc632c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc61e8`](#insn-00bc61e8)

~~~json
{
  "source": "00bc61e8",
  "target": "00bc6200",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc61f8`](#insn-00bc61f8)

~~~json
{
  "source": "00bc61f8",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6214`](#insn-00bc6214)

~~~json
{
  "source": "00bc6214",
  "target": "00bc6114",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc621c`](#insn-00bc621c)

~~~json
{
  "source": "00bc621c",
  "target": "00bc6244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6228`](#insn-00bc6228)

~~~json
{
  "source": "00bc6228",
  "target": "00bc6244",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc623c`](#insn-00bc623c)

~~~json
{
  "source": "00bc623c",
  "target": "00bc6250",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6240`](#insn-00bc6240)

~~~json
{
  "source": "00bc6240",
  "target": "00bc62fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc624c`](#insn-00bc624c)

~~~json
{
  "source": "00bc624c",
  "target": "00bc62fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6258`](#insn-00bc6258)

~~~json
{
  "source": "00bc6258",
  "target": "00bc62fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc625c`](#insn-00bc625c)

~~~json
{
  "source": "00bc625c",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc626c`](#insn-00bc626c)

~~~json
{
  "source": "00bc626c",
  "target": "00bbff2c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6288`](#insn-00bc6288)

~~~json
{
  "source": "00bc6288",
  "target": "00bc62a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6290`](#insn-00bc6290)

~~~json
{
  "source": "00bc6290",
  "target": "00bdd180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6294`](#insn-00bc6294)

~~~json
{
  "source": "00bc6294",
  "target": "00bc6324",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc62c0`](#insn-00bc62c0)

~~~json
{
  "source": "00bc62c0",
  "target": "00c18e88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c18e88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc62d0`](#insn-00bc62d0)

~~~json
{
  "source": "00bc62d0",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc62d8`](#insn-00bc62d8)

~~~json
{
  "source": "00bc62d8",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc62ec`](#insn-00bc62ec)

~~~json
{
  "source": "00bc62ec",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc62f8`](#insn-00bc62f8)

~~~json
{
  "source": "00bc62f8",
  "target": "00bc6300",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6300`](#insn-00bc6300)

~~~json
{
  "source": "00bc6300",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6304`](#insn-00bc6304)

~~~json
{
  "source": "00bc6304",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6308`](#insn-00bc6308)

~~~json
{
  "source": "00bc6308",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc630c`](#insn-00bc630c)

~~~json
{
  "source": "00bc630c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6310`](#insn-00bc6310)

~~~json
{
  "source": "00bc6310",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6314`](#insn-00bc6314)

~~~json
{
  "source": "00bc6314",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc6324`](#insn-00bc6324)

~~~json
{
  "source": "00bc6324",
  "target": "00bdb180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc6328`](#insn-00bc6328)

~~~json
{
  "source": "00bc6328",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc632c`](#insn-00bc632c)

~~~json
{
  "source": "00bc632c",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
