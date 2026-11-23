# 00abeec0

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00abef88`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00abe/00abef88.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/alignment_unresolved-0001.md#compare-e604891c40ab06e41f81d7dc6e4676b0)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00abeec0",
  "name": "FUN_00abeec0",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f770cb9c150ae929fc5920e6762607badb297d82bd592dcc4f2fa37947e80669",
  "source_text_sha256": "f770cb9c150ae929fc5920e6762607badb297d82bd592dcc4f2fa37947e80669",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00abeec0",
        "00abefb3"
      ],
      [
        "00abefbc",
        "00abefcf"
      ]
    ],
    "bytes_sha256": "14274b789c6e78857c460b16ec490748e11838115c916bf86ce45b2f320e0780",
    "instruction_count": 66,
    "instruction_bytes": 264,
    "body_bytes": 264,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00abe0c4](../00abe/00abe0c4.md)

## 呼び出し先

- [0041e380](../0041e/0041e380.md)
- [00bdaf40](../00bda/00bdaf40.md)
- [00bdaf60](../00bda/00bdaf60.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1675 bytes

~~~c

void FUN_00abeec0(long *param_1)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  void *__ptr;
  undefined8 *puVar3;
  undefined8 *puVar4;
  undefined8 *__ptr_00;
  ulong uVar5;
  undefined8 uVar6;
  
  puVar1 = (undefined8 *)param_1[1];
                    /* try { // try from 00abeed8 to 00bbefaf has its CatchHandler @ 00ac52f0 */
  __ptr_00 = (undefined8 *)*param_1;
  uVar5 = (long)puVar1 - (long)__ptr_00;
  if (uVar5 < (ulong)(param_1[2] - (long)__ptr_00)) {
    if (puVar1 == __ptr_00) {
      puVar2 = (undefined8 *)0x0;
    }
    else {
      if (0xaaaaaaaaaaaaaaa < (ulong)(((long)uVar5 >> 3) * -0x5555555555555555)) {
                    /* WARNING: Subroutine does not return */
        FUN_0041e380();
      }
      puVar2 = (undefined8 *)_Znwm(uVar5);
      uVar5 = (long)puVar2 + uVar5;
      puVar3 = puVar2;
      puVar4 = __ptr_00;
      do {
        uVar6 = *puVar4;
        puVar3[1] = puVar4[1];
        *puVar3 = uVar6;
        puVar3[2] = puVar4[2];
        puVar3 = puVar3 + 3;
        *puVar4 = 0;
        puVar4[1] = 0;
        puVar4[2] = 0;
        puVar4 = puVar4 + 3;
      } while (puVar4 != puVar1);
      do {
        __ptr = (void *)*__ptr_00;
        if (__ptr != (void *)0x0) {
          __ptr_00[1] = __ptr;
          _ZdlPv(__ptr);
        }
        __ptr_00 = __ptr_00 + 3;
      } while (__ptr_00 != puVar1);
      __ptr_00 = (undefined8 *)*param_1;
    }
    *param_1 = (long)puVar2;
    param_1[1] = uVar5;
    param_1[2] = uVar5;
    if (__ptr_00 != (undefined8 *)0x0) {
      _ZdlPv(__ptr_00);
      return;
    }
  }
                    /* try { // try from 00abefcc to 00bbeff7 has its CatchHandler @ 00ac5290 */
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00abeec0"></a> `00abeec0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00abeec4"></a> `00abeec4` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abeec8"></a> `00abeec8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abeecc"></a> `00abeecc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abeed0"></a> `00abeed0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00abeed4"></a> `00abeed4` | `17 a0 40 a9` | ldp x23,x8,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-00abeed8"></a> `00abeed8` | `13 00 40 f9` | ldr x19,[x0] | `FALL_THROUGH`
<a id="insn-00abeedc"></a> `00abeedc` | `08 01 13 cb` | sub x8,x8,x19 | `FALL_THROUGH`
<a id="insn-00abeee0"></a> `00abeee0` | `f5 02 13 cb` | sub x21,x23,x19 | `FALL_THROUGH`
<a id="insn-00abeee4"></a> `00abeee4` | `1f 01 15 eb` | cmp x8,x21 | `FALL_THROUGH`
<a id="insn-00abeee8"></a> `00abeee8` | `a9 06 00 54` | b.ls 0x00abefbc | `CONDITIONAL_JUMP`
<a id="insn-00abeeec"></a> `00abeeec` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00abeef0"></a> `00abeef0` | `ff 02 13 eb` | cmp x23,x19 | `FALL_THROUGH`
<a id="insn-00abeef4"></a> `00abeef4` | `a0 04 00 54` | b.eq 0x00abef88 | `CONDITIONAL_JUMP`
<a id="insn-00abeef8"></a> `00abeef8` | `a8 fe 43 93` | asr x8,x21,#0x3 | `FALL_THROUGH`
<a id="insn-00abeefc"></a> `00abeefc` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00abef00"></a> `00abef00` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00abef04"></a> `00abef04` | `08 7d 09 9b` | mul x8,x8,x9 | `FALL_THROUGH`
<a id="insn-00abef08"></a> `00abef08` | `e9 f3 01 b2` | orr x9,xzr,#-0x5555555555555556 | `FALL_THROUGH`
<a id="insn-00abef0c"></a> `00abef0c` | `69 55 95 f2` | movk x9,#0xaaab | `FALL_THROUGH`
<a id="insn-00abef10"></a> `00abef10` | `49 55 e1 f2` | movk x9,#0xaaa, LSL #48 | `FALL_THROUGH`
<a id="insn-00abef14"></a> `00abef14` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00abef18"></a> `00abef18` | `c2 04 00 54` | b.cs 0x00abefb0 | `CONDITIONAL_JUMP`
<a id="insn-00abef1c"></a> `00abef1c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00abef20"></a> `00abef20` | `08 70 04 94` | bl 0x00bdaf40 | `UNCONDITIONAL_CALL`
<a id="insn-00abef24"></a> `00abef24` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00abef28"></a> `00abef28` | `15 00 15 8b` | add x21,x0,x21 | `FALL_THROUGH`
<a id="insn-00abef2c"></a> `00abef2c` | `e8 03 00 aa` | mov x8,x0 | `FALL_THROUGH`
<a id="insn-00abef30"></a> `00abef30` | `e9 03 13 aa` | mov x9,x19 | `FALL_THROUGH`
<a id="insn-00abef34"></a> `00abef34` | `20 01 c0 3d` | ldr q0,[x9] | `FALL_THROUGH`
<a id="insn-00abef38"></a> `00abef38` | `00 01 80 3d` | str q0,[x8] | `FALL_THROUGH`
<a id="insn-00abef3c"></a> `00abef3c` | `2a 09 40 f9` | ldr x10,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00abef40"></a> `00abef40` | `0a 09 00 f9` | str x10,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00abef44"></a> `00abef44` | `08 61 00 91` | add x8,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00abef48"></a> `00abef48` | `3f 7d 00 a9` | stp xzr,xzr,[x9] | `FALL_THROUGH`
<a id="insn-00abef4c"></a> `00abef4c` | `3f 09 00 f9` | str xzr,[x9, #0x10] | `FALL_THROUGH`
<a id="insn-00abef50"></a> `00abef50` | `29 61 00 91` | add x9,x9,#0x18 | `FALL_THROUGH`
<a id="insn-00abef54"></a> `00abef54` | `3f 01 17 eb` | cmp x9,x23 | `FALL_THROUGH`
<a id="insn-00abef58"></a> `00abef58` | `e1 fe ff 54` | b.ne 0x00abef34 | `CONDITIONAL_JUMP`
<a id="insn-00abef5c"></a> `00abef5c` | `04 00 00 14` | b 0x00abef6c | `UNCONDITIONAL_JUMP`
<a id="insn-00abef60"></a> `00abef60` | `73 62 00 91` | add x19,x19,#0x18 | `FALL_THROUGH`
<a id="insn-00abef64"></a> `00abef64` | `7f 02 17 eb` | cmp x19,x23 | `FALL_THROUGH`
<a id="insn-00abef68"></a> `00abef68` | `c0 00 00 54` | b.eq 0x00abef80 | `CONDITIONAL_JUMP`
<a id="insn-00abef6c"></a> `00abef6c` | `60 02 40 f9` | ldr x0,[x19] | `FALL_THROUGH`
<a id="insn-00abef70"></a> `00abef70` | `80 ff ff b4` | cbz x0,0x00abef60 | `CONDITIONAL_JUMP`
<a id="insn-00abef74"></a> `00abef74` | `60 06 00 f9` | str x0,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00abef78"></a> `00abef78` | `fa 6f 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00abef7c"></a> `00abef7c` | `f9 ff ff 17` | b 0x00abef60 | `UNCONDITIONAL_JUMP`
<a id="insn-00abef80"></a> `00abef80` | `93 02 40 f9` | ldr x19,[x20] | `FALL_THROUGH`
<a id="insn-00abef84"></a> `00abef84` | `02 00 00 14` | b 0x00abef8c | `UNCONDITIONAL_JUMP`
<a id="insn-00abef88"></a> `00abef88` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00abef8c"></a> `00abef8c` | `96 56 00 a9` | stp x22,x21,[x20] | `FALL_THROUGH`
<a id="insn-00abef90"></a> `00abef90` | `95 0a 00 f9` | str x21,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00abef94"></a> `00abef94` | `53 01 00 b4` | cbz x19,0x00abefbc | `CONDITIONAL_JUMP`
<a id="insn-00abef98"></a> `00abef98` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00abef9c"></a> `00abef9c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abefa0"></a> `00abefa0` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abefa4"></a> `00abefa4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abefa8"></a> `00abefa8` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00abefac"></a> `00abefac` | `ed 6f 04 14` | b 0x00bdaf60 | `CALL_TERMINATOR`
<a id="insn-00abefb0"></a> `00abefb0` | `f4 7c e5 97` | bl 0x0041e380 | `CALL_TERMINATOR`
<a id="insn-00abefbc"></a> `00abefbc` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00abefc0"></a> `00abefc0` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00abefc4"></a> `00abefc4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00abefc8"></a> `00abefc8` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00abefcc"></a> `00abefcc` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00abeec0`](#insn-00abeec0) 範囲 `[['00abeec0', '00abeed7']]`
  - `FALL_THROUGH` [`00abeed4`](#insn-00abeed4) → [`00abeed8`](#insn-00abeed8)
- ブロック [`00abeed8`](#insn-00abeed8) 範囲 `[['00abeed8', '00abeeeb']]`
  - `CONDITIONAL_JUMP` [`00abeee8`](#insn-00abeee8) → [`00abefbc`](#insn-00abefbc)
  - `FALL_THROUGH` [`00abeee8`](#insn-00abeee8) → [`00abeeec`](#insn-00abeeec)
- ブロック [`00abeeec`](#insn-00abeeec) 範囲 `[['00abeeec', '00abeef7']]`
  - `CONDITIONAL_JUMP` [`00abeef4`](#insn-00abeef4) → [`00abef88`](#insn-00abef88)
  - `FALL_THROUGH` [`00abeef4`](#insn-00abeef4) → [`00abeef8`](#insn-00abeef8)
- ブロック [`00abeef8`](#insn-00abeef8) 範囲 `[['00abeef8', '00abef1b']]`
  - `CONDITIONAL_JUMP` [`00abef18`](#insn-00abef18) → [`00abefb0`](#insn-00abefb0)
  - `FALL_THROUGH` [`00abef18`](#insn-00abef18) → [`00abef1c`](#insn-00abef1c)
- ブロック [`00abef1c`](#insn-00abef1c) 範囲 `[['00abef1c', '00abef33']]`
  - `FALL_THROUGH` [`00abef30`](#insn-00abef30) → [`00abef34`](#insn-00abef34)
- ブロック [`00abef34`](#insn-00abef34) 範囲 `[['00abef34', '00abef5b']]`
  - `CONDITIONAL_JUMP` [`00abef58`](#insn-00abef58) → [`00abef34`](#insn-00abef34)
  - `FALL_THROUGH` [`00abef58`](#insn-00abef58) → [`00abef5c`](#insn-00abef5c)
- ブロック [`00abef5c`](#insn-00abef5c) 範囲 `[['00abef5c', '00abef5f']]`
  - `UNCONDITIONAL_JUMP` [`00abef5c`](#insn-00abef5c) → [`00abef6c`](#insn-00abef6c)
- ブロック [`00abef60`](#insn-00abef60) 範囲 `[['00abef60', '00abef6b']]`
  - `CONDITIONAL_JUMP` [`00abef68`](#insn-00abef68) → [`00abef80`](#insn-00abef80)
  - `FALL_THROUGH` [`00abef68`](#insn-00abef68) → [`00abef6c`](#insn-00abef6c)
- ブロック [`00abef6c`](#insn-00abef6c) 範囲 `[['00abef6c', '00abef73']]`
  - `CONDITIONAL_JUMP` [`00abef70`](#insn-00abef70) → [`00abef60`](#insn-00abef60)
  - `FALL_THROUGH` [`00abef70`](#insn-00abef70) → [`00abef74`](#insn-00abef74)
- ブロック [`00abef74`](#insn-00abef74) 範囲 `[['00abef74', '00abef7f']]`
  - `UNCONDITIONAL_JUMP` [`00abef7c`](#insn-00abef7c) → [`00abef60`](#insn-00abef60)
- ブロック [`00abef80`](#insn-00abef80) 範囲 `[['00abef80', '00abef87']]`
  - `UNCONDITIONAL_JUMP` [`00abef84`](#insn-00abef84) → [`00abef8c`](#insn-00abef8c)
- ブロック [`00abef88`](#insn-00abef88) 範囲 `[['00abef88', '00abef8b']]`
  - `FALL_THROUGH` [`00abef88`](#insn-00abef88) → [`00abef8c`](#insn-00abef8c)
- ブロック [`00abef8c`](#insn-00abef8c) 範囲 `[['00abef8c', '00abef97']]`
  - `CONDITIONAL_JUMP` [`00abef94`](#insn-00abef94) → [`00abefbc`](#insn-00abefbc)
  - `FALL_THROUGH` [`00abef94`](#insn-00abef94) → [`00abef98`](#insn-00abef98)
- ブロック [`00abef98`](#insn-00abef98) 範囲 `[['00abef98', '00abefaf']]`
- ブロック [`00abefb0`](#insn-00abefb0) 範囲 `[['00abefb0', '00abefb3']]`
- ブロック [`00abefbc`](#insn-00abefbc) 範囲 `[['00abefbc', '00abefcb']]`
  - `FALL_THROUGH` [`00abefc8`](#insn-00abefc8) → [`00abefcc`](#insn-00abefcc)
- ブロック [`00abefcc`](#insn-00abefcc) 範囲 `[['00abefcc', '00abefcf']]`

## 命令位置別の参照

- [`00abeec0`](#insn-00abeec0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeec4`](#insn-00abeec4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeec8`](#insn-00abeec8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeecc`](#insn-00abeecc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeee8`](#insn-00abeee8) → [`00abefbc`](#insn-00abefbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abeef4`](#insn-00abeef4) → [`00abef88`](#insn-00abef88) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef18`](#insn-00abef18) → [`00abefb0`](#insn-00abefb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef20`](#insn-00abef20) → [`00bdaf40`](../00bda/00bdaf40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf40` · 推定シンボル `None` · 推定型 `None`
- [`00abef58`](#insn-00abef58) → [`00abef34`](#insn-00abef34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef5c`](#insn-00abef5c) → [`00abef6c`](#insn-00abef6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef68`](#insn-00abef68) → [`00abef80`](#insn-00abef80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef70`](#insn-00abef70) → [`00abef60`](#insn-00abef60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef78`](#insn-00abef78) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abef7c`](#insn-00abef7c) → [`00abef60`](#insn-00abef60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef84`](#insn-00abef84) → [`00abef8c`](#insn-00abef8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef94`](#insn-00abef94) → [`00abefbc`](#insn-00abefbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abef9c`](#insn-00abef9c) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefa0`](#insn-00abefa0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefa4`](#insn-00abefa4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefa8`](#insn-00abefa8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefac`](#insn-00abefac) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00abefb0`](#insn-00abefb0) → [`0041e380`](../0041e/0041e380.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0041e380` · 推定シンボル `None` · 推定型 `None`
- [`00abefbc`](#insn-00abefbc) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefc0`](#insn-00abefc0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefc4`](#insn-00abefc4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00abefc8`](#insn-00abefc8) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00abeec0`](#insn-00abeec0)

~~~json
{
  "source": "00abeec0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeec4`](#insn-00abeec4)

~~~json
{
  "source": "00abeec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeec8`](#insn-00abeec8)

~~~json
{
  "source": "00abeec8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeecc`](#insn-00abeecc)

~~~json
{
  "source": "00abeecc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeee8`](#insn-00abeee8)

~~~json
{
  "source": "00abeee8",
  "target": "00abefbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abeef4`](#insn-00abeef4)

~~~json
{
  "source": "00abeef4",
  "target": "00abef88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef18`](#insn-00abef18)

~~~json
{
  "source": "00abef18",
  "target": "00abefb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef20`](#insn-00abef20)

~~~json
{
  "source": "00abef20",
  "target": "00bdaf40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abef58`](#insn-00abef58)

~~~json
{
  "source": "00abef58",
  "target": "00abef34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef5c`](#insn-00abef5c)

~~~json
{
  "source": "00abef5c",
  "target": "00abef6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef68`](#insn-00abef68)

~~~json
{
  "source": "00abef68",
  "target": "00abef80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef70`](#insn-00abef70)

~~~json
{
  "source": "00abef70",
  "target": "00abef60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef78`](#insn-00abef78)

~~~json
{
  "source": "00abef78",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abef7c`](#insn-00abef7c)

~~~json
{
  "source": "00abef7c",
  "target": "00abef60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef84`](#insn-00abef84)

~~~json
{
  "source": "00abef84",
  "target": "00abef8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef94`](#insn-00abef94)

~~~json
{
  "source": "00abef94",
  "target": "00abefbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abef9c`](#insn-00abef9c)

~~~json
{
  "source": "00abef9c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefa0`](#insn-00abefa0)

~~~json
{
  "source": "00abefa0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefa4`](#insn-00abefa4)

~~~json
{
  "source": "00abefa4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefa8`](#insn-00abefa8)

~~~json
{
  "source": "00abefa8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefac`](#insn-00abefac)

~~~json
{
  "source": "00abefac",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abefb0`](#insn-00abefb0)

~~~json
{
  "source": "00abefb0",
  "target": "0041e380",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00abefbc`](#insn-00abefbc)

~~~json
{
  "source": "00abefbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefc0`](#insn-00abefc0)

~~~json
{
  "source": "00abefc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefc4`](#insn-00abefc4)

~~~json
{
  "source": "00abefc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00abefc8`](#insn-00abefc8)

~~~json
{
  "source": "00abefc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
