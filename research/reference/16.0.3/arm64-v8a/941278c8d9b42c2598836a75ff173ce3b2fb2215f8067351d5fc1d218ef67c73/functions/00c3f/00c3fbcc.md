# 00c3fbcc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c3ebd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c3e/00c3ebd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0090.md#compare-ec26f416c108181455f73046559dd2a6)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c3fbcc",
  "name": "FUN_00c3fbcc",
  "size": 964,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "da9bc0e923ed3b2346e92f901d15e1c04c1f5b669ecb0e3729e2078d9ba52ce7",
  "source_text_sha256": "da9bc0e923ed3b2346e92f901d15e1c04c1f5b669ecb0e3729e2078d9ba52ce7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c3fbcc",
        "00c3ff8f"
      ]
    ],
    "bytes_sha256": "eeacbf6278e1673917ad415f0f8cfcdeb82e4da718049ea0eeb89d5815a24700",
    "instruction_count": 241,
    "instruction_bytes": 964,
    "body_bytes": 964,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c3bd5c](../00c3b/00c3bd5c.md)
- [00c3d29c](../00c3d/00c3d29c.md)
- [00c40e0c](../00c40/00c40e0c.md)
- [00c4c6b8](../00c4c/00c4c6b8.md)

## 呼び出し先

- [00c40a00](../00c40/00c40a00.md)
- [00c40ad8](../00c40/00c40ad8.md)
- [00c58fe0](../00c58/00c58fe0.md)
- [00c590c0](../00c59/00c590c0.md)
- [00c5b0c0](../00c5b/00c5b0c0.md)
- [00c5b140](../00c5b/00c5b140.md)
- [00c5c1e0](../00c5c/00c5c1e0.md)

## 関連文字列（未確認候補）

~~~text
"auto"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6693 bytes

~~~c

undefined8 * FUN_00c3fbcc(long *param_1)

{
  byte *pbVar1;
  byte *pbVar2;
  byte *pbVar3;
  undefined8 *puVar4;
  long *plVar5;
  ulong uVar6;
  long lVar7;
  long lVar8;
  ulong uVar9;
  byte *pbVar10;
  byte *pbVar11;
  undefined8 *puVar12;
  size_t __n;
  ulong uVar13;
  void *pvVar14;
  long *plVar15;
  undefined8 local_48;
  
  pbVar1 = (byte *)*param_1;
  pbVar2 = (byte *)param_1[1];
  if ((pbVar1 != pbVar2) && (*pbVar1 == 0x54)) {
                    /* try { // try from 00c3fc00 to 00d3fca7 has its CatchHandler @ 00c4052c */
    pbVar11 = pbVar1 + 1;
    *param_1 = (long)pbVar11;
    if (pbVar11 != pbVar2) {
      if (*pbVar11 == 0x4c) {
        pbVar11 = pbVar1 + 2;
        *param_1 = (long)pbVar11;
        if (pbVar2 == pbVar11) {
          return (undefined8 *)0x0;
        }
        if (*pbVar11 - 0x3a < 0xfffffff6) {
          return (undefined8 *)0x0;
        }
        lVar7 = 0;
        pbVar3 = pbVar1 + 4;
        do {
          pbVar11 = pbVar3;
          pbVar10 = pbVar11 + -1;
          *param_1 = (long)pbVar10;
          lVar8 = (ulong)pbVar11[-2] + lVar7 * 10;
          lVar7 = lVar8 + -0x30;
          if (pbVar10 == pbVar2) break;
          pbVar3 = pbVar11 + 1;
        } while (pbVar11[-1] - 0x30 < 10);
        if (pbVar10 == pbVar2) {
          return (undefined8 *)0x0;
        }
        if (pbVar11[-1] != 0x5f) {
          return (undefined8 *)0x0;
        }
        uVar9 = lVar8 - 0x2f;
        *param_1 = (long)pbVar11;
      }
      else {
                    /* try { // try from 00c3fca8 to 00d3fcb3 has its CatchHandler @ 00c40510 */
        uVar9 = 0;
      }
      if (pbVar11 != pbVar2) {
        if (*pbVar11 == 0x5f) {
          uVar13 = 0;
        }
        else {
          if (*pbVar11 - 0x3a < 0xfffffff6) {
            return (undefined8 *)0x0;
          }
          lVar7 = 0;
          pbVar3 = pbVar11;
          do {
            pbVar11 = pbVar3 + 1;
            *param_1 = (long)pbVar11;
            lVar8 = (ulong)*pbVar3 + lVar7 * 10;
            lVar7 = lVar8 + -0x30;
            if (pbVar11 == pbVar2) break;
            pbVar3 = pbVar11;
          } while (*pbVar11 - 0x30 < 10);
          if (pbVar11 == pbVar2) {
            return (undefined8 *)0x0;
          }
          if (*pbVar11 != 0x5f) {
            return (undefined8 *)0x0;
          }
          uVar13 = lVar8 - 0x2f;
        }
        *param_1 = (long)(pbVar11 + 1);
        if (*(char *)((long)param_1 + 0x30a) == '\0') {
          if ((*(char *)((long)param_1 + 0x309) == '\0') || (uVar9 != 0)) {
            uVar6 = param_1[0x54] - param_1[0x53] >> 3;
            if ((uVar9 < uVar6) &&
               ((plVar15 = *(long **)(param_1[0x53] + uVar9 * 8), plVar15 != (long *)0x0 &&
                (uVar13 < (ulong)(plVar15[1] - *plVar15 >> 3))))) {
              return *(undefined8 **)(*plVar15 + uVar13 * 8);
            }
            if (uVar6 < uVar9) {
              return (undefined8 *)0x0;
            }
            if (param_1[0x62] == uVar9) {
              if (uVar9 == uVar6) {
                local_48 = 0;
                FUN_00c40a00(param_1 + 0x53,&local_48);
                    /* try { // try from 00c3ff10 to 00d3ff1f has its CatchHandler @ 00c40484 */
              }
              puVar4 = (undefined8 *)FUN_00c40ad8(param_1,&DAT_002a1d8c);
              return puVar4;
            }
            return (undefined8 *)0x0;
          }
          pvVar14 = (void *)param_1[0x266];
          lVar7 = *(long *)((long)pvVar14 + 8);
          puVar4 = pvVar14;
          if (lVar7 - 0xfc0U < 0xfffffffffffff010) {
            puVar4 = malloc(0x1000);
            if (puVar4 == (void *)0x0) {
LAB_00c3ff88:
                    /* WARNING: Subroutine does not return */
              _ZSt9terminatev();
            }
            lVar7 = 0;
            *puVar4 = pvVar14;
            puVar4[1] = 0;
                    /* try { // try from 00c3fe1c to 00d3ff0f has its CatchHandler @ 00c4049c */
            param_1[0x266] = (long)puVar4;
          }
          *(long *)((long)puVar4 + 8) = lVar7 + 0x30;
          puVar12 = (undefined8 *)((long)puVar4 + lVar7 + 0x10);
          *puVar12 = &PTR_FUN_00c987c0;
          *(ulong *)((long)puVar4 + lVar7 + 0x20) = uVar13;
          *(undefined8 *)((long)puVar4 + lVar7 + 0x28) = 0;
          *(undefined1 *)((long)puVar4 + lVar7 + 0x30) = 0;
          *(ushort *)((long)puVar4 + lVar7 + 0x19) =
               *(ushort *)((long)puVar4 + lVar7 + 0x19) & 0xf000 | 0xa80;
          plVar15 = (long *)param_1[0x5b];
          plVar5 = (long *)param_1[0x5c];
          *(undefined1 *)((long)puVar4 + lVar7 + 0x18) = 0x2c;
          if (plVar15 == plVar5) {
            plVar5 = (long *)param_1[0x5a];
            __n = (long)plVar15 - (long)plVar5;
            if (plVar5 == param_1 + 0x5d) {
              pvVar14 = malloc(__n * 2);
              if (pvVar14 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                abort();
              }
              if (plVar15 != plVar5) {
                memmove(pvVar14,plVar5,__n);
              }
              param_1[0x5a] = (long)pvVar14;
            }
            else {
              pvVar14 = realloc(plVar5,__n * 2);
              param_1[0x5a] = (long)pvVar14;
              if (pvVar14 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
                abort();
              }
            }
            plVar15 = (long *)((long)pvVar14 + __n);
            param_1[0x5c] = (long)((long)pvVar14 + ((long)__n >> 2) * 8);
          }
          param_1[0x5b] = (long)(plVar15 + 1);
          *plVar15 = (long)puVar12;
          return puVar12;
        }
        pvVar14 = (void *)param_1[0x266];
        lVar7 = *(long *)((long)pvVar14 + 8);
        puVar4 = pvVar14;
        if (lVar7 - 0xfd0U < 0xfffffffffffff010) {
          puVar4 = malloc(0x1000);
          if (puVar4 == (void *)0x0) goto LAB_00c3ff88;
          lVar7 = 0;
          *puVar4 = pvVar14;
          puVar4[1] = 0;
          param_1[0x266] = (long)puVar4;
        }
        *(long *)((long)puVar4 + 8) = lVar7 + 0x20;
                    /* try { // try from 00c3fd1c to 00d3fdc7 has its CatchHandler @ 00c40540 */
        puVar12 = (undefined8 *)((long)puVar4 + lVar7 + 0x10);
        *puVar12 = &PTR_FUN_00c986e0;
        *(undefined1 *)((long)puVar4 + lVar7 + 0x18) = 8;
        *(ushort *)((long)puVar4 + lVar7 + 0x19) =
             *(ushort *)((long)puVar4 + lVar7 + 0x19) & 0xf000 | 0x540;
        *(byte **)((long)puVar4 + lVar7 + 0x20) = pbVar1;
        *(long *)((long)puVar4 + lVar7 + 0x28) = (long)pbVar11 - (long)pbVar1;
        return puVar12;
      }
    }
  }
  return (undefined8 *)0x0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c3fbcc"></a> `00c3fbcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c3fbd0"></a> `00c3fbd0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00c3fbd4"></a> `00c3fbd4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3fbd8"></a> `00c3fbd8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3fbdc"></a> `00c3fbdc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c3fbe0"></a> `00c3fbe0` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c3fbe4"></a> `00c3fbe4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00c3fbe8"></a> `00c3fbe8` | `14 20 40 a9` | ldp x20,x8,[x0] | `FALL_THROUGH`
<a id="insn-00c3fbec"></a> `00c3fbec` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00c3fbf0"></a> `00c3fbf0` | `20 0e 00 54` | b.eq 0x00c3fdb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fbf4"></a> `00c3fbf4` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00c3fbf8"></a> `00c3fbf8` | `3f 51 01 71` | cmp w9,#0x54 | `FALL_THROUGH`
<a id="insn-00c3fbfc"></a> `00c3fbfc` | `c1 0d 00 54` | b.ne 0x00c3fdb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fc00"></a> `00c3fc00` | `95 06 00 91` | add x21,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00c3fc04"></a> `00c3fc04` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00c3fc08"></a> `00c3fc08` | `15 00 00 f9` | str x21,[x0] | `FALL_THROUGH`
<a id="insn-00c3fc0c"></a> `00c3fc0c` | `40 0d 00 54` | b.eq 0x00c3fdb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fc10"></a> `00c3fc10` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00c3fc14"></a> `00c3fc14` | `3f 31 01 71` | cmp w9,#0x4c | `FALL_THROUGH`
<a id="insn-00c3fc18"></a> `00c3fc18` | `81 04 00 54` | b.ne 0x00c3fca8 | `CONDITIONAL_JUMP`
<a id="insn-00c3fc1c"></a> `00c3fc1c` | `89 0a 00 91` | add x9,x20,#0x2 | `FALL_THROUGH`
<a id="insn-00c3fc20"></a> `00c3fc20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00c3fc24"></a> `00c3fc24` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00c3fc28"></a> `00c3fc28` | `60 0c 00 54` | b.eq 0x00c3fdb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fc2c"></a> `00c3fc2c` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00c3fc30"></a> `00c3fc30` | `29 e9 00 51` | sub w9,w9,#0x3a | `FALL_THROUGH`
<a id="insn-00c3fc34"></a> `00c3fc34` | `3f 29 00 31` | cmn w9,#0xa | `FALL_THROUGH`
<a id="insn-00c3fc38"></a> `00c3fc38` | `e3 0b 00 54` | b.cc 0x00c3fdb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fc3c"></a> `00c3fc3c` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00c3fc40"></a> `00c3fc40` | `8c 12 00 91` | add x12,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00c3fc44"></a> `00c3fc44` | `4a 01 80 52` | mov w10,#0xa | `FALL_THROUGH`
<a id="insn-00c3fc48"></a> `00c3fc48` | `8b 05 00 d1` | sub x11,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00c3fc4c"></a> `00c3fc4c` | `f5 03 0c aa` | mov x21,x12 | `FALL_THROUGH`
<a id="insn-00c3fc50"></a> `00c3fc50` | `0b 00 00 f9` | str x11,[x0] | `FALL_THROUGH`
<a id="insn-00c3fc54"></a> `00c3fc54` | `7f 01 08 eb` | cmp x11,x8 | `FALL_THROUGH`
<a id="insn-00c3fc58"></a> `00c3fc58` | `8c e1 5f 38` | ldurb w12,[x12, #-0x2] | `FALL_THROUGH`
<a id="insn-00c3fc5c"></a> `00c3fc5c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c3fc60"></a> `00c3fc60` | `29 31 0a 9b` | madd x9,x9,x10,x12 | `FALL_THROUGH`
<a id="insn-00c3fc64"></a> `00c3fc64` | `29 c1 00 d1` | sub x9,x9,#0x30 | `FALL_THROUGH`
<a id="insn-00c3fc68"></a> `00c3fc68` | `c0 00 00 54` | b.eq 0x00c3fc80 | `CONDITIONAL_JUMP`
<a id="insn-00c3fc6c"></a> `00c3fc6c` | `ac f2 5f 38` | ldurb w12,[x21, #-0x1] | `FALL_THROUGH`
<a id="insn-00c3fc70"></a> `00c3fc70` | `8c c1 00 51` | sub w12,w12,#0x30 | `FALL_THROUGH`
<a id="insn-00c3fc74"></a> `00c3fc74` | `9f 25 00 71` | cmp w12,#0x9 | `FALL_THROUGH`
<a id="insn-00c3fc78"></a> `00c3fc78` | `ac 06 00 91` | add x12,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00c3fc7c"></a> `00c3fc7c` | `69 fe ff 54` | b.ls 0x00c3fc48 | `CONDITIONAL_JUMP`
<a id="insn-00c3fc80"></a> `00c3fc80` | `7f 01 08 eb` | cmp x11,x8 | `FALL_THROUGH`
<a id="insn-00c3fc84"></a> `00c3fc84` | `80 09 00 54` | b.eq 0x00c3fdb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fc88"></a> `00c3fc88` | `aa f2 5f 38` | ldurb w10,[x21, #-0x1] | `FALL_THROUGH`
<a id="insn-00c3fc8c"></a> `00c3fc8c` | `5f 7d 01 71` | cmp w10,#0x5f | `FALL_THROUGH`
<a id="insn-00c3fc90"></a> `00c3fc90` | `21 09 00 54` | b.ne 0x00c3fdb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fc94"></a> `00c3fc94` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c3fc98"></a> `00c3fc98` | `15 00 00 f9` | str x21,[x0] | `FALL_THROUGH`
<a id="insn-00c3fc9c"></a> `00c3fc9c` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00c3fca0"></a> `00c3fca0` | `a1 00 00 54` | b.ne 0x00c3fcb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fca4"></a> `00c3fca4` | `44 00 00 14` | b 0x00c3fdb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00c3fca8"></a> `00c3fca8` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00c3fcac"></a> `00c3fcac` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00c3fcb0"></a> `00c3fcb0` | `20 08 00 54` | b.eq 0x00c3fdb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fcb4"></a> `00c3fcb4` | `aa 02 40 39` | ldrb w10,[x21] | `FALL_THROUGH`
<a id="insn-00c3fcb8"></a> `00c3fcb8` | `5f 7d 01 71` | cmp w10,#0x5f | `FALL_THROUGH`
<a id="insn-00c3fcbc"></a> `00c3fcbc` | `61 04 00 54` | b.ne 0x00c3fd48 | `CONDITIONAL_JUMP`
<a id="insn-00c3fcc0"></a> `00c3fcc0` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00c3fcc4"></a> `00c3fcc4` | `08 28 4c 39` | ldrb w8,[x0, #0x30a] | `FALL_THROUGH`
<a id="insn-00c3fcc8"></a> `00c3fcc8` | `aa 06 00 91` | add x10,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00c3fccc"></a> `00c3fccc` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00c3fcd0"></a> `00c3fcd0` | `48 08 00 34` | cbz w8,0x00c3fdd8 | `CONDITIONAL_JUMP`
<a id="insn-00c3fcd4"></a> `00c3fcd4` | `16 98 49 f9` | ldr x22,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00c3fcd8"></a> `00c3fcd8` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c3fcdc"></a> `00c3fcdc` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00c3fce0"></a> `00c3fce0` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00c3fce4"></a> `00c3fce4` | `28 01 00 54` | b.hi 0x00c3fd08 | `CONDITIONAL_JUMP`
<a id="insn-00c3fce8"></a> `00c3fce8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00c3fcec"></a> `00c3fcec` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c3fcf0"></a> `00c3fcf0` | `f4 6c 00 94` | bl 0x00c5b0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00c3fcf4"></a> `00c3fcf4` | `a0 14 00 b4` | cbz x0,0x00c3ff88 | `CONDITIONAL_JUMP`
<a id="insn-00c3fcf8"></a> `00c3fcf8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00c3fcfc"></a> `00c3fcfc` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c3fd00"></a> `00c3fd00` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00c3fd04"></a> `00c3fd04` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00c3fd08"></a> `00c3fd08` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00c3fd0c"></a> `00c3fd0c` | `d3 02 08 8b` | add x19,x22,x8 | `FALL_THROUGH`
<a id="insn-00c3fd10"></a> `00c3fd10` | `c8 02 00 b0` | adrp x8,0xc98000 | `FALL_THROUGH`
<a id="insn-00c3fd14"></a> `00c3fd14` | `08 81 1b 91` | add x8,x8,#0x6e0 | `FALL_THROUGH`
<a id="insn-00c3fd18"></a> `00c3fd18` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00c3fd1c"></a> `00c3fd1c` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00c3fd20"></a> `00c3fd20` | `68 0e 01 f8` | str x8,[x19, #0x10]! | `FALL_THROUGH`
<a id="insn-00c3fd24"></a> `00c3fd24` | `68 92 40 78` | ldurh w8,[x19, #0x9] | `FALL_THROUGH`
<a id="insn-00c3fd28"></a> `00c3fd28` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00c3fd2c"></a> `00c3fd2c` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00c3fd30"></a> `00c3fd30` | `69 22 00 39` | strb w9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3fd34"></a> `00c3fd34` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00c3fd38"></a> `00c3fd38` | `68 92 00 78` | sturh w8,[x19, #0x9] | `FALL_THROUGH`
<a id="insn-00c3fd3c"></a> `00c3fd3c` | `a8 02 14 cb` | sub x8,x21,x20 | `FALL_THROUGH`
<a id="insn-00c3fd40"></a> `00c3fd40` | `74 22 01 a9` | stp x20,x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c3fd44"></a> `00c3fd44` | `1d 00 00 14` | b 0x00c3fdb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00c3fd48"></a> `00c3fd48` | `aa 02 40 39` | ldrb w10,[x21] | `FALL_THROUGH`
<a id="insn-00c3fd4c"></a> `00c3fd4c` | `4a e9 00 51` | sub w10,w10,#0x3a | `FALL_THROUGH`
<a id="insn-00c3fd50"></a> `00c3fd50` | `5f 29 00 31` | cmn w10,#0xa | `FALL_THROUGH`
<a id="insn-00c3fd54"></a> `00c3fd54` | `03 03 00 54` | b.cc 0x00c3fdb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fd58"></a> `00c3fd58` | `ea 03 1f aa` | mov x10,xzr | `FALL_THROUGH`
<a id="insn-00c3fd5c"></a> `00c3fd5c` | `ac 06 00 91` | add x12,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00c3fd60"></a> `00c3fd60` | `4b 01 80 52` | mov w11,#0xa | `FALL_THROUGH`
<a id="insn-00c3fd64"></a> `00c3fd64` | `0c 00 00 f9` | str x12,[x0] | `FALL_THROUGH`
<a id="insn-00c3fd68"></a> `00c3fd68` | `f5 03 0c aa` | mov x21,x12 | `FALL_THROUGH`
<a id="insn-00c3fd6c"></a> `00c3fd6c` | `8c f1 5f 38` | ldurb w12,[x12, #-0x1] | `FALL_THROUGH`
<a id="insn-00c3fd70"></a> `00c3fd70` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c3fd74"></a> `00c3fd74` | `4a 31 0b 9b` | madd x10,x10,x11,x12 | `FALL_THROUGH`
<a id="insn-00c3fd78"></a> `00c3fd78` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00c3fd7c"></a> `00c3fd7c` | `4a c1 00 d1` | sub x10,x10,#0x30 | `FALL_THROUGH`
<a id="insn-00c3fd80"></a> `00c3fd80` | `c0 00 00 54` | b.eq 0x00c3fd98 | `CONDITIONAL_JUMP`
<a id="insn-00c3fd84"></a> `00c3fd84` | `ec 03 15 aa` | mov x12,x21 | `FALL_THROUGH`
<a id="insn-00c3fd88"></a> `00c3fd88` | `8d 15 40 38` | ldrb w13,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-00c3fd8c"></a> `00c3fd8c` | `ad c1 00 51` | sub w13,w13,#0x30 | `FALL_THROUGH`
<a id="insn-00c3fd90"></a> `00c3fd90` | `bf 25 00 71` | cmp w13,#0x9 | `FALL_THROUGH`
<a id="insn-00c3fd94"></a> `00c3fd94` | `89 fe ff 54` | b.ls 0x00c3fd64 | `CONDITIONAL_JUMP`
<a id="insn-00c3fd98"></a> `00c3fd98` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00c3fd9c"></a> `00c3fd9c` | `c0 00 00 54` | b.eq 0x00c3fdb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fda0"></a> `00c3fda0` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00c3fda4"></a> `00c3fda4` | `1f 7d 01 71` | cmp w8,#0x5f | `FALL_THROUGH`
<a id="insn-00c3fda8"></a> `00c3fda8` | `61 00 00 54` | b.ne 0x00c3fdb4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fdac"></a> `00c3fdac` | `56 05 00 91` | add x22,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c3fdb0"></a> `00c3fdb0` | `c5 ff ff 17` | b 0x00c3fcc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00c3fdb4"></a> `00c3fdb4` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00c3fdb8"></a> `00c3fdb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c3fdbc"></a> `00c3fdbc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c3fdc0"></a> `00c3fdc0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c3fdc4"></a> `00c3fdc4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3fdc8"></a> `00c3fdc8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3fdcc"></a> `00c3fdcc` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00c3fdd0"></a> `00c3fdd0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c3fdd4"></a> `00c3fdd4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c3fdd8"></a> `00c3fdd8` | `08 24 4c 39` | ldrb w8,[x0, #0x309] | `FALL_THROUGH`
<a id="insn-00c3fddc"></a> `00c3fddc` | `48 06 00 34` | cbz w8,0x00c3fea4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fde0"></a> `00c3fde0` | `29 06 00 b5` | cbnz x9,0x00c3fea4 | `CONDITIONAL_JUMP`
<a id="insn-00c3fde4"></a> `00c3fde4` | `13 98 49 f9` | ldr x19,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00c3fde8"></a> `00c3fde8` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3fdec"></a> `00c3fdec` | `28 01 3f d1` | sub x8,x9,#0xfc0 | `FALL_THROUGH`
<a id="insn-00c3fdf0"></a> `00c3fdf0` | `1f c5 3f b1` | cmn x8,#0xff1 | `FALL_THROUGH`
<a id="insn-00c3fdf4"></a> `00c3fdf4` | `68 01 00 54` | b.hi 0x00c3fe20 | `CONDITIONAL_JUMP`
<a id="insn-00c3fdf8"></a> `00c3fdf8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00c3fdfc"></a> `00c3fdfc` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00c3fe00"></a> `00c3fe00` | `b0 6c 00 94` | bl 0x00c5b0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00c3fe04"></a> `00c3fe04` | `20 0c 00 b4` | cbz x0,0x00c3ff88 | `CONDITIONAL_JUMP`
<a id="insn-00c3fe08"></a> `00c3fe08` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00c3fe0c"></a> `00c3fe0c` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00c3fe10"></a> `00c3fe10` | `13 7c 00 a9` | stp x19,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00c3fe14"></a> `00c3fe14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00c3fe18"></a> `00c3fe18` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c3fe1c"></a> `00c3fe1c` | `88 9a 09 f9` | str x8,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00c3fe20"></a> `00c3fe20` | `28 c1 00 91` | add x8,x9,#0x30 | `FALL_THROUGH`
<a id="insn-00c3fe24"></a> `00c3fe24` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3fe28"></a> `00c3fe28` | `73 02 09 8b` | add x19,x19,x9 | `FALL_THROUGH`
<a id="insn-00c3fe2c"></a> `00c3fe2c` | `c8 02 00 b0` | adrp x8,0xc98000 | `FALL_THROUGH`
<a id="insn-00c3fe30"></a> `00c3fe30` | `08 01 1f 91` | add x8,x8,#0x7c0 | `FALL_THROUGH`
<a id="insn-00c3fe34"></a> `00c3fe34` | `09 50 81 52` | mov w9,#0xa80 | `FALL_THROUGH`
<a id="insn-00c3fe38"></a> `00c3fe38` | `68 0e 01 f8` | str x8,[x19, #0x10]! | `FALL_THROUGH`
<a id="insn-00c3fe3c"></a> `00c3fe3c` | `68 92 40 78` | ldurh w8,[x19, #0x9] | `FALL_THROUGH`
<a id="insn-00c3fe40"></a> `00c3fe40` | `76 7e 01 a9` | stp x22,xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c3fe44"></a> `00c3fe44` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00c3fe48"></a> `00c3fe48` | `7f 82 00 39` | strb wzr,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00c3fe4c"></a> `00c3fe4c` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00c3fe50"></a> `00c3fe50` | `89 05 80 52` | mov w9,#0x2c | `FALL_THROUGH`
<a id="insn-00c3fe54"></a> `00c3fe54` | `68 92 00 78` | sturh w8,[x19, #0x9] | `FALL_THROUGH`
<a id="insn-00c3fe58"></a> `00c3fe58` | `17 6c 41 f9` | ldr x23,[x0, #0x2d8] | `FALL_THROUGH`
<a id="insn-00c3fe5c"></a> `00c3fe5c` | `08 70 41 f9` | ldr x8,[x0, #0x2e0] | `FALL_THROUGH`
<a id="insn-00c3fe60"></a> `00c3fe60` | `69 22 00 39` | strb w9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00c3fe64"></a> `00c3fe64` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00c3fe68"></a> `00c3fe68` | `81 08 00 54` | b.ne 0x00c3ff78 | `CONDITIONAL_JUMP`
<a id="insn-00c3fe6c"></a> `00c3fe6c` | `16 68 41 f9` | ldr x22,[x0, #0x2d0] | `FALL_THROUGH`
<a id="insn-00c3fe70"></a> `00c3fe70` | `08 a0 0b 91` | add x8,x0,#0x2e8 | `FALL_THROUGH`
<a id="insn-00c3fe74"></a> `00c3fe74` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00c3fe78"></a> `00c3fe78` | `f4 02 16 cb` | sub x20,x23,x22 | `FALL_THROUGH`
<a id="insn-00c3fe7c"></a> `00c3fe7c` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00c3fe80"></a> `00c3fe80` | `81 fa 7f d3` | lsl x1,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00c3fe84"></a> `00c3fe84` | `a0 05 00 54` | b.eq 0x00c3ff38 | `CONDITIONAL_JUMP`
<a id="insn-00c3fe88"></a> `00c3fe88` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00c3fe8c"></a> `00c3fe8c` | `ad 6c 00 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00c3fe90"></a> `00c3fe90` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c3fe94"></a> `00c3fe94` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00c3fe98"></a> `00c3fe98` | `15 6b 01 f9` | str x21,[x24, #0x2d0] | `FALL_THROUGH`
<a id="insn-00c3fe9c"></a> `00c3fe9c` | `75 06 00 b5` | cbnz x21,0x00c3ff68 | `CONDITIONAL_JUMP`
<a id="insn-00c3fea0"></a> `00c3fea0` | `d0 70 00 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`
<a id="insn-00c3fea4"></a> `00c3fea4` | `08 50 41 f9` | ldr x8,[x0, #0x2a0] | `FALL_THROUGH`
<a id="insn-00c3fea8"></a> `00c3fea8` | `0a 4c 41 f9` | ldr x10,[x0, #0x298] | `FALL_THROUGH`
<a id="insn-00c3feac"></a> `00c3feac` | `08 01 0a cb` | sub x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00c3feb0"></a> `00c3feb0` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00c3feb4"></a> `00c3feb4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c3feb8"></a> `00c3feb8` | `22 01 00 54` | b.cs 0x00c3fedc | `CONDITIONAL_JUMP`
<a id="insn-00c3febc"></a> `00c3febc` | `4a 79 69 f8` | ldr x10,[x10, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00c3fec0"></a> `00c3fec0` | `ea 00 00 b4` | cbz x10,0x00c3fedc | `CONDITIONAL_JUMP`
<a id="insn-00c3fec4"></a> `00c3fec4` | `4a 2d 40 a9` | ldp x10,x11,[x10] | `FALL_THROUGH`
<a id="insn-00c3fec8"></a> `00c3fec8` | `6b 01 0a cb` | sub x11,x11,x10 | `FALL_THROUGH`
<a id="insn-00c3fecc"></a> `00c3fecc` | `df 0e 8b eb` | cmp x22,x11, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00c3fed0"></a> `00c3fed0` | `62 00 00 54` | b.cs 0x00c3fedc | `CONDITIONAL_JUMP`
<a id="insn-00c3fed4"></a> `00c3fed4` | `53 79 76 f8` | ldr x19,[x10, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00c3fed8"></a> `00c3fed8` | `b8 ff ff 17` | b 0x00c3fdb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00c3fedc"></a> `00c3fedc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c3fee0"></a> `00c3fee0` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00c3fee4"></a> `00c3fee4` | `a8 f6 ff 54` | b.hi 0x00c3fdb8 | `CONDITIONAL_JUMP`
<a id="insn-00c3fee8"></a> `00c3fee8` | `0a 88 41 f9` | ldr x10,[x0, #0x310] | `FALL_THROUGH`
<a id="insn-00c3feec"></a> `00c3feec` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00c3fef0"></a> `00c3fef0` | `41 f6 ff 54` | b.ne 0x00c3fdb8 | `CONDITIONAL_JUMP`
<a id="insn-00c3fef4"></a> `00c3fef4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00c3fef8"></a> `00c3fef8` | `e1 00 00 54` | b.ne 0x00c3ff14 | `CONDITIONAL_JUMP`
<a id="insn-00c3fefc"></a> `00c3fefc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00c3ff00"></a> `00c3ff00` | `00 60 0a 91` | add x0,x0,#0x298 | `FALL_THROUGH`
<a id="insn-00c3ff04"></a> `00c3ff04` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00c3ff08"></a> `00c3ff08` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00c3ff0c"></a> `00c3ff0c` | `bd 02 00 94` | bl 0x00c40a00 | `UNCONDITIONAL_CALL`
<a id="insn-00c3ff10"></a> `00c3ff10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00c3ff14"></a> `00c3ff14` | `01 b3 ff d0` | adrp x1,0x2a1000 | `FALL_THROUGH`
<a id="insn-00c3ff18"></a> `00c3ff18` | `21 30 36 91` | add x1,x1,#0xd8c | `FALL_THROUGH`
<a id="insn-00c3ff1c"></a> `00c3ff1c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c3ff20"></a> `00c3ff20` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c3ff24"></a> `00c3ff24` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c3ff28"></a> `00c3ff28` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c3ff2c"></a> `00c3ff2c` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00c3ff30"></a> `00c3ff30` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c3ff34"></a> `00c3ff34` | `e9 02 00 14` | b 0x00c40ad8 | `CALL_TERMINATOR`
<a id="insn-00c3ff38"></a> `00c3ff38` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00c3ff3c"></a> `00c3ff3c` | `61 6c 00 94` | bl 0x00c5b0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00c3ff40"></a> `00c3ff40` | `60 02 00 b4` | cbz x0,0x00c3ff8c | `CONDITIONAL_JUMP`
<a id="insn-00c3ff44"></a> `00c3ff44` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00c3ff48"></a> `00c3ff48` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00c3ff4c"></a> `00c3ff4c` | `a0 00 00 54` | b.eq 0x00c3ff60 | `CONDITIONAL_JUMP`
<a id="insn-00c3ff50"></a> `00c3ff50` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c3ff54"></a> `00c3ff54` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00c3ff58"></a> `00c3ff58` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00c3ff5c"></a> `00c3ff5c` | `21 64 00 94` | bl 0x00c58fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00c3ff60"></a> `00c3ff60` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00c3ff64"></a> `00c3ff64` | `15 6b 01 f9` | str x21,[x24, #0x2d0] | `FALL_THROUGH`
<a id="insn-00c3ff68"></a> `00c3ff68` | `88 fe 42 93` | asr x8,x20,#0x2 | `FALL_THROUGH`
<a id="insn-00c3ff6c"></a> `00c3ff6c` | `b7 02 14 8b` | add x23,x21,x20 | `FALL_THROUGH`
<a id="insn-00c3ff70"></a> `00c3ff70` | `a8 0e 08 8b` | add x8,x21,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00c3ff74"></a> `00c3ff74` | `08 70 01 f9` | str x8,[x0, #0x2e0] | `FALL_THROUGH`
<a id="insn-00c3ff78"></a> `00c3ff78` | `e8 22 00 91` | add x8,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00c3ff7c"></a> `00c3ff7c` | `08 6c 01 f9` | str x8,[x0, #0x2d8] | `FALL_THROUGH`
<a id="insn-00c3ff80"></a> `00c3ff80` | `f3 02 00 f9` | str x19,[x23] | `FALL_THROUGH`
<a id="insn-00c3ff84"></a> `00c3ff84` | `8d ff ff 17` | b 0x00c3fdb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00c3ff88"></a> `00c3ff88` | `4e 64 00 94` | bl 0x00c590c0 | `CALL_TERMINATOR`
<a id="insn-00c3ff8c"></a> `00c3ff8c` | `95 70 00 94` | bl 0x00c5c1e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c3fbcc`](#insn-00c3fbcc) 範囲 `[['00c3fbcc', '00c3fbf3']]`
  - `CONDITIONAL_JUMP` [`00c3fbf0`](#insn-00c3fbf0) → [`00c3fdb4`](#insn-00c3fdb4)
  - `FALL_THROUGH` [`00c3fbf0`](#insn-00c3fbf0) → [`00c3fbf4`](#insn-00c3fbf4)
- ブロック [`00c3fbf4`](#insn-00c3fbf4) 範囲 `[['00c3fbf4', '00c3fbff']]`
  - `CONDITIONAL_JUMP` [`00c3fbfc`](#insn-00c3fbfc) → [`00c3fdb4`](#insn-00c3fdb4)
  - `FALL_THROUGH` [`00c3fbfc`](#insn-00c3fbfc) → [`00c3fc00`](#insn-00c3fc00)
- ブロック [`00c3fc00`](#insn-00c3fc00) 範囲 `[['00c3fc00', '00c3fc0f']]`
  - `CONDITIONAL_JUMP` [`00c3fc0c`](#insn-00c3fc0c) → [`00c3fdb4`](#insn-00c3fdb4)
  - `FALL_THROUGH` [`00c3fc0c`](#insn-00c3fc0c) → [`00c3fc10`](#insn-00c3fc10)
- ブロック [`00c3fc10`](#insn-00c3fc10) 範囲 `[['00c3fc10', '00c3fc1b']]`
  - `CONDITIONAL_JUMP` [`00c3fc18`](#insn-00c3fc18) → [`00c3fca8`](#insn-00c3fca8)
  - `FALL_THROUGH` [`00c3fc18`](#insn-00c3fc18) → [`00c3fc1c`](#insn-00c3fc1c)
- ブロック [`00c3fc1c`](#insn-00c3fc1c) 範囲 `[['00c3fc1c', '00c3fc2b']]`
  - `CONDITIONAL_JUMP` [`00c3fc28`](#insn-00c3fc28) → [`00c3fdb4`](#insn-00c3fdb4)
  - `FALL_THROUGH` [`00c3fc28`](#insn-00c3fc28) → [`00c3fc2c`](#insn-00c3fc2c)
- ブロック [`00c3fc2c`](#insn-00c3fc2c) 範囲 `[['00c3fc2c', '00c3fc3b']]`
  - `CONDITIONAL_JUMP` [`00c3fc38`](#insn-00c3fc38) → [`00c3fdb4`](#insn-00c3fdb4)
  - `FALL_THROUGH` [`00c3fc38`](#insn-00c3fc38) → [`00c3fc3c`](#insn-00c3fc3c)
- ブロック [`00c3fc3c`](#insn-00c3fc3c) 範囲 `[['00c3fc3c', '00c3fc47']]`
  - `FALL_THROUGH` [`00c3fc44`](#insn-00c3fc44) → [`00c3fc48`](#insn-00c3fc48)
- ブロック [`00c3fc48`](#insn-00c3fc48) 範囲 `[['00c3fc48', '00c3fc6b']]`
  - `CONDITIONAL_JUMP` [`00c3fc68`](#insn-00c3fc68) → [`00c3fc80`](#insn-00c3fc80)
  - `FALL_THROUGH` [`00c3fc68`](#insn-00c3fc68) → [`00c3fc6c`](#insn-00c3fc6c)
- ブロック [`00c3fc6c`](#insn-00c3fc6c) 範囲 `[['00c3fc6c', '00c3fc7f']]`
  - `CONDITIONAL_JUMP` [`00c3fc7c`](#insn-00c3fc7c) → [`00c3fc48`](#insn-00c3fc48)
  - `FALL_THROUGH` [`00c3fc7c`](#insn-00c3fc7c) → [`00c3fc80`](#insn-00c3fc80)
- ブロック [`00c3fc80`](#insn-00c3fc80) 範囲 `[['00c3fc80', '00c3fc87']]`
  - `CONDITIONAL_JUMP` [`00c3fc84`](#insn-00c3fc84) → [`00c3fdb4`](#insn-00c3fdb4)
  - `FALL_THROUGH` [`00c3fc84`](#insn-00c3fc84) → [`00c3fc88`](#insn-00c3fc88)
- ブロック [`00c3fc88`](#insn-00c3fc88) 範囲 `[['00c3fc88', '00c3fc93']]`
  - `CONDITIONAL_JUMP` [`00c3fc90`](#insn-00c3fc90) → [`00c3fdb4`](#insn-00c3fdb4)
  - `FALL_THROUGH` [`00c3fc90`](#insn-00c3fc90) → [`00c3fc94`](#insn-00c3fc94)
- ブロック [`00c3fc94`](#insn-00c3fc94) 範囲 `[['00c3fc94', '00c3fca3']]`
  - `CONDITIONAL_JUMP` [`00c3fca0`](#insn-00c3fca0) → [`00c3fcb4`](#insn-00c3fcb4)
  - `FALL_THROUGH` [`00c3fca0`](#insn-00c3fca0) → [`00c3fca4`](#insn-00c3fca4)
- ブロック [`00c3fca4`](#insn-00c3fca4) 範囲 `[['00c3fca4', '00c3fca7']]`
  - `UNCONDITIONAL_JUMP` [`00c3fca4`](#insn-00c3fca4) → [`00c3fdb4`](#insn-00c3fdb4)
- ブロック [`00c3fca8`](#insn-00c3fca8) 範囲 `[['00c3fca8', '00c3fcb3']]`
  - `CONDITIONAL_JUMP` [`00c3fcb0`](#insn-00c3fcb0) → [`00c3fdb4`](#insn-00c3fdb4)
  - `FALL_THROUGH` [`00c3fcb0`](#insn-00c3fcb0) → [`00c3fcb4`](#insn-00c3fcb4)
- ブロック [`00c3fcb4`](#insn-00c3fcb4) 範囲 `[['00c3fcb4', '00c3fcbf']]`
  - `CONDITIONAL_JUMP` [`00c3fcbc`](#insn-00c3fcbc) → [`00c3fd48`](#insn-00c3fd48)
  - `FALL_THROUGH` [`00c3fcbc`](#insn-00c3fcbc) → [`00c3fcc0`](#insn-00c3fcc0)
- ブロック [`00c3fcc0`](#insn-00c3fcc0) 範囲 `[['00c3fcc0', '00c3fcc3']]`
  - `FALL_THROUGH` [`00c3fcc0`](#insn-00c3fcc0) → [`00c3fcc4`](#insn-00c3fcc4)
- ブロック [`00c3fcc4`](#insn-00c3fcc4) 範囲 `[['00c3fcc4', '00c3fcd3']]`
  - `CONDITIONAL_JUMP` [`00c3fcd0`](#insn-00c3fcd0) → [`00c3fdd8`](#insn-00c3fdd8)
  - `FALL_THROUGH` [`00c3fcd0`](#insn-00c3fcd0) → [`00c3fcd4`](#insn-00c3fcd4)
- ブロック [`00c3fcd4`](#insn-00c3fcd4) 範囲 `[['00c3fcd4', '00c3fce7']]`
  - `CONDITIONAL_JUMP` [`00c3fce4`](#insn-00c3fce4) → [`00c3fd08`](#insn-00c3fd08)
  - `FALL_THROUGH` [`00c3fce4`](#insn-00c3fce4) → [`00c3fce8`](#insn-00c3fce8)
- ブロック [`00c3fce8`](#insn-00c3fce8) 範囲 `[['00c3fce8', '00c3fcf7']]`
  - `CONDITIONAL_JUMP` [`00c3fcf4`](#insn-00c3fcf4) → [`00c3ff88`](#insn-00c3ff88)
  - `FALL_THROUGH` [`00c3fcf4`](#insn-00c3fcf4) → [`00c3fcf8`](#insn-00c3fcf8)
- ブロック [`00c3fcf8`](#insn-00c3fcf8) 範囲 `[['00c3fcf8', '00c3fd07']]`
  - `FALL_THROUGH` [`00c3fd04`](#insn-00c3fd04) → [`00c3fd08`](#insn-00c3fd08)
- ブロック [`00c3fd08`](#insn-00c3fd08) 範囲 `[['00c3fd08', '00c3fd1b']]`
  - `FALL_THROUGH` [`00c3fd18`](#insn-00c3fd18) → [`00c3fd1c`](#insn-00c3fd1c)
- ブロック [`00c3fd1c`](#insn-00c3fd1c) 範囲 `[['00c3fd1c', '00c3fd47']]`
  - `UNCONDITIONAL_JUMP` [`00c3fd44`](#insn-00c3fd44) → [`00c3fdb8`](#insn-00c3fdb8)
- ブロック [`00c3fd48`](#insn-00c3fd48) 範囲 `[['00c3fd48', '00c3fd57']]`
  - `CONDITIONAL_JUMP` [`00c3fd54`](#insn-00c3fd54) → [`00c3fdb4`](#insn-00c3fdb4)
  - `FALL_THROUGH` [`00c3fd54`](#insn-00c3fd54) → [`00c3fd58`](#insn-00c3fd58)
- ブロック [`00c3fd58`](#insn-00c3fd58) 範囲 `[['00c3fd58', '00c3fd63']]`
  - `FALL_THROUGH` [`00c3fd60`](#insn-00c3fd60) → [`00c3fd64`](#insn-00c3fd64)
- ブロック [`00c3fd64`](#insn-00c3fd64) 範囲 `[['00c3fd64', '00c3fd83']]`
  - `CONDITIONAL_JUMP` [`00c3fd80`](#insn-00c3fd80) → [`00c3fd98`](#insn-00c3fd98)
  - `FALL_THROUGH` [`00c3fd80`](#insn-00c3fd80) → [`00c3fd84`](#insn-00c3fd84)
- ブロック [`00c3fd84`](#insn-00c3fd84) 範囲 `[['00c3fd84', '00c3fd97']]`
  - `CONDITIONAL_JUMP` [`00c3fd94`](#insn-00c3fd94) → [`00c3fd64`](#insn-00c3fd64)
  - `FALL_THROUGH` [`00c3fd94`](#insn-00c3fd94) → [`00c3fd98`](#insn-00c3fd98)
- ブロック [`00c3fd98`](#insn-00c3fd98) 範囲 `[['00c3fd98', '00c3fd9f']]`
  - `CONDITIONAL_JUMP` [`00c3fd9c`](#insn-00c3fd9c) → [`00c3fdb4`](#insn-00c3fdb4)
  - `FALL_THROUGH` [`00c3fd9c`](#insn-00c3fd9c) → [`00c3fda0`](#insn-00c3fda0)
- ブロック [`00c3fda0`](#insn-00c3fda0) 範囲 `[['00c3fda0', '00c3fdab']]`
  - `CONDITIONAL_JUMP` [`00c3fda8`](#insn-00c3fda8) → [`00c3fdb4`](#insn-00c3fdb4)
  - `FALL_THROUGH` [`00c3fda8`](#insn-00c3fda8) → [`00c3fdac`](#insn-00c3fdac)
- ブロック [`00c3fdac`](#insn-00c3fdac) 範囲 `[['00c3fdac', '00c3fdb3']]`
  - `UNCONDITIONAL_JUMP` [`00c3fdb0`](#insn-00c3fdb0) → [`00c3fcc4`](#insn-00c3fcc4)
- ブロック [`00c3fdb4`](#insn-00c3fdb4) 範囲 `[['00c3fdb4', '00c3fdb7']]`
  - `FALL_THROUGH` [`00c3fdb4`](#insn-00c3fdb4) → [`00c3fdb8`](#insn-00c3fdb8)
- ブロック [`00c3fdb8`](#insn-00c3fdb8) 範囲 `[['00c3fdb8', '00c3fdd7']]`
- ブロック [`00c3fdd8`](#insn-00c3fdd8) 範囲 `[['00c3fdd8', '00c3fddf']]`
  - `CONDITIONAL_JUMP` [`00c3fddc`](#insn-00c3fddc) → [`00c3fea4`](#insn-00c3fea4)
  - `FALL_THROUGH` [`00c3fddc`](#insn-00c3fddc) → [`00c3fde0`](#insn-00c3fde0)
- ブロック [`00c3fde0`](#insn-00c3fde0) 範囲 `[['00c3fde0', '00c3fde3']]`
  - `CONDITIONAL_JUMP` [`00c3fde0`](#insn-00c3fde0) → [`00c3fea4`](#insn-00c3fea4)
  - `FALL_THROUGH` [`00c3fde0`](#insn-00c3fde0) → [`00c3fde4`](#insn-00c3fde4)
- ブロック [`00c3fde4`](#insn-00c3fde4) 範囲 `[['00c3fde4', '00c3fdf7']]`
  - `CONDITIONAL_JUMP` [`00c3fdf4`](#insn-00c3fdf4) → [`00c3fe20`](#insn-00c3fe20)
  - `FALL_THROUGH` [`00c3fdf4`](#insn-00c3fdf4) → [`00c3fdf8`](#insn-00c3fdf8)
- ブロック [`00c3fdf8`](#insn-00c3fdf8) 範囲 `[['00c3fdf8', '00c3fe07']]`
  - `CONDITIONAL_JUMP` [`00c3fe04`](#insn-00c3fe04) → [`00c3ff88`](#insn-00c3ff88)
  - `FALL_THROUGH` [`00c3fe04`](#insn-00c3fe04) → [`00c3fe08`](#insn-00c3fe08)
- ブロック [`00c3fe08`](#insn-00c3fe08) 範囲 `[['00c3fe08', '00c3fe1b']]`
  - `FALL_THROUGH` [`00c3fe18`](#insn-00c3fe18) → [`00c3fe1c`](#insn-00c3fe1c)
- ブロック [`00c3fe1c`](#insn-00c3fe1c) 範囲 `[['00c3fe1c', '00c3fe1f']]`
  - `FALL_THROUGH` [`00c3fe1c`](#insn-00c3fe1c) → [`00c3fe20`](#insn-00c3fe20)
- ブロック [`00c3fe20`](#insn-00c3fe20) 範囲 `[['00c3fe20', '00c3fe6b']]`
  - `CONDITIONAL_JUMP` [`00c3fe68`](#insn-00c3fe68) → [`00c3ff78`](#insn-00c3ff78)
  - `FALL_THROUGH` [`00c3fe68`](#insn-00c3fe68) → [`00c3fe6c`](#insn-00c3fe6c)
- ブロック [`00c3fe6c`](#insn-00c3fe6c) 範囲 `[['00c3fe6c', '00c3fe87']]`
  - `CONDITIONAL_JUMP` [`00c3fe84`](#insn-00c3fe84) → [`00c3ff38`](#insn-00c3ff38)
  - `FALL_THROUGH` [`00c3fe84`](#insn-00c3fe84) → [`00c3fe88`](#insn-00c3fe88)
- ブロック [`00c3fe88`](#insn-00c3fe88) 範囲 `[['00c3fe88', '00c3fe9f']]`
  - `CONDITIONAL_JUMP` [`00c3fe9c`](#insn-00c3fe9c) → [`00c3ff68`](#insn-00c3ff68)
  - `FALL_THROUGH` [`00c3fe9c`](#insn-00c3fe9c) → [`00c3fea0`](#insn-00c3fea0)
- ブロック [`00c3fea0`](#insn-00c3fea0) 範囲 `[['00c3fea0', '00c3fea3']]`
- ブロック [`00c3fea4`](#insn-00c3fea4) 範囲 `[['00c3fea4', '00c3febb']]`
  - `CONDITIONAL_JUMP` [`00c3feb8`](#insn-00c3feb8) → [`00c3fedc`](#insn-00c3fedc)
  - `FALL_THROUGH` [`00c3feb8`](#insn-00c3feb8) → [`00c3febc`](#insn-00c3febc)
- ブロック [`00c3febc`](#insn-00c3febc) 範囲 `[['00c3febc', '00c3fec3']]`
  - `CONDITIONAL_JUMP` [`00c3fec0`](#insn-00c3fec0) → [`00c3fedc`](#insn-00c3fedc)
  - `FALL_THROUGH` [`00c3fec0`](#insn-00c3fec0) → [`00c3fec4`](#insn-00c3fec4)
- ブロック [`00c3fec4`](#insn-00c3fec4) 範囲 `[['00c3fec4', '00c3fed3']]`
  - `CONDITIONAL_JUMP` [`00c3fed0`](#insn-00c3fed0) → [`00c3fedc`](#insn-00c3fedc)
  - `FALL_THROUGH` [`00c3fed0`](#insn-00c3fed0) → [`00c3fed4`](#insn-00c3fed4)
- ブロック [`00c3fed4`](#insn-00c3fed4) 範囲 `[['00c3fed4', '00c3fedb']]`
  - `UNCONDITIONAL_JUMP` [`00c3fed8`](#insn-00c3fed8) → [`00c3fdb8`](#insn-00c3fdb8)
- ブロック [`00c3fedc`](#insn-00c3fedc) 範囲 `[['00c3fedc', '00c3fee7']]`
  - `CONDITIONAL_JUMP` [`00c3fee4`](#insn-00c3fee4) → [`00c3fdb8`](#insn-00c3fdb8)
  - `FALL_THROUGH` [`00c3fee4`](#insn-00c3fee4) → [`00c3fee8`](#insn-00c3fee8)
- ブロック [`00c3fee8`](#insn-00c3fee8) 範囲 `[['00c3fee8', '00c3fef3']]`
  - `CONDITIONAL_JUMP` [`00c3fef0`](#insn-00c3fef0) → [`00c3fdb8`](#insn-00c3fdb8)
  - `FALL_THROUGH` [`00c3fef0`](#insn-00c3fef0) → [`00c3fef4`](#insn-00c3fef4)
- ブロック [`00c3fef4`](#insn-00c3fef4) 範囲 `[['00c3fef4', '00c3fefb']]`
  - `CONDITIONAL_JUMP` [`00c3fef8`](#insn-00c3fef8) → [`00c3ff14`](#insn-00c3ff14)
  - `FALL_THROUGH` [`00c3fef8`](#insn-00c3fef8) → [`00c3fefc`](#insn-00c3fefc)
- ブロック [`00c3fefc`](#insn-00c3fefc) 範囲 `[['00c3fefc', '00c3ff0f']]`
  - `FALL_THROUGH` [`00c3ff0c`](#insn-00c3ff0c) → [`00c3ff10`](#insn-00c3ff10)
- ブロック [`00c3ff10`](#insn-00c3ff10) 範囲 `[['00c3ff10', '00c3ff13']]`
  - `FALL_THROUGH` [`00c3ff10`](#insn-00c3ff10) → [`00c3ff14`](#insn-00c3ff14)
- ブロック [`00c3ff14`](#insn-00c3ff14) 範囲 `[['00c3ff14', '00c3ff37']]`
- ブロック [`00c3ff38`](#insn-00c3ff38) 範囲 `[['00c3ff38', '00c3ff43']]`
  - `CONDITIONAL_JUMP` [`00c3ff40`](#insn-00c3ff40) → [`00c3ff8c`](#insn-00c3ff8c)
  - `FALL_THROUGH` [`00c3ff40`](#insn-00c3ff40) → [`00c3ff44`](#insn-00c3ff44)
- ブロック [`00c3ff44`](#insn-00c3ff44) 範囲 `[['00c3ff44', '00c3ff4f']]`
  - `CONDITIONAL_JUMP` [`00c3ff4c`](#insn-00c3ff4c) → [`00c3ff60`](#insn-00c3ff60)
  - `FALL_THROUGH` [`00c3ff4c`](#insn-00c3ff4c) → [`00c3ff50`](#insn-00c3ff50)
- ブロック [`00c3ff50`](#insn-00c3ff50) 範囲 `[['00c3ff50', '00c3ff5f']]`
  - `FALL_THROUGH` [`00c3ff5c`](#insn-00c3ff5c) → [`00c3ff60`](#insn-00c3ff60)
- ブロック [`00c3ff60`](#insn-00c3ff60) 範囲 `[['00c3ff60', '00c3ff67']]`
  - `FALL_THROUGH` [`00c3ff64`](#insn-00c3ff64) → [`00c3ff68`](#insn-00c3ff68)
- ブロック [`00c3ff68`](#insn-00c3ff68) 範囲 `[['00c3ff68', '00c3ff77']]`
  - `FALL_THROUGH` [`00c3ff74`](#insn-00c3ff74) → [`00c3ff78`](#insn-00c3ff78)
- ブロック [`00c3ff78`](#insn-00c3ff78) 範囲 `[['00c3ff78', '00c3ff87']]`
  - `UNCONDITIONAL_JUMP` [`00c3ff84`](#insn-00c3ff84) → [`00c3fdb8`](#insn-00c3fdb8)
- ブロック [`00c3ff88`](#insn-00c3ff88) 範囲 `[['00c3ff88', '00c3ff8b']]`
- ブロック [`00c3ff8c`](#insn-00c3ff8c) 範囲 `[['00c3ff8c', '00c3ff8f']]`

## 命令位置別の参照

- [`00c3fbd4`](#insn-00c3fbd4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fbd8`](#insn-00c3fbd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fbdc`](#insn-00c3fbdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fbe0`](#insn-00c3fbe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fbf0`](#insn-00c3fbf0) → [`00c3fdb4`](#insn-00c3fdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fbfc`](#insn-00c3fbfc) → [`00c3fdb4`](#insn-00c3fdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc0c`](#insn-00c3fc0c) → [`00c3fdb4`](#insn-00c3fdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc18`](#insn-00c3fc18) → [`00c3fca8`](#insn-00c3fca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc28`](#insn-00c3fc28) → [`00c3fdb4`](#insn-00c3fdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc38`](#insn-00c3fc38) → [`00c3fdb4`](#insn-00c3fdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc68`](#insn-00c3fc68) → [`00c3fc80`](#insn-00c3fc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc7c`](#insn-00c3fc7c) → [`00c3fc48`](#insn-00c3fc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc84`](#insn-00c3fc84) → [`00c3fdb4`](#insn-00c3fdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fc90`](#insn-00c3fc90) → [`00c3fdb4`](#insn-00c3fdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fca0`](#insn-00c3fca0) → [`00c3fcb4`](#insn-00c3fcb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fca4`](#insn-00c3fca4) → [`00c3fdb4`](#insn-00c3fdb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fcb0`](#insn-00c3fcb0) → [`00c3fdb4`](#insn-00c3fdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fcbc`](#insn-00c3fcbc) → [`00c3fd48`](#insn-00c3fd48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fcd0`](#insn-00c3fcd0) → [`00c3fdd8`](#insn-00c3fdd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fce4`](#insn-00c3fce4) → [`00c3fd08`](#insn-00c3fd08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fcf0`](#insn-00c3fcf0) → [`00c5b0c0`](../00c5b/00c5b0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0c0` · 推定シンボル `None` · 推定型 `None`
- [`00c3fcf4`](#insn-00c3fcf4) → [`00c3ff88`](#insn-00c3ff88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fd20`](#insn-00c3fd20) → `00c986e0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c3fd44`](#insn-00c3fd44) → [`00c3fdb8`](#insn-00c3fdb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fd54`](#insn-00c3fd54) → [`00c3fdb4`](#insn-00c3fdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fd80`](#insn-00c3fd80) → [`00c3fd98`](#insn-00c3fd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fd94`](#insn-00c3fd94) → [`00c3fd64`](#insn-00c3fd64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fd9c`](#insn-00c3fd9c) → [`00c3fdb4`](#insn-00c3fdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fda8`](#insn-00c3fda8) → [`00c3fdb4`](#insn-00c3fdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fdb0`](#insn-00c3fdb0) → [`00c3fcc4`](#insn-00c3fcc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fdbc`](#insn-00c3fdbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fdc0`](#insn-00c3fdc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fdc4`](#insn-00c3fdc4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fdc8`](#insn-00c3fdc8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fddc`](#insn-00c3fddc) → [`00c3fea4`](#insn-00c3fea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fde0`](#insn-00c3fde0) → [`00c3fea4`](#insn-00c3fea4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fdf4`](#insn-00c3fdf4) → [`00c3fe20`](#insn-00c3fe20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fe00`](#insn-00c3fe00) → [`00c5b0c0`](../00c5b/00c5b0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0c0` · 推定シンボル `None` · 推定型 `None`
- [`00c3fe04`](#insn-00c3fe04) → [`00c3ff88`](#insn-00c3ff88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fe38`](#insn-00c3fe38) → `00c987c0`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00c3fe68`](#insn-00c3fe68) → [`00c3ff78`](#insn-00c3ff78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fe84`](#insn-00c3fe84) → [`00c3ff38`](#insn-00c3ff38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fe8c`](#insn-00c3fe8c) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00c3fe9c`](#insn-00c3fe9c) → [`00c3ff68`](#insn-00c3ff68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fea0`](#insn-00c3fea0) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`
- [`00c3feb8`](#insn-00c3feb8) → [`00c3fedc`](#insn-00c3fedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fec0`](#insn-00c3fec0) → [`00c3fedc`](#insn-00c3fedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fed0`](#insn-00c3fed0) → [`00c3fedc`](#insn-00c3fedc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fed8`](#insn-00c3fed8) → [`00c3fdb8`](#insn-00c3fdb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fee4`](#insn-00c3fee4) → [`00c3fdb8`](#insn-00c3fdb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fef0`](#insn-00c3fef0) → [`00c3fdb8`](#insn-00c3fdb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3fef8`](#insn-00c3fef8) → [`00c3ff14`](#insn-00c3ff14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff08`](#insn-00c3ff08) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff0c`](#insn-00c3ff0c) → [`00c40a00`](../00c40/00c40a00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c40a00` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff18`](#insn-00c3ff18) → `002a1d8c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff1c`](#insn-00c3ff1c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff20`](#insn-00c3ff20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff24`](#insn-00c3ff24) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff28`](#insn-00c3ff28) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff34`](#insn-00c3ff34) → [`00c40ad8`](../00c40/00c40ad8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c40ad8` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff3c`](#insn-00c3ff3c) → [`00c5b0c0`](../00c5b/00c5b0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0c0` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff40`](#insn-00c3ff40) → [`00c3ff8c`](#insn-00c3ff8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff4c`](#insn-00c3ff4c) → [`00c3ff60`](#insn-00c3ff60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff5c`](#insn-00c3ff5c) → [`00c58fe0`](../00c58/00c58fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58fe0` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff84`](#insn-00c3ff84) → [`00c3fdb8`](#insn-00c3fdb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff88`](#insn-00c3ff88) → [`00c590c0`](../00c59/00c590c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c590c0` · 推定シンボル `None` · 推定型 `None`
- [`00c3ff8c`](#insn-00c3ff8c) → [`00c5c1e0`](../00c5c/00c5c1e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c1e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c3fbd4`](#insn-00c3fbd4)

~~~json
{
  "source": "00c3fbd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fbd8`](#insn-00c3fbd8)

~~~json
{
  "source": "00c3fbd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fbdc`](#insn-00c3fbdc)

~~~json
{
  "source": "00c3fbdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fbe0`](#insn-00c3fbe0)

~~~json
{
  "source": "00c3fbe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fbf0`](#insn-00c3fbf0)

~~~json
{
  "source": "00c3fbf0",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fbfc`](#insn-00c3fbfc)

~~~json
{
  "source": "00c3fbfc",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc0c`](#insn-00c3fc0c)

~~~json
{
  "source": "00c3fc0c",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc18`](#insn-00c3fc18)

~~~json
{
  "source": "00c3fc18",
  "target": "00c3fca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc28`](#insn-00c3fc28)

~~~json
{
  "source": "00c3fc28",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc38`](#insn-00c3fc38)

~~~json
{
  "source": "00c3fc38",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc68`](#insn-00c3fc68)

~~~json
{
  "source": "00c3fc68",
  "target": "00c3fc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc7c`](#insn-00c3fc7c)

~~~json
{
  "source": "00c3fc7c",
  "target": "00c3fc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc84`](#insn-00c3fc84)

~~~json
{
  "source": "00c3fc84",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fc90`](#insn-00c3fc90)

~~~json
{
  "source": "00c3fc90",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fca0`](#insn-00c3fca0)

~~~json
{
  "source": "00c3fca0",
  "target": "00c3fcb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fca4`](#insn-00c3fca4)

~~~json
{
  "source": "00c3fca4",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fcb0`](#insn-00c3fcb0)

~~~json
{
  "source": "00c3fcb0",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fcbc`](#insn-00c3fcbc)

~~~json
{
  "source": "00c3fcbc",
  "target": "00c3fd48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fcd0`](#insn-00c3fcd0)

~~~json
{
  "source": "00c3fcd0",
  "target": "00c3fdd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fce4`](#insn-00c3fce4)

~~~json
{
  "source": "00c3fce4",
  "target": "00c3fd08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fcf0`](#insn-00c3fcf0)

~~~json
{
  "source": "00c3fcf0",
  "target": "00c5b0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3fcf4`](#insn-00c3fcf4)

~~~json
{
  "source": "00c3fcf4",
  "target": "00c3ff88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fd20`](#insn-00c3fd20)

~~~json
{
  "source": "00c3fd20",
  "target": "00c986e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c986e0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c3fd44`](#insn-00c3fd44)

~~~json
{
  "source": "00c3fd44",
  "target": "00c3fdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fd54`](#insn-00c3fd54)

~~~json
{
  "source": "00c3fd54",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fd80`](#insn-00c3fd80)

~~~json
{
  "source": "00c3fd80",
  "target": "00c3fd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fd94`](#insn-00c3fd94)

~~~json
{
  "source": "00c3fd94",
  "target": "00c3fd64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fd9c`](#insn-00c3fd9c)

~~~json
{
  "source": "00c3fd9c",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fda8`](#insn-00c3fda8)

~~~json
{
  "source": "00c3fda8",
  "target": "00c3fdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fdb0`](#insn-00c3fdb0)

~~~json
{
  "source": "00c3fdb0",
  "target": "00c3fcc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fdbc`](#insn-00c3fdbc)

~~~json
{
  "source": "00c3fdbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fdc0`](#insn-00c3fdc0)

~~~json
{
  "source": "00c3fdc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fdc4`](#insn-00c3fdc4)

~~~json
{
  "source": "00c3fdc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fdc8`](#insn-00c3fdc8)

~~~json
{
  "source": "00c3fdc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fddc`](#insn-00c3fddc)

~~~json
{
  "source": "00c3fddc",
  "target": "00c3fea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fde0`](#insn-00c3fde0)

~~~json
{
  "source": "00c3fde0",
  "target": "00c3fea4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fdf4`](#insn-00c3fdf4)

~~~json
{
  "source": "00c3fdf4",
  "target": "00c3fe20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fe00`](#insn-00c3fe00)

~~~json
{
  "source": "00c3fe00",
  "target": "00c5b0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3fe04`](#insn-00c3fe04)

~~~json
{
  "source": "00c3fe04",
  "target": "00c3ff88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fe38`](#insn-00c3fe38)

~~~json
{
  "source": "00c3fe38",
  "target": "00c987c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c987c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c3fe68`](#insn-00c3fe68)

~~~json
{
  "source": "00c3fe68",
  "target": "00c3ff78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fe84`](#insn-00c3fe84)

~~~json
{
  "source": "00c3fe84",
  "target": "00c3ff38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fe8c`](#insn-00c3fe8c)

~~~json
{
  "source": "00c3fe8c",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3fe9c`](#insn-00c3fe9c)

~~~json
{
  "source": "00c3fe9c",
  "target": "00c3ff68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fea0`](#insn-00c3fea0)

~~~json
{
  "source": "00c3fea0",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3feb8`](#insn-00c3feb8)

~~~json
{
  "source": "00c3feb8",
  "target": "00c3fedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fec0`](#insn-00c3fec0)

~~~json
{
  "source": "00c3fec0",
  "target": "00c3fedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fed0`](#insn-00c3fed0)

~~~json
{
  "source": "00c3fed0",
  "target": "00c3fedc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fed8`](#insn-00c3fed8)

~~~json
{
  "source": "00c3fed8",
  "target": "00c3fdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fee4`](#insn-00c3fee4)

~~~json
{
  "source": "00c3fee4",
  "target": "00c3fdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fef0`](#insn-00c3fef0)

~~~json
{
  "source": "00c3fef0",
  "target": "00c3fdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3fef8`](#insn-00c3fef8)

~~~json
{
  "source": "00c3fef8",
  "target": "00c3ff14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ff08`](#insn-00c3ff08)

~~~json
{
  "source": "00c3ff08",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ff0c`](#insn-00c3ff0c)

~~~json
{
  "source": "00c3ff0c",
  "target": "00c40a00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3ff18`](#insn-00c3ff18)

~~~json
{
  "source": "00c3ff18",
  "target": "002a1d8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ff1c`](#insn-00c3ff1c)

~~~json
{
  "source": "00c3ff1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ff20`](#insn-00c3ff20)

~~~json
{
  "source": "00c3ff20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ff24`](#insn-00c3ff24)

~~~json
{
  "source": "00c3ff24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ff28`](#insn-00c3ff28)

~~~json
{
  "source": "00c3ff28",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ff34`](#insn-00c3ff34)

~~~json
{
  "source": "00c3ff34",
  "target": "00c40ad8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3ff3c`](#insn-00c3ff3c)

~~~json
{
  "source": "00c3ff3c",
  "target": "00c5b0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3ff40`](#insn-00c3ff40)

~~~json
{
  "source": "00c3ff40",
  "target": "00c3ff8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ff4c`](#insn-00c3ff4c)

~~~json
{
  "source": "00c3ff4c",
  "target": "00c3ff60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ff5c`](#insn-00c3ff5c)

~~~json
{
  "source": "00c3ff5c",
  "target": "00c58fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3ff84`](#insn-00c3ff84)

~~~json
{
  "source": "00c3ff84",
  "target": "00c3fdb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c3ff88`](#insn-00c3ff88)

~~~json
{
  "source": "00c3ff88",
  "target": "00c590c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c3ff8c`](#insn-00c3ff8c)

~~~json
{
  "source": "00c3ff8c",
  "target": "00c5c1e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
