# 00bcde4c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bcddb0`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bcd/00bcddb0.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-7d41db8a9fb1a24b9cf08e1f91efceb4)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bcee40`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bce/00bcee40.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/inspection-0036.md#compare-3f032bc313a2f47abe4706998cd4113b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcde4c",
  "name": "_ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "fea7e615e59ea2afc10979236807e2bc4df7e5dfd0e62c67fec0099e5dd597d8",
  "source_text_sha256": "fea7e615e59ea2afc10979236807e2bc4df7e5dfd0e62c67fec0099e5dd597d8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcde4c",
        "00bcdf1b"
      ]
    ],
    "bytes_sha256": "b5b0dff334819975091cd40ea4cafb5414b95059dbfbb44342a6076a1155e8ef",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5ddb0](../00c5d/00c5ddb0.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ab60](../00c5a/00c5ab60.md)
- [00c5aed0](../00c5a/00c5aed0.md)
- [00c5dca0](../00c5d/00c5dca0.md)
- [00c5dde0](../00c5d/00c5dde0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1849 bytes

~~~c

undefined8
_ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
          (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  void *pvVar1;
  long lVar2;
  int iVar3;
  undefined8 uVar4;
  undefined1 auStack_68 [16];
  ulong local_58;
  undefined8 local_50;
  void *local_48;
  undefined1 auStack_40 [8];
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00bcde68 to 00ccde6f has its CatchHandler @ 00bce950 */
  local_50 = 0;
  local_48 = (void *)0x0;
  local_58 = 0;
  iVar3 = _ZN8firebase4auth30CheckAndClearJniAuthExceptionsEP7_JNIEnvPNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
                    (param_1,&local_58);
  if (iVar3 == 0) {
    uVar4 = 0;
  }
  else {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_68,param_3);
                    /* try { // try from 00bcdea4 to 00ccdeab has its CatchHandler @ 00bce948 */
    pvVar1 = (void *)((ulong)&local_58 | 1);
    if ((local_58 & 1) != 0) {
      pvVar1 = local_48;
    }
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS8_iSA_RKT0_
              (param_2,auStack_68,iVar3,pvVar1,auStack_40);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
    uVar4 = 1;
  }
  if ((local_58 & 1) != 0) {
                    /* try { // try from 00bcded8 to 00ccdef7 has its CatchHandler @ 00bce938 */
    _ZdlPv(local_48);
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* try { // try from 00bcdf04 to 00ccdf23 has its CatchHandler @ 00bce928 */
    return uVar4;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcde4c"></a> `00bcde4c` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcde50"></a> `00bcde50` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcde54"></a> `00bcde54` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcde58"></a> `00bcde58` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcde5c"></a> `00bcde5c` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcde60"></a> `00bcde60` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcde64"></a> `00bcde64` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcde68"></a> `00bcde68` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bcde6c"></a> `00bcde6c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcde70"></a> `00bcde70` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bcde74"></a> `00bcde74` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcde78"></a> `00bcde78` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcde7c"></a> `00bcde7c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcde80"></a> `00bcde80` | `d8 3f 02 94` | bl 0x00c5dde0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcde84"></a> `00bcde84` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bcde88"></a> `00bcde88` | `00 04 00 34` | cbz w0,0x00bcdf08 | `CONDITIONAL_JUMP`
<a id="insn-00bcde8c"></a> `00bcde8c` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcde90"></a> `00bcde90` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcde94"></a> `00bcde94` | `0f 34 02 94` | bl 0x00c5aed0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcde98"></a> `00bcde98` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcde9c"></a> `00bcde9c` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdea0"></a> `00bcdea0` | `ea 63 00 91` | add x10,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdea4"></a> `00bcdea4` | `4a 01 40 b2` | orr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdea8"></a> `00bcdea8` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdeac"></a> `00bcdeac` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bcdeb0"></a> `00bcdeb0` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdeb4"></a> `00bcdeb4` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bcdeb8"></a> `00bcdeb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdebc"></a> `00bcdebc` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00bcdec0"></a> `00bcdec0` | `78 3f 02 94` | bl 0x00c5dca0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdec4"></a> `00bcdec4` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdec8"></a> `00bcdec8` | `26 33 02 94` | bl 0x00c5ab60 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdecc"></a> `00bcdecc` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00bcded0"></a> `00bcded0` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcded4"></a> `00bcded4` | `68 00 00 36` | tbz w8,#0x0,0x00bcdee0 | `CONDITIONAL_JUMP`
<a id="insn-00bcded8"></a> `00bcded8` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdedc"></a> `00bcdedc` | `29 28 02 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdee0"></a> `00bcdee0` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdee4"></a> `00bcdee4` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bcdee8"></a> `00bcdee8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcdeec"></a> `00bcdeec` | `61 01 00 54` | b.ne 0x00bcdf18 | `CONDITIONAL_JUMP`
<a id="insn-00bcdef0"></a> `00bcdef0` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bcdef4"></a> `00bcdef4` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcdef8"></a> `00bcdef8` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcdefc"></a> `00bcdefc` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcdf00"></a> `00bcdf00` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcdf04"></a> `00bcdf04` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcdf08"></a> `00bcdf08` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00bcdf0c"></a> `00bcdf0c` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcdf10"></a> `00bcdf10` | `48 fe 07 37` | tbnz w8,#0x0,0x00bcded8 | `CONDITIONAL_JUMP`
<a id="insn-00bcdf14"></a> `00bcdf14` | `f3 ff ff 17` | b 0x00bcdee0 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdf18"></a> `00bcdf18` | `26 28 02 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcde4c`](#insn-00bcde4c) 範囲 `[['00bcde4c', '00bcde67']]`
  - `FALL_THROUGH` [`00bcde64`](#insn-00bcde64) → [`00bcde68`](#insn-00bcde68)
- ブロック [`00bcde68`](#insn-00bcde68) 範囲 `[['00bcde68', '00bcde8b']]`
  - `CONDITIONAL_JUMP` [`00bcde88`](#insn-00bcde88) → [`00bcdf08`](#insn-00bcdf08)
  - `FALL_THROUGH` [`00bcde88`](#insn-00bcde88) → [`00bcde8c`](#insn-00bcde8c)
- ブロック [`00bcde8c`](#insn-00bcde8c) 範囲 `[['00bcde8c', '00bcdea3']]`
  - `FALL_THROUGH` [`00bcdea0`](#insn-00bcdea0) → [`00bcdea4`](#insn-00bcdea4)
- ブロック [`00bcdea4`](#insn-00bcdea4) 範囲 `[['00bcdea4', '00bcded7']]`
  - `CONDITIONAL_JUMP` [`00bcded4`](#insn-00bcded4) → [`00bcdee0`](#insn-00bcdee0)
  - `FALL_THROUGH` [`00bcded4`](#insn-00bcded4) → [`00bcded8`](#insn-00bcded8)
- ブロック [`00bcded8`](#insn-00bcded8) 範囲 `[['00bcded8', '00bcdedf']]`
  - `FALL_THROUGH` [`00bcdedc`](#insn-00bcdedc) → [`00bcdee0`](#insn-00bcdee0)
- ブロック [`00bcdee0`](#insn-00bcdee0) 範囲 `[['00bcdee0', '00bcdeef']]`
  - `CONDITIONAL_JUMP` [`00bcdeec`](#insn-00bcdeec) → [`00bcdf18`](#insn-00bcdf18)
  - `FALL_THROUGH` [`00bcdeec`](#insn-00bcdeec) → [`00bcdef0`](#insn-00bcdef0)
- ブロック [`00bcdef0`](#insn-00bcdef0) 範囲 `[['00bcdef0', '00bcdf03']]`
  - `FALL_THROUGH` [`00bcdf00`](#insn-00bcdf00) → [`00bcdf04`](#insn-00bcdf04)
- ブロック [`00bcdf04`](#insn-00bcdf04) 範囲 `[['00bcdf04', '00bcdf07']]`
- ブロック [`00bcdf08`](#insn-00bcdf08) 範囲 `[['00bcdf08', '00bcdf13']]`
  - `CONDITIONAL_JUMP` [`00bcdf10`](#insn-00bcdf10) → [`00bcded8`](#insn-00bcded8)
  - `FALL_THROUGH` [`00bcdf10`](#insn-00bcdf10) → [`00bcdf14`](#insn-00bcdf14)
- ブロック [`00bcdf14`](#insn-00bcdf14) 範囲 `[['00bcdf14', '00bcdf17']]`
  - `UNCONDITIONAL_JUMP` [`00bcdf14`](#insn-00bcdf14) → [`00bcdee0`](#insn-00bcdee0)
- ブロック [`00bcdf18`](#insn-00bcdf18) 範囲 `[['00bcdf18', '00bcdf1b']]`

## 命令位置別の参照

- [`00bcde50`](#insn-00bcde50) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde54`](#insn-00bcde54) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde58`](#insn-00bcde58) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde70`](#insn-00bcde70) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde74`](#insn-00bcde74) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde78`](#insn-00bcde78) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde80`](#insn-00bcde80) → [`00c5dde0`](../00c5d/00c5dde0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dde0` · 推定シンボル `None` · 推定型 `None`
- [`00bcde88`](#insn-00bcde88) → [`00bcdf08`](#insn-00bcdf08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde94`](#insn-00bcde94) → [`00c5aed0`](../00c5a/00c5aed0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aed0` · 推定シンボル `None` · 推定型 `None`
- [`00bcde98`](#insn-00bcde98) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde9c`](#insn-00bcde9c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdec0`](#insn-00bcdec0) → [`00c5dca0`](../00c5d/00c5dca0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dca0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdec8`](#insn-00bcdec8) → [`00c5ab60`](../00c5a/00c5ab60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab60` · 推定シンボル `None` · 推定型 `None`
- [`00bcded0`](#insn-00bcded0) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcded4`](#insn-00bcded4) → [`00bcdee0`](#insn-00bcdee0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcded8`](#insn-00bcded8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdedc`](#insn-00bcdedc) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00bcdee4`](#insn-00bcdee4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdeec`](#insn-00bcdeec) → [`00bcdf18`](#insn-00bcdf18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdef4`](#insn-00bcdef4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdef8`](#insn-00bcdef8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdefc`](#insn-00bcdefc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf0c`](#insn-00bcdf0c) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf10`](#insn-00bcdf10) → [`00bcded8`](#insn-00bcded8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf14`](#insn-00bcdf14) → [`00bcdee0`](#insn-00bcdee0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdf18`](#insn-00bcdf18) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcde50`](#insn-00bcde50)

~~~json
{
  "source": "00bcde50",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde54`](#insn-00bcde54)

~~~json
{
  "source": "00bcde54",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde58`](#insn-00bcde58)

~~~json
{
  "source": "00bcde58",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde70`](#insn-00bcde70)

~~~json
{
  "source": "00bcde70",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde74`](#insn-00bcde74)

~~~json
{
  "source": "00bcde74",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde78`](#insn-00bcde78)

~~~json
{
  "source": "00bcde78",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde80`](#insn-00bcde80)

~~~json
{
  "source": "00bcde80",
  "target": "00c5dde0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcde88`](#insn-00bcde88)

~~~json
{
  "source": "00bcde88",
  "target": "00bcdf08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde94`](#insn-00bcde94)

~~~json
{
  "source": "00bcde94",
  "target": "00c5aed0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcde98`](#insn-00bcde98)

~~~json
{
  "source": "00bcde98",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde9c`](#insn-00bcde9c)

~~~json
{
  "source": "00bcde9c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdec0`](#insn-00bcdec0)

~~~json
{
  "source": "00bcdec0",
  "target": "00c5dca0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdec8`](#insn-00bcdec8)

~~~json
{
  "source": "00bcdec8",
  "target": "00c5ab60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcded0`](#insn-00bcded0)

~~~json
{
  "source": "00bcded0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcded4`](#insn-00bcded4)

~~~json
{
  "source": "00bcded4",
  "target": "00bcdee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcded8`](#insn-00bcded8)

~~~json
{
  "source": "00bcded8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdedc`](#insn-00bcdedc)

~~~json
{
  "source": "00bcdedc",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdee4`](#insn-00bcdee4)

~~~json
{
  "source": "00bcdee4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdeec`](#insn-00bcdeec)

~~~json
{
  "source": "00bcdeec",
  "target": "00bcdf18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdef4`](#insn-00bcdef4)

~~~json
{
  "source": "00bcdef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdef8`](#insn-00bcdef8)

~~~json
{
  "source": "00bcdef8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdefc`](#insn-00bcdefc)

~~~json
{
  "source": "00bcdefc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf0c`](#insn-00bcdf0c)

~~~json
{
  "source": "00bcdf0c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf10`](#insn-00bcdf10)

~~~json
{
  "source": "00bcdf10",
  "target": "00bcded8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf14`](#insn-00bcdf14)

~~~json
{
  "source": "00bcdf14",
  "target": "00bcdee0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdf18`](#insn-00bcdf18)

~~~json
{
  "source": "00bcdf18",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
