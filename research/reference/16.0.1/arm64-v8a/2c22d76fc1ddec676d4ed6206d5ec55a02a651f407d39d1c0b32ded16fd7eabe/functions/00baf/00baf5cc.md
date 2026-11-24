# 00baf5cc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00baf1a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00baf/00baf1a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0038.md#compare-4073deac5b9db64f6c44b84856ae1d6d)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00baf668`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00baf/00baf668.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0038.md#compare-785942314583bd29095077d28595eb52)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00baf5cc",
  "name": "_ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a601f1da93f9ab88491b541bb4df674b2b3cd091ef8639ac372f5926caec8a93",
  "source_text_sha256": "a601f1da93f9ab88491b541bb4df674b2b3cd091ef8639ac372f5926caec8a93",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00baf5cc",
        "00baf727"
      ]
    ],
    "bytes_sha256": "fa1e88cd30667c55020cd0f99cbc15426ee4250b8d1a8c2107fc2b603c71a2a9",
    "instruction_count": 87,
    "instruction_bytes": 348,
    "body_bytes": 348,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [00c5cbf0](../00c5c/00c5cbf0.md)

## 呼び出し先

解決済みの記録なし。

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2862 bytes

~~~c

void _ZNSt6__ndk118__insertion_sort_3IRPFbPKN11flatbuffers8FieldDefES4_EPPS2_EEvT0_SA_T_
               (undefined1 (*param_1) [16],undefined1 (*param_2) [16],undefined8 *param_3)

{
  long lVar1;
  ulong uVar2;
  ulong uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined1 (*pauVar6) [16];
  undefined1 (*pauVar7) [16];
  undefined1 (*pauVar8) [16];
  long lVar9;
  long lVar10;
  undefined1 auVar11 [16];
  undefined1 auVar12 [16];
  
  uVar2 = (*(code *)*param_3)(*(undefined8 *)(*param_1 + 8),*(undefined8 *)*param_1);
  uVar3 = (*(code *)*param_3)(*(undefined8 *)param_1[1],*(undefined8 *)(*param_1 + 8));
  if ((uVar2 & 1) == 0) {
    if ((uVar3 & 1) != 0) {
      auVar11 = *(undefined1 (*) [16])(*param_1 + 8);
      uVar4 = *(undefined8 *)*param_1;
      auVar12 = NEON_ext(auVar11,auVar11,8,1);
      *(long *)param_1[1] = auVar12._8_8_;
      *(long *)(*param_1 + 8) = auVar12._0_8_;
      uVar2 = (*(code *)*param_3)(auVar11._8_8_,uVar4);
      if ((uVar2 & 1) != 0) {
        auVar11 = NEON_ext(*param_1,*param_1,8,1);
        *(long *)(*param_1 + 8) = auVar11._8_8_;
        *(long *)*param_1 = auVar11._0_8_;
      }
    }
  }
  else {
    uVar4 = *(undefined8 *)*param_1;
    if ((uVar3 & 1) == 0) {
      uVar5 = *(undefined8 *)param_1[1];
      *(undefined8 *)*param_1 = *(undefined8 *)(*param_1 + 8);
      *(undefined8 *)(*param_1 + 8) = uVar4;
      uVar2 = (*(code *)*param_3)(uVar5);
      if ((uVar2 & 1) != 0) {
        auVar11 = NEON_ext(*(undefined1 (*) [16])(*param_1 + 8),*(undefined1 (*) [16])(*param_1 + 8)
                           ,8,1);
        *(long *)param_1[1] = auVar11._8_8_;
        *(long *)(*param_1 + 8) = auVar11._0_8_;
      }
    }
    else {
      uVar5 = *(undefined8 *)param_1[1];
      *(undefined8 *)param_1[1] = uVar4;
      *(undefined8 *)*param_1 = uVar5;
    }
  }
  if ((undefined1 (*) [16])(param_1[1] + 8) != param_2) {
    lVar9 = 0;
    pauVar6 = (undefined1 (*) [16])(param_1[1] + 8);
    pauVar8 = param_1 + 1;
    do {
      pauVar7 = pauVar6;
      uVar2 = (*(code *)*param_3)(*(undefined8 *)*pauVar7,*(undefined8 *)*pauVar8);
      if ((uVar2 & 1) != 0) {
        uVar4 = *(undefined8 *)*pauVar7;
        lVar1 = lVar9;
        do {
          lVar10 = lVar1;
          *(undefined8 *)(param_1[1] + lVar10 + 8) = *(undefined8 *)(param_1[1] + lVar10);
          pauVar6 = param_1;
          if (lVar10 == -0x10) goto LAB_00baf6a4;
          uVar2 = (*(code *)*param_3)(uVar4,*(undefined8 *)(*param_1 + lVar10 + 8));
          lVar1 = lVar10 + -8;
        } while ((uVar2 & 1) != 0);
        pauVar6 = (undefined1 (*) [16])(param_1[1] + lVar10);
LAB_00baf6a4:
        *(undefined8 *)*pauVar6 = uVar4;
      }
      lVar9 = lVar9 + 8;
      pauVar6 = (undefined1 (*) [16])(*pauVar7 + 8);
      pauVar8 = pauVar7;
    } while ((undefined1 (*) [16])(*pauVar7 + 8) != param_2);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00baf5cc"></a> `00baf5cc` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00baf5d0"></a> `00baf5d0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf5d4"></a> `00baf5d4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baf5d8"></a> `00baf5d8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baf5dc"></a> `00baf5dc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baf5e0"></a> `00baf5e0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00baf5e4"></a> `00baf5e4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00baf5e8"></a> `00baf5e8` | `08 00 40 a9` | ldp x8,x0,[x0] | `FALL_THROUGH`
<a id="insn-00baf5ec"></a> `00baf5ec` | `49 00 40 f9` | ldr x9,[x2] | `FALL_THROUGH`
<a id="insn-00baf5f0"></a> `00baf5f0` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00baf5f4"></a> `00baf5f4` | `f3 03 02 aa` | mov x19,x2 | `FALL_THROUGH`
<a id="insn-00baf5f8"></a> `00baf5f8` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00baf5fc"></a> `00baf5fc` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00baf600"></a> `00baf600` | `f7 03 14 aa` | mov x23,x20 | `FALL_THROUGH`
<a id="insn-00baf604"></a> `00baf604` | `e8 0e 41 f8` | ldr x8,[x23, #0x10]! | `FALL_THROUGH`
<a id="insn-00baf608"></a> `00baf608` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00baf60c"></a> `00baf60c` | `81 06 40 f9` | ldr x1,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00baf610"></a> `00baf610` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00baf614"></a> `00baf614` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00baf618"></a> `00baf618` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00baf61c"></a> `00baf61c` | `f6 00 00 36` | tbz w22,#0x0,0x00baf638 | `CONDITIONAL_JUMP`
<a id="insn-00baf620"></a> `00baf620` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00baf624"></a> `00baf624` | `40 02 00 36` | tbz w0,#0x0,0x00baf66c | `CONDITIONAL_JUMP`
<a id="insn-00baf628"></a> `00baf628` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00baf62c"></a> `00baf62c` | `81 0a 00 f9` | str x1,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00baf630"></a> `00baf630` | `88 02 00 f9` | str x8,[x20] | `FALL_THROUGH`
<a id="insn-00baf634"></a> `00baf634` | `16 00 00 14` | b 0x00baf68c | `UNCONDITIONAL_JUMP`
<a id="insn-00baf638"></a> `00baf638` | `a0 02 00 36` | tbz w0,#0x0,0x00baf68c | `CONDITIONAL_JUMP`
<a id="insn-00baf63c"></a> `00baf63c` | `80 82 c0 3c` | ldur q0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00baf640"></a> `00baf640` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00baf644"></a> `00baf644` | `01 40 00 6e` | ext v1.16B,v0.16B,v0.16B,0x8 | `FALL_THROUGH`
<a id="insn-00baf648"></a> `00baf648` | `81 82 80 3c` | stur q1,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00baf64c"></a> `00baf64c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf650"></a> `00baf650` | `00 3c 18 4e` | mov x0,v0.D[0x1] | `FALL_THROUGH`
<a id="insn-00baf654"></a> `00baf654` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf658"></a> `00baf658` | `a0 01 00 36` | tbz w0,#0x0,0x00baf68c | `CONDITIONAL_JUMP`
<a id="insn-00baf65c"></a> `00baf65c` | `80 02 c0 3d` | ldr q0,[x20] | `FALL_THROUGH`
<a id="insn-00baf660"></a> `00baf660` | `00 40 00 6e` | ext v0.16B,v0.16B,v0.16B,0x8 | `FALL_THROUGH`
<a id="insn-00baf664"></a> `00baf664` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00baf668"></a> `00baf668` | `09 00 00 14` | b 0x00baf68c | `UNCONDITIONAL_JUMP`
<a id="insn-00baf66c"></a> `00baf66c` | `88 82 40 a9` | ldp x8,x0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00baf670"></a> `00baf670` | `88 06 00 a9` | stp x8,x1,[x20] | `FALL_THROUGH`
<a id="insn-00baf674"></a> `00baf674` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf678"></a> `00baf678` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf67c"></a> `00baf67c` | `80 00 00 36` | tbz w0,#0x0,0x00baf68c | `CONDITIONAL_JUMP`
<a id="insn-00baf680"></a> `00baf680` | `80 82 c0 3c` | ldur q0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00baf684"></a> `00baf684` | `00 40 00 6e` | ext v0.16B,v0.16B,v0.16B,0x8 | `FALL_THROUGH`
<a id="insn-00baf688"></a> `00baf688` | `80 82 80 3c` | stur q0,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00baf68c"></a> `00baf68c` | `88 62 00 91` | add x8,x20,#0x18 | `FALL_THROUGH`
<a id="insn-00baf690"></a> `00baf690` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00baf694"></a> `00baf694` | `e0 03 00 54` | b.eq 0x00baf710 | `CONDITIONAL_JUMP`
<a id="insn-00baf698"></a> `00baf698` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00baf69c"></a> `00baf69c` | `07 00 00 14` | b 0x00baf6b8 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf6a0"></a> `00baf6a0` | `e8 03 14 aa` | mov x8,x20 | `FALL_THROUGH`
<a id="insn-00baf6a4"></a> `00baf6a4` | `16 01 00 f9` | str x22,[x8] | `FALL_THROUGH`
<a id="insn-00baf6a8"></a> `00baf6a8` | `e8 22 00 91` | add x8,x23,#0x8 | `FALL_THROUGH`
<a id="insn-00baf6ac"></a> `00baf6ac` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00baf6b0"></a> `00baf6b0` | `18 23 00 91` | add x24,x24,#0x8 | `FALL_THROUGH`
<a id="insn-00baf6b4"></a> `00baf6b4` | `e0 02 00 54` | b.eq 0x00baf710 | `CONDITIONAL_JUMP`
<a id="insn-00baf6b8"></a> `00baf6b8` | `e1 02 40 f9` | ldr x1,[x23] | `FALL_THROUGH`
<a id="insn-00baf6bc"></a> `00baf6bc` | `f7 03 08 aa` | mov x23,x8 | `FALL_THROUGH`
<a id="insn-00baf6c0"></a> `00baf6c0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00baf6c4"></a> `00baf6c4` | `e0 02 40 f9` | ldr x0,[x23] | `FALL_THROUGH`
<a id="insn-00baf6c8"></a> `00baf6c8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00baf6cc"></a> `00baf6cc` | `e0 fe 07 36` | tbz w0,#0x0,0x00baf6a8 | `CONDITIONAL_JUMP`
<a id="insn-00baf6d0"></a> `00baf6d0` | `f6 02 40 f9` | ldr x22,[x23] | `FALL_THROUGH`
<a id="insn-00baf6d4"></a> `00baf6d4` | `f9 03 18 aa` | mov x25,x24 | `FALL_THROUGH`
<a id="insn-00baf6d8"></a> `00baf6d8` | `88 02 19 8b` | add x8,x20,x25 | `FALL_THROUGH`
<a id="insn-00baf6dc"></a> `00baf6dc` | `09 09 40 f9` | ldr x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00baf6e0"></a> `00baf6e0` | `3f 43 00 b1` | cmn x25,#0x10 | `FALL_THROUGH`
<a id="insn-00baf6e4"></a> `00baf6e4` | `09 0d 00 f9` | str x9,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00baf6e8"></a> `00baf6e8` | `c0 fd ff 54` | b.eq 0x00baf6a0 | `CONDITIONAL_JUMP`
<a id="insn-00baf6ec"></a> `00baf6ec` | `69 02 40 f9` | ldr x9,[x19] | `FALL_THROUGH`
<a id="insn-00baf6f0"></a> `00baf6f0` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00baf6f4"></a> `00baf6f4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00baf6f8"></a> `00baf6f8` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00baf6fc"></a> `00baf6fc` | `39 23 00 d1` | sub x25,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00baf700"></a> `00baf700` | `c0 fe 07 37` | tbnz w0,#0x0,0x00baf6d8 | `CONDITIONAL_JUMP`
<a id="insn-00baf704"></a> `00baf704` | `88 02 19 8b` | add x8,x20,x25 | `FALL_THROUGH`
<a id="insn-00baf708"></a> `00baf708` | `08 61 00 91` | add x8,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00baf70c"></a> `00baf70c` | `e6 ff ff 17` | b 0x00baf6a4 | `UNCONDITIONAL_JUMP`
<a id="insn-00baf710"></a> `00baf710` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00baf714"></a> `00baf714` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00baf718"></a> `00baf718` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00baf71c"></a> `00baf71c` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00baf720"></a> `00baf720` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00baf724"></a> `00baf724` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00baf5cc`](#insn-00baf5cc) 範囲 `[['00baf5cc', '00baf61f']]`
  - `CONDITIONAL_JUMP` [`00baf61c`](#insn-00baf61c) → [`00baf638`](#insn-00baf638)
  - `FALL_THROUGH` [`00baf61c`](#insn-00baf61c) → [`00baf620`](#insn-00baf620)
- ブロック [`00baf620`](#insn-00baf620) 範囲 `[['00baf620', '00baf627']]`
  - `CONDITIONAL_JUMP` [`00baf624`](#insn-00baf624) → [`00baf66c`](#insn-00baf66c)
  - `FALL_THROUGH` [`00baf624`](#insn-00baf624) → [`00baf628`](#insn-00baf628)
- ブロック [`00baf628`](#insn-00baf628) 範囲 `[['00baf628', '00baf637']]`
  - `UNCONDITIONAL_JUMP` [`00baf634`](#insn-00baf634) → [`00baf68c`](#insn-00baf68c)
- ブロック [`00baf638`](#insn-00baf638) 範囲 `[['00baf638', '00baf63b']]`
  - `CONDITIONAL_JUMP` [`00baf638`](#insn-00baf638) → [`00baf68c`](#insn-00baf68c)
  - `FALL_THROUGH` [`00baf638`](#insn-00baf638) → [`00baf63c`](#insn-00baf63c)
- ブロック [`00baf63c`](#insn-00baf63c) 範囲 `[['00baf63c', '00baf65b']]`
  - `CONDITIONAL_JUMP` [`00baf658`](#insn-00baf658) → [`00baf68c`](#insn-00baf68c)
  - `FALL_THROUGH` [`00baf658`](#insn-00baf658) → [`00baf65c`](#insn-00baf65c)
- ブロック [`00baf65c`](#insn-00baf65c) 範囲 `[['00baf65c', '00baf66b']]`
  - `UNCONDITIONAL_JUMP` [`00baf668`](#insn-00baf668) → [`00baf68c`](#insn-00baf68c)
- ブロック [`00baf66c`](#insn-00baf66c) 範囲 `[['00baf66c', '00baf67f']]`
  - `CONDITIONAL_JUMP` [`00baf67c`](#insn-00baf67c) → [`00baf68c`](#insn-00baf68c)
  - `FALL_THROUGH` [`00baf67c`](#insn-00baf67c) → [`00baf680`](#insn-00baf680)
- ブロック [`00baf680`](#insn-00baf680) 範囲 `[['00baf680', '00baf68b']]`
  - `FALL_THROUGH` [`00baf688`](#insn-00baf688) → [`00baf68c`](#insn-00baf68c)
- ブロック [`00baf68c`](#insn-00baf68c) 範囲 `[['00baf68c', '00baf697']]`
  - `CONDITIONAL_JUMP` [`00baf694`](#insn-00baf694) → [`00baf710`](#insn-00baf710)
  - `FALL_THROUGH` [`00baf694`](#insn-00baf694) → [`00baf698`](#insn-00baf698)
- ブロック [`00baf698`](#insn-00baf698) 範囲 `[['00baf698', '00baf69f']]`
  - `UNCONDITIONAL_JUMP` [`00baf69c`](#insn-00baf69c) → [`00baf6b8`](#insn-00baf6b8)
- ブロック [`00baf6a0`](#insn-00baf6a0) 範囲 `[['00baf6a0', '00baf6a3']]`
  - `FALL_THROUGH` [`00baf6a0`](#insn-00baf6a0) → [`00baf6a4`](#insn-00baf6a4)
- ブロック [`00baf6a4`](#insn-00baf6a4) 範囲 `[['00baf6a4', '00baf6a7']]`
  - `FALL_THROUGH` [`00baf6a4`](#insn-00baf6a4) → [`00baf6a8`](#insn-00baf6a8)
- ブロック [`00baf6a8`](#insn-00baf6a8) 範囲 `[['00baf6a8', '00baf6b7']]`
  - `CONDITIONAL_JUMP` [`00baf6b4`](#insn-00baf6b4) → [`00baf710`](#insn-00baf710)
  - `FALL_THROUGH` [`00baf6b4`](#insn-00baf6b4) → [`00baf6b8`](#insn-00baf6b8)
- ブロック [`00baf6b8`](#insn-00baf6b8) 範囲 `[['00baf6b8', '00baf6cf']]`
  - `CONDITIONAL_JUMP` [`00baf6cc`](#insn-00baf6cc) → [`00baf6a8`](#insn-00baf6a8)
  - `FALL_THROUGH` [`00baf6cc`](#insn-00baf6cc) → [`00baf6d0`](#insn-00baf6d0)
- ブロック [`00baf6d0`](#insn-00baf6d0) 範囲 `[['00baf6d0', '00baf6d7']]`
  - `FALL_THROUGH` [`00baf6d4`](#insn-00baf6d4) → [`00baf6d8`](#insn-00baf6d8)
- ブロック [`00baf6d8`](#insn-00baf6d8) 範囲 `[['00baf6d8', '00baf6eb']]`
  - `CONDITIONAL_JUMP` [`00baf6e8`](#insn-00baf6e8) → [`00baf6a0`](#insn-00baf6a0)
  - `FALL_THROUGH` [`00baf6e8`](#insn-00baf6e8) → [`00baf6ec`](#insn-00baf6ec)
- ブロック [`00baf6ec`](#insn-00baf6ec) 範囲 `[['00baf6ec', '00baf703']]`
  - `CONDITIONAL_JUMP` [`00baf700`](#insn-00baf700) → [`00baf6d8`](#insn-00baf6d8)
  - `FALL_THROUGH` [`00baf700`](#insn-00baf700) → [`00baf704`](#insn-00baf704)
- ブロック [`00baf704`](#insn-00baf704) 範囲 `[['00baf704', '00baf70f']]`
  - `UNCONDITIONAL_JUMP` [`00baf70c`](#insn-00baf70c) → [`00baf6a4`](#insn-00baf6a4)
- ブロック [`00baf710`](#insn-00baf710) 範囲 `[['00baf710', '00baf727']]`

## 命令位置別の参照

- [`00baf5cc`](#insn-00baf5cc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf5d0`](#insn-00baf5d0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf5d4`](#insn-00baf5d4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf5d8`](#insn-00baf5d8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf5dc`](#insn-00baf5dc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf61c`](#insn-00baf61c) → [`00baf638`](#insn-00baf638) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf624`](#insn-00baf624) → [`00baf66c`](#insn-00baf66c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf634`](#insn-00baf634) → [`00baf68c`](#insn-00baf68c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf638`](#insn-00baf638) → [`00baf68c`](#insn-00baf68c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf658`](#insn-00baf658) → [`00baf68c`](#insn-00baf68c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf668`](#insn-00baf668) → [`00baf68c`](#insn-00baf68c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf67c`](#insn-00baf67c) → [`00baf68c`](#insn-00baf68c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf694`](#insn-00baf694) → [`00baf710`](#insn-00baf710) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf69c`](#insn-00baf69c) → [`00baf6b8`](#insn-00baf6b8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf6b4`](#insn-00baf6b4) → [`00baf710`](#insn-00baf710) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf6cc`](#insn-00baf6cc) → [`00baf6a8`](#insn-00baf6a8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf6e8`](#insn-00baf6e8) → [`00baf6a0`](#insn-00baf6a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf700`](#insn-00baf700) → [`00baf6d8`](#insn-00baf6d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf70c`](#insn-00baf70c) → [`00baf6a4`](#insn-00baf6a4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf710`](#insn-00baf710) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf714`](#insn-00baf714) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf718`](#insn-00baf718) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00baf71c`](#insn-00baf71c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00baf5cc`](#insn-00baf5cc)

~~~json
{
  "source": "00baf5cc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf5d0`](#insn-00baf5d0)

~~~json
{
  "source": "00baf5d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf5d4`](#insn-00baf5d4)

~~~json
{
  "source": "00baf5d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf5d8`](#insn-00baf5d8)

~~~json
{
  "source": "00baf5d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf5dc`](#insn-00baf5dc)

~~~json
{
  "source": "00baf5dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf61c`](#insn-00baf61c)

~~~json
{
  "source": "00baf61c",
  "target": "00baf638",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf624`](#insn-00baf624)

~~~json
{
  "source": "00baf624",
  "target": "00baf66c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf634`](#insn-00baf634)

~~~json
{
  "source": "00baf634",
  "target": "00baf68c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf638`](#insn-00baf638)

~~~json
{
  "source": "00baf638",
  "target": "00baf68c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf658`](#insn-00baf658)

~~~json
{
  "source": "00baf658",
  "target": "00baf68c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf668`](#insn-00baf668)

~~~json
{
  "source": "00baf668",
  "target": "00baf68c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf67c`](#insn-00baf67c)

~~~json
{
  "source": "00baf67c",
  "target": "00baf68c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf694`](#insn-00baf694)

~~~json
{
  "source": "00baf694",
  "target": "00baf710",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf69c`](#insn-00baf69c)

~~~json
{
  "source": "00baf69c",
  "target": "00baf6b8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf6b4`](#insn-00baf6b4)

~~~json
{
  "source": "00baf6b4",
  "target": "00baf710",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf6cc`](#insn-00baf6cc)

~~~json
{
  "source": "00baf6cc",
  "target": "00baf6a8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf6e8`](#insn-00baf6e8)

~~~json
{
  "source": "00baf6e8",
  "target": "00baf6a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf700`](#insn-00baf700)

~~~json
{
  "source": "00baf700",
  "target": "00baf6d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf70c`](#insn-00baf70c)

~~~json
{
  "source": "00baf70c",
  "target": "00baf6a4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf710`](#insn-00baf710)

~~~json
{
  "source": "00baf710",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf714`](#insn-00baf714)

~~~json
{
  "source": "00baf714",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf718`](#insn-00baf718)

~~~json
{
  "source": "00baf718",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00baf71c`](#insn-00baf71c)

~~~json
{
  "source": "00baf71c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
