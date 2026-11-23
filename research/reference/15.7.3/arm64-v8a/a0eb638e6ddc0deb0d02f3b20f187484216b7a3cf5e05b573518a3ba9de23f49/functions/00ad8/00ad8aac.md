# 00ad8aac

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00ad89e4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00ad8/00ad89e4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-dfd1994f95375a4013890e057208c47c)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00ad8af0`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00ad8/00ad8af0.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0060.md#compare-443dd61427c1c11690e607bd457bb9fc)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad8aac",
  "name": "Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdOpened",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3471cf2ef7fd42c683aee2cabf448d3139b677c3e981119ae807b68131347c0",
  "source_text_sha256": "d3471cf2ef7fd42c683aee2cabf448d3139b677c3e981119ae807b68131347c0",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad8aac",
        "00ad8c03"
      ],
      [
        "00ad8c58",
        "00ad8c5b"
      ]
    ],
    "bytes_sha256": "6f6b0f828937581b11aac0e47a1dddd39155d30205365c8778e52778a6efe01e",
    "instruction_count": 87,
    "instruction_bytes": 348,
    "body_bytes": 348,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00436e9c](../00436/00436e9c.md)
- [00566a7c](../00566/00566a7c.md)
- [00574054](../00574/00574054.md)
- [0057473c](../00574/0057473c.md)
- [00bd6e50](../00bd6/00bd6e50.md)
- [00bdafe0](../00bda/00bdafe0.md)
- [00bdb010](../00bdb/00bdb010.md)
- [00bdb040](../00bdb/00bdb040.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2079 bytes

~~~c

void Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdOpened
               (undefined8 param_1,undefined8 param_2,undefined8 param_3)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  byte local_88 [16];
  void *local_78;
  undefined8 local_70;
  long *plStack_68;
  undefined8 local_60;
  long *plStack_58;
  undefined1 auStack_48 [8];
  long *local_40;
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (DAT_0109fea0 != (long *)0x0) {
    FUN_00566a7c(local_88,param_1,param_3);
    thunk_FUN_0056839c(&local_70,local_88);
    plStack_58 = plStack_68;
    local_60 = local_70;
    local_70 = 0;
    plStack_68 = (long *)0x0;
    FUN_00574054(auStack_48,&local_60);
    plVar2 = plStack_58;
    if ((plStack_58 != (long *)0x0) &&
       (lVar3 = FUN_00bd6e50(0xffffffffffffffff,plStack_58 + 1), lVar3 == 0)) {
      (**(code **)(*plVar2 + 0x10))(plVar2);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    }
    plVar2 = plStack_68;
    if ((plStack_68 != (long *)0x0) &&
       (lVar3 = FUN_00bd6e50(0xffffffffffffffff,plStack_68 + 1), lVar3 == 0)) {
                    /* try { // try from 00ad8bd4 to 00bd8c03 has its CatchHandler @ 00ad8cf8 */
      (**(code **)(*plVar2 + 0x10))(plVar2);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    }
    if ((local_88[0] & 1) != 0) {
      _ZdlPv(local_78);
    }
    if (DAT_0109fea0 == (long *)0x0) {
      if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
        FUN_00436e9c();
      }
      goto LAB_00ad8c58;
    }
    (**(code **)(*DAT_0109fea0 + 0x30))(DAT_0109fea0,auStack_48);
    if ((local_40 != (long *)0x0) &&
       (lVar3 = FUN_00bd6e50(0xffffffffffffffff,local_40 + 1), lVar3 == 0)) {
      (**(code **)(*local_40 + 0x10))(local_40);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_40);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
LAB_00ad8c58:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ad8aac"></a> `00ad8aac` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ad8ab0"></a> `00ad8ab0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad8ab4"></a> `00ad8ab4` | `f5 3b 00 f9` | str x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ad8ab8"></a> `00ad8ab8` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ad8abc"></a> `00ad8abc` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00ad8ac0"></a> `00ad8ac0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ad8ac4"></a> `00ad8ac4` | `35 2e 00 f0` | adrp x21,0x109f000 | `FALL_THROUGH`
<a id="insn-00ad8ac8"></a> `00ad8ac8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8acc"></a> `00ad8acc` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad8ad0"></a> `00ad8ad0` | `a8 52 47 f9` | ldr x8,[x21, #0xea0] | `FALL_THROUGH`
<a id="insn-00ad8ad4"></a> `00ad8ad4` | `a8 06 00 b4` | cbz x8,0x00ad8ba8 | `CONDITIONAL_JUMP`
<a id="insn-00ad8ad8"></a> `00ad8ad8` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8adc"></a> `00ad8adc` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00ad8ae0"></a> `00ad8ae0` | `e7 37 ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00ad8ae4"></a> `00ad8ae4` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad8ae8"></a> `00ad8ae8` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8aec"></a> `00ad8aec` | `14 6f ea 97` | bl 0x0057473c | `UNCONDITIONAL_CALL`
<a id="insn-00ad8af0"></a> `00ad8af0` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad8af4"></a> `00ad8af4` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad8af8"></a> `00ad8af8` | `e0 0f 80 3d` | str q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad8afc"></a> `00ad8afc` | `a8 63 00 d1` | sub x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00ad8b00"></a> `00ad8b00` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00ad8b04"></a> `00ad8b04` | `54 6d ea 97` | bl 0x00574054 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8b08"></a> `00ad8b08` | `f3 1f 40 f9` | ldr x19,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ad8b0c"></a> `00ad8b0c` | `73 01 00 b4` | cbz x19,0x00ad8b38 | `CONDITIONAL_JUMP`
<a id="insn-00ad8b10"></a> `00ad8b10` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8b14"></a> `00ad8b14` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ad8b18"></a> `00ad8b18` | `ce f8 03 94` | bl 0x00bd6e50 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8b1c"></a> `00ad8b1c` | `e0 00 00 b5` | cbnz x0,0x00ad8b38 | `CONDITIONAL_JUMP`
<a id="insn-00ad8b20"></a> `00ad8b20` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ad8b24"></a> `00ad8b24` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8b28"></a> `00ad8b28` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad8b2c"></a> `00ad8b2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8b30"></a> `00ad8b30` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8b34"></a> `00ad8b34` | `2b 09 04 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8b38"></a> `00ad8b38` | `f3 17 40 f9` | ldr x19,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8b3c"></a> `00ad8b3c` | `b3 00 00 b4` | cbz x19,0x00ad8b50 | `CONDITIONAL_JUMP`
<a id="insn-00ad8b40"></a> `00ad8b40` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8b44"></a> `00ad8b44` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ad8b48"></a> `00ad8b48` | `c2 f8 03 94` | bl 0x00bd6e50 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8b4c"></a> `00ad8b4c` | `00 04 00 b4` | cbz x0,0x00ad8bcc | `CONDITIONAL_JUMP`
<a id="insn-00ad8b50"></a> `00ad8b50` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ad8b54"></a> `00ad8b54` | `68 00 00 36` | tbz w8,#0x0,0x00ad8b60 | `CONDITIONAL_JUMP`
<a id="insn-00ad8b58"></a> `00ad8b58` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad8b5c"></a> `00ad8b5c` | `2d 09 04 94` | bl 0x00bdb010 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8b60"></a> `00ad8b60` | `a0 52 47 f9` | ldr x0,[x21, #0xea0] | `FALL_THROUGH`
<a id="insn-00ad8b64"></a> `00ad8b64` | `60 04 00 b4` | cbz x0,0x00ad8bf0 | `CONDITIONAL_JUMP`
<a id="insn-00ad8b68"></a> `00ad8b68` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad8b6c"></a> `00ad8b6c` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00ad8b70"></a> `00ad8b70` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00ad8b74"></a> `00ad8b74` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8b78"></a> `00ad8b78` | `b3 03 5f f8` | ldur x19,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ad8b7c"></a> `00ad8b7c` | `73 01 00 b4` | cbz x19,0x00ad8ba8 | `CONDITIONAL_JUMP`
<a id="insn-00ad8b80"></a> `00ad8b80` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8b84"></a> `00ad8b84` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ad8b88"></a> `00ad8b88` | `b2 f8 03 94` | bl 0x00bd6e50 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8b8c"></a> `00ad8b8c` | `e0 00 00 b5` | cbnz x0,0x00ad8ba8 | `CONDITIONAL_JUMP`
<a id="insn-00ad8b90"></a> `00ad8b90` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ad8b94"></a> `00ad8b94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8b98"></a> `00ad8b98` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad8b9c"></a> `00ad8b9c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8ba0"></a> `00ad8ba0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8ba4"></a> `00ad8ba4` | `0f 09 04 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8ba8"></a> `00ad8ba8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8bac"></a> `00ad8bac` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad8bb0"></a> `00ad8bb0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad8bb4"></a> `00ad8bb4` | `21 05 00 54` | b.ne 0x00ad8c58 | `CONDITIONAL_JUMP`
<a id="insn-00ad8bb8"></a> `00ad8bb8` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ad8bbc"></a> `00ad8bbc` | `f5 3b 40 f9` | ldr x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ad8bc0"></a> `00ad8bc0` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad8bc4"></a> `00ad8bc4` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ad8bc8"></a> `00ad8bc8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ad8bcc"></a> `00ad8bcc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ad8bd0"></a> `00ad8bd0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8bd4"></a> `00ad8bd4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad8bd8"></a> `00ad8bd8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8bdc"></a> `00ad8bdc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8be0"></a> `00ad8be0` | `00 09 04 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8be4"></a> `00ad8be4` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ad8be8"></a> `00ad8be8` | `88 fb 07 37` | tbnz w8,#0x0,0x00ad8b58 | `CONDITIONAL_JUMP`
<a id="insn-00ad8bec"></a> `00ad8bec` | `dd ff ff 17` | b 0x00ad8b60 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad8bf0"></a> `00ad8bf0` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8bf4"></a> `00ad8bf4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad8bf8"></a> `00ad8bf8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad8bfc"></a> `00ad8bfc` | `e1 02 00 54` | b.ne 0x00ad8c58 | `CONDITIONAL_JUMP`
<a id="insn-00ad8c00"></a> `00ad8c00` | `a7 78 e5 97` | bl 0x00436e9c | `CALL_TERMINATOR`
<a id="insn-00ad8c58"></a> `00ad8c58` | `fa 08 04 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad8aac`](#insn-00ad8aac) 範囲 `[['00ad8aac', '00ad8ad7']]`
  - `CONDITIONAL_JUMP` [`00ad8ad4`](#insn-00ad8ad4) → [`00ad8ba8`](#insn-00ad8ba8)
  - `FALL_THROUGH` [`00ad8ad4`](#insn-00ad8ad4) → [`00ad8ad8`](#insn-00ad8ad8)
- ブロック [`00ad8ad8`](#insn-00ad8ad8) 範囲 `[['00ad8ad8', '00ad8b0f']]`
  - `CONDITIONAL_JUMP` [`00ad8b0c`](#insn-00ad8b0c) → [`00ad8b38`](#insn-00ad8b38)
  - `FALL_THROUGH` [`00ad8b0c`](#insn-00ad8b0c) → [`00ad8b10`](#insn-00ad8b10)
- ブロック [`00ad8b10`](#insn-00ad8b10) 範囲 `[['00ad8b10', '00ad8b1f']]`
  - `CONDITIONAL_JUMP` [`00ad8b1c`](#insn-00ad8b1c) → [`00ad8b38`](#insn-00ad8b38)
  - `FALL_THROUGH` [`00ad8b1c`](#insn-00ad8b1c) → [`00ad8b20`](#insn-00ad8b20)
- ブロック [`00ad8b20`](#insn-00ad8b20) 範囲 `[['00ad8b20', '00ad8b37']]`
  - `FALL_THROUGH` [`00ad8b34`](#insn-00ad8b34) → [`00ad8b38`](#insn-00ad8b38)
- ブロック [`00ad8b38`](#insn-00ad8b38) 範囲 `[['00ad8b38', '00ad8b3f']]`
  - `CONDITIONAL_JUMP` [`00ad8b3c`](#insn-00ad8b3c) → [`00ad8b50`](#insn-00ad8b50)
  - `FALL_THROUGH` [`00ad8b3c`](#insn-00ad8b3c) → [`00ad8b40`](#insn-00ad8b40)
- ブロック [`00ad8b40`](#insn-00ad8b40) 範囲 `[['00ad8b40', '00ad8b4f']]`
  - `CONDITIONAL_JUMP` [`00ad8b4c`](#insn-00ad8b4c) → [`00ad8bcc`](#insn-00ad8bcc)
  - `FALL_THROUGH` [`00ad8b4c`](#insn-00ad8b4c) → [`00ad8b50`](#insn-00ad8b50)
- ブロック [`00ad8b50`](#insn-00ad8b50) 範囲 `[['00ad8b50', '00ad8b57']]`
  - `CONDITIONAL_JUMP` [`00ad8b54`](#insn-00ad8b54) → [`00ad8b60`](#insn-00ad8b60)
  - `FALL_THROUGH` [`00ad8b54`](#insn-00ad8b54) → [`00ad8b58`](#insn-00ad8b58)
- ブロック [`00ad8b58`](#insn-00ad8b58) 範囲 `[['00ad8b58', '00ad8b5f']]`
  - `FALL_THROUGH` [`00ad8b5c`](#insn-00ad8b5c) → [`00ad8b60`](#insn-00ad8b60)
- ブロック [`00ad8b60`](#insn-00ad8b60) 範囲 `[['00ad8b60', '00ad8b67']]`
  - `CONDITIONAL_JUMP` [`00ad8b64`](#insn-00ad8b64) → [`00ad8bf0`](#insn-00ad8bf0)
  - `FALL_THROUGH` [`00ad8b64`](#insn-00ad8b64) → [`00ad8b68`](#insn-00ad8b68)
- ブロック [`00ad8b68`](#insn-00ad8b68) 範囲 `[['00ad8b68', '00ad8b7f']]`
  - `CONDITIONAL_JUMP` [`00ad8b7c`](#insn-00ad8b7c) → [`00ad8ba8`](#insn-00ad8ba8)
  - `FALL_THROUGH` [`00ad8b7c`](#insn-00ad8b7c) → [`00ad8b80`](#insn-00ad8b80)
- ブロック [`00ad8b80`](#insn-00ad8b80) 範囲 `[['00ad8b80', '00ad8b8f']]`
  - `CONDITIONAL_JUMP` [`00ad8b8c`](#insn-00ad8b8c) → [`00ad8ba8`](#insn-00ad8ba8)
  - `FALL_THROUGH` [`00ad8b8c`](#insn-00ad8b8c) → [`00ad8b90`](#insn-00ad8b90)
- ブロック [`00ad8b90`](#insn-00ad8b90) 範囲 `[['00ad8b90', '00ad8ba7']]`
  - `FALL_THROUGH` [`00ad8ba4`](#insn-00ad8ba4) → [`00ad8ba8`](#insn-00ad8ba8)
- ブロック [`00ad8ba8`](#insn-00ad8ba8) 範囲 `[['00ad8ba8', '00ad8bb7']]`
  - `CONDITIONAL_JUMP` [`00ad8bb4`](#insn-00ad8bb4) → [`00ad8c58`](#insn-00ad8c58)
  - `FALL_THROUGH` [`00ad8bb4`](#insn-00ad8bb4) → [`00ad8bb8`](#insn-00ad8bb8)
- ブロック [`00ad8bb8`](#insn-00ad8bb8) 範囲 `[['00ad8bb8', '00ad8bcb']]`
- ブロック [`00ad8bcc`](#insn-00ad8bcc) 範囲 `[['00ad8bcc', '00ad8bd3']]`
  - `FALL_THROUGH` [`00ad8bd0`](#insn-00ad8bd0) → [`00ad8bd4`](#insn-00ad8bd4)
- ブロック [`00ad8bd4`](#insn-00ad8bd4) 範囲 `[['00ad8bd4', '00ad8beb']]`
  - `CONDITIONAL_JUMP` [`00ad8be8`](#insn-00ad8be8) → [`00ad8b58`](#insn-00ad8b58)
  - `FALL_THROUGH` [`00ad8be8`](#insn-00ad8be8) → [`00ad8bec`](#insn-00ad8bec)
- ブロック [`00ad8bec`](#insn-00ad8bec) 範囲 `[['00ad8bec', '00ad8bef']]`
  - `UNCONDITIONAL_JUMP` [`00ad8bec`](#insn-00ad8bec) → [`00ad8b60`](#insn-00ad8b60)
- ブロック [`00ad8bf0`](#insn-00ad8bf0) 範囲 `[['00ad8bf0', '00ad8bff']]`
  - `CONDITIONAL_JUMP` [`00ad8bfc`](#insn-00ad8bfc) → [`00ad8c58`](#insn-00ad8c58)
  - `FALL_THROUGH` [`00ad8bfc`](#insn-00ad8bfc) → [`00ad8c00`](#insn-00ad8c00)
- ブロック [`00ad8c00`](#insn-00ad8c00) 範囲 `[['00ad8c00', '00ad8c03']]`
- ブロック [`00ad8c58`](#insn-00ad8c58) 範囲 `[['00ad8c58', '00ad8c5b']]`

## 命令位置別の参照

- [`00ad8ab0`](#insn-00ad8ab0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8ab4`](#insn-00ad8ab4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8ab8`](#insn-00ad8ab8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8acc`](#insn-00ad8acc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8ad0`](#insn-00ad8ad0) → `0109fea0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad8ad4`](#insn-00ad8ad4) → [`00ad8ba8`](#insn-00ad8ba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8ae0`](#insn-00ad8ae0) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00ad8aec`](#insn-00ad8aec) → [`0057473c`](../00574/0057473c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057473c` · 推定シンボル `None` · 推定型 `None`
- [`00ad8af0`](#insn-00ad8af0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8af4`](#insn-00ad8af4) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8af8`](#insn-00ad8af8) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b04`](#insn-00ad8b04) → [`00574054`](../00574/00574054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574054` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b08`](#insn-00ad8b08) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b0c`](#insn-00ad8b0c) → [`00ad8b38`](#insn-00ad8b38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b18`](#insn-00ad8b18) → [`00bd6e50`](../00bd6/00bd6e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e50` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b1c`](#insn-00ad8b1c) → [`00ad8b38`](#insn-00ad8b38) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b34`](#insn-00ad8b34) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b38`](#insn-00ad8b38) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b3c`](#insn-00ad8b3c) → [`00ad8b50`](#insn-00ad8b50) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b48`](#insn-00ad8b48) → [`00bd6e50`](../00bd6/00bd6e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e50` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b4c`](#insn-00ad8b4c) → [`00ad8bcc`](#insn-00ad8bcc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b50`](#insn-00ad8b50) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b54`](#insn-00ad8b54) → [`00ad8b60`](#insn-00ad8b60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b58`](#insn-00ad8b58) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b5c`](#insn-00ad8b5c) → [`00bdb010`](../00bdb/00bdb010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb010` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b60`](#insn-00ad8b60) → `0109fea0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad8b64`](#insn-00ad8b64) → [`00ad8bf0`](#insn-00ad8bf0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b78`](#insn-00ad8b78) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b7c`](#insn-00ad8b7c) → [`00ad8ba8`](#insn-00ad8ba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b88`](#insn-00ad8b88) → [`00bd6e50`](../00bd6/00bd6e50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6e50` · 推定シンボル `None` · 推定型 `None`
- [`00ad8b8c`](#insn-00ad8b8c) → [`00ad8ba8`](#insn-00ad8ba8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8ba4`](#insn-00ad8ba4) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00ad8bac`](#insn-00ad8bac) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8bb4`](#insn-00ad8bb4) → [`00ad8c58`](#insn-00ad8c58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8bb8`](#insn-00ad8bb8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8bbc`](#insn-00ad8bbc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8bc0`](#insn-00ad8bc0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8be0`](#insn-00ad8be0) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00ad8be4`](#insn-00ad8be4) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8be8`](#insn-00ad8be8) → [`00ad8b58`](#insn-00ad8b58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8bec`](#insn-00ad8bec) → [`00ad8b60`](#insn-00ad8b60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8bf4`](#insn-00ad8bf4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8bfc`](#insn-00ad8bfc) → [`00ad8c58`](#insn-00ad8c58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8c00`](#insn-00ad8c00) → [`00436e9c`](../00436/00436e9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00436e9c` · 推定シンボル `None` · 推定型 `None`
- [`00ad8c58`](#insn-00ad8c58) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad8ab0`](#insn-00ad8ab0)

~~~json
{
  "source": "00ad8ab0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8ab4`](#insn-00ad8ab4)

~~~json
{
  "source": "00ad8ab4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8ab8`](#insn-00ad8ab8)

~~~json
{
  "source": "00ad8ab8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8acc`](#insn-00ad8acc)

~~~json
{
  "source": "00ad8acc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8ad0`](#insn-00ad8ad0)

~~~json
{
  "source": "00ad8ad0",
  "target": "0109fea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad8ad4`](#insn-00ad8ad4)

~~~json
{
  "source": "00ad8ad4",
  "target": "00ad8ba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8ae0`](#insn-00ad8ae0)

~~~json
{
  "source": "00ad8ae0",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8aec`](#insn-00ad8aec)

~~~json
{
  "source": "00ad8aec",
  "target": "0057473c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8af0`](#insn-00ad8af0)

~~~json
{
  "source": "00ad8af0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8af4`](#insn-00ad8af4)

~~~json
{
  "source": "00ad8af4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8af8`](#insn-00ad8af8)

~~~json
{
  "source": "00ad8af8",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b04`](#insn-00ad8b04)

~~~json
{
  "source": "00ad8b04",
  "target": "00574054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8b08`](#insn-00ad8b08)

~~~json
{
  "source": "00ad8b08",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b0c`](#insn-00ad8b0c)

~~~json
{
  "source": "00ad8b0c",
  "target": "00ad8b38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b18`](#insn-00ad8b18)

~~~json
{
  "source": "00ad8b18",
  "target": "00bd6e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8b1c`](#insn-00ad8b1c)

~~~json
{
  "source": "00ad8b1c",
  "target": "00ad8b38",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b34`](#insn-00ad8b34)

~~~json
{
  "source": "00ad8b34",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8b38`](#insn-00ad8b38)

~~~json
{
  "source": "00ad8b38",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b3c`](#insn-00ad8b3c)

~~~json
{
  "source": "00ad8b3c",
  "target": "00ad8b50",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b48`](#insn-00ad8b48)

~~~json
{
  "source": "00ad8b48",
  "target": "00bd6e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8b4c`](#insn-00ad8b4c)

~~~json
{
  "source": "00ad8b4c",
  "target": "00ad8bcc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b50`](#insn-00ad8b50)

~~~json
{
  "source": "00ad8b50",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b54`](#insn-00ad8b54)

~~~json
{
  "source": "00ad8b54",
  "target": "00ad8b60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b58`](#insn-00ad8b58)

~~~json
{
  "source": "00ad8b58",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b5c`](#insn-00ad8b5c)

~~~json
{
  "source": "00ad8b5c",
  "target": "00bdb010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8b60`](#insn-00ad8b60)

~~~json
{
  "source": "00ad8b60",
  "target": "0109fea0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fea0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad8b64`](#insn-00ad8b64)

~~~json
{
  "source": "00ad8b64",
  "target": "00ad8bf0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b78`](#insn-00ad8b78)

~~~json
{
  "source": "00ad8b78",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b7c`](#insn-00ad8b7c)

~~~json
{
  "source": "00ad8b7c",
  "target": "00ad8ba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8b88`](#insn-00ad8b88)

~~~json
{
  "source": "00ad8b88",
  "target": "00bd6e50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8b8c`](#insn-00ad8b8c)

~~~json
{
  "source": "00ad8b8c",
  "target": "00ad8ba8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8ba4`](#insn-00ad8ba4)

~~~json
{
  "source": "00ad8ba4",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8bac`](#insn-00ad8bac)

~~~json
{
  "source": "00ad8bac",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8bb4`](#insn-00ad8bb4)

~~~json
{
  "source": "00ad8bb4",
  "target": "00ad8c58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8bb8`](#insn-00ad8bb8)

~~~json
{
  "source": "00ad8bb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8bbc`](#insn-00ad8bbc)

~~~json
{
  "source": "00ad8bbc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8bc0`](#insn-00ad8bc0)

~~~json
{
  "source": "00ad8bc0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8be0`](#insn-00ad8be0)

~~~json
{
  "source": "00ad8be0",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8be4`](#insn-00ad8be4)

~~~json
{
  "source": "00ad8be4",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8be8`](#insn-00ad8be8)

~~~json
{
  "source": "00ad8be8",
  "target": "00ad8b58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8bec`](#insn-00ad8bec)

~~~json
{
  "source": "00ad8bec",
  "target": "00ad8b60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8bf4`](#insn-00ad8bf4)

~~~json
{
  "source": "00ad8bf4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8bfc`](#insn-00ad8bfc)

~~~json
{
  "source": "00ad8bfc",
  "target": "00ad8c58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8c00`](#insn-00ad8c00)

~~~json
{
  "source": "00ad8c00",
  "target": "00436e9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8c58`](#insn-00ad8c58)

~~~json
{
  "source": "00ad8c58",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
