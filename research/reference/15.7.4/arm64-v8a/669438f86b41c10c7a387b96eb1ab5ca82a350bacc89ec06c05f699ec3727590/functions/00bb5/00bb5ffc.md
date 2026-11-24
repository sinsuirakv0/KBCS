# 00bb5ffc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00bb5fb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00bb5/00bb5fb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0017.md#compare-2ba0e64f0e001b03f4ef130bb193658d)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c32a44`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c32/00c32a44.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0076.md#compare-b3c607eb7876e9023a05f60eaa636ae3)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb5ffc",
  "name": "FUN_00bb5ffc",
  "size": 1324,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e36e4d631ed1c6a96edd0a93b57b6d9db4d074eb9149b340c5216f4a11ac3b24",
  "source_text_sha256": "e36e4d631ed1c6a96edd0a93b57b6d9db4d074eb9149b340c5216f4a11ac3b24",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb5ffc",
        "00bb6527"
      ]
    ],
    "bytes_sha256": "3ec6d5dd39e02522d165a010cd66756312056420a920f7a28ad19224d7f63d2e",
    "instruction_count": 331,
    "instruction_bytes": 1324,
    "body_bytes": 1324,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bb5c14](../00bb5/00bb5c14.md)
- [00bb6528](../00bb6/00bb6528.md)

## 呼び出し先

- [00bb9248](../00bb9/00bb9248.md)
- [00bdb0f0](../00bdb/00bdb0f0.md)
- [00bdb7b0](../00bdb/00bdb7b0.md)
- [00be0fe0](../00be0/00be0fe0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 9023 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void FUN_00bb5ffc(undefined4 *param_1,byte *param_2,ulong param_3,char param_4,char param_5,
                 byte param_6)

{
  ulong uVar1;
  byte bVar2;
  size_t __n;
  byte *pbVar3;
  bool bVar4;
  undefined2 uVar5;
  long lVar6;
  long lVar7;
  byte *pbVar8;
  byte *pbVar10;
  long lVar11;
  byte *pbVar12;
  byte *pbVar13;
  byte *pbVar9;
  
  if ((param_3 & 1) == 0) {
    bVar4 = false;
  }
  else {
    uVar1 = (ulong)(*param_2 >> 1);
    if ((*param_2 & 1) != 0) {
      uVar1 = *(ulong *)(param_2 + 8);
    }
    bVar4 = uVar1 == 4;
  }
                    /* try { // try from 00bb6040 to 00cb604b has its CatchHandler @ 00bbabc4 */
  if (param_4 == '\x01') {
    if (param_6 < 2) {
      if (param_6 == 0) {
        *param_1 = (int)DAT_002b2708;
joined_r0x00bb61d0:
        if (param_5 == '\0') {
          return;
        }
        if (param_5 == '\x02') {
          return;
        }
        if (param_5 != '\x01') goto LAB_00bb63c4;
        goto joined_r0x00bb63bc;
      }
      if (param_6 != 1) goto LAB_00bb63c4;
      *(undefined1 *)param_1 = 3;
      *(undefined1 *)((long)param_1 + 3) = 4;
    }
    else {
      if (param_6 == 2) {
        *(undefined1 *)param_1 = 2;
        *(undefined1 *)((long)param_1 + 3) = 3;
                    /* try { // try from 00bb6170 to 00cb617f has its CatchHandler @ 00bbada0 */
        if (param_5 == '\x02') {
                    /* try { // try from 00bb6438 to 00cb6443 has its CatchHandler @ 00bbade8 */
          uVar5 = 0x104;
          goto LAB_00bb643c;
        }
        if (param_5 != '\x01') {
          if (param_5 == '\0') {
            *(undefined2 *)((long)param_1 + 1) = 0x400;
            return;
          }
          goto LAB_00bb63c4;
        }
                    /* try { // try from 00bb6420 to 00cb642f has its CatchHandler @ 00bbade4 */
        uVar5 = 0x400;
        goto LAB_00bb64bc;
      }
      if (param_6 != 3) {
        if (param_6 == 4) {
          *(undefined1 *)param_1 = 2;
          *(undefined1 *)((long)param_1 + 3) = 4;
          if (param_5 == '\x02') {
            uVar5 = 0x300;
            goto LAB_00bb64bc;
          }
                    /* try { // try from 00bb610c to 00cb6117 has its CatchHandler @ 00bbacb0 */
          if (param_5 == '\x01') {
            uVar5 = 0x103;
            goto LAB_00bb643c;
          }
          if (param_5 == '\0') {
            *(undefined2 *)((long)param_1 + 1) = 3;
            return;
          }
        }
        goto LAB_00bb63c4;
      }
      *(undefined1 *)param_1 = 3;
      *(undefined1 *)((long)param_1 + 3) = 4;
    }
    if (param_5 == '\x02') {
      uVar5 = 0x201;
LAB_00bb643c:
      *(undefined2 *)((long)param_1 + 1) = uVar5;
      if (bVar4) {
        bVar2 = *param_2;
        uVar1 = (ulong)(bVar2 >> 1);
        if ((bVar2 & 1) != 0) {
          uVar1 = *(ulong *)(param_2 + 8);
        }
        lVar7 = uVar1 - 1;
        if ((bVar2 & 1) == 0) {
          pbVar10 = param_2 + 1;
          *param_2 = (byte)((int)lVar7 << 1);
        }
        else {
          pbVar10 = *(byte **)(param_2 + 0x10);
          *(long *)(param_2 + 8) = lVar7;
        }
        pbVar10[lVar7] = 0;
        return;
      }
      return;
    }
    if (param_5 == '\x01') {
      uVar5 = 2;
LAB_00bb64bc:
      *(undefined2 *)((long)param_1 + 1) = uVar5;
                    /* try { // try from 00bb64c0 to 00cb64cb has its CatchHandler @ 00bbacac */
      if (!bVar4) {
        _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE9push_backEc(param_2,0x20)
        ;
        return;
      }
      return;
    }
    if (param_5 == '\0') {
      *(undefined2 *)((long)param_1 + 1) = 2;
      return;
    }
LAB_00bb63c4:
    *param_1 = (int)DAT_002b27f8;
    return;
  }
  if (param_4 != '\0') goto LAB_00bb63c4;
  if (bVar4) {
    uVar1 = *(ulong *)(param_2 + 8);
    pbVar10 = *(byte **)(param_2 + 0x10);
                    /* try { // try from 00bb605c to 00cb6063 has its CatchHandler @ 00bbae50 */
    if ((*param_2 & 1) == 0) {
      pbVar10 = param_2 + 1;
      uVar1 = (ulong)(*param_2 >> 1);
    }
                    /* try { // try from 00bb606c to 00cb607b has its CatchHandler @ 00bbadf0 */
    lVar7 = uVar1 - 3;
    if (lVar7 != 0) {
      if (uVar1 == 4) {
                    /* try { // try from 00bb6084 to 00cb608f has its CatchHandler @ 00bbadec */
        bVar2 = pbVar10[3];
        __n = (long)(pbVar10 + 3) - (long)pbVar10;
        if (__n != 0) {
          memmove(pbVar10 + (4 - __n),pbVar10,__n);
        }
        *pbVar10 = bVar2;
      }
      else if (lVar7 == 3) {
        bVar2 = *pbVar10;
        *pbVar10 = pbVar10[3];
        pbVar10[3] = bVar2;
        if (uVar1 != 4) {
                    /* try { // try from 00bb620c to 00cb620f has its CatchHandler @ 00bbacf8 */
          bVar2 = pbVar10[1];
                    /* try { // try from 00bb6210 to 00cb628f has its CatchHandler @ 00bb3444 */
          pbVar10[1] = pbVar10[4];
          pbVar10[4] = bVar2;
          if (uVar1 != 5) {
            bVar2 = pbVar10[2];
            pbVar10[2] = pbVar10[5];
            pbVar10[5] = bVar2;
          }
        }
      }
      else {
        lVar11 = 3;
        do {
          lVar6 = lVar7;
          lVar7 = 0;
          if (lVar6 != 0) {
            lVar7 = lVar11 / lVar6;
          }
          lVar7 = lVar11 - lVar7 * lVar6;
          lVar11 = lVar6;
        } while (lVar7 != 0);
        pbVar9 = pbVar10 + lVar6;
        do {
          pbVar8 = pbVar9 + -1;
          bVar2 = *pbVar8;
          pbVar12 = pbVar8;
          pbVar9 = pbVar9 + 2;
          do {
            pbVar13 = pbVar9;
            pbVar3 = pbVar13;
            if ((long)(pbVar10 + (uVar1 - (long)pbVar13)) < 4) {
              pbVar3 = pbVar10 + -(long)(pbVar10 + (uVar1 - (long)pbVar13));
            }
            *pbVar12 = *pbVar13;
            pbVar12 = pbVar13;
            pbVar9 = pbVar3 + 3;
                    /* try { // try from 00bb6290 to 00cb6297 has its CatchHandler @ 00bbacdc */
          } while (pbVar3 + 3 != pbVar8);
          *pbVar13 = bVar2;
          pbVar9 = pbVar8;
        } while (pbVar8 != pbVar10);
      }
    }
  }
  if (param_6 < 2) {
    if (param_6 == 0) {
      *param_1 = (int)DAT_002b2bf8;
      goto joined_r0x00bb61d0;
    }
    if (param_6 != 1) goto LAB_00bb63c4;
    *(undefined1 *)param_1 = 3;
    *(undefined1 *)((long)param_1 + 3) = 2;
    if (param_5 == '\x02') {
      uVar5 = 0x401;
      goto LAB_00bb64ec;
    }
    if (param_5 != '\x01') {
      if (param_5 == '\0') {
        *(undefined2 *)((long)param_1 + 1) = 4;
        return;
      }
      goto LAB_00bb63c4;
    }
    uVar5 = 4;
  }
  else {
    if (param_6 == 2) {
      *(undefined1 *)param_1 = 4;
      *(undefined1 *)((long)param_1 + 3) = 3;
      if (param_5 != '\x02') {
                    /* try { // try from 00bb634c to 00cb6357 has its CatchHandler @ 00bba79c */
        if (param_5 == '\x01') {
                    /* try { // try from 00bb63f4 to 00cb63ff has its CatchHandler @ 00bbabc0 */
          if (!bVar4) {
            _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmmc
                      (param_2,0,1,0x20);
                    /* try { // try from 00bb6410 to 00cb6417 has its CatchHandler @ 00bbae4c */
          }
          goto LAB_00bb6358;
        }
LAB_00bb6354:
        if (param_5 == '\0') {
LAB_00bb6358:
                    /* try { // try from 00bb6358 to 00cb6367 has its CatchHandler @ 00bba788 */
          *(undefined2 *)((long)param_1 + 1) = 0x200;
          return;
        }
        goto LAB_00bb63c4;
      }
LAB_00bb63ec:
      uVar5 = 0x102;
LAB_00bb64ec:
      *(undefined2 *)((long)param_1 + 1) = uVar5;
      if (bVar4) {
        pbVar10 = *(byte **)(param_2 + 0x10);
        if ((*param_2 & 1) == 0) {
          pbVar10 = param_2 + 1;
        }
                    /* try { // try from 00bb6524 to 00cb6533 has its CatchHandler @ 00bbad9c */
        FUN_00bb9248(param_2,pbVar10);
        return;
      }
      return;
    }
    if (param_6 == 3) {
                    /* try { // try from 00bb6368 to 00cb637b has its CatchHandler @ 00bba75c */
      *(undefined1 *)param_1 = 4;
      *(undefined1 *)((long)param_1 + 3) = 2;
      if (param_5 != '\x02') {
        if (param_5 == '\x01') {
          uVar5 = 0x301;
          goto LAB_00bb64ec;
        }
        if (param_5 == '\0') {
          *(undefined2 *)((long)param_1 + 1) = 0x300;
          return;
        }
        goto LAB_00bb63c4;
      }
      uVar5 = 3;
    }
    else {
      if (param_6 != 4) goto LAB_00bb63c4;
      *(undefined1 *)param_1 = 4;
      *(undefined1 *)((long)param_1 + 3) = 3;
      if (param_5 == '\x02') goto LAB_00bb63ec;
      if (param_5 != '\x01') goto LAB_00bb6354;
      uVar5 = 0x200;
    }
  }
  *(undefined2 *)((long)param_1 + 1) = uVar5;
joined_r0x00bb63bc:
  if (!bVar4) {
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmmc(param_2,0,1,0x20);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb5ffc"></a> `00bb5ffc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bb6000"></a> `00bb6000` | `fd 7b bb a9` | stp x29,x30,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bb6004"></a> `00bb6004` | `f9 0b 00 f9` | str x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb6008"></a> `00bb6008` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb600c"></a> `00bb600c` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb6010"></a> `00bb6010` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb6014"></a> `00bb6014` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bb6018"></a> `00bb6018` | `22 01 00 36` | tbz w2,#0x0,0x00bb603c | `CONDITIONAL_JUMP`
<a id="insn-00bb601c"></a> `00bb601c` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bb6020"></a> `00bb6020` | `29 04 40 f9` | ldr x9,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bb6024"></a> `00bb6024` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6028"></a> `00bb6028` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb602c"></a> `00bb602c` | `48 01 89 9a` | csel x8,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bb6030"></a> `00bb6030` | `1f 11 00 f1` | cmp x8,#0x4 | `FALL_THROUGH`
<a id="insn-00bb6034"></a> `00bb6034` | `f4 17 9f 1a` | cset w20,eq | `FALL_THROUGH`
<a id="insn-00bb6038"></a> `00bb6038` | `02 00 00 14` | b 0x00bb6040 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb603c"></a> `00bb603c` | `f4 03 1f 2a` | mov w20,wzr | `FALL_THROUGH`
<a id="insn-00bb6040"></a> `00bb6040` | `68 1c 00 12` | and w8,w3,#0xff | `FALL_THROUGH`
<a id="insn-00bb6044"></a> `00bb6044` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6048"></a> `00bb6048` | `00 04 00 54` | b.eq 0x00bb60c8 | `CONDITIONAL_JUMP`
<a id="insn-00bb604c"></a> `00bb604c` | `c8 1b 00 35` | cbnz w8,0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb6050"></a> `00bb6050` | `94 12 00 34` | cbz w20,0x00bb62a0 | `CONDITIONAL_JUMP`
<a id="insn-00bb6054"></a> `00bb6054` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bb6058"></a> `00bb6058` | `29 ac 40 a9` | ldp x9,x11,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bb605c"></a> `00bb605c` | `0a fd 41 d3` | lsr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6060"></a> `00bb6060` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6064"></a> `00bb6064` | `73 15 81 9a` | csinc x19,x11,x1,ne | `FALL_THROUGH`
<a id="insn-00bb6068"></a> `00bb6068` | `4a 01 89 9a` | csel x10,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bb606c"></a> `00bb606c` | `49 0d 00 f1` | subs x9,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb6070"></a> `00bb6070` | `80 11 00 54` | b.eq 0x00bb62a0 | `CONDITIONAL_JUMP`
<a id="insn-00bb6074"></a> `00bb6074` | `5f 11 00 f1` | cmp x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bb6078"></a> `00bb6078` | `68 02 0a 8b` | add x8,x19,x10 | `FALL_THROUGH`
<a id="insn-00bb607c"></a> `00bb607c` | `61 0b 00 54` | b.ne 0x00bb61e8 | `CONDITIONAL_JUMP`
<a id="insn-00bb6080"></a> `00bb6080` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00bb6084"></a> `00bb6084` | `35 fd 5f 38` | ldrb w21,[x9, #-0x1]! | `FALL_THROUGH`
<a id="insn-00bb6088"></a> `00bb6088` | `22 01 13 eb` | subs x2,x9,x19 | `FALL_THROUGH`
<a id="insn-00bb608c"></a> `00bb608c` | `a0 01 00 54` | b.eq 0x00bb60c0 | `CONDITIONAL_JUMP`
<a id="insn-00bb6090"></a> `00bb6090` | `08 01 02 cb` | sub x8,x8,x2 | `FALL_THROUGH`
<a id="insn-00bb6094"></a> `00bb6094` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bb6098"></a> `00bb6098` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bb609c"></a> `00bb609c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bb60a0"></a> `00bb60a0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bb60a4"></a> `00bb60a4` | `f8 03 04 2a` | mov w24,w4 | `FALL_THROUGH`
<a id="insn-00bb60a8"></a> `00bb60a8` | `f9 03 05 2a` | mov w25,w5 | `FALL_THROUGH`
<a id="insn-00bb60ac"></a> `00bb60ac` | `11 94 00 94` | bl 0x00bdb0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb60b0"></a> `00bb60b0` | `e5 03 19 2a` | mov w5,w25 | `FALL_THROUGH`
<a id="insn-00bb60b4"></a> `00bb60b4` | `e4 03 18 2a` | mov w4,w24 | `FALL_THROUGH`
<a id="insn-00bb60b8"></a> `00bb60b8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bb60bc"></a> `00bb60bc` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bb60c0"></a> `00bb60c0` | `75 02 00 39` | strb w21,[x19] | `FALL_THROUGH`
<a id="insn-00bb60c4"></a> `00bb60c4` | `77 00 00 14` | b 0x00bb62a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb60c8"></a> `00bb60c8` | `a8 1c 00 12` | and w8,w5,#0xff | `FALL_THROUGH`
<a id="insn-00bb60cc"></a> `00bb60cc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb60d0"></a> `00bb60d0` | `8d 02 00 54` | b.le 0x00bb6120 | `CONDITIONAL_JUMP`
<a id="insn-00bb60d4"></a> `00bb60d4` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb60d8"></a> `00bb60d8` | `00 04 00 54` | b.eq 0x00bb6158 | `CONDITIONAL_JUMP`
<a id="insn-00bb60dc"></a> `00bb60dc` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bb60e0"></a> `00bb60e0` | `60 05 00 54` | b.eq 0x00bb618c | `CONDITIONAL_JUMP`
<a id="insn-00bb60e4"></a> `00bb60e4` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bb60e8"></a> `00bb60e8` | `e1 16 00 54` | b.ne 0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb60ec"></a> `00bb60ec` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00bb60f0"></a> `00bb60f0` | `88 1c 00 12` | and w8,w4,#0xff | `FALL_THROUGH`
<a id="insn-00bb60f4"></a> `00bb60f4` | `09 00 00 39` | strb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bb60f8"></a> `00bb60f8` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bb60fc"></a> `00bb60fc` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb6100"></a> `00bb6100` | `09 0c 00 39` | strb w9,[x0, #0x3] | `FALL_THROUGH`
<a id="insn-00bb6104"></a> `00bb6104` | `a0 1d 00 54` | b.eq 0x00bb64b8 | `CONDITIONAL_JUMP`
<a id="insn-00bb6108"></a> `00bb6108` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb610c"></a> `00bb610c` | `20 19 00 54` | b.eq 0x00bb6430 | `CONDITIONAL_JUMP`
<a id="insn-00bb6110"></a> `00bb6110` | `a8 15 00 35` | cbnz w8,0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb6114"></a> `00bb6114` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bb6118"></a> `00bb6118` | `08 10 00 78` | sturh w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bb611c"></a> `00bb611c` | `ad 00 00 14` | b 0x00bb63d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6120"></a> `00bb6120` | `08 05 00 34` | cbz w8,0x00bb61c0 | `CONDITIONAL_JUMP`
<a id="insn-00bb6124"></a> `00bb6124` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6128"></a> `00bb6128` | `e1 14 00 54` | b.ne 0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb612c"></a> `00bb612c` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bb6130"></a> `00bb6130` | `88 1c 00 12` | and w8,w4,#0xff | `FALL_THROUGH`
<a id="insn-00bb6134"></a> `00bb6134` | `09 00 00 39` | strb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bb6138"></a> `00bb6138` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bb613c"></a> `00bb613c` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb6140"></a> `00bb6140` | `09 0c 00 39` | strb w9,[x0, #0x3] | `FALL_THROUGH`
<a id="insn-00bb6144"></a> `00bb6144` | `80 07 00 54` | b.eq 0x00bb6234 | `CONDITIONAL_JUMP`
<a id="insn-00bb6148"></a> `00bb6148` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb614c"></a> `00bb614c` | `21 03 00 54` | b.ne 0x00bb61b0 | `CONDITIONAL_JUMP`
<a id="insn-00bb6150"></a> `00bb6150` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb6154"></a> `00bb6154` | `da 00 00 14` | b 0x00bb64bc | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6158"></a> `00bb6158` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00bb615c"></a> `00bb615c` | `88 1c 00 12` | and w8,w4,#0xff | `FALL_THROUGH`
<a id="insn-00bb6160"></a> `00bb6160` | `09 00 00 39` | strb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bb6164"></a> `00bb6164` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bb6168"></a> `00bb6168` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb616c"></a> `00bb616c` | `09 0c 00 39` | strb w9,[x0, #0x3] | `FALL_THROUGH`
<a id="insn-00bb6170"></a> `00bb6170` | `40 16 00 54` | b.eq 0x00bb6438 | `CONDITIONAL_JUMP`
<a id="insn-00bb6174"></a> `00bb6174` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6178"></a> `00bb6178` | `40 15 00 54` | b.eq 0x00bb6420 | `CONDITIONAL_JUMP`
<a id="insn-00bb617c"></a> `00bb617c` | `48 12 00 35` | cbnz w8,0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb6180"></a> `00bb6180` | `08 80 80 52` | mov w8,#0x400 | `FALL_THROUGH`
<a id="insn-00bb6184"></a> `00bb6184` | `08 10 00 78` | sturh w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bb6188"></a> `00bb6188` | `92 00 00 14` | b 0x00bb63d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb618c"></a> `00bb618c` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bb6190"></a> `00bb6190` | `88 1c 00 12` | and w8,w4,#0xff | `FALL_THROUGH`
<a id="insn-00bb6194"></a> `00bb6194` | `09 00 00 39` | strb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bb6198"></a> `00bb6198` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bb619c"></a> `00bb619c` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb61a0"></a> `00bb61a0` | `09 0c 00 39` | strb w9,[x0, #0x3] | `FALL_THROUGH`
<a id="insn-00bb61a4"></a> `00bb61a4` | `80 04 00 54` | b.eq 0x00bb6234 | `CONDITIONAL_JUMP`
<a id="insn-00bb61a8"></a> `00bb61a8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb61ac"></a> `00bb61ac` | `20 fd ff 54` | b.eq 0x00bb6150 | `CONDITIONAL_JUMP`
<a id="insn-00bb61b0"></a> `00bb61b0` | `a8 10 00 35` | cbnz w8,0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb61b4"></a> `00bb61b4` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb61b8"></a> `00bb61b8` | `08 10 00 78` | sturh w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bb61bc"></a> `00bb61bc` | `85 00 00 14` | b 0x00bb63d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb61c0"></a> `00bb61c0` | `e8 b7 ff 90` | adrp x8,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bb61c4"></a> `00bb61c4` | `00 85 43 fd` | ldr d0,[x8, #0x708] | `FALL_THROUGH`
<a id="insn-00bb61c8"></a> `00bb61c8` | `88 1c 00 72` | ands w8,w4,#0xff | `FALL_THROUGH`
<a id="insn-00bb61cc"></a> `00bb61cc` | `00 00 00 bd` | str s0,[x0] | `FALL_THROUGH`
<a id="insn-00bb61d0"></a> `00bb61d0` | `00 10 00 54` | b.eq 0x00bb63d0 | `CONDITIONAL_JUMP`
<a id="insn-00bb61d4"></a> `00bb61d4` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb61d8"></a> `00bb61d8` | `c0 0f 00 54` | b.eq 0x00bb63d0 | `CONDITIONAL_JUMP`
<a id="insn-00bb61dc"></a> `00bb61dc` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb61e0"></a> `00bb61e0` | `e0 0e 00 54` | b.eq 0x00bb63bc | `CONDITIONAL_JUMP`
<a id="insn-00bb61e4"></a> `00bb61e4` | `78 00 00 14` | b 0x00bb63c4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb61e8"></a> `00bb61e8` | `3f 0d 00 f1` | cmp x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bb61ec"></a> `00bb61ec` | `81 02 00 54` | b.ne 0x00bb623c | `CONDITIONAL_JUMP`
<a id="insn-00bb61f0"></a> `00bb61f0` | `69 0e 40 39` | ldrb w9,[x19, #0x3] | `FALL_THROUGH`
<a id="insn-00bb61f4"></a> `00bb61f4` | `6b 02 40 39` | ldrb w11,[x19] | `FALL_THROUGH`
<a id="insn-00bb61f8"></a> `00bb61f8` | `48 11 00 f1` | subs x8,x10,#0x4 | `FALL_THROUGH`
<a id="insn-00bb61fc"></a> `00bb61fc` | `69 02 00 39` | strb w9,[x19] | `FALL_THROUGH`
<a id="insn-00bb6200"></a> `00bb6200` | `6b 0e 00 39` | strb w11,[x19, #0x3] | `FALL_THROUGH`
<a id="insn-00bb6204"></a> `00bb6204` | `e0 04 00 54` | b.eq 0x00bb62a0 | `CONDITIONAL_JUMP`
<a id="insn-00bb6208"></a> `00bb6208` | `69 12 40 39` | ldrb w9,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00bb620c"></a> `00bb620c` | `6a 06 40 39` | ldrb w10,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bb6210"></a> `00bb6210` | `1f 05 00 f1` | cmp x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6214"></a> `00bb6214` | `69 06 00 39` | strb w9,[x19, #0x1] | `FALL_THROUGH`
<a id="insn-00bb6218"></a> `00bb6218` | `6a 12 00 39` | strb w10,[x19, #0x4] | `FALL_THROUGH`
<a id="insn-00bb621c"></a> `00bb621c` | `20 04 00 54` | b.eq 0x00bb62a0 | `CONDITIONAL_JUMP`
<a id="insn-00bb6220"></a> `00bb6220` | `68 16 40 39` | ldrb w8,[x19, #0x5] | `FALL_THROUGH`
<a id="insn-00bb6224"></a> `00bb6224` | `69 0a 40 39` | ldrb w9,[x19, #0x2] | `FALL_THROUGH`
<a id="insn-00bb6228"></a> `00bb6228` | `68 0a 00 39` | strb w8,[x19, #0x2] | `FALL_THROUGH`
<a id="insn-00bb622c"></a> `00bb622c` | `69 16 00 39` | strb w9,[x19, #0x5] | `FALL_THROUGH`
<a id="insn-00bb6230"></a> `00bb6230` | `1c 00 00 14` | b 0x00bb62a0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6234"></a> `00bb6234` | `28 40 80 52` | mov w8,#0x201 | `FALL_THROUGH`
<a id="insn-00bb6238"></a> `00bb6238` | `81 00 00 14` | b 0x00bb643c | `UNCONDITIONAL_JUMP`
<a id="insn-00bb623c"></a> `00bb623c` | `6a 00 80 52` | mov w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb6240"></a> `00bb6240` | `eb 03 0a aa` | mov x11,x10 | `FALL_THROUGH`
<a id="insn-00bb6244"></a> `00bb6244` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-00bb6248"></a> `00bb6248` | `69 0d c9 9a` | sdiv x9,x11,x9 | `FALL_THROUGH`
<a id="insn-00bb624c"></a> `00bb624c` | `29 ad 0a 9b` | msub x9,x9,x10,x11 | `FALL_THROUGH`
<a id="insn-00bb6250"></a> `00bb6250` | `89 ff ff b5` | cbnz x9,0x00bb6240 | `CONDITIONAL_JUMP`
<a id="insn-00bb6254"></a> `00bb6254` | `69 02 0a 8b` | add x9,x19,x10 | `FALL_THROUGH`
<a id="insn-00bb6258"></a> `00bb6258` | `2a fd 5f 38` | ldrb w10,[x9, #-0x1]! | `FALL_THROUGH`
<a id="insn-00bb625c"></a> `00bb625c` | `2d 0d 00 91` | add x13,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bb6260"></a> `00bb6260` | `ec 03 09 aa` | mov x12,x9 | `FALL_THROUGH`
<a id="insn-00bb6264"></a> `00bb6264` | `eb 03 0d aa` | mov x11,x13 | `FALL_THROUGH`
<a id="insn-00bb6268"></a> `00bb6268` | `0d 01 0d cb` | sub x13,x8,x13 | `FALL_THROUGH`
<a id="insn-00bb626c"></a> `00bb626c` | `6e 02 0d cb` | sub x14,x19,x13 | `FALL_THROUGH`
<a id="insn-00bb6270"></a> `00bb6270` | `ef 03 0b aa` | mov x15,x11 | `FALL_THROUGH`
<a id="insn-00bb6274"></a> `00bb6274` | `bf 0d 00 f1` | cmp x13,#0x3 | `FALL_THROUGH`
<a id="insn-00bb6278"></a> `00bb6278` | `ce 0d 00 91` | add x14,x14,#0x3 | `FALL_THROUGH`
<a id="insn-00bb627c"></a> `00bb627c` | `f0 35 40 38` | ldrb w16,[x15], #0x3 | `FALL_THROUGH`
<a id="insn-00bb6280"></a> `00bb6280` | `ed c1 8e 9a` | csel x13,x15,x14,gt | `FALL_THROUGH`
<a id="insn-00bb6284"></a> `00bb6284` | `bf 01 09 eb` | cmp x13,x9 | `FALL_THROUGH`
<a id="insn-00bb6288"></a> `00bb6288` | `90 01 00 39` | strb w16,[x12] | `FALL_THROUGH`
<a id="insn-00bb628c"></a> `00bb628c` | `ec 03 0b aa` | mov x12,x11 | `FALL_THROUGH`
<a id="insn-00bb6290"></a> `00bb6290` | `a1 fe ff 54` | b.ne 0x00bb6264 | `CONDITIONAL_JUMP`
<a id="insn-00bb6294"></a> `00bb6294` | `3f 01 13 eb` | cmp x9,x19 | `FALL_THROUGH`
<a id="insn-00bb6298"></a> `00bb6298` | `6a 01 00 39` | strb w10,[x11] | `FALL_THROUGH`
<a id="insn-00bb629c"></a> `00bb629c` | `e1 fd ff 54` | b.ne 0x00bb6258 | `CONDITIONAL_JUMP`
<a id="insn-00bb62a0"></a> `00bb62a0` | `a8 1c 00 12` | and w8,w5,#0xff | `FALL_THROUGH`
<a id="insn-00bb62a4"></a> `00bb62a4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb62a8"></a> `00bb62a8` | `4d 02 00 54` | b.le 0x00bb62f0 | `CONDITIONAL_JUMP`
<a id="insn-00bb62ac"></a> `00bb62ac` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb62b0"></a> `00bb62b0` | `00 04 00 54` | b.eq 0x00bb6330 | `CONDITIONAL_JUMP`
<a id="insn-00bb62b4"></a> `00bb62b4` | `1f 0d 00 71` | cmp w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bb62b8"></a> `00bb62b8` | `60 05 00 54` | b.eq 0x00bb6364 | `CONDITIONAL_JUMP`
<a id="insn-00bb62bc"></a> `00bb62bc` | `1f 11 00 71` | cmp w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bb62c0"></a> `00bb62c0` | `21 08 00 54` | b.ne 0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb62c4"></a> `00bb62c4` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bb62c8"></a> `00bb62c8` | `88 1c 00 12` | and w8,w4,#0xff | `FALL_THROUGH`
<a id="insn-00bb62cc"></a> `00bb62cc` | `09 00 00 39` | strb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bb62d0"></a> `00bb62d0` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bb62d4"></a> `00bb62d4` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb62d8"></a> `00bb62d8` | `09 0c 00 39` | strb w9,[x0, #0x3] | `FALL_THROUGH`
<a id="insn-00bb62dc"></a> `00bb62dc` | `80 08 00 54` | b.eq 0x00bb63ec | `CONDITIONAL_JUMP`
<a id="insn-00bb62e0"></a> `00bb62e0` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb62e4"></a> `00bb62e4` | `81 03 00 54` | b.ne 0x00bb6354 | `CONDITIONAL_JUMP`
<a id="insn-00bb62e8"></a> `00bb62e8` | `08 40 80 52` | mov w8,#0x200 | `FALL_THROUGH`
<a id="insn-00bb62ec"></a> `00bb62ec` | `62 00 00 14` | b 0x00bb6474 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb62f0"></a> `00bb62f0` | `48 05 00 34` | cbz w8,0x00bb6398 | `CONDITIONAL_JUMP`
<a id="insn-00bb62f4"></a> `00bb62f4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb62f8"></a> `00bb62f8` | `61 06 00 54` | b.ne 0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb62fc"></a> `00bb62fc` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bb6300"></a> `00bb6300` | `88 1c 00 12` | and w8,w4,#0xff | `FALL_THROUGH`
<a id="insn-00bb6304"></a> `00bb6304` | `09 00 00 39` | strb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bb6308"></a> `00bb6308` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00bb630c"></a> `00bb630c` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb6310"></a> `00bb6310` | `09 0c 00 39` | strb w9,[x0, #0x3] | `FALL_THROUGH`
<a id="insn-00bb6314"></a> `00bb6314` | `a0 0e 00 54` | b.eq 0x00bb64e8 | `CONDITIONAL_JUMP`
<a id="insn-00bb6318"></a> `00bb6318` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb631c"></a> `00bb631c` | `a0 0a 00 54` | b.eq 0x00bb6470 | `CONDITIONAL_JUMP`
<a id="insn-00bb6320"></a> `00bb6320` | `28 05 00 35` | cbnz w8,0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb6324"></a> `00bb6324` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bb6328"></a> `00bb6328` | `08 10 00 78` | sturh w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bb632c"></a> `00bb632c` | `29 00 00 14` | b 0x00bb63d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6330"></a> `00bb6330` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bb6334"></a> `00bb6334` | `88 1c 00 12` | and w8,w4,#0xff | `FALL_THROUGH`
<a id="insn-00bb6338"></a> `00bb6338` | `09 00 00 39` | strb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bb633c"></a> `00bb633c` | `69 00 80 52` | mov w9,#0x3 | `FALL_THROUGH`
<a id="insn-00bb6340"></a> `00bb6340` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb6344"></a> `00bb6344` | `09 0c 00 39` | strb w9,[x0, #0x3] | `FALL_THROUGH`
<a id="insn-00bb6348"></a> `00bb6348` | `20 05 00 54` | b.eq 0x00bb63ec | `CONDITIONAL_JUMP`
<a id="insn-00bb634c"></a> `00bb634c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6350"></a> `00bb6350` | `20 05 00 54` | b.eq 0x00bb63f4 | `CONDITIONAL_JUMP`
<a id="insn-00bb6354"></a> `00bb6354` | `88 03 00 35` | cbnz w8,0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb6358"></a> `00bb6358` | `08 40 80 52` | mov w8,#0x200 | `FALL_THROUGH`
<a id="insn-00bb635c"></a> `00bb635c` | `08 10 00 78` | sturh w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bb6360"></a> `00bb6360` | `1c 00 00 14` | b 0x00bb63d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6364"></a> `00bb6364` | `89 00 80 52` | mov w9,#0x4 | `FALL_THROUGH`
<a id="insn-00bb6368"></a> `00bb6368` | `88 1c 00 12` | and w8,w4,#0xff | `FALL_THROUGH`
<a id="insn-00bb636c"></a> `00bb636c` | `09 00 00 39` | strb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bb6370"></a> `00bb6370` | `49 00 80 52` | mov w9,#0x2 | `FALL_THROUGH`
<a id="insn-00bb6374"></a> `00bb6374` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb6378"></a> `00bb6378` | `09 0c 00 39` | strb w9,[x0, #0x3] | `FALL_THROUGH`
<a id="insn-00bb637c"></a> `00bb637c` | `60 05 00 54` | b.eq 0x00bb6428 | `CONDITIONAL_JUMP`
<a id="insn-00bb6380"></a> `00bb6380` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6384"></a> `00bb6384` | `a0 04 00 54` | b.eq 0x00bb6418 | `CONDITIONAL_JUMP`
<a id="insn-00bb6388"></a> `00bb6388` | `e8 01 00 35` | cbnz w8,0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb638c"></a> `00bb638c` | `08 60 80 52` | mov w8,#0x300 | `FALL_THROUGH`
<a id="insn-00bb6390"></a> `00bb6390` | `08 10 00 78` | sturh w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bb6394"></a> `00bb6394` | `0f 00 00 14` | b 0x00bb63d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6398"></a> `00bb6398` | `e8 b7 ff 90` | adrp x8,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bb639c"></a> `00bb639c` | `00 fd 45 fd` | ldr d0,[x8, #0xbf8] | `FALL_THROUGH`
<a id="insn-00bb63a0"></a> `00bb63a0` | `88 1c 00 72` | ands w8,w4,#0xff | `FALL_THROUGH`
<a id="insn-00bb63a4"></a> `00bb63a4` | `00 00 00 bd` | str s0,[x0] | `FALL_THROUGH`
<a id="insn-00bb63a8"></a> `00bb63a8` | `40 01 00 54` | b.eq 0x00bb63d0 | `CONDITIONAL_JUMP`
<a id="insn-00bb63ac"></a> `00bb63ac` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bb63b0"></a> `00bb63b0` | `00 01 00 54` | b.eq 0x00bb63d0 | `CONDITIONAL_JUMP`
<a id="insn-00bb63b4"></a> `00bb63b4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb63b8"></a> `00bb63b8` | `61 00 00 54` | b.ne 0x00bb63c4 | `CONDITIONAL_JUMP`
<a id="insn-00bb63bc"></a> `00bb63bc` | `14 06 00 36` | tbz w20,#0x0,0x00bb647c | `CONDITIONAL_JUMP`
<a id="insn-00bb63c0"></a> `00bb63c0` | `04 00 00 14` | b 0x00bb63d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb63c4"></a> `00bb63c4` | `e8 b7 ff 90` | adrp x8,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bb63c8"></a> `00bb63c8` | `00 fd 43 fd` | ldr d0,[x8, #0x7f8] | `FALL_THROUGH`
<a id="insn-00bb63cc"></a> `00bb63cc` | `00 00 00 bd` | str s0,[x0] | `FALL_THROUGH`
<a id="insn-00bb63d0"></a> `00bb63d0` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb63d4"></a> `00bb63d4` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb63d8"></a> `00bb63d8` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb63dc"></a> `00bb63dc` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb63e0"></a> `00bb63e0` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bb63e4"></a> `00bb63e4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb63e8"></a> `00bb63e8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bb63ec"></a> `00bb63ec` | `48 20 80 52` | mov w8,#0x102 | `FALL_THROUGH`
<a id="insn-00bb63f0"></a> `00bb63f0` | `3f 00 00 14` | b 0x00bb64ec | `UNCONDITIONAL_JUMP`
<a id="insn-00bb63f4"></a> `00bb63f4` | `34 fb 07 37` | tbnz w20,#0x0,0x00bb6358 | `CONDITIONAL_JUMP`
<a id="insn-00bb63f8"></a> `00bb63f8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb63fc"></a> `00bb63fc` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bb6400"></a> `00bb6400` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bb6404"></a> `00bb6404` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6408"></a> `00bb6408` | `03 04 80 52` | mov w3,#0x20 | `FALL_THROUGH`
<a id="insn-00bb640c"></a> `00bb640c` | `f5 aa 00 94` | bl 0x00be0fe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb6410"></a> `00bb6410` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb6414"></a> `00bb6414` | `d1 ff ff 17` | b 0x00bb6358 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6418"></a> `00bb6418` | `28 60 80 52` | mov w8,#0x301 | `FALL_THROUGH`
<a id="insn-00bb641c"></a> `00bb641c` | `34 00 00 14` | b 0x00bb64ec | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6420"></a> `00bb6420` | `08 80 80 52` | mov w8,#0x400 | `FALL_THROUGH`
<a id="insn-00bb6424"></a> `00bb6424` | `26 00 00 14` | b 0x00bb64bc | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6428"></a> `00bb6428` | `68 00 80 52` | mov w8,#0x3 | `FALL_THROUGH`
<a id="insn-00bb642c"></a> `00bb642c` | `12 00 00 14` | b 0x00bb6474 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6430"></a> `00bb6430` | `68 20 80 52` | mov w8,#0x103 | `FALL_THROUGH`
<a id="insn-00bb6434"></a> `00bb6434` | `02 00 00 14` | b 0x00bb643c | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6438"></a> `00bb6438` | `88 20 80 52` | mov w8,#0x104 | `FALL_THROUGH`
<a id="insn-00bb643c"></a> `00bb643c` | `08 10 00 78` | sturh w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bb6440"></a> `00bb6440` | `94 fc ff 34` | cbz w20,0x00bb63d0 | `CONDITIONAL_JUMP`
<a id="insn-00bb6444"></a> `00bb6444` | `29 00 40 39` | ldrb w9,[x1] | `FALL_THROUGH`
<a id="insn-00bb6448"></a> `00bb6448` | `28 04 40 f9` | ldr x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bb644c"></a> `00bb644c` | `2a fd 41 d3` | lsr x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6450"></a> `00bb6450` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6454"></a> `00bb6454` | `48 01 88 9a` | csel x8,x10,x8,eq | `FALL_THROUGH`
<a id="insn-00bb6458"></a> `00bb6458` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb645c"></a> `00bb645c` | `69 02 00 37` | tbnz w9,#0x0,0x00bb64a8 | `CONDITIONAL_JUMP`
<a id="insn-00bb6460"></a> `00bb6460` | `09 79 1f 53` | lsl w9,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6464"></a> `00bb6464` | `29 14 00 38` | strb w9,[x1], #0x1 | `FALL_THROUGH`
<a id="insn-00bb6468"></a> `00bb6468` | `e9 03 01 aa` | mov x9,x1 | `FALL_THROUGH`
<a id="insn-00bb646c"></a> `00bb646c` | `11 00 00 14` | b 0x00bb64b0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb6470"></a> `00bb6470` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bb6474"></a> `00bb6474` | `08 10 00 78` | sturh w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bb6478"></a> `00bb6478` | `d4 fa 07 37` | tbnz w20,#0x0,0x00bb63d0 | `CONDITIONAL_JUMP`
<a id="insn-00bb647c"></a> `00bb647c` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bb6480"></a> `00bb6480` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00bb6484"></a> `00bb6484` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6488"></a> `00bb6488` | `03 04 80 52` | mov w3,#0x20 | `FALL_THROUGH`
<a id="insn-00bb648c"></a> `00bb648c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb6490"></a> `00bb6490` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb6494"></a> `00bb6494` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb6498"></a> `00bb6498` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb649c"></a> `00bb649c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bb64a0"></a> `00bb64a0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb64a4"></a> `00bb64a4` | `cf aa 00 14` | b 0x00be0fe0 | `CALL_TERMINATOR`
<a id="insn-00bb64a8"></a> `00bb64a8` | `29 08 40 f9` | ldr x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bb64ac"></a> `00bb64ac` | `28 04 00 f9` | str x8,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-00bb64b0"></a> `00bb64b0` | `3f 69 28 38` | strb wzr,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bb64b4"></a> `00bb64b4` | `c7 ff ff 17` | b 0x00bb63d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb64b8"></a> `00bb64b8` | `08 60 80 52` | mov w8,#0x300 | `FALL_THROUGH`
<a id="insn-00bb64bc"></a> `00bb64bc` | `08 10 00 78` | sturh w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bb64c0"></a> `00bb64c0` | `94 f8 07 37` | tbnz w20,#0x0,0x00bb63d0 | `CONDITIONAL_JUMP`
<a id="insn-00bb64c4"></a> `00bb64c4` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bb64c8"></a> `00bb64c8` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bb64cc"></a> `00bb64cc` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb64d0"></a> `00bb64d0` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb64d4"></a> `00bb64d4` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb64d8"></a> `00bb64d8` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb64dc"></a> `00bb64dc` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bb64e0"></a> `00bb64e0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb64e4"></a> `00bb64e4` | `b3 94 00 14` | b 0x00bdb7b0 | `CALL_TERMINATOR`
<a id="insn-00bb64e8"></a> `00bb64e8` | `28 80 80 52` | mov w8,#0x401 | `FALL_THROUGH`
<a id="insn-00bb64ec"></a> `00bb64ec` | `08 10 00 78` | sturh w8,[x0, #0x1] | `FALL_THROUGH`
<a id="insn-00bb64f0"></a> `00bb64f0` | `14 f7 ff 34` | cbz w20,0x00bb63d0 | `CONDITIONAL_JUMP`
<a id="insn-00bb64f4"></a> `00bb64f4` | `28 00 40 39` | ldrb w8,[x1] | `FALL_THROUGH`
<a id="insn-00bb64f8"></a> `00bb64f8` | `29 08 40 f9` | ldr x9,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bb64fc"></a> `00bb64fc` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-00bb6500"></a> `00bb6500` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb6504"></a> `00bb6504` | `28 15 81 9a` | csinc x8,x9,x1,ne | `FALL_THROUGH`
<a id="insn-00bb6508"></a> `00bb6508` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00bb650c"></a> `00bb650c` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb6510"></a> `00bb6510` | `f9 0b 40 f9` | ldr x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb6514"></a> `00bb6514` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb6518"></a> `00bb6518` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb651c"></a> `00bb651c` | `fd 7b c5 a8` | ldp x29,x30,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bb6520"></a> `00bb6520` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bb6524"></a> `00bb6524` | `49 0b 00 14` | b 0x00bb9248 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb5ffc`](#insn-00bb5ffc) 範囲 `[['00bb5ffc', '00bb601b']]`
  - `CONDITIONAL_JUMP` [`00bb6018`](#insn-00bb6018) → [`00bb603c`](#insn-00bb603c)
  - `FALL_THROUGH` [`00bb6018`](#insn-00bb6018) → [`00bb601c`](#insn-00bb601c)
- ブロック [`00bb601c`](#insn-00bb601c) 範囲 `[['00bb601c', '00bb603b']]`
  - `UNCONDITIONAL_JUMP` [`00bb6038`](#insn-00bb6038) → [`00bb6040`](#insn-00bb6040)
- ブロック [`00bb603c`](#insn-00bb603c) 範囲 `[['00bb603c', '00bb603f']]`
  - `FALL_THROUGH` [`00bb603c`](#insn-00bb603c) → [`00bb6040`](#insn-00bb6040)
- ブロック [`00bb6040`](#insn-00bb6040) 範囲 `[['00bb6040', '00bb604b']]`
  - `CONDITIONAL_JUMP` [`00bb6048`](#insn-00bb6048) → [`00bb60c8`](#insn-00bb60c8)
  - `FALL_THROUGH` [`00bb6048`](#insn-00bb6048) → [`00bb604c`](#insn-00bb604c)
- ブロック [`00bb604c`](#insn-00bb604c) 範囲 `[['00bb604c', '00bb604f']]`
  - `CONDITIONAL_JUMP` [`00bb604c`](#insn-00bb604c) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb604c`](#insn-00bb604c) → [`00bb6050`](#insn-00bb6050)
- ブロック [`00bb6050`](#insn-00bb6050) 範囲 `[['00bb6050', '00bb6053']]`
  - `CONDITIONAL_JUMP` [`00bb6050`](#insn-00bb6050) → [`00bb62a0`](#insn-00bb62a0)
  - `FALL_THROUGH` [`00bb6050`](#insn-00bb6050) → [`00bb6054`](#insn-00bb6054)
- ブロック [`00bb6054`](#insn-00bb6054) 範囲 `[['00bb6054', '00bb605b']]`
  - `FALL_THROUGH` [`00bb6058`](#insn-00bb6058) → [`00bb605c`](#insn-00bb605c)
- ブロック [`00bb605c`](#insn-00bb605c) 範囲 `[['00bb605c', '00bb606b']]`
  - `FALL_THROUGH` [`00bb6068`](#insn-00bb6068) → [`00bb606c`](#insn-00bb606c)
- ブロック [`00bb606c`](#insn-00bb606c) 範囲 `[['00bb606c', '00bb6073']]`
  - `CONDITIONAL_JUMP` [`00bb6070`](#insn-00bb6070) → [`00bb62a0`](#insn-00bb62a0)
  - `FALL_THROUGH` [`00bb6070`](#insn-00bb6070) → [`00bb6074`](#insn-00bb6074)
- ブロック [`00bb6074`](#insn-00bb6074) 範囲 `[['00bb6074', '00bb607f']]`
  - `CONDITIONAL_JUMP` [`00bb607c`](#insn-00bb607c) → [`00bb61e8`](#insn-00bb61e8)
  - `FALL_THROUGH` [`00bb607c`](#insn-00bb607c) → [`00bb6080`](#insn-00bb6080)
- ブロック [`00bb6080`](#insn-00bb6080) 範囲 `[['00bb6080', '00bb6083']]`
  - `FALL_THROUGH` [`00bb6080`](#insn-00bb6080) → [`00bb6084`](#insn-00bb6084)
- ブロック [`00bb6084`](#insn-00bb6084) 範囲 `[['00bb6084', '00bb608f']]`
  - `CONDITIONAL_JUMP` [`00bb608c`](#insn-00bb608c) → [`00bb60c0`](#insn-00bb60c0)
  - `FALL_THROUGH` [`00bb608c`](#insn-00bb608c) → [`00bb6090`](#insn-00bb6090)
- ブロック [`00bb6090`](#insn-00bb6090) 範囲 `[['00bb6090', '00bb60bf']]`
  - `FALL_THROUGH` [`00bb60bc`](#insn-00bb60bc) → [`00bb60c0`](#insn-00bb60c0)
- ブロック [`00bb60c0`](#insn-00bb60c0) 範囲 `[['00bb60c0', '00bb60c7']]`
  - `UNCONDITIONAL_JUMP` [`00bb60c4`](#insn-00bb60c4) → [`00bb62a0`](#insn-00bb62a0)
- ブロック [`00bb60c8`](#insn-00bb60c8) 範囲 `[['00bb60c8', '00bb60d3']]`
  - `CONDITIONAL_JUMP` [`00bb60d0`](#insn-00bb60d0) → [`00bb6120`](#insn-00bb6120)
  - `FALL_THROUGH` [`00bb60d0`](#insn-00bb60d0) → [`00bb60d4`](#insn-00bb60d4)
- ブロック [`00bb60d4`](#insn-00bb60d4) 範囲 `[['00bb60d4', '00bb60db']]`
  - `CONDITIONAL_JUMP` [`00bb60d8`](#insn-00bb60d8) → [`00bb6158`](#insn-00bb6158)
  - `FALL_THROUGH` [`00bb60d8`](#insn-00bb60d8) → [`00bb60dc`](#insn-00bb60dc)
- ブロック [`00bb60dc`](#insn-00bb60dc) 範囲 `[['00bb60dc', '00bb60e3']]`
  - `CONDITIONAL_JUMP` [`00bb60e0`](#insn-00bb60e0) → [`00bb618c`](#insn-00bb618c)
  - `FALL_THROUGH` [`00bb60e0`](#insn-00bb60e0) → [`00bb60e4`](#insn-00bb60e4)
- ブロック [`00bb60e4`](#insn-00bb60e4) 範囲 `[['00bb60e4', '00bb60eb']]`
  - `CONDITIONAL_JUMP` [`00bb60e8`](#insn-00bb60e8) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb60e8`](#insn-00bb60e8) → [`00bb60ec`](#insn-00bb60ec)
- ブロック [`00bb60ec`](#insn-00bb60ec) 範囲 `[['00bb60ec', '00bb6107']]`
  - `CONDITIONAL_JUMP` [`00bb6104`](#insn-00bb6104) → [`00bb64b8`](#insn-00bb64b8)
  - `FALL_THROUGH` [`00bb6104`](#insn-00bb6104) → [`00bb6108`](#insn-00bb6108)
- ブロック [`00bb6108`](#insn-00bb6108) 範囲 `[['00bb6108', '00bb610b']]`
  - `FALL_THROUGH` [`00bb6108`](#insn-00bb6108) → [`00bb610c`](#insn-00bb610c)
- ブロック [`00bb610c`](#insn-00bb610c) 範囲 `[['00bb610c', '00bb610f']]`
  - `CONDITIONAL_JUMP` [`00bb610c`](#insn-00bb610c) → [`00bb6430`](#insn-00bb6430)
  - `FALL_THROUGH` [`00bb610c`](#insn-00bb610c) → [`00bb6110`](#insn-00bb6110)
- ブロック [`00bb6110`](#insn-00bb6110) 範囲 `[['00bb6110', '00bb6113']]`
  - `CONDITIONAL_JUMP` [`00bb6110`](#insn-00bb6110) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb6110`](#insn-00bb6110) → [`00bb6114`](#insn-00bb6114)
- ブロック [`00bb6114`](#insn-00bb6114) 範囲 `[['00bb6114', '00bb611f']]`
  - `UNCONDITIONAL_JUMP` [`00bb611c`](#insn-00bb611c) → [`00bb63d0`](#insn-00bb63d0)
- ブロック [`00bb6120`](#insn-00bb6120) 範囲 `[['00bb6120', '00bb6123']]`
  - `CONDITIONAL_JUMP` [`00bb6120`](#insn-00bb6120) → [`00bb61c0`](#insn-00bb61c0)
  - `FALL_THROUGH` [`00bb6120`](#insn-00bb6120) → [`00bb6124`](#insn-00bb6124)
- ブロック [`00bb6124`](#insn-00bb6124) 範囲 `[['00bb6124', '00bb612b']]`
  - `CONDITIONAL_JUMP` [`00bb6128`](#insn-00bb6128) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb6128`](#insn-00bb6128) → [`00bb612c`](#insn-00bb612c)
- ブロック [`00bb612c`](#insn-00bb612c) 範囲 `[['00bb612c', '00bb6147']]`
  - `CONDITIONAL_JUMP` [`00bb6144`](#insn-00bb6144) → [`00bb6234`](#insn-00bb6234)
  - `FALL_THROUGH` [`00bb6144`](#insn-00bb6144) → [`00bb6148`](#insn-00bb6148)
- ブロック [`00bb6148`](#insn-00bb6148) 範囲 `[['00bb6148', '00bb614f']]`
  - `CONDITIONAL_JUMP` [`00bb614c`](#insn-00bb614c) → [`00bb61b0`](#insn-00bb61b0)
  - `FALL_THROUGH` [`00bb614c`](#insn-00bb614c) → [`00bb6150`](#insn-00bb6150)
- ブロック [`00bb6150`](#insn-00bb6150) 範囲 `[['00bb6150', '00bb6157']]`
  - `UNCONDITIONAL_JUMP` [`00bb6154`](#insn-00bb6154) → [`00bb64bc`](#insn-00bb64bc)
- ブロック [`00bb6158`](#insn-00bb6158) 範囲 `[['00bb6158', '00bb616f']]`
  - `FALL_THROUGH` [`00bb616c`](#insn-00bb616c) → [`00bb6170`](#insn-00bb6170)
- ブロック [`00bb6170`](#insn-00bb6170) 範囲 `[['00bb6170', '00bb6173']]`
  - `CONDITIONAL_JUMP` [`00bb6170`](#insn-00bb6170) → [`00bb6438`](#insn-00bb6438)
  - `FALL_THROUGH` [`00bb6170`](#insn-00bb6170) → [`00bb6174`](#insn-00bb6174)
- ブロック [`00bb6174`](#insn-00bb6174) 範囲 `[['00bb6174', '00bb617b']]`
  - `CONDITIONAL_JUMP` [`00bb6178`](#insn-00bb6178) → [`00bb6420`](#insn-00bb6420)
  - `FALL_THROUGH` [`00bb6178`](#insn-00bb6178) → [`00bb617c`](#insn-00bb617c)
- ブロック [`00bb617c`](#insn-00bb617c) 範囲 `[['00bb617c', '00bb617f']]`
  - `CONDITIONAL_JUMP` [`00bb617c`](#insn-00bb617c) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb617c`](#insn-00bb617c) → [`00bb6180`](#insn-00bb6180)
- ブロック [`00bb6180`](#insn-00bb6180) 範囲 `[['00bb6180', '00bb618b']]`
  - `UNCONDITIONAL_JUMP` [`00bb6188`](#insn-00bb6188) → [`00bb63d0`](#insn-00bb63d0)
- ブロック [`00bb618c`](#insn-00bb618c) 範囲 `[['00bb618c', '00bb61a7']]`
  - `CONDITIONAL_JUMP` [`00bb61a4`](#insn-00bb61a4) → [`00bb6234`](#insn-00bb6234)
  - `FALL_THROUGH` [`00bb61a4`](#insn-00bb61a4) → [`00bb61a8`](#insn-00bb61a8)
- ブロック [`00bb61a8`](#insn-00bb61a8) 範囲 `[['00bb61a8', '00bb61af']]`
  - `CONDITIONAL_JUMP` [`00bb61ac`](#insn-00bb61ac) → [`00bb6150`](#insn-00bb6150)
  - `FALL_THROUGH` [`00bb61ac`](#insn-00bb61ac) → [`00bb61b0`](#insn-00bb61b0)
- ブロック [`00bb61b0`](#insn-00bb61b0) 範囲 `[['00bb61b0', '00bb61b3']]`
  - `CONDITIONAL_JUMP` [`00bb61b0`](#insn-00bb61b0) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb61b0`](#insn-00bb61b0) → [`00bb61b4`](#insn-00bb61b4)
- ブロック [`00bb61b4`](#insn-00bb61b4) 範囲 `[['00bb61b4', '00bb61bf']]`
  - `UNCONDITIONAL_JUMP` [`00bb61bc`](#insn-00bb61bc) → [`00bb63d0`](#insn-00bb63d0)
- ブロック [`00bb61c0`](#insn-00bb61c0) 範囲 `[['00bb61c0', '00bb61d3']]`
  - `CONDITIONAL_JUMP` [`00bb61d0`](#insn-00bb61d0) → [`00bb63d0`](#insn-00bb63d0)
  - `FALL_THROUGH` [`00bb61d0`](#insn-00bb61d0) → [`00bb61d4`](#insn-00bb61d4)
- ブロック [`00bb61d4`](#insn-00bb61d4) 範囲 `[['00bb61d4', '00bb61db']]`
  - `CONDITIONAL_JUMP` [`00bb61d8`](#insn-00bb61d8) → [`00bb63d0`](#insn-00bb63d0)
  - `FALL_THROUGH` [`00bb61d8`](#insn-00bb61d8) → [`00bb61dc`](#insn-00bb61dc)
- ブロック [`00bb61dc`](#insn-00bb61dc) 範囲 `[['00bb61dc', '00bb61e3']]`
  - `CONDITIONAL_JUMP` [`00bb61e0`](#insn-00bb61e0) → [`00bb63bc`](#insn-00bb63bc)
  - `FALL_THROUGH` [`00bb61e0`](#insn-00bb61e0) → [`00bb61e4`](#insn-00bb61e4)
- ブロック [`00bb61e4`](#insn-00bb61e4) 範囲 `[['00bb61e4', '00bb61e7']]`
  - `UNCONDITIONAL_JUMP` [`00bb61e4`](#insn-00bb61e4) → [`00bb63c4`](#insn-00bb63c4)
- ブロック [`00bb61e8`](#insn-00bb61e8) 範囲 `[['00bb61e8', '00bb61ef']]`
  - `CONDITIONAL_JUMP` [`00bb61ec`](#insn-00bb61ec) → [`00bb623c`](#insn-00bb623c)
  - `FALL_THROUGH` [`00bb61ec`](#insn-00bb61ec) → [`00bb61f0`](#insn-00bb61f0)
- ブロック [`00bb61f0`](#insn-00bb61f0) 範囲 `[['00bb61f0', '00bb6207']]`
  - `CONDITIONAL_JUMP` [`00bb6204`](#insn-00bb6204) → [`00bb62a0`](#insn-00bb62a0)
  - `FALL_THROUGH` [`00bb6204`](#insn-00bb6204) → [`00bb6208`](#insn-00bb6208)
- ブロック [`00bb6208`](#insn-00bb6208) 範囲 `[['00bb6208', '00bb620b']]`
  - `FALL_THROUGH` [`00bb6208`](#insn-00bb6208) → [`00bb620c`](#insn-00bb620c)
- ブロック [`00bb620c`](#insn-00bb620c) 範囲 `[['00bb620c', '00bb620f']]`
  - `FALL_THROUGH` [`00bb620c`](#insn-00bb620c) → [`00bb6210`](#insn-00bb6210)
- ブロック [`00bb6210`](#insn-00bb6210) 範囲 `[['00bb6210', '00bb621f']]`
  - `CONDITIONAL_JUMP` [`00bb621c`](#insn-00bb621c) → [`00bb62a0`](#insn-00bb62a0)
  - `FALL_THROUGH` [`00bb621c`](#insn-00bb621c) → [`00bb6220`](#insn-00bb6220)
- ブロック [`00bb6220`](#insn-00bb6220) 範囲 `[['00bb6220', '00bb6233']]`
  - `UNCONDITIONAL_JUMP` [`00bb6230`](#insn-00bb6230) → [`00bb62a0`](#insn-00bb62a0)
- ブロック [`00bb6234`](#insn-00bb6234) 範囲 `[['00bb6234', '00bb623b']]`
  - `UNCONDITIONAL_JUMP` [`00bb6238`](#insn-00bb6238) → [`00bb643c`](#insn-00bb643c)
- ブロック [`00bb623c`](#insn-00bb623c) 範囲 `[['00bb623c', '00bb623f']]`
  - `FALL_THROUGH` [`00bb623c`](#insn-00bb623c) → [`00bb6240`](#insn-00bb6240)
- ブロック [`00bb6240`](#insn-00bb6240) 範囲 `[['00bb6240', '00bb6253']]`
  - `CONDITIONAL_JUMP` [`00bb6250`](#insn-00bb6250) → [`00bb6240`](#insn-00bb6240)
  - `FALL_THROUGH` [`00bb6250`](#insn-00bb6250) → [`00bb6254`](#insn-00bb6254)
- ブロック [`00bb6254`](#insn-00bb6254) 範囲 `[['00bb6254', '00bb6257']]`
  - `FALL_THROUGH` [`00bb6254`](#insn-00bb6254) → [`00bb6258`](#insn-00bb6258)
- ブロック [`00bb6258`](#insn-00bb6258) 範囲 `[['00bb6258', '00bb6263']]`
  - `FALL_THROUGH` [`00bb6260`](#insn-00bb6260) → [`00bb6264`](#insn-00bb6264)
- ブロック [`00bb6264`](#insn-00bb6264) 範囲 `[['00bb6264', '00bb628f']]`
  - `FALL_THROUGH` [`00bb628c`](#insn-00bb628c) → [`00bb6290`](#insn-00bb6290)
- ブロック [`00bb6290`](#insn-00bb6290) 範囲 `[['00bb6290', '00bb6293']]`
  - `CONDITIONAL_JUMP` [`00bb6290`](#insn-00bb6290) → [`00bb6264`](#insn-00bb6264)
  - `FALL_THROUGH` [`00bb6290`](#insn-00bb6290) → [`00bb6294`](#insn-00bb6294)
- ブロック [`00bb6294`](#insn-00bb6294) 範囲 `[['00bb6294', '00bb629f']]`
  - `CONDITIONAL_JUMP` [`00bb629c`](#insn-00bb629c) → [`00bb6258`](#insn-00bb6258)
  - `FALL_THROUGH` [`00bb629c`](#insn-00bb629c) → [`00bb62a0`](#insn-00bb62a0)
- ブロック [`00bb62a0`](#insn-00bb62a0) 範囲 `[['00bb62a0', '00bb62ab']]`
  - `CONDITIONAL_JUMP` [`00bb62a8`](#insn-00bb62a8) → [`00bb62f0`](#insn-00bb62f0)
  - `FALL_THROUGH` [`00bb62a8`](#insn-00bb62a8) → [`00bb62ac`](#insn-00bb62ac)
- ブロック [`00bb62ac`](#insn-00bb62ac) 範囲 `[['00bb62ac', '00bb62b3']]`
  - `CONDITIONAL_JUMP` [`00bb62b0`](#insn-00bb62b0) → [`00bb6330`](#insn-00bb6330)
  - `FALL_THROUGH` [`00bb62b0`](#insn-00bb62b0) → [`00bb62b4`](#insn-00bb62b4)
- ブロック [`00bb62b4`](#insn-00bb62b4) 範囲 `[['00bb62b4', '00bb62bb']]`
  - `CONDITIONAL_JUMP` [`00bb62b8`](#insn-00bb62b8) → [`00bb6364`](#insn-00bb6364)
  - `FALL_THROUGH` [`00bb62b8`](#insn-00bb62b8) → [`00bb62bc`](#insn-00bb62bc)
- ブロック [`00bb62bc`](#insn-00bb62bc) 範囲 `[['00bb62bc', '00bb62c3']]`
  - `CONDITIONAL_JUMP` [`00bb62c0`](#insn-00bb62c0) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb62c0`](#insn-00bb62c0) → [`00bb62c4`](#insn-00bb62c4)
- ブロック [`00bb62c4`](#insn-00bb62c4) 範囲 `[['00bb62c4', '00bb62df']]`
  - `CONDITIONAL_JUMP` [`00bb62dc`](#insn-00bb62dc) → [`00bb63ec`](#insn-00bb63ec)
  - `FALL_THROUGH` [`00bb62dc`](#insn-00bb62dc) → [`00bb62e0`](#insn-00bb62e0)
- ブロック [`00bb62e0`](#insn-00bb62e0) 範囲 `[['00bb62e0', '00bb62e7']]`
  - `CONDITIONAL_JUMP` [`00bb62e4`](#insn-00bb62e4) → [`00bb6354`](#insn-00bb6354)
  - `FALL_THROUGH` [`00bb62e4`](#insn-00bb62e4) → [`00bb62e8`](#insn-00bb62e8)
- ブロック [`00bb62e8`](#insn-00bb62e8) 範囲 `[['00bb62e8', '00bb62ef']]`
  - `UNCONDITIONAL_JUMP` [`00bb62ec`](#insn-00bb62ec) → [`00bb6474`](#insn-00bb6474)
- ブロック [`00bb62f0`](#insn-00bb62f0) 範囲 `[['00bb62f0', '00bb62f3']]`
  - `CONDITIONAL_JUMP` [`00bb62f0`](#insn-00bb62f0) → [`00bb6398`](#insn-00bb6398)
  - `FALL_THROUGH` [`00bb62f0`](#insn-00bb62f0) → [`00bb62f4`](#insn-00bb62f4)
- ブロック [`00bb62f4`](#insn-00bb62f4) 範囲 `[['00bb62f4', '00bb62fb']]`
  - `CONDITIONAL_JUMP` [`00bb62f8`](#insn-00bb62f8) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb62f8`](#insn-00bb62f8) → [`00bb62fc`](#insn-00bb62fc)
- ブロック [`00bb62fc`](#insn-00bb62fc) 範囲 `[['00bb62fc', '00bb6317']]`
  - `CONDITIONAL_JUMP` [`00bb6314`](#insn-00bb6314) → [`00bb64e8`](#insn-00bb64e8)
  - `FALL_THROUGH` [`00bb6314`](#insn-00bb6314) → [`00bb6318`](#insn-00bb6318)
- ブロック [`00bb6318`](#insn-00bb6318) 範囲 `[['00bb6318', '00bb631f']]`
  - `CONDITIONAL_JUMP` [`00bb631c`](#insn-00bb631c) → [`00bb6470`](#insn-00bb6470)
  - `FALL_THROUGH` [`00bb631c`](#insn-00bb631c) → [`00bb6320`](#insn-00bb6320)
- ブロック [`00bb6320`](#insn-00bb6320) 範囲 `[['00bb6320', '00bb6323']]`
  - `CONDITIONAL_JUMP` [`00bb6320`](#insn-00bb6320) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb6320`](#insn-00bb6320) → [`00bb6324`](#insn-00bb6324)
- ブロック [`00bb6324`](#insn-00bb6324) 範囲 `[['00bb6324', '00bb632f']]`
  - `UNCONDITIONAL_JUMP` [`00bb632c`](#insn-00bb632c) → [`00bb63d0`](#insn-00bb63d0)
- ブロック [`00bb6330`](#insn-00bb6330) 範囲 `[['00bb6330', '00bb634b']]`
  - `CONDITIONAL_JUMP` [`00bb6348`](#insn-00bb6348) → [`00bb63ec`](#insn-00bb63ec)
  - `FALL_THROUGH` [`00bb6348`](#insn-00bb6348) → [`00bb634c`](#insn-00bb634c)
- ブロック [`00bb634c`](#insn-00bb634c) 範囲 `[['00bb634c', '00bb6353']]`
  - `CONDITIONAL_JUMP` [`00bb6350`](#insn-00bb6350) → [`00bb63f4`](#insn-00bb63f4)
  - `FALL_THROUGH` [`00bb6350`](#insn-00bb6350) → [`00bb6354`](#insn-00bb6354)
- ブロック [`00bb6354`](#insn-00bb6354) 範囲 `[['00bb6354', '00bb6357']]`
  - `CONDITIONAL_JUMP` [`00bb6354`](#insn-00bb6354) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb6354`](#insn-00bb6354) → [`00bb6358`](#insn-00bb6358)
- ブロック [`00bb6358`](#insn-00bb6358) 範囲 `[['00bb6358', '00bb6363']]`
  - `UNCONDITIONAL_JUMP` [`00bb6360`](#insn-00bb6360) → [`00bb63d0`](#insn-00bb63d0)
- ブロック [`00bb6364`](#insn-00bb6364) 範囲 `[['00bb6364', '00bb6367']]`
  - `FALL_THROUGH` [`00bb6364`](#insn-00bb6364) → [`00bb6368`](#insn-00bb6368)
- ブロック [`00bb6368`](#insn-00bb6368) 範囲 `[['00bb6368', '00bb637f']]`
  - `CONDITIONAL_JUMP` [`00bb637c`](#insn-00bb637c) → [`00bb6428`](#insn-00bb6428)
  - `FALL_THROUGH` [`00bb637c`](#insn-00bb637c) → [`00bb6380`](#insn-00bb6380)
- ブロック [`00bb6380`](#insn-00bb6380) 範囲 `[['00bb6380', '00bb6387']]`
  - `CONDITIONAL_JUMP` [`00bb6384`](#insn-00bb6384) → [`00bb6418`](#insn-00bb6418)
  - `FALL_THROUGH` [`00bb6384`](#insn-00bb6384) → [`00bb6388`](#insn-00bb6388)
- ブロック [`00bb6388`](#insn-00bb6388) 範囲 `[['00bb6388', '00bb638b']]`
  - `CONDITIONAL_JUMP` [`00bb6388`](#insn-00bb6388) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb6388`](#insn-00bb6388) → [`00bb638c`](#insn-00bb638c)
- ブロック [`00bb638c`](#insn-00bb638c) 範囲 `[['00bb638c', '00bb6397']]`
  - `UNCONDITIONAL_JUMP` [`00bb6394`](#insn-00bb6394) → [`00bb63d0`](#insn-00bb63d0)
- ブロック [`00bb6398`](#insn-00bb6398) 範囲 `[['00bb6398', '00bb63ab']]`
  - `CONDITIONAL_JUMP` [`00bb63a8`](#insn-00bb63a8) → [`00bb63d0`](#insn-00bb63d0)
  - `FALL_THROUGH` [`00bb63a8`](#insn-00bb63a8) → [`00bb63ac`](#insn-00bb63ac)
- ブロック [`00bb63ac`](#insn-00bb63ac) 範囲 `[['00bb63ac', '00bb63b3']]`
  - `CONDITIONAL_JUMP` [`00bb63b0`](#insn-00bb63b0) → [`00bb63d0`](#insn-00bb63d0)
  - `FALL_THROUGH` [`00bb63b0`](#insn-00bb63b0) → [`00bb63b4`](#insn-00bb63b4)
- ブロック [`00bb63b4`](#insn-00bb63b4) 範囲 `[['00bb63b4', '00bb63bb']]`
  - `CONDITIONAL_JUMP` [`00bb63b8`](#insn-00bb63b8) → [`00bb63c4`](#insn-00bb63c4)
  - `FALL_THROUGH` [`00bb63b8`](#insn-00bb63b8) → [`00bb63bc`](#insn-00bb63bc)
- ブロック [`00bb63bc`](#insn-00bb63bc) 範囲 `[['00bb63bc', '00bb63bf']]`
  - `CONDITIONAL_JUMP` [`00bb63bc`](#insn-00bb63bc) → [`00bb647c`](#insn-00bb647c)
  - `FALL_THROUGH` [`00bb63bc`](#insn-00bb63bc) → [`00bb63c0`](#insn-00bb63c0)
- ブロック [`00bb63c0`](#insn-00bb63c0) 範囲 `[['00bb63c0', '00bb63c3']]`
  - `UNCONDITIONAL_JUMP` [`00bb63c0`](#insn-00bb63c0) → [`00bb63d0`](#insn-00bb63d0)
- ブロック [`00bb63c4`](#insn-00bb63c4) 範囲 `[['00bb63c4', '00bb63cf']]`
  - `FALL_THROUGH` [`00bb63cc`](#insn-00bb63cc) → [`00bb63d0`](#insn-00bb63d0)
- ブロック [`00bb63d0`](#insn-00bb63d0) 範囲 `[['00bb63d0', '00bb63eb']]`
- ブロック [`00bb63ec`](#insn-00bb63ec) 範囲 `[['00bb63ec', '00bb63f3']]`
  - `UNCONDITIONAL_JUMP` [`00bb63f0`](#insn-00bb63f0) → [`00bb64ec`](#insn-00bb64ec)
- ブロック [`00bb63f4`](#insn-00bb63f4) 範囲 `[['00bb63f4', '00bb63f7']]`
  - `CONDITIONAL_JUMP` [`00bb63f4`](#insn-00bb63f4) → [`00bb6358`](#insn-00bb6358)
  - `FALL_THROUGH` [`00bb63f4`](#insn-00bb63f4) → [`00bb63f8`](#insn-00bb63f8)
- ブロック [`00bb63f8`](#insn-00bb63f8) 範囲 `[['00bb63f8', '00bb640f']]`
  - `FALL_THROUGH` [`00bb640c`](#insn-00bb640c) → [`00bb6410`](#insn-00bb6410)
- ブロック [`00bb6410`](#insn-00bb6410) 範囲 `[['00bb6410', '00bb6417']]`
  - `UNCONDITIONAL_JUMP` [`00bb6414`](#insn-00bb6414) → [`00bb6358`](#insn-00bb6358)
- ブロック [`00bb6418`](#insn-00bb6418) 範囲 `[['00bb6418', '00bb641f']]`
  - `UNCONDITIONAL_JUMP` [`00bb641c`](#insn-00bb641c) → [`00bb64ec`](#insn-00bb64ec)
- ブロック [`00bb6420`](#insn-00bb6420) 範囲 `[['00bb6420', '00bb6427']]`
  - `UNCONDITIONAL_JUMP` [`00bb6424`](#insn-00bb6424) → [`00bb64bc`](#insn-00bb64bc)
- ブロック [`00bb6428`](#insn-00bb6428) 範囲 `[['00bb6428', '00bb642f']]`
  - `UNCONDITIONAL_JUMP` [`00bb642c`](#insn-00bb642c) → [`00bb6474`](#insn-00bb6474)
- ブロック [`00bb6430`](#insn-00bb6430) 範囲 `[['00bb6430', '00bb6437']]`
  - `UNCONDITIONAL_JUMP` [`00bb6434`](#insn-00bb6434) → [`00bb643c`](#insn-00bb643c)
- ブロック [`00bb6438`](#insn-00bb6438) 範囲 `[['00bb6438', '00bb643b']]`
  - `FALL_THROUGH` [`00bb6438`](#insn-00bb6438) → [`00bb643c`](#insn-00bb643c)
- ブロック [`00bb643c`](#insn-00bb643c) 範囲 `[['00bb643c', '00bb6443']]`
  - `CONDITIONAL_JUMP` [`00bb6440`](#insn-00bb6440) → [`00bb63d0`](#insn-00bb63d0)
  - `FALL_THROUGH` [`00bb6440`](#insn-00bb6440) → [`00bb6444`](#insn-00bb6444)
- ブロック [`00bb6444`](#insn-00bb6444) 範囲 `[['00bb6444', '00bb645f']]`
  - `CONDITIONAL_JUMP` [`00bb645c`](#insn-00bb645c) → [`00bb64a8`](#insn-00bb64a8)
  - `FALL_THROUGH` [`00bb645c`](#insn-00bb645c) → [`00bb6460`](#insn-00bb6460)
- ブロック [`00bb6460`](#insn-00bb6460) 範囲 `[['00bb6460', '00bb646f']]`
  - `UNCONDITIONAL_JUMP` [`00bb646c`](#insn-00bb646c) → [`00bb64b0`](#insn-00bb64b0)
- ブロック [`00bb6470`](#insn-00bb6470) 範囲 `[['00bb6470', '00bb6473']]`
  - `FALL_THROUGH` [`00bb6470`](#insn-00bb6470) → [`00bb6474`](#insn-00bb6474)
- ブロック [`00bb6474`](#insn-00bb6474) 範囲 `[['00bb6474', '00bb647b']]`
  - `CONDITIONAL_JUMP` [`00bb6478`](#insn-00bb6478) → [`00bb63d0`](#insn-00bb63d0)
  - `FALL_THROUGH` [`00bb6478`](#insn-00bb6478) → [`00bb647c`](#insn-00bb647c)
- ブロック [`00bb647c`](#insn-00bb647c) 範囲 `[['00bb647c', '00bb64a7']]`
- ブロック [`00bb64a8`](#insn-00bb64a8) 範囲 `[['00bb64a8', '00bb64af']]`
  - `FALL_THROUGH` [`00bb64ac`](#insn-00bb64ac) → [`00bb64b0`](#insn-00bb64b0)
- ブロック [`00bb64b0`](#insn-00bb64b0) 範囲 `[['00bb64b0', '00bb64b7']]`
  - `UNCONDITIONAL_JUMP` [`00bb64b4`](#insn-00bb64b4) → [`00bb63d0`](#insn-00bb63d0)
- ブロック [`00bb64b8`](#insn-00bb64b8) 範囲 `[['00bb64b8', '00bb64bb']]`
  - `FALL_THROUGH` [`00bb64b8`](#insn-00bb64b8) → [`00bb64bc`](#insn-00bb64bc)
- ブロック [`00bb64bc`](#insn-00bb64bc) 範囲 `[['00bb64bc', '00bb64bf']]`
  - `FALL_THROUGH` [`00bb64bc`](#insn-00bb64bc) → [`00bb64c0`](#insn-00bb64c0)
- ブロック [`00bb64c0`](#insn-00bb64c0) 範囲 `[['00bb64c0', '00bb64c3']]`
  - `CONDITIONAL_JUMP` [`00bb64c0`](#insn-00bb64c0) → [`00bb63d0`](#insn-00bb63d0)
  - `FALL_THROUGH` [`00bb64c0`](#insn-00bb64c0) → [`00bb64c4`](#insn-00bb64c4)
- ブロック [`00bb64c4`](#insn-00bb64c4) 範囲 `[['00bb64c4', '00bb64e7']]`
- ブロック [`00bb64e8`](#insn-00bb64e8) 範囲 `[['00bb64e8', '00bb64eb']]`
  - `FALL_THROUGH` [`00bb64e8`](#insn-00bb64e8) → [`00bb64ec`](#insn-00bb64ec)
- ブロック [`00bb64ec`](#insn-00bb64ec) 範囲 `[['00bb64ec', '00bb64f3']]`
  - `CONDITIONAL_JUMP` [`00bb64f0`](#insn-00bb64f0) → [`00bb63d0`](#insn-00bb63d0)
  - `FALL_THROUGH` [`00bb64f0`](#insn-00bb64f0) → [`00bb64f4`](#insn-00bb64f4)
- ブロック [`00bb64f4`](#insn-00bb64f4) 範囲 `[['00bb64f4', '00bb6523']]`
  - `FALL_THROUGH` [`00bb6520`](#insn-00bb6520) → [`00bb6524`](#insn-00bb6524)
- ブロック [`00bb6524`](#insn-00bb6524) 範囲 `[['00bb6524', '00bb6527']]`

## 命令位置別の参照

- [`00bb6000`](#insn-00bb6000) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6004`](#insn-00bb6004) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6008`](#insn-00bb6008) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb600c`](#insn-00bb600c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6010`](#insn-00bb6010) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6018`](#insn-00bb6018) → [`00bb603c`](#insn-00bb603c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6038`](#insn-00bb6038) → [`00bb6040`](#insn-00bb6040) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6048`](#insn-00bb6048) → [`00bb60c8`](#insn-00bb60c8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb604c`](#insn-00bb604c) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6050`](#insn-00bb6050) → [`00bb62a0`](#insn-00bb62a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6070`](#insn-00bb6070) → [`00bb62a0`](#insn-00bb62a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb607c`](#insn-00bb607c) → [`00bb61e8`](#insn-00bb61e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb608c`](#insn-00bb608c) → [`00bb60c0`](#insn-00bb60c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb60ac`](#insn-00bb60ac) → [`00bdb0f0`](../00bdb/00bdb0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bb60c4`](#insn-00bb60c4) → [`00bb62a0`](#insn-00bb62a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb60d0`](#insn-00bb60d0) → [`00bb6120`](#insn-00bb6120) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb60d8`](#insn-00bb60d8) → [`00bb6158`](#insn-00bb6158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb60e0`](#insn-00bb60e0) → [`00bb618c`](#insn-00bb618c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb60e8`](#insn-00bb60e8) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6104`](#insn-00bb6104) → [`00bb64b8`](#insn-00bb64b8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb610c`](#insn-00bb610c) → [`00bb6430`](#insn-00bb6430) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6110`](#insn-00bb6110) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb611c`](#insn-00bb611c) → [`00bb63d0`](#insn-00bb63d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6120`](#insn-00bb6120) → [`00bb61c0`](#insn-00bb61c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6128`](#insn-00bb6128) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6144`](#insn-00bb6144) → [`00bb6234`](#insn-00bb6234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb614c`](#insn-00bb614c) → [`00bb61b0`](#insn-00bb61b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6154`](#insn-00bb6154) → [`00bb64bc`](#insn-00bb64bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6170`](#insn-00bb6170) → [`00bb6438`](#insn-00bb6438) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6178`](#insn-00bb6178) → [`00bb6420`](#insn-00bb6420) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb617c`](#insn-00bb617c) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6188`](#insn-00bb6188) → [`00bb63d0`](#insn-00bb63d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb61a4`](#insn-00bb61a4) → [`00bb6234`](#insn-00bb6234) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb61ac`](#insn-00bb61ac) → [`00bb6150`](#insn-00bb6150) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb61b0`](#insn-00bb61b0) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb61bc`](#insn-00bb61bc) → [`00bb63d0`](#insn-00bb63d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb61c4`](#insn-00bb61c4) → `002b2708`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb61d0`](#insn-00bb61d0) → [`00bb63d0`](#insn-00bb63d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb61d8`](#insn-00bb61d8) → [`00bb63d0`](#insn-00bb63d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb61e0`](#insn-00bb61e0) → [`00bb63bc`](#insn-00bb63bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb61e4`](#insn-00bb61e4) → [`00bb63c4`](#insn-00bb63c4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb61ec`](#insn-00bb61ec) → [`00bb623c`](#insn-00bb623c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6204`](#insn-00bb6204) → [`00bb62a0`](#insn-00bb62a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb621c`](#insn-00bb621c) → [`00bb62a0`](#insn-00bb62a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6230`](#insn-00bb6230) → [`00bb62a0`](#insn-00bb62a0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6238`](#insn-00bb6238) → [`00bb643c`](#insn-00bb643c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6250`](#insn-00bb6250) → [`00bb6240`](#insn-00bb6240) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6290`](#insn-00bb6290) → [`00bb6264`](#insn-00bb6264) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb629c`](#insn-00bb629c) → [`00bb6258`](#insn-00bb6258) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb62a8`](#insn-00bb62a8) → [`00bb62f0`](#insn-00bb62f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb62b0`](#insn-00bb62b0) → [`00bb6330`](#insn-00bb6330) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb62b8`](#insn-00bb62b8) → [`00bb6364`](#insn-00bb6364) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb62c0`](#insn-00bb62c0) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb62dc`](#insn-00bb62dc) → [`00bb63ec`](#insn-00bb63ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb62e4`](#insn-00bb62e4) → [`00bb6354`](#insn-00bb6354) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb62ec`](#insn-00bb62ec) → [`00bb6474`](#insn-00bb6474) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb62f0`](#insn-00bb62f0) → [`00bb6398`](#insn-00bb6398) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb62f8`](#insn-00bb62f8) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6314`](#insn-00bb6314) → [`00bb64e8`](#insn-00bb64e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb631c`](#insn-00bb631c) → [`00bb6470`](#insn-00bb6470) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6320`](#insn-00bb6320) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb632c`](#insn-00bb632c) → [`00bb63d0`](#insn-00bb63d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6348`](#insn-00bb6348) → [`00bb63ec`](#insn-00bb63ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6350`](#insn-00bb6350) → [`00bb63f4`](#insn-00bb63f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6354`](#insn-00bb6354) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6360`](#insn-00bb6360) → [`00bb63d0`](#insn-00bb63d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb637c`](#insn-00bb637c) → [`00bb6428`](#insn-00bb6428) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6384`](#insn-00bb6384) → [`00bb6418`](#insn-00bb6418) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6388`](#insn-00bb6388) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6394`](#insn-00bb6394) → [`00bb63d0`](#insn-00bb63d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb639c`](#insn-00bb639c) → `002b2bf8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb63a8`](#insn-00bb63a8) → [`00bb63d0`](#insn-00bb63d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb63b0`](#insn-00bb63b0) → [`00bb63d0`](#insn-00bb63d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb63b8`](#insn-00bb63b8) → [`00bb63c4`](#insn-00bb63c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb63bc`](#insn-00bb63bc) → [`00bb647c`](#insn-00bb647c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb63c0`](#insn-00bb63c0) → [`00bb63d0`](#insn-00bb63d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb63c8`](#insn-00bb63c8) → `002b27f8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bb63d0`](#insn-00bb63d0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb63d4`](#insn-00bb63d4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb63d8`](#insn-00bb63d8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb63dc`](#insn-00bb63dc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb63e0`](#insn-00bb63e0) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb63f0`](#insn-00bb63f0) → [`00bb64ec`](#insn-00bb64ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb63f4`](#insn-00bb63f4) → [`00bb6358`](#insn-00bb6358) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb640c`](#insn-00bb640c) → [`00be0fe0`](../00be0/00be0fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bb6414`](#insn-00bb6414) → [`00bb6358`](#insn-00bb6358) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb641c`](#insn-00bb641c) → [`00bb64ec`](#insn-00bb64ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6424`](#insn-00bb6424) → [`00bb64bc`](#insn-00bb64bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb642c`](#insn-00bb642c) → [`00bb6474`](#insn-00bb6474) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6434`](#insn-00bb6434) → [`00bb643c`](#insn-00bb643c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6440`](#insn-00bb6440) → [`00bb63d0`](#insn-00bb63d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb645c`](#insn-00bb645c) → [`00bb64a8`](#insn-00bb64a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb646c`](#insn-00bb646c) → [`00bb64b0`](#insn-00bb64b0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6478`](#insn-00bb6478) → [`00bb63d0`](#insn-00bb63d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb648c`](#insn-00bb648c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6490`](#insn-00bb6490) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6494`](#insn-00bb6494) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6498`](#insn-00bb6498) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb649c`](#insn-00bb649c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb64a4`](#insn-00bb64a4) → [`00be0fe0`](../00be0/00be0fe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0fe0` · 推定シンボル `None` · 推定型 `None`
- [`00bb64b4`](#insn-00bb64b4) → [`00bb63d0`](#insn-00bb63d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb64c0`](#insn-00bb64c0) → [`00bb63d0`](#insn-00bb63d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb64cc`](#insn-00bb64cc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb64d0`](#insn-00bb64d0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb64d4`](#insn-00bb64d4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb64d8`](#insn-00bb64d8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb64dc`](#insn-00bb64dc) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb64e4`](#insn-00bb64e4) → [`00bdb7b0`](../00bdb/00bdb7b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7b0` · 推定シンボル `None` · 推定型 `None`
- [`00bb64f0`](#insn-00bb64f0) → [`00bb63d0`](#insn-00bb63d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb650c`](#insn-00bb650c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6510`](#insn-00bb6510) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6514`](#insn-00bb6514) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6518`](#insn-00bb6518) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb651c`](#insn-00bb651c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb6524`](#insn-00bb6524) → [`00bb9248`](../00bb9/00bb9248.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bb9248` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb6000`](#insn-00bb6000)

~~~json
{
  "source": "00bb6000",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6004`](#insn-00bb6004)

~~~json
{
  "source": "00bb6004",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6008`](#insn-00bb6008)

~~~json
{
  "source": "00bb6008",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb600c`](#insn-00bb600c)

~~~json
{
  "source": "00bb600c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6010`](#insn-00bb6010)

~~~json
{
  "source": "00bb6010",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6018`](#insn-00bb6018)

~~~json
{
  "source": "00bb6018",
  "target": "00bb603c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6038`](#insn-00bb6038)

~~~json
{
  "source": "00bb6038",
  "target": "00bb6040",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6048`](#insn-00bb6048)

~~~json
{
  "source": "00bb6048",
  "target": "00bb60c8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb604c`](#insn-00bb604c)

~~~json
{
  "source": "00bb604c",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6050`](#insn-00bb6050)

~~~json
{
  "source": "00bb6050",
  "target": "00bb62a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6070`](#insn-00bb6070)

~~~json
{
  "source": "00bb6070",
  "target": "00bb62a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb607c`](#insn-00bb607c)

~~~json
{
  "source": "00bb607c",
  "target": "00bb61e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb608c`](#insn-00bb608c)

~~~json
{
  "source": "00bb608c",
  "target": "00bb60c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb60ac`](#insn-00bb60ac)

~~~json
{
  "source": "00bb60ac",
  "target": "00bdb0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb60c4`](#insn-00bb60c4)

~~~json
{
  "source": "00bb60c4",
  "target": "00bb62a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb60d0`](#insn-00bb60d0)

~~~json
{
  "source": "00bb60d0",
  "target": "00bb6120",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb60d8`](#insn-00bb60d8)

~~~json
{
  "source": "00bb60d8",
  "target": "00bb6158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb60e0`](#insn-00bb60e0)

~~~json
{
  "source": "00bb60e0",
  "target": "00bb618c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb60e8`](#insn-00bb60e8)

~~~json
{
  "source": "00bb60e8",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6104`](#insn-00bb6104)

~~~json
{
  "source": "00bb6104",
  "target": "00bb64b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb610c`](#insn-00bb610c)

~~~json
{
  "source": "00bb610c",
  "target": "00bb6430",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6110`](#insn-00bb6110)

~~~json
{
  "source": "00bb6110",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb611c`](#insn-00bb611c)

~~~json
{
  "source": "00bb611c",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6120`](#insn-00bb6120)

~~~json
{
  "source": "00bb6120",
  "target": "00bb61c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6128`](#insn-00bb6128)

~~~json
{
  "source": "00bb6128",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6144`](#insn-00bb6144)

~~~json
{
  "source": "00bb6144",
  "target": "00bb6234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb614c`](#insn-00bb614c)

~~~json
{
  "source": "00bb614c",
  "target": "00bb61b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6154`](#insn-00bb6154)

~~~json
{
  "source": "00bb6154",
  "target": "00bb64bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6170`](#insn-00bb6170)

~~~json
{
  "source": "00bb6170",
  "target": "00bb6438",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6178`](#insn-00bb6178)

~~~json
{
  "source": "00bb6178",
  "target": "00bb6420",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb617c`](#insn-00bb617c)

~~~json
{
  "source": "00bb617c",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6188`](#insn-00bb6188)

~~~json
{
  "source": "00bb6188",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb61a4`](#insn-00bb61a4)

~~~json
{
  "source": "00bb61a4",
  "target": "00bb6234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb61ac`](#insn-00bb61ac)

~~~json
{
  "source": "00bb61ac",
  "target": "00bb6150",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb61b0`](#insn-00bb61b0)

~~~json
{
  "source": "00bb61b0",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb61bc`](#insn-00bb61bc)

~~~json
{
  "source": "00bb61bc",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb61c4`](#insn-00bb61c4)

~~~json
{
  "source": "00bb61c4",
  "target": "002b2708",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2708",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0302000400000000",
  "capture_start": "002b2708",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bb61d0`](#insn-00bb61d0)

~~~json
{
  "source": "00bb61d0",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb61d8`](#insn-00bb61d8)

~~~json
{
  "source": "00bb61d8",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb61e0`](#insn-00bb61e0)

~~~json
{
  "source": "00bb61e0",
  "target": "00bb63bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb61e4`](#insn-00bb61e4)

~~~json
{
  "source": "00bb61e4",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb61ec`](#insn-00bb61ec)

~~~json
{
  "source": "00bb61ec",
  "target": "00bb623c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6204`](#insn-00bb6204)

~~~json
{
  "source": "00bb6204",
  "target": "00bb62a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb621c`](#insn-00bb621c)

~~~json
{
  "source": "00bb621c",
  "target": "00bb62a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6230`](#insn-00bb6230)

~~~json
{
  "source": "00bb6230",
  "target": "00bb62a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6238`](#insn-00bb6238)

~~~json
{
  "source": "00bb6238",
  "target": "00bb643c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6250`](#insn-00bb6250)

~~~json
{
  "source": "00bb6250",
  "target": "00bb6240",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6290`](#insn-00bb6290)

~~~json
{
  "source": "00bb6290",
  "target": "00bb6264",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb629c`](#insn-00bb629c)

~~~json
{
  "source": "00bb629c",
  "target": "00bb6258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb62a8`](#insn-00bb62a8)

~~~json
{
  "source": "00bb62a8",
  "target": "00bb62f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb62b0`](#insn-00bb62b0)

~~~json
{
  "source": "00bb62b0",
  "target": "00bb6330",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb62b8`](#insn-00bb62b8)

~~~json
{
  "source": "00bb62b8",
  "target": "00bb6364",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb62c0`](#insn-00bb62c0)

~~~json
{
  "source": "00bb62c0",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb62dc`](#insn-00bb62dc)

~~~json
{
  "source": "00bb62dc",
  "target": "00bb63ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb62e4`](#insn-00bb62e4)

~~~json
{
  "source": "00bb62e4",
  "target": "00bb6354",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb62ec`](#insn-00bb62ec)

~~~json
{
  "source": "00bb62ec",
  "target": "00bb6474",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb62f0`](#insn-00bb62f0)

~~~json
{
  "source": "00bb62f0",
  "target": "00bb6398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb62f8`](#insn-00bb62f8)

~~~json
{
  "source": "00bb62f8",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6314`](#insn-00bb6314)

~~~json
{
  "source": "00bb6314",
  "target": "00bb64e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb631c`](#insn-00bb631c)

~~~json
{
  "source": "00bb631c",
  "target": "00bb6470",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6320`](#insn-00bb6320)

~~~json
{
  "source": "00bb6320",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb632c`](#insn-00bb632c)

~~~json
{
  "source": "00bb632c",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6348`](#insn-00bb6348)

~~~json
{
  "source": "00bb6348",
  "target": "00bb63ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6350`](#insn-00bb6350)

~~~json
{
  "source": "00bb6350",
  "target": "00bb63f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6354`](#insn-00bb6354)

~~~json
{
  "source": "00bb6354",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6360`](#insn-00bb6360)

~~~json
{
  "source": "00bb6360",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb637c`](#insn-00bb637c)

~~~json
{
  "source": "00bb637c",
  "target": "00bb6428",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6384`](#insn-00bb6384)

~~~json
{
  "source": "00bb6384",
  "target": "00bb6418",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6388`](#insn-00bb6388)

~~~json
{
  "source": "00bb6388",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6394`](#insn-00bb6394)

~~~json
{
  "source": "00bb6394",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb639c`](#insn-00bb639c)

~~~json
{
  "source": "00bb639c",
  "target": "002b2bf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2bf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0304000200000000",
  "capture_start": "002b2bf8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bb63a8`](#insn-00bb63a8)

~~~json
{
  "source": "00bb63a8",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb63b0`](#insn-00bb63b0)

~~~json
{
  "source": "00bb63b0",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb63b8`](#insn-00bb63b8)

~~~json
{
  "source": "00bb63b8",
  "target": "00bb63c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb63bc`](#insn-00bb63bc)

~~~json
{
  "source": "00bb63bc",
  "target": "00bb647c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb63c0`](#insn-00bb63c0)

~~~json
{
  "source": "00bb63c0",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb63c8`](#insn-00bb63c8)

~~~json
{
  "source": "00bb63c8",
  "target": "002b27f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b27f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "0203000400000000",
  "capture_start": "002b27f8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bb63d0`](#insn-00bb63d0)

~~~json
{
  "source": "00bb63d0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb63d4`](#insn-00bb63d4)

~~~json
{
  "source": "00bb63d4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb63d8`](#insn-00bb63d8)

~~~json
{
  "source": "00bb63d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb63dc`](#insn-00bb63dc)

~~~json
{
  "source": "00bb63dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb63e0`](#insn-00bb63e0)

~~~json
{
  "source": "00bb63e0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb63f0`](#insn-00bb63f0)

~~~json
{
  "source": "00bb63f0",
  "target": "00bb64ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb63f4`](#insn-00bb63f4)

~~~json
{
  "source": "00bb63f4",
  "target": "00bb6358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb640c`](#insn-00bb640c)

~~~json
{
  "source": "00bb640c",
  "target": "00be0fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb6414`](#insn-00bb6414)

~~~json
{
  "source": "00bb6414",
  "target": "00bb6358",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb641c`](#insn-00bb641c)

~~~json
{
  "source": "00bb641c",
  "target": "00bb64ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6424`](#insn-00bb6424)

~~~json
{
  "source": "00bb6424",
  "target": "00bb64bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb642c`](#insn-00bb642c)

~~~json
{
  "source": "00bb642c",
  "target": "00bb6474",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6434`](#insn-00bb6434)

~~~json
{
  "source": "00bb6434",
  "target": "00bb643c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6440`](#insn-00bb6440)

~~~json
{
  "source": "00bb6440",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb645c`](#insn-00bb645c)

~~~json
{
  "source": "00bb645c",
  "target": "00bb64a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb646c`](#insn-00bb646c)

~~~json
{
  "source": "00bb646c",
  "target": "00bb64b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6478`](#insn-00bb6478)

~~~json
{
  "source": "00bb6478",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb648c`](#insn-00bb648c)

~~~json
{
  "source": "00bb648c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6490`](#insn-00bb6490)

~~~json
{
  "source": "00bb6490",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6494`](#insn-00bb6494)

~~~json
{
  "source": "00bb6494",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6498`](#insn-00bb6498)

~~~json
{
  "source": "00bb6498",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb649c`](#insn-00bb649c)

~~~json
{
  "source": "00bb649c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb64a4`](#insn-00bb64a4)

~~~json
{
  "source": "00bb64a4",
  "target": "00be0fe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb64b4`](#insn-00bb64b4)

~~~json
{
  "source": "00bb64b4",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb64c0`](#insn-00bb64c0)

~~~json
{
  "source": "00bb64c0",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb64cc`](#insn-00bb64cc)

~~~json
{
  "source": "00bb64cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb64d0`](#insn-00bb64d0)

~~~json
{
  "source": "00bb64d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb64d4`](#insn-00bb64d4)

~~~json
{
  "source": "00bb64d4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb64d8`](#insn-00bb64d8)

~~~json
{
  "source": "00bb64d8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb64dc`](#insn-00bb64dc)

~~~json
{
  "source": "00bb64dc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb64e4`](#insn-00bb64e4)

~~~json
{
  "source": "00bb64e4",
  "target": "00bdb7b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb64f0`](#insn-00bb64f0)

~~~json
{
  "source": "00bb64f0",
  "target": "00bb63d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb650c`](#insn-00bb650c)

~~~json
{
  "source": "00bb650c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6510`](#insn-00bb6510)

~~~json
{
  "source": "00bb6510",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6514`](#insn-00bb6514)

~~~json
{
  "source": "00bb6514",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6518`](#insn-00bb6518)

~~~json
{
  "source": "00bb6518",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb651c`](#insn-00bb651c)

~~~json
{
  "source": "00bb651c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb6524`](#insn-00bb6524)

~~~json
{
  "source": "00bb6524",
  "target": "00bb9248",
  "target_space": "ram",
  "resolution": "function"
}
~~~
