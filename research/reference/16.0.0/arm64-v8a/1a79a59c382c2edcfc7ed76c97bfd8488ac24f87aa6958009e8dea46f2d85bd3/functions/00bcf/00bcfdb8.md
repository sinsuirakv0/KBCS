# 00bcfdb8

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b608b8`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b60/00b608b8.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0067.md#compare-131df35565691c664c0fc2f5d4371694)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bd01e0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bd0/00bd01e0.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0082.md#compare-e62828a13812c178083aa68c21bd3791)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcfdb8",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4UserEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "97faf76b8e9f7d0fa63d27e65c5675b49904615183763c748520a2d515337cca",
  "source_text_sha256": "97faf76b8e9f7d0fa63d27e65c5675b49904615183763c748520a2d515337cca",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcfdb8",
        "00bcfeef"
      ]
    ],
    "bytes_sha256": "6eb74327eb69c84bf591d87888e155cfe74d852246e672b2175c69f462134753",
    "instruction_count": 78,
    "instruction_bytes": 312,
    "body_bytes": 312,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [00c5d7b0](../00c5d/00c5d7b0.md)

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

## 疑似コード / UTF-8 1855 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINS_4auth4UserEZNS2_14FutureCallbackIS3_EEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPvEUlSD_E_EEvRKNS_12FutureHandleEiSC_RKT0_
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
                    /* WARNING: Could not recover jumptable at 0x00bcfeb8. Too many branches */
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
<a id="insn-00bcfdb8"></a> `00bcfdb8` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bcfdbc"></a> `00bcfdbc` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfdc0"></a> `00bcfdc0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfdc4"></a> `00bcfdc4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfdc8"></a> `00bcfdc8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfdcc"></a> `00bcfdcc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bcfdd0"></a> `00bcfdd0` | `19 20 00 91` | add x25,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bcfdd4"></a> `00bcfdd4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bcfdd8"></a> `00bcfdd8` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bcfddc"></a> `00bcfddc` | `f5 03 04 aa` | mov x21,x4 | `FALL_THROUGH`
<a id="insn-00bcfde0"></a> `00bcfde0` | `f7 03 03 aa` | mov x23,x3 | `FALL_THROUGH`
<a id="insn-00bcfde4"></a> `00bcfde4` | `f8 03 02 2a` | mov w24,w2 | `FALL_THROUGH`
<a id="insn-00bcfde8"></a> `00bcfde8` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bcfdec"></a> `00bcfdec` | `05 2a 02 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfdf0"></a> `00bcfdf0` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00bcfdf4"></a> `00bcfdf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfdf8"></a> `00bcfdf8` | `22 2b 02 94` | bl 0x00c5aa80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfdfc"></a> `00bcfdfc` | `00 06 00 b4` | cbz x0,0x00bcfebc | `CONDITIONAL_JUMP`
<a id="insn-00bcfe00"></a> `00bcfe00` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcfe04"></a> `00bcfe04` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcfe08"></a> `00bcfe08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfe0c"></a> `00bcfe0c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfe10"></a> `00bcfe10` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfe14"></a> `00bcfe14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfe18"></a> `00bcfe18` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bcfe1c"></a> `00bcfe1c` | `80 00 00 54` | b.eq 0x00bcfe2c | `CONDITIONAL_JUMP`
<a id="insn-00bcfe20"></a> `00bcfe20` | `c0 b6 ff 90` | adrp x0,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bcfe24"></a> `00bcfe24` | `00 20 00 91` | add x0,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00bcfe28"></a> `00bcfe28` | `76 2b 02 94` | bl 0x00c5ac00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe2c"></a> `00bcfe2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfe30"></a> `00bcfe30` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcfe34"></a> `00bcfe34` | `e2 03 18 2a` | mov w2,w24 | `FALL_THROUGH`
<a id="insn-00bcfe38"></a> `00bcfe38` | `e3 03 17 aa` | mov x3,x23 | `FALL_THROUGH`
<a id="insn-00bcfe3c"></a> `00bcfe3c` | `0d 2b 02 94` | bl 0x00c5aa70 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe40"></a> `00bcfe40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfe44"></a> `00bcfe44` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcfe48"></a> `00bcfe48` | `fa 2a 02 94` | bl 0x00c5aa30 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe4c"></a> `00bcfe4c` | `a1 0a 40 f9` | ldr x1,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfe50"></a> `00bcfe50` | `28 0c 40 f9` | ldr x8,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-00bcfe54"></a> `00bcfe54` | `a8 00 00 b4` | cbz x8,0x00bcfe68 | `CONDITIONAL_JUMP`
<a id="insn-00bcfe58"></a> `00bcfe58` | `e3 03 00 aa` | mov x3,x0 | `FALL_THROUGH`
<a id="insn-00bcfe5c"></a> `00bcfe5c` | `a0 02 40 f9` | ldr x0,[x21] | `FALL_THROUGH`
<a id="insn-00bcfe60"></a> `00bcfe60` | `a2 22 40 39` | ldrb w2,[x21, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfe64"></a> `00bcfe64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcfe68"></a> `00bcfe68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfe6c"></a> `00bcfe6c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfe70"></a> `00bcfe70` | `fc 2a 02 94` | bl 0x00c5aa60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe74"></a> `00bcfe74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfe78"></a> `00bcfe78` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcfe7c"></a> `00bcfe7c` | `f5 2a 02 94` | bl 0x00c5aa50 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe80"></a> `00bcfe80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfe84"></a> `00bcfe84` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcfe88"></a> `00bcfe88` | `02 2b 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe8c"></a> `00bcfe8c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfe90"></a> `00bcfe90` | `78 2b 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bcfe94"></a> `00bcfe94` | `20 02 00 36` | tbz w0,#0x0,0x00bcfed8 | `CONDITIONAL_JUMP`
<a id="insn-00bcfe98"></a> `00bcfe98` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bcfe9c"></a> `00bcfe9c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcfea0"></a> `00bcfea0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfea4"></a> `00bcfea4` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfea8"></a> `00bcfea8` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bcfeac"></a> `00bcfeac` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfeb0"></a> `00bcfeb0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfeb4"></a> `00bcfeb4` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcfeb8"></a> `00bcfeb8` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00bcfebc"></a> `00bcfebc` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfec0"></a> `00bcfec0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfec4"></a> `00bcfec4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfec8"></a> `00bcfec8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfecc"></a> `00bcfecc` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bcfed0"></a> `00bcfed0` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcfed4"></a> `00bcfed4` | `cf 29 02 14` | b 0x00c5a610 | `CALL_TERMINATOR`
<a id="insn-00bcfed8"></a> `00bcfed8` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcfedc"></a> `00bcfedc` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcfee0"></a> `00bcfee0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcfee4"></a> `00bcfee4` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bcfee8"></a> `00bcfee8` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bcfeec"></a> `00bcfeec` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcfdb8`](#insn-00bcfdb8) 範囲 `[['00bcfdb8', '00bcfdff']]`
  - `CONDITIONAL_JUMP` [`00bcfdfc`](#insn-00bcfdfc) → [`00bcfebc`](#insn-00bcfebc)
  - `FALL_THROUGH` [`00bcfdfc`](#insn-00bcfdfc) → [`00bcfe00`](#insn-00bcfe00)
- ブロック [`00bcfe00`](#insn-00bcfe00) 範囲 `[['00bcfe00', '00bcfe1f']]`
  - `CONDITIONAL_JUMP` [`00bcfe1c`](#insn-00bcfe1c) → [`00bcfe2c`](#insn-00bcfe2c)
  - `FALL_THROUGH` [`00bcfe1c`](#insn-00bcfe1c) → [`00bcfe20`](#insn-00bcfe20)
- ブロック [`00bcfe20`](#insn-00bcfe20) 範囲 `[['00bcfe20', '00bcfe2b']]`
  - `FALL_THROUGH` [`00bcfe28`](#insn-00bcfe28) → [`00bcfe2c`](#insn-00bcfe2c)
- ブロック [`00bcfe2c`](#insn-00bcfe2c) 範囲 `[['00bcfe2c', '00bcfe57']]`
  - `CONDITIONAL_JUMP` [`00bcfe54`](#insn-00bcfe54) → [`00bcfe68`](#insn-00bcfe68)
  - `FALL_THROUGH` [`00bcfe54`](#insn-00bcfe54) → [`00bcfe58`](#insn-00bcfe58)
- ブロック [`00bcfe58`](#insn-00bcfe58) 範囲 `[['00bcfe58', '00bcfe67']]`
  - `FALL_THROUGH` [`00bcfe64`](#insn-00bcfe64) → [`00bcfe68`](#insn-00bcfe68)
- ブロック [`00bcfe68`](#insn-00bcfe68) 範囲 `[['00bcfe68', '00bcfe97']]`
  - `CONDITIONAL_JUMP` [`00bcfe94`](#insn-00bcfe94) → [`00bcfed8`](#insn-00bcfed8)
  - `FALL_THROUGH` [`00bcfe94`](#insn-00bcfe94) → [`00bcfe98`](#insn-00bcfe98)
- ブロック [`00bcfe98`](#insn-00bcfe98) 範囲 `[['00bcfe98', '00bcfebb']]`
- ブロック [`00bcfebc`](#insn-00bcfebc) 範囲 `[['00bcfebc', '00bcfed7']]`
- ブロック [`00bcfed8`](#insn-00bcfed8) 範囲 `[['00bcfed8', '00bcfeef']]`

## 命令位置別の参照

- [`00bcfdb8`](#insn-00bcfdb8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfdbc`](#insn-00bcfdbc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfdc0`](#insn-00bcfdc0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfdc4`](#insn-00bcfdc4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfdc8`](#insn-00bcfdc8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfdec`](#insn-00bcfdec) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00bcfdf8`](#insn-00bcfdf8) → [`00c5aa80`](../00c5a/00c5aa80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa80` · 推定シンボル `None` · 推定型 `None`
- [`00bcfdfc`](#insn-00bcfdfc) → [`00bcfebc`](#insn-00bcfebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe1c`](#insn-00bcfe1c) → [`00bcfe2c`](#insn-00bcfe2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe24`](#insn-00bcfe24) → `002a7008`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bcfe28`](#insn-00bcfe28) → [`00c5ac00`](../00c5a/00c5ac00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac00` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe3c`](#insn-00bcfe3c) → [`00c5aa70`](../00c5a/00c5aa70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa70` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe48`](#insn-00bcfe48) → [`00c5aa30`](../00c5a/00c5aa30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa30` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe54`](#insn-00bcfe54) → [`00bcfe68`](#insn-00bcfe68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe70`](#insn-00bcfe70) → [`00c5aa60`](../00c5a/00c5aa60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa60` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe7c`](#insn-00bcfe7c) → [`00c5aa50`](../00c5a/00c5aa50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa50` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe88`](#insn-00bcfe88) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe90`](#insn-00bcfe90) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bcfe94`](#insn-00bcfe94) → [`00bcfed8`](#insn-00bcfed8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfea0`](#insn-00bcfea0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfea4`](#insn-00bcfea4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfeac`](#insn-00bcfeac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfeb0`](#insn-00bcfeb0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfebc`](#insn-00bcfebc) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfec0`](#insn-00bcfec0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfec4`](#insn-00bcfec4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfec8`](#insn-00bcfec8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfed4`](#insn-00bcfed4) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00bcfed8`](#insn-00bcfed8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfedc`](#insn-00bcfedc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfee0`](#insn-00bcfee0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcfee4`](#insn-00bcfee4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcfdb8`](#insn-00bcfdb8)

~~~json
{
  "source": "00bcfdb8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfdbc`](#insn-00bcfdbc)

~~~json
{
  "source": "00bcfdbc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfdc0`](#insn-00bcfdc0)

~~~json
{
  "source": "00bcfdc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfdc4`](#insn-00bcfdc4)

~~~json
{
  "source": "00bcfdc4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfdc8`](#insn-00bcfdc8)

~~~json
{
  "source": "00bcfdc8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfdec`](#insn-00bcfdec)

~~~json
{
  "source": "00bcfdec",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfdf8`](#insn-00bcfdf8)

~~~json
{
  "source": "00bcfdf8",
  "target": "00c5aa80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfdfc`](#insn-00bcfdfc)

~~~json
{
  "source": "00bcfdfc",
  "target": "00bcfebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe1c`](#insn-00bcfe1c)

~~~json
{
  "source": "00bcfe1c",
  "target": "00bcfe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe24`](#insn-00bcfe24)

~~~json
{
  "source": "00bcfe24",
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
- 参照命令 [`00bcfe28`](#insn-00bcfe28)

~~~json
{
  "source": "00bcfe28",
  "target": "00c5ac00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe3c`](#insn-00bcfe3c)

~~~json
{
  "source": "00bcfe3c",
  "target": "00c5aa70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe48`](#insn-00bcfe48)

~~~json
{
  "source": "00bcfe48",
  "target": "00c5aa30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe54`](#insn-00bcfe54)

~~~json
{
  "source": "00bcfe54",
  "target": "00bcfe68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfe70`](#insn-00bcfe70)

~~~json
{
  "source": "00bcfe70",
  "target": "00c5aa60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe7c`](#insn-00bcfe7c)

~~~json
{
  "source": "00bcfe7c",
  "target": "00c5aa50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe88`](#insn-00bcfe88)

~~~json
{
  "source": "00bcfe88",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe90`](#insn-00bcfe90)

~~~json
{
  "source": "00bcfe90",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfe94`](#insn-00bcfe94)

~~~json
{
  "source": "00bcfe94",
  "target": "00bcfed8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfea0`](#insn-00bcfea0)

~~~json
{
  "source": "00bcfea0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfea4`](#insn-00bcfea4)

~~~json
{
  "source": "00bcfea4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfeac`](#insn-00bcfeac)

~~~json
{
  "source": "00bcfeac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfeb0`](#insn-00bcfeb0)

~~~json
{
  "source": "00bcfeb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfebc`](#insn-00bcfebc)

~~~json
{
  "source": "00bcfebc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfec0`](#insn-00bcfec0)

~~~json
{
  "source": "00bcfec0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfec4`](#insn-00bcfec4)

~~~json
{
  "source": "00bcfec4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfec8`](#insn-00bcfec8)

~~~json
{
  "source": "00bcfec8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfed4`](#insn-00bcfed4)

~~~json
{
  "source": "00bcfed4",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcfed8`](#insn-00bcfed8)

~~~json
{
  "source": "00bcfed8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfedc`](#insn-00bcfedc)

~~~json
{
  "source": "00bcfedc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfee0`](#insn-00bcfee0)

~~~json
{
  "source": "00bcfee0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcfee4`](#insn-00bcfee4)

~~~json
{
  "source": "00bcfee4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
