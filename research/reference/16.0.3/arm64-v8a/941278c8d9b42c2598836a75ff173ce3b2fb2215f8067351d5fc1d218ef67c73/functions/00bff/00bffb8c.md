# 00bffb8c

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfeb98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfeb98.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-a084740166b9eebb897cf8b1166ad270)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bffb8c",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEb",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "693c1eeeec1844374dde5158c4bfd82f09a62ca297440decbde561099d619904",
  "source_text_sha256": "693c1eeeec1844374dde5158c4bfd82f09a62ca297440decbde561099d619904",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bffb8c",
        "00bffcb7"
      ]
    ],
    "bytes_sha256": "360e5bf41a594bf63f42dc8796c2773fe6212180b5564451f9911cbc0c8445cf",
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

## 疑似コード / UTF-8 1627 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEb(long *param_1,uint param_2)

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
    lVar4 = (**(code **)(*plVar2 + 0x18))(plVar2,uVar5,lVar4,uVar1,param_2 & 1);
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
<a id="insn-00bffb8c"></a> `00bffb8c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bffb90"></a> `00bffb90` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bffb94"></a> `00bffb94` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bffb98"></a> `00bffb98` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bffb9c"></a> `00bffb9c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bffba0"></a> `00bffba0` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bffba4"></a> `00bffba4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bffba8"></a> `00bffba8` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00bffbac"></a> `00bffbac` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bffbb0"></a> `00bffbb0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bffbb4"></a> `00bffbb4` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bffbb8"></a> `00bffbb8` | `d2 65 01 94` | bl 0x00c59300 | `UNCONDITIONAL_CALL`
<a id="insn-00bffbbc"></a> `00bffbbc` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bffbc0"></a> `00bffbc0` | `88 06 00 34` | cbz w8,0x00bffc90 | `CONDITIONAL_JUMP`
<a id="insn-00bffbc4"></a> `00bffbc4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bffbc8"></a> `00bffbc8` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bffbcc"></a> `00bffbcc` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffbd0"></a> `00bffbd0` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bffbd4"></a> `00bffbd4` | `cf 65 01 94` | bl 0x00c59310 | `UNCONDITIONAL_CALL`
<a id="insn-00bffbd8"></a> `00bffbd8` | `e1 04 00 b0` | adrp x1,0xc9c000 | `FALL_THROUGH`
<a id="insn-00bffbdc"></a> `00bffbdc` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffbe0"></a> `00bffbe0` | `21 6c 44 f9` | ldr x1,[x1, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bffbe4"></a> `00bffbe4` | `cf 65 01 94` | bl 0x00c59320 | `UNCONDITIONAL_CALL`
<a id="insn-00bffbe8"></a> `00bffbe8` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bffbec"></a> `00bffbec` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffbf0"></a> `00bffbf0` | `d0 65 01 94` | bl 0x00c59330 | `UNCONDITIONAL_CALL`
<a id="insn-00bffbf4"></a> `00bffbf4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bffbf8"></a> `00bffbf8` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bffbfc"></a> `00bffbfc` | `62 02 08 8b` | add x2,x19,x8 | `FALL_THROUGH`
<a id="insn-00bffc00"></a> `00bffc00` | `43 90 40 b9` | ldr w3,[x2, #0x90] | `FALL_THROUGH`
<a id="insn-00bffc04"></a> `00bffc04` | `56 14 40 f9` | ldr x22,[x2, #0x28] | `FALL_THROUGH`
<a id="insn-00bffc08"></a> `00bffc08` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bffc0c"></a> `00bffc0c` | `61 02 00 54` | b.ne 0x00bffc58 | `CONDITIONAL_JUMP`
<a id="insn-00bffc10"></a> `00bffc10` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffc14"></a> `00bffc14` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bffc18"></a> `00bffc18` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bffc1c"></a> `00bffc1c` | `bd 65 01 94` | bl 0x00c59310 | `UNCONDITIONAL_CALL`
<a id="insn-00bffc20"></a> `00bffc20` | `e1 04 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bffc24"></a> `00bffc24` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffc28"></a> `00bffc28` | `21 68 46 f9` | ldr x1,[x1, #0xcd0] | `FALL_THROUGH`
<a id="insn-00bffc2c"></a> `00bffc2c` | `bd 65 01 94` | bl 0x00c59320 | `UNCONDITIONAL_CALL`
<a id="insn-00bffc30"></a> `00bffc30` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bffc34"></a> `00bffc34` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bffc38"></a> `00bffc38` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bffc3c"></a> `00bffc3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bffc40"></a> `00bffc40` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bffc44"></a> `00bffc44` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bffc48"></a> `00bffc48` | `ba 65 01 94` | bl 0x00c59330 | `UNCONDITIONAL_CALL`
<a id="insn-00bffc4c"></a> `00bffc4c` | `e3 1e 00 12` | and w3,w23,#0xff | `FALL_THROUGH`
<a id="insn-00bffc50"></a> `00bffc50` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bffc54"></a> `00bffc54` | `03 93 00 b9` | str w3,[x24, #0x90] | `FALL_THROUGH`
<a id="insn-00bffc58"></a> `00bffc58` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bffc5c"></a> `00bffc5c` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00bffc60"></a> `00bffc60` | `84 02 00 12` | and w4,w20,#0x1 | `FALL_THROUGH`
<a id="insn-00bffc64"></a> `00bffc64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bffc68"></a> `00bffc68` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bffc6c"></a> `00bffc6c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bffc70"></a> `00bffc70` | `00 01 00 b5` | cbnz x0,0x00bffc90 | `CONDITIONAL_JUMP`
<a id="insn-00bffc74"></a> `00bffc74` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bffc78"></a> `00bffc78` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bffc7c"></a> `00bffc7c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bffc80"></a> `00bffc80` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bffc84"></a> `00bffc84` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bffc88"></a> `00bffc88` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00bffc8c"></a> `00bffc8c` | `ad 65 01 94` | bl 0x00c59340 | `UNCONDITIONAL_CALL`
<a id="insn-00bffc90"></a> `00bffc90` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bffc94"></a> `00bffc94` | `af 65 01 94` | bl 0x00c59350 | `UNCONDITIONAL_CALL`
<a id="insn-00bffc98"></a> `00bffc98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bffc9c"></a> `00bffc9c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bffca0"></a> `00bffca0` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bffca4"></a> `00bffca4` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bffca8"></a> `00bffca8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bffcac"></a> `00bffcac` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bffcb0"></a> `00bffcb0` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bffcb4"></a> `00bffcb4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bffb8c`](#insn-00bffb8c) 範囲 `[['00bffb8c', '00bffbc3']]`
  - `CONDITIONAL_JUMP` [`00bffbc0`](#insn-00bffbc0) → [`00bffc90`](#insn-00bffc90)
  - `FALL_THROUGH` [`00bffbc0`](#insn-00bffbc0) → [`00bffbc4`](#insn-00bffbc4)
- ブロック [`00bffbc4`](#insn-00bffbc4) 範囲 `[['00bffbc4', '00bffc0f']]`
  - `CONDITIONAL_JUMP` [`00bffc0c`](#insn-00bffc0c) → [`00bffc58`](#insn-00bffc58)
  - `FALL_THROUGH` [`00bffc0c`](#insn-00bffc0c) → [`00bffc10`](#insn-00bffc10)
- ブロック [`00bffc10`](#insn-00bffc10) 範囲 `[['00bffc10', '00bffc57']]`
  - `FALL_THROUGH` [`00bffc54`](#insn-00bffc54) → [`00bffc58`](#insn-00bffc58)
- ブロック [`00bffc58`](#insn-00bffc58) 範囲 `[['00bffc58', '00bffc73']]`
  - `CONDITIONAL_JUMP` [`00bffc70`](#insn-00bffc70) → [`00bffc90`](#insn-00bffc90)
  - `FALL_THROUGH` [`00bffc70`](#insn-00bffc70) → [`00bffc74`](#insn-00bffc74)
- ブロック [`00bffc74`](#insn-00bffc74) 範囲 `[['00bffc74', '00bffc8f']]`
  - `FALL_THROUGH` [`00bffc8c`](#insn-00bffc8c) → [`00bffc90`](#insn-00bffc90)
- ブロック [`00bffc90`](#insn-00bffc90) 範囲 `[['00bffc90', '00bffcb7']]`

## 命令位置別の参照

- [`00bffb94`](#insn-00bffb94) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffb98`](#insn-00bffb98) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffb9c`](#insn-00bffb9c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffba0`](#insn-00bffba0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffbb8`](#insn-00bffbb8) → [`00c59300`](../00c59/00c59300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59300` · 推定シンボル `None` · 推定型 `None`
- [`00bffbbc`](#insn-00bffbbc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffbc0`](#insn-00bffbc0) → [`00bffc90`](#insn-00bffc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffbd4`](#insn-00bffbd4) → [`00c59310`](../00c59/00c59310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59310` · 推定シンボル `None` · 推定型 `None`
- [`00bffbe0`](#insn-00bffbe0) → `00c9c8d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bffbe0`](#insn-00bffbe0) → `01128c58`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bffbe4`](#insn-00bffbe4) → [`00c59320`](../00c59/00c59320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59320` · 推定シンボル `None` · 推定型 `None`
- [`00bffbf0`](#insn-00bffbf0) → [`00c59330`](../00c59/00c59330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59330` · 推定シンボル `None` · 推定型 `None`
- [`00bffc0c`](#insn-00bffc0c) → [`00bffc58`](#insn-00bffc58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffc1c`](#insn-00bffc1c) → [`00c59310`](../00c59/00c59310.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59310` · 推定シンボル `None` · 推定型 `None`
- [`00bffc28`](#insn-00bffc28) → `00c9bcd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bffc28`](#insn-00bffc28) → `01128ed8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bffc2c`](#insn-00bffc2c) → [`00c59320`](../00c59/00c59320.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59320` · 推定シンボル `None` · 推定型 `None`
- [`00bffc48`](#insn-00bffc48) → [`00c59330`](../00c59/00c59330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59330` · 推定シンボル `None` · 推定型 `None`
- [`00bffc70`](#insn-00bffc70) → [`00bffc90`](#insn-00bffc90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffc8c`](#insn-00bffc8c) → [`00c59340`](../00c59/00c59340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59340` · 推定シンボル `None` · 推定型 `None`
- [`00bffc94`](#insn-00bffc94) → [`00c59350`](../00c59/00c59350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59350` · 推定シンボル `None` · 推定型 `None`
- [`00bffc9c`](#insn-00bffc9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffca0`](#insn-00bffca0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffca4`](#insn-00bffca4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bffca8`](#insn-00bffca8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bffb94`](#insn-00bffb94)

~~~json
{
  "source": "00bffb94",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffb98`](#insn-00bffb98)

~~~json
{
  "source": "00bffb98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffb9c`](#insn-00bffb9c)

~~~json
{
  "source": "00bffb9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffba0`](#insn-00bffba0)

~~~json
{
  "source": "00bffba0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffbb8`](#insn-00bffbb8)

~~~json
{
  "source": "00bffbb8",
  "target": "00c59300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffbbc`](#insn-00bffbbc)

~~~json
{
  "source": "00bffbbc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffbc0`](#insn-00bffbc0)

~~~json
{
  "source": "00bffbc0",
  "target": "00bffc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffbd4`](#insn-00bffbd4)

~~~json
{
  "source": "00bffbd4",
  "target": "00c59310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffbe0`](#insn-00bffbe0)

~~~json
{
  "source": "00bffbe0",
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
- 参照命令 [`00bffbe0`](#insn-00bffbe0)

~~~json
{
  "source": "00bffbe0",
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
- 参照命令 [`00bffbe4`](#insn-00bffbe4)

~~~json
{
  "source": "00bffbe4",
  "target": "00c59320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffbf0`](#insn-00bffbf0)

~~~json
{
  "source": "00bffbf0",
  "target": "00c59330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffc0c`](#insn-00bffc0c)

~~~json
{
  "source": "00bffc0c",
  "target": "00bffc58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffc1c`](#insn-00bffc1c)

~~~json
{
  "source": "00bffc1c",
  "target": "00c59310",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffc28`](#insn-00bffc28)

~~~json
{
  "source": "00bffc28",
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
- 参照命令 [`00bffc28`](#insn-00bffc28)

~~~json
{
  "source": "00bffc28",
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
- 参照命令 [`00bffc2c`](#insn-00bffc2c)

~~~json
{
  "source": "00bffc2c",
  "target": "00c59320",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffc48`](#insn-00bffc48)

~~~json
{
  "source": "00bffc48",
  "target": "00c59330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffc70`](#insn-00bffc70)

~~~json
{
  "source": "00bffc70",
  "target": "00bffc90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffc8c`](#insn-00bffc8c)

~~~json
{
  "source": "00bffc8c",
  "target": "00c59340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffc94`](#insn-00bffc94)

~~~json
{
  "source": "00bffc94",
  "target": "00c59350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bffc9c`](#insn-00bffc9c)

~~~json
{
  "source": "00bffc9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffca0`](#insn-00bffca0)

~~~json
{
  "source": "00bffca0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffca4`](#insn-00bffca4)

~~~json
{
  "source": "00bffca4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bffca8`](#insn-00bffca8)

~~~json
{
  "source": "00bffca8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
