# 00bfed1c

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b822d4`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b82/00b822d4.md) · 移動量 `+0x7ca48`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0072.md#compare-859a2bfdbed6bbffb809aa03a9475ca7)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bff144`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bff/00bff144.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0087.md#compare-074a78d988a47189261e5799f7bdabf1)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfed1c",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEe",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eede71f3e83ba331485f612ff116f353327d0e167094fc8ad6e998bdd360d3c3",
  "source_text_sha256": "eede71f3e83ba331485f612ff116f353327d0e167094fc8ad6e998bdd360d3c3",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfed1c",
        "00bfee47"
      ]
    ],
    "bytes_sha256": "c0c8615b664fd8d522b38c39662bd661f89d7397030e54f5fe19ceb4b2f730cf",
    "instruction_count": 75,
    "instruction_bytes": 300,
    "body_bytes": 300,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c57e60](../00c57/00c57e60.md)
- [00c57e70](../00c57/00c57e70.md)
- [00c57e80](../00c57/00c57e80.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57ea0](../00c57/00c57ea0.md)
- [00c57eb0](../00c57/00c57eb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1574 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEe(undefined8 param_1,long *param_2)

{
  uint uVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  undefined8 uVar5;
  char local_50 [16];
  undefined1 auStack_28 [8];
  
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_(local_50,param_2);
  if (local_50[0] != '\0') {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_28,(long)param_2 + *(long *)(*param_2 + -0x18));
    plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_28,
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b438
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_28);
    lVar4 = (long)param_2 + *(long *)(*param_2 + -0x18);
    uVar5 = *(undefined8 *)(lVar4 + 0x28);
    if (*(int *)(lVar4 + 0x90) == -1) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_28,lVar4);
      plVar3 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_28,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9a830);
      uVar1 = (**(code **)(*plVar3 + 0x38))(plVar3,0x20);
      _ZNSt6__ndk16localeD1Ev(auStack_28);
      *(uint *)(lVar4 + 0x90) = uVar1 & 0xff;
    }
    lVar4 = (**(code **)(*plVar2 + 0x48))(param_1,plVar2,uVar5,lVar4);
    if (lVar4 == 0) {
      lVar4 = (long)param_2 + *(long *)(*param_2 + -0x18);
      _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | 5);
    }
  }
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD2Ev(local_50);
  return param_2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfed1c"></a> `00bfed1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfed20"></a> `00bfed20` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfed24"></a> `00bfed24` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfed28"></a> `00bfed28` | `f7 1b 00 f9` | str x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfed2c"></a> `00bfed2c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfed30"></a> `00bfed30` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfed34"></a> `00bfed34` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfed38"></a> `00bfed38` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfed3c"></a> `00bfed3c` | `e0 03 80 3d` | str q0,[sp] | `FALL_THROUGH`
<a id="insn-00bfed40"></a> `00bfed40` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfed44"></a> `00bfed44` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfed48"></a> `00bfed48` | `46 64 01 94` | bl 0x00c57e60 | `UNCONDITIONAL_CALL`
<a id="insn-00bfed4c"></a> `00bfed4c` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfed50"></a> `00bfed50` | `88 06 00 34` | cbz w8,0x00bfee20 | `CONDITIONAL_JUMP`
<a id="insn-00bfed54"></a> `00bfed54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfed58"></a> `00bfed58` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfed5c"></a> `00bfed5c` | `a8 63 00 91` | add x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bfed60"></a> `00bfed60` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfed64"></a> `00bfed64` | `43 64 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfed68"></a> `00bfed68` | `e1 04 00 b0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfed6c"></a> `00bfed6c` | `a0 63 00 91` | add x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bfed70"></a> `00bfed70` | `21 1c 42 f9` | ldr x1,[x1, #0x438] | `FALL_THROUGH`
<a id="insn-00bfed74"></a> `00bfed74` | `43 64 01 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bfed78"></a> `00bfed78` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfed7c"></a> `00bfed7c` | `a0 63 00 91` | add x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bfed80"></a> `00bfed80` | `44 64 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfed84"></a> `00bfed84` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfed88"></a> `00bfed88` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfed8c"></a> `00bfed8c` | `62 02 08 8b` | add x2,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfed90"></a> `00bfed90` | `43 90 40 b9` | ldr w3,[x2, #0x90] | `FALL_THROUGH`
<a id="insn-00bfed94"></a> `00bfed94` | `55 14 40 f9` | ldr x21,[x2, #0x28] | `FALL_THROUGH`
<a id="insn-00bfed98"></a> `00bfed98` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bfed9c"></a> `00bfed9c` | `61 02 00 54` | b.ne 0x00bfede8 | `CONDITIONAL_JUMP`
<a id="insn-00bfeda0"></a> `00bfeda0` | `a8 63 00 91` | add x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bfeda4"></a> `00bfeda4` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bfeda8"></a> `00bfeda8` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bfedac"></a> `00bfedac` | `31 64 01 94` | bl 0x00c57e70 | `UNCONDITIONAL_CALL`
<a id="insn-00bfedb0"></a> `00bfedb0` | `e1 04 00 90` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00bfedb4"></a> `00bfedb4` | `a0 63 00 91` | add x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bfedb8"></a> `00bfedb8` | `21 18 44 f9` | ldr x1,[x1, #0x830] | `FALL_THROUGH`
<a id="insn-00bfedbc"></a> `00bfedbc` | `31 64 01 94` | bl 0x00c57e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bfedc0"></a> `00bfedc0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfedc4"></a> `00bfedc4` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfedc8"></a> `00bfedc8` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bfedcc"></a> `00bfedcc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfedd0"></a> `00bfedd0` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bfedd4"></a> `00bfedd4` | `a0 63 00 91` | add x0,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bfedd8"></a> `00bfedd8` | `2e 64 01 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeddc"></a> `00bfeddc` | `c3 1e 00 12` | and w3,w22,#0xff | `FALL_THROUGH`
<a id="insn-00bfede0"></a> `00bfede0` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00bfede4"></a> `00bfede4` | `e3 92 00 b9` | str w3,[x23, #0x90] | `FALL_THROUGH`
<a id="insn-00bfede8"></a> `00bfede8` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bfedec"></a> `00bfedec` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00bfedf0"></a> `00bfedf0` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00bfedf4"></a> `00bfedf4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfedf8"></a> `00bfedf8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bfedfc"></a> `00bfedfc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfee00"></a> `00bfee00` | `00 01 00 b5` | cbnz x0,0x00bfee20 | `CONDITIONAL_JUMP`
<a id="insn-00bfee04"></a> `00bfee04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfee08"></a> `00bfee08` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bfee0c"></a> `00bfee0c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfee10"></a> `00bfee10` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfee14"></a> `00bfee14` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfee18"></a> `00bfee18` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00bfee1c"></a> `00bfee1c` | `21 64 01 94` | bl 0x00c57ea0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfee20"></a> `00bfee20` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bfee24"></a> `00bfee24` | `23 64 01 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfee28"></a> `00bfee28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfee2c"></a> `00bfee2c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfee30"></a> `00bfee30` | `f7 1b 40 f9` | ldr x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfee34"></a> `00bfee34` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfee38"></a> `00bfee38` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfee3c"></a> `00bfee3c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfee40"></a> `00bfee40` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfee44"></a> `00bfee44` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfed1c`](#insn-00bfed1c) 範囲 `[['00bfed1c', '00bfed53']]`
  - `CONDITIONAL_JUMP` [`00bfed50`](#insn-00bfed50) → [`00bfee20`](#insn-00bfee20)
  - `FALL_THROUGH` [`00bfed50`](#insn-00bfed50) → [`00bfed54`](#insn-00bfed54)
- ブロック [`00bfed54`](#insn-00bfed54) 範囲 `[['00bfed54', '00bfed9f']]`
  - `CONDITIONAL_JUMP` [`00bfed9c`](#insn-00bfed9c) → [`00bfede8`](#insn-00bfede8)
  - `FALL_THROUGH` [`00bfed9c`](#insn-00bfed9c) → [`00bfeda0`](#insn-00bfeda0)
- ブロック [`00bfeda0`](#insn-00bfeda0) 範囲 `[['00bfeda0', '00bfede7']]`
  - `FALL_THROUGH` [`00bfede4`](#insn-00bfede4) → [`00bfede8`](#insn-00bfede8)
- ブロック [`00bfede8`](#insn-00bfede8) 範囲 `[['00bfede8', '00bfee03']]`
  - `CONDITIONAL_JUMP` [`00bfee00`](#insn-00bfee00) → [`00bfee20`](#insn-00bfee20)
  - `FALL_THROUGH` [`00bfee00`](#insn-00bfee00) → [`00bfee04`](#insn-00bfee04)
- ブロック [`00bfee04`](#insn-00bfee04) 範囲 `[['00bfee04', '00bfee1f']]`
  - `FALL_THROUGH` [`00bfee1c`](#insn-00bfee1c) → [`00bfee20`](#insn-00bfee20)
- ブロック [`00bfee20`](#insn-00bfee20) 範囲 `[['00bfee20', '00bfee47']]`

## 命令位置別の参照

- [`00bfed24`](#insn-00bfed24) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfed28`](#insn-00bfed28) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfed2c`](#insn-00bfed2c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfed30`](#insn-00bfed30) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfed3c`](#insn-00bfed3c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfed48`](#insn-00bfed48) → [`00c57e60`](../00c57/00c57e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e60` · 推定シンボル `None` · 推定型 `None`
- [`00bfed4c`](#insn-00bfed4c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfed50`](#insn-00bfed50) → [`00bfee20`](#insn-00bfee20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfed64`](#insn-00bfed64) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bfed70`](#insn-00bfed70) → `00c9b438`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfed70`](#insn-00bfed70) → `01127798`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfed74`](#insn-00bfed74) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bfed80`](#insn-00bfed80) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfed9c`](#insn-00bfed9c) → [`00bfede8`](#insn-00bfede8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfedac`](#insn-00bfedac) → [`00c57e70`](../00c57/00c57e70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e70` · 推定シンボル `None` · 推定型 `None`
- [`00bfedb8`](#insn-00bfedb8) → `00c9a830`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfedb8`](#insn-00bfedb8) → `01127a18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bfedbc`](#insn-00bfedbc) → [`00c57e80`](../00c57/00c57e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e80` · 推定シンボル `None` · 推定型 `None`
- [`00bfedd8`](#insn-00bfedd8) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bfedf0`](#insn-00bfedf0) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfee00`](#insn-00bfee00) → [`00bfee20`](#insn-00bfee20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfee1c`](#insn-00bfee1c) → [`00c57ea0`](../00c57/00c57ea0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ea0` · 推定シンボル `None` · 推定型 `None`
- [`00bfee24`](#insn-00bfee24) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bfee2c`](#insn-00bfee2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfee30`](#insn-00bfee30) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfee34`](#insn-00bfee34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfee38`](#insn-00bfee38) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfed24`](#insn-00bfed24)

~~~json
{
  "source": "00bfed24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfed28`](#insn-00bfed28)

~~~json
{
  "source": "00bfed28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfed2c`](#insn-00bfed2c)

~~~json
{
  "source": "00bfed2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfed30`](#insn-00bfed30)

~~~json
{
  "source": "00bfed30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfed3c`](#insn-00bfed3c)

~~~json
{
  "source": "00bfed3c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfed48`](#insn-00bfed48)

~~~json
{
  "source": "00bfed48",
  "target": "00c57e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed4c`](#insn-00bfed4c)

~~~json
{
  "source": "00bfed4c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfed50`](#insn-00bfed50)

~~~json
{
  "source": "00bfed50",
  "target": "00bfee20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfed64`](#insn-00bfed64)

~~~json
{
  "source": "00bfed64",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed70`](#insn-00bfed70)

~~~json
{
  "source": "00bfed70",
  "target": "00c9b438",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b438",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfed70`](#insn-00bfed70)

~~~json
{
  "source": "00bfed70",
  "target": "01127798",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127798",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfed74`](#insn-00bfed74)

~~~json
{
  "source": "00bfed74",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed80`](#insn-00bfed80)

~~~json
{
  "source": "00bfed80",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed9c`](#insn-00bfed9c)

~~~json
{
  "source": "00bfed9c",
  "target": "00bfede8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfedac`](#insn-00bfedac)

~~~json
{
  "source": "00bfedac",
  "target": "00c57e70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfedb8`](#insn-00bfedb8)

~~~json
{
  "source": "00bfedb8",
  "target": "00c9a830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfedb8`](#insn-00bfedb8)

~~~json
{
  "source": "00bfedb8",
  "target": "01127a18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127a18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfedbc`](#insn-00bfedbc)

~~~json
{
  "source": "00bfedbc",
  "target": "00c57e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfedd8`](#insn-00bfedd8)

~~~json
{
  "source": "00bfedd8",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfedf0`](#insn-00bfedf0)

~~~json
{
  "source": "00bfedf0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfee00`](#insn-00bfee00)

~~~json
{
  "source": "00bfee00",
  "target": "00bfee20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfee1c`](#insn-00bfee1c)

~~~json
{
  "source": "00bfee1c",
  "target": "00c57ea0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfee24`](#insn-00bfee24)

~~~json
{
  "source": "00bfee24",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfee2c`](#insn-00bfee2c)

~~~json
{
  "source": "00bfee2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfee30`](#insn-00bfee30)

~~~json
{
  "source": "00bfee30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfee34`](#insn-00bfee34)

~~~json
{
  "source": "00bfee34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfee38`](#insn-00bfee38)

~~~json
{
  "source": "00bfee38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
