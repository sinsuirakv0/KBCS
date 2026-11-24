# 00bcdfb0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5eab0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5eab0.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0067.md#compare-ea9f495f397cdf341b7ce001427dff43)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bce3d8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce3d8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-e4df7074f01ea3a1d698474672c5ffdc)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdfb0",
  "name": "_ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE",
  "size": 208,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "4c8e2bc1df85ab6b767abf7249144127d2c4c1fe92afcc72a6bee778f1704d97",
  "source_text_sha256": "4c8e2bc1df85ab6b767abf7249144127d2c4c1fe92afcc72a6bee778f1704d97",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdfb0",
        "00bce07f"
      ]
    ],
    "bytes_sha256": "280cedb7f772db7eef61e41780774b6b4fe2a0099c8324122953b6d3d81066e9",
    "instruction_count": 52,
    "instruction_bytes": 208,
    "body_bytes": 208,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5d8d0](../00c5d/00c5d8d0.md)

## 呼び出し先

- [00c57ab0](../00c57/00c57ab0.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a690](../00c5a/00c5a690.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5d7c0](../00c5d/00c5d7c0.md)
- [00c5d910](../00c5d/00c5d910.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1819 bytes

~~~c

undefined8
_ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
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
  
                    /* try { // try from 00bcdfb8 to 00ccdfd3 has its CatchHandler @ 00bce694 */
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
                    /* try { // try from 00bcdfd4 to 00cce02f has its CatchHandler @ 00bcc3d4 */
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
    pvVar1 = (void *)((ulong)&local_58 | 1);
    if ((local_58 & 1) != 0) {
      pvVar1 = local_48;
    }
    _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalIvZNS0_16CompleteInternalINS_4auth10AuthResultEEEvRKNS_12FutureHandleEiPKcEUlPvE_EEvS7_iS9_RKT0_
              (param_2,auStack_68,iVar3,pvVar1,auStack_40);
    _ZN8firebase12FutureHandleD2Ev(auStack_68);
                    /* try { // try from 00bce030 to 00cce03f has its CatchHandler @ 00bce744 */
    uVar4 = 1;
  }
  if ((local_58 & 1) != 0) {
                    /* try { // try from 00bce040 to 00cce95f has its CatchHandler @ 00bcc3d4 */
    _ZdlPv(local_48);
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
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
<a id="insn-00bcdfb0"></a> `00bcdfb0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcdfb4"></a> `00bcdfb4` | `f6 57 04 a9` | stp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcdfb8"></a> `00bcdfb8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcdfbc"></a> `00bcdfbc` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcdfc0"></a> `00bcdfc0` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00bcdfc4"></a> `00bcdfc4` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcdfc8"></a> `00bcdfc8` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdfcc"></a> `00bcdfcc` | `f5 03 02 aa` | mov x21,x2 | `FALL_THROUGH`
<a id="insn-00bcdfd0"></a> `00bcdfd0` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bcdfd4"></a> `00bcdfd4` | `a8 83 1d f8` | stur x8,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bcdfd8"></a> `00bcdfd8` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bcdfdc"></a> `00bcdfdc` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bcdfe0"></a> `00bcdfe0` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdfe4"></a> `00bcdfe4` | `4b 3e 02 94` | bl 0x00c5d910 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdfe8"></a> `00bcdfe8` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bcdfec"></a> `00bcdfec` | `00 04 00 34` | cbz w0,0x00bce06c | `CONDITIONAL_JUMP`
<a id="insn-00bcdff0"></a> `00bcdff0` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdff4"></a> `00bcdff4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bcdff8"></a> `00bcdff8` | `82 32 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdffc"></a> `00bcdffc` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bce000"></a> `00bce000` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bce004"></a> `00bce004` | `ea 63 00 91` | add x10,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bce008"></a> `00bce008` | `4a 01 40 b2` | orr x10,x10,#0x1 | `FALL_THROUGH`
<a id="insn-00bce00c"></a> `00bce00c` | `1f 01 00 72` | tst w8,#0x1 | `FALL_THROUGH`
<a id="insn-00bce010"></a> `00bce010` | `43 01 89 9a` | csel x3,x10,x9,eq | `FALL_THROUGH`
<a id="insn-00bce014"></a> `00bce014` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bce018"></a> `00bce018` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bce01c"></a> `00bce01c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce020"></a> `00bce020` | `e2 03 14 2a` | mov w2,w20 | `FALL_THROUGH`
<a id="insn-00bce024"></a> `00bce024` | `e7 3d 02 94` | bl 0x00c5d7c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce028"></a> `00bce028` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bce02c"></a> `00bce02c` | `99 31 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bce030"></a> `00bce030` | `33 00 80 52` | mov w19,#0x1 | `FALL_THROUGH`
<a id="insn-00bce034"></a> `00bce034` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bce038"></a> `00bce038` | `68 00 00 36` | tbz w8,#0x0,0x00bce044 | `CONDITIONAL_JUMP`
<a id="insn-00bce03c"></a> `00bce03c` | `e0 17 40 f9` | ldr x0,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bce040"></a> `00bce040` | `9c 26 02 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce044"></a> `00bce044` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-00bce048"></a> `00bce048` | `a9 83 5d f8` | ldur x9,[x29, #-0x28] | `FALL_THROUGH`
<a id="insn-00bce04c"></a> `00bce04c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bce050"></a> `00bce050` | `61 01 00 54` | b.ne 0x00bce07c | `CONDITIONAL_JUMP`
<a id="insn-00bce054"></a> `00bce054` | `e0 03 13 2a` | mov w0,w19 | `FALL_THROUGH`
<a id="insn-00bce058"></a> `00bce058` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bce05c"></a> `00bce05c` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bce060"></a> `00bce060` | `f6 57 44 a9` | ldp x22,x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bce064"></a> `00bce064` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bce068"></a> `00bce068` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bce06c"></a> `00bce06c` | `f3 03 1f 2a` | mov w19,wzr | `FALL_THROUGH`
<a id="insn-00bce070"></a> `00bce070` | `e8 63 40 39` | ldrb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bce074"></a> `00bce074` | `48 fe 07 37` | tbnz w8,#0x0,0x00bce03c | `CONDITIONAL_JUMP`
<a id="insn-00bce078"></a> `00bce078` | `f3 ff ff 17` | b 0x00bce044 | `UNCONDITIONAL_JUMP`
<a id="insn-00bce07c"></a> `00bce07c` | `99 26 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdfb0`](#insn-00bcdfb0) 範囲 `[['00bcdfb0', '00bcdfb7']]`
  - `FALL_THROUGH` [`00bcdfb4`](#insn-00bcdfb4) → [`00bcdfb8`](#insn-00bcdfb8)
- ブロック [`00bcdfb8`](#insn-00bcdfb8) 範囲 `[['00bcdfb8', '00bcdfd3']]`
  - `FALL_THROUGH` [`00bcdfd0`](#insn-00bcdfd0) → [`00bcdfd4`](#insn-00bcdfd4)
- ブロック [`00bcdfd4`](#insn-00bcdfd4) 範囲 `[['00bcdfd4', '00bcdfef']]`
  - `CONDITIONAL_JUMP` [`00bcdfec`](#insn-00bcdfec) → [`00bce06c`](#insn-00bce06c)
  - `FALL_THROUGH` [`00bcdfec`](#insn-00bcdfec) → [`00bcdff0`](#insn-00bcdff0)
- ブロック [`00bcdff0`](#insn-00bcdff0) 範囲 `[['00bcdff0', '00bce02f']]`
  - `FALL_THROUGH` [`00bce02c`](#insn-00bce02c) → [`00bce030`](#insn-00bce030)
- ブロック [`00bce030`](#insn-00bce030) 範囲 `[['00bce030', '00bce03b']]`
  - `CONDITIONAL_JUMP` [`00bce038`](#insn-00bce038) → [`00bce044`](#insn-00bce044)
  - `FALL_THROUGH` [`00bce038`](#insn-00bce038) → [`00bce03c`](#insn-00bce03c)
- ブロック [`00bce03c`](#insn-00bce03c) 範囲 `[['00bce03c', '00bce03f']]`
  - `FALL_THROUGH` [`00bce03c`](#insn-00bce03c) → [`00bce040`](#insn-00bce040)
- ブロック [`00bce040`](#insn-00bce040) 範囲 `[['00bce040', '00bce043']]`
  - `FALL_THROUGH` [`00bce040`](#insn-00bce040) → [`00bce044`](#insn-00bce044)
- ブロック [`00bce044`](#insn-00bce044) 範囲 `[['00bce044', '00bce053']]`
  - `CONDITIONAL_JUMP` [`00bce050`](#insn-00bce050) → [`00bce07c`](#insn-00bce07c)
  - `FALL_THROUGH` [`00bce050`](#insn-00bce050) → [`00bce054`](#insn-00bce054)
- ブロック [`00bce054`](#insn-00bce054) 範囲 `[['00bce054', '00bce06b']]`
- ブロック [`00bce06c`](#insn-00bce06c) 範囲 `[['00bce06c', '00bce077']]`
  - `CONDITIONAL_JUMP` [`00bce074`](#insn-00bce074) → [`00bce03c`](#insn-00bce03c)
  - `FALL_THROUGH` [`00bce074`](#insn-00bce074) → [`00bce078`](#insn-00bce078)
- ブロック [`00bce078`](#insn-00bce078) 範囲 `[['00bce078', '00bce07b']]`
  - `UNCONDITIONAL_JUMP` [`00bce078`](#insn-00bce078) → [`00bce044`](#insn-00bce044)
- ブロック [`00bce07c`](#insn-00bce07c) 範囲 `[['00bce07c', '00bce07f']]`

## 命令位置別の参照

- [`00bcdfb4`](#insn-00bcdfb4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfb8`](#insn-00bcdfb8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfbc`](#insn-00bcdfbc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfd4`](#insn-00bcdfd4) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfd8`](#insn-00bcdfd8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfdc`](#insn-00bcdfdc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfe4`](#insn-00bcdfe4) → [`00c5d910`](../00c5d/00c5d910.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d910` · 推定シンボル `None` · 推定型 `None`
- [`00bcdfec`](#insn-00bcdfec) → [`00bce06c`](#insn-00bce06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdff8`](#insn-00bcdff8) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcdffc`](#insn-00bcdffc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce000`](#insn-00bce000) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce024`](#insn-00bce024) → [`00c5d7c0`](../00c5d/00c5d7c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d7c0` · 推定シンボル `None` · 推定型 `None`
- [`00bce02c`](#insn-00bce02c) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bce034`](#insn-00bce034) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce038`](#insn-00bce038) → [`00bce044`](#insn-00bce044) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce03c`](#insn-00bce03c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce040`](#insn-00bce040) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00bce048`](#insn-00bce048) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce050`](#insn-00bce050) → [`00bce07c`](#insn-00bce07c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce058`](#insn-00bce058) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce05c`](#insn-00bce05c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce060`](#insn-00bce060) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce070`](#insn-00bce070) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce074`](#insn-00bce074) → [`00bce03c`](#insn-00bce03c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce078`](#insn-00bce078) → [`00bce044`](#insn-00bce044) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce07c`](#insn-00bce07c) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdfb4`](#insn-00bcdfb4)

~~~json
{
  "source": "00bcdfb4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfb8`](#insn-00bcdfb8)

~~~json
{
  "source": "00bcdfb8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfbc`](#insn-00bcdfbc)

~~~json
{
  "source": "00bcdfbc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfd4`](#insn-00bcdfd4)

~~~json
{
  "source": "00bcdfd4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfd8`](#insn-00bcdfd8)

~~~json
{
  "source": "00bcdfd8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfdc`](#insn-00bcdfdc)

~~~json
{
  "source": "00bcdfdc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdfe4`](#insn-00bcdfe4)

~~~json
{
  "source": "00bcdfe4",
  "target": "00c5d910",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdfec`](#insn-00bcdfec)

~~~json
{
  "source": "00bcdfec",
  "target": "00bce06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdff8`](#insn-00bcdff8)

~~~json
{
  "source": "00bcdff8",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdffc`](#insn-00bcdffc)

~~~json
{
  "source": "00bcdffc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce000`](#insn-00bce000)

~~~json
{
  "source": "00bce000",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce024`](#insn-00bce024)

~~~json
{
  "source": "00bce024",
  "target": "00c5d7c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce02c`](#insn-00bce02c)

~~~json
{
  "source": "00bce02c",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce034`](#insn-00bce034)

~~~json
{
  "source": "00bce034",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce038`](#insn-00bce038)

~~~json
{
  "source": "00bce038",
  "target": "00bce044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce03c`](#insn-00bce03c)

~~~json
{
  "source": "00bce03c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce040`](#insn-00bce040)

~~~json
{
  "source": "00bce040",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce048`](#insn-00bce048)

~~~json
{
  "source": "00bce048",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce050`](#insn-00bce050)

~~~json
{
  "source": "00bce050",
  "target": "00bce07c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce058`](#insn-00bce058)

~~~json
{
  "source": "00bce058",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce05c`](#insn-00bce05c)

~~~json
{
  "source": "00bce05c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce060`](#insn-00bce060)

~~~json
{
  "source": "00bce060",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce070`](#insn-00bce070)

~~~json
{
  "source": "00bce070",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce074`](#insn-00bce074)

~~~json
{
  "source": "00bce074",
  "target": "00bce03c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce078`](#insn-00bce078)

~~~json
{
  "source": "00bce078",
  "target": "00bce044",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce07c`](#insn-00bce07c)

~~~json
{
  "source": "00bce07c",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
