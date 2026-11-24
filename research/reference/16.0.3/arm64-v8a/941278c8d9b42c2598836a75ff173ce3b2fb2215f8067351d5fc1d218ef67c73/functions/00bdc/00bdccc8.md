# 00bdccc8

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bdbcd4`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bdb/00bdbcd4.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-7a87e970fd59a378984de7779a0855d4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdccc8",
  "name": "FUN_00bdccc8",
  "size": 576,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "78bc1b1e3420acd0f447d442f445b485132a6e830b5f4e511758792cf74e095d",
  "source_text_sha256": "78bc1b1e3420acd0f447d442f445b485132a6e830b5f4e511758792cf74e095d",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdccc8",
        "00bdcf07"
      ]
    ],
    "bytes_sha256": "de38574fec8b026222309b959d21a92aa79f55b1e7bc4c955bf55d9a627be0e3",
    "instruction_count": 144,
    "instruction_bytes": 576,
    "body_bytes": 576,
    "indirect": 13,
    "unresolved": 13
  }
}
~~~

## 呼び出し元

- [00bdc924](../00bdc/00bdc924.md)
- [00bdcf08](../00bdc/00bdcf08.md)
- [00bdd1e0](../00bdd/00bdd1e0.md)

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00589a54](../00589/00589a54.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bc40](../00c5b/00c5bc40.md)
- [00c5c050](../00c5c/00c5c050.md)
- [00c5c060](../00c5c/00c5c060.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5c3c0](../00c5c/00c5c3c0.md)
- [00c5c4c0](../00c5c/00c5c4c0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2540 bytes

~~~c

void FUN_00bdccc8(undefined8 *param_1,byte *param_2)

{
  long lVar1;
  char cVar2;
  long *plVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  undefined8 uVar6;
  code *pcVar7;
  byte *pbVar8;
  undefined8 local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  plVar3 = (long *)_ZNK8firebase3App9GetJNIEnvEv(*param_1);
  pbVar8 = *(byte **)(param_2 + 0x10);
  if ((*param_2 & 1) == 0) {
    pbVar8 = param_2 + 1;
  }
  uVar4 = (**(code **)(*plVar3 + 0x538))(plVar3,pbVar8);
  uVar5 = _ZN7_JNIEnv22CallStaticObjectMethodEP7_jclassP10_jmethodIDz
                    (plVar3,DAT_01127be8,DAT_01127c00,uVar4,param_1[0x3f]);
  (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
  cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
  if (cVar2 == '\0') {
    uVar4 = _ZN8firebase4util19StdVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEEE
                      (plVar3,param_2 + 0x18);
    cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
    if (cVar2 == '\0') {
      uVar6 = FUN_00497b94(plVar3,uVar5,DAT_01127cd8,uVar4);
      (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
      cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
      pcVar7 = *(code **)(*plVar3 + 0xb8);
      if (cVar2 == '\0') {
        (*pcVar7)(plVar3,uVar6);
        uVar4 = _ZN8firebase4util8hash_map8GetClassEv();
        uVar6 = _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE(0);
        local_50 = FUN_00589a54(plVar3,uVar4,uVar6);
        _ZN8firebase4util15StdMapToJavaMapEP7_JNIEnvPP8_jobjectRKNSt6__ndk13mapINS6_12basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEESD_NS6_4lessISD_EENSB_INS6_4pairIKSD_SD_EEEEEE
                  (plVar3,&local_50,param_2 + 0x30);
        uVar4 = FUN_00497b94(plVar3,uVar5,DAT_01127cd0,local_50);
        (**(code **)(*plVar3 + 0xb8))(plVar3,local_50);
        cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
        pcVar7 = *(code **)(*plVar3 + 0xb8);
        if (cVar2 == '\0') {
          (*pcVar7)(plVar3,uVar4);
          uVar4 = FUN_00497b94(plVar3,uVar5,DAT_01127ce0);
          (**(code **)(*plVar3 + 0xb8))(plVar3,uVar5);
          cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
          if (cVar2 != '\0') {
            uVar4 = 0;
          }
          goto LAB_00bdce88;
        }
      }
      (*pcVar7)(plVar3,uVar5);
    }
  }
  uVar4 = 0;
LAB_00bdce88:
  if (*(long *)(lVar1 + 0x28) != local_48) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail(uVar4);
  }
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bdccc8"></a> `00bdccc8` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bdcccc"></a> `00bdcccc` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdccd0"></a> `00bdccd0` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdccd4"></a> `00bdccd4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdccd8"></a> `00bdccd8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdccdc"></a> `00bdccdc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bdcce0"></a> `00bdcce0` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdcce4"></a> `00bdcce4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdcce8"></a> `00bdcce8` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdccec"></a> `00bdccec` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bdccf0"></a> `00bdccf0` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdccf4"></a> `00bdccf4` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bdccf8"></a> `00bdccf8` | `0a fd 01 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bdccfc"></a> `00bdccfc` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdcd00"></a> `00bdcd00` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bdcd04"></a> `00bdcd04` | `aa 0a 40 f9` | ldr x10,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcd08"></a> `00bdcd08` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdcd0c"></a> `00bdcd0c` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bdcd10"></a> `00bdcd10` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bdcd14"></a> `00bdcd14` | `41 15 95 9a` | csinc x1,x10,x21,ne | `FALL_THROUGH`
<a id="insn-00bdcd18"></a> `00bdcd18` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcd1c"></a> `00bdcd1c` | `48 2a 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdcd20"></a> `00bdcd20` | `49 2a 00 f0` | adrp x9,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdcd24"></a> `00bdcd24` | `01 f5 45 f9` | ldr x1,[x8, #0xbe8] | `FALL_THROUGH`
<a id="insn-00bdcd28"></a> `00bdcd28` | `22 01 46 f9` | ldr x2,[x9, #0xc00] | `FALL_THROUGH`
<a id="insn-00bdcd2c"></a> `00bdcd2c` | `84 fe 40 f9` | ldr x4,[x20, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bdcd30"></a> `00bdcd30` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdcd34"></a> `00bdcd34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcd38"></a> `00bdcd38` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bdcd3c"></a> `00bdcd3c` | `c1 fb 01 94` | bl 0x00c5bc40 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcd40"></a> `00bdcd40` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdcd44"></a> `00bdcd44` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdcd48"></a> `00bdcd48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcd4c"></a> `00bdcd4c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdcd50"></a> `00bdcd50` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdcd54"></a> `00bdcd54` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcd58"></a> `00bdcd58` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdcd5c"></a> `00bdcd5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcd60"></a> `00bdcd60` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bdcd64"></a> `00bdcd64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcd68"></a> `00bdcd68` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdcd6c"></a> `00bdcd6c` | `c1 08 00 54` | b.ne 0x00bdce84 | `CONDITIONAL_JUMP`
<a id="insn-00bdcd70"></a> `00bdcd70` | `a1 62 00 91` | add x1,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00bdcd74"></a> `00bdcd74` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcd78"></a> `00bdcd78` | `d2 fd 01 94` | bl 0x00c5c4c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcd7c"></a> `00bdcd7c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdcd80"></a> `00bdcd80` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdcd84"></a> `00bdcd84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcd88"></a> `00bdcd88` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bdcd8c"></a> `00bdcd8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcd90"></a> `00bdcd90` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdcd94"></a> `00bdcd94` | `81 07 00 54` | b.ne 0x00bdce84 | `CONDITIONAL_JUMP`
<a id="insn-00bdcd98"></a> `00bdcd98` | `48 2a 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdcd9c"></a> `00bdcd9c` | `02 6d 46 f9` | ldr x2,[x8, #0xcd8] | `FALL_THROUGH`
<a id="insn-00bdcda0"></a> `00bdcda0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcda4"></a> `00bdcda4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdcda8"></a> `00bdcda8` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bdcdac"></a> `00bdcdac` | `7a eb e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcdb0"></a> `00bdcdb0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdcdb4"></a> `00bdcdb4` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdcdb8"></a> `00bdcdb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcdbc"></a> `00bdcdbc` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdcdc0"></a> `00bdcdc0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdcdc4"></a> `00bdcdc4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcdc8"></a> `00bdcdc8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdcdcc"></a> `00bdcdcc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcdd0"></a> `00bdcdd0` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bdcdd4"></a> `00bdcdd4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcdd8"></a> `00bdcdd8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdcddc"></a> `00bdcddc` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdcde0"></a> `00bdcde0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdcde4"></a> `00bdcde4` | `a1 04 00 54` | b.ne 0x00bdce78 | `CONDITIONAL_JUMP`
<a id="insn-00bdcde8"></a> `00bdcde8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcdec"></a> `00bdcdec` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bdcdf0"></a> `00bdcdf0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcdf4"></a> `00bdcdf4` | `9b fc 01 94` | bl 0x00c5c060 | `UNCONDITIONAL_CALL`
<a id="insn-00bdcdf8"></a> `00bdcdf8` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdcdfc"></a> `00bdcdfc` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdce00"></a> `00bdce00` | `94 fc 01 94` | bl 0x00c5c050 | `UNCONDITIONAL_CALL`
<a id="insn-00bdce04"></a> `00bdce04` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bdce08"></a> `00bdce08` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdce0c"></a> `00bdce0c` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdce10"></a> `00bdce10` | `11 b3 e6 97` | bl 0x00589a54 | `UNCONDITIONAL_CALL`
<a id="insn-00bdce14"></a> `00bdce14` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-00bdce18"></a> `00bdce18` | `a2 c2 00 91` | add x2,x21,#0x30 | `FALL_THROUGH`
<a id="insn-00bdce1c"></a> `00bdce1c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bdce20"></a> `00bdce20` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdce24"></a> `00bdce24` | `67 fd 01 94` | bl 0x00c5c3c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdce28"></a> `00bdce28` | `48 2a 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdce2c"></a> `00bdce2c` | `02 69 46 f9` | ldr x2,[x8, #0xcd0] | `FALL_THROUGH`
<a id="insn-00bdce30"></a> `00bdce30` | `e3 03 40 f9` | ldr x3,[sp] | `FALL_THROUGH`
<a id="insn-00bdce34"></a> `00bdce34` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdce38"></a> `00bdce38` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdce3c"></a> `00bdce3c` | `56 eb e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bdce40"></a> `00bdce40` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdce44"></a> `00bdce44` | `e1 03 40 f9` | ldr x1,[sp] | `FALL_THROUGH`
<a id="insn-00bdce48"></a> `00bdce48` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdce4c"></a> `00bdce4c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdce50"></a> `00bdce50` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdce54"></a> `00bdce54` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdce58"></a> `00bdce58` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdce5c"></a> `00bdce5c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdce60"></a> `00bdce60` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bdce64"></a> `00bdce64` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdce68"></a> `00bdce68` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdce6c"></a> `00bdce6c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdce70"></a> `00bdce70` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdce74"></a> `00bdce74` | `e0 01 00 54` | b.eq 0x00bdceb0 | `CONDITIONAL_JUMP`
<a id="insn-00bdce78"></a> `00bdce78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdce7c"></a> `00bdce7c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdce80"></a> `00bdce80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdce84"></a> `00bdce84` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bdce88"></a> `00bdce88` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdce8c"></a> `00bdce8c` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdce90"></a> `00bdce90` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdce94"></a> `00bdce94` | `81 03 00 54` | b.ne 0x00bdcf04 | `CONDITIONAL_JUMP`
<a id="insn-00bdce98"></a> `00bdce98` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdce9c"></a> `00bdce9c` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdcea0"></a> `00bdcea0` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdcea4"></a> `00bdcea4` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdcea8"></a> `00bdcea8` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bdceac"></a> `00bdceac` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdceb0"></a> `00bdceb0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdceb4"></a> `00bdceb4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdceb8"></a> `00bdceb8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcebc"></a> `00bdcebc` | `48 2a 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bdcec0"></a> `00bdcec0` | `02 71 46 f9` | ldr x2,[x8, #0xce0] | `FALL_THROUGH`
<a id="insn-00bdcec4"></a> `00bdcec4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcec8"></a> `00bdcec8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdcecc"></a> `00bdcecc` | `32 eb e2 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bdced0"></a> `00bdced0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdced4"></a> `00bdced4` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdced8"></a> `00bdced8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcedc"></a> `00bdcedc` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdcee0"></a> `00bdcee0` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdcee4"></a> `00bdcee4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcee8"></a> `00bdcee8` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdceec"></a> `00bdceec` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdcef0"></a> `00bdcef0` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bdcef4"></a> `00bdcef4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdcef8"></a> `00bdcef8` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdcefc"></a> `00bdcefc` | `a0 02 9f 9a` | csel x0,x21,xzr,eq | `FALL_THROUGH`
<a id="insn-00bdcf00"></a> `00bdcf00` | `e2 ff ff 17` | b 0x00bdce88 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdcf04"></a> `00bdcf04` | `1f f0 01 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdccc8`](#insn-00bdccc8) 範囲 `[['00bdccc8', '00bdcd6f']]`
  - `CONDITIONAL_JUMP` [`00bdcd6c`](#insn-00bdcd6c) → [`00bdce84`](#insn-00bdce84)
  - `FALL_THROUGH` [`00bdcd6c`](#insn-00bdcd6c) → [`00bdcd70`](#insn-00bdcd70)
- ブロック [`00bdcd70`](#insn-00bdcd70) 範囲 `[['00bdcd70', '00bdcd97']]`
  - `CONDITIONAL_JUMP` [`00bdcd94`](#insn-00bdcd94) → [`00bdce84`](#insn-00bdce84)
  - `FALL_THROUGH` [`00bdcd94`](#insn-00bdcd94) → [`00bdcd98`](#insn-00bdcd98)
- ブロック [`00bdcd98`](#insn-00bdcd98) 範囲 `[['00bdcd98', '00bdcde7']]`
  - `CONDITIONAL_JUMP` [`00bdcde4`](#insn-00bdcde4) → [`00bdce78`](#insn-00bdce78)
  - `FALL_THROUGH` [`00bdcde4`](#insn-00bdcde4) → [`00bdcde8`](#insn-00bdcde8)
- ブロック [`00bdcde8`](#insn-00bdcde8) 範囲 `[['00bdcde8', '00bdce77']]`
  - `CONDITIONAL_JUMP` [`00bdce74`](#insn-00bdce74) → [`00bdceb0`](#insn-00bdceb0)
  - `FALL_THROUGH` [`00bdce74`](#insn-00bdce74) → [`00bdce78`](#insn-00bdce78)
- ブロック [`00bdce78`](#insn-00bdce78) 範囲 `[['00bdce78', '00bdce83']]`
  - `FALL_THROUGH` [`00bdce80`](#insn-00bdce80) → [`00bdce84`](#insn-00bdce84)
- ブロック [`00bdce84`](#insn-00bdce84) 範囲 `[['00bdce84', '00bdce87']]`
  - `FALL_THROUGH` [`00bdce84`](#insn-00bdce84) → [`00bdce88`](#insn-00bdce88)
- ブロック [`00bdce88`](#insn-00bdce88) 範囲 `[['00bdce88', '00bdce97']]`
  - `CONDITIONAL_JUMP` [`00bdce94`](#insn-00bdce94) → [`00bdcf04`](#insn-00bdcf04)
  - `FALL_THROUGH` [`00bdce94`](#insn-00bdce94) → [`00bdce98`](#insn-00bdce98)
- ブロック [`00bdce98`](#insn-00bdce98) 範囲 `[['00bdce98', '00bdceaf']]`
- ブロック [`00bdceb0`](#insn-00bdceb0) 範囲 `[['00bdceb0', '00bdcf03']]`
  - `UNCONDITIONAL_JUMP` [`00bdcf00`](#insn-00bdcf00) → [`00bdce88`](#insn-00bdce88)
- ブロック [`00bdcf04`](#insn-00bdcf04) 範囲 `[['00bdcf04', '00bdcf07']]`

## 命令位置別の参照

- [`00bdcccc`](#insn-00bdcccc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdccd0`](#insn-00bdccd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdccd4`](#insn-00bdccd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdccd8`](#insn-00bdccd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdccf0`](#insn-00bdccf0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdccf8`](#insn-00bdccf8) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd24`](#insn-00bdcd24) → `01127be8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcd28`](#insn-00bdcd28) → `01127c00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcd3c`](#insn-00bdcd3c) → [`00c5bc40`](../00c5b/00c5bc40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bc40` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd6c`](#insn-00bdcd6c) → [`00bdce84`](#insn-00bdce84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd78`](#insn-00bdcd78) → [`00c5c4c0`](../00c5c/00c5c4c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c4c0` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd94`](#insn-00bdcd94) → [`00bdce84`](#insn-00bdce84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcd9c`](#insn-00bdcd9c) → `01127cd8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcdac`](#insn-00bdcdac) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bdcde4`](#insn-00bdcde4) → [`00bdce78`](#insn-00bdce78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcdf4`](#insn-00bdcdf4) → [`00c5c060`](../00c5c/00c5c060.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c060` · 推定シンボル `None` · 推定型 `None`
- [`00bdce00`](#insn-00bdce00) → [`00c5c050`](../00c5c/00c5c050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c050` · 推定シンボル `None` · 推定型 `None`
- [`00bdce10`](#insn-00bdce10) → [`00589a54`](../00589/00589a54.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00589a54` · 推定シンボル `None` · 推定型 `None`
- [`00bdce14`](#insn-00bdce14) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce24`](#insn-00bdce24) → [`00c5c3c0`](../00c5c/00c5c3c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c3c0` · 推定シンボル `None` · 推定型 `None`
- [`00bdce2c`](#insn-00bdce2c) → `01127cd0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdce30`](#insn-00bdce30) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce3c`](#insn-00bdce3c) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bdce44`](#insn-00bdce44) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce74`](#insn-00bdce74) → [`00bdceb0`](#insn-00bdceb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce8c`](#insn-00bdce8c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce94`](#insn-00bdce94) → [`00bdcf04`](#insn-00bdcf04) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce98`](#insn-00bdce98) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdce9c`](#insn-00bdce9c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcea0`](#insn-00bdcea0) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcea4`](#insn-00bdcea4) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcec0`](#insn-00bdcec0) → `01127ce0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdcecc`](#insn-00bdcecc) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf00`](#insn-00bdcf00) → [`00bdce88`](#insn-00bdce88) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdcf04`](#insn-00bdcf04) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdcccc`](#insn-00bdcccc)

~~~json
{
  "source": "00bdcccc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdccd0`](#insn-00bdccd0)

~~~json
{
  "source": "00bdccd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdccd4`](#insn-00bdccd4)

~~~json
{
  "source": "00bdccd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdccd8`](#insn-00bdccd8)

~~~json
{
  "source": "00bdccd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdccf0`](#insn-00bdccf0)

~~~json
{
  "source": "00bdccf0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdccf8`](#insn-00bdccf8)

~~~json
{
  "source": "00bdccf8",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcd24`](#insn-00bdcd24)

~~~json
{
  "source": "00bdcd24",
  "target": "01127be8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127be8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcd28`](#insn-00bdcd28)

~~~json
{
  "source": "00bdcd28",
  "target": "01127c00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcd3c`](#insn-00bdcd3c)

~~~json
{
  "source": "00bdcd3c",
  "target": "00c5bc40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcd6c`](#insn-00bdcd6c)

~~~json
{
  "source": "00bdcd6c",
  "target": "00bdce84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcd78`](#insn-00bdcd78)

~~~json
{
  "source": "00bdcd78",
  "target": "00c5c4c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcd94`](#insn-00bdcd94)

~~~json
{
  "source": "00bdcd94",
  "target": "00bdce84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcd9c`](#insn-00bdcd9c)

~~~json
{
  "source": "00bdcd9c",
  "target": "01127cd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127cd8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcdac`](#insn-00bdcdac)

~~~json
{
  "source": "00bdcdac",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcde4`](#insn-00bdcde4)

~~~json
{
  "source": "00bdcde4",
  "target": "00bdce78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcdf4`](#insn-00bdcdf4)

~~~json
{
  "source": "00bdcdf4",
  "target": "00c5c060",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdce00`](#insn-00bdce00)

~~~json
{
  "source": "00bdce00",
  "target": "00c5c050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdce10`](#insn-00bdce10)

~~~json
{
  "source": "00bdce10",
  "target": "00589a54",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdce14`](#insn-00bdce14)

~~~json
{
  "source": "00bdce14",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce24`](#insn-00bdce24)

~~~json
{
  "source": "00bdce24",
  "target": "00c5c3c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdce2c`](#insn-00bdce2c)

~~~json
{
  "source": "00bdce2c",
  "target": "01127cd0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127cd0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdce30`](#insn-00bdce30)

~~~json
{
  "source": "00bdce30",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce3c`](#insn-00bdce3c)

~~~json
{
  "source": "00bdce3c",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdce44`](#insn-00bdce44)

~~~json
{
  "source": "00bdce44",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce74`](#insn-00bdce74)

~~~json
{
  "source": "00bdce74",
  "target": "00bdceb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce8c`](#insn-00bdce8c)

~~~json
{
  "source": "00bdce8c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce94`](#insn-00bdce94)

~~~json
{
  "source": "00bdce94",
  "target": "00bdcf04",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce98`](#insn-00bdce98)

~~~json
{
  "source": "00bdce98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdce9c`](#insn-00bdce9c)

~~~json
{
  "source": "00bdce9c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcea0`](#insn-00bdcea0)

~~~json
{
  "source": "00bdcea0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcea4`](#insn-00bdcea4)

~~~json
{
  "source": "00bdcea4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcec0`](#insn-00bdcec0)

~~~json
{
  "source": "00bdcec0",
  "target": "01127ce0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127ce0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdcecc`](#insn-00bdcecc)

~~~json
{
  "source": "00bdcecc",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdcf00`](#insn-00bdcf00)

~~~json
{
  "source": "00bdcf00",
  "target": "00bdce88",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdcf04`](#insn-00bdcf04)

~~~json
{
  "source": "00bdcf04",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
