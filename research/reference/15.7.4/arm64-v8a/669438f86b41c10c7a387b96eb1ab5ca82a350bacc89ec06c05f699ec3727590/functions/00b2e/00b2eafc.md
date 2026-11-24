# 00b2eafc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b2eab8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b2e/00b2eab8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0010.md#compare-d69bf730f29b4f01433bbffc148a448a)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b95f48`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b95/00b95f48.md) · 移動量 `+0x6744c`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0063.md#compare-c18607f040e06ff7c7a63542a1c502c9)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b2eafc",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE15__emplace_multiIJRKNS_4pairIKS7_SA_EEEEENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEEDpOT_",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eb969f3f73bece37a74bd71567e41be6cbd4f3c6fb1f7ab0f52048107312dbaf",
  "source_text_sha256": "eb969f3f73bece37a74bd71567e41be6cbd4f3c6fb1f7ab0f52048107312dbaf",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b2eafc",
        "00b2ec2f"
      ]
    ],
    "bytes_sha256": "dc4d3bedc192637332b51821d5d3e4f34c60b68f8764482c25de1647f91e236d",
    "instruction_count": 77,
    "instruction_bytes": 308,
    "body_bytes": 308,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdff70](../00bdf/00bdff70.md)

## 呼び出し先

- [00bdb040](../00bdb/00bdb040.md)
- [00bdb200](../00bdb/00bdb200.md)
- [00bde730](../00bde/00bde730.md)
- [00bde760](../00bde/00bde760.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2738 bytes

~~~c

undefined8 *
_ZNSt6__ndk16__treeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPN11flatbuffers7EnumDefEEENS_19__map_value_compareIS7_SB_NS_4lessIS7_EELb1EEENS5_ISB_EEE15__emplace_multiIJRKNS_4pairIKS7_SA_EEEEENS_15__tree_iteratorISB_PNS_11__tree_nodeISB_PvEElEEDpOT_
          (long *param_1,long param_2)

{
  void *__s1;
  ulong uVar1;
  size_t __n;
  byte bVar2;
  ulong uVar3;
  int iVar4;
  undefined8 *puVar5;
  undefined8 *puVar6;
  long *plVar7;
  void *__s2;
  long *plVar8;
  long *plVar9;
  
                    /* try { // try from 00b2eb00 to 00c2eb0b has its CatchHandler @ 00b2f8ec */
                    /* try { // try from 00b2eb0c to 00c2eb33 has its CatchHandler @ 00b2f8e8 */
  puVar5 = (undefined8 *)_Znwm(0x40);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2ERKS5_(puVar5 + 4,param_2);
                    /* try { // try from 00b2eb34 to 00c2ec07 has its CatchHandler @ 00b2c3b0 */
  puVar5[7] = *(undefined8 *)(param_2 + 0x18);
  plVar7 = param_1 + 1;
  plVar8 = (long *)*plVar7;
  plVar9 = plVar7;
  if (plVar8 != (long *)0x0) {
    uVar3 = (ulong)(*(byte *)(puVar5 + 4) >> 1);
    __s1 = (void *)((long)puVar5 + 0x21);
    if ((*(byte *)(puVar5 + 4) & 1) != 0) {
      uVar3 = puVar5[5];
      __s1 = (void *)puVar5[6];
    }
    do {
      while( true ) {
        plVar9 = plVar8;
        bVar2 = *(byte *)(plVar9 + 4);
        uVar1 = (ulong)(bVar2 >> 1);
        if ((bVar2 & 1) != 0) {
          uVar1 = plVar9[5];
        }
        __n = uVar1;
        if (uVar3 <= uVar1) {
          __n = uVar3;
        }
        if (__n == 0) break;
        __s2 = (void *)plVar9[6];
        if ((bVar2 & 1) == 0) {
          __s2 = (void *)((long)plVar9 + 0x21);
        }
        iVar4 = memcmp(__s1,__s2,__n);
        if (iVar4 == 0) break;
        if (-1 < iVar4) goto LAB_00b2eb64;
LAB_00b2ebb0:
        plVar7 = plVar9;
        plVar8 = (long *)*plVar9;
        if ((long *)*plVar9 == (long *)0x0) goto LAB_00b2ebdc;
      }
      if (uVar3 < uVar1) goto LAB_00b2ebb0;
LAB_00b2eb64:
      plVar8 = (long *)plVar9[1];
    } while ((long *)plVar9[1] != (long *)0x0);
    plVar7 = plVar9 + 1;
  }
LAB_00b2ebdc:
  *puVar5 = 0;
  puVar5[1] = 0;
  puVar5[2] = plVar9;
  *plVar7 = (long)puVar5;
  puVar6 = puVar5;
  if (*(long *)*param_1 != 0) {
    *param_1 = *(long *)*param_1;
    puVar6 = (undefined8 *)*plVar7;
  }
                    /* try { // try from 00b2ec08 to 00c2ec13 has its CatchHandler @ 00b2f8e0 */
  _ZNSt6__ndk127__tree_balance_after_insertIPNS_16__tree_node_baseIPvEEEEvT_S5_(param_1[1],puVar6);
                    /* try { // try from 00b2ec14 to 00c2ec3b has its CatchHandler @ 00b2f8dc */
  param_1[2] = param_1[2] + 1;
  return puVar5;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b2eafc"></a> `00b2eafc` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00b2eb00"></a> `00b2eb00` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2eb04"></a> `00b2eb04` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2eb08"></a> `00b2eb08` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2eb0c"></a> `00b2eb0c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b2eb10"></a> `00b2eb10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b2eb14"></a> `00b2eb14` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00b2eb18"></a> `00b2eb18` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00b2eb1c"></a> `00b2eb1c` | `49 b1 02 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00b2eb20"></a> `00b2eb20` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b2eb24"></a> `00b2eb24` | `00 80 00 91` | add x0,x0,#0x20 | `FALL_THROUGH`
<a id="insn-00b2eb28"></a> `00b2eb28` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b2eb2c"></a> `00b2eb2c` | `01 bf 02 94` | bl 0x00bde730 | `UNCONDITIONAL_CALL`
<a id="insn-00b2eb30"></a> `00b2eb30` | `a8 0e 40 f9` | ldr x8,[x21, #0x18] | `FALL_THROUGH`
<a id="insn-00b2eb34"></a> `00b2eb34` | `88 1e 00 f9` | str x8,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00b2eb38"></a> `00b2eb38` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-00b2eb3c"></a> `00b2eb3c` | `16 8d 40 f8` | ldr x22,[x8, #0x8]! | `FALL_THROUGH`
<a id="insn-00b2eb40"></a> `00b2eb40` | `56 04 00 b4` | cbz x22,0x00b2ebc8 | `CONDITIONAL_JUMP`
<a id="insn-00b2eb44"></a> `00b2eb44` | `88 82 40 39` | ldrb w8,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00b2eb48"></a> `00b2eb48` | `8a ae 42 a9` | ldp x10,x11,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b2eb4c"></a> `00b2eb4c` | `89 86 00 91` | add x9,x20,#0x21 | `FALL_THROUGH`
<a id="insn-00b2eb50"></a> `00b2eb50` | `0c fd 41 d3` | lsr x12,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b2eb54"></a> `00b2eb54` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b2eb58"></a> `00b2eb58` | `97 01 8a 9a` | csel x23,x12,x10,eq | `FALL_THROUGH`
<a id="insn-00b2eb5c"></a> `00b2eb5c` | `35 01 8b 9a` | csel x21,x9,x11,eq | `FALL_THROUGH`
<a id="insn-00b2eb60"></a> `00b2eb60` | `04 00 00 14` | b 0x00b2eb70 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2eb64"></a> `00b2eb64` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00b2eb68"></a> `00b2eb68` | `48 03 00 b4` | cbz x8,0x00b2ebd0 | `CONDITIONAL_JUMP`
<a id="insn-00b2eb6c"></a> `00b2eb6c` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00b2eb70"></a> `00b2eb70` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00b2eb74"></a> `00b2eb74` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00b2eb78"></a> `00b2eb78` | `0a 05 40 f9` | ldr x10,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b2eb7c"></a> `00b2eb7c` | `2b fd 41 d3` | lsr x11,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b2eb80"></a> `00b2eb80` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b2eb84"></a> `00b2eb84` | `78 01 8a 9a` | csel x24,x11,x10,eq | `FALL_THROUGH`
<a id="insn-00b2eb88"></a> `00b2eb88` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00b2eb8c"></a> `00b2eb8c` | `02 33 97 9a` | csel x2,x24,x23,cc | `FALL_THROUGH`
<a id="insn-00b2eb90"></a> `00b2eb90` | `62 01 00 b4` | cbz x2,0x00b2ebbc | `CONDITIONAL_JUMP`
<a id="insn-00b2eb94"></a> `00b2eb94` | `ca 1a 40 f9` | ldr x10,[x22, #0x30] | `FALL_THROUGH`
<a id="insn-00b2eb98"></a> `00b2eb98` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b2eb9c"></a> `00b2eb9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00b2eba0"></a> `00b2eba0` | `41 15 88 9a` | csinc x1,x10,x8,ne | `FALL_THROUGH`
<a id="insn-00b2eba4"></a> `00b2eba4` | `97 b1 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b2eba8"></a> `00b2eba8` | `a0 00 00 34` | cbz w0,0x00b2ebbc | `CONDITIONAL_JUMP`
<a id="insn-00b2ebac"></a> `00b2ebac` | `c0 fd ff 36` | tbz w0,#0x1f,0x00b2eb64 | `CONDITIONAL_JUMP`
<a id="insn-00b2ebb0"></a> `00b2ebb0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00b2ebb4"></a> `00b2ebb4` | `c8 fd ff b5` | cbnz x8,0x00b2eb6c | `CONDITIONAL_JUMP`
<a id="insn-00b2ebb8"></a> `00b2ebb8` | `08 00 00 14` | b 0x00b2ebd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ebbc"></a> `00b2ebbc` | `ff 02 18 eb` | cmp x23,x24 | `FALL_THROUGH`
<a id="insn-00b2ebc0"></a> `00b2ebc0` | `22 fd ff 54` | b.cs 0x00b2eb64 | `CONDITIONAL_JUMP`
<a id="insn-00b2ebc4"></a> `00b2ebc4` | `fb ff ff 17` | b 0x00b2ebb0 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ebc8"></a> `00b2ebc8` | `f6 03 08 aa` | mov x22,x8 | `FALL_THROUGH`
<a id="insn-00b2ebcc"></a> `00b2ebcc` | `04 00 00 14` | b 0x00b2ebdc | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ebd0"></a> `00b2ebd0` | `c8 22 00 91` | add x8,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00b2ebd4"></a> `00b2ebd4` | `02 00 00 14` | b 0x00b2ebdc | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ebd8"></a> `00b2ebd8` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00b2ebdc"></a> `00b2ebdc` | `9f 7e 00 a9` | stp xzr,xzr,[x20] | `FALL_THROUGH`
<a id="insn-00b2ebe0"></a> `00b2ebe0` | `96 0a 00 f9` | str x22,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ebe4"></a> `00b2ebe4` | `14 01 00 f9` | str x20,[x8] | `FALL_THROUGH`
<a id="insn-00b2ebe8"></a> `00b2ebe8` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00b2ebec"></a> `00b2ebec` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00b2ebf0"></a> `00b2ebf0` | `89 00 00 b4` | cbz x9,0x00b2ec00 | `CONDITIONAL_JUMP`
<a id="insn-00b2ebf4"></a> `00b2ebf4` | `69 02 00 f9` | str x9,[x19] | `FALL_THROUGH`
<a id="insn-00b2ebf8"></a> `00b2ebf8` | `01 01 40 f9` | ldr x1,[x8] | `FALL_THROUGH`
<a id="insn-00b2ebfc"></a> `00b2ebfc` | `02 00 00 14` | b 0x00b2ec04 | `UNCONDITIONAL_JUMP`
<a id="insn-00b2ec00"></a> `00b2ec00` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b2ec04"></a> `00b2ec04` | `60 06 40 f9` | ldr x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00b2ec08"></a> `00b2ec08` | `d6 be 02 94` | bl 0x00bde760 | `UNCONDITIONAL_CALL`
<a id="insn-00b2ec0c"></a> `00b2ec0c` | `68 0a 40 f9` | ldr x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ec10"></a> `00b2ec10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b2ec14"></a> `00b2ec14` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b2ec18"></a> `00b2ec18` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ec1c"></a> `00b2ec1c` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b2ec20"></a> `00b2ec20` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b2ec24"></a> `00b2ec24` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b2ec28"></a> `00b2ec28` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b2ec2c"></a> `00b2ec2c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b2eafc`](#insn-00b2eafc) 範囲 `[['00b2eafc', '00b2eaff']]`
  - `FALL_THROUGH` [`00b2eafc`](#insn-00b2eafc) → [`00b2eb00`](#insn-00b2eb00)
- ブロック [`00b2eb00`](#insn-00b2eb00) 範囲 `[['00b2eb00', '00b2eb0b']]`
  - `FALL_THROUGH` [`00b2eb08`](#insn-00b2eb08) → [`00b2eb0c`](#insn-00b2eb0c)
- ブロック [`00b2eb0c`](#insn-00b2eb0c) 範囲 `[['00b2eb0c', '00b2eb33']]`
  - `FALL_THROUGH` [`00b2eb30`](#insn-00b2eb30) → [`00b2eb34`](#insn-00b2eb34)
- ブロック [`00b2eb34`](#insn-00b2eb34) 範囲 `[['00b2eb34', '00b2eb43']]`
  - `CONDITIONAL_JUMP` [`00b2eb40`](#insn-00b2eb40) → [`00b2ebc8`](#insn-00b2ebc8)
  - `FALL_THROUGH` [`00b2eb40`](#insn-00b2eb40) → [`00b2eb44`](#insn-00b2eb44)
- ブロック [`00b2eb44`](#insn-00b2eb44) 範囲 `[['00b2eb44', '00b2eb63']]`
  - `UNCONDITIONAL_JUMP` [`00b2eb60`](#insn-00b2eb60) → [`00b2eb70`](#insn-00b2eb70)
- ブロック [`00b2eb64`](#insn-00b2eb64) 範囲 `[['00b2eb64', '00b2eb6b']]`
  - `CONDITIONAL_JUMP` [`00b2eb68`](#insn-00b2eb68) → [`00b2ebd0`](#insn-00b2ebd0)
  - `FALL_THROUGH` [`00b2eb68`](#insn-00b2eb68) → [`00b2eb6c`](#insn-00b2eb6c)
- ブロック [`00b2eb6c`](#insn-00b2eb6c) 範囲 `[['00b2eb6c', '00b2eb6f']]`
  - `FALL_THROUGH` [`00b2eb6c`](#insn-00b2eb6c) → [`00b2eb70`](#insn-00b2eb70)
- ブロック [`00b2eb70`](#insn-00b2eb70) 範囲 `[['00b2eb70', '00b2eb93']]`
  - `CONDITIONAL_JUMP` [`00b2eb90`](#insn-00b2eb90) → [`00b2ebbc`](#insn-00b2ebbc)
  - `FALL_THROUGH` [`00b2eb90`](#insn-00b2eb90) → [`00b2eb94`](#insn-00b2eb94)
- ブロック [`00b2eb94`](#insn-00b2eb94) 範囲 `[['00b2eb94', '00b2ebab']]`
  - `CONDITIONAL_JUMP` [`00b2eba8`](#insn-00b2eba8) → [`00b2ebbc`](#insn-00b2ebbc)
  - `FALL_THROUGH` [`00b2eba8`](#insn-00b2eba8) → [`00b2ebac`](#insn-00b2ebac)
- ブロック [`00b2ebac`](#insn-00b2ebac) 範囲 `[['00b2ebac', '00b2ebaf']]`
  - `CONDITIONAL_JUMP` [`00b2ebac`](#insn-00b2ebac) → [`00b2eb64`](#insn-00b2eb64)
  - `FALL_THROUGH` [`00b2ebac`](#insn-00b2ebac) → [`00b2ebb0`](#insn-00b2ebb0)
- ブロック [`00b2ebb0`](#insn-00b2ebb0) 範囲 `[['00b2ebb0', '00b2ebb7']]`
  - `CONDITIONAL_JUMP` [`00b2ebb4`](#insn-00b2ebb4) → [`00b2eb6c`](#insn-00b2eb6c)
  - `FALL_THROUGH` [`00b2ebb4`](#insn-00b2ebb4) → [`00b2ebb8`](#insn-00b2ebb8)
- ブロック [`00b2ebb8`](#insn-00b2ebb8) 範囲 `[['00b2ebb8', '00b2ebbb']]`
  - `UNCONDITIONAL_JUMP` [`00b2ebb8`](#insn-00b2ebb8) → [`00b2ebd8`](#insn-00b2ebd8)
- ブロック [`00b2ebbc`](#insn-00b2ebbc) 範囲 `[['00b2ebbc', '00b2ebc3']]`
  - `CONDITIONAL_JUMP` [`00b2ebc0`](#insn-00b2ebc0) → [`00b2eb64`](#insn-00b2eb64)
  - `FALL_THROUGH` [`00b2ebc0`](#insn-00b2ebc0) → [`00b2ebc4`](#insn-00b2ebc4)
- ブロック [`00b2ebc4`](#insn-00b2ebc4) 範囲 `[['00b2ebc4', '00b2ebc7']]`
  - `UNCONDITIONAL_JUMP` [`00b2ebc4`](#insn-00b2ebc4) → [`00b2ebb0`](#insn-00b2ebb0)
- ブロック [`00b2ebc8`](#insn-00b2ebc8) 範囲 `[['00b2ebc8', '00b2ebcf']]`
  - `UNCONDITIONAL_JUMP` [`00b2ebcc`](#insn-00b2ebcc) → [`00b2ebdc`](#insn-00b2ebdc)
- ブロック [`00b2ebd0`](#insn-00b2ebd0) 範囲 `[['00b2ebd0', '00b2ebd7']]`
  - `UNCONDITIONAL_JUMP` [`00b2ebd4`](#insn-00b2ebd4) → [`00b2ebdc`](#insn-00b2ebdc)
- ブロック [`00b2ebd8`](#insn-00b2ebd8) 範囲 `[['00b2ebd8', '00b2ebdb']]`
  - `FALL_THROUGH` [`00b2ebd8`](#insn-00b2ebd8) → [`00b2ebdc`](#insn-00b2ebdc)
- ブロック [`00b2ebdc`](#insn-00b2ebdc) 範囲 `[['00b2ebdc', '00b2ebf3']]`
  - `CONDITIONAL_JUMP` [`00b2ebf0`](#insn-00b2ebf0) → [`00b2ec00`](#insn-00b2ec00)
  - `FALL_THROUGH` [`00b2ebf0`](#insn-00b2ebf0) → [`00b2ebf4`](#insn-00b2ebf4)
- ブロック [`00b2ebf4`](#insn-00b2ebf4) 範囲 `[['00b2ebf4', '00b2ebff']]`
  - `UNCONDITIONAL_JUMP` [`00b2ebfc`](#insn-00b2ebfc) → [`00b2ec04`](#insn-00b2ec04)
- ブロック [`00b2ec00`](#insn-00b2ec00) 範囲 `[['00b2ec00', '00b2ec03']]`
  - `FALL_THROUGH` [`00b2ec00`](#insn-00b2ec00) → [`00b2ec04`](#insn-00b2ec04)
- ブロック [`00b2ec04`](#insn-00b2ec04) 範囲 `[['00b2ec04', '00b2ec07']]`
  - `FALL_THROUGH` [`00b2ec04`](#insn-00b2ec04) → [`00b2ec08`](#insn-00b2ec08)
- ブロック [`00b2ec08`](#insn-00b2ec08) 範囲 `[['00b2ec08', '00b2ec13']]`
  - `FALL_THROUGH` [`00b2ec10`](#insn-00b2ec10) → [`00b2ec14`](#insn-00b2ec14)
- ブロック [`00b2ec14`](#insn-00b2ec14) 範囲 `[['00b2ec14', '00b2ec2f']]`

## 命令位置別の参照

- [`00b2eafc`](#insn-00b2eafc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2eb00`](#insn-00b2eb00) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2eb04`](#insn-00b2eb04) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2eb08`](#insn-00b2eb08) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2eb1c`](#insn-00b2eb1c) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00b2eb2c`](#insn-00b2eb2c) → [`00bde730`](../00bde/00bde730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde730` · 推定シンボル `None` · 推定型 `None`
- [`00b2eb40`](#insn-00b2eb40) → [`00b2ebc8`](#insn-00b2ebc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2eb60`](#insn-00b2eb60) → [`00b2eb70`](#insn-00b2eb70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2eb68`](#insn-00b2eb68) → [`00b2ebd0`](#insn-00b2ebd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2eb90`](#insn-00b2eb90) → [`00b2ebbc`](#insn-00b2ebbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2eba4`](#insn-00b2eba4) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b2eba8`](#insn-00b2eba8) → [`00b2ebbc`](#insn-00b2ebbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebac`](#insn-00b2ebac) → [`00b2eb64`](#insn-00b2eb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebb4`](#insn-00b2ebb4) → [`00b2eb6c`](#insn-00b2eb6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebb8`](#insn-00b2ebb8) → [`00b2ebd8`](#insn-00b2ebd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebc0`](#insn-00b2ebc0) → [`00b2eb64`](#insn-00b2eb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebc4`](#insn-00b2ebc4) → [`00b2ebb0`](#insn-00b2ebb0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebcc`](#insn-00b2ebcc) → [`00b2ebdc`](#insn-00b2ebdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebd4`](#insn-00b2ebd4) → [`00b2ebdc`](#insn-00b2ebdc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebf0`](#insn-00b2ebf0) → [`00b2ec00`](#insn-00b2ec00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ebfc`](#insn-00b2ebfc) → [`00b2ec04`](#insn-00b2ec04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec08`](#insn-00b2ec08) → [`00bde760`](../00bde/00bde760.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde760` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec1c`](#insn-00b2ec1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec20`](#insn-00b2ec20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b2ec24`](#insn-00b2ec24) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b2eafc`](#insn-00b2eafc)

~~~json
{
  "source": "00b2eafc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2eb00`](#insn-00b2eb00)

~~~json
{
  "source": "00b2eb00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2eb04`](#insn-00b2eb04)

~~~json
{
  "source": "00b2eb04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2eb08`](#insn-00b2eb08)

~~~json
{
  "source": "00b2eb08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2eb1c`](#insn-00b2eb1c)

~~~json
{
  "source": "00b2eb1c",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2eb2c`](#insn-00b2eb2c)

~~~json
{
  "source": "00b2eb2c",
  "target": "00bde730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2eb40`](#insn-00b2eb40)

~~~json
{
  "source": "00b2eb40",
  "target": "00b2ebc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2eb60`](#insn-00b2eb60)

~~~json
{
  "source": "00b2eb60",
  "target": "00b2eb70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2eb68`](#insn-00b2eb68)

~~~json
{
  "source": "00b2eb68",
  "target": "00b2ebd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2eb90`](#insn-00b2eb90)

~~~json
{
  "source": "00b2eb90",
  "target": "00b2ebbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2eba4`](#insn-00b2eba4)

~~~json
{
  "source": "00b2eba4",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2eba8`](#insn-00b2eba8)

~~~json
{
  "source": "00b2eba8",
  "target": "00b2ebbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebac`](#insn-00b2ebac)

~~~json
{
  "source": "00b2ebac",
  "target": "00b2eb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebb4`](#insn-00b2ebb4)

~~~json
{
  "source": "00b2ebb4",
  "target": "00b2eb6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebb8`](#insn-00b2ebb8)

~~~json
{
  "source": "00b2ebb8",
  "target": "00b2ebd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebc0`](#insn-00b2ebc0)

~~~json
{
  "source": "00b2ebc0",
  "target": "00b2eb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebc4`](#insn-00b2ebc4)

~~~json
{
  "source": "00b2ebc4",
  "target": "00b2ebb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebcc`](#insn-00b2ebcc)

~~~json
{
  "source": "00b2ebcc",
  "target": "00b2ebdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebd4`](#insn-00b2ebd4)

~~~json
{
  "source": "00b2ebd4",
  "target": "00b2ebdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebf0`](#insn-00b2ebf0)

~~~json
{
  "source": "00b2ebf0",
  "target": "00b2ec00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ebfc`](#insn-00b2ebfc)

~~~json
{
  "source": "00b2ebfc",
  "target": "00b2ec04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ec08`](#insn-00b2ec08)

~~~json
{
  "source": "00b2ec08",
  "target": "00bde760",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b2ec1c`](#insn-00b2ec1c)

~~~json
{
  "source": "00b2ec1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ec20`](#insn-00b2ec20)

~~~json
{
  "source": "00b2ec20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b2ec24`](#insn-00b2ec24)

~~~json
{
  "source": "00b2ec24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
