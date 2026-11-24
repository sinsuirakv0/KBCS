# 00bfd4ac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfc4b8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfc/00bfc4b8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-5b81c4737a5b7f4b200f6bb4b1bde60f)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfd4ac",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE",
  "size": 344,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "8df2e4271da5cabb8710bde50fbc3f7034058318604713a0921f437f9d64040d",
  "source_text_sha256": "8df2e4271da5cabb8710bde50fbc3f7034058318604713a0921f437f9d64040d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfd4ac",
        "00bfd603"
      ]
    ],
    "bytes_sha256": "20cba9821f56c68acdcf333e04fff261469f17a459ac4e8b24128afbcc4538dc",
    "instruction_count": 86,
    "instruction_bytes": 344,
    "body_bytes": 344,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c59340](../00c59/00c59340.md)
- [00c5ae70](../00c5a/00c5ae70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1697 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEErsEPNS_15basic_streambufIcS2_EE
                 (long *param_1,long *param_2)

{
  long lVar1;
  undefined1 *puVar2;
  uint uVar3;
  int iVar4;
  long *plVar5;
  uint uVar6;
  char local_34 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_34,param_1,1);
  if (local_34[0] == '\0') {
    return param_1;
  }
  if (param_2 != (long *)0x0) {
LAB_00bfd518:
    plVar5 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
    if ((byte *)plVar5[3] == (byte *)plVar5[4]) {
      uVar3 = (**(code **)(*plVar5 + 0x48))();
      if (uVar3 == 0xffffffff) {
        uVar3 = 2;
        goto LAB_00bfd5c0;
      }
    }
    else {
      uVar3 = (uint)*(byte *)plVar5[3];
    }
    puVar2 = (undefined1 *)param_2[6];
    if (puVar2 == (undefined1 *)param_2[7]) {
      iVar4 = (**(code **)(*param_2 + 0x68))(param_2,uVar3 & 0xff);
      if (iVar4 == -1) goto LAB_00bfd5bc;
    }
    else {
      param_2[6] = (long)(puVar2 + 1);
      *puVar2 = (char)uVar3;
    }
    if (param_1[1] != 0x7fffffffffffffff) {
      param_1[1] = param_1[1] + 1;
    }
    plVar5 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
    if (plVar5[3] == plVar5[4]) {
      (**(code **)(*plVar5 + 0x50))();
    }
    else {
      plVar5[3] = plVar5[3] + 1;
    }
    goto LAB_00bfd518;
  }
  uVar6 = 4;
LAB_00bfd5d0:
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | uVar6);
  return param_1;
LAB_00bfd5bc:
  uVar3 = 0;
LAB_00bfd5c0:
  uVar6 = uVar3 | 4;
  if (param_1[1] != 0) {
    uVar6 = uVar3;
  }
  goto LAB_00bfd5d0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfd4ac"></a> `00bfd4ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfd4b0"></a> `00bfd4b0` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfd4b4"></a> `00bfd4b4` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfd4b8"></a> `00bfd4b8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfd4bc"></a> `00bfd4bc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfd4c0"></a> `00bfd4c0` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfd4c4"></a> `00bfd4c4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfd4c8"></a> `00bfd4c8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfd4cc"></a> `00bfd4cc` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd4d0"></a> `00bfd4d0` | `a0 13 00 d1` | sub x0,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfd4d4"></a> `00bfd4d4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfd4d8"></a> `00bfd4d8` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd4dc"></a> `00bfd4dc` | `65 76 01 94` | bl 0x00c5ae70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfd4e0"></a> `00bfd4e0` | `a8 c3 5f 38` | ldurb w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfd4e4"></a> `00bfd4e4` | `28 08 00 34` | cbz w8,0x00bfd5e8 | `CONDITIONAL_JUMP`
<a id="insn-00bfd4e8"></a> `00bfd4e8` | `34 06 00 b4` | cbz x20,0x00bfd5ac | `CONDITIONAL_JUMP`
<a id="insn-00bfd4ec"></a> `00bfd4ec` | `75 a2 00 91` | add x21,x19,#0x28 | `FALL_THROUGH`
<a id="insn-00bfd4f0"></a> `00bfd4f0` | `16 00 f0 92` | mov x22,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfd4f4"></a> `00bfd4f4` | `09 00 00 14` | b 0x00bfd518 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd4f8"></a> `00bfd4f8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfd4fc"></a> `00bfd4fc` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfd500"></a> `00bfd500` | `a0 6a 68 f8` | ldr x0,[x21, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfd504"></a> `00bfd504` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfd508"></a> `00bfd508` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfd50c"></a> `00bfd50c` | `80 04 00 54` | b.eq 0x00bfd59c | `CONDITIONAL_JUMP`
<a id="insn-00bfd510"></a> `00bfd510` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd514"></a> `00bfd514` | `08 0c 00 f9` | str x8,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfd518"></a> `00bfd518` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfd51c"></a> `00bfd51c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfd520"></a> `00bfd520` | `a0 6a 68 f8` | ldr x0,[x21, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfd524"></a> `00bfd524` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfd528"></a> `00bfd528` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfd52c"></a> `00bfd52c` | `60 00 00 54` | b.eq 0x00bfd538 | `CONDITIONAL_JUMP`
<a id="insn-00bfd530"></a> `00bfd530` | `00 01 40 39` | ldrb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfd534"></a> `00bfd534` | `06 00 00 14` | b 0x00bfd54c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd538"></a> `00bfd538` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfd53c"></a> `00bfd53c` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfd540"></a> `00bfd540` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfd544"></a> `00bfd544` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd548"></a> `00bfd548` | `60 03 00 54` | b.eq 0x00bfd5b4 | `CONDITIONAL_JUMP`
<a id="insn-00bfd54c"></a> `00bfd54c` | `88 26 43 a9` | ldp x8,x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bfd550"></a> `00bfd550` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfd554"></a> `00bfd554` | `a0 00 00 54` | b.eq 0x00bfd568 | `CONDITIONAL_JUMP`
<a id="insn-00bfd558"></a> `00bfd558` | `09 05 00 91` | add x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd55c"></a> `00bfd55c` | `89 1a 00 f9` | str x9,[x20, #0x30] | `FALL_THROUGH`
<a id="insn-00bfd560"></a> `00bfd560` | `00 01 00 39` | strb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfd564"></a> `00bfd564` | `08 00 00 14` | b 0x00bfd584 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd568"></a> `00bfd568` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfd56c"></a> `00bfd56c` | `08 35 40 f9` | ldr x8,[x8, #0x68] | `FALL_THROUGH`
<a id="insn-00bfd570"></a> `00bfd570` | `01 1c 00 12` | and w1,w0,#0xff | `FALL_THROUGH`
<a id="insn-00bfd574"></a> `00bfd574` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfd578"></a> `00bfd578` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfd57c"></a> `00bfd57c` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd580"></a> `00bfd580` | `e0 01 00 54` | b.eq 0x00bfd5bc | `CONDITIONAL_JUMP`
<a id="insn-00bfd584"></a> `00bfd584` | `68 06 40 f9` | ldr x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd588"></a> `00bfd588` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bfd58c"></a> `00bfd58c` | `60 fb ff 54` | b.eq 0x00bfd4f8 | `CONDITIONAL_JUMP`
<a id="insn-00bfd590"></a> `00bfd590` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd594"></a> `00bfd594` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd598"></a> `00bfd598` | `d8 ff ff 17` | b 0x00bfd4f8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd59c"></a> `00bfd59c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfd5a0"></a> `00bfd5a0` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfd5a4"></a> `00bfd5a4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfd5a8"></a> `00bfd5a8` | `dc ff ff 17` | b 0x00bfd518 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd5ac"></a> `00bfd5ac` | `94 00 80 52` | mov w20,#0x4 | `FALL_THROUGH`
<a id="insn-00bfd5b0"></a> `00bfd5b0` | `08 00 00 14` | b 0x00bfd5d0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd5b4"></a> `00bfd5b4` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bfd5b8"></a> `00bfd5b8` | `02 00 00 14` | b 0x00bfd5c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd5bc"></a> `00bfd5bc` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfd5c0"></a> `00bfd5c0` | `69 06 40 f9` | ldr x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd5c4"></a> `00bfd5c4` | `0a 01 1e 32` | orr w10,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfd5c8"></a> `00bfd5c8` | `3f 01 00 f1` | cmp x9,#0x0 | `FALL_THROUGH`
<a id="insn-00bfd5cc"></a> `00bfd5cc` | `54 01 88 1a` | csel w20,w10,w8,eq | `FALL_THROUGH`
<a id="insn-00bfd5d0"></a> `00bfd5d0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfd5d4"></a> `00bfd5d4` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfd5d8"></a> `00bfd5d8` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfd5dc"></a> `00bfd5dc` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfd5e0"></a> `00bfd5e0` | `01 01 14 2a` | orr w1,w8,w20 | `FALL_THROUGH`
<a id="insn-00bfd5e4"></a> `00bfd5e4` | `57 6f 01 94` | bl 0x00c59340 | `UNCONDITIONAL_CALL`
<a id="insn-00bfd5e8"></a> `00bfd5e8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfd5ec"></a> `00bfd5ec` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfd5f0"></a> `00bfd5f0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfd5f4"></a> `00bfd5f4` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfd5f8"></a> `00bfd5f8` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfd5fc"></a> `00bfd5fc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfd600"></a> `00bfd600` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfd4ac`](#insn-00bfd4ac) 範囲 `[['00bfd4ac', '00bfd4e7']]`
  - `CONDITIONAL_JUMP` [`00bfd4e4`](#insn-00bfd4e4) → [`00bfd5e8`](#insn-00bfd5e8)
  - `FALL_THROUGH` [`00bfd4e4`](#insn-00bfd4e4) → [`00bfd4e8`](#insn-00bfd4e8)
- ブロック [`00bfd4e8`](#insn-00bfd4e8) 範囲 `[['00bfd4e8', '00bfd4eb']]`
  - `CONDITIONAL_JUMP` [`00bfd4e8`](#insn-00bfd4e8) → [`00bfd5ac`](#insn-00bfd5ac)
  - `FALL_THROUGH` [`00bfd4e8`](#insn-00bfd4e8) → [`00bfd4ec`](#insn-00bfd4ec)
- ブロック [`00bfd4ec`](#insn-00bfd4ec) 範囲 `[['00bfd4ec', '00bfd4f7']]`
  - `UNCONDITIONAL_JUMP` [`00bfd4f4`](#insn-00bfd4f4) → [`00bfd518`](#insn-00bfd518)
- ブロック [`00bfd4f8`](#insn-00bfd4f8) 範囲 `[['00bfd4f8', '00bfd50f']]`
  - `CONDITIONAL_JUMP` [`00bfd50c`](#insn-00bfd50c) → [`00bfd59c`](#insn-00bfd59c)
  - `FALL_THROUGH` [`00bfd50c`](#insn-00bfd50c) → [`00bfd510`](#insn-00bfd510)
- ブロック [`00bfd510`](#insn-00bfd510) 範囲 `[['00bfd510', '00bfd517']]`
  - `FALL_THROUGH` [`00bfd514`](#insn-00bfd514) → [`00bfd518`](#insn-00bfd518)
- ブロック [`00bfd518`](#insn-00bfd518) 範囲 `[['00bfd518', '00bfd52f']]`
  - `CONDITIONAL_JUMP` [`00bfd52c`](#insn-00bfd52c) → [`00bfd538`](#insn-00bfd538)
  - `FALL_THROUGH` [`00bfd52c`](#insn-00bfd52c) → [`00bfd530`](#insn-00bfd530)
- ブロック [`00bfd530`](#insn-00bfd530) 範囲 `[['00bfd530', '00bfd537']]`
  - `UNCONDITIONAL_JUMP` [`00bfd534`](#insn-00bfd534) → [`00bfd54c`](#insn-00bfd54c)
- ブロック [`00bfd538`](#insn-00bfd538) 範囲 `[['00bfd538', '00bfd54b']]`
  - `CONDITIONAL_JUMP` [`00bfd548`](#insn-00bfd548) → [`00bfd5b4`](#insn-00bfd5b4)
  - `FALL_THROUGH` [`00bfd548`](#insn-00bfd548) → [`00bfd54c`](#insn-00bfd54c)
- ブロック [`00bfd54c`](#insn-00bfd54c) 範囲 `[['00bfd54c', '00bfd557']]`
  - `CONDITIONAL_JUMP` [`00bfd554`](#insn-00bfd554) → [`00bfd568`](#insn-00bfd568)
  - `FALL_THROUGH` [`00bfd554`](#insn-00bfd554) → [`00bfd558`](#insn-00bfd558)
- ブロック [`00bfd558`](#insn-00bfd558) 範囲 `[['00bfd558', '00bfd567']]`
  - `UNCONDITIONAL_JUMP` [`00bfd564`](#insn-00bfd564) → [`00bfd584`](#insn-00bfd584)
- ブロック [`00bfd568`](#insn-00bfd568) 範囲 `[['00bfd568', '00bfd583']]`
  - `CONDITIONAL_JUMP` [`00bfd580`](#insn-00bfd580) → [`00bfd5bc`](#insn-00bfd5bc)
  - `FALL_THROUGH` [`00bfd580`](#insn-00bfd580) → [`00bfd584`](#insn-00bfd584)
- ブロック [`00bfd584`](#insn-00bfd584) 範囲 `[['00bfd584', '00bfd58f']]`
  - `CONDITIONAL_JUMP` [`00bfd58c`](#insn-00bfd58c) → [`00bfd4f8`](#insn-00bfd4f8)
  - `FALL_THROUGH` [`00bfd58c`](#insn-00bfd58c) → [`00bfd590`](#insn-00bfd590)
- ブロック [`00bfd590`](#insn-00bfd590) 範囲 `[['00bfd590', '00bfd59b']]`
  - `UNCONDITIONAL_JUMP` [`00bfd598`](#insn-00bfd598) → [`00bfd4f8`](#insn-00bfd4f8)
- ブロック [`00bfd59c`](#insn-00bfd59c) 範囲 `[['00bfd59c', '00bfd5ab']]`
  - `UNCONDITIONAL_JUMP` [`00bfd5a8`](#insn-00bfd5a8) → [`00bfd518`](#insn-00bfd518)
- ブロック [`00bfd5ac`](#insn-00bfd5ac) 範囲 `[['00bfd5ac', '00bfd5b3']]`
  - `UNCONDITIONAL_JUMP` [`00bfd5b0`](#insn-00bfd5b0) → [`00bfd5d0`](#insn-00bfd5d0)
- ブロック [`00bfd5b4`](#insn-00bfd5b4) 範囲 `[['00bfd5b4', '00bfd5bb']]`
  - `UNCONDITIONAL_JUMP` [`00bfd5b8`](#insn-00bfd5b8) → [`00bfd5c0`](#insn-00bfd5c0)
- ブロック [`00bfd5bc`](#insn-00bfd5bc) 範囲 `[['00bfd5bc', '00bfd5bf']]`
  - `FALL_THROUGH` [`00bfd5bc`](#insn-00bfd5bc) → [`00bfd5c0`](#insn-00bfd5c0)
- ブロック [`00bfd5c0`](#insn-00bfd5c0) 範囲 `[['00bfd5c0', '00bfd5cf']]`
  - `FALL_THROUGH` [`00bfd5cc`](#insn-00bfd5cc) → [`00bfd5d0`](#insn-00bfd5d0)
- ブロック [`00bfd5d0`](#insn-00bfd5d0) 範囲 `[['00bfd5d0', '00bfd5e7']]`
  - `FALL_THROUGH` [`00bfd5e4`](#insn-00bfd5e4) → [`00bfd5e8`](#insn-00bfd5e8)
- ブロック [`00bfd5e8`](#insn-00bfd5e8) 範囲 `[['00bfd5e8', '00bfd603']]`

## 命令位置別の参照

- [`00bfd4b4`](#insn-00bfd4b4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4b8`](#insn-00bfd4b8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4bc`](#insn-00bfd4bc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4dc`](#insn-00bfd4dc) → [`00c5ae70`](../00c5a/00c5ae70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae70` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4e0`](#insn-00bfd4e0) → `Stack[-0x34]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4e4`](#insn-00bfd4e4) → [`00bfd5e8`](#insn-00bfd5e8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4e8`](#insn-00bfd4e8) → [`00bfd5ac`](#insn-00bfd5ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4f4`](#insn-00bfd4f4) → [`00bfd518`](#insn-00bfd518) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd50c`](#insn-00bfd50c) → [`00bfd59c`](#insn-00bfd59c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd52c`](#insn-00bfd52c) → [`00bfd538`](#insn-00bfd538) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd534`](#insn-00bfd534) → [`00bfd54c`](#insn-00bfd54c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd548`](#insn-00bfd548) → [`00bfd5b4`](#insn-00bfd5b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd554`](#insn-00bfd554) → [`00bfd568`](#insn-00bfd568) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd564`](#insn-00bfd564) → [`00bfd584`](#insn-00bfd584) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd580`](#insn-00bfd580) → [`00bfd5bc`](#insn-00bfd5bc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd58c`](#insn-00bfd58c) → [`00bfd4f8`](#insn-00bfd4f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd598`](#insn-00bfd598) → [`00bfd4f8`](#insn-00bfd4f8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd5a8`](#insn-00bfd5a8) → [`00bfd518`](#insn-00bfd518) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd5b0`](#insn-00bfd5b0) → [`00bfd5d0`](#insn-00bfd5d0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd5b8`](#insn-00bfd5b8) → [`00bfd5c0`](#insn-00bfd5c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd5e4`](#insn-00bfd5e4) → [`00c59340`](../00c59/00c59340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59340` · 推定シンボル `None` · 推定型 `None`
- [`00bfd5ec`](#insn-00bfd5ec) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd5f0`](#insn-00bfd5f0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd5f4`](#insn-00bfd5f4) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfd4b4`](#insn-00bfd4b4)

~~~json
{
  "source": "00bfd4b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4b8`](#insn-00bfd4b8)

~~~json
{
  "source": "00bfd4b8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4bc`](#insn-00bfd4bc)

~~~json
{
  "source": "00bfd4bc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4dc`](#insn-00bfd4dc)

~~~json
{
  "source": "00bfd4dc",
  "target": "00c5ae70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfd4e0`](#insn-00bfd4e0)

~~~json
{
  "source": "00bfd4e0",
  "target": "Stack[-0x34]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4e4`](#insn-00bfd4e4)

~~~json
{
  "source": "00bfd4e4",
  "target": "00bfd5e8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4e8`](#insn-00bfd4e8)

~~~json
{
  "source": "00bfd4e8",
  "target": "00bfd5ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4f4`](#insn-00bfd4f4)

~~~json
{
  "source": "00bfd4f4",
  "target": "00bfd518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd50c`](#insn-00bfd50c)

~~~json
{
  "source": "00bfd50c",
  "target": "00bfd59c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd52c`](#insn-00bfd52c)

~~~json
{
  "source": "00bfd52c",
  "target": "00bfd538",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd534`](#insn-00bfd534)

~~~json
{
  "source": "00bfd534",
  "target": "00bfd54c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd548`](#insn-00bfd548)

~~~json
{
  "source": "00bfd548",
  "target": "00bfd5b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd554`](#insn-00bfd554)

~~~json
{
  "source": "00bfd554",
  "target": "00bfd568",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd564`](#insn-00bfd564)

~~~json
{
  "source": "00bfd564",
  "target": "00bfd584",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd580`](#insn-00bfd580)

~~~json
{
  "source": "00bfd580",
  "target": "00bfd5bc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd58c`](#insn-00bfd58c)

~~~json
{
  "source": "00bfd58c",
  "target": "00bfd4f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd598`](#insn-00bfd598)

~~~json
{
  "source": "00bfd598",
  "target": "00bfd4f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd5a8`](#insn-00bfd5a8)

~~~json
{
  "source": "00bfd5a8",
  "target": "00bfd518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd5b0`](#insn-00bfd5b0)

~~~json
{
  "source": "00bfd5b0",
  "target": "00bfd5d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd5b8`](#insn-00bfd5b8)

~~~json
{
  "source": "00bfd5b8",
  "target": "00bfd5c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd5e4`](#insn-00bfd5e4)

~~~json
{
  "source": "00bfd5e4",
  "target": "00c59340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfd5ec`](#insn-00bfd5ec)

~~~json
{
  "source": "00bfd5ec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd5f0`](#insn-00bfd5f0)

~~~json
{
  "source": "00bfd5f0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd5f4`](#insn-00bfd5f4)

~~~json
{
  "source": "00bfd5f4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
