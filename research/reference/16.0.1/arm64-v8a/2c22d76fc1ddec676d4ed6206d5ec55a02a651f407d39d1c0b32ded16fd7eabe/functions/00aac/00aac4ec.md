# 00aac4ec

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00aac2f0`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00aac/00aac2f0.md) · 移動量 `+0x1fc`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0063.md#compare-321374f5a75bf4f5f484d611bc6ea561)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aac55c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aac/00aac55c.md) · 移動量 `+0x70`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0064.md#compare-b5ed92172e2cad1e1ccfc35b602ce99b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aac4ec",
  "name": "FUN_00aac4ec",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "44d00785c6fbc857ebc5c8428b846c2c3e7c271d1df45c4b52a20febedc6372e",
  "source_text_sha256": "44d00785c6fbc857ebc5c8428b846c2c3e7c271d1df45c4b52a20febedc6372e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aac4ec",
        "00aac6d7"
      ],
      [
        "00aac768",
        "00aac76b"
      ]
    ],
    "bytes_sha256": "4b972ffef2ad55829cd49d70f0d1dfe95af9376ecd1f4856d9e163e28c87f6cf",
    "instruction_count": 124,
    "instruction_bytes": 496,
    "body_bytes": 496,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aa3e24](../00aa3/00aa3e24.md)

## 呼び出し先

- [008514f8](../00851/008514f8.md)
- [0087929c](../00879/0087929c.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5a830](../00c5a/00c5a830.md)
- [00c5a840](../00c5a/00c5a840.md)

## 関連文字列（未確認候補）

~~~text
"BcResitemShop"
"Sale"
"itemID"
"sec1_id"
"sec1_type"
"sec2_id"
"sec2_type"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2186 bytes

~~~c

void FUN_00aac4ec(int param_1,ulong param_2)

{
  long lVar1;
  long lVar2;
  undefined4 local_e0 [2];
  char *local_d8;
  char *local_c8;
  undefined4 local_c0 [2];
  undefined8 local_b8;
  char *local_a8;
  undefined4 local_a0 [2];
  undefined8 local_98;
  char *local_88;
  undefined4 local_80 [2];
  undefined8 local_78;
  char *local_68;
  undefined4 local_60 [2];
  undefined8 local_58;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  local_c8 = "sec1_type";
  local_c0[0] = 0;
  local_b8 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
  local_d8 = "itemID";
  _ZN8firebase7VariantaSEOS0_(local_c0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_a0[0] = 0;
  local_a8 = "sec1_id";
  local_98 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,1);
  local_d8 = (char *)(long)param_1;
                    /* try { // try from 00aac598 to 00bac61f has its CatchHandler @ 00aac704 */
  _ZN8firebase7VariantaSEOS0_(local_a0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_80[0] = 0;
  local_88 = "sec2_type";
  local_78 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
  local_d8 = "Sale";
  _ZN8firebase7VariantaSEOS0_(local_80,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_60[0] = 0;
  local_68 = "sec2_id";
                    /* try { // try from 00aac620 to 00bac7d3 has its CatchHandler @ 00aac444 */
  local_58 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,1);
  local_d8 = (char *)(param_2 & 1);
  _ZN8firebase7VariantaSEOS0_(local_60,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  lVar2 = FUN_008514f8();
  FUN_0087929c(*(undefined8 *)(lVar2 + 0x22b0),"BcResitemShop",&local_c8,4);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_60,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_80,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_a0,0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_c0,0);
  if (*(long *)(lVar1 + 0x28) == local_48) {
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
<a id="insn-00aac4ec"></a> `00aac4ec` | `ff 83 03 d1` | sub sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00aac4f0"></a> `00aac4f0` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aac4f4"></a> `00aac4f4` | `f7 5b 00 f9` | str x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aac4f8"></a> `00aac4f8` | `f6 57 0c a9` | stp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aac4fc"></a> `00aac4fc` | `f4 4f 0d a9` | stp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aac500"></a> `00aac500` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00aac504"></a> `00aac504` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aac508"></a> `00aac508` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00aac50c"></a> `00aac50c` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aac510"></a> `00aac510` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aac514"></a> `00aac514` | `f4 63 00 91` | add x20,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aac518"></a> `00aac518` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aac51c"></a> `00aac51c` | `08 c0 ff d0` | adrp x8,0x2ae000 | `FALL_THROUGH`
<a id="insn-00aac520"></a> `00aac520` | `08 d1 2b 91` | add x8,x8,#0xaf4 | `FALL_THROUGH`
<a id="insn-00aac524"></a> `00aac524` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aac528"></a> `00aac528` | `ff 23 00 b9` | str wzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aac52c"></a> `00aac52c` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aac530"></a> `00aac530` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aac534"></a> `00aac534` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aac538"></a> `00aac538` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aac53c"></a> `00aac53c` | `bd b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac540"></a> `00aac540` | `28 c0 ff f0` | adrp x8,0x2b3000 | `FALL_THROUGH`
<a id="insn-00aac544"></a> `00aac544` | `08 89 0d 91` | add x8,x8,#0x362 | `FALL_THROUGH`
<a id="insn-00aac548"></a> `00aac548` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aac54c"></a> `00aac54c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aac550"></a> `00aac550` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aac554"></a> `00aac554` | `bb b8 06 94` | bl 0x00c5a840 | `UNCONDITIONAL_CALL`
<a id="insn-00aac558"></a> `00aac558` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aac55c"></a> `00aac55c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aac560"></a> `00aac560` | `b4 b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac564"></a> `00aac564` | `28 c0 ff b0` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00aac568"></a> `00aac568` | `08 21 39 91` | add x8,x8,#0xe48 | `FALL_THROUGH`
<a id="insn-00aac56c"></a> `00aac56c` | `ff 43 00 b9` | str wzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aac570"></a> `00aac570` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aac574"></a> `00aac574` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aac578"></a> `00aac578` | `15 81 00 91` | add x21,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aac57c"></a> `00aac57c` | `14 a1 00 91` | add x20,x8,#0x28 | `FALL_THROUGH`
<a id="insn-00aac580"></a> `00aac580` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aac584"></a> `00aac584` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aac588"></a> `00aac588` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aac58c"></a> `00aac58c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aac590"></a> `00aac590` | `a8 b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac594"></a> `00aac594` | `c8 7e 40 93` | sxtw x8,w22 | `FALL_THROUGH`
<a id="insn-00aac598"></a> `00aac598` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aac59c"></a> `00aac59c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aac5a0"></a> `00aac5a0` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aac5a4"></a> `00aac5a4` | `a7 b8 06 94` | bl 0x00c5a840 | `UNCONDITIONAL_CALL`
<a id="insn-00aac5a8"></a> `00aac5a8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aac5ac"></a> `00aac5ac` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aac5b0"></a> `00aac5b0` | `a0 b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac5b4"></a> `00aac5b4` | `c8 bf ff f0` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aac5b8"></a> `00aac5b8` | `08 e9 2a 91` | add x8,x8,#0xaba | `FALL_THROUGH`
<a id="insn-00aac5bc"></a> `00aac5bc` | `ff 63 00 b9` | str wzr,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aac5c0"></a> `00aac5c0` | `e8 2f 00 f9` | str x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00aac5c4"></a> `00aac5c4` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aac5c8"></a> `00aac5c8` | `15 01 01 91` | add x21,x8,#0x40 | `FALL_THROUGH`
<a id="insn-00aac5cc"></a> `00aac5cc` | `14 21 01 91` | add x20,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00aac5d0"></a> `00aac5d0` | `ff 37 00 f9` | str xzr,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aac5d4"></a> `00aac5d4` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aac5d8"></a> `00aac5d8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aac5dc"></a> `00aac5dc` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aac5e0"></a> `00aac5e0` | `94 b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac5e4"></a> `00aac5e4` | `68 c0 ff f0` | adrp x8,0x2bb000 | `FALL_THROUGH`
<a id="insn-00aac5e8"></a> `00aac5e8` | `08 cd 33 91` | add x8,x8,#0xcf3 | `FALL_THROUGH`
<a id="insn-00aac5ec"></a> `00aac5ec` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aac5f0"></a> `00aac5f0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aac5f4"></a> `00aac5f4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aac5f8"></a> `00aac5f8` | `92 b8 06 94` | bl 0x00c5a840 | `UNCONDITIONAL_CALL`
<a id="insn-00aac5fc"></a> `00aac5fc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aac600"></a> `00aac600` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aac604"></a> `00aac604` | `8b b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac608"></a> `00aac608` | `08 c0 ff f0` | adrp x8,0x2af000 | `FALL_THROUGH`
<a id="insn-00aac60c"></a> `00aac60c` | `08 ad 30 91` | add x8,x8,#0xc2b | `FALL_THROUGH`
<a id="insn-00aac610"></a> `00aac610` | `ff 83 00 b9` | str wzr,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aac614"></a> `00aac614` | `e8 3f 00 f9` | str x8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00aac618"></a> `00aac618` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aac61c"></a> `00aac61c` | `15 81 01 91` | add x21,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00aac620"></a> `00aac620` | `14 a1 01 91` | add x20,x8,#0x68 | `FALL_THROUGH`
<a id="insn-00aac624"></a> `00aac624` | `ff 47 00 f9` | str xzr,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aac628"></a> `00aac628` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aac62c"></a> `00aac62c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aac630"></a> `00aac630` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aac634"></a> `00aac634` | `7f b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac638"></a> `00aac638` | `68 02 40 92` | and x8,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00aac63c"></a> `00aac63c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aac640"></a> `00aac640` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aac644"></a> `00aac644` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aac648"></a> `00aac648` | `7e b8 06 94` | bl 0x00c5a840 | `UNCONDITIONAL_CALL`
<a id="insn-00aac64c"></a> `00aac64c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aac650"></a> `00aac650` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aac654"></a> `00aac654` | `77 b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac658"></a> `00aac658` | `a8 93 f6 97` | bl 0x008514f8 | `UNCONDITIONAL_CALL`
<a id="insn-00aac65c"></a> `00aac65c` | `00 58 51 f9` | ldr x0,[x0, #0x22b0] | `FALL_THROUGH`
<a id="insn-00aac660"></a> `00aac660` | `41 c0 ff 90` | adrp x1,0x2b4000 | `FALL_THROUGH`
<a id="insn-00aac664"></a> `00aac664` | `21 50 14 91` | add x1,x1,#0x514 | `FALL_THROUGH`
<a id="insn-00aac668"></a> `00aac668` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aac66c"></a> `00aac66c` | `83 00 80 52` | mov w3,#0x4 | `FALL_THROUGH`
<a id="insn-00aac670"></a> `00aac670` | `f3 63 00 91` | add x19,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aac674"></a> `00aac674` | `0a 33 f7 97` | bl 0x0087929c | `UNCONDITIONAL_CALL`
<a id="insn-00aac678"></a> `00aac678` | `60 a2 01 91` | add x0,x19,#0x68 | `FALL_THROUGH`
<a id="insn-00aac67c"></a> `00aac67c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aac680"></a> `00aac680` | `6c b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac684"></a> `00aac684` | `f3 63 00 91` | add x19,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aac688"></a> `00aac688` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00aac68c"></a> `00aac68c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aac690"></a> `00aac690` | `68 b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac694"></a> `00aac694` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00aac698"></a> `00aac698` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aac69c"></a> `00aac69c` | `65 b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac6a0"></a> `00aac6a0` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aac6a4"></a> `00aac6a4` | `00 21 00 91` | add x0,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00aac6a8"></a> `00aac6a8` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aac6ac"></a> `00aac6ac` | `61 b8 06 94` | bl 0x00c5a830 | `UNCONDITIONAL_CALL`
<a id="insn-00aac6b0"></a> `00aac6b0` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aac6b4"></a> `00aac6b4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aac6b8"></a> `00aac6b8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aac6bc"></a> `00aac6bc` | `61 05 00 54` | b.ne 0x00aac768 | `CONDITIONAL_JUMP`
<a id="insn-00aac6c0"></a> `00aac6c0` | `f4 4f 4d a9` | ldp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aac6c4"></a> `00aac6c4` | `f7 5b 40 f9` | ldr x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aac6c8"></a> `00aac6c8` | `f6 57 4c a9` | ldp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aac6cc"></a> `00aac6cc` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aac6d0"></a> `00aac6d0` | `ff 83 03 91` | add sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00aac6d4"></a> `00aac6d4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aac768"></a> `00aac768` | `de ad 06 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aac4ec`](#insn-00aac4ec) 範囲 `[['00aac4ec', '00aac597']]`
  - `FALL_THROUGH` [`00aac594`](#insn-00aac594) → [`00aac598`](#insn-00aac598)
- ブロック [`00aac598`](#insn-00aac598) 範囲 `[['00aac598', '00aac61f']]`
  - `FALL_THROUGH` [`00aac61c`](#insn-00aac61c) → [`00aac620`](#insn-00aac620)
- ブロック [`00aac620`](#insn-00aac620) 範囲 `[['00aac620', '00aac6bf']]`
  - `CONDITIONAL_JUMP` [`00aac6bc`](#insn-00aac6bc) → [`00aac768`](#insn-00aac768)
  - `FALL_THROUGH` [`00aac6bc`](#insn-00aac6bc) → [`00aac6c0`](#insn-00aac6c0)
- ブロック [`00aac6c0`](#insn-00aac6c0) 範囲 `[['00aac6c0', '00aac6d7']]`
- ブロック [`00aac768`](#insn-00aac768) 範囲 `[['00aac768', '00aac76b']]`

## 命令位置別の参照

- [`00aac4f0`](#insn-00aac4f0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac4f4`](#insn-00aac4f4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac4f8`](#insn-00aac4f8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac4fc`](#insn-00aac4fc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac518`](#insn-00aac518) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac524`](#insn-00aac524) → `002aeaf4`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aac524`](#insn-00aac524) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac528`](#insn-00aac528) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac52c`](#insn-00aac52c) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac530`](#insn-00aac530) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac53c`](#insn-00aac53c) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac550`](#insn-00aac550) → `002b3362`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aac550`](#insn-00aac550) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac554`](#insn-00aac554) → [`00c5a840`](../00c5a/00c5a840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a840` · 推定シンボル `None` · 推定型 `None`
- [`00aac560`](#insn-00aac560) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac56c`](#insn-00aac56c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac570`](#insn-00aac570) → `002b1e48`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aac570`](#insn-00aac570) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac580`](#insn-00aac580) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac584`](#insn-00aac584) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac590`](#insn-00aac590) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac5a0`](#insn-00aac5a0) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac5a4`](#insn-00aac5a4) → [`00c5a840`](../00c5a/00c5a840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a840` · 推定シンボル `None` · 推定型 `None`
- [`00aac5b0`](#insn-00aac5b0) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac5bc`](#insn-00aac5bc) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac5c0`](#insn-00aac5c0) → `002a7aba`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aac5c0`](#insn-00aac5c0) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac5d0`](#insn-00aac5d0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac5d4`](#insn-00aac5d4) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac5e0`](#insn-00aac5e0) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac5f4`](#insn-00aac5f4) → `002bbcf3`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac5f4`](#insn-00aac5f4) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac5f8`](#insn-00aac5f8) → [`00c5a840`](../00c5a/00c5a840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a840` · 推定シンボル `None` · 推定型 `None`
- [`00aac604`](#insn-00aac604) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac610`](#insn-00aac610) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac614`](#insn-00aac614) → `002afc2b`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aac614`](#insn-00aac614) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac624`](#insn-00aac624) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac628`](#insn-00aac628) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac634`](#insn-00aac634) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac644`](#insn-00aac644) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac648`](#insn-00aac648) → [`00c5a840`](../00c5a/00c5a840.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a840` · 推定シンボル `None` · 推定型 `None`
- [`00aac654`](#insn-00aac654) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac658`](#insn-00aac658) → [`008514f8`](../00851/008514f8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008514f8` · 推定シンボル `None` · 推定型 `None`
- [`00aac664`](#insn-00aac664) → `002b4514`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aac674`](#insn-00aac674) → [`0087929c`](../00879/0087929c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0087929c` · 推定シンボル `None` · 推定型 `None`
- [`00aac680`](#insn-00aac680) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac690`](#insn-00aac690) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac69c`](#insn-00aac69c) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac6ac`](#insn-00aac6ac) → [`00c5a830`](../00c5a/00c5a830.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a830` · 推定シンボル `None` · 推定型 `None`
- [`00aac6b4`](#insn-00aac6b4) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac6bc`](#insn-00aac6bc) → [`00aac768`](#insn-00aac768) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac6c0`](#insn-00aac6c0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac6c4`](#insn-00aac6c4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac6c8`](#insn-00aac6c8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac6cc`](#insn-00aac6cc) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aac768`](#insn-00aac768) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aac4f0`](#insn-00aac4f0)

~~~json
{
  "source": "00aac4f0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac4f4`](#insn-00aac4f4)

~~~json
{
  "source": "00aac4f4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac4f8`](#insn-00aac4f8)

~~~json
{
  "source": "00aac4f8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac4fc`](#insn-00aac4fc)

~~~json
{
  "source": "00aac4fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac518`](#insn-00aac518)

~~~json
{
  "source": "00aac518",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac524`](#insn-00aac524)

~~~json
{
  "source": "00aac524",
  "target": "002aeaf4",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aeaf4",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563315f7479706500",
  "capture_start": "002aeaf4",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aac524`](#insn-00aac524)

~~~json
{
  "source": "00aac524",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac528`](#insn-00aac528)

~~~json
{
  "source": "00aac528",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac52c`](#insn-00aac52c)

~~~json
{
  "source": "00aac52c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac530`](#insn-00aac530)

~~~json
{
  "source": "00aac530",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac53c`](#insn-00aac53c)

~~~json
{
  "source": "00aac53c",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac550`](#insn-00aac550)

~~~json
{
  "source": "00aac550",
  "target": "002b3362",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b3362",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "6974656d494400",
  "capture_start": "002b3362",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aac550`](#insn-00aac550)

~~~json
{
  "source": "00aac550",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac554`](#insn-00aac554)

~~~json
{
  "source": "00aac554",
  "target": "00c5a840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac560`](#insn-00aac560)

~~~json
{
  "source": "00aac560",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac56c`](#insn-00aac56c)

~~~json
{
  "source": "00aac56c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac570`](#insn-00aac570)

~~~json
{
  "source": "00aac570",
  "target": "002b1e48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1e48",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563315f696400",
  "capture_start": "002b1e48",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aac570`](#insn-00aac570)

~~~json
{
  "source": "00aac570",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac580`](#insn-00aac580)

~~~json
{
  "source": "00aac580",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac584`](#insn-00aac584)

~~~json
{
  "source": "00aac584",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac590`](#insn-00aac590)

~~~json
{
  "source": "00aac590",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac5a0`](#insn-00aac5a0)

~~~json
{
  "source": "00aac5a0",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac5a4`](#insn-00aac5a4)

~~~json
{
  "source": "00aac5a4",
  "target": "00c5a840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac5b0`](#insn-00aac5b0)

~~~json
{
  "source": "00aac5b0",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac5bc`](#insn-00aac5bc)

~~~json
{
  "source": "00aac5bc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac5c0`](#insn-00aac5c0)

~~~json
{
  "source": "00aac5c0",
  "target": "002a7aba",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7aba",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563325f7479706500",
  "capture_start": "002a7aba",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aac5c0`](#insn-00aac5c0)

~~~json
{
  "source": "00aac5c0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac5d0`](#insn-00aac5d0)

~~~json
{
  "source": "00aac5d0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac5d4`](#insn-00aac5d4)

~~~json
{
  "source": "00aac5d4",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac5e0`](#insn-00aac5e0)

~~~json
{
  "source": "00aac5e0",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac5f4`](#insn-00aac5f4)

~~~json
{
  "source": "00aac5f4",
  "target": "002bbcf3",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac5f4`](#insn-00aac5f4)

~~~json
{
  "source": "00aac5f4",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac5f8`](#insn-00aac5f8)

~~~json
{
  "source": "00aac5f8",
  "target": "00c5a840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac604`](#insn-00aac604)

~~~json
{
  "source": "00aac604",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac610`](#insn-00aac610)

~~~json
{
  "source": "00aac610",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac614`](#insn-00aac614)

~~~json
{
  "source": "00aac614",
  "target": "002afc2b",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002afc2b",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563325f696400",
  "capture_start": "002afc2b",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aac614`](#insn-00aac614)

~~~json
{
  "source": "00aac614",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac624`](#insn-00aac624)

~~~json
{
  "source": "00aac624",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac628`](#insn-00aac628)

~~~json
{
  "source": "00aac628",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac634`](#insn-00aac634)

~~~json
{
  "source": "00aac634",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac644`](#insn-00aac644)

~~~json
{
  "source": "00aac644",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac648`](#insn-00aac648)

~~~json
{
  "source": "00aac648",
  "target": "00c5a840",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac654`](#insn-00aac654)

~~~json
{
  "source": "00aac654",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac658`](#insn-00aac658)

~~~json
{
  "source": "00aac658",
  "target": "008514f8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac664`](#insn-00aac664)

~~~json
{
  "source": "00aac664",
  "target": "002b4514",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b4514",
  "offset": 0,
  "size": 14,
  "datatype": "string",
  "bytes": "42635265736974656d53686f7000",
  "capture_start": "002b4514",
  "capture_bytes": 14,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aac674`](#insn-00aac674)

~~~json
{
  "source": "00aac674",
  "target": "0087929c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac680`](#insn-00aac680)

~~~json
{
  "source": "00aac680",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac690`](#insn-00aac690)

~~~json
{
  "source": "00aac690",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac69c`](#insn-00aac69c)

~~~json
{
  "source": "00aac69c",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac6ac`](#insn-00aac6ac)

~~~json
{
  "source": "00aac6ac",
  "target": "00c5a830",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aac6b4`](#insn-00aac6b4)

~~~json
{
  "source": "00aac6b4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac6bc`](#insn-00aac6bc)

~~~json
{
  "source": "00aac6bc",
  "target": "00aac768",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac6c0`](#insn-00aac6c0)

~~~json
{
  "source": "00aac6c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac6c4`](#insn-00aac6c4)

~~~json
{
  "source": "00aac6c4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac6c8`](#insn-00aac6c8)

~~~json
{
  "source": "00aac6c8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac6cc`](#insn-00aac6cc)

~~~json
{
  "source": "00aac6cc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aac768`](#insn-00aac768)

~~~json
{
  "source": "00aac768",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
