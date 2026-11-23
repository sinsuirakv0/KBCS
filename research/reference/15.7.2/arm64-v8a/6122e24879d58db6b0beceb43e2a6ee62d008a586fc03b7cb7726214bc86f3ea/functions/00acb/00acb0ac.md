# 00acb0ac

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00acb174`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00acb/00acb174.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-2bb8be75ea0565d06de719a2c0bdfebd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acb0ac",
  "name": "FUN_00acb0ac",
  "size": 632,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6b03d6619afa14ef4752ca5f72039c794a5b1ffe0f9f3c11ff22d5909cc791b4",
  "source_text_sha256": "6b03d6619afa14ef4752ca5f72039c794a5b1ffe0f9f3c11ff22d5909cc791b4",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acb0ac",
        "00acb2f7"
      ],
      [
        "00acb304",
        "00acb32f"
      ]
    ],
    "bytes_sha256": "fd974235a4eb59a064811426d96439418a28f3934a00711ea5fe8f997be90795",
    "instruction_count": 158,
    "instruction_bytes": 632,
    "body_bytes": 632,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00abf464](../00abf/00abf464.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [005f064c](../005f0/005f064c.md)
- [0062c99c](../0062c/0062c99c.md)
- [0062ca28](../0062c/0062ca28.md)
- [00acb330](../00acb/00acb330.md)
- [00acb44c](../00acb/00acb44c.md)
- [00acb508](../00acb/00acb508.md)
- [00bd6fec](../00bd6/00bd6fec.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3478 bytes

~~~c

long FUN_00acb0ac(long *param_1,long *param_2)

{
  ulong uVar1;
  long lVar2;
  long lVar3;
  long *plVar4;
  long lVar5;
  undefined8 *puVar6;
  void *__ptr;
  undefined8 uVar7;
  long lVar8;
  undefined8 *puVar9;
  long lVar10;
  ulong uVar11;
  long *plVar12;
  long *plVar13;
  undefined8 *puVar14;
  void *local_90;
  long *local_88;
  long *local_80;
  void *pvStack_78;
  long *local_70;
  long *local_68;
  undefined1 local_60;
  long local_58;
  
  lVar3 = tpidr_el0;
  local_58 = *(long *)(lVar3 + 0x28);
  lVar8 = param_1[1] - *param_1 >> 3;
  uVar1 = lVar8 * -0x5555555555555555 + 1;
  if (uVar1 < 0xaaaaaaaaaaaaaab) {
    local_70 = param_1 + 2;
    lVar10 = *local_70 - *param_1 >> 3;
    uVar11 = lVar10 * 0x5555555555555556;
    if (uVar11 < uVar1 || uVar11 - uVar1 == 0) {
      uVar11 = uVar1;
    }
    if (0x555555555555554 < (ulong)(lVar10 * -0x5555555555555555)) {
      uVar11 = 0xaaaaaaaaaaaaaaa;
    }
    if (uVar11 == 0) {
      local_90 = (void *)0x0;
    }
    else {
      if (0xaaaaaaaaaaaaaaa < uVar11) goto LAB_00acb2c0;
      local_90 = (void *)_Znwm(uVar11 * 0x18);
    }
    local_60 = 0;
    plVar12 = (long *)((long)local_90 + lVar8 * 8);
    pvStack_78 = (void *)((long)local_90 + uVar11 * 0x18);
    lVar8 = *param_2;
    lVar10 = param_2[1];
    lVar2 = lVar10 - lVar8;
    *plVar12 = 0;
    plVar12[1] = 0;
    plVar12[2] = 0;
    local_80 = plVar12;
    local_88 = plVar12;
    local_68 = plVar12;
    if (lVar2 != 0) {
      if (0xaaaaaaaaaaaaaaa < (ulong)((lVar2 >> 3) * -0x5555555555555555)) {
        if (*(long *)(lVar3 + 0x28) == local_58) {
          uVar7 = FUN_005f064c(plVar12);
          plVar12[1] = 0xaaaaaaaaaaaaaaa;
          FUN_0062c99c(&local_68);
          FUN_00acb44c(&local_90);
          if (*(long *)(lVar3 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
            FUN_00bd6fec(uVar7);
          }
        }
        goto LAB_00acb32c;
      }
      lVar5 = _Znwm(lVar2);
      *plVar12 = lVar5;
      plVar12[1] = lVar5;
      plVar12[2] = lVar5 + lVar2;
      lVar8 = FUN_0062ca28(plVar12 + 2,lVar8,lVar10,lVar5);
      plVar12[1] = lVar8;
    }
    local_80 = local_80 + 3;
    FUN_00acb330(param_1,&local_90);
    plVar12 = local_88;
    lVar8 = param_1[1];
    while (plVar4 = local_80, plVar4 != plVar12) {
      plVar13 = plVar4 + -3;
      puVar14 = (undefined8 *)*plVar13;
      local_80 = plVar13;
      if (puVar14 != (undefined8 *)0x0) {
        puVar9 = (undefined8 *)plVar4[-2];
        puVar6 = puVar14;
        if (puVar9 != puVar14) {
          do {
            puVar6 = puVar9 + -3;
            __ptr = (void *)*puVar6;
            if (__ptr != (void *)0x0) {
              puVar9[-2] = __ptr;
              _ZdlPv(__ptr);
            }
            puVar9 = puVar6;
          } while (puVar6 != puVar14);
          puVar6 = (undefined8 *)*plVar13;
        }
        plVar4[-2] = (long)puVar14;
        _ZdlPv(puVar6);
      }
    }
    local_80 = plVar4;
    if (local_90 != (void *)0x0) {
      _ZdlPv(local_90);
    }
    if (*(long *)(lVar3 + 0x28) == local_58) {
      return lVar8;
    }
  }
  else {
    if (*(long *)(lVar3 + 0x28) != local_58) goto LAB_00acb32c;
    FUN_00acb508(param_1);
LAB_00acb2c0:
    if (*(long *)(lVar3 + 0x28) == local_58) {
                    /* WARNING: Subroutine does not return */
      FUN_0041e380();
    }
  }
LAB_00acb32c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acb0ac"></a> `00acb0ac` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00acb0b0"></a> `00acb0b0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acb0b4"></a> `00acb0b4` | `fa 67 05 a9` | stp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acb0b8"></a> `00acb0b8` | `f8 5f 06 a9` | stp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acb0bc"></a> `00acb0bc` | `f6 57 07 a9` | stp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acb0c0"></a> `00acb0c0` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acb0c4"></a> `00acb0c4` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00acb0c8"></a> `00acb0c8` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acb0cc"></a> `00acb0cc` | `ea f3 01 b2` | orr x10,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00acb0d0"></a> `00acb0d0` | `f9 f3 01 b2` | orr x25,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00acb0d4"></a> `00acb0d4` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00acb0d8"></a> `00acb0d8` | `6a 55 95 f2` | movk x10,#0xaaab | `FALL_THROUGH`
<a id="insn-00acb0dc"></a> `00acb0dc` | `59 55 e1 f2` | movk x25,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00acb0e0"></a> `00acb0e0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acb0e4"></a> `00acb0e4` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acb0e8"></a> `00acb0e8` | `09 20 40 a9` | ldp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00acb0ec"></a> `00acb0ec` | `08 01 09 cb` | sub x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00acb0f0"></a> `00acb0f0` | `08 fd 43 93` | asr x8,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00acb0f4"></a> `00acb0f4` | `14 7d 0a 9b` | mul x20,x8,x10 | `FALL_THROUGH`
<a id="insn-00acb0f8"></a> `00acb0f8` | `88 06 00 91` | add x8,x20,#0x1 | `FALL_THROUGH`
<a id="insn-00acb0fc"></a> `00acb0fc` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00acb100"></a> `00acb100` | `48 0d 00 54` | b.hi 0x00acb2a8 | `CONDITIONAL_JUMP`
<a id="insn-00acb104"></a> `00acb104` | `eb 03 13 aa` | mov x11,x19 | `FALL_THROUGH`
<a id="insn-00acb108"></a> `00acb108` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00acb10c"></a> `00acb10c` | `6c 0d 41 f8` | ldr x12,[x11, #0x10]! | `FALL_THROUGH`
<a id="insn-00acb110"></a> `00acb110` | `eb 13 00 f9` | str x11,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acb114"></a> `00acb114` | `89 01 09 cb` | sub x9,x12,x9 | `FALL_THROUGH`
<a id="insn-00acb118"></a> `00acb118` | `ec f3 00 b2` | orr x12,xzr,#0x5555555555555555 | `FALL_THROUGH`
<a id="insn-00acb11c"></a> `00acb11c` | `29 fd 43 93` | asr x9,x9,#0x3 | `FALL_THROUGH`
<a id="insn-00acb120"></a> `00acb120` | `ac aa e0 f2` | movk x12,#0x555, LSL #48 | `FALL_THROUGH`
<a id="insn-00acb124"></a> `00acb124` | `29 7d 0a 9b` | mul x9,x9,x10 | `FALL_THROUGH`
<a id="insn-00acb128"></a> `00acb128` | `2a f9 7f d3` | lsl x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00acb12c"></a> `00acb12c` | `5f 01 08 eb` | cmp x10,x8 | `FALL_THROUGH`
<a id="insn-00acb130"></a> `00acb130` | `48 81 88 9a` | csel x8,x10,x8,hi | `FALL_THROUGH`
<a id="insn-00acb134"></a> `00acb134` | `3f 01 0c eb` | cmp x9,x12 | `FALL_THROUGH`
<a id="insn-00acb138"></a> `00acb138` | `16 31 99 9a` | csel x22,x8,x25,cc | `FALL_THROUGH`
<a id="insn-00acb13c"></a> `00acb13c` | `f6 00 00 b4` | cbz x22,0x00acb158 | `CONDITIONAL_JUMP`
<a id="insn-00acb140"></a> `00acb140` | `df 02 19 eb` | cmp x22,x25 | `FALL_THROUGH`
<a id="insn-00acb144"></a> `00acb144` | `e8 0b 00 54` | b.hi 0x00acb2c0 | `CONDITIONAL_JUMP`
<a id="insn-00acb148"></a> `00acb148` | `c8 06 16 8b` | add x8,x22,x22, LSL #0x1 | `FALL_THROUGH`
<a id="insn-00acb14c"></a> `00acb14c` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00acb150"></a> `00acb150` | `7c 3f 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00acb154"></a> `00acb154` | `02 00 00 14` | b 0x00acb15c | `UNCONDITIONAL_JUMP`
<a id="insn-00acb158"></a> `00acb158` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00acb15c"></a> `00acb15c` | `08 03 80 52` | mov w8,#0x18 | `FALL_THROUGH`
<a id="insn-00acb160"></a> `00acb160` | `bf 03 1f 38` | sturb wzr,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00acb164"></a> `00acb164` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00acb168"></a> `00acb168` | `94 02 08 9b` | madd x20,x20,x8,x0 | `FALL_THROUGH`
<a id="insn-00acb16c"></a> `00acb16c` | `c8 02 08 9b` | madd x8,x22,x8,x0 | `FALL_THROUGH`
<a id="insn-00acb170"></a> `00acb170` | `b6 56 40 a9` | ldp x22,x21,[x21] | `FALL_THROUGH`
<a id="insn-00acb174"></a> `00acb174` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-00acb178"></a> `00acb178` | `b8 02 16 eb` | subs x24,x21,x22 | `FALL_THROUGH`
<a id="insn-00acb17c"></a> `00acb17c` | `e0 53 00 a9` | stp x0,x20,[sp] | `FALL_THROUGH`
<a id="insn-00acb180"></a> `00acb180` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00acb184"></a> `00acb184` | `f4 23 01 a9` | stp x20,x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb188"></a> `00acb188` | `b4 83 1e f8` | stur x20,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00acb18c"></a> `00acb18c` | `ff 0e 01 f8` | str xzr,[x23, #0x10]! | `FALL_THROUGH`
<a id="insn-00acb190"></a> `00acb190` | `80 02 00 54` | b.eq 0x00acb1e0 | `CONDITIONAL_JUMP`
<a id="insn-00acb194"></a> `00acb194` | `08 ff 43 93` | asr x8,x24,#0x3 | `FALL_THROUGH`
<a id="insn-00acb198"></a> `00acb198` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00acb19c"></a> `00acb19c` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00acb1a0"></a> `00acb1a0` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00acb1a4"></a> `00acb1a4` | `1f 01 19 eb` | cmp x8,x25 | `FALL_THROUGH`
<a id="insn-00acb1a8"></a> `00acb1a8` | `68 09 00 54` | b.hi 0x00acb2d4 | `CONDITIONAL_JUMP`
<a id="insn-00acb1ac"></a> `00acb1ac` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00acb1b0"></a> `00acb1b0` | `64 3f 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00acb1b4"></a> `00acb1b4` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00acb1b8"></a> `00acb1b8` | `08 00 18 8b` | add x8,x0,x24 | `FALL_THROUGH`
<a id="insn-00acb1bc"></a> `00acb1bc` | `80 02 00 a9` | stp x0,x0,[x20] | `FALL_THROUGH`
<a id="insn-00acb1c0"></a> `00acb1c0` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00acb1c4"></a> `00acb1c4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00acb1c8"></a> `00acb1c8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00acb1cc"></a> `00acb1cc` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00acb1d0"></a> `00acb1d0` | `e3 03 19 aa` | mov x3,x25 | `FALL_THROUGH`
<a id="insn-00acb1d4"></a> `00acb1d4` | `15 86 ed 97` | bl 0x0062ca28 | `UNCONDITIONAL_CALL`
<a id="insn-00acb1d8"></a> `00acb1d8` | `80 06 00 f9` | str x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00acb1dc"></a> `00acb1dc` | `f4 0b 40 f9` | ldr x20,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb1e0"></a> `00acb1e0` | `88 62 00 91` | add x8,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00acb1e4"></a> `00acb1e4` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb1e8"></a> `00acb1e8` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00acb1ec"></a> `00acb1ec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb1f0"></a> `00acb1f0` | `50 00 00 94` | bl 0x00acb330 | `UNCONDITIONAL_CALL`
<a id="insn-00acb1f4"></a> `00acb1f4` | `f4 d7 40 a9` | ldp x20,x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00acb1f8"></a> `00acb1f8` | `73 06 40 f9` | ldr x19,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00acb1fc"></a> `00acb1fc` | `bf 02 14 eb` | cmp x21,x20 | `FALL_THROUGH`
<a id="insn-00acb200"></a> `00acb200` | `60 03 00 54` | b.eq 0x00acb26c | `CONDITIONAL_JUMP`
<a id="insn-00acb204"></a> `00acb204` | `f6 03 15 aa` | mov x22,x21 | `FALL_THROUGH`
<a id="insn-00acb208"></a> `00acb208` | `08 00 00 14` | b 0x00acb228 | `UNCONDITIONAL_JUMP`
<a id="insn-00acb20c"></a> `00acb20c` | `c0 02 40 f9` | ldr x0,[x22] | `FALL_THROUGH`
<a id="insn-00acb210"></a> `00acb210` | `b7 02 1f f8` | stur x23,[x21, #-0x10] | `FALL_THROUGH`
<a id="insn-00acb214"></a> `00acb214` | `53 3f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acb218"></a> `00acb218` | `f6 0b 40 f9` | ldr x22,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb21c"></a> `00acb21c` | `df 02 14 eb` | cmp x22,x20 | `FALL_THROUGH`
<a id="insn-00acb220"></a> `00acb220` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00acb224"></a> `00acb224` | `40 02 00 54` | b.eq 0x00acb26c | `CONDITIONAL_JUMP`
<a id="insn-00acb228"></a> `00acb228` | `d7 8e 5e f8` | ldr x23,[x22, #-0x18]! | `FALL_THROUGH`
<a id="insn-00acb22c"></a> `00acb22c` | `f6 0b 00 f9` | str x22,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acb230"></a> `00acb230` | `77 ff ff b4` | cbz x23,0x00acb21c | `CONDITIONAL_JUMP`
<a id="insn-00acb234"></a> `00acb234` | `a8 02 5f f8` | ldur x8,[x21, #-0x10] | `FALL_THROUGH`
<a id="insn-00acb238"></a> `00acb238` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00acb23c"></a> `00acb23c` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00acb240"></a> `00acb240` | `80 fe ff 54` | b.eq 0x00acb210 | `CONDITIONAL_JUMP`
<a id="insn-00acb244"></a> `00acb244` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00acb248"></a> `00acb248` | `04 00 00 14` | b 0x00acb258 | `UNCONDITIONAL_JUMP`
<a id="insn-00acb24c"></a> `00acb24c` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00acb250"></a> `00acb250` | `e8 03 18 aa` | mov x8,x24 | `FALL_THROUGH`
<a id="insn-00acb254"></a> `00acb254` | `c0 fd ff 54` | b.eq 0x00acb20c | `CONDITIONAL_JUMP`
<a id="insn-00acb258"></a> `00acb258` | `00 8f 5e f8` | ldr x0,[x24, #-0x18]! | `FALL_THROUGH`
<a id="insn-00acb25c"></a> `00acb25c` | `80 ff ff b4` | cbz x0,0x00acb24c | `CONDITIONAL_JUMP`
<a id="insn-00acb260"></a> `00acb260` | `00 01 1f f8` | stur x0,[x8, #-0x10] | `FALL_THROUGH`
<a id="insn-00acb264"></a> `00acb264` | `3f 3f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acb268"></a> `00acb268` | `f9 ff ff 17` | b 0x00acb24c | `UNCONDITIONAL_JUMP`
<a id="insn-00acb26c"></a> `00acb26c` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00acb270"></a> `00acb270` | `40 00 00 b4` | cbz x0,0x00acb278 | `CONDITIONAL_JUMP`
<a id="insn-00acb274"></a> `00acb274` | `3b 3f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00acb278"></a> `00acb278` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00acb27c"></a> `00acb27c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acb280"></a> `00acb280` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acb284"></a> `00acb284` | `41 05 00 54` | b.ne 0x00acb32c | `CONDITIONAL_JUMP`
<a id="insn-00acb288"></a> `00acb288` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb28c"></a> `00acb28c` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00acb290"></a> `00acb290` | `f6 57 47 a9` | ldp x22,x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00acb294"></a> `00acb294` | `f8 5f 46 a9` | ldp x24,x23,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acb298"></a> `00acb298` | `fa 67 45 a9` | ldp x26,x25,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acb29c"></a> `00acb29c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acb2a0"></a> `00acb2a0` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00acb2a4"></a> `00acb2a4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acb2a8"></a> `00acb2a8` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00acb2ac"></a> `00acb2ac` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acb2b0"></a> `00acb2b0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acb2b4"></a> `00acb2b4` | `c1 03 00 54` | b.ne 0x00acb32c | `CONDITIONAL_JUMP`
<a id="insn-00acb2b8"></a> `00acb2b8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb2bc"></a> `00acb2bc` | `93 00 00 94` | bl 0x00acb508 | `UNCONDITIONAL_CALL`
<a id="insn-00acb2c0"></a> `00acb2c0` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00acb2c4"></a> `00acb2c4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acb2c8"></a> `00acb2c8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acb2cc"></a> `00acb2cc` | `01 03 00 54` | b.ne 0x00acb32c | `CONDITIONAL_JUMP`
<a id="insn-00acb2d0"></a> `00acb2d0` | `2c 4c e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-00acb2d4"></a> `00acb2d4` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00acb2d8"></a> `00acb2d8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acb2dc"></a> `00acb2dc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acb2e0"></a> `00acb2e0` | `61 02 00 54` | b.ne 0x00acb32c | `CONDITIONAL_JUMP`
<a id="insn-00acb2e4"></a> `00acb2e4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb2e8"></a> `00acb2e8` | `d9 94 ec 97` | bl 0x005f064c | `UNCONDITIONAL_CALL`
<a id="insn-00acb2ec"></a> `00acb2ec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acb2f0"></a> `00acb2f0` | `99 06 00 f9` | str x25,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00acb2f4"></a> `00acb2f4` | `04 00 00 14` | b 0x00acb304 | `UNCONDITIONAL_JUMP`
<a id="insn-00acb304"></a> `00acb304` | `a0 63 00 d1` | sub x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00acb308"></a> `00acb308` | `a5 85 ed 97` | bl 0x0062c99c | `UNCONDITIONAL_CALL`
<a id="insn-00acb30c"></a> `00acb30c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00acb310"></a> `00acb310` | `4f 00 00 94` | bl 0x00acb44c | `UNCONDITIONAL_CALL`
<a id="insn-00acb314"></a> `00acb314` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00acb318"></a> `00acb318` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acb31c"></a> `00acb31c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acb320"></a> `00acb320` | `61 00 00 54` | b.ne 0x00acb32c | `CONDITIONAL_JUMP`
<a id="insn-00acb324"></a> `00acb324` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00acb328"></a> `00acb328` | `31 2f 04 94` | bl 0x00bd6fec | `CALL_TERMINATOR`
<a id="insn-00acb32c"></a> `00acb32c` | `19 3f 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acb0ac`](#insn-00acb0ac) 範囲 `[['00acb0ac', '00acb103']]`
  - `CONDITIONAL_JUMP` [`00acb100`](#insn-00acb100) → [`00acb2a8`](#insn-00acb2a8)
  - `FALL_THROUGH` [`00acb100`](#insn-00acb100) → [`00acb104`](#insn-00acb104)
- ブロック [`00acb104`](#insn-00acb104) 範囲 `[['00acb104', '00acb13f']]`
  - `CONDITIONAL_JUMP` [`00acb13c`](#insn-00acb13c) → [`00acb158`](#insn-00acb158)
  - `FALL_THROUGH` [`00acb13c`](#insn-00acb13c) → [`00acb140`](#insn-00acb140)
- ブロック [`00acb140`](#insn-00acb140) 範囲 `[['00acb140', '00acb147']]`
  - `CONDITIONAL_JUMP` [`00acb144`](#insn-00acb144) → [`00acb2c0`](#insn-00acb2c0)
  - `FALL_THROUGH` [`00acb144`](#insn-00acb144) → [`00acb148`](#insn-00acb148)
- ブロック [`00acb148`](#insn-00acb148) 範囲 `[['00acb148', '00acb157']]`
  - `UNCONDITIONAL_JUMP` [`00acb154`](#insn-00acb154) → [`00acb15c`](#insn-00acb15c)
- ブロック [`00acb158`](#insn-00acb158) 範囲 `[['00acb158', '00acb15b']]`
  - `FALL_THROUGH` [`00acb158`](#insn-00acb158) → [`00acb15c`](#insn-00acb15c)
- ブロック [`00acb15c`](#insn-00acb15c) 範囲 `[['00acb15c', '00acb193']]`
  - `CONDITIONAL_JUMP` [`00acb190`](#insn-00acb190) → [`00acb1e0`](#insn-00acb1e0)
  - `FALL_THROUGH` [`00acb190`](#insn-00acb190) → [`00acb194`](#insn-00acb194)
- ブロック [`00acb194`](#insn-00acb194) 範囲 `[['00acb194', '00acb1ab']]`
  - `CONDITIONAL_JUMP` [`00acb1a8`](#insn-00acb1a8) → [`00acb2d4`](#insn-00acb2d4)
  - `FALL_THROUGH` [`00acb1a8`](#insn-00acb1a8) → [`00acb1ac`](#insn-00acb1ac)
- ブロック [`00acb1ac`](#insn-00acb1ac) 範囲 `[['00acb1ac', '00acb1df']]`
  - `FALL_THROUGH` [`00acb1dc`](#insn-00acb1dc) → [`00acb1e0`](#insn-00acb1e0)
- ブロック [`00acb1e0`](#insn-00acb1e0) 範囲 `[['00acb1e0', '00acb203']]`
  - `CONDITIONAL_JUMP` [`00acb200`](#insn-00acb200) → [`00acb26c`](#insn-00acb26c)
  - `FALL_THROUGH` [`00acb200`](#insn-00acb200) → [`00acb204`](#insn-00acb204)
- ブロック [`00acb204`](#insn-00acb204) 範囲 `[['00acb204', '00acb20b']]`
  - `UNCONDITIONAL_JUMP` [`00acb208`](#insn-00acb208) → [`00acb228`](#insn-00acb228)
- ブロック [`00acb20c`](#insn-00acb20c) 範囲 `[['00acb20c', '00acb20f']]`
  - `FALL_THROUGH` [`00acb20c`](#insn-00acb20c) → [`00acb210`](#insn-00acb210)
- ブロック [`00acb210`](#insn-00acb210) 範囲 `[['00acb210', '00acb21b']]`
  - `FALL_THROUGH` [`00acb218`](#insn-00acb218) → [`00acb21c`](#insn-00acb21c)
- ブロック [`00acb21c`](#insn-00acb21c) 範囲 `[['00acb21c', '00acb227']]`
  - `CONDITIONAL_JUMP` [`00acb224`](#insn-00acb224) → [`00acb26c`](#insn-00acb26c)
  - `FALL_THROUGH` [`00acb224`](#insn-00acb224) → [`00acb228`](#insn-00acb228)
- ブロック [`00acb228`](#insn-00acb228) 範囲 `[['00acb228', '00acb233']]`
  - `CONDITIONAL_JUMP` [`00acb230`](#insn-00acb230) → [`00acb21c`](#insn-00acb21c)
  - `FALL_THROUGH` [`00acb230`](#insn-00acb230) → [`00acb234`](#insn-00acb234)
- ブロック [`00acb234`](#insn-00acb234) 範囲 `[['00acb234', '00acb243']]`
  - `CONDITIONAL_JUMP` [`00acb240`](#insn-00acb240) → [`00acb210`](#insn-00acb210)
  - `FALL_THROUGH` [`00acb240`](#insn-00acb240) → [`00acb244`](#insn-00acb244)
- ブロック [`00acb244`](#insn-00acb244) 範囲 `[['00acb244', '00acb24b']]`
  - `UNCONDITIONAL_JUMP` [`00acb248`](#insn-00acb248) → [`00acb258`](#insn-00acb258)
- ブロック [`00acb24c`](#insn-00acb24c) 範囲 `[['00acb24c', '00acb257']]`
  - `CONDITIONAL_JUMP` [`00acb254`](#insn-00acb254) → [`00acb20c`](#insn-00acb20c)
  - `FALL_THROUGH` [`00acb254`](#insn-00acb254) → [`00acb258`](#insn-00acb258)
- ブロック [`00acb258`](#insn-00acb258) 範囲 `[['00acb258', '00acb25f']]`
  - `CONDITIONAL_JUMP` [`00acb25c`](#insn-00acb25c) → [`00acb24c`](#insn-00acb24c)
  - `FALL_THROUGH` [`00acb25c`](#insn-00acb25c) → [`00acb260`](#insn-00acb260)
- ブロック [`00acb260`](#insn-00acb260) 範囲 `[['00acb260', '00acb26b']]`
  - `UNCONDITIONAL_JUMP` [`00acb268`](#insn-00acb268) → [`00acb24c`](#insn-00acb24c)
- ブロック [`00acb26c`](#insn-00acb26c) 範囲 `[['00acb26c', '00acb273']]`
  - `CONDITIONAL_JUMP` [`00acb270`](#insn-00acb270) → [`00acb278`](#insn-00acb278)
  - `FALL_THROUGH` [`00acb270`](#insn-00acb270) → [`00acb274`](#insn-00acb274)
- ブロック [`00acb274`](#insn-00acb274) 範囲 `[['00acb274', '00acb277']]`
  - `FALL_THROUGH` [`00acb274`](#insn-00acb274) → [`00acb278`](#insn-00acb278)
- ブロック [`00acb278`](#insn-00acb278) 範囲 `[['00acb278', '00acb287']]`
  - `CONDITIONAL_JUMP` [`00acb284`](#insn-00acb284) → [`00acb32c`](#insn-00acb32c)
  - `FALL_THROUGH` [`00acb284`](#insn-00acb284) → [`00acb288`](#insn-00acb288)
- ブロック [`00acb288`](#insn-00acb288) 範囲 `[['00acb288', '00acb2a7']]`
- ブロック [`00acb2a8`](#insn-00acb2a8) 範囲 `[['00acb2a8', '00acb2b7']]`
  - `CONDITIONAL_JUMP` [`00acb2b4`](#insn-00acb2b4) → [`00acb32c`](#insn-00acb32c)
  - `FALL_THROUGH` [`00acb2b4`](#insn-00acb2b4) → [`00acb2b8`](#insn-00acb2b8)
- ブロック [`00acb2b8`](#insn-00acb2b8) 範囲 `[['00acb2b8', '00acb2bf']]`
  - `FALL_THROUGH` [`00acb2bc`](#insn-00acb2bc) → [`00acb2c0`](#insn-00acb2c0)
- ブロック [`00acb2c0`](#insn-00acb2c0) 範囲 `[['00acb2c0', '00acb2cf']]`
  - `CONDITIONAL_JUMP` [`00acb2cc`](#insn-00acb2cc) → [`00acb32c`](#insn-00acb32c)
  - `FALL_THROUGH` [`00acb2cc`](#insn-00acb2cc) → [`00acb2d0`](#insn-00acb2d0)
- ブロック [`00acb2d0`](#insn-00acb2d0) 範囲 `[['00acb2d0', '00acb2d3']]`
- ブロック [`00acb2d4`](#insn-00acb2d4) 範囲 `[['00acb2d4', '00acb2e3']]`
  - `CONDITIONAL_JUMP` [`00acb2e0`](#insn-00acb2e0) → [`00acb32c`](#insn-00acb32c)
  - `FALL_THROUGH` [`00acb2e0`](#insn-00acb2e0) → [`00acb2e4`](#insn-00acb2e4)
- ブロック [`00acb2e4`](#insn-00acb2e4) 範囲 `[['00acb2e4', '00acb2f7']]`
  - `UNCONDITIONAL_JUMP` [`00acb2f4`](#insn-00acb2f4) → [`00acb304`](#insn-00acb304)
- ブロック [`00acb304`](#insn-00acb304) 範囲 `[['00acb304', '00acb323']]`
  - `CONDITIONAL_JUMP` [`00acb320`](#insn-00acb320) → [`00acb32c`](#insn-00acb32c)
  - `FALL_THROUGH` [`00acb320`](#insn-00acb320) → [`00acb324`](#insn-00acb324)
- ブロック [`00acb324`](#insn-00acb324) 範囲 `[['00acb324', '00acb32b']]`
- ブロック [`00acb32c`](#insn-00acb32c) 範囲 `[['00acb32c', '00acb32f']]`

## 命令位置別の参照

- [`00acb0b0`](#insn-00acb0b0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb0b4`](#insn-00acb0b4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb0b8`](#insn-00acb0b8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb0bc`](#insn-00acb0bc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb0c0`](#insn-00acb0c0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb0e4`](#insn-00acb0e4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb100`](#insn-00acb100) → [`00acb2a8`](#insn-00acb2a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb110`](#insn-00acb110) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb13c`](#insn-00acb13c) → [`00acb158`](#insn-00acb158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb144`](#insn-00acb144) → [`00acb2c0`](#insn-00acb2c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb150`](#insn-00acb150) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00acb154`](#insn-00acb154) → [`00acb15c`](#insn-00acb15c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb160`](#insn-00acb160) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb17c`](#insn-00acb17c) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb184`](#insn-00acb184) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb188`](#insn-00acb188) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb190`](#insn-00acb190) → [`00acb1e0`](#insn-00acb1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1a8`](#insn-00acb1a8) → [`00acb2d4`](#insn-00acb2d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1b0`](#insn-00acb1b0) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00acb1d4`](#insn-00acb1d4) → [`0062ca28`](../0062c/0062ca28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0062ca28` · 推定シンボル `None` · 推定型 `None`
- [`00acb1dc`](#insn-00acb1dc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1e4`](#insn-00acb1e4) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb1f0`](#insn-00acb1f0) → [`00acb330`](00acb330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acb330` · 推定シンボル `None` · 推定型 `None`
- [`00acb1f4`](#insn-00acb1f4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb200`](#insn-00acb200) → [`00acb26c`](#insn-00acb26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb208`](#insn-00acb208) → [`00acb228`](#insn-00acb228) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb214`](#insn-00acb214) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acb218`](#insn-00acb218) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb224`](#insn-00acb224) → [`00acb26c`](#insn-00acb26c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb22c`](#insn-00acb22c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb230`](#insn-00acb230) → [`00acb21c`](#insn-00acb21c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb240`](#insn-00acb240) → [`00acb210`](#insn-00acb210) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb248`](#insn-00acb248) → [`00acb258`](#insn-00acb258) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb254`](#insn-00acb254) → [`00acb20c`](#insn-00acb20c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb25c`](#insn-00acb25c) → [`00acb24c`](#insn-00acb24c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb264`](#insn-00acb264) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acb268`](#insn-00acb268) → [`00acb24c`](#insn-00acb24c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb26c`](#insn-00acb26c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb270`](#insn-00acb270) → [`00acb278`](#insn-00acb278) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb274`](#insn-00acb274) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00acb27c`](#insn-00acb27c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb284`](#insn-00acb284) → [`00acb32c`](#insn-00acb32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb28c`](#insn-00acb28c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb290`](#insn-00acb290) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb294`](#insn-00acb294) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb298`](#insn-00acb298) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb29c`](#insn-00acb29c) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2ac`](#insn-00acb2ac) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2b4`](#insn-00acb2b4) → [`00acb32c`](#insn-00acb32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2bc`](#insn-00acb2bc) → [`00acb508`](00acb508.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acb508` · 推定シンボル `None` · 推定型 `None`
- [`00acb2c4`](#insn-00acb2c4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2cc`](#insn-00acb2cc) → [`00acb32c`](#insn-00acb32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2d0`](#insn-00acb2d0) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`00acb2d8`](#insn-00acb2d8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2e0`](#insn-00acb2e0) → [`00acb32c`](#insn-00acb32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb2e8`](#insn-00acb2e8) → [`005f064c`](../005f0/005f064c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005f064c` · 推定シンボル `None` · 推定型 `None`
- [`00acb2f4`](#insn-00acb2f4) → [`00acb304`](#insn-00acb304) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb308`](#insn-00acb308) → [`0062c99c`](../0062c/0062c99c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0062c99c` · 推定シンボル `None` · 推定型 `None`
- [`00acb310`](#insn-00acb310) → [`00acb44c`](00acb44c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00acb44c` · 推定シンボル `None` · 推定型 `None`
- [`00acb318`](#insn-00acb318) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb320`](#insn-00acb320) → [`00acb32c`](#insn-00acb32c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb328`](#insn-00acb328) → [`00bd6fec`](../00bd6/00bd6fec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6fec` · 推定シンボル `None` · 推定型 `None`
- [`00acb32c`](#insn-00acb32c) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acb0b0`](#insn-00acb0b0)

~~~json
{
  "source": "00acb0b0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb0b4`](#insn-00acb0b4)

~~~json
{
  "source": "00acb0b4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb0b8`](#insn-00acb0b8)

~~~json
{
  "source": "00acb0b8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb0bc`](#insn-00acb0bc)

~~~json
{
  "source": "00acb0bc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb0c0`](#insn-00acb0c0)

~~~json
{
  "source": "00acb0c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb0e4`](#insn-00acb0e4)

~~~json
{
  "source": "00acb0e4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb100`](#insn-00acb100)

~~~json
{
  "source": "00acb100",
  "target": "00acb2a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb110`](#insn-00acb110)

~~~json
{
  "source": "00acb110",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb13c`](#insn-00acb13c)

~~~json
{
  "source": "00acb13c",
  "target": "00acb158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb144`](#insn-00acb144)

~~~json
{
  "source": "00acb144",
  "target": "00acb2c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb150`](#insn-00acb150)

~~~json
{
  "source": "00acb150",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb154`](#insn-00acb154)

~~~json
{
  "source": "00acb154",
  "target": "00acb15c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb160`](#insn-00acb160)

~~~json
{
  "source": "00acb160",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb17c`](#insn-00acb17c)

~~~json
{
  "source": "00acb17c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb184`](#insn-00acb184)

~~~json
{
  "source": "00acb184",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb188`](#insn-00acb188)

~~~json
{
  "source": "00acb188",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb190`](#insn-00acb190)

~~~json
{
  "source": "00acb190",
  "target": "00acb1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1a8`](#insn-00acb1a8)

~~~json
{
  "source": "00acb1a8",
  "target": "00acb2d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1b0`](#insn-00acb1b0)

~~~json
{
  "source": "00acb1b0",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb1d4`](#insn-00acb1d4)

~~~json
{
  "source": "00acb1d4",
  "target": "0062ca28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb1dc`](#insn-00acb1dc)

~~~json
{
  "source": "00acb1dc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1e4`](#insn-00acb1e4)

~~~json
{
  "source": "00acb1e4",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb1f0`](#insn-00acb1f0)

~~~json
{
  "source": "00acb1f0",
  "target": "00acb330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb1f4`](#insn-00acb1f4)

~~~json
{
  "source": "00acb1f4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb200`](#insn-00acb200)

~~~json
{
  "source": "00acb200",
  "target": "00acb26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb208`](#insn-00acb208)

~~~json
{
  "source": "00acb208",
  "target": "00acb228",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb214`](#insn-00acb214)

~~~json
{
  "source": "00acb214",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb218`](#insn-00acb218)

~~~json
{
  "source": "00acb218",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb224`](#insn-00acb224)

~~~json
{
  "source": "00acb224",
  "target": "00acb26c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb22c`](#insn-00acb22c)

~~~json
{
  "source": "00acb22c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb230`](#insn-00acb230)

~~~json
{
  "source": "00acb230",
  "target": "00acb21c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb240`](#insn-00acb240)

~~~json
{
  "source": "00acb240",
  "target": "00acb210",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb248`](#insn-00acb248)

~~~json
{
  "source": "00acb248",
  "target": "00acb258",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb254`](#insn-00acb254)

~~~json
{
  "source": "00acb254",
  "target": "00acb20c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb25c`](#insn-00acb25c)

~~~json
{
  "source": "00acb25c",
  "target": "00acb24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb264`](#insn-00acb264)

~~~json
{
  "source": "00acb264",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb268`](#insn-00acb268)

~~~json
{
  "source": "00acb268",
  "target": "00acb24c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb26c`](#insn-00acb26c)

~~~json
{
  "source": "00acb26c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb270`](#insn-00acb270)

~~~json
{
  "source": "00acb270",
  "target": "00acb278",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb274`](#insn-00acb274)

~~~json
{
  "source": "00acb274",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb27c`](#insn-00acb27c)

~~~json
{
  "source": "00acb27c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb284`](#insn-00acb284)

~~~json
{
  "source": "00acb284",
  "target": "00acb32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb28c`](#insn-00acb28c)

~~~json
{
  "source": "00acb28c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb290`](#insn-00acb290)

~~~json
{
  "source": "00acb290",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb294`](#insn-00acb294)

~~~json
{
  "source": "00acb294",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb298`](#insn-00acb298)

~~~json
{
  "source": "00acb298",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb29c`](#insn-00acb29c)

~~~json
{
  "source": "00acb29c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2ac`](#insn-00acb2ac)

~~~json
{
  "source": "00acb2ac",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2b4`](#insn-00acb2b4)

~~~json
{
  "source": "00acb2b4",
  "target": "00acb32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2bc`](#insn-00acb2bc)

~~~json
{
  "source": "00acb2bc",
  "target": "00acb508",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb2c4`](#insn-00acb2c4)

~~~json
{
  "source": "00acb2c4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2cc`](#insn-00acb2cc)

~~~json
{
  "source": "00acb2cc",
  "target": "00acb32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2d0`](#insn-00acb2d0)

~~~json
{
  "source": "00acb2d0",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb2d8`](#insn-00acb2d8)

~~~json
{
  "source": "00acb2d8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2e0`](#insn-00acb2e0)

~~~json
{
  "source": "00acb2e0",
  "target": "00acb32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb2e8`](#insn-00acb2e8)

~~~json
{
  "source": "00acb2e8",
  "target": "005f064c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb2f4`](#insn-00acb2f4)

~~~json
{
  "source": "00acb2f4",
  "target": "00acb304",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb308`](#insn-00acb308)

~~~json
{
  "source": "00acb308",
  "target": "0062c99c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb310`](#insn-00acb310)

~~~json
{
  "source": "00acb310",
  "target": "00acb44c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb318`](#insn-00acb318)

~~~json
{
  "source": "00acb318",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb320`](#insn-00acb320)

~~~json
{
  "source": "00acb320",
  "target": "00acb32c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb328`](#insn-00acb328)

~~~json
{
  "source": "00acb328",
  "target": "00bd6fec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acb32c`](#insn-00acb32c)

~~~json
{
  "source": "00acb32c",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
