# 00bbb5ac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bbb568`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bbb/00bbb568.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0018.md#compare-f33e6e4cf45ed7f03a3259351865ddfc)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c37ff4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c37/00c37ff4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0020.md#compare-3c56a90a6b2183f0f2671ac6855bebc3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbb5ac",
  "name": "__dynamic_cast",
  "size": 524,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6b220ebd7a75eac874a02dfa03d7456f1d01990d1b061199c0e2bbfb3edfadcf",
  "source_text_sha256": "6b220ebd7a75eac874a02dfa03d7456f1d01990d1b061199c0e2bbfb3edfadcf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbb5ac",
        "00bbb7b7"
      ]
    ],
    "bytes_sha256": "038a7c157faef69ef47aa9139aa31a6084b4b2083c202b2f5019b843cd454407",
    "instruction_count": 131,
    "instruction_bytes": 524,
    "body_bytes": 524,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00bdb7c0](../00bdb/00bdb7c0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3228 bytes

~~~c

long __dynamic_cast(long *param_1,undefined8 param_2,long *param_3,long param_4)

{
  long *plVar1;
  bool bVar2;
  long lVar3;
  long lVar4;
  long *local_98;
  long *plStack_90;
  long *local_88;
  long lStack_80;
  long local_78;
  long lStack_70;
  undefined8 local_68;
  int iStack_60;
  int iStack_5c;
  int local_58;
  undefined4 uStack_54;
  undefined4 local_50;
  undefined4 local_4c;
  undefined8 local_48;
  
                    /* try { // try from 00bbb5c8 to 00cbb5cf has its CatchHandler @ 00bbb8e8 */
  lVar3 = *(long *)(*param_1 + -0x10);
  plVar1 = *(long **)(*param_1 + -8);
  lVar4 = (long)param_1 + lVar3;
  lStack_80 = param_4;
  if (plVar1[1] == param_3[1]) {
    if (param_4 < 0) {
      if (param_4 == -2) {
        return 0;
      }
      local_50 = 1;
      local_58 = 0;
      uStack_54 = 0;
      local_48 = 0;
      lStack_70 = 0;
      local_78 = 0;
      iStack_60 = 0;
      iStack_5c = 0;
      local_68 = 0;
      local_4c = 0x1000000;
      local_98 = param_3;
      plStack_90 = param_1;
      local_88 = (long *)param_2;
      (**(code **)(*param_3 + 0x28))(param_3,&local_98,lVar4,lVar4,1,0);
      bVar2 = (int)local_68 == 1;
    }
    else {
      bVar2 = param_4 + lVar3 == 0;
    }
    if (!bVar2) {
      lVar4 = 0;
    }
  }
  else {
    if ((-1 < param_4) && (lVar3 = (long)param_1 - param_4, lVar4 <= lVar3)) {
                    /* try { // try from 00bbb604 to 00cbb60f has its CatchHandler @ 00bbb7ec */
                    /* try { // try from 00bbb610 to 00cbb61f has its CatchHandler @ 00bbb7d8 */
      local_58 = 0;
      uStack_54 = 0;
      iStack_60 = 0;
      iStack_5c = 0;
                    /* try { // try from 00bbb620 to 00cbb633 has its CatchHandler @ 00bbb7c0 */
      local_68 = 0;
      lStack_70 = 0;
      local_78 = 0;
      local_50 = 1;
      local_4c = 0x1000000;
      local_48 = 0;
      local_98 = plVar1;
      plStack_90 = (long *)lVar3;
      local_88 = param_3;
      (**(code **)(*plVar1 + 0x28))(plVar1,&local_98,lVar4,lVar4,1,0);
      if ((int)local_68 != 0) {
        return lVar3;
      }
    }
    local_48 = 0;
    local_50 = 0;
    local_4c = 0x1000000;
    local_58 = 0;
    uStack_54 = 0;
    lStack_70 = 0;
    local_78 = 0;
    iStack_60 = 0;
    iStack_5c = 0;
    local_68 = 0;
    local_98 = param_3;
    plStack_90 = param_1;
    local_88 = (long *)param_2;
    lStack_80 = param_4;
    (**(code **)(*plVar1 + 0x30))(plVar1,&local_98,lVar4,1,0);
    if (iStack_5c == 1) {
                    /* try { // try from 00bbb6f8 to 00cbb703 has its CatchHandler @ 00bbb8e8 */
                    /* try { // try from 00bbb704 to 00cbb92f has its CatchHandler @ 00bbaf68 */
      if (((int)local_68 == 1) ||
         (((lVar4 = 0, local_58 == 0 && (local_68._4_4_ == 1)) && (iStack_60 == 1)))) {
        lVar4 = local_78;
      }
    }
    else {
      lVar4 = 0;
                    /* try { // try from 00bbb6c8 to 00cbb6d3 has its CatchHandler @ 00bbb8ec */
                    /* try { // try from 00bbb6d4 to 00cbb6e3 has its CatchHandler @ 00bbb8f0 */
      if ((iStack_5c == 0) &&
         (lVar4 = lStack_70, (iStack_60 != 1 || local_68._4_4_ != 1) || local_58 != 1)) {
        lVar4 = 0;
      }
    }
  }
  return lVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bbb5ac"></a> `00bbb5ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bbb5b0"></a> `00bbb5b0` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbb5b4"></a> `00bbb5b4` | `fe 67 06 a9` | stp x30,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbb5b8"></a> `00bbb5b8` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbb5bc"></a> `00bbb5bc` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbb5c0"></a> `00bbb5c0` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbb5c4"></a> `00bbb5c4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bbb5c8"></a> `00bbb5c8` | `49 04 40 f9` | ldr x9,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb5cc"></a> `00bbb5cc` | `08 51 7f a9` | ldp x8,x20,[x8, #-0x10] | `FALL_THROUGH`
<a id="insn-00bbb5d0"></a> `00bbb5d0` | `8a 06 40 f9` | ldr x10,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb5d4"></a> `00bbb5d4` | `13 00 08 8b` | add x19,x0,x8 | `FALL_THROUGH`
<a id="insn-00bbb5d8"></a> `00bbb5d8` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bbb5dc"></a> `00bbb5dc` | `60 08 00 54` | b.eq 0x00bbb6e8 | `CONDITIONAL_JUMP`
<a id="insn-00bbb5e0"></a> `00bbb5e0` | `83 04 f8 b7` | tbnz x3,#0x3f,0x00bbb670 | `CONDITIONAL_JUMP`
<a id="insn-00bbb5e4"></a> `00bbb5e4` | `08 00 03 cb` | sub x8,x0,x3 | `FALL_THROUGH`
<a id="insn-00bbb5e8"></a> `00bbb5e8` | `1f 01 13 eb` | cmp x8,x19 | `FALL_THROUGH`
<a id="insn-00bbb5ec"></a> `00bbb5ec` | `2b 04 00 54` | b.lt 0x00bbb670 | `CONDITIONAL_JUMP`
<a id="insn-00bbb5f0"></a> `00bbb5f0` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bbb5f4"></a> `00bbb5f4` | `21 64 00 0f` | movi v1.2S,#0x1, LSL #24 | `FALL_THROUGH`
<a id="insn-00bbb5f8"></a> `00bbb5f8` | `29 00 80 52` | mov w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb5fc"></a> `00bbb5fc` | `f4 a3 00 a9` | stp x20,x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb600"></a> `00bbb600` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bbb604"></a> `00bbb604` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbb608"></a> `00bbb608` | `e2 8f 01 a9` | stp x2,x3,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbb60c"></a> `00bbb60c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbb610"></a> `00bbb610` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbb614"></a> `00bbb614` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbb618"></a> `00bbb618` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bbb61c"></a> `00bbb61c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bbb620"></a> `00bbb620` | `e0 83 83 3c` | stur q0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbb624"></a> `00bbb624` | `f9 03 03 aa` | mov x25,x3 | `FALL_THROUGH`
<a id="insn-00bbb628"></a> `00bbb628` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bbb62c"></a> `00bbb62c` | `e0 83 82 3c` | stur q0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb630"></a> `00bbb630` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb634"></a> `00bbb634` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00bbb638"></a> `00bbb638` | `e9 53 00 b9` | str w9,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbb63c"></a> `00bbb63c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00bbb640"></a> `00bbb640` | `e1 57 00 bd` | str s1,[sp, #0x54] | `FALL_THROUGH`
<a id="insn-00bbb644"></a> `00bbb644` | `ff 2f 00 f9` | str xzr,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bbb648"></a> `00bbb648` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bbb64c"></a> `00bbb64c` | `29 15 40 f9` | ldr x9,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb650"></a> `00bbb650` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00bbb654"></a> `00bbb654` | `e9 3b 40 b9` | ldr w9,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbb658"></a> `00bbb658` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbb65c"></a> `00bbb65c` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bbb660"></a> `00bbb660` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bbb664"></a> `00bbb664` | `e3 03 19 aa` | mov x3,x25 | `FALL_THROUGH`
<a id="insn-00bbb668"></a> `00bbb668` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bbb66c"></a> `00bbb66c` | `69 09 00 35` | cbnz w9,0x00bbb798 | `CONDITIONAL_JUMP`
<a id="insn-00bbb670"></a> `00bbb670` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bbb674"></a> `00bbb674` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb678"></a> `00bbb678` | `e2 83 00 a9` | stp x2,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb67c"></a> `00bbb67c` | `e1 8f 01 a9` | stp x1,x3,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbb680"></a> `00bbb680` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbb684"></a> `00bbb684` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bbb688"></a> `00bbb688` | `e8 5f 01 39` | strb w8,[sp, #0x57] | `FALL_THROUGH`
<a id="insn-00bbb68c"></a> `00bbb68c` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bbb690"></a> `00bbb690` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb694"></a> `00bbb694` | `ff 2f 00 f9` | str xzr,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bbb698"></a> `00bbb698` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bbb69c"></a> `00bbb69c` | `e0 73 84 3c` | stur q0,[sp, #0x47] | `FALL_THROUGH`
<a id="insn-00bbb6a0"></a> `00bbb6a0` | `e0 83 82 3c` | stur q0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb6a4"></a> `00bbb6a4` | `e0 83 83 3c` | stur q0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbb6a8"></a> `00bbb6a8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bbb6ac"></a> `00bbb6ac` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb6b0"></a> `00bbb6b0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbb6b4"></a> `00bbb6b4` | `e9 47 40 b9` | ldr w9,[sp, #0x44] | `FALL_THROUGH`
<a id="insn-00bbb6b8"></a> `00bbb6b8` | `3f 05 00 71` | cmp w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb6bc"></a> `00bbb6bc` | `c0 01 00 54` | b.eq 0x00bbb6f4 | `CONDITIONAL_JUMP`
<a id="insn-00bbb6c0"></a> `00bbb6c0` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbb6c4"></a> `00bbb6c4` | `a9 06 00 35` | cbnz w9,0x00bbb798 | `CONDITIONAL_JUMP`
<a id="insn-00bbb6c8"></a> `00bbb6c8` | `e9 a3 47 29` | ldp w9,w8,[sp, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbb6cc"></a> `00bbb6cc` | `ea 4b 40 b9` | ldr w10,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbb6d0"></a> `00bbb6d0` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb6d4"></a> `00bbb6d4` | `e8 1b 40 f9` | ldr x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbb6d8"></a> `00bbb6d8` | `20 09 41 7a` | ccmp w9,#0x1,#0x0,eq | `FALL_THROUGH`
<a id="insn-00bbb6dc"></a> `00bbb6dc` | `40 09 41 7a` | ccmp w10,#0x1,#0x0,eq | `FALL_THROUGH`
<a id="insn-00bbb6e0"></a> `00bbb6e0` | `08 01 9f 9a` | csel x8,x8,xzr,eq | `FALL_THROUGH`
<a id="insn-00bbb6e4"></a> `00bbb6e4` | `2d 00 00 14` | b 0x00bbb798 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb6e8"></a> `00bbb6e8` | `23 02 f8 b7` | tbnz x3,#0x3f,0x00bbb72c | `CONDITIONAL_JUMP`
<a id="insn-00bbb6ec"></a> `00bbb6ec` | `7f 00 08 ab` | cmn x3,x8 | `FALL_THROUGH`
<a id="insn-00bbb6f0"></a> `00bbb6f0` | `29 00 00 14` | b 0x00bbb794 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb6f4"></a> `00bbb6f4` | `e8 3b 40 b9` | ldr w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbb6f8"></a> `00bbb6f8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb6fc"></a> `00bbb6fc` | `40 01 00 54` | b.eq 0x00bbb724 | `CONDITIONAL_JUMP`
<a id="insn-00bbb700"></a> `00bbb700` | `e9 4b 40 b9` | ldr w9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbb704"></a> `00bbb704` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbb708"></a> `00bbb708` | `89 04 00 35` | cbnz w9,0x00bbb798 | `CONDITIONAL_JUMP`
<a id="insn-00bbb70c"></a> `00bbb70c` | `e9 3f 40 b9` | ldr w9,[sp, #0x3c] | `FALL_THROUGH`
<a id="insn-00bbb710"></a> `00bbb710` | `3f 05 00 71` | cmp w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb714"></a> `00bbb714` | `21 04 00 54` | b.ne 0x00bbb798 | `CONDITIONAL_JUMP`
<a id="insn-00bbb718"></a> `00bbb718` | `e9 43 40 b9` | ldr w9,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbb71c"></a> `00bbb71c` | `3f 05 00 71` | cmp w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb720"></a> `00bbb720` | `c1 03 00 54` | b.ne 0x00bbb798 | `CONDITIONAL_JUMP`
<a id="insn-00bbb724"></a> `00bbb724` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb728"></a> `00bbb728` | `1c 00 00 14` | b 0x00bbb798 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb72c"></a> `00bbb72c` | `7f 08 00 b1` | cmn x3,#0x2 | `FALL_THROUGH`
<a id="insn-00bbb730"></a> `00bbb730` | `61 00 00 54` | b.ne 0x00bbb73c | `CONDITIONAL_JUMP`
<a id="insn-00bbb734"></a> `00bbb734` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bbb738"></a> `00bbb738` | `18 00 00 14` | b 0x00bbb798 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbb73c"></a> `00bbb73c` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00bbb740"></a> `00bbb740` | `21 64 00 0f` | movi v1.2S,#0x1, LSL #24 | `FALL_THROUGH`
<a id="insn-00bbb744"></a> `00bbb744` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb748"></a> `00bbb748` | `e8 53 00 b9` | str w8,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbb74c"></a> `00bbb74c` | `48 00 40 f9` | ldr x8,[x2] | `FALL_THROUGH`
<a id="insn-00bbb750"></a> `00bbb750` | `24 00 80 52` | mov w4,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb754"></a> `00bbb754` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbb758"></a> `00bbb758` | `e5 03 1f 2a` | mov w5,wzr | `FALL_THROUGH`
<a id="insn-00bbb75c"></a> `00bbb75c` | `ff 2f 00 f9` | str xzr,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00bbb760"></a> `00bbb760` | `e0 83 82 3c` | stur q0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb764"></a> `00bbb764` | `e0 83 83 3c` | stur q0,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbb768"></a> `00bbb768` | `e1 57 00 bd` | str s1,[sp, #0x54] | `FALL_THROUGH`
<a id="insn-00bbb76c"></a> `00bbb76c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bbb770"></a> `00bbb770` | `e2 83 00 a9` | stp x2,x0,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bbb774"></a> `00bbb774` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bbb778"></a> `00bbb778` | `e1 8f 01 a9` | stp x1,x3,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbb77c"></a> `00bbb77c` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bbb780"></a> `00bbb780` | `e2 03 13 aa` | mov x2,x19 | `FALL_THROUGH`
<a id="insn-00bbb784"></a> `00bbb784` | `e3 03 13 aa` | mov x3,x19 | `FALL_THROUGH`
<a id="insn-00bbb788"></a> `00bbb788` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bbb78c"></a> `00bbb78c` | `e8 3b 40 b9` | ldr w8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbb790"></a> `00bbb790` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bbb794"></a> `00bbb794` | `68 02 9f 9a` | csel x8,x19,xzr,eq | `FALL_THROUGH`
<a id="insn-00bbb798"></a> `00bbb798` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbb79c"></a> `00bbb79c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bbb7a0"></a> `00bbb7a0` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbb7a4"></a> `00bbb7a4` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbb7a8"></a> `00bbb7a8` | `fe 67 46 a9` | ldp x30,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbb7ac"></a> `00bbb7ac` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbb7b0"></a> `00bbb7b0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bbb7b4"></a> `00bbb7b4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbb5ac`](#insn-00bbb5ac) 範囲 `[['00bbb5ac', '00bbb5c7']]`
  - `FALL_THROUGH` [`00bbb5c4`](#insn-00bbb5c4) → [`00bbb5c8`](#insn-00bbb5c8)
- ブロック [`00bbb5c8`](#insn-00bbb5c8) 範囲 `[['00bbb5c8', '00bbb5df']]`
  - `CONDITIONAL_JUMP` [`00bbb5dc`](#insn-00bbb5dc) → [`00bbb6e8`](#insn-00bbb6e8)
  - `FALL_THROUGH` [`00bbb5dc`](#insn-00bbb5dc) → [`00bbb5e0`](#insn-00bbb5e0)
- ブロック [`00bbb5e0`](#insn-00bbb5e0) 範囲 `[['00bbb5e0', '00bbb5e3']]`
  - `CONDITIONAL_JUMP` [`00bbb5e0`](#insn-00bbb5e0) → [`00bbb670`](#insn-00bbb670)
  - `FALL_THROUGH` [`00bbb5e0`](#insn-00bbb5e0) → [`00bbb5e4`](#insn-00bbb5e4)
- ブロック [`00bbb5e4`](#insn-00bbb5e4) 範囲 `[['00bbb5e4', '00bbb5ef']]`
  - `CONDITIONAL_JUMP` [`00bbb5ec`](#insn-00bbb5ec) → [`00bbb670`](#insn-00bbb670)
  - `FALL_THROUGH` [`00bbb5ec`](#insn-00bbb5ec) → [`00bbb5f0`](#insn-00bbb5f0)
- ブロック [`00bbb5f0`](#insn-00bbb5f0) 範囲 `[['00bbb5f0', '00bbb603']]`
  - `FALL_THROUGH` [`00bbb600`](#insn-00bbb600) → [`00bbb604`](#insn-00bbb604)
- ブロック [`00bbb604`](#insn-00bbb604) 範囲 `[['00bbb604', '00bbb60f']]`
  - `FALL_THROUGH` [`00bbb60c`](#insn-00bbb60c) → [`00bbb610`](#insn-00bbb610)
- ブロック [`00bbb610`](#insn-00bbb610) 範囲 `[['00bbb610', '00bbb61f']]`
  - `FALL_THROUGH` [`00bbb61c`](#insn-00bbb61c) → [`00bbb620`](#insn-00bbb620)
- ブロック [`00bbb620`](#insn-00bbb620) 範囲 `[['00bbb620', '00bbb66f']]`
  - `CONDITIONAL_JUMP` [`00bbb66c`](#insn-00bbb66c) → [`00bbb798`](#insn-00bbb798)
  - `FALL_THROUGH` [`00bbb66c`](#insn-00bbb66c) → [`00bbb670`](#insn-00bbb670)
- ブロック [`00bbb670`](#insn-00bbb670) 範囲 `[['00bbb670', '00bbb6bf']]`
  - `CONDITIONAL_JUMP` [`00bbb6bc`](#insn-00bbb6bc) → [`00bbb6f4`](#insn-00bbb6f4)
  - `FALL_THROUGH` [`00bbb6bc`](#insn-00bbb6bc) → [`00bbb6c0`](#insn-00bbb6c0)
- ブロック [`00bbb6c0`](#insn-00bbb6c0) 範囲 `[['00bbb6c0', '00bbb6c7']]`
  - `CONDITIONAL_JUMP` [`00bbb6c4`](#insn-00bbb6c4) → [`00bbb798`](#insn-00bbb798)
  - `FALL_THROUGH` [`00bbb6c4`](#insn-00bbb6c4) → [`00bbb6c8`](#insn-00bbb6c8)
- ブロック [`00bbb6c8`](#insn-00bbb6c8) 範囲 `[['00bbb6c8', '00bbb6d3']]`
  - `FALL_THROUGH` [`00bbb6d0`](#insn-00bbb6d0) → [`00bbb6d4`](#insn-00bbb6d4)
- ブロック [`00bbb6d4`](#insn-00bbb6d4) 範囲 `[['00bbb6d4', '00bbb6e7']]`
  - `UNCONDITIONAL_JUMP` [`00bbb6e4`](#insn-00bbb6e4) → [`00bbb798`](#insn-00bbb798)
- ブロック [`00bbb6e8`](#insn-00bbb6e8) 範囲 `[['00bbb6e8', '00bbb6eb']]`
  - `CONDITIONAL_JUMP` [`00bbb6e8`](#insn-00bbb6e8) → [`00bbb72c`](#insn-00bbb72c)
  - `FALL_THROUGH` [`00bbb6e8`](#insn-00bbb6e8) → [`00bbb6ec`](#insn-00bbb6ec)
- ブロック [`00bbb6ec`](#insn-00bbb6ec) 範囲 `[['00bbb6ec', '00bbb6f3']]`
  - `UNCONDITIONAL_JUMP` [`00bbb6f0`](#insn-00bbb6f0) → [`00bbb794`](#insn-00bbb794)
- ブロック [`00bbb6f4`](#insn-00bbb6f4) 範囲 `[['00bbb6f4', '00bbb6f7']]`
  - `FALL_THROUGH` [`00bbb6f4`](#insn-00bbb6f4) → [`00bbb6f8`](#insn-00bbb6f8)
- ブロック [`00bbb6f8`](#insn-00bbb6f8) 範囲 `[['00bbb6f8', '00bbb6ff']]`
  - `CONDITIONAL_JUMP` [`00bbb6fc`](#insn-00bbb6fc) → [`00bbb724`](#insn-00bbb724)
  - `FALL_THROUGH` [`00bbb6fc`](#insn-00bbb6fc) → [`00bbb700`](#insn-00bbb700)
- ブロック [`00bbb700`](#insn-00bbb700) 範囲 `[['00bbb700', '00bbb703']]`
  - `FALL_THROUGH` [`00bbb700`](#insn-00bbb700) → [`00bbb704`](#insn-00bbb704)
- ブロック [`00bbb704`](#insn-00bbb704) 範囲 `[['00bbb704', '00bbb70b']]`
  - `CONDITIONAL_JUMP` [`00bbb708`](#insn-00bbb708) → [`00bbb798`](#insn-00bbb798)
  - `FALL_THROUGH` [`00bbb708`](#insn-00bbb708) → [`00bbb70c`](#insn-00bbb70c)
- ブロック [`00bbb70c`](#insn-00bbb70c) 範囲 `[['00bbb70c', '00bbb717']]`
  - `CONDITIONAL_JUMP` [`00bbb714`](#insn-00bbb714) → [`00bbb798`](#insn-00bbb798)
  - `FALL_THROUGH` [`00bbb714`](#insn-00bbb714) → [`00bbb718`](#insn-00bbb718)
- ブロック [`00bbb718`](#insn-00bbb718) 範囲 `[['00bbb718', '00bbb723']]`
  - `CONDITIONAL_JUMP` [`00bbb720`](#insn-00bbb720) → [`00bbb798`](#insn-00bbb798)
  - `FALL_THROUGH` [`00bbb720`](#insn-00bbb720) → [`00bbb724`](#insn-00bbb724)
- ブロック [`00bbb724`](#insn-00bbb724) 範囲 `[['00bbb724', '00bbb72b']]`
  - `UNCONDITIONAL_JUMP` [`00bbb728`](#insn-00bbb728) → [`00bbb798`](#insn-00bbb798)
- ブロック [`00bbb72c`](#insn-00bbb72c) 範囲 `[['00bbb72c', '00bbb733']]`
  - `CONDITIONAL_JUMP` [`00bbb730`](#insn-00bbb730) → [`00bbb73c`](#insn-00bbb73c)
  - `FALL_THROUGH` [`00bbb730`](#insn-00bbb730) → [`00bbb734`](#insn-00bbb734)
- ブロック [`00bbb734`](#insn-00bbb734) 範囲 `[['00bbb734', '00bbb73b']]`
  - `UNCONDITIONAL_JUMP` [`00bbb738`](#insn-00bbb738) → [`00bbb798`](#insn-00bbb798)
- ブロック [`00bbb73c`](#insn-00bbb73c) 範囲 `[['00bbb73c', '00bbb793']]`
  - `FALL_THROUGH` [`00bbb790`](#insn-00bbb790) → [`00bbb794`](#insn-00bbb794)
- ブロック [`00bbb794`](#insn-00bbb794) 範囲 `[['00bbb794', '00bbb797']]`
  - `FALL_THROUGH` [`00bbb794`](#insn-00bbb794) → [`00bbb798`](#insn-00bbb798)
- ブロック [`00bbb798`](#insn-00bbb798) 範囲 `[['00bbb798', '00bbb7b7']]`

## 命令位置別の参照

- [`00bbb5b4`](#insn-00bbb5b4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5b8`](#insn-00bbb5b8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5bc`](#insn-00bbb5bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5c0`](#insn-00bbb5c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5dc`](#insn-00bbb5dc) → [`00bbb6e8`](#insn-00bbb6e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5e0`](#insn-00bbb5e0) → [`00bbb670`](#insn-00bbb670) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5ec`](#insn-00bbb5ec) → [`00bbb670`](#insn-00bbb670) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb5fc`](#insn-00bbb5fc) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb608`](#insn-00bbb608) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb614`](#insn-00bbb614) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb620`](#insn-00bbb620) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb62c`](#insn-00bbb62c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb638`](#insn-00bbb638) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb640`](#insn-00bbb640) → `01000000`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb640`](#insn-00bbb640) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb644`](#insn-00bbb644) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb654`](#insn-00bbb654) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb66c`](#insn-00bbb66c) → [`00bbb798`](#insn-00bbb798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb678`](#insn-00bbb678) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb67c`](#insn-00bbb67c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb688`](#insn-00bbb688) → `Stack[-0x49]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb694`](#insn-00bbb694) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb69c`](#insn-00bbb69c) → `Stack[-0x59]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6a0`](#insn-00bbb6a0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6a4`](#insn-00bbb6a4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6b4`](#insn-00bbb6b4) → `Stack[-0x5c]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6bc`](#insn-00bbb6bc) → [`00bbb6f4`](#insn-00bbb6f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6c4`](#insn-00bbb6c4) → [`00bbb798`](#insn-00bbb798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6c8`](#insn-00bbb6c8) → `Stack[-0x64]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6cc`](#insn-00bbb6cc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6d4`](#insn-00bbb6d4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6e4`](#insn-00bbb6e4) → [`00bbb798`](#insn-00bbb798) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6e8`](#insn-00bbb6e8) → [`00bbb72c`](#insn-00bbb72c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6f0`](#insn-00bbb6f0) → [`00bbb794`](#insn-00bbb794) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6f4`](#insn-00bbb6f4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb6fc`](#insn-00bbb6fc) → [`00bbb724`](#insn-00bbb724) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb700`](#insn-00bbb700) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb708`](#insn-00bbb708) → [`00bbb798`](#insn-00bbb798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb70c`](#insn-00bbb70c) → `Stack[-0x64]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb714`](#insn-00bbb714) → [`00bbb798`](#insn-00bbb798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb718`](#insn-00bbb718) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb720`](#insn-00bbb720) → [`00bbb798`](#insn-00bbb798) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb724`](#insn-00bbb724) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb728`](#insn-00bbb728) → [`00bbb798`](#insn-00bbb798) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb730`](#insn-00bbb730) → [`00bbb73c`](#insn-00bbb73c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb738`](#insn-00bbb738) → [`00bbb798`](#insn-00bbb798) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb748`](#insn-00bbb748) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb754`](#insn-00bbb754) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb75c`](#insn-00bbb75c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb760`](#insn-00bbb760) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb764`](#insn-00bbb764) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb768`](#insn-00bbb768) → `01000000`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb768`](#insn-00bbb768) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb770`](#insn-00bbb770) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb778`](#insn-00bbb778) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb78c`](#insn-00bbb78c) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb798`](#insn-00bbb798) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb7a0`](#insn-00bbb7a0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb7a4`](#insn-00bbb7a4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbb7a8`](#insn-00bbb7a8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbb5b4`](#insn-00bbb5b4)

~~~json
{
  "source": "00bbb5b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5b8`](#insn-00bbb5b8)

~~~json
{
  "source": "00bbb5b8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5bc`](#insn-00bbb5bc)

~~~json
{
  "source": "00bbb5bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5c0`](#insn-00bbb5c0)

~~~json
{
  "source": "00bbb5c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5dc`](#insn-00bbb5dc)

~~~json
{
  "source": "00bbb5dc",
  "target": "00bbb6e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5e0`](#insn-00bbb5e0)

~~~json
{
  "source": "00bbb5e0",
  "target": "00bbb670",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5ec`](#insn-00bbb5ec)

~~~json
{
  "source": "00bbb5ec",
  "target": "00bbb670",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb5fc`](#insn-00bbb5fc)

~~~json
{
  "source": "00bbb5fc",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb608`](#insn-00bbb608)

~~~json
{
  "source": "00bbb608",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb614`](#insn-00bbb614)

~~~json
{
  "source": "00bbb614",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb620`](#insn-00bbb620)

~~~json
{
  "source": "00bbb620",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb62c`](#insn-00bbb62c)

~~~json
{
  "source": "00bbb62c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb638`](#insn-00bbb638)

~~~json
{
  "source": "00bbb638",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb640`](#insn-00bbb640)

~~~json
{
  "source": "00bbb640",
  "target": "01000000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb640`](#insn-00bbb640)

~~~json
{
  "source": "00bbb640",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb644`](#insn-00bbb644)

~~~json
{
  "source": "00bbb644",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb654`](#insn-00bbb654)

~~~json
{
  "source": "00bbb654",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb66c`](#insn-00bbb66c)

~~~json
{
  "source": "00bbb66c",
  "target": "00bbb798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb678`](#insn-00bbb678)

~~~json
{
  "source": "00bbb678",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb67c`](#insn-00bbb67c)

~~~json
{
  "source": "00bbb67c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb688`](#insn-00bbb688)

~~~json
{
  "source": "00bbb688",
  "target": "Stack[-0x49]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb694`](#insn-00bbb694)

~~~json
{
  "source": "00bbb694",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb69c`](#insn-00bbb69c)

~~~json
{
  "source": "00bbb69c",
  "target": "Stack[-0x59]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6a0`](#insn-00bbb6a0)

~~~json
{
  "source": "00bbb6a0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6a4`](#insn-00bbb6a4)

~~~json
{
  "source": "00bbb6a4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6b4`](#insn-00bbb6b4)

~~~json
{
  "source": "00bbb6b4",
  "target": "Stack[-0x5c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6bc`](#insn-00bbb6bc)

~~~json
{
  "source": "00bbb6bc",
  "target": "00bbb6f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6c4`](#insn-00bbb6c4)

~~~json
{
  "source": "00bbb6c4",
  "target": "00bbb798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6c8`](#insn-00bbb6c8)

~~~json
{
  "source": "00bbb6c8",
  "target": "Stack[-0x64]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6cc`](#insn-00bbb6cc)

~~~json
{
  "source": "00bbb6cc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6d4`](#insn-00bbb6d4)

~~~json
{
  "source": "00bbb6d4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6e4`](#insn-00bbb6e4)

~~~json
{
  "source": "00bbb6e4",
  "target": "00bbb798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6e8`](#insn-00bbb6e8)

~~~json
{
  "source": "00bbb6e8",
  "target": "00bbb72c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6f0`](#insn-00bbb6f0)

~~~json
{
  "source": "00bbb6f0",
  "target": "00bbb794",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6f4`](#insn-00bbb6f4)

~~~json
{
  "source": "00bbb6f4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb6fc`](#insn-00bbb6fc)

~~~json
{
  "source": "00bbb6fc",
  "target": "00bbb724",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb700`](#insn-00bbb700)

~~~json
{
  "source": "00bbb700",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb708`](#insn-00bbb708)

~~~json
{
  "source": "00bbb708",
  "target": "00bbb798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb70c`](#insn-00bbb70c)

~~~json
{
  "source": "00bbb70c",
  "target": "Stack[-0x64]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb714`](#insn-00bbb714)

~~~json
{
  "source": "00bbb714",
  "target": "00bbb798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb718`](#insn-00bbb718)

~~~json
{
  "source": "00bbb718",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb720`](#insn-00bbb720)

~~~json
{
  "source": "00bbb720",
  "target": "00bbb798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb724`](#insn-00bbb724)

~~~json
{
  "source": "00bbb724",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb728`](#insn-00bbb728)

~~~json
{
  "source": "00bbb728",
  "target": "00bbb798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb730`](#insn-00bbb730)

~~~json
{
  "source": "00bbb730",
  "target": "00bbb73c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb738`](#insn-00bbb738)

~~~json
{
  "source": "00bbb738",
  "target": "00bbb798",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb748`](#insn-00bbb748)

~~~json
{
  "source": "00bbb748",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb754`](#insn-00bbb754)

~~~json
{
  "source": "00bbb754",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb75c`](#insn-00bbb75c)

~~~json
{
  "source": "00bbb75c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb760`](#insn-00bbb760)

~~~json
{
  "source": "00bbb760",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb764`](#insn-00bbb764)

~~~json
{
  "source": "00bbb764",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb768`](#insn-00bbb768)

~~~json
{
  "source": "00bbb768",
  "target": "01000000",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb768`](#insn-00bbb768)

~~~json
{
  "source": "00bbb768",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb770`](#insn-00bbb770)

~~~json
{
  "source": "00bbb770",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb778`](#insn-00bbb778)

~~~json
{
  "source": "00bbb778",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb78c`](#insn-00bbb78c)

~~~json
{
  "source": "00bbb78c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb798`](#insn-00bbb798)

~~~json
{
  "source": "00bbb798",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb7a0`](#insn-00bbb7a0)

~~~json
{
  "source": "00bbb7a0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb7a4`](#insn-00bbb7a4)

~~~json
{
  "source": "00bbb7a4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbb7a8`](#insn-00bbb7a8)

~~~json
{
  "source": "00bbb7a8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
