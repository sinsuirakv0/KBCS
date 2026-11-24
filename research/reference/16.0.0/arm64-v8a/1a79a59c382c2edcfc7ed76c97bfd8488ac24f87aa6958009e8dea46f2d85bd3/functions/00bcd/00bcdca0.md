# 00bcdca0

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00b5e7a0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00b5e/00b5e7a0.md) · 移動量 `+0x6f500`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0066.md#compare-0a272a24c55d312982ee81c219dc5d4e)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bce0c8`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bce/00bce0c8.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0081.md#compare-1fd60fa9520c978cd1f8804fa4da8ef2)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bcdca0",
  "name": "_ZN8firebase4auth4Auth21SignInWithCustomTokenEPKc",
  "size": 392,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "59e331db3b4be4963a2e5ef2716e24b50b42264189db1e3abdc433fc045c4a2b",
  "source_text_sha256": "59e331db3b4be4963a2e5ef2716e24b50b42264189db1e3abdc433fc045c4a2b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bcdca0",
        "00bcde27"
      ]
    ],
    "bytes_sha256": "dc69967d22767838cbd5adf809fb7ceaf569ad7749fe41c7cd306065226e02a5",
    "instruction_count": 98,
    "instruction_bytes": 392,
    "body_bytes": 392,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004977f4](../00497/004977f4.md)
- [00c57a90](../00c57/00c57a90.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c5a690](../00c5a/00c5a690.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5ab40](../00c5a/00c5ab40.md)
- [00c5ac80](../00c5a/00c5ac80.md)
- [00c5d800](../00c5d/00c5d800.md)
- [00c5d8d0](../00c5d/00c5d8d0.md)
- [00c5d930](../00c5d/00c5d930.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2899 bytes

~~~c

void _ZN8firebase4auth4Auth21SignInWithCustomTokenEPKc
               (undefined8 param_1,long *param_2,undefined8 param_3)

{
  long lVar1;
  long lVar2;
  undefined *puVar3;
  long *plVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  ulong uVar7;
  long lVar8;
  long lVar9;
  undefined8 *puVar10;
  undefined1 auStack_78 [16];
  undefined1 auStack_68 [16];
  long local_58;
  
                    /* try { // try from 00bcdcb8 to 00ccdd4b has its CatchHandler @ 00bcc3d4 */
  lVar2 = tpidr_el0;
  local_58 = *(long *)(lVar2 + 0x28);
  lVar1 = *param_2 + 0x10;
  _ZN8firebase26ReferenceCountedFutureImpl9SafeAllocINS_4auth10AuthResultEEENS_16SafeFutureHandleIT_EEi
            (auStack_68,lVar1,1);
  plVar4 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*(undefined8 *)*param_2);
  uVar5 = (**(code **)(*plVar4 + 0x538))(plVar4,param_3);
  uVar6 = FUN_004977f4(plVar4,*(undefined8 *)(*param_2 + 0x1f8),DAT_01126398,uVar5);
  (**(code **)(*plVar4 + 0xb8))(plVar4,uVar5);
                    /* try { // try from 00bcdd4c to 00ccdd53 has its CatchHandler @ 00bce6b4 */
  uVar7 = _ZN8firebase4auth29CheckAndCompleteFutureOnErrorINS0_10AuthResultEEEbP7_JNIEnvPNS_26ReferenceCountedFutureImplERKNS_16SafeFutureHandleIT_EE
                    (plVar4,lVar1,auStack_68);
  if ((uVar7 & 1) == 0) {
    _ZN8firebase12FutureHandleC1ERKS0_(auStack_78,auStack_68);
    puVar10 = (undefined8 *)*param_2;
    uVar5 = _ZNK8firebase3App9GetJNIEnvEv(*puVar10);
    lVar8 = _Znwm(0x20);
                    /* try { // try from 00bcdd7c to 00ccdd93 has its CatchHandler @ 00bce6b0 */
    _ZN8firebase12FutureHandleC1ERKS0_(lVar8,auStack_78);
    puVar3 = 
    PTR__ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv_00c9b620
    ;
    *(undefined8 **)(lVar8 + 0x10) = puVar10;
    *(undefined **)(lVar8 + 0x18) = puVar3;
    if ((*(byte *)(puVar10 + 0x28) & 1) == 0) {
      lVar9 = (long)puVar10 + 0x141;
                    /* try { // try from 00bcdda4 to 00ccddc3 has its CatchHandler @ 00bce6ac */
    }
    else {
      lVar9 = puVar10[0x2a];
    }
    _ZN8firebase4util22RegisterCallbackOnTaskEP7_JNIEnvP8_jobjectPFvS2_S4_NS0_12FutureResultEPKcPvES8_S7_
              (uVar5,uVar6,
               PTR__ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv_00c9b600
               ,lVar8,lVar9);
                    /* try { // try from 00bcddc4 to 00ccde7b has its CatchHandler @ 00bcc3d4 */
    _ZN8firebase12FutureHandleD2Ev(auStack_78);
    (**(code **)(*plVar4 + 0xb8))(plVar4,uVar6);
  }
  _ZN8firebase6FutureINS_4auth10AuthResultEEC2EPNS_6detail18FutureApiInterfaceERKNS_12FutureHandleE
            (param_1,lVar1,auStack_68);
  _ZN8firebase12FutureHandleD2Ev(auStack_68);
  if (*(long *)(lVar2 + 0x28) == local_58) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bcdca0"></a> `00bcdca0` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcdca4"></a> `00bcdca4` | `fa 67 03 a9` | stp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcdca8"></a> `00bcdca8` | `f8 5f 04 a9` | stp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcdcac"></a> `00bcdcac` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcdcb0"></a> `00bcdcb0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcdcb4"></a> `00bcdcb4` | `fd 7b 07 a9` | stp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcdcb8"></a> `00bcdcb8` | `fd c3 01 91` | add x29,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bcdcbc"></a> `00bcdcbc` | `59 d0 3b d5` | mrs x25,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bcdcc0"></a> `00bcdcc0` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bcdcc4"></a> `00bcdcc4` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdcc8"></a> `00bcdcc8` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bcdccc"></a> `00bcdccc` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcdcd0"></a> `00bcdcd0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdcd4"></a> `00bcdcd4` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bcdcd8"></a> `00bcdcd8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcdcdc"></a> `00bcdcdc` | `14 41 00 91` | add x20,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00bcdce0"></a> `00bcdce0` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdce4"></a> `00bcdce4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bcdce8"></a> `00bcdce8` | `c6 3e 02 94` | bl 0x00c5d800 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdcec"></a> `00bcdcec` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bcdcf0"></a> `00bcdcf0` | `00 01 40 f9` | ldr x0,[x8] | `FALL_THROUGH`
<a id="insn-00bcdcf4"></a> `00bcdcf4` | `e3 33 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdcf8"></a> `00bcdcf8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bcdcfc"></a> `00bcdcfc` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bcdd00"></a> `00bcdd00` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bcdd04"></a> `00bcdd04` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcdd08"></a> `00bcdd08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdd0c"></a> `00bcdd0c` | `e8 02 40 f9` | ldr x8,[x23] | `FALL_THROUGH`
<a id="insn-00bcdd10"></a> `00bcdd10` | `c9 2a 00 b0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bcdd14"></a> `00bcdd14` | `22 cd 41 f9` | ldr x2,[x9, #0x398] | `FALL_THROUGH`
<a id="insn-00bcdd18"></a> `00bcdd18` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcdd1c"></a> `00bcdd1c` | `01 fd 40 f9` | ldr x1,[x8, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bcdd20"></a> `00bcdd20` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcdd24"></a> `00bcdd24` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bcdd28"></a> `00bcdd28` | `b3 26 e3 97` | bl 0x004977f4 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd2c"></a> `00bcdd2c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcdd30"></a> `00bcdd30` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bcdd34"></a> `00bcdd34` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcdd38"></a> `00bcdd38` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcdd3c"></a> `00bcdd3c` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bcdd40"></a> `00bcdd40` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdd44"></a> `00bcdd44` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdd48"></a> `00bcdd48` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcdd4c"></a> `00bcdd4c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcdd50"></a> `00bcdd50` | `e0 3e 02 94` | bl 0x00c5d8d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd54"></a> `00bcdd54` | `60 04 00 37` | tbnz w0,#0x0,0x00bcdde0 | `CONDITIONAL_JUMP`
<a id="insn-00bcdd58"></a> `00bcdd58` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdd5c"></a> `00bcdd5c` | `e1 63 00 91` | add x1,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdd60"></a> `00bcdd60` | `28 33 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd64"></a> `00bcdd64` | `fa 02 40 f9` | ldr x26,[x23] | `FALL_THROUGH`
<a id="insn-00bcdd68"></a> `00bcdd68` | `40 03 40 f9` | ldr x0,[x26] | `FALL_THROUGH`
<a id="insn-00bcdd6c"></a> `00bcdd6c` | `c5 33 02 94` | bl 0x00c5ac80 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd70"></a> `00bcdd70` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bcdd74"></a> `00bcdd74` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00bcdd78"></a> `00bcdd78` | `46 27 02 94` | bl 0x00c57a90 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd7c"></a> `00bcdd7c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bcdd80"></a> `00bcdd80` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcdd84"></a> `00bcdd84` | `1f 33 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bcdd88"></a> `00bcdd88` | `68 06 00 d0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcdd8c"></a> `00bcdd8c` | `08 11 43 f9` | ldr x8,[x8, #0x620] | `FALL_THROUGH`
<a id="insn-00bcdd90"></a> `00bcdd90` | `1a 23 01 a9` | stp x26,x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00bcdd94"></a> `00bcdd94` | `48 03 45 39` | ldrb w8,[x26, #0x140] | `FALL_THROUGH`
<a id="insn-00bcdd98"></a> `00bcdd98` | `88 00 00 37` | tbnz w8,#0x0,0x00bcdda8 | `CONDITIONAL_JUMP`
<a id="insn-00bcdd9c"></a> `00bcdd9c` | `48 03 05 91` | add x8,x26,#0x140 | `FALL_THROUGH`
<a id="insn-00bcdda0"></a> `00bcdda0` | `04 05 00 91` | add x4,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bcdda4"></a> `00bcdda4` | `02 00 00 14` | b 0x00bcddac | `UNCONDITIONAL_JUMP`
<a id="insn-00bcdda8"></a> `00bcdda8` | `44 ab 40 f9` | ldr x4,[x26, #0x150] | `FALL_THROUGH`
<a id="insn-00bcddac"></a> `00bcddac` | `62 06 00 d0` | adrp x2,0xc9b000 | `FALL_THROUGH`
<a id="insn-00bcddb0"></a> `00bcddb0` | `42 00 43 f9` | ldr x2,[x2, #0x600] | `FALL_THROUGH`
<a id="insn-00bcddb4"></a> `00bcddb4` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bcddb8"></a> `00bcddb8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcddbc"></a> `00bcddbc` | `e3 03 18 aa` | mov x3,x24 | `FALL_THROUGH`
<a id="insn-00bcddc0"></a> `00bcddc0` | `60 33 02 94` | bl 0x00c5ab40 | `UNCONDITIONAL_CALL`
<a id="insn-00bcddc4"></a> `00bcddc4` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bcddc8"></a> `00bcddc8` | `32 32 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bcddcc"></a> `00bcddcc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bcddd0"></a> `00bcddd0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bcddd4"></a> `00bcddd4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bcddd8"></a> `00bcddd8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bcdddc"></a> `00bcdddc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bcdde0"></a> `00bcdde0` | `e2 63 00 91` | add x2,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcdde4"></a> `00bcdde4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bcdde8"></a> `00bcdde8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bcddec"></a> `00bcddec` | `d1 3e 02 94` | bl 0x00c5d930 | `UNCONDITIONAL_CALL`
<a id="insn-00bcddf0"></a> `00bcddf0` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bcddf4"></a> `00bcddf4` | `27 32 02 94` | bl 0x00c5a690 | `UNCONDITIONAL_CALL`
<a id="insn-00bcddf8"></a> `00bcddf8` | `28 17 40 f9` | ldr x8,[x25, #0x28] | `FALL_THROUGH`
<a id="insn-00bcddfc"></a> `00bcddfc` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bcde00"></a> `00bcde00` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bcde04"></a> `00bcde04` | `01 01 00 54` | b.ne 0x00bcde24 | `CONDITIONAL_JUMP`
<a id="insn-00bcde08"></a> `00bcde08` | `fd 7b 47 a9` | ldp x29,x30,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bcde0c"></a> `00bcde0c` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bcde10"></a> `00bcde10` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bcde14"></a> `00bcde14` | `f8 5f 44 a9` | ldp x24,x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bcde18"></a> `00bcde18` | `fa 67 43 a9` | ldp x26,x25,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bcde1c"></a> `00bcde1c` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00bcde20"></a> `00bcde20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bcde24"></a> `00bcde24` | `2f 27 02 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bcdca0`](#insn-00bcdca0) 範囲 `[['00bcdca0', '00bcdcb7']]`
  - `FALL_THROUGH` [`00bcdcb4`](#insn-00bcdcb4) → [`00bcdcb8`](#insn-00bcdcb8)
- ブロック [`00bcdcb8`](#insn-00bcdcb8) 範囲 `[['00bcdcb8', '00bcdd4b']]`
  - `FALL_THROUGH` [`00bcdd48`](#insn-00bcdd48) → [`00bcdd4c`](#insn-00bcdd4c)
- ブロック [`00bcdd4c`](#insn-00bcdd4c) 範囲 `[['00bcdd4c', '00bcdd57']]`
  - `CONDITIONAL_JUMP` [`00bcdd54`](#insn-00bcdd54) → [`00bcdde0`](#insn-00bcdde0)
  - `FALL_THROUGH` [`00bcdd54`](#insn-00bcdd54) → [`00bcdd58`](#insn-00bcdd58)
- ブロック [`00bcdd58`](#insn-00bcdd58) 範囲 `[['00bcdd58', '00bcdd7b']]`
  - `FALL_THROUGH` [`00bcdd78`](#insn-00bcdd78) → [`00bcdd7c`](#insn-00bcdd7c)
- ブロック [`00bcdd7c`](#insn-00bcdd7c) 範囲 `[['00bcdd7c', '00bcdd9b']]`
  - `CONDITIONAL_JUMP` [`00bcdd98`](#insn-00bcdd98) → [`00bcdda8`](#insn-00bcdda8)
  - `FALL_THROUGH` [`00bcdd98`](#insn-00bcdd98) → [`00bcdd9c`](#insn-00bcdd9c)
- ブロック [`00bcdd9c`](#insn-00bcdd9c) 範囲 `[['00bcdd9c', '00bcdda3']]`
  - `FALL_THROUGH` [`00bcdda0`](#insn-00bcdda0) → [`00bcdda4`](#insn-00bcdda4)
- ブロック [`00bcdda4`](#insn-00bcdda4) 範囲 `[['00bcdda4', '00bcdda7']]`
  - `UNCONDITIONAL_JUMP` [`00bcdda4`](#insn-00bcdda4) → [`00bcddac`](#insn-00bcddac)
- ブロック [`00bcdda8`](#insn-00bcdda8) 範囲 `[['00bcdda8', '00bcddab']]`
  - `FALL_THROUGH` [`00bcdda8`](#insn-00bcdda8) → [`00bcddac`](#insn-00bcddac)
- ブロック [`00bcddac`](#insn-00bcddac) 範囲 `[['00bcddac', '00bcddc3']]`
  - `FALL_THROUGH` [`00bcddc0`](#insn-00bcddc0) → [`00bcddc4`](#insn-00bcddc4)
- ブロック [`00bcddc4`](#insn-00bcddc4) 範囲 `[['00bcddc4', '00bcdddf']]`
  - `FALL_THROUGH` [`00bcdddc`](#insn-00bcdddc) → [`00bcdde0`](#insn-00bcdde0)
- ブロック [`00bcdde0`](#insn-00bcdde0) 範囲 `[['00bcdde0', '00bcde07']]`
  - `CONDITIONAL_JUMP` [`00bcde04`](#insn-00bcde04) → [`00bcde24`](#insn-00bcde24)
  - `FALL_THROUGH` [`00bcde04`](#insn-00bcde04) → [`00bcde08`](#insn-00bcde08)
- ブロック [`00bcde08`](#insn-00bcde08) 範囲 `[['00bcde08', '00bcde23']]`
- ブロック [`00bcde24`](#insn-00bcde24) 範囲 `[['00bcde24', '00bcde27']]`

## 命令位置別の参照

- [`00bcdca4`](#insn-00bcdca4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdca8`](#insn-00bcdca8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcac`](#insn-00bcdcac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcb0`](#insn-00bcdcb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcb4`](#insn-00bcdcb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcd4`](#insn-00bcdcd4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdce8`](#insn-00bcdce8) → [`00c5d800`](../00c5d/00c5d800.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d800` · 推定シンボル `None` · 推定型 `None`
- [`00bcdcf4`](#insn-00bcdcf4) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd14`](#insn-00bcdd14) → `01126398`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bcdd28`](#insn-00bcdd28) → [`004977f4`](../00497/004977f4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004977f4` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd50`](#insn-00bcdd50) → [`00c5d8d0`](../00c5d/00c5d8d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d8d0` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd54`](#insn-00bcdd54) → [`00bcdde0`](#insn-00bcdde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd60`](#insn-00bcdd60) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd6c`](#insn-00bcdd6c) → [`00c5ac80`](../00c5a/00c5ac80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac80` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd78`](#insn-00bcdd78) → [`00c57a90`](../00c57/00c57a90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a90` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd84`](#insn-00bcdd84) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bcdd8c`](#insn-00bcdd8c) → `00c9b620`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcdd90`](#insn-00bcdd90) → [`00bd4404`](../00bd4/00bd4404.md) · `DATA` · `ANALYSIS` · 関数 `00bd4404` · 推定シンボル `_ZN8firebase4auth14ReadAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_10AuthResultEEEbPv` · 推定型 `None`
- [`00bcdd98`](#insn-00bcdd98) → [`00bcdda8`](#insn-00bcdda8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcdda4`](#insn-00bcdda4) → [`00bcddac`](#insn-00bcddac) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcddb0`](#insn-00bcddb0) → `00c9b600`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bcddb0`](#insn-00bcddb0) → [`00bcf91c`](../00bcf/00bcf91c.md) · `PARAM` · `ANALYSIS` · 関数 `00bcf91c` · 推定シンボル `_ZN8firebase4auth14FutureCallbackINS0_10AuthResultEEEvP7_JNIEnvP8_jobjectNS_4util12FutureResultEPKcPv` · 推定型 `None`
- [`00bcddc0`](#insn-00bcddc0) → [`00c5ab40`](../00c5a/00c5ab40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ab40` · 推定シンボル `None` · 推定型 `None`
- [`00bcddc8`](#insn-00bcddc8) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bcddec`](#insn-00bcddec) → [`00c5d930`](../00c5d/00c5d930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d930` · 推定シンボル `None` · 推定型 `None`
- [`00bcddf4`](#insn-00bcddf4) → [`00c5a690`](../00c5a/00c5a690.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a690` · 推定シンボル `None` · 推定型 `None`
- [`00bcddfc`](#insn-00bcddfc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde04`](#insn-00bcde04) → [`00bcde24`](#insn-00bcde24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde08`](#insn-00bcde08) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde0c`](#insn-00bcde0c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde10`](#insn-00bcde10) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde14`](#insn-00bcde14) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde18`](#insn-00bcde18) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bcde24`](#insn-00bcde24) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bcdca4`](#insn-00bcdca4)

~~~json
{
  "source": "00bcdca4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdca8`](#insn-00bcdca8)

~~~json
{
  "source": "00bcdca8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdcac`](#insn-00bcdcac)

~~~json
{
  "source": "00bcdcac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdcb0`](#insn-00bcdcb0)

~~~json
{
  "source": "00bcdcb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdcb4`](#insn-00bcdcb4)

~~~json
{
  "source": "00bcdcb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdcd4`](#insn-00bcdcd4)

~~~json
{
  "source": "00bcdcd4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdce8`](#insn-00bcdce8)

~~~json
{
  "source": "00bcdce8",
  "target": "00c5d800",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdcf4`](#insn-00bcdcf4)

~~~json
{
  "source": "00bcdcf4",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd14`](#insn-00bcdd14)

~~~json
{
  "source": "00bcdd14",
  "target": "01126398",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126398",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bcdd28`](#insn-00bcdd28)

~~~json
{
  "source": "00bcdd28",
  "target": "004977f4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd50`](#insn-00bcdd50)

~~~json
{
  "source": "00bcdd50",
  "target": "00c5d8d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd54`](#insn-00bcdd54)

~~~json
{
  "source": "00bcdd54",
  "target": "00bcdde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdd60`](#insn-00bcdd60)

~~~json
{
  "source": "00bcdd60",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd6c`](#insn-00bcdd6c)

~~~json
{
  "source": "00bcdd6c",
  "target": "00c5ac80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd78`](#insn-00bcdd78)

~~~json
{
  "source": "00bcdd78",
  "target": "00c57a90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd84`](#insn-00bcdd84)

~~~json
{
  "source": "00bcdd84",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd8c`](#insn-00bcdd8c)

~~~json
{
  "source": "00bcdd8c",
  "target": "00c9b620",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b620",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcdd90`](#insn-00bcdd90)

~~~json
{
  "source": "00bcdd90",
  "target": "00bd4404",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcdd98`](#insn-00bcdd98)

~~~json
{
  "source": "00bcdd98",
  "target": "00bcdda8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcdda4`](#insn-00bcdda4)

~~~json
{
  "source": "00bcdda4",
  "target": "00bcddac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcddb0`](#insn-00bcddb0)

~~~json
{
  "source": "00bcddb0",
  "target": "00c9b600",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b600",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bcddb0`](#insn-00bcddb0)

~~~json
{
  "source": "00bcddb0",
  "target": "00bcf91c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcddc0`](#insn-00bcddc0)

~~~json
{
  "source": "00bcddc0",
  "target": "00c5ab40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcddc8`](#insn-00bcddc8)

~~~json
{
  "source": "00bcddc8",
  "target": "00c5a690",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcddec`](#insn-00bcddec)

~~~json
{
  "source": "00bcddec",
  "target": "00c5d930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bcddf4`](#insn-00bcddf4)

~~~json
{
  "source": "00bcddf4",
  "target": "00c5a690",
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
- 参照命令 [`00bcde04`](#insn-00bcde04)

~~~json
{
  "source": "00bcde04",
  "target": "00bcde24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde08`](#insn-00bcde08)

~~~json
{
  "source": "00bcde08",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde0c`](#insn-00bcde0c)

~~~json
{
  "source": "00bcde0c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde10`](#insn-00bcde10)

~~~json
{
  "source": "00bcde10",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde14`](#insn-00bcde14)

~~~json
{
  "source": "00bcde14",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde18`](#insn-00bcde18)

~~~json
{
  "source": "00bcde18",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bcde24`](#insn-00bcde24)

~~~json
{
  "source": "00bcde24",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
