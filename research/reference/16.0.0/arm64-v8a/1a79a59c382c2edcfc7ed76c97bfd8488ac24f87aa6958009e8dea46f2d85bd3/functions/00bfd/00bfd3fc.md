# 00bfd3fc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b809b4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b80/00b809b4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-aa634ddd950b1823e603b7b4edf0e6b5)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfd824`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfd/00bfd824.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0041.md#compare-42b6a1d443cc482fe59aff22afdc6a59)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfd3fc",
  "name": "_ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPclc",
  "size": 380,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2edb679b7653a143fe2ae43518559ed7341d4fcca6977818184e20af9c35bb57",
  "source_text_sha256": "2edb679b7653a143fe2ae43518559ed7341d4fcca6977818184e20af9c35bb57",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfd3fc",
        "00bfd577"
      ]
    ],
    "bytes_sha256": "1b9d3b7edca0c0105dbd46e2a3fcb5e47b4f1fc6c51f9ce65d7123e5877fe50a",
    "instruction_count": 95,
    "instruction_bytes": 380,
    "body_bytes": 380,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5df70](../00c5d/00c5df70.md)

## 呼び出し先

- [00c57ea0](../00c57/00c57ea0.md)
- [00c599d0](../00c59/00c599d0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2139 bytes

~~~c

long * _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE3getEPclc
                 (long *param_1,undefined1 *param_2,long param_3,uint param_4)

{
  long lVar1;
  uint uVar2;
  long *plVar3;
  uint uVar4;
  long lVar5;
  undefined1 *puVar6;
  char local_44 [4];
  
  param_1[1] = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_44,param_1,1);
  if (local_44[0] != '\0') {
    lVar1 = param_3 + -1;
    if (param_3 < 1) {
      uVar2 = 4;
    }
    else {
      lVar5 = param_1[1];
      if (lVar5 < lVar1) {
        do {
          while( true ) {
            plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
            if ((byte *)plVar3[3] == (byte *)plVar3[4]) {
              uVar2 = (**(code **)(*plVar3 + 0x48))();
              if (uVar2 == 0xffffffff) {
                uVar4 = 2;
                goto LAB_00bfd508;
              }
            }
            else {
              uVar2 = (uint)*(byte *)plVar3[3];
            }
            puVar6 = param_2;
            if ((uVar2 & 0xff) == (param_4 & 0xff)) goto LAB_00bfd504;
            puVar6 = param_2 + 1;
            *param_2 = (char)uVar2;
            lVar5 = 0x7fffffffffffffff;
            if (param_1[1] != 0x7fffffffffffffff) {
              lVar5 = param_1[1] + 1;
              param_1[1] = lVar5;
            }
            plVar3 = *(long **)((long)param_1 + *(long *)(*param_1 + -0x18) + 0x28);
            param_2 = puVar6;
            if (plVar3[3] == plVar3[4]) break;
            plVar3[3] = plVar3[3] + 1;
            if (lVar1 <= lVar5) goto LAB_00bfd504;
          }
          (**(code **)(*plVar3 + 0x50))();
        } while (param_1[1] < lVar1);
LAB_00bfd504:
        uVar4 = 0;
        param_2 = puVar6;
LAB_00bfd508:
        lVar5 = param_1[1];
      }
      else {
        uVar4 = 0;
      }
      uVar2 = uVar4 | 4;
      if (lVar5 != 0) {
        uVar2 = uVar4;
      }
      *param_2 = 0;
    }
    lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
    _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | uVar2);
  }
  if (0 < param_3) {
    *param_2 = 0;
  }
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfd3fc"></a> `00bfd3fc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfd400"></a> `00bfd400` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bfd404"></a> `00bfd404` | `fd 7b 01 a9` | stp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfd408"></a> `00bfd408` | `f8 5f 02 a9` | stp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfd40c"></a> `00bfd40c` | `f6 57 03 a9` | stp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfd410"></a> `00bfd410` | `f4 4f 04 a9` | stp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfd414"></a> `00bfd414` | `fd 43 00 91` | add x29,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfd418"></a> `00bfd418` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfd41c"></a> `00bfd41c` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bfd420"></a> `00bfd420` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bfd424"></a> `00bfd424` | `1f 04 00 f9` | str xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd428"></a> `00bfd428` | `a0 13 00 d1` | sub x0,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfd42c"></a> `00bfd42c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfd430"></a> `00bfd430` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd434"></a> `00bfd434` | `f6 03 03 2a` | mov w22,w3 | `FALL_THROUGH`
<a id="insn-00bfd438"></a> `00bfd438` | `66 71 01 94` | bl 0x00c599d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfd43c"></a> `00bfd43c` | `a8 c3 5f 38` | ldurb w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfd440"></a> `00bfd440` | `28 08 00 34` | cbz w8,0x00bfd544 | `CONDITIONAL_JUMP`
<a id="insn-00bfd444"></a> `00bfd444` | `b7 06 00 f1` | subs x23,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd448"></a> `00bfd448` | `4b 06 00 54` | b.lt 0x00bfd510 | `CONDITIONAL_JUMP`
<a id="insn-00bfd44c"></a> `00bfd44c` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd450"></a> `00bfd450` | `3f 01 17 eb` | cmp x9,x23 | `FALL_THROUGH`
<a id="insn-00bfd454"></a> `00bfd454` | `2a 06 00 54` | b.ge 0x00bfd518 | `CONDITIONAL_JUMP`
<a id="insn-00bfd458"></a> `00bfd458` | `d6 1e 00 12` | and w22,w22,#0xff | `FALL_THROUGH`
<a id="insn-00bfd45c"></a> `00bfd45c` | `98 a2 00 91` | add x24,x20,#0x28 | `FALL_THROUGH`
<a id="insn-00bfd460"></a> `00bfd460` | `0b 00 00 14` | b 0x00bfd48c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd464"></a> `00bfd464` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bfd468"></a> `00bfd468` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfd46c"></a> `00bfd46c` | `00 6b 69 f8` | ldr x0,[x24, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfd470"></a> `00bfd470` | `09 a8 41 a9` | ldp x9,x10,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfd474"></a> `00bfd474` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-00bfd478"></a> `00bfd478` | `a0 03 00 54` | b.eq 0x00bfd4ec | `CONDITIONAL_JUMP`
<a id="insn-00bfd47c"></a> `00bfd47c` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd480"></a> `00bfd480` | `09 0c 00 f9` | str x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfd484"></a> `00bfd484` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00bfd488"></a> `00bfd488` | `ea 03 00 54` | b.ge 0x00bfd504 | `CONDITIONAL_JUMP`
<a id="insn-00bfd48c"></a> `00bfd48c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfd490"></a> `00bfd490` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfd494"></a> `00bfd494` | `00 6b 68 f8` | ldr x0,[x24, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfd498"></a> `00bfd498` | `08 a4 41 a9` | ldp x8,x9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-00bfd49c"></a> `00bfd49c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfd4a0"></a> `00bfd4a0` | `60 00 00 54` | b.eq 0x00bfd4ac | `CONDITIONAL_JUMP`
<a id="insn-00bfd4a4"></a> `00bfd4a4` | `00 01 40 39` | ldrb w0,[x8] | `FALL_THROUGH`
<a id="insn-00bfd4a8"></a> `00bfd4a8` | `06 00 00 14` | b 0x00bfd4c0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd4ac"></a> `00bfd4ac` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfd4b0"></a> `00bfd4b0` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfd4b4"></a> `00bfd4b4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfd4b8"></a> `00bfd4b8` | `1f 04 00 31` | cmn w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd4bc"></a> `00bfd4bc` | `a0 05 00 54` | b.eq 0x00bfd570 | `CONDITIONAL_JUMP`
<a id="insn-00bfd4c0"></a> `00bfd4c0` | `08 1c 00 12` | and w8,w0,#0xff | `FALL_THROUGH`
<a id="insn-00bfd4c4"></a> `00bfd4c4` | `1f 01 16 6b` | cmp w8,w22 | `FALL_THROUGH`
<a id="insn-00bfd4c8"></a> `00bfd4c8` | `e0 01 00 54` | b.eq 0x00bfd504 | `CONDITIONAL_JUMP`
<a id="insn-00bfd4cc"></a> `00bfd4cc` | `68 16 00 38` | strb w8,[x19], #0x1 | `FALL_THROUGH`
<a id="insn-00bfd4d0"></a> `00bfd4d0` | `08 00 f0 92` | mov x8,#0x7fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfd4d4"></a> `00bfd4d4` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd4d8"></a> `00bfd4d8` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfd4dc"></a> `00bfd4dc` | `40 fc ff 54` | b.eq 0x00bfd464 | `CONDITIONAL_JUMP`
<a id="insn-00bfd4e0"></a> `00bfd4e0` | `28 05 00 91` | add x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd4e4"></a> `00bfd4e4` | `88 06 00 f9` | str x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd4e8"></a> `00bfd4e8` | `df ff ff 17` | b 0x00bfd464 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd4ec"></a> `00bfd4ec` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfd4f0"></a> `00bfd4f0` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00bfd4f4"></a> `00bfd4f4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfd4f8"></a> `00bfd4f8` | `88 06 40 f9` | ldr x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd4fc"></a> `00bfd4fc` | `1f 01 17 eb` | cmp x8,x23 | `FALL_THROUGH`
<a id="insn-00bfd500"></a> `00bfd500` | `6b fc ff 54` | b.lt 0x00bfd48c | `CONDITIONAL_JUMP`
<a id="insn-00bfd504"></a> `00bfd504` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfd508"></a> `00bfd508` | `89 06 40 f9` | ldr x9,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00bfd50c"></a> `00bfd50c` | `04 00 00 14` | b 0x00bfd51c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd510"></a> `00bfd510` | `88 00 80 52` | mov w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfd514"></a> `00bfd514` | `06 00 00 14` | b 0x00bfd52c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfd518"></a> `00bfd518` | `e8 03 1f 2a` | mov w8,wzr | `FALL_THROUGH`
<a id="insn-00bfd51c"></a> `00bfd51c` | `0a 01 1e 32` | orr w10,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfd520"></a> `00bfd520` | `3f 01 00 f1` | cmp x9,#0x0 | `FALL_THROUGH`
<a id="insn-00bfd524"></a> `00bfd524` | `48 01 88 1a` | csel w8,w10,w8,eq | `FALL_THROUGH`
<a id="insn-00bfd528"></a> `00bfd528` | `7f 02 00 39` | strb wzr,[x19] | `FALL_THROUGH`
<a id="insn-00bfd52c"></a> `00bfd52c` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00bfd530"></a> `00bfd530` | `29 81 5e f8` | ldur x9,[x9, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfd534"></a> `00bfd534` | `80 02 09 8b` | add x0,x20,x9 | `FALL_THROUGH`
<a id="insn-00bfd538"></a> `00bfd538` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfd53c"></a> `00bfd53c` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfd540"></a> `00bfd540` | `58 6a 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfd544"></a> `00bfd544` | `bf 06 00 f1` | cmp x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfd548"></a> `00bfd548` | `4b 00 00 54` | b.lt 0x00bfd550 | `CONDITIONAL_JUMP`
<a id="insn-00bfd54c"></a> `00bfd54c` | `7f 02 00 39` | strb wzr,[x19] | `FALL_THROUGH`
<a id="insn-00bfd550"></a> `00bfd550` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfd554"></a> `00bfd554` | `f4 4f 44 a9` | ldp x20,x19,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfd558"></a> `00bfd558` | `f6 57 43 a9` | ldp x22,x21,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfd55c"></a> `00bfd55c` | `f8 5f 42 a9` | ldp x24,x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfd560"></a> `00bfd560` | `fd 7b 41 a9` | ldp x29,x30,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfd564"></a> `00bfd564` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bfd568"></a> `00bfd568` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfd56c"></a> `00bfd56c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfd570"></a> `00bfd570` | `48 00 80 52` | mov w8,#0x2 | `FALL_THROUGH`
<a id="insn-00bfd574"></a> `00bfd574` | `e5 ff ff 17` | b 0x00bfd508 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bfd3fc`](#insn-00bfd3fc) 範囲 `[['00bfd3fc', '00bfd443']]`
  - `CONDITIONAL_JUMP` [`00bfd440`](#insn-00bfd440) → [`00bfd544`](#insn-00bfd544)
  - `FALL_THROUGH` [`00bfd440`](#insn-00bfd440) → [`00bfd444`](#insn-00bfd444)
- ブロック [`00bfd444`](#insn-00bfd444) 範囲 `[['00bfd444', '00bfd44b']]`
  - `CONDITIONAL_JUMP` [`00bfd448`](#insn-00bfd448) → [`00bfd510`](#insn-00bfd510)
  - `FALL_THROUGH` [`00bfd448`](#insn-00bfd448) → [`00bfd44c`](#insn-00bfd44c)
- ブロック [`00bfd44c`](#insn-00bfd44c) 範囲 `[['00bfd44c', '00bfd457']]`
  - `CONDITIONAL_JUMP` [`00bfd454`](#insn-00bfd454) → [`00bfd518`](#insn-00bfd518)
  - `FALL_THROUGH` [`00bfd454`](#insn-00bfd454) → [`00bfd458`](#insn-00bfd458)
- ブロック [`00bfd458`](#insn-00bfd458) 範囲 `[['00bfd458', '00bfd463']]`
  - `UNCONDITIONAL_JUMP` [`00bfd460`](#insn-00bfd460) → [`00bfd48c`](#insn-00bfd48c)
- ブロック [`00bfd464`](#insn-00bfd464) 範囲 `[['00bfd464', '00bfd47b']]`
  - `CONDITIONAL_JUMP` [`00bfd478`](#insn-00bfd478) → [`00bfd4ec`](#insn-00bfd4ec)
  - `FALL_THROUGH` [`00bfd478`](#insn-00bfd478) → [`00bfd47c`](#insn-00bfd47c)
- ブロック [`00bfd47c`](#insn-00bfd47c) 範囲 `[['00bfd47c', '00bfd48b']]`
  - `CONDITIONAL_JUMP` [`00bfd488`](#insn-00bfd488) → [`00bfd504`](#insn-00bfd504)
  - `FALL_THROUGH` [`00bfd488`](#insn-00bfd488) → [`00bfd48c`](#insn-00bfd48c)
- ブロック [`00bfd48c`](#insn-00bfd48c) 範囲 `[['00bfd48c', '00bfd4a3']]`
  - `CONDITIONAL_JUMP` [`00bfd4a0`](#insn-00bfd4a0) → [`00bfd4ac`](#insn-00bfd4ac)
  - `FALL_THROUGH` [`00bfd4a0`](#insn-00bfd4a0) → [`00bfd4a4`](#insn-00bfd4a4)
- ブロック [`00bfd4a4`](#insn-00bfd4a4) 範囲 `[['00bfd4a4', '00bfd4ab']]`
  - `UNCONDITIONAL_JUMP` [`00bfd4a8`](#insn-00bfd4a8) → [`00bfd4c0`](#insn-00bfd4c0)
- ブロック [`00bfd4ac`](#insn-00bfd4ac) 範囲 `[['00bfd4ac', '00bfd4bf']]`
  - `CONDITIONAL_JUMP` [`00bfd4bc`](#insn-00bfd4bc) → [`00bfd570`](#insn-00bfd570)
  - `FALL_THROUGH` [`00bfd4bc`](#insn-00bfd4bc) → [`00bfd4c0`](#insn-00bfd4c0)
- ブロック [`00bfd4c0`](#insn-00bfd4c0) 範囲 `[['00bfd4c0', '00bfd4cb']]`
  - `CONDITIONAL_JUMP` [`00bfd4c8`](#insn-00bfd4c8) → [`00bfd504`](#insn-00bfd504)
  - `FALL_THROUGH` [`00bfd4c8`](#insn-00bfd4c8) → [`00bfd4cc`](#insn-00bfd4cc)
- ブロック [`00bfd4cc`](#insn-00bfd4cc) 範囲 `[['00bfd4cc', '00bfd4df']]`
  - `CONDITIONAL_JUMP` [`00bfd4dc`](#insn-00bfd4dc) → [`00bfd464`](#insn-00bfd464)
  - `FALL_THROUGH` [`00bfd4dc`](#insn-00bfd4dc) → [`00bfd4e0`](#insn-00bfd4e0)
- ブロック [`00bfd4e0`](#insn-00bfd4e0) 範囲 `[['00bfd4e0', '00bfd4eb']]`
  - `UNCONDITIONAL_JUMP` [`00bfd4e8`](#insn-00bfd4e8) → [`00bfd464`](#insn-00bfd464)
- ブロック [`00bfd4ec`](#insn-00bfd4ec) 範囲 `[['00bfd4ec', '00bfd503']]`
  - `CONDITIONAL_JUMP` [`00bfd500`](#insn-00bfd500) → [`00bfd48c`](#insn-00bfd48c)
  - `FALL_THROUGH` [`00bfd500`](#insn-00bfd500) → [`00bfd504`](#insn-00bfd504)
- ブロック [`00bfd504`](#insn-00bfd504) 範囲 `[['00bfd504', '00bfd507']]`
  - `FALL_THROUGH` [`00bfd504`](#insn-00bfd504) → [`00bfd508`](#insn-00bfd508)
- ブロック [`00bfd508`](#insn-00bfd508) 範囲 `[['00bfd508', '00bfd50f']]`
  - `UNCONDITIONAL_JUMP` [`00bfd50c`](#insn-00bfd50c) → [`00bfd51c`](#insn-00bfd51c)
- ブロック [`00bfd510`](#insn-00bfd510) 範囲 `[['00bfd510', '00bfd517']]`
  - `UNCONDITIONAL_JUMP` [`00bfd514`](#insn-00bfd514) → [`00bfd52c`](#insn-00bfd52c)
- ブロック [`00bfd518`](#insn-00bfd518) 範囲 `[['00bfd518', '00bfd51b']]`
  - `FALL_THROUGH` [`00bfd518`](#insn-00bfd518) → [`00bfd51c`](#insn-00bfd51c)
- ブロック [`00bfd51c`](#insn-00bfd51c) 範囲 `[['00bfd51c', '00bfd52b']]`
  - `FALL_THROUGH` [`00bfd528`](#insn-00bfd528) → [`00bfd52c`](#insn-00bfd52c)
- ブロック [`00bfd52c`](#insn-00bfd52c) 範囲 `[['00bfd52c', '00bfd543']]`
  - `FALL_THROUGH` [`00bfd540`](#insn-00bfd540) → [`00bfd544`](#insn-00bfd544)
- ブロック [`00bfd544`](#insn-00bfd544) 範囲 `[['00bfd544', '00bfd54b']]`
  - `CONDITIONAL_JUMP` [`00bfd548`](#insn-00bfd548) → [`00bfd550`](#insn-00bfd550)
  - `FALL_THROUGH` [`00bfd548`](#insn-00bfd548) → [`00bfd54c`](#insn-00bfd54c)
- ブロック [`00bfd54c`](#insn-00bfd54c) 範囲 `[['00bfd54c', '00bfd54f']]`
  - `FALL_THROUGH` [`00bfd54c`](#insn-00bfd54c) → [`00bfd550`](#insn-00bfd550)
- ブロック [`00bfd550`](#insn-00bfd550) 範囲 `[['00bfd550', '00bfd56f']]`
- ブロック [`00bfd570`](#insn-00bfd570) 範囲 `[['00bfd570', '00bfd577']]`
  - `UNCONDITIONAL_JUMP` [`00bfd574`](#insn-00bfd574) → [`00bfd508`](#insn-00bfd508)

## 命令位置別の参照

- [`00bfd404`](#insn-00bfd404) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd408`](#insn-00bfd408) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd40c`](#insn-00bfd40c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd410`](#insn-00bfd410) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd438`](#insn-00bfd438) → [`00c599d0`](../00c59/00c599d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c599d0` · 推定シンボル `None` · 推定型 `None`
- [`00bfd43c`](#insn-00bfd43c) → `Stack[-0x44]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd440`](#insn-00bfd440) → [`00bfd544`](#insn-00bfd544) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd448`](#insn-00bfd448) → [`00bfd510`](#insn-00bfd510) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd454`](#insn-00bfd454) → [`00bfd518`](#insn-00bfd518) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd460`](#insn-00bfd460) → [`00bfd48c`](#insn-00bfd48c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd478`](#insn-00bfd478) → [`00bfd4ec`](#insn-00bfd4ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd488`](#insn-00bfd488) → [`00bfd504`](#insn-00bfd504) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4a0`](#insn-00bfd4a0) → [`00bfd4ac`](#insn-00bfd4ac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4a8`](#insn-00bfd4a8) → [`00bfd4c0`](#insn-00bfd4c0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4bc`](#insn-00bfd4bc) → [`00bfd570`](#insn-00bfd570) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4c8`](#insn-00bfd4c8) → [`00bfd504`](#insn-00bfd504) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4dc`](#insn-00bfd4dc) → [`00bfd464`](#insn-00bfd464) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd4e8`](#insn-00bfd4e8) → [`00bfd464`](#insn-00bfd464) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd500`](#insn-00bfd500) → [`00bfd48c`](#insn-00bfd48c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd50c`](#insn-00bfd50c) → [`00bfd51c`](#insn-00bfd51c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd514`](#insn-00bfd514) → [`00bfd52c`](#insn-00bfd52c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd540`](#insn-00bfd540) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfd548`](#insn-00bfd548) → [`00bfd550`](#insn-00bfd550) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd554`](#insn-00bfd554) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd558`](#insn-00bfd558) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd55c`](#insn-00bfd55c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd560`](#insn-00bfd560) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfd574`](#insn-00bfd574) → [`00bfd508`](#insn-00bfd508) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfd404`](#insn-00bfd404)

~~~json
{
  "source": "00bfd404",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd408`](#insn-00bfd408)

~~~json
{
  "source": "00bfd408",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd40c`](#insn-00bfd40c)

~~~json
{
  "source": "00bfd40c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd410`](#insn-00bfd410)

~~~json
{
  "source": "00bfd410",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd438`](#insn-00bfd438)

~~~json
{
  "source": "00bfd438",
  "target": "00c599d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfd43c`](#insn-00bfd43c)

~~~json
{
  "source": "00bfd43c",
  "target": "Stack[-0x44]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd440`](#insn-00bfd440)

~~~json
{
  "source": "00bfd440",
  "target": "00bfd544",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd448`](#insn-00bfd448)

~~~json
{
  "source": "00bfd448",
  "target": "00bfd510",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd454`](#insn-00bfd454)

~~~json
{
  "source": "00bfd454",
  "target": "00bfd518",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd460`](#insn-00bfd460)

~~~json
{
  "source": "00bfd460",
  "target": "00bfd48c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd478`](#insn-00bfd478)

~~~json
{
  "source": "00bfd478",
  "target": "00bfd4ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd488`](#insn-00bfd488)

~~~json
{
  "source": "00bfd488",
  "target": "00bfd504",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4a0`](#insn-00bfd4a0)

~~~json
{
  "source": "00bfd4a0",
  "target": "00bfd4ac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4a8`](#insn-00bfd4a8)

~~~json
{
  "source": "00bfd4a8",
  "target": "00bfd4c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4bc`](#insn-00bfd4bc)

~~~json
{
  "source": "00bfd4bc",
  "target": "00bfd570",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4c8`](#insn-00bfd4c8)

~~~json
{
  "source": "00bfd4c8",
  "target": "00bfd504",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4dc`](#insn-00bfd4dc)

~~~json
{
  "source": "00bfd4dc",
  "target": "00bfd464",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd4e8`](#insn-00bfd4e8)

~~~json
{
  "source": "00bfd4e8",
  "target": "00bfd464",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd500`](#insn-00bfd500)

~~~json
{
  "source": "00bfd500",
  "target": "00bfd48c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd50c`](#insn-00bfd50c)

~~~json
{
  "source": "00bfd50c",
  "target": "00bfd51c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd514`](#insn-00bfd514)

~~~json
{
  "source": "00bfd514",
  "target": "00bfd52c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd540`](#insn-00bfd540)

~~~json
{
  "source": "00bfd540",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfd548`](#insn-00bfd548)

~~~json
{
  "source": "00bfd548",
  "target": "00bfd550",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd554`](#insn-00bfd554)

~~~json
{
  "source": "00bfd554",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd558`](#insn-00bfd558)

~~~json
{
  "source": "00bfd558",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd55c`](#insn-00bfd55c)

~~~json
{
  "source": "00bfd55c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd560`](#insn-00bfd560)

~~~json
{
  "source": "00bfd560",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfd574`](#insn-00bfd574)

~~~json
{
  "source": "00bfd574",
  "target": "00bfd508",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
