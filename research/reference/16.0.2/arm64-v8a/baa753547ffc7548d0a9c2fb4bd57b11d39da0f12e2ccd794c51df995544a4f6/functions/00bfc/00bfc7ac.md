# 00bfc7ac

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfc710`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfc/00bfc710.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-f43a8d005cfa4ebaf90c0ce52d8192ec)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfd7a0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfd/00bfd7a0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-a7810de8c8ccc945ad77c63d21b01c22)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfc7ac",
  "name": "FUN_00bfc7ac",
  "size": 256,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d72e4a7d80a0f004a9cb97ce209d4ac37a963160d1d82decd0cda36a8d3be210",
  "source_text_sha256": "d72e4a7d80a0f004a9cb97ce209d4ac37a963160d1d82decd0cda36a8d3be210",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfc7ac",
        "00bfc8ab"
      ]
    ],
    "bytes_sha256": "885cbac7341855b35f9007ed39d5caf55063336fccccf628bddb9061e7300895",
    "instruction_count": 64,
    "instruction_bytes": 256,
    "body_bytes": 256,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [00bfc7a4](../00bfc/00bfc7a4.md)

## 呼び出し先

- [00c58340](../00c58/00c58340.md)
- [00c58350](../00c58/00c58350.md)
- [00c58360](../00c58/00c58360.md)
- [00c58370](../00c58/00c58370.md)
- [00c59ea0](../00c59/00c59ea0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1282 bytes

~~~c

long * FUN_00bfc7ac(long *param_1,undefined2 *param_2)

{
  long lVar1;
  long *plVar2;
  undefined2 uVar3;
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
  if (local_30 < -0x8000) {
    uVar3 = 0x8000;
  }
  else {
    if (local_30 < 0x8000) {
      *param_2 = (short)local_30;
      goto LAB_00bfc878;
    }
    uVar3 = 0x7fff;
  }
  local_24 = local_24 | 4;
  *param_2 = uVar3;
LAB_00bfc878:
  lVar1 = (long)param_1 + *(long *)(*param_1 + -0x18);
  _ZNSt6__ndk18ios_base5clearEj(lVar1,*(uint *)(lVar1 + 0x20) | local_24);
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfc7ac"></a> `00bfc7ac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfc7b0"></a> `00bfc7b0` | `ff 03 01 d1` | sub sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfc7b4"></a> `00bfc7b4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc7b8"></a> `00bfc7b8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfc7bc"></a> `00bfc7bc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfc7c0"></a> `00bfc7c0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfc7c4"></a> `00bfc7c4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfc7c8"></a> `00bfc7c8` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfc7cc"></a> `00bfc7cc` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfc7d0"></a> `00bfc7d0` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00bfc7d4"></a> `00bfc7d4` | `bf c3 1f b8` | stur wzr,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfc7d8"></a> `00bfc7d8` | `b2 75 01 94` | bl 0x00c59ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfc7dc"></a> `00bfc7dc` | `a8 83 5f 38` | ldurb w8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bfc7e0"></a> `00bfc7e0` | `a8 05 00 34` | cbz w8,0x00bfc894 | `CONDITIONAL_JUMP`
<a id="insn-00bfc7e4"></a> `00bfc7e4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfc7e8"></a> `00bfc7e8` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfc7ec"></a> `00bfc7ec` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfc7f0"></a> `00bfc7f0` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfc7f4"></a> `00bfc7f4` | `d3 6e 01 94` | bl 0x00c58340 | `UNCONDITIONAL_CALL`
<a id="insn-00bfc7f8"></a> `00bfc7f8` | `e1 04 00 f0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfc7fc"></a> `00bfc7fc` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfc800"></a> `00bfc800` | `21 f0 45 f9` | ldr x1,[x1, #0xbe0] | `FALL_THROUGH`
<a id="insn-00bfc804"></a> `00bfc804` | `d3 6e 01 94` | bl 0x00c58350 | `UNCONDITIONAL_CALL`
<a id="insn-00bfc808"></a> `00bfc808` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfc80c"></a> `00bfc80c` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00bfc810"></a> `00bfc810` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfc814"></a> `00bfc814` | `63 02 08 8b` | add x3,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfc818"></a> `00bfc818` | `28 11 40 f9` | ldr x8,[x9, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc81c"></a> `00bfc81c` | `61 14 40 f9` | ldr x1,[x3, #0x28] | `FALL_THROUGH`
<a id="insn-00bfc820"></a> `00bfc820` | `a4 13 00 d1` | sub x4,x29,#0x4 | `FALL_THROUGH`
<a id="insn-00bfc824"></a> `00bfc824` | `e5 43 00 91` | add x5,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfc828"></a> `00bfc828` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bfc82c"></a> `00bfc82c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfc830"></a> `00bfc830` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfc834"></a> `00bfc834` | `cb 6e 01 94` | bl 0x00c58360 | `UNCONDITIONAL_CALL`
<a id="insn-00bfc838"></a> `00bfc838` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfc83c"></a> `00bfc83c` | `09 00 90 92` | mov x9,#-0x8001 | `FALL_THROUGH`
<a id="insn-00bfc840"></a> `00bfc840` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bfc844"></a> `00bfc844` | `8c 00 00 54` | b.gt 0x00bfc854 | `CONDITIONAL_JUMP`
<a id="insn-00bfc848"></a> `00bfc848` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfc84c"></a> `00bfc84c` | `09 00 90 52` | mov w9,#0x8000 | `FALL_THROUGH`
<a id="insn-00bfc850"></a> `00bfc850` | `05 00 00 14` | b 0x00bfc864 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfc854"></a> `00bfc854` | `1f 21 40 f1` | cmp x8,#0x8, LSL #12 | `FALL_THROUGH`
<a id="insn-00bfc858"></a> `00bfc858` | `eb 00 00 54` | b.lt 0x00bfc874 | `CONDITIONAL_JUMP`
<a id="insn-00bfc85c"></a> `00bfc85c` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfc860"></a> `00bfc860` | `e9 ff 8f 52` | mov w9,#0x7fff | `FALL_THROUGH`
<a id="insn-00bfc864"></a> `00bfc864` | `08 01 1e 32` | orr w8,w8,#0x4 | `FALL_THROUGH`
<a id="insn-00bfc868"></a> `00bfc868` | `a8 c3 1f b8` | stur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfc86c"></a> `00bfc86c` | `89 02 00 79` | strh w9,[x20] | `FALL_THROUGH`
<a id="insn-00bfc870"></a> `00bfc870` | `02 00 00 14` | b 0x00bfc878 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfc874"></a> `00bfc874` | `88 02 00 79` | strh w8,[x20] | `FALL_THROUGH`
<a id="insn-00bfc878"></a> `00bfc878` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfc87c"></a> `00bfc87c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfc880"></a> `00bfc880` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfc884"></a> `00bfc884` | `a8 c3 5f b8` | ldur w8,[x29, #-0x4] | `FALL_THROUGH`
<a id="insn-00bfc888"></a> `00bfc888` | `09 20 40 b9` | ldr w9,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc88c"></a> `00bfc88c` | `21 01 08 2a` | orr w1,w9,w8 | `FALL_THROUGH`
<a id="insn-00bfc890"></a> `00bfc890` | `b8 6e 01 94` | bl 0x00c58370 | `UNCONDITIONAL_CALL`
<a id="insn-00bfc894"></a> `00bfc894` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfc898"></a> `00bfc898` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfc89c"></a> `00bfc89c` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfc8a0"></a> `00bfc8a0` | `ff 03 01 91` | add sp,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bfc8a4"></a> `00bfc8a4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfc8a8"></a> `00bfc8a8` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfc7ac`](#insn-00bfc7ac) 範囲 `[['00bfc7ac', '00bfc7e3']]`
  - `CONDITIONAL_JUMP` [`00bfc7e0`](#insn-00bfc7e0) → [`00bfc894`](#insn-00bfc894)
  - `FALL_THROUGH` [`00bfc7e0`](#insn-00bfc7e0) → [`00bfc7e4`](#insn-00bfc7e4)
- ブロック [`00bfc7e4`](#insn-00bfc7e4) 範囲 `[['00bfc7e4', '00bfc847']]`
  - `CONDITIONAL_JUMP` [`00bfc844`](#insn-00bfc844) → [`00bfc854`](#insn-00bfc854)
  - `FALL_THROUGH` [`00bfc844`](#insn-00bfc844) → [`00bfc848`](#insn-00bfc848)
- ブロック [`00bfc848`](#insn-00bfc848) 範囲 `[['00bfc848', '00bfc853']]`
  - `UNCONDITIONAL_JUMP` [`00bfc850`](#insn-00bfc850) → [`00bfc864`](#insn-00bfc864)
- ブロック [`00bfc854`](#insn-00bfc854) 範囲 `[['00bfc854', '00bfc85b']]`
  - `CONDITIONAL_JUMP` [`00bfc858`](#insn-00bfc858) → [`00bfc874`](#insn-00bfc874)
  - `FALL_THROUGH` [`00bfc858`](#insn-00bfc858) → [`00bfc85c`](#insn-00bfc85c)
- ブロック [`00bfc85c`](#insn-00bfc85c) 範囲 `[['00bfc85c', '00bfc863']]`
  - `FALL_THROUGH` [`00bfc860`](#insn-00bfc860) → [`00bfc864`](#insn-00bfc864)
- ブロック [`00bfc864`](#insn-00bfc864) 範囲 `[['00bfc864', '00bfc873']]`
  - `UNCONDITIONAL_JUMP` [`00bfc870`](#insn-00bfc870) → [`00bfc878`](#insn-00bfc878)
- ブロック [`00bfc874`](#insn-00bfc874) 範囲 `[['00bfc874', '00bfc877']]`
  - `FALL_THROUGH` [`00bfc874`](#insn-00bfc874) → [`00bfc878`](#insn-00bfc878)
- ブロック [`00bfc878`](#insn-00bfc878) 範囲 `[['00bfc878', '00bfc893']]`
  - `FALL_THROUGH` [`00bfc890`](#insn-00bfc890) → [`00bfc894`](#insn-00bfc894)
- ブロック [`00bfc894`](#insn-00bfc894) 範囲 `[['00bfc894', '00bfc8ab']]`

## 命令位置別の参照

- [`00bfc7b4`](#insn-00bfc7b4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc7b8`](#insn-00bfc7b8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc7d4`](#insn-00bfc7d4) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc7d8`](#insn-00bfc7d8) → [`00c59ea0`](../00c59/00c59ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfc7dc`](#insn-00bfc7dc) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc7e0`](#insn-00bfc7e0) → [`00bfc894`](#insn-00bfc894) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc7f4`](#insn-00bfc7f4) → [`00c58340`](../00c58/00c58340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58340` · 推定シンボル `None` · 推定型 `None`
- [`00bfc800`](#insn-00bfc800) → `00c9bbe0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfc800`](#insn-00bfc800) → `01127c78`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_getIcNS_19istreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfc804`](#insn-00bfc804) → [`00c58350`](../00c58/00c58350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58350` · 推定シンボル `None` · 推定型 `None`
- [`00bfc834`](#insn-00bfc834) → [`00c58360`](../00c58/00c58360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58360` · 推定シンボル `None` · 推定型 `None`
- [`00bfc838`](#insn-00bfc838) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc844`](#insn-00bfc844) → [`00bfc854`](#insn-00bfc854) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc848`](#insn-00bfc848) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc850`](#insn-00bfc850) → [`00bfc864`](#insn-00bfc864) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc858`](#insn-00bfc858) → [`00bfc874`](#insn-00bfc874) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc85c`](#insn-00bfc85c) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc868`](#insn-00bfc868) → `Stack[-0x24]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc870`](#insn-00bfc870) → [`00bfc878`](#insn-00bfc878) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc884`](#insn-00bfc884) → `Stack[-0x24]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc890`](#insn-00bfc890) → [`00c58370`](../00c58/00c58370.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58370` · 推定シンボル `None` · 推定型 `None`
- [`00bfc898`](#insn-00bfc898) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfc89c`](#insn-00bfc89c) → `Stack[-0x20]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfc7b4`](#insn-00bfc7b4)

~~~json
{
  "source": "00bfc7b4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc7b8`](#insn-00bfc7b8)

~~~json
{
  "source": "00bfc7b8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc7d4`](#insn-00bfc7d4)

~~~json
{
  "source": "00bfc7d4",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc7d8`](#insn-00bfc7d8)

~~~json
{
  "source": "00bfc7d8",
  "target": "00c59ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfc7dc`](#insn-00bfc7dc)

~~~json
{
  "source": "00bfc7dc",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc7e0`](#insn-00bfc7e0)

~~~json
{
  "source": "00bfc7e0",
  "target": "00bfc894",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc7f4`](#insn-00bfc7f4)

~~~json
{
  "source": "00bfc7f4",
  "target": "00c58340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfc800`](#insn-00bfc800)

~~~json
{
  "source": "00bfc800",
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
- 参照命令 [`00bfc800`](#insn-00bfc800)

~~~json
{
  "source": "00bfc800",
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
- 参照命令 [`00bfc804`](#insn-00bfc804)

~~~json
{
  "source": "00bfc804",
  "target": "00c58350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfc834`](#insn-00bfc834)

~~~json
{
  "source": "00bfc834",
  "target": "00c58360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfc838`](#insn-00bfc838)

~~~json
{
  "source": "00bfc838",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc844`](#insn-00bfc844)

~~~json
{
  "source": "00bfc844",
  "target": "00bfc854",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc848`](#insn-00bfc848)

~~~json
{
  "source": "00bfc848",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc850`](#insn-00bfc850)

~~~json
{
  "source": "00bfc850",
  "target": "00bfc864",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc858`](#insn-00bfc858)

~~~json
{
  "source": "00bfc858",
  "target": "00bfc874",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc85c`](#insn-00bfc85c)

~~~json
{
  "source": "00bfc85c",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc868`](#insn-00bfc868)

~~~json
{
  "source": "00bfc868",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc870`](#insn-00bfc870)

~~~json
{
  "source": "00bfc870",
  "target": "00bfc878",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc884`](#insn-00bfc884)

~~~json
{
  "source": "00bfc884",
  "target": "Stack[-0x24]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc890`](#insn-00bfc890)

~~~json
{
  "source": "00bfc890",
  "target": "00c58370",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfc898`](#insn-00bfc898)

~~~json
{
  "source": "00bfc898",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfc89c`](#insn-00bfc89c)

~~~json
{
  "source": "00bfc89c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
