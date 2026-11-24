# 00bcfb9c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcfb00`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcf/00bcfb00.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0082.md#compare-21b93dfb2b7b66a0b0ff4a1f0226c94e)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bd0b90`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bd0/00bd0b90.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-cd5153b9102acdf7c196767543e00fb3)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfb9c",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4Auth20FetchProvidersResultEZNS2_14FutureCallbackIS4_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSE_E_EEvRKNS_12FutureHandleEiSD_RKT0_",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9429e6e9c5167b4493db76ba6bc8fa96f5528a246eb5bc8355a1359fca30495b",
  "source_text_sha256": "9429e6e9c5167b4493db76ba6bc8fa96f5528a246eb5bc8355a1359fca30495b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfb9c",
        "00bcfcd3"
      ]
    ],
    "bytes_sha256": "34e6bcfe359894859c25e80950f6f719f753ac9c494093f0f81c1584e794c53d",
    "instruction_count": 78,
    "instruction_bytes": 312,
    "body_bytes": 312,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5dc70](../00c5d/00c5dc70.md)

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

## 疑似コード / UTF-8 1877 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4Auth20FetchProvidersResultEZNS2_14FutureCallbackIS4_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSE_E_EEvRKNS_12FutureHandleEiSD_RKT0_
               (long *param_1,undefined8 *param_2,undefined4 param_3,undefined8 param_4,
               undefined8 *param_5)

{
  int iVar1;
  long lVar2;
  undefined8 uVar3;
  ulong uVar4;
  code *pcVar5;
  
  _ZN8firebase5Mutex7AcquireEv(param_1 + 1);
  lVar2 = _ZN8firebase26ReferenceCountedFutureImpl17BackingFromHandleEm(param_1,*param_2);
  if (lVar2 == 0) {
    _ZN8firebase5Mutex7ReleaseEv(param_1 + 1);
    return;
  }
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
                    /* WARNING: Could not recover jumptable at 0x00bcfc9c. Too many branches */
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
<a id="insn-00bcfb9c"></a> `00bcfb9c` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcfba0"></a> `00bcfba0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfba4"></a> `00bcfba4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfba8"></a> `00bcfba8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfbac"></a> `00bcfbac` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfbb0"></a> `00bcfbb0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bcfbb4"></a> `00bcfbb4` | `19 20 00 91` | add x25,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bcfbb8"></a> `00bcfbb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcfbbc"></a> `00bcfbbc` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bcfbc0"></a> `00bcfbc0` | `f5 03 04 aa` | mov x21,x4 | `FALL_THROUGH`
<a id="insn-00bcfbc4"></a> `00bcfbc4` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00bcfbc8"></a> `00bcfbc8` | `f8 03 02 2a` | mov w24,w2 | `FALL_THROUGH`
<a id="insn-00bcfbcc"></a> `00bcfbcc` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcfbd0"></a> `00bcfbd0` | `c0 2b 02 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfbd4"></a> `00bcfbd4` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bcfbd8"></a> `00bcfbd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfbdc"></a> `00bcfbdc` | `dd 2c 02 94` | bl 0x00c5af50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfbe0"></a> `00bcfbe0` | `00 06 00 b4` | cbz x0,0x00bcfca0 | `CONDITIONAL_JUMP`
<a id="insn-00bcfbe4"></a> `00bcfbe4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcfbe8"></a> `00bcfbe8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcfbec"></a> `00bcfbec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfbf0"></a> `00bcfbf0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfbf4"></a> `00bcfbf4` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfbf8"></a> `00bcfbf8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfbfc"></a> `00bcfbfc` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfc00"></a> `00bcfc00` | `80 00 00 54` | b.eq 0x00bcfc10 | `CONDITIONAL_JUMP`
<a id="insn-00bcfc04"></a> `00bcfc04` | `c0 b6 ff 90` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bcfc08"></a> `00bcfc08` | `00 20 02 91` | add x0,x0,#0x88 | `FALL_THROUGH`
<a id="insn-00bcfc0c"></a> `00bcfc0c` | `31 2d 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc10"></a> `00bcfc10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc14"></a> `00bcfc14` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcfc18"></a> `00bcfc18` | `e2 03 18 2a` | mov w2,w24 | `FALL_THROUGH`
<a id="insn-00bcfc1c"></a> `00bcfc1c` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00bcfc20"></a> `00bcfc20` | `c8 2c 02 94` | bl 0x00c5af40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc24"></a> `00bcfc24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc28"></a> `00bcfc28` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcfc2c"></a> `00bcfc2c` | `b5 2c 02 94` | bl 0x00c5af00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc30"></a> `00bcfc30` | `a1 0a 40 f9` | ldr x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfc34"></a> `00bcfc34` | `28 0c 40 f9` | ldr x8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bcfc38"></a> `00bcfc38` | `a8 00 00 b4` | cbz x8,0x00bcfc4c | `CONDITIONAL_JUMP`
<a id="insn-00bcfc3c"></a> `00bcfc3c` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bcfc40"></a> `00bcfc40` | `a0 02 40 f9` | ldr x0,[x21] | `FALL_THROUGH`
<a id="insn-00bcfc44"></a> `00bcfc44` | `a2 22 40 39` | ldrb w2,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfc48"></a> `00bcfc48` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfc4c"></a> `00bcfc4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc50"></a> `00bcfc50` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfc54"></a> `00bcfc54` | `b7 2c 02 94` | bl 0x00c5af30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc58"></a> `00bcfc58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc5c"></a> `00bcfc5c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcfc60"></a> `00bcfc60` | `b0 2c 02 94` | bl 0x00c5af20 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc64"></a> `00bcfc64` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc68"></a> `00bcfc68` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfc6c"></a> `00bcfc6c` | `bd 2c 02 94` | bl 0x00c5af60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc70"></a> `00bcfc70` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc74"></a> `00bcfc74` | `33 2d 02 94` | bl 0x00c5b140 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc78"></a> `00bcfc78` | `20 02 00 36` | tbz w0,#0x0,0x00bcfcbc | `CONDITIONAL_JUMP`
<a id="insn-00bcfc7c"></a> `00bcfc7c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcfc80"></a> `00bcfc80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc84"></a> `00bcfc84` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfc88"></a> `00bcfc88` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfc8c"></a> `00bcfc8c` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfc90"></a> `00bcfc90` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfc94"></a> `00bcfc94` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfc98"></a> `00bcfc98` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcfc9c"></a> `00bcfc9c` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bcfca0"></a> `00bcfca0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfca4"></a> `00bcfca4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfca8"></a> `00bcfca8` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfcac"></a> `00bcfcac` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfcb0"></a> `00bcfcb0` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bcfcb4"></a> `00bcfcb4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcfcb8"></a> `00bcfcb8` | `8a 2b 02 14` | b 0x00c5aae0 | `CALL_TERMINATOR`
<a id="insn-00bcfcbc"></a> `00bcfcbc` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfcc0"></a> `00bcfcc0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfcc4"></a> `00bcfcc4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfcc8"></a> `00bcfcc8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfccc"></a> `00bcfccc` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcfcd0"></a> `00bcfcd0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfb9c`](#insn-00bcfb9c) 範囲 `[['00bcfb9c', '00bcfbe3']]`
  - `CONDITIONAL_JUMP` [`00bcfbe0`](#insn-00bcfbe0) → [`00bcfca0`](#insn-00bcfca0)
  - `FALL_THROUGH` [`00bcfbe0`](#insn-00bcfbe0) → [`00bcfbe4`](#insn-00bcfbe4)
- ブロック [`00bcfbe4`](#insn-00bcfbe4) 範囲 `[['00bcfbe4', '00bcfc03']]`
  - `CONDITIONAL_JUMP` [`00bcfc00`](#insn-00bcfc00) → [`00bcfc10`](#insn-00bcfc10)
  - `FALL_THROUGH` [`00bcfc00`](#insn-00bcfc00) → [`00bcfc04`](#insn-00bcfc04)
- ブロック [`00bcfc04`](#insn-00bcfc04) 範囲 `[['00bcfc04', '00bcfc0f']]`
  - `FALL_THROUGH` [`00bcfc0c`](#insn-00bcfc0c) → [`00bcfc10`](#insn-00bcfc10)
- ブロック [`00bcfc10`](#insn-00bcfc10) 範囲 `[['00bcfc10', '00bcfc3b']]`
  - `CONDITIONAL_JUMP` [`00bcfc38`](#insn-00bcfc38) → [`00bcfc4c`](#insn-00bcfc4c)
  - `FALL_THROUGH` [`00bcfc38`](#insn-00bcfc38) → [`00bcfc3c`](#insn-00bcfc3c)
- ブロック [`00bcfc3c`](#insn-00bcfc3c) 範囲 `[['00bcfc3c', '00bcfc4b']]`
  - `FALL_THROUGH` [`00bcfc48`](#insn-00bcfc48) → [`00bcfc4c`](#insn-00bcfc4c)
- ブロック [`00bcfc4c`](#insn-00bcfc4c) 範囲 `[['00bcfc4c', '00bcfc7b']]`
  - `CONDITIONAL_JUMP` [`00bcfc78`](#insn-00bcfc78) → [`00bcfcbc`](#insn-00bcfcbc)
  - `FALL_THROUGH` [`00bcfc78`](#insn-00bcfc78) → [`00bcfc7c`](#insn-00bcfc7c)
- ブロック [`00bcfc7c`](#insn-00bcfc7c) 範囲 `[['00bcfc7c', '00bcfc9f']]`
- ブロック [`00bcfca0`](#insn-00bcfca0) 範囲 `[['00bcfca0', '00bcfcbb']]`
- ブロック [`00bcfcbc`](#insn-00bcfcbc) 範囲 `[['00bcfcbc', '00bcfcd3']]`

## 命令位置別の参照

- [`00bcfb9c`](#insn-00bcfb9c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfba0`](#insn-00bcfba0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfba4`](#insn-00bcfba4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfba8`](#insn-00bcfba8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfbac`](#insn-00bcfbac) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfbd0`](#insn-00bcfbd0) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfbdc`](#insn-00bcfbdc) → [`00c5af50`](../00c5a/00c5af50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af50` · 推定シンボル `None` · 推定型 `None`
- [`00bcfbe0`](#insn-00bcfbe0) → [`00bcfca0`](#insn-00bcfca0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc00`](#insn-00bcfc00) → [`00bcfc10`](#insn-00bcfc10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc08`](#insn-00bcfc08) → `002a7088`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcfc0c`](#insn-00bcfc0c) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc20`](#insn-00bcfc20) → [`00c5af40`](../00c5a/00c5af40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af40` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc2c`](#insn-00bcfc2c) → [`00c5af00`](../00c5a/00c5af00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af00` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc38`](#insn-00bcfc38) → [`00bcfc4c`](#insn-00bcfc4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc54`](#insn-00bcfc54) → [`00c5af30`](../00c5a/00c5af30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af30` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc60`](#insn-00bcfc60) → [`00c5af20`](../00c5a/00c5af20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af20` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc6c`](#insn-00bcfc6c) → [`00c5af60`](../00c5a/00c5af60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5af60` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc74`](#insn-00bcfc74) → [`00c5b140`](../00c5b/00c5b140.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b140` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc78`](#insn-00bcfc78) → [`00bcfcbc`](#insn-00bcfcbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc84`](#insn-00bcfc84) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc88`](#insn-00bcfc88) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc90`](#insn-00bcfc90) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc94`](#insn-00bcfc94) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfca0`](#insn-00bcfca0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfca4`](#insn-00bcfca4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfca8`](#insn-00bcfca8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcac`](#insn-00bcfcac) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcb8`](#insn-00bcfcb8) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcbc`](#insn-00bcfcbc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcc0`](#insn-00bcfcc0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcc4`](#insn-00bcfcc4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcc8`](#insn-00bcfcc8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfb9c`](#insn-00bcfb9c)

~~~json
{
  "source": "00bcfb9c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfba0`](#insn-00bcfba0)

~~~json
{
  "source": "00bcfba0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfba4`](#insn-00bcfba4)

~~~json
{
  "source": "00bcfba4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfba8`](#insn-00bcfba8)

~~~json
{
  "source": "00bcfba8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfbac`](#insn-00bcfbac)

~~~json
{
  "source": "00bcfbac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfbd0`](#insn-00bcfbd0)

~~~json
{
  "source": "00bcfbd0",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfbdc`](#insn-00bcfbdc)

~~~json
{
  "source": "00bcfbdc",
  "target": "00c5af50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfbe0`](#insn-00bcfbe0)

~~~json
{
  "source": "00bcfbe0",
  "target": "00bcfca0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc00`](#insn-00bcfc00)

~~~json
{
  "source": "00bcfc00",
  "target": "00bcfc10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc08`](#insn-00bcfc08)

~~~json
{
  "source": "00bcfc08",
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
- 参照命令 [`00bcfc0c`](#insn-00bcfc0c)

~~~json
{
  "source": "00bcfc0c",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc20`](#insn-00bcfc20)

~~~json
{
  "source": "00bcfc20",
  "target": "00c5af40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc2c`](#insn-00bcfc2c)

~~~json
{
  "source": "00bcfc2c",
  "target": "00c5af00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc38`](#insn-00bcfc38)

~~~json
{
  "source": "00bcfc38",
  "target": "00bcfc4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc54`](#insn-00bcfc54)

~~~json
{
  "source": "00bcfc54",
  "target": "00c5af30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc60`](#insn-00bcfc60)

~~~json
{
  "source": "00bcfc60",
  "target": "00c5af20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc6c`](#insn-00bcfc6c)

~~~json
{
  "source": "00bcfc6c",
  "target": "00c5af60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc74`](#insn-00bcfc74)

~~~json
{
  "source": "00bcfc74",
  "target": "00c5b140",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc78`](#insn-00bcfc78)

~~~json
{
  "source": "00bcfc78",
  "target": "00bcfcbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc84`](#insn-00bcfc84)

~~~json
{
  "source": "00bcfc84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc88`](#insn-00bcfc88)

~~~json
{
  "source": "00bcfc88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc90`](#insn-00bcfc90)

~~~json
{
  "source": "00bcfc90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc94`](#insn-00bcfc94)

~~~json
{
  "source": "00bcfc94",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfca0`](#insn-00bcfca0)

~~~json
{
  "source": "00bcfca0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfca4`](#insn-00bcfca4)

~~~json
{
  "source": "00bcfca4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfca8`](#insn-00bcfca8)

~~~json
{
  "source": "00bcfca8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcac`](#insn-00bcfcac)

~~~json
{
  "source": "00bcfcac",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcb8`](#insn-00bcfcb8)

~~~json
{
  "source": "00bcfcb8",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfcbc`](#insn-00bcfcbc)

~~~json
{
  "source": "00bcfcbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcc0`](#insn-00bcfcc0)

~~~json
{
  "source": "00bcfcc0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcc4`](#insn-00bcfcc4)

~~~json
{
  "source": "00bcfcc4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcc8`](#insn-00bcfcc8)

~~~json
{
  "source": "00bcfcc8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
