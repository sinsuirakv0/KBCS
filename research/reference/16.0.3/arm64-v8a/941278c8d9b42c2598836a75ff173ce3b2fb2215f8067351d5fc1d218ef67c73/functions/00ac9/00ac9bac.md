# 00ac9bac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00ac8bb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00ac8/00ac8bb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/alignment_unresolved-0011.md#compare-1694ae00963dd54320b05ed64fd3e57d)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00ac9bac",
  "name": "FUN_00ac9bac",
  "size": 276,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "0c295b5f92822cc0bfbb173d61a5ffff5057a9ce2ded457e7a2dbce27cacbe1e",
  "source_text_sha256": "0c295b5f92822cc0bfbb173d61a5ffff5057a9ce2ded457e7a2dbce27cacbe1e",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00ac9bac",
        "00ac9cbf"
      ]
    ],
    "bytes_sha256": "04797beab59281156ea747aee1737a79d560286dc3fc92e2a6f6f744d9618a49",
    "instruction_count": 69,
    "instruction_bytes": 276,
    "body_bytes": 276,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

- [007890e0](../00789/007890e0.md)
- [0082fe24](../0082f/0082fe24.md)
- [008cbbc0](../008cb/008cbbc0.md)
- [00a735f8](../00a73/00a735f8.md)
- [00ac14b8](../00ac1/00ac14b8.md)

## 呼び出し先

- [0057c9b4](../0057c/0057c9b4.md)
- [008524fc](../00852/008524fc.md)
- [00c58f80](../00c58/00c58f80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1980 bytes

~~~c

void FUN_00ac9bac(long param_1,undefined4 param_2,undefined4 param_3,int param_4,long *param_5)

{
  long lVar1;
  long *plVar2;
  long *plVar3;
  long lVar4;
  long local_70 [4];
  long *local_50;
  long local_38;
  
  local_50 = local_70;
  plVar3 = local_70;
  lVar1 = tpidr_el0;
                    /* try { // try from 00ac9bcc to 00bc9d2f has its CatchHandler @ 00ac9bcc
                       catch() { ... } // from try @ 00ac9bcc with catch @ 00ac9bcc
                       catch() { ... } // from try @ 00ac9df0 with catch @ 00ac9bcc
                       catch() { ... } // from try @ 00aca06c with catch @ 00ac9bcc
                       catch() { ... } // from try @ 00aca114 with catch @ 00ac9bcc
                       catch() { ... } // from try @ 00aca270 with catch @ 00ac9bcc
                       catch() { ... } // from try @ 00aca2fc with catch @ 00ac9bcc */
  local_38 = *(long *)(lVar1 + 0x28);
  *(bool *)(param_1 + 0x3c) = 1 < param_4;
  plVar2 = (long *)param_5[4];
  *(undefined4 *)(param_1 + 0x280) = param_3;
  *(int *)(param_1 + 0x5c) = param_4;
  if (plVar2 == (long *)0x0) {
    local_50 = (long *)0x0;
  }
  else if (plVar2 == param_5) {
    (**(code **)(*param_5 + 0x18))(param_5,local_70);
  }
  else {
    local_50 = (long *)(**(code **)(*plVar2 + 0x10))();
  }
  FUN_0057c9b4(local_70,param_1 + 0x170);
  if (local_50 == local_70) {
    lVar4 = 0x20;
  }
  else {
    if (local_50 == (long *)0x0) goto LAB_00ac9c6c;
    lVar4 = 0x28;
    plVar3 = local_50;
  }
  (**(code **)(*plVar3 + lVar4))();
LAB_00ac9c6c:
  *(undefined4 *)(param_1 + 0x68) = param_2;
  lVar4 = FUN_008524fc();
  *(undefined1 *)(lVar4 + 0x3570) = 0;
  lVar4 = FUN_008524fc();
  *(undefined1 *)(lVar4 + 0x3573) = 0;
  lVar4 = FUN_008524fc();
  *(undefined1 *)(param_1 + 0x3d) = 0;
  *(undefined1 *)(lVar4 + 0x3572) = 0;
  if (*(long *)(lVar1 + 0x28) == local_38) {
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
<a id="insn-00ac9bac"></a> `00ac9bac` | `ff c3 01 d1` | sub sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00ac9bb0"></a> `00ac9bb0` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9bb4"></a> `00ac9bb4` | `f6 57 05 a9` | stp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ac9bb8"></a> `00ac9bb8` | `f4 4f 06 a9` | stp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ac9bbc"></a> `00ac9bbc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00ac9bc0"></a> `00ac9bc0` | `55 d0 3b d5` | mrs x21,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00ac9bc4"></a> `00ac9bc4` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00ac9bc8"></a> `00ac9bc8` | `f4 03 01 2a` | mov w20,w1 | `FALL_THROUGH`
<a id="insn-00ac9bcc"></a> `00ac9bcc` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00ac9bd0"></a> `00ac9bd0` | `7f 04 00 71` | cmp w3,#0x1 | `FALL_THROUGH`
<a id="insn-00ac9bd4"></a> `00ac9bd4` | `e9 d7 9f 1a` | cset w9,gt | `FALL_THROUGH`
<a id="insn-00ac9bd8"></a> `00ac9bd8` | `a8 83 1f f8` | stur x8,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ac9bdc"></a> `00ac9bdc` | `09 f0 00 39` | strb w9,[x0, #0x3c] | `FALL_THROUGH`
<a id="insn-00ac9be0"></a> `00ac9be0` | `80 10 40 f9` | ldr x0,[x4, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9be4"></a> `00ac9be4` | `62 82 02 b9` | str w2,[x19, #0x280] | `FALL_THROUGH`
<a id="insn-00ac9be8"></a> `00ac9be8` | `63 5e 00 b9` | str w3,[x19, #0x5c] | `FALL_THROUGH`
<a id="insn-00ac9bec"></a> `00ac9bec` | `00 01 00 b4` | cbz x0,0x00ac9c0c | `CONDITIONAL_JUMP`
<a id="insn-00ac9bf0"></a> `00ac9bf0` | `1f 00 04 eb` | cmp x0,x4 | `FALL_THROUGH`
<a id="insn-00ac9bf4"></a> `00ac9bf4` | `00 01 00 54` | b.eq 0x00ac9c14 | `CONDITIONAL_JUMP`
<a id="insn-00ac9bf8"></a> `00ac9bf8` | `08 00 40 f9` | ldr x8,[x0] | `FALL_THROUGH`
<a id="insn-00ac9bfc"></a> `00ac9bfc` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00ac9c00"></a> `00ac9c00` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9c04"></a> `00ac9c04` | `e0 13 00 f9` | str x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9c08"></a> `00ac9c08` | `0a 00 00 14` | b 0x00ac9c30 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9c0c"></a> `00ac9c0c` | `ff 13 00 f9` | str xzr,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9c10"></a> `00ac9c10` | `08 00 00 14` | b 0x00ac9c30 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9c14"></a> `00ac9c14` | `e8 03 00 91` | mov x8,sp | `FALL_THROUGH`
<a id="insn-00ac9c18"></a> `00ac9c18` | `89 00 40 f9` | ldr x9,[x4] | `FALL_THROUGH`
<a id="insn-00ac9c1c"></a> `00ac9c1c` | `e1 03 00 91` | mov x1,sp | `FALL_THROUGH`
<a id="insn-00ac9c20"></a> `00ac9c20` | `e8 13 00 f9` | str x8,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9c24"></a> `00ac9c24` | `e0 03 04 aa` | mov x0,x4 | `FALL_THROUGH`
<a id="insn-00ac9c28"></a> `00ac9c28` | `28 0d 40 f9` | ldr x8,[x9, #0x18] | `FALL_THROUGH`
<a id="insn-00ac9c2c"></a> `00ac9c2c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9c30"></a> `00ac9c30` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00ac9c34"></a> `00ac9c34` | `61 c2 05 91` | add x1,x19,#0x170 | `FALL_THROUGH`
<a id="insn-00ac9c38"></a> `00ac9c38` | `f6 03 00 91` | mov x22,sp | `FALL_THROUGH`
<a id="insn-00ac9c3c"></a> `00ac9c3c` | `5e cb ea 97` | bl 0x0057c9b4 | `UNCONDITIONAL_CALL`
<a id="insn-00ac9c40"></a> `00ac9c40` | `e0 13 40 f9` | ldr x0,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00ac9c44"></a> `00ac9c44` | `1f 00 16 eb` | cmp x0,x22 | `FALL_THROUGH`
<a id="insn-00ac9c48"></a> `00ac9c48` | `80 00 00 54` | b.eq 0x00ac9c58 | `CONDITIONAL_JUMP`
<a id="insn-00ac9c4c"></a> `00ac9c4c` | `00 01 00 b4` | cbz x0,0x00ac9c6c | `CONDITIONAL_JUMP`
<a id="insn-00ac9c50"></a> `00ac9c50` | `08 05 80 52` | mov w8,#0x28 | `FALL_THROUGH`
<a id="insn-00ac9c54"></a> `00ac9c54` | `03 00 00 14` | b 0x00ac9c60 | `UNCONDITIONAL_JUMP`
<a id="insn-00ac9c58"></a> `00ac9c58` | `08 04 80 52` | mov w8,#0x20 | `FALL_THROUGH`
<a id="insn-00ac9c5c"></a> `00ac9c5c` | `e0 03 00 91` | mov x0,sp | `FALL_THROUGH`
<a id="insn-00ac9c60"></a> `00ac9c60` | `09 00 40 f9` | ldr x9,[x0] | `FALL_THROUGH`
<a id="insn-00ac9c64"></a> `00ac9c64` | `28 69 68 f8` | ldr x8,[x9, x8, LSL #0x0] | `FALL_THROUGH`
<a id="insn-00ac9c68"></a> `00ac9c68` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00ac9c6c"></a> `00ac9c6c` | `74 6a 00 b9` | str w20,[x19, #0x68] | `FALL_THROUGH`
<a id="insn-00ac9c70"></a> `00ac9c70` | `23 22 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac9c74"></a> `00ac9c74` | `08 ae 86 52` | mov w8,#0x3570 | `FALL_THROUGH`
<a id="insn-00ac9c78"></a> `00ac9c78` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ac9c7c"></a> `00ac9c7c` | `20 22 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac9c80"></a> `00ac9c80` | `68 ae 86 52` | mov w8,#0x3573 | `FALL_THROUGH`
<a id="insn-00ac9c84"></a> `00ac9c84` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ac9c88"></a> `00ac9c88` | `1d 22 f6 97` | bl 0x008524fc | `UNCONDITIONAL_CALL`
<a id="insn-00ac9c8c"></a> `00ac9c8c` | `48 ae 86 52` | mov w8,#0x3572 | `FALL_THROUGH`
<a id="insn-00ac9c90"></a> `00ac9c90` | `7f f6 00 39` | strb wzr,[x19, #0x3d] | `FALL_THROUGH`
<a id="insn-00ac9c94"></a> `00ac9c94` | `1f 68 28 38` | strb wzr,[x0, x8, LSL ] | `FALL_THROUGH`
<a id="insn-00ac9c98"></a> `00ac9c98` | `a8 16 40 f9` | ldr x8,[x21, #0x28] | `FALL_THROUGH`
<a id="insn-00ac9c9c"></a> `00ac9c9c` | `a9 83 5f f8` | ldur x9,[x29, #-0x8] | `FALL_THROUGH`
<a id="insn-00ac9ca0"></a> `00ac9ca0` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00ac9ca4"></a> `00ac9ca4` | `c1 00 00 54` | b.ne 0x00ac9cbc | `CONDITIONAL_JUMP`
<a id="insn-00ac9ca8"></a> `00ac9ca8` | `f4 4f 46 a9` | ldp x20,x19,[sp, #0x60] | `FALL_THROUGH`
<a id="insn-00ac9cac"></a> `00ac9cac` | `f6 57 45 a9` | ldp x22,x21,[sp, #0x50] | `FALL_THROUGH`
<a id="insn-00ac9cb0"></a> `00ac9cb0` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00ac9cb4"></a> `00ac9cb4` | `ff c3 01 91` | add sp,sp,#0x70 | `FALL_THROUGH`
<a id="insn-00ac9cb8"></a> `00ac9cb8` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00ac9cbc"></a> `00ac9cbc` | `b1 3c 06 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00ac9bac`](#insn-00ac9bac) 範囲 `[['00ac9bac', '00ac9bcb']]`
  - `FALL_THROUGH` [`00ac9bc8`](#insn-00ac9bc8) → [`00ac9bcc`](#insn-00ac9bcc)
- ブロック [`00ac9bcc`](#insn-00ac9bcc) 範囲 `[['00ac9bcc', '00ac9bef']]`
  - `CONDITIONAL_JUMP` [`00ac9bec`](#insn-00ac9bec) → [`00ac9c0c`](#insn-00ac9c0c)
  - `FALL_THROUGH` [`00ac9bec`](#insn-00ac9bec) → [`00ac9bf0`](#insn-00ac9bf0)
- ブロック [`00ac9bf0`](#insn-00ac9bf0) 範囲 `[['00ac9bf0', '00ac9bf7']]`
  - `CONDITIONAL_JUMP` [`00ac9bf4`](#insn-00ac9bf4) → [`00ac9c14`](#insn-00ac9c14)
  - `FALL_THROUGH` [`00ac9bf4`](#insn-00ac9bf4) → [`00ac9bf8`](#insn-00ac9bf8)
- ブロック [`00ac9bf8`](#insn-00ac9bf8) 範囲 `[['00ac9bf8', '00ac9c0b']]`
  - `UNCONDITIONAL_JUMP` [`00ac9c08`](#insn-00ac9c08) → [`00ac9c30`](#insn-00ac9c30)
- ブロック [`00ac9c0c`](#insn-00ac9c0c) 範囲 `[['00ac9c0c', '00ac9c13']]`
  - `UNCONDITIONAL_JUMP` [`00ac9c10`](#insn-00ac9c10) → [`00ac9c30`](#insn-00ac9c30)
- ブロック [`00ac9c14`](#insn-00ac9c14) 範囲 `[['00ac9c14', '00ac9c2f']]`
  - `FALL_THROUGH` [`00ac9c2c`](#insn-00ac9c2c) → [`00ac9c30`](#insn-00ac9c30)
- ブロック [`00ac9c30`](#insn-00ac9c30) 範囲 `[['00ac9c30', '00ac9c4b']]`
  - `CONDITIONAL_JUMP` [`00ac9c48`](#insn-00ac9c48) → [`00ac9c58`](#insn-00ac9c58)
  - `FALL_THROUGH` [`00ac9c48`](#insn-00ac9c48) → [`00ac9c4c`](#insn-00ac9c4c)
- ブロック [`00ac9c4c`](#insn-00ac9c4c) 範囲 `[['00ac9c4c', '00ac9c4f']]`
  - `CONDITIONAL_JUMP` [`00ac9c4c`](#insn-00ac9c4c) → [`00ac9c6c`](#insn-00ac9c6c)
  - `FALL_THROUGH` [`00ac9c4c`](#insn-00ac9c4c) → [`00ac9c50`](#insn-00ac9c50)
- ブロック [`00ac9c50`](#insn-00ac9c50) 範囲 `[['00ac9c50', '00ac9c57']]`
  - `UNCONDITIONAL_JUMP` [`00ac9c54`](#insn-00ac9c54) → [`00ac9c60`](#insn-00ac9c60)
- ブロック [`00ac9c58`](#insn-00ac9c58) 範囲 `[['00ac9c58', '00ac9c5f']]`
  - `FALL_THROUGH` [`00ac9c5c`](#insn-00ac9c5c) → [`00ac9c60`](#insn-00ac9c60)
- ブロック [`00ac9c60`](#insn-00ac9c60) 範囲 `[['00ac9c60', '00ac9c6b']]`
  - `FALL_THROUGH` [`00ac9c68`](#insn-00ac9c68) → [`00ac9c6c`](#insn-00ac9c6c)
- ブロック [`00ac9c6c`](#insn-00ac9c6c) 範囲 `[['00ac9c6c', '00ac9ca7']]`
  - `CONDITIONAL_JUMP` [`00ac9ca4`](#insn-00ac9ca4) → [`00ac9cbc`](#insn-00ac9cbc)
  - `FALL_THROUGH` [`00ac9ca4`](#insn-00ac9ca4) → [`00ac9ca8`](#insn-00ac9ca8)
- ブロック [`00ac9ca8`](#insn-00ac9ca8) 範囲 `[['00ac9ca8', '00ac9cbb']]`
- ブロック [`00ac9cbc`](#insn-00ac9cbc) 範囲 `[['00ac9cbc', '00ac9cbf']]`

## 命令位置別の参照

- [`00ac9bb0`](#insn-00ac9bb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bb4`](#insn-00ac9bb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bb8`](#insn-00ac9bb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bd8`](#insn-00ac9bd8) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bec`](#insn-00ac9bec) → [`00ac9c0c`](#insn-00ac9c0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9bf4`](#insn-00ac9bf4) → [`00ac9c14`](#insn-00ac9c14) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c04`](#insn-00ac9c04) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c08`](#insn-00ac9c08) → [`00ac9c30`](#insn-00ac9c30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c0c`](#insn-00ac9c0c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c10`](#insn-00ac9c10) → [`00ac9c30`](#insn-00ac9c30) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c20`](#insn-00ac9c20) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c3c`](#insn-00ac9c3c) → [`0057c9b4`](../0057c/0057c9b4.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `0057c9b4` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c40`](#insn-00ac9c40) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c48`](#insn-00ac9c48) → [`00ac9c58`](#insn-00ac9c58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c4c`](#insn-00ac9c4c) → [`00ac9c6c`](#insn-00ac9c6c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c54`](#insn-00ac9c54) → [`00ac9c60`](#insn-00ac9c60) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c60`](#insn-00ac9c60) → `Stack[-0x70]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c70`](#insn-00ac9c70) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c7c`](#insn-00ac9c7c) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c88`](#insn-00ac9c88) → [`008524fc`](../00852/008524fc.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `008524fc` · 推定シンボル `None` · 推定型 `None`
- [`00ac9c9c`](#insn-00ac9c9c) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ca4`](#insn-00ac9ca4) → [`00ac9cbc`](#insn-00ac9cbc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9ca8`](#insn-00ac9ca8) → `Stack[-0x10]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9cac`](#insn-00ac9cac) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9cb0`](#insn-00ac9cb0) → `Stack[-0x30]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00ac9cbc`](#insn-00ac9cbc) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00ac9bb0`](#insn-00ac9bb0)

~~~json
{
  "source": "00ac9bb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bb4`](#insn-00ac9bb4)

~~~json
{
  "source": "00ac9bb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bb8`](#insn-00ac9bb8)

~~~json
{
  "source": "00ac9bb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bd8`](#insn-00ac9bd8)

~~~json
{
  "source": "00ac9bd8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bec`](#insn-00ac9bec)

~~~json
{
  "source": "00ac9bec",
  "target": "00ac9c0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9bf4`](#insn-00ac9bf4)

~~~json
{
  "source": "00ac9bf4",
  "target": "00ac9c14",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c04`](#insn-00ac9c04)

~~~json
{
  "source": "00ac9c04",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c08`](#insn-00ac9c08)

~~~json
{
  "source": "00ac9c08",
  "target": "00ac9c30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c0c`](#insn-00ac9c0c)

~~~json
{
  "source": "00ac9c0c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c10`](#insn-00ac9c10)

~~~json
{
  "source": "00ac9c10",
  "target": "00ac9c30",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c20`](#insn-00ac9c20)

~~~json
{
  "source": "00ac9c20",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c3c`](#insn-00ac9c3c)

~~~json
{
  "source": "00ac9c3c",
  "target": "0057c9b4",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9c40`](#insn-00ac9c40)

~~~json
{
  "source": "00ac9c40",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c48`](#insn-00ac9c48)

~~~json
{
  "source": "00ac9c48",
  "target": "00ac9c58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c4c`](#insn-00ac9c4c)

~~~json
{
  "source": "00ac9c4c",
  "target": "00ac9c6c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c54`](#insn-00ac9c54)

~~~json
{
  "source": "00ac9c54",
  "target": "00ac9c60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c60`](#insn-00ac9c60)

~~~json
{
  "source": "00ac9c60",
  "target": "Stack[-0x70]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9c70`](#insn-00ac9c70)

~~~json
{
  "source": "00ac9c70",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9c7c`](#insn-00ac9c7c)

~~~json
{
  "source": "00ac9c7c",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9c88`](#insn-00ac9c88)

~~~json
{
  "source": "00ac9c88",
  "target": "008524fc",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00ac9c9c`](#insn-00ac9c9c)

~~~json
{
  "source": "00ac9c9c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ca4`](#insn-00ac9ca4)

~~~json
{
  "source": "00ac9ca4",
  "target": "00ac9cbc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9ca8`](#insn-00ac9ca8)

~~~json
{
  "source": "00ac9ca8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9cac`](#insn-00ac9cac)

~~~json
{
  "source": "00ac9cac",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9cb0`](#insn-00ac9cb0)

~~~json
{
  "source": "00ac9cb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00ac9cbc`](#insn-00ac9cbc)

~~~json
{
  "source": "00ac9cbc",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
