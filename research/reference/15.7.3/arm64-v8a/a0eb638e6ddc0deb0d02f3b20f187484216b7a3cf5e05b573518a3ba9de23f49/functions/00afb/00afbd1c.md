# 00afbd1c

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afbc54`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afbc54.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-428965d557de72a99251c688c84bbd14)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afbd60`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbd60.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/priority-0066.md#compare-7774e6d2ae3e003cfdd96334e83b1c45)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbd1c",
  "name": "_ZN8firebase8callback14RemoveCallbackEPv",
  "size": 300,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "5d7bc422c8e954cd7832d95a5e3ac20b449ef8a24440be41a4ee1023921744bc",
  "source_text_sha256": "5d7bc422c8e954cd7832d95a5e3ac20b449ef8a24440be41a4ee1023921744bc",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbd1c",
        "00afbe47"
      ]
    ],
    "bytes_sha256": "977269acb2c52ea0aab21c6ebdf0667887ff563cc58368a583a4c4bf78da8ef4",
    "instruction_count": 75,
    "instruction_bytes": 300,
    "body_bytes": 300,
    "indirect": 1,
    "unresolved": 1
  }
}
~~~

## 呼び出し元

解決済みの記録なし。

## 呼び出し先

- [00afb944](../00afb/00afb944.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)
- [00bdddd0](../00bdd/00bdddd0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 1920 bytes

~~~c

void _ZN8firebase8callback14RemoveCallbackEPv(undefined8 *param_1)

{
  undefined8 uVar1;
  long lVar2;
  undefined8 uVar3;
  long *plVar4;
  
  uVar3 = DAT_010a0ce0;
                    /* try { // try from 00afbd40 to 00bfbd57 has its CatchHandler @ 00aff40c */
  _ZN8firebase5Mutex7AcquireEv(DAT_010a0ce0);
  uVar1 = DAT_010a0ce0;
  if (0 < DAT_010a0ce8) {
    _ZN8firebase5Mutex7AcquireEv(DAT_010a0ce0);
    if (DAT_010a0ce8 == 0) {
      lVar2 = _Znwm(0x68);
      *(long *)lVar2 = lVar2;
      *(long *)(lVar2 + 8) = lVar2;
      *(undefined8 *)(lVar2 + 0x10) = 0;
      _ZN8firebase5MutexC2ENS0_4ModeE(lVar2 + 0x18,1);
                    /* try { // try from 00afbd90 to 00bfbda7 has its CatchHandler @ 00aff408 */
      _ZN8firebase5MutexC2ENS0_4ModeE(lVar2 + 0x40,1);
      DAT_010a0cf0 = lVar2;
    }
    DAT_010a0ce8 = DAT_010a0ce8 + 1;
                    /* try { // try from 00afbda8 to 00bfbdd7 has its CatchHandler @ 00af560c */
    _ZN8firebase5Mutex7ReleaseEv(uVar1);
    _ZN8firebase5Mutex7ReleaseEv(uVar3);
    lVar2 = DAT_010a0cf0 + 0x18;
    _ZN8firebase5Mutex7AcquireEv(lVar2);
    uVar3 = param_1[1];
    _ZN8firebase5Mutex7AcquireEv(uVar3);
                    /* try { // try from 00afbdd8 to 00bfbdef has its CatchHandler @ 00aff3f8 */
                    /* try { // try from 00afbdf0 to 00bfbe1f has its CatchHandler @ 00af560c */
    if ((*(char *)(param_1 + 2) == '\0') && (plVar4 = (long *)*param_1, plVar4 != (long *)0x0)) {
      *param_1 = 0;
      _ZN8firebase5Mutex7ReleaseEv(uVar3);
      (**(code **)(*plVar4 + 8))(plVar4);
    }
    else {
      _ZN8firebase5Mutex7ReleaseEv(uVar3);
    }
    _ZN8firebase5Mutex7ReleaseEv(lVar2);
    uVar3 = DAT_010a0ce0;
                    /* try { // try from 00afbe20 to 00bfbe37 has its CatchHandler @ 00b0037c */
    _ZN8firebase5Mutex7AcquireEv(DAT_010a0ce0);
    FUN_00afb944(1);
  }
  _ZN8firebase5Mutex7ReleaseEv(uVar3);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbd1c"></a> `00afbd1c` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00afbd20"></a> `00afbd20` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbd24"></a> `00afbd24` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbd28"></a> `00afbd28` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afbd2c"></a> `00afbd2c` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afbd30"></a> `00afbd30` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00afbd34"></a> `00afbd34` | `37 2d 00 b0` | adrp x23,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbd38"></a> `00afbd38` | `f4 72 46 f9` | ldr x20,[x23, #0xce0] | `FALL_THROUGH`
<a id="insn-00afbd3c"></a> `00afbd3c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afbd40"></a> `00afbd40` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afbd44"></a> `00afbd44` | `a3 87 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbd48"></a> `00afbd48` | `38 2d 00 b0` | adrp x24,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbd4c"></a> `00afbd4c` | `08 eb 4c b9` | ldr w8,[x24, #0xce8] | `FALL_THROUGH`
<a id="insn-00afbd50"></a> `00afbd50` | `1f 05 00 71` | cmp w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbd54"></a> `00afbd54` | `cb 06 00 54` | b.lt 0x00afbe2c | `CONDITIONAL_JUMP`
<a id="insn-00afbd58"></a> `00afbd58` | `f5 72 46 f9` | ldr x21,[x23, #0xce0] | `FALL_THROUGH`
<a id="insn-00afbd5c"></a> `00afbd5c` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afbd60"></a> `00afbd60` | `9c 87 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbd64"></a> `00afbd64` | `08 eb 4c b9` | ldr w8,[x24, #0xce8] | `FALL_THROUGH`
<a id="insn-00afbd68"></a> `00afbd68` | `39 2d 00 b0` | adrp x25,0x10a0000 | `FALL_THROUGH`
<a id="insn-00afbd6c"></a> `00afbd6c` | `c8 01 00 35` | cbnz w8,0x00afbda4 | `CONDITIONAL_JUMP`
<a id="insn-00afbd70"></a> `00afbd70` | `00 0d 80 52` | mov w0,#0x68 | `FALL_THROUGH`
<a id="insn-00afbd74"></a> `00afbd74` | `9f 7c 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbd78"></a> `00afbd78` | `f6 03 00 aa` | mov x22,x0 | `FALL_THROUGH`
<a id="insn-00afbd7c"></a> `00afbd7c` | `00 00 00 a9` | stp x0,x0,[x0] | `FALL_THROUGH`
<a id="insn-00afbd80"></a> `00afbd80` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afbd84"></a> `00afbd84` | `00 60 00 91` | add x0,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00afbd88"></a> `00afbd88` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00afbd8c"></a> `00afbd8c` | `11 88 03 94` | bl 0x00bdddd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbd90"></a> `00afbd90` | `c0 02 01 91` | add x0,x22,#0x40 | `FALL_THROUGH`
<a id="insn-00afbd94"></a> `00afbd94` | `21 00 80 52` | mov w1,#0x1 | `FALL_THROUGH`
<a id="insn-00afbd98"></a> `00afbd98` | `0e 88 03 94` | bl 0x00bdddd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbd9c"></a> `00afbd9c` | `08 eb 4c b9` | ldr w8,[x24, #0xce8] | `FALL_THROUGH`
<a id="insn-00afbda0"></a> `00afbda0` | `36 7b 06 f9` | str x22,[x25, #0xcf0] | `FALL_THROUGH`
<a id="insn-00afbda4"></a> `00afbda4` | `08 05 00 11` | add w8,w8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbda8"></a> `00afbda8` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afbdac"></a> `00afbdac` | `08 eb 0c b9` | str w8,[x24, #0xce8] | `FALL_THROUGH`
<a id="insn-00afbdb0"></a> `00afbdb0` | `8c 87 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbdb4"></a> `00afbdb4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afbdb8"></a> `00afbdb8` | `8a 87 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbdbc"></a> `00afbdbc` | `28 7b 46 f9` | ldr x8,[x25, #0xcf0] | `FALL_THROUGH`
<a id="insn-00afbdc0"></a> `00afbdc0` | `14 61 00 91` | add x20,x8,#0x18 | `FALL_THROUGH`
<a id="insn-00afbdc4"></a> `00afbdc4` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afbdc8"></a> `00afbdc8` | `82 87 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbdcc"></a> `00afbdcc` | `75 06 40 f9` | ldr x21,[x19, #0x8] | `FALL_THROUGH`
<a id="insn-00afbdd0"></a> `00afbdd0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afbdd4"></a> `00afbdd4` | `7f 87 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbdd8"></a> `00afbdd8` | `68 42 40 39` | ldrb w8,[x19, #0x10] | `FALL_THROUGH`
<a id="insn-00afbddc"></a> `00afbddc` | `88 00 00 34` | cbz w8,0x00afbdec | `CONDITIONAL_JUMP`
<a id="insn-00afbde0"></a> `00afbde0` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afbde4"></a> `00afbde4` | `7f 87 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbde8"></a> `00afbde8` | `0a 00 00 14` | b 0x00afbe10 | `UNCONDITIONAL_JUMP`
<a id="insn-00afbdec"></a> `00afbdec` | `76 02 40 f9` | ldr x22,[x19] | `FALL_THROUGH`
<a id="insn-00afbdf0"></a> `00afbdf0` | `96 ff ff b4` | cbz x22,0x00afbde0 | `CONDITIONAL_JUMP`
<a id="insn-00afbdf4"></a> `00afbdf4` | `e0 03 15 aa` | mov x0,x21 | `FALL_THROUGH`
<a id="insn-00afbdf8"></a> `00afbdf8` | `7f 02 00 f9` | str xzr,[x19] | `FALL_THROUGH`
<a id="insn-00afbdfc"></a> `00afbdfc` | `79 87 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbe00"></a> `00afbe00` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00afbe04"></a> `00afbe04` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afbe08"></a> `00afbe08` | `08 05 40 f9` | ldr x8,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afbe0c"></a> `00afbe0c` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbe10"></a> `00afbe10` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afbe14"></a> `00afbe14` | `73 87 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbe18"></a> `00afbe18` | `f4 72 46 f9` | ldr x20,[x23, #0xce0] | `FALL_THROUGH`
<a id="insn-00afbe1c"></a> `00afbe1c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afbe20"></a> `00afbe20` | `6c 87 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbe24"></a> `00afbe24` | `20 00 80 52` | mov w0,#0x1 | `FALL_THROUGH`
<a id="insn-00afbe28"></a> `00afbe28` | `c7 fe ff 97` | bl 0x00afb944 | `UNCONDITIONAL_CALL`
<a id="insn-00afbe2c"></a> `00afbe2c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afbe30"></a> `00afbe30` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00afbe34"></a> `00afbe34` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afbe38"></a> `00afbe38` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbe3c"></a> `00afbe3c` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbe40"></a> `00afbe40` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00afbe44"></a> `00afbe44` | `67 87 03 14` | b 0x00bddbe0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbd1c`](#insn-00afbd1c) 範囲 `[['00afbd1c', '00afbd3f']]`
  - `FALL_THROUGH` [`00afbd3c`](#insn-00afbd3c) → [`00afbd40`](#insn-00afbd40)
- ブロック [`00afbd40`](#insn-00afbd40) 範囲 `[['00afbd40', '00afbd57']]`
  - `CONDITIONAL_JUMP` [`00afbd54`](#insn-00afbd54) → [`00afbe2c`](#insn-00afbe2c)
  - `FALL_THROUGH` [`00afbd54`](#insn-00afbd54) → [`00afbd58`](#insn-00afbd58)
- ブロック [`00afbd58`](#insn-00afbd58) 範囲 `[['00afbd58', '00afbd6f']]`
  - `CONDITIONAL_JUMP` [`00afbd6c`](#insn-00afbd6c) → [`00afbda4`](#insn-00afbda4)
  - `FALL_THROUGH` [`00afbd6c`](#insn-00afbd6c) → [`00afbd70`](#insn-00afbd70)
- ブロック [`00afbd70`](#insn-00afbd70) 範囲 `[['00afbd70', '00afbd8f']]`
  - `FALL_THROUGH` [`00afbd8c`](#insn-00afbd8c) → [`00afbd90`](#insn-00afbd90)
- ブロック [`00afbd90`](#insn-00afbd90) 範囲 `[['00afbd90', '00afbda3']]`
  - `FALL_THROUGH` [`00afbda0`](#insn-00afbda0) → [`00afbda4`](#insn-00afbda4)
- ブロック [`00afbda4`](#insn-00afbda4) 範囲 `[['00afbda4', '00afbda7']]`
  - `FALL_THROUGH` [`00afbda4`](#insn-00afbda4) → [`00afbda8`](#insn-00afbda8)
- ブロック [`00afbda8`](#insn-00afbda8) 範囲 `[['00afbda8', '00afbdd7']]`
  - `FALL_THROUGH` [`00afbdd4`](#insn-00afbdd4) → [`00afbdd8`](#insn-00afbdd8)
- ブロック [`00afbdd8`](#insn-00afbdd8) 範囲 `[['00afbdd8', '00afbddf']]`
  - `CONDITIONAL_JUMP` [`00afbddc`](#insn-00afbddc) → [`00afbdec`](#insn-00afbdec)
  - `FALL_THROUGH` [`00afbddc`](#insn-00afbddc) → [`00afbde0`](#insn-00afbde0)
- ブロック [`00afbde0`](#insn-00afbde0) 範囲 `[['00afbde0', '00afbdeb']]`
  - `UNCONDITIONAL_JUMP` [`00afbde8`](#insn-00afbde8) → [`00afbe10`](#insn-00afbe10)
- ブロック [`00afbdec`](#insn-00afbdec) 範囲 `[['00afbdec', '00afbdef']]`
  - `FALL_THROUGH` [`00afbdec`](#insn-00afbdec) → [`00afbdf0`](#insn-00afbdf0)
- ブロック [`00afbdf0`](#insn-00afbdf0) 範囲 `[['00afbdf0', '00afbdf3']]`
  - `CONDITIONAL_JUMP` [`00afbdf0`](#insn-00afbdf0) → [`00afbde0`](#insn-00afbde0)
  - `FALL_THROUGH` [`00afbdf0`](#insn-00afbdf0) → [`00afbdf4`](#insn-00afbdf4)
- ブロック [`00afbdf4`](#insn-00afbdf4) 範囲 `[['00afbdf4', '00afbe0f']]`
  - `FALL_THROUGH` [`00afbe0c`](#insn-00afbe0c) → [`00afbe10`](#insn-00afbe10)
- ブロック [`00afbe10`](#insn-00afbe10) 範囲 `[['00afbe10', '00afbe1f']]`
  - `FALL_THROUGH` [`00afbe1c`](#insn-00afbe1c) → [`00afbe20`](#insn-00afbe20)
- ブロック [`00afbe20`](#insn-00afbe20) 範囲 `[['00afbe20', '00afbe2b']]`
  - `FALL_THROUGH` [`00afbe28`](#insn-00afbe28) → [`00afbe2c`](#insn-00afbe2c)
- ブロック [`00afbe2c`](#insn-00afbe2c) 範囲 `[['00afbe2c', '00afbe47']]`

## 命令位置別の参照

- [`00afbd1c`](#insn-00afbd1c) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd20`](#insn-00afbd20) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd24`](#insn-00afbd24) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd28`](#insn-00afbd28) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd2c`](#insn-00afbd2c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd38`](#insn-00afbd38) → `010a0ce0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbd44`](#insn-00afbd44) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00afbd4c`](#insn-00afbd4c) → `010a0ce8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00afbd54`](#insn-00afbd54) → [`00afbe2c`](#insn-00afbe2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd58`](#insn-00afbd58) → `010a0ce0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbd60`](#insn-00afbd60) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00afbd64`](#insn-00afbd64) → `010a0ce8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00afbd6c`](#insn-00afbd6c) → [`00afbda4`](#insn-00afbda4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbd74`](#insn-00afbd74) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00afbd8c`](#insn-00afbd8c) → [`00bdddd0`](../00bdd/00bdddd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdddd0` · 推定シンボル `None` · 推定型 `None`
- [`00afbd98`](#insn-00afbd98) → [`00bdddd0`](../00bdd/00bdddd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdddd0` · 推定シンボル `None` · 推定型 `None`
- [`00afbd9c`](#insn-00afbd9c) → `010a0ce8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00afbda0`](#insn-00afbda0) → `010a0cf0`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbdac`](#insn-00afbdac) → `010a0ce8`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined4`
- [`00afbdb0`](#insn-00afbdb0) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afbdb8`](#insn-00afbdb8) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afbdbc`](#insn-00afbdbc) → `010a0cf0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbdc8`](#insn-00afbdc8) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00afbdd4`](#insn-00afbdd4) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00afbddc`](#insn-00afbddc) → [`00afbdec`](#insn-00afbdec) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbde4`](#insn-00afbde4) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afbde8`](#insn-00afbde8) → [`00afbe10`](#insn-00afbe10) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbdf0`](#insn-00afbdf0) → [`00afbde0`](#insn-00afbde0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbdfc`](#insn-00afbdfc) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afbe14`](#insn-00afbe14) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afbe18`](#insn-00afbe18) → `010a0ce0`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined8`
- [`00afbe20`](#insn-00afbe20) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00afbe28`](#insn-00afbe28) → [`00afb944`](00afb944.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00afb944` · 推定シンボル `None` · 推定型 `None`
- [`00afbe30`](#insn-00afbe30) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe34`](#insn-00afbe34) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe38`](#insn-00afbe38) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe3c`](#insn-00afbe3c) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbe44`](#insn-00afbe44) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbd1c`](#insn-00afbd1c)

~~~json
{
  "source": "00afbd1c",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd20`](#insn-00afbd20)

~~~json
{
  "source": "00afbd20",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd24`](#insn-00afbd24)

~~~json
{
  "source": "00afbd24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd28`](#insn-00afbd28)

~~~json
{
  "source": "00afbd28",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd2c`](#insn-00afbd2c)

~~~json
{
  "source": "00afbd2c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd38`](#insn-00afbd38)

~~~json
{
  "source": "00afbd38",
  "target": "010a0ce0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0ce0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbd44`](#insn-00afbd44)

~~~json
{
  "source": "00afbd44",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbd4c`](#insn-00afbd4c)

~~~json
{
  "source": "00afbd4c",
  "target": "010a0ce8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0ce8",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbd54`](#insn-00afbd54)

~~~json
{
  "source": "00afbd54",
  "target": "00afbe2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd58`](#insn-00afbd58)

~~~json
{
  "source": "00afbd58",
  "target": "010a0ce0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0ce0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbd60`](#insn-00afbd60)

~~~json
{
  "source": "00afbd60",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbd64`](#insn-00afbd64)

~~~json
{
  "source": "00afbd64",
  "target": "010a0ce8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0ce8",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbd6c`](#insn-00afbd6c)

~~~json
{
  "source": "00afbd6c",
  "target": "00afbda4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbd74`](#insn-00afbd74)

~~~json
{
  "source": "00afbd74",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbd8c`](#insn-00afbd8c)

~~~json
{
  "source": "00afbd8c",
  "target": "00bdddd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbd98`](#insn-00afbd98)

~~~json
{
  "source": "00afbd98",
  "target": "00bdddd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbd9c`](#insn-00afbd9c)

~~~json
{
  "source": "00afbd9c",
  "target": "010a0ce8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0ce8",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbda0`](#insn-00afbda0)

~~~json
{
  "source": "00afbda0",
  "target": "010a0cf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0cf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbdac`](#insn-00afbdac)

~~~json
{
  "source": "00afbdac",
  "target": "010a0ce8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0ce8",
  "offset": 0,
  "size": 4,
  "datatype": "undefined4",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbdb0`](#insn-00afbdb0)

~~~json
{
  "source": "00afbdb0",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbdb8`](#insn-00afbdb8)

~~~json
{
  "source": "00afbdb8",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbdbc`](#insn-00afbdbc)

~~~json
{
  "source": "00afbdbc",
  "target": "010a0cf0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0cf0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbdc8`](#insn-00afbdc8)

~~~json
{
  "source": "00afbdc8",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbdd4`](#insn-00afbdd4)

~~~json
{
  "source": "00afbdd4",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbddc`](#insn-00afbddc)

~~~json
{
  "source": "00afbddc",
  "target": "00afbdec",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbde4`](#insn-00afbde4)

~~~json
{
  "source": "00afbde4",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbde8`](#insn-00afbde8)

~~~json
{
  "source": "00afbde8",
  "target": "00afbe10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbdf0`](#insn-00afbdf0)

~~~json
{
  "source": "00afbdf0",
  "target": "00afbde0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbdfc`](#insn-00afbdfc)

~~~json
{
  "source": "00afbdfc",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbe14`](#insn-00afbe14)

~~~json
{
  "source": "00afbe14",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbe18`](#insn-00afbe18)

~~~json
{
  "source": "00afbe18",
  "target": "010a0ce0",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "010a0ce0",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00afbe20`](#insn-00afbe20)

~~~json
{
  "source": "00afbe20",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbe28`](#insn-00afbe28)

~~~json
{
  "source": "00afbe28",
  "target": "00afb944",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbe30`](#insn-00afbe30)

~~~json
{
  "source": "00afbe30",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe34`](#insn-00afbe34)

~~~json
{
  "source": "00afbe34",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe38`](#insn-00afbe38)

~~~json
{
  "source": "00afbe38",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe3c`](#insn-00afbe3c)

~~~json
{
  "source": "00afbe3c",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbe44`](#insn-00afbe44)

~~~json
{
  "source": "00afbe44",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
