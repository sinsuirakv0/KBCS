# 00bc1ccc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bc1c88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bc1/00bc1c88.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-9dfe747c4e38eada18f1082acdaf4641)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c3e714`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3e/00c3e714.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-c28faf93aebd4e76adb103e61e992fc2)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bc1ccc",
  "name": "FUN_00bc1ccc",
  "size": 964,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5140b3ba974a38c08d1026dad10bc9c0f54dc978a27c32ac0fd166195eaf429d",
  "source_text_sha256": "5140b3ba974a38c08d1026dad10bc9c0f54dc978a27c32ac0fd166195eaf429d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bc1ccc",
        "00bc208f"
      ]
    ],
    "bytes_sha256": "30208113c8182d4a4b01c67da0c7512db456bcb4854516efe064b9d5bcdff6b3",
    "instruction_count": 241,
    "instruction_bytes": 964,
    "body_bytes": 964,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbde5c](../00bbd/00bbde5c.md)
- [00bbf39c](../00bbf/00bbf39c.md)
- [00bc2f0c](../00bc2/00bc2f0c.md)
- [00bce7b8](../00bce/00bce7b8.md)

## 呼び出し先

- [00bc2b00](../00bc2/00bc2b00.md)
- [00bc2bd8](../00bc2/00bc2bd8.md)
- [00bdb0f0](../00bdb/00bdb0f0.md)
- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
"auto"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6596 bytes

~~~c

undefined8 * FUN_00bc1ccc(long *param_1)

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
  
                    /* try { // try from 00bc1cd8 to 00cc1d57 has its CatchHandler @ 00bc8b14 */
  pbVar1 = (byte *)*param_1;
  pbVar2 = (byte *)param_1[1];
  if ((pbVar1 != pbVar2) && (*pbVar1 == 0x54)) {
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
                    /* try { // try from 00bc1fa8 to 00cc1fd3 has its CatchHandler @ 00bc8a90 */
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
                FUN_00bc2b00(param_1 + 0x53,&local_48);
              }
                    /* try { // try from 00bc2034 to 00cc203b has its CatchHandler @ 00bc88e0 */
              puVar4 = (undefined8 *)FUN_00bc2bd8(param_1,&DAT_002925bc);
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
LAB_00bc2088:
                    /* WARNING: Subroutine does not return */
              _ZSt9terminatev();
            }
            lVar7 = 0;
            *puVar4 = pvVar14;
            puVar4[1] = 0;
            param_1[0x266] = (long)puVar4;
          }
          *(long *)((long)puVar4 + 8) = lVar7 + 0x30;
          puVar12 = (undefined8 *)((long)puVar4 + lVar7 + 0x10);
          *puVar12 = &PTR_FUN_00c17978;
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
          if (puVar4 == (void *)0x0) goto LAB_00bc2088;
          lVar7 = 0;
          *puVar4 = pvVar14;
          puVar4[1] = 0;
          param_1[0x266] = (long)puVar4;
        }
        *(long *)((long)puVar4 + 8) = lVar7 + 0x20;
        puVar12 = (undefined8 *)((long)puVar4 + lVar7 + 0x10);
        *puVar12 = &PTR_FUN_00c17898;
        *(undefined1 *)((long)puVar4 + lVar7 + 0x18) = 8;
        *(ushort *)((long)puVar4 + lVar7 + 0x19) =
             *(ushort *)((long)puVar4 + lVar7 + 0x19) & 0xf000 | 0x540;
        *(byte **)((long)puVar4 + lVar7 + 0x20) = pbVar1;
        *(long *)((long)puVar4 + lVar7 + 0x28) = (long)pbVar11 - (long)pbVar1;
        return puVar12;
                    /* try { // try from 00bc1e44 to 00cc1ec3 has its CatchHandler @ 00bc8b20 */
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
<a id="insn-00bc1ccc"></a> `00bc1ccc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bc1cd0"></a> `00bc1cd0` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bc1cd4"></a> `00bc1cd4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1cd8"></a> `00bc1cd8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc1cdc"></a> `00bc1cdc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc1ce0"></a> `00bc1ce0` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bc1ce4"></a> `00bc1ce4` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bc1ce8"></a> `00bc1ce8` | `14 20 40 a9` | ldp x20,x8,[x0] | `FALL_THROUGH`
<a id="insn-00bc1cec"></a> `00bc1cec` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00bc1cf0"></a> `00bc1cf0` | `20 0e 00 54` | b.eq 0x00bc1eb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1cf4"></a> `00bc1cf4` | `89 02 40 39` | ldrb w9,[x20] | `FALL_THROUGH`
<a id="insn-00bc1cf8"></a> `00bc1cf8` | `3f 51 01 71` | cmp w9,#0x54 | `FALL_THROUGH`
<a id="insn-00bc1cfc"></a> `00bc1cfc` | `c1 0d 00 54` | b.ne 0x00bc1eb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1d00"></a> `00bc1d00` | `95 06 00 91` | add x21,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bc1d04"></a> `00bc1d04` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bc1d08"></a> `00bc1d08` | `15 00 00 f9` | str x21,[x0] | `FALL_THROUGH`
<a id="insn-00bc1d0c"></a> `00bc1d0c` | `40 0d 00 54` | b.eq 0x00bc1eb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1d10"></a> `00bc1d10` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bc1d14"></a> `00bc1d14` | `3f 31 01 71` | cmp w9,#0x4c | `FALL_THROUGH`
<a id="insn-00bc1d18"></a> `00bc1d18` | `81 04 00 54` | b.ne 0x00bc1da8 | `CONDITIONAL_JUMP`
<a id="insn-00bc1d1c"></a> `00bc1d1c` | `89 0a 00 91` | add x9,x20,#0x2 | `FALL_THROUGH`
<a id="insn-00bc1d20"></a> `00bc1d20` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bc1d24"></a> `00bc1d24` | `09 00 00 f9` | str x9,[x0] | `FALL_THROUGH`
<a id="insn-00bc1d28"></a> `00bc1d28` | `60 0c 00 54` | b.eq 0x00bc1eb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1d2c"></a> `00bc1d2c` | `29 01 40 39` | ldrb w9,[x9] | `FALL_THROUGH`
<a id="insn-00bc1d30"></a> `00bc1d30` | `29 e9 00 51` | sub w9,w9,#0x3a | `FALL_THROUGH`
<a id="insn-00bc1d34"></a> `00bc1d34` | `3f 29 00 31` | cmn w9,#0xa | `FALL_THROUGH`
<a id="insn-00bc1d38"></a> `00bc1d38` | `e3 0b 00 54` | b.cc 0x00bc1eb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1d3c"></a> `00bc1d3c` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00bc1d40"></a> `00bc1d40` | `8c 12 00 91` | add x12,x20,#0x4 | `FALL_THROUGH`
<a id="insn-00bc1d44"></a> `00bc1d44` | `4a 01 80 52` | mov w10,#0xa | `FALL_THROUGH`
<a id="insn-00bc1d48"></a> `00bc1d48` | `8b 05 00 d1` | sub x11,x12,#0x1 | `FALL_THROUGH`
<a id="insn-00bc1d4c"></a> `00bc1d4c` | `f5 03 0c aa` | mov x21,x12 | `FALL_THROUGH`
<a id="insn-00bc1d50"></a> `00bc1d50` | `0b 00 00 f9` | str x11,[x0] | `FALL_THROUGH`
<a id="insn-00bc1d54"></a> `00bc1d54` | `7f 01 08 eb` | cmp x11,x8 | `FALL_THROUGH`
<a id="insn-00bc1d58"></a> `00bc1d58` | `8c e1 5f 38` | ldurb w12,[x12, #-0x2] | `FALL_THROUGH`
<a id="insn-00bc1d5c"></a> `00bc1d5c` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bc1d60"></a> `00bc1d60` | `29 31 0a 9b` | madd x9,x9,x10,x12 | `FALL_THROUGH`
<a id="insn-00bc1d64"></a> `00bc1d64` | `29 c1 00 d1` | sub x9,x9,#0x30 | `FALL_THROUGH`
<a id="insn-00bc1d68"></a> `00bc1d68` | `c0 00 00 54` | b.eq 0x00bc1d80 | `CONDITIONAL_JUMP`
<a id="insn-00bc1d6c"></a> `00bc1d6c` | `ac f2 5f 38` | ldurb w12,[x21, #-0x1] | `FALL_THROUGH`
<a id="insn-00bc1d70"></a> `00bc1d70` | `8c c1 00 51` | sub w12,w12,#0x30 | `FALL_THROUGH`
<a id="insn-00bc1d74"></a> `00bc1d74` | `9f 25 00 71` | cmp w12,#0x9 | `FALL_THROUGH`
<a id="insn-00bc1d78"></a> `00bc1d78` | `ac 06 00 91` | add x12,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bc1d7c"></a> `00bc1d7c` | `69 fe ff 54` | b.ls 0x00bc1d48 | `CONDITIONAL_JUMP`
<a id="insn-00bc1d80"></a> `00bc1d80` | `7f 01 08 eb` | cmp x11,x8 | `FALL_THROUGH`
<a id="insn-00bc1d84"></a> `00bc1d84` | `80 09 00 54` | b.eq 0x00bc1eb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1d88"></a> `00bc1d88` | `aa f2 5f 38` | ldurb w10,[x21, #-0x1] | `FALL_THROUGH`
<a id="insn-00bc1d8c"></a> `00bc1d8c` | `5f 7d 01 71` | cmp w10,#0x5f | `FALL_THROUGH`
<a id="insn-00bc1d90"></a> `00bc1d90` | `21 09 00 54` | b.ne 0x00bc1eb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1d94"></a> `00bc1d94` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bc1d98"></a> `00bc1d98` | `15 00 00 f9` | str x21,[x0] | `FALL_THROUGH`
<a id="insn-00bc1d9c"></a> `00bc1d9c` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bc1da0"></a> `00bc1da0` | `a1 00 00 54` | b.ne 0x00bc1db4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1da4"></a> `00bc1da4` | `44 00 00 14` | b 0x00bc1eb4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc1da8"></a> `00bc1da8` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00bc1dac"></a> `00bc1dac` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bc1db0"></a> `00bc1db0` | `20 08 00 54` | b.eq 0x00bc1eb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1db4"></a> `00bc1db4` | `aa 02 40 39` | ldrb w10,[x21] | `FALL_THROUGH`
<a id="insn-00bc1db8"></a> `00bc1db8` | `5f 7d 01 71` | cmp w10,#0x5f | `FALL_THROUGH`
<a id="insn-00bc1dbc"></a> `00bc1dbc` | `61 04 00 54` | b.ne 0x00bc1e48 | `CONDITIONAL_JUMP`
<a id="insn-00bc1dc0"></a> `00bc1dc0` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00bc1dc4"></a> `00bc1dc4` | `08 28 4c 39` | ldrb w8,[x0, #0x30a] | `FALL_THROUGH`
<a id="insn-00bc1dc8"></a> `00bc1dc8` | `aa 06 00 91` | add x10,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bc1dcc"></a> `00bc1dcc` | `0a 00 00 f9` | str x10,[x0] | `FALL_THROUGH`
<a id="insn-00bc1dd0"></a> `00bc1dd0` | `48 08 00 34` | cbz w8,0x00bc1ed8 | `CONDITIONAL_JUMP`
<a id="insn-00bc1dd4"></a> `00bc1dd4` | `16 98 49 f9` | ldr x22,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc1dd8"></a> `00bc1dd8` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bc1ddc"></a> `00bc1ddc` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bc1de0"></a> `00bc1de0` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bc1de4"></a> `00bc1de4` | `28 01 00 54` | b.hi 0x00bc1e08 | `CONDITIONAL_JUMP`
<a id="insn-00bc1de8"></a> `00bc1de8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc1dec"></a> `00bc1dec` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bc1df0"></a> `00bc1df0` | `f8 6c 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc1df4"></a> `00bc1df4` | `a0 14 00 b4` | cbz x0,0x00bc2088 | `CONDITIONAL_JUMP`
<a id="insn-00bc1df8"></a> `00bc1df8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bc1dfc"></a> `00bc1dfc` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bc1e00"></a> `00bc1e00` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bc1e04"></a> `00bc1e04` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc1e08"></a> `00bc1e08` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bc1e0c"></a> `00bc1e0c` | `d3 02 08 8b` | add x19,x22,x8 | `FALL_THROUGH`
<a id="insn-00bc1e10"></a> `00bc1e10` | `a8 02 00 d0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bc1e14"></a> `00bc1e14` | `08 61 22 91` | add x8,x8,#0x898 | `FALL_THROUGH`
<a id="insn-00bc1e18"></a> `00bc1e18` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bc1e1c"></a> `00bc1e1c` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bc1e20"></a> `00bc1e20` | `68 0e 01 f8` | str x8,[x19, #0x10]! | `FALL_THROUGH`
<a id="insn-00bc1e24"></a> `00bc1e24` | `68 92 40 78` | ldurh w8,[x19, #0x9] | `FALL_THROUGH`
<a id="insn-00bc1e28"></a> `00bc1e28` | `09 01 80 52` | mov w9,#0x8 | `FALL_THROUGH`
<a id="insn-00bc1e2c"></a> `00bc1e2c` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bc1e30"></a> `00bc1e30` | `69 22 00 39` | strb w9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc1e34"></a> `00bc1e34` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bc1e38"></a> `00bc1e38` | `68 92 00 78` | sturh w8,[x19, #0x9] | `FALL_THROUGH`
<a id="insn-00bc1e3c"></a> `00bc1e3c` | `a8 02 14 cb` | sub x8,x21,x20 | `FALL_THROUGH`
<a id="insn-00bc1e40"></a> `00bc1e40` | `74 22 01 a9` | stp x20,x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1e44"></a> `00bc1e44` | `1d 00 00 14` | b 0x00bc1eb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc1e48"></a> `00bc1e48` | `aa 02 40 39` | ldrb w10,[x21] | `FALL_THROUGH`
<a id="insn-00bc1e4c"></a> `00bc1e4c` | `4a e9 00 51` | sub w10,w10,#0x3a | `FALL_THROUGH`
<a id="insn-00bc1e50"></a> `00bc1e50` | `5f 29 00 31` | cmn w10,#0xa | `FALL_THROUGH`
<a id="insn-00bc1e54"></a> `00bc1e54` | `03 03 00 54` | b.cc 0x00bc1eb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1e58"></a> `00bc1e58` | `ea 03 1f aa` | mov x10,xzr | `FALL_THROUGH`
<a id="insn-00bc1e5c"></a> `00bc1e5c` | `ac 06 00 91` | add x12,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bc1e60"></a> `00bc1e60` | `4b 01 80 52` | mov w11,#0xa | `FALL_THROUGH`
<a id="insn-00bc1e64"></a> `00bc1e64` | `0c 00 00 f9` | str x12,[x0] | `FALL_THROUGH`
<a id="insn-00bc1e68"></a> `00bc1e68` | `f5 03 0c aa` | mov x21,x12 | `FALL_THROUGH`
<a id="insn-00bc1e6c"></a> `00bc1e6c` | `8c f1 5f 38` | ldurb w12,[x12, #-0x1] | `FALL_THROUGH`
<a id="insn-00bc1e70"></a> `00bc1e70` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bc1e74"></a> `00bc1e74` | `4a 31 0b 9b` | madd x10,x10,x11,x12 | `FALL_THROUGH`
<a id="insn-00bc1e78"></a> `00bc1e78` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bc1e7c"></a> `00bc1e7c` | `4a c1 00 d1` | sub x10,x10,#0x30 | `FALL_THROUGH`
<a id="insn-00bc1e80"></a> `00bc1e80` | `c0 00 00 54` | b.eq 0x00bc1e98 | `CONDITIONAL_JUMP`
<a id="insn-00bc1e84"></a> `00bc1e84` | `ec 03 15 aa` | mov x12,x21 | `FALL_THROUGH`
<a id="insn-00bc1e88"></a> `00bc1e88` | `8d 15 40 38` | ldrb w13,[x12], #0x1 | `FALL_THROUGH`
<a id="insn-00bc1e8c"></a> `00bc1e8c` | `ad c1 00 51` | sub w13,w13,#0x30 | `FALL_THROUGH`
<a id="insn-00bc1e90"></a> `00bc1e90` | `bf 25 00 71` | cmp w13,#0x9 | `FALL_THROUGH`
<a id="insn-00bc1e94"></a> `00bc1e94` | `89 fe ff 54` | b.ls 0x00bc1e64 | `CONDITIONAL_JUMP`
<a id="insn-00bc1e98"></a> `00bc1e98` | `bf 02 08 eb` | cmp x21,x8 | `FALL_THROUGH`
<a id="insn-00bc1e9c"></a> `00bc1e9c` | `c0 00 00 54` | b.eq 0x00bc1eb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1ea0"></a> `00bc1ea0` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bc1ea4"></a> `00bc1ea4` | `1f 7d 01 71` | cmp w8,#0x5f | `FALL_THROUGH`
<a id="insn-00bc1ea8"></a> `00bc1ea8` | `61 00 00 54` | b.ne 0x00bc1eb4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1eac"></a> `00bc1eac` | `56 05 00 91` | add x22,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bc1eb0"></a> `00bc1eb0` | `c5 ff ff 17` | b 0x00bc1dc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc1eb4"></a> `00bc1eb4` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00bc1eb8"></a> `00bc1eb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc1ebc"></a> `00bc1ebc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bc1ec0"></a> `00bc1ec0` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc1ec4"></a> `00bc1ec4` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc1ec8"></a> `00bc1ec8` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1ecc"></a> `00bc1ecc` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bc1ed0"></a> `00bc1ed0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bc1ed4"></a> `00bc1ed4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bc1ed8"></a> `00bc1ed8` | `08 24 4c 39` | ldrb w8,[x0, #0x309] | `FALL_THROUGH`
<a id="insn-00bc1edc"></a> `00bc1edc` | `48 06 00 34` | cbz w8,0x00bc1fa4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1ee0"></a> `00bc1ee0` | `29 06 00 b5` | cbnz x9,0x00bc1fa4 | `CONDITIONAL_JUMP`
<a id="insn-00bc1ee4"></a> `00bc1ee4` | `13 98 49 f9` | ldr x19,[x0, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc1ee8"></a> `00bc1ee8` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc1eec"></a> `00bc1eec` | `28 01 3f d1` | sub x8,x9,#0xfc0 | `FALL_THROUGH`
<a id="insn-00bc1ef0"></a> `00bc1ef0` | `1f c5 3f b1` | cmn x8,#0xff1 | `FALL_THROUGH`
<a id="insn-00bc1ef4"></a> `00bc1ef4` | `68 01 00 54` | b.hi 0x00bc1f20 | `CONDITIONAL_JUMP`
<a id="insn-00bc1ef8"></a> `00bc1ef8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bc1efc"></a> `00bc1efc` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bc1f00"></a> `00bc1f00` | `b4 6c 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc1f04"></a> `00bc1f04` | `20 0c 00 b4` | cbz x0,0x00bc2088 | `CONDITIONAL_JUMP`
<a id="insn-00bc1f08"></a> `00bc1f08` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00bc1f0c"></a> `00bc1f0c` | `e9 03 1f aa` | mov x9,xzr | `FALL_THROUGH`
<a id="insn-00bc1f10"></a> `00bc1f10` | `13 7c 00 a9` | stp x19,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bc1f14"></a> `00bc1f14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc1f18"></a> `00bc1f18` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bc1f1c"></a> `00bc1f1c` | `88 9a 09 f9` | str x8,[x20, #0x1330] | `FALL_THROUGH`
<a id="insn-00bc1f20"></a> `00bc1f20` | `28 c1 00 91` | add x8,x9,#0x30 | `FALL_THROUGH`
<a id="insn-00bc1f24"></a> `00bc1f24` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc1f28"></a> `00bc1f28` | `73 02 09 8b` | add x19,x19,x9 | `FALL_THROUGH`
<a id="insn-00bc1f2c"></a> `00bc1f2c` | `a8 02 00 d0` | adrp x8,0xc17000 | `FALL_THROUGH`
<a id="insn-00bc1f30"></a> `00bc1f30` | `08 e1 25 91` | add x8,x8,#0x978 | `FALL_THROUGH`
<a id="insn-00bc1f34"></a> `00bc1f34` | `09 50 81 52` | mov w9,#0xa80 | `FALL_THROUGH`
<a id="insn-00bc1f38"></a> `00bc1f38` | `68 0e 01 f8` | str x8,[x19, #0x10]! | `FALL_THROUGH`
<a id="insn-00bc1f3c"></a> `00bc1f3c` | `68 92 40 78` | ldurh w8,[x19, #0x9] | `FALL_THROUGH`
<a id="insn-00bc1f40"></a> `00bc1f40` | `76 7e 01 a9` | stp x22,xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bc1f44"></a> `00bc1f44` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bc1f48"></a> `00bc1f48` | `7f 82 00 39` | strb wzr,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bc1f4c"></a> `00bc1f4c` | `08 01 09 2a` | orr w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00bc1f50"></a> `00bc1f50` | `89 05 80 52` | mov w9,#0x2c | `FALL_THROUGH`
<a id="insn-00bc1f54"></a> `00bc1f54` | `68 92 00 78` | sturh w8,[x19, #0x9] | `FALL_THROUGH`
<a id="insn-00bc1f58"></a> `00bc1f58` | `17 6c 41 f9` | ldr x23,[x0, #0x2d8] | `FALL_THROUGH`
<a id="insn-00bc1f5c"></a> `00bc1f5c` | `08 70 41 f9` | ldr x8,[x0, #0x2e0] | `FALL_THROUGH`
<a id="insn-00bc1f60"></a> `00bc1f60` | `69 22 00 39` | strb w9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bc1f64"></a> `00bc1f64` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00bc1f68"></a> `00bc1f68` | `81 08 00 54` | b.ne 0x00bc2078 | `CONDITIONAL_JUMP`
<a id="insn-00bc1f6c"></a> `00bc1f6c` | `16 68 41 f9` | ldr x22,[x0, #0x2d0] | `FALL_THROUGH`
<a id="insn-00bc1f70"></a> `00bc1f70` | `08 a0 0b 91` | add x8,x0,#0x2e8 | `FALL_THROUGH`
<a id="insn-00bc1f74"></a> `00bc1f74` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bc1f78"></a> `00bc1f78` | `f4 02 16 cb` | sub x20,x23,x22 | `FALL_THROUGH`
<a id="insn-00bc1f7c"></a> `00bc1f7c` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bc1f80"></a> `00bc1f80` | `81 fa 7f d3` | lsl x1,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00bc1f84"></a> `00bc1f84` | `a0 05 00 54` | b.eq 0x00bc2038 | `CONDITIONAL_JUMP`
<a id="insn-00bc1f88"></a> `00bc1f88` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bc1f8c"></a> `00bc1f8c` | `b1 6c 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bc1f90"></a> `00bc1f90` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bc1f94"></a> `00bc1f94` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bc1f98"></a> `00bc1f98` | `15 6b 01 f9` | str x21,[x24, #0x2d0] | `FALL_THROUGH`
<a id="insn-00bc1f9c"></a> `00bc1f9c` | `75 06 00 b5` | cbnz x21,0x00bc2068 | `CONDITIONAL_JUMP`
<a id="insn-00bc1fa0"></a> `00bc1fa0` | `c8 70 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bc1fa4"></a> `00bc1fa4` | `08 50 41 f9` | ldr x8,[x0, #0x2a0] | `FALL_THROUGH`
<a id="insn-00bc1fa8"></a> `00bc1fa8` | `0a 4c 41 f9` | ldr x10,[x0, #0x298] | `FALL_THROUGH`
<a id="insn-00bc1fac"></a> `00bc1fac` | `08 01 0a cb` | sub x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00bc1fb0"></a> `00bc1fb0` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bc1fb4"></a> `00bc1fb4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc1fb8"></a> `00bc1fb8` | `22 01 00 54` | b.cs 0x00bc1fdc | `CONDITIONAL_JUMP`
<a id="insn-00bc1fbc"></a> `00bc1fbc` | `4a 79 69 f8` | ldr x10,[x10, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bc1fc0"></a> `00bc1fc0` | `ea 00 00 b4` | cbz x10,0x00bc1fdc | `CONDITIONAL_JUMP`
<a id="insn-00bc1fc4"></a> `00bc1fc4` | `4a 2d 40 a9` | ldp x10,x11,[x10] | `FALL_THROUGH`
<a id="insn-00bc1fc8"></a> `00bc1fc8` | `6b 01 0a cb` | sub x11,x11,x10 | `FALL_THROUGH`
<a id="insn-00bc1fcc"></a> `00bc1fcc` | `df 0e 8b eb` | cmp x22,x11, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00bc1fd0"></a> `00bc1fd0` | `62 00 00 54` | b.cs 0x00bc1fdc | `CONDITIONAL_JUMP`
<a id="insn-00bc1fd4"></a> `00bc1fd4` | `53 79 76 f8` | ldr x19,[x10, x22, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00bc1fd8"></a> `00bc1fd8` | `b8 ff ff 17` | b 0x00bc1eb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc1fdc"></a> `00bc1fdc` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc1fe0"></a> `00bc1fe0` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00bc1fe4"></a> `00bc1fe4` | `a8 f6 ff 54` | b.hi 0x00bc1eb8 | `CONDITIONAL_JUMP`
<a id="insn-00bc1fe8"></a> `00bc1fe8` | `0a 88 41 f9` | ldr x10,[x0, #0x310] | `FALL_THROUGH`
<a id="insn-00bc1fec"></a> `00bc1fec` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bc1ff0"></a> `00bc1ff0` | `41 f6 ff 54` | b.ne 0x00bc1eb8 | `CONDITIONAL_JUMP`
<a id="insn-00bc1ff4"></a> `00bc1ff4` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bc1ff8"></a> `00bc1ff8` | `e1 00 00 54` | b.ne 0x00bc2014 | `CONDITIONAL_JUMP`
<a id="insn-00bc1ffc"></a> `00bc1ffc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bc2000"></a> `00bc2000` | `00 60 0a 91` | add x0,x0,#0x298 | `FALL_THROUGH`
<a id="insn-00bc2004"></a> `00bc2004` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bc2008"></a> `00bc2008` | `ff 07 00 f9` | str xzr,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bc200c"></a> `00bc200c` | `bd 02 00 94` | bl 0x00bc2b00 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2010"></a> `00bc2010` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bc2014"></a> `00bc2014` | `81 b6 ff 90` | adrp x1,0x292000 | `FALL_THROUGH`
<a id="insn-00bc2018"></a> `00bc2018` | `21 f0 16 91` | add x1,x1,#0x5bc | `FALL_THROUGH`
<a id="insn-00bc201c"></a> `00bc201c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bc2020"></a> `00bc2020` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bc2024"></a> `00bc2024` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bc2028"></a> `00bc2028` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bc202c"></a> `00bc202c` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bc2030"></a> `00bc2030` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bc2034"></a> `00bc2034` | `e9 02 00 14` | b 0x00bc2bd8 | `CALL_TERMINATOR`
<a id="insn-00bc2038"></a> `00bc2038` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bc203c"></a> `00bc203c` | `65 6c 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2040"></a> `00bc2040` | `60 02 00 b4` | cbz x0,0x00bc208c | `CONDITIONAL_JUMP`
<a id="insn-00bc2044"></a> `00bc2044` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bc2048"></a> `00bc2048` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00bc204c"></a> `00bc204c` | `a0 00 00 54` | b.eq 0x00bc2060 | `CONDITIONAL_JUMP`
<a id="insn-00bc2050"></a> `00bc2050` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bc2054"></a> `00bc2054` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bc2058"></a> `00bc2058` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bc205c"></a> `00bc205c` | `25 64 00 94` | bl 0x00bdb0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bc2060"></a> `00bc2060` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bc2064"></a> `00bc2064` | `15 6b 01 f9` | str x21,[x24, #0x2d0] | `FALL_THROUGH`
<a id="insn-00bc2068"></a> `00bc2068` | `88 fe 42 93` | asr x8,x20,#0x2 | `FALL_THROUGH`
<a id="insn-00bc206c"></a> `00bc206c` | `b7 02 14 8b` | add x23,x21,x20 | `FALL_THROUGH`
<a id="insn-00bc2070"></a> `00bc2070` | `a8 0e 08 8b` | add x8,x21,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bc2074"></a> `00bc2074` | `08 70 01 f9` | str x8,[x0, #0x2e0] | `FALL_THROUGH`
<a id="insn-00bc2078"></a> `00bc2078` | `e8 22 00 91` | add x8,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00bc207c"></a> `00bc207c` | `08 6c 01 f9` | str x8,[x0, #0x2d8] | `FALL_THROUGH`
<a id="insn-00bc2080"></a> `00bc2080` | `f3 02 00 f9` | str x19,[x23] | `FALL_THROUGH`
<a id="insn-00bc2084"></a> `00bc2084` | `8d ff ff 17` | b 0x00bc1eb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bc2088"></a> `00bc2088` | `52 64 00 94` | bl 0x00bdb1d0 | `CALL_TERMINATOR`
<a id="insn-00bc208c"></a> `00bc208c` | `8d 70 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bc1ccc`](#insn-00bc1ccc) 範囲 `[['00bc1ccc', '00bc1cd7']]`
  - `FALL_THROUGH` [`00bc1cd4`](#insn-00bc1cd4) → [`00bc1cd8`](#insn-00bc1cd8)
- ブロック [`00bc1cd8`](#insn-00bc1cd8) 範囲 `[['00bc1cd8', '00bc1cf3']]`
  - `CONDITIONAL_JUMP` [`00bc1cf0`](#insn-00bc1cf0) → [`00bc1eb4`](#insn-00bc1eb4)
  - `FALL_THROUGH` [`00bc1cf0`](#insn-00bc1cf0) → [`00bc1cf4`](#insn-00bc1cf4)
- ブロック [`00bc1cf4`](#insn-00bc1cf4) 範囲 `[['00bc1cf4', '00bc1cff']]`
  - `CONDITIONAL_JUMP` [`00bc1cfc`](#insn-00bc1cfc) → [`00bc1eb4`](#insn-00bc1eb4)
  - `FALL_THROUGH` [`00bc1cfc`](#insn-00bc1cfc) → [`00bc1d00`](#insn-00bc1d00)
- ブロック [`00bc1d00`](#insn-00bc1d00) 範囲 `[['00bc1d00', '00bc1d0f']]`
  - `CONDITIONAL_JUMP` [`00bc1d0c`](#insn-00bc1d0c) → [`00bc1eb4`](#insn-00bc1eb4)
  - `FALL_THROUGH` [`00bc1d0c`](#insn-00bc1d0c) → [`00bc1d10`](#insn-00bc1d10)
- ブロック [`00bc1d10`](#insn-00bc1d10) 範囲 `[['00bc1d10', '00bc1d1b']]`
  - `CONDITIONAL_JUMP` [`00bc1d18`](#insn-00bc1d18) → [`00bc1da8`](#insn-00bc1da8)
  - `FALL_THROUGH` [`00bc1d18`](#insn-00bc1d18) → [`00bc1d1c`](#insn-00bc1d1c)
- ブロック [`00bc1d1c`](#insn-00bc1d1c) 範囲 `[['00bc1d1c', '00bc1d2b']]`
  - `CONDITIONAL_JUMP` [`00bc1d28`](#insn-00bc1d28) → [`00bc1eb4`](#insn-00bc1eb4)
  - `FALL_THROUGH` [`00bc1d28`](#insn-00bc1d28) → [`00bc1d2c`](#insn-00bc1d2c)
- ブロック [`00bc1d2c`](#insn-00bc1d2c) 範囲 `[['00bc1d2c', '00bc1d3b']]`
  - `CONDITIONAL_JUMP` [`00bc1d38`](#insn-00bc1d38) → [`00bc1eb4`](#insn-00bc1eb4)
  - `FALL_THROUGH` [`00bc1d38`](#insn-00bc1d38) → [`00bc1d3c`](#insn-00bc1d3c)
- ブロック [`00bc1d3c`](#insn-00bc1d3c) 範囲 `[['00bc1d3c', '00bc1d47']]`
  - `FALL_THROUGH` [`00bc1d44`](#insn-00bc1d44) → [`00bc1d48`](#insn-00bc1d48)
- ブロック [`00bc1d48`](#insn-00bc1d48) 範囲 `[['00bc1d48', '00bc1d6b']]`
  - `CONDITIONAL_JUMP` [`00bc1d68`](#insn-00bc1d68) → [`00bc1d80`](#insn-00bc1d80)
  - `FALL_THROUGH` [`00bc1d68`](#insn-00bc1d68) → [`00bc1d6c`](#insn-00bc1d6c)
- ブロック [`00bc1d6c`](#insn-00bc1d6c) 範囲 `[['00bc1d6c', '00bc1d7f']]`
  - `CONDITIONAL_JUMP` [`00bc1d7c`](#insn-00bc1d7c) → [`00bc1d48`](#insn-00bc1d48)
  - `FALL_THROUGH` [`00bc1d7c`](#insn-00bc1d7c) → [`00bc1d80`](#insn-00bc1d80)
- ブロック [`00bc1d80`](#insn-00bc1d80) 範囲 `[['00bc1d80', '00bc1d87']]`
  - `CONDITIONAL_JUMP` [`00bc1d84`](#insn-00bc1d84) → [`00bc1eb4`](#insn-00bc1eb4)
  - `FALL_THROUGH` [`00bc1d84`](#insn-00bc1d84) → [`00bc1d88`](#insn-00bc1d88)
- ブロック [`00bc1d88`](#insn-00bc1d88) 範囲 `[['00bc1d88', '00bc1d93']]`
  - `CONDITIONAL_JUMP` [`00bc1d90`](#insn-00bc1d90) → [`00bc1eb4`](#insn-00bc1eb4)
  - `FALL_THROUGH` [`00bc1d90`](#insn-00bc1d90) → [`00bc1d94`](#insn-00bc1d94)
- ブロック [`00bc1d94`](#insn-00bc1d94) 範囲 `[['00bc1d94', '00bc1da3']]`
  - `CONDITIONAL_JUMP` [`00bc1da0`](#insn-00bc1da0) → [`00bc1db4`](#insn-00bc1db4)
  - `FALL_THROUGH` [`00bc1da0`](#insn-00bc1da0) → [`00bc1da4`](#insn-00bc1da4)
- ブロック [`00bc1da4`](#insn-00bc1da4) 範囲 `[['00bc1da4', '00bc1da7']]`
  - `UNCONDITIONAL_JUMP` [`00bc1da4`](#insn-00bc1da4) → [`00bc1eb4`](#insn-00bc1eb4)
- ブロック [`00bc1da8`](#insn-00bc1da8) 範囲 `[['00bc1da8', '00bc1db3']]`
  - `CONDITIONAL_JUMP` [`00bc1db0`](#insn-00bc1db0) → [`00bc1eb4`](#insn-00bc1eb4)
  - `FALL_THROUGH` [`00bc1db0`](#insn-00bc1db0) → [`00bc1db4`](#insn-00bc1db4)
- ブロック [`00bc1db4`](#insn-00bc1db4) 範囲 `[['00bc1db4', '00bc1dbf']]`
  - `CONDITIONAL_JUMP` [`00bc1dbc`](#insn-00bc1dbc) → [`00bc1e48`](#insn-00bc1e48)
  - `FALL_THROUGH` [`00bc1dbc`](#insn-00bc1dbc) → [`00bc1dc0`](#insn-00bc1dc0)
- ブロック [`00bc1dc0`](#insn-00bc1dc0) 範囲 `[['00bc1dc0', '00bc1dc3']]`
  - `FALL_THROUGH` [`00bc1dc0`](#insn-00bc1dc0) → [`00bc1dc4`](#insn-00bc1dc4)
- ブロック [`00bc1dc4`](#insn-00bc1dc4) 範囲 `[['00bc1dc4', '00bc1dd3']]`
  - `CONDITIONAL_JUMP` [`00bc1dd0`](#insn-00bc1dd0) → [`00bc1ed8`](#insn-00bc1ed8)
  - `FALL_THROUGH` [`00bc1dd0`](#insn-00bc1dd0) → [`00bc1dd4`](#insn-00bc1dd4)
- ブロック [`00bc1dd4`](#insn-00bc1dd4) 範囲 `[['00bc1dd4', '00bc1de7']]`
  - `CONDITIONAL_JUMP` [`00bc1de4`](#insn-00bc1de4) → [`00bc1e08`](#insn-00bc1e08)
  - `FALL_THROUGH` [`00bc1de4`](#insn-00bc1de4) → [`00bc1de8`](#insn-00bc1de8)
- ブロック [`00bc1de8`](#insn-00bc1de8) 範囲 `[['00bc1de8', '00bc1df7']]`
  - `CONDITIONAL_JUMP` [`00bc1df4`](#insn-00bc1df4) → [`00bc2088`](#insn-00bc2088)
  - `FALL_THROUGH` [`00bc1df4`](#insn-00bc1df4) → [`00bc1df8`](#insn-00bc1df8)
- ブロック [`00bc1df8`](#insn-00bc1df8) 範囲 `[['00bc1df8', '00bc1e07']]`
  - `FALL_THROUGH` [`00bc1e04`](#insn-00bc1e04) → [`00bc1e08`](#insn-00bc1e08)
- ブロック [`00bc1e08`](#insn-00bc1e08) 範囲 `[['00bc1e08', '00bc1e43']]`
  - `FALL_THROUGH` [`00bc1e40`](#insn-00bc1e40) → [`00bc1e44`](#insn-00bc1e44)
- ブロック [`00bc1e44`](#insn-00bc1e44) 範囲 `[['00bc1e44', '00bc1e47']]`
  - `UNCONDITIONAL_JUMP` [`00bc1e44`](#insn-00bc1e44) → [`00bc1eb8`](#insn-00bc1eb8)
- ブロック [`00bc1e48`](#insn-00bc1e48) 範囲 `[['00bc1e48', '00bc1e57']]`
  - `CONDITIONAL_JUMP` [`00bc1e54`](#insn-00bc1e54) → [`00bc1eb4`](#insn-00bc1eb4)
  - `FALL_THROUGH` [`00bc1e54`](#insn-00bc1e54) → [`00bc1e58`](#insn-00bc1e58)
- ブロック [`00bc1e58`](#insn-00bc1e58) 範囲 `[['00bc1e58', '00bc1e63']]`
  - `FALL_THROUGH` [`00bc1e60`](#insn-00bc1e60) → [`00bc1e64`](#insn-00bc1e64)
- ブロック [`00bc1e64`](#insn-00bc1e64) 範囲 `[['00bc1e64', '00bc1e83']]`
  - `CONDITIONAL_JUMP` [`00bc1e80`](#insn-00bc1e80) → [`00bc1e98`](#insn-00bc1e98)
  - `FALL_THROUGH` [`00bc1e80`](#insn-00bc1e80) → [`00bc1e84`](#insn-00bc1e84)
- ブロック [`00bc1e84`](#insn-00bc1e84) 範囲 `[['00bc1e84', '00bc1e97']]`
  - `CONDITIONAL_JUMP` [`00bc1e94`](#insn-00bc1e94) → [`00bc1e64`](#insn-00bc1e64)
  - `FALL_THROUGH` [`00bc1e94`](#insn-00bc1e94) → [`00bc1e98`](#insn-00bc1e98)
- ブロック [`00bc1e98`](#insn-00bc1e98) 範囲 `[['00bc1e98', '00bc1e9f']]`
  - `CONDITIONAL_JUMP` [`00bc1e9c`](#insn-00bc1e9c) → [`00bc1eb4`](#insn-00bc1eb4)
  - `FALL_THROUGH` [`00bc1e9c`](#insn-00bc1e9c) → [`00bc1ea0`](#insn-00bc1ea0)
- ブロック [`00bc1ea0`](#insn-00bc1ea0) 範囲 `[['00bc1ea0', '00bc1eab']]`
  - `CONDITIONAL_JUMP` [`00bc1ea8`](#insn-00bc1ea8) → [`00bc1eb4`](#insn-00bc1eb4)
  - `FALL_THROUGH` [`00bc1ea8`](#insn-00bc1ea8) → [`00bc1eac`](#insn-00bc1eac)
- ブロック [`00bc1eac`](#insn-00bc1eac) 範囲 `[['00bc1eac', '00bc1eb3']]`
  - `UNCONDITIONAL_JUMP` [`00bc1eb0`](#insn-00bc1eb0) → [`00bc1dc4`](#insn-00bc1dc4)
- ブロック [`00bc1eb4`](#insn-00bc1eb4) 範囲 `[['00bc1eb4', '00bc1eb7']]`
  - `FALL_THROUGH` [`00bc1eb4`](#insn-00bc1eb4) → [`00bc1eb8`](#insn-00bc1eb8)
- ブロック [`00bc1eb8`](#insn-00bc1eb8) 範囲 `[['00bc1eb8', '00bc1ed7']]`
- ブロック [`00bc1ed8`](#insn-00bc1ed8) 範囲 `[['00bc1ed8', '00bc1edf']]`
  - `CONDITIONAL_JUMP` [`00bc1edc`](#insn-00bc1edc) → [`00bc1fa4`](#insn-00bc1fa4)
  - `FALL_THROUGH` [`00bc1edc`](#insn-00bc1edc) → [`00bc1ee0`](#insn-00bc1ee0)
- ブロック [`00bc1ee0`](#insn-00bc1ee0) 範囲 `[['00bc1ee0', '00bc1ee3']]`
  - `CONDITIONAL_JUMP` [`00bc1ee0`](#insn-00bc1ee0) → [`00bc1fa4`](#insn-00bc1fa4)
  - `FALL_THROUGH` [`00bc1ee0`](#insn-00bc1ee0) → [`00bc1ee4`](#insn-00bc1ee4)
- ブロック [`00bc1ee4`](#insn-00bc1ee4) 範囲 `[['00bc1ee4', '00bc1ef7']]`
  - `CONDITIONAL_JUMP` [`00bc1ef4`](#insn-00bc1ef4) → [`00bc1f20`](#insn-00bc1f20)
  - `FALL_THROUGH` [`00bc1ef4`](#insn-00bc1ef4) → [`00bc1ef8`](#insn-00bc1ef8)
- ブロック [`00bc1ef8`](#insn-00bc1ef8) 範囲 `[['00bc1ef8', '00bc1f07']]`
  - `CONDITIONAL_JUMP` [`00bc1f04`](#insn-00bc1f04) → [`00bc2088`](#insn-00bc2088)
  - `FALL_THROUGH` [`00bc1f04`](#insn-00bc1f04) → [`00bc1f08`](#insn-00bc1f08)
- ブロック [`00bc1f08`](#insn-00bc1f08) 範囲 `[['00bc1f08', '00bc1f1f']]`
  - `FALL_THROUGH` [`00bc1f1c`](#insn-00bc1f1c) → [`00bc1f20`](#insn-00bc1f20)
- ブロック [`00bc1f20`](#insn-00bc1f20) 範囲 `[['00bc1f20', '00bc1f6b']]`
  - `CONDITIONAL_JUMP` [`00bc1f68`](#insn-00bc1f68) → [`00bc2078`](#insn-00bc2078)
  - `FALL_THROUGH` [`00bc1f68`](#insn-00bc1f68) → [`00bc1f6c`](#insn-00bc1f6c)
- ブロック [`00bc1f6c`](#insn-00bc1f6c) 範囲 `[['00bc1f6c', '00bc1f87']]`
  - `CONDITIONAL_JUMP` [`00bc1f84`](#insn-00bc1f84) → [`00bc2038`](#insn-00bc2038)
  - `FALL_THROUGH` [`00bc1f84`](#insn-00bc1f84) → [`00bc1f88`](#insn-00bc1f88)
- ブロック [`00bc1f88`](#insn-00bc1f88) 範囲 `[['00bc1f88', '00bc1f9f']]`
  - `CONDITIONAL_JUMP` [`00bc1f9c`](#insn-00bc1f9c) → [`00bc2068`](#insn-00bc2068)
  - `FALL_THROUGH` [`00bc1f9c`](#insn-00bc1f9c) → [`00bc1fa0`](#insn-00bc1fa0)
- ブロック [`00bc1fa0`](#insn-00bc1fa0) 範囲 `[['00bc1fa0', '00bc1fa3']]`
- ブロック [`00bc1fa4`](#insn-00bc1fa4) 範囲 `[['00bc1fa4', '00bc1fa7']]`
  - `FALL_THROUGH` [`00bc1fa4`](#insn-00bc1fa4) → [`00bc1fa8`](#insn-00bc1fa8)
- ブロック [`00bc1fa8`](#insn-00bc1fa8) 範囲 `[['00bc1fa8', '00bc1fbb']]`
  - `CONDITIONAL_JUMP` [`00bc1fb8`](#insn-00bc1fb8) → [`00bc1fdc`](#insn-00bc1fdc)
  - `FALL_THROUGH` [`00bc1fb8`](#insn-00bc1fb8) → [`00bc1fbc`](#insn-00bc1fbc)
- ブロック [`00bc1fbc`](#insn-00bc1fbc) 範囲 `[['00bc1fbc', '00bc1fc3']]`
  - `CONDITIONAL_JUMP` [`00bc1fc0`](#insn-00bc1fc0) → [`00bc1fdc`](#insn-00bc1fdc)
  - `FALL_THROUGH` [`00bc1fc0`](#insn-00bc1fc0) → [`00bc1fc4`](#insn-00bc1fc4)
- ブロック [`00bc1fc4`](#insn-00bc1fc4) 範囲 `[['00bc1fc4', '00bc1fd3']]`
  - `CONDITIONAL_JUMP` [`00bc1fd0`](#insn-00bc1fd0) → [`00bc1fdc`](#insn-00bc1fdc)
  - `FALL_THROUGH` [`00bc1fd0`](#insn-00bc1fd0) → [`00bc1fd4`](#insn-00bc1fd4)
- ブロック [`00bc1fd4`](#insn-00bc1fd4) 範囲 `[['00bc1fd4', '00bc1fdb']]`
  - `UNCONDITIONAL_JUMP` [`00bc1fd8`](#insn-00bc1fd8) → [`00bc1eb8`](#insn-00bc1eb8)
- ブロック [`00bc1fdc`](#insn-00bc1fdc) 範囲 `[['00bc1fdc', '00bc1fe7']]`
  - `CONDITIONAL_JUMP` [`00bc1fe4`](#insn-00bc1fe4) → [`00bc1eb8`](#insn-00bc1eb8)
  - `FALL_THROUGH` [`00bc1fe4`](#insn-00bc1fe4) → [`00bc1fe8`](#insn-00bc1fe8)
- ブロック [`00bc1fe8`](#insn-00bc1fe8) 範囲 `[['00bc1fe8', '00bc1ff3']]`
  - `CONDITIONAL_JUMP` [`00bc1ff0`](#insn-00bc1ff0) → [`00bc1eb8`](#insn-00bc1eb8)
  - `FALL_THROUGH` [`00bc1ff0`](#insn-00bc1ff0) → [`00bc1ff4`](#insn-00bc1ff4)
- ブロック [`00bc1ff4`](#insn-00bc1ff4) 範囲 `[['00bc1ff4', '00bc1ffb']]`
  - `CONDITIONAL_JUMP` [`00bc1ff8`](#insn-00bc1ff8) → [`00bc2014`](#insn-00bc2014)
  - `FALL_THROUGH` [`00bc1ff8`](#insn-00bc1ff8) → [`00bc1ffc`](#insn-00bc1ffc)
- ブロック [`00bc1ffc`](#insn-00bc1ffc) 範囲 `[['00bc1ffc', '00bc2013']]`
  - `FALL_THROUGH` [`00bc2010`](#insn-00bc2010) → [`00bc2014`](#insn-00bc2014)
- ブロック [`00bc2014`](#insn-00bc2014) 範囲 `[['00bc2014', '00bc2033']]`
  - `FALL_THROUGH` [`00bc2030`](#insn-00bc2030) → [`00bc2034`](#insn-00bc2034)
- ブロック [`00bc2034`](#insn-00bc2034) 範囲 `[['00bc2034', '00bc2037']]`
- ブロック [`00bc2038`](#insn-00bc2038) 範囲 `[['00bc2038', '00bc2043']]`
  - `CONDITIONAL_JUMP` [`00bc2040`](#insn-00bc2040) → [`00bc208c`](#insn-00bc208c)
  - `FALL_THROUGH` [`00bc2040`](#insn-00bc2040) → [`00bc2044`](#insn-00bc2044)
- ブロック [`00bc2044`](#insn-00bc2044) 範囲 `[['00bc2044', '00bc204f']]`
  - `CONDITIONAL_JUMP` [`00bc204c`](#insn-00bc204c) → [`00bc2060`](#insn-00bc2060)
  - `FALL_THROUGH` [`00bc204c`](#insn-00bc204c) → [`00bc2050`](#insn-00bc2050)
- ブロック [`00bc2050`](#insn-00bc2050) 範囲 `[['00bc2050', '00bc205f']]`
  - `FALL_THROUGH` [`00bc205c`](#insn-00bc205c) → [`00bc2060`](#insn-00bc2060)
- ブロック [`00bc2060`](#insn-00bc2060) 範囲 `[['00bc2060', '00bc2067']]`
  - `FALL_THROUGH` [`00bc2064`](#insn-00bc2064) → [`00bc2068`](#insn-00bc2068)
- ブロック [`00bc2068`](#insn-00bc2068) 範囲 `[['00bc2068', '00bc2077']]`
  - `FALL_THROUGH` [`00bc2074`](#insn-00bc2074) → [`00bc2078`](#insn-00bc2078)
- ブロック [`00bc2078`](#insn-00bc2078) 範囲 `[['00bc2078', '00bc2087']]`
  - `UNCONDITIONAL_JUMP` [`00bc2084`](#insn-00bc2084) → [`00bc1eb8`](#insn-00bc1eb8)
- ブロック [`00bc2088`](#insn-00bc2088) 範囲 `[['00bc2088', '00bc208b']]`
- ブロック [`00bc208c`](#insn-00bc208c) 範囲 `[['00bc208c', '00bc208f']]`

## 命令位置別の参照

- [`00bc1cd4`](#insn-00bc1cd4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1cd8`](#insn-00bc1cd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1cdc`](#insn-00bc1cdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ce0`](#insn-00bc1ce0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1cf0`](#insn-00bc1cf0) → [`00bc1eb4`](#insn-00bc1eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1cfc`](#insn-00bc1cfc) → [`00bc1eb4`](#insn-00bc1eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1d0c`](#insn-00bc1d0c) → [`00bc1eb4`](#insn-00bc1eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1d18`](#insn-00bc1d18) → [`00bc1da8`](#insn-00bc1da8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1d28`](#insn-00bc1d28) → [`00bc1eb4`](#insn-00bc1eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1d38`](#insn-00bc1d38) → [`00bc1eb4`](#insn-00bc1eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1d68`](#insn-00bc1d68) → [`00bc1d80`](#insn-00bc1d80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1d7c`](#insn-00bc1d7c) → [`00bc1d48`](#insn-00bc1d48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1d84`](#insn-00bc1d84) → [`00bc1eb4`](#insn-00bc1eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1d90`](#insn-00bc1d90) → [`00bc1eb4`](#insn-00bc1eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1da0`](#insn-00bc1da0) → [`00bc1db4`](#insn-00bc1db4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1da4`](#insn-00bc1da4) → [`00bc1eb4`](#insn-00bc1eb4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1db0`](#insn-00bc1db0) → [`00bc1eb4`](#insn-00bc1eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1dbc`](#insn-00bc1dbc) → [`00bc1e48`](#insn-00bc1e48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1dd0`](#insn-00bc1dd0) → [`00bc1ed8`](#insn-00bc1ed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1de4`](#insn-00bc1de4) → [`00bc1e08`](#insn-00bc1e08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1df0`](#insn-00bc1df0) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bc1df4`](#insn-00bc1df4) → [`00bc2088`](#insn-00bc2088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1e20`](#insn-00bc1e20) → `00c17898`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bc1e44`](#insn-00bc1e44) → [`00bc1eb8`](#insn-00bc1eb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1e54`](#insn-00bc1e54) → [`00bc1eb4`](#insn-00bc1eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1e80`](#insn-00bc1e80) → [`00bc1e98`](#insn-00bc1e98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1e94`](#insn-00bc1e94) → [`00bc1e64`](#insn-00bc1e64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1e9c`](#insn-00bc1e9c) → [`00bc1eb4`](#insn-00bc1eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ea8`](#insn-00bc1ea8) → [`00bc1eb4`](#insn-00bc1eb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1eb0`](#insn-00bc1eb0) → [`00bc1dc4`](#insn-00bc1dc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ebc`](#insn-00bc1ebc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ec0`](#insn-00bc1ec0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ec4`](#insn-00bc1ec4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ec8`](#insn-00bc1ec8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1edc`](#insn-00bc1edc) → [`00bc1fa4`](#insn-00bc1fa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ee0`](#insn-00bc1ee0) → [`00bc1fa4`](#insn-00bc1fa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ef4`](#insn-00bc1ef4) → [`00bc1f20`](#insn-00bc1f20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1f00`](#insn-00bc1f00) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bc1f04`](#insn-00bc1f04) → [`00bc2088`](#insn-00bc2088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1f38`](#insn-00bc1f38) → `00c17978`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bc1f68`](#insn-00bc1f68) → [`00bc2078`](#insn-00bc2078) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1f84`](#insn-00bc1f84) → [`00bc2038`](#insn-00bc2038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1f8c`](#insn-00bc1f8c) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bc1f9c`](#insn-00bc1f9c) → [`00bc2068`](#insn-00bc2068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1fa0`](#insn-00bc1fa0) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bc1fb8`](#insn-00bc1fb8) → [`00bc1fdc`](#insn-00bc1fdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1fc0`](#insn-00bc1fc0) → [`00bc1fdc`](#insn-00bc1fdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1fd0`](#insn-00bc1fd0) → [`00bc1fdc`](#insn-00bc1fdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1fd8`](#insn-00bc1fd8) → [`00bc1eb8`](#insn-00bc1eb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1fe4`](#insn-00bc1fe4) → [`00bc1eb8`](#insn-00bc1eb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ff0`](#insn-00bc1ff0) → [`00bc1eb8`](#insn-00bc1eb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc1ff8`](#insn-00bc1ff8) → [`00bc2014`](#insn-00bc2014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2008`](#insn-00bc2008) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc200c`](#insn-00bc200c) → [`00bc2b00`](../00bc2/00bc2b00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2b00` · 推定シンボル `None` · 推定型 `None`
- [`00bc2018`](#insn-00bc2018) → `002925bc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc201c`](#insn-00bc201c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2020`](#insn-00bc2020) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2024`](#insn-00bc2024) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2028`](#insn-00bc2028) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2034`](#insn-00bc2034) → [`00bc2bd8`](../00bc2/00bc2bd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2bd8` · 推定シンボル `None` · 推定型 `None`
- [`00bc203c`](#insn-00bc203c) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bc2040`](#insn-00bc2040) → [`00bc208c`](#insn-00bc208c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc204c`](#insn-00bc204c) → [`00bc2060`](#insn-00bc2060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc205c`](#insn-00bc205c) → [`00bdb0f0`](../00bdb/00bdb0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bc2084`](#insn-00bc2084) → [`00bc1eb8`](#insn-00bc1eb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bc2088`](#insn-00bc2088) → [`00bdb1d0`](../00bdb/00bdb1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bc208c`](#insn-00bc208c) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bc1cd4`](#insn-00bc1cd4)

~~~json
{
  "source": "00bc1cd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1cd8`](#insn-00bc1cd8)

~~~json
{
  "source": "00bc1cd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1cdc`](#insn-00bc1cdc)

~~~json
{
  "source": "00bc1cdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ce0`](#insn-00bc1ce0)

~~~json
{
  "source": "00bc1ce0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1cf0`](#insn-00bc1cf0)

~~~json
{
  "source": "00bc1cf0",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1cfc`](#insn-00bc1cfc)

~~~json
{
  "source": "00bc1cfc",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1d0c`](#insn-00bc1d0c)

~~~json
{
  "source": "00bc1d0c",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1d18`](#insn-00bc1d18)

~~~json
{
  "source": "00bc1d18",
  "target": "00bc1da8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1d28`](#insn-00bc1d28)

~~~json
{
  "source": "00bc1d28",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1d38`](#insn-00bc1d38)

~~~json
{
  "source": "00bc1d38",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1d68`](#insn-00bc1d68)

~~~json
{
  "source": "00bc1d68",
  "target": "00bc1d80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1d7c`](#insn-00bc1d7c)

~~~json
{
  "source": "00bc1d7c",
  "target": "00bc1d48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1d84`](#insn-00bc1d84)

~~~json
{
  "source": "00bc1d84",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1d90`](#insn-00bc1d90)

~~~json
{
  "source": "00bc1d90",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1da0`](#insn-00bc1da0)

~~~json
{
  "source": "00bc1da0",
  "target": "00bc1db4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1da4`](#insn-00bc1da4)

~~~json
{
  "source": "00bc1da4",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1db0`](#insn-00bc1db0)

~~~json
{
  "source": "00bc1db0",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1dbc`](#insn-00bc1dbc)

~~~json
{
  "source": "00bc1dbc",
  "target": "00bc1e48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1dd0`](#insn-00bc1dd0)

~~~json
{
  "source": "00bc1dd0",
  "target": "00bc1ed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1de4`](#insn-00bc1de4)

~~~json
{
  "source": "00bc1de4",
  "target": "00bc1e08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1df0`](#insn-00bc1df0)

~~~json
{
  "source": "00bc1df0",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc1df4`](#insn-00bc1df4)

~~~json
{
  "source": "00bc1df4",
  "target": "00bc2088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1e20`](#insn-00bc1e20)

~~~json
{
  "source": "00bc1e20",
  "target": "00c17898",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17898",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc1e44`](#insn-00bc1e44)

~~~json
{
  "source": "00bc1e44",
  "target": "00bc1eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1e54`](#insn-00bc1e54)

~~~json
{
  "source": "00bc1e54",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1e80`](#insn-00bc1e80)

~~~json
{
  "source": "00bc1e80",
  "target": "00bc1e98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1e94`](#insn-00bc1e94)

~~~json
{
  "source": "00bc1e94",
  "target": "00bc1e64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1e9c`](#insn-00bc1e9c)

~~~json
{
  "source": "00bc1e9c",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ea8`](#insn-00bc1ea8)

~~~json
{
  "source": "00bc1ea8",
  "target": "00bc1eb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1eb0`](#insn-00bc1eb0)

~~~json
{
  "source": "00bc1eb0",
  "target": "00bc1dc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ebc`](#insn-00bc1ebc)

~~~json
{
  "source": "00bc1ebc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ec0`](#insn-00bc1ec0)

~~~json
{
  "source": "00bc1ec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ec4`](#insn-00bc1ec4)

~~~json
{
  "source": "00bc1ec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ec8`](#insn-00bc1ec8)

~~~json
{
  "source": "00bc1ec8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1edc`](#insn-00bc1edc)

~~~json
{
  "source": "00bc1edc",
  "target": "00bc1fa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ee0`](#insn-00bc1ee0)

~~~json
{
  "source": "00bc1ee0",
  "target": "00bc1fa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ef4`](#insn-00bc1ef4)

~~~json
{
  "source": "00bc1ef4",
  "target": "00bc1f20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1f00`](#insn-00bc1f00)

~~~json
{
  "source": "00bc1f00",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc1f04`](#insn-00bc1f04)

~~~json
{
  "source": "00bc1f04",
  "target": "00bc2088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1f38`](#insn-00bc1f38)

~~~json
{
  "source": "00bc1f38",
  "target": "00c17978",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c17978",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bc1f68`](#insn-00bc1f68)

~~~json
{
  "source": "00bc1f68",
  "target": "00bc2078",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1f84`](#insn-00bc1f84)

~~~json
{
  "source": "00bc1f84",
  "target": "00bc2038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1f8c`](#insn-00bc1f8c)

~~~json
{
  "source": "00bc1f8c",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc1f9c`](#insn-00bc1f9c)

~~~json
{
  "source": "00bc1f9c",
  "target": "00bc2068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1fa0`](#insn-00bc1fa0)

~~~json
{
  "source": "00bc1fa0",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc1fb8`](#insn-00bc1fb8)

~~~json
{
  "source": "00bc1fb8",
  "target": "00bc1fdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1fc0`](#insn-00bc1fc0)

~~~json
{
  "source": "00bc1fc0",
  "target": "00bc1fdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1fd0`](#insn-00bc1fd0)

~~~json
{
  "source": "00bc1fd0",
  "target": "00bc1fdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1fd8`](#insn-00bc1fd8)

~~~json
{
  "source": "00bc1fd8",
  "target": "00bc1eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1fe4`](#insn-00bc1fe4)

~~~json
{
  "source": "00bc1fe4",
  "target": "00bc1eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ff0`](#insn-00bc1ff0)

~~~json
{
  "source": "00bc1ff0",
  "target": "00bc1eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc1ff8`](#insn-00bc1ff8)

~~~json
{
  "source": "00bc1ff8",
  "target": "00bc2014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2008`](#insn-00bc2008)

~~~json
{
  "source": "00bc2008",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc200c`](#insn-00bc200c)

~~~json
{
  "source": "00bc200c",
  "target": "00bc2b00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2018`](#insn-00bc2018)

~~~json
{
  "source": "00bc2018",
  "target": "002925bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc201c`](#insn-00bc201c)

~~~json
{
  "source": "00bc201c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2020`](#insn-00bc2020)

~~~json
{
  "source": "00bc2020",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2024`](#insn-00bc2024)

~~~json
{
  "source": "00bc2024",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2028`](#insn-00bc2028)

~~~json
{
  "source": "00bc2028",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2034`](#insn-00bc2034)

~~~json
{
  "source": "00bc2034",
  "target": "00bc2bd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc203c`](#insn-00bc203c)

~~~json
{
  "source": "00bc203c",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2040`](#insn-00bc2040)

~~~json
{
  "source": "00bc2040",
  "target": "00bc208c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc204c`](#insn-00bc204c)

~~~json
{
  "source": "00bc204c",
  "target": "00bc2060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc205c`](#insn-00bc205c)

~~~json
{
  "source": "00bc205c",
  "target": "00bdb0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc2084`](#insn-00bc2084)

~~~json
{
  "source": "00bc2084",
  "target": "00bc1eb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bc2088`](#insn-00bc2088)

~~~json
{
  "source": "00bc2088",
  "target": "00bdb1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bc208c`](#insn-00bc208c)

~~~json
{
  "source": "00bc208c",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
