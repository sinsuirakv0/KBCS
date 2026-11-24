# 004baacc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `004baa8c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ba/004baa8c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0006.md#compare-e9d98caa13ca105fa660bbf4e0d4b3ed)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `004bab0c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ba/004bab0c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/inspection-0006.md#compare-274c909760b51210ee088bda69251f09)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004baacc",
  "name": "_ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4_",
  "size": 252,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "88b3979b8c5ba87de1ff380792f19eceeca082f7b5a365ffc458e27a42bf22b0",
  "source_text_sha256": "88b3979b8c5ba87de1ff380792f19eceeca082f7b5a365ffc458e27a42bf22b0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004baacc",
        "004babc7"
      ]
    ],
    "bytes_sha256": "03fe21ce8b2a8df8625d737970dbe453506df2f4e27dd13c571fb0e1b9cf1df7",
    "instruction_count": 63,
    "instruction_bytes": 252,
    "body_bytes": 252,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c58d00](../00c58/00c58d00.md)

## 呼び出し先

- [00c58b20](../00c58/00c58b20.md)
- [00c58cf0](../00c58/00c58cf0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1330 bytes

~~~c

void _ZN5Botan6BigInt14random_integerERNS_21RandomNumberGeneratorERKS0_S4_
               (undefined8 *param_1,undefined8 param_2,undefined8 param_3,long *param_4)

{
  long lVar1;
  int iVar2;
  uint uVar3;
  ulong uVar4;
  ulong uVar5;
  long lVar6;
  
  lVar6 = *param_4;
  lVar1 = param_4[1];
  *param_1 = 0;
  param_1[1] = 0;
  param_1[2] = 0;
  uVar4 = lVar1 - lVar6 >> 2;
  *(undefined4 *)(param_1 + 3) = 1;
  uVar5 = uVar4;
  if (lVar1 - lVar6 == 0) {
LAB_004bab34:
    if (uVar5 == 0) {
      lVar6 = 0;
    }
    else {
      uVar5 = uVar5 - 1;
      if (uVar5 < uVar4) {
        uVar3 = *(uint *)(lVar6 + uVar5 * 4);
      }
      else {
        uVar3 = 0;
      }
      lVar6 = 0x20;
      do {
        if ((uVar3 >> (ulong)((int)lVar6 - 1U & 0x1f) & 1) != 0) break;
        lVar6 = lVar6 + -1;
      } while (lVar6 != 0);
      lVar6 = lVar6 + uVar5 * 0x20;
    }
  }
  else {
    do {
      if (*(int *)(lVar6 + -4 + uVar5 * 4) != 0) goto LAB_004bab34;
      uVar5 = uVar5 - 1;
    } while (uVar5 != 0);
    lVar6 = 0;
  }
  do {
    do {
      _ZN5Botan6BigInt9randomizeERNS_21RandomNumberGeneratorEmb(param_1,param_2,lVar6,0);
      iVar2 = _ZNK5Botan6BigInt3cmpERKS0_b(param_1,param_3,1);
    } while (iVar2 < 0);
    iVar2 = _ZNK5Botan6BigInt3cmpERKS0_b(param_1,param_4,1);
  } while (-1 < iVar2);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004baacc"></a> `004baacc` | `fd 7b bc a9` | stp x29,x30,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-004baad0"></a> `004baad0` | `f7 0b 00 f9` | str x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004baad4"></a> `004baad4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004baad8"></a> `004baad8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004baadc"></a> `004baadc` | `fd 03 00 91` | mov x29,sp | `FALL_THROUGH`
<a id="insn-004baae0"></a> `004baae0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004baae4"></a> `004baae4` | `48 24 40 a9` | ldp x8,x9,[x2] | `FALL_THROUGH`
<a id="insn-004baae8"></a> `004baae8` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-004baaec"></a> `004baaec` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-004baaf0"></a> `004baaf0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-004baaf4"></a> `004baaf4` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-004baaf8"></a> `004baaf8` | `7f 7e 00 a9` | stp xzr,xzr,[x19] | `FALL_THROUGH`
<a id="insn-004baafc"></a> `004baafc` | `29 01 08 eb` | subs x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004bab00"></a> `004bab00` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004bab04"></a> `004bab04` | `29 fd 42 93` | asr x9,x9,#0x2 | `FALL_THROUGH`
<a id="insn-004bab08"></a> `004bab08` | `6a 1a 00 b9` | str w10,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-004bab0c"></a> `004bab0c` | `20 01 00 54` | b.eq 0x004bab30 | `CONDITIONAL_JUMP`
<a id="insn-004bab10"></a> `004bab10` | `0b 11 00 d1` | sub x11,x8,#0x4 | `FALL_THROUGH`
<a id="insn-004bab14"></a> `004bab14` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-004bab18"></a> `004bab18` | `6c 79 6a b8` | ldr w12,[x11, x10, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004bab1c"></a> `004bab1c` | `cc 00 00 35` | cbnz w12,0x004bab34 | `CONDITIONAL_JUMP`
<a id="insn-004bab20"></a> `004bab20` | `4a 05 00 f1` | subs x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-004bab24"></a> `004bab24` | `a1 ff ff 54` | b.ne 0x004bab18 | `CONDITIONAL_JUMP`
<a id="insn-004bab28"></a> `004bab28` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-004bab2c"></a> `004bab2c` | `13 00 00 14` | b 0x004bab78 | `UNCONDITIONAL_JUMP`
<a id="insn-004bab30"></a> `004bab30` | `ea 03 09 aa` | mov x10,x9 | `FALL_THROUGH`
<a id="insn-004bab34"></a> `004bab34` | `ca 00 00 b4` | cbz x10,0x004bab4c | `CONDITIONAL_JUMP`
<a id="insn-004bab38"></a> `004bab38` | `4a 05 00 d1` | sub x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-004bab3c"></a> `004bab3c` | `3f 01 0a eb` | cmp x9,x10 | `FALL_THROUGH`
<a id="insn-004bab40"></a> `004bab40` | `a9 00 00 54` | b.ls 0x004bab54 | `CONDITIONAL_JUMP`
<a id="insn-004bab44"></a> `004bab44` | `09 79 6a b8` | ldr w9,[x8, x10, LSL #0x2] | `FALL_THROUGH`
<a id="insn-004bab48"></a> `004bab48` | `04 00 00 14` | b 0x004bab58 | `UNCONDITIONAL_JUMP`
<a id="insn-004bab4c"></a> `004bab4c` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-004bab50"></a> `004bab50` | `0a 00 00 14` | b 0x004bab78 | `UNCONDITIONAL_JUMP`
<a id="insn-004bab54"></a> `004bab54` | `e9 03 1f 2a` | mov w9,wzr | `FALL_THROUGH`
<a id="insn-004bab58"></a> `004bab58` | `48 e9 7b d3` | lsl x8,x10,#0x5 | `FALL_THROUGH`
<a id="insn-004bab5c"></a> `004bab5c` | `0a 04 80 52` | mov w10,#0x20 | `FALL_THROUGH`
<a id="insn-004bab60"></a> `004bab60` | `4b 05 00 51` | sub w11,w10,#0x1 | `FALL_THROUGH`
<a id="insn-004bab64"></a> `004bab64` | `2b 25 cb 1a` | lsr w11,w9,w11 | `FALL_THROUGH`
<a id="insn-004bab68"></a> `004bab68` | `6b 00 00 37` | tbnz w11,#0x0,0x004bab74 | `CONDITIONAL_JUMP`
<a id="insn-004bab6c"></a> `004bab6c` | `4a 05 00 f1` | subs x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-004bab70"></a> `004bab70` | `81 ff ff 54` | b.ne 0x004bab60 | `CONDITIONAL_JUMP`
<a id="insn-004bab74"></a> `004bab74` | `57 01 08 8b` | add x23,x10,x8 | `FALL_THROUGH`
<a id="insn-004bab78"></a> `004bab78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bab7c"></a> `004bab7c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-004bab80"></a> `004bab80` | `e2 03 17 aa` | mov x2,x23 | `FALL_THROUGH`
<a id="insn-004bab84"></a> `004bab84` | `e3 03 1f 2a` | mov w3,wzr | `FALL_THROUGH`
<a id="insn-004bab88"></a> `004bab88` | `5a 78 1e 94` | bl 0x00c58cf0 | `UNCONDITIONAL_CALL`
<a id="insn-004bab8c"></a> `004bab8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bab90"></a> `004bab90` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-004bab94"></a> `004bab94` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004bab98"></a> `004bab98` | `e2 77 1e 94` | bl 0x00c58b20 | `UNCONDITIONAL_CALL`
<a id="insn-004bab9c"></a> `004bab9c` | `e0 fe ff 37` | tbnz w0,#0x1f,0x004bab78 | `CONDITIONAL_JUMP`
<a id="insn-004baba0"></a> `004baba0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004baba4"></a> `004baba4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-004baba8"></a> `004baba8` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004babac"></a> `004babac` | `dd 77 1e 94` | bl 0x00c58b20 | `UNCONDITIONAL_CALL`
<a id="insn-004babb0"></a> `004babb0` | `40 fe ff 36` | tbz w0,#0x1f,0x004bab78 | `CONDITIONAL_JUMP`
<a id="insn-004babb4"></a> `004babb4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004babb8"></a> `004babb8` | `f7 0b 40 f9` | ldr x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-004babbc"></a> `004babbc` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004babc0"></a> `004babc0` | `fd 7b c4 a8` | ldp x29,x30,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-004babc4"></a> `004babc4` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004baacc`](#insn-004baacc) 範囲 `[['004baacc', '004bab0f']]`
  - `CONDITIONAL_JUMP` [`004bab0c`](#insn-004bab0c) → [`004bab30`](#insn-004bab30)
  - `FALL_THROUGH` [`004bab0c`](#insn-004bab0c) → [`004bab10`](#insn-004bab10)
- ブロック [`004bab10`](#insn-004bab10) 範囲 `[['004bab10', '004bab17']]`
  - `FALL_THROUGH` [`004bab14`](#insn-004bab14) → [`004bab18`](#insn-004bab18)
- ブロック [`004bab18`](#insn-004bab18) 範囲 `[['004bab18', '004bab1f']]`
  - `CONDITIONAL_JUMP` [`004bab1c`](#insn-004bab1c) → [`004bab34`](#insn-004bab34)
  - `FALL_THROUGH` [`004bab1c`](#insn-004bab1c) → [`004bab20`](#insn-004bab20)
- ブロック [`004bab20`](#insn-004bab20) 範囲 `[['004bab20', '004bab27']]`
  - `CONDITIONAL_JUMP` [`004bab24`](#insn-004bab24) → [`004bab18`](#insn-004bab18)
  - `FALL_THROUGH` [`004bab24`](#insn-004bab24) → [`004bab28`](#insn-004bab28)
- ブロック [`004bab28`](#insn-004bab28) 範囲 `[['004bab28', '004bab2f']]`
  - `UNCONDITIONAL_JUMP` [`004bab2c`](#insn-004bab2c) → [`004bab78`](#insn-004bab78)
- ブロック [`004bab30`](#insn-004bab30) 範囲 `[['004bab30', '004bab33']]`
  - `FALL_THROUGH` [`004bab30`](#insn-004bab30) → [`004bab34`](#insn-004bab34)
- ブロック [`004bab34`](#insn-004bab34) 範囲 `[['004bab34', '004bab37']]`
  - `CONDITIONAL_JUMP` [`004bab34`](#insn-004bab34) → [`004bab4c`](#insn-004bab4c)
  - `FALL_THROUGH` [`004bab34`](#insn-004bab34) → [`004bab38`](#insn-004bab38)
- ブロック [`004bab38`](#insn-004bab38) 範囲 `[['004bab38', '004bab43']]`
  - `CONDITIONAL_JUMP` [`004bab40`](#insn-004bab40) → [`004bab54`](#insn-004bab54)
  - `FALL_THROUGH` [`004bab40`](#insn-004bab40) → [`004bab44`](#insn-004bab44)
- ブロック [`004bab44`](#insn-004bab44) 範囲 `[['004bab44', '004bab4b']]`
  - `UNCONDITIONAL_JUMP` [`004bab48`](#insn-004bab48) → [`004bab58`](#insn-004bab58)
- ブロック [`004bab4c`](#insn-004bab4c) 範囲 `[['004bab4c', '004bab53']]`
  - `UNCONDITIONAL_JUMP` [`004bab50`](#insn-004bab50) → [`004bab78`](#insn-004bab78)
- ブロック [`004bab54`](#insn-004bab54) 範囲 `[['004bab54', '004bab57']]`
  - `FALL_THROUGH` [`004bab54`](#insn-004bab54) → [`004bab58`](#insn-004bab58)
- ブロック [`004bab58`](#insn-004bab58) 範囲 `[['004bab58', '004bab5f']]`
  - `FALL_THROUGH` [`004bab5c`](#insn-004bab5c) → [`004bab60`](#insn-004bab60)
- ブロック [`004bab60`](#insn-004bab60) 範囲 `[['004bab60', '004bab6b']]`
  - `CONDITIONAL_JUMP` [`004bab68`](#insn-004bab68) → [`004bab74`](#insn-004bab74)
  - `FALL_THROUGH` [`004bab68`](#insn-004bab68) → [`004bab6c`](#insn-004bab6c)
- ブロック [`004bab6c`](#insn-004bab6c) 範囲 `[['004bab6c', '004bab73']]`
  - `CONDITIONAL_JUMP` [`004bab70`](#insn-004bab70) → [`004bab60`](#insn-004bab60)
  - `FALL_THROUGH` [`004bab70`](#insn-004bab70) → [`004bab74`](#insn-004bab74)
- ブロック [`004bab74`](#insn-004bab74) 範囲 `[['004bab74', '004bab77']]`
  - `FALL_THROUGH` [`004bab74`](#insn-004bab74) → [`004bab78`](#insn-004bab78)
- ブロック [`004bab78`](#insn-004bab78) 範囲 `[['004bab78', '004bab9f']]`
  - `CONDITIONAL_JUMP` [`004bab9c`](#insn-004bab9c) → [`004bab78`](#insn-004bab78)
  - `FALL_THROUGH` [`004bab9c`](#insn-004bab9c) → [`004baba0`](#insn-004baba0)
- ブロック [`004baba0`](#insn-004baba0) 範囲 `[['004baba0', '004babb3']]`
  - `CONDITIONAL_JUMP` [`004babb0`](#insn-004babb0) → [`004bab78`](#insn-004bab78)
  - `FALL_THROUGH` [`004babb0`](#insn-004babb0) → [`004babb4`](#insn-004babb4)
- ブロック [`004babb4`](#insn-004babb4) 範囲 `[['004babb4', '004babc7']]`

## 命令位置別の参照

- [`004baacc`](#insn-004baacc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baad0`](#insn-004baad0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baad4`](#insn-004baad4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004baad8`](#insn-004baad8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab0c`](#insn-004bab0c) → [`004bab30`](#insn-004bab30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab1c`](#insn-004bab1c) → [`004bab34`](#insn-004bab34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab24`](#insn-004bab24) → [`004bab18`](#insn-004bab18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab2c`](#insn-004bab2c) → [`004bab78`](#insn-004bab78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab34`](#insn-004bab34) → [`004bab4c`](#insn-004bab4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab40`](#insn-004bab40) → [`004bab54`](#insn-004bab54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab48`](#insn-004bab48) → [`004bab58`](#insn-004bab58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab50`](#insn-004bab50) → [`004bab78`](#insn-004bab78) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab68`](#insn-004bab68) → [`004bab74`](#insn-004bab74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab70`](#insn-004bab70) → [`004bab60`](#insn-004bab60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bab88`](#insn-004bab88) → [`00c58cf0`](../00c58/00c58cf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58cf0` · 推定シンボル `None` · 推定型 `None`
- [`004bab98`](#insn-004bab98) → [`00c58b20`](../00c58/00c58b20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58b20` · 推定シンボル `None` · 推定型 `None`
- [`004bab9c`](#insn-004bab9c) → [`004bab78`](#insn-004bab78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004babac`](#insn-004babac) → [`00c58b20`](../00c58/00c58b20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58b20` · 推定シンボル `None` · 推定型 `None`
- [`004babb0`](#insn-004babb0) → [`004bab78`](#insn-004bab78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004babb4`](#insn-004babb4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004babb8`](#insn-004babb8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004babbc`](#insn-004babbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004babc0`](#insn-004babc0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004baacc`](#insn-004baacc)

~~~json
{
  "source": "004baacc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baad0`](#insn-004baad0)

~~~json
{
  "source": "004baad0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baad4`](#insn-004baad4)

~~~json
{
  "source": "004baad4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004baad8`](#insn-004baad8)

~~~json
{
  "source": "004baad8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab0c`](#insn-004bab0c)

~~~json
{
  "source": "004bab0c",
  "target": "004bab30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab1c`](#insn-004bab1c)

~~~json
{
  "source": "004bab1c",
  "target": "004bab34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab24`](#insn-004bab24)

~~~json
{
  "source": "004bab24",
  "target": "004bab18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab2c`](#insn-004bab2c)

~~~json
{
  "source": "004bab2c",
  "target": "004bab78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab34`](#insn-004bab34)

~~~json
{
  "source": "004bab34",
  "target": "004bab4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab40`](#insn-004bab40)

~~~json
{
  "source": "004bab40",
  "target": "004bab54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab48`](#insn-004bab48)

~~~json
{
  "source": "004bab48",
  "target": "004bab58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab50`](#insn-004bab50)

~~~json
{
  "source": "004bab50",
  "target": "004bab78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab68`](#insn-004bab68)

~~~json
{
  "source": "004bab68",
  "target": "004bab74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab70`](#insn-004bab70)

~~~json
{
  "source": "004bab70",
  "target": "004bab60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bab88`](#insn-004bab88)

~~~json
{
  "source": "004bab88",
  "target": "00c58cf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bab98`](#insn-004bab98)

~~~json
{
  "source": "004bab98",
  "target": "00c58b20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bab9c`](#insn-004bab9c)

~~~json
{
  "source": "004bab9c",
  "target": "004bab78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004babac`](#insn-004babac)

~~~json
{
  "source": "004babac",
  "target": "00c58b20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004babb0`](#insn-004babb0)

~~~json
{
  "source": "004babb0",
  "target": "004bab78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004babb4`](#insn-004babb4)

~~~json
{
  "source": "004babb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004babb8`](#insn-004babb8)

~~~json
{
  "source": "004babb8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004babbc`](#insn-004babbc)

~~~json
{
  "source": "004babbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004babc0`](#insn-004babc0)

~~~json
{
  "source": "004babc0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
