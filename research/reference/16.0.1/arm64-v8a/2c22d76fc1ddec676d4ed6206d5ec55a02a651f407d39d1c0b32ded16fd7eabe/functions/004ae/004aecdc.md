# 004aecdc

版: 16.0.1 / arm64-v8a / libnative-lib.so

SO SHA-256: `2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe`

解析リビジョン `711084564ddd8b14` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.0**
  - 採用 · [関数詳細 `004aec9c`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/004ae/004aec9c.md) · 移動量 `+0x40`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/priority-0007.md#compare-fada4b6f053ad4920b6b439a92198fd4)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

- **次の公開版 v16.0.2**
  - 採用 · [関数詳細 `004aed1c`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/004ae/004aed1c.md) · 移動量 `+0x40`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0007.md#compare-894bc2977b0cbb3ef69d24b35e93032a)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "004aecdc",
  "name": "_ZNK5Botan9X509_Time3cmpERKS0_",
  "size": 308,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "00da6c14accec90e07925b05ed72148891b687f22b4f430d316c547a1780b287",
  "source_text_sha256": "00da6c14accec90e07925b05ed72148891b687f22b4f430d316c547a1780b287",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b53909337d9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "004aecdc",
        "004aee0b"
      ],
      [
        "004aee58",
        "004aee5b"
      ]
    ],
    "bytes_sha256": "6fcb2476fcdb1609c6cece27c82bd1358dd992b0d38c751b9a7b678341e6b060",
    "instruction_count": 77,
    "instruction_bytes": 308,
    "body_bytes": 308,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c589e0](../00c58/00c589e0.md)

## 呼び出し先

- [0043ddd8](../0043d/0043ddd8.md)
- [004aec64](../004ae/004aec64.md)
- [00c57ee0](../00c57/00c57ee0.md)
- [00c57ef0](../00c57/00c57ef0.md)
- [00c57f10](../00c57/00c57f10.md)

## 関連文字列（未確認候補）

~~~text
"X509_Time::cmp: No time set"
~~~

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1814 bytes

~~~c

void _ZNK5Botan9X509_Time3cmpERKS0_(long param_1,long param_2)

{
  uint uVar1;
  long lVar2;
  ulong uVar3;
  undefined8 uVar4;
  undefined1 auStack_50 [24];
  long local_38;
  
  lVar2 = tpidr_el0;
  local_38 = *(long *)(lVar2 + 0x28);
  uVar1 = *(uint *)(param_1 + 8);
  if (uVar1 == 0) {
    uVar4 = __cxa_allocate_exception(0x20);
    FUN_0043ddd8(auStack_50,"X509_Time::cmp: No time set");
    uVar3 = FUN_004aec64(uVar4,auStack_50);
    if (*(long *)(lVar2 + 0x28) == local_38) {
                    /* WARNING: Subroutine does not return */
      __cxa_throw(uVar4,PTR__ZTIN5Botan13Invalid_StateE_00c9ad48,FUN_00535868);
    }
    goto LAB_004aee58;
  }
  if (uVar1 < *(uint *)(param_2 + 8)) {
LAB_004aed10:
    uVar3 = 0xffffffff;
  }
  else if (uVar1 == *(uint *)(param_2 + 8)) {
    if (*(uint *)(param_1 + 0xc) < *(uint *)(param_2 + 0xc)) goto LAB_004aed10;
    if (*(uint *)(param_2 + 0xc) < *(uint *)(param_1 + 0xc)) goto LAB_004aed1c;
    if (*(uint *)(param_1 + 0x10) < *(uint *)(param_2 + 0x10)) goto LAB_004aed10;
    if (*(uint *)(param_2 + 0x10) < *(uint *)(param_1 + 0x10)) goto LAB_004aed1c;
    if (*(uint *)(param_1 + 0x14) < *(uint *)(param_2 + 0x14)) goto LAB_004aed10;
    if (*(uint *)(param_2 + 0x14) < *(uint *)(param_1 + 0x14)) goto LAB_004aed1c;
    if (*(uint *)(param_1 + 0x18) < *(uint *)(param_2 + 0x18)) goto LAB_004aed10;
    if (*(uint *)(param_2 + 0x18) < *(uint *)(param_1 + 0x18)) goto LAB_004aed1c;
    if (*(uint *)(param_1 + 0x1c) < *(uint *)(param_2 + 0x1c)) goto LAB_004aed10;
    uVar3 = (ulong)(*(uint *)(param_2 + 0x1c) < *(uint *)(param_1 + 0x1c));
  }
  else {
LAB_004aed1c:
    uVar3 = 1;
  }
  if (*(long *)(lVar2 + 0x28) == local_38) {
    return;
  }
LAB_004aee58:
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar3);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-004aecdc"></a> `004aecdc` | `ff 83 01 d1` | sub sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004aece0"></a> `004aece0` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004aece4"></a> `004aece4` | `f5 23 00 f9` | str x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004aece8"></a> `004aece8` | `f4 4f 05 a9` | stp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004aecec"></a> `004aecec` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-004aecf0"></a> `004aecf0` | `48 d0 3b d5` | mrs x8,tpidr_el0 | `FALL_THROUGH`
<a id="insn-004aecf4"></a> `004aecf4` | `09 15 40 f9` | ldr x9,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004aecf8"></a> `004aecf8` | `a9 83 1f f8` | stur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004aecfc"></a> `004aecfc` | `09 08 40 b9` | ldr w9,[x0, #0x8] | `FALL_THROUGH`
<a id="insn-004aed00"></a> `004aed00` | `69 05 00 34` | cbz w9,0x004aedac | `CONDITIONAL_JUMP`
<a id="insn-004aed04"></a> `004aed04` | `2a 08 40 b9` | ldr w10,[x1, #0x8] | `FALL_THROUGH`
<a id="insn-004aed08"></a> `004aed08` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-004aed0c"></a> `004aed0c` | `62 00 00 54` | b.cs 0x004aed18 | `CONDITIONAL_JUMP`
<a id="insn-004aed10"></a> `004aed10` | `00 00 80 12` | mov w0,#0xffffffff | `FALL_THROUGH`
<a id="insn-004aed14"></a> `004aed14` | `03 00 00 14` | b 0x004aed20 | `UNCONDITIONAL_JUMP`
<a id="insn-004aed18"></a> `004aed18` | `69 01 00 54` | b.ls 0x004aed44 | `CONDITIONAL_JUMP`
<a id="insn-004aed1c"></a> `004aed1c` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-004aed20"></a> `004aed20` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004aed24"></a> `004aed24` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004aed28"></a> `004aed28` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004aed2c"></a> `004aed2c` | `61 09 00 54` | b.ne 0x004aee58 | `CONDITIONAL_JUMP`
<a id="insn-004aed30"></a> `004aed30` | `f4 4f 45 a9` | ldp x20,x19,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-004aed34"></a> `004aed34` | `f5 23 40 f9` | ldr x21,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-004aed38"></a> `004aed38` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-004aed3c"></a> `004aed3c` | `ff 83 01 91` | add sp,sp,#0x60 | `FALL_THROUGH`
<a id="insn-004aed40"></a> `004aed40` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-004aed44"></a> `004aed44` | `09 0c 40 b9` | ldr w9,[x0, #0xc] | `FALL_THROUGH`
<a id="insn-004aed48"></a> `004aed48` | `2a 0c 40 b9` | ldr w10,[x1, #0xc] | `FALL_THROUGH`
<a id="insn-004aed4c"></a> `004aed4c` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-004aed50"></a> `004aed50` | `03 fe ff 54` | b.cc 0x004aed10 | `CONDITIONAL_JUMP`
<a id="insn-004aed54"></a> `004aed54` | `48 fe ff 54` | b.hi 0x004aed1c | `CONDITIONAL_JUMP`
<a id="insn-004aed58"></a> `004aed58` | `09 10 40 b9` | ldr w9,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-004aed5c"></a> `004aed5c` | `2a 10 40 b9` | ldr w10,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-004aed60"></a> `004aed60` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-004aed64"></a> `004aed64` | `63 fd ff 54` | b.cc 0x004aed10 | `CONDITIONAL_JUMP`
<a id="insn-004aed68"></a> `004aed68` | `a8 fd ff 54` | b.hi 0x004aed1c | `CONDITIONAL_JUMP`
<a id="insn-004aed6c"></a> `004aed6c` | `09 14 40 b9` | ldr w9,[x0, #0x14] | `FALL_THROUGH`
<a id="insn-004aed70"></a> `004aed70` | `2a 14 40 b9` | ldr w10,[x1, #0x14] | `FALL_THROUGH`
<a id="insn-004aed74"></a> `004aed74` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-004aed78"></a> `004aed78` | `c3 fc ff 54` | b.cc 0x004aed10 | `CONDITIONAL_JUMP`
<a id="insn-004aed7c"></a> `004aed7c` | `08 fd ff 54` | b.hi 0x004aed1c | `CONDITIONAL_JUMP`
<a id="insn-004aed80"></a> `004aed80` | `09 18 40 b9` | ldr w9,[x0, #0x18] | `FALL_THROUGH`
<a id="insn-004aed84"></a> `004aed84` | `2a 18 40 b9` | ldr w10,[x1, #0x18] | `FALL_THROUGH`
<a id="insn-004aed88"></a> `004aed88` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-004aed8c"></a> `004aed8c` | `23 fc ff 54` | b.cc 0x004aed10 | `CONDITIONAL_JUMP`
<a id="insn-004aed90"></a> `004aed90` | `68 fc ff 54` | b.hi 0x004aed1c | `CONDITIONAL_JUMP`
<a id="insn-004aed94"></a> `004aed94` | `09 1c 40 b9` | ldr w9,[x0, #0x1c] | `FALL_THROUGH`
<a id="insn-004aed98"></a> `004aed98` | `2a 1c 40 b9` | ldr w10,[x1, #0x1c] | `FALL_THROUGH`
<a id="insn-004aed9c"></a> `004aed9c` | `3f 01 0a 6b` | cmp w9,w10 | `FALL_THROUGH`
<a id="insn-004aeda0"></a> `004aeda0` | `83 fb ff 54` | b.cc 0x004aed10 | `CONDITIONAL_JUMP`
<a id="insn-004aeda4"></a> `004aeda4` | `e0 97 9f 1a` | cset w0,hi | `FALL_THROUGH`
<a id="insn-004aeda8"></a> `004aeda8` | `de ff ff 17` | b 0x004aed20 | `UNCONDITIONAL_JUMP`
<a id="insn-004aedac"></a> `004aedac` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-004aedb0"></a> `004aedb0` | `e8 07 00 f9` | str x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004aedb4"></a> `004aedb4` | `4f a4 1e 94` | bl 0x00c57ef0 | `UNCONDITIONAL_CALL`
<a id="insn-004aedb8"></a> `004aedb8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-004aedbc"></a> `004aedbc` | `41 f0 ff d0` | adrp x1,0x2b8000 | `FALL_THROUGH`
<a id="insn-004aedc0"></a> `004aedc0` | `21 08 39 91` | add x1,x1,#0xe42 | `FALL_THROUGH`
<a id="insn-004aedc4"></a> `004aedc4` | `e0 43 00 91` | add x0,sp,#0x10 | `FALL_THROUGH`
<a id="insn-004aedc8"></a> `004aedc8` | `04 3c fe 97` | bl 0x0043ddd8 | `UNCONDITIONAL_CALL`
<a id="insn-004aedcc"></a> `004aedcc` | `35 00 80 52` | mov w21,#0x1 | `FALL_THROUGH`
<a id="insn-004aedd0"></a> `004aedd0` | `e1 43 00 91` | add x1,sp,#0x10 | `FALL_THROUGH`
<a id="insn-004aedd4"></a> `004aedd4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004aedd8"></a> `004aedd8` | `a3 ff ff 97` | bl 0x004aec64 | `UNCONDITIONAL_CALL`
<a id="insn-004aeddc"></a> `004aeddc` | `e8 07 40 f9` | ldr x8,[sp, #0x8] | `FALL_THROUGH`
<a id="insn-004aede0"></a> `004aede0` | `08 15 40 f9` | ldr x8,[x8, #0x28] | `FALL_THROUGH`
<a id="insn-004aede4"></a> `004aede4` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-004aede8"></a> `004aede8` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-004aedec"></a> `004aedec` | `61 03 00 54` | b.ne 0x004aee58 | `CONDITIONAL_JUMP`
<a id="insn-004aedf0"></a> `004aedf0` | `61 3f 00 90` | adrp x1,0xc9a000 | `FALL_THROUGH`
<a id="insn-004aedf4"></a> `004aedf4` | `1f 20 03 d5` | nop | `FALL_THROUGH`
<a id="insn-004aedf8"></a> `004aedf8` | `82 53 43 10` | adr x2,0x535868 | `FALL_THROUGH`
<a id="insn-004aedfc"></a> `004aedfc` | `21 a4 46 f9` | ldr x1,[x1, #0xd48] | `FALL_THROUGH`
<a id="insn-004aee00"></a> `004aee00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-004aee04"></a> `004aee04` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-004aee08"></a> `004aee08` | `42 a4 1e 94` | bl 0x00c57f10 | `CALL_TERMINATOR`
<a id="insn-004aee58"></a> `004aee58` | `22 a4 1e 94` | bl 0x00c57ee0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`004aecdc`](#insn-004aecdc) 範囲 `[['004aecdc', '004aed03']]`
  - `CONDITIONAL_JUMP` [`004aed00`](#insn-004aed00) → [`004aedac`](#insn-004aedac)
  - `FALL_THROUGH` [`004aed00`](#insn-004aed00) → [`004aed04`](#insn-004aed04)
- ブロック [`004aed04`](#insn-004aed04) 範囲 `[['004aed04', '004aed0f']]`
  - `CONDITIONAL_JUMP` [`004aed0c`](#insn-004aed0c) → [`004aed18`](#insn-004aed18)
  - `FALL_THROUGH` [`004aed0c`](#insn-004aed0c) → [`004aed10`](#insn-004aed10)
- ブロック [`004aed10`](#insn-004aed10) 範囲 `[['004aed10', '004aed17']]`
  - `UNCONDITIONAL_JUMP` [`004aed14`](#insn-004aed14) → [`004aed20`](#insn-004aed20)
- ブロック [`004aed18`](#insn-004aed18) 範囲 `[['004aed18', '004aed1b']]`
  - `CONDITIONAL_JUMP` [`004aed18`](#insn-004aed18) → [`004aed44`](#insn-004aed44)
  - `FALL_THROUGH` [`004aed18`](#insn-004aed18) → [`004aed1c`](#insn-004aed1c)
- ブロック [`004aed1c`](#insn-004aed1c) 範囲 `[['004aed1c', '004aed1f']]`
  - `FALL_THROUGH` [`004aed1c`](#insn-004aed1c) → [`004aed20`](#insn-004aed20)
- ブロック [`004aed20`](#insn-004aed20) 範囲 `[['004aed20', '004aed2f']]`
  - `CONDITIONAL_JUMP` [`004aed2c`](#insn-004aed2c) → [`004aee58`](#insn-004aee58)
  - `FALL_THROUGH` [`004aed2c`](#insn-004aed2c) → [`004aed30`](#insn-004aed30)
- ブロック [`004aed30`](#insn-004aed30) 範囲 `[['004aed30', '004aed43']]`
- ブロック [`004aed44`](#insn-004aed44) 範囲 `[['004aed44', '004aed53']]`
  - `CONDITIONAL_JUMP` [`004aed50`](#insn-004aed50) → [`004aed10`](#insn-004aed10)
  - `FALL_THROUGH` [`004aed50`](#insn-004aed50) → [`004aed54`](#insn-004aed54)
- ブロック [`004aed54`](#insn-004aed54) 範囲 `[['004aed54', '004aed57']]`
  - `CONDITIONAL_JUMP` [`004aed54`](#insn-004aed54) → [`004aed1c`](#insn-004aed1c)
  - `FALL_THROUGH` [`004aed54`](#insn-004aed54) → [`004aed58`](#insn-004aed58)
- ブロック [`004aed58`](#insn-004aed58) 範囲 `[['004aed58', '004aed67']]`
  - `CONDITIONAL_JUMP` [`004aed64`](#insn-004aed64) → [`004aed10`](#insn-004aed10)
  - `FALL_THROUGH` [`004aed64`](#insn-004aed64) → [`004aed68`](#insn-004aed68)
- ブロック [`004aed68`](#insn-004aed68) 範囲 `[['004aed68', '004aed6b']]`
  - `CONDITIONAL_JUMP` [`004aed68`](#insn-004aed68) → [`004aed1c`](#insn-004aed1c)
  - `FALL_THROUGH` [`004aed68`](#insn-004aed68) → [`004aed6c`](#insn-004aed6c)
- ブロック [`004aed6c`](#insn-004aed6c) 範囲 `[['004aed6c', '004aed7b']]`
  - `CONDITIONAL_JUMP` [`004aed78`](#insn-004aed78) → [`004aed10`](#insn-004aed10)
  - `FALL_THROUGH` [`004aed78`](#insn-004aed78) → [`004aed7c`](#insn-004aed7c)
- ブロック [`004aed7c`](#insn-004aed7c) 範囲 `[['004aed7c', '004aed7f']]`
  - `CONDITIONAL_JUMP` [`004aed7c`](#insn-004aed7c) → [`004aed1c`](#insn-004aed1c)
  - `FALL_THROUGH` [`004aed7c`](#insn-004aed7c) → [`004aed80`](#insn-004aed80)
- ブロック [`004aed80`](#insn-004aed80) 範囲 `[['004aed80', '004aed8f']]`
  - `CONDITIONAL_JUMP` [`004aed8c`](#insn-004aed8c) → [`004aed10`](#insn-004aed10)
  - `FALL_THROUGH` [`004aed8c`](#insn-004aed8c) → [`004aed90`](#insn-004aed90)
- ブロック [`004aed90`](#insn-004aed90) 範囲 `[['004aed90', '004aed93']]`
  - `CONDITIONAL_JUMP` [`004aed90`](#insn-004aed90) → [`004aed1c`](#insn-004aed1c)
  - `FALL_THROUGH` [`004aed90`](#insn-004aed90) → [`004aed94`](#insn-004aed94)
- ブロック [`004aed94`](#insn-004aed94) 範囲 `[['004aed94', '004aeda3']]`
  - `CONDITIONAL_JUMP` [`004aeda0`](#insn-004aeda0) → [`004aed10`](#insn-004aed10)
  - `FALL_THROUGH` [`004aeda0`](#insn-004aeda0) → [`004aeda4`](#insn-004aeda4)
- ブロック [`004aeda4`](#insn-004aeda4) 範囲 `[['004aeda4', '004aedab']]`
  - `UNCONDITIONAL_JUMP` [`004aeda8`](#insn-004aeda8) → [`004aed20`](#insn-004aed20)
- ブロック [`004aedac`](#insn-004aedac) 範囲 `[['004aedac', '004aedef']]`
  - `CONDITIONAL_JUMP` [`004aedec`](#insn-004aedec) → [`004aee58`](#insn-004aee58)
  - `FALL_THROUGH` [`004aedec`](#insn-004aedec) → [`004aedf0`](#insn-004aedf0)
- ブロック [`004aedf0`](#insn-004aedf0) 範囲 `[['004aedf0', '004aee0b']]`
- ブロック [`004aee58`](#insn-004aee58) 範囲 `[['004aee58', '004aee5b']]`

## 命令位置別の参照

- [`004aece0`](#insn-004aece0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aece4`](#insn-004aece4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aece8`](#insn-004aece8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aecf8`](#insn-004aecf8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed00`](#insn-004aed00) → [`004aedac`](#insn-004aedac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed0c`](#insn-004aed0c) → [`004aed18`](#insn-004aed18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed14`](#insn-004aed14) → [`004aed20`](#insn-004aed20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed18`](#insn-004aed18) → [`004aed44`](#insn-004aed44) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed24`](#insn-004aed24) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed2c`](#insn-004aed2c) → [`004aee58`](#insn-004aee58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed30`](#insn-004aed30) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed34`](#insn-004aed34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed38`](#insn-004aed38) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed50`](#insn-004aed50) → [`004aed10`](#insn-004aed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed54`](#insn-004aed54) → [`004aed1c`](#insn-004aed1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed64`](#insn-004aed64) → [`004aed10`](#insn-004aed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed68`](#insn-004aed68) → [`004aed1c`](#insn-004aed1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed78`](#insn-004aed78) → [`004aed10`](#insn-004aed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed7c`](#insn-004aed7c) → [`004aed1c`](#insn-004aed1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed8c`](#insn-004aed8c) → [`004aed10`](#insn-004aed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aed90`](#insn-004aed90) → [`004aed1c`](#insn-004aed1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aeda0`](#insn-004aeda0) → [`004aed10`](#insn-004aed10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aeda8`](#insn-004aeda8) → [`004aed20`](#insn-004aed20) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aedb0`](#insn-004aedb0) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aedb4`](#insn-004aedb4) → [`00c57ef0`](../00c57/00c57ef0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ef0` · 推定シンボル `None` · 推定型 `None`
- [`004aedc0`](#insn-004aedc0) → `002b8e42`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `string`
- [`004aedc8`](#insn-004aedc8) → [`0043ddd8`](../0043d/0043ddd8.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0043ddd8` · 推定シンボル `None` · 推定型 `None`
- [`004aedd8`](#insn-004aedd8) → [`004aec64`](004aec64.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `004aec64` · 推定シンボル `None` · 推定型 `None`
- [`004aeddc`](#insn-004aeddc) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aede4`](#insn-004aede4) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aedec`](#insn-004aedec) → [`004aee58`](#insn-004aee58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`004aedf8`](#insn-004aedf8) → [`00535868`](../00535/00535868.md) · `PARAM` · `ANALYSIS` · 関数 `00535868` · 推定シンボル `None` · 推定型 `None`
- [`004aedfc`](#insn-004aedfc) → `00c9ad48`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`004aedfc`](#insn-004aedfc) → `00c66398`（関数外または未収録） · `PARAM` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZTIN5Botan13Invalid_StateE` · 推定型 `pointer __((offset(0x10)))`
- [`004aee08`](#insn-004aee08) → [`00c57f10`](../00c57/00c57f10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f10` · 推定シンボル `None` · 推定型 `None`
- [`004aee58`](#insn-004aee58) → [`00c57ee0`](../00c57/00c57ee0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ee0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`004aece0`](#insn-004aece0)

~~~json
{
  "source": "004aece0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aece4`](#insn-004aece4)

~~~json
{
  "source": "004aece4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aece8`](#insn-004aece8)

~~~json
{
  "source": "004aece8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aecf8`](#insn-004aecf8)

~~~json
{
  "source": "004aecf8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed00`](#insn-004aed00)

~~~json
{
  "source": "004aed00",
  "target": "004aedac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed0c`](#insn-004aed0c)

~~~json
{
  "source": "004aed0c",
  "target": "004aed18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed14`](#insn-004aed14)

~~~json
{
  "source": "004aed14",
  "target": "004aed20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed18`](#insn-004aed18)

~~~json
{
  "source": "004aed18",
  "target": "004aed44",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed24`](#insn-004aed24)

~~~json
{
  "source": "004aed24",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed2c`](#insn-004aed2c)

~~~json
{
  "source": "004aed2c",
  "target": "004aee58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed30`](#insn-004aed30)

~~~json
{
  "source": "004aed30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed34`](#insn-004aed34)

~~~json
{
  "source": "004aed34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed38`](#insn-004aed38)

~~~json
{
  "source": "004aed38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed50`](#insn-004aed50)

~~~json
{
  "source": "004aed50",
  "target": "004aed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed54`](#insn-004aed54)

~~~json
{
  "source": "004aed54",
  "target": "004aed1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed64`](#insn-004aed64)

~~~json
{
  "source": "004aed64",
  "target": "004aed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed68`](#insn-004aed68)

~~~json
{
  "source": "004aed68",
  "target": "004aed1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed78`](#insn-004aed78)

~~~json
{
  "source": "004aed78",
  "target": "004aed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed7c`](#insn-004aed7c)

~~~json
{
  "source": "004aed7c",
  "target": "004aed1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed8c`](#insn-004aed8c)

~~~json
{
  "source": "004aed8c",
  "target": "004aed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aed90`](#insn-004aed90)

~~~json
{
  "source": "004aed90",
  "target": "004aed1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aeda0`](#insn-004aeda0)

~~~json
{
  "source": "004aeda0",
  "target": "004aed10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aeda8`](#insn-004aeda8)

~~~json
{
  "source": "004aeda8",
  "target": "004aed20",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aedb0`](#insn-004aedb0)

~~~json
{
  "source": "004aedb0",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aedb4`](#insn-004aedb4)

~~~json
{
  "source": "004aedb4",
  "target": "00c57ef0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004aedc0`](#insn-004aedc0)

~~~json
{
  "source": "004aedc0",
  "target": "002b8e42",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "002b8e42",
  "offset": 0,
  "size": 28,
  "datatype": "string",
  "bytes": "583530395f54696d653a3a636d703a204e6f2074696d652073657400",
  "capture_start": "002b8e42",
  "capture_bytes": 28,
  "capture_state": "complete_static_bytes"
}
~~~
- 参照命令 [`004aedc8`](#insn-004aedc8)

~~~json
{
  "source": "004aedc8",
  "target": "0043ddd8",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004aedd8`](#insn-004aedd8)

~~~json
{
  "source": "004aedd8",
  "target": "004aec64",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004aeddc`](#insn-004aeddc)

~~~json
{
  "source": "004aeddc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aede4`](#insn-004aede4)

~~~json
{
  "source": "004aede4",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aedec`](#insn-004aedec)

~~~json
{
  "source": "004aedec",
  "target": "004aee58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`004aedf8`](#insn-004aedf8)

~~~json
{
  "source": "004aedf8",
  "target": "00535868",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004aedfc`](#insn-004aedfc)

~~~json
{
  "source": "004aedfc",
  "target": "00c9ad48",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9ad48",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004aedfc`](#insn-004aedfc)

~~~json
{
  "source": "004aedfc",
  "target": "00c66398",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c66398",
  "offset": 0,
  "size": 8,
  "datatype": "pointer __((offset(0x10)))",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`004aee08`](#insn-004aee08)

~~~json
{
  "source": "004aee08",
  "target": "00c57f10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`004aee58`](#insn-004aee58)

~~~json
{
  "source": "004aee58",
  "target": "00c57ee0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
