# 00b5ceac

版: 16.0.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73`

解析リビジョン `9afc4f9e264e1fda` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.2**
  - 採用 · [関数詳細 `00b5beb8`](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/functions/00b5b/00b5beb8.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0008.md#compare-0aed1fcd4cfa144718744ee0d529f9d4)
  - [v16.0.2の関数一覧](../../../../../16.0.2/arm64-v8a/baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6/README.md)

- **次の公開版** 公開版なし

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5ceac",
  "name": "_ZN8firebase8callback19AddBlockingCallbackEPNS0_8CallbackE",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5150549079e943c0218f5b1d22dcd499ab4f9bb70695e237f27ca6feb79d80c2",
  "source_text_sha256": "5150549079e943c0218f5b1d22dcd499ab4f9bb70695e237f27ca6feb79d80c2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b6bda0ebc7fc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5ceac",
        "00b5cf9b"
      ]
    ],
    "bytes_sha256": "f2aa6c8fcb2baf309ea7dbfa095442df8a39fa5319fda32be62c3b36152562da",
    "instruction_count": 60,
    "instruction_bytes": 240,
    "body_bytes": 240,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00c58f30](../00c58/00c58f30.md)
- [00c58f80](../00c58/00c58f80.md)
- [00c596c0](../00c59/00c596c0.md)
- [00c5cb90](../00c5c/00c5cb90.md)
- [00c5cbf0](../00c5c/00c5cbf0.md)
- [00c5cc00](../00c5c/00c5cc00.md)
- [00c5cc10](../00c5c/00c5cc10.md)
- [00c5cc30](../00c5c/00c5cc30.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1355 bytes

~~~c

void _ZN8firebase8callback19AddBlockingCallbackEPNS0_8CallbackE(long *param_1)

{
  long lVar1;
  undefined *puVar2;
  int iVar3;
  uint uVar4;
  pthread_t __thread1;
  ulong uVar5;
  long *plVar6;
  sem_t *local_50 [3];
  long local_38;
  
  lVar1 = tpidr_el0;
  local_38 = *(long *)(lVar1 + 0x28);
  if (DAT_011270b8 == '\x01') {
    __thread1 = pthread_self();
    if ((__thread1 == 0) || (DAT_011270c0 == 0)) {
      if (DAT_011270c0 != 0 || __thread1 != 0) goto LAB_00b5cf2c;
    }
    else {
      iVar3 = pthread_equal(__thread1,DAT_011270c0);
      if (iVar3 == 0) goto LAB_00b5cf2c;
    }
    uVar5 = (**(code **)(*param_1 + 0x10))(param_1);
    if (param_1 != (long *)0x0) {
      uVar5 = (**(code **)(*param_1 + 8))(param_1);
    }
  }
  else {
LAB_00b5cf2c:
    local_50[0] = (sem_t *)(local_50 + 1);
    sem_init(local_50[0],0,0);
    plVar6 = (long *)_Znwm(0x18);
    puVar2 = PTR__ZTVN8firebase8callback16BlockingCallbackE_00c9c820;
    plVar6[2] = (long)local_50;
    *plVar6 = (long)(puVar2 + 0x10);
    plVar6[1] = (long)param_1;
    _ZN8firebase8callback11AddCallbackEPNS0_8CallbackE();
    sem_wait(local_50[0]);
    uVar4 = sem_destroy(local_50[0]);
    uVar5 = (ulong)uVar4;
  }
  if (*(long *)(lVar1 + 0x28) == local_38) {
    return;
  }
                    /* WARNING: Subroutine does not return */
  __stack_chk_fail(uVar5);
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5ceac"></a> `00b5ceac` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b5ceb0"></a> `00b5ceb0` | `f5 13 00 f9` | str x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5ceb4"></a> `00b5ceb4` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5ceb8"></a> `00b5ceb8` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5cebc"></a> `00b5cebc` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b5cec0"></a> `00b5cec0` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00b5cec4"></a> `00b5cec4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b5cec8"></a> `00b5cec8` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00b5cecc"></a> `00b5cecc` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b5ced0"></a> `00b5ced0` | `48 2e 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00b5ced4"></a> `00b5ced4` | `08 e1 42 39` | ldrb w8,[x8, #0xb8] | `FALL_THROUGH`
<a id="insn-00b5ced8"></a> `00b5ced8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5cedc"></a> `00b5cedc` | `81 02 00 54` | b.ne 0x00b5cf2c | `CONDITIONAL_JUMP`
<a id="insn-00b5cee0"></a> `00b5cee0` | `f8 f1 03 94` | bl 0x00c596c0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cee4"></a> `00b5cee4` | `48 2e 00 f0` | adrp x8,0x1127000 | `FALL_THROUGH`
<a id="insn-00b5cee8"></a> `00b5cee8` | `01 61 40 f9` | ldr x1,[x8, #0xc0] | `FALL_THROUGH`
<a id="insn-00b5ceec"></a> `00b5ceec` | `c0 01 00 b4` | cbz x0,0x00b5cf24 | `CONDITIONAL_JUMP`
<a id="insn-00b5cef0"></a> `00b5cef0` | `a1 01 00 b4` | cbz x1,0x00b5cf24 | `CONDITIONAL_JUMP`
<a id="insn-00b5cef4"></a> `00b5cef4` | `3f ff 03 94` | bl 0x00c5cbf0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cef8"></a> `00b5cef8` | `a0 01 00 34` | cbz w0,0x00b5cf2c | `CONDITIONAL_JUMP`
<a id="insn-00b5cefc"></a> `00b5cefc` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b5cf00"></a> `00b5cf00` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5cf04"></a> `00b5cf04` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cf08"></a> `00b5cf08` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5cf0c"></a> `00b5cf0c` | `53 03 00 b4` | cbz x19,0x00b5cf74 | `CONDITIONAL_JUMP`
<a id="insn-00b5cf10"></a> `00b5cf10` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00b5cf14"></a> `00b5cf14` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5cf18"></a> `00b5cf18` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b5cf1c"></a> `00b5cf1c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5cf20"></a> `00b5cf20` | `15 00 00 14` | b 0x00b5cf74 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5cf24"></a> `00b5cf24` | `28 00 00 aa` | orr x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00b5cf28"></a> `00b5cf28` | `a8 fe ff b4` | cbz x8,0x00b5cefc | `CONDITIONAL_JUMP`
<a id="insn-00b5cf2c"></a> `00b5cf2c` | `f5 03 00 91` | mov x21,sp | `FALL_THROUGH`
<a id="insn-00b5cf30"></a> `00b5cf30` | `a0 22 00 91` | add x0,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00b5cf34"></a> `00b5cf34` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00b5cf38"></a> `00b5cf38` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00b5cf3c"></a> `00b5cf3c` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-00b5cf40"></a> `00b5cf40` | `34 ff 03 94` | bl 0x00c5cc10 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cf44"></a> `00b5cf44` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-00b5cf48"></a> `00b5cf48` | `fa ef 03 94` | bl 0x00c58f30 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cf4c"></a> `00b5cf4c` | `08 0a 00 90` | adrp x8,0xc9c000 | `FALL_THROUGH`
<a id="insn-00b5cf50"></a> `00b5cf50` | `08 11 44 f9` | ldr x8,[x8, #0x820] | `FALL_THROUGH`
<a id="insn-00b5cf54"></a> `00b5cf54` | `15 08 00 f9` | str x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cf58"></a> `00b5cf58` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00b5cf5c"></a> `00b5cf5c` | `08 4c 00 a9` | stp x8,x19,[x0] | `FALL_THROUGH`
<a id="insn-00b5cf60"></a> `00b5cf60` | `0c ff 03 94` | bl 0x00c5cb90 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cf64"></a> `00b5cf64` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00b5cf68"></a> `00b5cf68` | `32 ff 03 94` | bl 0x00c5cc30 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cf6c"></a> `00b5cf6c` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00b5cf70"></a> `00b5cf70` | `24 ff 03 94` | bl 0x00c5cc00 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cf74"></a> `00b5cf74` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00b5cf78"></a> `00b5cf78` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00b5cf7c"></a> `00b5cf7c` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00b5cf80"></a> `00b5cf80` | `c1 00 00 54` | b.ne 0x00b5cf98 | `CONDITIONAL_JUMP`
<a id="insn-00b5cf84"></a> `00b5cf84` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5cf88"></a> `00b5cf88` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5cf8c"></a> `00b5cf8c` | `f5 13 40 f9` | ldr x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5cf90"></a> `00b5cf90` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00b5cf94"></a> `00b5cf94` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00b5cf98"></a> `00b5cf98` | `fa ef 03 94` | bl 0x00c58f80 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5ceac`](#insn-00b5ceac) 範囲 `[['00b5ceac', '00b5cedf']]`
  - `CONDITIONAL_JUMP` [`00b5cedc`](#insn-00b5cedc) → [`00b5cf2c`](#insn-00b5cf2c)
  - `FALL_THROUGH` [`00b5cedc`](#insn-00b5cedc) → [`00b5cee0`](#insn-00b5cee0)
- ブロック [`00b5cee0`](#insn-00b5cee0) 範囲 `[['00b5cee0', '00b5ceef']]`
  - `CONDITIONAL_JUMP` [`00b5ceec`](#insn-00b5ceec) → [`00b5cf24`](#insn-00b5cf24)
  - `FALL_THROUGH` [`00b5ceec`](#insn-00b5ceec) → [`00b5cef0`](#insn-00b5cef0)
- ブロック [`00b5cef0`](#insn-00b5cef0) 範囲 `[['00b5cef0', '00b5cef3']]`
  - `CONDITIONAL_JUMP` [`00b5cef0`](#insn-00b5cef0) → [`00b5cf24`](#insn-00b5cf24)
  - `FALL_THROUGH` [`00b5cef0`](#insn-00b5cef0) → [`00b5cef4`](#insn-00b5cef4)
- ブロック [`00b5cef4`](#insn-00b5cef4) 範囲 `[['00b5cef4', '00b5cefb']]`
  - `CONDITIONAL_JUMP` [`00b5cef8`](#insn-00b5cef8) → [`00b5cf2c`](#insn-00b5cf2c)
  - `FALL_THROUGH` [`00b5cef8`](#insn-00b5cef8) → [`00b5cefc`](#insn-00b5cefc)
- ブロック [`00b5cefc`](#insn-00b5cefc) 範囲 `[['00b5cefc', '00b5cf0f']]`
  - `CONDITIONAL_JUMP` [`00b5cf0c`](#insn-00b5cf0c) → [`00b5cf74`](#insn-00b5cf74)
  - `FALL_THROUGH` [`00b5cf0c`](#insn-00b5cf0c) → [`00b5cf10`](#insn-00b5cf10)
- ブロック [`00b5cf10`](#insn-00b5cf10) 範囲 `[['00b5cf10', '00b5cf23']]`
  - `UNCONDITIONAL_JUMP` [`00b5cf20`](#insn-00b5cf20) → [`00b5cf74`](#insn-00b5cf74)
- ブロック [`00b5cf24`](#insn-00b5cf24) 範囲 `[['00b5cf24', '00b5cf2b']]`
  - `CONDITIONAL_JUMP` [`00b5cf28`](#insn-00b5cf28) → [`00b5cefc`](#insn-00b5cefc)
  - `FALL_THROUGH` [`00b5cf28`](#insn-00b5cf28) → [`00b5cf2c`](#insn-00b5cf2c)
- ブロック [`00b5cf2c`](#insn-00b5cf2c) 範囲 `[['00b5cf2c', '00b5cf73']]`
  - `FALL_THROUGH` [`00b5cf70`](#insn-00b5cf70) → [`00b5cf74`](#insn-00b5cf74)
- ブロック [`00b5cf74`](#insn-00b5cf74) 範囲 `[['00b5cf74', '00b5cf83']]`
  - `CONDITIONAL_JUMP` [`00b5cf80`](#insn-00b5cf80) → [`00b5cf98`](#insn-00b5cf98)
  - `FALL_THROUGH` [`00b5cf80`](#insn-00b5cf80) → [`00b5cf84`](#insn-00b5cf84)
- ブロック [`00b5cf84`](#insn-00b5cf84) 範囲 `[['00b5cf84', '00b5cf97']]`
- ブロック [`00b5cf98`](#insn-00b5cf98) 範囲 `[['00b5cf98', '00b5cf9b']]`

## 命令位置別の参照

- [`00b5ceb0`](#insn-00b5ceb0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ceb4`](#insn-00b5ceb4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ceb8`](#insn-00b5ceb8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cecc`](#insn-00b5cecc) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5ced4`](#insn-00b5ced4) → `011270b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00b5cedc`](#insn-00b5cedc) → [`00b5cf2c`](#insn-00b5cf2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cee0`](#insn-00b5cee0) → [`00c596c0`](../00c59/00c596c0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c596c0` · 推定シンボル `None` · 推定型 `None`
- [`00b5cee8`](#insn-00b5cee8) → `011270c0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00b5ceec`](#insn-00b5ceec) → [`00b5cf24`](#insn-00b5cf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cef0`](#insn-00b5cef0) → [`00b5cf24`](#insn-00b5cf24) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cef4`](#insn-00b5cef4) → [`00c5cbf0`](../00c5c/00c5cbf0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cbf0` · 推定シンボル `None` · 推定型 `None`
- [`00b5cef8`](#insn-00b5cef8) → [`00b5cf2c`](#insn-00b5cf2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf0c`](#insn-00b5cf0c) → [`00b5cf74`](#insn-00b5cf74) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf20`](#insn-00b5cf20) → [`00b5cf74`](#insn-00b5cf74) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf28`](#insn-00b5cf28) → [`00b5cefc`](#insn-00b5cefc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf3c`](#insn-00b5cf3c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf40`](#insn-00b5cf40) → [`00c5cc10`](../00c5c/00c5cc10.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cc10` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf48`](#insn-00b5cf48) → [`00c58f30`](../00c58/00c58f30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f30` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf50`](#insn-00b5cf50) → `00c9c820`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b5cf5c`](#insn-00b5cf5c) → `00c91408`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00b5cf60`](#insn-00b5cf60) → [`00c5cb90`](../00c5c/00c5cb90.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cb90` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf64`](#insn-00b5cf64) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf68`](#insn-00b5cf68) → [`00c5cc30`](../00c5c/00c5cc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cc30` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf6c`](#insn-00b5cf6c) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf70`](#insn-00b5cf70) → [`00c5cc00`](../00c5c/00c5cc00.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5cc00` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf78`](#insn-00b5cf78) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf80`](#insn-00b5cf80) → [`00b5cf98`](#insn-00b5cf98) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf84`](#insn-00b5cf84) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf88`](#insn-00b5cf88) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf8c`](#insn-00b5cf8c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf98`](#insn-00b5cf98) → [`00c58f80`](../00c58/00c58f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58f80` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5ceb0`](#insn-00b5ceb0)

~~~json
{
  "source": "00b5ceb0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ceb4`](#insn-00b5ceb4)

~~~json
{
  "source": "00b5ceb4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ceb8`](#insn-00b5ceb8)

~~~json
{
  "source": "00b5ceb8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cecc`](#insn-00b5cecc)

~~~json
{
  "source": "00b5cecc",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5ced4`](#insn-00b5ced4)

~~~json
{
  "source": "00b5ced4",
  "target": "011270b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011270b8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5cedc`](#insn-00b5cedc)

~~~json
{
  "source": "00b5cedc",
  "target": "00b5cf2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cee0`](#insn-00b5cee0)

~~~json
{
  "source": "00b5cee0",
  "target": "00c596c0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cee8`](#insn-00b5cee8)

~~~json
{
  "source": "00b5cee8",
  "target": "011270c0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "011270c0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5ceec`](#insn-00b5ceec)

~~~json
{
  "source": "00b5ceec",
  "target": "00b5cf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cef0`](#insn-00b5cef0)

~~~json
{
  "source": "00b5cef0",
  "target": "00b5cf24",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cef4`](#insn-00b5cef4)

~~~json
{
  "source": "00b5cef4",
  "target": "00c5cbf0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cef8`](#insn-00b5cef8)

~~~json
{
  "source": "00b5cef8",
  "target": "00b5cf2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf0c`](#insn-00b5cf0c)

~~~json
{
  "source": "00b5cf0c",
  "target": "00b5cf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf20`](#insn-00b5cf20)

~~~json
{
  "source": "00b5cf20",
  "target": "00b5cf74",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf28`](#insn-00b5cf28)

~~~json
{
  "source": "00b5cf28",
  "target": "00b5cefc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf3c`](#insn-00b5cf3c)

~~~json
{
  "source": "00b5cf3c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf40`](#insn-00b5cf40)

~~~json
{
  "source": "00b5cf40",
  "target": "00c5cc10",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cf48`](#insn-00b5cf48)

~~~json
{
  "source": "00b5cf48",
  "target": "00c58f30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cf50`](#insn-00b5cf50)

~~~json
{
  "source": "00b5cf50",
  "target": "00c9c820",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9c820",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b5cf5c`](#insn-00b5cf5c)

~~~json
{
  "source": "00b5cf5c",
  "target": "00c91408",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c913f8",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00b5cf60`](#insn-00b5cf60)

~~~json
{
  "source": "00b5cf60",
  "target": "00c5cb90",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cf64`](#insn-00b5cf64)

~~~json
{
  "source": "00b5cf64",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf68`](#insn-00b5cf68)

~~~json
{
  "source": "00b5cf68",
  "target": "00c5cc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cf6c`](#insn-00b5cf6c)

~~~json
{
  "source": "00b5cf6c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf70`](#insn-00b5cf70)

~~~json
{
  "source": "00b5cf70",
  "target": "00c5cc00",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cf78`](#insn-00b5cf78)

~~~json
{
  "source": "00b5cf78",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf80`](#insn-00b5cf80)

~~~json
{
  "source": "00b5cf80",
  "target": "00b5cf98",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf84`](#insn-00b5cf84)

~~~json
{
  "source": "00b5cf84",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf88`](#insn-00b5cf88)

~~~json
{
  "source": "00b5cf88",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf8c`](#insn-00b5cf8c)

~~~json
{
  "source": "00b5cf8c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf98`](#insn-00b5cf98)

~~~json
{
  "source": "00b5cf98",
  "target": "00c58f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
