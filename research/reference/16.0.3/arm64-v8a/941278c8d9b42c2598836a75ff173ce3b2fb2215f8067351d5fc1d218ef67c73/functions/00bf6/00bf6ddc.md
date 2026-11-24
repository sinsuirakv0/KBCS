# 00bf6ddc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bf5de8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bf5/00bf5de8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-9df35b9843d01e30d6e1d67c64b92d89)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf6ddc",
  "name": "_ZNSt6__ndk14stofERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm",
  "size": 340,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "a3f6598fb80373758f55951a343be7fcc0d3982ec2dcd5dbaadd0c6d3f3bb992",
  "source_text_sha256": "a3f6598fb80373758f55951a343be7fcc0d3982ec2dcd5dbaadd0c6d3f3bb992",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf6ddc",
        "00bf6f1f"
      ],
      [
        "00bf6f24",
        "00bf6f33"
      ]
    ],
    "bytes_sha256": "dcaf19ccbc4802e5e7223d68a9adb7020be1a3b2a88ed2db84b47876b209b3c6",
    "instruction_count": 85,
    "instruction_bytes": 340,
    "body_bytes": 340,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00442c90](../00442/00442c90.md)
- [00bf925c](../00bf9/00bf925c.md)
- [00c54fec](../00c54/00c54fec.md)
- [00c59160](../00c59/00c59160.md)
- [00c5f0f0](../00c5f/00c5f0f0.md)
- [00c5f170](../00c5f/00c5f170.md)

## 関連文字列（未確認候補）

~~~text
": no conversion"
": out of range"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2453 bytes

~~~c

float _ZNSt6__ndk14stofERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPm
                (byte *param_1,long *param_2)

{
  wchar_t *__nptr;
  int iVar1;
  int iVar2;
  int *piVar3;
  undefined8 uVar4;
  float fVar5;
  undefined1 local_70;
  undefined4 local_6f;
  undefined1 local_6b;
  undefined1 local_58;
  undefined4 local_57;
  undefined6 local_53;
  char cStack_4d;
  undefined4 uStack_4c;
  uint local_48;
  undefined4 uStack_44;
  wchar_t *local_38;
  
  local_70 = 8;
  local_6b = 0;
  local_6f = 0x666f7473;
  local_38 = (wchar_t *)0x0;
  __nptr = (wchar_t *)(param_1 + 4);
  if ((*param_1 & 1) != 0) {
    __nptr = *(wchar_t **)(param_1 + 0x10);
  }
  piVar3 = (int *)__errno();
  iVar1 = *piVar3;
  *piVar3 = 0;
  fVar5 = wcstof(__nptr,&local_38);
  iVar2 = *piVar3;
  *piVar3 = iVar1;
  if (iVar2 != 0x22) {
    if ((long)local_38 - (long)__nptr != 0) {
      if (param_2 != (long *)0x0) {
        *param_2 = (long)local_38 - (long)__nptr >> 2;
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
      return fVar5;
    }
    local_58 = 0x26;
    uStack_44 = 0;
    local_57 = local_6f;
    local_53 = (undefined6)s___no_conversion_002a7606._0_7_;
    cStack_4d = SUB71(s___no_conversion_002a7606._0_7_,6);
    uStack_4c = (undefined4)CONCAT71(s___no_conversion_002a7606._8_7_,s___no_conversion_002a7606[7])
    ;
    local_48 = SUB74(s___no_conversion_002a7606._8_7_,3);
    uVar4 = FUN_00bf925c((ulong)&local_58 | 1);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_58);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
                    /* WARNING: Subroutine does not return */
    FUN_00c54fec(uVar4);
  }
  local_58 = 0x24;
  uStack_44 = 0;
  local_57 = local_6f;
  local_53._0_1_ = s___out_of_range_002b9e50[0];
  local_53._1_1_ = s___out_of_range_002b9e50[1];
  local_53._2_1_ = s___out_of_range_002b9e50[2];
  local_53._3_1_ = s___out_of_range_002b9e50[3];
  local_53._4_1_ = s___out_of_range_002b9e50[4];
  local_53._5_1_ = s___out_of_range_002b9e50[5];
  cStack_4d = (char)s___out_of_range_002b9e50._6_2_;
  uStack_4c = (undefined4)
              (CONCAT62(s___out_of_range_002b9e50._8_6_,s___out_of_range_002b9e50._6_2_) >> 8);
  local_48 = (uint)SUB63(s___out_of_range_002b9e50._8_6_,3);
                    /* WARNING: Subroutine does not return */
  FUN_00442c90((ulong)&local_58 | 1);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf6ddc"></a> `00bf6ddc` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf6de0"></a> `00bf6de0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bf6de4"></a> `00bf6de4` | `e8 1b 00 fd` | str d8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf6de8"></a> `00bf6de8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf6dec"></a> `00bf6dec` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf6df0"></a> `00bf6df0` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf6df4"></a> `00bf6df4` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00bf6df8"></a> `00bf6df8` | `08 01 80 52` | mov w8,#0x8 | `FALL_THROUGH`
<a id="insn-00bf6dfc"></a> `00bf6dfc` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bf6e00"></a> `00bf6e00` | `0a 10 00 91` | add x10,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bf6e04"></a> `00bf6e04` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00bf6e08"></a> `00bf6e08` | `68 8e 8e 52` | mov w8,#0x7473 | `FALL_THROUGH`
<a id="insn-00bf6e0c"></a> `00bf6e0c` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bf6e10"></a> `00bf6e10` | `e8 cd ac 72` | movk w8,#0x666f, LSL #16 | `FALL_THROUGH`
<a id="insn-00bf6e14"></a> `00bf6e14` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf6e18"></a> `00bf6e18` | `ff 17 00 39` | strb wzr,[sp, #0x5] | `FALL_THROUGH`
<a id="insn-00bf6e1c"></a> `00bf6e1c` | `e8 13 00 b8` | stur w8,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00bf6e20"></a> `00bf6e20` | `08 08 40 f9` | ldr x8,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bf6e24"></a> `00bf6e24` | `bf 83 1f f8` | stur xzr,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bf6e28"></a> `00bf6e28` | `54 01 88 9a` | csel x20,x10,x8,eq | `FALL_THROUGH`
<a id="insn-00bf6e2c"></a> `00bf6e2c` | `cd 88 01 94` | bl 0x00c59160 | `UNCONDITIONAL_CALL`
<a id="insn-00bf6e30"></a> `00bf6e30` | `16 00 40 b9` | ldr w22,[x0] | `FALL_THROUGH`
<a id="insn-00bf6e34"></a> `00bf6e34` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bf6e38"></a> `00bf6e38` | `1f 00 00 b9` | str wzr,[x0] | `FALL_THROUGH`
<a id="insn-00bf6e3c"></a> `00bf6e3c` | `a1 23 00 d1` | sub x1,x29,#0x8 | `FALL_THROUGH`
<a id="insn-00bf6e40"></a> `00bf6e40` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bf6e44"></a> `00bf6e44` | `cb a0 01 94` | bl 0x00c5f170 | `UNCONDITIONAL_CALL`
<a id="insn-00bf6e48"></a> `00bf6e48` | `a8 02 40 b9` | ldr w8,[x21] | `FALL_THROUGH`
<a id="insn-00bf6e4c"></a> `00bf6e4c` | `b6 02 00 b9` | str w22,[x21] | `FALL_THROUGH`
<a id="insn-00bf6e50"></a> `00bf6e50` | `1f 89 00 71` | cmp w8,#0x22 | `FALL_THROUGH`
<a id="insn-00bf6e54"></a> `00bf6e54` | `40 02 00 54` | b.eq 0x00bf6e9c | `CONDITIONAL_JUMP`
<a id="insn-00bf6e58"></a> `00bf6e58` | `a8 83 5f f8` | ldur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00bf6e5c"></a> `00bf6e5c` | `08 01 14 eb` | subs x8,x8,x20 | `FALL_THROUGH`
<a id="insn-00bf6e60"></a> `00bf6e60` | `a0 03 00 54` | b.eq 0x00bf6ed4 | `CONDITIONAL_JUMP`
<a id="insn-00bf6e64"></a> `00bf6e64` | `08 40 20 1e` | fmov s8,s0 | `FALL_THROUGH`
<a id="insn-00bf6e68"></a> `00bf6e68` | `73 00 00 b4` | cbz x19,0x00bf6e74 | `CONDITIONAL_JUMP`
<a id="insn-00bf6e6c"></a> `00bf6e6c` | `08 fd 42 93` | asr x8,x8,#0x2 | `FALL_THROUGH`
<a id="insn-00bf6e70"></a> `00bf6e70` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bf6e74"></a> `00bf6e74` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf6e78"></a> `00bf6e78` | `9e a0 01 94` | bl 0x00c5f0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf6e7c"></a> `00bf6e7c` | `00 41 20 1e` | fmov s0,s8 | `FALL_THROUGH`
<a id="insn-00bf6e80"></a> `00bf6e80` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf6e84"></a> `00bf6e84` | `e8 1b 40 fd` | ldr d8,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf6e88"></a> `00bf6e88` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf6e8c"></a> `00bf6e8c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf6e90"></a> `00bf6e90` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bf6e94"></a> `00bf6e94` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf6e98"></a> `00bf6e98` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf6e9c"></a> `00bf6e9c` | `88 04 80 52` | mov w8,#0x24 | `FALL_THROUGH`
<a id="insn-00bf6ea0"></a> `00bf6ea0` | `0a b6 ff f0` | adrp x10,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bf6ea4"></a> `00bf6ea4` | `4a 41 39 91` | add x10,x10,#0xe50 | `FALL_THROUGH`
<a id="insn-00bf6ea8"></a> `00bf6ea8` | `e9 13 40 b8` | ldur w9,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00bf6eac"></a> `00bf6eac` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bf6eb0"></a> `00bf6eb0` | `48 01 40 f9` | ldr x8,[x10] | `FALL_THROUGH`
<a id="insn-00bf6eb4"></a> `00bf6eb4` | `4a 61 40 f8` | ldur x10,[x10, #0x6] | `FALL_THROUGH`
<a id="insn-00bf6eb8"></a> `00bf6eb8` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bf6ebc"></a> `00bf6ebc` | `e9 93 01 b8` | stur w9,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00bf6ec0"></a> `00bf6ec0` | `e8 d3 01 f8` | stur x8,[sp, #0x1d] | `FALL_THROUGH`
<a id="insn-00bf6ec4"></a> `00bf6ec4` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf6ec8"></a> `00bf6ec8` | `ea 33 02 f8` | stur x10,[sp, #0x23] | `FALL_THROUGH`
<a id="insn-00bf6ecc"></a> `00bf6ecc` | `00 01 40 b2` | orr x0,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf6ed0"></a> `00bf6ed0` | `70 2f e1 97` | bl 0x00442c90 | `CALL_TERMINATOR`
<a id="insn-00bf6ed4"></a> `00bf6ed4` | `c8 04 80 52` | mov w8,#0x26 | `FALL_THROUGH`
<a id="insn-00bf6ed8"></a> `00bf6ed8` | `8a b5 ff b0` | adrp x10,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bf6edc"></a> `00bf6edc` | `4a 19 18 91` | add x10,x10,#0x606 | `FALL_THROUGH`
<a id="insn-00bf6ee0"></a> `00bf6ee0` | `e9 13 40 b8` | ldur w9,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00bf6ee4"></a> `00bf6ee4` | `e8 63 00 39` | strb w8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bf6ee8"></a> `00bf6ee8` | `48 01 40 f9` | ldr x8,[x10] | `FALL_THROUGH`
<a id="insn-00bf6eec"></a> `00bf6eec` | `4a 71 40 f8` | ldur x10,[x10, #0x7] | `FALL_THROUGH`
<a id="insn-00bf6ef0"></a> `00bf6ef0` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bf6ef4"></a> `00bf6ef4` | `e9 93 01 b8` | stur w9,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00bf6ef8"></a> `00bf6ef8` | `e8 d3 01 f8` | stur x8,[sp, #0x1d] | `FALL_THROUGH`
<a id="insn-00bf6efc"></a> `00bf6efc` | `e8 63 00 91` | add x8,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf6f00"></a> `00bf6f00` | `ea 43 02 f8` | stur x10,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00bf6f04"></a> `00bf6f04` | `00 01 40 b2` | orr x0,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00bf6f08"></a> `00bf6f08` | `d5 08 00 94` | bl 0x00bf925c | `UNCONDITIONAL_CALL`
<a id="insn-00bf6f0c"></a> `00bf6f0c` | `01 00 00 14` | b 0x00bf6f10 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf6f10"></a> `00bf6f10` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bf6f14"></a> `00bf6f14` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf6f18"></a> `00bf6f18` | `76 a0 01 94` | bl 0x00c5f0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf6f1c"></a> `00bf6f1c` | `02 00 00 14` | b 0x00bf6f24 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf6f24"></a> `00bf6f24` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf6f28"></a> `00bf6f28` | `72 a0 01 94` | bl 0x00c5f0f0 | `UNCONDITIONAL_CALL`
<a id="insn-00bf6f2c"></a> `00bf6f2c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bf6f30"></a> `00bf6f30` | `2f 78 01 94` | bl 0x00c54fec | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf6ddc`](#insn-00bf6ddc) 範囲 `[['00bf6ddc', '00bf6e57']]`
  - `CONDITIONAL_JUMP` [`00bf6e54`](#insn-00bf6e54) → [`00bf6e9c`](#insn-00bf6e9c)
  - `FALL_THROUGH` [`00bf6e54`](#insn-00bf6e54) → [`00bf6e58`](#insn-00bf6e58)
- ブロック [`00bf6e58`](#insn-00bf6e58) 範囲 `[['00bf6e58', '00bf6e63']]`
  - `CONDITIONAL_JUMP` [`00bf6e60`](#insn-00bf6e60) → [`00bf6ed4`](#insn-00bf6ed4)
  - `FALL_THROUGH` [`00bf6e60`](#insn-00bf6e60) → [`00bf6e64`](#insn-00bf6e64)
- ブロック [`00bf6e64`](#insn-00bf6e64) 範囲 `[['00bf6e64', '00bf6e6b']]`
  - `CONDITIONAL_JUMP` [`00bf6e68`](#insn-00bf6e68) → [`00bf6e74`](#insn-00bf6e74)
  - `FALL_THROUGH` [`00bf6e68`](#insn-00bf6e68) → [`00bf6e6c`](#insn-00bf6e6c)
- ブロック [`00bf6e6c`](#insn-00bf6e6c) 範囲 `[['00bf6e6c', '00bf6e73']]`
  - `FALL_THROUGH` [`00bf6e70`](#insn-00bf6e70) → [`00bf6e74`](#insn-00bf6e74)
- ブロック [`00bf6e74`](#insn-00bf6e74) 範囲 `[['00bf6e74', '00bf6e9b']]`
- ブロック [`00bf6e9c`](#insn-00bf6e9c) 範囲 `[['00bf6e9c', '00bf6ed3']]`
- ブロック [`00bf6ed4`](#insn-00bf6ed4) 範囲 `[['00bf6ed4', '00bf6f0f']]`
  - `UNCONDITIONAL_JUMP` [`00bf6f0c`](#insn-00bf6f0c) → [`00bf6f10`](#insn-00bf6f10)
- ブロック [`00bf6f10`](#insn-00bf6f10) 範囲 `[['00bf6f10', '00bf6f1f']]`
  - `UNCONDITIONAL_JUMP` [`00bf6f1c`](#insn-00bf6f1c) → [`00bf6f24`](#insn-00bf6f24)
- ブロック [`00bf6f24`](#insn-00bf6f24) 範囲 `[['00bf6f24', '00bf6f33']]`

## 命令位置別の参照

- [`00bf6de4`](#insn-00bf6de4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6de8`](#insn-00bf6de8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6dec`](#insn-00bf6dec) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6df0`](#insn-00bf6df0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e04`](#insn-00bf6e04) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e18`](#insn-00bf6e18) → `Stack[-0x6b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e1c`](#insn-00bf6e1c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e24`](#insn-00bf6e24) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e2c`](#insn-00bf6e2c) → [`00c59160`](../00c59/00c59160.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c59160` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e44`](#insn-00bf6e44) → [`00c5f170`](../00c5f/00c5f170.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f170` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e54`](#insn-00bf6e54) → [`00bf6e9c`](#insn-00bf6e9c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e58`](#insn-00bf6e58) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e60`](#insn-00bf6e60) → [`00bf6ed4`](#insn-00bf6ed4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e68`](#insn-00bf6e68) → [`00bf6e74`](#insn-00bf6e74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e78`](#insn-00bf6e78) → [`00c5f0f0`](../00c5f/00c5f0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e80`](#insn-00bf6e80) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e84`](#insn-00bf6e84) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e88`](#insn-00bf6e88) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6e8c`](#insn-00bf6e8c) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6ea8`](#insn-00bf6ea8) → `Stack[-0x6f]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6eac`](#insn-00bf6eac) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6eb0`](#insn-00bf6eb0) → `002b9e50`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf6eb4`](#insn-00bf6eb4) → `002b9e56`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf6eb8`](#insn-00bf6eb8) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6ebc`](#insn-00bf6ebc) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6ec0`](#insn-00bf6ec0) → `Stack[-0x53]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6ec8`](#insn-00bf6ec8) → `Stack[-0x4d]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6ed0`](#insn-00bf6ed0) → [`00442c90`](../00442/00442c90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00442c90` · 推定シンボル `None` · 推定型 `None`
- [`00bf6ee0`](#insn-00bf6ee0) → `Stack[-0x6f]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6ee4`](#insn-00bf6ee4) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6ee8`](#insn-00bf6ee8) → `002a7606`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf6eec`](#insn-00bf6eec) → `002a760d`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf6ef0`](#insn-00bf6ef0) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6ef4`](#insn-00bf6ef4) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6ef8`](#insn-00bf6ef8) → `Stack[-0x53]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6f00`](#insn-00bf6f00) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6f08`](#insn-00bf6f08) → [`00bf925c`](../00bf9/00bf925c.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bf925c` · 推定シンボル `None` · 推定型 `None`
- [`00bf6f0c`](#insn-00bf6f0c) → [`00bf6f10`](#insn-00bf6f10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6f18`](#insn-00bf6f18) → [`00c5f0f0`](../00c5f/00c5f0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bf6f1c`](#insn-00bf6f1c) → [`00bf6f24`](#insn-00bf6f24) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf6f28`](#insn-00bf6f28) → [`00c5f0f0`](../00c5f/00c5f0f0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5f0f0` · 推定シンボル `None` · 推定型 `None`
- [`00bf6f30`](#insn-00bf6f30) → [`00c54fec`](../00c54/00c54fec.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c54fec` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf6de4`](#insn-00bf6de4)

~~~json
{
  "source": "00bf6de4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6de8`](#insn-00bf6de8)

~~~json
{
  "source": "00bf6de8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6dec`](#insn-00bf6dec)

~~~json
{
  "source": "00bf6dec",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6df0`](#insn-00bf6df0)

~~~json
{
  "source": "00bf6df0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e04`](#insn-00bf6e04)

~~~json
{
  "source": "00bf6e04",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e18`](#insn-00bf6e18)

~~~json
{
  "source": "00bf6e18",
  "target": "Stack[-0x6b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e1c`](#insn-00bf6e1c)

~~~json
{
  "source": "00bf6e1c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e24`](#insn-00bf6e24)

~~~json
{
  "source": "00bf6e24",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e2c`](#insn-00bf6e2c)

~~~json
{
  "source": "00bf6e2c",
  "target": "00c59160",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf6e44`](#insn-00bf6e44)

~~~json
{
  "source": "00bf6e44",
  "target": "00c5f170",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf6e54`](#insn-00bf6e54)

~~~json
{
  "source": "00bf6e54",
  "target": "00bf6e9c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e58`](#insn-00bf6e58)

~~~json
{
  "source": "00bf6e58",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e60`](#insn-00bf6e60)

~~~json
{
  "source": "00bf6e60",
  "target": "00bf6ed4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e68`](#insn-00bf6e68)

~~~json
{
  "source": "00bf6e68",
  "target": "00bf6e74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e78`](#insn-00bf6e78)

~~~json
{
  "source": "00bf6e78",
  "target": "00c5f0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf6e80`](#insn-00bf6e80)

~~~json
{
  "source": "00bf6e80",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e84`](#insn-00bf6e84)

~~~json
{
  "source": "00bf6e84",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e88`](#insn-00bf6e88)

~~~json
{
  "source": "00bf6e88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6e8c`](#insn-00bf6e8c)

~~~json
{
  "source": "00bf6e8c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6ea8`](#insn-00bf6ea8)

~~~json
{
  "source": "00bf6ea8",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6eac`](#insn-00bf6eac)

~~~json
{
  "source": "00bf6eac",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6eb0`](#insn-00bf6eb0)

~~~json
{
  "source": "00bf6eb0",
  "target": "002b9e50",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9e50",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "3a206f7574206f662072616e676500",
  "capture_start": "002b9e50",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf6eb4`](#insn-00bf6eb4)

~~~json
{
  "source": "00bf6eb4",
  "target": "002b9e56",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9e50",
  "offset": 6,
  "size": 15,
  "datatype": "string",
  "bytes": "3a206f7574206f662072616e676500",
  "capture_start": "002b9e50",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf6eb8`](#insn-00bf6eb8)

~~~json
{
  "source": "00bf6eb8",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6ebc`](#insn-00bf6ebc)

~~~json
{
  "source": "00bf6ebc",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6ec0`](#insn-00bf6ec0)

~~~json
{
  "source": "00bf6ec0",
  "target": "Stack[-0x53]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6ec8`](#insn-00bf6ec8)

~~~json
{
  "source": "00bf6ec8",
  "target": "Stack[-0x4d]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6ed0`](#insn-00bf6ed0)

~~~json
{
  "source": "00bf6ed0",
  "target": "00442c90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf6ee0`](#insn-00bf6ee0)

~~~json
{
  "source": "00bf6ee0",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6ee4`](#insn-00bf6ee4)

~~~json
{
  "source": "00bf6ee4",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6ee8`](#insn-00bf6ee8)

~~~json
{
  "source": "00bf6ee8",
  "target": "002a7606",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7606",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "3a206e6f20636f6e76657273696f6e00",
  "capture_start": "002a7606",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf6eec`](#insn-00bf6eec)

~~~json
{
  "source": "00bf6eec",
  "target": "002a760d",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a7606",
  "offset": 7,
  "size": 16,
  "datatype": "string",
  "bytes": "3a206e6f20636f6e76657273696f6e00",
  "capture_start": "002a7606",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf6ef0`](#insn-00bf6ef0)

~~~json
{
  "source": "00bf6ef0",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6ef4`](#insn-00bf6ef4)

~~~json
{
  "source": "00bf6ef4",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6ef8`](#insn-00bf6ef8)

~~~json
{
  "source": "00bf6ef8",
  "target": "Stack[-0x53]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6f00`](#insn-00bf6f00)

~~~json
{
  "source": "00bf6f00",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6f08`](#insn-00bf6f08)

~~~json
{
  "source": "00bf6f08",
  "target": "00bf925c",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf6f0c`](#insn-00bf6f0c)

~~~json
{
  "source": "00bf6f0c",
  "target": "00bf6f10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6f18`](#insn-00bf6f18)

~~~json
{
  "source": "00bf6f18",
  "target": "00c5f0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf6f1c`](#insn-00bf6f1c)

~~~json
{
  "source": "00bf6f1c",
  "target": "00bf6f24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf6f28`](#insn-00bf6f28)

~~~json
{
  "source": "00bf6f28",
  "target": "00c5f0f0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf6f30`](#insn-00bf6f30)

~~~json
{
  "source": "00bf6f30",
  "target": "00c54fec",
  "target_space": "ram",
  "resolution": "function"
}
~~~
