# 00bfee1c

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfe9f4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfe9f4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0087.md#compare-bab285744fdac5262d77632ac5199790)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bfeeb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bfe/00bfeeb8.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0087.md#compare-25bdfe7d399e1a7a89ba22023c70623d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfee1c",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEy",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c281b9914662913f99e79dee058283a2ca927bc0b0b71dacd9e20347a21f0ffe",
  "source_text_sha256": "c281b9914662913f99e79dee058283a2ca927bc0b0b71dacd9e20347a21f0ffe",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfee1c",
        "00bfef47"
      ]
    ],
    "bytes_sha256": "ee534f677b720df75cd6a532b9901192c49fbe5f68699f5ff19a55feb8ab6a4f",
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
<a id="insn-00bfee1c"></a> `00bfee1c` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfee20"></a> `00bfee20` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfee24"></a> `00bfee24` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfee28"></a> `00bfee28` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfee2c"></a> `00bfee2c` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfee30"></a> `00bfee30` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfee34"></a> `00bfee34` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfee38"></a> `00bfee38` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfee3c"></a> `00bfee3c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfee40"></a> `00bfee40` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfee44"></a> `00bfee44` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfee48"></a> `00bfee48` | `06 65 01 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-00bfee4c"></a> `00bfee4c` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfee50"></a> `00bfee50` | `88 06 00 34` | cbz w8,0x00bfef20 | `CONDITIONAL_JUMP`
<a id="insn-00bfee54"></a> `00bfee54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfee58"></a> `00bfee58` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfee5c"></a> `00bfee5c` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfee60"></a> `00bfee60` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfee64"></a> `00bfee64` | `03 65 01 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00bfee68"></a> `00bfee68` | `e1 04 00 b0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfee6c"></a> `00bfee6c` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfee70"></a> `00bfee70` | `21 1c 44 f9` | ldr x1,[x1, #0x838] | `FALL_THROUGH`
<a id="insn-00bfee74"></a> `00bfee74` | `03 65 01 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00bfee78"></a> `00bfee78` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bfee7c"></a> `00bfee7c` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfee80"></a> `00bfee80` | `04 65 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00bfee84"></a> `00bfee84` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfee88"></a> `00bfee88` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfee8c"></a> `00bfee8c` | `62 02 08 8b` | add x2,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfee90"></a> `00bfee90` | `43 90 40 b9` | ldr w3,[x2, #0x90] | `FALL_THROUGH`
<a id="insn-00bfee94"></a> `00bfee94` | `56 14 40 f9` | ldr x22,[x2, #0x28] | `FALL_THROUGH`
<a id="insn-00bfee98"></a> `00bfee98` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bfee9c"></a> `00bfee9c` | `61 02 00 54` | b.ne 0x00bfeee8 | `CONDITIONAL_JUMP`
<a id="insn-00bfeea0"></a> `00bfeea0` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeea4"></a> `00bfeea4` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bfeea8"></a> `00bfeea8` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bfeeac"></a> `00bfeeac` | `f1 64 01 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeeb0"></a> `00bfeeb0` | `e1 04 00 90` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00bfeeb4"></a> `00bfeeb4` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeeb8"></a> `00bfeeb8` | `21 18 46 f9` | ldr x1,[x1, #0xc30] | `FALL_THROUGH`
<a id="insn-00bfeebc"></a> `00bfeebc` | `f1 64 01 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeec0"></a> `00bfeec0` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfeec4"></a> `00bfeec4` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfeec8"></a> `00bfeec8` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bfeecc"></a> `00bfeecc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfeed0"></a> `00bfeed0` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bfeed4"></a> `00bfeed4` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeed8"></a> `00bfeed8` | `ee 64 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeedc"></a> `00bfeedc` | `e3 1e 00 12` | and w3,w23,#0xff | `FALL_THROUGH`
<a id="insn-00bfeee0"></a> `00bfeee0` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bfeee4"></a> `00bfeee4` | `03 93 00 b9` | str w3,[x24, #0x90] | `FALL_THROUGH`
<a id="insn-00bfeee8"></a> `00bfeee8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bfeeec"></a> `00bfeeec` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfeef0"></a> `00bfeef0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfeef4"></a> `00bfeef4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bfeef8"></a> `00bfeef8` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-00bfeefc"></a> `00bfeefc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfef00"></a> `00bfef00` | `00 01 00 b5` | cbnz x0,0x00bfef20 | `CONDITIONAL_JUMP`
<a id="insn-00bfef04"></a> `00bfef04` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfef08"></a> `00bfef08` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bfef0c"></a> `00bfef0c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfef10"></a> `00bfef10` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfef14"></a> `00bfef14` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfef18"></a> `00bfef18` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00bfef1c"></a> `00bfef1c` | `e1 64 01 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef20"></a> `00bfef20` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfef24"></a> `00bfef24` | `e3 64 01 94` | bl 0x00c582b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef28"></a> `00bfef28` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfef2c"></a> `00bfef2c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfef30"></a> `00bfef30` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfef34"></a> `00bfef34` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfef38"></a> `00bfef38` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfef3c"></a> `00bfef3c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfef40"></a> `00bfef40` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfef44"></a> `00bfef44` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfee1c`](#insn-00bfee1c) 範囲 `[['00bfee1c', '00bfee53']]`
  - `CONDITIONAL_JUMP` [`00bfee50`](#insn-00bfee50) → [`00bfef20`](#insn-00bfef20)
  - `FALL_THROUGH` [`00bfee50`](#insn-00bfee50) → [`00bfee54`](#insn-00bfee54)
- ブロック [`00bfee54`](#insn-00bfee54) 範囲 `[['00bfee54', '00bfee9f']]`
  - `CONDITIONAL_JUMP` [`00bfee9c`](#insn-00bfee9c) → [`00bfeee8`](#insn-00bfeee8)
  - `FALL_THROUGH` [`00bfee9c`](#insn-00bfee9c) → [`00bfeea0`](#insn-00bfeea0)
- ブロック [`00bfeea0`](#insn-00bfeea0) 範囲 `[['00bfeea0', '00bfeee7']]`
  - `FALL_THROUGH` [`00bfeee4`](#insn-00bfeee4) → [`00bfeee8`](#insn-00bfeee8)
- ブロック [`00bfeee8`](#insn-00bfeee8) 範囲 `[['00bfeee8', '00bfef03']]`
  - `CONDITIONAL_JUMP` [`00bfef00`](#insn-00bfef00) → [`00bfef20`](#insn-00bfef20)
  - `FALL_THROUGH` [`00bfef00`](#insn-00bfef00) → [`00bfef04`](#insn-00bfef04)
- ブロック [`00bfef04`](#insn-00bfef04) 範囲 `[['00bfef04', '00bfef1f']]`
  - `FALL_THROUGH` [`00bfef1c`](#insn-00bfef1c) → [`00bfef20`](#insn-00bfef20)
- ブロック [`00bfef20`](#insn-00bfef20) 範囲 `[['00bfef20', '00bfef47']]`

## 命令位置別の参照

- [`00bfee24`](#insn-00bfee24) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfee28`](#insn-00bfee28) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfee2c`](#insn-00bfee2c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfee30`](#insn-00bfee30) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfee48`](#insn-00bfee48) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`00bfee4c`](#insn-00bfee4c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfee50`](#insn-00bfee50) → [`00bfef20`](#insn-00bfef20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfee64`](#insn-00bfee64) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00bfee70`](#insn-00bfee70) → `00c9b838`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfee70`](#insn-00bfee70) → `01127b98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfee74`](#insn-00bfee74) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00bfee80`](#insn-00bfee80) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00bfee9c`](#insn-00bfee9c) → [`00bfeee8`](#insn-00bfeee8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeeac`](#insn-00bfeeac) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00bfeeb8`](#insn-00bfeeb8) → `00c9ac30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfeeb8`](#insn-00bfeeb8) → `01127e18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bfeebc`](#insn-00bfeebc) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00bfeed8`](#insn-00bfeed8) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00bfef00`](#insn-00bfef00) → [`00bfef20`](#insn-00bfef20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfef1c`](#insn-00bfef1c) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00bfef24`](#insn-00bfef24) → [`00c582b0`](../00c58/00c582b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582b0` · 推定シンボル `None` · 推定型 `None`
- [`00bfef2c`](#insn-00bfef2c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfef30`](#insn-00bfef30) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfef34`](#insn-00bfef34) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfef38`](#insn-00bfef38) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfee24`](#insn-00bfee24)

~~~json
{
  "source": "00bfee24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfee28`](#insn-00bfee28)

~~~json
{
  "source": "00bfee28",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfee2c`](#insn-00bfee2c)

~~~json
{
  "source": "00bfee2c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfee30`](#insn-00bfee30)

~~~json
{
  "source": "00bfee30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfee48`](#insn-00bfee48)

~~~json
{
  "source": "00bfee48",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfee4c`](#insn-00bfee4c)

~~~json
{
  "source": "00bfee4c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfee50`](#insn-00bfee50)

~~~json
{
  "source": "00bfee50",
  "target": "00bfef20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfee64`](#insn-00bfee64)

~~~json
{
  "source": "00bfee64",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfee70`](#insn-00bfee70)

~~~json
{
  "source": "00bfee70",
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
- 参照命令 [`00bfee70`](#insn-00bfee70)

~~~json
{
  "source": "00bfee70",
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
- 参照命令 [`00bfee74`](#insn-00bfee74)

~~~json
{
  "source": "00bfee74",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfee80`](#insn-00bfee80)

~~~json
{
  "source": "00bfee80",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfee9c`](#insn-00bfee9c)

~~~json
{
  "source": "00bfee9c",
  "target": "00bfeee8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeeac`](#insn-00bfeeac)

~~~json
{
  "source": "00bfeeac",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfeeb8`](#insn-00bfeeb8)

~~~json
{
  "source": "00bfeeb8",
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
- 参照命令 [`00bfeeb8`](#insn-00bfeeb8)

~~~json
{
  "source": "00bfeeb8",
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
- 参照命令 [`00bfeebc`](#insn-00bfeebc)

~~~json
{
  "source": "00bfeebc",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfeed8`](#insn-00bfeed8)

~~~json
{
  "source": "00bfeed8",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef00`](#insn-00bfef00)

~~~json
{
  "source": "00bfef00",
  "target": "00bfef20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfef1c`](#insn-00bfef1c)

~~~json
{
  "source": "00bfef1c",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef24`](#insn-00bfef24)

~~~json
{
  "source": "00bfef24",
  "target": "00c582b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef2c`](#insn-00bfef2c)

~~~json
{
  "source": "00bfef2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfef30`](#insn-00bfef30)

~~~json
{
  "source": "00bfef30",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfef34`](#insn-00bfef34)

~~~json
{
  "source": "00bfef34",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfef38`](#insn-00bfef38)

~~~json
{
  "source": "00bfef38",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
