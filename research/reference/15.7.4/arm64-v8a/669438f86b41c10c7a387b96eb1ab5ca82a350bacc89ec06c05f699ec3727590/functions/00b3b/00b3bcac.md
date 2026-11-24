# 00b3bcac

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b3bc68`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b3b/00b3bc68.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0010.md#compare-da81e6ad7af607fd23b1f6af2840b287)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 対応未確定
  - [v15.7.4 → v16.0.0 版の比較一覧](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/README.md)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3bcac",
  "name": "FUN_00b3bcac",
  "size": 632,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8696cfd4ce21430cc6e9e03b466b5bf67d775c89e09895b89ae4bc9a0f3cbeb7",
  "source_text_sha256": "8696cfd4ce21430cc6e9e03b466b5bf67d775c89e09895b89ae4bc9a0f3cbeb7",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3bcac",
        "00b3bf23"
      ]
    ],
    "bytes_sha256": "1e9b11d44249498e682208b976ce52187947cd47c0803ce587eb9b7fe9c545d8",
    "instruction_count": 158,
    "instruction_bytes": 632,
    "body_bytes": 632,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00b3b138](../00b3b/00b3b138.md)
- [00b3c0c0](../00b3c/00b3c0c0.md)

## 呼び出し先

- [00bdb200](../00bdb/00bdb200.md)
- [00be0170](../00be0/00be0170.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 5453 bytes

~~~c

int FUN_00b3bcac(uint *param_1,uint *param_2,uint *param_3,uint *param_4,uint *param_5,long *param_6
                )

{
  long lVar1;
  uint *puVar2;
  uint *puVar3;
  uint uVar4;
  uint uVar5;
  uint uVar6;
  uint uVar7;
  uint uVar8;
  bool bVar9;
  int iVar10;
  int iVar11;
  int *piVar12;
  int *piVar13;
  
  iVar10 = _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection6ObjectEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_
                     ();
  uVar5 = *param_5;
  uVar6 = *param_4;
  lVar1 = *(long *)(*param_6 + 0x28) + *(long *)(*param_6 + 0x20);
  piVar12 = (int *)(lVar1 - (ulong)uVar5);
  piVar13 = (int *)(lVar1 - (ulong)uVar6);
                    /* catch() { ... } // from try @ 00b3b988 with catch @ 00b3bd18 */
                    /* catch() { ... } // from try @ 00b3b97c with catch @ 00b3bd1c */
                    /* catch() { ... } // from try @ 00b3b878 with catch @ 00b3bd20 */
                    /* catch() { ... } // from try @ 00b3b86c with catch @ 00b3bd24 */
  puVar2 = (uint *)((long)piVar12 + (ulong)*(ushort *)((long)piVar12 + (4 - (long)*piVar12)));
                    /* catch() { ... } // from try @ 00b3b768 with catch @ 00b3bd28 */
  puVar3 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
                    /* catch() { ... } // from try @ 00b3b75c with catch @ 00b3bd2c */
                    /* catch() { ... } // from try @ 00b3b650 with catch @ 00b3bd30 */
  puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
  puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
  uVar7 = *puVar2;
  uVar8 = *puVar3;
  uVar4 = uVar8;
                    /* catch() { ... } // from try @ 00b3b644 with catch @ 00b3bd48 */
  if (uVar7 <= uVar8) {
    uVar4 = uVar7;
  }
  iVar11 = memcmp(puVar2 + 1,puVar3 + 1,(ulong)uVar4);
  bVar9 = uVar7 < uVar8;
                    /* catch() { ... } // from try @ 00b3b598 with catch @ 00b3bd5c */
  if (iVar11 != 0) {
    bVar9 = iVar11 < 0;
  }
                    /* catch() { ... } // from try @ 00b3b58c with catch @ 00b3bd6c */
  if (bVar9) {
    *param_4 = uVar5;
    *param_5 = uVar6;
    uVar5 = *param_4;
    uVar6 = *param_3;
    piVar12 = (int *)(lVar1 - (ulong)uVar5);
    piVar13 = (int *)(lVar1 - (ulong)uVar6);
                    /* catch() { ... } // from try @ 00b3b56c with catch @ 00b3bd8c */
                    /* catch() { ... } // from try @ 00b3b550 with catch @ 00b3bd94 */
                    /* catch() { ... } // from try @ 00b3b538 with catch @ 00b3bd9c */
                    /* catch() { ... } // from try @ 00b3b488 with catch @ 00b3bda0 */
    puVar2 = (uint *)((long)piVar12 + (ulong)*(ushort *)((long)piVar12 + (4 - (long)*piVar12)));
    puVar3 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
    puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
                    /* catch() { ... } // from try @ 00b3b4a4 with catch @ 00b3bdb8 */
    puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
    uVar7 = *puVar2;
                    /* catch() { ... } // from try @ 00b3b4d4 with catch @ 00b3bdc0 */
    uVar8 = *puVar3;
                    /* catch() { ... } // from try @ 00b3b4e8 with catch @ 00b3bdc4 */
    uVar4 = uVar8;
                    /* catch() { ... } // from try @ 00b3b4f8 with catch @ 00b3bdc8 */
    if (uVar7 <= uVar8) {
      uVar4 = uVar7;
    }
    iVar11 = memcmp(puVar2 + 1,puVar3 + 1,(ulong)uVar4);
    bVar9 = uVar7 < uVar8;
    if (iVar11 != 0) {
      bVar9 = iVar11 < 0;
    }
    if (bVar9) {
      *param_3 = uVar5;
      *param_4 = uVar6;
      uVar5 = *param_3;
      uVar6 = *param_2;
      piVar12 = (int *)(lVar1 - (ulong)uVar5);
      piVar13 = (int *)(lVar1 - (ulong)uVar6);
      puVar2 = (uint *)((long)piVar12 + (ulong)*(ushort *)((long)piVar12 + (4 - (long)*piVar12)));
      puVar3 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
      puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
      puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
      uVar7 = *puVar2;
      uVar8 = *puVar3;
      uVar4 = uVar8;
      if (uVar7 <= uVar8) {
        uVar4 = uVar7;
      }
      iVar11 = memcmp(puVar2 + 1,puVar3 + 1,(ulong)uVar4);
      bVar9 = uVar7 < uVar8;
      if (iVar11 != 0) {
        bVar9 = iVar11 < 0;
      }
      if (bVar9) {
        *param_2 = uVar5;
        *param_3 = uVar6;
        uVar5 = *param_2;
        uVar6 = *param_1;
        piVar12 = (int *)(lVar1 - (ulong)uVar5);
        piVar13 = (int *)(lVar1 - (ulong)uVar6);
        puVar2 = (uint *)((long)piVar12 + (ulong)*(ushort *)((long)piVar12 + (4 - (long)*piVar12)));
        puVar3 = (uint *)((long)piVar13 + (ulong)*(ushort *)((long)piVar13 + (4 - (long)*piVar13)));
        puVar2 = (uint *)((long)puVar2 + (ulong)*puVar2);
        puVar3 = (uint *)((long)puVar3 + (ulong)*puVar3);
        uVar7 = *puVar2;
        uVar8 = *puVar3;
        uVar4 = uVar8;
        if (uVar7 <= uVar8) {
          uVar4 = uVar7;
        }
        iVar11 = memcmp(puVar2 + 1,puVar3 + 1,(ulong)uVar4);
        bVar9 = uVar7 < uVar8;
        if (iVar11 != 0) {
          bVar9 = iVar11 < 0;
        }
        if (bVar9) {
          iVar10 = iVar10 + 4;
          *param_1 = uVar5;
          *param_2 = uVar6;
        }
        else {
          iVar10 = iVar10 + 3;
        }
      }
      else {
        iVar10 = iVar10 + 2;
      }
    }
    else {
      iVar10 = iVar10 + 1;
    }
  }
  return iVar10;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b3bcac"></a> `00b3bcac` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b3bcb0"></a> `00b3bcb0` | `fc 6f 01 a9` | stp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3bcb4"></a> `00b3bcb4` | `fa 67 02 a9` | stp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3bcb8"></a> `00b3bcb8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3bcbc"></a> `00b3bcbc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3bcc0"></a> `00b3bcc0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3bcc4"></a> `00b3bcc4` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b3bcc8"></a> `00b3bcc8` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00b3bccc"></a> `00b3bccc` | `f8 03 04 aa` | mov x24,x4 | `FALL_THROUGH`
<a id="insn-00b3bcd0"></a> `00b3bcd0` | `e4 03 05 aa` | mov x4,x5 | `FALL_THROUGH`
<a id="insn-00b3bcd4"></a> `00b3bcd4` | `f9 03 05 aa` | mov x25,x5 | `FALL_THROUGH`
<a id="insn-00b3bcd8"></a> `00b3bcd8` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00b3bcdc"></a> `00b3bcdc` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b3bce0"></a> `00b3bce0` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b3bce4"></a> `00b3bce4` | `e2 07 00 f9` | str x2,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b3bce8"></a> `00b3bce8` | `22 91 02 94` | bl 0x00be0170 | `UNCONDITIONAL_CALL`
<a id="insn-00b3bcec"></a> `00b3bcec` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00b3bcf0"></a> `00b3bcf0` | `1a 03 40 b9` | ldr w26,[x24] | `FALL_THROUGH`
<a id="insn-00b3bcf4"></a> `00b3bcf4` | `fb 02 40 b9` | ldr w27,[x23] | `FALL_THROUGH`
<a id="insn-00b3bcf8"></a> `00b3bcf8` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00b3bcfc"></a> `00b3bcfc` | `09 21 42 a9` | ldp x9,x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b3bd00"></a> `00b3bd00` | `19 01 09 8b` | add x25,x8,x9 | `FALL_THROUGH`
<a id="insn-00b3bd04"></a> `00b3bd04` | `28 03 1a cb` | sub x8,x25,x26 | `FALL_THROUGH`
<a id="insn-00b3bd08"></a> `00b3bd08` | `29 03 1b cb` | sub x9,x25,x27 | `FALL_THROUGH`
<a id="insn-00b3bd0c"></a> `00b3bd0c` | `0a 01 80 b9` | ldrsw x10,[x8] | `FALL_THROUGH`
<a id="insn-00b3bd10"></a> `00b3bd10` | `2b 01 80 b9` | ldrsw x11,[x9] | `FALL_THROUGH`
<a id="insn-00b3bd14"></a> `00b3bd14` | `0a 01 0a cb` | sub x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3bd18"></a> `00b3bd18` | `2b 01 0b cb` | sub x11,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3bd1c"></a> `00b3bd1c` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3bd20"></a> `00b3bd20` | `6b 09 40 79` | ldrh w11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00b3bd24"></a> `00b3bd24` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3bd28"></a> `00b3bd28` | `29 01 0b 8b` | add x9,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3bd2c"></a> `00b3bd2c` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b3bd30"></a> `00b3bd30` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00b3bd34"></a> `00b3bd34` | `00 01 0a 8b` | add x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3bd38"></a> `00b3bd38` | `21 01 0b 8b` | add x1,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3bd3c"></a> `00b3bd3c` | `1c 44 40 b8` | ldr w28,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00b3bd40"></a> `00b3bd40` | `35 44 40 b8` | ldr w21,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3bd44"></a> `00b3bd44` | `bf 02 1c 6b` | cmp w21,w28 | `FALL_THROUGH`
<a id="insn-00b3bd48"></a> `00b3bd48` | `a2 32 9c 1a` | csel w2,w21,w28,cc | `FALL_THROUGH`
<a id="insn-00b3bd4c"></a> `00b3bd4c` | `2d 7d 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b3bd50"></a> `00b3bd50` | `9f 03 15 6b` | cmp w28,w21 | `FALL_THROUGH`
<a id="insn-00b3bd54"></a> `00b3bd54` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3bd58"></a> `00b3bd58` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3bd5c"></a> `00b3bd5c` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3bd60"></a> `00b3bd60` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3bd64"></a> `00b3bd64` | `fc 03 16 2a` | mov w28,w22 | `FALL_THROUGH`
<a id="insn-00b3bd68"></a> `00b3bd68` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3bd6c"></a> `00b3bd6c` | `a1 0c 00 54` | b.ne 0x00b3bf00 | `CONDITIONAL_JUMP`
<a id="insn-00b3bd70"></a> `00b3bd70` | `f6 07 40 f9` | ldr x22,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00b3bd74"></a> `00b3bd74` | `fa 02 00 b9` | str w26,[x23] | `FALL_THROUGH`
<a id="insn-00b3bd78"></a> `00b3bd78` | `1b 03 00 b9` | str w27,[x24] | `FALL_THROUGH`
<a id="insn-00b3bd7c"></a> `00b3bd7c` | `f8 02 40 b9` | ldr w24,[x23] | `FALL_THROUGH`
<a id="insn-00b3bd80"></a> `00b3bd80` | `da 02 40 b9` | ldr w26,[x22] | `FALL_THROUGH`
<a id="insn-00b3bd84"></a> `00b3bd84` | `28 03 18 cb` | sub x8,x25,x24 | `FALL_THROUGH`
<a id="insn-00b3bd88"></a> `00b3bd88` | `29 03 1a cb` | sub x9,x25,x26 | `FALL_THROUGH`
<a id="insn-00b3bd8c"></a> `00b3bd8c` | `0a 01 80 b9` | ldrsw x10,[x8] | `FALL_THROUGH`
<a id="insn-00b3bd90"></a> `00b3bd90` | `2b 01 80 b9` | ldrsw x11,[x9] | `FALL_THROUGH`
<a id="insn-00b3bd94"></a> `00b3bd94` | `0a 01 0a cb` | sub x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3bd98"></a> `00b3bd98` | `2b 01 0b cb` | sub x11,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3bd9c"></a> `00b3bd9c` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3bda0"></a> `00b3bda0` | `6b 09 40 79` | ldrh w11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00b3bda4"></a> `00b3bda4` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3bda8"></a> `00b3bda8` | `29 01 0b 8b` | add x9,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3bdac"></a> `00b3bdac` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b3bdb0"></a> `00b3bdb0` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00b3bdb4"></a> `00b3bdb4` | `00 01 0a 8b` | add x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3bdb8"></a> `00b3bdb8` | `21 01 0b 8b` | add x1,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3bdbc"></a> `00b3bdbc` | `15 44 40 b8` | ldr w21,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00b3bdc0"></a> `00b3bdc0` | `3b 44 40 b8` | ldr w27,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3bdc4"></a> `00b3bdc4` | `7f 03 15 6b` | cmp w27,w21 | `FALL_THROUGH`
<a id="insn-00b3bdc8"></a> `00b3bdc8` | `62 33 95 1a` | csel w2,w27,w21,cc | `FALL_THROUGH`
<a id="insn-00b3bdcc"></a> `00b3bdcc` | `0d 7d 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b3bdd0"></a> `00b3bdd0` | `bf 02 1b 6b` | cmp w21,w27 | `FALL_THROUGH`
<a id="insn-00b3bdd4"></a> `00b3bdd4` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3bdd8"></a> `00b3bdd8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3bddc"></a> `00b3bddc` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3bde0"></a> `00b3bde0` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3bde4"></a> `00b3bde4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3bde8"></a> `00b3bde8` | `21 08 00 54` | b.ne 0x00b3beec | `CONDITIONAL_JUMP`
<a id="insn-00b3bdec"></a> `00b3bdec` | `d8 02 00 b9` | str w24,[x22] | `FALL_THROUGH`
<a id="insn-00b3bdf0"></a> `00b3bdf0` | `fa 02 00 b9` | str w26,[x23] | `FALL_THROUGH`
<a id="insn-00b3bdf4"></a> `00b3bdf4` | `d7 02 40 b9` | ldr w23,[x22] | `FALL_THROUGH`
<a id="insn-00b3bdf8"></a> `00b3bdf8` | `78 02 40 b9` | ldr w24,[x19] | `FALL_THROUGH`
<a id="insn-00b3bdfc"></a> `00b3bdfc` | `28 03 17 cb` | sub x8,x25,x23 | `FALL_THROUGH`
<a id="insn-00b3be00"></a> `00b3be00` | `29 03 18 cb` | sub x9,x25,x24 | `FALL_THROUGH`
<a id="insn-00b3be04"></a> `00b3be04` | `0a 01 80 b9` | ldrsw x10,[x8] | `FALL_THROUGH`
<a id="insn-00b3be08"></a> `00b3be08` | `2b 01 80 b9` | ldrsw x11,[x9] | `FALL_THROUGH`
<a id="insn-00b3be0c"></a> `00b3be0c` | `0a 01 0a cb` | sub x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3be10"></a> `00b3be10` | `2b 01 0b cb` | sub x11,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3be14"></a> `00b3be14` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3be18"></a> `00b3be18` | `6b 09 40 79` | ldrh w11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00b3be1c"></a> `00b3be1c` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3be20"></a> `00b3be20` | `29 01 0b 8b` | add x9,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3be24"></a> `00b3be24` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b3be28"></a> `00b3be28` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00b3be2c"></a> `00b3be2c` | `00 01 0a 8b` | add x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3be30"></a> `00b3be30` | `21 01 0b 8b` | add x1,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3be34"></a> `00b3be34` | `15 44 40 b8` | ldr w21,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00b3be38"></a> `00b3be38` | `3a 44 40 b8` | ldr w26,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3be3c"></a> `00b3be3c` | `5f 03 15 6b` | cmp w26,w21 | `FALL_THROUGH`
<a id="insn-00b3be40"></a> `00b3be40` | `42 33 95 1a` | csel w2,w26,w21,cc | `FALL_THROUGH`
<a id="insn-00b3be44"></a> `00b3be44` | `ef 7c 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b3be48"></a> `00b3be48` | `bf 02 1a 6b` | cmp w21,w26 | `FALL_THROUGH`
<a id="insn-00b3be4c"></a> `00b3be4c` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3be50"></a> `00b3be50` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3be54"></a> `00b3be54` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3be58"></a> `00b3be58` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3be5c"></a> `00b3be5c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3be60"></a> `00b3be60` | `a1 04 00 54` | b.ne 0x00b3bef4 | `CONDITIONAL_JUMP`
<a id="insn-00b3be64"></a> `00b3be64` | `77 02 00 b9` | str w23,[x19] | `FALL_THROUGH`
<a id="insn-00b3be68"></a> `00b3be68` | `d8 02 00 b9` | str w24,[x22] | `FALL_THROUGH`
<a id="insn-00b3be6c"></a> `00b3be6c` | `76 02 40 b9` | ldr w22,[x19] | `FALL_THROUGH`
<a id="insn-00b3be70"></a> `00b3be70` | `97 02 40 b9` | ldr w23,[x20] | `FALL_THROUGH`
<a id="insn-00b3be74"></a> `00b3be74` | `28 03 16 cb` | sub x8,x25,x22 | `FALL_THROUGH`
<a id="insn-00b3be78"></a> `00b3be78` | `29 03 17 cb` | sub x9,x25,x23 | `FALL_THROUGH`
<a id="insn-00b3be7c"></a> `00b3be7c` | `0a 01 80 b9` | ldrsw x10,[x8] | `FALL_THROUGH`
<a id="insn-00b3be80"></a> `00b3be80` | `2b 01 80 b9` | ldrsw x11,[x9] | `FALL_THROUGH`
<a id="insn-00b3be84"></a> `00b3be84` | `0a 01 0a cb` | sub x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3be88"></a> `00b3be88` | `2b 01 0b cb` | sub x11,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3be8c"></a> `00b3be8c` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3be90"></a> `00b3be90` | `6b 09 40 79` | ldrh w11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00b3be94"></a> `00b3be94` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3be98"></a> `00b3be98` | `29 01 0b 8b` | add x9,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3be9c"></a> `00b3be9c` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b3bea0"></a> `00b3bea0` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00b3bea4"></a> `00b3bea4` | `00 01 0a 8b` | add x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3bea8"></a> `00b3bea8` | `21 01 0b 8b` | add x1,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3beac"></a> `00b3beac` | `15 44 40 b8` | ldr w21,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00b3beb0"></a> `00b3beb0` | `38 44 40 b8` | ldr w24,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3beb4"></a> `00b3beb4` | `1f 03 15 6b` | cmp w24,w21 | `FALL_THROUGH`
<a id="insn-00b3beb8"></a> `00b3beb8` | `02 33 95 1a` | csel w2,w24,w21,cc | `FALL_THROUGH`
<a id="insn-00b3bebc"></a> `00b3bebc` | `d1 7c 02 94` | bl 0x00bdb200 | `UNCONDITIONAL_CALL`
<a id="insn-00b3bec0"></a> `00b3bec0` | `bf 02 18 6b` | cmp w21,w24 | `FALL_THROUGH`
<a id="insn-00b3bec4"></a> `00b3bec4` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3bec8"></a> `00b3bec8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3becc"></a> `00b3becc` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3bed0"></a> `00b3bed0` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3bed4"></a> `00b3bed4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3bed8"></a> `00b3bed8` | `21 01 00 54` | b.ne 0x00b3befc | `CONDITIONAL_JUMP`
<a id="insn-00b3bedc"></a> `00b3bedc` | `9c 13 00 11` | add w28,w28,#0x4 | `FALL_THROUGH`
<a id="insn-00b3bee0"></a> `00b3bee0` | `96 02 00 b9` | str w22,[x20] | `FALL_THROUGH`
<a id="insn-00b3bee4"></a> `00b3bee4` | `77 02 00 b9` | str w23,[x19] | `FALL_THROUGH`
<a id="insn-00b3bee8"></a> `00b3bee8` | `06 00 00 14` | b 0x00b3bf00 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3beec"></a> `00b3beec` | `9c 07 00 11` | add w28,w28,#0x1 | `FALL_THROUGH`
<a id="insn-00b3bef0"></a> `00b3bef0` | `04 00 00 14` | b 0x00b3bf00 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3bef4"></a> `00b3bef4` | `9c 0b 00 11` | add w28,w28,#0x2 | `FALL_THROUGH`
<a id="insn-00b3bef8"></a> `00b3bef8` | `02 00 00 14` | b 0x00b3bf00 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3befc"></a> `00b3befc` | `9c 0f 00 11` | add w28,w28,#0x3 | `FALL_THROUGH`
<a id="insn-00b3bf00"></a> `00b3bf00` | `e0 03 1c 2a` | mov w0,w28 | `FALL_THROUGH`
<a id="insn-00b3bf04"></a> `00b3bf04` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00b3bf08"></a> `00b3bf08` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3bf0c"></a> `00b3bf0c` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3bf10"></a> `00b3bf10` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3bf14"></a> `00b3bf14` | `fa 67 42 a9` | ldp x26,x25,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3bf18"></a> `00b3bf18` | `fc 6f 41 a9` | ldp x28,x27,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3bf1c"></a> `00b3bf1c` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00b3bf20"></a> `00b3bf20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3bcac`](#insn-00b3bcac) 範囲 `[['00b3bcac', '00b3bd17']]`
  - `FALL_THROUGH` [`00b3bd14`](#insn-00b3bd14) → [`00b3bd18`](#insn-00b3bd18)
- ブロック [`00b3bd18`](#insn-00b3bd18) 範囲 `[['00b3bd18', '00b3bd1b']]`
  - `FALL_THROUGH` [`00b3bd18`](#insn-00b3bd18) → [`00b3bd1c`](#insn-00b3bd1c)
- ブロック [`00b3bd1c`](#insn-00b3bd1c) 範囲 `[['00b3bd1c', '00b3bd1f']]`
  - `FALL_THROUGH` [`00b3bd1c`](#insn-00b3bd1c) → [`00b3bd20`](#insn-00b3bd20)
- ブロック [`00b3bd20`](#insn-00b3bd20) 範囲 `[['00b3bd20', '00b3bd23']]`
  - `FALL_THROUGH` [`00b3bd20`](#insn-00b3bd20) → [`00b3bd24`](#insn-00b3bd24)
- ブロック [`00b3bd24`](#insn-00b3bd24) 範囲 `[['00b3bd24', '00b3bd27']]`
  - `FALL_THROUGH` [`00b3bd24`](#insn-00b3bd24) → [`00b3bd28`](#insn-00b3bd28)
- ブロック [`00b3bd28`](#insn-00b3bd28) 範囲 `[['00b3bd28', '00b3bd2b']]`
  - `FALL_THROUGH` [`00b3bd28`](#insn-00b3bd28) → [`00b3bd2c`](#insn-00b3bd2c)
- ブロック [`00b3bd2c`](#insn-00b3bd2c) 範囲 `[['00b3bd2c', '00b3bd2f']]`
  - `FALL_THROUGH` [`00b3bd2c`](#insn-00b3bd2c) → [`00b3bd30`](#insn-00b3bd30)
- ブロック [`00b3bd30`](#insn-00b3bd30) 範囲 `[['00b3bd30', '00b3bd47']]`
  - `FALL_THROUGH` [`00b3bd44`](#insn-00b3bd44) → [`00b3bd48`](#insn-00b3bd48)
- ブロック [`00b3bd48`](#insn-00b3bd48) 範囲 `[['00b3bd48', '00b3bd5b']]`
  - `FALL_THROUGH` [`00b3bd58`](#insn-00b3bd58) → [`00b3bd5c`](#insn-00b3bd5c)
- ブロック [`00b3bd5c`](#insn-00b3bd5c) 範囲 `[['00b3bd5c', '00b3bd6b']]`
  - `FALL_THROUGH` [`00b3bd68`](#insn-00b3bd68) → [`00b3bd6c`](#insn-00b3bd6c)
- ブロック [`00b3bd6c`](#insn-00b3bd6c) 範囲 `[['00b3bd6c', '00b3bd6f']]`
  - `CONDITIONAL_JUMP` [`00b3bd6c`](#insn-00b3bd6c) → [`00b3bf00`](#insn-00b3bf00)
  - `FALL_THROUGH` [`00b3bd6c`](#insn-00b3bd6c) → [`00b3bd70`](#insn-00b3bd70)
- ブロック [`00b3bd70`](#insn-00b3bd70) 範囲 `[['00b3bd70', '00b3bd8b']]`
  - `FALL_THROUGH` [`00b3bd88`](#insn-00b3bd88) → [`00b3bd8c`](#insn-00b3bd8c)
- ブロック [`00b3bd8c`](#insn-00b3bd8c) 範囲 `[['00b3bd8c', '00b3bd93']]`
  - `FALL_THROUGH` [`00b3bd90`](#insn-00b3bd90) → [`00b3bd94`](#insn-00b3bd94)
- ブロック [`00b3bd94`](#insn-00b3bd94) 範囲 `[['00b3bd94', '00b3bd9b']]`
  - `FALL_THROUGH` [`00b3bd98`](#insn-00b3bd98) → [`00b3bd9c`](#insn-00b3bd9c)
- ブロック [`00b3bd9c`](#insn-00b3bd9c) 範囲 `[['00b3bd9c', '00b3bd9f']]`
  - `FALL_THROUGH` [`00b3bd9c`](#insn-00b3bd9c) → [`00b3bda0`](#insn-00b3bda0)
- ブロック [`00b3bda0`](#insn-00b3bda0) 範囲 `[['00b3bda0', '00b3bdb7']]`
  - `FALL_THROUGH` [`00b3bdb4`](#insn-00b3bdb4) → [`00b3bdb8`](#insn-00b3bdb8)
- ブロック [`00b3bdb8`](#insn-00b3bdb8) 範囲 `[['00b3bdb8', '00b3bdbf']]`
  - `FALL_THROUGH` [`00b3bdbc`](#insn-00b3bdbc) → [`00b3bdc0`](#insn-00b3bdc0)
- ブロック [`00b3bdc0`](#insn-00b3bdc0) 範囲 `[['00b3bdc0', '00b3bdc3']]`
  - `FALL_THROUGH` [`00b3bdc0`](#insn-00b3bdc0) → [`00b3bdc4`](#insn-00b3bdc4)
- ブロック [`00b3bdc4`](#insn-00b3bdc4) 範囲 `[['00b3bdc4', '00b3bdc7']]`
  - `FALL_THROUGH` [`00b3bdc4`](#insn-00b3bdc4) → [`00b3bdc8`](#insn-00b3bdc8)
- ブロック [`00b3bdc8`](#insn-00b3bdc8) 範囲 `[['00b3bdc8', '00b3bdeb']]`
  - `CONDITIONAL_JUMP` [`00b3bde8`](#insn-00b3bde8) → [`00b3beec`](#insn-00b3beec)
  - `FALL_THROUGH` [`00b3bde8`](#insn-00b3bde8) → [`00b3bdec`](#insn-00b3bdec)
- ブロック [`00b3bdec`](#insn-00b3bdec) 範囲 `[['00b3bdec', '00b3be63']]`
  - `CONDITIONAL_JUMP` [`00b3be60`](#insn-00b3be60) → [`00b3bef4`](#insn-00b3bef4)
  - `FALL_THROUGH` [`00b3be60`](#insn-00b3be60) → [`00b3be64`](#insn-00b3be64)
- ブロック [`00b3be64`](#insn-00b3be64) 範囲 `[['00b3be64', '00b3bedb']]`
  - `CONDITIONAL_JUMP` [`00b3bed8`](#insn-00b3bed8) → [`00b3befc`](#insn-00b3befc)
  - `FALL_THROUGH` [`00b3bed8`](#insn-00b3bed8) → [`00b3bedc`](#insn-00b3bedc)
- ブロック [`00b3bedc`](#insn-00b3bedc) 範囲 `[['00b3bedc', '00b3beeb']]`
  - `UNCONDITIONAL_JUMP` [`00b3bee8`](#insn-00b3bee8) → [`00b3bf00`](#insn-00b3bf00)
- ブロック [`00b3beec`](#insn-00b3beec) 範囲 `[['00b3beec', '00b3bef3']]`
  - `UNCONDITIONAL_JUMP` [`00b3bef0`](#insn-00b3bef0) → [`00b3bf00`](#insn-00b3bf00)
- ブロック [`00b3bef4`](#insn-00b3bef4) 範囲 `[['00b3bef4', '00b3befb']]`
  - `UNCONDITIONAL_JUMP` [`00b3bef8`](#insn-00b3bef8) → [`00b3bf00`](#insn-00b3bf00)
- ブロック [`00b3befc`](#insn-00b3befc) 範囲 `[['00b3befc', '00b3beff']]`
  - `FALL_THROUGH` [`00b3befc`](#insn-00b3befc) → [`00b3bf00`](#insn-00b3bf00)
- ブロック [`00b3bf00`](#insn-00b3bf00) 範囲 `[['00b3bf00', '00b3bf23']]`

## 命令位置別の参照

- [`00b3bcb0`](#insn-00b3bcb0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bcb4`](#insn-00b3bcb4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bcb8`](#insn-00b3bcb8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bcbc`](#insn-00b3bcbc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bcc0`](#insn-00b3bcc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bcc4`](#insn-00b3bcc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bce4`](#insn-00b3bce4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bce8`](#insn-00b3bce8) → [`00be0170`](../00be0/00be0170.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be0170` · 推定シンボル `None` · 推定型 `None`
- [`00b3bd4c`](#insn-00b3bd4c) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b3bd6c`](#insn-00b3bd6c) → [`00b3bf00`](#insn-00b3bf00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bd70`](#insn-00b3bd70) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bdcc`](#insn-00b3bdcc) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b3bde8`](#insn-00b3bde8) → [`00b3beec`](#insn-00b3beec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3be44`](#insn-00b3be44) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b3be60`](#insn-00b3be60) → [`00b3bef4`](#insn-00b3bef4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bebc`](#insn-00b3bebc) → [`00bdb200`](../00bdb/00bdb200.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb200` · 推定シンボル `None` · 推定型 `None`
- [`00b3bed8`](#insn-00b3bed8) → [`00b3befc`](#insn-00b3befc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bee8`](#insn-00b3bee8) → [`00b3bf00`](#insn-00b3bf00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bef0`](#insn-00b3bef0) → [`00b3bf00`](#insn-00b3bf00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bef8`](#insn-00b3bef8) → [`00b3bf00`](#insn-00b3bf00) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bf04`](#insn-00b3bf04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bf08`](#insn-00b3bf08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bf0c`](#insn-00b3bf0c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bf10`](#insn-00b3bf10) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bf14`](#insn-00b3bf14) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3bf18`](#insn-00b3bf18) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3bcb0`](#insn-00b3bcb0)

~~~json
{
  "source": "00b3bcb0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bcb4`](#insn-00b3bcb4)

~~~json
{
  "source": "00b3bcb4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bcb8`](#insn-00b3bcb8)

~~~json
{
  "source": "00b3bcb8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bcbc`](#insn-00b3bcbc)

~~~json
{
  "source": "00b3bcbc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bcc0`](#insn-00b3bcc0)

~~~json
{
  "source": "00b3bcc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bcc4`](#insn-00b3bcc4)

~~~json
{
  "source": "00b3bcc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bce4`](#insn-00b3bce4)

~~~json
{
  "source": "00b3bce4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bce8`](#insn-00b3bce8)

~~~json
{
  "source": "00b3bce8",
  "target": "00be0170",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3bd4c`](#insn-00b3bd4c)

~~~json
{
  "source": "00b3bd4c",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3bd6c`](#insn-00b3bd6c)

~~~json
{
  "source": "00b3bd6c",
  "target": "00b3bf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bd70`](#insn-00b3bd70)

~~~json
{
  "source": "00b3bd70",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bdcc`](#insn-00b3bdcc)

~~~json
{
  "source": "00b3bdcc",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3bde8`](#insn-00b3bde8)

~~~json
{
  "source": "00b3bde8",
  "target": "00b3beec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3be44`](#insn-00b3be44)

~~~json
{
  "source": "00b3be44",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3be60`](#insn-00b3be60)

~~~json
{
  "source": "00b3be60",
  "target": "00b3bef4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bebc`](#insn-00b3bebc)

~~~json
{
  "source": "00b3bebc",
  "target": "00bdb200",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3bed8`](#insn-00b3bed8)

~~~json
{
  "source": "00b3bed8",
  "target": "00b3befc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bee8`](#insn-00b3bee8)

~~~json
{
  "source": "00b3bee8",
  "target": "00b3bf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bef0`](#insn-00b3bef0)

~~~json
{
  "source": "00b3bef0",
  "target": "00b3bf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bef8`](#insn-00b3bef8)

~~~json
{
  "source": "00b3bef8",
  "target": "00b3bf00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bf04`](#insn-00b3bf04)

~~~json
{
  "source": "00b3bf04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bf08`](#insn-00b3bf08)

~~~json
{
  "source": "00b3bf08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bf0c`](#insn-00b3bf0c)

~~~json
{
  "source": "00b3bf0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bf10`](#insn-00b3bf10)

~~~json
{
  "source": "00b3bf10",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bf14`](#insn-00b3bf14)

~~~json
{
  "source": "00b3bf14",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3bf18`](#insn-00b3bf18)

~~~json
{
  "source": "00b3bf18",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
