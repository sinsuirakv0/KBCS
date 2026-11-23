# 00af2edc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00af2e14`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00af2/00af2e14.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-841ec28342abe16a771ae4fa2e360b87)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00af2f20`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00af2/00af2f20.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0065.md#compare-b5cde98e68a55826c367fc3c6e02e41d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00af2edc",
  "name": "_ZN8firebase4util24JavaSetToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEEEP8_jobject",
  "size": 640,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "bbc98c11bc201ed65471e9f31285f1029082313d90861513a5121c34f2463fd1",
  "source_text_sha256": "bbc98c11bc201ed65471e9f31285f1029082313d90861513a5121c34f2463fd1",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00af2edc",
        "00af315b"
      ]
    ],
    "bytes_sha256": "af331aaac2f3407e44bd255157b9acf3b9b194cfdd579adcc11de2f86d10f625",
    "instruction_count": 160,
    "instruction_bytes": 640,
    "body_bytes": 640,
    "indirect": 11,
    "unresolved": 11
  }
}
~~~

## 呼び出し元

- [00bde600](../00bde/00bde600.md)

## 呼び出し先

- [0047495c](../00474/0047495c.md)
- [00474b70](../00474/00474b70.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb160](../00bdb/00bdb160.md)
- [00bde050](../00bde/00bde050.md)
- [00bde270](../00bde/00bde270.md)
- [00bde770](../00bde/00bde770.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3046 bytes

~~~c

void _ZN8firebase4util24JavaSetToStdStringVectorEP7_JNIEnvPNSt6__ndk16vectorINS3_12basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEENS8_ISA_EEEEP8_jobject
               (long *param_1,long param_2,undefined8 param_3)

{
  ulong *puVar1;
  long lVar2;
  ulong __n;
  void *__src;
  char cVar3;
  undefined8 uVar4;
  undefined8 uVar5;
  long lVar6;
  ulong uVar7;
  void *__dest;
  byte local_80;
  undefined7 uStack_7f;
  ulong uStack_78;
  void *local_70;
  long local_68;
  
  lVar2 = tpidr_el0;
  local_68 = *(long *)(lVar2 + 0x28);
  uVar4 = FUN_0047495c(param_1,param_3,DAT_010a0998);
  cVar3 = (**(code **)(*param_1 + 0x720))(param_1);
  if (cVar3 != '\0') {
    (**(code **)(*param_1 + 0x80))(param_1);
    (**(code **)(*param_1 + 0x88))(param_1);
  }
  cVar3 = FUN_00474b70(param_1,uVar4,DAT_010a08c8);
  lVar6 = *param_1;
  do {
    if (cVar3 == '\0') {
      (**(code **)(lVar6 + 0xb8))(param_1,uVar4);
      if (*(long *)(lVar2 + 0x28) == local_68) {
        return;
      }
                    /* WARNING: Subroutine does not return */
      __stack_chk_fail();
    }
    cVar3 = (**(code **)(lVar6 + 0x720))(param_1);
    if (cVar3 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    uVar5 = FUN_0047495c(param_1,uVar4,DAT_010a08d0);
    cVar3 = (**(code **)(*param_1 + 0x720))(param_1);
    if (cVar3 != '\0') {
      (**(code **)(*param_1 + 0x80))(param_1);
      (**(code **)(*param_1 + 0x88))(param_1);
    }
    _ZN8firebase4util15JStringToStringEP7_JNIEnvP8_jobject(&local_80,param_1,uVar5);
    (**(code **)(*param_1 + 0xb8))(param_1,uVar5);
    __src = local_70;
    __n = uStack_78;
    puVar1 = *(ulong **)(param_2 + 8);
    if (puVar1 == *(ulong **)(param_2 + 0x10)) {
      _ZNSt6__ndk16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE21__push_back_slow_pathIRKS6_EEvOT_
                (param_2,&local_80);
    }
    else {
      *puVar1 = 0;
      puVar1[1] = 0;
      puVar1[2] = 0;
      if ((local_80 & 1) == 0) {
        puVar1[2] = (ulong)local_70;
        puVar1[1] = uStack_78;
        *puVar1 = CONCAT71(uStack_7f,local_80);
      }
      else {
        if (0xffffffffffffffef < uStack_78) {
                    /* WARNING: Subroutine does not return */
          abort();
        }
        if (uStack_78 < 0x17) {
          __dest = (void *)((long)puVar1 + 1);
          *(char *)puVar1 = (char)((int)uStack_78 << 1);
          if (uStack_78 != 0) goto LAB_00af30e0;
        }
        else {
          uVar7 = uStack_78 + 0x10 & 0xfffffffffffffff0;
          __dest = (void *)_Znwm(uVar7);
          puVar1[1] = __n;
          puVar1[2] = (ulong)__dest;
          *puVar1 = uVar7 | 1;
LAB_00af30e0:
          memcpy(__dest,__src,__n);
        }
        *(undefined1 *)((long)__dest + __n) = 0;
      }
      *(ulong **)(param_2 + 8) = puVar1 + 3;
    }
    if ((local_80 & 1) != 0) {
      _ZdlPv(local_70);
    }
    cVar3 = FUN_00474b70(param_1,uVar4,DAT_010a08c8);
    lVar6 = *param_1;
  } while( true );
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00af2edc"></a> `00af2edc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00af2ee0"></a> `00af2ee0` | `fc 6f 03 a9` | stp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af2ee4"></a> `00af2ee4` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00af2ee8"></a> `00af2ee8` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00af2eec"></a> `00af2eec` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00af2ef0"></a> `00af2ef0` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00af2ef4"></a> `00af2ef4` | `fd 7b 08 a9` | stp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00af2ef8"></a> `00af2ef8` | `fd 03 02 91` | add x29,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00af2efc"></a> `00af2efc` | `49 d0 3b d5` | mrs x9,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00af2f00"></a> `00af2f00` | `e9 07 00 f9` | str x9,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00af2f04"></a> `00af2f04` | `29 15 40 f9` | ldr x9,[x9, #0x28] | `FALL_THROUGH`
<a id="insn-00af2f08"></a> `00af2f08` | `e8 03 02 aa` | mov x8,x2 | `FALL_THROUGH`
<a id="insn-00af2f0c"></a> `00af2f0c` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00af2f10"></a> `00af2f10` | `e1 03 08 aa` | mov x1,x8 | `FALL_THROUGH`
<a id="insn-00af2f14"></a> `00af2f14` | `e9 17 00 f9` | str x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00af2f18"></a> `00af2f18` | `69 2d 00 d0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af2f1c"></a> `00af2f1c` | `22 cd 44 f9` | ldr x2,[x9, #0x998] | `FALL_THROUGH`
<a id="insn-00af2f20"></a> `00af2f20` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00af2f24"></a> `00af2f24` | `8e 06 e6 97` | bl 0x0047495c | `UNCONDITIONAL_CALL`
<a id="insn-00af2f28"></a> `00af2f28` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af2f2c"></a> `00af2f2c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00af2f30"></a> `00af2f30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af2f34"></a> `00af2f34` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00af2f38"></a> `00af2f38` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af2f3c"></a> `00af2f3c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00af2f40"></a> `00af2f40` | `20 01 00 54` | b.eq 0x00af2f64 | `CONDITIONAL_JUMP`
<a id="insn-00af2f44"></a> `00af2f44` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af2f48"></a> `00af2f48` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af2f4c"></a> `00af2f4c` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00af2f50"></a> `00af2f50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af2f54"></a> `00af2f54` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af2f58"></a> `00af2f58` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af2f5c"></a> `00af2f5c` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00af2f60"></a> `00af2f60` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af2f64"></a> `00af2f64` | `7b 2d 00 d0` | adrp x27,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af2f68"></a> `00af2f68` | `62 67 44 f9` | ldr x2,[x27, #0x8c8] | `FALL_THROUGH`
<a id="insn-00af2f6c"></a> `00af2f6c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af2f70"></a> `00af2f70` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00af2f74"></a> `00af2f74` | `ff 06 e6 97` | bl 0x00474b70 | `UNCONDITIONAL_CALL`
<a id="insn-00af2f78"></a> `00af2f78` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af2f7c"></a> `00af2f7c` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00af2f80"></a> `00af2f80` | `80 0c 00 54` | b.eq 0x00af3110 | `CONDITIONAL_JUMP`
<a id="insn-00af2f84"></a> `00af2f84` | `7c 2d 00 d0` | adrp x28,0x10a0000 | `FALL_THROUGH`
<a id="insn-00af2f88"></a> `00af2f88` | `08 00 00 14` | b 0x00af2fa8 | `UNCONDITIONAL_JUMP`
<a id="insn-00af2f8c"></a> `00af2f8c` | `62 67 44 f9` | ldr x2,[x27, #0x8c8] | `FALL_THROUGH`
<a id="insn-00af2f90"></a> `00af2f90` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af2f94"></a> `00af2f94` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00af2f98"></a> `00af2f98` | `f6 06 e6 97` | bl 0x00474b70 | `UNCONDITIONAL_CALL`
<a id="insn-00af2f9c"></a> `00af2f9c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af2fa0"></a> `00af2fa0` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00af2fa4"></a> `00af2fa4` | `60 0b 00 54` | b.eq 0x00af3110 | `CONDITIONAL_JUMP`
<a id="insn-00af2fa8"></a> `00af2fa8` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00af2fac"></a> `00af2fac` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af2fb0"></a> `00af2fb0` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af2fb4"></a> `00af2fb4` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00af2fb8"></a> `00af2fb8` | `20 01 00 54` | b.eq 0x00af2fdc | `CONDITIONAL_JUMP`
<a id="insn-00af2fbc"></a> `00af2fbc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af2fc0"></a> `00af2fc0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af2fc4"></a> `00af2fc4` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00af2fc8"></a> `00af2fc8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af2fcc"></a> `00af2fcc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af2fd0"></a> `00af2fd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af2fd4"></a> `00af2fd4` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00af2fd8"></a> `00af2fd8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af2fdc"></a> `00af2fdc` | `82 6b 44 f9` | ldr x2,[x28, #0x8d0] | `FALL_THROUGH`
<a id="insn-00af2fe0"></a> `00af2fe0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af2fe4"></a> `00af2fe4` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00af2fe8"></a> `00af2fe8` | `5d 06 e6 97` | bl 0x0047495c | `UNCONDITIONAL_CALL`
<a id="insn-00af2fec"></a> `00af2fec` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af2ff0"></a> `00af2ff0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00af2ff4"></a> `00af2ff4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af2ff8"></a> `00af2ff8` | `08 91 43 f9` | ldr x8,[x8, #0x720] | `FALL_THROUGH`
<a id="insn-00af2ffc"></a> `00af2ffc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3000"></a> `00af3000` | `1f 1c 00 72` | tst w0,#0xff | `FALL_THROUGH`
<a id="insn-00af3004"></a> `00af3004` | `20 01 00 54` | b.eq 0x00af3028 | `CONDITIONAL_JUMP`
<a id="insn-00af3008"></a> `00af3008` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af300c"></a> `00af300c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3010"></a> `00af3010` | `08 41 40 f9` | ldr x8,[x8, #0x80] | `FALL_THROUGH`
<a id="insn-00af3014"></a> `00af3014` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3018"></a> `00af3018` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af301c"></a> `00af301c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3020"></a> `00af3020` | `08 45 40 f9` | ldr x8,[x8, #0x88] | `FALL_THROUGH`
<a id="insn-00af3024"></a> `00af3024` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3028"></a> `00af3028` | `e8 43 00 91` | add x8,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00af302c"></a> `00af302c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3030"></a> `00af3030` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00af3034"></a> `00af3034` | `07 ac 03 94` | bl 0x00bde050 | `UNCONDITIONAL_CALL`
<a id="insn-00af3038"></a> `00af3038` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00af303c"></a> `00af303c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3040"></a> `00af3040` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00af3044"></a> `00af3044` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00af3048"></a> `00af3048` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af304c"></a> `00af304c` | `98 a2 40 a9` | ldp x24,x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00af3050"></a> `00af3050` | `1f 03 08 eb` | cmp x24,x8 | `FALL_THROUGH`
<a id="insn-00af3054"></a> `00af3054` | `40 01 00 54` | b.eq 0x00af307c | `CONDITIONAL_JUMP`
<a id="insn-00af3058"></a> `00af3058` | `1f 7f 00 a9` | stp xzr,xzr,[x24] | `FALL_THROUGH`
<a id="insn-00af305c"></a> `00af305c` | `1f 0b 00 f9` | str xzr,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00af3060"></a> `00af3060` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3064"></a> `00af3064` | `88 01 00 37` | tbnz w8,#0x0,0x00af3094 | `CONDITIONAL_JUMP`
<a id="insn-00af3068"></a> `00af3068` | `e8 13 40 f9` | ldr x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af306c"></a> `00af306c` | `e0 07 c0 3d` | ldr q0,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3070"></a> `00af3070` | `08 0b 00 f9` | str x8,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00af3074"></a> `00af3074` | `00 03 80 3d` | str q0,[x24] | `FALL_THROUGH`
<a id="insn-00af3078"></a> `00af3078` | `1f 00 00 14` | b 0x00af30f4 | `UNCONDITIONAL_JUMP`
<a id="insn-00af307c"></a> `00af307c` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-00af3080"></a> `00af3080` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00af3084"></a> `00af3084` | `bb ad 03 94` | bl 0x00bde770 | `UNCONDITIONAL_CALL`
<a id="insn-00af3088"></a> `00af3088` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af308c"></a> `00af308c` | `08 f8 07 36` | tbz w8,#0x0,0x00af2f8c | `CONDITIONAL_JUMP`
<a id="insn-00af3090"></a> `00af3090` | `1d 00 00 14` | b 0x00af3104 | `UNCONDITIONAL_JUMP`
<a id="insn-00af3094"></a> `00af3094` | `f6 0f 40 f9` | ldr x22,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00af3098"></a> `00af3098` | `df 42 00 b1` | cmn x22,#0x10 | `FALL_THROUGH`
<a id="insn-00af309c"></a> `00af309c` | `c2 05 00 54` | b.cs 0x00af3154 | `CONDITIONAL_JUMP`
<a id="insn-00af30a0"></a> `00af30a0` | `f7 13 40 f9` | ldr x23,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af30a4"></a> `00af30a4` | `df 5e 00 f1` | cmp x22,#0x17 | `FALL_THROUGH`
<a id="insn-00af30a8"></a> `00af30a8` | `c2 00 00 54` | b.cs 0x00af30c0 | `CONDITIONAL_JUMP`
<a id="insn-00af30ac"></a> `00af30ac` | `c8 7a 1f 53` | lsl w8,w22,#0x1 | `FALL_THROUGH`
<a id="insn-00af30b0"></a> `00af30b0` | `fa 03 18 aa` | mov x26,x24 | `FALL_THROUGH`
<a id="insn-00af30b4"></a> `00af30b4` | `48 17 00 38` | strb w8,[x26], #0x1 | `FALL_THROUGH`
<a id="insn-00af30b8"></a> `00af30b8` | `56 01 00 b5` | cbnz x22,0x00af30e0 | `CONDITIONAL_JUMP`
<a id="insn-00af30bc"></a> `00af30bc` | `0d 00 00 14` | b 0x00af30f0 | `UNCONDITIONAL_JUMP`
<a id="insn-00af30c0"></a> `00af30c0` | `c8 42 00 91` | add x8,x22,#0x10 | `FALL_THROUGH`
<a id="insn-00af30c4"></a> `00af30c4` | `19 ed 7c 92` | and x25,x8,#-0x10 | `FALL_THROUGH`
<a id="insn-00af30c8"></a> `00af30c8` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00af30cc"></a> `00af30cc` | `c9 9f 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00af30d0"></a> `00af30d0` | `28 03 40 b2` | orr x8,x25,#0x1 | `FALL_THROUGH`
<a id="insn-00af30d4"></a> `00af30d4` | `fa 03 00 aa` | mov x26,x0 | `FALL_THROUGH`
<a id="insn-00af30d8"></a> `00af30d8` | `16 83 00 a9` | stp x22,x0,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00af30dc"></a> `00af30dc` | `08 03 00 f9` | str x8,[x24] | `FALL_THROUGH`
<a id="insn-00af30e0"></a> `00af30e0` | `e0 03 1a aa` | mov x0,x26 | `FALL_THROUGH`
<a id="insn-00af30e4"></a> `00af30e4` | `e1 03 17 aa` | mov x1,x23 | `FALL_THROUGH`
<a id="insn-00af30e8"></a> `00af30e8` | `e2 03 16 aa` | mov x2,x22 | `FALL_THROUGH`
<a id="insn-00af30ec"></a> `00af30ec` | `1d a0 03 94` | bl 0x00bdb160 | `UNCONDITIONAL_CALL`
<a id="insn-00af30f0"></a> `00af30f0` | `5f 6b 36 38` | strb wzr,[x26, x22, LSL ] | `FALL_THROUGH`
<a id="insn-00af30f4"></a> `00af30f4` | `08 63 00 91` | add x8,x24,#0x18 | `FALL_THROUGH`
<a id="insn-00af30f8"></a> `00af30f8` | `88 06 00 f9` | str x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00af30fc"></a> `00af30fc` | `e8 43 40 39` | ldrb w8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00af3100"></a> `00af3100` | `68 f4 07 36` | tbz w8,#0x0,0x00af2f8c | `CONDITIONAL_JUMP`
<a id="insn-00af3104"></a> `00af3104` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00af3108"></a> `00af3108` | `c2 9f 03 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00af310c"></a> `00af310c` | `a0 ff ff 17` | b 0x00af2f8c | `UNCONDITIONAL_JUMP`
<a id="insn-00af3110"></a> `00af3110` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00af3114"></a> `00af3114` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00af3118"></a> `00af3118` | `e1 03 15 aa` | mov x1,x21 | `FALL_THROUGH`
<a id="insn-00af311c"></a> `00af311c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00af3120"></a> `00af3120` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00af3124"></a> `00af3124` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00af3128"></a> `00af3128` | `e9 17 40 f9` | ldr x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00af312c"></a> `00af312c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00af3130"></a> `00af3130` | `41 01 00 54` | b.ne 0x00af3158 | `CONDITIONAL_JUMP`
<a id="insn-00af3134"></a> `00af3134` | `fd 7b 48 a9` | ldp x29,x30,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00af3138"></a> `00af3138` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00af313c"></a> `00af313c` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00af3140"></a> `00af3140` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00af3144"></a> `00af3144` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00af3148"></a> `00af3148` | `fc 6f 43 a9` | ldp x28,x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00af314c"></a> `00af314c` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00af3150"></a> `00af3150` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00af3154"></a> `00af3154` | `47 ac 03 94` | bl 0x00bde270 | `CALL_TERMINATOR`
<a id="insn-00af3158"></a> `00af3158` | `ba 9f 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00af2edc`](#insn-00af2edc) 範囲 `[['00af2edc', '00af2f43']]`
  - `CONDITIONAL_JUMP` [`00af2f40`](#insn-00af2f40) → [`00af2f64`](#insn-00af2f64)
  - `FALL_THROUGH` [`00af2f40`](#insn-00af2f40) → [`00af2f44`](#insn-00af2f44)
- ブロック [`00af2f44`](#insn-00af2f44) 範囲 `[['00af2f44', '00af2f63']]`
  - `FALL_THROUGH` [`00af2f60`](#insn-00af2f60) → [`00af2f64`](#insn-00af2f64)
- ブロック [`00af2f64`](#insn-00af2f64) 範囲 `[['00af2f64', '00af2f83']]`
  - `CONDITIONAL_JUMP` [`00af2f80`](#insn-00af2f80) → [`00af3110`](#insn-00af3110)
  - `FALL_THROUGH` [`00af2f80`](#insn-00af2f80) → [`00af2f84`](#insn-00af2f84)
- ブロック [`00af2f84`](#insn-00af2f84) 範囲 `[['00af2f84', '00af2f8b']]`
  - `UNCONDITIONAL_JUMP` [`00af2f88`](#insn-00af2f88) → [`00af2fa8`](#insn-00af2fa8)
- ブロック [`00af2f8c`](#insn-00af2f8c) 範囲 `[['00af2f8c', '00af2fa7']]`
  - `CONDITIONAL_JUMP` [`00af2fa4`](#insn-00af2fa4) → [`00af3110`](#insn-00af3110)
  - `FALL_THROUGH` [`00af2fa4`](#insn-00af2fa4) → [`00af2fa8`](#insn-00af2fa8)
- ブロック [`00af2fa8`](#insn-00af2fa8) 範囲 `[['00af2fa8', '00af2fbb']]`
  - `CONDITIONAL_JUMP` [`00af2fb8`](#insn-00af2fb8) → [`00af2fdc`](#insn-00af2fdc)
  - `FALL_THROUGH` [`00af2fb8`](#insn-00af2fb8) → [`00af2fbc`](#insn-00af2fbc)
- ブロック [`00af2fbc`](#insn-00af2fbc) 範囲 `[['00af2fbc', '00af2fdb']]`
  - `FALL_THROUGH` [`00af2fd8`](#insn-00af2fd8) → [`00af2fdc`](#insn-00af2fdc)
- ブロック [`00af2fdc`](#insn-00af2fdc) 範囲 `[['00af2fdc', '00af3007']]`
  - `CONDITIONAL_JUMP` [`00af3004`](#insn-00af3004) → [`00af3028`](#insn-00af3028)
  - `FALL_THROUGH` [`00af3004`](#insn-00af3004) → [`00af3008`](#insn-00af3008)
- ブロック [`00af3008`](#insn-00af3008) 範囲 `[['00af3008', '00af3027']]`
  - `FALL_THROUGH` [`00af3024`](#insn-00af3024) → [`00af3028`](#insn-00af3028)
- ブロック [`00af3028`](#insn-00af3028) 範囲 `[['00af3028', '00af3057']]`
  - `CONDITIONAL_JUMP` [`00af3054`](#insn-00af3054) → [`00af307c`](#insn-00af307c)
  - `FALL_THROUGH` [`00af3054`](#insn-00af3054) → [`00af3058`](#insn-00af3058)
- ブロック [`00af3058`](#insn-00af3058) 範囲 `[['00af3058', '00af3067']]`
  - `CONDITIONAL_JUMP` [`00af3064`](#insn-00af3064) → [`00af3094`](#insn-00af3094)
  - `FALL_THROUGH` [`00af3064`](#insn-00af3064) → [`00af3068`](#insn-00af3068)
- ブロック [`00af3068`](#insn-00af3068) 範囲 `[['00af3068', '00af307b']]`
  - `UNCONDITIONAL_JUMP` [`00af3078`](#insn-00af3078) → [`00af30f4`](#insn-00af30f4)
- ブロック [`00af307c`](#insn-00af307c) 範囲 `[['00af307c', '00af308f']]`
  - `CONDITIONAL_JUMP` [`00af308c`](#insn-00af308c) → [`00af2f8c`](#insn-00af2f8c)
  - `FALL_THROUGH` [`00af308c`](#insn-00af308c) → [`00af3090`](#insn-00af3090)
- ブロック [`00af3090`](#insn-00af3090) 範囲 `[['00af3090', '00af3093']]`
  - `UNCONDITIONAL_JUMP` [`00af3090`](#insn-00af3090) → [`00af3104`](#insn-00af3104)
- ブロック [`00af3094`](#insn-00af3094) 範囲 `[['00af3094', '00af309f']]`
  - `CONDITIONAL_JUMP` [`00af309c`](#insn-00af309c) → [`00af3154`](#insn-00af3154)
  - `FALL_THROUGH` [`00af309c`](#insn-00af309c) → [`00af30a0`](#insn-00af30a0)
- ブロック [`00af30a0`](#insn-00af30a0) 範囲 `[['00af30a0', '00af30ab']]`
  - `CONDITIONAL_JUMP` [`00af30a8`](#insn-00af30a8) → [`00af30c0`](#insn-00af30c0)
  - `FALL_THROUGH` [`00af30a8`](#insn-00af30a8) → [`00af30ac`](#insn-00af30ac)
- ブロック [`00af30ac`](#insn-00af30ac) 範囲 `[['00af30ac', '00af30bb']]`
  - `CONDITIONAL_JUMP` [`00af30b8`](#insn-00af30b8) → [`00af30e0`](#insn-00af30e0)
  - `FALL_THROUGH` [`00af30b8`](#insn-00af30b8) → [`00af30bc`](#insn-00af30bc)
- ブロック [`00af30bc`](#insn-00af30bc) 範囲 `[['00af30bc', '00af30bf']]`
  - `UNCONDITIONAL_JUMP` [`00af30bc`](#insn-00af30bc) → [`00af30f0`](#insn-00af30f0)
- ブロック [`00af30c0`](#insn-00af30c0) 範囲 `[['00af30c0', '00af30df']]`
  - `FALL_THROUGH` [`00af30dc`](#insn-00af30dc) → [`00af30e0`](#insn-00af30e0)
- ブロック [`00af30e0`](#insn-00af30e0) 範囲 `[['00af30e0', '00af30ef']]`
  - `FALL_THROUGH` [`00af30ec`](#insn-00af30ec) → [`00af30f0`](#insn-00af30f0)
- ブロック [`00af30f0`](#insn-00af30f0) 範囲 `[['00af30f0', '00af30f3']]`
  - `FALL_THROUGH` [`00af30f0`](#insn-00af30f0) → [`00af30f4`](#insn-00af30f4)
- ブロック [`00af30f4`](#insn-00af30f4) 範囲 `[['00af30f4', '00af3103']]`
  - `CONDITIONAL_JUMP` [`00af3100`](#insn-00af3100) → [`00af2f8c`](#insn-00af2f8c)
  - `FALL_THROUGH` [`00af3100`](#insn-00af3100) → [`00af3104`](#insn-00af3104)
- ブロック [`00af3104`](#insn-00af3104) 範囲 `[['00af3104', '00af310f']]`
  - `UNCONDITIONAL_JUMP` [`00af310c`](#insn-00af310c) → [`00af2f8c`](#insn-00af2f8c)
- ブロック [`00af3110`](#insn-00af3110) 範囲 `[['00af3110', '00af3133']]`
  - `CONDITIONAL_JUMP` [`00af3130`](#insn-00af3130) → [`00af3158`](#insn-00af3158)
  - `FALL_THROUGH` [`00af3130`](#insn-00af3130) → [`00af3134`](#insn-00af3134)
- ブロック [`00af3134`](#insn-00af3134) 範囲 `[['00af3134', '00af3153']]`
- ブロック [`00af3154`](#insn-00af3154) 範囲 `[['00af3154', '00af3157']]`
- ブロック [`00af3158`](#insn-00af3158) 範囲 `[['00af3158', '00af315b']]`

## 命令位置別の参照

- [`00af2ee0`](#insn-00af2ee0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2ee4`](#insn-00af2ee4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2ee8`](#insn-00af2ee8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2eec`](#insn-00af2eec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2ef0`](#insn-00af2ef0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2ef4`](#insn-00af2ef4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2f00`](#insn-00af2f00) → `Stack[-0x88]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2f14`](#insn-00af2f14) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2f1c`](#insn-00af2f1c) → `010a0998`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af2f24`](#insn-00af2f24) → [`0047495c`](../00474/0047495c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047495c` · 推定シンボル `None` · 推定型 `None`
- [`00af2f40`](#insn-00af2f40) → [`00af2f64`](#insn-00af2f64) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2f68`](#insn-00af2f68) → `010a08c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af2f74`](#insn-00af2f74) → [`00474b70`](../00474/00474b70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00474b70` · 推定シンボル `None` · 推定型 `None`
- [`00af2f80`](#insn-00af2f80) → [`00af3110`](#insn-00af3110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2f88`](#insn-00af2f88) → [`00af2fa8`](#insn-00af2fa8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2f8c`](#insn-00af2f8c) → `010a08c8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af2f98`](#insn-00af2f98) → [`00474b70`](../00474/00474b70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00474b70` · 推定シンボル `None` · 推定型 `None`
- [`00af2fa4`](#insn-00af2fa4) → [`00af3110`](#insn-00af3110) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2fb8`](#insn-00af2fb8) → [`00af2fdc`](#insn-00af2fdc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af2fdc`](#insn-00af2fdc) → `010a08d0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00af2fe8`](#insn-00af2fe8) → [`0047495c`](../00474/0047495c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0047495c` · 推定シンボル `None` · 推定型 `None`
- [`00af3004`](#insn-00af3004) → [`00af3028`](#insn-00af3028) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3034`](#insn-00af3034) → [`00bde050`](../00bde/00bde050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde050` · 推定シンボル `None` · 推定型 `None`
- [`00af3054`](#insn-00af3054) → [`00af307c`](#insn-00af307c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3060`](#insn-00af3060) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3064`](#insn-00af3064) → [`00af3094`](#insn-00af3094) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3068`](#insn-00af3068) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af306c`](#insn-00af306c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3078`](#insn-00af3078) → [`00af30f4`](#insn-00af30f4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3084`](#insn-00af3084) → [`00bde770`](../00bde/00bde770.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde770` · 推定シンボル `None` · 推定型 `None`
- [`00af3088`](#insn-00af3088) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af308c`](#insn-00af308c) → [`00af2f8c`](#insn-00af2f8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3090`](#insn-00af3090) → [`00af3104`](#insn-00af3104) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3094`](#insn-00af3094) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af309c`](#insn-00af309c) → [`00af3154`](#insn-00af3154) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af30a0`](#insn-00af30a0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af30a8`](#insn-00af30a8) → [`00af30c0`](#insn-00af30c0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af30b8`](#insn-00af30b8) → [`00af30e0`](#insn-00af30e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af30bc`](#insn-00af30bc) → [`00af30f0`](#insn-00af30f0) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af30cc`](#insn-00af30cc) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00af30ec`](#insn-00af30ec) → [`00bdb160`](../00bdb/00bdb160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb160` · 推定シンボル `None` · 推定型 `None`
- [`00af30fc`](#insn-00af30fc) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3100`](#insn-00af3100) → [`00af2f8c`](#insn-00af2f8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3104`](#insn-00af3104) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3108`](#insn-00af3108) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00af310c`](#insn-00af310c) → [`00af2f8c`](#insn-00af2f8c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3120`](#insn-00af3120) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3128`](#insn-00af3128) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3130`](#insn-00af3130) → [`00af3158`](#insn-00af3158) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3134`](#insn-00af3134) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3138`](#insn-00af3138) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af313c`](#insn-00af313c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3140`](#insn-00af3140) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3144`](#insn-00af3144) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3148`](#insn-00af3148) → `Stack[-0x60]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00af3154`](#insn-00af3154) → [`00bde270`](../00bde/00bde270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bde270` · 推定シンボル `None` · 推定型 `None`
- [`00af3158`](#insn-00af3158) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00af2ee0`](#insn-00af2ee0)

~~~json
{
  "source": "00af2ee0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2ee4`](#insn-00af2ee4)

~~~json
{
  "source": "00af2ee4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2ee8`](#insn-00af2ee8)

~~~json
{
  "source": "00af2ee8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2eec`](#insn-00af2eec)

~~~json
{
  "source": "00af2eec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2ef0`](#insn-00af2ef0)

~~~json
{
  "source": "00af2ef0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2ef4`](#insn-00af2ef4)

~~~json
{
  "source": "00af2ef4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2f00`](#insn-00af2f00)

~~~json
{
  "source": "00af2f00",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2f14`](#insn-00af2f14)

~~~json
{
  "source": "00af2f14",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2f1c`](#insn-00af2f1c)

~~~json
{
  "source": "00af2f1c",
  "target": "010a0998",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0998",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af2f24`](#insn-00af2f24)

~~~json
{
  "source": "00af2f24",
  "target": "0047495c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af2f40`](#insn-00af2f40)

~~~json
{
  "source": "00af2f40",
  "target": "00af2f64",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2f68`](#insn-00af2f68)

~~~json
{
  "source": "00af2f68",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af2f74`](#insn-00af2f74)

~~~json
{
  "source": "00af2f74",
  "target": "00474b70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af2f80`](#insn-00af2f80)

~~~json
{
  "source": "00af2f80",
  "target": "00af3110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2f88`](#insn-00af2f88)

~~~json
{
  "source": "00af2f88",
  "target": "00af2fa8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2f8c`](#insn-00af2f8c)

~~~json
{
  "source": "00af2f8c",
  "target": "010a08c8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08c8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af2f98`](#insn-00af2f98)

~~~json
{
  "source": "00af2f98",
  "target": "00474b70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af2fa4`](#insn-00af2fa4)

~~~json
{
  "source": "00af2fa4",
  "target": "00af3110",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2fb8`](#insn-00af2fb8)

~~~json
{
  "source": "00af2fb8",
  "target": "00af2fdc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af2fdc`](#insn-00af2fdc)

~~~json
{
  "source": "00af2fdc",
  "target": "010a08d0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a08d0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00af2fe8`](#insn-00af2fe8)

~~~json
{
  "source": "00af2fe8",
  "target": "0047495c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3004`](#insn-00af3004)

~~~json
{
  "source": "00af3004",
  "target": "00af3028",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3034`](#insn-00af3034)

~~~json
{
  "source": "00af3034",
  "target": "00bde050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3054`](#insn-00af3054)

~~~json
{
  "source": "00af3054",
  "target": "00af307c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3060`](#insn-00af3060)

~~~json
{
  "source": "00af3060",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3064`](#insn-00af3064)

~~~json
{
  "source": "00af3064",
  "target": "00af3094",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3068`](#insn-00af3068)

~~~json
{
  "source": "00af3068",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af306c`](#insn-00af306c)

~~~json
{
  "source": "00af306c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3078`](#insn-00af3078)

~~~json
{
  "source": "00af3078",
  "target": "00af30f4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3084`](#insn-00af3084)

~~~json
{
  "source": "00af3084",
  "target": "00bde770",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3088`](#insn-00af3088)

~~~json
{
  "source": "00af3088",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af308c`](#insn-00af308c)

~~~json
{
  "source": "00af308c",
  "target": "00af2f8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3090`](#insn-00af3090)

~~~json
{
  "source": "00af3090",
  "target": "00af3104",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3094`](#insn-00af3094)

~~~json
{
  "source": "00af3094",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af309c`](#insn-00af309c)

~~~json
{
  "source": "00af309c",
  "target": "00af3154",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af30a0`](#insn-00af30a0)

~~~json
{
  "source": "00af30a0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af30a8`](#insn-00af30a8)

~~~json
{
  "source": "00af30a8",
  "target": "00af30c0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af30b8`](#insn-00af30b8)

~~~json
{
  "source": "00af30b8",
  "target": "00af30e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af30bc`](#insn-00af30bc)

~~~json
{
  "source": "00af30bc",
  "target": "00af30f0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af30cc`](#insn-00af30cc)

~~~json
{
  "source": "00af30cc",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af30ec`](#insn-00af30ec)

~~~json
{
  "source": "00af30ec",
  "target": "00bdb160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af30fc`](#insn-00af30fc)

~~~json
{
  "source": "00af30fc",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3100`](#insn-00af3100)

~~~json
{
  "source": "00af3100",
  "target": "00af2f8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3104`](#insn-00af3104)

~~~json
{
  "source": "00af3104",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3108`](#insn-00af3108)

~~~json
{
  "source": "00af3108",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af310c`](#insn-00af310c)

~~~json
{
  "source": "00af310c",
  "target": "00af2f8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3120`](#insn-00af3120)

~~~json
{
  "source": "00af3120",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3128`](#insn-00af3128)

~~~json
{
  "source": "00af3128",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3130`](#insn-00af3130)

~~~json
{
  "source": "00af3130",
  "target": "00af3158",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3134`](#insn-00af3134)

~~~json
{
  "source": "00af3134",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3138`](#insn-00af3138)

~~~json
{
  "source": "00af3138",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af313c`](#insn-00af313c)

~~~json
{
  "source": "00af313c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3140`](#insn-00af3140)

~~~json
{
  "source": "00af3140",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3144`](#insn-00af3144)

~~~json
{
  "source": "00af3144",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3148`](#insn-00af3148)

~~~json
{
  "source": "00af3148",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00af3154`](#insn-00af3154)

~~~json
{
  "source": "00af3154",
  "target": "00bde270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00af3158`](#insn-00af3158)

~~~json
{
  "source": "00af3158",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
