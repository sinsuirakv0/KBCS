# 00b8daec

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b8dbb4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b8d/00b8dbb4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0076.md#compare-389161d45084a95ca4ec96398240bb8f)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b8daec",
  "name": "_ZNSt6__ndk19__num_getIcE17__stage2_int_loopEciPcRS2_RjcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSD_S2_",
  "size": 448,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d95eb14fe7d21627aa66f75316d492d5077a5f452ed18833db516ba4f4f56d34",
  "source_text_sha256": "d95eb14fe7d21627aa66f75316d492d5077a5f452ed18833db516ba4f4f56d34",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b8daec",
        "00b8dcab"
      ]
    ],
    "bytes_sha256": "bed9b1c59edc0425c68fe66d82fc632e0f6901b68508819af53d69c4cccd2f1b",
    "instruction_count": 112,
    "instruction_bytes": 448,
    "body_bytes": 448,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be1430](../00be1/00be1430.md)

## 呼び出し先

- [00bdb080](../00bdb/00bdb080.md)

## 関連文字列（未確認候補）

~~~text
"0123456789abcdefABCDEFxX+-pPiInN"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2738 bytes

~~~c

undefined8
_ZNSt6__ndk19__num_getIcE17__stage2_int_loopEciPcRS2_RjcRKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPjRSD_S2_
          (byte param_1,uint param_2,undefined1 *param_3,long *param_4,int *param_5,byte param_6,
          byte *param_7,long param_8,undefined8 *param_9,void *param_10)

{
  ulong uVar1;
  void *pvVar2;
  undefined *puVar3;
  void *pvVar4;
  undefined8 uVar5;
  undefined1 uVar6;
  long lVar7;
  int *piVar8;
  undefined1 *puVar9;
  
  puVar9 = (undefined1 *)*param_4;
  if (puVar9 == param_3) {
    if (*(byte *)((long)param_10 + 0x18) == param_1) {
      uVar6 = 0x2b;
LAB_00b8dbd0:
      *param_4 = (long)(param_3 + 1);
      *param_3 = uVar6;
      *param_5 = 0;
      return 0;
    }
    if (*(byte *)((long)param_10 + 0x19) == param_1) {
      uVar6 = 0x2d;
      goto LAB_00b8dbd0;
    }
  }
  uVar1 = (ulong)(*param_7 >> 1);
  if ((*param_7 & 1) != 0) {
    uVar1 = *(ulong *)(param_7 + 8);
  }
  if ((param_1 == param_6) && (uVar1 != 0)) {
    piVar8 = (int *)*param_9;
                    /* try { // try from 00b8db4c to 00c8dc97 has its CatchHandler @ 00b8db4c
                       catch() { ... } // from try @ 00b8db4c with catch @ 00b8db4c
                       catch() { ... } // from try @ 00b8dca4 with catch @ 00b8db4c */
    if ((long)piVar8 - param_8 < 0xa0) {
      *piVar8 = *param_5;
      *param_9 = piVar8 + 1;
      *param_5 = 0;
      return 0;
    }
    return 0;
  }
  pvVar4 = memchr(param_10,(uint)param_1,0x1a);
  puVar3 = PTR__ZNSt6__ndk114__num_get_base5__srcE_00c1bc90;
  pvVar2 = (void *)((long)param_10 + 0x1a);
  if (pvVar4 != (void *)0x0) {
    pvVar2 = pvVar4;
  }
  lVar7 = (long)pvVar2 - (long)param_10;
  if (lVar7 < 0x18) {
    if (param_2 == 8) {
LAB_00b8dc08:
      if ((long)(ulong)param_2 <= lVar7) goto LAB_00b8dbb8;
    }
    else if (param_2 == 0x10) {
      if (0x15 < lVar7) {
        if (puVar9 == param_3) {
          return 0xffffffff;
        }
        if (2 < (long)puVar9 - (long)param_3) {
          return 0xffffffff;
        }
        if (puVar9[-1] != '0') {
          return 0xffffffff;
        }
        *param_5 = 0;
                    /* try { // try from 00b8dc98 to 00c8dca3 has its CatchHandler @ 00b8dd24 */
        uVar6 = puVar3[lVar7];
        *param_4 = (long)(puVar9 + 1);
                    /* try { // try from 00b8dca4 to 00c8dd4b has its CatchHandler @ 00b8db4c */
        *puVar9 = uVar6;
        return 0;
      }
    }
    else if (param_2 == 10) goto LAB_00b8dc08;
    uVar5 = 0;
    uVar6 = PTR__ZNSt6__ndk114__num_get_base5__srcE_00c1bc90[lVar7];
    *param_4 = (long)(puVar9 + 1);
    *puVar9 = uVar6;
    *param_5 = *param_5 + 1;
  }
  else {
LAB_00b8dbb8:
    uVar5 = 0xffffffff;
  }
  return uVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b8daec"></a> `00b8daec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00b8daf0"></a> `00b8daf0` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00b8daf4"></a> `00b8daf4` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b8daf8"></a> `00b8daf8` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b8dafc"></a> `00b8dafc` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b8db00"></a> `00b8db00` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b8db04"></a> `00b8db04` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00b8db08"></a> `00b8db08` | `74 00 40 f9` | ldr x20,[x3] | `FALL_THROUGH`
<a id="insn-00b8db0c"></a> `00b8db0c` | `b3 2f 40 f9` | ldr x19,[x29, #0x58] | `FALL_THROUGH`
<a id="insn-00b8db10"></a> `00b8db10` | `08 1c 00 12` | and w8,w0,#0xff | `FALL_THROUGH`
<a id="insn-00b8db14"></a> `00b8db14` | `9f 02 02 eb` | cmp x20,x2 | `FALL_THROUGH`
<a id="insn-00b8db18"></a> `00b8db18` | `a0 02 00 54` | b.eq 0x00b8db6c | `CONDITIONAL_JUMP`
<a id="insn-00b8db1c"></a> `00b8db1c` | `c9 00 40 39` | ldrb w9,[x6] | `FALL_THROUGH`
<a id="insn-00b8db20"></a> `00b8db20` | `ca 04 40 f9` | ldr x10,[x6, #0x8] | `FALL_THROUGH`
<a id="insn-00b8db24"></a> `00b8db24` | `ac 1c 00 12` | and w12,w5,#0xff | `FALL_THROUGH`
<a id="insn-00b8db28"></a> `00b8db28` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b8db2c"></a> `00b8db2c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b8db30"></a> `00b8db30` | `69 01 8a 9a` | csel x9,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00b8db34"></a> `00b8db34` | `1f 01 0c 6b` | cmp w8,w12 | `FALL_THROUGH`
<a id="insn-00b8db38"></a> `00b8db38` | `41 02 00 54` | b.ne 0x00b8db80 | `CONDITIONAL_JUMP`
<a id="insn-00b8db3c"></a> `00b8db3c` | `29 02 00 b4` | cbz x9,0x00b8db80 | `CONDITIONAL_JUMP`
<a id="insn-00b8db40"></a> `00b8db40` | `a8 2b 40 f9` | ldr x8,[x29, #0x50] | `FALL_THROUGH`
<a id="insn-00b8db44"></a> `00b8db44` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00b8db48"></a> `00b8db48` | `2a 01 07 cb` | sub x10,x9,x7 | `FALL_THROUGH`
<a id="insn-00b8db4c"></a> `00b8db4c` | `5f 7d 02 f1` | cmp x10,#0x9f | `FALL_THROUGH`
<a id="insn-00b8db50"></a> `00b8db50` | `2c 06 00 54` | b.gt 0x00b8dc14 | `CONDITIONAL_JUMP`
<a id="insn-00b8db54"></a> `00b8db54` | `8a 00 40 b9` | ldr w10,[x4] | `FALL_THROUGH`
<a id="insn-00b8db58"></a> `00b8db58` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b8db5c"></a> `00b8db5c` | `2a 45 00 b8` | str w10,[x9], #0x4 | `FALL_THROUGH`
<a id="insn-00b8db60"></a> `00b8db60` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00b8db64"></a> `00b8db64` | `9f 00 00 b9` | str wzr,[x4] | `FALL_THROUGH`
<a id="insn-00b8db68"></a> `00b8db68` | `39 00 00 14` | b 0x00b8dc4c | `UNCONDITIONAL_JUMP`
<a id="insn-00b8db6c"></a> `00b8db6c` | `69 62 40 39` | ldrb w9,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00b8db70"></a> `00b8db70` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00b8db74"></a> `00b8db74` | `61 02 00 54` | b.ne 0x00b8dbc0 | `CONDITIONAL_JUMP`
<a id="insn-00b8db78"></a> `00b8db78` | `68 05 80 52` | mov w8,#0x2b | `FALL_THROUGH`
<a id="insn-00b8db7c"></a> `00b8db7c` | `15 00 00 14` | b 0x00b8dbd0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8db80"></a> `00b8db80` | `f8 03 01 2a` | mov w24,w1 | `FALL_THROUGH`
<a id="insn-00b8db84"></a> `00b8db84` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00b8db88"></a> `00b8db88` | `01 1c 00 12` | and w1,w0,#0xff | `FALL_THROUGH`
<a id="insn-00b8db8c"></a> `00b8db8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b8db90"></a> `00b8db90` | `42 03 80 52` | mov w2,#0x1a | `FALL_THROUGH`
<a id="insn-00b8db94"></a> `00b8db94` | `f6 03 03 aa` | mov x22,x3 | `FALL_THROUGH`
<a id="insn-00b8db98"></a> `00b8db98` | `f7 03 04 aa` | mov x23,x4 | `FALL_THROUGH`
<a id="insn-00b8db9c"></a> `00b8db9c` | `79 6a 00 91` | add x25,x19,#0x1a | `FALL_THROUGH`
<a id="insn-00b8dba0"></a> `00b8dba0` | `38 35 01 94` | bl 0x00bdb080 | `UNCONDITIONAL_CALL`
<a id="insn-00b8dba4"></a> `00b8dba4` | `1f 00 00 f1` | cmp x0,#0x0 | `FALL_THROUGH`
<a id="insn-00b8dba8"></a> `00b8dba8` | `28 03 80 9a` | csel x8,x25,x0,eq | `FALL_THROUGH`
<a id="insn-00b8dbac"></a> `00b8dbac` | `08 01 13 cb` | sub x8,x8,x19 | `FALL_THROUGH`
<a id="insn-00b8dbb0"></a> `00b8dbb0` | `1f 5d 00 f1` | cmp x8,#0x17 | `FALL_THROUGH`
<a id="insn-00b8dbb4"></a> `00b8dbb4` | `ad 01 00 54` | b.le 0x00b8dbe8 | `CONDITIONAL_JUMP`
<a id="insn-00b8dbb8"></a> `00b8dbb8` | `00 00 80 12` | mov w0,#0xffffffff | `FALL_THROUGH`
<a id="insn-00b8dbbc"></a> `00b8dbbc` | `24 00 00 14` | b 0x00b8dc4c | `UNCONDITIONAL_JUMP`
<a id="insn-00b8dbc0"></a> `00b8dbc0` | `69 66 40 39` | ldrb w9,[x19, #0x19] | `FALL_THROUGH`
<a id="insn-00b8dbc4"></a> `00b8dbc4` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00b8dbc8"></a> `00b8dbc8` | `a1 fa ff 54` | b.ne 0x00b8db1c | `CONDITIONAL_JUMP`
<a id="insn-00b8dbcc"></a> `00b8dbcc` | `a8 05 80 52` | mov w8,#0x2d | `FALL_THROUGH`
<a id="insn-00b8dbd0"></a> `00b8dbd0` | `49 04 00 91` | add x9,x2,#0x1 | `FALL_THROUGH`
<a id="insn-00b8dbd4"></a> `00b8dbd4` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b8dbd8"></a> `00b8dbd8` | `69 00 00 f9` | str x9,[x3] | `FALL_THROUGH`
<a id="insn-00b8dbdc"></a> `00b8dbdc` | `48 00 00 39` | strb w8,[x2] | `FALL_THROUGH`
<a id="insn-00b8dbe0"></a> `00b8dbe0` | `9f 00 00 b9` | str wzr,[x4] | `FALL_THROUGH`
<a id="insn-00b8dbe4"></a> `00b8dbe4` | `1a 00 00 14` | b 0x00b8dc4c | `UNCONDITIONAL_JUMP`
<a id="insn-00b8dbe8"></a> `00b8dbe8` | `1f 23 00 71` | cmp w24,#0x8 | `FALL_THROUGH`
<a id="insn-00b8dbec"></a> `00b8dbec` | `e9 03 17 aa` | mov x9,x23 | `FALL_THROUGH`
<a id="insn-00b8dbf0"></a> `00b8dbf0` | `ea 03 16 aa` | mov x10,x22 | `FALL_THROUGH`
<a id="insn-00b8dbf4"></a> `00b8dbf4` | `a0 00 00 54` | b.eq 0x00b8dc08 | `CONDITIONAL_JUMP`
<a id="insn-00b8dbf8"></a> `00b8dbf8` | `1f 43 00 71` | cmp w24,#0x10 | `FALL_THROUGH`
<a id="insn-00b8dbfc"></a> `00b8dbfc` | `00 01 00 54` | b.eq 0x00b8dc1c | `CONDITIONAL_JUMP`
<a id="insn-00b8dc00"></a> `00b8dc00` | `1f 2b 00 71` | cmp w24,#0xa | `FALL_THROUGH`
<a id="insn-00b8dc04"></a> `00b8dc04` | `01 01 00 54` | b.ne 0x00b8dc24 | `CONDITIONAL_JUMP`
<a id="insn-00b8dc08"></a> `00b8dc08` | `1f 41 38 eb` | cmp x8,w24, UXTW  | `FALL_THROUGH`
<a id="insn-00b8dc0c"></a> `00b8dc0c` | `6a fd ff 54` | b.ge 0x00b8dbb8 | `CONDITIONAL_JUMP`
<a id="insn-00b8dc10"></a> `00b8dc10` | `05 00 00 14` | b 0x00b8dc24 | `UNCONDITIONAL_JUMP`
<a id="insn-00b8dc14"></a> `00b8dc14` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b8dc18"></a> `00b8dc18` | `0d 00 00 14` | b 0x00b8dc4c | `UNCONDITIONAL_JUMP`
<a id="insn-00b8dc1c"></a> `00b8dc1c` | `1f 59 00 f1` | cmp x8,#0x16 | `FALL_THROUGH`
<a id="insn-00b8dc20"></a> `00b8dc20` | `4a 02 00 54` | b.ge 0x00b8dc68 | `CONDITIONAL_JUMP`
<a id="insn-00b8dc24"></a> `00b8dc24` | `6b 04 00 d0` | adrp x11,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b8dc28"></a> `00b8dc28` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b8dc2c"></a> `00b8dc2c` | `6b 49 46 f9` | ldr x11,[x11, #0xc90] | `FALL_THROUGH`
<a id="insn-00b8dc30"></a> `00b8dc30` | `68 69 68 38` | ldrb w8,[x11, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00b8dc34"></a> `00b8dc34` | `8b 06 00 91` | add x11,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00b8dc38"></a> `00b8dc38` | `4b 01 00 f9` | str x11,[x10] | `FALL_THROUGH`
<a id="insn-00b8dc3c"></a> `00b8dc3c` | `88 02 00 39` | strb w8,[x20] | `FALL_THROUGH`
<a id="insn-00b8dc40"></a> `00b8dc40` | `28 01 40 b9` | ldr w8,[x9] | `FALL_THROUGH`
<a id="insn-00b8dc44"></a> `00b8dc44` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b8dc48"></a> `00b8dc48` | `28 01 00 b9` | str w8,[x9] | `FALL_THROUGH`
<a id="insn-00b8dc4c"></a> `00b8dc4c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b8dc50"></a> `00b8dc50` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b8dc54"></a> `00b8dc54` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b8dc58"></a> `00b8dc58` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b8dc5c"></a> `00b8dc5c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00b8dc60"></a> `00b8dc60` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00b8dc64"></a> `00b8dc64` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b8dc68"></a> `00b8dc68` | `8b 02 15 eb` | subs x11,x20,x21 | `FALL_THROUGH`
<a id="insn-00b8dc6c"></a> `00b8dc6c` | `00 00 80 12` | mov w0,#0xffffffff | `FALL_THROUGH`
<a id="insn-00b8dc70"></a> `00b8dc70` | `e0 fe ff 54` | b.eq 0x00b8dc4c | `CONDITIONAL_JUMP`
<a id="insn-00b8dc74"></a> `00b8dc74` | `7f 09 00 f1` | cmp x11,#0x2 | `FALL_THROUGH`
<a id="insn-00b8dc78"></a> `00b8dc78` | `ac fe ff 54` | b.gt 0x00b8dc4c | `CONDITIONAL_JUMP`
<a id="insn-00b8dc7c"></a> `00b8dc7c` | `8b f2 5f 38` | ldurb w11,[x20, #-0x1] | `FALL_THROUGH`
<a id="insn-00b8dc80"></a> `00b8dc80` | `7f c1 00 71` | cmp w11,#0x30 | `FALL_THROUGH`
<a id="insn-00b8dc84"></a> `00b8dc84` | `41 fe ff 54` | b.ne 0x00b8dc4c | `CONDITIONAL_JUMP`
<a id="insn-00b8dc88"></a> `00b8dc88` | `6b 04 00 d0` | adrp x11,0xc1b000 | `FALL_THROUGH`
<a id="insn-00b8dc8c"></a> `00b8dc8c` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00b8dc90"></a> `00b8dc90` | `6b 49 46 f9` | ldr x11,[x11, #0xc90] | `FALL_THROUGH`
<a id="insn-00b8dc94"></a> `00b8dc94` | `3f 01 00 b9` | str wzr,[x9] | `FALL_THROUGH`
<a id="insn-00b8dc98"></a> `00b8dc98` | `89 06 00 91` | add x9,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00b8dc9c"></a> `00b8dc9c` | `68 69 68 38` | ldrb w8,[x11, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00b8dca0"></a> `00b8dca0` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-00b8dca4"></a> `00b8dca4` | `88 02 00 39` | strb w8,[x20] | `FALL_THROUGH`
<a id="insn-00b8dca8"></a> `00b8dca8` | `e9 ff ff 17` | b 0x00b8dc4c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00b8daec`](#insn-00b8daec) 範囲 `[['00b8daec', '00b8db1b']]`
  - `CONDITIONAL_JUMP` [`00b8db18`](#insn-00b8db18) → [`00b8db6c`](#insn-00b8db6c)
  - `FALL_THROUGH` [`00b8db18`](#insn-00b8db18) → [`00b8db1c`](#insn-00b8db1c)
- ブロック [`00b8db1c`](#insn-00b8db1c) 範囲 `[['00b8db1c', '00b8db3b']]`
  - `CONDITIONAL_JUMP` [`00b8db38`](#insn-00b8db38) → [`00b8db80`](#insn-00b8db80)
  - `FALL_THROUGH` [`00b8db38`](#insn-00b8db38) → [`00b8db3c`](#insn-00b8db3c)
- ブロック [`00b8db3c`](#insn-00b8db3c) 範囲 `[['00b8db3c', '00b8db3f']]`
  - `CONDITIONAL_JUMP` [`00b8db3c`](#insn-00b8db3c) → [`00b8db80`](#insn-00b8db80)
  - `FALL_THROUGH` [`00b8db3c`](#insn-00b8db3c) → [`00b8db40`](#insn-00b8db40)
- ブロック [`00b8db40`](#insn-00b8db40) 範囲 `[['00b8db40', '00b8db4b']]`
  - `FALL_THROUGH` [`00b8db48`](#insn-00b8db48) → [`00b8db4c`](#insn-00b8db4c)
- ブロック [`00b8db4c`](#insn-00b8db4c) 範囲 `[['00b8db4c', '00b8db53']]`
  - `CONDITIONAL_JUMP` [`00b8db50`](#insn-00b8db50) → [`00b8dc14`](#insn-00b8dc14)
  - `FALL_THROUGH` [`00b8db50`](#insn-00b8db50) → [`00b8db54`](#insn-00b8db54)
- ブロック [`00b8db54`](#insn-00b8db54) 範囲 `[['00b8db54', '00b8db6b']]`
  - `UNCONDITIONAL_JUMP` [`00b8db68`](#insn-00b8db68) → [`00b8dc4c`](#insn-00b8dc4c)
- ブロック [`00b8db6c`](#insn-00b8db6c) 範囲 `[['00b8db6c', '00b8db77']]`
  - `CONDITIONAL_JUMP` [`00b8db74`](#insn-00b8db74) → [`00b8dbc0`](#insn-00b8dbc0)
  - `FALL_THROUGH` [`00b8db74`](#insn-00b8db74) → [`00b8db78`](#insn-00b8db78)
- ブロック [`00b8db78`](#insn-00b8db78) 範囲 `[['00b8db78', '00b8db7f']]`
  - `UNCONDITIONAL_JUMP` [`00b8db7c`](#insn-00b8db7c) → [`00b8dbd0`](#insn-00b8dbd0)
- ブロック [`00b8db80`](#insn-00b8db80) 範囲 `[['00b8db80', '00b8dbb7']]`
  - `CONDITIONAL_JUMP` [`00b8dbb4`](#insn-00b8dbb4) → [`00b8dbe8`](#insn-00b8dbe8)
  - `FALL_THROUGH` [`00b8dbb4`](#insn-00b8dbb4) → [`00b8dbb8`](#insn-00b8dbb8)
- ブロック [`00b8dbb8`](#insn-00b8dbb8) 範囲 `[['00b8dbb8', '00b8dbbf']]`
  - `UNCONDITIONAL_JUMP` [`00b8dbbc`](#insn-00b8dbbc) → [`00b8dc4c`](#insn-00b8dc4c)
- ブロック [`00b8dbc0`](#insn-00b8dbc0) 範囲 `[['00b8dbc0', '00b8dbcb']]`
  - `CONDITIONAL_JUMP` [`00b8dbc8`](#insn-00b8dbc8) → [`00b8db1c`](#insn-00b8db1c)
  - `FALL_THROUGH` [`00b8dbc8`](#insn-00b8dbc8) → [`00b8dbcc`](#insn-00b8dbcc)
- ブロック [`00b8dbcc`](#insn-00b8dbcc) 範囲 `[['00b8dbcc', '00b8dbcf']]`
  - `FALL_THROUGH` [`00b8dbcc`](#insn-00b8dbcc) → [`00b8dbd0`](#insn-00b8dbd0)
- ブロック [`00b8dbd0`](#insn-00b8dbd0) 範囲 `[['00b8dbd0', '00b8dbe7']]`
  - `UNCONDITIONAL_JUMP` [`00b8dbe4`](#insn-00b8dbe4) → [`00b8dc4c`](#insn-00b8dc4c)
- ブロック [`00b8dbe8`](#insn-00b8dbe8) 範囲 `[['00b8dbe8', '00b8dbf7']]`
  - `CONDITIONAL_JUMP` [`00b8dbf4`](#insn-00b8dbf4) → [`00b8dc08`](#insn-00b8dc08)
  - `FALL_THROUGH` [`00b8dbf4`](#insn-00b8dbf4) → [`00b8dbf8`](#insn-00b8dbf8)
- ブロック [`00b8dbf8`](#insn-00b8dbf8) 範囲 `[['00b8dbf8', '00b8dbff']]`
  - `CONDITIONAL_JUMP` [`00b8dbfc`](#insn-00b8dbfc) → [`00b8dc1c`](#insn-00b8dc1c)
  - `FALL_THROUGH` [`00b8dbfc`](#insn-00b8dbfc) → [`00b8dc00`](#insn-00b8dc00)
- ブロック [`00b8dc00`](#insn-00b8dc00) 範囲 `[['00b8dc00', '00b8dc07']]`
  - `CONDITIONAL_JUMP` [`00b8dc04`](#insn-00b8dc04) → [`00b8dc24`](#insn-00b8dc24)
  - `FALL_THROUGH` [`00b8dc04`](#insn-00b8dc04) → [`00b8dc08`](#insn-00b8dc08)
- ブロック [`00b8dc08`](#insn-00b8dc08) 範囲 `[['00b8dc08', '00b8dc0f']]`
  - `CONDITIONAL_JUMP` [`00b8dc0c`](#insn-00b8dc0c) → [`00b8dbb8`](#insn-00b8dbb8)
  - `FALL_THROUGH` [`00b8dc0c`](#insn-00b8dc0c) → [`00b8dc10`](#insn-00b8dc10)
- ブロック [`00b8dc10`](#insn-00b8dc10) 範囲 `[['00b8dc10', '00b8dc13']]`
  - `UNCONDITIONAL_JUMP` [`00b8dc10`](#insn-00b8dc10) → [`00b8dc24`](#insn-00b8dc24)
- ブロック [`00b8dc14`](#insn-00b8dc14) 範囲 `[['00b8dc14', '00b8dc1b']]`
  - `UNCONDITIONAL_JUMP` [`00b8dc18`](#insn-00b8dc18) → [`00b8dc4c`](#insn-00b8dc4c)
- ブロック [`00b8dc1c`](#insn-00b8dc1c) 範囲 `[['00b8dc1c', '00b8dc23']]`
  - `CONDITIONAL_JUMP` [`00b8dc20`](#insn-00b8dc20) → [`00b8dc68`](#insn-00b8dc68)
  - `FALL_THROUGH` [`00b8dc20`](#insn-00b8dc20) → [`00b8dc24`](#insn-00b8dc24)
- ブロック [`00b8dc24`](#insn-00b8dc24) 範囲 `[['00b8dc24', '00b8dc4b']]`
  - `FALL_THROUGH` [`00b8dc48`](#insn-00b8dc48) → [`00b8dc4c`](#insn-00b8dc4c)
- ブロック [`00b8dc4c`](#insn-00b8dc4c) 範囲 `[['00b8dc4c', '00b8dc67']]`
- ブロック [`00b8dc68`](#insn-00b8dc68) 範囲 `[['00b8dc68', '00b8dc73']]`
  - `CONDITIONAL_JUMP` [`00b8dc70`](#insn-00b8dc70) → [`00b8dc4c`](#insn-00b8dc4c)
  - `FALL_THROUGH` [`00b8dc70`](#insn-00b8dc70) → [`00b8dc74`](#insn-00b8dc74)
- ブロック [`00b8dc74`](#insn-00b8dc74) 範囲 `[['00b8dc74', '00b8dc7b']]`
  - `CONDITIONAL_JUMP` [`00b8dc78`](#insn-00b8dc78) → [`00b8dc4c`](#insn-00b8dc4c)
  - `FALL_THROUGH` [`00b8dc78`](#insn-00b8dc78) → [`00b8dc7c`](#insn-00b8dc7c)
- ブロック [`00b8dc7c`](#insn-00b8dc7c) 範囲 `[['00b8dc7c', '00b8dc87']]`
  - `CONDITIONAL_JUMP` [`00b8dc84`](#insn-00b8dc84) → [`00b8dc4c`](#insn-00b8dc4c)
  - `FALL_THROUGH` [`00b8dc84`](#insn-00b8dc84) → [`00b8dc88`](#insn-00b8dc88)
- ブロック [`00b8dc88`](#insn-00b8dc88) 範囲 `[['00b8dc88', '00b8dc97']]`
  - `FALL_THROUGH` [`00b8dc94`](#insn-00b8dc94) → [`00b8dc98`](#insn-00b8dc98)
- ブロック [`00b8dc98`](#insn-00b8dc98) 範囲 `[['00b8dc98', '00b8dca3']]`
  - `FALL_THROUGH` [`00b8dca0`](#insn-00b8dca0) → [`00b8dca4`](#insn-00b8dca4)
- ブロック [`00b8dca4`](#insn-00b8dca4) 範囲 `[['00b8dca4', '00b8dcab']]`
  - `UNCONDITIONAL_JUMP` [`00b8dca8`](#insn-00b8dca8) → [`00b8dc4c`](#insn-00b8dc4c)

## 命令位置別の参照

- [`00b8daf0`](#insn-00b8daf0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8daf4`](#insn-00b8daf4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8daf8`](#insn-00b8daf8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dafc`](#insn-00b8dafc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8db00`](#insn-00b8db00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8db0c`](#insn-00b8db0c) → `Stack[0x8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8db18`](#insn-00b8db18) → [`00b8db6c`](#insn-00b8db6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8db38`](#insn-00b8db38) → [`00b8db80`](#insn-00b8db80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8db3c`](#insn-00b8db3c) → [`00b8db80`](#insn-00b8db80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8db40`](#insn-00b8db40) → `Stack[0x0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8db50`](#insn-00b8db50) → [`00b8dc14`](#insn-00b8dc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8db68`](#insn-00b8db68) → [`00b8dc4c`](#insn-00b8dc4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8db74`](#insn-00b8db74) → [`00b8dbc0`](#insn-00b8dbc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8db7c`](#insn-00b8db7c) → [`00b8dbd0`](#insn-00b8dbd0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dba0`](#insn-00b8dba0) → [`00bdb080`](../00bdb/00bdb080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb080` · 推定シンボル `None` · 推定型 `None`
- [`00b8dbb4`](#insn-00b8dbb4) → [`00b8dbe8`](#insn-00b8dbe8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dbbc`](#insn-00b8dbbc) → [`00b8dc4c`](#insn-00b8dc4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dbc8`](#insn-00b8dbc8) → [`00b8db1c`](#insn-00b8db1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dbe4`](#insn-00b8dbe4) → [`00b8dc4c`](#insn-00b8dc4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dbf4`](#insn-00b8dbf4) → [`00b8dc08`](#insn-00b8dc08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dbfc`](#insn-00b8dbfc) → [`00b8dc1c`](#insn-00b8dc1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc04`](#insn-00b8dc04) → [`00b8dc24`](#insn-00b8dc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc0c`](#insn-00b8dc0c) → [`00b8dbb8`](#insn-00b8dbb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc10`](#insn-00b8dc10) → [`00b8dc24`](#insn-00b8dc24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc18`](#insn-00b8dc18) → [`00b8dc4c`](#insn-00b8dc4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc20`](#insn-00b8dc20) → [`00b8dc68`](#insn-00b8dc68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc2c`](#insn-00b8dc2c) → `00c1bc90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b8dc30`](#insn-00b8dc30) → `002fb026`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk114__num_get_base5__srcE` · 推定型 `string`
- [`00b8dc4c`](#insn-00b8dc4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc50`](#insn-00b8dc50) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc54`](#insn-00b8dc54) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc58`](#insn-00b8dc58) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc5c`](#insn-00b8dc5c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc70`](#insn-00b8dc70) → [`00b8dc4c`](#insn-00b8dc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc78`](#insn-00b8dc78) → [`00b8dc4c`](#insn-00b8dc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc84`](#insn-00b8dc84) → [`00b8dc4c`](#insn-00b8dc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b8dc90`](#insn-00b8dc90) → `00c1bc90`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b8dc9c`](#insn-00b8dc9c) → `002fb026`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk114__num_get_base5__srcE` · 推定型 `string`
- [`00b8dca8`](#insn-00b8dca8) → [`00b8dc4c`](#insn-00b8dc4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b8daf0`](#insn-00b8daf0)

~~~json
{
  "source": "00b8daf0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8daf4`](#insn-00b8daf4)

~~~json
{
  "source": "00b8daf4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8daf8`](#insn-00b8daf8)

~~~json
{
  "source": "00b8daf8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dafc`](#insn-00b8dafc)

~~~json
{
  "source": "00b8dafc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8db00`](#insn-00b8db00)

~~~json
{
  "source": "00b8db00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8db0c`](#insn-00b8db0c)

~~~json
{
  "source": "00b8db0c",
  "target": "Stack[0x8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8db18`](#insn-00b8db18)

~~~json
{
  "source": "00b8db18",
  "target": "00b8db6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8db38`](#insn-00b8db38)

~~~json
{
  "source": "00b8db38",
  "target": "00b8db80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8db3c`](#insn-00b8db3c)

~~~json
{
  "source": "00b8db3c",
  "target": "00b8db80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8db40`](#insn-00b8db40)

~~~json
{
  "source": "00b8db40",
  "target": "Stack[0x0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8db50`](#insn-00b8db50)

~~~json
{
  "source": "00b8db50",
  "target": "00b8dc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8db68`](#insn-00b8db68)

~~~json
{
  "source": "00b8db68",
  "target": "00b8dc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8db74`](#insn-00b8db74)

~~~json
{
  "source": "00b8db74",
  "target": "00b8dbc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8db7c`](#insn-00b8db7c)

~~~json
{
  "source": "00b8db7c",
  "target": "00b8dbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dba0`](#insn-00b8dba0)

~~~json
{
  "source": "00b8dba0",
  "target": "00bdb080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b8dbb4`](#insn-00b8dbb4)

~~~json
{
  "source": "00b8dbb4",
  "target": "00b8dbe8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dbbc`](#insn-00b8dbbc)

~~~json
{
  "source": "00b8dbbc",
  "target": "00b8dc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dbc8`](#insn-00b8dbc8)

~~~json
{
  "source": "00b8dbc8",
  "target": "00b8db1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dbe4`](#insn-00b8dbe4)

~~~json
{
  "source": "00b8dbe4",
  "target": "00b8dc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dbf4`](#insn-00b8dbf4)

~~~json
{
  "source": "00b8dbf4",
  "target": "00b8dc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dbfc`](#insn-00b8dbfc)

~~~json
{
  "source": "00b8dbfc",
  "target": "00b8dc1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc04`](#insn-00b8dc04)

~~~json
{
  "source": "00b8dc04",
  "target": "00b8dc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc0c`](#insn-00b8dc0c)

~~~json
{
  "source": "00b8dc0c",
  "target": "00b8dbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc10`](#insn-00b8dc10)

~~~json
{
  "source": "00b8dc10",
  "target": "00b8dc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc18`](#insn-00b8dc18)

~~~json
{
  "source": "00b8dc18",
  "target": "00b8dc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc20`](#insn-00b8dc20)

~~~json
{
  "source": "00b8dc20",
  "target": "00b8dc68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc2c`](#insn-00b8dc2c)

~~~json
{
  "source": "00b8dc2c",
  "target": "00c1bc90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bc90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b8dc30`](#insn-00b8dc30)

~~~json
{
  "source": "00b8dc30",
  "target": "002fb026",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fb026",
  "offset": 0,
  "size": 33,
  "datatype": "string",
  "bytes": "3031323334353637383961626364656641424344454678582b2d705069496e4e",
  "capture_start": "002fb026",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b8dc4c`](#insn-00b8dc4c)

~~~json
{
  "source": "00b8dc4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc50`](#insn-00b8dc50)

~~~json
{
  "source": "00b8dc50",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc54`](#insn-00b8dc54)

~~~json
{
  "source": "00b8dc54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc58`](#insn-00b8dc58)

~~~json
{
  "source": "00b8dc58",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc5c`](#insn-00b8dc5c)

~~~json
{
  "source": "00b8dc5c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc70`](#insn-00b8dc70)

~~~json
{
  "source": "00b8dc70",
  "target": "00b8dc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc78`](#insn-00b8dc78)

~~~json
{
  "source": "00b8dc78",
  "target": "00b8dc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc84`](#insn-00b8dc84)

~~~json
{
  "source": "00b8dc84",
  "target": "00b8dc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b8dc90`](#insn-00b8dc90)

~~~json
{
  "source": "00b8dc90",
  "target": "00c1bc90",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1bc90",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b8dc9c`](#insn-00b8dc9c)

~~~json
{
  "source": "00b8dc9c",
  "target": "002fb026",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002fb026",
  "offset": 0,
  "size": 33,
  "datatype": "string",
  "bytes": "3031323334353637383961626364656641424344454678582b2d705069496e4e",
  "capture_start": "002fb026",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b8dca8`](#insn-00b8dca8)

~~~json
{
  "source": "00b8dca8",
  "target": "00b8dc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
