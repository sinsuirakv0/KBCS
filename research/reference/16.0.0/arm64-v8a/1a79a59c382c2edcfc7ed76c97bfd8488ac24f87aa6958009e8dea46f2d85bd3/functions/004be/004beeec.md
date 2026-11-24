# 004beeec

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `0049c054`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/0049c/0049c054.md) · 移動量 `+0x22e98`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0008.md#compare-a686a92171da76d16754d8cde23efb4d)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `004bef2c`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/004be/004bef2c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0008.md#compare-bb2201c8d8722ab5f0661058c8d97b27)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004beeec",
  "name": "_ZN5Botan8ECB_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE",
  "size": 408,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "594f6c5a40df9992454b58790f4593541135b2f15fe94fd13dc428da841f1d52",
  "source_text_sha256": "594f6c5a40df9992454b58790f4593541135b2f15fe94fd13dc428da841f1d52",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004beeec",
        "004bf07f"
      ],
      [
        "004bf1e0",
        "004bf1e3"
      ]
    ],
    "bytes_sha256": "14c68d86468407d22ca2e18056d198e352078eebc1f04eae3062ba29deb3ea23",
    "instruction_count": 102,
    "instruction_bytes": 408,
    "body_bytes": 408,
    "indirect": 4,
    "unresolved": 4
  }
}
~~~

## 呼び出し元

- [00c589b0](../00c58/00c589b0.md)

## 呼び出し先

- [004a680c](../004a6/004a680c.md)
- [00c57ae0](../00c57/00c57ae0.md)
- [00c57af0](../00c57/00c57af0.md)
- [00c57b10](../00c57/00c57b10.md)
- [00c57b60](../00c57/00c57b60.md)
- [00c57b70](../00c57/00c57b70.md)
- [00c58270](../00c58/00c58270.md)

## 関連文字列（未確認候補）

~~~text
" cannot be used with "
"/ECB"
"Padding "
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2518 bytes

~~~c

void _ZN5Botan8ECB_ModeC2EPNS_11BlockCipherEPNS_28BlockCipherModePaddingMethodE
               (long *param_1,long *param_2,long *param_3)

{
  long lVar1;
  undefined8 uVar2;
  ulong uVar3;
  undefined8 *puVar4;
  long lVar5;
  undefined1 auStack_e0 [24];
  undefined1 auStack_c8 [24];
  undefined8 local_b0;
  undefined8 uStack_a8;
  undefined8 local_a0;
  undefined8 local_90;
  undefined8 uStack_88;
  undefined8 local_80;
  undefined1 auStack_78 [24];
  undefined8 local_60;
  undefined8 uStack_58;
  undefined8 local_50;
  long local_48;
  
  lVar1 = tpidr_el0;
  local_48 = *(long *)(lVar1 + 0x28);
  *param_1 = (long)(PTR__ZTVN5Botan8ECB_ModeE_00c9aa48 + 0x10);
  param_1[1] = (long)param_2;
  lVar5 = *param_2;
  param_1[2] = (long)param_3;
  uVar2 = (**(code **)(lVar5 + 0x30))(param_2);
  uVar3 = (**(code **)(*param_3 + 0x10))(param_3,uVar2);
  if ((uVar3 & 1) == 0) {
    uVar2 = __cxa_allocate_exception(0x20);
    (**(code **)(*(long *)param_1[2] + 0x18))(auStack_c8,(long *)param_1[2]);
    puVar4 = (undefined8 *)
             _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6insertEmPKc
                       (auStack_c8,0,"Padding ");
    local_a0 = puVar4[2];
    uStack_a8 = puVar4[1];
    local_b0 = *puVar4;
    puVar4[1] = 0;
    puVar4[2] = 0;
    *puVar4 = 0;
    puVar4 = (undefined8 *)
             _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
                       (&local_b0," cannot be used with ");
    local_80 = puVar4[2];
    uStack_88 = puVar4[1];
    local_90 = *puVar4;
    puVar4[1] = 0;
    puVar4[2] = 0;
    *puVar4 = 0;
    (**(code **)(*param_2 + 0x20))(auStack_e0,param_2);
    FUN_004a680c(auStack_78,&local_90,auStack_e0);
    puVar4 = (undefined8 *)
             _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6appendEPKc
                       (auStack_78,&DAT_002bb350);
    local_50 = puVar4[2];
    uStack_58 = puVar4[1];
    local_60 = *puVar4;
    puVar4[1] = 0;
    puVar4[2] = 0;
    *puVar4 = 0;
    _ZN5Botan16Invalid_ArgumentC2ERKNSt6__ndk112basic_stringIcNS1_11char_traitsIcEENS1_9allocatorIcEEEE
              (uVar2,&local_60);
    if (*(long *)(lVar1 + 0x28) == local_48) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar2,PTR__ZTIN5Botan16Invalid_ArgumentE_00c9a930,FUN_00535828);
    }
  }
  else if (*(long *)(lVar1 + 0x28) == local_48) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004beeec"></a> `004beeec` | `ff 83 03 d1` | sub sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-004beef0"></a> `004beef0` | `fd 7b 0a a9` | stp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004beef4"></a> `004beef4` | `f7 5b 00 f9` | str x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004beef8"></a> `004beef8` | `f6 57 0c a9` | stp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004beefc"></a> `004beefc` | `f4 4f 0d a9` | stp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004bef00"></a> `004bef00` | `fd 83 02 91` | add x29,sp,#0xa0 | `FALL_THROUGH`
<a id="insn-004bef04"></a> `004bef04` | `56 d0 3b d5` | mrs x22,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004bef08"></a> `004bef08` | `e9 3e 00 90` | adrp x9,0xc9a000 | `FALL_THROUGH`
<a id="insn-004bef0c"></a> `004bef0c` | `f4 03 02 aa` | mov x20,x2 | `FALL_THROUGH`
<a id="insn-004bef10"></a> `004bef10` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004bef14"></a> `004bef14` | `29 25 45 f9` | ldr x9,[x9, #0xa48] | `FALL_THROUGH`
<a id="insn-004bef18"></a> `004bef18` | `f5 03 01 aa` | mov x21,x1 | `FALL_THROUGH`
<a id="insn-004bef1c"></a> `004bef1c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004bef20"></a> `004bef20` | `29 41 00 91` | add x9,x9,#0x10 | `FALL_THROUGH`
<a id="insn-004bef24"></a> `004bef24` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bef28"></a> `004bef28` | `09 04 00 a9` | stp x9,x1,[x0] | `FALL_THROUGH`
<a id="insn-004bef2c"></a> `004bef2c` | `28 00 40 f9` | ldr x8,[x1] | `FALL_THROUGH`
<a id="insn-004bef30"></a> `004bef30` | `02 08 00 f9` | str x2,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004bef34"></a> `004bef34` | `08 19 40 f9` | ldr x8,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-004bef38"></a> `004bef38` | `e0 03 01 aa` | mov x0,x1 | `FALL_THROUGH`
<a id="insn-004bef3c"></a> `004bef3c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004bef40"></a> `004bef40` | `e1 03 00 aa` | mov x1,x0 | `FALL_THROUGH`
<a id="insn-004bef44"></a> `004bef44` | `88 02 40 f9` | ldr x8,[x20] | `FALL_THROUGH`
<a id="insn-004bef48"></a> `004bef48` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-004bef4c"></a> `004bef4c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004bef50"></a> `004bef50` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-004bef54"></a> `004bef54` | `60 01 00 36` | tbz w0,#0x0,0x004bef80 | `CONDITIONAL_JUMP`
<a id="insn-004bef58"></a> `004bef58` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004bef5c"></a> `004bef5c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bef60"></a> `004bef60` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bef64"></a> `004bef64` | `e1 13 00 54` | b.ne 0x004bf1e0 | `CONDITIONAL_JUMP`
<a id="insn-004bef68"></a> `004bef68` | `f4 4f 4d a9` | ldp x20,x19,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-004bef6c"></a> `004bef6c` | `f7 5b 40 f9` | ldr x23,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-004bef70"></a> `004bef70` | `f6 57 4c a9` | ldp x22,x21,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-004bef74"></a> `004bef74` | `fd 7b 4a a9` | ldp x29,x30,[sp, #0xa0] | `FALL_THROUGH`
<a id="insn-004bef78"></a> `004bef78` | `ff 83 03 91` | add sp,sp,#0xe0 | `FALL_THROUGH`
<a id="insn-004bef7c"></a> `004bef7c` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004bef80"></a> `004bef80` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-004bef84"></a> `004bef84` | `db 62 1e 94` | bl 0x00c57af0 | `UNCONDITIONAL_CALL`
<a id="insn-004bef88"></a> `004bef88` | `69 0a 40 f9` | ldr x9,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-004bef8c"></a> `004bef8c` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-004bef90"></a> `004bef90` | `28 01 40 f9` | ldr x8,[x9] | `FALL_THROUGH`
<a id="insn-004bef94"></a> `004bef94` | `0a 0d 40 f9` | ldr x10,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-004bef98"></a> `004bef98` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-004bef9c"></a> `004bef9c` | `e0 03 09 aa` | mov x0,x9 | `FALL_THROUGH`
<a id="insn-004befa0"></a> `004befa0` | `40 01 3f d6` | blr x10 | `COMPUTED_CALL`
<a id="insn-004befa4"></a> `004befa4` | `e2 ef ff b0` | adrp x2,0x2bb000 | `FALL_THROUGH`
<a id="insn-004befa8"></a> `004befa8` | `42 1c 0d 91` | add x2,x2,#0x347 | `FALL_THROUGH`
<a id="insn-004befac"></a> `004befac` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-004befb0"></a> `004befb0` | `e1 03 1f aa` | mov x1,xzr | `FALL_THROUGH`
<a id="insn-004befb4"></a> `004befb4` | `eb 62 1e 94` | bl 0x00c57b60 | `UNCONDITIONAL_CALL`
<a id="insn-004befb8"></a> `004befb8` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004befbc"></a> `004befbc` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-004befc0"></a> `004befc0` | `e8 23 00 f9` | str x8,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004befc4"></a> `004befc4` | `e0 0f 80 3d` | str q0,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004befc8"></a> `004befc8` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004befcc"></a> `004befcc` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-004befd0"></a> `004befd0` | `41 ef ff f0` | adrp x1,0x2a9000 | `FALL_THROUGH`
<a id="insn-004befd4"></a> `004befd4` | `21 f8 2a 91` | add x1,x1,#0xabe | `FALL_THROUGH`
<a id="insn-004befd8"></a> `004befd8` | `e0 c3 00 91` | add x0,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004befdc"></a> `004befdc` | `e5 62 1e 94` | bl 0x00c57b70 | `UNCONDITIONAL_CALL`
<a id="insn-004befe0"></a> `004befe0` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004befe4"></a> `004befe4` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-004befe8"></a> `004befe8` | `e8 33 00 f9` | str x8,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-004befec"></a> `004befec` | `e0 17 80 3d` | str q0,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004beff0"></a> `004beff0` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004beff4"></a> `004beff4` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-004beff8"></a> `004beff8` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-004beffc"></a> `004beffc` | `09 11 40 f9` | ldr x9,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-004bf000"></a> `004bf000` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-004bf004"></a> `004bf004` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-004bf008"></a> `004bf008` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-004bf00c"></a> `004bf00c` | `a8 e3 00 d1` | sub x8,x29,#0x38 | `FALL_THROUGH`
<a id="insn-004bf010"></a> `004bf010` | `e0 43 01 91` | add x0,sp,#0x50 | `FALL_THROUGH`
<a id="insn-004bf014"></a> `004bf014` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-004bf018"></a> `004bf018` | `fd 9d ff 97` | bl 0x004a680c | `UNCONDITIONAL_CALL`
<a id="insn-004bf01c"></a> `004bf01c` | `e1 ef ff 90` | adrp x1,0x2bb000 | `FALL_THROUGH`
<a id="insn-004bf020"></a> `004bf020` | `21 40 0d 91` | add x1,x1,#0x350 | `FALL_THROUGH`
<a id="insn-004bf024"></a> `004bf024` | `a0 e3 00 d1` | sub x0,x29,#0x38 | `FALL_THROUGH`
<a id="insn-004bf028"></a> `004bf028` | `d2 62 1e 94` | bl 0x00c57b70 | `UNCONDITIONAL_CALL`
<a id="insn-004bf02c"></a> `004bf02c` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004bf030"></a> `004bf030` | `00 00 c0 3d` | ldr q0,[x0] | `FALL_THROUGH`
<a id="insn-004bf034"></a> `004bf034` | `37 00 80 52` | mov w23,#0x1 | `FALL_THROUGH`
<a id="insn-004bf038"></a> `004bf038` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004bf03c"></a> `004bf03c` | `a0 03 9e 3c` | stur q0,[x29, #-0x20] | `FALL_THROUGH`
<a id="insn-004bf040"></a> `004bf040` | `1f fc 00 a9` | stp xzr,xzr,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004bf044"></a> `004bf044` | `1f 00 00 f9` | str xzr,[x0] | `FALL_THROUGH`
<a id="insn-004bf048"></a> `004bf048` | `a1 83 00 d1` | sub x1,x29,#0x20 | `FALL_THROUGH`
<a id="insn-004bf04c"></a> `004bf04c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004bf050"></a> `004bf050` | `88 64 1e 94` | bl 0x00c58270 | `UNCONDITIONAL_CALL`
<a id="insn-004bf054"></a> `004bf054` | `c8 16 40 f9` | ldr x8,[x22, #0x28] | `FALL_THROUGH`
<a id="insn-004bf058"></a> `004bf058` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004bf05c"></a> `004bf05c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004bf060"></a> `004bf060` | `01 0c 00 54` | b.ne 0x004bf1e0 | `CONDITIONAL_JUMP`
<a id="insn-004bf064"></a> `004bf064` | `c1 3e 00 f0` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-004bf068"></a> `004bf068` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004bf06c"></a> `004bf06c` | `e2 3d 3b 10` | adr x2,0x535828 | `FALL_THROUGH`
<a id="insn-004bf070"></a> `004bf070` | `21 98 44 f9` | ldr x1,[x1, #0x930] | `FALL_THROUGH`
<a id="insn-004bf074"></a> `004bf074` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-004bf078"></a> `004bf078` | `f7 03 1f 2a` | mov w23,wzr | `FALL_THROUGH`
<a id="insn-004bf07c"></a> `004bf07c` | `a5 62 1e 94` | bl 0x00c57b10 | `CALL_TERMINATOR`
<a id="insn-004bf1e0"></a> `004bf1e0` | `40 62 1e 94` | bl 0x00c57ae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004beeec`](#insn-004beeec) 範囲 `[['004beeec', '004bef57']]`
  - `CONDITIONAL_JUMP` [`004bef54`](#insn-004bef54) → [`004bef80`](#insn-004bef80)
  - `FALL_THROUGH` [`004bef54`](#insn-004bef54) → [`004bef58`](#insn-004bef58)
- ブロック [`004bef58`](#insn-004bef58) 範囲 `[['004bef58', '004bef67']]`
  - `CONDITIONAL_JUMP` [`004bef64`](#insn-004bef64) → [`004bf1e0`](#insn-004bf1e0)
  - `FALL_THROUGH` [`004bef64`](#insn-004bef64) → [`004bef68`](#insn-004bef68)
- ブロック [`004bef68`](#insn-004bef68) 範囲 `[['004bef68', '004bef7f']]`
- ブロック [`004bef80`](#insn-004bef80) 範囲 `[['004bef80', '004bf063']]`
  - `CONDITIONAL_JUMP` [`004bf060`](#insn-004bf060) → [`004bf1e0`](#insn-004bf1e0)
  - `FALL_THROUGH` [`004bf060`](#insn-004bf060) → [`004bf064`](#insn-004bf064)
- ブロック [`004bf064`](#insn-004bf064) 範囲 `[['004bf064', '004bf07f']]`
- ブロック [`004bf1e0`](#insn-004bf1e0) 範囲 `[['004bf1e0', '004bf1e3']]`

## 命令位置別の参照

- [`004beef0`](#insn-004beef0) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004beef4`](#insn-004beef4) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004beef8`](#insn-004beef8) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004beefc`](#insn-004beefc) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef14`](#insn-004bef14) → `00c9aa48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004bef24`](#insn-004bef24) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef28`](#insn-004bef28) → `00c660d8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[160]`
- [`004bef54`](#insn-004bef54) → [`004bef80`](#insn-004bef80) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef5c`](#insn-004bef5c) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef64`](#insn-004bef64) → [`004bf1e0`](#insn-004bf1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef68`](#insn-004bef68) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef6c`](#insn-004bef6c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef70`](#insn-004bef70) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef74`](#insn-004bef74) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bef84`](#insn-004bef84) → [`00c57af0`](../00c57/00c57af0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57af0` · 推定シンボル `None` · 推定型 `None`
- [`004befa8`](#insn-004befa8) → `002bb347`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004befb4`](#insn-004befb4) → [`00c57b60`](../00c57/00c57b60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b60` · 推定シンボル `None` · 推定型 `None`
- [`004befc0`](#insn-004befc0) → `Stack[-0xa0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004befc4`](#insn-004befc4) → `Stack[-0xb0]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004befd4`](#insn-004befd4) → `002a9abe`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004befdc`](#insn-004befdc) → [`00c57b70`](../00c57/00c57b70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b70` · 推定シンボル `None` · 推定型 `None`
- [`004befe8`](#insn-004befe8) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004befec`](#insn-004befec) → `Stack[-0x90]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bf018`](#insn-004bf018) → [`004a680c`](../004a6/004a680c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004a680c` · 推定シンボル `None` · 推定型 `None`
- [`004bf020`](#insn-004bf020) → `002bb350`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bf028`](#insn-004bf028) → [`00c57b70`](../00c57/00c57b70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b70` · 推定シンボル `None` · 推定型 `None`
- [`004bf038`](#insn-004bf038) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bf03c`](#insn-004bf03c) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bf050`](#insn-004bf050) → [`00c58270`](../00c58/00c58270.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58270` · 推定シンボル `None` · 推定型 `None`
- [`004bf058`](#insn-004bf058) → `Stack[-0x48]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bf060`](#insn-004bf060) → [`004bf1e0`](#insn-004bf1e0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004bf06c`](#insn-004bf06c) → [`00535828`](../00535/00535828.md) · `PARAM` · `ANALYSIS` · 関数 `00535828` · 推定シンボル `None` · 推定型 `None`
- [`004bf070`](#insn-004bf070) → `00c9a930`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004bf070`](#insn-004bf070) → `00c65ea8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN5Botan16Invalid_ArgumentE` · 推定型 `pointer __((offset(0x10)))`
- [`004bf07c`](#insn-004bf07c) → [`00c57b10`](../00c57/00c57b10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57b10` · 推定シンボル `None` · 推定型 `None`
- [`004bf1e0`](#insn-004bf1e0) → [`00c57ae0`](../00c57/00c57ae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004beef0`](#insn-004beef0)

~~~json
{
  "source": "004beef0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004beef4`](#insn-004beef4)

~~~json
{
  "source": "004beef4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004beef8`](#insn-004beef8)

~~~json
{
  "source": "004beef8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004beefc`](#insn-004beefc)

~~~json
{
  "source": "004beefc",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef14`](#insn-004bef14)

~~~json
{
  "source": "004bef14",
  "target": "00c9aa48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9aa48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004bef24`](#insn-004bef24)

~~~json
{
  "source": "004bef24",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef28`](#insn-004bef28)

~~~json
{
  "source": "004bef28",
  "target": "00c660d8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c660c8",
  "offset": 16,
  "size": 160,
  "datatype": "undefined1[160]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004bef54`](#insn-004bef54)

~~~json
{
  "source": "004bef54",
  "target": "004bef80",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef5c`](#insn-004bef5c)

~~~json
{
  "source": "004bef5c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef64`](#insn-004bef64)

~~~json
{
  "source": "004bef64",
  "target": "004bf1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef68`](#insn-004bef68)

~~~json
{
  "source": "004bef68",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef6c`](#insn-004bef6c)

~~~json
{
  "source": "004bef6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef70`](#insn-004bef70)

~~~json
{
  "source": "004bef70",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef74`](#insn-004bef74)

~~~json
{
  "source": "004bef74",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bef84`](#insn-004bef84)

~~~json
{
  "source": "004bef84",
  "target": "00c57af0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004befa8`](#insn-004befa8)

~~~json
{
  "source": "004befa8",
  "target": "002bb347",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002bb347",
  "offset": 0,
  "size": 9,
  "datatype": "string",
  "bytes": "50616464696e672000",
  "capture_start": "002bb347",
  "capture_bytes": 9,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004befb4`](#insn-004befb4)

~~~json
{
  "source": "004befb4",
  "target": "00c57b60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004befc0`](#insn-004befc0)

~~~json
{
  "source": "004befc0",
  "target": "Stack[-0xa0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004befc4`](#insn-004befc4)

~~~json
{
  "source": "004befc4",
  "target": "Stack[-0xb0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004befd4`](#insn-004befd4)

~~~json
{
  "source": "004befd4",
  "target": "002a9abe",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a9abe",
  "offset": 0,
  "size": 22,
  "datatype": "string",
  "bytes": "2063616e6e6f74206265207573656420776974682000",
  "capture_start": "002a9abe",
  "capture_bytes": 22,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004befdc`](#insn-004befdc)

~~~json
{
  "source": "004befdc",
  "target": "00c57b70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004befe8`](#insn-004befe8)

~~~json
{
  "source": "004befe8",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004befec`](#insn-004befec)

~~~json
{
  "source": "004befec",
  "target": "Stack[-0x90]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bf018`](#insn-004bf018)

~~~json
{
  "source": "004bf018",
  "target": "004a680c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bf020`](#insn-004bf020)

~~~json
{
  "source": "004bf020",
  "target": "002bb350",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bf028`](#insn-004bf028)

~~~json
{
  "source": "004bf028",
  "target": "00c57b70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bf038`](#insn-004bf038)

~~~json
{
  "source": "004bf038",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bf03c`](#insn-004bf03c)

~~~json
{
  "source": "004bf03c",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bf050`](#insn-004bf050)

~~~json
{
  "source": "004bf050",
  "target": "00c58270",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bf058`](#insn-004bf058)

~~~json
{
  "source": "004bf058",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bf060`](#insn-004bf060)

~~~json
{
  "source": "004bf060",
  "target": "004bf1e0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004bf06c`](#insn-004bf06c)

~~~json
{
  "source": "004bf06c",
  "target": "00535828",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bf070`](#insn-004bf070)

~~~json
{
  "source": "004bf070",
  "target": "00c9a930",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9a930",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004bf070`](#insn-004bf070)

~~~json
{
  "source": "004bf070",
  "target": "00c65ea8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c65ea8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004bf07c`](#insn-004bf07c)

~~~json
{
  "source": "004bf07c",
  "target": "00c57b10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004bf1e0`](#insn-004bf1e0)

~~~json
{
  "source": "004bf1e0",
  "target": "00c57ae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
