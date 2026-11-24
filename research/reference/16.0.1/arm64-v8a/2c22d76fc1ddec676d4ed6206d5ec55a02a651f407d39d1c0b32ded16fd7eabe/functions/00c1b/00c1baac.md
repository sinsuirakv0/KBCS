# 00c1baac

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00c1b684`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00c1b/00c1b684.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/high-0010.md#compare-6ca2cc9d4d3c9aafbc9098dfab203e82)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00c1bb48`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00c1b/00c1bb48.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/high-0011.md#compare-37a017b35c9012fc9772957077d4c152)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00c1baac",
  "name": "_ZNSt6__ndk111__money_putIcE13__gather_infoEbbRKNS_6localeERNS_10money_base7patternERcS8_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEESF_SF_Ri",
  "size": 532,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "6ced324615398db8ce2e96dbd947e1dc3f0d04cfb2fc25e4396eb1085049d7cc",
  "source_text_sha256": "6ced324615398db8ce2e96dbd947e1dc3f0d04cfb2fc25e4396eb1085049d7cc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00c1baac",
        "00c1bcbf"
      ]
    ],
    "bytes_sha256": "ecf3be1167f911e7685a4ec99fb305cdb4a58c786251af512118b7beeb016e1c",
    "instruction_count": 133,
    "instruction_bytes": 532,
    "body_bytes": 532,
    "indirect": 8,
    "unresolved": 8
  }
}
~~~

## 呼び出し元

- [00c5e6e0](../00c5e/00c5e6e0.md)

## 呼び出し先

- [00c05f58](../00c05/00c05f58.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c5dee0](../00c5d/00c5dee0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3602 bytes

~~~c

void _ZNSt6__ndk111__money_putIcE13__gather_infoEbbRKNS_6localeERNS_10money_base7patternERcS8_RNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEESF_SF_Ri
               (ulong param_1,ulong param_2,long *param_3,undefined4 *param_4,undefined1 *param_5,
               undefined1 *param_6,byte *param_7,byte *param_8,byte *param_9,undefined4 *param_10)

{
  undefined *puVar1;
  undefined1 uVar2;
  undefined4 uVar3;
  long lVar4;
  code *pcVar5;
  long lVar6;
  long *plVar7;
  undefined **local_80;
  undefined8 uStack_78;
  undefined8 local_70;
  undefined *local_68;
  undefined ***local_48;
  
                    /* try { // try from 00c1babc to 00d1bacf has its CatchHandler @ 00c1d0ec */
  lVar6 = *param_3;
  if ((param_1 & 1) == 0) {
    lVar4 = *(long *)PTR__ZNSt6__ndk110moneypunctIcLb0EE2idE_00c9bbe0;
    puVar1 = PTR__ZNSt6__ndk110moneypunctIcLb0EE2idE_00c9bbe0;
  }
  else {
    lVar4 = *(long *)PTR__ZNSt6__ndk110moneypunctIcLb1EE2idE_00c9bbd8;
    puVar1 = PTR__ZNSt6__ndk110moneypunctIcLb1EE2idE_00c9bbd8;
  }
  local_68 = puVar1;
  if (lVar4 != -1) {
    local_48 = &local_80;
    local_80 = &local_68;
    _ZNSt6__ndk111__call_onceERVmPvPFvS2_E(puVar1,&local_48,FUN_00c35fb8);
  }
  lVar4 = *(long *)(lVar6 + 0x10);
  if (((long)*(int *)(puVar1 + 8) - 1U < (ulong)(*(long *)(lVar6 + 0x18) - lVar4 >> 3)) &&
     (plVar7 = *(long **)(lVar4 + ((long)*(int *)(puVar1 + 8) - 1U) * 8), plVar7 != (long *)0x0)) {
    if ((param_2 & 1) == 0) {
                    /* try { // try from 00c1bbb4 to 00d1bbbb has its CatchHandler @ 00c1d1e4 */
      uVar3 = (**(code **)(*plVar7 + 0x50))(plVar7);
      *param_4 = uVar3;
                    /* try { // try from 00c1bbbc to 00d1bbc3 has its CatchHandler @ 00c1d0e8 */
      pcVar5 = *(code **)(*plVar7 + 0x38);
    }
    else {
                    /* try { // try from 00c1bb90 to 00d1bb9f has its CatchHandler @ 00c1d2e8 */
      uVar3 = (**(code **)(*plVar7 + 0x58))(plVar7);
      *param_4 = uVar3;
      pcVar5 = *(code **)(*plVar7 + 0x40);
    }
    (*pcVar5)(&local_80,plVar7);
    if ((*param_9 & 1) != 0) {
      _ZdlPv(*(void **)(param_9 + 0x10));
    }
    *(undefined8 *)(param_9 + 8) = uStack_78;
    *(undefined ***)param_9 = local_80;
    *(undefined8 *)(param_9 + 0x10) = local_70;
    uVar2 = (**(code **)(*plVar7 + 0x18))(plVar7);
                    /* try { // try from 00c1bc00 to 00d1bc0b has its CatchHandler @ 00c1d0e4 */
    *param_5 = uVar2;
                    /* try { // try from 00c1bc0c to 00d1bc1b has its CatchHandler @ 00c1d0d0 */
    uVar2 = (**(code **)(*plVar7 + 0x20))(plVar7);
    *param_6 = uVar2;
                    /* try { // try from 00c1bc1c to 00d1bc2f has its CatchHandler @ 00c1d0b8 */
    (**(code **)(*plVar7 + 0x28))(&local_80,plVar7);
    if ((*param_7 & 1) != 0) {
      _ZdlPv(*(void **)(param_7 + 0x10));
    }
    *(undefined8 *)(param_7 + 8) = uStack_78;
    *(undefined ***)param_7 = local_80;
    *(undefined8 *)(param_7 + 0x10) = local_70;
    (**(code **)(*plVar7 + 0x30))(&local_80,plVar7);
    if ((*param_8 & 1) != 0) {
                    /* try { // try from 00c1bc68 to 00d1bc73 has its CatchHandler @ 00c1d1e4 */
      _ZdlPv(*(void **)(param_8 + 0x10));
    }
                    /* try { // try from 00c1bc74 to 00d1bd4f has its CatchHandler @ 00c1d198 */
    *(undefined8 *)(param_8 + 8) = uStack_78;
    *(undefined ***)param_8 = local_80;
    *(undefined8 *)(param_8 + 0x10) = local_70;
    uVar3 = (**(code **)(*plVar7 + 0x48))(plVar7);
    *param_10 = uVar3;
    return;
  }
                    /* WARNING: Subroutine does not return */
  FUN_00c05f58();
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00c1baac"></a> `00c1baac` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00c1bab0"></a> `00c1bab0` | `ff 03 02 d1` | sub sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00c1bab4"></a> `00c1bab4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c1bab8"></a> `00c1bab8` | `fb 1b 00 f9` | str x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c1babc"></a> `00c1babc` | `fa 67 04 a9` | stp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c1bac0"></a> `00c1bac0` | `f8 5f 05 a9` | stp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c1bac4"></a> `00c1bac4` | `f6 57 06 a9` | stp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00c1bac8"></a> `00c1bac8` | `f4 4f 07 a9` | stp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00c1bacc"></a> `00c1bacc` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00c1bad0"></a> `00c1bad0` | `ba 33 40 f9` | ldr x26,[x29, #0x60] | `FALL_THROUGH`
<a id="insn-00c1bad4"></a> `00c1bad4` | `55 00 40 f9` | ldr x21,[x2] | `FALL_THROUGH`
<a id="insn-00c1bad8"></a> `00c1bad8` | `f3 03 07 aa` | mov x19,x7 | `FALL_THROUGH`
<a id="insn-00c1badc"></a> `00c1badc` | `f4 03 06 aa` | mov x20,x6 | `FALL_THROUGH`
<a id="insn-00c1bae0"></a> `00c1bae0` | `f6 03 05 aa` | mov x22,x5 | `FALL_THROUGH`
<a id="insn-00c1bae4"></a> `00c1bae4` | `f7 03 04 aa` | mov x23,x4 | `FALL_THROUGH`
<a id="insn-00c1bae8"></a> `00c1bae8` | `f8 03 03 aa` | mov x24,x3 | `FALL_THROUGH`
<a id="insn-00c1baec"></a> `00c1baec` | `f9 03 01 2a` | mov w25,w1 | `FALL_THROUGH`
<a id="insn-00c1baf0"></a> `00c1baf0` | `c0 01 00 36` | tbz w0,#0x0,0x00c1bb28 | `CONDITIONAL_JUMP`
<a id="insn-00c1baf4"></a> `00c1baf4` | `1b 04 00 90` | adrp x27,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c1baf8"></a> `00c1baf8` | `7b ef 45 f9` | ldr x27,[x27, #0xbd8] | `FALL_THROUGH`
<a id="insn-00c1bafc"></a> `00c1bafc` | `bb 83 1f f8` | stur x27,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00c1bb00"></a> `00c1bb00` | `68 ff df c8` | ldar x8,[x27] | `FALL_THROUGH`
<a id="insn-00c1bb04"></a> `00c1bb04` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1bb08"></a> `00c1bb08` | `00 03 00 54` | b.eq 0x00c1bb68 | `CONDITIONAL_JUMP`
<a id="insn-00c1bb0c"></a> `00c1bb0c` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00c1bb10"></a> `00c1bb10` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-00c1bb14"></a> `00c1bb14` | `00 04 00 90` | adrp x0,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c1bb18"></a> `00c1bb18` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00c1bb1c"></a> `00c1bb1c` | `a9 0f 00 f9` | str x9,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00c1bb20"></a> `00c1bb20` | `00 ec 45 f9` | ldr x0,[x0, #0xbd8] | `FALL_THROUGH`
<a id="insn-00c1bb24"></a> `00c1bb24` | `0d 00 00 14` | b 0x00c1bb58 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1bb28"></a> `00c1bb28` | `1b 04 00 90` | adrp x27,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c1bb2c"></a> `00c1bb2c` | `7b f3 45 f9` | ldr x27,[x27, #0xbe0] | `FALL_THROUGH`
<a id="insn-00c1bb30"></a> `00c1bb30` | `bb 83 1f f8` | stur x27,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00c1bb34"></a> `00c1bb34` | `68 ff df c8` | ldar x8,[x27] | `FALL_THROUGH`
<a id="insn-00c1bb38"></a> `00c1bb38` | `1f 05 00 b1` | cmn x8,#0x1 | `FALL_THROUGH`
<a id="insn-00c1bb3c"></a> `00c1bb3c` | `60 01 00 54` | b.eq 0x00c1bb68 | `CONDITIONAL_JUMP`
<a id="insn-00c1bb40"></a> `00c1bb40` | `a8 23 00 d1` | sub x8,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00c1bb44"></a> `00c1bb44` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-00c1bb48"></a> `00c1bb48` | `00 04 00 90` | adrp x0,0xc9b000 | `FALL_THROUGH`
<a id="insn-00c1bb4c"></a> `00c1bb4c` | `e8 03 00 f9` | str x8,[sp] | `FALL_THROUGH`
<a id="insn-00c1bb50"></a> `00c1bb50` | `a9 0f 00 f9` | str x9,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00c1bb54"></a> `00c1bb54` | `00 f0 45 f9` | ldr x0,[x0, #0xbe0] | `FALL_THROUGH`
<a id="insn-00c1bb58"></a> `00c1bb58` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-00c1bb5c"></a> `00c1bb5c` | `e2 22 0d 10` | adr x2,0xc35fb8 | `FALL_THROUGH`
<a id="insn-00c1bb60"></a> `00c1bb60` | `a1 63 00 91` | add x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00c1bb64"></a> `00c1bb64` | `df 08 01 94` | bl 0x00c5dee0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1bb68"></a> `00c1bb68` | `a8 2a 41 a9` | ldp x8,x10,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00c1bb6c"></a> `00c1bb6c` | `69 0b 80 b9` | ldrsw x9,[x27, #0x8] | `FALL_THROUGH`
<a id="insn-00c1bb70"></a> `00c1bb70` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00c1bb74"></a> `00c1bb74` | `4a 01 08 cb` | sub x10,x10,x8 | `FALL_THROUGH`
<a id="insn-00c1bb78"></a> `00c1bb78` | `3f 0d 8a eb` | cmp x9,x10, ASR #0x3 | `FALL_THROUGH`
<a id="insn-00c1bb7c"></a> `00c1bb7c` | `02 0a 00 54` | b.cs 0x00c1bcbc | `CONDITIONAL_JUMP`
<a id="insn-00c1bb80"></a> `00c1bb80` | `15 79 69 f8` | ldr x21,[x8, x9, LSL #0x3] | `FALL_THROUGH`
<a id="insn-00c1bb84"></a> `00c1bb84` | `d5 09 00 b4` | cbz x21,0x00c1bcbc | `CONDITIONAL_JUMP`
<a id="insn-00c1bb88"></a> `00c1bb88` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c1bb8c"></a> `00c1bb8c` | `19 01 00 36` | tbz w25,#0x0,0x00c1bbac | `CONDITIONAL_JUMP`
<a id="insn-00c1bb90"></a> `00c1bb90` | `08 2d 40 f9` | ldr x8,[x8, #0x58] | `FALL_THROUGH`
<a id="insn-00c1bb94"></a> `00c1bb94` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c1bb98"></a> `00c1bb98` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c1bb9c"></a> `00c1bb9c` | `00 03 00 b9` | str w0,[x24] | `FALL_THROUGH`
<a id="insn-00c1bba0"></a> `00c1bba0` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c1bba4"></a> `00c1bba4` | `09 21 40 f9` | ldr x9,[x8, #0x40] | `FALL_THROUGH`
<a id="insn-00c1bba8"></a> `00c1bba8` | `07 00 00 14` | b 0x00c1bbc4 | `UNCONDITIONAL_JUMP`
<a id="insn-00c1bbac"></a> `00c1bbac` | `08 29 40 f9` | ldr x8,[x8, #0x50] | `FALL_THROUGH`
<a id="insn-00c1bbb0"></a> `00c1bbb0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c1bbb4"></a> `00c1bbb4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c1bbb8"></a> `00c1bbb8` | `00 03 00 b9` | str w0,[x24] | `FALL_THROUGH`
<a id="insn-00c1bbbc"></a> `00c1bbbc` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c1bbc0"></a> `00c1bbc0` | `09 1d 40 f9` | ldr x9,[x8, #0x38] | `FALL_THROUGH`
<a id="insn-00c1bbc4"></a> `00c1bbc4` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00c1bbc8"></a> `00c1bbc8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c1bbcc"></a> `00c1bbcc` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00c1bbd0"></a> `00c1bbd0` | `48 03 40 39` | ldrb w8,[x26] | `FALL_THROUGH`
<a id="insn-00c1bbd4"></a> `00c1bbd4` | `68 00 00 36` | tbz w8,#0x0,0x00c1bbe0 | `CONDITIONAL_JUMP`
<a id="insn-00c1bbd8"></a> `00c1bbd8` | `40 0b 40 f9` | ldr x0,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00c1bbdc"></a> `00c1bbdc` | `b5 f0 00 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1bbe0"></a> `00c1bbe0` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00c1bbe4"></a> `00c1bbe4` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c1bbe8"></a> `00c1bbe8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c1bbec"></a> `00c1bbec` | `40 03 80 3d` | str q0,[x26] | `FALL_THROUGH`
<a id="insn-00c1bbf0"></a> `00c1bbf0` | `48 0b 00 f9` | str x8,[x26, #0x10] | `FALL_THROUGH`
<a id="insn-00c1bbf4"></a> `00c1bbf4` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c1bbf8"></a> `00c1bbf8` | `08 0d 40 f9` | ldr x8,[x8, #0x18] | `FALL_THROUGH`
<a id="insn-00c1bbfc"></a> `00c1bbfc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c1bc00"></a> `00c1bc00` | `e0 02 00 39` | strb w0,[x23] | `FALL_THROUGH`
<a id="insn-00c1bc04"></a> `00c1bc04` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c1bc08"></a> `00c1bc08` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c1bc0c"></a> `00c1bc0c` | `08 11 40 f9` | ldr x8,[x8, #0x20] | `FALL_THROUGH`
<a id="insn-00c1bc10"></a> `00c1bc10` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c1bc14"></a> `00c1bc14` | `c0 02 00 39` | strb w0,[x22] | `FALL_THROUGH`
<a id="insn-00c1bc18"></a> `00c1bc18` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c1bc1c"></a> `00c1bc1c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c1bc20"></a> `00c1bc20` | `09 15 40 f9` | ldr x9,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-00c1bc24"></a> `00c1bc24` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00c1bc28"></a> `00c1bc28` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00c1bc2c"></a> `00c1bc2c` | `88 02 40 39` | ldrb w8,[x20] | `FALL_THROUGH`
<a id="insn-00c1bc30"></a> `00c1bc30` | `68 00 00 36` | tbz w8,#0x0,0x00c1bc3c | `CONDITIONAL_JUMP`
<a id="insn-00c1bc34"></a> `00c1bc34` | `80 0a 40 f9` | ldr x0,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00c1bc38"></a> `00c1bc38` | `9e f0 00 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1bc3c"></a> `00c1bc3c` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00c1bc40"></a> `00c1bc40` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c1bc44"></a> `00c1bc44` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c1bc48"></a> `00c1bc48` | `80 02 80 3d` | str q0,[x20] | `FALL_THROUGH`
<a id="insn-00c1bc4c"></a> `00c1bc4c` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00c1bc50"></a> `00c1bc50` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c1bc54"></a> `00c1bc54` | `09 19 40 f9` | ldr x9,[x8, #0x30] | `FALL_THROUGH`
<a id="insn-00c1bc58"></a> `00c1bc58` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00c1bc5c"></a> `00c1bc5c` | `20 01 3f d6` | blr x9 | `COMPUTED_CALL`
<a id="insn-00c1bc60"></a> `00c1bc60` | `68 02 40 39` | ldrb w8,[x19] | `FALL_THROUGH`
<a id="insn-00c1bc64"></a> `00c1bc64` | `68 00 00 36` | tbz w8,#0x0,0x00c1bc70 | `CONDITIONAL_JUMP`
<a id="insn-00c1bc68"></a> `00c1bc68` | `60 0a 40 f9` | ldr x0,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c1bc6c"></a> `00c1bc6c` | `91 f0 00 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-00c1bc70"></a> `00c1bc70` | `e0 03 c0 3d` | ldr q0,[sp] | `FALL_THROUGH`
<a id="insn-00c1bc74"></a> `00c1bc74` | `e8 0b 40 f9` | ldr x8,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00c1bc78"></a> `00c1bc78` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00c1bc7c"></a> `00c1bc7c` | `60 02 80 3d` | str q0,[x19] | `FALL_THROUGH`
<a id="insn-00c1bc80"></a> `00c1bc80` | `68 0a 00 f9` | str x8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00c1bc84"></a> `00c1bc84` | `b3 37 40 f9` | ldr x19,[x29, #0x68] | `FALL_THROUGH`
<a id="insn-00c1bc88"></a> `00c1bc88` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00c1bc8c"></a> `00c1bc8c` | `08 25 40 f9` | ldr x8,[x8, #0x48] | `FALL_THROUGH`
<a id="insn-00c1bc90"></a> `00c1bc90` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00c1bc94"></a> `00c1bc94` | `60 02 00 b9` | str w0,[x19] | `FALL_THROUGH`
<a id="insn-00c1bc98"></a> `00c1bc98` | `f4 4f 47 a9` | ldp x20,x19,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-00c1bc9c"></a> `00c1bc9c` | `fb 1b 40 f9` | ldr x27,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00c1bca0"></a> `00c1bca0` | `f6 57 46 a9` | ldp x22,x21,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00c1bca4"></a> `00c1bca4` | `f8 5f 45 a9` | ldp x24,x23,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00c1bca8"></a> `00c1bca8` | `fa 67 44 a9` | ldp x26,x25,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00c1bcac"></a> `00c1bcac` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00c1bcb0"></a> `00c1bcb0` | `ff 03 02 91` | add sp,sp,#0x80 | `FALL_THROUGH`
<a id="insn-00c1bcb4"></a> `00c1bcb4` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00c1bcb8"></a> `00c1bcb8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00c1bcbc"></a> `00c1bcbc` | `a7 a8 ff 97` | bl 0x00c05f58 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00c1baac`](#insn-00c1baac) 範囲 `[['00c1baac', '00c1babb']]`
  - `FALL_THROUGH` [`00c1bab8`](#insn-00c1bab8) → [`00c1babc`](#insn-00c1babc)
- ブロック [`00c1babc`](#insn-00c1babc) 範囲 `[['00c1babc', '00c1baf3']]`
  - `CONDITIONAL_JUMP` [`00c1baf0`](#insn-00c1baf0) → [`00c1bb28`](#insn-00c1bb28)
  - `FALL_THROUGH` [`00c1baf0`](#insn-00c1baf0) → [`00c1baf4`](#insn-00c1baf4)
- ブロック [`00c1baf4`](#insn-00c1baf4) 範囲 `[['00c1baf4', '00c1bb0b']]`
  - `CONDITIONAL_JUMP` [`00c1bb08`](#insn-00c1bb08) → [`00c1bb68`](#insn-00c1bb68)
  - `FALL_THROUGH` [`00c1bb08`](#insn-00c1bb08) → [`00c1bb0c`](#insn-00c1bb0c)
- ブロック [`00c1bb0c`](#insn-00c1bb0c) 範囲 `[['00c1bb0c', '00c1bb27']]`
  - `UNCONDITIONAL_JUMP` [`00c1bb24`](#insn-00c1bb24) → [`00c1bb58`](#insn-00c1bb58)
- ブロック [`00c1bb28`](#insn-00c1bb28) 範囲 `[['00c1bb28', '00c1bb3f']]`
  - `CONDITIONAL_JUMP` [`00c1bb3c`](#insn-00c1bb3c) → [`00c1bb68`](#insn-00c1bb68)
  - `FALL_THROUGH` [`00c1bb3c`](#insn-00c1bb3c) → [`00c1bb40`](#insn-00c1bb40)
- ブロック [`00c1bb40`](#insn-00c1bb40) 範囲 `[['00c1bb40', '00c1bb57']]`
  - `FALL_THROUGH` [`00c1bb54`](#insn-00c1bb54) → [`00c1bb58`](#insn-00c1bb58)
- ブロック [`00c1bb58`](#insn-00c1bb58) 範囲 `[['00c1bb58', '00c1bb67']]`
  - `FALL_THROUGH` [`00c1bb64`](#insn-00c1bb64) → [`00c1bb68`](#insn-00c1bb68)
- ブロック [`00c1bb68`](#insn-00c1bb68) 範囲 `[['00c1bb68', '00c1bb7f']]`
  - `CONDITIONAL_JUMP` [`00c1bb7c`](#insn-00c1bb7c) → [`00c1bcbc`](#insn-00c1bcbc)
  - `FALL_THROUGH` [`00c1bb7c`](#insn-00c1bb7c) → [`00c1bb80`](#insn-00c1bb80)
- ブロック [`00c1bb80`](#insn-00c1bb80) 範囲 `[['00c1bb80', '00c1bb87']]`
  - `CONDITIONAL_JUMP` [`00c1bb84`](#insn-00c1bb84) → [`00c1bcbc`](#insn-00c1bcbc)
  - `FALL_THROUGH` [`00c1bb84`](#insn-00c1bb84) → [`00c1bb88`](#insn-00c1bb88)
- ブロック [`00c1bb88`](#insn-00c1bb88) 範囲 `[['00c1bb88', '00c1bb8f']]`
  - `CONDITIONAL_JUMP` [`00c1bb8c`](#insn-00c1bb8c) → [`00c1bbac`](#insn-00c1bbac)
  - `FALL_THROUGH` [`00c1bb8c`](#insn-00c1bb8c) → [`00c1bb90`](#insn-00c1bb90)
- ブロック [`00c1bb90`](#insn-00c1bb90) 範囲 `[['00c1bb90', '00c1bbab']]`
  - `UNCONDITIONAL_JUMP` [`00c1bba8`](#insn-00c1bba8) → [`00c1bbc4`](#insn-00c1bbc4)
- ブロック [`00c1bbac`](#insn-00c1bbac) 範囲 `[['00c1bbac', '00c1bbb3']]`
  - `FALL_THROUGH` [`00c1bbb0`](#insn-00c1bbb0) → [`00c1bbb4`](#insn-00c1bbb4)
- ブロック [`00c1bbb4`](#insn-00c1bbb4) 範囲 `[['00c1bbb4', '00c1bbbb']]`
  - `FALL_THROUGH` [`00c1bbb8`](#insn-00c1bbb8) → [`00c1bbbc`](#insn-00c1bbbc)
- ブロック [`00c1bbbc`](#insn-00c1bbbc) 範囲 `[['00c1bbbc', '00c1bbc3']]`
  - `FALL_THROUGH` [`00c1bbc0`](#insn-00c1bbc0) → [`00c1bbc4`](#insn-00c1bbc4)
- ブロック [`00c1bbc4`](#insn-00c1bbc4) 範囲 `[['00c1bbc4', '00c1bbd7']]`
  - `CONDITIONAL_JUMP` [`00c1bbd4`](#insn-00c1bbd4) → [`00c1bbe0`](#insn-00c1bbe0)
  - `FALL_THROUGH` [`00c1bbd4`](#insn-00c1bbd4) → [`00c1bbd8`](#insn-00c1bbd8)
- ブロック [`00c1bbd8`](#insn-00c1bbd8) 範囲 `[['00c1bbd8', '00c1bbdf']]`
  - `FALL_THROUGH` [`00c1bbdc`](#insn-00c1bbdc) → [`00c1bbe0`](#insn-00c1bbe0)
- ブロック [`00c1bbe0`](#insn-00c1bbe0) 範囲 `[['00c1bbe0', '00c1bbff']]`
  - `FALL_THROUGH` [`00c1bbfc`](#insn-00c1bbfc) → [`00c1bc00`](#insn-00c1bc00)
- ブロック [`00c1bc00`](#insn-00c1bc00) 範囲 `[['00c1bc00', '00c1bc0b']]`
  - `FALL_THROUGH` [`00c1bc08`](#insn-00c1bc08) → [`00c1bc0c`](#insn-00c1bc0c)
- ブロック [`00c1bc0c`](#insn-00c1bc0c) 範囲 `[['00c1bc0c', '00c1bc1b']]`
  - `FALL_THROUGH` [`00c1bc18`](#insn-00c1bc18) → [`00c1bc1c`](#insn-00c1bc1c)
- ブロック [`00c1bc1c`](#insn-00c1bc1c) 範囲 `[['00c1bc1c', '00c1bc33']]`
  - `CONDITIONAL_JUMP` [`00c1bc30`](#insn-00c1bc30) → [`00c1bc3c`](#insn-00c1bc3c)
  - `FALL_THROUGH` [`00c1bc30`](#insn-00c1bc30) → [`00c1bc34`](#insn-00c1bc34)
- ブロック [`00c1bc34`](#insn-00c1bc34) 範囲 `[['00c1bc34', '00c1bc3b']]`
  - `FALL_THROUGH` [`00c1bc38`](#insn-00c1bc38) → [`00c1bc3c`](#insn-00c1bc3c)
- ブロック [`00c1bc3c`](#insn-00c1bc3c) 範囲 `[['00c1bc3c', '00c1bc67']]`
  - `CONDITIONAL_JUMP` [`00c1bc64`](#insn-00c1bc64) → [`00c1bc70`](#insn-00c1bc70)
  - `FALL_THROUGH` [`00c1bc64`](#insn-00c1bc64) → [`00c1bc68`](#insn-00c1bc68)
- ブロック [`00c1bc68`](#insn-00c1bc68) 範囲 `[['00c1bc68', '00c1bc6f']]`
  - `FALL_THROUGH` [`00c1bc6c`](#insn-00c1bc6c) → [`00c1bc70`](#insn-00c1bc70)
- ブロック [`00c1bc70`](#insn-00c1bc70) 範囲 `[['00c1bc70', '00c1bc73']]`
  - `FALL_THROUGH` [`00c1bc70`](#insn-00c1bc70) → [`00c1bc74`](#insn-00c1bc74)
- ブロック [`00c1bc74`](#insn-00c1bc74) 範囲 `[['00c1bc74', '00c1bcbb']]`
- ブロック [`00c1bcbc`](#insn-00c1bcbc) 範囲 `[['00c1bcbc', '00c1bcbf']]`

## 命令位置別の参照

- [`00c1bab4`](#insn-00c1bab4) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bab8`](#insn-00c1bab8) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1babc`](#insn-00c1babc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bac0`](#insn-00c1bac0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bac4`](#insn-00c1bac4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bac8`](#insn-00c1bac8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bad0`](#insn-00c1bad0) → `Stack[0x0]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1baf0`](#insn-00c1baf0) → [`00c1bb28`](#insn-00c1bb28) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1baf8`](#insn-00c1baf8) → `00c9bbd8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c1bafc`](#insn-00c1bafc) → `01127c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk110moneypunctIcLb1EE2idE` · 推定型 `undefined8`
- [`00c1bafc`](#insn-00c1bafc) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb00`](#insn-00c1bb00) → `01127c08`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk110moneypunctIcLb1EE2idE` · 推定型 `undefined8`
- [`00c1bb08`](#insn-00c1bb08) → [`00c1bb68`](#insn-00c1bb68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb18`](#insn-00c1bb18) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb1c`](#insn-00c1bb1c) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb20`](#insn-00c1bb20) → `00c9bbd8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c1bb20`](#insn-00c1bb20) → `01127c08`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk110moneypunctIcLb1EE2idE` · 推定型 `undefined8`
- [`00c1bb24`](#insn-00c1bb24) → [`00c1bb58`](#insn-00c1bb58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb2c`](#insn-00c1bb2c) → `00c9bbe0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c1bb30`](#insn-00c1bb30) → `01127bf8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk110moneypunctIcLb0EE2idE` · 推定型 `undefined8`
- [`00c1bb30`](#insn-00c1bb30) → `Stack[-0x68]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb34`](#insn-00c1bb34) → `01127bf8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk110moneypunctIcLb0EE2idE` · 推定型 `undefined8`
- [`00c1bb3c`](#insn-00c1bb3c) → [`00c1bb68`](#insn-00c1bb68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb4c`](#insn-00c1bb4c) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb50`](#insn-00c1bb50) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb54`](#insn-00c1bb54) → `00c9bbe0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00c1bb54`](#insn-00c1bb54) → `01127bf8`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZNSt6__ndk110moneypunctIcLb0EE2idE` · 推定型 `undefined8`
- [`00c1bb5c`](#insn-00c1bb5c) → [`00c35fb8`](../00c35/00c35fb8.md) · `PARAM` · `ANALYSIS` · 関数 `00c35fb8` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb64`](#insn-00c1bb64) → [`00c5dee0`](../00c5d/00c5dee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5dee0` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb6c`](#insn-00c1bb6c) → `01127c10`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c1bb6c`](#insn-00c1bb6c) → `01127c00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00c1bb7c`](#insn-00c1bb7c) → [`00c1bcbc`](#insn-00c1bcbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb84`](#insn-00c1bb84) → [`00c1bcbc`](#insn-00c1bcbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bb8c`](#insn-00c1bb8c) → [`00c1bbac`](#insn-00c1bbac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bba8`](#insn-00c1bba8) → [`00c1bbc4`](#insn-00c1bbc4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bbd4`](#insn-00c1bbd4) → [`00c1bbe0`](#insn-00c1bbe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bbdc`](#insn-00c1bbdc) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00c1bbe0`](#insn-00c1bbe0) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bbe4`](#insn-00c1bbe4) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bc30`](#insn-00c1bc30) → [`00c1bc3c`](#insn-00c1bc3c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bc38`](#insn-00c1bc38) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00c1bc3c`](#insn-00c1bc3c) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bc40`](#insn-00c1bc40) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bc64`](#insn-00c1bc64) → [`00c1bc70`](#insn-00c1bc70) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bc6c`](#insn-00c1bc6c) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`00c1bc70`](#insn-00c1bc70) → `Stack[-0x80]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bc74`](#insn-00c1bc74) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bc84`](#insn-00c1bc84) → `Stack[0x8]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bc98`](#insn-00c1bc98) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bc9c`](#insn-00c1bc9c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bca0`](#insn-00c1bca0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bca4`](#insn-00c1bca4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bca8`](#insn-00c1bca8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bcac`](#insn-00c1bcac) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00c1bcbc`](#insn-00c1bcbc) → [`00c05f58`](../00c05/00c05f58.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c05f58` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00c1bab4`](#insn-00c1bab4)

~~~json
{
  "source": "00c1bab4",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bab8`](#insn-00c1bab8)

~~~json
{
  "source": "00c1bab8",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1babc`](#insn-00c1babc)

~~~json
{
  "source": "00c1babc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bac0`](#insn-00c1bac0)

~~~json
{
  "source": "00c1bac0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bac4`](#insn-00c1bac4)

~~~json
{
  "source": "00c1bac4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bac8`](#insn-00c1bac8)

~~~json
{
  "source": "00c1bac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bad0`](#insn-00c1bad0)

~~~json
{
  "source": "00c1bad0",
  "target": "Stack[0x0]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1baf0`](#insn-00c1baf0)

~~~json
{
  "source": "00c1baf0",
  "target": "00c1bb28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1baf8`](#insn-00c1baf8)

~~~json
{
  "source": "00c1baf8",
  "target": "00c9bbd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bbd8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c1bafc`](#insn-00c1bafc)

~~~json
{
  "source": "00c1bafc",
  "target": "01127c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1bafc`](#insn-00c1bafc)

~~~json
{
  "source": "00c1bafc",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bb00`](#insn-00c1bb00)

~~~json
{
  "source": "00c1bb00",
  "target": "01127c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1bb08`](#insn-00c1bb08)

~~~json
{
  "source": "00c1bb08",
  "target": "00c1bb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bb18`](#insn-00c1bb18)

~~~json
{
  "source": "00c1bb18",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bb1c`](#insn-00c1bb1c)

~~~json
{
  "source": "00c1bb1c",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bb20`](#insn-00c1bb20)

~~~json
{
  "source": "00c1bb20",
  "target": "00c9bbd8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bbd8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c1bb20`](#insn-00c1bb20)

~~~json
{
  "source": "00c1bb20",
  "target": "01127c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c08",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1bb24`](#insn-00c1bb24)

~~~json
{
  "source": "00c1bb24",
  "target": "00c1bb58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bb2c`](#insn-00c1bb2c)

~~~json
{
  "source": "00c1bb2c",
  "target": "00c9bbe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bbe0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c1bb30`](#insn-00c1bb30)

~~~json
{
  "source": "00c1bb30",
  "target": "01127bf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127bf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1bb30`](#insn-00c1bb30)

~~~json
{
  "source": "00c1bb30",
  "target": "Stack[-0x68]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bb34`](#insn-00c1bb34)

~~~json
{
  "source": "00c1bb34",
  "target": "01127bf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127bf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1bb3c`](#insn-00c1bb3c)

~~~json
{
  "source": "00c1bb3c",
  "target": "00c1bb68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bb4c`](#insn-00c1bb4c)

~~~json
{
  "source": "00c1bb4c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bb50`](#insn-00c1bb50)

~~~json
{
  "source": "00c1bb50",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bb54`](#insn-00c1bb54)

~~~json
{
  "source": "00c1bb54",
  "target": "00c9bbe0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9bbe0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00c1bb54`](#insn-00c1bb54)

~~~json
{
  "source": "00c1bb54",
  "target": "01127bf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127bf8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1bb5c`](#insn-00c1bb5c)

~~~json
{
  "source": "00c1bb5c",
  "target": "00c35fb8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1bb64`](#insn-00c1bb64)

~~~json
{
  "source": "00c1bb64",
  "target": "00c5dee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1bb6c`](#insn-00c1bb6c)

~~~json
{
  "source": "00c1bb6c",
  "target": "01127c10",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c10",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1bb6c`](#insn-00c1bb6c)

~~~json
{
  "source": "00c1bb6c",
  "target": "01127c00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127c00",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00c1bb7c`](#insn-00c1bb7c)

~~~json
{
  "source": "00c1bb7c",
  "target": "00c1bcbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bb84`](#insn-00c1bb84)

~~~json
{
  "source": "00c1bb84",
  "target": "00c1bcbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bb8c`](#insn-00c1bb8c)

~~~json
{
  "source": "00c1bb8c",
  "target": "00c1bbac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bba8`](#insn-00c1bba8)

~~~json
{
  "source": "00c1bba8",
  "target": "00c1bbc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bbd4`](#insn-00c1bbd4)

~~~json
{
  "source": "00c1bbd4",
  "target": "00c1bbe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bbdc`](#insn-00c1bbdc)

~~~json
{
  "source": "00c1bbdc",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1bbe0`](#insn-00c1bbe0)

~~~json
{
  "source": "00c1bbe0",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bbe4`](#insn-00c1bbe4)

~~~json
{
  "source": "00c1bbe4",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bc30`](#insn-00c1bc30)

~~~json
{
  "source": "00c1bc30",
  "target": "00c1bc3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bc38`](#insn-00c1bc38)

~~~json
{
  "source": "00c1bc38",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1bc3c`](#insn-00c1bc3c)

~~~json
{
  "source": "00c1bc3c",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bc40`](#insn-00c1bc40)

~~~json
{
  "source": "00c1bc40",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bc64`](#insn-00c1bc64)

~~~json
{
  "source": "00c1bc64",
  "target": "00c1bc70",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bc6c`](#insn-00c1bc6c)

~~~json
{
  "source": "00c1bc6c",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00c1bc70`](#insn-00c1bc70)

~~~json
{
  "source": "00c1bc70",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bc74`](#insn-00c1bc74)

~~~json
{
  "source": "00c1bc74",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bc84`](#insn-00c1bc84)

~~~json
{
  "source": "00c1bc84",
  "target": "Stack[0x8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bc98`](#insn-00c1bc98)

~~~json
{
  "source": "00c1bc98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bc9c`](#insn-00c1bc9c)

~~~json
{
  "source": "00c1bc9c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bca0`](#insn-00c1bca0)

~~~json
{
  "source": "00c1bca0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bca4`](#insn-00c1bca4)

~~~json
{
  "source": "00c1bca4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bca8`](#insn-00c1bca8)

~~~json
{
  "source": "00c1bca8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bcac`](#insn-00c1bcac)

~~~json
{
  "source": "00c1bcac",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00c1bcbc`](#insn-00c1bcbc)

~~~json
{
  "source": "00c1bcbc",
  "target": "00c05f58",
  "target_space": "ram",
  "resolution": "function"
}
~~~
