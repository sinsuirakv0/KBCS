# 00a9edec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00a9ebf0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00a9e/00a9ebf0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0062.md#compare-f395c0f08ba0c6557a5fba2c1b0b896c)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00a9ee5c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00a9e/00a9ee5c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-42e73a35a42502ee5b820dad12154442)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00a9edec",
  "name": "FUN_00a9edec",
  "size": 856,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fa43ae8a97754eba4b4080e55f19a913f920dceae6fba7b7a9de9b8b08b308f3",
  "source_text_sha256": "fa43ae8a97754eba4b4080e55f19a913f920dceae6fba7b7a9de9b8b08b308f3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00a9edec",
        "00a9f13f"
      ],
      [
        "00a9f194",
        "00a9f197"
      ]
    ],
    "bytes_sha256": "4bc69eac960c11e689a7d8b0c26167addadcd9fa0db778cd07dc27c83246cea5",
    "instruction_count": 214,
    "instruction_bytes": 856,
    "body_bytes": 856,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00a9c6f0](../00a9c/00a9c6f0.md)

## 呼び出し先

- [00440ec0](../00440/00440ec0.md)
- [008001ec](../00800/008001ec.md)
- [00804074](../00804/00804074.md)
- [0080645c](../00806/0080645c.md)
- [00806614](../00806/00806614.md)
- [008514f8](../00851/008514f8.md)
- [00860588](../00860/00860588.md)
- [009a9760](../009a9/009a9760.md)
- [009a9770](../009a9/009a9770.md)
- [009ad980](../009ad/009ad980.md)
- [009b1e90](../009b1/009b1e90.md)
- [00a31b78](../00a31/00a31b78.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58000](../00c58/00c58000.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5534 bytes

~~~c

undefined4 FUN_00a9edec(undefined8 param_1,long *param_2,uint param_3)

{
  int iVar1;
  long lVar2;
  byte bVar3;
  undefined4 uVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  undefined8 *__dest;
  ulong uVar8;
  ulong uVar9;
  undefined8 *puVar10;
  undefined8 *puVar11;
  undefined8 uVar12;
  undefined8 *puVar13;
  size_t __n;
  undefined8 *local_98;
  undefined8 *local_90;
  undefined8 *local_88;
  undefined8 *local_80;
  undefined8 *local_78;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  lVar6 = FUN_008514f8();
  iVar5 = *(int *)(*param_2 + 0x20);
  iVar1 = *(int *)(*param_2 + 100);
  FUN_009ad980(&local_80,*(undefined8 *)(lVar6 + 0x2268));
  local_98 = (undefined8 *)0x0;
  local_90 = (undefined8 *)0x0;
  local_88 = (undefined8 *)0x0;
  puVar11 = local_80;
  if (local_80 == local_78) {
    uVar4 = 1;
    puVar11 = local_90;
  }
  else {
    do {
      uVar12 = *puVar11;
      uVar4 = FUN_009a9760(uVar12);
      uVar4 = FUN_008001ec(4,uVar4);
      if (iVar5 == 6) {
        lVar7 = FUN_00a31b78(lVar6 + 0x510,uVar4);
        puVar13 = local_98;
        if (lVar7 != 0) {
                    /* try { // try from 00a9eea8 to 00b9eeef has its CatchHandler @ 00aa134c */
          if (local_90 < local_88) goto LAB_00a9ee60;
          __n = (long)local_90 - (long)local_98;
          lVar7 = (long)__n >> 3;
          uVar8 = lVar7 + 1;
          if (uVar8 >> 0x3d != 0) {
LAB_00a9f10c:
            if (*(long *)(lVar2 + 0x28) == local_68) {
              FUN_009b1e90(&local_98);
              goto LAB_00a9f128;
            }
            goto LAB_00a9f194;
          }
          uVar9 = (long)local_88 - (long)local_98 >> 2;
          if (uVar9 <= uVar8) {
            uVar9 = uVar8;
          }
          if (0x7ffffffffffffff7 < (ulong)((long)local_88 - (long)local_98)) {
            uVar9 = 0x1fffffffffffffff;
          }
          if (uVar9 == 0) {
LAB_00a9ef6c:
            __dest = (undefined8 *)0x0;
            puVar13 = local_98;
          }
          else {
            if (uVar9 >> 0x3d != 0) goto LAB_00a9f128;
            __dest = (undefined8 *)_Znwm(uVar9 << 3);
          }
LAB_00a9ef70:
          puVar10 = __dest + lVar7 + 1;
          __dest[lVar7] = uVar12;
          memcpy(__dest,puVar13,__n);
          local_98 = __dest;
          local_90 = puVar10;
          local_88 = __dest + uVar9;
          if (puVar13 != (undefined8 *)0x0) {
            _ZdlPv(puVar13);
            local_90 = puVar10;
          }
        }
      }
      else {
                    /* try { // try from 00a9ef00 to 00b9f3a7 has its CatchHandler @ 00aa1348 */
        lVar7 = FUN_00a31b78(lVar6 + 0x510,uVar4);
        puVar13 = local_98;
        if (lVar7 == 0) {
          if (local_88 <= local_90) {
            __n = (long)local_90 - (long)local_98;
            lVar7 = (long)__n >> 3;
            uVar8 = lVar7 + 1;
            if (uVar8 >> 0x3d != 0) goto LAB_00a9f10c;
            uVar9 = (long)local_88 - (long)local_98 >> 2;
            if (uVar9 <= uVar8) {
              uVar9 = uVar8;
            }
            if (0x7ffffffffffffff7 < (ulong)((long)local_88 - (long)local_98)) {
              uVar9 = 0x1fffffffffffffff;
            }
            if (uVar9 == 0) goto LAB_00a9ef6c;
            if (uVar9 >> 0x3d == 0) {
              __dest = (undefined8 *)_Znwm(uVar9 << 3);
              goto LAB_00a9ef70;
            }
LAB_00a9f128:
            if (*(long *)(lVar2 + 0x28) == local_68) {
                    /* WARNING: Subroutine does not return */
              FUN_00440ec0();
            }
            goto LAB_00a9f194;
          }
LAB_00a9ee60:
          *local_90 = uVar12;
          local_90 = local_90 + 1;
        }
      }
      puVar13 = local_90;
      puVar11 = puVar11 + 1;
    } while (puVar11 != local_78);
    if (local_98 == local_90) {
      uVar4 = 1;
      puVar11 = local_90;
    }
    else {
      puVar11 = local_98;
      if (iVar1 == 1) {
        do {
          uVar12 = *puVar11;
          iVar5 = FUN_009a9770(uVar12);
          uVar4 = FUN_009a9760(uVar12);
          if ((param_3 & 1) == 0) {
            if (iVar5 - 1U < 2) goto LAB_00a9f048;
          }
          else {
            uVar8 = FUN_00804074(4,uVar4);
            if (((uVar8 & 1) != 0) && (uVar8 = FUN_00806614(4,uVar4), (uVar8 & 1) != 0)) {
              uVar4 = FUN_0080645c(4,uVar4);
              bVar3 = FUN_00860588(lVar6,uVar4);
              if ((iVar5 - 1U < 2 & bVar3) != 0) goto LAB_00a9f048;
            }
          }
          puVar11 = puVar11 + 1;
        } while (puVar11 != puVar13);
LAB_00a9f090:
        uVar4 = 1;
        puVar13 = local_98;
        puVar11 = local_90;
      }
      else {
        do {
          iVar5 = FUN_009a9770(*puVar11);
          if (iVar1 == 0) {
            if (iVar5 != 0) goto LAB_00a9f090;
          }
          else if (iVar1 == 2) {
            if (iVar5 != 3) goto LAB_00a9f090;
          }
          else if ((iVar1 == 3) && (iVar5 != 4)) goto LAB_00a9f090;
          puVar11 = puVar11 + 1;
        } while (puVar11 != puVar13);
LAB_00a9f048:
        uVar4 = 0;
        puVar13 = local_98;
        puVar11 = local_90;
      }
    }
    local_90 = puVar13;
    if (local_90 != (undefined8 *)0x0) {
      _ZdlPv(local_90);
      puVar11 = local_90;
    }
  }
  local_90 = puVar11;
  if (local_80 != (undefined8 *)0x0) {
    _ZdlPv(local_80);
  }
  if (*(long *)(lVar2 + 0x28) == local_68) {
    return uVar4;
  }
LAB_00a9f194:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00a9edec"></a> `00a9edec` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00a9edf0"></a> `00a9edf0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a9edf4"></a> `00a9edf4` | `fc 6f 06 a9` | stp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a9edf8"></a> `00a9edf8` | `fa 67 07 a9` | stp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a9edfc"></a> `00a9edfc` | `f8 5f 08 a9` | stp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a9ee00"></a> `00a9ee00` | `f6 57 09 a9` | stp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a9ee04"></a> `00a9ee04` | `f4 4f 0a a9` | stp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00a9ee08"></a> `00a9ee08` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00a9ee0c"></a> `00a9ee0c` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00a9ee10"></a> `00a9ee10` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00a9ee14"></a> `00a9ee14` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00a9ee18"></a> `00a9ee18` | `e8 0b 00 f9` | str x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9ee1c"></a> `00a9ee1c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00a9ee20"></a> `00a9ee20` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a9ee24"></a> `00a9ee24` | `b5 c9 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ee28"></a> `00a9ee28` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00a9ee2c"></a> `00a9ee2c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00a9ee30"></a> `00a9ee30` | `00 34 51 f9` | ldr x0,[x0, #0x2268] | `FALL_THROUGH`
<a id="insn-00a9ee34"></a> `00a9ee34` | `1c 21 40 b9` | ldr w28,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00a9ee38"></a> `00a9ee38` | `16 65 40 b9` | ldr w22,[x8, #0x64] | `FALL_THROUGH`
<a id="insn-00a9ee3c"></a> `00a9ee3c` | `a8 83 00 d1` | sub x8,x29,#0x20 | `FALL_THROUGH`
<a id="insn-00a9ee40"></a> `00a9ee40` | `d0 3a fc 97` | bl 0x009ad980 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ee44"></a> `00a9ee44` | `b5 6b 7e a9` | ldp x21,x26,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00a9ee48"></a> `00a9ee48` | `ff ff 01 a9` | stp xzr,xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a9ee4c"></a> `00a9ee4c` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00a9ee50"></a> `00a9ee50` | `bf 02 1a eb` | cmp x21,x26 | `FALL_THROUGH`
<a id="insn-00a9ee54"></a> `00a9ee54` | `00 15 00 54` | b.eq 0x00a9f0f4 | `CONDITIONAL_JUMP`
<a id="insn-00a9ee58"></a> `00a9ee58` | `f3 5b 01 29` | stp w19,w22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a9ee5c"></a> `00a9ee5c` | `06 00 00 14` | b 0x00a9ee74 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9ee60"></a> `00a9ee60` | `76 86 00 f8` | str x22,[x19], #0x8 | `FALL_THROUGH`
<a id="insn-00a9ee64"></a> `00a9ee64` | `f3 13 00 f9` | str x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9ee68"></a> `00a9ee68` | `b5 22 00 91` | add x21,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00a9ee6c"></a> `00a9ee6c` | `bf 02 1a eb` | cmp x21,x26 | `FALL_THROUGH`
<a id="insn-00a9ee70"></a> `00a9ee70` | `a0 09 00 54` | b.eq 0x00a9efa4 | `CONDITIONAL_JUMP`
<a id="insn-00a9ee74"></a> `00a9ee74` | `b6 02 40 f9` | ldr x22,[x21] | `FALL_THROUGH`
<a id="insn-00a9ee78"></a> `00a9ee78` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00a9ee7c"></a> `00a9ee7c` | `39 2a fc 97` | bl 0x009a9760 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ee80"></a> `00a9ee80` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00a9ee84"></a> `00a9ee84` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00a9ee88"></a> `00a9ee88` | `d9 84 f5 97` | bl 0x008001ec | `UNCONDITIONAL_CALL`
<a id="insn-00a9ee8c"></a> `00a9ee8c` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00a9ee90"></a> `00a9ee90` | `9f 1b 00 71` | cmp w28,#0x6 | `FALL_THROUGH`
<a id="insn-00a9ee94"></a> `00a9ee94` | `61 03 00 54` | b.ne 0x00a9ef00 | `CONDITIONAL_JUMP`
<a id="insn-00a9ee98"></a> `00a9ee98` | `80 42 14 91` | add x0,x20,#0x510 | `FALL_THROUGH`
<a id="insn-00a9ee9c"></a> `00a9ee9c` | `37 4b fe 97` | bl 0x00a31b78 | `UNCONDITIONAL_CALL`
<a id="insn-00a9eea0"></a> `00a9eea0` | `40 fe ff b4` | cbz x0,0x00a9ee68 | `CONDITIONAL_JUMP`
<a id="insn-00a9eea4"></a> `00a9eea4` | `f3 23 42 a9` | ldp x19,x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9eea8"></a> `00a9eea8` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00a9eeac"></a> `00a9eeac` | `a3 fd ff 54` | b.cc 0x00a9ee60 | `CONDITIONAL_JUMP`
<a id="insn-00a9eeb0"></a> `00a9eeb0` | `f7 0f 40 f9` | ldr x23,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a9eeb4"></a> `00a9eeb4` | `78 02 17 cb` | sub x24,x19,x23 | `FALL_THROUGH`
<a id="insn-00a9eeb8"></a> `00a9eeb8` | `13 ff 43 93` | asr x19,x24,#0x3 | `FALL_THROUGH`
<a id="insn-00a9eebc"></a> `00a9eebc` | `69 06 00 91` | add x9,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00a9eec0"></a> `00a9eec0` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-00a9eec4"></a> `00a9eec4` | `4a 12 00 b5` | cbnz x10,0x00a9f10c | `CONDITIONAL_JUMP`
<a id="insn-00a9eec8"></a> `00a9eec8` | `08 01 17 cb` | sub x8,x8,x23 | `FALL_THROUGH`
<a id="insn-00a9eecc"></a> `00a9eecc` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00a9eed0"></a> `00a9eed0` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00a9eed4"></a> `00a9eed4` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00a9eed8"></a> `00a9eed8` | `ea ef 7d b2` | orr x10,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00a9eedc"></a> `00a9eedc` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00a9eee0"></a> `00a9eee0` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00a9eee4"></a> `00a9eee4` | `3b 31 88 9a` | csel x27,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00a9eee8"></a> `00a9eee8` | `3b 04 00 b4` | cbz x27,0x00a9ef6c | `CONDITIONAL_JUMP`
<a id="insn-00a9eeec"></a> `00a9eeec` | `68 ff 7d d3` | lsr x8,x27,#0x3d | `FALL_THROUGH`
<a id="insn-00a9eef0"></a> `00a9eef0` | `c8 11 00 b5` | cbnz x8,0x00a9f128 | `CONDITIONAL_JUMP`
<a id="insn-00a9eef4"></a> `00a9eef4` | `60 f3 7d d3` | lsl x0,x27,#0x3 | `FALL_THROUGH`
<a id="insn-00a9eef8"></a> `00a9eef8` | `e6 e3 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00a9eefc"></a> `00a9eefc` | `1a 00 00 14` | b 0x00a9ef64 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9ef00"></a> `00a9ef00` | `80 42 14 91` | add x0,x20,#0x510 | `FALL_THROUGH`
<a id="insn-00a9ef04"></a> `00a9ef04` | `1d 4b fe 97` | bl 0x00a31b78 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ef08"></a> `00a9ef08` | `00 fb ff b5` | cbnz x0,0x00a9ee68 | `CONDITIONAL_JUMP`
<a id="insn-00a9ef0c"></a> `00a9ef0c` | `f3 23 42 a9` | ldp x19,x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9ef10"></a> `00a9ef10` | `7f 02 08 eb` | cmp x19,x8 | `FALL_THROUGH`
<a id="insn-00a9ef14"></a> `00a9ef14` | `63 fa ff 54` | b.cc 0x00a9ee60 | `CONDITIONAL_JUMP`
<a id="insn-00a9ef18"></a> `00a9ef18` | `f7 0f 40 f9` | ldr x23,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a9ef1c"></a> `00a9ef1c` | `78 02 17 cb` | sub x24,x19,x23 | `FALL_THROUGH`
<a id="insn-00a9ef20"></a> `00a9ef20` | `13 ff 43 93` | asr x19,x24,#0x3 | `FALL_THROUGH`
<a id="insn-00a9ef24"></a> `00a9ef24` | `69 06 00 91` | add x9,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00a9ef28"></a> `00a9ef28` | `2a fd 7d d3` | lsr x10,x9,#0x3d | `FALL_THROUGH`
<a id="insn-00a9ef2c"></a> `00a9ef2c` | `0a 0f 00 b5` | cbnz x10,0x00a9f10c | `CONDITIONAL_JUMP`
<a id="insn-00a9ef30"></a> `00a9ef30` | `08 01 17 cb` | sub x8,x8,x23 | `FALL_THROUGH`
<a id="insn-00a9ef34"></a> `00a9ef34` | `0a fd 42 93` | asr x10,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00a9ef38"></a> `00a9ef38` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00a9ef3c"></a> `00a9ef3c` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00a9ef40"></a> `00a9ef40` | `ea ef 7d b2` | orr x10,xzr,#0x7ffffffffffffff8 | `FALL_THROUGH`
<a id="insn-00a9ef44"></a> `00a9ef44` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00a9ef48"></a> `00a9ef48` | `08 00 fc 92` | mov x8,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00a9ef4c"></a> `00a9ef4c` | `3b 31 88 9a` | csel x27,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00a9ef50"></a> `00a9ef50` | `fb 00 00 b4` | cbz x27,0x00a9ef6c | `CONDITIONAL_JUMP`
<a id="insn-00a9ef54"></a> `00a9ef54` | `68 ff 7d d3` | lsr x8,x27,#0x3d | `FALL_THROUGH`
<a id="insn-00a9ef58"></a> `00a9ef58` | `88 0e 00 b5` | cbnz x8,0x00a9f128 | `CONDITIONAL_JUMP`
<a id="insn-00a9ef5c"></a> `00a9ef5c` | `60 f3 7d d3` | lsl x0,x27,#0x3 | `FALL_THROUGH`
<a id="insn-00a9ef60"></a> `00a9ef60` | `cc e3 06 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ef64"></a> `00a9ef64` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00a9ef68"></a> `00a9ef68` | `02 00 00 14` | b 0x00a9ef70 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9ef6c"></a> `00a9ef6c` | `f9 03 1f aa` | mov x25,xzr | `FALL_THROUGH`
<a id="insn-00a9ef70"></a> `00a9ef70` | `33 0f 13 8b` | add x19,x25,x19, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00a9ef74"></a> `00a9ef74` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00a9ef78"></a> `00a9ef78` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00a9ef7c"></a> `00a9ef7c` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00a9ef80"></a> `00a9ef80` | `3b 0f 1b 8b` | add x27,x25,x27, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00a9ef84"></a> `00a9ef84` | `76 86 00 f8` | str x22,[x19], #0x8 | `FALL_THROUGH`
<a id="insn-00a9ef88"></a> `00a9ef88` | `1e e4 06 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00a9ef8c"></a> `00a9ef8c` | `f9 cf 01 a9` | stp x25,x19,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a9ef90"></a> `00a9ef90` | `fb 17 00 f9` | str x27,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00a9ef94"></a> `00a9ef94` | `97 f6 ff b4` | cbz x23,0x00a9ee64 | `CONDITIONAL_JUMP`
<a id="insn-00a9ef98"></a> `00a9ef98` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00a9ef9c"></a> `00a9ef9c` | `c5 e3 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00a9efa0"></a> `00a9efa0` | `b1 ff ff 17` | b 0x00a9ee64 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9efa4"></a> `00a9efa4` | `f8 d7 41 a9` | ldp x24,x21,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a9efa8"></a> `00a9efa8` | `1f 03 15 eb` | cmp x24,x21 | `FALL_THROUGH`
<a id="insn-00a9efac"></a> `00a9efac` | `a0 0a 00 54` | b.eq 0x00a9f100 | `CONDITIONAL_JUMP`
<a id="insn-00a9efb0"></a> `00a9efb0` | `f3 0f 40 b9` | ldr w19,[sp, #0xc] | `FALL_THROUGH`
<a id="insn-00a9efb4"></a> `00a9efb4` | `7f 06 00 71` | cmp w19,#0x1 | `FALL_THROUGH`
<a id="insn-00a9efb8"></a> `00a9efb8` | `61 05 00 54` | b.ne 0x00a9f064 | `CONDITIONAL_JUMP`
<a id="insn-00a9efbc"></a> `00a9efbc` | `f3 0b 40 b9` | ldr w19,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00a9efc0"></a> `00a9efc0` | `07 00 00 14` | b 0x00a9efdc | `UNCONDITIONAL_JUMP`
<a id="insn-00a9efc4"></a> `00a9efc4` | `c8 06 00 51` | sub w8,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00a9efc8"></a> `00a9efc8` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00a9efcc"></a> `00a9efcc` | `e3 03 00 54` | b.cc 0x00a9f048 | `CONDITIONAL_JUMP`
<a id="insn-00a9efd0"></a> `00a9efd0` | `18 23 00 91` | add x24,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00a9efd4"></a> `00a9efd4` | `1f 03 15 eb` | cmp x24,x21 | `FALL_THROUGH`
<a id="insn-00a9efd8"></a> `00a9efd8` | `c0 05 00 54` | b.eq 0x00a9f090 | `CONDITIONAL_JUMP`
<a id="insn-00a9efdc"></a> `00a9efdc` | `17 03 40 f9` | ldr x23,[x24] | `FALL_THROUGH`
<a id="insn-00a9efe0"></a> `00a9efe0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00a9efe4"></a> `00a9efe4` | `e3 29 fc 97` | bl 0x009a9770 | `UNCONDITIONAL_CALL`
<a id="insn-00a9efe8"></a> `00a9efe8` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00a9efec"></a> `00a9efec` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00a9eff0"></a> `00a9eff0` | `dc 29 fc 97` | bl 0x009a9760 | `UNCONDITIONAL_CALL`
<a id="insn-00a9eff4"></a> `00a9eff4` | `93 fe 07 36` | tbz w19,#0x0,0x00a9efc4 | `CONDITIONAL_JUMP`
<a id="insn-00a9eff8"></a> `00a9eff8` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00a9effc"></a> `00a9effc` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00a9f000"></a> `00a9f000` | `e1 03 17 2a` | mov w1,w23 | `FALL_THROUGH`
<a id="insn-00a9f004"></a> `00a9f004` | `1c 94 f5 97` | bl 0x00804074 | `UNCONDITIONAL_CALL`
<a id="insn-00a9f008"></a> `00a9f008` | `40 fe 07 36` | tbz w0,#0x0,0x00a9efd0 | `CONDITIONAL_JUMP`
<a id="insn-00a9f00c"></a> `00a9f00c` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00a9f010"></a> `00a9f010` | `e1 03 17 2a` | mov w1,w23 | `FALL_THROUGH`
<a id="insn-00a9f014"></a> `00a9f014` | `80 9d f5 97` | bl 0x00806614 | `UNCONDITIONAL_CALL`
<a id="insn-00a9f018"></a> `00a9f018` | `c0 fd 07 36` | tbz w0,#0x0,0x00a9efd0 | `CONDITIONAL_JUMP`
<a id="insn-00a9f01c"></a> `00a9f01c` | `80 00 80 52` | mov w0,#0x4 | `FALL_THROUGH`
<a id="insn-00a9f020"></a> `00a9f020` | `e1 03 17 2a` | mov w1,w23 | `FALL_THROUGH`
<a id="insn-00a9f024"></a> `00a9f024` | `0e 9d f5 97` | bl 0x0080645c | `UNCONDITIONAL_CALL`
<a id="insn-00a9f028"></a> `00a9f028` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00a9f02c"></a> `00a9f02c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00a9f030"></a> `00a9f030` | `56 05 f7 97` | bl 0x00860588 | `UNCONDITIONAL_CALL`
<a id="insn-00a9f034"></a> `00a9f034` | `c8 06 00 51` | sub w8,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00a9f038"></a> `00a9f038` | `1f 09 00 71` | cmp w8,#0x2 | `FALL_THROUGH`
<a id="insn-00a9f03c"></a> `00a9f03c` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00a9f040"></a> `00a9f040` | `08 01 00 0a` | and w8,w8,w0 | `FALL_THROUGH`
<a id="insn-00a9f044"></a> `00a9f044` | `68 fc 07 36` | tbz w8,#0x0,0x00a9efd0 | `CONDITIONAL_JUMP`
<a id="insn-00a9f048"></a> `00a9f048` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00a9f04c"></a> `00a9f04c` | `12 00 00 14` | b 0x00a9f094 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9f050"></a> `00a9f050` | `1f 0c 00 71` | cmp w0,#0x3 | `FALL_THROUGH`
<a id="insn-00a9f054"></a> `00a9f054` | `e1 01 00 54` | b.ne 0x00a9f090 | `CONDITIONAL_JUMP`
<a id="insn-00a9f058"></a> `00a9f058` | `18 23 00 91` | add x24,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00a9f05c"></a> `00a9f05c` | `1f 03 15 eb` | cmp x24,x21 | `FALL_THROUGH`
<a id="insn-00a9f060"></a> `00a9f060` | `40 ff ff 54` | b.eq 0x00a9f048 | `CONDITIONAL_JUMP`
<a id="insn-00a9f064"></a> `00a9f064` | `00 03 40 f9` | ldr x0,[x24] | `FALL_THROUGH`
<a id="insn-00a9f068"></a> `00a9f068` | `c2 29 fc 97` | bl 0x009a9770 | `UNCONDITIONAL_CALL`
<a id="insn-00a9f06c"></a> `00a9f06c` | `13 01 00 34` | cbz w19,0x00a9f08c | `CONDITIONAL_JUMP`
<a id="insn-00a9f070"></a> `00a9f070` | `7f 0a 00 71` | cmp w19,#0x2 | `FALL_THROUGH`
<a id="insn-00a9f074"></a> `00a9f074` | `e0 fe ff 54` | b.eq 0x00a9f050 | `CONDITIONAL_JUMP`
<a id="insn-00a9f078"></a> `00a9f078` | `7f 0e 00 71` | cmp w19,#0x3 | `FALL_THROUGH`
<a id="insn-00a9f07c"></a> `00a9f07c` | `e1 fe ff 54` | b.ne 0x00a9f058 | `CONDITIONAL_JUMP`
<a id="insn-00a9f080"></a> `00a9f080` | `1f 10 00 71` | cmp w0,#0x4 | `FALL_THROUGH`
<a id="insn-00a9f084"></a> `00a9f084` | `a0 fe ff 54` | b.eq 0x00a9f058 | `CONDITIONAL_JUMP`
<a id="insn-00a9f088"></a> `00a9f088` | `02 00 00 14` | b 0x00a9f090 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9f08c"></a> `00a9f08c` | `60 fe ff 34` | cbz w0,0x00a9f058 | `CONDITIONAL_JUMP`
<a id="insn-00a9f090"></a> `00a9f090` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00a9f094"></a> `00a9f094` | `f5 0f 40 f9` | ldr x21,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00a9f098"></a> `00a9f098` | `95 00 00 b4` | cbz x21,0x00a9f0a8 | `CONDITIONAL_JUMP`
<a id="insn-00a9f09c"></a> `00a9f09c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a9f0a0"></a> `00a9f0a0` | `f5 13 00 f9` | str x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00a9f0a4"></a> `00a9f0a4` | `83 e3 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00a9f0a8"></a> `00a9f0a8` | `b5 03 5e f8` | ldur x21,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-00a9f0ac"></a> `00a9f0ac` | `95 00 00 b4` | cbz x21,0x00a9f0bc | `CONDITIONAL_JUMP`
<a id="insn-00a9f0b0"></a> `00a9f0b0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00a9f0b4"></a> `00a9f0b4` | `b5 83 1e f8` | stur x21,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00a9f0b8"></a> `00a9f0b8` | `7e e3 06 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00a9f0bc"></a> `00a9f0bc` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9f0c0"></a> `00a9f0c0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00a9f0c4"></a> `00a9f0c4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a9f0c8"></a> `00a9f0c8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a9f0cc"></a> `00a9f0cc` | `41 06 00 54` | b.ne 0x00a9f194 | `CONDITIONAL_JUMP`
<a id="insn-00a9f0d0"></a> `00a9f0d0` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00a9f0d4"></a> `00a9f0d4` | `f4 4f 4a a9` | ldp x20,x19,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00a9f0d8"></a> `00a9f0d8` | `f6 57 49 a9` | ldp x22,x21,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00a9f0dc"></a> `00a9f0dc` | `f8 5f 48 a9` | ldp x24,x23,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00a9f0e0"></a> `00a9f0e0` | `fa 67 47 a9` | ldp x26,x25,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00a9f0e4"></a> `00a9f0e4` | `fc 6f 46 a9` | ldp x28,x27,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00a9f0e8"></a> `00a9f0e8` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00a9f0ec"></a> `00a9f0ec` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00a9f0f0"></a> `00a9f0f0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00a9f0f4"></a> `00a9f0f4` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00a9f0f8"></a> `00a9f0f8` | `d5 fd ff b5` | cbnz x21,0x00a9f0b0 | `CONDITIONAL_JUMP`
<a id="insn-00a9f0fc"></a> `00a9f0fc` | `f0 ff ff 17` | b 0x00a9f0bc | `UNCONDITIONAL_JUMP`
<a id="insn-00a9f100"></a> `00a9f100` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00a9f104"></a> `00a9f104` | `d5 fc ff b5` | cbnz x21,0x00a9f09c | `CONDITIONAL_JUMP`
<a id="insn-00a9f108"></a> `00a9f108` | `e8 ff ff 17` | b 0x00a9f0a8 | `UNCONDITIONAL_JUMP`
<a id="insn-00a9f10c"></a> `00a9f10c` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9f110"></a> `00a9f110` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00a9f114"></a> `00a9f114` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a9f118"></a> `00a9f118` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a9f11c"></a> `00a9f11c` | `c1 03 00 54` | b.ne 0x00a9f194 | `CONDITIONAL_JUMP`
<a id="insn-00a9f120"></a> `00a9f120` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00a9f124"></a> `00a9f124` | `5b 4b fc 97` | bl 0x009b1e90 | `UNCONDITIONAL_CALL`
<a id="insn-00a9f128"></a> `00a9f128` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00a9f12c"></a> `00a9f12c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00a9f130"></a> `00a9f130` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00a9f134"></a> `00a9f134` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00a9f138"></a> `00a9f138` | `e1 02 00 54` | b.ne 0x00a9f194 | `CONDITIONAL_JUMP`
<a id="insn-00a9f13c"></a> `00a9f13c` | `61 87 e6 97` | bl 0x00440ec0 | `CALL_TERMINATOR`
<a id="insn-00a9f194"></a> `00a9f194` | `53 e3 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00a9edec`](#insn-00a9edec) 範囲 `[['00a9edec', '00a9ee57']]`
  - `CONDITIONAL_JUMP` [`00a9ee54`](#insn-00a9ee54) → [`00a9f0f4`](#insn-00a9f0f4)
  - `FALL_THROUGH` [`00a9ee54`](#insn-00a9ee54) → [`00a9ee58`](#insn-00a9ee58)
- ブロック [`00a9ee58`](#insn-00a9ee58) 範囲 `[['00a9ee58', '00a9ee5f']]`
  - `UNCONDITIONAL_JUMP` [`00a9ee5c`](#insn-00a9ee5c) → [`00a9ee74`](#insn-00a9ee74)
- ブロック [`00a9ee60`](#insn-00a9ee60) 範囲 `[['00a9ee60', '00a9ee63']]`
  - `FALL_THROUGH` [`00a9ee60`](#insn-00a9ee60) → [`00a9ee64`](#insn-00a9ee64)
- ブロック [`00a9ee64`](#insn-00a9ee64) 範囲 `[['00a9ee64', '00a9ee67']]`
  - `FALL_THROUGH` [`00a9ee64`](#insn-00a9ee64) → [`00a9ee68`](#insn-00a9ee68)
- ブロック [`00a9ee68`](#insn-00a9ee68) 範囲 `[['00a9ee68', '00a9ee73']]`
  - `CONDITIONAL_JUMP` [`00a9ee70`](#insn-00a9ee70) → [`00a9efa4`](#insn-00a9efa4)
  - `FALL_THROUGH` [`00a9ee70`](#insn-00a9ee70) → [`00a9ee74`](#insn-00a9ee74)
- ブロック [`00a9ee74`](#insn-00a9ee74) 範囲 `[['00a9ee74', '00a9ee97']]`
  - `CONDITIONAL_JUMP` [`00a9ee94`](#insn-00a9ee94) → [`00a9ef00`](#insn-00a9ef00)
  - `FALL_THROUGH` [`00a9ee94`](#insn-00a9ee94) → [`00a9ee98`](#insn-00a9ee98)
- ブロック [`00a9ee98`](#insn-00a9ee98) 範囲 `[['00a9ee98', '00a9eea3']]`
  - `CONDITIONAL_JUMP` [`00a9eea0`](#insn-00a9eea0) → [`00a9ee68`](#insn-00a9ee68)
  - `FALL_THROUGH` [`00a9eea0`](#insn-00a9eea0) → [`00a9eea4`](#insn-00a9eea4)
- ブロック [`00a9eea4`](#insn-00a9eea4) 範囲 `[['00a9eea4', '00a9eea7']]`
  - `FALL_THROUGH` [`00a9eea4`](#insn-00a9eea4) → [`00a9eea8`](#insn-00a9eea8)
- ブロック [`00a9eea8`](#insn-00a9eea8) 範囲 `[['00a9eea8', '00a9eeaf']]`
  - `CONDITIONAL_JUMP` [`00a9eeac`](#insn-00a9eeac) → [`00a9ee60`](#insn-00a9ee60)
  - `FALL_THROUGH` [`00a9eeac`](#insn-00a9eeac) → [`00a9eeb0`](#insn-00a9eeb0)
- ブロック [`00a9eeb0`](#insn-00a9eeb0) 範囲 `[['00a9eeb0', '00a9eec7']]`
  - `CONDITIONAL_JUMP` [`00a9eec4`](#insn-00a9eec4) → [`00a9f10c`](#insn-00a9f10c)
  - `FALL_THROUGH` [`00a9eec4`](#insn-00a9eec4) → [`00a9eec8`](#insn-00a9eec8)
- ブロック [`00a9eec8`](#insn-00a9eec8) 範囲 `[['00a9eec8', '00a9eeeb']]`
  - `CONDITIONAL_JUMP` [`00a9eee8`](#insn-00a9eee8) → [`00a9ef6c`](#insn-00a9ef6c)
  - `FALL_THROUGH` [`00a9eee8`](#insn-00a9eee8) → [`00a9eeec`](#insn-00a9eeec)
- ブロック [`00a9eeec`](#insn-00a9eeec) 範囲 `[['00a9eeec', '00a9eef3']]`
  - `CONDITIONAL_JUMP` [`00a9eef0`](#insn-00a9eef0) → [`00a9f128`](#insn-00a9f128)
  - `FALL_THROUGH` [`00a9eef0`](#insn-00a9eef0) → [`00a9eef4`](#insn-00a9eef4)
- ブロック [`00a9eef4`](#insn-00a9eef4) 範囲 `[['00a9eef4', '00a9eeff']]`
  - `UNCONDITIONAL_JUMP` [`00a9eefc`](#insn-00a9eefc) → [`00a9ef64`](#insn-00a9ef64)
- ブロック [`00a9ef00`](#insn-00a9ef00) 範囲 `[['00a9ef00', '00a9ef0b']]`
  - `CONDITIONAL_JUMP` [`00a9ef08`](#insn-00a9ef08) → [`00a9ee68`](#insn-00a9ee68)
  - `FALL_THROUGH` [`00a9ef08`](#insn-00a9ef08) → [`00a9ef0c`](#insn-00a9ef0c)
- ブロック [`00a9ef0c`](#insn-00a9ef0c) 範囲 `[['00a9ef0c', '00a9ef17']]`
  - `CONDITIONAL_JUMP` [`00a9ef14`](#insn-00a9ef14) → [`00a9ee60`](#insn-00a9ee60)
  - `FALL_THROUGH` [`00a9ef14`](#insn-00a9ef14) → [`00a9ef18`](#insn-00a9ef18)
- ブロック [`00a9ef18`](#insn-00a9ef18) 範囲 `[['00a9ef18', '00a9ef2f']]`
  - `CONDITIONAL_JUMP` [`00a9ef2c`](#insn-00a9ef2c) → [`00a9f10c`](#insn-00a9f10c)
  - `FALL_THROUGH` [`00a9ef2c`](#insn-00a9ef2c) → [`00a9ef30`](#insn-00a9ef30)
- ブロック [`00a9ef30`](#insn-00a9ef30) 範囲 `[['00a9ef30', '00a9ef53']]`
  - `CONDITIONAL_JUMP` [`00a9ef50`](#insn-00a9ef50) → [`00a9ef6c`](#insn-00a9ef6c)
  - `FALL_THROUGH` [`00a9ef50`](#insn-00a9ef50) → [`00a9ef54`](#insn-00a9ef54)
- ブロック [`00a9ef54`](#insn-00a9ef54) 範囲 `[['00a9ef54', '00a9ef5b']]`
  - `CONDITIONAL_JUMP` [`00a9ef58`](#insn-00a9ef58) → [`00a9f128`](#insn-00a9f128)
  - `FALL_THROUGH` [`00a9ef58`](#insn-00a9ef58) → [`00a9ef5c`](#insn-00a9ef5c)
- ブロック [`00a9ef5c`](#insn-00a9ef5c) 範囲 `[['00a9ef5c', '00a9ef63']]`
  - `FALL_THROUGH` [`00a9ef60`](#insn-00a9ef60) → [`00a9ef64`](#insn-00a9ef64)
- ブロック [`00a9ef64`](#insn-00a9ef64) 範囲 `[['00a9ef64', '00a9ef6b']]`
  - `UNCONDITIONAL_JUMP` [`00a9ef68`](#insn-00a9ef68) → [`00a9ef70`](#insn-00a9ef70)
- ブロック [`00a9ef6c`](#insn-00a9ef6c) 範囲 `[['00a9ef6c', '00a9ef6f']]`
  - `FALL_THROUGH` [`00a9ef6c`](#insn-00a9ef6c) → [`00a9ef70`](#insn-00a9ef70)
- ブロック [`00a9ef70`](#insn-00a9ef70) 範囲 `[['00a9ef70', '00a9ef97']]`
  - `CONDITIONAL_JUMP` [`00a9ef94`](#insn-00a9ef94) → [`00a9ee64`](#insn-00a9ee64)
  - `FALL_THROUGH` [`00a9ef94`](#insn-00a9ef94) → [`00a9ef98`](#insn-00a9ef98)
- ブロック [`00a9ef98`](#insn-00a9ef98) 範囲 `[['00a9ef98', '00a9efa3']]`
  - `UNCONDITIONAL_JUMP` [`00a9efa0`](#insn-00a9efa0) → [`00a9ee64`](#insn-00a9ee64)
- ブロック [`00a9efa4`](#insn-00a9efa4) 範囲 `[['00a9efa4', '00a9efaf']]`
  - `CONDITIONAL_JUMP` [`00a9efac`](#insn-00a9efac) → [`00a9f100`](#insn-00a9f100)
  - `FALL_THROUGH` [`00a9efac`](#insn-00a9efac) → [`00a9efb0`](#insn-00a9efb0)
- ブロック [`00a9efb0`](#insn-00a9efb0) 範囲 `[['00a9efb0', '00a9efbb']]`
  - `CONDITIONAL_JUMP` [`00a9efb8`](#insn-00a9efb8) → [`00a9f064`](#insn-00a9f064)
  - `FALL_THROUGH` [`00a9efb8`](#insn-00a9efb8) → [`00a9efbc`](#insn-00a9efbc)
- ブロック [`00a9efbc`](#insn-00a9efbc) 範囲 `[['00a9efbc', '00a9efc3']]`
  - `UNCONDITIONAL_JUMP` [`00a9efc0`](#insn-00a9efc0) → [`00a9efdc`](#insn-00a9efdc)
- ブロック [`00a9efc4`](#insn-00a9efc4) 範囲 `[['00a9efc4', '00a9efcf']]`
  - `CONDITIONAL_JUMP` [`00a9efcc`](#insn-00a9efcc) → [`00a9f048`](#insn-00a9f048)
  - `FALL_THROUGH` [`00a9efcc`](#insn-00a9efcc) → [`00a9efd0`](#insn-00a9efd0)
- ブロック [`00a9efd0`](#insn-00a9efd0) 範囲 `[['00a9efd0', '00a9efdb']]`
  - `CONDITIONAL_JUMP` [`00a9efd8`](#insn-00a9efd8) → [`00a9f090`](#insn-00a9f090)
  - `FALL_THROUGH` [`00a9efd8`](#insn-00a9efd8) → [`00a9efdc`](#insn-00a9efdc)
- ブロック [`00a9efdc`](#insn-00a9efdc) 範囲 `[['00a9efdc', '00a9eff7']]`
  - `CONDITIONAL_JUMP` [`00a9eff4`](#insn-00a9eff4) → [`00a9efc4`](#insn-00a9efc4)
  - `FALL_THROUGH` [`00a9eff4`](#insn-00a9eff4) → [`00a9eff8`](#insn-00a9eff8)
- ブロック [`00a9eff8`](#insn-00a9eff8) 範囲 `[['00a9eff8', '00a9f00b']]`
  - `CONDITIONAL_JUMP` [`00a9f008`](#insn-00a9f008) → [`00a9efd0`](#insn-00a9efd0)
  - `FALL_THROUGH` [`00a9f008`](#insn-00a9f008) → [`00a9f00c`](#insn-00a9f00c)
- ブロック [`00a9f00c`](#insn-00a9f00c) 範囲 `[['00a9f00c', '00a9f01b']]`
  - `CONDITIONAL_JUMP` [`00a9f018`](#insn-00a9f018) → [`00a9efd0`](#insn-00a9efd0)
  - `FALL_THROUGH` [`00a9f018`](#insn-00a9f018) → [`00a9f01c`](#insn-00a9f01c)
- ブロック [`00a9f01c`](#insn-00a9f01c) 範囲 `[['00a9f01c', '00a9f047']]`
  - `CONDITIONAL_JUMP` [`00a9f044`](#insn-00a9f044) → [`00a9efd0`](#insn-00a9efd0)
  - `FALL_THROUGH` [`00a9f044`](#insn-00a9f044) → [`00a9f048`](#insn-00a9f048)
- ブロック [`00a9f048`](#insn-00a9f048) 範囲 `[['00a9f048', '00a9f04f']]`
  - `UNCONDITIONAL_JUMP` [`00a9f04c`](#insn-00a9f04c) → [`00a9f094`](#insn-00a9f094)
- ブロック [`00a9f050`](#insn-00a9f050) 範囲 `[['00a9f050', '00a9f057']]`
  - `CONDITIONAL_JUMP` [`00a9f054`](#insn-00a9f054) → [`00a9f090`](#insn-00a9f090)
  - `FALL_THROUGH` [`00a9f054`](#insn-00a9f054) → [`00a9f058`](#insn-00a9f058)
- ブロック [`00a9f058`](#insn-00a9f058) 範囲 `[['00a9f058', '00a9f063']]`
  - `CONDITIONAL_JUMP` [`00a9f060`](#insn-00a9f060) → [`00a9f048`](#insn-00a9f048)
  - `FALL_THROUGH` [`00a9f060`](#insn-00a9f060) → [`00a9f064`](#insn-00a9f064)
- ブロック [`00a9f064`](#insn-00a9f064) 範囲 `[['00a9f064', '00a9f06f']]`
  - `CONDITIONAL_JUMP` [`00a9f06c`](#insn-00a9f06c) → [`00a9f08c`](#insn-00a9f08c)
  - `FALL_THROUGH` [`00a9f06c`](#insn-00a9f06c) → [`00a9f070`](#insn-00a9f070)
- ブロック [`00a9f070`](#insn-00a9f070) 範囲 `[['00a9f070', '00a9f077']]`
  - `CONDITIONAL_JUMP` [`00a9f074`](#insn-00a9f074) → [`00a9f050`](#insn-00a9f050)
  - `FALL_THROUGH` [`00a9f074`](#insn-00a9f074) → [`00a9f078`](#insn-00a9f078)
- ブロック [`00a9f078`](#insn-00a9f078) 範囲 `[['00a9f078', '00a9f07f']]`
  - `CONDITIONAL_JUMP` [`00a9f07c`](#insn-00a9f07c) → [`00a9f058`](#insn-00a9f058)
  - `FALL_THROUGH` [`00a9f07c`](#insn-00a9f07c) → [`00a9f080`](#insn-00a9f080)
- ブロック [`00a9f080`](#insn-00a9f080) 範囲 `[['00a9f080', '00a9f087']]`
  - `CONDITIONAL_JUMP` [`00a9f084`](#insn-00a9f084) → [`00a9f058`](#insn-00a9f058)
  - `FALL_THROUGH` [`00a9f084`](#insn-00a9f084) → [`00a9f088`](#insn-00a9f088)
- ブロック [`00a9f088`](#insn-00a9f088) 範囲 `[['00a9f088', '00a9f08b']]`
  - `UNCONDITIONAL_JUMP` [`00a9f088`](#insn-00a9f088) → [`00a9f090`](#insn-00a9f090)
- ブロック [`00a9f08c`](#insn-00a9f08c) 範囲 `[['00a9f08c', '00a9f08f']]`
  - `CONDITIONAL_JUMP` [`00a9f08c`](#insn-00a9f08c) → [`00a9f058`](#insn-00a9f058)
  - `FALL_THROUGH` [`00a9f08c`](#insn-00a9f08c) → [`00a9f090`](#insn-00a9f090)
- ブロック [`00a9f090`](#insn-00a9f090) 範囲 `[['00a9f090', '00a9f093']]`
  - `FALL_THROUGH` [`00a9f090`](#insn-00a9f090) → [`00a9f094`](#insn-00a9f094)
- ブロック [`00a9f094`](#insn-00a9f094) 範囲 `[['00a9f094', '00a9f09b']]`
  - `CONDITIONAL_JUMP` [`00a9f098`](#insn-00a9f098) → [`00a9f0a8`](#insn-00a9f0a8)
  - `FALL_THROUGH` [`00a9f098`](#insn-00a9f098) → [`00a9f09c`](#insn-00a9f09c)
- ブロック [`00a9f09c`](#insn-00a9f09c) 範囲 `[['00a9f09c', '00a9f0a7']]`
  - `FALL_THROUGH` [`00a9f0a4`](#insn-00a9f0a4) → [`00a9f0a8`](#insn-00a9f0a8)
- ブロック [`00a9f0a8`](#insn-00a9f0a8) 範囲 `[['00a9f0a8', '00a9f0af']]`
  - `CONDITIONAL_JUMP` [`00a9f0ac`](#insn-00a9f0ac) → [`00a9f0bc`](#insn-00a9f0bc)
  - `FALL_THROUGH` [`00a9f0ac`](#insn-00a9f0ac) → [`00a9f0b0`](#insn-00a9f0b0)
- ブロック [`00a9f0b0`](#insn-00a9f0b0) 範囲 `[['00a9f0b0', '00a9f0bb']]`
  - `FALL_THROUGH` [`00a9f0b8`](#insn-00a9f0b8) → [`00a9f0bc`](#insn-00a9f0bc)
- ブロック [`00a9f0bc`](#insn-00a9f0bc) 範囲 `[['00a9f0bc', '00a9f0cf']]`
  - `CONDITIONAL_JUMP` [`00a9f0cc`](#insn-00a9f0cc) → [`00a9f194`](#insn-00a9f194)
  - `FALL_THROUGH` [`00a9f0cc`](#insn-00a9f0cc) → [`00a9f0d0`](#insn-00a9f0d0)
- ブロック [`00a9f0d0`](#insn-00a9f0d0) 範囲 `[['00a9f0d0', '00a9f0f3']]`
- ブロック [`00a9f0f4`](#insn-00a9f0f4) 範囲 `[['00a9f0f4', '00a9f0fb']]`
  - `CONDITIONAL_JUMP` [`00a9f0f8`](#insn-00a9f0f8) → [`00a9f0b0`](#insn-00a9f0b0)
  - `FALL_THROUGH` [`00a9f0f8`](#insn-00a9f0f8) → [`00a9f0fc`](#insn-00a9f0fc)
- ブロック [`00a9f0fc`](#insn-00a9f0fc) 範囲 `[['00a9f0fc', '00a9f0ff']]`
  - `UNCONDITIONAL_JUMP` [`00a9f0fc`](#insn-00a9f0fc) → [`00a9f0bc`](#insn-00a9f0bc)
- ブロック [`00a9f100`](#insn-00a9f100) 範囲 `[['00a9f100', '00a9f107']]`
  - `CONDITIONAL_JUMP` [`00a9f104`](#insn-00a9f104) → [`00a9f09c`](#insn-00a9f09c)
  - `FALL_THROUGH` [`00a9f104`](#insn-00a9f104) → [`00a9f108`](#insn-00a9f108)
- ブロック [`00a9f108`](#insn-00a9f108) 範囲 `[['00a9f108', '00a9f10b']]`
  - `UNCONDITIONAL_JUMP` [`00a9f108`](#insn-00a9f108) → [`00a9f0a8`](#insn-00a9f0a8)
- ブロック [`00a9f10c`](#insn-00a9f10c) 範囲 `[['00a9f10c', '00a9f11f']]`
  - `CONDITIONAL_JUMP` [`00a9f11c`](#insn-00a9f11c) → [`00a9f194`](#insn-00a9f194)
  - `FALL_THROUGH` [`00a9f11c`](#insn-00a9f11c) → [`00a9f120`](#insn-00a9f120)
- ブロック [`00a9f120`](#insn-00a9f120) 範囲 `[['00a9f120', '00a9f127']]`
  - `FALL_THROUGH` [`00a9f124`](#insn-00a9f124) → [`00a9f128`](#insn-00a9f128)
- ブロック [`00a9f128`](#insn-00a9f128) 範囲 `[['00a9f128', '00a9f13b']]`
  - `CONDITIONAL_JUMP` [`00a9f138`](#insn-00a9f138) → [`00a9f194`](#insn-00a9f194)
  - `FALL_THROUGH` [`00a9f138`](#insn-00a9f138) → [`00a9f13c`](#insn-00a9f13c)
- ブロック [`00a9f13c`](#insn-00a9f13c) 範囲 `[['00a9f13c', '00a9f13f']]`
- ブロック [`00a9f194`](#insn-00a9f194) 範囲 `[['00a9f194', '00a9f197']]`

## 命令位置別の参照

- [`00a9edf0`](#insn-00a9edf0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9edf4`](#insn-00a9edf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9edf8`](#insn-00a9edf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9edfc`](#insn-00a9edfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee00`](#insn-00a9ee00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee04`](#insn-00a9ee04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee18`](#insn-00a9ee18) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee20`](#insn-00a9ee20) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee24`](#insn-00a9ee24) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee40`](#insn-00a9ee40) → [`009ad980`](../009ad/009ad980.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009ad980` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee44`](#insn-00a9ee44) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee48`](#insn-00a9ee48) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee4c`](#insn-00a9ee4c) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee54`](#insn-00a9ee54) → [`00a9f0f4`](#insn-00a9f0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee58`](#insn-00a9ee58) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee5c`](#insn-00a9ee5c) → [`00a9ee74`](#insn-00a9ee74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee64`](#insn-00a9ee64) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee70`](#insn-00a9ee70) → [`00a9efa4`](#insn-00a9efa4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee7c`](#insn-00a9ee7c) → [`009a9760`](../009a9/009a9760.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a9760` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee88`](#insn-00a9ee88) → [`008001ec`](../00800/008001ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008001ec` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee94`](#insn-00a9ee94) → [`00a9ef00`](#insn-00a9ef00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ee9c`](#insn-00a9ee9c) → [`00a31b78`](../00a31/00a31b78.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a31b78` · 推定シンボル `None` · 推定型 `None`
- [`00a9eea0`](#insn-00a9eea0) → [`00a9ee68`](#insn-00a9ee68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9eea4`](#insn-00a9eea4) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9eeac`](#insn-00a9eeac) → [`00a9ee60`](#insn-00a9ee60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9eeb0`](#insn-00a9eeb0) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9eec4`](#insn-00a9eec4) → [`00a9f10c`](#insn-00a9f10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9eee8`](#insn-00a9eee8) → [`00a9ef6c`](#insn-00a9ef6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9eef0`](#insn-00a9eef0) → [`00a9f128`](#insn-00a9f128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9eef8`](#insn-00a9eef8) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00a9eefc`](#insn-00a9eefc) → [`00a9ef64`](#insn-00a9ef64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef04`](#insn-00a9ef04) → [`00a31b78`](../00a31/00a31b78.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00a31b78` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef08`](#insn-00a9ef08) → [`00a9ee68`](#insn-00a9ee68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef0c`](#insn-00a9ef0c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef14`](#insn-00a9ef14) → [`00a9ee60`](#insn-00a9ee60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef18`](#insn-00a9ef18) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef2c`](#insn-00a9ef2c) → [`00a9f10c`](#insn-00a9f10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef50`](#insn-00a9ef50) → [`00a9ef6c`](#insn-00a9ef6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef58`](#insn-00a9ef58) → [`00a9f128`](#insn-00a9f128) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef60`](#insn-00a9ef60) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef68`](#insn-00a9ef68) → [`00a9ef70`](#insn-00a9ef70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef88`](#insn-00a9ef88) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef8c`](#insn-00a9ef8c) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef90`](#insn-00a9ef90) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef94`](#insn-00a9ef94) → [`00a9ee64`](#insn-00a9ee64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9ef9c`](#insn-00a9ef9c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00a9efa0`](#insn-00a9efa0) → [`00a9ee64`](#insn-00a9ee64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9efa4`](#insn-00a9efa4) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9efac`](#insn-00a9efac) → [`00a9f100`](#insn-00a9f100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9efb0`](#insn-00a9efb0) → `Stack[-0xa4]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9efb8`](#insn-00a9efb8) → [`00a9f064`](#insn-00a9f064) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9efbc`](#insn-00a9efbc) → `Stack[-0xa8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9efc0`](#insn-00a9efc0) → [`00a9efdc`](#insn-00a9efdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9efcc`](#insn-00a9efcc) → [`00a9f048`](#insn-00a9f048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9efd8`](#insn-00a9efd8) → [`00a9f090`](#insn-00a9f090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9efe4`](#insn-00a9efe4) → [`009a9770`](../009a9/009a9770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a9770` · 推定シンボル `None` · 推定型 `None`
- [`00a9eff0`](#insn-00a9eff0) → [`009a9760`](../009a9/009a9760.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a9760` · 推定シンボル `None` · 推定型 `None`
- [`00a9eff4`](#insn-00a9eff4) → [`00a9efc4`](#insn-00a9efc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f004`](#insn-00a9f004) → [`00804074`](../00804/00804074.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00804074` · 推定シンボル `None` · 推定型 `None`
- [`00a9f008`](#insn-00a9f008) → [`00a9efd0`](#insn-00a9efd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f014`](#insn-00a9f014) → [`00806614`](../00806/00806614.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00806614` · 推定シンボル `None` · 推定型 `None`
- [`00a9f018`](#insn-00a9f018) → [`00a9efd0`](#insn-00a9efd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f024`](#insn-00a9f024) → [`0080645c`](../00806/0080645c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0080645c` · 推定シンボル `None` · 推定型 `None`
- [`00a9f030`](#insn-00a9f030) → [`00860588`](../00860/00860588.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00860588` · 推定シンボル `None` · 推定型 `None`
- [`00a9f044`](#insn-00a9f044) → [`00a9efd0`](#insn-00a9efd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f04c`](#insn-00a9f04c) → [`00a9f094`](#insn-00a9f094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f054`](#insn-00a9f054) → [`00a9f090`](#insn-00a9f090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f060`](#insn-00a9f060) → [`00a9f048`](#insn-00a9f048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f068`](#insn-00a9f068) → [`009a9770`](../009a9/009a9770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009a9770` · 推定シンボル `None` · 推定型 `None`
- [`00a9f06c`](#insn-00a9f06c) → [`00a9f08c`](#insn-00a9f08c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f074`](#insn-00a9f074) → [`00a9f050`](#insn-00a9f050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f07c`](#insn-00a9f07c) → [`00a9f058`](#insn-00a9f058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f084`](#insn-00a9f084) → [`00a9f058`](#insn-00a9f058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f088`](#insn-00a9f088) → [`00a9f090`](#insn-00a9f090) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f08c`](#insn-00a9f08c) → [`00a9f058`](#insn-00a9f058) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f094`](#insn-00a9f094) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f098`](#insn-00a9f098) → [`00a9f0a8`](#insn-00a9f0a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0a0`](#insn-00a9f0a0) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0a4`](#insn-00a9f0a4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0a8`](#insn-00a9f0a8) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0ac`](#insn-00a9f0ac) → [`00a9f0bc`](#insn-00a9f0bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0b4`](#insn-00a9f0b4) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0b8`](#insn-00a9f0b8) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0bc`](#insn-00a9f0bc) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0c4`](#insn-00a9f0c4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0cc`](#insn-00a9f0cc) → [`00a9f194`](#insn-00a9f194) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0d4`](#insn-00a9f0d4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0d8`](#insn-00a9f0d8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0dc`](#insn-00a9f0dc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0e0`](#insn-00a9f0e0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0e4`](#insn-00a9f0e4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0e8`](#insn-00a9f0e8) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0f8`](#insn-00a9f0f8) → [`00a9f0b0`](#insn-00a9f0b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f0fc`](#insn-00a9f0fc) → [`00a9f0bc`](#insn-00a9f0bc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f104`](#insn-00a9f104) → [`00a9f09c`](#insn-00a9f09c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f108`](#insn-00a9f108) → [`00a9f0a8`](#insn-00a9f0a8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f10c`](#insn-00a9f10c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f114`](#insn-00a9f114) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f11c`](#insn-00a9f11c) → [`00a9f194`](#insn-00a9f194) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f124`](#insn-00a9f124) → [`009b1e90`](../009b1/009b1e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b1e90` · 推定シンボル `None` · 推定型 `None`
- [`00a9f128`](#insn-00a9f128) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f130`](#insn-00a9f130) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f138`](#insn-00a9f138) → [`00a9f194`](#insn-00a9f194) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00a9f13c`](#insn-00a9f13c) → [`00440ec0`](../00440/00440ec0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00440ec0` · 推定シンボル `None` · 推定型 `None`
- [`00a9f194`](#insn-00a9f194) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00a9edf0`](#insn-00a9edf0)

~~~json
{
  "source": "00a9edf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9edf4`](#insn-00a9edf4)

~~~json
{
  "source": "00a9edf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9edf8`](#insn-00a9edf8)

~~~json
{
  "source": "00a9edf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9edfc`](#insn-00a9edfc)

~~~json
{
  "source": "00a9edfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee00`](#insn-00a9ee00)

~~~json
{
  "source": "00a9ee00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee04`](#insn-00a9ee04)

~~~json
{
  "source": "00a9ee04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee18`](#insn-00a9ee18)

~~~json
{
  "source": "00a9ee18",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee20`](#insn-00a9ee20)

~~~json
{
  "source": "00a9ee20",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee24`](#insn-00a9ee24)

~~~json
{
  "source": "00a9ee24",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ee40`](#insn-00a9ee40)

~~~json
{
  "source": "00a9ee40",
  "target": "009ad980",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ee44`](#insn-00a9ee44)

~~~json
{
  "source": "00a9ee44",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee48`](#insn-00a9ee48)

~~~json
{
  "source": "00a9ee48",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee4c`](#insn-00a9ee4c)

~~~json
{
  "source": "00a9ee4c",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee54`](#insn-00a9ee54)

~~~json
{
  "source": "00a9ee54",
  "target": "00a9f0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee58`](#insn-00a9ee58)

~~~json
{
  "source": "00a9ee58",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee5c`](#insn-00a9ee5c)

~~~json
{
  "source": "00a9ee5c",
  "target": "00a9ee74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee64`](#insn-00a9ee64)

~~~json
{
  "source": "00a9ee64",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee70`](#insn-00a9ee70)

~~~json
{
  "source": "00a9ee70",
  "target": "00a9efa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee7c`](#insn-00a9ee7c)

~~~json
{
  "source": "00a9ee7c",
  "target": "009a9760",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ee88`](#insn-00a9ee88)

~~~json
{
  "source": "00a9ee88",
  "target": "008001ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ee94`](#insn-00a9ee94)

~~~json
{
  "source": "00a9ee94",
  "target": "00a9ef00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ee9c`](#insn-00a9ee9c)

~~~json
{
  "source": "00a9ee9c",
  "target": "00a31b78",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9eea0`](#insn-00a9eea0)

~~~json
{
  "source": "00a9eea0",
  "target": "00a9ee68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9eea4`](#insn-00a9eea4)

~~~json
{
  "source": "00a9eea4",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9eeac`](#insn-00a9eeac)

~~~json
{
  "source": "00a9eeac",
  "target": "00a9ee60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9eeb0`](#insn-00a9eeb0)

~~~json
{
  "source": "00a9eeb0",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9eec4`](#insn-00a9eec4)

~~~json
{
  "source": "00a9eec4",
  "target": "00a9f10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9eee8`](#insn-00a9eee8)

~~~json
{
  "source": "00a9eee8",
  "target": "00a9ef6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9eef0`](#insn-00a9eef0)

~~~json
{
  "source": "00a9eef0",
  "target": "00a9f128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9eef8`](#insn-00a9eef8)

~~~json
{
  "source": "00a9eef8",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9eefc`](#insn-00a9eefc)

~~~json
{
  "source": "00a9eefc",
  "target": "00a9ef64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef04`](#insn-00a9ef04)

~~~json
{
  "source": "00a9ef04",
  "target": "00a31b78",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ef08`](#insn-00a9ef08)

~~~json
{
  "source": "00a9ef08",
  "target": "00a9ee68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef0c`](#insn-00a9ef0c)

~~~json
{
  "source": "00a9ef0c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef14`](#insn-00a9ef14)

~~~json
{
  "source": "00a9ef14",
  "target": "00a9ee60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef18`](#insn-00a9ef18)

~~~json
{
  "source": "00a9ef18",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef2c`](#insn-00a9ef2c)

~~~json
{
  "source": "00a9ef2c",
  "target": "00a9f10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef50`](#insn-00a9ef50)

~~~json
{
  "source": "00a9ef50",
  "target": "00a9ef6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef58`](#insn-00a9ef58)

~~~json
{
  "source": "00a9ef58",
  "target": "00a9f128",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef60`](#insn-00a9ef60)

~~~json
{
  "source": "00a9ef60",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ef68`](#insn-00a9ef68)

~~~json
{
  "source": "00a9ef68",
  "target": "00a9ef70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef88`](#insn-00a9ef88)

~~~json
{
  "source": "00a9ef88",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9ef8c`](#insn-00a9ef8c)

~~~json
{
  "source": "00a9ef8c",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef90`](#insn-00a9ef90)

~~~json
{
  "source": "00a9ef90",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef94`](#insn-00a9ef94)

~~~json
{
  "source": "00a9ef94",
  "target": "00a9ee64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9ef9c`](#insn-00a9ef9c)

~~~json
{
  "source": "00a9ef9c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9efa0`](#insn-00a9efa0)

~~~json
{
  "source": "00a9efa0",
  "target": "00a9ee64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9efa4`](#insn-00a9efa4)

~~~json
{
  "source": "00a9efa4",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9efac`](#insn-00a9efac)

~~~json
{
  "source": "00a9efac",
  "target": "00a9f100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9efb0`](#insn-00a9efb0)

~~~json
{
  "source": "00a9efb0",
  "target": "Stack[-0xa4]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9efb8`](#insn-00a9efb8)

~~~json
{
  "source": "00a9efb8",
  "target": "00a9f064",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9efbc`](#insn-00a9efbc)

~~~json
{
  "source": "00a9efbc",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9efc0`](#insn-00a9efc0)

~~~json
{
  "source": "00a9efc0",
  "target": "00a9efdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9efcc`](#insn-00a9efcc)

~~~json
{
  "source": "00a9efcc",
  "target": "00a9f048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9efd8`](#insn-00a9efd8)

~~~json
{
  "source": "00a9efd8",
  "target": "00a9f090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9efe4`](#insn-00a9efe4)

~~~json
{
  "source": "00a9efe4",
  "target": "009a9770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9eff0`](#insn-00a9eff0)

~~~json
{
  "source": "00a9eff0",
  "target": "009a9760",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9eff4`](#insn-00a9eff4)

~~~json
{
  "source": "00a9eff4",
  "target": "00a9efc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f004`](#insn-00a9f004)

~~~json
{
  "source": "00a9f004",
  "target": "00804074",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9f008`](#insn-00a9f008)

~~~json
{
  "source": "00a9f008",
  "target": "00a9efd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f014`](#insn-00a9f014)

~~~json
{
  "source": "00a9f014",
  "target": "00806614",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9f018`](#insn-00a9f018)

~~~json
{
  "source": "00a9f018",
  "target": "00a9efd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f024`](#insn-00a9f024)

~~~json
{
  "source": "00a9f024",
  "target": "0080645c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9f030`](#insn-00a9f030)

~~~json
{
  "source": "00a9f030",
  "target": "00860588",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9f044`](#insn-00a9f044)

~~~json
{
  "source": "00a9f044",
  "target": "00a9efd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f04c`](#insn-00a9f04c)

~~~json
{
  "source": "00a9f04c",
  "target": "00a9f094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f054`](#insn-00a9f054)

~~~json
{
  "source": "00a9f054",
  "target": "00a9f090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f060`](#insn-00a9f060)

~~~json
{
  "source": "00a9f060",
  "target": "00a9f048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f068`](#insn-00a9f068)

~~~json
{
  "source": "00a9f068",
  "target": "009a9770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9f06c`](#insn-00a9f06c)

~~~json
{
  "source": "00a9f06c",
  "target": "00a9f08c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f074`](#insn-00a9f074)

~~~json
{
  "source": "00a9f074",
  "target": "00a9f050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f07c`](#insn-00a9f07c)

~~~json
{
  "source": "00a9f07c",
  "target": "00a9f058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f084`](#insn-00a9f084)

~~~json
{
  "source": "00a9f084",
  "target": "00a9f058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f088`](#insn-00a9f088)

~~~json
{
  "source": "00a9f088",
  "target": "00a9f090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f08c`](#insn-00a9f08c)

~~~json
{
  "source": "00a9f08c",
  "target": "00a9f058",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f094`](#insn-00a9f094)

~~~json
{
  "source": "00a9f094",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f098`](#insn-00a9f098)

~~~json
{
  "source": "00a9f098",
  "target": "00a9f0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0a0`](#insn-00a9f0a0)

~~~json
{
  "source": "00a9f0a0",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0a4`](#insn-00a9f0a4)

~~~json
{
  "source": "00a9f0a4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9f0a8`](#insn-00a9f0a8)

~~~json
{
  "source": "00a9f0a8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0ac`](#insn-00a9f0ac)

~~~json
{
  "source": "00a9f0ac",
  "target": "00a9f0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0b4`](#insn-00a9f0b4)

~~~json
{
  "source": "00a9f0b4",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0b8`](#insn-00a9f0b8)

~~~json
{
  "source": "00a9f0b8",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9f0bc`](#insn-00a9f0bc)

~~~json
{
  "source": "00a9f0bc",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0c4`](#insn-00a9f0c4)

~~~json
{
  "source": "00a9f0c4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0cc`](#insn-00a9f0cc)

~~~json
{
  "source": "00a9f0cc",
  "target": "00a9f194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0d4`](#insn-00a9f0d4)

~~~json
{
  "source": "00a9f0d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0d8`](#insn-00a9f0d8)

~~~json
{
  "source": "00a9f0d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0dc`](#insn-00a9f0dc)

~~~json
{
  "source": "00a9f0dc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0e0`](#insn-00a9f0e0)

~~~json
{
  "source": "00a9f0e0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0e4`](#insn-00a9f0e4)

~~~json
{
  "source": "00a9f0e4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0e8`](#insn-00a9f0e8)

~~~json
{
  "source": "00a9f0e8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0f8`](#insn-00a9f0f8)

~~~json
{
  "source": "00a9f0f8",
  "target": "00a9f0b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f0fc`](#insn-00a9f0fc)

~~~json
{
  "source": "00a9f0fc",
  "target": "00a9f0bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f104`](#insn-00a9f104)

~~~json
{
  "source": "00a9f104",
  "target": "00a9f09c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f108`](#insn-00a9f108)

~~~json
{
  "source": "00a9f108",
  "target": "00a9f0a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f10c`](#insn-00a9f10c)

~~~json
{
  "source": "00a9f10c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f114`](#insn-00a9f114)

~~~json
{
  "source": "00a9f114",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f11c`](#insn-00a9f11c)

~~~json
{
  "source": "00a9f11c",
  "target": "00a9f194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f124`](#insn-00a9f124)

~~~json
{
  "source": "00a9f124",
  "target": "009b1e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9f128`](#insn-00a9f128)

~~~json
{
  "source": "00a9f128",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f130`](#insn-00a9f130)

~~~json
{
  "source": "00a9f130",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f138`](#insn-00a9f138)

~~~json
{
  "source": "00a9f138",
  "target": "00a9f194",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00a9f13c`](#insn-00a9f13c)

~~~json
{
  "source": "00a9f13c",
  "target": "00440ec0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00a9f194`](#insn-00a9f194)

~~~json
{
  "source": "00a9f194",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
