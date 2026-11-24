# 00bffeac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfeeb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfeeb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-31b02071dd8888eb9e4b6e3960376080)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffeac",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEy",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a23b8b2b10ca16054b839cafe070096e7386cea7076278fd31202a5f13eb4fea",
  "source_text_sha256": "a23b8b2b10ca16054b839cafe070096e7386cea7076278fd31202a5f13eb4fea",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffeac",
        "00bfffd7"
      ]
    ],
    "bytes_sha256": "8ad9967f3afc7d0df2dcedb9d62aa0a46a27ab6314517373bbc48253916e318b",
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

- [00c59300](../00c59/00c59300.md)
- [00c59310](../00c59/00c59310.md)
- [00c59320](../00c59/00c59320.md)
- [00c59330](../00c59/00c59330.md)
- [00c59340](../00c59/00c59340.md)
- [00c59350](../00c59/00c59350.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1629 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEy(long *param_1,undefined8 param_2)

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
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9c8d8
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_48);
    lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar1 = *(uint *)(lVar4 + 0x90);
    uVar5 = *(undefined8 *)(lVar4 + 0x28);
    if (uVar1 == 0xffffffff) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,lVar4);
      plVar3 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_48,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9bcd0);
      uVar1 = (**(code **)(*plVar3 + 0x38))(plVar3,0x20);
      _ZNSt6__ndk16localeD1Ev(auStack_48);
      uVar1 = uVar1 & 0xff;
      *(uint *)(lVar4 + 0x90) = uVar1;
    }
    lVar4 = (**(code **)(*plVar2 + 0x38))(plVar2,uVar5,lVar4,uVar1,param_2);
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
<a id="insn-00bffeac"></a> `00bffeac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bffeb0"></a> `00bffeb0` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bffeb4"></a> `00bffeb4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bffeb8"></a> `00bffeb8` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bffebc"></a> `00bffebc` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bffec0"></a> `00bffec0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bffec4"></a> `00bffec4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bffec8"></a> `00bffec8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bffecc"></a> `00bffecc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bffed0"></a> `00bffed0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bffed4"></a> `00bffed4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bffed8"></a> `00bffed8` | `0a 65 01 94` | bl 0x00c59300 | `UNCONDITIONAL_CALL`
<a id="insn-00bffedc"></a> `00bffedc` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bffee0"></a> `00bffee0` | `88 06 00 34` | cbz w8,0x00bfffb0 | `CONDITIONAL_JUMP`
<a id="insn-00bffee4"></a> `00bffee4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bffee8"></a> `00bffee8` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bffeec"></a> `00bffeec` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffef0"></a> `00bffef0` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bffef4"></a> `00bffef4` | `07 65 01 94` | bl 0x00c59310 | `UNCONDITIONAL_CALL`
<a id="insn-00bffef8"></a> `00bffef8` | `e1 04 00 b0` | adrp x1,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bffefc"></a> `00bffefc` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfff00"></a> `00bfff00` | `21 6c 44 f9` | ldr x1,[x1, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bfff04"></a> `00bfff04` | `07 65 01 94` | bl 0x00c59320 | `UNCONDITIONAL_CALL`
<a id="insn-00bfff08"></a> `00bfff08` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bfff0c"></a> `00bfff0c` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfff10"></a> `00bfff10` | `08 65 01 94` | bl 0x00c59330 | `UNCONDITIONAL_CALL`
<a id="insn-00bfff14"></a> `00bfff14` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfff18"></a> `00bfff18` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfff1c"></a> `00bfff1c` | `62 02 08 8b` | add x2,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfff20"></a> `00bfff20` | `43 90 40 b9` | ldr w3,[x2, #0x90] | `FALL_THROUGH`
<a id="insn-00bfff24"></a> `00bfff24` | `56 14 40 f9` | ldr x22,[x2, #0x28] | `FALL_THROUGH`
<a id="insn-00bfff28"></a> `00bfff28` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bfff2c"></a> `00bfff2c` | `61 02 00 54` | b.ne 0x00bfff78 | `CONDITIONAL_JUMP`
<a id="insn-00bfff30"></a> `00bfff30` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfff34"></a> `00bfff34` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bfff38"></a> `00bfff38` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bfff3c"></a> `00bfff3c` | `f5 64 01 94` | bl 0x00c59310 | `UNCONDITIONAL_CALL`
<a id="insn-00bfff40"></a> `00bfff40` | `e1 04 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfff44"></a> `00bfff44` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfff48"></a> `00bfff48` | `21 68 46 f9` | ldr x1,[x1, #0xcd0] | `FALL_THROUGH`
<a id="insn-00bfff4c"></a> `00bfff4c` | `f5 64 01 94` | bl 0x00c59320 | `UNCONDITIONAL_CALL`
<a id="insn-00bfff50"></a> `00bfff50` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfff54"></a> `00bfff54` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfff58"></a> `00bfff58` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bfff5c"></a> `00bfff5c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfff60"></a> `00bfff60` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bfff64"></a> `00bfff64` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfff68"></a> `00bfff68` | `f2 64 01 94` | bl 0x00c59330 | `UNCONDITIONAL_CALL`
<a id="insn-00bfff6c"></a> `00bfff6c` | `e3 1e 00 12` | and w3,w23,#0xff | `FALL_THROUGH`
<a id="insn-00bfff70"></a> `00bfff70` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bfff74"></a> `00bfff74` | `03 93 00 b9` | str w3,[x24, #0x90] | `FALL_THROUGH`
<a id="insn-00bfff78"></a> `00bfff78` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bfff7c"></a> `00bfff7c` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfff80"></a> `00bfff80` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfff84"></a> `00bfff84` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bfff88"></a> `00bfff88` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-00bfff8c"></a> `00bfff8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfff90"></a> `00bfff90` | `00 01 00 b5` | cbnz x0,0x00bfffb0 | `CONDITIONAL_JUMP`
<a id="insn-00bfff94"></a> `00bfff94` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfff98"></a> `00bfff98` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bfff9c"></a> `00bfff9c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfffa0"></a> `00bfffa0` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfffa4"></a> `00bfffa4` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfffa8"></a> `00bfffa8` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00bfffac"></a> `00bfffac` | `e5 64 01 94` | bl 0x00c59340 | `UNCONDITIONAL_CALL`
<a id="insn-00bfffb0"></a> `00bfffb0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfffb4"></a> `00bfffb4` | `e7 64 01 94` | bl 0x00c59350 | `UNCONDITIONAL_CALL`
<a id="insn-00bfffb8"></a> `00bfffb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfffbc"></a> `00bfffbc` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfffc0"></a> `00bfffc0` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfffc4"></a> `00bfffc4` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfffc8"></a> `00bfffc8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfffcc"></a> `00bfffcc` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfffd0"></a> `00bfffd0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfffd4"></a> `00bfffd4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffeac`](#insn-00bffeac) 範囲 `[['00bffeac', '00bffee3']]`
  - `CONDITIONAL_JUMP` [`00bffee0`](#insn-00bffee0) → [`00bfffb0`](#insn-00bfffb0)
  - `FALL_THROUGH` [`00bffee0`](#insn-00bffee0) → [`00bffee4`](#insn-00bffee4)
- ブロック [`00bffee4`](#insn-00bffee4) 範囲 `[['00bffee4', '00bfff2f']]`
  - `CONDITIONAL_JUMP` [`00bfff2c`](#insn-00bfff2c) → [`00bfff78`](#insn-00bfff78)
  - `FALL_THROUGH` [`00bfff2c`](#insn-00bfff2c) → [`00bfff30`](#insn-00bfff30)
- ブロック [`00bfff30`](#insn-00bfff30) 範囲 `[['00bfff30', '00bfff77']]`
  - `FALL_THROUGH` [`00bfff74`](#insn-00bfff74) → [`00bfff78`](#insn-00bfff78)
- ブロック [`00bfff78`](#insn-00bfff78) 範囲 `[['00bfff78', '00bfff93']]`
  - `CONDITIONAL_JUMP` [`00bfff90`](#insn-00bfff90) → [`00bfffb0`](#insn-00bfffb0)
  - `FALL_THROUGH` [`00bfff90`](#insn-00bfff90) → [`00bfff94`](#insn-00bfff94)
- ブロック [`00bfff94`](#insn-00bfff94) 範囲 `[['00bfff94', '00bfffaf']]`
  - `FALL_THROUGH` [`00bfffac`](#insn-00bfffac) → [`00bfffb0`](#insn-00bfffb0)
- ブロック [`00bfffb0`](#insn-00bfffb0) 範囲 `[['00bfffb0', '00bfffd7']]`

## 命令位置別の参照

- [`00bffeb4`](#insn-00bffeb4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffeb8`](#insn-00bffeb8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffebc`](#insn-00bffebc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffec0`](#insn-00bffec0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffed8`](#insn-00bffed8) → [`00c59300`](../00c59/00c59300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59300` · 推定シンボル `None` · 推定型 `None`
- [`00bffedc`](#insn-00bffedc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffee0`](#insn-00bffee0) → [`00bfffb0`](#insn-00bfffb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffef4`](#insn-00bffef4) → [`00c59310`](../00c59/00c59310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59310` · 推定シンボル `None` · 推定型 `None`
- [`00bfff00`](#insn-00bfff00) → `00c9c8d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfff00`](#insn-00bfff00) → `01128c58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfff04`](#insn-00bfff04) → [`00c59320`](../00c59/00c59320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59320` · 推定シンボル `None` · 推定型 `None`
- [`00bfff10`](#insn-00bfff10) → [`00c59330`](../00c59/00c59330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59330` · 推定シンボル `None` · 推定型 `None`
- [`00bfff2c`](#insn-00bfff2c) → [`00bfff78`](#insn-00bfff78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfff3c`](#insn-00bfff3c) → [`00c59310`](../00c59/00c59310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59310` · 推定シンボル `None` · 推定型 `None`
- [`00bfff48`](#insn-00bfff48) → `00c9bcd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfff48`](#insn-00bfff48) → `01128ed8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bfff4c`](#insn-00bfff4c) → [`00c59320`](../00c59/00c59320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59320` · 推定シンボル `None` · 推定型 `None`
- [`00bfff68`](#insn-00bfff68) → [`00c59330`](../00c59/00c59330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59330` · 推定シンボル `None` · 推定型 `None`
- [`00bfff90`](#insn-00bfff90) → [`00bfffb0`](#insn-00bfffb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffac`](#insn-00bfffac) → [`00c59340`](../00c59/00c59340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59340` · 推定シンボル `None` · 推定型 `None`
- [`00bfffb4`](#insn-00bfffb4) → [`00c59350`](../00c59/00c59350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59350` · 推定シンボル `None` · 推定型 `None`
- [`00bfffbc`](#insn-00bfffbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffc0`](#insn-00bfffc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffc4`](#insn-00bfffc4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfffc8`](#insn-00bfffc8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffeb4`](#insn-00bffeb4)

~~~json
{
  "source": "00bffeb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffeb8`](#insn-00bffeb8)

~~~json
{
  "source": "00bffeb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffebc`](#insn-00bffebc)

~~~json
{
  "source": "00bffebc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffec0`](#insn-00bffec0)

~~~json
{
  "source": "00bffec0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffed8`](#insn-00bffed8)

~~~json
{
  "source": "00bffed8",
  "target": "00c59300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffedc`](#insn-00bffedc)

~~~json
{
  "source": "00bffedc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffee0`](#insn-00bffee0)

~~~json
{
  "source": "00bffee0",
  "target": "00bfffb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffef4`](#insn-00bffef4)

~~~json
{
  "source": "00bffef4",
  "target": "00c59310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfff00`](#insn-00bfff00)

~~~json
{
  "source": "00bfff00",
  "target": "00c9c8d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c8d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfff00`](#insn-00bfff00)

~~~json
{
  "source": "00bfff00",
  "target": "01128c58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128c58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfff04`](#insn-00bfff04)

~~~json
{
  "source": "00bfff04",
  "target": "00c59320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfff10`](#insn-00bfff10)

~~~json
{
  "source": "00bfff10",
  "target": "00c59330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfff2c`](#insn-00bfff2c)

~~~json
{
  "source": "00bfff2c",
  "target": "00bfff78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfff3c`](#insn-00bfff3c)

~~~json
{
  "source": "00bfff3c",
  "target": "00c59310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfff48`](#insn-00bfff48)

~~~json
{
  "source": "00bfff48",
  "target": "00c9bcd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bcd0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfff48`](#insn-00bfff48)

~~~json
{
  "source": "00bfff48",
  "target": "01128ed8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01128ed8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfff4c`](#insn-00bfff4c)

~~~json
{
  "source": "00bfff4c",
  "target": "00c59320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfff68`](#insn-00bfff68)

~~~json
{
  "source": "00bfff68",
  "target": "00c59330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfff90`](#insn-00bfff90)

~~~json
{
  "source": "00bfff90",
  "target": "00bfffb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffac`](#insn-00bfffac)

~~~json
{
  "source": "00bfffac",
  "target": "00c59340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfffb4`](#insn-00bfffb4)

~~~json
{
  "source": "00bfffb4",
  "target": "00c59350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfffbc`](#insn-00bfffbc)

~~~json
{
  "source": "00bfffbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffc0`](#insn-00bfffc0)

~~~json
{
  "source": "00bfffc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffc4`](#insn-00bfffc4)

~~~json
{
  "source": "00bfffc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfffc8`](#insn-00bfffc8)

~~~json
{
  "source": "00bfffc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
