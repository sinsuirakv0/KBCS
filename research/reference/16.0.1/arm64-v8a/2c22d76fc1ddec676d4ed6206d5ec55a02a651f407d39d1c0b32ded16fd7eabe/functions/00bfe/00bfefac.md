# 00bfefac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bfeb84`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bfe/00bfeb84.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0087.md#compare-6677facc252bb41b87db49a93b2c6b90)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bff048`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bff/00bff048.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0087.md#compare-b4ec2fa6ccef6d7c1c2dd15897ea49c2)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfefac",
  "name": "_ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEf",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "e17b500b0dd71ab07a4ba1b2f889ad42abbf79181132946298b7c4bfe42d3a18",
  "source_text_sha256": "e17b500b0dd71ab07a4ba1b2f889ad42abbf79181132946298b7c4bfe42d3a18",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfefac",
        "00bff0df"
      ]
    ],
    "bytes_sha256": "5b301fd0cf59e1647e7ef38b008cf46c6341b92e7d7111be672810bbd34eb0d0",
    "instruction_count": 77,
    "instruction_bytes": 308,
    "body_bytes": 308,
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

## 疑似コード / UTF-8 1577 bytes

~~~c

long * _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEf(float param_1,long *param_2)

{
  uint uVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  undefined8 uVar5;
  char local_58 [16];
  undefined1 auStack_48 [8];
  
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryC1ERS3_(local_58,param_2);
  if (local_58[0] != '\0') {
    _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,(long)param_2 + *(long *)(*param_2 + -0x18));
    plVar2 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                               (auStack_48,
                                PTR__ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE_00c9b838
                               );
    _ZNSt6__ndk16localeD1Ev(auStack_48);
    lVar4 = (long)param_2 + *(long *)(*param_2 + -0x18);
    uVar5 = *(undefined8 *)(lVar4 + 0x28);
    if (*(int *)(lVar4 + 0x90) == -1) {
      _ZNKSt6__ndk18ios_base6getlocEv(auStack_48,lVar4);
      plVar3 = (long *)_ZNKSt6__ndk16locale9use_facetERNS0_2idE
                                 (auStack_48,PTR__ZNSt6__ndk15ctypeIcE2idE_00c9ac30);
      uVar1 = (**(code **)(*plVar3 + 0x38))(plVar3,0x20);
      _ZNSt6__ndk16localeD1Ev(auStack_48);
      *(uint *)(lVar4 + 0x90) = uVar1 & 0xff;
    }
    lVar4 = (**(code **)(*plVar2 + 0x40))((double)param_1,plVar2,uVar5,lVar4);
    if (lVar4 == 0) {
      lVar4 = (long)param_2 + *(long *)(*param_2 + -0x18);
      _ZNSt6__ndk18ios_base5clearEj(lVar4,*(uint *)(lVar4 + 0x20) | 5);
    }
  }
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEE6sentryD2Ev(local_58);
  return param_2;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfefac"></a> `00bfefac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfefb0"></a> `00bfefb0` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bfefb4"></a> `00bfefb4` | `e8 13 00 fd` | str d8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfefb8"></a> `00bfefb8` | `fd fb 02 a9` | stp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bfefbc"></a> `00bfefbc` | `f7 1f 00 f9` | str x23,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bfefc0"></a> `00bfefc0` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bfefc4"></a> `00bfefc4` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bfefc8"></a> `00bfefc8` | `fd a3 00 91` | add x29,sp,#0x28 | `FALL_THROUGH`
<a id="insn-00bfefcc"></a> `00bfefcc` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-00bfefd0"></a> `00bfefd0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfefd4"></a> `00bfefd4` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bfefd8"></a> `00bfefd8` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bfefdc"></a> `00bfefdc` | `a1 64 01 94` | bl 0x00c58260 | `UNCONDITIONAL_CALL`
<a id="insn-00bfefe0"></a> `00bfefe0` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bfefe4"></a> `00bfefe4` | `88 06 00 34` | cbz w8,0x00bff0b4 | `CONDITIONAL_JUMP`
<a id="insn-00bfefe8"></a> `00bfefe8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bfefec"></a> `00bfefec` | `09 81 5e f8` | ldur x9,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bfeff0"></a> `00bfeff0` | `a8 43 00 d1` | sub x8,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00bfeff4"></a> `00bfeff4` | `60 02 09 8b` | add x0,x19,x9 | `FALL_THROUGH`
<a id="insn-00bfeff8"></a> `00bfeff8` | `9e 64 01 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00bfeffc"></a> `00bfeffc` | `e1 04 00 b0` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bff000"></a> `00bff000` | `a0 43 00 d1` | sub x0,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00bff004"></a> `00bff004` | `21 1c 44 f9` | ldr x1,[x1, #0x838] | `FALL_THROUGH`
<a id="insn-00bff008"></a> `00bff008` | `9e 64 01 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00bff00c"></a> `00bff00c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bff010"></a> `00bff010` | `a0 43 00 d1` | sub x0,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00bff014"></a> `00bff014` | `9f 64 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00bff018"></a> `00bff018` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bff01c"></a> `00bff01c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bff020"></a> `00bff020` | `62 02 08 8b` | add x2,x19,x8 | `FALL_THROUGH`
<a id="insn-00bff024"></a> `00bff024` | `43 90 40 b9` | ldr w3,[x2, #0x90] | `FALL_THROUGH`
<a id="insn-00bff028"></a> `00bff028` | `55 14 40 f9` | ldr x21,[x2, #0x28] | `FALL_THROUGH`
<a id="insn-00bff02c"></a> `00bff02c` | `7f 04 00 31` | cmn w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bff030"></a> `00bff030` | `61 02 00 54` | b.ne 0x00bff07c | `CONDITIONAL_JUMP`
<a id="insn-00bff034"></a> `00bff034` | `a8 43 00 d1` | sub x8,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00bff038"></a> `00bff038` | `e0 03 02 aa` | mov x0,x2 | `FALL_THROUGH`
<a id="insn-00bff03c"></a> `00bff03c` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bff040"></a> `00bff040` | `8c 64 01 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-00bff044"></a> `00bff044` | `c1 04 00 f0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-00bff048"></a> `00bff048` | `a0 43 00 d1` | sub x0,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00bff04c"></a> `00bff04c` | `21 18 46 f9` | ldr x1,[x1, #0xc30] | `FALL_THROUGH`
<a id="insn-00bff050"></a> `00bff050` | `8c 64 01 94` | bl 0x00c58280 | `UNCONDITIONAL_CALL`
<a id="insn-00bff054"></a> `00bff054` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bff058"></a> `00bff058` | `08 1d 40 f9` | ldr x8,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00bff05c"></a> `00bff05c` | `01 04 80 52` | mov w1,#0x20 | `FALL_THROUGH`
<a id="insn-00bff060"></a> `00bff060` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bff064"></a> `00bff064` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bff068"></a> `00bff068` | `a0 43 00 d1` | sub x0,x29,#0x10 | `FALL_THROUGH`
<a id="insn-00bff06c"></a> `00bff06c` | `89 64 01 94` | bl 0x00c58290 | `UNCONDITIONAL_CALL`
<a id="insn-00bff070"></a> `00bff070` | `c3 1e 00 12` | and w3,w22,#0xff | `FALL_THROUGH`
<a id="insn-00bff074"></a> `00bff074` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-00bff078"></a> `00bff078` | `e3 92 00 b9` | str w3,[x23, #0x90] | `FALL_THROUGH`
<a id="insn-00bff07c"></a> `00bff07c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bff080"></a> `00bff080` | `00 c1 22 1e` | fcvt d0,s8 | `FALL_THROUGH`
<a id="insn-00bff084"></a> `00bff084` | `08 21 40 f9` | ldr x8,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00bff088"></a> `00bff088` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bff08c"></a> `00bff08c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bff090"></a> `00bff090` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bff094"></a> `00bff094` | `00 01 00 b5` | cbnz x0,0x00bff0b4 | `CONDITIONAL_JUMP`
<a id="insn-00bff098"></a> `00bff098` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bff09c"></a> `00bff09c` | `a9 00 80 52` | mov w9,#0x5 | `FALL_THROUGH`
<a id="insn-00bff0a0"></a> `00bff0a0` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-00bff0a4"></a> `00bff0a4` | `60 02 08 8b` | add x0,x19,x8 | `FALL_THROUGH`
<a id="insn-00bff0a8"></a> `00bff0a8` | `08 20 40 b9` | ldr w8,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00bff0ac"></a> `00bff0ac` | `01 01 09 2a` | orr w1,w8,w9 | `FALL_THROUGH`
<a id="insn-00bff0b0"></a> `00bff0b0` | `7c 64 01 94` | bl 0x00c582a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bff0b4"></a> `00bff0b4` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bff0b8"></a> `00bff0b8` | `7e 64 01 94` | bl 0x00c582b0 | `UNCONDITIONAL_CALL`
<a id="insn-00bff0bc"></a> `00bff0bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bff0c0"></a> `00bff0c0` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bff0c4"></a> `00bff0c4` | `f7 1f 40 f9` | ldr x23,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bff0c8"></a> `00bff0c8` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bff0cc"></a> `00bff0cc` | `e8 13 40 fd` | ldr d8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bff0d0"></a> `00bff0d0` | `fd fb 42 a9` | ldp x29,x30,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bff0d4"></a> `00bff0d4` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bff0d8"></a> `00bff0d8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bff0dc"></a> `00bff0dc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfefac`](#insn-00bfefac) 範囲 `[['00bfefac', '00bfefe7']]`
  - `CONDITIONAL_JUMP` [`00bfefe4`](#insn-00bfefe4) → [`00bff0b4`](#insn-00bff0b4)
  - `FALL_THROUGH` [`00bfefe4`](#insn-00bfefe4) → [`00bfefe8`](#insn-00bfefe8)
- ブロック [`00bfefe8`](#insn-00bfefe8) 範囲 `[['00bfefe8', '00bff033']]`
  - `CONDITIONAL_JUMP` [`00bff030`](#insn-00bff030) → [`00bff07c`](#insn-00bff07c)
  - `FALL_THROUGH` [`00bff030`](#insn-00bff030) → [`00bff034`](#insn-00bff034)
- ブロック [`00bff034`](#insn-00bff034) 範囲 `[['00bff034', '00bff07b']]`
  - `FALL_THROUGH` [`00bff078`](#insn-00bff078) → [`00bff07c`](#insn-00bff07c)
- ブロック [`00bff07c`](#insn-00bff07c) 範囲 `[['00bff07c', '00bff097']]`
  - `CONDITIONAL_JUMP` [`00bff094`](#insn-00bff094) → [`00bff0b4`](#insn-00bff0b4)
  - `FALL_THROUGH` [`00bff094`](#insn-00bff094) → [`00bff098`](#insn-00bff098)
- ブロック [`00bff098`](#insn-00bff098) 範囲 `[['00bff098', '00bff0b3']]`
  - `FALL_THROUGH` [`00bff0b0`](#insn-00bff0b0) → [`00bff0b4`](#insn-00bff0b4)
- ブロック [`00bff0b4`](#insn-00bff0b4) 範囲 `[['00bff0b4', '00bff0df']]`

## 命令位置別の参照

- [`00bfefb4`](#insn-00bfefb4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefb8`](#insn-00bfefb8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefbc`](#insn-00bfefbc) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefc0`](#insn-00bfefc0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefc4`](#insn-00bfefc4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefdc`](#insn-00bfefdc) → [`00c58260`](../00c58/00c58260.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58260` · 推定シンボル `None` · 推定型 `None`
- [`00bfefe0`](#insn-00bfefe0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfefe4`](#insn-00bfefe4) → [`00bff0b4`](#insn-00bff0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfeff8`](#insn-00bfeff8) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00bff004`](#insn-00bff004) → `00c9b838`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bff004`](#insn-00bff004) → `01127b98`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk17num_putIcNS_19ostreambuf_iteratorIcNS_11char_traitsIcEEEEE2idE` · 推定型 `undefined8`
- [`00bff008`](#insn-00bff008) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00bff014`](#insn-00bff014) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00bff030`](#insn-00bff030) → [`00bff07c`](#insn-00bff07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff040`](#insn-00bff040) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`00bff04c`](#insn-00bff04c) → `00c9ac30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bff04c`](#insn-00bff04c) → `01127e18`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk15ctypeIcE2idE` · 推定型 `undefined8`
- [`00bff050`](#insn-00bff050) → [`00c58280`](../00c58/00c58280.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58280` · 推定シンボル `None` · 推定型 `None`
- [`00bff06c`](#insn-00bff06c) → [`00c58290`](../00c58/00c58290.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58290` · 推定シンボル `None` · 推定型 `None`
- [`00bff094`](#insn-00bff094) → [`00bff0b4`](#insn-00bff0b4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff0b0`](#insn-00bff0b0) → [`00c582a0`](../00c58/00c582a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582a0` · 推定シンボル `None` · 推定型 `None`
- [`00bff0b8`](#insn-00bff0b8) → [`00c582b0`](../00c58/00c582b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c582b0` · 推定シンボル `None` · 推定型 `None`
- [`00bff0c0`](#insn-00bff0c0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff0c4`](#insn-00bff0c4) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff0c8`](#insn-00bff0c8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff0cc`](#insn-00bff0cc) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bff0d0`](#insn-00bff0d0) → `Stack[-0x38]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfefb4`](#insn-00bfefb4)

~~~json
{
  "source": "00bfefb4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefb8`](#insn-00bfefb8)

~~~json
{
  "source": "00bfefb8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefbc`](#insn-00bfefbc)

~~~json
{
  "source": "00bfefbc",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefc0`](#insn-00bfefc0)

~~~json
{
  "source": "00bfefc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefc4`](#insn-00bfefc4)

~~~json
{
  "source": "00bfefc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefdc`](#insn-00bfefdc)

~~~json
{
  "source": "00bfefdc",
  "target": "00c58260",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfefe0`](#insn-00bfefe0)

~~~json
{
  "source": "00bfefe0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfefe4`](#insn-00bfefe4)

~~~json
{
  "source": "00bfefe4",
  "target": "00bff0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfeff8`](#insn-00bfeff8)

~~~json
{
  "source": "00bfeff8",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff004`](#insn-00bff004)

~~~json
{
  "source": "00bff004",
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
- 参照命令 [`00bff004`](#insn-00bff004)

~~~json
{
  "source": "00bff004",
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
- 参照命令 [`00bff008`](#insn-00bff008)

~~~json
{
  "source": "00bff008",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff014`](#insn-00bff014)

~~~json
{
  "source": "00bff014",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff030`](#insn-00bff030)

~~~json
{
  "source": "00bff030",
  "target": "00bff07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff040`](#insn-00bff040)

~~~json
{
  "source": "00bff040",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff04c`](#insn-00bff04c)

~~~json
{
  "source": "00bff04c",
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
- 参照命令 [`00bff04c`](#insn-00bff04c)

~~~json
{
  "source": "00bff04c",
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
- 参照命令 [`00bff050`](#insn-00bff050)

~~~json
{
  "source": "00bff050",
  "target": "00c58280",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff06c`](#insn-00bff06c)

~~~json
{
  "source": "00bff06c",
  "target": "00c58290",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff094`](#insn-00bff094)

~~~json
{
  "source": "00bff094",
  "target": "00bff0b4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff0b0`](#insn-00bff0b0)

~~~json
{
  "source": "00bff0b0",
  "target": "00c582a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff0b8`](#insn-00bff0b8)

~~~json
{
  "source": "00bff0b8",
  "target": "00c582b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bff0c0`](#insn-00bff0c0)

~~~json
{
  "source": "00bff0c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff0c4`](#insn-00bff0c4)

~~~json
{
  "source": "00bff0c4",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff0c8`](#insn-00bff0c8)

~~~json
{
  "source": "00bff0c8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff0cc`](#insn-00bff0cc)

~~~json
{
  "source": "00bff0cc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bff0d0`](#insn-00bff0d0)

~~~json
{
  "source": "00bff0d0",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
