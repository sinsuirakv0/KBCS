# 00bbfad0

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbfa8c`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbf/00bbfa8c.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0078.md#compare-75a549b12567d9200c67c88218008af4)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c3c518`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c3c/00c3c518.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0077.md#compare-5cce155f19abafd4c83c491489cfee39)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbfad0",
  "name": "FUN_00bbfad0",
  "size": 808,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4746c9cff12fab10f19ce2789654994d91ce964a2532c6cd324129f59fd56b75",
  "source_text_sha256": "4746c9cff12fab10f19ce2789654994d91ce964a2532c6cd324129f59fd56b75",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbfad0",
        "00bbfdf7"
      ]
    ],
    "bytes_sha256": "047c031ca74ef39151027c0ac40d88cacbcc5d3e7bc39d4f2a7d488188849a36",
    "instruction_count": 202,
    "instruction_bytes": 808,
    "body_bytes": 808,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bbd308](../00bbd/00bbd308.md)
- [00bbfad0](../00bbf/00bbfad0.md)
- [00bc1754](../00bc1/00bc1754.md)
- [00bc2f0c](../00bc2/00bc2f0c.md)

## 呼び出し先

- [00bbd308](../00bbd/00bbd308.md)
- [00bbde5c](../00bbd/00bbde5c.md)
- [00bbfad0](../00bbf/00bbfad0.md)
- [00bbff70](../00bbf/00bbff70.md)
- [00bc2f0c](../00bc2/00bc2f0c.md)
- [00bc48e0](../00bc4/00bc48e0.md)
- [00bca9c4](../00bca/00bca9c4.md)
- [00bdb180](../00bdb/00bdb180.md)
- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00bdb1d0](../00bdb/00bdb1d0.md)
- [00bdd1d0](../00bdd/00bdd1d0.md)
- [00bdd250](../00bdd/00bdd250.md)
- [00bde2c0](../00bde/00bde2c0.md)

## 関連文字列（未確認候補）

~~~text
"yptnk"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5841 bytes

~~~c

undefined8 * FUN_00bbfad0(long *param_1)

{
  long *__src;
  undefined8 *puVar1;
  long lVar2;
  long *__ptr;
  void *pvVar3;
  char *pcVar4;
  long lVar5;
  byte *pbVar6;
  long lVar7;
  undefined **ppuVar8;
  undefined1 uVar9;
  byte *pbVar10;
  uint uVar11;
  size_t __n;
  long *plVar12;
  undefined1 auVar13 [16];
  
  pbVar6 = (byte *)*param_1;
  pbVar10 = (byte *)param_1[1];
  if (pbVar10 == pbVar6) {
    uVar11 = 0;
  }
  else {
    uVar11 = (uint)*pbVar6;
  }
  uVar11 = uVar11 - 0x4a >> 1 | uVar11 << 0x1f;
                    /* try { // try from 00bbfb0c to 00cbfb0f has its CatchHandler @ 00bc8b2c */
  if ((int)uVar11 < 5) {
    if (uVar11 == 0) {
      lVar7 = param_1[2];
      lVar5 = param_1[3];
      pbVar6 = pbVar6 + 1;
      __src = param_1 + 5;
      *param_1 = (long)pbVar6;
      while ((pbVar6 == pbVar10 || (*pbVar6 != 0x45))) {
        lVar2 = FUN_00bbfad0(param_1);
        if (lVar2 == 0) {
          return (undefined8 *)0x0;
        }
        plVar12 = (long *)param_1[3];
        if (plVar12 == (long *)param_1[4]) {
          __ptr = (long *)param_1[2];
          __n = (long)plVar12 - (long)__ptr;
          if (__ptr == __src) {
            pvVar3 = malloc(__n * 2);
            if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
              abort();
            }
            if (plVar12 != __src) {
              memcpy(pvVar3,__src,__n);
            }
                    /* try { // try from 00bbfc4c to 00cbfc5f has its CatchHandler @ 00bc87ec */
            param_1[2] = (long)pvVar3;
          }
          else {
            pvVar3 = realloc(__ptr,__n * 2);
            param_1[2] = (long)pvVar3;
            if (pvVar3 == (void *)0x0) {
                    /* WARNING: Subroutine does not return */
              abort();
            }
          }
          plVar12 = (long *)((long)pvVar3 + __n);
          param_1[4] = (long)((long)pvVar3 + ((long)__n >> 2) * 8);
        }
        param_1[3] = (long)(plVar12 + 1);
                    /* try { // try from 00bbfbd8 to 00cbfbdb has its CatchHandler @ 00bc8890 */
        *plVar12 = lVar2;
        pbVar10 = (byte *)param_1[1];
                    /* try { // try from 00bbfbdc to 00cbfc4b has its CatchHandler @ 00bbf570 */
        pbVar6 = (byte *)*param_1;
      }
      *param_1 = (long)(pbVar6 + 1);
      auVar13 = FUN_00bbff70(param_1,lVar5 - lVar7 >> 3);
      pvVar3 = (void *)param_1[0x266];
                    /* try { // try from 00bbfcb4 to 00cbfcbf has its CatchHandler @ 00bc8a70 */
      lVar7 = *(long *)((long)pvVar3 + 8);
                    /* try { // try from 00bbfcc0 to 00cbfccf has its CatchHandler @ 00bc8a68 */
      puVar1 = pvVar3;
      if (lVar7 - 0xfd0U < 0xfffffffffffff010) {
        puVar1 = malloc(0x1000);
        if (puVar1 == (void *)0x0) {
LAB_00bbfdf4:
                    /* WARNING: Subroutine does not return */
          _ZSt9terminatev();
        }
        lVar7 = 0;
        *puVar1 = pvVar3;
        puVar1[1] = 0;
        param_1[0x266] = (long)puVar1;
      }
      lVar5 = (long)puVar1 + lVar7;
                    /* try { // try from 00bbfcf0 to 00cbfd63 has its CatchHandler @ 00bc8bc4 */
      ppuVar8 = &PTR_FUN_00c19808;
      *(long *)((long)puVar1 + 8) = lVar7 + 0x20;
      uVar9 = 0x29;
LAB_00bbfd00:
      *(undefined8 *)(lVar5 + 0x10) = ppuVar8;
      *(undefined1 *)(lVar5 + 0x18) = uVar9;
      *(undefined1 (*) [16])(lVar5 + 0x20) = auVar13;
      *(ushort *)(lVar5 + 0x19) = *(ushort *)(lVar5 + 0x19) & 0xf000 | 0x540;
      return (undefined8 *)(lVar5 + 0x10);
    }
    if (uVar11 == 1) {
      if (((ulong)((long)pbVar10 - (long)pbVar6) < 2) || (pbVar6[1] != 0x5a)) {
        puVar1 = (undefined8 *)FUN_00bc48e0(param_1);
        return puVar1;
      }
      *param_1 = (long)(pbVar6 + 2);
      puVar1 = (undefined8 *)FUN_00bbd308(param_1);
joined_r0x00bbfb6c:
      if (puVar1 != (undefined8 *)0x0) {
        pcVar4 = (char *)*param_1;
                    /* try { // try from 00bbfb74 to 00cbfb77 has its CatchHandler @ 00bc8ad0 */
        if ((pcVar4 == (char *)param_1[1]) || (*pcVar4 != 'E')) {
          puVar1 = (undefined8 *)0x0;
        }
        else {
          *param_1 = (long)(pcVar4 + 1);
        }
      }
      return puVar1;
    }
  }
  else if (uVar11 == 5) {
    if ((pbVar10 != pbVar6) && (*pbVar6 == 0x54)) {
      if ((ulong)((long)pbVar10 - (long)pbVar6) < 2) {
        uVar11 = 0;
      }
      else {
        uVar11 = (uint)pbVar6[1];
      }
      pcVar4 = memchr("yptnk",uVar11,5);
      if ((pcVar4 != (char *)0x0) && (pcVar4 != "")) {
        lVar7 = FUN_00bca9c4(param_1,0);
        if (lVar7 == 0) {
          return (undefined8 *)0x0;
        }
        lVar5 = FUN_00bbfad0(param_1);
        auVar13._8_8_ = lVar5;
        auVar13._0_8_ = lVar7;
                    /* try { // try from 00bbfd7c to 00cbfd83 has its CatchHandler @ 00bc8b2c */
        if (lVar5 == 0) {
          return (undefined8 *)0x0;
        }
        pvVar3 = (void *)param_1[0x266];
        lVar7 = *(long *)((long)pvVar3 + 8);
        puVar1 = pvVar3;
        if (lVar7 - 0xfd0U < 0xfffffffffffff010) {
          puVar1 = malloc(0x1000);
          if (puVar1 == (void *)0x0) goto LAB_00bbfdf4;
          lVar7 = 0;
          *puVar1 = pvVar3;
          puVar1[1] = 0;
                    /* try { // try from 00bbfdac to 00cbfdbf has its CatchHandler @ 00bc87e8 */
          param_1[0x266] = (long)puVar1;
        }
        lVar5 = (long)puVar1 + lVar7;
        ppuVar8 = &PTR_FUN_00c19878;
        *(long *)((long)puVar1 + 8) = lVar7 + 0x20;
        uVar9 = 0x22;
        goto LAB_00bbfd00;
      }
    }
  }
  else if (uVar11 == 7) {
    *param_1 = (long)(pbVar6 + 1);
    puVar1 = (undefined8 *)FUN_00bc2f0c(param_1);
    goto joined_r0x00bbfb6c;
  }
  puVar1 = (undefined8 *)FUN_00bbde5c(param_1);
  return puVar1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbfad0"></a> `00bbfad0` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbfad4"></a> `00bbfad4` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bbfad8"></a> `00bbfad8` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfadc"></a> `00bbfadc` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfae0"></a> `00bbfae0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfae4"></a> `00bbfae4` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bbfae8"></a> `00bbfae8` | `08 24 40 a9` | ldp x8,x9,[x0] | `FALL_THROUGH`
<a id="insn-00bbfaec"></a> `00bbfaec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbfaf0"></a> `00bbfaf0` | `2a 01 08 eb` | subs x10,x9,x8 | `FALL_THROUGH`
<a id="insn-00bbfaf4"></a> `00bbfaf4` | `60 00 00 54` | b.eq 0x00bbfb00 | `CONDITIONAL_JUMP`
<a id="insn-00bbfaf8"></a> `00bbfaf8` | `0b 01 40 39` | ldrb w11,[x8] | `FALL_THROUGH`
<a id="insn-00bbfafc"></a> `00bbfafc` | `02 00 00 14` | b 0x00bbfb04 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfb00"></a> `00bbfb00` | `eb 03 1f 2a` | mov w11,wzr | `FALL_THROUGH`
<a id="insn-00bbfb04"></a> `00bbfb04` | `6b 29 01 51` | sub w11,w11,#0x4a | `FALL_THROUGH`
<a id="insn-00bbfb08"></a> `00bbfb08` | `6b 05 8b 13` | ror w11,w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfb0c"></a> `00bbfb0c` | `7f 11 00 71` | cmp w11,#0x4 | `FALL_THROUGH`
<a id="insn-00bbfb10"></a> `00bbfb10` | `ec 01 00 54` | b.gt 0x00bbfb4c | `CONDITIONAL_JUMP`
<a id="insn-00bbfb14"></a> `00bbfb14` | `0b 04 00 34` | cbz w11,0x00bbfb94 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb18"></a> `00bbfb18` | `7f 05 00 71` | cmp w11,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfb1c"></a> `00bbfb1c` | `a1 15 00 54` | b.ne 0x00bbfdd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb20"></a> `00bbfb20` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfb24"></a> `00bbfb24` | `a3 0a 00 54` | b.cc 0x00bbfc78 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb28"></a> `00bbfb28` | `09 05 40 39` | ldrb w9,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bbfb2c"></a> `00bbfb2c` | `3f 69 01 71` | cmp w9,#0x5a | `FALL_THROUGH`
<a id="insn-00bbfb30"></a> `00bbfb30` | `41 0a 00 54` | b.ne 0x00bbfc78 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb34"></a> `00bbfb34` | `08 09 00 91` | add x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfb38"></a> `00bbfb38` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfb3c"></a> `00bbfb3c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb40"></a> `00bbfb40` | `f2 f5 ff 97` | bl 0x00bbd308 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfb44"></a> `00bbfb44` | `60 01 00 b5` | cbnz x0,0x00bbfb70 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb48"></a> `00bbfb48` | `76 00 00 14` | b 0x00bbfd20 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfb4c"></a> `00bbfb4c` | `7f 15 00 71` | cmp w11,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfb50"></a> `00bbfb50` | `20 08 00 54` | b.eq 0x00bbfc54 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb54"></a> `00bbfb54` | `7f 1d 00 71` | cmp w11,#0x7 | `FALL_THROUGH`
<a id="insn-00bbfb58"></a> `00bbfb58` | `c1 13 00 54` | b.ne 0x00bbfdd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb5c"></a> `00bbfb5c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfb60"></a> `00bbfb60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfb64"></a> `00bbfb64` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb68"></a> `00bbfb68` | `e9 0c 00 94` | bl 0x00bc2f0c | `UNCONDITIONAL_CALL`
<a id="insn-00bbfb6c"></a> `00bbfb6c` | `a0 0d 00 b4` | cbz x0,0x00bbfd20 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb70"></a> `00bbfb70` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb74"></a> `00bbfb74` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbfb78"></a> `00bbfb78` | `e0 08 00 54` | b.eq 0x00bbfc94 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb7c"></a> `00bbfb7c` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbfb80"></a> `00bbfb80` | `3f 15 01 71` | cmp w9,#0x45 | `FALL_THROUGH`
<a id="insn-00bbfb84"></a> `00bbfb84` | `81 08 00 54` | b.ne 0x00bbfc94 | `CONDITIONAL_JUMP`
<a id="insn-00bbfb88"></a> `00bbfb88` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfb8c"></a> `00bbfb8c` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbfb90"></a> `00bbfb90` | `64 00 00 14` | b 0x00bbfd20 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfb94"></a> `00bbfb94` | `6b 2a 41 a9` | ldp x11,x10,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfb98"></a> `00bbfb98` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfb9c"></a> `00bbfb9c` | `75 a2 00 91` | add x21,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bbfba0"></a> `00bbfba0` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbfba4"></a> `00bbfba4` | `4a 01 0b cb` | sub x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bbfba8"></a> `00bbfba8` | `54 fd 43 93` | asr x20,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bbfbac"></a> `00bbfbac` | `0d 00 00 14` | b 0x00bbfbe0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfbb0"></a> `00bbfbb0` | `a8 75 00 94` | bl 0x00bdd250 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfbb4"></a> `00bbfbb4` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfbb8"></a> `00bbfbb8` | `a0 11 00 b4` | cbz x0,0x00bbfdec | `CONDITIONAL_JUMP`
<a id="insn-00bbfbbc"></a> `00bbfbbc` | `c8 fe 42 93` | asr x8,x22,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfbc0"></a> `00bbfbc0` | `17 00 16 8b` | add x23,x0,x22 | `FALL_THROUGH`
<a id="insn-00bbfbc4"></a> `00bbfbc4` | `08 0c 08 8b` | add x8,x0,x8, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bbfbc8"></a> `00bbfbc8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbfbcc"></a> `00bbfbcc` | `68 12 00 f9` | str x8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfbd0"></a> `00bbfbd0` | `e8 22 00 91` | add x8,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00bbfbd4"></a> `00bbfbd4` | `68 0e 00 f9` | str x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfbd8"></a> `00bbfbd8` | `e0 02 00 f9` | str x0,[x23] | `FALL_THROUGH`
<a id="insn-00bbfbdc"></a> `00bbfbdc` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-00bbfbe0"></a> `00bbfbe0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbfbe4"></a> `00bbfbe4` | `80 00 00 54` | b.eq 0x00bbfbf4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfbe8"></a> `00bbfbe8` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbfbec"></a> `00bbfbec` | `3f 15 01 71` | cmp w9,#0x45 | `FALL_THROUGH`
<a id="insn-00bbfbf0"></a> `00bbfbf0` | `60 05 00 54` | b.eq 0x00bbfc9c | `CONDITIONAL_JUMP`
<a id="insn-00bbfbf4"></a> `00bbfbf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfbf8"></a> `00bbfbf8` | `b6 ff ff 97` | bl 0x00bbfad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfbfc"></a> `00bbfbfc` | `20 09 00 b4` | cbz x0,0x00bbfd20 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc00"></a> `00bbfc00` | `77 a2 41 a9` | ldp x23,x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bbfc04"></a> `00bbfc04` | `ff 02 08 eb` | cmp x23,x8 | `FALL_THROUGH`
<a id="insn-00bbfc08"></a> `00bbfc08` | `41 fe ff 54` | b.ne 0x00bbfbd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc0c"></a> `00bbfc0c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bbfc10"></a> `00bbfc10` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfc14"></a> `00bbfc14` | `f6 02 00 cb` | sub x22,x23,x0 | `FALL_THROUGH`
<a id="insn-00bbfc18"></a> `00bbfc18` | `1f 00 15 eb` | cmp x0,x21 | `FALL_THROUGH`
<a id="insn-00bbfc1c"></a> `00bbfc1c` | `c1 fa 7f d3` | lsl x1,x22,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfc20"></a> `00bbfc20` | `81 fc ff 54` | b.ne 0x00bbfbb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc24"></a> `00bbfc24` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bbfc28"></a> `00bbfc28` | `6a 75 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfc2c"></a> `00bbfc2c` | `20 0e 00 b4` | cbz x0,0x00bbfdf0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc30"></a> `00bbfc30` | `ff 02 15 eb` | cmp x23,x21 | `FALL_THROUGH`
<a id="insn-00bbfc34"></a> `00bbfc34` | `c0 00 00 54` | b.eq 0x00bbfc4c | `CONDITIONAL_JUMP`
<a id="insn-00bbfc38"></a> `00bbfc38` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbfc3c"></a> `00bbfc3c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bbfc40"></a> `00bbfc40` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbfc44"></a> `00bbfc44` | `5b 6d 00 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfc48"></a> `00bbfc48` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbfc4c"></a> `00bbfc4c` | `60 0a 00 f9` | str x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfc50"></a> `00bbfc50` | `db ff ff 17` | b 0x00bbfbbc | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfc54"></a> `00bbfc54` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bbfc58"></a> `00bbfc58` | `c0 0b 00 54` | b.eq 0x00bbfdd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc5c"></a> `00bbfc5c` | `09 01 40 39` | ldrb w9,[x8] | `FALL_THROUGH`
<a id="insn-00bbfc60"></a> `00bbfc60` | `3f 51 01 71` | cmp w9,#0x54 | `FALL_THROUGH`
<a id="insn-00bbfc64"></a> `00bbfc64` | `61 0b 00 54` | b.ne 0x00bbfdd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc68"></a> `00bbfc68` | `5f 09 00 f1` | cmp x10,#0x2 | `FALL_THROUGH`
<a id="insn-00bbfc6c"></a> `00bbfc6c` | `63 06 00 54` | b.cc 0x00bbfd38 | `CONDITIONAL_JUMP`
<a id="insn-00bbfc70"></a> `00bbfc70` | `01 05 40 39` | ldrb w1,[x8, #0x1] | `FALL_THROUGH`
<a id="insn-00bbfc74"></a> `00bbfc74` | `32 00 00 14` | b 0x00bbfd3c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfc78"></a> `00bbfc78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfc7c"></a> `00bbfc7c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfc80"></a> `00bbfc80` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfc84"></a> `00bbfc84` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfc88"></a> `00bbfc88` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbfc8c"></a> `00bbfc8c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbfc90"></a> `00bbfc90` | `14 13 00 14` | b 0x00bc48e0 | `CALL_TERMINATOR`
<a id="insn-00bbfc94"></a> `00bbfc94` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bbfc98"></a> `00bbfc98` | `22 00 00 14` | b 0x00bbfd20 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfc9c"></a> `00bbfc9c` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfca0"></a> `00bbfca0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfca4"></a> `00bbfca4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bbfca8"></a> `00bbfca8` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bbfcac"></a> `00bbfcac` | `b1 00 00 94` | bl 0x00bbff70 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfcb0"></a> `00bbfcb0` | `76 9a 49 f9` | ldr x22,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfcb4"></a> `00bbfcb4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbfcb8"></a> `00bbfcb8` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bbfcbc"></a> `00bbfcbc` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfcc0"></a> `00bbfcc0` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbfcc4"></a> `00bbfcc4` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbfcc8"></a> `00bbfcc8` | `08 01 00 54` | b.hi 0x00bbfce8 | `CONDITIONAL_JUMP`
<a id="insn-00bbfccc"></a> `00bbfccc` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbfcd0"></a> `00bbfcd0` | `40 75 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfcd4"></a> `00bbfcd4` | `00 09 00 b4` | cbz x0,0x00bbfdf4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfcd8"></a> `00bbfcd8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbfcdc"></a> `00bbfcdc` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbfce0"></a> `00bbfce0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbfce4"></a> `00bbfce4` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfce8"></a> `00bbfce8` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfcec"></a> `00bbfcec` | `c0 02 08 8b` | add x0,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbfcf0"></a> `00bbfcf0` | `c8 02 00 d0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bbfcf4"></a> `00bbfcf4` | `08 21 20 91` | add x8,x8,#0x808 | `FALL_THROUGH`
<a id="insn-00bbfcf8"></a> `00bbfcf8` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfcfc"></a> `00bbfcfc` | `29 05 80 52` | mov w9,#0x29 | `FALL_THROUGH`
<a id="insn-00bbfd00"></a> `00bbfd00` | `08 0c 01 f8` | str x8,[x0, #0x10]! | `FALL_THROUGH`
<a id="insn-00bbfd04"></a> `00bbfd04` | `08 90 40 78` | ldurh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbfd08"></a> `00bbfd08` | `0a a8 80 52` | mov w10,#0x540 | `FALL_THROUGH`
<a id="insn-00bbfd0c"></a> `00bbfd0c` | `08 0d 14 12` | and w8,w8,#0xf000 | `FALL_THROUGH`
<a id="insn-00bbfd10"></a> `00bbfd10` | `09 20 00 39` | strb w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfd14"></a> `00bbfd14` | `08 01 0a 2a` | orr w8,w8,w10 | `FALL_THROUGH`
<a id="insn-00bbfd18"></a> `00bbfd18` | `14 54 01 a9` | stp x20,x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfd1c"></a> `00bbfd1c` | `08 90 00 78` | sturh w8,[x0, #0x9] | `FALL_THROUGH`
<a id="insn-00bbfd20"></a> `00bbfd20` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfd24"></a> `00bbfd24` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfd28"></a> `00bbfd28` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfd2c"></a> `00bbfd2c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbfd30"></a> `00bbfd30` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbfd34"></a> `00bbfd34` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbfd38"></a> `00bbfd38` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bbfd3c"></a> `00bbfd3c` | `b4 b6 ff d0` | adrp x20,0x295000 | `FALL_THROUGH`
<a id="insn-00bbfd40"></a> `00bbfd40` | `94 e6 1d 91` | add x20,x20,#0x779 | `FALL_THROUGH`
<a id="insn-00bbfd44"></a> `00bbfd44` | `a2 00 80 52` | mov w2,#0x5 | `FALL_THROUGH`
<a id="insn-00bbfd48"></a> `00bbfd48` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbfd4c"></a> `00bbfd4c` | `0d 6d 00 94` | bl 0x00bdb180 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfd50"></a> `00bbfd50` | `00 04 00 b4` | cbz x0,0x00bbfdd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd54"></a> `00bbfd54` | `08 00 14 cb` | sub x8,x0,x20 | `FALL_THROUGH`
<a id="insn-00bbfd58"></a> `00bbfd58` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbfd5c"></a> `00bbfd5c` | `a0 03 00 54` | b.eq 0x00bbfdd0 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd60"></a> `00bbfd60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfd64"></a> `00bbfd64` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bbfd68"></a> `00bbfd68` | `17 2b 00 94` | bl 0x00bca9c4 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfd6c"></a> `00bbfd6c` | `a0 fd ff b4` | cbz x0,0x00bbfd20 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd70"></a> `00bbfd70` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bbfd74"></a> `00bbfd74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfd78"></a> `00bbfd78` | `56 ff ff 97` | bl 0x00bbfad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfd7c"></a> `00bbfd7c` | `20 fd ff b4` | cbz x0,0x00bbfd20 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd80"></a> `00bbfd80` | `76 9a 49 f9` | ldr x22,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfd84"></a> `00bbfd84` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbfd88"></a> `00bbfd88` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfd8c"></a> `00bbfd8c` | `09 41 3f d1` | sub x9,x8,#0xfd0 | `FALL_THROUGH`
<a id="insn-00bbfd90"></a> `00bbfd90` | `3f c5 3f b1` | cmn x9,#0xff1 | `FALL_THROUGH`
<a id="insn-00bbfd94"></a> `00bbfd94` | `08 01 00 54` | b.hi 0x00bbfdb4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfd98"></a> `00bbfd98` | `00 00 82 52` | mov w0,#0x1000 | `FALL_THROUGH`
<a id="insn-00bbfd9c"></a> `00bbfd9c` | `0d 75 00 94` | bl 0x00bdd1d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbfda0"></a> `00bbfda0` | `a0 02 00 b4` | cbz x0,0x00bbfdf4 | `CONDITIONAL_JUMP`
<a id="insn-00bbfda4"></a> `00bbfda4` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbfda8"></a> `00bbfda8` | `16 7c 00 a9` | stp x22,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bbfdac"></a> `00bbfdac` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bbfdb0"></a> `00bbfdb0` | `60 9a 09 f9` | str x0,[x19, #0x1330] | `FALL_THROUGH`
<a id="insn-00bbfdb4"></a> `00bbfdb4` | `09 81 00 91` | add x9,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00bbfdb8"></a> `00bbfdb8` | `c0 02 08 8b` | add x0,x22,x8 | `FALL_THROUGH`
<a id="insn-00bbfdbc"></a> `00bbfdbc` | `c8 02 00 d0` | adrp x8,0xc19000 | `FALL_THROUGH`
<a id="insn-00bbfdc0"></a> `00bbfdc0` | `08 e1 21 91` | add x8,x8,#0x878 | `FALL_THROUGH`
<a id="insn-00bbfdc4"></a> `00bbfdc4` | `c9 06 00 f9` | str x9,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bbfdc8"></a> `00bbfdc8` | `49 04 80 52` | mov w9,#0x22 | `FALL_THROUGH`
<a id="insn-00bbfdcc"></a> `00bbfdcc` | `cd ff ff 17` | b 0x00bbfd00 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbfdd0"></a> `00bbfdd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbfdd4"></a> `00bbfdd4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbfdd8"></a> `00bbfdd8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbfddc"></a> `00bbfddc` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbfde0"></a> `00bbfde0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bbfde4"></a> `00bbfde4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbfde8"></a> `00bbfde8` | `1d f8 ff 17` | b 0x00bbde5c | `CALL_TERMINATOR`
<a id="insn-00bbfdec"></a> `00bbfdec` | `35 79 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bbfdf0"></a> `00bbfdf0` | `34 79 00 94` | bl 0x00bde2c0 | `CALL_TERMINATOR`
<a id="insn-00bbfdf4"></a> `00bbfdf4` | `f7 6c 00 94` | bl 0x00bdb1d0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbfad0`](#insn-00bbfad0) 範囲 `[['00bbfad0', '00bbfaf7']]`
  - `CONDITIONAL_JUMP` [`00bbfaf4`](#insn-00bbfaf4) → [`00bbfb00`](#insn-00bbfb00)
  - `FALL_THROUGH` [`00bbfaf4`](#insn-00bbfaf4) → [`00bbfaf8`](#insn-00bbfaf8)
- ブロック [`00bbfaf8`](#insn-00bbfaf8) 範囲 `[['00bbfaf8', '00bbfaff']]`
  - `UNCONDITIONAL_JUMP` [`00bbfafc`](#insn-00bbfafc) → [`00bbfb04`](#insn-00bbfb04)
- ブロック [`00bbfb00`](#insn-00bbfb00) 範囲 `[['00bbfb00', '00bbfb03']]`
  - `FALL_THROUGH` [`00bbfb00`](#insn-00bbfb00) → [`00bbfb04`](#insn-00bbfb04)
- ブロック [`00bbfb04`](#insn-00bbfb04) 範囲 `[['00bbfb04', '00bbfb0b']]`
  - `FALL_THROUGH` [`00bbfb08`](#insn-00bbfb08) → [`00bbfb0c`](#insn-00bbfb0c)
- ブロック [`00bbfb0c`](#insn-00bbfb0c) 範囲 `[['00bbfb0c', '00bbfb13']]`
  - `CONDITIONAL_JUMP` [`00bbfb10`](#insn-00bbfb10) → [`00bbfb4c`](#insn-00bbfb4c)
  - `FALL_THROUGH` [`00bbfb10`](#insn-00bbfb10) → [`00bbfb14`](#insn-00bbfb14)
- ブロック [`00bbfb14`](#insn-00bbfb14) 範囲 `[['00bbfb14', '00bbfb17']]`
  - `CONDITIONAL_JUMP` [`00bbfb14`](#insn-00bbfb14) → [`00bbfb94`](#insn-00bbfb94)
  - `FALL_THROUGH` [`00bbfb14`](#insn-00bbfb14) → [`00bbfb18`](#insn-00bbfb18)
- ブロック [`00bbfb18`](#insn-00bbfb18) 範囲 `[['00bbfb18', '00bbfb1f']]`
  - `CONDITIONAL_JUMP` [`00bbfb1c`](#insn-00bbfb1c) → [`00bbfdd0`](#insn-00bbfdd0)
  - `FALL_THROUGH` [`00bbfb1c`](#insn-00bbfb1c) → [`00bbfb20`](#insn-00bbfb20)
- ブロック [`00bbfb20`](#insn-00bbfb20) 範囲 `[['00bbfb20', '00bbfb27']]`
  - `CONDITIONAL_JUMP` [`00bbfb24`](#insn-00bbfb24) → [`00bbfc78`](#insn-00bbfc78)
  - `FALL_THROUGH` [`00bbfb24`](#insn-00bbfb24) → [`00bbfb28`](#insn-00bbfb28)
- ブロック [`00bbfb28`](#insn-00bbfb28) 範囲 `[['00bbfb28', '00bbfb33']]`
  - `CONDITIONAL_JUMP` [`00bbfb30`](#insn-00bbfb30) → [`00bbfc78`](#insn-00bbfc78)
  - `FALL_THROUGH` [`00bbfb30`](#insn-00bbfb30) → [`00bbfb34`](#insn-00bbfb34)
- ブロック [`00bbfb34`](#insn-00bbfb34) 範囲 `[['00bbfb34', '00bbfb47']]`
  - `CONDITIONAL_JUMP` [`00bbfb44`](#insn-00bbfb44) → [`00bbfb70`](#insn-00bbfb70)
  - `FALL_THROUGH` [`00bbfb44`](#insn-00bbfb44) → [`00bbfb48`](#insn-00bbfb48)
- ブロック [`00bbfb48`](#insn-00bbfb48) 範囲 `[['00bbfb48', '00bbfb4b']]`
  - `UNCONDITIONAL_JUMP` [`00bbfb48`](#insn-00bbfb48) → [`00bbfd20`](#insn-00bbfd20)
- ブロック [`00bbfb4c`](#insn-00bbfb4c) 範囲 `[['00bbfb4c', '00bbfb53']]`
  - `CONDITIONAL_JUMP` [`00bbfb50`](#insn-00bbfb50) → [`00bbfc54`](#insn-00bbfc54)
  - `FALL_THROUGH` [`00bbfb50`](#insn-00bbfb50) → [`00bbfb54`](#insn-00bbfb54)
- ブロック [`00bbfb54`](#insn-00bbfb54) 範囲 `[['00bbfb54', '00bbfb5b']]`
  - `CONDITIONAL_JUMP` [`00bbfb58`](#insn-00bbfb58) → [`00bbfdd0`](#insn-00bbfdd0)
  - `FALL_THROUGH` [`00bbfb58`](#insn-00bbfb58) → [`00bbfb5c`](#insn-00bbfb5c)
- ブロック [`00bbfb5c`](#insn-00bbfb5c) 範囲 `[['00bbfb5c', '00bbfb6f']]`
  - `CONDITIONAL_JUMP` [`00bbfb6c`](#insn-00bbfb6c) → [`00bbfd20`](#insn-00bbfd20)
  - `FALL_THROUGH` [`00bbfb6c`](#insn-00bbfb6c) → [`00bbfb70`](#insn-00bbfb70)
- ブロック [`00bbfb70`](#insn-00bbfb70) 範囲 `[['00bbfb70', '00bbfb73']]`
  - `FALL_THROUGH` [`00bbfb70`](#insn-00bbfb70) → [`00bbfb74`](#insn-00bbfb74)
- ブロック [`00bbfb74`](#insn-00bbfb74) 範囲 `[['00bbfb74', '00bbfb7b']]`
  - `CONDITIONAL_JUMP` [`00bbfb78`](#insn-00bbfb78) → [`00bbfc94`](#insn-00bbfc94)
  - `FALL_THROUGH` [`00bbfb78`](#insn-00bbfb78) → [`00bbfb7c`](#insn-00bbfb7c)
- ブロック [`00bbfb7c`](#insn-00bbfb7c) 範囲 `[['00bbfb7c', '00bbfb87']]`
  - `CONDITIONAL_JUMP` [`00bbfb84`](#insn-00bbfb84) → [`00bbfc94`](#insn-00bbfc94)
  - `FALL_THROUGH` [`00bbfb84`](#insn-00bbfb84) → [`00bbfb88`](#insn-00bbfb88)
- ブロック [`00bbfb88`](#insn-00bbfb88) 範囲 `[['00bbfb88', '00bbfb93']]`
  - `UNCONDITIONAL_JUMP` [`00bbfb90`](#insn-00bbfb90) → [`00bbfd20`](#insn-00bbfd20)
- ブロック [`00bbfb94`](#insn-00bbfb94) 範囲 `[['00bbfb94', '00bbfbaf']]`
  - `UNCONDITIONAL_JUMP` [`00bbfbac`](#insn-00bbfbac) → [`00bbfbe0`](#insn-00bbfbe0)
- ブロック [`00bbfbb0`](#insn-00bbfbb0) 範囲 `[['00bbfbb0', '00bbfbbb']]`
  - `CONDITIONAL_JUMP` [`00bbfbb8`](#insn-00bbfbb8) → [`00bbfdec`](#insn-00bbfdec)
  - `FALL_THROUGH` [`00bbfbb8`](#insn-00bbfbb8) → [`00bbfbbc`](#insn-00bbfbbc)
- ブロック [`00bbfbbc`](#insn-00bbfbbc) 範囲 `[['00bbfbbc', '00bbfbcf']]`
  - `FALL_THROUGH` [`00bbfbcc`](#insn-00bbfbcc) → [`00bbfbd0`](#insn-00bbfbd0)
- ブロック [`00bbfbd0`](#insn-00bbfbd0) 範囲 `[['00bbfbd0', '00bbfbd7']]`
  - `FALL_THROUGH` [`00bbfbd4`](#insn-00bbfbd4) → [`00bbfbd8`](#insn-00bbfbd8)
- ブロック [`00bbfbd8`](#insn-00bbfbd8) 範囲 `[['00bbfbd8', '00bbfbdb']]`
  - `FALL_THROUGH` [`00bbfbd8`](#insn-00bbfbd8) → [`00bbfbdc`](#insn-00bbfbdc)
- ブロック [`00bbfbdc`](#insn-00bbfbdc) 範囲 `[['00bbfbdc', '00bbfbdf']]`
  - `FALL_THROUGH` [`00bbfbdc`](#insn-00bbfbdc) → [`00bbfbe0`](#insn-00bbfbe0)
- ブロック [`00bbfbe0`](#insn-00bbfbe0) 範囲 `[['00bbfbe0', '00bbfbe7']]`
  - `CONDITIONAL_JUMP` [`00bbfbe4`](#insn-00bbfbe4) → [`00bbfbf4`](#insn-00bbfbf4)
  - `FALL_THROUGH` [`00bbfbe4`](#insn-00bbfbe4) → [`00bbfbe8`](#insn-00bbfbe8)
- ブロック [`00bbfbe8`](#insn-00bbfbe8) 範囲 `[['00bbfbe8', '00bbfbf3']]`
  - `CONDITIONAL_JUMP` [`00bbfbf0`](#insn-00bbfbf0) → [`00bbfc9c`](#insn-00bbfc9c)
  - `FALL_THROUGH` [`00bbfbf0`](#insn-00bbfbf0) → [`00bbfbf4`](#insn-00bbfbf4)
- ブロック [`00bbfbf4`](#insn-00bbfbf4) 範囲 `[['00bbfbf4', '00bbfbff']]`
  - `CONDITIONAL_JUMP` [`00bbfbfc`](#insn-00bbfbfc) → [`00bbfd20`](#insn-00bbfd20)
  - `FALL_THROUGH` [`00bbfbfc`](#insn-00bbfbfc) → [`00bbfc00`](#insn-00bbfc00)
- ブロック [`00bbfc00`](#insn-00bbfc00) 範囲 `[['00bbfc00', '00bbfc0b']]`
  - `CONDITIONAL_JUMP` [`00bbfc08`](#insn-00bbfc08) → [`00bbfbd0`](#insn-00bbfbd0)
  - `FALL_THROUGH` [`00bbfc08`](#insn-00bbfc08) → [`00bbfc0c`](#insn-00bbfc0c)
- ブロック [`00bbfc0c`](#insn-00bbfc0c) 範囲 `[['00bbfc0c', '00bbfc23']]`
  - `CONDITIONAL_JUMP` [`00bbfc20`](#insn-00bbfc20) → [`00bbfbb0`](#insn-00bbfbb0)
  - `FALL_THROUGH` [`00bbfc20`](#insn-00bbfc20) → [`00bbfc24`](#insn-00bbfc24)
- ブロック [`00bbfc24`](#insn-00bbfc24) 範囲 `[['00bbfc24', '00bbfc2f']]`
  - `CONDITIONAL_JUMP` [`00bbfc2c`](#insn-00bbfc2c) → [`00bbfdf0`](#insn-00bbfdf0)
  - `FALL_THROUGH` [`00bbfc2c`](#insn-00bbfc2c) → [`00bbfc30`](#insn-00bbfc30)
- ブロック [`00bbfc30`](#insn-00bbfc30) 範囲 `[['00bbfc30', '00bbfc37']]`
  - `CONDITIONAL_JUMP` [`00bbfc34`](#insn-00bbfc34) → [`00bbfc4c`](#insn-00bbfc4c)
  - `FALL_THROUGH` [`00bbfc34`](#insn-00bbfc34) → [`00bbfc38`](#insn-00bbfc38)
- ブロック [`00bbfc38`](#insn-00bbfc38) 範囲 `[['00bbfc38', '00bbfc4b']]`
  - `FALL_THROUGH` [`00bbfc48`](#insn-00bbfc48) → [`00bbfc4c`](#insn-00bbfc4c)
- ブロック [`00bbfc4c`](#insn-00bbfc4c) 範囲 `[['00bbfc4c', '00bbfc53']]`
  - `UNCONDITIONAL_JUMP` [`00bbfc50`](#insn-00bbfc50) → [`00bbfbbc`](#insn-00bbfbbc)
- ブロック [`00bbfc54`](#insn-00bbfc54) 範囲 `[['00bbfc54', '00bbfc5b']]`
  - `CONDITIONAL_JUMP` [`00bbfc58`](#insn-00bbfc58) → [`00bbfdd0`](#insn-00bbfdd0)
  - `FALL_THROUGH` [`00bbfc58`](#insn-00bbfc58) → [`00bbfc5c`](#insn-00bbfc5c)
- ブロック [`00bbfc5c`](#insn-00bbfc5c) 範囲 `[['00bbfc5c', '00bbfc67']]`
  - `CONDITIONAL_JUMP` [`00bbfc64`](#insn-00bbfc64) → [`00bbfdd0`](#insn-00bbfdd0)
  - `FALL_THROUGH` [`00bbfc64`](#insn-00bbfc64) → [`00bbfc68`](#insn-00bbfc68)
- ブロック [`00bbfc68`](#insn-00bbfc68) 範囲 `[['00bbfc68', '00bbfc6f']]`
  - `CONDITIONAL_JUMP` [`00bbfc6c`](#insn-00bbfc6c) → [`00bbfd38`](#insn-00bbfd38)
  - `FALL_THROUGH` [`00bbfc6c`](#insn-00bbfc6c) → [`00bbfc70`](#insn-00bbfc70)
- ブロック [`00bbfc70`](#insn-00bbfc70) 範囲 `[['00bbfc70', '00bbfc77']]`
  - `UNCONDITIONAL_JUMP` [`00bbfc74`](#insn-00bbfc74) → [`00bbfd3c`](#insn-00bbfd3c)
- ブロック [`00bbfc78`](#insn-00bbfc78) 範囲 `[['00bbfc78', '00bbfc93']]`
- ブロック [`00bbfc94`](#insn-00bbfc94) 範囲 `[['00bbfc94', '00bbfc9b']]`
  - `UNCONDITIONAL_JUMP` [`00bbfc98`](#insn-00bbfc98) → [`00bbfd20`](#insn-00bbfd20)
- ブロック [`00bbfc9c`](#insn-00bbfc9c) 範囲 `[['00bbfc9c', '00bbfcb3']]`
  - `FALL_THROUGH` [`00bbfcb0`](#insn-00bbfcb0) → [`00bbfcb4`](#insn-00bbfcb4)
- ブロック [`00bbfcb4`](#insn-00bbfcb4) 範囲 `[['00bbfcb4', '00bbfcbf']]`
  - `FALL_THROUGH` [`00bbfcbc`](#insn-00bbfcbc) → [`00bbfcc0`](#insn-00bbfcc0)
- ブロック [`00bbfcc0`](#insn-00bbfcc0) 範囲 `[['00bbfcc0', '00bbfccb']]`
  - `CONDITIONAL_JUMP` [`00bbfcc8`](#insn-00bbfcc8) → [`00bbfce8`](#insn-00bbfce8)
  - `FALL_THROUGH` [`00bbfcc8`](#insn-00bbfcc8) → [`00bbfccc`](#insn-00bbfccc)
- ブロック [`00bbfccc`](#insn-00bbfccc) 範囲 `[['00bbfccc', '00bbfcd7']]`
  - `CONDITIONAL_JUMP` [`00bbfcd4`](#insn-00bbfcd4) → [`00bbfdf4`](#insn-00bbfdf4)
  - `FALL_THROUGH` [`00bbfcd4`](#insn-00bbfcd4) → [`00bbfcd8`](#insn-00bbfcd8)
- ブロック [`00bbfcd8`](#insn-00bbfcd8) 範囲 `[['00bbfcd8', '00bbfce7']]`
  - `FALL_THROUGH` [`00bbfce4`](#insn-00bbfce4) → [`00bbfce8`](#insn-00bbfce8)
- ブロック [`00bbfce8`](#insn-00bbfce8) 範囲 `[['00bbfce8', '00bbfcef']]`
  - `FALL_THROUGH` [`00bbfcec`](#insn-00bbfcec) → [`00bbfcf0`](#insn-00bbfcf0)
- ブロック [`00bbfcf0`](#insn-00bbfcf0) 範囲 `[['00bbfcf0', '00bbfcff']]`
  - `FALL_THROUGH` [`00bbfcfc`](#insn-00bbfcfc) → [`00bbfd00`](#insn-00bbfd00)
- ブロック [`00bbfd00`](#insn-00bbfd00) 範囲 `[['00bbfd00', '00bbfd1f']]`
  - `FALL_THROUGH` [`00bbfd1c`](#insn-00bbfd1c) → [`00bbfd20`](#insn-00bbfd20)
- ブロック [`00bbfd20`](#insn-00bbfd20) 範囲 `[['00bbfd20', '00bbfd37']]`
- ブロック [`00bbfd38`](#insn-00bbfd38) 範囲 `[['00bbfd38', '00bbfd3b']]`
  - `FALL_THROUGH` [`00bbfd38`](#insn-00bbfd38) → [`00bbfd3c`](#insn-00bbfd3c)
- ブロック [`00bbfd3c`](#insn-00bbfd3c) 範囲 `[['00bbfd3c', '00bbfd53']]`
  - `CONDITIONAL_JUMP` [`00bbfd50`](#insn-00bbfd50) → [`00bbfdd0`](#insn-00bbfdd0)
  - `FALL_THROUGH` [`00bbfd50`](#insn-00bbfd50) → [`00bbfd54`](#insn-00bbfd54)
- ブロック [`00bbfd54`](#insn-00bbfd54) 範囲 `[['00bbfd54', '00bbfd5f']]`
  - `CONDITIONAL_JUMP` [`00bbfd5c`](#insn-00bbfd5c) → [`00bbfdd0`](#insn-00bbfdd0)
  - `FALL_THROUGH` [`00bbfd5c`](#insn-00bbfd5c) → [`00bbfd60`](#insn-00bbfd60)
- ブロック [`00bbfd60`](#insn-00bbfd60) 範囲 `[['00bbfd60', '00bbfd6f']]`
  - `CONDITIONAL_JUMP` [`00bbfd6c`](#insn-00bbfd6c) → [`00bbfd20`](#insn-00bbfd20)
  - `FALL_THROUGH` [`00bbfd6c`](#insn-00bbfd6c) → [`00bbfd70`](#insn-00bbfd70)
- ブロック [`00bbfd70`](#insn-00bbfd70) 範囲 `[['00bbfd70', '00bbfd7b']]`
  - `FALL_THROUGH` [`00bbfd78`](#insn-00bbfd78) → [`00bbfd7c`](#insn-00bbfd7c)
- ブロック [`00bbfd7c`](#insn-00bbfd7c) 範囲 `[['00bbfd7c', '00bbfd7f']]`
  - `CONDITIONAL_JUMP` [`00bbfd7c`](#insn-00bbfd7c) → [`00bbfd20`](#insn-00bbfd20)
  - `FALL_THROUGH` [`00bbfd7c`](#insn-00bbfd7c) → [`00bbfd80`](#insn-00bbfd80)
- ブロック [`00bbfd80`](#insn-00bbfd80) 範囲 `[['00bbfd80', '00bbfd97']]`
  - `CONDITIONAL_JUMP` [`00bbfd94`](#insn-00bbfd94) → [`00bbfdb4`](#insn-00bbfdb4)
  - `FALL_THROUGH` [`00bbfd94`](#insn-00bbfd94) → [`00bbfd98`](#insn-00bbfd98)
- ブロック [`00bbfd98`](#insn-00bbfd98) 範囲 `[['00bbfd98', '00bbfda3']]`
  - `CONDITIONAL_JUMP` [`00bbfda0`](#insn-00bbfda0) → [`00bbfdf4`](#insn-00bbfdf4)
  - `FALL_THROUGH` [`00bbfda0`](#insn-00bbfda0) → [`00bbfda4`](#insn-00bbfda4)
- ブロック [`00bbfda4`](#insn-00bbfda4) 範囲 `[['00bbfda4', '00bbfdab']]`
  - `FALL_THROUGH` [`00bbfda8`](#insn-00bbfda8) → [`00bbfdac`](#insn-00bbfdac)
- ブロック [`00bbfdac`](#insn-00bbfdac) 範囲 `[['00bbfdac', '00bbfdb3']]`
  - `FALL_THROUGH` [`00bbfdb0`](#insn-00bbfdb0) → [`00bbfdb4`](#insn-00bbfdb4)
- ブロック [`00bbfdb4`](#insn-00bbfdb4) 範囲 `[['00bbfdb4', '00bbfdcf']]`
  - `UNCONDITIONAL_JUMP` [`00bbfdcc`](#insn-00bbfdcc) → [`00bbfd00`](#insn-00bbfd00)
- ブロック [`00bbfdd0`](#insn-00bbfdd0) 範囲 `[['00bbfdd0', '00bbfdeb']]`
- ブロック [`00bbfdec`](#insn-00bbfdec) 範囲 `[['00bbfdec', '00bbfdef']]`
- ブロック [`00bbfdf0`](#insn-00bbfdf0) 範囲 `[['00bbfdf0', '00bbfdf3']]`
- ブロック [`00bbfdf4`](#insn-00bbfdf4) 範囲 `[['00bbfdf4', '00bbfdf7']]`

## 命令位置別の参照

- [`00bbfad4`](#insn-00bbfad4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfad8`](#insn-00bbfad8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfadc`](#insn-00bbfadc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfae0`](#insn-00bbfae0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfaf4`](#insn-00bbfaf4) → [`00bbfb00`](#insn-00bbfb00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfafc`](#insn-00bbfafc) → [`00bbfb04`](#insn-00bbfb04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb10`](#insn-00bbfb10) → [`00bbfb4c`](#insn-00bbfb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb14`](#insn-00bbfb14) → [`00bbfb94`](#insn-00bbfb94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb1c`](#insn-00bbfb1c) → [`00bbfdd0`](#insn-00bbfdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb24`](#insn-00bbfb24) → [`00bbfc78`](#insn-00bbfc78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb30`](#insn-00bbfb30) → [`00bbfc78`](#insn-00bbfc78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb40`](#insn-00bbfb40) → [`00bbd308`](../00bbd/00bbd308.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbd308` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb44`](#insn-00bbfb44) → [`00bbfb70`](#insn-00bbfb70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb48`](#insn-00bbfb48) → [`00bbfd20`](#insn-00bbfd20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb50`](#insn-00bbfb50) → [`00bbfc54`](#insn-00bbfc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb58`](#insn-00bbfb58) → [`00bbfdd0`](#insn-00bbfdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb68`](#insn-00bbfb68) → [`00bc2f0c`](../00bc2/00bc2f0c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc2f0c` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb6c`](#insn-00bbfb6c) → [`00bbfd20`](#insn-00bbfd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb78`](#insn-00bbfb78) → [`00bbfc94`](#insn-00bbfc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb84`](#insn-00bbfb84) → [`00bbfc94`](#insn-00bbfc94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfb90`](#insn-00bbfb90) → [`00bbfd20`](#insn-00bbfd20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbac`](#insn-00bbfbac) → [`00bbfbe0`](#insn-00bbfbe0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbb0`](#insn-00bbfbb0) → [`00bdd250`](../00bdd/00bdd250.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd250` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbb8`](#insn-00bbfbb8) → [`00bbfdec`](#insn-00bbfdec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbe4`](#insn-00bbfbe4) → [`00bbfbf4`](#insn-00bbfbf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbf0`](#insn-00bbfbf0) → [`00bbfc9c`](#insn-00bbfc9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbf8`](#insn-00bbfbf8) → [`00bbfad0`](#insn-00bbfad0) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbfad0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfbfc`](#insn-00bbfbfc) → [`00bbfd20`](#insn-00bbfd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc08`](#insn-00bbfc08) → [`00bbfbd0`](#insn-00bbfbd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc20`](#insn-00bbfc20) → [`00bbfbb0`](#insn-00bbfbb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc28`](#insn-00bbfc28) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc2c`](#insn-00bbfc2c) → [`00bbfdf0`](#insn-00bbfdf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc34`](#insn-00bbfc34) → [`00bbfc4c`](#insn-00bbfc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc44`](#insn-00bbfc44) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc50`](#insn-00bbfc50) → [`00bbfbbc`](#insn-00bbfbbc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc58`](#insn-00bbfc58) → [`00bbfdd0`](#insn-00bbfdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc64`](#insn-00bbfc64) → [`00bbfdd0`](#insn-00bbfdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc6c`](#insn-00bbfc6c) → [`00bbfd38`](#insn-00bbfd38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc74`](#insn-00bbfc74) → [`00bbfd3c`](#insn-00bbfd3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc7c`](#insn-00bbfc7c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc80`](#insn-00bbfc80) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc84`](#insn-00bbfc84) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc88`](#insn-00bbfc88) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc90`](#insn-00bbfc90) → [`00bc48e0`](../00bc4/00bc48e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bc48e0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfc98`](#insn-00bbfc98) → [`00bbfd20`](#insn-00bbfd20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcac`](#insn-00bbfcac) → [`00bbff70`](00bbff70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbff70` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcc8`](#insn-00bbfcc8) → [`00bbfce8`](#insn-00bbfce8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcd0`](#insn-00bbfcd0) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfcd4`](#insn-00bbfcd4) → [`00bbfdf4`](#insn-00bbfdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd00`](#insn-00bbfd00) → `00c19808`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbfd00`](#insn-00bbfd00) → `00c19878`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bbfd20`](#insn-00bbfd20) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd24`](#insn-00bbfd24) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd28`](#insn-00bbfd28) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd2c`](#insn-00bbfd2c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd48`](#insn-00bbfd48) → `00295779`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbfd4c`](#insn-00bbfd4c) → [`00bdb180`](../00bdb/00bdb180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb180` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd50`](#insn-00bbfd50) → [`00bbfdd0`](#insn-00bbfdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd5c`](#insn-00bbfd5c) → [`00bbfdd0`](#insn-00bbfdd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd68`](#insn-00bbfd68) → [`00bca9c4`](../00bca/00bca9c4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bca9c4` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd6c`](#insn-00bbfd6c) → [`00bbfd20`](#insn-00bbfd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd78`](#insn-00bbfd78) → [`00bbfad0`](#insn-00bbfad0) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbfad0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd7c`](#insn-00bbfd7c) → [`00bbfd20`](#insn-00bbfd20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd94`](#insn-00bbfd94) → [`00bbfdb4`](#insn-00bbfdb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfd9c`](#insn-00bbfd9c) → [`00bdd1d0`](../00bdd/00bdd1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdd1d0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfda0`](#insn-00bbfda0) → [`00bbfdf4`](#insn-00bbfdf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdcc`](#insn-00bbfdcc) → [`00bbfd00`](#insn-00bbfd00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdd4`](#insn-00bbfdd4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdd8`](#insn-00bbfdd8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfddc`](#insn-00bbfddc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfde0`](#insn-00bbfde0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbfde8`](#insn-00bbfde8) → [`00bbde5c`](../00bbd/00bbde5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bbde5c` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdec`](#insn-00bbfdec) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdf0`](#insn-00bbfdf0) → [`00bde2c0`](../00bde/00bde2c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde2c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbfdf4`](#insn-00bbfdf4) → [`00bdb1d0`](../00bdb/00bdb1d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1d0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbfad4`](#insn-00bbfad4)

~~~json
{
  "source": "00bbfad4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfad8`](#insn-00bbfad8)

~~~json
{
  "source": "00bbfad8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfadc`](#insn-00bbfadc)

~~~json
{
  "source": "00bbfadc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfae0`](#insn-00bbfae0)

~~~json
{
  "source": "00bbfae0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfaf4`](#insn-00bbfaf4)

~~~json
{
  "source": "00bbfaf4",
  "target": "00bbfb00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfafc`](#insn-00bbfafc)

~~~json
{
  "source": "00bbfafc",
  "target": "00bbfb04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb10`](#insn-00bbfb10)

~~~json
{
  "source": "00bbfb10",
  "target": "00bbfb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb14`](#insn-00bbfb14)

~~~json
{
  "source": "00bbfb14",
  "target": "00bbfb94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb1c`](#insn-00bbfb1c)

~~~json
{
  "source": "00bbfb1c",
  "target": "00bbfdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb24`](#insn-00bbfb24)

~~~json
{
  "source": "00bbfb24",
  "target": "00bbfc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb30`](#insn-00bbfb30)

~~~json
{
  "source": "00bbfb30",
  "target": "00bbfc78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb40`](#insn-00bbfb40)

~~~json
{
  "source": "00bbfb40",
  "target": "00bbd308",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfb44`](#insn-00bbfb44)

~~~json
{
  "source": "00bbfb44",
  "target": "00bbfb70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb48`](#insn-00bbfb48)

~~~json
{
  "source": "00bbfb48",
  "target": "00bbfd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb50`](#insn-00bbfb50)

~~~json
{
  "source": "00bbfb50",
  "target": "00bbfc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb58`](#insn-00bbfb58)

~~~json
{
  "source": "00bbfb58",
  "target": "00bbfdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb68`](#insn-00bbfb68)

~~~json
{
  "source": "00bbfb68",
  "target": "00bc2f0c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfb6c`](#insn-00bbfb6c)

~~~json
{
  "source": "00bbfb6c",
  "target": "00bbfd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb78`](#insn-00bbfb78)

~~~json
{
  "source": "00bbfb78",
  "target": "00bbfc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb84`](#insn-00bbfb84)

~~~json
{
  "source": "00bbfb84",
  "target": "00bbfc94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfb90`](#insn-00bbfb90)

~~~json
{
  "source": "00bbfb90",
  "target": "00bbfd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbac`](#insn-00bbfbac)

~~~json
{
  "source": "00bbfbac",
  "target": "00bbfbe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbb0`](#insn-00bbfbb0)

~~~json
{
  "source": "00bbfbb0",
  "target": "00bdd250",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfbb8`](#insn-00bbfbb8)

~~~json
{
  "source": "00bbfbb8",
  "target": "00bbfdec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbe4`](#insn-00bbfbe4)

~~~json
{
  "source": "00bbfbe4",
  "target": "00bbfbf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbf0`](#insn-00bbfbf0)

~~~json
{
  "source": "00bbfbf0",
  "target": "00bbfc9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfbf8`](#insn-00bbfbf8)

~~~json
{
  "source": "00bbfbf8",
  "target": "00bbfad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfbfc`](#insn-00bbfbfc)

~~~json
{
  "source": "00bbfbfc",
  "target": "00bbfd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc08`](#insn-00bbfc08)

~~~json
{
  "source": "00bbfc08",
  "target": "00bbfbd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc20`](#insn-00bbfc20)

~~~json
{
  "source": "00bbfc20",
  "target": "00bbfbb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc28`](#insn-00bbfc28)

~~~json
{
  "source": "00bbfc28",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfc2c`](#insn-00bbfc2c)

~~~json
{
  "source": "00bbfc2c",
  "target": "00bbfdf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc34`](#insn-00bbfc34)

~~~json
{
  "source": "00bbfc34",
  "target": "00bbfc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc44`](#insn-00bbfc44)

~~~json
{
  "source": "00bbfc44",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfc50`](#insn-00bbfc50)

~~~json
{
  "source": "00bbfc50",
  "target": "00bbfbbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc58`](#insn-00bbfc58)

~~~json
{
  "source": "00bbfc58",
  "target": "00bbfdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc64`](#insn-00bbfc64)

~~~json
{
  "source": "00bbfc64",
  "target": "00bbfdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc6c`](#insn-00bbfc6c)

~~~json
{
  "source": "00bbfc6c",
  "target": "00bbfd38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc74`](#insn-00bbfc74)

~~~json
{
  "source": "00bbfc74",
  "target": "00bbfd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc7c`](#insn-00bbfc7c)

~~~json
{
  "source": "00bbfc7c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc80`](#insn-00bbfc80)

~~~json
{
  "source": "00bbfc80",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc84`](#insn-00bbfc84)

~~~json
{
  "source": "00bbfc84",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc88`](#insn-00bbfc88)

~~~json
{
  "source": "00bbfc88",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfc90`](#insn-00bbfc90)

~~~json
{
  "source": "00bbfc90",
  "target": "00bc48e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfc98`](#insn-00bbfc98)

~~~json
{
  "source": "00bbfc98",
  "target": "00bbfd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcac`](#insn-00bbfcac)

~~~json
{
  "source": "00bbfcac",
  "target": "00bbff70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfcc8`](#insn-00bbfcc8)

~~~json
{
  "source": "00bbfcc8",
  "target": "00bbfce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfcd0`](#insn-00bbfcd0)

~~~json
{
  "source": "00bbfcd0",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfcd4`](#insn-00bbfcd4)

~~~json
{
  "source": "00bbfcd4",
  "target": "00bbfdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd00`](#insn-00bbfd00)

~~~json
{
  "source": "00bbfd00",
  "target": "00c19808",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19808",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbfd00`](#insn-00bbfd00)

~~~json
{
  "source": "00bbfd00",
  "target": "00c19878",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c19878",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bbfd20`](#insn-00bbfd20)

~~~json
{
  "source": "00bbfd20",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd24`](#insn-00bbfd24)

~~~json
{
  "source": "00bbfd24",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd28`](#insn-00bbfd28)

~~~json
{
  "source": "00bbfd28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd2c`](#insn-00bbfd2c)

~~~json
{
  "source": "00bbfd2c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd48`](#insn-00bbfd48)

~~~json
{
  "source": "00bbfd48",
  "target": "00295779",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00295779",
  "offset": 0,
  "size": 6,
  "datatype": "string",
  "bytes": "7970746e6b00",
  "capture_start": "00295779",
  "capture_bytes": 6,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbfd4c`](#insn-00bbfd4c)

~~~json
{
  "source": "00bbfd4c",
  "target": "00bdb180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfd50`](#insn-00bbfd50)

~~~json
{
  "source": "00bbfd50",
  "target": "00bbfdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd5c`](#insn-00bbfd5c)

~~~json
{
  "source": "00bbfd5c",
  "target": "00bbfdd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd68`](#insn-00bbfd68)

~~~json
{
  "source": "00bbfd68",
  "target": "00bca9c4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfd6c`](#insn-00bbfd6c)

~~~json
{
  "source": "00bbfd6c",
  "target": "00bbfd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd78`](#insn-00bbfd78)

~~~json
{
  "source": "00bbfd78",
  "target": "00bbfad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfd7c`](#insn-00bbfd7c)

~~~json
{
  "source": "00bbfd7c",
  "target": "00bbfd20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd94`](#insn-00bbfd94)

~~~json
{
  "source": "00bbfd94",
  "target": "00bbfdb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfd9c`](#insn-00bbfd9c)

~~~json
{
  "source": "00bbfd9c",
  "target": "00bdd1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfda0`](#insn-00bbfda0)

~~~json
{
  "source": "00bbfda0",
  "target": "00bbfdf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdcc`](#insn-00bbfdcc)

~~~json
{
  "source": "00bbfdcc",
  "target": "00bbfd00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdd4`](#insn-00bbfdd4)

~~~json
{
  "source": "00bbfdd4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfdd8`](#insn-00bbfdd8)

~~~json
{
  "source": "00bbfdd8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfddc`](#insn-00bbfddc)

~~~json
{
  "source": "00bbfddc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfde0`](#insn-00bbfde0)

~~~json
{
  "source": "00bbfde0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbfde8`](#insn-00bbfde8)

~~~json
{
  "source": "00bbfde8",
  "target": "00bbde5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfdec`](#insn-00bbfdec)

~~~json
{
  "source": "00bbfdec",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfdf0`](#insn-00bbfdf0)

~~~json
{
  "source": "00bbfdf0",
  "target": "00bde2c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbfdf4`](#insn-00bbfdf4)

~~~json
{
  "source": "00bbfdf4",
  "target": "00bdb1d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
