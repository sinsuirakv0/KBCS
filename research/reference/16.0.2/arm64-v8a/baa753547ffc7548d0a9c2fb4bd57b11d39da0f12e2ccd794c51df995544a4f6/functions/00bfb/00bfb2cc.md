# 00bfb2cc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bfb230`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bfb/00bfb230.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-00d986ea682c9ef189e1b5fbdde1cfe8)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bfc2c0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bfc/00bfc2c0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-a83f688a62cb4331ceae4a6b8664fe5f)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bfb2cc",
  "name": "_ZNSt6__ndk18ios_base5pwordEi",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9611b7119b6fe70e63528bceffcb321031120284ab2e966513aebd7c8abf5dd0",
  "source_text_sha256": "9611b7119b6fe70e63528bceffcb321031120284ab2e966513aebd7c8abf5dd0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bfb2cc",
        "00bfb3df"
      ]
    ],
    "bytes_sha256": "dc897dc084e808e6f374011c347523851e3caa3bc4bf4461ec3813415defc291",
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

- [00bfb5e0](../00bfb/00bfb5e0.md)
- [00c58160](../00c58/00c58160.md)
- [00c5a170](../00c5a/00c5a170.md)

## 関連文字列（未確認候補）

~~~text
"ios_base::clear"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1569 bytes

~~~c

undefined8 * _ZNSt6__ndk18ios_base5pwordEi(long param_1,int param_2)

{
  ulong uVar1;
  void *pvVar2;
  void *pvVar3;
  void *__s;
  uint uVar4;
  void *pvVar5;
  ulong uVar6;
  ulong uVar7;
  
  uVar1 = (long)param_2 + 1;
  if (*(ulong *)(param_1 + 0x80) < uVar1) {
    uVar6 = *(long *)(param_1 + 0x68) * 2;
    if (uVar6 < uVar1 || uVar6 - uVar1 == 0) {
      uVar6 = uVar1;
    }
    if (0xffffffffffffffe < uVar1) {
      uVar6 = 0x1fffffffffffffff;
    }
    pvVar5 = realloc(*(void **)(param_1 + 0x70),uVar6 * 8);
    if (pvVar5 == (void *)0x0) {
      uVar4 = *(uint *)(param_1 + 0x20) | 1;
      *(uint *)(param_1 + 0x20) = uVar4;
      if ((*(uint *)(param_1 + 0x24) & uVar4) == 0) {
        DAT_011274a8 = 0;
        return &DAT_011274a8;
      }
                    /* WARNING: Subroutine does not return */
      FUN_00bfb5e0("ios_base::clear");
    }
    uVar7 = *(ulong *)(param_1 + 0x78);
    *(void **)(param_1 + 0x70) = pvVar5;
    if ((long)uVar7 < (long)uVar6) {
      pvVar3 = (void *)(uVar6 * 8 + (long)pvVar5);
      __s = (void *)((long)pvVar5 + uVar7 * 8);
      pvVar2 = (void *)((long)__s + 8);
      if (pvVar2 <= pvVar3) {
        pvVar2 = pvVar3;
      }
      memset(__s,0,((long)pvVar2 + uVar7 * -8 + ~(ulong)pvVar5 & 0xfffffffffffffff8) + 8);
    }
    *(ulong *)(param_1 + 0x80) = uVar6;
  }
  else {
    pvVar5 = *(void **)(param_1 + 0x70);
    uVar7 = *(ulong *)(param_1 + 0x78);
  }
  if (uVar7 <= uVar1) {
    uVar7 = uVar1;
  }
  *(ulong *)(param_1 + 0x78) = uVar7;
  return (undefined8 *)((long)pvVar5 + (long)param_2 * 8);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bfb2cc"></a> `00bfb2cc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bfb2d0"></a> `00bfb2d0` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bfb2d4"></a> `00bfb2d4` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb2d8"></a> `00bfb2d8` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb2dc"></a> `00bfb2dc` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfb2e0"></a> `00bfb2e0` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-00bfb2e4"></a> `00bfb2e4` | `35 7c 40 93` | sxtw x21,w1 | `FALL_THROUGH`
<a id="insn-00bfb2e8"></a> `00bfb2e8` | `08 40 40 f9` | ldr x8,[x0, #0x80] | `FALL_THROUGH`
<a id="insn-00bfb2ec"></a> `00bfb2ec` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bfb2f0"></a> `00bfb2f0` | `b6 06 00 91` | add x22,x21,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb2f4"></a> `00bfb2f4` | `df 02 08 eb` | cmp x22,x8 | `FALL_THROUGH`
<a id="insn-00bfb2f8"></a> `00bfb2f8` | `69 04 00 54` | b.ls 0x00bfb384 | `CONDITIONAL_JUMP`
<a id="insn-00bfb2fc"></a> `00bfb2fc` | `68 82 46 a9` | ldp x8,x0,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00bfb300"></a> `00bfb300` | `09 00 fe 92` | mov x9,#0xfffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfb304"></a> `00bfb304` | `08 f9 7f d3` | lsl x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb308"></a> `00bfb308` | `1f 01 16 eb` | cmp x8,x22 | `FALL_THROUGH`
<a id="insn-00bfb30c"></a> `00bfb30c` | `08 81 96 9a` | csel x8,x8,x22,hi | `FALL_THROUGH`
<a id="insn-00bfb310"></a> `00bfb310` | `df 02 09 eb` | cmp x22,x9 | `FALL_THROUGH`
<a id="insn-00bfb314"></a> `00bfb314` | `09 00 fc 92` | mov x9,#0x1fffffffffffffff | `FALL_THROUGH`
<a id="insn-00bfb318"></a> `00bfb318` | `17 31 89 9a` | csel x23,x8,x9,cc | `FALL_THROUGH`
<a id="insn-00bfb31c"></a> `00bfb31c` | `f4 f2 7d d3` | lsl x20,x23,#0x3 | `FALL_THROUGH`
<a id="insn-00bfb320"></a> `00bfb320` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bfb324"></a> `00bfb324` | `93 7b 01 94` | bl 0x00c5a170 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb328"></a> `00bfb328` | `40 04 00 b4` | cbz x0,0x00bfb3b0 | `CONDITIONAL_JUMP`
<a id="insn-00bfb32c"></a> `00bfb32c` | `78 3e 40 f9` | ldr x24,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00bfb330"></a> `00bfb330` | `60 3a 00 f9` | str x0,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00bfb334"></a> `00bfb334` | `1f 03 17 eb` | cmp x24,x23 | `FALL_THROUGH`
<a id="insn-00bfb338"></a> `00bfb338` | `2a 02 00 54` | b.ge 0x00bfb37c | `CONDITIONAL_JUMP`
<a id="insn-00bfb33c"></a> `00bfb33c` | `09 f3 7d d3` | lsl x9,x24,#0x3 | `FALL_THROUGH`
<a id="insn-00bfb340"></a> `00bfb340` | `8b 02 00 8b` | add x11,x20,x0 | `FALL_THROUGH`
<a id="insn-00bfb344"></a> `00bfb344` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bfb348"></a> `00bfb348` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00bfb34c"></a> `00bfb34c` | `08 00 09 8b` | add x8,x0,x9 | `FALL_THROUGH`
<a id="insn-00bfb350"></a> `00bfb350` | `0a 21 00 91` | add x10,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00bfb354"></a> `00bfb354` | `5f 01 0b eb` | cmp x10,x11 | `FALL_THROUGH`
<a id="insn-00bfb358"></a> `00bfb358` | `4a 81 8b 9a` | csel x10,x10,x11,hi | `FALL_THROUGH`
<a id="insn-00bfb35c"></a> `00bfb35c` | `eb 03 20 aa` | mvn x11,x0 | `FALL_THROUGH`
<a id="insn-00bfb360"></a> `00bfb360` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bfb364"></a> `00bfb364` | `4a 01 0b 8b` | add x10,x10,x11 | `FALL_THROUGH`
<a id="insn-00bfb368"></a> `00bfb368` | `49 01 09 cb` | sub x9,x10,x9 | `FALL_THROUGH`
<a id="insn-00bfb36c"></a> `00bfb36c` | `29 f1 7d 92` | and x9,x9,#-0x8 | `FALL_THROUGH`
<a id="insn-00bfb370"></a> `00bfb370` | `22 21 00 91` | add x2,x9,#0x8 | `FALL_THROUGH`
<a id="insn-00bfb374"></a> `00bfb374` | `7b 73 01 94` | bl 0x00c58160 | `UNCONDITIONAL_CALL`
<a id="insn-00bfb378"></a> `00bfb378` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bfb37c"></a> `00bfb37c` | `77 42 00 f9` | str x23,[x19, #0x80] | `FALL_THROUGH`
<a id="insn-00bfb380"></a> `00bfb380` | `02 00 00 14` | b 0x00bfb388 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfb384"></a> `00bfb384` | `60 62 47 a9` | ldp x0,x24,[x19, #0x70] | `FALL_THROUGH`
<a id="insn-00bfb388"></a> `00bfb388` | `1f 03 16 eb` | cmp x24,x22 | `FALL_THROUGH`
<a id="insn-00bfb38c"></a> `00bfb38c` | `00 0c 15 8b` | add x0,x0,x21, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00bfb390"></a> `00bfb390` | `08 83 96 9a` | csel x8,x24,x22,hi | `FALL_THROUGH`
<a id="insn-00bfb394"></a> `00bfb394` | `68 3e 00 f9` | str x8,[x19, #0x78] | `FALL_THROUGH`
<a id="insn-00bfb398"></a> `00bfb398` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bfb39c"></a> `00bfb39c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb3a0"></a> `00bfb3a0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bfb3a4"></a> `00bfb3a4` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bfb3a8"></a> `00bfb3a8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bfb3ac"></a> `00bfb3ac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bfb3b0"></a> `00bfb3b0` | `68 26 44 29` | ldp w8,w9,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb3b4"></a> `00bfb3b4` | `08 01 00 32` | orr w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bfb3b8"></a> `00bfb3b8` | `3f 01 08 6a` | tst w9,w8 | `FALL_THROUGH`
<a id="insn-00bfb3bc"></a> `00bfb3bc` | `68 22 00 b9` | str w8,[x19, #0x20] | `FALL_THROUGH`
<a id="insn-00bfb3c0"></a> `00bfb3c0` | `a1 00 00 54` | b.ne 0x00bfb3d4 | `CONDITIONAL_JUMP`
<a id="insn-00bfb3c4"></a> `00bfb3c4` | `60 29 00 90` | adrp x0,0x1127000 | `FALL_THROUGH`
<a id="insn-00bfb3c8"></a> `00bfb3c8` | `00 a0 12 91` | add x0,x0,#0x4a8 | `FALL_THROUGH`
<a id="insn-00bfb3cc"></a> `00bfb3cc` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-00bfb3d0"></a> `00bfb3d0` | `f2 ff ff 17` | b 0x00bfb398 | `UNCONDITIONAL_JUMP`
<a id="insn-00bfb3d4"></a> `00bfb3d4` | `60 b5 ff 90` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bfb3d8"></a> `00bfb3d8` | `00 68 13 91` | add x0,x0,#0x4da | `FALL_THROUGH`
<a id="insn-00bfb3dc"></a> `00bfb3dc` | `81 00 00 94` | bl 0x00bfb5e0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bfb2cc`](#insn-00bfb2cc) 範囲 `[['00bfb2cc', '00bfb2fb']]`
  - `CONDITIONAL_JUMP` [`00bfb2f8`](#insn-00bfb2f8) → [`00bfb384`](#insn-00bfb384)
  - `FALL_THROUGH` [`00bfb2f8`](#insn-00bfb2f8) → [`00bfb2fc`](#insn-00bfb2fc)
- ブロック [`00bfb2fc`](#insn-00bfb2fc) 範囲 `[['00bfb2fc', '00bfb32b']]`
  - `CONDITIONAL_JUMP` [`00bfb328`](#insn-00bfb328) → [`00bfb3b0`](#insn-00bfb3b0)
  - `FALL_THROUGH` [`00bfb328`](#insn-00bfb328) → [`00bfb32c`](#insn-00bfb32c)
- ブロック [`00bfb32c`](#insn-00bfb32c) 範囲 `[['00bfb32c', '00bfb33b']]`
  - `CONDITIONAL_JUMP` [`00bfb338`](#insn-00bfb338) → [`00bfb37c`](#insn-00bfb37c)
  - `FALL_THROUGH` [`00bfb338`](#insn-00bfb338) → [`00bfb33c`](#insn-00bfb33c)
- ブロック [`00bfb33c`](#insn-00bfb33c) 範囲 `[['00bfb33c', '00bfb37b']]`
  - `FALL_THROUGH` [`00bfb378`](#insn-00bfb378) → [`00bfb37c`](#insn-00bfb37c)
- ブロック [`00bfb37c`](#insn-00bfb37c) 範囲 `[['00bfb37c', '00bfb383']]`
  - `UNCONDITIONAL_JUMP` [`00bfb380`](#insn-00bfb380) → [`00bfb388`](#insn-00bfb388)
- ブロック [`00bfb384`](#insn-00bfb384) 範囲 `[['00bfb384', '00bfb387']]`
  - `FALL_THROUGH` [`00bfb384`](#insn-00bfb384) → [`00bfb388`](#insn-00bfb388)
- ブロック [`00bfb388`](#insn-00bfb388) 範囲 `[['00bfb388', '00bfb397']]`
  - `FALL_THROUGH` [`00bfb394`](#insn-00bfb394) → [`00bfb398`](#insn-00bfb398)
- ブロック [`00bfb398`](#insn-00bfb398) 範囲 `[['00bfb398', '00bfb3af']]`
- ブロック [`00bfb3b0`](#insn-00bfb3b0) 範囲 `[['00bfb3b0', '00bfb3c3']]`
  - `CONDITIONAL_JUMP` [`00bfb3c0`](#insn-00bfb3c0) → [`00bfb3d4`](#insn-00bfb3d4)
  - `FALL_THROUGH` [`00bfb3c0`](#insn-00bfb3c0) → [`00bfb3c4`](#insn-00bfb3c4)
- ブロック [`00bfb3c4`](#insn-00bfb3c4) 範囲 `[['00bfb3c4', '00bfb3d3']]`
  - `UNCONDITIONAL_JUMP` [`00bfb3d0`](#insn-00bfb3d0) → [`00bfb398`](#insn-00bfb398)
- ブロック [`00bfb3d4`](#insn-00bfb3d4) 範囲 `[['00bfb3d4', '00bfb3df']]`

## 命令位置別の参照

- [`00bfb2d0`](#insn-00bfb2d0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb2d4`](#insn-00bfb2d4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb2d8`](#insn-00bfb2d8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb2dc`](#insn-00bfb2dc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb2f8`](#insn-00bfb2f8) → [`00bfb384`](#insn-00bfb384) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb324`](#insn-00bfb324) → [`00c5a170`](../00c5a/00c5a170.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a170` · 推定シンボル `None` · 推定型 `None`
- [`00bfb328`](#insn-00bfb328) → [`00bfb3b0`](#insn-00bfb3b0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb338`](#insn-00bfb338) → [`00bfb37c`](#insn-00bfb37c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb374`](#insn-00bfb374) → [`00c58160`](../00c58/00c58160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58160` · 推定シンボル `None` · 推定型 `None`
- [`00bfb380`](#insn-00bfb380) → [`00bfb388`](#insn-00bfb388) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb398`](#insn-00bfb398) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb39c`](#insn-00bfb39c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb3a0`](#insn-00bfb3a0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb3a4`](#insn-00bfb3a4) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb3c0`](#insn-00bfb3c0) → [`00bfb3d4`](#insn-00bfb3d4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb3c8`](#insn-00bfb3c8) → `011274a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bfb3cc`](#insn-00bfb3cc) → `011274a8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bfb3d0`](#insn-00bfb3d0) → [`00bfb398`](#insn-00bfb398) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bfb3d8`](#insn-00bfb3d8) → `002a74da`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bfb3dc`](#insn-00bfb3dc) → [`00bfb5e0`](00bfb5e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bfb5e0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bfb2d0`](#insn-00bfb2d0)

~~~json
{
  "source": "00bfb2d0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb2d4`](#insn-00bfb2d4)

~~~json
{
  "source": "00bfb2d4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb2d8`](#insn-00bfb2d8)

~~~json
{
  "source": "00bfb2d8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb2dc`](#insn-00bfb2dc)

~~~json
{
  "source": "00bfb2dc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb2f8`](#insn-00bfb2f8)

~~~json
{
  "source": "00bfb2f8",
  "target": "00bfb384",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb324`](#insn-00bfb324)

~~~json
{
  "source": "00bfb324",
  "target": "00c5a170",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb328`](#insn-00bfb328)

~~~json
{
  "source": "00bfb328",
  "target": "00bfb3b0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb338`](#insn-00bfb338)

~~~json
{
  "source": "00bfb338",
  "target": "00bfb37c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb374`](#insn-00bfb374)

~~~json
{
  "source": "00bfb374",
  "target": "00c58160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bfb380`](#insn-00bfb380)

~~~json
{
  "source": "00bfb380",
  "target": "00bfb388",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb398`](#insn-00bfb398)

~~~json
{
  "source": "00bfb398",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb39c`](#insn-00bfb39c)

~~~json
{
  "source": "00bfb39c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb3a0`](#insn-00bfb3a0)

~~~json
{
  "source": "00bfb3a0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb3a4`](#insn-00bfb3a4)

~~~json
{
  "source": "00bfb3a4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb3c0`](#insn-00bfb3c0)

~~~json
{
  "source": "00bfb3c0",
  "target": "00bfb3d4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb3c8`](#insn-00bfb3c8)

~~~json
{
  "source": "00bfb3c8",
  "target": "011274a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011274a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfb3cc`](#insn-00bfb3cc)

~~~json
{
  "source": "00bfb3cc",
  "target": "011274a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011274a8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bfb3d0`](#insn-00bfb3d0)

~~~json
{
  "source": "00bfb3d0",
  "target": "00bfb398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bfb3d8`](#insn-00bfb3d8)

~~~json
{
  "source": "00bfb3d8",
  "target": "002a74da",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a74da",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "696f735f626173653a3a636c65617200",
  "capture_start": "002a74da",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bfb3dc`](#insn-00bfb3dc)

~~~json
{
  "source": "00bfb3dc",
  "target": "00bfb5e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
