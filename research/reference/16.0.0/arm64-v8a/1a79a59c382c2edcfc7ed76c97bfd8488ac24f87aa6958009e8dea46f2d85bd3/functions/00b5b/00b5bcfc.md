# 00b5bcfc

版: 16.0.0 / arm64-v8a / libnative-lib.so

SO SHA-256: `1a79a59c382c2edcfc7ed76c97bfd8488ac24f87aa6958009e8dea46f2d85bd3`

解析リビジョン `70b5c9c0dcc036b2` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v15.7.4**
  - 採用 · [関数詳細 `00afbf78`](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/functions/00afb/00afbf78.md) · 移動量 `+0x5fd84`
  - [v15.7.4 → v16.0.0 当該関数比較](../../../../../../comparisons/arm64-v8a/9801c0f5b635b1292885b4ed/0-1/alignment_unresolved-0015.md#compare-a5b48a71a9892e8df122a6413b7d8a14)
  - [v15.7.4の関数一覧](../../../../../15.7.4/arm64-v8a/669438f86b41c10c7a387b96eb1ab5ca82a350bacc89ec06c05f699ec3727590/README.md)

- **次の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b5c124`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5c124.md) · 移動量 `+0x428`
  - [v16.0.0 → v16.0.1 当該関数比較](../../../../../../comparisons/arm64-v8a/6bf8de28d08f0f4f0e3c832d/0-1/inspection-0037.md#compare-3b757612c7854e67f8a80844582b52bb)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5bcfc",
  "name": "_ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv",
  "size": 312,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "616db4f575b13c5b7d6812933dcc2e0b3234d6cb09ddd7e5b3abac0b880933be",
  "source_text_sha256": "616db4f575b13c5b7d6812933dcc2e0b3234d6cb09ddd7e5b3abac0b880933be",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "34411a6fd886ea7c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5bcfc",
        "00b5be33"
      ]
    ],
    "bytes_sha256": "0c0b1908a5fc9660d926f0bdee35f39594cbff958c462377ff0e5952c66c7acc",
    "instruction_count": 78,
    "instruction_bytes": 312,
    "body_bytes": 312,
    "indirect": 2,
    "unresolved": 2
  }
}
~~~

## 呼び出し元

- [00c5b730](../00c5b/00c5b730.md)

## 呼び出し先

- [00c57a80](../00c57/00c57a80.md)
- [00c57ab0](../00c57/00c57ab0.md)
- [00c5a600](../00c5a/00c5a600.md)
- [00c5a610](../00c5a/00c5a610.md)
- [00c5b700](../00c5b/00c5b700.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 2456 bytes

~~~c

int _ZN8firebase8callback18CallbackDispatcher17DispatchCallbacksEv(long param_1)

{
  long lVar1;
  long *plVar2;
  long lVar3;
  long lVar4;
  long *plVar5;
  char cVar6;
  bool bVar7;
  long lVar8;
  int iVar9;
  long *plVar10;
  long *plVar11;
  
  lVar1 = param_1 + 0x18;
  _ZN8firebase5Mutex7AcquireEv(lVar1);
  lVar8 = *(long *)(param_1 + 0x10);
  if (lVar8 == 0) {
    iVar9 = 0;
  }
  else {
    iVar9 = 0;
    do {
      plVar10 = *(long **)(param_1 + 8);
      lVar3 = plVar10[2];
      plVar5 = (long *)plVar10[3];
      if (plVar5 != (long *)0x0) {
        plVar10 = plVar5 + 1;
        do {
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar10,0x10);
          if (bVar7) {
            *plVar10 = *plVar10 + 1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        plVar10 = *(long **)(param_1 + 8);
        lVar8 = *(long *)(param_1 + 0x10);
      }
      lVar4 = *plVar10;
      *(long *)(lVar4 + 8) = plVar10[1];
      *(long *)plVar10[1] = lVar4;
      *(long *)(param_1 + 0x10) = lVar8 + -1;
      plVar11 = (long *)plVar10[3];
      if (plVar11 != (long *)0x0) {
        plVar2 = plVar11 + 1;
        do {
          lVar8 = *plVar2;
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar2,0x10);
          if (bVar7) {
            *plVar2 = lVar8 + -1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        if (lVar8 == 0) {
          (**(code **)(*plVar11 + 0x10))(plVar11);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar11);
        }
      }
      _ZdlPv(plVar10);
      _ZN8firebase5Mutex7ReleaseEv(lVar1);
      _ZN8firebase8callback13CallbackEntry7ExecuteEv(lVar3);
      iVar9 = iVar9 + 1;
      _ZN8firebase5Mutex7AcquireEv(lVar1);
      if (plVar5 != (long *)0x0) {
        plVar10 = plVar5 + 1;
        do {
          lVar8 = *plVar10;
          cVar6 = '\x01';
          bVar7 = (bool)ExclusiveMonitorPass(plVar10,0x10);
          if (bVar7) {
            *plVar10 = lVar8 + -1;
            cVar6 = ExclusiveMonitorsStatus();
          }
        } while (cVar6 != '\0');
        if (lVar8 == 0) {
          (**(code **)(*plVar5 + 0x10))(plVar5);
          _ZNSt6__ndk119__shared_weak_count14__release_weakEv(plVar5);
        }
      }
      lVar8 = *(long *)(param_1 + 0x10);
    } while (lVar8 != 0);
  }
  _ZN8firebase5Mutex7ReleaseEv(lVar1);
  return iVar9;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5bcfc"></a> `00b5bcfc` | `f9 0f 1b f8` | str x25,[sp, #-0x50]! | `FALL_THROUGH`
<a id="insn-00b5bd00"></a> `00b5bd00` | `f8 5f 01 a9` | stp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bd04"></a> `00b5bd04` | `f6 57 02 a9` | stp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5bd08"></a> `00b5bd08` | `f4 4f 03 a9` | stp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5bd0c"></a> `00b5bd0c` | `fd 7b 04 a9` | stp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5bd10"></a> `00b5bd10` | `fd 03 01 91` | add x29,sp,#0x40 | `FALL_THROUGH`
<a id="insn-00b5bd14"></a> `00b5bd14` | `13 60 00 91` | add x19,x0,#0x18 | `FALL_THROUGH`
<a id="insn-00b5bd18"></a> `00b5bd18` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b5bd1c"></a> `00b5bd1c` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5bd20"></a> `00b5bd20` | `38 fa 03 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bd24"></a> `00b5bd24` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bd28"></a> `00b5bd28` | `28 07 00 b4` | cbz x8,0x00b5be0c | `CONDITIONAL_JUMP`
<a id="insn-00b5bd2c"></a> `00b5bd2c` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00b5bd30"></a> `00b5bd30` | `03 00 00 14` | b 0x00b5bd3c | `UNCONDITIONAL_JUMP`
<a id="insn-00b5bd34"></a> `00b5bd34` | `88 0a 40 f9` | ldr x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bd38"></a> `00b5bd38` | `c8 06 00 b4` | cbz x8,0x00b5be10 | `CONDITIONAL_JUMP`
<a id="insn-00b5bd3c"></a> `00b5bd3c` | `98 06 40 f9` | ldr x24,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b5bd40"></a> `00b5bd40` | `17 5b 41 a9` | ldp x23,x22,[x24, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bd44"></a> `00b5bd44` | `f6 00 00 b4` | cbz x22,0x00b5bd60 | `CONDITIONAL_JUMP`
<a id="insn-00b5bd48"></a> `00b5bd48` | `c8 22 00 91` | add x8,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00b5bd4c"></a> `00b5bd4c` | `09 7d 5f c8` | ldxr x9,[x8] | `FALL_THROUGH`
<a id="insn-00b5bd50"></a> `00b5bd50` | `29 05 00 91` | add x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b5bd54"></a> `00b5bd54` | `09 7d 0a c8` | stxr w10,x9,[x8] | `FALL_THROUGH`
<a id="insn-00b5bd58"></a> `00b5bd58` | `aa ff ff 35` | cbnz w10,0x00b5bd4c | `CONDITIONAL_JUMP`
<a id="insn-00b5bd5c"></a> `00b5bd5c` | `98 a2 40 a9` | ldp x24,x8,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b5bd60"></a> `00b5bd60` | `09 2b 40 a9` | ldp x9,x10,[x24] | `FALL_THROUGH`
<a id="insn-00b5bd64"></a> `00b5bd64` | `08 05 00 d1` | sub x8,x8,#0x1 | `FALL_THROUGH`
<a id="insn-00b5bd68"></a> `00b5bd68` | `2a 05 00 f9` | str x10,[x9, #0x8] | `FALL_THROUGH`
<a id="insn-00b5bd6c"></a> `00b5bd6c` | `0a 07 40 f9` | ldr x10,[x24, #0x8] | `FALL_THROUGH`
<a id="insn-00b5bd70"></a> `00b5bd70` | `49 01 00 f9` | str x9,[x10] | `FALL_THROUGH`
<a id="insn-00b5bd74"></a> `00b5bd74` | `88 0a 00 f9` | str x8,[x20, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bd78"></a> `00b5bd78` | `19 0f 40 f9` | ldr x25,[x24, #0x18] | `FALL_THROUGH`
<a id="insn-00b5bd7c"></a> `00b5bd7c` | `b9 01 00 b4` | cbz x25,0x00b5bdb0 | `CONDITIONAL_JUMP`
<a id="insn-00b5bd80"></a> `00b5bd80` | `28 23 00 91` | add x8,x25,#0x8 | `FALL_THROUGH`
<a id="insn-00b5bd84"></a> `00b5bd84` | `09 fd 5f c8` | ldaxr x9,[x8] | `FALL_THROUGH`
<a id="insn-00b5bd88"></a> `00b5bd88` | `2a 05 00 d1` | sub x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b5bd8c"></a> `00b5bd8c` | `0a fd 0b c8` | stlxr w11,x10,[x8] | `FALL_THROUGH`
<a id="insn-00b5bd90"></a> `00b5bd90` | `ab ff ff 35` | cbnz w11,0x00b5bd84 | `CONDITIONAL_JUMP`
<a id="insn-00b5bd94"></a> `00b5bd94` | `e9 00 00 b5` | cbnz x9,0x00b5bdb0 | `CONDITIONAL_JUMP`
<a id="insn-00b5bd98"></a> `00b5bd98` | `28 03 40 f9` | ldr x8,[x25] | `FALL_THROUGH`
<a id="insn-00b5bd9c"></a> `00b5bd9c` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00b5bda0"></a> `00b5bda0` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bda4"></a> `00b5bda4` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5bda8"></a> `00b5bda8` | `e0 03 19 aa` | mov x0,x25 | `FALL_THROUGH`
<a id="insn-00b5bdac"></a> `00b5bdac` | `35 ef 03 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bdb0"></a> `00b5bdb0` | `e0 03 18 aa` | mov x0,x24 | `FALL_THROUGH`
<a id="insn-00b5bdb4"></a> `00b5bdb4` | `3f ef 03 94` | bl 0x00c57ab0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bdb8"></a> `00b5bdb8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5bdbc"></a> `00b5bdbc` | `15 fa 03 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bdc0"></a> `00b5bdc0` | `e0 03 17 aa` | mov x0,x23 | `FALL_THROUGH`
<a id="insn-00b5bdc4"></a> `00b5bdc4` | `4f fe 03 94` | bl 0x00c5b700 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bdc8"></a> `00b5bdc8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5bdcc"></a> `00b5bdcc` | `b5 06 00 11` | add w21,w21,#0x1 | `FALL_THROUGH`
<a id="insn-00b5bdd0"></a> `00b5bdd0` | `0c fa 03 94` | bl 0x00c5a600 | `UNCONDITIONAL_CALL`
<a id="insn-00b5bdd4"></a> `00b5bdd4` | `16 fb ff b4` | cbz x22,0x00b5bd34 | `CONDITIONAL_JUMP`
<a id="insn-00b5bdd8"></a> `00b5bdd8` | `c8 22 00 91` | add x8,x22,#0x8 | `FALL_THROUGH`
<a id="insn-00b5bddc"></a> `00b5bddc` | `09 fd 5f c8` | ldaxr x9,[x8] | `FALL_THROUGH`
<a id="insn-00b5bde0"></a> `00b5bde0` | `2a 05 00 d1` | sub x10,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b5bde4"></a> `00b5bde4` | `0a fd 0b c8` | stlxr w11,x10,[x8] | `FALL_THROUGH`
<a id="insn-00b5bde8"></a> `00b5bde8` | `ab ff ff 35` | cbnz w11,0x00b5bddc | `CONDITIONAL_JUMP`
<a id="insn-00b5bdec"></a> `00b5bdec` | `49 fa ff b5` | cbnz x9,0x00b5bd34 | `CONDITIONAL_JUMP`
<a id="insn-00b5bdf0"></a> `00b5bdf0` | `c8 02 40 f9` | ldr x8,[x22] | `FALL_THROUGH`
<a id="insn-00b5bdf4"></a> `00b5bdf4` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b5bdf8"></a> `00b5bdf8` | `08 09 40 f9` | ldr x8,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b5bdfc"></a> `00b5bdfc` | `00 01 3f d6` | blr x8 | `COMPUTED_CALL`
<a id="insn-00b5be00"></a> `00b5be00` | `e0 03 16 aa` | mov x0,x22 | `FALL_THROUGH`
<a id="insn-00b5be04"></a> `00b5be04` | `1f ef 03 94` | bl 0x00c57a80 | `UNCONDITIONAL_CALL`
<a id="insn-00b5be08"></a> `00b5be08` | `cb ff ff 17` | b 0x00b5bd34 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5be0c"></a> `00b5be0c` | `f5 03 1f 2a` | mov w21,wzr | `FALL_THROUGH`
<a id="insn-00b5be10"></a> `00b5be10` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5be14"></a> `00b5be14` | `ff f9 03 94` | bl 0x00c5a610 | `UNCONDITIONAL_CALL`
<a id="insn-00b5be18"></a> `00b5be18` | `e0 03 15 2a` | mov w0,w21 | `FALL_THROUGH`
<a id="insn-00b5be1c"></a> `00b5be1c` | `fd 7b 44 a9` | ldp x29,x30,[sp, #0x40] | `FALL_THROUGH`
<a id="insn-00b5be20"></a> `00b5be20` | `f4 4f 43 a9` | ldp x20,x19,[sp, #0x30] | `FALL_THROUGH`
<a id="insn-00b5be24"></a> `00b5be24` | `f6 57 42 a9` | ldp x22,x21,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5be28"></a> `00b5be28` | `f8 5f 41 a9` | ldp x24,x23,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5be2c"></a> `00b5be2c` | `f9 07 45 f8` | ldr x25,[sp], #0x50 | `FALL_THROUGH`
<a id="insn-00b5be30"></a> `00b5be30` | `c0 03 5f d6` | ret | `TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5bcfc`](#insn-00b5bcfc) 範囲 `[['00b5bcfc', '00b5bd2b']]`
  - `CONDITIONAL_JUMP` [`00b5bd28`](#insn-00b5bd28) → [`00b5be0c`](#insn-00b5be0c)
  - `FALL_THROUGH` [`00b5bd28`](#insn-00b5bd28) → [`00b5bd2c`](#insn-00b5bd2c)
- ブロック [`00b5bd2c`](#insn-00b5bd2c) 範囲 `[['00b5bd2c', '00b5bd33']]`
  - `UNCONDITIONAL_JUMP` [`00b5bd30`](#insn-00b5bd30) → [`00b5bd3c`](#insn-00b5bd3c)
- ブロック [`00b5bd34`](#insn-00b5bd34) 範囲 `[['00b5bd34', '00b5bd3b']]`
  - `CONDITIONAL_JUMP` [`00b5bd38`](#insn-00b5bd38) → [`00b5be10`](#insn-00b5be10)
  - `FALL_THROUGH` [`00b5bd38`](#insn-00b5bd38) → [`00b5bd3c`](#insn-00b5bd3c)
- ブロック [`00b5bd3c`](#insn-00b5bd3c) 範囲 `[['00b5bd3c', '00b5bd47']]`
  - `CONDITIONAL_JUMP` [`00b5bd44`](#insn-00b5bd44) → [`00b5bd60`](#insn-00b5bd60)
  - `FALL_THROUGH` [`00b5bd44`](#insn-00b5bd44) → [`00b5bd48`](#insn-00b5bd48)
- ブロック [`00b5bd48`](#insn-00b5bd48) 範囲 `[['00b5bd48', '00b5bd4b']]`
  - `FALL_THROUGH` [`00b5bd48`](#insn-00b5bd48) → [`00b5bd4c`](#insn-00b5bd4c)
- ブロック [`00b5bd4c`](#insn-00b5bd4c) 範囲 `[['00b5bd4c', '00b5bd5b']]`
  - `CONDITIONAL_JUMP` [`00b5bd58`](#insn-00b5bd58) → [`00b5bd4c`](#insn-00b5bd4c)
  - `FALL_THROUGH` [`00b5bd58`](#insn-00b5bd58) → [`00b5bd5c`](#insn-00b5bd5c)
- ブロック [`00b5bd5c`](#insn-00b5bd5c) 範囲 `[['00b5bd5c', '00b5bd5f']]`
  - `FALL_THROUGH` [`00b5bd5c`](#insn-00b5bd5c) → [`00b5bd60`](#insn-00b5bd60)
- ブロック [`00b5bd60`](#insn-00b5bd60) 範囲 `[['00b5bd60', '00b5bd7f']]`
  - `CONDITIONAL_JUMP` [`00b5bd7c`](#insn-00b5bd7c) → [`00b5bdb0`](#insn-00b5bdb0)
  - `FALL_THROUGH` [`00b5bd7c`](#insn-00b5bd7c) → [`00b5bd80`](#insn-00b5bd80)
- ブロック [`00b5bd80`](#insn-00b5bd80) 範囲 `[['00b5bd80', '00b5bd83']]`
  - `FALL_THROUGH` [`00b5bd80`](#insn-00b5bd80) → [`00b5bd84`](#insn-00b5bd84)
- ブロック [`00b5bd84`](#insn-00b5bd84) 範囲 `[['00b5bd84', '00b5bd93']]`
  - `CONDITIONAL_JUMP` [`00b5bd90`](#insn-00b5bd90) → [`00b5bd84`](#insn-00b5bd84)
  - `FALL_THROUGH` [`00b5bd90`](#insn-00b5bd90) → [`00b5bd94`](#insn-00b5bd94)
- ブロック [`00b5bd94`](#insn-00b5bd94) 範囲 `[['00b5bd94', '00b5bd97']]`
  - `CONDITIONAL_JUMP` [`00b5bd94`](#insn-00b5bd94) → [`00b5bdb0`](#insn-00b5bdb0)
  - `FALL_THROUGH` [`00b5bd94`](#insn-00b5bd94) → [`00b5bd98`](#insn-00b5bd98)
- ブロック [`00b5bd98`](#insn-00b5bd98) 範囲 `[['00b5bd98', '00b5bdaf']]`
  - `FALL_THROUGH` [`00b5bdac`](#insn-00b5bdac) → [`00b5bdb0`](#insn-00b5bdb0)
- ブロック [`00b5bdb0`](#insn-00b5bdb0) 範囲 `[['00b5bdb0', '00b5bdd7']]`
  - `CONDITIONAL_JUMP` [`00b5bdd4`](#insn-00b5bdd4) → [`00b5bd34`](#insn-00b5bd34)
  - `FALL_THROUGH` [`00b5bdd4`](#insn-00b5bdd4) → [`00b5bdd8`](#insn-00b5bdd8)
- ブロック [`00b5bdd8`](#insn-00b5bdd8) 範囲 `[['00b5bdd8', '00b5bddb']]`
  - `FALL_THROUGH` [`00b5bdd8`](#insn-00b5bdd8) → [`00b5bddc`](#insn-00b5bddc)
- ブロック [`00b5bddc`](#insn-00b5bddc) 範囲 `[['00b5bddc', '00b5bdeb']]`
  - `CONDITIONAL_JUMP` [`00b5bde8`](#insn-00b5bde8) → [`00b5bddc`](#insn-00b5bddc)
  - `FALL_THROUGH` [`00b5bde8`](#insn-00b5bde8) → [`00b5bdec`](#insn-00b5bdec)
- ブロック [`00b5bdec`](#insn-00b5bdec) 範囲 `[['00b5bdec', '00b5bdef']]`
  - `CONDITIONAL_JUMP` [`00b5bdec`](#insn-00b5bdec) → [`00b5bd34`](#insn-00b5bd34)
  - `FALL_THROUGH` [`00b5bdec`](#insn-00b5bdec) → [`00b5bdf0`](#insn-00b5bdf0)
- ブロック [`00b5bdf0`](#insn-00b5bdf0) 範囲 `[['00b5bdf0', '00b5be0b']]`
  - `UNCONDITIONAL_JUMP` [`00b5be08`](#insn-00b5be08) → [`00b5bd34`](#insn-00b5bd34)
- ブロック [`00b5be0c`](#insn-00b5be0c) 範囲 `[['00b5be0c', '00b5be0f']]`
  - `FALL_THROUGH` [`00b5be0c`](#insn-00b5be0c) → [`00b5be10`](#insn-00b5be10)
- ブロック [`00b5be10`](#insn-00b5be10) 範囲 `[['00b5be10', '00b5be33']]`

## 命令位置別の参照

- [`00b5bcfc`](#insn-00b5bcfc) → `Stack[-0x50]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd00`](#insn-00b5bd00) → `Stack[-0x40]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd04`](#insn-00b5bd04) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd08`](#insn-00b5bd08) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd0c`](#insn-00b5bd0c) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd20`](#insn-00b5bd20) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd28`](#insn-00b5bd28) → [`00b5be0c`](#insn-00b5be0c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd30`](#insn-00b5bd30) → [`00b5bd3c`](#insn-00b5bd3c) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd38`](#insn-00b5bd38) → [`00b5be10`](#insn-00b5be10) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd44`](#insn-00b5bd44) → [`00b5bd60`](#insn-00b5bd60) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd58`](#insn-00b5bd58) → [`00b5bd4c`](#insn-00b5bd4c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd7c`](#insn-00b5bd7c) → [`00b5bdb0`](#insn-00b5bdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd90`](#insn-00b5bd90) → [`00b5bd84`](#insn-00b5bd84) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bd94`](#insn-00b5bd94) → [`00b5bdb0`](#insn-00b5bdb0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bdac`](#insn-00b5bdac) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00b5bdb4`](#insn-00b5bdb4) → [`00c57ab0`](../00c57/00c57ab0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57ab0` · 推定シンボル `None` · 推定型 `None`
- [`00b5bdbc`](#insn-00b5bdbc) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00b5bdc4`](#insn-00b5bdc4) → [`00c5b700`](../00c5b/00c5b700.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b700` · 推定シンボル `None` · 推定型 `None`
- [`00b5bdd0`](#insn-00b5bdd0) → [`00c5a600`](../00c5a/00c5a600.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a600` · 推定シンボル `None` · 推定型 `None`
- [`00b5bdd4`](#insn-00b5bdd4) → [`00b5bd34`](#insn-00b5bd34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bde8`](#insn-00b5bde8) → [`00b5bddc`](#insn-00b5bddc) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5bdec`](#insn-00b5bdec) → [`00b5bd34`](#insn-00b5bd34) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be04`](#insn-00b5be04) → [`00c57a80`](../00c57/00c57a80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57a80` · 推定シンボル `None` · 推定型 `None`
- [`00b5be08`](#insn-00b5be08) → [`00b5bd34`](#insn-00b5bd34) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be14`](#insn-00b5be14) → [`00c5a610`](../00c5a/00c5a610.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5a610` · 推定シンボル `None` · 推定型 `None`
- [`00b5be1c`](#insn-00b5be1c) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be20`](#insn-00b5be20) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be24`](#insn-00b5be24) → `Stack[-0x30]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5be28`](#insn-00b5be28) → `Stack[-0x40]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5bcfc`](#insn-00b5bcfc)

~~~json
{
  "source": "00b5bcfc",
  "target": "Stack[-0x50]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd00`](#insn-00b5bd00)

~~~json
{
  "source": "00b5bd00",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd04`](#insn-00b5bd04)

~~~json
{
  "source": "00b5bd04",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd08`](#insn-00b5bd08)

~~~json
{
  "source": "00b5bd08",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd0c`](#insn-00b5bd0c)

~~~json
{
  "source": "00b5bd0c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd20`](#insn-00b5bd20)

~~~json
{
  "source": "00b5bd20",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bd28`](#insn-00b5bd28)

~~~json
{
  "source": "00b5bd28",
  "target": "00b5be0c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd30`](#insn-00b5bd30)

~~~json
{
  "source": "00b5bd30",
  "target": "00b5bd3c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd38`](#insn-00b5bd38)

~~~json
{
  "source": "00b5bd38",
  "target": "00b5be10",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd44`](#insn-00b5bd44)

~~~json
{
  "source": "00b5bd44",
  "target": "00b5bd60",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd58`](#insn-00b5bd58)

~~~json
{
  "source": "00b5bd58",
  "target": "00b5bd4c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd7c`](#insn-00b5bd7c)

~~~json
{
  "source": "00b5bd7c",
  "target": "00b5bdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd90`](#insn-00b5bd90)

~~~json
{
  "source": "00b5bd90",
  "target": "00b5bd84",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bd94`](#insn-00b5bd94)

~~~json
{
  "source": "00b5bd94",
  "target": "00b5bdb0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bdac`](#insn-00b5bdac)

~~~json
{
  "source": "00b5bdac",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bdb4`](#insn-00b5bdb4)

~~~json
{
  "source": "00b5bdb4",
  "target": "00c57ab0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bdbc`](#insn-00b5bdbc)

~~~json
{
  "source": "00b5bdbc",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bdc4`](#insn-00b5bdc4)

~~~json
{
  "source": "00b5bdc4",
  "target": "00c5b700",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bdd0`](#insn-00b5bdd0)

~~~json
{
  "source": "00b5bdd0",
  "target": "00c5a600",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5bdd4`](#insn-00b5bdd4)

~~~json
{
  "source": "00b5bdd4",
  "target": "00b5bd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bde8`](#insn-00b5bde8)

~~~json
{
  "source": "00b5bde8",
  "target": "00b5bddc",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5bdec`](#insn-00b5bdec)

~~~json
{
  "source": "00b5bdec",
  "target": "00b5bd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be04`](#insn-00b5be04)

~~~json
{
  "source": "00b5be04",
  "target": "00c57a80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5be08`](#insn-00b5be08)

~~~json
{
  "source": "00b5be08",
  "target": "00b5bd34",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be14`](#insn-00b5be14)

~~~json
{
  "source": "00b5be14",
  "target": "00c5a610",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5be1c`](#insn-00b5be1c)

~~~json
{
  "source": "00b5be1c",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be20`](#insn-00b5be20)

~~~json
{
  "source": "00b5be20",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be24`](#insn-00b5be24)

~~~json
{
  "source": "00b5be24",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5be28`](#insn-00b5be28)

~~~json
{
  "source": "00b5be28",
  "target": "Stack[-0x40]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
