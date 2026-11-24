# 00bfeeb8

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfee1c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfe/00bfee1c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0087.md#compare-25bdfe7d399e1a7a89ba22023c70623d)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bffeac`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bff/00bffeac.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0087.md#compare-31b02071dd8888eb9e4b6e3960376080)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfeeb8",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEy",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5981e3d3c5b22970d67302cab363cc051626ff0ec5f2afa6041c2f32c9800144",
  "source_text_sha256": "5981e3d3c5b22970d67302cab363cc051626ff0ec5f2afa6041c2f32c9800144",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfeeb8",
        "00bfefe3"
      ]
    ],
    "bytes_sha256": "bd1c9645237ff9c287aebcbbf24b5a528a15e00cb419f4ba2a3ee30f0c42fd77",
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

- [00c58330](../00c58/00c58330.md)
- [00c58340](../00c58/00c58340.md)
- [00c58350](../00c58/00c58350.md)
- [00c58360](../00c58/00c58360.md)
- [00c58370](../00c58/00c58370.md)
- [00c58380](../00c58/00c58380.md)

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
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b908
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_48);
    lVar4 = (long)param_1 + *(long *)(*param_1 + -0x18);
    uVar1 = *(uint *)(lVar4 + 0x90);
    uVar5 = *(undefined8 *)(lVar4 + 0x28);
    if (uVar1 == 0xffffffff) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,lVar4);
      plVar3 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_48,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ad00);
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
<a id="insn-00bfeeb8"></a> `00bfeeb8` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfeebc"></a> `00bfeebc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfeec0"></a> `00bfeec0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfeec4"></a> `00bfeec4` | `f8 5f 03 a9` | stp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfeec8"></a> `00bfeec8` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfeecc"></a> `00bfeecc` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfeed0"></a> `00bfeed0` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bfeed4"></a> `00bfeed4` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bfeed8"></a> `00bfeed8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfeedc"></a> `00bfeedc` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeee0"></a> `00bfeee0` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfeee4"></a> `00bfeee4` | `13 65 01 94` | bl 0x00c58330 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeee8"></a> `00bfeee8` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfeeec"></a> `00bfeeec` | `88 06 00 34` | cbz w8,0x00bfefbc | `CONDITIONAL_JUMP`
<a id="insn-00bfeef0"></a> `00bfeef0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfeef4"></a> `00bfeef4` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfeef8"></a> `00bfeef8` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfeefc"></a> `00bfeefc` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfef00"></a> `00bfef00` | `10 65 01 94` | bl 0x00c58340 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef04"></a> `00bfef04` | `e1 04 00 b0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bfef08"></a> `00bfef08` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfef0c"></a> `00bfef0c` | `21 84 44 f9` | ldr x1,[x1, #0x908] | `FALL_THROUGH`
<a id="insn-00bfef10"></a> `00bfef10` | `10 65 01 94` | bl 0x00c58350 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef14"></a> `00bfef14` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bfef18"></a> `00bfef18` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfef1c"></a> `00bfef1c` | `11 65 01 94` | bl 0x00c58360 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef20"></a> `00bfef20` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfef24"></a> `00bfef24` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfef28"></a> `00bfef28` | `62 02 08 8b` | add x2,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfef2c"></a> `00bfef2c` | `43 90 40 b9` | ldr w3,[x2, #0x90] | `FALL_THROUGH`
<a id="insn-00bfef30"></a> `00bfef30` | `56 14 40 f9` | ldr x22,[x2, #0x28] | `FALL_THROUGH`
<a id="insn-00bfef34"></a> `00bfef34` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bfef38"></a> `00bfef38` | `61 02 00 54` | b.ne 0x00bfef84 | `CONDITIONAL_JUMP`
<a id="insn-00bfef3c"></a> `00bfef3c` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfef40"></a> `00bfef40` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bfef44"></a> `00bfef44` | `f8 03 02 aa` | mov x24,x2 | `FALL_THROUGH`
<a id="insn-00bfef48"></a> `00bfef48` | `fe 64 01 94` | bl 0x00c58340 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef4c"></a> `00bfef4c` | `e1 04 00 90` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00bfef50"></a> `00bfef50` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfef54"></a> `00bfef54` | `21 80 46 f9` | ldr x1,[x1, #0xd00] | `FALL_THROUGH`
<a id="insn-00bfef58"></a> `00bfef58` | `fe 64 01 94` | bl 0x00c58350 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef5c"></a> `00bfef5c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bfef60"></a> `00bfef60` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfef64"></a> `00bfef64` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bfef68"></a> `00bfef68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfef6c"></a> `00bfef6c` | `f7 03 00 2a` | mov w23,w0 | `FALL_THROUGH`
<a id="insn-00bfef70"></a> `00bfef70` | `a0 23 00 d1` | sub x0,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bfef74"></a> `00bfef74` | `fb 64 01 94` | bl 0x00c58360 | `UNCONDITIONAL_CALL`
<a id="insn-00bfef78"></a> `00bfef78` | `e3 1e 00 12` | and w3,w23,#0xff | `FALL_THROUGH`
<a id="insn-00bfef7c"></a> `00bfef7c` | `e2 03 18 aa` | mov x2,x24 | `FALL_THROUGH`
<a id="insn-00bfef80"></a> `00bfef80` | `03 93 00 b9` | str w3,[x24, #0x90] | `FALL_THROUGH`
<a id="insn-00bfef84"></a> `00bfef84` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bfef88"></a> `00bfef88` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bfef8c"></a> `00bfef8c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bfef90"></a> `00bfef90` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bfef94"></a> `00bfef94` | `e4 03 14 aa` | mov x4,x20 | `FALL_THROUGH`
<a id="insn-00bfef98"></a> `00bfef98` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bfef9c"></a> `00bfef9c` | `00 01 00 b5` | cbnz x0,0x00bfefbc | `CONDITIONAL_JUMP`
<a id="insn-00bfefa0"></a> `00bfefa0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfefa4"></a> `00bfefa4` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bfefa8"></a> `00bfefa8` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfefac"></a> `00bfefac` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bfefb0"></a> `00bfefb0` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bfefb4"></a> `00bfefb4` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00bfefb8"></a> `00bfefb8` | `ee 64 01 94` | bl 0x00c58370 | `UNCONDITIONAL_CALL`
<a id="insn-00bfefbc"></a> `00bfefbc` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfefc0"></a> `00bfefc0` | `f0 64 01 94` | bl 0x00c58380 | `UNCONDITIONAL_CALL`
<a id="insn-00bfefc4"></a> `00bfefc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bfefc8"></a> `00bfefc8` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfefcc"></a> `00bfefcc` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfefd0"></a> `00bfefd0` | `f8 5f 43 a9` | ldp x24,x23,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfefd4"></a> `00bfefd4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfefd8"></a> `00bfefd8` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfefdc"></a> `00bfefdc` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfefe0"></a> `00bfefe0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfeeb8`](#insn-00bfeeb8) 範囲 `[['00bfeeb8', '00bfeeef']]`
  - `CONDITIONAL_JUMP` [`00bfeeec`](#insn-00bfeeec) → [`00bfefbc`](#insn-00bfefbc)
  - `FALL_THROUGH` [`00bfeeec`](#insn-00bfeeec) → [`00bfeef0`](#insn-00bfeef0)
- ブロック [`00bfeef0`](#insn-00bfeef0) 範囲 `[['00bfeef0', '00bfef3b']]`
  - `CONDITIONAL_JUMP` [`00bfef38`](#insn-00bfef38) → [`00bfef84`](#insn-00bfef84)
  - `FALL_THROUGH` [`00bfef38`](#insn-00bfef38) → [`00bfef3c`](#insn-00bfef3c)
- ブロック [`00bfef3c`](#insn-00bfef3c) 範囲 `[['00bfef3c', '00bfef83']]`
  - `FALL_THROUGH` [`00bfef80`](#insn-00bfef80) → [`00bfef84`](#insn-00bfef84)
- ブロック [`00bfef84`](#insn-00bfef84) 範囲 `[['00bfef84', '00bfef9f']]`
  - `CONDITIONAL_JUMP` [`00bfef9c`](#insn-00bfef9c) → [`00bfefbc`](#insn-00bfefbc)
  - `FALL_THROUGH` [`00bfef9c`](#insn-00bfef9c) → [`00bfefa0`](#insn-00bfefa0)
- ブロック [`00bfefa0`](#insn-00bfefa0) 範囲 `[['00bfefa0', '00bfefbb']]`
  - `FALL_THROUGH` [`00bfefb8`](#insn-00bfefb8) → [`00bfefbc`](#insn-00bfefbc)
- ブロック [`00bfefbc`](#insn-00bfefbc) 範囲 `[['00bfefbc', '00bfefe3']]`

## 命令位置別の参照

- [`00bfeec0`](#insn-00bfeec0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeec4`](#insn-00bfeec4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeec8`](#insn-00bfeec8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeecc`](#insn-00bfeecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeee4`](#insn-00bfeee4) → [`00c58330`](../00c58/00c58330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58330` · 推定シンボル `None` · 推定型 `None`
- [`00bfeee8`](#insn-00bfeee8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeeec`](#insn-00bfeeec) → [`00bfefbc`](#insn-00bfefbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfef00`](#insn-00bfef00) → [`00c58340`](../00c58/00c58340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58340` · 推定シンボル `None` · 推定型 `None`
- [`00bfef0c`](#insn-00bfef0c) → `00c9b908`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfef0c`](#insn-00bfef0c) → `01127c98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bfef10`](#insn-00bfef10) → [`00c58350`](../00c58/00c58350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58350` · 推定シンボル `None` · 推定型 `None`
- [`00bfef1c`](#insn-00bfef1c) → [`00c58360`](../00c58/00c58360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58360` · 推定シンボル `None` · 推定型 `None`
- [`00bfef38`](#insn-00bfef38) → [`00bfef84`](#insn-00bfef84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfef48`](#insn-00bfef48) → [`00c58340`](../00c58/00c58340.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58340` · 推定シンボル `None` · 推定型 `None`
- [`00bfef54`](#insn-00bfef54) → `00c9ad00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bfef54`](#insn-00bfef54) → `01127f18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bfef58`](#insn-00bfef58) → [`00c58350`](../00c58/00c58350.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58350` · 推定シンボル `None` · 推定型 `None`
- [`00bfef74`](#insn-00bfef74) → [`00c58360`](../00c58/00c58360.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58360` · 推定シンボル `None` · 推定型 `None`
- [`00bfef9c`](#insn-00bfef9c) → [`00bfefbc`](#insn-00bfefbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefb8`](#insn-00bfefb8) → [`00c58370`](../00c58/00c58370.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58370` · 推定シンボル `None` · 推定型 `None`
- [`00bfefc0`](#insn-00bfefc0) → [`00c58380`](../00c58/00c58380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58380` · 推定シンボル `None` · 推定型 `None`
- [`00bfefc8`](#insn-00bfefc8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefcc`](#insn-00bfefcc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefd0`](#insn-00bfefd0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefd4`](#insn-00bfefd4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfeec0`](#insn-00bfeec0)

~~~json
{
  "source": "00bfeec0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeec4`](#insn-00bfeec4)

~~~json
{
  "source": "00bfeec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeec8`](#insn-00bfeec8)

~~~json
{
  "source": "00bfeec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeecc`](#insn-00bfeecc)

~~~json
{
  "source": "00bfeecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeee4`](#insn-00bfeee4)

~~~json
{
  "source": "00bfeee4",
  "target": "00c58330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfeee8`](#insn-00bfeee8)

~~~json
{
  "source": "00bfeee8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeeec`](#insn-00bfeeec)

~~~json
{
  "source": "00bfeeec",
  "target": "00bfefbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfef00`](#insn-00bfef00)

~~~json
{
  "source": "00bfef00",
  "target": "00c58340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef0c`](#insn-00bfef0c)

~~~json
{
  "source": "00bfef0c",
  "target": "00c9b908",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b908",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfef0c`](#insn-00bfef0c)

~~~json
{
  "source": "00bfef0c",
  "target": "01127c98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfef10`](#insn-00bfef10)

~~~json
{
  "source": "00bfef10",
  "target": "00c58350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef1c`](#insn-00bfef1c)

~~~json
{
  "source": "00bfef1c",
  "target": "00c58360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef38`](#insn-00bfef38)

~~~json
{
  "source": "00bfef38",
  "target": "00bfef84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfef48`](#insn-00bfef48)

~~~json
{
  "source": "00bfef48",
  "target": "00c58340",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef54`](#insn-00bfef54)

~~~json
{
  "source": "00bfef54",
  "target": "00c9ad00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ad00",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bfef54`](#insn-00bfef54)

~~~json
{
  "source": "00bfef54",
  "target": "01127f18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127f18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfef58`](#insn-00bfef58)

~~~json
{
  "source": "00bfef58",
  "target": "00c58350",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef74`](#insn-00bfef74)

~~~json
{
  "source": "00bfef74",
  "target": "00c58360",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfef9c`](#insn-00bfef9c)

~~~json
{
  "source": "00bfef9c",
  "target": "00bfefbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefb8`](#insn-00bfefb8)

~~~json
{
  "source": "00bfefb8",
  "target": "00c58370",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfefc0`](#insn-00bfefc0)

~~~json
{
  "source": "00bfefc0",
  "target": "00c58380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfefc8`](#insn-00bfefc8)

~~~json
{
  "source": "00bfefc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefcc`](#insn-00bfefcc)

~~~json
{
  "source": "00bfefcc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefd0`](#insn-00bfefd0)

~~~json
{
  "source": "00bfefd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefd4`](#insn-00bfefd4)

~~~json
{
  "source": "00bfefd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
