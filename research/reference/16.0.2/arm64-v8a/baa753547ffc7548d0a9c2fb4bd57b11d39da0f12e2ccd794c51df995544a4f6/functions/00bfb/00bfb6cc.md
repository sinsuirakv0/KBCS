# 00bfb6cc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfb630`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb630.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0041.md#compare-8d3205166a170fb1df84c6a63216f034)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfc6c0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc6c0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0038.md#compare-bbf569e92eb392cead5468cd2aec41b6)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb6cc",
  "name": "_ZNSt6__ndk18ios_base7copyfmtERKS0_",
  "size": 688,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b67b69acf7dcb784668b08e1a57eb853e1444e917f18b082240fc5ef1ec76d11",
  "source_text_sha256": "b67b69acf7dcb784668b08e1a57eb853e1444e917f18b082240fc5ef1ec76d11",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfb6cc",
        "00bfb95f"
      ],
      [
        "00bfb970",
        "00bfb98b"
      ]
    ],
    "bytes_sha256": "02090f10852cfa821eebf93fa0056084baf1633833e2ca7cc5e6160c96fd427f",
    "instruction_count": 172,
    "instruction_bytes": 688,
    "body_bytes": 688,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5e3e0](../00c5e/00c5e3e0.md)

## 呼び出し先

- [00c53ffc](../00c53/00c53ffc.md)
- [00c58730](../00c58/00c58730.md)
- [00c5a0f0](../00c5a/00c5a0f0.md)
- [00c5e050](../00c5e/00c5e050.md)
- [00c5e3b0](../00c5e/00c5e3b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4411 bytes

~~~c

void _ZNSt6__ndk18ios_base7copyfmtERKS0_(long param_1,long param_2)

{
  ulong uVar1;
  void *__ptr;
  void *__ptr_00;
  void *__ptr_01;
  undefined8 uVar2;
  ulong uVar3;
  long lVar4;
  long lVar5;
  void *unaff_x19;
  void *pvVar6;
  void *unaff_x23;
  undefined8 uVar7;
  
  pvVar6 = *(void **)(param_2 + 0x48);
  if (*(void **)(param_1 + 0x50) < pvVar6) {
    __ptr = malloc((long)pvVar6 << 3);
    if (__ptr == (void *)0x0) {
      _ZSt17__throw_bad_allocv();
LAB_00bfb934:
      uVar2 = _ZSt17__throw_bad_allocv();
      if (unaff_x23 != (void *)0x0) {
        free(unaff_x23);
      }
      if (pvVar6 != (void *)0x0) {
        free(pvVar6);
      }
      if (unaff_x19 != (void *)0x0) {
        free(unaff_x19);
                    /* WARNING: Subroutine does not return */
        FUN_00c53ffc(uVar2);
      }
                    /* WARNING: Subroutine does not return */
      FUN_00c53ffc(uVar2);
    }
    __ptr_00 = malloc((long)pvVar6 << 2);
    unaff_x19 = __ptr;
    if (__ptr_00 == (void *)0x0) goto LAB_00bfb934;
  }
  else {
    __ptr_00 = (void *)0x0;
    __ptr = (void *)0x0;
  }
  if (*(ulong *)(param_1 + 0x68) < *(ulong *)(param_2 + 0x60)) {
    pvVar6 = malloc(*(ulong *)(param_2 + 0x60) << 3);
    if (pvVar6 == (void *)0x0) {
      _ZSt17__throw_bad_allocv();
      goto LAB_00bfb74c;
    }
  }
  else {
LAB_00bfb74c:
    pvVar6 = (void *)0x0;
  }
  if (*(ulong *)(param_1 + 0x80) < *(ulong *)(param_2 + 0x78)) {
    __ptr_01 = malloc(*(ulong *)(param_2 + 0x78) << 3);
    if (__ptr_01 != (void *)0x0) goto LAB_00bfb778;
    _ZSt17__throw_bad_allocv();
  }
  __ptr_01 = (void *)0x0;
LAB_00bfb778:
  uVar7 = *(undefined8 *)(param_2 + 0x18);
  uVar2 = *(undefined8 *)(param_2 + 0x10);
  *(undefined4 *)(param_1 + 8) = *(undefined4 *)(param_2 + 8);
  *(undefined8 *)(param_1 + 0x18) = uVar7;
  *(undefined8 *)(param_1 + 0x10) = uVar2;
  _ZNSt6__ndk16localeaSERKS0_(param_1 + 0x30,param_2 + 0x30);
  if (*(ulong *)(param_1 + 0x50) < *(ulong *)(param_2 + 0x48)) {
    free(*(void **)(param_1 + 0x38));
    *(void **)(param_1 + 0x38) = __ptr;
    free(*(void **)(param_1 + 0x40));
    uVar2 = *(undefined8 *)(param_2 + 0x48);
    __ptr = (void *)0x0;
    *(void **)(param_1 + 0x40) = __ptr_00;
    __ptr_00 = (void *)0x0;
    *(undefined8 *)(param_1 + 0x50) = uVar2;
  }
  *(undefined8 *)(param_1 + 0x48) = 0;
  if (*(long *)(param_2 + 0x48) != 0) {
    uVar3 = 0;
    do {
      lVar4 = uVar3 * 8;
      lVar5 = uVar3 * 4;
      uVar3 = uVar3 + 1;
      uVar2 = *(undefined8 *)(*(long *)(param_2 + 0x38) + lVar4);
      *(ulong *)(param_1 + 0x48) = uVar3;
      *(undefined8 *)(*(long *)(param_1 + 0x38) + lVar4) = uVar2;
      uVar1 = *(ulong *)(param_2 + 0x48);
      *(undefined4 *)(*(long *)(param_1 + 0x40) + lVar5) =
           *(undefined4 *)(*(long *)(param_2 + 0x40) + lVar5);
    } while (uVar3 < uVar1);
  }
  if (*(ulong *)(param_1 + 0x68) < *(ulong *)(param_2 + 0x60)) {
    free(*(void **)(param_1 + 0x58));
    uVar2 = *(undefined8 *)(param_2 + 0x60);
    *(void **)(param_1 + 0x58) = pvVar6;
    pvVar6 = (void *)0x0;
    *(undefined8 *)(param_1 + 0x68) = uVar2;
  }
  *(undefined8 *)(param_1 + 0x60) = 0;
  if (*(long *)(param_2 + 0x60) != 0) {
    lVar4 = *(long *)(param_2 + 0x58);
    lVar5 = *(long *)(param_1 + 0x58);
    uVar3 = 0;
    do {
      *(undefined8 *)(lVar5 + uVar3 * 8) = *(undefined8 *)(lVar4 + uVar3 * 8);
      uVar3 = *(long *)(param_1 + 0x60) + 1;
      *(ulong *)(param_1 + 0x60) = uVar3;
    } while (uVar3 < *(ulong *)(param_2 + 0x60));
  }
  if (*(ulong *)(param_1 + 0x80) < *(ulong *)(param_2 + 0x78)) {
    free(*(void **)(param_1 + 0x70));
    uVar2 = *(undefined8 *)(param_2 + 0x78);
    *(void **)(param_1 + 0x70) = __ptr_01;
    __ptr_01 = (void *)0x0;
    *(undefined8 *)(param_1 + 0x80) = uVar2;
  }
  *(undefined8 *)(param_1 + 0x78) = 0;
  if (*(long *)(param_2 + 0x78) != 0) {
    uVar3 = 0;
    do {
      lVar4 = uVar3 * 8;
      uVar3 = uVar3 + 1;
      *(ulong *)(param_1 + 0x78) = uVar3;
      uVar1 = *(ulong *)(param_2 + 0x78);
      *(undefined8 *)(*(long *)(param_1 + 0x70) + lVar4) =
           *(undefined8 *)(*(long *)(param_2 + 0x70) + lVar4);
    } while (uVar3 < uVar1);
  }
  if (__ptr_01 != (void *)0x0) {
    free(__ptr_01);
  }
  if (pvVar6 != (void *)0x0) {
    free(pvVar6);
  }
  if (__ptr_00 != (void *)0x0) {
    free(__ptr_00);
  }
  if (__ptr != (void *)0x0) {
    free(__ptr);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfb6cc"></a> `00bfb6cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfb6d0"></a> `00bfb6d0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bfb6d4"></a> `00bfb6d4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb6d8"></a> `00bfb6d8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb6dc"></a> `00bfb6dc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfb6e0"></a> `00bfb6e0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfb6e4"></a> `00bfb6e4` | `08 28 40 f9` | ldr x8,[x0, #0x50] | `FALL_THROUGH`
<a id="insn-00bfb6e8"></a> `00bfb6e8` | `34 24 40 f9` | ldr x20,[x1, #0x48] | `FALL_THROUGH`
<a id="insn-00bfb6ec"></a> `00bfb6ec` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bfb6f0"></a> `00bfb6f0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bfb6f4"></a> `00bfb6f4` | `1f 01 14 eb` | cmp x8,x20 | `FALL_THROUGH`
<a id="insn-00bfb6f8"></a> `00bfb6f8` | `42 01 00 54` | b.cs 0x00bfb720 | `CONDITIONAL_JUMP`
<a id="insn-00bfb6fc"></a> `00bfb6fc` | `80 f2 7d d3` | lsl x0,x20,#0x3 | `FALL_THROUGH`
<a id="insn-00bfb700"></a> `00bfb700` | `7c 7a 01 94` | bl 0x00c5a0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb704"></a> `00bfb704` | `60 11 00 b4` | cbz x0,0x00bfb930 | `CONDITIONAL_JUMP`
<a id="insn-00bfb708"></a> `00bfb708` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfb70c"></a> `00bfb70c` | `80 f6 7e d3` | lsl x0,x20,#0x2 | `FALL_THROUGH`
<a id="insn-00bfb710"></a> `00bfb710` | `78 7a 01 94` | bl 0x00c5a0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb714"></a> `00bfb714` | `00 11 00 b4` | cbz x0,0x00bfb934 | `CONDITIONAL_JUMP`
<a id="insn-00bfb718"></a> `00bfb718` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfb71c"></a> `00bfb71c` | `03 00 00 14` | b 0x00bfb728 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfb720"></a> `00bfb720` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00bfb724"></a> `00bfb724` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00bfb728"></a> `00bfb728` | `c9 36 40 f9` | ldr x9,[x22, #0x68] | `FALL_THROUGH`
<a id="insn-00bfb72c"></a> `00bfb72c` | `a8 32 40 f9` | ldr x8,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00bfb730"></a> `00bfb730` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfb734"></a> `00bfb734` | `c2 00 00 54` | b.cs 0x00bfb74c | `CONDITIONAL_JUMP`
<a id="insn-00bfb738"></a> `00bfb738` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bfb73c"></a> `00bfb73c` | `6d 7a 01 94` | bl 0x00c5a0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb740"></a> `00bfb740` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bfb744"></a> `00bfb744` | `60 00 00 b5` | cbnz x0,0x00bfb750 | `CONDITIONAL_JUMP`
<a id="insn-00bfb748"></a> `00bfb748` | `42 8a 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb74c"></a> `00bfb74c` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bfb750"></a> `00bfb750` | `c9 42 40 f9` | ldr x9,[x22, #0x80] | `FALL_THROUGH`
<a id="insn-00bfb754"></a> `00bfb754` | `a8 3e 40 f9` | ldr x8,[x21, #0x78] | `FALL_THROUGH`
<a id="insn-00bfb758"></a> `00bfb758` | `3f 01 08 eb` | cmp x9,x8 | `FALL_THROUGH`
<a id="insn-00bfb75c"></a> `00bfb75c` | `c2 00 00 54` | b.cs 0x00bfb774 | `CONDITIONAL_JUMP`
<a id="insn-00bfb760"></a> `00bfb760` | `00 f1 7d d3` | lsl x0,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bfb764"></a> `00bfb764` | `63 7a 01 94` | bl 0x00c5a0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb768"></a> `00bfb768` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bfb76c"></a> `00bfb76c` | `60 00 00 b5` | cbnz x0,0x00bfb778 | `CONDITIONAL_JUMP`
<a id="insn-00bfb770"></a> `00bfb770` | `38 8a 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb774"></a> `00bfb774` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00bfb778"></a> `00bfb778` | `a8 0a 40 b9` | ldr w8,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bfb77c"></a> `00bfb77c` | `a0 06 c0 3d` | ldr q0,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb780"></a> `00bfb780` | `c0 c2 00 91` | add x0,x22,#0x30 | `FALL_THROUGH`
<a id="insn-00bfb784"></a> `00bfb784` | `a1 c2 00 91` | add x1,x21,#0x30 | `FALL_THROUGH`
<a id="insn-00bfb788"></a> `00bfb788` | `c8 0a 00 b9` | str w8,[x22, #0x8] | `FALL_THROUGH`
<a id="insn-00bfb78c"></a> `00bfb78c` | `c0 06 80 3d` | str q0,[x22, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb790"></a> `00bfb790` | `08 8b 01 94` | bl 0x00c5e3b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb794"></a> `00bfb794` | `c8 2a 40 f9` | ldr x8,[x22, #0x50] | `FALL_THROUGH`
<a id="insn-00bfb798"></a> `00bfb798` | `a9 26 40 f9` | ldr x9,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00bfb79c"></a> `00bfb79c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfb7a0"></a> `00bfb7a0` | `62 01 00 54` | b.cs 0x00bfb7cc | `CONDITIONAL_JUMP`
<a id="insn-00bfb7a4"></a> `00bfb7a4` | `c0 1e 40 f9` | ldr x0,[x22, #0x38] | `FALL_THROUGH`
<a id="insn-00bfb7a8"></a> `00bfb7a8` | `e2 73 01 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb7ac"></a> `00bfb7ac` | `c0 22 40 f9` | ldr x0,[x22, #0x40] | `FALL_THROUGH`
<a id="insn-00bfb7b0"></a> `00bfb7b0` | `d3 1e 00 f9` | str x19,[x22, #0x38] | `FALL_THROUGH`
<a id="insn-00bfb7b4"></a> `00bfb7b4` | `df 73 01 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb7b8"></a> `00bfb7b8` | `a8 26 40 f9` | ldr x8,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00bfb7bc"></a> `00bfb7bc` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-00bfb7c0"></a> `00bfb7c0` | `d4 22 00 f9` | str x20,[x22, #0x40] | `FALL_THROUGH`
<a id="insn-00bfb7c4"></a> `00bfb7c4` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00bfb7c8"></a> `00bfb7c8` | `c8 2a 00 f9` | str x8,[x22, #0x50] | `FALL_THROUGH`
<a id="insn-00bfb7cc"></a> `00bfb7cc` | `df 26 00 f9` | str xzr,[x22, #0x48] | `FALL_THROUGH`
<a id="insn-00bfb7d0"></a> `00bfb7d0` | `a8 26 40 f9` | ldr x8,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00bfb7d4"></a> `00bfb7d4` | `08 02 00 b4` | cbz x8,0x00bfb814 | `CONDITIONAL_JUMP`
<a id="insn-00bfb7d8"></a> `00bfb7d8` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bfb7dc"></a> `00bfb7dc` | `a9 1e 40 f9` | ldr x9,[x21, #0x38] | `FALL_THROUGH`
<a id="insn-00bfb7e0"></a> `00bfb7e0` | `0a f1 7d d3` | lsl x10,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bfb7e4"></a> `00bfb7e4` | `cb 1e 40 f9` | ldr x11,[x22, #0x38] | `FALL_THROUGH`
<a id="insn-00bfb7e8"></a> `00bfb7e8` | `0c f5 7e d3` | lsl x12,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bfb7ec"></a> `00bfb7ec` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb7f0"></a> `00bfb7f0` | `29 69 6a f8` | ldr x9,[x9, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfb7f4"></a> `00bfb7f4` | `c8 26 00 f9` | str x8,[x22, #0x48] | `FALL_THROUGH`
<a id="insn-00bfb7f8"></a> `00bfb7f8` | `69 69 2a f8` | str x9,[x11, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfb7fc"></a> `00bfb7fc` | `a9 2a 44 a9` | ldp x9,x10,[x21, #0x40] | `FALL_THROUGH`
<a id="insn-00bfb800"></a> `00bfb800` | `cb 22 40 f9` | ldr x11,[x22, #0x40] | `FALL_THROUGH`
<a id="insn-00bfb804"></a> `00bfb804` | `29 69 6c b8` | ldr w9,[x9, x12, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfb808"></a> `00bfb808` | `1f 01 0a eb` | cmp x8,x10 | `FALL_THROUGH`
<a id="insn-00bfb80c"></a> `00bfb80c` | `69 69 2c b8` | str w9,[x11, x12, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfb810"></a> `00bfb810` | `63 fe ff 54` | b.cc 0x00bfb7dc | `CONDITIONAL_JUMP`
<a id="insn-00bfb814"></a> `00bfb814` | `c8 36 40 f9` | ldr x8,[x22, #0x68] | `FALL_THROUGH`
<a id="insn-00bfb818"></a> `00bfb818` | `a9 32 40 f9` | ldr x9,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00bfb81c"></a> `00bfb81c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfb820"></a> `00bfb820` | `e2 00 00 54` | b.cs 0x00bfb83c | `CONDITIONAL_JUMP`
<a id="insn-00bfb824"></a> `00bfb824` | `c0 2e 40 f9` | ldr x0,[x22, #0x58] | `FALL_THROUGH`
<a id="insn-00bfb828"></a> `00bfb828` | `c2 73 01 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb82c"></a> `00bfb82c` | `a8 32 40 f9` | ldr x8,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00bfb830"></a> `00bfb830` | `d7 2e 00 f9` | str x23,[x22, #0x58] | `FALL_THROUGH`
<a id="insn-00bfb834"></a> `00bfb834` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bfb838"></a> `00bfb838` | `c8 36 00 f9` | str x8,[x22, #0x68] | `FALL_THROUGH`
<a id="insn-00bfb83c"></a> `00bfb83c` | `df 32 00 f9` | str xzr,[x22, #0x60] | `FALL_THROUGH`
<a id="insn-00bfb840"></a> `00bfb840` | `a8 32 40 f9` | ldr x8,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00bfb844"></a> `00bfb844` | `a8 01 00 b4` | cbz x8,0x00bfb878 | `CONDITIONAL_JUMP`
<a id="insn-00bfb848"></a> `00bfb848` | `a8 2e 40 f9` | ldr x8,[x21, #0x58] | `FALL_THROUGH`
<a id="insn-00bfb84c"></a> `00bfb84c` | `c9 2e 40 f9` | ldr x9,[x22, #0x58] | `FALL_THROUGH`
<a id="insn-00bfb850"></a> `00bfb850` | `ea 03 1f aa` | mov x10,xzr | `FALL_THROUGH`
<a id="insn-00bfb854"></a> `00bfb854` | `4a f1 7d d3` | lsl x10,x10,#0x3 | `FALL_THROUGH`
<a id="insn-00bfb858"></a> `00bfb858` | `0b 69 6a f8` | ldr x11,[x8, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfb85c"></a> `00bfb85c` | `2b 69 2a f8` | str x11,[x9, x10, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfb860"></a> `00bfb860` | `ca 32 40 f9` | ldr x10,[x22, #0x60] | `FALL_THROUGH`
<a id="insn-00bfb864"></a> `00bfb864` | `4a 05 00 91` | add x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb868"></a> `00bfb868` | `ca 32 00 f9` | str x10,[x22, #0x60] | `FALL_THROUGH`
<a id="insn-00bfb86c"></a> `00bfb86c` | `ab 32 40 f9` | ldr x11,[x21, #0x60] | `FALL_THROUGH`
<a id="insn-00bfb870"></a> `00bfb870` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bfb874"></a> `00bfb874` | `03 ff ff 54` | b.cc 0x00bfb854 | `CONDITIONAL_JUMP`
<a id="insn-00bfb878"></a> `00bfb878` | `c8 42 40 f9` | ldr x8,[x22, #0x80] | `FALL_THROUGH`
<a id="insn-00bfb87c"></a> `00bfb87c` | `a9 3e 40 f9` | ldr x9,[x21, #0x78] | `FALL_THROUGH`
<a id="insn-00bfb880"></a> `00bfb880` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfb884"></a> `00bfb884` | `e2 00 00 54` | b.cs 0x00bfb8a0 | `CONDITIONAL_JUMP`
<a id="insn-00bfb888"></a> `00bfb888` | `c0 3a 40 f9` | ldr x0,[x22, #0x70] | `FALL_THROUGH`
<a id="insn-00bfb88c"></a> `00bfb88c` | `a9 73 01 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb890"></a> `00bfb890` | `a8 3e 40 f9` | ldr x8,[x21, #0x78] | `FALL_THROUGH`
<a id="insn-00bfb894"></a> `00bfb894` | `d8 3a 00 f9` | str x24,[x22, #0x70] | `FALL_THROUGH`
<a id="insn-00bfb898"></a> `00bfb898` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00bfb89c"></a> `00bfb89c` | `c8 42 00 f9` | str x8,[x22, #0x80] | `FALL_THROUGH`
<a id="insn-00bfb8a0"></a> `00bfb8a0` | `df 3e 00 f9` | str xzr,[x22, #0x78] | `FALL_THROUGH`
<a id="insn-00bfb8a4"></a> `00bfb8a4` | `a8 3e 40 f9` | ldr x8,[x21, #0x78] | `FALL_THROUGH`
<a id="insn-00bfb8a8"></a> `00bfb8a8` | `68 01 00 b4` | cbz x8,0x00bfb8d4 | `CONDITIONAL_JUMP`
<a id="insn-00bfb8ac"></a> `00bfb8ac` | `e8 03 1f aa` | mov x8,xzr | `FALL_THROUGH`
<a id="insn-00bfb8b0"></a> `00bfb8b0` | `09 f1 7d d3` | lsl x9,x8,#0x3 | `FALL_THROUGH`
<a id="insn-00bfb8b4"></a> `00bfb8b4` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb8b8"></a> `00bfb8b8` | `cc 3a 40 f9` | ldr x12,[x22, #0x70] | `FALL_THROUGH`
<a id="insn-00bfb8bc"></a> `00bfb8bc` | `c8 3e 00 f9` | str x8,[x22, #0x78] | `FALL_THROUGH`
<a id="insn-00bfb8c0"></a> `00bfb8c0` | `aa 2e 47 a9` | ldp x10,x11,[x21, #0x70] | `FALL_THROUGH`
<a id="insn-00bfb8c4"></a> `00bfb8c4` | `4a 69 69 f8` | ldr x10,[x10, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfb8c8"></a> `00bfb8c8` | `1f 01 0b eb` | cmp x8,x11 | `FALL_THROUGH`
<a id="insn-00bfb8cc"></a> `00bfb8cc` | `8a 69 29 f8` | str x10,[x12, x9, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00bfb8d0"></a> `00bfb8d0` | `03 ff ff 54` | b.cc 0x00bfb8b0 | `CONDITIONAL_JUMP`
<a id="insn-00bfb8d4"></a> `00bfb8d4` | `78 00 00 b4` | cbz x24,0x00bfb8e0 | `CONDITIONAL_JUMP`
<a id="insn-00bfb8d8"></a> `00bfb8d8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bfb8dc"></a> `00bfb8dc` | `95 73 01 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb8e0"></a> `00bfb8e0` | `77 00 00 b4` | cbz x23,0x00bfb8ec | `CONDITIONAL_JUMP`
<a id="insn-00bfb8e4"></a> `00bfb8e4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bfb8e8"></a> `00bfb8e8` | `92 73 01 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb8ec"></a> `00bfb8ec` | `74 00 00 b4` | cbz x20,0x00bfb8f8 | `CONDITIONAL_JUMP`
<a id="insn-00bfb8f0"></a> `00bfb8f0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfb8f4"></a> `00bfb8f4` | `8f 73 01 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb8f8"></a> `00bfb8f8` | `13 01 00 b4` | cbz x19,0x00bfb918 | `CONDITIONAL_JUMP`
<a id="insn-00bfb8fc"></a> `00bfb8fc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfb900"></a> `00bfb900` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfb904"></a> `00bfb904` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb908"></a> `00bfb908` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb90c"></a> `00bfb90c` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bfb910"></a> `00bfb910` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb914"></a> `00bfb914` | `87 73 01 14` | b 0x00c58730 | `CALL_TERMINATOR`
<a id="insn-00bfb918"></a> `00bfb918` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfb91c"></a> `00bfb91c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb920"></a> `00bfb920` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb924"></a> `00bfb924` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bfb928"></a> `00bfb928` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb92c"></a> `00bfb92c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfb930"></a> `00bfb930` | `c8 89 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb934"></a> `00bfb934` | `c7 89 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb938"></a> `00bfb938` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bfb93c"></a> `00bfb93c` | `b7 00 00 b5` | cbnz x23,0x00bfb950 | `CONDITIONAL_JUMP`
<a id="insn-00bfb940"></a> `00bfb940` | `94 01 00 b5` | cbnz x20,0x00bfb970 | `CONDITIONAL_JUMP`
<a id="insn-00bfb944"></a> `00bfb944` | `d3 01 00 b5` | cbnz x19,0x00bfb97c | `CONDITIONAL_JUMP`
<a id="insn-00bfb948"></a> `00bfb948` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfb94c"></a> `00bfb94c` | `ac 61 01 94` | bl 0x00c53ffc | `CALL_TERMINATOR`
<a id="insn-00bfb950"></a> `00bfb950` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bfb954"></a> `00bfb954` | `77 73 01 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb958"></a> `00bfb958` | `74 ff ff b4` | cbz x20,0x00bfb944 | `CONDITIONAL_JUMP`
<a id="insn-00bfb95c"></a> `00bfb95c` | `05 00 00 14` | b 0x00bfb970 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfb970"></a> `00bfb970` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfb974"></a> `00bfb974` | `6f 73 01 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb978"></a> `00bfb978` | `93 fe ff b4` | cbz x19,0x00bfb948 | `CONDITIONAL_JUMP`
<a id="insn-00bfb97c"></a> `00bfb97c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfb980"></a> `00bfb980` | `6c 73 01 94` | bl 0x00c58730 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb984"></a> `00bfb984` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfb988"></a> `00bfb988` | `9d 61 01 94` | bl 0x00c53ffc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfb6cc`](#insn-00bfb6cc) 範囲 `[['00bfb6cc', '00bfb6fb']]`
  - `CONDITIONAL_JUMP` [`00bfb6f8`](#insn-00bfb6f8) → [`00bfb720`](#insn-00bfb720)
  - `FALL_THROUGH` [`00bfb6f8`](#insn-00bfb6f8) → [`00bfb6fc`](#insn-00bfb6fc)
- ブロック [`00bfb6fc`](#insn-00bfb6fc) 範囲 `[['00bfb6fc', '00bfb707']]`
  - `CONDITIONAL_JUMP` [`00bfb704`](#insn-00bfb704) → [`00bfb930`](#insn-00bfb930)
  - `FALL_THROUGH` [`00bfb704`](#insn-00bfb704) → [`00bfb708`](#insn-00bfb708)
- ブロック [`00bfb708`](#insn-00bfb708) 範囲 `[['00bfb708', '00bfb717']]`
  - `CONDITIONAL_JUMP` [`00bfb714`](#insn-00bfb714) → [`00bfb934`](#insn-00bfb934)
  - `FALL_THROUGH` [`00bfb714`](#insn-00bfb714) → [`00bfb718`](#insn-00bfb718)
- ブロック [`00bfb718`](#insn-00bfb718) 範囲 `[['00bfb718', '00bfb71f']]`
  - `UNCONDITIONAL_JUMP` [`00bfb71c`](#insn-00bfb71c) → [`00bfb728`](#insn-00bfb728)
- ブロック [`00bfb720`](#insn-00bfb720) 範囲 `[['00bfb720', '00bfb727']]`
  - `FALL_THROUGH` [`00bfb724`](#insn-00bfb724) → [`00bfb728`](#insn-00bfb728)
- ブロック [`00bfb728`](#insn-00bfb728) 範囲 `[['00bfb728', '00bfb737']]`
  - `CONDITIONAL_JUMP` [`00bfb734`](#insn-00bfb734) → [`00bfb74c`](#insn-00bfb74c)
  - `FALL_THROUGH` [`00bfb734`](#insn-00bfb734) → [`00bfb738`](#insn-00bfb738)
- ブロック [`00bfb738`](#insn-00bfb738) 範囲 `[['00bfb738', '00bfb747']]`
  - `CONDITIONAL_JUMP` [`00bfb744`](#insn-00bfb744) → [`00bfb750`](#insn-00bfb750)
  - `FALL_THROUGH` [`00bfb744`](#insn-00bfb744) → [`00bfb748`](#insn-00bfb748)
- ブロック [`00bfb748`](#insn-00bfb748) 範囲 `[['00bfb748', '00bfb74b']]`
  - `FALL_THROUGH` [`00bfb748`](#insn-00bfb748) → [`00bfb74c`](#insn-00bfb74c)
- ブロック [`00bfb74c`](#insn-00bfb74c) 範囲 `[['00bfb74c', '00bfb74f']]`
  - `FALL_THROUGH` [`00bfb74c`](#insn-00bfb74c) → [`00bfb750`](#insn-00bfb750)
- ブロック [`00bfb750`](#insn-00bfb750) 範囲 `[['00bfb750', '00bfb75f']]`
  - `CONDITIONAL_JUMP` [`00bfb75c`](#insn-00bfb75c) → [`00bfb774`](#insn-00bfb774)
  - `FALL_THROUGH` [`00bfb75c`](#insn-00bfb75c) → [`00bfb760`](#insn-00bfb760)
- ブロック [`00bfb760`](#insn-00bfb760) 範囲 `[['00bfb760', '00bfb76f']]`
  - `CONDITIONAL_JUMP` [`00bfb76c`](#insn-00bfb76c) → [`00bfb778`](#insn-00bfb778)
  - `FALL_THROUGH` [`00bfb76c`](#insn-00bfb76c) → [`00bfb770`](#insn-00bfb770)
- ブロック [`00bfb770`](#insn-00bfb770) 範囲 `[['00bfb770', '00bfb773']]`
  - `FALL_THROUGH` [`00bfb770`](#insn-00bfb770) → [`00bfb774`](#insn-00bfb774)
- ブロック [`00bfb774`](#insn-00bfb774) 範囲 `[['00bfb774', '00bfb777']]`
  - `FALL_THROUGH` [`00bfb774`](#insn-00bfb774) → [`00bfb778`](#insn-00bfb778)
- ブロック [`00bfb778`](#insn-00bfb778) 範囲 `[['00bfb778', '00bfb7a3']]`
  - `CONDITIONAL_JUMP` [`00bfb7a0`](#insn-00bfb7a0) → [`00bfb7cc`](#insn-00bfb7cc)
  - `FALL_THROUGH` [`00bfb7a0`](#insn-00bfb7a0) → [`00bfb7a4`](#insn-00bfb7a4)
- ブロック [`00bfb7a4`](#insn-00bfb7a4) 範囲 `[['00bfb7a4', '00bfb7cb']]`
  - `FALL_THROUGH` [`00bfb7c8`](#insn-00bfb7c8) → [`00bfb7cc`](#insn-00bfb7cc)
- ブロック [`00bfb7cc`](#insn-00bfb7cc) 範囲 `[['00bfb7cc', '00bfb7d7']]`
  - `CONDITIONAL_JUMP` [`00bfb7d4`](#insn-00bfb7d4) → [`00bfb814`](#insn-00bfb814)
  - `FALL_THROUGH` [`00bfb7d4`](#insn-00bfb7d4) → [`00bfb7d8`](#insn-00bfb7d8)
- ブロック [`00bfb7d8`](#insn-00bfb7d8) 範囲 `[['00bfb7d8', '00bfb7db']]`
  - `FALL_THROUGH` [`00bfb7d8`](#insn-00bfb7d8) → [`00bfb7dc`](#insn-00bfb7dc)
- ブロック [`00bfb7dc`](#insn-00bfb7dc) 範囲 `[['00bfb7dc', '00bfb813']]`
  - `CONDITIONAL_JUMP` [`00bfb810`](#insn-00bfb810) → [`00bfb7dc`](#insn-00bfb7dc)
  - `FALL_THROUGH` [`00bfb810`](#insn-00bfb810) → [`00bfb814`](#insn-00bfb814)
- ブロック [`00bfb814`](#insn-00bfb814) 範囲 `[['00bfb814', '00bfb823']]`
  - `CONDITIONAL_JUMP` [`00bfb820`](#insn-00bfb820) → [`00bfb83c`](#insn-00bfb83c)
  - `FALL_THROUGH` [`00bfb820`](#insn-00bfb820) → [`00bfb824`](#insn-00bfb824)
- ブロック [`00bfb824`](#insn-00bfb824) 範囲 `[['00bfb824', '00bfb83b']]`
  - `FALL_THROUGH` [`00bfb838`](#insn-00bfb838) → [`00bfb83c`](#insn-00bfb83c)
- ブロック [`00bfb83c`](#insn-00bfb83c) 範囲 `[['00bfb83c', '00bfb847']]`
  - `CONDITIONAL_JUMP` [`00bfb844`](#insn-00bfb844) → [`00bfb878`](#insn-00bfb878)
  - `FALL_THROUGH` [`00bfb844`](#insn-00bfb844) → [`00bfb848`](#insn-00bfb848)
- ブロック [`00bfb848`](#insn-00bfb848) 範囲 `[['00bfb848', '00bfb853']]`
  - `FALL_THROUGH` [`00bfb850`](#insn-00bfb850) → [`00bfb854`](#insn-00bfb854)
- ブロック [`00bfb854`](#insn-00bfb854) 範囲 `[['00bfb854', '00bfb877']]`
  - `CONDITIONAL_JUMP` [`00bfb874`](#insn-00bfb874) → [`00bfb854`](#insn-00bfb854)
  - `FALL_THROUGH` [`00bfb874`](#insn-00bfb874) → [`00bfb878`](#insn-00bfb878)
- ブロック [`00bfb878`](#insn-00bfb878) 範囲 `[['00bfb878', '00bfb887']]`
  - `CONDITIONAL_JUMP` [`00bfb884`](#insn-00bfb884) → [`00bfb8a0`](#insn-00bfb8a0)
  - `FALL_THROUGH` [`00bfb884`](#insn-00bfb884) → [`00bfb888`](#insn-00bfb888)
- ブロック [`00bfb888`](#insn-00bfb888) 範囲 `[['00bfb888', '00bfb89f']]`
  - `FALL_THROUGH` [`00bfb89c`](#insn-00bfb89c) → [`00bfb8a0`](#insn-00bfb8a0)
- ブロック [`00bfb8a0`](#insn-00bfb8a0) 範囲 `[['00bfb8a0', '00bfb8ab']]`
  - `CONDITIONAL_JUMP` [`00bfb8a8`](#insn-00bfb8a8) → [`00bfb8d4`](#insn-00bfb8d4)
  - `FALL_THROUGH` [`00bfb8a8`](#insn-00bfb8a8) → [`00bfb8ac`](#insn-00bfb8ac)
- ブロック [`00bfb8ac`](#insn-00bfb8ac) 範囲 `[['00bfb8ac', '00bfb8af']]`
  - `FALL_THROUGH` [`00bfb8ac`](#insn-00bfb8ac) → [`00bfb8b0`](#insn-00bfb8b0)
- ブロック [`00bfb8b0`](#insn-00bfb8b0) 範囲 `[['00bfb8b0', '00bfb8d3']]`
  - `CONDITIONAL_JUMP` [`00bfb8d0`](#insn-00bfb8d0) → [`00bfb8b0`](#insn-00bfb8b0)
  - `FALL_THROUGH` [`00bfb8d0`](#insn-00bfb8d0) → [`00bfb8d4`](#insn-00bfb8d4)
- ブロック [`00bfb8d4`](#insn-00bfb8d4) 範囲 `[['00bfb8d4', '00bfb8d7']]`
  - `CONDITIONAL_JUMP` [`00bfb8d4`](#insn-00bfb8d4) → [`00bfb8e0`](#insn-00bfb8e0)
  - `FALL_THROUGH` [`00bfb8d4`](#insn-00bfb8d4) → [`00bfb8d8`](#insn-00bfb8d8)
- ブロック [`00bfb8d8`](#insn-00bfb8d8) 範囲 `[['00bfb8d8', '00bfb8df']]`
  - `FALL_THROUGH` [`00bfb8dc`](#insn-00bfb8dc) → [`00bfb8e0`](#insn-00bfb8e0)
- ブロック [`00bfb8e0`](#insn-00bfb8e0) 範囲 `[['00bfb8e0', '00bfb8e3']]`
  - `CONDITIONAL_JUMP` [`00bfb8e0`](#insn-00bfb8e0) → [`00bfb8ec`](#insn-00bfb8ec)
  - `FALL_THROUGH` [`00bfb8e0`](#insn-00bfb8e0) → [`00bfb8e4`](#insn-00bfb8e4)
- ブロック [`00bfb8e4`](#insn-00bfb8e4) 範囲 `[['00bfb8e4', '00bfb8eb']]`
  - `FALL_THROUGH` [`00bfb8e8`](#insn-00bfb8e8) → [`00bfb8ec`](#insn-00bfb8ec)
- ブロック [`00bfb8ec`](#insn-00bfb8ec) 範囲 `[['00bfb8ec', '00bfb8ef']]`
  - `CONDITIONAL_JUMP` [`00bfb8ec`](#insn-00bfb8ec) → [`00bfb8f8`](#insn-00bfb8f8)
  - `FALL_THROUGH` [`00bfb8ec`](#insn-00bfb8ec) → [`00bfb8f0`](#insn-00bfb8f0)
- ブロック [`00bfb8f0`](#insn-00bfb8f0) 範囲 `[['00bfb8f0', '00bfb8f7']]`
  - `FALL_THROUGH` [`00bfb8f4`](#insn-00bfb8f4) → [`00bfb8f8`](#insn-00bfb8f8)
- ブロック [`00bfb8f8`](#insn-00bfb8f8) 範囲 `[['00bfb8f8', '00bfb8fb']]`
  - `CONDITIONAL_JUMP` [`00bfb8f8`](#insn-00bfb8f8) → [`00bfb918`](#insn-00bfb918)
  - `FALL_THROUGH` [`00bfb8f8`](#insn-00bfb8f8) → [`00bfb8fc`](#insn-00bfb8fc)
- ブロック [`00bfb8fc`](#insn-00bfb8fc) 範囲 `[['00bfb8fc', '00bfb917']]`
- ブロック [`00bfb918`](#insn-00bfb918) 範囲 `[['00bfb918', '00bfb92f']]`
- ブロック [`00bfb930`](#insn-00bfb930) 範囲 `[['00bfb930', '00bfb933']]`
  - `FALL_THROUGH` [`00bfb930`](#insn-00bfb930) → [`00bfb934`](#insn-00bfb934)
- ブロック [`00bfb934`](#insn-00bfb934) 範囲 `[['00bfb934', '00bfb93f']]`
  - `CONDITIONAL_JUMP` [`00bfb93c`](#insn-00bfb93c) → [`00bfb950`](#insn-00bfb950)
  - `FALL_THROUGH` [`00bfb93c`](#insn-00bfb93c) → [`00bfb940`](#insn-00bfb940)
- ブロック [`00bfb940`](#insn-00bfb940) 範囲 `[['00bfb940', '00bfb943']]`
  - `CONDITIONAL_JUMP` [`00bfb940`](#insn-00bfb940) → [`00bfb970`](#insn-00bfb970)
  - `FALL_THROUGH` [`00bfb940`](#insn-00bfb940) → [`00bfb944`](#insn-00bfb944)
- ブロック [`00bfb944`](#insn-00bfb944) 範囲 `[['00bfb944', '00bfb947']]`
  - `CONDITIONAL_JUMP` [`00bfb944`](#insn-00bfb944) → [`00bfb97c`](#insn-00bfb97c)
  - `FALL_THROUGH` [`00bfb944`](#insn-00bfb944) → [`00bfb948`](#insn-00bfb948)
- ブロック [`00bfb948`](#insn-00bfb948) 範囲 `[['00bfb948', '00bfb94f']]`
- ブロック [`00bfb950`](#insn-00bfb950) 範囲 `[['00bfb950', '00bfb95b']]`
  - `CONDITIONAL_JUMP` [`00bfb958`](#insn-00bfb958) → [`00bfb944`](#insn-00bfb944)
  - `FALL_THROUGH` [`00bfb958`](#insn-00bfb958) → [`00bfb95c`](#insn-00bfb95c)
- ブロック [`00bfb95c`](#insn-00bfb95c) 範囲 `[['00bfb95c', '00bfb95f']]`
  - `UNCONDITIONAL_JUMP` [`00bfb95c`](#insn-00bfb95c) → [`00bfb970`](#insn-00bfb970)
- ブロック [`00bfb970`](#insn-00bfb970) 範囲 `[['00bfb970', '00bfb97b']]`
  - `CONDITIONAL_JUMP` [`00bfb978`](#insn-00bfb978) → [`00bfb948`](#insn-00bfb948)
  - `FALL_THROUGH` [`00bfb978`](#insn-00bfb978) → [`00bfb97c`](#insn-00bfb97c)
- ブロック [`00bfb97c`](#insn-00bfb97c) 範囲 `[['00bfb97c', '00bfb98b']]`

## 命令位置別の参照

- [`00bfb6d0`](#insn-00bfb6d0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb6d4`](#insn-00bfb6d4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb6d8`](#insn-00bfb6d8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb6dc`](#insn-00bfb6dc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb6f8`](#insn-00bfb6f8) → [`00bfb720`](#insn-00bfb720) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb700`](#insn-00bfb700) → [`00c5a0f0`](../00c5a/00c5a0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bfb704`](#insn-00bfb704) → [`00bfb930`](#insn-00bfb930) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb710`](#insn-00bfb710) → [`00c5a0f0`](../00c5a/00c5a0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bfb714`](#insn-00bfb714) → [`00bfb934`](#insn-00bfb934) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb71c`](#insn-00bfb71c) → [`00bfb728`](#insn-00bfb728) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb734`](#insn-00bfb734) → [`00bfb74c`](#insn-00bfb74c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb73c`](#insn-00bfb73c) → [`00c5a0f0`](../00c5a/00c5a0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bfb744`](#insn-00bfb744) → [`00bfb750`](#insn-00bfb750) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb748`](#insn-00bfb748) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bfb75c`](#insn-00bfb75c) → [`00bfb774`](#insn-00bfb774) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb764`](#insn-00bfb764) → [`00c5a0f0`](../00c5a/00c5a0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bfb76c`](#insn-00bfb76c) → [`00bfb778`](#insn-00bfb778) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb770`](#insn-00bfb770) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bfb790`](#insn-00bfb790) → [`00c5e3b0`](../00c5e/00c5e3b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e3b0` · 推定シンボル `None` · 推定型 `None`
- [`00bfb7a0`](#insn-00bfb7a0) → [`00bfb7cc`](#insn-00bfb7cc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb7a8`](#insn-00bfb7a8) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`00bfb7b4`](#insn-00bfb7b4) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`00bfb7d4`](#insn-00bfb7d4) → [`00bfb814`](#insn-00bfb814) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb810`](#insn-00bfb810) → [`00bfb7dc`](#insn-00bfb7dc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb820`](#insn-00bfb820) → [`00bfb83c`](#insn-00bfb83c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb828`](#insn-00bfb828) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`00bfb844`](#insn-00bfb844) → [`00bfb878`](#insn-00bfb878) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb874`](#insn-00bfb874) → [`00bfb854`](#insn-00bfb854) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb884`](#insn-00bfb884) → [`00bfb8a0`](#insn-00bfb8a0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb88c`](#insn-00bfb88c) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`00bfb8a8`](#insn-00bfb8a8) → [`00bfb8d4`](#insn-00bfb8d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb8d0`](#insn-00bfb8d0) → [`00bfb8b0`](#insn-00bfb8b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb8d4`](#insn-00bfb8d4) → [`00bfb8e0`](#insn-00bfb8e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb8dc`](#insn-00bfb8dc) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`00bfb8e0`](#insn-00bfb8e0) → [`00bfb8ec`](#insn-00bfb8ec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb8e8`](#insn-00bfb8e8) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`00bfb8ec`](#insn-00bfb8ec) → [`00bfb8f8`](#insn-00bfb8f8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb8f4`](#insn-00bfb8f4) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`00bfb8f8`](#insn-00bfb8f8) → [`00bfb918`](#insn-00bfb918) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb900`](#insn-00bfb900) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb904`](#insn-00bfb904) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb908`](#insn-00bfb908) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb90c`](#insn-00bfb90c) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb914`](#insn-00bfb914) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`00bfb918`](#insn-00bfb918) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb91c`](#insn-00bfb91c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb920`](#insn-00bfb920) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb924`](#insn-00bfb924) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb930`](#insn-00bfb930) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bfb934`](#insn-00bfb934) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bfb93c`](#insn-00bfb93c) → [`00bfb950`](#insn-00bfb950) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb940`](#insn-00bfb940) → [`00bfb970`](#insn-00bfb970) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb944`](#insn-00bfb944) → [`00bfb97c`](#insn-00bfb97c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb94c`](#insn-00bfb94c) → [`00c53ffc`](../00c53/00c53ffc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53ffc` · 推定シンボル `None` · 推定型 `None`
- [`00bfb954`](#insn-00bfb954) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`00bfb958`](#insn-00bfb958) → [`00bfb944`](#insn-00bfb944) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb95c`](#insn-00bfb95c) → [`00bfb970`](#insn-00bfb970) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb974`](#insn-00bfb974) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`00bfb978`](#insn-00bfb978) → [`00bfb948`](#insn-00bfb948) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb980`](#insn-00bfb980) → [`00c58730`](../00c58/00c58730.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58730` · 推定シンボル `None` · 推定型 `None`
- [`00bfb988`](#insn-00bfb988) → [`00c53ffc`](../00c53/00c53ffc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53ffc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfb6d0`](#insn-00bfb6d0)

~~~json
{
  "source": "00bfb6d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb6d4`](#insn-00bfb6d4)

~~~json
{
  "source": "00bfb6d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb6d8`](#insn-00bfb6d8)

~~~json
{
  "source": "00bfb6d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb6dc`](#insn-00bfb6dc)

~~~json
{
  "source": "00bfb6dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb6f8`](#insn-00bfb6f8)

~~~json
{
  "source": "00bfb6f8",
  "target": "00bfb720",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb700`](#insn-00bfb700)

~~~json
{
  "source": "00bfb700",
  "target": "00c5a0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb704`](#insn-00bfb704)

~~~json
{
  "source": "00bfb704",
  "target": "00bfb930",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb710`](#insn-00bfb710)

~~~json
{
  "source": "00bfb710",
  "target": "00c5a0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb714`](#insn-00bfb714)

~~~json
{
  "source": "00bfb714",
  "target": "00bfb934",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb71c`](#insn-00bfb71c)

~~~json
{
  "source": "00bfb71c",
  "target": "00bfb728",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb734`](#insn-00bfb734)

~~~json
{
  "source": "00bfb734",
  "target": "00bfb74c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb73c`](#insn-00bfb73c)

~~~json
{
  "source": "00bfb73c",
  "target": "00c5a0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb744`](#insn-00bfb744)

~~~json
{
  "source": "00bfb744",
  "target": "00bfb750",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb748`](#insn-00bfb748)

~~~json
{
  "source": "00bfb748",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb75c`](#insn-00bfb75c)

~~~json
{
  "source": "00bfb75c",
  "target": "00bfb774",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb764`](#insn-00bfb764)

~~~json
{
  "source": "00bfb764",
  "target": "00c5a0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb76c`](#insn-00bfb76c)

~~~json
{
  "source": "00bfb76c",
  "target": "00bfb778",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb770`](#insn-00bfb770)

~~~json
{
  "source": "00bfb770",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb790`](#insn-00bfb790)

~~~json
{
  "source": "00bfb790",
  "target": "00c5e3b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb7a0`](#insn-00bfb7a0)

~~~json
{
  "source": "00bfb7a0",
  "target": "00bfb7cc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb7a8`](#insn-00bfb7a8)

~~~json
{
  "source": "00bfb7a8",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb7b4`](#insn-00bfb7b4)

~~~json
{
  "source": "00bfb7b4",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb7d4`](#insn-00bfb7d4)

~~~json
{
  "source": "00bfb7d4",
  "target": "00bfb814",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb810`](#insn-00bfb810)

~~~json
{
  "source": "00bfb810",
  "target": "00bfb7dc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb820`](#insn-00bfb820)

~~~json
{
  "source": "00bfb820",
  "target": "00bfb83c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb828`](#insn-00bfb828)

~~~json
{
  "source": "00bfb828",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb844`](#insn-00bfb844)

~~~json
{
  "source": "00bfb844",
  "target": "00bfb878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb874`](#insn-00bfb874)

~~~json
{
  "source": "00bfb874",
  "target": "00bfb854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb884`](#insn-00bfb884)

~~~json
{
  "source": "00bfb884",
  "target": "00bfb8a0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb88c`](#insn-00bfb88c)

~~~json
{
  "source": "00bfb88c",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb8a8`](#insn-00bfb8a8)

~~~json
{
  "source": "00bfb8a8",
  "target": "00bfb8d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb8d0`](#insn-00bfb8d0)

~~~json
{
  "source": "00bfb8d0",
  "target": "00bfb8b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb8d4`](#insn-00bfb8d4)

~~~json
{
  "source": "00bfb8d4",
  "target": "00bfb8e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb8dc`](#insn-00bfb8dc)

~~~json
{
  "source": "00bfb8dc",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb8e0`](#insn-00bfb8e0)

~~~json
{
  "source": "00bfb8e0",
  "target": "00bfb8ec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb8e8`](#insn-00bfb8e8)

~~~json
{
  "source": "00bfb8e8",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb8ec`](#insn-00bfb8ec)

~~~json
{
  "source": "00bfb8ec",
  "target": "00bfb8f8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb8f4`](#insn-00bfb8f4)

~~~json
{
  "source": "00bfb8f4",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb8f8`](#insn-00bfb8f8)

~~~json
{
  "source": "00bfb8f8",
  "target": "00bfb918",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb900`](#insn-00bfb900)

~~~json
{
  "source": "00bfb900",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb904`](#insn-00bfb904)

~~~json
{
  "source": "00bfb904",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb908`](#insn-00bfb908)

~~~json
{
  "source": "00bfb908",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb90c`](#insn-00bfb90c)

~~~json
{
  "source": "00bfb90c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb914`](#insn-00bfb914)

~~~json
{
  "source": "00bfb914",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb918`](#insn-00bfb918)

~~~json
{
  "source": "00bfb918",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb91c`](#insn-00bfb91c)

~~~json
{
  "source": "00bfb91c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb920`](#insn-00bfb920)

~~~json
{
  "source": "00bfb920",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb924`](#insn-00bfb924)

~~~json
{
  "source": "00bfb924",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb930`](#insn-00bfb930)

~~~json
{
  "source": "00bfb930",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb934`](#insn-00bfb934)

~~~json
{
  "source": "00bfb934",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb93c`](#insn-00bfb93c)

~~~json
{
  "source": "00bfb93c",
  "target": "00bfb950",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb940`](#insn-00bfb940)

~~~json
{
  "source": "00bfb940",
  "target": "00bfb970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb944`](#insn-00bfb944)

~~~json
{
  "source": "00bfb944",
  "target": "00bfb97c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb94c`](#insn-00bfb94c)

~~~json
{
  "source": "00bfb94c",
  "target": "00c53ffc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb954`](#insn-00bfb954)

~~~json
{
  "source": "00bfb954",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb958`](#insn-00bfb958)

~~~json
{
  "source": "00bfb958",
  "target": "00bfb944",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb95c`](#insn-00bfb95c)

~~~json
{
  "source": "00bfb95c",
  "target": "00bfb970",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb974`](#insn-00bfb974)

~~~json
{
  "source": "00bfb974",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb978`](#insn-00bfb978)

~~~json
{
  "source": "00bfb978",
  "target": "00bfb948",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb980`](#insn-00bfb980)

~~~json
{
  "source": "00bfb980",
  "target": "00c58730",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb988`](#insn-00bfb988)

~~~json
{
  "source": "00bfb988",
  "target": "00c53ffc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
