# 00bbcab4

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bbc68c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bbc/00bbc68c.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0079.md#compare-41ec7ea1c1df28c7f5a5aa43e5080e71)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bbcb50`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bbc/00bbcb50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0079.md#compare-39a10b2848cc68153a76d1cce5b7f345)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bbcab4",
  "name": "FUN_00bbcab4",
  "size": 592,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "350cb53bad5dcbc3c2495683574a8cf1a746d387ae68f396988f4bf2ba7ff1ea",
  "source_text_sha256": "350cb53bad5dcbc3c2495683574a8cf1a746d387ae68f396988f4bf2ba7ff1ea",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bbcab4",
        "00bbccd3"
      ],
      [
        "00bbcce8",
        "00bbccf3"
      ],
      [
        "00bbcd14",
        "00bbcd37"
      ]
    ],
    "bytes_sha256": "9f841455e0271cdbc6acac0ec3299b58ccb1b31a7dd2ad0bd560bbee2e4d0590",
    "instruction_count": 148,
    "instruction_bytes": 592,
    "body_bytes": 592,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c53f5c](../00c53/00c53f5c.md)
- [00c57e90](../00c57/00c57e90.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c58000](../00c58/00c58000.md)
- [00c5aa00](../00c5a/00c5aa00.md)
- [00c5aa10](../00c5a/00c5aa10.md)
- [00c5aa90](../00c5a/00c5aa90.md)
- [00c5ad60](../00c5a/00c5ad60.md)
- [00c5ade0](../00c5a/00c5ade0.md)
- [00c5ae00](../00c5a/00c5ae00.md)
- [00c5b090](../00c5b/00c5b090.md)
- [00c5b390](../00c5b/00c5b390.md)
- [00c5b5c0](../00c5b/00c5b5c0.md)
- [00c5d270](../00c5d/00c5d270.md)

## 関連文字列（未確認候補）

~~~text
"Failed to complete Future as it was likely already deleted."
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3585 bytes

~~~c

void FUN_00bbcab4(undefined8 param_1,long param_2,int param_3,undefined8 param_4,void *param_5)

{
  long lVar1;
  ulong __n;
  undefined1 *__src;
  long lVar2;
  undefined8 uVar3;
  undefined1 *__dest;
  ulong uVar4;
  undefined1 auStack_b0 [16];
  ulong local_a0;
  ulong uStack_98;
  undefined1 *local_90;
  ulong local_80;
  ulong uStack_78;
  undefined1 *local_70;
  long local_68;
  
  lVar1 = tpidr_el0;
  local_68 = *(long *)(lVar1 + 0x28);
  _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2IDnEEPKc
            (&local_a0,&DAT_002a63ea);
  if ((param_2 != 0) && (param_3 == 0)) {
    _ZN8firebase4util17JniStringToStringEP7_JNIEnvP8_jobject(&local_80,param_1,param_2);
    if ((local_a0 & 1) != 0) {
      *local_90 = 0;
      uStack_98 = 0;
      if ((local_a0 & 1) != 0) {
        _ZdlPv(local_90);
      }
    }
    uStack_98 = uStack_78;
    local_a0 = local_80;
    local_90 = local_70;
  }
  _ZN8firebase5Mutex7AcquireEv(&DAT_01126280);
  lVar2 = _ZN8firebase9messaging10FutureData3GetEv();
  if ((lVar2 == 0) || (lVar2 = _ZN8firebase9messaging10FutureData3GetEv(), lVar2 == 0)) {
    _ZN8firebase10LogWarningEPKcz("Failed to complete Future as it was likely already deleted.");
    goto joined_r0x00bbcbc4;
  }
  uVar3 = _ZN8firebase9messaging10FutureData3GetEv();
                    /* try { // try from 00bbcb88 to 00cbcb93 has its CatchHandler @ 00bbce40 */
  _ZN8firebase12FutureHandleC1ERKS0_(auStack_b0,param_5);
  __src = local_90;
  __n = uStack_98;
  uStack_78 = 0;
  local_70 = (undefined1 *)0x0;
  local_80 = 0;
  if ((local_a0 & 1) == 0) {
    uStack_78 = uStack_98;
    local_80 = local_a0;
    local_70 = local_90;
  }
  else {
    if (0xffffffffffffffef < uStack_98) {
      uVar3 = _ZNKSt6__ndk121__basic_string_commonILb1EE20__throw_length_errorEv(&local_80);
      _ZN8firebase12FutureHandleD2Ev(auStack_b0);
      _ZN8firebase5Mutex7ReleaseEv(&DAT_01126280);
      if ((local_a0 & 1) != 0) {
        _ZdlPv(local_90);
      }
                    /* WARNING: Subroutine does not return */
      FUN_00c53f5c(uVar3);
    }
                    /* try { // try from 00bbcc38 to 00cbcc7b has its CatchHandler @ 00bbc8d8 */
    if (uStack_98 < 0x17) {
      __dest = (undefined1 *)((ulong)&local_80 | 1);
      local_80 = (ulong)(byte)((int)uStack_98 << 1);
      if (uStack_98 != 0) goto LAB_00bbcc74;
    }
    else {
      uVar4 = uStack_98 + 0x10 & 0xfffffffffffffff0;
      __dest = (undefined1 *)_Znwm(uVar4);
      local_80 = uVar4 | 1;
      uStack_78 = __n;
      local_70 = __dest;
LAB_00bbcc74:
                    /* try { // try from 00bbcc7c to 00cbcc7f has its CatchHandler @ 00bbce28 */
      memcpy(__dest,__src,__n);
    }
    __dest[__n] = 0;
  }
  _ZN8firebase26ReferenceCountedFutureImpl16CompleteInternalINSt6__ndk112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEZNS0_26CompleteWithResultInternalIS8_EEvRKNS_12FutureHandleEiPKcRKT_EUlPS8_E_EEvSC_iSE_RKT0_
            (uVar3,auStack_b0,(ulong)(param_3 != 0) << 2,param_4,&local_80);
  if ((local_80 & 1) != 0) {
    _ZdlPv(local_70);
  }
  _ZN8firebase12FutureHandleD2Ev(auStack_b0);
joined_r0x00bbcbc4:
  if (param_5 != (void *)0x0) {
    _ZN8firebase12FutureHandleD2Ev(param_5);
                    /* try { // try from 00bbcbd0 to 00cbcc37 has its CatchHandler @ 00bbce78 */
    _ZdlPv(param_5);
  }
  _ZN8firebase5Mutex7ReleaseEv(&DAT_01126280);
  if ((local_a0 & 1) != 0) {
    _ZdlPv(local_90);
  }
  if (*(long *)(lVar1 + 0x28) == local_68) {
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
<a id="insn-00bbcab4"></a> `00bbcab4` | `ff c3 02 d1` | sub sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bbcab8"></a> `00bbcab8` | `fb 2b 00 f9` | str x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbcabc"></a> `00bbcabc` | `fa 67 06 a9` | stp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbcac0"></a> `00bbcac0` | `f8 5f 07 a9` | stp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbcac4"></a> `00bbcac4` | `f6 57 08 a9` | stp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbcac8"></a> `00bbcac8` | `f4 4f 09 a9` | stp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbcacc"></a> `00bbcacc` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbcad0"></a> `00bbcad0` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-00bbcad4"></a> `00bbcad4` | `5a d0 3b d5` | mrs x26,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bbcad8"></a> `00bbcad8` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcadc"></a> `00bbcadc` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00bbcae0"></a> `00bbcae0` | `41 b7 ff d0` | adrp x1,0x2a6000 | `FALL_THROUGH`
<a id="insn-00bbcae4"></a> `00bbcae4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bbcae8"></a> `00bbcae8` | `21 a8 0f 91` | add x1,x1,#0x3ea | `FALL_THROUGH`
<a id="insn-00bbcaec"></a> `00bbcaec` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00bbcaf0"></a> `00bbcaf0` | `f3 03 04 aa` | mov x19,x4 | `FALL_THROUGH`
<a id="insn-00bbcaf4"></a> `00bbcaf4` | `f4 03 03 aa` | mov x20,x3 | `FALL_THROUGH`
<a id="insn-00bbcaf8"></a> `00bbcaf8` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bbcafc"></a> `00bbcafc` | `e8 27 00 f9` | str x8,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbcb00"></a> `00bbcb00` | `b0 7a 02 94` | bl 0x00c5b5c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb04"></a> `00bbcb04` | `d6 02 00 b4` | cbz x22,0x00bbcb5c | `CONDITIONAL_JUMP`
<a id="insn-00bbcb08"></a> `00bbcb08` | `b5 02 00 35` | cbnz w21,0x00bbcb5c | `CONDITIONAL_JUMP`
<a id="insn-00bbcb0c"></a> `00bbcb0c` | `e8 c3 00 91` | add x8,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcb10"></a> `00bbcb10` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00bbcb14"></a> `00bbcb14` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bbcb18"></a> `00bbcb18` | `1e 7a 02 94` | bl 0x00c5b390 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb1c"></a> `00bbcb1c` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcb20"></a> `00bbcb20` | `68 00 00 37` | tbnz w8,#0x0,0x00bbcb2c | `CONDITIONAL_JUMP`
<a id="insn-00bbcb24"></a> `00bbcb24` | `ff 23 00 79` | strh wzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcb28"></a> `00bbcb28` | `09 00 00 14` | b 0x00bbcb4c | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcb2c"></a> `00bbcb2c` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcb30"></a> `00bbcb30` | `1f 01 00 39` | strb wzr,[x8] | `FALL_THROUGH`
<a id="insn-00bbcb34"></a> `00bbcb34` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcb38"></a> `00bbcb38` | `ff 0f 00 f9` | str xzr,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbcb3c"></a> `00bbcb3c` | `88 00 00 36` | tbz w8,#0x0,0x00bbcb4c | `CONDITIONAL_JUMP`
<a id="insn-00bbcb40"></a> `00bbcb40` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcb44"></a> `00bbcb44` | `db 6c 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb48"></a> `00bbcb48` | `ff 0b 00 f9` | str xzr,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcb4c"></a> `00bbcb4c` | `e0 0f c0 3d` | ldr q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcb50"></a> `00bbcb50` | `e8 23 40 f9` | ldr x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbcb54"></a> `00bbcb54` | `e0 07 80 3d` | str q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcb58"></a> `00bbcb58` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcb5c"></a> `00bbcb5c` | `bf 02 00 71` | cmp w21,#0x0 | `FALL_THROUGH`
<a id="insn-00bbcb60"></a> `00bbcb60` | `fb 07 9f 1a` | cset w27,ne | `FALL_THROUGH`
<a id="insn-00bbcb64"></a> `00bbcb64` | `40 2b 00 d0` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbcb68"></a> `00bbcb68` | `00 00 0a 91` | add x0,x0,#0x280 | `FALL_THROUGH`
<a id="insn-00bbcb6c"></a> `00bbcb6c` | `a5 77 02 94` | bl 0x00c5aa00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb70"></a> `00bbcb70` | `c0 81 02 94` | bl 0x00c5d270 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb74"></a> `00bbcb74` | `20 02 00 b4` | cbz x0,0x00bbcbb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbcb78"></a> `00bbcb78` | `be 81 02 94` | bl 0x00c5d270 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb7c"></a> `00bbcb7c` | `e0 01 00 b4` | cbz x0,0x00bbcbb8 | `CONDITIONAL_JUMP`
<a id="insn-00bbcb80"></a> `00bbcb80` | `bc 81 02 94` | bl 0x00c5d270 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb84"></a> `00bbcb84` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bbcb88"></a> `00bbcb88` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bbcb8c"></a> `00bbcb8c` | `e1 03 13 aa` | mov x1,x19 | `FALL_THROUGH`
<a id="insn-00bbcb90"></a> `00bbcb90` | `9c 78 02 94` | bl 0x00c5ae00 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcb94"></a> `00bbcb94` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcb98"></a> `00bbcb98` | `ff ff 03 a9` | stp xzr,xzr,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00bbcb9c"></a> `00bbcb9c` | `ff 1b 00 f9` | str xzr,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcba0"></a> `00bbcba0` | `28 04 00 37` | tbnz w8,#0x0,0x00bbcc24 | `CONDITIONAL_JUMP`
<a id="insn-00bbcba4"></a> `00bbcba4` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcba8"></a> `00bbcba8` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcbac"></a> `00bbcbac` | `e0 0f 80 3d` | str q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcbb0"></a> `00bbcbb0` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbcbb4"></a> `00bbcbb4` | `35 00 00 14` | b 0x00bbcc88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcbb8"></a> `00bbcbb8` | `80 b7 ff 90` | adrp x0,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bbcbbc"></a> `00bbcbbc` | `00 54 06 91` | add x0,x0,#0x195 | `FALL_THROUGH`
<a id="insn-00bbcbc0"></a> `00bbcbc0` | `88 78 02 94` | bl 0x00c5ade0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcbc4"></a> `00bbcbc4` | `b3 00 00 b4` | cbz x19,0x00bbcbd8 | `CONDITIONAL_JUMP`
<a id="insn-00bbcbc8"></a> `00bbcbc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcbcc"></a> `00bbcbcc` | `b1 77 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcbd0"></a> `00bbcbd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcbd4"></a> `00bbcbd4` | `b7 6c 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcbd8"></a> `00bbcbd8` | `40 2b 00 d0` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbcbdc"></a> `00bbcbdc` | `00 00 0a 91` | add x0,x0,#0x280 | `FALL_THROUGH`
<a id="insn-00bbcbe0"></a> `00bbcbe0` | `8c 77 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcbe4"></a> `00bbcbe4` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcbe8"></a> `00bbcbe8` | `68 00 00 36` | tbz w8,#0x0,0x00bbcbf4 | `CONDITIONAL_JUMP`
<a id="insn-00bbcbec"></a> `00bbcbec` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcbf0"></a> `00bbcbf0` | `b0 6c 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcbf4"></a> `00bbcbf4` | `48 17 40 f9` | ldr x8,[x26, #0x28] | `FALL_THROUGH`
<a id="insn-00bbcbf8"></a> `00bbcbf8` | `e9 27 40 f9` | ldr x9,[sp, #0x48] | `FALL_THROUGH`
<a id="insn-00bbcbfc"></a> `00bbcbfc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bbcc00"></a> `00bbcc00` | `01 06 00 54` | b.ne 0x00bbccc0 | `CONDITIONAL_JUMP`
<a id="insn-00bbcc04"></a> `00bbcc04` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-00bbcc08"></a> `00bbcc08` | `f4 4f 49 a9` | ldp x20,x19,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-00bbcc0c"></a> `00bbcc0c` | `f6 57 48 a9` | ldp x22,x21,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00bbcc10"></a> `00bbcc10` | `f8 5f 47 a9` | ldp x24,x23,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00bbcc14"></a> `00bbcc14` | `fa 67 46 a9` | ldp x26,x25,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bbcc18"></a> `00bbcc18` | `fb 2b 40 f9` | ldr x27,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bbcc1c"></a> `00bbcc1c` | `ff c3 02 91` | add sp,sp,#0xb0 | `FALL_THROUGH`
<a id="insn-00bbcc20"></a> `00bbcc20` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bbcc24"></a> `00bbcc24` | `f6 0f 40 f9` | ldr x22,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bbcc28"></a> `00bbcc28` | `df 42 00 b1` | cmn x22,#0x10 | `FALL_THROUGH`
<a id="insn-00bbcc2c"></a> `00bbcc2c` | `c2 04 00 54` | b.cs 0x00bbccc4 | `CONDITIONAL_JUMP`
<a id="insn-00bbcc30"></a> `00bbcc30` | `f7 13 40 f9` | ldr x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcc34"></a> `00bbcc34` | `df 5e 00 f1` | cmp x22,#0x17 | `FALL_THROUGH`
<a id="insn-00bbcc38"></a> `00bbcc38` | `e2 00 00 54` | b.cs 0x00bbcc54 | `CONDITIONAL_JUMP`
<a id="insn-00bbcc3c"></a> `00bbcc3c` | `e9 c3 00 91` | add x9,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcc40"></a> `00bbcc40` | `c8 7a 1f 53` | lsl w8,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcc44"></a> `00bbcc44` | `38 01 40 b2` | orr x24,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcc48"></a> `00bbcc48` | `e8 c3 00 39` | strb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcc4c"></a> `00bbcc4c` | `56 01 00 b5` | cbnz x22,0x00bbcc74 | `CONDITIONAL_JUMP`
<a id="insn-00bbcc50"></a> `00bbcc50` | `0d 00 00 14` | b 0x00bbcc84 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcc54"></a> `00bbcc54` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00bbcc58"></a> `00bbcc58` | `19 ed 7c 92` | and x25,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00bbcc5c"></a> `00bbcc5c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00bbcc60"></a> `00bbcc60` | `8c 6c 02 94` | bl 0x00c57e90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcc64"></a> `00bbcc64` | `28 03 40 b2` | orr x8,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00bbcc68"></a> `00bbcc68` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bbcc6c"></a> `00bbcc6c` | `e8 5b 03 a9` | stp x8,x22,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcc70"></a> `00bbcc70` | `e0 23 00 f9` | str x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbcc74"></a> `00bbcc74` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00bbcc78"></a> `00bbcc78` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bbcc7c"></a> `00bbcc7c` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00bbcc80"></a> `00bbcc80` | `e0 6c 02 94` | bl 0x00c58000 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcc84"></a> `00bbcc84` | `1f 6b 36 38` | strb wzr,[x24, x22, LSL ] | `FALL_THROUGH`
<a id="insn-00bbcc88"></a> `00bbcc88` | `62 77 1e 53` | lsl w2,w27,#0x2 | `FALL_THROUGH`
<a id="insn-00bbcc8c"></a> `00bbcc8c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bbcc90"></a> `00bbcc90` | `e4 c3 00 91` | add x4,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbcc94"></a> `00bbcc94` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bbcc98"></a> `00bbcc98` | `e3 03 14 aa` | mov x3,x20 | `FALL_THROUGH`
<a id="insn-00bbcc9c"></a> `00bbcc9c` | `31 78 02 94` | bl 0x00c5ad60 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcca0"></a> `00bbcca0` | `e8 c3 40 39` | ldrb w8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bbcca4"></a> `00bbcca4` | `68 00 00 36` | tbz w8,#0x0,0x00bbccb0 | `CONDITIONAL_JUMP`
<a id="insn-00bbcca8"></a> `00bbcca8` | `e0 23 40 f9` | ldr x0,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bbccac"></a> `00bbccac` | `81 6c 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbccb0"></a> `00bbccb0` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bbccb4"></a> `00bbccb4` | `77 77 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbccb8"></a> `00bbccb8` | `93 f8 ff b5` | cbnz x19,0x00bbcbc8 | `CONDITIONAL_JUMP`
<a id="insn-00bbccbc"></a> `00bbccbc` | `c7 ff ff 17` | b 0x00bbcbd8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbccc0"></a> `00bbccc0` | `88 6c 02 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`
<a id="insn-00bbccc4"></a> `00bbccc4` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bbccc8"></a> `00bbccc8` | `f2 78 02 94` | bl 0x00c5b090 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcccc"></a> `00bbcccc` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bbccd0"></a> `00bbccd0` | `06 00 00 14` | b 0x00bbcce8 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcce8"></a> `00bbcce8` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bbccec"></a> `00bbccec` | `69 77 02 94` | bl 0x00c5aa90 | `UNCONDITIONAL_CALL`
<a id="insn-00bbccf0"></a> `00bbccf0` | `09 00 00 14` | b 0x00bbcd14 | `UNCONDITIONAL_JUMP`
<a id="insn-00bbcd14"></a> `00bbcd14` | `40 2b 00 d0` | adrp x0,0x1126000 | `FALL_THROUGH`
<a id="insn-00bbcd18"></a> `00bbcd18` | `00 00 0a 91` | add x0,x0,#0x280 | `FALL_THROUGH`
<a id="insn-00bbcd1c"></a> `00bbcd1c` | `3d 77 02 94` | bl 0x00c5aa10 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcd20"></a> `00bbcd20` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bbcd24"></a> `00bbcd24` | `68 00 00 36` | tbz w8,#0x0,0x00bbcd30 | `CONDITIONAL_JUMP`
<a id="insn-00bbcd28"></a> `00bbcd28` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bbcd2c"></a> `00bbcd2c` | `61 6c 02 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bbcd30"></a> `00bbcd30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bbcd34"></a> `00bbcd34` | `8a 5c 02 94` | bl 0x00c53f5c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bbcab4`](#insn-00bbcab4) 範囲 `[['00bbcab4', '00bbcb07']]`
  - `CONDITIONAL_JUMP` [`00bbcb04`](#insn-00bbcb04) → [`00bbcb5c`](#insn-00bbcb5c)
  - `FALL_THROUGH` [`00bbcb04`](#insn-00bbcb04) → [`00bbcb08`](#insn-00bbcb08)
- ブロック [`00bbcb08`](#insn-00bbcb08) 範囲 `[['00bbcb08', '00bbcb0b']]`
  - `CONDITIONAL_JUMP` [`00bbcb08`](#insn-00bbcb08) → [`00bbcb5c`](#insn-00bbcb5c)
  - `FALL_THROUGH` [`00bbcb08`](#insn-00bbcb08) → [`00bbcb0c`](#insn-00bbcb0c)
- ブロック [`00bbcb0c`](#insn-00bbcb0c) 範囲 `[['00bbcb0c', '00bbcb23']]`
  - `CONDITIONAL_JUMP` [`00bbcb20`](#insn-00bbcb20) → [`00bbcb2c`](#insn-00bbcb2c)
  - `FALL_THROUGH` [`00bbcb20`](#insn-00bbcb20) → [`00bbcb24`](#insn-00bbcb24)
- ブロック [`00bbcb24`](#insn-00bbcb24) 範囲 `[['00bbcb24', '00bbcb2b']]`
  - `UNCONDITIONAL_JUMP` [`00bbcb28`](#insn-00bbcb28) → [`00bbcb4c`](#insn-00bbcb4c)
- ブロック [`00bbcb2c`](#insn-00bbcb2c) 範囲 `[['00bbcb2c', '00bbcb3f']]`
  - `CONDITIONAL_JUMP` [`00bbcb3c`](#insn-00bbcb3c) → [`00bbcb4c`](#insn-00bbcb4c)
  - `FALL_THROUGH` [`00bbcb3c`](#insn-00bbcb3c) → [`00bbcb40`](#insn-00bbcb40)
- ブロック [`00bbcb40`](#insn-00bbcb40) 範囲 `[['00bbcb40', '00bbcb4b']]`
  - `FALL_THROUGH` [`00bbcb48`](#insn-00bbcb48) → [`00bbcb4c`](#insn-00bbcb4c)
- ブロック [`00bbcb4c`](#insn-00bbcb4c) 範囲 `[['00bbcb4c', '00bbcb5b']]`
  - `FALL_THROUGH` [`00bbcb58`](#insn-00bbcb58) → [`00bbcb5c`](#insn-00bbcb5c)
- ブロック [`00bbcb5c`](#insn-00bbcb5c) 範囲 `[['00bbcb5c', '00bbcb77']]`
  - `CONDITIONAL_JUMP` [`00bbcb74`](#insn-00bbcb74) → [`00bbcbb8`](#insn-00bbcbb8)
  - `FALL_THROUGH` [`00bbcb74`](#insn-00bbcb74) → [`00bbcb78`](#insn-00bbcb78)
- ブロック [`00bbcb78`](#insn-00bbcb78) 範囲 `[['00bbcb78', '00bbcb7f']]`
  - `CONDITIONAL_JUMP` [`00bbcb7c`](#insn-00bbcb7c) → [`00bbcbb8`](#insn-00bbcbb8)
  - `FALL_THROUGH` [`00bbcb7c`](#insn-00bbcb7c) → [`00bbcb80`](#insn-00bbcb80)
- ブロック [`00bbcb80`](#insn-00bbcb80) 範囲 `[['00bbcb80', '00bbcb87']]`
  - `FALL_THROUGH` [`00bbcb84`](#insn-00bbcb84) → [`00bbcb88`](#insn-00bbcb88)
- ブロック [`00bbcb88`](#insn-00bbcb88) 範囲 `[['00bbcb88', '00bbcba3']]`
  - `CONDITIONAL_JUMP` [`00bbcba0`](#insn-00bbcba0) → [`00bbcc24`](#insn-00bbcc24)
  - `FALL_THROUGH` [`00bbcba0`](#insn-00bbcba0) → [`00bbcba4`](#insn-00bbcba4)
- ブロック [`00bbcba4`](#insn-00bbcba4) 範囲 `[['00bbcba4', '00bbcbb7']]`
  - `UNCONDITIONAL_JUMP` [`00bbcbb4`](#insn-00bbcbb4) → [`00bbcc88`](#insn-00bbcc88)
- ブロック [`00bbcbb8`](#insn-00bbcbb8) 範囲 `[['00bbcbb8', '00bbcbc7']]`
  - `CONDITIONAL_JUMP` [`00bbcbc4`](#insn-00bbcbc4) → [`00bbcbd8`](#insn-00bbcbd8)
  - `FALL_THROUGH` [`00bbcbc4`](#insn-00bbcbc4) → [`00bbcbc8`](#insn-00bbcbc8)
- ブロック [`00bbcbc8`](#insn-00bbcbc8) 範囲 `[['00bbcbc8', '00bbcbcf']]`
  - `FALL_THROUGH` [`00bbcbcc`](#insn-00bbcbcc) → [`00bbcbd0`](#insn-00bbcbd0)
- ブロック [`00bbcbd0`](#insn-00bbcbd0) 範囲 `[['00bbcbd0', '00bbcbd7']]`
  - `FALL_THROUGH` [`00bbcbd4`](#insn-00bbcbd4) → [`00bbcbd8`](#insn-00bbcbd8)
- ブロック [`00bbcbd8`](#insn-00bbcbd8) 範囲 `[['00bbcbd8', '00bbcbeb']]`
  - `CONDITIONAL_JUMP` [`00bbcbe8`](#insn-00bbcbe8) → [`00bbcbf4`](#insn-00bbcbf4)
  - `FALL_THROUGH` [`00bbcbe8`](#insn-00bbcbe8) → [`00bbcbec`](#insn-00bbcbec)
- ブロック [`00bbcbec`](#insn-00bbcbec) 範囲 `[['00bbcbec', '00bbcbf3']]`
  - `FALL_THROUGH` [`00bbcbf0`](#insn-00bbcbf0) → [`00bbcbf4`](#insn-00bbcbf4)
- ブロック [`00bbcbf4`](#insn-00bbcbf4) 範囲 `[['00bbcbf4', '00bbcc03']]`
  - `CONDITIONAL_JUMP` [`00bbcc00`](#insn-00bbcc00) → [`00bbccc0`](#insn-00bbccc0)
  - `FALL_THROUGH` [`00bbcc00`](#insn-00bbcc00) → [`00bbcc04`](#insn-00bbcc04)
- ブロック [`00bbcc04`](#insn-00bbcc04) 範囲 `[['00bbcc04', '00bbcc23']]`
- ブロック [`00bbcc24`](#insn-00bbcc24) 範囲 `[['00bbcc24', '00bbcc2f']]`
  - `CONDITIONAL_JUMP` [`00bbcc2c`](#insn-00bbcc2c) → [`00bbccc4`](#insn-00bbccc4)
  - `FALL_THROUGH` [`00bbcc2c`](#insn-00bbcc2c) → [`00bbcc30`](#insn-00bbcc30)
- ブロック [`00bbcc30`](#insn-00bbcc30) 範囲 `[['00bbcc30', '00bbcc37']]`
  - `FALL_THROUGH` [`00bbcc34`](#insn-00bbcc34) → [`00bbcc38`](#insn-00bbcc38)
- ブロック [`00bbcc38`](#insn-00bbcc38) 範囲 `[['00bbcc38', '00bbcc3b']]`
  - `CONDITIONAL_JUMP` [`00bbcc38`](#insn-00bbcc38) → [`00bbcc54`](#insn-00bbcc54)
  - `FALL_THROUGH` [`00bbcc38`](#insn-00bbcc38) → [`00bbcc3c`](#insn-00bbcc3c)
- ブロック [`00bbcc3c`](#insn-00bbcc3c) 範囲 `[['00bbcc3c', '00bbcc4f']]`
  - `CONDITIONAL_JUMP` [`00bbcc4c`](#insn-00bbcc4c) → [`00bbcc74`](#insn-00bbcc74)
  - `FALL_THROUGH` [`00bbcc4c`](#insn-00bbcc4c) → [`00bbcc50`](#insn-00bbcc50)
- ブロック [`00bbcc50`](#insn-00bbcc50) 範囲 `[['00bbcc50', '00bbcc53']]`
  - `UNCONDITIONAL_JUMP` [`00bbcc50`](#insn-00bbcc50) → [`00bbcc84`](#insn-00bbcc84)
- ブロック [`00bbcc54`](#insn-00bbcc54) 範囲 `[['00bbcc54', '00bbcc73']]`
  - `FALL_THROUGH` [`00bbcc70`](#insn-00bbcc70) → [`00bbcc74`](#insn-00bbcc74)
- ブロック [`00bbcc74`](#insn-00bbcc74) 範囲 `[['00bbcc74', '00bbcc7b']]`
  - `FALL_THROUGH` [`00bbcc78`](#insn-00bbcc78) → [`00bbcc7c`](#insn-00bbcc7c)
- ブロック [`00bbcc7c`](#insn-00bbcc7c) 範囲 `[['00bbcc7c', '00bbcc83']]`
  - `FALL_THROUGH` [`00bbcc80`](#insn-00bbcc80) → [`00bbcc84`](#insn-00bbcc84)
- ブロック [`00bbcc84`](#insn-00bbcc84) 範囲 `[['00bbcc84', '00bbcc87']]`
  - `FALL_THROUGH` [`00bbcc84`](#insn-00bbcc84) → [`00bbcc88`](#insn-00bbcc88)
- ブロック [`00bbcc88`](#insn-00bbcc88) 範囲 `[['00bbcc88', '00bbcca7']]`
  - `CONDITIONAL_JUMP` [`00bbcca4`](#insn-00bbcca4) → [`00bbccb0`](#insn-00bbccb0)
  - `FALL_THROUGH` [`00bbcca4`](#insn-00bbcca4) → [`00bbcca8`](#insn-00bbcca8)
- ブロック [`00bbcca8`](#insn-00bbcca8) 範囲 `[['00bbcca8', '00bbccaf']]`
  - `FALL_THROUGH` [`00bbccac`](#insn-00bbccac) → [`00bbccb0`](#insn-00bbccb0)
- ブロック [`00bbccb0`](#insn-00bbccb0) 範囲 `[['00bbccb0', '00bbccbb']]`
  - `CONDITIONAL_JUMP` [`00bbccb8`](#insn-00bbccb8) → [`00bbcbc8`](#insn-00bbcbc8)
  - `FALL_THROUGH` [`00bbccb8`](#insn-00bbccb8) → [`00bbccbc`](#insn-00bbccbc)
- ブロック [`00bbccbc`](#insn-00bbccbc) 範囲 `[['00bbccbc', '00bbccbf']]`
  - `UNCONDITIONAL_JUMP` [`00bbccbc`](#insn-00bbccbc) → [`00bbcbd8`](#insn-00bbcbd8)
- ブロック [`00bbccc0`](#insn-00bbccc0) 範囲 `[['00bbccc0', '00bbccc3']]`
- ブロック [`00bbccc4`](#insn-00bbccc4) 範囲 `[['00bbccc4', '00bbccd3']]`
  - `UNCONDITIONAL_JUMP` [`00bbccd0`](#insn-00bbccd0) → [`00bbcce8`](#insn-00bbcce8)
- ブロック [`00bbcce8`](#insn-00bbcce8) 範囲 `[['00bbcce8', '00bbccf3']]`
  - `UNCONDITIONAL_JUMP` [`00bbccf0`](#insn-00bbccf0) → [`00bbcd14`](#insn-00bbcd14)
- ブロック [`00bbcd14`](#insn-00bbcd14) 範囲 `[['00bbcd14', '00bbcd27']]`
  - `CONDITIONAL_JUMP` [`00bbcd24`](#insn-00bbcd24) → [`00bbcd30`](#insn-00bbcd30)
  - `FALL_THROUGH` [`00bbcd24`](#insn-00bbcd24) → [`00bbcd28`](#insn-00bbcd28)
- ブロック [`00bbcd28`](#insn-00bbcd28) 範囲 `[['00bbcd28', '00bbcd2f']]`
  - `FALL_THROUGH` [`00bbcd2c`](#insn-00bbcd2c) → [`00bbcd30`](#insn-00bbcd30)
- ブロック [`00bbcd30`](#insn-00bbcd30) 範囲 `[['00bbcd30', '00bbcd37']]`

## 命令位置別の参照

- [`00bbcab8`](#insn-00bbcab8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcabc`](#insn-00bbcabc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcac0`](#insn-00bbcac0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcac4`](#insn-00bbcac4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcac8`](#insn-00bbcac8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcacc`](#insn-00bbcacc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcae8`](#insn-00bbcae8) → `002a63ea`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bbcafc`](#insn-00bbcafc) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb00`](#insn-00bbcb00) → [`00c5b5c0`](../00c5b/00c5b5c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b5c0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb04`](#insn-00bbcb04) → [`00bbcb5c`](#insn-00bbcb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb08`](#insn-00bbcb08) → [`00bbcb5c`](#insn-00bbcb5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb18`](#insn-00bbcb18) → [`00c5b390`](../00c5b/00c5b390.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b390` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb1c`](#insn-00bbcb1c) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb20`](#insn-00bbcb20) → [`00bbcb2c`](#insn-00bbcb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb24`](#insn-00bbcb24) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb28`](#insn-00bbcb28) → [`00bbcb4c`](#insn-00bbcb4c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb2c`](#insn-00bbcb2c) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb34`](#insn-00bbcb34) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb38`](#insn-00bbcb38) → `Stack[-0x98]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb3c`](#insn-00bbcb3c) → [`00bbcb4c`](#insn-00bbcb4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb40`](#insn-00bbcb40) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb44`](#insn-00bbcb44) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb48`](#insn-00bbcb48) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb4c`](#insn-00bbcb4c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb50`](#insn-00bbcb50) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb54`](#insn-00bbcb54) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb58`](#insn-00bbcb58) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb68`](#insn-00bbcb68) → `01126280`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb6c`](#insn-00bbcb6c) → [`00c5aa00`](../00c5a/00c5aa00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa00` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb70`](#insn-00bbcb70) → [`00c5d270`](../00c5d/00c5d270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d270` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb74`](#insn-00bbcb74) → [`00bbcbb8`](#insn-00bbcbb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb78`](#insn-00bbcb78) → [`00c5d270`](../00c5d/00c5d270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d270` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb7c`](#insn-00bbcb7c) → [`00bbcbb8`](#insn-00bbcbb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb80`](#insn-00bbcb80) → [`00c5d270`](../00c5d/00c5d270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5d270` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb90`](#insn-00bbcb90) → [`00c5ae00`](../00c5a/00c5ae00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ae00` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb94`](#insn-00bbcb94) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb98`](#insn-00bbcb98) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcb9c`](#insn-00bbcb9c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcba0`](#insn-00bbcba0) → [`00bbcc24`](#insn-00bbcc24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcba4`](#insn-00bbcba4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcba8`](#insn-00bbcba8) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbac`](#insn-00bbcbac) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbb0`](#insn-00bbcbb0) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbb4`](#insn-00bbcbb4) → [`00bbcc88`](#insn-00bbcc88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbbc`](#insn-00bbcbbc) → `002ac195`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bbcbc0`](#insn-00bbcbc0) → [`00c5ade0`](../00c5a/00c5ade0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ade0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbc4`](#insn-00bbcbc4) → [`00bbcbd8`](#insn-00bbcbd8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbcc`](#insn-00bbcbcc) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbd4`](#insn-00bbcbd4) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbdc`](#insn-00bbcbdc) → `01126280`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbe0`](#insn-00bbcbe0) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbe4`](#insn-00bbcbe4) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbe8`](#insn-00bbcbe8) → [`00bbcbf4`](#insn-00bbcbf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbec`](#insn-00bbcbec) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbf0`](#insn-00bbcbf0) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcbf8`](#insn-00bbcbf8) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc00`](#insn-00bbcc00) → [`00bbccc0`](#insn-00bbccc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc04`](#insn-00bbcc04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc08`](#insn-00bbcc08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc0c`](#insn-00bbcc0c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc10`](#insn-00bbcc10) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc14`](#insn-00bbcc14) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc18`](#insn-00bbcc18) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc24`](#insn-00bbcc24) → `Stack[-0x98]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc2c`](#insn-00bbcc2c) → [`00bbccc4`](#insn-00bbccc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc30`](#insn-00bbcc30) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc38`](#insn-00bbcc38) → [`00bbcc54`](#insn-00bbcc54) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc48`](#insn-00bbcc48) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc4c`](#insn-00bbcc4c) → [`00bbcc74`](#insn-00bbcc74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc50`](#insn-00bbcc50) → [`00bbcc84`](#insn-00bbcc84) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc60`](#insn-00bbcc60) → [`00c57e90`](../00c57/00c57e90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57e90` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc6c`](#insn-00bbcc6c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc70`](#insn-00bbcc70) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc80`](#insn-00bbcc80) → [`00c58000`](../00c58/00c58000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58000` · 推定シンボル `None` · 推定型 `None`
- [`00bbcc9c`](#insn-00bbcc9c) → [`00c5ad60`](../00c5a/00c5ad60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad60` · 推定シンボル `None` · 推定型 `None`
- [`00bbcca0`](#insn-00bbcca0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcca4`](#insn-00bbcca4) → [`00bbccb0`](#insn-00bbccb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcca8`](#insn-00bbcca8) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccac`](#insn-00bbccac) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbccb4`](#insn-00bbccb4) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bbccb8`](#insn-00bbccb8) → [`00bbcbc8`](#insn-00bbcbc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccbc`](#insn-00bbccbc) → [`00bbcbd8`](#insn-00bbcbd8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccc0`](#insn-00bbccc0) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`
- [`00bbccc8`](#insn-00bbccc8) → [`00c5b090`](../00c5b/00c5b090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b090` · 推定シンボル `None` · 推定型 `None`
- [`00bbccd0`](#insn-00bbccd0) → [`00bbcce8`](#insn-00bbcce8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbccec`](#insn-00bbccec) → [`00c5aa90`](../00c5a/00c5aa90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa90` · 推定シンボル `None` · 推定型 `None`
- [`00bbccf0`](#insn-00bbccf0) → [`00bbcd14`](#insn-00bbcd14) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd18`](#insn-00bbcd18) → `01126280`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd1c`](#insn-00bbcd1c) → [`00c5aa10`](../00c5a/00c5aa10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aa10` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd20`](#insn-00bbcd20) → `Stack[-0xa0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd24`](#insn-00bbcd24) → [`00bbcd30`](#insn-00bbcd30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd28`](#insn-00bbcd28) → `Stack[-0x90]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd2c`](#insn-00bbcd2c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00bbcd34`](#insn-00bbcd34) → [`00c53f5c`](../00c53/00c53f5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53f5c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bbcab8`](#insn-00bbcab8)

~~~json
{
  "source": "00bbcab8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcabc`](#insn-00bbcabc)

~~~json
{
  "source": "00bbcabc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcac0`](#insn-00bbcac0)

~~~json
{
  "source": "00bbcac0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcac4`](#insn-00bbcac4)

~~~json
{
  "source": "00bbcac4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcac8`](#insn-00bbcac8)

~~~json
{
  "source": "00bbcac8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcacc`](#insn-00bbcacc)

~~~json
{
  "source": "00bbcacc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcae8`](#insn-00bbcae8)

~~~json
{
  "source": "00bbcae8",
  "target": "002a63ea",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a63ea",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "bytes": "00",
  "capture_start": "002a63ea",
  "capture_bytes": 1,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bbcafc`](#insn-00bbcafc)

~~~json
{
  "source": "00bbcafc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb00`](#insn-00bbcb00)

~~~json
{
  "source": "00bbcb00",
  "target": "00c5b5c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb04`](#insn-00bbcb04)

~~~json
{
  "source": "00bbcb04",
  "target": "00bbcb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb08`](#insn-00bbcb08)

~~~json
{
  "source": "00bbcb08",
  "target": "00bbcb5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb18`](#insn-00bbcb18)

~~~json
{
  "source": "00bbcb18",
  "target": "00c5b390",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb1c`](#insn-00bbcb1c)

~~~json
{
  "source": "00bbcb1c",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb20`](#insn-00bbcb20)

~~~json
{
  "source": "00bbcb20",
  "target": "00bbcb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb24`](#insn-00bbcb24)

~~~json
{
  "source": "00bbcb24",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb28`](#insn-00bbcb28)

~~~json
{
  "source": "00bbcb28",
  "target": "00bbcb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb2c`](#insn-00bbcb2c)

~~~json
{
  "source": "00bbcb2c",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb34`](#insn-00bbcb34)

~~~json
{
  "source": "00bbcb34",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb38`](#insn-00bbcb38)

~~~json
{
  "source": "00bbcb38",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb3c`](#insn-00bbcb3c)

~~~json
{
  "source": "00bbcb3c",
  "target": "00bbcb4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb40`](#insn-00bbcb40)

~~~json
{
  "source": "00bbcb40",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb44`](#insn-00bbcb44)

~~~json
{
  "source": "00bbcb44",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb48`](#insn-00bbcb48)

~~~json
{
  "source": "00bbcb48",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb4c`](#insn-00bbcb4c)

~~~json
{
  "source": "00bbcb4c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb50`](#insn-00bbcb50)

~~~json
{
  "source": "00bbcb50",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb54`](#insn-00bbcb54)

~~~json
{
  "source": "00bbcb54",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb58`](#insn-00bbcb58)

~~~json
{
  "source": "00bbcb58",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb68`](#insn-00bbcb68)

~~~json
{
  "source": "00bbcb68",
  "target": "01126280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb6c`](#insn-00bbcb6c)

~~~json
{
  "source": "00bbcb6c",
  "target": "00c5aa00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb70`](#insn-00bbcb70)

~~~json
{
  "source": "00bbcb70",
  "target": "00c5d270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb74`](#insn-00bbcb74)

~~~json
{
  "source": "00bbcb74",
  "target": "00bbcbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb78`](#insn-00bbcb78)

~~~json
{
  "source": "00bbcb78",
  "target": "00c5d270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb7c`](#insn-00bbcb7c)

~~~json
{
  "source": "00bbcb7c",
  "target": "00bbcbb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb80`](#insn-00bbcb80)

~~~json
{
  "source": "00bbcb80",
  "target": "00c5d270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb90`](#insn-00bbcb90)

~~~json
{
  "source": "00bbcb90",
  "target": "00c5ae00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcb94`](#insn-00bbcb94)

~~~json
{
  "source": "00bbcb94",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb98`](#insn-00bbcb98)

~~~json
{
  "source": "00bbcb98",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcb9c`](#insn-00bbcb9c)

~~~json
{
  "source": "00bbcb9c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcba0`](#insn-00bbcba0)

~~~json
{
  "source": "00bbcba0",
  "target": "00bbcc24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcba4`](#insn-00bbcba4)

~~~json
{
  "source": "00bbcba4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcba8`](#insn-00bbcba8)

~~~json
{
  "source": "00bbcba8",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbac`](#insn-00bbcbac)

~~~json
{
  "source": "00bbcbac",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbb0`](#insn-00bbcbb0)

~~~json
{
  "source": "00bbcbb0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbb4`](#insn-00bbcbb4)

~~~json
{
  "source": "00bbcbb4",
  "target": "00bbcc88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbbc`](#insn-00bbcbbc)

~~~json
{
  "source": "00bbcbbc",
  "target": "002ac195",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac195",
  "offset": 0,
  "size": 60,
  "datatype": "string",
  "bytes": "4661696c656420746f20636f6d706c6574652046757475726520617320697420",
  "capture_start": "002ac195",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bbcbc0`](#insn-00bbcbc0)

~~~json
{
  "source": "00bbcbc0",
  "target": "00c5ade0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcbc4`](#insn-00bbcbc4)

~~~json
{
  "source": "00bbcbc4",
  "target": "00bbcbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbcc`](#insn-00bbcbcc)

~~~json
{
  "source": "00bbcbcc",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcbd4`](#insn-00bbcbd4)

~~~json
{
  "source": "00bbcbd4",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcbdc`](#insn-00bbcbdc)

~~~json
{
  "source": "00bbcbdc",
  "target": "01126280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbe0`](#insn-00bbcbe0)

~~~json
{
  "source": "00bbcbe0",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcbe4`](#insn-00bbcbe4)

~~~json
{
  "source": "00bbcbe4",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbe8`](#insn-00bbcbe8)

~~~json
{
  "source": "00bbcbe8",
  "target": "00bbcbf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbec`](#insn-00bbcbec)

~~~json
{
  "source": "00bbcbec",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcbf0`](#insn-00bbcbf0)

~~~json
{
  "source": "00bbcbf0",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcbf8`](#insn-00bbcbf8)

~~~json
{
  "source": "00bbcbf8",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc00`](#insn-00bbcc00)

~~~json
{
  "source": "00bbcc00",
  "target": "00bbccc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc04`](#insn-00bbcc04)

~~~json
{
  "source": "00bbcc04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc08`](#insn-00bbcc08)

~~~json
{
  "source": "00bbcc08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc0c`](#insn-00bbcc0c)

~~~json
{
  "source": "00bbcc0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc10`](#insn-00bbcc10)

~~~json
{
  "source": "00bbcc10",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc14`](#insn-00bbcc14)

~~~json
{
  "source": "00bbcc14",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc18`](#insn-00bbcc18)

~~~json
{
  "source": "00bbcc18",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc24`](#insn-00bbcc24)

~~~json
{
  "source": "00bbcc24",
  "target": "Stack[-0x98]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc2c`](#insn-00bbcc2c)

~~~json
{
  "source": "00bbcc2c",
  "target": "00bbccc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc30`](#insn-00bbcc30)

~~~json
{
  "source": "00bbcc30",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc38`](#insn-00bbcc38)

~~~json
{
  "source": "00bbcc38",
  "target": "00bbcc54",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc48`](#insn-00bbcc48)

~~~json
{
  "source": "00bbcc48",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc4c`](#insn-00bbcc4c)

~~~json
{
  "source": "00bbcc4c",
  "target": "00bbcc74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc50`](#insn-00bbcc50)

~~~json
{
  "source": "00bbcc50",
  "target": "00bbcc84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc60`](#insn-00bbcc60)

~~~json
{
  "source": "00bbcc60",
  "target": "00c57e90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcc6c`](#insn-00bbcc6c)

~~~json
{
  "source": "00bbcc6c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc70`](#insn-00bbcc70)

~~~json
{
  "source": "00bbcc70",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcc80`](#insn-00bbcc80)

~~~json
{
  "source": "00bbcc80",
  "target": "00c58000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcc9c`](#insn-00bbcc9c)

~~~json
{
  "source": "00bbcc9c",
  "target": "00c5ad60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcca0`](#insn-00bbcca0)

~~~json
{
  "source": "00bbcca0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcca4`](#insn-00bbcca4)

~~~json
{
  "source": "00bbcca4",
  "target": "00bbccb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcca8`](#insn-00bbcca8)

~~~json
{
  "source": "00bbcca8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccac`](#insn-00bbccac)

~~~json
{
  "source": "00bbccac",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbccb4`](#insn-00bbccb4)

~~~json
{
  "source": "00bbccb4",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbccb8`](#insn-00bbccb8)

~~~json
{
  "source": "00bbccb8",
  "target": "00bbcbc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccbc`](#insn-00bbccbc)

~~~json
{
  "source": "00bbccbc",
  "target": "00bbcbd8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccc0`](#insn-00bbccc0)

~~~json
{
  "source": "00bbccc0",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbccc8`](#insn-00bbccc8)

~~~json
{
  "source": "00bbccc8",
  "target": "00c5b090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbccd0`](#insn-00bbccd0)

~~~json
{
  "source": "00bbccd0",
  "target": "00bbcce8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbccec`](#insn-00bbccec)

~~~json
{
  "source": "00bbccec",
  "target": "00c5aa90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbccf0`](#insn-00bbccf0)

~~~json
{
  "source": "00bbccf0",
  "target": "00bbcd14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd18`](#insn-00bbcd18)

~~~json
{
  "source": "00bbcd18",
  "target": "01126280",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd1c`](#insn-00bbcd1c)

~~~json
{
  "source": "00bbcd1c",
  "target": "00c5aa10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcd20`](#insn-00bbcd20)

~~~json
{
  "source": "00bbcd20",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd24`](#insn-00bbcd24)

~~~json
{
  "source": "00bbcd24",
  "target": "00bbcd30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd28`](#insn-00bbcd28)

~~~json
{
  "source": "00bbcd28",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bbcd2c`](#insn-00bbcd2c)

~~~json
{
  "source": "00bbcd2c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bbcd34`](#insn-00bbcd34)

~~~json
{
  "source": "00bbcd34",
  "target": "00c53f5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
