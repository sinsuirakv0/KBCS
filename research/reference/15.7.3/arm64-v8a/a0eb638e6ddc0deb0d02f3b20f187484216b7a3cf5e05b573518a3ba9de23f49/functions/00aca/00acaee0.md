# 00acaee0

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00acae18`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aca/00acae18.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-966b9e508915a0cbad5642eb7086c923)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00acaf24`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aca/00acaf24.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0007.md#compare-6da3f0b786e0c05acb406fd879a13c03)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00acaee0",
  "name": "FUN_00acaee0",
  "size": 328,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0e87c586ccda3cde0e5cfce03e0c9676ec366ffd3c282a439a78d4b40c991adf",
  "source_text_sha256": "0e87c586ccda3cde0e5cfce03e0c9676ec366ffd3c282a439a78d4b40c991adf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00acaee0",
        "00acb023"
      ],
      [
        "00acb048",
        "00acb04b"
      ]
    ],
    "bytes_sha256": "4ed9470ab1ab15d290808a41c8fd8d17e18ac94ad52fe4b26a253b5d2ab68180",
    "instruction_count": 82,
    "instruction_bytes": 328,
    "body_bytes": 328,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00abf52c](../00abf/00abf52c.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [005c3468](../005c3/005c3468.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1743 bytes

~~~c

long * FUN_00acaee0(long *param_1,int *param_2,undefined8 param_3,undefined8 *param_4)

{
  undefined4 uVar1;
  long lVar2;
  long *plVar3;
  long *plVar4;
  undefined8 uVar5;
  long lVar6;
  long *plVar7;
  long *plVar8;
  
  lVar2 = tpidr_el0;
  lVar6 = *(long *)(lVar2 + 0x28);
  plVar7 = param_1 + 1;
  plVar8 = plVar7;
  if ((long *)*plVar7 != (long *)0x0) {
    plVar3 = (long *)*plVar7;
    do {
      while (plVar4 = plVar3, plVar7 = plVar4, (int)plVar4[4] <= *param_2) {
        if (*param_2 <= (int)plVar4[4]) {
          uVar5 = 0;
          goto LAB_00acaff4;
        }
        plVar3 = (long *)plVar4[1];
        if ((long *)plVar4[1] == (long *)0x0) {
          plVar8 = plVar4 + 1;
          goto LAB_00acaf5c;
        }
      }
      plVar3 = (long *)*plVar4;
      plVar8 = plVar4;
    } while ((long *)*plVar4 != (long *)0x0);
  }
LAB_00acaf5c:
  plVar4 = (long *)_Znwm(0x60);
  uVar1 = *(undefined4 *)*param_4;
  plVar4[0xb] = 0;
  *(undefined4 *)(plVar4 + 4) = uVar1;
  plVar4[10] = 0;
  plVar4[9] = 0;
  plVar4[8] = 0;
  plVar4[7] = 0;
  plVar4[6] = 0;
  plVar4[5] = 0;
  FUN_005c3468((long)plVar4 + 0x2c);
  *(undefined4 *)((long)plVar4 + 0x34) = 0;
  FUN_005c3468();
  plVar4[8] = 0;
  plVar4[9] = 0;
  plVar4[10] = 0;
  *plVar4 = 0;
  plVar4[1] = 0;
  plVar4[2] = (long)plVar7;
  *plVar8 = (long)plVar4;
  plVar7 = plVar4;
  if (*(long *)*param_1 != 0) {
    *param_1 = *(long *)*param_1;
    plVar7 = (long *)*plVar8;
  }
  plVar7 = (long *)FUN_00419064(param_1[1],plVar7);
  uVar5 = 1;
  param_1[2] = param_1[2] + 1;
  param_1 = plVar7;
LAB_00acaff4:
  if (*(long *)(lVar2 + 0x28) == lVar6) {
    return plVar4;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(param_1,uVar5);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00acaee0"></a> `00acaee0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acaee4"></a> `00acaee4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acaee8"></a> `00acaee8` | `f9 1b 00 f9` | str x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acaeec"></a> `00acaeec` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acaef0"></a> `00acaef0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acaef4"></a> `00acaef4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acaef8"></a> `00acaef8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00acaefc"></a> `00acaefc` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00acaf00"></a> `00acaf00` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00acaf04"></a> `00acaf04` | `f6 03 03 aa` | mov x22,x3 | `FALL_THROUGH`
<a id="insn-00acaf08"></a> `00acaf08` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00acaf0c"></a> `00acaf0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00acaf10"></a> `00acaf10` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acaf14"></a> `00acaf14` | `29 8f 40 f8` | ldr x9,[x25, #0x8]! | `FALL_THROUGH`
<a id="insn-00acaf18"></a> `00acaf18` | `f8 03 19 aa` | mov x24,x25 | `FALL_THROUGH`
<a id="insn-00acaf1c"></a> `00acaf1c` | `f4 03 19 aa` | mov x20,x25 | `FALL_THROUGH`
<a id="insn-00acaf20"></a> `00acaf20` | `e9 01 00 b4` | cbz x9,0x00acaf5c | `CONDITIONAL_JUMP`
<a id="insn-00acaf24"></a> `00acaf24` | `28 00 40 b9` | ldr w8,[x1] | `FALL_THROUGH`
<a id="insn-00acaf28"></a> `00acaf28` | `04 00 00 14` | b 0x00acaf38 | `UNCONDITIONAL_JUMP`
<a id="insn-00acaf2c"></a> `00acaf2c` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00acaf30"></a> `00acaf30` | `f8 03 14 aa` | mov x24,x20 | `FALL_THROUGH`
<a id="insn-00acaf34"></a> `00acaf34` | `49 01 00 b4` | cbz x9,0x00acaf5c | `CONDITIONAL_JUMP`
<a id="insn-00acaf38"></a> `00acaf38` | `f4 03 09 aa` | mov x20,x9 | `FALL_THROUGH`
<a id="insn-00acaf3c"></a> `00acaf3c` | `29 21 40 b9` | ldr w9,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf40"></a> `00acaf40` | `1f 01 09 6b` | cmp w8,w9 | `FALL_THROUGH`
<a id="insn-00acaf44"></a> `00acaf44` | `4b ff ff 54` | b.lt 0x00acaf2c | `CONDITIONAL_JUMP`
<a id="insn-00acaf48"></a> `00acaf48` | `3f 01 08 6b` | cmp w9,w8 | `FALL_THROUGH`
<a id="insn-00acaf4c"></a> `00acaf4c` | `2a 05 00 54` | b.ge 0x00acaff0 | `CONDITIONAL_JUMP`
<a id="insn-00acaf50"></a> `00acaf50` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00acaf54"></a> `00acaf54` | `29 ff ff b5` | cbnz x9,0x00acaf38 | `CONDITIONAL_JUMP`
<a id="insn-00acaf58"></a> `00acaf58` | `98 22 00 91` | add x24,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00acaf5c"></a> `00acaf5c` | `00 0c 80 52` | mov w0,#0x60 | `FALL_THROUGH`
<a id="insn-00acaf60"></a> `00acaf60` | `24 40 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf64"></a> `00acaf64` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00acaf68"></a> `00acaf68` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00acaf6c"></a> `00acaf6c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00acaf70"></a> `00acaf70` | `ff 43 00 39` | strb wzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00acaf74"></a> `00acaf74` | `08 01 40 b9` | ldr w8,[x8] | `FALL_THROUGH`
<a id="insn-00acaf78"></a> `00acaf78` | `e0 67 00 a9` | stp x0,x25,[sp] | `FALL_THROUGH`
<a id="insn-00acaf7c"></a> `00acaf7c` | `1f 2c 00 f9` | str xzr,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00acaf80"></a> `00acaf80` | `08 20 00 b9` | str w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00acaf84"></a> `00acaf84` | `00 80 84 3c` | stur q0,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00acaf88"></a> `00acaf88` | `00 80 83 3c` | stur q0,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00acaf8c"></a> `00acaf8c` | `00 80 82 3c` | stur q0,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00acaf90"></a> `00acaf90` | `00 b0 00 91` | add x0,x0,#0x2c | `FALL_THROUGH`
<a id="insn-00acaf94"></a> `00acaf94` | `35 e1 eb 97` | bl 0x005c3468 | `UNCONDITIONAL_CALL`
<a id="insn-00acaf98"></a> `00acaf98` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00acaf9c"></a> `00acaf9c` | `1f 4c 03 b8` | str wzr,[x0, #0x34]! | `FALL_THROUGH`
<a id="insn-00acafa0"></a> `00acafa0` | `32 e1 eb 97` | bl 0x005c3468 | `UNCONDITIONAL_CALL`
<a id="insn-00acafa4"></a> `00acafa4` | `bf 7e 04 a9` | stp xzr,xzr,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00acafa8"></a> `00acafa8` | `bf 2a 00 f9` | str xzr,[x21, #0x50] | `FALL_THROUGH`
<a id="insn-00acafac"></a> `00acafac` | `bf 7e 00 a9` | stp xzr,xzr,[x21] | `FALL_THROUGH`
<a id="insn-00acafb0"></a> `00acafb0` | `b4 0a 00 f9` | str x20,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00acafb4"></a> `00acafb4` | `15 03 00 f9` | str x21,[x24] | `FALL_THROUGH`
<a id="insn-00acafb8"></a> `00acafb8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00acafbc"></a> `00acafbc` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00acafc0"></a> `00acafc0` | `68 00 00 b4` | cbz x8,0x00acafcc | `CONDITIONAL_JUMP`
<a id="insn-00acafc4"></a> `00acafc4` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00acafc8"></a> `00acafc8` | `15 03 40 f9` | ldr x21,[x24] | `FALL_THROUGH`
<a id="insn-00acafcc"></a> `00acafcc` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00acafd0"></a> `00acafd0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00acafd4"></a> `00acafd4` | `24 38 e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00acafd8"></a> `00acafd8` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00acafdc"></a> `00acafdc` | `f4 03 40 f9` | ldr x20,[sp] | `FALL_THROUGH`
<a id="insn-00acafe0"></a> `00acafe0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00acafe4"></a> `00acafe4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00acafe8"></a> `00acafe8` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00acafec"></a> `00acafec` | `02 00 00 14` | b 0x00acaff4 | `UNCONDITIONAL_JUMP`
<a id="insn-00acaff0"></a> `00acaff0` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-00acaff4"></a> `00acaff4` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00acaff8"></a> `00acaff8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00acaffc"></a> `00acaffc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00acb000"></a> `00acb000` | `41 02 00 54` | b.ne 0x00acb048 | `CONDITIONAL_JUMP`
<a id="insn-00acb004"></a> `00acb004` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00acb008"></a> `00acb008` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00acb00c"></a> `00acb00c` | `f9 1b 40 f9` | ldr x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00acb010"></a> `00acb010` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00acb014"></a> `00acb014` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00acb018"></a> `00acb018` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00acb01c"></a> `00acb01c` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00acb020"></a> `00acb020` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00acb048"></a> `00acb048` | `fe 3f 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00acaee0`](#insn-00acaee0) 範囲 `[['00acaee0', '00acaf23']]`
  - `CONDITIONAL_JUMP` [`00acaf20`](#insn-00acaf20) → [`00acaf5c`](#insn-00acaf5c)
  - `FALL_THROUGH` [`00acaf20`](#insn-00acaf20) → [`00acaf24`](#insn-00acaf24)
- ブロック [`00acaf24`](#insn-00acaf24) 範囲 `[['00acaf24', '00acaf2b']]`
  - `UNCONDITIONAL_JUMP` [`00acaf28`](#insn-00acaf28) → [`00acaf38`](#insn-00acaf38)
- ブロック [`00acaf2c`](#insn-00acaf2c) 範囲 `[['00acaf2c', '00acaf37']]`
  - `CONDITIONAL_JUMP` [`00acaf34`](#insn-00acaf34) → [`00acaf5c`](#insn-00acaf5c)
  - `FALL_THROUGH` [`00acaf34`](#insn-00acaf34) → [`00acaf38`](#insn-00acaf38)
- ブロック [`00acaf38`](#insn-00acaf38) 範囲 `[['00acaf38', '00acaf47']]`
  - `CONDITIONAL_JUMP` [`00acaf44`](#insn-00acaf44) → [`00acaf2c`](#insn-00acaf2c)
  - `FALL_THROUGH` [`00acaf44`](#insn-00acaf44) → [`00acaf48`](#insn-00acaf48)
- ブロック [`00acaf48`](#insn-00acaf48) 範囲 `[['00acaf48', '00acaf4f']]`
  - `CONDITIONAL_JUMP` [`00acaf4c`](#insn-00acaf4c) → [`00acaff0`](#insn-00acaff0)
  - `FALL_THROUGH` [`00acaf4c`](#insn-00acaf4c) → [`00acaf50`](#insn-00acaf50)
- ブロック [`00acaf50`](#insn-00acaf50) 範囲 `[['00acaf50', '00acaf57']]`
  - `CONDITIONAL_JUMP` [`00acaf54`](#insn-00acaf54) → [`00acaf38`](#insn-00acaf38)
  - `FALL_THROUGH` [`00acaf54`](#insn-00acaf54) → [`00acaf58`](#insn-00acaf58)
- ブロック [`00acaf58`](#insn-00acaf58) 範囲 `[['00acaf58', '00acaf5b']]`
  - `FALL_THROUGH` [`00acaf58`](#insn-00acaf58) → [`00acaf5c`](#insn-00acaf5c)
- ブロック [`00acaf5c`](#insn-00acaf5c) 範囲 `[['00acaf5c', '00acafc3']]`
  - `CONDITIONAL_JUMP` [`00acafc0`](#insn-00acafc0) → [`00acafcc`](#insn-00acafcc)
  - `FALL_THROUGH` [`00acafc0`](#insn-00acafc0) → [`00acafc4`](#insn-00acafc4)
- ブロック [`00acafc4`](#insn-00acafc4) 範囲 `[['00acafc4', '00acafcb']]`
  - `FALL_THROUGH` [`00acafc8`](#insn-00acafc8) → [`00acafcc`](#insn-00acafcc)
- ブロック [`00acafcc`](#insn-00acafcc) 範囲 `[['00acafcc', '00acafef']]`
  - `UNCONDITIONAL_JUMP` [`00acafec`](#insn-00acafec) → [`00acaff4`](#insn-00acaff4)
- ブロック [`00acaff0`](#insn-00acaff0) 範囲 `[['00acaff0', '00acaff3']]`
  - `FALL_THROUGH` [`00acaff0`](#insn-00acaff0) → [`00acaff4`](#insn-00acaff4)
- ブロック [`00acaff4`](#insn-00acaff4) 範囲 `[['00acaff4', '00acb003']]`
  - `CONDITIONAL_JUMP` [`00acb000`](#insn-00acb000) → [`00acb048`](#insn-00acb048)
  - `FALL_THROUGH` [`00acb000`](#insn-00acb000) → [`00acb004`](#insn-00acb004)
- ブロック [`00acb004`](#insn-00acb004) 範囲 `[['00acb004', '00acb023']]`
- ブロック [`00acb048`](#insn-00acb048) 範囲 `[['00acb048', '00acb04b']]`

## 命令位置別の参照

- [`00acaee4`](#insn-00acaee4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaee8`](#insn-00acaee8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaeec`](#insn-00acaeec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaef0`](#insn-00acaef0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaef4`](#insn-00acaef4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf10`](#insn-00acaf10) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf20`](#insn-00acaf20) → [`00acaf5c`](#insn-00acaf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf28`](#insn-00acaf28) → [`00acaf38`](#insn-00acaf38) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf34`](#insn-00acaf34) → [`00acaf5c`](#insn-00acaf5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf44`](#insn-00acaf44) → [`00acaf2c`](#insn-00acaf2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf4c`](#insn-00acaf4c) → [`00acaff0`](#insn-00acaff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf54`](#insn-00acaf54) → [`00acaf38`](#insn-00acaf38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf60`](#insn-00acaf60) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00acaf70`](#insn-00acaf70) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf78`](#insn-00acaf78) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaf94`](#insn-00acaf94) → [`005c3468`](../005c3/005c3468.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c3468` · 推定シンボル `None` · 推定型 `None`
- [`00acafa0`](#insn-00acafa0) → [`005c3468`](../005c3/005c3468.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `005c3468` · 推定シンボル `None` · 推定型 `None`
- [`00acafc0`](#insn-00acafc0) → [`00acafcc`](#insn-00acafcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafd4`](#insn-00acafd4) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00acafdc`](#insn-00acafdc) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acafec`](#insn-00acafec) → [`00acaff4`](#insn-00acaff4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acaff8`](#insn-00acaff8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb000`](#insn-00acb000) → [`00acb048`](#insn-00acb048) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb008`](#insn-00acb008) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb00c`](#insn-00acb00c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb010`](#insn-00acb010) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb014`](#insn-00acb014) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb018`](#insn-00acb018) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00acb048`](#insn-00acb048) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00acaee4`](#insn-00acaee4)

~~~json
{
  "source": "00acaee4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaee8`](#insn-00acaee8)

~~~json
{
  "source": "00acaee8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaeec`](#insn-00acaeec)

~~~json
{
  "source": "00acaeec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaef0`](#insn-00acaef0)

~~~json
{
  "source": "00acaef0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaef4`](#insn-00acaef4)

~~~json
{
  "source": "00acaef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf10`](#insn-00acaf10)

~~~json
{
  "source": "00acaf10",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf20`](#insn-00acaf20)

~~~json
{
  "source": "00acaf20",
  "target": "00acaf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf28`](#insn-00acaf28)

~~~json
{
  "source": "00acaf28",
  "target": "00acaf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf34`](#insn-00acaf34)

~~~json
{
  "source": "00acaf34",
  "target": "00acaf5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf44`](#insn-00acaf44)

~~~json
{
  "source": "00acaf44",
  "target": "00acaf2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf4c`](#insn-00acaf4c)

~~~json
{
  "source": "00acaf4c",
  "target": "00acaff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf54`](#insn-00acaf54)

~~~json
{
  "source": "00acaf54",
  "target": "00acaf38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf60`](#insn-00acaf60)

~~~json
{
  "source": "00acaf60",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acaf70`](#insn-00acaf70)

~~~json
{
  "source": "00acaf70",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf78`](#insn-00acaf78)

~~~json
{
  "source": "00acaf78",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaf94`](#insn-00acaf94)

~~~json
{
  "source": "00acaf94",
  "target": "005c3468",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acafa0`](#insn-00acafa0)

~~~json
{
  "source": "00acafa0",
  "target": "005c3468",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acafc0`](#insn-00acafc0)

~~~json
{
  "source": "00acafc0",
  "target": "00acafcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafd4`](#insn-00acafd4)

~~~json
{
  "source": "00acafd4",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00acafdc`](#insn-00acafdc)

~~~json
{
  "source": "00acafdc",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acafec`](#insn-00acafec)

~~~json
{
  "source": "00acafec",
  "target": "00acaff4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acaff8`](#insn-00acaff8)

~~~json
{
  "source": "00acaff8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb000`](#insn-00acb000)

~~~json
{
  "source": "00acb000",
  "target": "00acb048",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb008`](#insn-00acb008)

~~~json
{
  "source": "00acb008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb00c`](#insn-00acb00c)

~~~json
{
  "source": "00acb00c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb010`](#insn-00acb010)

~~~json
{
  "source": "00acb010",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb014`](#insn-00acb014)

~~~json
{
  "source": "00acb014",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb018`](#insn-00acb018)

~~~json
{
  "source": "00acb018",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00acb048`](#insn-00acb048)

~~~json
{
  "source": "00acb048",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
