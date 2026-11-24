# 00bb1efc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0174.md#review-3c4fff4a7c6165a1af2b6d899678fd1b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bb2324`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bb2/00bb2324.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0078.md#compare-1e2c53a434ebd1322c2e3ae0555ebd5e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bb1efc",
  "name": "_ZN11flatbuffers21FlatBufferBuilderImplILb0EE21CreateVectorOfStringsINSt6__ndk111__wrap_iterIPKNS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEEENS_6OffsetINS_6VectorINSE_INS_6StringEEEjEEEET_SK_",
  "size": 464,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d62923abd10461c91bee61e5c9948c96f4992533dd6ad03c79a84f82cea54267",
  "source_text_sha256": "d62923abd10461c91bee61e5c9948c96f4992533dd6ad03c79a84f82cea54267",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bb1efc",
        "00bb20cb"
      ]
    ],
    "bytes_sha256": "acf2b5c21469f913faaf0f1d7f8932f1d193d476dc3ea6f3d5667d3f46419a9c",
    "instruction_count": 116,
    "instruction_bytes": 464,
    "body_bytes": 464,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5bec0](../00c5b/00c5bec0.md)

## 呼び出し先

- [00c5bda0](../00c5b/00c5bda0.md)
- [00c5be50](../00c5b/00c5be50.md)
- [00c5be80](../00c5b/00c5be80.md)
- [00c5bea0](../00c5b/00c5bea0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3893 bytes

~~~c

undefined4
_ZN11flatbuffers21FlatBufferBuilderImplILb0EE21CreateVectorOfStringsINSt6__ndk111__wrap_iterIPKNS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEEEEEENS_6OffsetINS_6VectorINSE_INS_6StringEEEjEEEET_SK_
          (long param_1,byte *param_2,byte *param_3)

{
  uint uVar1;
  byte *pbVar2;
  int iVar3;
  undefined4 uVar4;
  undefined4 *puVar5;
  long lVar6;
  ulong uVar7;
  int iVar8;
  long lVar9;
  ulong uVar10;
  ulong uVar11;
  ulong uVar12;
  long lVar13;
  
  lVar13 = (long)param_3 - (long)param_2;
  lVar9 = lVar13 >> 3;
  uVar10 = lVar9 * -0x5555555555555555;
  if ((ulong)(uint)(*(int *)(param_1 + 0x40) - *(int *)(param_1 + 0x48)) <
      (ulong)(lVar9 * -0x5555555555555554)) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,lVar9 * -0x5555555555555554);
  }
  for (; param_2 != param_3; param_2 = param_2 + 0x18) {
                    /* catch() { ... } // from try @ 00bb1e0c with catch @ 00bb1f78 */
    uVar12 = *(ulong *)(param_2 + 8);
    pbVar2 = *(byte **)(param_2 + 0x10);
    if ((*param_2 & 1) == 0) {
      pbVar2 = param_2 + 1;
      uVar12 = (ulong)(*param_2 >> 1);
    }
    _ZN11flatbuffers21FlatBufferBuilderImplILb0EE16CreateStringImplEPKcm(param_1,pbVar2,uVar12);
    puVar5 = *(undefined4 **)(param_1 + 0x48);
    uVar4 = *(undefined4 *)(param_1 + 0x30);
    if ((*(int *)(param_1 + 0x40) - (int)puVar5 & 0xfffffffcU) == 0) {
      _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,4);
      puVar5 = *(undefined4 **)(param_1 + 0x48);
    }
    *puVar5 = uVar4;
    *(undefined4 **)(param_1 + 0x48) = puVar5 + 1;
  }
  _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11StartVectorINS_6OffsetEjEEvmmm(param_1,uVar10,4,4);
  lVar6 = *(long *)(param_1 + 0x48);
  if (lVar13 != 0) {
    uVar12 = 1;
    do {
      iVar3 = *(int *)(lVar6 + uVar12 * -4);
      if (*(ulong *)(param_1 + 0x68) < 4) {
        *(undefined8 *)(param_1 + 0x68) = 4;
      }
      iVar8 = *(int *)(param_1 + 0x30);
      uVar1 = -iVar8 & 3;
      uVar11 = (ulong)uVar1;
      if (uVar1 != 0) {
        lVar13 = *(long *)(param_1 + 0x40);
                    /* try { // try from 00bb2048 to 00cb2123 has its CatchHandler @ 00bb2048
                       catch() { ... } // from try @ 00bb2048 with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb2144 with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb21c4 with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb2298 with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb23cc with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb24e4 with catch @ 00bb2048
                       catch() { ... } // from try @ 00bb2564 with catch @ 00bb2048 */
        if ((uint)((int)lVar13 - (int)lVar6) < uVar11) {
          _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_1,uVar11);
          lVar13 = *(long *)(param_1 + 0x40);
          iVar8 = *(int *)(param_1 + 0x30);
        }
        *(undefined1 **)(param_1 + 0x40) = (undefined1 *)(lVar13 - uVar11);
        *(uint *)(param_1 + 0x30) = iVar8 + uVar1;
        *(undefined1 *)(lVar13 - uVar11) = 0;
        if (uVar1 != 1) {
          uVar7 = 1;
          do {
            *(undefined1 *)(*(long *)(param_1 + 0x40) + uVar7) = 0;
            uVar7 = uVar7 + 1;
          } while (uVar11 != uVar7);
        }
      }
      _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIjjEET0_T_
                (param_1,(*(int *)(param_1 + 0x30) - iVar3) + 4);
      lVar6 = *(long *)(param_1 + 0x48);
      uVar12 = uVar12 + 1;
    } while (uVar12 <= uVar10);
  }
  *(long *)(param_1 + 0x48) = lVar6 + lVar9 * 0x5555555555555554;
  *(undefined1 *)(param_1 + 0x60) = 0;
  uVar4 = _ZN11flatbuffers21FlatBufferBuilderImplILb0EE11PushElementIjjEET0_T_
                    (param_1,uVar10 & 0xffffffff);
  return uVar4;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bb1efc"></a> `00bb1efc` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bb1f00"></a> `00bb1f00` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb1f04"></a> `00bb1f04` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb1f08"></a> `00bb1f08` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb1f0c"></a> `00bb1f0c` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb1f10"></a> `00bb1f10` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bb1f14"></a> `00bb1f14` | `08 40 40 b9` | ldr w8,[x0, #0x40] | `FALL_THROUGH`
<a id="insn-00bb1f18"></a> `00bb1f18` | `09 48 40 b9` | ldr w9,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00bb1f1c"></a> `00bb1f1c` | `58 00 01 cb` | sub x24,x2,x1 | `FALL_THROUGH`
<a id="insn-00bb1f20"></a> `00bb1f20` | `eb f3 01 b2` | orr x11,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00bb1f24"></a> `00bb1f24` | `0a ff 43 93` | asr x10,x24,#0x3 | `FALL_THROUGH`
<a id="insn-00bb1f28"></a> `00bb1f28` | `6b 55 95 f2` | movk x11,#0xaaab | `FALL_THROUGH`
<a id="insn-00bb1f2c"></a> `00bb1f2c` | `54 7d 0b 9b` | mul x20,x10,x11 | `FALL_THROUGH`
<a id="insn-00bb1f30"></a> `00bb1f30` | `95 f6 7e d3` | lsl x21,x20,#0x2 | `FALL_THROUGH`
<a id="insn-00bb1f34"></a> `00bb1f34` | `08 01 09 4b` | sub w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00bb1f38"></a> `00bb1f38` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-00bb1f3c"></a> `00bb1f3c` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00bb1f40"></a> `00bb1f40` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bb1f44"></a> `00bb1f44` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00bb1f48"></a> `00bb1f48` | `82 00 00 54` | b.cs 0x00bb1f58 | `CONDITIONAL_JUMP`
<a id="insn-00bb1f4c"></a> `00bb1f4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb1f50"></a> `00bb1f50` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bb1f54"></a> `00bb1f54` | `93 a7 02 94` | bl 0x00c5bda0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb1f58"></a> `00bb1f58` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00bb1f5c"></a> `00bb1f5c` | `e1 00 00 54` | b.ne 0x00bb1f78 | `CONDITIONAL_JUMP`
<a id="insn-00bb1f60"></a> `00bb1f60` | `1a 00 00 14` | b 0x00bb1fc8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb1f64"></a> `00bb1f64` | `17 45 00 b8` | str w23,[x8], #0x4 | `FALL_THROUGH`
<a id="insn-00bb1f68"></a> `00bb1f68` | `37 5f 00 91` | add x23,x25,#0x17 | `FALL_THROUGH`
<a id="insn-00bb1f6c"></a> `00bb1f6c` | `ff 02 16 eb` | cmp x23,x22 | `FALL_THROUGH`
<a id="insn-00bb1f70"></a> `00bb1f70` | `68 26 00 f9` | str x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00bb1f74"></a> `00bb1f74` | `a0 02 00 54` | b.eq 0x00bb1fc8 | `CONDITIONAL_JUMP`
<a id="insn-00bb1f78"></a> `00bb1f78` | `e8 02 40 39` | ldrb w8,[x23] | `FALL_THROUGH`
<a id="insn-00bb1f7c"></a> `00bb1f7c` | `e9 aa 40 a9` | ldp x9,x10,[x23, #0x8] | `FALL_THROUGH`
<a id="insn-00bb1f80"></a> `00bb1f80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb1f84"></a> `00bb1f84` | `f9 06 00 91` | add x25,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bb1f88"></a> `00bb1f88` | `0b fd 41 d3` | lsr x11,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb1f8c"></a> `00bb1f8c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb1f90"></a> `00bb1f90` | `41 15 97 9a` | csinc x1,x10,x23,ne | `FALL_THROUGH`
<a id="insn-00bb1f94"></a> `00bb1f94` | `62 01 89 9a` | csel x2,x11,x9,eq | `FALL_THROUGH`
<a id="insn-00bb1f98"></a> `00bb1f98` | `c2 a7 02 94` | bl 0x00c5bea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb1f9c"></a> `00bb1f9c` | `69 42 40 b9` | ldr w9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bb1fa0"></a> `00bb1fa0` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00bb1fa4"></a> `00bb1fa4` | `77 32 40 b9` | ldr w23,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bb1fa8"></a> `00bb1fa8` | `29 01 08 4b` | sub w9,w9,w8 | `FALL_THROUGH`
<a id="insn-00bb1fac"></a> `00bb1fac` | `3f 75 7e f2` | tst x9,#0xfffffffc | `FALL_THROUGH`
<a id="insn-00bb1fb0"></a> `00bb1fb0` | `a1 fd ff 54` | b.ne 0x00bb1f64 | `CONDITIONAL_JUMP`
<a id="insn-00bb1fb4"></a> `00bb1fb4` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00bb1fb8"></a> `00bb1fb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb1fbc"></a> `00bb1fbc` | `79 a7 02 94` | bl 0x00c5bda0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb1fc0"></a> `00bb1fc0` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00bb1fc4"></a> `00bb1fc4` | `e8 ff ff 17` | b 0x00bb1f64 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb1fc8"></a> `00bb1fc8` | `82 00 80 52` | mov w2,#0x4 | `FALL_THROUGH`
<a id="insn-00bb1fcc"></a> `00bb1fcc` | `83 00 80 52` | mov w3,#0x4 | `FALL_THROUGH`
<a id="insn-00bb1fd0"></a> `00bb1fd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb1fd4"></a> `00bb1fd4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bb1fd8"></a> `00bb1fd8` | `aa a7 02 94` | bl 0x00c5be80 | `UNCONDITIONAL_CALL`
<a id="insn-00bb1fdc"></a> `00bb1fdc` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00bb1fe0"></a> `00bb1fe0` | `d8 05 00 b4` | cbz x24,0x00bb2098 | `CONDITIONAL_JUMP`
<a id="insn-00bb1fe4"></a> `00bb1fe4` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00bb1fe8"></a> `00bb1fe8` | `98 00 80 52` | mov w24,#0x4 | `FALL_THROUGH`
<a id="insn-00bb1fec"></a> `00bb1fec` | `0a 00 00 14` | b 0x00bb2014 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb1ff0"></a> `00bb1ff0` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bb1ff4"></a> `00bb1ff4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb1ff8"></a> `00bb1ff8` | `08 01 19 4b` | sub w8,w8,w25 | `FALL_THROUGH`
<a id="insn-00bb1ffc"></a> `00bb1ffc` | `01 11 00 11` | add w1,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bb2000"></a> `00bb2000` | `94 a7 02 94` | bl 0x00c5be50 | `UNCONDITIONAL_CALL`
<a id="insn-00bb2004"></a> `00bb2004` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00bb2008"></a> `00bb2008` | `f7 06 00 91` | add x23,x23,#0x1 | `FALL_THROUGH`
<a id="insn-00bb200c"></a> `00bb200c` | `ff 02 14 eb` | cmp x23,x20 | `FALL_THROUGH`
<a id="insn-00bb2010"></a> `00bb2010` | `48 04 00 54` | b.hi 0x00bb2098 | `CONDITIONAL_JUMP`
<a id="insn-00bb2014"></a> `00bb2014` | `69 36 40 f9` | ldr x9,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bb2018"></a> `00bb2018` | `0a 09 17 cb` | sub x10,x8,x23, LSL #0x2 | `FALL_THROUGH`
<a id="insn-00bb201c"></a> `00bb201c` | `59 01 40 b9` | ldr w25,[x10] | `FALL_THROUGH`
<a id="insn-00bb2020"></a> `00bb2020` | `3f 0d 00 f1` | cmp x9,#0x3 | `FALL_THROUGH`
<a id="insn-00bb2024"></a> `00bb2024` | `48 00 00 54` | b.hi 0x00bb202c | `CONDITIONAL_JUMP`
<a id="insn-00bb2028"></a> `00bb2028` | `78 36 00 f9` | str x24,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bb202c"></a> `00bb202c` | `69 32 40 b9` | ldr w9,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bb2030"></a> `00bb2030` | `ea 03 09 4b` | neg w10,w9 | `FALL_THROUGH`
<a id="insn-00bb2034"></a> `00bb2034` | `56 05 00 72` | ands w22,w10,#0x3 | `FALL_THROUGH`
<a id="insn-00bb2038"></a> `00bb2038` | `c0 fd ff 54` | b.eq 0x00bb1ff0 | `CONDITIONAL_JUMP`
<a id="insn-00bb203c"></a> `00bb203c` | `6a 22 40 f9` | ldr x10,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bb2040"></a> `00bb2040` | `48 01 08 4b` | sub w8,w10,w8 | `FALL_THROUGH`
<a id="insn-00bb2044"></a> `00bb2044` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bb2048"></a> `00bb2048` | `c2 00 00 54` | b.cs 0x00bb2060 | `CONDITIONAL_JUMP`
<a id="insn-00bb204c"></a> `00bb204c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb2050"></a> `00bb2050` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bb2054"></a> `00bb2054` | `53 a7 02 94` | bl 0x00c5bda0 | `UNCONDITIONAL_CALL`
<a id="insn-00bb2058"></a> `00bb2058` | `6a 22 40 f9` | ldr x10,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bb205c"></a> `00bb205c` | `69 32 40 b9` | ldr w9,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bb2060"></a> `00bb2060` | `48 01 16 cb` | sub x8,x10,x22 | `FALL_THROUGH`
<a id="insn-00bb2064"></a> `00bb2064` | `29 01 16 0b` | add w9,w9,w22 | `FALL_THROUGH`
<a id="insn-00bb2068"></a> `00bb2068` | `df 06 00 71` | cmp w22,#0x1 | `FALL_THROUGH`
<a id="insn-00bb206c"></a> `00bb206c` | `68 22 00 f9` | str x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bb2070"></a> `00bb2070` | `69 32 00 b9` | str w9,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00bb2074"></a> `00bb2074` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bb2078"></a> `00bb2078` | `c0 fb ff 54` | b.eq 0x00bb1ff0 | `CONDITIONAL_JUMP`
<a id="insn-00bb207c"></a> `00bb207c` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb2080"></a> `00bb2080` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00bb2084"></a> `00bb2084` | `3f 69 28 38` | strb wzr,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00bb2088"></a> `00bb2088` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bb208c"></a> `00bb208c` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bb2090"></a> `00bb2090` | `81 ff ff 54` | b.ne 0x00bb2080 | `CONDITIONAL_JUMP`
<a id="insn-00bb2094"></a> `00bb2094` | `d7 ff ff 17` | b 0x00bb1ff0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bb2098"></a> `00bb2098` | `08 01 15 cb` | sub x8,x8,x21 | `FALL_THROUGH`
<a id="insn-00bb209c"></a> `00bb209c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bb20a0"></a> `00bb20a0` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-00bb20a4"></a> `00bb20a4` | `68 26 00 f9` | str x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00bb20a8"></a> `00bb20a8` | `7f 82 01 39` | strb wzr,[x19, #0x60] | `FALL_THROUGH`
<a id="insn-00bb20ac"></a> `00bb20ac` | `69 a7 02 94` | bl 0x00c5be50 | `UNCONDITIONAL_CALL`
<a id="insn-00bb20b0"></a> `00bb20b0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bb20b4"></a> `00bb20b4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bb20b8"></a> `00bb20b8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bb20bc"></a> `00bb20bc` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bb20c0"></a> `00bb20c0` | `e0 03 00 2a` | mov w0,w0 | `FALL_THROUGH`
<a id="insn-00bb20c4"></a> `00bb20c4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bb20c8"></a> `00bb20c8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bb1efc`](#insn-00bb1efc) 範囲 `[['00bb1efc', '00bb1f4b']]`
  - `CONDITIONAL_JUMP` [`00bb1f48`](#insn-00bb1f48) → [`00bb1f58`](#insn-00bb1f58)
  - `FALL_THROUGH` [`00bb1f48`](#insn-00bb1f48) → [`00bb1f4c`](#insn-00bb1f4c)
- ブロック [`00bb1f4c`](#insn-00bb1f4c) 範囲 `[['00bb1f4c', '00bb1f57']]`
  - `FALL_THROUGH` [`00bb1f54`](#insn-00bb1f54) → [`00bb1f58`](#insn-00bb1f58)
- ブロック [`00bb1f58`](#insn-00bb1f58) 範囲 `[['00bb1f58', '00bb1f5f']]`
  - `CONDITIONAL_JUMP` [`00bb1f5c`](#insn-00bb1f5c) → [`00bb1f78`](#insn-00bb1f78)
  - `FALL_THROUGH` [`00bb1f5c`](#insn-00bb1f5c) → [`00bb1f60`](#insn-00bb1f60)
- ブロック [`00bb1f60`](#insn-00bb1f60) 範囲 `[['00bb1f60', '00bb1f63']]`
  - `UNCONDITIONAL_JUMP` [`00bb1f60`](#insn-00bb1f60) → [`00bb1fc8`](#insn-00bb1fc8)
- ブロック [`00bb1f64`](#insn-00bb1f64) 範囲 `[['00bb1f64', '00bb1f77']]`
  - `CONDITIONAL_JUMP` [`00bb1f74`](#insn-00bb1f74) → [`00bb1fc8`](#insn-00bb1fc8)
  - `FALL_THROUGH` [`00bb1f74`](#insn-00bb1f74) → [`00bb1f78`](#insn-00bb1f78)
- ブロック [`00bb1f78`](#insn-00bb1f78) 範囲 `[['00bb1f78', '00bb1fb3']]`
  - `CONDITIONAL_JUMP` [`00bb1fb0`](#insn-00bb1fb0) → [`00bb1f64`](#insn-00bb1f64)
  - `FALL_THROUGH` [`00bb1fb0`](#insn-00bb1fb0) → [`00bb1fb4`](#insn-00bb1fb4)
- ブロック [`00bb1fb4`](#insn-00bb1fb4) 範囲 `[['00bb1fb4', '00bb1fc7']]`
  - `UNCONDITIONAL_JUMP` [`00bb1fc4`](#insn-00bb1fc4) → [`00bb1f64`](#insn-00bb1f64)
- ブロック [`00bb1fc8`](#insn-00bb1fc8) 範囲 `[['00bb1fc8', '00bb1fe3']]`
  - `CONDITIONAL_JUMP` [`00bb1fe0`](#insn-00bb1fe0) → [`00bb2098`](#insn-00bb2098)
  - `FALL_THROUGH` [`00bb1fe0`](#insn-00bb1fe0) → [`00bb1fe4`](#insn-00bb1fe4)
- ブロック [`00bb1fe4`](#insn-00bb1fe4) 範囲 `[['00bb1fe4', '00bb1fef']]`
  - `UNCONDITIONAL_JUMP` [`00bb1fec`](#insn-00bb1fec) → [`00bb2014`](#insn-00bb2014)
- ブロック [`00bb1ff0`](#insn-00bb1ff0) 範囲 `[['00bb1ff0', '00bb2013']]`
  - `CONDITIONAL_JUMP` [`00bb2010`](#insn-00bb2010) → [`00bb2098`](#insn-00bb2098)
  - `FALL_THROUGH` [`00bb2010`](#insn-00bb2010) → [`00bb2014`](#insn-00bb2014)
- ブロック [`00bb2014`](#insn-00bb2014) 範囲 `[['00bb2014', '00bb2027']]`
  - `CONDITIONAL_JUMP` [`00bb2024`](#insn-00bb2024) → [`00bb202c`](#insn-00bb202c)
  - `FALL_THROUGH` [`00bb2024`](#insn-00bb2024) → [`00bb2028`](#insn-00bb2028)
- ブロック [`00bb2028`](#insn-00bb2028) 範囲 `[['00bb2028', '00bb202b']]`
  - `FALL_THROUGH` [`00bb2028`](#insn-00bb2028) → [`00bb202c`](#insn-00bb202c)
- ブロック [`00bb202c`](#insn-00bb202c) 範囲 `[['00bb202c', '00bb203b']]`
  - `CONDITIONAL_JUMP` [`00bb2038`](#insn-00bb2038) → [`00bb1ff0`](#insn-00bb1ff0)
  - `FALL_THROUGH` [`00bb2038`](#insn-00bb2038) → [`00bb203c`](#insn-00bb203c)
- ブロック [`00bb203c`](#insn-00bb203c) 範囲 `[['00bb203c', '00bb2047']]`
  - `FALL_THROUGH` [`00bb2044`](#insn-00bb2044) → [`00bb2048`](#insn-00bb2048)
- ブロック [`00bb2048`](#insn-00bb2048) 範囲 `[['00bb2048', '00bb204b']]`
  - `CONDITIONAL_JUMP` [`00bb2048`](#insn-00bb2048) → [`00bb2060`](#insn-00bb2060)
  - `FALL_THROUGH` [`00bb2048`](#insn-00bb2048) → [`00bb204c`](#insn-00bb204c)
- ブロック [`00bb204c`](#insn-00bb204c) 範囲 `[['00bb204c', '00bb205f']]`
  - `FALL_THROUGH` [`00bb205c`](#insn-00bb205c) → [`00bb2060`](#insn-00bb2060)
- ブロック [`00bb2060`](#insn-00bb2060) 範囲 `[['00bb2060', '00bb207b']]`
  - `CONDITIONAL_JUMP` [`00bb2078`](#insn-00bb2078) → [`00bb1ff0`](#insn-00bb1ff0)
  - `FALL_THROUGH` [`00bb2078`](#insn-00bb2078) → [`00bb207c`](#insn-00bb207c)
- ブロック [`00bb207c`](#insn-00bb207c) 範囲 `[['00bb207c', '00bb207f']]`
  - `FALL_THROUGH` [`00bb207c`](#insn-00bb207c) → [`00bb2080`](#insn-00bb2080)
- ブロック [`00bb2080`](#insn-00bb2080) 範囲 `[['00bb2080', '00bb2093']]`
  - `CONDITIONAL_JUMP` [`00bb2090`](#insn-00bb2090) → [`00bb2080`](#insn-00bb2080)
  - `FALL_THROUGH` [`00bb2090`](#insn-00bb2090) → [`00bb2094`](#insn-00bb2094)
- ブロック [`00bb2094`](#insn-00bb2094) 範囲 `[['00bb2094', '00bb2097']]`
  - `UNCONDITIONAL_JUMP` [`00bb2094`](#insn-00bb2094) → [`00bb1ff0`](#insn-00bb1ff0)
- ブロック [`00bb2098`](#insn-00bb2098) 範囲 `[['00bb2098', '00bb20cb']]`

## 命令位置別の参照

- [`00bb1efc`](#insn-00bb1efc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f00`](#insn-00bb1f00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f04`](#insn-00bb1f04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f08`](#insn-00bb1f08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f0c`](#insn-00bb1f0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f48`](#insn-00bb1f48) → [`00bb1f58`](#insn-00bb1f58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f54`](#insn-00bb1f54) → [`00c5bda0`](../00c5b/00c5bda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bda0` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f5c`](#insn-00bb1f5c) → [`00bb1f78`](#insn-00bb1f78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f60`](#insn-00bb1f60) → [`00bb1fc8`](#insn-00bb1fc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f74`](#insn-00bb1f74) → [`00bb1fc8`](#insn-00bb1fc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1f98`](#insn-00bb1f98) → [`00c5bea0`](../00c5b/00c5bea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bea0` · 推定シンボル `None` · 推定型 `None`
- [`00bb1fb0`](#insn-00bb1fb0) → [`00bb1f64`](#insn-00bb1f64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1fbc`](#insn-00bb1fbc) → [`00c5bda0`](../00c5b/00c5bda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bda0` · 推定シンボル `None` · 推定型 `None`
- [`00bb1fc4`](#insn-00bb1fc4) → [`00bb1f64`](#insn-00bb1f64) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1fd8`](#insn-00bb1fd8) → [`00c5be80`](../00c5b/00c5be80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be80` · 推定シンボル `None` · 推定型 `None`
- [`00bb1fe0`](#insn-00bb1fe0) → [`00bb2098`](#insn-00bb2098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb1fec`](#insn-00bb1fec) → [`00bb2014`](#insn-00bb2014) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb2000`](#insn-00bb2000) → [`00c5be50`](../00c5b/00c5be50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be50` · 推定シンボル `None` · 推定型 `None`
- [`00bb2010`](#insn-00bb2010) → [`00bb2098`](#insn-00bb2098) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb2024`](#insn-00bb2024) → [`00bb202c`](#insn-00bb202c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb2038`](#insn-00bb2038) → [`00bb1ff0`](#insn-00bb1ff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb2048`](#insn-00bb2048) → [`00bb2060`](#insn-00bb2060) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb2054`](#insn-00bb2054) → [`00c5bda0`](../00c5b/00c5bda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bda0` · 推定シンボル `None` · 推定型 `None`
- [`00bb2078`](#insn-00bb2078) → [`00bb1ff0`](#insn-00bb1ff0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb2090`](#insn-00bb2090) → [`00bb2080`](#insn-00bb2080) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb2094`](#insn-00bb2094) → [`00bb1ff0`](#insn-00bb1ff0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb20ac`](#insn-00bb20ac) → [`00c5be50`](../00c5b/00c5be50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5be50` · 推定シンボル `None` · 推定型 `None`
- [`00bb20b0`](#insn-00bb20b0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb20b4`](#insn-00bb20b4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb20b8`](#insn-00bb20b8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bb20bc`](#insn-00bb20bc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bb1efc`](#insn-00bb1efc)

~~~json
{
  "source": "00bb1efc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f00`](#insn-00bb1f00)

~~~json
{
  "source": "00bb1f00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f04`](#insn-00bb1f04)

~~~json
{
  "source": "00bb1f04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f08`](#insn-00bb1f08)

~~~json
{
  "source": "00bb1f08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f0c`](#insn-00bb1f0c)

~~~json
{
  "source": "00bb1f0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f48`](#insn-00bb1f48)

~~~json
{
  "source": "00bb1f48",
  "target": "00bb1f58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f54`](#insn-00bb1f54)

~~~json
{
  "source": "00bb1f54",
  "target": "00c5bda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb1f5c`](#insn-00bb1f5c)

~~~json
{
  "source": "00bb1f5c",
  "target": "00bb1f78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f60`](#insn-00bb1f60)

~~~json
{
  "source": "00bb1f60",
  "target": "00bb1fc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f74`](#insn-00bb1f74)

~~~json
{
  "source": "00bb1f74",
  "target": "00bb1fc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1f98`](#insn-00bb1f98)

~~~json
{
  "source": "00bb1f98",
  "target": "00c5bea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb1fb0`](#insn-00bb1fb0)

~~~json
{
  "source": "00bb1fb0",
  "target": "00bb1f64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1fbc`](#insn-00bb1fbc)

~~~json
{
  "source": "00bb1fbc",
  "target": "00c5bda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb1fc4`](#insn-00bb1fc4)

~~~json
{
  "source": "00bb1fc4",
  "target": "00bb1f64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1fd8`](#insn-00bb1fd8)

~~~json
{
  "source": "00bb1fd8",
  "target": "00c5be80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb1fe0`](#insn-00bb1fe0)

~~~json
{
  "source": "00bb1fe0",
  "target": "00bb2098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb1fec`](#insn-00bb1fec)

~~~json
{
  "source": "00bb1fec",
  "target": "00bb2014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb2000`](#insn-00bb2000)

~~~json
{
  "source": "00bb2000",
  "target": "00c5be50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb2010`](#insn-00bb2010)

~~~json
{
  "source": "00bb2010",
  "target": "00bb2098",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb2024`](#insn-00bb2024)

~~~json
{
  "source": "00bb2024",
  "target": "00bb202c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb2038`](#insn-00bb2038)

~~~json
{
  "source": "00bb2038",
  "target": "00bb1ff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb2048`](#insn-00bb2048)

~~~json
{
  "source": "00bb2048",
  "target": "00bb2060",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb2054`](#insn-00bb2054)

~~~json
{
  "source": "00bb2054",
  "target": "00c5bda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb2078`](#insn-00bb2078)

~~~json
{
  "source": "00bb2078",
  "target": "00bb1ff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb2090`](#insn-00bb2090)

~~~json
{
  "source": "00bb2090",
  "target": "00bb2080",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb2094`](#insn-00bb2094)

~~~json
{
  "source": "00bb2094",
  "target": "00bb1ff0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb20ac`](#insn-00bb20ac)

~~~json
{
  "source": "00bb20ac",
  "target": "00c5be50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bb20b0`](#insn-00bb20b0)

~~~json
{
  "source": "00bb20b0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb20b4`](#insn-00bb20b4)

~~~json
{
  "source": "00bb20b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb20b8`](#insn-00bb20b8)

~~~json
{
  "source": "00bb20b8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bb20bc`](#insn-00bb20bc)

~~~json
{
  "source": "00bb20bc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
