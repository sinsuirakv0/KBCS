# 00bdc9ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdc950`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdc950.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-388c6fbc88571004d7a9166d6f9b7782)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdd9e0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bdd9e0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-5dfa2d220b1bfb14bdc6c4ad06230f2c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdc9ec",
  "name": "_ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__find_equalIS3_EERPNS_16__tree_node_baseIPvEENS_21__tree_const_iteratorIS4_PNS_11__tree_nodeIS4_SE_EElEERPNS_15__tree_end_nodeISG_EESH_RKT_",
  "size": 556,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c75be2148c87863479f9b71a9730792395a7e4bac8c409eccf6536b9c9a7b4fb",
  "source_text_sha256": "c75be2148c87863479f9b71a9730792395a7e4bac8c409eccf6536b9c9a7b4fb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdc9ec",
        "00bdcc17"
      ]
    ],
    "bytes_sha256": "e271dc50cb29b505c6f094260854927495e9ecd2c16b782ae707d8910a653281",
    "instruction_count": 139,
    "instruction_bytes": 556,
    "body_bytes": 556,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5df30](../00c5d/00c5df30.md)

## 呼び出し先

- [00c5b670](../00c5b/00c5b670.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4277 bytes

~~~c

long * _ZNSt6__ndk16__treeINS_12__value_typeIN8firebase7VariantES3_EENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE12__find_equalIS3_EERPNS_16__tree_node_baseIPvEENS_21__tree_const_iteratorIS4_PNS_11__tree_nodeIS4_SE_EElEERPNS_15__tree_end_nodeISG_EESH_RKT_
                 (long *param_1,long *param_2,long *param_3,long *param_4,undefined8 param_5)

{
  bool bVar1;
  ulong uVar2;
  long lVar3;
  long *plVar4;
  long *plVar5;
  long *plVar6;
  long *plVar7;
  
  plVar6 = param_1 + 1;
  if (plVar6 == param_2) {
LAB_00bdca38:
    plVar5 = param_2;
    if ((long *)*param_1 != param_2) {
      plVar7 = (long *)*param_2;
      plVar4 = param_2;
      if ((long *)*param_2 == (long *)0x0) {
        do {
          plVar5 = (long *)plVar4[2];
          bVar1 = (long *)*plVar5 == plVar4;
          plVar4 = plVar5;
        } while (bVar1);
      }
      else {
        do {
          plVar5 = plVar7;
          plVar7 = (long *)plVar5[1];
        } while ((long *)plVar5[1] != (long *)0x0);
      }
      uVar2 = _ZNK8firebase7VariantltERKS0_(plVar5 + 4,param_5);
      if ((uVar2 & 1) == 0) {
        if ((long *)*plVar6 != (long *)0x0) {
          plVar5 = param_1 + 1;
          plVar6 = (long *)*plVar6;
          do {
            while( true ) {
              plVar7 = plVar6;
              uVar2 = _ZNK8firebase7VariantltERKS0_(param_5,plVar7 + 4);
              if ((uVar2 & 1) == 0) break;
              plVar5 = plVar7;
              plVar6 = (long *)*plVar7;
              if ((long *)*plVar7 == (long *)0x0) goto LAB_00bdcb84;
            }
            uVar2 = _ZNK8firebase7VariantltERKS0_(plVar7 + 4,param_5);
            if ((uVar2 & 1) == 0) break;
            plVar5 = plVar7 + 1;
            plVar6 = (long *)*plVar5;
          } while ((long *)*plVar5 != (long *)0x0);
LAB_00bdcbe4:
          *param_3 = (long)plVar7;
          return plVar5;
        }
        goto LAB_00bdcbec;
      }
    }
    if (*param_2 == 0) {
      *param_3 = (long)param_2;
      plVar6 = param_2;
    }
    else {
      *param_3 = (long)plVar5;
      plVar6 = plVar5 + 1;
    }
  }
  else {
                    /* try { // try from 00bdca20 to 00cdca6f has its CatchHandler @ 00bdee44 */
    uVar2 = _ZNK8firebase7VariantltERKS0_(param_5,param_2 + 4);
    if ((uVar2 & 1) != 0) goto LAB_00bdca38;
    uVar2 = _ZNK8firebase7VariantltERKS0_(param_2 + 4,param_5);
    if ((uVar2 & 1) == 0) {
      *param_3 = (long)param_2;
      *param_4 = (long)param_2;
      return param_4;
    }
                    /* try { // try from 00bdca70 to 00cdcb47 has its CatchHandler @ 00bd6fbc */
    plVar5 = (long *)param_2[1];
    if (plVar5 == (long *)0x0) {
      plVar5 = param_2 + 2;
      plVar7 = (long *)*plVar5;
                    /* try { // try from 00bdcb48 to 00cdcb4f has its CatchHandler @ 00bdecfc */
      if ((long *)*plVar7 != param_2) {
        do {
          lVar3 = *plVar5;
                    /* try { // try from 00bdcb50 to 00cdcd03 has its CatchHandler @ 00bd6fbc */
          plVar5 = (long *)(lVar3 + 0x10);
          plVar7 = (long *)*plVar5;
        } while (*plVar7 != lVar3);
      }
    }
    else {
      do {
        plVar7 = plVar5;
        plVar5 = (long *)*plVar7;
      } while ((long *)*plVar7 != (long *)0x0);
    }
    if ((plVar7 == plVar6) ||
       (uVar2 = _ZNK8firebase7VariantltERKS0_(param_5,plVar7 + 4), (uVar2 & 1) != 0)) {
      if (param_2[1] == 0) {
        *param_3 = (long)param_2;
        return param_2 + 1;
      }
LAB_00bdcb84:
      *param_3 = (long)plVar7;
      return plVar7;
    }
    if ((long *)*plVar6 != (long *)0x0) {
      plVar5 = param_1 + 1;
      plVar6 = (long *)*plVar6;
      do {
        while( true ) {
          plVar7 = plVar6;
          uVar2 = _ZNK8firebase7VariantltERKS0_(param_5,plVar7 + 4);
          if ((uVar2 & 1) == 0) break;
          plVar5 = plVar7;
          plVar6 = (long *)*plVar7;
          if ((long *)*plVar7 == (long *)0x0) goto LAB_00bdcb84;
        }
        uVar2 = _ZNK8firebase7VariantltERKS0_(plVar7 + 4,param_5);
        if ((uVar2 & 1) == 0) break;
        plVar5 = plVar7 + 1;
        plVar6 = (long *)*plVar5;
      } while ((long *)*plVar5 != (long *)0x0);
      goto LAB_00bdcbe4;
    }
LAB_00bdcbec:
    *param_3 = (long)plVar6;
  }
  return plVar6;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdc9ec"></a> `00bdc9ec` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bdc9f0"></a> `00bdc9f0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdc9f4"></a> `00bdc9f4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdc9f8"></a> `00bdc9f8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdc9fc"></a> `00bdc9fc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdca00"></a> `00bdca00` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bdca04"></a> `00bdca04` | `19 20 00 91` | add x25,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bdca08"></a> `00bdca08` | `f4 03 04 aa` | mov x20,x4 | `FALL_THROUGH`
<a id="insn-00bdca0c"></a> `00bdca0c` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bdca10"></a> `00bdca10` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdca14"></a> `00bdca14` | `3f 03 01 eb` | cmp x25,x1 | `FALL_THROUGH`
<a id="insn-00bdca18"></a> `00bdca18` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00bdca1c"></a> `00bdca1c` | `e0 00 00 54` | b.eq 0x00bdca38 | `CONDITIONAL_JUMP`
<a id="insn-00bdca20"></a> `00bdca20` | `d8 82 00 91` | add x24,x22,#0x20 | `FALL_THROUGH`
<a id="insn-00bdca24"></a> `00bdca24` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdca28"></a> `00bdca28` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bdca2c"></a> `00bdca2c` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00bdca30"></a> `00bdca30` | `10 fb 01 94` | bl 0x00c5b670 | `UNCONDITIONAL_CALL`
<a id="insn-00bdca34"></a> `00bdca34` | `60 01 00 36` | tbz w0,#0x0,0x00bdca60 | `CONDITIONAL_JUMP`
<a id="insn-00bdca38"></a> `00bdca38` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bdca3c"></a> `00bdca3c` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00bdca40"></a> `00bdca40` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bdca44"></a> `00bdca44` | `80 03 00 54` | b.eq 0x00bdcab4 | `CONDITIONAL_JUMP`
<a id="insn-00bdca48"></a> `00bdca48` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bdca4c"></a> `00bdca4c` | `08 02 00 b4` | cbz x8,0x00bdca8c | `CONDITIONAL_JUMP`
<a id="insn-00bdca50"></a> `00bdca50` | `f5 03 08 aa` | mov x21,x8 | `FALL_THROUGH`
<a id="insn-00bdca54"></a> `00bdca54` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bdca58"></a> `00bdca58` | `c8 ff ff b5` | cbnz x8,0x00bdca50 | `CONDITIONAL_JUMP`
<a id="insn-00bdca5c"></a> `00bdca5c` | `12 00 00 14` | b 0x00bdcaa4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdca60"></a> `00bdca60` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bdca64"></a> `00bdca64` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdca68"></a> `00bdca68` | `02 fb 01 94` | bl 0x00c5b670 | `UNCONDITIONAL_CALL`
<a id="insn-00bdca6c"></a> `00bdca6c` | `00 06 00 36` | tbz w0,#0x0,0x00bdcb2c | `CONDITIONAL_JUMP`
<a id="insn-00bdca70"></a> `00bdca70` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00bdca74"></a> `00bdca74` | `a8 8e 40 f8` | ldr x8,[x21, #0x8]! | `FALL_THROUGH`
<a id="insn-00bdca78"></a> `00bdca78` | `08 06 00 b4` | cbz x8,0x00bdcb38 | `CONDITIONAL_JUMP`
<a id="insn-00bdca7c"></a> `00bdca7c` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00bdca80"></a> `00bdca80` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bdca84"></a> `00bdca84` | `c8 ff ff b5` | cbnz x8,0x00bdca7c | `CONDITIONAL_JUMP`
<a id="insn-00bdca88"></a> `00bdca88` | `37 00 00 14` | b 0x00bdcb64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdca8c"></a> `00bdca8c` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00bdca90"></a> `00bdca90` | `e8 03 15 aa` | mov x8,x21 | `FALL_THROUGH`
<a id="insn-00bdca94"></a> `00bdca94` | `b5 0a 40 f9` | ldr x21,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bdca98"></a> `00bdca98` | `a9 02 40 f9` | ldr x9,[x21] | `FALL_THROUGH`
<a id="insn-00bdca9c"></a> `00bdca9c` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bdcaa0"></a> `00bdcaa0` | `80 ff ff 54` | b.eq 0x00bdca90 | `CONDITIONAL_JUMP`
<a id="insn-00bdcaa4"></a> `00bdcaa4` | `a0 82 00 91` | add x0,x21,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcaa8"></a> `00bdcaa8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdcaac"></a> `00bdcaac` | `f1 fa 01 94` | bl 0x00c5b670 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcab0"></a> `00bdcab0` | `c0 00 00 36` | tbz w0,#0x0,0x00bdcac8 | `CONDITIONAL_JUMP`
<a id="insn-00bdcab4"></a> `00bdcab4` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bdcab8"></a> `00bdcab8` | `48 03 00 b4` | cbz x8,0x00bdcb20 | `CONDITIONAL_JUMP`
<a id="insn-00bdcabc"></a> `00bdcabc` | `75 02 00 f9` | str x21,[x19] | `FALL_THROUGH`
<a id="insn-00bdcac0"></a> `00bdcac0` | `b5 22 00 91` | add x21,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00bdcac4"></a> `00bdcac4` | `4e 00 00 14` | b 0x00bdcbfc | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcac8"></a> `00bdcac8` | `38 03 40 f9` | ldr x24,[x25] | `FALL_THROUGH`
<a id="insn-00bdcacc"></a> `00bdcacc` | `18 09 00 b4` | cbz x24,0x00bdcbec | `CONDITIONAL_JUMP`
<a id="insn-00bdcad0"></a> `00bdcad0` | `f5 22 00 91` | add x21,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00bdcad4"></a> `00bdcad4` | `02 00 00 14` | b 0x00bdcadc | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcad8"></a> `00bdcad8` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00bdcadc"></a> `00bdcadc` | `16 83 00 91` | add x22,x24,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcae0"></a> `00bdcae0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdcae4"></a> `00bdcae4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdcae8"></a> `00bdcae8` | `e2 fa 01 94` | bl 0x00c5b670 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcaec"></a> `00bdcaec` | `a0 00 00 36` | tbz w0,#0x0,0x00bdcb00 | `CONDITIONAL_JUMP`
<a id="insn-00bdcaf0"></a> `00bdcaf0` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00bdcaf4"></a> `00bdcaf4` | `88 04 00 b4` | cbz x8,0x00bdcb84 | `CONDITIONAL_JUMP`
<a id="insn-00bdcaf8"></a> `00bdcaf8` | `f5 03 18 aa` | mov x21,x24 | `FALL_THROUGH`
<a id="insn-00bdcafc"></a> `00bdcafc` | `f7 ff ff 17` | b 0x00bdcad8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcb00"></a> `00bdcb00` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdcb04"></a> `00bdcb04` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdcb08"></a> `00bdcb08` | `da fa 01 94` | bl 0x00c5b670 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcb0c"></a> `00bdcb0c` | `c0 06 00 36` | tbz w0,#0x0,0x00bdcbe4 | `CONDITIONAL_JUMP`
<a id="insn-00bdcb10"></a> `00bdcb10` | `f5 03 18 aa` | mov x21,x24 | `FALL_THROUGH`
<a id="insn-00bdcb14"></a> `00bdcb14` | `a8 8e 40 f8` | ldr x8,[x21, #0x8]! | `FALL_THROUGH`
<a id="insn-00bdcb18"></a> `00bdcb18` | `08 fe ff b5` | cbnz x8,0x00bdcad8 | `CONDITIONAL_JUMP`
<a id="insn-00bdcb1c"></a> `00bdcb1c` | `32 00 00 14` | b 0x00bdcbe4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcb20"></a> `00bdcb20` | `76 02 00 f9` | str x22,[x19] | `FALL_THROUGH`
<a id="insn-00bdcb24"></a> `00bdcb24` | `f5 03 16 aa` | mov x21,x22 | `FALL_THROUGH`
<a id="insn-00bdcb28"></a> `00bdcb28` | `35 00 00 14` | b 0x00bdcbfc | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcb2c"></a> `00bdcb2c` | `76 02 00 f9` | str x22,[x19] | `FALL_THROUGH`
<a id="insn-00bdcb30"></a> `00bdcb30` | `b6 02 00 f9` | str x22,[x21] | `FALL_THROUGH`
<a id="insn-00bdcb34"></a> `00bdcb34` | `32 00 00 14` | b 0x00bdcbfc | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcb38"></a> `00bdcb38` | `e8 03 16 aa` | mov x8,x22 | `FALL_THROUGH`
<a id="insn-00bdcb3c"></a> `00bdcb3c` | `18 0d 41 f8` | ldr x24,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00bdcb40"></a> `00bdcb40` | `09 03 40 f9` | ldr x9,[x24] | `FALL_THROUGH`
<a id="insn-00bdcb44"></a> `00bdcb44` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00bdcb48"></a> `00bdcb48` | `e0 00 00 54` | b.eq 0x00bdcb64 | `CONDITIONAL_JUMP`
<a id="insn-00bdcb4c"></a> `00bdcb4c` | `09 01 40 f9` | ldr x9,[x8] | `FALL_THROUGH`
<a id="insn-00bdcb50"></a> `00bdcb50` | `e8 03 09 aa` | mov x8,x9 | `FALL_THROUGH`
<a id="insn-00bdcb54"></a> `00bdcb54` | `18 0d 41 f8` | ldr x24,[x8, #0x10]! | `FALL_THROUGH`
<a id="insn-00bdcb58"></a> `00bdcb58` | `0a 03 40 f9` | ldr x10,[x24] | `FALL_THROUGH`
<a id="insn-00bdcb5c"></a> `00bdcb5c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00bdcb60"></a> `00bdcb60` | `61 ff ff 54` | b.ne 0x00bdcb4c | `CONDITIONAL_JUMP`
<a id="insn-00bdcb64"></a> `00bdcb64` | `1f 03 19 eb` | cmp x24,x25 | `FALL_THROUGH`
<a id="insn-00bdcb68"></a> `00bdcb68` | `a0 00 00 54` | b.eq 0x00bdcb7c | `CONDITIONAL_JUMP`
<a id="insn-00bdcb6c"></a> `00bdcb6c` | `01 83 00 91` | add x1,x24,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcb70"></a> `00bdcb70` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdcb74"></a> `00bdcb74` | `bf fa 01 94` | bl 0x00c5b670 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcb78"></a> `00bdcb78` | `c0 00 00 36` | tbz w0,#0x0,0x00bdcb90 | `CONDITIONAL_JUMP`
<a id="insn-00bdcb7c"></a> `00bdcb7c` | `c8 06 40 f9` | ldr x8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bdcb80"></a> `00bdcb80` | `c8 03 00 b4` | cbz x8,0x00bdcbf8 | `CONDITIONAL_JUMP`
<a id="insn-00bdcb84"></a> `00bdcb84` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00bdcb88"></a> `00bdcb88` | `f5 03 18 aa` | mov x21,x24 | `FALL_THROUGH`
<a id="insn-00bdcb8c"></a> `00bdcb8c` | `1c 00 00 14` | b 0x00bdcbfc | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcb90"></a> `00bdcb90` | `38 03 40 f9` | ldr x24,[x25] | `FALL_THROUGH`
<a id="insn-00bdcb94"></a> `00bdcb94` | `d8 02 00 b4` | cbz x24,0x00bdcbec | `CONDITIONAL_JUMP`
<a id="insn-00bdcb98"></a> `00bdcb98` | `f5 22 00 91` | add x21,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00bdcb9c"></a> `00bdcb9c` | `02 00 00 14` | b 0x00bdcba4 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcba0"></a> `00bdcba0` | `f8 03 08 aa` | mov x24,x8 | `FALL_THROUGH`
<a id="insn-00bdcba4"></a> `00bdcba4` | `16 83 00 91` | add x22,x24,#0x20 | `FALL_THROUGH`
<a id="insn-00bdcba8"></a> `00bdcba8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdcbac"></a> `00bdcbac` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdcbb0"></a> `00bdcbb0` | `b0 fa 01 94` | bl 0x00c5b670 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcbb4"></a> `00bdcbb4` | `a0 00 00 36` | tbz w0,#0x0,0x00bdcbc8 | `CONDITIONAL_JUMP`
<a id="insn-00bdcbb8"></a> `00bdcbb8` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00bdcbbc"></a> `00bdcbbc` | `48 fe ff b4` | cbz x8,0x00bdcb84 | `CONDITIONAL_JUMP`
<a id="insn-00bdcbc0"></a> `00bdcbc0` | `f5 03 18 aa` | mov x21,x24 | `FALL_THROUGH`
<a id="insn-00bdcbc4"></a> `00bdcbc4` | `f7 ff ff 17` | b 0x00bdcba0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcbc8"></a> `00bdcbc8` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdcbcc"></a> `00bdcbcc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdcbd0"></a> `00bdcbd0` | `a8 fa 01 94` | bl 0x00c5b670 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcbd4"></a> `00bdcbd4` | `80 00 00 36` | tbz w0,#0x0,0x00bdcbe4 | `CONDITIONAL_JUMP`
<a id="insn-00bdcbd8"></a> `00bdcbd8` | `f5 03 18 aa` | mov x21,x24 | `FALL_THROUGH`
<a id="insn-00bdcbdc"></a> `00bdcbdc` | `a8 8e 40 f8` | ldr x8,[x21, #0x8]! | `FALL_THROUGH`
<a id="insn-00bdcbe0"></a> `00bdcbe0` | `08 fe ff b5` | cbnz x8,0x00bdcba0 | `CONDITIONAL_JUMP`
<a id="insn-00bdcbe4"></a> `00bdcbe4` | `78 02 00 f9` | str x24,[x19] | `FALL_THROUGH`
<a id="insn-00bdcbe8"></a> `00bdcbe8` | `05 00 00 14` | b 0x00bdcbfc | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcbec"></a> `00bdcbec` | `79 02 00 f9` | str x25,[x19] | `FALL_THROUGH`
<a id="insn-00bdcbf0"></a> `00bdcbf0` | `f5 03 19 aa` | mov x21,x25 | `FALL_THROUGH`
<a id="insn-00bdcbf4"></a> `00bdcbf4` | `02 00 00 14` | b 0x00bdcbfc | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcbf8"></a> `00bdcbf8` | `76 02 00 f9` | str x22,[x19] | `FALL_THROUGH`
<a id="insn-00bdcbfc"></a> `00bdcbfc` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bdcc00"></a> `00bdcc00` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdcc04"></a> `00bdcc04` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdcc08"></a> `00bdcc08` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcc0c"></a> `00bdcc0c` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcc10"></a> `00bdcc10` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bdcc14"></a> `00bdcc14` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdc9ec`](#insn-00bdc9ec) 範囲 `[['00bdc9ec', '00bdca1f']]`
  - `CONDITIONAL_JUMP` [`00bdca1c`](#insn-00bdca1c) → [`00bdca38`](#insn-00bdca38)
  - `FALL_THROUGH` [`00bdca1c`](#insn-00bdca1c) → [`00bdca20`](#insn-00bdca20)
- ブロック [`00bdca20`](#insn-00bdca20) 範囲 `[['00bdca20', '00bdca37']]`
  - `CONDITIONAL_JUMP` [`00bdca34`](#insn-00bdca34) → [`00bdca60`](#insn-00bdca60)
  - `FALL_THROUGH` [`00bdca34`](#insn-00bdca34) → [`00bdca38`](#insn-00bdca38)
- ブロック [`00bdca38`](#insn-00bdca38) 範囲 `[['00bdca38', '00bdca47']]`
  - `CONDITIONAL_JUMP` [`00bdca44`](#insn-00bdca44) → [`00bdcab4`](#insn-00bdcab4)
  - `FALL_THROUGH` [`00bdca44`](#insn-00bdca44) → [`00bdca48`](#insn-00bdca48)
- ブロック [`00bdca48`](#insn-00bdca48) 範囲 `[['00bdca48', '00bdca4f']]`
  - `CONDITIONAL_JUMP` [`00bdca4c`](#insn-00bdca4c) → [`00bdca8c`](#insn-00bdca8c)
  - `FALL_THROUGH` [`00bdca4c`](#insn-00bdca4c) → [`00bdca50`](#insn-00bdca50)
- ブロック [`00bdca50`](#insn-00bdca50) 範囲 `[['00bdca50', '00bdca5b']]`
  - `CONDITIONAL_JUMP` [`00bdca58`](#insn-00bdca58) → [`00bdca50`](#insn-00bdca50)
  - `FALL_THROUGH` [`00bdca58`](#insn-00bdca58) → [`00bdca5c`](#insn-00bdca5c)
- ブロック [`00bdca5c`](#insn-00bdca5c) 範囲 `[['00bdca5c', '00bdca5f']]`
  - `UNCONDITIONAL_JUMP` [`00bdca5c`](#insn-00bdca5c) → [`00bdcaa4`](#insn-00bdcaa4)
- ブロック [`00bdca60`](#insn-00bdca60) 範囲 `[['00bdca60', '00bdca6f']]`
  - `CONDITIONAL_JUMP` [`00bdca6c`](#insn-00bdca6c) → [`00bdcb2c`](#insn-00bdcb2c)
  - `FALL_THROUGH` [`00bdca6c`](#insn-00bdca6c) → [`00bdca70`](#insn-00bdca70)
- ブロック [`00bdca70`](#insn-00bdca70) 範囲 `[['00bdca70', '00bdca7b']]`
  - `CONDITIONAL_JUMP` [`00bdca78`](#insn-00bdca78) → [`00bdcb38`](#insn-00bdcb38)
  - `FALL_THROUGH` [`00bdca78`](#insn-00bdca78) → [`00bdca7c`](#insn-00bdca7c)
- ブロック [`00bdca7c`](#insn-00bdca7c) 範囲 `[['00bdca7c', '00bdca87']]`
  - `CONDITIONAL_JUMP` [`00bdca84`](#insn-00bdca84) → [`00bdca7c`](#insn-00bdca7c)
  - `FALL_THROUGH` [`00bdca84`](#insn-00bdca84) → [`00bdca88`](#insn-00bdca88)
- ブロック [`00bdca88`](#insn-00bdca88) 範囲 `[['00bdca88', '00bdca8b']]`
  - `UNCONDITIONAL_JUMP` [`00bdca88`](#insn-00bdca88) → [`00bdcb64`](#insn-00bdcb64)
- ブロック [`00bdca8c`](#insn-00bdca8c) 範囲 `[['00bdca8c', '00bdca8f']]`
  - `FALL_THROUGH` [`00bdca8c`](#insn-00bdca8c) → [`00bdca90`](#insn-00bdca90)
- ブロック [`00bdca90`](#insn-00bdca90) 範囲 `[['00bdca90', '00bdcaa3']]`
  - `CONDITIONAL_JUMP` [`00bdcaa0`](#insn-00bdcaa0) → [`00bdca90`](#insn-00bdca90)
  - `FALL_THROUGH` [`00bdcaa0`](#insn-00bdcaa0) → [`00bdcaa4`](#insn-00bdcaa4)
- ブロック [`00bdcaa4`](#insn-00bdcaa4) 範囲 `[['00bdcaa4', '00bdcab3']]`
  - `CONDITIONAL_JUMP` [`00bdcab0`](#insn-00bdcab0) → [`00bdcac8`](#insn-00bdcac8)
  - `FALL_THROUGH` [`00bdcab0`](#insn-00bdcab0) → [`00bdcab4`](#insn-00bdcab4)
- ブロック [`00bdcab4`](#insn-00bdcab4) 範囲 `[['00bdcab4', '00bdcabb']]`
  - `CONDITIONAL_JUMP` [`00bdcab8`](#insn-00bdcab8) → [`00bdcb20`](#insn-00bdcb20)
  - `FALL_THROUGH` [`00bdcab8`](#insn-00bdcab8) → [`00bdcabc`](#insn-00bdcabc)
- ブロック [`00bdcabc`](#insn-00bdcabc) 範囲 `[['00bdcabc', '00bdcac7']]`
  - `UNCONDITIONAL_JUMP` [`00bdcac4`](#insn-00bdcac4) → [`00bdcbfc`](#insn-00bdcbfc)
- ブロック [`00bdcac8`](#insn-00bdcac8) 範囲 `[['00bdcac8', '00bdcacf']]`
  - `CONDITIONAL_JUMP` [`00bdcacc`](#insn-00bdcacc) → [`00bdcbec`](#insn-00bdcbec)
  - `FALL_THROUGH` [`00bdcacc`](#insn-00bdcacc) → [`00bdcad0`](#insn-00bdcad0)
- ブロック [`00bdcad0`](#insn-00bdcad0) 範囲 `[['00bdcad0', '00bdcad7']]`
  - `UNCONDITIONAL_JUMP` [`00bdcad4`](#insn-00bdcad4) → [`00bdcadc`](#insn-00bdcadc)
- ブロック [`00bdcad8`](#insn-00bdcad8) 範囲 `[['00bdcad8', '00bdcadb']]`
  - `FALL_THROUGH` [`00bdcad8`](#insn-00bdcad8) → [`00bdcadc`](#insn-00bdcadc)
- ブロック [`00bdcadc`](#insn-00bdcadc) 範囲 `[['00bdcadc', '00bdcaef']]`
  - `CONDITIONAL_JUMP` [`00bdcaec`](#insn-00bdcaec) → [`00bdcb00`](#insn-00bdcb00)
  - `FALL_THROUGH` [`00bdcaec`](#insn-00bdcaec) → [`00bdcaf0`](#insn-00bdcaf0)
- ブロック [`00bdcaf0`](#insn-00bdcaf0) 範囲 `[['00bdcaf0', '00bdcaf7']]`
  - `CONDITIONAL_JUMP` [`00bdcaf4`](#insn-00bdcaf4) → [`00bdcb84`](#insn-00bdcb84)
  - `FALL_THROUGH` [`00bdcaf4`](#insn-00bdcaf4) → [`00bdcaf8`](#insn-00bdcaf8)
- ブロック [`00bdcaf8`](#insn-00bdcaf8) 範囲 `[['00bdcaf8', '00bdcaff']]`
  - `UNCONDITIONAL_JUMP` [`00bdcafc`](#insn-00bdcafc) → [`00bdcad8`](#insn-00bdcad8)
- ブロック [`00bdcb00`](#insn-00bdcb00) 範囲 `[['00bdcb00', '00bdcb0f']]`
  - `CONDITIONAL_JUMP` [`00bdcb0c`](#insn-00bdcb0c) → [`00bdcbe4`](#insn-00bdcbe4)
  - `FALL_THROUGH` [`00bdcb0c`](#insn-00bdcb0c) → [`00bdcb10`](#insn-00bdcb10)
- ブロック [`00bdcb10`](#insn-00bdcb10) 範囲 `[['00bdcb10', '00bdcb1b']]`
  - `CONDITIONAL_JUMP` [`00bdcb18`](#insn-00bdcb18) → [`00bdcad8`](#insn-00bdcad8)
  - `FALL_THROUGH` [`00bdcb18`](#insn-00bdcb18) → [`00bdcb1c`](#insn-00bdcb1c)
- ブロック [`00bdcb1c`](#insn-00bdcb1c) 範囲 `[['00bdcb1c', '00bdcb1f']]`
  - `UNCONDITIONAL_JUMP` [`00bdcb1c`](#insn-00bdcb1c) → [`00bdcbe4`](#insn-00bdcbe4)
- ブロック [`00bdcb20`](#insn-00bdcb20) 範囲 `[['00bdcb20', '00bdcb2b']]`
  - `UNCONDITIONAL_JUMP` [`00bdcb28`](#insn-00bdcb28) → [`00bdcbfc`](#insn-00bdcbfc)
- ブロック [`00bdcb2c`](#insn-00bdcb2c) 範囲 `[['00bdcb2c', '00bdcb37']]`
  - `UNCONDITIONAL_JUMP` [`00bdcb34`](#insn-00bdcb34) → [`00bdcbfc`](#insn-00bdcbfc)
- ブロック [`00bdcb38`](#insn-00bdcb38) 範囲 `[['00bdcb38', '00bdcb47']]`
  - `FALL_THROUGH` [`00bdcb44`](#insn-00bdcb44) → [`00bdcb48`](#insn-00bdcb48)
- ブロック [`00bdcb48`](#insn-00bdcb48) 範囲 `[['00bdcb48', '00bdcb4b']]`
  - `CONDITIONAL_JUMP` [`00bdcb48`](#insn-00bdcb48) → [`00bdcb64`](#insn-00bdcb64)
  - `FALL_THROUGH` [`00bdcb48`](#insn-00bdcb48) → [`00bdcb4c`](#insn-00bdcb4c)
- ブロック [`00bdcb4c`](#insn-00bdcb4c) 範囲 `[['00bdcb4c', '00bdcb4f']]`
  - `FALL_THROUGH` [`00bdcb4c`](#insn-00bdcb4c) → [`00bdcb50`](#insn-00bdcb50)
- ブロック [`00bdcb50`](#insn-00bdcb50) 範囲 `[['00bdcb50', '00bdcb63']]`
  - `CONDITIONAL_JUMP` [`00bdcb60`](#insn-00bdcb60) → [`00bdcb4c`](#insn-00bdcb4c)
  - `FALL_THROUGH` [`00bdcb60`](#insn-00bdcb60) → [`00bdcb64`](#insn-00bdcb64)
- ブロック [`00bdcb64`](#insn-00bdcb64) 範囲 `[['00bdcb64', '00bdcb6b']]`
  - `CONDITIONAL_JUMP` [`00bdcb68`](#insn-00bdcb68) → [`00bdcb7c`](#insn-00bdcb7c)
  - `FALL_THROUGH` [`00bdcb68`](#insn-00bdcb68) → [`00bdcb6c`](#insn-00bdcb6c)
- ブロック [`00bdcb6c`](#insn-00bdcb6c) 範囲 `[['00bdcb6c', '00bdcb7b']]`
  - `CONDITIONAL_JUMP` [`00bdcb78`](#insn-00bdcb78) → [`00bdcb90`](#insn-00bdcb90)
  - `FALL_THROUGH` [`00bdcb78`](#insn-00bdcb78) → [`00bdcb7c`](#insn-00bdcb7c)
- ブロック [`00bdcb7c`](#insn-00bdcb7c) 範囲 `[['00bdcb7c', '00bdcb83']]`
  - `CONDITIONAL_JUMP` [`00bdcb80`](#insn-00bdcb80) → [`00bdcbf8`](#insn-00bdcbf8)
  - `FALL_THROUGH` [`00bdcb80`](#insn-00bdcb80) → [`00bdcb84`](#insn-00bdcb84)
- ブロック [`00bdcb84`](#insn-00bdcb84) 範囲 `[['00bdcb84', '00bdcb8f']]`
  - `UNCONDITIONAL_JUMP` [`00bdcb8c`](#insn-00bdcb8c) → [`00bdcbfc`](#insn-00bdcbfc)
- ブロック [`00bdcb90`](#insn-00bdcb90) 範囲 `[['00bdcb90', '00bdcb97']]`
  - `CONDITIONAL_JUMP` [`00bdcb94`](#insn-00bdcb94) → [`00bdcbec`](#insn-00bdcbec)
  - `FALL_THROUGH` [`00bdcb94`](#insn-00bdcb94) → [`00bdcb98`](#insn-00bdcb98)
- ブロック [`00bdcb98`](#insn-00bdcb98) 範囲 `[['00bdcb98', '00bdcb9f']]`
  - `UNCONDITIONAL_JUMP` [`00bdcb9c`](#insn-00bdcb9c) → [`00bdcba4`](#insn-00bdcba4)
- ブロック [`00bdcba0`](#insn-00bdcba0) 範囲 `[['00bdcba0', '00bdcba3']]`
  - `FALL_THROUGH` [`00bdcba0`](#insn-00bdcba0) → [`00bdcba4`](#insn-00bdcba4)
- ブロック [`00bdcba4`](#insn-00bdcba4) 範囲 `[['00bdcba4', '00bdcbb7']]`
  - `CONDITIONAL_JUMP` [`00bdcbb4`](#insn-00bdcbb4) → [`00bdcbc8`](#insn-00bdcbc8)
  - `FALL_THROUGH` [`00bdcbb4`](#insn-00bdcbb4) → [`00bdcbb8`](#insn-00bdcbb8)
- ブロック [`00bdcbb8`](#insn-00bdcbb8) 範囲 `[['00bdcbb8', '00bdcbbf']]`
  - `CONDITIONAL_JUMP` [`00bdcbbc`](#insn-00bdcbbc) → [`00bdcb84`](#insn-00bdcb84)
  - `FALL_THROUGH` [`00bdcbbc`](#insn-00bdcbbc) → [`00bdcbc0`](#insn-00bdcbc0)
- ブロック [`00bdcbc0`](#insn-00bdcbc0) 範囲 `[['00bdcbc0', '00bdcbc7']]`
  - `UNCONDITIONAL_JUMP` [`00bdcbc4`](#insn-00bdcbc4) → [`00bdcba0`](#insn-00bdcba0)
- ブロック [`00bdcbc8`](#insn-00bdcbc8) 範囲 `[['00bdcbc8', '00bdcbd7']]`
  - `CONDITIONAL_JUMP` [`00bdcbd4`](#insn-00bdcbd4) → [`00bdcbe4`](#insn-00bdcbe4)
  - `FALL_THROUGH` [`00bdcbd4`](#insn-00bdcbd4) → [`00bdcbd8`](#insn-00bdcbd8)
- ブロック [`00bdcbd8`](#insn-00bdcbd8) 範囲 `[['00bdcbd8', '00bdcbe3']]`
  - `CONDITIONAL_JUMP` [`00bdcbe0`](#insn-00bdcbe0) → [`00bdcba0`](#insn-00bdcba0)
  - `FALL_THROUGH` [`00bdcbe0`](#insn-00bdcbe0) → [`00bdcbe4`](#insn-00bdcbe4)
- ブロック [`00bdcbe4`](#insn-00bdcbe4) 範囲 `[['00bdcbe4', '00bdcbeb']]`
  - `UNCONDITIONAL_JUMP` [`00bdcbe8`](#insn-00bdcbe8) → [`00bdcbfc`](#insn-00bdcbfc)
- ブロック [`00bdcbec`](#insn-00bdcbec) 範囲 `[['00bdcbec', '00bdcbf7']]`
  - `UNCONDITIONAL_JUMP` [`00bdcbf4`](#insn-00bdcbf4) → [`00bdcbfc`](#insn-00bdcbfc)
- ブロック [`00bdcbf8`](#insn-00bdcbf8) 範囲 `[['00bdcbf8', '00bdcbfb']]`
  - `FALL_THROUGH` [`00bdcbf8`](#insn-00bdcbf8) → [`00bdcbfc`](#insn-00bdcbfc)
- ブロック [`00bdcbfc`](#insn-00bdcbfc) 範囲 `[['00bdcbfc', '00bdcc17']]`

## 命令位置別の参照

- [`00bdc9ec`](#insn-00bdc9ec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc9f0`](#insn-00bdc9f0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc9f4`](#insn-00bdc9f4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc9f8`](#insn-00bdc9f8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdc9fc`](#insn-00bdc9fc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdca1c`](#insn-00bdca1c) → [`00bdca38`](#insn-00bdca38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdca30`](#insn-00bdca30) → [`00c5b670`](../00c5b/00c5b670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b670` · 推定シンボル `None` · 推定型 `None`
- [`00bdca34`](#insn-00bdca34) → [`00bdca60`](#insn-00bdca60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdca44`](#insn-00bdca44) → [`00bdcab4`](#insn-00bdcab4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdca4c`](#insn-00bdca4c) → [`00bdca8c`](#insn-00bdca8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdca58`](#insn-00bdca58) → [`00bdca50`](#insn-00bdca50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdca5c`](#insn-00bdca5c) → [`00bdcaa4`](#insn-00bdcaa4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdca68`](#insn-00bdca68) → [`00c5b670`](../00c5b/00c5b670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b670` · 推定シンボル `None` · 推定型 `None`
- [`00bdca6c`](#insn-00bdca6c) → [`00bdcb2c`](#insn-00bdcb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdca78`](#insn-00bdca78) → [`00bdcb38`](#insn-00bdcb38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdca84`](#insn-00bdca84) → [`00bdca7c`](#insn-00bdca7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdca88`](#insn-00bdca88) → [`00bdcb64`](#insn-00bdcb64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcaa0`](#insn-00bdcaa0) → [`00bdca90`](#insn-00bdca90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcaac`](#insn-00bdcaac) → [`00c5b670`](../00c5b/00c5b670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b670` · 推定シンボル `None` · 推定型 `None`
- [`00bdcab0`](#insn-00bdcab0) → [`00bdcac8`](#insn-00bdcac8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcab8`](#insn-00bdcab8) → [`00bdcb20`](#insn-00bdcb20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcac4`](#insn-00bdcac4) → [`00bdcbfc`](#insn-00bdcbfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcacc`](#insn-00bdcacc) → [`00bdcbec`](#insn-00bdcbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcad4`](#insn-00bdcad4) → [`00bdcadc`](#insn-00bdcadc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcae8`](#insn-00bdcae8) → [`00c5b670`](../00c5b/00c5b670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b670` · 推定シンボル `None` · 推定型 `None`
- [`00bdcaec`](#insn-00bdcaec) → [`00bdcb00`](#insn-00bdcb00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcaf4`](#insn-00bdcaf4) → [`00bdcb84`](#insn-00bdcb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcafc`](#insn-00bdcafc) → [`00bdcad8`](#insn-00bdcad8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb08`](#insn-00bdcb08) → [`00c5b670`](../00c5b/00c5b670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b670` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb0c`](#insn-00bdcb0c) → [`00bdcbe4`](#insn-00bdcbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb18`](#insn-00bdcb18) → [`00bdcad8`](#insn-00bdcad8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb1c`](#insn-00bdcb1c) → [`00bdcbe4`](#insn-00bdcbe4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb28`](#insn-00bdcb28) → [`00bdcbfc`](#insn-00bdcbfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb34`](#insn-00bdcb34) → [`00bdcbfc`](#insn-00bdcbfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb48`](#insn-00bdcb48) → [`00bdcb64`](#insn-00bdcb64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb60`](#insn-00bdcb60) → [`00bdcb4c`](#insn-00bdcb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb68`](#insn-00bdcb68) → [`00bdcb7c`](#insn-00bdcb7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb74`](#insn-00bdcb74) → [`00c5b670`](../00c5b/00c5b670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b670` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb78`](#insn-00bdcb78) → [`00bdcb90`](#insn-00bdcb90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb80`](#insn-00bdcb80) → [`00bdcbf8`](#insn-00bdcbf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb8c`](#insn-00bdcb8c) → [`00bdcbfc`](#insn-00bdcbfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb94`](#insn-00bdcb94) → [`00bdcbec`](#insn-00bdcbec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcb9c`](#insn-00bdcb9c) → [`00bdcba4`](#insn-00bdcba4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbb0`](#insn-00bdcbb0) → [`00c5b670`](../00c5b/00c5b670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b670` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbb4`](#insn-00bdcbb4) → [`00bdcbc8`](#insn-00bdcbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbbc`](#insn-00bdcbbc) → [`00bdcb84`](#insn-00bdcb84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbc4`](#insn-00bdcbc4) → [`00bdcba0`](#insn-00bdcba0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbd0`](#insn-00bdcbd0) → [`00c5b670`](../00c5b/00c5b670.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b670` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbd4`](#insn-00bdcbd4) → [`00bdcbe4`](#insn-00bdcbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbe0`](#insn-00bdcbe0) → [`00bdcba0`](#insn-00bdcba0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbe8`](#insn-00bdcbe8) → [`00bdcbfc`](#insn-00bdcbfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcbf4`](#insn-00bdcbf4) → [`00bdcbfc`](#insn-00bdcbfc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc00`](#insn-00bdcc00) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc04`](#insn-00bdcc04) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc08`](#insn-00bdcc08) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcc0c`](#insn-00bdcc0c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdc9ec`](#insn-00bdc9ec)

~~~json
{
  "source": "00bdc9ec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc9f0`](#insn-00bdc9f0)

~~~json
{
  "source": "00bdc9f0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc9f4`](#insn-00bdc9f4)

~~~json
{
  "source": "00bdc9f4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc9f8`](#insn-00bdc9f8)

~~~json
{
  "source": "00bdc9f8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdc9fc`](#insn-00bdc9fc)

~~~json
{
  "source": "00bdc9fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdca1c`](#insn-00bdca1c)

~~~json
{
  "source": "00bdca1c",
  "target": "00bdca38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdca30`](#insn-00bdca30)

~~~json
{
  "source": "00bdca30",
  "target": "00c5b670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdca34`](#insn-00bdca34)

~~~json
{
  "source": "00bdca34",
  "target": "00bdca60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdca44`](#insn-00bdca44)

~~~json
{
  "source": "00bdca44",
  "target": "00bdcab4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdca4c`](#insn-00bdca4c)

~~~json
{
  "source": "00bdca4c",
  "target": "00bdca8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdca58`](#insn-00bdca58)

~~~json
{
  "source": "00bdca58",
  "target": "00bdca50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdca5c`](#insn-00bdca5c)

~~~json
{
  "source": "00bdca5c",
  "target": "00bdcaa4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdca68`](#insn-00bdca68)

~~~json
{
  "source": "00bdca68",
  "target": "00c5b670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdca6c`](#insn-00bdca6c)

~~~json
{
  "source": "00bdca6c",
  "target": "00bdcb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdca78`](#insn-00bdca78)

~~~json
{
  "source": "00bdca78",
  "target": "00bdcb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdca84`](#insn-00bdca84)

~~~json
{
  "source": "00bdca84",
  "target": "00bdca7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdca88`](#insn-00bdca88)

~~~json
{
  "source": "00bdca88",
  "target": "00bdcb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcaa0`](#insn-00bdcaa0)

~~~json
{
  "source": "00bdcaa0",
  "target": "00bdca90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcaac`](#insn-00bdcaac)

~~~json
{
  "source": "00bdcaac",
  "target": "00c5b670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcab0`](#insn-00bdcab0)

~~~json
{
  "source": "00bdcab0",
  "target": "00bdcac8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcab8`](#insn-00bdcab8)

~~~json
{
  "source": "00bdcab8",
  "target": "00bdcb20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcac4`](#insn-00bdcac4)

~~~json
{
  "source": "00bdcac4",
  "target": "00bdcbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcacc`](#insn-00bdcacc)

~~~json
{
  "source": "00bdcacc",
  "target": "00bdcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcad4`](#insn-00bdcad4)

~~~json
{
  "source": "00bdcad4",
  "target": "00bdcadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcae8`](#insn-00bdcae8)

~~~json
{
  "source": "00bdcae8",
  "target": "00c5b670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcaec`](#insn-00bdcaec)

~~~json
{
  "source": "00bdcaec",
  "target": "00bdcb00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcaf4`](#insn-00bdcaf4)

~~~json
{
  "source": "00bdcaf4",
  "target": "00bdcb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcafc`](#insn-00bdcafc)

~~~json
{
  "source": "00bdcafc",
  "target": "00bdcad8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb08`](#insn-00bdcb08)

~~~json
{
  "source": "00bdcb08",
  "target": "00c5b670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcb0c`](#insn-00bdcb0c)

~~~json
{
  "source": "00bdcb0c",
  "target": "00bdcbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb18`](#insn-00bdcb18)

~~~json
{
  "source": "00bdcb18",
  "target": "00bdcad8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb1c`](#insn-00bdcb1c)

~~~json
{
  "source": "00bdcb1c",
  "target": "00bdcbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb28`](#insn-00bdcb28)

~~~json
{
  "source": "00bdcb28",
  "target": "00bdcbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb34`](#insn-00bdcb34)

~~~json
{
  "source": "00bdcb34",
  "target": "00bdcbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb48`](#insn-00bdcb48)

~~~json
{
  "source": "00bdcb48",
  "target": "00bdcb64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb60`](#insn-00bdcb60)

~~~json
{
  "source": "00bdcb60",
  "target": "00bdcb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb68`](#insn-00bdcb68)

~~~json
{
  "source": "00bdcb68",
  "target": "00bdcb7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb74`](#insn-00bdcb74)

~~~json
{
  "source": "00bdcb74",
  "target": "00c5b670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcb78`](#insn-00bdcb78)

~~~json
{
  "source": "00bdcb78",
  "target": "00bdcb90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb80`](#insn-00bdcb80)

~~~json
{
  "source": "00bdcb80",
  "target": "00bdcbf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb8c`](#insn-00bdcb8c)

~~~json
{
  "source": "00bdcb8c",
  "target": "00bdcbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb94`](#insn-00bdcb94)

~~~json
{
  "source": "00bdcb94",
  "target": "00bdcbec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcb9c`](#insn-00bdcb9c)

~~~json
{
  "source": "00bdcb9c",
  "target": "00bdcba4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbb0`](#insn-00bdcbb0)

~~~json
{
  "source": "00bdcbb0",
  "target": "00c5b670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcbb4`](#insn-00bdcbb4)

~~~json
{
  "source": "00bdcbb4",
  "target": "00bdcbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbbc`](#insn-00bdcbbc)

~~~json
{
  "source": "00bdcbbc",
  "target": "00bdcb84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbc4`](#insn-00bdcbc4)

~~~json
{
  "source": "00bdcbc4",
  "target": "00bdcba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbd0`](#insn-00bdcbd0)

~~~json
{
  "source": "00bdcbd0",
  "target": "00c5b670",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcbd4`](#insn-00bdcbd4)

~~~json
{
  "source": "00bdcbd4",
  "target": "00bdcbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbe0`](#insn-00bdcbe0)

~~~json
{
  "source": "00bdcbe0",
  "target": "00bdcba0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbe8`](#insn-00bdcbe8)

~~~json
{
  "source": "00bdcbe8",
  "target": "00bdcbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcbf4`](#insn-00bdcbf4)

~~~json
{
  "source": "00bdcbf4",
  "target": "00bdcbfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc00`](#insn-00bdcc00)

~~~json
{
  "source": "00bdcc00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc04`](#insn-00bdcc04)

~~~json
{
  "source": "00bdcc04",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc08`](#insn-00bdcc08)

~~~json
{
  "source": "00bdcc08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcc0c`](#insn-00bdcc0c)

~~~json
{
  "source": "00bdcc0c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
