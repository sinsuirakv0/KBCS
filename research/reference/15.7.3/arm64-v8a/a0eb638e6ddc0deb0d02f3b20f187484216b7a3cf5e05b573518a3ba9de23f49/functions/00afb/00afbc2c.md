# 00afbc2c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afbb64`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbb64.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-fab42784601654a61d75309923b3e9b9)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afbc70`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbc70.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-0ed2317eb94eb04e1e6591b28e13166b)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbc2c",
  "name": "_ZN8firebase8callback19AddBlockingCallbackEPNS0_8CallbackE",
  "size": 240,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "c712b1cab17365974a8b8d6e38eb6c5692351caabc0aba147d7b0b38125aa0d2",
  "source_text_sha256": "c712b1cab17365974a8b8d6e38eb6c5692351caabc0aba147d7b0b38125aa0d2",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbc2c",
        "00afbd1b"
      ]
    ],
    "bytes_sha256": "4290d9af6c4dba44bcc5e2d689e0eb8fc5d1e8e11537f6d98f4c9934fda7b0b1",
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

- [00bdaff0](../00bda/00bdaff0.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb780](../00bdb/00bdb780.md)
- [00bdebe0](../00bde/00bdebe0.md)
- [00bdec40](../00bde/00bdec40.md)
- [00bdec50](../00bde/00bdec50.md)
- [00bdec60](../00bde/00bdec60.md)
- [00bdec80](../00bde/00bdec80.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1549 bytes

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
  if (DAT_010a0cf8 == '\x01') {
    __thread1 = pthread_self();
    if ((__thread1 == 0) || (DAT_010a0d00 == 0)) {
      if (DAT_010a0d00 != 0 || __thread1 != 0) goto LAB_00afbcac;
    }
    else {
      iVar3 = pthread_equal(__thread1,DAT_010a0d00);
      if (iVar3 == 0) goto LAB_00afbcac;
    }
    uVar5 = (**(code **)(*param_1 + 0x10))(param_1);
    if (param_1 != (long *)0x0) {
                    /* try { // try from 00afbc98 to 00bfbcb3 has its CatchHandler @ 00aff410 */
      uVar5 = (**(code **)(*param_1 + 8))(param_1);
    }
  }
  else {
LAB_00afbcac:
    local_50[0] = (sem_t *)(local_50 + 1);
                    /* try { // try from 00afbcb4 to 00bfbd3f has its CatchHandler @ 00af560c */
    sem_init(local_50[0],0,0);
    plVar6 = (long *)_Znwm(0x18);
    puVar2 = PTR__ZTVN8firebase8callback16BlockingCallbackE_00c1b930;
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
<a id="insn-00afbc2c"></a> `00afbc2c` | `ff 43 01 d1` | sub sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afbc30"></a> `00afbc30` | `f5 13 00 f9` | str x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbc34"></a> `00afbc34` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afbc38"></a> `00afbc38` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afbc3c"></a> `00afbc3c` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00afbc40"></a> `00afbc40` | `54 d0 3b d5` | mrs x20,tpidr_el0 | `FALL_THROUGH`
<a id="insn-00afbc44"></a> `00afbc44` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00afbc48"></a> `00afbc48` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afbc4c"></a> `00afbc4c` | `e8 0f 00 f9` | str x8,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00afbc50"></a> `00afbc50` | `28 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbc54"></a> `00afbc54` | `08 e1 73 39` | ldrb w8,[x8, #0xcf8] | `FALL_THROUGH`
<a id="insn-00afbc58"></a> `00afbc58` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbc5c"></a> `00afbc5c` | `81 02 00 54` | b.ne 0x00afbcac | `CONDITIONAL_JUMP`
<a id="insn-00afbc60"></a> `00afbc60` | `c8 7e 03 94` | bl 0x00bdb780 | `UNCONDITIONAL_CALL`
<a id="insn-00afbc64"></a> `00afbc64` | `28 2d 00 b0` | adrp x8,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbc68"></a> `00afbc68` | `01 81 46 f9` | ldr x1,[x8, #0xd00] | `FALL_THROUGH`
<a id="insn-00afbc6c"></a> `00afbc6c` | `c0 01 00 b4` | cbz x0,0x00afbca4 | `CONDITIONAL_JUMP`
<a id="insn-00afbc70"></a> `00afbc70` | `a1 01 00 b4` | cbz x1,0x00afbca4 | `CONDITIONAL_JUMP`
<a id="insn-00afbc74"></a> `00afbc74` | `f3 8b 03 94` | bl 0x00bdec40 | `UNCONDITIONAL_CALL`
<a id="insn-00afbc78"></a> `00afbc78` | `a0 01 00 34` | cbz w0,0x00afbcac | `CONDITIONAL_JUMP`
<a id="insn-00afbc7c"></a> `00afbc7c` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afbc80"></a> `00afbc80` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbc84"></a> `00afbc84` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afbc88"></a> `00afbc88` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbc8c"></a> `00afbc8c` | `53 03 00 b4` | cbz x19,0x00afbcf4 | `CONDITIONAL_JUMP`
<a id="insn-00afbc90"></a> `00afbc90` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afbc94"></a> `00afbc94` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbc98"></a> `00afbc98` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afbc9c"></a> `00afbc9c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbca0"></a> `00afbca0` | `15 00 00 14` | b 0x00afbcf4 | `UNCONDITIONAL_JUMP`
<a id="insn-00afbca4"></a> `00afbca4` | `28 00 00 aa` | orr x8,x1,x0 | `FALL_THROUGH`
<a id="insn-00afbca8"></a> `00afbca8` | `a8 fe ff b4` | cbz x8,0x00afbc7c | `CONDITIONAL_JUMP`
<a id="insn-00afbcac"></a> `00afbcac` | `f5 03 00 91` | mov x21,sp | `FALL_THROUGH`
<a id="insn-00afbcb0"></a> `00afbcb0` | `a0 22 00 91` | add x0,x21,#0x8 | `FALL_THROUGH`
<a id="insn-00afbcb4"></a> `00afbcb4` | `e1 03 1f 2a` | mov w1,wzr | `FALL_THROUGH`
<a id="insn-00afbcb8"></a> `00afbcb8` | `e2 03 1f 2a` | mov w2,wzr | `FALL_THROUGH`
<a id="insn-00afbcbc"></a> `00afbcbc` | `e0 03 00 f9` | str x0,[sp] | `FALL_THROUGH`
<a id="insn-00afbcc0"></a> `00afbcc0` | `e8 8b 03 94` | bl 0x00bdec60 | `UNCONDITIONAL_CALL`
<a id="insn-00afbcc4"></a> `00afbcc4` | `00 03 80 52` | mov w0,#0x18 | `FALL_THROUGH`
<a id="insn-00afbcc8"></a> `00afbcc8` | `ca 7c 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbccc"></a> `00afbccc` | `08 09 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afbcd0"></a> `00afbcd0` | `08 99 44 f9` | ldr x8,[x8, #0x930] | `FALL_THROUGH`
<a id="insn-00afbcd4"></a> `00afbcd4` | `15 08 00 f9` | str x21,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afbcd8"></a> `00afbcd8` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00afbcdc"></a> `00afbcdc` | `08 4c 00 a9` | stp x8,x19,[x0] | `FALL_THROUGH`
<a id="insn-00afbce0"></a> `00afbce0` | `c0 8b 03 94` | bl 0x00bdebe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbce4"></a> `00afbce4` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00afbce8"></a> `00afbce8` | `e6 8b 03 94` | bl 0x00bdec80 | `UNCONDITIONAL_CALL`
<a id="insn-00afbcec"></a> `00afbcec` | `e0 03 40 f9` | ldr x0,[sp] | `FALL_THROUGH`
<a id="insn-00afbcf0"></a> `00afbcf0` | `d8 8b 03 94` | bl 0x00bdec50 | `UNCONDITIONAL_CALL`
<a id="insn-00afbcf4"></a> `00afbcf4` | `88 16 40 f9` | ldr x8,[x20, #0x28] | `FALL_THROUGH`
<a id="insn-00afbcf8"></a> `00afbcf8` | `e9 0f 40 f9` | ldr x9,[sp, #0x18] | `FALL_THROUGH`
<a id="insn-00afbcfc"></a> `00afbcfc` | `1f 01 09 eb` | cmp x8,x9 | `FALL_THROUGH`
<a id="insn-00afbd00"></a> `00afbd00` | `c1 00 00 54` | b.ne 0x00afbd18 | `CONDITIONAL_JUMP`
<a id="insn-00afbd04"></a> `00afbd04` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afbd08"></a> `00afbd08` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afbd0c"></a> `00afbd0c` | `f5 13 40 f9` | ldr x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbd10"></a> `00afbd10` | `ff 43 01 91` | add sp,sp,#0x50 | `FALL_THROUGH`
<a id="insn-00afbd14"></a> `00afbd14` | `c0 03 5f d6` | ret | `TERMINATOR`
<a id="insn-00afbd18"></a> `00afbd18` | `ca 7c 03 94` | bl 0x00bdb040 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbc2c`](#insn-00afbc2c) 範囲 `[['00afbc2c', '00afbc5f']]`
  - `CONDITIONAL_JUMP` [`00afbc5c`](#insn-00afbc5c) → [`00afbcac`](#insn-00afbcac)
  - `FALL_THROUGH` [`00afbc5c`](#insn-00afbc5c) → [`00afbc60`](#insn-00afbc60)
- ブロック [`00afbc60`](#insn-00afbc60) 範囲 `[['00afbc60', '00afbc6f']]`
  - `CONDITIONAL_JUMP` [`00afbc6c`](#insn-00afbc6c) → [`00afbca4`](#insn-00afbca4)
  - `FALL_THROUGH` [`00afbc6c`](#insn-00afbc6c) → [`00afbc70`](#insn-00afbc70)
- ブロック [`00afbc70`](#insn-00afbc70) 範囲 `[['00afbc70', '00afbc73']]`
  - `CONDITIONAL_JUMP` [`00afbc70`](#insn-00afbc70) → [`00afbca4`](#insn-00afbca4)
  - `FALL_THROUGH` [`00afbc70`](#insn-00afbc70) → [`00afbc74`](#insn-00afbc74)
- ブロック [`00afbc74`](#insn-00afbc74) 範囲 `[['00afbc74', '00afbc7b']]`
  - `CONDITIONAL_JUMP` [`00afbc78`](#insn-00afbc78) → [`00afbcac`](#insn-00afbcac)
  - `FALL_THROUGH` [`00afbc78`](#insn-00afbc78) → [`00afbc7c`](#insn-00afbc7c)
- ブロック [`00afbc7c`](#insn-00afbc7c) 範囲 `[['00afbc7c', '00afbc8f']]`
  - `CONDITIONAL_JUMP` [`00afbc8c`](#insn-00afbc8c) → [`00afbcf4`](#insn-00afbcf4)
  - `FALL_THROUGH` [`00afbc8c`](#insn-00afbc8c) → [`00afbc90`](#insn-00afbc90)
- ブロック [`00afbc90`](#insn-00afbc90) 範囲 `[['00afbc90', '00afbc97']]`
  - `FALL_THROUGH` [`00afbc94`](#insn-00afbc94) → [`00afbc98`](#insn-00afbc98)
- ブロック [`00afbc98`](#insn-00afbc98) 範囲 `[['00afbc98', '00afbca3']]`
  - `UNCONDITIONAL_JUMP` [`00afbca0`](#insn-00afbca0) → [`00afbcf4`](#insn-00afbcf4)
- ブロック [`00afbca4`](#insn-00afbca4) 範囲 `[['00afbca4', '00afbcab']]`
  - `CONDITIONAL_JUMP` [`00afbca8`](#insn-00afbca8) → [`00afbc7c`](#insn-00afbc7c)
  - `FALL_THROUGH` [`00afbca8`](#insn-00afbca8) → [`00afbcac`](#insn-00afbcac)
- ブロック [`00afbcac`](#insn-00afbcac) 範囲 `[['00afbcac', '00afbcb3']]`
  - `FALL_THROUGH` [`00afbcb0`](#insn-00afbcb0) → [`00afbcb4`](#insn-00afbcb4)
- ブロック [`00afbcb4`](#insn-00afbcb4) 範囲 `[['00afbcb4', '00afbcf3']]`
  - `FALL_THROUGH` [`00afbcf0`](#insn-00afbcf0) → [`00afbcf4`](#insn-00afbcf4)
- ブロック [`00afbcf4`](#insn-00afbcf4) 範囲 `[['00afbcf4', '00afbd03']]`
  - `CONDITIONAL_JUMP` [`00afbd00`](#insn-00afbd00) → [`00afbd18`](#insn-00afbd18)
  - `FALL_THROUGH` [`00afbd00`](#insn-00afbd00) → [`00afbd04`](#insn-00afbd04)
- ブロック [`00afbd04`](#insn-00afbd04) 範囲 `[['00afbd04', '00afbd17']]`
- ブロック [`00afbd18`](#insn-00afbd18) 範囲 `[['00afbd18', '00afbd1b']]`

## 命令位置別の参照

- [`00afbc30`](#insn-00afbc30) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc34`](#insn-00afbc34) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc38`](#insn-00afbc38) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc4c`](#insn-00afbc4c) → `Stack[-0x38]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc54`](#insn-00afbc54) → `010a0cf8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00afbc5c`](#insn-00afbc5c) → [`00afbcac`](#insn-00afbcac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc60`](#insn-00afbc60) → [`00bdb780`](../00bdb/00bdb780.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb780` · 推定シンボル `None` · 推定型 `None`
- [`00afbc68`](#insn-00afbc68) → `010a0d00`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbc6c`](#insn-00afbc6c) → [`00afbca4`](#insn-00afbca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc70`](#insn-00afbc70) → [`00afbca4`](#insn-00afbca4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc74`](#insn-00afbc74) → [`00bdec40`](../00bde/00bdec40.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec40` · 推定シンボル `None` · 推定型 `None`
- [`00afbc78`](#insn-00afbc78) → [`00afbcac`](#insn-00afbcac) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbc8c`](#insn-00afbc8c) → [`00afbcf4`](#insn-00afbcf4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbca0`](#insn-00afbca0) → [`00afbcf4`](#insn-00afbcf4) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbca8`](#insn-00afbca8) → [`00afbc7c`](#insn-00afbc7c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbcbc`](#insn-00afbcbc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbcc0`](#insn-00afbcc0) → [`00bdec60`](../00bde/00bdec60.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec60` · 推定シンボル `None` · 推定型 `None`
- [`00afbcc8`](#insn-00afbcc8) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00afbcd0`](#insn-00afbcd0) → `00c1b930`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afbcdc`](#insn-00afbcdc) → `00c107f8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[40]`
- [`00afbce0`](#insn-00afbce0) → [`00bdebe0`](../00bde/00bdebe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdebe0` · 推定シンボル `None` · 推定型 `None`
- [`00afbce4`](#insn-00afbce4) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbce8`](#insn-00afbce8) → [`00bdec80`](../00bde/00bdec80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec80` · 推定シンボル `None` · 推定型 `None`
- [`00afbcec`](#insn-00afbcec) → `Stack[-0x50]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbcf0`](#insn-00afbcf0) → [`00bdec50`](../00bde/00bdec50.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec50` · 推定シンボル `None` · 推定型 `None`
- [`00afbcf8`](#insn-00afbcf8) → `Stack[-0x38]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd00`](#insn-00afbd00) → [`00afbd18`](#insn-00afbd18) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd04`](#insn-00afbd04) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd08`](#insn-00afbd08) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd0c`](#insn-00afbd0c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd18`](#insn-00afbd18) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbc30`](#insn-00afbc30)

~~~json
{
  "source": "00afbc30",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc34`](#insn-00afbc34)

~~~json
{
  "source": "00afbc34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc38`](#insn-00afbc38)

~~~json
{
  "source": "00afbc38",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc4c`](#insn-00afbc4c)

~~~json
{
  "source": "00afbc4c",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc54`](#insn-00afbc54)

~~~json
{
  "source": "00afbc54",
  "target": "010a0cf8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0cf8",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbc5c`](#insn-00afbc5c)

~~~json
{
  "source": "00afbc5c",
  "target": "00afbcac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc60`](#insn-00afbc60)

~~~json
{
  "source": "00afbc60",
  "target": "00bdb780",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbc68`](#insn-00afbc68)

~~~json
{
  "source": "00afbc68",
  "target": "010a0d00",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d00",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbc6c`](#insn-00afbc6c)

~~~json
{
  "source": "00afbc6c",
  "target": "00afbca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc70`](#insn-00afbc70)

~~~json
{
  "source": "00afbc70",
  "target": "00afbca4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc74`](#insn-00afbc74)

~~~json
{
  "source": "00afbc74",
  "target": "00bdec40",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbc78`](#insn-00afbc78)

~~~json
{
  "source": "00afbc78",
  "target": "00afbcac",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbc8c`](#insn-00afbc8c)

~~~json
{
  "source": "00afbc8c",
  "target": "00afbcf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbca0`](#insn-00afbca0)

~~~json
{
  "source": "00afbca0",
  "target": "00afbcf4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbca8`](#insn-00afbca8)

~~~json
{
  "source": "00afbca8",
  "target": "00afbc7c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbcbc`](#insn-00afbcbc)

~~~json
{
  "source": "00afbcbc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbcc0`](#insn-00afbcc0)

~~~json
{
  "source": "00afbcc0",
  "target": "00bdec60",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbcc8`](#insn-00afbcc8)

~~~json
{
  "source": "00afbcc8",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbcd0`](#insn-00afbcd0)

~~~json
{
  "source": "00afbcd0",
  "target": "00c1b930",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b930",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afbcdc`](#insn-00afbcdc)

~~~json
{
  "source": "00afbcdc",
  "target": "00c107f8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c107e8",
  "offset": 16,
  "size": 40,
  "datatype": "undefined1[40]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00afbce0`](#insn-00afbce0)

~~~json
{
  "source": "00afbce0",
  "target": "00bdebe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbce4`](#insn-00afbce4)

~~~json
{
  "source": "00afbce4",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbce8`](#insn-00afbce8)

~~~json
{
  "source": "00afbce8",
  "target": "00bdec80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbcec`](#insn-00afbcec)

~~~json
{
  "source": "00afbcec",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbcf0`](#insn-00afbcf0)

~~~json
{
  "source": "00afbcf0",
  "target": "00bdec50",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbcf8`](#insn-00afbcf8)

~~~json
{
  "source": "00afbcf8",
  "target": "Stack[-0x38]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd00`](#insn-00afbd00)

~~~json
{
  "source": "00afbd00",
  "target": "00afbd18",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd04`](#insn-00afbd04)

~~~json
{
  "source": "00afbd04",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd08`](#insn-00afbd08)

~~~json
{
  "source": "00afbd08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd0c`](#insn-00afbd0c)

~~~json
{
  "source": "00afbd0c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd18`](#insn-00afbd18)

~~~json
{
  "source": "00afbd18",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
