# 00afbabc

版: 15.7.3 / arm64-v8a / libnative-lib.so

SO SHA-256: `a0eb638e6ddc0deb0d02f3b20f187484216b7a3cf5e05b573518a3ba9de23f49`

解析リビジョン `45565ee9c155ae02` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.2**
  - 採用 · [関数詳細 `00afb9f4`](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/functions/00afb/00afb9f4.md) · 移動量 `+0xc8`
  - [v15.7.2 → v15.7.3 当該関数比較](../../../../../../comparisons/arm64-v8a/a3b91f0e1be9445c739dcadd/0-1/priority-0062.md#compare-f522d4619b420b1b60ad858483f8dea8)
  - [v15.7.2の関数一覧](../../../../../15.7.2/arm64-v8a/6122e24879d58db6b0beceb43e2a6ee62d008a586fc03b7cb7726214bc86f3ea/README.md)

- **次の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afbb00`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbb00.md) · 移動量 `+0x44`
  - [v15.7.3 → v15.7.4 当該関数比較](../../../../../../comparisons/arm64-v8a/af8902ef9a3f2de12eeaa7fe/0-1/high-0008.md#compare-75c53a6b58f36c3fea7f93d01df67c19)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00afbabc",
  "name": "_ZN8firebase8callback18CallbackDispatcher11AddCallbackEPNS0_8CallbackE",
  "size": 232,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "d3ab303b97dddb6a6409ba8b6c8323975b9113eb1eb1a54ac2b6c6bff82a6ce8",
  "source_text_sha256": "d3ab303b97dddb6a6409ba8b6c8323975b9113eb1eb1a54ac2b6c6bff82a6ce8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34410fe8fa9e7c9c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00afbabc",
        "00afbba3"
      ]
    ],
    "bytes_sha256": "5abea6dd2f2d4173ed5ad851fc1a25d8eead67dece081f80c74f98795bc89c48",
    "instruction_count": 58,
    "instruction_bytes": 232,
    "body_bytes": 232,
    "indirect": 1,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00bdec00](../00bde/00bdec00.md)

## 呼び出し先

- [00afc304](../00afc/00afc304.md)
- [00bdafe0](../00bda/00bdafe0.md)
- [00bdaff0](../00bda/00bdaff0.md)
- [00bddbd0](../00bdd/00bddbd0.md)
- [00bddbe0](../00bdd/00bddbe0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2111 bytes

~~~c

long * _ZN8firebase8callback18CallbackDispatcher11AddCallbackEPNS0_8CallbackE
                 (long *param_1,long param_2)

{
  char cVar1;
  bool bVar2;
  undefined *puVar3;
  long *plVar4;
  long *plVar5;
  long lVar6;
  long *plVar7;
  long *plVar8;
  
                    /* try { // try from 00afbad4 to 00bfbaef has its CatchHandler @ 00aff42c */
  plVar4 = (long *)_Znwm(0x30);
  plVar4[2] = 0;
  puVar3 = 
  PTR__ZTVNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEEE_00c1b938
  ;
  plVar8 = plVar4 + 1;
  *plVar8 = 0;
                    /* try { // try from 00afbb00 to 00bfbb07 has its CatchHandler @ 00aff428 */
  *plVar4 = (long)(puVar3 + 0x10);
  plVar7 = plVar4 + 3;
  *plVar7 = param_2;
  plVar4[4] = (long)(param_1 + 8);
  *(undefined1 *)(plVar4 + 5) = 0;
  _ZN8firebase5Mutex7AcquireEv(param_1 + 3);
  plVar5 = (long *)_Znwm(0x20);
  plVar5[2] = (long)plVar7;
  plVar5[3] = (long)plVar4;
  do {
                    /* try { // try from 00afbb30 to 00bfbb47 has its CatchHandler @ 00aff424 */
    cVar1 = '\x01';
    bVar2 = (bool)ExclusiveMonitorPass(plVar8,0x10);
    if (bVar2) {
      *plVar8 = *plVar8 + 1;
      cVar1 = ExclusiveMonitorsStatus();
    }
  } while (cVar1 != '\0');
  lVar6 = *param_1;
  *plVar5 = lVar6;
  plVar5[1] = (long)param_1;
  *(long **)(lVar6 + 8) = plVar5;
  *param_1 = (long)plVar5;
                    /* try { // try from 00afbb58 to 00bfbb6f has its CatchHandler @ 00b0037c */
  param_1[2] = param_1[2] + 1;
  _ZN8firebase5Mutex7ReleaseEv(param_1 + 3);
  do {
    lVar6 = *plVar8;
    cVar1 = '\x01';
    bVar2 = (bool)ExclusiveMonitorPass(plVar8,0x10);
    if (bVar2) {
      *plVar8 = lVar6 + -1;
      cVar1 = ExclusiveMonitorsStatus();
    }
  } while (cVar1 != '\0');
                    /* try { // try from 00afbb70 to 00bfbb77 has its CatchHandler @ 00aff420 */
  if (lVar6 == 0) {
    (**(code **)(*plVar4 + 0x10))(plVar4);
    _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar4);
  }
                    /* try { // try from 00afbba0 to 00bfbbbb has its CatchHandler @ 00aff41c */
  return plVar7;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00afbabc"></a> `00afbabc` | `f8 5f bc a9` | stp x24,x23,[sp, #-0x40]! | `FALL_THROUGH`
<a id="insn-00afbac0"></a> `00afbac0` | `f6 57 01 a9` | stp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbac4"></a> `00afbac4` | `f4 4f 02 a9` | stp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbac8"></a> `00afbac8` | `fd 7b 03 a9` | stp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afbacc"></a> `00afbacc` | `fd c3 00 91` | add x29,sp,#0x30 | `FALL_THROUGH`
<a id="insn-00afbad0"></a> `00afbad0` | `f5 03 00 aa` | mov x21,x0 | `FALL_THROUGH`
<a id="insn-00afbad4"></a> `00afbad4` | `18 00 01 91` | add x24,x0,#0x40 | `FALL_THROUGH`
<a id="insn-00afbad8"></a> `00afbad8` | `00 06 80 52` | mov w0,#0x30 | `FALL_THROUGH`
<a id="insn-00afbadc"></a> `00afbadc` | `f6 03 01 aa` | mov x22,x1 | `FALL_THROUGH`
<a id="insn-00afbae0"></a> `00afbae0` | `44 7d 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbae4"></a> `00afbae4` | `1f 08 00 f9` | str xzr,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afbae8"></a> `00afbae8` | `08 09 00 90` | adrp x8,0xc1b000 | `FALL_THROUGH`
<a id="insn-00afbaec"></a> `00afbaec` | `08 9d 44 f9` | ldr x8,[x8, #0x938] | `FALL_THROUGH`
<a id="insn-00afbaf0"></a> `00afbaf0` | `f7 03 00 aa` | mov x23,x0 | `FALL_THROUGH`
<a id="insn-00afbaf4"></a> `00afbaf4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00afbaf8"></a> `00afbaf8` | `ff 8e 00 f8` | str xzr,[x23, #0x8]! | `FALL_THROUGH`
<a id="insn-00afbafc"></a> `00afbafc` | `08 41 00 91` | add x8,x8,#0x10 | `FALL_THROUGH`
<a id="insn-00afbb00"></a> `00afbb00` | `08 00 00 f9` | str x8,[x0] | `FALL_THROUGH`
<a id="insn-00afbb04"></a> `00afbb04` | `96 8e 01 f8` | str x22,[x20, #0x18]! | `FALL_THROUGH`
<a id="insn-00afbb08"></a> `00afbb08` | `b6 62 00 91` | add x22,x21,#0x18 | `FALL_THROUGH`
<a id="insn-00afbb0c"></a> `00afbb0c` | `f3 03 00 aa` | mov x19,x0 | `FALL_THROUGH`
<a id="insn-00afbb10"></a> `00afbb10` | `18 10 00 f9` | str x24,[x0, #0x20] | `FALL_THROUGH`
<a id="insn-00afbb14"></a> `00afbb14` | `1f a0 00 39` | strb wzr,[x0, #0x28] | `FALL_THROUGH`
<a id="insn-00afbb18"></a> `00afbb18` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afbb1c"></a> `00afbb1c` | `2d 88 03 94` | bl 0x00bddbd0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbb20"></a> `00afbb20` | `00 04 80 52` | mov w0,#0x20 | `FALL_THROUGH`
<a id="insn-00afbb24"></a> `00afbb24` | `33 7d 03 94` | bl 0x00bdaff0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbb28"></a> `00afbb28` | `14 4c 01 a9` | stp x20,x19,[x0, #0x10] | `FALL_THROUGH`
<a id="insn-00afbb2c"></a> `00afbb2c` | `e8 7e 5f c8` | ldxr x8,[x23] | `FALL_THROUGH`
<a id="insn-00afbb30"></a> `00afbb30` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbb34"></a> `00afbb34` | `e8 7e 09 c8` | stxr w9,x8,[x23] | `FALL_THROUGH`
<a id="insn-00afbb38"></a> `00afbb38` | `a9 ff ff 35` | cbnz w9,0x00afbb2c | `CONDITIONAL_JUMP`
<a id="insn-00afbb3c"></a> `00afbb3c` | `a8 02 40 f9` | ldr x8,[x21] | `FALL_THROUGH`
<a id="insn-00afbb40"></a> `00afbb40` | `08 54 00 a9` | stp x8,x21,[x0] | `FALL_THROUGH`
<a id="insn-00afbb44"></a> `00afbb44` | `00 05 00 f9` | str x0,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00afbb48"></a> `00afbb48` | `a8 0a 40 f9` | ldr x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00afbb4c"></a> `00afbb4c` | `a0 02 00 f9` | str x0,[x21] | `FALL_THROUGH`
<a id="insn-00afbb50"></a> `00afbb50` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00afbb54"></a> `00afbb54` | `08 05 00 91` | add x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbb58"></a> `00afbb58` | `a8 0a 00 f9` | str x8,[x21, #0x10] | `FALL_THROUGH`
<a id="insn-00afbb5c"></a> `00afbb5c` | `21 88 03 94` | bl 0x00bddbe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbb60"></a> `00afbb60` | `e8 fe 5f c8` | ldaxr x8,[x23] | `FALL_THROUGH`
<a id="insn-00afbb64"></a> `00afbb64` | `09 05 00 d1` | sub x9,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00afbb68"></a> `00afbb68` | `e9 fe 0a c8` | stlxr w10,x9,[x23] | `FALL_THROUGH`
<a id="insn-00afbb6c"></a> `00afbb6c` | `aa ff ff 35` | cbnz w10,0x00afbb60 | `CONDITIONAL_JUMP`
<a id="insn-00afbb70"></a> `00afbb70` | `e8 00 00 b5` | cbnz x8,0x00afbb8c | `CONDITIONAL_JUMP`
<a id="insn-00afbb74"></a> `00afbb74` | `68 02 40 f9` | ldr x8,[x19] | `FALL_THROUGH`
<a id="insn-00afbb78"></a> `00afbb78` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbb7c"></a> `00afbb7c` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00afbb80"></a> `00afbb80` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00afbb84"></a> `00afbb84` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00afbb88"></a> `00afbb88` | `16 7d 03 94` | bl 0x00bdafe0 | `UNCONDITIONAL_CALL`
<a id="insn-00afbb8c"></a> `00afbb8c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00afbb90"></a> `00afbb90` | `fd 7b 43 a9` | ldp x29,x30,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00afbb94"></a> `00afbb94` | `f4 4f 42 a9` | ldp x20,x19,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00afbb98"></a> `00afbb98` | `f6 57 41 a9` | ldp x22,x21,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00afbb9c"></a> `00afbb9c` | `f8 5f c4 a8` | ldp x24,x23,[sp], #0x40 | `FALL_THROUGH`
<a id="insn-00afbba0"></a> `00afbba0` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00afbabc`](#insn-00afbabc) 範囲 `[['00afbabc', '00afbad3']]`
  - `FALL_THROUGH` [`00afbad0`](#insn-00afbad0) → [`00afbad4`](#insn-00afbad4)
- ブロック [`00afbad4`](#insn-00afbad4) 範囲 `[['00afbad4', '00afbaff']]`
  - `FALL_THROUGH` [`00afbafc`](#insn-00afbafc) → [`00afbb00`](#insn-00afbb00)
- ブロック [`00afbb00`](#insn-00afbb00) 範囲 `[['00afbb00', '00afbb2b']]`
  - `FALL_THROUGH` [`00afbb28`](#insn-00afbb28) → [`00afbb2c`](#insn-00afbb2c)
- ブロック [`00afbb2c`](#insn-00afbb2c) 範囲 `[['00afbb2c', '00afbb2f']]`
  - `FALL_THROUGH` [`00afbb2c`](#insn-00afbb2c) → [`00afbb30`](#insn-00afbb30)
- ブロック [`00afbb30`](#insn-00afbb30) 範囲 `[['00afbb30', '00afbb3b']]`
  - `CONDITIONAL_JUMP` [`00afbb38`](#insn-00afbb38) → [`00afbb2c`](#insn-00afbb2c)
  - `FALL_THROUGH` [`00afbb38`](#insn-00afbb38) → [`00afbb3c`](#insn-00afbb3c)
- ブロック [`00afbb3c`](#insn-00afbb3c) 範囲 `[['00afbb3c', '00afbb57']]`
  - `FALL_THROUGH` [`00afbb54`](#insn-00afbb54) → [`00afbb58`](#insn-00afbb58)
- ブロック [`00afbb58`](#insn-00afbb58) 範囲 `[['00afbb58', '00afbb5f']]`
  - `FALL_THROUGH` [`00afbb5c`](#insn-00afbb5c) → [`00afbb60`](#insn-00afbb60)
- ブロック [`00afbb60`](#insn-00afbb60) 範囲 `[['00afbb60', '00afbb6f']]`
  - `CONDITIONAL_JUMP` [`00afbb6c`](#insn-00afbb6c) → [`00afbb60`](#insn-00afbb60)
  - `FALL_THROUGH` [`00afbb6c`](#insn-00afbb6c) → [`00afbb70`](#insn-00afbb70)
- ブロック [`00afbb70`](#insn-00afbb70) 範囲 `[['00afbb70', '00afbb73']]`
  - `CONDITIONAL_JUMP` [`00afbb70`](#insn-00afbb70) → [`00afbb8c`](#insn-00afbb8c)
  - `FALL_THROUGH` [`00afbb70`](#insn-00afbb70) → [`00afbb74`](#insn-00afbb74)
- ブロック [`00afbb74`](#insn-00afbb74) 範囲 `[['00afbb74', '00afbb8b']]`
  - `FALL_THROUGH` [`00afbb88`](#insn-00afbb88) → [`00afbb8c`](#insn-00afbb8c)
- ブロック [`00afbb8c`](#insn-00afbb8c) 範囲 `[['00afbb8c', '00afbb9f']]`
  - `FALL_THROUGH` [`00afbb9c`](#insn-00afbb9c) → [`00afbba0`](#insn-00afbba0)
- ブロック [`00afbba0`](#insn-00afbba0) 範囲 `[['00afbba0', '00afbba3']]`

## 命令位置別の参照

- [`00afbabc`](#insn-00afbabc) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbac0`](#insn-00afbac0) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbac4`](#insn-00afbac4) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbac8`](#insn-00afbac8) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbae0`](#insn-00afbae0) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00afbaec`](#insn-00afbaec) → `00c1b938`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00afbb00`](#insn-00afbb00) → `00c107a8`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[56]`
- [`00afbb1c`](#insn-00afbb1c) → [`00bddbd0`](../00bdd/00bddbd0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbd0` · 推定シンボル `None` · 推定型 `None`
- [`00afbb24`](#insn-00afbb24) → [`00bdaff0`](../00bda/00bdaff0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdaff0` · 推定シンボル `None` · 推定型 `None`
- [`00afbb38`](#insn-00afbb38) → [`00afbb2c`](#insn-00afbb2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb5c`](#insn-00afbb5c) → [`00bddbe0`](../00bdd/00bddbe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bddbe0` · 推定シンボル `None` · 推定型 `None`
- [`00afbb6c`](#insn-00afbb6c) → [`00afbb60`](#insn-00afbb60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb70`](#insn-00afbb70) → [`00afbb8c`](#insn-00afbb8c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb7c`](#insn-00afbb7c) → `00c107b8`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `undefined1[56]`
- [`00afbb80`](#insn-00afbb80) → [`00afc304`](../00afc/00afc304.md) · `COMPUTED_CALL` · `ANALYSIS` · 関数 `00afc304` · 推定シンボル `_ZNSt6__ndk120__shared_ptr_emplaceIN8firebase8callback13CallbackEntryENS_9allocatorIS3_EEE16__on_zero_sharedEv` · 推定型 `None`
- [`00afbb88`](#insn-00afbb88) → [`00bdafe0`](../00bda/00bdafe0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00bdafe0` · 推定シンボル `None` · 推定型 `None`
- [`00afbb90`](#insn-00afbb90) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb94`](#insn-00afbb94) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00afbb98`](#insn-00afbb98) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00afbabc`](#insn-00afbabc)

~~~json
{
  "source": "00afbabc",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbac0`](#insn-00afbac0)

~~~json
{
  "source": "00afbac0",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbac4`](#insn-00afbac4)

~~~json
{
  "source": "00afbac4",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbac8`](#insn-00afbac8)

~~~json
{
  "source": "00afbac8",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbae0`](#insn-00afbae0)

~~~json
{
  "source": "00afbae0",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbaec`](#insn-00afbaec)

~~~json
{
  "source": "00afbaec",
  "target": "00c1b938",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c1b938",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00afbb00`](#insn-00afbb00)

~~~json
{
  "source": "00afbb00",
  "target": "00c107a8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10798",
  "offset": 16,
  "size": 56,
  "datatype": "undefined1[56]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00afbb1c`](#insn-00afbb1c)

~~~json
{
  "source": "00afbb1c",
  "target": "00bddbd0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbb24`](#insn-00afbb24)

~~~json
{
  "source": "00afbb24",
  "target": "00bdaff0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbb38`](#insn-00afbb38)

~~~json
{
  "source": "00afbb38",
  "target": "00afbb2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb5c`](#insn-00afbb5c)

~~~json
{
  "source": "00afbb5c",
  "target": "00bddbe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbb6c`](#insn-00afbb6c)

~~~json
{
  "source": "00afbb6c",
  "target": "00afbb60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb70`](#insn-00afbb70)

~~~json
{
  "source": "00afbb70",
  "target": "00afbb8c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb7c`](#insn-00afbb7c)

~~~json
{
  "source": "00afbb7c",
  "target": "00c107b8",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c10798",
  "offset": 32,
  "size": 56,
  "datatype": "undefined1[56]",
  "capture_state": "contains_relocation"
}
~~~
- 参照命令 [`00afbb80`](#insn-00afbb80)

~~~json
{
  "source": "00afbb80",
  "target": "00afc304",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbb88`](#insn-00afbb88)

~~~json
{
  "source": "00afbb88",
  "target": "00bdafe0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00afbb90`](#insn-00afbb90)

~~~json
{
  "source": "00afbb90",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb94`](#insn-00afbb94)

~~~json
{
  "source": "00afbb94",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00afbb98`](#insn-00afbb98)

~~~json
{
  "source": "00afbb98",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
