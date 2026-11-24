# 00bda1ec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bda150`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bda/00bda150.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-6c615d5446040e0cb5b9940bf09b7936)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdb1e0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdb/00bdb1e0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-a9dafea852207ad3f79d4e32e4c365e2)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bda1ec",
  "name": "_ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_S3_",
  "size": 704,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "740792cfe53ff55b5c0ce96ecc2696358b579d5d4eec68cf418854cc1f642394",
  "source_text_sha256": "740792cfe53ff55b5c0ce96ecc2696358b579d5d4eec68cf418854cc1f642394",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bda1ec",
        "00bda4ab"
      ]
    ],
    "bytes_sha256": "5849a8d6de1f43ff1196893638e4d71081d7ef9d78bc7f110881fc8d1f365860",
    "instruction_count": 176,
    "instruction_bytes": 704,
    "body_bytes": 704,
    "indirect": 14,
    "unresolved": 14
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5ad70](../00c5a/00c5ad70.md)
- [00c5b030](../00c5b/00c5b030.md)
- [00c5b0d0](../00c5b/00c5b0d0.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5b330](../00c5b/00c5b330.md)

## 関連文字列（未確認候補）

~~~text
"Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
"app != nullptr"
"g_methods_cached"
"provider_id && id_token && raw_nonce"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3098 bytes

~~~c

void _ZN8firebase4auth13OAuthProvider13GetCredentialEPKcS3_S3_S3_
               (undefined8 *param_1,long param_2,long param_3,long param_4,long param_5)

{
  long lVar1;
  long *plVar2;
  undefined8 uVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  ulong uVar6;
  undefined8 uVar7;
  undefined8 uVar8;
  char *pcVar9;
  long lVar10;
  
  if (((param_2 == 0) || (param_3 == 0)) || (param_4 == 0)) {
    pcVar9 = "provider_id && id_token && raw_nonce";
LAB_00bda394:
    _ZN8firebase9LogAssertEPKcz(pcVar9);
  }
  else {
    if (DAT_01126df8 == '\0') {
      _ZN8firebase8LogErrorEPKcz("g_methods_cached");
      pcVar9 = 
      "Firebase Auth was not initialized, unable to create a Credential. Create an Auth instance first."
      ;
      goto LAB_00bda394;
    }
    lVar1 = _ZN8firebase10app_common9GetAnyAppEv();
    if (lVar1 == 0) {
      _ZN8firebase9LogAssertEPKcz("app != nullptr");
    }
    plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar1);
    uVar3 = (**(code **)(*plVar2 + 0x538))(plVar2,param_2);
    uVar4 = (**(code **)(*plVar2 + 0x538))(plVar2,param_3);
    uVar5 = (**(code **)(*plVar2 + 0x538))(plVar2,param_4);
    lVar1 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                      (plVar2,DAT_01126c28,DAT_01126c48,uVar3);
    uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
    if ((uVar6 & 1) == 0) {
      uVar7 = FUN_00497874(plVar2,lVar1,DAT_01126d50,uVar4,uVar5);
      uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
      if (((uVar6 & 1) == 0) && ((**(code **)(*plVar2 + 0xb8))(plVar2,uVar7), param_5 != 0)) {
        uVar7 = (**(code **)(*plVar2 + 0x538))(plVar2,param_5);
        uVar8 = FUN_00497874(plVar2,lVar1,DAT_01126d40,uVar7);
        (**(code **)(*plVar2 + 0xb8))(plVar2,uVar7);
        uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
        if ((uVar6 & 1) != 0) {
          (**(code **)(*plVar2 + 0xb8))(plVar2,lVar1);
          goto LAB_00bda418;
        }
        (**(code **)(*plVar2 + 0xb8))(plVar2,uVar8);
      }
      if (lVar1 == 0) goto LAB_00bda418;
      lVar10 = FUN_00497874(plVar2,lVar1,DAT_01126d58);
      uVar6 = _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
      (**(code **)(*plVar2 + 0xb8))(plVar2,lVar1);
      lVar1 = 0;
      if ((uVar6 & 1) == 0) {
        lVar1 = lVar10;
      }
    }
    else {
LAB_00bda418:
      lVar1 = 0;
    }
    (**(code **)(*plVar2 + 0xb8))(plVar2,uVar3);
    (**(code **)(*plVar2 + 0xb8))(plVar2,uVar5);
    (**(code **)(*plVar2 + 0xb8))(plVar2,uVar4);
    if (lVar1 != 0) {
      lVar10 = _ZN8firebase10app_common9GetAnyAppEv();
      if (lVar10 == 0) {
        _ZN8firebase9LogAssertEPKcz("app != nullptr");
      }
      plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(lVar10);
      uVar3 = (**(code **)(*plVar2 + 0xa8))(plVar2,lVar1);
      (**(code **)(*plVar2 + 0xb8))(plVar2,lVar1);
      goto LAB_00bda39c;
    }
  }
  uVar3 = 0;
LAB_00bda39c:
  *param_1 = uVar3;
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
<a id="insn-00bda1ec"></a> `00bda1ec` | `fa 67 bb a9` | stp x26,x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00bda1f0"></a> `00bda1f0` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda1f4"></a> `00bda1f4` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda1f8"></a> `00bda1f8` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda1fc"></a> `00bda1fc` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bda200"></a> `00bda200` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bda204"></a> `00bda204` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-00bda208"></a> `00bda208` | `60 0b 00 b4` | cbz x0,0x00bda374 | `CONDITIONAL_JUMP`
<a id="insn-00bda20c"></a> `00bda20c` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bda210"></a> `00bda210` | `21 0b 00 b4` | cbz x1,0x00bda374 | `CONDITIONAL_JUMP`
<a id="insn-00bda214"></a> `00bda214` | `f7 03 02 aa` | mov x23,x2 | `FALL_THROUGH`
<a id="insn-00bda218"></a> `00bda218` | `e2 0a 00 b4` | cbz x2,0x00bda374 | `CONDITIONAL_JUMP`
<a id="insn-00bda21c"></a> `00bda21c` | `68 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bda220"></a> `00bda220` | `08 e1 77 39` | ldrb w8,[x8, #0xdf8] | `FALL_THROUGH`
<a id="insn-00bda224"></a> `00bda224` | `e8 0a 00 34` | cbz w8,0x00bda380 | `CONDITIONAL_JUMP`
<a id="insn-00bda228"></a> `00bda228` | `f8 03 03 aa` | mov x24,x3 | `FALL_THROUGH`
<a id="insn-00bda22c"></a> `00bda22c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bda230"></a> `00bda230` | `40 04 02 94` | bl 0x00c5b330 | `UNCONDITIONAL_CALL`
<a id="insn-00bda234"></a> `00bda234` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bda238"></a> `00bda238` | `80 00 00 b5` | cbnz x0,0x00bda248 | `CONDITIONAL_JUMP`
<a id="insn-00bda23c"></a> `00bda23c` | `c0 b6 ff 90` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bda240"></a> `00bda240` | `00 24 18 91` | add x0,x0,#0x609 | `FALL_THROUGH`
<a id="insn-00bda244"></a> `00bda244` | `a3 03 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda248"></a> `00bda248` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda24c"></a> `00bda24c` | `c1 03 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bda250"></a> `00bda250` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bda254"></a> `00bda254` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bda258"></a> `00bda258` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bda25c"></a> `00bda25c` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bda260"></a> `00bda260` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda264"></a> `00bda264` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bda268"></a> `00bda268` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bda26c"></a> `00bda26c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda270"></a> `00bda270` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bda274"></a> `00bda274` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bda278"></a> `00bda278` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda27c"></a> `00bda27c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bda280"></a> `00bda280` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bda284"></a> `00bda284` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda288"></a> `00bda288` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bda28c"></a> `00bda28c` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bda290"></a> `00bda290` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda294"></a> `00bda294` | `68 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bda298"></a> `00bda298` | `69 2a 00 90` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bda29c"></a> `00bda29c` | `01 15 46 f9` | ldr x1,[x8, #0xc28] | `FALL_THROUGH`
<a id="insn-00bda2a0"></a> `00bda2a0` | `22 25 46 f9` | ldr x2,[x9, #0xc48] | `FALL_THROUGH`
<a id="insn-00bda2a4"></a> `00bda2a4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bda2a8"></a> `00bda2a8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda2ac"></a> `00bda2ac` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bda2b0"></a> `00bda2b0` | `70 02 02 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bda2b4"></a> `00bda2b4` | `f9 03 00 aa` | mov x25,x0 | `FALL_THROUGH`
<a id="insn-00bda2b8"></a> `00bda2b8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda2bc"></a> `00bda2bc` | `5d 03 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bda2c0"></a> `00bda2c0` | `c0 0a 00 37` | tbnz w0,#0x0,0x00bda418 | `CONDITIONAL_JUMP`
<a id="insn-00bda2c4"></a> `00bda2c4` | `68 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bda2c8"></a> `00bda2c8` | `02 a9 46 f9` | ldr x2,[x8, #0xd50] | `FALL_THROUGH`
<a id="insn-00bda2cc"></a> `00bda2cc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda2d0"></a> `00bda2d0` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bda2d4"></a> `00bda2d4` | `e3 03 15 aa` | mov x3,x21 | `FALL_THROUGH`
<a id="insn-00bda2d8"></a> `00bda2d8` | `e4 03 17 aa` | mov x4,x23 | `FALL_THROUGH`
<a id="insn-00bda2dc"></a> `00bda2dc` | `66 f5 e2 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bda2e0"></a> `00bda2e0` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bda2e4"></a> `00bda2e4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda2e8"></a> `00bda2e8` | `52 03 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bda2ec"></a> `00bda2ec` | `20 07 00 37` | tbnz w0,#0x0,0x00bda3d0 | `CONDITIONAL_JUMP`
<a id="insn-00bda2f0"></a> `00bda2f0` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bda2f4"></a> `00bda2f4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda2f8"></a> `00bda2f8` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bda2fc"></a> `00bda2fc` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bda300"></a> `00bda300` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda304"></a> `00bda304` | `78 06 00 b4` | cbz x24,0x00bda3d0 | `CONDITIONAL_JUMP`
<a id="insn-00bda308"></a> `00bda308` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bda30c"></a> `00bda30c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda310"></a> `00bda310` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bda314"></a> `00bda314` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bda318"></a> `00bda318` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda31c"></a> `00bda31c` | `68 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bda320"></a> `00bda320` | `02 a1 46 f9` | ldr x2,[x8, #0xd40] | `FALL_THROUGH`
<a id="insn-00bda324"></a> `00bda324` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00bda328"></a> `00bda328` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda32c"></a> `00bda32c` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bda330"></a> `00bda330` | `e3 03 1a aa` | mov x3,x26 | `FALL_THROUGH`
<a id="insn-00bda334"></a> `00bda334` | `50 f5 e2 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bda338"></a> `00bda338` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bda33c"></a> `00bda33c` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bda340"></a> `00bda340` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda344"></a> `00bda344` | `e1 03 1a aa` | mov x1,x26 | `FALL_THROUGH`
<a id="insn-00bda348"></a> `00bda348` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bda34c"></a> `00bda34c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda350"></a> `00bda350` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda354"></a> `00bda354` | `37 03 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bda358"></a> `00bda358` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bda35c"></a> `00bda35c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bda360"></a> `00bda360` | `20 03 00 36` | tbz w0,#0x0,0x00bda3c4 | `CONDITIONAL_JUMP`
<a id="insn-00bda364"></a> `00bda364` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda368"></a> `00bda368` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bda36c"></a> `00bda36c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda370"></a> `00bda370` | `2a 00 00 14` | b 0x00bda418 | `UNCONDITIONAL_JUMP`
<a id="insn-00bda374"></a> `00bda374` | `20 b7 ff b0` | adrp x0,0x2bf000 | `FALL_THROUGH`
<a id="insn-00bda378"></a> `00bda378` | `00 4c 29 91` | add x0,x0,#0xa53 | `FALL_THROUGH`
<a id="insn-00bda37c"></a> `00bda37c` | `06 00 00 14` | b 0x00bda394 | `UNCONDITIONAL_JUMP`
<a id="insn-00bda380"></a> `00bda380` | `e0 b6 ff b0` | adrp x0,0x2b7000 | `FALL_THROUGH`
<a id="insn-00bda384"></a> `00bda384` | `00 40 39 91` | add x0,x0,#0xe50 | `FALL_THROUGH`
<a id="insn-00bda388"></a> `00bda388` | `7a 02 02 94` | bl 0x00c5ad70 | `UNCONDITIONAL_CALL`
<a id="insn-00bda38c"></a> `00bda38c` | `a0 b9 ff d0` | adrp x0,0x310000 | `FALL_THROUGH`
<a id="insn-00bda390"></a> `00bda390` | `00 c0 04 91` | add x0,x0,#0x130 | `FALL_THROUGH`
<a id="insn-00bda394"></a> `00bda394` | `4f 03 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda398"></a> `00bda398` | `f4 03 1f aa` | mov x20,xzr | `FALL_THROUGH`
<a id="insn-00bda39c"></a> `00bda39c` | `74 02 00 f9` | str x20,[x19] | `FALL_THROUGH`
<a id="insn-00bda3a0"></a> `00bda3a0` | `7f 0a 00 b9` | str wzr,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00bda3a4"></a> `00bda3a4` | `7f fe 01 a9` | stp xzr,xzr,[x19, #0x18] | `FALL_THROUGH`
<a id="insn-00bda3a8"></a> `00bda3a8` | `7f 0a 00 f9` | str xzr,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00bda3ac"></a> `00bda3ac` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bda3b0"></a> `00bda3b0` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bda3b4"></a> `00bda3b4` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bda3b8"></a> `00bda3b8` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bda3bc"></a> `00bda3bc` | `fa 67 c5 a8` | ldp x26,x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00bda3c0"></a> `00bda3c0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bda3c4"></a> `00bda3c4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda3c8"></a> `00bda3c8` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bda3cc"></a> `00bda3cc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda3d0"></a> `00bda3d0` | `59 02 00 b4` | cbz x25,0x00bda418 | `CONDITIONAL_JUMP`
<a id="insn-00bda3d4"></a> `00bda3d4` | `68 2a 00 90` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bda3d8"></a> `00bda3d8` | `02 ad 46 f9` | ldr x2,[x8, #0xd58] | `FALL_THROUGH`
<a id="insn-00bda3dc"></a> `00bda3dc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda3e0"></a> `00bda3e0` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bda3e4"></a> `00bda3e4` | `24 f5 e2 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bda3e8"></a> `00bda3e8` | `f8 03 00 aa` | mov x24,x0 | `FALL_THROUGH`
<a id="insn-00bda3ec"></a> `00bda3ec` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda3f0"></a> `00bda3f0` | `10 03 02 94` | bl 0x00c5b030 | `UNCONDITIONAL_CALL`
<a id="insn-00bda3f4"></a> `00bda3f4` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bda3f8"></a> `00bda3f8` | `fa 03 00 2a` | mov w26,w0 | `FALL_THROUGH`
<a id="insn-00bda3fc"></a> `00bda3fc` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda400"></a> `00bda400` | `e1 03 19 aa` | mov x1,x25 | `FALL_THROUGH`
<a id="insn-00bda404"></a> `00bda404` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bda408"></a> `00bda408` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda40c"></a> `00bda40c` | `5f 03 00 72` | tst w26,#0x1 | `FALL_THROUGH`
<a id="insn-00bda410"></a> `00bda410` | `f8 13 98 9a` | csel x24,xzr,x24,ne | `FALL_THROUGH`
<a id="insn-00bda414"></a> `00bda414` | `02 00 00 14` | b 0x00bda41c | `UNCONDITIONAL_JUMP`
<a id="insn-00bda418"></a> `00bda418` | `f8 03 1f aa` | mov x24,xzr | `FALL_THROUGH`
<a id="insn-00bda41c"></a> `00bda41c` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bda420"></a> `00bda420` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda424"></a> `00bda424` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bda428"></a> `00bda428` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bda42c"></a> `00bda42c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda430"></a> `00bda430` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bda434"></a> `00bda434` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda438"></a> `00bda438` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bda43c"></a> `00bda43c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bda440"></a> `00bda440` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda444"></a> `00bda444` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-00bda448"></a> `00bda448` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda44c"></a> `00bda44c` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bda450"></a> `00bda450` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bda454"></a> `00bda454` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda458"></a> `00bda458` | `18 fa ff b4` | cbz x24,0x00bda398 | `CONDITIONAL_JUMP`
<a id="insn-00bda45c"></a> `00bda45c` | `b5 03 02 94` | bl 0x00c5b330 | `UNCONDITIONAL_CALL`
<a id="insn-00bda460"></a> `00bda460` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bda464"></a> `00bda464` | `80 00 00 b5` | cbnz x0,0x00bda474 | `CONDITIONAL_JUMP`
<a id="insn-00bda468"></a> `00bda468` | `c0 b6 ff 90` | adrp x0,0x2b2000 | `FALL_THROUGH`
<a id="insn-00bda46c"></a> `00bda46c` | `00 24 18 91` | add x0,x0,#0x609 | `FALL_THROUGH`
<a id="insn-00bda470"></a> `00bda470` | `18 03 02 94` | bl 0x00c5b0d0 | `UNCONDITIONAL_CALL`
<a id="insn-00bda474"></a> `00bda474` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bda478"></a> `00bda478` | `36 03 02 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bda47c"></a> `00bda47c` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bda480"></a> `00bda480` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bda484"></a> `00bda484` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bda488"></a> `00bda488` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bda48c"></a> `00bda48c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda490"></a> `00bda490` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bda494"></a> `00bda494` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bda498"></a> `00bda498` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bda49c"></a> `00bda49c` | `e1 03 18 aa` | mov x1,x24 | `FALL_THROUGH`
<a id="insn-00bda4a0"></a> `00bda4a0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bda4a4"></a> `00bda4a4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bda4a8"></a> `00bda4a8` | `bd ff ff 17` | b 0x00bda39c | `UNCONDITIONAL_JUMP`

## 基本ブロックと分岐先

- ブロック [`00bda1ec`](#insn-00bda1ec) 範囲 `[['00bda1ec', '00bda20b']]`
  - `CONDITIONAL_JUMP` [`00bda208`](#insn-00bda208) → [`00bda374`](#insn-00bda374)
  - `FALL_THROUGH` [`00bda208`](#insn-00bda208) → [`00bda20c`](#insn-00bda20c)
- ブロック [`00bda20c`](#insn-00bda20c) 範囲 `[['00bda20c', '00bda213']]`
  - `CONDITIONAL_JUMP` [`00bda210`](#insn-00bda210) → [`00bda374`](#insn-00bda374)
  - `FALL_THROUGH` [`00bda210`](#insn-00bda210) → [`00bda214`](#insn-00bda214)
- ブロック [`00bda214`](#insn-00bda214) 範囲 `[['00bda214', '00bda21b']]`
  - `CONDITIONAL_JUMP` [`00bda218`](#insn-00bda218) → [`00bda374`](#insn-00bda374)
  - `FALL_THROUGH` [`00bda218`](#insn-00bda218) → [`00bda21c`](#insn-00bda21c)
- ブロック [`00bda21c`](#insn-00bda21c) 範囲 `[['00bda21c', '00bda227']]`
  - `CONDITIONAL_JUMP` [`00bda224`](#insn-00bda224) → [`00bda380`](#insn-00bda380)
  - `FALL_THROUGH` [`00bda224`](#insn-00bda224) → [`00bda228`](#insn-00bda228)
- ブロック [`00bda228`](#insn-00bda228) 範囲 `[['00bda228', '00bda23b']]`
  - `CONDITIONAL_JUMP` [`00bda238`](#insn-00bda238) → [`00bda248`](#insn-00bda248)
  - `FALL_THROUGH` [`00bda238`](#insn-00bda238) → [`00bda23c`](#insn-00bda23c)
- ブロック [`00bda23c`](#insn-00bda23c) 範囲 `[['00bda23c', '00bda247']]`
  - `FALL_THROUGH` [`00bda244`](#insn-00bda244) → [`00bda248`](#insn-00bda248)
- ブロック [`00bda248`](#insn-00bda248) 範囲 `[['00bda248', '00bda2c3']]`
  - `CONDITIONAL_JUMP` [`00bda2c0`](#insn-00bda2c0) → [`00bda418`](#insn-00bda418)
  - `FALL_THROUGH` [`00bda2c0`](#insn-00bda2c0) → [`00bda2c4`](#insn-00bda2c4)
- ブロック [`00bda2c4`](#insn-00bda2c4) 範囲 `[['00bda2c4', '00bda2ef']]`
  - `CONDITIONAL_JUMP` [`00bda2ec`](#insn-00bda2ec) → [`00bda3d0`](#insn-00bda3d0)
  - `FALL_THROUGH` [`00bda2ec`](#insn-00bda2ec) → [`00bda2f0`](#insn-00bda2f0)
- ブロック [`00bda2f0`](#insn-00bda2f0) 範囲 `[['00bda2f0', '00bda307']]`
  - `CONDITIONAL_JUMP` [`00bda304`](#insn-00bda304) → [`00bda3d0`](#insn-00bda3d0)
  - `FALL_THROUGH` [`00bda304`](#insn-00bda304) → [`00bda308`](#insn-00bda308)
- ブロック [`00bda308`](#insn-00bda308) 範囲 `[['00bda308', '00bda363']]`
  - `CONDITIONAL_JUMP` [`00bda360`](#insn-00bda360) → [`00bda3c4`](#insn-00bda3c4)
  - `FALL_THROUGH` [`00bda360`](#insn-00bda360) → [`00bda364`](#insn-00bda364)
- ブロック [`00bda364`](#insn-00bda364) 範囲 `[['00bda364', '00bda373']]`
  - `UNCONDITIONAL_JUMP` [`00bda370`](#insn-00bda370) → [`00bda418`](#insn-00bda418)
- ブロック [`00bda374`](#insn-00bda374) 範囲 `[['00bda374', '00bda37f']]`
  - `UNCONDITIONAL_JUMP` [`00bda37c`](#insn-00bda37c) → [`00bda394`](#insn-00bda394)
- ブロック [`00bda380`](#insn-00bda380) 範囲 `[['00bda380', '00bda393']]`
  - `FALL_THROUGH` [`00bda390`](#insn-00bda390) → [`00bda394`](#insn-00bda394)
- ブロック [`00bda394`](#insn-00bda394) 範囲 `[['00bda394', '00bda397']]`
  - `FALL_THROUGH` [`00bda394`](#insn-00bda394) → [`00bda398`](#insn-00bda398)
- ブロック [`00bda398`](#insn-00bda398) 範囲 `[['00bda398', '00bda39b']]`
  - `FALL_THROUGH` [`00bda398`](#insn-00bda398) → [`00bda39c`](#insn-00bda39c)
- ブロック [`00bda39c`](#insn-00bda39c) 範囲 `[['00bda39c', '00bda3c3']]`
- ブロック [`00bda3c4`](#insn-00bda3c4) 範囲 `[['00bda3c4', '00bda3cf']]`
  - `FALL_THROUGH` [`00bda3cc`](#insn-00bda3cc) → [`00bda3d0`](#insn-00bda3d0)
- ブロック [`00bda3d0`](#insn-00bda3d0) 範囲 `[['00bda3d0', '00bda3d3']]`
  - `CONDITIONAL_JUMP` [`00bda3d0`](#insn-00bda3d0) → [`00bda418`](#insn-00bda418)
  - `FALL_THROUGH` [`00bda3d0`](#insn-00bda3d0) → [`00bda3d4`](#insn-00bda3d4)
- ブロック [`00bda3d4`](#insn-00bda3d4) 範囲 `[['00bda3d4', '00bda417']]`
  - `UNCONDITIONAL_JUMP` [`00bda414`](#insn-00bda414) → [`00bda41c`](#insn-00bda41c)
- ブロック [`00bda418`](#insn-00bda418) 範囲 `[['00bda418', '00bda41b']]`
  - `FALL_THROUGH` [`00bda418`](#insn-00bda418) → [`00bda41c`](#insn-00bda41c)
- ブロック [`00bda41c`](#insn-00bda41c) 範囲 `[['00bda41c', '00bda45b']]`
  - `CONDITIONAL_JUMP` [`00bda458`](#insn-00bda458) → [`00bda398`](#insn-00bda398)
  - `FALL_THROUGH` [`00bda458`](#insn-00bda458) → [`00bda45c`](#insn-00bda45c)
- ブロック [`00bda45c`](#insn-00bda45c) 範囲 `[['00bda45c', '00bda467']]`
  - `CONDITIONAL_JUMP` [`00bda464`](#insn-00bda464) → [`00bda474`](#insn-00bda474)
  - `FALL_THROUGH` [`00bda464`](#insn-00bda464) → [`00bda468`](#insn-00bda468)
- ブロック [`00bda468`](#insn-00bda468) 範囲 `[['00bda468', '00bda473']]`
  - `FALL_THROUGH` [`00bda470`](#insn-00bda470) → [`00bda474`](#insn-00bda474)
- ブロック [`00bda474`](#insn-00bda474) 範囲 `[['00bda474', '00bda4ab']]`
  - `UNCONDITIONAL_JUMP` [`00bda4a8`](#insn-00bda4a8) → [`00bda39c`](#insn-00bda39c)

## 命令位置別の参照

- [`00bda1ec`](#insn-00bda1ec) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda1f0`](#insn-00bda1f0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda1f4`](#insn-00bda1f4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda1f8`](#insn-00bda1f8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda1fc`](#insn-00bda1fc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda208`](#insn-00bda208) → [`00bda374`](#insn-00bda374) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda210`](#insn-00bda210) → [`00bda374`](#insn-00bda374) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda218`](#insn-00bda218) → [`00bda374`](#insn-00bda374) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda220`](#insn-00bda220) → `01126df8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00bda224`](#insn-00bda224) → [`00bda380`](#insn-00bda380) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda230`](#insn-00bda230) → [`00c5b330`](../00c5b/00c5b330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b330` · 推定シンボル `None` · 推定型 `None`
- [`00bda238`](#insn-00bda238) → [`00bda248`](#insn-00bda248) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda240`](#insn-00bda240) → `002b2609`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda244`](#insn-00bda244) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bda24c`](#insn-00bda24c) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bda29c`](#insn-00bda29c) → `01126c28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bda2a0`](#insn-00bda2a0) → `01126c48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bda2b0`](#insn-00bda2b0) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bda2bc`](#insn-00bda2bc) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bda2c0`](#insn-00bda2c0) → [`00bda418`](#insn-00bda418) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda2c8`](#insn-00bda2c8) → `01126d50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bda2dc`](#insn-00bda2dc) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bda2e8`](#insn-00bda2e8) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bda2ec`](#insn-00bda2ec) → [`00bda3d0`](#insn-00bda3d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda304`](#insn-00bda304) → [`00bda3d0`](#insn-00bda3d0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda320`](#insn-00bda320) → `01126d40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bda334`](#insn-00bda334) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bda354`](#insn-00bda354) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bda360`](#insn-00bda360) → [`00bda3c4`](#insn-00bda3c4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda370`](#insn-00bda370) → [`00bda418`](#insn-00bda418) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda378`](#insn-00bda378) → `002bfa53`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda37c`](#insn-00bda37c) → [`00bda394`](#insn-00bda394) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda384`](#insn-00bda384) → `002b7e50`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda388`](#insn-00bda388) → [`00c5ad70`](../00c5a/00c5ad70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ad70` · 推定シンボル `None` · 推定型 `None`
- [`00bda390`](#insn-00bda390) → `00310130`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda394`](#insn-00bda394) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bda3ac`](#insn-00bda3ac) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda3b0`](#insn-00bda3b0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda3b4`](#insn-00bda3b4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda3b8`](#insn-00bda3b8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda3d0`](#insn-00bda3d0) → [`00bda418`](#insn-00bda418) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda3d8`](#insn-00bda3d8) → `01126d58`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bda3e4`](#insn-00bda3e4) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bda3f0`](#insn-00bda3f0) → [`00c5b030`](../00c5b/00c5b030.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b030` · 推定シンボル `None` · 推定型 `None`
- [`00bda414`](#insn-00bda414) → [`00bda41c`](#insn-00bda41c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda458`](#insn-00bda458) → [`00bda398`](#insn-00bda398) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda45c`](#insn-00bda45c) → [`00c5b330`](../00c5b/00c5b330.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b330` · 推定シンボル `None` · 推定型 `None`
- [`00bda464`](#insn-00bda464) → [`00bda474`](#insn-00bda474) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bda46c`](#insn-00bda46c) → `002b2609`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bda470`](#insn-00bda470) → [`00c5b0d0`](../00c5b/00c5b0d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b0d0` · 推定シンボル `None` · 推定型 `None`
- [`00bda478`](#insn-00bda478) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bda4a8`](#insn-00bda4a8) → [`00bda39c`](#insn-00bda39c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bda1ec`](#insn-00bda1ec)

~~~json
{
  "source": "00bda1ec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda1f0`](#insn-00bda1f0)

~~~json
{
  "source": "00bda1f0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda1f4`](#insn-00bda1f4)

~~~json
{
  "source": "00bda1f4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda1f8`](#insn-00bda1f8)

~~~json
{
  "source": "00bda1f8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda1fc`](#insn-00bda1fc)

~~~json
{
  "source": "00bda1fc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda208`](#insn-00bda208)

~~~json
{
  "source": "00bda208",
  "target": "00bda374",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda210`](#insn-00bda210)

~~~json
{
  "source": "00bda210",
  "target": "00bda374",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda218`](#insn-00bda218)

~~~json
{
  "source": "00bda218",
  "target": "00bda374",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda220`](#insn-00bda220)

~~~json
{
  "source": "00bda220",
  "target": "01126df8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126df8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bda224`](#insn-00bda224)

~~~json
{
  "source": "00bda224",
  "target": "00bda380",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda230`](#insn-00bda230)

~~~json
{
  "source": "00bda230",
  "target": "00c5b330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda238`](#insn-00bda238)

~~~json
{
  "source": "00bda238",
  "target": "00bda248",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda240`](#insn-00bda240)

~~~json
{
  "source": "00bda240",
  "target": "002b2609",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2609",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2609",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bda244`](#insn-00bda244)

~~~json
{
  "source": "00bda244",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda24c`](#insn-00bda24c)

~~~json
{
  "source": "00bda24c",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda29c`](#insn-00bda29c)

~~~json
{
  "source": "00bda29c",
  "target": "01126c28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c28",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bda2a0`](#insn-00bda2a0)

~~~json
{
  "source": "00bda2a0",
  "target": "01126c48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c48",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bda2b0`](#insn-00bda2b0)

~~~json
{
  "source": "00bda2b0",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda2bc`](#insn-00bda2bc)

~~~json
{
  "source": "00bda2bc",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda2c0`](#insn-00bda2c0)

~~~json
{
  "source": "00bda2c0",
  "target": "00bda418",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda2c8`](#insn-00bda2c8)

~~~json
{
  "source": "00bda2c8",
  "target": "01126d50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d50",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bda2dc`](#insn-00bda2dc)

~~~json
{
  "source": "00bda2dc",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda2e8`](#insn-00bda2e8)

~~~json
{
  "source": "00bda2e8",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda2ec`](#insn-00bda2ec)

~~~json
{
  "source": "00bda2ec",
  "target": "00bda3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda304`](#insn-00bda304)

~~~json
{
  "source": "00bda304",
  "target": "00bda3d0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda320`](#insn-00bda320)

~~~json
{
  "source": "00bda320",
  "target": "01126d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bda334`](#insn-00bda334)

~~~json
{
  "source": "00bda334",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda354`](#insn-00bda354)

~~~json
{
  "source": "00bda354",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda360`](#insn-00bda360)

~~~json
{
  "source": "00bda360",
  "target": "00bda3c4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda370`](#insn-00bda370)

~~~json
{
  "source": "00bda370",
  "target": "00bda418",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda378`](#insn-00bda378)

~~~json
{
  "source": "00bda378",
  "target": "002bfa53",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bfa53",
  "offset": 0,
  "size": 37,
  "datatype": "string",
  "bytes": "70726f76696465725f69642026262069645f746f6b656e202626207261775f6e",
  "capture_start": "002bfa53",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bda37c`](#insn-00bda37c)

~~~json
{
  "source": "00bda37c",
  "target": "00bda394",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda384`](#insn-00bda384)

~~~json
{
  "source": "00bda384",
  "target": "002b7e50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7e50",
  "offset": 0,
  "size": 17,
  "datatype": "string",
  "bytes": "675f6d6574686f64735f63616368656400",
  "capture_start": "002b7e50",
  "capture_bytes": 17,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bda388`](#insn-00bda388)

~~~json
{
  "source": "00bda388",
  "target": "00c5ad70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda390`](#insn-00bda390)

~~~json
{
  "source": "00bda390",
  "target": "00310130",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00310130",
  "offset": 0,
  "size": 97,
  "datatype": "string",
  "bytes": "4669726562617365204175746820776173206e6f7420696e697469616c697a65",
  "capture_start": "00310130",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`00bda394`](#insn-00bda394)

~~~json
{
  "source": "00bda394",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda3ac`](#insn-00bda3ac)

~~~json
{
  "source": "00bda3ac",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda3b0`](#insn-00bda3b0)

~~~json
{
  "source": "00bda3b0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda3b4`](#insn-00bda3b4)

~~~json
{
  "source": "00bda3b4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda3b8`](#insn-00bda3b8)

~~~json
{
  "source": "00bda3b8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda3d0`](#insn-00bda3d0)

~~~json
{
  "source": "00bda3d0",
  "target": "00bda418",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda3d8`](#insn-00bda3d8)

~~~json
{
  "source": "00bda3d8",
  "target": "01126d58",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d58",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bda3e4`](#insn-00bda3e4)

~~~json
{
  "source": "00bda3e4",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda3f0`](#insn-00bda3f0)

~~~json
{
  "source": "00bda3f0",
  "target": "00c5b030",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda414`](#insn-00bda414)

~~~json
{
  "source": "00bda414",
  "target": "00bda41c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda458`](#insn-00bda458)

~~~json
{
  "source": "00bda458",
  "target": "00bda398",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda45c`](#insn-00bda45c)

~~~json
{
  "source": "00bda45c",
  "target": "00c5b330",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda464`](#insn-00bda464)

~~~json
{
  "source": "00bda464",
  "target": "00bda474",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bda46c`](#insn-00bda46c)

~~~json
{
  "source": "00bda46c",
  "target": "002b2609",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b2609",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "61707020213d206e756c6c70747200",
  "capture_start": "002b2609",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bda470`](#insn-00bda470)

~~~json
{
  "source": "00bda470",
  "target": "00c5b0d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda478`](#insn-00bda478)

~~~json
{
  "source": "00bda478",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bda4a8`](#insn-00bda4a8)

~~~json
{
  "source": "00bda4a8",
  "target": "00bda39c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
