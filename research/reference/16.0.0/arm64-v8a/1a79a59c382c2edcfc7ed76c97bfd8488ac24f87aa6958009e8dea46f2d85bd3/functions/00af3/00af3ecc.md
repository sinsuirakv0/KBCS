# 00af3ecc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0166.md#review-19a9a24d5b88141c847f0c62c0f42350)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00af42f4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00af4/00af42f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0065.md#compare-d0abc833c242c4562182c6a35920911b)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af3ecc",
  "name": "FUN_00af3ecc",
  "size": 740,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "7ee441d4aa745da94cea0cac763539eef90b56bdd8fd04ffc9c9b43662eb2ba1",
  "source_text_sha256": "7ee441d4aa745da94cea0cac763539eef90b56bdd8fd04ffc9c9b43662eb2ba1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af3ecc",
        "00af41af"
      ]
    ],
    "bytes_sha256": "81c672e095fb6130cc615bcad8def3ae8b5ab795a38437d321bae0fa4be5b0af",
    "instruction_count": 185,
    "instruction_bytes": 740,
    "body_bytes": 740,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00af4220](../00af4/00af4220.md)
- [00af42cc](../00af4/00af42cc.md)

## 呼び出し先

- [0046e6ec](../0046e/0046e6ec.md)
- [0046e76c](../0046e/0046e76c.md)
- [0046e774](../0046e/0046e774.md)
- [0046e77c](../0046e/0046e77c.md)
- [004700ec](../00470/004700ec.md)
- [005e0c80](../005e0/005e0c80.md)
- [005e0eac](../005e0/005e0eac.md)
- [005e2ac8](../005e2/005e2ac8.md)
- [005e73e0](../005e7/005e73e0.md)
- [0067d0c0](../0067d/0067d0c0.md)
- [008514b8](../00851/008514b8.md)
- [00c57ae0](../00c57/00c57ae0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3411 bytes

~~~c

void FUN_00af3ecc(undefined8 param_1,int param_2,int param_3)

{
  int iVar1;
  int iVar2;
  long lVar3;
  int iVar4;
  undefined4 uVar5;
  uint uVar6;
  undefined4 uVar7;
  int iVar8;
  long lVar9;
  undefined8 uVar10;
  undefined8 uVar11;
  undefined8 uVar12;
  ulong uVar13;
  int extraout_w1;
  int extraout_w1_00;
  int extraout_w1_01;
  int local_70 [2];
  long local_68;
  
  lVar3 = tpidr_el0;
  local_68 = *(long *)(lVar3 + 0x28);
  uVar5 = FUN_005e0eac(param_2,param_3);
  lVar9 = FUN_008514b8();
  uVar6 = FUN_005e73e0(lVar9 + (long)param_2 * 0x1f0 + 0x2768);
  uVar10 = FUN_005e2ac8(param_1,param_2,uVar5);
  FUN_004700ec(uVar10,uVar6 & 1);
  uVar10 = FUN_0046e76c();
  uVar11 = FUN_005e2ac8(param_1,param_2,uVar5);
  uVar12 = FUN_005e2ac8(param_1,param_2,uVar5);
  FUN_004700ec(uVar12,uVar6 & 1);
  uVar7 = FUN_0046e774();
  uVar12 = FUN_005e2ac8(param_1,param_2,uVar5);
  FUN_004700ec(uVar12,uVar6 & 1);
  uVar5 = FUN_0046e77c();
  FUN_0046e6ec(uVar10,uVar11,uVar7,uVar5,local_70);
  if (param_2 == 0) {
    lVar9 = FUN_008514b8();
    iVar1 = *(int *)(lVar9 + 0x9f690);
    lVar9 = FUN_008514b8();
    *(int *)(lVar9 + (long)param_3 * 0x3ec + 0x84940) = iVar1 + local_70[0] * -0x14;
  }
  else {
    lVar9 = FUN_008514b8();
    *(int *)(lVar9 + (long)param_2 * 0xc804 + (long)param_3 * 0x3ec + 0x84940) = local_70[0] * 10;
    if (param_2 == 1) {
      lVar9 = FUN_008514b8();
      uVar13 = FUN_005e73e0(lVar9 + 0x2958);
      if ((uVar13 & 1) == 0) {
        lVar9 = FUN_008514b8();
        if (*(int *)(lVar9 + (long)param_3 * 0x3ec + 0x911cc) != 0) {
          lVar9 = FUN_008514b8();
          iVar1 = *(int *)(lVar9 + 0x910d8);
          lVar9 = FUN_008514b8();
          uVar5 = FUN_005e0c80();
                    /* try { // try from 00af405c to 00bf40df has its CatchHandler @ 00af405c
                       catch() { ... } // from try @ 00af405c with catch @ 00af405c
                       catch() { ... } // from try @ 00af40f4 with catch @ 00af405c */
          FUN_0067d0c0((long)&fde_table_entry_00333a08.initial_loc + lVar9,uVar5);
          iVar4 = (int)((ulong)((long)(extraout_w1 * 0x49c) * -0x51eb851f) >> 0x20);
          lVar9 = FUN_008514b8();
          uVar5 = FUN_005e0c80();
          iVar8 = FUN_0067d0c0((long)&fde_table_entry_00333a08.initial_loc + lVar9,uVar5);
          lVar9 = FUN_008514b8();
          uVar5 = FUN_005e0c80();
          FUN_0067d0c0((long)&fde_table_entry_00333a08.initial_loc + lVar9,uVar5);
          lVar9 = FUN_008514b8();
          uVar5 = FUN_005e0c80();
                    /* try { // try from 00af40e0 to 00bf40f3 has its CatchHandler @ 00af4124 */
          FUN_0067d0c0((long)&fde_table_entry_00333a08.initial_loc + lVar9,uVar5);
                    /* try { // try from 00af40f4 to 00bf4143 has its CatchHandler @ 00af405c */
          lVar9 = FUN_008514b8();
          iVar2 = *(int *)(lVar9 + (long)param_3 * 0x3ec + 0x91144);
                    /* catch() { ... } // from try @ 00af40e0 with catch @ 00af4124 */
          lVar9 = FUN_008514b8();
          *(int *)(lVar9 + (long)param_3 * 0x3ec + 0x91144) =
               ((iVar4 >> 5) - (iVar4 >> 0x1f)) + iVar1 + (extraout_w1_00 * iVar8) / 10 + iVar2 +
               (extraout_w1_01 * 0x7f) / 10;
        }
      }
    }
  }
  if (*(long *)(lVar3 + 0x28) == local_68) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af3ecc"></a> `00af3ecc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00af3ed0"></a> `00af3ed0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3ed4"></a> `00af3ed4` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af3ed8"></a> `00af3ed8` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af3edc"></a> `00af3edc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00af3ee0"></a> `00af3ee0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00af3ee4"></a> `00af3ee4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00af3ee8"></a> `00af3ee8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00af3eec"></a> `00af3eec` | `5b d0 3b d5` | mrs x27,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00af3ef0"></a> `00af3ef0` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00af3ef4"></a> `00af3ef4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00af3ef8"></a> `00af3ef8` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00af3efc"></a> `00af3efc` | `e0 03 01 2a` | mov w0,w1 | `FALL_THROUGH`
<a id="insn-00af3f00"></a> `00af3f00` | `e1 03 02 2a` | mov w1,w2 | `FALL_THROUGH`
<a id="insn-00af3f04"></a> `00af3f04` | `f3 03 02 2a` | mov w19,w2 | `FALL_THROUGH`
<a id="insn-00af3f08"></a> `00af3f08` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00af3f0c"></a> `00af3f0c` | `e8 b3 eb 97` | bl 0x005e0eac | `UNCONDITIONAL_CALL`
<a id="insn-00af3f10"></a> `00af3f10` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00af3f14"></a> `00af3f14` | `69 75 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af3f18"></a> `00af3f18` | `08 3e 80 52` | mov w8,#0x1f0 | `FALL_THROUGH`
<a id="insn-00af3f1c"></a> `00af3f1c` | `09 ed 84 52` | mov w9,#0x2768 | `FALL_THROUGH`
<a id="insn-00af3f20"></a> `00af3f20` | `9c 7e 40 93` | sxtw x28,w20 | `FALL_THROUGH`
<a id="insn-00af3f24"></a> `00af3f24` | `88 02 28 9b` | smaddl x8,w20,w8,x0 | `FALL_THROUGH`
<a id="insn-00af3f28"></a> `00af3f28` | `00 01 09 8b` | add x0,x8,x9 | `FALL_THROUGH`
<a id="insn-00af3f2c"></a> `00af3f2c` | `2d cd eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00af3f30"></a> `00af3f30` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00af3f34"></a> `00af3f34` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af3f38"></a> `00af3f38` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00af3f3c"></a> `00af3f3c` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00af3f40"></a> `00af3f40` | `e2 ba eb 97` | bl 0x005e2ac8 | `UNCONDITIONAL_CALL`
<a id="insn-00af3f44"></a> `00af3f44` | `e1 02 00 12` | and w1,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00af3f48"></a> `00af3f48` | `69 f0 e5 97` | bl 0x004700ec | `UNCONDITIONAL_CALL`
<a id="insn-00af3f4c"></a> `00af3f4c` | `08 ea e5 97` | bl 0x0046e76c | `UNCONDITIONAL_CALL`
<a id="insn-00af3f50"></a> `00af3f50` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00af3f54"></a> `00af3f54` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af3f58"></a> `00af3f58` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00af3f5c"></a> `00af3f5c` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00af3f60"></a> `00af3f60` | `da ba eb 97` | bl 0x005e2ac8 | `UNCONDITIONAL_CALL`
<a id="insn-00af3f64"></a> `00af3f64` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00af3f68"></a> `00af3f68` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af3f6c"></a> `00af3f6c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00af3f70"></a> `00af3f70` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00af3f74"></a> `00af3f74` | `d5 ba eb 97` | bl 0x005e2ac8 | `UNCONDITIONAL_CALL`
<a id="insn-00af3f78"></a> `00af3f78` | `e1 02 00 12` | and w1,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00af3f7c"></a> `00af3f7c` | `5c f0 e5 97` | bl 0x004700ec | `UNCONDITIONAL_CALL`
<a id="insn-00af3f80"></a> `00af3f80` | `fd e9 e5 97` | bl 0x0046e774 | `UNCONDITIONAL_CALL`
<a id="insn-00af3f84"></a> `00af3f84` | `fa 03 00 2a` | mov w26,w0 | `FALL_THROUGH`
<a id="insn-00af3f88"></a> `00af3f88` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00af3f8c"></a> `00af3f8c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00af3f90"></a> `00af3f90` | `e2 03 16 2a` | mov w2,w22 | `FALL_THROUGH`
<a id="insn-00af3f94"></a> `00af3f94` | `cd ba eb 97` | bl 0x005e2ac8 | `UNCONDITIONAL_CALL`
<a id="insn-00af3f98"></a> `00af3f98` | `e1 02 00 12` | and w1,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00af3f9c"></a> `00af3f9c` | `54 f0 e5 97` | bl 0x004700ec | `UNCONDITIONAL_CALL`
<a id="insn-00af3fa0"></a> `00af3fa0` | `f7 e9 e5 97` | bl 0x0046e77c | `UNCONDITIONAL_CALL`
<a id="insn-00af3fa4"></a> `00af3fa4` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-00af3fa8"></a> `00af3fa8` | `e4 03 00 91` | mov x4,sp | `FALL_THROUGH`
<a id="insn-00af3fac"></a> `00af3fac` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00af3fb0"></a> `00af3fb0` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00af3fb4"></a> `00af3fb4` | `e2 03 1a 2a` | mov w2,w26 | `FALL_THROUGH`
<a id="insn-00af3fb8"></a> `00af3fb8` | `cd e9 e5 97` | bl 0x0046e6ec | `UNCONDITIONAL_CALL`
<a id="insn-00af3fbc"></a> `00af3fbc` | `34 0c 00 34` | cbz w20,0x00af4140 | `CONDITIONAL_JUMP`
<a id="insn-00af3fc0"></a> `00af3fc0` | `e8 03 40 b9` | ldr w8,[sp] | `FALL_THROUGH`
<a id="insn-00af3fc4"></a> `00af3fc4` | `08 09 08 0b` | add w8,w8,w8, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00af3fc8"></a> `00af3fc8` | `15 79 1f 53` | lsl w21,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00af3fcc"></a> `00af3fcc` | `3b 75 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af3fd0"></a> `00af3fd0` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af3fd4"></a> `00af3fd4` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af3fd8"></a> `00af3fd8` | `9f 06 00 71` | cmp w20,#0x1 | `FALL_THROUGH`
<a id="insn-00af3fdc"></a> `00af3fdc` | `88 03 28 9b` | smaddl x8,w28,w8,x0 | `FALL_THROUGH`
<a id="insn-00af3fe0"></a> `00af3fe0` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00af3fe4"></a> `00af3fe4` | `09 28 89 52` | mov w9,#0x4940 | `FALL_THROUGH`
<a id="insn-00af3fe8"></a> `00af3fe8` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af3fec"></a> `00af3fec` | `15 69 29 b8` | str w21,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af3ff0"></a> `00af3ff0` | `61 0c 00 54` | b.ne 0x00af417c | `CONDITIONAL_JUMP`
<a id="insn-00af3ff4"></a> `00af3ff4` | `31 75 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af3ff8"></a> `00af3ff8` | `08 2b 85 52` | mov w8,#0x2958 | `FALL_THROUGH`
<a id="insn-00af3ffc"></a> `00af3ffc` | `00 00 08 8b` | add x0,x0,x8 | `FALL_THROUGH`
<a id="insn-00af4000"></a> `00af4000` | `f8 cc eb 97` | bl 0x005e73e0 | `UNCONDITIONAL_CALL`
<a id="insn-00af4004"></a> `00af4004` | `c0 0b 00 37` | tbnz w0,#0x0,0x00af417c | `CONDITIONAL_JUMP`
<a id="insn-00af4008"></a> `00af4008` | `75 7e 40 93` | sxtw x21,w19 | `FALL_THROUGH`
<a id="insn-00af400c"></a> `00af400c` | `2b 75 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af4010"></a> `00af4010` | `88 7d 80 52` | mov w8,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4014"></a> `00af4014` | `89 39 82 52` | mov w9,#0x11cc | `FALL_THROUGH`
<a id="insn-00af4018"></a> `00af4018` | `a8 02 28 9b` | smaddl x8,w21,w8,x0 | `FALL_THROUGH`
<a id="insn-00af401c"></a> `00af401c` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4020"></a> `00af4020` | `08 69 69 b8` | ldr w8,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4024"></a> `00af4024` | `c8 0a 00 34` | cbz w8,0x00af417c | `CONDITIONAL_JUMP`
<a id="insn-00af4028"></a> `00af4028` | `24 75 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af402c"></a> `00af402c` | `96 00 99 52` | mov w22,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4030"></a> `00af4030` | `89 1a 89 52` | mov w9,#0x48d4 | `FALL_THROUGH`
<a id="insn-00af4034"></a> `00af4034` | `88 03 36 9b` | smaddl x8,w28,w22,x0 | `FALL_THROUGH`
<a id="insn-00af4038"></a> `00af4038` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af403c"></a> `00af403c` | `17 69 69 b8` | ldr w23,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4040"></a> `00af4040` | `1e 75 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af4044"></a> `00af4044` | `19 41 87 52` | mov w25,#0x3a08 | `FALL_THROUGH`
<a id="insn-00af4048"></a> `00af4048` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af404c"></a> `00af404c` | `79 06 a0 72` | movk w25,#0x33, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4050"></a> `00af4050` | `0c b3 eb 97` | bl 0x005e0c80 | `UNCONDITIONAL_CALL`
<a id="insn-00af4054"></a> `00af4054` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00af4058"></a> `00af4058` | `60 02 19 8b` | add x0,x19,x25 | `FALL_THROUGH`
<a id="insn-00af405c"></a> `00af405c` | `19 24 ee 97` | bl 0x0067d0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00af4060"></a> `00af4060` | `88 93 80 52` | mov w8,#0x49c | `FALL_THROUGH`
<a id="insn-00af4064"></a> `00af4064` | `29 5c 8f 52` | mov w9,#0x7ae1 | `FALL_THROUGH`
<a id="insn-00af4068"></a> `00af4068` | `28 7c 08 1b` | mul w8,w1,w8 | `FALL_THROUGH`
<a id="insn-00af406c"></a> `00af406c` | `89 c2 b5 72` | movk w9,#0xae14, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4070"></a> `00af4070` | `08 7d 29 9b` | smull x8,w8,w9 | `FALL_THROUGH`
<a id="insn-00af4074"></a> `00af4074` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00af4078"></a> `00af4078` | `08 fd 65 93` | asr x8,x8,#0x25 | `FALL_THROUGH`
<a id="insn-00af407c"></a> `00af407c` | `18 01 09 0b` | add w24,w8,w9 | `FALL_THROUGH`
<a id="insn-00af4080"></a> `00af4080` | `0e 75 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af4084"></a> `00af4084` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af4088"></a> `00af4088` | `fe b2 eb 97` | bl 0x005e0c80 | `UNCONDITIONAL_CALL`
<a id="insn-00af408c"></a> `00af408c` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00af4090"></a> `00af4090` | `60 02 19 8b` | add x0,x19,x25 | `FALL_THROUGH`
<a id="insn-00af4094"></a> `00af4094` | `0b 24 ee 97` | bl 0x0067d0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00af4098"></a> `00af4098` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af409c"></a> `00af409c` | `07 75 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af40a0"></a> `00af40a0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00af40a4"></a> `00af40a4` | `f7 b2 eb 97` | bl 0x005e0c80 | `UNCONDITIONAL_CALL`
<a id="insn-00af40a8"></a> `00af40a8` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00af40ac"></a> `00af40ac` | `80 02 19 8b` | add x0,x20,x25 | `FALL_THROUGH`
<a id="insn-00af40b0"></a> `00af40b0` | `04 24 ee 97` | bl 0x0067d0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00af40b4"></a> `00af40b4` | `28 7c 13 1b` | mul w8,w1,w19 | `FALL_THROUGH`
<a id="insn-00af40b8"></a> `00af40b8` | `f4 cc 8c 52` | mov w20,#0x6667 | `FALL_THROUGH`
<a id="insn-00af40bc"></a> `00af40bc` | `d4 cc ac 72` | movk w20,#0x6666, LSL #16 | `FALL_THROUGH`
<a id="insn-00af40c0"></a> `00af40c0` | `08 7d 34 9b` | smull x8,w8,w20 | `FALL_THROUGH`
<a id="insn-00af40c4"></a> `00af40c4` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00af40c8"></a> `00af40c8` | `08 fd 62 93` | asr x8,x8,#0x22 | `FALL_THROUGH`
<a id="insn-00af40cc"></a> `00af40cc` | `1a 01 09 0b` | add w26,w8,w9 | `FALL_THROUGH`
<a id="insn-00af40d0"></a> `00af40d0` | `fa 74 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af40d4"></a> `00af40d4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af40d8"></a> `00af40d8` | `ea b2 eb 97` | bl 0x005e0c80 | `UNCONDITIONAL_CALL`
<a id="insn-00af40dc"></a> `00af40dc` | `e1 03 00 2a` | mov w1,w0 | `FALL_THROUGH`
<a id="insn-00af40e0"></a> `00af40e0` | `60 02 19 8b` | add x0,x19,x25 | `FALL_THROUGH`
<a id="insn-00af40e4"></a> `00af40e4` | `f7 23 ee 97` | bl 0x0067d0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00af40e8"></a> `00af40e8` | `28 60 19 53` | lsl w8,w1,#0x7 | `FALL_THROUGH`
<a id="insn-00af40ec"></a> `00af40ec` | `08 01 01 4b` | sub w8,w8,w1 | `FALL_THROUGH`
<a id="insn-00af40f0"></a> `00af40f0` | `08 7d 34 9b` | smull x8,w8,w20 | `FALL_THROUGH`
<a id="insn-00af40f4"></a> `00af40f4` | `09 fd 7f d3` | lsr x9,x8,#0x3f | `FALL_THROUGH`
<a id="insn-00af40f8"></a> `00af40f8` | `08 fd 62 93` | asr x8,x8,#0x22 | `FALL_THROUGH`
<a id="insn-00af40fc"></a> `00af40fc` | `13 01 09 0b` | add w19,w8,w9 | `FALL_THROUGH`
<a id="insn-00af4100"></a> `00af4100` | `ee 74 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af4104"></a> `00af4104` | `88 03 36 9b` | smaddl x8,w28,w22,x0 | `FALL_THROUGH`
<a id="insn-00af4108"></a> `00af4108` | `94 7d 80 52` | mov w20,#0x3ec | `FALL_THROUGH`
<a id="insn-00af410c"></a> `00af410c` | `19 28 89 52` | mov w25,#0x4940 | `FALL_THROUGH`
<a id="insn-00af4110"></a> `00af4110` | `a8 22 34 9b` | smaddl x8,w21,w20,x8 | `FALL_THROUGH`
<a id="insn-00af4114"></a> `00af4114` | `19 01 a0 72` | movk w25,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4118"></a> `00af4118` | `09 03 17 0b` | add w9,w24,w23 | `FALL_THROUGH`
<a id="insn-00af411c"></a> `00af411c` | `08 69 79 b8` | ldr w8,[x8, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4120"></a> `00af4120` | `48 03 08 0b` | add w8,w26,w8 | `FALL_THROUGH`
<a id="insn-00af4124"></a> `00af4124` | `28 01 08 0b` | add w8,w9,w8 | `FALL_THROUGH`
<a id="insn-00af4128"></a> `00af4128` | `13 01 13 0b` | add w19,w8,w19 | `FALL_THROUGH`
<a id="insn-00af412c"></a> `00af412c` | `e3 74 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af4130"></a> `00af4130` | `88 03 36 9b` | smaddl x8,w28,w22,x0 | `FALL_THROUGH`
<a id="insn-00af4134"></a> `00af4134` | `a8 22 34 9b` | smaddl x8,w21,w20,x8 | `FALL_THROUGH`
<a id="insn-00af4138"></a> `00af4138` | `13 69 39 b8` | str w19,[x8, x25, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af413c"></a> `00af413c` | `10 00 00 14` | b 0x00af417c | `UNCONDITIONAL_JUMP`
<a id="insn-00af4140"></a> `00af4140` | `de 74 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af4144"></a> `00af4144` | `e8 03 40 b9` | ldr w8,[sp] | `FALL_THROUGH`
<a id="insn-00af4148"></a> `00af4148` | `09 d2 9e 52` | mov w9,#0xf690 | `FALL_THROUGH`
<a id="insn-00af414c"></a> `00af414c` | `6a 02 80 12` | mov w10,#0xffffffec | `FALL_THROUGH`
<a id="insn-00af4150"></a> `00af4150` | `29 01 a0 72` | movk w9,#0x9, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4154"></a> `00af4154` | `09 68 69 b8` | ldr w9,[x0, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af4158"></a> `00af4158` | `14 25 0a 1b` | madd w20,w8,w10,w9 | `FALL_THROUGH`
<a id="insn-00af415c"></a> `00af415c` | `d7 74 f5 97` | bl 0x008514b8 | `UNCONDITIONAL_CALL`
<a id="insn-00af4160"></a> `00af4160` | `88 00 99 52` | mov w8,#0xc804 | `FALL_THROUGH`
<a id="insn-00af4164"></a> `00af4164` | `89 7d 80 52` | mov w9,#0x3ec | `FALL_THROUGH`
<a id="insn-00af4168"></a> `00af4168` | `88 03 28 9b` | smaddl x8,w28,w8,x0 | `FALL_THROUGH`
<a id="insn-00af416c"></a> `00af416c` | `68 22 29 9b` | smaddl x8,w19,w9,x8 | `FALL_THROUGH`
<a id="insn-00af4170"></a> `00af4170` | `09 28 89 52` | mov w9,#0x4940 | `FALL_THROUGH`
<a id="insn-00af4174"></a> `00af4174` | `09 01 a0 72` | movk w9,#0x8, LSL #16 | `FALL_THROUGH`
<a id="insn-00af4178"></a> `00af4178` | `14 69 29 b8` | str w20,[x8, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00af417c"></a> `00af417c` | `68 17 40 f9` | ldr x8,[x27, #0x28] | `FALL_THROUGH`
<a id="insn-00af4180"></a> `00af4180` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00af4184"></a> `00af4184` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00af4188"></a> `00af4188` | `21 01 00 54` | b.ne 0x00af41ac | `CONDITIONAL_JUMP`
<a id="insn-00af418c"></a> `00af418c` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00af4190"></a> `00af4190` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00af4194"></a> `00af4194` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00af4198"></a> `00af4198` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af419c"></a> `00af419c` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af41a0"></a> `00af41a0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af41a4"></a> `00af41a4` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00af41a8"></a> `00af41a8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00af41ac"></a> `00af41ac` | `4d 8e 05 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af3ecc`](#insn-00af3ecc) 範囲 `[['00af3ecc', '00af3fbf']]`
  - `CONDITIONAL_JUMP` [`00af3fbc`](#insn-00af3fbc) → [`00af4140`](#insn-00af4140)
  - `FALL_THROUGH` [`00af3fbc`](#insn-00af3fbc) → [`00af3fc0`](#insn-00af3fc0)
- ブロック [`00af3fc0`](#insn-00af3fc0) 範囲 `[['00af3fc0', '00af3ff3']]`
  - `CONDITIONAL_JUMP` [`00af3ff0`](#insn-00af3ff0) → [`00af417c`](#insn-00af417c)
  - `FALL_THROUGH` [`00af3ff0`](#insn-00af3ff0) → [`00af3ff4`](#insn-00af3ff4)
- ブロック [`00af3ff4`](#insn-00af3ff4) 範囲 `[['00af3ff4', '00af4007']]`
  - `CONDITIONAL_JUMP` [`00af4004`](#insn-00af4004) → [`00af417c`](#insn-00af417c)
  - `FALL_THROUGH` [`00af4004`](#insn-00af4004) → [`00af4008`](#insn-00af4008)
- ブロック [`00af4008`](#insn-00af4008) 範囲 `[['00af4008', '00af4027']]`
  - `CONDITIONAL_JUMP` [`00af4024`](#insn-00af4024) → [`00af417c`](#insn-00af417c)
  - `FALL_THROUGH` [`00af4024`](#insn-00af4024) → [`00af4028`](#insn-00af4028)
- ブロック [`00af4028`](#insn-00af4028) 範囲 `[['00af4028', '00af405b']]`
  - `FALL_THROUGH` [`00af4058`](#insn-00af4058) → [`00af405c`](#insn-00af405c)
- ブロック [`00af405c`](#insn-00af405c) 範囲 `[['00af405c', '00af40df']]`
  - `FALL_THROUGH` [`00af40dc`](#insn-00af40dc) → [`00af40e0`](#insn-00af40e0)
- ブロック [`00af40e0`](#insn-00af40e0) 範囲 `[['00af40e0', '00af40f3']]`
  - `FALL_THROUGH` [`00af40f0`](#insn-00af40f0) → [`00af40f4`](#insn-00af40f4)
- ブロック [`00af40f4`](#insn-00af40f4) 範囲 `[['00af40f4', '00af4123']]`
  - `FALL_THROUGH` [`00af4120`](#insn-00af4120) → [`00af4124`](#insn-00af4124)
- ブロック [`00af4124`](#insn-00af4124) 範囲 `[['00af4124', '00af413f']]`
  - `UNCONDITIONAL_JUMP` [`00af413c`](#insn-00af413c) → [`00af417c`](#insn-00af417c)
- ブロック [`00af4140`](#insn-00af4140) 範囲 `[['00af4140', '00af417b']]`
  - `FALL_THROUGH` [`00af4178`](#insn-00af4178) → [`00af417c`](#insn-00af417c)
- ブロック [`00af417c`](#insn-00af417c) 範囲 `[['00af417c', '00af418b']]`
  - `CONDITIONAL_JUMP` [`00af4188`](#insn-00af4188) → [`00af41ac`](#insn-00af41ac)
  - `FALL_THROUGH` [`00af4188`](#insn-00af4188) → [`00af418c`](#insn-00af418c)
- ブロック [`00af418c`](#insn-00af418c) 範囲 `[['00af418c', '00af41ab']]`
- ブロック [`00af41ac`](#insn-00af41ac) 範囲 `[['00af41ac', '00af41af']]`

## 命令位置別の参照

- [`00af3ed0`](#insn-00af3ed0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3ed4`](#insn-00af3ed4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3ed8`](#insn-00af3ed8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3edc`](#insn-00af3edc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3ee0`](#insn-00af3ee0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3ee4`](#insn-00af3ee4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3f08`](#insn-00af3f08) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3f0c`](#insn-00af3f0c) → [`005e0eac`](../005e0/005e0eac.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e0eac` · 推定シンボル `None` · 推定型 `None`
- [`00af3f14`](#insn-00af3f14) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af3f2c`](#insn-00af3f2c) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00af3f40`](#insn-00af3f40) → [`005e2ac8`](../005e2/005e2ac8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e2ac8` · 推定シンボル `None` · 推定型 `None`
- [`00af3f48`](#insn-00af3f48) → [`004700ec`](../00470/004700ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004700ec` · 推定シンボル `None` · 推定型 `None`
- [`00af3f4c`](#insn-00af3f4c) → [`0046e76c`](../0046e/0046e76c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e76c` · 推定シンボル `None` · 推定型 `None`
- [`00af3f60`](#insn-00af3f60) → [`005e2ac8`](../005e2/005e2ac8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e2ac8` · 推定シンボル `None` · 推定型 `None`
- [`00af3f74`](#insn-00af3f74) → [`005e2ac8`](../005e2/005e2ac8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e2ac8` · 推定シンボル `None` · 推定型 `None`
- [`00af3f7c`](#insn-00af3f7c) → [`004700ec`](../00470/004700ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004700ec` · 推定シンボル `None` · 推定型 `None`
- [`00af3f80`](#insn-00af3f80) → [`0046e774`](../0046e/0046e774.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e774` · 推定シンボル `None` · 推定型 `None`
- [`00af3f94`](#insn-00af3f94) → [`005e2ac8`](../005e2/005e2ac8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e2ac8` · 推定シンボル `None` · 推定型 `None`
- [`00af3f9c`](#insn-00af3f9c) → [`004700ec`](../00470/004700ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004700ec` · 推定シンボル `None` · 推定型 `None`
- [`00af3fa0`](#insn-00af3fa0) → [`0046e77c`](../0046e/0046e77c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e77c` · 推定シンボル `None` · 推定型 `None`
- [`00af3fb8`](#insn-00af3fb8) → [`0046e6ec`](../0046e/0046e6ec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0046e6ec` · 推定シンボル `None` · 推定型 `None`
- [`00af3fbc`](#insn-00af3fbc) → [`00af4140`](#insn-00af4140) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3fc0`](#insn-00af3fc0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3fcc`](#insn-00af3fcc) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af3ff0`](#insn-00af3ff0) → [`00af417c`](#insn-00af417c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3ff4`](#insn-00af3ff4) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af4000`](#insn-00af4000) → [`005e73e0`](../005e7/005e73e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e73e0` · 推定シンボル `None` · 推定型 `None`
- [`00af4004`](#insn-00af4004) → [`00af417c`](#insn-00af417c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af400c`](#insn-00af400c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af4024`](#insn-00af4024) → [`00af417c`](#insn-00af417c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4028`](#insn-00af4028) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af4040`](#insn-00af4040) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af4050`](#insn-00af4050) → [`005e0c80`](../005e0/005e0c80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e0c80` · 推定シンボル `None` · 推定型 `None`
- [`00af405c`](#insn-00af405c) → [`0067d0c0`](../0067d/0067d0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0067d0c0` · 推定シンボル `None` · 推定型 `None`
- [`00af4080`](#insn-00af4080) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af4088`](#insn-00af4088) → [`005e0c80`](../005e0/005e0c80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e0c80` · 推定シンボル `None` · 推定型 `None`
- [`00af4094`](#insn-00af4094) → [`0067d0c0`](../0067d/0067d0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0067d0c0` · 推定シンボル `None` · 推定型 `None`
- [`00af409c`](#insn-00af409c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af40a4`](#insn-00af40a4) → [`005e0c80`](../005e0/005e0c80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e0c80` · 推定シンボル `None` · 推定型 `None`
- [`00af40b0`](#insn-00af40b0) → [`0067d0c0`](../0067d/0067d0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0067d0c0` · 推定シンボル `None` · 推定型 `None`
- [`00af40d0`](#insn-00af40d0) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af40d8`](#insn-00af40d8) → [`005e0c80`](../005e0/005e0c80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005e0c80` · 推定シンボル `None` · 推定型 `None`
- [`00af40e4`](#insn-00af40e4) → [`0067d0c0`](../0067d/0067d0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0067d0c0` · 推定シンボル `None` · 推定型 `None`
- [`00af4100`](#insn-00af4100) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af412c`](#insn-00af412c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af413c`](#insn-00af413c) → [`00af417c`](#insn-00af417c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4140`](#insn-00af4140) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af4144`](#insn-00af4144) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af415c`](#insn-00af415c) → [`008514b8`](../00851/008514b8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514b8` · 推定シンボル `None` · 推定型 `None`
- [`00af4180`](#insn-00af4180) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4188`](#insn-00af4188) → [`00af41ac`](#insn-00af41ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af418c`](#insn-00af418c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4190`](#insn-00af4190) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4194`](#insn-00af4194) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af4198`](#insn-00af4198) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af419c`](#insn-00af419c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af41a0`](#insn-00af41a0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af41ac`](#insn-00af41ac) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af3ed0`](#insn-00af3ed0)

~~~json
{
  "source": "00af3ed0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3ed4`](#insn-00af3ed4)

~~~json
{
  "source": "00af3ed4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3ed8`](#insn-00af3ed8)

~~~json
{
  "source": "00af3ed8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3edc`](#insn-00af3edc)

~~~json
{
  "source": "00af3edc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3ee0`](#insn-00af3ee0)

~~~json
{
  "source": "00af3ee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3ee4`](#insn-00af3ee4)

~~~json
{
  "source": "00af3ee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3f08`](#insn-00af3f08)

~~~json
{
  "source": "00af3f08",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3f0c`](#insn-00af3f0c)

~~~json
{
  "source": "00af3f0c",
  "target": "005e0eac",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f14`](#insn-00af3f14)

~~~json
{
  "source": "00af3f14",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f2c`](#insn-00af3f2c)

~~~json
{
  "source": "00af3f2c",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f40`](#insn-00af3f40)

~~~json
{
  "source": "00af3f40",
  "target": "005e2ac8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f48`](#insn-00af3f48)

~~~json
{
  "source": "00af3f48",
  "target": "004700ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f4c`](#insn-00af3f4c)

~~~json
{
  "source": "00af3f4c",
  "target": "0046e76c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f60`](#insn-00af3f60)

~~~json
{
  "source": "00af3f60",
  "target": "005e2ac8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f74`](#insn-00af3f74)

~~~json
{
  "source": "00af3f74",
  "target": "005e2ac8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f7c`](#insn-00af3f7c)

~~~json
{
  "source": "00af3f7c",
  "target": "004700ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f80`](#insn-00af3f80)

~~~json
{
  "source": "00af3f80",
  "target": "0046e774",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f94`](#insn-00af3f94)

~~~json
{
  "source": "00af3f94",
  "target": "005e2ac8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3f9c`](#insn-00af3f9c)

~~~json
{
  "source": "00af3f9c",
  "target": "004700ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3fa0`](#insn-00af3fa0)

~~~json
{
  "source": "00af3fa0",
  "target": "0046e77c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3fb8`](#insn-00af3fb8)

~~~json
{
  "source": "00af3fb8",
  "target": "0046e6ec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3fbc`](#insn-00af3fbc)

~~~json
{
  "source": "00af3fbc",
  "target": "00af4140",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3fc0`](#insn-00af3fc0)

~~~json
{
  "source": "00af3fc0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3fcc`](#insn-00af3fcc)

~~~json
{
  "source": "00af3fcc",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3ff0`](#insn-00af3ff0)

~~~json
{
  "source": "00af3ff0",
  "target": "00af417c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3ff4`](#insn-00af3ff4)

~~~json
{
  "source": "00af3ff4",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4000`](#insn-00af4000)

~~~json
{
  "source": "00af4000",
  "target": "005e73e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4004`](#insn-00af4004)

~~~json
{
  "source": "00af4004",
  "target": "00af417c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af400c`](#insn-00af400c)

~~~json
{
  "source": "00af400c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4024`](#insn-00af4024)

~~~json
{
  "source": "00af4024",
  "target": "00af417c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4028`](#insn-00af4028)

~~~json
{
  "source": "00af4028",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4040`](#insn-00af4040)

~~~json
{
  "source": "00af4040",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4050`](#insn-00af4050)

~~~json
{
  "source": "00af4050",
  "target": "005e0c80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af405c`](#insn-00af405c)

~~~json
{
  "source": "00af405c",
  "target": "0067d0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4080`](#insn-00af4080)

~~~json
{
  "source": "00af4080",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4088`](#insn-00af4088)

~~~json
{
  "source": "00af4088",
  "target": "005e0c80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4094`](#insn-00af4094)

~~~json
{
  "source": "00af4094",
  "target": "0067d0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af409c`](#insn-00af409c)

~~~json
{
  "source": "00af409c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af40a4`](#insn-00af40a4)

~~~json
{
  "source": "00af40a4",
  "target": "005e0c80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af40b0`](#insn-00af40b0)

~~~json
{
  "source": "00af40b0",
  "target": "0067d0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af40d0`](#insn-00af40d0)

~~~json
{
  "source": "00af40d0",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af40d8`](#insn-00af40d8)

~~~json
{
  "source": "00af40d8",
  "target": "005e0c80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af40e4`](#insn-00af40e4)

~~~json
{
  "source": "00af40e4",
  "target": "0067d0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4100`](#insn-00af4100)

~~~json
{
  "source": "00af4100",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af412c`](#insn-00af412c)

~~~json
{
  "source": "00af412c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af413c`](#insn-00af413c)

~~~json
{
  "source": "00af413c",
  "target": "00af417c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4140`](#insn-00af4140)

~~~json
{
  "source": "00af4140",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4144`](#insn-00af4144)

~~~json
{
  "source": "00af4144",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af415c`](#insn-00af415c)

~~~json
{
  "source": "00af415c",
  "target": "008514b8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af4180`](#insn-00af4180)

~~~json
{
  "source": "00af4180",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4188`](#insn-00af4188)

~~~json
{
  "source": "00af4188",
  "target": "00af41ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af418c`](#insn-00af418c)

~~~json
{
  "source": "00af418c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4190`](#insn-00af4190)

~~~json
{
  "source": "00af4190",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4194`](#insn-00af4194)

~~~json
{
  "source": "00af4194",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af4198`](#insn-00af4198)

~~~json
{
  "source": "00af4198",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af419c`](#insn-00af419c)

~~~json
{
  "source": "00af419c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af41a0`](#insn-00af41a0)

~~~json
{
  "source": "00af41a0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af41ac`](#insn-00af41ac)

~~~json
{
  "source": "00af41ac",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
