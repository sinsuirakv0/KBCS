# 009adbcc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `009adb78`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/009ad/009adb78.md) · 移動量 `+0x54`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/alignment_unresolved-0004.md#compare-622f25ceb1aa7cc5555383c10cfdcdb6)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `009aeb78`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/009ae/009aeb78.md) · 移動量 `+0xfac`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0024.md#compare-e25ae1c35c5ebcf815a68c8e25748880)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "009adbcc",
  "name": "FUN_009adbcc",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "21a697e71986c819f2980888ad13033e509049cddfbfb3f808bc45f8bbef7046",
  "source_text_sha256": "21a697e71986c819f2980888ad13033e509049cddfbfb3f808bc45f8bbef7046",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "009adbcc",
        "009adcaf"
      ],
      [
        "009adcd4",
        "009adcd7"
      ]
    ],
    "bytes_sha256": "4fe5cc29d37b493ed981dced97b86b0b676097548b0e94d241da9ae786971678",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

- [0072b1f8](../0072b/0072b1f8.md)
- [00793960](../00793/00793960.md)

## 呼び出し先

- [009b5ce8](../009b5/009b5ce8.md)
- [00c53d70](../00c53/00c53d70.md)
- [00c53da0](../00c53/00c53da0.md)
- [00c57f50](../00c57/00c57f50.md)
- [00c57fb0](../00c57/00c57fb0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1316 bytes

~~~c

undefined8 FUN_009adbcc(long *param_1,int param_2)

{
  undefined8 *puVar1;
  undefined8 *puVar2;
  long *plVar3;
  long lVar4;
  int iVar5;
  long lVar6;
  long lVar7;
  undefined8 uVar8;
  undefined8 *puVar9;
  
                    /* catch() { ... } // from try @ 009ad938 with catch @ 009adbd0 */
                    /* catch() { ... } // from try @ 009ad9c4 with catch @ 009adbe4 */
  lVar4 = tpidr_el0;
  lVar7 = *(long *)(lVar4 + 0x28);
  puVar9 = (undefined8 *)*param_1;
  puVar2 = (undefined8 *)param_1[1];
  if (puVar9 == puVar2) {
    uVar8 = 0;
  }
  else {
    uVar8 = 0;
    do {
      puVar1 = (undefined8 *)*puVar9;
      plVar3 = (long *)puVar9[1];
      if (plVar3 != (long *)0x0) {
        FUN_00c53d70(1,plVar3 + 1);
      }
      iVar5 = FUN_009b5ce8(puVar1);
      if (iVar5 == param_2) {
        uVar8 = *puVar1;
      }
      if ((plVar3 != (long *)0x0) &&
         (lVar6 = FUN_00c53da0(0xffffffffffffffff,plVar3 + 1), lVar6 == 0)) {
        (**(code **)(*plVar3 + 0x10))(plVar3);
        _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar3);
      }
    } while ((iVar5 != param_2) && (puVar9 = puVar9 + 2, puVar9 != puVar2));
  }
  if (*(long *)(lVar4 + 0x28) != lVar7) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar8;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-009adbcc"></a> `009adbcc` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009adbd0"></a> `009adbd0` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009adbd4"></a> `009adbd4` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009adbd8"></a> `009adbd8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009adbdc"></a> `009adbdc` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009adbe0"></a> `009adbe0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009adbe4"></a> `009adbe4` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-009adbe8"></a> `009adbe8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-009adbec"></a> `009adbec` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009adbf0"></a> `009adbf0` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009adbf4"></a> `009adbf4` | `19 68 40 a9` | ldp x25,x26,[x0] | `FALL_THROUGH`
<a id="insn-009adbf8"></a> `009adbf8` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-009adbfc"></a> `009adbfc` | `00 04 00 54` | b.eq 0x009adc7c | `CONDITIONAL_JUMP`
<a id="insn-009adc00"></a> `009adc00` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-009adc04"></a> `009adc04` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-009adc08"></a> `009adc08` | `37 57 40 a9` | ldp x23,x21,[x25] | `FALL_THROUGH`
<a id="insn-009adc0c"></a> `009adc0c` | `f7 d7 00 a9` | stp x23,x21,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-009adc10"></a> `009adc10` | `95 00 00 b4` | cbz x21,0x009adc20 | `CONDITIONAL_JUMP`
<a id="insn-009adc14"></a> `009adc14` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-009adc18"></a> `009adc18` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-009adc1c"></a> `009adc1c` | `55 98 0a 94` | bl 0x00c53d70 | `UNCONDITIONAL_CALL`
<a id="insn-009adc20"></a> `009adc20` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-009adc24"></a> `009adc24` | `31 20 00 94` | bl 0x009b5ce8 | `UNCONDITIONAL_CALL`
<a id="insn-009adc28"></a> `009adc28` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-009adc2c"></a> `009adc2c` | `1f 00 14 6b` | cmp w0,w20 | `FALL_THROUGH`
<a id="insn-009adc30"></a> `009adc30` | `41 00 00 54` | b.ne 0x009adc38 | `CONDITIONAL_JUMP`
<a id="insn-009adc34"></a> `009adc34` | `f3 02 40 f9` | ldr x19,[x23] | `FALL_THROUGH`
<a id="insn-009adc38"></a> `009adc38` | `75 01 00 b4` | cbz x21,0x009adc64 | `CONDITIONAL_JUMP`
<a id="insn-009adc3c"></a> `009adc3c` | `a1 22 00 91` | add x1,x21,#0x8 | `FALL_THROUGH`
<a id="insn-009adc40"></a> `009adc40` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-009adc44"></a> `009adc44` | `57 98 0a 94` | bl 0x00c53da0 | `UNCONDITIONAL_CALL`
<a id="insn-009adc48"></a> `009adc48` | `e0 00 00 b5` | cbnz x0,0x009adc64 | `CONDITIONAL_JUMP`
<a id="insn-009adc4c"></a> `009adc4c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-009adc50"></a> `009adc50` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009adc54"></a> `009adc54` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-009adc58"></a> `009adc58` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-009adc5c"></a> `009adc5c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-009adc60"></a> `009adc60` | `bc a8 0a 94` | bl 0x00c57f50 | `UNCONDITIONAL_CALL`
<a id="insn-009adc64"></a> `009adc64` | `df 02 14 6b` | cmp w22,w20 | `FALL_THROUGH`
<a id="insn-009adc68"></a> `009adc68` | `c0 00 00 54` | b.eq 0x009adc80 | `CONDITIONAL_JUMP`
<a id="insn-009adc6c"></a> `009adc6c` | `39 43 00 91` | add x25,x25,#0x10 | `FALL_THROUGH`
<a id="insn-009adc70"></a> `009adc70` | `3f 03 1a eb` | cmp x25,x26 | `FALL_THROUGH`
<a id="insn-009adc74"></a> `009adc74` | `a1 fc ff 54` | b.ne 0x009adc08 | `CONDITIONAL_JUMP`
<a id="insn-009adc78"></a> `009adc78` | `02 00 00 14` | b 0x009adc80 | `UNCONDITIONAL_JUMP`
<a id="insn-009adc7c"></a> `009adc7c` | `f3 03 1f aa` | mov x19,xzr | `FALL_THROUGH`
<a id="insn-009adc80"></a> `009adc80` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-009adc84"></a> `009adc84` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-009adc88"></a> `009adc88` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-009adc8c"></a> `009adc8c` | `41 02 00 54` | b.ne 0x009adcd4 | `CONDITIONAL_JUMP`
<a id="insn-009adc90"></a> `009adc90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-009adc94"></a> `009adc94` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-009adc98"></a> `009adc98` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-009adc9c"></a> `009adc9c` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-009adca0"></a> `009adca0` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-009adca4"></a> `009adca4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-009adca8"></a> `009adca8` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-009adcac"></a> `009adcac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-009adcd4"></a> `009adcd4` | `b7 a8 0a 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`009adbcc`](#insn-009adbcc) 範囲 `[['009adbcc', '009adbcf']]`
  - `FALL_THROUGH` [`009adbcc`](#insn-009adbcc) → [`009adbd0`](#insn-009adbd0)
- ブロック [`009adbd0`](#insn-009adbd0) 範囲 `[['009adbd0', '009adbe3']]`
  - `FALL_THROUGH` [`009adbe0`](#insn-009adbe0) → [`009adbe4`](#insn-009adbe4)
- ブロック [`009adbe4`](#insn-009adbe4) 範囲 `[['009adbe4', '009adbff']]`
  - `CONDITIONAL_JUMP` [`009adbfc`](#insn-009adbfc) → [`009adc7c`](#insn-009adc7c)
  - `FALL_THROUGH` [`009adbfc`](#insn-009adbfc) → [`009adc00`](#insn-009adc00)
- ブロック [`009adc00`](#insn-009adc00) 範囲 `[['009adc00', '009adc07']]`
  - `FALL_THROUGH` [`009adc04`](#insn-009adc04) → [`009adc08`](#insn-009adc08)
- ブロック [`009adc08`](#insn-009adc08) 範囲 `[['009adc08', '009adc13']]`
  - `CONDITIONAL_JUMP` [`009adc10`](#insn-009adc10) → [`009adc20`](#insn-009adc20)
  - `FALL_THROUGH` [`009adc10`](#insn-009adc10) → [`009adc14`](#insn-009adc14)
- ブロック [`009adc14`](#insn-009adc14) 範囲 `[['009adc14', '009adc1f']]`
  - `FALL_THROUGH` [`009adc1c`](#insn-009adc1c) → [`009adc20`](#insn-009adc20)
- ブロック [`009adc20`](#insn-009adc20) 範囲 `[['009adc20', '009adc33']]`
  - `CONDITIONAL_JUMP` [`009adc30`](#insn-009adc30) → [`009adc38`](#insn-009adc38)
  - `FALL_THROUGH` [`009adc30`](#insn-009adc30) → [`009adc34`](#insn-009adc34)
- ブロック [`009adc34`](#insn-009adc34) 範囲 `[['009adc34', '009adc37']]`
  - `FALL_THROUGH` [`009adc34`](#insn-009adc34) → [`009adc38`](#insn-009adc38)
- ブロック [`009adc38`](#insn-009adc38) 範囲 `[['009adc38', '009adc3b']]`
  - `CONDITIONAL_JUMP` [`009adc38`](#insn-009adc38) → [`009adc64`](#insn-009adc64)
  - `FALL_THROUGH` [`009adc38`](#insn-009adc38) → [`009adc3c`](#insn-009adc3c)
- ブロック [`009adc3c`](#insn-009adc3c) 範囲 `[['009adc3c', '009adc4b']]`
  - `CONDITIONAL_JUMP` [`009adc48`](#insn-009adc48) → [`009adc64`](#insn-009adc64)
  - `FALL_THROUGH` [`009adc48`](#insn-009adc48) → [`009adc4c`](#insn-009adc4c)
- ブロック [`009adc4c`](#insn-009adc4c) 範囲 `[['009adc4c', '009adc63']]`
  - `FALL_THROUGH` [`009adc60`](#insn-009adc60) → [`009adc64`](#insn-009adc64)
- ブロック [`009adc64`](#insn-009adc64) 範囲 `[['009adc64', '009adc6b']]`
  - `CONDITIONAL_JUMP` [`009adc68`](#insn-009adc68) → [`009adc80`](#insn-009adc80)
  - `FALL_THROUGH` [`009adc68`](#insn-009adc68) → [`009adc6c`](#insn-009adc6c)
- ブロック [`009adc6c`](#insn-009adc6c) 範囲 `[['009adc6c', '009adc77']]`
  - `CONDITIONAL_JUMP` [`009adc74`](#insn-009adc74) → [`009adc08`](#insn-009adc08)
  - `FALL_THROUGH` [`009adc74`](#insn-009adc74) → [`009adc78`](#insn-009adc78)
- ブロック [`009adc78`](#insn-009adc78) 範囲 `[['009adc78', '009adc7b']]`
  - `UNCONDITIONAL_JUMP` [`009adc78`](#insn-009adc78) → [`009adc80`](#insn-009adc80)
- ブロック [`009adc7c`](#insn-009adc7c) 範囲 `[['009adc7c', '009adc7f']]`
  - `FALL_THROUGH` [`009adc7c`](#insn-009adc7c) → [`009adc80`](#insn-009adc80)
- ブロック [`009adc80`](#insn-009adc80) 範囲 `[['009adc80', '009adc8f']]`
  - `CONDITIONAL_JUMP` [`009adc8c`](#insn-009adc8c) → [`009adcd4`](#insn-009adcd4)
  - `FALL_THROUGH` [`009adc8c`](#insn-009adc8c) → [`009adc90`](#insn-009adc90)
- ブロック [`009adc90`](#insn-009adc90) 範囲 `[['009adc90', '009adcaf']]`
- ブロック [`009adcd4`](#insn-009adcd4) 範囲 `[['009adcd4', '009adcd7']]`

## 命令位置別の参照

- [`009adbd0`](#insn-009adbd0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adbd4`](#insn-009adbd4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adbd8`](#insn-009adbd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adbdc`](#insn-009adbdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adbe0`](#insn-009adbe0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adbf0`](#insn-009adbf0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adbfc`](#insn-009adbfc) → [`009adc7c`](#insn-009adc7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc0c`](#insn-009adc0c) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc10`](#insn-009adc10) → [`009adc20`](#insn-009adc20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc1c`](#insn-009adc1c) → [`00c53d70`](../00c53/00c53d70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53d70` · 推定シンボル `None` · 推定型 `None`
- [`009adc24`](#insn-009adc24) → [`009b5ce8`](../009b5/009b5ce8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `009b5ce8` · 推定シンボル `None` · 推定型 `None`
- [`009adc30`](#insn-009adc30) → [`009adc38`](#insn-009adc38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc38`](#insn-009adc38) → [`009adc64`](#insn-009adc64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc44`](#insn-009adc44) → [`00c53da0`](../00c53/00c53da0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53da0` · 推定シンボル `None` · 推定型 `None`
- [`009adc48`](#insn-009adc48) → [`009adc64`](#insn-009adc64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc60`](#insn-009adc60) → [`00c57f50`](../00c57/00c57f50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f50` · 推定シンボル `None` · 推定型 `None`
- [`009adc68`](#insn-009adc68) → [`009adc80`](#insn-009adc80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc74`](#insn-009adc74) → [`009adc08`](#insn-009adc08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc78`](#insn-009adc78) → [`009adc80`](#insn-009adc80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc84`](#insn-009adc84) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc8c`](#insn-009adc8c) → [`009adcd4`](#insn-009adcd4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc94`](#insn-009adc94) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc98`](#insn-009adc98) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adc9c`](#insn-009adc9c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adca0`](#insn-009adca0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adca4`](#insn-009adca4) → `Stack[-0x50]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`009adcd4`](#insn-009adcd4) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`009adbd0`](#insn-009adbd0)

~~~json
{
  "source": "009adbd0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adbd4`](#insn-009adbd4)

~~~json
{
  "source": "009adbd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adbd8`](#insn-009adbd8)

~~~json
{
  "source": "009adbd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adbdc`](#insn-009adbdc)

~~~json
{
  "source": "009adbdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adbe0`](#insn-009adbe0)

~~~json
{
  "source": "009adbe0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adbf0`](#insn-009adbf0)

~~~json
{
  "source": "009adbf0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adbfc`](#insn-009adbfc)

~~~json
{
  "source": "009adbfc",
  "target": "009adc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc0c`](#insn-009adc0c)

~~~json
{
  "source": "009adc0c",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc10`](#insn-009adc10)

~~~json
{
  "source": "009adc10",
  "target": "009adc20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc1c`](#insn-009adc1c)

~~~json
{
  "source": "009adc1c",
  "target": "00c53d70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009adc24`](#insn-009adc24)

~~~json
{
  "source": "009adc24",
  "target": "009b5ce8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009adc30`](#insn-009adc30)

~~~json
{
  "source": "009adc30",
  "target": "009adc38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc38`](#insn-009adc38)

~~~json
{
  "source": "009adc38",
  "target": "009adc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc44`](#insn-009adc44)

~~~json
{
  "source": "009adc44",
  "target": "00c53da0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009adc48`](#insn-009adc48)

~~~json
{
  "source": "009adc48",
  "target": "009adc64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc60`](#insn-009adc60)

~~~json
{
  "source": "009adc60",
  "target": "00c57f50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`009adc68`](#insn-009adc68)

~~~json
{
  "source": "009adc68",
  "target": "009adc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc74`](#insn-009adc74)

~~~json
{
  "source": "009adc74",
  "target": "009adc08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc78`](#insn-009adc78)

~~~json
{
  "source": "009adc78",
  "target": "009adc80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc84`](#insn-009adc84)

~~~json
{
  "source": "009adc84",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc8c`](#insn-009adc8c)

~~~json
{
  "source": "009adc8c",
  "target": "009adcd4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc94`](#insn-009adc94)

~~~json
{
  "source": "009adc94",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc98`](#insn-009adc98)

~~~json
{
  "source": "009adc98",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adc9c`](#insn-009adc9c)

~~~json
{
  "source": "009adc9c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adca0`](#insn-009adca0)

~~~json
{
  "source": "009adca0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adca4`](#insn-009adca4)

~~~json
{
  "source": "009adca4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`009adcd4`](#insn-009adcd4)

~~~json
{
  "source": "009adcd4",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
