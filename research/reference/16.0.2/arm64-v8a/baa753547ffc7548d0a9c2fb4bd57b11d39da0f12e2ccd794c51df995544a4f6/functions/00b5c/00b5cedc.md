# 00b5cedc

版: 16.0.2 / arm64-v8a / libnative-lib.so

SO SHA-256: `baa753547ffc7548d0a9c2fb4bd57b11d39da0f12e2ccd794c51df995544a4f6`

解析リビジョン `ea0159f06d493a87` · Ghidra `12.1.2`

<a id="comparisons"></a>

[擬似コード](#pseudocode) · [逆アセンブリ](#逆アセンブリ) · [分岐](#基本ブロックと分岐先) · [参照](#命令位置別の参照) · [比較](#comparisons)

<!-- kbcs-version-function-tracking -->
## バージョン間の関数追跡

- **前の公開版 v16.0.1**
  - 採用 · [関数詳細 `00b5ce40`](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/functions/00b5c/00b5ce40.md) · 移動量 `+0x9c`
  - [v16.0.1 → v16.0.2 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/0-1/priority-0075.md#compare-88086c4529e89ca90d79330411faa37c)
  - [v16.0.1の関数一覧](../../../../../16.0.1/arm64-v8a/2c22d76fc1ddec676d4ed6206d5ec55a02a651f407d39d1c0b32ded16fd7eabe/README.md)

- **次の公開版 v16.0.3**
  - 採用 · [関数詳細 `00b5ded0`](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/functions/00b5d/00b5ded0.md) · 移動量 `+0xff4`
  - [v16.0.2 → v16.0.3 当該関数比較](../../../../../../comparisons/arm64-v8a/d102850eb939af4f4bb0eaf5/1-2/high-0008.md#compare-99dbc6bbabcceec3cecfa7ce625e5f40)
  - [v16.0.3の関数一覧](../../../../../16.0.3/arm64-v8a/941278c8d9b42c2598836a75ff173ce3b2fb2215f8067351d5fc1d218ef67c73/README.md)

[版の関数一覧](../../README.md) · [全バージョン一覧](../../../../../README.md)
<!-- /kbcs-version-function-tracking -->

## 関数情報

~~~json
{
  "address": "00b5cedc",
  "name": "_ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nodeIS7_S5_EElEEEE",
  "size": 288,
  "external": 0,
  "thunk": 0,
  "status": "cached",
  "confidence": "unreviewed",
  "error": "",
  "source_sha256": "cc87efcc994811e8fea46e0758069651d6d7c8cf937451f30e5f10e94a309ca8",
  "source_text_sha256": "cc87efcc994811e8fea46e0758069651d6d7c8cf937451f30e5f10e94a309ca8",
  "structure_status": "available",
  "structure_provenance": "receipt_verified",
  "index_boundary_verification": "legacy_boundary_unverified",
  "index_program_id": null,
  "structure_program_id": "3440b5f9d13f8b5c",
  "analysis_link": "legacy_program_id_unavailable",
  "structure": {
    "ranges": [
      [
        "00b5cedc",
        "00b5cffb"
      ]
    ],
    "bytes_sha256": "ad9365c2567533fec95255d7b09850ec492e45bdecd1c65e66a468036e8aad3c",
    "instruction_count": 72,
    "instruction_bytes": 288,
    "body_bytes": 288,
    "indirect": 0,
    "unresolved": 0
  }
}
~~~

## 呼び出し元

- [00c5bc70](../00c5b/00c5bc70.md)

## 呼び出し先

- [00c57f80](../00c57/00c57f80.md)
- [00c58010](../00c58/00c58010.md)
- [00c5aad0](../00c5a/00c5aad0.md)
- [00c5aae0](../00c5a/00c5aae0.md)
- [00c5b6a0](../00c5b/00c5b6a0.md)

<a id="pseudocode"></a>

Ghidraによる復元。型・変数名・制御構造は推定です。

## 疑似コード / UTF-8 6277 bytes

~~~c

void _ZN8firebase15CleanupNotifier15UnregisterOwnerENSt6__ndk114__map_iteratorINS1_15__tree_iteratorINS1_12__value_typeIPvPS0_EEPNS1_11__tree_nodeIS7_S5_EElEEEE
               (void *param_1)

{
  long *plVar1;
  long lVar2;
  long lVar3;
  size_t __n;
  undefined8 *puVar4;
  long *plVar5;
  long *plVar6;
  long lVar7;
  undefined8 uVar8;
  long *plVar9;
  
                    /* catch() { ... } // from try @ 00b572a8 with catch @ 00b5cedc */
                    /* catch() { ... } // from try @ 00b57248 with catch @ 00b5cee0 */
                    /* catch() { ... } // from try @ 00b5723c with catch @ 00b5cee4 */
                    /* catch() { ... } // from try @ 00b571b8 with catch @ 00b5cee8 */
                    /* catch() { ... } // from try @ 00b571ac with catch @ 00b5ceec */
                    /* catch() { ... } // from try @ 00b57138 with catch @ 00b5cef0 */
                    /* catch() { ... } // from try @ 00b5712c with catch @ 00b5cef4 */
                    /* catch() { ... } // from try @ 00b5711c with catch @ 00b5cef8 */
  uVar8 = *(undefined8 *)
           PTR__ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E_00c9b868;
                    /* catch() { ... } // from try @ 00b570f4 with catch @ 00b5cf00 */
  _ZN8firebase5Mutex7AcquireEv(uVar8);
                    /* catch() { ... } // from try @ 00b57090 with catch @ 00b5cf04 */
                    /* catch() { ... } // from try @ 00b57084 with catch @ 00b5cf08 */
  lVar2 = *(long *)((long)param_1 + 0x20);
  lVar3 = *(long *)((long)param_1 + 0x28);
                    /* catch() { ... } // from try @ 00b57074 with catch @ 00b5cf0c */
                    /* catch() { ... } // from try @ 00b5704c with catch @ 00b5cf14 */
  puVar4 = *(undefined8 **)PTR__ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E_00c9b860;
                    /* catch() { ... } // from try @ 00b57010 with catch @ 00b5cf18 */
  plVar6 = *(long **)((long)param_1 + 8);
  if (*(long **)((long)param_1 + 8) == (long *)0x0) {
                    /* catch() { ... } // from try @ 00b57004 with catch @ 00b5cf30 */
    plVar6 = (long *)((long)param_1 + 0x10);
    plVar5 = (long *)*plVar6;
    if ((void *)*plVar5 != param_1) {
      do {
        lVar7 = *plVar6;
        plVar6 = (long *)(lVar7 + 0x10);
        plVar5 = (long *)*plVar6;
                    /* catch() { ... } // from try @ 00b56ff4 with catch @ 00b5cf50 */
      } while (*plVar5 != lVar7);
    }
  }
  else {
    do {
      plVar5 = plVar6;
      plVar6 = (long *)*plVar5;
    } while ((long *)*plVar5 != (long *)0x0);
  }
                    /* catch() { ... } // from try @ 00b56fcc with catch @ 00b5cf58 */
                    /* catch() { ... } // from try @ 00b56f70 with catch @ 00b5cf5c */
                    /* catch() { ... } // from try @ 00b56f64 with catch @ 00b5cf60 */
  if ((void *)*puVar4 == param_1) {
                    /* catch() { ... } // from try @ 00b56f04 with catch @ 00b5cf64 */
    *puVar4 = plVar5;
  }
                    /* catch() { ... } // from try @ 00b56ef8 with catch @ 00b5cf68 */
                    /* catch() { ... } // from try @ 00b56e74 with catch @ 00b5cf6c */
                    /* catch() { ... } // from try @ 00b56e68 with catch @ 00b5cf70 */
                    /* catch() { ... } // from try @ 00b56e0c with catch @ 00b5cf74 */
  puVar4[2] = puVar4[2] + -1;
                    /* catch() { ... } // from try @ 00b56e00 with catch @ 00b5cf78 */
  _ZNSt6__ndk113__tree_removeIPNS_16__tree_node_baseIPvEEEEvT_S5_(puVar4[1],param_1);
                    /* catch() { ... } // from try @ 00b56d7c with catch @ 00b5cf7c */
                    /* catch() { ... } // from try @ 00b56d70 with catch @ 00b5cf80 */
  _ZdlPv(param_1);
                    /* catch() { ... } // from try @ 00b56d10 with catch @ 00b5cf84 */
  plVar6 = *(long **)(lVar3 + 0x48);
  plVar5 = *(long **)(lVar3 + 0x50);
                    /* catch() { ... } // from try @ 00b56d04 with catch @ 00b5cf88 */
                    /* catch() { ... } // from try @ 00b56c80 with catch @ 00b5cf8c */
                    /* catch() { ... } // from try @ 00b56c74 with catch @ 00b5cf90 */
                    /* catch() { ... } // from try @ 00b56c14 with catch @ 00b5cf94 */
                    /* catch() { ... } // from try @ 00b56c08 with catch @ 00b5cf98 */
  if ((plVar6 != plVar5) && (*plVar6 != lVar2)) {
                    /* catch() { ... } // from try @ 00b56b7c with catch @ 00b5cf9c */
    plVar9 = plVar6;
    do {
                    /* catch() { ... } // from try @ 00b56b70 with catch @ 00b5cfa0 */
      plVar6 = plVar5;
                    /* catch() { ... } // from try @ 00b56b00 with catch @ 00b5cfa4 */
      if (plVar5 + -1 == plVar9) break;
      plVar1 = plVar9 + 1;
                    /* catch() { ... } // from try @ 00b56af4 with catch @ 00b5cfa8 */
                    /* catch() { ... } // from try @ 00b56860 with catch @ 00b5cfac */
      plVar6 = plVar9 + 1;
                    /* catch() { ... } // from try @ 00b56830 with catch @ 00b5cfb0 */
                    /* catch() { ... } // from try @ 00b5680c with catch @ 00b5cfb4 */
      plVar9 = plVar6;
                    /* catch() { ... } // from try @ 00b567dc with catch @ 00b5cfb8 */
    } while (*plVar1 != lVar2);
  }
  __n = (long)plVar5 - (long)(plVar6 + 1);
                    /* catch() { ... } // from try @ 00b5670c with catch @ 00b5cfd4 */
  if (__n != 0) {
                    /* catch() { ... } // from try @ 00b5668c with catch @ 00b5cfd8 */
                    /* catch() { ... } // from try @ 00b56654 with catch @ 00b5cfdc */
    memmove(plVar6,plVar6 + 1,__n);
  }
                    /* catch() { ... } // from try @ 00b5661c with catch @ 00b5cfe4 */
  *(long **)(lVar3 + 0x50) = plVar6 + ((long)__n >> 3);
                    /* catch() { ... } // from try @ 00b565a4 with catch @ 00b5cfe8 */
                    /* catch() { ... } // from try @ 00b56598 with catch @ 00b5cfec */
                    /* catch() { ... } // from try @ 00b56540 with catch @ 00b5cff0 */
                    /* catch() { ... } // from try @ 00b56534 with catch @ 00b5cff4 */
                    /* catch() { ... } // from try @ 00b564d4 with catch @ 00b5cff8 */
  _ZN8firebase5Mutex7ReleaseEv(uVar8);
  return;
}

~~~

## 逆アセンブリ

命令アドレス、生バイト（メモリ順）、オペランド、フロー。

| アドレス | 生バイト | 命令・オペランド | フロー |
| --- | --- | --- | --- |
<a id="insn-00b5cedc"></a> `00b5cedc` | `f6 57 bd a9` | stp x22,x21,[sp, #-0x30]! | `FALL_THROUGH`
<a id="insn-00b5cee0"></a> `00b5cee0` | `f4 4f 01 a9` | stp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cee4"></a> `00b5cee4` | `fd 7b 02 a9` | stp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5cee8"></a> `00b5cee8` | `fd 83 00 91` | add x29,sp,#0x20 | `FALL_THROUGH`
<a id="insn-00b5ceec"></a> `00b5ceec` | `e8 09 00 f0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00b5cef0"></a> `00b5cef0` | `08 35 44 f9` | ldr x8,[x8, #0x868] | `FALL_THROUGH`
<a id="insn-00b5cef4"></a> `00b5cef4` | `f4 03 00 aa` | mov x20,x0 | `FALL_THROUGH`
<a id="insn-00b5cef8"></a> `00b5cef8` | `13 01 40 f9` | ldr x19,[x8] | `FALL_THROUGH`
<a id="insn-00b5cefc"></a> `00b5cefc` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5cf00"></a> `00b5cf00` | `f4 f6 03 94` | bl 0x00c5aad0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cf04"></a> `00b5cf04` | `e8 09 00 f0` | adrp x8,0xc9b000 | `FALL_THROUGH`
<a id="insn-00b5cf08"></a> `00b5cf08` | `96 56 42 a9` | ldp x22,x21,[x20, #0x20] | `FALL_THROUGH`
<a id="insn-00b5cf0c"></a> `00b5cf0c` | `08 31 44 f9` | ldr x8,[x8, #0x860] | `FALL_THROUGH`
<a id="insn-00b5cf10"></a> `00b5cf10` | `8a 06 40 f9` | ldr x10,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b5cf14"></a> `00b5cf14` | `08 01 40 f9` | ldr x8,[x8] | `FALL_THROUGH`
<a id="insn-00b5cf18"></a> `00b5cf18` | `aa 00 00 b4` | cbz x10,0x00b5cf2c | `CONDITIONAL_JUMP`
<a id="insn-00b5cf1c"></a> `00b5cf1c` | `e9 03 0a aa` | mov x9,x10 | `FALL_THROUGH`
<a id="insn-00b5cf20"></a> `00b5cf20` | `4a 01 40 f9` | ldr x10,[x10] | `FALL_THROUGH`
<a id="insn-00b5cf24"></a> `00b5cf24` | `ca ff ff b5` | cbnz x10,0x00b5cf1c | `CONDITIONAL_JUMP`
<a id="insn-00b5cf28"></a> `00b5cf28` | `0c 00 00 14` | b 0x00b5cf58 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5cf2c"></a> `00b5cf2c` | `ea 03 14 aa` | mov x10,x20 | `FALL_THROUGH`
<a id="insn-00b5cf30"></a> `00b5cf30` | `49 0d 41 f8` | ldr x9,[x10, #0x10]! | `FALL_THROUGH`
<a id="insn-00b5cf34"></a> `00b5cf34` | `2b 01 40 f9` | ldr x11,[x9] | `FALL_THROUGH`
<a id="insn-00b5cf38"></a> `00b5cf38` | `7f 01 14 eb` | cmp x11,x20 | `FALL_THROUGH`
<a id="insn-00b5cf3c"></a> `00b5cf3c` | `e0 00 00 54` | b.eq 0x00b5cf58 | `CONDITIONAL_JUMP`
<a id="insn-00b5cf40"></a> `00b5cf40` | `4b 01 40 f9` | ldr x11,[x10] | `FALL_THROUGH`
<a id="insn-00b5cf44"></a> `00b5cf44` | `ea 03 0b aa` | mov x10,x11 | `FALL_THROUGH`
<a id="insn-00b5cf48"></a> `00b5cf48` | `49 0d 41 f8` | ldr x9,[x10, #0x10]! | `FALL_THROUGH`
<a id="insn-00b5cf4c"></a> `00b5cf4c` | `2c 01 40 f9` | ldr x12,[x9] | `FALL_THROUGH`
<a id="insn-00b5cf50"></a> `00b5cf50` | `9f 01 0b eb` | cmp x12,x11 | `FALL_THROUGH`
<a id="insn-00b5cf54"></a> `00b5cf54` | `61 ff ff 54` | b.ne 0x00b5cf40 | `CONDITIONAL_JUMP`
<a id="insn-00b5cf58"></a> `00b5cf58` | `0a 01 40 f9` | ldr x10,[x8] | `FALL_THROUGH`
<a id="insn-00b5cf5c"></a> `00b5cf5c` | `5f 01 14 eb` | cmp x10,x20 | `FALL_THROUGH`
<a id="insn-00b5cf60"></a> `00b5cf60` | `41 00 00 54` | b.ne 0x00b5cf68 | `CONDITIONAL_JUMP`
<a id="insn-00b5cf64"></a> `00b5cf64` | `09 01 00 f9` | str x9,[x8] | `FALL_THROUGH`
<a id="insn-00b5cf68"></a> `00b5cf68` | `00 a5 40 a9` | ldp x0,x9,[x8, #0x8] | `FALL_THROUGH`
<a id="insn-00b5cf6c"></a> `00b5cf6c` | `e1 03 14 aa` | mov x1,x20 | `FALL_THROUGH`
<a id="insn-00b5cf70"></a> `00b5cf70` | `29 05 00 d1` | sub x9,x9,#0x1 | `FALL_THROUGH`
<a id="insn-00b5cf74"></a> `00b5cf74` | `09 09 00 f9` | str x9,[x8, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cf78"></a> `00b5cf78` | `ca f9 03 94` | bl 0x00c5b6a0 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cf7c"></a> `00b5cf7c` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b5cf80"></a> `00b5cf80` | `00 ec 03 94` | bl 0x00c57f80 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cf84"></a> `00b5cf84` | `b4 a2 44 a9` | ldp x20,x8,[x21, #0x48] | `FALL_THROUGH`
<a id="insn-00b5cf88"></a> `00b5cf88` | `9f 02 08 eb` | cmp x20,x8 | `FALL_THROUGH`
<a id="insn-00b5cf8c"></a> `00b5cf8c` | `e0 01 00 54` | b.eq 0x00b5cfc8 | `CONDITIONAL_JUMP`
<a id="insn-00b5cf90"></a> `00b5cf90` | `89 02 40 f9` | ldr x9,[x20] | `FALL_THROUGH`
<a id="insn-00b5cf94"></a> `00b5cf94` | `3f 01 16 eb` | cmp x9,x22 | `FALL_THROUGH`
<a id="insn-00b5cf98"></a> `00b5cf98` | `80 01 00 54` | b.eq 0x00b5cfc8 | `CONDITIONAL_JUMP`
<a id="insn-00b5cf9c"></a> `00b5cf9c` | `09 21 00 d1` | sub x9,x8,#0x8 | `FALL_THROUGH`
<a id="insn-00b5cfa0"></a> `00b5cfa0` | `3f 01 14 eb` | cmp x9,x20 | `FALL_THROUGH`
<a id="insn-00b5cfa4"></a> `00b5cfa4` | `00 01 00 54` | b.eq 0x00b5cfc4 | `CONDITIONAL_JUMP`
<a id="insn-00b5cfa8"></a> `00b5cfa8` | `8b 06 40 f9` | ldr x11,[x20, #0x8] | `FALL_THROUGH`
<a id="insn-00b5cfac"></a> `00b5cfac` | `8a 22 00 91` | add x10,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00b5cfb0"></a> `00b5cfb0` | `f4 03 0a aa` | mov x20,x10 | `FALL_THROUGH`
<a id="insn-00b5cfb4"></a> `00b5cfb4` | `7f 01 16 eb` | cmp x11,x22 | `FALL_THROUGH`
<a id="insn-00b5cfb8"></a> `00b5cfb8` | `41 ff ff 54` | b.ne 0x00b5cfa0 | `CONDITIONAL_JUMP`
<a id="insn-00b5cfbc"></a> `00b5cfbc` | `f4 03 0a aa` | mov x20,x10 | `FALL_THROUGH`
<a id="insn-00b5cfc0"></a> `00b5cfc0` | `02 00 00 14` | b 0x00b5cfc8 | `UNCONDITIONAL_JUMP`
<a id="insn-00b5cfc4"></a> `00b5cfc4` | `f4 03 08 aa` | mov x20,x8 | `FALL_THROUGH`
<a id="insn-00b5cfc8"></a> `00b5cfc8` | `81 22 00 91` | add x1,x20,#0x8 | `FALL_THROUGH`
<a id="insn-00b5cfcc"></a> `00b5cfcc` | `02 01 01 eb` | subs x2,x8,x1 | `FALL_THROUGH`
<a id="insn-00b5cfd0"></a> `00b5cfd0` | `56 fc 43 93` | asr x22,x2,#0x3 | `FALL_THROUGH`
<a id="insn-00b5cfd4"></a> `00b5cfd4` | `60 00 00 54` | b.eq 0x00b5cfe0 | `CONDITIONAL_JUMP`
<a id="insn-00b5cfd8"></a> `00b5cfd8` | `e0 03 14 aa` | mov x0,x20 | `FALL_THROUGH`
<a id="insn-00b5cfdc"></a> `00b5cfdc` | `0d ec 03 94` | bl 0x00c58010 | `UNCONDITIONAL_CALL`
<a id="insn-00b5cfe0"></a> `00b5cfe0` | `88 0e 16 8b` | add x8,x20,x22, LSL #0x3 | `FALL_THROUGH`
<a id="insn-00b5cfe4"></a> `00b5cfe4` | `a8 2a 00 f9` | str x8,[x21, #0x50] | `FALL_THROUGH`
<a id="insn-00b5cfe8"></a> `00b5cfe8` | `e0 03 13 aa` | mov x0,x19 | `FALL_THROUGH`
<a id="insn-00b5cfec"></a> `00b5cfec` | `fd 7b 42 a9` | ldp x29,x30,[sp, #0x20] | `FALL_THROUGH`
<a id="insn-00b5cff0"></a> `00b5cff0` | `f4 4f 41 a9` | ldp x20,x19,[sp, #0x10] | `FALL_THROUGH`
<a id="insn-00b5cff4"></a> `00b5cff4` | `f6 57 c3 a8` | ldp x22,x21,[sp], #0x30 | `FALL_THROUGH`
<a id="insn-00b5cff8"></a> `00b5cff8` | `ba f6 03 14` | b 0x00c5aae0 | `CALL_TERMINATOR`

## 基本ブロックと分岐先

- ブロック [`00b5cedc`](#insn-00b5cedc) 範囲 `[['00b5cedc', '00b5cedf']]`
  - `FALL_THROUGH` [`00b5cedc`](#insn-00b5cedc) → [`00b5cee0`](#insn-00b5cee0)
- ブロック [`00b5cee0`](#insn-00b5cee0) 範囲 `[['00b5cee0', '00b5cee3']]`
  - `FALL_THROUGH` [`00b5cee0`](#insn-00b5cee0) → [`00b5cee4`](#insn-00b5cee4)
- ブロック [`00b5cee4`](#insn-00b5cee4) 範囲 `[['00b5cee4', '00b5cee7']]`
  - `FALL_THROUGH` [`00b5cee4`](#insn-00b5cee4) → [`00b5cee8`](#insn-00b5cee8)
- ブロック [`00b5cee8`](#insn-00b5cee8) 範囲 `[['00b5cee8', '00b5ceeb']]`
  - `FALL_THROUGH` [`00b5cee8`](#insn-00b5cee8) → [`00b5ceec`](#insn-00b5ceec)
- ブロック [`00b5ceec`](#insn-00b5ceec) 範囲 `[['00b5ceec', '00b5ceef']]`
  - `FALL_THROUGH` [`00b5ceec`](#insn-00b5ceec) → [`00b5cef0`](#insn-00b5cef0)
- ブロック [`00b5cef0`](#insn-00b5cef0) 範囲 `[['00b5cef0', '00b5cef3']]`
  - `FALL_THROUGH` [`00b5cef0`](#insn-00b5cef0) → [`00b5cef4`](#insn-00b5cef4)
- ブロック [`00b5cef4`](#insn-00b5cef4) 範囲 `[['00b5cef4', '00b5cef7']]`
  - `FALL_THROUGH` [`00b5cef4`](#insn-00b5cef4) → [`00b5cef8`](#insn-00b5cef8)
- ブロック [`00b5cef8`](#insn-00b5cef8) 範囲 `[['00b5cef8', '00b5ceff']]`
  - `FALL_THROUGH` [`00b5cefc`](#insn-00b5cefc) → [`00b5cf00`](#insn-00b5cf00)
- ブロック [`00b5cf00`](#insn-00b5cf00) 範囲 `[['00b5cf00', '00b5cf03']]`
  - `FALL_THROUGH` [`00b5cf00`](#insn-00b5cf00) → [`00b5cf04`](#insn-00b5cf04)
- ブロック [`00b5cf04`](#insn-00b5cf04) 範囲 `[['00b5cf04', '00b5cf07']]`
  - `FALL_THROUGH` [`00b5cf04`](#insn-00b5cf04) → [`00b5cf08`](#insn-00b5cf08)
- ブロック [`00b5cf08`](#insn-00b5cf08) 範囲 `[['00b5cf08', '00b5cf0b']]`
  - `FALL_THROUGH` [`00b5cf08`](#insn-00b5cf08) → [`00b5cf0c`](#insn-00b5cf0c)
- ブロック [`00b5cf0c`](#insn-00b5cf0c) 範囲 `[['00b5cf0c', '00b5cf13']]`
  - `FALL_THROUGH` [`00b5cf10`](#insn-00b5cf10) → [`00b5cf14`](#insn-00b5cf14)
- ブロック [`00b5cf14`](#insn-00b5cf14) 範囲 `[['00b5cf14', '00b5cf17']]`
  - `FALL_THROUGH` [`00b5cf14`](#insn-00b5cf14) → [`00b5cf18`](#insn-00b5cf18)
- ブロック [`00b5cf18`](#insn-00b5cf18) 範囲 `[['00b5cf18', '00b5cf1b']]`
  - `CONDITIONAL_JUMP` [`00b5cf18`](#insn-00b5cf18) → [`00b5cf2c`](#insn-00b5cf2c)
  - `FALL_THROUGH` [`00b5cf18`](#insn-00b5cf18) → [`00b5cf1c`](#insn-00b5cf1c)
- ブロック [`00b5cf1c`](#insn-00b5cf1c) 範囲 `[['00b5cf1c', '00b5cf27']]`
  - `CONDITIONAL_JUMP` [`00b5cf24`](#insn-00b5cf24) → [`00b5cf1c`](#insn-00b5cf1c)
  - `FALL_THROUGH` [`00b5cf24`](#insn-00b5cf24) → [`00b5cf28`](#insn-00b5cf28)
- ブロック [`00b5cf28`](#insn-00b5cf28) 範囲 `[['00b5cf28', '00b5cf2b']]`
  - `UNCONDITIONAL_JUMP` [`00b5cf28`](#insn-00b5cf28) → [`00b5cf58`](#insn-00b5cf58)
- ブロック [`00b5cf2c`](#insn-00b5cf2c) 範囲 `[['00b5cf2c', '00b5cf2f']]`
  - `FALL_THROUGH` [`00b5cf2c`](#insn-00b5cf2c) → [`00b5cf30`](#insn-00b5cf30)
- ブロック [`00b5cf30`](#insn-00b5cf30) 範囲 `[['00b5cf30', '00b5cf3f']]`
  - `CONDITIONAL_JUMP` [`00b5cf3c`](#insn-00b5cf3c) → [`00b5cf58`](#insn-00b5cf58)
  - `FALL_THROUGH` [`00b5cf3c`](#insn-00b5cf3c) → [`00b5cf40`](#insn-00b5cf40)
- ブロック [`00b5cf40`](#insn-00b5cf40) 範囲 `[['00b5cf40', '00b5cf4f']]`
  - `FALL_THROUGH` [`00b5cf4c`](#insn-00b5cf4c) → [`00b5cf50`](#insn-00b5cf50)
- ブロック [`00b5cf50`](#insn-00b5cf50) 範囲 `[['00b5cf50', '00b5cf57']]`
  - `CONDITIONAL_JUMP` [`00b5cf54`](#insn-00b5cf54) → [`00b5cf40`](#insn-00b5cf40)
  - `FALL_THROUGH` [`00b5cf54`](#insn-00b5cf54) → [`00b5cf58`](#insn-00b5cf58)
- ブロック [`00b5cf58`](#insn-00b5cf58) 範囲 `[['00b5cf58', '00b5cf5b']]`
  - `FALL_THROUGH` [`00b5cf58`](#insn-00b5cf58) → [`00b5cf5c`](#insn-00b5cf5c)
- ブロック [`00b5cf5c`](#insn-00b5cf5c) 範囲 `[['00b5cf5c', '00b5cf5f']]`
  - `FALL_THROUGH` [`00b5cf5c`](#insn-00b5cf5c) → [`00b5cf60`](#insn-00b5cf60)
- ブロック [`00b5cf60`](#insn-00b5cf60) 範囲 `[['00b5cf60', '00b5cf63']]`
  - `CONDITIONAL_JUMP` [`00b5cf60`](#insn-00b5cf60) → [`00b5cf68`](#insn-00b5cf68)
  - `FALL_THROUGH` [`00b5cf60`](#insn-00b5cf60) → [`00b5cf64`](#insn-00b5cf64)
- ブロック [`00b5cf64`](#insn-00b5cf64) 範囲 `[['00b5cf64', '00b5cf67']]`
  - `FALL_THROUGH` [`00b5cf64`](#insn-00b5cf64) → [`00b5cf68`](#insn-00b5cf68)
- ブロック [`00b5cf68`](#insn-00b5cf68) 範囲 `[['00b5cf68', '00b5cf6b']]`
  - `FALL_THROUGH` [`00b5cf68`](#insn-00b5cf68) → [`00b5cf6c`](#insn-00b5cf6c)
- ブロック [`00b5cf6c`](#insn-00b5cf6c) 範囲 `[['00b5cf6c', '00b5cf6f']]`
  - `FALL_THROUGH` [`00b5cf6c`](#insn-00b5cf6c) → [`00b5cf70`](#insn-00b5cf70)
- ブロック [`00b5cf70`](#insn-00b5cf70) 範囲 `[['00b5cf70', '00b5cf73']]`
  - `FALL_THROUGH` [`00b5cf70`](#insn-00b5cf70) → [`00b5cf74`](#insn-00b5cf74)
- ブロック [`00b5cf74`](#insn-00b5cf74) 範囲 `[['00b5cf74', '00b5cf77']]`
  - `FALL_THROUGH` [`00b5cf74`](#insn-00b5cf74) → [`00b5cf78`](#insn-00b5cf78)
- ブロック [`00b5cf78`](#insn-00b5cf78) 範囲 `[['00b5cf78', '00b5cf7b']]`
  - `FALL_THROUGH` [`00b5cf78`](#insn-00b5cf78) → [`00b5cf7c`](#insn-00b5cf7c)
- ブロック [`00b5cf7c`](#insn-00b5cf7c) 範囲 `[['00b5cf7c', '00b5cf7f']]`
  - `FALL_THROUGH` [`00b5cf7c`](#insn-00b5cf7c) → [`00b5cf80`](#insn-00b5cf80)
- ブロック [`00b5cf80`](#insn-00b5cf80) 範囲 `[['00b5cf80', '00b5cf83']]`
  - `FALL_THROUGH` [`00b5cf80`](#insn-00b5cf80) → [`00b5cf84`](#insn-00b5cf84)
- ブロック [`00b5cf84`](#insn-00b5cf84) 範囲 `[['00b5cf84', '00b5cf87']]`
  - `FALL_THROUGH` [`00b5cf84`](#insn-00b5cf84) → [`00b5cf88`](#insn-00b5cf88)
- ブロック [`00b5cf88`](#insn-00b5cf88) 範囲 `[['00b5cf88', '00b5cf8b']]`
  - `FALL_THROUGH` [`00b5cf88`](#insn-00b5cf88) → [`00b5cf8c`](#insn-00b5cf8c)
- ブロック [`00b5cf8c`](#insn-00b5cf8c) 範囲 `[['00b5cf8c', '00b5cf8f']]`
  - `CONDITIONAL_JUMP` [`00b5cf8c`](#insn-00b5cf8c) → [`00b5cfc8`](#insn-00b5cfc8)
  - `FALL_THROUGH` [`00b5cf8c`](#insn-00b5cf8c) → [`00b5cf90`](#insn-00b5cf90)
- ブロック [`00b5cf90`](#insn-00b5cf90) 範囲 `[['00b5cf90', '00b5cf93']]`
  - `FALL_THROUGH` [`00b5cf90`](#insn-00b5cf90) → [`00b5cf94`](#insn-00b5cf94)
- ブロック [`00b5cf94`](#insn-00b5cf94) 範囲 `[['00b5cf94', '00b5cf97']]`
  - `FALL_THROUGH` [`00b5cf94`](#insn-00b5cf94) → [`00b5cf98`](#insn-00b5cf98)
- ブロック [`00b5cf98`](#insn-00b5cf98) 範囲 `[['00b5cf98', '00b5cf9b']]`
  - `CONDITIONAL_JUMP` [`00b5cf98`](#insn-00b5cf98) → [`00b5cfc8`](#insn-00b5cfc8)
  - `FALL_THROUGH` [`00b5cf98`](#insn-00b5cf98) → [`00b5cf9c`](#insn-00b5cf9c)
- ブロック [`00b5cf9c`](#insn-00b5cf9c) 範囲 `[['00b5cf9c', '00b5cf9f']]`
  - `FALL_THROUGH` [`00b5cf9c`](#insn-00b5cf9c) → [`00b5cfa0`](#insn-00b5cfa0)
- ブロック [`00b5cfa0`](#insn-00b5cfa0) 範囲 `[['00b5cfa0', '00b5cfa3']]`
  - `FALL_THROUGH` [`00b5cfa0`](#insn-00b5cfa0) → [`00b5cfa4`](#insn-00b5cfa4)
- ブロック [`00b5cfa4`](#insn-00b5cfa4) 範囲 `[['00b5cfa4', '00b5cfa7']]`
  - `CONDITIONAL_JUMP` [`00b5cfa4`](#insn-00b5cfa4) → [`00b5cfc4`](#insn-00b5cfc4)
  - `FALL_THROUGH` [`00b5cfa4`](#insn-00b5cfa4) → [`00b5cfa8`](#insn-00b5cfa8)
- ブロック [`00b5cfa8`](#insn-00b5cfa8) 範囲 `[['00b5cfa8', '00b5cfab']]`
  - `FALL_THROUGH` [`00b5cfa8`](#insn-00b5cfa8) → [`00b5cfac`](#insn-00b5cfac)
- ブロック [`00b5cfac`](#insn-00b5cfac) 範囲 `[['00b5cfac', '00b5cfaf']]`
  - `FALL_THROUGH` [`00b5cfac`](#insn-00b5cfac) → [`00b5cfb0`](#insn-00b5cfb0)
- ブロック [`00b5cfb0`](#insn-00b5cfb0) 範囲 `[['00b5cfb0', '00b5cfb3']]`
  - `FALL_THROUGH` [`00b5cfb0`](#insn-00b5cfb0) → [`00b5cfb4`](#insn-00b5cfb4)
- ブロック [`00b5cfb4`](#insn-00b5cfb4) 範囲 `[['00b5cfb4', '00b5cfb7']]`
  - `FALL_THROUGH` [`00b5cfb4`](#insn-00b5cfb4) → [`00b5cfb8`](#insn-00b5cfb8)
- ブロック [`00b5cfb8`](#insn-00b5cfb8) 範囲 `[['00b5cfb8', '00b5cfbb']]`
  - `CONDITIONAL_JUMP` [`00b5cfb8`](#insn-00b5cfb8) → [`00b5cfa0`](#insn-00b5cfa0)
  - `FALL_THROUGH` [`00b5cfb8`](#insn-00b5cfb8) → [`00b5cfbc`](#insn-00b5cfbc)
- ブロック [`00b5cfbc`](#insn-00b5cfbc) 範囲 `[['00b5cfbc', '00b5cfbf']]`
  - `FALL_THROUGH` [`00b5cfbc`](#insn-00b5cfbc) → [`00b5cfc0`](#insn-00b5cfc0)
- ブロック [`00b5cfc0`](#insn-00b5cfc0) 範囲 `[['00b5cfc0', '00b5cfc3']]`
  - `UNCONDITIONAL_JUMP` [`00b5cfc0`](#insn-00b5cfc0) → [`00b5cfc8`](#insn-00b5cfc8)
- ブロック [`00b5cfc4`](#insn-00b5cfc4) 範囲 `[['00b5cfc4', '00b5cfc7']]`
  - `FALL_THROUGH` [`00b5cfc4`](#insn-00b5cfc4) → [`00b5cfc8`](#insn-00b5cfc8)
- ブロック [`00b5cfc8`](#insn-00b5cfc8) 範囲 `[['00b5cfc8', '00b5cfd3']]`
  - `FALL_THROUGH` [`00b5cfd0`](#insn-00b5cfd0) → [`00b5cfd4`](#insn-00b5cfd4)
- ブロック [`00b5cfd4`](#insn-00b5cfd4) 範囲 `[['00b5cfd4', '00b5cfd7']]`
  - `CONDITIONAL_JUMP` [`00b5cfd4`](#insn-00b5cfd4) → [`00b5cfe0`](#insn-00b5cfe0)
  - `FALL_THROUGH` [`00b5cfd4`](#insn-00b5cfd4) → [`00b5cfd8`](#insn-00b5cfd8)
- ブロック [`00b5cfd8`](#insn-00b5cfd8) 範囲 `[['00b5cfd8', '00b5cfdb']]`
  - `FALL_THROUGH` [`00b5cfd8`](#insn-00b5cfd8) → [`00b5cfdc`](#insn-00b5cfdc)
- ブロック [`00b5cfdc`](#insn-00b5cfdc) 範囲 `[['00b5cfdc', '00b5cfdf']]`
  - `FALL_THROUGH` [`00b5cfdc`](#insn-00b5cfdc) → [`00b5cfe0`](#insn-00b5cfe0)
- ブロック [`00b5cfe0`](#insn-00b5cfe0) 範囲 `[['00b5cfe0', '00b5cfe3']]`
  - `FALL_THROUGH` [`00b5cfe0`](#insn-00b5cfe0) → [`00b5cfe4`](#insn-00b5cfe4)
- ブロック [`00b5cfe4`](#insn-00b5cfe4) 範囲 `[['00b5cfe4', '00b5cfe7']]`
  - `FALL_THROUGH` [`00b5cfe4`](#insn-00b5cfe4) → [`00b5cfe8`](#insn-00b5cfe8)
- ブロック [`00b5cfe8`](#insn-00b5cfe8) 範囲 `[['00b5cfe8', '00b5cfeb']]`
  - `FALL_THROUGH` [`00b5cfe8`](#insn-00b5cfe8) → [`00b5cfec`](#insn-00b5cfec)
- ブロック [`00b5cfec`](#insn-00b5cfec) 範囲 `[['00b5cfec', '00b5cfef']]`
  - `FALL_THROUGH` [`00b5cfec`](#insn-00b5cfec) → [`00b5cff0`](#insn-00b5cff0)
- ブロック [`00b5cff0`](#insn-00b5cff0) 範囲 `[['00b5cff0', '00b5cff3']]`
  - `FALL_THROUGH` [`00b5cff0`](#insn-00b5cff0) → [`00b5cff4`](#insn-00b5cff4)
- ブロック [`00b5cff4`](#insn-00b5cff4) 範囲 `[['00b5cff4', '00b5cff7']]`
  - `FALL_THROUGH` [`00b5cff4`](#insn-00b5cff4) → [`00b5cff8`](#insn-00b5cff8)
- ブロック [`00b5cff8`](#insn-00b5cff8) 範囲 `[['00b5cff8', '00b5cffb']]`

## 命令位置別の参照

- [`00b5cedc`](#insn-00b5cedc) → `Stack[-0x30]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cee0`](#insn-00b5cee0) → `Stack[-0x20]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cee4`](#insn-00b5cee4) → `Stack[-0x10]`（関数外または未収録） · `WRITE` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cef0`](#insn-00b5cef0) → `00c9b868`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b5cef8`](#insn-00b5cef8) → `01126108`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier33cleanup_notifiers_by_owner_mutex_E` · 推定型 `undefined8`
- [`00b5cf00`](#insn-00b5cf00) → [`00c5aad0`](../00c5a/00c5aad0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aad0` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf0c`](#insn-00b5cf0c) → `00c9b860`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `pointer`
- [`00b5cf14`](#insn-00b5cf14) → `01126110`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `_ZN8firebase15CleanupNotifier27cleanup_notifiers_by_owner_E` · 推定型 `undefined8`
- [`00b5cf18`](#insn-00b5cf18) → [`00b5cf2c`](#insn-00b5cf2c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf24`](#insn-00b5cf24) → [`00b5cf1c`](#insn-00b5cf1c) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf28`](#insn-00b5cf28) → [`00b5cf58`](#insn-00b5cf58) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf3c`](#insn-00b5cf3c) → [`00b5cf58`](#insn-00b5cf58) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf54`](#insn-00b5cf54) → [`00b5cf40`](#insn-00b5cf40) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf60`](#insn-00b5cf60) → [`00b5cf68`](#insn-00b5cf68) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf78`](#insn-00b5cf78) → [`00c5b6a0`](../00c5b/00c5b6a0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5b6a0` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf80`](#insn-00b5cf80) → [`00c57f80`](../00c57/00c57f80.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c57f80` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf8c`](#insn-00b5cf8c) → [`00b5cfc8`](#insn-00b5cfc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cf98`](#insn-00b5cf98) → [`00b5cfc8`](#insn-00b5cfc8) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cfa4`](#insn-00b5cfa4) → [`00b5cfc4`](#insn-00b5cfc4) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cfb8`](#insn-00b5cfb8) → [`00b5cfa0`](#insn-00b5cfa0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cfc0`](#insn-00b5cfc0) → [`00b5cfc8`](#insn-00b5cfc8) · `UNCONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cfd4`](#insn-00b5cfd4) → [`00b5cfe0`](#insn-00b5cfe0) · `CONDITIONAL_JUMP` · `DEFAULT` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cfdc`](#insn-00b5cfdc) → [`00c58010`](../00c58/00c58010.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c58010` · 推定シンボル `None` · 推定型 `None`
- [`00b5cfec`](#insn-00b5cfec) → `Stack[-0x10]`（関数外または未収録） · `DATA` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cff0`](#insn-00b5cff0) → `Stack[-0x20]`（関数外または未収録） · `READ` · `ANALYSIS` · 関数 `None` · 推定シンボル `None` · 推定型 `None`
- [`00b5cff8`](#insn-00b5cff8) → [`00c5aae0`](../00c5a/00c5aae0.md) · `UNCONDITIONAL_CALL` · `DEFAULT` · 関数 `00c5aae0` · 推定シンボル `None` · 推定型 `None`

## 読み取り専用データの取得範囲

Ghidraが定義した境界から先頭32バイトまで取得。型は推定値です。ポインタ、再配置、書込可能領域は取得理由を別記します。

## 読み取り専用データ

- 参照命令 [`00b5cedc`](#insn-00b5cedc)

~~~json
{
  "source": "00b5cedc",
  "target": "Stack[-0x30]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cee0`](#insn-00b5cee0)

~~~json
{
  "source": "00b5cee0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cee4`](#insn-00b5cee4)

~~~json
{
  "source": "00b5cee4",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cef0`](#insn-00b5cef0)

~~~json
{
  "source": "00b5cef0",
  "target": "00c9b868",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b868",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b5cef8`](#insn-00b5cef8)

~~~json
{
  "source": "00b5cef8",
  "target": "01126108",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126108",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5cf00`](#insn-00b5cf00)

~~~json
{
  "source": "00b5cf00",
  "target": "00c5aad0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cf0c`](#insn-00b5cf0c)

~~~json
{
  "source": "00b5cf0c",
  "target": "00c9b860",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "00c9b860",
  "offset": 0,
  "size": 8,
  "datatype": "pointer",
  "capture_state": "pointer_requires_relocation_and_runtime_resolution"
}
~~~
- 参照命令 [`00b5cf14`](#insn-00b5cf14)

~~~json
{
  "source": "00b5cf14",
  "target": "01126110",
  "target_space": "ram",
  "resolution": "defined_data",
  "start": "01126110",
  "offset": 0,
  "size": 8,
  "datatype": "undefined8",
  "capture_state": "not_readonly_initialized_data"
}
~~~
- 参照命令 [`00b5cf18`](#insn-00b5cf18)

~~~json
{
  "source": "00b5cf18",
  "target": "00b5cf2c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf24`](#insn-00b5cf24)

~~~json
{
  "source": "00b5cf24",
  "target": "00b5cf1c",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf28`](#insn-00b5cf28)

~~~json
{
  "source": "00b5cf28",
  "target": "00b5cf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf3c`](#insn-00b5cf3c)

~~~json
{
  "source": "00b5cf3c",
  "target": "00b5cf58",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf54`](#insn-00b5cf54)

~~~json
{
  "source": "00b5cf54",
  "target": "00b5cf40",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf60`](#insn-00b5cf60)

~~~json
{
  "source": "00b5cf60",
  "target": "00b5cf68",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf78`](#insn-00b5cf78)

~~~json
{
  "source": "00b5cf78",
  "target": "00c5b6a0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cf80`](#insn-00b5cf80)

~~~json
{
  "source": "00b5cf80",
  "target": "00c57f80",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cf8c`](#insn-00b5cf8c)

~~~json
{
  "source": "00b5cf8c",
  "target": "00b5cfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cf98`](#insn-00b5cf98)

~~~json
{
  "source": "00b5cf98",
  "target": "00b5cfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cfa4`](#insn-00b5cfa4)

~~~json
{
  "source": "00b5cfa4",
  "target": "00b5cfc4",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cfb8`](#insn-00b5cfb8)

~~~json
{
  "source": "00b5cfb8",
  "target": "00b5cfa0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cfc0`](#insn-00b5cfc0)

~~~json
{
  "source": "00b5cfc0",
  "target": "00b5cfc8",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cfd4`](#insn-00b5cfd4)

~~~json
{
  "source": "00b5cfd4",
  "target": "00b5cfe0",
  "target_space": "ram",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cfdc`](#insn-00b5cfdc)

~~~json
{
  "source": "00b5cfdc",
  "target": "00c58010",
  "target_space": "ram",
  "resolution": "function"
}
~~~
- 参照命令 [`00b5cfec`](#insn-00b5cfec)

~~~json
{
  "source": "00b5cfec",
  "target": "Stack[-0x10]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cff0`](#insn-00b5cff0)

~~~json
{
  "source": "00b5cff0",
  "target": "Stack[-0x20]",
  "target_space": "stack",
  "resolution": "boundary_unknown"
}
~~~
- 参照命令 [`00b5cff8`](#insn-00b5cff8)

~~~json
{
  "source": "00b5cff8",
  "target": "00c5aae0",
  "target_space": "ram",
  "resolution": "function"
}
~~~
