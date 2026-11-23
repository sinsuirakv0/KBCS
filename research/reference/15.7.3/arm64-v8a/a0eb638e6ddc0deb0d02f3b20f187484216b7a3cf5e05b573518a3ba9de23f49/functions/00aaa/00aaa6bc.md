# 00aaa6bc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00aaa5f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00aaa/00aaa5f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/inspection-0001.md#compare-5e1ec3fb5094adb1dcee91e2b2ed5691)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00aaa700`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00aaa/00aaa700.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0006.md#compare-e863e77bdbc246c5443174918a823420)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aaa6bc",
  "name": "FUN_00aaa6bc",
  "size": 572,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6732db97a39357e2c1a391d95dbd2b805cdcd22f5017d4b237525121aaddc3a5",
  "source_text_sha256": "6732db97a39357e2c1a391d95dbd2b805cdcd22f5017d4b237525121aaddc3a5",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aaa6bc",
        "00aaa8f7"
      ]
    ],
    "bytes_sha256": "243b03968f55793c9d68cc6b7a82b5020defa425b9c3701b22477b20126ba344",
    "instruction_count": 143,
    "instruction_bytes": 572,
    "body_bytes": 572,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aaa18c](../00aaa/00aaa18c.md)
- [00aaae5c](../00aaa/00aaae5c.md)
- [00aac358](../00aac/00aac358.md)

## 呼び出し先

- [00419064](../00419/00419064.md)
- [0041e380](../0041e/0041e380.md)
- [0044d968](../0044d/0044d968.md)
- [007cf950](../007cf/007cf950.md)
- [007cfaa0](../007cf/007cfaa0.md)
- [007cfcd8](../007cf/007cfcd8.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb160](../00bdb/00bdb160.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4105 bytes

~~~c

void FUN_00aaa6bc(long param_1,int param_2,int param_3,int param_4)

{
  ulong uVar1;
  undefined4 *puVar2;
  long *plVar3;
  undefined4 *puVar4;
  int iVar5;
  undefined8 *puVar6;
  void *__dest;
  undefined8 *puVar7;
  long *plVar8;
  ulong uVar9;
  undefined8 *puVar10;
  ulong uVar11;
  undefined8 *puVar12;
  void *__src;
  undefined8 *puVar13;
  undefined4 *puVar14;
  undefined4 *puVar15;
  long lVar16;
  undefined4 *puVar17;
  
  if (param_2 == -1) {
    param_2 = FUN_007cf950(0);
    param_3 = FUN_007cfaa0();
    param_4 = FUN_007cfcd8();
  }
  puVar12 = (undefined8 *)(param_1 + 0x30);
  puVar7 = *(undefined8 **)(param_1 + 0x20);
  *(undefined8 *)(param_1 + 0x38) = *puVar12;
  if (puVar7 == (undefined8 *)0x0) {
    return;
  }
  iVar5 = param_4 + param_3 * 10 + param_2 * 1000;
  puVar10 = puVar7;
  do {
    if (*(int *)(puVar10 + 4) <= iVar5) {
      if (iVar5 <= *(int *)(puVar10 + 4)) break;
      puVar10 = puVar10 + 1;
    }
    puVar10 = (undefined8 *)*puVar10;
    if (puVar10 == (undefined8 *)0x0) {
      return;
    }
  } while( true );
LAB_00aaa764:
  puVar10 = puVar7;
  if (*(int *)(puVar10 + 4) <= iVar5) {
    if (iVar5 <= *(int *)(puVar10 + 4)) goto LAB_00aaa7e8;
    puVar7 = (undefined8 *)puVar10[1];
    if ((undefined8 *)puVar10[1] == (undefined8 *)0x0) {
      puVar13 = puVar10 + 1;
      goto LAB_00aaa790;
    }
    goto LAB_00aaa764;
  }
  puVar7 = (undefined8 *)*puVar10;
  puVar13 = puVar10;
  if ((undefined8 *)*puVar10 == (undefined8 *)0x0) {
LAB_00aaa790:
    puVar6 = (undefined8 *)_Znwm(0x40);
    puVar6[6] = 0;
    puVar6[7] = 0;
    puVar6[5] = 0;
    *puVar6 = 0;
    puVar6[1] = 0;
    puVar6[2] = puVar10;
    *puVar13 = puVar6;
    plVar8 = *(long **)(param_1 + 0x18);
    *(int *)(puVar6 + 4) = iVar5;
    puVar7 = puVar6;
    if (*plVar8 != 0) {
      *(long *)(param_1 + 0x18) = *plVar8;
      puVar7 = (undefined8 *)*puVar13;
    }
    FUN_00419064(*(undefined8 *)(param_1 + 0x20),puVar7);
    *(long *)(param_1 + 0x28) = *(long *)(param_1 + 0x28) + 1;
    puVar10 = puVar6;
LAB_00aaa7e8:
    plVar8 = (long *)puVar10[5];
    plVar3 = (long *)puVar10[6];
    do {
      if (plVar8 == plVar3) {
        return;
      }
      puVar17 = (undefined4 *)*plVar8;
      puVar4 = (undefined4 *)plVar8[1];
      if (puVar17 != puVar4) {
        puVar15 = *(undefined4 **)(param_1 + 0x38);
        do {
          if (puVar15 < *(undefined4 **)(param_1 + 0x40)) {
            puVar14 = puVar15 + 1;
            *puVar15 = *puVar17;
          }
          else {
            __src = (void *)*puVar12;
            lVar16 = (long)puVar15 - (long)__src >> 2;
            uVar1 = lVar16 + 1;
            if (uVar1 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
              FUN_0044d968(puVar12);
            }
            uVar9 = (long)*(undefined4 **)(param_1 + 0x40) - (long)__src;
            uVar11 = (long)uVar9 >> 1;
            if (uVar11 <= uVar1) {
              uVar11 = uVar1;
            }
            if (0x7ffffffffffffffb < uVar9) {
              uVar11 = 0x3fffffffffffffff;
            }
            if (uVar11 == 0) {
              __dest = (void *)0x0;
            }
            else {
              if (uVar11 >> 0x3e != 0) {
                    /* WARNING: Subroutine does not return */
                FUN_0041e380();
              }
              __dest = (void *)_Znwm(uVar11 << 2);
            }
            puVar2 = (undefined4 *)((long)__dest + lVar16 * 4);
            puVar14 = puVar2 + 1;
            *puVar2 = *puVar17;
            memcpy(__dest,__src,(long)puVar15 - (long)__src);
            *(void **)(param_1 + 0x30) = __dest;
            *(undefined4 **)(param_1 + 0x38) = puVar14;
            *(void **)(param_1 + 0x40) = (void *)((long)__dest + uVar11 * 4);
            if (__src != (void *)0x0) {
              _ZdlPv(__src);
            }
          }
          puVar17 = puVar17 + 2;
          *(undefined4 **)(param_1 + 0x38) = puVar14;
          puVar15 = puVar14;
        } while (puVar17 != puVar4);
      }
      plVar8 = plVar8 + 3;
    } while( true );
  }
  goto LAB_00aaa764;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00aaa6bc"></a> `00aaa6bc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aaa6c0"></a> `00aaa6c0` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaa6c4"></a> `00aaa6c4` | `fc 6f 02 a9` | stp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaa6c8"></a> `00aaa6c8` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaa6cc"></a> `00aaa6cc` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aaa6d0"></a> `00aaa6d0` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aaa6d4"></a> `00aaa6d4` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aaa6d8"></a> `00aaa6d8` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00aaa6dc"></a> `00aaa6dc` | `3f 04 00 31` | cmn w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aaa6e0"></a> `00aaa6e0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00aaa6e4"></a> `00aaa6e4` | `41 01 00 54` | b.ne 0x00aaa70c | `CONDITIONAL_JUMP`
<a id="insn-00aaa6e8"></a> `00aaa6e8` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00aaa6ec"></a> `00aaa6ec` | `99 94 f4 97` | bl 0x007cf950 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa6f0"></a> `00aaa6f0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00aaa6f4"></a> `00aaa6f4` | `eb 94 f4 97` | bl 0x007cfaa0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa6f8"></a> `00aaa6f8` | `f5 03 00 2a` | mov w21,w0 | `FALL_THROUGH`
<a id="insn-00aaa6fc"></a> `00aaa6fc` | `77 95 f4 97` | bl 0x007cfcd8 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa700"></a> `00aaa700` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00aaa704"></a> `00aaa704` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00aaa708"></a> `00aaa708` | `e3 03 00 2a` | mov w3,w0 | `FALL_THROUGH`
<a id="insn-00aaa70c"></a> `00aaa70c` | `f4 03 13 aa` | mov x20,x19 | `FALL_THROUGH`
<a id="insn-00aaa710"></a> `00aaa710` | `89 0e 43 f8` | ldr x9,[x20, #0x30]! | `FALL_THROUGH`
<a id="insn-00aaa714"></a> `00aaa714` | `88 02 5f f8` | ldur x8,[x20, #-0x10] | `FALL_THROUGH`
<a id="insn-00aaa718"></a> `00aaa718` | `89 06 00 f9` | str x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00aaa71c"></a> `00aaa71c` | `88 0d 00 b4` | cbz x8,0x00aaa8cc | `CONDITIONAL_JUMP`
<a id="insn-00aaa720"></a> `00aaa720` | `49 01 80 52` | mov w9,#0xa | `FALL_THROUGH`
<a id="insn-00aaa724"></a> `00aaa724` | `0a 7d 80 52` | mov w10,#0x3e8 | `FALL_THROUGH`
<a id="insn-00aaa728"></a> `00aaa728` | `49 0c 09 1b` | madd w9,w2,w9,w3 | `FALL_THROUGH`
<a id="insn-00aaa72c"></a> `00aaa72c` | `36 24 0a 1b` | madd w22,w1,w10,w9 | `FALL_THROUGH`
<a id="insn-00aaa730"></a> `00aaa730` | `e9 03 08 aa` | mov x9,x8 | `FALL_THROUGH`
<a id="insn-00aaa734"></a> `00aaa734` | `04 00 00 14` | b 0x00aaa744 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaa738"></a> `00aaa738` | `29 21 00 91` | add x9,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00aaa73c"></a> `00aaa73c` | `29 01 40 f9` | ldr x9,[x9] | `FALL_THROUGH`
<a id="insn-00aaa740"></a> `00aaa740` | `69 0c 00 b4` | cbz x9,0x00aaa8cc | `CONDITIONAL_JUMP`
<a id="insn-00aaa744"></a> `00aaa744` | `2a 21 40 b9` | ldr w10,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00aaa748"></a> `00aaa748` | `df 02 0a 6b` | cmp w22,w10 | `FALL_THROUGH`
<a id="insn-00aaa74c"></a> `00aaa74c` | `8b ff ff 54` | b.lt 0x00aaa73c | `CONDITIONAL_JUMP`
<a id="insn-00aaa750"></a> `00aaa750` | `5f 01 16 6b` | cmp w10,w22 | `FALL_THROUGH`
<a id="insn-00aaa754"></a> `00aaa754` | `2b ff ff 54` | b.lt 0x00aaa738 | `CONDITIONAL_JUMP`
<a id="insn-00aaa758"></a> `00aaa758` | `03 00 00 14` | b 0x00aaa764 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaa75c"></a> `00aaa75c` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00aaa760"></a> `00aaa760` | `68 01 00 b4` | cbz x8,0x00aaa78c | `CONDITIONAL_JUMP`
<a id="insn-00aaa764"></a> `00aaa764` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00aaa768"></a> `00aaa768` | `08 21 40 b9` | ldr w8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00aaa76c"></a> `00aaa76c` | `df 02 08 6b` | cmp w22,w8 | `FALL_THROUGH`
<a id="insn-00aaa770"></a> `00aaa770` | `6b ff ff 54` | b.lt 0x00aaa75c | `CONDITIONAL_JUMP`
<a id="insn-00aaa774"></a> `00aaa774` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00aaa778"></a> `00aaa778` | `6a 03 00 54` | b.ge 0x00aaa7e4 | `CONDITIONAL_JUMP`
<a id="insn-00aaa77c"></a> `00aaa77c` | `e8 06 40 f9` | ldr x8,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00aaa780"></a> `00aaa780` | `28 ff ff b5` | cbnz x8,0x00aaa764 | `CONDITIONAL_JUMP`
<a id="insn-00aaa784"></a> `00aaa784` | `f8 22 00 91` | add x24,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00aaa788"></a> `00aaa788` | `02 00 00 14` | b 0x00aaa790 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaa78c"></a> `00aaa78c` | `f8 03 17 aa` | mov x24,x23 | `FALL_THROUGH`
<a id="insn-00aaa790"></a> `00aaa790` | `00 08 80 52` | mov w0,#0x40 | `FALL_THROUGH`
<a id="insn-00aaa794"></a> `00aaa794` | `17 c2 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa798"></a> `00aaa798` | `1f 7c 03 a9` | stp xzr,xzr,[x0, #0x30] | `FALL_THROUGH`
<a id="insn-00aaa79c"></a> `00aaa79c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00aaa7a0"></a> `00aaa7a0` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00aaa7a4"></a> `00aaa7a4` | `1f 14 00 f9` | str xzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00aaa7a8"></a> `00aaa7a8` | `1f 7c 00 a9` | stp xzr,xzr,[x0] | `FALL_THROUGH`
<a id="insn-00aaa7ac"></a> `00aaa7ac` | `17 08 00 f9` | str x23,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00aaa7b0"></a> `00aaa7b0` | `00 03 00 f9` | str x0,[x24] | `FALL_THROUGH`
<a id="insn-00aaa7b4"></a> `00aaa7b4` | `68 0e 40 f9` | ldr x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00aaa7b8"></a> `00aaa7b8` | `16 20 00 b9` | str w22,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00aaa7bc"></a> `00aaa7bc` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00aaa7c0"></a> `00aaa7c0` | `68 00 00 b4` | cbz x8,0x00aaa7cc | `CONDITIONAL_JUMP`
<a id="insn-00aaa7c4"></a> `00aaa7c4` | `68 0e 00 f9` | str x8,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00aaa7c8"></a> `00aaa7c8` | `01 03 40 f9` | ldr x1,[x24] | `FALL_THROUGH`
<a id="insn-00aaa7cc"></a> `00aaa7cc` | `60 12 40 f9` | ldr x0,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00aaa7d0"></a> `00aaa7d0` | `25 ba e5 97` | bl 0x00419064 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa7d4"></a> `00aaa7d4` | `68 16 40 f9` | ldr x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aaa7d8"></a> `00aaa7d8` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aaa7dc"></a> `00aaa7dc` | `68 16 00 f9` | str x8,[x19, #0x28] | `FALL_THROUGH`
<a id="insn-00aaa7e0"></a> `00aaa7e0` | `02 00 00 14` | b 0x00aaa7e8 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaa7e4"></a> `00aaa7e4` | `f5 03 17 aa` | mov x21,x23 | `FALL_THROUGH`
<a id="insn-00aaa7e8"></a> `00aaa7e8` | `b8 a2 42 a9` | ldp x24,x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00aaa7ec"></a> `00aaa7ec` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aaa7f0"></a> `00aaa7f0` | `03 00 00 14` | b 0x00aaa7fc | `UNCONDITIONAL_JUMP`
<a id="insn-00aaa7f4"></a> `00aaa7f4` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aaa7f8"></a> `00aaa7f8` | `18 63 00 91` | add x24,x24,#0x18 | `FALL_THROUGH`
<a id="insn-00aaa7fc"></a> `00aaa7fc` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00aaa800"></a> `00aaa800` | `60 06 00 54` | b.eq 0x00aaa8cc | `CONDITIONAL_JUMP`
<a id="insn-00aaa804"></a> `00aaa804` | `1c 67 40 a9` | ldp x28,x25,[x24] | `FALL_THROUGH`
<a id="insn-00aaa808"></a> `00aaa808` | `9f 03 19 eb` | cmp x28,x25 | `FALL_THROUGH`
<a id="insn-00aaa80c"></a> `00aaa80c` | `40 ff ff 54` | b.eq 0x00aaa7f4 | `CONDITIONAL_JUMP`
<a id="insn-00aaa810"></a> `00aaa810` | `7a 1e 40 f9` | ldr x26,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00aaa814"></a> `00aaa814` | `07 00 00 14` | b 0x00aaa830 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaa818"></a> `00aaa818` | `88 03 40 b9` | ldr w8,[x28] | `FALL_THROUGH`
<a id="insn-00aaa81c"></a> `00aaa81c` | `48 47 00 b8` | str w8,[x26], #0x4 | `FALL_THROUGH`
<a id="insn-00aaa820"></a> `00aaa820` | `9c 23 00 91` | add x28,x28,#0x8 | `FALL_THROUGH`
<a id="insn-00aaa824"></a> `00aaa824` | `7a 1e 00 f9` | str x26,[x19, #0x38] | `FALL_THROUGH`
<a id="insn-00aaa828"></a> `00aaa828` | `9f 03 19 eb` | cmp x28,x25 | `FALL_THROUGH`
<a id="insn-00aaa82c"></a> `00aaa82c` | `40 fe ff 54` | b.eq 0x00aaa7f4 | `CONDITIONAL_JUMP`
<a id="insn-00aaa830"></a> `00aaa830` | `68 22 40 f9` | ldr x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00aaa834"></a> `00aaa834` | `5f 03 08 eb` | cmp x26,x8 | `FALL_THROUGH`
<a id="insn-00aaa838"></a> `00aaa838` | `03 ff ff 54` | b.cc 0x00aaa818 | `CONDITIONAL_JUMP`
<a id="insn-00aaa83c"></a> `00aaa83c` | `95 02 40 f9` | ldr x21,[x20] | `FALL_THROUGH`
<a id="insn-00aaa840"></a> `00aaa840` | `56 03 15 cb` | sub x22,x26,x21 | `FALL_THROUGH`
<a id="insn-00aaa844"></a> `00aaa844` | `da fe 42 93` | asr x26,x22,#0x2 | `FALL_THROUGH`
<a id="insn-00aaa848"></a> `00aaa848` | `49 07 00 91` | add x9,x26,#0x1 | `FALL_THROUGH`
<a id="insn-00aaa84c"></a> `00aaa84c` | `2a fd 7e d3` | lsr x10,x9,#0x3e | `FALL_THROUGH`
<a id="insn-00aaa850"></a> `00aaa850` | `ea 04 00 b5` | cbnz x10,0x00aaa8ec | `CONDITIONAL_JUMP`
<a id="insn-00aaa854"></a> `00aaa854` | `08 01 15 cb` | sub x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00aaa858"></a> `00aaa858` | `0a fd 41 93` | asr x10,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00aaa85c"></a> `00aaa85c` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-00aaa860"></a> `00aaa860` | `49 81 89 9a` | csel x9,x10,x9,hi | `FALL_THROUGH`
<a id="insn-00aaa864"></a> `00aaa864` | `ea f3 7e b2` | orr x10,xzr,#0x7ffffffffffffffc | `FALL_THROUGH`
<a id="insn-00aaa868"></a> `00aaa868` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00aaa86c"></a> `00aaa86c` | `08 00 f8 92` | mov x8,#0x3fffffffffffffff | `FALL_THROUGH`
<a id="insn-00aaa870"></a> `00aaa870` | `3b 31 88 9a` | csel x27,x9,x8,cc | `FALL_THROUGH`
<a id="insn-00aaa874"></a> `00aaa874` | `fb 00 00 b4` | cbz x27,0x00aaa890 | `CONDITIONAL_JUMP`
<a id="insn-00aaa878"></a> `00aaa878` | `68 ff 7e d3` | lsr x8,x27,#0x3e | `FALL_THROUGH`
<a id="insn-00aaa87c"></a> `00aaa87c` | `c8 03 00 b5` | cbnz x8,0x00aaa8f4 | `CONDITIONAL_JUMP`
<a id="insn-00aaa880"></a> `00aaa880` | `60 f7 7e d3` | lsl x0,x27,#0x2 | `FALL_THROUGH`
<a id="insn-00aaa884"></a> `00aaa884` | `db c1 04 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa888"></a> `00aaa888` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00aaa88c"></a> `00aaa88c` | `02 00 00 14` | b 0x00aaa894 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaa890"></a> `00aaa890` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00aaa894"></a> `00aaa894` | `fa 0a 1a 8b` | add x26,x23,x26, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00aaa898"></a> `00aaa898` | `88 03 40 b9` | ldr w8,[x28] | `FALL_THROUGH`
<a id="insn-00aaa89c"></a> `00aaa89c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00aaa8a0"></a> `00aaa8a0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00aaa8a4"></a> `00aaa8a4` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00aaa8a8"></a> `00aaa8a8` | `fb 0a 1b 8b` | add x27,x23,x27, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00aaa8ac"></a> `00aaa8ac` | `48 47 00 b8` | str w8,[x26], #0x4 | `FALL_THROUGH`
<a id="insn-00aaa8b0"></a> `00aaa8b0` | `2c c2 04 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa8b4"></a> `00aaa8b4` | `77 6a 03 a9` | stp x23,x26,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00aaa8b8"></a> `00aaa8b8` | `7b 22 00 f9` | str x27,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00aaa8bc"></a> `00aaa8bc` | `35 fb ff b4` | cbz x21,0x00aaa820 | `CONDITIONAL_JUMP`
<a id="insn-00aaa8c0"></a> `00aaa8c0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00aaa8c4"></a> `00aaa8c4` | `d3 c1 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00aaa8c8"></a> `00aaa8c8` | `d6 ff ff 17` | b 0x00aaa820 | `UNCONDITIONAL_JUMP`
<a id="insn-00aaa8cc"></a> `00aaa8cc` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aaa8d0"></a> `00aaa8d0` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00aaa8d4"></a> `00aaa8d4` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aaa8d8"></a> `00aaa8d8` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00aaa8dc"></a> `00aaa8dc` | `fc 6f 42 a9` | ldp x28,x27,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aaa8e0"></a> `00aaa8e0` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00aaa8e4"></a> `00aaa8e4` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00aaa8e8"></a> `00aaa8e8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aaa8ec"></a> `00aaa8ec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aaa8f0"></a> `00aaa8f0` | `1e 8c e6 97` | bl 0x0044d968 | `CALL_TERMINATOR`
<a id="insn-00aaa8f4"></a> `00aaa8f4` | `a3 ce e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aaa6bc`](#insn-00aaa6bc) 範囲 `[['00aaa6bc', '00aaa6e7']]`
  - `CONDITIONAL_JUMP` [`00aaa6e4`](#insn-00aaa6e4) → [`00aaa70c`](#insn-00aaa70c)
  - `FALL_THROUGH` [`00aaa6e4`](#insn-00aaa6e4) → [`00aaa6e8`](#insn-00aaa6e8)
- ブロック [`00aaa6e8`](#insn-00aaa6e8) 範囲 `[['00aaa6e8', '00aaa70b']]`
  - `FALL_THROUGH` [`00aaa708`](#insn-00aaa708) → [`00aaa70c`](#insn-00aaa70c)
- ブロック [`00aaa70c`](#insn-00aaa70c) 範囲 `[['00aaa70c', '00aaa71f']]`
  - `CONDITIONAL_JUMP` [`00aaa71c`](#insn-00aaa71c) → [`00aaa8cc`](#insn-00aaa8cc)
  - `FALL_THROUGH` [`00aaa71c`](#insn-00aaa71c) → [`00aaa720`](#insn-00aaa720)
- ブロック [`00aaa720`](#insn-00aaa720) 範囲 `[['00aaa720', '00aaa737']]`
  - `UNCONDITIONAL_JUMP` [`00aaa734`](#insn-00aaa734) → [`00aaa744`](#insn-00aaa744)
- ブロック [`00aaa738`](#insn-00aaa738) 範囲 `[['00aaa738', '00aaa73b']]`
  - `FALL_THROUGH` [`00aaa738`](#insn-00aaa738) → [`00aaa73c`](#insn-00aaa73c)
- ブロック [`00aaa73c`](#insn-00aaa73c) 範囲 `[['00aaa73c', '00aaa743']]`
  - `CONDITIONAL_JUMP` [`00aaa740`](#insn-00aaa740) → [`00aaa8cc`](#insn-00aaa8cc)
  - `FALL_THROUGH` [`00aaa740`](#insn-00aaa740) → [`00aaa744`](#insn-00aaa744)
- ブロック [`00aaa744`](#insn-00aaa744) 範囲 `[['00aaa744', '00aaa74f']]`
  - `CONDITIONAL_JUMP` [`00aaa74c`](#insn-00aaa74c) → [`00aaa73c`](#insn-00aaa73c)
  - `FALL_THROUGH` [`00aaa74c`](#insn-00aaa74c) → [`00aaa750`](#insn-00aaa750)
- ブロック [`00aaa750`](#insn-00aaa750) 範囲 `[['00aaa750', '00aaa757']]`
  - `CONDITIONAL_JUMP` [`00aaa754`](#insn-00aaa754) → [`00aaa738`](#insn-00aaa738)
  - `FALL_THROUGH` [`00aaa754`](#insn-00aaa754) → [`00aaa758`](#insn-00aaa758)
- ブロック [`00aaa758`](#insn-00aaa758) 範囲 `[['00aaa758', '00aaa75b']]`
  - `UNCONDITIONAL_JUMP` [`00aaa758`](#insn-00aaa758) → [`00aaa764`](#insn-00aaa764)
- ブロック [`00aaa75c`](#insn-00aaa75c) 範囲 `[['00aaa75c', '00aaa763']]`
  - `CONDITIONAL_JUMP` [`00aaa760`](#insn-00aaa760) → [`00aaa78c`](#insn-00aaa78c)
  - `FALL_THROUGH` [`00aaa760`](#insn-00aaa760) → [`00aaa764`](#insn-00aaa764)
- ブロック [`00aaa764`](#insn-00aaa764) 範囲 `[['00aaa764', '00aaa773']]`
  - `CONDITIONAL_JUMP` [`00aaa770`](#insn-00aaa770) → [`00aaa75c`](#insn-00aaa75c)
  - `FALL_THROUGH` [`00aaa770`](#insn-00aaa770) → [`00aaa774`](#insn-00aaa774)
- ブロック [`00aaa774`](#insn-00aaa774) 範囲 `[['00aaa774', '00aaa77b']]`
  - `CONDITIONAL_JUMP` [`00aaa778`](#insn-00aaa778) → [`00aaa7e4`](#insn-00aaa7e4)
  - `FALL_THROUGH` [`00aaa778`](#insn-00aaa778) → [`00aaa77c`](#insn-00aaa77c)
- ブロック [`00aaa77c`](#insn-00aaa77c) 範囲 `[['00aaa77c', '00aaa783']]`
  - `CONDITIONAL_JUMP` [`00aaa780`](#insn-00aaa780) → [`00aaa764`](#insn-00aaa764)
  - `FALL_THROUGH` [`00aaa780`](#insn-00aaa780) → [`00aaa784`](#insn-00aaa784)
- ブロック [`00aaa784`](#insn-00aaa784) 範囲 `[['00aaa784', '00aaa78b']]`
  - `UNCONDITIONAL_JUMP` [`00aaa788`](#insn-00aaa788) → [`00aaa790`](#insn-00aaa790)
- ブロック [`00aaa78c`](#insn-00aaa78c) 範囲 `[['00aaa78c', '00aaa78f']]`
  - `FALL_THROUGH` [`00aaa78c`](#insn-00aaa78c) → [`00aaa790`](#insn-00aaa790)
- ブロック [`00aaa790`](#insn-00aaa790) 範囲 `[['00aaa790', '00aaa7c3']]`
  - `CONDITIONAL_JUMP` [`00aaa7c0`](#insn-00aaa7c0) → [`00aaa7cc`](#insn-00aaa7cc)
  - `FALL_THROUGH` [`00aaa7c0`](#insn-00aaa7c0) → [`00aaa7c4`](#insn-00aaa7c4)
- ブロック [`00aaa7c4`](#insn-00aaa7c4) 範囲 `[['00aaa7c4', '00aaa7cb']]`
  - `FALL_THROUGH` [`00aaa7c8`](#insn-00aaa7c8) → [`00aaa7cc`](#insn-00aaa7cc)
- ブロック [`00aaa7cc`](#insn-00aaa7cc) 範囲 `[['00aaa7cc', '00aaa7e3']]`
  - `UNCONDITIONAL_JUMP` [`00aaa7e0`](#insn-00aaa7e0) → [`00aaa7e8`](#insn-00aaa7e8)
- ブロック [`00aaa7e4`](#insn-00aaa7e4) 範囲 `[['00aaa7e4', '00aaa7e7']]`
  - `FALL_THROUGH` [`00aaa7e4`](#insn-00aaa7e4) → [`00aaa7e8`](#insn-00aaa7e8)
- ブロック [`00aaa7e8`](#insn-00aaa7e8) 範囲 `[['00aaa7e8', '00aaa7f3']]`
  - `UNCONDITIONAL_JUMP` [`00aaa7f0`](#insn-00aaa7f0) → [`00aaa7fc`](#insn-00aaa7fc)
- ブロック [`00aaa7f4`](#insn-00aaa7f4) 範囲 `[['00aaa7f4', '00aaa7fb']]`
  - `FALL_THROUGH` [`00aaa7f8`](#insn-00aaa7f8) → [`00aaa7fc`](#insn-00aaa7fc)
- ブロック [`00aaa7fc`](#insn-00aaa7fc) 範囲 `[['00aaa7fc', '00aaa803']]`
  - `CONDITIONAL_JUMP` [`00aaa800`](#insn-00aaa800) → [`00aaa8cc`](#insn-00aaa8cc)
  - `FALL_THROUGH` [`00aaa800`](#insn-00aaa800) → [`00aaa804`](#insn-00aaa804)
- ブロック [`00aaa804`](#insn-00aaa804) 範囲 `[['00aaa804', '00aaa80f']]`
  - `CONDITIONAL_JUMP` [`00aaa80c`](#insn-00aaa80c) → [`00aaa7f4`](#insn-00aaa7f4)
  - `FALL_THROUGH` [`00aaa80c`](#insn-00aaa80c) → [`00aaa810`](#insn-00aaa810)
- ブロック [`00aaa810`](#insn-00aaa810) 範囲 `[['00aaa810', '00aaa817']]`
  - `UNCONDITIONAL_JUMP` [`00aaa814`](#insn-00aaa814) → [`00aaa830`](#insn-00aaa830)
- ブロック [`00aaa818`](#insn-00aaa818) 範囲 `[['00aaa818', '00aaa81f']]`
  - `FALL_THROUGH` [`00aaa81c`](#insn-00aaa81c) → [`00aaa820`](#insn-00aaa820)
- ブロック [`00aaa820`](#insn-00aaa820) 範囲 `[['00aaa820', '00aaa82f']]`
  - `CONDITIONAL_JUMP` [`00aaa82c`](#insn-00aaa82c) → [`00aaa7f4`](#insn-00aaa7f4)
  - `FALL_THROUGH` [`00aaa82c`](#insn-00aaa82c) → [`00aaa830`](#insn-00aaa830)
- ブロック [`00aaa830`](#insn-00aaa830) 範囲 `[['00aaa830', '00aaa83b']]`
  - `CONDITIONAL_JUMP` [`00aaa838`](#insn-00aaa838) → [`00aaa818`](#insn-00aaa818)
  - `FALL_THROUGH` [`00aaa838`](#insn-00aaa838) → [`00aaa83c`](#insn-00aaa83c)
- ブロック [`00aaa83c`](#insn-00aaa83c) 範囲 `[['00aaa83c', '00aaa853']]`
  - `CONDITIONAL_JUMP` [`00aaa850`](#insn-00aaa850) → [`00aaa8ec`](#insn-00aaa8ec)
  - `FALL_THROUGH` [`00aaa850`](#insn-00aaa850) → [`00aaa854`](#insn-00aaa854)
- ブロック [`00aaa854`](#insn-00aaa854) 範囲 `[['00aaa854', '00aaa877']]`
  - `CONDITIONAL_JUMP` [`00aaa874`](#insn-00aaa874) → [`00aaa890`](#insn-00aaa890)
  - `FALL_THROUGH` [`00aaa874`](#insn-00aaa874) → [`00aaa878`](#insn-00aaa878)
- ブロック [`00aaa878`](#insn-00aaa878) 範囲 `[['00aaa878', '00aaa87f']]`
  - `CONDITIONAL_JUMP` [`00aaa87c`](#insn-00aaa87c) → [`00aaa8f4`](#insn-00aaa8f4)
  - `FALL_THROUGH` [`00aaa87c`](#insn-00aaa87c) → [`00aaa880`](#insn-00aaa880)
- ブロック [`00aaa880`](#insn-00aaa880) 範囲 `[['00aaa880', '00aaa88f']]`
  - `UNCONDITIONAL_JUMP` [`00aaa88c`](#insn-00aaa88c) → [`00aaa894`](#insn-00aaa894)
- ブロック [`00aaa890`](#insn-00aaa890) 範囲 `[['00aaa890', '00aaa893']]`
  - `FALL_THROUGH` [`00aaa890`](#insn-00aaa890) → [`00aaa894`](#insn-00aaa894)
- ブロック [`00aaa894`](#insn-00aaa894) 範囲 `[['00aaa894', '00aaa8bf']]`
  - `CONDITIONAL_JUMP` [`00aaa8bc`](#insn-00aaa8bc) → [`00aaa820`](#insn-00aaa820)
  - `FALL_THROUGH` [`00aaa8bc`](#insn-00aaa8bc) → [`00aaa8c0`](#insn-00aaa8c0)
- ブロック [`00aaa8c0`](#insn-00aaa8c0) 範囲 `[['00aaa8c0', '00aaa8cb']]`
  - `UNCONDITIONAL_JUMP` [`00aaa8c8`](#insn-00aaa8c8) → [`00aaa820`](#insn-00aaa820)
- ブロック [`00aaa8cc`](#insn-00aaa8cc) 範囲 `[['00aaa8cc', '00aaa8eb']]`
- ブロック [`00aaa8ec`](#insn-00aaa8ec) 範囲 `[['00aaa8ec', '00aaa8f3']]`
- ブロック [`00aaa8f4`](#insn-00aaa8f4) 範囲 `[['00aaa8f4', '00aaa8f7']]`

## 命令位置別の参照

- [`00aaa6c0`](#insn-00aaa6c0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa6c4`](#insn-00aaa6c4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa6c8`](#insn-00aaa6c8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa6cc`](#insn-00aaa6cc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa6d0`](#insn-00aaa6d0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa6d4`](#insn-00aaa6d4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa6e4`](#insn-00aaa6e4) → [`00aaa70c`](#insn-00aaa70c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa6ec`](#insn-00aaa6ec) → [`007cf950`](../007cf/007cf950.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cf950` · 推定シンボル `None` · 推定型 `None`
- [`00aaa6f4`](#insn-00aaa6f4) → [`007cfaa0`](../007cf/007cfaa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfaa0` · 推定シンボル `None` · 推定型 `None`
- [`00aaa6fc`](#insn-00aaa6fc) → [`007cfcd8`](../007cf/007cfcd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `007cfcd8` · 推定シンボル `None` · 推定型 `None`
- [`00aaa71c`](#insn-00aaa71c) → [`00aaa8cc`](#insn-00aaa8cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa734`](#insn-00aaa734) → [`00aaa744`](#insn-00aaa744) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa740`](#insn-00aaa740) → [`00aaa8cc`](#insn-00aaa8cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa74c`](#insn-00aaa74c) → [`00aaa73c`](#insn-00aaa73c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa754`](#insn-00aaa754) → [`00aaa738`](#insn-00aaa738) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa758`](#insn-00aaa758) → [`00aaa764`](#insn-00aaa764) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa760`](#insn-00aaa760) → [`00aaa78c`](#insn-00aaa78c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa770`](#insn-00aaa770) → [`00aaa75c`](#insn-00aaa75c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa778`](#insn-00aaa778) → [`00aaa7e4`](#insn-00aaa7e4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa780`](#insn-00aaa780) → [`00aaa764`](#insn-00aaa764) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa788`](#insn-00aaa788) → [`00aaa790`](#insn-00aaa790) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa794`](#insn-00aaa794) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aaa7c0`](#insn-00aaa7c0) → [`00aaa7cc`](#insn-00aaa7cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa7d0`](#insn-00aaa7d0) → [`00419064`](../00419/00419064.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00419064` · 推定シンボル `None` · 推定型 `None`
- [`00aaa7e0`](#insn-00aaa7e0) → [`00aaa7e8`](#insn-00aaa7e8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa7ec`](#insn-00aaa7ec) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa7f0`](#insn-00aaa7f0) → [`00aaa7fc`](#insn-00aaa7fc) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa7f4`](#insn-00aaa7f4) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa800`](#insn-00aaa800) → [`00aaa8cc`](#insn-00aaa8cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa80c`](#insn-00aaa80c) → [`00aaa7f4`](#insn-00aaa7f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa814`](#insn-00aaa814) → [`00aaa830`](#insn-00aaa830) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa82c`](#insn-00aaa82c) → [`00aaa7f4`](#insn-00aaa7f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa838`](#insn-00aaa838) → [`00aaa818`](#insn-00aaa818) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa850`](#insn-00aaa850) → [`00aaa8ec`](#insn-00aaa8ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa874`](#insn-00aaa874) → [`00aaa890`](#insn-00aaa890) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa87c`](#insn-00aaa87c) → [`00aaa8f4`](#insn-00aaa8f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa884`](#insn-00aaa884) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00aaa88c`](#insn-00aaa88c) → [`00aaa894`](#insn-00aaa894) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8b0`](#insn-00aaa8b0) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8bc`](#insn-00aaa8bc) → [`00aaa820`](#insn-00aaa820) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8c4`](#insn-00aaa8c4) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8c8`](#insn-00aaa8c8) → [`00aaa820`](#insn-00aaa820) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8cc`](#insn-00aaa8cc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8d0`](#insn-00aaa8d0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8d4`](#insn-00aaa8d4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8d8`](#insn-00aaa8d8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8dc`](#insn-00aaa8dc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8e0`](#insn-00aaa8e0) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8f0`](#insn-00aaa8f0) → [`0044d968`](../0044d/0044d968.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0044d968` · 推定シンボル `None` · 推定型 `None`
- [`00aaa8f4`](#insn-00aaa8f4) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aaa6c0`](#insn-00aaa6c0)

~~~json
{
  "source": "00aaa6c0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa6c4`](#insn-00aaa6c4)

~~~json
{
  "source": "00aaa6c4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa6c8`](#insn-00aaa6c8)

~~~json
{
  "source": "00aaa6c8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa6cc`](#insn-00aaa6cc)

~~~json
{
  "source": "00aaa6cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa6d0`](#insn-00aaa6d0)

~~~json
{
  "source": "00aaa6d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa6d4`](#insn-00aaa6d4)

~~~json
{
  "source": "00aaa6d4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa6e4`](#insn-00aaa6e4)

~~~json
{
  "source": "00aaa6e4",
  "target": "00aaa70c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa6ec`](#insn-00aaa6ec)

~~~json
{
  "source": "00aaa6ec",
  "target": "007cf950",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa6f4`](#insn-00aaa6f4)

~~~json
{
  "source": "00aaa6f4",
  "target": "007cfaa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa6fc`](#insn-00aaa6fc)

~~~json
{
  "source": "00aaa6fc",
  "target": "007cfcd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa71c`](#insn-00aaa71c)

~~~json
{
  "source": "00aaa71c",
  "target": "00aaa8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa734`](#insn-00aaa734)

~~~json
{
  "source": "00aaa734",
  "target": "00aaa744",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa740`](#insn-00aaa740)

~~~json
{
  "source": "00aaa740",
  "target": "00aaa8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa74c`](#insn-00aaa74c)

~~~json
{
  "source": "00aaa74c",
  "target": "00aaa73c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa754`](#insn-00aaa754)

~~~json
{
  "source": "00aaa754",
  "target": "00aaa738",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa758`](#insn-00aaa758)

~~~json
{
  "source": "00aaa758",
  "target": "00aaa764",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa760`](#insn-00aaa760)

~~~json
{
  "source": "00aaa760",
  "target": "00aaa78c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa770`](#insn-00aaa770)

~~~json
{
  "source": "00aaa770",
  "target": "00aaa75c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa778`](#insn-00aaa778)

~~~json
{
  "source": "00aaa778",
  "target": "00aaa7e4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa780`](#insn-00aaa780)

~~~json
{
  "source": "00aaa780",
  "target": "00aaa764",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa788`](#insn-00aaa788)

~~~json
{
  "source": "00aaa788",
  "target": "00aaa790",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa794`](#insn-00aaa794)

~~~json
{
  "source": "00aaa794",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa7c0`](#insn-00aaa7c0)

~~~json
{
  "source": "00aaa7c0",
  "target": "00aaa7cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa7d0`](#insn-00aaa7d0)

~~~json
{
  "source": "00aaa7d0",
  "target": "00419064",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa7e0`](#insn-00aaa7e0)

~~~json
{
  "source": "00aaa7e0",
  "target": "00aaa7e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa7ec`](#insn-00aaa7ec)

~~~json
{
  "source": "00aaa7ec",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa7f0`](#insn-00aaa7f0)

~~~json
{
  "source": "00aaa7f0",
  "target": "00aaa7fc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa7f4`](#insn-00aaa7f4)

~~~json
{
  "source": "00aaa7f4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa800`](#insn-00aaa800)

~~~json
{
  "source": "00aaa800",
  "target": "00aaa8cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa80c`](#insn-00aaa80c)

~~~json
{
  "source": "00aaa80c",
  "target": "00aaa7f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa814`](#insn-00aaa814)

~~~json
{
  "source": "00aaa814",
  "target": "00aaa830",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa82c`](#insn-00aaa82c)

~~~json
{
  "source": "00aaa82c",
  "target": "00aaa7f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa838`](#insn-00aaa838)

~~~json
{
  "source": "00aaa838",
  "target": "00aaa818",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa850`](#insn-00aaa850)

~~~json
{
  "source": "00aaa850",
  "target": "00aaa8ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa874`](#insn-00aaa874)

~~~json
{
  "source": "00aaa874",
  "target": "00aaa890",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa87c`](#insn-00aaa87c)

~~~json
{
  "source": "00aaa87c",
  "target": "00aaa8f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa884`](#insn-00aaa884)

~~~json
{
  "source": "00aaa884",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa88c`](#insn-00aaa88c)

~~~json
{
  "source": "00aaa88c",
  "target": "00aaa894",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa8b0`](#insn-00aaa8b0)

~~~json
{
  "source": "00aaa8b0",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa8bc`](#insn-00aaa8bc)

~~~json
{
  "source": "00aaa8bc",
  "target": "00aaa820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa8c4`](#insn-00aaa8c4)

~~~json
{
  "source": "00aaa8c4",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa8c8`](#insn-00aaa8c8)

~~~json
{
  "source": "00aaa8c8",
  "target": "00aaa820",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa8cc`](#insn-00aaa8cc)

~~~json
{
  "source": "00aaa8cc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa8d0`](#insn-00aaa8d0)

~~~json
{
  "source": "00aaa8d0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa8d4`](#insn-00aaa8d4)

~~~json
{
  "source": "00aaa8d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa8d8`](#insn-00aaa8d8)

~~~json
{
  "source": "00aaa8d8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa8dc`](#insn-00aaa8dc)

~~~json
{
  "source": "00aaa8dc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa8e0`](#insn-00aaa8e0)

~~~json
{
  "source": "00aaa8e0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aaa8f0`](#insn-00aaa8f0)

~~~json
{
  "source": "00aaa8f0",
  "target": "0044d968",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aaa8f4`](#insn-00aaa8f4)

~~~json
{
  "source": "00aaa8f4",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
