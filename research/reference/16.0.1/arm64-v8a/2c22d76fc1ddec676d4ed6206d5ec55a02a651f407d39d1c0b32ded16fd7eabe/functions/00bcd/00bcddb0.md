# 00bcddb0

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bcd988`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bcd/00bcd988.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-4e3424f4c433cb5bbf8f8710bd0184c1)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcde4c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcde4c.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0081.md#compare-7d41db8a9fb1a24b9cf08e1f91efceb4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcddb0",
  "name": "_ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_4Auth20FetchProvidersResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "39c2f139075666d80858e46632db1f8499c31054e40051280770c44b37e2d775",
  "source_text_sha256": "39c2f139075666d80858e46632db1f8499c31054e40051280770c44b37e2d775",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcddb0",
        "00bcde7f"
      ]
    ],
    "bytes_sha256": "c596b843774c60d49475cce23084e659a83ca1f11638c121fc23b0ba2cdbd417",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5dce0](../00c5d/00c5dce0.md)

## 呼び出し先

- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5dbd0](../00c5d/00c5dbd0.md)
- [00c5dd10](../00c5d/00c5dd10.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1752 bytes

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
  local_50 = 0;
  local_48 = (void *)0x0;
  local_58 = 0;
  iVar3 = _ZN8firebase4auth30CheckAndClearJniAuthExceptionsEP7_JNIEnvPNSt6__ndk112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEE
                    (param_1,&local_58);
  if (iVar3 == 0) {
    uVar4 = 0;
  }
  else {
                    /* try { // try from 00bcddf8 to 00ccddff has its CatchHandler @ 00bce8e0 */
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_68,param_3);
    pvVar1 = (void *)((ulong)&local_58 | 1);
    if ((local_58 & 1) != 0) {
      pvVar1 = local_48;
    }
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth4Auth20FetchProvidersResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS8_iSA_RKT0_
              (param_2,auStack_68,iVar3,pvVar1,auStack_40);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
    uVar4 = 1;
                    /* try { // try from 00bcde34 to 00ccde3b has its CatchHandler @ 00bce8d8 */
  }
  if ((local_58 & 1) != 0) {
    _ZdlPv(local_48);
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* try { // try from 00bcde68 to 00ccde87 has its CatchHandler @ 00bce8c8 */
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
<a id="insn-00bcddb0"></a> `00bcddb0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcddb4"></a> `00bcddb4` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcddb8"></a> `00bcddb8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcddbc"></a> `00bcddbc` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcddc0"></a> `00bcddc0` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcddc4"></a> `00bcddc4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcddc8"></a> `00bcddc8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcddcc"></a> `00bcddcc` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bcddd0"></a> `00bcddd0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcddd4"></a> `00bcddd4` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bcddd8"></a> `00bcddd8` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdddc"></a> `00bcdddc` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcdde0"></a> `00bcdde0` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdde4"></a> `00bcdde4` | `cb 3f 02 94` | bl 0x00c5dd10 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdde8"></a> `00bcdde8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bcddec"></a> `00bcddec` | `00 04 00 34` | cbz w0,0x00bcde6c | `CONDITIONAL_JUMP`
<a id="insn-00bcddf0"></a> `00bcddf0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcddf4"></a> `00bcddf4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcddf8"></a> `00bcddf8` | `02 34 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcddfc"></a> `00bcddfc` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcde00"></a> `00bcde00` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bcde04"></a> `00bcde04` | `ea 63 00 91` | add x10,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcde08"></a> `00bcde08` | `4a 01 40 b2` | orr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bcde0c"></a> `00bcde0c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcde10"></a> `00bcde10` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bcde14"></a> `00bcde14` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcde18"></a> `00bcde18` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bcde1c"></a> `00bcde1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcde20"></a> `00bcde20` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00bcde24"></a> `00bcde24` | `6b 3f 02 94` | bl 0x00c5dbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcde28"></a> `00bcde28` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcde2c"></a> `00bcde2c` | `19 33 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcde30"></a> `00bcde30` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00bcde34"></a> `00bcde34` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcde38"></a> `00bcde38` | `68 00 00 36` | tbz w8,#0x0,0x00bcde44 | `CONDITIONAL_JUMP`
<a id="insn-00bcde3c"></a> `00bcde3c` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bcde40"></a> `00bcde40` | `1c 28 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcde44"></a> `00bcde44` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcde48"></a> `00bcde48` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bcde4c"></a> `00bcde4c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcde50"></a> `00bcde50` | `61 01 00 54` | b.ne 0x00bcde7c | `CONDITIONAL_JUMP`
<a id="insn-00bcde54"></a> `00bcde54` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bcde58"></a> `00bcde58` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcde5c"></a> `00bcde5c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcde60"></a> `00bcde60` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcde64"></a> `00bcde64` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcde68"></a> `00bcde68` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcde6c"></a> `00bcde6c` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00bcde70"></a> `00bcde70` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcde74"></a> `00bcde74` | `48 fe 07 37` | tbnz w8,#0x0,0x00bcde3c | `CONDITIONAL_JUMP`
<a id="insn-00bcde78"></a> `00bcde78` | `f3 ff ff 17` | b 0x00bcde44 | `UNCONDITIONAL_JUMP`
<a id="insn-00bcde7c"></a> `00bcde7c` | `19 28 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcddb0`](#insn-00bcddb0) 範囲 `[['00bcddb0', '00bcddef']]`
  - `CONDITIONAL_JUMP` [`00bcddec`](#insn-00bcddec) → [`00bcde6c`](#insn-00bcde6c)
  - `FALL_THROUGH` [`00bcddec`](#insn-00bcddec) → [`00bcddf0`](#insn-00bcddf0)
- ブロック [`00bcddf0`](#insn-00bcddf0) 範囲 `[['00bcddf0', '00bcddf7']]`
  - `FALL_THROUGH` [`00bcddf4`](#insn-00bcddf4) → [`00bcddf8`](#insn-00bcddf8)
- ブロック [`00bcddf8`](#insn-00bcddf8) 範囲 `[['00bcddf8', '00bcde33']]`
  - `FALL_THROUGH` [`00bcde30`](#insn-00bcde30) → [`00bcde34`](#insn-00bcde34)
- ブロック [`00bcde34`](#insn-00bcde34) 範囲 `[['00bcde34', '00bcde3b']]`
  - `CONDITIONAL_JUMP` [`00bcde38`](#insn-00bcde38) → [`00bcde44`](#insn-00bcde44)
  - `FALL_THROUGH` [`00bcde38`](#insn-00bcde38) → [`00bcde3c`](#insn-00bcde3c)
- ブロック [`00bcde3c`](#insn-00bcde3c) 範囲 `[['00bcde3c', '00bcde43']]`
  - `FALL_THROUGH` [`00bcde40`](#insn-00bcde40) → [`00bcde44`](#insn-00bcde44)
- ブロック [`00bcde44`](#insn-00bcde44) 範囲 `[['00bcde44', '00bcde53']]`
  - `CONDITIONAL_JUMP` [`00bcde50`](#insn-00bcde50) → [`00bcde7c`](#insn-00bcde7c)
  - `FALL_THROUGH` [`00bcde50`](#insn-00bcde50) → [`00bcde54`](#insn-00bcde54)
- ブロック [`00bcde54`](#insn-00bcde54) 範囲 `[['00bcde54', '00bcde67']]`
  - `FALL_THROUGH` [`00bcde64`](#insn-00bcde64) → [`00bcde68`](#insn-00bcde68)
- ブロック [`00bcde68`](#insn-00bcde68) 範囲 `[['00bcde68', '00bcde6b']]`
- ブロック [`00bcde6c`](#insn-00bcde6c) 範囲 `[['00bcde6c', '00bcde77']]`
  - `CONDITIONAL_JUMP` [`00bcde74`](#insn-00bcde74) → [`00bcde3c`](#insn-00bcde3c)
  - `FALL_THROUGH` [`00bcde74`](#insn-00bcde74) → [`00bcde78`](#insn-00bcde78)
- ブロック [`00bcde78`](#insn-00bcde78) 範囲 `[['00bcde78', '00bcde7b']]`
  - `UNCONDITIONAL_JUMP` [`00bcde78`](#insn-00bcde78) → [`00bcde44`](#insn-00bcde44)
- ブロック [`00bcde7c`](#insn-00bcde7c) 範囲 `[['00bcde7c', '00bcde7f']]`

## 命令位置別の参照

- [`00bcddb4`](#insn-00bcddb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddb8`](#insn-00bcddb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddbc`](#insn-00bcddbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddd4`](#insn-00bcddd4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddd8`](#insn-00bcddd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdddc`](#insn-00bcdddc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdde4`](#insn-00bcdde4) → [`00c5dd10`](../00c5d/00c5dd10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dd10` · 推定シンボル `None` · 推定型 `None`
- [`00bcddec`](#insn-00bcddec) → [`00bcde6c`](#insn-00bcde6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddf8`](#insn-00bcddf8) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bcddfc`](#insn-00bcddfc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde00`](#insn-00bcde00) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde24`](#insn-00bcde24) → [`00c5dbd0`](../00c5d/00c5dbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dbd0` · 推定シンボル `None` · 推定型 `None`
- [`00bcde2c`](#insn-00bcde2c) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bcde34`](#insn-00bcde34) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde38`](#insn-00bcde38) → [`00bcde44`](#insn-00bcde44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde3c`](#insn-00bcde3c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde40`](#insn-00bcde40) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bcde48`](#insn-00bcde48) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde50`](#insn-00bcde50) → [`00bcde7c`](#insn-00bcde7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde58`](#insn-00bcde58) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde5c`](#insn-00bcde5c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde60`](#insn-00bcde60) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde70`](#insn-00bcde70) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde74`](#insn-00bcde74) → [`00bcde3c`](#insn-00bcde3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde78`](#insn-00bcde78) → [`00bcde44`](#insn-00bcde44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde7c`](#insn-00bcde7c) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcddb4`](#insn-00bcddb4)

~~~json
{
  "source": "00bcddb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddb8`](#insn-00bcddb8)

~~~json
{
  "source": "00bcddb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddbc`](#insn-00bcddbc)

~~~json
{
  "source": "00bcddbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddd4`](#insn-00bcddd4)

~~~json
{
  "source": "00bcddd4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddd8`](#insn-00bcddd8)

~~~json
{
  "source": "00bcddd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdddc`](#insn-00bcdddc)

~~~json
{
  "source": "00bcdddc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdde4`](#insn-00bcdde4)

~~~json
{
  "source": "00bcdde4",
  "target": "00c5dd10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcddec`](#insn-00bcddec)

~~~json
{
  "source": "00bcddec",
  "target": "00bcde6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddf8`](#insn-00bcddf8)

~~~json
{
  "source": "00bcddf8",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcddfc`](#insn-00bcddfc)

~~~json
{
  "source": "00bcddfc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde00`](#insn-00bcde00)

~~~json
{
  "source": "00bcde00",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde24`](#insn-00bcde24)

~~~json
{
  "source": "00bcde24",
  "target": "00c5dbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcde2c`](#insn-00bcde2c)

~~~json
{
  "source": "00bcde2c",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcde34`](#insn-00bcde34)

~~~json
{
  "source": "00bcde34",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde38`](#insn-00bcde38)

~~~json
{
  "source": "00bcde38",
  "target": "00bcde44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde3c`](#insn-00bcde3c)

~~~json
{
  "source": "00bcde3c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde40`](#insn-00bcde40)

~~~json
{
  "source": "00bcde40",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcde48`](#insn-00bcde48)

~~~json
{
  "source": "00bcde48",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde50`](#insn-00bcde50)

~~~json
{
  "source": "00bcde50",
  "target": "00bcde7c",
  "target_space": "ram",
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
- 参照命令 [`00bcde5c`](#insn-00bcde5c)

~~~json
{
  "source": "00bcde5c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde60`](#insn-00bcde60)

~~~json
{
  "source": "00bcde60",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde70`](#insn-00bcde70)

~~~json
{
  "source": "00bcde70",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde74`](#insn-00bcde74)

~~~json
{
  "source": "00bcde74",
  "target": "00bcde3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde78`](#insn-00bcde78)

~~~json
{
  "source": "00bcde78",
  "target": "00bcde44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde7c`](#insn-00bcde7c)

~~~json
{
  "source": "00bcde7c",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
