# 004bfcdc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `004bf9bc`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004bf/004bf9bc.md) · 移動量 `+0x320`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0008.md#compare-268425f10e2eba5e239675e6502f344b)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004bfcdc",
  "name": "_ZN5Botan14ECB_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm",
  "size": 580,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "ce0d5f745fa1c09427f52e70dd65c55b8c0ae4f3111b2cd0b59b4f299b9a719f",
  "source_text_sha256": "ce0d5f745fa1c09427f52e70dd65c55b8c0ae4f3111b2cd0b59b4f299b9a719f",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004bfcdc",
        "004bff1b"
      ],
      [
        "004bff8c",
        "004bff8f"
      ]
    ],
    "bytes_sha256": "3de91e3f184effcd1c05b334d07ba5041dd07d96e9c9917cfd12036eab98e875",
    "instruction_count": 145,
    "instruction_bytes": 580,
    "body_bytes": 580,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [0054084c](../00540/0054084c.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c58f90](../00c58/00c58f90.md)
- [00c58fb0](../00c58/00c58fb0.md)
- [00c59010](../00c59/00c59010.md)
- [00c596f0](../00c59/00c596f0.md)
- [00c597f0](../00c59/00c597f0.md)
- [00c59e60](../00c59/00c59e60.md)

## 関連文字列（未確認候補）

~~~text
"/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.3/Source/android_cpp/app/src/main/cpp/botan/botan_all.cpp"
"/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.3/Source/android_cpp/app/src/main/cpp/botan/botan_all.h"
": Ciphertext not a multiple of block size"
"Offset is sane"
"Offset ok"
"buffer.size() >= offset"
"finish"
"update"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3739 bytes

~~~c

void _ZN5Botan14ECB_Decryption6finishERNSt6__ndk16vectorIhNS_16secure_allocatorIhEEEEm
               (long *param_1,long *param_2,ulong param_3)

{
  long lVar1;
  ulong uVar2;
  long lVar3;
  long lVar4;
  undefined8 uVar5;
  undefined8 *puVar6;
  ulong uVar7;
  ulong uVar8;
  undefined1 auStack_78 [24];
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  lVar4 = *param_2;
  lVar3 = param_2[1];
  if ((ulong)(lVar3 - lVar4) < param_3) {
    if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
      _ZN5Botan17assertion_failureEPKcS1_S1_S1_i
                ("buffer.size() >= offset","Offset is sane","finish",
                 "/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.3/Source/android_cpp/app/src/main/cpp/botan/botan_all.cpp"
                 ,0x18a8);
    }
  }
  else {
    uVar2 = (**(code **)(*(long *)param_1[1] + 0x30))();
    uVar7 = (lVar3 - lVar4) - param_3;
    if (uVar7 != 0) {
      uVar8 = 0;
      if (uVar2 != 0) {
        uVar8 = uVar7 / uVar2;
      }
      if (uVar7 == uVar8 * uVar2) {
        uVar7 = param_2[1] - *param_2;
        if (uVar7 < param_3) {
          if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
            _ZN5Botan17assertion_failureEPKcS1_S1_S1_i
                      ("buffer.size() >= offset","Offset ok","update",
                       "/Users/battlecats/.jenkins/workspace/Battlecats-Jp-Android/release_jp-android-16.0.3/Source/android_cpp/app/src/main/cpp/botan/botan_all.h"
                       ,0x15e7);
          }
        }
        else {
          lVar3 = (**(code **)(*param_1 + 0x18))(param_1,*param_2 + param_3,uVar7 - param_3);
          lVar4 = param_2[1];
          param_3 = lVar3 + param_3;
          uVar7 = lVar4 - *param_2;
          if (param_3 < uVar7 || param_3 - uVar7 == 0) {
            if (param_3 < uVar7) {
              lVar4 = *param_2 + param_3;
              param_2[1] = lVar4;
            }
          }
          else {
            FUN_0054084c(param_2,param_3 - uVar7);
            lVar4 = param_2[1];
          }
          lVar4 = (**(code **)(*(long *)param_1[2] + 8))((long *)param_1[2],lVar4 - uVar2,uVar2);
          uVar8 = param_2[1] - *param_2;
          uVar7 = uVar8 + (lVar4 - uVar2);
          if (uVar8 < uVar7) {
            if (*(long *)(lVar1 + 0x28) == local_48) {
              FUN_0054084c(param_2);
              return;
            }
          }
          else {
            if (uVar8 != uVar7) {
              param_2[1] = *param_2 + uVar7;
            }
            if (*(long *)(lVar1 + 0x28) == local_48) {
              return;
            }
          }
        }
        goto LAB_004bff8c;
      }
    }
    uVar5 = __cxa_allocate_exception(0x20);
    _ZNK5Botan8ECB_Mode4nameEv(auStack_78,param_1);
    puVar6 = (undefined8 *)
             _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
                       (auStack_78,": Ciphertext not a multiple of block size");
    local_50 = puVar6[2];
    uStack_58 = puVar6[1];
    local_60 = *puVar6;
    puVar6[1] = 0;
    puVar6[2] = 0;
    *puVar6 = 0;
    _ZN5Botan14Decoding_ErrorC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (uVar5,&local_60);
    if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar5,PTR__ZTIN5Botan14Decoding_ErrorE_00c9bdf0,FUN_00535bc8);
    }
  }
LAB_004bff8c:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004bfcdc"></a> `004bfcdc` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-004bfce0"></a> `004bfce0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bfce4"></a> `004bfce4` | `f7 2b 00 f9` | str x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004bfce8"></a> `004bfce8` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004bfcec"></a> `004bfcec` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004bfcf0"></a> `004bfcf0` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-004bfcf4"></a> `004bfcf4` | `57 d0 3b d5` | mrs x23,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004bfcf8"></a> `004bfcf8` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-004bfcfc"></a> `004bfcfc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bfd00"></a> `004bfd00` | `29 20 40 a9` | ldp x9,x8,[x1] | `FALL_THROUGH`
<a id="insn-004bfd04"></a> `004bfd04` | `15 01 09 cb` | sub x21,x8,x9 | `FALL_THROUGH`
<a id="insn-004bfd08"></a> `004bfd08` | `bf 02 02 eb` | cmp x21,x2 | `FALL_THROUGH`
<a id="insn-004bfd0c"></a> `004bfd0c` | `03 0d 00 54` | b.cc 0x004bfeac | `CONDITIONAL_JUMP`
<a id="insn-004bfd10"></a> `004bfd10` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004bfd14"></a> `004bfd14` | `00 04 40 f9` | ldr x0,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004bfd18"></a> `004bfd18` | `f6 03 02 aa` | mov x22,x2 | `FALL_THROUGH`
<a id="insn-004bfd1c"></a> `004bfd1c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-004bfd20"></a> `004bfd20` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-004bfd24"></a> `004bfd24` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-004bfd28"></a> `004bfd28` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004bfd2c"></a> `004bfd2c` | `a8 02 16 eb` | subs x8,x21,x22 | `FALL_THROUGH`
<a id="insn-004bfd30"></a> `004bfd30` | `00 08 00 54` | b.eq 0x004bfe30 | `CONDITIONAL_JUMP`
<a id="insn-004bfd34"></a> `004bfd34` | `09 09 c0 9a` | udiv x9,x8,x0 | `FALL_THROUGH`
<a id="insn-004bfd38"></a> `004bfd38` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-004bfd3c"></a> `004bfd3c` | `28 a1 00 9b` | msub x8,x9,x0,x8 | `FALL_THROUGH`
<a id="insn-004bfd40"></a> `004bfd40` | `88 07 00 b5` | cbnz x8,0x004bfe30 | `CONDITIONAL_JUMP`
<a id="insn-004bfd44"></a> `004bfd44` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-004bfd48"></a> `004bfd48` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004bfd4c"></a> `004bfd4c` | `22 01 16 eb` | subs x2,x9,x22 | `FALL_THROUGH`
<a id="insn-004bfd50"></a> `004bfd50` | `a3 0c 00 54` | b.cc 0x004bfee4 | `CONDITIONAL_JUMP`
<a id="insn-004bfd54"></a> `004bfd54` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-004bfd58"></a> `004bfd58` | `01 01 16 8b` | add x1,x8,x22 | `FALL_THROUGH`
<a id="insn-004bfd5c"></a> `004bfd5c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004bfd60"></a> `004bfd60` | `29 0d 40 f9` | ldr x9,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-004bfd64"></a> `004bfd64` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004bfd68"></a> `004bfd68` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-004bfd6c"></a> `004bfd6c` | `0a 00 16 8b` | add x10,x0,x22 | `FALL_THROUGH`
<a id="insn-004bfd70"></a> `004bfd70` | `2b 01 08 cb` | sub x11,x9,x8 | `FALL_THROUGH`
<a id="insn-004bfd74"></a> `004bfd74` | `41 01 0b eb` | subs x1,x10,x11 | `FALL_THROUGH`
<a id="insn-004bfd78"></a> `004bfd78` | `a9 00 00 54` | b.ls 0x004bfd8c | `CONDITIONAL_JUMP`
<a id="insn-004bfd7c"></a> `004bfd7c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bfd80"></a> `004bfd80` | `b3 02 02 94` | bl 0x0054084c | `UNCONDITIONAL_CALL`
<a id="insn-004bfd84"></a> `004bfd84` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-004bfd88"></a> `004bfd88` | `04 00 00 14` | b 0x004bfd98 | `UNCONDITIONAL_JUMP`
<a id="insn-004bfd8c"></a> `004bfd8c` | `62 00 00 54` | b.cs 0x004bfd98 | `CONDITIONAL_JUMP`
<a id="insn-004bfd90"></a> `004bfd90` | `09 01 0a 8b` | add x9,x8,x10 | `FALL_THROUGH`
<a id="insn-004bfd94"></a> `004bfd94` | `69 06 00 f9` | str x9,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-004bfd98"></a> `004bfd98` | `80 0a 40 f9` | ldr x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-004bfd9c"></a> `004bfd9c` | `29 01 08 cb` | sub x9,x9,x8 | `FALL_THROUGH`
<a id="insn-004bfda0"></a> `004bfda0` | `e2 03 15 aa` | mov x2,x21 | `FALL_THROUGH`
<a id="insn-004bfda4"></a> `004bfda4` | `29 01 15 cb` | sub x9,x9,x21 | `FALL_THROUGH`
<a id="insn-004bfda8"></a> `004bfda8` | `0a 00 40 f9` | ldr x10,[x0] | `FALL_THROUGH`
<a id="insn-004bfdac"></a> `004bfdac` | `01 01 09 8b` | add x1,x8,x9 | `FALL_THROUGH`
<a id="insn-004bfdb0"></a> `004bfdb0` | `4a 05 40 f9` | ldr x10,[x10, #0x8] | `FALL_THROUGH`
<a id="insn-004bfdb4"></a> `004bfdb4` | `40 01 3f d6` | blr x10 | `COMPUTED_CALL`
<a id="insn-004bfdb8"></a> `004bfdb8` | `68 26 40 a9` | ldp x8,x9,[x19] | `FALL_THROUGH`
<a id="insn-004bfdbc"></a> `004bfdbc` | `01 00 15 cb` | sub x1,x0,x21 | `FALL_THROUGH`
<a id="insn-004bfdc0"></a> `004bfdc0` | `2a 01 08 cb` | sub x10,x9,x8 | `FALL_THROUGH`
<a id="insn-004bfdc4"></a> `004bfdc4` | `49 01 01 8b` | add x9,x10,x1 | `FALL_THROUGH`
<a id="insn-004bfdc8"></a> `004bfdc8` | `5f 01 09 eb` | cmp x10,x9 | `FALL_THROUGH`
<a id="insn-004bfdcc"></a> `004bfdcc` | `82 01 00 54` | b.cs 0x004bfdfc | `CONDITIONAL_JUMP`
<a id="insn-004bfdd0"></a> `004bfdd0` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-004bfdd4"></a> `004bfdd4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bfdd8"></a> `004bfdd8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bfddc"></a> `004bfddc` | `81 0d 00 54` | b.ne 0x004bff8c | `CONDITIONAL_JUMP`
<a id="insn-004bfde0"></a> `004bfde0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bfde4"></a> `004bfde4` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004bfde8"></a> `004bfde8` | `f7 2b 40 f9` | ldr x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004bfdec"></a> `004bfdec` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004bfdf0"></a> `004bfdf0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bfdf4"></a> `004bfdf4` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-004bfdf8"></a> `004bfdf8` | `95 02 02 14` | b 0x0054084c | `CALL_TERMINATOR`
<a id="insn-004bfdfc"></a> `004bfdfc` | `69 00 00 54` | b.ls 0x004bfe08 | `CONDITIONAL_JUMP`
<a id="insn-004bfe00"></a> `004bfe00` | `08 01 09 8b` | add x8,x8,x9 | `FALL_THROUGH`
<a id="insn-004bfe04"></a> `004bfe04` | `68 06 00 f9` | str x8,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-004bfe08"></a> `004bfe08` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-004bfe0c"></a> `004bfe0c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bfe10"></a> `004bfe10` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bfe14"></a> `004bfe14` | `c1 0b 00 54` | b.ne 0x004bff8c | `CONDITIONAL_JUMP`
<a id="insn-004bfe18"></a> `004bfe18` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004bfe1c"></a> `004bfe1c` | `f7 2b 40 f9` | ldr x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004bfe20"></a> `004bfe20` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004bfe24"></a> `004bfe24` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004bfe28"></a> `004bfe28` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-004bfe2c"></a> `004bfe2c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004bfe30"></a> `004bfe30` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-004bfe34"></a> `004bfe34` | `57 64 1e 94` | bl 0x00c58f90 | `UNCONDITIONAL_CALL`
<a id="insn-004bfe38"></a> `004bfe38` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004bfe3c"></a> `004bfe3c` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004bfe40"></a> `004bfe40` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004bfe44"></a> `004bfe44` | `07 68 1e 94` | bl 0x00c59e60 | `UNCONDITIONAL_CALL`
<a id="insn-004bfe48"></a> `004bfe48` | `01 f0 ff d0` | adrp x1,0x2c1000 | `FALL_THROUGH`
<a id="insn-004bfe4c"></a> `004bfe4c` | `21 74 03 91` | add x1,x1,#0xdd | `FALL_THROUGH`
<a id="insn-004bfe50"></a> `004bfe50` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004bfe54"></a> `004bfe54` | `6f 64 1e 94` | bl 0x00c59010 | `UNCONDITIONAL_CALL`
<a id="insn-004bfe58"></a> `004bfe58` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004bfe5c"></a> `004bfe5c` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-004bfe60"></a> `004bfe60` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-004bfe64"></a> `004bfe64` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004bfe68"></a> `004bfe68` | `e0 0b 80 3d` | str q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-004bfe6c"></a> `004bfe6c` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004bfe70"></a> `004bfe70` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-004bfe74"></a> `004bfe74` | `e1 83 00 91` | add x1,sp,#0x20 | `FALL_THROUGH`
<a id="insn-004bfe78"></a> `004bfe78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bfe7c"></a> `004bfe7c` | `5d 66 1e 94` | bl 0x00c597f0 | `UNCONDITIONAL_CALL`
<a id="insn-004bfe80"></a> `004bfe80` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-004bfe84"></a> `004bfe84` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bfe88"></a> `004bfe88` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bfe8c"></a> `004bfe8c` | `01 08 00 54` | b.ne 0x004bff8c | `CONDITIONAL_JUMP`
<a id="insn-004bfe90"></a> `004bfe90` | `e1 3e 00 90` | adrp x1,0xc9b000 | `FALL_THROUGH`
<a id="insn-004bfe94"></a> `004bfe94` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004bfe98"></a> `004bfe98` | `82 e9 3a 10` | adr x2,0x535bc8 | `FALL_THROUGH`
<a id="insn-004bfe9c"></a> `004bfe9c` | `21 f8 46 f9` | ldr x1,[x1, #0xdf0] | `FALL_THROUGH`
<a id="insn-004bfea0"></a> `004bfea0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004bfea4"></a> `004bfea4` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-004bfea8"></a> `004bfea8` | `42 64 1e 94` | bl 0x00c58fb0 | `CALL_TERMINATOR`
<a id="insn-004bfeac"></a> `004bfeac` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-004bfeb0"></a> `004bfeb0` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bfeb4"></a> `004bfeb4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bfeb8"></a> `004bfeb8` | `a1 06 00 54` | b.ne 0x004bff8c | `CONDITIONAL_JUMP`
<a id="insn-004bfebc"></a> `004bfebc` | `60 ef ff d0` | adrp x0,0x2ad000 | `FALL_THROUGH`
<a id="insn-004bfec0"></a> `004bfec0` | `00 58 1f 91` | add x0,x0,#0x7d6 | `FALL_THROUGH`
<a id="insn-004bfec4"></a> `004bfec4` | `a1 ef ff b0` | adrp x1,0x2b4000 | `FALL_THROUGH`
<a id="insn-004bfec8"></a> `004bfec8` | `21 b0 38 91` | add x1,x1,#0xe2c | `FALL_THROUGH`
<a id="insn-004bfecc"></a> `004bfecc` | `c2 ef ff f0` | adrp x2,0x2ba000 | `FALL_THROUGH`
<a id="insn-004bfed0"></a> `004bfed0` | `42 5c 0b 91` | add x2,x2,#0x2d7 | `FALL_THROUGH`
<a id="insn-004bfed4"></a> `004bfed4` | `23 ef ff d0` | adrp x3,0x2a5000 | `FALL_THROUGH`
<a id="insn-004bfed8"></a> `004bfed8` | `63 a8 10 91` | add x3,x3,#0x42a | `FALL_THROUGH`
<a id="insn-004bfedc"></a> `004bfedc` | `04 15 83 52` | mov w4,#0x18a8 | `FALL_THROUGH`
<a id="insn-004bfee0"></a> `004bfee0` | `04 66 1e 94` | bl 0x00c596f0 | `CALL_TERMINATOR`
<a id="insn-004bfee4"></a> `004bfee4` | `e8 16 40 f9` | ldr x8,[x23, #0x28] | `FALL_THROUGH`
<a id="insn-004bfee8"></a> `004bfee8` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bfeec"></a> `004bfeec` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bfef0"></a> `004bfef0` | `e1 04 00 54` | b.ne 0x004bff8c | `CONDITIONAL_JUMP`
<a id="insn-004bfef4"></a> `004bfef4` | `60 ef ff d0` | adrp x0,0x2ad000 | `FALL_THROUGH`
<a id="insn-004bfef8"></a> `004bfef8` | `00 58 1f 91` | add x0,x0,#0x7d6 | `FALL_THROUGH`
<a id="insn-004bfefc"></a> `004bfefc` | `c1 ef ff 90` | adrp x1,0x2b7000 | `FALL_THROUGH`
<a id="insn-004bff00"></a> `004bff00` | `21 5c 14 91` | add x1,x1,#0x517 | `FALL_THROUGH`
<a id="insn-004bff04"></a> `004bff04` | `a2 ef ff 90` | adrp x2,0x2b3000 | `FALL_THROUGH`
<a id="insn-004bff08"></a> `004bff08` | `42 b4 34 91` | add x2,x2,#0xd2d | `FALL_THROUGH`
<a id="insn-004bff0c"></a> `004bff0c` | `03 ef ff f0` | adrp x3,0x2a2000 | `FALL_THROUGH`
<a id="insn-004bff10"></a> `004bff10` | `63 00 03 91` | add x3,x3,#0xc0 | `FALL_THROUGH`
<a id="insn-004bff14"></a> `004bff14` | `e4 bc 82 52` | mov w4,#0x15e7 | `FALL_THROUGH`
<a id="insn-004bff18"></a> `004bff18` | `f6 65 1e 94` | bl 0x00c596f0 | `CALL_TERMINATOR`
<a id="insn-004bff8c"></a> `004bff8c` | `fd 63 1e 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004bfcdc`](#insn-004bfcdc) 範囲 `[['004bfcdc', '004bfd0f']]`
  - `CONDITIONAL_JUMP` [`004bfd0c`](#insn-004bfd0c) → [`004bfeac`](#insn-004bfeac)
  - `FALL_THROUGH` [`004bfd0c`](#insn-004bfd0c) → [`004bfd10`](#insn-004bfd10)
- ブロック [`004bfd10`](#insn-004bfd10) 範囲 `[['004bfd10', '004bfd33']]`
  - `CONDITIONAL_JUMP` [`004bfd30`](#insn-004bfd30) → [`004bfe30`](#insn-004bfe30)
  - `FALL_THROUGH` [`004bfd30`](#insn-004bfd30) → [`004bfd34`](#insn-004bfd34)
- ブロック [`004bfd34`](#insn-004bfd34) 範囲 `[['004bfd34', '004bfd43']]`
  - `CONDITIONAL_JUMP` [`004bfd40`](#insn-004bfd40) → [`004bfe30`](#insn-004bfe30)
  - `FALL_THROUGH` [`004bfd40`](#insn-004bfd40) → [`004bfd44`](#insn-004bfd44)
- ブロック [`004bfd44`](#insn-004bfd44) 範囲 `[['004bfd44', '004bfd53']]`
  - `CONDITIONAL_JUMP` [`004bfd50`](#insn-004bfd50) → [`004bfee4`](#insn-004bfee4)
  - `FALL_THROUGH` [`004bfd50`](#insn-004bfd50) → [`004bfd54`](#insn-004bfd54)
- ブロック [`004bfd54`](#insn-004bfd54) 範囲 `[['004bfd54', '004bfd7b']]`
  - `CONDITIONAL_JUMP` [`004bfd78`](#insn-004bfd78) → [`004bfd8c`](#insn-004bfd8c)
  - `FALL_THROUGH` [`004bfd78`](#insn-004bfd78) → [`004bfd7c`](#insn-004bfd7c)
- ブロック [`004bfd7c`](#insn-004bfd7c) 範囲 `[['004bfd7c', '004bfd8b']]`
  - `UNCONDITIONAL_JUMP` [`004bfd88`](#insn-004bfd88) → [`004bfd98`](#insn-004bfd98)
- ブロック [`004bfd8c`](#insn-004bfd8c) 範囲 `[['004bfd8c', '004bfd8f']]`
  - `CONDITIONAL_JUMP` [`004bfd8c`](#insn-004bfd8c) → [`004bfd98`](#insn-004bfd98)
  - `FALL_THROUGH` [`004bfd8c`](#insn-004bfd8c) → [`004bfd90`](#insn-004bfd90)
- ブロック [`004bfd90`](#insn-004bfd90) 範囲 `[['004bfd90', '004bfd97']]`
  - `FALL_THROUGH` [`004bfd94`](#insn-004bfd94) → [`004bfd98`](#insn-004bfd98)
- ブロック [`004bfd98`](#insn-004bfd98) 範囲 `[['004bfd98', '004bfdcf']]`
  - `CONDITIONAL_JUMP` [`004bfdcc`](#insn-004bfdcc) → [`004bfdfc`](#insn-004bfdfc)
  - `FALL_THROUGH` [`004bfdcc`](#insn-004bfdcc) → [`004bfdd0`](#insn-004bfdd0)
- ブロック [`004bfdd0`](#insn-004bfdd0) 範囲 `[['004bfdd0', '004bfddf']]`
  - `CONDITIONAL_JUMP` [`004bfddc`](#insn-004bfddc) → [`004bff8c`](#insn-004bff8c)
  - `FALL_THROUGH` [`004bfddc`](#insn-004bfddc) → [`004bfde0`](#insn-004bfde0)
- ブロック [`004bfde0`](#insn-004bfde0) 範囲 `[['004bfde0', '004bfdfb']]`
- ブロック [`004bfdfc`](#insn-004bfdfc) 範囲 `[['004bfdfc', '004bfdff']]`
  - `CONDITIONAL_JUMP` [`004bfdfc`](#insn-004bfdfc) → [`004bfe08`](#insn-004bfe08)
  - `FALL_THROUGH` [`004bfdfc`](#insn-004bfdfc) → [`004bfe00`](#insn-004bfe00)
- ブロック [`004bfe00`](#insn-004bfe00) 範囲 `[['004bfe00', '004bfe07']]`
  - `FALL_THROUGH` [`004bfe04`](#insn-004bfe04) → [`004bfe08`](#insn-004bfe08)
- ブロック [`004bfe08`](#insn-004bfe08) 範囲 `[['004bfe08', '004bfe17']]`
  - `CONDITIONAL_JUMP` [`004bfe14`](#insn-004bfe14) → [`004bff8c`](#insn-004bff8c)
  - `FALL_THROUGH` [`004bfe14`](#insn-004bfe14) → [`004bfe18`](#insn-004bfe18)
- ブロック [`004bfe18`](#insn-004bfe18) 範囲 `[['004bfe18', '004bfe2f']]`
- ブロック [`004bfe30`](#insn-004bfe30) 範囲 `[['004bfe30', '004bfe8f']]`
  - `CONDITIONAL_JUMP` [`004bfe8c`](#insn-004bfe8c) → [`004bff8c`](#insn-004bff8c)
  - `FALL_THROUGH` [`004bfe8c`](#insn-004bfe8c) → [`004bfe90`](#insn-004bfe90)
- ブロック [`004bfe90`](#insn-004bfe90) 範囲 `[['004bfe90', '004bfeab']]`
- ブロック [`004bfeac`](#insn-004bfeac) 範囲 `[['004bfeac', '004bfebb']]`
  - `CONDITIONAL_JUMP` [`004bfeb8`](#insn-004bfeb8) → [`004bff8c`](#insn-004bff8c)
  - `FALL_THROUGH` [`004bfeb8`](#insn-004bfeb8) → [`004bfebc`](#insn-004bfebc)
- ブロック [`004bfebc`](#insn-004bfebc) 範囲 `[['004bfebc', '004bfee3']]`
- ブロック [`004bfee4`](#insn-004bfee4) 範囲 `[['004bfee4', '004bfef3']]`
  - `CONDITIONAL_JUMP` [`004bfef0`](#insn-004bfef0) → [`004bff8c`](#insn-004bff8c)
  - `FALL_THROUGH` [`004bfef0`](#insn-004bfef0) → [`004bfef4`](#insn-004bfef4)
- ブロック [`004bfef4`](#insn-004bfef4) 範囲 `[['004bfef4', '004bff1b']]`
- ブロック [`004bff8c`](#insn-004bff8c) 範囲 `[['004bff8c', '004bff8f']]`

## 命令位置別の参照

- [`004bfce0`](#insn-004bfce0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfce4`](#insn-004bfce4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfce8`](#insn-004bfce8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfcec`](#insn-004bfcec) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfcfc`](#insn-004bfcfc) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfd0c`](#insn-004bfd0c) → [`004bfeac`](#insn-004bfeac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfd30`](#insn-004bfd30) → [`004bfe30`](#insn-004bfe30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfd40`](#insn-004bfd40) → [`004bfe30`](#insn-004bfe30) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfd50`](#insn-004bfd50) → [`004bfee4`](#insn-004bfee4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfd78`](#insn-004bfd78) → [`004bfd8c`](#insn-004bfd8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfd80`](#insn-004bfd80) → [`0054084c`](../00540/0054084c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0054084c` · 推定シンボル `None` · 推定型 `None`
- [`004bfd88`](#insn-004bfd88) → [`004bfd98`](#insn-004bfd98) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfd8c`](#insn-004bfd8c) → [`004bfd98`](#insn-004bfd98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfdcc`](#insn-004bfdcc) → [`004bfdfc`](#insn-004bfdfc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfdd4`](#insn-004bfdd4) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfddc`](#insn-004bfddc) → [`004bff8c`](#insn-004bff8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfde4`](#insn-004bfde4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfde8`](#insn-004bfde8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfdec`](#insn-004bfdec) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfdf0`](#insn-004bfdf0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfdf8`](#insn-004bfdf8) → [`0054084c`](../00540/0054084c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0054084c` · 推定シンボル `None` · 推定型 `None`
- [`004bfdfc`](#insn-004bfdfc) → [`004bfe08`](#insn-004bfe08) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfe0c`](#insn-004bfe0c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfe14`](#insn-004bfe14) → [`004bff8c`](#insn-004bff8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfe18`](#insn-004bfe18) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfe1c`](#insn-004bfe1c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfe20`](#insn-004bfe20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfe24`](#insn-004bfe24) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfe34`](#insn-004bfe34) → [`00c58f90`](../00c58/00c58f90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f90` · 推定シンボル `None` · 推定型 `None`
- [`004bfe44`](#insn-004bfe44) → [`00c59e60`](../00c59/00c59e60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59e60` · 推定シンボル `None` · 推定型 `None`
- [`004bfe4c`](#insn-004bfe4c) → `002c10dd`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bfe54`](#insn-004bfe54) → [`00c59010`](../00c59/00c59010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59010` · 推定シンボル `None` · 推定型 `None`
- [`004bfe64`](#insn-004bfe64) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfe68`](#insn-004bfe68) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfe7c`](#insn-004bfe7c) → [`00c597f0`](../00c59/00c597f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c597f0` · 推定シンボル `None` · 推定型 `None`
- [`004bfe84`](#insn-004bfe84) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfe8c`](#insn-004bfe8c) → [`004bff8c`](#insn-004bff8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfe98`](#insn-004bfe98) → [`00535bc8`](../00535/00535bc8.md) · `PARAM` · `ANALYSIS` · 関数 `00535bc8` · 推定シンボル `None` · 推定型 `None`
- [`004bfe9c`](#insn-004bfe9c) → `00c9bdf0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004bfe9c`](#insn-004bfe9c) → `00c67360`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN5Botan14Decoding_ErrorE` · 推定型 `pointer __((offset(0x10)))`
- [`004bfea8`](#insn-004bfea8) → [`00c58fb0`](../00c58/00c58fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58fb0` · 推定シンボル `None` · 推定型 `None`
- [`004bfeb0`](#insn-004bfeb0) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfeb8`](#insn-004bfeb8) → [`004bff8c`](#insn-004bff8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfec0`](#insn-004bfec0) → `002ad7d6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bfec8`](#insn-004bfec8) → `002b4e2c`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bfed0`](#insn-004bfed0) → `002ba2d7`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bfed8`](#insn-004bfed8) → `002a542a`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bfee0`](#insn-004bfee0) → [`00c596f0`](../00c59/00c596f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c596f0` · 推定シンボル `None` · 推定型 `None`
- [`004bfee8`](#insn-004bfee8) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfef0`](#insn-004bfef0) → [`004bff8c`](#insn-004bff8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bfef8`](#insn-004bfef8) → `002ad7d6`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bff00`](#insn-004bff00) → `002b7517`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bff08`](#insn-004bff08) → `002b3d2d`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bff10`](#insn-004bff10) → `002a20c0`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004bff18`](#insn-004bff18) → [`00c596f0`](../00c59/00c596f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c596f0` · 推定シンボル `None` · 推定型 `None`
- [`004bff8c`](#insn-004bff8c) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004bfce0`](#insn-004bfce0)

~~~json
{
  "source": "004bfce0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfce4`](#insn-004bfce4)

~~~json
{
  "source": "004bfce4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfce8`](#insn-004bfce8)

~~~json
{
  "source": "004bfce8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfcec`](#insn-004bfcec)

~~~json
{
  "source": "004bfcec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfcfc`](#insn-004bfcfc)

~~~json
{
  "source": "004bfcfc",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfd0c`](#insn-004bfd0c)

~~~json
{
  "source": "004bfd0c",
  "target": "004bfeac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfd30`](#insn-004bfd30)

~~~json
{
  "source": "004bfd30",
  "target": "004bfe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfd40`](#insn-004bfd40)

~~~json
{
  "source": "004bfd40",
  "target": "004bfe30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfd50`](#insn-004bfd50)

~~~json
{
  "source": "004bfd50",
  "target": "004bfee4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfd78`](#insn-004bfd78)

~~~json
{
  "source": "004bfd78",
  "target": "004bfd8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfd80`](#insn-004bfd80)

~~~json
{
  "source": "004bfd80",
  "target": "0054084c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bfd88`](#insn-004bfd88)

~~~json
{
  "source": "004bfd88",
  "target": "004bfd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfd8c`](#insn-004bfd8c)

~~~json
{
  "source": "004bfd8c",
  "target": "004bfd98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfdcc`](#insn-004bfdcc)

~~~json
{
  "source": "004bfdcc",
  "target": "004bfdfc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfdd4`](#insn-004bfdd4)

~~~json
{
  "source": "004bfdd4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfddc`](#insn-004bfddc)

~~~json
{
  "source": "004bfddc",
  "target": "004bff8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfde4`](#insn-004bfde4)

~~~json
{
  "source": "004bfde4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfde8`](#insn-004bfde8)

~~~json
{
  "source": "004bfde8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfdec`](#insn-004bfdec)

~~~json
{
  "source": "004bfdec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfdf0`](#insn-004bfdf0)

~~~json
{
  "source": "004bfdf0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfdf8`](#insn-004bfdf8)

~~~json
{
  "source": "004bfdf8",
  "target": "0054084c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bfdfc`](#insn-004bfdfc)

~~~json
{
  "source": "004bfdfc",
  "target": "004bfe08",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfe0c`](#insn-004bfe0c)

~~~json
{
  "source": "004bfe0c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfe14`](#insn-004bfe14)

~~~json
{
  "source": "004bfe14",
  "target": "004bff8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfe18`](#insn-004bfe18)

~~~json
{
  "source": "004bfe18",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfe1c`](#insn-004bfe1c)

~~~json
{
  "source": "004bfe1c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfe20`](#insn-004bfe20)

~~~json
{
  "source": "004bfe20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfe24`](#insn-004bfe24)

~~~json
{
  "source": "004bfe24",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfe34`](#insn-004bfe34)

~~~json
{
  "source": "004bfe34",
  "target": "00c58f90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bfe44`](#insn-004bfe44)

~~~json
{
  "source": "004bfe44",
  "target": "00c59e60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bfe4c`](#insn-004bfe4c)

~~~json
{
  "source": "004bfe4c",
  "target": "002c10dd",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002c10dd",
  "offset": 0,
  "size": 42,
  "datatype": "string",
  "bytes": "3a2043697068657274657874206e6f742061206d756c7469706c65206f662062",
  "capture_start": "002c10dd",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`004bfe54`](#insn-004bfe54)

~~~json
{
  "source": "004bfe54",
  "target": "00c59010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bfe64`](#insn-004bfe64)

~~~json
{
  "source": "004bfe64",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfe68`](#insn-004bfe68)

~~~json
{
  "source": "004bfe68",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfe7c`](#insn-004bfe7c)

~~~json
{
  "source": "004bfe7c",
  "target": "00c597f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bfe84`](#insn-004bfe84)

~~~json
{
  "source": "004bfe84",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfe8c`](#insn-004bfe8c)

~~~json
{
  "source": "004bfe8c",
  "target": "004bff8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfe98`](#insn-004bfe98)

~~~json
{
  "source": "004bfe98",
  "target": "00535bc8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bfe9c`](#insn-004bfe9c)

~~~json
{
  "source": "004bfe9c",
  "target": "00c9bdf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bdf0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004bfe9c`](#insn-004bfe9c)

~~~json
{
  "source": "004bfe9c",
  "target": "00c67360",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c67360",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004bfea8`](#insn-004bfea8)

~~~json
{
  "source": "004bfea8",
  "target": "00c58fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bfeb0`](#insn-004bfeb0)

~~~json
{
  "source": "004bfeb0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfeb8`](#insn-004bfeb8)

~~~json
{
  "source": "004bfeb8",
  "target": "004bff8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfec0`](#insn-004bfec0)

~~~json
{
  "source": "004bfec0",
  "target": "002ad7d6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad7d6",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "6275666665722e73697a652829203e3d206f666673657400",
  "capture_start": "002ad7d6",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bfec8`](#insn-004bfec8)

~~~json
{
  "source": "004bfec8",
  "target": "002b4e2c",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b4e2c",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "4f66667365742069732073616e6500",
  "capture_start": "002b4e2c",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bfed0`](#insn-004bfed0)

~~~json
{
  "source": "004bfed0",
  "target": "002ba2d7",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ba2d7",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "66696e69736800",
  "capture_start": "002ba2d7",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bfed8`](#insn-004bfed8)

~~~json
{
  "source": "004bfed8",
  "target": "002a542a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a542a",
  "offset": 0,
  "size": 141,
  "datatype": "string",
  "bytes": "2f55736572732f626174746c65636174732f2e6a656e6b696e732f776f726b73",
  "capture_start": "002a542a",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`004bfee0`](#insn-004bfee0)

~~~json
{
  "source": "004bfee0",
  "target": "00c596f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bfee8`](#insn-004bfee8)

~~~json
{
  "source": "004bfee8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfef0`](#insn-004bfef0)

~~~json
{
  "source": "004bfef0",
  "target": "004bff8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bfef8`](#insn-004bfef8)

~~~json
{
  "source": "004bfef8",
  "target": "002ad7d6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ad7d6",
  "offset": 0,
  "size": 24,
  "datatype": "string",
  "bytes": "6275666665722e73697a652829203e3d206f666673657400",
  "capture_start": "002ad7d6",
  "capture_bytes": 24,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bff00`](#insn-004bff00)

~~~json
{
  "source": "004bff00",
  "target": "002b7517",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b7517",
  "offset": 0,
  "size": 10,
  "datatype": "string",
  "bytes": "4f6666736574206f6b00",
  "capture_start": "002b7517",
  "capture_bytes": 10,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bff08`](#insn-004bff08)

~~~json
{
  "source": "004bff08",
  "target": "002b3d2d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b3d2d",
  "offset": 0,
  "size": 7,
  "datatype": "string",
  "bytes": "75706461746500",
  "capture_start": "002b3d2d",
  "capture_bytes": 7,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004bff10`](#insn-004bff10)

~~~json
{
  "source": "004bff10",
  "target": "002a20c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a20c0",
  "offset": 0,
  "size": 139,
  "datatype": "string",
  "bytes": "2f55736572732f626174746c65636174732f2e6a656e6b696e732f776f726b73",
  "capture_start": "002a20c0",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`004bff18`](#insn-004bff18)

~~~json
{
  "source": "004bff18",
  "target": "00c596f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bff8c`](#insn-004bff8c)

~~~json
{
  "source": "004bff8c",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
