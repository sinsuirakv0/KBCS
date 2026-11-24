# 00c0efcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c0eba4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c0e/00c0eba4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0087.md#compare-584d5f43acf44525721d75865ca8458a)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c0f068`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c0f/00c0f068.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0087.md#compare-7d4a506b230d9d06849b2b1d6a666ddd)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c0efcc",
  "name": "FUN_00c0efcc",
  "size": 528,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ad9f9836e170316636939fa2098d5e2f889a0686176c9498eace4fa95fd89159",
  "source_text_sha256": "ad9f9836e170316636939fa2098d5e2f889a0686176c9498eace4fa95fd89159",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c0efcc",
        "00c0f1db"
      ]
    ],
    "bytes_sha256": "27c64ad37bda02704271f085aae8a918d74fe05495e2bb78d02917fde7ccfaba",
    "instruction_count": 132,
    "instruction_bytes": 528,
    "body_bytes": 528,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c0efbc](../00c0e/00c0efbc.md)

## 呼び出し先

- [00459668](../00459/00459668.md)
- [00c101a4](../00c10/00c101a4.md)
- [00c57e50](../00c57/00c57e50.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c58270](../00c58/00c58270.md)
- [00c58290](../00c58/00c58290.md)
- [00c5d220](../00c5d/00c5d220.md)
- [00c5e5d0](../00c5e/00c5e5d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2362 bytes

~~~c

void FUN_00c0efcc(undefined8 param_1,undefined8 param_2,long param_3,undefined4 param_4,
                 undefined8 param_5,char *param_6)

{
  uint uVar1;
  int iVar2;
  char *pcVar3;
  char *pcVar4;
  char cVar5;
  undefined1 auStack_a0 [8];
  undefined8 local_98;
  undefined8 uStack_90;
  undefined1 auStack_85 [45];
  char local_58 [24];
  undefined8 local_28;
  
  uVar1 = *(uint *)(param_3 + 8);
  local_28 = 0x25;
  pcVar3 = (char *)((ulong)&local_28 | 1);
  if ((((uVar1 >> 0xb & 1) != 0) && ((uVar1 & 0x4a) != 8)) && ((uVar1 & 0x4a) != 0x40)) {
    pcVar3 = (char *)((ulong)&local_28 | 2);
    local_28 = 0x2b25;
  }
  pcVar4 = pcVar3;
  if ((uVar1 >> 9 & 1) != 0) {
    pcVar4 = pcVar3 + 1;
    *pcVar3 = '#';
  }
  cVar5 = *param_6;
  while (cVar5 != '\0') {
    param_6 = param_6 + 1;
    *pcVar4 = cVar5;
    pcVar4 = pcVar4 + 1;
    cVar5 = *param_6;
  }
  if ((uVar1 & 0x4a) == 0x40) {
    cVar5 = 'o';
  }
  else if ((uVar1 & 0x4a) == 8) {
    cVar5 = 'x';
                    /* catch() { ... } // from try @ 00c0f258 with catch @ 00c0f07c */
    if ((uVar1 & 0x4000) != 0) {
      cVar5 = 'X';
    }
  }
  else {
    cVar5 = 'd';
  }
  *pcVar4 = cVar5;
  if (((DAT_01127ca0 & 1) == 0) && (iVar2 = __cxa_guard_acquire(&DAT_01127ca0), iVar2 != 0)) {
    DAT_01127c98 = newlocale(0x1fbf,"C",(__locale_t)0x0);
                    /* try { // try from 00c0f1d0 to 00d0f257 has its CatchHandler @ 00c0f33c */
    __cxa_guard_release(&DAT_01127ca0);
  }
  iVar2 = FUN_00c101a4(local_58,0x18,DAT_01127c98,&local_28,param_5);
  uVar1 = *(uint *)(param_3 + 8) & 0xb0;
  pcVar3 = local_58 + iVar2;
  if (uVar1 == 0x20) goto LAB_00c0f13c;
  if (uVar1 == 0x10) {
    if ((local_58[0] == '-') || (local_58[0] == '+')) {
      pcVar3 = (char *)((ulong)local_58 | 1);
      goto LAB_00c0f13c;
    }
    if (((1 < iVar2) && (local_58[0] == '0')) && ((byte)(local_58[1] | 0x20U) == 0x78)) {
      pcVar3 = (char *)((ulong)local_58 | 2);
      goto LAB_00c0f13c;
    }
  }
  pcVar3 = local_58;
LAB_00c0f13c:
  _ZNKSt6__ndk18ios_base6getlocEv(auStack_a0,param_3);
  _ZNSt6__ndk19__num_putIcE21__widen_and_group_intEPcS2_S2_S2_RS2_S3_RKNS_6localeE
            (local_58,pcVar3,local_58 + iVar2,auStack_85,&uStack_90,&local_98,auStack_a0);
  _ZNSt6__ndk16localeD1Ev(auStack_a0);
  FUN_00459668(param_2,auStack_85,uStack_90,local_98,param_3,param_4);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c0efcc"></a> `00c0efcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c0efd0"></a> `00c0efd0` | `ff 83 02 d1` | sub sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00c0efd4"></a> `00c0efd4` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00c0efd8"></a> `00c0efd8` | `f7 3b 00 f9` | str x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00c0efdc"></a> `00c0efdc` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00c0efe0"></a> `00c0efe0` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00c0efe4"></a> `00c0efe4` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00c0efe8"></a> `00c0efe8` | `49 08 40 b9` | ldr w9,[x2, #0x8] | `FALL_THROUGH`
<a id="insn-00c0efec"></a> `00c0efec` | `a8 04 80 52` | mov w8,#0x25 | `FALL_THROUGH`
<a id="insn-00c0eff0"></a> `00c0eff0` | `aa 63 00 91` | add x10,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c0eff4"></a> `00c0eff4` | `f6 03 04 aa` | mov x22,x4 | `FALL_THROUGH`
<a id="insn-00c0eff8"></a> `00c0eff8` | `f3 03 03 2a` | mov w19,w3 | `FALL_THROUGH`
<a id="insn-00c0effc"></a> `00c0effc` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00c0f000"></a> `00c0f000` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00c0f004"></a> `00c0f004` | `a8 0f 00 f9` | str x8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00c0f008"></a> `00c0f008` | `48 01 40 b2` | orr x8,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00c0f00c"></a> `00c0f00c` | `69 01 58 36` | tbz w9,#0xb,0x00c0f038 | `CONDITIONAL_JUMP`
<a id="insn-00c0f010"></a> `00c0f010` | `4a 09 80 52` | mov w10,#0x4a | `FALL_THROUGH`
<a id="insn-00c0f014"></a> `00c0f014` | `2a 01 0a 0a` | and w10,w9,w10 | `FALL_THROUGH`
<a id="insn-00c0f018"></a> `00c0f018` | `5f 21 00 71` | cmp w10,#0x8 | `FALL_THROUGH`
<a id="insn-00c0f01c"></a> `00c0f01c` | `e0 00 00 54` | b.eq 0x00c0f038 | `CONDITIONAL_JUMP`
<a id="insn-00c0f020"></a> `00c0f020` | `5f 01 01 71` | cmp w10,#0x40 | `FALL_THROUGH`
<a id="insn-00c0f024"></a> `00c0f024` | `a0 00 00 54` | b.eq 0x00c0f038 | `CONDITIONAL_JUMP`
<a id="insn-00c0f028"></a> `00c0f028` | `a8 63 00 91` | add x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c0f02c"></a> `00c0f02c` | `6a 05 80 52` | mov w10,#0x2b | `FALL_THROUGH`
<a id="insn-00c0f030"></a> `00c0f030` | `08 01 7f b2` | orr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c0f034"></a> `00c0f034` | `aa 67 00 39` | strb w10,[x29, #0x19] | `FALL_THROUGH`
<a id="insn-00c0f038"></a> `00c0f038` | `69 00 48 36` | tbz w9,#0x9,0x00c0f044 | `CONDITIONAL_JUMP`
<a id="insn-00c0f03c"></a> `00c0f03c` | `6a 04 80 52` | mov w10,#0x23 | `FALL_THROUGH`
<a id="insn-00c0f040"></a> `00c0f040` | `0a 15 00 38` | strb w10,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c0f044"></a> `00c0f044` | `aa 00 40 39` | ldrb w10,[x5] | `FALL_THROUGH`
<a id="insn-00c0f048"></a> `00c0f048` | `aa 00 00 34` | cbz w10,0x00c0f05c | `CONDITIONAL_JUMP`
<a id="insn-00c0f04c"></a> `00c0f04c` | `ab 04 00 91` | add x11,x5,#0x1 | `FALL_THROUGH`
<a id="insn-00c0f050"></a> `00c0f050` | `0a 15 00 38` | strb w10,[x8], #0x1 | `FALL_THROUGH`
<a id="insn-00c0f054"></a> `00c0f054` | `6a 15 40 38` | ldrb w10,[x11], #0x1 | `FALL_THROUGH`
<a id="insn-00c0f058"></a> `00c0f058` | `ca ff ff 35` | cbnz w10,0x00c0f050 | `CONDITIONAL_JUMP`
<a id="insn-00c0f05c"></a> `00c0f05c` | `4a 09 80 52` | mov w10,#0x4a | `FALL_THROUGH`
<a id="insn-00c0f060"></a> `00c0f060` | `2a 01 0a 0a` | and w10,w9,w10 | `FALL_THROUGH`
<a id="insn-00c0f064"></a> `00c0f064` | `5f 01 01 71` | cmp w10,#0x40 | `FALL_THROUGH`
<a id="insn-00c0f068"></a> `00c0f068` | `00 01 00 54` | b.eq 0x00c0f088 | `CONDITIONAL_JUMP`
<a id="insn-00c0f06c"></a> `00c0f06c` | `5f 21 00 71` | cmp w10,#0x8 | `FALL_THROUGH`
<a id="insn-00c0f070"></a> `00c0f070` | `01 01 00 54` | b.ne 0x00c0f090 | `CONDITIONAL_JUMP`
<a id="insn-00c0f074"></a> `00c0f074` | `3f 01 12 72` | tst w9,#0x4000 | `FALL_THROUGH`
<a id="insn-00c0f078"></a> `00c0f078` | `09 0b 80 52` | mov w9,#0x58 | `FALL_THROUGH`
<a id="insn-00c0f07c"></a> `00c0f07c` | `0a 0f 80 52` | mov w10,#0x78 | `FALL_THROUGH`
<a id="insn-00c0f080"></a> `00c0f080` | `49 01 89 1a` | csel w9,w10,w9,eq | `FALL_THROUGH`
<a id="insn-00c0f084"></a> `00c0f084` | `04 00 00 14` | b 0x00c0f094 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0f088"></a> `00c0f088` | `e9 0d 80 52` | mov w9,#0x6f | `FALL_THROUGH`
<a id="insn-00c0f08c"></a> `00c0f08c` | `02 00 00 14` | b 0x00c0f094 | `UNCONDITIONAL_JUMP`
<a id="insn-00c0f090"></a> `00c0f090` | `89 0c 80 52` | mov w9,#0x64 | `FALL_THROUGH`
<a id="insn-00c0f094"></a> `00c0f094` | `09 01 00 39` | strb w9,[x8] | `FALL_THROUGH`
<a id="insn-00c0f098"></a> `00c0f098` | `c8 28 00 90` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00c0f09c"></a> `00c0f09c` | `08 81 32 91` | add x8,x8,#0xca0 | `FALL_THROUGH`
<a id="insn-00c0f0a0"></a> `00c0f0a0` | `08 fd df 08` | ldarb w8,[x8] | `FALL_THROUGH`
<a id="insn-00c0f0a4"></a> `00c0f0a4` | `d7 28 00 90` | adrp x23,0x1127000 | `FALL_THROUGH`
<a id="insn-00c0f0a8"></a> `00c0f0a8` | `e8 07 00 36` | tbz w8,#0x0,0x00c0f1a4 | `CONDITIONAL_JUMP`
<a id="insn-00c0f0ac"></a> `00c0f0ac` | `e2 4e 46 f9` | ldr x2,[x23, #0xc98] | `FALL_THROUGH`
<a id="insn-00c0f0b0"></a> `00c0f0b0` | `a0 63 00 d1` | sub x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c0f0b4"></a> `00c0f0b4` | `a3 63 00 91` | add x3,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c0f0b8"></a> `00c0f0b8` | `01 03 80 52` | mov w1,#0x18 | `FALL_THROUGH`
<a id="insn-00c0f0bc"></a> `00c0f0bc` | `e4 03 16 aa` | mov x4,x22 | `FALL_THROUGH`
<a id="insn-00c0f0c0"></a> `00c0f0c0` | `b6 63 00 d1` | sub x22,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c0f0c4"></a> `00c0f0c4` | `38 04 00 94` | bl 0x00c101a4 | `UNCONDITIONAL_CALL`
<a id="insn-00c0f0c8"></a> `00c0f0c8` | `88 0a 40 b9` | ldr w8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00c0f0cc"></a> `00c0f0cc` | `09 16 80 52` | mov w9,#0xb0 | `FALL_THROUGH`
<a id="insn-00c0f0d0"></a> `00c0f0d0` | `d6 c2 20 8b` | add x22,x22,w0, SXTW  | `FALL_THROUGH`
<a id="insn-00c0f0d4"></a> `00c0f0d4` | `08 01 09 0a` | and w8,w8,w9 | `FALL_THROUGH`
<a id="insn-00c0f0d8"></a> `00c0f0d8` | `f7 03 16 aa` | mov x23,x22 | `FALL_THROUGH`
<a id="insn-00c0f0dc"></a> `00c0f0dc` | `1f 81 00 71` | cmp w8,#0x20 | `FALL_THROUGH`
<a id="insn-00c0f0e0"></a> `00c0f0e0` | `e0 02 00 54` | b.eq 0x00c0f13c | `CONDITIONAL_JUMP`
<a id="insn-00c0f0e4"></a> `00c0f0e4` | `1f 41 00 71` | cmp w8,#0x10 | `FALL_THROUGH`
<a id="insn-00c0f0e8"></a> `00c0f0e8` | `81 02 00 54` | b.ne 0x00c0f138 | `CONDITIONAL_JUMP`
<a id="insn-00c0f0ec"></a> `00c0f0ec` | `a8 83 5e 38` | ldurb w8,[x29, #-0x18] | `FALL_THROUGH`
<a id="insn-00c0f0f0"></a> `00c0f0f0` | `1f b5 00 71` | cmp w8,#0x2d | `FALL_THROUGH`
<a id="insn-00c0f0f4"></a> `00c0f0f4` | `60 00 00 54` | b.eq 0x00c0f100 | `CONDITIONAL_JUMP`
<a id="insn-00c0f0f8"></a> `00c0f0f8` | `1f ad 00 71` | cmp w8,#0x2b | `FALL_THROUGH`
<a id="insn-00c0f0fc"></a> `00c0f0fc` | `81 00 00 54` | b.ne 0x00c0f10c | `CONDITIONAL_JUMP`
<a id="insn-00c0f100"></a> `00c0f100` | `a8 63 00 d1` | sub x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c0f104"></a> `00c0f104` | `17 01 40 b2` | orr x23,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c0f108"></a> `00c0f108` | `0d 00 00 14` | b 0x00c0f13c | `UNCONDITIONAL_JUMP`
<a id="insn-00c0f10c"></a> `00c0f10c` | `1f 08 00 71` | cmp w0,#0x2 | `FALL_THROUGH`
<a id="insn-00c0f110"></a> `00c0f110` | `4b 01 00 54` | b.lt 0x00c0f138 | `CONDITIONAL_JUMP`
<a id="insn-00c0f114"></a> `00c0f114` | `1f c1 00 71` | cmp w8,#0x30 | `FALL_THROUGH`
<a id="insn-00c0f118"></a> `00c0f118` | `01 01 00 54` | b.ne 0x00c0f138 | `CONDITIONAL_JUMP`
<a id="insn-00c0f11c"></a> `00c0f11c` | `a8 93 5e 38` | ldurb w8,[x29, #-0x17] | `FALL_THROUGH`
<a id="insn-00c0f120"></a> `00c0f120` | `08 01 1b 32` | orr w8,w8,#0x20 | `FALL_THROUGH`
<a id="insn-00c0f124"></a> `00c0f124` | `1f e1 01 71` | cmp w8,#0x78 | `FALL_THROUGH`
<a id="insn-00c0f128"></a> `00c0f128` | `81 00 00 54` | b.ne 0x00c0f138 | `CONDITIONAL_JUMP`
<a id="insn-00c0f12c"></a> `00c0f12c` | `a8 63 00 d1` | sub x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c0f130"></a> `00c0f130` | `17 01 7f b2` | orr x23,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00c0f134"></a> `00c0f134` | `02 00 00 14` | b 0x00c0f13c | `UNCONDITIONAL_JUMP`
<a id="insn-00c0f138"></a> `00c0f138` | `b7 63 00 d1` | sub x23,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c0f13c"></a> `00c0f13c` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00c0f140"></a> `00c0f140` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00c0f144"></a> `00c0f144` | `4b 24 01 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00c0f148"></a> `00c0f148` | `a0 63 00 d1` | sub x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c0f14c"></a> `00c0f14c` | `e3 6f 00 91` | add x3,sp,#0x1b | `FALL_THROUGH`
<a id="insn-00c0f150"></a> `00c0f150` | `e4 43 00 91` | add x4,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00c0f154"></a> `00c0f154` | `e5 23 00 91` | add x5,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00c0f158"></a> `00c0f158` | `e6 03 00 91` | mov x6,sp | `FALL_THROUGH`
<a id="insn-00c0f15c"></a> `00c0f15c` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00c0f160"></a> `00c0f160` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00c0f164"></a> `00c0f164` | `1b 3d 01 94` | bl 0x00c5e5d0 | `UNCONDITIONAL_CALL`
<a id="insn-00c0f168"></a> `00c0f168` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00c0f16c"></a> `00c0f16c` | `49 24 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00c0f170"></a> `00c0f170` | `e3 8b 40 a9` | ldp x3,x2,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00c0f174"></a> `00c0f174` | `e1 6f 00 91` | add x1,sp,#0x1b | `FALL_THROUGH`
<a id="insn-00c0f178"></a> `00c0f178` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c0f17c"></a> `00c0f17c` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-00c0f180"></a> `00c0f180` | `e5 03 13 2a` | mov w5,w19 | `FALL_THROUGH`
<a id="insn-00c0f184"></a> `00c0f184` | `39 29 e1 97` | bl 0x00459668 | `UNCONDITIONAL_CALL`
<a id="insn-00c0f188"></a> `00c0f188` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00c0f18c"></a> `00c0f18c` | `f7 3b 40 f9` | ldr x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00c0f190"></a> `00c0f190` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00c0f194"></a> `00c0f194` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00c0f198"></a> `00c0f198` | `ff 83 02 91` | add sp,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00c0f19c"></a> `00c0f19c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c0f1a0"></a> `00c0f1a0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c0f1a4"></a> `00c0f1a4` | `c0 28 00 90` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00c0f1a8"></a> `00c0f1a8` | `00 80 32 91` | add x0,x0,#0xca0 | `FALL_THROUGH`
<a id="insn-00c0f1ac"></a> `00c0f1ac` | `29 23 01 94` | bl 0x00c57e50 | `UNCONDITIONAL_CALL`
<a id="insn-00c0f1b0"></a> `00c0f1b0` | `e0 f7 ff 34` | cbz w0,0x00c0f0ac | `CONDITIONAL_JUMP`
<a id="insn-00c0f1b4"></a> `00c0f1b4` | `21 b5 ff f0` | adrp x1,0x2b6000 | `FALL_THROUGH`
<a id="insn-00c0f1b8"></a> `00c0f1b8` | `21 f0 05 91` | add x1,x1,#0x17c | `FALL_THROUGH`
<a id="insn-00c0f1bc"></a> `00c0f1bc` | `e0 f7 83 52` | mov w0,#0x1fbf | `FALL_THROUGH`
<a id="insn-00c0f1c0"></a> `00c0f1c0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00c0f1c4"></a> `00c0f1c4` | `17 38 01 94` | bl 0x00c5d220 | `UNCONDITIONAL_CALL`
<a id="insn-00c0f1c8"></a> `00c0f1c8` | `e0 4e 06 f9` | str x0,[x23, #0xc98] | `FALL_THROUGH`
<a id="insn-00c0f1cc"></a> `00c0f1cc` | `c0 28 00 90` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00c0f1d0"></a> `00c0f1d0` | `00 80 32 91` | add x0,x0,#0xca0 | `FALL_THROUGH`
<a id="insn-00c0f1d4"></a> `00c0f1d4` | `27 23 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00c0f1d8"></a> `00c0f1d8` | `b5 ff ff 17` | b 0x00c0f0ac | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00c0efcc`](#insn-00c0efcc) 範囲 `[['00c0efcc', '00c0f00f']]`
  - `CONDITIONAL_JUMP` [`00c0f00c`](#insn-00c0f00c) → [`00c0f038`](#insn-00c0f038)
  - `FALL_THROUGH` [`00c0f00c`](#insn-00c0f00c) → [`00c0f010`](#insn-00c0f010)
- ブロック [`00c0f010`](#insn-00c0f010) 範囲 `[['00c0f010', '00c0f01f']]`
  - `CONDITIONAL_JUMP` [`00c0f01c`](#insn-00c0f01c) → [`00c0f038`](#insn-00c0f038)
  - `FALL_THROUGH` [`00c0f01c`](#insn-00c0f01c) → [`00c0f020`](#insn-00c0f020)
- ブロック [`00c0f020`](#insn-00c0f020) 範囲 `[['00c0f020', '00c0f027']]`
  - `CONDITIONAL_JUMP` [`00c0f024`](#insn-00c0f024) → [`00c0f038`](#insn-00c0f038)
  - `FALL_THROUGH` [`00c0f024`](#insn-00c0f024) → [`00c0f028`](#insn-00c0f028)
- ブロック [`00c0f028`](#insn-00c0f028) 範囲 `[['00c0f028', '00c0f037']]`
  - `FALL_THROUGH` [`00c0f034`](#insn-00c0f034) → [`00c0f038`](#insn-00c0f038)
- ブロック [`00c0f038`](#insn-00c0f038) 範囲 `[['00c0f038', '00c0f03b']]`
  - `CONDITIONAL_JUMP` [`00c0f038`](#insn-00c0f038) → [`00c0f044`](#insn-00c0f044)
  - `FALL_THROUGH` [`00c0f038`](#insn-00c0f038) → [`00c0f03c`](#insn-00c0f03c)
- ブロック [`00c0f03c`](#insn-00c0f03c) 範囲 `[['00c0f03c', '00c0f043']]`
  - `FALL_THROUGH` [`00c0f040`](#insn-00c0f040) → [`00c0f044`](#insn-00c0f044)
- ブロック [`00c0f044`](#insn-00c0f044) 範囲 `[['00c0f044', '00c0f04b']]`
  - `CONDITIONAL_JUMP` [`00c0f048`](#insn-00c0f048) → [`00c0f05c`](#insn-00c0f05c)
  - `FALL_THROUGH` [`00c0f048`](#insn-00c0f048) → [`00c0f04c`](#insn-00c0f04c)
- ブロック [`00c0f04c`](#insn-00c0f04c) 範囲 `[['00c0f04c', '00c0f04f']]`
  - `FALL_THROUGH` [`00c0f04c`](#insn-00c0f04c) → [`00c0f050`](#insn-00c0f050)
- ブロック [`00c0f050`](#insn-00c0f050) 範囲 `[['00c0f050', '00c0f05b']]`
  - `CONDITIONAL_JUMP` [`00c0f058`](#insn-00c0f058) → [`00c0f050`](#insn-00c0f050)
  - `FALL_THROUGH` [`00c0f058`](#insn-00c0f058) → [`00c0f05c`](#insn-00c0f05c)
- ブロック [`00c0f05c`](#insn-00c0f05c) 範囲 `[['00c0f05c', '00c0f06b']]`
  - `CONDITIONAL_JUMP` [`00c0f068`](#insn-00c0f068) → [`00c0f088`](#insn-00c0f088)
  - `FALL_THROUGH` [`00c0f068`](#insn-00c0f068) → [`00c0f06c`](#insn-00c0f06c)
- ブロック [`00c0f06c`](#insn-00c0f06c) 範囲 `[['00c0f06c', '00c0f073']]`
  - `CONDITIONAL_JUMP` [`00c0f070`](#insn-00c0f070) → [`00c0f090`](#insn-00c0f090)
  - `FALL_THROUGH` [`00c0f070`](#insn-00c0f070) → [`00c0f074`](#insn-00c0f074)
- ブロック [`00c0f074`](#insn-00c0f074) 範囲 `[['00c0f074', '00c0f07b']]`
  - `FALL_THROUGH` [`00c0f078`](#insn-00c0f078) → [`00c0f07c`](#insn-00c0f07c)
- ブロック [`00c0f07c`](#insn-00c0f07c) 範囲 `[['00c0f07c', '00c0f087']]`
  - `UNCONDITIONAL_JUMP` [`00c0f084`](#insn-00c0f084) → [`00c0f094`](#insn-00c0f094)
- ブロック [`00c0f088`](#insn-00c0f088) 範囲 `[['00c0f088', '00c0f08f']]`
  - `UNCONDITIONAL_JUMP` [`00c0f08c`](#insn-00c0f08c) → [`00c0f094`](#insn-00c0f094)
- ブロック [`00c0f090`](#insn-00c0f090) 範囲 `[['00c0f090', '00c0f093']]`
  - `FALL_THROUGH` [`00c0f090`](#insn-00c0f090) → [`00c0f094`](#insn-00c0f094)
- ブロック [`00c0f094`](#insn-00c0f094) 範囲 `[['00c0f094', '00c0f0ab']]`
  - `CONDITIONAL_JUMP` [`00c0f0a8`](#insn-00c0f0a8) → [`00c0f1a4`](#insn-00c0f1a4)
  - `FALL_THROUGH` [`00c0f0a8`](#insn-00c0f0a8) → [`00c0f0ac`](#insn-00c0f0ac)
- ブロック [`00c0f0ac`](#insn-00c0f0ac) 範囲 `[['00c0f0ac', '00c0f0e3']]`
  - `CONDITIONAL_JUMP` [`00c0f0e0`](#insn-00c0f0e0) → [`00c0f13c`](#insn-00c0f13c)
  - `FALL_THROUGH` [`00c0f0e0`](#insn-00c0f0e0) → [`00c0f0e4`](#insn-00c0f0e4)
- ブロック [`00c0f0e4`](#insn-00c0f0e4) 範囲 `[['00c0f0e4', '00c0f0eb']]`
  - `CONDITIONAL_JUMP` [`00c0f0e8`](#insn-00c0f0e8) → [`00c0f138`](#insn-00c0f138)
  - `FALL_THROUGH` [`00c0f0e8`](#insn-00c0f0e8) → [`00c0f0ec`](#insn-00c0f0ec)
- ブロック [`00c0f0ec`](#insn-00c0f0ec) 範囲 `[['00c0f0ec', '00c0f0f7']]`
  - `CONDITIONAL_JUMP` [`00c0f0f4`](#insn-00c0f0f4) → [`00c0f100`](#insn-00c0f100)
  - `FALL_THROUGH` [`00c0f0f4`](#insn-00c0f0f4) → [`00c0f0f8`](#insn-00c0f0f8)
- ブロック [`00c0f0f8`](#insn-00c0f0f8) 範囲 `[['00c0f0f8', '00c0f0ff']]`
  - `CONDITIONAL_JUMP` [`00c0f0fc`](#insn-00c0f0fc) → [`00c0f10c`](#insn-00c0f10c)
  - `FALL_THROUGH` [`00c0f0fc`](#insn-00c0f0fc) → [`00c0f100`](#insn-00c0f100)
- ブロック [`00c0f100`](#insn-00c0f100) 範囲 `[['00c0f100', '00c0f10b']]`
  - `UNCONDITIONAL_JUMP` [`00c0f108`](#insn-00c0f108) → [`00c0f13c`](#insn-00c0f13c)
- ブロック [`00c0f10c`](#insn-00c0f10c) 範囲 `[['00c0f10c', '00c0f113']]`
  - `CONDITIONAL_JUMP` [`00c0f110`](#insn-00c0f110) → [`00c0f138`](#insn-00c0f138)
  - `FALL_THROUGH` [`00c0f110`](#insn-00c0f110) → [`00c0f114`](#insn-00c0f114)
- ブロック [`00c0f114`](#insn-00c0f114) 範囲 `[['00c0f114', '00c0f11b']]`
  - `CONDITIONAL_JUMP` [`00c0f118`](#insn-00c0f118) → [`00c0f138`](#insn-00c0f138)
  - `FALL_THROUGH` [`00c0f118`](#insn-00c0f118) → [`00c0f11c`](#insn-00c0f11c)
- ブロック [`00c0f11c`](#insn-00c0f11c) 範囲 `[['00c0f11c', '00c0f12b']]`
  - `CONDITIONAL_JUMP` [`00c0f128`](#insn-00c0f128) → [`00c0f138`](#insn-00c0f138)
  - `FALL_THROUGH` [`00c0f128`](#insn-00c0f128) → [`00c0f12c`](#insn-00c0f12c)
- ブロック [`00c0f12c`](#insn-00c0f12c) 範囲 `[['00c0f12c', '00c0f137']]`
  - `UNCONDITIONAL_JUMP` [`00c0f134`](#insn-00c0f134) → [`00c0f13c`](#insn-00c0f13c)
- ブロック [`00c0f138`](#insn-00c0f138) 範囲 `[['00c0f138', '00c0f13b']]`
  - `FALL_THROUGH` [`00c0f138`](#insn-00c0f138) → [`00c0f13c`](#insn-00c0f13c)
- ブロック [`00c0f13c`](#insn-00c0f13c) 範囲 `[['00c0f13c', '00c0f1a3']]`
- ブロック [`00c0f1a4`](#insn-00c0f1a4) 範囲 `[['00c0f1a4', '00c0f1b3']]`
  - `CONDITIONAL_JUMP` [`00c0f1b0`](#insn-00c0f1b0) → [`00c0f0ac`](#insn-00c0f0ac)
  - `FALL_THROUGH` [`00c0f1b0`](#insn-00c0f1b0) → [`00c0f1b4`](#insn-00c0f1b4)
- ブロック [`00c0f1b4`](#insn-00c0f1b4) 範囲 `[['00c0f1b4', '00c0f1cf']]`
  - `FALL_THROUGH` [`00c0f1cc`](#insn-00c0f1cc) → [`00c0f1d0`](#insn-00c0f1d0)
- ブロック [`00c0f1d0`](#insn-00c0f1d0) 範囲 `[['00c0f1d0', '00c0f1db']]`
  - `UNCONDITIONAL_JUMP` [`00c0f1d8`](#insn-00c0f1d8) → [`00c0f0ac`](#insn-00c0f0ac)

## 命令位置別の参照

- [`00c0efd4`](#insn-00c0efd4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0efd8`](#insn-00c0efd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0efdc`](#insn-00c0efdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0efe0`](#insn-00c0efe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f004`](#insn-00c0f004) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f00c`](#insn-00c0f00c) → [`00c0f038`](#insn-00c0f038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f01c`](#insn-00c0f01c) → [`00c0f038`](#insn-00c0f038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f024`](#insn-00c0f024) → [`00c0f038`](#insn-00c0f038) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f034`](#insn-00c0f034) → `Stack[-0x27]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f038`](#insn-00c0f038) → [`00c0f044`](#insn-00c0f044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f048`](#insn-00c0f048) → [`00c0f05c`](#insn-00c0f05c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f058`](#insn-00c0f058) → [`00c0f050`](#insn-00c0f050) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f068`](#insn-00c0f068) → [`00c0f088`](#insn-00c0f088) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f070`](#insn-00c0f070) → [`00c0f090`](#insn-00c0f090) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f084`](#insn-00c0f084) → [`00c0f094`](#insn-00c0f094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f08c`](#insn-00c0f08c) → [`00c0f094`](#insn-00c0f094) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f0a0`](#insn-00c0f0a0) → `01127ca0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c0f0a8`](#insn-00c0f0a8) → [`00c0f1a4`](#insn-00c0f1a4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f0ac`](#insn-00c0f0ac) → `01127c98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c0f0c4`](#insn-00c0f0c4) → [`00c101a4`](../00c10/00c101a4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c101a4` · 推定シンボル `None` · 推定型 `None`
- [`00c0f0e0`](#insn-00c0f0e0) → [`00c0f13c`](#insn-00c0f13c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f0e8`](#insn-00c0f0e8) → [`00c0f138`](#insn-00c0f138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f0ec`](#insn-00c0f0ec) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f0f4`](#insn-00c0f0f4) → [`00c0f100`](#insn-00c0f100) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f0fc`](#insn-00c0f0fc) → [`00c0f10c`](#insn-00c0f10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f108`](#insn-00c0f108) → [`00c0f13c`](#insn-00c0f13c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f110`](#insn-00c0f110) → [`00c0f138`](#insn-00c0f138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f118`](#insn-00c0f118) → [`00c0f138`](#insn-00c0f138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f11c`](#insn-00c0f11c) → `Stack[-0x57]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f128`](#insn-00c0f128) → [`00c0f138`](#insn-00c0f138) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f134`](#insn-00c0f134) → [`00c0f13c`](#insn-00c0f13c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f144`](#insn-00c0f144) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00c0f164`](#insn-00c0f164) → [`00c5e5d0`](../00c5e/00c5e5d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e5d0` · 推定シンボル `None` · 推定型 `None`
- [`00c0f16c`](#insn-00c0f16c) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00c0f170`](#insn-00c0f170) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f184`](#insn-00c0f184) → [`00459668`](../00459/00459668.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00459668` · 推定シンボル `None` · 推定型 `None`
- [`00c0f188`](#insn-00c0f188) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f18c`](#insn-00c0f18c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f190`](#insn-00c0f190) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f194`](#insn-00c0f194) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f1a8`](#insn-00c0f1a8) → `01127ca0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c0f1ac`](#insn-00c0f1ac) → [`00c57e50`](../00c57/00c57e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e50` · 推定シンボル `None` · 推定型 `None`
- [`00c0f1b0`](#insn-00c0f1b0) → [`00c0f0ac`](#insn-00c0f0ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f1b8`](#insn-00c0f1b8) → `002b617c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c0f1c4`](#insn-00c0f1c4) → [`00c5d220`](../00c5d/00c5d220.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d220` · 推定シンボル `None` · 推定型 `None`
- [`00c0f1c8`](#insn-00c0f1c8) → `01127c98`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00c0f1d0`](#insn-00c0f1d0) → `01127ca0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00c0f1d4`](#insn-00c0f1d4) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00c0f1d8`](#insn-00c0f1d8) → [`00c0f0ac`](#insn-00c0f0ac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c0efd4`](#insn-00c0efd4)

~~~json
{
  "source": "00c0efd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0efd8`](#insn-00c0efd8)

~~~json
{
  "source": "00c0efd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0efdc`](#insn-00c0efdc)

~~~json
{
  "source": "00c0efdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0efe0`](#insn-00c0efe0)

~~~json
{
  "source": "00c0efe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f004`](#insn-00c0f004)

~~~json
{
  "source": "00c0f004",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f00c`](#insn-00c0f00c)

~~~json
{
  "source": "00c0f00c",
  "target": "00c0f038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f01c`](#insn-00c0f01c)

~~~json
{
  "source": "00c0f01c",
  "target": "00c0f038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f024`](#insn-00c0f024)

~~~json
{
  "source": "00c0f024",
  "target": "00c0f038",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f034`](#insn-00c0f034)

~~~json
{
  "source": "00c0f034",
  "target": "Stack[-0x27]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f038`](#insn-00c0f038)

~~~json
{
  "source": "00c0f038",
  "target": "00c0f044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f048`](#insn-00c0f048)

~~~json
{
  "source": "00c0f048",
  "target": "00c0f05c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f058`](#insn-00c0f058)

~~~json
{
  "source": "00c0f058",
  "target": "00c0f050",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f068`](#insn-00c0f068)

~~~json
{
  "source": "00c0f068",
  "target": "00c0f088",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f070`](#insn-00c0f070)

~~~json
{
  "source": "00c0f070",
  "target": "00c0f090",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f084`](#insn-00c0f084)

~~~json
{
  "source": "00c0f084",
  "target": "00c0f094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f08c`](#insn-00c0f08c)

~~~json
{
  "source": "00c0f08c",
  "target": "00c0f094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f0a0`](#insn-00c0f0a0)

~~~json
{
  "source": "00c0f0a0",
  "target": "01127ca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ca0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0f0a8`](#insn-00c0f0a8)

~~~json
{
  "source": "00c0f0a8",
  "target": "00c0f1a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f0ac`](#insn-00c0f0ac)

~~~json
{
  "source": "00c0f0ac",
  "target": "01127c98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0f0c4`](#insn-00c0f0c4)

~~~json
{
  "source": "00c0f0c4",
  "target": "00c101a4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0f0e0`](#insn-00c0f0e0)

~~~json
{
  "source": "00c0f0e0",
  "target": "00c0f13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f0e8`](#insn-00c0f0e8)

~~~json
{
  "source": "00c0f0e8",
  "target": "00c0f138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f0ec`](#insn-00c0f0ec)

~~~json
{
  "source": "00c0f0ec",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f0f4`](#insn-00c0f0f4)

~~~json
{
  "source": "00c0f0f4",
  "target": "00c0f100",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f0fc`](#insn-00c0f0fc)

~~~json
{
  "source": "00c0f0fc",
  "target": "00c0f10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f108`](#insn-00c0f108)

~~~json
{
  "source": "00c0f108",
  "target": "00c0f13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f110`](#insn-00c0f110)

~~~json
{
  "source": "00c0f110",
  "target": "00c0f138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f118`](#insn-00c0f118)

~~~json
{
  "source": "00c0f118",
  "target": "00c0f138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f11c`](#insn-00c0f11c)

~~~json
{
  "source": "00c0f11c",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f128`](#insn-00c0f128)

~~~json
{
  "source": "00c0f128",
  "target": "00c0f138",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f134`](#insn-00c0f134)

~~~json
{
  "source": "00c0f134",
  "target": "00c0f13c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f144`](#insn-00c0f144)

~~~json
{
  "source": "00c0f144",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0f164`](#insn-00c0f164)

~~~json
{
  "source": "00c0f164",
  "target": "00c5e5d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0f16c`](#insn-00c0f16c)

~~~json
{
  "source": "00c0f16c",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0f170`](#insn-00c0f170)

~~~json
{
  "source": "00c0f170",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f184`](#insn-00c0f184)

~~~json
{
  "source": "00c0f184",
  "target": "00459668",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0f188`](#insn-00c0f188)

~~~json
{
  "source": "00c0f188",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f18c`](#insn-00c0f18c)

~~~json
{
  "source": "00c0f18c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f190`](#insn-00c0f190)

~~~json
{
  "source": "00c0f190",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f194`](#insn-00c0f194)

~~~json
{
  "source": "00c0f194",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f1a8`](#insn-00c0f1a8)

~~~json
{
  "source": "00c0f1a8",
  "target": "01127ca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ca0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0f1ac`](#insn-00c0f1ac)

~~~json
{
  "source": "00c0f1ac",
  "target": "00c57e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0f1b0`](#insn-00c0f1b0)

~~~json
{
  "source": "00c0f1b0",
  "target": "00c0f0ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f1b8`](#insn-00c0f1b8)

~~~json
{
  "source": "00c0f1b8",
  "target": "002b617c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c0f1c4`](#insn-00c0f1c4)

~~~json
{
  "source": "00c0f1c4",
  "target": "00c5d220",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0f1c8`](#insn-00c0f1c8)

~~~json
{
  "source": "00c0f1c8",
  "target": "01127c98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0f1d0`](#insn-00c0f1d0)

~~~json
{
  "source": "00c0f1d0",
  "target": "01127ca0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ca0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c0f1d4`](#insn-00c0f1d4)

~~~json
{
  "source": "00c0f1d4",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c0f1d8`](#insn-00c0f1d8)

~~~json
{
  "source": "00c0f1d8",
  "target": "00c0f0ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
