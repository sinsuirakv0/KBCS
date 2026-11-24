# 00bdbcd4

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bdbc38`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bdb/00bdbc38.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0085.md#compare-f61f27b1b3d2d8dce3963656c63ec582)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bdccc8`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bdc/00bdccc8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0085.md#compare-7a87e970fd59a378984de7779a0855d4)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bdbcd4",
  "name": "FUN_00bdbcd4",
  "size": 576,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "b0775e9671eb2853bfc7280ab4737b8d731194bdf216bbfc3b8a66d034bd32ae",
  "source_text_sha256": "b0775e9671eb2853bfc7280ab4737b8d731194bdf216bbfc3b8a66d034bd32ae",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bdbcd4",
        "00bdbf13"
      ]
    ],
    "bytes_sha256": "4a0ca8060048c75ec37fbb652869c4ca4e46d3507029a4f92462b29b38b312dd",
    "instruction_count": 144,
    "instruction_bytes": 576,
    "body_bytes": 576,
    "indirect": 13,
    "unresolved": 13
  }
}
~~~

## 呼び出し元

- [00bdb930](../00bdb/00bdb930.md)
- [00bdbf14](../00bdb/00bdbf14.md)
- [00bdc1ec](../00bdc/00bdc1ec.md)

## 呼び出し先

- [00497874](../00497/00497874.md)
- [00589734](../00589/00589734.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c5ac70](../00c5a/00c5ac70.md)
- [00c5b080](../00c5b/00c5b080.md)
- [00c5b090](../00c5b/00c5b090.md)
- [00c5b150](../00c5b/00c5b150.md)
- [00c5b3f0](../00c5b/00c5b3f0.md)
- [00c5b4f0](../00c5b/00c5b4f0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2540 bytes

~~~c

void FUN_00bdbcd4(undefined8 *param_1,byte *param_2)

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
                    (plVar3,DAT_01126c28,DAT_01126c40,uVar4,param_1[0x3f]);
  (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
  cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
  if (cVar2 == '\0') {
    uVar4 = _ZN8firebase4util19StdVectorToJavaListEP7_JNIEnvRKNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEEE
                      (plVar3,param_2 + 0x18);
    cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
    if (cVar2 == '\0') {
      uVar6 = FUN_00497874(plVar3,uVar5,DAT_01126d18,uVar4);
      (**(code **)(*plVar3 + 0xb8))(plVar3,uVar4);
      cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
      pcVar7 = *(code **)(*plVar3 + 0xb8);
      if (cVar2 == '\0') {
        (*pcVar7)(plVar3,uVar6);
        uVar4 = _ZN8firebase4util8hash_map8GetClassEv();
        uVar6 = _ZN8firebase4util8hash_map11GetMethodIdENS1_6MethodE(0);
        local_50 = FUN_00589734(plVar3,uVar4,uVar6);
        _ZN8firebase4util15StdMapToJavaMapEP7_JNIEnvPP8_jobjectRKNSt6__ndk13mapINS6_12basic_stringIcNS6_11char_traitsIcEENS6_9allocatorIcEEEESD_NS6_4lessISD_EENSB_INS6_4pairIKSD_SD_EEEEEE
                  (plVar3,&local_50,param_2 + 0x30);
        uVar4 = FUN_00497874(plVar3,uVar5,DAT_01126d10,local_50);
        (**(code **)(*plVar3 + 0xb8))(plVar3,local_50);
        cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
        pcVar7 = *(code **)(*plVar3 + 0xb8);
        if (cVar2 == '\0') {
          (*pcVar7)(plVar3,uVar4);
          uVar4 = FUN_00497874(plVar3,uVar5,DAT_01126d20);
          (**(code **)(*plVar3 + 0xb8))(plVar3,uVar5);
          cVar2 = (**(code **)(*plVar3 + 0x720))(plVar3);
          if (cVar2 != '\0') {
            uVar4 = 0;
          }
          goto LAB_00bdbe94;
        }
      }
      (*pcVar7)(plVar3,uVar5);
    }
  }
  uVar4 = 0;
LAB_00bdbe94:
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
<a id="insn-00bdbcd4"></a> `00bdbcd4` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bdbcd8"></a> `00bdbcd8` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdbcdc"></a> `00bdbcdc` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdbce0"></a> `00bdbce0` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdbce4"></a> `00bdbce4` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdbce8"></a> `00bdbce8` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bdbcec"></a> `00bdbcec` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bdbcf0"></a> `00bdbcf0` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdbcf4"></a> `00bdbcf4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdbcf8"></a> `00bdbcf8` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-00bdbcfc"></a> `00bdbcfc` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdbd00"></a> `00bdbd00` | `00 00 40 f9` | ldr x0,[x0] | `FALL_THROUGH`
<a id="insn-00bdbd04"></a> `00bdbd04` | `13 fd 01 94` | bl 0x00c5b150 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbd08"></a> `00bdbd08` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00bdbd0c"></a> `00bdbd0c` | `a9 02 40 39` | ldrb w9,[x21] | `FALL_THROUGH`
<a id="insn-00bdbd10"></a> `00bdbd10` | `aa 0a 40 f9` | ldr x10,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00bdbd14"></a> `00bdbd14` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bdbd18"></a> `00bdbd18` | `08 9d 42 f9` | ldr x8,[x8, #0x538] | `FALL_THROUGH`
<a id="insn-00bdbd1c"></a> `00bdbd1c` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bdbd20"></a> `00bdbd20` | `41 15 95 9a` | csinc x1,x10,x21,ne | `FALL_THROUGH`
<a id="insn-00bdbd24"></a> `00bdbd24` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbd28"></a> `00bdbd28` | `48 2a 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdbd2c"></a> `00bdbd2c` | `49 2a 00 f0` | adrp x9,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdbd30"></a> `00bdbd30` | `01 15 46 f9` | ldr x1,[x8, #0xc28] | `FALL_THROUGH`
<a id="insn-00bdbd34"></a> `00bdbd34` | `22 21 46 f9` | ldr x2,[x9, #0xc40] | `FALL_THROUGH`
<a id="insn-00bdbd38"></a> `00bdbd38` | `84 fe 40 f9` | ldr x4,[x20, #0x1f8] | `FALL_THROUGH`
<a id="insn-00bdbd3c"></a> `00bdbd3c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdbd40"></a> `00bdbd40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbd44"></a> `00bdbd44` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bdbd48"></a> `00bdbd48` | `ca fb 01 94` | bl 0x00c5ac70 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbd4c"></a> `00bdbd4c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdbd50"></a> `00bdbd50` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00bdbd54"></a> `00bdbd54` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbd58"></a> `00bdbd58` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdbd5c"></a> `00bdbd5c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdbd60"></a> `00bdbd60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbd64"></a> `00bdbd64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdbd68"></a> `00bdbd68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbd6c"></a> `00bdbd6c` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bdbd70"></a> `00bdbd70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbd74"></a> `00bdbd74` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdbd78"></a> `00bdbd78` | `c1 08 00 54` | b.ne 0x00bdbe90 | `CONDITIONAL_JUMP`
<a id="insn-00bdbd7c"></a> `00bdbd7c` | `a1 62 00 91` | add x1,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00bdbd80"></a> `00bdbd80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbd84"></a> `00bdbd84` | `db fd 01 94` | bl 0x00c5b4f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbd88"></a> `00bdbd88` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdbd8c"></a> `00bdbd8c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdbd90"></a> `00bdbd90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbd94"></a> `00bdbd94` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bdbd98"></a> `00bdbd98` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbd9c"></a> `00bdbd9c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdbda0"></a> `00bdbda0` | `81 07 00 54` | b.ne 0x00bdbe90 | `CONDITIONAL_JUMP`
<a id="insn-00bdbda4"></a> `00bdbda4` | `48 2a 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdbda8"></a> `00bdbda8` | `02 8d 46 f9` | ldr x2,[x8, #0xd18] | `FALL_THROUGH`
<a id="insn-00bdbdac"></a> `00bdbdac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbdb0"></a> `00bdbdb0` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdbdb4"></a> `00bdbdb4` | `e3 03 16 aa` | mov x3,x22 | `FALL_THROUGH`
<a id="insn-00bdbdb8"></a> `00bdbdb8` | `af ee e2 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbdbc"></a> `00bdbdbc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdbdc0"></a> `00bdbdc0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bdbdc4"></a> `00bdbdc4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbdc8"></a> `00bdbdc8` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdbdcc"></a> `00bdbdcc` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdbdd0"></a> `00bdbdd0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbdd4"></a> `00bdbdd4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdbdd8"></a> `00bdbdd8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbddc"></a> `00bdbddc` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bdbde0"></a> `00bdbde0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbde4"></a> `00bdbde4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdbde8"></a> `00bdbde8` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdbdec"></a> `00bdbdec` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdbdf0"></a> `00bdbdf0` | `a1 04 00 54` | b.ne 0x00bdbe84 | `CONDITIONAL_JUMP`
<a id="insn-00bdbdf4"></a> `00bdbdf4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbdf8"></a> `00bdbdf8` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00bdbdfc"></a> `00bdbdfc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbe00"></a> `00bdbe00` | `a4 fc 01 94` | bl 0x00c5b090 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbe04"></a> `00bdbe04` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bdbe08"></a> `00bdbe08` | `e0 03 1f 2a` | mov w0,wzr | `FALL_THROUGH`
<a id="insn-00bdbe0c"></a> `00bdbe0c` | `9d fc 01 94` | bl 0x00c5b080 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbe10"></a> `00bdbe10` | `e2 03 00 aa` | mov x2,x0 | `FALL_THROUGH`
<a id="insn-00bdbe14"></a> `00bdbe14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbe18"></a> `00bdbe18` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bdbe1c"></a> `00bdbe1c` | `46 b6 e6 97` | bl 0x00589734 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbe20"></a> `00bdbe20` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-00bdbe24"></a> `00bdbe24` | `a2 c2 00 91` | add x2,x21,#0x30 | `FALL_THROUGH`
<a id="insn-00bdbe28"></a> `00bdbe28` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00bdbe2c"></a> `00bdbe2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbe30"></a> `00bdbe30` | `70 fd 01 94` | bl 0x00c5b3f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbe34"></a> `00bdbe34` | `48 2a 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdbe38"></a> `00bdbe38` | `02 89 46 f9` | ldr x2,[x8, #0xd10] | `FALL_THROUGH`
<a id="insn-00bdbe3c"></a> `00bdbe3c` | `e3 03 40 f9` | ldr x3,[sp] | `FALL_THROUGH`
<a id="insn-00bdbe40"></a> `00bdbe40` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbe44"></a> `00bdbe44` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdbe48"></a> `00bdbe48` | `8b ee e2 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbe4c"></a> `00bdbe4c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdbe50"></a> `00bdbe50` | `e1 03 40 f9` | ldr x1,[sp] | `FALL_THROUGH`
<a id="insn-00bdbe54"></a> `00bdbe54` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdbe58"></a> `00bdbe58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbe5c"></a> `00bdbe5c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdbe60"></a> `00bdbe60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbe64"></a> `00bdbe64` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdbe68"></a> `00bdbe68` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbe6c"></a> `00bdbe6c` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bdbe70"></a> `00bdbe70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbe74"></a> `00bdbe74` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdbe78"></a> `00bdbe78` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdbe7c"></a> `00bdbe7c` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdbe80"></a> `00bdbe80` | `e0 01 00 54` | b.eq 0x00bdbebc | `CONDITIONAL_JUMP`
<a id="insn-00bdbe84"></a> `00bdbe84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbe88"></a> `00bdbe88` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdbe8c"></a> `00bdbe8c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbe90"></a> `00bdbe90` | `e0 03 1f aa` | mov x0,xzr | `FALL_THROUGH`
<a id="insn-00bdbe94"></a> `00bdbe94` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bdbe98"></a> `00bdbe98` | `e9 07 40 f9` | ldr x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00bdbe9c"></a> `00bdbe9c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bdbea0"></a> `00bdbea0` | `81 03 00 54` | b.ne 0x00bdbf10 | `CONDITIONAL_JUMP`
<a id="insn-00bdbea4"></a> `00bdbea4` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bdbea8"></a> `00bdbea8` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bdbeac"></a> `00bdbeac` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00bdbeb0"></a> `00bdbeb0` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00bdbeb4"></a> `00bdbeb4` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00bdbeb8"></a> `00bdbeb8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bdbebc"></a> `00bdbebc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbec0"></a> `00bdbec0` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00bdbec4"></a> `00bdbec4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbec8"></a> `00bdbec8` | `48 2a 00 f0` | adrp x8,0x1126000 | `FALL_THROUGH`
<a id="insn-00bdbecc"></a> `00bdbecc` | `02 91 46 f9` | ldr x2,[x8, #0xd20] | `FALL_THROUGH`
<a id="insn-00bdbed0"></a> `00bdbed0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbed4"></a> `00bdbed4` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdbed8"></a> `00bdbed8` | `67 ee e2 97` | bl 0x00497874 | `UNCONDITIONAL_CALL`
<a id="insn-00bdbedc"></a> `00bdbedc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdbee0"></a> `00bdbee0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bdbee4"></a> `00bdbee4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbee8"></a> `00bdbee8` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00bdbeec"></a> `00bdbeec` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bdbef0"></a> `00bdbef0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbef4"></a> `00bdbef4` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00bdbef8"></a> `00bdbef8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bdbefc"></a> `00bdbefc` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00bdbf00"></a> `00bdbf00` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bdbf04"></a> `00bdbf04` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00bdbf08"></a> `00bdbf08` | `a0 02 9f 9a` | csel x0,x21,xzr,eq | `FALL_THROUGH`
<a id="insn-00bdbf0c"></a> `00bdbf0c` | `e2 ff ff 17` | b 0x00bdbe94 | `UNCONDITIONAL_JUMP`
<a id="insn-00bdbf10"></a> `00bdbf10` | `28 f0 01 94` | bl 0x00c57fb0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bdbcd4`](#insn-00bdbcd4) 範囲 `[['00bdbcd4', '00bdbd7b']]`
  - `CONDITIONAL_JUMP` [`00bdbd78`](#insn-00bdbd78) → [`00bdbe90`](#insn-00bdbe90)
  - `FALL_THROUGH` [`00bdbd78`](#insn-00bdbd78) → [`00bdbd7c`](#insn-00bdbd7c)
- ブロック [`00bdbd7c`](#insn-00bdbd7c) 範囲 `[['00bdbd7c', '00bdbda3']]`
  - `CONDITIONAL_JUMP` [`00bdbda0`](#insn-00bdbda0) → [`00bdbe90`](#insn-00bdbe90)
  - `FALL_THROUGH` [`00bdbda0`](#insn-00bdbda0) → [`00bdbda4`](#insn-00bdbda4)
- ブロック [`00bdbda4`](#insn-00bdbda4) 範囲 `[['00bdbda4', '00bdbdf3']]`
  - `CONDITIONAL_JUMP` [`00bdbdf0`](#insn-00bdbdf0) → [`00bdbe84`](#insn-00bdbe84)
  - `FALL_THROUGH` [`00bdbdf0`](#insn-00bdbdf0) → [`00bdbdf4`](#insn-00bdbdf4)
- ブロック [`00bdbdf4`](#insn-00bdbdf4) 範囲 `[['00bdbdf4', '00bdbe83']]`
  - `CONDITIONAL_JUMP` [`00bdbe80`](#insn-00bdbe80) → [`00bdbebc`](#insn-00bdbebc)
  - `FALL_THROUGH` [`00bdbe80`](#insn-00bdbe80) → [`00bdbe84`](#insn-00bdbe84)
- ブロック [`00bdbe84`](#insn-00bdbe84) 範囲 `[['00bdbe84', '00bdbe8f']]`
  - `FALL_THROUGH` [`00bdbe8c`](#insn-00bdbe8c) → [`00bdbe90`](#insn-00bdbe90)
- ブロック [`00bdbe90`](#insn-00bdbe90) 範囲 `[['00bdbe90', '00bdbe93']]`
  - `FALL_THROUGH` [`00bdbe90`](#insn-00bdbe90) → [`00bdbe94`](#insn-00bdbe94)
- ブロック [`00bdbe94`](#insn-00bdbe94) 範囲 `[['00bdbe94', '00bdbea3']]`
  - `CONDITIONAL_JUMP` [`00bdbea0`](#insn-00bdbea0) → [`00bdbf10`](#insn-00bdbf10)
  - `FALL_THROUGH` [`00bdbea0`](#insn-00bdbea0) → [`00bdbea4`](#insn-00bdbea4)
- ブロック [`00bdbea4`](#insn-00bdbea4) 範囲 `[['00bdbea4', '00bdbebb']]`
- ブロック [`00bdbebc`](#insn-00bdbebc) 範囲 `[['00bdbebc', '00bdbf0f']]`
  - `UNCONDITIONAL_JUMP` [`00bdbf0c`](#insn-00bdbf0c) → [`00bdbe94`](#insn-00bdbe94)
- ブロック [`00bdbf10`](#insn-00bdbf10) 範囲 `[['00bdbf10', '00bdbf13']]`

## 命令位置別の参照

- [`00bdbcd8`](#insn-00bdbcd8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbcdc`](#insn-00bdbcdc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbce0`](#insn-00bdbce0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbce4`](#insn-00bdbce4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbcfc`](#insn-00bdbcfc) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbd04`](#insn-00bdbd04) → [`00c5b150`](../00c5b/00c5b150.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b150` · 推定シンボル `None` · 推定型 `None`
- [`00bdbd30`](#insn-00bdbd30) → `01126c28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdbd34`](#insn-00bdbd34) → `01126c40`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdbd48`](#insn-00bdbd48) → [`00c5ac70`](../00c5a/00c5ac70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ac70` · 推定シンボル `None` · 推定型 `None`
- [`00bdbd78`](#insn-00bdbd78) → [`00bdbe90`](#insn-00bdbe90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbd84`](#insn-00bdbd84) → [`00c5b4f0`](../00c5b/00c5b4f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b4f0` · 推定シンボル `None` · 推定型 `None`
- [`00bdbda0`](#insn-00bdbda0) → [`00bdbe90`](#insn-00bdbe90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbda8`](#insn-00bdbda8) → `01126d18`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdbdb8`](#insn-00bdbdb8) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bdbdf0`](#insn-00bdbdf0) → [`00bdbe84`](#insn-00bdbe84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbe00`](#insn-00bdbe00) → [`00c5b090`](../00c5b/00c5b090.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b090` · 推定シンボル `None` · 推定型 `None`
- [`00bdbe0c`](#insn-00bdbe0c) → [`00c5b080`](../00c5b/00c5b080.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b080` · 推定シンボル `None` · 推定型 `None`
- [`00bdbe1c`](#insn-00bdbe1c) → [`00589734`](../00589/00589734.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00589734` · 推定シンボル `None` · 推定型 `None`
- [`00bdbe20`](#insn-00bdbe20) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbe30`](#insn-00bdbe30) → [`00c5b3f0`](../00c5b/00c5b3f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b3f0` · 推定シンボル `None` · 推定型 `None`
- [`00bdbe38`](#insn-00bdbe38) → `01126d10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdbe3c`](#insn-00bdbe3c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbe48`](#insn-00bdbe48) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bdbe50`](#insn-00bdbe50) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbe80`](#insn-00bdbe80) → [`00bdbebc`](#insn-00bdbebc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbe98`](#insn-00bdbe98) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbea0`](#insn-00bdbea0) → [`00bdbf10`](#insn-00bdbf10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbea4`](#insn-00bdbea4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbea8`](#insn-00bdbea8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbeac`](#insn-00bdbeac) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbeb0`](#insn-00bdbeb0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbecc`](#insn-00bdbecc) → `01126d20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bdbed8`](#insn-00bdbed8) → [`00497874`](../00497/00497874.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497874` · 推定シンボル `None` · 推定型 `None`
- [`00bdbf0c`](#insn-00bdbf0c) → [`00bdbe94`](#insn-00bdbe94) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bdbf10`](#insn-00bdbf10) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bdbcd8`](#insn-00bdbcd8)

~~~json
{
  "source": "00bdbcd8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbcdc`](#insn-00bdbcdc)

~~~json
{
  "source": "00bdbcdc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbce0`](#insn-00bdbce0)

~~~json
{
  "source": "00bdbce0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbce4`](#insn-00bdbce4)

~~~json
{
  "source": "00bdbce4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbcfc`](#insn-00bdbcfc)

~~~json
{
  "source": "00bdbcfc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbd04`](#insn-00bdbd04)

~~~json
{
  "source": "00bdbd04",
  "target": "00c5b150",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbd30`](#insn-00bdbd30)

~~~json
{
  "source": "00bdbd30",
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
- 参照命令 [`00bdbd34`](#insn-00bdbd34)

~~~json
{
  "source": "00bdbd34",
  "target": "01126c40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126c40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdbd48`](#insn-00bdbd48)

~~~json
{
  "source": "00bdbd48",
  "target": "00c5ac70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbd78`](#insn-00bdbd78)

~~~json
{
  "source": "00bdbd78",
  "target": "00bdbe90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbd84`](#insn-00bdbd84)

~~~json
{
  "source": "00bdbd84",
  "target": "00c5b4f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbda0`](#insn-00bdbda0)

~~~json
{
  "source": "00bdbda0",
  "target": "00bdbe90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbda8`](#insn-00bdbda8)

~~~json
{
  "source": "00bdbda8",
  "target": "01126d18",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d18",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdbdb8`](#insn-00bdbdb8)

~~~json
{
  "source": "00bdbdb8",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbdf0`](#insn-00bdbdf0)

~~~json
{
  "source": "00bdbdf0",
  "target": "00bdbe84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbe00`](#insn-00bdbe00)

~~~json
{
  "source": "00bdbe00",
  "target": "00c5b090",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbe0c`](#insn-00bdbe0c)

~~~json
{
  "source": "00bdbe0c",
  "target": "00c5b080",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbe1c`](#insn-00bdbe1c)

~~~json
{
  "source": "00bdbe1c",
  "target": "00589734",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbe20`](#insn-00bdbe20)

~~~json
{
  "source": "00bdbe20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbe30`](#insn-00bdbe30)

~~~json
{
  "source": "00bdbe30",
  "target": "00c5b3f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbe38`](#insn-00bdbe38)

~~~json
{
  "source": "00bdbe38",
  "target": "01126d10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdbe3c`](#insn-00bdbe3c)

~~~json
{
  "source": "00bdbe3c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbe48`](#insn-00bdbe48)

~~~json
{
  "source": "00bdbe48",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbe50`](#insn-00bdbe50)

~~~json
{
  "source": "00bdbe50",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbe80`](#insn-00bdbe80)

~~~json
{
  "source": "00bdbe80",
  "target": "00bdbebc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbe98`](#insn-00bdbe98)

~~~json
{
  "source": "00bdbe98",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbea0`](#insn-00bdbea0)

~~~json
{
  "source": "00bdbea0",
  "target": "00bdbf10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbea4`](#insn-00bdbea4)

~~~json
{
  "source": "00bdbea4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbea8`](#insn-00bdbea8)

~~~json
{
  "source": "00bdbea8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbeac`](#insn-00bdbeac)

~~~json
{
  "source": "00bdbeac",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbeb0`](#insn-00bdbeb0)

~~~json
{
  "source": "00bdbeb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbecc`](#insn-00bdbecc)

~~~json
{
  "source": "00bdbecc",
  "target": "01126d20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126d20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bdbed8`](#insn-00bdbed8)

~~~json
{
  "source": "00bdbed8",
  "target": "00497874",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bdbf0c`](#insn-00bdbf0c)

~~~json
{
  "source": "00bdbf0c",
  "target": "00bdbe94",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bdbf10`](#insn-00bdbf10)

~~~json
{
  "source": "00bdbf10",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
