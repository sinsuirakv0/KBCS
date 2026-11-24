# 00bddf1c

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdde80`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdd/00bdde80.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-b08f3ad841ff2b04db7243c32c330925)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdef10`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bde/00bdef10.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-81b8c594ec11562e0c521e3d151b3e67)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bddf1c",
  "name": "_ZN8firebase4auth18CacheUserMethodIdsEP7_JNIEnvP8_jobject",
  "size": 492,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a70ec06841dbfc28923713cede09460112dd683678d829c96f28d336edfd2f74",
  "source_text_sha256": "a70ec06841dbfc28923713cede09460112dd683678d829c96f28d336edfd2f74",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bddf1c",
        "00bde107"
      ]
    ],
    "bytes_sha256": "17078c24af52e7e9094fe6896f9a0ecaae4f96e639d1403fba14cc7e66f64130",
    "instruction_count": 123,
    "instruction_bytes": 492,
    "body_bytes": 492,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5dd20](../00c5d/00c5dd20.md)

## 呼び出し先

- [00c5afe0](../00c5a/00c5afe0.md)
- [00c5b000](../00c5b/00c5b000.md)

## 関連文字列（未確認候補）

~~~text
"%PG%com/google/firebase/auth/FirebaseUser"
"%PG%com/google/firebase/auth/FirebaseUserMetadata"
"%PG%com/google/firebase/auth/GetTokenResult"
"%PG%com/google/firebase/auth/UserInfo"
"%PG%com/google/firebase/auth/UserProfileChangeRequest$Builder"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3374 bytes

~~~c

undefined8
_ZN8firebase4auth18CacheUserMethodIdsEP7_JNIEnvP8_jobject(undefined8 param_1,undefined8 param_2)

{
  ulong uVar1;
  undefined8 uVar2;
  
  if (DAT_01126e00 == 0) {
    DAT_01126e00 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                             (param_1,param_2,0,"com/google/firebase/auth/GetTokenResult",0);
  }
  uVar1 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                    (param_1,DAT_01126e00,&PTR_s_getToken_00c926b0,1,&DAT_01126e10,
                     "com/google/firebase/auth/GetTokenResult");
  if ((uVar1 & 1) != 0) {
    if (DAT_01126e20 == 0) {
      DAT_01126e20 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                               (param_1,param_2,0,"com/google/firebase/auth/FirebaseUser",0);
    }
    uVar1 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                      (param_1,DAT_01126e20,&PTR_s_isAnonymous_00c926c8,0xf,&DAT_01126e30,
                       "com/google/firebase/auth/FirebaseUser");
    if ((uVar1 & 1) != 0) {
      if (DAT_01126eb0 == 0) {
        DAT_01126eb0 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                 (param_1,param_2,0,"com/google/firebase/auth/UserInfo",0);
      }
      uVar1 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                        (param_1,DAT_01126eb0,&PTR_s_getUid_00c92830,7,&DAT_01126ec0,
                         "com/google/firebase/auth/UserInfo");
      if ((uVar1 & 1) != 0) {
        if (DAT_01126f00 == 0) {
          DAT_01126f00 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                   (param_1,param_2,0,
                                    "com/google/firebase/auth/FirebaseUserMetadata",0);
        }
        uVar1 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                          (param_1,DAT_01126f00,&PTR_s_getLastSignInTimestamp_00c928d8,2,
                           &DAT_01126f10,"com/google/firebase/auth/FirebaseUserMetadata");
        if ((uVar1 & 1) != 0) {
          if (DAT_01126f28 == 0) {
            DAT_01126f28 = _ZN8firebase4util15FindClassGlobalEP7_JNIEnvP8_jobjectPKNSt6__ndk16vectorINS_8internal12EmbeddedFileENS5_9allocatorIS8_EEEEPKcNS0_16ClassRequirementE
                                     (param_1,param_2,0,
                                      "com/google/firebase/auth/UserProfileChangeRequest$Builder",0)
            ;
          }
          uVar2 = _ZN8firebase4util15LookupMethodIdsEP7_JNIEnvP7_jclassPKNS0_19MethodNameSignatureEmPP10_jmethodIDPKc
                            (param_1,DAT_01126f28,&PTR_s_<init>_00c92908,4,&DAT_01126f38,
                             "com/google/firebase/auth/UserProfileChangeRequest$Builder");
          return uVar2;
        }
      }
    }
  }
  return 0;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bddf1c"></a> `00bddf1c` | `f5 0f 1d f8` | str x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00bddf20"></a> `00bddf20` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bddf24"></a> `00bddf24` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bddf28"></a> `00bddf28` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00bddf2c"></a> `00bddf2c` | `55 2a 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddf30"></a> `00bddf30` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bddf34"></a> `00bddf34` | `a1 02 47 f9` | ldr x1,[x21, #0xe00] | `FALL_THROUGH`
<a id="insn-00bddf38"></a> `00bddf38` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bddf3c"></a> `00bddf3c` | `41 01 00 b5` | cbnz x1,0x00bddf64 | `CONDITIONAL_JUMP`
<a id="insn-00bddf40"></a> `00bddf40` | `e3 b6 ff f0` | adrp x3,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bddf44"></a> `00bddf44` | `63 f0 07 91` | add x3,x3,#0x1fc | `FALL_THROUGH`
<a id="insn-00bddf48"></a> `00bddf48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddf4c"></a> `00bddf4c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bddf50"></a> `00bddf50` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bddf54"></a> `00bddf54` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bddf58"></a> `00bddf58` | `22 f4 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddf5c"></a> `00bddf5c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bddf60"></a> `00bddf60` | `a0 02 07 f9` | str x0,[x21, #0xe00] | `FALL_THROUGH`
<a id="insn-00bddf64"></a> `00bddf64` | `a2 05 00 b0` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bddf68"></a> `00bddf68` | `44 2a 00 b0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddf6c"></a> `00bddf6c` | `e5 b6 ff f0` | adrp x5,0x2bc000 | `FALL_THROUGH`
<a id="insn-00bddf70"></a> `00bddf70` | `42 c0 1a 91` | add x2,x2,#0x6b0 | `FALL_THROUGH`
<a id="insn-00bddf74"></a> `00bddf74` | `84 40 38 91` | add x4,x4,#0xe10 | `FALL_THROUGH`
<a id="insn-00bddf78"></a> `00bddf78` | `a5 f0 07 91` | add x5,x5,#0x1fc | `FALL_THROUGH`
<a id="insn-00bddf7c"></a> `00bddf7c` | `23 00 80 52` | mov w3,#0x1 | `FALL_THROUGH`
<a id="insn-00bddf80"></a> `00bddf80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddf84"></a> `00bddf84` | `1f f4 01 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bddf88"></a> `00bddf88` | `60 0b 00 36` | tbz w0,#0x0,0x00bde0f4 | `CONDITIONAL_JUMP`
<a id="insn-00bddf8c"></a> `00bddf8c` | `55 2a 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddf90"></a> `00bddf90` | `a1 12 47 f9` | ldr x1,[x21, #0xe20] | `FALL_THROUGH`
<a id="insn-00bddf94"></a> `00bddf94` | `41 01 00 b5` | cbnz x1,0x00bddfbc | `CONDITIONAL_JUMP`
<a id="insn-00bddf98"></a> `00bddf98` | `63 b6 ff 90` | adrp x3,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bddf9c"></a> `00bddf9c` | `63 d8 22 91` | add x3,x3,#0x8b6 | `FALL_THROUGH`
<a id="insn-00bddfa0"></a> `00bddfa0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddfa4"></a> `00bddfa4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bddfa8"></a> `00bddfa8` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bddfac"></a> `00bddfac` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bddfb0"></a> `00bddfb0` | `0c f4 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bddfb4"></a> `00bddfb4` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bddfb8"></a> `00bddfb8` | `a0 12 07 f9` | str x0,[x21, #0xe20] | `FALL_THROUGH`
<a id="insn-00bddfbc"></a> `00bddfbc` | `a2 05 00 b0` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bddfc0"></a> `00bddfc0` | `44 2a 00 b0` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddfc4"></a> `00bddfc4` | `65 b6 ff 90` | adrp x5,0x2a9000 | `FALL_THROUGH`
<a id="insn-00bddfc8"></a> `00bddfc8` | `42 20 1b 91` | add x2,x2,#0x6c8 | `FALL_THROUGH`
<a id="insn-00bddfcc"></a> `00bddfcc` | `84 c0 38 91` | add x4,x4,#0xe30 | `FALL_THROUGH`
<a id="insn-00bddfd0"></a> `00bddfd0` | `a5 d8 22 91` | add x5,x5,#0x8b6 | `FALL_THROUGH`
<a id="insn-00bddfd4"></a> `00bddfd4` | `e3 01 80 52` | mov w3,#0xf | `FALL_THROUGH`
<a id="insn-00bddfd8"></a> `00bddfd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddfdc"></a> `00bddfdc` | `09 f4 01 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bddfe0"></a> `00bddfe0` | `a0 08 00 36` | tbz w0,#0x0,0x00bde0f4 | `CONDITIONAL_JUMP`
<a id="insn-00bddfe4"></a> `00bddfe4` | `55 2a 00 b0` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bddfe8"></a> `00bddfe8` | `a1 5a 47 f9` | ldr x1,[x21, #0xeb0] | `FALL_THROUGH`
<a id="insn-00bddfec"></a> `00bddfec` | `41 01 00 b5` | cbnz x1,0x00bde014 | `CONDITIONAL_JUMP`
<a id="insn-00bddff0"></a> `00bddff0` | `a3 b6 ff 90` | adrp x3,0x2b1000 | `FALL_THROUGH`
<a id="insn-00bddff4"></a> `00bddff4` | `63 80 1c 91` | add x3,x3,#0x720 | `FALL_THROUGH`
<a id="insn-00bddff8"></a> `00bddff8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bddffc"></a> `00bddffc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bde000"></a> `00bde000` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bde004"></a> `00bde004` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bde008"></a> `00bde008` | `f6 f3 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bde00c"></a> `00bde00c` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bde010"></a> `00bde010` | `a0 5a 07 f9` | str x0,[x21, #0xeb0] | `FALL_THROUGH`
<a id="insn-00bde014"></a> `00bde014` | `a2 05 00 90` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bde018"></a> `00bde018` | `44 2a 00 90` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bde01c"></a> `00bde01c` | `85 b6 ff f0` | adrp x5,0x2b1000 | `FALL_THROUGH`
<a id="insn-00bde020"></a> `00bde020` | `42 c0 20 91` | add x2,x2,#0x830 | `FALL_THROUGH`
<a id="insn-00bde024"></a> `00bde024` | `84 00 3b 91` | add x4,x4,#0xec0 | `FALL_THROUGH`
<a id="insn-00bde028"></a> `00bde028` | `a5 80 1c 91` | add x5,x5,#0x720 | `FALL_THROUGH`
<a id="insn-00bde02c"></a> `00bde02c` | `e3 00 80 52` | mov w3,#0x7 | `FALL_THROUGH`
<a id="insn-00bde030"></a> `00bde030` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bde034"></a> `00bde034` | `f3 f3 01 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bde038"></a> `00bde038` | `e0 05 00 36` | tbz w0,#0x0,0x00bde0f4 | `CONDITIONAL_JUMP`
<a id="insn-00bde03c"></a> `00bde03c` | `55 2a 00 90` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bde040"></a> `00bde040` | `a1 82 47 f9` | ldr x1,[x21, #0xf00] | `FALL_THROUGH`
<a id="insn-00bde044"></a> `00bde044` | `41 01 00 b5` | cbnz x1,0x00bde06c | `CONDITIONAL_JUMP`
<a id="insn-00bde048"></a> `00bde048` | `03 b7 ff 90` | adrp x3,0x2be000 | `FALL_THROUGH`
<a id="insn-00bde04c"></a> `00bde04c` | `63 64 25 91` | add x3,x3,#0x959 | `FALL_THROUGH`
<a id="insn-00bde050"></a> `00bde050` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bde054"></a> `00bde054` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bde058"></a> `00bde058` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bde05c"></a> `00bde05c` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bde060"></a> `00bde060` | `e0 f3 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bde064"></a> `00bde064` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bde068"></a> `00bde068` | `a0 82 07 f9` | str x0,[x21, #0xf00] | `FALL_THROUGH`
<a id="insn-00bde06c"></a> `00bde06c` | `a2 05 00 90` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bde070"></a> `00bde070` | `44 2a 00 90` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bde074"></a> `00bde074` | `05 b7 ff 90` | adrp x5,0x2be000 | `FALL_THROUGH`
<a id="insn-00bde078"></a> `00bde078` | `42 60 23 91` | add x2,x2,#0x8d8 | `FALL_THROUGH`
<a id="insn-00bde07c"></a> `00bde07c` | `84 40 3c 91` | add x4,x4,#0xf10 | `FALL_THROUGH`
<a id="insn-00bde080"></a> `00bde080` | `a5 64 25 91` | add x5,x5,#0x959 | `FALL_THROUGH`
<a id="insn-00bde084"></a> `00bde084` | `43 00 80 52` | mov w3,#0x2 | `FALL_THROUGH`
<a id="insn-00bde088"></a> `00bde088` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bde08c"></a> `00bde08c` | `dd f3 01 94` | bl 0x00c5b000 | `UNCONDITIONAL_CALL`
<a id="insn-00bde090"></a> `00bde090` | `20 03 00 36` | tbz w0,#0x0,0x00bde0f4 | `CONDITIONAL_JUMP`
<a id="insn-00bde094"></a> `00bde094` | `55 2a 00 90` | adrp x21,0x1126000 | `FALL_THROUGH`
<a id="insn-00bde098"></a> `00bde098` | `a1 96 47 f9` | ldr x1,[x21, #0xf28] | `FALL_THROUGH`
<a id="insn-00bde09c"></a> `00bde09c` | `41 01 00 b5` | cbnz x1,0x00bde0c4 | `CONDITIONAL_JUMP`
<a id="insn-00bde0a0"></a> `00bde0a0` | `63 b6 ff f0` | adrp x3,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bde0a4"></a> `00bde0a4` | `63 b0 10 91` | add x3,x3,#0x42c | `FALL_THROUGH`
<a id="insn-00bde0a8"></a> `00bde0a8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bde0ac"></a> `00bde0ac` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bde0b0"></a> `00bde0b0` | `e2 03 1f aa` | mov x2,xzr | `FALL_THROUGH`
<a id="insn-00bde0b4"></a> `00bde0b4` | `e4 03 1f 2a` | mov w4,wzr | `FALL_THROUGH`
<a id="insn-00bde0b8"></a> `00bde0b8` | `ca f3 01 94` | bl 0x00c5afe0 | `UNCONDITIONAL_CALL`
<a id="insn-00bde0bc"></a> `00bde0bc` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-00bde0c0"></a> `00bde0c0` | `a0 96 07 f9` | str x0,[x21, #0xf28] | `FALL_THROUGH`
<a id="insn-00bde0c4"></a> `00bde0c4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bde0c8"></a> `00bde0c8` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bde0cc"></a> `00bde0cc` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde0d0"></a> `00bde0d0` | `a2 05 00 90` | adrp x2,0xc92000 | `FALL_THROUGH`
<a id="insn-00bde0d4"></a> `00bde0d4` | `44 2a 00 90` | adrp x4,0x1126000 | `FALL_THROUGH`
<a id="insn-00bde0d8"></a> `00bde0d8` | `65 b6 ff f0` | adrp x5,0x2ad000 | `FALL_THROUGH`
<a id="insn-00bde0dc"></a> `00bde0dc` | `42 20 24 91` | add x2,x2,#0x908 | `FALL_THROUGH`
<a id="insn-00bde0e0"></a> `00bde0e0` | `84 e0 3c 91` | add x4,x4,#0xf38 | `FALL_THROUGH`
<a id="insn-00bde0e4"></a> `00bde0e4` | `a5 b0 10 91` | add x5,x5,#0x42c | `FALL_THROUGH`
<a id="insn-00bde0e8"></a> `00bde0e8` | `83 00 80 52` | mov w3,#0x4 | `FALL_THROUGH`
<a id="insn-00bde0ec"></a> `00bde0ec` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bde0f0"></a> `00bde0f0` | `c4 f3 01 14` | b 0x00c5b000 | `CALL_TERMINATOR`
<a id="insn-00bde0f4"></a> `00bde0f4` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bde0f8"></a> `00bde0f8` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bde0fc"></a> `00bde0fc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bde100"></a> `00bde100` | `f5 07 43 f8` | ldr x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00bde104"></a> `00bde104` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bddf1c`](#insn-00bddf1c) 範囲 `[['00bddf1c', '00bddf3f']]`
  - `CONDITIONAL_JUMP` [`00bddf3c`](#insn-00bddf3c) → [`00bddf64`](#insn-00bddf64)
  - `FALL_THROUGH` [`00bddf3c`](#insn-00bddf3c) → [`00bddf40`](#insn-00bddf40)
- ブロック [`00bddf40`](#insn-00bddf40) 範囲 `[['00bddf40', '00bddf63']]`
  - `FALL_THROUGH` [`00bddf60`](#insn-00bddf60) → [`00bddf64`](#insn-00bddf64)
- ブロック [`00bddf64`](#insn-00bddf64) 範囲 `[['00bddf64', '00bddf8b']]`
  - `CONDITIONAL_JUMP` [`00bddf88`](#insn-00bddf88) → [`00bde0f4`](#insn-00bde0f4)
  - `FALL_THROUGH` [`00bddf88`](#insn-00bddf88) → [`00bddf8c`](#insn-00bddf8c)
- ブロック [`00bddf8c`](#insn-00bddf8c) 範囲 `[['00bddf8c', '00bddf97']]`
  - `CONDITIONAL_JUMP` [`00bddf94`](#insn-00bddf94) → [`00bddfbc`](#insn-00bddfbc)
  - `FALL_THROUGH` [`00bddf94`](#insn-00bddf94) → [`00bddf98`](#insn-00bddf98)
- ブロック [`00bddf98`](#insn-00bddf98) 範囲 `[['00bddf98', '00bddfbb']]`
  - `FALL_THROUGH` [`00bddfb8`](#insn-00bddfb8) → [`00bddfbc`](#insn-00bddfbc)
- ブロック [`00bddfbc`](#insn-00bddfbc) 範囲 `[['00bddfbc', '00bddfe3']]`
  - `CONDITIONAL_JUMP` [`00bddfe0`](#insn-00bddfe0) → [`00bde0f4`](#insn-00bde0f4)
  - `FALL_THROUGH` [`00bddfe0`](#insn-00bddfe0) → [`00bddfe4`](#insn-00bddfe4)
- ブロック [`00bddfe4`](#insn-00bddfe4) 範囲 `[['00bddfe4', '00bddfef']]`
  - `CONDITIONAL_JUMP` [`00bddfec`](#insn-00bddfec) → [`00bde014`](#insn-00bde014)
  - `FALL_THROUGH` [`00bddfec`](#insn-00bddfec) → [`00bddff0`](#insn-00bddff0)
- ブロック [`00bddff0`](#insn-00bddff0) 範囲 `[['00bddff0', '00bde013']]`
  - `FALL_THROUGH` [`00bde010`](#insn-00bde010) → [`00bde014`](#insn-00bde014)
- ブロック [`00bde014`](#insn-00bde014) 範囲 `[['00bde014', '00bde03b']]`
  - `CONDITIONAL_JUMP` [`00bde038`](#insn-00bde038) → [`00bde0f4`](#insn-00bde0f4)
  - `FALL_THROUGH` [`00bde038`](#insn-00bde038) → [`00bde03c`](#insn-00bde03c)
- ブロック [`00bde03c`](#insn-00bde03c) 範囲 `[['00bde03c', '00bde047']]`
  - `CONDITIONAL_JUMP` [`00bde044`](#insn-00bde044) → [`00bde06c`](#insn-00bde06c)
  - `FALL_THROUGH` [`00bde044`](#insn-00bde044) → [`00bde048`](#insn-00bde048)
- ブロック [`00bde048`](#insn-00bde048) 範囲 `[['00bde048', '00bde06b']]`
  - `FALL_THROUGH` [`00bde068`](#insn-00bde068) → [`00bde06c`](#insn-00bde06c)
- ブロック [`00bde06c`](#insn-00bde06c) 範囲 `[['00bde06c', '00bde093']]`
  - `CONDITIONAL_JUMP` [`00bde090`](#insn-00bde090) → [`00bde0f4`](#insn-00bde0f4)
  - `FALL_THROUGH` [`00bde090`](#insn-00bde090) → [`00bde094`](#insn-00bde094)
- ブロック [`00bde094`](#insn-00bde094) 範囲 `[['00bde094', '00bde09f']]`
  - `CONDITIONAL_JUMP` [`00bde09c`](#insn-00bde09c) → [`00bde0c4`](#insn-00bde0c4)
  - `FALL_THROUGH` [`00bde09c`](#insn-00bde09c) → [`00bde0a0`](#insn-00bde0a0)
- ブロック [`00bde0a0`](#insn-00bde0a0) 範囲 `[['00bde0a0', '00bde0c3']]`
  - `FALL_THROUGH` [`00bde0c0`](#insn-00bde0c0) → [`00bde0c4`](#insn-00bde0c4)
- ブロック [`00bde0c4`](#insn-00bde0c4) 範囲 `[['00bde0c4', '00bde0f3']]`
- ブロック [`00bde0f4`](#insn-00bde0f4) 範囲 `[['00bde0f4', '00bde107']]`

## 命令位置別の参照

- [`00bddf1c`](#insn-00bddf1c) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf20`](#insn-00bddf20) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf24`](#insn-00bddf24) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf34`](#insn-00bddf34) → `01126e00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddf3c`](#insn-00bddf3c) → [`00bddf64`](#insn-00bddf64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf44`](#insn-00bddf44) → `002bc1fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddf58`](#insn-00bddf58) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bddf60`](#insn-00bddf60) → `01126e00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddf70`](#insn-00bddf70) → `00c926b0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddf74`](#insn-00bddf74) → `01126e10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddf78`](#insn-00bddf78) → `002bc1fc`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddf84`](#insn-00bddf84) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bddf88`](#insn-00bddf88) → [`00bde0f4`](#insn-00bde0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf90`](#insn-00bddf90) → `01126e20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddf94`](#insn-00bddf94) → [`00bddfbc`](#insn-00bddfbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddf9c`](#insn-00bddf9c) → `002a98b6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddfb0`](#insn-00bddfb0) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bddfb8`](#insn-00bddfb8) → `01126e20`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddfc8`](#insn-00bddfc8) → `00c926c8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bddfcc`](#insn-00bddfcc) → `01126e30`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddfd0`](#insn-00bddfd0) → `002a98b6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bddfdc`](#insn-00bddfdc) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bddfe0`](#insn-00bddfe0) → [`00bde0f4`](#insn-00bde0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddfe8`](#insn-00bddfe8) → `01126eb0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bddfec`](#insn-00bddfec) → [`00bde014`](#insn-00bde014) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bddff4`](#insn-00bddff4) → `002b1720`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bde008`](#insn-00bde008) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bde010`](#insn-00bde010) → `01126eb0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde020`](#insn-00bde020) → `00c92830`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bde024`](#insn-00bde024) → `01126ec0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde028`](#insn-00bde028) → `002b1720`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bde034`](#insn-00bde034) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bde038`](#insn-00bde038) → [`00bde0f4`](#insn-00bde0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde040`](#insn-00bde040) → `01126f00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde044`](#insn-00bde044) → [`00bde06c`](#insn-00bde06c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde04c`](#insn-00bde04c) → `002be959`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bde060`](#insn-00bde060) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bde068`](#insn-00bde068) → `01126f00`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde078`](#insn-00bde078) → `00c928d8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bde07c`](#insn-00bde07c) → `01126f10`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde080`](#insn-00bde080) → `002be959`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bde08c`](#insn-00bde08c) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bde090`](#insn-00bde090) → [`00bde0f4`](#insn-00bde0f4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde098`](#insn-00bde098) → `01126f28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde09c`](#insn-00bde09c) → [`00bde0c4`](#insn-00bde0c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde0a4`](#insn-00bde0a4) → `002ad42c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bde0b8`](#insn-00bde0b8) → [`00c5afe0`](../00c5a/00c5afe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5afe0` · 推定シンボル `None` · 推定型 `None`
- [`00bde0c0`](#insn-00bde0c0) → `01126f28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde0c8`](#insn-00bde0c8) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde0cc`](#insn-00bde0cc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde0dc`](#insn-00bde0dc) → `00c92908`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00bde0e0`](#insn-00bde0e0) → `01126f38`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bde0e4`](#insn-00bde0e4) → `002ad42c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bde0f0`](#insn-00bde0f0) → [`00c5b000`](../00c5b/00c5b000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b000` · 推定シンボル `None` · 推定型 `None`
- [`00bde0f4`](#insn-00bde0f4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bde0f8`](#insn-00bde0f8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bddf1c`](#insn-00bddf1c)

~~~json
{
  "source": "00bddf1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf20`](#insn-00bddf20)

~~~json
{
  "source": "00bddf20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf24`](#insn-00bddf24)

~~~json
{
  "source": "00bddf24",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf34`](#insn-00bddf34)

~~~json
{
  "source": "00bddf34",
  "target": "01126e00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddf3c`](#insn-00bddf3c)

~~~json
{
  "source": "00bddf3c",
  "target": "00bddf64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf44`](#insn-00bddf44)

~~~json
{
  "source": "00bddf44",
  "target": "002bc1fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc1f8",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc1f8",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddf58`](#insn-00bddf58)

~~~json
{
  "source": "00bddf58",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddf60`](#insn-00bddf60)

~~~json
{
  "source": "00bddf60",
  "target": "01126e00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddf70`](#insn-00bddf70)

~~~json
{
  "source": "00bddf70",
  "target": "00c926b0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c926b0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddf74`](#insn-00bddf74)

~~~json
{
  "source": "00bddf74",
  "target": "01126e10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddf78`](#insn-00bddf78)

~~~json
{
  "source": "00bddf78",
  "target": "002bc1fc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bc1f8",
  "offset": 4,
  "size": 44,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f476574",
  "capture_start": "002bc1f8",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddf84`](#insn-00bddf84)

~~~json
{
  "source": "00bddf84",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddf88`](#insn-00bddf88)

~~~json
{
  "source": "00bddf88",
  "target": "00bde0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf90`](#insn-00bddf90)

~~~json
{
  "source": "00bddf90",
  "target": "01126e20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddf94`](#insn-00bddf94)

~~~json
{
  "source": "00bddf94",
  "target": "00bddfbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddf9c`](#insn-00bddf9c)

~~~json
{
  "source": "00bddf9c",
  "target": "002a98b6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a98b2",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a98b2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddfb0`](#insn-00bddfb0)

~~~json
{
  "source": "00bddfb0",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddfb8`](#insn-00bddfb8)

~~~json
{
  "source": "00bddfb8",
  "target": "01126e20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddfc8`](#insn-00bddfc8)

~~~json
{
  "source": "00bddfc8",
  "target": "00c926c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c926c8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bddfcc`](#insn-00bddfcc)

~~~json
{
  "source": "00bddfcc",
  "target": "01126e30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126e30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddfd0`](#insn-00bddfd0)

~~~json
{
  "source": "00bddfd0",
  "target": "002a98b6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a98b2",
  "offset": 4,
  "size": 42,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002a98b2",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bddfdc`](#insn-00bddfdc)

~~~json
{
  "source": "00bddfdc",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bddfe0`](#insn-00bddfe0)

~~~json
{
  "source": "00bddfe0",
  "target": "00bde0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddfe8`](#insn-00bddfe8)

~~~json
{
  "source": "00bddfe8",
  "target": "01126eb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126eb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bddfec`](#insn-00bddfec)

~~~json
{
  "source": "00bddfec",
  "target": "00bde014",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bddff4`](#insn-00bddff4)

~~~json
{
  "source": "00bddff4",
  "target": "002b1720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b171c",
  "offset": 4,
  "size": 38,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002b171c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bde008`](#insn-00bde008)

~~~json
{
  "source": "00bde008",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde010`](#insn-00bde010)

~~~json
{
  "source": "00bde010",
  "target": "01126eb0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126eb0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde020`](#insn-00bde020)

~~~json
{
  "source": "00bde020",
  "target": "00c92830",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92830",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bde024`](#insn-00bde024)

~~~json
{
  "source": "00bde024",
  "target": "01126ec0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126ec0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde028`](#insn-00bde028)

~~~json
{
  "source": "00bde028",
  "target": "002b1720",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b171c",
  "offset": 4,
  "size": 38,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002b171c",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bde034`](#insn-00bde034)

~~~json
{
  "source": "00bde034",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde038`](#insn-00bde038)

~~~json
{
  "source": "00bde038",
  "target": "00bde0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde040`](#insn-00bde040)

~~~json
{
  "source": "00bde040",
  "target": "01126f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde044`](#insn-00bde044)

~~~json
{
  "source": "00bde044",
  "target": "00bde06c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde04c`](#insn-00bde04c)

~~~json
{
  "source": "00bde04c",
  "target": "002be959",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be955",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002be955",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bde060`](#insn-00bde060)

~~~json
{
  "source": "00bde060",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde068`](#insn-00bde068)

~~~json
{
  "source": "00bde068",
  "target": "01126f00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde078`](#insn-00bde078)

~~~json
{
  "source": "00bde078",
  "target": "00c928d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c928d8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bde07c`](#insn-00bde07c)

~~~json
{
  "source": "00bde07c",
  "target": "01126f10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde080`](#insn-00bde080)

~~~json
{
  "source": "00bde080",
  "target": "002be959",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002be955",
  "offset": 4,
  "size": 50,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f466972",
  "capture_start": "002be955",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bde08c`](#insn-00bde08c)

~~~json
{
  "source": "00bde08c",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde090`](#insn-00bde090)

~~~json
{
  "source": "00bde090",
  "target": "00bde0f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde098`](#insn-00bde098)

~~~json
{
  "source": "00bde098",
  "target": "01126f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde09c`](#insn-00bde09c)

~~~json
{
  "source": "00bde09c",
  "target": "00bde0c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde0a4`](#insn-00bde0a4)

~~~json
{
  "source": "00bde0a4",
  "target": "002ad42c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad428",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad428",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bde0b8`](#insn-00bde0b8)

~~~json
{
  "source": "00bde0b8",
  "target": "00c5afe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde0c0`](#insn-00bde0c0)

~~~json
{
  "source": "00bde0c0",
  "target": "01126f28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde0c8`](#insn-00bde0c8)

~~~json
{
  "source": "00bde0c8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde0cc`](#insn-00bde0cc)

~~~json
{
  "source": "00bde0cc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde0dc`](#insn-00bde0dc)

~~~json
{
  "source": "00bde0dc",
  "target": "00c92908",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c92908",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00bde0e0`](#insn-00bde0e0)

~~~json
{
  "source": "00bde0e0",
  "target": "01126f38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126f38",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bde0e4`](#insn-00bde0e4)

~~~json
{
  "source": "00bde0e4",
  "target": "002ad42c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad428",
  "offset": 4,
  "size": 62,
  "datatype": "string",
  "bytes": "25504725636f6d2f676f6f676c652f66697265626173652f617574682f557365",
  "capture_start": "002ad428",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bde0f0`](#insn-00bde0f0)

~~~json
{
  "source": "00bde0f0",
  "target": "00c5b000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bde0f4`](#insn-00bde0f4)

~~~json
{
  "source": "00bde0f4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bde0f8`](#insn-00bde0f8)

~~~json
{
  "source": "00bde0f8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
