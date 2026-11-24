# 00bfca5c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfc9c0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc9c0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-35b16e94d3d1f909cea4456b2fe402f4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfda50`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfda50.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-a7658b4cb10fb840f4cc222aae451b2c)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfca5c",
  "name": "FUN_00bfca5c",
  "size": 260,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cd26bf10f0cfc0cc890e92bc0cd8866892b8f82f4682c034886d6b567a052ab9",
  "source_text_sha256": "cd26bf10f0cfc0cc890e92bc0cd8866892b8f82f4682c034886d6b567a052ab9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfca5c",
        "00bfcb5f"
      ]
    ],
    "bytes_sha256": "1ba232b6ed4fb837da156b0e31166989b88810a251eb9e13c14b13829c66fbe9",
    "instruction_count": 65,
    "instruction_bytes": 260,
    "body_bytes": 260,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bfca54](../00bfc/00bfca54.md)

## 呼び出し先

- [00c58340](../00c58/00c58340.md)
- [00c58350](../00c58/00c58350.md)
- [00c58360](../00c58/00c58360.md)
- [00c58370](../00c58/00c58370.md)
- [00c59ea0](../00c59/00c59ea0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1296 bytes

~~~c

long * FUN_00bfca5c(long *param_1,undefined4 *param_2)

{
  long lVar1;
  long *plVar2;
  undefined4 uVar3;
  undefined1 auStack_38 [8];
  long local_30;
  char local_28 [4];
  uint local_24;
  
  local_24 = 0;
  _ZNSt6__ndk113basic_istreamIcNS_11char_traitsIcEEE6sentryC1ERS3_b(local_28,param_1,0);
  if (local_28[0] == '\0') {
    return param_1;
  }
  _ZNKSt6__ndk18ios_base6getlocEv(auStack_38,(long)param_1 + *(long *)(*param_1 + -0x18));
  plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                             (auStack_38,
                              PTR__ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9bbe0
                             );
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  (**(code **)(*plVar2 + 0x20))(plVar2,*(undefined8 *)(lVar1 + 0x28),0,lVar1,&local_24,&local_30);
  _ZNSt6__ndk16localeD1Ev(auStack_38);
  if (local_30 < -0x80000000) {
    uVar3 = 0x80000000;
  }
  else {
    if (local_30 < 0x80000000) {
      *param_2 = (int)local_30;
      goto LAB_00bfcb2c;
    }
    uVar3 = 0x7fffffff;
  }
  local_24 = local_24 | 4;
  *param_2 = uVar3;
LAB_00bfcb2c:
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | local_24);
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfca5c"></a> `00bfca5c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfca60"></a> `00bfca60` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfca64"></a> `00bfca64` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfca68"></a> `00bfca68` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfca6c"></a> `00bfca6c` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfca70"></a> `00bfca70` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfca74"></a> `00bfca74` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfca78"></a> `00bfca78` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfca7c"></a> `00bfca7c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfca80"></a> `00bfca80` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bfca84"></a> `00bfca84` | `bf c3 1f b8` | stur wzr,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfca88"></a> `00bfca88` | `06 75 01 94` | bl 0x00c59ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfca8c"></a> `00bfca8c` | `a8 83 5f 38` | ldurb w8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bfca90"></a> `00bfca90` | `c8 05 00 34` | cbz w8,0x00bfcb48 | `CONDITIONAL_JUMP`
<a id="insn-00bfca94"></a> `00bfca94` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfca98"></a> `00bfca98` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfca9c"></a> `00bfca9c` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcaa0"></a> `00bfcaa0` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfcaa4"></a> `00bfcaa4` | `27 6e 01 94` | bl 0x00c58340 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcaa8"></a> `00bfcaa8` | `e1 04 00 f0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfcaac"></a> `00bfcaac` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcab0"></a> `00bfcab0` | `21 f0 45 f9` | ldr x1,[x1, #0xbe0] | `FALL_THROUGH`
<a id="insn-00bfcab4"></a> `00bfcab4` | `27 6e 01 94` | bl 0x00c58350 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcab8"></a> `00bfcab8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcabc"></a> `00bfcabc` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bfcac0"></a> `00bfcac0` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcac4"></a> `00bfcac4` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfcac8"></a> `00bfcac8` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcacc"></a> `00bfcacc` | `61 14 40 f9` | ldr x1,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00bfcad0"></a> `00bfcad0` | `a4 13 00 d1` | sub x4,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfcad4"></a> `00bfcad4` | `e5 43 00 91` | add x5,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfcad8"></a> `00bfcad8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bfcadc"></a> `00bfcadc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfcae0"></a> `00bfcae0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfcae4"></a> `00bfcae4` | `1f 6e 01 94` | bl 0x00c58360 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcae8"></a> `00bfcae8` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfcaec"></a> `00bfcaec` | `09 00 b0 92` | mov x9,#-0x80000001 | `FALL_THROUGH`
<a id="insn-00bfcaf0"></a> `00bfcaf0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfcaf4"></a> `00bfcaf4` | `8c 00 00 54` | b.gt 0x00bfcb04 | `CONDITIONAL_JUMP`
<a id="insn-00bfcaf8"></a> `00bfcaf8` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcafc"></a> `00bfcafc` | `09 00 b0 52` | mov w9,#0x80000000 | `FALL_THROUGH`
<a id="insn-00bfcb00"></a> `00bfcb00` | `06 00 00 14` | b 0x00bfcb18 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfcb04"></a> `00bfcb04` | `09 00 b0 52` | mov w9,#0x80000000 | `FALL_THROUGH`
<a id="insn-00bfcb08"></a> `00bfcb08` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfcb0c"></a> `00bfcb0c` | `eb 00 00 54` | b.lt 0x00bfcb28 | `CONDITIONAL_JUMP`
<a id="insn-00bfcb10"></a> `00bfcb10` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcb14"></a> `00bfcb14` | `09 00 b0 12` | mov w9,#0x7fffffff | `FALL_THROUGH`
<a id="insn-00bfcb18"></a> `00bfcb18` | `08 01 1e 32` | orr w8,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfcb1c"></a> `00bfcb1c` | `a8 c3 1f b8` | stur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcb20"></a> `00bfcb20` | `89 02 00 b9` | str w9,[x20] | `FALL_THROUGH`
<a id="insn-00bfcb24"></a> `00bfcb24` | `02 00 00 14` | b 0x00bfcb2c | `UNCONDITIONAL_JUMP`
<a id="insn-00bfcb28"></a> `00bfcb28` | `88 02 00 b9` | str w8,[x20] | `FALL_THROUGH`
<a id="insn-00bfcb2c"></a> `00bfcb2c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfcb30"></a> `00bfcb30` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfcb34"></a> `00bfcb34` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfcb38"></a> `00bfcb38` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfcb3c"></a> `00bfcb3c` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcb40"></a> `00bfcb40` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfcb44"></a> `00bfcb44` | `0b 6e 01 94` | bl 0x00c58370 | `UNCONDITIONAL_CALL`
<a id="insn-00bfcb48"></a> `00bfcb48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfcb4c"></a> `00bfcb4c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfcb50"></a> `00bfcb50` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfcb54"></a> `00bfcb54` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfcb58"></a> `00bfcb58` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfcb5c"></a> `00bfcb5c` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfca5c`](#insn-00bfca5c) 範囲 `[['00bfca5c', '00bfca93']]`
  - `CONDITIONAL_JUMP` [`00bfca90`](#insn-00bfca90) → [`00bfcb48`](#insn-00bfcb48)
  - `FALL_THROUGH` [`00bfca90`](#insn-00bfca90) → [`00bfca94`](#insn-00bfca94)
- ブロック [`00bfca94`](#insn-00bfca94) 範囲 `[['00bfca94', '00bfcaf7']]`
  - `CONDITIONAL_JUMP` [`00bfcaf4`](#insn-00bfcaf4) → [`00bfcb04`](#insn-00bfcb04)
  - `FALL_THROUGH` [`00bfcaf4`](#insn-00bfcaf4) → [`00bfcaf8`](#insn-00bfcaf8)
- ブロック [`00bfcaf8`](#insn-00bfcaf8) 範囲 `[['00bfcaf8', '00bfcb03']]`
  - `UNCONDITIONAL_JUMP` [`00bfcb00`](#insn-00bfcb00) → [`00bfcb18`](#insn-00bfcb18)
- ブロック [`00bfcb04`](#insn-00bfcb04) 範囲 `[['00bfcb04', '00bfcb0f']]`
  - `CONDITIONAL_JUMP` [`00bfcb0c`](#insn-00bfcb0c) → [`00bfcb28`](#insn-00bfcb28)
  - `FALL_THROUGH` [`00bfcb0c`](#insn-00bfcb0c) → [`00bfcb10`](#insn-00bfcb10)
- ブロック [`00bfcb10`](#insn-00bfcb10) 範囲 `[['00bfcb10', '00bfcb17']]`
  - `FALL_THROUGH` [`00bfcb14`](#insn-00bfcb14) → [`00bfcb18`](#insn-00bfcb18)
- ブロック [`00bfcb18`](#insn-00bfcb18) 範囲 `[['00bfcb18', '00bfcb27']]`
  - `UNCONDITIONAL_JUMP` [`00bfcb24`](#insn-00bfcb24) → [`00bfcb2c`](#insn-00bfcb2c)
- ブロック [`00bfcb28`](#insn-00bfcb28) 範囲 `[['00bfcb28', '00bfcb2b']]`
  - `FALL_THROUGH` [`00bfcb28`](#insn-00bfcb28) → [`00bfcb2c`](#insn-00bfcb2c)
- ブロック [`00bfcb2c`](#insn-00bfcb2c) 範囲 `[['00bfcb2c', '00bfcb47']]`
  - `FALL_THROUGH` [`00bfcb44`](#insn-00bfcb44) → [`00bfcb48`](#insn-00bfcb48)
- ブロック [`00bfcb48`](#insn-00bfcb48) 範囲 `[['00bfcb48', '00bfcb5f']]`

## 命令位置別の参照

- [`00bfca64`](#insn-00bfca64) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfca68`](#insn-00bfca68) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfca84`](#insn-00bfca84) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfca88`](#insn-00bfca88) → [`00c59ea0`](../00c59/00c59ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfca8c`](#insn-00bfca8c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfca90`](#insn-00bfca90) → [`00bfcb48`](#insn-00bfcb48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcaa4`](#insn-00bfcaa4) → [`00c58340`](../00c58/00c58340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58340` · 推定シンボル `None` · 推定型 `None`
- [`00bfcab0`](#insn-00bfcab0) → `00c9bbe0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfcab0`](#insn-00bfcab0) → `01127c78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfcab4`](#insn-00bfcab4) → [`00c58350`](../00c58/00c58350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58350` · 推定シンボル `None` · 推定型 `None`
- [`00bfcae4`](#insn-00bfcae4) → [`00c58360`](../00c58/00c58360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58360` · 推定シンボル `None` · 推定型 `None`
- [`00bfcae8`](#insn-00bfcae8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcaf4`](#insn-00bfcaf4) → [`00bfcb04`](#insn-00bfcb04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcaf8`](#insn-00bfcaf8) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb00`](#insn-00bfcb00) → [`00bfcb18`](#insn-00bfcb18) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb0c`](#insn-00bfcb0c) → [`00bfcb28`](#insn-00bfcb28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb10`](#insn-00bfcb10) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb1c`](#insn-00bfcb1c) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb24`](#insn-00bfcb24) → [`00bfcb2c`](#insn-00bfcb2c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb38`](#insn-00bfcb38) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb44`](#insn-00bfcb44) → [`00c58370`](../00c58/00c58370.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58370` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb4c`](#insn-00bfcb4c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfcb50`](#insn-00bfcb50) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfca64`](#insn-00bfca64)

~~~json
{
  "source": "00bfca64",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfca68`](#insn-00bfca68)

~~~json
{
  "source": "00bfca68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfca84`](#insn-00bfca84)

~~~json
{
  "source": "00bfca84",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfca88`](#insn-00bfca88)

~~~json
{
  "source": "00bfca88",
  "target": "00c59ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfca8c`](#insn-00bfca8c)

~~~json
{
  "source": "00bfca8c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfca90`](#insn-00bfca90)

~~~json
{
  "source": "00bfca90",
  "target": "00bfcb48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcaa4`](#insn-00bfcaa4)

~~~json
{
  "source": "00bfcaa4",
  "target": "00c58340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcab0`](#insn-00bfcab0)

~~~json
{
  "source": "00bfcab0",
  "target": "00c9bbe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bbe0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfcab0`](#insn-00bfcab0)

~~~json
{
  "source": "00bfcab0",
  "target": "01127c78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c78",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfcab4`](#insn-00bfcab4)

~~~json
{
  "source": "00bfcab4",
  "target": "00c58350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcae4`](#insn-00bfcae4)

~~~json
{
  "source": "00bfcae4",
  "target": "00c58360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcae8`](#insn-00bfcae8)

~~~json
{
  "source": "00bfcae8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcaf4`](#insn-00bfcaf4)

~~~json
{
  "source": "00bfcaf4",
  "target": "00bfcb04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcaf8`](#insn-00bfcaf8)

~~~json
{
  "source": "00bfcaf8",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb00`](#insn-00bfcb00)

~~~json
{
  "source": "00bfcb00",
  "target": "00bfcb18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb0c`](#insn-00bfcb0c)

~~~json
{
  "source": "00bfcb0c",
  "target": "00bfcb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb10`](#insn-00bfcb10)

~~~json
{
  "source": "00bfcb10",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb1c`](#insn-00bfcb1c)

~~~json
{
  "source": "00bfcb1c",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb24`](#insn-00bfcb24)

~~~json
{
  "source": "00bfcb24",
  "target": "00bfcb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb38`](#insn-00bfcb38)

~~~json
{
  "source": "00bfcb38",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb44`](#insn-00bfcb44)

~~~json
{
  "source": "00bfcb44",
  "target": "00c58370",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfcb4c`](#insn-00bfcb4c)

~~~json
{
  "source": "00bfcb4c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfcb50`](#insn-00bfcb50)

~~~json
{
  "source": "00bfcb50",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
