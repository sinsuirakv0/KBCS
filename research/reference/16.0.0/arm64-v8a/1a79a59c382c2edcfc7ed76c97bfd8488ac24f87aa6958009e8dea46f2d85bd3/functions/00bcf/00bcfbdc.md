# 00bcfbdc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b606dc`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b606dc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0067.md#compare-fe352a951291394805d7293b5518527a)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd0004`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd0004.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-19ca6e125d78a996116fbd7e56675cf0)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfbdc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4UserEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "59a9b479201a35d99d9bea0bafdbe30c6e487453939eb986b5e1feb1229777c1",
  "source_text_sha256": "59a9b479201a35d99d9bea0bafdbe30c6e487453939eb986b5e1feb1229777c1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfbdc",
        "00bcfce3"
      ]
    ],
    "bytes_sha256": "dadaa3666ecf0aba73510a20e906161f17c0e30f48104c255926bdb4a1c45bbd",
    "instruction_count": 66,
    "instruction_bytes": 264,
    "body_bytes": 264,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5d7e0](../00c5d/00c5d7e0.md)

## 呼び出し先

- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5aa30](../00c5a/00c5aa30.md)
- [00c5aa50](../00c5a/00c5aa50.md)
- [00c5aa60](../00c5a/00c5aa60.md)
- [00c5aa70](../00c5a/00c5aa70.md)
- [00c5aa80](../00c5a/00c5aa80.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ac00](../00c5a/00c5ac00.md)
- [00c5ac70](../00c5a/00c5ac70.md)

## 関連文字列（未確認候補）

~~~text
"GetFutureStatus(handle) == kFutureStatusPending"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1759 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4UserEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
               (long *param_1,undefined8 *param_2,undefined4 param_3,undefined8 param_4)

{
  int iVar1;
  long lVar2;
  ulong uVar3;
  
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
  _ZN8firebase26ReferenceCountedFutureImpl11BackingDataEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl14CompleteHandleERKNS_12FutureHandleE(param_1,param_2);
  _ZN8firebase26ReferenceCountedFutureImpl13CompleteProxyEPNS_17FutureBackingDataE(param_1,lVar2);
  _ZN8firebase26ReferenceCountedFutureImpl27ReleaseMutexAndRunCallbacksERKNS_12FutureHandleE
            (param_1,param_2);
  uVar3 = _ZNK8firebase26ReferenceCountedFutureImpl11is_orphanedEv(param_1);
  if ((uVar3 & 1) != 0) {
                    /* try { // try from 00bcfca4 to 00ccfcaf has its CatchHandler @ 00bd0174 */
                    /* try { // try from 00bcfcb0 to 00ccfd0f has its CatchHandler @ 00bcfac4 */
                    /* WARNING: Could not recover jumptable at 0x00bcfcb4. Too many branches */
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
<a id="insn-00bcfbdc"></a> `00bcfbdc` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bcfbe0"></a> `00bcfbe0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfbe4"></a> `00bcfbe4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfbe8"></a> `00bcfbe8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfbec"></a> `00bcfbec` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bcfbf0"></a> `00bcfbf0` | `18 20 00 91` | add x24,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bcfbf4"></a> `00bcfbf4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcfbf8"></a> `00bcfbf8` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bcfbfc"></a> `00bcfbfc` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00bcfc00"></a> `00bcfc00` | `f7 03 02 2a` | mov w23,w2 | `FALL_THROUGH`
<a id="insn-00bcfc04"></a> `00bcfc04` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcfc08"></a> `00bcfc08` | `7e 2a 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc0c"></a> `00bcfc0c` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bcfc10"></a> `00bcfc10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc14"></a> `00bcfc14` | `9b 2b 02 94` | bl 0x00c5aa80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc18"></a> `00bcfc18` | `00 05 00 b4` | cbz x0,0x00bcfcb8 | `CONDITIONAL_JUMP`
<a id="insn-00bcfc1c"></a> `00bcfc1c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcfc20"></a> `00bcfc20` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcfc24"></a> `00bcfc24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc28"></a> `00bcfc28` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfc2c"></a> `00bcfc2c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfc30"></a> `00bcfc30` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfc34"></a> `00bcfc34` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfc38"></a> `00bcfc38` | `80 00 00 54` | b.eq 0x00bcfc48 | `CONDITIONAL_JUMP`
<a id="insn-00bcfc3c"></a> `00bcfc3c` | `c0 b6 ff 90` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bcfc40"></a> `00bcfc40` | `00 20 00 91` | add x0,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bcfc44"></a> `00bcfc44` | `ef 2b 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc48"></a> `00bcfc48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc4c"></a> `00bcfc4c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcfc50"></a> `00bcfc50` | `e2 03 17 2a` | mov w2,w23 | `FALL_THROUGH`
<a id="insn-00bcfc54"></a> `00bcfc54` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00bcfc58"></a> `00bcfc58` | `86 2b 02 94` | bl 0x00c5aa70 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc5c"></a> `00bcfc5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc60"></a> `00bcfc60` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcfc64"></a> `00bcfc64` | `73 2b 02 94` | bl 0x00c5aa30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc68"></a> `00bcfc68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc6c"></a> `00bcfc6c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfc70"></a> `00bcfc70` | `7c 2b 02 94` | bl 0x00c5aa60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc74"></a> `00bcfc74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc78"></a> `00bcfc78` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcfc7c"></a> `00bcfc7c` | `75 2b 02 94` | bl 0x00c5aa50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc80"></a> `00bcfc80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc84"></a> `00bcfc84` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfc88"></a> `00bcfc88` | `82 2b 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc8c"></a> `00bcfc8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfc90"></a> `00bcfc90` | `f8 2b 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfc94"></a> `00bcfc94` | `e0 01 00 36` | tbz w0,#0x0,0x00bcfcd0 | `CONDITIONAL_JUMP`
<a id="insn-00bcfc98"></a> `00bcfc98` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcfc9c"></a> `00bcfc9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfca0"></a> `00bcfca0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfca4"></a> `00bcfca4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfca8"></a> `00bcfca8` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfcac"></a> `00bcfcac` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfcb0"></a> `00bcfcb0` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcfcb4"></a> `00bcfcb4` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bcfcb8"></a> `00bcfcb8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfcbc"></a> `00bcfcbc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfcc0"></a> `00bcfcc0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfcc4"></a> `00bcfcc4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bcfcc8"></a> `00bcfcc8` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcfccc"></a> `00bcfccc` | `51 2a 02 14` | b 0x00c5a610 | `CALL_TERMINATOR`
<a id="insn-00bcfcd0"></a> `00bcfcd0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfcd4"></a> `00bcfcd4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfcd8"></a> `00bcfcd8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfcdc"></a> `00bcfcdc` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bcfce0"></a> `00bcfce0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfbdc`](#insn-00bcfbdc) 範囲 `[['00bcfbdc', '00bcfc1b']]`
  - `CONDITIONAL_JUMP` [`00bcfc18`](#insn-00bcfc18) → [`00bcfcb8`](#insn-00bcfcb8)
  - `FALL_THROUGH` [`00bcfc18`](#insn-00bcfc18) → [`00bcfc1c`](#insn-00bcfc1c)
- ブロック [`00bcfc1c`](#insn-00bcfc1c) 範囲 `[['00bcfc1c', '00bcfc3b']]`
  - `CONDITIONAL_JUMP` [`00bcfc38`](#insn-00bcfc38) → [`00bcfc48`](#insn-00bcfc48)
  - `FALL_THROUGH` [`00bcfc38`](#insn-00bcfc38) → [`00bcfc3c`](#insn-00bcfc3c)
- ブロック [`00bcfc3c`](#insn-00bcfc3c) 範囲 `[['00bcfc3c', '00bcfc47']]`
  - `FALL_THROUGH` [`00bcfc44`](#insn-00bcfc44) → [`00bcfc48`](#insn-00bcfc48)
- ブロック [`00bcfc48`](#insn-00bcfc48) 範囲 `[['00bcfc48', '00bcfc97']]`
  - `CONDITIONAL_JUMP` [`00bcfc94`](#insn-00bcfc94) → [`00bcfcd0`](#insn-00bcfcd0)
  - `FALL_THROUGH` [`00bcfc94`](#insn-00bcfc94) → [`00bcfc98`](#insn-00bcfc98)
- ブロック [`00bcfc98`](#insn-00bcfc98) 範囲 `[['00bcfc98', '00bcfca3']]`
  - `FALL_THROUGH` [`00bcfca0`](#insn-00bcfca0) → [`00bcfca4`](#insn-00bcfca4)
- ブロック [`00bcfca4`](#insn-00bcfca4) 範囲 `[['00bcfca4', '00bcfcaf']]`
  - `FALL_THROUGH` [`00bcfcac`](#insn-00bcfcac) → [`00bcfcb0`](#insn-00bcfcb0)
- ブロック [`00bcfcb0`](#insn-00bcfcb0) 範囲 `[['00bcfcb0', '00bcfcb7']]`
- ブロック [`00bcfcb8`](#insn-00bcfcb8) 範囲 `[['00bcfcb8', '00bcfccf']]`
- ブロック [`00bcfcd0`](#insn-00bcfcd0) 範囲 `[['00bcfcd0', '00bcfce3']]`

## 命令位置別の参照

- [`00bcfbdc`](#insn-00bcfbdc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfbe0`](#insn-00bcfbe0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfbe4`](#insn-00bcfbe4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfbe8`](#insn-00bcfbe8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc08`](#insn-00bcfc08) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc14`](#insn-00bcfc14) → [`00c5aa80`](../00c5a/00c5aa80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa80` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc18`](#insn-00bcfc18) → [`00bcfcb8`](#insn-00bcfcb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc38`](#insn-00bcfc38) → [`00bcfc48`](#insn-00bcfc48) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc40`](#insn-00bcfc40) → `002a7008`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcfc44`](#insn-00bcfc44) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc58`](#insn-00bcfc58) → [`00c5aa70`](../00c5a/00c5aa70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa70` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc64`](#insn-00bcfc64) → [`00c5aa30`](../00c5a/00c5aa30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa30` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc70`](#insn-00bcfc70) → [`00c5aa60`](../00c5a/00c5aa60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa60` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc7c`](#insn-00bcfc7c) → [`00c5aa50`](../00c5a/00c5aa50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa50` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc88`](#insn-00bcfc88) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc90`](#insn-00bcfc90) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bcfc94`](#insn-00bcfc94) → [`00bcfcd0`](#insn-00bcfcd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfca0`](#insn-00bcfca0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfca4`](#insn-00bcfca4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcac`](#insn-00bcfcac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcb8`](#insn-00bcfcb8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcbc`](#insn-00bcfcbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcc0`](#insn-00bcfcc0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfccc`](#insn-00bcfccc) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcd0`](#insn-00bcfcd0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcd4`](#insn-00bcfcd4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfcd8`](#insn-00bcfcd8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfbdc`](#insn-00bcfbdc)

~~~json
{
  "source": "00bcfbdc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfbe0`](#insn-00bcfbe0)

~~~json
{
  "source": "00bcfbe0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfbe4`](#insn-00bcfbe4)

~~~json
{
  "source": "00bcfbe4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfbe8`](#insn-00bcfbe8)

~~~json
{
  "source": "00bcfbe8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc08`](#insn-00bcfc08)

~~~json
{
  "source": "00bcfc08",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc14`](#insn-00bcfc14)

~~~json
{
  "source": "00bcfc14",
  "target": "00c5aa80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc18`](#insn-00bcfc18)

~~~json
{
  "source": "00bcfc18",
  "target": "00bcfcb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc38`](#insn-00bcfc38)

~~~json
{
  "source": "00bcfc38",
  "target": "00bcfc48",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfc40`](#insn-00bcfc40)

~~~json
{
  "source": "00bcfc40",
  "target": "002a7008",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7008",
  "offset": 0,
  "size": 48,
  "datatype": "string",
  "bytes": "4765744675747572655374617475732868616e646c6529203d3d206b46757475",
  "capture_start": "002a7008",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bcfc44`](#insn-00bcfc44)

~~~json
{
  "source": "00bcfc44",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc58`](#insn-00bcfc58)

~~~json
{
  "source": "00bcfc58",
  "target": "00c5aa70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc64`](#insn-00bcfc64)

~~~json
{
  "source": "00bcfc64",
  "target": "00c5aa30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc70`](#insn-00bcfc70)

~~~json
{
  "source": "00bcfc70",
  "target": "00c5aa60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc7c`](#insn-00bcfc7c)

~~~json
{
  "source": "00bcfc7c",
  "target": "00c5aa50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc88`](#insn-00bcfc88)

~~~json
{
  "source": "00bcfc88",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc90`](#insn-00bcfc90)

~~~json
{
  "source": "00bcfc90",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfc94`](#insn-00bcfc94)

~~~json
{
  "source": "00bcfc94",
  "target": "00bcfcd0",
  "target_space": "ram",
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
- 参照命令 [`00bcfcac`](#insn-00bcfcac)

~~~json
{
  "source": "00bcfcac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcb8`](#insn-00bcfcb8)

~~~json
{
  "source": "00bcfcb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcbc`](#insn-00bcfcbc)

~~~json
{
  "source": "00bcfcbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcc0`](#insn-00bcfcc0)

~~~json
{
  "source": "00bcfcc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfccc`](#insn-00bcfccc)

~~~json
{
  "source": "00bcfccc",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfcd0`](#insn-00bcfcd0)

~~~json
{
  "source": "00bcfcd0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcd4`](#insn-00bcfcd4)

~~~json
{
  "source": "00bcfcd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfcd8`](#insn-00bcfcd8)

~~~json
{
  "source": "00bcfcd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
