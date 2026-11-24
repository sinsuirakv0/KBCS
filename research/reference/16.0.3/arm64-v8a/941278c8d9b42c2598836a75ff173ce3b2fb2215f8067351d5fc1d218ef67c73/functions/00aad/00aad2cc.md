# 00aad2cc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00aac2d8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00aac/00aac2d8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0065.md#compare-9a69bb1d82bb32e4613eee014279e780)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00aad2cc",
  "name": "FUN_00aad2cc",
  "size": 496,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "988a4494a452b591acbff2f957c37f4372a0676be638e9a0d58c2f0c4992a537",
  "source_text_sha256": "988a4494a452b591acbff2f957c37f4372a0676be638e9a0d58c2f0c4992a537",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00aad2cc",
        "00aad4b7"
      ],
      [
        "00aad548",
        "00aad54b"
      ]
    ],
    "bytes_sha256": "c7c12b1d7e33e82dc8de9b0907a5da09f94b6cb48a0a2ea2771c50346b2605ba",
    "instruction_count": 124,
    "instruction_bytes": 496,
    "body_bytes": 496,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00aa4e88](../00aa4/00aa4e88.md)

## 呼び出し先

- [008524fc](../00852/008524fc.md)
- [0087a2a0](../0087a/0087a2a0.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5b8d0](../00c5b/00c5b8d0.md)
- [00c5b8e0](../00c5b/00c5b8e0.md)

## 関連文字列（未確認候補）

~~~text
"BcResSlot"
"Sale"
"SlotID"
"sec1_id"
"sec1_type"
"sec2_id"
"sec2_type"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2718 bytes

~~~c

void FUN_00aad2cc(int param_1,ulong param_2)

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
                    /* try { // try from 00aad318 to 00bad31b has its CatchHandler @ 00aad3c4 */
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
  local_d8 = "SlotID";
  _ZN8firebase7VariantaSEOS0_(local_c0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_a0[0] = 0;
  local_a8 = "sec1_id";
                    /* try { // try from 00aad358 to 00bad35f has its CatchHandler @ 00aad3cc */
  local_98 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,1);
  local_d8 = (char *)(long)param_1;
  _ZN8firebase7VariantaSEOS0_(local_a0,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_80[0] = 0;
  local_88 = "sec2_type";
  local_78 = 0;
  local_e0[0] = 0;
                    /* try { // try from 00aad3bc to 00bad3c3 has its CatchHandler @ 00aad3c4 */
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,4);
                    /* catch() { ... } // from try @ 00aad318 with catch @ 00aad3c4
                       catch() { ... } // from try @ 00aad3bc with catch @ 00aad3c4
                       try { // try from 00aad3c4 to 00bad3ff has its CatchHandler @ 00aad2b8 */
                    /* catch() { ... } // from try @ 00aad358 with catch @ 00aad3cc */
  local_d8 = "Sale";
  _ZN8firebase7VariantaSEOS0_(local_80,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  local_60[0] = 0;
  local_68 = "sec2_id";
  local_58 = 0;
  local_e0[0] = 0;
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,1);
  local_d8 = (char *)(param_2 & 1);
  _ZN8firebase7VariantaSEOS0_(local_60,local_e0);
  _ZN8firebase7Variant5ClearENS0_4TypeE(local_e0,0);
  lVar2 = FUN_008524fc();
                    /* catch() { ... } // from try @ 00aad620 with catch @ 00aad444 */
  FUN_0087a2a0(*(undefined8 *)(lVar2 + 0x22b0),"BcResSlot",&local_c8,4);
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
<a id="insn-00aad2cc"></a> `00aad2cc` | `ff 83 03 d1` | sub sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad2d0"></a> `00aad2d0` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aad2d4"></a> `00aad2d4` | `f7 5b 00 f9` | str x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aad2d8"></a> `00aad2d8` | `f6 57 0c a9` | stp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aad2dc"></a> `00aad2dc` | `f4 4f 0d a9` | stp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aad2e0"></a> `00aad2e0` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00aad2e4"></a> `00aad2e4` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00aad2e8"></a> `00aad2e8` | `f3 03 01 2a` | mov w19,w1 | `FALL_THROUGH`
<a id="insn-00aad2ec"></a> `00aad2ec` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00aad2f0"></a> `00aad2f0` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aad2f4"></a> `00aad2f4` | `f4 63 00 91` | add x20,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aad2f8"></a> `00aad2f8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aad2fc"></a> `00aad2fc` | `08 c0 ff b0` | adrp x8,0x2ae000 | `FALL_THROUGH`
<a id="insn-00aad300"></a> `00aad300` | `08 bd 2d 91` | add x8,x8,#0xb6f | `FALL_THROUGH`
<a id="insn-00aad304"></a> `00aad304` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00aad308"></a> `00aad308` | `ff 23 00 b9` | str wzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00aad30c"></a> `00aad30c` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00aad310"></a> `00aad310` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aad314"></a> `00aad314` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aad318"></a> `00aad318` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aad31c"></a> `00aad31c` | `6d b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad320"></a> `00aad320` | `68 c0 ff 90` | adrp x8,0x2b9000 | `FALL_THROUGH`
<a id="insn-00aad324"></a> `00aad324` | `08 39 23 91` | add x8,x8,#0x8ce | `FALL_THROUGH`
<a id="insn-00aad328"></a> `00aad328` | `80 22 00 91` | add x0,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00aad32c"></a> `00aad32c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aad330"></a> `00aad330` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aad334"></a> `00aad334` | `6b b9 06 94` | bl 0x00c5b8e0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad338"></a> `00aad338` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aad33c"></a> `00aad33c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad340"></a> `00aad340` | `64 b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad344"></a> `00aad344` | `28 c0 ff 90` | adrp x8,0x2b1000 | `FALL_THROUGH`
<a id="insn-00aad348"></a> `00aad348` | `08 0d 3b 91` | add x8,x8,#0xec3 | `FALL_THROUGH`
<a id="insn-00aad34c"></a> `00aad34c` | `ff 43 00 b9` | str wzr,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00aad350"></a> `00aad350` | `e8 1f 00 f9` | str x8,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00aad354"></a> `00aad354` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aad358"></a> `00aad358` | `15 81 00 91` | add x21,x8,#0x20 | `FALL_THROUGH`
<a id="insn-00aad35c"></a> `00aad35c` | `14 a1 00 91` | add x20,x8,#0x28 | `FALL_THROUGH`
<a id="insn-00aad360"></a> `00aad360` | `ff 27 00 f9` | str xzr,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00aad364"></a> `00aad364` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aad368"></a> `00aad368` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aad36c"></a> `00aad36c` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aad370"></a> `00aad370` | `58 b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad374"></a> `00aad374` | `c8 7e 40 93` | sxtw x8,w22 | `FALL_THROUGH`
<a id="insn-00aad378"></a> `00aad378` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aad37c"></a> `00aad37c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aad380"></a> `00aad380` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aad384"></a> `00aad384` | `57 b9 06 94` | bl 0x00c5b8e0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad388"></a> `00aad388` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aad38c"></a> `00aad38c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad390"></a> `00aad390` | `50 b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad394"></a> `00aad394` | `c8 bf ff d0` | adrp x8,0x2a7000 | `FALL_THROUGH`
<a id="insn-00aad398"></a> `00aad398` | `08 d9 2e 91` | add x8,x8,#0xbb6 | `FALL_THROUGH`
<a id="insn-00aad39c"></a> `00aad39c` | `ff 63 00 b9` | str wzr,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00aad3a0"></a> `00aad3a0` | `e8 2f 00 f9` | str x8,[sp, #0x58] | `FALL_THROUGH`
<a id="insn-00aad3a4"></a> `00aad3a4` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aad3a8"></a> `00aad3a8` | `15 01 01 91` | add x21,x8,#0x40 | `FALL_THROUGH`
<a id="insn-00aad3ac"></a> `00aad3ac` | `14 21 01 91` | add x20,x8,#0x48 | `FALL_THROUGH`
<a id="insn-00aad3b0"></a> `00aad3b0` | `ff 37 00 f9` | str xzr,[sp, #0x68] | `FALL_THROUGH`
<a id="insn-00aad3b4"></a> `00aad3b4` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aad3b8"></a> `00aad3b8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aad3bc"></a> `00aad3bc` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00aad3c0"></a> `00aad3c0` | `44 b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad3c4"></a> `00aad3c4` | `68 c0 ff d0` | adrp x8,0x2bb000 | `FALL_THROUGH`
<a id="insn-00aad3c8"></a> `00aad3c8` | `08 f5 35 91` | add x8,x8,#0xd7d | `FALL_THROUGH`
<a id="insn-00aad3cc"></a> `00aad3cc` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aad3d0"></a> `00aad3d0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aad3d4"></a> `00aad3d4` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aad3d8"></a> `00aad3d8` | `42 b9 06 94` | bl 0x00c5b8e0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad3dc"></a> `00aad3dc` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aad3e0"></a> `00aad3e0` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad3e4"></a> `00aad3e4` | `3b b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad3e8"></a> `00aad3e8` | `08 c0 ff d0` | adrp x8,0x2af000 | `FALL_THROUGH`
<a id="insn-00aad3ec"></a> `00aad3ec` | `08 99 32 91` | add x8,x8,#0xca6 | `FALL_THROUGH`
<a id="insn-00aad3f0"></a> `00aad3f0` | `ff 83 00 b9` | str wzr,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00aad3f4"></a> `00aad3f4` | `e8 3f 00 f9` | str x8,[sp, #0x78] | `FALL_THROUGH`
<a id="insn-00aad3f8"></a> `00aad3f8` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aad3fc"></a> `00aad3fc` | `15 81 01 91` | add x21,x8,#0x60 | `FALL_THROUGH`
<a id="insn-00aad400"></a> `00aad400` | `14 a1 01 91` | add x20,x8,#0x68 | `FALL_THROUGH`
<a id="insn-00aad404"></a> `00aad404` | `ff 47 00 f9` | str xzr,[sp, #0x88] | `FALL_THROUGH`
<a id="insn-00aad408"></a> `00aad408` | `ff 03 00 b9` | str wzr,[sp] | `FALL_THROUGH`
<a id="insn-00aad40c"></a> `00aad40c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aad410"></a> `00aad410` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00aad414"></a> `00aad414` | `2f b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad418"></a> `00aad418` | `68 02 40 92` | and x8,x19,#0x1 | `FALL_THROUGH`
<a id="insn-00aad41c"></a> `00aad41c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00aad420"></a> `00aad420` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00aad424"></a> `00aad424` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00aad428"></a> `00aad428` | `2e b9 06 94` | bl 0x00c5b8e0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad42c"></a> `00aad42c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00aad430"></a> `00aad430` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad434"></a> `00aad434` | `27 b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad438"></a> `00aad438` | `31 94 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00aad43c"></a> `00aad43c` | `00 58 51 f9` | ldr x0,[x0, #0x22b0] | `FALL_THROUGH`
<a id="insn-00aad440"></a> `00aad440` | `81 c0 ff d0` | adrp x1,0x2bf000 | `FALL_THROUGH`
<a id="insn-00aad444"></a> `00aad444` | `21 bc 1d 91` | add x1,x1,#0x76f | `FALL_THROUGH`
<a id="insn-00aad448"></a> `00aad448` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aad44c"></a> `00aad44c` | `83 00 80 52` | mov w3,#0x4 | `FALL_THROUGH`
<a id="insn-00aad450"></a> `00aad450` | `f3 63 00 91` | add x19,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aad454"></a> `00aad454` | `93 33 f7 97` | bl 0x0087a2a0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad458"></a> `00aad458` | `60 a2 01 91` | add x0,x19,#0x68 | `FALL_THROUGH`
<a id="insn-00aad45c"></a> `00aad45c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad460"></a> `00aad460` | `1c b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad464"></a> `00aad464` | `f3 63 00 91` | add x19,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aad468"></a> `00aad468` | `60 22 01 91` | add x0,x19,#0x48 | `FALL_THROUGH`
<a id="insn-00aad46c"></a> `00aad46c` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad470"></a> `00aad470` | `18 b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad474"></a> `00aad474` | `60 a2 00 91` | add x0,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00aad478"></a> `00aad478` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad47c"></a> `00aad47c` | `15 b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad480"></a> `00aad480` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00aad484"></a> `00aad484` | `00 21 00 91` | add x0,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00aad488"></a> `00aad488` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00aad48c"></a> `00aad48c` | `11 b9 06 94` | bl 0x00c5b8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00aad490"></a> `00aad490` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-00aad494"></a> `00aad494` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00aad498"></a> `00aad498` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00aad49c"></a> `00aad49c` | `61 05 00 54` | b.ne 0x00aad548 | `CONDITIONAL_JUMP`
<a id="insn-00aad4a0"></a> `00aad4a0` | `f4 4f 4d a9` | ldp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00aad4a4"></a> `00aad4a4` | `f7 5b 40 f9` | ldr x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00aad4a8"></a> `00aad4a8` | `f6 57 4c a9` | ldp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00aad4ac"></a> `00aad4ac` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00aad4b0"></a> `00aad4b0` | `ff 83 03 91` | add sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-00aad4b4"></a> `00aad4b4` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00aad548"></a> `00aad548` | `8e ae 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00aad2cc`](#insn-00aad2cc) 範囲 `[['00aad2cc', '00aad317']]`
  - `FALL_THROUGH` [`00aad314`](#insn-00aad314) → [`00aad318`](#insn-00aad318)
- ブロック [`00aad318`](#insn-00aad318) 範囲 `[['00aad318', '00aad357']]`
  - `FALL_THROUGH` [`00aad354`](#insn-00aad354) → [`00aad358`](#insn-00aad358)
- ブロック [`00aad358`](#insn-00aad358) 範囲 `[['00aad358', '00aad3bb']]`
  - `FALL_THROUGH` [`00aad3b8`](#insn-00aad3b8) → [`00aad3bc`](#insn-00aad3bc)
- ブロック [`00aad3bc`](#insn-00aad3bc) 範囲 `[['00aad3bc', '00aad3c3']]`
  - `FALL_THROUGH` [`00aad3c0`](#insn-00aad3c0) → [`00aad3c4`](#insn-00aad3c4)
- ブロック [`00aad3c4`](#insn-00aad3c4) 範囲 `[['00aad3c4', '00aad3cb']]`
  - `FALL_THROUGH` [`00aad3c8`](#insn-00aad3c8) → [`00aad3cc`](#insn-00aad3cc)
- ブロック [`00aad3cc`](#insn-00aad3cc) 範囲 `[['00aad3cc', '00aad443']]`
  - `FALL_THROUGH` [`00aad440`](#insn-00aad440) → [`00aad444`](#insn-00aad444)
- ブロック [`00aad444`](#insn-00aad444) 範囲 `[['00aad444', '00aad49f']]`
  - `CONDITIONAL_JUMP` [`00aad49c`](#insn-00aad49c) → [`00aad548`](#insn-00aad548)
  - `FALL_THROUGH` [`00aad49c`](#insn-00aad49c) → [`00aad4a0`](#insn-00aad4a0)
- ブロック [`00aad4a0`](#insn-00aad4a0) 範囲 `[['00aad4a0', '00aad4b7']]`
- ブロック [`00aad548`](#insn-00aad548) 範囲 `[['00aad548', '00aad54b']]`

## 命令位置別の参照

- [`00aad2d0`](#insn-00aad2d0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad2d4`](#insn-00aad2d4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad2d8`](#insn-00aad2d8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad2dc`](#insn-00aad2dc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad2f8`](#insn-00aad2f8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad304`](#insn-00aad304) → `002aeb6f`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad304`](#insn-00aad304) → `Stack[-0xc8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad308`](#insn-00aad308) → `Stack[-0xc0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad30c`](#insn-00aad30c) → `Stack[-0xb8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad310`](#insn-00aad310) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad31c`](#insn-00aad31c) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad330`](#insn-00aad330) → `002b98ce`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad330`](#insn-00aad330) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad334`](#insn-00aad334) → [`00c5b8e0`](../00c5b/00c5b8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8e0` · 推定シンボル `None` · 推定型 `None`
- [`00aad340`](#insn-00aad340) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad34c`](#insn-00aad34c) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad350`](#insn-00aad350) → `002b1ec3`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad350`](#insn-00aad350) → `Stack[-0xa8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad360`](#insn-00aad360) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad364`](#insn-00aad364) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad370`](#insn-00aad370) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad380`](#insn-00aad380) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad384`](#insn-00aad384) → [`00c5b8e0`](../00c5b/00c5b8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8e0` · 推定シンボル `None` · 推定型 `None`
- [`00aad390`](#insn-00aad390) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad39c`](#insn-00aad39c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad3a0`](#insn-00aad3a0) → `002a7bb6`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad3a0`](#insn-00aad3a0) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad3b0`](#insn-00aad3b0) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad3b4`](#insn-00aad3b4) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad3c0`](#insn-00aad3c0) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad3d4`](#insn-00aad3d4) → `002bbd7d`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad3d4`](#insn-00aad3d4) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad3d8`](#insn-00aad3d8) → [`00c5b8e0`](../00c5b/00c5b8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8e0` · 推定シンボル `None` · 推定型 `None`
- [`00aad3e4`](#insn-00aad3e4) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad3f0`](#insn-00aad3f0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad3f4`](#insn-00aad3f4) → `002afca6`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad3f4`](#insn-00aad3f4) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad404`](#insn-00aad404) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad408`](#insn-00aad408) → `Stack[-0xe0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad414`](#insn-00aad414) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad424`](#insn-00aad424) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad428`](#insn-00aad428) → [`00c5b8e0`](../00c5b/00c5b8e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8e0` · 推定シンボル `None` · 推定型 `None`
- [`00aad434`](#insn-00aad434) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad438`](#insn-00aad438) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00aad444`](#insn-00aad444) → `002bf76f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00aad454`](#insn-00aad454) → [`0087a2a0`](../0087a/0087a2a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0087a2a0` · 推定シンボル `None` · 推定型 `None`
- [`00aad460`](#insn-00aad460) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad470`](#insn-00aad470) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad47c`](#insn-00aad47c) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad48c`](#insn-00aad48c) → [`00c5b8d0`](../00c5b/00c5b8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b8d0` · 推定シンボル `None` · 推定型 `None`
- [`00aad494`](#insn-00aad494) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad49c`](#insn-00aad49c) → [`00aad548`](#insn-00aad548) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad4a0`](#insn-00aad4a0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad4a4`](#insn-00aad4a4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad4a8`](#insn-00aad4a8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad4ac`](#insn-00aad4ac) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00aad548`](#insn-00aad548) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00aad2d0`](#insn-00aad2d0)

~~~json
{
  "source": "00aad2d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad2d4`](#insn-00aad2d4)

~~~json
{
  "source": "00aad2d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad2d8`](#insn-00aad2d8)

~~~json
{
  "source": "00aad2d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad2dc`](#insn-00aad2dc)

~~~json
{
  "source": "00aad2dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad2f8`](#insn-00aad2f8)

~~~json
{
  "source": "00aad2f8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad304`](#insn-00aad304)

~~~json
{
  "source": "00aad304",
  "target": "002aeb6f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aeb6f",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563315f7479706500",
  "capture_start": "002aeb6f",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad304`](#insn-00aad304)

~~~json
{
  "source": "00aad304",
  "target": "Stack[-0xc8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad308`](#insn-00aad308)

~~~json
{
  "source": "00aad308",
  "target": "Stack[-0xc0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad30c`](#insn-00aad30c)

~~~json
{
  "source": "00aad30c",
  "target": "Stack[-0xb8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad310`](#insn-00aad310)

~~~json
{
  "source": "00aad310",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad31c`](#insn-00aad31c)

~~~json
{
  "source": "00aad31c",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad330`](#insn-00aad330)

~~~json
{
  "source": "00aad330",
  "target": "002b98ce",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b98ce",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "536c6f74494400",
  "capture_start": "002b98ce",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad330`](#insn-00aad330)

~~~json
{
  "source": "00aad330",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad334`](#insn-00aad334)

~~~json
{
  "source": "00aad334",
  "target": "00c5b8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad340`](#insn-00aad340)

~~~json
{
  "source": "00aad340",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad34c`](#insn-00aad34c)

~~~json
{
  "source": "00aad34c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad350`](#insn-00aad350)

~~~json
{
  "source": "00aad350",
  "target": "002b1ec3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b1ec3",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563315f696400",
  "capture_start": "002b1ec3",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad350`](#insn-00aad350)

~~~json
{
  "source": "00aad350",
  "target": "Stack[-0xa8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad360`](#insn-00aad360)

~~~json
{
  "source": "00aad360",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad364`](#insn-00aad364)

~~~json
{
  "source": "00aad364",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad370`](#insn-00aad370)

~~~json
{
  "source": "00aad370",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad380`](#insn-00aad380)

~~~json
{
  "source": "00aad380",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad384`](#insn-00aad384)

~~~json
{
  "source": "00aad384",
  "target": "00c5b8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad390`](#insn-00aad390)

~~~json
{
  "source": "00aad390",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad39c`](#insn-00aad39c)

~~~json
{
  "source": "00aad39c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad3a0`](#insn-00aad3a0)

~~~json
{
  "source": "00aad3a0",
  "target": "002a7bb6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7bb6",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "736563325f7479706500",
  "capture_start": "002a7bb6",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad3a0`](#insn-00aad3a0)

~~~json
{
  "source": "00aad3a0",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad3b0`](#insn-00aad3b0)

~~~json
{
  "source": "00aad3b0",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad3b4`](#insn-00aad3b4)

~~~json
{
  "source": "00aad3b4",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad3c0`](#insn-00aad3c0)

~~~json
{
  "source": "00aad3c0",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad3d4`](#insn-00aad3d4)

~~~json
{
  "source": "00aad3d4",
  "target": "002bbd7d",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad3d4`](#insn-00aad3d4)

~~~json
{
  "source": "00aad3d4",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad3d8`](#insn-00aad3d8)

~~~json
{
  "source": "00aad3d8",
  "target": "00c5b8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad3e4`](#insn-00aad3e4)

~~~json
{
  "source": "00aad3e4",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad3f0`](#insn-00aad3f0)

~~~json
{
  "source": "00aad3f0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad3f4`](#insn-00aad3f4)

~~~json
{
  "source": "00aad3f4",
  "target": "002afca6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002afca6",
  "offset": 0,
  "size": 8,
  "datatype": "string",
  "bytes": "736563325f696400",
  "capture_start": "002afca6",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad3f4`](#insn-00aad3f4)

~~~json
{
  "source": "00aad3f4",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad404`](#insn-00aad404)

~~~json
{
  "source": "00aad404",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad408`](#insn-00aad408)

~~~json
{
  "source": "00aad408",
  "target": "Stack[-0xe0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad414`](#insn-00aad414)

~~~json
{
  "source": "00aad414",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad424`](#insn-00aad424)

~~~json
{
  "source": "00aad424",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad428`](#insn-00aad428)

~~~json
{
  "source": "00aad428",
  "target": "00c5b8e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad434`](#insn-00aad434)

~~~json
{
  "source": "00aad434",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad438`](#insn-00aad438)

~~~json
{
  "source": "00aad438",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad444`](#insn-00aad444)

~~~json
{
  "source": "00aad444",
  "target": "002bf76f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bf76f",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "4263526573536c6f7400",
  "capture_start": "002bf76f",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00aad454`](#insn-00aad454)

~~~json
{
  "source": "00aad454",
  "target": "0087a2a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad460`](#insn-00aad460)

~~~json
{
  "source": "00aad460",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad470`](#insn-00aad470)

~~~json
{
  "source": "00aad470",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad47c`](#insn-00aad47c)

~~~json
{
  "source": "00aad47c",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad48c`](#insn-00aad48c)

~~~json
{
  "source": "00aad48c",
  "target": "00c5b8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00aad494`](#insn-00aad494)

~~~json
{
  "source": "00aad494",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad49c`](#insn-00aad49c)

~~~json
{
  "source": "00aad49c",
  "target": "00aad548",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad4a0`](#insn-00aad4a0)

~~~json
{
  "source": "00aad4a0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad4a4`](#insn-00aad4a4)

~~~json
{
  "source": "00aad4a4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad4a8`](#insn-00aad4a8)

~~~json
{
  "source": "00aad4a8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad4ac`](#insn-00aad4ac)

~~~json
{
  "source": "00aad4ac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00aad548`](#insn-00aad548)

~~~json
{
  "source": "00aad548",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
