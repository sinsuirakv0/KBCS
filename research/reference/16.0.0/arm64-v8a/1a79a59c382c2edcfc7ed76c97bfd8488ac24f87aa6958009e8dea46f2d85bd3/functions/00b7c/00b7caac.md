# 00b7caac

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 要確認
  - [v15.7.4 → v16.0.0 候補と検査根拠](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/review-0173.md#review-1cb7b0c27cb3432b784758d04af7e7db)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b7ced4`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b7c/00b7ced4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0076.md#compare-802e7aa88875164d9818d45b7aff7899)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b7caac",
  "name": "_ZN11flatbuffers6Parser15SerializeStructERNS_21FlatBufferBuilderImplILb0EEERKNS_9StructDefERKNS_5ValueE",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9f4d03e5e51dec5feb81e84bb4aacf1803be0a86ab825d91e73877611621b76b",
  "source_text_sha256": "9f4d03e5e51dec5feb81e84bb4aacf1803be0a86ab825d91e73877611621b76b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b7caac",
        "00b7cc23"
      ]
    ],
    "bytes_sha256": "cadf8c96d8a54661dea49c39ab101e2521b424706723705f66aa5aab27a3bca6",
    "instruction_count": 94,
    "instruction_bytes": 376,
    "body_bytes": 376,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5c1c0](../00c5c/00c5c1c0.md)

## 呼び出し先

- [00c57c00](../00c57/00c57c00.md)
- [00c5bda0](../00c5b/00c5bda0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3041 bytes

~~~c

void _ZN11flatbuffers6Parser15SerializeStructERNS_21FlatBufferBuilderImplILb0EEERKNS_9StructDefERKNS_5ValueE
               (undefined8 param_1,long param_2,long param_3,long param_4)

{
  undefined4 uVar1;
  ushort uVar2;
  uint uVar3;
  ulong uVar4;
  ulong *puVar5;
  ulong uVar6;
  long lVar7;
  void *__src;
  
  uVar6 = *(ulong *)(param_3 + 0xd8);
  if (*(ulong *)(param_2 + 0x68) < uVar6) {
    *(ulong *)(param_2 + 0x68) = uVar6;
  }
                    /* try { // try from 00b7cadc to 00c7cae3 has its CatchHandler @ 00b7d7fc */
  uVar3 = *(uint *)(param_2 + 0x30);
  uVar6 = uVar6 - 1 & -(ulong)uVar3;
  if (uVar6 != 0) {
    lVar7 = *(long *)(param_2 + 0x40);
    if ((uint)((int)lVar7 - *(int *)(param_2 + 0x48)) < uVar6) {
      _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_2,uVar6);
      lVar7 = *(long *)(param_2 + 0x40);
      uVar3 = *(uint *)(param_2 + 0x30);
    }
    *(undefined1 **)(param_2 + 0x40) = (undefined1 *)(lVar7 - uVar6);
    *(uint *)(param_2 + 0x30) = uVar3 + (int)uVar6;
                    /* try { // try from 00b7cb2c to 00c7cb37 has its CatchHandler @ 00b7d7e8 */
    *(undefined1 *)(lVar7 - uVar6) = 0;
    if (uVar6 != 1) {
      uVar4 = 1;
      do {
                    /* try { // try from 00b7cb38 to 00c7cb4b has its CatchHandler @ 00b7d7d8 */
        *(undefined1 *)(*(long *)(param_2 + 0x40) + uVar4) = 0;
        uVar4 = uVar4 + 1;
      } while (uVar6 != uVar4);
    }
  }
                    /* try { // try from 00b7cb4c to 00c7cb57 has its CatchHandler @ 00b7d7a8 */
  if ((*(byte *)(param_4 + 0x20) & 1) == 0) {
    __src = (void *)(param_4 + 0x21);
                    /* try { // try from 00b7cb5c to 00c7cb73 has its CatchHandler @ 00b7d754 */
    uVar6 = *(ulong *)(param_3 + 0xe0);
  }
  else {
    __src = *(void **)(param_4 + 0x30);
    uVar6 = *(ulong *)(param_3 + 0xe0);
  }
  if (uVar6 != 0) {
    lVar7 = *(long *)(param_2 + 0x40);
                    /* try { // try from 00b7cb78 to 00c7cb8f has its CatchHandler @ 00b7d744 */
    if ((uint)((int)lVar7 - *(int *)(param_2 + 0x48)) < uVar6) {
                    /* try { // try from 00b7cb90 to 00c7cc57 has its CatchHandler @ 00b7c2fc */
      _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_2,uVar6);
      lVar7 = *(long *)(param_2 + 0x40);
    }
    *(void **)(param_2 + 0x40) = (void *)(lVar7 - uVar6);
    *(int *)(param_2 + 0x30) = *(int *)(param_2 + 0x30) + (int)uVar6;
    memcpy((void *)(lVar7 - uVar6),__src,uVar6);
  }
  puVar5 = *(ulong **)(param_2 + 0x48);
  uVar2 = *(ushort *)(param_4 + 0x38);
  uVar1 = *(undefined4 *)(param_2 + 0x30);
  if ((*(int *)(param_2 + 0x40) - (int)puVar5 & 0xfffffff8U) == 0) {
    _ZN11flatbuffers15vector_downwardIjE10reallocateEm(param_2,8);
    puVar5 = *(ulong **)(param_2 + 0x48);
  }
  *puVar5 = (ulong)CONCAT24(uVar2,uVar1);
  *(long *)(param_2 + 0x48) = *(long *)(param_2 + 0x48) + 8;
  *(int *)(param_2 + 0x50) = *(int *)(param_2 + 0x50) + 1;
  if (*(ushort *)(param_2 + 0x54) < uVar2) {
    *(ushort *)(param_2 + 0x54) = uVar2;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b7caac"></a> `00b7caac` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b7cab0"></a> `00b7cab0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7cab4"></a> `00b7cab4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7cab8"></a> `00b7cab8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b7cabc"></a> `00b7cabc` | `49 6c 40 f9` | ldr x9,[x2, #0xd8] | `FALL_THROUGH`
<a id="insn-00b7cac0"></a> `00b7cac0` | `28 34 40 f9` | ldr x8,[x1, #0x68] | `FALL_THROUGH`
<a id="insn-00b7cac4"></a> `00b7cac4` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00b7cac8"></a> `00b7cac8` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00b7cacc"></a> `00b7cacc` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00b7cad0"></a> `00b7cad0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b7cad4"></a> `00b7cad4` | `42 00 00 54` | b.cs 0x00b7cadc | `CONDITIONAL_JUMP`
<a id="insn-00b7cad8"></a> `00b7cad8` | `69 36 00 f9` | str x9,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00b7cadc"></a> `00b7cadc` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7cae0"></a> `00b7cae0` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b7cae4"></a> `00b7cae4` | `ea 03 08 cb` | neg x10,x8 | `FALL_THROUGH`
<a id="insn-00b7cae8"></a> `00b7cae8` | `36 01 0a ea` | ands x22,x9,x10 | `FALL_THROUGH`
<a id="insn-00b7caec"></a> `00b7caec` | `00 03 00 54` | b.eq 0x00b7cb4c | `CONDITIONAL_JUMP`
<a id="insn-00b7caf0"></a> `00b7caf0` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7caf4"></a> `00b7caf4` | `6a 4a 40 b9` | ldr w10,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7caf8"></a> `00b7caf8` | `2a 01 0a 4b` | sub w10,w9,w10 | `FALL_THROUGH`
<a id="insn-00b7cafc"></a> `00b7cafc` | `5f 01 16 eb` | cmp x10,x22 | `FALL_THROUGH`
<a id="insn-00b7cb00"></a> `00b7cb00` | `c2 00 00 54` | b.cs 0x00b7cb18 | `CONDITIONAL_JUMP`
<a id="insn-00b7cb04"></a> `00b7cb04` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7cb08"></a> `00b7cb08` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b7cb0c"></a> `00b7cb0c` | `a5 7c 03 94` | bl 0x00c5bda0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7cb10"></a> `00b7cb10` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7cb14"></a> `00b7cb14` | `68 32 40 b9` | ldr w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7cb18"></a> `00b7cb18` | `29 01 16 cb` | sub x9,x9,x22 | `FALL_THROUGH`
<a id="insn-00b7cb1c"></a> `00b7cb1c` | `08 01 16 0b` | add w8,w8,w22 | `FALL_THROUGH`
<a id="insn-00b7cb20"></a> `00b7cb20` | `df 06 00 f1` | cmp x22,#0x1 | `FALL_THROUGH`
<a id="insn-00b7cb24"></a> `00b7cb24` | `69 22 00 f9` | str x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7cb28"></a> `00b7cb28` | `68 32 00 b9` | str w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7cb2c"></a> `00b7cb2c` | `3f 01 00 39` | strb wzr,[x9] | `FALL_THROUGH`
<a id="insn-00b7cb30"></a> `00b7cb30` | `e0 00 00 54` | b.eq 0x00b7cb4c | `CONDITIONAL_JUMP`
<a id="insn-00b7cb34"></a> `00b7cb34` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7cb38"></a> `00b7cb38` | `69 22 40 f9` | ldr x9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7cb3c"></a> `00b7cb3c` | `3f 69 28 38` | strb wzr,[x9, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00b7cb40"></a> `00b7cb40` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7cb44"></a> `00b7cb44` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00b7cb48"></a> `00b7cb48` | `81 ff ff 54` | b.ne 0x00b7cb38 | `CONDITIONAL_JUMP`
<a id="insn-00b7cb4c"></a> `00b7cb4c` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00b7cb50"></a> `00b7cb50` | `09 0d 42 38` | ldrb w9,[x8, #0x20]! | `FALL_THROUGH`
<a id="insn-00b7cb54"></a> `00b7cb54` | `a9 00 00 37` | tbnz w9,#0x0,0x00b7cb68 | `CONDITIONAL_JUMP`
<a id="insn-00b7cb58"></a> `00b7cb58` | `16 05 00 91` | add x22,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b7cb5c"></a> `00b7cb5c` | `b5 72 40 f9` | ldr x21,[x21, #0xe0] | `FALL_THROUGH`
<a id="insn-00b7cb60"></a> `00b7cb60` | `b5 00 00 b5` | cbnz x21,0x00b7cb74 | `CONDITIONAL_JUMP`
<a id="insn-00b7cb64"></a> `00b7cb64` | `15 00 00 14` | b 0x00b7cbb8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b7cb68"></a> `00b7cb68` | `96 1a 40 f9` | ldr x22,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00b7cb6c"></a> `00b7cb6c` | `b5 72 40 f9` | ldr x21,[x21, #0xe0] | `FALL_THROUGH`
<a id="insn-00b7cb70"></a> `00b7cb70` | `55 02 00 b4` | cbz x21,0x00b7cbb8 | `CONDITIONAL_JUMP`
<a id="insn-00b7cb74"></a> `00b7cb74` | `68 22 40 f9` | ldr x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7cb78"></a> `00b7cb78` | `69 4a 40 b9` | ldr w9,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7cb7c"></a> `00b7cb7c` | `09 01 09 4b` | sub w9,w8,w9 | `FALL_THROUGH`
<a id="insn-00b7cb80"></a> `00b7cb80` | `3f 01 15 eb` | cmp x9,x21 | `FALL_THROUGH`
<a id="insn-00b7cb84"></a> `00b7cb84` | `a2 00 00 54` | b.cs 0x00b7cb98 | `CONDITIONAL_JUMP`
<a id="insn-00b7cb88"></a> `00b7cb88` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7cb8c"></a> `00b7cb8c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00b7cb90"></a> `00b7cb90` | `84 7c 03 94` | bl 0x00c5bda0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7cb94"></a> `00b7cb94` | `68 22 40 f9` | ldr x8,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7cb98"></a> `00b7cb98` | `69 32 40 b9` | ldr w9,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7cb9c"></a> `00b7cb9c` | `00 01 15 cb` | sub x0,x8,x21 | `FALL_THROUGH`
<a id="insn-00b7cba0"></a> `00b7cba0` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b7cba4"></a> `00b7cba4` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-00b7cba8"></a> `00b7cba8` | `28 01 15 0b` | add w8,w9,w21 | `FALL_THROUGH`
<a id="insn-00b7cbac"></a> `00b7cbac` | `60 22 00 f9` | str x0,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7cbb0"></a> `00b7cbb0` | `68 32 00 b9` | str w8,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7cbb4"></a> `00b7cbb4` | `13 6c 03 94` | bl 0x00c57c00 | `UNCONDITIONAL_CALL`
<a id="insn-00b7cbb8"></a> `00b7cbb8` | `69 42 40 b9` | ldr w9,[x19, #0x40] | `FALL_THROUGH`
<a id="insn-00b7cbbc"></a> `00b7cbbc` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7cbc0"></a> `00b7cbc0` | `94 72 40 79` | ldrh w20,[x20, #0x38] | `FALL_THROUGH`
<a id="insn-00b7cbc4"></a> `00b7cbc4` | `75 32 40 b9` | ldr w21,[x19, #0x30] | `FALL_THROUGH`
<a id="insn-00b7cbc8"></a> `00b7cbc8` | `29 01 08 4b` | sub w9,w9,w8 | `FALL_THROUGH`
<a id="insn-00b7cbcc"></a> `00b7cbcc` | `3f 71 7d f2` | tst x9,#0xfffffff8 | `FALL_THROUGH`
<a id="insn-00b7cbd0"></a> `00b7cbd0` | `a1 00 00 54` | b.ne 0x00b7cbe4 | `CONDITIONAL_JUMP`
<a id="insn-00b7cbd4"></a> `00b7cbd4` | `01 01 80 52` | mov w1,#0x8 | `FALL_THROUGH`
<a id="insn-00b7cbd8"></a> `00b7cbd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b7cbdc"></a> `00b7cbdc` | `71 7c 03 94` | bl 0x00c5bda0 | `UNCONDITIONAL_CALL`
<a id="insn-00b7cbe0"></a> `00b7cbe0` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7cbe4"></a> `00b7cbe4` | `95 3e 60 b3` | bfm x21,x20,#0x20,#0xf | `FALL_THROUGH`
<a id="insn-00b7cbe8"></a> `00b7cbe8` | `15 01 00 f9` | str x21,[x8] | `FALL_THROUGH`
<a id="insn-00b7cbec"></a> `00b7cbec` | `68 26 40 f9` | ldr x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7cbf0"></a> `00b7cbf0` | `69 52 40 b9` | ldr w9,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00b7cbf4"></a> `00b7cbf4` | `6a aa 40 79` | ldrh w10,[x19, #0x54] | `FALL_THROUGH`
<a id="insn-00b7cbf8"></a> `00b7cbf8` | `08 21 00 91` | add x8,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00b7cbfc"></a> `00b7cbfc` | `29 05 00 11` | add w9,w9,#0x1 | `FALL_THROUGH`
<a id="insn-00b7cc00"></a> `00b7cc00` | `5f 01 14 6b` | cmp w10,w20 | `FALL_THROUGH`
<a id="insn-00b7cc04"></a> `00b7cc04` | `68 26 00 f9` | str x8,[x19, #0x48] | `FALL_THROUGH`
<a id="insn-00b7cc08"></a> `00b7cc08` | `69 52 00 b9` | str w9,[x19, #0x50] | `FALL_THROUGH`
<a id="insn-00b7cc0c"></a> `00b7cc0c` | `42 00 00 54` | b.cs 0x00b7cc14 | `CONDITIONAL_JUMP`
<a id="insn-00b7cc10"></a> `00b7cc10` | `74 aa 00 79` | strh w20,[x19, #0x54] | `FALL_THROUGH`
<a id="insn-00b7cc14"></a> `00b7cc14` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b7cc18"></a> `00b7cc18` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b7cc1c"></a> `00b7cc1c` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b7cc20"></a> `00b7cc20` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b7caac`](#insn-00b7caac) 範囲 `[['00b7caac', '00b7cad7']]`
  - `CONDITIONAL_JUMP` [`00b7cad4`](#insn-00b7cad4) → [`00b7cadc`](#insn-00b7cadc)
  - `FALL_THROUGH` [`00b7cad4`](#insn-00b7cad4) → [`00b7cad8`](#insn-00b7cad8)
- ブロック [`00b7cad8`](#insn-00b7cad8) 範囲 `[['00b7cad8', '00b7cadb']]`
  - `FALL_THROUGH` [`00b7cad8`](#insn-00b7cad8) → [`00b7cadc`](#insn-00b7cadc)
- ブロック [`00b7cadc`](#insn-00b7cadc) 範囲 `[['00b7cadc', '00b7caef']]`
  - `CONDITIONAL_JUMP` [`00b7caec`](#insn-00b7caec) → [`00b7cb4c`](#insn-00b7cb4c)
  - `FALL_THROUGH` [`00b7caec`](#insn-00b7caec) → [`00b7caf0`](#insn-00b7caf0)
- ブロック [`00b7caf0`](#insn-00b7caf0) 範囲 `[['00b7caf0', '00b7cb03']]`
  - `CONDITIONAL_JUMP` [`00b7cb00`](#insn-00b7cb00) → [`00b7cb18`](#insn-00b7cb18)
  - `FALL_THROUGH` [`00b7cb00`](#insn-00b7cb00) → [`00b7cb04`](#insn-00b7cb04)
- ブロック [`00b7cb04`](#insn-00b7cb04) 範囲 `[['00b7cb04', '00b7cb17']]`
  - `FALL_THROUGH` [`00b7cb14`](#insn-00b7cb14) → [`00b7cb18`](#insn-00b7cb18)
- ブロック [`00b7cb18`](#insn-00b7cb18) 範囲 `[['00b7cb18', '00b7cb2b']]`
  - `FALL_THROUGH` [`00b7cb28`](#insn-00b7cb28) → [`00b7cb2c`](#insn-00b7cb2c)
- ブロック [`00b7cb2c`](#insn-00b7cb2c) 範囲 `[['00b7cb2c', '00b7cb33']]`
  - `CONDITIONAL_JUMP` [`00b7cb30`](#insn-00b7cb30) → [`00b7cb4c`](#insn-00b7cb4c)
  - `FALL_THROUGH` [`00b7cb30`](#insn-00b7cb30) → [`00b7cb34`](#insn-00b7cb34)
- ブロック [`00b7cb34`](#insn-00b7cb34) 範囲 `[['00b7cb34', '00b7cb37']]`
  - `FALL_THROUGH` [`00b7cb34`](#insn-00b7cb34) → [`00b7cb38`](#insn-00b7cb38)
- ブロック [`00b7cb38`](#insn-00b7cb38) 範囲 `[['00b7cb38', '00b7cb4b']]`
  - `CONDITIONAL_JUMP` [`00b7cb48`](#insn-00b7cb48) → [`00b7cb38`](#insn-00b7cb38)
  - `FALL_THROUGH` [`00b7cb48`](#insn-00b7cb48) → [`00b7cb4c`](#insn-00b7cb4c)
- ブロック [`00b7cb4c`](#insn-00b7cb4c) 範囲 `[['00b7cb4c', '00b7cb57']]`
  - `CONDITIONAL_JUMP` [`00b7cb54`](#insn-00b7cb54) → [`00b7cb68`](#insn-00b7cb68)
  - `FALL_THROUGH` [`00b7cb54`](#insn-00b7cb54) → [`00b7cb58`](#insn-00b7cb58)
- ブロック [`00b7cb58`](#insn-00b7cb58) 範囲 `[['00b7cb58', '00b7cb5b']]`
  - `FALL_THROUGH` [`00b7cb58`](#insn-00b7cb58) → [`00b7cb5c`](#insn-00b7cb5c)
- ブロック [`00b7cb5c`](#insn-00b7cb5c) 範囲 `[['00b7cb5c', '00b7cb63']]`
  - `CONDITIONAL_JUMP` [`00b7cb60`](#insn-00b7cb60) → [`00b7cb74`](#insn-00b7cb74)
  - `FALL_THROUGH` [`00b7cb60`](#insn-00b7cb60) → [`00b7cb64`](#insn-00b7cb64)
- ブロック [`00b7cb64`](#insn-00b7cb64) 範囲 `[['00b7cb64', '00b7cb67']]`
  - `UNCONDITIONAL_JUMP` [`00b7cb64`](#insn-00b7cb64) → [`00b7cbb8`](#insn-00b7cbb8)
- ブロック [`00b7cb68`](#insn-00b7cb68) 範囲 `[['00b7cb68', '00b7cb73']]`
  - `CONDITIONAL_JUMP` [`00b7cb70`](#insn-00b7cb70) → [`00b7cbb8`](#insn-00b7cbb8)
  - `FALL_THROUGH` [`00b7cb70`](#insn-00b7cb70) → [`00b7cb74`](#insn-00b7cb74)
- ブロック [`00b7cb74`](#insn-00b7cb74) 範囲 `[['00b7cb74', '00b7cb77']]`
  - `FALL_THROUGH` [`00b7cb74`](#insn-00b7cb74) → [`00b7cb78`](#insn-00b7cb78)
- ブロック [`00b7cb78`](#insn-00b7cb78) 範囲 `[['00b7cb78', '00b7cb87']]`
  - `CONDITIONAL_JUMP` [`00b7cb84`](#insn-00b7cb84) → [`00b7cb98`](#insn-00b7cb98)
  - `FALL_THROUGH` [`00b7cb84`](#insn-00b7cb84) → [`00b7cb88`](#insn-00b7cb88)
- ブロック [`00b7cb88`](#insn-00b7cb88) 範囲 `[['00b7cb88', '00b7cb8f']]`
  - `FALL_THROUGH` [`00b7cb8c`](#insn-00b7cb8c) → [`00b7cb90`](#insn-00b7cb90)
- ブロック [`00b7cb90`](#insn-00b7cb90) 範囲 `[['00b7cb90', '00b7cb97']]`
  - `FALL_THROUGH` [`00b7cb94`](#insn-00b7cb94) → [`00b7cb98`](#insn-00b7cb98)
- ブロック [`00b7cb98`](#insn-00b7cb98) 範囲 `[['00b7cb98', '00b7cbb7']]`
  - `FALL_THROUGH` [`00b7cbb4`](#insn-00b7cbb4) → [`00b7cbb8`](#insn-00b7cbb8)
- ブロック [`00b7cbb8`](#insn-00b7cbb8) 範囲 `[['00b7cbb8', '00b7cbd3']]`
  - `CONDITIONAL_JUMP` [`00b7cbd0`](#insn-00b7cbd0) → [`00b7cbe4`](#insn-00b7cbe4)
  - `FALL_THROUGH` [`00b7cbd0`](#insn-00b7cbd0) → [`00b7cbd4`](#insn-00b7cbd4)
- ブロック [`00b7cbd4`](#insn-00b7cbd4) 範囲 `[['00b7cbd4', '00b7cbe3']]`
  - `FALL_THROUGH` [`00b7cbe0`](#insn-00b7cbe0) → [`00b7cbe4`](#insn-00b7cbe4)
- ブロック [`00b7cbe4`](#insn-00b7cbe4) 範囲 `[['00b7cbe4', '00b7cc0f']]`
  - `CONDITIONAL_JUMP` [`00b7cc0c`](#insn-00b7cc0c) → [`00b7cc14`](#insn-00b7cc14)
  - `FALL_THROUGH` [`00b7cc0c`](#insn-00b7cc0c) → [`00b7cc10`](#insn-00b7cc10)
- ブロック [`00b7cc10`](#insn-00b7cc10) 範囲 `[['00b7cc10', '00b7cc13']]`
  - `FALL_THROUGH` [`00b7cc10`](#insn-00b7cc10) → [`00b7cc14`](#insn-00b7cc14)
- ブロック [`00b7cc14`](#insn-00b7cc14) 範囲 `[['00b7cc14', '00b7cc23']]`

## 命令位置別の参照

- [`00b7caac`](#insn-00b7caac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cab0`](#insn-00b7cab0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cab4`](#insn-00b7cab4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cad4`](#insn-00b7cad4) → [`00b7cadc`](#insn-00b7cadc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7caec`](#insn-00b7caec) → [`00b7cb4c`](#insn-00b7cb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cb00`](#insn-00b7cb00) → [`00b7cb18`](#insn-00b7cb18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cb0c`](#insn-00b7cb0c) → [`00c5bda0`](../00c5b/00c5bda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bda0` · 推定シンボル `None` · 推定型 `None`
- [`00b7cb30`](#insn-00b7cb30) → [`00b7cb4c`](#insn-00b7cb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cb48`](#insn-00b7cb48) → [`00b7cb38`](#insn-00b7cb38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cb54`](#insn-00b7cb54) → [`00b7cb68`](#insn-00b7cb68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cb60`](#insn-00b7cb60) → [`00b7cb74`](#insn-00b7cb74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cb64`](#insn-00b7cb64) → [`00b7cbb8`](#insn-00b7cbb8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cb70`](#insn-00b7cb70) → [`00b7cbb8`](#insn-00b7cbb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cb84`](#insn-00b7cb84) → [`00b7cb98`](#insn-00b7cb98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cb90`](#insn-00b7cb90) → [`00c5bda0`](../00c5b/00c5bda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bda0` · 推定シンボル `None` · 推定型 `None`
- [`00b7cbb4`](#insn-00b7cbb4) → [`00c57c00`](../00c57/00c57c00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57c00` · 推定シンボル `None` · 推定型 `None`
- [`00b7cbd0`](#insn-00b7cbd0) → [`00b7cbe4`](#insn-00b7cbe4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cbdc`](#insn-00b7cbdc) → [`00c5bda0`](../00c5b/00c5bda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bda0` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc0c`](#insn-00b7cc0c) → [`00b7cc14`](#insn-00b7cc14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc14`](#insn-00b7cc14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b7cc18`](#insn-00b7cc18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b7caac`](#insn-00b7caac)

~~~json
{
  "source": "00b7caac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cab0`](#insn-00b7cab0)

~~~json
{
  "source": "00b7cab0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cab4`](#insn-00b7cab4)

~~~json
{
  "source": "00b7cab4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cad4`](#insn-00b7cad4)

~~~json
{
  "source": "00b7cad4",
  "target": "00b7cadc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7caec`](#insn-00b7caec)

~~~json
{
  "source": "00b7caec",
  "target": "00b7cb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cb00`](#insn-00b7cb00)

~~~json
{
  "source": "00b7cb00",
  "target": "00b7cb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cb0c`](#insn-00b7cb0c)

~~~json
{
  "source": "00b7cb0c",
  "target": "00c5bda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cb30`](#insn-00b7cb30)

~~~json
{
  "source": "00b7cb30",
  "target": "00b7cb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cb48`](#insn-00b7cb48)

~~~json
{
  "source": "00b7cb48",
  "target": "00b7cb38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cb54`](#insn-00b7cb54)

~~~json
{
  "source": "00b7cb54",
  "target": "00b7cb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cb60`](#insn-00b7cb60)

~~~json
{
  "source": "00b7cb60",
  "target": "00b7cb74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cb64`](#insn-00b7cb64)

~~~json
{
  "source": "00b7cb64",
  "target": "00b7cbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cb70`](#insn-00b7cb70)

~~~json
{
  "source": "00b7cb70",
  "target": "00b7cbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cb84`](#insn-00b7cb84)

~~~json
{
  "source": "00b7cb84",
  "target": "00b7cb98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cb90`](#insn-00b7cb90)

~~~json
{
  "source": "00b7cb90",
  "target": "00c5bda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cbb4`](#insn-00b7cbb4)

~~~json
{
  "source": "00b7cbb4",
  "target": "00c57c00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cbd0`](#insn-00b7cbd0)

~~~json
{
  "source": "00b7cbd0",
  "target": "00b7cbe4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cbdc`](#insn-00b7cbdc)

~~~json
{
  "source": "00b7cbdc",
  "target": "00c5bda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b7cc0c`](#insn-00b7cc0c)

~~~json
{
  "source": "00b7cc0c",
  "target": "00b7cc14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc14`](#insn-00b7cc14)

~~~json
{
  "source": "00b7cc14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b7cc18`](#insn-00b7cc18)

~~~json
{
  "source": "00b7cc18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
