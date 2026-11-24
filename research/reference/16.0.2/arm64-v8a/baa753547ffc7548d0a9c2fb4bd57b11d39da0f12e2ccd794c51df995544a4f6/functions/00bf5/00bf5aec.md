# 00bf5aec

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00bf5a50`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00bf5/00bf5a50.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0086.md#compare-bc1566ce1b2982c552352392fc2155cd)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00bf6ae0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00bf6/00bf6ae0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/priority-0086.md#compare-e2008ba44a305fab2761b08ba374dd3b)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bf5aec",
  "name": "_ZNSt6__ndk15stollERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi",
  "size": 376,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "9d17a3ab785391b8d5067f2980ee5aaf51c889a7badc7464ea01a8cae55e6d2b",
  "source_text_sha256": "9d17a3ab785391b8d5067f2980ee5aaf51c889a7badc7464ea01a8cae55e6d2b",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bf5aec",
        "00bf5c53"
      ],
      [
        "00bf5c58",
        "00bf5c67"
      ]
    ],
    "bytes_sha256": "d43c61d2c05e10b9e4105f797193bd65f08f7ef9857835c7a777429273030d94",
    "instruction_count": 94,
    "instruction_bytes": 376,
    "body_bytes": 376,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00442970](../00442/00442970.md)
- [00bf8268](../00bf8/00bf8268.md)
- [00c53ffc](../00c53/00c53ffc.md)
- [00c58190](../00c58/00c58190.md)
- [00c5e120](../00c5e/00c5e120.md)
- [00c5e180](../00c5e/00c5e180.md)

## 関連文字列（未確認候補）

~~~text
": no conversion"
": out of range"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2719 bytes

~~~c

longlong _ZNSt6__ndk15stollERKNS_12basic_stringIwNS_11char_traitsIwEENS_9allocatorIwEEEEPmi
                   (byte *param_1,long *param_2,int param_3)

{
  wchar_t *__nptr;
  int iVar1;
  int iVar2;
  int *piVar3;
  longlong lVar4;
  undefined8 uVar5;
  undefined4 *puVar6;
  undefined1 local_70;
  undefined4 local_6f;
  undefined2 local_6b;
  undefined1 local_58;
  undefined4 local_57;
  undefined1 local_53;
  undefined6 local_52;
  char cStack_4c;
  char cStack_4b;
  undefined2 uStack_4a;
  undefined4 local_48;
  uint uStack_44;
  wchar_t *local_28;
  
  local_70 = 10;
  local_6f = 0x6c6f7473;
  local_6b = 0x6c;
  local_28 = (wchar_t *)0x0;
  __nptr = (wchar_t *)(param_1 + 4);
  if ((*param_1 & 1) != 0) {
    __nptr = *(wchar_t **)(param_1 + 0x10);
  }
  piVar3 = (int *)__errno();
  iVar1 = *piVar3;
  *piVar3 = 0;
  lVar4 = wcstoll(__nptr,&local_28,param_3);
  iVar2 = *piVar3;
  *piVar3 = iVar1;
  puVar6 = (undefined4 *)((ulong)&local_70 | 1);
  if (iVar2 != 0x22) {
    if ((long)local_28 - (long)__nptr != 0) {
      if (param_2 != (long *)0x0) {
        *param_2 = (long)local_28 - (long)__nptr >> 2;
      }
      _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
      return lVar4;
    }
    local_57 = *puVar6;
    local_53 = *(undefined1 *)(puVar6 + 1);
    local_58 = 0x28;
    local_52 = (undefined6)s___no_conversion_002a74ae._0_7_;
    cStack_4c = SUB71(s___no_conversion_002a74ae._0_7_,6);
    cStack_4b = s___no_conversion_002a74ae[7];
    uStack_4a = (undefined2)s___no_conversion_002a74ae._8_7_;
    local_48 = SUB74(s___no_conversion_002a74ae._8_7_,2);
    uStack_44 = (uint)SUB71(s___no_conversion_002a74ae._8_7_,6);
    uVar5 = FUN_00bf8268((ulong)&local_58 | 1);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_58);
    _ZNSt6__ndk112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev(&local_70);
                    /* WARNING: Subroutine does not return */
    FUN_00c53ffc(uVar5);
  }
  local_57 = *puVar6;
  local_53 = *(undefined1 *)(puVar6 + 1);
  local_58 = 0x26;
  uStack_44 = 0;
  local_52._0_1_ = s___out_of_range_002b9d72[0];
  local_52._1_1_ = s___out_of_range_002b9d72[1];
  local_52._2_1_ = s___out_of_range_002b9d72[2];
  local_52._3_1_ = s___out_of_range_002b9d72[3];
  local_52._4_1_ = s___out_of_range_002b9d72[4];
  local_52._5_1_ = s___out_of_range_002b9d72[5];
  cStack_4c = (char)s___out_of_range_002b9d72._6_2_;
  cStack_4b = SUB21(s___out_of_range_002b9d72._6_2_,1);
  uStack_4a = (undefined2)s___out_of_range_002b9d72._8_6_;
  local_48 = SUB64(s___out_of_range_002b9d72._8_6_,2);
                    /* WARNING: Subroutine does not return */
  FUN_00442970((ulong)&local_58 | 1);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00bf5aec"></a> `00bf5aec` | `3f 23 03 d5` | paciasp | `FALL_THROUGH`
<a id="insn-00bf5af0"></a> `00bf5af0` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bf5af4"></a> `00bf5af4` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf5af8"></a> `00bf5af8` | `f7 23 00 f9` | str x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf5afc"></a> `00bf5afc` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf5b00"></a> `00bf5b00` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf5b04"></a> `00bf5b04` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00bf5b08"></a> `00bf5b08` | `48 01 80 52` | mov w8,#0xa | `FALL_THROUGH`
<a id="insn-00bf5b0c"></a> `00bf5b0c` | `09 00 40 39` | ldrb w9,[x0] | `FALL_THROUGH`
<a id="insn-00bf5b10"></a> `00bf5b10` | `0a 08 40 f9` | ldr x10,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00bf5b14"></a> `00bf5b14` | `e8 03 00 39` | strb w8,[sp] | `FALL_THROUGH`
<a id="insn-00bf5b18"></a> `00bf5b18` | `68 8e 8e 52` | mov w8,#0x7473 | `FALL_THROUGH`
<a id="insn-00bf5b1c"></a> `00bf5b1c` | `f5 03 02 2a` | mov w21,w2 | `FALL_THROUGH`
<a id="insn-00bf5b20"></a> `00bf5b20` | `e8 8d ad 72` | movk w8,#0x6c6f, LSL #16 | `FALL_THROUGH`
<a id="insn-00bf5b24"></a> `00bf5b24` | `3f 01 00 72` | tst w9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf5b28"></a> `00bf5b28` | `f3 03 01 aa` | mov x19,x1 | `FALL_THROUGH`
<a id="insn-00bf5b2c"></a> `00bf5b2c` | `e8 13 00 b8` | stur w8,[sp, #0x1] | `FALL_THROUGH`
<a id="insn-00bf5b30"></a> `00bf5b30` | `88 0d 80 52` | mov w8,#0x6c | `FALL_THROUGH`
<a id="insn-00bf5b34"></a> `00bf5b34` | `e8 53 00 78` | sturh w8,[sp, #0x5] | `FALL_THROUGH`
<a id="insn-00bf5b38"></a> `00bf5b38` | `08 10 00 91` | add x8,x0,#0x4 | `FALL_THROUGH`
<a id="insn-00bf5b3c"></a> `00bf5b3c` | `bf 0f 00 f9` | str xzr,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bf5b40"></a> `00bf5b40` | `14 01 8a 9a` | csel x20,x8,x10,eq | `FALL_THROUGH`
<a id="insn-00bf5b44"></a> `00bf5b44` | `93 89 01 94` | bl 0x00c58190 | `UNCONDITIONAL_CALL`
<a id="insn-00bf5b48"></a> `00bf5b48` | `17 00 40 b9` | ldr w23,[x0] | `FALL_THROUGH`
<a id="insn-00bf5b4c"></a> `00bf5b4c` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bf5b50"></a> `00bf5b50` | `1f 00 00 b9` | str wzr,[x0] | `FALL_THROUGH`
<a id="insn-00bf5b54"></a> `00bf5b54` | `a1 63 00 91` | add x1,x29,#0x18 | `FALL_THROUGH`
<a id="insn-00bf5b58"></a> `00bf5b58` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00bf5b5c"></a> `00bf5b5c` | `e2 03 15 2a` | mov w2,w21 | `FALL_THROUGH`
<a id="insn-00bf5b60"></a> `00bf5b60` | `88 a1 01 94` | bl 0x00c5e180 | `UNCONDITIONAL_CALL`
<a id="insn-00bf5b64"></a> `00bf5b64` | `c8 02 40 b9` | ldr w8,[x22] | `FALL_THROUGH`
<a id="insn-00bf5b68"></a> `00bf5b68` | `e9 03 00 91` | mov x9,sp | `FALL_THROUGH`
<a id="insn-00bf5b6c"></a> `00bf5b6c` | `d7 02 00 b9` | str w23,[x22] | `FALL_THROUGH`
<a id="insn-00bf5b70"></a> `00bf5b70` | `1f 89 00 71` | cmp w8,#0x22 | `FALL_THROUGH`
<a id="insn-00bf5b74"></a> `00bf5b74` | `28 01 40 b2` | orr x8,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf5b78"></a> `00bf5b78` | `40 02 00 54` | b.eq 0x00bf5bc0 | `CONDITIONAL_JUMP`
<a id="insn-00bf5b7c"></a> `00bf5b7c` | `a9 0f 40 f9` | ldr x9,[x29, #0x18] | `FALL_THROUGH`
<a id="insn-00bf5b80"></a> `00bf5b80` | `29 01 14 eb` | subs x9,x9,x20 | `FALL_THROUGH`
<a id="insn-00bf5b84"></a> `00bf5b84` | `e0 03 00 54` | b.eq 0x00bf5c00 | `CONDITIONAL_JUMP`
<a id="insn-00bf5b88"></a> `00bf5b88` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bf5b8c"></a> `00bf5b8c` | `73 00 00 b4` | cbz x19,0x00bf5b98 | `CONDITIONAL_JUMP`
<a id="insn-00bf5b90"></a> `00bf5b90` | `28 fd 42 93` | asr x8,x9,#0x2 | `FALL_THROUGH`
<a id="insn-00bf5b94"></a> `00bf5b94` | `68 02 00 f9` | str x8,[x19] | `FALL_THROUGH`
<a id="insn-00bf5b98"></a> `00bf5b98` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf5b9c"></a> `00bf5b9c` | `61 a1 01 94` | bl 0x00c5e120 | `UNCONDITIONAL_CALL`
<a id="insn-00bf5ba0"></a> `00bf5ba0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bf5ba4"></a> `00bf5ba4` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00bf5ba8"></a> `00bf5ba8` | `f7 23 40 f9` | ldr x23,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00bf5bac"></a> `00bf5bac` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00bf5bb0"></a> `00bf5bb0` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00bf5bb4"></a> `00bf5bb4` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00bf5bb8"></a> `00bf5bb8` | `bf 23 03 d5` | autiasp | `FALL_THROUGH`
<a id="insn-00bf5bbc"></a> `00bf5bbc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bf5bc0"></a> `00bf5bc0` | `c9 04 80 52` | mov w9,#0x26 | `FALL_THROUGH`
<a id="insn-00bf5bc4"></a> `00bf5bc4` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00bf5bc8"></a> `00bf5bc8` | `08 11 40 39` | ldrb w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bf5bcc"></a> `00bf5bcc` | `e9 63 00 39` | strb w9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bf5bd0"></a> `00bf5bd0` | `29 b6 ff 90` | adrp x9,0x2b9000 | `FALL_THROUGH`
<a id="insn-00bf5bd4"></a> `00bf5bd4` | `29 c9 35 91` | add x9,x9,#0xd72 | `FALL_THROUGH`
<a id="insn-00bf5bd8"></a> `00bf5bd8` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bf5bdc"></a> `00bf5bdc` | `e8 77 00 39` | strb w8,[sp, #0x1d] | `FALL_THROUGH`
<a id="insn-00bf5be0"></a> `00bf5be0` | `28 61 40 f8` | ldur x8,[x9, #0x6] | `FALL_THROUGH`
<a id="insn-00bf5be4"></a> `00bf5be4` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bf5be8"></a> `00bf5be8` | `e9 63 00 91` | add x9,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf5bec"></a> `00bf5bec` | `ea 93 01 b8` | stur w10,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00bf5bf0"></a> `00bf5bf0` | `eb e3 01 f8` | stur x11,[sp, #0x1e] | `FALL_THROUGH`
<a id="insn-00bf5bf4"></a> `00bf5bf4` | `e8 43 02 f8` | stur x8,[sp, #0x24] | `FALL_THROUGH`
<a id="insn-00bf5bf8"></a> `00bf5bf8` | `20 01 40 b2` | orr x0,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf5bfc"></a> `00bf5bfc` | `5d 33 e1 97` | bl 0x00442970 | `CALL_TERMINATOR`
<a id="insn-00bf5c00"></a> `00bf5c00` | `09 05 80 52` | mov w9,#0x28 | `FALL_THROUGH`
<a id="insn-00bf5c04"></a> `00bf5c04` | `0a 01 40 b9` | ldr w10,[x8] | `FALL_THROUGH`
<a id="insn-00bf5c08"></a> `00bf5c08` | `08 11 40 39` | ldrb w8,[x8, #0x4] | `FALL_THROUGH`
<a id="insn-00bf5c0c"></a> `00bf5c0c` | `e9 63 00 39` | strb w9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00bf5c10"></a> `00bf5c10` | `89 b5 ff d0` | adrp x9,0x2a7000 | `FALL_THROUGH`
<a id="insn-00bf5c14"></a> `00bf5c14` | `29 b9 12 91` | add x9,x9,#0x4ae | `FALL_THROUGH`
<a id="insn-00bf5c18"></a> `00bf5c18` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00bf5c1c"></a> `00bf5c1c` | `e8 77 00 39` | strb w8,[sp, #0x1d] | `FALL_THROUGH`
<a id="insn-00bf5c20"></a> `00bf5c20` | `28 71 40 f8` | ldur x8,[x9, #0x7] | `FALL_THROUGH`
<a id="insn-00bf5c24"></a> `00bf5c24` | `ff 17 00 f9` | str xzr,[sp, #0x28] | `FALL_THROUGH`
<a id="insn-00bf5c28"></a> `00bf5c28` | `e9 63 00 91` | add x9,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf5c2c"></a> `00bf5c2c` | `ea 93 01 b8` | stur w10,[sp, #0x19] | `FALL_THROUGH`
<a id="insn-00bf5c30"></a> `00bf5c30` | `eb e3 01 f8` | stur x11,[sp, #0x1e] | `FALL_THROUGH`
<a id="insn-00bf5c34"></a> `00bf5c34` | `e8 53 02 f8` | stur x8,[sp, #0x25] | `FALL_THROUGH`
<a id="insn-00bf5c38"></a> `00bf5c38` | `20 01 40 b2` | orr x0,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00bf5c3c"></a> `00bf5c3c` | `8b 09 00 94` | bl 0x00bf8268 | `UNCONDITIONAL_CALL`
<a id="insn-00bf5c40"></a> `00bf5c40` | `01 00 00 14` | b 0x00bf5c44 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf5c44"></a> `00bf5c44` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00bf5c48"></a> `00bf5c48` | `e0 63 00 91` | add x0,sp,#0x18 | `FALL_THROUGH`
<a id="insn-00bf5c4c"></a> `00bf5c4c` | `35 a1 01 94` | bl 0x00c5e120 | `UNCONDITIONAL_CALL`
<a id="insn-00bf5c50"></a> `00bf5c50` | `02 00 00 14` | b 0x00bf5c58 | `UNCONDITIONAL_JUMP`
<a id="insn-00bf5c58"></a> `00bf5c58` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00bf5c5c"></a> `00bf5c5c` | `31 a1 01 94` | bl 0x00c5e120 | `UNCONDITIONAL_CALL`
<a id="insn-00bf5c60"></a> `00bf5c60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bf5c64"></a> `00bf5c64` | `e6 78 01 94` | bl 0x00c53ffc | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bf5aec`](#insn-00bf5aec) 範囲 `[['00bf5aec', '00bf5b7b']]`
  - `CONDITIONAL_JUMP` [`00bf5b78`](#insn-00bf5b78) → [`00bf5bc0`](#insn-00bf5bc0)
  - `FALL_THROUGH` [`00bf5b78`](#insn-00bf5b78) → [`00bf5b7c`](#insn-00bf5b7c)
- ブロック [`00bf5b7c`](#insn-00bf5b7c) 範囲 `[['00bf5b7c', '00bf5b87']]`
  - `CONDITIONAL_JUMP` [`00bf5b84`](#insn-00bf5b84) → [`00bf5c00`](#insn-00bf5c00)
  - `FALL_THROUGH` [`00bf5b84`](#insn-00bf5b84) → [`00bf5b88`](#insn-00bf5b88)
- ブロック [`00bf5b88`](#insn-00bf5b88) 範囲 `[['00bf5b88', '00bf5b8f']]`
  - `CONDITIONAL_JUMP` [`00bf5b8c`](#insn-00bf5b8c) → [`00bf5b98`](#insn-00bf5b98)
  - `FALL_THROUGH` [`00bf5b8c`](#insn-00bf5b8c) → [`00bf5b90`](#insn-00bf5b90)
- ブロック [`00bf5b90`](#insn-00bf5b90) 範囲 `[['00bf5b90', '00bf5b97']]`
  - `FALL_THROUGH` [`00bf5b94`](#insn-00bf5b94) → [`00bf5b98`](#insn-00bf5b98)
- ブロック [`00bf5b98`](#insn-00bf5b98) 範囲 `[['00bf5b98', '00bf5bbf']]`
- ブロック [`00bf5bc0`](#insn-00bf5bc0) 範囲 `[['00bf5bc0', '00bf5bff']]`
- ブロック [`00bf5c00`](#insn-00bf5c00) 範囲 `[['00bf5c00', '00bf5c43']]`
  - `UNCONDITIONAL_JUMP` [`00bf5c40`](#insn-00bf5c40) → [`00bf5c44`](#insn-00bf5c44)
- ブロック [`00bf5c44`](#insn-00bf5c44) 範囲 `[['00bf5c44', '00bf5c53']]`
  - `UNCONDITIONAL_JUMP` [`00bf5c50`](#insn-00bf5c50) → [`00bf5c58`](#insn-00bf5c58)
- ブロック [`00bf5c58`](#insn-00bf5c58) 範囲 `[['00bf5c58', '00bf5c67']]`

## 命令位置別の参照

- [`00bf5af4`](#insn-00bf5af4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5af8`](#insn-00bf5af8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5afc`](#insn-00bf5afc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b00`](#insn-00bf5b00) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b14`](#insn-00bf5b14) → `Stack[-0x70]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b2c`](#insn-00bf5b2c) → `Stack[-0x6f]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b34`](#insn-00bf5b34) → `Stack[-0x6b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b3c`](#insn-00bf5b3c) → `Stack[-0x28]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b44`](#insn-00bf5b44) → [`00c58190`](../00c58/00c58190.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58190` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b60`](#insn-00bf5b60) → [`00c5e180`](../00c5e/00c5e180.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e180` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b78`](#insn-00bf5b78) → [`00bf5bc0`](#insn-00bf5bc0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b7c`](#insn-00bf5b7c) → `Stack[-0x28]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b84`](#insn-00bf5b84) → [`00bf5c00`](#insn-00bf5c00) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b8c`](#insn-00bf5b8c) → [`00bf5b98`](#insn-00bf5b98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5b9c`](#insn-00bf5b9c) → [`00c5e120`](../00c5e/00c5e120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e120` · 推定シンボル `None` · 推定型 `None`
- [`00bf5ba4`](#insn-00bf5ba4) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5ba8`](#insn-00bf5ba8) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5bac`](#insn-00bf5bac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5bb0`](#insn-00bf5bb0) → `Stack[-0x40]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5bcc`](#insn-00bf5bcc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5bd8`](#insn-00bf5bd8) → `002b9d72`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf5bdc`](#insn-00bf5bdc) → `Stack[-0x53]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5be0`](#insn-00bf5be0) → `002b9d78`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf5be4`](#insn-00bf5be4) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5bec`](#insn-00bf5bec) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5bf0`](#insn-00bf5bf0) → `Stack[-0x52]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5bf4`](#insn-00bf5bf4) → `Stack[-0x4c]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5bfc`](#insn-00bf5bfc) → [`00442970`](../00442/00442970.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00442970` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c0c`](#insn-00bf5c0c) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c18`](#insn-00bf5c18) → `002a74ae`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf5c1c`](#insn-00bf5c1c) → `Stack[-0x53]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c20`](#insn-00bf5c20) → `002a74b5`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`00bf5c24`](#insn-00bf5c24) → `Stack[-0x48]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c2c`](#insn-00bf5c2c) → `Stack[-0x57]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c30`](#insn-00bf5c30) → `Stack[-0x52]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c34`](#insn-00bf5c34) → `Stack[-0x4b]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c3c`](#insn-00bf5c3c) → [`00bf8268`](../00bf8/00bf8268.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bf8268` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c40`](#insn-00bf5c40) → [`00bf5c44`](#insn-00bf5c44) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c4c`](#insn-00bf5c4c) → [`00c5e120`](../00c5e/00c5e120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e120` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c50`](#insn-00bf5c50) → [`00bf5c58`](#insn-00bf5c58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c5c`](#insn-00bf5c5c) → [`00c5e120`](../00c5e/00c5e120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5e120` · 推定シンボル `None` · 推定型 `None`
- [`00bf5c64`](#insn-00bf5c64) → [`00c53ffc`](../00c53/00c53ffc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c53ffc` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bf5af4`](#insn-00bf5af4)

~~~json
{
  "source": "00bf5af4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5af8`](#insn-00bf5af8)

~~~json
{
  "source": "00bf5af8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5afc`](#insn-00bf5afc)

~~~json
{
  "source": "00bf5afc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5b00`](#insn-00bf5b00)

~~~json
{
  "source": "00bf5b00",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5b14`](#insn-00bf5b14)

~~~json
{
  "source": "00bf5b14",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5b2c`](#insn-00bf5b2c)

~~~json
{
  "source": "00bf5b2c",
  "target": "Stack[-0x6f]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5b34`](#insn-00bf5b34)

~~~json
{
  "source": "00bf5b34",
  "target": "Stack[-0x6b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5b3c`](#insn-00bf5b3c)

~~~json
{
  "source": "00bf5b3c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5b44`](#insn-00bf5b44)

~~~json
{
  "source": "00bf5b44",
  "target": "00c58190",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5b60`](#insn-00bf5b60)

~~~json
{
  "source": "00bf5b60",
  "target": "00c5e180",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5b78`](#insn-00bf5b78)

~~~json
{
  "source": "00bf5b78",
  "target": "00bf5bc0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5b7c`](#insn-00bf5b7c)

~~~json
{
  "source": "00bf5b7c",
  "target": "Stack[-0x28]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5b84`](#insn-00bf5b84)

~~~json
{
  "source": "00bf5b84",
  "target": "00bf5c00",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5b8c`](#insn-00bf5b8c)

~~~json
{
  "source": "00bf5b8c",
  "target": "00bf5b98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5b9c`](#insn-00bf5b9c)

~~~json
{
  "source": "00bf5b9c",
  "target": "00c5e120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5ba4`](#insn-00bf5ba4)

~~~json
{
  "source": "00bf5ba4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5ba8`](#insn-00bf5ba8)

~~~json
{
  "source": "00bf5ba8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5bac`](#insn-00bf5bac)

~~~json
{
  "source": "00bf5bac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5bb0`](#insn-00bf5bb0)

~~~json
{
  "source": "00bf5bb0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5bcc`](#insn-00bf5bcc)

~~~json
{
  "source": "00bf5bcc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5bd8`](#insn-00bf5bd8)

~~~json
{
  "source": "00bf5bd8",
  "target": "002b9d72",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9d72",
  "offset": 0,
  "size": 15,
  "datatype": "string",
  "bytes": "3a206f7574206f662072616e676500",
  "capture_start": "002b9d72",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf5bdc`](#insn-00bf5bdc)

~~~json
{
  "source": "00bf5bdc",
  "target": "Stack[-0x53]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5be0`](#insn-00bf5be0)

~~~json
{
  "source": "00bf5be0",
  "target": "002b9d78",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b9d72",
  "offset": 6,
  "size": 15,
  "datatype": "string",
  "bytes": "3a206f7574206f662072616e676500",
  "capture_start": "002b9d72",
  "capture_bytes": 15,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf5be4`](#insn-00bf5be4)

~~~json
{
  "source": "00bf5be4",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5bec`](#insn-00bf5bec)

~~~json
{
  "source": "00bf5bec",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5bf0`](#insn-00bf5bf0)

~~~json
{
  "source": "00bf5bf0",
  "target": "Stack[-0x52]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5bf4`](#insn-00bf5bf4)

~~~json
{
  "source": "00bf5bf4",
  "target": "Stack[-0x4c]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5bfc`](#insn-00bf5bfc)

~~~json
{
  "source": "00bf5bfc",
  "target": "00442970",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5c0c`](#insn-00bf5c0c)

~~~json
{
  "source": "00bf5c0c",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c18`](#insn-00bf5c18)

~~~json
{
  "source": "00bf5c18",
  "target": "002a74ae",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a74ae",
  "offset": 0,
  "size": 16,
  "datatype": "string",
  "bytes": "3a206e6f20636f6e76657273696f6e00",
  "capture_start": "002a74ae",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf5c1c`](#insn-00bf5c1c)

~~~json
{
  "source": "00bf5c1c",
  "target": "Stack[-0x53]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c20`](#insn-00bf5c20)

~~~json
{
  "source": "00bf5c20",
  "target": "002a74b5",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002a74ae",
  "offset": 7,
  "size": 16,
  "datatype": "string",
  "bytes": "3a206e6f20636f6e76657273696f6e00",
  "capture_start": "002a74ae",
  "capture_bytes": 16,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`00bf5c24`](#insn-00bf5c24)

~~~json
{
  "source": "00bf5c24",
  "target": "Stack[-0x48]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c2c`](#insn-00bf5c2c)

~~~json
{
  "source": "00bf5c2c",
  "target": "Stack[-0x57]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c30`](#insn-00bf5c30)

~~~json
{
  "source": "00bf5c30",
  "target": "Stack[-0x52]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c34`](#insn-00bf5c34)

~~~json
{
  "source": "00bf5c34",
  "target": "Stack[-0x4b]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c3c`](#insn-00bf5c3c)

~~~json
{
  "source": "00bf5c3c",
  "target": "00bf8268",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5c40`](#insn-00bf5c40)

~~~json
{
  "source": "00bf5c40",
  "target": "00bf5c44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c4c`](#insn-00bf5c4c)

~~~json
{
  "source": "00bf5c4c",
  "target": "00c5e120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5c50`](#insn-00bf5c50)

~~~json
{
  "source": "00bf5c50",
  "target": "00bf5c58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bf5c5c`](#insn-00bf5c5c)

~~~json
{
  "source": "00bf5c5c",
  "target": "00c5e120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bf5c64`](#insn-00bf5c64)

~~~json
{
  "source": "00bf5c64",
  "target": "00c53ffc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
