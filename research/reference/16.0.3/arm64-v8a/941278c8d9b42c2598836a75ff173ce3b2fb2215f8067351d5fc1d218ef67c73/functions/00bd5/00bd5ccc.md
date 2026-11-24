# 00bd5ccc

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00bd4cd8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00bd4/00bd4cd8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0010.md#compare-b087b674273f72f86fa9d52813eabfa1)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00bd5ccc",
  "name": "_ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv",
  "size": 280,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "f5f7f433c47db5903671a92f4b6c789d65c12267216ea3b4a8e423c0f288cd4c",
  "source_text_sha256": "f5f7f433c47db5903671a92f4b6c789d65c12267216ea3b4a8e423c0f288cd4c",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00bd5ccc",
        "00bd5de3"
      ]
    ],
    "bytes_sha256": "62eaa1ab514543ceab224f754e03be2013ce7097a5da2b65a47da142f51b6e86",
    "instruction_count": 70,
    "instruction_bytes": 280,
    "body_bytes": 280,
    "indirect": 3,
    "unresolved": 3
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00497b94](../00497/00497b94.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c5bad0](../00c5b/00c5bad0.md)
- [00c5baf0](../00c5b/00c5baf0.md)
- [00c5c000](../00c5c/00c5c000.md)
- [00c5c120](../00c5c/00c5c120.md)
- [00c5ee50](../00c5e/00c5ee50.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1427 bytes

~~~c

void _ZN8firebase4auth22ReadUserFromAuthResultEP8_jobjectPNS0_18FutureCallbackDataINS0_4UserEEEbPv
               (long param_1,long param_2,ulong param_3,undefined8 param_4)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  undefined8 uVar4;
  long lVar5;
  undefined1 auStack_f8 [160];
  long local_58;
  
  lVar1 = tpidr_el0;
  local_58 = *(long *)(lVar1 + 0x28);
  plVar2 = (long *)_ZNK8firebase3App9GetJNIEnvEv(**(undefined8 **)(param_2 + 0x10));
  if ((param_1 != 0) && ((param_3 & 1) != 0)) {
    lVar3 = FUN_00497b94(plVar2,param_1,DAT_01127918);
    _ZN8firebase4util26CheckAndClearJniExceptionsEP7_JNIEnv(plVar2);
    lVar5 = *(long *)(param_2 + 0x10);
    if (*(long *)(lVar5 + 0x200) != 0) {
      (**(code **)(*plVar2 + 0xb0))(plVar2);
      *(undefined8 *)(lVar5 + 0x200) = 0;
    }
    if (lVar3 != 0) {
      uVar4 = (**(code **)(*plVar2 + 0xa8))(plVar2,lVar3);
      (**(code **)(*plVar2 + 0xb8))(plVar2,lVar3);
      *(undefined8 *)(lVar5 + 0x200) = uVar4;
    }
  }
  _ZN8firebase4auth4Auth12current_userEv(auStack_f8,*(undefined8 *)(*(long *)(param_2 + 0x10) + 8));
  _ZN8firebase4auth4UseraSERKS1_(param_4,auStack_f8);
                    /* try { // try from 00bd5dac to 00cd5f97 has its CatchHandler @ 00bd7a18 */
  _ZN8firebase4auth4UserD2Ev(auStack_f8);
  if (*(long *)(lVar1 + 0x28) == local_58) {
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
<a id="insn-00bd5ccc"></a> `00bd5ccc` | `ff 03 04 d1` | sub sp,sp,#0x100 | `FALL_THROUGH`
<a id="insn-00bd5cd0"></a> `00bd5cd0` | `f9 5b 00 f9` | str x25,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd5cd4"></a> `00bd5cd4` | `f8 5f 0c a9` | stp x24,x23,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bd5cd8"></a> `00bd5cd8` | `f6 57 0d a9` | stp x22,x21,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bd5cdc"></a> `00bd5cdc` | `f4 4f 0e a9` | stp x20,x19,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bd5ce0"></a> `00bd5ce0` | `fd 7b 0f a9` | stp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00bd5ce4"></a> `00bd5ce4` | `fd c3 03 91` | add x29,sp,#0xf0 | `FALL_THROUGH`
<a id="insn-00bd5ce8"></a> `00bd5ce8` | `58 d0 3b d5` | mrs x24,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00bd5cec"></a> `00bd5cec` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bd5cf0"></a> `00bd5cf0` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bd5cf4"></a> `00bd5cf4` | `f3 03 03 aa` | mov x19,x3 | `FALL_THROUGH`
<a id="insn-00bd5cf8"></a> `00bd5cf8` | `f7 03 02 2a` | mov w23,w2 | `FALL_THROUGH`
<a id="insn-00bd5cfc"></a> `00bd5cfc` | `a8 83 1b f8` | stur x8,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00bd5d00"></a> `00bd5d00` | `28 08 40 f9` | ldr x8,[x1, #0x10] | `FALL_THROUGH`
<a id="insn-00bd5d04"></a> `00bd5d04` | `f4 03 01 aa` | mov x20,x1 | `FALL_THROUGH`
<a id="insn-00bd5d08"></a> `00bd5d08` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00bd5d0c"></a> `00bd5d0c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00bd5d10"></a> `00bd5d10` | `04 19 02 94` | bl 0x00c5c120 | `UNCONDITIONAL_CALL`
<a id="insn-00bd5d14"></a> `00bd5d14` | `f6 03 00 b4` | cbz x22,0x00bd5d90 | `CONDITIONAL_JUMP`
<a id="insn-00bd5d18"></a> `00bd5d18` | `d7 03 00 36` | tbz w23,#0x0,0x00bd5d90 | `CONDITIONAL_JUMP`
<a id="insn-00bd5d1c"></a> `00bd5d1c` | `88 2a 00 d0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00bd5d20"></a> `00bd5d20` | `02 8d 44 f9` | ldr x2,[x8, #0x918] | `FALL_THROUGH`
<a id="insn-00bd5d24"></a> `00bd5d24` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bd5d28"></a> `00bd5d28` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00bd5d2c"></a> `00bd5d2c` | `9a 07 e3 97` | bl 0x00497b94 | `UNCONDITIONAL_CALL`
<a id="insn-00bd5d30"></a> `00bd5d30` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00bd5d34"></a> `00bd5d34` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd5d38"></a> `00bd5d38` | `b2 18 02 94` | bl 0x00c5c000 | `UNCONDITIONAL_CALL`
<a id="insn-00bd5d3c"></a> `00bd5d3c` | `99 0a 40 f9` | ldr x25,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bd5d40"></a> `00bd5d40` | `21 03 41 f9` | ldr x1,[x25, #0x200] | `FALL_THROUGH`
<a id="insn-00bd5d44"></a> `00bd5d44` | `c1 00 00 b4` | cbz x1,0x00bd5d5c | `CONDITIONAL_JUMP`
<a id="insn-00bd5d48"></a> `00bd5d48` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd5d4c"></a> `00bd5d4c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd5d50"></a> `00bd5d50` | `08 59 40 f9` | ldr x8,[x8, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd5d54"></a> `00bd5d54` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd5d58"></a> `00bd5d58` | `3f 03 01 f9` | str xzr,[x25, #0x200] | `FALL_THROUGH`
<a id="insn-00bd5d5c"></a> `00bd5d5c` | `b6 01 00 b4` | cbz x22,0x00bd5d90 | `CONDITIONAL_JUMP`
<a id="insn-00bd5d60"></a> `00bd5d60` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd5d64"></a> `00bd5d64` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd5d68"></a> `00bd5d68` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bd5d6c"></a> `00bd5d6c` | `08 55 40 f9` | ldr x8,[x8, #0xa8] | `FALL_THROUGH`
<a id="insn-00bd5d70"></a> `00bd5d70` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd5d74"></a> `00bd5d74` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00bd5d78"></a> `00bd5d78` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00bd5d7c"></a> `00bd5d7c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00bd5d80"></a> `00bd5d80` | `e1 03 16 aa` | mov x1,x22 | `FALL_THROUGH`
<a id="insn-00bd5d84"></a> `00bd5d84` | `08 5d 40 f9` | ldr x8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00bd5d88"></a> `00bd5d88` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00bd5d8c"></a> `00bd5d8c` | `37 03 01 f9` | str x23,[x25, #0x200] | `FALL_THROUGH`
<a id="insn-00bd5d90"></a> `00bd5d90` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00bd5d94"></a> `00bd5d94` | `00 05 40 f9` | ldr x0,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00bd5d98"></a> `00bd5d98` | `e8 23 00 91` | add x8,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bd5d9c"></a> `00bd5d9c` | `4d 17 02 94` | bl 0x00c5bad0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd5da0"></a> `00bd5da0` | `e1 23 00 91` | add x1,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bd5da4"></a> `00bd5da4` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00bd5da8"></a> `00bd5da8` | `2a 24 02 94` | bl 0x00c5ee50 | `UNCONDITIONAL_CALL`
<a id="insn-00bd5dac"></a> `00bd5dac` | `e0 23 00 91` | add x0,sp,#0x8 | `FALL_THROUGH`
<a id="insn-00bd5db0"></a> `00bd5db0` | `50 17 02 94` | bl 0x00c5baf0 | `UNCONDITIONAL_CALL`
<a id="insn-00bd5db4"></a> `00bd5db4` | `08 17 40 f9` | ldr x8,[x24, #0x28] | `FALL_THROUGH`
<a id="insn-00bd5db8"></a> `00bd5db8` | `a9 83 5b f8` | ldur x9,[x29, #-0x48] | `FALL_THROUGH`
<a id="insn-00bd5dbc"></a> `00bd5dbc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00bd5dc0"></a> `00bd5dc0` | `01 01 00 54` | b.ne 0x00bd5de0 | `CONDITIONAL_JUMP`
<a id="insn-00bd5dc4"></a> `00bd5dc4` | `fd 7b 4f a9` | ldp x29,x30,[sp, #0xf0] | `FALL_THROUGH`
<a id="insn-00bd5dc8"></a> `00bd5dc8` | `f4 4f 4e a9` | ldp x20,x19,[sp, #0xe0] | `FALL_THROUGH`
<a id="insn-00bd5dcc"></a> `00bd5dcc` | `f6 57 4d a9` | ldp x22,x21,[sp, #0xd0] | `FALL_THROUGH`
<a id="insn-00bd5dd0"></a> `00bd5dd0` | `f8 5f 4c a9` | ldp x24,x23,[sp, #0xc0] | `FALL_THROUGH`
<a id="insn-00bd5dd4"></a> `00bd5dd4` | `f9 5b 40 f9` | ldr x25,[sp, #0xb0] | `FALL_THROUGH`
<a id="insn-00bd5dd8"></a> `00bd5dd8` | `ff 03 04 91` | add sp,sp,#0x100 | `FALL_THROUGH`
<a id="insn-00bd5ddc"></a> `00bd5ddc` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00bd5de0"></a> `00bd5de0` | `68 0c 02 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00bd5ccc`](#insn-00bd5ccc) 範囲 `[['00bd5ccc', '00bd5d17']]`
  - `CONDITIONAL_JUMP` [`00bd5d14`](#insn-00bd5d14) → [`00bd5d90`](#insn-00bd5d90)
  - `FALL_THROUGH` [`00bd5d14`](#insn-00bd5d14) → [`00bd5d18`](#insn-00bd5d18)
- ブロック [`00bd5d18`](#insn-00bd5d18) 範囲 `[['00bd5d18', '00bd5d1b']]`
  - `CONDITIONAL_JUMP` [`00bd5d18`](#insn-00bd5d18) → [`00bd5d90`](#insn-00bd5d90)
  - `FALL_THROUGH` [`00bd5d18`](#insn-00bd5d18) → [`00bd5d1c`](#insn-00bd5d1c)
- ブロック [`00bd5d1c`](#insn-00bd5d1c) 範囲 `[['00bd5d1c', '00bd5d47']]`
  - `CONDITIONAL_JUMP` [`00bd5d44`](#insn-00bd5d44) → [`00bd5d5c`](#insn-00bd5d5c)
  - `FALL_THROUGH` [`00bd5d44`](#insn-00bd5d44) → [`00bd5d48`](#insn-00bd5d48)
- ブロック [`00bd5d48`](#insn-00bd5d48) 範囲 `[['00bd5d48', '00bd5d5b']]`
  - `FALL_THROUGH` [`00bd5d58`](#insn-00bd5d58) → [`00bd5d5c`](#insn-00bd5d5c)
- ブロック [`00bd5d5c`](#insn-00bd5d5c) 範囲 `[['00bd5d5c', '00bd5d5f']]`
  - `CONDITIONAL_JUMP` [`00bd5d5c`](#insn-00bd5d5c) → [`00bd5d90`](#insn-00bd5d90)
  - `FALL_THROUGH` [`00bd5d5c`](#insn-00bd5d5c) → [`00bd5d60`](#insn-00bd5d60)
- ブロック [`00bd5d60`](#insn-00bd5d60) 範囲 `[['00bd5d60', '00bd5d8f']]`
  - `FALL_THROUGH` [`00bd5d8c`](#insn-00bd5d8c) → [`00bd5d90`](#insn-00bd5d90)
- ブロック [`00bd5d90`](#insn-00bd5d90) 範囲 `[['00bd5d90', '00bd5dab']]`
  - `FALL_THROUGH` [`00bd5da8`](#insn-00bd5da8) → [`00bd5dac`](#insn-00bd5dac)
- ブロック [`00bd5dac`](#insn-00bd5dac) 範囲 `[['00bd5dac', '00bd5dc3']]`
  - `CONDITIONAL_JUMP` [`00bd5dc0`](#insn-00bd5dc0) → [`00bd5de0`](#insn-00bd5de0)
  - `FALL_THROUGH` [`00bd5dc0`](#insn-00bd5dc0) → [`00bd5dc4`](#insn-00bd5dc4)
- ブロック [`00bd5dc4`](#insn-00bd5dc4) 範囲 `[['00bd5dc4', '00bd5ddf']]`
- ブロック [`00bd5de0`](#insn-00bd5de0) 範囲 `[['00bd5de0', '00bd5de3']]`

## 命令位置別の参照

- [`00bd5cd0`](#insn-00bd5cd0) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5cd4`](#insn-00bd5cd4) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5cd8`](#insn-00bd5cd8) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5cdc`](#insn-00bd5cdc) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5ce0`](#insn-00bd5ce0) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5cfc`](#insn-00bd5cfc) → `Stack[-0x58]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5d10`](#insn-00bd5d10) → [`00c5c120`](../00c5c/00c5c120.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c120` · 推定シンボル `None` · 推定型 `None`
- [`00bd5d14`](#insn-00bd5d14) → [`00bd5d90`](#insn-00bd5d90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5d18`](#insn-00bd5d18) → [`00bd5d90`](#insn-00bd5d90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5d20`](#insn-00bd5d20) → `01127918`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00bd5d2c`](#insn-00bd5d2c) → [`00497b94`](../00497/00497b94.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00497b94` · 推定シンボル `None` · 推定型 `None`
- [`00bd5d38`](#insn-00bd5d38) → [`00c5c000`](../00c5c/00c5c000.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5c000` · 推定シンボル `None` · 推定型 `None`
- [`00bd5d44`](#insn-00bd5d44) → [`00bd5d5c`](#insn-00bd5d5c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5d5c`](#insn-00bd5d5c) → [`00bd5d90`](#insn-00bd5d90) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5d9c`](#insn-00bd5d9c) → [`00c5bad0`](../00c5b/00c5bad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5bad0` · 推定シンボル `None` · 推定型 `None`
- [`00bd5da8`](#insn-00bd5da8) → [`00c5ee50`](../00c5e/00c5ee50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5ee50` · 推定シンボル `None` · 推定型 `None`
- [`00bd5db0`](#insn-00bd5db0) → [`00c5baf0`](../00c5b/00c5baf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5baf0` · 推定シンボル `None` · 推定型 `None`
- [`00bd5db8`](#insn-00bd5db8) → `Stack[-0x58]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5dc0`](#insn-00bd5dc0) → [`00bd5de0`](#insn-00bd5de0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5dc4`](#insn-00bd5dc4) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5dc8`](#insn-00bd5dc8) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5dcc`](#insn-00bd5dcc) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5dd0`](#insn-00bd5dd0) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5dd4`](#insn-00bd5dd4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00bd5de0`](#insn-00bd5de0) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00bd5cd0`](#insn-00bd5cd0)

~~~json
{
  "source": "00bd5cd0",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5cd4`](#insn-00bd5cd4)

~~~json
{
  "source": "00bd5cd4",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5cd8`](#insn-00bd5cd8)

~~~json
{
  "source": "00bd5cd8",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5cdc`](#insn-00bd5cdc)

~~~json
{
  "source": "00bd5cdc",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5ce0`](#insn-00bd5ce0)

~~~json
{
  "source": "00bd5ce0",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5cfc`](#insn-00bd5cfc)

~~~json
{
  "source": "00bd5cfc",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5d10`](#insn-00bd5d10)

~~~json
{
  "source": "00bd5d10",
  "target": "00c5c120",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd5d14`](#insn-00bd5d14)

~~~json
{
  "source": "00bd5d14",
  "target": "00bd5d90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5d18`](#insn-00bd5d18)

~~~json
{
  "source": "00bd5d18",
  "target": "00bd5d90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5d20`](#insn-00bd5d20)

~~~json
{
  "source": "00bd5d20",
  "target": "01127918",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01127918",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00bd5d2c`](#insn-00bd5d2c)

~~~json
{
  "source": "00bd5d2c",
  "target": "00497b94",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd5d38`](#insn-00bd5d38)

~~~json
{
  "source": "00bd5d38",
  "target": "00c5c000",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd5d44`](#insn-00bd5d44)

~~~json
{
  "source": "00bd5d44",
  "target": "00bd5d5c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5d5c`](#insn-00bd5d5c)

~~~json
{
  "source": "00bd5d5c",
  "target": "00bd5d90",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5d9c`](#insn-00bd5d9c)

~~~json
{
  "source": "00bd5d9c",
  "target": "00c5bad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd5da8`](#insn-00bd5da8)

~~~json
{
  "source": "00bd5da8",
  "target": "00c5ee50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd5db0`](#insn-00bd5db0)

~~~json
{
  "source": "00bd5db0",
  "target": "00c5baf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00bd5db8`](#insn-00bd5db8)

~~~json
{
  "source": "00bd5db8",
  "target": "Stack[-0x58]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5dc0`](#insn-00bd5dc0)

~~~json
{
  "source": "00bd5dc0",
  "target": "00bd5de0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5dc4`](#insn-00bd5dc4)

~~~json
{
  "source": "00bd5dc4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5dc8`](#insn-00bd5dc8)

~~~json
{
  "source": "00bd5dc8",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5dcc`](#insn-00bd5dcc)

~~~json
{
  "source": "00bd5dcc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5dd0`](#insn-00bd5dd0)

~~~json
{
  "source": "00bd5dd0",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5dd4`](#insn-00bd5dd4)

~~~json
{
  "source": "00bd5dd4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00bd5de0`](#insn-00bd5de0)

~~~json
{
  "source": "00bd5de0",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
