# 00bf5bcc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `00bf57a4`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00bf5/00bf57a4.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0086.md#compare-caa0ebfc4611e1e2272069e371bd16da)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf5c68`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5c68.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-d3602b3a408d7e217f4c66d0e55ea0a3)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf5bcc",
  "name": "_ZNSt6__ndk16stoullERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi",
  "size": 380,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a2ad63f5763b390af7cc7d12b7c5b68010a4dabf627d4d1ec3c16f28892aece8",
  "source_text_sha256": "a2ad63f5763b390af7cc7d12b7c5b68010a4dabf627d4d1ec3c16f28892aece8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf5bcc",
        "00bf5d37"
      ],
      [
        "00bf5d3c",
        "00bf5d4b"
      ]
    ],
    "bytes_sha256": "3e9af73751339711e7477b949a69f45a60df4f342d938f0b1625fa8858afb425",
    "instruction_count": 95,
    "instruction_bytes": 380,
    "body_bytes": 380,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00442930](../00442/00442930.md)
- [00bf81cc](../00bf8/00bf81cc.md)
- [00c53f5c](../00c53/00c53f5c.md)
- [00c580c0](../00c58/00c580c0.md)
- [00c5e050](../00c5e/00c5e050.md)
- [00c5e0c0](../00c5e/00c5e0c0.md)

## 関連文字列（未確認候補）

~~~text
": no conversion"
": out of range"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2802 bytes

~~~c

ulonglong _ZNSt6__ndk16stoullERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi
                    (byte *param_1,long *param_2,int param_3)

{
  wchar_t *__nptr;
  int iVar1;
  int iVar2;
  int *piVar3;
  ulonglong uVar4;
  undefined8 uVar5;
  undefined4 *puVar6;
  undefined1 local_70;
  undefined4 local_6f;
  undefined2 local_6b;
  undefined1 local_69;
  undefined1 local_58;
  undefined4 local_57;
  undefined2 local_53;
  undefined6 local_51;
  char cStack_4b;
  char cStack_4a;
  char cStack_49;
  undefined5 local_48;
  char cStack_43;
  undefined2 uStack_42;
  wchar_t *local_28;
  
  local_70 = 0xc;
  local_6f = 0x756f7473;
  local_6b = 0x6c6c;
  local_69 = 0;
  local_28 = (wchar_t *)0x0;
  __nptr = (wchar_t *)(param_1 + 4);
  if ((*param_1 & 1) != 0) {
    __nptr = *(wchar_t **)(param_1 + 0x10);
  }
  piVar3 = (int *)__errno();
  iVar1 = *piVar3;
  *piVar3 = 0;
  uVar4 = wcstoull(__nptr,&local_28,param_3);
  iVar2 = *piVar3;
  *piVar3 = iVar1;
  puVar6 = (undefined4 *)((ulong)&local_70 | 1);
  if (iVar2 != 0x22) {
    if ((long)local_28 - (long)__nptr != 0) {
      if (param_2 != (long *)0x0) {
        *param_2 = (long)local_28 - (long)__nptr >> 2;
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
      return uVar4;
    }
    local_57 = *puVar6;
    local_53 = *(undefined2 *)(puVar6 + 1);
    local_58 = 0x2a;
    uStack_42 = 0;
    local_51 = (undefined6)s___no_conversion_002a750a._0_7_;
    cStack_4b = SUB71(s___no_conversion_002a750a._0_7_,6);
    cStack_4a = s___no_conversion_002a750a[7];
    cStack_49 = (char)s___no_conversion_002a750a._8_7_;
    local_48 = SUB75(s___no_conversion_002a750a._8_7_,1);
    cStack_43 = SUB71(s___no_conversion_002a750a._8_7_,6);
    uVar5 = FUN_00bf81cc((ulong)&local_58 | 1);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_58);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
                    /* WARNING: Subroutine does not return */
    FUN_00c53f5c(uVar5);
  }
  local_57 = *puVar6;
  local_53 = *(undefined2 *)(puVar6 + 1);
  local_58 = 0x28;
  cStack_43 = 0;
  uStack_42 = 0;
  local_51._0_1_ = s___out_of_range_002b9dc6[0];
  local_51._1_1_ = s___out_of_range_002b9dc6[1];
  local_51._2_1_ = s___out_of_range_002b9dc6[2];
  local_51._3_1_ = s___out_of_range_002b9dc6[3];
  local_51._4_1_ = s___out_of_range_002b9dc6[4];
  local_51._5_1_ = s___out_of_range_002b9dc6[5];
  cStack_4b = (char)s___out_of_range_002b9dc6._6_2_;
  cStack_4a = SUB21(s___out_of_range_002b9dc6._6_2_,1);
  cStack_49 = (char)s___out_of_range_002b9dc6._8_6_;
  local_48 = SUB65(s___out_of_range_002b9dc6._8_6_,1);
                    /* WARNING: Subroutine does not return */
  FUN_00442930((ulong)&local_58 | 1);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf5bcc"></a> `00bf5bcc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf5bd0"></a> `00bf5bd0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bf5bd4"></a> `00bf5bd4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf5bd8"></a> `00bf5bd8` | `f7 23 00 f9` | str x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf5bdc"></a> `00bf5bdc` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf5be0"></a> `00bf5be0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf5be4"></a> `00bf5be4` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bf5be8"></a> `00bf5be8` | `69 8e 8e 52` | mov w9,#0x7473 | `FALL_THROUGH`
<a id="insn-00bf5bec"></a> `00bf5bec` | `88 01 80 52` | mov w8,#0xc | `FALL_THROUGH`
<a id="insn-00bf5bf0"></a> `00bf5bf0` | `0a 10 00 91` | add x10,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bf5bf4"></a> `00bf5bf4` | `e9 ad ae 72` | movk w9,#0x756f, LSL #16 | `FALL_THROUGH`
<a id="insn-00bf5bf8"></a> `00bf5bf8` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00bf5bfc"></a> `00bf5bfc` | `88 8d 8d 52` | mov w8,#0x6c6c | `FALL_THROUGH`
<a id="insn-00bf5c00"></a> `00bf5c00` | `e9 13 00 b8` | stur w9,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00bf5c04"></a> `00bf5c04` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bf5c08"></a> `00bf5c08` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bf5c0c"></a> `00bf5c0c` | `e8 53 00 78` | sturh w8,[sp, #0x5] | `FALL_THROUGH`
<a id="insn-00bf5c10"></a> `00bf5c10` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bf5c14"></a> `00bf5c14` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bf5c18"></a> `00bf5c18` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf5c1c"></a> `00bf5c1c` | `ff 1f 00 39` | strb wzr,[sp, #0x7] | `FALL_THROUGH`
<a id="insn-00bf5c20"></a> `00bf5c20` | `bf 0f 00 f9` | str xzr,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bf5c24"></a> `00bf5c24` | `54 01 88 9a` | csel x20,x10,x8,eq | `FALL_THROUGH`
<a id="insn-00bf5c28"></a> `00bf5c28` | `26 89 01 94` | bl 0x00c580c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf5c2c"></a> `00bf5c2c` | `17 00 40 b9` | ldr w23,[x0] | `FALL_THROUGH`
<a id="insn-00bf5c30"></a> `00bf5c30` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bf5c34"></a> `00bf5c34` | `1f 00 00 b9` | str wzr,[x0] | `FALL_THROUGH`
<a id="insn-00bf5c38"></a> `00bf5c38` | `a1 63 00 91` | add x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bf5c3c"></a> `00bf5c3c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bf5c40"></a> `00bf5c40` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bf5c44"></a> `00bf5c44` | `1f a1 01 94` | bl 0x00c5e0c0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf5c48"></a> `00bf5c48` | `c8 02 40 b9` | ldr w8,[x22] | `FALL_THROUGH`
<a id="insn-00bf5c4c"></a> `00bf5c4c` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-00bf5c50"></a> `00bf5c50` | `d7 02 00 b9` | str w23,[x22] | `FALL_THROUGH`
<a id="insn-00bf5c54"></a> `00bf5c54` | `1f 89 00 71` | cmp w8,#0x22 | `FALL_THROUGH`
<a id="insn-00bf5c58"></a> `00bf5c58` | `28 01 40 b2` | orr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf5c5c"></a> `00bf5c5c` | `40 02 00 54` | b.eq 0x00bf5ca4 | `CONDITIONAL_JUMP`
<a id="insn-00bf5c60"></a> `00bf5c60` | `a9 0f 40 f9` | ldr x9,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bf5c64"></a> `00bf5c64` | `29 01 14 eb` | subs x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00bf5c68"></a> `00bf5c68` | `e0 03 00 54` | b.eq 0x00bf5ce4 | `CONDITIONAL_JUMP`
<a id="insn-00bf5c6c"></a> `00bf5c6c` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bf5c70"></a> `00bf5c70` | `73 00 00 b4` | cbz x19,0x00bf5c7c | `CONDITIONAL_JUMP`
<a id="insn-00bf5c74"></a> `00bf5c74` | `28 fd 42 93` | asr x8,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bf5c78"></a> `00bf5c78` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bf5c7c"></a> `00bf5c7c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf5c80"></a> `00bf5c80` | `f4 a0 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bf5c84"></a> `00bf5c84` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bf5c88"></a> `00bf5c88` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf5c8c"></a> `00bf5c8c` | `f7 23 40 f9` | ldr x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf5c90"></a> `00bf5c90` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf5c94"></a> `00bf5c94` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf5c98"></a> `00bf5c98` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bf5c9c"></a> `00bf5c9c` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf5ca0"></a> `00bf5ca0` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf5ca4"></a> `00bf5ca4` | `09 05 80 52` | mov w9,#0x28 | `FALL_THROUGH`
<a id="insn-00bf5ca8"></a> `00bf5ca8` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00bf5cac"></a> `00bf5cac` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bf5cb0"></a> `00bf5cb0` | `e9 63 00 39` | strb w9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bf5cb4"></a> `00bf5cb4` | `29 b6 ff 90` | adrp x9,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bf5cb8"></a> `00bf5cb8` | `29 19 37 91` | add x9,x9,#0xdc6 | `FALL_THROUGH`
<a id="insn-00bf5cbc"></a> `00bf5cbc` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bf5cc0"></a> `00bf5cc0` | `e8 d3 01 78` | sturh w8,[sp, #0x1d] | `FALL_THROUGH`
<a id="insn-00bf5cc4"></a> `00bf5cc4` | `28 61 40 f8` | ldur x8,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00bf5cc8"></a> `00bf5cc8` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bf5ccc"></a> `00bf5ccc` | `e9 63 00 91` | add x9,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf5cd0"></a> `00bf5cd0` | `ea 93 01 b8` | stur w10,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00bf5cd4"></a> `00bf5cd4` | `eb f3 01 f8` | stur x11,[sp, #0x1f] | `FALL_THROUGH`
<a id="insn-00bf5cd8"></a> `00bf5cd8` | `e8 53 02 f8` | stur x8,[sp, #0x25] | `FALL_THROUGH`
<a id="insn-00bf5cdc"></a> `00bf5cdc` | `20 01 40 b2` | orr x0,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf5ce0"></a> `00bf5ce0` | `14 33 e1 97` | bl 0x00442930 | `CALL_TERMINATOR`
<a id="insn-00bf5ce4"></a> `00bf5ce4` | `49 05 80 52` | mov w9,#0x2a | `FALL_THROUGH`
<a id="insn-00bf5ce8"></a> `00bf5ce8` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00bf5cec"></a> `00bf5cec` | `08 09 40 79` | ldrh w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bf5cf0"></a> `00bf5cf0` | `e9 63 00 39` | strb w9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bf5cf4"></a> `00bf5cf4` | `89 b5 ff d0` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bf5cf8"></a> `00bf5cf8` | `29 29 14 91` | add x9,x9,#0x50a | `FALL_THROUGH`
<a id="insn-00bf5cfc"></a> `00bf5cfc` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bf5d00"></a> `00bf5d00` | `e8 d3 01 78` | sturh w8,[sp, #0x1d] | `FALL_THROUGH`
<a id="insn-00bf5d04"></a> `00bf5d04` | `28 71 40 f8` | ldur x8,[x9, #0x7] | `FALL_THROUGH`
<a id="insn-00bf5d08"></a> `00bf5d08` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bf5d0c"></a> `00bf5d0c` | `e9 63 00 91` | add x9,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf5d10"></a> `00bf5d10` | `ea 93 01 b8` | stur w10,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00bf5d14"></a> `00bf5d14` | `eb f3 01 f8` | stur x11,[sp, #0x1f] | `FALL_THROUGH`
<a id="insn-00bf5d18"></a> `00bf5d18` | `e8 63 02 f8` | stur x8,[sp, #0x26] | `FALL_THROUGH`
<a id="insn-00bf5d1c"></a> `00bf5d1c` | `20 01 40 b2` | orr x0,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf5d20"></a> `00bf5d20` | `2b 09 00 94` | bl 0x00bf81cc | `UNCONDITIONAL_CALL`
<a id="insn-00bf5d24"></a> `00bf5d24` | `01 00 00 14` | b 0x00bf5d28 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf5d28"></a> `00bf5d28` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bf5d2c"></a> `00bf5d2c` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf5d30"></a> `00bf5d30` | `c8 a0 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bf5d34"></a> `00bf5d34` | `02 00 00 14` | b 0x00bf5d3c | `UNCONDITIONAL_JUMP`
<a id="insn-00bf5d3c"></a> `00bf5d3c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf5d40"></a> `00bf5d40` | `c4 a0 01 94` | bl 0x00c5e050 | `UNCONDITIONAL_CALL`
<a id="insn-00bf5d44"></a> `00bf5d44` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bf5d48"></a> `00bf5d48` | `85 78 01 94` | bl 0x00c53f5c | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf5bcc`](#insn-00bf5bcc) 範囲 `[['00bf5bcc', '00bf5c5f']]`
  - `CONDITIONAL_JUMP` [`00bf5c5c`](#insn-00bf5c5c) → [`00bf5ca4`](#insn-00bf5ca4)
  - `FALL_THROUGH` [`00bf5c5c`](#insn-00bf5c5c) → [`00bf5c60`](#insn-00bf5c60)
- ブロック [`00bf5c60`](#insn-00bf5c60) 範囲 `[['00bf5c60', '00bf5c6b']]`
  - `CONDITIONAL_JUMP` [`00bf5c68`](#insn-00bf5c68) → [`00bf5ce4`](#insn-00bf5ce4)
  - `FALL_THROUGH` [`00bf5c68`](#insn-00bf5c68) → [`00bf5c6c`](#insn-00bf5c6c)
- ブロック [`00bf5c6c`](#insn-00bf5c6c) 範囲 `[['00bf5c6c', '00bf5c73']]`
  - `CONDITIONAL_JUMP` [`00bf5c70`](#insn-00bf5c70) → [`00bf5c7c`](#insn-00bf5c7c)
  - `FALL_THROUGH` [`00bf5c70`](#insn-00bf5c70) → [`00bf5c74`](#insn-00bf5c74)
- ブロック [`00bf5c74`](#insn-00bf5c74) 範囲 `[['00bf5c74', '00bf5c7b']]`
  - `FALL_THROUGH` [`00bf5c78`](#insn-00bf5c78) → [`00bf5c7c`](#insn-00bf5c7c)
- ブロック [`00bf5c7c`](#insn-00bf5c7c) 範囲 `[['00bf5c7c', '00bf5ca3']]`
- ブロック [`00bf5ca4`](#insn-00bf5ca4) 範囲 `[['00bf5ca4', '00bf5ce3']]`
- ブロック [`00bf5ce4`](#insn-00bf5ce4) 範囲 `[['00bf5ce4', '00bf5d27']]`
  - `UNCONDITIONAL_JUMP` [`00bf5d24`](#insn-00bf5d24) → [`00bf5d28`](#insn-00bf5d28)
- ブロック [`00bf5d28`](#insn-00bf5d28) 範囲 `[['00bf5d28', '00bf5d37']]`
  - `UNCONDITIONAL_JUMP` [`00bf5d34`](#insn-00bf5d34) → [`00bf5d3c`](#insn-00bf5d3c)
- ブロック [`00bf5d3c`](#insn-00bf5d3c) 範囲 `[['00bf5d3c', '00bf5d4b']]`

## 命令位置別の参照

- [`00bf5bd4`](#insn-00bf5bd4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5bd8`](#insn-00bf5bd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5bdc`](#insn-00bf5bdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5be0`](#insn-00bf5be0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5bf8`](#insn-00bf5bf8) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c00`](#insn-00bf5c00) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c0c`](#insn-00bf5c0c) → `Stack[-0x6b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c1c`](#insn-00bf5c1c) → `Stack[-0x69]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c20`](#insn-00bf5c20) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c28`](#insn-00bf5c28) → [`00c580c0`](../00c58/00c580c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c580c0` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c44`](#insn-00bf5c44) → [`00c5e0c0`](../00c5e/00c5e0c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e0c0` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c5c`](#insn-00bf5c5c) → [`00bf5ca4`](#insn-00bf5ca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c60`](#insn-00bf5c60) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c68`](#insn-00bf5c68) → [`00bf5ce4`](#insn-00bf5ce4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c70`](#insn-00bf5c70) → [`00bf5c7c`](#insn-00bf5c7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c80`](#insn-00bf5c80) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c88`](#insn-00bf5c88) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c8c`](#insn-00bf5c8c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c90`](#insn-00bf5c90) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c94`](#insn-00bf5c94) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5cb0`](#insn-00bf5cb0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5cbc`](#insn-00bf5cbc) → `002b9dc6`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf5cc0`](#insn-00bf5cc0) → `Stack[-0x53]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5cc4`](#insn-00bf5cc4) → `002b9dcc`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf5cc8`](#insn-00bf5cc8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5cd0`](#insn-00bf5cd0) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5cd4`](#insn-00bf5cd4) → `Stack[-0x51]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5cd8`](#insn-00bf5cd8) → `Stack[-0x4b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5ce0`](#insn-00bf5ce0) → [`00442930`](../00442/00442930.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00442930` · 推定シンボル `None` · 推定型 `None`
- [`00bf5cf0`](#insn-00bf5cf0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5cfc`](#insn-00bf5cfc) → `002a750a`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf5d00`](#insn-00bf5d00) → `Stack[-0x53]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5d04`](#insn-00bf5d04) → `002a7511`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf5d08`](#insn-00bf5d08) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5d10`](#insn-00bf5d10) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5d14`](#insn-00bf5d14) → `Stack[-0x51]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5d18`](#insn-00bf5d18) → `Stack[-0x4a]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5d20`](#insn-00bf5d20) → [`00bf81cc`](../00bf8/00bf81cc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bf81cc` · 推定シンボル `None` · 推定型 `None`
- [`00bf5d24`](#insn-00bf5d24) → [`00bf5d28`](#insn-00bf5d28) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5d30`](#insn-00bf5d30) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bf5d34`](#insn-00bf5d34) → [`00bf5d3c`](#insn-00bf5d3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5d40`](#insn-00bf5d40) → [`00c5e050`](../00c5e/00c5e050.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e050` · 推定シンボル `None` · 推定型 `None`
- [`00bf5d48`](#insn-00bf5d48) → [`00c53f5c`](../00c53/00c53f5c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53f5c` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf5bd4`](#insn-00bf5bd4)

~~~json
{
  "source": "00bf5bd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5bd8`](#insn-00bf5bd8)

~~~json
{
  "source": "00bf5bd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5bdc`](#insn-00bf5bdc)

~~~json
{
  "source": "00bf5bdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5be0`](#insn-00bf5be0)

~~~json
{
  "source": "00bf5be0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5bf8`](#insn-00bf5bf8)

~~~json
{
  "source": "00bf5bf8",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c00`](#insn-00bf5c00)

~~~json
{
  "source": "00bf5c00",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c0c`](#insn-00bf5c0c)

~~~json
{
  "source": "00bf5c0c",
  "target": "Stack[-0x6b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c1c`](#insn-00bf5c1c)

~~~json
{
  "source": "00bf5c1c",
  "target": "Stack[-0x69]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c20`](#insn-00bf5c20)

~~~json
{
  "source": "00bf5c20",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c28`](#insn-00bf5c28)

~~~json
{
  "source": "00bf5c28",
  "target": "00c580c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5c44`](#insn-00bf5c44)

~~~json
{
  "source": "00bf5c44",
  "target": "00c5e0c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5c5c`](#insn-00bf5c5c)

~~~json
{
  "source": "00bf5c5c",
  "target": "00bf5ca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c60`](#insn-00bf5c60)

~~~json
{
  "source": "00bf5c60",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c68`](#insn-00bf5c68)

~~~json
{
  "source": "00bf5c68",
  "target": "00bf5ce4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c70`](#insn-00bf5c70)

~~~json
{
  "source": "00bf5c70",
  "target": "00bf5c7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c80`](#insn-00bf5c80)

~~~json
{
  "source": "00bf5c80",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5c88`](#insn-00bf5c88)

~~~json
{
  "source": "00bf5c88",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c8c`](#insn-00bf5c8c)

~~~json
{
  "source": "00bf5c8c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c90`](#insn-00bf5c90)

~~~json
{
  "source": "00bf5c90",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c94`](#insn-00bf5c94)

~~~json
{
  "source": "00bf5c94",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5cb0`](#insn-00bf5cb0)

~~~json
{
  "source": "00bf5cb0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5cbc`](#insn-00bf5cbc)

~~~json
{
  "source": "00bf5cbc",
  "target": "002b9dc6",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9dc6",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "3a206f7574206f662072616e676500",
  "capture_start": "002b9dc6",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf5cc0`](#insn-00bf5cc0)

~~~json
{
  "source": "00bf5cc0",
  "target": "Stack[-0x53]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5cc4`](#insn-00bf5cc4)

~~~json
{
  "source": "00bf5cc4",
  "target": "002b9dcc",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9dc6",
  "offset": 6,
  "size": 15,
  "datatype": "string",
  "bytes": "3a206f7574206f662072616e676500",
  "capture_start": "002b9dc6",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf5cc8`](#insn-00bf5cc8)

~~~json
{
  "source": "00bf5cc8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5cd0`](#insn-00bf5cd0)

~~~json
{
  "source": "00bf5cd0",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5cd4`](#insn-00bf5cd4)

~~~json
{
  "source": "00bf5cd4",
  "target": "Stack[-0x51]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5cd8`](#insn-00bf5cd8)

~~~json
{
  "source": "00bf5cd8",
  "target": "Stack[-0x4b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5ce0`](#insn-00bf5ce0)

~~~json
{
  "source": "00bf5ce0",
  "target": "00442930",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5cf0`](#insn-00bf5cf0)

~~~json
{
  "source": "00bf5cf0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5cfc`](#insn-00bf5cfc)

~~~json
{
  "source": "00bf5cfc",
  "target": "002a750a",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a750a",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "3a206e6f20636f6e76657273696f6e00",
  "capture_start": "002a750a",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf5d00`](#insn-00bf5d00)

~~~json
{
  "source": "00bf5d00",
  "target": "Stack[-0x53]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5d04`](#insn-00bf5d04)

~~~json
{
  "source": "00bf5d04",
  "target": "002a7511",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a750a",
  "offset": 7,
  "size": 16,
  "datatype": "string",
  "bytes": "3a206e6f20636f6e76657273696f6e00",
  "capture_start": "002a750a",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf5d08`](#insn-00bf5d08)

~~~json
{
  "source": "00bf5d08",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5d10`](#insn-00bf5d10)

~~~json
{
  "source": "00bf5d10",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5d14`](#insn-00bf5d14)

~~~json
{
  "source": "00bf5d14",
  "target": "Stack[-0x51]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5d18`](#insn-00bf5d18)

~~~json
{
  "source": "00bf5d18",
  "target": "Stack[-0x4a]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5d20`](#insn-00bf5d20)

~~~json
{
  "source": "00bf5d20",
  "target": "00bf81cc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5d24`](#insn-00bf5d24)

~~~json
{
  "source": "00bf5d24",
  "target": "00bf5d28",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5d30`](#insn-00bf5d30)

~~~json
{
  "source": "00bf5d30",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5d34`](#insn-00bf5d34)

~~~json
{
  "source": "00bf5d34",
  "target": "00bf5d3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5d40`](#insn-00bf5d40)

~~~json
{
  "source": "00bf5d40",
  "target": "00c5e050",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5d48`](#insn-00bf5d48)

~~~json
{
  "source": "00bf5d48",
  "target": "00c53f5c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
