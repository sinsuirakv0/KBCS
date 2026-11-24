# 00bf4cfc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf48d4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf4/00bf48d4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-c912fbdb4e667a4ab4739d12cf6a7fd6)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf4d98`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf4/00bf4d98.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-556dab66f70424c900fa076062e769bf)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf4cfc",
  "name": "_ZNSt6__ndk14stolERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "292961000c1938a2a7a84656a25de287bee7b38d7be3979a23619850113c5705",
  "source_text_sha256": "292961000c1938a2a7a84656a25de287bee7b38d7be3979a23619850113c5705",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf4cfc",
        "00bf4dff"
      ],
      [
        "00bf4e04",
        "00bf4e13"
      ]
    ],
    "bytes_sha256": "a927766c18f1a985ae18e50ebcaa70433733722d578474277feaf79eac3fa149",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00442930](../00442/00442930.md)
- [00481e80](../00481/00481e80.md)
- [00bf817c](../00bf8/00bf817c.md)
- [00c53f5c](../00c53/00c53f5c.md)
- [00c580c0](../00c58/00c580c0.md)
- [00c58590](../00c58/00c58590.md)
- [00c5e050](../00c5e/00c5e050.md)

## 関連文字列（未確認候補）

~~~text
": out of range"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1519 bytes

~~~c

long _ZNSt6__ndk14stolERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
               (byte *param_1,long *param_2,int param_3)

{
  int iVar1;
  int iVar2;
  int *piVar3;
  long lVar4;
  undefined8 uVar5;
  byte *__nptr;
  undefined1 local_70;
  undefined4 local_6f;
  undefined1 local_6b;
  byte local_58;
  undefined1 auStack_57 [15];
  undefined1 *local_48;
  char *local_28;
  
  local_70 = 8;
  local_6b = 0;
  local_6f = 0x6c6f7473;
  __nptr = *(byte **)(param_1 + 0x10);
  local_28 = (char *)0x0;
  if ((*param_1 & 1) == 0) {
    __nptr = param_1 + 1;
  }
  piVar3 = (int *)__errno();
  iVar1 = *piVar3;
  *piVar3 = 0;
  lVar4 = strtol((char *)__nptr,&local_28,param_3);
  iVar2 = *piVar3;
  *piVar3 = iVar1;
  if (iVar2 != 0x22) {
    if ((long)local_28 - (long)__nptr != 0) {
      if (param_2 != (long *)0x0) {
        *param_2 = (long)local_28 - (long)__nptr;
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
      return lVar4;
    }
    uVar5 = FUN_00bf817c(&local_70);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_58);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
                    /* WARNING: Subroutine does not return */
    FUN_00c53f5c(uVar5);
  }
  FUN_00481e80(&local_58,&local_70,": out of range");
  if ((local_58 & 1) == 0) {
    local_48 = auStack_57;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00442930(local_48);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf4cfc"></a> `00bf4cfc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf4d00"></a> `00bf4d00` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bf4d04"></a> `00bf4d04` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf4d08"></a> `00bf4d08` | `f7 23 00 f9` | str x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf4d0c"></a> `00bf4d0c` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf4d10"></a> `00bf4d10` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf4d14"></a> `00bf4d14` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bf4d18"></a> `00bf4d18` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00bf4d1c"></a> `00bf4d1c` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bf4d20"></a> `00bf4d20` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bf4d24"></a> `00bf4d24` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00bf4d28"></a> `00bf4d28` | `68 8e 8e 52` | mov w8,#0x7473 | `FALL_THROUGH`
<a id="insn-00bf4d2c"></a> `00bf4d2c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bf4d30"></a> `00bf4d30` | `e8 8d ad 72` | movk w8,#0x6c6f, LSL #16 | `FALL_THROUGH`
<a id="insn-00bf4d34"></a> `00bf4d34` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf4d38"></a> `00bf4d38` | `ff 17 00 39` | strb wzr,[sp, #0x5] | `FALL_THROUGH`
<a id="insn-00bf4d3c"></a> `00bf4d3c` | `e8 13 00 b8` | stur w8,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00bf4d40"></a> `00bf4d40` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bf4d44"></a> `00bf4d44` | `bf 0f 00 f9` | str xzr,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bf4d48"></a> `00bf4d48` | `14 15 80 9a` | csinc x20,x8,x0,ne | `FALL_THROUGH`
<a id="insn-00bf4d4c"></a> `00bf4d4c` | `dd 8c 01 94` | bl 0x00c580c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf4d50"></a> `00bf4d50` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bf4d54"></a> `00bf4d54` | `17 00 40 b9` | ldr w23,[x0] | `FALL_THROUGH`
<a id="insn-00bf4d58"></a> `00bf4d58` | `1f 00 00 b9` | str wzr,[x0] | `FALL_THROUGH`
<a id="insn-00bf4d5c"></a> `00bf4d5c` | `a1 63 00 91` | add x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bf4d60"></a> `00bf4d60` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bf4d64"></a> `00bf4d64` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bf4d68"></a> `00bf4d68` | `0a 8e 01 94` | bl 0x00c58590 | `UNCONDITIONAL_CALL`
<a id="insn-00bf4d6c"></a> `00bf4d6c` | `c8 02 40 b9` | ldr w8,[x22] | `FALL_THROUGH`
<a id="insn-00bf4d70"></a> `00bf4d70` | `d7 02 00 b9` | str w23,[x22] | `FALL_THROUGH`
<a id="insn-00bf4d74"></a> `00bf4d74` | `1f 89 00 71` | cmp w8,#0x22 | `FALL_THROUGH`
<a id="insn-00bf4d78"></a> `00bf4d78` | `20 02 00 54` | b.eq 0x00bf4dbc | `CONDITIONAL_JUMP`
<a id="insn-00bf4d7c"></a> `00bf4d7c` | `a8 0f 40 f9` | ldr x8,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bf4d80"></a> `00bf4d80` | `08 01 14 eb` | subs x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00bf4d84"></a> `00bf4d84` | `20 03 00 54` | b.eq 0x00bf4de8 | `CONDITIONAL_JUMP`
<a id="insn-00bf4d88"></a> `00bf4d88` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bf4d8c"></a> `00bf4d8c` | `53 00 00 b4` | cbz x19,0x00bf4d94 | `CONDITIONAL_JUMP`
<a id="insn-00bf4d90"></a> `00bf4d90` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bf4d94"></a> `00bf4d94` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf4d98"></a> `00bf4d98` | `ae a4 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bf4d9c"></a> `00bf4d9c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bf4da0"></a> `00bf4da0` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf4da4"></a> `00bf4da4` | `f7 23 40 f9` | ldr x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf4da8"></a> `00bf4da8` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf4dac"></a> `00bf4dac` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf4db0"></a> `00bf4db0` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bf4db4"></a> `00bf4db4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf4db8"></a> `00bf4db8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf4dbc"></a> `00bf4dbc` | `21 b6 ff b0` | adrp x1,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bf4dc0"></a> `00bf4dc0` | `21 18 37 91` | add x1,x1,#0xdc6 | `FALL_THROUGH`
<a id="insn-00bf4dc4"></a> `00bf4dc4` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf4dc8"></a> `00bf4dc8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf4dcc"></a> `00bf4dcc` | `f3 63 00 91` | add x19,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf4dd0"></a> `00bf4dd0` | `2c 34 e2 97` | bl 0x00481e80 | `UNCONDITIONAL_CALL`
<a id="insn-00bf4dd4"></a> `00bf4dd4` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bf4dd8"></a> `00bf4dd8` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bf4ddc"></a> `00bf4ddc` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf4de0"></a> `00bf4de0` | `20 15 93 9a` | csinc x0,x9,x19,ne | `FALL_THROUGH`
<a id="insn-00bf4de4"></a> `00bf4de4` | `d3 36 e1 97` | bl 0x00442930 | `CALL_TERMINATOR`
<a id="insn-00bf4de8"></a> `00bf4de8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf4dec"></a> `00bf4dec` | `e4 0c 00 94` | bl 0x00bf817c | `UNCONDITIONAL_CALL`
<a id="insn-00bf4df0"></a> `00bf4df0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bf4df4"></a> `00bf4df4` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf4df8"></a> `00bf4df8` | `96 a4 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bf4dfc"></a> `00bf4dfc` | `02 00 00 14` | b 0x00bf4e04 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf4e04"></a> `00bf4e04` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf4e08"></a> `00bf4e08` | `92 a4 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bf4e0c"></a> `00bf4e0c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bf4e10"></a> `00bf4e10` | `53 7c 01 94` | bl 0x00c53f5c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf4cfc`](#insn-00bf4cfc) 範囲 `[['00bf4cfc', '00bf4d7b']]`
  - `CONDITIONAL_JUMP` [`00bf4d78`](#insn-00bf4d78) → [`00bf4dbc`](#insn-00bf4dbc)
  - `FALL_THROUGH` [`00bf4d78`](#insn-00bf4d78) → [`00bf4d7c`](#insn-00bf4d7c)
- ブロック [`00bf4d7c`](#insn-00bf4d7c) 範囲 `[['00bf4d7c', '00bf4d87']]`
  - `CONDITIONAL_JUMP` [`00bf4d84`](#insn-00bf4d84) → [`00bf4de8`](#insn-00bf4de8)
  - `FALL_THROUGH` [`00bf4d84`](#insn-00bf4d84) → [`00bf4d88`](#insn-00bf4d88)
- ブロック [`00bf4d88`](#insn-00bf4d88) 範囲 `[['00bf4d88', '00bf4d8f']]`
  - `CONDITIONAL_JUMP` [`00bf4d8c`](#insn-00bf4d8c) → [`00bf4d94`](#insn-00bf4d94)
  - `FALL_THROUGH` [`00bf4d8c`](#insn-00bf4d8c) → [`00bf4d90`](#insn-00bf4d90)
- ブロック [`00bf4d90`](#insn-00bf4d90) 範囲 `[['00bf4d90', '00bf4d93']]`
  - `FALL_THROUGH` [`00bf4d90`](#insn-00bf4d90) → [`00bf4d94`](#insn-00bf4d94)
- ブロック [`00bf4d94`](#insn-00bf4d94) 範囲 `[['00bf4d94', '00bf4dbb']]`
- ブロック [`00bf4dbc`](#insn-00bf4dbc) 範囲 `[['00bf4dbc', '00bf4de7']]`
- ブロック [`00bf4de8`](#insn-00bf4de8) 範囲 `[['00bf4de8', '00bf4dff']]`
  - `UNCONDITIONAL_JUMP` [`00bf4dfc`](#insn-00bf4dfc) → [`00bf4e04`](#insn-00bf4e04)
- ブロック [`00bf4e04`](#insn-00bf4e04) 範囲 `[['00bf4e04', '00bf4e13']]`

## 命令位置別の参照

- [`00bf4d04`](#insn-00bf4d04) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d08`](#insn-00bf4d08) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d0c`](#insn-00bf4d0c) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d10`](#insn-00bf4d10) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d24`](#insn-00bf4d24) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d38`](#insn-00bf4d38) → `Stack[-0x6b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d3c`](#insn-00bf4d3c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d44`](#insn-00bf4d44) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d4c`](#insn-00bf4d4c) → [`00c580c0`](../00c58/00c580c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580c0` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d68`](#insn-00bf4d68) → [`00c58590`](../00c58/00c58590.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58590` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d78`](#insn-00bf4d78) → [`00bf4dbc`](#insn-00bf4dbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d7c`](#insn-00bf4d7c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d84`](#insn-00bf4d84) → [`00bf4de8`](#insn-00bf4de8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d8c`](#insn-00bf4d8c) → [`00bf4d94`](#insn-00bf4d94) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4d98`](#insn-00bf4d98) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bf4da0`](#insn-00bf4da0) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4da4`](#insn-00bf4da4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4da8`](#insn-00bf4da8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4dac`](#insn-00bf4dac) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4dc0`](#insn-00bf4dc0) → `002b9dc6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf4dd0`](#insn-00bf4dd0) → [`00481e80`](../00481/00481e80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00481e80` · 推定シンボル `None` · 推定型 `None`
- [`00bf4dd4`](#insn-00bf4dd4) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4dd8`](#insn-00bf4dd8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4de4`](#insn-00bf4de4) → [`00442930`](../00442/00442930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00442930` · 推定シンボル `None` · 推定型 `None`
- [`00bf4dec`](#insn-00bf4dec) → [`00bf817c`](../00bf8/00bf817c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bf817c` · 推定シンボル `None` · 推定型 `None`
- [`00bf4df8`](#insn-00bf4df8) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bf4dfc`](#insn-00bf4dfc) → [`00bf4e04`](#insn-00bf4e04) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf4e08`](#insn-00bf4e08) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bf4e10`](#insn-00bf4e10) → [`00c53f5c`](../00c53/00c53f5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53f5c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf4d04`](#insn-00bf4d04)

~~~json
{
  "source": "00bf4d04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d08`](#insn-00bf4d08)

~~~json
{
  "source": "00bf4d08",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d0c`](#insn-00bf4d0c)

~~~json
{
  "source": "00bf4d0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d10`](#insn-00bf4d10)

~~~json
{
  "source": "00bf4d10",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d24`](#insn-00bf4d24)

~~~json
{
  "source": "00bf4d24",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d38`](#insn-00bf4d38)

~~~json
{
  "source": "00bf4d38",
  "target": "Stack[-0x6b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d3c`](#insn-00bf4d3c)

~~~json
{
  "source": "00bf4d3c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d44`](#insn-00bf4d44)

~~~json
{
  "source": "00bf4d44",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d4c`](#insn-00bf4d4c)

~~~json
{
  "source": "00bf4d4c",
  "target": "00c580c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf4d68`](#insn-00bf4d68)

~~~json
{
  "source": "00bf4d68",
  "target": "00c58590",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf4d78`](#insn-00bf4d78)

~~~json
{
  "source": "00bf4d78",
  "target": "00bf4dbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d7c`](#insn-00bf4d7c)

~~~json
{
  "source": "00bf4d7c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d84`](#insn-00bf4d84)

~~~json
{
  "source": "00bf4d84",
  "target": "00bf4de8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d8c`](#insn-00bf4d8c)

~~~json
{
  "source": "00bf4d8c",
  "target": "00bf4d94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4d98`](#insn-00bf4d98)

~~~json
{
  "source": "00bf4d98",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf4da0`](#insn-00bf4da0)

~~~json
{
  "source": "00bf4da0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4da4`](#insn-00bf4da4)

~~~json
{
  "source": "00bf4da4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4da8`](#insn-00bf4da8)

~~~json
{
  "source": "00bf4da8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4dac`](#insn-00bf4dac)

~~~json
{
  "source": "00bf4dac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4dc0`](#insn-00bf4dc0)

~~~json
{
  "source": "00bf4dc0",
  "target": "002b9dc6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9dc6",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "3a206f7574206f662072616e676500",
  "capture_start": "002b9dc6",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf4dd0`](#insn-00bf4dd0)

~~~json
{
  "source": "00bf4dd0",
  "target": "00481e80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf4dd4`](#insn-00bf4dd4)

~~~json
{
  "source": "00bf4dd4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4dd8`](#insn-00bf4dd8)

~~~json
{
  "source": "00bf4dd8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4de4`](#insn-00bf4de4)

~~~json
{
  "source": "00bf4de4",
  "target": "00442930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf4dec`](#insn-00bf4dec)

~~~json
{
  "source": "00bf4dec",
  "target": "00bf817c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf4df8`](#insn-00bf4df8)

~~~json
{
  "source": "00bf4df8",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf4dfc`](#insn-00bf4dfc)

~~~json
{
  "source": "00bf4dfc",
  "target": "00bf4e04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf4e08`](#insn-00bf4e08)

~~~json
{
  "source": "00bf4e08",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf4e10`](#insn-00bf4e10)

~~~json
{
  "source": "00bf4e10",
  "target": "00c53f5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
