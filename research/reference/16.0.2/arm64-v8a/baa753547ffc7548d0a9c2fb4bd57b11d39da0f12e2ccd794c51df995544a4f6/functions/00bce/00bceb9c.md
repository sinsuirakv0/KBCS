# 00bceb9c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bceb00`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bceb00.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-ec18b4dbaa3394f4e155e3e17147b17c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcfb90`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bcf/00bcfb90.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0010.md#compare-f78b0b6bba043dfe180522e9e2ac226f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bceb9c",
  "name": "_ZN8firebase4auth4Auth17SignInAnonymouslyEv",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "41e96f138b874be64e5df5b4c7a895ca83f956e3882cc592c4dd672928a2951c",
  "source_text_sha256": "41e96f138b874be64e5df5b4c7a895ca83f956e3882cc592c4dd672928a2951c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bceb9c",
        "00bcecef"
      ]
    ],
    "bytes_sha256": "ccdc3d2091ccb87f3a4b962289902ce2ef3c38350557449a5b3b6b14585fb8ac",
    "instruction_count": 85,
    "instruction_bytes": 340,
    "body_bytes": 340,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c57f60](../00c57/00c57f60.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5b010](../00c5b/00c5b010.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5dcd0](../00c5d/00c5dcd0.md)
- [00c5dda0](../00c5d/00c5dda0.md)
- [00c5de00](../00c5d/00c5de00.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2527 bytes

~~~c

void _ZN8firebase4auth4Auth17SignInAnonymouslyEv(undefined8 param_1,long *param_2)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  long *plVar4;
  undefined8 uVar5;
  ulong uVar6;
  undefined8 uVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
            (auStack_68,lVar1,4);
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
  uVar5 = FUN_00497874(plVar4,*(undefined8 *)(*param_2 + 0x1f8),DAT_011268a8);
  uVar6 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                    (plVar4,lVar1,auStack_68);
  if ((uVar6 & 1) == 0) {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
    puVar10 = (undefined8 *)*param_2;
    uVar7 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
    lVar8 = _Znwm(0x20);
    _ZN8firebase12FutureHandleC1ERKS0_(lVar8,auStack_78);
    puVar3 = 
    PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9baf0
    ;
    *(undefined8 **)(lVar8 + 0x10) = puVar10;
    *(undefined **)(lVar8 + 0x18) = puVar3;
    if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
      lVar9 = (long)puVar10 + 0x141;
    }
    else {
      lVar9 = puVar10[0x2a];
    }
    _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
              (uVar7,uVar5,
               PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9bad0
               ,lVar8,lVar9);
    _ZN8firebase12FutureHandleD2Ev(auStack_78);
    (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
  }
  _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,lVar1,auStack_68);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
                    /* try { // try from 00bcecc4 to 00ccee53 has its CatchHandler @ 00bcecc4
                       catch() { ... } // from try @ 00bcecc4 with catch @ 00bcecc4
                       catch() { ... } // from try @ 00bcee5c with catch @ 00bcecc4 */
  if (*(long *)(lVar2 + 0x28) == local_58) {
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
<a id="insn-00bceb9c"></a> `00bceb9c` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bceba0"></a> `00bceba0` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bceba4"></a> `00bceba4` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bceba8"></a> `00bceba8` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcebac"></a> `00bcebac` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcebb0"></a> `00bcebb0` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcebb4"></a> `00bcebb4` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcebb8"></a> `00bcebb8` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcebbc"></a> `00bcebbc` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcebc0"></a> `00bcebc0` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bcebc4"></a> `00bcebc4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcebc8"></a> `00bcebc8` | `81 00 80 52` | mov w1,#0x4 | `FALL_THROUGH`
<a id="insn-00bcebcc"></a> `00bcebcc` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bcebd0"></a> `00bcebd0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcebd4"></a> `00bcebd4` | `14 41 00 91` | add x20,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcebd8"></a> `00bcebd8` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcebdc"></a> `00bcebdc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcebe0"></a> `00bcebe0` | `3c 3c 02 94` | bl 0x00c5dcd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcebe4"></a> `00bcebe4` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bcebe8"></a> `00bcebe8` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcebec"></a> `00bcebec` | `59 31 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcebf0"></a> `00bcebf0` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bcebf4"></a> `00bcebf4` | `c9 2a 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcebf8"></a> `00bcebf8` | `22 55 44 f9` | ldr x2,[x9, #0x8a8] | `FALL_THROUGH`
<a id="insn-00bcebfc"></a> `00bcebfc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcec00"></a> `00bcec00` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bcec04"></a> `00bcec04` | `1c 23 e3 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec08"></a> `00bcec08` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcec0c"></a> `00bcec0c` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcec10"></a> `00bcec10` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcec14"></a> `00bcec14` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcec18"></a> `00bcec18` | `62 3c 02 94` | bl 0x00c5dda0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec1c"></a> `00bcec1c` | `60 04 00 37` | tbnz w0,#0x0,0x00bceca8 | `CONDITIONAL_JUMP`
<a id="insn-00bcec20"></a> `00bcec20` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcec24"></a> `00bcec24` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcec28"></a> `00bcec28` | `aa 30 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec2c"></a> `00bcec2c` | `fa 02 40 f9` | ldr x26,[x23] | `FALL_THROUGH`
<a id="insn-00bcec30"></a> `00bcec30` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00bcec34"></a> `00bcec34` | `47 31 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec38"></a> `00bcec38` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcec3c"></a> `00bcec3c` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bcec40"></a> `00bcec40` | `c8 24 02 94` | bl 0x00c57f60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec44"></a> `00bcec44` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcec48"></a> `00bcec48` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcec4c"></a> `00bcec4c` | `a1 30 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec50"></a> `00bcec50` | `68 06 00 b0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcec54"></a> `00bcec54` | `08 79 45 f9` | ldr x8,[x8, #0xaf0] | `FALL_THROUGH`
<a id="insn-00bcec58"></a> `00bcec58` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bcec5c"></a> `00bcec5c` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00bcec60"></a> `00bcec60` | `88 00 00 37` | tbnz w8,#0x0,0x00bcec70 | `CONDITIONAL_JUMP`
<a id="insn-00bcec64"></a> `00bcec64` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00bcec68"></a> `00bcec68` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcec6c"></a> `00bcec6c` | `02 00 00 14` | b 0x00bcec74 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcec70"></a> `00bcec70` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00bcec74"></a> `00bcec74` | `62 06 00 b0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcec78"></a> `00bcec78` | `42 68 45 f9` | ldr x2,[x2, #0xad0] | `FALL_THROUGH`
<a id="insn-00bcec7c"></a> `00bcec7c` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcec80"></a> `00bcec80` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcec84"></a> `00bcec84` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bcec88"></a> `00bcec88` | `e2 30 02 94` | bl 0x00c5b010 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec8c"></a> `00bcec8c` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcec90"></a> `00bcec90` | `b4 2f 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcec94"></a> `00bcec94` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcec98"></a> `00bcec98` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcec9c"></a> `00bcec9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bceca0"></a> `00bceca0` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bceca4"></a> `00bceca4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bceca8"></a> `00bceca8` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcecac"></a> `00bcecac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcecb0"></a> `00bcecb0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcecb4"></a> `00bcecb4` | `53 3c 02 94` | bl 0x00c5de00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcecb8"></a> `00bcecb8` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcecbc"></a> `00bcecbc` | `a9 2f 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcecc0"></a> `00bcecc0` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bcecc4"></a> `00bcecc4` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bcecc8"></a> `00bcecc8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bceccc"></a> `00bceccc` | `01 01 00 54` | b.ne 0x00bcecec | `CONDITIONAL_JUMP`
<a id="insn-00bcecd0"></a> `00bcecd0` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcecd4"></a> `00bcecd4` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcecd8"></a> `00bcecd8` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcecdc"></a> `00bcecdc` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcece0"></a> `00bcece0` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcece4"></a> `00bcece4` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcece8"></a> `00bcece8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcecec"></a> `00bcecec` | `b1 24 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bceb9c`](#insn-00bceb9c) 範囲 `[['00bceb9c', '00bcec1f']]`
  - `CONDITIONAL_JUMP` [`00bcec1c`](#insn-00bcec1c) → [`00bceca8`](#insn-00bceca8)
  - `FALL_THROUGH` [`00bcec1c`](#insn-00bcec1c) → [`00bcec20`](#insn-00bcec20)
- ブロック [`00bcec20`](#insn-00bcec20) 範囲 `[['00bcec20', '00bcec63']]`
  - `CONDITIONAL_JUMP` [`00bcec60`](#insn-00bcec60) → [`00bcec70`](#insn-00bcec70)
  - `FALL_THROUGH` [`00bcec60`](#insn-00bcec60) → [`00bcec64`](#insn-00bcec64)
- ブロック [`00bcec64`](#insn-00bcec64) 範囲 `[['00bcec64', '00bcec6f']]`
  - `UNCONDITIONAL_JUMP` [`00bcec6c`](#insn-00bcec6c) → [`00bcec74`](#insn-00bcec74)
- ブロック [`00bcec70`](#insn-00bcec70) 範囲 `[['00bcec70', '00bcec73']]`
  - `FALL_THROUGH` [`00bcec70`](#insn-00bcec70) → [`00bcec74`](#insn-00bcec74)
- ブロック [`00bcec74`](#insn-00bcec74) 範囲 `[['00bcec74', '00bceca7']]`
  - `FALL_THROUGH` [`00bceca4`](#insn-00bceca4) → [`00bceca8`](#insn-00bceca8)
- ブロック [`00bceca8`](#insn-00bceca8) 範囲 `[['00bceca8', '00bcecc3']]`
  - `FALL_THROUGH` [`00bcecc0`](#insn-00bcecc0) → [`00bcecc4`](#insn-00bcecc4)
- ブロック [`00bcecc4`](#insn-00bcecc4) 範囲 `[['00bcecc4', '00bceccf']]`
  - `CONDITIONAL_JUMP` [`00bceccc`](#insn-00bceccc) → [`00bcecec`](#insn-00bcecec)
  - `FALL_THROUGH` [`00bceccc`](#insn-00bceccc) → [`00bcecd0`](#insn-00bcecd0)
- ブロック [`00bcecd0`](#insn-00bcecd0) 範囲 `[['00bcecd0', '00bceceb']]`
- ブロック [`00bcecec`](#insn-00bcecec) 範囲 `[['00bcecec', '00bcecef']]`

## 命令位置別の参照

- [`00bceba0`](#insn-00bceba0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceba4`](#insn-00bceba4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceba8`](#insn-00bceba8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebac`](#insn-00bcebac) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebb0`](#insn-00bcebb0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebcc`](#insn-00bcebcc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcebe0`](#insn-00bcebe0) → [`00c5dcd0`](../00c5d/00c5dcd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dcd0` · 推定シンボル `None` · 推定型 `None`
- [`00bcebec`](#insn-00bcebec) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bcebf8`](#insn-00bcebf8) → `011268a8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcec04`](#insn-00bcec04) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bcec18`](#insn-00bcec18) → [`00c5dda0`](../00c5d/00c5dda0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dda0` · 推定シンボル `None` · 推定型 `None`
- [`00bcec1c`](#insn-00bcec1c) → [`00bceca8`](#insn-00bceca8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec28`](#insn-00bcec28) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcec34`](#insn-00bcec34) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bcec40`](#insn-00bcec40) → [`00c57f60`](../00c57/00c57f60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f60` · 推定シンボル `None` · 推定型 `None`
- [`00bcec4c`](#insn-00bcec4c) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcec54`](#insn-00bcec54) → `00c9baf0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcec58`](#insn-00bcec58) → [`00bd48c8`](../00bd4/00bd48c8.md) · `DATA` · `ANALYSIS` · 関数 `00bd48c8` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00bcec60`](#insn-00bcec60) → [`00bcec70`](#insn-00bcec70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec6c`](#insn-00bcec6c) → [`00bcec74`](#insn-00bcec74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcec78`](#insn-00bcec78) → `00c9bad0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcec78`](#insn-00bcec78) → [`00bcfde0`](../00bcf/00bcfde0.md) · `PARAM` · `ANALYSIS` · 関数 `00bcfde0` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bcec88`](#insn-00bcec88) → [`00c5b010`](../00c5b/00c5b010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b010` · 推定シンボル `None` · 推定型 `None`
- [`00bcec90`](#insn-00bcec90) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcecb4`](#insn-00bcecb4) → [`00c5de00`](../00c5d/00c5de00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5de00` · 推定シンボル `None` · 推定型 `None`
- [`00bcecbc`](#insn-00bcecbc) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcecc4`](#insn-00bcecc4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bceccc`](#insn-00bceccc) → [`00bcecec`](#insn-00bcecec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecd0`](#insn-00bcecd0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecd4`](#insn-00bcecd4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecd8`](#insn-00bcecd8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecdc`](#insn-00bcecdc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcece0`](#insn-00bcece0) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcecec`](#insn-00bcecec) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bceba0`](#insn-00bceba0)

~~~json
{
  "source": "00bceba0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceba4`](#insn-00bceba4)

~~~json
{
  "source": "00bceba4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceba8`](#insn-00bceba8)

~~~json
{
  "source": "00bceba8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebac`](#insn-00bcebac)

~~~json
{
  "source": "00bcebac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebb0`](#insn-00bcebb0)

~~~json
{
  "source": "00bcebb0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebcc`](#insn-00bcebcc)

~~~json
{
  "source": "00bcebcc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcebe0`](#insn-00bcebe0)

~~~json
{
  "source": "00bcebe0",
  "target": "00c5dcd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcebec`](#insn-00bcebec)

~~~json
{
  "source": "00bcebec",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcebf8`](#insn-00bcebf8)

~~~json
{
  "source": "00bcebf8",
  "target": "011268a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011268a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcec04`](#insn-00bcec04)

~~~json
{
  "source": "00bcec04",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec18`](#insn-00bcec18)

~~~json
{
  "source": "00bcec18",
  "target": "00c5dda0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec1c`](#insn-00bcec1c)

~~~json
{
  "source": "00bcec1c",
  "target": "00bceca8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec28`](#insn-00bcec28)

~~~json
{
  "source": "00bcec28",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec34`](#insn-00bcec34)

~~~json
{
  "source": "00bcec34",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec40`](#insn-00bcec40)

~~~json
{
  "source": "00bcec40",
  "target": "00c57f60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec4c`](#insn-00bcec4c)

~~~json
{
  "source": "00bcec4c",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec54`](#insn-00bcec54)

~~~json
{
  "source": "00bcec54",
  "target": "00c9baf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9baf0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcec58`](#insn-00bcec58)

~~~json
{
  "source": "00bcec58",
  "target": "00bd48c8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec60`](#insn-00bcec60)

~~~json
{
  "source": "00bcec60",
  "target": "00bcec70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec6c`](#insn-00bcec6c)

~~~json
{
  "source": "00bcec6c",
  "target": "00bcec74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcec78`](#insn-00bcec78)

~~~json
{
  "source": "00bcec78",
  "target": "00c9bad0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bad0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcec78`](#insn-00bcec78)

~~~json
{
  "source": "00bcec78",
  "target": "00bcfde0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec88`](#insn-00bcec88)

~~~json
{
  "source": "00bcec88",
  "target": "00c5b010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcec90`](#insn-00bcec90)

~~~json
{
  "source": "00bcec90",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcecb4`](#insn-00bcecb4)

~~~json
{
  "source": "00bcecb4",
  "target": "00c5de00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcecbc`](#insn-00bcecbc)

~~~json
{
  "source": "00bcecbc",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcecc4`](#insn-00bcecc4)

~~~json
{
  "source": "00bcecc4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bceccc`](#insn-00bceccc)

~~~json
{
  "source": "00bceccc",
  "target": "00bcecec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecd0`](#insn-00bcecd0)

~~~json
{
  "source": "00bcecd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecd4`](#insn-00bcecd4)

~~~json
{
  "source": "00bcecd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecd8`](#insn-00bcecd8)

~~~json
{
  "source": "00bcecd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecdc`](#insn-00bcecdc)

~~~json
{
  "source": "00bcecdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcece0`](#insn-00bcece0)

~~~json
{
  "source": "00bcece0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcecec`](#insn-00bcecec)

~~~json
{
  "source": "00bcecec",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
