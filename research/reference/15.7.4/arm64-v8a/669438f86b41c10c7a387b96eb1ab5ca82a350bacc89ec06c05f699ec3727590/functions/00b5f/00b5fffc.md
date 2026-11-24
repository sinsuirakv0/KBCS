# 00b5fffc

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00b5ffb8`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00b5f/00b5ffb8.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0070.md#compare-37f0d36c9d28b836894c7080e6b83576)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcf4fc`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcf/00bcf4fc.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0067.md#compare-ab1da60d8e74a3c5dec76e9d0fc43a86)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5fffc",
  "name": "_ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS8_iSA_RKT0_",
  "size": 264,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "2d44d6f95d34f137046f121ca902e9135fb0e238e33b2d34e834d136ce578c56",
  "source_text_sha256": "2d44d6f95d34f137046f121ca902e9135fb0e238e33b2d34e834d136ce578c56",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5fffc",
        "00b60103"
      ]
    ],
    "bytes_sha256": "2622a33e39d9cdbfd66781642504cb7c73694f91d5063e83ad902ac8325bb733",
    "instruction_count": 66,
    "instruction_bytes": 264,
    "body_bytes": 264,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00be0bd0](../00be0/00be0bd0.md)

## 呼び出し先

- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)
- [00bddfb0](../00bdd/00bddfb0.md)
- [00bddfd0](../00bdd/00bddfd0.md)
- [00bddfe0](../00bdd/00bddfe0.md)
- [00bddff0](../00bdd/00bddff0.md)
- [00bde000](../00bde/00bde000.md)
- [00bde010](../00bde/00bde010.md)
- [00bde180](../00bde/00bde180.md)
- [00bde1f0](../00bde/00bde1f0.md)

## 関連文字列（未確認候補）

~~~text
"GetFutureStatus(handle) == kFutureStatusPending"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1587 bytes

~~~c

void _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS8_iSA_RKT0_
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
                    /* WARNING: Could not recover jumptable at 0x00b600d4. Too many branches */
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
<a id="insn-00b5fffc"></a> `00b5fffc` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00b60000"></a> `00b60000` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b60004"></a> `00b60004` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b60008"></a> `00b60008` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b6000c"></a> `00b6000c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00b60010"></a> `00b60010` | `18 20 00 91` | add x24,x0,#0x8 | `FALL_THROUGH`
<a id="insn-00b60014"></a> `00b60014` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b60018"></a> `00b60018` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b6001c"></a> `00b6001c` | `f5 03 03 aa` | mov x21,x3 | `FALL_THROUGH`
<a id="insn-00b60020"></a> `00b60020` | `f7 03 02 2a` | mov w23,w2 | `FALL_THROUGH`
<a id="insn-00b60024"></a> `00b60024` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00b60028"></a> `00b60028` | `fe f6 01 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00b6002c"></a> `00b6002c` | `81 02 40 f9` | ldr x1,[x20] | `FALL_THROUGH`
<a id="insn-00b60030"></a> `00b60030` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b60034"></a> `00b60034` | `f3 f7 01 94` | bl 0x00bde000 | `UNCONDITIONAL_CALL`
<a id="insn-00b60038"></a> `00b60038` | `00 05 00 b4` | cbz x0,0x00b600d8 | `CONDITIONAL_JUMP`
<a id="insn-00b6003c"></a> `00b6003c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b60040"></a> `00b60040` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00b60044"></a> `00b60044` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b60048"></a> `00b60048` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b6004c"></a> `00b6004c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00b60050"></a> `00b60050` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b60054"></a> `00b60054` | `1f 04 00 71` | cmp w0,#0x1 | `FALL_THROUGH`
<a id="insn-00b60058"></a> `00b60058` | `80 00 00 54` | b.eq 0x00b60068 | `CONDITIONAL_JUMP`
<a id="insn-00b6005c"></a> `00b6005c` | `a0 b9 ff f0` | adrp x0,0x297000 | `FALL_THROUGH`
<a id="insn-00b60060"></a> `00b60060` | `00 9c 11 91` | add x0,x0,#0x467 | `FALL_THROUGH`
<a id="insn-00b60064"></a> `00b60064` | `47 f8 01 94` | bl 0x00bde180 | `UNCONDITIONAL_CALL`
<a id="insn-00b60068"></a> `00b60068` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6006c"></a> `00b6006c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b60070"></a> `00b60070` | `e2 03 17 2a` | mov w2,w23 | `FALL_THROUGH`
<a id="insn-00b60074"></a> `00b60074` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00b60078"></a> `00b60078` | `de f7 01 94` | bl 0x00bddff0 | `UNCONDITIONAL_CALL`
<a id="insn-00b6007c"></a> `00b6007c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b60080"></a> `00b60080` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b60084"></a> `00b60084` | `cb f7 01 94` | bl 0x00bddfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00b60088"></a> `00b60088` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b6008c"></a> `00b6008c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b60090"></a> `00b60090` | `d4 f7 01 94` | bl 0x00bddfe0 | `UNCONDITIONAL_CALL`
<a id="insn-00b60094"></a> `00b60094` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b60098"></a> `00b60098` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00b6009c"></a> `00b6009c` | `cd f7 01 94` | bl 0x00bddfd0 | `UNCONDITIONAL_CALL`
<a id="insn-00b600a0"></a> `00b600a0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b600a4"></a> `00b600a4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b600a8"></a> `00b600a8` | `da f7 01 94` | bl 0x00bde010 | `UNCONDITIONAL_CALL`
<a id="insn-00b600ac"></a> `00b600ac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b600b0"></a> `00b600b0` | `50 f8 01 94` | bl 0x00bde1f0 | `UNCONDITIONAL_CALL`
<a id="insn-00b600b4"></a> `00b600b4` | `e0 01 00 36` | tbz w0,#0x0,0x00b600f0 | `CONDITIONAL_JUMP`
<a id="insn-00b600b8"></a> `00b600b8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b600bc"></a> `00b600bc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b600c0"></a> `00b600c0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b600c4"></a> `00b600c4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b600c8"></a> `00b600c8` | `01 05 40 f9` | ldr x1,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b600cc"></a> `00b600cc` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b600d0"></a> `00b600d0` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b600d4"></a> `00b600d4` | `20 00 1f d6` | br x1 | `COMPUTED_JUMP`
<a id="insn-00b600d8"></a> `00b600d8` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b600dc"></a> `00b600dc` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b600e0"></a> `00b600e0` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b600e4"></a> `00b600e4` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b600e8"></a> `00b600e8` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b600ec"></a> `00b600ec` | `d1 f6 01 14` | b 0x00bddc30 | `CALL_TERMINATOR`
<a id="insn-00b600f0"></a> `00b600f0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b600f4"></a> `00b600f4` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b600f8"></a> `00b600f8` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b600fc"></a> `00b600fc` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00b60100"></a> `00b60100` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5fffc`](#insn-00b5fffc) 範囲 `[['00b5fffc', '00b6003b']]`
  - `CONDITIONAL_JUMP` [`00b60038`](#insn-00b60038) → [`00b600d8`](#insn-00b600d8)
  - `FALL_THROUGH` [`00b60038`](#insn-00b60038) → [`00b6003c`](#insn-00b6003c)
- ブロック [`00b6003c`](#insn-00b6003c) 範囲 `[['00b6003c', '00b6005b']]`
  - `CONDITIONAL_JUMP` [`00b60058`](#insn-00b60058) → [`00b60068`](#insn-00b60068)
  - `FALL_THROUGH` [`00b60058`](#insn-00b60058) → [`00b6005c`](#insn-00b6005c)
- ブロック [`00b6005c`](#insn-00b6005c) 範囲 `[['00b6005c', '00b60067']]`
  - `FALL_THROUGH` [`00b60064`](#insn-00b60064) → [`00b60068`](#insn-00b60068)
- ブロック [`00b60068`](#insn-00b60068) 範囲 `[['00b60068', '00b600b7']]`
  - `CONDITIONAL_JUMP` [`00b600b4`](#insn-00b600b4) → [`00b600f0`](#insn-00b600f0)
  - `FALL_THROUGH` [`00b600b4`](#insn-00b600b4) → [`00b600b8`](#insn-00b600b8)
- ブロック [`00b600b8`](#insn-00b600b8) 範囲 `[['00b600b8', '00b600d7']]`
- ブロック [`00b600d8`](#insn-00b600d8) 範囲 `[['00b600d8', '00b600ef']]`
- ブロック [`00b600f0`](#insn-00b600f0) 範囲 `[['00b600f0', '00b60103']]`

## 命令位置別の参照

- [`00b5fffc`](#insn-00b5fffc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b60000`](#insn-00b60000) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b60004`](#insn-00b60004) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b60008`](#insn-00b60008) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b60028`](#insn-00b60028) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00b60034`](#insn-00b60034) → [`00bde000`](../00bde/00bde000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde000` · 推定シンボル `None` · 推定型 `None`
- [`00b60038`](#insn-00b60038) → [`00b600d8`](#insn-00b600d8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b60058`](#insn-00b60058) → [`00b60068`](#insn-00b60068) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b60060`](#insn-00b60060) → `00297467`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00b60064`](#insn-00b60064) → [`00bde180`](../00bde/00bde180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde180` · 推定シンボル `None` · 推定型 `None`
- [`00b60078`](#insn-00b60078) → [`00bddff0`](../00bdd/00bddff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddff0` · 推定シンボル `None` · 推定型 `None`
- [`00b60084`](#insn-00b60084) → [`00bddfb0`](../00bdd/00bddfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfb0` · 推定シンボル `None` · 推定型 `None`
- [`00b60090`](#insn-00b60090) → [`00bddfe0`](../00bdd/00bddfe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfe0` · 推定シンボル `None` · 推定型 `None`
- [`00b6009c`](#insn-00b6009c) → [`00bddfd0`](../00bdd/00bddfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddfd0` · 推定シンボル `None` · 推定型 `None`
- [`00b600a8`](#insn-00b600a8) → [`00bde010`](../00bde/00bde010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde010` · 推定シンボル `None` · 推定型 `None`
- [`00b600b0`](#insn-00b600b0) → [`00bde1f0`](../00bde/00bde1f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde1f0` · 推定シンボル `None` · 推定型 `None`
- [`00b600b4`](#insn-00b600b4) → [`00b600f0`](#insn-00b600f0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b600c0`](#insn-00b600c0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b600c4`](#insn-00b600c4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b600cc`](#insn-00b600cc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b600d8`](#insn-00b600d8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b600dc`](#insn-00b600dc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b600e0`](#insn-00b600e0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b600ec`](#insn-00b600ec) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00b600f0`](#insn-00b600f0) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b600f4`](#insn-00b600f4) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b600f8`](#insn-00b600f8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5fffc`](#insn-00b5fffc)

~~~json
{
  "source": "00b5fffc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b60000`](#insn-00b60000)

~~~json
{
  "source": "00b60000",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b60004`](#insn-00b60004)

~~~json
{
  "source": "00b60004",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b60008`](#insn-00b60008)

~~~json
{
  "source": "00b60008",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b60028`](#insn-00b60028)

~~~json
{
  "source": "00b60028",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b60034`](#insn-00b60034)

~~~json
{
  "source": "00b60034",
  "target": "00bde000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b60038`](#insn-00b60038)

~~~json
{
  "source": "00b60038",
  "target": "00b600d8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b60058`](#insn-00b60058)

~~~json
{
  "source": "00b60058",
  "target": "00b60068",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b60060`](#insn-00b60060)

~~~json
{
  "source": "00b60060",
  "target": "00297467",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00297467",
  "offset": 0,
  "size": 48,
  "datatype": "string",
  "bytes": "4765744675747572655374617475732868616e646c6529203d3d206b46757475",
  "capture_start": "00297467",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00b60064`](#insn-00b60064)

~~~json
{
  "source": "00b60064",
  "target": "00bde180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b60078`](#insn-00b60078)

~~~json
{
  "source": "00b60078",
  "target": "00bddff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b60084`](#insn-00b60084)

~~~json
{
  "source": "00b60084",
  "target": "00bddfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b60090`](#insn-00b60090)

~~~json
{
  "source": "00b60090",
  "target": "00bddfe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b6009c`](#insn-00b6009c)

~~~json
{
  "source": "00b6009c",
  "target": "00bddfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b600a8`](#insn-00b600a8)

~~~json
{
  "source": "00b600a8",
  "target": "00bde010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b600b0`](#insn-00b600b0)

~~~json
{
  "source": "00b600b0",
  "target": "00bde1f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b600b4`](#insn-00b600b4)

~~~json
{
  "source": "00b600b4",
  "target": "00b600f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b600c0`](#insn-00b600c0)

~~~json
{
  "source": "00b600c0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b600c4`](#insn-00b600c4)

~~~json
{
  "source": "00b600c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b600cc`](#insn-00b600cc)

~~~json
{
  "source": "00b600cc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b600d8`](#insn-00b600d8)

~~~json
{
  "source": "00b600d8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b600dc`](#insn-00b600dc)

~~~json
{
  "source": "00b600dc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b600e0`](#insn-00b600e0)

~~~json
{
  "source": "00b600e0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b600ec`](#insn-00b600ec)

~~~json
{
  "source": "00b600ec",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b600f0`](#insn-00b600f0)

~~~json
{
  "source": "00b600f0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b600f4`](#insn-00b600f4)

~~~json
{
  "source": "00b600f4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b600f8`](#insn-00b600f8)

~~~json
{
  "source": "00b600f8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
