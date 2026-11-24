# 004febdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `004feb9c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004fe/004feb9c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0011.md#compare-19be97769ccf95193791c7b7cf6faebd)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `004fec1c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004fe/004fec1c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0011.md#compare-c3c7d44ec27e5ee865d6d000053fedfb)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004febdc",
  "name": "_ZN5Botan21runtime_version_checkEjjj",
  "size": 564,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5b127da73f123dea8c83e3a2f683b7cbe612ff50005180f7971bd59441fcf514",
  "source_text_sha256": "5b127da73f123dea8c83e3a2f683b7cbe612ff50005180f7971bd59441fcf514",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004febdc",
        "004fee0b"
      ],
      [
        "004fee6c",
        "004fee6f"
      ]
    ],
    "bytes_sha256": "67aedd269695c0f2c874afb7c97b780671aad354a2012135e9931c95eb5e682d",
    "instruction_count": 141,
    "instruction_bytes": 564,
    "body_bytes": 564,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [004594d0](../00459/004594d0.md)
- [00c57eb0](../00c57/00c57eb0.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57fa0](../00c57/00c57fa0.md)
- [00c57fb0](../00c57/00c57fb0.md)
- [00c57fc0](../00c57/00c57fc0.md)
- [00c581b0](../00c58/00c581b0.md)
- [00c581e0](../00c58/00c581e0.md)
- [00c581f0](../00c58/00c581f0.md)
- [00c58960](../00c58/00c58960.md)

## 関連文字列（未確認候補）

~~~text
" does not match version built against "
"Warning: linked version ("
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 3865 bytes

~~~c

/* WARNING: Type propagation algorithm not settling */

void _ZN5Botan21runtime_version_checkEjjj(undefined8 param_1,int param_2,int param_3,int param_4)

{
  undefined *puVar1;
  long lVar2;
  undefined *puVar3;
  undefined *puVar4;
  undefined8 uVar5;
  long lVar6;
  byte local_198 [16];
  void *local_188;
  undefined1 local_17c [4];
  undefined *local_178 [9];
  ulong local_130;
  undefined8 uStack_128;
  void *local_120;
  undefined8 uStack_118;
  undefined4 local_110;
  undefined *local_108 [3];
  undefined8 uStack_f0;
  undefined4 auStack_e8 [4];
  undefined8 local_d8;
  long local_70;
  
  puVar4 = PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
  ;
  puVar3 = PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
  ;
  lVar2 = tpidr_el0;
  local_70 = *(long *)(lVar2 + 0x28);
  puVar1 = PTR__ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9ac88
           + 0x40;
  local_178[0] = *(undefined **)
                  (
                  PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8
                  + 8);
  local_d8 = 0;
  local_108[0] = puVar1;
  *(undefined8 *)((long)local_178 + *(long *)(local_178[0] + -0x18)) =
       *(undefined8 *)
        (PTR__ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abb8 +
        0x10);
  lVar6 = *(long *)(local_178[0] + -0x18);
  _ZNSt6__ndk18ios_base4initEPv((long)local_178 + lVar6,local_178 + 1);
  local_178[0] = puVar4 + 0x18;
  *(undefined8 *)((long)&uStack_f0 + lVar6) = 0;
  *(undefined4 *)((long)auStack_e8 + lVar6) = 0xffffffff;
  local_108[0] = puVar1;
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEEC1Ev(local_178 + 1);
  puVar1 = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0;
  local_178[1] = PTR__ZTVNSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEE_00c9abc0
                 + 0x10;
  uStack_128 = 0;
  local_130 = 0;
  uStack_118 = 0;
  local_120 = (void *)0x0;
  local_110 = 0x10;
  if (((param_2 != 2) || (param_3 != 4)) || (param_4 != 0)) {
    uVar5 = FUN_004594d0(local_178,"Warning: linked version (",0x19);
    local_198[0] = 10;
    local_198[1] = 0x32;
    local_198[2] = 0x2e;
    local_198[3] = 0x34;
    local_198[4] = 0x2e;
    local_198[5] = 0x30;
    local_198[6] = 0;
    uVar5 = FUN_004594d0(uVar5,(ulong)local_198 | 1,5);
    uVar5 = FUN_004594d0(uVar5,&DAT_002ab332,1);
    uVar5 = FUN_004594d0(uVar5," does not match version built against ",0x26);
    uVar5 = FUN_004594d0(uVar5,&DAT_002afa22,1);
    uVar5 = _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEj(uVar5,param_2);
    local_17c[0] = 0x2e;
    uVar5 = FUN_004594d0(uVar5,local_17c,1);
    uVar5 = _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEj(uVar5,param_3);
    local_17c[0] = 0x2e;
    uVar5 = FUN_004594d0(uVar5,local_17c,1);
    uVar5 = _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEElsEj(uVar5,param_4);
    FUN_004594d0(uVar5,&DAT_002a3205,2);
    if ((local_198[0] & 1) != 0) {
      _ZdlPv(local_188);
    }
  }
  _ZNKSt6__ndk115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strEv
            (param_1,local_178 + 1);
  local_178[0] = *(undefined **)puVar3;
  *(undefined8 *)((long)local_178 + *(long *)(local_178[0] + -0x18)) =
       *(undefined8 *)(puVar3 + 0x18);
  local_178[1] = puVar1 + 0x10;
  if ((local_130 & 1) != 0) {
    _ZdlPv(local_120);
  }
  _ZNSt6__ndk115basic_streambufIcNS_11char_traitsIcEEED2Ev(local_178 + 1);
  _ZNSt6__ndk113basic_ostreamIcNS_11char_traitsIcEEED2Ev(local_178,puVar3 + 8);
  _ZNSt6__ndk19basic_iosIcNS_11char_traitsIcEEED1Ev(local_108);
  if (*(long *)(lVar2 + 0x28) == local_70) {
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
<a id="insn-004febdc"></a> `004febdc` | `ff 83 06 d1` | sub sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-004febe0"></a> `004febe0` | `fd 7b 14 a9` | stp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-004febe4"></a> `004febe4` | `fc 6f 15 a9` | stp x28,x27,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-004febe8"></a> `004febe8` | `fa 67 16 a9` | stp x26,x25,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-004febec"></a> `004febec` | `f8 5f 17 a9` | stp x24,x23,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-004febf0"></a> `004febf0` | `f6 57 18 a9` | stp x22,x21,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-004febf4"></a> `004febf4` | `f4 4f 19 a9` | stp x20,x19,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-004febf8"></a> `004febf8` | `fd 03 05 91` | add x29,sp,#0x140 | `FALL_THROUGH`
<a id="insn-004febfc"></a> `004febfc` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004fec00"></a> `004fec00` | `fb 3c 00 90` | adrp x27,0xc9a000 | `FALL_THROUGH`
<a id="insn-004fec04"></a> `004fec04` | `fa 3c 00 90` | adrp x26,0xc9a000 | `FALL_THROUGH`
<a id="insn-004fec08"></a> `004fec08` | `f3 03 08 aa` | mov x19,x8 | `FALL_THROUGH`
<a id="insn-004fec0c"></a> `004fec0c` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004fec10"></a> `004fec10` | `7b 47 46 f9` | ldr x27,[x27, #0xc88] | `FALL_THROUGH`
<a id="insn-004fec14"></a> `004fec14` | `5a df 45 f9` | ldr x26,[x26, #0xbb8] | `FALL_THROUGH`
<a id="insn-004fec18"></a> `004fec18` | `f9 a3 00 91` | add x25,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004fec1c"></a> `004fec1c` | `f4 03 02 2a` | mov w20,w2 | `FALL_THROUGH`
<a id="insn-004fec20"></a> `004fec20` | `a8 03 1f f8` | stur x8,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004fec24"></a> `004fec24` | `7c 03 01 91` | add x28,x27,#0x40 | `FALL_THROUGH`
<a id="insn-004fec28"></a> `004fec28` | `f5 03 01 2a` | mov w21,w1 | `FALL_THROUGH`
<a id="insn-004fec2c"></a> `004fec2c` | `48 a7 40 a9` | ldp x8,x9,[x26, #0x8] | `FALL_THROUGH`
<a id="insn-004fec30"></a> `004fec30` | `ff 67 00 f9` | str xzr,[sp, #0xc8] | `FALL_THROUGH`
<a id="insn-004fec34"></a> `004fec34` | `fc 4f 00 f9` | str x28,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-004fec38"></a> `004fec38` | `f6 03 00 2a` | mov w22,w0 | `FALL_THROUGH`
<a id="insn-004fec3c"></a> `004fec3c` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004fec40"></a> `004fec40` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-004fec44"></a> `004fec44` | `29 6b 28 f8` | str x9,[x25, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004fec48"></a> `004fec48` | `e8 17 40 f9` | ldr x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004fec4c"></a> `004fec4c` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-004fec50"></a> `004fec50` | `37 03 08 8b` | add x23,x25,x8 | `FALL_THROUGH`
<a id="insn-004fec54"></a> `004fec54` | `21 23 00 91` | add x1,x25,#0x8 | `FALL_THROUGH`
<a id="insn-004fec58"></a> `004fec58` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-004fec5c"></a> `004fec5c` | `61 65 1d 94` | bl 0x00c581e0 | `UNCONDITIONAL_CALL`
<a id="insn-004fec60"></a> `004fec60` | `08 00 80 12` | mov w8,#0xffffffff | `FALL_THROUGH`
<a id="insn-004fec64"></a> `004fec64` | `69 63 00 91` | add x9,x27,#0x18 | `FALL_THROUGH`
<a id="insn-004fec68"></a> `004fec68` | `ff 46 00 f9` | str xzr,[x23, #0x88] | `FALL_THROUGH`
<a id="insn-004fec6c"></a> `004fec6c` | `e8 92 00 b9` | str w8,[x23, #0x90] | `FALL_THROUGH`
<a id="insn-004fec70"></a> `004fec70` | `e9 17 00 f9` | str x9,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004fec74"></a> `004fec74` | `fc 4f 00 f9` | str x28,[sp, #0x98] | `FALL_THROUGH`
<a id="insn-004fec78"></a> `004fec78` | `20 23 00 91` | add x0,x25,#0x8 | `FALL_THROUGH`
<a id="insn-004fec7c"></a> `004fec7c` | `5d 65 1d 94` | bl 0x00c581f0 | `UNCONDITIONAL_CALL`
<a id="insn-004fec80"></a> `004fec80` | `f7 3c 00 90` | adrp x23,0xc9a000 | `FALL_THROUGH`
<a id="insn-004fec84"></a> `004fec84` | `00 e4 00 6f` | movi v0.2D,#0x0 | `FALL_THROUGH`
<a id="insn-004fec88"></a> `004fec88` | `df 0a 00 71` | cmp w22,#0x2 | `FALL_THROUGH`
<a id="insn-004fec8c"></a> `004fec8c` | `f7 e2 45 f9` | ldr x23,[x23, #0xbc0] | `FALL_THROUGH`
<a id="insn-004fec90"></a> `004fec90` | `e8 42 00 91` | add x8,x23,#0x10 | `FALL_THROUGH`
<a id="insn-004fec94"></a> `004fec94` | `e8 1b 00 f9` | str x8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fec98"></a> `004fec98` | `08 02 80 52` | mov w8,#0x10 | `FALL_THROUGH`
<a id="insn-004fec9c"></a> `004fec9c` | `e0 83 03 ad` | stp q0,q0,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004feca0"></a> `004feca0` | `e8 93 00 b9` | str w8,[sp, #0x90] | `FALL_THROUGH`
<a id="insn-004feca4"></a> `004feca4` | `81 00 00 54` | b.ne 0x004fecb4 | `CONDITIONAL_JUMP`
<a id="insn-004feca8"></a> `004feca8` | `bf 12 00 71` | cmp w21,#0x4 | `FALL_THROUGH`
<a id="insn-004fecac"></a> `004fecac` | `41 00 00 54` | b.ne 0x004fecb4 | `CONDITIONAL_JUMP`
<a id="insn-004fecb0"></a> `004fecb0` | `b4 06 00 34` | cbz w20,0x004fed84 | `CONDITIONAL_JUMP`
<a id="insn-004fecb4"></a> `004fecb4` | `61 ed ff d0` | adrp x1,0x2ac000 | `FALL_THROUGH`
<a id="insn-004fecb8"></a> `004fecb8` | `21 58 21 91` | add x1,x1,#0x856 | `FALL_THROUGH`
<a id="insn-004fecbc"></a> `004fecbc` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004fecc0"></a> `004fecc0` | `22 03 80 52` | mov w2,#0x19 | `FALL_THROUGH`
<a id="insn-004fecc4"></a> `004fecc4` | `03 6a fd 97` | bl 0x004594d0 | `UNCONDITIONAL_CALL`
<a id="insn-004fecc8"></a> `004fecc8` | `48 01 80 52` | mov w8,#0xa | `FALL_THROUGH`
<a id="insn-004feccc"></a> `004feccc` | `49 c6 85 52` | mov w9,#0x2e32 | `FALL_THROUGH`
<a id="insn-004fecd0"></a> `004fecd0` | `89 c6 a5 72` | movk w9,#0x2e34, LSL #16 | `FALL_THROUGH`
<a id="insn-004fecd4"></a> `004fecd4` | `e8 23 00 39` | strb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fecd8"></a> `004fecd8` | `08 06 80 52` | mov w8,#0x30 | `FALL_THROUGH`
<a id="insn-004fecdc"></a> `004fecdc` | `e9 93 00 b8` | stur w9,[sp, #0x9] | `FALL_THROUGH`
<a id="insn-004fece0"></a> `004fece0` | `e9 23 00 91` | add x9,sp,#0x8 | `FALL_THROUGH`
<a id="insn-004fece4"></a> `004fece4` | `e8 d3 00 78` | sturh w8,[sp, #0xd] | `FALL_THROUGH`
<a id="insn-004fece8"></a> `004fece8` | `21 01 40 b2` | orr x1,x9,#0x1 | `FALL_THROUGH`
<a id="insn-004fecec"></a> `004fecec` | `a2 00 80 52` | mov w2,#0x5 | `FALL_THROUGH`
<a id="insn-004fecf0"></a> `004fecf0` | `f8 69 fd 97` | bl 0x004594d0 | `UNCONDITIONAL_CALL`
<a id="insn-004fecf4"></a> `004fecf4` | `61 ed ff b0` | adrp x1,0x2ab000 | `FALL_THROUGH`
<a id="insn-004fecf8"></a> `004fecf8` | `21 c8 0c 91` | add x1,x1,#0x332 | `FALL_THROUGH`
<a id="insn-004fecfc"></a> `004fecfc` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004fed00"></a> `004fed00` | `f4 69 fd 97` | bl 0x004594d0 | `UNCONDITIONAL_CALL`
<a id="insn-004fed04"></a> `004fed04` | `01 ed ff d0` | adrp x1,0x2a0000 | `FALL_THROUGH`
<a id="insn-004fed08"></a> `004fed08` | `21 8c 03 91` | add x1,x1,#0xe3 | `FALL_THROUGH`
<a id="insn-004fed0c"></a> `004fed0c` | `c2 04 80 52` | mov w2,#0x26 | `FALL_THROUGH`
<a id="insn-004fed10"></a> `004fed10` | `f0 69 fd 97` | bl 0x004594d0 | `UNCONDITIONAL_CALL`
<a id="insn-004fed14"></a> `004fed14` | `81 ed ff b0` | adrp x1,0x2af000 | `FALL_THROUGH`
<a id="insn-004fed18"></a> `004fed18` | `21 88 28 91` | add x1,x1,#0xa22 | `FALL_THROUGH`
<a id="insn-004fed1c"></a> `004fed1c` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004fed20"></a> `004fed20` | `ec 69 fd 97` | bl 0x004594d0 | `UNCONDITIONAL_CALL`
<a id="insn-004fed24"></a> `004fed24` | `e1 03 16 2a` | mov w1,w22 | `FALL_THROUGH`
<a id="insn-004fed28"></a> `004fed28` | `0e 67 1d 94` | bl 0x00c58960 | `UNCONDITIONAL_CALL`
<a id="insn-004fed2c"></a> `004fed2c` | `c8 05 80 52` | mov w8,#0x2e | `FALL_THROUGH`
<a id="insn-004fed30"></a> `004fed30` | `e8 93 00 39` | strb w8,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-004fed34"></a> `004fed34` | `e1 93 00 91` | add x1,sp,#0x24 | `FALL_THROUGH`
<a id="insn-004fed38"></a> `004fed38` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004fed3c"></a> `004fed3c` | `e5 69 fd 97` | bl 0x004594d0 | `UNCONDITIONAL_CALL`
<a id="insn-004fed40"></a> `004fed40` | `e1 03 15 2a` | mov w1,w21 | `FALL_THROUGH`
<a id="insn-004fed44"></a> `004fed44` | `07 67 1d 94` | bl 0x00c58960 | `UNCONDITIONAL_CALL`
<a id="insn-004fed48"></a> `004fed48` | `c8 05 80 52` | mov w8,#0x2e | `FALL_THROUGH`
<a id="insn-004fed4c"></a> `004fed4c` | `e8 93 00 39` | strb w8,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-004fed50"></a> `004fed50` | `e1 93 00 91` | add x1,sp,#0x24 | `FALL_THROUGH`
<a id="insn-004fed54"></a> `004fed54` | `22 00 80 52` | mov w2,#0x1 | `FALL_THROUGH`
<a id="insn-004fed58"></a> `004fed58` | `de 69 fd 97` | bl 0x004594d0 | `UNCONDITIONAL_CALL`
<a id="insn-004fed5c"></a> `004fed5c` | `e1 03 14 2a` | mov w1,w20 | `FALL_THROUGH`
<a id="insn-004fed60"></a> `004fed60` | `00 67 1d 94` | bl 0x00c58960 | `UNCONDITIONAL_CALL`
<a id="insn-004fed64"></a> `004fed64` | `21 ed ff b0` | adrp x1,0x2a3000 | `FALL_THROUGH`
<a id="insn-004fed68"></a> `004fed68` | `21 14 08 91` | add x1,x1,#0x205 | `FALL_THROUGH`
<a id="insn-004fed6c"></a> `004fed6c` | `42 00 80 52` | mov w2,#0x2 | `FALL_THROUGH`
<a id="insn-004fed70"></a> `004fed70` | `d8 69 fd 97` | bl 0x004594d0 | `UNCONDITIONAL_CALL`
<a id="insn-004fed74"></a> `004fed74` | `e8 23 40 39` | ldrb w8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004fed78"></a> `004fed78` | `68 00 00 36` | tbz w8,#0x0,0x004fed84 | `CONDITIONAL_JUMP`
<a id="insn-004fed7c"></a> `004fed7c` | `e0 0f 40 f9` | ldr x0,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-004fed80"></a> `004fed80` | `4c 64 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fed84"></a> `004fed84` | `20 23 00 91` | add x0,x25,#0x8 | `FALL_THROUGH`
<a id="insn-004fed88"></a> `004fed88` | `e8 03 13 aa` | mov x8,x19 | `FALL_THROUGH`
<a id="insn-004fed8c"></a> `004fed8c` | `09 65 1d 94` | bl 0x00c581b0 | `UNCONDITIONAL_CALL`
<a id="insn-004fed90"></a> `004fed90` | `48 03 40 f9` | ldr x8,[x26] | `FALL_THROUGH`
<a id="insn-004fed94"></a> `004fed94` | `49 0f 40 f9` | ldr x9,[x26, #0x18] | `FALL_THROUGH`
<a id="insn-004fed98"></a> `004fed98` | `ea a3 00 91` | add x10,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004fed9c"></a> `004fed9c` | `e8 17 00 f9` | str x8,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-004feda0"></a> `004feda0` | `08 81 5e f8` | ldur x8,[x8, #-0x18] | `FALL_THROUGH`
<a id="insn-004feda4"></a> `004feda4` | `49 69 28 f8` | str x9,[x10, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-004feda8"></a> `004feda8` | `e9 42 00 91` | add x9,x23,#0x10 | `FALL_THROUGH`
<a id="insn-004fedac"></a> `004fedac` | `e8 c3 41 39` | ldrb w8,[sp, #0x70] | `FALL_THROUGH`
<a id="insn-004fedb0"></a> `004fedb0` | `e9 1b 00 f9` | str x9,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004fedb4"></a> `004fedb4` | `68 00 00 36` | tbz w8,#0x0,0x004fedc0 | `CONDITIONAL_JUMP`
<a id="insn-004fedb8"></a> `004fedb8` | `e0 43 40 f9` | ldr x0,[sp, #0x80] | `FALL_THROUGH`
<a id="insn-004fedbc"></a> `004fedbc` | `3d 64 1d 94` | bl 0x00c57eb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fedc0"></a> `004fedc0` | `20 23 00 91` | add x0,x25,#0x8 | `FALL_THROUGH`
<a id="insn-004fedc4"></a> `004fedc4` | `77 64 1d 94` | bl 0x00c57fa0 | `UNCONDITIONAL_CALL`
<a id="insn-004fedc8"></a> `004fedc8` | `e0 a3 00 91` | add x0,sp,#0x28 | `FALL_THROUGH`
<a id="insn-004fedcc"></a> `004fedcc` | `41 23 00 91` | add x1,x26,#0x8 | `FALL_THROUGH`
<a id="insn-004fedd0"></a> `004fedd0` | `78 64 1d 94` | bl 0x00c57fb0 | `UNCONDITIONAL_CALL`
<a id="insn-004fedd4"></a> `004fedd4` | `20 c3 01 91` | add x0,x25,#0x70 | `FALL_THROUGH`
<a id="insn-004fedd8"></a> `004fedd8` | `7a 64 1d 94` | bl 0x00c57fc0 | `UNCONDITIONAL_CALL`
<a id="insn-004feddc"></a> `004feddc` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-004fede0"></a> `004fede0` | `a9 03 5f f8` | ldur x9,[x29, #-0x10] | `FALL_THROUGH`
<a id="insn-004fede4"></a> `004fede4` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004fede8"></a> `004fede8` | `21 04 00 54` | b.ne 0x004fee6c | `CONDITIONAL_JUMP`
<a id="insn-004fedec"></a> `004fedec` | `f4 4f 59 a9` | ldp x20,x19,[sp, #0x190] | `FALL_THROUGH`
<a id="insn-004fedf0"></a> `004fedf0` | `f6 57 58 a9` | ldp x22,x21,[sp, #0x180] | `FALL_THROUGH`
<a id="insn-004fedf4"></a> `004fedf4` | `f8 5f 57 a9` | ldp x24,x23,[sp, #0x170] | `FALL_THROUGH`
<a id="insn-004fedf8"></a> `004fedf8` | `fa 67 56 a9` | ldp x26,x25,[sp, #0x160] | `FALL_THROUGH`
<a id="insn-004fedfc"></a> `004fedfc` | `fc 6f 55 a9` | ldp x28,x27,[sp, #0x150] | `FALL_THROUGH`
<a id="insn-004fee00"></a> `004fee00` | `fd 7b 54 a9` | ldp x29,x30,[sp, #0x140] | `FALL_THROUGH`
<a id="insn-004fee04"></a> `004fee04` | `ff 83 06 91` | add sp,sp,#0x1a0 | `FALL_THROUGH`
<a id="insn-004fee08"></a> `004fee08` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004fee6c"></a> `004fee6c` | `1d 64 1d 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004febdc`](#insn-004febdc) 範囲 `[['004febdc', '004feca7']]`
  - `CONDITIONAL_JUMP` [`004feca4`](#insn-004feca4) → [`004fecb4`](#insn-004fecb4)
  - `FALL_THROUGH` [`004feca4`](#insn-004feca4) → [`004feca8`](#insn-004feca8)
- ブロック [`004feca8`](#insn-004feca8) 範囲 `[['004feca8', '004fecaf']]`
  - `CONDITIONAL_JUMP` [`004fecac`](#insn-004fecac) → [`004fecb4`](#insn-004fecb4)
  - `FALL_THROUGH` [`004fecac`](#insn-004fecac) → [`004fecb0`](#insn-004fecb0)
- ブロック [`004fecb0`](#insn-004fecb0) 範囲 `[['004fecb0', '004fecb3']]`
  - `CONDITIONAL_JUMP` [`004fecb0`](#insn-004fecb0) → [`004fed84`](#insn-004fed84)
  - `FALL_THROUGH` [`004fecb0`](#insn-004fecb0) → [`004fecb4`](#insn-004fecb4)
- ブロック [`004fecb4`](#insn-004fecb4) 範囲 `[['004fecb4', '004fed7b']]`
  - `CONDITIONAL_JUMP` [`004fed78`](#insn-004fed78) → [`004fed84`](#insn-004fed84)
  - `FALL_THROUGH` [`004fed78`](#insn-004fed78) → [`004fed7c`](#insn-004fed7c)
- ブロック [`004fed7c`](#insn-004fed7c) 範囲 `[['004fed7c', '004fed83']]`
  - `FALL_THROUGH` [`004fed80`](#insn-004fed80) → [`004fed84`](#insn-004fed84)
- ブロック [`004fed84`](#insn-004fed84) 範囲 `[['004fed84', '004fedb7']]`
  - `CONDITIONAL_JUMP` [`004fedb4`](#insn-004fedb4) → [`004fedc0`](#insn-004fedc0)
  - `FALL_THROUGH` [`004fedb4`](#insn-004fedb4) → [`004fedb8`](#insn-004fedb8)
- ブロック [`004fedb8`](#insn-004fedb8) 範囲 `[['004fedb8', '004fedbf']]`
  - `FALL_THROUGH` [`004fedbc`](#insn-004fedbc) → [`004fedc0`](#insn-004fedc0)
- ブロック [`004fedc0`](#insn-004fedc0) 範囲 `[['004fedc0', '004fedeb']]`
  - `CONDITIONAL_JUMP` [`004fede8`](#insn-004fede8) → [`004fee6c`](#insn-004fee6c)
  - `FALL_THROUGH` [`004fede8`](#insn-004fede8) → [`004fedec`](#insn-004fedec)
- ブロック [`004fedec`](#insn-004fedec) 範囲 `[['004fedec', '004fee0b']]`
- ブロック [`004fee6c`](#insn-004fee6c) 範囲 `[['004fee6c', '004fee6f']]`

## 命令位置別の参照

- [`004febe0`](#insn-004febe0) → `Stack[-0x60]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004febe4`](#insn-004febe4) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004febe8`](#insn-004febe8) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004febec`](#insn-004febec) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004febf0`](#insn-004febf0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004febf4`](#insn-004febf4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fec10`](#insn-004fec10) → `00c9ac88`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fec14`](#insn-004fec14) → `00c9abb8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fec20`](#insn-004fec20) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fec2c`](#insn-004fec2c) → `00c93208`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`004fec2c`](#insn-004fec2c) → `00c93210`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`004fec30`](#insn-004fec30) → `Stack[-0xd8]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fec34`](#insn-004fec34) → `00c91038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fec34`](#insn-004fec34) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fec3c`](#insn-004fec3c) → `00c91060`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fec3c`](#insn-004fec3c) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fec40`](#insn-004fec40) → `00c91048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTCNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE0_NS_13basic_ostreamIcS2_EE` · 推定型 `undefined8`
- [`004fec44`](#insn-004fec44) → `00c91088`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fec48`](#insn-004fec48) → `Stack[-0x178]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fec4c`](#insn-004fec4c) → `00c91048`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTCNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE0_NS_13basic_ostreamIcS2_EE` · 推定型 `undefined8`
- [`004fec5c`](#insn-004fec5c) → [`00c581e0`](../00c58/00c581e0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581e0` · 推定シンボル `None` · 推定型 `None`
- [`004fec68`](#insn-004fec68) → `Stack[-0x80]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fec6c`](#insn-004fec6c) → `Stack[-0x78]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fec70`](#insn-004fec70) → `00c91010`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fec70`](#insn-004fec70) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fec74`](#insn-004fec74) → `00c91038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fec74`](#insn-004fec74) → `Stack[-0x108]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fec7c`](#insn-004fec7c) → [`00c581f0`](../00c58/00c581f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581f0` · 推定シンボル `None` · 推定型 `None`
- [`004fec8c`](#insn-004fec8c) → `00c9abc0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fec94`](#insn-004fec94) → `00c90c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004fec94`](#insn-004fec94) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fec9c`](#insn-004fec9c) → `Stack[-0x130]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004feca0`](#insn-004feca0) → `Stack[-0x110]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004feca4`](#insn-004feca4) → [`004fecb4`](#insn-004fecb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fecac`](#insn-004fecac) → [`004fecb4`](#insn-004fecb4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fecb0`](#insn-004fecb0) → [`004fed84`](#insn-004fed84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fecb8`](#insn-004fecb8) → `002ac856`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004fecc4`](#insn-004fecc4) → [`004594d0`](../00459/004594d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004594d0` · 推定シンボル `None` · 推定型 `None`
- [`004fecd4`](#insn-004fecd4) → `Stack[-0x198]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fecdc`](#insn-004fecdc) → `Stack[-0x197]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fece4`](#insn-004fece4) → `Stack[-0x193]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fecf0`](#insn-004fecf0) → [`004594d0`](../00459/004594d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004594d0` · 推定シンボル `None` · 推定型 `None`
- [`004fecf8`](#insn-004fecf8) → `002ab332`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fed00`](#insn-004fed00) → [`004594d0`](../00459/004594d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004594d0` · 推定シンボル `None` · 推定型 `None`
- [`004fed08`](#insn-004fed08) → `002a00e3`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004fed10`](#insn-004fed10) → [`004594d0`](../00459/004594d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004594d0` · 推定シンボル `None` · 推定型 `None`
- [`004fed18`](#insn-004fed18) → `002afa22`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fed20`](#insn-004fed20) → [`004594d0`](../00459/004594d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004594d0` · 推定シンボル `None` · 推定型 `None`
- [`004fed28`](#insn-004fed28) → [`00c58960`](../00c58/00c58960.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58960` · 推定シンボル `None` · 推定型 `None`
- [`004fed30`](#insn-004fed30) → `Stack[-0x17c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fed3c`](#insn-004fed3c) → [`004594d0`](../00459/004594d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004594d0` · 推定シンボル `None` · 推定型 `None`
- [`004fed44`](#insn-004fed44) → [`00c58960`](../00c58/00c58960.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58960` · 推定シンボル `None` · 推定型 `None`
- [`004fed4c`](#insn-004fed4c) → `Stack[-0x17c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fed58`](#insn-004fed58) → [`004594d0`](../00459/004594d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004594d0` · 推定シンボル `None` · 推定型 `None`
- [`004fed60`](#insn-004fed60) → [`00c58960`](../00c58/00c58960.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58960` · 推定シンボル `None` · 推定型 `None`
- [`004fed68`](#insn-004fed68) → `002a3205`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fed70`](#insn-004fed70) → [`004594d0`](../00459/004594d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004594d0` · 推定シンボル `None` · 推定型 `None`
- [`004fed74`](#insn-004fed74) → `Stack[-0x198]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fed78`](#insn-004fed78) → [`004fed84`](#insn-004fed84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fed7c`](#insn-004fed7c) → `Stack[-0x188]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fed80`](#insn-004fed80) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004fed8c`](#insn-004fed8c) → [`00c581b0`](../00c58/00c581b0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c581b0` · 推定シンボル `None` · 推定型 `None`
- [`004fed90`](#insn-004fed90) → `00c93200`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTTNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `pointer __((offset(0x18)))`
- [`004fed94`](#insn-004fed94) → `00c93218`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x40)))`
- [`004fed9c`](#insn-004fed9c) → `00c91010`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fed9c`](#insn-004fed9c) → `Stack[-0x178]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004feda0`](#insn-004feda0) → `00c90ff8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTVNSt6__ndk119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEE` · 推定型 `undefined8`
- [`004feda4`](#insn-004feda4) → `00c91038`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004fedac`](#insn-004fedac) → `Stack[-0x130]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fedb0`](#insn-004fedb0) → `00c90c08`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[128]`
- [`004fedb0`](#insn-004fedb0) → `Stack[-0x170]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fedb4`](#insn-004fedb4) → [`004fedc0`](#insn-004fedc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fedb8`](#insn-004fedb8) → `Stack[-0x120]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fedbc`](#insn-004fedbc) → [`00c57eb0`](../00c57/00c57eb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57eb0` · 推定シンボル `None` · 推定型 `None`
- [`004fedc4`](#insn-004fedc4) → [`00c57fa0`](../00c57/00c57fa0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fa0` · 推定シンボル `None` · 推定型 `None`
- [`004fedcc`](#insn-004fedcc) → `00c93208`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer __((offset(0x18)))`
- [`004fedd0`](#insn-004fedd0) → [`00c57fb0`](../00c57/00c57fb0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fb0` · 推定シンボル `None` · 推定型 `None`
- [`004fedd8`](#insn-004fedd8) → [`00c57fc0`](../00c57/00c57fc0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57fc0` · 推定シンボル `None` · 推定型 `None`
- [`004fede0`](#insn-004fede0) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fede8`](#insn-004fede8) → [`004fee6c`](#insn-004fee6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fedec`](#insn-004fedec) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fedf0`](#insn-004fedf0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fedf4`](#insn-004fedf4) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fedf8`](#insn-004fedf8) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fedfc`](#insn-004fedfc) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fee00`](#insn-004fee00) → `Stack[-0x60]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004fee6c`](#insn-004fee6c) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004febe0`](#insn-004febe0)

~~~json
{
  "source": "004febe0",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004febe4`](#insn-004febe4)

~~~json
{
  "source": "004febe4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004febe8`](#insn-004febe8)

~~~json
{
  "source": "004febe8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004febec`](#insn-004febec)

~~~json
{
  "source": "004febec",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004febf0`](#insn-004febf0)

~~~json
{
  "source": "004febf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004febf4`](#insn-004febf4)

~~~json
{
  "source": "004febf4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fec10`](#insn-004fec10)

~~~json
{
  "source": "004fec10",
  "target": "00c9ac88",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ac88",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fec14`](#insn-004fec14)

~~~json
{
  "source": "004fec14",
  "target": "00c9abb8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abb8",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fec20`](#insn-004fec20)

~~~json
{
  "source": "004fec20",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fec2c`](#insn-004fec2c)

~~~json
{
  "source": "004fec2c",
  "target": "00c93208",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93208",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fec2c`](#insn-004fec2c)

~~~json
{
  "source": "004fec2c",
  "target": "00c93210",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93210",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fec30`](#insn-004fec30)

~~~json
{
  "source": "004fec30",
  "target": "Stack[-0xd8]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fec34`](#insn-004fec34)

~~~json
{
  "source": "004fec34",
  "target": "00c91038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91038",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fec34`](#insn-004fec34)

~~~json
{
  "source": "004fec34",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fec3c`](#insn-004fec3c)

~~~json
{
  "source": "004fec3c",
  "target": "00c91060",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91060",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fec3c`](#insn-004fec3c)

~~~json
{
  "source": "004fec3c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fec40`](#insn-004fec40)

~~~json
{
  "source": "004fec40",
  "target": "00c91048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91048",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c91048",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004fec44`](#insn-004fec44)

~~~json
{
  "source": "004fec44",
  "target": "00c91088",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91088",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fec48`](#insn-004fec48)

~~~json
{
  "source": "004fec48",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fec4c`](#insn-004fec4c)

~~~json
{
  "source": "004fec4c",
  "target": "00c91048",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91048",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c91048",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004fec5c`](#insn-004fec5c)

~~~json
{
  "source": "004fec5c",
  "target": "00c581e0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fec68`](#insn-004fec68)

~~~json
{
  "source": "004fec68",
  "target": "Stack[-0x80]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fec6c`](#insn-004fec6c)

~~~json
{
  "source": "004fec6c",
  "target": "Stack[-0x78]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fec70`](#insn-004fec70)

~~~json
{
  "source": "004fec70",
  "target": "00c91010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91010",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fec70`](#insn-004fec70)

~~~json
{
  "source": "004fec70",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fec74`](#insn-004fec74)

~~~json
{
  "source": "004fec74",
  "target": "00c91038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91038",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fec74`](#insn-004fec74)

~~~json
{
  "source": "004fec74",
  "target": "Stack[-0x108]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fec7c`](#insn-004fec7c)

~~~json
{
  "source": "004fec7c",
  "target": "00c581f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fec8c`](#insn-004fec8c)

~~~json
{
  "source": "004fec8c",
  "target": "00c9abc0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9abc0",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fec94`](#insn-004fec94)

~~~json
{
  "source": "004fec94",
  "target": "00c90c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90bf8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fec94`](#insn-004fec94)

~~~json
{
  "source": "004fec94",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fec9c`](#insn-004fec9c)

~~~json
{
  "source": "004fec9c",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004feca0`](#insn-004feca0)

~~~json
{
  "source": "004feca0",
  "target": "Stack[-0x110]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004feca4`](#insn-004feca4)

~~~json
{
  "source": "004feca4",
  "target": "004fecb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fecac`](#insn-004fecac)

~~~json
{
  "source": "004fecac",
  "target": "004fecb4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fecb0`](#insn-004fecb0)

~~~json
{
  "source": "004fecb0",
  "target": "004fed84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fecb8`](#insn-004fecb8)

~~~json
{
  "source": "004fecb8",
  "target": "002ac856",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002ac856",
  "offset": 0,
  "size": 26,
  "datatype": "string",
  "bytes": "5761726e696e673a206c696e6b65642076657273696f6e202800",
  "capture_start": "002ac856",
  "capture_bytes": 26,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004fecc4`](#insn-004fecc4)

~~~json
{
  "source": "004fecc4",
  "target": "004594d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fecd4`](#insn-004fecd4)

~~~json
{
  "source": "004fecd4",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fecdc`](#insn-004fecdc)

~~~json
{
  "source": "004fecdc",
  "target": "Stack[-0x197]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fece4`](#insn-004fece4)

~~~json
{
  "source": "004fece4",
  "target": "Stack[-0x193]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fecf0`](#insn-004fecf0)

~~~json
{
  "source": "004fecf0",
  "target": "004594d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fecf8`](#insn-004fecf8)

~~~json
{
  "source": "004fecf8",
  "target": "002ab332",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fed00`](#insn-004fed00)

~~~json
{
  "source": "004fed00",
  "target": "004594d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fed08`](#insn-004fed08)

~~~json
{
  "source": "004fed08",
  "target": "002a00e3",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a00e3",
  "offset": 0,
  "size": 39,
  "datatype": "string",
  "bytes": "20646f6573206e6f74206d617463682076657273696f6e206275696c74206167",
  "capture_start": "002a00e3",
  "capture_bytes": 32,
  "capture_state": "bounded_prefix"
}
~~~
- 参照命令 [`004fed10`](#insn-004fed10)

~~~json
{
  "source": "004fed10",
  "target": "004594d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fed18`](#insn-004fed18)

~~~json
{
  "source": "004fed18",
  "target": "002afa22",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fed20`](#insn-004fed20)

~~~json
{
  "source": "004fed20",
  "target": "004594d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fed28`](#insn-004fed28)

~~~json
{
  "source": "004fed28",
  "target": "00c58960",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fed30`](#insn-004fed30)

~~~json
{
  "source": "004fed30",
  "target": "Stack[-0x17c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fed3c`](#insn-004fed3c)

~~~json
{
  "source": "004fed3c",
  "target": "004594d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fed44`](#insn-004fed44)

~~~json
{
  "source": "004fed44",
  "target": "00c58960",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fed4c`](#insn-004fed4c)

~~~json
{
  "source": "004fed4c",
  "target": "Stack[-0x17c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fed58`](#insn-004fed58)

~~~json
{
  "source": "004fed58",
  "target": "004594d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fed60`](#insn-004fed60)

~~~json
{
  "source": "004fed60",
  "target": "00c58960",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fed68`](#insn-004fed68)

~~~json
{
  "source": "004fed68",
  "target": "002a3205",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fed70`](#insn-004fed70)

~~~json
{
  "source": "004fed70",
  "target": "004594d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fed74`](#insn-004fed74)

~~~json
{
  "source": "004fed74",
  "target": "Stack[-0x198]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fed78`](#insn-004fed78)

~~~json
{
  "source": "004fed78",
  "target": "004fed84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fed7c`](#insn-004fed7c)

~~~json
{
  "source": "004fed7c",
  "target": "Stack[-0x188]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fed80`](#insn-004fed80)

~~~json
{
  "source": "004fed80",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fed8c`](#insn-004fed8c)

~~~json
{
  "source": "004fed8c",
  "target": "00c581b0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fed90`](#insn-004fed90)

~~~json
{
  "source": "004fed90",
  "target": "00c93200",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93200",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fed94`](#insn-004fed94)

~~~json
{
  "source": "004fed94",
  "target": "00c93218",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93218",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x40)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fed9c`](#insn-004fed9c)

~~~json
{
  "source": "004fed9c",
  "target": "00c91010",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91010",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fed9c`](#insn-004fed9c)

~~~json
{
  "source": "004fed9c",
  "target": "Stack[-0x178]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004feda0`](#insn-004feda0)

~~~json
{
  "source": "004feda0",
  "target": "00c90ff8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90ff8",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "bytes": "7000000000000000",
  "capture_start": "00c90ff8",
  "capture_bytes": 8,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004feda4`](#insn-004feda4)

~~~json
{
  "source": "004feda4",
  "target": "00c91038",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c91038",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fedac`](#insn-004fedac)

~~~json
{
  "source": "004fedac",
  "target": "Stack[-0x130]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fedb0`](#insn-004fedb0)

~~~json
{
  "source": "004fedb0",
  "target": "00c90c08",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c90bf8",
  "offset": 16,
  "size": 128,
  "datatype": "undefined1[128]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`004fedb0`](#insn-004fedb0)

~~~json
{
  "source": "004fedb0",
  "target": "Stack[-0x170]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fedb4`](#insn-004fedb4)

~~~json
{
  "source": "004fedb4",
  "target": "004fedc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fedb8`](#insn-004fedb8)

~~~json
{
  "source": "004fedb8",
  "target": "Stack[-0x120]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fedbc`](#insn-004fedbc)

~~~json
{
  "source": "004fedbc",
  "target": "00c57eb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fedc4`](#insn-004fedc4)

~~~json
{
  "source": "004fedc4",
  "target": "00c57fa0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fedcc`](#insn-004fedcc)

~~~json
{
  "source": "004fedcc",
  "target": "00c93208",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c93208",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x18)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004fedd0`](#insn-004fedd0)

~~~json
{
  "source": "004fedd0",
  "target": "00c57fb0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fedd8`](#insn-004fedd8)

~~~json
{
  "source": "004fedd8",
  "target": "00c57fc0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004fede0`](#insn-004fede0)

~~~json
{
  "source": "004fede0",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fede8`](#insn-004fede8)

~~~json
{
  "source": "004fede8",
  "target": "004fee6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fedec`](#insn-004fedec)

~~~json
{
  "source": "004fedec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fedf0`](#insn-004fedf0)

~~~json
{
  "source": "004fedf0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fedf4`](#insn-004fedf4)

~~~json
{
  "source": "004fedf4",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fedf8`](#insn-004fedf8)

~~~json
{
  "source": "004fedf8",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fedfc`](#insn-004fedfc)

~~~json
{
  "source": "004fedfc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fee00`](#insn-004fee00)

~~~json
{
  "source": "004fee00",
  "target": "Stack[-0x60]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004fee6c`](#insn-004fee6c)

~~~json
{
  "source": "004fee6c",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
