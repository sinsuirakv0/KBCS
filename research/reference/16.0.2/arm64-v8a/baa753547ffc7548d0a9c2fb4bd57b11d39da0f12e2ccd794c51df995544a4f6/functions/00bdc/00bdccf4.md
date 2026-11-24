# 00bdccf4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdcc58`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdc/00bdcc58.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-2ad246b874eb3ac854435184fb5e77d0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bddce8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdd/00bddce8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-9e16e8036cc711a97e581ac7d398f2b0)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdccf4",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9eea8b2d5dc9eb1c3fed70076b6fb6f3c672759deb326e3af00a70f2da2fdbdb",
  "source_text_sha256": "9eea8b2d5dc9eb1c3fed70076b6fb6f3c672759deb326e3af00a70f2da2fdbdb",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdccf4",
        "00bdce2b"
      ]
    ],
    "bytes_sha256": "29c00e2cc7fcdea5b723eacecb6b3334ae3b32f2589709782e188cb3b2cbdda2",
    "instruction_count": 78,
    "instruction_bytes": 312,
    "body_bytes": 312,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5de90](../00c5d/00c5de90.md)

## 呼び出し先

- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5af00](../00c5a/00c5af00.md)
- [00c5af20](../00c5a/00c5af20.md)
- [00c5af30](../00c5a/00c5af30.md)
- [00c5af40](../00c5a/00c5af40.md)
- [00c5af50](../00c5a/00c5af50.md)
- [00c5af60](../00c5a/00c5af60.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b140](../00c5b/00c5b140.md)

## 関連文字列（未確認候補）

~~~text
"GetFutureStatus(handle) == kFutureStatusPending"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2368 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth10AuthResultEZNS2_35FederatedAuthProviderFutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_
               (long *param_1,undefined8 *param_2,undefined4 param_3,undefined8 param_4,
               undefined8 *param_5)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  ulong uVar4;
  code *pcVar5;
  
                    /* try { // try from 00bdcd04 to 00cdcd0f has its CatchHandler @ 00bdec48 */
                    /* try { // try from 00bdcd10 to 00cdcd1f has its CatchHandler @ 00bdec40 */
                    /* try { // try from 00bdcd20 to 00cdcd2b has its CatchHandler @ 00bdec3c */
  _ZN8firebase5Mutex7AcquireEv(param_1 + 1);
                    /* try { // try from 00bdcd2c to 00cdcd43 has its CatchHandler @ 00bdec38 */
  lVar2 = _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(param_1,*param_2);
  if (lVar2 == 0) {
    _ZN8firebase5Mutex7ReleaseEv(param_1 + 1);
    return;
  }
                    /* try { // try from 00bdcd44 to 00cdd75f has its CatchHandler @ 00bd6fbc */
  iVar1 = (**(code **)(*param_1 + 0x20))(param_1,param_2);
  if (iVar1 != 1) {
    _ZN8firebase9LogAssertEPKcz("GetFutureStatus(handle) == kFutureStatusPending");
  }
  _ZN8firebase26ReferenceCountedFutureImpl15SetBackingErrorEPNS_17FutureBackingDataEiPKc
            (param_1,lVar2,param_3,param_4);
  uVar3 = _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE
                    (param_1,lVar2);
  pcVar5 = *(code **)(param_5[2] + 0x18);
  if (pcVar5 != (code *)0x0) {
    (*pcVar5)(*param_5,param_5[2],*(undefined1 *)(param_5 + 1),uVar3);
  }
  _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(param_1,param_2);
  _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
  uVar4 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar4 & 1) != 0) {
                    /* WARNING: Could not recover jumptable at 0x00bdcdf4. Too many branches */
                    /* WARNING: Treating indirect jump as call */
    (**(code **)(*param_1 + 8))(param_1);
    return;
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdccf4"></a> `00bdccf4` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bdccf8"></a> `00bdccf8` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdccfc"></a> `00bdccfc` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcd00"></a> `00bdcd00` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdcd04"></a> `00bdcd04` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdcd08"></a> `00bdcd08` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bdcd0c"></a> `00bdcd0c` | `19 20 00 91` | add x25,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bdcd10"></a> `00bdcd10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdcd14"></a> `00bdcd14` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdcd18"></a> `00bdcd18` | `f5 03 04 aa` | mov x21,x4 | `FALL_THROUGH`
<a id="insn-00bdcd1c"></a> `00bdcd1c` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00bdcd20"></a> `00bdcd20` | `f8 03 02 2a` | mov w24,w2 | `FALL_THROUGH`
<a id="insn-00bdcd24"></a> `00bdcd24` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bdcd28"></a> `00bdcd28` | `6a f7 01 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcd2c"></a> `00bdcd2c` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bdcd30"></a> `00bdcd30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcd34"></a> `00bdcd34` | `87 f8 01 94` | bl 0x00c5af50 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcd38"></a> `00bdcd38` | `00 06 00 b4` | cbz x0,0x00bdcdf8 | `CONDITIONAL_JUMP`
<a id="insn-00bdcd3c"></a> `00bdcd3c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdcd40"></a> `00bdcd40` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdcd44"></a> `00bdcd44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcd48"></a> `00bdcd48` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdcd4c"></a> `00bdcd4c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcd50"></a> `00bdcd50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcd54"></a> `00bdcd54` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdcd58"></a> `00bdcd58` | `80 00 00 54` | b.eq 0x00bdcd68 | `CONDITIONAL_JUMP`
<a id="insn-00bdcd5c"></a> `00bdcd5c` | `40 b6 ff f0` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bdcd60"></a> `00bdcd60` | `00 20 02 91` | add x0,x0,#0x88 | `FALL_THROUGH`
<a id="insn-00bdcd64"></a> `00bdcd64` | `db f8 01 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcd68"></a> `00bdcd68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcd6c"></a> `00bdcd6c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdcd70"></a> `00bdcd70` | `e2 03 18 2a` | mov w2,w24 | `FALL_THROUGH`
<a id="insn-00bdcd74"></a> `00bdcd74` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00bdcd78"></a> `00bdcd78` | `72 f8 01 94` | bl 0x00c5af40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcd7c"></a> `00bdcd7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcd80"></a> `00bdcd80` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdcd84"></a> `00bdcd84` | `5f f8 01 94` | bl 0x00c5af00 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcd88"></a> `00bdcd88` | `a1 0a 40 f9` | ldr x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcd8c"></a> `00bdcd8c` | `28 0c 40 f9` | ldr x8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bdcd90"></a> `00bdcd90` | `a8 00 00 b4` | cbz x8,0x00bdcda4 | `CONDITIONAL_JUMP`
<a id="insn-00bdcd94"></a> `00bdcd94` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bdcd98"></a> `00bdcd98` | `a0 02 40 f9` | ldr x0,[x21] | `FALL_THROUGH`
<a id="insn-00bdcd9c"></a> `00bdcd9c` | `a2 22 40 39` | ldrb w2,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bdcda0"></a> `00bdcda0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcda4"></a> `00bdcda4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcda8"></a> `00bdcda8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdcdac"></a> `00bdcdac` | `61 f8 01 94` | bl 0x00c5af30 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcdb0"></a> `00bdcdb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcdb4"></a> `00bdcdb4` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdcdb8"></a> `00bdcdb8` | `5a f8 01 94` | bl 0x00c5af20 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcdbc"></a> `00bdcdbc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcdc0"></a> `00bdcdc0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdcdc4"></a> `00bdcdc4` | `67 f8 01 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcdc8"></a> `00bdcdc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcdcc"></a> `00bdcdcc` | `dd f8 01 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcdd0"></a> `00bdcdd0` | `20 02 00 36` | tbz w0,#0x0,0x00bdce14 | `CONDITIONAL_JUMP`
<a id="insn-00bdcdd4"></a> `00bdcdd4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdcdd8"></a> `00bdcdd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcddc"></a> `00bdcddc` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdcde0"></a> `00bdcde0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdcde4"></a> `00bdcde4` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bdcde8"></a> `00bdcde8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcdec"></a> `00bdcdec` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcdf0"></a> `00bdcdf0` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bdcdf4"></a> `00bdcdf4` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bdcdf8"></a> `00bdcdf8` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdcdfc"></a> `00bdcdfc` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdce00"></a> `00bdce00` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdce04"></a> `00bdce04` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdce08"></a> `00bdce08` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bdce0c"></a> `00bdce0c` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bdce10"></a> `00bdce10` | `34 f7 01 14` | b 0x00c5aae0 | `CALL_TERMINATOR`
<a id="insn-00bdce14"></a> `00bdce14` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdce18"></a> `00bdce18` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdce1c"></a> `00bdce1c` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdce20"></a> `00bdce20` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdce24"></a> `00bdce24` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bdce28"></a> `00bdce28` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdccf4`](#insn-00bdccf4) 範囲 `[['00bdccf4', '00bdcd03']]`
  - `FALL_THROUGH` [`00bdcd00`](#insn-00bdcd00) → [`00bdcd04`](#insn-00bdcd04)
- ブロック [`00bdcd04`](#insn-00bdcd04) 範囲 `[['00bdcd04', '00bdcd0f']]`
  - `FALL_THROUGH` [`00bdcd0c`](#insn-00bdcd0c) → [`00bdcd10`](#insn-00bdcd10)
- ブロック [`00bdcd10`](#insn-00bdcd10) 範囲 `[['00bdcd10', '00bdcd1f']]`
  - `FALL_THROUGH` [`00bdcd1c`](#insn-00bdcd1c) → [`00bdcd20`](#insn-00bdcd20)
- ブロック [`00bdcd20`](#insn-00bdcd20) 範囲 `[['00bdcd20', '00bdcd2b']]`
  - `FALL_THROUGH` [`00bdcd28`](#insn-00bdcd28) → [`00bdcd2c`](#insn-00bdcd2c)
- ブロック [`00bdcd2c`](#insn-00bdcd2c) 範囲 `[['00bdcd2c', '00bdcd3b']]`
  - `CONDITIONAL_JUMP` [`00bdcd38`](#insn-00bdcd38) → [`00bdcdf8`](#insn-00bdcdf8)
  - `FALL_THROUGH` [`00bdcd38`](#insn-00bdcd38) → [`00bdcd3c`](#insn-00bdcd3c)
- ブロック [`00bdcd3c`](#insn-00bdcd3c) 範囲 `[['00bdcd3c', '00bdcd43']]`
  - `FALL_THROUGH` [`00bdcd40`](#insn-00bdcd40) → [`00bdcd44`](#insn-00bdcd44)
- ブロック [`00bdcd44`](#insn-00bdcd44) 範囲 `[['00bdcd44', '00bdcd5b']]`
  - `CONDITIONAL_JUMP` [`00bdcd58`](#insn-00bdcd58) → [`00bdcd68`](#insn-00bdcd68)
  - `FALL_THROUGH` [`00bdcd58`](#insn-00bdcd58) → [`00bdcd5c`](#insn-00bdcd5c)
- ブロック [`00bdcd5c`](#insn-00bdcd5c) 範囲 `[['00bdcd5c', '00bdcd67']]`
  - `FALL_THROUGH` [`00bdcd64`](#insn-00bdcd64) → [`00bdcd68`](#insn-00bdcd68)
- ブロック [`00bdcd68`](#insn-00bdcd68) 範囲 `[['00bdcd68', '00bdcd93']]`
  - `CONDITIONAL_JUMP` [`00bdcd90`](#insn-00bdcd90) → [`00bdcda4`](#insn-00bdcda4)
  - `FALL_THROUGH` [`00bdcd90`](#insn-00bdcd90) → [`00bdcd94`](#insn-00bdcd94)
- ブロック [`00bdcd94`](#insn-00bdcd94) 範囲 `[['00bdcd94', '00bdcda3']]`
  - `FALL_THROUGH` [`00bdcda0`](#insn-00bdcda0) → [`00bdcda4`](#insn-00bdcda4)
- ブロック [`00bdcda4`](#insn-00bdcda4) 範囲 `[['00bdcda4', '00bdcdd3']]`
  - `CONDITIONAL_JUMP` [`00bdcdd0`](#insn-00bdcdd0) → [`00bdce14`](#insn-00bdce14)
  - `FALL_THROUGH` [`00bdcdd0`](#insn-00bdcdd0) → [`00bdcdd4`](#insn-00bdcdd4)
- ブロック [`00bdcdd4`](#insn-00bdcdd4) 範囲 `[['00bdcdd4', '00bdcdf7']]`
- ブロック [`00bdcdf8`](#insn-00bdcdf8) 範囲 `[['00bdcdf8', '00bdce13']]`
- ブロック [`00bdce14`](#insn-00bdce14) 範囲 `[['00bdce14', '00bdce2b']]`

## 命令位置別の参照

- [`00bdccf4`](#insn-00bdccf4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdccf8`](#insn-00bdccf8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdccfc`](#insn-00bdccfc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd00`](#insn-00bdcd00) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd04`](#insn-00bdcd04) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd28`](#insn-00bdcd28) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd34`](#insn-00bdcd34) → [`00c5af50`](../00c5a/00c5af50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af50` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd38`](#insn-00bdcd38) → [`00bdcdf8`](#insn-00bdcdf8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd58`](#insn-00bdcd58) → [`00bdcd68`](#insn-00bdcd68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd60`](#insn-00bdcd60) → `002a7088`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdcd64`](#insn-00bdcd64) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd78`](#insn-00bdcd78) → [`00c5af40`](../00c5a/00c5af40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af40` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd84`](#insn-00bdcd84) → [`00c5af00`](../00c5a/00c5af00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af00` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd90`](#insn-00bdcd90) → [`00bdcda4`](#insn-00bdcda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcdac`](#insn-00bdcdac) → [`00c5af30`](../00c5a/00c5af30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af30` · 推定シンボル `None` · 推定型 `None`
- [`00bdcdb8`](#insn-00bdcdb8) → [`00c5af20`](../00c5a/00c5af20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af20` · 推定シンボル `None` · 推定型 `None`
- [`00bdcdc4`](#insn-00bdcdc4) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bdcdcc`](#insn-00bdcdcc) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00bdcdd0`](#insn-00bdcdd0) → [`00bdce14`](#insn-00bdce14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcddc`](#insn-00bdcddc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcde0`](#insn-00bdcde0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcde8`](#insn-00bdcde8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcdec`](#insn-00bdcdec) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcdf8`](#insn-00bdcdf8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcdfc`](#insn-00bdcdfc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce00`](#insn-00bdce00) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce04`](#insn-00bdce04) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce10`](#insn-00bdce10) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bdce14`](#insn-00bdce14) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce18`](#insn-00bdce18) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce1c`](#insn-00bdce1c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce20`](#insn-00bdce20) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdccf4`](#insn-00bdccf4)

~~~json
{
  "source": "00bdccf4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdccf8`](#insn-00bdccf8)

~~~json
{
  "source": "00bdccf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdccfc`](#insn-00bdccfc)

~~~json
{
  "source": "00bdccfc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcd00`](#insn-00bdcd00)

~~~json
{
  "source": "00bdcd00",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcd04`](#insn-00bdcd04)

~~~json
{
  "source": "00bdcd04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcd28`](#insn-00bdcd28)

~~~json
{
  "source": "00bdcd28",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcd34`](#insn-00bdcd34)

~~~json
{
  "source": "00bdcd34",
  "target": "00c5af50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcd38`](#insn-00bdcd38)

~~~json
{
  "source": "00bdcd38",
  "target": "00bdcdf8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcd58`](#insn-00bdcd58)

~~~json
{
  "source": "00bdcd58",
  "target": "00bdcd68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcd60`](#insn-00bdcd60)

~~~json
{
  "source": "00bdcd60",
  "target": "002a7088",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7088",
  "offset": 0,
  "size": 48,
  "datatype": "string",
  "bytes": "4765744675747572655374617475732868616e646c6529203d3d206b46757475",
  "capture_start": "002a7088",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdcd64`](#insn-00bdcd64)

~~~json
{
  "source": "00bdcd64",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcd78`](#insn-00bdcd78)

~~~json
{
  "source": "00bdcd78",
  "target": "00c5af40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcd84`](#insn-00bdcd84)

~~~json
{
  "source": "00bdcd84",
  "target": "00c5af00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcd90`](#insn-00bdcd90)

~~~json
{
  "source": "00bdcd90",
  "target": "00bdcda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcdac`](#insn-00bdcdac)

~~~json
{
  "source": "00bdcdac",
  "target": "00c5af30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcdb8`](#insn-00bdcdb8)

~~~json
{
  "source": "00bdcdb8",
  "target": "00c5af20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcdc4`](#insn-00bdcdc4)

~~~json
{
  "source": "00bdcdc4",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcdcc`](#insn-00bdcdcc)

~~~json
{
  "source": "00bdcdcc",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcdd0`](#insn-00bdcdd0)

~~~json
{
  "source": "00bdcdd0",
  "target": "00bdce14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcddc`](#insn-00bdcddc)

~~~json
{
  "source": "00bdcddc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcde0`](#insn-00bdcde0)

~~~json
{
  "source": "00bdcde0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcde8`](#insn-00bdcde8)

~~~json
{
  "source": "00bdcde8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcdec`](#insn-00bdcdec)

~~~json
{
  "source": "00bdcdec",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcdf8`](#insn-00bdcdf8)

~~~json
{
  "source": "00bdcdf8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcdfc`](#insn-00bdcdfc)

~~~json
{
  "source": "00bdcdfc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce00`](#insn-00bdce00)

~~~json
{
  "source": "00bdce00",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce04`](#insn-00bdce04)

~~~json
{
  "source": "00bdce04",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce10`](#insn-00bdce10)

~~~json
{
  "source": "00bdce10",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdce14`](#insn-00bdce14)

~~~json
{
  "source": "00bdce14",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce18`](#insn-00bdce18)

~~~json
{
  "source": "00bdce18",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce1c`](#insn-00bdce1c)

~~~json
{
  "source": "00bdce1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce20`](#insn-00bdce20)

~~~json
{
  "source": "00bdce20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
