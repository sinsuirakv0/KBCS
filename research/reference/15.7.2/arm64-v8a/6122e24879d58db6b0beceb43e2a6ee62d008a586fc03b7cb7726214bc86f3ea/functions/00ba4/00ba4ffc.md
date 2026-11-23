# 00ba4ffc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ba50c4`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ba5/00ba50c4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0077.md#compare-c6af0ecd780bc0cd973fac14c68cb385)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ba4ffc",
  "name": "FUN_00ba4ffc",
  "size": 676,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ff4b4bfc1e1be911febccc5067aa40be0052727bc837c1ea67d59c7b6f15c3be",
  "source_text_sha256": "ff4b4bfc1e1be911febccc5067aa40be0052727bc837c1ea67d59c7b6f15c3be",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ba4ffc",
        "00ba529f"
      ]
    ],
    "bytes_sha256": "2fe6050178357fd120fd3dde2f83a168cf1220bcb6969e98f40cbc0a2cae3412",
    "instruction_count": 169,
    "instruction_bytes": 676,
    "body_bytes": 676,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00ba82ec](../00ba8/00ba82ec.md)

## 呼び出し先

- [00ba05e4](../00ba0/00ba05e4.md)
- [00ba5360](../00ba5/00ba5360.md)
- [00ba54a4](../00ba5/00ba54a4.md)
- [00ba55e8](../00ba5/00ba55e8.md)
- [00ba572c](../00ba5/00ba572c.md)
- [00ba5870](../00ba5/00ba5870.md)
- [00ba59b4](../00ba5/00ba59b4.md)
- [00ba5af8](../00ba5/00ba5af8.md)
- [00ba5c3c](../00ba5/00ba5c3c.md)
- [00ba5d80](../00ba5/00ba5d80.md)
- [00ba5ec4](../00ba5/00ba5ec4.md)
- [00ba6008](../00ba6/00ba6008.md)
- [00ba614c](../00ba6/00ba614c.md)
- [00ba6290](../00ba6/00ba6290.md)
- [00ba63d4](../00ba6/00ba63d4.md)
- [00ba6518](../00ba6/00ba6518.md)
- [00ba665c](../00ba6/00ba665c.md)
- [00ba67a0](../00ba6/00ba67a0.md)
- [00ba68e4](../00ba6/00ba68e4.md)
- [00ba6a28](../00ba6/00ba6a28.md)
- [00ba6b6c](../00ba6/00ba6b6c.md)
- [00ba6cb0](../00ba6/00ba6cb0.md)
- [00ba6df4](../00ba6/00ba6df4.md)
- [00ba6f38](../00ba6/00ba6f38.md)
- [00ba707c](../00ba7/00ba707c.md)
- [00ba71c0](../00ba7/00ba71c0.md)
- [00ba7304](../00ba7/00ba7304.md)
- [00ba7448](../00ba7/00ba7448.md)
- [00ba758c](../00ba7/00ba758c.md)
- [00ba76d0](../00ba7/00ba76d0.md)
- [00ba7814](../00ba7/00ba7814.md)
- [00bb896c](../00bb8/00bb896c.md)
- [00bd6d60](../00bd6/00bd6d60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3253 bytes

~~~c

void FUN_00ba4ffc(undefined8 *param_1,undefined8 *param_2,long param_3,uint param_4)

{
  bool bVar1;
  long lVar2;
  long lVar3;
  long lVar4;
  ulong uVar6;
  ulong uVar5;
  
  *param_1 = &PTR_FUN_00c13818;
  param_1[1] = 0xffffffffffffffff;
  *(undefined1 *)(param_1 + 0x23) = 1;
  param_1[6] = 0;
  param_1[5] = 0;
  param_1[2] = param_1 + 5;
  param_1[8] = 0;
  param_1[7] = 0;
  param_1[10] = 0;
  param_1[9] = 0;
  param_1[0xc] = 0;
  param_1[0xb] = 0;
  param_1[0xe] = 0;
  param_1[0xd] = 0;
  param_1[0x10] = 0;
  param_1[0xf] = 0;
  param_1[0x12] = 0;
  param_1[0x11] = 0;
  param_1[0x14] = 0;
  param_1[0x13] = 0;
  param_1[0x16] = 0;
  param_1[0x15] = 0;
  param_1[0x18] = 0;
  param_1[0x17] = 0;
  param_1[0x1a] = 0;
  param_1[0x19] = 0;
  param_1[0x1c] = 0;
  param_1[0x1b] = 0;
  param_1[0x1e] = 0;
  param_1[0x1d] = 0;
  param_1[0x20] = 0;
  param_1[0x1f] = 0;
  param_1[0x22] = 0;
  param_1[0x21] = 0;
  param_1[3] = param_1 + 0x23;
  param_1[4] = param_1 + 0x23;
  FUN_00ba05e4(param_1 + 0x24,param_2 + 0x24,param_3 + 0x120,param_4);
  if (param_1 != param_2) {
    FUN_00bb896c(param_1 + 2,param_2[2],param_2[3],(long)(param_2[3] - param_2[2]) >> 3);
  }
  lVar3 = param_1[2];
  lVar2 = param_1[3];
  if (lVar2 != lVar3) {
    uVar5 = 0;
    uVar6 = 1;
    do {
      lVar4 = *(long *)(lVar3 + uVar5 * 8);
      if (lVar4 != 0) {
        FUN_00bd6d60(1,lVar4 + 8);
        lVar3 = param_1[2];
        lVar2 = param_1[3];
      }
      bVar1 = uVar6 < (ulong)(lVar2 - lVar3 >> 3);
      uVar5 = uVar6;
      uVar6 = (ulong)((int)uVar6 + 1);
    } while (bVar1);
  }
  if ((param_4 >> 3 & 1) != 0) {
    FUN_00ba5360(param_1,param_3);
                    /* try { // try from 00ba511c to 00ca517b has its CatchHandler @ 00ba5534 */
    FUN_00ba54a4(param_1,param_3);
  }
  if ((param_4 & 1) != 0) {
    FUN_00ba55e8(param_1,param_3);
    FUN_00ba572c(param_1,param_3);
    FUN_00ba5870(param_1,param_3);
    FUN_00ba59b4(param_1,param_3);
    FUN_00ba5af8(param_1,param_3);
    FUN_00ba5c3c(param_1,param_3);
    FUN_00ba5d80(param_1,param_3);
    FUN_00ba5ec4(param_1,param_3);
  }
  if ((param_4 >> 4 & 1) != 0) {
                    /* try { // try from 00ba5190 to 00ca51df has its CatchHandler @ 00ba5540 */
    FUN_00ba6008(param_1,param_3);
    FUN_00ba614c(param_1,param_3);
    FUN_00ba6290(param_1,param_3);
    FUN_00ba63d4(param_1,param_3);
    FUN_00ba6518(param_1,param_3);
    FUN_00ba665c(param_1,param_3);
    FUN_00ba67a0(param_1,param_3);
                    /* try { // try from 00ba51e0 to 00ca524b has its CatchHandler @ 00ba4fb0 */
    FUN_00ba68e4(param_1,param_3);
  }
  if ((param_4 >> 1 & 1) != 0) {
    FUN_00ba6a28(param_1,param_3);
    FUN_00ba6b6c(param_1,param_3);
    FUN_00ba6cb0(param_1,param_3);
    FUN_00ba6df4(param_1,param_3);
    FUN_00ba6f38(param_1,param_3);
    FUN_00ba707c(param_1,param_3);
  }
  if ((param_4 >> 2 & 1) != 0) {
    FUN_00ba71c0(param_1,param_3);
                    /* try { // try from 00ba524c to 00ca529b has its CatchHandler @ 00ba5540 */
    FUN_00ba7304(param_1,param_3);
    FUN_00ba7448(param_1,param_3);
    FUN_00ba758c(param_1,param_3);
  }
  if ((param_4 >> 5 & 1) != 0) {
    FUN_00ba76d0(param_1,param_3);
    FUN_00ba7814(param_1,param_3);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ba4ffc"></a> `00ba4ffc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00ba5000"></a> `00ba5000` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00ba5004"></a> `00ba5004` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba5008"></a> `00ba5008` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba500c"></a> `00ba500c` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba5010"></a> `00ba5010` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00ba5014"></a> `00ba5014` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-00ba5018"></a> `00ba5018` | `08 00 80 92` | mov x8,#-0x1 | `FALL_THROUGH`
<a id="insn-00ba501c"></a> `00ba501c` | `69 03 00 d0` | adrp x9,0xc13000 | `FALL_THROUGH`
<a id="insn-00ba5020"></a> `00ba5020` | `29 61 20 91` | add x9,x9,#0x818 | `FALL_THROUGH`
<a id="insn-00ba5024"></a> `00ba5024` | `f6 03 03 2a` | mov w22,w3 | `FALL_THROUGH`
<a id="insn-00ba5028"></a> `00ba5028` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00ba502c"></a> `00ba502c` | `09 20 00 a9` | stp x9,x8,[x0] | `FALL_THROUGH`
<a id="insn-00ba5030"></a> `00ba5030` | `28 00 80 52` | mov w8,#0x1 | `FALL_THROUGH`
<a id="insn-00ba5034"></a> `00ba5034` | `f7 03 01 aa` | mov x23,x1 | `FALL_THROUGH`
<a id="insn-00ba5038"></a> `00ba5038` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ba503c"></a> `00ba503c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00ba5040"></a> `00ba5040` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00ba5044"></a> `00ba5044` | `08 60 04 39` | strb w8,[x0, #0x118] | `FALL_THROUGH`
<a id="insn-00ba5048"></a> `00ba5048` | `08 60 04 91` | add x8,x0,#0x118 | `FALL_THROUGH`
<a id="insn-00ba504c"></a> `00ba504c` | `00 8f 82 3c` | str q0,[x24, #0x28]! | `FALL_THROUGH`
<a id="insn-00ba5050"></a> `00ba5050` | `98 0e 01 f8` | str x24,[x20, #0x10]! | `FALL_THROUGH`
<a id="insn-00ba5054"></a> `00ba5054` | `00 80 83 3c` | stur q0,[x0, #0x38] | `FALL_THROUGH`
<a id="insn-00ba5058"></a> `00ba5058` | `00 80 84 3c` | stur q0,[x0, #0x48] | `FALL_THROUGH`
<a id="insn-00ba505c"></a> `00ba505c` | `00 80 85 3c` | stur q0,[x0, #0x58] | `FALL_THROUGH`
<a id="insn-00ba5060"></a> `00ba5060` | `00 80 86 3c` | stur q0,[x0, #0x68] | `FALL_THROUGH`
<a id="insn-00ba5064"></a> `00ba5064` | `00 80 87 3c` | stur q0,[x0, #0x78] | `FALL_THROUGH`
<a id="insn-00ba5068"></a> `00ba5068` | `00 80 88 3c` | stur q0,[x0, #0x88] | `FALL_THROUGH`
<a id="insn-00ba506c"></a> `00ba506c` | `00 80 89 3c` | stur q0,[x0, #0x98] | `FALL_THROUGH`
<a id="insn-00ba5070"></a> `00ba5070` | `00 80 8a 3c` | stur q0,[x0, #0xa8] | `FALL_THROUGH`
<a id="insn-00ba5074"></a> `00ba5074` | `00 80 8b 3c` | stur q0,[x0, #0xb8] | `FALL_THROUGH`
<a id="insn-00ba5078"></a> `00ba5078` | `00 80 8c 3c` | stur q0,[x0, #0xc8] | `FALL_THROUGH`
<a id="insn-00ba507c"></a> `00ba507c` | `00 80 8d 3c` | stur q0,[x0, #0xd8] | `FALL_THROUGH`
<a id="insn-00ba5080"></a> `00ba5080` | `00 80 8e 3c` | stur q0,[x0, #0xe8] | `FALL_THROUGH`
<a id="insn-00ba5084"></a> `00ba5084` | `00 80 8f 3c` | stur q0,[x0, #0xf8] | `FALL_THROUGH`
<a id="insn-00ba5088"></a> `00ba5088` | `00 3b 80 3d` | str q0,[x24, #0xe0] | `FALL_THROUGH`
<a id="insn-00ba508c"></a> `00ba508c` | `08 a0 01 a9` | stp x8,x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00ba5090"></a> `00ba5090` | `08 80 04 91` | add x8,x0,#0x120 | `FALL_THROUGH`
<a id="insn-00ba5094"></a> `00ba5094` | `20 80 04 91` | add x0,x1,#0x120 | `FALL_THROUGH`
<a id="insn-00ba5098"></a> `00ba5098` | `41 80 04 91` | add x1,x2,#0x120 | `FALL_THROUGH`
<a id="insn-00ba509c"></a> `00ba509c` | `e2 03 03 2a` | mov w2,w3 | `FALL_THROUGH`
<a id="insn-00ba50a0"></a> `00ba50a0` | `51 ed ff 97` | bl 0x00ba05e4 | `UNCONDITIONAL_CALL`
<a id="insn-00ba50a4"></a> `00ba50a4` | `7f 02 17 eb` | cmp x19,x23 | `FALL_THROUGH`
<a id="insn-00ba50a8"></a> `00ba50a8` | `c0 00 00 54` | b.eq 0x00ba50c0 | `CONDITIONAL_JUMP`
<a id="insn-00ba50ac"></a> `00ba50ac` | `e1 0a 41 a9` | ldp x1,x2,[x23, #0x10] | `FALL_THROUGH`
<a id="insn-00ba50b0"></a> `00ba50b0` | `48 00 01 cb` | sub x8,x2,x1 | `FALL_THROUGH`
<a id="insn-00ba50b4"></a> `00ba50b4` | `03 fd 43 93` | asr x3,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00ba50b8"></a> `00ba50b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00ba50bc"></a> `00ba50bc` | `2c 4e 00 94` | bl 0x00bb896c | `UNCONDITIONAL_CALL`
<a id="insn-00ba50c0"></a> `00ba50c0` | `69 22 41 a9` | ldp x9,x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ba50c4"></a> `00ba50c4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ba50c8"></a> `00ba50c8` | `00 02 00 54` | b.eq 0x00ba5108 | `CONDITIONAL_JUMP`
<a id="insn-00ba50cc"></a> `00ba50cc` | `ea 03 1f aa` | mov x10,xzr | `FALL_THROUGH`
<a id="insn-00ba50d0"></a> `00ba50d0` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-00ba50d4"></a> `00ba50d4` | `06 00 00 14` | b 0x00ba50ec | `UNCONDITIONAL_JUMP`
<a id="insn-00ba50d8"></a> `00ba50d8` | `ea 03 17 2a` | mov w10,w23 | `FALL_THROUGH`
<a id="insn-00ba50dc"></a> `00ba50dc` | `0b 01 09 cb` | sub x11,x8,x9 | `FALL_THROUGH`
<a id="insn-00ba50e0"></a> `00ba50e0` | `f7 06 00 11` | add w23,w23,#0x1 | `FALL_THROUGH`
<a id="insn-00ba50e4"></a> `00ba50e4` | `5f 0d 8b eb` | cmp x10,x11, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00ba50e8"></a> `00ba50e8` | `02 01 00 54` | b.cs 0x00ba5108 | `CONDITIONAL_JUMP`
<a id="insn-00ba50ec"></a> `00ba50ec` | `2a 79 6a f8` | ldr x10,[x9, x10, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00ba50f0"></a> `00ba50f0` | `4a ff ff b4` | cbz x10,0x00ba50d8 | `CONDITIONAL_JUMP`
<a id="insn-00ba50f4"></a> `00ba50f4` | `41 21 00 91` | add x1,x10,#0x8 | `FALL_THROUGH`
<a id="insn-00ba50f8"></a> `00ba50f8` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00ba50fc"></a> `00ba50fc` | `19 c7 00 94` | bl 0x00bd6d60 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5100"></a> `00ba5100` | `69 22 41 a9` | ldp x9,x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00ba5104"></a> `00ba5104` | `f5 ff ff 17` | b 0x00ba50d8 | `UNCONDITIONAL_JUMP`
<a id="insn-00ba5108"></a> `00ba5108` | `f6 00 18 36` | tbz w22,#0x3,0x00ba5124 | `CONDITIONAL_JUMP`
<a id="insn-00ba510c"></a> `00ba510c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5110"></a> `00ba5110` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5114"></a> `00ba5114` | `93 00 00 94` | bl 0x00ba5360 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5118"></a> `00ba5118` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba511c"></a> `00ba511c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5120"></a> `00ba5120` | `e1 00 00 94` | bl 0x00ba54a4 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5124"></a> `00ba5124` | `36 03 00 36` | tbz w22,#0x0,0x00ba5188 | `CONDITIONAL_JUMP`
<a id="insn-00ba5128"></a> `00ba5128` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba512c"></a> `00ba512c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5130"></a> `00ba5130` | `2e 01 00 94` | bl 0x00ba55e8 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5134"></a> `00ba5134` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5138"></a> `00ba5138` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba513c"></a> `00ba513c` | `7c 01 00 94` | bl 0x00ba572c | `UNCONDITIONAL_CALL`
<a id="insn-00ba5140"></a> `00ba5140` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5144"></a> `00ba5144` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5148"></a> `00ba5148` | `ca 01 00 94` | bl 0x00ba5870 | `UNCONDITIONAL_CALL`
<a id="insn-00ba514c"></a> `00ba514c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5150"></a> `00ba5150` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5154"></a> `00ba5154` | `18 02 00 94` | bl 0x00ba59b4 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5158"></a> `00ba5158` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba515c"></a> `00ba515c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5160"></a> `00ba5160` | `66 02 00 94` | bl 0x00ba5af8 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5164"></a> `00ba5164` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5168"></a> `00ba5168` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba516c"></a> `00ba516c` | `b4 02 00 94` | bl 0x00ba5c3c | `UNCONDITIONAL_CALL`
<a id="insn-00ba5170"></a> `00ba5170` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5174"></a> `00ba5174` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5178"></a> `00ba5178` | `02 03 00 94` | bl 0x00ba5d80 | `UNCONDITIONAL_CALL`
<a id="insn-00ba517c"></a> `00ba517c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5180"></a> `00ba5180` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5184"></a> `00ba5184` | `50 03 00 94` | bl 0x00ba5ec4 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5188"></a> `00ba5188` | `36 03 20 36` | tbz w22,#0x4,0x00ba51ec | `CONDITIONAL_JUMP`
<a id="insn-00ba518c"></a> `00ba518c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5190"></a> `00ba5190` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5194"></a> `00ba5194` | `9d 03 00 94` | bl 0x00ba6008 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5198"></a> `00ba5198` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba519c"></a> `00ba519c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba51a0"></a> `00ba51a0` | `eb 03 00 94` | bl 0x00ba614c | `UNCONDITIONAL_CALL`
<a id="insn-00ba51a4"></a> `00ba51a4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba51a8"></a> `00ba51a8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba51ac"></a> `00ba51ac` | `39 04 00 94` | bl 0x00ba6290 | `UNCONDITIONAL_CALL`
<a id="insn-00ba51b0"></a> `00ba51b0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba51b4"></a> `00ba51b4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba51b8"></a> `00ba51b8` | `87 04 00 94` | bl 0x00ba63d4 | `UNCONDITIONAL_CALL`
<a id="insn-00ba51bc"></a> `00ba51bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba51c0"></a> `00ba51c0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba51c4"></a> `00ba51c4` | `d5 04 00 94` | bl 0x00ba6518 | `UNCONDITIONAL_CALL`
<a id="insn-00ba51c8"></a> `00ba51c8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba51cc"></a> `00ba51cc` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba51d0"></a> `00ba51d0` | `23 05 00 94` | bl 0x00ba665c | `UNCONDITIONAL_CALL`
<a id="insn-00ba51d4"></a> `00ba51d4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba51d8"></a> `00ba51d8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba51dc"></a> `00ba51dc` | `71 05 00 94` | bl 0x00ba67a0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba51e0"></a> `00ba51e0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba51e4"></a> `00ba51e4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba51e8"></a> `00ba51e8` | `bf 05 00 94` | bl 0x00ba68e4 | `UNCONDITIONAL_CALL`
<a id="insn-00ba51ec"></a> `00ba51ec` | `76 02 08 36` | tbz w22,#0x1,0x00ba5238 | `CONDITIONAL_JUMP`
<a id="insn-00ba51f0"></a> `00ba51f0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba51f4"></a> `00ba51f4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba51f8"></a> `00ba51f8` | `0c 06 00 94` | bl 0x00ba6a28 | `UNCONDITIONAL_CALL`
<a id="insn-00ba51fc"></a> `00ba51fc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5200"></a> `00ba5200` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5204"></a> `00ba5204` | `5a 06 00 94` | bl 0x00ba6b6c | `UNCONDITIONAL_CALL`
<a id="insn-00ba5208"></a> `00ba5208` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba520c"></a> `00ba520c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5210"></a> `00ba5210` | `a8 06 00 94` | bl 0x00ba6cb0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5214"></a> `00ba5214` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5218"></a> `00ba5218` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba521c"></a> `00ba521c` | `f6 06 00 94` | bl 0x00ba6df4 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5220"></a> `00ba5220` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5224"></a> `00ba5224` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5228"></a> `00ba5228` | `44 07 00 94` | bl 0x00ba6f38 | `UNCONDITIONAL_CALL`
<a id="insn-00ba522c"></a> `00ba522c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5230"></a> `00ba5230` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5234"></a> `00ba5234` | `92 07 00 94` | bl 0x00ba707c | `UNCONDITIONAL_CALL`
<a id="insn-00ba5238"></a> `00ba5238` | `b6 01 10 36` | tbz w22,#0x2,0x00ba526c | `CONDITIONAL_JUMP`
<a id="insn-00ba523c"></a> `00ba523c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5240"></a> `00ba5240` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5244"></a> `00ba5244` | `df 07 00 94` | bl 0x00ba71c0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5248"></a> `00ba5248` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba524c"></a> `00ba524c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5250"></a> `00ba5250` | `2d 08 00 94` | bl 0x00ba7304 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5254"></a> `00ba5254` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5258"></a> `00ba5258` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba525c"></a> `00ba525c` | `7b 08 00 94` | bl 0x00ba7448 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5260"></a> `00ba5260` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5264"></a> `00ba5264` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5268"></a> `00ba5268` | `c9 08 00 94` | bl 0x00ba758c | `UNCONDITIONAL_CALL`
<a id="insn-00ba526c"></a> `00ba526c` | `f6 00 28 36` | tbz w22,#0x5,0x00ba5288 | `CONDITIONAL_JUMP`
<a id="insn-00ba5270"></a> `00ba5270` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5274"></a> `00ba5274` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5278"></a> `00ba5278` | `16 09 00 94` | bl 0x00ba76d0 | `UNCONDITIONAL_CALL`
<a id="insn-00ba527c"></a> `00ba527c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ba5280"></a> `00ba5280` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00ba5284"></a> `00ba5284` | `64 09 00 94` | bl 0x00ba7814 | `UNCONDITIONAL_CALL`
<a id="insn-00ba5288"></a> `00ba5288` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ba528c"></a> `00ba528c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ba5290"></a> `00ba5290` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00ba5294"></a> `00ba5294` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00ba5298"></a> `00ba5298` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00ba529c"></a> `00ba529c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ba4ffc`](#insn-00ba4ffc) 範囲 `[['00ba4ffc', '00ba50ab']]`
  - `CONDITIONAL_JUMP` [`00ba50a8`](#insn-00ba50a8) → [`00ba50c0`](#insn-00ba50c0)
  - `FALL_THROUGH` [`00ba50a8`](#insn-00ba50a8) → [`00ba50ac`](#insn-00ba50ac)
- ブロック [`00ba50ac`](#insn-00ba50ac) 範囲 `[['00ba50ac', '00ba50bf']]`
  - `FALL_THROUGH` [`00ba50bc`](#insn-00ba50bc) → [`00ba50c0`](#insn-00ba50c0)
- ブロック [`00ba50c0`](#insn-00ba50c0) 範囲 `[['00ba50c0', '00ba50cb']]`
  - `CONDITIONAL_JUMP` [`00ba50c8`](#insn-00ba50c8) → [`00ba5108`](#insn-00ba5108)
  - `FALL_THROUGH` [`00ba50c8`](#insn-00ba50c8) → [`00ba50cc`](#insn-00ba50cc)
- ブロック [`00ba50cc`](#insn-00ba50cc) 範囲 `[['00ba50cc', '00ba50d7']]`
  - `UNCONDITIONAL_JUMP` [`00ba50d4`](#insn-00ba50d4) → [`00ba50ec`](#insn-00ba50ec)
- ブロック [`00ba50d8`](#insn-00ba50d8) 範囲 `[['00ba50d8', '00ba50eb']]`
  - `CONDITIONAL_JUMP` [`00ba50e8`](#insn-00ba50e8) → [`00ba5108`](#insn-00ba5108)
  - `FALL_THROUGH` [`00ba50e8`](#insn-00ba50e8) → [`00ba50ec`](#insn-00ba50ec)
- ブロック [`00ba50ec`](#insn-00ba50ec) 範囲 `[['00ba50ec', '00ba50f3']]`
  - `CONDITIONAL_JUMP` [`00ba50f0`](#insn-00ba50f0) → [`00ba50d8`](#insn-00ba50d8)
  - `FALL_THROUGH` [`00ba50f0`](#insn-00ba50f0) → [`00ba50f4`](#insn-00ba50f4)
- ブロック [`00ba50f4`](#insn-00ba50f4) 範囲 `[['00ba50f4', '00ba5107']]`
  - `UNCONDITIONAL_JUMP` [`00ba5104`](#insn-00ba5104) → [`00ba50d8`](#insn-00ba50d8)
- ブロック [`00ba5108`](#insn-00ba5108) 範囲 `[['00ba5108', '00ba510b']]`
  - `CONDITIONAL_JUMP` [`00ba5108`](#insn-00ba5108) → [`00ba5124`](#insn-00ba5124)
  - `FALL_THROUGH` [`00ba5108`](#insn-00ba5108) → [`00ba510c`](#insn-00ba510c)
- ブロック [`00ba510c`](#insn-00ba510c) 範囲 `[['00ba510c', '00ba511b']]`
  - `FALL_THROUGH` [`00ba5118`](#insn-00ba5118) → [`00ba511c`](#insn-00ba511c)
- ブロック [`00ba511c`](#insn-00ba511c) 範囲 `[['00ba511c', '00ba5123']]`
  - `FALL_THROUGH` [`00ba5120`](#insn-00ba5120) → [`00ba5124`](#insn-00ba5124)
- ブロック [`00ba5124`](#insn-00ba5124) 範囲 `[['00ba5124', '00ba5127']]`
  - `CONDITIONAL_JUMP` [`00ba5124`](#insn-00ba5124) → [`00ba5188`](#insn-00ba5188)
  - `FALL_THROUGH` [`00ba5124`](#insn-00ba5124) → [`00ba5128`](#insn-00ba5128)
- ブロック [`00ba5128`](#insn-00ba5128) 範囲 `[['00ba5128', '00ba5187']]`
  - `FALL_THROUGH` [`00ba5184`](#insn-00ba5184) → [`00ba5188`](#insn-00ba5188)
- ブロック [`00ba5188`](#insn-00ba5188) 範囲 `[['00ba5188', '00ba518b']]`
  - `CONDITIONAL_JUMP` [`00ba5188`](#insn-00ba5188) → [`00ba51ec`](#insn-00ba51ec)
  - `FALL_THROUGH` [`00ba5188`](#insn-00ba5188) → [`00ba518c`](#insn-00ba518c)
- ブロック [`00ba518c`](#insn-00ba518c) 範囲 `[['00ba518c', '00ba518f']]`
  - `FALL_THROUGH` [`00ba518c`](#insn-00ba518c) → [`00ba5190`](#insn-00ba5190)
- ブロック [`00ba5190`](#insn-00ba5190) 範囲 `[['00ba5190', '00ba51df']]`
  - `FALL_THROUGH` [`00ba51dc`](#insn-00ba51dc) → [`00ba51e0`](#insn-00ba51e0)
- ブロック [`00ba51e0`](#insn-00ba51e0) 範囲 `[['00ba51e0', '00ba51eb']]`
  - `FALL_THROUGH` [`00ba51e8`](#insn-00ba51e8) → [`00ba51ec`](#insn-00ba51ec)
- ブロック [`00ba51ec`](#insn-00ba51ec) 範囲 `[['00ba51ec', '00ba51ef']]`
  - `CONDITIONAL_JUMP` [`00ba51ec`](#insn-00ba51ec) → [`00ba5238`](#insn-00ba5238)
  - `FALL_THROUGH` [`00ba51ec`](#insn-00ba51ec) → [`00ba51f0`](#insn-00ba51f0)
- ブロック [`00ba51f0`](#insn-00ba51f0) 範囲 `[['00ba51f0', '00ba5237']]`
  - `FALL_THROUGH` [`00ba5234`](#insn-00ba5234) → [`00ba5238`](#insn-00ba5238)
- ブロック [`00ba5238`](#insn-00ba5238) 範囲 `[['00ba5238', '00ba523b']]`
  - `CONDITIONAL_JUMP` [`00ba5238`](#insn-00ba5238) → [`00ba526c`](#insn-00ba526c)
  - `FALL_THROUGH` [`00ba5238`](#insn-00ba5238) → [`00ba523c`](#insn-00ba523c)
- ブロック [`00ba523c`](#insn-00ba523c) 範囲 `[['00ba523c', '00ba524b']]`
  - `FALL_THROUGH` [`00ba5248`](#insn-00ba5248) → [`00ba524c`](#insn-00ba524c)
- ブロック [`00ba524c`](#insn-00ba524c) 範囲 `[['00ba524c', '00ba526b']]`
  - `FALL_THROUGH` [`00ba5268`](#insn-00ba5268) → [`00ba526c`](#insn-00ba526c)
- ブロック [`00ba526c`](#insn-00ba526c) 範囲 `[['00ba526c', '00ba526f']]`
  - `CONDITIONAL_JUMP` [`00ba526c`](#insn-00ba526c) → [`00ba5288`](#insn-00ba5288)
  - `FALL_THROUGH` [`00ba526c`](#insn-00ba526c) → [`00ba5270`](#insn-00ba5270)
- ブロック [`00ba5270`](#insn-00ba5270) 範囲 `[['00ba5270', '00ba5287']]`
  - `FALL_THROUGH` [`00ba5284`](#insn-00ba5284) → [`00ba5288`](#insn-00ba5288)
- ブロック [`00ba5288`](#insn-00ba5288) 範囲 `[['00ba5288', '00ba529f']]`

## 命令位置別の参照

- [`00ba5000`](#insn-00ba5000) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5004`](#insn-00ba5004) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5008`](#insn-00ba5008) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba500c`](#insn-00ba500c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba502c`](#insn-00ba502c) → `00c13818`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00ba50a0`](#insn-00ba50a0) → [`00ba05e4`](../00ba0/00ba05e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba05e4` · 推定シンボル `None` · 推定型 `None`
- [`00ba50a8`](#insn-00ba50a8) → [`00ba50c0`](#insn-00ba50c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba50bc`](#insn-00ba50bc) → [`00bb896c`](../00bb8/00bb896c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bb896c` · 推定シンボル `None` · 推定型 `None`
- [`00ba50c8`](#insn-00ba50c8) → [`00ba5108`](#insn-00ba5108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba50d4`](#insn-00ba50d4) → [`00ba50ec`](#insn-00ba50ec) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba50e8`](#insn-00ba50e8) → [`00ba5108`](#insn-00ba5108) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba50f0`](#insn-00ba50f0) → [`00ba50d8`](#insn-00ba50d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba50fc`](#insn-00ba50fc) → [`00bd6d60`](../00bd6/00bd6d60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d60` · 推定シンボル `None` · 推定型 `None`
- [`00ba5104`](#insn-00ba5104) → [`00ba50d8`](#insn-00ba50d8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5108`](#insn-00ba5108) → [`00ba5124`](#insn-00ba5124) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5114`](#insn-00ba5114) → [`00ba5360`](../00ba5/00ba5360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba5360` · 推定シンボル `None` · 推定型 `None`
- [`00ba5120`](#insn-00ba5120) → [`00ba54a4`](../00ba5/00ba54a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba54a4` · 推定シンボル `None` · 推定型 `None`
- [`00ba5124`](#insn-00ba5124) → [`00ba5188`](#insn-00ba5188) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5130`](#insn-00ba5130) → [`00ba55e8`](../00ba5/00ba55e8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba55e8` · 推定シンボル `None` · 推定型 `None`
- [`00ba513c`](#insn-00ba513c) → [`00ba572c`](../00ba5/00ba572c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba572c` · 推定シンボル `None` · 推定型 `None`
- [`00ba5148`](#insn-00ba5148) → [`00ba5870`](../00ba5/00ba5870.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba5870` · 推定シンボル `None` · 推定型 `None`
- [`00ba5154`](#insn-00ba5154) → [`00ba59b4`](../00ba5/00ba59b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba59b4` · 推定シンボル `None` · 推定型 `None`
- [`00ba5160`](#insn-00ba5160) → [`00ba5af8`](../00ba5/00ba5af8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba5af8` · 推定シンボル `None` · 推定型 `None`
- [`00ba516c`](#insn-00ba516c) → [`00ba5c3c`](../00ba5/00ba5c3c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba5c3c` · 推定シンボル `None` · 推定型 `None`
- [`00ba5178`](#insn-00ba5178) → [`00ba5d80`](../00ba5/00ba5d80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba5d80` · 推定シンボル `None` · 推定型 `None`
- [`00ba5184`](#insn-00ba5184) → [`00ba5ec4`](../00ba5/00ba5ec4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba5ec4` · 推定シンボル `None` · 推定型 `None`
- [`00ba5188`](#insn-00ba5188) → [`00ba51ec`](#insn-00ba51ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5194`](#insn-00ba5194) → [`00ba6008`](../00ba6/00ba6008.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba6008` · 推定シンボル `None` · 推定型 `None`
- [`00ba51a0`](#insn-00ba51a0) → [`00ba614c`](../00ba6/00ba614c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba614c` · 推定シンボル `None` · 推定型 `None`
- [`00ba51ac`](#insn-00ba51ac) → [`00ba6290`](../00ba6/00ba6290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba6290` · 推定シンボル `None` · 推定型 `None`
- [`00ba51b8`](#insn-00ba51b8) → [`00ba63d4`](../00ba6/00ba63d4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba63d4` · 推定シンボル `None` · 推定型 `None`
- [`00ba51c4`](#insn-00ba51c4) → [`00ba6518`](../00ba6/00ba6518.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba6518` · 推定シンボル `None` · 推定型 `None`
- [`00ba51d0`](#insn-00ba51d0) → [`00ba665c`](../00ba6/00ba665c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba665c` · 推定シンボル `None` · 推定型 `None`
- [`00ba51dc`](#insn-00ba51dc) → [`00ba67a0`](../00ba6/00ba67a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba67a0` · 推定シンボル `None` · 推定型 `None`
- [`00ba51e8`](#insn-00ba51e8) → [`00ba68e4`](../00ba6/00ba68e4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba68e4` · 推定シンボル `None` · 推定型 `None`
- [`00ba51ec`](#insn-00ba51ec) → [`00ba5238`](#insn-00ba5238) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba51f8`](#insn-00ba51f8) → [`00ba6a28`](../00ba6/00ba6a28.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba6a28` · 推定シンボル `None` · 推定型 `None`
- [`00ba5204`](#insn-00ba5204) → [`00ba6b6c`](../00ba6/00ba6b6c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba6b6c` · 推定シンボル `None` · 推定型 `None`
- [`00ba5210`](#insn-00ba5210) → [`00ba6cb0`](../00ba6/00ba6cb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba6cb0` · 推定シンボル `None` · 推定型 `None`
- [`00ba521c`](#insn-00ba521c) → [`00ba6df4`](../00ba6/00ba6df4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba6df4` · 推定シンボル `None` · 推定型 `None`
- [`00ba5228`](#insn-00ba5228) → [`00ba6f38`](../00ba6/00ba6f38.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba6f38` · 推定シンボル `None` · 推定型 `None`
- [`00ba5234`](#insn-00ba5234) → [`00ba707c`](../00ba7/00ba707c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba707c` · 推定シンボル `None` · 推定型 `None`
- [`00ba5238`](#insn-00ba5238) → [`00ba526c`](#insn-00ba526c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5244`](#insn-00ba5244) → [`00ba71c0`](../00ba7/00ba71c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba71c0` · 推定シンボル `None` · 推定型 `None`
- [`00ba5250`](#insn-00ba5250) → [`00ba7304`](../00ba7/00ba7304.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba7304` · 推定シンボル `None` · 推定型 `None`
- [`00ba525c`](#insn-00ba525c) → [`00ba7448`](../00ba7/00ba7448.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba7448` · 推定シンボル `None` · 推定型 `None`
- [`00ba5268`](#insn-00ba5268) → [`00ba758c`](../00ba7/00ba758c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba758c` · 推定シンボル `None` · 推定型 `None`
- [`00ba526c`](#insn-00ba526c) → [`00ba5288`](#insn-00ba5288) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5278`](#insn-00ba5278) → [`00ba76d0`](../00ba7/00ba76d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba76d0` · 推定シンボル `None` · 推定型 `None`
- [`00ba5284`](#insn-00ba5284) → [`00ba7814`](../00ba7/00ba7814.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00ba7814` · 推定シンボル `None` · 推定型 `None`
- [`00ba5288`](#insn-00ba5288) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba528c`](#insn-00ba528c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5290`](#insn-00ba5290) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ba5294`](#insn-00ba5294) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ba5000`](#insn-00ba5000)

~~~json
{
  "source": "00ba5000",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5004`](#insn-00ba5004)

~~~json
{
  "source": "00ba5004",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5008`](#insn-00ba5008)

~~~json
{
  "source": "00ba5008",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba500c`](#insn-00ba500c)

~~~json
{
  "source": "00ba500c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba502c`](#insn-00ba502c)

~~~json
{
  "source": "00ba502c",
  "target": "00c13818",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c13818",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00ba50a0`](#insn-00ba50a0)

~~~json
{
  "source": "00ba50a0",
  "target": "00ba05e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba50a8`](#insn-00ba50a8)

~~~json
{
  "source": "00ba50a8",
  "target": "00ba50c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba50bc`](#insn-00ba50bc)

~~~json
{
  "source": "00ba50bc",
  "target": "00bb896c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba50c8`](#insn-00ba50c8)

~~~json
{
  "source": "00ba50c8",
  "target": "00ba5108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba50d4`](#insn-00ba50d4)

~~~json
{
  "source": "00ba50d4",
  "target": "00ba50ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba50e8`](#insn-00ba50e8)

~~~json
{
  "source": "00ba50e8",
  "target": "00ba5108",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba50f0`](#insn-00ba50f0)

~~~json
{
  "source": "00ba50f0",
  "target": "00ba50d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba50fc`](#insn-00ba50fc)

~~~json
{
  "source": "00ba50fc",
  "target": "00bd6d60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5104`](#insn-00ba5104)

~~~json
{
  "source": "00ba5104",
  "target": "00ba50d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5108`](#insn-00ba5108)

~~~json
{
  "source": "00ba5108",
  "target": "00ba5124",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5114`](#insn-00ba5114)

~~~json
{
  "source": "00ba5114",
  "target": "00ba5360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5120`](#insn-00ba5120)

~~~json
{
  "source": "00ba5120",
  "target": "00ba54a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5124`](#insn-00ba5124)

~~~json
{
  "source": "00ba5124",
  "target": "00ba5188",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5130`](#insn-00ba5130)

~~~json
{
  "source": "00ba5130",
  "target": "00ba55e8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba513c`](#insn-00ba513c)

~~~json
{
  "source": "00ba513c",
  "target": "00ba572c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5148`](#insn-00ba5148)

~~~json
{
  "source": "00ba5148",
  "target": "00ba5870",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5154`](#insn-00ba5154)

~~~json
{
  "source": "00ba5154",
  "target": "00ba59b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5160`](#insn-00ba5160)

~~~json
{
  "source": "00ba5160",
  "target": "00ba5af8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba516c`](#insn-00ba516c)

~~~json
{
  "source": "00ba516c",
  "target": "00ba5c3c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5178`](#insn-00ba5178)

~~~json
{
  "source": "00ba5178",
  "target": "00ba5d80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5184`](#insn-00ba5184)

~~~json
{
  "source": "00ba5184",
  "target": "00ba5ec4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5188`](#insn-00ba5188)

~~~json
{
  "source": "00ba5188",
  "target": "00ba51ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5194`](#insn-00ba5194)

~~~json
{
  "source": "00ba5194",
  "target": "00ba6008",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba51a0`](#insn-00ba51a0)

~~~json
{
  "source": "00ba51a0",
  "target": "00ba614c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba51ac`](#insn-00ba51ac)

~~~json
{
  "source": "00ba51ac",
  "target": "00ba6290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba51b8`](#insn-00ba51b8)

~~~json
{
  "source": "00ba51b8",
  "target": "00ba63d4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba51c4`](#insn-00ba51c4)

~~~json
{
  "source": "00ba51c4",
  "target": "00ba6518",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba51d0`](#insn-00ba51d0)

~~~json
{
  "source": "00ba51d0",
  "target": "00ba665c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba51dc`](#insn-00ba51dc)

~~~json
{
  "source": "00ba51dc",
  "target": "00ba67a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba51e8`](#insn-00ba51e8)

~~~json
{
  "source": "00ba51e8",
  "target": "00ba68e4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba51ec`](#insn-00ba51ec)

~~~json
{
  "source": "00ba51ec",
  "target": "00ba5238",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba51f8`](#insn-00ba51f8)

~~~json
{
  "source": "00ba51f8",
  "target": "00ba6a28",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5204`](#insn-00ba5204)

~~~json
{
  "source": "00ba5204",
  "target": "00ba6b6c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5210`](#insn-00ba5210)

~~~json
{
  "source": "00ba5210",
  "target": "00ba6cb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba521c`](#insn-00ba521c)

~~~json
{
  "source": "00ba521c",
  "target": "00ba6df4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5228`](#insn-00ba5228)

~~~json
{
  "source": "00ba5228",
  "target": "00ba6f38",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5234`](#insn-00ba5234)

~~~json
{
  "source": "00ba5234",
  "target": "00ba707c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5238`](#insn-00ba5238)

~~~json
{
  "source": "00ba5238",
  "target": "00ba526c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5244`](#insn-00ba5244)

~~~json
{
  "source": "00ba5244",
  "target": "00ba71c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5250`](#insn-00ba5250)

~~~json
{
  "source": "00ba5250",
  "target": "00ba7304",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba525c`](#insn-00ba525c)

~~~json
{
  "source": "00ba525c",
  "target": "00ba7448",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5268`](#insn-00ba5268)

~~~json
{
  "source": "00ba5268",
  "target": "00ba758c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba526c`](#insn-00ba526c)

~~~json
{
  "source": "00ba526c",
  "target": "00ba5288",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5278`](#insn-00ba5278)

~~~json
{
  "source": "00ba5278",
  "target": "00ba76d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5284`](#insn-00ba5284)

~~~json
{
  "source": "00ba5284",
  "target": "00ba7814",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ba5288`](#insn-00ba5288)

~~~json
{
  "source": "00ba5288",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba528c`](#insn-00ba528c)

~~~json
{
  "source": "00ba528c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5290`](#insn-00ba5290)

~~~json
{
  "source": "00ba5290",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ba5294`](#insn-00ba5294)

~~~json
{
  "source": "00ba5294",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
