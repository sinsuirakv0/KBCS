# 00ad8dcc

版: 15.7.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea`

解析リビジョン `5ed057380ac853a2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版** 公開版なし

- **次の公開版 v15.7.3**
  - 採用 · [関数詳細 `00ad8e94`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00ad8/00ad8e94.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0057.md#compare-6bc3ed1547fa7dc97b1ef1935b050cdd)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ad8dcc",
  "name": "Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdClosed",
  "size": 348,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "df2c72a698f12fc132547e945a99e341eadf5b2cfa1d3015cb98b903609bfb30",
  "source_text_sha256": "df2c72a698f12fc132547e945a99e341eadf5b2cfa1d3015cb98b903609bfb30",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410f235c7222fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ad8dcc",
        "00ad8f23"
      ],
      [
        "00ad8f78",
        "00ad8f7b"
      ]
    ],
    "bytes_sha256": "a49fd58d9aab4f4e711292341537fd0c9f476e362fcf31cdfe71fd35e2fabf50",
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
- [00bd6d90](../00bd6/00bd6d90.md)
- [00bdaf30](../00bda/00bdaf30.md)
- [00bdaf60](../00bda/00bdaf60.md)
- [00bdaf90](../00bda/00bdaf90.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2273 bytes

~~~c

void Java_jp_co_ponos_battlecats_IronSourceImplementation_onAdClosed
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
  if (DAT_0109fe10 != (long *)0x0) {
    FUN_00566a7c(local_88,param_1,param_3);
    thunk_FUN_0056839c(&local_70,local_88);
    plStack_58 = plStack_68;
    local_60 = local_70;
    local_70 = 0;
    plStack_68 = (long *)0x0;
    FUN_00574054(auStack_48,&local_60);
    plVar2 = plStack_58;
    if ((plStack_58 != (long *)0x0) &&
       (lVar3 = FUN_00bd6d90(0xffffffffffffffff,plStack_58 + 1), lVar3 == 0)) {
      (**(code **)(*plVar2 + 0x10))(plVar2);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    }
    plVar2 = plStack_68;
    if ((plStack_68 != (long *)0x0) &&
       (lVar3 = FUN_00bd6d90(0xffffffffffffffff,plStack_68 + 1), lVar3 == 0)) {
                    /* try { // try from 00ad8ef4 to 00bd8f37 has its CatchHandler @ 00ad8fb0 */
      (**(code **)(*plVar2 + 0x10))(plVar2);
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar2);
    }
    if ((local_88[0] & 1) != 0) {
      _ZdlPv(local_78);
    }
    if (DAT_0109fe10 == (long *)0x0) {
      if (*(long *)(lVar1 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
        FUN_00436e9c();
      }
      goto LAB_00ad8f78;
    }
                    /* try { // try from 00ad8e90 to 00bd8ebf has its CatchHandler @ 00ad8fb4 */
    (**(code **)(*DAT_0109fe10 + 0x30))(DAT_0109fe10,auStack_48);
    if ((local_40 != (long *)0x0) &&
       (lVar3 = FUN_00bd6d90(0xffffffffffffffff,local_40 + 1), lVar3 == 0)) {
      (**(code **)(*local_40 + 0x10))(local_40);
                    /* try { // try from 00ad8ec0 to 00bd8ef3 has its CatchHandler @ 00ad8d28 */
      _ZNSt6__ndk119__shared_weak_count14__release_weakEv(local_40);
    }
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
LAB_00ad8f78:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00ad8dcc"></a> `00ad8dcc` | `ff 43 02 d1` | sub sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ad8dd0"></a> `00ad8dd0` | `fd 7b 06 a9` | stp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad8dd4"></a> `00ad8dd4` | `f5 3b 00 f9` | str x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ad8dd8"></a> `00ad8dd8` | `f4 4f 08 a9` | stp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ad8ddc"></a> `00ad8ddc` | `fd 83 01 91` | add x29,sp,#0x60 | `FALL_THROUGH`
<a id="insn-00ad8de0"></a> `00ad8de0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ad8de4"></a> `00ad8de4` | `35 2e 00 f0` | adrp x21,0x109f000 | `FALL_THROUGH`
<a id="insn-00ad8de8"></a> `00ad8de8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8dec"></a> `00ad8dec` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad8df0"></a> `00ad8df0` | `a8 0a 47 f9` | ldr x8,[x21, #0xe10] | `FALL_THROUGH`
<a id="insn-00ad8df4"></a> `00ad8df4` | `a8 06 00 b4` | cbz x8,0x00ad8ec8 | `CONDITIONAL_JUMP`
<a id="insn-00ad8df8"></a> `00ad8df8` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8dfc"></a> `00ad8dfc` | `e1 03 02 aa` | mov x1,x2 | `FALL_THROUGH`
<a id="insn-00ad8e00"></a> `00ad8e00` | `1f 37 ea 97` | bl 0x00566a7c | `UNCONDITIONAL_CALL`
<a id="insn-00ad8e04"></a> `00ad8e04` | `e8 83 00 91` | add x8,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00ad8e08"></a> `00ad8e08` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8e0c"></a> `00ad8e0c` | `4c 6e ea 97` | bl 0x0057473c | `UNCONDITIONAL_CALL`
<a id="insn-00ad8e10"></a> `00ad8e10` | `e0 0b c0 3d` | ldr q0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad8e14"></a> `00ad8e14` | `ff 7f 02 a9` | stp xzr,xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ad8e18"></a> `00ad8e18` | `e0 0f 80 3d` | str q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00ad8e1c"></a> `00ad8e1c` | `a8 63 00 d1` | sub x8,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00ad8e20"></a> `00ad8e20` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00ad8e24"></a> `00ad8e24` | `8c 6c ea 97` | bl 0x00574054 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8e28"></a> `00ad8e28` | `f3 1f 40 f9` | ldr x19,[sp, #0x38] | `FALL_THROUGH`
<a id="insn-00ad8e2c"></a> `00ad8e2c` | `73 01 00 b4` | cbz x19,0x00ad8e58 | `CONDITIONAL_JUMP`
<a id="insn-00ad8e30"></a> `00ad8e30` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8e34"></a> `00ad8e34` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ad8e38"></a> `00ad8e38` | `d6 f7 03 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8e3c"></a> `00ad8e3c` | `e0 00 00 b5` | cbnz x0,0x00ad8e58 | `CONDITIONAL_JUMP`
<a id="insn-00ad8e40"></a> `00ad8e40` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ad8e44"></a> `00ad8e44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8e48"></a> `00ad8e48` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad8e4c"></a> `00ad8e4c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8e50"></a> `00ad8e50` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8e54"></a> `00ad8e54` | `37 08 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8e58"></a> `00ad8e58` | `f3 17 40 f9` | ldr x19,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8e5c"></a> `00ad8e5c` | `b3 00 00 b4` | cbz x19,0x00ad8e70 | `CONDITIONAL_JUMP`
<a id="insn-00ad8e60"></a> `00ad8e60` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8e64"></a> `00ad8e64` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ad8e68"></a> `00ad8e68` | `ca f7 03 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8e6c"></a> `00ad8e6c` | `00 04 00 b4` | cbz x0,0x00ad8eec | `CONDITIONAL_JUMP`
<a id="insn-00ad8e70"></a> `00ad8e70` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ad8e74"></a> `00ad8e74` | `68 00 00 36` | tbz w8,#0x0,0x00ad8e80 | `CONDITIONAL_JUMP`
<a id="insn-00ad8e78"></a> `00ad8e78` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00ad8e7c"></a> `00ad8e7c` | `39 08 04 94` | bl 0x00bdaf60 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8e80"></a> `00ad8e80` | `a0 0a 47 f9` | ldr x0,[x21, #0xe10] | `FALL_THROUGH`
<a id="insn-00ad8e84"></a> `00ad8e84` | `60 04 00 b4` | cbz x0,0x00ad8f10 | `CONDITIONAL_JUMP`
<a id="insn-00ad8e88"></a> `00ad8e88` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ad8e8c"></a> `00ad8e8c` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00ad8e90"></a> `00ad8e90` | `a1 63 00 d1` | sub x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00ad8e94"></a> `00ad8e94` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8e98"></a> `00ad8e98` | `b3 03 5f f8` | ldur x19,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-00ad8e9c"></a> `00ad8e9c` | `73 01 00 b4` | cbz x19,0x00ad8ec8 | `CONDITIONAL_JUMP`
<a id="insn-00ad8ea0"></a> `00ad8ea0` | `61 22 00 91` | add x1,x19,#0x8 | `FALL_THROUGH`
<a id="insn-00ad8ea4"></a> `00ad8ea4` | `00 00 80 92` | mov x0,#-0x1 | `FALL_THROUGH`
<a id="insn-00ad8ea8"></a> `00ad8ea8` | `ba f7 03 94` | bl 0x00bd6d90 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8eac"></a> `00ad8eac` | `e0 00 00 b5` | cbnz x0,0x00ad8ec8 | `CONDITIONAL_JUMP`
<a id="insn-00ad8eb0"></a> `00ad8eb0` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ad8eb4"></a> `00ad8eb4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8eb8"></a> `00ad8eb8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad8ebc"></a> `00ad8ebc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8ec0"></a> `00ad8ec0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8ec4"></a> `00ad8ec4` | `1b 08 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8ec8"></a> `00ad8ec8` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8ecc"></a> `00ad8ecc` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad8ed0"></a> `00ad8ed0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad8ed4"></a> `00ad8ed4` | `21 05 00 54` | b.ne 0x00ad8f78 | `CONDITIONAL_JUMP`
<a id="insn-00ad8ed8"></a> `00ad8ed8` | `f4 4f 48 a9` | ldp x20,x19,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-00ad8edc"></a> `00ad8edc` | `f5 3b 40 f9` | ldr x21,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00ad8ee0"></a> `00ad8ee0` | `fd 7b 46 a9` | ldp x29,x30,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ad8ee4"></a> `00ad8ee4` | `ff 43 02 91` | add sp,sp,#0x90 | `FALL_THROUGH`
<a id="insn-00ad8ee8"></a> `00ad8ee8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ad8eec"></a> `00ad8eec` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00ad8ef0"></a> `00ad8ef0` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8ef4"></a> `00ad8ef4` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ad8ef8"></a> `00ad8ef8` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ad8efc"></a> `00ad8efc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00ad8f00"></a> `00ad8f00` | `0c 08 04 94` | bl 0x00bdaf30 | `UNCONDITIONAL_CALL`
<a id="insn-00ad8f04"></a> `00ad8f04` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-00ad8f08"></a> `00ad8f08` | `88 fb 07 37` | tbnz w8,#0x0,0x00ad8e78 | `CONDITIONAL_JUMP`
<a id="insn-00ad8f0c"></a> `00ad8f0c` | `dd ff ff 17` | b 0x00ad8e80 | `UNCONDITIONAL_JUMP`
<a id="insn-00ad8f10"></a> `00ad8f10` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00ad8f14"></a> `00ad8f14` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ad8f18"></a> `00ad8f18` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ad8f1c"></a> `00ad8f1c` | `e1 02 00 54` | b.ne 0x00ad8f78 | `CONDITIONAL_JUMP`
<a id="insn-00ad8f20"></a> `00ad8f20` | `df 77 e5 97` | bl 0x00436e9c | `CALL_TERMINATOR`
<a id="insn-00ad8f78"></a> `00ad8f78` | `06 08 04 94` | bl 0x00bdaf90 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ad8dcc`](#insn-00ad8dcc) 範囲 `[['00ad8dcc', '00ad8df7']]`
  - `CONDITIONAL_JUMP` [`00ad8df4`](#insn-00ad8df4) → [`00ad8ec8`](#insn-00ad8ec8)
  - `FALL_THROUGH` [`00ad8df4`](#insn-00ad8df4) → [`00ad8df8`](#insn-00ad8df8)
- ブロック [`00ad8df8`](#insn-00ad8df8) 範囲 `[['00ad8df8', '00ad8e2f']]`
  - `CONDITIONAL_JUMP` [`00ad8e2c`](#insn-00ad8e2c) → [`00ad8e58`](#insn-00ad8e58)
  - `FALL_THROUGH` [`00ad8e2c`](#insn-00ad8e2c) → [`00ad8e30`](#insn-00ad8e30)
- ブロック [`00ad8e30`](#insn-00ad8e30) 範囲 `[['00ad8e30', '00ad8e3f']]`
  - `CONDITIONAL_JUMP` [`00ad8e3c`](#insn-00ad8e3c) → [`00ad8e58`](#insn-00ad8e58)
  - `FALL_THROUGH` [`00ad8e3c`](#insn-00ad8e3c) → [`00ad8e40`](#insn-00ad8e40)
- ブロック [`00ad8e40`](#insn-00ad8e40) 範囲 `[['00ad8e40', '00ad8e57']]`
  - `FALL_THROUGH` [`00ad8e54`](#insn-00ad8e54) → [`00ad8e58`](#insn-00ad8e58)
- ブロック [`00ad8e58`](#insn-00ad8e58) 範囲 `[['00ad8e58', '00ad8e5f']]`
  - `CONDITIONAL_JUMP` [`00ad8e5c`](#insn-00ad8e5c) → [`00ad8e70`](#insn-00ad8e70)
  - `FALL_THROUGH` [`00ad8e5c`](#insn-00ad8e5c) → [`00ad8e60`](#insn-00ad8e60)
- ブロック [`00ad8e60`](#insn-00ad8e60) 範囲 `[['00ad8e60', '00ad8e6f']]`
  - `CONDITIONAL_JUMP` [`00ad8e6c`](#insn-00ad8e6c) → [`00ad8eec`](#insn-00ad8eec)
  - `FALL_THROUGH` [`00ad8e6c`](#insn-00ad8e6c) → [`00ad8e70`](#insn-00ad8e70)
- ブロック [`00ad8e70`](#insn-00ad8e70) 範囲 `[['00ad8e70', '00ad8e77']]`
  - `CONDITIONAL_JUMP` [`00ad8e74`](#insn-00ad8e74) → [`00ad8e80`](#insn-00ad8e80)
  - `FALL_THROUGH` [`00ad8e74`](#insn-00ad8e74) → [`00ad8e78`](#insn-00ad8e78)
- ブロック [`00ad8e78`](#insn-00ad8e78) 範囲 `[['00ad8e78', '00ad8e7f']]`
  - `FALL_THROUGH` [`00ad8e7c`](#insn-00ad8e7c) → [`00ad8e80`](#insn-00ad8e80)
- ブロック [`00ad8e80`](#insn-00ad8e80) 範囲 `[['00ad8e80', '00ad8e87']]`
  - `CONDITIONAL_JUMP` [`00ad8e84`](#insn-00ad8e84) → [`00ad8f10`](#insn-00ad8f10)
  - `FALL_THROUGH` [`00ad8e84`](#insn-00ad8e84) → [`00ad8e88`](#insn-00ad8e88)
- ブロック [`00ad8e88`](#insn-00ad8e88) 範囲 `[['00ad8e88', '00ad8e8f']]`
  - `FALL_THROUGH` [`00ad8e8c`](#insn-00ad8e8c) → [`00ad8e90`](#insn-00ad8e90)
- ブロック [`00ad8e90`](#insn-00ad8e90) 範囲 `[['00ad8e90', '00ad8e9f']]`
  - `CONDITIONAL_JUMP` [`00ad8e9c`](#insn-00ad8e9c) → [`00ad8ec8`](#insn-00ad8ec8)
  - `FALL_THROUGH` [`00ad8e9c`](#insn-00ad8e9c) → [`00ad8ea0`](#insn-00ad8ea0)
- ブロック [`00ad8ea0`](#insn-00ad8ea0) 範囲 `[['00ad8ea0', '00ad8eaf']]`
  - `CONDITIONAL_JUMP` [`00ad8eac`](#insn-00ad8eac) → [`00ad8ec8`](#insn-00ad8ec8)
  - `FALL_THROUGH` [`00ad8eac`](#insn-00ad8eac) → [`00ad8eb0`](#insn-00ad8eb0)
- ブロック [`00ad8eb0`](#insn-00ad8eb0) 範囲 `[['00ad8eb0', '00ad8ebf']]`
  - `FALL_THROUGH` [`00ad8ebc`](#insn-00ad8ebc) → [`00ad8ec0`](#insn-00ad8ec0)
- ブロック [`00ad8ec0`](#insn-00ad8ec0) 範囲 `[['00ad8ec0', '00ad8ec7']]`
  - `FALL_THROUGH` [`00ad8ec4`](#insn-00ad8ec4) → [`00ad8ec8`](#insn-00ad8ec8)
- ブロック [`00ad8ec8`](#insn-00ad8ec8) 範囲 `[['00ad8ec8', '00ad8ed7']]`
  - `CONDITIONAL_JUMP` [`00ad8ed4`](#insn-00ad8ed4) → [`00ad8f78`](#insn-00ad8f78)
  - `FALL_THROUGH` [`00ad8ed4`](#insn-00ad8ed4) → [`00ad8ed8`](#insn-00ad8ed8)
- ブロック [`00ad8ed8`](#insn-00ad8ed8) 範囲 `[['00ad8ed8', '00ad8eeb']]`
- ブロック [`00ad8eec`](#insn-00ad8eec) 範囲 `[['00ad8eec', '00ad8ef3']]`
  - `FALL_THROUGH` [`00ad8ef0`](#insn-00ad8ef0) → [`00ad8ef4`](#insn-00ad8ef4)
- ブロック [`00ad8ef4`](#insn-00ad8ef4) 範囲 `[['00ad8ef4', '00ad8f0b']]`
  - `CONDITIONAL_JUMP` [`00ad8f08`](#insn-00ad8f08) → [`00ad8e78`](#insn-00ad8e78)
  - `FALL_THROUGH` [`00ad8f08`](#insn-00ad8f08) → [`00ad8f0c`](#insn-00ad8f0c)
- ブロック [`00ad8f0c`](#insn-00ad8f0c) 範囲 `[['00ad8f0c', '00ad8f0f']]`
  - `UNCONDITIONAL_JUMP` [`00ad8f0c`](#insn-00ad8f0c) → [`00ad8e80`](#insn-00ad8e80)
- ブロック [`00ad8f10`](#insn-00ad8f10) 範囲 `[['00ad8f10', '00ad8f1f']]`
  - `CONDITIONAL_JUMP` [`00ad8f1c`](#insn-00ad8f1c) → [`00ad8f78`](#insn-00ad8f78)
  - `FALL_THROUGH` [`00ad8f1c`](#insn-00ad8f1c) → [`00ad8f20`](#insn-00ad8f20)
- ブロック [`00ad8f20`](#insn-00ad8f20) 範囲 `[['00ad8f20', '00ad8f23']]`
- ブロック [`00ad8f78`](#insn-00ad8f78) 範囲 `[['00ad8f78', '00ad8f7b']]`

## 命令位置別の参照

- [`00ad8dd0`](#insn-00ad8dd0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8dd4`](#insn-00ad8dd4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8dd8`](#insn-00ad8dd8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8dec`](#insn-00ad8dec) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8df0`](#insn-00ad8df0) → `0109fe10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad8df4`](#insn-00ad8df4) → [`00ad8ec8`](#insn-00ad8ec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e00`](#insn-00ad8e00) → [`00566a7c`](../00566/00566a7c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00566a7c` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e0c`](#insn-00ad8e0c) → [`0057473c`](../00574/0057473c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057473c` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e10`](#insn-00ad8e10) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e14`](#insn-00ad8e14) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e18`](#insn-00ad8e18) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e24`](#insn-00ad8e24) → [`00574054`](../00574/00574054.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00574054` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e28`](#insn-00ad8e28) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e2c`](#insn-00ad8e2c) → [`00ad8e58`](#insn-00ad8e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e38`](#insn-00ad8e38) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e3c`](#insn-00ad8e3c) → [`00ad8e58`](#insn-00ad8e58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e54`](#insn-00ad8e54) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e58`](#insn-00ad8e58) → `Stack[-0x68]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e5c`](#insn-00ad8e5c) → [`00ad8e70`](#insn-00ad8e70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e68`](#insn-00ad8e68) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e6c`](#insn-00ad8e6c) → [`00ad8eec`](#insn-00ad8eec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e70`](#insn-00ad8e70) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e74`](#insn-00ad8e74) → [`00ad8e80`](#insn-00ad8e80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e78`](#insn-00ad8e78) → `Stack[-0x78]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e7c`](#insn-00ad8e7c) → [`00bdaf60`](../00bda/00bdaf60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf60` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e80`](#insn-00ad8e80) → `0109fe10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00ad8e84`](#insn-00ad8e84) → [`00ad8f10`](#insn-00ad8f10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e98`](#insn-00ad8e98) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8e9c`](#insn-00ad8e9c) → [`00ad8ec8`](#insn-00ad8ec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8ea8`](#insn-00ad8ea8) → [`00bd6d90`](../00bd6/00bd6d90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bd6d90` · 推定シンボル `None` · 推定型 `None`
- [`00ad8eac`](#insn-00ad8eac) → [`00ad8ec8`](#insn-00ad8ec8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8ec4`](#insn-00ad8ec4) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00ad8ecc`](#insn-00ad8ecc) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8ed4`](#insn-00ad8ed4) → [`00ad8f78`](#insn-00ad8f78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8ed8`](#insn-00ad8ed8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8edc`](#insn-00ad8edc) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8ee0`](#insn-00ad8ee0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8f00`](#insn-00ad8f00) → [`00bdaf30`](../00bda/00bdaf30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf30` · 推定シンボル `None` · 推定型 `None`
- [`00ad8f04`](#insn-00ad8f04) → `Stack[-0x88]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8f08`](#insn-00ad8f08) → [`00ad8e78`](#insn-00ad8e78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8f0c`](#insn-00ad8f0c) → [`00ad8e80`](#insn-00ad8e80) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8f14`](#insn-00ad8f14) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8f1c`](#insn-00ad8f1c) → [`00ad8f78`](#insn-00ad8f78) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ad8f20`](#insn-00ad8f20) → [`00436e9c`](../00436/00436e9c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00436e9c` · 推定シンボル `None` · 推定型 `None`
- [`00ad8f78`](#insn-00ad8f78) → [`00bdaf90`](../00bda/00bdaf90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaf90` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ad8dd0`](#insn-00ad8dd0)

~~~json
{
  "source": "00ad8dd0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8dd4`](#insn-00ad8dd4)

~~~json
{
  "source": "00ad8dd4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8dd8`](#insn-00ad8dd8)

~~~json
{
  "source": "00ad8dd8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8dec`](#insn-00ad8dec)

~~~json
{
  "source": "00ad8dec",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8df0`](#insn-00ad8df0)

~~~json
{
  "source": "00ad8df0",
  "target": "0109fe10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad8df4`](#insn-00ad8df4)

~~~json
{
  "source": "00ad8df4",
  "target": "00ad8ec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e00`](#insn-00ad8e00)

~~~json
{
  "source": "00ad8e00",
  "target": "00566a7c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8e0c`](#insn-00ad8e0c)

~~~json
{
  "source": "00ad8e0c",
  "target": "0057473c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8e10`](#insn-00ad8e10)

~~~json
{
  "source": "00ad8e10",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e14`](#insn-00ad8e14)

~~~json
{
  "source": "00ad8e14",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e18`](#insn-00ad8e18)

~~~json
{
  "source": "00ad8e18",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e24`](#insn-00ad8e24)

~~~json
{
  "source": "00ad8e24",
  "target": "00574054",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8e28`](#insn-00ad8e28)

~~~json
{
  "source": "00ad8e28",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e2c`](#insn-00ad8e2c)

~~~json
{
  "source": "00ad8e2c",
  "target": "00ad8e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e38`](#insn-00ad8e38)

~~~json
{
  "source": "00ad8e38",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8e3c`](#insn-00ad8e3c)

~~~json
{
  "source": "00ad8e3c",
  "target": "00ad8e58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e54`](#insn-00ad8e54)

~~~json
{
  "source": "00ad8e54",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8e58`](#insn-00ad8e58)

~~~json
{
  "source": "00ad8e58",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e5c`](#insn-00ad8e5c)

~~~json
{
  "source": "00ad8e5c",
  "target": "00ad8e70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e68`](#insn-00ad8e68)

~~~json
{
  "source": "00ad8e68",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8e6c`](#insn-00ad8e6c)

~~~json
{
  "source": "00ad8e6c",
  "target": "00ad8eec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e70`](#insn-00ad8e70)

~~~json
{
  "source": "00ad8e70",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e74`](#insn-00ad8e74)

~~~json
{
  "source": "00ad8e74",
  "target": "00ad8e80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e78`](#insn-00ad8e78)

~~~json
{
  "source": "00ad8e78",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e7c`](#insn-00ad8e7c)

~~~json
{
  "source": "00ad8e7c",
  "target": "00bdaf60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8e80`](#insn-00ad8e80)

~~~json
{
  "source": "00ad8e80",
  "target": "0109fe10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "0109fe10",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00ad8e84`](#insn-00ad8e84)

~~~json
{
  "source": "00ad8e84",
  "target": "00ad8f10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e98`](#insn-00ad8e98)

~~~json
{
  "source": "00ad8e98",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8e9c`](#insn-00ad8e9c)

~~~json
{
  "source": "00ad8e9c",
  "target": "00ad8ec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8ea8`](#insn-00ad8ea8)

~~~json
{
  "source": "00ad8ea8",
  "target": "00bd6d90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8eac`](#insn-00ad8eac)

~~~json
{
  "source": "00ad8eac",
  "target": "00ad8ec8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8ec4`](#insn-00ad8ec4)

~~~json
{
  "source": "00ad8ec4",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8ecc`](#insn-00ad8ecc)

~~~json
{
  "source": "00ad8ecc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8ed4`](#insn-00ad8ed4)

~~~json
{
  "source": "00ad8ed4",
  "target": "00ad8f78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8ed8`](#insn-00ad8ed8)

~~~json
{
  "source": "00ad8ed8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8edc`](#insn-00ad8edc)

~~~json
{
  "source": "00ad8edc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8ee0`](#insn-00ad8ee0)

~~~json
{
  "source": "00ad8ee0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8f00`](#insn-00ad8f00)

~~~json
{
  "source": "00ad8f00",
  "target": "00bdaf30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8f04`](#insn-00ad8f04)

~~~json
{
  "source": "00ad8f04",
  "target": "Stack[-0x88]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8f08`](#insn-00ad8f08)

~~~json
{
  "source": "00ad8f08",
  "target": "00ad8e78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8f0c`](#insn-00ad8f0c)

~~~json
{
  "source": "00ad8f0c",
  "target": "00ad8e80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8f14`](#insn-00ad8f14)

~~~json
{
  "source": "00ad8f14",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8f1c`](#insn-00ad8f1c)

~~~json
{
  "source": "00ad8f1c",
  "target": "00ad8f78",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ad8f20`](#insn-00ad8f20)

~~~json
{
  "source": "00ad8f20",
  "target": "00436e9c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ad8f78`](#insn-00ad8f78)

~~~json
{
  "source": "00ad8f78",
  "target": "00bdaf90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
