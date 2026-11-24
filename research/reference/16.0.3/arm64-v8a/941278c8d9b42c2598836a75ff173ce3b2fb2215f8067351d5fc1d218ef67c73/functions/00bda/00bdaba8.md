# 00bdaba8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd9bb4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd9/00bd9bb4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-3be16bc9a38c5bd07a33a7fddf78e5ec)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdaba8",
  "name": "_ZN8firebase4auth18GoogleAuthProvider13GetCredentialEPKcS3_",
  "size": 420,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ab677bfb8fd4c021a9a31464a6a6c42b0da3d31d147c982974860801ded85dd9",
  "source_text_sha256": "ab677bfb8fd4c021a9a31464a6a6c42b0da3d31d147c982974860801ded85dd9",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdaba8",
        "00bdad4b"
      ]
    ],
    "bytes_sha256": "9af57addb36402d59a3d1d71a97a446907db84d2d2911a58d84c228a28d0fe79",
    "instruction_count": 105,
    "instruction_bytes": 420,
    "body_bytes": 420,
    "indirect": 6,
    "unresolved": 6
  }
}
~~~

## 呼び出し元

- [00c5ba70](../00c5b/00c5ba70.md)

## 呼び出し先

- [00c5bc40](../00c5b/00c5bc40.md)
- [00c5bd40](../00c5b/00c5bd40.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c0a0](../00c5c/00c5c0a0.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c300](../00c5c/00c5c300.md)

## 関連文字列（未確認候補）

~~~text
"Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
"app != nullptr"
"g_methods_cached"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2555 bytes

~~~c

void _ZN8firebase4auth18GoogleAuthProvider13GetCredentialEPKcS3_
               (undefined8 *param_1,char *param_2,char *param_3)

{
  long lVar1;
  long lVar2;
  long *plVar3;
  long lVar4;
  long lVar5;
  ulong uVar6;
  undefined8 uVar7;
  
  if (DAT_01127db8 == '\0') {
    _ZN8firebase8LogErrorEPKcz("g_methods_cached");
                    /* try { // try from 00bdac54 to 00cdb4e3 has its CatchHandler @ 00bd7fb0 */
    _ZN8firebase9LogAssertEPKcz
              (
              "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
              );
  }
  else {
    lVar2 = _ZN8firebase10app_common9GetAnyAppEv();
    if (lVar2 == 0) {
      _ZN8firebase9LogAssertEPKcz("app != nullptr");
    }
    plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar2);
                    /* try { // try from 00bdabf8 to 00cdac03 has its CatchHandler @ 00be0074 */
    lVar2 = 0;
    if (param_2 == (char *)0x0) {
LAB_00bdac1c:
      if (param_3 == (char *)0x0) goto LAB_00bdac68;
LAB_00bdac20:
      if (*param_3 == '\0') goto LAB_00bdac68;
                    /* try { // try from 00bdac2c to 00cdac37 has its CatchHandler @ 00be004c */
                    /* try { // try from 00bdac38 to 00cdac53 has its CatchHandler @ 00be0034 */
      lVar4 = (**(code **)(*plVar3 + 0x538))(plVar3,param_3);
    }
    else {
      if (*param_2 != '\0') {
        lVar2 = (**(code **)(*plVar3 + 0x538))(plVar3,param_2);
        goto LAB_00bdac1c;
      }
      lVar2 = 0;
      if (param_3 != (char *)0x0) goto LAB_00bdac20;
LAB_00bdac68:
      lVar4 = 0;
    }
    lVar5 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                      (plVar3,DAT_01127b88,DAT_01127b98,lVar2,lVar4);
    uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar3);
    lVar1 = 0;
    if ((uVar6 & 1) == 0) {
      lVar1 = lVar5;
    }
    if (lVar2 != 0) {
      (**(code **)(*plVar3 + 0xb8))(plVar3,lVar2);
    }
    if (lVar4 != 0) {
      (**(code **)(*plVar3 + 0xb8))(plVar3,lVar4);
    }
    if (lVar1 != 0) {
      lVar2 = _ZN8firebase10app_common9GetAnyAppEv();
      if (lVar2 == 0) {
        _ZN8firebase9LogAssertEPKcz("app != nullptr");
      }
      plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar2);
      uVar7 = (**(code **)(*plVar3 + 0xa8))(plVar3,lVar1);
      (**(code **)(*plVar3 + 0xb8))(plVar3,lVar1);
      goto LAB_00bdad28;
    }
  }
  uVar7 = 0;
LAB_00bdad28:
  *param_1 = uVar7;
  *(undefined4 *)(param_1 + 1) = 0;
  param_1[3] = 0;
  param_1[4] = 0;
  param_1[2] = 0;
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdaba8"></a> `00bdaba8` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bdabac"></a> `00bdabac` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdabb0"></a> `00bdabb0` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdabb4"></a> `00bdabb4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdabb8"></a> `00bdabb8` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bdabbc"></a> `00bdabbc` | `69 2a 00 b0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdabc0"></a> `00bdabc0` | `29 e1 76 39` | ldrb w9,[x9, #0xdb8] | `FALL_THROUGH`
<a id="insn-00bdabc4"></a> `00bdabc4` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bdabc8"></a> `00bdabc8` | `e9 03 00 34` | cbz w9,0x00bdac44 | `CONDITIONAL_JUMP`
<a id="insn-00bdabcc"></a> `00bdabcc` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bdabd0"></a> `00bdabd0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdabd4"></a> `00bdabd4` | `cb 05 02 94` | bl 0x00c5c300 | `UNCONDITIONAL_CALL`
<a id="insn-00bdabd8"></a> `00bdabd8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdabdc"></a> `00bdabdc` | `80 00 00 b5` | cbnz x0,0x00bdabec | `CONDITIONAL_JUMP`
<a id="insn-00bdabe0"></a> `00bdabe0` | `c0 b6 ff 90` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bdabe4"></a> `00bdabe4` | `00 4c 19 91` | add x0,x0,#0x653 | `FALL_THROUGH`
<a id="insn-00bdabe8"></a> `00bdabe8` | `2e 05 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdabec"></a> `00bdabec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdabf0"></a> `00bdabf0` | `4c 05 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdabf4"></a> `00bdabf4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdabf8"></a> `00bdabf8` | `36 01 00 b4` | cbz x22,0x00bdac1c | `CONDITIONAL_JUMP`
<a id="insn-00bdabfc"></a> `00bdabfc` | `c8 02 40 39` | ldrb w8,[x22] | `FALL_THROUGH`
<a id="insn-00bdac00"></a> `00bdac00` | `08 03 00 34` | cbz w8,0x00bdac60 | `CONDITIONAL_JUMP`
<a id="insn-00bdac04"></a> `00bdac04` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bdac08"></a> `00bdac08` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdac0c"></a> `00bdac0c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdac10"></a> `00bdac10` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bdac14"></a> `00bdac14` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdac18"></a> `00bdac18` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdac1c"></a> `00bdac1c` | `75 02 00 b4` | cbz x21,0x00bdac68 | `CONDITIONAL_JUMP`
<a id="insn-00bdac20"></a> `00bdac20` | `a8 02 40 39` | ldrb w8,[x21] | `FALL_THROUGH`
<a id="insn-00bdac24"></a> `00bdac24` | `28 02 00 34` | cbz w8,0x00bdac68 | `CONDITIONAL_JUMP`
<a id="insn-00bdac28"></a> `00bdac28` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bdac2c"></a> `00bdac2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdac30"></a> `00bdac30` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdac34"></a> `00bdac34` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bdac38"></a> `00bdac38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdac3c"></a> `00bdac3c` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdac40"></a> `00bdac40` | `0b 00 00 14` | b 0x00bdac6c | `UNCONDITIONAL_JUMP`
<a id="insn-00bdac44"></a> `00bdac44` | `e0 b6 ff b0` | adrp x0,0x2b7000 | `FALL_THROUGH`
<a id="insn-00bdac48"></a> `00bdac48` | `00 7c 3c 91` | add x0,x0,#0xf1f | `FALL_THROUGH`
<a id="insn-00bdac4c"></a> `00bdac4c` | `3d 04 02 94` | bl 0x00c5bd40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdac50"></a> `00bdac50` | `a0 b9 ff d0` | adrp x0,0x310000 | `FALL_THROUGH`
<a id="insn-00bdac54"></a> `00bdac54` | `00 c0 05 91` | add x0,x0,#0x170 | `FALL_THROUGH`
<a id="insn-00bdac58"></a> `00bdac58` | `12 05 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdac5c"></a> `00bdac5c` | `32 00 00 14` | b 0x00bdad24 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdac60"></a> `00bdac60` | `f6 03 1f aa` | mov x22,xzr | `FALL_THROUGH`
<a id="insn-00bdac64"></a> `00bdac64` | `f5 fd ff b5` | cbnz x21,0x00bdac20 | `CONDITIONAL_JUMP`
<a id="insn-00bdac68"></a> `00bdac68` | `f7 03 1f aa` | mov x23,xzr | `FALL_THROUGH`
<a id="insn-00bdac6c"></a> `00bdac6c` | `68 2a 00 b0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdac70"></a> `00bdac70` | `69 2a 00 b0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdac74"></a> `00bdac74` | `01 c5 45 f9` | ldr x1,[x8, #0xb88] | `FALL_THROUGH`
<a id="insn-00bdac78"></a> `00bdac78` | `22 cd 45 f9` | ldr x2,[x9, #0xb98] | `FALL_THROUGH`
<a id="insn-00bdac7c"></a> `00bdac7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdac80"></a> `00bdac80` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bdac84"></a> `00bdac84` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00bdac88"></a> `00bdac88` | `ee 03 02 94` | bl 0x00c5bc40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdac8c"></a> `00bdac8c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdac90"></a> `00bdac90` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdac94"></a> `00bdac94` | `db 04 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bdac98"></a> `00bdac98` | `1f 00 00 72` | tst w0,#0x1 | `FALL_THROUGH`
<a id="insn-00bdac9c"></a> `00bdac9c` | `f5 13 95 9a` | csel x21,xzr,x21,ne | `FALL_THROUGH`
<a id="insn-00bdaca0"></a> `00bdaca0` | `d6 00 00 b4` | cbz x22,0x00bdacb8 | `CONDITIONAL_JUMP`
<a id="insn-00bdaca4"></a> `00bdaca4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bdaca8"></a> `00bdaca8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdacac"></a> `00bdacac` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdacb0"></a> `00bdacb0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdacb4"></a> `00bdacb4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdacb8"></a> `00bdacb8` | `d7 00 00 b4` | cbz x23,0x00bdacd0 | `CONDITIONAL_JUMP`
<a id="insn-00bdacbc"></a> `00bdacbc` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bdacc0"></a> `00bdacc0` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdacc4"></a> `00bdacc4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bdacc8"></a> `00bdacc8` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdaccc"></a> `00bdaccc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdacd0"></a> `00bdacd0` | `b5 02 00 b4` | cbz x21,0x00bdad24 | `CONDITIONAL_JUMP`
<a id="insn-00bdacd4"></a> `00bdacd4` | `8b 05 02 94` | bl 0x00c5c300 | `UNCONDITIONAL_CALL`
<a id="insn-00bdacd8"></a> `00bdacd8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdacdc"></a> `00bdacdc` | `80 00 00 b5` | cbnz x0,0x00bdacec | `CONDITIONAL_JUMP`
<a id="insn-00bdace0"></a> `00bdace0` | `c0 b6 ff 90` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bdace4"></a> `00bdace4` | `00 4c 19 91` | add x0,x0,#0x653 | `FALL_THROUGH`
<a id="insn-00bdace8"></a> `00bdace8` | `ee 04 02 94` | bl 0x00c5c0a0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdacec"></a> `00bdacec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bdacf0"></a> `00bdacf0` | `0c 05 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdacf4"></a> `00bdacf4` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdacf8"></a> `00bdacf8` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdacfc"></a> `00bdacfc` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdad00"></a> `00bdad00` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bdad04"></a> `00bdad04` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdad08"></a> `00bdad08` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00bdad0c"></a> `00bdad0c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdad10"></a> `00bdad10` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00bdad14"></a> `00bdad14` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdad18"></a> `00bdad18` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdad1c"></a> `00bdad1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdad20"></a> `00bdad20` | `02 00 00 14` | b 0x00bdad28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdad24"></a> `00bdad24` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00bdad28"></a> `00bdad28` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bdad2c"></a> `00bdad2c` | `7f 0a 00 b9` | str wzr,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bdad30"></a> `00bdad30` | `7f fe 01 a9` | stp xzr,xzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bdad34"></a> `00bdad34` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bdad38"></a> `00bdad38` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdad3c"></a> `00bdad3c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdad40"></a> `00bdad40` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdad44"></a> `00bdad44` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bdad48"></a> `00bdad48` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdaba8`](#insn-00bdaba8) 範囲 `[['00bdaba8', '00bdabcb']]`
  - `CONDITIONAL_JUMP` [`00bdabc8`](#insn-00bdabc8) → [`00bdac44`](#insn-00bdac44)
  - `FALL_THROUGH` [`00bdabc8`](#insn-00bdabc8) → [`00bdabcc`](#insn-00bdabcc)
- ブロック [`00bdabcc`](#insn-00bdabcc) 範囲 `[['00bdabcc', '00bdabdf']]`
  - `CONDITIONAL_JUMP` [`00bdabdc`](#insn-00bdabdc) → [`00bdabec`](#insn-00bdabec)
  - `FALL_THROUGH` [`00bdabdc`](#insn-00bdabdc) → [`00bdabe0`](#insn-00bdabe0)
- ブロック [`00bdabe0`](#insn-00bdabe0) 範囲 `[['00bdabe0', '00bdabeb']]`
  - `FALL_THROUGH` [`00bdabe8`](#insn-00bdabe8) → [`00bdabec`](#insn-00bdabec)
- ブロック [`00bdabec`](#insn-00bdabec) 範囲 `[['00bdabec', '00bdabf7']]`
  - `FALL_THROUGH` [`00bdabf4`](#insn-00bdabf4) → [`00bdabf8`](#insn-00bdabf8)
- ブロック [`00bdabf8`](#insn-00bdabf8) 範囲 `[['00bdabf8', '00bdabfb']]`
  - `CONDITIONAL_JUMP` [`00bdabf8`](#insn-00bdabf8) → [`00bdac1c`](#insn-00bdac1c)
  - `FALL_THROUGH` [`00bdabf8`](#insn-00bdabf8) → [`00bdabfc`](#insn-00bdabfc)
- ブロック [`00bdabfc`](#insn-00bdabfc) 範囲 `[['00bdabfc', '00bdac03']]`
  - `CONDITIONAL_JUMP` [`00bdac00`](#insn-00bdac00) → [`00bdac60`](#insn-00bdac60)
  - `FALL_THROUGH` [`00bdac00`](#insn-00bdac00) → [`00bdac04`](#insn-00bdac04)
- ブロック [`00bdac04`](#insn-00bdac04) 範囲 `[['00bdac04', '00bdac1b']]`
  - `FALL_THROUGH` [`00bdac18`](#insn-00bdac18) → [`00bdac1c`](#insn-00bdac1c)
- ブロック [`00bdac1c`](#insn-00bdac1c) 範囲 `[['00bdac1c', '00bdac1f']]`
  - `CONDITIONAL_JUMP` [`00bdac1c`](#insn-00bdac1c) → [`00bdac68`](#insn-00bdac68)
  - `FALL_THROUGH` [`00bdac1c`](#insn-00bdac1c) → [`00bdac20`](#insn-00bdac20)
- ブロック [`00bdac20`](#insn-00bdac20) 範囲 `[['00bdac20', '00bdac27']]`
  - `CONDITIONAL_JUMP` [`00bdac24`](#insn-00bdac24) → [`00bdac68`](#insn-00bdac68)
  - `FALL_THROUGH` [`00bdac24`](#insn-00bdac24) → [`00bdac28`](#insn-00bdac28)
- ブロック [`00bdac28`](#insn-00bdac28) 範囲 `[['00bdac28', '00bdac2b']]`
  - `FALL_THROUGH` [`00bdac28`](#insn-00bdac28) → [`00bdac2c`](#insn-00bdac2c)
- ブロック [`00bdac2c`](#insn-00bdac2c) 範囲 `[['00bdac2c', '00bdac37']]`
  - `FALL_THROUGH` [`00bdac34`](#insn-00bdac34) → [`00bdac38`](#insn-00bdac38)
- ブロック [`00bdac38`](#insn-00bdac38) 範囲 `[['00bdac38', '00bdac43']]`
  - `UNCONDITIONAL_JUMP` [`00bdac40`](#insn-00bdac40) → [`00bdac6c`](#insn-00bdac6c)
- ブロック [`00bdac44`](#insn-00bdac44) 範囲 `[['00bdac44', '00bdac53']]`
  - `FALL_THROUGH` [`00bdac50`](#insn-00bdac50) → [`00bdac54`](#insn-00bdac54)
- ブロック [`00bdac54`](#insn-00bdac54) 範囲 `[['00bdac54', '00bdac5f']]`
  - `UNCONDITIONAL_JUMP` [`00bdac5c`](#insn-00bdac5c) → [`00bdad24`](#insn-00bdad24)
- ブロック [`00bdac60`](#insn-00bdac60) 範囲 `[['00bdac60', '00bdac67']]`
  - `CONDITIONAL_JUMP` [`00bdac64`](#insn-00bdac64) → [`00bdac20`](#insn-00bdac20)
  - `FALL_THROUGH` [`00bdac64`](#insn-00bdac64) → [`00bdac68`](#insn-00bdac68)
- ブロック [`00bdac68`](#insn-00bdac68) 範囲 `[['00bdac68', '00bdac6b']]`
  - `FALL_THROUGH` [`00bdac68`](#insn-00bdac68) → [`00bdac6c`](#insn-00bdac6c)
- ブロック [`00bdac6c`](#insn-00bdac6c) 範囲 `[['00bdac6c', '00bdaca3']]`
  - `CONDITIONAL_JUMP` [`00bdaca0`](#insn-00bdaca0) → [`00bdacb8`](#insn-00bdacb8)
  - `FALL_THROUGH` [`00bdaca0`](#insn-00bdaca0) → [`00bdaca4`](#insn-00bdaca4)
- ブロック [`00bdaca4`](#insn-00bdaca4) 範囲 `[['00bdaca4', '00bdacb7']]`
  - `FALL_THROUGH` [`00bdacb4`](#insn-00bdacb4) → [`00bdacb8`](#insn-00bdacb8)
- ブロック [`00bdacb8`](#insn-00bdacb8) 範囲 `[['00bdacb8', '00bdacbb']]`
  - `CONDITIONAL_JUMP` [`00bdacb8`](#insn-00bdacb8) → [`00bdacd0`](#insn-00bdacd0)
  - `FALL_THROUGH` [`00bdacb8`](#insn-00bdacb8) → [`00bdacbc`](#insn-00bdacbc)
- ブロック [`00bdacbc`](#insn-00bdacbc) 範囲 `[['00bdacbc', '00bdaccf']]`
  - `FALL_THROUGH` [`00bdaccc`](#insn-00bdaccc) → [`00bdacd0`](#insn-00bdacd0)
- ブロック [`00bdacd0`](#insn-00bdacd0) 範囲 `[['00bdacd0', '00bdacd3']]`
  - `CONDITIONAL_JUMP` [`00bdacd0`](#insn-00bdacd0) → [`00bdad24`](#insn-00bdad24)
  - `FALL_THROUGH` [`00bdacd0`](#insn-00bdacd0) → [`00bdacd4`](#insn-00bdacd4)
- ブロック [`00bdacd4`](#insn-00bdacd4) 範囲 `[['00bdacd4', '00bdacdf']]`
  - `CONDITIONAL_JUMP` [`00bdacdc`](#insn-00bdacdc) → [`00bdacec`](#insn-00bdacec)
  - `FALL_THROUGH` [`00bdacdc`](#insn-00bdacdc) → [`00bdace0`](#insn-00bdace0)
- ブロック [`00bdace0`](#insn-00bdace0) 範囲 `[['00bdace0', '00bdaceb']]`
  - `FALL_THROUGH` [`00bdace8`](#insn-00bdace8) → [`00bdacec`](#insn-00bdacec)
- ブロック [`00bdacec`](#insn-00bdacec) 範囲 `[['00bdacec', '00bdad23']]`
  - `UNCONDITIONAL_JUMP` [`00bdad20`](#insn-00bdad20) → [`00bdad28`](#insn-00bdad28)
- ブロック [`00bdad24`](#insn-00bdad24) 範囲 `[['00bdad24', '00bdad27']]`
  - `FALL_THROUGH` [`00bdad24`](#insn-00bdad24) → [`00bdad28`](#insn-00bdad28)
- ブロック [`00bdad28`](#insn-00bdad28) 範囲 `[['00bdad28', '00bdad4b']]`

## 命令位置別の参照

- [`00bdaba8`](#insn-00bdaba8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabac`](#insn-00bdabac) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabb0`](#insn-00bdabb0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabb4`](#insn-00bdabb4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabc0`](#insn-00bdabc0) → `01127db8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bdabc8`](#insn-00bdabc8) → [`00bdac44`](#insn-00bdac44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabd4`](#insn-00bdabd4) → [`00c5c300`](../00c5c/00c5c300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c300` · 推定シンボル `None` · 推定型 `None`
- [`00bdabdc`](#insn-00bdabdc) → [`00bdabec`](#insn-00bdabec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdabe4`](#insn-00bdabe4) → `002b2653`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdabe8`](#insn-00bdabe8) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdabf0`](#insn-00bdabf0) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdabf8`](#insn-00bdabf8) → [`00bdac1c`](#insn-00bdac1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac00`](#insn-00bdac00) → [`00bdac60`](#insn-00bdac60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac1c`](#insn-00bdac1c) → [`00bdac68`](#insn-00bdac68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac24`](#insn-00bdac24) → [`00bdac68`](#insn-00bdac68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac40`](#insn-00bdac40) → [`00bdac6c`](#insn-00bdac6c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac48`](#insn-00bdac48) → `002b7f1f`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdac4c`](#insn-00bdac4c) → [`00c5bd40`](../00c5b/00c5bd40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bd40` · 推定シンボル `None` · 推定型 `None`
- [`00bdac54`](#insn-00bdac54) → `00310170`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdac58`](#insn-00bdac58) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdac5c`](#insn-00bdac5c) → [`00bdad24`](#insn-00bdad24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac64`](#insn-00bdac64) → [`00bdac20`](#insn-00bdac20) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdac74`](#insn-00bdac74) → `01127b88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdac78`](#insn-00bdac78) → `01127b98`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdac88`](#insn-00bdac88) → [`00c5bc40`](../00c5b/00c5bc40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc40` · 推定シンボル `None` · 推定型 `None`
- [`00bdac94`](#insn-00bdac94) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bdaca0`](#insn-00bdaca0) → [`00bdacb8`](#insn-00bdacb8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdacb8`](#insn-00bdacb8) → [`00bdacd0`](#insn-00bdacd0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdacd0`](#insn-00bdacd0) → [`00bdad24`](#insn-00bdad24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdacd4`](#insn-00bdacd4) → [`00c5c300`](../00c5c/00c5c300.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c300` · 推定シンボル `None` · 推定型 `None`
- [`00bdacdc`](#insn-00bdacdc) → [`00bdacec`](#insn-00bdacec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdace4`](#insn-00bdace4) → `002b2653`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bdace8`](#insn-00bdace8) → [`00c5c0a0`](../00c5c/00c5c0a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c0a0` · 推定シンボル `None` · 推定型 `None`
- [`00bdacf0`](#insn-00bdacf0) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdad20`](#insn-00bdad20) → [`00bdad28`](#insn-00bdad28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad38`](#insn-00bdad38) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad3c`](#insn-00bdad3c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdad40`](#insn-00bdad40) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdaba8`](#insn-00bdaba8)

~~~json
{
  "source": "00bdaba8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabac`](#insn-00bdabac)

~~~json
{
  "source": "00bdabac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabb0`](#insn-00bdabb0)

~~~json
{
  "source": "00bdabb0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabb4`](#insn-00bdabb4)

~~~json
{
  "source": "00bdabb4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabc0`](#insn-00bdabc0)

~~~json
{
  "source": "00bdabc0",
  "target": "01127db8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127db8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdabc8`](#insn-00bdabc8)

~~~json
{
  "source": "00bdabc8",
  "target": "00bdac44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabd4`](#insn-00bdabd4)

~~~json
{
  "source": "00bdabd4",
  "target": "00c5c300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdabdc`](#insn-00bdabdc)

~~~json
{
  "source": "00bdabdc",
  "target": "00bdabec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdabe4`](#insn-00bdabe4)

~~~json
{
  "source": "00bdabe4",
  "target": "002b2653",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2653",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2653",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdabe8`](#insn-00bdabe8)

~~~json
{
  "source": "00bdabe8",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdabf0`](#insn-00bdabf0)

~~~json
{
  "source": "00bdabf0",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdabf8`](#insn-00bdabf8)

~~~json
{
  "source": "00bdabf8",
  "target": "00bdac1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac00`](#insn-00bdac00)

~~~json
{
  "source": "00bdac00",
  "target": "00bdac60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac1c`](#insn-00bdac1c)

~~~json
{
  "source": "00bdac1c",
  "target": "00bdac68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac24`](#insn-00bdac24)

~~~json
{
  "source": "00bdac24",
  "target": "00bdac68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac40`](#insn-00bdac40)

~~~json
{
  "source": "00bdac40",
  "target": "00bdac6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac48`](#insn-00bdac48)

~~~json
{
  "source": "00bdac48",
  "target": "002b7f1f",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7f1f",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "675f6d6574686f64735f63616368656400",
  "capture_start": "002b7f1f",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdac4c`](#insn-00bdac4c)

~~~json
{
  "source": "00bdac4c",
  "target": "00c5bd40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac54`](#insn-00bdac54)

~~~json
{
  "source": "00bdac54",
  "target": "00310170",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00310170",
  "offset": 0,
  "size": 97,
  "datatype": "string",
  "bytes": "4669726562617365204175746820776173206e6f7420696e697469616c697a65",
  "capture_start": "00310170",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bdac58`](#insn-00bdac58)

~~~json
{
  "source": "00bdac58",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac5c`](#insn-00bdac5c)

~~~json
{
  "source": "00bdac5c",
  "target": "00bdad24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac64`](#insn-00bdac64)

~~~json
{
  "source": "00bdac64",
  "target": "00bdac20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdac74`](#insn-00bdac74)

~~~json
{
  "source": "00bdac74",
  "target": "01127b88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b88",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdac78`](#insn-00bdac78)

~~~json
{
  "source": "00bdac78",
  "target": "01127b98",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127b98",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdac88`](#insn-00bdac88)

~~~json
{
  "source": "00bdac88",
  "target": "00c5bc40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdac94`](#insn-00bdac94)

~~~json
{
  "source": "00bdac94",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdaca0`](#insn-00bdaca0)

~~~json
{
  "source": "00bdaca0",
  "target": "00bdacb8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdacb8`](#insn-00bdacb8)

~~~json
{
  "source": "00bdacb8",
  "target": "00bdacd0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdacd0`](#insn-00bdacd0)

~~~json
{
  "source": "00bdacd0",
  "target": "00bdad24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdacd4`](#insn-00bdacd4)

~~~json
{
  "source": "00bdacd4",
  "target": "00c5c300",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdacdc`](#insn-00bdacdc)

~~~json
{
  "source": "00bdacdc",
  "target": "00bdacec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdace4`](#insn-00bdace4)

~~~json
{
  "source": "00bdace4",
  "target": "002b2653",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2653",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2653",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bdace8`](#insn-00bdace8)

~~~json
{
  "source": "00bdace8",
  "target": "00c5c0a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdacf0`](#insn-00bdacf0)

~~~json
{
  "source": "00bdacf0",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdad20`](#insn-00bdad20)

~~~json
{
  "source": "00bdad20",
  "target": "00bdad28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad38`](#insn-00bdad38)

~~~json
{
  "source": "00bdad38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad3c`](#insn-00bdad3c)

~~~json
{
  "source": "00bdad3c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdad40`](#insn-00bdad40)

~~~json
{
  "source": "00bdad40",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
