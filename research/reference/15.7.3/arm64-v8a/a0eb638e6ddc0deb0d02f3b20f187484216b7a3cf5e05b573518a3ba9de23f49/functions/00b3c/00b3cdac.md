# 00b3cdac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00b3cce4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00b3c/00b3cce4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0003.md#compare-9a30079725902720f056c55fee7e2470)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b3cdf0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b3c/00b3cdf0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/inspection-0010.md#compare-0ac47a4b989677fa3c812f26c5968d76)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b3cdac",
  "name": "_ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_",
  "size": 484,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "3a2beb84d94d929175f65f0ee717b31f55eef006080c2ac50ceaa7f2e2c21cd2",
  "source_text_sha256": "3a2beb84d94d929175f65f0ee717b31f55eef006080c2ac50ceaa7f2e2c21cd2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b3cdac",
        "00b3cf8f"
      ]
    ],
    "bytes_sha256": "b05e317af21f8b3069d5b3a3e2bcebf1d5ec01f1105e3dfd7496b9c6b05e7f4f",
    "instruction_count": 121,
    "instruction_bytes": 484,
    "body_bytes": 484,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00be0100](../00be0/00be0100.md)

## 呼び出し先

- [00bdb1b0](../00bdb/00bdb1b0.md)
- [00be00a0](../00be0/00be00a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3250 bytes

~~~c

int _ZNSt6__ndk17__sort4IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_SB_T_
              (uint *param_1,uint *param_2,uint *param_3,uint *param_4,long *param_5)

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
  
                    /* catch() { ... } // from try @ 00b3cd14 with catch @ 00b3cdd8 */
                    /* catch() { ... } // from try @ 00b3cd9c with catch @ 00b3cddc */
  iVar10 = _ZNSt6__ndk17__sort3IRN11flatbuffers17FlatBufferBuilder18TableKeyComparatorIN10reflection4EnumEEEPNS1_6OffsetIS5_EEEEjT0_SB_SB_T_
                     ();
  uVar5 = *param_4;
  uVar6 = *param_3;
  lVar1 = *(long *)(*param_5 + 0x28) + *(long *)(*param_5 + 0x20);
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
        iVar10 = iVar10 + 3;
        *param_1 = uVar5;
        *param_2 = uVar6;
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
<a id="insn-00b3cdac"></a> `00b3cdac` | `fc 6f ba a9` | stp x28,x27,[sp, #-0x60]! | `FALL_THROUGH`
<a id="insn-00b3cdb0"></a> `00b3cdb0` | `fa 67 01 a9` | stp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3cdb4"></a> `00b3cdb4` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3cdb8"></a> `00b3cdb8` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3cdbc"></a> `00b3cdbc` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3cdc0"></a> `00b3cdc0` | `fd 7b 05 a9` | stp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3cdc4"></a> `00b3cdc4` | `fd 43 01 91` | add x29,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b3cdc8"></a> `00b3cdc8` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00b3cdcc"></a> `00b3cdcc` | `e3 03 04 aa` | mov x3,x4 | `FALL_THROUGH`
<a id="insn-00b3cdd0"></a> `00b3cdd0` | `f8 03 04 aa` | mov x24,x4 | `FALL_THROUGH`
<a id="insn-00b3cdd4"></a> `00b3cdd4` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00b3cdd8"></a> `00b3cdd8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b3cddc"></a> `00b3cddc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00b3cde0"></a> `00b3cde0` | `b0 8c 02 94` | bl 0x00be00a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3cde4"></a> `00b3cde4` | `08 03 40 f9` | ldr x8,[x24] | `FALL_THROUGH`
<a id="insn-00b3cde8"></a> `00b3cde8` | `f9 02 40 b9` | ldr w25,[x23] | `FALL_THROUGH`
<a id="insn-00b3cdec"></a> `00b3cdec` | `da 02 40 b9` | ldr w26,[x22] | `FALL_THROUGH`
<a id="insn-00b3cdf0"></a> `00b3cdf0` | `f3 03 00 2a` | mov w19,w0 | `FALL_THROUGH`
<a id="insn-00b3cdf4"></a> `00b3cdf4` | `09 21 42 a9` | ldp x9,x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b3cdf8"></a> `00b3cdf8` | `18 01 09 8b` | add x24,x8,x9 | `FALL_THROUGH`
<a id="insn-00b3cdfc"></a> `00b3cdfc` | `08 03 19 cb` | sub x8,x24,x25 | `FALL_THROUGH`
<a id="insn-00b3ce00"></a> `00b3ce00` | `09 03 1a cb` | sub x9,x24,x26 | `FALL_THROUGH`
<a id="insn-00b3ce04"></a> `00b3ce04` | `0a 01 80 b9` | ldrsw x10,[x8] | `FALL_THROUGH`
<a id="insn-00b3ce08"></a> `00b3ce08` | `2b 01 80 b9` | ldrsw x11,[x9] | `FALL_THROUGH`
<a id="insn-00b3ce0c"></a> `00b3ce0c` | `0a 01 0a cb` | sub x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3ce10"></a> `00b3ce10` | `2b 01 0b cb` | sub x11,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3ce14"></a> `00b3ce14` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3ce18"></a> `00b3ce18` | `6b 09 40 79` | ldrh w11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00b3ce1c"></a> `00b3ce1c` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3ce20"></a> `00b3ce20` | `29 01 0b 8b` | add x9,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3ce24"></a> `00b3ce24` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b3ce28"></a> `00b3ce28` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00b3ce2c"></a> `00b3ce2c` | `00 01 0a 8b` | add x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3ce30"></a> `00b3ce30` | `21 01 0b 8b` | add x1,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3ce34"></a> `00b3ce34` | `1b 44 40 b8` | ldr w27,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00b3ce38"></a> `00b3ce38` | `3c 44 40 b8` | ldr w28,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3ce3c"></a> `00b3ce3c` | `9f 03 1b 6b` | cmp w28,w27 | `FALL_THROUGH`
<a id="insn-00b3ce40"></a> `00b3ce40` | `82 33 9b 1a` | csel w2,w28,w27,cc | `FALL_THROUGH`
<a id="insn-00b3ce44"></a> `00b3ce44` | `db 78 02 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3ce48"></a> `00b3ce48` | `7f 03 1c 6b` | cmp w27,w28 | `FALL_THROUGH`
<a id="insn-00b3ce4c"></a> `00b3ce4c` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3ce50"></a> `00b3ce50` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3ce54"></a> `00b3ce54` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3ce58"></a> `00b3ce58` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3ce5c"></a> `00b3ce5c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3ce60"></a> `00b3ce60` | `81 08 00 54` | b.ne 0x00b3cf70 | `CONDITIONAL_JUMP`
<a id="insn-00b3ce64"></a> `00b3ce64` | `d9 02 00 b9` | str w25,[x22] | `FALL_THROUGH`
<a id="insn-00b3ce68"></a> `00b3ce68` | `fa 02 00 b9` | str w26,[x23] | `FALL_THROUGH`
<a id="insn-00b3ce6c"></a> `00b3ce6c` | `d7 02 40 b9` | ldr w23,[x22] | `FALL_THROUGH`
<a id="insn-00b3ce70"></a> `00b3ce70` | `99 02 40 b9` | ldr w25,[x20] | `FALL_THROUGH`
<a id="insn-00b3ce74"></a> `00b3ce74` | `08 03 17 cb` | sub x8,x24,x23 | `FALL_THROUGH`
<a id="insn-00b3ce78"></a> `00b3ce78` | `09 03 19 cb` | sub x9,x24,x25 | `FALL_THROUGH`
<a id="insn-00b3ce7c"></a> `00b3ce7c` | `0a 01 80 b9` | ldrsw x10,[x8] | `FALL_THROUGH`
<a id="insn-00b3ce80"></a> `00b3ce80` | `2b 01 80 b9` | ldrsw x11,[x9] | `FALL_THROUGH`
<a id="insn-00b3ce84"></a> `00b3ce84` | `0a 01 0a cb` | sub x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3ce88"></a> `00b3ce88` | `2b 01 0b cb` | sub x11,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3ce8c"></a> `00b3ce8c` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3ce90"></a> `00b3ce90` | `6b 09 40 79` | ldrh w11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00b3ce94"></a> `00b3ce94` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3ce98"></a> `00b3ce98` | `29 01 0b 8b` | add x9,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3ce9c"></a> `00b3ce9c` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b3cea0"></a> `00b3cea0` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00b3cea4"></a> `00b3cea4` | `00 01 0a 8b` | add x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3cea8"></a> `00b3cea8` | `21 01 0b 8b` | add x1,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3ceac"></a> `00b3ceac` | `1a 44 40 b8` | ldr w26,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00b3ceb0"></a> `00b3ceb0` | `3b 44 40 b8` | ldr w27,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3ceb4"></a> `00b3ceb4` | `7f 03 1a 6b` | cmp w27,w26 | `FALL_THROUGH`
<a id="insn-00b3ceb8"></a> `00b3ceb8` | `62 33 9a 1a` | csel w2,w27,w26,cc | `FALL_THROUGH`
<a id="insn-00b3cebc"></a> `00b3cebc` | `bd 78 02 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3cec0"></a> `00b3cec0` | `5f 03 1b 6b` | cmp w26,w27 | `FALL_THROUGH`
<a id="insn-00b3cec4"></a> `00b3cec4` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3cec8"></a> `00b3cec8` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3cecc"></a> `00b3cecc` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3ced0"></a> `00b3ced0` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3ced4"></a> `00b3ced4` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3ced8"></a> `00b3ced8` | `61 04 00 54` | b.ne 0x00b3cf64 | `CONDITIONAL_JUMP`
<a id="insn-00b3cedc"></a> `00b3cedc` | `97 02 00 b9` | str w23,[x20] | `FALL_THROUGH`
<a id="insn-00b3cee0"></a> `00b3cee0` | `d9 02 00 b9` | str w25,[x22] | `FALL_THROUGH`
<a id="insn-00b3cee4"></a> `00b3cee4` | `96 02 40 b9` | ldr w22,[x20] | `FALL_THROUGH`
<a id="insn-00b3cee8"></a> `00b3cee8` | `b7 02 40 b9` | ldr w23,[x21] | `FALL_THROUGH`
<a id="insn-00b3ceec"></a> `00b3ceec` | `08 03 16 cb` | sub x8,x24,x22 | `FALL_THROUGH`
<a id="insn-00b3cef0"></a> `00b3cef0` | `09 03 17 cb` | sub x9,x24,x23 | `FALL_THROUGH`
<a id="insn-00b3cef4"></a> `00b3cef4` | `0a 01 80 b9` | ldrsw x10,[x8] | `FALL_THROUGH`
<a id="insn-00b3cef8"></a> `00b3cef8` | `2b 01 80 b9` | ldrsw x11,[x9] | `FALL_THROUGH`
<a id="insn-00b3cefc"></a> `00b3cefc` | `0a 01 0a cb` | sub x10,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3cf00"></a> `00b3cf00` | `2b 01 0b cb` | sub x11,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3cf04"></a> `00b3cf04` | `4a 09 40 79` | ldrh w10,[x10, #0x4] | `FALL_THROUGH`
<a id="insn-00b3cf08"></a> `00b3cf08` | `6b 09 40 79` | ldrh w11,[x11, #0x4] | `FALL_THROUGH`
<a id="insn-00b3cf0c"></a> `00b3cf0c` | `08 01 0a 8b` | add x8,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3cf10"></a> `00b3cf10` | `29 01 0b 8b` | add x9,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3cf14"></a> `00b3cf14` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00b3cf18"></a> `00b3cf18` | `2b 01 40 b9` | ldr w11,[x9] | `FALL_THROUGH`
<a id="insn-00b3cf1c"></a> `00b3cf1c` | `00 01 0a 8b` | add x0,x8,x10 | `FALL_THROUGH`
<a id="insn-00b3cf20"></a> `00b3cf20` | `21 01 0b 8b` | add x1,x9,x11 | `FALL_THROUGH`
<a id="insn-00b3cf24"></a> `00b3cf24` | `18 44 40 b8` | ldr w24,[x0], #0x4 | `FALL_THROUGH`
<a id="insn-00b3cf28"></a> `00b3cf28` | `39 44 40 b8` | ldr w25,[x1], #0x4 | `FALL_THROUGH`
<a id="insn-00b3cf2c"></a> `00b3cf2c` | `3f 03 18 6b` | cmp w25,w24 | `FALL_THROUGH`
<a id="insn-00b3cf30"></a> `00b3cf30` | `22 33 98 1a` | csel w2,w25,w24,cc | `FALL_THROUGH`
<a id="insn-00b3cf34"></a> `00b3cf34` | `9f 78 02 94` | bl 0x00bdb1b0 | `UNCONDITIONAL_CALL`
<a id="insn-00b3cf38"></a> `00b3cf38` | `1f 03 19 6b` | cmp w24,w25 | `FALL_THROUGH`
<a id="insn-00b3cf3c"></a> `00b3cf3c` | `e8 27 9f 1a` | cset w8,cc | `FALL_THROUGH`
<a id="insn-00b3cf40"></a> `00b3cf40` | `1f 00 00 71` | cmp w0,#0x0 | `FALL_THROUGH`
<a id="insn-00b3cf44"></a> `00b3cf44` | `e9 a7 9f 1a` | cset w9,lt | `FALL_THROUGH`
<a id="insn-00b3cf48"></a> `00b3cf48` | `08 01 89 1a` | csel w8,w8,w9,eq | `FALL_THROUGH`
<a id="insn-00b3cf4c"></a> `00b3cf4c` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b3cf50"></a> `00b3cf50` | `e1 00 00 54` | b.ne 0x00b3cf6c | `CONDITIONAL_JUMP`
<a id="insn-00b3cf54"></a> `00b3cf54` | `73 0e 00 11` | add w19,w19,#0x3 | `FALL_THROUGH`
<a id="insn-00b3cf58"></a> `00b3cf58` | `b6 02 00 b9` | str w22,[x21] | `FALL_THROUGH`
<a id="insn-00b3cf5c"></a> `00b3cf5c` | `97 02 00 b9` | str w23,[x20] | `FALL_THROUGH`
<a id="insn-00b3cf60"></a> `00b3cf60` | `04 00 00 14` | b 0x00b3cf70 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3cf64"></a> `00b3cf64` | `73 06 00 11` | add w19,w19,#0x1 | `FALL_THROUGH`
<a id="insn-00b3cf68"></a> `00b3cf68` | `02 00 00 14` | b 0x00b3cf70 | `UNCONDITIONAL_JUMP`
<a id="insn-00b3cf6c"></a> `00b3cf6c` | `73 0a 00 11` | add w19,w19,#0x2 | `FALL_THROUGH`
<a id="insn-00b3cf70"></a> `00b3cf70` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00b3cf74"></a> `00b3cf74` | `fd 7b 45 a9` | ldp x29,x30,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00b3cf78"></a> `00b3cf78` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b3cf7c"></a> `00b3cf7c` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b3cf80"></a> `00b3cf80` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b3cf84"></a> `00b3cf84` | `fa 67 41 a9` | ldp x26,x25,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b3cf88"></a> `00b3cf88` | `fc 6f c6 a8` | ldp x28,x27,[sp], #0x60 | `FALL_THROUGH`
<a id="insn-00b3cf8c"></a> `00b3cf8c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b3cdac`](#insn-00b3cdac) 範囲 `[['00b3cdac', '00b3cdd7']]`
  - `FALL_THROUGH` [`00b3cdd4`](#insn-00b3cdd4) → [`00b3cdd8`](#insn-00b3cdd8)
- ブロック [`00b3cdd8`](#insn-00b3cdd8) 範囲 `[['00b3cdd8', '00b3cddb']]`
  - `FALL_THROUGH` [`00b3cdd8`](#insn-00b3cdd8) → [`00b3cddc`](#insn-00b3cddc)
- ブロック [`00b3cddc`](#insn-00b3cddc) 範囲 `[['00b3cddc', '00b3ce63']]`
  - `CONDITIONAL_JUMP` [`00b3ce60`](#insn-00b3ce60) → [`00b3cf70`](#insn-00b3cf70)
  - `FALL_THROUGH` [`00b3ce60`](#insn-00b3ce60) → [`00b3ce64`](#insn-00b3ce64)
- ブロック [`00b3ce64`](#insn-00b3ce64) 範囲 `[['00b3ce64', '00b3cedb']]`
  - `CONDITIONAL_JUMP` [`00b3ced8`](#insn-00b3ced8) → [`00b3cf64`](#insn-00b3cf64)
  - `FALL_THROUGH` [`00b3ced8`](#insn-00b3ced8) → [`00b3cedc`](#insn-00b3cedc)
- ブロック [`00b3cedc`](#insn-00b3cedc) 範囲 `[['00b3cedc', '00b3cf53']]`
  - `CONDITIONAL_JUMP` [`00b3cf50`](#insn-00b3cf50) → [`00b3cf6c`](#insn-00b3cf6c)
  - `FALL_THROUGH` [`00b3cf50`](#insn-00b3cf50) → [`00b3cf54`](#insn-00b3cf54)
- ブロック [`00b3cf54`](#insn-00b3cf54) 範囲 `[['00b3cf54', '00b3cf63']]`
  - `UNCONDITIONAL_JUMP` [`00b3cf60`](#insn-00b3cf60) → [`00b3cf70`](#insn-00b3cf70)
- ブロック [`00b3cf64`](#insn-00b3cf64) 範囲 `[['00b3cf64', '00b3cf6b']]`
  - `UNCONDITIONAL_JUMP` [`00b3cf68`](#insn-00b3cf68) → [`00b3cf70`](#insn-00b3cf70)
- ブロック [`00b3cf6c`](#insn-00b3cf6c) 範囲 `[['00b3cf6c', '00b3cf6f']]`
  - `FALL_THROUGH` [`00b3cf6c`](#insn-00b3cf6c) → [`00b3cf70`](#insn-00b3cf70)
- ブロック [`00b3cf70`](#insn-00b3cf70) 範囲 `[['00b3cf70', '00b3cf8f']]`

## 命令位置別の参照

- [`00b3cdac`](#insn-00b3cdac) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cdb0`](#insn-00b3cdb0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cdb4`](#insn-00b3cdb4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cdb8`](#insn-00b3cdb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cdbc`](#insn-00b3cdbc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cdc0`](#insn-00b3cdc0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cde0`](#insn-00b3cde0) → [`00be00a0`](../00be0/00be00a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00be00a0` · 推定シンボル `None` · 推定型 `None`
- [`00b3ce44`](#insn-00b3ce44) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b3ce60`](#insn-00b3ce60) → [`00b3cf70`](#insn-00b3cf70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cebc`](#insn-00b3cebc) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b3ced8`](#insn-00b3ced8) → [`00b3cf64`](#insn-00b3cf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cf34`](#insn-00b3cf34) → [`00bdb1b0`](../00bdb/00bdb1b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb1b0` · 推定シンボル `None` · 推定型 `None`
- [`00b3cf50`](#insn-00b3cf50) → [`00b3cf6c`](#insn-00b3cf6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cf60`](#insn-00b3cf60) → [`00b3cf70`](#insn-00b3cf70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cf68`](#insn-00b3cf68) → [`00b3cf70`](#insn-00b3cf70) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cf74`](#insn-00b3cf74) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cf78`](#insn-00b3cf78) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cf7c`](#insn-00b3cf7c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cf80`](#insn-00b3cf80) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b3cf84`](#insn-00b3cf84) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b3cdac`](#insn-00b3cdac)

~~~json
{
  "source": "00b3cdac",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cdb0`](#insn-00b3cdb0)

~~~json
{
  "source": "00b3cdb0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cdb4`](#insn-00b3cdb4)

~~~json
{
  "source": "00b3cdb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cdb8`](#insn-00b3cdb8)

~~~json
{
  "source": "00b3cdb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cdbc`](#insn-00b3cdbc)

~~~json
{
  "source": "00b3cdbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cdc0`](#insn-00b3cdc0)

~~~json
{
  "source": "00b3cdc0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cde0`](#insn-00b3cde0)

~~~json
{
  "source": "00b3cde0",
  "target": "00be00a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ce44`](#insn-00b3ce44)

~~~json
{
  "source": "00b3ce44",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ce60`](#insn-00b3ce60)

~~~json
{
  "source": "00b3ce60",
  "target": "00b3cf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cebc`](#insn-00b3cebc)

~~~json
{
  "source": "00b3cebc",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3ced8`](#insn-00b3ced8)

~~~json
{
  "source": "00b3ced8",
  "target": "00b3cf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cf34`](#insn-00b3cf34)

~~~json
{
  "source": "00b3cf34",
  "target": "00bdb1b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b3cf50`](#insn-00b3cf50)

~~~json
{
  "source": "00b3cf50",
  "target": "00b3cf6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cf60`](#insn-00b3cf60)

~~~json
{
  "source": "00b3cf60",
  "target": "00b3cf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cf68`](#insn-00b3cf68)

~~~json
{
  "source": "00b3cf68",
  "target": "00b3cf70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cf74`](#insn-00b3cf74)

~~~json
{
  "source": "00b3cf74",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cf78`](#insn-00b3cf78)

~~~json
{
  "source": "00b3cf78",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cf7c`](#insn-00b3cf7c)

~~~json
{
  "source": "00b3cf7c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cf80`](#insn-00b3cf80)

~~~json
{
  "source": "00b3cf80",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b3cf84`](#insn-00b3cf84)

~~~json
{
  "source": "00b3cf84",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
