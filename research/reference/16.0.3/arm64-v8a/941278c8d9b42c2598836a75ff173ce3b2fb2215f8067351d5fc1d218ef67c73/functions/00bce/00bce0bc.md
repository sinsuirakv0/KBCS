# 00bce0bc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bcd0c8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bcd/00bcd0c8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0081.md#compare-a8c91f69b1a4e5f628bb17800643a355)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bce0bc",
  "name": "_ZN8firebase4auth18CacheAuthMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE",
  "size": 560,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c7b2d6a3c31beef0d422c044a1bb93727e8710579ecbf7c8c7af847d78ef94ab",
  "source_text_sha256": "c7b2d6a3c31beef0d422c044a1bb93727e8710579ecbf7c8c7af847d78ef94ab",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bce0bc",
        "00bce2eb"
      ]
    ],
    "bytes_sha256": "a59d0dcbe2b459c4af4c4ad1563b849bf24fe7a18218204c8da90eb257c11d84",
    "instruction_count": 140,
    "instruction_bytes": 560,
    "body_bytes": 560,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5ece0](../00c5e/00c5ece0.md)

## 呼び出し先

- [00c5bfb0](../00c5b/00c5bfb0.md)
- [00c5bfd0](../00c5b/00c5bfd0.md)
- [00c5c000](../00c5c/00c5c000.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseAuth"
"%PG%com/google/firebase/auth/SignInMethodQueryResult"
"com/google/firebase/auth/internal/cpp/JniAuthStateListener"
"com/google/firebase/auth/internal/cpp/JniIdTokenListener"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 4074 bytes

~~~c

bool _ZN8firebase4auth18CacheAuthMethodIdsEP7_JNIEnvP8_jobjectRKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEE
               (long *param_1,undefined8 param_2,undefined8 param_3)

{
  int iVar1;
  ulong uVar2;
  
  if (DAT_011277e8 == 0) {
                    /* try { // try from 00bce0ec to 00cce0f7 has its CatchHandler @ 00bcfa6c */
                    /* try { // try from 00bce0f8 to 00cce18b has its CatchHandler @ 00bcd634 */
    DAT_011277e8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/FirebaseAuth",0);
  }
  uVar2 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                    (param_1,DAT_011277e8,&PTR_s_getInstance_00c92a28,0x12,&DAT_011277f8,
                     "com/google/firebase/auth/FirebaseAuth");
  if ((uVar2 & 1) != 0) {
    if (DAT_01127890 == 0) {
      DAT_01127890 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                               (param_1,param_2,0,"com/google/firebase/auth/SignInMethodQueryResult"
                                ,0);
    }
    uVar2 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                      (param_1,DAT_01127890,&PTR_s_getSignInMethods_00c92bd8,1,&DAT_011278a0,
                       "com/google/firebase/auth/SignInMethodQueryResult");
                    /* try { // try from 00bce18c to 00cce197 has its CatchHandler @ 00bcfa0c */
                    /* try { // try from 00bce1b4 to 00cce1cf has its CatchHandler @ 00bcfa1c */
                    /* try { // try from 00bce1d0 to 00cce313 has its CatchHandler @ 00bcd634 */
    if ((((uVar2 & 1) != 0) &&
        (((DAT_011278b0 != 0 ||
          (DAT_011278b0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                    (param_1,param_2,param_3,
                                     "com/google/firebase/auth/internal/cpp/JniAuthStateListener",0)
          , DAT_011278b0 != 0)) &&
         (uVar2 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                            (param_1,DAT_011278b0,&PTR_s_<init>_00c92bf0,2,&DAT_011278c0,
                             "com/google/firebase/auth/internal/cpp/JniAuthStateListener"),
         (uVar2 & 1) != 0)))) && (DAT_011278b8 == '\0')) {
      iVar1 = (**(code **)(*param_1 + 0x6b8))
                        (param_1,DAT_011278b0,&PTR_s_nativeOnAuthStateChanged_00c92c50,1);
      _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
      DAT_011278b8 = iVar1 == 0;
      if (((iVar1 == 0) &&
          ((DAT_011278d8 != 0 ||
           (DAT_011278d8 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                     (param_1,param_2,param_3,
                                      "com/google/firebase/auth/internal/cpp/JniIdTokenListener",0),
           DAT_011278d8 != 0)))) &&
         ((uVar2 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                             (param_1,DAT_011278d8,&PTR_s_<init>_00c92c20,2,&DAT_011278e8,
                              "com/google/firebase/auth/internal/cpp/JniIdTokenListener"),
          (uVar2 & 1) != 0 && (DAT_011278e0 == '\0')))) {
        iVar1 = (**(code **)(*param_1 + 0x6b8))
                          (param_1,DAT_011278d8,&PTR_s_nativeOnIdTokenChanged_00c92c68,1);
        _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(param_1);
        DAT_011278e0 = iVar1 == 0;
        return iVar1 == 0;
      }
    }
  }
  return false;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bce0bc"></a> `00bce0bc` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00bce0c0"></a> `00bce0c0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce0c4"></a> `00bce0c4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce0c8"></a> `00bce0c8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bce0cc"></a> `00bce0cc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bce0d0"></a> `00bce0d0` | `d6 2a 00 b0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce0d4"></a> `00bce0d4` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bce0d8"></a> `00bce0d8` | `c1 f6 43 f9` | ldr x1,[x22, #0x7e8] | `FALL_THROUGH`
<a id="insn-00bce0dc"></a> `00bce0dc` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-00bce0e0"></a> `00bce0e0` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bce0e4"></a> `00bce0e4` | `41 01 00 b5` | cbnz x1,0x00bce10c | `CONDITIONAL_JUMP`
<a id="insn-00bce0e8"></a> `00bce0e8` | `e3 b6 ff d0` | adrp x3,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bce0ec"></a> `00bce0ec` | `63 b4 0a 91` | add x3,x3,#0x2ad | `FALL_THROUGH`
<a id="insn-00bce0f0"></a> `00bce0f0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce0f4"></a> `00bce0f4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bce0f8"></a> `00bce0f8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bce0fc"></a> `00bce0fc` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bce100"></a> `00bce100` | `ac 37 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce104"></a> `00bce104` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bce108"></a> `00bce108` | `c0 f6 03 f9` | str x0,[x22, #0x7e8] | `FALL_THROUGH`
<a id="insn-00bce10c"></a> `00bce10c` | `22 06 00 90` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bce110"></a> `00bce110` | `c4 2a 00 b0` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce114"></a> `00bce114` | `e5 b6 ff d0` | adrp x5,0x2ac000 | `FALL_THROUGH`
<a id="insn-00bce118"></a> `00bce118` | `42 a0 28 91` | add x2,x2,#0xa28 | `FALL_THROUGH`
<a id="insn-00bce11c"></a> `00bce11c` | `84 e0 1f 91` | add x4,x4,#0x7f8 | `FALL_THROUGH`
<a id="insn-00bce120"></a> `00bce120` | `a5 b4 0a 91` | add x5,x5,#0x2ad | `FALL_THROUGH`
<a id="insn-00bce124"></a> `00bce124` | `43 02 80 52` | mov w3,#0x12 | `FALL_THROUGH`
<a id="insn-00bce128"></a> `00bce128` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce12c"></a> `00bce12c` | `a9 37 02 94` | bl 0x00c5bfd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce130"></a> `00bce130` | `00 08 00 36` | tbz w0,#0x0,0x00bce230 | `CONDITIONAL_JUMP`
<a id="insn-00bce134"></a> `00bce134` | `d6 2a 00 b0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce138"></a> `00bce138` | `c1 4a 44 f9` | ldr x1,[x22, #0x890] | `FALL_THROUGH`
<a id="insn-00bce13c"></a> `00bce13c` | `41 01 00 b5` | cbnz x1,0x00bce164 | `CONDITIONAL_JUMP`
<a id="insn-00bce140"></a> `00bce140` | `a3 b6 ff 90` | adrp x3,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bce144"></a> `00bce144` | `63 00 35 91` | add x3,x3,#0xd40 | `FALL_THROUGH`
<a id="insn-00bce148"></a> `00bce148` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce14c"></a> `00bce14c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bce150"></a> `00bce150` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bce154"></a> `00bce154` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bce158"></a> `00bce158` | `96 37 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce15c"></a> `00bce15c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bce160"></a> `00bce160` | `c0 4a 04 f9` | str x0,[x22, #0x890] | `FALL_THROUGH`
<a id="insn-00bce164"></a> `00bce164` | `22 06 00 90` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bce168"></a> `00bce168` | `c4 2a 00 b0` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce16c"></a> `00bce16c` | `a5 b6 ff 90` | adrp x5,0x2a2000 | `FALL_THROUGH`
<a id="insn-00bce170"></a> `00bce170` | `42 60 2f 91` | add x2,x2,#0xbd8 | `FALL_THROUGH`
<a id="insn-00bce174"></a> `00bce174` | `84 80 22 91` | add x4,x4,#0x8a0 | `FALL_THROUGH`
<a id="insn-00bce178"></a> `00bce178` | `a5 00 35 91` | add x5,x5,#0xd40 | `FALL_THROUGH`
<a id="insn-00bce17c"></a> `00bce17c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bce180"></a> `00bce180` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce184"></a> `00bce184` | `93 37 02 94` | bl 0x00c5bfd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce188"></a> `00bce188` | `40 05 00 36` | tbz w0,#0x0,0x00bce230 | `CONDITIONAL_JUMP`
<a id="insn-00bce18c"></a> `00bce18c` | `d6 2a 00 b0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce190"></a> `00bce190` | `c1 5a 44 f9` | ldr x1,[x22, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bce194"></a> `00bce194` | `61 01 00 b5` | cbnz x1,0x00bce1c0 | `CONDITIONAL_JUMP`
<a id="insn-00bce198"></a> `00bce198` | `23 b7 ff f0` | adrp x3,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bce19c"></a> `00bce19c` | `63 a4 33 91` | add x3,x3,#0xce9 | `FALL_THROUGH`
<a id="insn-00bce1a0"></a> `00bce1a0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce1a4"></a> `00bce1a4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bce1a8"></a> `00bce1a8` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bce1ac"></a> `00bce1ac` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bce1b0"></a> `00bce1b0` | `80 37 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce1b4"></a> `00bce1b4` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bce1b8"></a> `00bce1b8` | `c0 5a 04 f9` | str x0,[x22, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bce1bc"></a> `00bce1bc` | `a0 03 00 b4` | cbz x0,0x00bce230 | `CONDITIONAL_JUMP`
<a id="insn-00bce1c0"></a> `00bce1c0` | `22 06 00 90` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bce1c4"></a> `00bce1c4` | `c4 2a 00 b0` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce1c8"></a> `00bce1c8` | `25 b7 ff f0` | adrp x5,0x2b5000 | `FALL_THROUGH`
<a id="insn-00bce1cc"></a> `00bce1cc` | `42 c0 2f 91` | add x2,x2,#0xbf0 | `FALL_THROUGH`
<a id="insn-00bce1d0"></a> `00bce1d0` | `84 00 23 91` | add x4,x4,#0x8c0 | `FALL_THROUGH`
<a id="insn-00bce1d4"></a> `00bce1d4` | `a5 a4 33 91` | add x5,x5,#0xce9 | `FALL_THROUGH`
<a id="insn-00bce1d8"></a> `00bce1d8` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00bce1dc"></a> `00bce1dc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce1e0"></a> `00bce1e0` | `7c 37 02 94` | bl 0x00c5bfd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce1e4"></a> `00bce1e4` | `60 02 00 36` | tbz w0,#0x0,0x00bce230 | `CONDITIONAL_JUMP`
<a id="insn-00bce1e8"></a> `00bce1e8` | `d7 2a 00 b0` | adrp x23,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce1ec"></a> `00bce1ec` | `e8 e2 62 39` | ldrb w8,[x23, #0x8b8] | `FALL_THROUGH`
<a id="insn-00bce1f0"></a> `00bce1f0` | `08 02 00 35` | cbnz w8,0x00bce230 | `CONDITIONAL_JUMP`
<a id="insn-00bce1f4"></a> `00bce1f4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bce1f8"></a> `00bce1f8` | `c1 5a 44 f9` | ldr x1,[x22, #0x8b0] | `FALL_THROUGH`
<a id="insn-00bce1fc"></a> `00bce1fc` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bce200"></a> `00bce200` | `82 52 62 10` | adr x2,0xc92c50 | `FALL_THROUGH`
<a id="insn-00bce204"></a> `00bce204` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bce208"></a> `00bce208` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bce20c"></a> `00bce20c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce210"></a> `00bce210` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce214"></a> `00bce214` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-00bce218"></a> `00bce218` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce21c"></a> `00bce21c` | `79 37 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bce220"></a> `00bce220` | `df 02 00 71` | cmp w22,#0x0 | `FALL_THROUGH`
<a id="insn-00bce224"></a> `00bce224` | `e8 17 9f 1a` | cset w8,eq | `FALL_THROUGH`
<a id="insn-00bce228"></a> `00bce228` | `e8 e2 22 39` | strb w8,[x23, #0x8b8] | `FALL_THROUGH`
<a id="insn-00bce22c"></a> `00bce22c` | `f6 00 00 34` | cbz w22,0x00bce248 | `CONDITIONAL_JUMP`
<a id="insn-00bce230"></a> `00bce230` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bce234"></a> `00bce234` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bce238"></a> `00bce238` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bce23c"></a> `00bce23c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bce240"></a> `00bce240` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00bce244"></a> `00bce244` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bce248"></a> `00bce248` | `d6 2a 00 b0` | adrp x22,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce24c"></a> `00bce24c` | `c1 6e 44 f9` | ldr x1,[x22, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bce250"></a> `00bce250` | `61 01 00 b5` | cbnz x1,0x00bce27c | `CONDITIONAL_JUMP`
<a id="insn-00bce254"></a> `00bce254` | `e3 b6 ff 90` | adrp x3,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bce258"></a> `00bce258` | `63 ec 27 91` | add x3,x3,#0x9fb | `FALL_THROUGH`
<a id="insn-00bce25c"></a> `00bce25c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce260"></a> `00bce260` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bce264"></a> `00bce264` | `e2 03 14 aa` | mov x2,x20 | `FALL_THROUGH`
<a id="insn-00bce268"></a> `00bce268` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bce26c"></a> `00bce26c` | `51 37 02 94` | bl 0x00c5bfb0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce270"></a> `00bce270` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bce274"></a> `00bce274` | `c0 6e 04 f9` | str x0,[x22, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bce278"></a> `00bce278` | `c0 fd ff b4` | cbz x0,0x00bce230 | `CONDITIONAL_JUMP`
<a id="insn-00bce27c"></a> `00bce27c` | `22 06 00 90` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bce280"></a> `00bce280` | `c4 2a 00 b0` | adrp x4,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce284"></a> `00bce284` | `e5 b6 ff 90` | adrp x5,0x2aa000 | `FALL_THROUGH`
<a id="insn-00bce288"></a> `00bce288` | `42 80 30 91` | add x2,x2,#0xc20 | `FALL_THROUGH`
<a id="insn-00bce28c"></a> `00bce28c` | `84 a0 23 91` | add x4,x4,#0x8e8 | `FALL_THROUGH`
<a id="insn-00bce290"></a> `00bce290` | `a5 ec 27 91` | add x5,x5,#0x9fb | `FALL_THROUGH`
<a id="insn-00bce294"></a> `00bce294` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00bce298"></a> `00bce298` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce29c"></a> `00bce29c` | `4d 37 02 94` | bl 0x00c5bfd0 | `UNCONDITIONAL_CALL`
<a id="insn-00bce2a0"></a> `00bce2a0` | `80 fc 07 36` | tbz w0,#0x0,0x00bce230 | `CONDITIONAL_JUMP`
<a id="insn-00bce2a4"></a> `00bce2a4` | `d5 2a 00 b0` | adrp x21,0x1127000 | `FALL_THROUGH`
<a id="insn-00bce2a8"></a> `00bce2a8` | `a8 82 63 39` | ldrb w8,[x21, #0x8e0] | `FALL_THROUGH`
<a id="insn-00bce2ac"></a> `00bce2ac` | `28 fc ff 35` | cbnz w8,0x00bce230 | `CONDITIONAL_JUMP`
<a id="insn-00bce2b0"></a> `00bce2b0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bce2b4"></a> `00bce2b4` | `c1 6e 44 f9` | ldr x1,[x22, #0x8d8] | `FALL_THROUGH`
<a id="insn-00bce2b8"></a> `00bce2b8` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00bce2bc"></a> `00bce2bc` | `62 4d 62 10` | adr x2,0xc92c68 | `FALL_THROUGH`
<a id="insn-00bce2c0"></a> `00bce2c0` | `08 5d 43 f9` | ldr x8,[x8, #0x6b8] | `FALL_THROUGH`
<a id="insn-00bce2c4"></a> `00bce2c4` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bce2c8"></a> `00bce2c8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce2cc"></a> `00bce2cc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bce2d0"></a> `00bce2d0` | `f4 03 00 2a` | mov w20,w0 | `FALL_THROUGH`
<a id="insn-00bce2d4"></a> `00bce2d4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bce2d8"></a> `00bce2d8` | `4a 37 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bce2dc"></a> `00bce2dc` | `9f 02 00 71` | cmp w20,#0x0 | `FALL_THROUGH`
<a id="insn-00bce2e0"></a> `00bce2e0` | `e0 17 9f 1a` | cset w0,eq | `FALL_THROUGH`
<a id="insn-00bce2e4"></a> `00bce2e4` | `a0 82 23 39` | strb w0,[x21, #0x8e0] | `FALL_THROUGH`
<a id="insn-00bce2e8"></a> `00bce2e8` | `d3 ff ff 17` | b 0x00bce234 | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bce0bc`](#insn-00bce0bc) 範囲 `[['00bce0bc', '00bce0e7']]`
  - `CONDITIONAL_JUMP` [`00bce0e4`](#insn-00bce0e4) → [`00bce10c`](#insn-00bce10c)
  - `FALL_THROUGH` [`00bce0e4`](#insn-00bce0e4) → [`00bce0e8`](#insn-00bce0e8)
- ブロック [`00bce0e8`](#insn-00bce0e8) 範囲 `[['00bce0e8', '00bce0eb']]`
  - `FALL_THROUGH` [`00bce0e8`](#insn-00bce0e8) → [`00bce0ec`](#insn-00bce0ec)
- ブロック [`00bce0ec`](#insn-00bce0ec) 範囲 `[['00bce0ec', '00bce0f7']]`
  - `FALL_THROUGH` [`00bce0f4`](#insn-00bce0f4) → [`00bce0f8`](#insn-00bce0f8)
- ブロック [`00bce0f8`](#insn-00bce0f8) 範囲 `[['00bce0f8', '00bce10b']]`
  - `FALL_THROUGH` [`00bce108`](#insn-00bce108) → [`00bce10c`](#insn-00bce10c)
- ブロック [`00bce10c`](#insn-00bce10c) 範囲 `[['00bce10c', '00bce133']]`
  - `CONDITIONAL_JUMP` [`00bce130`](#insn-00bce130) → [`00bce230`](#insn-00bce230)
  - `FALL_THROUGH` [`00bce130`](#insn-00bce130) → [`00bce134`](#insn-00bce134)
- ブロック [`00bce134`](#insn-00bce134) 範囲 `[['00bce134', '00bce13f']]`
  - `CONDITIONAL_JUMP` [`00bce13c`](#insn-00bce13c) → [`00bce164`](#insn-00bce164)
  - `FALL_THROUGH` [`00bce13c`](#insn-00bce13c) → [`00bce140`](#insn-00bce140)
- ブロック [`00bce140`](#insn-00bce140) 範囲 `[['00bce140', '00bce163']]`
  - `FALL_THROUGH` [`00bce160`](#insn-00bce160) → [`00bce164`](#insn-00bce164)
- ブロック [`00bce164`](#insn-00bce164) 範囲 `[['00bce164', '00bce18b']]`
  - `CONDITIONAL_JUMP` [`00bce188`](#insn-00bce188) → [`00bce230`](#insn-00bce230)
  - `FALL_THROUGH` [`00bce188`](#insn-00bce188) → [`00bce18c`](#insn-00bce18c)
- ブロック [`00bce18c`](#insn-00bce18c) 範囲 `[['00bce18c', '00bce197']]`
  - `CONDITIONAL_JUMP` [`00bce194`](#insn-00bce194) → [`00bce1c0`](#insn-00bce1c0)
  - `FALL_THROUGH` [`00bce194`](#insn-00bce194) → [`00bce198`](#insn-00bce198)
- ブロック [`00bce198`](#insn-00bce198) 範囲 `[['00bce198', '00bce1b3']]`
  - `FALL_THROUGH` [`00bce1b0`](#insn-00bce1b0) → [`00bce1b4`](#insn-00bce1b4)
- ブロック [`00bce1b4`](#insn-00bce1b4) 範囲 `[['00bce1b4', '00bce1bf']]`
  - `CONDITIONAL_JUMP` [`00bce1bc`](#insn-00bce1bc) → [`00bce230`](#insn-00bce230)
  - `FALL_THROUGH` [`00bce1bc`](#insn-00bce1bc) → [`00bce1c0`](#insn-00bce1c0)
- ブロック [`00bce1c0`](#insn-00bce1c0) 範囲 `[['00bce1c0', '00bce1cf']]`
  - `FALL_THROUGH` [`00bce1cc`](#insn-00bce1cc) → [`00bce1d0`](#insn-00bce1d0)
- ブロック [`00bce1d0`](#insn-00bce1d0) 範囲 `[['00bce1d0', '00bce1e7']]`
  - `CONDITIONAL_JUMP` [`00bce1e4`](#insn-00bce1e4) → [`00bce230`](#insn-00bce230)
  - `FALL_THROUGH` [`00bce1e4`](#insn-00bce1e4) → [`00bce1e8`](#insn-00bce1e8)
- ブロック [`00bce1e8`](#insn-00bce1e8) 範囲 `[['00bce1e8', '00bce1f3']]`
  - `CONDITIONAL_JUMP` [`00bce1f0`](#insn-00bce1f0) → [`00bce230`](#insn-00bce230)
  - `FALL_THROUGH` [`00bce1f0`](#insn-00bce1f0) → [`00bce1f4`](#insn-00bce1f4)
- ブロック [`00bce1f4`](#insn-00bce1f4) 範囲 `[['00bce1f4', '00bce22f']]`
  - `CONDITIONAL_JUMP` [`00bce22c`](#insn-00bce22c) → [`00bce248`](#insn-00bce248)
  - `FALL_THROUGH` [`00bce22c`](#insn-00bce22c) → [`00bce230`](#insn-00bce230)
- ブロック [`00bce230`](#insn-00bce230) 範囲 `[['00bce230', '00bce233']]`
  - `FALL_THROUGH` [`00bce230`](#insn-00bce230) → [`00bce234`](#insn-00bce234)
- ブロック [`00bce234`](#insn-00bce234) 範囲 `[['00bce234', '00bce247']]`
- ブロック [`00bce248`](#insn-00bce248) 範囲 `[['00bce248', '00bce253']]`
  - `CONDITIONAL_JUMP` [`00bce250`](#insn-00bce250) → [`00bce27c`](#insn-00bce27c)
  - `FALL_THROUGH` [`00bce250`](#insn-00bce250) → [`00bce254`](#insn-00bce254)
- ブロック [`00bce254`](#insn-00bce254) 範囲 `[['00bce254', '00bce27b']]`
  - `CONDITIONAL_JUMP` [`00bce278`](#insn-00bce278) → [`00bce230`](#insn-00bce230)
  - `FALL_THROUGH` [`00bce278`](#insn-00bce278) → [`00bce27c`](#insn-00bce27c)
- ブロック [`00bce27c`](#insn-00bce27c) 範囲 `[['00bce27c', '00bce2a3']]`
  - `CONDITIONAL_JUMP` [`00bce2a0`](#insn-00bce2a0) → [`00bce230`](#insn-00bce230)
  - `FALL_THROUGH` [`00bce2a0`](#insn-00bce2a0) → [`00bce2a4`](#insn-00bce2a4)
- ブロック [`00bce2a4`](#insn-00bce2a4) 範囲 `[['00bce2a4', '00bce2af']]`
  - `CONDITIONAL_JUMP` [`00bce2ac`](#insn-00bce2ac) → [`00bce230`](#insn-00bce230)
  - `FALL_THROUGH` [`00bce2ac`](#insn-00bce2ac) → [`00bce2b0`](#insn-00bce2b0)
- ブロック [`00bce2b0`](#insn-00bce2b0) 範囲 `[['00bce2b0', '00bce2eb']]`
  - `UNCONDITIONAL_JUMP` [`00bce2e8`](#insn-00bce2e8) → [`00bce234`](#insn-00bce234)

## 命令位置別の参照

- [`00bce0bc`](#insn-00bce0bc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0c0`](#insn-00bce0c0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0c4`](#insn-00bce0c4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0c8`](#insn-00bce0c8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0d8`](#insn-00bce0d8) → `011277e8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce0e4`](#insn-00bce0e4) → [`00bce10c`](#insn-00bce10c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce0ec`](#insn-00bce0ec) → `002ac2ad`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bce100`](#insn-00bce100) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bce108`](#insn-00bce108) → `011277e8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce118`](#insn-00bce118) → `00c92a28`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bce11c`](#insn-00bce11c) → `011277f8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce120`](#insn-00bce120) → `002ac2ad`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bce12c`](#insn-00bce12c) → [`00c5bfd0`](../00c5b/00c5bfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfd0` · 推定シンボル `None` · 推定型 `None`
- [`00bce130`](#insn-00bce130) → [`00bce230`](#insn-00bce230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce138`](#insn-00bce138) → `01127890`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce13c`](#insn-00bce13c) → [`00bce164`](#insn-00bce164) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce144`](#insn-00bce144) → `002a2d40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bce158`](#insn-00bce158) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bce160`](#insn-00bce160) → `01127890`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce170`](#insn-00bce170) → `00c92bd8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bce174`](#insn-00bce174) → `011278a0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce178`](#insn-00bce178) → `002a2d40`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bce184`](#insn-00bce184) → [`00c5bfd0`](../00c5b/00c5bfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfd0` · 推定シンボル `None` · 推定型 `None`
- [`00bce188`](#insn-00bce188) → [`00bce230`](#insn-00bce230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce190`](#insn-00bce190) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce194`](#insn-00bce194) → [`00bce1c0`](#insn-00bce1c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce19c`](#insn-00bce19c) → `002b5ce9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bce1b0`](#insn-00bce1b0) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bce1b8`](#insn-00bce1b8) → `011278b0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce1bc`](#insn-00bce1bc) → [`00bce230`](#insn-00bce230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce1cc`](#insn-00bce1cc) → `00c92bf0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bce1d0`](#insn-00bce1d0) → `011278c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce1d4`](#insn-00bce1d4) → `002b5ce9`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bce1e0`](#insn-00bce1e0) → [`00c5bfd0`](../00c5b/00c5bfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfd0` · 推定シンボル `None` · 推定型 `None`
- [`00bce1e4`](#insn-00bce1e4) → [`00bce230`](#insn-00bce230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce1ec`](#insn-00bce1ec) → `011278b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce1f0`](#insn-00bce1f0) → [`00bce230`](#insn-00bce230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce1f8`](#insn-00bce1f8) → `011278b0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce200`](#insn-00bce200) → `00c92c50`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bce21c`](#insn-00bce21c) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bce228`](#insn-00bce228) → `011278b8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce22c`](#insn-00bce22c) → [`00bce248`](#insn-00bce248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce234`](#insn-00bce234) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce238`](#insn-00bce238) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce23c`](#insn-00bce23c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce24c`](#insn-00bce24c) → `011278d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce250`](#insn-00bce250) → [`00bce27c`](#insn-00bce27c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce258`](#insn-00bce258) → `002aa9fb`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bce26c`](#insn-00bce26c) → [`00c5bfb0`](../00c5b/00c5bfb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfb0` · 推定シンボル `None` · 推定型 `None`
- [`00bce274`](#insn-00bce274) → `011278d8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce278`](#insn-00bce278) → [`00bce230`](#insn-00bce230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce288`](#insn-00bce288) → `00c92c20`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bce28c`](#insn-00bce28c) → `011278e8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce290`](#insn-00bce290) → `002aa9fb`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bce29c`](#insn-00bce29c) → [`00c5bfd0`](../00c5b/00c5bfd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bfd0` · 推定シンボル `None` · 推定型 `None`
- [`00bce2a0`](#insn-00bce2a0) → [`00bce230`](#insn-00bce230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce2a8`](#insn-00bce2a8) → `011278e0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce2ac`](#insn-00bce2ac) → [`00bce230`](#insn-00bce230) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bce2b4`](#insn-00bce2b4) → `011278d8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bce2bc`](#insn-00bce2bc) → `00c92c68`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined *`
- [`00bce2d8`](#insn-00bce2d8) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bce2e4`](#insn-00bce2e4) → `011278e0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bce2e8`](#insn-00bce2e8) → [`00bce234`](#insn-00bce234) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bce0bc`](#insn-00bce0bc)

~~~json
{
  "source": "00bce0bc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0c0`](#insn-00bce0c0)

~~~json
{
  "source": "00bce0c0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0c4`](#insn-00bce0c4)

~~~json
{
  "source": "00bce0c4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0c8`](#insn-00bce0c8)

~~~json
{
  "source": "00bce0c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0d8`](#insn-00bce0d8)

~~~json
{
  "source": "00bce0d8",
  "target": "011277e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce0e4`](#insn-00bce0e4)

~~~json
{
  "source": "00bce0e4",
  "target": "00bce10c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce0ec`](#insn-00bce0ec)

~~~json
{
  "source": "00bce0ec",
  "target": "002ac2ad",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac2a9",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002ac2a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bce100`](#insn-00bce100)

~~~json
{
  "source": "00bce100",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce108`](#insn-00bce108)

~~~json
{
  "source": "00bce108",
  "target": "011277e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce118`](#insn-00bce118)

~~~json
{
  "source": "00bce118",
  "target": "00c92a28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92a28",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bce11c`](#insn-00bce11c)

~~~json
{
  "source": "00bce11c",
  "target": "011277f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011277f8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce120`](#insn-00bce120)

~~~json
{
  "source": "00bce120",
  "target": "002ac2ad",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac2a9",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002ac2a9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bce12c`](#insn-00bce12c)

~~~json
{
  "source": "00bce12c",
  "target": "00c5bfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce130`](#insn-00bce130)

~~~json
{
  "source": "00bce130",
  "target": "00bce230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce138`](#insn-00bce138)

~~~json
{
  "source": "00bce138",
  "target": "01127890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127890",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce13c`](#insn-00bce13c)

~~~json
{
  "source": "00bce13c",
  "target": "00bce164",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce144`](#insn-00bce144)

~~~json
{
  "source": "00bce144",
  "target": "002a2d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2d3c",
  "offset": 4,
  "size": 53,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f536967",
  "capture_start": "002a2d3c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bce158`](#insn-00bce158)

~~~json
{
  "source": "00bce158",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce160`](#insn-00bce160)

~~~json
{
  "source": "00bce160",
  "target": "01127890",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127890",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce170`](#insn-00bce170)

~~~json
{
  "source": "00bce170",
  "target": "00c92bd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92bd8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bce174`](#insn-00bce174)

~~~json
{
  "source": "00bce174",
  "target": "011278a0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278a0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce178`](#insn-00bce178)

~~~json
{
  "source": "00bce178",
  "target": "002a2d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a2d3c",
  "offset": 4,
  "size": 53,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f536967",
  "capture_start": "002a2d3c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bce184`](#insn-00bce184)

~~~json
{
  "source": "00bce184",
  "target": "00c5bfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce188`](#insn-00bce188)

~~~json
{
  "source": "00bce188",
  "target": "00bce230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce190`](#insn-00bce190)

~~~json
{
  "source": "00bce190",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce194`](#insn-00bce194)

~~~json
{
  "source": "00bce194",
  "target": "00bce1c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce19c`](#insn-00bce19c)

~~~json
{
  "source": "00bce19c",
  "target": "002b5ce9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5ce9",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5ce9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bce1b0`](#insn-00bce1b0)

~~~json
{
  "source": "00bce1b0",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce1b8`](#insn-00bce1b8)

~~~json
{
  "source": "00bce1b8",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce1bc`](#insn-00bce1bc)

~~~json
{
  "source": "00bce1bc",
  "target": "00bce230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce1cc`](#insn-00bce1cc)

~~~json
{
  "source": "00bce1cc",
  "target": "00c92bf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92bf0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bce1d0`](#insn-00bce1d0)

~~~json
{
  "source": "00bce1d0",
  "target": "011278c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce1d4`](#insn-00bce1d4)

~~~json
{
  "source": "00bce1d4",
  "target": "002b5ce9",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b5ce9",
  "offset": 0,
  "size": 59,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002b5ce9",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bce1e0`](#insn-00bce1e0)

~~~json
{
  "source": "00bce1e0",
  "target": "00c5bfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce1e4`](#insn-00bce1e4)

~~~json
{
  "source": "00bce1e4",
  "target": "00bce230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce1ec`](#insn-00bce1ec)

~~~json
{
  "source": "00bce1ec",
  "target": "011278b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce1f0`](#insn-00bce1f0)

~~~json
{
  "source": "00bce1f0",
  "target": "00bce230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce1f8`](#insn-00bce1f8)

~~~json
{
  "source": "00bce1f8",
  "target": "011278b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce200`](#insn-00bce200)

~~~json
{
  "source": "00bce200",
  "target": "00c92c50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92c50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bce21c`](#insn-00bce21c)

~~~json
{
  "source": "00bce21c",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce228`](#insn-00bce228)

~~~json
{
  "source": "00bce228",
  "target": "011278b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278b8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce22c`](#insn-00bce22c)

~~~json
{
  "source": "00bce22c",
  "target": "00bce248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce234`](#insn-00bce234)

~~~json
{
  "source": "00bce234",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce238`](#insn-00bce238)

~~~json
{
  "source": "00bce238",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce23c`](#insn-00bce23c)

~~~json
{
  "source": "00bce23c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce24c`](#insn-00bce24c)

~~~json
{
  "source": "00bce24c",
  "target": "011278d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce250`](#insn-00bce250)

~~~json
{
  "source": "00bce250",
  "target": "00bce27c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce258`](#insn-00bce258)

~~~json
{
  "source": "00bce258",
  "target": "002aa9fb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa9fb",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa9fb",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bce26c`](#insn-00bce26c)

~~~json
{
  "source": "00bce26c",
  "target": "00c5bfb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce274`](#insn-00bce274)

~~~json
{
  "source": "00bce274",
  "target": "011278d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce278`](#insn-00bce278)

~~~json
{
  "source": "00bce278",
  "target": "00bce230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce288`](#insn-00bce288)

~~~json
{
  "source": "00bce288",
  "target": "00c92c20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92c20",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bce28c`](#insn-00bce28c)

~~~json
{
  "source": "00bce28c",
  "target": "011278e8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278e8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce290`](#insn-00bce290)

~~~json
{
  "source": "00bce290",
  "target": "002aa9fb",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002aa9fb",
  "offset": 0,
  "size": 57,
  "datatype": "string",
  "bytes": "636f6d2f676f6f676c652f66697265626173652f617574682f696e7465726e61",
  "capture_start": "002aa9fb",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bce29c`](#insn-00bce29c)

~~~json
{
  "source": "00bce29c",
  "target": "00c5bfd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce2a0`](#insn-00bce2a0)

~~~json
{
  "source": "00bce2a0",
  "target": "00bce230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce2a8`](#insn-00bce2a8)

~~~json
{
  "source": "00bce2a8",
  "target": "011278e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce2ac`](#insn-00bce2ac)

~~~json
{
  "source": "00bce2ac",
  "target": "00bce230",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bce2b4`](#insn-00bce2b4)

~~~json
{
  "source": "00bce2b4",
  "target": "011278d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278d8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce2bc`](#insn-00bce2bc)

~~~json
{
  "source": "00bce2bc",
  "target": "00c92c68",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92c68",
  "offset": 0,
  "size": 8,
  "datatype": "undefined *",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bce2d8`](#insn-00bce2d8)

~~~json
{
  "source": "00bce2d8",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bce2e4`](#insn-00bce2e4)

~~~json
{
  "source": "00bce2e4",
  "target": "011278e0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011278e0",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bce2e8`](#insn-00bce2e8)

~~~json
{
  "source": "00bce2e8",
  "target": "00bce234",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
