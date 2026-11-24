# 00bfec8c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfe864`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe864.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0087.md#compare-0c1f2b401889b49ff33d2006765bb627)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfed28`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfed28.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0087.md#compare-79d25039201b262094ffe76401688478)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfec8c",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEx",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "eae49ef6376055cfa68432bfbe54dacb40d6f4df0b22c224ae95a06b1621de0d",
  "source_text_sha256": "eae49ef6376055cfa68432bfbe54dacb40d6f4df0b22c224ae95a06b1621de0d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfec8c",
        "00bfedb7"
      ]
    ],
    "bytes_sha256": "8169576aa20fa536fac342cf1b09dbb075a16a9108f6a755d2bf787952a24d4b",
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

- [00c58260](../00c58/00c58260.md)
- [00c58270](../00c58/00c58270.md)
- [00c58280](../00c58/00c58280.md)
- [00c58290](../00c58/00c58290.md)
- [00c582a0](../00c58/00c582a0.md)
- [00c582b0](../00c58/00c582b0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1629 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEx(long *param_1,undefined8 param_2)

{
  uint uVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  undefined8 uVar5;
  char local_58 [16];
  undefined1 auStack_48 [8];
  
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_(local_58,param_1);
  if (local_58[0] != '\0') {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,(long)param_1 + *(long *)(*param_1 + -0x18));
    plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_48,
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b838
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_48);
    lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar1 = *(uint *)(lVar4 + 0x90);
    uVar5 = *(undefined8 *)(lVar4 + 0x28);
    if (uVar1 == 0xffffffff) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,lVar4);
      plVar3 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_48,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ac30);
      uVar1 = (**(code **)(*plVar3 + 0x38))(plVar3,0x20);
      _ZNSt6__ndk16localeD1Ev(auStack_48);
      uVar1 = uVar1 & 0xff;
      *(uint *)(lVar4 + 0x90) = uVar1;
    }
    lVar4 = (**(code **)(*plVar2 + 0x28))(plVar2,uVar5,lVar4,uVar1,param_2);
    if (lVar4 == 0) {
      lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
      _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | 5);
    }
  }
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD2Ev(local_58);
  return param_1;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfec8c"></a> `00bfec8c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfec90"></a> `00bfec90` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfec94"></a> `00bfec94` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfec98"></a> `00bfec98` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfec9c"></a> `00bfec9c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfeca0"></a> `00bfeca0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfeca4"></a> `00bfeca4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfeca8"></a> `00bfeca8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfecac"></a> `00bfecac` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfecb0"></a> `00bfecb0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfecb4"></a> `00bfecb4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfecb8"></a> `00bfecb8` | `6a 65 01 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-00bfecbc"></a> `00bfecbc` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfecc0"></a> `00bfecc0` | `88 06 00 34` | cbz w8,0x00bfed90 | `CONDITIONAL_JUMP`
<a id="insn-00bfecc4"></a> `00bfecc4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfecc8"></a> `00bfecc8` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfeccc"></a> `00bfeccc` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfecd0"></a> `00bfecd0` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfecd4"></a> `00bfecd4` | `67 65 01 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00bfecd8"></a> `00bfecd8` | `e1 04 00 b0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfecdc"></a> `00bfecdc` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfece0"></a> `00bfece0` | `21 1c 44 f9` | ldr x1,[x1, #0x838] | `FALL_THROUGH`
<a id="insn-00bfece4"></a> `00bfece4` | `67 65 01 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00bfece8"></a> `00bfece8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bfecec"></a> `00bfecec` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfecf0"></a> `00bfecf0` | `68 65 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00bfecf4"></a> `00bfecf4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfecf8"></a> `00bfecf8` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfecfc"></a> `00bfecfc` | `62 02 08 8b` | add x2,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfed00"></a> `00bfed00` | `43 90 40 b9` | ldr w3,[x2, #0x90] | `FALL_THROUGH`
<a id="insn-00bfed04"></a> `00bfed04` | `56 14 40 f9` | ldr x22,[x2, #0x28] | `FALL_THROUGH`
<a id="insn-00bfed08"></a> `00bfed08` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bfed0c"></a> `00bfed0c` | `61 02 00 54` | b.ne 0x00bfed58 | `CONDITIONAL_JUMP`
<a id="insn-00bfed10"></a> `00bfed10` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfed14"></a> `00bfed14` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bfed18"></a> `00bfed18` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bfed1c"></a> `00bfed1c` | `55 65 01 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00bfed20"></a> `00bfed20` | `e1 04 00 90` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00bfed24"></a> `00bfed24` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfed28"></a> `00bfed28` | `21 18 46 f9` | ldr x1,[x1, #0xc30] | `FALL_THROUGH`
<a id="insn-00bfed2c"></a> `00bfed2c` | `55 65 01 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00bfed30"></a> `00bfed30` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfed34"></a> `00bfed34` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfed38"></a> `00bfed38` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bfed3c"></a> `00bfed3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfed40"></a> `00bfed40` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bfed44"></a> `00bfed44` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfed48"></a> `00bfed48` | `52 65 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00bfed4c"></a> `00bfed4c` | `e3 1e 00 12` | and w3,w23,#0xff | `FALL_THROUGH`
<a id="insn-00bfed50"></a> `00bfed50` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bfed54"></a> `00bfed54` | `03 93 00 b9` | str w3,[x24, #0x90] | `FALL_THROUGH`
<a id="insn-00bfed58"></a> `00bfed58` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bfed5c"></a> `00bfed5c` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00bfed60"></a> `00bfed60` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfed64"></a> `00bfed64` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bfed68"></a> `00bfed68` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-00bfed6c"></a> `00bfed6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfed70"></a> `00bfed70` | `00 01 00 b5` | cbnz x0,0x00bfed90 | `CONDITIONAL_JUMP`
<a id="insn-00bfed74"></a> `00bfed74` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfed78"></a> `00bfed78` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bfed7c"></a> `00bfed7c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfed80"></a> `00bfed80` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfed84"></a> `00bfed84` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfed88"></a> `00bfed88` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00bfed8c"></a> `00bfed8c` | `45 65 01 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfed90"></a> `00bfed90` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfed94"></a> `00bfed94` | `47 65 01 94` | bl 0x00c582b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfed98"></a> `00bfed98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfed9c"></a> `00bfed9c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfeda0"></a> `00bfeda0` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfeda4"></a> `00bfeda4` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfeda8"></a> `00bfeda8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfedac"></a> `00bfedac` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfedb0"></a> `00bfedb0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfedb4"></a> `00bfedb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfec8c`](#insn-00bfec8c) 範囲 `[['00bfec8c', '00bfecc3']]`
  - `CONDITIONAL_JUMP` [`00bfecc0`](#insn-00bfecc0) → [`00bfed90`](#insn-00bfed90)
  - `FALL_THROUGH` [`00bfecc0`](#insn-00bfecc0) → [`00bfecc4`](#insn-00bfecc4)
- ブロック [`00bfecc4`](#insn-00bfecc4) 範囲 `[['00bfecc4', '00bfed0f']]`
  - `CONDITIONAL_JUMP` [`00bfed0c`](#insn-00bfed0c) → [`00bfed58`](#insn-00bfed58)
  - `FALL_THROUGH` [`00bfed0c`](#insn-00bfed0c) → [`00bfed10`](#insn-00bfed10)
- ブロック [`00bfed10`](#insn-00bfed10) 範囲 `[['00bfed10', '00bfed57']]`
  - `FALL_THROUGH` [`00bfed54`](#insn-00bfed54) → [`00bfed58`](#insn-00bfed58)
- ブロック [`00bfed58`](#insn-00bfed58) 範囲 `[['00bfed58', '00bfed73']]`
  - `CONDITIONAL_JUMP` [`00bfed70`](#insn-00bfed70) → [`00bfed90`](#insn-00bfed90)
  - `FALL_THROUGH` [`00bfed70`](#insn-00bfed70) → [`00bfed74`](#insn-00bfed74)
- ブロック [`00bfed74`](#insn-00bfed74) 範囲 `[['00bfed74', '00bfed8f']]`
  - `FALL_THROUGH` [`00bfed8c`](#insn-00bfed8c) → [`00bfed90`](#insn-00bfed90)
- ブロック [`00bfed90`](#insn-00bfed90) 範囲 `[['00bfed90', '00bfedb7']]`

## 命令位置別の参照

- [`00bfec94`](#insn-00bfec94) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec98`](#insn-00bfec98) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfec9c`](#insn-00bfec9c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeca0`](#insn-00bfeca0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfecb8`](#insn-00bfecb8) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`00bfecbc`](#insn-00bfecbc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfecc0`](#insn-00bfecc0) → [`00bfed90`](#insn-00bfed90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfecd4`](#insn-00bfecd4) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00bfece0`](#insn-00bfece0) → `00c9b838`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfece0`](#insn-00bfece0) → `01127b98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfece4`](#insn-00bfece4) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00bfecf0`](#insn-00bfecf0) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00bfed0c`](#insn-00bfed0c) → [`00bfed58`](#insn-00bfed58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfed1c`](#insn-00bfed1c) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00bfed28`](#insn-00bfed28) → `00c9ac30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfed28`](#insn-00bfed28) → `01127e18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bfed2c`](#insn-00bfed2c) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00bfed48`](#insn-00bfed48) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00bfed70`](#insn-00bfed70) → [`00bfed90`](#insn-00bfed90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfed8c`](#insn-00bfed8c) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00bfed94`](#insn-00bfed94) → [`00c582b0`](../00c58/00c582b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582b0` · 推定シンボル `None` · 推定型 `None`
- [`00bfed9c`](#insn-00bfed9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeda0`](#insn-00bfeda0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeda4`](#insn-00bfeda4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeda8`](#insn-00bfeda8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfec94`](#insn-00bfec94)

~~~json
{
  "source": "00bfec94",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec98`](#insn-00bfec98)

~~~json
{
  "source": "00bfec98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfec9c`](#insn-00bfec9c)

~~~json
{
  "source": "00bfec9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeca0`](#insn-00bfeca0)

~~~json
{
  "source": "00bfeca0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfecb8`](#insn-00bfecb8)

~~~json
{
  "source": "00bfecb8",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfecbc`](#insn-00bfecbc)

~~~json
{
  "source": "00bfecbc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfecc0`](#insn-00bfecc0)

~~~json
{
  "source": "00bfecc0",
  "target": "00bfed90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfecd4`](#insn-00bfecd4)

~~~json
{
  "source": "00bfecd4",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfece0`](#insn-00bfece0)

~~~json
{
  "source": "00bfece0",
  "target": "00c9b838",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b838",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfece0`](#insn-00bfece0)

~~~json
{
  "source": "00bfece0",
  "target": "01127b98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfece4`](#insn-00bfece4)

~~~json
{
  "source": "00bfece4",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfecf0`](#insn-00bfecf0)

~~~json
{
  "source": "00bfecf0",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed0c`](#insn-00bfed0c)

~~~json
{
  "source": "00bfed0c",
  "target": "00bfed58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfed1c`](#insn-00bfed1c)

~~~json
{
  "source": "00bfed1c",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed28`](#insn-00bfed28)

~~~json
{
  "source": "00bfed28",
  "target": "00c9ac30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac30",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfed28`](#insn-00bfed28)

~~~json
{
  "source": "00bfed28",
  "target": "01127e18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127e18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfed2c`](#insn-00bfed2c)

~~~json
{
  "source": "00bfed2c",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed48`](#insn-00bfed48)

~~~json
{
  "source": "00bfed48",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed70`](#insn-00bfed70)

~~~json
{
  "source": "00bfed70",
  "target": "00bfed90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfed8c`](#insn-00bfed8c)

~~~json
{
  "source": "00bfed8c",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed94`](#insn-00bfed94)

~~~json
{
  "source": "00bfed94",
  "target": "00c582b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfed9c`](#insn-00bfed9c)

~~~json
{
  "source": "00bfed9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeda0`](#insn-00bfeda0)

~~~json
{
  "source": "00bfeda0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeda4`](#insn-00bfeda4)

~~~json
{
  "source": "00bfeda4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeda8`](#insn-00bfeda8)

~~~json
{
  "source": "00bfeda8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
