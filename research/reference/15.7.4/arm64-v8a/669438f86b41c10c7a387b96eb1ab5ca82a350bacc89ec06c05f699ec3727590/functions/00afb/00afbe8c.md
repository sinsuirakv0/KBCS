# 00afbe8c

版: 15.7.4 / arm64-v8a / libnative-lib.so

SO SHA-256: `669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590`

解析リビジョン `6cf79e30b2bdfc73` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.3**
  - 採用 · [関数詳細 `00afbe48`](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/functions/00afb/00afbe48.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0066.md#compare-c192aba99d7edffa229430c43dea87b5)
  - [v15.7.3の関数一覧](../../../../../15.7.3/arm64-v8a/a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49/README.md)

- **次の公開版 v16.0.0**
  - 採用 · [関数詳細 `00b5bc10`](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/functions/00b5b/00b5bc10.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/priority-0060.md#compare-b1c8b7f0da1a184f84567c76cf585de7)
  - [v16.0.0の関数一覧](../../../../../16.0.0/arm64-v8a/1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbe8c",
  "name": "_ZN8firebase8callback13PollCallbacksEv",
  "size": 236,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "126834f70ad2beb0e719f92696bed8f1156f2c52f96a1d0d100e08608d071623",
  "source_text_sha256": "126834f70ad2beb0e719f92696bed8f1156f2c52f96a1d0d100e08608d071623",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3441138fe5d8eadc",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbe8c",
        "00afbf77"
      ]
    ],
    "bytes_sha256": "57af36ef15e56201a156a2c5da3974d10cfa85422dc51aa8eb62620f6e8745ef",
    "instruction_count": 59,
    "instruction_bytes": 236,
    "body_bytes": 236,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00afb988](../00afb/00afb988.md)
- [00bdb040](../00bdb/00bdb040.md)
- [00bdb7d0](../00bdb/00bdb7d0.md)
- [00bddc20](../00bdd/00bddc20.md)
- [00bddc30](../00bdd/00bddc30.md)
- [00bdde20](../00bdd/00bdde20.md)
- [00bdec70](../00bde/00bdec70.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1350 bytes

~~~c

void _ZN8firebase8callback13PollCallbacksEv(void)

{
  undefined8 uVar1;
  undefined8 uVar2;
  int iVar3;
  long lVar4;
  
  uVar1 = DAT_010a0d20;
  _ZN8firebase5Mutex7AcquireEv(DAT_010a0d20);
  uVar2 = DAT_010a0d20;
  if (0 < DAT_010a0d28) {
    _ZN8firebase5Mutex7AcquireEv(DAT_010a0d20);
                    /* try { // try from 00afbecc to 00bfbed7 has its CatchHandler @ 00b00490 */
    if (DAT_010a0d28 == 0) {
                    /* try { // try from 00afbedc to 00bfbee7 has its CatchHandler @ 00b00488 */
      lVar4 = _Znwm(0x68);
      *(long *)lVar4 = lVar4;
      *(long *)(lVar4 + 8) = lVar4;
                    /* try { // try from 00afbee8 to 00bfbef7 has its CatchHandler @ 00b00484 */
      *(undefined8 *)(lVar4 + 0x10) = 0;
      _ZN8firebase5MutexC2ENS0_4ModeE(lVar4 + 0x18,1);
                    /* try { // try from 00afbef8 to 00bfbf0b has its CatchHandler @ 00b0048c */
      _ZN8firebase5MutexC2ENS0_4ModeE(lVar4 + 0x40,1);
      DAT_010a0d30 = lVar4;
    }
    DAT_010a0d28 = DAT_010a0d28 + 1;
    _ZN8firebase5Mutex7ReleaseEv(uVar2);
    _ZN8firebase5Mutex7ReleaseEv(uVar1);
    DAT_010a0d40 = pthread_self();
    DAT_010a0d38 = 1;
    iVar3 = _ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv(DAT_010a0d30);
    FUN_00afb988(iVar3 + 1);
    return;
  }
  _ZN8firebase5Mutex7ReleaseEv(uVar1);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbe8c"></a> `00afbe8c` | `f7 0f 1c f8` | str x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00afbe90"></a> `00afbe90` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbe94"></a> `00afbe94` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbe98"></a> `00afbe98` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afbe9c"></a> `00afbe9c` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00afbea0"></a> `00afbea0` | `34 2d 00 b0` | adrp x20,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbea4"></a> `00afbea4` | `93 92 46 f9` | ldr x19,[x20, #0xd20] | `FALL_THROUGH`
<a id="insn-00afbea8"></a> `00afbea8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbeac"></a> `00afbeac` | `5d 87 03 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00afbeb0"></a> `00afbeb0` | `37 2d 00 b0` | adrp x23,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbeb4"></a> `00afbeb4` | `e8 2a 4d b9` | ldr w8,[x23, #0xd28] | `FALL_THROUGH`
<a id="insn-00afbeb8"></a> `00afbeb8` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbebc"></a> `00afbebc` | `2b 05 00 54` | b.lt 0x00afbf60 | `CONDITIONAL_JUMP`
<a id="insn-00afbec0"></a> `00afbec0` | `94 92 46 f9` | ldr x20,[x20, #0xd20] | `FALL_THROUGH`
<a id="insn-00afbec4"></a> `00afbec4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afbec8"></a> `00afbec8` | `56 87 03 94` | bl 0x00bddc20 | `UNCONDITIONAL_CALL`
<a id="insn-00afbecc"></a> `00afbecc` | `e8 2a 4d b9` | ldr w8,[x23, #0xd28] | `FALL_THROUGH`
<a id="insn-00afbed0"></a> `00afbed0` | `36 2d 00 b0` | adrp x22,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbed4"></a> `00afbed4` | `c8 01 00 35` | cbnz w8,0x00afbf0c | `CONDITIONAL_JUMP`
<a id="insn-00afbed8"></a> `00afbed8` | `00 0d 80 52` | mov w0,#0x68 | `FALL_THROUGH`
<a id="insn-00afbedc"></a> `00afbedc` | `59 7c 03 94` | bl 0x00bdb040 | `UNCONDITIONAL_CALL`
<a id="insn-00afbee0"></a> `00afbee0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00afbee4"></a> `00afbee4` | `00 00 00 a9` | stp x0,x0,[x0] | `FALL_THROUGH`
<a id="insn-00afbee8"></a> `00afbee8` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afbeec"></a> `00afbeec` | `00 60 00 91` | add x0,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00afbef0"></a> `00afbef0` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00afbef4"></a> `00afbef4` | `cb 87 03 94` | bl 0x00bdde20 | `UNCONDITIONAL_CALL`
<a id="insn-00afbef8"></a> `00afbef8` | `a0 02 01 91` | add x0,x21,#0x40 | `FALL_THROUGH`
<a id="insn-00afbefc"></a> `00afbefc` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00afbf00"></a> `00afbf00` | `c8 87 03 94` | bl 0x00bdde20 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf04"></a> `00afbf04` | `e8 2a 4d b9` | ldr w8,[x23, #0xd28] | `FALL_THROUGH`
<a id="insn-00afbf08"></a> `00afbf08` | `d5 9a 06 f9` | str x21,[x22, #0xd30] | `FALL_THROUGH`
<a id="insn-00afbf0c"></a> `00afbf0c` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbf10"></a> `00afbf10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afbf14"></a> `00afbf14` | `e8 2a 0d b9` | str w8,[x23, #0xd28] | `FALL_THROUGH`
<a id="insn-00afbf18"></a> `00afbf18` | `46 87 03 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf1c"></a> `00afbf1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbf20"></a> `00afbf20` | `44 87 03 94` | bl 0x00bddc30 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf24"></a> `00afbf24` | `2b 7e 03 94` | bl 0x00bdb7d0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf28"></a> `00afbf28` | `c8 9a 46 f9` | ldr x8,[x22, #0xd30] | `FALL_THROUGH`
<a id="insn-00afbf2c"></a> `00afbf2c` | `29 2d 00 b0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbf30"></a> `00afbf30` | `20 a1 06 f9` | str x0,[x9, #0xd40] | `FALL_THROUGH`
<a id="insn-00afbf34"></a> `00afbf34` | `29 2d 00 b0` | adrp x9,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbf38"></a> `00afbf38` | `2a 00 80 52` | mov w10,#0x1 | `FALL_THROUGH`
<a id="insn-00afbf3c"></a> `00afbf3c` | `e0 03 08 aa` | mov x0,x8 | `FALL_THROUGH`
<a id="insn-00afbf40"></a> `00afbf40` | `2a e1 34 39` | strb w10,[x9, #0xd38] | `FALL_THROUGH`
<a id="insn-00afbf44"></a> `00afbf44` | `4b 8b 03 94` | bl 0x00bdec70 | `UNCONDITIONAL_CALL`
<a id="insn-00afbf48"></a> `00afbf48` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afbf4c"></a> `00afbf4c` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbf50"></a> `00afbf50` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbf54"></a> `00afbf54` | `00 04 00 11` | add w0,w0,#0x1 | `FALL_THROUGH`
<a id="insn-00afbf58"></a> `00afbf58` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afbf5c"></a> `00afbf5c` | `8b fe ff 17` | b 0x00afb988 | `CALL_TERMINATOR`
<a id="insn-00afbf60"></a> `00afbf60` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbf64"></a> `00afbf64` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afbf68"></a> `00afbf68` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbf6c"></a> `00afbf6c` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbf70"></a> `00afbf70` | `f7 07 44 f8` | ldr x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afbf74"></a> `00afbf74` | `2f 87 03 14` | b 0x00bddc30 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbe8c`](#insn-00afbe8c) 範囲 `[['00afbe8c', '00afbebf']]`
  - `CONDITIONAL_JUMP` [`00afbebc`](#insn-00afbebc) → [`00afbf60`](#insn-00afbf60)
  - `FALL_THROUGH` [`00afbebc`](#insn-00afbebc) → [`00afbec0`](#insn-00afbec0)
- ブロック [`00afbec0`](#insn-00afbec0) 範囲 `[['00afbec0', '00afbecb']]`
  - `FALL_THROUGH` [`00afbec8`](#insn-00afbec8) → [`00afbecc`](#insn-00afbecc)
- ブロック [`00afbecc`](#insn-00afbecc) 範囲 `[['00afbecc', '00afbed7']]`
  - `CONDITIONAL_JUMP` [`00afbed4`](#insn-00afbed4) → [`00afbf0c`](#insn-00afbf0c)
  - `FALL_THROUGH` [`00afbed4`](#insn-00afbed4) → [`00afbed8`](#insn-00afbed8)
- ブロック [`00afbed8`](#insn-00afbed8) 範囲 `[['00afbed8', '00afbedb']]`
  - `FALL_THROUGH` [`00afbed8`](#insn-00afbed8) → [`00afbedc`](#insn-00afbedc)
- ブロック [`00afbedc`](#insn-00afbedc) 範囲 `[['00afbedc', '00afbee7']]`
  - `FALL_THROUGH` [`00afbee4`](#insn-00afbee4) → [`00afbee8`](#insn-00afbee8)
- ブロック [`00afbee8`](#insn-00afbee8) 範囲 `[['00afbee8', '00afbef7']]`
  - `FALL_THROUGH` [`00afbef4`](#insn-00afbef4) → [`00afbef8`](#insn-00afbef8)
- ブロック [`00afbef8`](#insn-00afbef8) 範囲 `[['00afbef8', '00afbf0b']]`
  - `FALL_THROUGH` [`00afbf08`](#insn-00afbf08) → [`00afbf0c`](#insn-00afbf0c)
- ブロック [`00afbf0c`](#insn-00afbf0c) 範囲 `[['00afbf0c', '00afbf5f']]`
- ブロック [`00afbf60`](#insn-00afbf60) 範囲 `[['00afbf60', '00afbf77']]`

## 命令位置別の参照

- [`00afbe8c`](#insn-00afbe8c) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe90`](#insn-00afbe90) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe94`](#insn-00afbe94) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe98`](#insn-00afbe98) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbea4`](#insn-00afbea4) → `010a0d20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbeac`](#insn-00afbeac) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00afbeb4`](#insn-00afbeb4) → `010a0d28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00afbebc`](#insn-00afbebc) → [`00afbf60`](#insn-00afbf60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbec0`](#insn-00afbec0) → `010a0d20`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbec8`](#insn-00afbec8) → [`00bddc20`](../00bdd/00bddc20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc20` · 推定シンボル `None` · 推定型 `None`
- [`00afbecc`](#insn-00afbecc) → `010a0d28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00afbed4`](#insn-00afbed4) → [`00afbf0c`](#insn-00afbf0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbedc`](#insn-00afbedc) → [`00bdb040`](../00bdb/00bdb040.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb040` · 推定シンボル `None` · 推定型 `None`
- [`00afbef4`](#insn-00afbef4) → [`00bdde20`](../00bdd/00bdde20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdde20` · 推定シンボル `None` · 推定型 `None`
- [`00afbf00`](#insn-00afbf00) → [`00bdde20`](../00bdd/00bdde20.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdde20` · 推定シンボル `None` · 推定型 `None`
- [`00afbf04`](#insn-00afbf04) → `010a0d28`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00afbf08`](#insn-00afbf08) → `010a0d30`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbf14`](#insn-00afbf14) → `010a0d28`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00afbf18`](#insn-00afbf18) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00afbf20`](#insn-00afbf20) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`
- [`00afbf24`](#insn-00afbf24) → [`00bdb7d0`](../00bdb/00bdb7d0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdb7d0` · 推定シンボル `None` · 推定型 `None`
- [`00afbf28`](#insn-00afbf28) → `010a0d30`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbf30`](#insn-00afbf30) → `010a0d40`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbf40`](#insn-00afbf40) → `010a0d38`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1`
- [`00afbf44`](#insn-00afbf44) → [`00bdec70`](../00bde/00bdec70.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdec70` · 推定シンボル `None` · 推定型 `None`
- [`00afbf48`](#insn-00afbf48) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf4c`](#insn-00afbf4c) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf50`](#insn-00afbf50) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf5c`](#insn-00afbf5c) → [`00afb988`](00afb988.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afb988` · 推定シンボル `None` · 推定型 `None`
- [`00afbf64`](#insn-00afbf64) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf68`](#insn-00afbf68) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf6c`](#insn-00afbf6c) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbf74`](#insn-00afbf74) → [`00bddc30`](../00bdd/00bddc30.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddc30` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbe8c`](#insn-00afbe8c)

~~~json
{
  "source": "00afbe8c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe90`](#insn-00afbe90)

~~~json
{
  "source": "00afbe90",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe94`](#insn-00afbe94)

~~~json
{
  "source": "00afbe94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe98`](#insn-00afbe98)

~~~json
{
  "source": "00afbe98",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbea4`](#insn-00afbea4)

~~~json
{
  "source": "00afbea4",
  "target": "010a0d20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbeac`](#insn-00afbeac)

~~~json
{
  "source": "00afbeac",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbeb4`](#insn-00afbeb4)

~~~json
{
  "source": "00afbeb4",
  "target": "010a0d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d28",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbebc`](#insn-00afbebc)

~~~json
{
  "source": "00afbebc",
  "target": "00afbf60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbec0`](#insn-00afbec0)

~~~json
{
  "source": "00afbec0",
  "target": "010a0d20",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d20",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbec8`](#insn-00afbec8)

~~~json
{
  "source": "00afbec8",
  "target": "00bddc20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbecc`](#insn-00afbecc)

~~~json
{
  "source": "00afbecc",
  "target": "010a0d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d28",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbed4`](#insn-00afbed4)

~~~json
{
  "source": "00afbed4",
  "target": "00afbf0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbedc`](#insn-00afbedc)

~~~json
{
  "source": "00afbedc",
  "target": "00bdb040",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbef4`](#insn-00afbef4)

~~~json
{
  "source": "00afbef4",
  "target": "00bdde20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf00`](#insn-00afbf00)

~~~json
{
  "source": "00afbf00",
  "target": "00bdde20",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf04`](#insn-00afbf04)

~~~json
{
  "source": "00afbf04",
  "target": "010a0d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d28",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbf08`](#insn-00afbf08)

~~~json
{
  "source": "00afbf08",
  "target": "010a0d30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbf14`](#insn-00afbf14)

~~~json
{
  "source": "00afbf14",
  "target": "010a0d28",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d28",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbf18`](#insn-00afbf18)

~~~json
{
  "source": "00afbf18",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf20`](#insn-00afbf20)

~~~json
{
  "source": "00afbf20",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf24`](#insn-00afbf24)

~~~json
{
  "source": "00afbf24",
  "target": "00bdb7d0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf28`](#insn-00afbf28)

~~~json
{
  "source": "00afbf28",
  "target": "010a0d30",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d30",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbf30`](#insn-00afbf30)

~~~json
{
  "source": "00afbf30",
  "target": "010a0d40",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d40",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbf40`](#insn-00afbf40)

~~~json
{
  "source": "00afbf40",
  "target": "010a0d38",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0d38",
  "offset": 0,
  "size": 1,
  "datatype": "undefined1",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbf44`](#insn-00afbf44)

~~~json
{
  "source": "00afbf44",
  "target": "00bdec70",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf48`](#insn-00afbf48)

~~~json
{
  "source": "00afbf48",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf4c`](#insn-00afbf4c)

~~~json
{
  "source": "00afbf4c",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf50`](#insn-00afbf50)

~~~json
{
  "source": "00afbf50",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf5c`](#insn-00afbf5c)

~~~json
{
  "source": "00afbf5c",
  "target": "00afb988",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbf64`](#insn-00afbf64)

~~~json
{
  "source": "00afbf64",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf68`](#insn-00afbf68)

~~~json
{
  "source": "00afbf68",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf6c`](#insn-00afbf6c)

~~~json
{
  "source": "00afbf6c",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbf74`](#insn-00afbf74)

~~~json
{
  "source": "00afbf74",
  "target": "00bddc30",
  "target_space": "ram",
  "resolution": "function"
}
~~~
